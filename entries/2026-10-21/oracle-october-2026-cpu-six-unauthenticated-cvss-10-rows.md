---
schema: 1
kind: vulnerability
title: "Oracle October 2026 Critical Patch Update: six unauthenticated network CVSS 10.0 rows in Access Manager, SOA Suite, E-Business Suite and JD Edwards, and WebLogic CVSS 9.8 flaws reachable over HTTP and T3/IIOP"
headline: "Oracle's October CPU carries six unauthenticated CVSS 10.0 rows and two WebLogic 9.8 flaws; none is reported exploited"
summary: >
  Oracle's Critical Patch Update of 2026-10-20 carries 1295 new patches. Its risk matrices list 90 rows (73 distinct CVE ids)
  scored CVSS 3.1 9.0 or higher that need no authentication over the network, among them six at 10.0 in Access Manager, SOA Suite
  (three), E-Business Suite Workflow Notification Mailer and JD Edwards EnterpriseOne Orchestrator, and two WebLogic Server
  flaws at 9.8 reachable over HTTP and over T3 and IIOP. The advisory states no exploitation for any row, and it points to
  My Oracle Support documents for patch availability.
discovered_at: "2026-10-21T03:41:00Z"
updated_at: null
event_date: "2026-10-20"
run_id: 2026-10-21T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, patch-available]
regions: [global]
sectors: []
entities: []
techniques: [T1190, T1059.004]
affected_products: ["Oracle WebLogic Server", "Oracle SOA Suite", "Oracle Access Manager", "Oracle Identity Manager", "Oracle E-Business Suite", "Oracle JD Edwards EnterpriseOne"]
cves:
  - id: CVE-2026-87337
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0 and 14.1.2.1.0, Authentication Engine component, reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91231
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle SOA Suite 12.2.1.4.0 and 14.1.2.0.0, Adapters component, reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91216
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle SOA Suite 12.2.1.4.0 and 14.1.2.0.0, Fabric Layer component, reachable over T3 and IIOP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91221
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle SOA Suite 12.2.1.4.0 and 14.1.2.0.0, Fabric Layer component, reachable over T3 and IIOP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-101809
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Workflow Notification Mailer component, reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-101767
    cvss: "9.8 (CVSS 3.1)"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle E-Business Suite 12.2.3 to 12.2.15, Application Object Library Core component (Thin Client Framework servlet), reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91299
    cvss: "10.0"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle JD Edwards EnterpriseOne 9.2.0.0 to 9.2.26.5, E1 IOT Orchestrator Security component (Orchestrator), reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91323
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0, Core component, reachable over HTTP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-83399
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0, Core component, reachable over T3 and IIOP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-87302
    cvss: "9.1"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0, Core component, reachable over HTTP; Oracle's matrix rates availability impact None"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-91408
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Identity Manager 12.2.1.4.0 and 14.1.2.1.0, End User Self Service component, reachable over T3 and IIOP"
    fixed: "October 2026 Critical Patch Update"
  - id: CVE-2026-87251
    cvss: "9.8"
    epss: null
    type: null
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Oracle Access Manager 12.2.1.4.0 and 14.1.2.1.0, Authentication Engine component, reachable over SAML"
    fixed: "October 2026 Critical Patch Update"
sources:
  - url: "https://www.oracle.com/security-alerts/cpuoct2026.html"
    publisher: "Oracle (Critical Patch Update Advisory, October 2026)"
    date: "2026-10-20"
    role: primary
  - url: "https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/"
    publisher: "Horizon3.ai (CVE-2026-101767 write-up)"
    date: "2026-10-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This Critical Patch Update contains 1295 new security patches across the product families listed below."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cpuoct2026.html"
  - quote: "Oracle continues to periodically receive reports of attempts to maliciously exploit vulnerabilities for which Oracle has already released security patches."
    publisher: "Oracle"
    source_url: "https://www.oracle.com/security-alerts/cpuoct2026.html"
verification: single-source
sourcing_note: >
  Oracle's advisory is the primary source, a vendor advisory for its own products, and Horizon3, which reported
  CVE-2026-101767, is the source for that flaw's chain and indicators; the counts (112 rows at 9.0 or higher,
  90 of them unauthenticated over the network, 73 distinct ids) are a tally of its risk matrices, where an id that
  affects several products appears once per product. Oracle states no exploitation, and no third-party report of
  exploitation or a proof of concept was found for these ids on 2026-10-21 or 2026-10-25.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-10-25T14:09:42Z"
    run_id: 2026-10-25T1308Z-audit
    type: improvement
    summary: >
      Adds the E-Business Suite flaw CVE-2026-101767 (CVSS 9.8, unauthenticated over HTTP), whose
      discoverer Horizon3 described the SQL-injection-to-command-execution chain, the
      default-configuration exposure, an interim mitigation and behavioural indicators on the release day,
      without exploit code; the Exposure, Detection and takeaway lines carry them.
    fields: [cves, techniques, sources, sourcing_note, body]
