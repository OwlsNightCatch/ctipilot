---
schema: 1
kind: threat
title: "Flooding Dropper: 846 npm packages published from disposable accounts, with a dropper that falls back to DNS TXT records when its download hosts are blocked"
headline: "An npm campaign built for attrition — throwaway publisher accounts, per-package payload variation, and a DNS fallback that survives host blocking"
summary: >
  Sonatype Research Labs is tracking Flooding Dropper, an active npm campaign spanning 846 components published
  across many automatically generated accounts rather than one prolific publisher. The install-time loader
  selects a Windows, Linux or macOS payload, tries a randomised set of hardcoded download hosts, and falls back
  to reassembling the binary from DNS TXT records when HTTPS fails — then launches it as a detached background
  process that outlives the npm install. The Windows second stage patches ETW and AMSI, checks for analysis
  environments, persists via both a Run key and a scheduled task, and reflectively executes an encrypted payload
  in memory. Sonatype's guidance is to treat an affected host as compromised.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-05"
run_id: 2026-08-07T0411Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, vulnerabilities]
regions: [global]
sectors: [technology, public-sector, finance]
entities: ["campaign:flooding-dropper-npm-2026-08"]
techniques: [T1195.002, T1059.007, T1071.004, T1105, T1027, T1685, T1497.001, T1547.001, T1053.005, T1620]
affected_products: ["npm"]
cves: []
sources:
  - url: "https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages"
    publisher: "Sonatype Research Labs"
    date: "2026-08-05"
    role: primary
closed_sources: []
evidence:
  - quote: "Launching the payload in a detached process is an important failsafe because killing the npm installation process or parent Node.js process does not necessarily stop the attack."
    publisher: "Sonatype Research Labs"
  - quote: "Impacted organizations should consider the host compromised, remove the package, investigate secondary payload execution and persistence, and rotate exposed credentials only after the environment has been cleaned."
    publisher: "Sonatype Research Labs"
verification: single-source
sourcing_note: >
  Single-source: Sonatype Research Labs' own analysis, which credits researchers at OpenSourceMalware with
  first reporting one package in the set on 2026-08-05 before Sonatype identified the wider campaign. No second
  party has independently assessed the campaign, so credibility is 2 rather than 1. Sonatype describes the
  Windows second-stage behaviour as initial analysis. Published 2026-08-05, inside the 72-hour developing-story
  window rather than the 26-hour default: Sonatype states the campaign is active and that its naming convention
  is already evolving.
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
actions:
  - "Pull the affected package list from Sonatype's tracking record for this campaign, sonatype-2026-005660, then search build logs, lockfiles, dependency caches, container layers and internal npm mirrors for any install of one — and treat a host that installed one as compromised rather than cleaned."
migrated_from: null
---

Sonatype Research Labs is tracking an active npm campaign it calls Flooding Dropper, spanning 846 components at the time of publication, after researchers at OpenSourceMalware reported one package in the set on 2026-08-05 ([Sonatype Research Labs, 2026-08-05](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)). The distribution model is the point: instead of one prolific publisher, the operator appears to automate npm account and package creation, publishing a handful of packages from each of many accounts with names that interpolate a small set of recurring terms and version numbers clustered in one range. Sonatype is explicit that these naming characteristics are a correlation aid rather than a control — they help group today's packages and will change — and this entry deliberately carries the shape of the convention rather than package names.

The first-stage JavaScript runs at install or import time and behaves as a cross-platform loader with more than one way to succeed. It checks environment variables and local state markers to decide whether to run at all, identifies the host operating system and processor architecture to select a matching Windows, Linux or macOS payload, and attempts the download from a randomised set of hardcoded hosts. When those HTTPS fetches fail it falls back to DNS: the payload is reassembled and decoded from TXT-record responses, so blocking a download host does not prevent delivery. The binary is then written to a temporary directory, marked executable on Unix-like systems, and launched detached with output suppressed — and Sonatype spells out why that matters operationally: "Launching the payload in a detached process is an important failsafe because killing the npm installation process or parent Node.js process does not necessarily stop the attack" ([Sonatype Research Labs, 2026-08-05](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)). Killing the build does not kill the intrusion.

Sonatype's initial analysis of the Windows second stage finds another loader rather than a final payload: it patches Event Tracing for Windows and Antimalware Scan Interface functions to interfere with monitoring and scanning, checks for debuggers, virtual machines, sandboxes and security products, copies itself to a persistent location under the user's AppData directory, establishes persistence through both a Registry Run key and a scheduled task, then downloads an encrypted payload, decrypts it and executes it reflectively in memory so nothing conventional is written to disk for a disk-focused control to catch ([Sonatype Research Labs, 2026-08-05](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)). Sonatype classifies the affected packages under CWE-506 at CVSS 8.7 and tracks the campaign as sonatype-2026-005660, which is the handle to pull the current package list from rather than any naming heuristic. The packages also carry slightly modified payloads — syntactically different, functionally identical, with renamed URL functions and variables — which is aimed squarely at signature matching rather than at behavioural detection.

**Defender takeaway:** the remediation order is the actionable content, because removing the dependency is the step that feels like the fix and is not. Sonatype's own guidance is that "impacted organizations should consider the host compromised, remove the package, investigate secondary payload execution and persistence, and rotate exposed credentials only after the environment has been cleaned" ([Sonatype Research Labs, 2026-08-05](https://www.sonatype.com/blog/flooding-dropper-hits-npm-with-850-malicious-packages)) — rotating credentials into a still-compromised host just hands over the new ones. Detection concepts, telemetry class first: in process-creation telemetry with parent lineage, a detached child process surviving after an `npm`/`node` parent tree exits, especially one executing from a temporary directory, is the first-stage signature; in DNS telemetry, a burst of TXT-record queries from a build agent or developer workstation is what the fallback channel looks like, and TXT volume from a host that has no reason to query it is more tractable than blocking the answer; on Windows, ETW provider tampering and AMSI patching in the same process that then schedules a task and writes a Run key is the second-stage sequence. Scope the search across developer workstations, CI/CD runners and build agents, internal registries and caches, and container layers, since a retained copy in a mirror re-infects after cleanup. **Triage:** build tooling legitimately spawns child processes from `node` trees and legitimately writes to temporary directories, so neither is the signal alone — the discriminators are a child process that *persists after the install completes*, TXT-record queries from a host whose workload never uses them, and a process that both disables telemetry interfaces and installs two independent persistence mechanisms; the ETW/AMSI patching is the least ambiguous of the three.
