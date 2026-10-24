---
schema: 1
kind: incident
title: "AdaptHealth breached via a social-engineered hijack of a third-party contractor's session"
headline: "AdaptHealth breached via a social-engineered hijack of a third-party contractor's session"
summary: DME and home-healthcare provider AdaptHealth Corp.
discovered_at: "2026-07-03T04:48:12Z"
event_date: 2026-07-02
run_id: 2026-07-03-04ba8283
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
  - identity
regions:
  - us
sectors:
  - healthcare
entities: []
cves: []
sources:
  - url: "https://www.sec.gov/Archives/edgar/data/1725255/000110465926080297/ahco-20260627x8k.htm"
    publisher: SEC EDGAR — AdaptHealth 8-K
    role: primary
  - url: "https://www.stocktitan.net/sec-filings/AHCO/8-k-adapt-health-corp-reports-material-event-80512081bbc7.html"
    publisher: StockTitan filing digest
    role: corroborating
closed_sources: []
evidence:
  - quote: The incident was the result of a successful social engineering attack that compromised a user session associated with a third-party contractor.
    publisher: SEC EDGAR — AdaptHealth 8-K
  - quote: The Company has confirmed that certain data was exfiltrated from its systems including a stored password file associated with insurance billing.
    publisher: SEC EDGAR — AdaptHealth 8-K
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-07-03.md
---

DME and home-healthcare provider AdaptHealth Corp. (Nasdaq: AHCO) filed an SEC Form 8-K (Item 1.05) on 2026-07-02 disclosing that an actor accessed its cloud-based business applications — including internal patient-management systems and document storage — through "a successful social engineering attack that compromised a user session associated with a third-party contractor" ([SEC 8-K, 2026-07-02](https://www.sec.gov/Archives/edgar/data/1725255/000110465926080297/ahco-20260627x8k.htm)). The company received an extortion communication on 2026-06-15 and determined materiality on 2026-06-27; confirmed exfiltration includes a stored insurance-billing password file plus patient PII and PHI, though it says SSNs and payment-card data are not held in the affected systems ([StockTitan filing digest, 2026-07-02](https://www.stocktitan.net/sec-filings/AHCO/8-k-adapt-health-corp-reports-material-event-80512081bbc7.html)). No threat-actor group is named. The session-hijack-of-a-contractor pattern echoes Scattered-Spider-style help-desk/vishing tradecraft, though the filing does not attribute.

**Defender takeaway:** contractor/third-party sessions into cloud EHR and document SaaS are a distinct trust boundary. Conditional Access that treats contractor accounts like staff, and long-lived session tokens not re-validated against device/location, are the exploitable gap — enforce phishing-resistant MFA plus token-theft-resistant session binding (e.g. Continuous Access Evaluation) on contractor identities, and scope CASB impossible-travel / new-device-reuse alerts specifically to guest/contractor principals.
