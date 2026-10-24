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
  ShinyHunters (UNC6240) exploited CVE-2026-35273, an unauthenticated flaw in Oracle PeopleSoft's
  Environment Management Hub, as a zero-day from 27 May 2026, and Mandiant notified more than 100
  organisations, mostly in higher education; Oracle fixed it out of band on 2026-06-10 and CISA listed
  it in KEV on 12 June. Have I Been Pwned's analysis of the leaked data counts about 455,000 University of
  Nottingham students and alumni. A second wave from September reaches the hub past WAF path rules with a URL-encoded path.
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
techniques: [T1190, T1078.001, T1021.004, T1213, T1505.003, T1572, T1219, T1027.002, T1553.002, T1048]
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
  - quote: "The activity was observed between May 27, 2026, and June 9, 2026 and is consistent with the exploitation of CVE-2026-35273, a critical remote code execution vulnerability (CVSS 9.8) in the Environment Management component"
    publisher: "Mandiant GTIG"
  - quote: "Organizations running PeopleTools versions 8.61 or 8.62 should apply the vendor-supplied patch on an emergency basis, without waiting for a regular patch cycle to occur."
    publisher: Rapid7
    source_url: "https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/"
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
references:
  - 2026-06-28/naic-breached-via-oracle-peoplesoft-zero-day-shinyhunters-pu
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "**Patch every Oracle PeopleSoft instance to a supported PeopleTools release or disable/remove PSEMHUB now (CVE-2026-35273); a WAF rule alone no longer stops this.** UNC6240 (ShinyHunters) bypasses literal-string `/PSEMHUB/` WAF blocks with the URL-encoded `/%50SEMHUB/` path, so a perimeter block that has not been reconfigured to match on the normalized path is not a control. Investigate any instance that was internet-reachable and unpatched at any point since 27 May 2026 for compromise; on any host where a web shell is found, treat the host as compromised and rotate all credentials accessible from the PeopleSoft tier (its service accounts reach PeopleSoft configuration files and database connection strings), starting with hosts where WebLogic runs as `root` or `SYSTEM`."
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
  - at: "2026-10-11T14:56:35Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The summary and the main analysis still called the initial-access vector attacker-asserted and the campaign's CVEs undisclosed, although the entry's own updates record Oracle's confirmation of CVE-2026-35273, its zero-day exploitation from 27 May, the KEV listing and the September wave; both now say so, and the hardening line names the Security Alert and Mandiant's advice to remove the hub where unused. A truncated sentence in the 2026-06-13 section is repaired. A reference to the NAIC breach entry, a victim of this campaign that shares CVE-2026-35273, is added, and an evidence record attributed to a publisher missing from the sources is removed. The Nottingham count is attributed to Have I Been Pwned's analysis of the leaked data, Oracle is described as publishing the alert and Mandiant as tying the campaign to it, the entry surface and the recovered script follow Mandiant and BleepingComputer, the Council of Europe is no longer called a confirmed victim or the first of its kind, uncited sentences gain their citations, and the hunting action that restated the body is dropped. The exfiltration step is mapped to the outbound SSH channel Mandiant records rather than a web service, TechCrunch is described as relaying the actor's account, the Oracle patch is cited to Rapid7 rather than SecurityWeek, which reports mitigations, the Council of Europe's link to the campaign is cited to The Register, and the Rapid7 evidence quote is replaced with a sentence the page carries.
    fields: [references, evidence, summary, body, actions, techniques]
  - at: "2026-10-21T08:13:55Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      The SSH hunt now looks for spraying from a compromised PeopleSoft server toward the internal hosts
      in its /etc/hosts, as Mandiant's recovered script does, rather than from external ranges. The
      credential-rotation action now names what the PeopleSoft tier exposes (configuration files and
      database connection strings) and Mandiant's priority on hosts where WebLogic runs as root or SYSTEM.
    fields: [actions, body]
migrated_from: briefs/2026-06-11.md
---

ShinyHunters confirmed to BleepingComputer on 10 June 2026 that it had compromised Oracle PeopleSoft servers across approximately 300 instances at more than 100 organisations, with a heavy concentration in higher education ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). The University of Nottingham confirmed the same day that student and alumni data had been accessed in a security incident affecting its student-record system, opened a dedicated support line, and is working with Action Fraud and the Information Commissioner's Office ([University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). A ShinyHunters member gave TechCrunch the same account of the campaign's scale and its concentration on universities ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)).

