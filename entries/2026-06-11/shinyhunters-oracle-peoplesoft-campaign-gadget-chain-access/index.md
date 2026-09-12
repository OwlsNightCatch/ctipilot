---
schema: 1
kind: threat
title: >
  ShinyHunters Oracle PeopleSoft campaign: gadget-chain access, SSH default-credential lateral
  movement, mass exfiltration
headline: >
  ShinyHunters Oracle PeopleSoft campaign: gadget-chain access, SSH default-credential lateral
  movement, mass exfiltration
summary: >
  ShinyHunters claims Oracle PeopleSoft data theft at 100+ organisations across ~300 instances,
  mostly in higher education; the University of Nottingham confirmed student and alumni data was
  accessed (BleepingComputer, 2026-06-10). Post-access lateral movement abuses default
  PeopleSoft/Oracle SSH service accounts — see the deep dive.
discovered_at: "2026-06-11T05:00:07Z"
updated_at: "2026-06-16T05:09:02Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: critical
immediate_action:
  title: patch Oracle PeopleSoft out-of-band and run a compromise assessment
  action: >
    Oracle has published an out-of-band Security Alert for CVE-2026-35273, an unauthenticated remote
    code execution flaw (CVSS 9.8) in the PeopleTools Environment Management Hub (PSEMHUB) exploited
    as a zero-day by UNC6240 (ShinyHunters) from 27 May to 9 June against 100+ organisations, 68 %
    of them in higher education (Oracle, 2026-06-10; Mandiant GTIG, 2026-06-11).
tags:
  - data-breach
  - organized-crime
  - supply-chain
  - vulnerabilities
  - actively-exploited
  - pre-auth
  - rce
  - zero-day
  - patch-available
  - cisa-kev
  - identity
regions:
  - uk
  - europe
  - global
  - switzerland
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
  - "campaign:shinyhunters-peoplesoft-2026"
techniques: []
affected_products: []
cves:
  - id: CVE-2026-35273
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
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
  - url: "https://www.oracle.com/security-alerts/alert-cve-2026-35273.html"
    publisher: Oracle Security Alert CVE-2026-35273
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/"
    publisher: Mandiant GTIG
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://therecord.media/university-of-nottingham-cyber-incident-shiny-hunters"
    publisher: The Record
    role: corroborating
  - url: "https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/"
    publisher: Rapid7
    role: corroborating
  - url: "https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757"
    publisher: The Register
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "Mandiant and Google Threat Intelligence Group (GTIG) have identified an active compromise and extortion campaign attributed to UNC6240 (ShinyHunters) targeting Oracle PeopleSoft application infrastructure. The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273, a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component."
    publisher: Google/Mandiant GTIG
  - quote: "Google's Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a zero-day the entire time."
    publisher: The Hacker News
  - quote: "The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273, a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component"
    publisher: Mandiant/GTIG
  - quote: CVE-2026-35273 is a critical remote code execution vulnerability (CVSS 9.8) in Oracle PeopleTools versions 8.61 and 8.62 that exploits a server-side request forgery flaw in the Environment Management component
    publisher: Rapid7
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "**Patch Oracle PeopleSoft out-of-band and treat every 8.61/8.62 instance as compromised until proven clean (CVE-2026-35273).** Apply Oracle's alert, restrict PSEMHUB to management networks, and hunt the post-exploitation chain: SSH credential spraying from the application server against hosts in `/etc/hosts`, remote-management agents masquerading as Azure components, and ransom-note markers in PeopleSoft directories. Exploitation ran 27 May – 9 June, before the patch existed."
  - "**Patch internet-exposed Oracle PeopleSoft (PeopleTools 8.61/8.62) now** — CVE-2026-35273 is under active zero-day exploitation by ShinyHunters with ongoing victim acquisition in education. Apply Oracle's out-of-band fix, restrict `/PSEMHUB/hub` and `/PSIGW/HttpListeningConnector` to trusted admin subnets, rotate PeopleSoft admin credentials, and hunt for MeshCentral agents spawned by the app-server process and unexpected outbound SMB (."
  - "**Block perimeter access to `/PSEMHUB/*` on Oracle PeopleSoft** and treat any externally-reachable Environment Management Hub as compromised pending forensic review (CVE-2026-35273)."
