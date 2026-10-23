---
schema: 1
kind: vulnerability
title: "Fortinet FortiSandbox GUI authentication bypass (CVE-2026-107656, CVSS 9.6) and FortiSIEM 7.5.0 unauthenticated path traversal to code execution (CVE-2026-106173, CVSS 9.4): both critical, fixed 2026-10-13, neither reported exploited"
headline: "FortiSandbox GUI auth bypass (9.6) and FortiSIEM 7.5.0 pre-auth code execution (9.4) fixed; no exploitation listed"
summary: >
  Fortinet's PSIRT published two critical unauthenticated advisories on 2026-10-13: an authentication bypass in the FortiSandbox GUI
  (CVE-2026-107656, CVSS 3.1 9.6; fixed in 5.0.7 and 4.4.10) and a path traversal in the FortiSIEM phQueryMaster service that allows
  code execution (CVE-2026-106173, 9.4; FortiSIEM 7.5.0 only, fixed in 7.5.1, workaround: restrict tcp port 27918). Fortinet lists
  neither as known to be exploited. The FortiSandbox ranges include 5.0.6 and 4.4.9, the builds that fixed CVE-2026-25089, one of three
  FortiSandbox flaws reported exploited in June, so a unit patched for that one is still affected.
discovered_at: "2026-10-23T04:25:40Z"
updated_at: null
event_date: "2026-10-13"
run_id: 2026-10-23T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, auth-bypass, rce, patch-available]
regions: [global]
sectors: []
entities: ["product:fortinet-fortisandbox", "product:fortinet-fortisandbox-paas", "product:fortinet-fortisiem"]
techniques: [T1190]
affected_products: ["Fortinet FortiSandbox", "Fortinet FortiSandbox PaaS", "Fortinet FortiSIEM"]
cves:
  - id: CVE-2026-107656
    cvss: "9.6 (CVSS 3.1)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiSandbox 5.0.0 to 5.0.6 and 4.4.0 to 4.4.9; FortiSandbox PaaS 5.0.0 to 5.0.6 and all 4.4 versions"
    fixed: "FortiSandbox 5.0.7 and 4.4.10 (5.2 not affected); FortiSandbox PaaS 5.0.7, 4.4 migrates to a fixed release"
  - id: CVE-2026-106173
    cvss: "9.4 (CVSS 3.1)"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "FortiSIEM 7.5.0"
    fixed: "FortiSIEM 7.5.1 (7.6 and FortiSIEM Cloud not affected); workaround: restrict access on tcp port 27918"
sources:
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-185"
    publisher: "Fortinet PSIRT (FG-IR-26-185)"
    date: "2026-10-13"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-180"
    publisher: "Fortinet PSIRT (FG-IR-26-180)"
    date: "2026-10-13"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/16/fortisandbox-vulnerabilities-cve-2026-39813-cve-2026-39808-cve-2026-25089/"
    publisher: "Help Net Security"
    date: "2026-06-16"
    role: corroborating
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-141"
    publisher: "Fortinet PSIRT (FG-IR-26-141)"
    date: "2026-06-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "may allow a remote unauthenticated attacker to bypass authentication via crafted HTTP requests"
    publisher: "Fortinet PSIRT (FG-IR-26-185)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-185"
  - quote: "may allow an unauthenticated attacker to execute unauthorized code or commands via specially crafted packets"
    publisher: "Fortinet PSIRT (FG-IR-26-180)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-180"
  - quote: "Restricting access on tcp port 27918 prevents the issue."
    publisher: "Fortinet PSIRT (FG-IR-26-180)"
    source_url: "https://fortiguard.fortinet.com/psirt/FG-IR-26-180"
verification: single-source
sourcing_note: >
  Fortinet's PSIRT is the first-party source for both flaws, the affected ranges and the workaround; no independent reporting was
  found. The exploitation status, the CVSS score and the CVE identifiers are fields on the advisory pages, not part of the advisory text.
