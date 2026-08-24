---
schema: 1
kind: threat
horizon: operational
title: "SilkParasite runs seven RAT families behind six signed-application side-loading pairs — and the reusable detection is the pairing itself, not any DLL name: a signed binary loading a library placed beside it from an unusual location"
headline: "SilkParasite gets five named RAT families and one reusable detection: the side-loading pairing, not the DLL name"
summary: >
  Bitdefender documented SilkParasite on 2026-08-19, a China-nexus cluster it holds at medium confidence and
  deliberately does not attribute to a single controlling actor, running espionage against government bodies in
  Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan and Kazakhstan with one recovered lure addressed to a Georgian
  government entity. Seven RAT families are involved, five newly named: DriveSilkRAT, whose command-and-control runs
  entirely through a shared Google Drive folder with twelve in-memory .NET plugins and executes commands through WMI
  rather than spawning a shell; CookiETagRAT, which carries tasking inside HTTP Cookie and ETag headers under a
  per-host key; plus NomadRAT, GoginRAT and NodeEdgeRAT. Initial access runs through malicious Office documents; what Bitdefender calls the most
  consistent detection surface across the campaign, used by most of the toolset rather than all of it, is DLL
  side-loading beside a legitimate signed application — Calibre, ABBYY FineReader, Quick Heal, Mp3tag and a Windows
  Defender component among the named hosts — and its own detection formulation is that the reliable signal is the
  pairing rather than the library name.
discovered_at: "2026-08-24T09:18:00Z"
event_date: "2026-08-19"
run_id: 2026-08-24T0410Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, china-nexus, ai-abuse, cloud]
regions: [apac, europe, global]
sectors: [public-sector]
entities:
  - campaign:silkparasite-central-asia-2026
  - malware:drivesilkrat
  - malware:cookietagrat
  - malware:nomadrat
  - malware:goginrat
  - malware:nodeedgerat
techniques: [T1574.001, T1566.001, T1102.002, T1071.001, T1047, T1620, T1573.001, T1027]
affected_products: []
cves: []
sources:
  - url: "https://www.bitdefender.com/en-us/blog/businessinsights/silkparasite-tracking-china-nexus-apt-across-central-asia"
    publisher: "Bitdefender"
    date: "2026-08-19"
    role: primary
closed_sources: []
evidence:
  - quote: "The most consistent detection surface across the campaign is DLL sideloading, and the reliable signal is the pairing, not the DLL name alone: a legitimately signed application loading a library placed beside it while running from an unusual location."
    publisher: "Bitdefender"
  - quote: "SilkParasite is primarily assisted: capable humans do the engineering and lean on AI to move faster, leaving behind a few tells but none of the degradation."
    publisher: "Bitdefender"
verification: single-source
sourcing_note: >
  Single-source: Bitdefender is the discovering party and no second party has examined this cluster. Attribution
  discipline follows the vendor's own, which is deliberately restrained: the China-nexus affiliation is held at
  medium confidence on four circumstantial grounds — another vendor's public link between one of the older RATs and a
  China-based group, infrastructure on a Chinese carrier backbone, a victim profile fitting a China-nexus
  intelligence interest, and one family's placement in a known malware lineage — and Bitdefender states explicitly
  that shared tooling ecosystems are not the same as a single controlling actor and that IP-level infrastructure
  analysis is circumstantial. This entry therefore carries SilkParasite as a cluster designation, not as an actor,
  and records no attribution edge to any named group. The AI-assistance assessment is likewise the vendor's, at
  medium confidence. Two elements of this research were already published here inside the window by strategic
  synthesis entries — the Google Drive and Cookie/ETag command channels, and the AI-assistance tells — and are
  referenced rather than presented as new; what this entry adds is the dedicated operational treatment, the five named
  families as registry entities, and the side-loading pairing discriminator, none of which those entries carry.
