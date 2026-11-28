---
schema: 1
kind: incident
title: "Nozomi Networks/CBC: Winnipeg's largest hospital network loses HVAC and door-access central monitoring to a ransomware incident with no named actor, access vector, or ransomware family disclosed 18 days later"
headline: "IT/OT segmentation held for patient care, but the hospital's own building-management network was one ransomware incident from a ventilation failure"
summary: >
  Manitoba's Shared Health disclosed that Winnipeg's Health Sciences Centre and CancerCare
  Manitoba were hit by a ransomware incident affecting facility maintenance systems, including
  HVAC and door-access controls. Central HVAC monitoring was lost and physical ID-card issuance
  stopped, while clinical systems stayed unaffected — credited by Nozomi Networks to IT/OT
  segmentation holding. No actor, vector or ransomware family has been named 18 days on.
discovered_at: "2026-08-28T06:48:00Z"
updated_at: null
event_date: "2026-08-10"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, ot-ics, data-breach]
regions: [us]
sectors: [healthcare]
entities: [incident:winnipeg-health-sciences-centre-ransomware-2026-08]
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.nozominetworks.com/blog/when-ransomware-turns-off-the-hvac-lessons-from-the-winnipeg-hospital-incident"
    publisher: "Nozomi Networks"
    date: "2026-08-12"
    role: primary
  - url: "https://www.cbc.ca/news/canada/manitoba/health-sciences-centre-ransomware-hack-9.7302058"
    publisher: "CBC News"
    date: "2026-08-10"
    role: primary
  - url: "https://www.cbc.ca/news/canada/manitoba/winnipeg-hsc-ransomware-cyberattack-9.7310005"
    publisher: "CBC News (The Canadian Press)"
    date: "2026-08-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Shared Health, the Canadian province's health authority, confirmed that Winnipeg's Health Sciences Centre (HSC) was responding to \"a ransomware incident affecting certain facility maintenance systems, including HVAC and door access controls.\""
    publisher: "Nozomi Networks"
  - quote: "Clinical services continue uninterrupted, and based on the investigation conducted to date, there is no indication that patients have been affected."
    publisher: "Shared Health (via CBC News)"
  - quote: "The health authority says its investigation has found the attack has affected central monitoring of its heating, ventilation and cooling systems but that they are still operating and being monitored locally."
    publisher: "CBC News (The Canadian Press), reporting Shared Health's update"
verification: multi-source
sourcing_note: >
  Nozomi Networks' technical analysis and CBC News's direct reporting of Shared Health's own
  statements are independent, corroborating primaries. No actor, ransomware family or access
  vector has been named by Shared Health as of the most recent update (2026-08-17) or by this
  run's own re-check; only the confirmed encryption/impact outcome is mapped — no source
  supports an access-vector claim.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [sourcing_note, body]
migrated_from: null
---

Manitoba's provincial health authority, Shared Health, disclosed on 2026-08-10 that Winnipeg's Health Sciences Centre (the province's largest hospital) and CancerCare Manitoba were hit by "a ransomware incident affecting certain facility maintenance systems, including HVAC and door access controls" ([Nozomi Networks, 2026-08-12](https://www.nozominetworks.com/blog/when-ransomware-turns-off-the-hvac-lessons-from-the-winnipeg-hospital-incident)). Central monitoring of heating, ventilation and cooling was lost — the equipment itself kept running and was switched to local/manual monitoring — the hospital's security office was closed, and staff could not issue or update physical ID access cards, prompting the Manitoba Nurses Union to flag entrance-security concerns given a history of violent incidents at the facility. Clinical care and patient-facing IT systems were not affected: "clinical services continue uninterrupted, and based on the investigation conducted to date, there is no indication that patients have been affected" ([Shared Health, via CBC News, 2026-08-10](https://www.cbc.ca/news/canada/manitoba/health-sciences-centre-ransomware-hack-9.7302058)) — which Nozomi Networks' analysis credits to IT/OT network segmentation having held between the clinical and facility networks.

As of CBC's most recent status update (2026-08-17, one week post-disclosure), Shared Health's investigation had still not attributed the incident to a named ransomware group, disclosed an access vector, or confirmed whether personal health or financial data was accessed — initial review suggested none was: "the health authority says its investigation has found the attack has affected central monitoring of its heating, ventilation and cooling systems but that they are still operating and being monitored locally" ([CBC News (The Canadian Press), reporting Shared Health's update, 2026-08-17](https://www.cbc.ca/news/canada/manitoba/winnipeg-hsc-ransomware-cyberattack-9.7310005)). No extortion group has claimed the incident on a leak site.

Nozomi frames the transferable lesson as structural rather than incident-specific: hospital building-management systems — BACnet-class protocols, often a decade-plus without patching, owned by facilities teams outside IT's asset inventory — sit on the same class of network reachability as any other IT asset, so ransomware that never specifically targets OT can still disable HVAC and access-control availability as a side effect. In a hospital, ventilation loss is itself an infection-control failure under ANSI/ASHRAE/ASHE 170 pressure-relationship and air-change requirements, not merely a comfort issue — the transferable point this constituency's healthcare-sector estates should carry regardless of Winnipeg's specific vector, which remains undisclosed.
