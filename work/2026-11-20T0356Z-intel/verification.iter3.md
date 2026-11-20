**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-20T06:22:25Z · ended_at=2026-11-20T06:45:10Z · duration_seconds=1365

## Verification report — 2026-11-20T0356Z-intel (iteration 3)

Scope: post-fix pass after iteration 2 (NEEDS_FIXES). Claim ledger `claims.iter3.yaml` (317 claims): every changed claim (33), every claim of the ten entries the deltas block names (zammad, old PHP, ARTEX, Turla, Puppet, vCenter, PHP 8.5.13, OpenScape 4000, USI, Ruby), all 25 MiCollab claims and 14 Java4Shell claims (7 random older ones plus the 7 new-section claims), 303 rows in `verification.iter3.claims.yaml` (297 ok, 2 F3/F4-or-F14 pairs listed below, 2 unreadable). Every cited page was re-fetched this iteration (`extract`, `url`, `pdf`, `ncsc-csh post`, CSAF/CNA JSON for the SPAs, WebFetch for cisa.gov); unreadable on every rung: community.citrix.com (403) and the web.archive.org copy of the Palo Alto advisory (empty body).

### Iteration-2 fixes (all 21 checked against the fetched sources)
Confirmed correct: #1 php summary (18 CVEs per branch confirmed against php.net ChangeLog-8, 8.5.13 = 18 CVEs, 8.4.28 = 14, 8.3.37 = 13, 8.2.36 = 12), #2 old PHP no-exploitation now cited to watchTowr ("As of November 20, 2026, no exploitation in the wild has been reported."), #3 PHP 8.1 (GHSA-jm4m sidebar: Patched versions None for 8.1.20-8.1.34), #5 DIVD splice fixed (41,000 titles vs Jira/Confluence 207 emails, two phones, seven pictures), #6 and #7 ARTEX (POLITICO "Disruption has lasted over 10 days"; Commission transcript names no tool), #8 Ruby sourcing note (Veria: "found this vulnerability independently and was the first to demonstrate remote code execution"), #9 OpenScape clause removed, #10 vpxuser/root, #11 Puppet (THN quotes a "115731 intrusion"; NCSC.ch lists the Reddit report as an additional source), #12 improvement type, #13 and #14 PHP 129474 and vCenter TCP 2012 (GTIG Table 1 plus "rigorous testing"), #15 VMware Tools both ranges, #16 NCSC.ch measures cited, #17 DIVD section reworded (record summary still says "closed", advisory below), #18 Detection wording, #19 improvement kept, #20 Turla (attribution basis present; ESET blog and PDF support every sentence), #21 USI (translation marker present; window 2026-11-09 to 2026-11-17 matches all three outlets). #4 (pre-auth kept on CVE-2026-126714 / 129481) stands as advisory, see F11.

### Claim does not support / unsupported (truth)

