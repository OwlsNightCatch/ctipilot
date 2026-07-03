---
schema: 1
kind: incident
horizon: operational
title: "Magecart family runs its skimmer out of Stripe — payload in customer metadata, stolen cards exfiltrated back through api.stripe.com"
headline: "Magecart family runs its skimmer out of Stripe — payload in customer metadata, stolen cards exfiltrated back through api.stripe.com"
summary: "A Magecart variant hides its skimmer inside Stripe customer metadata and exfiltrates stolen cards back through api.stripe.com as fake customer records — defeating CSP and WAF rules that universally allow-list Stripe. Detection must shift to server-side GTM-container integrity (Sansec, 2026-06-04)."
discovered_at: "2026-06-07T05:00:01Z"
event_date: 2026-06-04
run_id: 2026-06-07-0885f123
priority: high
immediate_action: null
tags:
  - organized-crime
  - supply-chain
  - data-breach
regions:
  - global
  - europe
sectors:
  - retail
  - finance
entities: []
cves: []
sources:
  - url: "https://sansec.io/research/stripe-api-skimmer-infrastructure"
    publisher: Sansec
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/credit-card-theft-campaign-abuses-stripe-to-host-stolen-payment-info/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-06-07.md
---

Sansec's forensics team documented a card-skimming family that routes both payload delivery and exfiltration entirely through Stripe's legitimate API ([Sansec, 2026-06-04](https://sansec.io/research/stripe-api-skimmer-infrastructure)). The actor creates a Stripe customer object and stores the skimmer JavaScript in that customer's metadata fields; at checkout the skimmer is fetched from `api.stripe.com`, captures full card number, CVV, expiry and billing address, then writes the stolen data *back* to Stripe by creating new fake customer records — so both inbound payload and outbound theft look like ordinary Stripe API traffic ([BleepingComputer, 2026-06-04](https://www.bleepingcomputer.com/news/security/credit-card-theft-campaign-abuses-stripe-to-host-stolen-payment-info/)). The entry point is a malicious Google Tag Manager (GTM) container injected into checkout pages of Magento / Adobe Commerce stores; the skimmer-hosting Stripe customer record was created 2025-12-24, indicating a campaign running since at least late 2025. Maps to `T1059.007` (JavaScript) and `T1071.001` (Application Layer Protocol: Web).
**Why it matters to us:** `api.stripe.com` is universally allow-listed in CSP `script-src`/`connect-src` and WAF egress rules on payment sites, so the standard "block unknown exfil endpoints" control is blind to this. Detection has to move server-side: inventory GTM container IDs against an approved list, alert on Stripe customer-creation events that don't map to real orders, inspect customer-metadata fields for encoded JavaScript, and run file-integrity monitoring on checkout-page tag configuration rather than relying on browser-side CSP.
