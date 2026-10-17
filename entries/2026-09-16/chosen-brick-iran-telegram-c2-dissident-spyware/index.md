---
schema: 1
kind: threat
title: "CHOSEN BRICK — Iranian state cyber actors run Telegram-C2 Windows spyware against dissidents, activists and journalists, per joint NCSC-UK/FBI/AIVD advisory"
headline: "NCSC-UK, the FBI and AIVD detail an Iranian spyware family that gives every victim their own private Telegram bot for command and control"
summary: >
  NCSC-UK, the FBI and the Netherlands' AIVD jointly published a technical advisory on 2026-09-15 for
  CHOSEN BRICK, a Windows-only malware family Iranian state cyber actors have used since at least 2025
  against dissidents, activists and journalists around the world, including in the UK, US and the Netherlands. Delivery is social-engineering-led over WhatsApp/Telegram. The malware persists via a registry Run key, adds Microsoft Defender exclusions to evade detection, and uses a per-victim unique Telegram bot for command and control, with data
  exfiltrated through Telegram or legitimate cloud object stores.
discovered_at: "2026-09-16T05:00:00Z"
updated_at: null
event_date: "2026-09-15"
run_id: 2026-09-16T0409Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - iran-nexus
regions:
  - global
sectors:
  - public-sector
entities:
  - "malware:chosen-brick"
techniques:
  - T1589
  - T1566.003
  - T1204.002
  - T1547.001
  - T1480.002
  - T1685
  - T1102.002
  - T1090.002
  - T1057
  - T1082
  - T1113
  - T1123
  - T1005
  - T1114.001
  - T1485
  - T1041
  - T1567.002
affected_products: ["Microsoft Windows"]
cves: []
sources:
  - url: "https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists"
    publisher: "NCSC UK (with FBI and AIVD)"
    date: "2026-09-15"
    role: primary
  - url: "https://www.ncsc.gov.uk/news/uk-allies-expose-spyware-iranian-state-actors-target-dissidents-activists-journalists"
    publisher: "NCSC UK"
    date: "2026-09-15"
    role: primary
  - url: "https://therecord.media/iran-cyber-spies-use-fake-mri-scans-as-lure"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CHOSEN BRICK is a malware family that has been used to target individuals around the world including in the UK, US and the Netherlands from at least 2025."
    publisher: "NCSC UK"
  - quote: "Iran almost certainly uses cyber activity to support the repression of individuals who are seen as a threat to the regime, such as dissidents, activists and journalists. In some cases, the Iranian intelligence services have plotted to kidnap or conduct lethal operations against individuals internationally, who they perceive as enemies of the regime."
    publisher: "NCSC UK"
  - quote: "Once established on the victim, the malware connects to Telegram for Command and Control (T1102.002). Each victim device connects to a different Telegram Bot ID unique to them as an Operational Security precaution, preventing cross-contamination between victims."
    publisher: "NCSC UK"
  - quote: "The personal details of some previous victims of CHOSEN BRICK have appeared on pro-Iranian leak sites, potentially increasing the risk to the personal safety of those affected."
    publisher: "NCSC UK"
verification: single-source-national-cert
sourcing_note: >
  NCSC UK, the FBI and AIVD co-authored one joint advisory rather than three independent
  assessments, and The Record relays that advisory without independent technical confirmation. It
  rests on a single high-reliability government primary.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-20T13:30:32Z"
    run_id: 2026-09-20T1308Z-audit
    type: improvement
    summary: >
      The sourcing note carried an internal policy-reference code in reader-facing text. It now names the
      government-authority carve-out in plain language. No sourcing or factual claim changes.
    fields: [sourcing_note]
    internal: true
  - at: "2026-09-30T06:54:18Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Two mutex names, which are host indicators, are removed from the main text. NCSC's framing and
      the triage line now follow the advisory, which gives the Run-key check and the
      unexpected-connections check as separate steps. The drop directory is described rather than
      given as a path, and the victim geography, the screen-capture frequency, the data-wiping
      sample and the Defender exclusions follow NCSC's wording. The delivery paragraph now cites
      NCSC.
    fields: [body, sourcing_note, summary]
migrated_from: null
---

