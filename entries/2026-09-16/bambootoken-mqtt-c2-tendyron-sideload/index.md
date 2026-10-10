---
schema: 1
kind: threat
title: "BambooToken — a previously undocumented MQTT-based malware framework sideloads via a signed Chinese hardware-token utility to control Windows and Linux hosts"
headline: "Lumen: an unattributed cluster hides its command-and-control behind an IoT messaging broker so infected hosts never talk to the attacker directly"
summary: >
  Lumen's Black Lotus Labs disclosed BambooToken on 2026-09-15, a previously undocumented malware
  framework active since February 2023 and observed through July 2026 that uses the MQTT
  publish/subscribe protocol, rather than direct callbacks, to control Windows and Linux hosts. The
  Windows toolset is sideloaded via a digitally signed Chinese USB hardware-token utility widely
  deployed in Chinese banking and government networks; targeting spans roughly a dozen enterprise
  victims across Asia and a handful in South America, including a compromised GitLab instance, and
  Lumen assesses the cluster as China-aligned without attributing it to a named group.
discovered_at: "2026-09-16T05:10:00Z"
updated_at: null
event_date: "2026-09-15"
run_id: 2026-09-16T0409Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - supply-chain
  - china-nexus
regions:
  - apac
  - latam
sectors:
  - finance
  - legal-services
  - technology
entities:
  - "malware:bambootoken"
techniques:
  - T1574.001
  - T1036.005
  - T1071.005
  - T1059
  - T1082
  - T1047
  - T1518.001
  - T1105
  - T1027
affected_products: []
cves: []
sources:
  - url: "https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt"
    publisher: "Lumen Black Lotus Labs"
    date: "2026-09-15"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/bambootoken-malware-controls-windows-and-linux-systems-via-mqtt/"
    publisher: "BleepingComputer"
    date: "2026-09-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Black Lotus Labs®, the threat research division at Lumen, uncovered BambooToken, an emerging malware family using the Message Queueing and Telemetry Transport (MQTT) to quietly control infected Windows and Linux systems."
    publisher: "Lumen Black Lotus Labs"
  - quote: "The Windows agent was sideloaded by the Tendyron “OnKey” program, which validates system access by retrieving cryptographic material stored on a USB drive. This product line is popular in Chinese banking and government networks."
    publisher: "Lumen Black Lotus Labs"
  - quote: "Lumen does not assess that Tendyron's code signing certificate was compromised. Preliminary analysis indicates the signed executable appears benign and was vulnerable to side-loading rather than actively abused through a certificate compromise."
    publisher: "Lumen Black Lotus Labs"
  - quote: "This approach has the advantage that infected systems do not connect directly to the attacker’s infrastructure, which increases evasion and resilience. At the same time, communications can be asynchronous, ensuring operational continuity during temporary network disruptions."
    publisher: "BleepingComputer"
verification: single-source
sourcing_note: >
  BleepingComputer's article relays Lumen Black Lotus Labs' own findings rather than independently
  assessing the malware or its infrastructure; every technical claim traces to the single Lumen
  report, so this is a single-source item despite two publishers.
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

Lumen's Black Lotus Labs disclosed BambooToken on 2026-09-15: an emerging, previously undocumented malware framework that, based on embedded artifacts, has been active since at least February 2023 and continued through July 2026 ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). The most recent sample Lumen correlated to the campaign, a Linux build, was first observed in December 2025 ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). Rather than the direct HTTP callbacks its 2023 version used, the current Windows and Linux toolset communicates over MQTT, a publish/subscribe protocol built for IoT device control: infected hosts publish and subscribe to topics through a broker rather than contacting a command server directly, so a compromised machine never talks to the attacker's infrastructure at all, and the channel supports asynchronous tasking that survives temporary network disruption ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). Lumen's own review of prior campaigns found only three other malware families that have ever used MQTT for command and control — IOCONTROL, Korplug/PlugX and WailingCrab — making this a rare, not novel, technique choice.

