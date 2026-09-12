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
  binary. A third iked flaw and a Dimension management-platform session-hijack bug surfaced in a
  follow-up NCSC-CH advisory on the same bulletin. WatchGuard reports no observed exploitation for
  any of the five; fixed in Fireware OS 2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20 and Dimension 2.3.1.
discovered_at: "2026-08-31T04:40:00Z"
updated_at: "2026-09-02T04:45:00Z"
event_date: "2026-08-27"
run_id: 2026-08-31T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [public-sector]
entities: []
techniques: [T1190, "T1550.004"]
affected_products: ["WatchGuard Firebox", "WatchGuard Fireware OS", "WatchGuard Dimension"]
cves:
  - id: CVE-2026-19313
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2 (default); T15/T35: >= 12.0, < 12.5.20; >= 2026.3, < 2026.3.1"
    fixed: "2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-19315
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2; >= 2026.3, < 2026.3.1 (default); T15/T35: >= 12.0, < 12.5.20"
    fixed: "2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-13086
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2; >= 2026.3, < 2026.3.1 (default); T15/T35: >= 12.0, < 12.5.20"
    fixed: "2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-19318
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: ">= 2025.0, < 2026.2.2; >= 12.0, < 12.12.2 (default); T15/T35: >= 12.0, < 12.5.20; >= 2026.3, < 2026.3.1"
    fixed: "2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20"
  - id: CVE-2026-78174
    cvss: "9.3"
    epss: null
    type: priv-esc
    vector: zero-click
    auth: admin-required
    status: [patch-available]
    affected: ">= 2.0, < 2.3.1"
    fixed: "2.3.1"
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
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12901"
    publisher: "NCSC Switzerland (GovCERT.ch) Cyber Security Hub"
    date: "2026-09-01"
    role: corroborating
  - url: "https://psirt.watchguard.com/CVE-2026-19318/"
    publisher: "WatchGuard PSIRT"
    date: "2026-08-27"
    role: primary
  - url: "https://psirt.watchguard.com/CVE-2026-78174/"
    publisher: "WatchGuard PSIRT"
    date: "2026-08-27"
    role: primary
closed_sources: []
evidence:
  - quote: "A remote, unauthenticated attacker can send a specially crafted IKE_AUTH message containing two EAP payloads to crash the IKE daemon (iked), causing a denial-of-service condition through process termination and respawn. Because the flaw results in an out-of-bounds read followed by a free() call on an attacker-influenced pointer value, it may also present potential for further memory corruption and remote code execution beyond denial of service."
    publisher: "WatchGuard PSIRT (CVE-2026-19315)"
  - quote: "A network-adjacent attacker with access to a trusted interface can send a specially crafted JSON-RPC request to the epm service to overflow a stack buffer, overwrite the saved return address, and execute arbitrary code with root privileges without authentication. The lack of a stack canary and use of a non-PIE binary make exploitation via return-oriented programming straightforward"
    publisher: "WatchGuard PSIRT (CVE-2026-13086)"
  - quote: "An unauthenticated remote attacker who completes IKE_SA_INIT can send a specially crafted IKE_AUTH message containing an EAP-MSCHAPv2 payload with an undersized embedded length field, triggering a stack buffer overflow in the iked process. This causes a crash and denial-of-service condition (with automatic respawn), and given the attacker-influenced nature of the stack overwrite, may carry potential for remote code execution. Exploitation requires that IKE payload diagnostic logging, a supported operational troubleshooting setting, be enabled on the affected device."
    publisher: "WatchGuard PSIRT (CVE-2026-19318)"
  - quote: "WatchGuard Dimension records unredacted session identifiers for logged-in users in its web UI diagnostic log. A low-privileged Dimension Administrator can retrieve this log and extract a Super Administrator's session token while that administrator is logged in, enabling account takeover."
    publisher: "WatchGuard PSIRT (CVE-2026-78174)"
