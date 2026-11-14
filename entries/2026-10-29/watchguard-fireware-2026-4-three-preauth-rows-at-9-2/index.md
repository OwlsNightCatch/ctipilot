---
schema: 1
kind: vulnerability
title: "WatchGuard Fireware OS 2026.4, 12.12.4 and 12.5.22: seven of 17 fixed Fireware OS flaws are scored 9.0 or higher, among them unauthenticated memory-corruption and missing-authentication rows in the Access Portal, the SIP proxy and the FireCluster sync daemon; WatchGuard knows of no exploitation"
headline: "WatchGuard fixes three feature-dependent unauthenticated flaws scored 9.2 in Fireware OS; no exploitation known"
summary: >
  WatchGuard's advisories of 2026-10-27 fix 17 flaws in Fireware OS 2026.4, 12.12.4 and, for T15 and T35 models, 12.5.22, seven of them scored 9.0 or higher.
  Three need no authentication but a specific feature: a heap write in the Access Portal's WebSocket handling, a stack overflow in the SIP proxy and missing
  authentication in the FireCluster sync daemon, each scored 9.2. Four more need an attacker who controls or intercepts traffic to an Active Directory server,
  to WatchGuard Cloud or to a log server. WatchGuard is not aware of exploitation of any of them.
discovered_at: "2026-10-29T04:42:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-29T0255Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, patch-available]
regions: [global]
sectors: []
entities: ["product:watchguard-fireware-os"]
techniques: [T1190]
affected_products: ["WatchGuard Fireware OS"]
cves:
  - id: CVE-2026-93866
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, with the Access Portal enabled"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
  - id: CVE-2026-93857
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, with a SIP proxy configured"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
  - id: CVE-2026-93865
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, on Firebox appliances that are FireCluster members"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
  - id: CVE-2026-112710
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, with an Active Directory authentication server configured; needs an attacker who controls or intercepts traffic to that server"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
  - id: CVE-2026-112709
    cvss: "9.2 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, with an Active Directory authentication server configured; needs an attacker who controls or intercepts traffic to that server"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
  - id: CVE-2026-103594
    cvss: "9.5 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2026.2 up to before 2026.4 and 12.12 up to before 12.12.4, on a Firebox that acts as a FireCloud Gateway; needs a man-in-the-middle position with TLS-decrypted access between the Firebox and WatchGuard Cloud"
    fixed: "Fireware OS 2026.4 and 12.12.4"
  - id: CVE-2026-103593
    cvss: "9.1 (CVSS 4.0)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 12.0 up to before 12.5.22, in FIPS mode with an external log server; needs a network-adjacent attacker who can impersonate or intercept traffic to the log server"
    fixed: "Fireware OS 2026.4, 12.12.4 and 12.5.22 (T15 and T35)"
sources:
  - url: "https://psirt.watchguard.com/CVE-2026-93866/"
    publisher: "WatchGuard PSIRT (CVE-2026-93866)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-93857/"
    publisher: "WatchGuard PSIRT (CVE-2026-93857)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-93865/"
    publisher: "WatchGuard PSIRT (CVE-2026-93865)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-112710/"
    publisher: "WatchGuard PSIRT (CVE-2026-112710)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-112709/"
    publisher: "WatchGuard PSIRT (CVE-2026-112709)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-103594/"
    publisher: "WatchGuard PSIRT (CVE-2026-103594)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-103593/"
    publisher: "WatchGuard PSIRT (CVE-2026-103593)"
    date: "2026-10-27"
    role: primary
  - url: "https://psirt.watchguard.com/"
    publisher: "WatchGuard PSIRT (advisory listing)"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "WatchGuard is not aware of any exploitation of this vulnerability in the wild."
    publisher: "WatchGuard PSIRT (CVE-2026-93866)"
    source_url: "https://psirt.watchguard.com/CVE-2026-93866/"
  - quote: "allows a remote, unauthenticated attacker to write beyond the bounds of a heap buffer by sending a specially crafted request while the Access Portal feature is enabled."
    publisher: "WatchGuard PSIRT (CVE-2026-93866)"
    source_url: "https://psirt.watchguard.com/CVE-2026-93866/"
  - quote: "The exploit for this vulnerability requires a SIP proxy configured on the Firebox."
    publisher: "WatchGuard PSIRT (CVE-2026-93857)"
    source_url: "https://psirt.watchguard.com/CVE-2026-93857/"
  - quote: "allows a remote, unauthenticated attacker to invoke privileged system-level administrative actions by sending a specially crafted request to the FireCluster management IP when the clustering feature is enabled."
    publisher: "WatchGuard PSIRT (CVE-2026-93865)"
    source_url: "https://psirt.watchguard.com/CVE-2026-93865/"
