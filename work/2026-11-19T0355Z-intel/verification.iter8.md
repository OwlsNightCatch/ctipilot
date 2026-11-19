**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T08:34:50Z · ended_at=2026-11-19T08:57:23Z · duration_seconds=1353

## Verification report — 2026-11-19T0355Z-intel (iteration 8)

Scope: cap-iteration post-fix pass after the iteration-7 NEEDS_FIXES. All 313 ledger claims have a verdict row in `verification.iter8.claims.yaml` (313 ok; `tools/claim_ledger.py --coverage 8`: 313/313 answered, 0 missing). That covers the 3 changed claims, every claim of the remediated entries (Java4Shell, Synology, OptimJack, Airlock, nginx, tcherber, REDCap) and, beyond the required quarter, every claim of the remaining seven entries (Obsidian/LiteLLM, Drupal, Confluence, PHP2Shell, HPE, Idunno, CyberPower). Beyond the ledger I read every title, `sourcing_note`, record summary, run-record note and `techniques[]` list, because the ledger does not carry the `sourcing_note` field. The run record was checked for truth only (counts, dispositions, fetch failures, entities_added against the registry diff).

Passage rows in the claims file were machine-checked as literal substrings of the page body I read (after markdown and whitespace normalisation); rows with `source_url` pointing at a CSAF, CISA alert or Drupal advisory carry fields read through the raw JSON, the WebFetch outbound-links template (CISA, Drupal SA-017/018/PSA) or the `ncsc-csh` bridge.

### Prior-iteration deltas (all eight confirmed)

