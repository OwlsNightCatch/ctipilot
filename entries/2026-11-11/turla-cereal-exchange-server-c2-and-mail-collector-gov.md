---
schema: 1
kind: threat
title: "Turla's Cereal toolset turns a compromised on-premises Exchange server into the command channel and mail collector at Kazakh and Romanian government bodies, with no attacker infrastructure and no new transport agent registered (ESET)"
headline: "ESET: Turla's Cereal runs the victim's own Exchange server as C2 and wraps transport agents to collect mail"
summary: >
  ESET found a previously undocumented .NET toolset, Cereal, on a Kazakh government organisation's Exchange server in November 2025 and on a Romanian government organisation's from December 2025, and attributes it to Turla with high confidence. The compromised Exchange server is the command channel, answering requests on web paths that imitate Outlook Web Access, Autodiscover and ActiveSync, and a module injected into the transport service wraps existing transport agents to collect mail, in Romania configured to select messages to or from NATO and EU addresses; ESET could not determine the initial access method.
discovered_at: "2026-11-11T03:40:30Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, russia-nexus]
regions: [europe, russia-cis]
sectors: [public-sector]
entities: ["actor:secretblizzard", "malware:cereal"]
techniques: [T1505.002, T1574.001, T1055.001, T1620, T1027.009, T1140, T1070.004, T1003.004, T1114.002, T1119, T1560.002, T1087.002, T1069.002, T1047, T1071.001, T1573.001, T1041, T1036.005]
affected_products: ["Microsoft Exchange Server"]
cves: []
sources:
  - url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
    publisher: "ESET Research (WeLiveSecurity)"
    date: "2026-11-10"
    role: primary
  - url: "https://web-assets.esetstatic.com/wls/en/papers/white-papers/turla-cereal-tricks.pdf"
    publisher: "ESET Research (white paper)"
    date: "2026-11-10"
    role: primary
closed_sources: []
evidence:
  - quote: "Instead – adding insult to injury – the victim’s compromised Exchange server is co-opted to act as the C&C infrastructure."
    publisher: "ESET Research"
    source_url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
  - quote: "We attribute Cereal, with high confidence, to the Russia-aligned APT group Turla, based on the concurrent use of another component publicly linked to Turla and conceptual similarities to older Turla malware."
    publisher: "ESET Research"
    source_url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
  - quote: "Once inside, CerealBox accesses Exchange’s internal structures, finds the existing transport agents, and wraps their handlers with malicious code."
    publisher: "ESET Research"
    source_url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
  - quote: "No new agent appears anywhere in Exchange’s configuration."
    publisher: "ESET Research"
    source_url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
  - quote: "it was configured to identify emails sent to, or received from, The North Atlantic Treaty Organization (NATO) and European Union (EU)."
    publisher: "ESET Research"
    source_url: "https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/"
verification: single-source
sourcing_note: >
  ESET is the telemetry holder and first-hand discoverer, in its blog post and white paper; the outlets that rewrote the post add no observation of their own. ESET could not determine the initial access method and names no affected Exchange version or vulnerability, though it considers exploitation of a vulnerability on the internet-reachable servers possible. The Detection line's integrity checks on the Exchange host follow from the described mechanism rather than from an ESET statement.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every internet-facing Exchange server, compare ncobjapi.dll and wbemcomn.dll in C:\\Windows\\System32\\wbem\\ and the Microsoft.Exchange .ni.dll files in the .NET native image cache with the Microsoft originals and list the non-Microsoft assemblies loaded into EdgeTransport.exe, because ESET places the Cereal loader at those locations and Get-TransportAgent shows nothing new."
updates: []
migrated_from: null
---

ESET found a previously undocumented .NET toolset, Cereal, on a Kazakh government organisation's Exchange server on 2025-11-28 and, after tuning its detections, on a Romanian government organisation's Exchange server compromised from 2025-12-23; in Romania the mail-collection module was configured to identify messages to or from NATO and EU institutional addresses ([ESET Research, 2026-11-10](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)). ESET attributes Cereal to Turla with high confidence, on the concurrent use of another component publicly linked to Turla and conceptual similarity to older Turla malware, and could not determine the initial access method, although it considers a vulnerability exploit possible because the servers are reachable from the internet ([ESET Research, 2026-11-10](https://web-assets.esetstatic.com/wls/en/papers/white-papers/turla-cereal-tricks.pdf)).

The command channel is the victim's own Exchange server. CerealNeuron runs on the compromised server and passively waits for requests on web paths made to look like Outlook Web Access, Autodiscover and ActiveSync traffic; a correctly encrypted request is treated as a command and a bad one gets a normal-looking Exchange error page, and ESET found no operator-controlled server and could not identify ingress addresses ([ESET Research, 2026-11-10](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)). CerealHermit is a network-less variant that reads encrypted command files from disk, and each task runs as a small .NET assembly inside a CerealRunner (mailbox retrieval, Active Directory and WMI queries, LSA secrets extraction, file operations) ([ESET Research, 2026-11-10](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)). CerealLoader, the only component written to disk in recognisable .NET form, abuses .NET VTable fixups so native code runs before managed code and is placed where trusted processes load it: the System32 wbem directory (ncobjapi.dll, wbemcomn.dll, loaded by WMI) and the .NET native image cache ([ESET Research, 2026-11-10](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)). CerealBox, injected into EdgeTransport.exe, wraps the handlers of transport agents already loaded, so "no new agent appears anywhere in Exchange's configuration"; it keeps messages with .doc, .docx or .pdf attachments that match hard-coded sender, recipient, subject or attachment-name lists and stages them compressed and encrypted on disk for exfiltration through CerealNeuron ([ESET Research, 2026-11-10](https://www.welivesecurity.com/en/eset-research/exchange-for-breakfast-turlas-cereal-tricks-are-not-for-kids/)).

**Exposure:** any organisation that runs Microsoft Exchange on premises with a role reachable from the internet; ESET names no vulnerable version, so exposure is the deployment model.

**Detection:** file-integrity telemetry on the Exchange host for DLLs in the System32 wbem directory and .NET native image cache files that do not match the Microsoft originals; module telemetry for non-Microsoft assemblies loaded into EdgeTransport.exe while Get-TransportAgent lists nothing new; web-server logs for requests to the Outlook Web Access, Autodiscover and ActiveSync look-alike paths from clients with no matching mailbox flow, whose encrypted bodies return a generic error page; and Exchange Web Services mailbox retrievals made from the server's own context. With no external C2 and no known entry vector, the check is a compromise assessment of every internet-facing Exchange server.

**Triage:** third-party anti-spam, data-loss-prevention and archiving products also inject into the transport service, but they are vendor-signed and appear in the transport-agent configuration, which CerealBox does not; the native image cache regenerates legitimately after .NET updates, so a changed timestamp alone is weak, while a file that does not match the Microsoft binary is the signal.

**Defender takeaway:** treat internet-facing Exchange servers as top-tier assets with endpoint detection and restricted egress, baseline the wbem directory and the native image cache, and run the compromise assessment now, because network-only detection will not find a channel that rides the victim's own web paths.
