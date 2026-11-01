**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T04:35:15Z · ended_at=2026-11-01T04:51:19Z · duration_seconds=964

## Verification report — 2026-11-01T0256Z-intel (iteration 3)

Scope: all 149 ledger claims of claims.iter3.yaml (the 21 changed claims plus every other claim of all six entries; no claim sampled out). Verdict rows: 146 ok, 2 F3, 1 F4 (verification.iter3.claims.yaml). Pages read this iteration: run bodies (Dream, Unit 42, GTIG, MSRC, Cisco eMudhra and PHP, GitLab, Python post, tracker, Oracle alert revision 2, vd.ch, RTS, SRF, Hunt.io, GreyNoise html); fetched fresh with `extract`/`url`: PSIRT page and JSON, php.net archive (raw HTML), Karimi report, VulnCheck, Sansec, Red Hat (CVE page and RHSB-2026-003), BACS, Inside IT, CERT-EU, ENISA, Cloudflare, watchTowr, Sophos, CrowdStrike (raw dateModified), Wordfence, SRF/Blick TCS Camping, nau.ch, Publica, Siemens, Tenable, WatchGuard, Fortinet, Splunk, Citrix, ReliaQuest, SecurityWeek, BleepingComputer, Google, Mozilla, THN, Oracle 91403, OpenJDK, Go announcement, tracker raw HTML, Hunt.io raw HTML (datePublished), GreyNoise live page (04:21 UTC, 1,177 / 5 IPs unchanged), CISA KEV via `cisa-kev`, CISA alert via WebFetch.

### Iteration-2 remediations (deltas block)

All fourteen remediations check out.
- PHP Detection clause and update section: GreyNoise rows show `mkdir -p /var/www/.ssh` and `chmod 600 /var/www/.ssh/authorized_keys` at 2026-10-29 19:56:46 UTC, reverse shell `bash -i >&/dev/tcp/` at 19:56:40, metadata-address queries from 19:58:50, linpeas and gitleaks downloads at 20:05:42; the first `gitleaks dir /var/www/html` run is 2026-10-31 01:34:33. "web server account's home" and "secret-scanning runs ... in the sessions of 2026-10-31" are right. Record summary matches the section.
- eMudhra CVE-2026-115557 `patch-available`: the Python post lists it in "Security content in all five releases". Action 2 and takeaway: MSRC says "make sure your update process delivers the updated Disallowed Certificate Trust List and the upcoming trust-list changes"; naming Microsoft's out-of-band update of 2026-10-26 as one of the trust-list changes is a fair reading.
- PAN-OS record summary and section both state Dream's GlobalProtect claim against the advisory's "not impacted"; run-record bullet now says the entry states both.
- PHP "all twenty hotfixes": PSIRT table rows 1+3+5+6+5 = 20, timeline ends 2026-10-29T23:54Z "Removed ETAs for 11.1.7-h12"; the new 2026-10-30 PSIRT source record exists.
- Fragnesia summary label "Dream Research, 2026-10-29" matches Dream's "Updated: October 29, 2026"; supersession sentence present.
- Oracle revision 2 (2026-October-30): DB 19.3-19.32, 21.3-21.23, 23.4.0-23.26.3 (not client-only), TFA 26.3-26.10, OPatch 12.2.0.1.16-12.2.0.1.52, SPMS 23.3.4-23.3.6, each remotely exploitable without authentication at 9.1; tracker raw HTML Java row "Pending for OpenJDK, Oracle JDK 27.0.1.0.3, 25.0.5.0.3, 21.0.13.0.3, 17.0.21.0.3, 11.0.33.0.3, 8u511 b33".
- PAN-OS Exposure: Dream's version table lists profiles for 11.1 (7.4.33, provisional) and 12.1/12.2 only.
- Hunt.io relay wording, record summaries and PAN-OS `fields` (no classification) confirmed.

### Citation does not support the claim

