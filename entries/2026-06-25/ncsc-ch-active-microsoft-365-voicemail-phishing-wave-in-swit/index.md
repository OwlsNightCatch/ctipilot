---
schema: 1
kind: threat
title: "NCSC-CH: active Microsoft 365 \"voicemail\" phishing wave in Switzerland delivers infostealers and harvests M365 credentials"
headline: "NCSC-CH: active Microsoft 365 \"voicemail\" phishing wave in Switzerland delivers infostealers and harvests M365 credentials"
summary: "NCSC-CH flags an active Microsoft 365 \"voicemail\" phishing wave in Switzerland — Week 25 review documents dual-path ZIP-borne infostealer / fake-login credential theft against M365 tenants, with downstream BEC and chain-phishing once a mailbox is taken; the ZIP-as-audio lure is the key detection discriminator (NCSC-CH, 2026-06-23)."
discovered_at: "2026-06-25T04:59:04Z"
event_date: 2026-06-23
run_id: 2026-06-25-da7fbd23
priority: high
immediate_action: null
tags:
  - phishing
  - infostealer
  - identity
  - eu-nexus
regions:
  - switzerland
sectors:
  - public-sector
  - finance
entities: []
cves: []
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_25.html"
    publisher: "NCSC-CH Wochenrückblick Week 25"
    role: primary
closed_sources: []
evidence:
  - quote: "In one version of the scam, the attackers try to trick the victim into running malware. The email has a compressed file attached to it, for example a ZIP file called 'audio_Y6CEKNH8OE.zip'."
    publisher: NCSC-CH
  - quote: "Stolen Microsoft 365 login details give attackers access to emails, OneDrive, SharePoint and Teams... The compromised mailbox is then often used to send phishing emails to all of the victim's contacts ('chain phishing')."
    publisher: NCSC-CH
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-25.md
---

Switzerland's National Cyber Security Centre reported a higher-than-usual volume of a dual-path Microsoft 365 / OneDrive-for-Business phishing campaign in its Week 25 review ([NCSC-CH, 2026-06-23](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_25.html)). In the malware-delivery variant the email carries a ZIP "audio" attachment that, when run, installs an infostealer harvesting browser credentials, session cookies and wallet data; in the credential-harvest variant a fake Microsoft login page with a simulated audio player ("Play voicemail as guest") captures the M365 username and password. NCSC-CH notes that a compromised mailbox is then used to read live business email and run chain-phishing and BEC fraud from a recognised sender replying inside an existing thread (`T1114.003`, `T1098`), and that stolen credentials are frequently resold and resurface in targeted follow-up attacks weeks later.
**Why it matters to us:** Swiss public-sector staff are direct recipients. The discriminator is mechanical — legitimate voicemail notifications deliver `.wav`/`.mp3`, never a ZIP. Phishing-resistant MFA (FIDO2 / certificate-based Conditional Access) defeats the credential-theft path even when the lure succeeds; hunt M365 audit logs for inbox-rule and forwarding-rule creation within minutes of a sign-in from a new country/ASN.
