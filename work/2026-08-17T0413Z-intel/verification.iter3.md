**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-17T05:03:42Z · ended_at=2026-08-17T05:13:59Z · duration_seconds=617
**Self-telemetry:** urls_checked=6 · webfetch_calls=5 · bridge_fetches=6 · websearch_calls=3

## Verification report — 2026-08-17T0413Z-intel (iteration 3, confirmation pass)

Read cold. Iteration 2's CLEAN was not used as a starting point: both entries and the run record were
re-read end to end, all six cited URLs were **re-fetched live** in this iteration (not read from the run's
saved captures), and every evidence quote was string-matched against the live page body rather than
eyeballed. Coverage completeness was re-derived independently (feeds, KEV, NCSC-CH, targeted searches)
rather than accepted from the run record's telemetry.

### What was checked, and how

**Transport / liveness.** All six source URLs returned HTTP 200 under a desktop-Chrome UA with redirects
followed, and every one lands on a specific dated article — no homepage, listing or category page:

- `https://www.huntress.com/blog/akira-hits-safe-mode-ransomware-rebooting-around-edr` (200)
- `https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/` (200)
- `https://www.theregister.com/research/2026/08/12/akira-ransomware-scum-blocked-victims-security-tools-and-broke-their-own-encryptor/5286515` (200) — the unusual `/research/…/<id>` path shape was checked explicitly; it resolves to the real bylined article (Jessica Lyons, 12 Aug 2026), not a redirect stub or index.
- `https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/` (200)
- `https://thehackernews.com/2026/08/new-patchcord-backdoor-targets-afghan.html` (200)
- `https://securityaffairs.com/197266/intelligence/apt36-suspected-in-patchcord-espionage-campaign-using-google-sheets-c2.html` (200)

**Citation dates (F3(e)).** Huntress 2026-08-12 (visible dateline) ✓; The Register "Wed 12 Aug 2026" ✓;
BleepingComputer 13 Aug 2026 ✓; Acronis JSON-LD `"datePublished":"2026-08-13T07:45:00.000000Z"` ✓;
The Hacker News 13 Aug 2026 ✓; Security Affairs 16 Aug 2026 ✓. All six `sources[].date` values match. The two
date corrections iteration 1 applied hold against the live pages.

