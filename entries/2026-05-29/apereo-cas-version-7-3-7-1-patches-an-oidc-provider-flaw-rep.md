---
schema: 1
kind: threat
horizon: operational
title: "Apereo CAS version 7.3.7.1 patches an OIDC-provider flaw reported by Coop Switzerland; CERT-FR issues advisory CERTFR-2026-AVI-0654"
headline: "Apereo CAS version 7.3.7.1 patches an OIDC-provider flaw reported by Coop Switzerland; CERT-FR issues advisory CERTFR-2026-AVI-0654"
summary: The Apereo Foundation released CAS version 7.3.7.1 on 2026-05-27 fixing an unspecified vulnerability in the OpenID Connect identity-provider component of its Central Authentication Service.
discovered_at: "2026-05-29T05:00:00Z"
event_date: 2026-05-28
run_id: 2026-05-29-c7f56b00
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - identity
  - patch-available
regions:
  - switzerland
  - europe
sectors:
  - public-sector
  - education
  - finance
entities: []
cves: []
sources:
  - url: "https://apereo.github.io/2026/05/27/oidc-vuln/"
    publisher: Apereo (oidc-vuln disclosure)
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0654/"
    publisher: CERT-FR CERTFR-2026-AVI-0654
    role: corroborating
closed_sources: []
evidence:
  - quote: The vulnerability only affects deployments where CAS operates as an OpenID Connect identity provider
    publisher: Apereo CAS security disclosure
  - quote: "Une vulnérabilité a été découverte dans Apereo CAS. Elle permet à un attaquant de provoquer un problème de sécurité non spécifié par l'éditeur."
    publisher: CERT-FR CERTFR-2026-AVI-0654
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
migrated_from: briefs/2026-05-29.md
---

The Apereo Foundation [released CAS version 7.3.7.1 on 2026-05-27](https://apereo.github.io/2026/05/27/oidc-vuln/) fixing an unspecified vulnerability in the OpenID Connect identity-provider component of its Central Authentication Service. Apereo scoped the disclosure to deployments where CAS acts as an OIDC IdP (no explicit statement about non-OIDC deployments, but the scoping suggests SAML / Kerberos-only configurations are out of scope of this specific defect). The reporters are **Artur Stoecklin and David Roth at Coop (Switzerland)**, who reported the issue to the Apereo team via the **YesWeHack** bug-bounty platform — a direct CH-discovered identity-infrastructure issue rather than a vendor-only disclosure. CERT-FR / ANSSI [issued advisory CERTFR-2026-AVI-0654 on 2026-05-28](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0654/) framing the impact as *"un problème de sécurité non spécifié par l'éditeur"* and recommending immediate patching. Full technical details are withheld pending the standard security grace window. Apereo CAS is the dominant open-source SSO platform in European higher education and is also deployed across Swiss federal and cantonal administrations.

**Why it matters to us:** CH-relevant identity infrastructure with an EU-wide deployment footprint and a CH-sourced disclosure. Until technical detail is public, prioritise upgrade to the fixed version 7.3.7.1 on any CAS instance acting as an OIDC IdP and monitor OIDC token-issuance logs for unexpected `client_id` values, anomalous `sub` claims and tokens granted to unregistered clients.
