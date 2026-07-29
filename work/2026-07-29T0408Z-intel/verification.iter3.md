**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-07-29T05:51:18Z · ended_at=2026-07-29T06:16:17Z · duration_seconds=1499
**Self-telemetry:** urls_checked=25 · webfetch_calls=6 · bridge_fetches=21 · websearch_calls=2

## Verification report — 2026-07-29T0408Z-intel (iteration 3)

Read cold over all 11 entries plus the run record. Every one of the 25 source URLs on this run's entries
was fetched in this iteration (WebFetch, `fetch_source.py url`, `cisa page`, `cisa-kev`, `bsi-csaf`) —
no sampling. Evidence quotes were checked as literal substrings of the fetched page text; CVE ids and
scores were checked against the per-CVE authority (Siemens CSAF, OpenSSL oss-security, JetBrains CNA
record, ZDI advisory, cveawg), not against roundups. The prior-iteration deltas were walked first.

### Prior-iteration deltas — both verified sound

- **iter-2 F4 (Mirage Kitten NetSetup.log inference).** Kaspersky's page reads: *"NetSetup.log is a Windows
  diagnostic log generated under C:\Windows\debug\ during domain/workgroup join, unjoin, and related
  network setup operations."* The entry now reads "which Kaspersky describes as a diagnostic log generated
  during domain and workgroup join, unjoin and related network-setup operations" — faithful, and no
  residual inference sits inside that citation. **Confirmed fixed.** (Note: the *removal* left a side
  effect on the ATT&CK mapping — see F7, advisory.)
- **iter-2 F4 (run record `entities_added` stale key).** `entities/registry.yaml:3955` carries
  `incident:uvvg-arad-cyberattack-2026-07`; the entry's `entities:` list and the run record's
  `entities_added` now carry the same string; the pre-rename key appears nowhere in `entries/`, `runs/`
  or `entities/` (only in `work/` forensic artefacts, which is correct). All 11 `entities_added` keys
  resolve to exactly one registry record each, and the registry holds exactly 11 records with
  `first_seen: 2026-07-29`. **Confirmed fixed.**

Also re-confirmed independently (not re-litigated below): iter-1 F1 (CISA's ICSA-26-209-01 carries no
exploit-availability statement — verified against the fetched page; the PoC repo exists and is titled
"Command Execution PoC for OpenSSL Stack buffer overflow CVE-2025-15467"); iter-1 F2 (South St. Paul text
is in Cybersecurity Dive, not StateScoop; Braham's "a later notice noted that the plant was back online"
is verbatim); iter-1 F5/F13/F15/F16 (no PoC claim on CVE-2026-0769 anywhere; exactly five entry ATT&CK ids
are absent from Talos's table — T1557, T1098.005, T1543.003, T1003.003, T1021.006, the two others being
sub-technique refinements of tabulated parents; 9.1 is recorded as NVD-assigned in the 2026-07-23 entry;
the 2026-06-11 entry does record CVE-2026-5027 as effectively pre-auth via default auto-login);
iter-1 F11 (Minnesota's second action — physical mode switch to RUN — is verbatim advisory guidance and
does not duplicate the 2026-07-24 entry's single baseline-logic action); iter-1 F6 (all evidence quotes
re-checked as contiguous substrings — the only mismatches are typographic Unicode in the *source*
(curly quotes, U+2011 non-breaking hyphens, curly apostrophes) normalised to ASCII in the entry, which
is not a splice and is not flagged).

### Citation does not support the claim

