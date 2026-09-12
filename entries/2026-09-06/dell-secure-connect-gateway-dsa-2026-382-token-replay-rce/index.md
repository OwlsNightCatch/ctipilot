---
schema: 1
kind: vulnerability
title: "Dell Secure Connect Gateway DSA-2026-382: an unauthenticated request replayed indefinitely mints ADMIN tokens, and Dell ships no workaround for any of the 105 flaws"
headline: "Dell's on-prem support gateway takes a 105-CVE bundle with three critical unauthenticated paths and no mitigation short of patching"
summary: >
  Dell's DSA-2026-382, released 2026-08-31, fixes 105 proprietary-code CVEs in Secure Connect Gateway
  5.0, the on-premises gateway that carries diagnostics and remote-support traffic from a customer's
  Dell estate to Dell. CVE-2026-80172 (CVSS 9.8) lets an unauthenticated attacker replay one captured
  request without limit to mint ADMIN access and refresh tokens; CVE-2026-61410 (9.4) is
  unauthenticated remote command execution through a single crafted request; CVE-2026-80238 (9.3)
  turns SSH access into host root through an exposed Docker socket. Dell lists no workarounds:
  the fixed releases are Application version 5.36.00.00 and Appliance version 5.36.00.16. No
  exploitation is reported.
discovered_at: "2026-09-06T13:55:00Z"
updated_at: null
event_date: "2026-08-31"
run_id: 2026-09-06T1308Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, priv-esc, patch-available, supply-chain]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1190, "T1550.001", T1611, T1068]
affected_products: ["Dell Secure Connect Gateway"]
cves:
  - id: CVE-2026-80172
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Application < 5.36.00.00; Appliance < 5.36.00.16"
    fixed: "Application 5.36.00.00; Appliance 5.36.00.16"
  - id: CVE-2026-61410
    cvss: "9.4"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Application < 5.36.00.00; Appliance < 5.36.00.16"
    fixed: "Application 5.36.00.00; Appliance 5.36.00.16"
  - id: CVE-2026-80238
    cvss: "9.3"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "Application < 5.36.00.00; Appliance < 5.36.00.16"
    fixed: "Application 5.36.00.00; Appliance 5.36.00.16"
  - id: CVE-2026-61409
    cvss: "7.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Application < 5.36.00.00"
    fixed: "Application 5.36.00.00"
sources:
  - url: "https://www.dell.com/support/kbdoc/de-de/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-application-and-appliance-multiple-vulnerabilities"
    publisher: "Dell PSIRT (DSA-2026-382)"
    date: "2026-08-31"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3184"
    publisher: "BSI CERT-Bund (WID-SEC-2026-3184)"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This vulnerability is considered critical as an unauthenticated attacker can repeatedly reuse a captured request to generate ADMIN access and refresh tokens. Since there is no nonce validation or time limit on requests, the attack can be performed indefinitely."
    publisher: "Dell PSIRT (DSA-2026-382)"
  - quote: "a low-privileged operator with SSH access to the SCG host can gain root-level access to the host without requiring a password by leveraging the exposed Docker socket. Additionally, an attacker who compromises a service running within the orchestrator container can access the same socket and escape the container boundary to obtain host-level control."
    publisher: "Dell PSIRT (DSA-2026-382)"
  - quote: "it allows an attacker to execute commands remotely on a target system by sending a specially crafted request to the application, bypassing intended restrictions on code execution."
    publisher: "Dell PSIRT (DSA-2026-382)"
verification: single-source
sourcing_note: "Dell PSIRT as the primary disclosing party for its own product, with BSI CERT-Bund's WID-SEC-2026-3184 relaying the same bulletin rather than assessing it independently, so credibility stays at 2. The count of 105 proprietary-code CVEs and the CVSS figures are read from the advisory's own vulnerability table; one further third-party CVE (CVE-2025-26333 in BSAFE Crypto-J) is listed separately and is not counted in that total."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade every Dell Secure Connect Gateway to the fixed releases, Application version 5.36.00.00 or Appliance version 5.36.00.16; there is no interim mitigation, since Dell's advisory lists its workarounds as None."
  - "Until the upgrade lands, confirm no SCG instance answers from an untrusted segment, and treat SSH access to the SCG host as equivalent to root on it: any operator account with SSH reaches host root through the exposed Docker socket without a password."
