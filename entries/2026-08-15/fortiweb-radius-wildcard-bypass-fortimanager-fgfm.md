---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-26035 — FortiWeb: one non-default RADIUS admin setting turns any username and password into a valid GUI/CLI login, alongside an FGFM impersonation bug and a FortiClient flaw reachable by anyone who can answer a laptop's DNS"
headline: "Fortinet patches a FortiWeb admin-login bypass gated on a 'Wildcard' option, an FGFM impersonation flaw, and a FortiClient RCE reached via crafted DNS"
summary: >
  Fortinet patched eight vulnerabilities across its products on 2026-08-12. CVE-2026-26035 (CVSS 8.8) lets a
  remote unauthenticated attacker log into the FortiWeb GUI or CLI with a random username and password when
  Remote RADIUS Type Admin authentication has the non-default Wildcard option enabled; CVE-2026-70468 (7.3)
  lets an attacker with a valid certificate impersonate any FortiGate managed by a FortiManager with a specific
  CLI option set; and CVE-2026-70465 (7.3) lets anyone able to craft DNS responses to a Windows endpoint run
  code through FortiClient. Each has a vendor workaround that is a configuration change rather than an upgrade.
  No exploitation is reported.
discovered_at: "2026-08-15T04:56:00Z"
event_date: "2026-08-12"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - rce
  - pre-auth
  - patch-available
  - no-patch
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - telco
  - healthcare
  - energy
entities: []
techniques: [T1190, T1078, T1557]
affected_products:
  - Fortinet FortiWeb
  - Fortinet FortiManager
  - Fortinet FortiManager Cloud
  - Fortinet FortiClient
cves:
  - id: CVE-2026-26035
    cvss: "8.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiWeb 8.0.0–8.0.2, 7.6.0–7.6.6, 7.4.0–7.4.11, 7.2.0–7.2.12, 7.0.0–7.0.12"
    fixed: "8.0.3, 7.6.7, 7.4.12 — 7.2.13 and 7.0.13 are listed as upcoming, so the 7.2 and 7.0 branches have no released fix"
  - id: CVE-2026-70468
    cvss: "7.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiManager 7.6.1, 7.4.3–7.4.5, 7.2.5–7.2.9 and FortiManager Cloud equivalents"
    fixed: "7.6.2, 7.4.6, 7.2.10"
  - id: CVE-2026-70466
    cvss: "4.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
      - mitigation-only
    affected: "FortiWeb 8.0.0–8.0.2, 7.6.0–7.6.5; the 7.4, 7.2 and 7.0 branches at all versions"
    fixed: "8.0.3, 7.6.6 — the 7.4, 7.2 and 7.0 branches have no fixed build and must be migrated"
  - id: CVE-2026-70465
    cvss: "7.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiClient for Windows 7.4.0–7.4.3, 7.2.0–7.2.11"
    fixed: "7.4.4, 7.2.12"
sources:
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-158"
    publisher: "Fortinet PSIRT — FG-IR-26-158"
    date: "2026-08-12"
    role: primary
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-160"
    publisher: "Fortinet PSIRT — FG-IR-26-160"
    date: "2026-08-12"
    role: primary
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-157"
    publisher: "Fortinet PSIRT — FG-IR-26-157"
    date: "2026-08-12"
    role: primary
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-156"
    publisher: "Fortinet PSIRT — FG-IR-26-156"
    date: "2026-08-12"
    role: primary
  - url: "https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/"
    publisher: SecurityWeek
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An Improper Authentication vulnerability  [CWE-287] in the FortiWeb Remote Radius Type Admin Authentication configured with specific, non-default settings may allow a remote unauthenticated attacker to login into the Fortiweb GUI/CLI with a random username and password"
    publisher: "Fortinet PSIRT — FG-IR-26-158"
  - quote: "An Authentication Bypass Using an Alternate Path or Channel [CWE-288] vulnerability in FortiManager and FortiManager Cloud may allow a remote unauthenticated attacker to impersonate any FortiGate managed by the FortiManager with a specific CLI option set via crafted FGFM requests if the attacker has a valid certificate."
    publisher: "Fortinet PSIRT — FG-IR-26-160"
  - quote: "A buffer copy without checking size of input vulnerability [CWE-120] in FortiClient Windows may allow an unauthenticated attacker in a position to alter or craft DNS responses to the targeted host to execute arbitrary code via malicious packets."
    publisher: "Fortinet PSIRT — FG-IR-26-156"
verification: multi-source
sourcing_note: >
  Affected and fixed version strings, and every CVSS score, are read from Fortinet's own per-advisory version
  tables and CSAF records rather than from secondary summaries. The advisories' rendered tables omit the FortiWeb
  7.0 branch and present two builds as available that the structured records mark as upcoming, so the CSAF is
  what this entry follows on both points. Every score here is
  Fortinet's own published figure, which its CSAF records give with temporal metrics applied rather than as a
  bare base score; NVD lists the higher base score for the same Fortinet-supplied vector, so the two are the
  same assessment at different metric sets rather than a disagreement between authorities.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade FortiClient for Windows to 7.4.4 or 7.2.12 across the remote-working fleet, or disable application-based filtering in the EMS remote-access profile's VPN tunnel settings in the meantime — the flaw needs no credential, only an attacker positioned to answer the endpoint's DNS, which is the normal condition of a laptop on an untrusted network before the tunnel comes up."
  - "Check whether the Wildcard option is enabled on any FortiWeb Remote Type administrator account (System > Administrators) and disable it — this is Fortinet's own workaround for CVE-2026-26035 and it removes the exposure without waiting for a maintenance window, ahead of upgrading to 8.0.3, 7.6.7 or 7.4.12. On the 7.2 and 7.0 branches that configuration change is the whole remediation for now, because their fixed builds are listed as upcoming rather than released."
  - "Check whether fgfm-peercert-withoutsn is set on any FortiManager or FortiManager Cloud instance and disable it, then upgrade to 7.6.2 / 7.4.6 / 7.2.10 — with the option set, a valid certificate is enough to impersonate a managed FortiGate over FGFM."