NCSC UK, the US FBI and the Netherlands' AIVD jointly published a technical advisory on 2026-09-15 for CHOSEN BRICK, a Windows-only malware family Iranian state cyber actors have used since at least 2025 against dissidents, activists and journalists, targeting individuals around the world including in the UK, US and the Netherlands ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC assesses Iran "almost certainly" uses cyber activity to support repression of people it sees as regime threats, and notes Iranian intelligence services have in some cases plotted kidnap or lethal operations against such people internationally ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC UK's advisory does not itself name a specific Iranian government entity, but the tradecraft closely matches activity the FBI attributed to actors operating "on behalf of the Government of Iran Ministry of Intelligence and Security" in a flash warning circulated in March 2026, which also linked a July 2025 hack-and-leak operation to the "Handala Hack" persona the FBI assesses MOIS operates and connects to a further group, "Homeland Justice" ([The Record, 2026-09-15](https://therecord.media/iran-cyber-spies-use-fake-mri-scans-as-lure)).

Access begins with rapport-building over messaging apps such as WhatsApp and Telegram, drawing on extensive prior research into the target, with the actor often posing as someone the target already knows or as the platform's technical support. The victim is then persuaded to download and open a file disguised as a legitimate application (observed lures include Pictory, RunwayML, Norton Antivirus, Telegram, Adobe Flash Player and KeePass) or as MRI scan results. A decoy screen matching the lure's theme displays while the core malware downloads and runs in the background. The actor often contacts the target's work device first and, if delivery fails or detection risk looks high, asks the target to open the file on a personal device instead, evading the corporate controls that protect them. In every observed instance the malware has targeted Windows only ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)).

CHOSEN BRICK persists across reboot via the registry Run key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, registers a mutex so only one copy runs, and adds Microsoft Defender exclusions to evade detection. Command and control runs over Telegram, with each victim device assigned its own unique Telegram Bot ID as an explicit operational-security measure to prevent cross-contamination between victims ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)); newer variants layer HTTPS/SOCKS5 proxies over that channel to further obscure it. No automated lateral-movement capability has been observed, though the malware can download and persist additional payloads through the same registry mechanism, making it technically possible.

Tasking supports process and system enumeration, screen capture, microphone capture, theft of Telegram/WhatsApp browser data and email content, and file deletion or a full disk wipe. NCSC says screen capture is a data-theft feature commonly observed in these infections, which the actor can use to identify a victim's contacts, location and pattern of life ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). Collected data exfiltrates through the Telegram bot or cloud object stores such as VultrObjects and StorjShare. NCSC states the most commonly observed additional-malware drop location is a lookalike of the system SysWOW64 directory under a folder named "Windows" with a trailing space, which NCSC states the actor created specifically for the purpose of deploying malware. NCSC adds that in at least one sample there was functionality for data wiping ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). Some victims' personal data has since surfaced on pro-Iranian leak sites, which NCSC reads as a further harassment vector rather than incidental exposure ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)).

**Defender takeaway:** CHOSEN BRICK targets people, not infrastructure, so the relevant defensive population is any organization with staff whose personal profile makes them a plausible transnational-repression target, such as diplomatic missions, asylum and refugee-support units, and any authority protecting activists, journalists or dissidents. Because operators explicitly pivot to a victim's personal device when a corporate one resists, guidance and detection support need to extend to personal devices for at-risk staff, not only managed endpoints. **Triage:** legitimate use of the Telegram Bot API, Backblaze B2, Vultr and Storj object storage, and the IPRoyal and Lightning Proxies proxy services is common and none is inherently malicious. The discriminator NCSC gives is connections to these services in DNS or web proxy logs where they are not expected as part of normal business ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC's investigation guidance lists a separate check of the current user's Run key, where the malware most often persists, for programs set to start at logon ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)), so a Run-key entry the user did not knowingly set up on the same host corroborates the lead.

## Correction — 2026-09-30T06:54:18Z

NCSC does not contrast CHOSEN BRICK with conventional espionage. Its investigation guidance gives two separate checks: the current user's Run key for programs set to start at logon, and connections to the listed legitimate services where they are not expected as part of normal business ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC says the malware adds exclusions to Microsoft Defender to evade detection, not that it disables Defender ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)).

NCSC gives the targeting as individuals around the world including in the UK, US and the Netherlands, not as confirmed victims in those three countries, while The Record reads the advisory as covering victims in all three ([The Record, 2026-09-15](https://therecord.media/iran-cyber-spies-use-fake-mri-scans-as-lure)). It calls screen capture a commonly observed data-theft feature, not the most common one, and it says only that at least one sample had data-wiping functionality, without tying that to the payloads the malware downloads ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)).
