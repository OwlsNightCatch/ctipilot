---
schema: 1
kind: threat
title: "NIK C2: Talos documents a Go Windows implant that sends operator prompts to the OpenAI API from the infected host and falls back to the victim's own API key"
headline: "Talos: NIK C2 implant calls the OpenAI API from the victim host and bills the victim's own key if none is given"
summary: >
  Cisco Talos describes NIK C2, a command-and-control framework seen with a live server, whose Go implant for Windows has more than 52
  commands and an ai_generate command that builds an OpenAI Chat Completions request on the infected host from an operator prompt. If the
  operator supplies no key the implant reads the OPENAI_API_KEY environment variable, so OpenAI bills and logs the victim's key; Talos names no
  victims, sector or initial-access method.
discovered_at: "2026-11-02T03:46:30Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-11-02T0256Z-intel
priority: routine
immediate_action: null
tags: [ai-abuse, infostealer]
regions: [global]
sectors: []
entities: ["malware:nik-c2", "product:openai-api"]
techniques: [T1071.001, T1573.001, T1056.001, T1113, T1125, T1123, T1115, T1555.003, T1021.005, T1563.002, T1090, T1055.012, T1685, T1548.002, T1036.005, T1547.001, T1546.015, T1588.007, T1059.001, T1218.005, T1041, T1622, T1539, T1518.001, T1082, T1057]
affected_products: ["Microsoft Windows", "OpenAI API"]
cves: []
sources:
  - url: "https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/"
    publisher: "Cisco Talos"
    date: "2026-10-29"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/nik-c2-malware-victims-openai-keys/"
    publisher: "Infosecurity Magazine"
    date: "2026-10-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "allowing operators to route arbitrary prompts to the OpenAI Chat Completions API directly through the infected host"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/"
  - quote: "OpenAI's billing system will charge the victim's payment method, and OpenAI's access logs will show the victim's API key as the one that made the requests"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/"
  - quote: "It does not encrypt any files, which means it leaves no forensic trail of file modification timestamps or encryption markers"
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/"
verification: single-source
sourcing_note: >
  Cisco Talos is the only party that analysed the framework; Infosecurity Magazine restates the Talos post and adds no observation of its own.
  Talos observed the framework hosted on a server during its research and assesses with moderate confidence that the framework is functional rather than a proof of
  concept; the post names no victims, sector, actor or delivery method.
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

Cisco Talos found a command-and-control framework it calls NIK C2, with a live server, whose 64-bit Go implant for Windows takes more than 52 commands: browser and Wi-Fi credential theft, keylogging, screen, camera, microphone and clipboard capture, hidden VNC, RDP session interaction, an embedded SOCKS5 and HTTP proxy with a reverse tunnel for lateral movement, AMSI patching, UAC bypass and process hollowing ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)). It talks to its server over TLS WebSockets on port 443 with an HTTP polling fallback about every 250 milliseconds under AES-256-GCM, persists through registry Run keys and COM hijacking, masquerades under a system-process name such as svchost.exe and runs a watchdog process ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)). The new part is the `ai_generate` command: the implant builds an OpenAI Chat Completions request from an operator prompt on the infected host, posts it to OpenAI from the victim's address and returns the answer to the panel; if the operator gives no key it reads the `OPENAI_API_KEY` environment variable, so OpenAI charges the victim's payment method and its logs show the victim's key ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/); [Infosecurity Magazine, 2026-10-29](https://www.infosecurity-magazine.com/news/nik-c2-malware-victims-openai-keys/)). A screen-locking ransomware module encrypts no files: PowerShell copies the boot sector to a temporary file, and a looping batch file reopens a lock page shown through mshta.exe ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)). Talos sees at least three implant versions and assesses with moderate confidence that the framework is functional; its post names no victims, sector or delivery method ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)).

**Exposure:** Windows hosts; the post gives no initial-access method, so exposure cannot be read from an estate's configuration. A host that holds an `OPENAI_API_KEY` in its environment lends that key to the operator.

**Detection:** in egress and proxy telemetry, requests to the OpenAI API from a process that is not a sanctioned AI client, in particular a process named like a system binary such as svchost.exe that runs from the user's Roaming Microsoft Network folder, the install location the post describes; in process and registry telemetry, the fodhelper.exe UAC-bypass pattern (a command written under the ms-settings shell key and removed within seconds), an AMSI patch in a PowerShell session and, from the lock-screen module, a Run key that launches a looping batch file ([Cisco Talos, 2026-10-29](https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/)); on the OpenAI side, usage or billing under a key the owner did not use.

**Defender takeaway:** add the OpenAI API (and other LLM endpoints) to the list of destinations that only sanctioned clients may reach, and rotate any OpenAI key found on a host where this framework ran, because the implant bills and logs it as the victim's own.
