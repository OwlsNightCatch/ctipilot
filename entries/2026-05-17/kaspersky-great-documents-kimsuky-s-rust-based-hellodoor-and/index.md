---
schema: 1
kind: research
title: "Kaspersky: Kimsuky adds Rust-based HelloDoor and httpMalice to its PebbleDash toolkit and takes over hosts through VSCode tunnels and DWAgent"
headline: "Kaspersky: Kimsuky's new PebbleDash backdoors hide C2 behind tunnels and take over hosts through VSCode Remote Tunnels"
summary: "Kaspersky's Securelist report of 2026-05-14 analyzes Kimsuky (APT43, Ruby Sleet) campaigns with droppers detected from August 2025 to February 2026: spear-phishing attachments disguised as documents (JSE, SCR, PIF) install the PebbleDash-family backdoors HelloDoor (Rust, early-stage, C2 behind TryCloudflare), httpMalice, the MemLoad loader and httpTroy, and the AppleSeed and HappyDoor malware. For post-exploitation the group runs a legitimate VSCode CLI tunnel authorized with its own GitHub account or deploys DWAgent tied to its account; targets are mainly South Korean, and PebbleDash also hit defense organizations in Brazil and Germany."
discovered_at: "2026-05-17T05:00:04Z"
event_date: 2026-05-14
run_id: 2026-05-17-4381863a
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - north-korea-nexus
  - identity
  - cloud
regions:
  - apac
  - dach
  - latam
sectors:
  - public-sector
  - defense
  - healthcare
entities:
  - "actor:kimsuky"
  - "campaign:kimsuky-pebbledash-hellodoor-trycloudflare-tunnel-c2-evolution"
techniques: [T1566.001, T1204.002, T1036.007, T1059.007, T1059.001, T1564.003, T1140, T1218.010, T1218.011, T1547.001, T1053.005, T1543.003, T1497.001, T1620, T1105, T1082, T1071.001, T1102.002, T1573.001, T1572, T1219, T1113, T1560, T1041, T1056.001, T1553.002]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
    publisher: "Kaspersky Securelist"
    date: "2026-05-14"
    role: primary
closed_sources: []
evidence:
  - quote: "Our monitoring indicates various strategic updates to the group’s arsenal, including the use of VSCode Tunneling, Cloudflare Quick Tunnels, DWAgent, large language models (LLMs), and the Rust programming language."
    publisher: Kaspersky Securelist
    source_url: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
  - quote: "Kimsuky obtains initial access to target systems by delivering spear-phishing emails containing malicious attachments disguised as documents."
    publisher: Kaspersky Securelist
    source_url: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
  - quote: "Since it has limited capabilities and a simplistic communication mechanism, the backdoor is most probably in the early stages of development."
    publisher: Kaspersky Securelist
    source_url: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
  - quote: "Kimsuky mainly targets South Korean entities. However, PebbleDash attacks were also seen in Brazil and Germany."
    publisher: Kaspersky Securelist
    source_url: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
verification: single-source
sourcing_note: >
  A single Kaspersky GReAT report on its own telemetry; it cites other vendors for parts of the toolset (Gen Digital on httpTroy, AhnLab on HappyDoor,
  Darktrace on the VSCode tunnel technique), but the HelloDoor and httpMalice findings are Kaspersky's alone.
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
migrated_from: briefs/2026-05-17.md
updates:
  - at: "2026-10-21T20:28:53Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Kaspersky describes httpMalice as a PebbleDash-based backdoor (HTTP or HTTPS in version 1.9, the
      Dropbox API in version 1.8), MemLoad as a loader that reflectively runs httpTroy after anti-VM
      checks, and httpTroy as the long-term access and exfiltration backdoor, rather than an HTTP-only
      loader, a reflective DLL loader and a C2 backdoor. The report gives observations, not detection
      guidance, and its targets are mainly South Korean, with PebbleDash victims including Brazilian
      defense organizations and a German defense firm. HelloDoor is an early-stage Rust backdoor whose
      TryCloudflare-hosted C2 makes its infrastructure hard to trace.
    fields: [actions, affected_products, body, classification, entities, evidence, headline, regions, sources, sourcing_note, summary, techniques, title]
