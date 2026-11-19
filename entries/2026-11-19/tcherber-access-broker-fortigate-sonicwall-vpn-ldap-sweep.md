---
schema: 1
kind: threat
title: "tcherber: Cyderes finds an access broker's Go toolkit with VPN clients for FortiGate and SonicWall that, once a tunnel is up, maps internal routes and sweeps Active Directory over LDAP; a credential file mixes default guest, admin and test logins with organisation-specific passwords (more than 500 FortiGate entries) and connection logs show root-level tunnels into multiple victims in May and June 2026"
headline: "Cyderes: 'tcherber' VPN toolkit for FortiGate and SonicWall, credential file mixing default and real logins, LDAP sweep"
summary: >
  Cyderes' Howler Cell recovered a Go toolkit that wraps OpenConnect for FortiGate and NetExtender for SonicWall, a credential file of more than 500 FortiGate entries mixing default guest, admin and test logins with organisation-specific passwords, and VPN connection logs showing sustained root-level tunnels into multiple victim environments in May and June 2026. Once the tunnel is up the orchestrator maps internal routes and enumerates Active Directory over LDAP, while port scanning, SMB reconnaissance and credential validation are manual tools. Cyderes assesses a Russian-speaking initial access broker and malware-as-a-service seller and names no victim, vulnerability or firmware version.
discovered_at: "2026-11-19T05:22:00Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-19T0355Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, identity, cryptocrime]
regions: [global]
sectors: [technology]
entities: ["actor:tcherber", "malware:enigma-locker"]
techniques: [T1133, T1078.001, T1087.002, T1069.002, T1016]
affected_products: ["Fortinet FortiGate", "SonicWall SSL VPN"]
cves: []
sources:
  - url: "https://www.cyderes.com/howler-cell/exposing-tcherber"
    publisher: "Cyderes Howler Cell"
    date: "2026-11-17"
    role: primary
  - url: "https://www.vmray.com/news/one-leftover-build-path-links-an-infostealer-a-remote-access-tool-and-a-ransomware-family/"
    publisher: "VMRay Labs"
    date: "2026-09-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Howler Cell identified a database containing more than 500 FortiGate VPN credential entries, together with VPN connection records showing successful root-level network tunnels into multiple victim environments during May and June 2026."
    publisher: "Cyderes Howler Cell"
    source_url: "https://www.cyderes.com/howler-cell/exposing-tcherber"
  - quote: "Contains a mix of default credentials (guest:guest, admin:admin, test:test) and organization-specific passwords, indicating both brute-force harvesting and credential dump sourcing."
    publisher: "Cyderes Howler Cell"
    source_url: "https://www.cyderes.com/howler-cell/exposing-tcherber"
  - quote: "The remaining tools (nmap.go, netexec_scaner.go, smb_info.go, sonik.go) are not called by the orchestrator and are intended for manual use by the operator as needed."
    publisher: "Cyderes Howler Cell"
    source_url: "https://www.cyderes.com/howler-cell/exposing-tcherber"
  - quote: "Defenders should treat the indicators in this report as current and actionable and prioritize VPN credential audits across FortiGate and SonicWall appliances."
    publisher: "Cyderes Howler Cell"
    source_url: "https://www.cyderes.com/howler-cell/exposing-tcherber"
verification: single-source
sourcing_note: >
  Cyderes is the only source for the toolkit, the credential file and the connection logs, and names no victim, vulnerability, firmware version or multi-factor setup; the handle rests on a build-path username that may be shared by several machines. VMRay independently links the same build identity to an infostealer, a ransomware family and a remote-control tool, but says nothing about VPN access brokerage.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Audit every FortiGate and SonicWall VPN gateway for local accounts with default or guessed passwords (guest, admin, test) or passwords that appear in credential dumps, reset or remove them, and search VPN logs since May 2026 for logins by such accounts that are followed by a broad LDAP enumeration from the VPN address pool, because Cyderes found a broker's toolkit and logs showing root-level tunnels into multiple victims."
updates: []
migrated_from: null
---

Cyderes' Howler Cell identified a database holding more than 500 FortiGate VPN credential entries and VPN connection records showing successful root-level tunnels into multiple victim environments during May and June 2026 ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)). The recovered Go toolkit wraps OpenConnect with --protocol=fortinet for FortiGate, with a 30-second reconnect loop that keeps the tunnel up, and NetExtender for SonicWall, whose wrapper probes seven login URL paths and ten page patterns to find the authentication domain ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)). The credential file mixes default guest, admin and test logins with organisation-specific passwords, which Cyderes reads as both brute-force harvesting and credential-dump sourcing; the broker's forum advert claims the access came from brute-forcing and an "exploit toolkit", which Cyderes relays without confirming ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)).

The orchestrator launches the FortiGate client in the background with a 20-second stabilization delay, maps internal subnets and gateways from the established tunnel, and runs an LDAP module that enumerates users, groups, domain structure and domain controllers; port scanning, SMB reconnaissance and credential validation sit in separate tools that the operator runs by hand ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)). Cyderes assesses a Russian-speaking operator working as both an initial access broker and a malware-as-a-service provider, with operations ongoing as of September 2026, and notes that the handle comes from a build-path username that one machine or several could share ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)). VMRay independently links the same build path to Zer0day Stealer and ENIGMA Locker and calls the same developer the likely author of an HVNC remote-control sample, without mentioning VPN access brokerage ([VMRay, 2026-09-01](https://www.vmray.com/news/one-leftover-build-path-links-an-infostealer-a-remote-access-tool-and-a-ransomware-family/)).

**Exposure:** a FortiGate or SonicWall VPN gateway reachable from the internet that accepts a local account with a default or guessed password, or a password that appears in a credential dump; Cyderes names no vulnerability or firmware version and does not discuss multi-factor authentication ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)).

**Detection:** VPN gateway logs for successful logins by default-named accounts and for repeated reconnect attempts from one source about every 30 seconds, the interval of the FortiGate client's retry loop; after the tunnel is up, route parsing and a broad LDAP enumeration of users, groups and domain controllers from an address in the VPN pool follow from the toolkit's orchestrator ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)).

**Defender takeaway:** audit VPN credentials on FortiGate and SonicWall appliances, which is Cyderes' own recommendation, and treat default-named accounts and dumped passwords as the entry the toolkit relies on ([Cyderes, 2026-11-17](https://www.cyderes.com/howler-cell/exposing-tcherber)).
