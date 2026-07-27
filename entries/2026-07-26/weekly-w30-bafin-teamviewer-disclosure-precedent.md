---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "BaFin fined TeamViewer EUR 240,000 for how it disclosed its 2024 nation-state breach — a website notice did not satisfy the ad-hoc-disclosure duty, setting a breach-disclosure-mechanics precedent for any SIX/EU-listed software or CI supplier"
headline: "A EUR 240k BaFin fine makes a vendor's nation-state breach 'inside information' requiring formal multi-channel ad-hoc disclosure — not just a website post"
summary: >
  Germany's BaFin announced on 2026-07-20 that it fined TeamViewer SE EUR 240,000 (imposed 2026-07-16) for violating Article 17(1) of the EU Market Abuse Regulation — the duty to publish market-moving inside information immediately — over its mid-2024 IT-environment compromise, publicly attributed at the time to the Russia-nexus actor APT29/Cozy Bear. BaFin's finding is narrow but consequential: TeamViewer did post a notice on its own website, but MAR requires ad-hoc disclosures to be distributed simultaneously through a regulated electronic information system to media and to BaFin itself, so a website post alone does not satisfy the obligation regardless of how fast it went up. The 2024 breach itself is old news; the fresh, in-window fact is the enforcement precedent — that a nation-state compromise of a widely-deployed software vendor is inside information demanding formal, immediate, multi-channel disclosure. It is directly relevant to any SIX- or EU-listed software / CI supplier weighing how, not just whether, to disclose a breach, and a reminder that a supplier's own disclosure discipline is now an enforceable, fined obligation in at least one major EU jurisdiction.
discovered_at: "2026-07-26T23:49:00Z"
event_date: 2026-07-20
run_id: 2026-07-26T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - data-breach
regions:
  - europe
  - switzerland
sectors:
  - finance
  - technology
  - public-sector
entities:
  - policy:bafin-teamviewer-mar-disclosure-fine-2026
cves: []
techniques: []
affected_products:
  - "TeamViewer"
sources:
  - url: "https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Massnahmen/40c_neu_124_WpHG/meldung_2026_07_20_team_viewer.html"
    publisher: "BaFin (German Federal Financial Supervisory Authority)"
    date: "2026-07-20"
    role: primary
  - url: "https://www.heise.de/news/TeamViewer-BaFin-verhaengt-Bussgeld-nach-Cyberangriff-11371639.html"
    publisher: "heise online"
    date: "2026-07-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Die Finanzaufsicht Bafin hat am 16. Juli 2026 eine Geldbuße in Höhe von 240.000 Euro gegen die TeamViewer SE festgesetzt."
    publisher: "BaFin"
  - quote: "Ad-hoc-Meldungen müssen über ein elektronisches Informationssystem an Medien und an die Bafin verteilt sowie auf der Unternehmenswebseite veröffentlicht werden."
    publisher: "heise online"
verification: multi-source
sourcing_note: "BaFin is the primary disclosing authority for its own enforcement action; heise online corroborates and adds the disclosure-channel mechanics and TeamViewer's appeal rights beyond a restatement. BaFin is not on this deployment's national-CERT carve-out list, so the item is treated as multi-source on the strength of independent corroboration. The 2024 APT29 attribution is contextual and reported at the time; this entry does not make a fresh actor claim."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Germany's Federal Financial Supervisory Authority, BaFin, announced on 2026-07-20 that it had fined TeamViewer SE EUR 240,000 — "Die Finanzaufsicht Bafin hat am 16. Juli 2026 eine Geldbuße in Höhe von 240.000 Euro gegen die TeamViewer SE festgesetzt" — for violating the EU Market Abuse Regulation (MAR) ([BaFin, 2026-07-20](https://www.bafin.de/SharedDocs/Veroeffentlichungen/DE/Massnahmen/40c_neu_124_WpHG/meldung_2026_07_20_team_viewer.html)). The underlying event is TeamViewer's confirmed mid-2024 compromise of its internal IT environment, attributed at the time to the Russia-nexus actor APT29/Cozy Bear — but that breach is not the point of this item. The fresh, in-window fact is the enforcement action and the disclosure-mechanics precedent it sets.

BaFin's finding is narrow and specific: the violation was of MAR Article 17(1), the duty to publish inside information immediately, and the deficiency was in the *channel*, not the speed. TeamViewer posted a notice on its own website, but as heise summarised the rule, "Ad-hoc-Meldungen müssen über ein elektronisches Informationssystem an Medien und an die Bafin verteilt sowie auf der Unternehmenswebseite veröffentlicht werden" ([heise online, 2026-07-21](https://www.heise.de/news/TeamViewer-BaFin-verhaengt-Bussgeld-nach-Cyberangriff-11371639.html)) — an ad-hoc disclosure must be distributed simultaneously through a regulated electronic information system to media and to BaFin itself, so a website post alone does not discharge the obligation. TeamViewer retains appeal rights, so the precedent is not yet final, but the principle BaFin has asserted is clear: a nation-state compromise of a widely-deployed software vendor is market-moving inside information that requires formal, immediate, multi-channel disclosure.

**Defender takeaway:** the transferable point for this constituency is twofold. For any SIX- or EU-listed software or CI supplier, breach disclosure now carries a *mechanics* obligation that is separately enforceable — how the disclosure is distributed (regulated dissemination system, media, regulator) matters as much as whether and how quickly it is made, and a company that "went public" only via its own website has, in at least one major EU jurisdiction, not met the duty. For public-sector and CI procurement and third-party-risk teams, it is a reminder that a supplier's own disclosure discipline is now a fined regulatory obligation, worth reflecting in vendor-management expectations and breach-notification clauses for listed software suppliers — TeamViewer being a remote-access/remote-support tool deployed across many Swiss and European public-sector and CI environments makes the example concrete rather than abstract.
