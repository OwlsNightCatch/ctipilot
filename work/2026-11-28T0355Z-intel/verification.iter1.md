**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-28T05:11:52Z · ended_at=2026-11-28T05:32:22Z · duration_seconds=1230

## Verification report — 2026-11-28T0355Z-intel (iteration 1)

Scope: 6 new entries, 4 updated entries (read whole, `git diff HEAD` per path), run record, 185-claim ledger (all claims in scope; 185 rows in `verification.iter1.claims.yaml`: 167 ok, 8 F3, 7 F4, 3 F5). Sources were read from the gate's cached bodies and re-fetched live where volatile (Cisco, Fortinet, Synology, Mitel, Handelsblatt, Cacti PR and releases, BSI CSAF and RSS, ENISA, cveawg, NCSC.ch hub, GHSA raw HTML, Kudelski raw HTML tables, Hunt.io raw HTML dateline).

### Citation does not support the claim

- **#1 (F3) cacti-1-2-31-4http2root-guest-session-rce-zero-day**, body para 3: "BSI classifies the issue as critical and unpatched" cited to `wid-sec-w-2026-4845.json`. The CSAF carries `aggregate_severity: kritisch`, one known_affected product and no remediation or "unpatched" marker. "[UNGEPATCHT]" exists only in BSI's RSS item title ("[NEU] [UNGEPATCHT] [kritisch] Cacti: Schwachstelle ermöglicht Codeausführung"), which the entry does not cite. Cite the RSS item or cut the clause to "critical".
- **#2 (F3) realvnc-cve-2026-137738-preauth-udp-memory-flaw**, body para 1: "The CVE record and ENISA's entry appeared on 2026-11-27, the day heise reported the flaw" cited to heise only. heise says nothing about when the CVE record or ENISA entry appeared. ENISA (`datePublished Nov 27, 2026, 5:52:17 AM`) and cveawg (`2026-11-27T05:52:17Z`) carry the date. Add the ENISA citation.
- **#3 (F3) hunt-io-open-directories-swiss-tax-office-ntds-ifm**, Exposure: "law firms and US federal agencies are reconnaissance targets only". Hunt.io's evidence table: "Simpson Thacher & Bartlett | US | Attacked, no success | Credential-stuffing, Citrix CVE-2019-19781, SQLi, SMTP relay test, service probing". One law firm was actively attacked (all results failed), so "reconnaissance only" understates it.
- **#4 (F3) bacs-first-confirmed-ai-agent-attacks-switzerland**, body para 1: "three on critical-infrastructure operators and the rest on SMEs that reported voluntarily". SRF: "drei Betreiberinnen kritischer Infrastrukturen ... Auch KMU, welche die Vorfälle freiwillig gemeldet hätten, seien ... gehackt worden." It does not say the remaining two of five are SMEs (RTS: "Des entreprises ont également été attaquées"). The new Update section words this correctly; align the paragraph.
- **#5 (F3) nginx-nginx2root-...**, Update 2026-11-28 para 2 and record summary: "Synology's SA-26:20 revisions of 2026-11-24 and 2026-11-25 added APM" / "adds APM with a fixed build". Revision table: "3 | 2026-11-24 | Update fix status for APM 1.2, APM 2.0, DSM 7.1, DSM 7.2.1, and DSM 7.2.2 | 4 | 2026-11-25 | Update fix status for APM 1.0 and APM 1.1." The revisions updated fix status; APM was already listed affected in the entry's own 2026-11-22 section.
- **#6 (F3, low confidence) nginx-nginx2root-...**, Update 2026-11-28 para 1: "NextFusion Platform, which version 1.1 listed, no longer appears". The cited page is now version 1.6 and has no NextFusion row; "which version 1.1 listed" cannot be read from it (rests on the entry's 2026-11-22 section). "No longer appears" is verifiable (0 hits).
- **#7 (F3, low confidence) kudelski-offensive-ai-identity-lifecycle-insurer**, body para 1: AI assessment "from machine-speed execution, application-specific reconnaissance and automated handling of complex identity workflows". The page's basis list starts "Correlated indicators of compromise. Infrastructure characteristics. Previously documented attack patterns." and says the assessment "is not based exclusively on the speed or volume of requests". The entry omits the IoC and infrastructure correlation with previously documented offensive-AI activity.

### Unsupported / hallucinated facts

