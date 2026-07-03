---
schema: 1
kind: threat
horizon: operational
title: "ShinyHunters Oracle PeopleSoft campaign: gadget-chain access, SSH default-credential lateral movement, mass exfiltration"
headline: "ShinyHunters Oracle PeopleSoft campaign: gadget-chain access, SSH default-credential lateral movement, mass exfiltration"
summary: "ShinyHunters claims Oracle PeopleSoft data theft at 100+ organisations across ~300 instances, mostly in higher education; the University of Nottingham confirmed student and alumni data was accessed (BleepingComputer, 2026-06-10). Post-access lateral movement abuses default PeopleSoft/Oracle SSH service accounts — see the deep dive."
discovered_at: "2026-06-11T05:00:07Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - supply-chain
regions:
  - uk
  - europe
  - global
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident"
    publisher: University of Nottingham
    role: corroborating
  - url: "https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/"
    publisher: TechCrunch
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-11.md
---

ShinyHunters confirmed to BleepingComputer on 10 June 2026 that it had compromised Oracle PeopleSoft servers across approximately 300 instances at more than 100 organisations, with a heavy concentration in higher education ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). The University of Nottingham confirmed the same day that student and alumni data had been accessed in a security incident affecting its student-record system, opened a dedicated support line, and notified Action Fraud and the ICO ([University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). TechCrunch independently corroborated the scale of the campaign and the education-sector skew ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)).

**Access and exploitation.** ShinyHunters describes initial access as a "gadget chain" combining legacy PeopleSoft vulnerabilities with claimed zero-days; the actor stresses that exploitation is configuration-dependent and not universal across all internet-reachable instances. Oracle has not published a CVE for the specific flaws in this campaign and did not respond to press inquiries, so the precise initial-access vector remains attacker-asserted rather than vendor-confirmed — treat the "zero-day" framing with appropriate caution. The relevant entry surface is the externally reachable PeopleSoft web and application tier (PIA, Integration Broker, and REST/SAML/OAuth endpoints), mapped to `T1190` Exploit Public-Facing Application.

**Post-access lateral movement.** The better-evidenced — and more directly defender-actionable — phase is what follows initial access. The actor's tooling attempts SSH connections against common PeopleSoft/Oracle operating-system service accounts (`psoft`, `oracle`, `linuxadm`) using password and key-based fallback, then runs a shell script that performs bulk data retrieval and drops ransom notes into PeopleSoft web/application server directories ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). This maps to `T1078.004` Valid Accounts: Cloud/default service accounts, `T1021.004` Remote Services: SSH, and `T1213` Data from Information Repositories, culminating in `T1567` Exfiltration Over Web Service. Exfiltrated data categories stated by the actor include student and applicant records, financial-aid data, immigration status, health records, and contact details — the full sensitive payload of a campus-management deployment.

**Detection and hunting concepts (no IOCs).** Watch for SSH authentication attempts to PeopleSoft hosts using the `psoft`/`oracle`/`linuxadm` account names from external or unexpected source ranges; correlate against successful logons followed by interactive shell activity. On the application tier, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations (`T1071`). Treat the appearance of unexpected ransom-note text files in web/app server document roots as a high-confidence lateral-movement indicator and review `authorized_keys` and `/etc/hosts` for unauthorised additions.

**Hardening / mitigation.** Rename or disable the default `psoft`/`oracle`/`linuxadm` OS service accounts and enforce SSH key-only authentication; restrict PeopleSoft administrative interfaces to jump-host access and remove direct internet exposure of the management tier; enable PeopleTools security-audit logging if not already on; and apply any outstanding Oracle Critical Patch Update advisories for PeopleSoft, recognising that the campaign's specific CVEs are undisclosed so defence-in-depth around authentication and exposure is the dependable control. Public-sector and university SOCs running PeopleSoft Campus Solutions or HCM should audit external reachability of the web/app tier as the first action.
