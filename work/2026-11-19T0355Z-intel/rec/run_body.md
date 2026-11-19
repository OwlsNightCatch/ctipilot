
## Verification & coverage notes

Window 26 h (gap 24.0 h to `2026-11-18T0356Z-intel`). Six new entries and eight changelog records, no deep dive, no critical. The will-publish set was 14 items, over the ~8 a main-agent deep read should carry, so two scoped `cti-research` follow-ups read the primaries and returned claim tables whose passages were `grep -F` checked against saved bodies: DR1 (the six new entries, 2026-11-19T04:39:20Z to 05:05:15Z) and DR2 (the eight records, 04:39:21Z to 04:58:45Z); the main agent composed every entry and record from those tables and the findings files. Stop-hook commit nudges arrived mid-run and were not acted on; the commit follows the gate and the verifier loop.

**Coverage and dispositions**

- KEV sweep (`work/2026-11-19T0355Z-intel/kev-window.txt`): CVE-2026-90817 REDCap → new entry `2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev` (Unit 42 had seen exploitation since 2026-10-07, so the CISA listing was not the only evidence S1 reported); CVE-2024-10441 → `update` on the Synology DSM entry; CVE-2026-40217 → `update` on the LiteLLM entry (a v2-shaped legacy record, brought to the current schema in the same record: classification, techniques, affected_products, per-CVE fixed versions; the CVE's CVSS now follows the vendor advisory, 5.9, not an unsourced 8.8); CVE-2026-90436 → `improvement` on the Confluence entry (the store already described exploitation through N-able N-central; CISA's listing and Apache's no-fix and handler statements are the reader-facing delta, no re-float). No RANSOMWARE rows.
- Backlog: no open rows at the start. Two rows opened and held with named conditions: the PHP critical release pre-announced for 2026-11-19 14:00 to 14:30 UTC (expiry 2026-11-26) and the Basel-Landschaft cantonal-administration incident (no vector, actor or behaviour, so no evidence-bound technique; expiry 2026-12-03).
- Scheduled releases: Drupal core released 2026-11-18 (update on the pre-announcement entry, priority notable to high); NGINX and F5 2026-11-18 (new entry; BIG-IP rows dropped below); Oracle CSPU and TYPO3 carried by yesterday's entries with no revision; Microsoft revisions informational; Trend Micro KA-0024802 status of 2026-11-18 (update; DR2 corrected S1: the Mobile Security for Enterprise patch is on the Download Center dated 2026-11-17 although the advisory row still shows it pending).
- Revised advisories: HPE HPESBNW05162 revision 2 (update; the entry carried CVE-2026-79845, which revision 2 replaced with CVE-2026-95787, and the FIPS build is now in the fixed strings); Java4Shell vendor impact from Cisco and Fortinet plus the BACS warning page (update; the entry cited BACS's 2026-11-17 announcement page for a compromise-check quote that only the 2026-11-18 warning page carries, so the citation was moved); OptimJack (update; Optimizely's status entry now names the flaw).
- Source-slice rotation: 102 sources were excluded as attempted by the previous two fires; the breach pool (S4) is small, so nine of its ten records had to be drawn from recently attempted ones, oldest cursor first.
- Corrections to the sub-agents' findings applied at composition: S2's claim that NGINX Plus 37.2.0.1 and 37.0.7.1 also fix CVE-2026-113425 was wrong (F5's record: only CVE-2026-123633); tcherber's orchestrator automates only the VPN connect, route parsing and LDAP enumeration, SMB reconnaissance and port scanning are manual tools; S1's list of Fortinet products as affected by Java4Shell was dropped (all are under investigation); CERT-EU states no exploitation for the nginx2root flaws, NCSC-NL only predicts it.
- Single-source entries: Airlock Gateway (vendor CNA text via ENISA EUVD, corroborated by the vendor's release notes only), Idunno.AntiCsrf (Mandiant as CNA, sole observer of the exploitation; the CISA assessment entry in the CVE record lists exploitation as none), CyberPower PowerPanel (Symantec), tcherber (Cyderes; VMRay corroborates only the developer identity).
- Candidate sources: nginx-security-advisories, unit42-timely-threat-intel, polizeiticker-ch (added); mitel-security-advisories promoted. Two source_health UNSOLVED items (typo3-security-advisories, cnil-fr) got `health_cmd` fixes that were not re-probed because the tool has no single-source mode; the next audit's run confirms them.
- Operator signals: `lab52` has failed on every transport for six fires (newest post 2026-10-05); the jina reader pool is dead (HTTP 402); `cisa csaf-recent` returned only a legacy bulk re-publish.

**Borderline drops**

- borderline-drop: F5 BIG-IP K000164058 data-plane flaws — F5 BIG-IP K000164058: six data-plane flaws need non-default iRule commands or APM agents, no exploitation, F5 page unreadable
- borderline-drop: Ruby 4.0.10, 3.4.13 and 3.3.14 memory-safety fixes — Ruby regex/case-conversion memory-safety fixes: CVE ids pending, no exploitation, needs attacker-controlled regex or crafted strings; patch-cycle
- borderline-drop: Linux kernel NoisyTCP CVE-2026-99288 — NoisyTCP CVE-2026-99288: reliable effect is remote panic only, UAF path hard, discoverer exploit lab-specific; kernel patch cycle
- borderline-drop: Dell PowerStore DSA-2026-479 — Dell PowerStore DSA-2026-479: internal storage service rows, no exploitation, no stated footprint
- borderline-drop: Roundcube 1.6.21 and 1.7.6 — Roundcube 1.6.21/1.7.6: no CVE ids, no exploitation, patch cycle
- borderline-drop: Eclipse Mosquitto CVE-2026-110486 — Mosquitto CVE-2026-110486: websockets listener only, no exploitation, niche
- borderline-drop: Chrome 158 stable — Chrome 158 stable: 204 fixes, no exploitation statement, regular cycle
- borderline-drop: Juniper JSA119568 Junos OS Evolved kernel TCP — Juniper JSA119568 Junos OS Evolved kernel TCP: vendor impact on an already-covered flaw, fix announced for later, no new action
- borderline-drop: Broadcom AutoSys CA20261117-01 — Broadcom AutoSys CA20261117-01: internal scheduler console, no exploitation, no stated footprint
- borderline-drop: EU sanctions on NoName057(16) — EU sanctions NoName057(16): no defender-side decision change
- borderline-drop: Canton Bern ICSG in force 2026-11-01 — Canton Bern ICSG in force 2026-11-01: sources dated 2026-09/10, outside window, awareness only
- borderline-drop: UAT-12643 (Talos) — UAT-12643 Talos: low-confidence DPRK attribution, Europe only potentially, no constituency nexus
- borderline-drop: AuditTeam and OpsAgent (Securelist) — AuditTeam/OpsAgent Securelist: single source, signed-driver killer and GitHub C2 are known classes; Italy/Finland victims only
- borderline-drop: Check Point State of Ransomware Q3 2026 — Check Point State of Ransomware Q3 2026: leak-site statistics report, stats not defender decision; feed stamp outside window
- borderline-drop: Elastic analysis of the agent-framework compromise — Elastic agent-framework analysis: third analysis, no material delta on the covered entry
- borderline-drop: Docker Model Runner (ZDI) — ZDI Docker Model Runner: non-default configuration, single source
- borderline-drop: ROMULUS and CNCMachineRMS (Blackpoint) — Blackpoint ROMULUS/CNCMachineRMS: family naming, no victim or post-exploitation
- borderline-drop: Equinor cyberattack — Equinor: no vector/actor, no constituency nexus
- borderline-drop: Wellington IT credit-union platform — Wellington IT credit-union platform: out-of-nexus, single relay source
- borderline-drop: TfL Oyster photocard site — TfL Oyster photocard site: out-of-nexus UK consumer accounts, single source
- borderline-drop: Municipality of Neuried — Neuried municipality IT offline: no vector, no actor, below incident floor
- borderline-drop: TeamCity CVE-2026-132231 to -132234 — four CVSS 9.9 rows that need a low-privilege account, no exploitation (S1 drop list)
- borderline-drop: Apache Roller CVE-2026-129448, PostgreSQL 14 to 18 minor releases, Apache Shiro and APISIX rows, SmarterMail CVE-2026-126969, Zyxel DX3301, Circutor PowerStudio, ASUS Control Center Express, DrayTek Vigor2960 and other EUVD 9.0+ rows — no exploitation and no stated constituency footprint (S1 drop list)
- borderline-drop: Bitdefender EggStreme, Dream Mustang Panda ASEAN lures, ThreatFabric Bazuka, Natto ZRON report, SpecterOps Black October — out-of-nexus, paywalled or vendor commentary (S3 drop list)

Coverage gaps: lab52 (every transport fails, newest post 2026-10-05); belden-psirt (listing 403, advisory PDFs read); my.f5.com K-articles (single-page application, read through the CNA record and nginx.org); baselland.ch (403 on every transport, read through the Polizeiticker relay); airlock.com advisory page (disclosure policy only); consilium.europa.eu (403); cnil-fr (503 maintenance page); safeonweb-be (5xx outage ended); apa-ots, cyberattaque-org (retirement or horizon limits); dell.com, support.hpe.com, advisories.ncsc.nl advisory stubs (read through CSAF and per-year URLs).
