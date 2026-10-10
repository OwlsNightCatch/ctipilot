---
schema: 1
kind: threat
title: CERT Polska discloses a JAR parser-confusion RCE in the SzafirHost e-signature client (CVE-2026-13165)
headline: CERT Polska discloses a JAR parser-confusion RCE in the SzafirHost e-signature client (CVE-2026-13165)
summary: "A Polish e-signature client, SzafirHost from Krajowa Izba Rozliczeniowa (CVE-2026-13165), carries a JAR parser-confusion RCE that smuggles a malicious native library past signature verification (CERT Polska, 2026-06-29); and China-nexus Mustang Panda is abusing Zoho WorkDrive as a dead-drop C2 channel against government and energy targets — both with directly transferable lessons for EU public-sector defenders (qualified e-signature tooling; SaaS-as-C2)."
discovered_at: "2026-06-30T05:10:33Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - supply-chain
  - rce
regions:
  - europe
sectors:
  - public-sector
  - finance
entities: []
cves:
  - id: CVE-2026-13165
    cvss: n/a
    epss: null
    type: rce
    vector: user-interaction
    auth: pre-auth
    status:
      - patch-available
sources:
  - url: "https://cert.pl/en/posts/2026/06/CVE-2026-13165/"
    publisher: CERT Polska
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-30.md
---

CERT Polska disclosed CVE-2026-13165 in SzafirHost, a Java-based e-signature and trusted-timestamping client developed by Krajowa Izba Rozliczeniowa (KIR) ([CERT Polska, 2026-06-29](https://cert.pl/en/posts/2026/06/CVE-2026-13165/)). The bug — assigned CWE-434 (Unrestricted Upload of File with Dangerous Type) — is a Java parser-confusion leading to remote code execution: SzafirHost verifies a JAR's signature with `JarFile` (which reads the ZIP Central Directory at the end of the archive) but extracts with `JarInputStream` (which walks local file headers sequentially). An attacker who can deliver a crafted JAR — for example a tampered update package or document — embeds a malicious native library between the last legitimate entry and the Central Directory; the signature walk never sees the injected entry (and archive-size validation still passes), but extraction writes the library to disk without hash verification, where it is then loaded and executed. CERT-PL is the disclosing authority and reports no in-the-wild exploitation; the fix is SzafirHost v1.2.2.

**Why it matters to us:** Qualified e-signature clients like SzafirHost sit in eIDAS-regulated document workflows used across EU public administration and finance, and they routinely process externally-supplied signed files — exactly the delivery path this bug needs. Inventory SzafirHost versions on signing workstations and push v1.2.2; the underlying `JarFile`-vs-`JarInputStream` confusion is a transferable hunting pattern for any Java signature-verification tooling. Detection concept: watch for unexpected native-library creation in Java temp directories during SzafirHost invocation, and JVM startup arguments referencing unexpected library paths.
