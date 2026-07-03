---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "UK Visa Portal — ~100,000 passport scans and selfies on a public-read S3 bucket behind a government-lookalike site"
headline: "UK Visa Portal — ~100,000 passport scans and selfies on a public-read S3 bucket behind a government-lookalike site"
summary: "TechCrunch found ~100,000 passport scans and applicant selfies exposed on a public-read Amazon S3 bucket used by \"UK Visa Portal,\" a site not affiliated with the UK government that some applicants mistook for the official GOV.UK service; the leak was unfixed at time of reporting (2026-05-29)."
discovered_at: "2026-05-25T05:00:16Z"
event_date: 2026-05-29
run_id: 2026-W22-da77963d
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
    publisher: TechCrunch — UK Visa Portal leak
    role: primary
  - url: "https://www.techradar.com/pro/security/uk-visa-portal-website-leaks-thousands-of-user-passport-data-and-photos-online"
    publisher: TechRadar
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
migrated_from: briefs/weekly/2026-W22.md
---

TechCrunch found ~100,000 passport scans and applicant selfies exposed on a **public-read Amazon S3 bucket** used by "UK Visa Portal," a site not affiliated with the UK government that some applicants mistook for the official GOV.UK service; the leak was unfixed at time of reporting ([2026-05-29](/briefs/2026-05-29/)). The defender double-lesson: the technical failure is the oldest cloud-storage misconfiguration in the book (object-level public read on a sensitive bucket), and the social failure is the government-service-lookalike that harvested real identity documents from people who believed they were on an official portal — a brand-protection and citizen-awareness problem for the genuine public-sector body whose service is being impersonated. CH/EU public bodies should monitor for lookalike service domains and re-confirm that no applicant-document storage is world-readable.