#### F3 #1 Ruby: Veria's GitLab status changed after composition
Quote: "Veria lists GitLab 19.6.0 and earlier, GitHub Enterprise Server 3.22.5 and earlier and Chatwoot 4.20.0 and earlier as having no fixed release and Mastodon, OpenProject and the Discourse base image as patched" (https://verialabs.com/ruby2shell/). The live page ("Updated 20 November 2026 at 06:00 UTC") reads: "GitLab | 19.6.0 and earlier | 19.6.1, 19.5.8 | Patched". The saved 04:29 UTC copy said "None / Vulnerable", so the entry matched the page when written; the page moved. Only GHES and Chatwoot remain unfixed in Veria's table. Fix: restate GitLab as patched (19.6.1, 19.5.8 per Veria) and re-read the page right before publish.

#### F4 #2 Zammad: "7.2.2 is the current release" and the upgrade target are stale
Quotes: `cves[CVE-2026-102489].fixed` "7.2.2 (2026-10-08) is the current release"; actions[0] "upgrade it to Zammad 7.2.2 (7.2.0 is affected by the 27 advisories ...)"; takeaway "upgrade to Zammad 7.2.2 after saving the logs". Evidence: https://zammad.com/en/product/releases/7-2-3 ("Zammad 7.2.3: Critical Security Update", 2026-11-11) and the GitHub advisory feed the entry itself cites (https://api.github.com/repos/zammad/zammad/security-advisories?per_page=100): 43 advisories published 2026-11-11, all "<= 7.2.2", patched "7.2.3", 2 critical (GHSA-pv63-rf47-cj6r "Unauthenticated creation of administrator accounts during a data migration"; GHSA-9x94-gcq4-jjgw "Encrypted or signed incoming email could reintroduce privileged headers past the untrusted-mail filter"), 10 high. 7.2.2 is therefore an affected build and no longer the current release. This run updated the entry, so the stale upgrade target ships. Fix: retarget to 7.2.3 or later and say why (see F10).

#### F3 #3 (low confidence) PHP 8.5.13: CVE-2026-129291 "gives root"
Quote: "CVE-2026-129291, an epoll use-after-free in PHP-FPM, gives root from a worker where catch_workers_output is on". GHSA-jm4m-qfqx-967m: "execute commands with the privileges of the FPM master, which commonly runs as root" and "If the master runs as an unprivileged user, successful exploitation is limited to that user's privileges"; NCSC.ch: "yields root command execution when the FPM master runs as root". The root-master condition is dropped. Fix: "gives the FPM master's privileges, commonly root, to code already running in a worker".

#### F14 #4 (low confidence) PHP 8.5.13: "only php.ini-production ... prevents the attack"
Quote: "and only php.ini-production, which sets zend.exception_ignore_args=1, prevents the attack". GHSA-8mjj-2r7p-4hg2: "On PHP 8.5 and later, setting fatal_error_backtraces=0 also prevents this attack path" and the immediate workaround is setting zend.exception_ignore_args=1 in the workers' configuration. "only" is the entry's quantifier; the source names more than one preventing setting.

### Missed angles
#### F10 #5 Zammad 7.2.3 (2026-11-11)
Nothing in the store covers it; the existing Zammad entry (priority high, Zammad is common in public-sector helpdesks) is the place for an update record. Search: "Zammad 7.2.3 security release GHSA-pv63-rf47-cj6r GHSA-9x94-gcq4-jjgw". Everything else checked (Chrome CVE-2026-125350, Outlook CVE-2026-124194, Cisco SD-WAN CVE-2026-20245, Cisco Secure Email CVE-2026-76519) is already in the store; KEV catalog 2026.11.18 has no addition inside the window.

### Editorial / less-is-more flags (advisory)
- #6 Zammad record summary still says "DIVD closed its forensic investigation" (section says "completed"; DIVD's case Status is "Open").
- #7 OpenScape 4000: stray full stop before the citation in the Exposure line; `entities: []` although product:mitel-openscape-4000 and -manager were registered this run.
- #8 PHP 8.5.13: `auth: pre-auth` on CVE-2026-126714 and CVE-2026-129481 while the GHSAs say authentication requirements depend on the application path (CNA vector is PR:N; advisory only).
- #9 Puppet: CVE-2026-115731 `affected`/`fixed` omit Puppet Core although THN, SecurityWeek and the entry's own action name it.
- #10 USI: routine incident body is longer than the two-sentence limit (nexus justifies keeping it).

### Whole-run notes
Run record notes checked for truth: update-versus-improvement for the old PHP entry, the vCenter `high` call, the dropped F5 entry (no file under entries/), 5 new files and 7 updated ids all hold on disk; the KEV statement holds against catalog 2026.11.18. Priorities: vCenter `high` (single targeted intrusion, no KEV listing yet) is defensible; Ruby `high` (dated public exploit announcement for 2026-11-25) and PHP `notable` hold. Classification letters and credibility numbers are consistent with the sources shown. No IOCs, no em dashes outside headings, no workflow vocabulary in reader-facing fields.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 5)

### Findings summary (machine-readable)
See `verification.iter3.findings.yaml` (10 records).
