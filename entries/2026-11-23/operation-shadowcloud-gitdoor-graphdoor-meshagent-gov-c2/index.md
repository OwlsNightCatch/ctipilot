---
schema: 1
kind: threat
title: "Operation ShadowCloud: Kaspersky's GitDoor and GraphDoor backdoors hide command and control in GitHub, Microsoft Graph with SharePoint, and Ably against government networks in Asia and Africa, delivered through an abused MeshCentral agent and DLL sideloading"
headline: "Kaspersky: ShadowCloud's GitDoor and GraphDoor hide C2 in GitHub and Microsoft Graph, planted via a MeshCentral agent"
summary: >
  Kaspersky GReAT describes Operation ShadowCloud, an intrusion set identified in early 2026 that abuses the legitimate MeshCentral agent to drop two new backdoors, GitDoor and GraphDoor, with victims in Asia and Africa primarily in the government sector; the entry point is unknown. The operators sideload a loader DLL into a legitimate program beside an encrypted config.ini, and the backdoors take commands through the GitHub API (GitDoor) or Microsoft Graph and SharePoint (GraphDoor), with Ably as a further channel. Kaspersky does not attribute the activity and reports overlaps with FamousSparrow and CopperTurtle; Sophos tracks a fragment as BRONZE SANDCASTLE.
discovered_at: "2026-11-23T04:38:00Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-23T0355Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, cloud]
regions: [apac, africa]
sectors: [public-sector]
entities: ["campaign:operation-shadowcloud", "malware:gitdoor", "malware:graphdoor", "actor:bronze-sandcastle", "product:meshcentral-meshagent"]
techniques: [T1219, T1574.001, T1569.002, T1102.002, T1071.001, T1055, T1620, T1027, T1090, T1056.001, T1113, T1057, T1003.001, T1539, T1105, T1583.006]
affected_products: ["MeshCentral MeshAgent", "Microsoft Graph", "GitHub"]
cves: []
sources:
  - url: "https://securelist.com/operation-shadowcloud-gitdoor/122004/"
    publisher: "Kaspersky Securelist (GReAT), part 1"
    date: "2026-11-17"
    role: primary
  - url: "https://securelist.com/operation-shadowcloud-graphdoor/122005/"
    publisher: "Kaspersky Securelist (GReAT), part 2"
    date: "2026-11-17"
    role: primary
  - url: "https://www.sophos.com/en-us/blog/bronze-sandcastle-deploys-modified-meterpreter-shells"
    publisher: "Sophos Counter Threat Unit"
    date: "2026-10-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We found victims in Asia and Africa, primarily within the government sector."
    publisher: "Kaspersky Securelist"
    source_url: "https://securelist.com/operation-shadowcloud-gitdoor/122004/"
  - quote: "The exact entry point that let the attackers install the agent is unknown, but evidence points to the reuse of a prior infection already present on the network."
    publisher: "Kaspersky Securelist"
    source_url: "https://securelist.com/operation-shadowcloud-gitdoor/122004/"
  - quote: "Currently, we lack sufficient information to definitively attribute this activity to a specific threat group."
    publisher: "Kaspersky Securelist"
    source_url: "https://securelist.com/operation-shadowcloud-graphdoor/122005/"
verification: multi-source
sourcing_note: >
  Kaspersky is first-hand for the backdoors, plug-ins and infrastructure; Sophos independently investigated a cluster it attributes to BRONZE SANDCASTLE that shares the sideloading pattern and the Ably and GitHub channels, and Kaspersky says Sophos covered a fragment of this campaign. Kaspersky makes no attribution, so the link to BRONZE SANDCASTLE, FamousSparrow and CopperTurtle is an overlap and not an identity. Kaspersky names a Taiwanese organisation for the first observed step; the countries listed here come from Sophos's victim analysis.
confidence: medium
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

Kaspersky GReAT describes Operation ShadowCloud, an intrusion set identified in early 2026 that abuses the legitimate MeshAgent utility to drop two new backdoors, with victims in Asia and Africa primarily in the government sector ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)). The entry point is unknown: the first observed step is a MeshCentral agent launched inside a Taiwanese organisation, with evidence pointing to reuse of a prior infection on the network ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)). Through the agent the operators drop a legitimate binary, a malicious loader DLL and an encrypted payload file named config.ini, so the legitimate program loads the loader when it starts; hosts include a Sandboxie launcher, an OpenJDK launcher, a Python application and Sysinternals ZoomIt started as a service ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)). Sophos, which tracks the Sandboxie sideloading as BRONZE SANDCASTLE and which Kaspersky says covered a fragment of this campaign ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)), saw victims between August 2025 and August 2026 in the Philippines, Taiwan, Afghanistan, Namibia and likely the Republic of Korea ([Sophos, 2026-10-20](https://www.sophos.com/en-us/blog/bronze-sandcastle-deploys-modified-meterpreter-shells)).

GitDoor uses GitHub as its command channel: it opens and labels an issue through the GitHub API, writes victim data to a private repository and reads commands and plug-ins from a public one, authenticating with a personal access token ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)). GraphDoor requests a token for an attacker-registered application with the client-credentials grant from Microsoft's sign-in endpoint, then writes encrypted data to files named like JavaScript source maps in a SharePoint document library through Microsoft Graph ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/)). Both download plug-ins on demand and run shellcode in memory, among it Mimikatz and a browser-cookie stealer, with plug-ins for keylogging, screen capture and proxying through a modified Erfrp client or Ably ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/); [Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/)). Kaspersky says it lacks sufficient information to attribute the activity and reports overlaps with the Chinese-speaking groups FamousSparrow and CopperTurtle, which on several victim systems shared staging directories with GitDoor ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/)).

**Exposure:** Windows servers and workstations in networks that let non-browser processes reach GitHub, Microsoft's sign-in and Graph endpoints and Ably over HTTPS, and where a MeshCentral agent is not a tool the organisation deploys ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/); [Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/)).

**Detection:** in endpoint inventory and process telemetry, MeshCentral agent processes and services that IT did not deploy, and a legitimate program (a Sandboxie start binary, an OpenJDK launcher, a Python host, ZoomIt) loading a DLL from the folder where an encrypted config.ini sits, as in the first instance Kaspersky shows, in system32 ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)). In network and identity telemetry, a non-browser process requesting an app-only token from Microsoft's sign-in endpoint and then writing files through Microsoft Graph to a SharePoint site outside your tenant, and a process other than a git client or CI runner calling the GitHub API to open issues, label them and write repository contents with a personal access token ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/); [Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)).

**Triage:** MeshCentral is legitimate software, so the agent alone is not the signal; the signal is an agent no administrator deployed that drops a legitimate binary, a DLL and an encrypted config.ini side by side ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)).

**Defender takeaway:** hunt now for MeshCentral agents nobody deployed and for that binary, DLL and config.ini triad, and baseline which processes on servers and workstations legitimately call GitHub, Microsoft Graph and Ably, because both backdoors hide their command channel in that traffic and Kaspersky found the entry point unknown ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-gitdoor/122004/)).