verification: single-source
sourcing_note: "WatchGuard PSIRT as the primary disclosing party for its own product (Admiralty vendor-PSIRT carve-out); BSI CERT-Bund's WID-SEC-2026-3068 and NCSC-CH's advisory both restate the same vendor bulletin rather than independently corroborating it, so credibility stays at 2 rather than 1."
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
  - "Patch every WatchGuard Firebox to Fireware OS >= 2026.2.2 / 12.12.2 / 12.5.20 (T15/T35: >= 12.5.20) now, and separately to >= 2026.3.1 on any appliance already running a 2026.3.x build: WatchGuard places a 2026.3 affected band on each of the four iked and epm flaws (on the Default product row for two of them and the T15/T35 row for the other two), and the 2026.2.2 fix does not cover it. Where immediate patching is not possible, restrict IKE/VPN exposure to trusted interfaces, disable the deprecated Mobile Security feature to remove the epm attack surface, and disable IKE payload diagnostic logging if enabled to close CVE-2026-19318."
  - "Patch every WatchGuard Dimension instance to >= 2.3.1 now, and audit which accounts have exported or viewed the web UI diagnostic log — a low-privileged Dimension Administrator account that has done so should be treated as a possible path to Super Administrator compromise."
updates:
  - at: "2026-09-02T04:45:00Z"
    run_id: 2026-09-02T0411Z-intel
    type: update
    summary: >
      NCSC-CH's advisory on the same 27 August bulletin adds two CVEs this entry had not covered:
      CVE-2026-19318, a third pre-auth stack overflow in the iked daemon that requires IKE payload
      diagnostic logging to be enabled, and CVE-2026-78174, a session-hijack flaw in the Dimension
      management platform where a low-privileged Dimension Administrator can extract a Super
      Administrator's session token from an unredacted diagnostic log. No exploitation reported for
      either.
    fields: [cves, affected_products, techniques, actions, summary, sources, evidence, sourcing_note]
  - at: "2026-09-06T13:40:00Z"
    run_id: 2026-09-06T1308Z-audit
    type: correction
    summary: >
      The recorded affected and fixed versions omitted a second affected band that WatchGuard's own
      PSIRT pages list for four of the five CVEs: Fireware OS 2026.3 up to but not including 2026.3.1,
      which takes its own fix in 2026.3.1. An appliance on a 2026.3.x build reading the previous
      version ranges would have concluded it was out of scope. Corrected for CVE-2026-19313,
      CVE-2026-19315, CVE-2026-13086 and CVE-2026-19318, with the band placed on the product row
      WatchGuard assigns it to in each case; CVE-2026-78174 (Dimension) was already correct. The fix-cadence sentence in the 2026-09-02 update section, which listed the same incomplete set for CVE-2026-19318, is corrected in place.
    fields: [cves, summary, actions, body]
migrated_from: null
---

WatchGuard's 27 August 2026 "Immediate Action Required" advisory ships fixes for eleven CVEs in Fireware OS, reserved under coordinated disclosure and detailed on WatchGuard's PSIRT pages. Two are pre-authentication remote code execution in the iked process, the daemon that handles IKE/IPsec VPN negotiation, each rated CVSS 4.0 9.3 Critical by WatchGuard: CVE-2026-19313 is a heap buffer overflow triggered by specially crafted network traffic reaching iked, and CVE-2026-19315 is a type confusion reached by sending an IKE_AUTH message containing two EAP payloads, causing an out-of-bounds read followed by a free() call on an attacker-influenced pointer — a crash-and-respawn denial of service at minimum, with WatchGuard itself stating the memory-corruption pattern carries potential for code execution beyond that ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)). Both flaws need no authentication and no configuration beyond a running iked process, which handles VPN and Mobile IKEv2 negotiation and is commonly reachable from the internet on a Firebox configured as a VPN gateway.

The third flaw, CVE-2026-13086 (also CVSS 4.0 9.3 Critical), sits in the epm service used by Fireware's deprecated Mobile Security feature: a network-adjacent, unauthenticated attacker can send a crafted JSON-RPC request that overflows a stack buffer and overwrites the saved return address, reaching arbitrary code execution as root ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)). WatchGuard's own advisory notes the binary ships with no stack canary and is not position-independent, which its own text states makes return-oriented-programming exploitation straightforward; even a failed attempt can crash and respawn the process. Reachability for this one is narrower than the iked pair — it requires network adjacency to a trusted interface where the deprecated Mobile Security feature is still enabled, rather than a bare internet-facing IKE listener.

