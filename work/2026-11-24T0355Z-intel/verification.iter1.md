**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-24T04:46:28Z · ended_at=2026-11-24T05:02:04Z · duration_seconds=936

## Verification report — 2026-11-24T0355Z-intel (iteration 1)

Scope: 7 new entries, 2 updated entries (git diff HEAD read for both), run record, claim ledger of 152 claims (all 152 have a verdict row in verification.iter1.claims.yaml: 143 ok, 5 F4, 4 F3). Every cited URL was read this iteration (cached bodies compared against re-fetches for Vates, GHSA, Krebs, MSRC, Optimizely PDF, F5 CNA records, CISA KEV alert via WebFetch). Both gate-unreadable quotes were checked by hand: the BSI quote is the summary text of the WID-SEC-2026-4723 CSAF (verbatim, translation faithful), and the CISA KEV title line is on the alert page.

### Citation does not support the claim

- #1 [F3] `2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (Exposure line, summary, actions[0])`
  - Quote: **Exposure:** a BIG-IP on 21.1, 17.5 or 17.1 whose virtual servers use one of those iRule commands or APM policy agents ... ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html))
  - Adjacency: the cited THN page lists the iRule and APM configuration per CVE but names no affected BIG-IP branches for these six flaws (its 21.1.0.3 / 17.5.1.10 / 17.1.3.6 numbers belong to a different CVE). The 21.1 / 17.5 / 17.1 branches are true per F5 CNA records and BSI CSAF product tree (read this iteration) but the entry cites neither for that fact. Cite BSI WID-SEC-2026-4723 beside the Exposure sentence (its product tree lists BIG-IP <21.1.0.4.0.19.3-ENG, <17.5.1.11.0.61.12-ENG, <17.1.3.7.0.21.4-ENG).
- #2 [F3] `2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (BSI and NCSC-NL sentence)`
  - Quote: BSI CERT-Bund says a remote, anonymous attacker can execute arbitrary code (translated from German) ([BSI CERT-Bund, 2026-11-23](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723)), and NCSC-NL rates the likelihood medium and the damage high ([NCSC-NL, 2026-11-19](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0508))
  - (low confidence) Scope: the CSAF of WID-SEC-2026-4723 holds only CVE-2026-123637 (the APM flaw) in its vulnerabilities array, and NCSC-2026-0508 covers 12 CVEs (the six plus CVE-2026-120718, -121812, -125272, -125274, -126336, -126822), so "Kans medium / Schade high" rates a broader advisory. In a paragraph about "six BIG-IP flaws" both clauses read as national-CERT statements about all six. Say what each advisory covers.
- #3 [F3] `2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router (Improvement section, Krebs citation and sources[].date)`
  - Quote: Report URI counted 68 of the affected sites with no policy ... ([Krebs on Security, 2026-11-18](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/))
  - (low confidence) Citation date: the Krebs page shows the dateline "November 17, 2026" (an "Update, Nov. 18, 7:06 a.m." line was added later for the Optimizely PDF); inline label and sources[].date say 2026-11-18. One day of drift, probably the update stamp; the 68 / 50 / 24 (15 percent) figures are on the page and correct. Use 2026-11-17. Same pattern, three days, on the Equinor citation in the APIM entry (page date 2026-11-17, citation 2026-11-20 = last update line): defensible for a live update log, no change needed.

### Unsupported / hallucinated facts

- #4 [F4] `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited (cves[CVE-2026-133469].affected)`
  - Quote: affected: "xen-orchestra before 6.9.2 and 6.10.0; xo-server before 5.211.2 and 5.213.0"
  - Frontmatter contradicts the CVE record and the entry body. The EUVD record for CVE-2026-133469 lists xen-orchestra "< 6.9.2" and "6.10.0, < 6.10.1" and xo-server "< 5.211.2" and "5.213.0, < 5.213.1" as affected (GHSA page: affected 5.213.0, patched 5.213.1 and 5.211.2); the body says "before 6.9.2 (stable) and before 6.10.1 (latest)". As written the string reads as excluding 6.10.0 and 5.213.0, which are affected. Fix to "xen-orchestra before 6.9.2, and 6.10.0; xo-server before 5.211.2, and 5.213.0" with the fixed 6.10.1 / 5.213.1 stated, or "before 6.9.2 and before 6.10.1".
