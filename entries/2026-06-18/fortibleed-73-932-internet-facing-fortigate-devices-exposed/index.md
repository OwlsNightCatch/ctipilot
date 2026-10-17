---
schema: 1
kind: incident
title: >
  FortiBleed: an active credential-compromise campaign against internet-facing FortiGate firewalls, now locking
  administrators out and supplying ransomware affiliates
headline: "FBI and Secret Service: FortiBleed is still active, locks admins out of FortiGates and feeds ransomware affiliates"
summary: >
  FortiBleed is an active credential-compromise campaign against internet-facing FortiGate firewalls and SSL VPN
  gateways, with SOCRadar counting more than 86,644 compromised devices in 194 countries; Fortinet said in June that it
  uses no new vulnerability, only reused credentials and brute force. A joint FBI and U.S. Secret Service advisory of
  2026-10-06 says attackers keep scanning exposed devices with previously obtained credentials, create administrator
  accounts on compromised firewalls and in some cases delete or change the original accounts so owners are locked out,
  and that access brokers using the chain have supplied INC/Lynx and Payload ransomware affiliates. An organisation
  with an internet-exposed FortiGate should end all administrator and VPN sessions, reset every credential and look
  for accounts and API keys it did not create.
discovered_at: "2026-06-18T05:10:28Z"
updated_at: "2026-10-08T04:58:53Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - actively-exploited
  - russia-nexus
  - ransomware
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - telco
  - manufacturing
entities:
  - "incident:fortibleed-fortigate-credential-exposure"
  - "product:fortinet-fortigate"
  - "product:fortinet-fortios"
  - "actor:inc-ransom"
  - "actor:payload-ransomware"
techniques: [T1595, T1110.003, T1110.004, T1003, T1110.002, T1133, T1078, T1136.001, T1087, T1531, T1041, T1583]
affected_products: ["Fortinet FortiGate", "Fortinet FortiOS"]
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.ic3.gov/CSA/2026/261006.pdf"
    publisher: "FBI and U.S. Secret Service (joint advisory JCSA-20261006-01)"
    date: "2026-10-06"
    role: primary
  - url: "https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices"
    publisher: Fortinet PSIRT
    role: corroborating
  - url: "https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/"
    publisher: Arctic Wolf
    role: corroborating
  - url: "https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure"
    publisher: CISA alert
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/"
    publisher: SOCRadar
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/"
    publisher: BleepingComputer
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "which abuses FortiOS's built-in diagnose sniffer packet functionality to capture authentication traffic traversing compromised FortiGate devices"
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/"
  - quote: "we believe the activity involves threat actors reusing credentials from previous incidents and employing brute-force techniques against devices with weak password hygiene and no multi-factor authentication (MFA)"
    publisher: SecurityWeek
    source_url: "https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/"
  - quote: "The FBI says that in some incidents, the threat actor creates administrator accounts and uses their privileges to delete existing admin accounts or change their passwords, denying victims access to their devices."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/"
  - quote: "Some groups benefiting from this are INC/Lynx ransomware and Payload ransomware."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/"
verification: multi-source
sourcing_note: >
  The FBI and Secret Service advisory is the primary source for the October developments; its device count rests on SOCRadar's reporting, which BleepingComputer also relays; the advisory's line on INC/Lynx and Payload
  names no source, and BleepingComputer reports SOCRadar's earlier link of the campaign to INC and Lynx separately.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "On every internet-facing FortiGate, terminate all administrator and VPN sessions, reset every administrator and VPN password, review the local administrator list and the REST API keys for entries nobody created (the actors add administrator accounts for persistence and may delete or lock the original ones), restrict management access to trusted hosts or a local-in policy, and enforce PBKDF2 for administrator password storage as Fortinet's guidance describes for FortiOS 7.2.11 and later."
