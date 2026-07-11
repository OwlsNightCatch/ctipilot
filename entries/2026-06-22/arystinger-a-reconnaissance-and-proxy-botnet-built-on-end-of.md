---
schema: 1
kind: vulnerability
horizon: operational
title: "AryStinger: a reconnaissance-and-proxy botnet built on end-of-life D-Link routers and QNAP NAS"
headline: "AryStinger: a reconnaissance-and-proxy botnet built on end-of-life D-Link routers and QNAP NAS"
summary: "A previously-undocumented botnet, AryStinger, has conscripted 4,300+ end-of-life D-Link routers (DIR-850L, DIR-818LW) and QNAP NAS devices into a distributed reconnaissance-and-proxy network — and Sweden is its third-largest victim pool at 6.4%. Initial access is three public CVEs (two decade-old D-Link RCEs plus a 2025 QNAP code-injection), after which each node gets a Dropbear SSH backdoor and is tasked with distributed DNS brute-forcing and traffic tunnelling that launders the operator's attack traffic (QiAnXin XLab, 2026-06-17). EoL D-Link models have no patch path — replacement is the only fix."
discovered_at: "2026-06-22T04:52:29Z"
event_date: 2026-06-21
run_id: 2026-06-22-dece656d
priority: high
immediate_action: null
tags:
  - botnet
  - actively-exploited
  - rce
  - ot-ics
regions:
  - global
  - europe
  - nordics
sectors:
  - public-sector
  - education
  - telco
entities:
  - "campaign:arystinger-botnet"
cves:
  - id: CVE-2013-3307
    cvss: "8.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
      - exploited
  - id: CVE-2016-5681
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
      - exploited
  - id: CVE-2025-11837
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
      - exploited
sources:
  - url: "https://blog.xlab.qianxin.com/arystinger-botnet-hijacks-legacy-routers-for-global-attacks-en/"
    publisher: QiAnXin XLab
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/arystinger-botnet-infected-thousands-of-d-link-routers-worldwide/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence:
  - quote: "QiAnXin XLab disclosed AryStinger, a previously-undocumented botnet its telemetry first observed on 2026-03-12, with English-language follow-up reporting on 2026-06-21 (QiAnXin XLab, 2026-06-17; BleepingComputer, 2026-06-21)."
    publisher: ctipilot v2 brief (migrated)
verification: multi-source
sourcing_note: "migration: evidence backfilled from v2 brief body (item predates the Evidence footer field)"
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-22.md
---

