---
schema: 1
kind: incident
horizon: strategic
weekly_section: weekly-incidents-recap
title: "German LG Berlin II ruling — Apobank liable for €218,000+ phishing loss; PSD2 IP-analytics obligation clarified"
headline: "German LG Berlin II ruling — Apobank liable for €218,000+ phishing loss; PSD2 IP-analytics obligation clarified"
summary: "On 2026-04-22 the Landgericht Berlin II (Civil Chamber 38, case 38 O 293/25; not yet final pending appeal) ordered Deutsche Apotheker- und Ärztebank (Apobank) to reimburse €218,000+ in losses from a sophisticated phishing attack combining forged physical bank letters, manipulated online banking interfaces, and …"
discovered_at: "2026-05-04T05:00:24Z"
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

On 2026-04-22 the Landgericht Berlin II (Civil Chamber 38, case 38 O 293/25; not yet final pending appeal) ordered Deutsche Apotheker- und Ärztebank (Apobank) to reimburse €218,000+ in losses from a sophisticated phishing attack combining forged physical bank letters, manipulated online banking interfaces, and spoofed-number phone calls. The court rejected gross-negligence defences, finding the fraud too sophisticated to attribute to customer failure; critically, the ruling found the bank's fraud-detection systems failed to act on a clear anomaly visible in bank-side logs — the new device registration and first login originated from materially different IP addresses and ISPs. The court treated this as an obligation under Germany's PSD2 implementation: an IP-based behavioural analytics duty triggering a strong-customer-authentication challenge when registration and first-use IPs diverge ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html) · [ilex Rechtsanwälte case summary](https://www.anwalt.de/rechtstipps/phishing-ilex-rechtsanwaelte-erwirkt-haftung-der-apobank-269786.html) · [daily 2026-05-09](/briefs/2026-05-09/)). **Defender takeaway:** EU and Swiss financial-sector and public-sector digital-service providers should expect this trend of liability lines moving toward the service provider when fraud signals are *present in server-side telemetry but not acted on*. The defensive engineering implication is concrete: register-new-device and first-login IP / ISP comparison is now a regulatory expectation in PSD2 jurisdictions, not just a best-practice control.
