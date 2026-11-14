---
schema: 1
kind: vulnerability
title: "Microsoft November 2026 Patch Tuesday: seven of the unauthenticated network flaws rated CVSS 9.8, in domain infrastructure and server roles, among them a Kerberos relay to a domain controller (CVE-2026-85844) and zero-click code execution through Exchange attachment indexing (CVE-2026-116928); none exploited or disclosed"
headline: "Patch Tuesday: Kerberos relay to a DC and Exchange zero-click RCE lead the 9.8 server rows; none exploited"
summary: >
  Microsoft's November 2026 updates fix seven unauthenticated network flaws in domain and server roles scored CVSS 3.1 9.8 that no record marks exploited or publicly disclosed: a Kerberos authentication relay that gives an unauthenticated attacker SYSTEM on a domain controller (CVE-2026-85844), code execution on an Exchange server through the Windows Search component when it indexes a crafted attachment, with no user action (CVE-2026-116928), and code-execution flaws in Windows DNS, DHCP Server, LDAP, iSCSI and SQL Server. The fixes are the November cumulative updates and SQL Server updates; the exploited Outlook flaw of the same release is a separate item.
discovered_at: "2026-11-11T03:37:30Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, zero-click, rce, auth-bypass, patch-available]
regions: [global]
sectors: []
entities: ["product:microsoft-exchange-server"]
techniques: [T1190, T1210, T1557]
affected_products: ["Microsoft Windows Server", "Microsoft Exchange Server", "Microsoft SQL Server"]
cves:
  - id: CVE-2026-85844
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows Kerberos on supported Windows Server and Windows client releases"
    fixed: "the November 2026 cumulative update for each release, for example KB5131291 (Windows Server 2016), KB5131085 (Server 2019), KB5131090 (Server 2022), KB5131080 or KB5131077 (Server 2025)"
  - id: CVE-2026-116928
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows Search component, reached on Exchange Server through automatic attachment indexing"
    fixed: "the November 2026 cumulative update for the release the Exchange server runs on, for example KB5131291 (Windows Server 2016), KB5131085 (Server 2019), KB5131090 (Server 2022), KB5131080 or KB5131077 (Server 2025)"
  - id: CVE-2026-88218
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows DNS Server"
    fixed: "the November 2026 cumulative update for the release"
  - id: CVE-2026-88243
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows DHCP Server"
    fixed: "the November 2026 cumulative update for the release"
  - id: CVE-2026-119958
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows LDAP service"
    fixed: "the November 2026 cumulative update for the release"
  - id: CVE-2026-88234
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Windows iSCSI"
    fixed: "the November 2026 cumulative update for the release"
  - id: CVE-2026-116945
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SQL Server 2017, 2019, 2022 and 2025 (GDR and CU branches)"
    fixed: "the November 2026 SQL Server GDR or CU update for the branch, for example KB5129299 (2025 CU10) and KB5129300 (2022 CU27)"
sources:
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85844"
    publisher: "Microsoft (Security Update Guide, CVE-2026-85844)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116928"
    publisher: "Microsoft (Security Update Guide, CVE-2026-116928)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88218"
    publisher: "Microsoft (Security Update Guide, CVE-2026-88218)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-119958"
    publisher: "Microsoft (Security Update Guide, CVE-2026-119958)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88243"
    publisher: "Microsoft (Security Update Guide, CVE-2026-88243)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88234"
    publisher: "Microsoft (Security Update Guide, CVE-2026-88234)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-95882"
    publisher: "Microsoft (Security Update Guide, CVE-2026-95882)"
    date: "2026-11-10"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116945"
    publisher: "Microsoft (Security Update Guide, CVE-2026-116945)"
    date: "2026-11-10"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/"
    publisher: "BleepingComputer"
    date: "2026-11-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unauthenticated attacker could send specially crafted Kerberos authentication traffic and relay the resulting authentication to an affected domain controller."
    publisher: "Microsoft"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85844"
  - quote: "Exchange automatically processes the attachment for indexing, so the recipient does not need to open the email or attachment."
    publisher: "Microsoft"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116928"
  - quote: "Double free in Windows DNS allows an unauthorized attacker to execute code over a network."
    publisher: "Microsoft"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88218"
  - quote: "An unauthenticated attacker who successfully exploited this vulnerability could gain code execution through a specially crafted set of LDAP calls to execute arbitrary code within the context of the LDAP service."
    publisher: "Microsoft"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-119958"
  - quote: "The attacker does not need SQL Server credentials or additional user interaction when the package runs automatically."
    publisher: "Microsoft"
    source_url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116945"
