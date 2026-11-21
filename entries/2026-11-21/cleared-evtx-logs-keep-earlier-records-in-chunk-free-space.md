---
schema: 1
kind: research
title: "Cleared Windows event logs are not empty: Arctic Wolf shows that clearing an EVTX log truncates it after the first 64 KB cluster and leaves the earlier records in that chunk's free space, where standard forensic tools do not parse or flag them, and recovered a ransomware encryptor's command line this way"
headline: "Arctic Wolf: a cleared Windows event log keeps earlier records in its first EVTX chunk; carve it"
summary: >
  Arctic Wolf incident responders report that clearing a Windows event log truncates the EVTX file after the first 64 KB cluster and resets the record numbers, but the first chunk keeps its earlier records in its free space. On a domain controller the System log held 104 allocated events after the final clear, yet the encryptor's full command line, stamped about three hours before the clear, sat inside the allocated file, and Event Viewer, EvtxECmd and Magnet AXIOM showed none of it; a PowerShell log in a second case held 44 records of which one was allocated.
discovered_at: "2026-11-21T04:50:00Z"
updated_at: null
event_date: "2026-11-20"
run_id: 2026-11-21T0355Z-intel
priority: notable
immediate_action: null
tags: [ransomware]
regions: [global]
sectors: []
entities: []
techniques: [T1685.005]
affected_products: []
cves: []
sources:
  - url: "https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/"
    publisher: "Arctic Wolf Incident Response"
    date: "2026-11-20"
    role: primary
closed_sources: []
evidence:
  - quote: "When a log is cleared, Windows truncates everything after the first 64 KB cluster and resets the first and last record numbers in the log."
    publisher: "Arctic Wolf Incident Response"
    source_url: "https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/"
  - quote: "until enough logs are generated to fill 64 KB, there will always be available data from the previous log file"
    publisher: "Arctic Wolf Incident Response"
    source_url: "https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/"
verification: single-source
sourcing_note: >
  Arctic Wolf is the only source: the findings come from two of its own incident-response cases and its own tool testing, and the claim that no forensic tool flags these records is limited to the tools it tested. The EVTX file layout is the vendor's description of the format.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Arctic Wolf's incident responders report that clearing a Windows event log does not wipe the underlying EVTX file ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)). On clearing, Windows truncates the file after the first 64 KB cluster and resets the first and last record numbers, but that first chunk keeps its earlier records in free space until enough new events fill it ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)). In a ransomware case the encryptor needed a password argument to run, and Arctic Wolf found its full command line inside the allocated System.EVTX of a domain controller, stamped about three hours before the final clear and absent from the parsed output of Event Viewer, EvtxECmd and Magnet AXIOM; another log held a netscan execution record and an attacker hostname that survived the same way ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)). In a second case a PowerShell log held 44 records of which one was allocated, all of them the same command that clears every log, which shows repeated clearing ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)). Arctic Wolf identified no forensic tool that flags records left in the slack space after a clear, and records come back with some template-held fields missing ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)).

**Detection:** the clearing itself is the alertable event, since Arctic Wolf notes that it often triggers EDR or IDS alerting and is frequently what exposes an attack in progress; the recovery step is forensic: when a log shows as cleared, acquire the EVTX file and carve its first chunk for records with earlier timestamps and lower record identifiers than the allocated ones ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)).

**Defender takeaway:** do not treat a cleared log as empty; preserve the EVTX files of affected hosts promptly, because new events overwrite the free space once they fill the first 64 KB, and search the whole file, not only the parsed events, for the encryptor's command line, tool names and hostnames ([Arctic Wolf, 2026-11-20](https://arcticwolf.com/resources/blog/windows-event-log-cleared-think-outside-the-box/)).
