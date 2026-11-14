---
schema: 1
kind: threat
title: "APT28 (Swallowtail) used the HOOKEDGE backdoor against a law-enforcement agency, a naval shipbuilder and an aircraft-engine maker in two NATO states; at the shipbuilder it then pushed an SSH key for a persistent tunnel, captured NTLM handshakes and ran a reflective loader"
headline: "Symantec: APT28's hidden-Edge backdoor hit law-enforcement and defence targets; at a shipbuilder it added an SSH tunnel"
summary: >
  Symantec reports that APT28, which it tracks as Swallowtail, used the HOOKEDGE backdoor against a law-enforcement agency, a naval
  shipbuilder and a military aircraft-engine manufacturer in two NATO member states, none named. A macro-enabled Word document
  started a script chain that uses a hidden, off-screen Microsoft Edge window as its HTTP client against a public webhook service;
  at the shipbuilder the operators then pushed an SSH private key for a persistent tunnel, captured NTLM handshakes from the host
  itself and ran a previously undocumented in-memory loader, in an intrusion that lasted at least two months. Recorded Future had
  documented HOOKEDGE against government and diplomatic targets in Romania, Spain and Turkiye in August.
discovered_at: "2026-10-21T03:44:00Z"
updated_at: null
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, russia-nexus]
regions: [europe]
sectors: [public-sector, defense]
entities: ["actor:apt28", "malware:hookedge"]
techniques: [T1566.001, T1204.002, T1027, T1059.005, T1059.003, T1059.001, T1564.003, T1102.002, T1105, T1053.005, T1572, T1187, T1620, T1070.004, T1033, T1082, T1016, T1083, T1057, T1069]
affected_products: ["Microsoft Word", "Microsoft Edge"]
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets"
    publisher: "Symantec Threat Hunter Team"
    date: "2026-10-20"
    role: primary
  - url: "https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge"
    publisher: "Recorded Future Insikt Group"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Swallowtail (aka APT28, Fancy Bear, Forest Blizzard), a Russian espionage group, targeted organizations in two NATO member states, including a law enforcement agency, a naval shipbuilder, and a manufacturer of military aircraft engines."
    publisher: "Symantec Threat Hunter Team"
    source_url: "https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets"
  - quote: "Hookedge is delivered through macro-enabled Word documents and communicates entirely through the webhook.site service, using it to stage tasks and to receive their output."
    publisher: "Symantec Threat Hunter Team"
    source_url: "https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets"
  - quote: "Organizations that identify Hookedge indicators in their environment should treat the intrusion as potentially ongoing rather than concluded"
    publisher: "Symantec Threat Hunter Team"
    source_url: "https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets"
  - quote: "Organizations should prioritize blocking macro execution from internet-originated documents and implementing detection coverage for scheduled task abuse, headless Microsoft Edge execution, and outbound connections to webhook services."
    publisher: "Recorded Future Insikt Group"
    source_url: "https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge"
verification: multi-source
sourcing_note: >
  The post-access tradecraft and the three new victims rest on Symantec alone, which holds first-hand telemetry and
  names no victim or country, while Recorded Future documented HOOKEDGE independently in August and assesses with
  moderate confidence that BlueDelta, which overlaps APT28, conducted that activity. Symantec relies on the US
  government for the GRU attribution, and the loader's payload was not recovered.
confidence: high
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

Symantec's Threat Hunter Team reports that Swallowtail, which it equates with APT28, Fancy Bear and Forest Blizzard, targeted organizations in two NATO member states: a law-enforcement agency, a naval shipbuilder and a manufacturer of military aircraft engines, none named ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)). Recorded Future had documented the HOOKEDGE backdoor in August, from campaigns between late September 2025 and early April 2026 against government and diplomatic organizations in Romania, Spain and Turkiye, and assesses with moderate confidence that BlueDelta, which overlaps APT28, is behind it ([Recorded Future, 2026-08-27](https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge)).

At the shipbuilder the vector was a macro-enabled Word document opened from the Outlook attachment cache on 2026-07-24, so it arrived by email; its macro dropped a VBScript launcher, an HTML pair that auto-submits a hidden form to a webhook endpoint and a batch script ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)). The batch script kills any running Microsoft Edge and restarts it as a one-pixel, off-screen window carrying an inline script instead of a URL, so the browser fetches the next task from the public webhook.site service, and the batch script then runs the task and uploads its output to the same endpoint ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)). A second stage then took its tasks from a dedicated address, and seven tasks arrived in about 30 seconds, a cadence Symantec reads as interactive ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)).

The operators then pushed an SSH private key onto the host and at once opened an outbound SSH session to their own server with host-key checking disabled, legacy RSA algorithms enabled and a background remote port forward, a persistent route into the internal network; separately a short PowerShell script ran an HTTP listener on loopback and net use against it, forcing the host to authenticate to itself so the NTLM handshake could be captured ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)). On 2026-07-31 they ran a previously undocumented reflective loader, which decrypts an encrypted file in memory; the payload was not recovered, and the launcher was last seen on 2026-09-24 ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)).

**Exposure:** Windows endpoints where users can open Office documents from mail and macros from internet-originated documents are allowed, and hosts with outbound access to webhook services. Symantec names no victim or country.

**Detection:** process-creation telemetry with parent lineage for Word spawning script hosts or the command shell, then msedge.exe killed and restarted with a one-pixel window, an off-screen position and a data: URL argument; network and proxy telemetry for msedge.exe or curl reaching a webhook service; ssh.exe started with an identity file, a remote forward and host-key checking disabled; a PowerShell HTTP listener on loopback followed by net use to localhost; and scheduled-task creation by the launcher or installer, since Symantec says the second-stage installer has a scheduled task and Recorded Future advises detecting scheduled-task abuse ([Recorded Future, 2026-08-27](https://www.recordedfuture.com/research/bluedelta-targets-with-hookedge)) ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)).

**Triage:** the distinctive sequence is an Office document's script host, then Edge killed and relaunched as a one-pixel off-screen window carrying an inline script instead of a URL; the Edge launch alone is not the signal.

**Defender takeaway:** block macro execution from internet-originated documents and, on any host where a HOOKEDGE launcher is found, hunt for the credential theft and the SSH tunnel described above and reset the credentials the host used, because the shipbuilder intrusion continued long after the dropper ran ([Symantec, 2026-10-20](https://www.security.com/threat-intelligence/swallowtail-russia-nato-targets)).
