---
schema: 1
kind: incident
title: "Deutsche Bank confirms a third-party vendor incident after 'Unsafe' ransomware group posts alleged employee data"
headline: "Deutsche Bank says its own network is untouched, pointing to a German marketing-platform vendor, after 'Unsafe' claims a breach and leaks employee records"
summary: >
  The ransomware/extortion group 'Unsafe' listed Deutsche Bank on its leak site and published
  screenshots of alleged employee records (emails, password hashes, addresses), claiming access
  to the bank's internal systems. Deutsche Bank's own statement says the incident is at an
  external German vendor running a marketing/incentive platform for its sales partners, with no
  indication its own network was affected. The transferable lesson: a vendor-side compromise can
  surface as an apparent client-brand breach, and leaked employee directories are a ready
  spear-phishing/credential-stuffing list regardless of who was actually compromised.
discovered_at: "2026-07-09T12:35:00Z"
event_date: "2026-07-08"
run_id: 2026-07-09T1211Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, supply-chain, organized-crime]
regions: [dach, europe]
sectors: [finance]
entities: [actor:unsafe-ransomware]
cves: []
sources:
  - url: "https://www.computing.co.uk/news/2026/security/deutsche-bank-probes-supplier-cyber-incident-after-ransomware-gang-claims-breach"
    publisher: "Computing (UK)"
    date: "2026-07-09"
    role: primary
  - url: "https://cybernews.com/security/deutsche-bank-ransomware-data-breach/"
    publisher: "Cybernews"
    date: "2026-07-07"
    role: corroborating
  - url: "https://www.cybersecurity-insiders.com/unsafe-ransomware-allegedly-targets-deutsche-bank/"
    publisher: "Cybersecurity Insiders"
    date: "2026-07-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "\"We have been informed of a cybersecurity incident at an external service provider,\" the spokesperson said, adding that there was \"no indication that Deutsche Bank's internal systems or networks were or are affected\" and no evidence of unauthorised access to the bank's network."
    publisher: "Computing (UK)"
  - quote: "Based on the available samples, it's not possible to determine whether customer data is included in the alleged breach"
    publisher: "Cybernews"
verification: multi-source
sourcing_note: "The breach claim originates from the 'Unsafe' leak-site posting (an attacker claim, reported as a claim); the third-party-vendor scope is confirmed by Deutsche Bank's own spokesperson statement carried by multiple outlets. Generic 'Unsafe' TTP profiling in secondary coverage (zero-day exploitation, specific tooling) is unverified for this intrusion — the actual initial-access vector into the vendor has not been disclosed. Credibility 2 (incident confirmed; scope/customer-data impact unconfirmed)."
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
actions:
  - "Treat leaked employee directories (email + password hashes + physical addresses) from any vendor compromise as an active spear-phishing and credential-stuffing target list: force password resets and step up MFA/phishing-resistant auth for named employees, and brief them on tailored social-engineering attempts."
  - "Inventory outsourced marketing/incentive/HR SaaS platforms that hold employee PII and confirm your incident-response and breach-notification obligations account for vendor-side compromises that surface under your brand — Deutsche Bank has now been hit through third parties repeatedly."
  - "Track 'Unsafe' as an actor with reported 2026 targets in Germany, Switzerland and France when scoping RaaS/double-extortion threat models for EU financial and public-sector bodies."
migrated_from: null
---

The ransomware/extortion group "Unsafe" listed Deutsche Bank on its dark-web leak site and published screenshots of alleged database exports, terminal commands and employee records — email addresses, password hashes, physical addresses — as proof of a claimed breach of the bank's "internal systems" ([Cybernews, 2026-07-07](https://cybernews.com/security/deutsche-bank-ransomware-data-breach/); [Cybersecurity Insiders, 2026-07-08](https://www.cybersecurity-insiders.com/unsafe-ransomware-allegedly-targets-deutsche-bank/)). Deutsche Bank's own spokesperson, in a statement carried on 2026-07-08/09, said the incident did not involve the bank's own network but instead affected a third-party company in Germany that runs a marketing and incentive platform for the bank's sales partners, with "no indication that Deutsche Bank's internal systems or networks were or are affected" ([Computing UK, 2026-07-09](https://www.computing.co.uk/news/2026/security/deutsche-bank-probes-supplier-cyber-incident-after-ransomware-gang-claims-breach)). Researchers assessing the leaked samples said the data appears to relate to bank employees but that they could not determine whether any customer information was included.

Unsafe operates a ransomware-as-a-service, double-extortion model; after a relatively quiet 2024–2025 it re-emerged in 2026 with reported targets in Germany, the United States, Switzerland and France — the same-actor reach into this constituency's home region being the reason the item is in scope rather than the victim's name. The actual initial-access vector into the German vendor has not been disclosed by any party, and generic secondary profiling of Unsafe's tooling should be treated as unverified for this specific intrusion. **Defender takeaway:** the operational lesson is third-party exposure, not Deutsche Bank specifically — an outsourced sales/marketing/incentive platform holding employee PII can be compromised and surface as an apparent breach of the client brand while the client's own network stays untouched, and the leaked employee directory is immediately useful to attackers for credential stuffing and targeted phishing. EU financial and public-sector bodies should inventory such SaaS relationships and rehearse the "vendor breached, our brand in the headline" incident-response and notification path in advance.
