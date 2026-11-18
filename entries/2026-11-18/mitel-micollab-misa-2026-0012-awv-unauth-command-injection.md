---
schema: 1
kind: vulnerability
title: "Mitel MiCollab 10.3 (10.3.0.18) and earlier, MISA-2026-0012: an unauthenticated blind command injection in the Audio, Web and Video Conferencing component (CVSS 3.1 10.0) and four more flaws there, one an XML injection that can run commands (9.0); CVE ids pending, patch KB000129195, no exploitation stated"
headline: "Mitel MiCollab: unauthenticated CVSS 10.0 command injection in the conferencing component; patch KB000129195"
summary: >
  Mitel's advisory MISA-2026-0012 of 2026-11-16 covers five flaws in the Audio, Web and Video Conferencing (AWV) component of MiCollab 10.3 (10.3.0.18) and earlier, led by an unauthenticated blind command injection scored CVSS 3.1 10.0 and an unauthenticated XML injection scored 9.0 that could run commands. CVE ids have been requested but not assigned, Mitel offers a patch through its portal (KB000129195) and says restricting external access to the AWV component reduces the risk, and neither Mitel nor any national authority states exploitation. The 10.3.0.18 release that Mitel named as the fix for its July advisory is itself in the affected range.
discovered_at: "2026-11-18T05:11:00Z"
updated_at: null
event_date: "2026-11-16"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["Mitel MiCollab"]
cves: []
sources:
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
    publisher: "Mitel (MISA-2026-0012)"
    date: "2026-11-16"
    role: primary
  - url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006"
    publisher: "Mitel (MISA-2026-0006)"
    date: "2026-07-22"
    role: corroborating
  - url: "https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/"
    publisher: "CERT-FR (CERTFR-2026-AVI-1547)"
    date: "2026-11-17"
    role: corroborating
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608"
    publisher: "BSI CERT-Bund (WID-SEC-2026-4608)"
    date: "2026-11-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "could allow an unauthenticated attacker to conduct a blind command injection attack due to insufficient parameter sanitization."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
  - quote: "the risk may be mitigated by restricting external access to the AWV component."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
  - quote: "Exploiting these vulnerabilities together can significantly amplify their impact."
    publisher: "Mitel (MISA-2026-0012)"
    source_url: "https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012"
verification: single-source
sourcing_note: >
  Mitel is the disclosing vendor for its own product; CERT-FR and BSI restate its advisory. They word the affected range as versions before 10.3.0.18, while Mitel's page says 10.3 (10.3.0.18) and earlier and asks customers to upgrade to that release and apply the patch, so the vendor's wording is followed. Mitel's text for the 10.0 flaw is garbled in the original ("requires could allow") and may have lost a stated precondition. The advisory says nothing either way about exploitation or public exploit code. The patch article sits behind Mitel's customer portal.
confidence: high
references: ["2026-07-24/mitel-micollab-awv-unauth-command-injection"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Apply Mitel's patch KB000129195 to every MiCollab on 10.3 (10.3.0.18) or earlier, including systems already moved to 10.3.0.18 for the July advisory, and until it is in, restrict external access to the Audio, Web and Video Conferencing component, because Mitel scores one unauthenticated flaw CVSS 10.0 and says the five flaws together amplify the impact."
updates: []
migrated_from: null
---

Mitel's advisory MISA-2026-0012, first issued on 2026-11-16, covers five flaws in the Audio, Web and Video Conferencing (AWV) component of MiCollab 10.3 (10.3.0.18) and earlier; Mitel tracks them by internal ids because the CVE identifiers it requested are not yet assigned ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). MTLVULN-1864 lets an unauthenticated attacker conduct a blind command injection through insufficient parameter sanitization and is scored CVSS 3.1 10.0 with changed scope; MTLVULN-1862 lets an unauthenticated attacker leverage pre-staged malicious content for an XML injection that could run arbitrary commands, scored 9.0 with high attack complexity ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Three further flaws are rated Medium: an unauthenticated arbitrary file upload through weak file-type validation (MTLVULN-1861, 5.3), unauthorized access that needs a system-generated random identifier or pre-staged content (MTLVULN-1863, 5.9) and an authentication bypass (MTLVULN-1877, 5.3) ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Mitel says exploiting them together can significantly amplify their impact ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).

The fix is a patch for release 10.3 (10.3.0.18), delivered through knowledge-base article KB000129195 on Mitel's customer portal, or an upgrade to a later release that Mitel does not name; Mitel's partners can supply it to customers without portal access ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)). Mitel's July advisory named 10.3 (10.3.0.18) as the release that fixed its earlier AWV command injection, so a system moved there in July is inside the new affected range ([Mitel, 2026-07-22](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006)). CERT-FR lists the advisory on 2026-11-17 and BSI rates it high, describing a remote anonymous attacker who can manipulate files, run code with the service's rights and bypass security measures ([CERT-FR, 2026-11-17](https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1547/); [BSI, 2026-11-17](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4608)).

**Exposure:** MiCollab 10.3 (10.3.0.18) and earlier whose AWV component external users can reach; Mitel assesses only supported versions and states no branch before 10.3 ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).

**Detection:** child processes of the AWV service, new files in the component's upload paths and unauthenticated requests to conferencing endpoints that carry shell metacharacters or XML payloads, which follow from the command-injection, upload and XML-injection mechanisms the advisory names ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).

**Defender takeaway:** apply the patch now; where that waits, restrict external access to the AWV component, the mitigation Mitel names ([Mitel, 2026-11-16](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0012)).