- **#8 (F4) freeradius-3-2-11-critical-ttls-use-after-free**, title "no exploitation or proof of concept stated", summary "the project states no proof of concept or exploitation", body "The page states no proof of concept and no exploitation". The cited page says for two High EAP-FAST issues ("Incorrect use of randomness in EAP-FAST could expose the PAC", "Possible stack overflow in EAP-FAST"): "Ada Logics validated the issue, wrote a proof of concept and the report" and "created a Proof-of-Concept" (found by Anthropic using agents). Scope the statement to the Critical TTLS issue and say a private PoC exists for those two.
- **#9 (F4) kudelski-offensive-ai-identity-lifecycle-insurer**, body para 2 and summary: "identity migration between a legacy platform and a modern provider did not preserve account activation states" / "identity migration that lost activation state". "account activation states" appears on the page only in the Section 9 recommendation ("Identity migrations must preserve existing account activation states and security guarantees."). The weakness table row reads "Identity migration preserves trusted account information -> Unverified contact information inherited a verified status". A recommendation is stated as an incident finding.
- **#10 (F4) sap-github-environment-intrusion-project-granite**, summary "SAP told dpa, BleepingComputer and Reuters" and sourcing_note "quoted by BleepingComputer, dpa and Reuters". No listed source carries a Reuters statement (the Reuters page is a CAPTCHA wall and not cited); the body names only BleepingComputer and dpa; cited SecurityWeek says "SAP told SecurityWeek". Replace Reuters with SecurityWeek. The same summary attributes the containment steps to "Handelsblatt's company circles" although the readable Handelsblatt text has no such sentence (the entry's own sourcing_note says so); attribute them to Handelsblatt as relayed by heise.
- **#11 (F4, F9 component) geoserver-five-step-unauthenticated-rce-chain-public-poc**, Update 2026-11-28, sourcing_note and record: "no source marks CVE-2026-129242, the administrator-only deserialization step, as exploited" / "CVE-2026-129242, which no source marks as exploited, loses its exploited status". The cited watchTowr FAQ says "CVE-2026-129245, CVE-2026-129242, CVE-2026-129243, CVE-2026-129244, and CVE-2026-120705 is being exploited in the wild, as reported by watchTowr and CISA" while its table says "Not reported" for 129242. The retained 2026-11-26 section says "watchTowr's prose names all five chain CVEs", and the sourcing_note's own rule ("set on every chain CVE that any of them names") would keep the status. Keep it with a Contradiction line (prose vs table), or state precisely that only the prose names it.
- **#12 (F4) geoserver-five-step-unauthenticated-rce-chain-public-poc**, updates[] record summary: "which settles which chain flaws are confirmed exploited". Neither the section nor the sources say this: CISA lists two flaws, while the entry keeps `exploited` on CVE-2026-129244 (The Hacker News quoting watchTowr) and CVE-2026-129245 (watchTowr table). Delete the clause.
- **#13 (F4) run record 2026-11-28T0355Z-intel**, notes: "the 2026-11-27 fire dropped it as outside its window". `runs/2026-11-27/2026-11-27T0355Z-intel.md` line 378: "Cacti Core 1.2.31 "4HTTP2ROOT" (S1) — single watchTowr source, the guest account must be enabled, no CVE or fix to track, no exploitation". The reason was source count, prerequisite and no exploitation; watchTowr's FAQ (2026-11-26) was inside that window.

### Claims missing inline citation

- **#14 (F5) hunt-io-open-directories-swiss-tax-office-ntds-ifm**, body para 1: "no Swiss authority has commented" sits inside a Hunt.io citation; an absence claim the page cannot carry (sourcing_note: two searches). My own search found no other coverage, so it is probably true; move it to the sourcing_note.
- **#15 (F5, low confidence) freeradius-3-2-11-critical-ttls-use-after-free**, body para 2 first sentence ("The High issues in DHCP, EAP-FAST, EAP-SIM and TEAP are in modules the project says are not enabled by default ...") has no link; true per the project page.
- **#16 (F5, low confidence) nginx-nginx2root-...**, Update 2026-11-28 first sentence ("Cisco's advisory is at version 1.6 of 2026-11-27 (updated affected products).") has no link of its own; true per the revision table.

### Needs more research

- **#17 (F8) kudelski-offensive-ai-identity-lifecycle-insurer**, Detection and weakness list. The page publishes behaviour-level telemetry the entry drops: excessive OTP generation or validation failures (more than 143,000 one-time-code attempts), distributed requests across rotating infrastructure (881 GraphQL reconnaissance requests from 881 source IPs, peak 717 requests per second), authentication transitions at machine speed, authenticator enrollment without completed MFA (ties to the ZITADEL flaw), source-map access by automated clients, activity targeting retired APIs, abnormal sequences across onboarding and recovery. Dropped weaknesses: token validation incomplete, authorization information exposed to the client, CAPTCHA not enforced by the underlying API, alternative registration paths skipping identity checks.

### Quantifier without source

