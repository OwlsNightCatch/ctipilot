---
schema: 1
kind: vulnerability
horizon: operational
title: "July Patch Tuesday follow-through: a SharePoint pre-auth JWT bypass from a Pwn2Own chain (CVE-2026-55040) and a pre-auth Dynamics 365 RCE Microsoft expects to be exploited (CVE-2026-55944)"
headline: "Beyond the two exploited zero-days, July's Microsoft set hides a Pwn2Own SharePoint auth-bypass and a pre-auth Dynamics 365 RCE rated Exploitation More Likely"
summary: >
  An update to the 2026-07-14 Patch Tuesday coverage: three further SharePoint fixes and a Dynamics fix in the
  same cycle carry pre-auth risk. CVE-2026-55040 (CVSS 9.1) is a SharePoint JWT authentication bypass from
  Rapid7's Pwn2Own Berlin chain — an unauthenticated attacker who knows a target's AD SID or UPN can act as
  that user or administrator; Rapid7 demonstrated the chain at Pwn2Own and is holding full technical details and
  the PoC under a 30-day disclosure embargo, and the chained RCE half will not be patched until August, so
  applying the July fix now is the only break in the chain. CVE-2026-55944 (CVSS 9.8) is an unauthenticated
  deserialization RCE in Dynamics NAV / Dynamics 365 Business Central (on-prem) that Microsoft rates
  "Exploitation More Likely." Two SharePoint deserialization RCEs (CVE-2026-50522, CVE-2026-58644, both CVSS 9.8)
  round out the set. None is confirmed exploited in the wild yet.
discovered_at: "2026-07-15T04:36:00Z"
event_date: "2026-07-14"
run_id: 2026-07-15T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, patch-available]
regions: [global]
sectors: [public-sector, finance]
entities: []
techniques: [T1190, T1606]
affected_products: ["Microsoft SharePoint Server Subscription Edition", "Microsoft SharePoint Server 2019", "Microsoft SharePoint Server 2016", "Microsoft Dynamics NAV", "Microsoft Dynamics 365 Business Central (On-Premises)"]
cves:
  - id: CVE-2026-55040
    cvss: "9.1"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "SharePoint Server Subscription Edition, 2019, 2016"
    fixed: "July 2026 SharePoint security update"
  - id: CVE-2026-55944
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Dynamics NAV / Dynamics 365 Business Central (On-Premises)"
    fixed: "July 2026 security update"
  - id: CVE-2026-50522
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "SharePoint Server Subscription Edition, 2019, 2016"
    fixed: "July 2026 cumulative update"
  - id: CVE-2026-58644
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [patch-available]
    affected: "SharePoint Server Subscription Edition, 2019, 2016"
    fixed: "June 2026 cumulative update (patch shipped in June; CVE documented 2026-07-14 after being omitted from the June release notes)"
sources:
  - url: "https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed"
    publisher: "Rapid7 Labs (Stephen Fewer)"
    date: "2026-07-14"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-55944"
    publisher: "Microsoft MSRC"
    date: "2026-07-14"
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-50522"
    publisher: "Microsoft MSRC"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Patching CVE-2026-55040 will successfully break this exploit chain; this underscores the importance of patching vulnerabilities such as authentication bypasses, which can break complex and high-impact exploit chains."
    publisher: "Rapid7 Labs"
  - quote: "Deserialization of untrusted data in Microsoft Dynamics NAV allows an unauthorized attacker to execute code over a network."
    publisher: "Microsoft MSRC"