updates:
  - at: "2026-06-12T05:00:10Z"
    run_id: 2026-06-12-5ab9a319
    type: update
    summary: >
      Oracle confirms the PeopleSoft zero-day: CVE-2026-35273, pre-auth RCE (CVSS 9.8) in the
      Environment Management Hub, out-of-band patch released. Mandiant attributes the
      100+-organisation data-theft campaign to UNC6240 (ShinyHunters) with an exploitation window of
      27 May – 9 June (Mandiant GTIG, 2026-06-11). Patch and compromise-assess — exploitation predates
      the fix.
    fields:
      - actions
      - cves
      - entities
      - evidence
      - immediate_action
      - priority
      - sources
      - tags
      - body
    merged_from: 2026-06-12/shinyhunters-peoplesoft-campaign-oracle-confirms-cve-2026-35
  - at: "2026-06-13T05:00:07Z"
    run_id: 2026-06-13-40b26572
    type: update
    summary: >
      Oracle PeopleSoft CVE-2026-35273 confirmed exploited as a zero-day since 27 May; 100+ orgs hit,
      68% higher education. Mandiant/GTIG attributes the unauthenticated SSRF→RCE campaign against the
      PeopleSoft Environment Management Hub to UNC6240 (ShinyHunters); the University of Nottingham
      confirmed 454,600 student records stolen. CISA added it to KEV on 12 June. Swiss/EU universities
      running PeopleTools 8.61/8.62 (Campus Solutions) are squarely in scope (Mandiant/GTIG,
      2026-06-11).
    fields:
      - actions
      - cves
      - evidence
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-13/oracle-peoplesoft-cve-2026-35273-attributed-to-shinyhunters
  - at: "2026-06-16T05:09:02Z"
    run_id: 2026-06-16-38d638e1
    type: update
    summary: >
      Council of Europe breached via the Oracle PeopleSoft zero-day (CVE-2026-35273) — ShinyHunters
      claims 297 GB / ~429,000 files and set a 16 June leak deadline; the first European
      intergovernmental victim named in the 100+-organisation PeopleSoft campaign (§ 4 update).
      (SecurityWeek, 2026-06-15)
    fields:
      - actions
      - sources
      - tags
      - body
    merged_from: 2026-06-16/council-of-europe-named-as-a-victim-of-the-oracle-peoplesoft
migrated_from: briefs/2026-06-11.md
---

ShinyHunters confirmed to BleepingComputer on 10 June 2026 that it had compromised Oracle PeopleSoft servers across approximately 300 instances at more than 100 organisations, with a heavy concentration in higher education ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). The University of Nottingham confirmed the same day that student and alumni data had been accessed in a security incident affecting its student-record system, opened a dedicated support line, and notified Action Fraud and the ICO ([University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). TechCrunch independently corroborated the scale of the campaign and the education-sector skew ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)).

**Access and exploitation.** ShinyHunters describes initial access as a "gadget chain" combining legacy PeopleSoft vulnerabilities with claimed zero-days; the actor stresses that exploitation is configuration-dependent and not universal across all internet-reachable instances. Oracle has not published a CVE for the specific flaws in this campaign and did not respond to press inquiries, so the precise initial-access vector remains attacker-asserted rather than vendor-confirmed — treat the "zero-day" framing with appropriate caution. The relevant entry surface is the externally reachable PeopleSoft web and application tier (PIA, Integration Broker, and REST/SAML/OAuth endpoints), mapped to `T1190` Exploit Public-Facing Application.

**Post-access lateral movement.** The better-evidenced — and more directly defender-actionable — phase is what follows initial access. The actor's tooling attempts SSH connections against common PeopleSoft/Oracle operating-system service accounts (`psoft`, `oracle`, `linuxadm`) using password and key-based fallback, then runs a shell script that performs bulk data retrieval and drops ransom notes into PeopleSoft web/application server directories ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). This maps to `T1078.004` Valid Accounts: Cloud/default service accounts, `T1021.004` Remote Services: SSH, and `T1213` Data from Information Repositories, culminating in `T1567` Exfiltration Over Web Service. Exfiltrated data categories stated by the actor include student and applicant records, financial-aid data, immigration status, health records, and contact details — the full sensitive payload of a campus-management deployment.

**Detection and hunting concepts (no IOCs).** Watch for SSH authentication attempts to PeopleSoft hosts using the `psoft`/`oracle`/`linuxadm` account names from external or unexpected source ranges; correlate against successful logons followed by interactive shell activity. On the application tier, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations (`T1071`). Treat the appearance of unexpected ransom-note text files in web/app server document roots as a high-confidence lateral-movement indicator and review `authorized_keys` and `/etc/hosts` for unauthorised additions.