**Access and exploitation.** ShinyHunters describes initial access as a "gadget chain" of old and zero-day vulnerabilities and says exploitation does not work on every system and may depend on how an instance is configured ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). Oracle published an out-of-band Security Alert on 2026-06-10 for CVE-2026-35273 (CVSS 9.8), a flaw in the PeopleTools Environment Management component that is remotely exploitable without authentication ([Oracle, 2026-06-10](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html)), and Mandiant assesses the campaign as consistent with exploitation of that CVE, dating the activity from 27 May, a zero-day for the whole window ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). The exposed surface Mandiant names is the Environment Management Hub (`/PSEMHUB/hub`) and the Integration Broker listening connector (`/PSIGW/HttpListeningConnector`), administrative and system-to-system components that ordinary PeopleSoft Internet Architecture user sessions do not need ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)); this is the `T1190` Exploit Public-Facing Application step.

**Post-access lateral movement.** The most directly defender-actionable phase is what follows initial access. A shell script recovered from exposed servers parses `/etc/hosts` for PeopleSoft-related systems, tries SSH with common PeopleSoft and Oracle administrative accounts (`psoft`, `oracle`, `linuxadm`), falling back to key-based authentication when passwords fail, and drops a ransom note into PeopleSoft web and application server directories ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)). Mandiant documents the exfiltration step separately ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). This maps to `T1078.001` Valid Accounts: Default Accounts, `T1021.004` Remote Services: SSH, and `T1213` Data from Information Repositories, culminating in exfiltration: Mandiant records the stolen directories compressed with `zstd` and an outbound SSH connection from the staging host to the server hosting the public mirror of the ShinyHunters leak site, `T1048` Exfiltration Over Alternative Protocol ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). Exfiltrated data categories stated by the actor include student, applicant, financial-aid, immigration, health and administrative data, with home addresses, phone numbers, emails and dates of birth ([TechCrunch, 2026-06-10](https://techcrunch.com/2026/06/10/cybercriminals-claim-breach-of-oracle-peoplesoft-servers-at-100-plus-organizations/)).

**Detection and hunting concepts (no IOCs).** Watch for SSH authentication attempts with the `psoft`/`oracle`/`linuxadm` account names or other administrative accounts ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)) that originate from a PeopleSoft server toward other internal PeopleSoft hosts: the recovered script sprays SSH credentials at the internal hosts named in the compromised server's `/etc/hosts` and, on each successful session, copies a marker file into the WebLogic and Process Scheduler directories, so a successful logon followed by a file written there is the sequence to correlate ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). On the application tier, in analyst judgement, alert on anomalous bulk-query volumes or out-of-hours mass record retrieval in PeopleTools security-audit logs, and on egress anomalies consistent with bulk data transfer to non-standard destinations. Treat the appearance of unexpected ransom-note text files in web/app server document roots as a high-confidence lateral-movement indicator and, in analyst judgement, review `authorized_keys` for unauthorised additions.

**Hardening / mitigation.** Apply Oracle's Security Alert for CVE-2026-35273 and stay on a supported PeopleTools release, and disable the Environment Management Hub or remove PSEMHUB where it is not needed ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)); where the hub cannot be disabled, block external access to `/PSEMHUB/*` and `/PSIGW/HttpListeningConnector` at the network perimeter rather than relying on WAF body-inspection rules ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). Against the lateral-movement script, in analyst judgement, the advice is to rename or disable the default `psoft`/`oracle`/`linuxadm` OS accounts, review their `authorized_keys`, and hold administrative interfaces behind jump hosts. In analyst judgement, public-sector and university SOCs running PeopleSoft should also audit the external reachability of the web and application tier.

## Update — 2026-06-12T05:00:10Z

The initial-access vector that was attacker-asserted yesterday now has a CVE: Oracle assigned **CVE-2026-35273** (CVSS 9.8), an unauthenticated RCE in the PeopleTools Environment Management Hub (PSEMHUB, versions 8.61/8.62), and published an out-of-band Security Alert ([Oracle, 2026-06-10](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html)), with a patch Rapid7 tells PeopleTools 8.61 and 8.62 customers to apply on an emergency basis ([Rapid7, 2026-06-12](https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/)).

Mandiant GTIG formally attributes the campaign to UNC6240 (ShinyHunters), dating exploitation 27 May – 9 June, a zero-day for the full window, and details the post-exploitation chain: customised MeshCentral remote-management agents masquerading as Microsoft Azure components for persistence and C2, and a per-victim `_fanout.sh` lateral-movement script spraying SSH credentials against internal hosts harvested from `/etc/hosts` (`T1190`, `T1021.004`). Mandiant notified more than 100 organisations with exposed PSEMHUB endpoints; 68 % are higher-education institutions ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)).