**F1 — Mirage Kitten: ArcBridge is credited with BridgeHead-only mechanics, in four places, each closed
with a Kaspersky citation.** This is the run's one substantive remaining truth defect. Kaspersky's
ArcBridge section (fetched this iteration, `https://securelist.com/mirage-kitten-new-tools/120811/`)
says only this about ArcBridge: it was first identified in April 2026 in Middle East activity; it creates
mutex `F56E68DA-…`; it carries an embedded config block (C2 host, C2 port, retry/timeout, SSL flag,
implant identifier); *"After initialization, ArcBridge communicates over a WebSocket-style channel and
waits for server-side control messages"*; and it supports two commands, `OPEN:` ("Creates a proxy/tunnel
session to a target selected by the operator") and `DNS:`. The page never associates ArcBridge with
SOCKS5, with an *authenticated* WebSocket, with HTTP 407 handling, with Negotiate/NTLM/SSO, or with a
username gate. Every SOCKS5 mention on the page (three: "the implant functions as a full SOCKS5 tunnel
proxy", "Open a new TCP tunnel to a SOCKS5 target address", "The target address is encoded in SOCKS5
format") sits in the BridgeHead section; the 407/`WinHttpQueryAuthSchemes`/Negotiate-then-NTLM/null-SSO-
credentials logic is BridgeHead's response table; and the 3-character control value belongs to a
*BridgeHead variant* (MD5 C832…), introduced with "Still, it implements the same technique…", inside the
BridgeHead section. The four affected locations:

1. `title:` — "fields NightLedger plus **two WebSocket SOCKS5 tunnelers built to negotiate their way
   through corporate proxies with the victim's own SSO**".
2. `summary:` — "**Two companion tunnelers, BridgeHead and ArcBridge, implement SOCKS5 over an
   authenticated WebSocket** and are engineered for defended networks: on an HTTP 407 **they** query
   available auth schemes, prefer Negotiate over NTLM, and retry with the logged-in user's SSO context.
   **Both gate execution on a 3-character substring** of the lowercased Windows username".
3. Body ¶2 — "**BridgeHead and ArcBridge both build SOCKS5 tunnels over an authenticated WebSocket**, but
   BridgeHead is explicitly engineered for networks that do not simply let traffic out: …
   ([Kaspersky Securelist, 2026-07-28])".
4. Body ¶2 — "**Both tools also refuse to run outside their intended target**: a hardcoded 3-character
   value must appear as a substring of the lowercased Windows username, and the implant exits silently
   otherwise — behaviour Kaspersky reads as evidence of prior internal reconnaissance and per-target
   tailoring of each binary ([Kaspersky Securelist, 2026-07-28])".

The conflation is inherited from the research layer (`work/…/findings.S3.yaml` lines 30–31: "Two companion
WebSocket tunnelers — BridgeHead and ArcBridge — implement full SOCKS5 tunnel-proxy functionality over an
authenticated WebSocket channel and are built to…") and the Phase-4 deep read did not correct it. Remedy:
attribute the proxy-traversal design, the SOCKS5 relay behaviour and the username gate to BridgeHead
(and its variant) only, and describe ArcBridge as what Kaspersky describes — a second WebSocket tunneler
with an embedded C2 config and `OPEN:`/`DNS:` control messages. The entry's headline, Defender takeaway
and Triage lines all stand as written.

**F2 — Mirage Kitten: "signed" vendor binary is not a Kaspersky claim.** The headline says the toolset
"loads under **a signed vendor binary** via RPC delay-load" and body ¶1 says the module is "pulled in
through the normal search order, **under a signed vendor process**, and forwards the expected exports to
the genuine DLL" — the latter inside a sentence closed with a Kaspersky citation. Kaspersky's text says
only: *"appears to be designed for DLL search-order hijacking, targeting a **legitimate**
AppVShNotify.exe binary"* and *"This allows a co-located malicious SspiCli.dll to be loaded while
forwarding expected exports to the **legitimate** DLL."* The page makes no code-signing statement about
`AppVShNotify.exe` anywhere (grep for "sign"/"signature" returns nothing in the article body). The
attribute came from the deep-read return ("loaded under the trusted, legitimately-signed
AppVShNotify.exe process", `work/…/findings.DR2.yaml`), not from the cited page. Low severity, one-word
remedy ("legitimate" for "signed"); it matters because the entry's own Triage line makes signature
checking the discriminator, so a reader takes "signed" as sourced.

### Unsupported / hallucinated facts

**F3 — Run record: the Siemens-source justification over-counts prior citations by one.** Twice in the
published record: `sources_changed` — "Added on evidence rather than speculation: **three published
entries in the trailing 30 days already cite cert-portal.siemens.com**"; and the notes body — "it is a
first-party A-reliability authority **already cited by three published entries**". A repo-wide grep for
`cert-portal.siemens.com` across `entries/` returns exactly three files, one of which is *this run's own*
`2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed.md`. The prior-coverage count that
the word "already" claims is **two**: `2026-07-10/siemens-sicam-8-ssa-229470-firmware-signing-bypass.md`
and `2026-07-18/siemens-ruggedcom-rox-ii-unit42-three-cve-chain.md`. Remedy: "two prior entries, plus
this run's own" — the evidence-based rationale is otherwise intact and the addition is well justified.

**F4 — Run record: the deep-dive rotation enumeration does not describe the window it names.** The notes
say: "Category rotation is clean: no annual-report deep dive in the prior 30 days, **whose picks were
firewall-vpn-rce, other, network-stack-rce, identity-infra and apt-campaign twice**." Scanning
`deep_dive: true` entries for 2026-06-29 → 2026-07-28 gives **13** deep dives:
ransomware-affiliate (06-30), web-app-rce (07-01), cloud-saas (07-02), linux-lpe (07-08),
identity-infra (07-09), firewall-vpn-rce (07-10), apt-campaign (07-13), firewall-vpn-rce (07-18),
other (07-19), network-stack-rce (07-20), identity-infra (07-21), apt-campaign (07-24),
apt-campaign (07-25). The record's six-item list corresponds only to 2026-07-18 → 07-25; it omits seven
picks inside the stated window, and apt-campaign occurred **three** times in 30 days, not twice. The
load-bearing conclusion — no annual-report deep dive in the prior 30 days — is **true** (verified: none
of the 13 is annual-report), and "No deep dive had been published on 26, 27 or 28 July" is also true.
Remedy: either name the window the list actually covers (the prior ~11 days) or complete the enumeration.

**F5 — Run record: the TeamCity publication timestamp is not the one the page carries.** The recency
disclosure states "The TeamCity advisory (**published 2026-07-27T15:09Z**)". The only timestamp on
`https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/` is `2026-07-27T15:20:35+01:00` — i.e.
**14:20:35 UTC**; the string "15:09" appears nowhere on the page, and the `Z` suffix mislabels a
`+01:00` stamp as UTC. The derived claim "roughly 37 to 38 hours before this run began" survives either
way (14:20Z → 04:08:59Z on 07-29 is 37.8 h), and `event_date: "2026-07-27"` on the entry is correct. The
defect is that the record makes a precision claim it cannot support, in the same paragraph where it
correctly cites LegacyHive's structured `datePublished` (verified: `2026-07-27T14:07:50.000Z`, exact).

### Surface contradiction

**F6 — Check Point update: vendor "very specific configuration" vs Rapid7 "a default setting" is never
named.** Rapid7 (fetched this iteration): *"Exploitation requires network access to the Management Server
and for a Trusted Clients configuration that does not restrict GUI clients, which in our testing was a
default setting."* The entry it updates (`2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232`)
records the vendor's own framing: "The precondition is narrow but severe: the Management Server must be
exposed directly to the internet with no Trusted-Clients … restriction — Check Point states this **'only
affects a very specific configuration'**". Those two statements about the same product's shipped state
are in direct tension, and the tension is the most operationally consequential thing in the update
(expected exposure of every unpatched, reachable estate). The update entry gestures at it — "exploitable
as shipped **rather than only when misconfigured**" — without naming the vendor's claim, and the run
record carries no `Contradiction:` line. Remedy: one clause in the entry naming Check Point's framing
alongside Rapid7's finding, or a `Contradiction:` line in § Verification Notes. Nothing in the entry is
false as written; the reader simply cannot see that the vendor said otherwise.

### Editorial / less-is-more flags (advisory)

**F7 — Mirage Kitten `techniques[]`: T1018 lost its basis when the iter-2 fix landed.** `techniques[]`
carries `T1018` (Remote System Discovery). The behaviour Kaspersky documents is command 25, "Gather host
and network information", and command 93's NetSetup.log collection — the clause that plausibly justified
a remote/domain-context reading ("a compact source of Active Directory context") was correctly removed by
iteration 2, and the body now describes no enumeration of *other* hosts. `T1016` (System Network
Configuration Discovery) is the id the surviving body text and source support. Suggest swapping T1018 →
T1016; the other seven ids (T1574.001, T1071.001, T1090, T1572, T1113, T1057, T1082) are all
source-supported.

**F8 — Mirage Kitten: the command list reads exhaustive but drops the execute primitive.** Body ¶1: "16
numeric commands — identity and host/network reconnaissance, process listing and termination, directory
and drive enumeration, file upload and download, screenshot capture, DLL loading, beacon-interval
changes, and collection of the Windows domain-join diagnostic log". Kaspersky's table (verified, 16 rows,
which independently confirms the record's "16, not 13" correction) also contains command 3, "Execute a
process/program" — arguably the most operationally significant entry, plus 27 copy-file, 62 delete-file,
69 terminate-thread. The frontmatter summary hedges correctly ("including"); the body does not.

**F9 — LegacyHive: `tags` assert what the body denies.** `tags: [vulnerabilities, priv-esc, no-patch,
poc-public]` on an entry whose summary says "**It is not a software vulnerability**" and whose body says
"This is not remote, not pre-authentication, and **not privilege escalation from nothing**". `no-patch`
and `poc-public` are apt; the first two tags are topical routing values that an automated consumer reads
as classification. Advisory only — the taxonomy offers no better fit, and the main agent may reasonably
leave them.

**F10 — Registry edge picks one horn of Sophos's disjunction.** `actor:stac4749` carries
`{to: actor:chaos-ransomware, type: collaborates-with, source: 2026-07-29/stac4749-…}`. Sophos states
(verified verbatim): *"Sophos analysts assess with high confidence that STAC4749 was a financially
motivated operation that **either directly deployed ransomware or coordinated with affiliates**"* — a
disjunction; `collaborates-with` asserts the second branch. What the source states unconditionally is
"At least three STAC4749 compromises led to Chaos ransomware deployment", which supports `uses` cleanly.
Suggest `uses`; a typed edge is permanent-ish and machine-read.

**F11 — Siemens entry: the PoC that carries the urgency argument has lab preconditions the entry omits.**
The cited repository (fetched) reproduces command execution only against an OpenSSL 3.4.0 rebuilt with
`-fno-stack-protector -D_FORTIFY_SOURCE=0 -z execstack` and with ASLR disabled
(`echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`), and OpenSSL's own advisory says *"While
exploitability to remote code execution depends on platform and toolchain mitigations, the stack-based
write primitive represents a severe risk."* The entry's "public command-execution proof-of-concept" and
the action item's "a public command-execution exploit … already exists" are accurate but leave a Tier 2/3
reader assessing V7 urgency without that caveat. One clause would settle it. (Not a truth finding: the
PoC is real, public, and does what the entry says.)

**F12 — Langflow: the ZDI timeline reads as one event more than ZDI lists.** "its disclosure timeline
records the report going to the vendor in July 2025, **three follow-ups over the following months, and
finally notice of intent to publish** without a fix". ZDI's Additional Details (verified verbatim) has
four lines total: `07/18/25 – ZDI submitted the report`, `09/11/25 – ZDI asked for updates`,
`10/10/25 – ZDI asked for the fix`, `12/10/25 – ZDI notified the vendor of the intention to publish the
case as a 0-day advisory`. Read strictly, the entry implies 1 + 3 + 1 = five events where the source has
four. Ambiguous rather than plainly false (the "three" does match the three post-report lines), hence
advisory; "two follow-up requests and then notice of intent" removes the ambiguity.

### Coverage — checked, no gap found

Completeness was probed rather than assumed. Two candidate misses surfaced from independent searching and
both turned out to be correctly handled: **Arista VeloCloud Orchestrator CVE-2026-16812 (CVSS 10.0,
actively exploited, reported 2026-07-28)** is already published as
`entries/2026-07-28/cve-2026-16812-arista-velocloud-orchestrator-exploited.md`; and the **Stadler Rail /
Everest CHF 10 M extortion**, which the 28 July French-language Swiss roundup re-reported, is already
published as `entries/2026-07-22/everest-ransomware-stadler-rail-supplier-platform-breach.md`, with the
home-region research return explicitly recording "still not listed on Everest's leak site, no delta".
Run-record coverage claims spot-verified against the repo: 15 essential-tier sources exist in
`sources/sources.json` and all 15 appear across S1/S2 `sources_attempted` ("No miss" — true); exactly one
source was added this run (`siemens-productcert-csaf`, diffed against `HEAD` — the one-candidate cap holds);
JetBrains is genuinely untracked; the French-language Swiss daily (`dcod-ch`) is tracked with
`last_successful_fetch: 2026-07-22`, as stated; the six borderline-drop bullets match the claimed six
drops; the kind split ("five vulnerabilities … three pieces of primary tradecraft research, two incidents
and one periodic report") matches the 11 files exactly; no entry carries `priority: critical`; the two
`check_run.py` dedup warnings correspond precisely to the two entries the record names, and its
description of the 2026-07-24 entry as "that operation's Rust remote-access tool" is accurate. Zero IOCs
across all 11 entries. **Coverage looks complete; no F10.**

### Verdict

NEEDS_FIXES (truth: 5, editorial: 1, advisory: 6)

F1 is the finding that matters: a named tool is credited, in the title and the machine-read summary as
well as the body, with tradecraft the cited lab attributes to a different tool. F2–F5 are small,
individually one-line fixes, but F3–F5 are all statements the published run record makes about itself
that the artefacts do not support. F6 is a genuine divergence the reader should see. The six advisory
items can be left without harm, with F7 the one most worth acting on since it corrupts a derived
mapping surface.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Mirage Kitten (UNC1549) fields NightLedger plus two WebSocket SOCKS5 tunnelers …"
  url_or_quote: "Two companion tunnelers, BridgeHead and ArcBridge, implement SOCKS5 over an authenticated WebSocket and are engineered for defended networks: on an HTTP 407 they query available auth schemes, prefer Negotiate over NTLM, and retry with the logged-in user's SSO context. Both gate execution on a 3-character substring of the lowercased Windows username"
  summary: "F1 — Kaspersky's ArcBridge section (fetched this iteration) describes only a mutex, an embedded C2 config block, a 'WebSocket-style channel' and two commands (OPEN:, DNS:). All SOCKS5 mentions, the HTTP 407 / WinHttpQueryAuthSchemes / Negotiate-over-NTLM / null-SSO-credential logic and the 3-character username gate (a BridgeHead variant, MD5 C832…) sit in the BridgeHead section. Four locations carry the conflation: title ('two WebSocket SOCKS5 tunnelers built to negotiate their way through corporate proxies with the victim's own SSO'), summary (quoted), body para 2 ('BridgeHead and ArcBridge both build SOCKS5 tunnels over an authenticated WebSocket'), body para 2 ('Both tools also refuse to run outside their intended target'), each closed with a Kaspersky citation. Inherited from findings.S3.yaml lines 30-31. Remedy: attribute proxy traversal, SOCKS5 relaying and the username gate to BridgeHead only; describe ArcBridge as Kaspersky does."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Mirage Kitten (UNC1549) fields NightLedger plus two WebSocket SOCKS5 tunnelers …"
  url_or_quote: "loads under a signed vendor binary via RPC delay-load / under a signed vendor process"
  summary: "F2 — Kaspersky says only 'a legitimate AppVShNotify.exe binary' and 'forwarding expected exports to the legitimate DLL'; the page makes no code-signing statement about that binary. 'signed' came from the deep-read return (findings.DR2.yaml: 'legitimately-signed AppVShNotify.exe process'), not the cited page, and sits inside a Kaspersky-cited sentence in the body plus the headline. Remedy: 'legitimate vendor binary/process'."
- code: F4
  category: hallucinated-fact
  section: verification-notes
  item: "runs/2026-07-29/2026-07-29T0408Z-intel — Siemens source-addition rationale"
  url_or_quote: "three published entries in the trailing 30 days already cite cert-portal.siemens.com"
  summary: "F3 — grep across entries/ returns exactly three files citing cert-portal.siemens.com, one of which is this run's own Desigo CC entry. The prior-coverage count the word 'already' claims is two (2026-07-10 siemens-sicam-8-ssa-229470, 2026-07-18 siemens-ruggedcom-rox-ii-unit42). Same over-count repeated in the notes body ('already cited by three published entries'). Remedy: 'two prior entries plus this run's own'."
- code: F4
  category: hallucinated-fact
  section: verification-notes
  item: "runs/2026-07-29/2026-07-29T0408Z-intel — deep-dive rotation note"
  url_or_quote: "no annual-report deep dive in the prior 30 days, whose picks were firewall-vpn-rce, other, network-stack-rce, identity-infra and apt-campaign twice"
  summary: "F4 — the 30-day window (2026-06-29..07-28) contains 13 deep dives: ransomware-affiliate 06-30, web-app-rce 07-01, cloud-saas 07-02, linux-lpe 07-08, identity-infra 07-09, firewall-vpn-rce 07-10, apt-campaign 07-13, firewall-vpn-rce 07-18, other 07-19, network-stack-rce 07-20, identity-infra 07-21, apt-campaign 07-24, apt-campaign 07-25. The six-item list covers only 07-18..07-25 and undercounts apt-campaign (three, not twice). The conclusion 'no annual-report deep dive in the prior 30 days' is TRUE and needs no change; only the enumeration or its stated window does."
- code: F4
  category: hallucinated-fact
  section: verification-notes
  item: "runs/2026-07-29/2026-07-29T0408Z-intel — recency disclosure"
  url_or_quote: "The TeamCity advisory (published 2026-07-27T15:09Z)"
  summary: "F5 — the only timestamp on blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/ is 2026-07-27T15:20:35+01:00 (= 14:20:35 UTC); '15:09' appears nowhere and the Z suffix mislabels a +01:00 stamp. The derived '37 to 38 hours' claim and the entry's event_date 2026-07-27 both remain correct; the LegacyHive stamp in the same paragraph (2026-07-27T14:07:50Z) is exact. Remedy: correct to 14:20Z or cite the local-time stamp."
- code: F9
  category: surface-contradiction
  section: updates
  item: "CVE-2026-16232 root cause — Check Point SmartConsole accepted a caller-supplied SIC distinguished name"
  url_or_quote: "Rapid7 states exploitation needs network access to the Management Server plus a Trusted Clients configuration that does not restrict GUI clients, and that this was a default setting in its testing"
  summary: "F6 — Rapid7's 'in our testing was a default setting' is in direct tension with Check Point PSIRT's own framing as recorded in the entry this updates (2026-07-23: Check Point states this 'only affects a very specific configuration'). The update entry alludes to it ('rather than only when misconfigured') without naming the vendor claim, and the run record carries no Contradiction line. Remedy: name both positions in one clause, or add a Contradiction: line to the run record's notes."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Mirage Kitten — techniques[] T1018"
  url_or_quote: "techniques: [T1574.001, T1071.001, T1090, T1572, T1113, T1057, T1082, T1018]"
  summary: "F7 — T1018 (Remote System Discovery) has no surviving basis: the source supports command 25 'Gather host and network information' and command 93 NetSetup.log collection, and the AD-context clause that plausibly justified a domain/remote reading was removed by iteration 2. T1016 (System Network Configuration Discovery) fits the surviving body text. Advisory: swap T1018 -> T1016."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Mirage Kitten — body command enumeration"
  url_or_quote: "dispatches 16 numeric commands — identity and host/network reconnaissance, process listing and termination, directory and drive enumeration, file upload and download, screenshot capture, DLL loading, beacon-interval changes, and collection of the Windows domain-join diagnostic log"
  summary: "F8 — the dash-list reads as exhaustive but omits command 3 'Execute a process/program' (plus 27 copy-file, 62 delete-file, 69 terminate-thread) from Kaspersky's 16-row table. The frontmatter summary hedges with 'including'; the body does not."
- code: F11
  category: editorial-advisory
  section: research
  item: "LegacyHive: a public Windows technique that redirects a profile's Local AppData …"
  url_or_quote: "tags: [vulnerabilities, priv-esc, no-patch, poc-public]"
  summary: "F9 — the body states 'It is not a software vulnerability' and 'not privilege escalation from nothing', which the first two tags contradict for an automated consumer. No better taxonomy value exists, so the main agent may reasonably leave this."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "entities/registry.yaml — actor:stac4749 relation"
  url_or_quote: "{to: actor:chaos-ransomware, type: collaborates-with, source: 2026-07-29/stac4749-teams-vishing-certificate-pinned-golang-chaos}"
  summary: "F10 — Sophos states a disjunction ('either directly deployed ransomware or coordinated with affiliates'); collaborates-with asserts the second branch. 'At least three STAC4749 compromises led to Chaos ransomware deployment' supports type: uses unconditionally. Advisory: prefer uses."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2025-15467 — Siemens Desigo CC: vendored OpenSSL CMS parsing overflow"
  url_or_quote: "a public command-execution proof-of-concept for the underlying OpenSSL flaw is already published"
  summary: "F11 — the cited repository achieves a shell only against an OpenSSL 3.4.0 rebuilt with -fno-stack-protector -D_FORTIFY_SOURCE=0 -z execstack and with ASLR disabled, and OpenSSL's advisory says 'exploitability to remote code execution depends on platform and toolchain mitigations'. The claim is true; a one-clause caveat would keep the V7 urgency argument honest."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-0769 — Langflow: unpatched pre-auth eval-injection RCE"
  url_or_quote: "its disclosure timeline records the report going to the vendor in July 2025, three follow-ups over the following months, and finally notice of intent to publish without a fix"
  summary: "F12 — ZDI's Additional Details lists four lines total (07/18/25 report, 09/11/25 asked for updates, 10/10/25 asked for the fix, 12/10/25 notified of intention to publish as a 0-day advisory). The entry's phrasing implies three follow-ups PLUS a separate notice, i.e. five events. Ambiguous rather than false; 'two follow-up requests and then notice of intent' removes it."
```
