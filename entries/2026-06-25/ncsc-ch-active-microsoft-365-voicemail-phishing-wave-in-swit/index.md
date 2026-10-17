---
schema: 1
kind: threat
title: "NCSC-CH: Microsoft 365 \"voicemail\" phishing wave delivers malware such as infostealers and harvests M365 credentials"
headline: "NCSC-CH: Microsoft 365 \"voicemail\" phishing wave delivers malware such as infostealers and harvests M365 credentials"
summary: "NCSC-CH received a higher than usual number of reports of a Microsoft 365 \"voicemail\" phishing wave: its Week 25 review documents a ZIP attachment that installs malware such as an infostealer and a fake login page that steals M365 credentials, with downstream BEC and chain-phishing once a mailbox is taken. The ZIP-as-audio lure is the key detection discriminator (NCSC-CH, 2026-06-23)."
discovered_at: "2026-06-25T04:59:04Z"
event_date: 2026-06-23
run_id: 2026-06-25-da7fbd23
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
  - identity
  - eu-nexus
regions:
  - switzerland
sectors: []
entities: ["campaign:ncsc-ch-m365-voicemail-phishing-week25"]
techniques: [T1566.001, T1566.002, T1204.002, T1555, T1539, T1078.004, T1114.002]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/en/26w25-en"
    publisher: "NCSC-CH, Week 25 review"
    role: primary
closed_sources: []
evidence:
  - quote: "In one version of the scam, the attackers try to trick the victim into running malware."
    publisher: NCSC-CH
  - quote: "The email has a compressed file attached to it"
    publisher: NCSC-CH
  - quote: "Stolen Microsoft 365 login details give attackers access to emails, OneDrive, SharePoint and Teams"
    publisher: NCSC-CH
  - quote: "The compromised mailbox is then often used to send phishing emails to all of the victim’s contacts (\"chain phishing\")."
    publisher: NCSC-CH
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
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
  - at: "2026-09-30T06:43:01Z"
    run_id: 2026-09-30T0634Z-audit
    type: correction
    summary: >
      NCSC does not describe forwarding rules or account manipulation, says genuine voicemails are
      usually rather than never audio files and harvested data may rather than frequently be resold,
      names no sector and gives the infostealer only as an example of the malware, so the title and
      analysis now follow the page and the entry moves from high to notable priority. The citation follows the page to its new address on bacs.admin.ch.
    fields: [sources, evidence, techniques, classification, title, headline, summary, priority, sectors, entities, body]
migrated_from: briefs/2026-06-25.md
---

Switzerland's National Cyber Security Centre received a higher-than-usual number of reports about a dual-path Microsoft 365 / OneDrive-for-Business phishing campaign, its Week 25 review says ([NCSC-CH, 2026-06-23](https://www.bacs.admin.ch/en/26w25-en)). In the malware-delivery variant the email carries a ZIP "audio" attachment, and running its contents installs malware, such as an infostealer, that can harvest login details, cookies or wallet information. In the credential-harvest variant a fake Microsoft login page with a simulated audio player ("Play voicemail as guest") captures the M365 username and password. The link in the notification, or an HTML file attached to it, leads to that page. NCSC-CH notes that a compromised mailbox is then often used to send phishing to all of the victim's contacts ("chain phishing"), that the attackers read business communications to prepare CEO fraud and business email compromise from a real employee's address, and that data an infostealer harvests may also be resold and in some cases resurfaces weeks or months later.

**Why it matters to us:** The discriminator is mechanical: genuine voicemail notifications are usually audio files such as `.wav` or `.mp3`, not ZIP archives. In analyst judgement, phishing-resistant MFA (FIDO2 / certificate-based Conditional Access) blocks the fake-login path even when the lure succeeds, though not a session cookie an infostealer has already taken. By inference from the mailbox monitoring NCSC-CH describes, hunt M365 audit logs for mailbox access from a new country or ASN shortly after a sign-in, and for inbox or forwarding rules created in that session.

## Correction — 2026-09-30T06:43:01Z

NCSC Switzerland's Week 25 review describes what attackers do with a compromised mailbox: they send phishing to the victim's contacts ("chain phishing") and read business communications to prepare CEO fraud and business email compromise ([NCSC-CH, 2026-06-23](https://www.bacs.admin.ch/en/26w25-en)). It does not describe forwarding rules or account manipulation, which the analysis had mapped. It also says genuine voicemails are usually sent as audio files rather than ZIP archives, and that data an infostealer harvests may be resold, where the analysis had said never and frequently. The analysis now follows the page, and the hunt for inbox and forwarding rules is marked as an inference from the mailbox monitoring NCSC describes. NCSC gives the infostealer only as an example of the malware the ZIP installs, and it names no sector and no Swiss public-sector recipients, so the title and analysis now say so and the entry's priority is notable rather than high. The citation now points at the page's new address on bacs.admin.ch, after the old ncsc.admin.ch page went dead.