The Windows variant is sideloaded through Tendyron's "OnKey" utility, a digitally signed USB hardware-token program that verifies cryptographic material for identity checks and is widely deployed across Chinese banking and government networks ("The Windows agent was sideloaded by the Tendyron 'OnKey' program, which validates system access by retrieving cryptographic material stored on a USB drive. This product line is popular in Chinese banking and government networks," [Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). One variant instead masquerades as "Zhuhai Kingsoft Office Software Co., Ltd." Lumen assesses neither Tendyron's nor Kingsoft's code-signing certificate was compromised: the OnKey binary itself is genuinely signed but merely vulnerable to sideloading rather than abused through a certificate compromise, while the Kingsoft-masquerading variant's own files fail certificate-signature validation outright, confirming that certificate was never actually applied to them ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)).

Once running, the malware enumerates the host through Windows Management Instrumentation — operating system details, computer system product details, the original product key, serial number and software licensing service information — then subscribes to a global broadcast topic plus per-host, GUID-scoped topics and publishes an online/offline heartbeat carrying that GUID ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). Three command handlers have been identified: SHELL spawns a command shell, FILEEX uploads, downloads and deletes files, and ONLINE collects and beacons a separate set of host parameters, including BIOS and system details, as a heartbeat ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). A recovered plugin performs security-software discovery via WMI on a five-second timer and reports results over plain HTTP. Static "dead code" strings referencing clipboard capture, keylogging, audio recording and webcam capture were found in one sample's unexecuted code sections ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)); because the detail comes from dead code, researchers cannot confidently determine whether these modules were ever operational or remain under development ([BleepingComputer, 2026-09-15](https://www.bleepingcomputer.com/news/security/bambootoken-malware-controls-windows-and-linux-systems-via-mqtt/)).

Lumen's telemetry links a dozen compromised enterprise environments mostly located in Asia, with a handful in South America — named examples include a biomedical company in Argentina and a legal firm in Chile — spanning mobile-application backends, legal and financial services, a smartwatch-adjacent software company, a hotel and a GitLab instance in Hong Kong, the last of which the report flags as a software-supply-chain concern given the developer access such a compromise could yield ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). A separate cluster of over 150 infected small-office and home routers was reached through internet-wide SNMP scanning; a handful of those IPs held persistent connections to an active C2 node over the MQTT port, and Lumen identifies the underlying devices in that handful as primarily MikroTik and DrayTek routers geolocated to Singapore, Cambodia and Vietnam. Lumen believes this pool primarily supports data collection against the Chinese diaspora rather than serving as C2 relay infrastructure ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). Command-and-control domains sit behind Cloudflare, with one domain reaching Cloudflare Radar's top 500,000 most-popular domains and an older one the top million at the height of its use — evidence of a wide, established infection base rather than a narrow test deployment ([Lumen Black Lotus Labs, 2026-09-15](https://www.lumen.com/blog/en-us/the-banana-stand-brokering-and-managing-infections-across-asia-using-mqtt)). Lumen assesses the targeting pattern as consistent with China-aligned operations but states it cannot attribute the cluster to any publicly documented actor.

**Defender takeaway:** the sideloading technique here does not require a vendor vulnerability disclosure to defend against — it abuses a legitimately signed binary's normal DLL search-order behavior. Any organization running Tendyron OnKey hardware-token software, or any other identity/cryptographic USB-token client, should verify the integrity and expected file set of that installation directory rather than trusting code-signing status alone, since a validly signed launcher can still load an attacker-supplied DLL placed alongside it. **Triage:** outbound MQTT traffic (ports 1883, 2883 and 8883) is unusual on a standard enterprise Windows or Linux fleet that has no legitimate IoT messaging use; unexpected MQTT connections from an endpoint, especially one also running identity-token, banking or point-of-sale-adjacent software, are the discriminator this technique's own protocol choice creates.