---

Kaspersky's report covers Kimsuky (also APT43, Ruby Sleet) campaigns whose droppers it detected between August 2025 and February 2026: spear-phishing emails deliver compressed attachments disguised as documents, with lure names carrying a document extension before .jse or .pif ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). JSE droppers decode at least two Base64 blobs with JScript into a location such as C:\ProgramData, open the lure, then decode the payload a second time with certutil from a hidden PowerShell window and run it through regsvr32 or rundll32, while the SCR and PIF droppers decrypt theirs with XOR ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). HelloDoor, a Rust DLL backdoor first seen in August 2025 that Kaspersky judges early-stage, persists through an HKCU Run value that launches regsvr32 and talks to a C2 hosted through TryCloudflare, which makes the infrastructure behind it hard to trace; httpMalice (version 1.9 over HTTP or HTTPS, version 1.8 over the Dropbox API) persists as a service when elevated and through an HKCU Run value otherwise, profiles the host, captures the screen, uploads archived directories and encrypts its traffic with ChaCha20 ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). MemLoad runs anti-VM checks and reconnaissance, persists through scheduled tasks that run regsvr32 on its DLL every minute, and reflectively loads the RC4-encrypted httpTroy backdoor in memory for long-term access and exfiltration; the AppleSeed Spy variant collects documents, screenshots, keystrokes and the GPKI certificate directory ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).

For post-exploitation the group downloads the legitimate VSCode CLI, unpacks it into C:\Users\Public and runs code.exe tunnel, completing the GitHub device-code authorization with its own account so the host then talks to Microsoft-owned servers, or installs DWAgent from C:\ProgramData with a configuration linked to its own account; it also tunnels through Ngrok, and some samples are signed with certificates stolen from South Korean organizations ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). Targets are mainly South Korean public and private entities, and PebbleDash victims also include Brazilian defense organizations and a German defense firm ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).

**Exposure:** South Korean government bodies, AppleSeed's most frequent target, and defense, military and medical organizations, PebbleDash's focus, including defense firms abroad as in Brazil and Germany ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).

**Detection:** in process-creation telemetry, a script host running a .jse attachment that spawns a hidden PowerShell calling certutil to decode a file, followed by regsvr32 /s or rundll32 on a file in C:\ProgramData or the temp folder; in persistence artifacts, HKCU Run values or per-minute scheduled tasks named after browser checks that run regsvr32 on a DLL, and a new service whose command runs rundll32 ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). For the tunnel path, code.exe running a tunnel from C:\Users\Public after a GitHub device-code login, and DWAgent services installed from C:\ProgramData by a dropper ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).

**Triage:** VSCode Remote Tunnels and DWAgent are legitimate remote-access tools; in Kimsuky's use the VSCode CLI is unpacked into C:\Users\Public and started by a script dropper or installer rather than by the user, and DWAgent arrives with a preset configuration from a dropper that unpacks it into C:\ProgramData ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).

**Defender takeaway:** where VSCode Remote Tunnels and DWAgent are not sanctioned, alert on tunnel creation and on DWAgent service installs, because both give the attacker access that bypasses detection built for malware C2 channels ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). Organizations in Kimsuky's target set should hunt for the dropper chain and the tunnel path described above.

## Correction — 2026-10-21T20:28:53Z

httpMalice is not an HTTP-only loader but a PebbleDash-based backdoor that talks over HTTP or HTTPS in version 1.9 and through the Dropbox API in version 1.8, MemLoad is the loader that runs anti-VM checks and reconnaissance before reflectively loading httpTroy, and httpTroy is the backdoor for long-term access and data exfiltration ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). The report gives observations rather than detection guidance, so detection follows the dropper, persistence and tunnel artifacts it documents ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). HelloDoor is judged early-stage, and its TryCloudflare-hosted C2 makes its infrastructure difficult to trace; Kimsuky also tunnels through VSCode Tunneling and Ngrok ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)). Targets are mainly South Korean, AppleSeed most often government bodies and PebbleDash the defense, military and medical sectors, and PebbleDash victims also include Brazilian defense organizations and a German defense firm over several years ([Kaspersky Securelist, 2026-05-14](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)).
