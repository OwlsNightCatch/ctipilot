---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "ShinyHunters Salesforce campaign — 40+ listed victims; Canada Life and Pitney Bowes confirm; the BreachForums extortion channel was previously seized"
headline: "ShinyHunters Salesforce campaign — 40+ listed victims; Canada Life and Pitney Bowes confirm; the BreachForums extortion channel was previously seized"
summary: "Complementing the § 2 victim arc, horizon research confirms the campaign now lists 40+ confirmed or claimed victims (key: item:shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c), with Canada Life (insurance carrier, UK/Ireland) and Pitney Bowes confirming breaches in the window, and …"
discovered_at: "2026-05-25T05:00:22Z"
event_date: null
run_id: 2026-W22-da77963d
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
regions:
  - us
  - uk
  - europe
sectors:
  - finance
  - education
  - retail
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/fbi-takes-down-breachforums-portal-used-for-salesforce-extortion/"
    publisher: BleepingComputer — FBI seizes BreachForums extortion portal
    role: primary
  - url: "https://www.scworld.com/brief/multiple-other-companies-purportedly-breached-by-shinyhunters-over-9m-record-leak-warned"
    publisher: SC Media — expanded victim list
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

Complementing the § 2 victim arc, horizon research confirms the campaign now lists **40+ confirmed or claimed victims** (`key: item:shinyhunters-salesforce-campaign-charter-and-7-eleven-both-c`), with **Canada Life** (insurance carrier, UK/Ireland) and **Pitney Bowes** confirming breaches in the window, and Canvas/Instructure reported to have paid ransom on 2026-05-12. The relevant law-enforcement context: the FBI and France's BL2C previously seized the ShinyHunters-operated BreachForums portal that served as the campaign's extortion channel (2025-10-10), which briefly interrupted operations before the group rebuilt — a reminder that channel seizures slow but do not stop a credential-extortion operation with this many active victims. No leadership arrests. The unchanged defender action is connected-app OAuth-scope and refresh-token review.