migrated_from: null
---

Oracle's Critical Patch Update advisory of 2026-10-20 contains 1295 new security patches ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)). Its risk matrices score 112 rows at CVSS 3.1 9.0 or higher, and 90 of those, covering 73 distinct CVE ids, are marked as remotely exploitable without authentication with a network attack vector ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)). Six rows score 10.0: CVE-2026-87337 in the Access Manager Authentication Engine (HTTP), CVE-2026-91231 in the SOA Suite Adapters (HTTP), CVE-2026-91216 and CVE-2026-91221 in the SOA Suite Fabric Layer (T3 and IIOP), CVE-2026-101809 in the E-Business Suite Workflow Notification Mailer (HTTP, 12.2.3 to 12.2.15) and CVE-2026-91299 in the JD Edwards EnterpriseOne Orchestrator security component (HTTP, 9.2.0.0 to 9.2.26.5) ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)). WebLogic Server 12.2.1.4.0, 14.1.1.0.0, 14.1.2.0.0 and 15.1.1.0.0 carry CVE-2026-91323 (HTTP) and CVE-2026-83399 (T3 and IIOP) at 9.8 and CVE-2026-87302 (HTTP) at 9.1; Identity Manager's End User Self Service has CVE-2026-91408 (T3 and IIOP, 9.8) and Access Manager's SAML path CVE-2026-87251 (9.8) ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)). The advisory states no exploitation for any row and carries only Oracle's standing sentence that it receives reports of attempts to exploit already-patched flaws ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)). Oracle points to My Oracle Support documents for patch availability ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)).

**Exposure:** a WebLogic, SOA Suite, Access Manager or Identity Manager server whose HTTP, T3 or IIOP listener, or SAML endpoint, answers from a network that is not the management network; an E-Business Suite 12.2.3 to 12.2.15 web tier with the Workflow Notification Mailer, or whose URL firewall allows the Thin Client Framework servlet, as the default configuration does ([Horizon3.ai, 2026-10-20](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/)); a JD Edwards EnterpriseOne 9.2 server with the Orchestrator. The product version comes from the product's own version command or the inventory.

**Detection:** Oracle names no indicator. For the E-Business Suite flaw CVE-2026-101767, Horizon3 lists unauthenticated POST requests to the Thin Client Framework servlet followed by backend database activity, SQL reconnaissance shortly after unauthenticated web requests, and the oracle account spawning a shell through the Concurrent Manager ([Horizon3.ai, 2026-10-20](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/)). Otherwise watch web and application-server access logs and the WebLogic and SOA server logs for requests to the affected components from untrusted sources, T3 and IIOP connections from unexpected networks in flow or load-balancer logs, and Java process-creation events where the middleware process spawns a shell, an interpreter or a download tool.

**Defender takeaway:** apply the October 2026 update to the six 10.0 components first wherever they are reachable beyond the management network, together with any E-Business Suite web tier exposed to CVE-2026-101767, whose chain Horizon3 has described, then to the WebLogic and Identity Manager rows; where a patch cannot go in at once, take T3, IIOP and the administration console off untrusted networks and remove the Thin Client Framework servlet from the EBS URL firewall allowlist ([Horizon3.ai, 2026-10-20](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/)). Oracle's next scheduled update is the Critical Security Patch Update of 17 November 2026 ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)).

## Improvement — 2026-10-25T14:09:42Z

Horizon3, which reported CVE-2026-101767 to Oracle on 2026-07-24, described the chain on release day, without publishing exploit code. An unauthenticated SQL injection in the Thin Client Framework servlet of E-Business Suite 12.2.3 to 12.2.15 (Application Object Library, Core component, CVSS 3.1 9.8), which the default EBS URL firewall configuration permits, gives SQL execution as the APPS database user and then operating-system commands as the EBS application account ([Horizon3.ai, 2026-10-20](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/)). Until the update is in, Horizon3 advises removing the servlet from the URL firewall allowlist and restricting the web tier to trusted networks, measures that reduce exposure but do not replace patching ([Horizon3.ai, 2026-10-20](https://horizon3.ai/attack-research/vulnerabilities/cve-2026-101767/)). Oracle scores the row 9.8, unauthenticated over HTTP ([Oracle, 2026-10-20](https://www.oracle.com/security-alerts/cpuoct2026.html)).
