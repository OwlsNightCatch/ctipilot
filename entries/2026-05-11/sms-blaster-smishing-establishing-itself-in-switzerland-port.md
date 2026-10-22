---
schema: 1
kind: threat
title: "SMS-blaster smishing in Switzerland: fake base stations push phones onto 2G and send spoofed texts past operator filters"
headline: "SMS blasters in Switzerland force nearby phones onto 2G to deliver spoofed phishing texts that bypass operator filters"
summary: "BACS reported in September 2025 that fake parking-fine texts in western Switzerland were being sent with SMS blasters, portable fake base stations that pull phones within 500 to 1,000 metres onto 2G and deliver texts with spoofed senders past the operators' SMS filters; Basel-Landschaft police arrested a suspect with such a device in November 2025. The awareness portal ebas.ch warned on 2026-05-07 that the scam is establishing itself in Switzerland, with lures posing as authorities, banks or couriers that link to fake sites collecting card data and e-banking credentials."
discovered_at: "2026-05-11T05:00:01Z"
event_date: 2026-05-07
run_id: 2026-05-11-migrated
priority: notable
immediate_action: null
tags:
  - phishing
  - mobile
  - organized-crime
regions:
  - switzerland
sectors:
  - finance
  - public-sector
entities:
  - "campaign:sms-blaster-ch-2026"
techniques: [T1566.002, T1598.003]
affected_products: []
cves: []
sources:
  - url: "https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/"
    publisher: "ebas.ch"
    date: "2026-05-07"
    role: primary
  - url: "https://www.bacs.admin.ch/en/25w36-en"
    publisher: "BACS (Federal Office for Cybersecurity), week 36 review"
    date: "2025-09-09"
    role: primary
  - url: "https://www.srf.ch/news/schweiz/seltener-fahndungserfolg-baselbieter-polizei-schnappt-mutmasslichen-sms-betrueger"
    publisher: "SRF"
    date: "2025-11-13"
    role: corroborating
  - url: "https://developer.android.com/reference/android/os/UserManager"
    publisher: "Android Developers (UserManager reference)"
    role: corroborating
closed_sources: []
evidence:
  - quote: "One person who reported a case provided another valuable clue: shortly before receiving the text message, their smartphone switched from the 4G network to the older 2G standard."
    publisher: "BACS (Federal Office for Cybersecurity), week 36 review"
    source_url: "https://www.bacs.admin.ch/en/25w36-en"
  - quote: "The SMS blaster emits a strong signal that prompts all smartphones within a radius of 500 to 1,000 metres to connect to it."
    publisher: "BACS (Federal Office for Cybersecurity), week 36 review"
    source_url: "https://www.bacs.admin.ch/en/25w36-en"
  - quote: "This bypasses the operator’s SMS filters, leaving only the filters installed on the device itself (if any)."
    publisher: "BACS (Federal Office for Cybersecurity), week 36 review"
    source_url: "https://www.bacs.admin.ch/en/25w36-en"
  - quote: "The suspect had an SMS blaster in his car. (translated from German)"
    original: "Der Verdächtige hatte in seinem Auto einen SMS-Blaster."
    publisher: "SRF"
    source_url: "https://www.srf.ch/news/schweiz/seltener-fahndungserfolg-baselbieter-polizei-schnappt-mutmasslichen-sms-betrueger"
  - quote: "As many smartphones keep on supporting 2G, even modern devices might potentially be affected."
    publisher: "ebas.ch"
    source_url: "https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/"
  - quote: "This restriction can only be set by a device owner or a profile owner of an organization-owned managed profile on the parent profile."
    publisher: "Android Developers (UserManager reference)"
    source_url: "https://developer.android.com/reference/android/os/UserManager"
verification: multi-source
sourcing_note: >
  BACS reported the Swiss SMS-blaster cases in September 2025 from reports it received, SRF independently reported a police arrest
  with a device in November 2025, and the ebas.ch post of 2026-05-07 restates the threat as awareness guidance.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-11.md
updates:
  - at: "2026-10-21T20:36:37Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      BACS had already reported SMS-blaster smishing in western Switzerland in September 2025, and
      Basel-Landschaft police arrested a suspect with a device in November 2025, so ebas.ch's May 2026
      post is a later awareness note rather than the only Swiss source. On managed Android devices 2G is
      blocked with the DISALLOW_CELLULAR_2G restriction from API level 34, set by a device owner, not
      through the TelephonyManager call; the user-visible sign is the brief switch from 4G to 2G that BACS
      describes.
    fields: [affected_products, body, classification, evidence, headline, priority, sources, sourcing_note, summary, techniques, title, verification]
---

BACS reported on 2025-09-09 that numerous fake parking-fine texts were reaching people in western Switzerland who had recently been in the places mentioned, and that one recipient's phone switched from 4G to 2G just before the message arrived, pointing to an SMS blaster ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)). The device builds on IMSI-catcher technology: it poses as the best available mobile mast within a radius of 500 to 1,000 metres, forces connecting phones onto the outdated 2G standard and sends texts with forged sender information directly to the handset, bypassing the operator's SMS filters ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)). In November 2025 Basel-Landschaft police arrested a suspect who had an SMS blaster in his car ([SRF, 2025-11-13](https://www.srf.ch/news/schweiz/seltener-fahndungserfolg-baselbieter-polizei-schnappt-mutmasslichen-sms-betrueger)). On 2026-05-07 the awareness portal ebas.ch warned that the scam is establishing itself in Switzerland, with texts posing as authorities, banks or courier services that link to fake websites collecting credit card data or e-banking credentials and are adapted to the location, such as a parking fine where many cars are parked ([ebas.ch, 2026-05-07](https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/)).

**Exposure:** any phone in range that still connects to 2G, which includes many modern smartphones; only SMS is affected, not services such as WhatsApp, Signal or Telegram ([ebas.ch, 2026-05-07](https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/)).

**Detection:** handset network state as users report it: the phone drops from 4G to 2G shortly before the scam text arrives and returns to 4G immediately afterwards ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)); the sender number is spoofed and cannot be verified or blocked ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)).

**Defender takeaway:** on managed Android devices at API level 34 (Android 14) or later, a device owner or the owner of an organisation-owned managed profile can block 2G for the whole device with the DISALLOW_CELLULAR_2G restriction, and emergency calls still use 2G ([Android Developers](https://developer.android.com/reference/android/os/UserManager)); iPhones cannot disable 2G directly, only through Lockdown Mode, which also limits other functions ([ebas.ch, 2026-05-07](https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/)).

## Correction — 2026-10-21T20:36:37Z

The Swiss signal predates the ebas.ch post: BACS reported in September 2025 that fake parking-fine texts in western Switzerland were being sent with SMS blasters ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)), and Basel-Landschaft police arrested a suspect with such a device in his car in November 2025 ([SRF, 2025-11-13](https://www.srf.ch/news/schweiz/seltener-fahndungserfolg-baselbieter-polizei-schnappt-mutmasslichen-sms-betrueger)). Blocking 2G on managed Android devices uses the DISALLOW_CELLULAR_2G user restriction, available from API level 34 and settable only by a device owner or the owner of an organisation-owned managed profile ([Android Developers](https://developer.android.com/reference/android/os/UserManager)), not an Android 12 network-type call. The observable BACS describes is the handset itself switching from 4G to 2G just before the scam text and back to 4G afterwards ([BACS, 2025-09-09](https://www.bacs.admin.ch/en/25w36-en)); no cited source documents mobile-management products surfacing that switch.