verification: multi-source
sourcing_note: >
  Each flaw's description, score and fix come from its own Security Update Guide record, read through Microsoft's update-guide API because the pages are a script-built application; BleepingComputer corroborates the release and the single exploited flaw. Microsoft's records give no exploitation, public-disclosure or proof-of-code statement for these rows beyond a temporal score that marks exploit code unproven on the Kerberos and Windows Search rows. The DNS, DHCP Server and iSCSI records state only an in-network attacker calling arbitrary endpoints and the LDAP record crafted LDAP calls, with no further mechanism. Other rows of the release are not covered here: further 9.8 rows (DirectMusic, Media Foundation, Xbox Live Networking Service, Color Management and several cloud services) and the authenticated ones (SharePoint, Azure DevOps Server, developer tools).
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
  - "Install the November 2026 cumulative update on every domain controller and every Exchange server first, then on DNS, DHCP and SQL Server hosts, because the Kerberos relay ends in SYSTEM on a domain controller and the Exchange flaw runs code from an inbound mail attachment that nobody has to open."
updates: []
migrated_from: null
---

Microsoft's November 2026 Patch Tuesday fixes seven flaws in domain infrastructure and server roles scored CVSS 3.1 9.8 that need no credentials over the network (the release carries further 9.8 rows, DirectMusic among them, that are not covered here ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-95882))); the only record Microsoft marks as exploited in this release is the Outlook zero-day, which is a separate item, and none of these rows is marked exploited or publicly disclosed ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85844); [BleepingComputer, 2026-11-10](https://www.bleepingcomputer.com/news/microsoft/microsoft-november-2026-patch-tuesday-fixes-1-235-flaws-outlook-zero-day/)). Two have mechanics that make the timeline short. CVE-2026-85844 is an authentication bypass in Windows Kerberos: an unauthenticated attacker sends crafted Kerberos authentication traffic and relays the resulting authentication to an affected domain controller, with no user interaction ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-85844)). CVE-2026-116928 is an out-of-bounds write in the Windows Search component that Exchange Server uses: an attacker emails a crafted attachment, Exchange indexes it automatically, so "the recipient does not need to open the email or attachment", and the code runs with the permissions of the processing service ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116928)).

The other five are described more thinly: a double free in Windows DNS (CVE-2026-88218) ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88218)), an out-of-bounds read in Windows DHCP Server (CVE-2026-88243) ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88243)) and a release of an invalid pointer in Windows iSCSI (CVE-2026-88234) ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-88234)), each reachable by an in-network attacker calling arbitrary endpoints; an out-of-bounds write in the Windows LDAP service that gives code execution in its context through crafted LDAP calls (CVE-2026-119958) ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-119958)); and a heap overflow in SQL Server (CVE-2026-116945) that needs an attacker who controls a network endpoint an integration package connects to, with no credentials or user interaction when the package runs automatically ([Microsoft, 2026-11-10](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-116945)). The fixes are the November cumulative updates per release, for example KB5131291 (Windows Server 2016), KB5131085 (Server 2019), KB5131090 (Server 2022) and KB5131080 or KB5131077 (Server 2025), and the November SQL Server updates, for example KB5129299 (2025 CU10) and KB5129300 (2022 CU27).

**Exposure:** domain controllers (Kerberos, LDAP, DNS), DNS and DHCP servers, Exchange servers that receive mail from the internet, and SQL Server hosts that run Integration Services packages against endpoints an attacker could control; the installed cumulative update shows in the update history of each host.

**Detection:** no exploitation is reported, so detection is hardening-grade: crashes or restarts of the DNS Server, DHCP Server and LSASS processes on domain controllers, Kerberos or LDAP bursts from workstation networks toward domain controllers, content-indexing or transport worker crashes on Exchange after inbound mail with unusual attachments, and an inventory of which domain controllers and Exchange servers already carry the November update.

**Defender takeaway:** put the November update on domain controllers and internet-facing Exchange servers first; Microsoft's records give an unauthenticated attacker a relay to a domain controller and a mail-borne path to code execution on Exchange, and the DNS, DHCP and iSCSI rows are reachable by an in-network attacker, so keep those services off untrusted segments until they are patched.
