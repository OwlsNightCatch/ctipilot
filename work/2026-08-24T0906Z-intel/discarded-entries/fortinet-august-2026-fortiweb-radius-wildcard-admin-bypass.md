---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-26035 — FortiWeb: a RADIUS 'wildcard' admin setting makes any username the right username, letting an unauthenticated caller log into the GUI or CLI with random credentials"
headline: "Fortinet's August batch is led by an appliance that accepts whatever username the RADIUS server returns — and the advisory names the exact toggle to check"
summary: >
  Fortinet published eight advisories on 2026-08-12, three of which the Dutch national CERT carried the following day in two bulletins. The
  headline flaw, CVE-2026-26035 in FortiWeb, applies where an administrator account uses Remote RADIUS Type
  authentication with the non-default wildcard setting enabled: the appliance then matches any username the remote
  server returns against the configured admin group, so a remote unauthenticated attacker logs into the FortiWeb GUI or
  CLI with a random username and password. Fortinet scores it 8.8, records it as internally discovered and not known to
  be exploited, and fixes it in FortiWeb 8.0.3, 7.6.7, 7.4.12 and 7.2.13, with disabling the wildcard option as the
  workaround. The same batch fixes an FGFM authentication bypass in FortiManager that lets a certificate-holder
  impersonate any managed FortiGate, and a FortiClient Windows buffer overflow reachable by an attacker who can craft
  DNS responses.
discovered_at: "2026-08-14T05:00:00Z"
event_date: "2026-08-12"
run_id: 2026-08-14T0417Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - pre-auth
  - patch-available
  - rce
regions:
  - global
  - europe
sectors:
  - public-sector
  - technology
entities: []
techniques:
  - T1190
  - T1557
  - T1068
affected_products:
  - "Fortinet FortiWeb"
  - "Fortinet FortiManager"
  - "Fortinet FortiManager Cloud"
  - "Fortinet FortiClient (Windows)"
cves:
  - id: CVE-2026-26035
    cvss: "8.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiWeb 8.0.0–8.0.2, 7.6.0–7.6.6, 7.4.0–7.4.11, 7.2.0–7.2.12 (only where a Remote RADIUS Type admin account has the wildcard setting enabled)"
    fixed: "8.0.3 / 7.6.7 / 7.4.12 / 7.2.13"
  - id: CVE-2026-70468
    cvss: "7.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiManager and FortiManager Cloud 7.6.1, 7.4.3–7.4.5, 7.2.5–7.2.9 (FortiManager 8.0 not affected)"
    fixed: "7.6.2 / 7.4.6 / 7.2.10"
  - id: CVE-2026-70465
    cvss: "7.3"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: "FortiClient Windows 7.4.0–7.4.3, 7.2.0–7.2.11 (8.0 not affected)"
    fixed: "7.4.4 / 7.2.12"
sources:
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-158"
    publisher: "Fortinet PSIRT"
    date: "2026-08-12"
    role: primary
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-160"
    publisher: "Fortinet PSIRT"
    date: "2026-08-12"
    role: primary
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-156"
    publisher: "Fortinet PSIRT"
    date: "2026-08-12"
    role: primary
  - url: "https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/"
    publisher: "SecurityWeek"
    date: "2026-08-13"
    role: corroborating
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0300.html"
    publisher: "NCSC-NL"
    date: "2026-08-13"
    role: corroborating
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0299.html"
    publisher: "NCSC-NL"
    date: "2026-08-13"
    role: corroborating
  - url: "https://filestore.fortinet.com/fortiguard/rss/ir.xml"
    publisher: "Fortinet PSIRT advisory feed"
    date: "2026-08-12"
    role: corroborating
  - url: "https://www.fortiguard.com/psirt/FG-IR-26-163"
    publisher: "Fortinet PSIRT"
    date: "2026-08-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An Improper Authentication vulnerability  [CWE-287] in the FortiWeb Remote Radius Type Admin Authentication configured with specific, non-default settings may allow a remote unauthenticated attacker to login into the Fortiweb GUI/CLI with a random username and password"
    publisher: "Fortinet PSIRT (FG-IR-26-158)"
  - quote: "The weakness is associated with the wildcard setting for administrator accounts, which is disabled by default. When it is enabled, the system will match any username on a remote server with the Remote User account."
    publisher: "SecurityWeek"
