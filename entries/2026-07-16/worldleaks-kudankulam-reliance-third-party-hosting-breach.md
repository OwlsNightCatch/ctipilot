---
schema: 1
kind: incident
horizon: operational
title: "World Leaks posts ~858,000 files tied to India's Kudankulam nuclear-plant contractor; Reliance confirms a third-party-hosting breach"
headline: "World Leaks leaks ~858k files from a Kudankulam nuclear-plant contractor breached at a third-party data-centre host — a lesson for energy-CI operators"
summary: >
  The data-theft-extortion group World Leaks (a Hunters International rebrand) posted roughly
  858,000 files on its leak site attributed to Reliance Group, a contractor to India's Kudankulam
  Nuclear Power Plant; Reuters reviewed ~19,000 sensitive files (2016–2025) purporting to show
  blueprints, supplier and inspection records. Reliance confirmed a "partial breach" from a server
  hosted by third-party Indian data-centre provider Yotta; India's CERT-In is investigating and the
  leaked files are only claimed — not established — to be authentic. Out-of-nexus (India) but carried
  for its global critical-infrastructure significance and a transferable third-party-hosting lesson
  for European energy-CI operators.
discovered_at: "2026-07-16T04:42:00Z"
event_date: "2026-07-15"
run_id: 2026-07-16T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain]
regions: [apac]
sectors: [energy]
entities: [actor:worldleaks, incident:kudankulam-reliance-worldleaks-2026-07]
techniques: [T1199, T1530]
affected_products: []
cves: []
sources:
  - url: "https://www.theweek.in/news/india/2026/07/15/india-s-nuclear-files-leaked-on-dark-web-858000-files-from-kudankulam-plant-out-reliance-group-admits-partial-breach.html"
    publisher: "The Week (India), relaying Reuters"
    date: "2026-07-15"
    role: primary
closed_sources: []
evidence:
  - quote: "They admitted to Reuters that a \"partial breach\" of its data had taken place from a server hosted by Yotta, a third-party Indian data centre service provider, and that the government has been informed about the incident."
    publisher: "The Week (India), relaying Reuters"
  - quote: "19,000 of these files appeared to be highly sensitive, the report added, noting that the documents were dated between 2016 and 2025, and reportedly featured blueprints, supplier details, meeting and inspection records, equipment reviews and insurance policies."
    publisher: "The Week (India), relaying Reuters"
verification: single-source
sourcing_note: "Sourced to a single Reuters wire report relayed by The Week (India); Reliance Group confirmed a partial breach at third-party host Yotta, while the leaked files are only claimed to originate from the plant and their authenticity is not established in the cited reporting. Included as an out-of-nexus item under the breach-gate global-significance and transferable-lesson exceptions, not as a confirmed home-region incident."
confidence: medium
update_of: null
references: []
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

The data-theft-extortion group **World Leaks** — the rebrand of Hunters International already tracked in this store — posted roughly **858,000 files** on its dark-web leak site attributed to Reliance Group, a contractor involved in India's Kudankulam Nuclear Power Plant (KNPP), the country's largest nuclear facility ([The Week / Reuters, 2026-07-15](https://www.theweek.in/news/india/2026/07/15/india-s-nuclear-files-leaked-on-dark-web-858000-files-from-kudankulam-plant-out-reliance-group-admits-partial-breach.html)). Reuters reviewed a subset of about 19,000 files dated 2016–2025 that purport to show facility blueprints, supplier details, meeting and inspection records, equipment reviews and insurance policies; the files are only claimed to originate from the plant and their authenticity is not established. Reliance Group confirmed to Reuters that a **"partial breach"** of its data occurred from a server hosted by **Yotta**, a third-party Indian data-centre provider, and that the government has been informed; India's CERT-In is investigating and a Nuclear Threat Initiative expert warned the exposure could pose a serious plant-safety risk.

**Defender takeaway:** the victim and jurisdiction are out of this constituency's nexus, but the structure is the recurring one — sensitive engineering, inspection and design documentation for a critical-infrastructure facility held on a subcontractor's externally hosted infrastructure, outside the operator's own security perimeter, and breached there rather than at the plant. For European energy-CI operators the transferable action is inventory: know which contractors and hosting providers hold facility design, inspection and supplier documentation, contractually bound them to breach notification and log access, and minimise how much of that documentation persists on third-party infrastructure at all. This is the same third-party-exposure pattern behind the Basel utility disclosure this window, at a far higher-consequence asset class.
