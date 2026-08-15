---
schema: 1
kind: incident
horizon: operational
title: "NHS Blood and Transplant sent organ-offer messages naming recipients over an unencrypted pager network — and because pager broadcasts leave no receiver log, it cannot scope who received them"
headline: "A BBC investigation forces NHSBT to report a breach: transplant-patient identifiers broadcast in clear over a legacy paging network"
summary: >
  NHS Blood and Transplant routinely sent transplant-patient names, dates of birth, tissue-match scores and
  immunosuppression risk factors to hospital transplant teams over an unencrypted pager network, unaware the
  channel carried no encryption. It acknowledged the breach only after the BBC raised it, reported to the ICO,
  and has stopped. Because pager broadcasts are one-way and receivers cannot be tracked, NHSBT states it cannot
  establish whether the data was accessed or how many people are affected.
discovered_at: "2026-08-15T04:49:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - info-disclosure
regions:
  - uk
  - europe
sectors:
  - healthcare
entities:
  - incident:nhs-blood-transplant-pager-breach-2026-08
techniques: [T1040]
affected_products: []
cves: []
sources:
  - url: "https://www.bbc.co.uk/news/articles/clyj92j210do"
    publisher: BBC News
    date: "2026-08-14"
    role: primary
closed_sources: []
evidence:
  - quote: "The sensitive medical data of transplant patients from across the UK was routinely sent over an unencrypted pager network, an NHS service has admitted."
    publisher: BBC News
  - quote: "Recipients of pager messages cannot be tracked, therefore NHSBT said it was unclear whether the unencrypted information was accessed or how many people may have been affected."
    publisher: BBC News
verification: single-source
sourcing_note: >
  The BBC's investigation is the originating and only first-hand account, and carries NHSBT's, the network
  operator's and the ICO's own statements directly; other coverage re-reports it rather than observing
  independently, so credibility is rated on the single investigating party.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory any surviving paging or one-way radio channel in the estate and check what is actually transmitted over it — clinical, dispatch or operational messages containing personal data belong on an encrypted channel, and unlike a logged system there is no retrospective way to scope an exposure once it has happened."
migrated_from: null
---

A BBC investigation established that NHS Blood and Transplant — the service that coordinates organ transplants across the UK — routinely sent the names, dates of birth and the types of organs being offered or needed to members of hospital transplant teams using pagers, unaware the messages were not encrypted ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)). The messages also carried tissue-match scores and immunosuppression risk factors for the people receiving transplants. NHSBT acknowledged this was a data breach after being alerted by the BBC, said it was "deeply sorry", reported the breach to the Information Commissioner and has stopped sending patient data this way; its head of organ transplantation, Anthony Clarkson, said the service had been using the channel for urgent communications where speed can be critical, and that "We were surprised that these messages were not encrypted, and that vulnerability was there." The ICO confirmed NHSBT reported an incident and that it is making inquiries ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)).

The property that makes this different from an ordinary disclosure is the absence of a receiver-side record. Paging is a one-way broadcast: the BBC reports NHSBT's position that because recipients of pager messages cannot be tracked, it is unclear whether the unencrypted information was accessed or how many people may have been affected ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)). Luca Arnaboldi, an assistant professor at the University of Birmingham quoted in the investigation, described the technology as "never meant for privacy", noted that a broadcast reaches anyone on the right frequency across a wide area, and characterised the result as "an unauditable log of leaked information". The exposure was not limited to NHSBT: over a ten-day sample the BBC found hundreds of messages on the same network from ambulance trusts, hospitals and fire services, including mental-health incident details, medication details and the name of a patient trying to take their own life. North West Ambulance Service and Northern Ireland Ambulance Service, both named as users, said their messages did not include patients' names; NWAS said pagers have now been fully withdrawn ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)).

Responsibility here sits with configuration rather than with a defect. The company operating the paging network told the BBC it provides encrypted paging and secure-messaging solutions with "customers determining how those services are deployed", that it has no visibility of or control over the content its customers transmit, and that its terms make clear radio signals may be intercepted and advise customers not to send sensitive or personal information over radio ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)). In 2019 the then-Health Secretary, Matt Hancock, announced that the NHS in England should stop using pagers by 2021, and parts of the organisation continued regardless; the Department for Health said that where "legacy technologies" are still in use, patient information should be "handled securely and in line with data protection requirements" ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)).

**Defender takeaway:** the transferable lesson for any hospital, utility or emergency-services operator is that legacy one-way channels sit outside every control a SOC normally reasons about. There is no authentication to strengthen, no log to hunt in, and no way to bound an exposure after the fact — which means the only point of control is an inventory question asked *before* an incident: which radio, paging or telemetry channels still exist, and what is being put on them. A channel that predates the security programme is not automatically out of its scope.