verification: multi-source
sourcing_note: "Fortinet's PSIRT advisories are the primaries and every CVSS figure in the frontmatter is the vendor's own. The Dutch national CERT scores three of these flaws differently — 9.8 against Fortinet's 8.8 for CVE-2026-26035, 8.1 against 7.3 for CVE-2026-70468, and 5.3 against 4.8 for CVE-2026-70466 — and each divergence is stated in the body where the flaw is described. The two Dutch advisories cover the FortiWeb pair and the FortiManager flaw separately — neither carries the FortiClient flaw, which is sourced to Fortinet alone."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "On every FortiWeb appliance, check whether any Remote-type administrator account has the wildcard option enabled (System → Administrators in the GUI, or the `wildcard` setting on the admin account in the CLI) and disable it — that closes CVE-2026-26035 without waiting for a maintenance window, and an appliance with it enabled accepts an administrative login with a random username and password from anyone who can reach the management interface."
  - "On FortiManager and FortiManager Cloud, disable the `fgfm-peercert-withoutsn` option under `config system global` or upgrade to 7.6.2 / 7.4.6 / 7.2.10 — while it is enabled, any holder of a valid certificate can impersonate any FortiGate the FortiManager manages, which is a path into device configuration rather than a flaw in one device."
migrated_from: null
---