1. **F3 (low confidence) — PHP main entry, Detection line.** "AWS, as relayed by Inside IT, advises starting the investigation from 2026-10-17, its earliest honeypot exploit attempt" (https://www.inside-it.ch/php-angriffe-schweiz-blieb-bis-anhin-verschont-20261022). Page: "Wer eine Kompromittierung nicht ausschliessen kann, sollte laut AWS die Untersuchung mindestens ab dem 17. Oktober ansetzen." `git diff HEAD` shows this run dropped "an operator who cannot exclude a compromise" and "at least"; the advice now reads as unconditional and as a fixed start. Restore both.
2. **F3 (low confidence) — PAN-OS entry, Exposure line.** "Dream found attacker profiles for PAN-OS 12.1, 12.2 and 11.1 only and says the web server also fronts the GlobalProtect portal, which Palo Alto's advisory says is not affected ([Dream Research, 2026-10-29])". Dream's page says only "The exploited surface is the PAN-OS management web server, which also fronts the GlobalProtect portal"; the advisory's "GlobalProtect portal, gateway and Clientless VPN are not impacted" is in the PSIRT FAQ. Add the PSIRT citation to the clause (the update section already cites both).

### Unsupported / hallucinated facts

3. **F4 (low confidence) — PAN-OS entry, Detection line.** "in directory logs, LDAP binds by the firewall's service account from unexpected sources, bulk LDAP enumeration and password-spray bursts ([Dream Research, 2026-10-29])". Dream: the attacker "launched" the Active Directory campaign "from the management server" that "already had LDAP connectivity to Active Directory (it needs it to authenticate VPN users)", with the decrypted service-account password hardcoded into the scripts; the bind source is therefore the account's normal host, and Dream does not say "unexpected sources". Keep enumeration and spray bursts; drop or reword that discriminator.

### Editorial / less-is-more flags (advisory)

4. **F11 (low)** — Vaud entry: "It is relevant as a Swiss cantonal education administration, a public body in the home region." Composition-rationale sentence.
5. **F11 (low)** — PHP main entry `techniques[]` has no T1105 or T1552.001 although the new section describes tool downloads and gitleaks runs over /var/www/html and system directories.
6. **F11 (low)** — eMudhra `entities[]` omits `product:oracle-database-server`, `product:oracle-autonomous-health-framework`, `product:oracle-global-lifecycle-management-opatch` (the last two newly registered); Oracle Hospitality Cruise Shipboard Property Management is in neither `entities[]` nor `affected_products[]`.
7. **F11 (low)** — PAN-OS update section carries Unit 42's "approximately .02%" installed-base figure, a vendor statistic.
8. **F11 (low confidence)** — run record `entities_added` lists four keys; `git diff HEAD -- entities/registry.yaml` adds six (the two Oracle product keys are missing from the list).

### Action-item discipline

9. **F18 (low confidence)** — PAN-OS actions[1] repeats the hunt in the Fragnesia entry's actions[1] (2026-10-29, earlier in-window): PHP files nobody deployed in web-reachable directories, an outbound SSH session kept up by systemd or rc.local. Keep the PAN-OS key rotation; trim one of the two hunts.

### Checked and clean

All other claims verified against the pages above. Vaud: vd.ch, RTS and SRF read in full; every clause of the new entry, the evidence quotes and the RTS attribution of the pupil suspicion hold; no prior coverage or registry key for the incident; shape matches the routine-incident floor. ARTEX: every GTIG clause (late August onset, PentAGI/CAIRN, extortion and PRC-nexus adoption, UNC7228 overlap with Storm-0940 dating to at least August, repository takedown with forks, 2 to 25 second bursts, MySQL general-log poisoning) holds. Fragnesia: CISA KEV entry (dateAdded 2026-10-28, chaining sentence), Red Hat RHSB-2026-003 (two of three CVEs affect Red Hat products), Dream 25-server count. eMudhra: Cisco v1.5 table (ISE 3.5P5 December 2026, 3.3P13 and 3.4P8 April 2027, CSCwx36769, updatenow, DAG 3.2.0, DNG 3.4.1, Agentic Connector 1.0.1, ThousandEyes 5.2.2), GitLab, Python, Go, MSRC, tracker pending list (Bottlerocket, OpenHarmony/HarmonyOS, certbot, containerd, Godot, LibreOffice). `updated_at` mirrors each non-internal update `at`; the improvement leaves Fragnesia's `updated_at` untouched; every changed line in `git diff HEAD` is covered by a record's `fields`. Priorities (PHP critical, PAN-OS and Fragnesia high, eMudhra and ARTEX notable, Vaud routine) and Admiralty codes hold. No IOCs, em dashes (one inside a verbatim OpenJDK evidence quote) or workflow vocabulary in entry prose. Run-record notes: dispositions, counts (23 iteration-1 findings, 25 vs 24 Dream count, weekend window, KEV sweep against `kev-window.txt` and the live catalog 2026.10.30) hold. Missed angles: KEV window re-checked (newest additions 2026-10-30, both covered); two searches for 2026-10-31 and 2026-11-01 items surfaced nothing new; coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 5)

All three truth findings and the F18 are marked low confidence; they are small, evidenced wording and citation-adjacency defects, not factual reversals.

### Findings summary (machine-readable)

See work/2026-11-01T0256Z-intel/verification.iter3.findings.yaml
