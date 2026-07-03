---
schema: 1
kind: vulnerability
horizon: operational
title: "CERTFR-2026-AVI-0564 — SPIP < 4.4.14: multiple RCEs (public and private area)"
headline: "CERTFR-2026-AVI-0564 — SPIP < 4.4.14: multiple RCEs (public and private area)"
summary: "CERT-FR's advisory CERTFR-2026-AVI-0564 (2026-05-12) covers multiple remote code execution flaws in SPIP — the open-source CMS that powers a substantial share of French ministry, université and francophone Swiss canton web sites (CERT-FR CERTFR-2026-AVI-0564, 2026-05-12; SPIP security bulletin, 2026-05-12)."
discovered_at: "2026-05-13T05:00:06Z"
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
  - "campaign:certfr-2026-avi-0564"
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/"
    publisher: "CERT-FR CERTFR-2026-AVI-0564, 2026-05-12"
    role: primary
  - url: "https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html"
    publisher: "SPIP security bulletin, 2026-05-12"
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
migrated_from: briefs/2026-05-13.md
---

CERT-FR's advisory CERTFR-2026-AVI-0564 (2026-05-12) covers multiple remote code execution flaws in SPIP — the open-source CMS that powers a substantial share of French ministry, université and francophone Swiss canton web sites ([CERT-FR CERTFR-2026-AVI-0564, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/); [SPIP security bulletin, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)). The SPIP bulletin describes two distinct RCE paths in versions prior to 4.4.14: one in the private (authenticated) area, and one in the public (unauthenticated) area "under specific nginx configurations" — the SPIP bulletin notes the bugs are "not covered by the security screen", meaning they bypass SPIP's built-in filter layer. No CVE identifiers are assigned in the vendor bulletin. Fixed in SPIP 4.4.14. No ITW reported. Detection concepts: monitor SPIP `ecrire/` and front-end access logs for the SSTI / template-load gadget patterns the bulletin enumerates; on shared-host SPIP estates, audit the nginx reverse-proxy configuration for the unsafe location pattern. Hardening: upgrade to 4.4.14; on internet-facing SPIP, gate `ecrire/` to a known admin source set at the reverse proxy.