**Evidence quotes (F4).** All eight `evidence[]` quotes were matched as contiguous substrings of the live
page text after tag-stripping. The Huntress detection-guidance quote ("Alert on boot-configuration changes
and Safe Mode boots: msconfig.exe / bcdedit activity, Kernel-Boot EID 27 …") matches the page exactly; the
only difference is a space the page emits around an inline `<code>BootMode=2</code>` element, which is a
markup artifact, not a splice — the quote is copyable from the rendered page unchanged. Not a defect.

**Adjacency sweep (F3(d)).** Both entries cite only their primaries inline (the corroborators appear in
`sources[]` only), so every inline clause was checked against its primary's full body. Verified against
Huntress: 03:45 UTC spray start on 4 August against multiple usernames from several external IPs; the
~7-minute gap to the 03:52:42 success; "no multi-factor authentication (MFA) in front of it"; "predates any
hands-on-keyboard action by nearly two hours"; RDP to the DC, elevated `cmd.exe`, full-property
`Get-ADUser`/`Get-ADComputer` to `C:\ProgramData`; `$formatenumerationlimit = -1` and the four-item
truncation rationale; WinRAR installed mid-intrusion, "the same WinRAR invocation Huntress documented in the
SonicWall campaign", exfil to cloud object storage; AnyDesk as a service doing "double duty"; the
`reg.exe add … \SafeBoot\Network\AnyDesk` write; msconfig at 06:29:21; Kernel-Boot 27 `SAFEBOOT:NETWORK` /
Kernel-General 12 `BootMode = 2`; Defender EID 3002 "seconds into the Safe Mode boot"; encryptor at
06:34:29 with System EID 26 virtual-memory errors and the powershell.exe guard-page failure at 06:36:34;
Defender scan detection 07:43:50 with repeated cleanup failure; reboot out 08:10:38 and quarantine 08:12:28;
the "more physical memory or a larger page file … retool the encryptor" caveat; the agent-coverage line.
Verified against Acronis: five `.lnk` locations incl. taskbar / Quick Launch / Start Menu / both desktops;
`IShellLinkW` + `IPersistFile`; the three-browser target set, the `.backup` copy, the preserved icon via
`SetIconLocation`, the silent real-browser launch; `VirtualAlloc` → `PAGE_EXECUTE_READ` via `VirtualProtect`
→ `CreateThread`; SHEETCORD's `powershell -Command` with script-block wrapping vs PATCHCORD's `cmd.exe /c`;
"significantly less system information"; six browsers adding Brave, Opera, Vivaldi; the generated
`temp_update.vbs` instead of COM; the Startup-folder VBScript with hidden window plus the `HKCU` Run key
written via `reg.exe`; HACKERAI on the cluster's earliest domain (defence[.]cgda[.]site, "the earliest domain
in the infrastructure cluster") moving tasking and exfiltration to GitHub Gists; the March 2026 India
energy-sector campaign behind the NHPC Fuel Conservation Client lure and its full anti-analysis list
(VirtualBox/VMware handles, processor and RAM floors, `IsDebuggerPresent` + PEB flag, TCP scan for
proxy-tool ports, hardcoded analysis-process list, cursor monitoring, randomised 30–90 s sleep "designed to
exhaust sandbox execution timeouts without raising process-termination alerts"); all four attribution
indicators; the SilverFox/SuperShell fingerprint that Acronis declines to elevate.

The **chronology wording** iteration 1 corrected reads correctly against the live page: the entry says "a
different PATCHCORD variant appears in what Acronis calls an earlier campaign … and it carries an
anti-analysis suite the Afghan-telecom sample does not", which is exactly the source's own dual framing
("an earlier campaign, observed in March 2026" / "anti-analysis techniques which were not present in the
earlier sample"). No inversion remains, and no over-correction was introduced.

**Quantifiers (F14).** "first observed use" / "the first reported tie to Akira that Huntress has observed"
is the source's own wording ✓. "under five hours" (Defender takeaway) is arithmetically true from the
source's own cited timestamps (03:52:42 → 06:34:29) and matches BleepingComputer's independent "within five
hours" framing — conservative, not inflated. "three previously undocumented implants", "three distinct C2
channels", "five locations", "three browsers to six", "30-to-90-second sleep", "moderate confidence",
"medium confidence" all carry to the source verbatim.

**Analytical links (F13).** The APT36 link is carried at the lab's stated level in headline, summary,
`sourcing_note`, body and registry edge ("overlaps with … or a closely related Pakistan-linked threat
actor", never "attributed to"). The SilverFox infrastructure fingerprint is reported *as* a link the lab
declines to draw, and creates no registry edge. No connection is asserted that a cited source does not make.

**Name collisions (F15).** SHEETCORD / SHEETCREEP / HACKERAI are checked against the 14-day prior-coverage
index and the registry: no prior entity of any of those names, and no defender-tool/attacker-tool inversion.
`actor:apt36` is registered with the `Transparent Tribe` alias, and the pre-existing
`campaign:operation-xenofiscal-sidecopy` record (which already named SideCopy/APT36 in prose) now carries an
`attributed-to` edge sourced to its own 2026-06-03 entry — the entity-linking gap is closed, not duplicated.

**Frontmatter ⇔ body (F4b).** Both summaries stay inside what the bodies and sources support (no
"exploited" overclaim; the Akira summary explicitly carries the encryptor *failure*). `event_date` equals
each primary's publication date (2026-08-12 / 2026-08-13). `affected_products` name only products the
sources name. `techniques[]` ids all map to behaviours the bodies describe and the sources support, and the
pinned-dataset check passes (ATT&CK v19.2, 2 entries consistent). `verification: single-source` with a
`sourcing_note` naming the one-assessor / three-publisher situation is correct on both, and the run record
carries the matching single-source line — no F12.

**Priority / relevance (5, 5b).** `high` on the Akira entry is right: a named, dated defence-evasion step
from an operator with confirmed Swiss victims, with boot-configuration telemetry a hunter can use this week;
it does not clear the stop-everything `critical` bar (no new CVE, no imminent mass exploitation) and is not
under-alerted. `notable` on the espionage cluster is right: no home-region victim, but the entry earns its
place on transferable tradecraft (C2 terminating on Google- and GitHub-owned endpoints; browser-shortcut
persistence) and says so explicitly rather than being framed around the victim list.

**Actions (F18).** One action on the Akira entry — a concrete, start-now retrospective sweep for
Kernel-Boot 27 / Kernel-General 12 and SafeBoot allow-list writes naming remote-access tooling, with the
"no change ticket ⇒ treat as intrusion" decision rule attached. Self-contained, derived from this finding's
own mechanics, not generic, not hedged, not a duplicate of any in-window action. Empty `actions[]` on the
espionage entry is the correct output. No F18.

**Classification (F17).** Both entries B/2. Huntress and Acronis TRU are both `reliability: B` in
`sources/sources.json`, so neither letter is above its source's own rating; `2` is the correct credibility
for a single assessor with republishers rather than independent corroboration (a `1` here would have been
the defect). `org_triage: null` and `watchlist_hit: false` on both, matching a profile with no triage scheme
and no watchlists — no F16.

**Style (12).** No hashes, IPs, attacker domains or rule code in either entry (the Huntress IOC table and
Acronis's domain/IP list were deliberately left out; `sheets.googleapis.com` is a legitimate vendor API host,
not an IOC). No vanity metrics, no product-efficacy claims, English throughout, and no workflow-internal
vocabulary in either entry or the run-record notes.

**Dedup / update-vs-new (11).** `actor:akira` co-occurs with three in-window entries (2026-08-05 RUAG ransom
review, 2026-08-10 ESXi BusyBox obfuscation, 2026-08-16 weekly Q2 ransomware roll-up); I read all three
records in the prior-coverage index and none describes this intrusion, this initial-access route or Safe
Mode boot evasion, so the three gate warnings are correctly answered by the run record and the non-update
decision stands. Nothing in the 14-day index or the registry carries PATCHCORD, SHEETCORD, HACKERAI or
APT36, so the new-entry decision there is right too. Neither entry needed `update_of`.

**Coverage completeness (13) — independently re-derived, no gap found.** The 24 h window
(2026-08-16T04:13Z → 2026-08-17T04:13Z) was swept against BleepingComputer, Security Affairs and Help Net
Security feeds, the KEV catalogue, and the NCSC-CH security hub, plus targeted searches for Swiss/European
incidents and in-window exploited CVEs. Findings: KEV is at catalogue version 2026.08.14 with no additions
after 2026-08-11, and all three of those (CVE-2026-20349, CVE-2026-68820, CVE-2026-72898) are already in
`state/cves_seen.json`; NCSC-CH's freshest post is the 2026-08-14 GeoServer zero-day, already published as
`2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited`; the in-window Threema DDoS reporting
is follow-on coverage of `2026-08-15/threema-nine-colocation-ddos-swiss-messenger-outage` with no fresh
delta; Jamf's AmnesiaStealer post is dated 2026-08-13, outside the recency floor and correctly logged as
such; the SafePal breach is an out-of-nexus crypto-wallet incident that clears none of the four higher
grounds. The BlgCloud borderline drop was re-read against the S4 finding and the run record's stated
reasoning holds (European region nexus but no profiled-sector, CI or government victim; a vendor-side
authorization defect during a dual-version migration rather than evolved attacker tradecraft; nothing for a
responder here to patch or hunt). The three struck backlog rows and the two left open are each consistent
with their own recorded instructions and with the store's existing coverage. **Coverage looks complete for
this window** — the "quiet weekend window" the run record describes is what the sources actually show, and
the two published items are the two that clear the gate.

### Editorial / less-is-more flags (advisory)

**F11 — `2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack`: one mapped behaviour has
no technique id.** The body states: "Its most consequential command decodes and decrypts an operator-supplied
payload, allocates memory with `VirtualAlloc` …", and Acronis describes the step in detail ("decodes it using
the same custom Base64 alphabet and decrypts it using a XOR-based routine with a key derived from the session
context"). `techniques[]` carries T1620 for the in-memory load but no T1140 (Deobfuscate/Decode Files or
Information) for the decode/decrypt stage. The other 13 ids are correct and the mapping is otherwise
complete. **Advisory only — leavable; this does not block publish**, and the main agent should feel free to
close the loop without acting on it.

### Verdict

**CLEAN**

No truth defects and no editorial defects. Every cited URL was re-fetched live in this iteration and
resolves to a specific article; every evidence quote is a contiguous verbatim substring of the page it is
attributed to; every named entity, timestamp, event id, command, version, count and date in both bodies is
carried by the page cited for it; the two remediations iteration 1 applied to source dates and to the
campaign chronology are correct against the live sources and introduced no regression; sourcing, priority,
classification, single-source flagging, action discipline, dedup and update-vs-new decisions all hold; and
an independent coverage sweep found no in-window item the run should have published and did not. The single
F11 above is advisory and explicitly leavable.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F11
  category: editorial-advisory
  section: threats
  item: "2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack"
  url_or_quote: "Its most consequential command decodes and decrypts an operator-supplied payload, allocates memory with `VirtualAlloc`"
  summary: >-
    Advisory only, leavable. The body describes a decode-then-decrypt step for the operator-supplied
    shellcode (Acronis: custom Base64 alphabet plus an XOR routine keyed off the session context) and
    techniques[] carries no T1140 (Deobfuscate/Decode Files or Information). The existing 13-id mapping is
    otherwise complete and correct; adding T1140 would close the last behaviour the body names without an
    id. Does not block publish.
```
