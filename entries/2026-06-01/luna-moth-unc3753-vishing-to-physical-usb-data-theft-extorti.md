---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Luna Moth / UNC3753: vishing-to-physical-USB data-theft extortion reaches ~$20 M suppression payment and DNS fast-flux C2"
headline: "Luna Moth / UNC3753: vishing-to-physical-USB data-theft extortion reaches ~$20 M suppression payment and DNS fast-flux C2"
summary: "Mandiant's comprehensive primary forensic analysis published 5 June (Mandiant; deep-dived daily 2026-06-06) documents a January–May 2026 data-theft extortion campaign against US legal and professional-services organisations by UNC3753 (Luna Moth / Silent Ransom Group)."
discovered_at: "2026-06-01T05:00:12Z"
event_date: 2026-06-06
run_id: 2026-W23-9118e7bd
priority: notable
immediate_action: null
tags:
  - organized-crime
  - data-breach
  - phishing
regions:
  - us
  - global
sectors:
  - legal-services
  - finance
entities:
  - "campaign:fbi-flash-csa-260526-silent-ransom-group-physical-usb-attacks-us-law-firms"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms/"
    publisher: Mandiant / Google Cloud GTIG
    role: primary
  - url: "https://www.legalcheek.com/2026/06/weil-reportedly-pays-up-to-20-million-after-hackers-steal-client-data/"
    publisher: "Legal Cheek, 2026-06-03"
    role: corroborating
  - url: "https://securityaffairs.com/193215/cyber-crime/silent-ransom-group-srg-switching-to-dns-fast-flux-infrastructure.html"
    publisher: Security Affairs — DNS fast-flux
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
migrated_from: briefs/weekly/2026-W23.md
---

Mandiant's comprehensive primary forensic analysis published 5 June ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/targeted-campaign-us-law-firms/); deep-dived [daily 2026-06-06](/briefs/2026-06-06/)) documents a January–May 2026 data-theft extortion campaign against US legal and professional-services organisations by UNC3753 (Luna Moth / Silent Ransom Group). The intrusion chain is entirely social-engineered: invoice/subscription pretext → vishing callback impersonating internal IT support → victim installs AnyDesk / Bomgar / Zoho Assist → actor enumerates file shares and document-management systems and exfiltrates in under an hour in several cases using portable WinSCP/Rclone. No ransomware, no encryption — leverage is the stolen data alone. Weil, Gotshal & Manges reportedly paid an estimated ~$20 M suppression payment ([Legal Cheek, 2026-06-03](https://www.legalcheek.com/2026/06/weil-reportedly-pays-up-to-20-million-after-hackers-steal-client-data/)). Two new in-window developments: (1) the FBI's 2026-05-26 Cyber FLASH and Mandiant both confirm operatives **entering corporate offices to insert USB exfiltration devices** when remote social engineering failed (`T1052.001`), bypassing every network-side control; (2) a 2026-06-05 report documents SRG migrating its C2 to **DNS fast-flux** infrastructure, hardening against takedown and static indicator blocking ([Security Affairs, 2026-06-05](https://securityaffairs.com/193215/cyber-crime/silent-ransom-group-srg-switching-to-dns-fast-flux-infrastructure.html)). For Swiss and European legal and professional-services firms: the IT-helpdesk-impersonation vector is identical to social-engineering pressure documented across European corporate intrusions; the physical-USB escalation raises duty-of-care questions that require physical-security response, not just SOC playbooks.
