---
schema: 1
kind: vulnerability
title: "Apereo CAS: an embargoed remote-code-execution disclosure affects every 7.3.x deployment regardless of configuration — patched to 7.3.8.3, no CVE or technical detail published yet"
headline: "Apereo's own advisory: \"you are affected if you simply run CAS\" — patch now, technical detail is still under embargo"
summary: >
  Apereo, the project behind the CAS single sign-on/identity-provider server widely deployed across
  higher education and government portals, disclosed on 2026-09-08 a vulnerability affecting every
  CAS 7.3.x deployment "regardless of configuration" that "will lead to remote code execution
  attempts." Fixed the same day in CAS 7.3.8.3; no CVE, CVSS score, or technical detail has been
  published, under the project's formal grace-window disclosure process.
discovered_at: "2026-09-11T04:36:00Z"
event_date: "2026-09-08"
run_id: 2026-09-11T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, patch-available]
regions: [global, europe]
sectors: [public-sector, education, technology]
entities: []
techniques: [T1190]
affected_products: ["Apereo CAS"]
cves: []
sources:
  - url: "https://apereo.github.io/2026/09/08/vuln/"
    publisher: "Apereo Community Blog (CAS project)"
    date: "2026-09-08"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1150/"
    publisher: "CERT-FR / ANSSI (CERTFR-2026-AVI-1150)"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The issue addressed here is not tied or connected to a specific feature or extension of the CAS software, and ultimately will lead to remote code execution attempts. While the affected area largely has to do with UI, the specific nature of the issue has nothing to do with whether the CAS deployment has customized the user interface or runs with a custom theme."
    publisher: "Apereo Community Blog (CAS project)"
    source_url: "https://apereo.github.io/2026/09/08/vuln/"
  - quote: "You are affected if you simply run CAS."
    publisher: "Apereo Community Blog (CAS project)"
    source_url: "https://apereo.github.io/2026/09/08/vuln/"
  - quote: "The issues were originally reported to the CAS project on September 4th, 2026 and fixed on September 8th, 2026."
    publisher: "Apereo Community Blog (CAS project)"
    source_url: "https://apereo.github.io/2026/09/08/vuln/"
  - quote: "The issues (almost entirely driven by AI analysis) were reported to the CAS project by third-party researchers (who decided to remain anonymous) and were then further validated and tested by the CAS security team."
    publisher: "Apereo Community Blog (CAS project)"
    source_url: "https://apereo.github.io/2026/09/08/vuln/"
  - quote: "A vulnerability has been discovered in Apereo CAS. It allows an attacker to cause arbitrary remote code execution. (translated from French)"
    original: "Une vulnérabilité a été découverte dans Apereo CAS. Elle permet à un attaquant de provoquer une exécution de code arbitraire à distance."
    publisher: "CERT-FR / ANSSI"
    source_url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1150/"
verification: multi-source
sourcing_note: >
  Confidence held at medium rather than high because Apereo has deliberately withheld the
  vulnerable component, the CWE class, the authentication precondition and any CVSS score during
  its disclosure grace window ("additional details will be provided once the security grace window
  passes") — the fact of the flaw and the patch are two-source verified (the project's own
  disclosure plus CERT-FR's independent advisory the same window), but the technical substance a
  Tier 2/3 responder would want is not yet public from any source. No CVE has been assigned as of
  this writing, so no CVE identifier is recorded here.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Apereo CAS 7.3.x deployment to the patched 7.3.8.3 release now, without waiting for the technical write-up Apereo says will follow once the grace window passes — the vendor states the issue affects any standard deployment regardless of feature use, customization or theme."
updates: []
migrated_from: null
---

Apereo, the open-source project behind CAS (Central Authentication Service) — a widely deployed SSO/identity-provider server used across higher education and, per CERT-FR's advisory the same day, flagged to the French government constituency — disclosed a vulnerability on 2026-09-08 under its formal grace-window vulnerability-response process, which withholds technical detail for a period after the fix ships ([Apereo Community Blog, 2026-09-08](https://apereo.github.io/2026/09/08/vuln/)). What Apereo does state: the issue is not tied to any specific feature, extension, customized UI or theme, and "you are affected if you simply run CAS"; exploitation "will lead to remote code execution attempts" ([Apereo Community Blog, 2026-09-08](https://apereo.github.io/2026/09/08/vuln/)). The affected release line is 7.3.x. A third party, working anonymously and describing its analysis as "almost entirely driven by AI," reported the issue on 2026-09-04, and Apereo's security team validated, tested and shipped the fix as CAS 7.3.8.3 on 2026-09-08 — described as a drop-in replacement for standard deployments ([Apereo Community Blog, 2026-09-08](https://apereo.github.io/2026/09/08/vuln/)). No CVE identifier or CVSS score has been published as of this writing — an unusual gap for an RCE-class disclosure. CERT-FR (ANSSI) independently carried the advisory the same window, rating the risk "arbitrary remote code execution" (translated from French) ([CERT-FR, 2026-09-10](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1150/)).

Because Apereo's own language deliberately omits the vulnerable component, the authentication precondition and the trigger mechanism during the embargo window, this is patch-now guidance rather than a hunt-and-detect brief: organizations running CAS 7.3.x should upgrade to the fixed 7.3.8.3 release without waiting for the technical write-up Apereo says will follow once the grace window passes.

**Defender takeaway:** CAS is commonly a single point of failure for an institution's whole authentication surface, so a "you are affected if you simply run CAS" advisory on an RCE-class issue warrants the same urgency as a confirmed pre-auth flaw even before the technical detail lands — patch to 7.3.8.3 now, and treat the coming technical write-up as the trigger to re-check for any signs of prior exploitation once the specifics are known.

