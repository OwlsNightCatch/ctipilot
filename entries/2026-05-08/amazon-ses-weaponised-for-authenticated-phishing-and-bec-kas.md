---
schema: 1
kind: research
horizon: operational
title: "Amazon SES weaponised for authenticated phishing and BEC (Kaspersky, 2026-05-04, ~96 h)"
headline: "Amazon SES weaponised for authenticated phishing and BEC (Kaspersky, 2026-05-04, ~96 h)"
summary: Kaspersky researchers documented a campaign technique using legitimate Amazon Simple Email Service (SES) accounts to deliver attacker-crafted phishing and business-email-compromise (BEC) lures.
discovered_at: "2026-05-08T05:00:13Z"
event_date: null
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - phishing
  - cloud
regions:
  - europe
  - global
sectors: []
entities: []
cves: []
sources:
  - url: "https://securelist.com/amazon-ses-bec-campaign-2026/"
    publisher: Kaspersky Securelist — Amazon SES BEC Campaign (2026-05-04)
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-08.md
---

Kaspersky researchers documented a campaign technique using legitimate **Amazon Simple Email Service (SES)** accounts to deliver attacker-crafted phishing and business-email-compromise (BEC) lures. Because messages originate from genuine SES infrastructure, SPF and DKIM authentication passes and messages evade most email security gateway filters based on sender reputation. Attackers obtain SES API credentials from publicly exposed AWS configuration files (S3 bucket misconfigurations, leaked GitHub repositories). Observed campaign goals include invoice-fraud lures targeting finance departments and credential phishing pages hosted on AWS infrastructure. Kaspersky observed targeting of finance departments at European manufacturing firms. This report is approximately 96 hours old at publication; first coverage in this brief series.
