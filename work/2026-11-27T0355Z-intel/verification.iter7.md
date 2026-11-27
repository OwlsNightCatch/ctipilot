**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T08:02:23Z · ended_at=2026-11-27T08:25:47Z · duration_seconds=1404

## Verification report — 2026-11-27T0355Z-intel (iteration 7)

Role: confirmation pass after the iteration-6 CLEAN. Read cold: all 11 entries (2 new, 9 updated, each with `git diff HEAD`), the run record, the dedup context and every one of the 328 ledger claims against pages fetched in this iteration (97 cited URLs through `extract` or the structured recipes; the 209-page DIVD forensic report through `pdf`; the KEV catalogue 2026.11.25 through `cisa-kev`; NCSC.ch posts 13203, 13205 and 13244 through `ncsc-csh post`; both cisa.gov alert pages through WebFetch with the outbound-links template; the two lore.kernel.org pages through the saved raw copies under `work/2026-11-27T0355Z-intel/fu1/`, whose text matches the ENISA record, OpenSec and watchTowr). Claim verdict rows: `work/2026-11-27T0355Z-intel/verification.iter7.claims.yaml` (328 rows: 326 ok, 1 F3, 1 F4; none unreadable).

Gate state re-run read-only: 60 pass, 0 warn, 1 fail (`verification-confirmation`, the check awaiting this pass). The one quote not machine-checkable (NCSC.ch post 13244, "Audit the fleet list for router names your team did not create.") is verbatim in the `ncsc-csh post 13244` content.

Known and deliberate items from the brief (Zammad main analysis over 550 words, Fragnesia at 550, long summary fields) were not re-raised; neither has grown.

### Unsupported / hallucinated facts

**#1 (F4) Zammad, `## Update — 2026-11-27T04:56:00Z`, Contradiction paragraph.** Entry: "…puts the CISO notification at 15:06 (…); neither source reconciles the two, so the entry quotes both." The cited case page (https://csirt.divd.nl/cases/DIVD-2026-00014/, last modified 25 Nov 2026 14:10 CET) carries a metrics table directly under its "19 hours" sentence: "Mean Time to Acknowledge (MTTA) | 07:20:51 | Time between first alert and SOC pickup" and "Mean Time to Respond (MTTR) | 19:16:51 | Time between first attack and formal response" (and "Mean Time to Contain 27:40:51"). All three durations count from the alert at 19:43:09 UTC: +7:20:51 is 03:04:00 (the report's first look), +19:16:51 is 15:00:00 (the report's CISO notification at 15:06), +27:40:51 is 23:24:00 (containment). So the case page itself separates pickup from formal response, and the entry's "neither source reconciles the two" misstates it. Fix: state that the case page's table gives 7 h 21 min to acknowledgement and about 19 h to formal response, matching the report's 03:04 pickup and 15:06 CISO notification, and keep a Contradiction line only for the shared wording "first response". Ledger claim 538f7f103c (the cited fragment) is marked F4 for this.

### Citation does not support the claim

**#2 (F3, low confidence) Zammad, same section, first paragraph.** Entry: "a Zammad administrator account and API token named with an artex- prefix and a number". The report's list of artefacts containing the term "artex" gives the API token `artex-i13033` and the account `artex.ops@divd.nl` (Table "Installed backdoors": account created and "granted admin rights"). The account has neither the hyphen nor a number. Fix: "an API token named artex- plus a number and an administrator account named artex.ops". Ledger claim 9449bd212e (marked F3).

### Editorial / less-is-more flags (advisory)

**#3 (F11, low confidence)** NFS2ROOT `sourcing_note` narrates the fetch path ("sits behind a bot challenge and was read through its raw form"); carried from iteration 6.
**#4 (F11, low confidence)** Mitel `## Update — 2026-11-26T05:05:30Z` closes "No source read names an exploiting actor, a victim or the number of systems hit", which reads stale beside the 2026-11-27 APEX section; carried from iteration 6.
**#5 (F11, low confidence)** Puppet update: "about two hours earlier"; Huntback's timestamps give 2 h 35 min (06:04:17 to 08:39:58) and its brief says "Two and a half hours earlier"; carried from iteration 6.
**#6 (F11, low confidence)** Mitel Detection line carries the path strings `/awcuser/cgi-bin/` and `/pictures/`; hunt locations rather than attacker infrastructure, but APEX lists the `/pictures/` shell path as an indicator. May be left.

### What held