1. Java4Shell sourcing_note: the Equixly sentence is gone; the remaining text ("Calif's own demonstrations ... Upwind reproduced only the heap overflow", NCSC.ch and Talos no malicious exploitation, Tenable relaying GreyNoise and VulnCheck) matches Calif, Upwind ("We reproduced the overflow on an AWS c6i instance"), Talos, the NCSC.ch hub post and Tenable. OK.
2. Synology sourcing_note: SA-24:20 revision table read this pass: rev 1 2024-11-05, rev 4 2024-11-26 (DSM 7.1), rev 5 and 6 2024-12-05 (DSM 6.2), rev 7 to 9 2025-03; "first published 2024-11-05, further fixes on 2024-11-26 and 2024-12-05" is exact and fits Synology's "December 2024"; BleepingComputer does say "a November 2024 security advisory". OK.
3. OptimJack sourcing_note: Ohey text reads "counted on 18 November 2026" and "Latest match | 18 November"; the note's "nominal date 2026-11-17, while its text counts through 2026-11-18" is correct. OK.
4. Java4Shell new update sentence, checked against https://www.tenable.com/blog/java4shell-cve-2026-114938-frequently-asked-questions-about-openjdk-rce-vulnerability: "As of November 18, Red Hat and Ubuntu had not released fixes, and Debian had fixed only its unstable branch."; "On November 18, the Keycloak project recommended starting its server with -XX:-UseBASE64Intrinsics as an interim mitigation. It said its x86-64 container images tagged 26.8.2-1 and 26.8.2-2 include an affected Java build". Both statements and the record-summary mirror are supported; one over-broad gloss is noted as F11 below. The citation date 2026-11-17 is the page's original publication date.
5. Java4Shell record summary: the record-keeping clause is gone; summary and section agree (4c(d)). OK.
6. Airlock actions[0]: "8.5.0 through 8.5.2 to 8.5.3 and every one running 8.6.0 to 8.6.1" reads as range then target; ENISA record: "8.5.2 and earlier, and 8.6.0 ... fixed in Airlock Gateway version 8.5.3 and 8.6.1". OK.
7. Technique ids against the pinned `attack/enterprise-attack.json` (v20.1): T1068 Exploitation for Privilege Escalation and T1611 Escape to Host (nginx; Xint's SCTP chain to host root and Docker escape), T1190 (OptimJack; Optimizely: "exploited a flaw in the Optimizely Web Experimentation account signup flow"), T1069.002 Domain Groups (tcherber; Cyderes: nxc_ldap.go enumerates "users, groups, domain structure, domain controllers"), T1027.003 Steganography (REDCap; Unit 42: "Steganographic payload delivery disguised as image files"). All active (not deprecated, not revoked); every id on all 14 entries resolves; T1574.001 is the active DLL id. T1046 left off tcherber is defensible (nmap.go "not called by the orchestrator", no use reported). OK.
8. Run record KEV sweep line: now says exploitation "reported as of 2026-10-07", which is what the Unit 42 note supports. OK.

### Truth checks

No truth defect found. Pages read this pass (cached quote bodies and fresh fetches): Tenable, Calif (raw page), Oracle CSPU, OpenJDK advisory, NCSC.ch hub 13196/13198/13203/12960 (bridge), BACS warning, Talos, Upwind, Equixly, Cisco PSIRT (raw: 12 "Affected" rows plus "Affected in releases 26.4.1 and later only" = 13; IOS XE and UCS Central under investigation), Fortinet PSIRT, CISA alerts (WebFetch), Drupal SA-CORE-2026-017/018 and PSA-2026-11-16 (WebFetch), NCSC-NL 2026-0506/0507, CERT-EU 2026-022, CERT.at, nginx.org, Rapid7 blog and PoC README, Wiz, Xint, ENISA EUVD records for Airlock and Idunno, Airlock documentation (changelogs 8.6.1 and 8.5.3, Smart Form Protection, support lifecycle), Mandiant MNDT-2026-0048, Symantec, CISA ICSA-24-123-01, CyberPower product page, Cyderes, VMRay, Securifera, Unit 42, OpenCVE, Pentest-Tools, Google GTIG, Optimizely status, Report URI, Zscaler, Hudson Rock, Ohey, Amirul Cyber, Synology SA-26:13, SA-24:20 and notice, 360, BleepingComputer, heise, CERT-FR (raw page, first version 21 septembre 2026), LiteLLM GHSA (raw page: Moderate 5.9, affected >= 1.81.8 < 1.83.10, patched >= 1.83.10, text "Fixed in 1.83.11"), Obsidian, The Hacker News, Apache announcement and oss-security post, Atlassian advisory, Huntback, Previdian, BleepingComputer N-able article, Trend Micro KA-0024802 and Download Center rows and readmes, Quest KB, NetApp advisory data (revision 13.0, 20261118), HPE CSAF JSON and text advisory.

Recomputed from the HPE CSAF: 76 CVEs, 33 at CVSS 3.1 9.0 or higher (8 at 10.0, 10 at 9.8, 10 at 9.6, 1 at 9.4, 4 at 9.3), 19 network and no privileges, 14 adjacent; the four added CVEs score 7.1, 7.2, 6.5 and 4.9; CVE-2026-95787 scores 10.0 AV:N/PR:N; all 19 `cves[]` rows match the CSAF scope (AOS-10 only, AOS-8 only, or both) and vector. CNA records for CVE-2026-113425 and CVE-2026-123633 (read, not cited) confirm the entry's NGINX Plus fixed builds and the run-record note that 37.2.0.1 and 37.0.7.1 fix only CVE-2026-123633.

Other checks that hold: record `summary` equals what each new section states for all eight updates; `updated_at` equals the last non-internal update `at` on all eight; `fields` match `entry_record.py diff` for HPE; verification values, `sourcing_note` and F12 flags on the four single-source new entries; classification block present and in vocabulary on all 14; no org_triage, no watchlist; no em dash outside the section headings; no workflow vocabulary, IOC or KEV deadline in reader-facing text; evidence quotes literal (Cyderes' first quote is literal in the page HTML across a `<strong>` tag); no new-entry CVE appears in the HEAD `state/cves_seen.json` or the prior-coverage index; the run record's `entities_added` (11 keys) match the registry diff; the two fetch_failures notes (Airlock page cookie-check shell, CodePlex archive basic-auth wall) match what the pages return.

### Missed angles

Coverage looks complete. The NCSC.ch hub feed holds three in-window posts (13196 Drupal, 13198 Java4Shell, 13203 NGINX), all covered; the four KEV additions of 2026-11-18 are all covered (REDCap new, Synology, LiteLLM, Confluence as updates); the two held backlog rows carry a named condition and expiry. No in-window item from a named source is missing.

### Editorial / less-is-more flags (advisory)

1. **F11 #1 (low confidence)** — Java4Shell update section: "so hosts on those distributions have no vendor build yet". Tenable: "As of November 18, Red Hat and Ubuntu had not released fixes, and Debian had fixed only its unstable branch." A Debian unstable host does have a vendor build; the gloss is broader than the page. Reword to "no stable-branch vendor build" or drop the "so" clause.
2. **F11 #2 (low confidence)** — tcherber scope: the Cyderes report is mostly about the operator's loader, stealer, HVNC, Enigma encryptor and a C2 panel with 178 bots and "the actor's infrastructure remains active"; the entry covers the VPN toolkit only and reaches the rest through the VMRay sentence. A scope choice the main agent may leave.
3. **F11 #3 (low confidence)** — nginx sourcing_note: "CERT-EU quotes CVSS 3.1 8.1" (CERT-EU says "a CVSS score of 8.1", no scale; 3.1 is CERT.at's and the CNA's) and "CERT-EU, Rapid7 and CERT.at give R34 to R36 for them" (Rapid7's table covers CVE-2026-123007 only). Recorded values are unaffected.

Left as previously dispositioned, not re-raised: Drupal record `fields` naming `priority` (iteration 6, left); Synology `.L0CK3D` and `read-me3.txt` (vendor and 360 published, iteration 1, left); T1046 on tcherber.

### Verdict

CLEAN

Counts: truth 0, editorial 0, advisory 3. This is the cap iteration, so the run publishes on this verdict whether or not a confirmation pass follows; the one non-ledger area (sourcing_note and title text) was read in full and its three iteration-7 defects are fixed.

### Findings summary (machine-readable)

See `work/2026-11-19T0355Z-intel/verification.iter8.findings.yaml` (3 records, all F11).