- #5 [F4] `2026-11-24/microsoft-entra-connect-health-api-tenant-metadata-exposed (Exposure line and actions[0])`
  - Quote: **Exposure:** a tenant that onboarded Connect Health and received the Azure Service Health notification ... / actions[0]: "Open Azure Service Health in every Entra tenant that onboarded Connect Health"
  - (low confidence) Neither BleepingComputer nor Netzwoche limits the affected population to tenants that onboarded Connect Health, and BleepingComputer lists "Connect Health onboarding status" among the exposed fields, which implies the API returned data whether or not a tenant had onboarded. The scoping is the entry's inference stated as fact in a cited line. Say "any tenant that received the Azure Service Health notification".
- #6 [F4] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (summary)`
  - Quote: breaching two of 14 analysed in depth through an unpatched Metabase (CVE-2023-38646), a weak password on a shared IT provider's storage interface that held the archives of more than 13 municipalities, and other plain exposures
  - (low confidence) SOCRadar: "Of the 14 organizations analyzed in depth, two were breached, three were partly breached"; it describes the Metabase insurer and the storage server in separate sections but does not say which two were the breached ones, and the sentence maps two breaches onto three causes ("other plain exposures" belong to the partly breached). Reword: two of 14 breached and three partly; the largest thefts were the Metabase insurer and the shared storage server.
- #7 [F4] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (headline)`
  - Quote: BabidiGhost AI agent hit 50+ targets in Belgium, France, Switzerland via exposed tools; MFA and allow-lists held
  - (low confidence) SOCRadar: "The agent targeted more than 50 organizations and datasets"; two of 14 analysed in depth were breached, three partly, and no Swiss victim is named. "hit 50+ targets" reads as 50+ compromised. Use "targeted" (the title already says "run against").

### Needs more research

- #8 [F8] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (cves[CVE-2026-108398].affected and .fixed)`
  - Quote: affected: ".NET Framework 4.x before the 2026-10-13 update (the per-branch version table was not read)" / fixed: "the 2026-10-13 .NET Framework security update (per-branch KB not read)"
  - The per-branch table is readable: MSRC Security Update Guide affectedProduct data (python3 tools/fetch_source.py url --direct "https://api.msrc.microsoft.com/sug/v2.0/en-US/affectedProduct?$filter=cveNumber eq 'CVE-2026-108398'", 24 rows, read this iteration) gives KB and fixed build per product: .NET Framework 4.8.1 fixed at 4.8.9363.0 (KB5127689, KB5127690, KB5127691, KB5127692, KB5127693; KB5127694 at 4.8.10008.0 for Windows 11 26H2), 4.8 at 4.8.4811.0 (KB5127683 to KB5127688), 4.6.2/4.7/4.7.1/4.7.2 at 4.7.4150.0 (KB5126868, KB5127666, KB5127667, KB5127668). The Defender takeaway "confirm the October 2026 .NET Framework update" is not checkable by a Tier 2 responder without them. Add the fixed builds to cves[] / Exposure and drop the "not read" narration.

### Surface contradiction

- #9 [F9] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (summary)`
  - Quote: ZATAZ reports that the same handle now rents the agent and offers a bank-phishing platform that covers 28 Swiss banks
  - (low confidence) "the same handle" after a sentence about the BabidiGhost operator carries ZATAZ's identity link (BlackHatSect0r handle associated with the BabidiGhost and GhostHunters signatures) into the summary, while SOCRadar calls BabidiGhost a second, far less capable operator of the BlackHatSect0r toolchain. The body ("the BlackHatSect0r handle, whose toolchain SOCRadar says the agent runs") and sourcing_note surface the disagreement; the summary silently takes ZATAZ's reading. Name the BlackHatSect0r handle in the summary.

### Editorial / less-is-more flags (advisory)

- #10 [F11] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (cves[] affected/fixed text)`
  - Quote: (the per-branch version table was not read) / (per-branch KB not read)
  - Reader-facing cves[] fields carry research-process narration; resolved by the F8 fix (state the fixed builds).
