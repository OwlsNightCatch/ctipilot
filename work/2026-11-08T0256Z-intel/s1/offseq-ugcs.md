---
title: Authentication bypass with empty credentials in the UgCS drone ground-control server – OffSeq
url: https://offseq.com/en/research/ugcs-cve-2026-59104/
hostname: offseq.com
description: The UgCS server's HCI protocol login handler treats empty credentials as "use the only user" whenever the user database holds exactly one account – the default…
sitename: OffSeq
date: "2026-06-30"
fingerprint: "7bc9c75acc89d1df"
---
[All results](https://offseq.com/en/case-studies/)

Vulnerability disclosure

# Authentication bypass with empty credentials in the UgCS drone ground-control server

UgCS server (\< 6.2) – SPH Engineering

CVE-2026-59104 is an authentication bypass OffSeq found in UgCS, the SPH Engineering drone ground-control software. The server's HCI protocol login handler treats empty credentials as "use the only user" whenever the user database holds exactly one account – which is the default single-operator install. Because the service listens on all interfaces without TLS by default, any attacker who can reach TCP port 3334 gets a fully authenticated session with no credential at all, and can then issue privileged commands, including commanding connected drones and uploading flight routes. SPH Engineering fixed it in UgCS 6.2.

OffSeq

5 min read

Severity: CriticalCVSS 9.8CVE-2026-59104

## Key facts

- Identifier
- CVE-2026-59104
- Class
- Authentication bypass (CWE-287, CWE-305)
- Severity
- Critical
- CVSS
- 9.8
- CVSS 4.0
- 9.3 (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
- Vendor
- SPH Engineering
- Affected
- UgCS for Windows, macOS and Linux (\< 6.2)
- Fixed in
- UgCS 6.2
- Coordinated by
- CERT.LV
- Disclosed
- 2026
- Status
- Fixed; CVE assigned
- Role
- Reporter (finder)

## CVSS base score

/ 10Critical

Every score is built from eight plain questions about how an attack works and what it costs you.

### How hard it is to exploit

### What the attacker can do

Select a metric to see what it means

CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

[§ 01](https://offseq.com#s-01)

## § 01. Overview

UgCS is drone ground-control software from SPH Engineering, used to plan and fly missions and to command unmanned aircraft. Its server exposes an HCI (host-computer integration) protocol on TCP port 3334 so that other software can log in and drive the platform – read state, issue commands, and upload flight routes.

OffSeq found that the HCI login handler lets a client authenticate with no credentials at all. When the user database contains exactly one account – the default for a single-operator installation – a login request with empty login and password fields is resolved to that one user and the session is fully authenticated. Because the listener binds to every interface without TLS by default, this turns a local convenience into a remote authentication bypass that any host on the network can use. It is tracked as CVE-2026-59104, coordinated by [CERT.LV](https://cert.lv/en/).

[§ 02](https://offseq.com#s-02)

## § 02. Empty credentials as a login

The HCI `LoginHandler` accepts a `LoginRequest` carrying a client identifier, a user login and a user password. When the login and password fields are absent, the handler does not reject the request as invalid. Instead, if the user database holds exactly one user, it resolves the empty credentials to that single account and returns a `LoginResponse` for a fully authenticated session.

That session is not degraded or read-only. It carries the privileges of the resolved operator, so from it a client can issue the platform's privileged commands – including those that command connected drones and upload or modify flight routes.

[§ 03](https://offseq.com#s-03)

## § 03. Root cause: a local convenience exposed to the network

The behaviour is a convenience path. On a local, single-operator machine, letting the operator connect without retyping credentials is a usability choice, and "the only user" is an unambiguous target. The flaw is that the same service is network-exposed by default: it binds to `0.0.0.0` – every interface – and runs without TLS. The assumption that the only client is the local operator does not hold once the port is reachable from other hosts, and the convenience becomes an unauthenticated bypass. This is why it is classed as improper authentication (CWE-287) via an authentication-bypass primary weakness (CWE-305), not a credential-strength problem: no credential is involved at all.

[§ 04](https://offseq.com#s-04)

## § 04. The HCI wire format

The finding was confirmed by speaking the HCI protocol directly. Each message is a 16-byte big-endian header followed by a protobuf body:

| Field | Type | Value | 
|---|---|---|
| signature | uint16 | `0x4850` | 
| version | uint16 | `1` | 
| instanceId | int32 | – | 
| messageType | int32 | message type | 
| bodyLength | int32 | protobuf body length | 

The relevant message types are `LoginRequest` (22), `LoginResponse` (23), `AuthorizeHciRequest` (20) and `Error` (0). A `LoginRequest` carries `clientId` (field 1), `userLogin` (field 2) and `userPassword` (field 3). Protobuf does not serialise absent fields, so a request that simply omits `userLogin` and `userPassword` reaches the handler with those fields empty – and, against a single-user database, is answered with a `LoginResponse` rather than an `Error`.

All testing was carried out in a controlled environment against systems OffSeq controls; no third-party systems were touched.

[§ 05](https://offseq.com#s-05)

## § 05. Impact and severity

The published metrics are CVSS 3.1 base **9.8 (Critical)** (`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`) and CVSS 4.0 base **9.3 (Critical)** (`CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`). The vector is network-reachable, low-complexity, with no privileges and no user interaction: the default one-operator install is the vulnerable state, the default bind is `0.0.0.0` without TLS, and no credential is needed. A successful login grants full privileged control of the session – reading state, issuing commands, and uploading or modifying flight routes – each of confidentiality, integrity and availability rated High.

[§ 06](https://offseq.com#s-06)

## § 06. Remediation

SPH Engineering fixed the issue in **UgCS 6.2**: empty credentials are no longer accepted as a valid login. Operators should upgrade to UgCS 6.2 or later.

For deployments that cannot upgrade immediately, reduce exposure in depth: bind the HCI listener to `127.0.0.1` rather than every interface, restrict TCP port 3334 with host and network firewall rules so only the hosts that need it can reach the service, and place it behind an authenticated TLS transport.

[§ 07](https://offseq.com#s-07)

## § 07. Disclosure and outcome

The vulnerability was reported to CERT.LV through Latvia's [national coordinated-vulnerability-disclosure platform](https://cvd.cert.lv/) on 30 June 2026, triaged and forwarded to the vendor on 6 July. It was confirmed and CVE-2026-59104 reserved on 6 August 2026. The vendor reported the fix complete on 8 October and released it in UgCS 6.2 on 9 October 2026. The disclosure is coordinated by CERT.LV.

The discovery is credited to Nils Putniņš (OffSeq Cybersecurity).

[§ 08](https://offseq.com#s-08)

## § 08. Disclosure timeline

1. 2026-06-30OffSeq reports the authentication bypass to CERT.LV through the national coordinated-disclosure platform
2. 2026-07-06CERT.LV triages the report and forwards it to the vendor
3. 2026-08-06The vulnerability is confirmed and CVE-2026-59104 reserved
4. 2026-10-08The vendor reports the fix complete, pending release
5. 2026-10-09Fix released in UgCS 6.2

## References

- [CVE-2026-59104 – CVE Record (opens in a new tab) (https://www.cve.org/CVERecord?id=CVE-2026-59104)](https://www.cve.org/CVERecord?id=CVE-2026-59104)
- [CVSS 3.1 calculator – this vector (9.8, Critical) (opens in a new tab) (https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
- [CVSS 4.0 calculator – this vector (9.3, Critical) (opens in a new tab) (https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)](https://www.first.org/cvss/calculator/4.0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
- [UgCS – SPH Engineering (vendor) (opens in a new tab) (https://www.ugcs.com/)](https://www.ugcs.com/)
- [CERT.LV – national CERT (opens in a new tab) (https://cert.lv/en/)](https://cert.lv/en/)
- [CWE-287: Improper Authentication (opens in a new tab) (https://cwe.mitre.org/data/definitions/287.html)](https://cwe.mitre.org/data/definitions/287.html)
- [CWE-305: Authentication Bypass by Primary Weakness (opens in a new tab) (https://cwe.mitre.org/data/definitions/305.html)](https://cwe.mitre.org/data/definitions/305.html)

## Credit

Discovered and reported by Nils Putniņš (OffSeq Cybersecurity); coordinated through CERT.LV and fixed by SPH Engineering in UgCS 6.2.

## More results

[All results](https://offseq.com/en/case-studies/)

[Universal SQL Server sysadmin credential in the Jumis accounting softwareCVE-2026-59105 is a universal administrative credential OffSeq found in Jumis (formerly Tildes Jumis), a widely used Latvian accounting application. Jumis creates a Microsoft SQL Server login, ##Tilde\_JumisAdmin##, that holds the sysadmin server role, and derives its password deterministically from the SQL Server name combined with constants hard-coded into the client. The derivation is identical on every installation and the only variable input is not secret, so anyone able to reach a Jumis SQL Server can compute the password and gain full control of every customer accounting database on it. Jumis Pro SIA fixed it from release TJ7.0.141.36.Vulnerability disclosure20267 min read](https://offseq.com/en/research/jumis-cve-2026-59105/)

[Cross-user report access in CERT.LV’s GraphoscopeOffSeq found a horizontal authorisation bypass in Graphoscope, the open-source platform CERT.LV publishes for querying many independent data sources from one interface and showing their relations as a graph. The report download endpoint checked that a user was signed in but not that the requested report was theirs, so any analyst could read another analyst's uploaded indicators and query results. OffSeq reported the issue to CERT.LV and contributed the fix, which CERT.LV merged.Vulnerability disclosure20262 min read](https://offseq.com/en/research/graphoscope-download-idor/)

[Server crash in CERT.LV’s Graphoscope when a user disconnects during an uploadOffSeq found a denial-of-service flaw in Graphoscope, the open-source platform CERT.LV publishes for querying many independent data sources from one interface and showing their relations as a graph. A user who uploaded an indicator list and closed the connection before processing finished made the server dereference a nil WebSocket and crash, signing out every user. Any self-registered account could trigger it reliably. OffSeq reported the issue to CERT.LV and contributed the fix, which CERT.LV merged.Vulnerability disclosure20263 min read](https://offseq.com/en/research/graphoscope-websocket-dos/)
