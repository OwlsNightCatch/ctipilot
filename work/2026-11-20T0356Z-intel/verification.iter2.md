**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-20T05:55:02Z · ended_at=2026-11-20T06:19:18Z · duration_seconds=1456

## Verification report — 2026-11-20T0356Z-intel (iteration 2)

Scope covered: 5 new entries, 7 updated entries (whole entry + `git diff HEAD` each), the run record, the deltas block, and the claim ledger `claims.iter2.yaml` (313 claims, all 313 rows in `verification.iter2.claims.yaml`; `tools/claim_ledger.py --coverage 2` reports 313/313). This is a full pass, not a sample: every claim of the 53 changed set, every other claim of every remediated entry and of the untouched MiCollab entry were answered. Evidence base this pass: 134 cited URLs fetched with `extract` / `url` / `ncsc-csh` / `cisa-kev` / `pdf`; CISA alert pages (PHP, Puppet KEV, Java) via WebFetch with the outbound-links template; php.net ChangeLog and archive, GHSA sidebars, calif.io, Veria Labs and the BSI CSAF read as raw HTML or JSON because `extract` drops them; CNA records and ENISA EUVD JSON read directly. Unreadable this pass: web.archive.org PAN copy of 2026-10-27, Citrix community page (403), Reddit thread cited by NCSC.ch and The Hacker News (anti-bot challenge). Weaker check, stated for weighing: claims on the old, unchanged text of previously published entries (Zammad, old PHP, ARTEX, Turla, Puppet, Java, MiCollab bodies) were checked by distinctive-token overlap against the pages fetched this pass, plus a semantic read of about 30 of them (Zammad DIVD pages and GHSA, ARTEX Wiz, Puppet Neodyme/OpenVox, Java Calif/Upwind/Tenable/Tanzu/PAN, Turla ESET PDF, PHP archive and KEV); no sentence-level read of every old clause.

### Prior-iteration fixes (deltas block), each re-checked against its source
Correct as remediated: #1 (CVE-2026-129474 exposed on built-in defaults, GHSA-8mjj), #3 ("up to 18 CVEs per branch, fewer on the older branches": ChangeLog-8 counts 18, 14, 13, 12), #4 and #5 (old PHP immediate_action and takeaway), #6 (ECK operator, Elastic page), #7 (credentials clause now on the overview page, 2026-11-18 case-page citations, second sources[] record), #8 (Ruby severity to NCSC.ch, CVE-id statement to the Ruby announcement, EUVD only for CVE-2026-132825; GHSAs rate three Critical so "by the project" holds), #11 to #13 and #25 (vCenter clauses re-cited, "then off again", "domain database, registry hives and DNS data from Windows guest virtual disks"), #14 and #30 (USI lines removed), #15, #16, #17, #18, #19 (ARTEX date disagreement now stated), #23 (record is an `improvement`, `updated_at` untouched), the F5 removal (no entry file, six CVE ids absent from `state/cves_seen.json`, no registry reference) and the declined #24, #26, #31, #32 (rebuttals judged sound: no-vector Basel-Landschaft incident cannot ship as an `incident` with empty `techniques[]`; the Commission incident is a new government victim for the ARTEX tooling; no technique source for certificate-name impersonation; compaction left to the audit).
Not fully correct: #2 (body and backlog fixed, frontmatter summary still carries the quantifier: finding 1), #20 (finding 15), #27 (finding 20), #29 (finding 21).

### Quantifier without source
- #1 (F14) `php-8-5-13-...` summary: "The one reachable without an application bug is CVE-2026-129289". GHSA-gr4f (CVE-2026-129496): "Successful exploitation does not require application-level code execution or attacker control of `PHP_VALUE` or `PHP_ADMIN_VALUE`." The entry's own `cves[].affected` and body say CVE-2026-129289 needs "an application path that opens php://input without reading it fully". Fix the summary the way the body was fixed.