- **#18 (F14, low confidence) hunt-io-open-directories-swiss-tax-office-ntds-ifm**, Exposure: "with the Swiss material being the only case of a public body". The report does not say whether the Bangladeshi university is public and lists US federal agencies and UNC School of Government as targeted. Reword or drop.

### Org-triage line missing / inconsistent

- **#19 (F16, low confidence) geoserver-five-step-unauthenticated-rce-chain-public-poc**, priority `high`. After this update: CISA KEV for two flaws, public full-chain PoC, default install, unauthenticated, fixes available, and watchTowr notes governments commonly expose GeoServer. Re-check against the critical bar for a product Swiss public bodies run. I do not claim it must be critical.

### Editorial / less-is-more flags (advisory)

- **#20 (F11) geoserver ...**, Update 2026-11-26 first paragraph: "...13242)). no victim, actor or scale is named; ..." Removal of "watchTowr is the only observer and" left a lowercase sentence start after a full stop.
- **#21 (F11) nginx-nginx2root-...**, Update 2026-11-28 Cisco paragraph and record summary restate Catalyst Center affected and the five NX-OS trains (already in the body from version 1.5) as new; the real v1.6 deltas are the extra rows (Crosswork Hierarchical Controller, Secure Endpoint Private Cloud Appliance, Intersight, UCS Fabric Interconnect, Optical Network Controller) and the NextFusion removal. Fortinet and Synology deltas are genuine.
- **#22 (F11, low confidence) freeradius ...**, Exposure "any server that accepts EAP-TLS, TTLS or PEAP": the Critical flaw is TTLS-specific, the page's TLS-section issues are Low; the High EAP-MSCHAPv2 over-read (no default statement, common inside PEAP) is not mentioned.
- **#23 (F11) hunt-io ...**, `affected_products`/`entities`: registry already has `product:microsoft-active-directory` (store entries use "Microsoft Active Directory"), the run added `product:active-directory-domain-services`; the JDBC driver is impersonated, not an affected product; `entities: []` although `tool:php2shell` and `product:citrix-netscaler` exist.
- **#24 (F11) cacti ...**: the author's current name 4HTTP2SHELL (BleepingComputer: "dubbed 4HTTP2SHELL (previously 4HTTP2ROOT)") appears only as a registry alias; add it to the body.
- **#25 (F11) sap ...**: `references: []` although the store holds `2026-11-26/1password-employee-github-account-backend-compromise`, whose disclosure the SAP takeaway cites.

### Coverage and other whole-run checks

- Missed angles: none evidenced. NCSC.ch hub since 2026-11-25 holds only GeoServer (13242) and Juniper (13244), both covered; CERT-EU's newest advisory is 2026-022 (nginx); Planzer, FIFA, US Air Force Cloud One, pCloud, AIM Consulting and the BSI agentic-AI warning were assessed and dropped or held with reasons in the notes. Coverage looks complete for a post-Thanksgiving window.
- Update-vs-new: no new entry duplicates stored coverage (prior-coverage index and registry checked; Kudelski declares the BabidiGhost entry in `references[]`). The four updates are the same finding each; each carries a genuine delta (the nginx Cisco restatement is the one thin spot, #21).
- Updated-entry contract: `updated_at` mirrors the last non-internal `update` record (BACS 04:41:50Z, GeoServer 04:50:22Z, nginx 04:51:23Z); Mitel improvement leaves `updated_at: null`; `fields` lists cover every changed frontmatter line in `git diff HEAD`; no silent edits found.
- Quotes: all evidence quotes spot-checked against live or cached pages; German and French `original:` fields (SRF, tagesschau, Handelsblatt, heise, WiWo, CERT-FR) match the pages and the English renderings are faithful.
- Style: no em dashes, IOCs, registry keys, Admiralty codes or workflow vocabulary in reader-facing text.
- Classification: all ten entries carry a block in vocabulary; letters match sources.json tiers; single-source entries carry `single-source*` and a `sourcing_note`.
- cves[]: all GeoServer scores and affected/fixed ranges match the project's GHSA pages (6.9, 8.8, 8.6, 9.2, 8.6, 7.2); Mitel ids and scores match ENISA and the CVE record; RealVNC 9.8 matches ENISA and the CVE record.

### Verdict

NEEDS_FIXES (truth: 14, editorial: 5, advisory: 6)

### Findings summary (machine-readable)

See `/home/user/ctipilot/work/2026-11-28T0355Z-intel/verification.iter1.findings.yaml` (25 records). Claim verdicts: `/home/user/ctipilot/work/2026-11-28T0355Z-intel/verification.iter1.claims.yaml` (185 rows: 167 ok, 8 F3, 7 F4, 3 F5).
