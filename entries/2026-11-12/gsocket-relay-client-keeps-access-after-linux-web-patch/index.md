---
schema: 1
kind: threat
title: "GSocket on compromised Linux web servers: Microsoft sees several unrelated actors install the open-source relay client after exploiting an internet-facing web application, so access outlives the patch; no inbound listener, no attacker-hosted infrastructure"
headline: "Microsoft: GSocket relay clients on exploited Linux web servers survive the patch; hunt the host, not the app"
summary: >
  Microsoft Defender telemetry shows multiple unrelated threat actors deploying GSocket, an open-source remote access tool that connects both ends outbound through a public relay, on Linux servers after exploiting an internet-facing web application, with kernel-thread-like process names and layered persistence through cron, systemd and shell profiles. Because the client runs independently of the exploited application, patching does not remove it, and blocking an address or domain is unlikely to cut off access.
discovered_at: "2026-11-12T04:06:00Z"
updated_at: null
event_date: "2026-11-11"
run_id: 2026-11-12T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities]
regions: [global]
sectors: []
entities: ["tool:gsocket"]
techniques: [T1190, T1059.004, T1105, T1219, T1090.002, T1564.001, T1222.002, T1573, T1036.011, T1053.003, T1543.002, T1546.004, T1070.006, T1070.004, T1068]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-11-11"
    role: primary
closed_sources: []
evidence:
  - quote: "Threat actors used Gsocket to maintain access even after the vulnerabilities used for initial compromise were remediated."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/"
  - quote: "Because GSocket runs independently of the exploited application, patching the vulnerability does not remove the relay client or its persistence."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/"
verification: single-source
sourcing_note: "The activity and the exposure statements are Microsoft's own Defender telemetry, and no independent source corroborates the 2026 incidents; older reports by SANS, Sansec and Elastic describe the same GSocket persistence and masquerading behaviours in other intrusions. Microsoft names no actor or cluster, says the privilege-escalation attempt with CVE-2026-43284 happened in a few incidents with no success statement, and says some outcomes were not confirmed in every case."
confidence: medium
references:
  - 2026-05-09/cve-2026-43284-cve-2026-43500-linux-dirty-frag-deterministic
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

Microsoft observed several unrelated threat actors deploy GSocket, an open-source remote access tool, on Linux servers after exploiting an internet-facing web application, and says it kept access after the exploited vulnerabilities were remediated ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)). The chain starts with command execution as a child of the web server or application runtime, where curl fetches an installation script that bash runs; the script profiles the host, picks a client matching the architecture, stages it as a hidden, executable file in a writable or memory-backed path such as /dev/shm and opens encrypted outbound command and control through the Global Socket Relay Network ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)). The client is then disguised with kernel-thread-like process names (bash exec -a), persisted through cron, systemd units, shell profiles, watchdogs and redundant copies, and the staging files are removed ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)). In a few incidents the actors afterwards attempted the Linux kernel flaw CVE-2026-43284, known as Dirty Frag, to reach root; Microsoft gives no success statement and no affected or fixed versions ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)).

Both the compromised host and the operator connect outbound to the public relay, so the host needs no inbound listener, inbound firewall rules do not see the traffic and a shared secret, not an address, pairs the endpoints, which lets the operator reconnect later from any compatible client; Microsoft therefore says that blocking an address or domain is unlikely to cut off access, while egress filtering and outbound monitoring can see it ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)). Microsoft's telemetry is concentrated on web applications and hosting; education and research and technology and telecommunications were the largest shares of affected organisations, which Microsoft says reflect exposure more likely than deliberate sector selection ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)).

**Exposure:** any Linux web, CMS or hosting server whose internet-facing application was exploited, patched or not, in the months before the patch; Microsoft says the same persistence problem applies when initial access came through remote access services or cloud shell sessions.

**Detection:** process-creation telemetry with parent lineage, where a web-server or application-runtime process starts curl and then bash, followed by a long-lived process whose name imitates a kernel thread but whose executable sits in a hidden or memory-backed path; file events in /dev/shm and /tmp; new cron entries and systemd units with plausible service names created in the same window as the download; shell startup file changes; and long-lived outbound sessions to a public relay from servers that have no reason to initiate them. After patching, remove the client, its persistence and staged files, and verify that the outbound relay connections stopped, because persistence is layered and stopping the process alone does not remove access ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)).

**Triage:** Microsoft notes that the same relay model also serves legitimate remote administration, and says a match must be judged on process ancestry, execution context, persistence changes and related network activity; a client started from a web-service process tree, from a writable or memory-backed path and under a kernel-thread-like name is the pattern it describes ([Microsoft, 2026-11-11](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)).

**Defender takeaway:** treat every Linux web server whose application was exploited as possibly holding a relay client, not only web shells, and hunt it on the host after patching; Microsoft's hardening steps are deny-by-default egress with monitoring of relay connections, non-executable mounts for temporary and memory-backed directories, and a review of cron entries, systemd units and shell startup files.