- Fragnesia, PAN-OS: PAN-SA-2026-0015 (timeline initial publication 2026-11-24T23:10Z, page header 2026-11-25, CVSS block zero, Informational) and CVE-2026-109618 advisory builds compared train by train: every kernel-flaw build is two to four hotfixes after the PHP2Shell build; KEV 2026.11.25 dateAdded 2026-10-28 for CVE-2026-46300 and 2026-10-26 for both PHP flaws.
- Mitel: APEX page (Last-Modified Tue 24 Nov 2026 18:22:52 GMT, "Published November 2026"), Exhibit 1 timeline, BSI CSAF revision 2 (2026-11-25, critical, "Aktive ausnutzung gemeldet"), KEV five Mitel CVEs on 2026-11-25, MISA-2026-0012 revision 2.0 and MISA-2026-0006 all match the entry; ATT&CK T1685.006 is the pin's replacement for T1070.002 (log clearing).
- nginx: nginx.org advisories (CVE-2026-132779 vulnerable 1.21.4 to 1.31.9), CHANGES and CHANGES-1.30 (both 23 Nov 2026), F5 Plus notes (37.3.1.1 and 37.0.9.1 each carry the single ssl_early_data fix), Veeam KB4976 (published 2026-11-20, last modified 2026-11-25), GitLab 19.6.2, Synology SA-26:20, CERT.at, NCSC-NL scores, Xint exposure table; F5 K000163947 is an application shell (confirms the stated gap).
- Ruby: all four GitHub Enterprise Server release-notes pages (3.22.6, 3.21.11, 3.20.13, 3.19.17, all November 22, 2026, CRITICAL Ruby update), GitLab 19.6.1 and 19.6.2 backport text, Veria page (Updated 21 November 2026 03:52 UTC; PoC date 25 November), Durendal timeline; the "no release found on 2026-11-27" statement holds (Veria blog index, RSS feed, GitHub organisation: no Ruby2Shell PoC).
- Juniper: SecurityWeek (2026-11-26; Tuesday update, Wednesday KEV), NCSC.ch 13244 (Actively Exploited, provisioning-service prerequisite, fleet-list audit), BSI CSAF revision 2 (2026-11-24T23:00Z), ENISA records, EPSS 0.0086 for 2026-11-25 (FIRST API).
- ARTEX, Puppet: Wiz intent-ID, Harvester and Huntback pages, GTIG numeric markers, Huntback decoy timing (1.47 s, 1.4 s, four other products) and advice, Neodyme/OpenVox/EUVD/Red Hat/oss-security/Vox Pupuli.
- Zammad: every timestamp, count and quote in the new section checked against the forensic report (alert 19:43:09, pickup 03:04, CISO 15:06, isolation 23:24, 990 payloads and 3,259 output files, ~39 hours of cloud interaction, omniauth offline-access backdoor that captured nothing, Jira and Confluence remember-me injection, Table 19 credentials including the Google OAuth client secret in an exfiltrated file, deny-by-default segmentation and containerisation recommendations).
- SoftwareOK: ASEC text, SoftwareOK release dates (Q-Dir 12.83 4 Nov, 12.84 13 Nov, 12.85 21 Nov; DesktopOK 12.82 28 Oct, 12.85 19 Nov) and the download page without a tamper notice.
- NFS2ROOT: saved kernel announcement (four fixed branches, introduced in 3.16), ENISA EUVD-2026-130020 (dateUpdated Nov 23, eight fixed versions), OpenSec (private exploit, exposure test, hunt list, mitigation), watchTowr (no exploitation as of Nov 26; restrict 2049 or turn off NFSv4.1/4.2), Red Hat page and Hydra record (RHEL 8 RHSA-2026:103817 on 2026-11-26; RHEL 9 and 10 affected; 9.4 against the CVE record's 9.8), Debian tracker, Ubuntu page (last updated 25 November 2026, all releases 16.04 to 26.10 vulnerable). OpenSec credits Jérémy Jean (ANSSI) as independent finder of the 2026-08-17 upstream fix; the entry does not say OpenSec was first, so no defect.
- Dedup and coverage: no earlier entry carries CVE-2026-99362 or SoftwareOK; Vates and Danfoss KEV additions of 2026-11-25 are covered by earlier entries; NCSC.ch hub listing and two WebSearch sweeps found no uncovered critical or high item in the window ("coverage looks complete"). Priorities, classification blocks (A2, A1, B2, single-source B2) and `actions[]` lists are consistent with the bars; no org_triage or watchlist use; no IOCs beyond note #6.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-11-27T0355Z-intel/verification.iter7.findings.yaml`.
