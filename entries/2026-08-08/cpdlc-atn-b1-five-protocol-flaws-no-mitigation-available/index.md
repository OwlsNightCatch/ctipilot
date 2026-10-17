---
schema: 1
kind: vulnerability
title: "CISA publishes five protocol-level flaws in CPDLC over ATN-B1, reported by a Swiss armasuisse researcher — no mitigation available, and CISA assesses exploitation unlikely outside a lab"
headline: "The controller-to-cockpit data link has no authentication by design, so the advisory has a remediation status of none-available"
summary: >
  CISA published ICS advisory ICSA-26-219-01 on 2026-08-07 covering five vulnerabilities in Controller-Pilot
  Data Link Communications as implemented over ATN-B1, the worldwide standard for text instructions between
  air traffic control and the cockpit. All five are properties of the standard rather than one vendor's
  product: the link is clear-text and unauthenticated, so a party able to transmit on the frequency can
  inject clearances or false emergency messages (CVE-2025-71409 and CVE-2025-71412, CVSS 7.1) or tear down
  sessions for one or many aircraft (CVE-2025-71410, -71411, -71413, CVSS 5.3). CISA's CSAF records
  remediation as none-available and states exploitation is unlikely outside a lab setting.
discovered_at: "2026-08-08T05:25:00Z"
event_date: "2026-08-07"
run_id: 2026-08-08T0409Z-intel
priority: routine
immediate_action: null
tags: [vulnerabilities, ot-ics, no-patch, auth-bypass, dos]
regions: [global, switzerland]
sectors: [transport]
entities: []
techniques: [T1565.002, T1499]
affected_products: ["ATN-B1 CPDLC (Advisory Circular 90-117 Data Link Communications)"]
cves:
  - id: CVE-2025-71409
    cvss: "7.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "ATN-B1 CPDLC, all versions of the standard"
    fixed: "none available — CISA records the remediation category as none_available"
  - id: CVE-2025-71412
    cvss: "7.1"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "ATN-B1 CPDLC, all versions of the standard"
    fixed: "none available — CISA records the remediation category as none_available"
  - id: CVE-2025-71410
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "ATN-B1 CPDLC, all versions of the standard"
    fixed: "none available — CISA records the remediation category as none_available"
  - id: CVE-2025-71411
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "ATN-B1 CPDLC, all versions of the standard"
    fixed: "none available — CISA records the remediation category as none_available"
  - id: CVE-2025-71413
    cvss: "5.3"
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "ATN-B1 CPDLC, all versions of the standard"
    fixed: "none available — CISA records the remediation category as none_available"
sources:
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01"
    publisher: "CISA"
    date: "2026-08-07"
    role: primary
closed_sources: []
evidence:
  - quote: "ATN-B1 CPDLC relies on legacy clear text unauthenticated radio frequency links."
    publisher: "CISA"
  - quote: "These vulnerabilities do not constitute an unsafe aircraft condition but can degrade operational safety margins by increasing workload, delaying safety-critical instructions, and reducing situational awareness."
    publisher: "CISA"
  - quote: "These vulnerabilities in the CPDLC protocol stack are exploitable in a lab environment. However, they require very specific conditions to be met and are unlikely to be exploited outside of a lab setting."
    publisher: "CISA (CSAF record for ICSA-26-219-01)"
verification: single-source-national-cert
sourcing_note: "CISA is the coordinating authority publishing this standards-level advisory and is the disclosing party for it, which is the recognised single-source carve-out. Per-CVE scores, CWE classes and descriptions are read from the advisory's own per-CVE sections and its CSAF record rather than inferred from the summary table, which prints a single collective 7.1."
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
actions: []
migrated_from: null
---

CISA published ICS advisory ICSA-26-219-01 on 2026-08-07 covering five vulnerabilities in Controller-Pilot Data Link Communications as implemented over the ATN-B1 standard — the data link that carries text clearances and instructions between air traffic controllers and flight crews worldwide, under Advisory Circular 90-117. The advisory's product version is `vers:all/*`, which is the honest way of saying this is a property of the standard rather than a defect in any implementation: "ATN-B1 CPDLC relies on legacy clear text unauthenticated radio frequency links" ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01)).

The five split into two effects. CVE-2025-71409 (CWE-306, CVSS 3.1 7.1) is the absence of authentication for VHF Data Link messages, which lets a rogue ground station inject CPDLC messages producing unexpected or misleading clearances; CVE-2025-71412 (CWE-754, 7.1) covers injection of false emergency or status messages, which CISA describes as potentially leading to misallocation of resources, operational confusion and improper responses by flight crews, controllers and ground operations. The remaining three are availability effects at CVSS 5.3: CVE-2025-71410 (Unnumbered Disconnect and malformed link-control frames terminating sessions and forcing reversion to voice), CVE-2025-71411 (broadcast control frames disconnecting multiple aircraft simultaneously, leading to controller overload) and CVE-2025-71413 (malformed or out-of-sequence frames at the X.25 layer causing repeated resets). Every one is carried out remotely over radio frequency ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01)).

Two statements from CISA bound this correctly, and both should travel with any onward summary. On consequence: the vulnerabilities "do not constitute an unsafe aircraft condition but can degrade operational safety margins by increasing workload, delaying safety-critical instructions, and reducing situational awareness". On likelihood, from the advisory's machine-readable CSAF record: they "are exploitable in a lab environment. However, they require very specific conditions to be met and are unlikely to be exploited outside of a lab setting" ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01)). The same record gives the remediation category as none-available for all five CVEs. There is no fix to schedule and no configuration to change.

There is a home-region thread: the advisory credits the report to "Martin Strohmeier of Armasuisse", the Swiss federal armaments enterprise ([CISA, 2026-08-07](https://www.cisa.gov/news-events/ics-advisories/icsa-26-219-01)).

This is carried for situational awareness in the transport sector rather than as an action item, and it is deliberately shipped without one. Nothing in an enterprise security stack touches an RF data link — the exposure belongs to air navigation service providers, airlines and aviation regulators, at the level of contingency planning for reversion to voice communication and of the multi-year standards work that would add authentication to the protocol. For a defender reading this brief, the useful takeaway is calibration: when reporting on this advisory circulates in less careful form, the two CISA statements above are what keep it in proportion.
