---
schema: 1
kind: threat
horizon: operational
title: "A fake Zoom installer stages Overlord RAT through the first .NET macOS downloader Jamf has observed — PE-format DLLs bundled inside a Mach-O binary"
headline: "macOS malware picks up .NET: one downloader codebase now targets Mac and Windows, and the Go payload is Garble-obfuscated to break static analysis"
summary: >
  Jamf Threat Labs analysed a counterfeit Zoom installer — a macOS ARM64 Mach-O binary named ZoomMeetings built
  as a self-contained .NET 10 single-file application, the first case Jamf has observed of .NET rather than Go or
  Rust used as a macOS downloader. Because .NET assemblies keep the Windows PE container for their bytecode even
  inside a Mach-O wrapper, one codebase targets both platforms; static analysis pulled 34 embedded PE/DLL files,
  one carrying Zoom product metadata copied from the legitimate installer. The stage-two payload is a
  Garble-obfuscated Go build of the open-source Overlord framework, reached over an encrypted WebSocket.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-06"
run_id: 2026-08-07T0411Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing]
regions: [global]
sectors: [technology, public-sector]
entities: ["tool:overlord-rat"]
techniques: [T1204.002, T1036.005, T1027, T1027.013, T1105, T1071.001, T1573, T1571, T1113, T1123, T1125, T1056.001, T1543.001, T1059.004]
affected_products: ["Apple macOS", "Microsoft Windows"]
cves: []
sources:
  - url: "https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/"
    publisher: "Jamf Threat Labs"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "The downloader is a macOS ARM64 Mach-O binary named ZoomMeetings, built as a self-contained .NET 10 single-file application with the .NET runtime bundled inside."
    publisher: "Jamf Threat Labs"
  - quote: ".NET now joins that list, with its cross-platform support enabling a single codebase to target both Windows and macOS."
    publisher: "Jamf Threat Labs"
  - quote: "The agent connects to its C2 over a secure WebSocket."
    publisher: "Jamf Threat Labs"
  - quote: "By the time anything suspicious happens on the machine, Zoom is installed and working."
    publisher: "Jamf Threat Labs"
verification: single-source
sourcing_note: >
  Single-source: Jamf Threat Labs' own static and behavioural analysis. No second party has independently
  assessed this sample, so credibility is 2 rather than 1. No file hashes, hosts or payload paths are carried
  from the source, which publishes all three. On attribution the entry follows Jamf exactly and does not
  combine its two separate similarity observations: Overlord's prior use by UNK_DeadDrop (a cluster Proofpoint
  assesses as likely North Korean, with no direct overlap to this campaign per Jamf) is one fact, and the
  LaunchAgent naming overlap with FlexibleFerret — a different, DPRK-attributed family tied to the Contagious
  Interview campaign per SentinelOne — is another. Jamf does not attribute this malware to any actor, so no
  attribution is asserted here and no relationship edge is recorded on either basis.
confidence: high
update_of: null
references: []
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

Jamf Threat Labs found a counterfeit Zoom installer that introduces a runtime macOS malware has not used before as a downloader stage. "The downloader is a macOS ARM64 Mach-O binary named ZoomMeetings, built as a self-contained .NET 10 single-file application with the .NET runtime bundled inside" ([Jamf Threat Labs, 2026-08-06](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/)). The choice is not cosmetic: recent macOS families have leaned on Go and Rust, and Jamf's point is portability — ".NET now joins that list, with its cross-platform support enabling a single codebase to target both Windows and macOS" ([Jamf Threat Labs, 2026-08-06](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/)). The structural quirk that makes it interesting to a reverser is that .NET assemblies carry their intermediate-language bytecode in the Windows PE container even when hosted inside a Mach-O wrapper, so a macOS binary here contains Windows-format executables: static analysis extracted 34 embedded PE/DLL files from the wrapper. One of them carries plaintext Zoom product-metadata strings lifted from the legitimate installer so casual inspection reads as genuine, while the malicious DLL's method, field and string-table names are obfuscated into generated identifiers.

Execution writes a stage-two binary into a temporary directory and launches it backgrounded and detached from the terminal session, so the payload outlives the installer. It then does the thing that makes this hard to triage. Jamf: "Concurrently, it fetches the real Zoom installer to maintain the lure. On macOS it downloads the .pkg; on Windows the .exe" — retrieved from Zoom's own download host — with the consequence that "By the time anything suspicious happens on the machine, Zoom is installed and working" ([Jamf Threat Labs, 2026-08-06](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/)). A user who checks whether they actually got Zoom will find that they did. That second stage is a Go build of Overlord, an openly available remote-access framework, compiled with Garble — which mangles the function, type and package names in Go's `pclntab` and obfuscates the `moduledata` structure that analysis tooling uses to locate them, breaking the standard Go reverse-engineering workflow that normally recovers a Go binary's symbol layout for free. "The agent connects to its C2 over a secure WebSocket" ([Jamf Threat Labs, 2026-08-06](https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/)), reaching a Zoom-branded lookalike host on a non-standard port. Overlord's capability set is broad — keylogging, screen, audio and webcam capture, filesystem access and arbitrary script execution — with optional LaunchAgent persistence. Jamf sets out two separate points of similarity and declines to draw a conclusion from either. Overlord was also used by UNK_DeadDrop, a cluster Proofpoint assesses as likely North Korean, though Jamf states no direct overlap has been identified between that activity and this campaign; and this Overlord variant shares its LaunchAgent label and plist name with FlexibleFerret, a DPRK-attributed macOS family associated with the Contagious Interview campaign and documented by SentinelOne in February 2025. Jamf's own position is that it has noted the similarities but does not currently attribute this malware to a specific threat actor, and the initial delivery vector remains under investigation — so on the evidence published this is an unattributed campaign reusing a public tool, and the DPRK-adjacent context is a naming and tooling overlap rather than an attribution.

**Defender takeaway:** two of this chain's properties defeat controls that usually work, and both are checkable. The `.NET`-in-Mach-O structure means a macOS binary that embeds dozens of PE files is itself anomalous — a legitimate self-contained .NET macOS application looks structurally similar, so the discriminating detail Jamf supplies is that the bundled DLL's only plaintext strings imitate a *different* vendor's product metadata. And Garble means that recovering the payload's logic will not come cheap: teams that rely on Go symbol recovery should expect that workflow to fail on this family and plan for behavioural analysis in a detonation environment instead. Detection concepts, telemetry class first: in process-creation telemetry with parent lineage, the sequence to alert on is an installer-named process writing an executable into a temporary directory and launching it detached, which is not something a real Zoom installation does; in egress telemetry, an outbound WebSocket to a non-standard port from a freshly installed conferencing application is the hunt trigger; endpoint policy that blocks execution from temporary directories removes the staging step outright. **Triage:** a working Zoom install is not evidence of benignity here, because the downloader fetches and installs the genuine client alongside its payload — so "the application the user expected is present and functional" must be treated as consistent with compromise rather than as a clear. Legitimate conferencing clients also connect out over TLS immediately after installation, so egress alone is not the signal either. The discriminators are the temporary-directory staging and the detached second process, the non-standard destination port, and the destination host's age and resemblance to the vendor's real domain; the staging step is the least ambiguous, since a genuine installer places its binaries in an application directory rather than running one from a scratch path.
