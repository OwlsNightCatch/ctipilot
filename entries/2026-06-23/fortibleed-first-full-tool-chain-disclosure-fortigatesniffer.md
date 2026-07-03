---
schema: 1
kind: vulnerability
horizon: operational
title: "FortiBleed — first full tool-chain disclosure (FortigateSniffer, SNIFTRAN, GPU cracking cluster); Fortinet confirms no new CVE"
headline: "FortiBleed — first full tool-chain disclosure (FortigateSniffer, SNIFTRAN, GPU cracking cluster); Fortinet confirms no new CVE"
summary: "The FortiBleed credential-harvesting campaign got its first full tool-chain disclosure: a Golang \"FortigateSniffer\" that abuses FortiOS's native diagnose sniffer packet to capture auth traffic, a PCAP converter, and a 36-GPU offline-cracking cluster — with Fortinet confirming no new CVE, only credential reuse and brute force. The detection opportunity is the sniffer's own footprint (BleepingComputer, 2026-06-22)."
discovered_at: "2026-06-23T04:52:50Z"
event_date: 2026-06-22
run_id: 2026-06-23-165387f6
priority: high
immediate_action: null
tags:
  - actively-exploited
  - data-breach
  - russia-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
  - manufacturing
  - telco
entities:
  - "incident:fortibleed-fortigate-credential-exposure"
cves: []
sources:
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
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2026-24858, CVE-2025-59718, CVE-2025-59719)"
confidence: high
update_of: 2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-23.md
---

**UPDATE (originally covered 2026-06-18, last 2026-06-20):** New analysis published 2026-06-22 gives the first complete tool-chain picture of the FortiBleed credential-harvesting campaign. The operators deploy a purpose-built Golang tool, **FortigateSniffer**, that abuses FortiOS's native `diagnose sniffer packet` diagnostic command to capture authentication traffic on a compromised FortiGate; a second tool, **SNIFTRAN**, converts the captured traffic to PCAP, which a Python toolkit then parses for cleartext credentials, NTLM hashes, Kerberos tickets and LDAP/SQL auth material across ~24 protocols ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/); [SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)).

Fortinet's PSIRT response confirms the campaign uses **no new vulnerability** — it reuses credentials from the previously-disclosed CVE-2026-24858, CVE-2025-59718 and CVE-2025-59719 plus brute force against devices lacking strong passwords and MFA ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices); [SecurityWeek, 2026-06-22](https://www.securityweek.com/fortinet-responds-to-fortibleed-campaign/)). Reported tradecraft includes a distributed 36-GPU cluster — rented from a generative-AI provider, per BleepingComputer — for offline cracking of the harvested hashes; SOCRadar characterises the operators as Russian-speaking ([SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/)).

The delta for defenders is a concrete detection surface that earlier coverage lacked: FortiOS audit-logs `diagnose sniffer packet` execution, so hunt for unexpected CLI sniffer invocations and stray PCAP files on the appliance, and — because harvested AD credentials are the downstream prize — treat all domain credentials on any FortiBleed-corpus device as compromised and force a domain-wide rotation, watching for anomalous Kerberos service-ticket requests (event 4769) and new-source Logon Type 3 events (4624) against privileged accounts. Upgrade to firmware with PBKDF2 password hashing to make offline cracking expensive, terminate active sessions, enable MFA and disable external management access.
