---
schema: 1
kind: threat
title: "DAEMON Tools Lite supply-chain compromise: signed installers deliver a profiler worldwide, with a backdoor and QUIC RAT reserved for a dozen targets in Russia, Belarus and Thailand"
headline: "Trojanised, validly signed DAEMON Tools installers ran a profiler on thousands of machines and a backdoor on about a dozen machines"
summary: >
  DAEMON Tools Lite versions 12.5.0.2421 to 12.5.0.2434, distributed from the vendor's site from
  2026-04-08 and signed with the developer's certificates, carried trojanised helper binaries. Kaspersky saw
  several thousand infection attempts in more than 100 countries, mostly delivering an information collector;
  a backdoor reached about a dozen machines at government, scientific, manufacturing and retail organizations in Russia,
  Belarus and Thailand, and QUIC RAT one Russian educational institution. Version 12.6.0.2445 no longer includes the malicious behaviour Kaspersky describes.
discovered_at: "2026-05-09T05:00:00Z"
event_date: "2026-05-05"
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - supply-chain
regions:
  - global
sectors: []
entities:
  - "incident:daemon-tools-supply-chain-2026"
cves: []
sources:
  - url: "https://securelist.com/tr/daemon-tools-backdoor/119654/"
    publisher: "Kaspersky Securelist"
    date: "2026-05-05"
    role: primary
  - url: "https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/"
    publisher: "Kaspersky blog"
    date: "2026-05-05"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/06/daemon-tools-compromised-backdoors-supply-chain-attack/"
    publisher: "Help Net Security"
    date: "2026-05-06"
    role: corroborating
  - url: "https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack"
    publisher: "The Record"
    date: "2026-05-06"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
affected_products: ["DAEMON Tools Lite"]
techniques: [T1195.002, T1059.001, T1105, T1082, T1055, T1071]
classification:
  reliability: B
  credibility: 2
migrated_from: briefs/2026-05-09.md
updates:
  - at: "2026-10-11T14:29:53Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The headline victimology was wrong: no EU government victim is reported; EU countries appear only among infection attempts, the backdoor reached about a dozen machines in Russia, Belarus and Thailand, and QUIC RAT one educational institution in Russia. Kaspersky does not describe keylogging, SOCKS proxying or tunnelling for QUIC RAT, does not attribute the attack, and calls the intent unclear; the Linux masquerade and asymmetric-cryptography mappings had no source. The Securelist report becomes the primary source, the espionage and China-nexus tags are removed, and the entry gains a rating and a supported ATT&CK mapping. Priority moves from high to notable. The startup behaviour and the Detection line now lead with the backdoor's beacon to a typosquatted vendor domain, which precedes any cmd.exe execution.
    fields: [title, headline, summary, event_date, priority, tags, regions, sectors, affected_products, techniques, sources, classification, body]
---

Kaspersky found that DAEMON Tools installers distributed from the product's legitimate website and signed with the developer's certificates had been trojanised from 2026-04-08: in versions 12.5.0.2421 to 12.5.0.2434 the helper binaries `DTHelper.exe`, `DiscSoftBusServiceLite.exe` and `DTShellHlp.exe`, signed by AVB Disc Soft, were compromised, and version 12.6.0.2445 no longer contains the malicious behaviour ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). At startup the trojanised binaries activate a backdoor that sends GET requests to a domain typosquatting the vendor's download site; when the server replies with a shell command, it runs through `cmd.exe`, which in the observed cases ran PowerShell to download an executable into `C:\Windows\Temp` and execute it, the first payload being a .NET information collector ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). Kaspersky saw several thousand infection attempts in more than 100 countries, 10% of the affected systems belonging to organizations, and most received only the information collector ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). A minimalistic backdoor reached about a dozen machines of government, scientific, manufacturing and retail organizations in Russia, Belarus and Thailand, and was used to deploy QUIC RAT against one organization, an educational institution in Russia; QUIC RAT supports HTTP, UDP, TCP, WSS, QUIC, DNS and HTTP/3 for command and control and can inject payloads into `notepad.exe` and `conhost.exe` ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). Chinese strings in the collector may imply a Chinese-speaking actor, but Kaspersky does not attribute the compromise, and whether the intent is espionage or big-game hunting is unclear ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). The developer says only the free Lite edition was affected ([The Record, 2026-05-06](https://therecord.media/hackers-compromise-daemon-tools-global-supply-chain-attack)).

**Exposure:** endpoints that installed or updated DAEMON Tools Lite to a version from 12.5.0.2421 to 12.5.0.2434 from 2026-04-08 onward ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)).

**Detection:** in DNS and proxy telemetry, a DAEMON Tools binary beaconing at startup to a lookalike of the vendor's download domain is the earliest signal; in process telemetry, the same binary spawning `cmd.exe` and then PowerShell that downloads a file into `C:\Windows\Temp` and executes it follows when the server issues a command ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). Injection into `notepad.exe` or `conhost.exe` shortly after such a chain points to QUIC RAT ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)).

**Defender takeaway:** a validly signed installer from the vendor's own site was the delivery vehicle, so code-signing trust did not help; inventory DAEMON Tools Lite installations, upgrade or remove them, and hunt the helper-to-PowerShell chain on any host that ran an affected version ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)).

## Correction — 2026-10-11T14:29:53Z

Kaspersky reports no EU government victim: EU countries are among the more than 100 countries with infection attempts, which mostly delivered an information collector, while the backdoor reached about a dozen machines in Russia, Belarus and Thailand and QUIC RAT a single educational institution in Russia ([Kaspersky Securelist, 2026-05-05](https://securelist.com/tr/daemon-tools-backdoor/119654/)). Its QUIC RAT description is limited to the C2 protocols and injection into `notepad.exe` and `conhost.exe`; the keylogging, SOCKS proxy and tunnelling capabilities given earlier had no source. Kaspersky does not attribute the compromise and calls its intent unclear.
