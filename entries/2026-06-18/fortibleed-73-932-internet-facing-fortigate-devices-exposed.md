---
schema: 1
kind: incident
horizon: operational
title: >
  FortiBleed — 73,932 internet-facing FortiGate devices exposed, Russian-speaking group cracking
  credentials into Active Directory
headline: >
  FortiBleed — 73,932 internet-facing FortiGate devices exposed, Russian-speaking group cracking
  credentials into Active Directory
summary: >
  FortiBleed: ~73,000 internet-facing FortiGate devices across 194 countries under active
  credential abuse. A dataset of 73,932 unique FortiGate URLs (≈75,000 devices) with valid
  VPN/admin credentials — assembled from brute-force campaigns and reshared prior-incident data,
  not a new vulnerability per Fortinet — is being actively worked by a Russian-speaking group that
  has cracked credentials and moved laterally into Active Directory at multiple victims
  (BleepingComputer, 2026-06-17). Any org with an internet-exposed FortiGate should treat its
  admin/VPN credentials as potentially exposed and rotate.
discovered_at: "2026-06-18T05:10:28Z"
updated_at: "2026-06-23T04:52:50Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - actively-exploited
  - russia-nexus
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
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/"
    publisher: BleepingComputer
    role: primary
  - url: "https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/"
    publisher: Arctic Wolf
    role: corroborating
  - url: "https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure"
    publisher: CISA alert
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices"
    publisher: Fortinet PSIRT
    role: corroborating
  - url: "https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/"
    publisher: SOCRadar
    role: corroborating
closed_sources: []
evidence:
  - quote: "Threat actors deployed a Golang-based tool called 'FortigateSniffer' that abused FortiOS's built-in diagnose sniffer packet functionality to harvest authentication credentials from network traffic"
    publisher: BleepingComputer
  - quote: "Fortinet states the attack does not exploit new vulnerabilities, but rather reuses credentials from prior incidents ... combined with brute-force techniques against systems lacking strong passwords and MFA"
    publisher: SecurityWeek
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
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
migrated_from: briefs/2026-06-18.md
---

A dataset branded "FortiBleed" surfaced on 2026-06-17 containing 73,932 unique FortiGate management URLs — roughly 75,000 devices across 194 countries and 21,632 domains — paired with valid VPN and administrative credentials ([BleepingComputer, 2026-06-17](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)). Fortinet's position is that this is **not a new vulnerability**: the corpus is a reshare of data from previous incidents combined with large-scale brute-forcing, and the credentials were validated as working. Per BleepingComputer, a Russian-speaking actor is performing systematic credential validation, offline password cracking and onward lateral movement into Active Directory at fully-compromised organisations in several countries ([BleepingComputer, 2026-06-17](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/)); Arctic Wolf is separately tracking the FortiBleed campaign's reach across 194 countries ([Arctic Wolf, 2026-06-17](https://arcticwolf.com/resources/blog/active-fortibleed-campaign-impacting-fortinet-devices-across-194-countries/)). The technique class is valid-account abuse (`T1078`) following credential access, not exploitation of a fresh CVE.

**Why it matters to us:** FortiGate is ubiquitous on Swiss and EU public-sector perimeters. Treat any internet-exposed FortiGate's local admin and VPN credentials as potentially in the corpus regardless of patch level — patching does not rotate an already-leaked credential. Force admin and VPN password resets, enforce MFA on all administrative and VPN logins, restrict the management interface off the WAN, and review FortiGate admin-login audit events and downstream domain-controller authentication (Windows EID 4624/4768) for logins from unexpected source addresses.

## Update — 2026-06-20T05:12:18Z

The FortiBleed SSL VPN credential-harvesting campaign has grown from the 73,932 internet-facing FortiGate devices reported on 2026-06-18 to 86,644 confirmed compromised credentials across 194 countries, and CISA has published an emergency hardening advisory ([SecurityWeek, 2026-06-19](https://www.securityweek.com/fortibleed-86000-fortinet-device-credentials-compromised/); [CISA, 2026-06-18](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-credential-exposure)).

The new detail is methodology and impact: a Russian-speaking actor cracked SSL VPN password hashes with a 45-GPU Hashtopolis cluster, after which the actors pivot into internal Active Directory using harvested service and admin accounts ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/)). CISA's guidance mandates immediate SSL VPN session termination, full credential resets, enforcement of PBKDF2 (replacing the older MD5-crypt admin-hash scheme), and phishing-resistant MFA on all remote access. Defenders should cross-reference SSL VPN session logs against the Shadowserver notification feed and hunt for sequential VPN authentication failures from rotating residential IP ranges followed by a success and immediate internal RDP/SMB/LDAP reconnaissance.

## Update — 2026-06-23T04:52:50Z

New analysis published 2026-06-22 gives the first complete tool-chain picture of the FortiBleed credential-harvesting campaign. The operators deploy a purpose-built Golang tool, **FortigateSniffer**, that abuses FortiOS's native `diagnose sniffer packet` diagnostic command to capture authentication traffic on a compromised FortiGate; a second tool, **SNIFTRAN**, converts the captured traffic to PCAP, which a Python toolkit then parses for cleartext credentials, NTLM hashes, Kerberos tickets and LDAP/SQL auth material across ~24 protocols ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/); [SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)).

Fortinet's PSIRT response confirms the campaign uses **no new vulnerability** — it reuses credentials from the previously-disclosed CVE-2026-24858, CVE-2025-59718 and CVE-2025-59719 plus brute force against devices lacking strong passwords and MFA ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices); [SecurityWeek, 2026-06-22](https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/)). Reported tradecraft includes a distributed 36-GPU cluster — rented from a generative-AI provider, per BleepingComputer — for offline cracking of the harvested hashes; SOCRadar characterises the operators as Russian-speaking ([SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)).

The delta for defenders is a concrete detection surface that earlier coverage lacked: FortiOS audit-logs `diagnose sniffer packet` execution, so hunt for unexpected CLI sniffer invocations and stray PCAP files on the appliance, and — because harvested AD credentials are the downstream prize — treat all domain credentials on any FortiBleed-corpus device as compromised and force a domain-wide rotation, watching for anomalous Kerberos service-ticket requests (event 4769) and new-source Logon Type 3 events (4624) against privileged accounts. Upgrade to firmware with PBKDF2 password hashing to make offline cracking expensive, terminate active sessions, enable MFA and disable external management access.
