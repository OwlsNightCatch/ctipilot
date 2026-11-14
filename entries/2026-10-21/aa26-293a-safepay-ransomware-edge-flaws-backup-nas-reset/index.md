---
schema: 1
kind: threat
title: "AA26-293A: FBI, CISA and German and UK law enforcement describe SafePay ransomware, which enters through VPN credentials and five edge-device and backup-server flaws and factory-resets backup NAS devices before encrypting"
headline: "Joint advisory on SafePay: VPN credentials and five old edge and backup flaws in, backup NAS wiped before encryption"
summary: >
  CISA, the FBI, the US Secret Service, Germany's LKA Rheinland-Pfalz and UK law enforcement published advisory AA26-293A on 2026-10-20 on
  SafePay, which they say was among the most active ransomware groups in 2026 and has affected at least 600 victims, in Europe among
  other regions. Access comes from exposed credentials, brute force and phished account profiles used over Mullvad VPN addresses,
  and from five known flaws in Cisco ASA and Firepower Threat Defense, Veeam Backup and Replication and SonicWall SonicOS; the
  distinctive step is stopping the Volume Shadow Copy Service and factory-resetting the network storage that holds backups before
  encryption.
discovered_at: "2026-10-21T03:42:00Z"
updated_at: null
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime]
regions: [global, europe]
sectors: []
entities: ["actor:safepay"]
techniques: [T1190, T1133, T1110, T1078, T1098, T1136, T1021.001, T1021.002, T1021.006, T1569.002, T1218, T1059.001, T1059.003, T1548.002, T1134.001, T1685, T1027.002, T1219, T1560.001, T1048, T1567, T1490, T1486, T1070.004]
affected_products: ["Cisco Adaptive Security Appliance (ASA)", "Cisco Firepower Threat Defense (FTD)", "Veeam Backup & Replication", "SonicWall SonicOS"]
cves:
  - id: CVE-2020-3259
    cvss: "7.5 (CVSS 3.0)"
    epss: null
    type: info-disclosure
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "Cisco ASA and Firepower Threat Defense with specific AnyConnect and WebVPN configurations (CISA KEV); the versions are in Cisco's advisory"
    fixed: "the first fixed releases are listed in Cisco's advisory"
  - id: CVE-2023-20269
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "Cisco ASA and Firepower Threat Defense (CISA KEV entry: an unauthenticated remote attacker can conduct a brute force attack); versions not stated by the advisory"
    fixed: "not stated by the advisory"
  - id: CVE-2023-27532
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "Veeam Backup & Replication (CISA KEV entry: Cloud Connect component, missing authentication for a critical function); versions not stated by the advisory"
    fixed: "not stated by the advisory"
  - id: CVE-2024-40711
    cvss: null
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "Veeam Backup & Replication (CISA KEV entry: deserialization allowing an unauthenticated user to run code remotely); versions not stated by the advisory"
    fixed: "not stated by the advisory"
  - id: CVE-2024-40766
    cvss: "9.3 (CVSS 3.0)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev]
    affected: "SonicWall Gen 5 and Gen 6 devices, and Gen 7 devices running SonicOS 7.0.1-5035 and older (SonicWall)"
    fixed: "the patch builds are listed in SonicWall's advisory SNWLID-2024-0015"
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a"
    publisher: "CISA, FBI, USSS, LKA Rheinland-Pfalz, UK NCA (AA26-293A)"
    date: "2026-10-20"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-10-20"
    role: corroborating
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-info-disclose-9eJtycMB"
    publisher: "Cisco (advisory cisco-sa-asaftd-info-disclose, last updated 2024-02-21)"
    date: "2024-02-21"
    role: corroborating
  - url: "https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0015"
    publisher: "SonicWall (advisory SNWLID-2024-0015, last updated 2024-11-20)"
    date: "2024-11-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The SafePay threat actors have impacted at least 600 separate victims from multiple critical infrastructure sectors."
    publisher: "CISA, FBI, USSS, LKA Rheinland-Pfalz, UK NCA (AA26-293A)"
    source_url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a"
  - quote: "SafePay ransomware was among the most active ransomware groups in 2026."
    publisher: "CISA, FBI, USSS, LKA Rheinland-Pfalz, UK NCA (AA26-293A)"
    source_url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a"
  - quote: "SafePay threat actors halt the Volume Shadow Copy Service and reset Network Attached Storage containing victim backup data to initial factory settings to inhibit system recovery attempts"
    publisher: "CISA, FBI, USSS, LKA Rheinland-Pfalz, UK NCA (AA26-293A)"
    source_url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a"
