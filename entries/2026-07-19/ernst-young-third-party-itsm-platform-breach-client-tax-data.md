---
schema: 1
kind: incident
horizon: operational
title: "Ernst & Young discloses a breach of a third-party IT support-ticket platform used by its tax practice, exposing client tax and financial documents"
headline: "EY discloses client tax-data exposure after a third-party ITSM support-ticket platform was breached"
summary: >
  Ernst & Young LLP filed breach notifications (2026-07-15) after detecting that an unauthorized party
  accessed a third-party IT service-management (ITSM) support-ticket platform used by its tax practice
  between 28 March and 12 April 2026 and downloaded documents belonging to multiple tax clients. Support
  tickets on the platform carried attached client tax and financial information; EY has not disclosed the
  access vector, the platform, or how many are affected. The transferable lesson for any organization —
  public-sector included — that outsources IT helpdesk/ticketing: sensitive attachments accumulate inside
  support-ticket systems that data-classification and DLP programs routinely overlook.
discovered_at: "2026-07-19T04:25:44Z"
event_date: "2026-07-15"
run_id: 2026-07-19T0408Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain]
regions: [global]
sectors: [finance, public-sector]
entities: ["incident:ey-third-party-itsm-breach-2026"]
techniques: [T1199, T1213]
affected_products: []
cves: []
sources:
  - url: "https://oag.ca.gov/ecrime/databreach/reports/sb24-626542"
    publisher: "California Office of the Attorney General (breach-notification filing)"
    date: "2026-07-15"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/"
    publisher: "BleepingComputer"
    date: "2026-07-17"
    role: corroborating
  - url: "https://cyberinsider.com/ey-says-client-tax-data-exposed-in-third-party-it-software-breach/"
    publisher: "CyberInsider"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "an unauthorized third party had accessed the said platform between March 28 and April 12 and downloaded multiple documents"
    publisher: "BleepingComputer"
  - quote: "Support tickets submitted through the platform may include documents containing client tax information."
    publisher: "CyberInsider"
  - quote: "Sample of Notice: EY Notice Letter US General.pdf Organization Name: Ernst & Young LLP Date(s) of Breach (if known): Saturday, March 28, 2026 Thursday, April 23, 2026"
    publisher: "California Office of the Attorney General (breach-notification filing)"
verification: multi-source
sourcing_note: "Ernst & Young's own regulatory breach notification (California/Vermont AG filings) is a first-party authoritative disclosure of its own incident (reliability A). The intrusion window (2026-03-28 to 04-12), the ~11-day gap between the intruder's access ending (2026-04-12) and EY's detection (2026-04-23), and the tax-document exposure are corroborated by BleepingComputer and CyberInsider; EY has not disclosed the initial-access vector, named the compromised platform, or stated the affected count or whether non-US clients are impacted — credibility rated 2 for that undisclosed scope."
confidence: medium
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
migrated_from: null
---

Ernst & Young LLP (EY), one of the "Big Four" audit/tax/consulting networks, filed data-breach notifications with the California and Vermont Attorneys General on 2026-07-15 after determining that an unauthorized third party had accessed a third-party IT service-management (ITSM) platform used by its tax practice ([California OAG, 2026-07-15](https://oag.ca.gov/ecrime/databreach/reports/sb24-626542)). EY detected anomalous activity on 2026-04-23 and an external forensics firm concluded that the intruder had access "between March 28 and April 12 and downloaded multiple documents" belonging to multiple tax clients — a roughly two-week access window, detected about eleven days after the intruder's access ended ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/)). The platform manages IT support tickets for tax-engagement work, and "support tickets submitted through the platform may include documents containing client tax information" — the financial information used to prepare tax filings ([CyberInsider, 2026-07-17](https://cyberinsider.com/ey-says-client-tax-data-exposed-in-third-party-it-software-breach/)); the regulatory notice letter itself redacts the specific data elements involved. EY has not disclosed the initial-access vector, named the compromised third-party platform, stated how many individuals are affected, or said whether non-US clients are impacted; no extortion or ransomware group has claimed the intrusion, and EY is offering 24 months of identity monitoring to affected individuals ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/ernst-and-young-discloses-data-breach-after-support-system-hack/)).

**Defender takeaway:** the transferable signal here is a data-exposure surface, not an actor or a TTP — sensitive client documents routinely accumulate as attachments inside third-party SaaS/ITSM support-ticket systems used by IT-support staff, a location that data-classification and DLP programs frequently miss because the platform is neither the primary case-management system nor customer-facing. Any organization that outsources IT helpdesk/ticketing — public-sector bodies included, given how much sensitive material flows through support requests referencing production systems — should inventory what sensitive attachments move through its support-ticket platform and apply the same access-governance, retention, logging and third-party-monitoring controls it applies to the primary systems those tickets reference. The ~11-day gap between the intruder losing access and EY detecting it also argues for retention of, and periodic review of, third-party-platform access logs long enough to reconstruct a two-week access window detected around a week and a half later.
