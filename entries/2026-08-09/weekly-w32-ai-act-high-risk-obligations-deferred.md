---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "The EU AI Act's high-risk obligations were deferred six days before they would have applied — Regulation (EU) 2026/1744 moves Annex III systems to 2 December 2027 and Annex I to 2 August 2028, and the Commission's own Article 113 page still shows the old text"
headline: "The AI Act's 2 August 2026 headline date survived; almost every obligation behind it was carved out and deferred"
summary: >
  Regulation (EU) 2026/1744, the "Digital Omnibus on AI," was published in the Official Journal on 24 July
  2026 and entered into force on 27 July. It amends Article 113 of the AI Act in three places: obligations
  for standalone high-risk AI systems under Annex III — which would have applied from the general 2 August
  2026 date — move to 2 December 2027; high-risk systems embedded as safety components in already-regulated
  products under Annex I move from 2 August 2027 to 2 August 2028; and the AI Act's sectoral-law amendment
  articles apply immediately from 27 July 2026. Article 113's headline sentence, "It shall apply from
  2 August 2026," is not edited, which is exactly why the change is easy to miss — and the Commission's own
  Article 113 explorer page still displayed the pre-amendment text when this run checked it.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-07-27"
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [europe, switzerland]
sectors: [public-sector, finance, healthcare, education]
entities:
  - policy:eu-ai-act-digital-omnibus-2026
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng/xhtml"
    publisher: "EUR-Lex / Official Journal of the European Union"
    date: "2026-07-24"
    role: primary
  - url: "https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng/xhtml"
    publisher: "EUR-Lex / Official Journal of the European Union"
    date: "2024-07-12"
    role: corroborating
  - url: "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113"
    publisher: "European Commission — AI Act Service Desk"
    date: "2026-08-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I;"
    publisher: "EUR-Lex / Official Journal of the European Union"
  - quote: "Articles 102 to 110 shall apply from 27 July 2026."
    publisher: "EUR-Lex / Official Journal of the European Union"
  - quote: "It shall apply from 2 August 2026."
    publisher: "EUR-Lex / Official Journal of the European Union"
verification: multi-source
sourcing_note: >
  Read from the consolidated legal text on EUR-Lex rather than from commentary, because the amendment
  operates as a surgical replacement inside Article 113's third paragraph and every secondary restatement
  this run encountered was either incomplete or out of date. A consolidated, amendment-applied version of
  the AI Act was not available on EUR-Lex or on the Commission's own AI Act Service Desk at the time of this
  check — both still show the original wording — so the amending regulation itself is the authority.
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

A compliance function that read the AI Act's headline application date and diarised 2 August 2026 got the right date and the wrong obligation set. Regulation (EU) 2026/1744, the "Digital Omnibus on AI," was published in the Official Journal on 24 July 2026 and entered into force on 27 July, six days before that date, and it rewrites the carve-outs that determine what actually applies.

The amendment is surgical, which is the reason it is easy to misread. It replaces points inside Article 113's *third* paragraph and leaves the second paragraph — "It shall apply from 2 August 2026" ([EUR-Lex, 2024-07-12](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng/xhtml)) — untouched as text, so a reader who stops at that sentence concludes nothing has changed. What changed sits one paragraph below: the amended point now provides that "Chapter III, Sections 1, 2, and 3, with the exception of Article 6(5), shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III; and (ii) 2 August 2028 as regards AI systems classified as high-risk pursuant to Article 6(1) and Annex I" ([EUR-Lex, 2026-07-24](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng/xhtml)). Annex III is the standalone high-risk list that covers biometrics, employment, education, migration, access to essential services and law enforcement — categories that map directly onto public-administration systems — and those obligations were due on the general date. They are now sixteen months further out. Annex I high-risk systems, embedded as safety components in products already regulated under EU product law, move from 2 August 2027 to 2 August 2028.

Two smaller changes run the other way. A new point provides that "Articles 102 to 110 shall apply from 27 July 2026" — the AI Act's own amendments to sectoral product legislation take effect immediately on the omnibus's entry into force rather than waiting for a later date. And the omnibus inserts two further prohibited practices into Article 5(1), which apply from 2 December 2026 rather than from the February 2025 date that governs the rest of Chapters I and II.

The secondary observation is operationally relevant to anyone whose compliance tooling reads from official web sources rather than from the Official Journal. The European Commission's own AI Act Service Desk explorer page for Article 113, fetched during this run, still displayed the pre-amendment text with the old three-point structure ([European Commission — AI Act Service Desk, checked 2026-08-09](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-113)), sixteen days after the Commission published the amending regulation. No consolidated version reflecting the amendment was available on EUR-Lex either. Any downstream tool, tracker or advisory that sources its dates from those pages is currently serving a timetable that the law has superseded.

**Defender takeaway:** for a Swiss federal or cantonal body this is not a direct obligation, and for most it is not a SOC matter at all — it belongs to the procurement and compliance functions and to any supplier placing AI systems on the EU market. The concrete action is narrow: re-check any AI Act readiness plan, supplier questionnaire or contractual clause that was written against the 2 August 2026 date for Annex III systems, because that date is no longer the one that applies, and re-check the source it was written from, because the Commission's own public-facing page has not caught up with its own legal act. Note also that the deferral moves obligations, not risk — the systems concerned are the same systems, and a longer conformity runway is not a reason to defer the security assessment of them.
