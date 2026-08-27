---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Edge and VPN appliances took three pre-auth RCE/overread disclosures in one week — Citrix NetScaler, WatchGuard Firebox, Kemp LoadMaster"
headline: "Edge/VPN appliances: three pre-auth flaws in one week — Citrix NetScaler, WatchGuard Firebox, Kemp LoadMaster"
summary: "Three internet-facing edge appliances disclosed pre-authentication memory-safety flaws across the week: Citrix NetScaler CVE-2026-8451 (CitrixBleed-lineage SAML overread, public susceptibility tool), WatchGuard Firebox CVE-2026-13368 (IKEv2 use-after-free RCE, CVSS 9.2), and Progress Kemp LoadMaster CVE-2026-8037 (uninitialized-heap pre-auth RCE, CVSS 9.8) — the last already seeing exploitation attempts the day its PoC dropped. The pattern, not any single CVE, is the signal: pre-auth edge RCE reliably attracts fast-follow mass exploitation."
discovered_at: "2026-07-05T23:26:00Z"
event_date: 2026-06-30
run_id: 2026-07-05T2305Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - rce
  - actively-exploited
  - poc-public
  - patch-available
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - technology
entities: []
cves: []
sources:
  - url: "https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/"
    publisher: watchTowr Labs
    role: primary
  - url: "https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2026-00023"
    publisher: WatchGuard PSIRT (WGSA-2026-00023)
    role: primary
  - url: "https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/"
    publisher: watchTowr Labs
    role: primary
closed_sources: []
evidence:
  - quote: "A remote unauthenticated attacker could exploit this vulnerability to execute arbitrary code in the context of the iked process on Fireboxes that have a Mobile VPN with IKEv2 configured to use an external LDAP authentication server."
    publisher: WatchGuard PSIRT (WGSA-2026-00023)
verification: multi-source
sourcing_note: "Kemp exploitation-attempt confirmation is eSentire TRU (single research source); the Citrix and WatchGuard strands carry vendor PSIRT + national-CERT corroboration."
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - "2026-07-01/cve-2026-8451-citrix-netscaler-adc-gateway-pre-auth-saml-mem"
  - "2026-07-03/cve-2026-13368-watchguard-fireware-iked-pre-auth-rce"
  - "2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin"
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Inventory internet-facing NetScaler ADC/Gateway and patch to 14.1-72.61 / 13.1-63.18 per CTX696604; disable the SAML IdP role where not required (CVE-2026-8451)."
  - "Patch WatchGuard Fireboxes to Fireware OS 2026.2.1 / 12.12.1; on the still-unfixed 12.5.x branch and EOL 11.x, move Mobile VPN with IKEv2 off external-LDAP auth (e.g. to RADIUS) until a build ships (CVE-2026-13368)."
  - "Patch Kemp LoadMaster to v7.2.63.2 and restrict the management interface to an admin VLAN — exploitation attempts began the day the PoC dropped (CVE-2026-8037)."
---

The through-line across three otherwise unrelated vendors this week is that the network edge kept producing the exact bug class — pre-authentication memory corruption / overread in an internet-reachable appliance — that the Fortinet/Ivanti/Citrix history shows reliably becomes a mass-exploitation target once detail surfaces.

**Kemp LoadMaster — CVE-2026-8037** (CVSS 9.8): watchTowr published full mechanics of an uninitialized-`malloc()` heap corruption in the `escape_quotes()` path of the `access` executable, reached by a sprayed JSON payload to `/accessv2`, yielding code execution as root with no authentication ([watchTowr, 2026-06-29](https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/)). eSentire's TRU reported in-the-wild exploitation attempts beginning **the same day the PoC dropped** (observed attempts failed) — the fastest disclosure-to-attempt turn of the three (first covered 06-30, exploitation confirmed 07-02; § references).

**Citrix NetScaler ADC/Gateway — CVE-2026-8451** (CVSS 8.8): a pre-auth out-of-bounds read in the hand-rolled XML attribute parser behind `/saml/login`, reachable only when the appliance is a SAML IdP, leaking adjacent process memory in the `NSC_TASS` response cookie — the fourth CitrixBleed-class memory-safety defect watchTowr has documented in NetScaler auth paths. watchTowr shipped a public "Detection Artefact Generator" so operators can test exposure; no in-the-wild exploitation was confirmed at disclosure, but CitrixBleed-lineage siblings have been exploited within days ([watchTowr, 2026-06-30](https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/); NCSC-NL advisory NCSC-2026-0216).

**WatchGuard Firebox — CVE-2026-13368** (CVSS 9.2): a use-after-free race in the `iked` IKEv2 daemon reachable during LDAP authentication for Mobile VPN with IKEv2; a remote unauthenticated attacker winning the race executes code in the `iked` context ([WatchGuard PSIRT, 2026-07-02](https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2026-00023); BSI CERT-Bund WID-SEC-2026-2193). The 12.5.x branch had no fix at publication and 11.x is EOL.

**Weekly takeaway for defenders:** the recurring exposure is not a product, it is the *class* — internet-terminated VPN/UTM/load-balancer appliances with pre-auth memory-corruption primitives. Where a fix does not yet exist for your build (Firebox 12.5.x), the correct move is to remove the vulnerable auth path, not wait; and detection for all three realistically lives in appliance crash telemetry and the backing auth server's logs, because the exploit fires before any session is established. Per-appliance detail in § references.
