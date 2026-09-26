---
schema: 1
kind: threat
title: "CHOSEN BRICK — Iranian state cyber actors run Telegram-C2 Windows spyware against dissidents, activists and journalists, per joint NCSC-UK/FBI/AIVD advisory"
headline: "NCSC-UK, the FBI and AIVD detail an Iranian spyware family that gives every victim their own private Telegram bot for command and control"
summary: >
  NCSC-UK, the FBI and the Netherlands' AIVD jointly published a technical advisory on 2026-09-15 for
  CHOSEN BRICK, a Windows-only malware family Iranian state cyber actors have used since at least 2025
  against dissidents, activists and journalists in the UK, US and Netherlands. Delivery is
  social-engineering-led over WhatsApp/Telegram; the malware persists via a registry Run key, disables
  Defender via exclusions, and uses a per-victim unique Telegram bot for command and control, with data
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
  NCSC UK, the FBI and AIVD co-authored a single joint advisory rather than three independently
  arrived-at assessments; The Record's reporting relays the same advisory rather than adding
  independent technical confirmation. Treated under the government-authority carve-out as a
  single-source item from a high-reliability primary disclosing authority.
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
migrated_from: null
---

NCSC UK, the US FBI and the Netherlands' AIVD jointly published a technical advisory on 2026-09-15 for CHOSEN BRICK, a Windows-only malware family Iranian state cyber actors have used since at least 2025 against dissidents, activists and journalists, with confirmed victims in the UK, US and Netherlands ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC assesses Iran "almost certainly" uses this activity to support repression of people it perceives as regime threats, and notes Iranian intelligence services have in parallel plotted kidnap or lethal operations against some of the same class of target — framing CHOSEN BRICK as a transnational-repression tool rather than conventional espionage tradecraft ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). NCSC UK's advisory does not itself name a specific Iranian government entity, but the tradecraft closely matches activity the FBI attributed to actors operating "on behalf of the Government of Iran Ministry of Intelligence and Security" in a flash warning circulated in March 2026, which also linked a July 2025 hack-and-leak operation to the "Handala Hack" persona the FBI assesses MOIS operates and connects to a further group, "Homeland Justice" ([The Record, 2026-09-15](https://therecord.media/iran-cyber-spies-use-fake-mri-scans-as-lure)).

Access begins with extensive social-engineering rapport-building over WhatsApp or Telegram, the actor posing as a contact already known to the target or as platform technical support (T1589, T1566.003). The victim is then persuaded to download and open a file disguised as a legitimate application — observed lures include Pictory, RunwayML, Norton Antivirus, Telegram, Adobe Flash Player and KeePass — or as MRI scan results (T1204.002); a decoy screen matching the lure's theme displays while the core malware installs in the background. Operators target the victim's work device first and, if delivery fails or detection risk looks high, pivot to asking the victim to open the file on a personal device instead, sidestepping corporate controls entirely. In every observed instance the malware has targeted Windows only.

CHOSEN BRICK persists across reboot via the registry Run key `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (T1547.001), registers a mutex — commonly "ytyjyujyu" or "noi672pp434awkc12f" (T1480.002) — and adds Microsoft Defender exclusions to evade detection (T1685). Command and control runs over Telegram, with each victim device assigned its own unique Telegram Bot ID as an explicit operational-security measure to prevent cross-contamination between victims ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)); newer variants layer HTTPS/SOCKS5 proxies over that channel to further obscure it (T1090.002). No automated lateral-movement capability has been observed, though the malware can download and persist additional payloads through the same registry mechanism, making it technically possible.

Tasking supports process and system enumeration (T1057, T1082), screen capture — the most commonly observed data-theft feature, used to map a victim's contacts, location and pattern of life (T1113) — microphone capture (T1123), theft of Telegram/WhatsApp browser data (T1005) and email content (T1114.001), and file deletion or a full disk wipe (T1485). Collected data exfiltrates through the Telegram bot (T1041) or cloud object stores such as VultrObjects and StorjShare (T1567.002). NCSC states the most commonly observed additional-malware drop path is `C:\Windows \SysWOW64` — a non-standard location on most Windows installs because of the deliberate space after "Windows," which NCSC states the actor created specifically for the purpose of deploying malware; in at least one sample, this downloaded payload carried the data-wiping functionality already described above ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)). Some victims' personal data has since surfaced on pro-Iranian leak sites, which NCSC reads as a further harassment vector rather than incidental exposure ([NCSC UK, 2026-09-15](https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists)).

**Defender takeaway:** CHOSEN BRICK targets people, not infrastructure, so the relevant defensive population is any organization with staff whose personal profile makes them a plausible transnational-repression target — diplomatic missions, asylum and refugee-support units, and any authority protecting activists, journalists or dissidents. Because operators explicitly pivot to a victim's personal device when a corporate one resists, guidance and detection support need to extend to personal devices for at-risk staff, not only managed endpoints. **Triage:** legitimate use of api.telegram.org, backblazeb2.com, vultrobjects.com, storjshare.io, iproyal.com and lightningproxies.net is common and none of these is inherently malicious; the discriminator NCSC gives is these domains appearing in DNS or proxy logs where they are not otherwise expected for the account or host in question, paired with a new Run-key entry the user did not knowingly install.

