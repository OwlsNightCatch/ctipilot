---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "Nearly every breach disclosed this week entered through someone else's infrastructure — a service provider, a data-centre host, an ITSM platform and a CI/CD pipeline, not the victim's own perimeter"
headline: "W29 breaches were third-party-mediated — IWB Basel, Kudankulam/Reliance, Ernst & Young and AsyncAPI entered through a trusted supplier, host or pipeline"
summary: >
  The week's confirmed breaches share one mechanism above all others: the victim's own systems largely held, and the exposure came through a third party it trusted. Basel utility IWB lost ~40,000 customer meter records via a compromised external service provider, its own systems unaffected. A contractor to India's Kudankulam nuclear plant, Reliance Group, confirmed a partial breach originating from a server hosted by third-party data-centre provider Yotta — ~858,000 files leaked by World Leaks. Ernst & Young disclosed client tax-data exposure through a breach of a third-party IT/ITSM platform, filed with the California Attorney General. And the AsyncAPI npm compromise reached three-million-downloads-a-week packages by abusing the org's own CI/CD trusted-publishing pipeline, then — Microsoft's forensic timeline showed — shipped versions carrying cryptographically valid npm/OIDC provenance attestations because the malicious commit rode the legitimate release workflow. The transferable lesson for the constituency is that supplier, host and pipeline trust boundaries are now the dominant breach vector, and that provenance/attestation controls verify which pipeline built an artifact, not that the triggering change was authorized.
discovered_at: "2026-07-19T23:58:00Z"
event_date: 2026-07-16
run_id: 2026-07-19T2310Z-weekly
priority: high
immediate_action: null
tags:
  - supply-chain
  - data-breach
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - energy
  - finance
entities:
  - incident:iwb-basel-service-provider-breach-2026-07
  - incident:kudankulam-reliance-worldleaks-2026-07
  - actor:worldleaks
  - incident:ey-third-party-itsm-breach-2026
  - incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07
  - tool:m-red-team-malware-framework
cves: []
techniques:
  - T1199
  - T1195.002
sources:
  - url: "https://oag.ca.gov/ecrime/databreach/reports/sb24-626542"
    publisher: "California Office of the Attorney General (breach-notification filing)"
    date: "2026-07-15"
    role: primary
  - url: "https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions"
    publisher: "Wiz"
    date: "2026-07-14"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-07-15"
    role: primary
  - url: "https://www.theweek.in/news/india/2026/07/15/india-s-nuclear-files-leaked-on-dark-web-858000-files-from-kudankulam-plant-out-reliance-group-admits-partial-breach.html"
    publisher: "The Week (India), relaying Reuters"
    date: "2026-07-15"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "EY (CA AG filing), IWB (Swiss press, corroborated) and AsyncAPI (Wiz + Microsoft) are confirmed; the Kudankulam/Reliance leak is a confirmed 'partial breach' per Reliance but the leaked files' authenticity is only claimed (Reuters reviewed a sample) — hence credibility 2. Kudankulam is out-of-nexus (India), carried for its global critical-infrastructure significance and the transferable third-party-hosting lesson."
confidence: high
update_of: null
references:
  - 2026-07-16/iwb-basel-third-party-provider-breach-40k-customer-records
  - 2026-07-16/worldleaks-kudankulam-reliance-third-party-hosting-breach
  - 2026-07-19/ernst-young-third-party-itsm-platform-breach-client-tax-data
  - 2026-07-14/asyncapi-npm-supply-chain-compromise-github-actions
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Read as a set, the week's breaches make one point: the perimeter that failed was rarely the victim's own. Four disclosures, four different trust boundaries.

A **service provider** was the vector for Basel utility IWB — a compromised external provider exfiltrated ~40,000 customer meter records while IWB's own systems and supply were unaffected. A **data-centre host** was the vector for the Kudankulam nuclear-plant contractor Reliance Group, which confirmed a "partial breach" originating from a server hosted by third-party provider Yotta, after World Leaks posted ~858,000 files (their authenticity only claimed, with Reuters reviewing a sample) ([The Week/Reuters, 2026-07-15](https://www.theweek.in/news/india/2026/07/15/india-s-nuclear-files-leaked-on-dark-web-858000-files-from-kudankulam-plant-out-reliance-group-admits-partial-breach.html)). An **ITSM/IT platform** was the vector for Ernst & Young, whose client tax data was exposed through a third-party software breach disclosed in a California Attorney General filing ([CA OAG, 2026-07-15](https://oag.ca.gov/ecrime/databreach/reports/sb24-626542)).

The **CI/CD pipeline** case is the most instructive for defenders because it broke an assumed control. The AsyncAPI compromise reached packages with over three million weekly downloads by abusing the org's own trusted-publishing workflow ([Wiz, 2026-07-14](https://www.wiz.io/blog/m-red-team-asyncapi-supply-chain-compromise-via-github-actions)); Microsoft's timeline then showed the trojanized versions carried cryptographically valid npm/OIDC provenance attestations that correctly name the real repo, commit and workflow — "even though the triggering commits were unauthorized" — and executed at import time, so `--ignore-scripts` did not stop them ([Microsoft, 2026-07-15](https://www.microsoft.com/en-us/security/blog/2026/07/15/unpacking-asyncapi-npm-supply-chain-compromise-import-time-payload-delivery/)).

**Defender takeaway:** the constituency's third-party exposure is now the dominant breach surface, and this week refined what that means in two concrete ways. First, supplier/host breaches (IWB, Reliance/Yotta, EY) put the detection burden on contract-level telemetry and notification you do not directly control — the practical lesson is inventorying which providers hold which data class and demanding breach-notification SLAs, because your own SOC will not see the intrusion. Second, the AsyncAPI case is a reminder that provenance verification answers "which pipeline built this?" and not "was this change authorized?" — so a valid attestation is not a substitute for branch-protection, workflow-trigger review and import-time (not just install-hook) dependency monitoring. The per-incident specifics are in the referenced operational entries.
