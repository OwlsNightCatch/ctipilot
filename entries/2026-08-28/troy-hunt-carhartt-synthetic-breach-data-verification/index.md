---
schema: 1
kind: research
title: "Troy Hunt: a 24.9M-address ShinyHunters/Carhartt breach-claim collapses to 12.9M real records once TPC-DS synthetic benchmark data and several duplicate/test-account patterns are filtered out — a reusable methodology for verifying inflated breach-claim record counts"
headline: "Domain-frequency, TLD and birth-year distribution analysis unmasks a benchmark dataset masquerading as half of a real breach"
summary: >
  Following ShinyHunters' claim to have stolen Carhartt customer data, Troy Hunt's initial Have I
  Been Pwned processing found 24.9M unique email addresses — but systematic verification, using an
  AI chat assistant ("PwnedClaw") to help analyse the corpus, showed the true figure was 12,933,413
  (12.9M) once TPC-DS retail-analytics benchmark test data co-located in the same Databricks schema
  and several duplicate/test-account patterns were filtered out. The diagnostic signals —
  singleton-domain frequency, gibberish-domain patterns, perfectly uniform birth-country and
  birth-year distributions — are a reusable methodology for any analyst triaging a leak-site
  record-count claim.
discovered_at: "2026-08-28T06:50:00Z"
updated_at: null
event_date: "2026-08-25"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [global]
sectors: [retail]
entities: [actor:shinyhunters]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/"
    publisher: "Troy Hunt (Have I Been Pwned)"
    date: "2026-08-25"
    role: primary
closed_sources: []
evidence:
  - quote: "97.6% of domains appear exactly once — that's not a long tail, that's a signature. Real breach data from a retail company would have thousands of addresses on corporate domains, hundreds on ISP domains, a natural power law. Instead you have 10.1M singleton domains. That's pure TPC-DS generation."
    publisher: "PwnedClaw, quoted by Troy Hunt (Have I Been Pwned)"
  - quote: "Birth year stats are conclusive. The distribution runs 1924-1992 and is perfectly flat — roughly 1,050-1,194 per year, every single year without exception. That's not population data, that's a random number generator with a fixed range."
    publisher: "PwnedClaw, quoted by Troy Hunt (Have I Been Pwned)"
  - quote: "The conclusion is pretty solid: this is a real Carhartt Databricks breach, but the TPC-DS benchmark data was co-located in the same schema and ShinyHunters (and every aggregator after them) grabbed it all without knowing what they were looking at."
    publisher: "PwnedClaw, quoted by Troy Hunt (Have I Been Pwned)"
  - quote: "New breach: Carhartt was the target of a ShinyHunters extortion campaign earlier this month. Data allegedly obtained from the company was later published, including 12.9M unique email addresses. 83% were already in @haveibeenpwned."
    publisher: "Troy Hunt (Have I Been Pwned)"
verification: single-source
sourcing_note: >
  Single-source by Admiralty terms (Troy Hunt / Have I Been Pwned, reliability B — no second
  outlet had independently replicated this specific verification analysis at fetch time), but the
  source is the person who directly did the primary verification work on the primary dataset, not
  a secondary report of someone else's claim, which places it closer to a primary technical
  disclosure than ordinary single-source news. Worth flagging for AI-content
  transparency: several of the analytical conclusions quoted here (the domain-singleton,
  birth-year and closing-synthesis observations) are verbatim output from "PwnedClaw," Hunt's own
  AI chat assistant, reproduced inside his post's chat transcript — not sentences Hunt personally
  wrote, though he directed the analysis, validated each finding against the raw data himself, and
  states the underlying figures and conclusions as his own. Evidence quotes are attributed to
  PwnedClaw accordingly rather than to Hunt directly.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
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

Following ShinyHunters' 2026-08-13 claim to have stolen 50GB+ of Carhartt customer data, Troy Hunt's initial Have I Been Pwned processing run found 24,876,077 unique email addresses in the dump. Using an AI chat assistant he calls "PwnedClaw" to help work through the corpus — while directing every step and validating each finding against the raw data himself — Hunt ran domain-frequency analysis, TLD pattern checks, and birth-country and birth-year distribution analysis, and found the bulk of the corpus was TPC-DS retail-analytics-benchmark synthetic test data that had been sitting in the same Databricks schema ShinyHunters exfiltrated, which the actor — and, per Hunt, "every aggregator after them" — failed to distinguish from real customer records before publishing.

