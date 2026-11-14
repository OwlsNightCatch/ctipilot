---
schema: 1
kind: vulnerability
title: "WatchGuard Fireware OS: three pre-auth RCEs in the iked IKE/VPN daemon plus a pre-auth stack overflow in the deprecated Mobile Security epm service"
headline: "WatchGuard tells Firebox admins to update now: three unauthenticated code-execution paths sit in the IKE/VPN daemon itself"
summary: >
  WatchGuard's 27 August 2026 "Immediate Action Required" advisory fixes eleven CVEs in Fireware OS,
  led by CVE-2026-19313 (pre-auth heap overflow) and CVE-2026-19315 (pre-auth type confusion), both
  unauthenticated remote code execution in the iked IKE/VPN daemon, plus CVE-2026-13086, a pre-auth
  stack overflow in the epm service of the deprecated Mobile Security feature. A third iked flaw and
  a Dimension management-platform session-hijack bug surfaced in a follow-up NCSC-CH advisory on the
  same bulletin. WatchGuard reports no observed exploitation for any of the five; fixed in Fireware
  OS 2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20 and Dimension 2.3.1.
discovered_at: "2026-08-31T04:40:00Z"
updated_at: "2026-09-29T21:55:58Z"
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
  - quote: "A type confusion vulnerability in the iked process of WatchGuard Fireware OS allows a remote unauthenticated attacker to execute arbitrary code by sending specially crafted network traffic."
    publisher: "WatchGuard PSIRT (CVE-2026-19315)"
    source_url: "https://psirt.watchguard.com/CVE-2026-19315/"
  - quote: "A stack-based buffer overflow in the epm (Endpoint Protection Manager) service used by the deprecated Mobile Security feature in WatchGuard Fireware OS allows an unauthenticated remote attacker to execute arbitrary code."
    publisher: "WatchGuard PSIRT (CVE-2026-13086)"
    source_url: "https://psirt.watchguard.com/CVE-2026-13086/"
  - quote: "A stack-based buffer overflow vulnerability in the WatchGuard Fireware OS iked process allows a remote unauthenticated attacker to execute arbitrary code by sending specially crafted network traffic."
    publisher: "WatchGuard PSIRT (CVE-2026-19318)"
    source_url: "https://psirt.watchguard.com/CVE-2026-19318/"
  - quote: "WatchGuard Dimension records unredacted session identifiers for logged-in users in its web UI diagnostic log. A low-privileged Dimension Administrator can retrieve this log and extract a Super Administrator's session token while that administrator is logged in, enabling account takeover."
    publisher: "WatchGuard PSIRT (CVE-2026-78174)"
    source_url: "https://psirt.watchguard.com/CVE-2026-78174/"
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
  - "Patch every WatchGuard Firebox to Fireware OS >= 2026.2.2 / 12.12.2 / 12.5.20 (T15/T35: >= 12.5.20) now, and separately to >= 2026.3.1 on any appliance already running a 2026.3.x build: WatchGuard places a 2026.3 affected band on each of the four iked and epm flaws (on the Default product row for two of them and the T15/T35 row for the other two), and the 2026.2.2 fix does not cover it. Where immediate patching is not possible, restrict IKE/VPN exposure to trusted interfaces and, as an inference from the service's role rather than a documented WatchGuard mitigation, disable the deprecated Mobile Security feature to take the epm service out of reach."
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
  - at: "2026-09-29T21:55:58Z"
    run_id: 2026-09-29T2134Z-audit
    type: update
    summary: >
      WatchGuard has revised its advisories. CVE-2026-19318 and CVE-2026-13086 are now rated
      exploitable by a remote unauthenticated attacker with no attack requirements, without the
      preconditions reported earlier (IKE payload diagnostic logging, network adjacency), so disabling
      diagnostic logging is no longer a documented mitigation, and the title and headline now count
      three iked code-execution flaws. The CVE-2026-19315 and CVE-2026-19318 pages no longer carry
      their earlier trigger detail or the crash-and-respawn outcome. Fixed releases unchanged. The
      crash-and-respawn detection concept is now marked as an inference from the bug class, and so is
      disabling Mobile Security for the epm flaw. The exploitation statement cites WatchGuard's
      bulletin.
    fields: [summary, evidence, actions, title, headline, body]
