---
schema: 1
kind: research
title: "BigDiskBuster: a roughly 300-line Windows proof of concept keeps Microsoft Defender from updating by claiming all free disk space, with no CVE and no patch"
headline: "A Defender bypass that needs no vulnerability: fill the disk during every update and the engine stays up, stale"
summary: >
  LevelBlue SpiderLabs reproduced BigDiskBuster, a proof of concept published on GitHub on 2026-09-19 by the actor
  known as MSNightmare, which watches the C: volume for Defender update activity and claims the free space so each
  update fails while the Defender service keeps running and real-time protection stays on. It runs from a standard
  account and has no CVE or patch; Microsoft says Defender Antivirus detects the proof of concept, and no use in
  attacks is reported.
discovered_at: "2026-10-08T04:54:00Z"
updated_at: null
event_date: "2026-10-05"
run_id: 2026-10-08T0404Z-intel
priority: notable
immediate_action: null
tags: [poc-public]
regions: [global]
sectors: []
entities: ["actor:nightmare-eclipse", "product:microsoft-defender-antivirus"]
techniques: [T1685, T1106, T1564.001]
affected_products: ["Microsoft Defender Antivirus"]
cves: []
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands"
    publisher: "LevelBlue SpiderLabs"
    date: "2026-10-05"
    role: primary
  - url: "https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates"
    publisher: "Dark Reading"
    date: "2026-10-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "At the time of publication, BigDiskBuster has no assigned CVE, available patch, or Microsoft advisory."
    publisher: "LevelBlue SpiderLabs"
  - quote: "a Microsoft spokesperson tells Dark Reading that Microsoft Defender Antivirus includes detections and preventions against the PoC"
    publisher: "Dark Reading"
  - quote: "a process holding both of these handles simultaneously has no ordinary reason to exist on a stock Windows endpoint"
    publisher: "LevelBlue SpiderLabs"
verification: multi-source
sourcing_note: >
  LevelBlue reproduced the proof of concept in its own lab and is the only source of the technical detail; Dark
  Reading restates it and adds Microsoft's statement and LevelBlue's description of the test environment. The
  GitHub repository has been taken down, and no source reports use in an attack.
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

LevelBlue SpiderLabs reproduced BigDiskBuster, a proof of concept published on GitHub on 2026-09-19 by the actor known as MSNightmare (Nightmare Eclipse) that needs no vulnerability to keep Microsoft Defender from updating ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)). It watches the C: volume for Defender update activity and, when an update begins, creates a hidden file whose allocation claims essentially all free space; the update runs out of room and fails, Defender cleans up its staging directory and the tool repeats the process on the next attempt ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)). The Defender service keeps running and real-time protection stays on; in LevelBlue's lab no alert appeared, and the only visible artifact was a stale security-intelligence version and the generic update error 0x80070643 ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)). The roughly 300 lines of C++ use no memory corruption or kernel component: a raw handle on the volume device, a file opened relative to that handle, a recursive watch of the volume and an oversized allocation, with the file hidden and deleted on close ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)). It ran under a standard user account on a default Defender installation ([Dark Reading, 2026-10-06](https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates)).

No CVE, patch or Microsoft advisory exists; a Microsoft spokesperson told Dark Reading that Defender Antivirus includes detections and preventions against the proof of concept and that customers should keep security intelligence and platform updates current ([Dark Reading, 2026-10-06](https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates)). The GitHub repository has been taken down, and Dark Reading notes that the technique could in theory extend the life of malicious tooling already on a machine by withholding new detections ([Dark Reading, 2026-10-06](https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates)). No source reports use in an attack.

**Exposure:** Windows endpoints running Defender Antivirus; it ran under a standard user account in LevelBlue's testing ([Dark Reading, 2026-10-06](https://www.darkreading.com/application-security/bigdiskbuster-microsoft-defender-running-blocking-updates)), and an estate shows the effect as endpoints whose security-intelligence age keeps growing ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)).

**Detection:** monitor whether Defender's content is staying current rather than whether the service runs: repeated update failures with error 0x80070643 and no installer activity, and an abrupt drop of free space on the system volume while the update chain (platform update, signature stub, recovery) runs and fails ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)). In endpoint file-handle or ETW telemetry, a non-Defender, non-TrustedInstaller process holding a handle on MRT.exe is a high-confidence signal, and the same process also holding a raw handle on the volume device is rated critical; short-lived hidden GUID-named files in the user temp directory during update failures corroborate it ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)).

**Triage:** a handle on the volume device alone is low-specificity because svchost, SearchIndexer, dllhost and TiWorker hold the same kind of handle in normal operation; in LevelBlue's tested environment only the Defender service processes and TrustedInstaller legitimately held a handle on MRT.exe ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)).

**Defender takeaway:** add an alert on Defender security-intelligence age and on repeated update failures, since a running service no longer proves current protection, and keep the handle correlation as the hunt for a process that is actively doing it ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands)).
