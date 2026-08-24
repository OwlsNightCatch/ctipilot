**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-14T06:32:33Z · ended_at=2026-08-14T06:47:28Z · duration_seconds=895

## Verification report — 2026-08-14T0417Z-intel (iteration 4)

### Prior-iteration deltas — verified

1. **Fortinet entry, F4 (Dutch-CERT batch count).** Fetched both NCSC-NL advisories directly. NCSC-2026-0300 carries CVE-2026-26035 (CVSS 9.8) and CVE-2026-70466 (CVSS 5.3), referencing FG-IR-26-157 and FG-IR-26-158. NCSC-2026-0299 carries CVE-2026-70468 (CVSS 8.1), referencing FG-IR-26-160. That is three Fortinet advisories (157, 158, 160) across two Dutch bulletins — the corrected summary ("three of which the Dutch national CERT carried the following day in two bulletins") is accurate, and the body/sourcing_note agree with it. **Confirmed correct.**
2. **Fortinet entry, F3 (5.3 score provenance).** Fetched FG-IR-26-157/158/160/156 directly from fortiguard.com. Vendor scores confirmed: CVE-2026-26035=8.8, CVE-2026-70466=4.8, CVE-2026-70468=7.3, CVE-2026-70465=7.3 (FortiClient). The body's 5.3 figure for CVE-2026-70466 is now directly hyperlinked to `ncsc-2026-0300.html`, which does state 5.3. Re-derived every CVSS number in the entry against its own vendor advisory page (not just the roundup feed) as instructed — all four match. **Confirmed correct, no residual drift.**
3. **NCSC-UK BitLocker entry, F8 (fourth fallback control).** Fetched the live NCSC UK page. It names exactly four fallback techniques: same-PIN-for-Hello, Network Unlock, Startup Key (with the TPM-and-key caveat), and conditional access ("Finally, if there is no way to add pre-boot authentication to your device, consider how you are going to manage that additional risk... conditional access policies to prevent these high-risk devices from accessing sensitive resources."). The entry's quote is verbatim and contiguous. No fifth control exists on the page. **Confirmed correct.**
4. **WordPress 7.0.4 / CVE-2026-65640 drop.** Verified via SecurityWeek and independent search: CVSS 8.8, requires an Author-level-or-higher account with upload rights, affects only installations running Imagick with Ghostscript, no exploitation reported. The drop-line facts are accurate. **I agree with the disposition.** An authenticated-high-privilege, narrow-precondition flaw with no observed exploitation does not clear the "beyond the regular patch cycle" bar, and recording it as a considered drop (rather than a silent omission) given the store's standing WordPress/Swiss thread is the right call.

### Unsupported / hallucinated facts

**F4-1 (ncsc-uk-bitlocker-pin-winre-fallback-controls).** `techniques: [T1006, T1542.003]`. T1542.003 is *Pre-OS Boot: Bootkit* — installing malicious code in the MBR/VBR/EFI partition to persist below the OS. Neither the entry's body nor the cited NCSC UK page describes installing a bootkit; the mechanism is that BitLocker deliberately leaves the (legitimate) WinRE partition unencrypted, and YellowKey used that recovery environment to reach and decrypt the protected volume. No malicious boot-sector code is involved anywhere in this story. The id names a behaviour the entry does not describe.

**F4-2 (cve-2026-71362-adobe-commerce-account-takeover-targeted).** `techniques: [T1190, T1078]`. T1078 (Valid Accounts) requires obtaining and abusing credentials of an existing account. The entry's own body says plainly: "Nothing is stolen from the victim to make this work — no phished password, no exfiltrated cookie" — and Adobe's own table marks "Authentication required to exploit?" **No**. The flaw switches session identity server-side with zero credential material of any kind. T1078 names a behaviour the entry explicitly denies happening.

