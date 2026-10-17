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
updated_at: "2026-09-27T04:35:00Z"
event_date: 2026-06-10
run_id: 2026-06-11-7edf1d8a
priority: critical
immediate_action:
  title: "Patch Oracle PeopleSoft PSEMHUB now and normalize WAF path-matching; a WAF rule alone no longer stops this"
  action: >
    UNC6240 (ShinyHunters) is again mass-exploiting CVE-2026-35273 against organisations that patched
    their WAF but not PeopleSoft itself, using a URL-encoded path (`/%50SEMHUB/`) that many WAFs match
    before decoding. Apply Oracle's Security Alert or disable/remove PSEMHUB; where a WAF is the only
    control, reconfigure it to block on the normalized path, not the literal string, and search
    WebLogic access logs for `/PSEMHUB/` and any encoded or mixed-case variant (Mandiant/GTIG,
    2026-09-25).
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
  - healthcare
  - technology
entities:
  - "actor:shinyhunters"
  - "campaign:shinyhunters-peoplesoft-2026"
techniques: [T1190, T1078.001, T1021.004, T1213, T1567, T1505.003, T1572, T1219, T1027.002, T1553.002]
affected_products: ["Oracle PeopleSoft PeopleTools"]
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
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/"
    publisher: "Mandiant GTIG"
    date: "2026-09-25"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
    publisher: BleepingComputer
    date: "2026-09-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Mandiant and Google Threat Intelligence Group (GTIG) have identified an active compromise and extortion campaign attributed to UNC6240 (ShinyHunters) targeting Oracle PeopleSoft application infrastructure. The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273, a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component."
    publisher: Google/Mandiant GTIG
  - quote: "Google's Mandiant attributes it to the group it tracks as UNC6240, and dates the activity between May 27 and June 9. Oracle did not publish its advisory until June 10, so the bug was a zero-day the entire time."
    publisher: The Hacker News
  - quote: "The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273, a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component"
    publisher: "Mandiant GTIG"
  - quote: CVE-2026-35273 is a critical remote code execution vulnerability (CVSS 9.8) in Oracle PeopleTools versions 8.61 and 8.62 that exploits a server-side request forgery flaw in the Environment Management component
    publisher: Rapid7
  - quote: "This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure."
    publisher: "Mandiant GTIG"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/"
  - quote: "Across compromised instances, a quarter of the threat actor's commands executed as `root` or `NT Authority\\SYSTEM`, granting full control of the operating system."
    publisher: "Mandiant GTIG"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/"
  - quote: "Google says the new wave of attacks has deployed web shells on dozens of systems worldwide within higher education, technology, IT services, healthcare, agriculture, transportation, and government organizations."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "**Patch every Oracle PeopleSoft instance to a supported PeopleTools release or disable/remove PSEMHUB now (CVE-2026-35273); a WAF rule alone no longer stops this.** UNC6240 (ShinyHunters) bypasses literal-string `/PSEMHUB/` WAF blocks with the URL-encoded `/%50SEMHUB/` path, so a perimeter block that has not been reconfigured to match on the normalized path is not a control. Treat any instance that was internet-reachable and unpatched at any point since 27 May 2026 as compromised until proven clean, and rotate every credential reachable from the PeopleSoft tier."
  - "**Hunt for the post-exploitation toolkit on any PeopleSoft host.** Search WebLogic access logs for `/PSEMHUB/` and its encoded/mixed-case variants; scan `PSEMHUB.war`/`PORTAL.war` for unexpected `.jsp`/`.jspx`/`.exe` files (including `Ple64.exe`); check for MeshAgent/MeshCentral agents and SSH credential-spraying against hosts in `/etc/hosts`; and review for ransom-note markers in PeopleSoft directories."
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
  - at: "2026-09-27T04:35:00Z"
    run_id: 2026-09-27T0404Z-intel
    type: update
    summary: >
      UNC6240 (ShinyHunters) has resumed mass exploitation of CVE-2026-35273 using a URL-encoded
      WAF-bypass path and a new backdoor, SIDEEYE, and has expanded targeting to include government
      organisations explicitly (Mandiant/GTIG, 2026-09-25). The ATT&CK technique mapping for the
      whole campaign, from initial access through this wave's tooling, is now complete.
    fields: [immediate_action, sectors, techniques, affected_products, classification, actions, sources, evidence, body]
migrated_from: briefs/2026-06-11.md
---

ShinyHunters confirmed to BleepingComputer on 10 June 2026 that it had compromised Oracle PeopleSoft servers across approximately 300 instances at more than 100 organisations, with a heavy concentration in higher education ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). The University of Nottingham confirmed the same day that student and alumni data had been accessed in a security incident affecting its student-record system, opened a dedicated support line, and notified Action Fraud and the ICO ([University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). TechCrunch independently corroborated the scale of the campaign and the education-sector skew ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)).

