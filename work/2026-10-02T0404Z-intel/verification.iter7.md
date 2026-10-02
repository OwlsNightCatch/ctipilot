**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-02T08:16:10Z · ended_at=2026-10-02T08:47:20Z · duration_seconds=1870

## Verification report — 2026-10-02T0404Z-intel (iteration 7)

Scope: post-fix pass, fresh cold read. All 295 claims in claims.iter7.yaml have a verdict row in verification.iter7.claims.yaml (`claim_ledger.py --coverage 7`: 295/295, 0 missing), which exceeds the required scope (the 11 changed claims, every claim of Citrix, Belnet, KillSwitch, UNCTAD and Stadt Wien, and a random quarter of the rest). Every cited page was read this iteration where a transport reached it: extract for web pages (Citrix set, Unit 42, watchTowr FAQ and Labs, BleepingComputer, Belnet, Risky, fedpol, Polizei Hamburg, OTS, Transluce, swarmcha.se, SiliconANGLE, Asymmetric, Cyber Centre, NCSC-NL Zammad, ICI), `pdf` for the ANSSI report, `ncsc-csh post` for 13005, 13021 and 13022, `cisa-kev`, the FIRST EPSS API, the Europol article body from the page's embedded JSON, raw HTML for the Adobe div tables, the FortiGuard advisory and the eight Kiteworks GHSA pages; the gate's saved bodies were reused for the rest (Talos, VulnCheck, Cisco, GTIG, Censys, eSentire, Tenable, Help Net Security, heise, Rhein-Zeitung, AK-Kurier, ZATAZ, Objectif Gard, DIVD case and CVE pages, Zimbra pages, THN, CERT-FR). The whole of all ten new entries, the five updated entries, the run record (notes checked against the backlog file, KEV and hub lists) and the registry diff were read, and `git diff HEAD` was compared with each record's `fields`.

### Iteration-6 deltas (9 findings): remediation check

