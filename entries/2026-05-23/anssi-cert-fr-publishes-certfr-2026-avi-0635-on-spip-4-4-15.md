---
schema: 1
kind: threat
horizon: operational
title: "ANSSI / CERT-FR publishes CERTFR-2026-AVI-0635 on SPIP < 4.4.15 — security-policy bypass in the dominant French public-administration CMS"
headline: "ANSSI / CERT-FR publishes CERTFR-2026-AVI-0635 on SPIP < 4.4.15 — security-policy bypass in the dominant French public-administration CMS"
summary: "ANSSI / CERT-FR issued CERTFR-2026-AVI-0635 on 2026-05-22 covering a security-policy bypass vulnerability in SPIP (Système de Publication pour l'Internet) versions prior to 4.4.15; SPIP 4.4.15 was released the same day (SPIP blog, 2026-05-22)."
discovered_at: "2026-05-23T05:00:05Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - patch-available
regions:
  - europe
  - switzerland
sectors:
  - public-sector
  - education
entities:
  - "trend:spip-2026-rce-wave"
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0635/"
    publisher: ANSSI / CERT-FR CERTFR-2026-AVI-0635
    role: primary
  - url: "https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-15.html"
    publisher: SPIP project blog
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
migrated_from: briefs/2026-05-23.md
---

ANSSI / CERT-FR issued [CERTFR-2026-AVI-0635](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0635/) on 2026-05-22 covering a security-policy bypass vulnerability in **SPIP** (Système de Publication pour l'Internet) versions prior to 4.4.15; SPIP 4.4.15 was released the same day ([SPIP blog, 2026-05-22](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-15.html)). The advisory quotes the issue in CERT-FR's standard French: *"Une vulnérabilité a été découverte dans SPIP. Elle permet à un attaquant de provoquer un contournement de la politique de sécurité. SPIP versions antérieures à 4.4.15 sont affectées."* (in English: a vulnerability allows an attacker to bypass the security policy; versions prior to 4.4.15 are affected). No CVE identifier or CVSS score is attached to the CERT-FR notice yet; no exploitation in the wild has been reported.

The SPIP project blog characterises the underlying issue specifically as an **open-redirect vulnerability in the cookie action** — the "policy bypass" framing in the CERT-FR advisory is the standard generic catch-all used by ANSSI, not a separate finding. SPIP is the predominant CMS across French public administration — préfectures, ministries, research institutions — and the Francophone government sphere in Belgium, Switzerland (Romandie cantonal and communal sites) and Canada. Open-redirect issues in authenticated cookie paths are typically chained into account-impersonation or token-laundering against OAuth/OpenID-Connect identity providers, so the EU/CH public-sector risk is concrete even without a CVE in the loop yet. SPIP 4.4.15 is the immediate follow-on to the earlier-May 4.4.14 security release. Detection vantage: review SPIP access logs for unexpected redirect-parameter values on the cookie-action endpoint and any outbound 30x responses to attacker-controlled hosts; defenders should also note that Swiss cantonal and communal administrations using SPIP for public portals fall under the 24-hour NCSC.ch reporting obligation for critical-infrastructure operators if a SPIP intrusion is later confirmed.

**Why it matters to us:** every Romandie cantonal/communal SOC with a SPIP-built portal needs to patch in this cycle; the absence of a CVE makes it easy to overlook on automated patch-track reports.