updates: []
migrated_from: null
---

Dell's DSA-2026-382, released 2026-08-31 in its only revision to date, fixes 105 proprietary-code CVEs in Secure Connect Gateway 5.0, plus one third-party flaw in the BSAFE Crypto-J component ([Dell PSIRT, 2026-08-31](https://www.dell.com/support/kbdoc/de-de/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-application-and-appliance-multiple-vulnerabilities)). Secure Connect Gateway is the on-premises component that collects telemetry and diagnostics from a customer's Dell server, storage and networking estate and carries remote-support sessions back to Dell, so it sits inside the estate with broad reach into it and an outbound path to the vendor. Three of the 105 score 9.0 or above; the remainder run from 2.4 to 8.2 and include further hard-coded credentials, certificate-validation bypasses, path traversal and command injection, most of them also reachable without authentication.

The one that changes the exposure calculation is CVE-2026-80172 (CVSS 9.8), an insufficient-verification-of-data-authenticity flaw. Dell's own description states that an unauthenticated attacker "can repeatedly reuse a captured request to generate ADMIN access and refresh tokens" and that "there is no nonce validation or time limit on requests, the attack can be performed indefinitely" ([Dell PSIRT, 2026-08-31](https://www.dell.com/support/kbdoc/de-de/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-application-and-appliance-multiple-vulnerabilities)). A single request observed once, at any point in the gateway's history, remains a working administrative credential for as long as the gateway stays unpatched: there is no expiry to wait out and no session to terminate. CVE-2026-61410 (9.4) is a missing-authorization flaw that Dell describes as letting an attacker "execute commands remotely on a target system by sending a specially crafted request to the application, bypassing intended restrictions on code execution", reported alongside sibling flaws CVE-2026-61409 and CVE-2026-61408 by the researcher credited as Saltedfish. CVE-2026-61409 (7.3) is an OS command injection Dell also records as reachable by an unauthenticated attacker with remote access, and unlike the other three its advisory row names only the Application component, not the Appliance ([Dell PSIRT, 2026-08-31](https://www.dell.com/support/kbdoc/de-de/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-application-and-appliance-multiple-vulnerabilities)).

CVE-2026-80238 (9.3) is the local half. Dell states that "a low-privileged operator with SSH access to the SCG host can gain root-level access to the host without requiring a password by leveraging the exposed Docker socket", and that an attacker who compromises any service inside the orchestrator container "can access the same socket and escape the container boundary to obtain host-level control" ([Dell PSIRT, 2026-08-31](https://www.dell.com/support/kbdoc/de-de/000503426/dsa-2026-382-security-update-for-dell-secure-connect-gateway-application-and-appliance-multiple-vulnerabilities)). The gateway's own container boundary therefore provides no isolation, which matters because the unauthenticated remote paths above land inside it. Dell's advisory records its workarounds as None: Application versions before 5.36.00.00 and Appliance versions before 5.36.00.16 are affected, and upgrading to those releases is the only control the vendor offers. Germany's BSI CERT-Bund relayed the same bulletin as WID-SEC-2026-3184 on 2026-09-03 ([BSI CERT-Bund, 2026-09-03](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3184)). Neither Dell nor any secondary source reports exploitation or a public proof-of-concept; every issue was privately reported.

**Defender takeaway:** this is the pre-exploitation window on an unauthenticated, replayable path to administrative control of a device that already holds privileged reach into the hardware estate, and there is no configuration change that buys time. Treat the upgrade as out-of-band rather than next-cycle work. Because CVE-2026-80172 replays a previously captured request, patching alone does not answer whether a token was already minted: after upgrading, review the gateway's own administrative audit trail for API sessions that do not correspond to a known operator or a scheduled Dell support session, and for administrative activity outside the hours the support workflow runs. On the local path, an SSH login by a low-privileged operator account followed by container-runtime activity from that session is the observable shape of CVE-2026-80238.

**Triage:** Secure Connect Gateway legitimately opens outbound sessions to Dell and legitimately performs privileged collection across the estate, so outbound connections and broad read access from the SCG host are normal and are not the signal. What separates abuse is direction and origin: an inbound request to the gateway's API from a source that is neither an administrator workstation nor the Dell support path, an administrative token in use from an address the operator team does not recognise, or container-runtime commands issued from an interactive SSH session rather than from the gateway's own orchestration.