### Citation does not support the claim
- #2 (F3) `php-critical-release-...` body: "the regular releases of 2026-11-19 fix it and no exploitation is reported ([PHP, 2026-11-19](.../GHSA-658j-r8rw-q6mx))". The GHSA says nothing about exploitation status; watchTowr's CVE-2026-115560 FAQ ("As of November 20, 2026, no exploitation in the wild has been reported") says it but is not cited on this entry.
- #3 (F3, low confidence) `php-8-5-13-...`: "PHP 8.1 gets no fix for CVE-2026-129291 ([GHSA-jm4m])"; the GHSA says only "Upgrade to the fixed release for your PHP branch". Support is in the CNA record (8.1.20 through 8.1.34, no fixed 8.1) and php.net's "PHP 8.1 and older no longer receive updates".
- #5 (F3, low confidence) `zammad-...` update: the 207 email addresses, two phone numbers and seven profile pictures are bound to the Zammad-host "selective extraction" explanation; the overview attributes them to "Our Jira and Confluence environment was compromised".
- #6 (F3, low confidence) `artex-...` update and record summary: "Sysper and MyPMO were offline for more than 10 days"; POLITICO: "Disruption has lasted over 10 days. Sysper ... and MyPMO ... were restored earlier this week".
- #7 (F3, low confidence) `artex-...` update: "The Commission has not confirmed the ARTEX link ... ([Cyber Security News])"; the cited page carries only the "did not establish whether ARTEX helped them break in" half.
- #10 (F3, low confidence) `vmware-vcenter-...` Detection: "vpxuser or root SSH logins from the vCenter or an appliance"; GTIG: "authenticating to ESXi Host Client ("ESXUI") using the `vpxuser` account and also connected to it via SSH using the root account", source host not stated.

### Unsupported / hallucinated facts
- #4 (F4, low confidence) `php-8-5-13-...` cves[]: `auth: pre-auth` for CVE-2026-129481 and CVE-2026-126714; GHSA-g3vh and GHSA-fm2m both say "Authentication requirements depend on ..." the application path.
- #8 (F4, low confidence) `ruby-...` sourcing_note: "Veria Labs and the Ruby project disagree on who found the flaw first"; Veria: "found this vulnerability independently and was the first to demonstrate remote code execution", and credits the project's reporters; no source states a disagreement.
- #9 (F4, low confidence) `mitel-openscape-4000-...` Exposure: "any path from user, partner or internet networks to the Platform counts ([Mitel])"; the advisory names only "adjacent network access".
- #12 (F4) run record notes and `state/coverage_backlog.md`: "plus an `update` record on the October pre-announcement entry"; the record is an `improvement` and the notes say so one bullet later.

### Analytical-link-as-fact
- #11 (F13, low confidence) `cve-2026-115731-puppet-...` improvement: "the Reddit intrusion report it rests on describes a CVE-2026-115731 intrusion". NCSC.ch lists the thread as "Community report of in-the-wild exploitation" beside the KEV entry and does not say its label rests on it; THN quotes the user on a "[CVE-2026-]115731 intrusion" but the thread URL slug reads `cve2026115732_published_114_being_exploited_in`. Thread unreadable.

### Claims missing inline citation
- #16 (F5) `cve-2026-115731-puppet-...`: "NCSC.ch's temporary measures are to disable certificate autosigning ..." has no link (NCSC.ch post 13204 lists them).
- #17 (F5) `zammad-...` update: "DIVD closed its forensic investigation on 2026-11-18" is uncited; the case page says "has been completed" and was updated 18 Nov, no completion date.

### Needs more research
- #13 (F8, low confidence) `php-8-5-13-...` Exposure and `cves[CVE-2026-129474].affected`: configuration-only exposure; GHSA-8mjj also requires "a reachable magic method call", request data controlling allocation size, "a fatal error at the relevant point" and address knowledge.
- #14 (F8, low confidence) `vmware-vcenter-...` actions[0]: the TCP 2012 allowlist omits GTIG's "rigorous testing and formal change control" caveat for its iptables rules; port 2012 is the SSO control RPC interface.

### Surface contradiction
- #15 (F9) `vmware-vcenter-...` cves[CVE-2026-123894].affected: advisory VMSA-2026-0009.1 lists 12.3.x, 12.4.x, 12.5.x; Q&A says 13.x, 12.x and 11.x; the entry writes "12.x" and attributes only 11.x to the Q&A.

### Editorial / less-is-more flags (advisory)
- #18 (F11) `php-8-5-13-...`: Detection "endpoints that read php://input early" should be "open php://input without consuming it"; stray comma in "attack, ([PHP, 2026-11-19]".
- #19 (F11, low confidence) `php-critical-release-...`: the record is typed `improvement` while the section reports a new development (new builds, three CVEs); defensible under the float directive.
- #20 (F11) `turla-...`: two ESET-supported statements (attribution basis, CerealHermit) were deleted from the main analysis with no mention in the section or summary; section narrates the edit ("folded into the Detection line above"); Detection lists proxy-DLL names as file-name indicators.
- #21 (F11) `usi-...`: evidence quote lacks "(translated from Italian)" (marker only in the summary); takeaway dates the vulnerable software "from 2026-11-09" although USI gives only the access window.

