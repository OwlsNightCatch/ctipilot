---
schema: 1
kind: threat
title: "Rapid7 links a Chaos-branded extortion intrusion to MuddyWater with moderate confidence: Teams screen-sharing harvested credentials and MFA, and no files were encrypted"
headline: "An intrusion posing as Chaos ransomware stole data without encrypting it, and Rapid7 ties it to Iran's MuddyWater through a code-signing certificate and C2"
summary: >
  Rapid7 assesses with moderate confidence that an early-2026 intrusion presented as a Chaos ransomware
  attack was MuddyWater activity, based on a code-signing certificate and C2 infrastructure. The actor
  used external Microsoft Teams chats and screen sharing to have victims type credentials into local text
  files and add attacker-controlled MFA devices, persisted with DWAgent and AnyDesk, moved over RDP to a
  domain controller, exfiltrated data and demanded ransom by email without encrypting any files.
discovered_at: "2026-05-08T05:00:03Z"
event_date: "2026-05-06"
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - nation-state
  - phishing
  - identity
  - iran-nexus
regions:
  - us
  - global
sectors: []
entities:
  - "actor:muddywater"
  - "actor:chaos-ransomware"
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/"
    publisher: "Rapid7"
    date: "2026-05-06"
    role: primary
  - url: "https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html"
    publisher: "The Hacker News"
    date: "2026-05-06"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source
sourcing_note: >
  Rapid7 is the only analyst; The Hacker News relays its report. The MuddyWater link is Rapid7's
  moderate-confidence assessment.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
techniques: [T1566.003, T1078, T1098.005, T1219, T1021.001, T1105, T1041]
classification:
  reliability: B
  credibility: 3
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-10-11T14:21:21Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The cited Deep Instinct source does not exist; the research is Rapid7's report of 2026-05-06. The actor did not deploy encrypting Chaos payloads but used the Chaos brand for extortion without encrypting files, Rapid7 links it to MuddyWater only with moderate confidence, and Rapid7 describes no government or defence victim in this intrusion. The prose ATT&CK ids were wrong (Spearphishing Voice, certificate theft, encryption); the entry is rewritten from Rapid7 with the Teams screen-sharing, MFA and remote-tool chain, a corrected mapping (adding the curl payload downloads as ingress tool transfer), labelled guidance, a rating and medium confidence.
    fields: [title, headline, summary, event_date, tags, regions, entities, techniques, sources, verification, sourcing_note, confidence, classification, body]
---

Rapid7 investigated an early-2026 intrusion that presented as an attack by the Chaos ransomware-as-a-service operation and assesses, "with moderate confidence", that it is linked to MuddyWater (Seedworm), the Iranian state-sponsored group, on the strength of a code-signing certificate and command-and-control infrastructure ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). The actor opened external one-on-one Microsoft Teams chats, moved victims into screen-sharing sessions, had them type credentials into locally created text files and change their MFA configuration to include attacker-controlled devices, then established persistence with the remote management tools DWAgent and AnyDesk ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). It authenticated to internal systems, including a domain controller, with several compromised accounts and deployed a downloader for the Darkcomp backdoor that Rapid7 says is firmly attributed to MuddyWater ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). The actor exfiltrated data and demanded ransom under the Chaos brand by email, but forwent file encryption in favour of data theft and long-term persistence ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). Rapid7 reads the false flag as deniability for espionage and prepositioning, particularly in the US; Chaos itself had claimed 36 victims by late March 2026 ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). The Hacker News reported the research the same day ([The Hacker News, 2026-05-06](https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html)).

**Detection:** in collaboration-platform audit telemetry, an external-tenant Teams one-on-one chat that moves to screen sharing, followed by a new MFA device registration for the same user, is the chain Rapid7 describes ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). On endpoints, DWAgent or AnyDesk installed outside change control and credential text files created during a support session are the follow-on signals ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)).

**Triage:** legitimate external Teams support sessions exist; the discriminator is an MFA method added during or right after a chat with an external tenant, a step a genuine support session has no reason to include.

**Defender takeaway:** an extortion demand with no encryption is not proof of a criminal actor. Restrict external Teams chat and screen sharing to approved tenants, and require out-of-band verification before any MFA change requested in a chat.

## Correction — 2026-10-11T14:21:21Z

Rapid7, not Deep Instinct, reported this intrusion, and it links it to MuddyWater only "with moderate confidence" ([Rapid7, 2026-05-06](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)). The actor encrypted nothing: it used the Chaos brand to demand ransom by email after stealing data. Rapid7 describes no government or defence victim in this intrusion and describes the prepositioning as "particularly in the US". The Teams chats with screen sharing were the main intrusion path, not a parallel vector, and Rapid7 describes no certificate theft or forging; the code-signing certificate is attribution evidence.
