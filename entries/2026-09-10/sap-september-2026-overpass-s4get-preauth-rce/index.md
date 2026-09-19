---
schema: 1
kind: vulnerability
title: "SAP September 2026 Patch Day: OVERPASS (CVE-2026-44756, CVSS 10.0) and S4GET (CVE-2026-58240, CVSS 9.8) — two unauthenticated pre-auth RCE flaws in shared SAP kernel components reachable through ports that cannot be firewalled without breaking normal SAP GUI/RFC use"
headline: "Two maximum-severity SAP kernel flaws are reachable through the same ports every SAP GUI and RFC client needs — network segmentation alone will not close them"
summary: >
  SAP's 8 September 2026 Patch Day fixed CVE-2026-44756 (OVERPASS, CVSS
  10.0), an unauthenticated memory-corruption flaw in kernel Extended
  Passport processing reachable via the web tier, SAP Dispatcher or RFC, and
  CVE-2026-58240 (S4GET, CVSS 9.8), an unauthenticated Message Server
  trust-bypass reachable on the port every SAP GUI client uses; both yield
  unauthenticated remote code execution across the SAP kernel-based product
  line. Neither is yet confirmed exploited, but Onapsis found over 10,000
  internet-facing SAP interfaces.
discovered_at: "2026-09-10T04:40:00Z"
updated_at: null
event_date: "2026-09-08"
run_id: 2026-09-10T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, auth-bypass]
regions: [global]
sectors: [public-sector]
entities: ["product:sap-netweaver-application-server-abap", "product:sap-abap-platform"]
techniques: [T1190, T1210]
affected_products: ["SAP NetWeaver Application Server ABAP", "SAP S/4HANA", "SAP Kernel", "SAP NetWeaver Message Server", "SAP Web Dispatcher", "SAP ERP / Business Suite (ECC)", "SAP BW/4HANA", "SAP Enterprise Portal", "SAP PI/PO", "SAP Solution Manager"]
cves:
  - id: CVE-2026-44756
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "KRNL64NUC 7.22/7.22EXT; KRNL64UC 7.22/7.22EXT/7.53/8.04; KERNEL 7.22/7.53/7.54/7.77/7.89/7.93/8.04/9.16/9.18/9.19/9.20; WEBDISP 9.16/9.18/9.19/9.20"
    fixed: "SAP Security Note 3747649 (kernel patch, closes all three routes); interim HTTP-only workaround in Note 3756304"
  - id: CVE-2026-58240
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SAP kernel 9.16/9.18/9.19/9.20 (SAP S/4HANA, S/4HANA Cloud Private Edition and other ABAP-based products on these kernel lines)"
    fixed: "SAP Security Note 3759472 — kernel patch levels 9.16/PL100, 9.18/PL32, 9.19/PL17, 9.20/PL7"
sources:
  - url: "https://onapsis.com/blog/sap-overpass-remediation/"
    publisher: "Onapsis Research Labs"
    date: "2026-09-09"
    role: primary
  - url: "https://onapsis.com/blog/s4get-cve-2026-58240-sap-message-server-threat-advisory/"
    publisher: "Onapsis Research Labs"
    date: "2026-09-09"
    role: primary
  - url: "https://cert.europa.eu/publications/security-advisories/2026-011/"
    publisher: "CERT-EU"
    date: "2026-09-09"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/sap-warns-of-maximum-severity-overpass-kernel-vulnerability/"
    publisher: "BleepingComputer"
    date: "2026-09-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A targeted search using high-fidelity fingerprints identifies more than 10,000 unique Internet-facing IP addresses presenting an SAP web interface reachable from the public Internet, and that figure is conservative."
    publisher: "Onapsis Research Labs"
  - quote: "Exploitation requires no credentials, no certificate, and no pre-existing misconfiguration. A successful attack yields full remote code execution as <sid>adm, the OS-level user that runs SAP, on every application server in the cluster."
    publisher: "Onapsis Research Labs"
