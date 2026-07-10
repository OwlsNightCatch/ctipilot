---
schema: 1
kind: vulnerability
horizon: operational
title: "Siemens SICAM 8 (A8000/EGS/S8000) grid RTUs: firmware-signature-validation bypass + OPC-UA-off-by-default among four CVEs (SSA-229470)"
headline: "Siemens patches a firmware-signing bypass and an insecure OPC UA default in SICAM 8 grid-protection controllers — plan the out-of-band OT update"
summary: >
  Siemens ProductCERT advisory SSA-229470 (2026-07-09), republished in-window by CERT-FR/ANSSI as
  CERTFR-2026-AVI-0860, patches four vulnerabilities in the CPCI85 and SICORE firmware of SICAM A8000,
  SICAM EGS and SICAM S8000 remote terminal units — controllers Siemens frames for transmission and
  distribution system operators. The most consequential are a firmware-update signature-validation flaw
  enabling persistent malicious firmware and an OPC UA default configuration that disables all OPC UA
  security. No exploitation is reported. Energy-sector operators running SICAM 8 should schedule the
  V26.20 firmware update and review OPC UA exposure.
discovered_at: "2026-07-10T20:34:32Z"
event_date: "2026-07-09"
run_id: 2026-07-10T2009Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, ot-ics, priv-esc, auth-bypass, patch-available]
regions: [europe, global]
sectors: [energy]
entities: []
techniques: [T1601, T1210, T1098, T1499]
affected_products:
  - "Siemens SICAM A8000 CP-8031/CP-8050 (CPCI85 firmware)"
  - "Siemens SICAM EGS (CPCI85 firmware)"
  - "Siemens SICAM A8000 CP-8010/CP-8012 (SICORE firmware)"
  - "Siemens SICAM S8000 (SICORE firmware)"
cves:
  - id: CVE-2026-54799
    cvss: "6.7"
    epss: null
    type: rce
    vector: local
    auth: admin-required
    status: [patch-available]
    affected: "CPCI85 < V26.20; SICORE < V26.20.0"
    fixed: "CPCI85 V26.20 / SICORE V26.20.0"
  - id: CVE-2026-54801
    cvss: "7.2"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "CPCI85 < V26.20; SICORE < V26.20.0"
    fixed: "CPCI85 V26.20 / SICORE V26.20.0"
  - id: CVE-2026-54800
    cvss: "4.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: default-config
    status: [patch-available]
    affected: "CPCI85 < V26.20; SICORE < V26.20.0"
    fixed: "CPCI85 V26.20 / SICORE V26.20.0"
  - id: CVE-2026-54798
    cvss: "6.5"
    epss: null
    type: dos
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "CPCI85 < V26.20; SICORE < V26.20.0"
    fixed: "CPCI85 V26.20 / SICORE V26.20.0"
sources:
  - url: "https://cert-portal.siemens.com/productcert/html/ssa-229470.html"
    publisher: "Siemens ProductCERT (SSA-229470)"
    date: "2026-07-09"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0860/"
    publisher: "CERT-FR / ANSSI"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The affected application contains a vulnerability in its firmware update mechanism's signature validation process. This could allow an attacker to install malicious firmware, leading to persistent code execution and system compromise."
    publisher: "Siemens ProductCERT (SSA-229470)"
  - quote: "The affected application ships with a default configuration that disables all OPC UA security mechanisms. This could allow an attacker to gain unauthorized access and control over critical system functions."
    publisher: "Siemens ProductCERT (SSA-229470)"
verification: multi-source
sourcing_note: "Siemens ProductCERT is the first-party primary for its own products; CERT-FR/ANSSI (a home-region national authority) independently republished the advisory in-window as CERTFR-2026-AVI-0860. No in-the-wild exploitation is claimed by either. Aggregate advisory scores CVSS v3.1 7.2 / v4.0 8.6; per-CVE v3.1 base scores recorded here."
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
  - "Plan an out-of-band firmware update to CPCI85 ≥ V26.20 / SICORE ≥ V26.20.0 across SICAM A8000/EGS/S8000 estates; validate in a test environment and supervise the update per Siemens' documented procedure before rolling to production grid devices."
  - "Audit SICAM 8 OPC UA configuration — the shipped default disables OPC UA security (CVE-2026-54800); enable it and confirm the OPC UA interface is not network-reachable from untrusted zones."
  - "Restrict network access to SICAM device HTTP/web-API and OPC UA interfaces via segmentation, firewalls and VPN; treat the debug HTTP endpoint (CVE-2026-54798) as attack surface and confirm resilient redundant protection is in place per grid-design guidance."
migrated_from: null
---

Siemens ProductCERT's SSA-229470 covers four flaws in the SICORE base system and CPCI85 central processing/communication firmware that underpin the SICAM A8000 (CP-8010/CP-8012 on SICORE; CP-8031/CP-8050 on CPCI85), SICAM EGS (CPCI85) and SICAM S8000 (SICORE) remote terminal units ([Siemens ProductCERT, 2026-07-09](https://cert-portal.siemens.com/productcert/html/ssa-229470.html)). The advisory's stated aggregate impact is denial of service, but the individual issues span further: CVE-2026-54799 (CVSS v3.1 6.7, AV:L/PR:H) is a firmware-update signature-validation flaw that lets an attacker who already holds high privileges install malicious firmware for persistent code execution; CVE-2026-54801 (v3.1 7.2) lets an authenticated attacker bypass credential validation when the web API processes administrative-account modifications and gain elevated privileges; CVE-2026-54800 (v3.1 4.8) is an insecure default that disables all OPC UA security, letting a network attacker reach control functions; and CVE-2026-54798 (v3.1 6.5) is an HTTP-reachable debug interface an authenticated attacker can use to crash the web process. All are fixed in CPCI85 V26.20 / SICORE V26.20.0. CERT-FR/ANSSI republished the advisory the next day as CERTFR-2026-AVI-0860, giving European energy-sector operators a home-region authority citation ([CERT-FR/ANSSI, 2026-07-10](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0860/)).

**Defender takeaway:** none of the four is a remote pre-authentication vector — the firmware-signing bypass requires prior high privilege on the device and the admin-API and debug flaws require authentication — so this is a defence-in-depth and supply-chain-integrity concern for grid-protection equipment rather than an emergency, but SICAM 8 sits on the power-grid boundary at TSOs and DSOs across Europe including Switzerland, where firmware updates are inherently planned out-of-band events rather than routine patch-cycle work. The load-bearing exposure to close proactively is CVE-2026-54800: because OPC UA security is off in the shipped configuration, any SICAM 8 device whose OPC UA interface is reachable from a less-trusted network segment is exposed to unauthorized control-function access without exploiting anything — a configuration review, not a patch, closes that one immediately. Siemens' own guidance stresses that grid resilience through redundant secondary protection schemes limits the reliability impact of any single compromised controller.
