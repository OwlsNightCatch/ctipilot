---
title: Detecting Timeroasting the Hard Way | Huntress
author: Andrew Schwartz
url: https://www.huntress.com/blog/detecting-timeroasting
hostname: huntress.com
description: Timeroasting leaves no authentication log, but it is not invisible. I reverse MS-SNTP's two authenticator forms to build detection that packet size cannot fool.
sitename: Huntress
date: "2026-11-19"
fingerprint: f619b91182a816d5
---
Most detection rules come from one of two places: a vendor feed or a breach report. There is a third source that stays underused, and it is the one that actually teaches you something. Read the protocol spec, then read the binary that implements it. Not the attacker's tool, and not the vendor's marketing page: the target's own code.

This post is what happened when I did that for timeroasting. The detection you can copy for it today is a volumetric counter of connections to UDP/123 that understands nothing about the protocol. Nobody keys on what actually separates an attacker from a member, and the extended form has no coverage at all. So I reversed the binary to understand the protocol well enough to detect it properly. This is the walk from the bytes in `netlogon.dll` to detection that works against a real fleet. Reversing the crypto that precisely also hands you a working cracker, which is a nice bonus, but detection is the point. That is the "hard way" in the title: there is no public documentation for the extended crypto and no `hashcat` module for it, so you recover both by reading the binary.

## **The roasts you know**

There are three roasts most people can name without thinking.

