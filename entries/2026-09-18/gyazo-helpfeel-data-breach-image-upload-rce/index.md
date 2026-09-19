---
schema: 1
kind: incident
title: "Gyazo (Helpfeel): an image-upload-server vulnerability reaches arbitrary command execution, exposing 23.62 million user records and 490 million image-metadata records"
headline: "Helpfeel's 'unguessable link' privacy model for Gyazo collapsed once the image IDs themselves leaked from the backend"
summary: >
  Helpfeel Inc. disclosed on 2026-09-16 that a third party exploited a vulnerability in Gyazo's
  image-upload server to execute arbitrary commands and reach its database, exposing roughly
  23.62 million user records and 490 million image-metadata records including the identifiers
  needed to access "private" images; no CVE or flaw class was named.
discovered_at: "2026-09-18T05:00:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-09-18T0410Z-intel
priority: notable
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
  Helpfeel's own incident notice is the primary source under the victim-disclosure carve-out
  (PD-5); The Hacker News's reporting relays rather than independently investigates the incident.
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
updates: []
migrated_from: null
---

Helpfeel Inc. (Kyoto, Japan) disclosed on 2026-09-16 that a third party exploited a vulnerability in the image-upload server of Gyazo, its screenshot-sharing service, on 2026-09-11, gaining unauthorized system access and the ability to execute arbitrary commands, then reaching Gyazo's database ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)); Helpfeel has not named the flaw class or assigned a CVE. Roughly 23.62 million user records were exposed — name, email, password hash, user ID, device ID, login-session ID, X/Google SSO tokens, profile data, language preference, registration and last-login timestamps, subscription plan and billing status, excluding payment-card numbers — plus roughly 490 million image-metadata records, mostly pre-2019, and metadata for a further 2.4 million images, including a link built from a 32-character image ID used to construct the access URL ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)), plus upload IP, User-Agent, EXIF location data, OCR-extracted text, and a hashed passphrase for password-protected private images ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)). Gyazo's default privacy setting for an image relies entirely on the image ID in its URL staying secret, distinct from the stricter "Only me" or password-protected settings ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)); the leaked IDs directly defeat the default setting, and Helpfeel confirms the attacker also obtained a list identifying which images were marked private, so it "cannot rule out" unauthorized viewing of private content ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)). Helpfeel's own public status page described the outage only as "emergency maintenance" on September 14 and 15 and did not disclose a breach until the September 16 notice, filing a report with Japan's Personal Information Protection Commission the day before ([The Hacker News, 2026-09-17](https://thehackernews.com/2026/09/gyazo-breach-exposes-2362-million-user.html)). Helpfeel's other two products, Helpfeel and Cosense, run on separate infrastructure and were not found to have any unauthorized data disclosure ([Helpfeel Inc., 2026-09-16](https://corp.helpfeel.com/en/news/news-20260916)).

**Defender takeaway:** an access-control model built on a long, unguessable identifier staying secret collapses entirely once the identifiers themselves leak from the backend, rather than from a shared link — any internal system relying on ID secrecy rather than an authorization check should be treated as fully exposed once any store of those IDs is breached, and the same incident is worth using to check whether your own status-page incident-communication practice could produce the same appearance of understating a security event.
