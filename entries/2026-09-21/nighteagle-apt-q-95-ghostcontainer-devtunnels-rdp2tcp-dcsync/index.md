---
schema: 1
kind: threat
title: "NightEagle (APT-Q-95) pivots to Russian targets, tunnels RDP through Microsoft's own legitimate dev-tunnels service, and DCSyncs domain credentials after exploiting BlueKeep"
headline: "Kaspersky: an APT group that abused Microsoft's own developer-tunnel feature to expose RDP outward, then chained BlueKeep into a full DCSync credential dump"
summary: >
  Kaspersky's Global Emergency Response Team documents NightEagle (also tracked as APT-Q-95), active
  since at least 2023 and previously focused on Asia, now confirmed against Russian organizations. The
  group deploys a VIEWSTATE-injected Exchange backdoor (GhostContainer), abuses Microsoft's legitimate
  dev-tunnels service plus the rdp2tcp tool to expose RDP outward without opening new firewall ports,
  and exploits CVE-2019-0708 (BlueKeep) and CVE-2020-0688 en route to a DCSync domain-credential dump.
discovered_at: "2026-09-21T04:42:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-09-21T0410Z-intel
priority: high
immediate_action: null
tags:
  - espionage
  - nation-state
  - identity
regions:
  - russia-cis
sectors: []
entities:
  - "actor:nighteagle"
  - "malware:ghostcontainer"
techniques:
  - T1078
  - T1190
  - T1505.003
  - T1027
  - T1685
  - T1572
  - T1090.001
  - T1036.005
  - T1210
  - T1053.002
  - T1558
  - T1003.006
affected_products: ["Microsoft Exchange Server", "Microsoft Windows"]
cves:
  - id: CVE-2020-0688
    cvss: "8.8"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "Microsoft Exchange Server (2010–2019, pre-February 2020 updates)"
    fixed: "February 2020 Exchange cumulative/security updates"
  - id: CVE-2019-0708
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "Windows RDP (Windows 7, Server 2008/2008 R2 and earlier RDP-enabled builds)"
    fixed: "May 2019 Windows security updates"
sources:
  - url: "https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/"
    publisher: "Kaspersky Securelist (GERT)"
    date: "2026-09-16"
    role: primary
closed_sources: []
evidence:
  - quote: "We have now identified attacks by the group targeting businesses in Russia."
    publisher: "Kaspersky Securelist (GERT)"
    source_url: "https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/"
  - quote: "This is a legitimate Microsoft mechanism that allows local web services to be published for internet access on *.*.devtunnels.ms domains. The attackers used this tunneling capability to expose port 3389 (RDP) on the compromised system."
    publisher: "Kaspersky Securelist (GERT)"
    source_url: "https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/"
  - quote: "In one incident, they exploited a well-known RDP implementation vulnerability, CVE-2019-0708 (BlueKeep). They used the vulnerable mechanism to create a local account on the system and add it to the Administrators and Remote Desktop Users groups."
    publisher: "Kaspersky Securelist (GERT)"
    source_url: "https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/"
  - quote: "The attackers also requested Kerberos tickets with a non-standard combination of flags (Forwardable, Proxiable, Renewable) and attempted to replicate the Domain-Password object from the Active Directory database to impersonate the domain controller (a technique known as DCSync) after obtaining an account with sufficient privileges."
    publisher: "Kaspersky Securelist (GERT)"
    source_url: "https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/"
verification: single-source
sourcing_note: >
  Kaspersky's Global Emergency Response Team is the sole publisher of this campaign update; no
  independent lab has corroborated the Russia-targeting pivot or the specific tooling chain.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Kaspersky's Global Emergency Response Team documents a NightEagle (also tracked as APT-Q-95) campaign, active since at least 2023 and previously focused on Asian targets, now confirmed against organizations in Russia ([Kaspersky Securelist, 2026-09-16](https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/)). Initial access used compromised VPN credentials, with connections originating from IP addresses in the Russian segment linked to Cloudflare WARP tunnels, as well as from European VPS ranges. On Microsoft Exchange servers the group deploys the GhostContainer backdoor, a .NET assembly that incorporates the Neo-reGeorg tunnel, an exploit component for CVE-2020-0688, and the `GhostWebShell` class from the ysoserial utility; Kaspersky assesses with high confidence that delivery reused a technique it had already documented — extracting Exchange's own ASP.NET machine keys, then overwriting the `VIEWSTATE` framework parameter and injecting a payload into it to launch the backdoor in memory. Once running, the backdoor evades detection by patching addresses in `amsi.dll` and `ntdll.dll`, blinding both the Antimalware Scan Interface and Windows Event Logging.

For network access, NightEagle abuses Microsoft's own legitimate dev-tunnels feature (`*.devtunnels.ms`) — a service meant to publish local developer web services to the internet — to expose port 3389 (RDP) outward on the compromised host, then layers `rdp2tcp`, a public RDP-virtual-channel TCP tunneling tool, inside that RDP session — a combination Kaspersky states lets the group maintain network access using legitimate services, without opening any additional suspicious port. Staged payloads on GitHub carry mismatched legitimate-sounding filenames (`adobe_32.exe`, `1c-office-plugin.exe`, `trueconf-broker.exe`) to blend in with normal software update or business-communication traffic. For lateral movement and privilege escalation, NightEagle exploited CVE-2019-0708 (BlueKeep) in one incident to create and elevate a local account into the Administrators and Remote Desktop Users groups, used Impacket's `atexec` to set scheduled netsh `portproxy` rules for internal port forwarding, and requested Kerberos tickets carrying a non-standard `Forwardable`/`Proxiable`/`Renewable` flag combination before executing DCSync against the `Domain-Password` object to dump domain credentials by impersonating the domain controller.

**Defender takeaway:** any environment permitting outbound access to `*.devtunnels.ms` should treat an unexpected dev-tunnels connection from a server or workstation as equivalent to an unauthorized reverse-tunnel opening; rdp2tcp's presence inside an RDP session is detectable via Windows event IDs 132 and 148 in `Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational.evtx`, where the RemoteFX virtual-channel name reads "rdp2tcp" or a random string in place of a legitimate RDS channel name. Confirm Exchange servers are current on CVE-2020-0688 and RDP-exposed legacy Windows builds are patched against CVE-2019-0708; a Kerberos ticket request combining `Forwardable`, `Proxiable` and `Renewable` flags together is an anomalous pattern worth a dedicated detection rule ahead of any DCSync attempt.

**Triage:** Microsoft dev-tunnels traffic to `*.devtunnels.ms` is legitimate on developer workstations running Visual Studio or the Dev Tunnels CLI — the discriminator is the host class: a production server, domain controller, or non-developer endpoint establishing an outbound dev-tunnels connection has no legitimate reason to do so.
