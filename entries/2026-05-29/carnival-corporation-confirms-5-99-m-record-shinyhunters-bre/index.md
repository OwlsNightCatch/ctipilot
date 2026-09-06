---
schema: 1
kind: incident
title: "Carnival Corporation confirms 5.99 M-record ShinyHunters breach — passport + driver's-licence numbers exposed across four cruise brands"
headline: "Carnival Corporation confirms 5.99 M-record ShinyHunters breach — passport + driver's-licence numbers exposed across four cruise brands"
summary: "Carnival Corporation files substitute notices confirming a breach affecting 5,995,277 individuals (Maine AG filing; driver's-licence + passport numbers exposed across Princess / Holland America / Cunard / Costa per The Record). Maine AG records the breach occurring 2026-04-10 and discovered 2026-04-14 (single-employee-account social engineering); ShinyHunters claimed and ultimately published when ransom was refused."
discovered_at: "2026-05-29T05:00:03Z"
event_date: 2026-05-27
run_id: 2026-05-29-c7f56b00
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
regions:
  - us
  - europe
  - uk
sectors:
  - retail
  - transport
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.prnewswire.com/news-releases/carnival-corporation-notice-of-data-breach-302783524.html"
    publisher: Carnival Corporation — Notice of Data Breach
    role: primary
  - url: "https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/d6729ef2-7bb3-42d3-abdd-99a1dd8f2415.html"
    publisher: Maine Attorney General data-breach filing
    role: corroborating
  - url: "https://therecord.media/cruise-giant-carnival-confirms-data-breach-affecting-6-million"
    publisher: The Record
    role: corroborating
  - url: "https://www.theregister.com/cyber-crime/2026/05/28/carnival-shinyhunters-cruised-off-with-6m-customer-records/5247808"
    publisher: The Register
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/28/carnival-corporation-data-breach/"
    publisher: Help Net Security
    role: corroborating
closed_sources: []
evidence:
  - quote: "On April 14, 2026, our IT security team identified unauthorized activity involving an employee's account, when an unauthorized actor used social engineering to deceive an employee to gain access to a limited portion of the company's IT system."
    publisher: Carnival Corporation PR Newswire official notice
  - quote: The company said the threat actor gained access to a limited portion of its IT environment last month after compromising an employee account.
    publisher: The Record
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

Carnival Corporation [filed substitute notices with state attorneys-general on 2026-05-27](https://www.prnewswire.com/news-releases/carnival-corporation-notice-of-data-breach-302783524.html) confirming **5,995,277 individuals** were affected across Princess Cruises, Holland America Line, Cunard and Costa Cruises — the precise figure is from the [Maine Attorney General data-breach filing](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/d6729ef2-7bb3-42d3-abdd-99a1dd8f2415.html), with secondary coverage in [The Record](https://therecord.media/cruise-giant-carnival-confirms-data-breach-affecting-6-million) and [The Register](https://www.theregister.com/cyber-crime/2026/05/28/carnival-shinyhunters-cruised-off-with-6m-customer-records/5247808). The Register notes that this is materially lower than the 8.7 million records ShinyHunters originally listed against Carnival on Have I Been Pwned — the 5.99 million is the count of *individuals* with unique notifications, not the row-count of the exfiltrated database, so defender-exposure scope discussions need to distinguish the two. The [Maine AG filing](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/d6729ef2-7bb3-42d3-abdd-99a1dd8f2415.html) records the breach as occurring 2026-04-10 and discovered on 2026-04-14 (PR Newswire's official notice describes 2026-04-14 as the day the security team *identified* the unauthorized activity); initial access was social engineering against a single employee account. ShinyHunters claimed responsibility on 2026-04-18 and ultimately published the data when the ransom demand was refused. Exposed fields include full name, address, email, phone, date of birth and state-issued ID numbers (driver's-licence and passport numbers). Costa Cruises is Italy-headquartered and Cunard has UK operations — EU-resident passport data is in scope, but no EU DPA notification has surfaced in-window. This is a separate ShinyHunters event from the previously-covered Charter / 7-Eleven Salesforce campaign ([covered 2026-05-25](/briefs/2026-05-25/) and [2026-05-27](/briefs/2026-05-27/)); the common pattern is single-account social-engineering footholds and the pay-or-leak extortion model run from the actor's own portal.

**Defender takeaway:** the kill chain is single-account-social-engineering → bulk data access — no CVE exploitation. For travel / hospitality and public-sector SOCs, focus user-behaviour-analytics rules on anomalous bulk data access by a single user / session (T1530, T1213.003) and on outbound transfer volume from CRM and ID-document repositories. EU GDPR notifications from the Italian (Costa) and UK (Cunard) subsidiaries are the immediate regulatory beat to watch.
