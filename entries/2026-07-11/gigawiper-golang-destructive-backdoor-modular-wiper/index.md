---
schema: 1
kind: threat
title: "GigaWiper: a Golang backdoor that folds a disk wiper, fake-ransomware encryptor and secure-wipe module into one modular implant"
headline: "Microsoft dissects GigaWiper — destruction dressed as extortion, driven over RabbitMQ/Redis/MinIO with an 'OneDrive Update' persistence tell"
summary: >
  Microsoft Threat Intelligence documented GigaWiper (2026-07-09), a Go destructive backdoor that
  combines a raw-disk wiper, a Crucio-derived encryptor whose keys are never saved, and a
  FlockWiper-derived secure-wipe module as on-demand commands, tasked over RabbitMQ/Redis with
  MinIO exfiltration. First seen October 2025; concrete low-noise hunt pivots exist. Relevant to
  any Windows critical-infrastructure estate as transferable destructive tradecraft.
discovered_at: "2026-07-11T04:30:43Z"
event_date: "2026-07-09"
run_id: 2026-07-11T0409Z-intel
priority: notable
immediate_action: null
tags: [wiper, ransomware, nation-state, infostealer]
regions: [global]
sectors: [energy, public-sector, healthcare, finance, telco]
entities: [tool:gigawiper, tool:crucio-ransomware, tool:flockwiper]
techniques: [T1485, T1561.001, T1561.002, T1486, T1053.005, T1112, T1113, T1056.001, T1071, T1567.002]
affected_products: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-09"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/new-gigawiper-espionage-destructive/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "It's not a single, purpose-built tool, but an amalgamation of separate malware families that were folded into GigaWiper as on-demand backdoor commands, giving threat actors the flexibility to choose their mode of destruction"
    publisher: "Microsoft Threat Intelligence"
  - quote: "The key and initialization vector (IV) that the malware uses to encrypt files are random and are not saved anywhere"
    publisher: "Microsoft Threat Intelligence"
verification: multi-source
sourcing_note: null
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
  - "Hunt for a scheduled task literally named 'OneDrive Update' running every minute plus at logon, and for a HKCU\\SOFTWARE\\OneDrive\\Environment registry value — neither is created by legitimate OneDrive; confirm the real OneDrive task name/path in your estate as the baseline."
  - "In egress/firewall telemetry, surface hosts making outbound RabbitMQ/AMQP, Redis and MinIO/S3-style object-storage connections with no legitimate business reason to speak any of the three, especially all three to the same endpoint."
  - "Treat GigaWiper as destruction, not ransomware: because encryption keys are never retained there is no decryption path — prioritise offline, tested backups and recovery drills for internet-exposed Windows critical-infrastructure hosts."
migrated_from: null
---

Microsoft Threat Intelligence first identified GigaWiper in October 2025 and has now published a code-level analysis of it: a Golang backdoor notable less for any single capability than for its construction — at least three previously separate destructive families folded into one implant as on-demand commands, so an operator can pick the mode of destruction at task time ([Microsoft Threat Intelligence, 2026-07-09](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/)). The raw-disk wiper command enumerates physical drives over WMI, identifies and spares the Windows installation drive, strips partition metadata from the other drives via `DeviceIoControl`/`IOCTL_DISK_CREATE_DISK`, overwrites disk content in 0xA00000-byte chunks (randomising only the first byte of each buffer to dodge naïve all-zero-wipe detections), then forces an immediate reboot. A second command reuses Crucio ransomware code to AES-encrypt files with per-run keys that are never saved and drops no ransom note — destruction wearing an extortion costume — while a third reimplements the C-based FlockWiper in Go for multi-pass secure wiping of the Windows drive. Microsoft ties the families together by code overlap and assesses that the same developer built GigaWiper and Crucio; it withholds actor attribution beyond that lineage. Google's Threat Intelligence Group and Binary Defense track the same activity as BLUERABBIT ([Microsoft Threat Intelligence, 2026-07-09](https://www.microsoft.com/en-us/security/blog/2026/07/09/gigawiper-anatomy-of-a-destructive-backdoor-assembled-from-multiple-malware/); [Infosecurity Magazine, 2026-07-10](https://www.infosecurity-magazine.com/news/new-gigawiper-espionage-destructive/)).

Operationally the implant is quieter than its payload. It persists as a scheduled task named `OneDrive Update` (configured to run roughly every minute and once at startup) and tracks its own execution count in a `HKCU\SOFTWARE\OneDrive\Environment` registry value, masquerading as Microsoft's sync client. For command-and-control it skips ordinary HTTP: tasking arrives over RabbitMQ/AMQP — a fanout exchange named `All` for broadcast to every infected client plus a topic exchange for targeted commands — status and output are polled back through a Redis server, and MinIO object storage carries exfiltration, alongside keylogging and screen-capture modules. **Defender takeaway:** the persistence footprint and the C2 protocol mix are both high-value, low-false-positive hunt anchors — legitimate OneDrive never lives under that task name or registry path, and a standard workstation has no reason to speak AMQP, Redis and MinIO outbound. **Triage:** genuine OneDrive does run scheduled sync tasks, so the discriminator is the exact task name (`OneDrive Update`) and the `HKCU\SOFTWARE\OneDrive\Environment` key rather than the presence of a OneDrive-named task per se; pair that with outbound RabbitMQ/Redis/MinIO from a host with no such workload and the two together are the signal. Because the encryptor discards its keys, defence is recovery-first: this is a data-destruction threat, and the only meaningful mitigation for an exposed Windows estate is tested, offline backups.
