---
schema: 1
kind: vulnerability
title: "CERTFR-2026-AVI-0572: Centreon April 2026 bulletin, SQL injection in eight components, command injection in MBI and XSS in MAP"
headline: "Centreon fixes SQL injection in eight Infra Monitoring components and command injection in MBI (CERTFR-2026-AVI-0572)"
summary: "Centreon's April 2026 monthly bulletin for Centreon Infra Monitoring, published on 2026-05-12 and relayed by CERT-FR as CERTFR-2026-AVI-0572, fixes SQL injection through string concatenation in legacy PHP files of eight components (CVSS 8.8), command injection through a dos2unix call in MBI (CVSS 8.8) and an SVG-based XSS in MAP (CVSS 6.8). Fixes cover the supported 24.04 (MBI), 24.10 and 25.10 branches; no CVE identifiers were published, and neither source reports exploitation as of 2026-05-12."
discovered_at: "2026-05-13T05:00:07Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - patch-available
regions:
  - europe
sectors:
  - public-sector
entities:
  - "trend:centreon-april-2026-vuln-cluster"
techniques: [T1190]
affected_products: ["Centreon Infra Monitoring"]
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/"
    publisher: "CERT-FR CERTFR-2026-AVI-0572"
    date: "2026-05-12"
    role: primary
  - url: "https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660"
    publisher: "Centreon security bulletin"
    date: "2026-05-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "SQL injection via string concatenation across legacy PHP files"
    publisher: "Centreon security bulletin"
    source_url: "https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660"
  - quote: "Command injection via dos2unix exec"
    publisher: "Centreon security bulletin"
    source_url: "https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660"
  - quote: "XSS in images by altering the SVG"
    publisher: "Centreon security bulletin"
    source_url: "https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660"
  - quote: "MBI versions 24.04.x before 24.04.15 (translated from French)"
    original: "MBI versions 24.04.x antérieures à 24.04.15"
    publisher: "CERT-FR CERTFR-2026-AVI-0572"
    source_url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/"
verification: multi-source
sourcing_note: >
  Centreon's own bulletin is the assessment; CERT-FR's advisory restates it and lists the fixed version per component and branch.
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
migrated_from: briefs/2026-05-13.md
updates:
  - at: "2026-10-21T20:48:52Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Neither Centreon nor CERT-FR published CVE identifiers for the April 2026 Centreon fixes: the
      bulletin lists SQL injection in eight components, command injection through a dos2unix call in MBI
      and an SVG-based XSS in MAP, with fixed releases per 24.04, 24.10 and 25.10 branch. The Fortinet,
      Exim, Microsoft and SAP CVEs that stood beside it belong to other advisories, and no cited source
      supports claims about Centreon's public-sector footprint or its stored credentials.
    fields: [affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

Centreon published its April 2026 monthly security bulletin for Centreon Infra Monitoring on 2026-05-12: SQL injection through string concatenation across legacy PHP files in Anomaly Detection, Auto Discovery, AWIE, BAM, DSM, License Manager, MAP and Open Tickets (CVSS 8.8 each), command injection through a dos2unix exec call in MBI (CVSS 8.8) and an XSS in MAP through altered SVG images (CVSS 6.8), each listed with no reference identifier ([Centreon, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660)). CERT-FR relayed it as CERTFR-2026-AVI-0572 with remote code execution, SQL injection and XSS as the risks, and lists no CVE identifiers ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)). The first fixed releases are Anomaly Detection 24.10.10 and 25.10.5, Auto Discovery 24.10.13 and 25.10.5, AWIE 24.10.6 and 25.10.6, BAM 24.10.14 and 25.10.5, DSM 24.10.6 and 25.10.3, License Manager 24.10.9 and 25.10.4, MAP 24.10.17 and 25.10.5, MBI 24.04.15, 24.10.17 and 25.10.5, and Open Tickets 24.10.11 and 25.10.6 ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)). Neither source states whether exploitation needs authentication or reports exploitation as of 2026-05-12 ([Centreon, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660); [CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)).

**Exposure:** Centreon installations running any of the nine listed components below the fixed release of their branch ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)); the components are installed and updated on the Central Server ([Centreon, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660)).

**Defender takeaway:** update the affected components on the Central Server to the fixed release of their branch, and back up any customised Open Tickets provider configuration before updating, as Centreon advises ([Centreon, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660)).

## Correction — 2026-10-21T20:48:52Z

Centreon's bulletin lists every fix with no reference identifier and CERT-FR's advisory has no CVE section, so no CVE identifiers exist for this release ([Centreon, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660); [CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)). The flaws are SQL injection through string concatenation in legacy PHP files of eight components, command injection through a dos2unix exec call in MBI and an XSS through altered SVG images in MAP, each with its own fixed release per branch ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)). The Fortinet, Exim, Microsoft and SAP vulnerabilities patched the same week are separate advisories, not part of this Centreon release, and neither Centreon advisory describes Centreon's deployment in public-sector networks or the monitored-host credentials it holds ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/)).