**F4-3 (city-forum-salesforce-servicenow-guest-identity-data-theft).** `techniques: [T1190, T1213, T1526, T1078.004, T1530]`. T1078.004 (Valid Accounts: Cloud Accounts) requires obtaining and abusing cloud-account credentials. The entry's opening sentence is: the operator is "using nothing but the anonymous guest identity every one of those platforms creates and cannot delete... no exploit, no stolen credential." The guest identity requires no authentication step at all — that absence of any credential is the entry's central finding. T1078.004 names a behaviour the body explicitly contradicts.

(These are three instances of the same pattern: a Valid-Accounts-family id applied to a scenario the entry's own prose says involves no credential. Note the Fortinet entry's T1078 usage was already reviewed and fixed across iterations 1–3 for a materially different fact pattern — that flaw *does* involve supplying a username/password that gets erroneously authenticated — so it is not re-litigated here.)

### Missed angles

**F10-1.** Acronis TRU published ["PATCHCORD: New malware cluster targets Afghan telecom and South Asian critical infrastructure"](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/) with `datePublished` 2026-08-13T07:45:00Z — inside this run's 26-hour window. It describes three previously-undocumented malware families: PATCHCORD (a C/C++ backdoor delivered via fake Afghan Telecom/Salaam Telecom VPN installers), SHEETCORD (a Go implant using Google Sheets as a C2 channel), and a GitHub-Gists-based C2 agent. This is not mentioned anywhere in the run record's coverage-gap or borderline-drop notes, so it reads as a silent miss rather than a considered decision — Acronis TRU is not a tracked source in `sources/sources.json`, which plausibly explains why the sweep never surfaced it. The item has no direct Swiss/European nexus, but this run already ships an entry (Armored Likho) justified purely on transferable tradecraft with a Russia-only victim set; the legitimate-cloud-service-as-C2 techniques here (Google Sheets, GitHub Gists) are exactly that class of transferable detection lesson. Suggested query: `Acronis TRU PATCHCORD SHEETCORD` or a site-scoped search on `acronis.com/en/tru`.

### Classification missing / inconsistent

**F17-1 (beacon-crm-aws-key-in-public-javascript-build-artifact).** `classification: {reliability: B, credibility: 2}`. The entry's primary source is `https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/`. `sources/sources.json` rates this exact publication (id `infosec-magazine`, publisher "Infosecurity Magazine (RSS)") reliability **C**, with the note: "2026-07-05 admiralty audit: C — reputable trade press, mostly re-reporting with some original interviews; corroborate before acting." The entry rates the whole item reliability B — one letter above its own primary source's tracked rating. The corroborating source (The Register) is untracked in `sources.json` and both outlets are re-reporting the same single Beacon vendor statement, per the entry's own sourcing_note ("one assessor, two publishers"), so there is no independent basis for the uplift.

### Verdict

**NEEDS_FIXES (truth: 3, editorial: 2, advisory: 0)**