- #11 [F11] `2026-11-24/symantec-ai-authored-powershell-toolkit-iis-webshell-dns (sourcing_note)`
  - Quote: The page was published on 2026-11-19, inside the lookback of the source's rotation rather than the 26-hour window.
  - Workflow-internal language ("lookback of the source's rotation", "26-hour window") and four sentences in sourcing_note, where two sentences of provenance are the standard. Keep: Symantec is first-hand and the only source (no corroboration found); AI authorship and the Witchetty attribution of the implants are Symantec's assessments.
- #12 [F11] `2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router and 2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (sourcing_note)`
  - Quote: the entry attributes each time to its source and does not reconcile them / transcribed from F5's CVE records, which were read but are not cited as endpoints
  - Composition-rationale and process wording in sourcing_note ("the entry attributes ...", "read but are not cited as endpoints"). State provenance directly: F5 branches, hotfix names and CVSS 3.1 are F5 CVE-record data; OptimJack: the two first-injection times differ and are reported separately.
- #13 [F11] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (Detection)`
  - Quote: flat-mapped managed code creates no image-load event, so look at process creation of the .NET assembly-registration utilities with an unregister option against a file in a user-writable path ...
  - Inference stated under a Project Zero citation: the post says protections that expect to check the loaded image section "will not see the load" and shows regasm /unregister plus COM hijacking, but never says "no image-load event" or "user-writable path". Mark the telemetry guidance as derived (as the F5 Detection line does).
- #14 [F11] `2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited (improvement record summary and sources)`
  - Quote: the fixed releases and actions are unchanged.
  - The diff also removes the body sentence "BleepingComputer gives different release numbers, so check the installed xo-server version rather than the release label" (BleepingComputer stays in sources[] but is cited nowhere in the body now) and adds the poc-public status and tag from the GitHub advisory's one-request proof of concept; neither is in the record summary, and the Improvement section mentions the proof of concept only in an uncited closing sentence. Mention both in the summary or restore a one-line pointer for the BleepingComputer discrepancy.

### Single-source items missing [SINGLE-SOURCE] flag

- #15 [F12] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (verification)`
  - Quote: verification: multi-source
  - (low confidence) Every fact about the operation (50+ targets, Metabase breach, municipal archives, implants, 2026-11-06 to 2026-11-14) is SOCRadar's alone, from static analysis of one exposed server; the two ZATAZ pages are one outlet and corroborate only the handle's commerce (agent rental, phishing platform), not the operation; SOCRadar is not on the national-CERT carve-out list. Consider verification: single-source (sourcing_note already written) or say in the note that the operation facts are single-sourced.

### Classification missing / inconsistent

- #16 [F17] `2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (classification)`
  - Quote: classification: {reliability: B, credibility: 2}
  - (low confidence) sources.json rates the primary (socradar) C ("fairly reliable") and the only corroborator (zataz) B; B on a lone C-tier primary whose corroboration does not cover the operation is generous. C2 fits the shown corroboration; if B is kept, justify it from the first-hand static analysis.

### Action-item discipline

- #17 [F18] `2026-11-24/microsoft-entra-connect-health-api-tenant-metadata-exposed (actions[0])`
  - Quote: ... and confirm that their privileged accounts use phishing-resistant MFA, because Microsoft says the exposed addresses and tenant details can be used for targeted attacks.
  - (low confidence) The first half (find the 2026-11-20 Azure Service Health notice, warn the named contacts) is a concrete task; the clause "confirm that their privileged accounts use phishing-resistant MFA" is generic hardening true without this entry (clause (a)). Keep the notice check and the warning; the MFA point stays in the Defender takeaway. See also the F4 on the "onboarded" qualifier in the same action.
- #18 [F18] `2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router (actions[2], added by the improvement)`
  - Quote: For every page that loaded an Optimizely snippet on 2026-11-16 (...), review the Content-Security-Policy violation reports and the card and cryptocurrency transactions of that day, keep the web server, CDN, WAF and payment logs that cover it and take the legal view on notification duties ...
  - (low confidence) The action reproduces items 3 to 6 of Optimizely's customer-action table that the Improvement section already carries (clause (b)), bundles four separate tasks and overlaps actions[0] (page inventory, treat payment pages as exposed). Narrow it to the one start-now task this finding adds (retain logs and review card and crypto transactions inside 07:51 to 22:24 UTC on 2026-11-16 for pages that loaded an Optimizely snippet) or leave the vendor list in the body.