**Hardening / mitigation.** Rename or disable the default `psoft`/`oracle`/`linuxadm` OS service accounts and enforce SSH key-only authentication; restrict PeopleSoft administrative interfaces to jump-host access and remove direct internet exposure of the management tier; enable PeopleTools security-audit logging if not already on; and apply any outstanding Oracle Critical Patch Update advisories for PeopleSoft, recognising that the campaign's specific CVEs are undisclosed so defence-in-depth around authentication and exposure is the dependable control. Public-sector and university SOCs running PeopleSoft Campus Solutions or HCM should audit external reachability of the web/app tier as the first action.

## Update — 2026-06-12T05:00:10Z

The initial-access vector that was attacker-asserted yesterday is now vendor-confirmed: Oracle assigned **CVE-2026-35273** (CVSS 9.8), an unauthenticated RCE in the PeopleTools Environment Management Hub (PSEMHUB, versions 8.61/8.62), and published an out-of-band Security Alert with fixes ([Oracle, 2026-06-10](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html); [SecurityWeek, 2026-06-11](https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/)).

Mandiant GTIG formally attributes the campaign to UNC6240 (ShinyHunters), dating exploitation 27 May – 9 June — a zero-day for the full window — and details the post-exploitation chain: customised MeshCentral remote-management agents masquerading as Microsoft Azure components for persistence and C2, and a per-victim `_fanout.sh` lateral-movement script spraying SSH credentials against internal hosts harvested from `/etc/hosts` ([T1190](https://attack.mitre.org/techniques/T1190/), [T1021.004](https://attack.mitre.org/techniques/T1021/004/)). Mandiant notified more than 100 organisations with exposed PSEMHUB endpoints; 68 % are higher-education institutions ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)).

The University of Nottingham — confirmed as a victim yesterday — now quantifies the damage: roughly 40 GB exfiltrated covering ~455,000 individuals across its UK, Malaysia and China campuses, including names, contact details, ethnicity, disability, passport and tuition-payment data; the ICO says it is assessing the report ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/); [The Record, 2026-06-11](https://therecord.media/university-of-nottingham-cyber-incident-shiny-hunters); [University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). Action: see the § 0 callout — patch out-of-band **and** compromise-assess; yesterday's hardening guidance (default SSH service accounts, PSEMHUB exposure) stands.

## Update — 2026-06-13T05:00:07Z

Mandiant and Google GTIG formally attribute the PeopleSoft Environment Management Hub exploitation campaign to UNC6240 (ShinyHunters) and confirm the activity ran from 27 May to 9 June 2026 — predating Oracle's 10 June out-of-band advisory, establishing CVE-2026-35273 (CVSS 9.8) as a zero-day at time of exploitation ([Mandiant/GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). The unauthenticated SSRF→RCE is reached via the `/PSEMHUB/hub` and `/PSIGW/HttpListeningConnector` endpoints in PeopleTools 8.61/8.62.

GTIG notified over 100 organisations whose endpoints correlated with exploitation; 68% are higher-education institutions. Post-exploitation, the actor deployed MeshCentral remote-management agents disguised as Azure binaries, used SSH fan-out scripts with PeopleSoft admin credentials for lateral movement, and exfiltrated to the ShinyHunters leak site ([Rapid7, 2026-06-12](https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/)). The University of Nottingham confirmed 454,600 student and alumni records were taken, including passport numbers ([University of Nottingham](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident); [BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/)). CISA added the CVE to KEV on 12 June. Swiss/EU universities running Campus Solutions should treat this as P1 (.

## Update — 2026-06-16T05:09:02Z

ShinyHunters listed the **Council of Europe** — the 46-member Strasbourg human-rights body, of which Switzerland is a member — claiming **297 GB across ~429,000 files** taken via the Oracle PeopleSoft Environment Management Hub zero-day **CVE-2026-35273**, and set a **16 June leak deadline** ([SecurityWeek, 2026-06-15](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)). This is the first European intergovernmental institution named in the 100+-organisation PeopleSoft campaign previously covered as an education-sector wave.

The claimed dataset spans payroll for 10,000+ current and former staff (2011–2026), 14,000+ CVs, and HR records with names, dates of birth, addresses, bank-account, tax/social-security and medical data. The Council of Europe confirmed it "is currently investigating the matter and assessing the situation" and has not confirmed exfiltration ([The Register, 2026-06-15](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757); [BleepingComputer, 2026-06-15](https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/)). The vector — unauthenticated HTTP to the `/PSEMHUB/hub` servlet (`T1190`) — is unchanged; treat any externally-reachable PeopleSoft Environment Management Hub as compromised pending forensic review and block perimeter access to `/PSEMHUB/*`. Confidence on the victim claim is MEDIUM pending Council of Europe confirmation (extortion-site claim).