confidence: medium
update_of: null
references: [2026-08-23/weekly-w34-c2-rendezvous-moved-to-services-you-cannot-block, 2026-08-23/weekly-w34-ai-bought-throughput-not-capability]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Bitdefender published an analysis on 2026-08-19 of **SilkParasite**, a cluster designation for espionage activity against government bodies in Uzbekistan, Turkmenistan, Kyrgyzstan, Tajikistan and Kazakhstan using regionally tailored lures — several impersonating specific ministries — with one further document recovered from a public malware-sharing platform addressed to a Georgian government entity ([Bitdefender, 2026-08-19](https://www.bitdefender.com/en-us/blog/businessinsights/silkparasite-tracking-china-nexus-apt-across-central-asia)). Seven remote-access families are involved. Two were previously documented by other vendors; **five are newly named here — DriveSilkRAT, CookiETagRAT, NomadRAT, GoginRAT and NodeEdgeRAT**.

Two of the five are worth a defender's attention for their command-and-control choices rather than their capabilities. **DriveSilkRAT** runs its tasking entirely through a **shared Google Drive folder**: operators drop command files in, the infected host polls the folder, downloads the tasking, executes it through a system of twelve custom in-memory .NET plugins covering process listing, system and network enumeration, file management and command execution, and uploads results back to the same folder. Its command execution runs through Windows Management Instrumentation rather than spawning a command interpreter directly, which removes the parent-child process shape most detections key on. Bitdefender observed roughly 65 infection instances at the time of writing, stating that figure is an upper bound rather than a machine count because the victim identifiers derive from hardware fingerprinting. **CookiETagRAT** puts its tasking in **HTTP Cookie and ETag response headers**, returning results in the body, with each host deriving its own stream-cipher key and nonce from a unique system identifier plus a fixed suffix — so captured traffic from one victim cannot decrypt another's. It also runs its malicious logic directly from the library's entry point rather than waiting for an exported function to be called, which makes it fire immediately in a sandbox as well as on a victim.

Initial access is a malicious Microsoft Office document, most likely spearphished, rather than the side-loading itself; what side-loading gives is the most consistent *detection* surface across the campaign — Bitdefender's phrasing is "most of the toolset", not all of it. Six side-loading pairs are named, each a legitimately signed application loading a malicious library placed alongside it: Calibre's ebook editor, ABBYY FineReader, a Quick Heal component, Mp3tag, a Windows Defender service binary, and one still-unidentified signed host. Bitdefender's own formulation of the detection is the reusable part: "The most consistent detection surface across the campaign is DLL sideloading, and the reliable signal is the pairing, not the DLL name alone: a legitimately signed application loading a library placed beside it while running from an unusual location." On the question of AI involvement it is measured rather than breathless — "SilkParasite is primarily assisted: capable humans do the engineering and lean on AI to move faster, leaving behind a few tells but none of the degradation" — with the tells being leftover test functions in the Go orchestrator, a hardcoded placeholder encryption key, a configuration field still carrying a change-me name, and a suspiciously close architectural resemblance between two implants written in different languages.

**Defender takeaway:** the targeting is Central Asian and this constituency is not in it, so the value here is the tradecraft, and specifically the detection formulation. Building the side-loading hunt as a *pairing* rather than a filename list — while remembering it is the most consistent surface rather than a universal one, so it is a high-yield hunt and not a complete net — is what makes it survive the next campaign: enumerate signed executables running from user-writable or otherwise non-standard directories, and alert where such a process loads a non-Microsoft library from its own directory. That catches all six named pairs without knowing any of them, and it keeps working when the seventh appears. Two secondary points transfer directly. A cloud-storage folder used as a bidirectional dead drop produces no attacker-controlled domain to block and terminates on a service most estates permit, so the detectable artefact is a non-browser process authenticating to a consumer cloud-storage API on a schedule — the periodicity, not the destination. And the WMI-based command execution is a reminder that a detection keyed to a shell spawning under an application parent will miss this family entirely; the equivalent signal is WMI process-creation activity originating from a process that has no business using it.

**Triage:** signed applications legitimately load libraries from their own install directory constantly, which is why the location and not the load is the discriminator — the same signed binary running from its vendor install path is normal, and running from a user profile, temporary or removable-media path is the anomaly worth an alert. For the Defender-component pair specifically, the benign twin is the real service running from its own protected directory; a copy of it running from anywhere else is not a false positive. On the network side, consumer cloud-storage and code-hosting traffic from a workstation is ordinary; the discriminators are the client identity and the rhythm — a long-lived process that is not a sync client or a browser, polling the same folder or endpoint on a fixed interval, with request and response sizes that stay small and regular.