migrated_from: null
---

WatchGuard's 27 August 2026 "Immediate Action Required" advisory ships fixes for eleven CVEs in Fireware OS, reserved under coordinated disclosure and detailed on WatchGuard's PSIRT pages. Two are pre-authentication remote code execution in the iked process, the daemon that handles IKE/IPsec VPN negotiation, each rated CVSS 4.0 9.3 Critical by WatchGuard: CVE-2026-19313 is a heap buffer overflow triggered by specially crafted network traffic reaching iked ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19313/)), and CVE-2026-19315 is a type confusion, with an out-of-bounds read and the release of an invalid pointer among its listed weaknesses, that lets a remote unauthenticated attacker execute arbitrary code with crafted network traffic ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)). Both flaws need no authentication and no configuration beyond a running iked process, which handles VPN and Mobile IKEv2 negotiation and is commonly reachable from the internet on a Firebox configured as a VPN gateway.

The third flaw, CVE-2026-13086 (also CVSS 4.0 9.3 Critical), is a stack-based buffer overflow in the epm (Endpoint Protection Manager) service used by Fireware's deprecated Mobile Security feature that lets an unauthenticated remote attacker execute arbitrary code, and WatchGuard's weakness list for it also includes the use of hard-coded credentials ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)). WatchGuard rates it network-reachable with no privileges, user interaction or attack requirements (CVSS 4.0 `AV:N/AC:L/AT:N/PR:N/UI:N`), the same rating as the iked flaws ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)), so an appliance with Mobile Security still enabled is exposed on those terms.

All three, along with the remaining eight CVEs WatchGuard's own bulletin lists, are fixed in Fireware OS 2026.3.1, 2026.2.2, 12.12.2 and 12.5.20 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19313/)). The 2026.3 branch is a separate affected band from the 2025.0-2026.2.2 one and takes its own fix: on CVE-2026-19315 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)) and CVE-2026-13086 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)) the band `>= 2026.3, < 2026.3.1` sits on the Default product row, and on CVE-2026-19313 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19313/)) and CVE-2026-19318 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) it sits on the T15/T35 row. WatchGuard states it has not seen any indication that these vulnerabilities have been exploited ([WatchGuard, 2026-08-27](https://www.watchguard.com/wgrd-blog/immediate-action-required-update-your-firebox-now)). Germany's BSI CERT-Bund relayed the same advisory as WID-SEC-2026-3068 the same day, listing a twelfth CVE for the same iked heap-overflow class not present in WatchGuard's own blog roundup — CVE-2026-81851, "Fireware OS Heap-Based Buffer Overflow in iked Allows Denial of Service" ([BSI CERT-Bund, 2026-08-27](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-3068)).

**Defender takeaway:** treat any Firebox with an internet-facing VPN configuration as needing this patch on an emergency timeline, not the next maintenance window — the iked flaws require no authentication and no non-default configuration. Detection concepts: by inference from the bug class rather than from the advisories, unexpected crashes or automatic respawns of the iked process are the likely symptom of a failed or exploratory attempt against either heap-overflow or type-confusion path; a working exploit against a memory-safety bug in a compiled daemon leaves little application-layer telemetry beyond the crash-restart cycle itself, which is why patching ahead of exploitation, not detection, is the primary control here. For the epm flaw, first confirm whether the deprecated Mobile Security feature is enabled at all. WatchGuard documents no mitigation for it, but since epm is the service that feature uses, disabling the feature should take it out of reach until the patch is in, an inference rather than vendor guidance.

## Update — 2026-09-02T04:45:00Z

