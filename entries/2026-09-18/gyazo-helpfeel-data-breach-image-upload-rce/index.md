---
schema: 1
kind: incident
title: "Gyazo (Helpfeel): an image-upload-server vulnerability reaches arbitrary command execution, exposing 23.62 million user records and 490 million image-metadata records"
headline: "Helpfeel's 'unguessable link' privacy model for Gyazo collapsed once the image IDs themselves leaked from the backend"
summary: >
  Helpfeel Inc. disclosed on 2026-09-16 that a third party exploited a vulnerability in Gyazo's
  image-upload server to execute arbitrary commands and reach its database, exposing roughly 23.62
  million user records and 490 million image-metadata records, including the image IDs used to build
  Gyazo image links, which Helpfeel says could be used to view the images without authorization. No
  CVE or flaw class was named.
discovered_at: "2026-09-18T05:00:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-09-18T0410Z-intel
priority: routine
immediate_action: null
tags: [data-breach]
regions: [global, apac]
sectors: [technology]
entities: ["incident:gyazo-helpfeel-data-breach-2026-09"]
techniques: [T1190]
affected_products: ["Gyazo"]
cves: []
sources:
  - url: "https://corp.helpfeel.com/en/news/news-20260916"
    publisher: "Helpfeel Inc."
    date: "2026-09-16"
    role: primary
  - url: "https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html"
    publisher: "The Hacker News"
    date: "2026-09-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On September 11, 2026, a third party exploited a vulnerability in Gyazo's image upload server to gain unauthorized access to our systems and execute arbitrary commands."
    publisher: "Helpfeel Inc."
    source_url: "https://corp.helpfeel.com/en/news/news-20260916"
  - quote: "We have also confirmed that the third party obtained a list identifying private images. As we cannot rule out the possibility that some private images may have been viewed by the third party, we are continuing our detailed investigation."
    publisher: "Helpfeel Inc."
    source_url: "https://corp.helpfeel.com/en/news/news-20260916"
verification: single-source-victim
sourcing_note: >
  Helpfeel's own incident notice is the primary source, as the victim's disclosure of its own
  breach. The Hacker News relays rather than independently investigates the incident.
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
updates:
  - at: "2026-09-20T13:28:45Z"
    run_id: 2026-09-20T1308Z-audit
    type: improvement
    summary: >
      The sourcing note carried an internal policy-reference code in reader-facing text. It now names the
      victim-disclosure carve-out in plain language. No sourcing or factual claim changes.
    fields: [sourcing_note]
    internal: true
  - at: "2026-09-30T06:56:00Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: a Japanese consumer image-hosting breach with
      no product or technique relevant to Swiss public bodies, so it is awareness only, and the main
      text is shortened to the breach, the exposure that matters and Helpfeel's guidance to users.
      The exposed user fields follow Helpfeel's list, which names an X integration token and the
      Google sign-on email address rather than SSO tokens. The summary no longer calls the affected
      images private: captures on the default setting are protected only by their link, so the leaked image IDs remove that protection.
    fields: [priority, sourcing_note, body, summary]
migrated_from: null
---

Helpfeel Inc. (Kyoto, Japan) disclosed on 2026-09-16 that on 2026-09-11 a third party exploited a vulnerability in the image-upload server of Gyazo, its screenshot-sharing service, executed arbitrary commands and accessed Gyazo's database ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)). Helpfeel has not named the flaw class ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)). About 23.62 million user records were exposed, including email addresses, password hashes and login session IDs, together with about 490 million image-metadata records, mostly for images registered in or before January 2019, that include the image IDs used to build Gyazo image links ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)). A capture at Gyazo's default setting is protected only by its link, so the leaked image IDs remove that protection ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)). Helpfeel says the attacker also obtained a list identifying private images and that it cannot rule out that some of them were viewed ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)).

**Defender takeaway:** where staff shared screenshots through Gyazo links, treat captures at the default setting as possibly viewed, since Helpfeel says the leaked image IDs could be used to view the corresponding images without authorization. Helpfeel asks every Gyazo user to change their password, and any same or similar password used on other services, and to watch for suspicious emails or messages related to the incident ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)).

## Correction — 2026-09-30T06:56:00Z

Helpfeel lists an X (formerly Twitter) integration token and the email address associated with Google single sign-on among the exposed user fields, not a Google SSO token ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)). For a capture at Gyazo's default setting, the link is the only protection, so the leaked image IDs remove it. Captures set to "Only me" cannot be viewed even by someone who knows the link, according to Gyazo's help pages as reported by The Hacker News ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)).