**Access and exploitation.** ShinyHunters describes initial access as a "gadget chain" combining legacy PeopleSoft vulnerabilities with claimed zero-days; the actor stresses that exploitation is configuration-dependent and not universal across all internet-reachable instances. Oracle has not published a CVE for the specific flaws in this campaign and did not respond to press inquiries, so the precise initial-access vector remains attacker-asserted rather than vendor-confirmed — treat the "zero-day" framing with appropriate caution. The relevant entry surface is the externally reachable PeopleSoft web and application tier (PIA, Integration Broker, and REST/SAML/OAuth endpoints), mapped to `T1190` Exploit Public-Facing Application.

**Post-access lateral movement.** The better-evidenced — and more directly defender-actionable — phase is what follows initial access. The actor's tooling attempts SSH connections against common PeopleSoft/Oracle operating-system service accounts (`psoft`, `oracle`, `linuxadm`) using password and key-based fallback, then runs a shell script that performs bulk data retrieval and drops ransom notes into PeopleSoft web/application server directories ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). This maps to `T1078.001` Valid Accounts: Default Accounts, `T1021.004` Remote Services: SSH, and `T1213` Data from Information Repositories, culminating in `T1567` Exfiltration Over Web Service. Exfiltrated data categories stated by the actor include student and applicant records, financial-aid data, immigration status, health records, and contact details — the full sensitive payload of a campus-management deployment.

**Detection and hunting concepts (no IOCs).** Watch for SSH authentication attempts to PeopleSoft hosts using the `psoft`/`oracle`/`linuxadm` account names from external or unexpected source ranges; correlate against successful logons followed by interactive shell activity. On the application tier, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations. Treat the appearance of unexpected ransom-note text files in web/app server document roots as a high-confidence lateral-movement indicator and review `authorized_keys` and `/etc/hosts` for unauthorised additions.

**Hardening / mitigation.** Rename or disable the default `psoft`/`oracle`/`linuxadm` OS service accounts and enforce SSH key-only authentication; restrict PeopleSoft administrative interfaces to jump-host access and remove direct internet exposure of the management tier; enable PeopleTools security-audit logging if not already on; and apply any outstanding Oracle Critical Patch Update advisories for PeopleSoft, recognising that the campaign's specific CVEs are undisclosed so defence-in-depth around authentication and exposure is the dependable control. Public-sector and university SOCs running PeopleSoft Campus Solutions or HCM should audit external reachability of the web/app tier as the first action.

## Update — 2026-06-12T05:00:10Z

The initial-access vector that was attacker-asserted yesterday is now vendor-confirmed: Oracle assigned **CVE-2026-35273** (CVSS 9.8), an unauthenticated RCE in the PeopleTools Environment Management Hub (PSEMHUB, versions 8.61/8.62), and published an out-of-band Security Alert with fixes ([Oracle, 2026-06-10](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html); [SecurityWeek, 2026-06-11](https://www.securityweek.com/oracle-addresses-peoplesoft-vulnerability-amid-reports-of-zero-day-attacks/)).

Mandiant GTIG formally attributes the campaign to UNC6240 (ShinyHunters), dating exploitation 27 May – 9 June — a zero-day for the full window — and details the post-exploitation chain: customised MeshCentral remote-management agents masquerading as Microsoft Azure components for persistence and C2, and a per-victim `_fanout.sh` lateral-movement script spraying SSH credentials against internal hosts harvested from `/etc/hosts` (`T1190`, `T1021.004`). Mandiant notified more than 100 organisations with exposed PSEMHUB endpoints; 68 % are higher-education institutions ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)).

