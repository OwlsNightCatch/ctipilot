---
schema: 1
kind: threat
title: "PATCHCORD, SHEETCORD and HACKERAI — one espionage cluster runs three different command-and-control channels, two of them inside Google Sheets and GitHub, and persists by rewriting the victim's browser shortcuts"
headline: "Espionage implants run command-and-control through the Google Sheets API and persist by rewriting browser shortcuts"
summary: >
  Acronis Threat Research Unit documents three previously undocumented implants sharing one operator's
  infrastructure against Afghan telecom providers and South Asian critical infrastructure: PATCHCORD, a C/C++
  backdoor delivered by fake Afghan Telecom VPN and ministry installers, SHEETCORD, a Go implant whose
  command-and-control runs entirely through the Google Sheets API v4 using a hardcoded cloud service account
  and a per-victim spreadsheet tab, and HACKERAI C2 Agent, which does the same job through GitHub Gists. All
  three persist by hijacking browser shortcuts so the implant launches first and then starts the real browser,
  and PATCHCORD executes operator-supplied shellcode entirely in memory. The targeting is South Asian, but the
  tradecraft is not: two of the three channels terminate on Google- and GitHub-owned endpoints that most egress
  policy treats as benign.
discovered_at: "2026-08-17T04:28:31Z"
event_date: "2026-08-13"
run_id: 2026-08-17T0413Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, cloud]
regions: [apac]
sectors: [telco, energy, public-sector, defense]
entities: [actor:apt36, malware:patchcord, malware:sheetcord, malware:hackerai-c2-agent]
techniques: [T1204.002, T1547.009, T1547.001, T1102.002, T1071.001, T1620, T1059.001, T1059.003, T1057, T1082, T1497, T1622, T1564.003, T1140]
affected_products: []
cves: []
sources:
  - url: "https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/"
    publisher: "Acronis Threat Research Unit"
    date: "2026-08-13"
    role: primary
  - url: "https://thehackernews.com/2026/08/new-patchcord-backdoor-targets-afghan.html"
    publisher: "The Hacker News"
    date: "2026-08-13"
    role: corroborating
  - url: "https://securityaffairs.com/197266/intelligence/apt36-suspected-in-patchcord-espionage-campaign-using-google-sheets-c2.html"
    publisher: "Security Affairs"
    date: "2026-08-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "TRU assesses with moderate confidence that the activity overlaps with the broader APT36 (Transparent Tribe) cluster or a closely related Pakistan-linked threat actor based on targeting, malware similarities, infrastructure and operational tradecraft."
    publisher: "Acronis Threat Research Unit"
  - quote: "The SHEETCORD implant uses the Google Sheets API v4 with a hardcoded GCP service account for authentication and creates per-victim tabs in the operator's spreadsheet for bidirectional communication, all of which are consistent with the documented SHEETCREEP implant."
    publisher: "Acronis Threat Research Unit"
  - quote: "the shellcode itself is never written to disk, making this a fully in-memory execution chain that leaves minimal forensic artifacts on the victim's machine."
    publisher: "Acronis Threat Research Unit"
  - quote: "these observations alone are insufficient to support an attribution"
    publisher: "Acronis Threat Research Unit"
verification: single-source
sourcing_note: >
  Acronis Threat Research Unit is the sole assessor; The Hacker News and Security Affairs republish the same
  research rather than observing the activity independently, so this is one assessor with three publishers.
  The attribution is carried at the confidence the lab itself states — a moderate-confidence overlap with the
  APT36 cluster or a closely related Pakistan-linked actor, not an attribution. Acronis separately records an
  infrastructure fingerprint shared with tooling previously attributed to SilverFox and explicitly declines to
  treat it as an attribution link; this entry does the same.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Acronis Threat Research Unit has published an analysis of three previously undocumented implants that share one operator's infrastructure and one design idea: put the command-and-control channel somewhere the network already trusts ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)). The named targeting is Afghan telecom providers and South Asian government, defence and energy organisations, reached through sector-specific lures — Inno Setup installers impersonating an Afghan Telecom service-management tool and VPN client, an archive themed on a second Afghan operator, and an installer and decoy document themed on Afghanistan's Ministry of Communications and Information Technology.

PATCHCORD, the C/C++ implant, is the baseline. It hides its console window, establishes persistence, fingerprints the host and enters a polling loop against a hardcoded server. Its persistence is the part worth reading twice: it enumerates `.lnk` files across five locations including the taskbar, Quick Launch, Start Menu and both desktop folders, resolves each shortcut's real target through the `IShellLinkW` and `IPersistFile` COM interfaces to confirm it points at a genuine Microsoft Edge, Google Chrome or Mozilla Firefox binary, backs the original up, then rewrites the shortcut to launch the implant with the real browser path passed as an argument — preserving the original icon so nothing looks changed. Clicking the browser runs the implant first, which then silently starts the real browser so the user notices nothing. Its most consequential command decodes and decrypts an operator-supplied payload, allocates memory with `VirtualAlloc`, flips it to `PAGE_EXECUTE_READ` with `VirtualProtect` and runs it via `CreateThread`; Acronis notes that "the shellcode itself is never written to disk, making this a fully in-memory execution chain that leaves minimal forensic artifacts on the victim's machine" ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)).

