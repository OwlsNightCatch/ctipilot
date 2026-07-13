---
schema: 1
kind: incident
horizon: operational
title: "Progress orders ShareFile Storage Zone Controller shutdown over a 'credible external threat' — day three, no patch or root cause disclosed"
headline: "Progress tells all on-prem ShareFile Storage Zone Controller customers to power off their servers over an undisclosed 'credible external security threat'"
summary: >
  Progress Software has ordered every customer running an on-premises ShareFile Storage Zone Controller (SZC) — the internet-facing IIS component bridging ShareFile's cloud to customer-managed storage — to physically shut the hosting server down over "a credible external security threat," first notified 2026-07-10 and still unresolved on the vendor status page as of 2026-07-13. No CVE, root cause, patch or restart timeline has been published; the shutdown-not-patch instruction signals no fix yet exists. Exposure of the component concentrates in the US and Germany, giving Swiss/European on-prem file-exchange operators direct reason to act.
discovered_at: "2026-07-13T12:45:00Z"
event_date: "2026-07-10"
run_id: 2026-07-13T1212Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global, europe, us]
sectors: [public-sector, finance, healthcare, legal-services]
entities: [incident:progress-sharefile-storage-zone-controller-shutdown-2026-07]
techniques: [T1190, T1505.003]
affected_products: ["Progress ShareFile Storage Zone Controller"]
cves:
  - id: CVE-2026-2699
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "ShareFile Storage Zone Controller 5.x below 5.12.4"
    fixed: "5.12.4"
  - id: CVE-2026-2701
    cvss: "9.1"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "ShareFile Storage Zone Controller 5.x below 5.12.4"
    fixed: "5.12.4"
sources:
  - url: "https://status.sharefile.com/"
    publisher: "Progress ShareFile (vendor status page)"
    date: "2026-07-13"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/"
    publisher: "BleepingComputer"
    date: "2026-07-10"
    role: primary
  - url: "https://www.heise.de/en/news/Progress-warns-admins-Deactivate-ShareFile-11362439.html"
    publisher: "heise online"
    date: "2026-07-13"
    role: corroborating
  - url: "https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/"
    publisher: "SecurityWeek"
    date: "2026-07-13"
    role: corroborating
  - url: "https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/"
    publisher: "watchTowr Labs"
    date: "2026-04-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We have reason to believe there is a credible external security threat targeting Progress Software's ShareFile Storage Zone Controllers."
    publisher: "Progress Software (via BleepingComputer)"
  - quote: "Currently, we have no indication of unauthorized access to any Progress ShareFile accounts or data."
    publisher: "Progress Software (via BleepingComputer)"
  - quote: "ShareFile customers with Storage Zone Controllers are not operational at this time."
    publisher: "Progress ShareFile (vendor status page)"
verification: multi-source
sourcing_note: "Hold two facts separately: Progress has confirmed the shutdown order and characterised the threat as 'credible' but has not disclosed its technical nature, and has stated no evidence of unauthorized access to date. The background CVE-2026-2699/2701 pre-auth RCE chain in the same component (watchTowr, patched in 5.12.4) is the plausible working hypothesis but is not confirmed by Progress to be the current threat — treat it as compounding risk, not as attribution."
confidence: medium
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
  - "Shut down internet-facing on-prem ShareFile Storage Zone Controller servers per Progress's active directive and do not restart until Progress confirms scope; separately confirm any SZC 5.x instance is on ≥ 5.12.4 (or migrate to the unaffected 6.x .NET-Core branch) to close the known CVE-2026-2699/2701 pre-auth RCE chain."
  - "On any on-prem SZC host, run a bounded compromise check for the known chain: unexpected .aspx files under the StorageCenter webroot subdirectories (documentum/cifs/sp) and the IIS worker process w3wp.exe spawning cmd.exe or powershell.exe."
migrated_from: null
---

Progress Software has told every customer running an on-premises ShareFile Storage Zone Controller (SZC) — the self-hosted IIS component that lets ShareFile's SaaS front end store files on customer-controlled storage (local filesystem, SMB, SharePoint, S3/Azure) rather than in Progress's cloud — to manually power off the Windows server hosting it, citing "a credible external security threat" first notified to customers on 2026-07-10 ([BleepingComputer, 2026-07-10](https://www.bleepingcomputer.com/news/security/progress-urges-sharefile-customers-to-shut-down-servers-over-credible-threat/)). Three days on, the vendor status page still lists the Storage Zone Controller service as not operational and under investigation ([Progress ShareFile status, 2026-07-13](https://status.sharefile.com/)), and Progress has disclosed neither a CVE, a root cause, nor a patch or safe-restart timeline; the mitigation on offer is a full shutdown rather than an update, with no fix published as of this run ([heise online, 2026-07-13](https://www.heise.de/en/news/Progress-warns-admins-Deactivate-ShareFile-11362439.html); [SecurityWeek, 2026-07-13](https://www.securityweek.com/progress-prompts-sharefile-storage-zone-controller-shutdown-amid-security-concerns/)). heise characterises the shutdown as a precautionary measure during an ongoing investigation. Progress states it has no indication of unauthorized access to any ShareFile account or data so far. Only on-premises SZC deployments are affected; cloud-only ShareFile tenants are not.

This sits on top of a chainable pre-auth RCE that watchTowr Labs disclosed in the same component in April 2026: CVE-2026-2699 (CVSS 9.8) is a CWE-698 execution-after-redirect authentication bypass in `/ConfigService/Admin.aspx`, where `Response.Redirect()` is called with the terminate flag set to false, so the admin page body still renders and executes after the browser is told to redirect to login; CVE-2026-2701 (CVSS 9.1) chains from that access, because the storage-location validation only checks writability, letting an attacker repoint the storage repository at the IIS web root and land an ASPX web shell ([watchTowr Labs, 2026-04-02](https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/)). Both were fixed in Storage Zone Controller 5.12.4 (the 6.x .NET-Core branch was unaffected); watchTowr counted roughly 30,000 internet-facing SZC instances at disclosure. Progress has not said whether the current threat relates to this chain or to a separate issue.

**Defender takeaway.** This is the same on-prem, internet-facing, managed-file-transfer-adjacent architecture class (ShareFile, MOVEit, GoAnywhere, Cleo) that has repeatedly produced mass pre-auth exploitation, and a vendor ordering customers to pull the plug rather than patch is a strong signal to treat any exposed SZC as untrusted until Progress publishes scope. Regardless of whether the July threat proves related to CVE-2026-2699/2701, any instance still on SZC 5.x below 5.12.4 carries a known, PoC-backed pre-auth RCE and should be upgraded or taken offline now. Since Progress has confirmed no mechanism, treat the CWE-698 chain as the working hunt hypothesis.

**Triage:** an authenticated administrator legitimately hits `/ConfigService/Admin.aspx` and receives a normal authenticated session; the anomaly for the known chain is a request to that path that returns a 302 whose response body nonetheless carries the full admin-panel HTML (the execution-after-redirect behaviour) rather than the redirect being honoured, followed by configuration changes to Zone/Primary-Zone-Controller/storage-repository fields outside a change window — and, downstream, an `.aspx` file appearing under a StorageCenter webroot subdirectory that is not part of the vendor's shipped file set.