verification: multi-source
sourcing_note: "CVE ids, CVSS v3.1 scores and exploitability ratings were transcribed per-CVE from the Microsoft MSRC Security Update Guide OData records; CVE-2026-55040's mechanism, its 30-day PoC/technical-detail embargo and the August RCE-patch timing are from Rapid7's own disclosure — no public PoC exists at composition. CVE-2026-55944 is confirmed pre-auth by its MSRC vector (AV:N/AC:L/PR:N/UI:N). CVE-2026-50522 and CVE-2026-58644 carry a base CVSS vector of PR:N, but Microsoft's per-CVE FAQ describes exploitation by an attacker authenticated as at least a SharePoint Site Owner — recorded here as post-auth on that FAQ basis; the discrepancy is noted for any team relying on the vector alone. CVE-2026-58644's MSRC revision history states the patch shipped with the June 2026 cumulative update and the CVE was inadvertently omitted from June's release notes, hence its fixed field references June, not July."
confidence: high
update_of: 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Confirm the July 2026 SharePoint security update is applied to every on-prem SharePoint Server (Subscription Edition, 2019, 2016) — it closes CVE-2026-55040 and breaks Rapid7's Pwn2Own chain even though the chained RCE stays unpatched until August."
  - "Inventory internet-reachable Dynamics NAV / Dynamics 365 Business Central (on-prem) instances and apply the July 2026 update; the deserialization RCE (CVE-2026-55944) fires pre-auth on the login path, so no authentication-based mitigation exists."
migrated_from: null
---

**UPDATE (originally covered 2026-07-14):** the July Patch Tuesday entry covered the two KEV-listed exploited zero-days (AD FS CVE-2026-56155, SharePoint CVE-2026-56164). Four further high-severity fixes in the same cycle carry pre-auth risk and warrant separate attention. **CVE-2026-55040** (CVSS 9.1, weak authentication) is a SharePoint JWT token-validation bypass that Rapid7's Stephen Fewer built into a two-vulnerability chain for Pwn2Own Berlin 2026: a remote unauthenticated attacker who knows a target's Active Directory SID or User Principal Name can forge identity and operate as that SharePoint user or administrator ([Rapid7 Labs, 2026-07-14](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed)). Rapid7 chained it to a still-undisclosed RCE that Microsoft will not patch until the August 2026 cycle — but "patching CVE-2026-55040 will successfully break this exploit chain," so the July update is the available defense today even with the RCE half outstanding ([Rapid7 Labs, 2026-07-14](https://www.rapid7.com/blog/post/ve-cve-2026-55040-microsoft-sharepoint-jwt-token-authentication-bypass-fixed)).

**CVE-2026-55944** (CVSS 9.8) is an unauthenticated deserialization RCE in **Microsoft Dynamics NAV / Dynamics 365 Business Central (on-premises)** — "deserialization of untrusted data ... allows an unauthorized attacker to execute code over a network," triggered by a crafted login request before any session exists (vector AV:N/AC:L/PR:N/UI:N), and rated "Exploitation More Likely" ([Microsoft MSRC, 2026-07-14](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-55944)). It is easy to overlook against SharePoint or Exchange in a busy Patch Tuesday, yet on-prem Dynamics back-office instances are frequently exposed. Two more SharePoint deserialization RCEs — **CVE-2026-50522** and **CVE-2026-58644** (both CVSS 9.8, "Exploitation More Likely") — require Site-Owner-level access per Microsoft's FAQ; CVE-2026-50522 is fixed in the July cumulative update, while CVE-2026-58644's patch actually shipped in the June cumulative update and the CVE was only documented on 14 July after being omitted from June's release notes — so a SharePoint estate patched through June is already covered for 58644 ([Microsoft MSRC, 2026-07-14](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-50522)).

**Defender takeaway:** the JWT-bypass path is invisible to normal sign-in and Conditional-Access telemetry because no credential is presented — hunt SharePoint web-server access logs for requests bearing anomalous JWT bearer tokens referencing SIDs/UPNs that do not match the session's authenticated principal, and audit-log operations performed "as" a user with no corresponding interactive or API sign-in in the same window. For the deserialization RCEs, the durable signal is the classic .NET deserialization-to-RCE lineage — anomalous `w3wp.exe` (SharePoint app-pool) or the Dynamics service host spawning child processes following list/webpart operations or an inbound login request. **Triage:** legitimate SharePoint operations are tied to a preceding authenticated sign-in for the acting principal; an operation attributed to a user or administrator with no matching sign-in event, or a service-account process spawn outside normal batch/report windows, is the discriminator.