confidence: high
references: ["2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm", "2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Check every FortiSandbox that was upgraded to 5.0.6 or 4.4.9 after the exploited-flaw advisories of this year: those builds are still affected by CVE-2026-107656 and need 5.0.7 or 4.4.10; on FortiSIEM 7.5.0 install 7.5.1, or until then restrict access to tcp 27918 as Fortinet's workaround says."
updates: []
migrated_from: null
---

Fortinet's PSIRT published two critical advisories for security-operations products on 2026-10-13. FG-IR-26-185 describes an authentication bypass through an alternate path or channel in the FortiSandbox GUI that a remote unauthenticated attacker can trigger with crafted HTTP requests, listed as CVE-2026-107656 with CVSS 3.1 9.6 and an impact of unauthorized code or command execution ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185)). FG-IR-26-180 describes a path traversal in the FortiSIEM phQueryMaster service ("arbitrary file write in grpc phQueryMaster") that lets an unauthenticated attacker execute unauthorized code or commands through specially crafted packets, listed as CVE-2026-106173 with CVSS 3.1 9.4 ([Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)). Both pages state that neither flaw is known to be exploited, and both carry temporal vector strings with an exploit-code maturity of functional (FortiSandbox) and high (FortiSIEM) that the advisories do not explain ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185); [Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)).

For FortiSandbox, versions 5.0.0 through 5.0.6 and 4.4.0 through 4.4.9 are affected and 5.0.7 and 4.4.10 fix it; 5.2 is not affected; FortiSandbox PaaS 5.0.0 through 5.0.6 is affected, and every PaaS 4.4 version must migrate to a fixed release ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185)). The ranges include 5.0.6 and 4.4.9 ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185)). Defused reported exploitation of three FortiSandbox flaws in June, CVE-2026-39813, CVE-2026-39808 and CVE-2026-25089 ([Help Net Security, 2026-06-16](https://www.helpnetsecurity.com/2026/06/16/fortisandbox-vulnerabilities-cve-2026-39813-cve-2026-39808-cve-2026-25089/)), and the build that fixes CVE-2026-25089 is 5.0.6 on the 5.0 branch and 4.4.9 on 4.4 ([Fortinet PSIRT FG-IR-26-141, 2026-06-09](https://fortiguard.fortinet.com/psirt/FG-IR-26-141)), so a unit patched for that flaw is not patched for this one. For FortiSIEM only 7.5.0 is affected and 7.5.1 fixes it; 7.6 and FortiSIEM Cloud are not affected, and Fortinet's workaround is to restrict access on tcp port 27918 ([Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)).

**Exposure:** FortiSandbox appliances, virtual machines and PaaS instances on the affected ranges whose GUI an unauthenticated client can reach, and FortiSIEM 7.5.0 nodes where tcp port 27918 is reachable from outside the deployment ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185); [Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)).

**Detection:** Fortinet publishes no indicator or post-compromise check for either flaw ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185); [Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)). The behaviors to look for follow from the mechanisms: on FortiSandbox, administrator-level GUI actions that have no matching login event, and on FortiSIEM, connections to tcp port 27918 from addresses outside the deployment followed by new files or processes on the node.

**Defender takeaway:** move FortiSandbox to 5.0.7 or 4.4.10 (PaaS 4.4 migrates) and FortiSIEM 7.5.0 to 7.5.1; a FortiSandbox at 5.0.6 or 4.4.9 still needs this upgrade ([Fortinet PSIRT FG-IR-26-185, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-185); [Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)). Fortinet's only workaround is for FortiSIEM, restricting access on tcp port 27918 ([Fortinet PSIRT FG-IR-26-180, 2026-10-13](https://fortiguard.fortinet.com/psirt/FG-IR-26-180)); it names none for FortiSandbox, where limiting GUI access to an administrator network is the usual precaution rather than a Fortinet instruction.
