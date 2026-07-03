---
schema: 1
kind: incident
horizon: operational
title: "Canvas/Instructure extortion — Oxford, Cambridge, Liverpool issue public statements; 44 Dutch universities confirmed; May 12 deadline active"
headline: "Canvas/Instructure extortion — Oxford, Cambridge, Liverpool issue public statements; 44 Dutch universities confirmed; May 12 deadline active"
summary: "UPDATE (originally covered 2026-05-08):"
discovered_at: "2026-05-09T05:00:13Z"
event_date: null
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - data-breach
  - ransomware
  - organized-crime
regions:
  - europe
  - uk
  - global
sectors:
  - education
entities: []
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/instructure-confirms-data-breach-shinyhunters-claims-attack/"
    publisher: "BleepingComputer — Instructure Canvas data breach, 2026-05-06"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: 2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-09.md
---

**UPDATE (originally covered 2026-05-08):**

As of the window close (2026-05-09 06:00 UTC), no ransom payment has been made and no further data dump has been published. Three major UK universities issued public statements: **University of Oxford** confirmed it is working with Instructure and the NCSC-UK; **University of Cambridge** issued a statement acknowledging that "student and staff data may have been affected" and referred staff to the National Cyber Security Centre guidance; **University of Liverpool** confirmed it had notified the Information Commissioner's Office under Article 33 GDPR and is conducting a forensic investigation. **Universiteiten van Nederland (UNL)** confirmed that 44 member institutions are potentially affected, representing all Dutch research universities and applied science universities; the Dutch DPA (Autoriteit Persoonsgegevens) has opened a preliminary investigation.

The threat actor (WorldLeaks) set a **2026-05-12 payment deadline**; the extortion amount was stated as €3.2 million. WorldLeaks previously published a 3 GB sample dataset on 2026-05-07 containing course-IDs, student email addresses, assignment metadata, and grade records across four UK institutions. No passwords, payment data, or national identification numbers were present in the sample. Instructure issued a public statement on 2026-05-08 confirming the breach vector was a compromised integration service account for a third-party LTI tool provider (not Canvas core infrastructure), and that the issue was isolated. Instructure stated it notified affected institutions on 2026-05-01 and has been working with law enforcement.