The University of Nottingham — confirmed as a victim yesterday — now quantifies the damage: roughly 40 GB exfiltrated covering ~455,000 individuals across its UK, Malaysia and China campuses, including names, contact details, ethnicity, disability, passport and tuition-payment data; the ICO says it is assessing the report ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/); [The Record, 2026-06-11](https://therecord.media/university-of-nottingham-cyber-incident-shiny-hunters); [University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). Action: see the § 0 callout — patch out-of-band **and** compromise-assess; yesterday's hardening guidance (default SSH service accounts, PSEMHUB exposure) stands.

## Update — 2026-06-13T05:00:07Z

Mandiant and Google GTIG formally attribute the PeopleSoft Environment Management Hub exploitation campaign to UNC6240 (ShinyHunters) and confirm the activity ran from 27 May to 9 June 2026 — predating Oracle's 10 June out-of-band advisory, establishing CVE-2026-35273 (CVSS 9.8) as a zero-day at time of exploitation ([Mandiant/GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). The unauthenticated SSRF→RCE is reached via the `/PSEMHUB/hub` and `/PSIGW/HttpListeningConnector` endpoints in PeopleTools 8.61/8.62.

GTIG notified over 100 organisations whose endpoints correlated with exploitation; 68% are higher-education institutions. Post-exploitation, the actor deployed MeshCentral remote-management agents disguised as Azure binaries, used SSH fan-out scripts with PeopleSoft admin credentials for lateral movement, and exfiltrated to the ShinyHunters leak site ([Rapid7, 2026-06-12](https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/)). The University of Nottingham confirmed 454,600 student and alumni records were taken, including passport numbers ([University of Nottingham](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident); [BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/)). CISA added the CVE to KEV on 12 June. Swiss/EU universities running Campus Solutions should treat this as P1 (.

## Update — 2026-06-16T05:09:02Z

ShinyHunters listed the **Council of Europe** — the 46-member Strasbourg human-rights body, of which Switzerland is a member — claiming **297 GB across ~429,000 files** taken via the Oracle PeopleSoft Environment Management Hub zero-day **CVE-2026-35273**, and set a **16 June leak deadline** ([SecurityWeek, 2026-06-15](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)). This is the first European intergovernmental institution named in the 100+-organisation PeopleSoft campaign previously covered as an education-sector wave.

The claimed dataset spans payroll for 10,000+ current and former staff (2011–2026), 14,000+ CVs, and HR records with names, dates of birth, addresses, bank-account, tax/social-security and medical data. The Council of Europe confirmed it "is currently investigating the matter and assessing the situation" and has not confirmed exfiltration ([The Register, 2026-06-15](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757); [BleepingComputer, 2026-06-15](https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/)). The vector — unauthenticated HTTP to the `/PSEMHUB/hub` servlet (`T1190`) — is unchanged; treat any externally-reachable PeopleSoft Environment Management Hub as compromised pending forensic review and block perimeter access to `/PSEMHUB/*`. Confidence on the victim claim is MEDIUM pending Council of Europe confirmation (extortion-site claim).

## Update — 2026-09-27T04:35:00Z

Mandiant and GTIG report that UNC6240 (ShinyHunters) has resumed mass exploitation of CVE-2026-35273, adapting to the defensive guidance this campaign's own earlier coverage carried. The actor now bypasses WAF rules that block the literal `/PSEMHUB/` path by requesting the URL-encoded `/%50SEMHUB/` instead: many WAFs and reverse proxies match the request path before decoding it, while the PeopleSoft application server decodes and routes the request normally. "This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure" ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)). Mandiant warns the actor may rotate to other percent-encoded, mixed-case or otherwise non-normalized path variants, so defenders should block on the normalized path rather than the literal string.

Before exploiting a target, the actor sends five to fifteen POST requests carrying a serialized Java object to quietly confirm exploitability without writing files or disrupting the service. Two complementary single-line JSP web shells are then dropped into the `PSEMHUB.war` directory: `x.jsp` executes hex-encoded commands cross-platform, and `u.jsp`/`u2.jsp` upload larger files in 150 KB Base64-encoded chunks, bypassing PeopleSoft's own file-size limits; a fileless variant returns command output directly in the HTTP response with nothing written to disk, defeating file-creation-based detection. On compromised Windows hosts, the actor uploads a trojanized installer, `Ple64.exe`, masquerading as a signed Light Alloy media-player installer and signed with a valid Extended Validation certificate Mandiant has asked the issuing certificate authority to revoke; it loads a VMProtect-3-packed multi-stage chain culminating in the SIDEEYE C++ backdoor, which steals browser and desktop credentials, manages processes and files, and provides an interactive reverse shell and reverse proxy over raw TCP. The actor also deploys the open-source Neo-reGeorg tunneling toolkit to route SOCKS5 proxy traffic over ordinary HTTP/S for internal lateral movement, and uses the legitimate MeshAgent/MeshCentral remote-management platform to maintain access on Linux hosts. "Across compromised instances, a quarter of the threat actor's commands executed as `root` or `NT Authority\SYSTEM`, granting full control of the operating system" ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)).

Targeting has expanded well beyond the original higher-education skew: "Google says the new wave of attacks has deployed web shells on dozens of systems worldwide within higher education, technology, IT services, healthcare, agriculture, transportation, and government organizations" ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)), and Mandiant's report names government among the sectors this wave has hit alongside the Council of Europe's earlier confirmed intergovernmental role. Mandiant's remediation guidance is unchanged in substance but sharper: apply the Oracle Security Alert and stay on a supported PeopleTools release rather than relying on a WAF at all; disable EMHub or remove PSEMHUB if not needed, since neither is required for standard PeopleSoft Internet Architecture user sessions; search WebLogic access logs for requests to `/PSEMHUB/` and its encoded variants and for POST requests to `/hub` with external-source bodies; and, on any host where a web shell is found, treat it as compromised, preserve evidence, and rotate every credential reachable from the PeopleSoft tier, prioritising hosts where WebLogic runs as `root` or `SYSTEM`.

This wave also clarifies part of a separately-tracked claim: ShinyHunters told BleepingComputer it used this same WAF-bypass technique against the FBI's own recruitment site, alongside a further, still-unconfirmed vulnerability it says it also exploited there; see the FBI PeopleSoft entry for that update.

**Defender takeaway:** a WAF rule that blocked the literal `/PSEMHUB/` path is no longer sufficient on its own; only patching, removing PSEMHUB, or a WAF reconfigured to match on the normalized path closes this exposure, and every organisation that relied on the June guidance's perimeter-blocking workaround should re-verify its control actually normalizes the path before matching.
