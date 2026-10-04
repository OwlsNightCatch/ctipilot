---
schema: 1
kind: research
title: "Sophos: \"Beagle\" backdoor distributed via fake Claude AI site using DonutLoader + DLL sideloading on a signed G DATA AV updater"
headline: "Sophos: \"Beagle\" backdoor distributed via fake Claude AI site using DonutLoader + DLL sideloading on a signed G DATA AV updater"
summary: "Sophos X-Ops published a write-up on 2026-05-07 of a counterfeit Claude AI site, which Sophos assesses is likely part of an active malvertising campaign, distributing a previously undocumented Windows backdoor named Beagle, loaded by Donut shellcode after DLL sideloading on a signed G DATA antivirus updater (Sophos X-Ops, 2026-05-07); Malwarebytes, describing the same archive, calls the payload PlugX (Malwarebytes, 2026-04-10)."
discovered_at: "2026-05-10T05:00:06Z"
event_date: 2026-05-07
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - technology
entities:
  - "tool:beagle-fake-claude-stac4713-2026"
techniques: [T1583.008, T1204.002, T1547.001, T1574, T1574.001, T1573.001]
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor"
    publisher: "Sophos X-Ops, 2026-05-07"
    role: primary
  - url: "https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer"
    publisher: "Malwarebytes, 2026-04-10"
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
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-09-30T06:54:53Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      An attacker-controlled domain is removed and the infrastructure is described instead. The
      description also tied the campaign to Sophos's STAC4713 cluster, linked Donut to an unrelated
      ATT&CK software page, listed four of Beagle's eight commands, dated samples to February, April
      and May, and claimed TTP similarity with named PlugX clusters and a developer targeting class
      no source states. The summary and main text now follow the Sophos report, and Sophos's
      malvertising assessment is hedged as Sophos hedges it. Malwarebytes' report is presented as
      coverage of the same attack rather than an earlier wave, and the main text gains cited
      detection and takeaway lines. A Contradiction line records that Malwarebytes calls the payload
      PlugX while Sophos identifies a new backdoor, Beagle.
    fields: [summary, body, classification, techniques]
---

Sophos X-Ops published a write-up on 2026-05-07 of a counterfeit Claude AI site distributing a previously undocumented Windows backdoor it named **Beagle**, and assesses that the site is likely part of an active malvertising campaign ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). The chain delivers a roughly 505 MB ZIP archive containing a malicious MSI that drops a *legitimate, signed G DATA antivirus updater executable*, an encrypted data file and an attacker-controlled DLL into the user's startup folder, so the updater sideloads the malicious DLL (DLL side-loading) ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). The DLL decrypts the data file and executes the resulting Donut (DonutLoader) shellcode, an open-source in-memory loader, which loads Beagle ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). Beagle communicates with a subdomain of the same lookalike site over TCP/443 and UDP/8080 with AES-encrypted payloads, and its eight commands are `uninstall`, `cmd`, `upload`, `download`, `mkdir`, `rename`, `ls` and `rm` ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). Sophos notes that an almost identical G DATA sideloading chain has previously been associated with PlugX, which several threat groups use, and suggests the Beagle payload may reflect an actor retooling or imitating another actor's chain. It does not attribute the campaign ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). A possible hosting server was set up in March 2026, and Sophos found related samples reusing the same XOR key from February, March and April 2026, while cautioning that further evidence would be needed to link them to the same actor ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)).

Sophos places the campaign in a wider pattern of threat actors crafting lures that imitate legitimate AI sites, often through malvertising ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). **Detection:** a signed G DATA antivirus updater, an encrypted data file and a DLL written together into a user's Startup folder after the fake installer's MSI runs ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). Malwarebytes, describing the same archive, adds that the MSI installs a desktop shortcut that launches a VBScript dropper, run through WScript.exe, which copies the three files into the Startup folder, and that the updater made an outbound connection within seconds (22 seconds in its sandbox run). The dropper script deletes itself, so the Startup-folder files and the running updater process are what persist ([Malwarebytes, 2026-04-10](https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer)).

**Contradiction:** Malwarebytes, describing the same archive, identifies the payload as PlugX, by analogy with an earlier campaign that used the same G DATA sideloading files ([Malwarebytes, 2026-04-10](https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer)), while Sophos analysed it as a previously undocumented backdoor it named Beagle ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)).

**Defender takeaway:** treat AI-tool installers as a high-risk download class. Sophos advises downloading Claude only from the legitimate site and being wary of links from ads and sponsored search results ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)), and Malwarebytes names claude.com/download as the official download page ([Malwarebytes, 2026-04-10](https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer)).

## Correction — 2026-09-30T06:54:53Z

The description above previously tied the campaign to Sophos's STAC4713 cluster, which Sophos mentions only for AdaptixC2 activity linked to a separate March sample. Sophos lists eight Beagle commands, dates the related samples to February, March and April 2026, and does not claim TTP similarity with named PlugX clusters or say who the lures target. It assesses the lookalike site as likely, not confirmed, part of an active malvertising campaign ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)).

Malwarebytes' report of 2026-04-10 covers the same attack, not an earlier wave. Sophos refers to it as coverage of this attack, and both describe the same download archive ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor); [Malwarebytes, 2026-04-10](https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer)).