SHEETCORD is the Go successor and the reason this cluster matters outside its own region. Rather than calling a server the operator has to keep alive, it authenticates to the Google Sheets API v4 with a hardcoded cloud service-account credential embedded in the binary and creates a per-victim tab in the operator's spreadsheet for two-way tasking and results — a design Acronis says is "consistent with the documented SHEETCREEP implant" it references from prior research ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)). It also diverges from PATCHCORD in ways that matter for detection: it runs commands through `powershell -Command` with script-block wrapping instead of `cmd.exe /c`, collects markedly less host information, widens the shortcut hijack from three browsers to six by adding Brave, Opera and Vivaldi, and generates a temporary VBScript to rewrite those shortcuts rather than using COM. It adds a persistence layer PATCHCORD lacks — a VBScript dropped into the user's Startup folder that launches the implant with a hidden window at every logon, plus a matching `HKCU` Run key written by shelling out to `reg.exe`. The third family, HACKERAI C2 Agent, was distributed from the cluster's earliest domain and shares the fingerprinting, remote-execution and shortcut-hijacking behaviour, but moves its tasking and exfiltration into GitHub Gists — a third distinct channel across one operator's toolset ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)).

A different PATCHCORD variant appears in what Acronis calls an earlier campaign, observed in March 2026 against India's energy sector behind a fuel-conservation-client lure, and it carries an anti-analysis suite the Afghan-telecom sample does not: checks for VirtualBox and VMware device handles, a floor on processor count and installed memory, both `IsDebuggerPresent` and the PEB debug flag, a scan of active TCP connections for ports associated with intercepting proxies, a process-name check against a hardcoded list of analysis tools, and cursor-movement monitoring — falling into a randomised 30-to-90-second sleep when any check fires, which Acronis describes as designed to exhaust sandbox timeouts without the process termination that would itself be suspicious. On attribution Acronis is careful, and this entry keeps its wording: it "assesses with moderate confidence that the activity overlaps with the broader APT36 (Transparent Tribe) cluster or a closely related Pakistan-linked threat actor", resting on sustained Afghan telecom and government targeting, a browser-credential harvesting tool previously seen in APT36 operations, a C2 framework independently documented as part of that group's toolkit, and the Google Sheets channel's resemblance to earlier work attributed at medium confidence to the same cluster ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)). Where an infrastructure fingerprint matched tooling previously attributed to a different, China-nexus operation, Acronis states that "these observations alone are insufficient to support an attribution" and does not carry the link forward ([Acronis TRU, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)).

**Defender takeaway:** the transferable half is the channel, not the victim list. An implant that authenticates to the Google Sheets API with an embedded service account and reads its tasking out of a spreadsheet cell produces egress that terminates on a Google-owned API endpoint, survives domain blocklists and reputation scoring, and looks in flow records like ordinary SaaS traffic; the GitHub Gist variant has the same property against a developer-tooling destination. The observable is the caller, not the destination: in proxy and egress telemetry, a host reaching `sheets.googleapis.com` or Gist endpoints with no browser session, no signed-in Workspace user and no sanctioned automation behind it is the anomaly, and server-class hosts with no developer function are where that reads cleanest. On the endpoint, three artifact classes carry the cluster: browser shortcut files whose target no longer points at the browser binary but passes it as an argument (with a `.backup` copy of the original left alongside), Startup-folder script drops and `HKCU` Run values created by `reg.exe` rather than by an installer, and the `VirtualAlloc` → `VirtualProtect(PAGE_EXECUTE_READ)` → `CreateThread` sequence in API telemetry, which is the only trace the in-memory payload leaves because nothing reaches disk.

**Triage:** browser shortcuts are legitimately rewritten by installers, enterprise deployment tooling and the browsers' own updaters, so a changed `.lnk` is not the signal on its own. The discriminator the mechanism supplies is that a hijacked shortcut points at a non-browser executable while carrying the real browser path as an argument and keeping the original icon, and that a `.backup` copy of the original sits next to it — an updater rewrites the target in place and leaves neither. Likewise, scripted Google Sheets access is ordinary in an organisation that automates reporting; what is not ordinary is a workstation or server authenticating to the Sheets API with a service-account credential that does not belong to any provisioned integration.