- Citrix Triage (F4): now "an unauthenticated request whose logged text carries command-like content is enough ... (see the 2026-09-29 update)". The old premise is gone; the new wording still overstates (finding #1).
- Citrix 2026-09-29 section (F3): now "relaying Citrix's confirmation of active exploitation" with inline links to the hub post (created 2026-09-28T05:39Z), NCSC UK (2026-09-28: "confirmed as being actively exploited" via the Citrix bulletin) and CERT-FR (2026-09-28: "Citrix indique que ... activement exploitées"). OK.
- Citrix takeaway (F5): CERT.at advisory (27. September 2026) now linked inline; NCSC-CH link present. OK.
- Belnet (F14): body now "all incoming mail to Belnet-owned domains (for example guest-roaming and BNIX addresses) and every download link ... generated and sent directly"; headline and title no longer carry the old quantifier. The summary still drops "and sent directly" (finding #3).
- KillSwitch (F3): the further-victims clause now cites Polizei Hamburg ("Die Beweismittel können dazu beitragen, weitere Geschädigte, Angriffe und beteiligte Personen zu identifizieren"). OK.
- UNCTAD (F3): summary, update paragraph and record summary now carry "so far" and "in these datasets" (Transluce: "We have so far identified no instances in these datasets ..."). OK.
- Stadt Wien Exposure (F3): now "the copied content included technical documentation, personal data and business and infrastructure information" ("sowohl technische Dokumentationen als auch personenbezogene Daten ... Geschäfts- und Infrastrukturinformationen"). OK.
- sources[] omissions (F11): confirmed already present (NCSC-CH 13022 in Zimbra, GHSA-gmgg-7xhc-75f9 in Kiteworks). OK.
- Registry KillSwitch summary: "identified" now (Polizei Hamburg and Europol both say identified). OK.

### Claim-ledger result

290 ok, 5 non-ok rows (d793a58403 F4; 0b95bcd983 F3; 11cd998d5d F14; 2733ea8d47 and ce3dd4cc75 F14). Changelog contract (check 4c): each of the five updated entries' record `fields` covers every changed frontmatter key in `git diff HEAD`; `updated_at` equals the record `at`; each record has its section; `discovered_at`, `run_id` and the path are untouched.

### Generic / oversight URLs (replace with specific article)

**#5 (F2, low confidence) Censys advisory in the Citrix entry.** Cited as `https://censys.com/advisory/cve-2026-10747-2/` (sources[], one evidence `source_url`, the 2026-09-30 section). The slug names CVE-2026-10747 (the IBM MQ item held in the backlog); the URL answers HTTP 301 to `https://censys.com/advisory/cve-2026-88771-cve-2026-88772/`, whose `<link rel="canonical">` and title ("Sept 28 Advisory: Citrix NetScaler ADC and NetScaler Gateway Zero-Day Remote Code Execution [CVE-2026-88771, CVE-2026-88772]") were read this iteration. Replace with the canonical URL. Lower weight: the SDIS entry's `objectifgard.com` article URL answers 301 to `www.objectifsud.fr` (the publisher's new domain); it still resolves.

### Citation does not support the claim

**#2 (F3, low confidence) UNCTAD summary, dates.** "On 2026-09-30 and 2026-10-01 Transluce reported failed SQL-injection attempts ... and Asymmetric Security separately reported probes for exposed Git files". Transluce's post is dated 2026-09-30 and Asymmetric's 2026-10-01; the sentence attaches both dates to Transluce. Name each date with its publisher.

### Unsupported / hallucinated facts

**#1 (F4, low confidence) Citrix Triage line** (claim d793a58403). Quote: "an unauthenticated request whose logged text carries command-like content is enough to reach the vulnerable code path". watchTowr Labs: the payload is `pitboss PPE unexpectedly died NSPPE;<command>` and the script's grep selects only lines matching `pitboss.*PPE.*(missed too many heartbeats|unexpectedly died)`; CERT-EU: "The `| tail -1` explains the hammering: only the last matching line counts"; Unit 42 shows the same `pitboss PPE missed too many heartbeatsNSPPE;` prefix. Command-like text on its own is not enough. Reword to "logged text that imitates a Pitboss crash message followed by shell syntax" so a hunter keys on the prefix.

### Quantifier without source

**#3 (F14, low confidence) Belnet summary and title** (claim 11cd998d5d). Summary: "plus every download link its FileSender and FedSender transfer services generated". Belnet: "All download links generated and sent directly by our FileSender and FedSender services during this period". The body keeps "and sent directly"; the summary does not.

**#4 (F14, low confidence) Kiteworks "No CVE had been assigned"** (summary claim ce3dd4cc75, body claim 2733ea8d47, cited to The Record). The Record carries watchTowr's "There is no known CVE, patch, or additional technical details available" and says Kiteworks did not answer whether the bug had a CVE yet. "No known CVE" is not "none assigned". BleepingComputer (2026-10-01) says Kiteworks "has not yet assigned a CVE ID" for the vulnerability it fixed during the shutdown; cite that, or write "no CVE was publicly known".

### Editorial / less-is-more flags (advisory)

**#6 (F11, low confidence) Citrix record summary.** The record summary lists three corrections; `git diff HEAD` also shows the Triage rewrite, the 2026-09-29 section reworded from "independently confirming" to "relaying Citrix's confirmation", the BleepingComputer/NCSC-NL clause reworded and CERT.at linked inline, none stated.

**#7 (F11, low confidence) UNCTAD update closing sentence** (claim 21f1612be9): "The record adds no Swiss target and no confirmed intrusion; its use is as a description of the traffic ...". Composition-rationale language in reader text (check 12); state the hunt-relevant list directly.

**#8 (F11, low confidence) KillSwitch "of which about 500"** (claim 57baab9914): Polizei Hamburg's 500 is of the roughly 1,000, but the clause follows "at least 70 of them in Germany" and reads as 500 of 70.

### Checked and clean (no finding)

Citrix: CTX697096 table, CWE ids, fixed builds, watchTowr FAQ and Labs, CERT-EU, NCSC-NL, hub 13005, BleepingComputer, KEV entries (2026-09-27, forensic triage), GTIG artefacts and controls, GreyNoise, eSentire, Tenable, Censys counts, Help Net Security, ZIDKOR/AK-Kurier/Rhein-Zeitung/heise, and every Unit 42 claim of the new section (2026-08-21 fingerprinting, 2026-09-04 to 2026-09-24 .deb web shells, 2026-09-10 to 2026-09-27 GetUserName stream, 2026-09-21 three-stage chain, SUID/Alias/php_flag, 50,277). Belnet: 65-day window, remediation time, FileSender detail, Risky sentence. KillSwitch: Hamburg, fedpol and Europol on every count. Stadt Wien: every date, count and filing, both evidence quotes verbatim with German originals. UNCTAD: swarmcha.se, SiliconANGLE, Transluce, Asymmetric, Cyber Centre claims and the six evidence quotes. Zimbra (Microsoft details, ENISA 8.9/EU KEV 2026-08-18/EPSS 0.11736, CERT-FR 19 August, THN, 10.1.20/10.1.21 pages, hub 13022), FortiMail (PSIRT table re-read, BleepingComputer, KEV), Cisco (advisory, VulnCheck, hub 13021, CISA alert, EPSS 0.01096), Zammad (NCSC-NL, DIVD cases 14 and 15, both CVE records 8.7/8.5/9.4, EPSS), UAT-11587 (Talos), Adobe (both bulletins' div tables, 18 CVEs of which 10 PR:N, KEV absence), ANSSI (PDF and report page), FTAPI (heise, Cybernews, Lucerne), Kiteworks (eight GHSA pages with CVE ids and CVSS, BleepingComputer, TechCrunch, Heise, The Record, Kiteworks pages), SDIS (ICI, Objectif Gard, ZATAZ). All ATT&CK ids in the pin are active. Style scan: no em dash outside `## Update` headings, no hashes, IPs or attacker domains, no pipeline vocabulary in reader text apart from the append-only 2026-09-29 Citrix record summary. Classification codes, priorities and verification values consistent with the sources. Run-record notes verified: 26 backlog rows = 2 published + 7 held + 17 struck (matches state/coverage_backlog.md), KEV sweep and hub list match, declined findings recorded.

### Missed angles (F10)

None found. KEV window sweep (3 additions since 2026-09-29: Apple CoreGraphics, Cisco SD-WAN Manager, FortiMail, all covered), NCSC-CH hub list (13027 FortiMail, 13022 Zimbra, 13021 Cisco covered; 13007 WatchGuard AP unknown status, dropped), WebSearch for exploited flaws and Swiss communal incidents (Manno TI is covered by the 2026-09-30 entry; the Montreux result is from 2021; the HPE OneView hits are XSS/redirect or the old 2025 RCE; SharePoint CVE-2026-65660 is covered). Coverage looks complete.

### Verifier side effects (for the operator)

- Running `tools/kev_window_diff.py` as a cross-check re-wrote `work/2026-10-02T0404Z-intel/kev-window.txt` (the tool persists to that path); it now shows the three in-window additions as COVERED (post-publish store state) instead of the original two NOT COVERED rows. The run-record note about two uncovered additions still stands as a statement about the run-start state. Regenerate or annotate the file if it matters for the forensic record.
- One FIRST API fetch through `fetch_source.py url` fell back to the jina reader (metered credit, one fetch).

### Verdict

NEEDS_FIXES (truth: 5, editorial: 0, advisory: 3)

All eight findings are small and marked low confidence. The one with operational weight is #1 (a Triage premise that omits the Pitboss-shaped prefix a hunter must key on); #5, #3 and #4 are one-line fixes. The nine iteration-6 deltas (eight edits and one already-satisfied check) are correct for the text they changed.

### Findings summary (machine-readable)

See work/2026-10-02T0404Z-intel/verification.iter7.findings.yaml (8 records: F4, F3, F14 x2, F2, F11 x3).
