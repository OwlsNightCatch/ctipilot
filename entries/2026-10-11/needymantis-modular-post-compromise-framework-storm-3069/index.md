---
schema: 1
kind: threat
title: "NeedyMantis: Microsoft details a modular post-compromise framework, found through the DAEMON Tools compromise, used against telecoms, universities, intergovernmental bodies and government contractors"
headline: "Microsoft: a China-aligned implant hides in legitimate software via DLL sideloading and takes modules over WebSockets"
summary: >
  Microsoft Threat Intelligence describes NeedyMantis, a modular post-compromise malware framework used since at
  least October 2025 in a limited number of targeted intrusions at telecommunications organizations, universities,
  medical nonprofits, intergovernmental organizations and government contractors. It is deployed after access exists,
  sideloaded as a DLL beside legitimate software, and loads further modules over a WebSocket channel. Storm-3069,
  Microsoft's designator for the DAEMON Tools supply-chain activity, is one operator; Microsoft assesses Storm-3069's
  activity originates from China without attributing it to a nation-state actor, and has not determined whether one
  operator is behind all NeedyMantis activity.
discovered_at: "2026-10-11T14:59:25Z"
updated_at: null
event_date: "2026-09-28"
run_id: 2026-10-11T1307Z-audit
priority: notable
immediate_action: null
tags: [china-nexus]
regions: [global]
sectors: [telco, education, public-sector]
entities: ["malware:needymantis", "actor:storm-3069", "incident:daemon-tools-supply-chain-2026"]
techniques: [T1570, T1574.001, T1036.005, T1027, T1622, T1082, T1057, T1083, T1071.001, T1573.001]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-09-28"
    role: primary
closed_sources: []
evidence:
  - quote: "Microsoft Threat Intelligence has identified NeedyMantis, a modular post-compromise malware family observed in a limited number of targeted operations affecting telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/"
  - quote: "While Microsoft assesses the activity originates from China, it has not attributed Storm-3069 to a Chinese nation-state actor."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/"
  - quote: "Microsoft has not observed NeedyMantis itself being distributed through a supply chain compromise."
    publisher: "Microsoft Threat Intelligence"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/"
verification: single-source
sourcing_note: >
  Microsoft Threat Intelligence is the only analyst of the malware; it found NeedyMantis by pivoting from Kaspersky's
  DAEMON Tools indicators. The China-origin assessment and the operator link are Microsoft's own.
confidence: medium
references:
  - 2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed
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

Microsoft Threat Intelligence published its analysis of NeedyMantis on 2026-09-28: a modular post-compromise malware family seen since at least October 2025 in a limited number of targeted operations against telecommunications organizations, universities, medical nonprofits, intergovernmental organizations and government contractors ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)). Microsoft found it by pivoting from indicators in Kaspersky's investigation of the DAEMON Tools supply-chain compromise and names Storm-3069, its designator for that activity, as at least one operator; it has seen further NeedyMantis activity beyond Storm-3069 that aligns with activity it associates with China-based actors, has not determined whether one actor is behind all of it, and assesses that Storm-3069's activity originates from China without attributing it to a Chinese nation-state actor ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)). Microsoft has not seen NeedyMantis itself delivered through a supply chain; it is deployed after the operator already has access, and in one intrusion the operator used Impacket to copy the legitimate application, the malicious DLL and an encrypted archive from a network share and run them ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)).

The first-stage loader is a DLL sideloaded by the legitimate program it ships with, in the analysed case a fake WinSparkle update component of the Poedit translation tool, with other pairings built on curl, Vim and TightVNC and DLLs masquerading as Microsoft Office, Broadcom, Intel and NVIDIA components under ProgramData and Program Files ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)). It hides its strings and constants, checks for debuggers, and extracts a second-stage shellcode loader from a custom encrypted archive that in turn unpacks the main component ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)). The main component reads its configuration from a file named after a Windows networking library, beacons with an HTTPS GET request whose cookie carries the computer name, user name, process list and Program Files listing, then switches to WebSockets with a binary protocol encrypted with RC4 after a key exchange; its handful of commands chiefly load, unload and pass data to further modules, whose capabilities Microsoft has not confirmed ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)).

**Detection:** in image-load telemetry, a legitimate application such as Poedit, curl, Vim or TightVNC loading a same-named DLL from an unusual ProgramData or Program Files folder, next to an extension-less archive with the DLL's name; in network telemetry, an HTTPS request whose cookie carries Base64-encoded compressed system information followed by a WebSocket upgrade from that process; and in process telemetry, Impacket-style remote execution that stages such a bundle from a network share ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)).

**Triage:** these tools legitimately load their own DLLs, and in the analysed case the malicious DLL replaced Poedit's own WinSparkle update component in its normal install folder, so the location alone does not decide it; the discriminator is the companion extension-less archive named like the DLL, which a genuine installation does not carry, together with a DLL that differs from the vendor's original component, and for the ProgramData pairings an application folder the organization never deployed ([Microsoft Threat Intelligence, 2026-09-28](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)).

**Defender takeaway:** NeedyMantis is a second-stage foothold, so a hit means an intrusion is already under way; organizations that ran an affected DAEMON Tools Lite build or that support intergovernmental bodies as contractors should hunt for the sideloading pattern rather than wait for an initial-access alert.