QiAnXin XLab disclosed AryStinger, a previously-undocumented botnet its telemetry first observed on 2026-03-12, with English-language follow-up reporting on 2026-06-21 ([QiAnXin XLab, 2026-06-17](https://blog.xlab.qianxin.com/arystinger-botnet-hijacks-legacy-routers-for-global-attacks-en/); [BleepingComputer, 2026-06-21](https://www.bleepingcomputer.com/news/security/arystinger-botnet-infected-thousands-of-d-link-routers-worldwide/)). Unlike the DDoS- and cryptomining-oriented router botnets that dominate this device class, AryStinger's design centre is **pre-intrusion reconnaissance and traffic laundering**: infected nodes are enrolled as "Executors" and handed distributed scanning and DNS-brute-force tasks by a C2 controller, and they relay the operator's attack traffic so its true origin is hidden. XLab counts at least 4,300 infected nodes and rising, distributed South Korea 48.5%, China 31.8%, **Sweden 6.4%**, Malaysia 3.5%, Singapore 2.5%; detection rate on public multi-engine scanning was zero at disclosure.

**Initial access — three public CVEs across two device classes.** The router variant spreads through `CVE-2013-3307` (command injection in Linksys/D-Link models built on the Realtek RTL819X SoC family) and `CVE-2016-5681` (a stack-based buffer overflow in the D-Link DIR-850L HTTP service) — both unauthenticated RCE on devices manufactured 2012–2015. From 2026-04-26 a second, NAS-targeting variant began exploiting `CVE-2025-11837`, a code-injection flaw in QNAP's Malware Remover utility (fixed in build `6.6.8.20251023`; QNAP's advisory scopes the affected product to the 6.6.x line — update to the latest build). Mapped to `T1190` Exploit Public-Facing Application ([T1190](https://attack.mitre.org/techniques/T1190/)). The most infected models — D-Link DIR-850L (75% of nodes) and DIR-818LW (13%) — are **end-of-life with no firmware fix** (D-Link support bulletin SAP10503), so for the router population there is no patch and replacement is the only remediation.

**Post-exploitation and persistence.** After exploitation a downloader pulls the current payload from C2, the bot authenticates with a unique Executor ID, and a **Dropbear SSH server is deployed on a fixed non-standard port** with an `iptables` rule added to allow inbound C2 traffic — establishing persistent, system-level remote access ([QiAnXin XLab, 2026-06-17](https://blog.xlab.qianxin.com/arystinger-botnet-hijacks-legacy-routers-for-global-attacks-en/)). This combines `T1133` External Remote Services ([T1133](https://attack.mitre.org/techniques/T1133/)) for the SSH backdoor with `T1562.004` Impair Defenses: Disable or Modify System Firewall ([T1562.004](https://attack.mitre.org/techniques/T1562/004/)) for the firewall change. The router binary masquerades under a system-daemon-like process name (`T1036` Masquerading, [T1036](https://attack.mitre.org/techniques/T1036/)).

**Two malware variants, different capability tiers.** The constrained RTL819X C variant carries `massdns`-style distributed DNS reconnaissance and a NAT-traversal tunnelling module (`T1572` Protocol Tunneling, [T1572](https://attack.mitre.org/techniques/T1572/); `T1090.002` external proxy, [T1090.002](https://attack.mitre.org/techniques/T1090/002/)). The Go "Standard" variant for more-capable hosts (NAS) bundles off-the-shelf offensive tooling — `fscan`, `ksubdomain`, `httpx`, `tlsx` — for network-service discovery and subdomain enumeration (`T1046` Network Service Discovery, [T1046](https://attack.mitre.org/techniques/T1046/); `T1595` Active Scanning, [T1595](https://attack.mitre.org/techniques/T1595/)), plus remote command execution and source-level payload execution in Go/Java/Python. C2 is HTTP/HTTPS with Protobuf message bodies under XOR obfuscation; a hardcoded key string embeds a 2024 marker, suggesting the operation predates the 2026 first-sighting.

**Why this matters to a Swiss/EU public-sector SOC.** The direct exposure is indirect but real: EoL D-Link SOHO routers persist in branch offices, municipal sites, and home-office setups, and QNAP NAS appliances are widely used as departmental file shares — both populations sit on the audience's attack surface, and Sweden's 6.4% share shows European devices are already being conscripted. A node's job is to *scan and proxy*, so a compromised device inside or adjacent to an organisation's network becomes a launch point for credential brute-forcing and lateral reconnaissance that looks like it originates from trusted infrastructure.

**Hunt and detection concepts (no IOCs).** On Linux/MIPS network appliances, hunt for an unexpected Dropbear (or any) SSH daemon listening on a non-standard port and for `iptables` rules added outside change management. On QNAP and other Linux NAS, alert on `curl`/`python` (or other interpreters) spawned from the security-utility process tree (`T1059.006`, [T1059.006](https://attack.mitre.org/techniques/T1059/006/)) and on file writes into `/tmp/bin/` by a service account that should not be writing executables. Network-side, watch for bursts of outbound DNS queries consistent with mass subdomain brute-forcing from edge/IoT VLAN segments, and for long-lived outbound SSH from device-management ranges. Inventory edge devices for the affected D-Link models and for QNAP Malware Remover build numbers.

**Hardening.** Replace EoL D-Link DIR-850L / DIR-818LW (and same-era RTL819X models) — there is no firmware path. Patch QNAP Malware Remover to `6.6.8.20251023` or later. Restrict inbound SSH on management VLANs to known jump hosts, and apply egress filtering so SOHO/IoT segments cannot freely initiate outbound SSH or high-volume DNS. Attribution: XLab claims none; the brief reports the activity as XLab characterises it, not as a named actor.
