**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-20T06:47:00Z · ended_at=2026-11-20T07:06:10Z · duration_seconds=1150

## Verification report — 2026-11-20T0356Z-intel (iteration 4)

Scope: post-fix pass after iteration 3 (NEEDS_FIXES). Ledger `claims.iter4.yaml` (322 claims). Verdict rows in `verification.iter4.claims.yaml`: 249 = every changed claim (15), every claim of the five remediated entries (Zammad 48, PHP 8.5.13 27, Puppet 29, Ruby 17, OpenScape 4000 12), every claim of vCenter (24), USI (6) and Turla (16), and a sample of the rest (Java4Shell 15 of 28, MiCollab 12 of 25, ARTEX 11 of 25, old PHP 22 of 65: 60 of 189, above the quarter). 248 ok, 1 F3, 0 unreadable. Every cited page was re-fetched this iteration (`extract`, `url`, `pdf`, `ncsc-csh post`, `bsi-csaf`, EUVD/CNA JSON, raw HTML where trafilatura dropped sections; WebFetch for the one cisa.gov page); usi.ch and the portal pages were not needed (relays read).

### Iteration-3 fixes (all re-checked against pages fetched this iteration)
- #1 Ruby / Veria: the live page (dateModified 2026-11-20T06:30Z) lists "GitLab | 19.6.0 and earlier | 19.6.1, 19.5.8, 19.4.10 | Patched", GHES and Chatwoot "None | Vulnerable"; the entry sentence matches. Confirmed.
- #2 Zammad 7.2.3: https://zammad.com/en/product/releases/7-2-3 ("Zammad 7.2.3: Critical Security Update", 2026-11-11) carries "addresses several vulnerabilities", the nginx/Apache2 `Remote-User` line next to `X-Forwarded-User` and "The Docker images apply this change automatically"; actions[0], cves[].fixed, the takeaway, the section and the record summary claim exactly that. The github advisory feed (43 advisories on 2026-11-11, `<= 7.2.2`, patched 7.2.3) agrees. `git diff` shows only changes the record's `fields` name. Confirmed.
- #3 PHP CVE-2026-129291: GHSA-jm4m "A root FPM master permits escalation from the pool user to root. If the master runs as an unprivileged user, successful exploitation is limited to that user's privileges"; the entry now carries the root-master condition. Confirmed.
- #4 PHP CVE-2026-129474: GHSA-8mjj "php.ini-production sets zend.exception_ignore_args=1 and prevents this attack path ... setting fatal_error_backtraces=0 also prevents this attack path"; body and cves[].affected now name both. Confirmed.
- #5 and advisories: record summary says "completed" (DIVD: "The forensic investigation of the breach has been completed"); OpenScape entities and stray stop fixed; Puppet affected/fixed now carry Puppet Core 9.1.3 and 8.22.2 (THN, SecurityWeek). Confirmed.

### Citation does not support the claim
#### F3 #1 (low confidence) Java4Shell: Cisco product count is stale
Quotes: summary "Cisco lists 13 products as affected with no fixed release yet"; body "Cisco lists 13 products, Catalyst Center, Secure Network Analytics and Secure Workload among them, as affected with the fixed release still to be determined ([Cisco, 2026-11-18])". The advisory (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-nov2026-java-rce-eCa6ss9z) is at revision 1.2, 2026-NOV-19 ("Updated the status of affected products"); its affected table now lists 21 products plus Catalyst Center in the priority table, several with a target release still marked (TBD). The count was true of the 2026-11-18 revision and the entry was updated this run, so the stale figure ships on a re-floated entry. Fix: restate from revision 1.2 or drop the number.

### Unsupported / hallucinated facts
#### F4 #2 (low confidence) Ruby: tag `poc-public`
`tags: [vulnerabilities, rce, pre-auth, poc-public, patch-available]`. Body and sources: Ruby "aware of PoCs", Veria "We'll be publishing a proof of concept ... on 25 November 2026", NCSC.ch "Proof of Concepts will become available in a week"; no cited source shows a public PoC, and `cves[].status` is only `patch-available`. Fix: drop `poc-public` until the PoC is out, or cite a public PoC.

### Missed angles
#### F10 #3 (low confidence) Old PHP entry: VulnCheck's 2026-11-10 expansion to unpatched branches
https://www.vulncheck.com/blog/php2shell-vulnerabilities (already cited): "As of November 10, the team has added RCE support for the following older PHP versions ... PHP 7.4.10-7.4.33, PHP 8.0.15-8.0.30, PHP 8.1.10-8.1.34". The `critical` entry, touched this run, says only that 8.1 and older need a backport. Search: "VulnCheck PHP2Shell exploit PHP 8.1 8.0 7.4 support November 10".

### Editorial / less-is-more flags (advisory)
- #4 Zammad: headline and summary still present 7.2.2 as the newest fix; 7.2.3 lives in actions, cves[].fixed, takeaway and the section.
- #5 vCenter: affected_products lists SDDC Manager and VMware Tools but entities omit product:vmware-sddc-manager / product:vmware-tools; Java4Shell lists Elastic Logstash but entities omit product:elastic-logstash (all registered this run).
- #6 Ruby (very low): NCSC.ch words the third Critical as "a regex size overflow during compilation"; "integer overflow" is the Ruby announcement's wording.
- #7 Old PHP (very low): "8.2.36 ... carry the follow-up fixes" while CVE-2026-129481 and CVE-2026-129182 do not apply to 8.2.

### Whole-run notes
Run record notes checked for truth: five new files and seven updated ids exist; KEV statement holds (catalog 2026.11.18, no addition in the window); the dropped F5 and borderline-drop lines are consistent with the store; NCSC.ch hub latest 15 posts (13198 to 13212) are all covered by entries or earlier entries, so no missed home-region angle. Priorities: vCenter `high` is defensible against the critical bar (one documented targeted intrusion, Broadcom does not state exploitation, "if unsure, it is high"); Ruby `high` (dated exploit announcement), PHP and OpenScape `notable`, USI `routine` hold. Classification letters and credibility numbers are consistent with the sources shown. No IOCs, no em dashes outside headings, no workflow vocabulary in reader-facing fields. The USI body length and the PHP `auth: pre-auth` advisories from iteration 3 stand as advisory.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 1, advisory: 4)

### Findings summary (machine-readable)
See `verification.iter4.findings.yaml` (7 records).