updates:
  - at: "2026-06-20T05:12:18Z"
    run_id: 2026-06-20-4cfd00ef
    type: update
    summary: >
      FortiBleed escalates to 86,644 compromised FortiGate devices; CISA issues emergency hardening
      guidance. Up from 73,932 (covered 2026-06-18); attackers are cracking SSL VPN password hashes
      and pivoting into Active Directory (§ 4).
    fields:
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-20/fortibleed-reaches-86-644-compromised-fortigate-devices-cisa
  - at: "2026-06-23T04:52:50Z"
    run_id: 2026-06-23-165387f6
    type: update
    summary: >
      The FortiBleed credential-harvesting campaign got its first full tool-chain disclosure: a Golang
      "FortigateSniffer" that abuses FortiOS's native diagnose sniffer packet to capture auth traffic,
      a PCAP converter, and a 36-GPU offline-cracking cluster — with Fortinet confirming no new CVE,
      only credential reuse and brute force. The detection opportunity is the sniffer's own footprint
      (BleepingComputer, 2026-06-22).
    fields:
      - evidence
      - sectors
      - sources
      - body
    merged_from: 2026-06-23/fortibleed-first-full-tool-chain-disclosure-fortigatesniffer
  - at: "2026-10-08T04:58:53Z"
    run_id: 2026-10-08T0404Z-intel
    type: update
    summary: >
      A joint FBI and U.S. Secret Service advisory of 2026-10-06 says FortiBleed is still active: the operators create
      administrator accounts on compromised FortiGates and in some cases delete or change the original accounts, locking
      owners out, and access brokers using the chain have supplied INC/Lynx and Payload ransomware affiliates. It cites
      SOCRadar for more than 86,644 compromised devices and adds firewall, VPN and domain controller log review, REST API
      key review and PBKDF2 enforcement to the response.
    fields: [title, headline, summary, tags, entities, techniques, affected_products, classification, sources, evidence, sourcing_note, actions, body]
migrated_from: briefs/2026-06-18.md
---

A dataset branded "FortiBleed" was reported on 2026-06-18, containing 73,932 unique FortiGate management URLs, roughly 75,000 devices across 194 countries and 21,632 domains, paired with valid VPN and administrative credentials ([BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)). Fortinet's position is that this is **not a new Fortinet vulnerability**: it believes threat actors are reusing credentials from previous incidents and using brute force against devices with weak password hygiene and no multi-factor authentication ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)). BleepingComputer reports researcher Bob Diachenko's claim that a Russian-speaking multi-operator group harvested the credentials, cracked intercepted SSL VPN hashes on a 45-GPU cluster and moved laterally into internal Active Directory environments, with several organisations fully compromised; Diachenko says he drew this from files the attackers left exposed on the same server ([BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)); Arctic Wolf is separately tracking the FortiBleed campaign's reach across 194 countries ([Arctic Wolf, 2026-06-17](https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/)). The technique class is valid-account abuse following credential access, not exploitation of a fresh CVE.

**Exposure:** any internet-exposed FortiGate: Fortinet says the campaign reuses credentials from previous incidents and tells customers to reset administrator and VPN passwords, especially on internet-facing systems ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)), and BleepingComputer reports researcher Kevin Beaumont observing that many affected devices were running relatively recent FortiOS versions ([BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)).

**Detection:** administrator-login and configuration audit events on the FortiGate, and domain controller authentication logs for logins from unexpected sources ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)).

**Defender takeaway:** force administrator and VPN password resets, enforce MFA on every administrator and VPN login, and restrict management access to trusted hosts, a local-in policy or no internet administration ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)).

## Update — 2026-06-20T05:12:18Z

The FortiBleed SSL VPN credential-harvesting campaign has grown from the 73,932 internet-facing FortiGate devices reported on 2026-06-18 to 86,644 confirmed compromised credentials across 194 countries, and CISA has published a hardening alert ([SecurityWeek, 2026-06-19](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/); [CISA, 2026-06-18](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure)).

The new detail is methodology and impact, as researcher Bob Diachenko claims it: the operators intercept SSL VPN authentication, crack the hashes on a 45-GPU cluster managed through Hashtopolis and pivot into internal Active Directory environments ([SecurityWeek, 2026-06-19](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/); [BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)). CISA's alert urges terminating active sessions and resetting credentials, storing administrator logins with PBKDF2, reviewing logs, enabling phishing-resistant MFA and locking down management access ([SecurityWeek, 2026-06-19](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/)). Fortinet advises checking for unexpected administrator access from an unknown IP and reviewing domain controller logs for lateral movement ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)).

## Update — 2026-06-23T04:52:50Z

