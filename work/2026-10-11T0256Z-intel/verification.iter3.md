**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T04:07:25Z · ended_at=2026-10-11T04:17:11Z · duration_seconds=586

## Verification report — 2026-10-11T0256Z-intel (iteration 3)

Scope: post-fix pass. All 112 claims of the ledger (claims.iter3.yaml) carry a verdict row in verification.iter3.claims.yaml (112/112, `claim_ledger.py --coverage 3`): the 13 changed claims, every other claim of all five remediated entries, which is the whole ledger, so no random-quarter sample was needed. Every cited page (23 URLs) was fetched in this iteration (extract; the LE forum and DR live blog parsed from raw HTML/JSON-LD); the mechanical gate was re-run and shows only the expected mid-loop FAILs (residual count, completed stamp).

### Prior-iteration deltas (all eight walked against the sources)
1. Denmark sourcing_note: attributions match the pages (ministry release and Datatilsynet; DR live blog; Pays confirmation to TV 2 and the 123456 finding are Politiken/Ritzau via cphpost.dk; 21 d 17 h is a bare Ritzau sentence; the access account is the hacker's claim). Correct; no residual supersession.
2. Denmark takeaway: 'multi-factor sign-in' gone; clause states the reported 123456 use on three accounts incl. admin (cphpost.dk). Correct.
3. ccTLD summary and registry: Google blocked the certificates in Chrome and 'worked with the issuing CAs to ensure the certificates were revoked' for the Google properties; other organizations' certificates were 'proactively blocked'. Wording now matches.
4. PoeLLM geography: Lumen 'predominantly in the United States and Western Europe' sits under the Lumen citation; BleepingComputer cited for the raised figure (2,100 to 3,400 in the live report). Registry summary: Lumen assessment without confidence level. Correct.
5. ChainDrop action 2: isolate-before-revoke attributed to OX's August report ('dead man's switch ... delete the current machine'); gh-token-monitor removal limited to hosts that ran tensorlake@0.5.144 (Socket and OX tensorlake pages). Correct; body says 'any token-monitor persistence'.
6. 'a further package' replaces 'a second package' in record summary and section. Correct.
7. IDCF: attacker-figure sentence and evidence record gone; remaining claims verified against IDC Frontier reports 2 and 3, BleepingComputer, Jiji/nippon.com.
8. Tensorlake product no longer in affected_products, no registry record (grep of entities/ and state/ finds none).

### Truth checks
Every URL resolves and is a specific article. Citation-adjacency walked clause by clause for all five entries; citation dates match the sources' own datelines (Lumen's own date field reads 2026-03-16, disclosed in the sourcing_note; BleepingComputer dates it 2026-10-07). Evidence quotes (13) verbatim; the four Danish originals match the pages and the translations are faithful. The Danish and Japanese pages were read in the original.
- CVE ids in PoeLLM prose (CVE-2026-42271, CVE-2026-48710, CVE-2026-10520) appear on the cited pages (Lumen, BleepingComputer); `cves: []` is correct for a botnet entry that is not about those flaws and the covering entries are in references[].
- Changelog contract (ChainDrop 2026-10-11T03:39:00Z; Denmark 2026-10-11T03:40:00Z): section `at` equals record `at` and `updated_at`; every changed line in `git diff HEAD` is covered by the record's `fields`; record summaries match their sections; the newest sections do not contradict the main analysis (Denmark detection line and summary updated to the Ritzau duration with the minister's figure attributed; ChainDrop containment paragraph points to the update). Both are genuine deltas of type `update`.
- No contradiction between main analysis and newest section found; no IOC; no workflow vocabulary in reader-facing text; no new em dash outside the section heading.

### Editorial checks
Relevance and priority: ccTLD registry compromise (global significance, transferable CT-monitoring and CAA lesson), PoeLLM (widely deployed AI/dev software, Western Europe victimology, new dead-drop C2 on a poem), IDCF (public-sector supplier concentration) all clear the bar at notable/routine; nothing is miscalibrated. Classification codes in vocabulary and consistent with sources.json (google-tag B, socket B, elastic B, lumen candidate B, ox C). No watchlist or org_triage use. actions[] on ChainDrop: three concrete tasks, none generic.
Missed angles: searched exploited-vulnerability, KEV and Swiss-incident queries; the exploited items surfaced (FortiMail CVE-2026-104286, Cisco SD-WAN CVE-2026-76504, NetScaler CVE-2026-88771/-88779/-107406, Chrome CVE-2026-11645) are all already carried by store entries. Coverage looks complete for a quiet weekend window.

### Editorial / less-is-more flags (advisory)
F11 #1 IDCF narrative length (four sentences; judged defensible), #2 ChainDrop carried-forward em dashes and persistence name (declined by main agent, may be left), #3 PoeLLM summary 'most likely' vs Lumen 'likely', #4 run record entities_added omits product:gotenberg and product:idc-frontier-idcf-cloud, #5 Denmark verification value defensible but could be multi-source. Details in verification.iter3.findings.yaml.

### Verdict
CLEAN (truth: 0, editorial: 0, advisory: 5)

### Findings summary (machine-readable)
See work/2026-10-11T0256Z-intel/verification.iter3.findings.yaml (5 advisory F11 records, none blocking).