verification: multi-source
sourcing_note: "CERT-EU's advisory relays SAP's patch-day fixes and Onapsis's own research rather than independently assessing the flaws; credibility reflects a single technical assessor (Onapsis) with several publishers."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Apply SAP Security Notes 3747649 (OVERPASS) and 3759472 (S4GET) to every SAP kernel-based system now — Onapsis found over 10,000 internet-facing SAP interfaces, and notes SAP patches have historically been reverse-engineered into working exploits within 72 hours, a window that keeps shrinking with AI-assisted tooling."
updates: []
migrated_from: null
---

SAP's 8 September 2026 Security Patch Day fixed CVE-2026-44756 ("OVERPASS", CVSS 10.0) and CVE-2026-58240 ("S4GET", CVSS 9.8), both discovered and responsibly disclosed by Onapsis Research Labs, both remotely exploitable pre-authentication ([CERT-EU, advisory 2026-011, 2026-09-09](https://cert.europa.eu/publications/security-advisories/2026-011/)). OVERPASS is a memory-corruption flaw in the SAP kernel's processing of the Extended Passport, a tracing structure attached to requests and parsed before session authentication; because the handling code is shared, the flaw is reachable via three independent unauthenticated routes — the Internet Communication Manager/Web Dispatcher (HTTP/HTTPS, Fiori/WebGUI/APIs), the SAP Dispatcher (the SAP GUI logon protocol), and RFC connections between systems — with a single crafted request corrupting memory to reach arbitrary OS command execution as the account that owns the SAP installation ([CERT-EU, 2026-09-09](https://cert.europa.eu/publications/security-advisories/2026-011/)). Onapsis's own internet-wide fingerprinting found more than 10,000 unique internet-facing IPs presenting an SAP web interface, a figure it calls conservative since it structurally undercounts the SAP Web Dispatcher, which returns no distinguishing banner ([Onapsis, 2026-09-09](https://onapsis.com/blog/sap-overpass-remediation/)). S4GET is a distinct logic flaw in the SAP NetWeaver Message Server (kernel lines 9.16-9.20, native to S/4HANA and S/4HANA Cloud Private Edition) reachable through the same public port every SAP GUI client connects to: a crafted packet gets an arbitrary IP address accepted as a trusted internal node, and the Message Server propagates that false trust across the cluster so the attacker can register with the Gateway as internal and invoke RFC-callable programs to reach code execution as `<sid>adm` on every application server — "exploitation requires no credentials, no certificate, and no pre-existing misconfiguration" ([Onapsis, 2026-09-09](https://onapsis.com/blog/s4get-cve-2026-58240-sap-message-server-threat-advisory/)). Because the flaw abuses the Gateway's trust-membership decision rather than its ACLs, the standard `secinfo`/`reginfo`/`ms/acl_info` hardening does not intercept it. Neither flaw is confirmed exploited as of publication, but Onapsis notes SAP patches have historically been reverse-engineered into working exploits within 72 hours — as happened with the RECON vulnerability (CVE-2020-6287) — and that window keeps shrinking with AI-assisted tooling, while a comparable pre-auth SAP disclosure (CVE-2025-31324) became 2025's most-exploited CVE by Mandiant's count ([Onapsis, 2026-09-09](https://onapsis.com/blog/sap-overpass-remediation/)). Fixed via SAP Security Note 3747649 (OVERPASS, a single kernel patch closing all three routes, with an HTTP-only interim workaround in Note 3756304) and Note 3759472 (S4GET, kernel patch levels 9.16 PL100/9.18 PL32/9.19 PL17/9.20 PL7).

**Defender takeaway:** patch now rather than relying on network segmentation — both flaws are reachable through ports every normal SAP GUI/RFC deployment already exposes internally, so a "not internet-facing" argument does not close OVERPASS's Dispatcher/RFC routes or S4GET's Message Server port.

**Triage:** an SAP Gateway or Message Server accepting a new application-server registration from an IP address that has never previously registered, or a burst of RFC-callable external-program invocations immediately following such a registration, is the S4GET trust-abuse pattern; normal application-server registration happens only at planned system startup, not ad hoc.