### Missed angles
None. NCSC.ch hub posts of the window (13196, 13198, 13203, 13204, 13205, 13211, 13212) are all covered by this run or earlier entries (nginx2root 2026-11-19, Drupal 2026-11-18, Java4Shell, Puppet); a general web search surfaced nothing dated inside the window that the entries lack. The held Basel-Landschaft item stays a judgement call, the home-region watch line and re-check query are in the run notes. Coverage looks complete.

### Classification / priority / action-item discipline
None. All 12 entries carry Admiralty ratings consistent with sourcing (USI `B/2` on a victim communique relayed by press; OpenScape `A/2` on a vendor advisory with CERT restatements); no `org_triage`, no watchlist tag; vCenter `high` (GTIG-only exploitation, no PoC or KEV listing, "if unsure, high"), Ruby `high` (dated exploit announcement, default Rails exposure), PHP and OpenScape `notable`, USI `routine`; every `actions[]` is a concrete task derived from the finding's mechanics (vCenter action 2 now the SSO, signing-material and authorized_keys review).

### Checked and fine (no finding)
vCenter: Broadcom VMSA-2026-0009.1 matrix (versions, KB88287, KB463116, CVSS 9.8/8.1/7.2/6.7/6.7, "Workarounds: None", Mandiant credit), Q&A (emergency change, ESX not affected, back-in-time), GTIG chain, Table 1 TCP 2012 row, BleepingComputer quote, four evidence quotes. PHP new: ChangeLog counts and 2026-11-19 dates, GHSA-qc49, 658j, fm2m, g3vh, 2fjv, 8mjj, gr4f, jm4m facts, CNA scores 9.2/8.8 and ranges, NCSC.ch status, watchTowr. Ruby: ruby-lang announcement, seven GHSA severities (3 Critical, 3 High, 1 Moderate), Veria table, product list and 25 November date, NCSC.ch, EUVD 7.4 AV:L/AC:H, watchTowr. OpenScape: advisory table, versions, workaround and fix quotes, CERT-FR and BSI CSAF wording. USI: three press relays against the Italian originals; evidence `original:` is verbatim. Updated entries: Zammad DIVD case and overview pages (19 h, 41,000 titles, 207, two, seven, GitLab token, Slack key, OAuth tokens), Puppet EUVD-2026-116493, OpenVox GHSA-q4hm (patched 9.2.0 and 8.18.0 incl. OpenVoxDB), Neodyme, SecurityWeek, NCSC.ch 13204, KEV dates and the CVE-2026-46300 chain note, CISA alerts via WebFetch, Java Elastic thread, Tanzu TNZ-2026-1107, PAN CVE-2026-114938 page, Calif raw HTML (17.0.6, ARM64, `-XX:UseAVX=2`), MiCollab EUVD records (each states "This is MTLVULN-nnnn"; CVSS 10.0, 9.0, 5.3, 5.9, 5.3; all published 2026-11-19 by mitre), Mitel MISA-2026-0012 page, CERT-FR dates, BSI CSAF, Turla ESET white paper and ReversingLabs page, ARTEX Commission transcript (22 and 26 October, "AI generated cyber campaign", no ransom request), POLITICO and Cyber Security News. Changelog contract: `updated_at` equals the record `at` for the three `update` records (Zammad, Java4Shell, ARTEX), is untouched by the four improvements, `fields` match `git diff HEAD` for all seven entries, record summaries match their sections. No IOCs, no em dash outside headings, no workflow vocabulary in reader-facing text.

### Verdict
NEEDS_FIXES (truth: 12, editorial: 5, advisory: 4)

Findings 1 and 2 are the only ones not marked low confidence: the PHP summary quantifier left from iteration 1, and a citation that does not carry its clause on the old PHP entry. The remaining truth items are small adjacency and attribution defects the main agent can fix by splitting clauses, rewording or re-citing.

### Findings summary (machine-readable)
See `work/2026-11-20T0356Z-intel/verification.iter2.findings.yaml` (21 records).
