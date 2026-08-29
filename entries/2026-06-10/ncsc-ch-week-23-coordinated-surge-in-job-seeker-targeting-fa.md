---
schema: 1
kind: threat
title: "NCSC-CH Week 23: coordinated surge in job-seeker targeting — fake interviews, reshipping identity theft, and LinkedIn-to-GitHub infostealer delivery"
headline: "NCSC-CH Week 23: coordinated surge in job-seeker targeting — fake interviews, reshipping identity theft, and LinkedIn-to-GitHub infostealer delivery"
summary: "NCSC Switzerland's Week 23 report (9 June) documents three concurrent technique chains aimed at job seekers in Switzerland (NCSC-CH, 2026-06-09). The first sends fake interview-confirmation emails for plausible Swiss employers, linking to a counterfeit Google login that harvests credentials (T1566.002, T1078)."
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
sectors:
  - public-sector
entities:
  - "campaign:ncsc-ch-jobseeker-targeting-2026"
cves: []
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_23.html"
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
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-10.md
---

NCSC Switzerland's Week 23 report (9 June) documents three concurrent technique chains aimed at job seekers in Switzerland ([NCSC-CH, 2026-06-09](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_23.html)). The first sends fake interview-confirmation emails for plausible Swiss employers, linking to a counterfeit Google login that harvests credentials (T1566.002, T1078). The second uses fraudulent job offers demanding identity documents for "onboarding," with stolen Swiss IDs then used to order goods and run parcel-reshipping (freight-forwarder) fraud. The third operates through compromised LinkedIn recruiter profiles that direct candidates to download a "technical assessment" or "onboarding" GitHub repository carrying infostealer malware that targets crypto wallets, browser cookies and saved credentials (T1566.003, T1059.001, T1555). NCSC notes attackers systematically exploit applicants' urgency and unfamiliarity with new-employer processes to lower vigilance.

**Why it matters to us:** the LinkedIn→GitHub chain is a credible vector into corporate endpoints via employees in job-search mode and HR/talent teams handling external candidate code. Detection signal: `git clone` / GitHub downloads followed by script execution minutes after a LinkedIn contact (Sysmon EID 1, parent `git.exe` / `python.exe` from a freshly-cloned path). This is a national-CERT primary disclosure for its own jurisdiction.