migrated_from: null
---

Fortinet issued patches for eight vulnerabilities across its products on 2026-08-12 ([SecurityWeek, 2026-08-13](https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/)). Four of the flaws in that batch matter to a defender's next week. The most consequential is CVE-2026-26035 (CVSS 8.8, CWE-287): where FortiWeb's Remote RADIUS Type Admin authentication is configured with specific, non-default settings, a remote unauthenticated attacker can log into the FortiWeb GUI or CLI with a random username and password ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-158)). The setting in question is named in the advisory's own workaround: the Wildcard option on a Remote Type administrator account, reached in the GUI under System > Administrators. The affected branches, read from Fortinet's CSAF record rather than the advisory's rendered table, are FortiWeb 8.0.0 through 8.0.2, 7.6.0 through 7.6.6, 7.4.0 through 7.4.11, 7.2.0 through 7.2.12 and 7.0.0 through 7.0.12. Released fixes exist for three of those five: 8.0.3, 7.6.7 and 7.4.12. The 7.2 and 7.0 branches are answered only by builds the record marks as upcoming — 7.2.13 and 7.0.13 — so an estate on either has no patch to install today and the Wildcard configuration check is its whole remediation.

CVE-2026-70468 (CVSS 7.3, CWE-288) is the management-plane counterpart: a remote unauthenticated attacker holding a valid certificate can impersonate any FortiGate managed by a FortiManager that has a specific CLI option set, via crafted FGFM protocol requests ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-160)). The option is `fgfm-peercert-withoutsn`, and disabling it is the vendor's stated workaround. Affected are FortiManager 7.6.1, 7.4.3 through 7.4.5 and 7.2.5 through 7.2.9 plus the corresponding FortiManager Cloud versions, fixed in 7.6.2, 7.4.6 and 7.2.10; FortiManager 8.0 is listed as not affected. CVE-2026-70466 (CVSS 4.8, CWE-184) is an incomplete list of disallowed inputs in the FortiWeb WAF that lets an unauthenticated attacker bypass policies via specifically crafted requests ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-157)) — a lower score, but a WAF that can be walked past is a compensating control that has stopped compensating. Its version data is the one to read carefully: 8.0.0 through 8.0.2 are answered by 8.0.3 and 7.6.0 through 7.6.5 by 7.6.6, but the 7.4, 7.2 and 7.0 branches are all listed as affected at every version with no fixed build at all — migration is the only remediation, and Fortinet offers an interim virtual patch, FG-VD-10009598.0day, in FortiWeb signature database update FMWP 26.071 — the concrete lever for the three branches with no fixed build.

The fourth flaw in the batch is the one that reaches past the data centre. CVE-2026-70465 (CVSS 7.3, CWE-120) is a buffer copy without checking the size of input in FortiClient for Windows that "may allow an unauthenticated attacker in a position to alter or craft DNS responses to the targeted host to execute arbitrary code via malicious packets" ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-156)). The precondition is not a credential but a network position: anyone able to answer the endpoint's DNS queries — a hostile or compromised local network, a captive portal, an on-path attacker upstream of a home or hotel connection — can reach the code path. That is precisely the position a remote-working laptop puts itself in every time it joins an untrusted network before the VPN comes up, which makes this a teleworker-fleet problem rather than a server-patching one. FortiClient for Windows 7.4.0 through 7.4.3 upgrade to 7.4.4 and 7.2.0 through 7.2.11 upgrade to 7.2.12; the 8.0 branch is not affected. Fortinet's stated workaround is to disable application-based filtering in the FortiClient EMS remote-access profile's VPN tunnel settings. SecurityWeek notes Fortinet makes no mention of any of these vulnerabilities being exploited in the wild ([SecurityWeek, 2026-08-13](https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/)).

None of them is reported exploited: SecurityWeek records that Fortinet makes no mention of any of these vulnerabilities being exploited in the wild. What lifts them above the ordinary patch queue is that two of them are *configuration-gated*, which cuts both ways: an estate that never enabled the Wildcard option or `fgfm-peercert-withoutsn` is not exposed at all and needs only a routine upgrade, while one that did is exposed right now and can close the hole today with a settings change rather than a maintenance window. That makes the first task an inventory question, not a patching question — and it is answerable in minutes across a fleet. The certificate precondition on the FortiManager bug is worth reading precisely: it does not say a certificate issued to the impersonated FortiGate, and the advisory's own framing is an alternate-path authentication bypass, so a defender should treat any valid certificate the deployment would accept as sufficient rather than assuming device-specific binding.

Detection concepts, telemetry class first: in administrative authentication logs on FortiWeb, a successful GUI or CLI admin login for a username that does not exist in the backing RADIUS directory is the signature of this bypass being used — the login succeeds locally, so the discriminator is the mismatch between the accepted account and the identity store that was supposed to authorise it. In management-fabric telemetry on FortiManager, watch for FGFM session establishment from a source presenting a certificate whose subject does not correspond to the device serial the session claims, and for a managed FortiGate appearing to check in from an unexpected address or twice from different sources. Fortinet edge and management products have a sustained recent history of rapid post-disclosure weaponisation — this pipeline recorded a Gunra ransomware campaign abusing older FortiOS authentication-bypass flaws for initial access four days ago — so the interval between a published advisory and a working exploit is the planning assumption here, not the absence of exploitation today.
