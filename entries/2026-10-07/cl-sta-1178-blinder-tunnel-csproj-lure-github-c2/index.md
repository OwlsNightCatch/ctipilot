---
schema: 1
kind: threat
title: "CL-STA-1178 (Blinder Tunnel): an Iranian-nexus recruitment lure delivers a Visual Studio project that runs code when it is opened, then hijacks the .NET AppDomainManager, disables ETW and takes tasking from GitHub"
headline: "Unit 42: a coding-test Visual Studio project executes on open, then disables ETW and takes tasking from GitHub"
summary: >
  Unit 42 describes a March 2026 campaign by an Iranian-nexus cluster it calls CL-STA-1178 against an individual in Iraqi
  critical infrastructure, in which a recruiter persona impersonating Dubai Airports IT sent a coding-test Visual Studio
  project whose project file runs code during the design-time build, before any compile. The chain then hijacks the .NET
  AppDomainManager through a configuration file that disables ETW, sideloads a DLL, and uses the GitHub API and issue comments
  for command and control, with PowerShell run inside the hijacked process so no powershell.exe starts. No Swiss or European
  target is reported and Unit 42 is the only source.
discovered_at: "2026-10-07T04:47:00Z"
updated_at: null
event_date: "2026-10-06"
run_id: 2026-10-07T0404Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, iran-nexus]
regions: [middle-east]
sectors: [aviation, telco, technology]
entities: ["actor:cl-sta-1178", "campaign:blinder-tunnel", "malware:shelbyloader", "malware:blackwood", "actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt", "product:microsoft-visual-studio", "product:microsoft-net-framework"]
techniques: [T1204.002, T1127.001, T1574.014, T1685, T1574.001, T1027, T1547.001, T1102.001, T1102.002, T1059.001, T1572, T1036.005]
affected_products: ["Microsoft Visual Studio", "Microsoft .NET Framework"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-10-06"
    role: primary
closed_sources: []
evidence:
  - quote: "We discovered that an Iranian state-aligned threat actor has been masquerading as the Dubai Airports IT department to deliver trojanized coding challenges to high-value targets."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/"
  - quote: "the attackers defined a custom XML target with this exact name in their malicious .csproj file, overriding the safe Microsoft default behavior."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/"
  - quote: "Because Event Tracing for Windows (ETW) is critical for monitoring execution and detecting in-memory threats, this flag could impair detection capabilities."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/"
  - quote: "This allowed the attacker's script to execute without spawning PowerShell.exe."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/"
verification: single-source
sourcing_note: >
  Unit 42 is the sole assessor. Its Iranian-nexus attribution is its own high-confidence assessment, resting on Iranian-hosted
  infrastructure, file metadata, regional victimology and tradecraft overlaps, with Screening Serpens among them, that it calls low-confidence and not strong
  enough to attribute the cluster to any established group; the link to Elastic's earlier Shelby research rests on the shared
  Peaky Blinders theming. Unit 42 states it is not aware of any breach of Dubai Airports.
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

Unit 42 tracks an Iranian state-aligned cluster as CL-STA-1178 and names its March 2026 campaign against an individual in Iraqi critical infrastructure "Blinder Tunnel"; the infrastructure was staged from November 2025, and the same actor ran conflict-themed Google Drive credential phishing against an Israeli entity in May and June 2026 ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)). A recruiter persona impersonating the Dubai Airports IT department sent a decoy career-portal installer and then a weaponised C# Visual Studio project as an at-home coding test ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)). When a developer opens a project, Visual Studio runs a design-time build in the background, and the project file overrides one of the targets that step runs, so the payload executes at project load, before any compile; it copies binaries into a folder under the user profile and launches one of them ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)).

The launched binary is a renamed, signed Microsoft Visual Studio hosting process. A configuration file beside it replaces the .NET application's default app-domain manager with a malicious one and sets the ETW enable flag to false, which Unit 42 says could impair detection, and the loader, ShelbyLoader V2, then arrives through DLL sideloading ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)). The loader persists through a current-user startup registry value, authenticates to the GitHub API with a hard-coded personal access token for tasking, and falls back to encrypted routing data in comments on GitHub issues; a follow-on module hooks the PowerShell engine inside the hijacked process, so commands run without starting powershell.exe, and a second loader, Blackwood, runs the open-source Chisel tunnelling tool in memory to give a reverse SOCKS proxy into the victim's network ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)). GitHub removed the malicious infrastructure Unit 42 identified, and Unit 42 is not aware of any breach of Dubai Airports ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)).

**Exposure:** developers and IT staff who open third-party Visual Studio projects, such as recruiter coding tests or contractor repositories, on workstations that can reach the GitHub API; no Swiss or European target is reported ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)).

**Detection:** process-creation lineage showing Visual Studio or the build engine copying executables into a user-profile folder and launching one at project open; a renamed, signed Microsoft host binary with a sidecar configuration file that names an app-domain manager or turns ETW off; binaries that load unknown or non-standard DLLs outside system directories, which Unit 42 advises monitoring; non-browser, non-git processes calling the GitHub API with a token or searching issues; and the PowerShell engine loaded into a process that is not a PowerShell host ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)).

**Triage:** developers legitimately build projects and call GitHub, so the discriminators are that execution starts at project open rather than at a build the developer chose to run, a DLL beside a renamed signed host binary that does not belong to it, and a configuration file that changes ETW or app-domain settings.

**Defender takeaway:** treat a recruiter-supplied or third-party Visual Studio project as untrusted code before it is ever built, since Unit 42 reports execution at project load, and watch for the sideload and configuration-file signals above on developer workstations; Unit 42's own advice is to secure developer environments and monitor anomalous cloud-platform traffic ([Unit 42, 2026-10-06](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/)).