The diagnostic signals were all independently conclusive. PwnedClaw's frequency analysis found 97.6% of domains in the corpus appeared exactly once: "97.6% of domains appear exactly once — that's not a long tail, that's a signature. Real breach data from a retail company would have thousands of addresses on corporate domains, hundreds on ISP domains, a natural power law. Instead you have 10.1M singleton domains. That's pure TPC-DS generation" ([PwnedClaw, quoted by Troy Hunt, 2026-08-25](https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/)). An initial 32% of addresses used syntactically plausible names on gibberish `.edu`/`.org` domains, and the same pattern was found to extend across `.com` and every TLD once Hunt pushed further: 54.8% of addresses (13.6M) sat on domains appearing 100+ times (real), against 45.2% (11.25M) on domains appearing under 100 times — the synthetic share, not the initially-estimated 32%. Birth-country data was perfectly uniform across all 211 ISO country codes (roughly 380–420 records per country, with the US tied with Canada and dwarfed by e.g. Antigua and Barbuda and Lesotho) rather than concentrated in Carhartt's actual US/European customer base. Birth-year distribution was mathematically flat from 1924–1992: "birth year stats are conclusive. The distribution runs 1924-1992 and is perfectly flat — roughly 1,050-1,194 per year, every single year without exception. That's not population data, that's a random number generator with a fixed range" ([PwnedClaw, quoted by Troy Hunt, 2026-08-25](https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/)) — no weighting toward a plausible customer-age curve.

Corroborating evidence the real customer data is present and genuinely breached: internal `@carhartt.com` employee addresses (15,057 of them), 32-character hex-prefixed internal aliases and the internal `carharttdonotship.com` domain — none of which an external actor could fabricate or scrape — plus a 70% hit rate against HIBP's existing freemail dataset and purchase-tagged sub-addresses (`+carhartt`, `+paypal`, and similar). PwnedClaw's synthesis: "the conclusion is pretty solid: this is a real Carhartt Databricks breach, but the TPC-DS benchmark data was co-located in the same schema and ShinyHunters (and every aggregator after them) grabbed it all without knowing what they were looking at" ([PwnedClaw, quoted by Troy Hunt, 2026-08-25](https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/)).

Excluding the identified TPC-DS synthetic chunk files (600 plus a further 1,200) dropped the count from 24.9M to 13,306,258 — a 47% reduction, and still not the final figure. Hunt's own further manual review, again assisted by PwnedClaw, found and removed several more inflation sources: 5,736 Microsoft-365 domain-alias triplicates (the same mailbox counted three times across `carhartt.com`, `carhartt.onmicrosoft.com` and `carhartt.mail.onmicrosoft.com`); 285,808 `deactivate-`-prefixed soft-delete duplicates (with 3,174 renamed back to their active form where no duplicate existed); and 48,787 `wctest.com` plus 32,514 `carharttdonotship.com` addresses, both internal performance-test domains identified by a shared `perftest` alias pattern rather than real customers. The final published figure — which Hunt's own tweet states directly — is 12,933,413 unique addresses: "New breach: Carhartt was the target of a ShinyHunters extortion campaign earlier this month. Data allegedly obtained from the company was later published, including 12.9M unique email addresses. 83% were already in @haveibeenpwned" ([Troy Hunt, 2026-08-25](https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/)) — a little over half of ShinyHunters' implied headline scope.

The methodology is region-agnostic: Carhartt itself is a US retailer, but the finding is a reusable verification methodology for any SOC or CTI team triaging leak-site record-count claims, not a victim-specific disclosure. It is also a case study in AI-assisted analysis discipline: an AI assistant's confident, well-phrased analytical output is not automatically fact, and PwnedClaw's own intermediate 13.3M figure was itself superseded by further manual review — the analyst directing it still owns validating every claim and every number against the underlying data before publishing.
