---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: German LG Berlin II — Apobank ruling sets PSD2 IP-analytics obligation as case law
headline: German LG Berlin II — Apobank ruling sets PSD2 IP-analytics obligation as case law
summary: "The Apobank phishing-liability ruling (LG Berlin II, case 38 O 293/25, 2026-04-22; not yet final pending appeal) explicitly places liability on the bank for failing to act on IP / ISP divergence between new-device registration and first login — interpreted under Germany's PSD2 implementation as an obligation to deploy …"
discovered_at: "2026-05-04T05:00:45Z"
event_date: 2026-05-09
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
  - law-enforcement
regions:
  - europe
  - dach
sectors:
  - finance
entities: []
cves: []
sources:
  - url: "https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html"
    publisher: heise online — Urteil gegen die Apobank
    role: primary
  - url: "https://www.anwalt.de/rechtstipps/phishing-ilex-rechtsanwaelte-erwirkt-haftung-der-apobank-269786.html"
    publisher: "ilex Rechtsanwälte case summary"
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
migrated_from: briefs/weekly/2026-W19.md
---

The Apobank phishing-liability ruling (LG Berlin II, case 38 O 293/25, 2026-04-22; not yet final pending appeal) explicitly places liability on the bank for failing to act on IP / ISP divergence between new-device registration and first login — interpreted under Germany's PSD2 implementation as an obligation to deploy IP-based behavioural analytics and trigger strong-customer-authentication challenges when registration and first-use IPs diverge ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html) · [daily 2026-05-09](/briefs/2026-05-09/)). **What changed:** even if not yet final on appeal, the ruling is the most explicit case-law statement to date in a PSD2 jurisdiction that *failure to act on a fraud signal present in bank-side telemetry* shifts liability to the service provider. **What defenders need to do differently:** EU and Swiss financial-sector and public-sector digital-service providers should treat register-new-device and first-login IP / ISP comparison as a regulatory expectation rather than best practice — and should specifically ensure the SCA-step-up signal can be raised in real time on this anomaly. Anticipate other EU member-state PSD2 jurisdictions following the LG Berlin II reasoning.
