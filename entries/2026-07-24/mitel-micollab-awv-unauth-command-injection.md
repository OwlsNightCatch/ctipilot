---
schema: 1
kind: vulnerability
horizon: operational
title: "Mitel MiCollab AWV: unauthenticated command injection to full system compromise (CVSS 9.8, MTLVULN-1694, CVE pending)"
headline: "Mitel ships an out-of-band fix for an unauthenticated RCE in MiCollab's conferencing component — no CVE yet, exposed appliances first"
summary: >
  Mitel PSIRT advisory MISA-2026-0006, republished by CERT-FR, patches an unauthenticated command-injection flaw
  (CVSS 9.8) in the Audio, Web and Video Conferencing (AWV) component of on-prem MiCollab that lets a
  network-reachable attacker execute arbitrary OS commands with no authentication or user interaction. No CVE is
  assigned yet (internal id MTLVULN-1694); no exploitation is reported, but the product class has a track record.
discovered_at: "2026-07-24T04:36:09Z"
event_date: "2026-07-22"
run_id: 2026-07-24T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global, europe]
sectors: [public-sector, telco, healthcare, finance]
entities: []
techniques: [T1190]
affected_products: ["Mitel MiCollab"]
cves: []
sources:
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006"
    publisher: "Mitel PSIRT (MISA-2026-0006)"
    date: "2026-07-22"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0911/"
    publisher: "CERT-FR / ANSSI (CERTFR-2026-AVI-0911)"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A command injection vulnerability has been identified in the Audio, Web, and Video Conferencing (AWV) component of Mitel MiCollab which, if successfully exploited, could allow an unauthenticated attacker to conduct a command injection attack due to insufficient parameter sanitization."
    publisher: "Mitel PSIRT (MISA-2026-0006)"
  - quote: "Note: The above issue is referenced here by our internal tracking ID. A CVE identifier has been requested but is not yet assigned."
    publisher: "Mitel PSIRT (MISA-2026-0006)"
verification: multi-source
sourcing_note: "No CVE is assigned yet — track by Mitel PSIRT id MISA-2026-0006 / internal MTLVULN-1694 until MITRE allocates one. Neither Mitel nor CERT-FR reports in-the-wild exploitation at publication; included on the unauthenticated-no-interaction profile plus this appliance class's documented exploitation history (a prior MiCollab unauthenticated RCE in 2025), not on confirmed exploitation."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Patch internet-facing Mitel MiCollab to 10.3.0.18, or apply the Mitel backport patches (KB000128275) for the 10.2 SP1 FP2 and 9.8 SP3 FP2 branches — the AWV command injection needs no authentication and no user interaction."
migrated_from: null
---

Mitel's PSIRT advisory **MISA-2026-0006** (2026-07-22, republished by CERT-FR as CERTFR-2026-AVI-0911 the next day) addresses a critical command-injection vulnerability, internally tracked as MTLVULN-1694 with a CVE requested but not yet assigned, in the **Audio, Web, and Video Conferencing (AWV)** component of on-premises MiCollab ([Mitel, 2026-07-22](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006)). Per Mitel, insufficient parameter sanitisation in the AWV component lets an unauthenticated attacker inject and execute arbitrary OS commands — rated CVSS 3.1 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), meaning network-reachable, no credentials and no user interaction ([Mitel, 2026-07-22](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006)). Affected releases run from 10.0.0.26 up to and including 10.2 SP1 FP2 (10.2.1.205) and 9.8 SP3 FP2 (9.8.3.203) and earlier; the fix ships in MiCollab 10.3.0.18, with Mitel-provided backport patches for the 10.2 SP1 FP2 and 9.8 SP3 FP2 branches (KB000128275) ([CERT-FR, 2026-07-23](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0911/)). Neither Mitel nor CERT-FR reports exploitation at publication.

**Defender takeaway:** MiCollab is a widely-deployed unified-communications and conferencing platform across European public-sector and enterprise voice estates, and its AWV component is frequently internet-exposed for external conferencing — exactly the surface that pre-auth command-injection targets. The absence of a CVE identifier is a tracking inconvenience, not a reason to defer: this is an out-of-band vendor advisory for an unauthenticated RCE on an appliance class with prior real-world exploitation (an earlier MiCollab unauthenticated RCE was exploited in the wild in 2025), so any internet-reachable AWV instance is a priority patch even before a public proof-of-concept or scanning appears. Where the patch cannot be applied immediately, restrict network reachability of the AWV conferencing interface to trusted networks and watch web/application access logs on that component for anomalous parameter values preceding process-execution telemetry (a web-tier process spawning a shell interpreter is the behavioural signature of successful command injection).
