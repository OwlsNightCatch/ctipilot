**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T05:38:19Z · ended_at=2026-11-27T06:03:37Z · duration_seconds=1518

## Verification report — 2026-11-27T0355Z-intel (iteration 2)

Scope: 2 new entries, 8 updated entries (each read whole, `git diff HEAD` read, record `fields` checked against the diff), the run record, all 295 ledger claims (every claim has a row in `verification.iter2.claims.yaml`: 290 ok, 5 non-ok). Pages were read this iteration from the gate's cached bodies and live (extract, url, pdf, ncsc-csh, cisa-kev, curl -I for the APEX Last-Modified header, first.org EPSS). The one quote the gate could not check (NCSC.ch post 13244, "Audit the fleet list for router names your team did not create.") is verbatim on the post.

### Prior-iteration deltas (23 findings), re-checked against the sources

1. PAN-OS "two to four hotfixes": PHP2Shell record builds (12.2.4-h1, 12.1.4-h13, 12.1.7-h11, 12.1.10-h3, 11.2.x-h16 to h23, ... 10.2.18-h13) against PAN-SA-2026-0015 builds (12.2.4-h3, 12.1.4-h15, 12.1.7-h15, 12.1.10-h6, ...): differences run 2 to 4 (4 for 12.1.7). Correct.
2. SoftwareOK hedge: ASEC "may not remove a Python RAT"; title, headline, action, takeaway now carry "may not". Correct.
3. Ruby attribution: NCSC.ch 13205 "Rails and classic-style Sinatra are exposed by default"; watchTowr kept for "As of November 19, 2026, no exploitation in the wild has been reported." Correct (watchTowr's page also says Rails and Sinatra are affected by default, so iteration 1's premise was partly wrong; the fix introduces no defect).
4. Mitel BSI: CSAF WID-SEC-W-2026-4608 aggregate_severity "kritisch", revision 2 of 2026-11-25T23:00Z "Aktive ausnutzung gemeldet, Bewertung angepasst, CVE's ergänzt"; the entry now says so. Correct.
5. Zammad CISO: report timeline "2026-09-22T15:06:00Z DIVD CISO informed of a possible attack". Correct.
6. Zammad contradiction: case page "it took us 19 hours to initiate our first response on 22 September 2026" and report "The first response to these alerts was observed on Sep 22nd 2026 at 03:04 UTC" are both quoted; no "therefore". Correct.
7. nginx: CHANGES (1.31.10, 23 Nov 2026), CHANGES-1.30 (1.30.8, 23 Nov 2026), security_advisories "Vulnerable: 1.21.4-1.31.9". Correct.
8. Ruby GHES: the four release-notes pages each carry the CRITICAL Ruby line with 3.22.6, 3.21.11, 3.20.13, 3.19.17 dated November 22, 2026. Correct.
9. Juniper: "before BSI's revision" removed; "before CISA's listing" fine (SecurityWeek: Juniper "On Tuesday", CISA "On Wednesday"). But see new finding F3 below.
10. Puppet decoy: Huntback "Our decoy signed the certificate, accepted the report with a 200, and returned no marker." Correct.
11. APEX date: HTTP `last-modified: Tue, 24 Nov 2026 18:22:52 GMT` confirmed; page says only "Published November 2026". Correct (one uncited side clause, F5 below).
12. ARTEX triage: limited to the two ConnectWise applications Expel reviewed. Correct.
13. Zammad blog: https://csirt.divd.nl/2026/11/25/full-disclosure-our-hack/ dated 25 Nov 2026, now cited. Correct.
14. PAN-OS KEV: catalogue 2026.11.25, CVE-2026-46300 dateAdded 2026-10-28. Correct; the sentence around it has a new problem (F4 below).
15. Juniper Router: KEV record, NCSC.ch 13244 and SecurityWeek (7.2.3, 7.1.7, 7.0.5 for both products) support the added Router coverage.
16. nginx Veeam: KB4976 lists the Plug-In appliances (install all updates through Veeam Updater) and Backup for Salesforce 3.2.1 (OS vendor update or disable HTTP/2). Correct.
17. F18: Mitel actions[0] and Zammad actions[0] are acceptable now; nginx and Juniper residue below.
18. PAN-OS pipeline narration removed. Correct.
19. SoftwareOK path and task name removed. Correct.
20. Zammad main analysis 1,030 words (1,068 at HEAD): not re-raised, did not grow.
21. Mitel headline attributes the exploitation to APEX; the six added techniques (T1068, T1041, T1105, T1087.002, T1552.001, T1572) are all in APEX's own ATT&CK table; T1685.006 is the v20.1 id for Clear Linux or Mac System Logs. Correct.
22. NFS2ROOT event_date 2026-11-19: kernel announcement "Date: Thu, 19 Nov 2026", Red Hat public_date 2026-11-19T14:22:44Z, EUVD datePublished Nov 19, 2026. Correct.
23. Puppet retype: the record is `type: update` with `at` = `updated_at` = 2026-11-27T04:58:00Z and a section. Correct in the entry; the run record still calls it an improvement (F4 below).

