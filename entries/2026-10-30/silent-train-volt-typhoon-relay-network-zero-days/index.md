---
schema: 1
kind: threat
title: "Silent Train: Lumen's Black Lotus Labs describes the rotating relay network Volt Typhoon used for one likely and four confirmed zero-day campaigns against management and control-plane platforms (Quest KACE, Versa Director, N-able N-central, Cisco Catalyst SD-WAN, Arista VeloCloud Orchestrator)"
headline: "Lumen: Volt Typhoon's Silent Train relay chains fronted zero-days against SD-WAN, N-central and KACE"
summary: >
  Lumen's Black Lotus Labs reports that Volt Typhoon ran exploitation, credential access and exfiltration through Silent Train, rotating chains of compromised SOHO, IoT and enterprise devices that it rebuilt for each operation,
  and that its monitoring uncovered one likely and four confirmed zero-day campaigns against endpoint and network management platforms and SD-WAN orchestrators, among them Cisco Catalyst SD-WAN, N-able N-central and Arista VeloCloud Orchestrator.
  The reported victims are US-centred and the report names no Swiss or European victim.
discovered_at: "2026-10-30T03:50:00Z"
updated_at: null
event_date: "2026-10-28"
run_id: 2026-10-30T0255Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, china-nexus]
regions: [global]
sectors: [telco, public-sector, defense]
entities: ["actor:volt-typhoon", "campaign:silent-train-covert-network-2026", "product:cisco-catalyst-sd-wan-controller", "product:arista-velocloud-orchestrator-on-prem", "product:n-able-n-central", "product:quest-kace-systems-management-appliance"]
techniques: [T1190, T1584.008, T1090.003, T1572, T1021.004, T1505.003, T1070]
affected_products: ["Cisco Catalyst SD-WAN Controller", "Arista VeloCloud Orchestrator On-Prem", "N-able N-central", "Quest KACE Systems Management Appliance"]
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework"
    publisher: "Lumen Black Lotus Labs"
    date: "2026-10-28"
    role: primary
  - url: "https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html"
    publisher: "The Hacker News"
    date: "2026-10-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This insight helped identify one likely and four confirmed zero-day campaigns targeting network and endpoint management platforms and SD-WAN orchestrators used by critical organizations."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework"
  - quote: "At the end of each session, operators removed all artifacts and dismantled the chain."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework"
  - quote: "Post-incident analysis with partners uncovered in-memory webshells, credential harvesting and abuse of native features such as endpoint control and remote file transfers."
    publisher: "Lumen Black Lotus Labs"
    source_url: "https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework"
verification: single-source
sourcing_note: >
  The analysis is Lumen's own, from its network telemetry, and The Hacker News relays it from a report shared with that outlet; the two are one assessor. Lumen published the report on 2026-10-28.
confidence: high
references: ["2026-10-29/keydrift-uat-11473-cisco-sd-wan-controllers-cve-2026-20127", "2026-07-28/cve-2026-16812-arista-velocloud-orchestrator-exploited", "2026-10-23/cve-2026-114625-arista-velocloud-orchestrator-sqli-exploited", "2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap"]
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

Lumen's Black Lotus Labs reports that Volt Typhoon used a covert framework it calls Silent Train, first seen in late 2023, for the phases that need protection: exploitation, credential access, data exfiltration and continued access to victims ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)). A session starts from a virtual private server outside the US, passes through compromised non-US SOHO and IoT devices and leaves through a compromised US device before the victim; more than 27 device classes were enrolled, from TP-Link routers and Netgear Orbi devices to Fortinet appliances and CyberPanel servers, and the enterprise platforms stayed in chains for one to three months as final hops ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)). The operators exploit exposed web interfaces on the relay devices and deploy only what chained SSH needs, namely temporary SSH services, keys, configuration files and living-off-the-land utilities, with reverse tunnels over open-source proxies in later variants; sessions averaged about four hours, and at the end the operators removed all artifacts and dismantled the chain ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)).

Lumen says its monitoring helped identify one likely and four confirmed zero-day campaigns against endpoint and network management platforms and SD-WAN orchestrators: Quest KACE, where the activity looked like an undisclosed flaw, affected more than 30 victims and fell after Quest's October 2025 updates (a moderate-confidence assessment); Versa Director in 2024; the N-able N-central flaws CVE-2025-8875 and CVE-2025-8876; Cisco Catalyst SD-WAN through CVE-2026-20127, exploited by late 2025 and after Cisco's February 2026 disclosure; and Arista VeloCloud Orchestrator through the zero-day later designated CVE-2026-16812 ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)). Post-incident analysis found in-memory webshells, credential harvesting and abuse of native platform features such as endpoint control and remote file transfers, and in several cases erased or altered logs ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)). The victims it names are US government, telecommunications, defence-industrial, managed-service and critical-infrastructure organisations, concentrated in Hawaii, California and Texas, and it names no European or Swiss victim ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)). The Hacker News carries the same findings from a report Lumen shared with it ([The Hacker News, 2026-10-28](https://thehackernews.com/2026/10/volt-typhoon-used-covert-silent-train.html)).

**Exposure:** internet-reachable management and control-plane platforms (endpoint management, SD-WAN controllers and orchestrators, out-of-band administration), and edge devices with exposed web interfaces, which can be enrolled as relay hops without any data of the owner being the target.

**Detection:** telemetry classes are administrative logins, API calls, remote file transfers and configuration changes on management platforms outside normal administration hours or workflow, in-memory web shells that leave no file on disk, and, on edge devices, temporary SSH services, unfamiliar keys and outbound reverse tunnels to unfamiliar upstream hosts ([Lumen Black Lotus Labs, 2026-10-28](https://www.lumen.com/blog/en-us/silent-train-volt-typhoon-operational-framework)).

**Defender takeaway:** restrict the administrative interfaces of management and control-plane platforms to a VPN, jump host or management network and prioritise their patching, as Lumen advises, and treat an edge device that shows temporary SSH services or reverse tunnels as a possible relay in someone else's intrusion chain.
