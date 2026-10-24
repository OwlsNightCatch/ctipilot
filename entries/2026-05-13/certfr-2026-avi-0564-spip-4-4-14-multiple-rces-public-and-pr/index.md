---
schema: 1
kind: vulnerability
title: "CERTFR-2026-AVI-0564: SPIP before 4.4.14, two remote code execution flaws in the private area and, on certain nginx configurations, the public area"
headline: "SPIP 4.4.14 fixes two RCE flaws, one reachable from the public area on certain nginx setups (CERTFR-2026-AVI-0564)"
summary: "SPIP 4.4.14, released on 2026-05-12 and flagged by CERT-FR in CERTFR-2026-AVI-0564, fixes two remote code execution flaws, one in the private area and one in the public area that is limited to certain nginx configurations. SPIP's security screen does not cover them, so only the upgrade protects; neither source publishes CVE identifiers or reports exploitation as of 2026-05-12."
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
  - "trend:spip-2026-rce-wave"
techniques: [T1190]
affected_products: ["SPIP"]
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/"
    publisher: "CERT-FR CERTFR-2026-AVI-0564"
    date: "2026-05-12"
    role: primary
  - url: "https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html"
    publisher: "SPIP security bulletin"
    date: "2026-05-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "an RCE-type flaw in the public area, limited to the use of certain nginx configurations (translated from French)"
    original: "une faille de type `RCE` dans l’espace public, limitée à l’usage de certaines configurations de nginx"
    publisher: "SPIP security bulletin"
    source_url: "https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html"
  - quote: "These flaws are not covered by the security screen. (translated from French)"
    original: "Ces failles ne sont pas prises en charge par l’écran de sécurité"
    publisher: "SPIP security bulletin"
    source_url: "https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html"
  - quote: "SPIP versions before 4.4.14 (translated from French)"
    original: "SPIP versions antérieures à 4.4.14"
    publisher: "CERT-FR CERTFR-2026-AVI-0564"
    source_url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/"
verification: multi-source
sourcing_note: >
  SPIP's own security bulletin is the assessment; CERT-FR's advisory restates it and points to it for the fix.
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
  - at: "2026-10-21T20:47:49Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      SPIP's bulletin gives no exploit detail beyond the public-area flaw being limited to certain nginx
      configurations, so there are no template-gadget patterns or proxy location rules to look for; the
      fix is the upgrade to 4.4.14, which the security screen does not replace. The two RCE flaws carry no
      CVE identifiers, and no cited source gives SPIP deployment figures for ministries, universities or
      Swiss cantons.
    fields: [affected_products, body, classification, entities, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

SPIP's maintenance team released SPIP 4.4.14 on 2026-05-12 to fix two security flaws, a remote code execution (RCE) flaw in the private area and an RCE flaw in the public area that is limited to the use of certain nginx configurations, reported by Louka Jacques-Chevallier (Laluka), Baptiste Rolando, Arthur Deloffre (Vozec), jvoisin and Cezame ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)). The bulletin states that "these flaws are not covered by the security screen" (translated from French), so SPIP's built-in screen gives no interim protection; it gives no technical detail beyond the nginx condition, and the release's change list also includes better sanitisation of HTTP_HOST and a fix to REMOTE_USER handling under nginx ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)). CERT-FR's CERTFR-2026-AVI-0564 lists SPIP versions before 4.4.14 as affected with remote arbitrary code execution as the risk, refers to the SPIP bulletin for the fix and names no CVE identifiers ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/)).

**Exposure:** SPIP sites on any version before 4.4.14 ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/)); the public-area flaw is reachable only on sites served with certain nginx configurations, which the bulletin does not specify ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)).

**Defender takeaway:** upgrade SPIP to 4.4.14, directly or through spip_loader version 8.0.5; the security screen is not a mitigation for these two flaws ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)).

## Correction — 2026-10-21T20:47:49Z

SPIP's bulletin describes the public-area flaw only as limited to certain nginx configurations and names no exploit pattern, so there are no template or gadget signatures in access logs and no specific reverse-proxy location rule to audit for ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)). Its statement that "these flaws are not covered by the security screen" (translated from French) means the screen does not block them and the upgrade to 4.4.14 is the only fix; the bulletin counts two flaws ([SPIP, 2026-05-12](https://blog.spip.net/Mise-a-jour-de-securite-sortie-de-SPIP-4-4-14.html)), and neither it nor CERT-FR gives figures on SPIP's use by ministries, universities or Swiss cantons ([CERT-FR, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0564/)).