Fortinet published eight security advisories dated 2026-08-12, of which the Dutch national CERT carried the FortiWeb pair and the FortiManager flaw to European constituents in two separate advisories the next day ([Fortinet PSIRT advisory feed](https://filestore.fortinet.com/fortiguard/rss/ir.xml); [NCSC-NL NCSC-2026-0300, 2026-08-13](https://advisories.ncsc.nl/2026/ncsc-2026-0300.html); [NCSC-NL NCSC-2026-0299, 2026-08-13](https://advisories.ncsc.nl/2026/ncsc-2026-0299.html)). The flaw that matters most is **CVE-2026-26035** in FortiWeb, Fortinet's web application firewall. Fortinet's own summary states that ["An Improper Authentication vulnerability  [CWE-287] in the FortiWeb Remote Radius Type Admin Authentication configured with specific, non-default settings may allow a remote unauthenticated attacker to login into the Fortiweb GUI/CLI with a random username and password"](https://www.fortiguard.com/psirt/FG-IR-26-158). The setting in question is `wildcard` on a Remote-type administrator account: it is disabled by default, and ["When it is enabled, the system will match any username on a remote server with the Remote User account"](https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/) — the appliance stops checking *which* identity the RADIUS server authenticated and accepts the fact that it authenticated one at all. Affected releases are FortiWeb 8.0.0 through 8.0.2, 7.6.0 through 7.6.6, 7.4.0 through 7.4.11 and 7.2.0 through 7.2.12; the fixes are 8.0.3, 7.6.7, 7.4.12 and 7.2.13, and the vendor's workaround is simply to turn the wildcard option off ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-158)). Note that the two advisories disagree on severity: Fortinet scores it CVSS v3 8.8, while [NCSC-NL records CVE-2026-26035 at CVSS v3 9.8](https://advisories.ncsc.nl/2026/ncsc-2026-0300.html). This entry carries the vendor's own number, which is the one that travels with the record — but a European reader triaging from the national advisory will see the higher score.

**Why this warrants attention ahead of the ordinary patch cycle even though nothing is exploited.** Fortinet records the flaw as internally discovered during an audit, rates it 8.8, and states plainly that it is not known to be exploited; SecurityWeek confirms Fortinet makes no mention of exploitation for any of the batch ([SecurityWeek, 2026-08-13](https://www.securityweek.com/fortinet-patches-authentication-flaws-in-fortiweb-and-fortimanager/)). What forces the timeline is the mechanics rather than any observed activity: the advisory names the precise configuration precondition, and the resulting test is an ordinary login attempt with an arbitrary name, so anyone reading the bulletin can determine remotely whether a given FortiWeb is in the vulnerable state. There is no exploit to build. The exposure is narrower than the CVSS suggests — an estate that authenticates administrators locally, or with the wildcard option off, is not affected at all — which makes the first action a configuration check rather than an upgrade, and it can be answered from the CLI in seconds.

**Two more in the same batch that touch the management plane.** **CVE-2026-70468** is an authentication bypass using an alternate path in FortiManager and FortiManager Cloud: per Fortinet, a remote unauthenticated attacker holding a valid certificate may impersonate any FortiGate managed by that FortiManager through crafted FGFM requests, when the `fgfm-peercert-withoutsn` CLI option is set ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-160)). That option instructs the manager not to bind a peer certificate to a device serial number, so certificate validity substitutes for device identity — the same shape of defect as the FortiWeb bug one layer up the stack. FortiManager 8.0 is not affected; 7.6.1, 7.4.3 through 7.4.5 and 7.2.5 through 7.2.9 are, fixed in 7.6.2, 7.4.6 and 7.2.10, with disabling the option as the workaround. The severity divergence recurs here: Fortinet scores this one 7.3 and [the Dutch advisory 8.1](https://advisories.ncsc.nl/2026/ncsc-2026-0299.html), and this entry again carries the vendor's number. **CVE-2026-70465** is a buffer copy without checking the size of input in FortiClient Windows that, in Fortinet's words, may allow an unauthenticated attacker in a position to alter or craft DNS responses to the targeted host to execute arbitrary code via malicious packets; Fortinet classes its impact as escalation of privilege, credits Nir Chako of Pentera, and fixes it in 7.4.4 and 7.2.12, with a workaround of disabling application-based filtering in the FortiClient EMS VPN configuration ([Fortinet PSIRT, 2026-08-12](https://www.fortiguard.com/psirt/FG-IR-26-156)). The other five advisories in the same batch are lower severity and did not drive this entry: a FortiWeb WAF Content-Encoding evasion (FG-IR-26-157 / CVE-2026-70466, which Fortinet scores CVSS v3 4.8 and [the Dutch advisory 5.3](https://advisories.ncsc.nl/2026/ncsc-2026-0300.html)), a stack buffer overflow in the FortiOS explicit-proxy daemon (FG-IR-26-161), a FortiOS user-interface denial of service (FG-IR-26-162), a server-side request forgery in FortiSIEM (FG-IR-26-159), and Fortinet's assessment of the Apache HTTP/2 Bomb issue CVE-2026-49975 across [FortiPAM, FortiProxy and FortiSwitchManager](https://www.fortiguard.com/psirt/FG-IR-26-163) (FG-IR-26-163) ([Fortinet PSIRT advisory feed](https://filestore.fortinet.com/fortiguard/rss/ir.xml)).

**Detection and exposure.** For the FortiWeb flaw, the telemetry that matters is administrative authentication on the appliance itself: successful administrator logons whose username does not correspond to any account your directory actually holds, or repeated administrative sessions whose RADIUS-returned identity differs from the configured admin account, are what a successful wildcard match looks like from the appliance's own logs — and because the outcome is a legitimate administrative session, everything downstream of it will appear as authorised configuration activity. For the FortiManager flaw, the equivalent signal is a device registering or checking in against a serial number that does not match the certificate presented, or a managed device appearing to connect from a network position it has never used. Fortinet's standing guidance on this device class applies regardless of patch state: management interfaces on FortiWeb and FortiManager have no business being reachable from the public internet, and the appliance-level exposure question is worth answering before the version-level one, because it is the control that survives the next disclosure in this family.