- **Kerberoasting.** Request a service ticket for any account with an SPN, then crack the encrypted ticket blob offline.
- **AS-REP roasting.** For accounts with Kerberos pre-authentication turned off, grab the AS-REP and crack its encrypted chunk.
- **Timeroasting.** Per [Tom Tervoort](https://cybersecurity.bureauveritas.com/uploads/whitepapers/Secura-WP-Timeroasting-v3.pdf)'s 2023 research, abuse Microsoft's proprietary NTP authentication extension, [MS-SNTP](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sntp/), to make a DC hand you a password-derived MAC for any computer or trust account, with zero authentication, then crack it offline.

## **The form nobody cracks**

Timeroasting's request comes in two authenticator formats, and only one of them has public cracking support: `hashcat` has a mode for the legacy form and none for the other.

MS-SNTP lets a domain client confirm that a time response really came from a DC that knows the client's machine password, without the client authenticating first. The client sends an NTP request that names an account by its Relative Identifier (RID), and the DC answers with a MAC computed over the response using that account's password-derived key. A RID is the tail of an account's Security Identifier (SID), its unique index within the domain; naming a target by that number is all "sweep RIDs" means. Sign for whatever RID I name, no auth required: that is the entire attack surface. Sweep RIDs, collect MACs, crack offline.

The form everyone knows is 68 bytes on the wire, and its MAC is built with MD5. That is what `hashcat` mode `31300` cracks, what [**timeroast.py**](https://github.com/Pennyw0rth/NetExec/blob/main/nxc/modules/timeroast.py) and [**netexec**](https://github.com/Pennyw0rth/NetExec) produce, and what every writeup covers.

The form almost nobody covers is 120 bytes, and it is neither new nor exotic. Microsoft added it to the spec as the preferred option, explicitly because of weaknesses in MD5, and it has been in real traffic for years. `chrony` added handling for it back in 2016, and modern Windows w32time sends it by default, to the point that it broke time synchronization against [Samba AD domain controllers](https://wiki.samba.org/index.php/Time_Synchronisation) (DCs), which do not implement the extended form. The documented workaround is a Windows registry flag, `SignatureAuthAllowed=0`, that forces clients back to the legacy authenticator. Its MAC is built with an SP800-108 key derivation step followed by HMAC-SHA512. Here is the actual gap: the exact byte encoding is not fully documented, and `hashcat` has no module for it, so when you collect the extended MAC the legacy cracker cannot touch it.

**Note:** The two forms are trivial to tell apart on the wire. A 68-byte authenticated NTP packet is the legacy form; a 120-byte one is the extended form. Keep them apart in your head, because which form you have decides whether your cracker works, though as we will see, building detection on size is a mistake.

## **Why a defender should care**

Timeroasting leaves no authentication event for the targeted account. The targeted accounts never log on, so there are no corresponding 4768, 4769, 4624, or 4776 events for logon-based analytics to evaluate. Network-aware products can still inspect the UDP/123 traffic.

That part of the usual claim is true, and it is where the attack earns its reputation for being quiet.

But quiet is not invisible. The DC still receives and answers a burst of UDP/123, and that is visible on the wire and in host network telemetry if you collect it, the half of the story most writeups skip. The extended form adds one wrinkle: if your DC speaks the 120-byte dialect and your collection assumes 68-byte MD5, your cracker produces nothing, and you misread an account as safe because you cracked the wrong format.

So the defender's questions are simple. Can you see the request happen? And if you harvest the MAC, can you actually crack it? We will answer both, but first we have to know exactly what the DC computes, and for that we read its code.

## **The two forms on the wire**

Both forms are a standard 48-byte NTP packet with an authenticator appended. Two fields carry the rest of this post:

- The `KeyIdentifier` at offset 48 (the target RID, little-endian)
- In the extended form, a Flags byte at offset 53 whose 0x01 bit means `USE_OLDKEY_VERSION`

The remaining extended fields are defined in \[MS-SNTP\] and sit at their defaults in a request.

A 68-byte authenticator is the legacy form (48-byte header, 4-byte KeyID, 16-byte MD5 MAC); a 120-byte authenticator is the extended form. The client sends the MAC zeroed, and the DC fills it in and echoes the structure back.

## **Reading the code instead of guessing**

The spec defines the high-level construction: derive K from the password hash, a label, and the RID context, then compute HMAC-SHA512 over the message. It identifies the label as `sntp-ms` and the context as the RID, but the exact byte encoding needed for an interoperable implementation is not fully documented. The prose does not make clear whether the label includes a trailing null, how the RID is serialized, or which PRF drives the SP800-108 KDF. Get any of those details wrong and the cracker produces convincing but incorrect output.

So I did not guess. Everything below is read off the actual binaries from a live, fully patched Windows Server 2025 domain controller (build 26100.33438), in `radare2`. I pulled `w32time.dll` and `netlogon.dll` off the DC over SMB and read them there.

### **Step 1: the crypto is not where you would expect it**

My first assumption was that the signing happened in **w32time.dll**, since that is the service listening on UDP/123. It does not. I grepped the binary for the KDF label and came up empty:

`rabin2 -zzq w32time.dll | grep -i "sntp-ms"`                  -> (nothing)

`rabin2 -zzq w32time.dll | grep -iE "SP800|SHA512"`   -> (nothing)

What `w32time` does import tells the story. Its crypto is delegated to Netlogon through:

```
logoncli.dll:
logoncli.dll  I_NetlogonComputeServerSignature  <- extended (SHA-512)
logoncli.dll  I_NetlogonComputeServerDigest     <- legacy (MD5)
logoncli.dll  I_NetlogonComputeClientSignature
logoncli.dll  I_NetlogonComputeClientDigest
logoncli.dll  I_NetlogonGetTrustRid
bcrypt.dll    BCryptCreateHash / HashData / FinishHash / DestroyHash / GenRandom
```
So `w32time` parses the packet and dispatches. The "Signature" functions are the extended, SHA-512 path; the "Digest" functions are the legacy, MD5 path. The interesting bytes live in **n**`etlogon.dll`.

### **Step 2: the w32time dispatch and the extended-vs-legacy branch**

*Figure 1: the time service imports I\_NetlogonComputeServerSignature and I\_NetlogonComputeServerDigest from logoncli.dll, and a string search for sntp-ms in w32time.dll comes back empty. The signing logic lives in Netlogon, not in* ***w32tim*e**.


Two functions in `w32time` call both compute paths, and the server picks the SHA-512 path or the MD5 path based on the request it parsed. The important finding at this layer: the attacker-controlled fields from the packet, the RID at offset 48 and the flag byte at offset 53, flow through `w32time` only as a RID value and a key selector that get passed down to Netlogon. They are not used as a length, an index, or a buffer size anywhere in the parse.

### **Step 3: NlGetKDFKey, the function that builds the key**

In `netlogon.dll`, the function that derives the KDF key uses its own debug-string name, `NlGetKDFKey`. It builds a `BCryptKeyDerivation` call with the SP800-108 counter-mode HMAC algorithm and three parameter buffers, and the disassembly (Figure 2) pins down the three things a cracker needs. The spec implies a KDF with "a label" and "a context." The bytes say: the PRF is HMAC-SHA512 (the hash-algorithm buffer is L"SHA512"), the label is the 8-byte "`sntp-ms\0`" with the `null` included (`cbBuffer` is 8 for a 7-character string), and the context is the 4-byte RID in little-endian, exactly as it arrived in the packet. Output is a fixed 64 bytes. Every size is constant, and nothing here is attacker-controlled.

*Figure 2. radare2 disassembly of the buffer setup: the sntp-ms label and the L"SHA512" algorithm string being loaded into the BCryptKeyDerivation call that derives the signing key.*

### **Step 4: NlComputeHMACMessageSignatureFromKey, the outer HMAC**

The caller is `NlComputeHMACMessageSignatureFromKey`. It calls `NlGetKDFKey,` then HMACs the message under the derived key: the 64-byte derived key is the secret, the message is the fixed 48-byte NTP header, and the output is 64 bytes. Note the one place a caller-supplied length reaches anything: the input length to that hash call. It is used only as the number of bytes to hash, never as an allocation size or an index, and `w32time` hands Netlogon a fixed 48-byte NTP header for the message. Every other size is BCrypt-derived or the fixed 64. The function error-checks every allocation and every BCrypt call with its own labeled failure path.

The chain is now pinned: the NThash feeds a SHA-512 SP800-108 KDF keyed by the `sntp-ms` label and the RID, producing a 64-byte key, and that key HMACs the 48-byte NTP response. That is everything the detection needs to know about the crypto. The cracker also needs the exact byte layout, which I lay out next to the cracker below.

## **Proving it against a live DC**

Reading bytes gives you a hypothesis; I wanted the DC to confirm it. First, reachability, because the extended form being in the spec does not mean a patched DC answers it. I probed a live computer-account RID with both forms and both key selectors. The result was reproducible five times out of five:

```
                  current key (flags=0)   old key (flags=0x01)
legacy (68B)      68-byte reply           68-byte reply
extended (120B)   silent timeout          120-byte reply (real HMAC-SHA512)
```
So the extended form is live on a fully patched DC, and it returns a genuine nonzero 64-byte checksum that changes every request, because the salt is the NTP response, which moves. The collector emits each old-key response as a single `$sntp-ms-sha512$<RID>$<checksum>$<salt>` line, the format laid out in full in the cracking section below. Because the salt is the live NTP response, no two captures are byte-identical, so the hash line in Figure 3 is one instance of that shape rather than a fixed value worth reprinting here.

*Figure 3: The collector's three-way probe against the DC: a 68-byte legacy reply, an extended current-key request that times out, and an extended old-key 120-byte reply, with one sntp-ms-sha512 hash line produced.*

Then the crypto proof: I wrote a small pure-Python reference (no dependencies) that implements the chain above, recovered the responding account's NT hash in the lab (the NT hash is just MD4 of the password, the long-term key every Windows account carries, and what both the MD5 and SHA-512 MACs are ultimately keyed on), and asked one question: does my code reproduce the DC's checksum from that hash? It does, exactly. The verifier reported the match and told me which parameters won, the 8-byte null-inclusive label and the little-endian RID context, confirmed against live output rather than assumed.

*Figure 4. The reference implementation reproducing the DC's checksum from the account NT hash: the captured wire checksum equals the recomputed HMAC-SHA512, and the 8-byte label and little-endian RID context are confirmed, not assumed.*

A reproducible known-answer test vector (synthetic, not a capture, so it corresponds to no figure) with a known password, safe to publish, so anyone reimplementing the KDF can check their work:

```
password : Summer2026! (example only, not a real account)
NThash   : 41aed72cec76816423703d8e545eea31
RID      : 1104 (arbitrary; the RID is just KDF context)
hash     : $sntp-ms-sha512$1104$a24990178f8f309a190f08c9a8c5000ce126eef19b236b50cc680d592057cd1ec872d3de6b7fdc47d8a865cae2c5c277d8842f3d1a8b7b6bb0c06bbffebb6307$1c0400e90000000800000291564d5450000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f
```
That current-key timeout deserves a note, because my first explanation for it was wrong. I had assumed it was specific to the DC's own never-rotated machine account. It is not. I retested across nine machine accounts, member computers included, and every one behaves the same way: legacy answers, extended old-key answers, extended current-key times out. So it is a property of this DC, not an artifact of one account. I do not have a confident explanation, and since modern Windows clients clearly use the extended form successfully in the wild, this DC's current-key behavior may not be representative, and I cannot rule out the simpler possibility that my collector's current-key request is itself malformed. Either way, I am flagging it as an open observation rather than resting any conclusion on it.

## **Cracking it: the bonus from reversing the KDF**

Detecting the extended form never needed the KDF internals. But with the binary already open, getting the key derivation exactly right is a small extra step that hands you a working cracker.

Here is the construction, straight from the two functions above:

```
NThash   = MD4(UTF-16LE(password))              # NTOWFv1, 16 bytes
K        = SP800-108-CounterMode(
             KI    = NThash,
             PRF   = HMAC-SHA512,
             Label = "sntp-ms\0" (8 bytes, includes the null),
             Context = RID (4 bytes, little-endian),
             L     = 512 bits)                   # 64 bytes, one block
checksum = HMAC-SHA512(K, NTP-response[0:48])    # 64 bytes
```
The SP800-108 fixed input, the way Microsoft's `BCryptKeyDerivation` assembles it (the same layout MS-GKDI uses, which is how I sanity-checked the counter and separator):

```
block(1) = HMAC-SHA512(NThash,
             BE32(1) || "sntp-ms\0" || 0x00 || LE32(RID) || BE32(512))
```
Four ways to get this wrong, every one of which silently breaks a cracker, and I would have shipped at least two if I had trusted the spec text alone:

- The label is 8 bytes including the null, not the 7-byte `sntp-ms` you would type.
- SP800-108 then inserts its own 0x00 separator after the label, so two `null` bytes land in the fixed input, not one.
- The counter and length are big-endian 32-bit, but the RID context is little-endian 32-bit: mixed endianness inside one buffer.
- It is a KDF and then an HMAC, two HMAC-SHA512 passes, not a single HMAC over the message.

Before the tooling, two questions I keep getting, because together they decide how much this should worry you.

### **Is the 120-byte form a different attack?**

No. Same protocol and trigger (unauthenticated MS-SNTP, name an account by RID, collect a MAC, no auth), same targets (computer and trust accounts), same collection (sweep RIDs), same goal. Only the MAC construction changes. Legacy builds its MAC with MD5 over the NT hash and the response; extended builds it with an SP800-108 key derivation and then HMAC-SHA512. Same secret, same request, a different MAC on the wire.

### **Is it harder to crack?**

Yes, in two senses, and only one of them is real cryptographically.

The first is per-guess cost, where it is genuinely harder. Legacy is one MD4 plus one MD5, and MD5 is about as GPU-friendly as a hash gets. Extended is one MD4 plus two HMAC-SHA512 passes (roughly eight SHA-512 compressions), nothing precomputable across guesses since the derived key depends on both the RID and the candidate, and SHA-512's 64-bit operations are deliberately GPU-unfriendly. So it is much slower per guess. I will not hand you a multiplier against Kerberoasting, because that depends on the ticket's encryption type (RC4, mode 13100, versus AES, mode `19700`); benchmark it against `hashcat`'s other SHA-512 HMAC modes on your own hardware.

The second is whether it protects a weak password, and there the answer is barely. Both forms key off the same NT hash, so a weak password falls to either and a random machine secret falls to neither; the MD5-versus-SHA-512 difference only changes the price per guess, not which accounts are roastable. Password entropy is the protection, exactly as it always was.

So why would an attacker reach for the extended form at all, when the 68-byte form is cheaper to crack and has a working `hashcat` mode? Two reasons, neither of which is that it is a better attack:

- First, evasion: on a fleet where legitimate clients already send 120-byte requests, extended traffic blends into the baseline, while the 68-byte tools stick out.
- Second, future-proofing, for a day when Microsoft disables the legacy MD5 path. The "your cracker silently fails" trap is real but narrow: it only catches a tool that requests the extended form and then formats the output as legacy. Whoever collects 120-byte responses can see they are 120 bytes.

Here is the current state of cracking:

- **What** `hashcat` **cracks today**: the 68-byte legacy form, mode `31300`, MD5.
- **What** `hashcat` **cracks for the extended form:** nothing in a released build yet; there is no upstream module. Issue 3629, which produced `31300`, is the MD5 one.

So if you collect the extended MAC today, your options are a custom kernel or a CPU reference implementation. I wrote the reference and used this hash format, matching the existing `$sntp-ms$` convention:

`$sntp-ms-sha512$<RID>$<checksum_hex>$<salt_hex>`
...where the salt is the 48-byte NTP response. For comparison, the legacy form captured off the same DC (`hashcat 31300`):

`1000:$sntp-ms$f3c43f1f39a61012e634983008213633$1c0400e90000000c000002a6564d5450ee667af63d863d9cee66797600000000ee667b146da6b866ee667b146da72a7b`
### **Building the hashcat module**

Since the reference proves the algorithm, the next step is a real `hashcat` module so the extended form can be attacked with the same GPU workflow as the legacy one and deserves the same detection attention. The module below is written and passes `hashcat`'s own self-test on a GPU. The algorithm is DC-verified through the Python reference, and the module plus its OpenCL kernel clear `tools/test.py -m 31350` cleanly across the single and multi vectors at vector widths 1 and 4, and crack a known-password vector end to end. On an Apple M3 Pro the mode benchmarks at 17.6 MH/s (`hashcat -b -m 31350`).

`31350` is not a released `hashcat` mode number. It is a placeholder; the maintainers assign the real one when this goes upstream, so you build it from the source below. Getting the kernel to pass took fixing exactly the byte-level traps this post keeps warning about: the `SP800-108 L` value has to land as the big-endian bytes `00 00 02 00` at the right offset in the KDF message, not as a little-endian word, and the password has to be decoded as real UTF-16LE. Guess either wrong and the self-test fails the same way, the same lesson as the label and the context.

The self-test oracle that `hashcat`'s `tools/test.py` uses to make a known hash (`tools/test_modules/m31350.py`) is the clearest statement of the whole algorithm in a few lines:

```
LABEL = b"sntp-ms\x00"  # 8 bytes, trailing null INCLUDED
def _nthash(word):
    return _md4(utf16le(word, "utf-8"))  # NTOWFv1 = MD4(UTF-16LE(pw))
def _kdf(nt_hash, rid):  # SP800-108 CTR, PRF HMAC-SHA512, single block (L=512)
    fixed = struct.pack(">I", 1) + LABEL + b"\x00" + struct.pack("<I", rid) + struct.pack(">I", 512)
    # BE32(counter=1) label 0x00 sep LE32(RID) BE32(L=512)  <- the byte trap
    return hmac.new(nt_hash, fixed, hashlib.sha512).digest()
def _hash(word, salt_bin, rid):  # checksum = HMAC-SHA512(K, 48-byte NTP response)
    k = _kdf(_nthash(word), rid)
    checksum = hmac.new(k, salt_bin, hashlib.sha512).digest()
    return "sntp-ms-sha512%d%s%s" % (rid, checksum.hex(), salt_bin.hex())
```
The implementation consists of `module_31350.c`, the [m31350-pure.cl](https://m31350-pure.cl) OpenCL kernel, and the [m31350.py](https://m31350.py) self-test oracle. I built the modified hashcat source tree and validated mode `31350` with `hashcat`’s self-test framework:

```
make -j
tools/test.py -m 31350
```
This verifies the compiled host-side module, the OpenCL kernel, and the Python test oracle together.

### **Watching it recover a password**

A module is only interesting if it recovers something. Here it is against a collected extended MAC: the dependency-free reference cracker first, then the same recovery in `hashcat`.

*Figure 5. Recovering a weak machine-account password from a collected extended (SHA-512) timeroast MAC with the pure-Python reference cracker. The crack is entirely offline, no DC contact and no lockout. A pre-created account still on its lowercase-name default falls instantly; a normal random machine secret would not fall to any wordlist.*

*Figure 6. The same recovery in hashcat with the new mode 31350.*

The extended form now cracks with the same tooling as the legacy one, built from the module in this post. This run is on a Kali box against a six-word list, so it finishes before `hashcat` can measure a representative rate; that box benchmarks at about 339 kH/s (`hashcat -b`), while the 17.6 MH/s above is the M3 Pro GPU. The mode number is a placeholder pending upstream assignment.

That is the whole point of the module: the extended form stops being a research curiosity and becomes practical to crack with GPU tooling, although it remains materially slower per guess than the legacy MD5 form. This only matters for accounts whose passwords are guessable in the first place. So the next question is who that actually is.

### **Who is actually at risk**

All of that, the reference implementation, the hash format, the module, is about turning a *collected* MAC into a password. But it assumes you have something worth cracking, and that set is narrower than a sweep's raw length suggests. Run one and look at what actually answers:

*Figure 7. A NetExec timeroast sweep against the lab DC: RID 1000 and the 1166-1195 cluster answer, while the 1001-1165 gaps stay empty, the accounts the DC refuses to sign for.*

*In the image above, a* request straight at user RID 1110 (`tony.soprano`) in that gap times out, confirming the gap is a refusal, not an omission. Every line is the 68-byte sntp-ms legacy form, because NetExec emits only legacy.

**The gaps are the finding.** In that sweep, RID 1000 answers, then nothing until 1166, then a cluster through 1195. The missing RIDs, 1001-1165, and the holes inside the 11xx block, are not users the sweep skipped. They are users the DC *refused to sign for*. You are not looking at a filtered list of the domain; you are looking at the complete set of accounts the DC was willing to answer for, and that set is **computer and trust accounts only**.

Why, in the protocol: the Netlogon signing path (the `ComputeServerDigest/…Signature` functions from Step 1, with trust RIDs resolved via `I_NetlogonGetTrustRid`) produces a MAC only when the named RID resolves to an account carrying a usable machine secret: `UF_WORKSTATION_TRUST_ACCOUNT`, `UF_SERVER_TRUST_ACCOUNT`, or `UF_INTERDOMAIN_TRUST_ACCOUNT`.

For a normal user (`UF_NORMAL_ACCOUNT`) the compute call returns an error and `w32time` simply does not reply. No reply, no MAC, nothing for the tool to print. RID 1000 answered, so it is a machine or trust account; fire a request straight at user RID 1110 (`tony.soprano`) in that gap and the DC stays silent. The gaps are not omissions, they are refusals.

This is the risk point made concrete: timeroasting reaches computer and trust accounts, full stop, which is why the crackable population is the narrow set worth naming (image-built or never-rotated machines, hand-set trusts, non-Windows joins). It is also exactly why targeted timeroasting has to exist: to roast a real user, an attacker with sufficient write access to the user account first flips that user into a machine-looking account, appending a $ to its name and setting its `userAccountControl` to a workstation trust, so the DC will sign for it, then reverts.

Without those changes, a user's RID in this sweep returns nothing. The gaps are your users. It requires permission to change the user’s `sAMAccountName` and `userAccountControl`, and the account changes it requires are loud, so it is a different risk class from the unauthenticated sweep this post is about.

One last tell, and it ties straight to the tooling section: every line here is `$sntp-ms$`, the 68-byte legacy form, because NetExec emits only legacy. On a modern Windows fleet where members normally send extended requests to capable DCs, that is the tooling skew made visible: the collector uses the old format while normal client traffic uses the new one.

## **Can defenders even see this?**

The targeted accounts never authenticate, so the sweep creates no normal authentication events for those accounts. But the request is still a packet on the wire and a connection on a host, and both are collectable. Three sources see it:

- The DC's own Windows Filtering Platform audit (event 5156) logs `w32time` accepting the UDP/123 connection, when that subcategory is enabled.
- Host EDR sees the network connection, and there is already a [public Sentinel detection](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules/blob/main/Sentinel/Sentinel%20Timeroasting%20KQL%20detection.kql) that counts UDP/123 connections per source over `DeviceNetworkEvents`.
- On the attacker's own machine, any process that is not the time service sending UDP/123 to a DC is a high-signal EDR hit.

So the honest framing is not that nobody can see it, it is that nobody is looking at the right telemetry, because everyone reaches for authentication logs first.

And it is worth being precise about what counts as coverage, because the one product that names timeroasting is easy to misread in both directions. Microsoft Defender for Identity ships an XDR alert, "Suspicious SAM Account Name Change" (`xdr_SuspiciousChangeOfSamName`, according to [Defender for Identity alert docs](https://learn.microsoft.com/en-us/defender-for-identity/alerts-xdr)), and invoking timeroasting in it is not wrong. It fires on a `sAMAccountName` change, which is the fingerprint of the targeted variant: the privileged attack where an attacker with sufficient write access temporarily appends a `$` to a user account's name and flips its `userAccountControl` to a workstation trust so the DC will MS-SNTP-sign for it, then reverts.

That rename is real and detectable, and the alert catches it. What the alert does not see is the attack this post is about, the unauthenticated RID sweep of real computer accounts, because that touches no directory object and leaves nothing for an identity product to key on. One clause of the description is genuinely wrong, timeroasting cracks a password offline and does not "brute-force or replay Kerberos tickets," but the timeroasting attribution itself is fair. So the coverage that exists is for the loud, privileged variant; the quiet, unprivileged one that anyone on the network can run still has none.

The harder question is what the good signal is, and here the extended form changes the answer.

**Do not build on packet size.** On an older fleet a 120-byte authenticated request looked rare. On a modern one it is the reverse: Windows clients send the extended form as normal time sync, and it is the 68-byte request that stands out, because both public timeroast tools emit only 68 bytes. Either way, size is a baseline question, not an attack signal, and which size is the odd one out depends on your Windows versions.

**The signal that actually holds, for both sizes and even for a single packet, is the requested RID relative to the source system.** An ordinary domain member normally asks the DC to sign for its own computer account. Resolve the source IP to a computer account through DHCP or DNS and then to its RID, and treat a request for another RID as anomalous. Handle domain controllers separately: during domain-hierarchy time synchronization, a DC can legitimately use a trusted-account RID obtained through Netlogon. For DC sources, compare the request with the expected trust RID or maintain an allowlist. This role-aware check catches a slow, one-RID-at-a-time sweep that no volume threshold would, and it works with both the 68-byte and 120-byte forms.

**Volume is the fallback.** A single source asking a DC to sign for many different RIDs in a short window is a sweep. It is weaker than the own-RID check, because a patient attacker can pace under the threshold, but it needs no IP-to-RID mapping, so it is the easy first rule.

## **Writing the detection, and the bug that ate all four of my rules**

I wrote four Suricata rules and then did the thing I have learned to always do: I ran them through the actual engine instead of trusting that they looked right. Suricata 8.0.7, against a real capture of a sweep: 41 legacy requests and 41 extended requests from one host to a DC.

The engine immediately caught a mistake I would have shipped. I had left C-style `/* ... */` comments inside the rule bodies to annotate them. Suricata has no inline comment syntax, so every rule that contained one failed to load, and the engine told me plainly that zero rules were loaded. Strip the comments.

With that fixed, all four loaded clean and fired. The extended-request rule matched all 41 extended packets and, because it is rate-limited to one alert per source per five minutes, logged a single alert, which is working as designed. The old-key rule matched and logged all 41 old-key requests. The legacy sweep rule fired once on the 25th matching request, exactly where its threshold says it should. Because this sweep advanced to a different RID with each request, that packet also happened to contain the 25th distinct RID, but the rule itself counts packets rather than distinct RIDs. The extended sweep rule behaved the same way on the extended packets.

The `fast.log` evidence:

```
[1:5200003:1] MS-SNTP authenticated-NTP RID sweep (Timeroast) {UDP} 10.x.x.x:42198 -> 10.x.x.x:123
[1:5200001:1] MS-SNTP ExtendedAuthenticator request (possible extended Timeroast) {UDP} ...
[1:5200002:1] MS-SNTP ExtendedAuthenticator USE_OLDKEY_VERSION (extended Timeroast, old key) {UDP} ... (x41)
[1:5200004:1] MS-SNTP extended RID sweep (Timeroast) {UDP} ...
```
That first pass validated the mechanics and taught me the `/* */` lesson, but all four rules were pinned to packet size, and the evidence that modern Windows sends the extended form means most of them do not survive a real fleet. Here is what I would actually ship. Set your own `$DC_SERVERS.`

Start with the volumetric sweep, deliberately size-agnostic so it catches both forms. An authenticated MS-SNTP request to a DC is 68 or 120 bytes; a plain NTP client request is 48, so `dsize` above 56 excludes plain 48-byte NTP requests and retains packets large enough to carry either MS-SNTP authenticator, although other extended NTP traffic can also match, and the `byte_test` on the low three bits of byte 0 keeps it to client-mode (mode 3) requests, not a mode-4 server reply that happens to be large:

`alert udp any any -> $DC_SERVERS 123 (msg:"MS-SNTP authenticated-NTP sweep to DC (Timeroast, either form)"; dsize:>56; byte_test:1,=,3,0,bitmask 0x07; threshold:type threshold, track by_src, count 25, seconds 60; classtype:attempted-recon; sid:5200010; rev:1;)`
Keep the old-key flag, but as a hypothesis to test rather than a verdict:

`alert udp any any -> $DC_SERVERS 123 (msg:"MS-SNTP ExtendedAuthenticator USE_OLDKEY_VERSION"; dsize:120; content:"|01|"; offset:53; depth:1; classtype:attempted-recon; sid:5200002; rev:1;)`
The spec ties that flag to a client-side Key Selector, and clients validate responses against both the current and the previous password, so a legitimate client around a machine-password rotation could plausibly set it. I have not seen a real member do it, but I have not watched enough real extended traffic to rule it out, so capture your own fleet's requests and look. If none of your members ever set the flag, this is your best size-based signal; if some do, demote it.

Both rules load clean and fire in Suricata 8.0.7 on a captured sweep (the volumetric one three times as the threshold rolls, the old-key one once per matching packet) and stay silent on a plain client.

*Figure 8. The two rules I would ship, in Suricata 8.0.7 against a captured sweep: both load clean, the old-key rule (5200002) fires on all 41 old-key requests, and the volumetric rule (5200010) fires 3 times as its threshold rolls.*

Do not ship a rule that simply alerts on a 120-byte request. On a modern fleet that fires on every Windows member doing normal time sync. It is a baseline measurement, not an attack signal.

The durable detector is not a Suricata rule at all, because the question that separates attacker from member (is this RID the sender's own?) needs an IP-to-account mapping Suricata does not have. Do it in Zeek or your SIEM: for each authenticated NTP request to a DC, pull the RID from offset 48, resolve the source IP to a computer account (DHCP or DNS, then LDAP to its `objectSid` and RID), and alert when the requested RID is not the source's own. That catches a single packet, a slow sweep, and both forms, and it does not depend on which size your fleet treats as normal.

Here is that check as a skeleton. The comparison is trivial; the work is the enrichment, a source-IP-to-own-RID table refreshed out of band from DHCP or DNS plus an LDAP lookup of each host's `objectSid.`

```
# For each authenticated MS-SNTP request to a DC:
on UDP packet to DC:123 where len(payload) in {68, 120}   # 48 = plain NTP, ignore
  and (payload[0] & 0x07) == 3:                            # client mode 3, not a server reply
    requested_rid = le32(payload[48:52])                   # KeyIdentifier, little-endian
    own_rid       = ip_to_rid[src_ip]                      # enrichment: DHCP/DNS -> LDAP objectSid -> RID
    if own_rid is None:
        alert("authenticated MS-SNTP from a host with no RID mapping")   # triage, not a verdict
    elif requested_rid != own_rid:
        alert("host asked the DC to sign for a RID that is not its own") # the durable signal
```
One honest caveat on wiring this to Zeek: the stock `ntp_message` event parses standard NTP and never surfaces the MS-SNTP `KeyIdentifier`, so you reach offset 48 with a small Spicy analyzer or raw-payload access, not three lines of script. Getting the RID off the wire and keeping the IP-to-RID table fresh is the real work; the mismatch test is the easy part.

### **Where these rules will lie to you**

Measure your own 68-versus-120 baseline before you alert on either size, treat the volumetric rule as the weak first pass that a paced attacker or a NAT'd source can fool and the own-RID check as the one that holds, and baseline the old-key flag before you trust it.

## **Fingerprinting the tools, and the rule not to write**

I ran the two public timeroast tools against a DC in the lab, SecuraBV's `timeroast.py` and `timeroast-ng`, and diffed their packets against a real NTP client byte for byte, to see whether there is a tool fingerprint worth keying on. There is, with one trap.

The trap first, because it is the tempting rule and it is wrong. Do not alert on a zero 16-byte MAC in the request. By the MS-SNTP design, the client sends its request with the crypto-checksum zeroed and the DC computes the MAC in the response. That is the whole point of the protocol: the client is asking the DC to prove it knows the password. A legitimate authenticated domain member sends exactly the same 68-byte request with a zero MAC, so a rule on that fires across your whole fleet. The attack is not in the shape of a single request; it is in the sweep and in cracking the response.

What holds up is tool-independent: both tools walk RIDs sequentially from a single source, reusing one ephemeral port, for RIDs that are not the sending host's own machine account. That is exactly the behavior the own-RID and volumetric rules already catch.

A supporting field tell is the transmit timestamp: both tools send a constant or all-zero value on every packet, because they do not care about time, while a real client's changes every request. The same timestamp repeated across many authenticated NTP requests from one source is a reasonable anomaly if your tooling can hold cross-packet state.

There are also byte-exact header signatures per tool, which ship in the rule file with this post. I validated that they fire on the tool captures and stay silent on a real `chrony` client, but a one-line edit to either tool breaks them, so keep them for telling which tool, not for coverage.

*Figure 9. tshark comparison of a timeroast.py request and a genuine chrony request, with the transmit-timestamp bytes and byte 0 highlighted.*

One point flips the usual intuition: the common tools emit only the 68-byte legacy form. The two I captured, SecuraBV's `timeroast.py` and `timeroast-ng`, and NetExec's `timeroast` module all produce legacy hashes, and `timeroast-ng` even ships an extended class that is not wired into its CLI. [KerbWolf](https://strongwind.dev/KerbWolf/commands/kw-timeroast/) is the exception, claiming 120-byte extended support, though I did not capture it.

On an older fleet that legacy skew is unremarkable. On a modern fleet, where real members send 120-byte requests, it means the tools are the ones sending the odd-sized packet, so a 68-byte authenticated request from a host whose Windows version should be speaking extended is itself worth a look. That is the baseline flip from the detection section made concrete; on a modern fleet, hunt the legacy request, not the extended one.

## **What this is not: the machine-account abuse next door**

If you run Active Directory detections, you are probably already watching machine accounts for a different reason. They get created or hijacked, through resource-based constrained delegation or shadow credentials, then authenticate around the domain and enumerate shares on a cadence. That is a real and common funnel, and it is worth keeping it firmly separate from timeroasting in your head, because the two look nothing alike in your logs and people keep conflating them.

Timeroasting uses no credentials. It is unauthenticated UDP/123, it produces no Kerberos logon (no 4768 or 4769 events) and no share access (no 5140 or 5145 events) for the accounts it targets, and it is pure offline recon. The delegation funnel is the opposite: It is all authenticated activity, it generates exactly those account and share events, and it is account takeover rather than recon. A timeroast might precede a later takeover, but the roast itself is invisible to your account-lifecycle rules, and your account-lifecycle rules are invisible to the roast.

The practical triage: if you see a machine account authenticate and then spray shares, that is delegation abuse, not timeroasting, and it belongs to a separate correlation rule. If you see sequential RID sweeps on UDP/123 with no matching logon activity, that is the roast. Do not let the two stories contaminate each other's detection logic.

And one more thing it is not, because the comparison comes up constantly: Timeroasting is not a stealthier DCSync. DCSync requires directory-replication rights, which are normally held by highly privileged accounts but can also be delegated. It pulls account hashes directly and can trigger replication auditing, when configured, as well as Microsoft Defender for Identity's DCSync detection.

.Timeroasting is something you do when you are nobody; it yields a crackable MAC for weak machine accounts and nothing more. They are not substitutes, so comparing their stealth is comparing a lockpick to already holding the key. The honest neighbors for timeroasting are the other roasts, Kerberoasting and AS-REP roasting.

## **Timeroasting and Microsoft Defender for Identity**

Microsoft Defender for Identity ships a catalog of directory and Kerberos detections ([Defender for Identity alerts reference](https://learn.microsoft.com/defender-for-identity/alerts-overview)). During this testing, none of them fired on timeroasting. Across eleven runs over five hours (with the sensor's detection pipeline confirmed live by a control DCSync that MDI flagged as a high-severity replication alert within roughly an hour), the MS-SNTP traffic produced no Defender for Identity alert.

Microsoft documents an alert named "Suspicious SAM Account Name Change" (`xdr_SuspiciousChangeOfSamName`). Its published description reads: "Detected a suspicious change of the SAM account name, which may indicate an attempt to exploit Kerberos authentication via NTP time manipulation (Timeroasting)..." ([Defender for Identity XDR alerts](https://learn.microsoft.com/en-us/defender-for-identity/alerts-xdr)). The description and the trigger describe different things. The alert fires on a change to a `sAMAccountName`, a directory modification recorded in Windows event 5136.

Timeroasting is a separate technique that abuses the authenticated MS-SNTP reply, where a domain controller signs an NTP response with a machine account password hash keyed by RID, so a client can collect those hashes and crack them offline. Timeroasting changes no account name, manipulates no time, and reads no directory object. The same description then adds "brute-force or replay Kerberos tickets" and maps to Kerberoasting ([<u>T1558.003</u>](https://attack.mitre.org/techniques/T1558/003/)), a third technique again. A reader who takes the text at face value would expect this alert to cover timeroasting, while the trigger covers a SAM account name change.

The takeaway is narrow: The alert that names timeroasting fires on a directory change, and the technique it names leaves no directory footprint, so the two do not line up. For visibility into timeroasting itself, log the NTP requests as shown earlier rather than treating this alert as coverage for the technique.

## **In summary**

MS-SNTP has two authenticator formats. Only the legacy MD5 form has public cracking support, while modern Windows clients normally use the SP800-108 and HMAC-SHA512 form when synchronizing with capable domain controllers.

I read `netlogon.dll` and `w32time.dll` to get the key derivation exactly right, down to the null byte in the label, the little-endian RID context, and which function in which DLL does what, and I proved it against live DC output instead of trusting the spec text. I established that `hashcat` cracks only the legacy form, and shipped a verified reference implementation and a hash format for the extended one, plus a `hashcat` module that passes the tool's own self-test on a GPU and now only needs its real mode number assigned upstream.

And I worked out what actually detects this, which turned out not to be packet size, because modern members send the extended form, but whether a host is asking the DC to sign for an account other than its own, with a size-agnostic volumetric rule as the easy fallback, both engine-validated where they could be.

The real value is not any single rule. It is the habit of reading the target's own code when the attacker's tool and the vendor's doc both leave a gap, then validating every claim against a live system and a real engine before you believe it. The extended form is live on patched domain controllers today, and your modern members already send it, so baseline which size is normal in your environment and detect on the one thing that does not move: a host has no business asking a DC to sign for anyone's machine account but its own.

## **Appendix: adjacent techniques**

These two techniques sit next to timeroasting rather than inside it. Neither is the unauthenticated sweep the post is about, but both reuse the same Netlogon signing path, and the detection mirror for each is the own-RID logic from the detection section.

### **DigestRoast: the same digest over a different pipe**

While reversing the signing path, one detail stood out. The function that builds the legacy MD5 MAC, `NetrLogonComputeServerDigest`, is a documented MS-NRPC method (`opnum 24`), callable directly over the **\PIPE\netlogon** named pipe. Feed it a RID and a message, and the domain controller returns `MD5(NThash, message)` keyed by that account: the same construction timeroast collects over UDP. I call this "DigestRoast," and the framing matters up front: DigestRoast is a sister to timeroast, not a new attack.

The construction is byte for byte the legacy timeroast MAC. Reading `NlComputeMd5Digest` in `netlogon.dll`, the DC hashes the 16-byte NT hash first, followed by the caller-supplied message, producing `MD5(NThash followed by message)`. This order matches the MS-NRPC specification. Because the layout matches, a captured DigestRoast digest cracks with the existing `hashcat` mode `31300`, with the chosen message in the salt slot. There is no new module and no new crypto here.

*Figure 10. digestroast.py calling* **o*pnum 24*** *for the domain controller machine account. The DC returns the New and Old message digests, and the tool prints a ready-to-crack $sntp-ms$ line for hashcat mode 31300.*

Two things separate DigestRoast from timeroast:

- The transport is MS-NRPC over TCP 445 rather than MS-SNTP over UDP 123.
- The access requirement, the part that keeps DigestRoast from being an attack, is privileged: `opnum 24` is gated by `NetpAccessCheck2` for a desired access of 0x10, which requires `Builtin\Administrators` on the domain controller.

Three live calls confirm the gate: a `null` session and a low-privileged user each return 0x5, and a domain administrator returns 0x0. If you can already call `opnum 24`, you already hold the domain, and you would pull the hash with DCSync rather than crack a MAC. So DigestRoast earns a footnote, not a section of its own.

DigestRoast's one defensive wrinkle is the pipe it uses. It pulls password-derived material down `\PIPE\netlogon`, not the `DRSUAPI` replication interface a DCSync detection watches, so the 4662 signatures never fire. The same is true of its **netsync** relatives `NetrServerPasswordGet`, `NetrServerTrustPasswordsGet`, and `NetrServerGetTrustInfo`. The event that does see it is a 5145 named-pipe access for `\PIPE\netlogon` (Figure 13), which is off by default. Enable Detailed File Share auditing and watch the Netlogon pipe.

*Figure 11. The construction proven end to end. DCSync recovers the machine account NT hash, and MD5 of that NT hash followed by the chosen message reproduces the exact digest opnum 24 returned, confirming MD5(NThash followed by message) and the hashcat 31300 format against live output rather than the spec text.*

Sweeping a RID range collects the roastable set directly: machine and trust accounts answer and users return an error. Pass the DC NetBIOS name to the server-name argument, since an IP returns `ERROR_INVALID_COMPUTERNAME`, and pad the signed message to 48 bytes so each digest is written as a `hashcat 31300` line (mode `31300`'s salt is the 48-byte NTP response, so a shorter message will not load).

*Figure 12. DigestRoast sweeping RIDs 1000-2000 over MS-NRPC opnum 24. Nine machine and trust accounts answer and users do not, so the output is already the roastable set, the same machine/trust-only population timeroast sees over UDP/123, here over the Netlogon pipe. The --pad48 flag signs a 48-byte message so each returned digest is written straight out as a hashcat -m 31300 line, with that 48-byte message sitting in the salt slot.*

*Figure 13. The event that does see DigestRoast: a 5145 \PIPE\netlogon access (Share \\\\\*\IPC$, Relative Target Name netlogon) from labadmin at 10.0.1.100. The credential egress rides the Netlogon pipe, and 5145 for named pipes is off by default, so Detailed File Share auditing has to be enabled before this event appears at all.*

### **Trustroasting: roasting the trust, and the targets that do not rotate**

A trust account is a machine-shaped account. An interdomain trust stores its secret in a user object whose `userAccountControl` carries `UF_INTERDOMAIN_TRUST_ACCOUNT,` and the domain controller signs an MS-SNTP reply for its RID exactly as it signs for a workstation. So a trust answers a timeroast sweep, and it answers DigestRoast over `opnum 24`, with the same MD5 construction and the same `hashcat` mode `31300`. A cracked trust account hands you not one computer but the inter-realm trust key, which forges referral tickets across the trust.

The catch is that the secret has to be crackable: a random rotating trust password is as uncrackable as any machine secret, so this pays off only against the weak or non-rotating cases named below. Tom Tervoort named this "Trustroasting" in his original work, so the technique is not new. What is missing is the tooling: NetExec sweeps a RID range and never identifies which RIDs are trusts, and nothing public does it over RPC or pairs it with the triage below.

There is a second path to the same trust secret, and it is pure Kerberos. [<u>Adam Chester described inter-realm key roasting in 2019</u>](https://blog.xpnsec.com/inter-realm-key-roasting/). Any authenticated user can request a cross-realm referral ticket for the trusted realm, and the ticket comes back encrypted under an inter-realm trust key. Capture that referral, format it as a `krb5tgs` record, and crack it with `hashcat` mode `13100` when the trust uses RC4. A weak trust password can therefore be attacked through three paths: MS-SNTP, MS-NRPC opnum 24, and a Kerberos referral. They test guesses against the same underlying trust password, but they do not necessarily use the same cryptographic key. RC4 uses the NT hash directly, while AES trust keys are derived differently.

The reason most of this does not pay off is password entropy and rotation. Windows-managed machine and trust secrets are normally long random values and generally rotate on roughly a thirty-day cycle. A captured MAC remains available for offline cracking, but a password recovered from it may no longer be current after rotation, and Windows can retain the previous secret during rollover. Thirty days is therefore not a hard validity limit. Random machine and trust passwords are unlikely to crack, while weak or non-rotating secrets remain the meaningful targets.

The accounts worth naming are the ones that break that defense. The Seamless SSO account `AZUREADSSOACC` does not rotate on its own, so a crack of it stays valid, and its key forges SSO tickets into Entra. A computer account created with the legacy "Assign this computer account as a pre-Windows 2000 computer" option carries `PASSWD_NOTREQD` and receives a predictable initial password based on the lowercase computer name without the trailing `$`, truncated to 14 characters. If the machine never joins and changes that password, recovery is a guess rather than a crack.

Any machine whose `pwdLastSet` is far past the rotation window has stopped rotating for some reason worth investigating. Trustroast enumerates trusts, trust accounts, and machines, triages every one of them by `pwdLastSet` age, flags `AZUREADSSOACC`, pre2k, and non rotating accounts, and roasts the set.

*Figure 14. trustroast.py identifies NEWYORK$ as the interdomain trust account (RID 1187), not a machine account, and collects it over MS-SNTP as a hashcat 31300 line. This is collection, not recovery: unlike DCSync, which requires directory-replication rights, or lsadump::trust /patch, which requires administrative code execution on a domain controller, both of which recover the trust key directly, timeroasting gets only a password-derived MAC you must crack. A random rotating trust secret like this one (pwdAge 14d) will not crack, so the value here is unauthenticated enumeration plus the triage in the next figure, which flags the non-rotating trusts where a crack is actually feasible.*

## **References**

### **Research and background**

- Tom Tervoort (Secura), [*Timeroasting, Trustroasting and Computer Spraying*](https://cybersecurity.bureauveritas.com/uploads/whitepapers/Secura-WP-Timeroasting-v3.pdf) (2023 whitepaper)
- Secura / Tervoort, [original Timeroast scripts](https://github.com/SecuraBV/Timeroast)
- offsecdeer, *Targeted Timeroasting: Stealing User Hashes With NTP*
- Adam Chester (XPN), [*Inter-Realm Key Roasting*](https://blog.xpnsec.com/inter-realm-key-roasting/) (2019)
- The Hacker Recipes, [Timeroasting](https://www.thehacker.recipes/ad/movement/kerberos/timeroast)
- HackTricks, [Timeroasting](https://hacktricks.wiki/en/windows-hardening/active-directory-methodology/TimeRoasting.html)
- RadiantSec, [Timeroast](https://radiantsec.io/docs/kerberos/timeroast/)

### **Tooling**

- [timeroast-ng (MatrixEditor)](https://github.com/MatrixEditor/timeroast-ng)
- [NetExec](https://www.netexec.wiki) timeroast [module](https://github.com/Pennyw0rth/NetExec)
- [KerbWolf](https://strongwind.dev/KerbWolf/commands/kw-timeroast/) (legacy 68-byte plus 120-byte extended SHA-512)

### **Protocol specifications**

- [\[MS-SNTP\] NTP Authentication Extensions](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sntp/)
- [\[MS-SNTP\] Authentication Request Behavior (client request generation and validation)](https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-sntp/478bf16b-78a9-4aa0-92c6-f798174dd119)
- <u>\[MS-NRPC\] Netlogon Remote Protocol</u>
- [\[SP800-108\] NIST Recommendation for Key Derivation Using Pseudorandom Functions](https://csrc.nist.gov/files/pubs/sp/800/108/final/docs/sp800-108-nov2008.pdf)

### **Cracking**

- [hashcat issue #3629](https://github.com/hashcat/hashcat/issues/3629) (mode 31300, legacy MD5; no module for the extended form)
- [John the Ripper issue #5238](https://github.com/openwall/john/issues/5238)

### **Detection**

- [SlimKQL, *Sentinel Timeroasting KQL detection*](https://github.com/SlimKQL/Hunting-Queries-Detection-Rules/blob/main/Sentinel/Sentinel%20Timeroasting%20KQL%20detection.kql) (volumetric over DeviceNetworkEvents)
- [Microsoft Defender for Identity XDR alerts](https://learn.microsoft.com/en-us/defender-for-identity/alerts-xdr) (the *Suspicious SAM Account Name Change* alert catches the targeted, account-rename variant, not the unauthenticated sweep)

### **Evidence that the extended form is long-standing and sent by modern Windows**

- chrony, *ntp: detect MS-SNTP packets* (adds the extended AUTH\_MSSNTP\_EXT case, 2016)
- [Samba bug #14757](https://bugzilla.samba.org/show_bug.cgi?id=14757) (ntp\_signd and the extended authenticator)
- [Samba AD DC time-sync breakage](https://wiki.samba.org/index.php/Time_Synchronisation) from Windows sending the extended authenticator by default, and the SignatureAuthAllowed=0 client workaround (independently reported by Univention, Zentyal, and Red Hat)

### **Mitigation**

Use Microsoft's [<u>Windows Time Service Tools and Settings</u>](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings) to configure the domain time hierarchy, and limit access to UDP/123 on domain controllers to trusted networks that require it. Keep [<u>automatic machine-account password rotation</u>](https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/domain-member-maximum-machine-account-password-age) enabled, remediate predictable pre-Windows 2000 computer-account passwords, and monitor authenticated NTP requests for anomalous sources and RIDs. If Seamless SSO is enabled, follow [<u>Microsoft's guidance to roll over the AZUREADSSOACC Kerberos key at least every thirty days</u>](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sso-how-it-works).

## **Thanks**

To Tom Tervoort for the original timeroasting research this builds on, and to the KerbWolf, timeroast-ng, and NetExec maintainers, whose tooling surfaced the extended form in the first place and gave me something to reverse against.

Special thanks to [Susannah Matt](https://www.huntress.com/authors/susannah-matt) for her help reviewing, formatting, and publishing this post.
