---
schema: 1
kind: vulnerability
title: Ubiquiti UniFi OS triple-flaw chain to unauthenticated root (CVE-2026-34908 / -34909 / -34910)
headline: Ubiquiti UniFi OS triple-flaw chain to unauthenticated root (CVE-2026-34908 / -34909 / -34910)
summary: "CISA KEV-listed three maximum-severity Ubiquiti UniFi OS flaws (CVE-2026-34908 / -34909 / -34910) on 2026-06-23 — chained, an unauthenticated attacker reaches OS command execution as root on internet-reachable UniFi gateways, consoles and NVRs. Patched — apply UniFi OS 5.0.8 for UniFi OS Server and the current fixed build for each appliance per Ubiquiti's advisory; UniFi is dense across DACH/EU schools, clinics and local government. Today's deep dive — § 5."
discovered_at: "2026-06-24T05:11:57Z"
event_date: 2026-06-08
run_id: 2026-06-24-de656486
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - pre-auth
  - rce
  - auth-bypass
  - patch-available
regions:
  - global
  - europe
  - dach
sectors:
  - public-sector
  - healthcare
  - education
entities: []
cves:
  - id: CVE-2026-34908
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
  - id: CVE-2026-34909
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
  - id: CVE-2026-34910
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
sources:
  - url: "https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/"
    publisher: BleepingComputer
    role: primary
  - url: "https://www.scworld.com/brief/ubiquiti-unifi-os-server-vulnerabilities-allow-unauthenticated-remote-code-execution"
    publisher: SC Media
    role: corroborating
closed_sources: []
evidence:
  - quote: "CVE-2026-34908 (improper access control) and CVE-2026-34909 (path traversal) can bypass authentication, allowing access to a vulnerable endpoint."
    publisher: SC Media
  - quote: Ubiquiti patches three max severity UniFi OS vulnerabilities
    publisher: BleepingComputer
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: firewall-vpn-rce
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-24.md
---

On 2026-06-23 CISA added three Ubiquiti UniFi OS vulnerabilities to its Known Exploited Vulnerabilities catalog — confirmation that they are being exploited in the wild — having entered them as the "Improper Access Control," "Path Traversal" and "Improper Input Validation" vulnerabilities respectively. All three are rated maximum severity by BleepingComputer's reporting (CVSS 10.0 on the CVE records for the access-control and path-traversal flaws), and chained they take an unauthenticated, network-adjacent attacker to **OS command execution as root** on the management plane of Ubiquiti's UniFi OS appliance family ([BleepingComputer, 2026-05-22](https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/); [SC Media, 2026-06-08](https://www.scworld.com/brief/ubiquiti-unifi-os-server-vulnerabilities-allow-unauthenticated-remote-code-execution)). UniFi OS is the management substrate for UniFi Dream Machine gateways/firewalls, UniFi consoles, Network Video Recorders (UNVR), Express, EFG and the software UniFi OS Server — a footprint that is dense across DACH/EU schools, clinics, SMEs and local-government networks, frequently with the console reachable for remote administration.

**The chain.** The three flaws compose into a single pre-authentication path:

- **CVE-2026-34908 — improper access control (CWE-284).** Bypasses authentication on a management endpoint, granting an unauthenticated request access it should not have. On its own it yields no code execution, but it changes the trust boundary the later steps depend on.
- **CVE-2026-34909 — path traversal (CWE-22).** Reads files on the underlying system that should not be reachable through the endpoint — the practical role being to surface material the final step consumes.
- **CVE-2026-34910 — improper input validation → command injection (CWE-20).** The endpoint passes attacker-controlled input into an OS command without sanitisation, achieving command execution as **root**. This is the flaw CISA names in the KEV entry as actively exploited.

SC Media's analysis states the access-control and path-traversal flaws "can bypass authentication, allowing access to a vulnerable endpoint," after which the input-validation flaw yields unauthenticated RCE with root privileges ([SC Media, 2026-06-08](https://www.scworld.com/brief/ubiquiti-unifi-os-server-vulnerabilities-allow-unauthenticated-remote-code-execution)). Because CVE-2026-34908 is what re-shapes the trust boundary, a partial update that addresses only the command-injection flaw is **not** sufficient — the full fixed UniFi OS version must be applied. Maps to [`T1190` Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190/) for initial access and [`T1068` Exploitation for Privilege Escalation](https://attack.mitre.org/techniques/T1068/) for the root outcome.

**Affected and patched versions.** UniFi OS Server is affected through 5.0.6 and fixed in **5.0.8** ([SC Media, 2026-06-08](https://www.scworld.com/brief/ubiquiti-unifi-os-server-vulnerabilities-allow-unauthenticated-remote-code-execution)); the appliance line (UDM / UDR / Express / UNVR / EFG consoles) is fixed in the corresponding UniFi OS 5.1.x release ([BleepingComputer, 2026-05-22](https://www.bleepingcomputer.com/news/security/ubiquiti-patches-three-max-severity-unifi-os-vulnerabilities/) reports the patched set but not per-model build strings). **Confirm the exact fixed build for each model against Ubiquiti's advisory** rather than assuming a single release line is clean, and verify that auto-update actually applied the fixed build.

**Hunt and detection concepts (no IOCs).** These are Linux-based network appliances that rarely carry EDR, so detection leans on the network and the device's own logs: the highest-value signal is the UniFi OS management process spawning unexpected shell children or executing `curl`/`wget` (anomalous process lineage from the web daemon); outbound connections originating *from* the appliance to infrastructure that is not Ubiquiti's update/cloud endpoints; and inbound scanning or anomalous request patterns against the management endpoints from outside the management network. Treat any UniFi console that has been internet-reachable and unpatched since the 2026-06-23 KEV date as potentially compromised, not merely vulnerable, and inspect for unauthorised configuration or account changes.

**Hardening / mitigation.** Apply the full fixed UniFi OS version per model; remove the management interface from internet exposure entirely (administer over LAN/VPN only) and place UniFi consoles on a segmented management VLAN with tight ingress; and, post-patch, rotate any credentials that the device handled and audit local accounts and configuration for tampering during the exposure window. The KEV remediation due date (2026-06-26) is a US-FCEB compliance date with no jurisdictional weight in CH/EU; the operational driver here is the confirmed in-the-wild exploitation of a pre-auth-to-root chain on widely-deployed, often-internet-reachable gear — not the deadline.
