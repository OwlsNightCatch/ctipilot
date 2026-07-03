---
schema: 1
kind: incident
horizon: operational
title: TechCrunch finds 100 K passport scans and selfies on a public-read S3 bucket behind a UK Visa Portal lookalike
headline: TechCrunch finds 100 K passport scans and selfies on a public-read S3 bucket behind a UK Visa Portal lookalike
summary: "TechCrunch reported on 2026-05-27 that ukvisaportal.com — a third-party site marketed as an immigration portal but not affiliated with the UK Government — exposed roughly 100,000 documents via a misconfigured Amazon S3 bucket."
discovered_at: "2026-05-29T05:00:05Z"
event_date: null
run_id: 2026-05-29-c7f56b00
priority: notable
immediate_action: null
tags:
  - data-breach
  - cloud
  - identity
regions:
  - uk
  - europe
  - switzerland
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/05/27/uk-visa-portal-spilled-thousands-of-applicants-passports-and-selfies-online-and-hasnt-fixed-the-leak/"
    publisher: TechCrunch — UK Visa Portal spilled passports and selfies
    role: primary
  - url: "https://www.techradar.com/pro/security/uk-visa-portal-website-leaks-thousands-of-user-passport-data-and-photos-online"
    publisher: TechRadar
    role: corroborating
closed_sources: []
evidence:
  - quote: "The data spill stemmed from a public Amazon-hosted storage server (also known as a bucket), which UK Visa Portal uses for hosting user-uploaded passports and selfies, with the files accessible and viewable to anyone who knew the web address of each file."
    publisher: TechCrunch
  - quote: "The website is not affiliated with the U.K. government, and some have complained that they mistakenly paid a fee to this company instead of using the official GOV.UK website."
    publisher: TechRadar
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
migrated_from: briefs/2026-05-29.md
---

TechCrunch reported on 2026-05-27 that *ukvisaportal.com* — a third-party site marketed as an immigration portal but **not affiliated with the UK Government** — [exposed roughly 100,000 documents](https://techcrunch.com/2026/05/27/uk-visa-portal-spilled-thousands-of-applicants-passports-and-selfies-online-and-hasnt-fixed-the-leak/) via a misconfigured Amazon S3 bucket. The bucket was not publicly listed, but a backend bug exposed directory listing, enabling enumeration of every object; individual files were readable to anyone with the URL. Exposed material included full passport pages (passport number, nationality, DOB, place of birth, issue / expiry dates), accompanying address documents and selfie photographs whose **EXIF GPS metadata** could pinpoint the applicant's home address. The operator — UAE-registered *Active Leadgen LLC* — marketed under brand names including "UK Visit" and "ETA-Pass" and impersonated the official GOV.UK service; some applicants told TechCrunch they paid fees believing it was the genuine government portal. TechCrunch and [TechRadar](https://www.techradar.com/pro/security/uk-visa-portal-website-leaks-thousands-of-user-passport-data-and-photos-online) report the bucket was secured overnight after publication; no ICO breach notification has surfaced in-window.

**Defender takeaway:** the lookalike-government-service pattern matters operationally even outside immigration. Where the public-sector security team is responsible for citizen-facing brand integrity (federal / cantonal IT, KAPO digital-services teams), the relevant action is to scan for lookalike domains and S3 / blob buckets carrying passport / ID-document keys — Trufflehog-style scanning of cloud-storage namespaces for `passport`, `national-id`, `eta` filename patterns. EU residents who used the service trigger UK GDPR Art. 33 notification on the operator's side.