NCSC Switzerland's advisory on the same 27 August bulletin, created 2026-09-01, adds two CVEs this entry had not covered. CVE-2026-19318 (CVSS 9.3) is a third pre-authentication stack buffer overflow in iked that lets a remote unauthenticated attacker execute arbitrary code with crafted network traffic ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)).

CVE-2026-78174 (CVSS 9.3) is a different bug class on a different product: WatchGuard Dimension, the centralized reporting and management platform. Dimension's web UI diagnostic log records session identifiers for logged-in users unredacted; a low-privileged Dimension Administrator who retrieves that log can extract a Super Administrator's session token while the Super Administrator is logged in, then impersonate them fully — reaching Access Management, creating, deleting or altering any user or group, changing system-wide configuration, locking out legitimate administrators, and holding persistent full administrative control ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-78174/)). Both flaws share the same fix cadence as the original three: Fireware OS 2026.3.1 / 2026.2.2 / 12.12.2 / 12.5.20 for CVE-2026-19318, Dimension 2.3.1 for CVE-2026-78174. WatchGuard reports no observed exploitation for either.

**Defender takeaway (updated):** CVE-2026-19318 applies to every affected appliance running iked, on the same terms as the other two iked flaws. For Dimension, treat diagnostic-log export or viewing as a privileged, logged action and audit which accounts have exercised it; patch to 2.3.1 regardless, since a compromised low-privileged Dimension Administrator account is now a path to full Super Administrator control.

## Correction — 2026-09-06T13:40:00Z

The version ranges recorded for four of the five CVEs were incomplete. WatchGuard's PSIRT page for each lists a second affected band alongside the 2025.0-2026.2.2 and 12.0-12.12.2 ones, `>= 2026.3, < 2026.3.1`, and names Fireware OS 2026.3.1 in its Solution section alongside 2026.2.2, 12.12.2 and 12.5.20. The band's placement differs by CVE: on CVE-2026-19315 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)) and CVE-2026-13086 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)) it sits on the Default product row, and on CVE-2026-19313 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19313/)) and CVE-2026-19318 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) on the T15/T35 row.

What this changes for a defender: an appliance running any 2026.3.0 build is in scope for all four flaws, including the two unauthenticated iked code-execution paths, and upgrading it to 2026.2.2 does not remediate them; 2026.3.1 is its fix. CVE-2026-78174 on Dimension is unaffected by this correction, its `>= 2.0, < 2.3.1` range matching WatchGuard's page exactly.

## Update — 2026-09-29T21:55:58Z

WatchGuard has revised its per-CVE advisories. The current pages rate both flaws exploitable by a remote unauthenticated attacker with no privileges, user interaction or attack requirements, CVSS 4.0 `AV:N/AC:L/AT:N/PR:N/UI:N` for CVE-2026-19318 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) and for CVE-2026-13086 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)). They no longer state the preconditions their earlier text carried: IKE payload diagnostic logging for CVE-2026-19318 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)), and network adjacency to a trusted interface for CVE-2026-13086 ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)). Disabling IKE payload diagnostic logging is therefore not a documented mitigation for CVE-2026-19318, and an appliance with the deprecated Mobile Security feature enabled is exposed through epm on the same terms as the iked flaws. The fixed releases (Fireware OS 2026.3.1, 2026.2.2, 12.12.2, 12.5.20) are unchanged, and both advisories still state that WatchGuard is not aware of any exploitation in the wild ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)) ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-13086/)).

The pages for CVE-2026-19315 and CVE-2026-19318 also no longer carry the trigger detail their earlier text gave, an IKE_AUTH message with two EAP payloads for CVE-2026-19315 and an EAP-MSCHAPv2 payload with an undersized length field for CVE-2026-19318, or the crash-and-respawn outcome. Both now state remote code execution directly ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19315/)) ([WatchGuard PSIRT, 2026-08-27](https://psirt.watchguard.com/CVE-2026-19318/)). The analysis above no longer offers those details as hunting cues, and it gives iked crashes and respawns only as an inference from the bug class. With CVE-2026-19318 unconditional, three of the iked flaws are unauthenticated code-execution paths.