At the University of Nottingham, ShinyHunters claims over 40 GB of student finance, billing and payment data, including data from the Malaysia and China campuses, and Have I Been Pwned's analysis of the partly published data counts about 455,000 unique email addresses with names, addresses, phone numbers, ethnicities, disabilities, passport numbers and fee-payment information; the university has reported the incident to Action Fraud and the Information Commissioner's Office ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/); [The Record, 2026-06-11](https://therecord.media/university-of-nottingham-cyber-incident-shiny-hunters); [University of Nottingham, 2026-06-10](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). Action: patch out-of-band **and** compromise-assess; yesterday's hardening guidance (default SSH service accounts, PSEMHUB exposure) stands.

## Update — 2026-06-13T05:00:07Z

Mandiant and Google GTIG formally attribute the PeopleSoft Environment Management Hub exploitation campaign to UNC6240 (ShinyHunters) and confirm the activity ran from 27 May to 9 June 2026, predating Oracle's 10 June out-of-band advisory, establishing CVE-2026-35273 (CVSS 9.8) as a zero-day at time of exploitation ([Mandiant/GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). The unauthenticated SSRF→RCE is reached via the `/PSEMHUB/hub` and `/PSIGW/HttpListeningConnector` endpoints in PeopleTools 8.61/8.62.

GTIG notified over 100 organisations whose endpoints correlated with exploitation; 68% are higher-education institutions. Post-exploitation, the actor deployed MeshCentral remote-management agents disguised as Azure binaries, used SSH fan-out scripts with PeopleSoft admin credentials for lateral movement, and exfiltrated to the ShinyHunters leak site ([Rapid7, 2026-06-12](https://www.rapid7.com/blog/post/etr-active-exploitation-of-oracle-peoplesoft-zero-day-cve-2026-35273/)). Have I Been Pwned's analysis of the leaked data puts the affected University of Nottingham students and alumni at 454,600, with passport numbers among the exposed fields ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/)); the university confirmed that data in its student-record system was accessed ([University of Nottingham](https://www.nottingham.ac.uk/currentstudents/news/student-and-alumni-data-has-been-compromised-in-a-data-security-incident)). CISA added the CVE to KEV on 12 June. Swiss and EU universities running Campus Solutions should treat it as a priority.

## Update — 2026-06-16T05:09:02Z

ShinyHunters listed the **Council of Europe** (the 46-member human-rights body), claiming **297 GB across ~429,000 files**, and set a **16 June leak deadline** ([SecurityWeek, 2026-06-15](https://www.securityweek.com/shinyhunters-claims-council-of-europe-hack/)); The Register reports the listing as part of ShinyHunters' PeopleSoft campaign ([The Register, 2026-06-15](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757)). This brings a European intergovernmental institution into the 100+-organisation PeopleSoft campaign previously covered as an education-sector wave.

The claimed dataset spans payroll for 10,000+ current and former staff (2011–2026), 14,000+ CVs, and HR records with names, dates of birth, addresses, bank-account, tax/social-security and medical data. The Council of Europe confirmed it "is currently investigating the matter and assessing the situation" and has not confirmed exfiltration ([The Register, 2026-06-15](https://www.theregister.com/cyber-crime/2026/06/15/council-of-europe-hacked-in-shinyhunters-peoplesoft-heist/5255757); [BleepingComputer, 2026-06-15](https://www.bleepingcomputer.com/news/security/council-of-europe-investigates-shinyhunters-data-breach-claims/)). The vector, unauthenticated HTTP to the `/PSEMHUB/hub` servlet (`T1190`), is unchanged; investigate any externally reachable PeopleSoft Environment Management Hub for compromise and block perimeter access to `/PSEMHUB/*`. Confidence on the victim claim is MEDIUM pending Council of Europe confirmation (extortion-site claim).

## Update — 2026-09-27T04:35:00Z

Mandiant and GTIG report that UNC6240 (ShinyHunters) has resumed mass exploitation of CVE-2026-35273, adapting to the defensive guidance published after the June wave. The actor now bypasses WAF rules that block the literal `/PSEMHUB/` path by requesting the URL-encoded `/%50SEMHUB/` instead: many WAFs and reverse proxies match the request path before decoding it, while the PeopleSoft application server decodes and routes the request normally. "This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure" ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)). Mandiant warns the actor may rotate to other percent-encoded, mixed-case or otherwise non-normalized path variants, so defenders should block on the normalized path rather than the literal string.

Before exploiting a target, the actor sends five to fifteen POST requests carrying a serialized Java object to quietly confirm exploitability without writing files or disrupting the service. Two complementary single-line JSP web shells are then dropped into the `PSEMHUB.war` directory: `x.jsp` executes hex-encoded commands cross-platform, and `u.jsp`/`u2.jsp` upload larger files in 150 KB Base64-encoded chunks, bypassing PeopleSoft's own file-size limits; a fileless variant returns command output directly in the HTTP response with nothing written to disk, defeating file-creation-based detection. On compromised Windows hosts, the actor uploads a trojanized installer, `Ple64.exe`, masquerading as a signed Light Alloy media-player installer and signed with a valid Extended Validation certificate Mandiant has asked the issuing certificate authority to revoke; it loads a VMProtect-3-packed multi-stage chain culminating in the SIDEEYE C++ backdoor, which steals browser and desktop credentials, manages processes and files, and provides an interactive reverse shell and reverse proxy over raw TCP. The actor also deploys the open-source Neo-reGeorg tunneling toolkit to route SOCKS5 proxy traffic over ordinary HTTP/S for internal lateral movement, and uses the legitimate MeshAgent/MeshCentral remote-management platform to maintain access on Linux hosts. "Across compromised instances, a quarter of the threat actor's commands executed as `root` or `NT Authority\SYSTEM`, granting full control of the operating system" ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)).

Targeting has expanded well beyond the original higher-education skew: "Google says the new wave of attacks has deployed web shells on dozens of systems worldwide within higher education, technology, IT services, healthcare, agriculture, transportation, and government organizations" ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)), and Mandiant's report names government among the sectors this wave has hit alongside the Council of Europe, which ShinyHunters listed in June and which said it was investigating. Mandiant's remediation guidance is unchanged in substance but sharper: apply the Oracle Security Alert and stay on a supported PeopleTools release rather than relying on a WAF at all; disable EMHub or remove PSEMHUB if not needed, since neither is required for standard PeopleSoft Internet Architecture user sessions; search WebLogic access logs for requests to `/PSEMHUB/` and its encoded variants and for POST requests to `/hub` with external-source bodies; and, on any host where a web shell is found, treat it as compromised, preserve evidence, and rotate every credential reachable from the PeopleSoft tier, prioritising hosts where WebLogic runs as `root` or `SYSTEM`.

This wave also clarifies part of a separately-tracked claim: ShinyHunters told BleepingComputer it used this same WAF-bypass technique against the FBI's own recruitment site, alongside a further, still-unconfirmed vulnerability it says it also exploited there.

**Defender takeaway:** a WAF rule that blocked the literal `/PSEMHUB/` path is no longer sufficient on its own; only patching, removing PSEMHUB, or a WAF reconfigured to match on the normalized path closes this exposure, and every organisation that relied on the June guidance's perimeter-blocking workaround should re-verify its control actually normalizes the path before matching.

## Correction — 2026-10-11T14:56:35Z

The main analysis described the initial-access vector as attacker-asserted and the campaign's CVEs as undisclosed. Oracle published an out-of-band Security Alert for CVE-2026-35273 (CVSS 9.8) on 2026-06-10 ([Oracle, 2026-06-10](https://www.oracle.com/security-alerts/alert-cve-2026-35273.html)), Mandiant assesses the campaign as consistent with exploitation of that CVE, dating it from 27 May, a zero-day for the whole window ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)), and the hardening advice now names that Security Alert and Mandiant's advice to remove the Environment Management Hub where it is not needed ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)). The count of about 455,000 affected University of Nottingham students and alumni is Have I Been Pwned's analysis of the leaked data, not a university figure; the university confirmed that data in its student-record system was accessed ([BleepingComputer, 2026-06-11](https://www.bleepingcomputer.com/news/security/nottingham-university-data-breach-affects-over-450-000-students/)). The exposed surface is the Environment Management Hub and the Integration Broker listening connector ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)), the script recovered from exposed servers spreads over SSH and drops ransom notes, ([BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/security/oracle-peoplesoft-servers-hacked-in-shinyhunters-data-theft-attacks/)), with exfiltration a separate step ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)), and the Council of Europe said it was investigating rather than confirming a breach.

## Improvement — 2026-10-21T08:13:55Z

The SSH spraying to hunt for originates inside the network: the recovered script runs on a compromised PeopleSoft server, sprays SSH credentials at the internal hosts named in that server's `/etc/hosts`, and on each successful session copies a marker file into the WebLogic and Process Scheduler directories ([Mandiant GTIG, 2026-06-11](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/)). Mandiant's advice for a host with a web shell is to rotate all credentials accessible from the PeopleSoft tier, prioritising hosts where WebLogic runs as `root` or `SYSTEM`; even commands run under the PeopleSoft or WebLogic service accounts reach PeopleSoft configuration files and database connection strings ([Mandiant/GTIG, 2026-09-25](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/)).