verification: single-source
sourcing_note: >
  WatchGuard is the disclosing party for its own product and its per-flaw advisories are the source for every score, configuration condition and fixed release. The scores are CVSS 4.0 by the vector on each advisory page, and WatchGuard publishes no workaround. The count of 17 Fireware OS advisories is a tally of the advisory listing, which also carries one Mobile VPN with SSL Client row.
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
  - "Upgrade every WatchGuard Firebox to Fireware OS 2026.4, 12.12.4 or, on T15 and T35 models, 12.5.22, starting with appliances that have the Access Portal or a SIP proxy enabled or that are FireCluster members, because WatchGuard names no workaround for the three unauthenticated flaws."
updates: []
migrated_from: null
---

WatchGuard's advisory listing of 2026-10-27 opens with 18 rows, 17 for Fireware OS and one for Mobile VPN with SSL Client for Windows, and seven of the 17 are scored 9.0 or higher ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/)). The fixes are in Fireware OS 2026.4, 12.12.4 and, for T15 and T35 models, 12.5.22. Three of the seven need no authentication but a specific feature. CVE-2026-93866 (9.2) is an integer overflow in the WebSocket handling of the Access Portal that lets a remote unauthenticated attacker write beyond the bounds of a heap buffer while the Access Portal is enabled ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93866/)). CVE-2026-93857 (9.2) is a stack buffer overflow in the SIP proxy that gives remote code execution when a SIP proxy is configured on the Firebox ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93857/)). CVE-2026-93865 (9.2) is missing authentication in the FireCluster synchronization daemon: a remote unauthenticated attacker invokes privileged administrative actions with a crafted request to the FireCluster management IP when clustering is enabled ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93865/)).

The other four need a network position. CVE-2026-112709 and CVE-2026-112710 (9.2 each) are heap overflows in the authentication service that give denial of service and possibly code execution to an attacker who controls or intercepts traffic to the configured Active Directory server and returns a crafted response ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112710/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112709/)). CVE-2026-103594 (9.5) is a stack overflow in WireGuard configuration processing for a man-in-the-middle with TLS-decrypted access between a Firebox that acts as a FireCloud Gateway and WatchGuard Cloud ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103594/)). CVE-2026-103593 (9.1) is a stack overflow in the logging service that gives root code execution to a network-adjacent attacker who impersonates or intercepts traffic to the log server with a crafted certificate, in FIPS mode ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103593/)). Six rows affect Fireware OS 2025.1 up to before 2026.4 and 12.0 up to before 12.12.4, T15 and T35 up to before 12.5.22, the WireGuard row starts at 2026.2 and 12.12, and each page states that WatchGuard is not aware of exploitation in the wild ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93866/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93857/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93865/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112710/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112709/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103594/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103593/)).

**Exposure:** a Firebox on a Fireware OS release inside those ranges with at least one of the listed features: the Access Portal, a SIP proxy policy, FireCluster membership, an Active Directory authentication server, the FireCloud Gateway role, or FIPS mode with an external log server; the three unauthenticated rows are reachable by any host that can reach the Access Portal, the SIP proxy policy or the cluster management address ([WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93866/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93857/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-93865/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112710/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-112709/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103594/); [WatchGuard PSIRT, 2026-10-27](https://psirt.watchguard.com/CVE-2026-103593/)).

**Detection:** WatchGuard publishes no indicator and no workaround. For the three unauthenticated rows, connections to the cluster management address from hosts that are not cluster peers, WebSocket upgrade requests to the Access Portal from unexpected sources, SIP traffic from outside expected carriers, and restarts of the portal, SIP or sync services on the Firebox are the telemetry to review; this is an inference from the stated mechanisms.

**Defender takeaway:** install the fixed release on appliances with the Access Portal, a SIP proxy or clustering first; where an upgrade has to wait, turn off a feature that is not used and keep the cluster management address off untrusted segments.
