**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-20T07:07:43Z · ended_at=2026-11-20T07:34:52Z · duration_seconds=1629

## Verification report — 2026-11-20T0356Z-intel (iteration 5)

Scope: post-fix pass after iteration 4 (NEEDS_FIXES). Ledger `claims.iter5.yaml` (324 claims). Verdict rows in `verification.iter5.claims.yaml`: 216 = every changed claim (3), every claim of the three remediated entries (old PHP 66, Java4Shell 29, Ruby 17), every claim of vCenter (24), PHP 8.5.13 (27), OpenScape 4000 (12) and USI (6), and the newest-section and record-summary claims of Puppet, MiCollab, Zammad, Turla and ARTEX; 209 ok, 5 F3, 2 unreadable (Citrix community page 403 on every transport, jina keys exhausted; the 2026-10-27 web.archive.org copy of the Palo Alto advisory is unreadable). The remaining 108 claims (older body claims of Puppet, MiCollab, Zammad, Turla, ARTEX) are not rowed; the 104 rowed claims outside the remediated entries are about half of the rest. Every cited page was re-fetched this iteration (`extract`, `url`, `pdf`, `ncsc-csh post`, `bsi-csaf`, EUVD and CNA JSON, raw HTML where trafilatura dropped text; WebFetch for the two cisa.gov pages).

### Iteration-4 fixes (re-checked against pages fetched this iteration)
- #1 Java4Shell / Cisco count: the summary and the Exposure sentence now say "Cisco lists affected products ... in an advisory it keeps updating"; the advisory (revision 1.2, 2026-NOV-19) says "This advisory will be updated as additional information becomes available." Confirmed for those two surfaces. The same stale count survives in `cves[0].fixed` (see F3 #1 below).
- #2 Ruby `poc-public` tag: removed (`tags: [vulnerabilities, rce, pre-auth, patch-available]`). No cited source shows a public PoC (Veria: PoC "on 25 November 2026", read from the page's `<time datetime="2026-11-25">`). Confirmed; see F10 #7 for an uncited public local reproduction.
- #3 old PHP / VulnCheck: https://www.vulncheck.com/blog/php2shell-vulnerabilities "As of November 10, the team has added RCE support for the following older PHP versions, all on AMD64 with the default memory settings and display_errors off: PHP 7.4.10-7.4.33, PHP 8.0.15-8.0.30, PHP 8.1.10-8.1.34" and "PHP 8.1 and older no longer receive supplier-provided patches". The Improvement sentence matches (it omits the display_errors condition, advisory). Confirmed.

### Citation does not support the claim
#### F3 #1 Java4Shell: `cves[0].fixed` still carries the stale Cisco count
Quote: "Cisco Catalyst Center, Secure Network Analytics, Secure Workload and ten more Cisco products: fixed release to be determined". Cisco revision 1.2 lists 22 affected products plus Catalyst Center in the priority table, and several now carry a target release marked "(TBD)" (Secure Network Analytics "7.6.0 (TBD)"). Fix: drop the count in the field, as was done in the summary and body.
#### F3 #2 (low confidence) Java4Shell: 2026-11-19 section carries superseded Tenable distro status
Quote: "as of 2026-11-18 Red Hat and Ubuntu had released no fix and Debian had fixed only its unstable branch, so hosts on those distributions had no stable vendor build yet". Tenable's page now: "As of November 19, Red Hat has released fixed OpenJDK packages for Red Hat Enterprise Linux ... Ubuntu released fixes for its openjdk-17, openjdk-21, openjdk-25 and openjdk-27 packages on November 18. Debian has fixed openjdk-21 and openjdk-25 in its stable release, Debian 13", and the Keycloak 26.8 images moved to 21.0.13.1. Fix: add the 2026-11-19 distro and Keycloak status to the newest section.
#### F3 #3 (low confidence) Ruby: regexp prerequisite stated for all regexp flaws
Quote: "The regexp flaws need an application that compiles, matches or stringifies an attacker-controlled pattern". NCSC.ch 13205: "Moderate flaw: A crafted subject string matched against a fixed pattern that uses a case-insensitive backreference" (GHSA-pvgc-g7gj-pv6h). Fix: scope the sentence to the flaws that allow code execution.
#### F3 #4 (low confidence) Old PHP: Cisco "(November 2026)"
Quote: "with fixes at 15.5.21, 26.2.1.9 (November 2026) and 3.2.0 ([Cisco PSIRT, 2026-10-30])". The advisory is now revision 1.11 (2026-NOV-06, Final): "Updated Ultra-Reliable Wireless Backhaul (URWB) and Unified Industrial Wireless Software as being available"; the fixed table shows 26.2.1.9 with no date.
#### F3 #5 (low confidence) Old PHP: Fortinet "under investigation"
Quote: "Fortinet keeps only FortiDDoS, FortiSOAR and FortiSOAR PaaS under investigation ([Fortinet PSIRT, 2026-10-26])". FG-IR-26-186 timeline: "2026-11-05: FortiSOAR and FortiSOAR PaaS added to impacted product list"; "Products Under Investigation: FortiDDoS"; FortiSOAR rows list fixes (8.0.1, upcoming 7.6.8 and 7.5.5), DoS only, CVSS 5.3.
#### F3 #6 (low confidence) Old PHP: GreyNoise start date
Quote (summary): "GreyNoise's sensors have recorded shell sessions since 2026-10-28"; Detection line "since 2026-10-28, on GreyNoise's sensors". The live tracker (as of 20 November) lists "2026-10-27 16:25:05 ... apache2 -> apache2" as the first shell, puts "First successful exploitation observed" one day after the KEV addition, and reports "1,304 successful exploitations, from 25 attacker IPs, against our vulnerable sensors". Fix: start date 2026-10-27 and, for a `critical` entry, the current tracker totals.

