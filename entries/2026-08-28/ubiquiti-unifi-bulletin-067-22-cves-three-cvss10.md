---
schema: 1
kind: vulnerability
horizon: operational
title: "Ubiquiti UniFi ecosystem: 22 CVEs in one bulletin, three at CVSS 10.0 — unauthenticated CRLF-injection auth bypass, and unauthenticated command injection in UniFi Protect and UniFi Talk"
headline: "Ubiquiti's August bulletin carries three separate unauthenticated maximum-severity flaws across its OS, video and telephony product lines in one release"
summary: >
  Ubiquiti's Security Advisory Bulletin 067 (2026-08-27) fixes 22 CVEs across the UniFi
  OS/Protect/Talk/Access/Network/Connect ecosystem. Three score CVSS 10.0: an authentication
  bypass via CRLF injection in UniFi OS devices, and unauthenticated command injection each in
  UniFi Protect and UniFi Talk. A further ten score 9.9–9.8. Vendor patches are available for the
  full set; NCSC-CH records current exploitation status as unknown, but notes a prior UniFi patch
  cycle was under criminal attack within weeks.
discovered_at: "2026-08-28T05:55:00Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, patch-available]
regions: [global, europe]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities: []
techniques: [T1190, T1078.001]
affected_products: ["Ubiquiti UniFi OS Server", "Ubiquiti UniFi Protect", "Ubiquiti UniFi Talk", "Ubiquiti UniFi Access", "Ubiquiti UniFi Network", "Ubiquiti UniFi Connect", "Ubiquiti UniFi Enterprise Audio/Video Bridge"]
cves:
  - id: CVE-2026-77550
    cvss: "10.0"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "UniFi OS devices — see Ubiquiti Security Advisory Bulletin 067"
    fixed: "UniFi OS Server 5.1.37"
  - id: CVE-2026-77537
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "UniFi Protect — see Ubiquiti Security Advisory Bulletin 067"
    fixed: "UniFi Protect 7.2.105"
  - id: CVE-2026-77554
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "UniFi Talk — see Ubiquiti Security Advisory Bulletin 067"
    fixed: "UniFi Talk 5.3.2"
sources:
  - url: "https://community.ui.com/releases/Security-Advisory-Bulletin-067/fc4a3488-7c43-4628-8bab-f715e96dbfc9"
    publisher: "Ubiquiti (Security Advisory Bulletin 067)"
    date: "2026-08-27"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12880"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-08-27"
    role: primary
  - url: "https://www.heise.de/news/Ubiquiti-schliesst-mehrere-kritische-Sicherheitsluecken-11431726.html"
    publisher: "Heise Security"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Successful exploitation could allow network-adjacent attackers to completely compromise affected devices, leading to full system takeover via authentication bypass, command injection, or privilege escalation."
    publisher: "NCSC Switzerland — Cyber Security Hub"
verification: multi-source
sourcing_note: >
  Ubiquiti's own advisory-hosting platform (community.ui.com) is a JavaScript SPA that returned
  only a loading shell to every direct/trafilatura/WebFetch transport this run. The structured
  CVE-to-description table above is transcribed from NCSC Switzerland's own Cyber Security Hub
  post — a national authority that independently parsed the vendor bulletin — corroborated by
  Heise Security's own independent reporting for the patched-version numbers: two parties reading
  Ubiquiti's primary bulletin separately, not one outlet republishing the other's assessment.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Patch every UniFi OS Server, Protect, Talk, Access, Network and Connect deployment to the fixed releases now (UniFi OS Server 5.1.37, UniFi Protect 7.2.105, UniFi Talk 5.3.2, UniFi Access 4.3.5, UniFi Network 10.5.67 per Heise's reporting) — three of the 22 flaws are unauthenticated, maximum-severity paths to full device takeover, and Ubiquiti's own May patch cycle was under criminal attack within roughly six weeks, so this batch should not be assumed safe on the strength of exploitation currently reading 'unknown'."
updates: []
migrated_from: null
---

NCSC Switzerland's Cyber Security Hub published an advisory on 2026-08-27 transcribing Ubiquiti's Security Advisory Bulletin 067: 22 CVEs across the UniFi OS/Protect/Talk/Access/Network/Connect ecosystem, many at maximum severity. The three CVSS 10.0 entries are CVE-2026-77550 (authentication bypass via CRLF injection in UniFi OS devices), CVE-2026-77537 (unauthenticated command injection in UniFi Protect), and CVE-2026-77554 (unauthenticated command injection in UniFi Talk). A further ten CVEs score 9.9–9.8 (CVSS 3.1), spanning authenticated command injection in UniFi Access/Protect, privilege escalation via improper access control in UniFi OS/UniFi Protect AI Key, and unauthenticated command injection in the UniFi Enterprise Audio/Video Bridge. All require only network access to UniFi OS management interfaces or applications; the unauthenticated entries need no privilege at all, while the authenticated command-injection entries need low or high privilege depending on the flaw.

Vendor patches are available for the full set — per Heise Security's reporting: UniFi OS Server 5.1.37, UniFi Protect 7.2.105, UniFi Talk 5.3.2, UniFi Access 4.3.5, UniFi Network 10.5.67 ([Heise Security, 2026-08-27](https://www.heise.de/news/Ubiquiti-schliesst-mehrere-kritische-Sicherheitsluecken-11431726.html)). NCSC-CH records current exploitation status as unknown for this batch: "successful exploitation could allow network-adjacent attackers to completely compromise affected devices, leading to full system takeover via authentication bypass, command injection, or privilege escalation" ([NCSC Switzerland Cyber Security Hub, 2026-08-27](https://community.ui.com/releases/Security-Advisory-Bulletin-067/fc4a3488-7c43-4628-8bab-f715e96dbfc9)) — but Heise notes historical context that argues against reading "unknown" as "safe": Ubiquiti UniFi OS vulnerabilities from a May 2026 patch cycle were already under criminal attack by the end of June 2026, so a comparably fast exploitation timeline for this batch should be actively watched for rather than assumed absent.

UniFi is heavily deployed in SME and public-sector network, access-control and video-surveillance infrastructure across Europe, and its product breadth — OS management plane, physical access control, video surveillance, telephony — means this single bulletin touches several distinct functional surfaces in the same estate at once. **Triage:** in the absence of a published exploitation narrative, the defensible detection posture is process- and configuration-anomaly monitoring on UniFi OS management interfaces — unexpected administrative session creation not tied to a known operator login, and command-execution telemetry on the underlying host that does not correspond to a documented UniFi OS operation — since the vendor has not yet published the specific request patterns an exploit would use.
