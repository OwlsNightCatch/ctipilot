---
schema: 1
kind: vulnerability
title: "Mitel OpenScape 4000 and OpenScape 4000 Manager, MISA-2026-0013: two unauthenticated flaws in the Platform component rated CVSS 3.1 10.0 (improper authentication, command injection) and an adjacent-network command injection (9.6); CVE ids pending, fixed in V11 R2.14, Security Mode restricted access is the workaround, no exploitation stated"
headline: "Mitel OpenScape 4000: two unauthenticated CVSS 10.0 Platform flaws; upgrade to V11 R2.14 or restrict access"
summary: >
  Mitel's advisory MISA-2026-0013 of 2026-11-18 covers three flaws in the Platform component of OpenScape 4000 and OpenScape 4000 Manager: an unauthenticated improper-authentication flaw and an unauthenticated command injection, both CVSS 3.1 10.0, and a command injection reachable from the adjacent network (9.6). CVE ids have been requested but not assigned; the fix is V11 R2.14, PLT HF5 on V11 R1.26 or a patch for V10 R0.28 to V11 R0.22, and enabling Security Mode restricted access is Mitel's workaround. The advisory says nothing about exploitation, and it is the second critical Mitel advisory in a week.
discovered_at: "2026-11-20T05:08:00Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-20T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: ["product:mitel-openscape-4000", "product:mitel-openscape-4000-manager"]
techniques: [T1190]
affected_products: ["Mitel OpenScape 4000", "Mitel OpenScape 4000 Manager"]
cves: []
sources:
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013"
    publisher: "Mitel (MISA-2026-0013)"
    date: "2026-11-18"
    role: primary
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1569/"
    publisher: "CERT-FR (CERTFR-2026-AVI-1569)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4685"
    publisher: "BSI CERT-Bund (WID-SEC-2026-4685)"
    date: "2026-11-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For customers who are not able to implement the recommended solution in a timely manner, enabling Security Mode restricted access can be used as a workaround to prevent exploitation of these vulnerabilities."
    publisher: "Mitel (MISA-2026-0013)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013"
  - quote: "These issues are corrected in OpenScape 4000 V11 R2.14. Also, Mitel has provided PLT HF5 for version OpenScape 4000 V11 R1.26, and patch for releases V10 R0.28 to V11 R0.22."
    publisher: "Mitel (MISA-2026-0013)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013"
verification: single-source
sourcing_note: >
  Mitel is the disclosing vendor for its own product; CERT-FR and BSI restate its advisory and add no independent assessment. CERT-FR words the affected range as versions before V11 R2.14 and V11 R1.x before R1.26 without PLT HF5, while Mitel's affected range ends at V11 R2.11, so R2.12 and R2.13 are not stated either way. The advisory carries no CVE ids and says nothing on exploitation or on whether the Platform interfaces are normally reachable from outside; the workaround article KB000129263 sits behind Mitel's customer portal.
confidence: high
references: ["2026-11-18/mitel-micollab-misa-2026-0012-awv-unauth-command-injection"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every OpenScape 4000 and OpenScape 4000 Manager to V11 R2.14, apply PLT HF5 on V11 R1.26 or Mitel's patch on V10 R0.28 to V11 R0.22, and until then enable Security Mode restricted access as Mitel's workaround article KB000129263 describes, because two unauthenticated Platform flaws are rated CVSS 10.0."
updates: []
migrated_from: null
---

Mitel's advisory MISA-2026-0013 of 2026-11-18 covers three flaws in the Platform component of OpenScape 4000 and OpenScape 4000 Manager, tracked by Mitel's internal ids because the CVE identifiers it requested are not yet assigned ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013)). MTLVULN-1785 is an unauthenticated improper-authentication flaw that gives unauthorized access and MTLVULN-1786 an unauthenticated command injection through insufficient parameter sanitization, both CVSS 3.1 10.0 with changed scope; MTLVULN-1793 is a command injection that an unauthenticated attacker with adjacent network access can use, scored 9.6 ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013)). Affected are OpenScape 4000 V11 R0.22 through V11 R2.11 and V10 R1.68 and earlier, and OpenScape 4000 Manager V11 R0.22 through V11 R2.11 and V10 R1.34, R1.42, R1.54 and R1.68; Mitel does not assess end-of-support releases ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013)).

The issues are corrected in V11 R2.14, Mitel provides PLT HF5 for V11 R1.26 and a patch for V10 R0.28 to V11 R0.22 (for the Manager, V10 R1.34 to V11 R0.22), and for customers who cannot apply the fix quickly, enabling Security Mode restricted access is a workaround that prevents exploitation, with the steps in a portal-only article ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013)). CERT-FR lists the risks as remote arbitrary code execution, remote denial of service, policy bypass and loss of integrity and confidentiality, and BSI describes an attacker who can bypass safeguards, disclose information or run arbitrary commands in the context of the system ([CERT-FR, 2026-11-19](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1569/); [BSI, 2026-11-19](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4685)). Mitel's text does not mention exploitation.

**Exposure:** OpenScape 4000 and OpenScape 4000 Manager at the releases above; the vulnerable component is the Platform, and the advisory does not say which of its interfaces are normally reachable ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013)).

**Detection:** unauthenticated access to the Platform component from hosts that are not administration or maintenance systems, and unexpected command execution on the platform; both follow from the improper-authentication and command-injection mechanisms, and the advisory gives no detection guidance.

**Defender takeaway:** apply the fix for the release in use now; where that waits, turn on Security Mode restricted access, and read the affected range against CERT-FR's wording if the system runs R2.12 or R2.13 ([Mitel, 2026-11-18](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0013); [CERT-FR, 2026-11-19](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1569/)).