### Unsupported / hallucinated facts
#### F4 #7 (low confidence) Old PHP: two evidence quotes no longer on their pages
Quotes: "exploited a vulnerable GreyNoise sensor: apache2 spawned sh, which ran curl" (tracker now: "An attacker exploited a vulnerable GreyNoise sensor: apache2 spawned apache2, which ran setsid ./xmrigDaemon ...") and "Upgrade to corresponding available PAN-OS version." (SSA-566512 is V1.3 of 2026-11-18, "Updated Remediation area information", and says only "Contact customer support to receive additional patch and update information."). The 2026-11-01 section sentence "Siemens' advisory ... at version 1.1 of 2026-10-28, now tells operators to upgrade to the corresponding available PAN-OS version" is superseded in the same way. Fix: replace the quotes with fragments the pages carry (or drop them) and mark the Siemens sentence as the V1.1 wording.

### Missed angles
#### F10 #8 (low confidence) Ruby: public local reproduction
https://github.com/evenomn/CVE-2026-132825 (listed in the ENISA EUVD record the entry cites): independent root-cause write-up with ASAN crash reproduction and local no-ASLR weaponization of CVE-2026-132825 and GHSA-87fm-7w84-j2px; no remote delivery path built, an unmerged third-party Rails/Rack PR cited for the delivery hypothesis. The entry mentions only Veria's planned PoC. Search: "CVE-2026-132825 Ruby2Shell proof of concept github".

### Editorial / less-is-more flags (advisory)
- #9 Zammad: headline and summary still present 7.2.2 as the newest fix; 7.2.3 is in actions, cves[].fixed, the takeaway and the newest section (carried over).
- #10 Entity links missing although registry keys exist: Puppet and MiCollab `entities: []`, vCenter (SDDC Manager, VMware Tools), Java4Shell (Elastic Logstash).
- #11 Puppet `epss` 0.00366 (FIRST 2026-11-17) against 0.00691 on 2026-11-19; old PHP improvement record, VulnCheck sentence without display_errors, "follow-up fixes" for 8.2.36 (carried over).

### Whole-run notes
Run record checked for truth: five new files and seven updated ids exist; KEV statement holds (catalog 2026.11.18, no addition after 2026-11-18T19:17Z; CVE-2026-115731 added 2026-11-17 is covered by the Puppet entry); NCSC.ch hub latest 12 posts (13198 to 13212) all covered; no missed home-region angle found. `check_run.py` shows only the empty verification block and informational dedup warnings. Priorities: vCenter `high`, Ruby `high`, PHP 8.5.13 and OpenScape `notable`, USI `routine` hold; the old PHP entry stays `critical` (KEV, GreyNoise confirmed exploitation). Classification letters and credibility numbers are consistent with the sources. No IOCs, no em dash outside headings, no workflow vocabulary in reader-facing fields found.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 1, advisory: 3)

### Findings summary (machine-readable)
See `verification.iter5.findings.yaml` (12 records).
