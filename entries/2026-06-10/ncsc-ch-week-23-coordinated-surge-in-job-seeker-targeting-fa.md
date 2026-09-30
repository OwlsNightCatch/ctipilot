---
schema: 1
kind: threat
title: "NCSC-CH Week 23: three job-seeker scams, a fake interview login, reshipping identity theft and LinkedIn-to-GitHub infostealer delivery"
headline: "NCSC-CH Week 23: three job-seeker scams, a fake interview login, reshipping identity theft and LinkedIn-to-GitHub infostealer delivery"
summary: "NCSC Switzerland's Week 23 review (9 June) describes three reported cases aimed at job seekers: an interview slot confirmed through a Google Calendar entry that opens a counterfeit Google login and harvests the credentials, a fake \"Swiss social welfare\" packing job that collects identity documents for reshipping and purchase fraud, and a fake LinkedIn recruiter whose technical interview has the candidate run a small programming task from a private GitHub repository, which installs an infostealer."
discovered_at: "2026-06-10T05:00:02Z"
event_date: 2026-06-09
run_id: 2026-06-10-c84347b2
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
  - identity
  - organized-crime
regions:
  - switzerland
sectors: []
entities:
  - "campaign:ncsc-ch-jobseeker-targeting-2026"
techniques: [T1566.002, T1566.003, T1586.001, T1204.002, T1555, T1539]
cves: []
sources:
  - url: "https://www.bacs.admin.ch/en/26w23-en"
    publisher: "NCSC-CH, 2026-06-09"
    role: primary
closed_sources: []
evidence: []
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
      NCSC presents three reported cases rather than a coordinated campaign, and none of the
      Swiss-employer emails, onboarding repository or PowerShell the analysis described, so the title,
      summary and analysis now follow the page. The citation follows the page to its new address on
      bacs.admin.ch.
    fields: [sources, techniques, classification, title, headline, summary, sectors, body]
migrated_from: briefs/2026-06-10.md
---

NCSC Switzerland's Week 23 review (9 June) walks through three reported cases aimed at job seekers ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). In the first, a job seeker was offered a phone-interview slot to confirm through a Google Calendar entry, and the confirmation opened a counterfeit Google login that sent the entered credentials to the scammers. In the second, an ad for a "Swiss social welfare" work-from-home packing job moved to WhatsApp and asked for photos of the passport, identity card, driving licence and home address. Such documents are used to order high-value goods in the victim's name, and the job itself is parcel reshipping that hides criminal proceeds. In the third, a recruiter on LinkedIn, in one case writing from a compromised but genuine-looking profile, offered a technical position and, as part of a technical interview, asked the candidate to download a private GitHub repository and complete a small programming task in it. Running the commands installed an infostealer that reads crypto wallets, stored login credentials and browser cookies. NCSC notes that attackers systematically exploit applicants' willingness to react quickly and engage with unfamiliar procedures.

**Why it matters to us:** the LinkedIn-to-GitHub chain is a credible vector into corporate endpoints through employees in job-search mode and HR or talent teams handling external candidate code. Detection concept, by inference from the mechanism: a repository clone or GitHub download followed within minutes by script execution from the freshly cloned path (process-creation telemetry, for example Sysmon event 1 with `git` or an interpreter as the parent).

## Correction — 2026-09-30T06:43:01Z

NCSC Switzerland's Week 23 review presents three reported cases, not a coordinated campaign ([NCSC-CH, 2026-06-09](https://www.bacs.admin.ch/en/26w23-en)). The fake interview was a phone-interview slot confirmed through a Google Calendar entry, which opened a counterfeit Google login. The recruiter case was a technical interview in which the candidate downloaded a private GitHub repository and ran a small programming task, and running its commands installed the infostealer. The analysis had described interview-confirmation emails from Swiss employers, an onboarding or technical-assessment repository and PowerShell, which the page does not say, and it now follows the page. The citation now points at the page's new address on bacs.admin.ch, after the old ncsc.admin.ch page went dead.
