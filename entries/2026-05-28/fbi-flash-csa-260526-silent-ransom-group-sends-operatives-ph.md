---
schema: 1
kind: threat
horizon: operational
title: FBI FLASH CSA 260526 — Silent Ransom Group sends operatives physically into US law-firm offices to insert USB exfiltration devices when remote social engineering fails
headline: FBI FLASH CSA 260526 — Silent Ransom Group sends operatives physically into US law-firm offices to insert USB exfiltration devices when remote social
summary: "The FBI issued CSA 260526 on 2026-05-26 warning that Silent Ransom Group (SRG; tracked variously across cited sources as Luna Moth, Chatty Spider and UNC3753, with the Storm-0252 designation specifically referenced by CyberScoop) — a Russia-linked extortion-only gang that does not deploy ransomware — has escalated its …"
discovered_at: "2026-05-28T05:00:04Z"
event_date: 2026-05-27
run_id: 2026-05-28-3e33200a
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - phishing
  - insider-threat
  - russia-nexus
regions:
  - us
  - europe
sectors:
  - legal-services
entities:
  - "campaign:fbi-flash-csa-260526-silent-ransom-group-physical-usb-attacks-us-law-firms"
cves: []
sources:
  - url: "https://cyberscoop.com/fbi-warning-silent-ransom-group-law-firms/"
    publisher: CyberScoop
    role: primary
  - url: "https://therecord.media/fbi-warns-hackers-visit-law-firms-to-steal-data"
    publisher: The Record
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/27/fbi-silent-ransom-group-law-firms-social-engineering/"
    publisher: Help Net Security
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
migrated_from: briefs/2026-05-28.md
---

The FBI issued CSA 260526 on 2026-05-26 warning that Silent Ransom Group (SRG; tracked variously across cited sources as Luna Moth, Chatty Spider and UNC3753, with the Storm-0252 designation specifically referenced by CyberScoop) — a Russia-linked extortion-only gang that does not deploy ransomware — has escalated its campaign against US law firms by physically sending operatives into victim offices impersonating IT support when remote access attempts fail ([CyberScoop, 2026-05-27](https://cyberscoop.com/fbi-warning-silent-ransom-group-law-firms/); [The Record, 2026-05-27](https://therecord.media/fbi-warns-hackers-visit-law-firms-to-steal-data); [Help Net Security, 2026-05-27](https://www.helpnetsecurity.com/2026/05/27/fbi-silent-ransom-group-law-firms-social-engineering/)). The kill chain begins with callback phishing — an email or call pretexting urgent IT support with a callback number; on the call, the actor attempts to establish a remote desktop session. If the target resists, an associate physically visits the office and attempts to insert a USB storage device into a workstation. CyberScoop, citing the FBI, reports the group has claimed more than 100 attacks.

**Defender takeaway:** the in-person USB tactic is operationally unusual — it requires geographic proximity and a credible IT impersonation persona, which suggests SRG maintains a roster of field operatives in US cities. European law firms with US counterpart offices or US client matters should treat themselves as in scope. Detection: USB-device-insertion events (Windows Security EID 6416 / Sysmon EID 6) on workstations correlated with callback-phishing precursor in mail-security telemetry and with an unfamiliar visitor in physical access logs; flag remote-desktop session initiation by non-IT accounts (EID 4624 Logon Type 10). Hardening: enforce Conditional Access requiring a compliant / managed device for all remote-desktop pathways; disable USB mass-storage on user endpoints via Device Installation policy or EDR enforcement; require second-person authorisation at reception for any visitor claiming IT support.