### Checks that came back clean (no finding)

- Evidence quotes: 29 machine-verified plus the two hand checks; the Vates (EUVD, GHSA), Optimizely PDF (whitespace-normalised) and Symantec quotes are contiguous substrings; translated NSM, BSI and ZATAZ quotes carry a faithful `original:`.
- N-able, Entra, APIM, BabidiGhost, Symantec and Project Zero bodies: every figure, date, build, count and attribution traced to the cited page (N-able build 20261121.1943, CVSS 4.0 9.3, KEV 2026-11-23, RCA within two weeks; NSM builds 31936 / 31938; SOCRadar 23 archives, 8.6 GB, 48 accounts; Symantec 41 modules, 08:44 to 08:47 UTC, six implants to Witchetty; MSRC Important 8.8, publicly disclosed, not exploited).
- F5 CNA records re-fetched for CVE-2026-120722 and CVE-2026-121805 and matched the cached copies; hotfix names, branches, CVSS 3.1 9.8 and the discoverer split (four watchTowr, two F5) match the entry. THN CNF caveat for CVE-2026-120722 is surfaced in sourcing_note.
- Changelog contract (4c): both improvement records name the fields the diff changed, `updated_at` unmoved, `## Improvement` headings match `at`, no silent edit, no supersession left behind (the Vates "no CVE assigned" lines are replaced everywhere; OptimJack summary and the 23:11 UTC Report URI clean-time are not contradicted by Optimizely's 22:24 UTC removal time, and the 04:21 vs 07:51 UTC first-injection disagreement is stated in the section). Both are correctly typed improvement.
- Dedup: no new entry shares a CVE with an existing one (cves_seen has none of the new ids); the N-able Mail Assure entry is a different finding from the 2026-11-10 N-central entry; F5 BIG-IP six differ from the 2026-11-19 NGINX entry and the September APM exploit (stated in the body).
- Style: no IOCs, no em dash in reader-facing text, no registry keys or pipeline vocabulary in titles, headlines, summaries or bodies.
- Priority and relevance: APIM `high` clears the bar (NSM-confirmed exploitation, rotate-now decision for every APIM user); F5 `notable` is right (no exploitation, configuration-dependent, hotfix-only); N-able, Entra, BabidiGhost, Symantec, Project Zero `notable` acceptable; Symantec earns its place on a transferable IIS web-shell / DNS-exfiltration / GPP-SCCM credential-hunting TTP.
- Missed angles: none found. SecurityWeek-linked same-day stories (SAP NetWeaver KEV, Cisco Expressway, GL.iNet, phpAfterShell) are already in the store; the Node2Shell/Brotli KEV item is covered (2026-10-24 and later entries); a web search surfaced no unlisted critical in-window item. Coverage looks complete on the critical/high signal; the Splunk SVD-2026-1103 / SOAR SVD-2026-1108 borderline-drop is defensible (no exploitation, no public exploit).

### Verdict

NEEDS_FIXES (truth: 7, editorial: 6, advisory: 5)

Strongest findings (evidence-complete): the Vates `cves[].affected` string (F4), the Project Zero fixed-build table that MSRC publishes (F8), and the F5 version-branch adjacency (F3). The remaining items are marked low confidence where the source supports the entry's reading but the wording over-reaches.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: updated-entry
  item: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited (cves[CVE-2026-133469].affected)
  url_or_quote: 'affected: "xen-orchestra before 6.9.2 and 6.10.0; xo-server before 5.211.2 and 5.213.0"'
  summary: 'Frontmatter contradicts the CVE record and the entry body. The EUVD record for CVE-2026-133469 lists xen-orchestra "< 6.9.2" and "6.10.0, < 6.10.1" and xo-server "< 5.211.2" and "5.213.0, < 5.213.1" as affected (GHSA page: affected 5.213.0, patched 5.213.1 and 5.211.2); the body says "before 6.9.2 (stable) and before 6.10.1 (latest)". As written the string reads as excluding 6.10.0 and 5.213.0, which are affected. Fix to "xen-orchestra before 6.9.2, and 6.10.0; xo-server before 5.211.2, and 5.213.0" with the fixed 6.10.1 / 5.213.1 stated, or "before 6.9.2 and before 6.10.1".'
- code: F3
  category: claim-not-supported
  section: vulnerability
  item: 2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (Exposure line, summary, actions[0])
  url_or_quote: '**Exposure:** a BIG-IP on 21.1, 17.5 or 17.1 whose virtual servers use one of those iRule commands or APM policy agents ... ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html))'
  summary: 'Adjacency: the cited THN page lists the iRule and APM configuration per CVE but names no affected BIG-IP branches for these six flaws (its 21.1.0.3 / 17.5.1.10 / 17.1.3.6 numbers belong to a different CVE). The 21.1 / 17.5 / 17.1 branches are true per F5 CNA records and BSI CSAF product tree (read this iteration) but the entry cites neither for that fact. Cite BSI WID-SEC-2026-4723 beside the Exposure sentence (its product tree lists BIG-IP <21.1.0.4.0.19.3-ENG, <17.5.1.11.0.61.12-ENG, <17.1.3.7.0.21.4-ENG).'
- code: F3
  category: claim-not-supported
  section: vulnerability
  item: 2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (BSI and NCSC-NL sentence)
  url_or_quote: BSI CERT-Bund says a remote, anonymous attacker can execute arbitrary code (translated from German) ([BSI CERT-Bund, 2026-11-23](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723)), and NCSC-NL rates the likelihood medium and the damage high ([NCSC-NL, 2026-11-19](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0508))
  summary: '(low confidence) Scope: the CSAF of WID-SEC-2026-4723 holds only CVE-2026-123637 (the APM flaw) in its vulnerabilities array, and NCSC-2026-0508 covers 12 CVEs (the six plus CVE-2026-120718, -121812, -125272, -125274, -126336, -126822), so "Kans medium / Schade high" rates a broader advisory. In a paragraph about "six BIG-IP flaws" both clauses read as national-CERT statements about all six. Say what each advisory covers.'
- code: F3
  category: claim-not-supported
  section: threat
  item: 2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router (Improvement section, Krebs citation and sources[].date)
  url_or_quote: Report URI counted 68 of the affected sites with no policy ... ([Krebs on Security, 2026-11-18](https://krebsonsecurity.com/2026/11/attackers-used-optimizely-to-a-b-test-malware-on-top-websites/))
  summary: '(low confidence) Citation date: the Krebs page shows the dateline "November 17, 2026" (an "Update, Nov. 18, 7:06 a.m." line was added later for the Optimizely PDF); inline label and sources[].date say 2026-11-18. One day of drift, probably the update stamp; the 68 / 50 / 24 (15 percent) figures are on the page and correct. Use 2026-11-17. Same pattern, three days, on the Equinor citation in the APIM entry (page date 2026-11-17, citation 2026-11-20 = last update line): defensible for a live update log, no change needed.'
- code: F4
  category: hallucinated-fact
  section: incident
  item: 2026-11-24/microsoft-entra-connect-health-api-tenant-metadata-exposed (Exposure line and actions[0])
  url_or_quote: '**Exposure:** a tenant that onboarded Connect Health and received the Azure Service Health notification ... / actions[0]: "Open Azure Service Health in every Entra tenant that onboarded Connect Health"'
  summary: (low confidence) Neither BleepingComputer nor Netzwoche limits the affected population to tenants that onboarded Connect Health, and BleepingComputer lists "Connect Health onboarding status" among the exposed fields, which implies the API returned data whether or not a tenant had onboarded. The scoping is the entry's inference stated as fact in a cited line. Say "any tenant that received the Azure Service Health notification".
- code: F4
  category: hallucinated-fact
  section: threat
  item: 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (summary)
  url_or_quote: breaching two of 14 analysed in depth through an unpatched Metabase (CVE-2023-38646), a weak password on a shared IT provider's storage interface that held the archives of more than 13 municipalities, and other plain exposures
  summary: '(low confidence) SOCRadar: "Of the 14 organizations analyzed in depth, two were breached, three were partly breached"; it describes the Metabase insurer and the storage server in separate sections but does not say which two were the breached ones, and the sentence maps two breaches onto three causes ("other plain exposures" belong to the partly breached). Reword: two of 14 breached and three partly; the largest thefts were the Metabase insurer and the shared storage server.'
- code: F4
  category: hallucinated-fact
  section: threat
  item: 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (headline)
  url_or_quote: BabidiGhost AI agent hit 50+ targets in Belgium, France, Switzerland via exposed tools; MFA and allow-lists held
  summary: '(low confidence) SOCRadar: "The agent targeted more than 50 organizations and datasets"; two of 14 analysed in depth were breached, three partly, and no Swiss victim is named. "hit 50+ targets" reads as 50+ compromised. Use "targeted" (the title already says "run against").'
- code: F8
  category: needs-more-research
  section: research
  item: 2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (cves[CVE-2026-108398].affected and .fixed)
  url_or_quote: 'affected: ".NET Framework 4.x before the 2026-10-13 update (the per-branch version table was not read)" / fixed: "the 2026-10-13 .NET Framework security update (per-branch KB not read)"'
  summary: 'The per-branch table is readable: MSRC Security Update Guide affectedProduct data (python3 tools/fetch_source.py url --direct "https://api.msrc.microsoft.com/sug/v2.0/en-US/affectedProduct?$filter=cveNumber eq ''CVE-2026-108398''", 24 rows, read this iteration) gives KB and fixed build per product: .NET Framework 4.8.1 fixed at 4.8.9363.0 (KB5127689, KB5127690, KB5127691, KB5127692, KB5127693; KB5127694 at 4.8.10008.0 for Windows 11 26H2), 4.8 at 4.8.4811.0 (KB5127683 to KB5127688), 4.6.2/4.7/4.7.1/4.7.2 at 4.7.4150.0 (KB5126868, KB5127666, KB5127667, KB5127668). The Defender takeaway "confirm the October 2026 .NET Framework update" is not checkable by a Tier 2 responder without them. Add the fixed builds to cves[] / Exposure and drop the "not read" narration.'
- code: F9
  category: surface-contradiction
  section: threat
  item: 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (summary)
  url_or_quote: ZATAZ reports that the same handle now rents the agent and offers a bank-phishing platform that covers 28 Swiss banks
  summary: (low confidence) "the same handle" after a sentence about the BabidiGhost operator carries ZATAZ's identity link (BlackHatSect0r handle associated with the BabidiGhost and GhostHunters signatures) into the summary, while SOCRadar calls BabidiGhost a second, far less capable operator of the BlackHatSect0r toolchain. The body ("the BlackHatSect0r handle, whose toolchain SOCRadar says the agent runs") and sourcing_note surface the disagreement; the summary silently takes ZATAZ's reading. Name the BlackHatSect0r handle in the summary.
- code: F12
  category: single-source-flag-missing
  section: threat
  item: 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (verification)
  url_or_quote: 'verification: multi-source'
  summary: '(low confidence) Every fact about the operation (50+ targets, Metabase breach, municipal archives, implants, 2026-11-06 to 2026-11-14) is SOCRadar''s alone, from static analysis of one exposed server; the two ZATAZ pages are one outlet and corroborate only the handle''s commerce (agent rental, phishing platform), not the operation; SOCRadar is not on the national-CERT carve-out list. Consider verification: single-source (sourcing_note already written) or say in the note that the operation facts are single-sourced.'
- code: F17
  category: classification
  section: threat
  item: 2026-11-24/babidighost-jailbroken-ai-agent-belgium-france-switzerland (classification)
  url_or_quote: 'classification: {reliability: B, credibility: 2}'
  summary: (low confidence) sources.json rates the primary (socradar) C ("fairly reliable") and the only corroborator (zataz) B; B on a lone C-tier primary whose corroboration does not cover the operation is generous. C2 fits the shown corroboration; if B is kept, justify it from the first-hand static analysis.
- code: F18
  category: action-item-discipline
  section: incident
  item: 2026-11-24/microsoft-entra-connect-health-api-tenant-metadata-exposed (actions[0])
  url_or_quote: '... and confirm that their privileged accounts use phishing-resistant MFA, because Microsoft says the exposed addresses and tenant details can be used for targeted attacks.'
  summary: (low confidence) The first half (find the 2026-11-20 Azure Service Health notice, warn the named contacts) is a concrete task; the clause "confirm that their privileged accounts use phishing-resistant MFA" is generic hardening true without this entry (clause (a)). Keep the notice check and the warning; the MFA point stays in the Defender takeaway. See also the F4 on the "onboarded" qualifier in the same action.
- code: F18
  category: action-item-discipline
  section: threat
  item: 2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router (actions[2], added by the improvement)
  url_or_quote: For every page that loaded an Optimizely snippet on 2026-11-16 (...), review the Content-Security-Policy violation reports and the card and cryptocurrency transactions of that day, keep the web server, CDN, WAF and payment logs that cover it and take the legal view on notification duties ...
  summary: (low confidence) The action reproduces items 3 to 6 of Optimizely's customer-action table that the Improvement section already carries (clause (b)), bundles four separate tasks and overlaps actions[0] (page inventory, treat payment pages as exposed). Narrow it to the one start-now task this finding adds (retain logs and review card and crypto transactions inside 07:51 to 22:24 UTC on 2026-11-16 for pages that loaded an Optimizely snippet) or leave the vendor list in the body.
- code: F11
  category: editorial-advisory
  section: research
  item: 2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (cves[] affected/fixed text)
  url_or_quote: (the per-branch version table was not read) / (per-branch KB not read)
  summary: Reader-facing cves[] fields carry research-process narration; resolved by the F8 fix (state the fixed builds).
- code: F11
  category: editorial-advisory
  section: threat
  item: 2026-11-24/symantec-ai-authored-powershell-toolkit-iis-webshell-dns (sourcing_note)
  url_or_quote: The page was published on 2026-11-19, inside the lookback of the source's rotation rather than the 26-hour window.
  summary: 'Workflow-internal language ("lookback of the source''s rotation", "26-hour window") and four sentences in sourcing_note, where two sentences of provenance are the standard. Keep: Symantec is first-hand and the only source (no corroboration found); AI authorship and the Witchetty attribution of the implants are Symantec''s assessments.'
- code: F11
  category: editorial-advisory
  section: threat
  item: 2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router and 2026-11-24/f5-big-ip-six-unauth-tmm-stack-overflows-engineering-hotfix (sourcing_note)
  url_or_quote: the entry attributes each time to its source and does not reconcile them / transcribed from F5's CVE records, which were read but are not cited as endpoints
  summary: 'Composition-rationale and process wording in sourcing_note ("the entry attributes ...", "read but are not cited as endpoints"). State provenance directly: F5 branches, hotfix names and CVSS 3.1 are F5 CVE-record data; OptimJack: the two first-injection times differ and are reported separately.'
- code: F11
  category: editorial-advisory
  section: research
  item: 2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (Detection)
  url_or_quote: flat-mapped managed code creates no image-load event, so look at process creation of the .NET assembly-registration utilities with an unregister option against a file in a user-writable path ...
  summary: 'Inference stated under a Project Zero citation: the post says protections that expect to check the loaded image section "will not see the load" and shows regasm /unregister plus COM hijacking, but never says "no image-load event" or "user-writable path". Mark the telemetry guidance as derived (as the F5 Detection line does).'
- code: F11
  category: editorial-advisory
  section: updated-entry
  item: 2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited (improvement record summary and sources)
  url_or_quote: the fixed releases and actions are unchanged.
  summary: The diff also removes the body sentence "BleepingComputer gives different release numbers, so check the installed xo-server version rather than the release label" (BleepingComputer stays in sources[] but is cited nowhere in the body now) and adds the poc-public status and tag from the GitHub advisory's one-request proof of concept; neither is in the record summary, and the Improvement section mentions the proof of concept only in an uncited closing sentence. Mention both in the summary or restore a one-line pointer for the BleepingComputer discrepancy.
```