### Citation does not support the claim (F3)

- #1 `juniper-...` summary, sourcing_note: "was updated on 2026-11-24 to say at least one malicious exploitation was reported to its security response team, as SecurityWeek and NCSC Switzerland relay it"; sourcing_note "reaches the record through SecurityWeek's quotation and NCSC Switzerland's post". NCSC.ch 13244 says only "Current exploitation status: Actively Exploited", with JSA112183 as source advisory; the "At least one instance ... reported to the Juniper SIRT" wording and the Tuesday update are SecurityWeek's alone. Credit NCSC.ch with its own rating only. (The body and record summary are worded correctly; the summary and sourcing_note are not.)
- #2 (low confidence) `artex-...` update: "its posts do not mention Storm-0940". The two cited Wiz posts do not, but the entry's earlier Wiz citation is titled "ARTEX in the Wild: Storm-0940 Expands Targeting of IT and Software Vendors". Say "these two posts".

### Unsupported / hallucinated facts (F4)

- #3 (low confidence) `pan-os-...` update: "so the vendor now states exploitation of the second half of the chain, which until then rested on Dream's account alone; CISA's catalog lists the kernel flaw as exploited, added on 2026-10-28". The cited KEV record (dateAdded 2026-10-28, "can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and run commands as root") predates the 2026-11-24 bulletin, contradicting "alone ... until then" in the same sentence; no source says CISA's listing derives only from Dream.
- #4 (low confidence) `softwareok-...` body: "a package holding a Python 3.9 runtime and a custom remote-access tool". ASEC: "Package containing a Python runtime environment and a RAT"; only py39 paths; no "custom".
- #5 run record notes: "`improvement` on the Puppet entry (Huntback decoy capture)". The Puppet record is now `update`; all 8 records are `update`.
- #6 run record notes: "the Zammad entry's main analysis now states both and the report's containment time". The 19 hours / 7 h 21 min statements and the Contradiction paragraph are in the 2026-11-27 Update section; the main analysis has neither.

### Analytical-link-as-fact (F13)

- #7 (low confidence) `softwareok-...`: "SoftwareOK's release pages date Q-Dir 12.83 to 4 November ... which sets the earliest possible exposure". ASEC gives no distribution window and says other versions installed or updated during the distribution period may be affected; release dates bound only the listed versions. The action's "since 2026-10-28" is the entry's own reading.

### Claims missing inline citation (F5)

- #8 (low confidence) `mitel-...` sourcing_note: "SecurityWeek covered it on 2026-11-26". True (securityweek.com/mitel-micollab-zero-days-exploited-in-suspected-ai-assisted-attacks/, dated 2026-11-26) but uncited and not in sources[].
- #9 (low confidence) `pan-os-...` Exposure line after the trim: "it is reachable from the internet where the management port, or a dataplane interface with a management profile, answers from outside the administrator range" has no citation; PAN-SA-2026-0015's FAQ supports it.
- #10 (low confidence) `zammad-...` Contradiction paragraph: the report quote ("The first response to these alerts was observed on Sep 22nd 2026 at 03:04 UTC") and the CISO time have no citation terminating their clause.

