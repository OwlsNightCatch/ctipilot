---
schema: 1
kind: vulnerability
title: "WatchGuard Fireware OS: two pre-auth RCEs in the iked IKE/VPN daemon plus a pre-auth stack overflow in the deprecated Mobile Security epm service"
headline: "WatchGuard tells Firebox admins to update now: two unauthenticated code-execution paths sit in the IKE/VPN daemon itself"
summary: >
  WatchGuard's 27 August 2026 "Immediate Action Required" advisory fixes eleven CVEs in Fireware OS,
  led by CVE-2026-19313 (pre-auth heap overflow) and CVE-2026-19315 (pre-auth type confusion), both
  unauthenticated remote code execution in the iked IKE/VPN daemon, plus CVE-2026-13086, a pre-auth
  stack overflow in the deprecated Mobile Security epm service with no stack canary and a non-PIE
  binary. WatchGuard reports no observed exploitation; fixed in Fireware OS 2026.2.2 / 12.12.2 / 12.5.20.
discovered_at: "2026-08-31T04:40:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [public-sector]
entities: []
techniques: [T1190]
affected_products: ["WatchGuard Firebox", "WatchGuard Fireware OS"]
cves:
  - id: CVE-2026-19313
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2 (default); T15/T35: >= 12.0, < 12.5.20"
    fixed: "2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-19315
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2 (default); T15/T35: >= 12.0, < 12.5.20"
    fixed: "2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-13086
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2 (default); T15/T35: >= 12.0, < 12.5.20"
    fixed: "2026.2.2 / 12.12.2 / 12.5.20"
sources:
  - url: "https://www.watchguard.com/wgrd-blog/immediate-action-required-update-your-firebox-now"
    publisher: "WatchGuard Technologies"
    date: "2026-08-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-19313/"
    publisher: "WatchGuard PSIRT"
    date: "2026-08-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-19315/"
    publisher: "WatchGuard PSIRT"
    date: "2026-08-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-13086/"
    publisher: "WatchGuard PSIRT"
    date: "2026-08-27"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068"
    publisher: "BSI CERT-Bund"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A remote, unauthenticated attacker can send a specially crafted IKE_AUTH message containing two EAP payloads to crash the IKE daemon (iked), causing a denial-of-service condition through process termination and respawn. Because the flaw results in an out-of-bounds read followed by a free() call on an attacker-influenced pointer value, it may also present potential for further memory corruption and remote code execution beyond denial of service."
    publisher: "WatchGuard PSIRT (CVE-2026-19315)"
  - quote: "A network-adjacent attacker with access to a trusted interface can send a specially crafted JSON-RPC request to the epm service to overflow a stack buffer, overwrite the saved return address, and execute arbitrary code with root privileges without authentication. The lack of a stack canary and use of a non-PIE binary make exploitation via return-oriented programming straightforward"
    publisher: "WatchGuard PSIRT (CVE-2026-13086)"
verification: single-source
sourcing_note: "WatchGuard PSIRT as the primary disclosing party for its own product (Admiralty vendor-PSIRT carve-out); BSI CERT-Bund's WID-SEC-2026-3068 restates the same vendor advisory rather than independently corroborating it, so credibility stays at 2 rather than 1."
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
  - "Patch every WatchGuard Firebox to Fireware OS >= 2026.2.2 / 12.12.2 / 12.5.20 (T15/T35: >= 12.5.20) now; where immediate patching is not possible, restrict IKE/VPN exposure to trusted interfaces and disable the deprecated Mobile Security feature to remove the epm attack surface entirely."
updates: []
migrated_from: null
---

WatchGuard's 27 August 2026 "Immediate Action Required" advisory ships fixes for eleven CVEs in Fireware OS, reserved under coordinated disclosure and detailed on WatchGuard's PSIRT pages. Two are pre-authentication remote code execution in the iked process, the daemon that handles IKE/IPsec VPN negotiation, each rated CVSS 4.0 9.3 Critical by WatchGuard: CVE-2026-19313 is a heap buffer overflow triggered by specially crafted network traffic reaching iked, and CVE-2026-19315 is a type confusion reached by sending an IKE_AUTH message containing two EAP payloads, causing an out-of-bounds read followed by a free() call on an attacker-influenced pointer — a crash-and-respawn denial of service at minimum, with WatchGuard itself stating the memory-corruption pattern carries potential for code execution beyond that ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)). Both flaws need no authentication and no configuration beyond a running iked process, which handles VPN and Mobile IKEv2 negotiation and is commonly reachable from the internet on a Firebox configured as a VPN gateway.

The third flaw, CVE-2026-13086 (also CVSS 4.0 9.3 Critical), sits in the epm service used by Fireware's deprecated Mobile Security feature: a network-adjacent, unauthenticated attacker can send a crafted JSON-RPC request that overflows a stack buffer and overwrites the saved return address, reaching arbitrary code execution as root ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)). WatchGuard's own advisory notes the binary ships with no stack canary and is not position-independent, which its own text states makes return-oriented-programming exploitation straightforward; even a failed attempt can crash and respawn the process. Reachability for this one is narrower than the iked pair — it requires network adjacency to a trusted interface where the deprecated Mobile Security feature is still enabled, rather than a bare internet-facing IKE listener.

All three, along with the remaining eight CVEs WatchGuard's own bulletin lists, are fixed in Fireware OS 2026.2.2, 12.12.2 and 12.5.20 (T15/T35 models: 12.5.20) ([WatchGuard, 2026-08-27](https://www.watchguard.com/wgrd-blog/immediate-action-required-update-your-firebox-now)). WatchGuard states it has not seen any indication that these vulnerabilities have been exploited. Germany's BSI CERT-Bund relayed the same advisory as WID-SEC-2026-3068 the same day, listing a twelfth CVE for the same iked heap-overflow class not present in WatchGuard's own blog roundup — CVE-2026-81851, "Fireware OS Heap-Based Buffer Overflow in iked Allows Denial of Service" ([BSI CERT-Bund, 2026-08-27](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068)).

**Defender takeaway:** treat any Firebox with an internet-facing VPN configuration as needing this patch on an emergency timeline, not the next maintenance window — the iked pair requires no authentication and no non-default configuration. Detection concepts: unexpected crashes or automatic respawns of the iked process are the observable symptom of a failed or exploratory attempt against either heap-overflow or type-confusion path; a working exploit against a memory-safety bug in a compiled daemon leaves little application-layer telemetry beyond the crash-restart cycle itself, which is why patching ahead of exploitation, not detection, is the primary control here. For the epm flaw, first confirm whether the deprecated Mobile Security feature is enabled at all — disabling it removes the exposure independent of patching.
