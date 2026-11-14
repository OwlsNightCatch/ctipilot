---
schema: 1
kind: incident
title: "Swiss Bitcoin Pay (Neuchâtel) shuts down its servers after a suspected intrusion, saying IBANs, wallet addresses and hashed passwords may have been accessed"
headline: "A Swiss Bitcoin payment processor takes itself offline over a suspected breach, but says customer funds stay safe under its non-custodial design"
summary: >
  Swiss Bitcoin Pay, a Neuchâtel-based non-custodial Bitcoin payment processor used by more than
  1,000 merchants, disclosed on 2026-09-14 that a malicious user likely gained access to its
  internal systems, and shut down its servers as a precaution while investigating. The company
  says customer email addresses, Bitcoin wallet addresses, IBANs, transaction history and hashed
  passwords may have been accessed; customer funds are unaffected because the platform's
  non-custodial design routes payments directly to merchant wallets rather than through the
  company.
discovered_at: "2026-09-15T05:20:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-15T0410Z-intel
priority: notable
immediate_action: null
tags: [data-breach, cryptocrime]
regions: [switzerland, dach]
sectors: [finance]
entities: ["incident:swiss-bitcoin-pay-internal-systems-breach-2026-09"]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://x.com/SwissBitcoinPay/status/2099473448162488618"
    publisher: "Swiss Bitcoin Pay (victim's own statement)"
    date: "2026-09-14"
    role: primary
  - url: "https://bitcoinmagazine.com/news/swiss-bitcoin-pay-data-breach"
    publisher: "Bitcoin Magazine"
    date: "2026-09-14"
    role: corroborating
  - url: "https://news.bitcoin.com/security/swiss-bitcoin-pay-just-went-dark-after-a-mysterious-intruder/"
    publisher: "Bitcoin.com News"
    date: "2026-09-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A malicious user has likely gained access to Swiss Bitcoin Pay’s internal systems. As a precaution, we are temporarily shutting down our servers while we investigate and secure our infrastructure."
    publisher: "Swiss Bitcoin Pay (victim's own statement)"
  - quote: "At this stage, we believe they may have accessed customer email addresses, Bitcoin addresses and IBANs, transaction history, and hashed passwords. It is not yet clear whether any other information was accessed."
    publisher: "Swiss Bitcoin Pay (victim's own statement)"
  - quote: "User funds are safe, and any amounts owed to users will be fully returned."
    publisher: "Swiss Bitcoin Pay (victim's own statement)"
verification: single-source-victim
sourcing_note: "Swiss Bitcoin Pay is the only party who has looked at the incident directly; the two corroborating outlets both relay the company's own statement rather than offering independent forensic assessment, and no regulator or independent investigator has commented."
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
updates: []
migrated_from: null
---

Swiss Bitcoin Pay, a Neuchâtel-based non-custodial Bitcoin payment processor whose website claims more than 1,000 merchants across 21 countries ([Bitcoin.com News, 2026-09-14](https://news.bitcoin.com/security/swiss-bitcoin-pay-just-went-dark-after-a-mysterious-intruder/)), disclosed on its official account on 2026-09-14 that "a malicious user has likely gained access to Swiss Bitcoin Pay's internal systems" and that, "as a precaution, we are temporarily shutting down our servers while we investigate and secure our infrastructure" ([Swiss Bitcoin Pay, 2026-09-14](https://x.com/SwissBitcoinPay/status/2099473448162488618)). The company says "at this stage, we believe they may have accessed customer email addresses, Bitcoin addresses and IBANs, transaction history, and hashed passwords," adding that "it is not yet clear whether any other information was accessed" ([Swiss Bitcoin Pay, 2026-09-14](https://x.com/SwissBitcoinPay/status/2099473448162488618)). No attacker has been named, no access vector or mechanism has been disclosed, and the company has not said when service will resume.

Customer funds themselves are unaffected: Swiss Bitcoin Pay's non-custodial model routes Bitcoin and Lightning Network payments directly to merchant wallets rather than holding them, so the company states "user funds are safe, and any amounts owed to users will be fully returned" ([Swiss Bitcoin Pay, 2026-09-14](https://x.com/SwissBitcoinPay/status/2099473448162488618)). The exposure risk instead falls on affected customers: the combination of email addresses, IBANs, Bitcoin wallet addresses and transaction history is enough to support targeted phishing, SIM-swap attempts, and social-engineering against payment-recovery or account-verification pretexts, even though the hashed passwords and non-custodial design limit direct account or fund takeover.

**Defender takeaway:** organizations and individuals who transacted through Swiss Bitcoin Pay should treat their email address, IBAN, wallet address and transaction history as exposed and watch for phishing or vishing attempts that reference specific past transactions or account details; the incident is a reminder that a non-custodial payment design protects funds but not the customer metadata a processor still stores, so a breach there still creates a real fraud-enablement risk even when no money moves.
