---
schema: 1
kind: threat
horizon: operational
title: "XCSSET v40 turns the macOS `defaults` preference system into a fileless re-infection store and holds an exclusive lock on the XProtect signature database"
headline: "Unit 42 documents an XCSSET rebuild that lives in memory and disables macOS's own update, telemetry and signature-database channels"
summary: >
  Unit 42 published an analysis of XCSSET v40 on 2026-07-31, the macOS malware family that spreads by infecting Xcode
  projects and Git repositories so the payload executes when a developer builds the project locally. Since early April
  2026 it has spread through the Xcode projects of dozens of legitimate applications with thousands of active users.
  Version 40 keeps its core logic in memory, deletes its installation files after the memory-resident loop starts, and
  adds a fileless persistence mechanism that stores a Base64 staging payload in a per-host macOS preferences domain
  under randomised keys. It also degrades the platform's defences directly — disabling the software-update
  configuration channel, killing the cloud telemetry process, holding an exclusive file lock on the XProtect signature
  database, and resetting the TCC permission database to re-prompt a user who declines.
discovered_at: "2026-08-01T04:24:59Z"
event_date: "2026-07-31"
run_id: 2026-08-01T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, ai-abuse]
regions: [global, apac]
sectors: [technology, public-sector]
entities: [malware:xcsset]
techniques: [T1195.001, T1027, T1140, T1543.004, T1546.004, T1554, T1685, T1548.006, T1555.003, T1115, T1056.001, T1082]
affected_products: ["Apple Xcode"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-31"
    role: primary
closed_sources: []
evidence:
  - quote: "Since early April 2026, the malware has spread through supply chain attacks by hiding itself in the Xcode projects of dozens of legitimate applications with thousands of active users."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "Rather than dropping additional scripts on disk between cycles, XCSSET v40 writes a Base64-encoded staging payload into a preferences domain it generates per host."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "XCSSET v40 uses the defaults system during initial infection to store and query system information. Misusing defaults as an operational configuration cache is uncommon in the macOS malware landscape."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "The malware spawns a Perl process that tries to acquire and hold access to the endpoint's YARA-rule database (XPdb). This exclusive file lock on the XProtect signature database ensures that if the endpoint does receive a security update, its content could not be written to disk."
    publisher: "Palo Alto Networks Unit 42"
verification: single-source
sourcing_note: >
  Single-source: Unit 42 is the only party reporting this version, and every technical claim here is from its analysis.
  The family's earlier history — initial discovery by Trend Micro in 2020 and two versions documented by Microsoft in
  March and September 2025 — is as Unit 42 states it; those prior reports were not independently re-fetched this run,
  so they are attributed to Unit 42's account rather than cited directly. The South Asia targeting concentration and
  the "dozens of legitimate applications with thousands of active users" scope are Unit 42's own telemetry, with no
  independent corroboration available. Indicators from the report, including the operator infrastructure fingerprints,
  are deliberately not reproduced.
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

Unit 42 published a technical analysis of XCSSET v40 on 2026-07-31, describing a rebuild of the long-running macOS family that targets Apple-ecosystem developers. The delivery model is what makes it a supply-chain problem rather than an endpoint one: the malware injects an initial downloader script into benign project files in Xcode projects and vulnerable Git repositories, and "the endpoint infection is triggered only when the developer builds that project locally" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Unit 42 records that "since early April 2026, the malware has spread through supply chain attacks by hiding itself in the Xcode projects of dozens of legitimate applications with thousands of active users", with a heightened volume of attacks against developers across South Asia, and states the author has upgraded its worming capability so it "can now infect all existing Xcode projects on a compromised system" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)).

The execution chain is built to leave nothing behind. It runs in four stages before the final payload — a loader script that establishes command-and-control, a fingerprinting stage that pulls further modules, a temporary staging applet that loads the final stage into volatile memory, and the core module itself; once the memory-resident core loop is active "the malware terminates its staging processes and deletes all installation files from the disk" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Unit 42 identified seventeen distinct modules delivered dynamically from C2 and executed in memory, and notes that payload binaries are scrambled at compile time, "switching between nested layers of different encryption mechanisms" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Unit 42 also describes using AI and pattern-matching to reverse the multi-layered cipher shift that concealed the malware's internal function names, recovering the operator's own naming — a defensive use of the same class of tooling the report elsewhere associates with the attacker's polymorphic generation ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)).

The genuinely new tradecraft is the persistence store. Alongside its usual Git hooks, Launch Daemons and trojanised applications, v40 abuses the macOS `defaults` preference system: "rather than dropping additional scripts on disk between cycles, XCSSET v40 writes a Base64-encoded staging payload into a preferences domain it generates per host", under keys made to look random, and a one-liner run when the victim launches a trojanised or hijacked application retrieves and decodes the blob to re-infect the machine ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Unit 42 notes that while families such as NetWire and FruitFly have previously misused `defaults` to store state data, using it as an operational configuration cache "is uncommon in the macOS malware landscape" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Practically, this means the re-infection payload lives in a configuration database that most macOS triage workflows do not treat as executable content.

The defence-degradation set is unusually deliberate and is the part a responder should hunt for even without knowing the family. XCSSET v40 sets the software-update configuration channel's values to false, which Unit 42 states prevents the endpoint from automatically retrieving updates to the XProtect, MRT and TCC databases and blocks access to Apple's Rapid Security Response channel ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). It runs a constant loop that hinders the cloud telemetry process from sending security data to Apple, which the report reads as "ensuring that the operator's tooling is not sampled into subsequent XProtect signature releases" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). It belt-and-braces that with a file lock: "the malware spawns a Perl process that tries to acquire and hold access to the endpoint's YARA-rule database (XPdb). This exclusive file lock on the XProtect signature database ensures that if the endpoint does receive a security update, its content could not be written to disk" ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). And where earlier versions gave up when a user denied an automation prompt, v40 resets the user's TCC decision database for the AppleEvents service and re-presents the prompt, masquerading as System Settings or Xcode ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)).

**Defender takeaway:** for a public-sector estate the relevant exposure is not the general macOS fleet but the developer subset — anyone building iOS or macOS software in-house or through a supplier, and anyone pulling Xcode projects from public repositories. The infection is triggered by a routine local build, so the control point is what enters the developer's project tree, not what the user clicks. Unit 42's own mitigation list is behavioural: watch for abnormal AppleScript instances, monitor browser launcher paths and block unauthorised file writes there, identify and block creation and modification of abnormal local `defaults` domains, track ad-hoc-signed applications and untrusted local code signers that bypass Gatekeeper, and run automated supply-chain dependency scanning so poisoned repositories are intercepted before they reach internal pipelines ([Unit 42, 2026-07-31](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/)). Note also the second-order effect worth checking on any suspect Mac: a host whose macOS signature databases have quietly stopped updating is not merely out of date, it may be held that way.

**Triage:** `defaults write` is ordinary macOS administration and appears constantly in benign automation, so the command alone is noise. The discriminators the report supports are the shape of the data and the parent: a preferences domain that does not correspond to any installed application, holding long Base64 values under keys that follow no product's naming convention, written by a script interpreter in a build or terminal process lineage rather than by the owning application. Legitimate software writes its own domain under its bundle identifier; this writes a per-host generated one. The defence-degradation cluster gives a second, independent test that needs no attribution: software-update configuration values flipped off, the cloud telemetry process repeatedly terminated, and a long-lived Perl process holding a handle on the XProtect signature database are each individually explicable and collectively not. On the delivery side, a script interpreter spawning from an Xcode build phase, and modifications to Git hooks in repositories no one has intentionally reconfigured, are the earliest points in the chain.