New analysis published 2026-06-22 gives a more detailed description of the tool chain behind the FortiBleed credential-harvesting campaign. SOCRadar's report, as BleepingComputer describes it, alleges a purpose-built Golang tool, **FortigateSniffer**, that abuses FortiOS's built-in `diagnose sniffer packet` command to capture authentication traffic on a compromised FortiGate, with a component named **SNIFTRAN** reconstructing the captured traffic into PCAP files and a Python toolkit extracting cleartext credentials, password hashes, Kerberos tickets and NTLM authentication material from them, across 24 protocols ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/)).

Fortinet's PSIRT response confirms the campaign uses **no new vulnerability**: it reuses credentials from the previously-disclosed CVE-2026-24858, CVE-2025-59718 and CVE-2025-59719 plus brute force against devices lacking strong passwords and MFA ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices); [SecurityWeek, 2026-06-22](https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/)). Reported tradecraft includes a distributed 36-GPU cluster rented from a GenAI company for offline cracking of the harvested hashes, according to researcher Kevin Beaumont ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/)), where Diachenko's earlier claim was a 45-GPU cluster managed through Hashtopolis ([BleepingComputer, 2026-06-18](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)); SOCRadar characterises the operators as Russian-speaking ([SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)).

The delta for defenders is a concrete detection surface that earlier coverage lacked: the tool connects to the FortiGate over SSH and launches the `diagnose sniffer packet` command ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/)), so hunt for unexpected invocations of that command on the appliance, and, because harvested AD credentials are the downstream prize, treat all domain credentials on any FortiBleed-corpus device as compromised and force a domain-wide rotation, watching for anomalous Kerberos service-ticket requests (event 4769) and new-source Logon Type 3 events (4624) against privileged accounts. Upgrade to firmware with PBKDF2 password hashing to make offline cracking expensive, terminate active sessions, enable MFA and disable external management access.

## Update — 2026-10-08T04:58:53Z

A joint advisory of the FBI and the U.S. Secret Service (JCSA-20261006-01, 2026-10-06) calls FortiBleed an active, global credential-compromise campaign against internet-facing FortiGate firewalls and SSL VPN gateways, cites SOCRadar for more than 86,644 compromised devices in 194 countries, and says attackers are continuing to scan exposed devices with previously obtained credentials ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)). The operators scan exposed SSL VPN portals, run credential stuffing and password spraying from earlier Fortinet leak dumps and infostealer logs, pull password hashes and session tokens from compromised devices and crack the hashes offline with Hashcat and Hashtopolis on a rented GPU cluster; the advisory ties the success to reused or leaked credentials and a legacy SHA-256 password storage ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)).

What the advisory adds is the lockout. On a compromised firewall the actors create administrator accounts that were not there before and, in some cases, delete existing accounts or change their passwords, so the owners cannot log in and recovery needs steps beyond patching and password resets ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf); [BleepingComputer, 2026-10-07](https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/)). Cracked credentials are enriched and validated by scripts that filter out honeypots and rank targets by revenue and network structure; with verified credentials the attackers enumerate Active Directory accounts and spray passwords to find privileged users, and the operation packages working VPN configurations and target lists for sale, the role of an initial-access broker ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)). The advisory says the chain has been an initial entry point for ransomware affiliates, currently INC/Lynx and Payload ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)); SOCRadar had linked FortiBleed to INC and Lynx in July after reaching both groups' negotiation panels on a server used in the campaign ([BleepingComputer, 2026-10-07](https://www.bleepingcomputer.com/news/security/fbi-ongoing-fortibleed-attacks-lock-out-fortigate-vpn-admins/)).

The advisory's measures: restrict external management through trusted hosts, a local-in policy or no internet administration at all; terminate all administrative and VPN sessions and reset all Fortinet VPN and administrator passwords; require phishing-resistant MFA on remote access and administrator accounts; review users, configuration and REST API keys for entries nobody created, removing unknown keys and refreshing the legitimate ones; enforce PBKDF2 for administrator password storage per Fortinet's guidance for FortiOS 7.2.11 and later; and review firewall, VPN, authentication and domain controller logs for lateral movement ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)). On a FortiGate the matching telemetry is the configuration and administrator audit log (administrator accounts created or deleted, passwords changed, new REST API keys); behind the VPN it is the domain controller authentication log, for lateral movement ([FBI and U.S. Secret Service, 2026-10-06](https://www.ic3.gov/CSA/2026/261006.pdf)).