### Missed angles (F10)

- #11 (low confidence) The Fragnesia entry (entries/2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x.md) did not receive PAN-SA-2026-0015 (vendor-stated exploitation of CVE-2026-46300, later fixed builds) while the PAN-OS entry now carries a `cves[]` record for the same CVE; its takeaway still says only "apply Palo Alto's PHP2Shell fixes". Add a changelog record or note why not. No other in-window omission found: the KEV additions (Juniper, five Mitel, Vates, Danfoss) are covered, Drupal SA-CORE-2026-019, GeoServer and AntiCsrf are covered by existing entries, and NCSC.ch's recent posts add nothing uncovered. Coverage looks complete for the critical/high signal.

### Action-item discipline (F18)

- #12 (low confidence) nginx actions[0] installs the same PAN-OS builds as the PAN-OS entry's actions[0] (duplicate, F18 d); nginx actions[1] still bundles nginx and Veeam appliances; Juniper actions[0] folds the body's hunting and fleet-audit steps into the upgrade task (F18 b).

### Editorial / less-is-more flags (advisory, F11)

- #13 nginx headline names "update 1.31.9, 1.30.7 or Plus 37.3.0.1" although the new section says "the update target moves" (title and headline not in the record's fields).
- #14 Juniper sourcing_note: "script-rendered shell no transport read" is fetch-pipeline language; use "could not be read".

### Checks that came out clean (no finding)

NFS2ROOT: announcement text and four fixes (raw capture), EUVD eight fixed branches (updated Nov 23), Red Hat API (RHEL 8 RHSA-2026:103817 on 2026-11-26, RHEL 9 and 10 Affected), Debian, Ubuntu (all releases 16.04 to 26.10 Vulnerable, updated 25 Nov), OpenSec exposure test and hunt list, watchTowr "As of November 26, 2026, no exploitation", the three evidence quotes. SoftwareOK: versions, release dates, 1,206 names, hedges, no vendor notice. Mitel: every APEX offset, the UTC-12 to UTC+1 gloss, second victim since 9 Nov, CERT-FR first version 17 November 2026, Mitel revision 2.0. PAN-OS: bulletin timestamp 2026-11-24T23:10Z, zero CVSS block, 20 build strings both ways. nginx: Plus 37.3.1.1 and 37.0.9.1 security-only releases of Nov 23, KB4976, GitLab 19.6.2 page, Unit 42 reload and HTTP/2 caveats. Ruby: Veria "Updated 21 November 2026 at 03:52 UTC", PoC 25 November 2026, blog and GitHub org (4 repos) show no release, Sanft credit and timeline. Juniper: EUVD ranges, EPSS 0.0086 on 2026-11-25, BSI revision 2026-11-24T23:00Z. Zammad: every chain timestamp (18:53:50, 1.3 s, 19:06:31, 19:27:58, 19:45:59), 990 / 3,259, 41 thousand, 39 hours to 08:33, the TLS, segmentation and containerisation recommendations, 7 h 21 / 19 h 23 / 27 h 41. ARTEX: Wiz intent-ID and Harvester posts, Huntback console, GTIG markers, Expel. Puppet: Huntback chain and advice, EUVD, Red Hat 9.9, release notes CVE list. Every record's `fields` covers its diff; `updated_at` equals the update `at` on all eight; no em dash outside headings; no workflow vocabulary beyond #14; classification letters match sources.json tiers; no new-entry overlap with prior coverage or cves_seen.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 5, advisory: 2)

### Findings summary (machine-readable)

See `work/2026-11-27T0355Z-intel/verification.iter2.findings.yaml` (14 records).