verification: single-source-national-cert
sourcing_note: >
  The joint advisory is the primary and the only source for the behavior, a first-party statement of its authors' own
  investigations as recently as August 2026. It names the five CVE ids but no product or version, the product names come
  from CISA's Known Exploited Vulnerabilities catalog, and neither the advisory nor the catalog states affected or fixed
  versions, which Cisco's and SonicWall's advisories give for the two flaws they cover.
confidence: high
references:
  - "2026-09-30/manno-ti-commune-ransomware-safepay-claim"
  - "2026-06-23/sonicwall-cve-2024-40766-why-patched-firewalls-keep-falling"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

CISA, the FBI, the US Secret Service, Germany's Landeskriminalamt Rheinland-Pfalz and UK law enforcement published advisory AA26-293A on 2026-10-20, drawing on investigations as recently as August 2026; they say SafePay has affected businesses and critical infrastructure in North America, South America, Europe and Australia since August 2024, was among the most active ransomware groups in 2026 and has impacted at least 600 separate victims ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)). Initial access is exposed credentials, brute force password attacks and VPN access, with the actors using Mullvad VPN addresses and phished account profiles to reach victim networks and exploit CVE-2020-3259 and CVE-2023-20269 on edge devices, and automated scripts exploiting CVE-2023-27532, CVE-2024-40711 and CVE-2024-40766 on internet-exposed systems ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)). CISA's catalog names them as Cisco ASA and Firepower Threat Defense (the first two), Veeam Backup & Replication (the next two) and SonicWall SonicOS flaws ([CISA KEV catalog, 2026-10-20](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

Once inside, the actors take administrative rights on existing accounts or create new ones, run commands remotely with PsExec and WinRM, enumerate network shares with ShareFinder.ps1 and SharpShares.exe, disable security software, bypass User Account Control, then move over RDP and remote-management tools ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)). They compress data with 7-Zip or WinRAR and exfiltrate it with WinSCP, RClone, FileZilla or OneDrive, and sometimes install AnyDesk or TeamViewer ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)). Before encrypting they halt the Volume Shadow Copy Service and reset network-attached storage that holds backup data to factory settings; encryption then appends .SafePay ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)).

**Exposure:** an internet-facing Cisco ASA or Firepower Threat Defense, Veeam Backup & Replication or SonicWall SonicOS system that one of the five flaws affects, and any VPN or remote-access account protected by a password alone; the advisory states neither affected versions nor fixes, so they come from each vendor's advisory for the CVE. Cisco calls CVE-2020-3259 reachable by an unauthenticated, remote attacker and SonicWall's CVSS vector for CVE-2024-40766 needs no privileges and no user interaction ([Cisco, 2024-02-21](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-info-disclose-9eJtycMB); [SonicWall, 2024-11-20](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0015)). CISA's catalog says CVE-2020-3259 affects only specific AnyConnect and WebVPN configurations, and describes CVE-2023-27532 as a Cloud Connect flaw for an unauthenticated user within the backup infrastructure network perimeter ([CISA KEV catalog, 2026-10-20](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Detection:** VPN and firewall authentication logs for repeated failures then a success, Mullvad exit addresses and new accounts; directory audit logs for administrator-group changes; process-creation events for PsExec, WinRM and remote-management tools installed outside a change window; archive and file-transfer tools run by non-administrative workflows; and backup and NAS audit logs for a shadow-copy service stop or a factory reset.

**Triage:** 7-Zip, WinRAR, RClone, FileZilla, AnyDesk, TeamViewer, PsExec and WinRM are everyday administrative tools, and the advisory warns against calling them malicious without evidence of actor use ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)); a shadow-copy service stop or a factory reset of backup storage that follows them is the discriminating step.

**Defender takeaway:** confirm that every Cisco ASA or Firepower Threat Defense, Veeam Backup & Replication and SonicWall SonicOS system has the vendor's fix or mitigation for the five flaws, require multi-factor authentication on VPN and administrator accounts, and keep offline backups that are encrypted and immutable so that a factory reset of the NAS does not remove the restore path; the advisory recommends offline, encrypted and immutable backups ([CISA et al., 2026-10-20](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-293a)).
