---
schema: 1
kind: research
title: German court finds bank liable for sophisticated phishing loss — PSD2/IP-analytics obligations clarified
headline: German court finds bank liable for sophisticated phishing loss — PSD2/IP-analytics obligations clarified
summary: "On 2026-04-22 the Landgericht Berlin II (Civil Chamber 38, case 38 O 293/25; not yet final pending appeal) ordered Deutsche Apotheker- und Ärztebank (Apobank) to reimburse €218,000+ in losses from a sophisticated phishing attack that combined forged physical bank letters, manipulated online banking interfaces, and …"
discovered_at: "2026-05-09T05:00:10Z"
event_date: 2026-05-08
run_id: 2026-05-09-migrated
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
    publisher: "heise online — Urteil gegen die Apobank, 2026-05-08"
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
migrated_from: briefs/2026-05-09.md
---

On 2026-04-22 the Landgericht Berlin II (Civil Chamber 38, case 38 O 293/25; not yet final pending appeal) ordered Deutsche Apotheker- und Ärztebank (Apobank) to reimburse €218,000+ in losses from a sophisticated phishing attack that combined forged physical bank letters, manipulated online banking interfaces, and spoofed-number phone calls ([heise online, 2026-05-08](https://www.heise.de/news/Urteil-gegen-die-Apobank-Finanzinstitut-haftet-fuer-Phishing-Schaden-11288231.html) · [ilex Rechtsanwälte — case summary, 2026-05](https://www.anwalt.de/rechtstipps/phishing-ilex-rechtsanwaelte-erwirkt-haftung-der-apobank-269786.html)). The court rejected gross-negligence defences, finding the fraud was too sophisticated to attribute to customer failure. Critically, the ruling found the bank's fraud-detection systems failed to act on a clear anomaly visible in bank-side logs: the new device registration and first login originated from materially different IP addresses and ISPs. The court treated this as an obligation under Germany's PSD2 implementation — specifically, a duty to apply IP-based behavioural analytics and trigger a strong-customer-authentication challenge when registration and first-use IPs diverge. For EU/Swiss financial-sector and public-sector digital-service providers: this reinforces the trend of courts placing authentication-failure liability on service providers when fraud signals are present in server-side telemetry but not acted on.