All three, along with the remaining eight CVEs WatchGuard's own bulletin lists, are fixed in Fireware OS 2026.3.1, 2026.2.2, 12.12.2 and 12.5.20 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19313/)). The 2026.3 branch is a separate affected band from the 2025.0-2026.2.2 one and takes its own fix: on CVE-2026-19315 and CVE-2026-13086 the band `>= 2026.3, < 2026.3.1` sits on the Default product row, and on CVE-2026-19313 and CVE-2026-19318 it sits on the T15/T35 row ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)). WatchGuard states it has not seen any indication that these vulnerabilities have been exploited. Germany's BSI CERT-Bund relayed the same advisory as WID-SEC-2026-3068 the same day, listing a twelfth CVE for the same iked heap-overflow class not present in WatchGuard's own blog roundup — CVE-2026-81851, "Fireware OS Heap-Based Buffer Overflow in iked Allows Denial of Service" ([BSI CERT-Bund, 2026-08-27](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068)).

**Defender takeaway:** treat any Firebox with an internet-facing VPN configuration as needing this patch on an emergency timeline, not the next maintenance window — the iked pair requires no authentication and no non-default configuration. Detection concepts: unexpected crashes or automatic respawns of the iked process are the observable symptom of a failed or exploratory attempt against either heap-overflow or type-confusion path; a working exploit against a memory-safety bug in a compiled daemon leaves little application-layer telemetry beyond the crash-restart cycle itself, which is why patching ahead of exploitation, not detection, is the primary control here. For the epm flaw, first confirm whether the deprecated Mobile Security feature is enabled at all — disabling it removes the exposure independent of patching.

## Update — 2026-09-02T04:45:00Z

NCSC Switzerland's advisory on the same 27 August bulletin, created 2026-09-01, adds two CVEs this entry had not covered. CVE-2026-19318 (CVSS 9.3) is a third pre-authentication stack overflow in iked's IKE_AUTH handling: an attacker who completes IKE_SA_INIT can send an IKE_AUTH message carrying an EAP-MSCHAPv2 payload with an undersized embedded length field, triggering the overflow, which WatchGuard's own advisory describes as causing "a crash and denial-of-service condition (with automatic respawn)," with "potential for remote code execution" given the attacker-influenced stack overwrite ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) — the same hedged severity language WatchGuard uses for the two iked flaws already covered above. Unlike those two, exploitation here is conditional: it requires that IKE payload diagnostic logging, an operational troubleshooting setting not enabled by default, be turned on ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) — a Firebox with diagnostic logging off is not exposed to this specific flaw.

CVE-2026-78174 (CVSS 9.3) is a different bug class on a different product: WatchGuard Dimension, the centralized reporting and management platform. Dimension's web UI diagnostic log records session identifiers for logged-in users unredacted; a low-privileged Dimension Administrator who retrieves that log can extract a Super Administrator's session token while the Super Administrator is logged in, then impersonate them fully — reaching Access Management, creating, deleting or altering any user or group, changing system-wide configuration, locking out legitimate administrators, and holding persistent full administrative control ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-78174/)). Both flaws share the same fix cadence as the original three: Fireware OS 2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20 for CVE-2026-19318, Dimension 2.3.1 for CVE-2026-78174. WatchGuard reports no observed exploitation for either.

**Defender takeaway (updated):** the exposure decision for CVE-2026-19318 turns on whether IKE payload diagnostic logging is enabled — check that setting before assuming this flaw applies to a given appliance. For Dimension, treat diagnostic-log export or viewing as a privileged, logged action and audit which accounts have exercised it; patch to 2.3.1 regardless, since a compromised low-privileged Dimension Administrator account is now a path to full Super Administrator control.

## Correction — 2026-09-06T13:40:00Z

The version ranges recorded for four of the five CVEs were incomplete. WatchGuard's PSIRT page for each lists a second affected band alongside the 2025.0-2026.2.2 and 12.0-12.12.2 ones, `>= 2026.3, < 2026.3.1`, and names Fireware OS 2026.3.1 in its Solution section alongside 2026.2.2, 12.12.2 and 12.5.20. The band's placement differs by CVE: on CVE-2026-19315 and CVE-2026-13086 it sits on the Default product row ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)), and on CVE-2026-19313 and CVE-2026-19318 on the T15/T35 row ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)).

What this changes for a defender: an appliance running any 2026.3.0 build is in scope for all four flaws, including the two unauthenticated iked code-execution paths, and upgrading it to 2026.2.2 does not remediate them; 2026.3.1 is its fix. CVE-2026-78174 on Dimension is unaffected by this correction, its `>= 2.0, < 2.3.1` range matching WatchGuard's page exactly.
