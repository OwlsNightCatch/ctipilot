---
schema: 1
kind: incident
title: "CNIL fines Hôpital privé de la Loire EUR 500,000 over a 727,000-record breach traced to a single unprotected external physician account"
headline: "France's data regulator details exactly how one compromised doctor account exposed an entire hospital's patient records"
summary: >
  France's CNIL imposed a EUR 500,000 GDPR fine (2026-09-03) on Hôpital privé de la Loire (HPL,
  Saint-Étienne) over a summer-2025 breach of its externally-reachable patient-record system that
  exposed 727,113 individuals. The root causes CNIL names — no VPN/MFA for external clinician
  access, no care-team-scoped access control, and no real-time anomaly detection — are a direct
  transferable lesson for any hospital exposing an EPR to external physicians.
discovered_at: "2026-09-04T05:30:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-04T0410Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity]
regions: [europe]
sectors: [healthcare, public-sector]
entities:
  - "incident:hopital-prive-de-la-loire-dpi-breach-2025"
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.cnil.fr/en/sanction-fine-hopital-prive-loire"
    publisher: "CNIL (French data protection authority)"
    date: "2026-09-03"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/"
    publisher: "BleepingComputer"
    date: "2026-09-03"
    role: corroborating
  - url: "https://databreaches.net/2026/09/03/cnil-health-data-breach-e500000-fine-imposed-on-the-loire-private-hospital/"
    publisher: "DataBreaches.net"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The authentication procedure to connect to the hospital's e-Health Patient Summary, used by users outside the hospital, in particular liberal doctors, was not sufficiently robust, due to the lack of VPNs and multifactor authentication means. The attacker took advantage of this vulnerability to access the data."
    publisher: "CNIL"
  - quote: "This lack of access limitation allowed the attacker, using the credentials of a single user account, to access the data of all hospital patients."
    publisher: "CNIL"
  - quote: "the attacker was able to explore the hospital's e-Health Patient Summary for several days and extract a very large volume of data, without that abnormal activity being detected"
    publisher: "CNIL"
verification: single-source-national-cert
sourcing_note: >
  Single-source under the national-authority carve-out: CNIL is the disclosing regulator for its
  own jurisdiction's sanction decision. BleepingComputer and DataBreaches.net both restate CNIL's
  own sanction text rather than independently assessing the breach mechanics; BleepingComputer adds
  one independent data point — the attacker's own 2025 claim to Le Progrès via Telegram, unverified
  against CNIL's findings — which does not raise credibility above 2.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

France's CNIL imposed a EUR 500,000 GDPR fine on 3 September 2026 against Hôpital privé de la Loire (HPL, Saint-Étienne, part of the Ramsay Santé group) over a summer-2025 breach of its externally-reachable electronic patient-record system, which exposed 524,867 patients and 202,246 people designated as "trusted third parties" — 727,113 individuals total ([CNIL, 2026-09-03](https://www.cnil.fr/en/sanction-fine-hopital-prive-loire)). CNIL's investigation names three compounding failures. First, the authentication procedure for external users — private-practice physicians accessing the record system from outside the hospital — required no VPN and no multi-factor authentication, and the attacker used the credentials of a single compromised physician account to get in. Second, the access-control model had no concept of "care team" restricting an account to the patients that physician actually treats, so one set of valid credentials opened every hospital patient's record. Third, with no real-time or near-real-time anomaly detection on the record system, the attacker was able to enumerate and extract records over several days undetected — CNIL states this absence "contributed to exacerbating the scale of the data breach." A self-identified attacker using the alias "Marak" told the French outlet Le Progrès via Telegram at the time that the intrusion began with a single doctor's account, and separately attempted to sell the stolen data for EUR 2,000-5,000; it was later reported that the data was in fact neither sold nor published. These are unconfirmed criminal self-claims, consistent with but not independently verified against CNIL's own findings ([BleepingComputer, 2026-09-03](https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/)).

CNIL separately sanctioned HPL under GDPR Article 34 for notifying only the direct patients affected and never notifying the 202,246 trusted third parties whose data was also taken. HPL has begun remediation and has three to fifteen months, depending on measure type, to complete it.

**Defender takeaway:** the reusable lesson is architectural, not incident-specific — any hospital or clinical-records operator exposing an EPR/DPI to external private-practice clinicians should verify three controls exist before an incident forces the question: VPN plus MFA on every external authentication path into the record system; access control scoped to an actual care-team relationship rather than blanket all-patient visibility per credential; and real-time or near-real-time access-velocity monitoring on the record-access application itself, not only at the network perimeter. This is directly transferable to any Swiss cantonal or regional hospital running a similar external-physician access model. Detection concept, telemetry class first: application-layer access logs on the EPR for per-account record-read volume and velocity — a single account reading records outside its declared roster, or reading more than a handful of distinct patients within one session, is the discriminator CNIL states was entirely absent here. **Triage:** a physician legitimately covering for a colleague or consulting on a transferred patient will show occasional multi-patient access; the sustained, broad, multi-day sweep CNIL describes is what separates an attacker from routine coverage.
