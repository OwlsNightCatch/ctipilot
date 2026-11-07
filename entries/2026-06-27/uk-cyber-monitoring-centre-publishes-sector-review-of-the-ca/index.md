---
schema: 1
kind: incident
title: "UK Cyber Monitoring Centre publishes sector review of the Canvas/Instructure LMS breach — 160 universities, ShinyHunters extortion, ransom paid"
headline: "UK Cyber Monitoring Centre publishes sector review of the Canvas/Instructure LMS breach — 160 universities, ShinyHunters extortion, ransom paid"
summary: "The UK Cyber Monitoring Centre (CMC) published a post-incident sector review on 2026-06-25 of the April 2026 ShinyHunters (UNC6240) breach of Instructure's Canvas learning-management platform, which affected roughly 160 UK higher-education institutions (Computer Weekly, 2026-06-25)."
discovered_at: "2026-06-27T05:17:39Z"
event_date: 2026-06-25
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - supply-chain
regions:
  - uk
  - europe
sectors:
  - education
  - public-sector
entities:
  - "actor:shinyhunters"
cves: []
sources:
  - url: "https://www.computerweekly.com/news/366645159/Canvas-breach-hit-160-UK-unis-but-caused-limited-damage"
    publisher: Computer Weekly
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/cmc-analysis-education-canvas-data/"
    publisher: Infosecurity Magazine
    role: corroborating
  - url: "https://www.instructure.com/incident_update"
    publisher: Instructure incident page
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
migrated_from: briefs/2026-06-27.md
---

The UK Cyber Monitoring Centre (CMC) published a post-incident sector review on 2026-06-25 of the April 2026 **ShinyHunters** (UNC6240) breach of Instructure's Canvas learning-management platform, which affected roughly 160 UK higher-education institutions ([Computer Weekly, 2026-06-25](https://www.computerweekly.com/news/366645159/Canvas-breach-hit-160-UK-unis-but-caused-limited-damage)). Attackers exfiltrated usernames, email addresses, course/enrolment data and student IDs, then pursued extortion by publishing victim lists, disrupting LMS access and defacing virtual learning environments; Instructure reportedly paid an undisclosed sum to have the stolen data destroyed ([Computer Weekly, 2026-06-25](https://www.computerweekly.com/news/366645159/Canvas-breach-hit-160-UK-unis-but-caused-limited-damage)), though Instructure's own incident statement describes only reaching an agreement and receiving deletion logs, without confirming a monetary payment ([Instructure incident update](https://www.instructure.com/incident_update)). The CMC found no evidence of lateral movement into institutional networks but flagged residual phishing risk from the exfiltrated student/staff identity data. Its hardening recommendations are directly transferable: separate application and data layers to support clean recovery; inventory and contractually govern dependencies on offshore SaaS providers not subject to local law; and rehearse breach/business-continuity scenarios in tabletop exercises.
**Defender takeaway:** Canvas is deployed at Swiss universities, German *Hochschulen* and Austrian *Fachhochschulen*; the same exfiltrated-identity → downstream-phishing risk applies. Education-sector SOCs should treat a third-party LMS breach as a phishing-enablement event for their entire student/staff population and pre-stage user comms, not only assess data-loss scope.