All four prior-iteration deltas verified correct with independent fetches — no regressions. Every inline citation checked in this pass (Fortinet ×2 rounds, NCSC-UK, Adobe/Sansec/SecurityWeek, Talos JWR, Kaspersky Armored Likho, Check Point, DGFiP ×2 French sources, Cl0p/Reuters, Beacon, City-Forum ×2 sources) matched its cited page verbatim — no F1/F2/F3 findings this pass. The three F4 findings are a single recurring pattern (Valid-Accounts-family technique ids applied to credential-less mechanisms the entries' own prose disclaims) rather than three unrelated defects, and are cheap to fix (drop or replace the mismatched id in three `techniques[]` lists). Volume (12 entries) was assessed against the relevance/actionability bar per-entry; none was marginal enough to recommend a drop beyond what the run record already documents. Haiwell/CISA (ICSA-26-225-02) could not be independently verified this iteration either: the CISA page 403s directly (expected), the CSAF mirror on raw.githubusercontent.com genuinely 404s despite being listed in the changes.csv index (confirmed via direct fetch and WebFetch, not a proxy artifact), and every jina reader key is confirmed exhausted (`jina-usage` shows `live_key_count: 0`). This is not treated as a finding against the entry — no rung of the ladder that was actually reachable contradicted its content — but the operator should refill jina credits so a future iteration can close this out with a direct read.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-14
  item: "ncsc-uk-bitlocker-pin-winre-fallback-controls"
  url_or_quote: "techniques: [T1006, T1542.003]"
  summary: "T1542.003 is Pre-OS Boot: Bootkit — installing malicious code in the MBR/VBR/EFI partition for persistence. Neither the body nor the cited NCSC UK source describes a bootkit; the mechanism is that BitLocker leaves WinRE unencrypted and YellowKey used that recovery partition to decrypt the drive. No bootkit is installed or referenced anywhere in the entry."
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-14
  item: "cve-2026-71362-adobe-commerce-account-takeover-targeted"
  url_or_quote: "techniques: [T1190, T1078]"
  summary: "T1078 (Valid Accounts) requires obtaining and abusing credentials of an existing account. The entry's own body states plainly: 'Nothing is stolen from the victim to make this work — no phished password, no exfiltrated cookie.' Adobe's own table marks 'Authentication required to exploit?' as No. The flaw switches session identity server-side; no credential of any kind is obtained or used, so T1078 names a behaviour the entry explicitly denies happening."
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-14
  item: "city-forum-salesforce-servicenow-guest-identity-data-theft"
  url_or_quote: "techniques: [T1190, T1213, T1526, T1078.004, T1530]"
  summary: "T1078.004 (Valid Accounts: Cloud Accounts) requires obtaining and abusing cloud-account credentials. The entry's own opening sentence states the operator is 'using nothing but the anonymous guest identity every one of those platforms creates and cannot delete' — 'no exploit, no stolen credential.' No credential of any kind is obtained; the guest identity requires no authentication step at all, which is the entry's central point. T1078.004 names a behaviour the body explicitly contradicts."
- code: F10
  category: missed-angle
  section: entries/2026-08-14
  item: "(whole run — no entry)"
  url_or_quote: "https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/"
  summary: "Acronis TRU published PATCHCORD on 2026-08-13T07:45:00Z (confirmed via datePublished metadata) — inside this run's 26-hour window — describing three previously-undocumented malware families (PATCHCORD, a C/C++ backdoor; SHEETCORD, a Go implant using Google Sheets for C2; and a GitHub-Gists-based C2 agent) against Afghan telecom and South Asian critical infrastructure. Not mentioned anywhere in the run record's coverage-gap or borderline-drop notes, so this reads as a silent miss rather than a considered decision. Acronis TRU is not a tracked source in sources/sources.json, which is plausibly why the sweep did not surface it. The item lacks a direct Swiss/European nexus, but this run already included an entry (Armored Likho) justified purely on transferable tradecraft with no regional nexus; the novel legitimate-cloud-service C2 techniques here (Google Sheets, GitHub Gists as C2 channels) are squarely the kind of transferable detection lesson this pipeline otherwise includes. Suggested query: \"Acronis TRU PATCHCORD SHEETCORD\" or a site-scoped search on acronis.com/en/tru."
- code: F17
  category: classification
  section: entries/2026-08-14
  item: "beacon-crm-aws-key-in-public-javascript-build-artifact"
  url_or_quote: "classification: {reliability: B, credibility: 2}"
  summary: "The entry's primary source is https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/ (publisher 'Infosecurity Magazine'). sources/sources.json rates this exact source (id infosec-magazine, publisher 'Infosecurity Magazine (RSS)') reliability C, with the note '2026-07-05 admiralty audit: C — reputable trade press, mostly re-reporting with some original interviews; corroborate before acting.' The entry's classification block rates the whole item reliability B, one letter above the tracked rating of its own primary source. The corroborating source (The Register) is untracked and cannot independently justify the uplift, and both outlets are re-reporting the same single Beacon vendor statement per the entry's own sourcing_note ('one assessor, two publishers')."
```
