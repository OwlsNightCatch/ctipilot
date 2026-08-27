---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "2026-W30 vulnerability status roll-up — five CVEs crossed into confirmed exploitation/KEV, three more carry public exploit code, and a dense CVSS-9-to-10 tail hit edge, ERP, OT and file-transfer"
headline: "W30 vuln trajectory — five CVEs newly exploited/KEV, three carry public exploit code, and a dense CVSS-9-to-10 tail across edge, ERP, file-transfer and OT"
summary: >
  Consolidated status of the vulnerabilities this pipeline covered operationally in ISO week 2026-W30, each with its trajectory this week versus first coverage. Confirmed exploited / newly KEV-listed: CVE-2026-6875 (ServiceNow AI Platform), CVE-2026-50522 (SharePoint Server, machine-key theft), CVE-2026-16232 (Check Point SmartConsole), CVE-2026-0770 (Langflow) and the WordPress "WP2Shell" chain CVE-2026-63030/-60137. Public exploit code or full mechanics but no confirmed in-the-wild abuse: CVE-2026-54121 (Windows AD CS "Certighost", full PoC), CVE-2026-2291 (dnsmasq, working RCE exploit) and CVE-2026-42533 (nginx, discoverer-demonstrated pre-auth RCE, PoC withheld ~21 days). Critical-but-unexploited tail requiring scheduled action: Oracle July CPU Fusion Middleware (nine unauth CVSS-10.0 CVEs, NCSC-NL assessing large-scale abuse "very likely"), SolarWinds Serv-U (16-CVE IDOR-to-root cluster), GLPI 11.0.8/10.0.26 (RCE + MFA bypass), Mitel MiCollab AWV (unauth command injection, CVE pending), Zimbra 10.1.20, the Check Point management siblings CVE-2026-62144/-62145, Langflow CVE-2026-14499, and OT libraries libIEC61850/lib60870 (CVE-2026-49035). Full per-CVE detail lives in the referenced operational entries; this roll-up carries only the week's trajectory.
discovered_at: "2026-07-26T23:45:00Z"
event_date: 2026-07-24
run_id: 2026-07-26T2309Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - poc-public
  - pre-auth
  - rce
  - patch-available
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - finance
  - energy
  - water
  - telco
cves: []
techniques:
  - T1190
  - T1068
  - T1552.004
  - T1136
affected_products: []
sources:
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12778"
    publisher: "NCSC-CH Cyber Security Hub"
    date: "2026-07-20"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/21/cisa-adds-four-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-07-21"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/22/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-07-22"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252"
    publisher: "NCSC-NL"
    date: "2026-07-22"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06"
    publisher: "CISA (ICSA-26-204-06)"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "A consolidating status view; each CVE's exploitation status and versions trace to the referenced operational entry, which carries the primary vendor/CERT source and the verbatim evidence. Statuses are stated as of this weekly's composition date (2026-07-26)."
confidence: high
update_of: null
references:
  - 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
  - 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
  - 2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232
  - 2026-07-22/langflow-cve-2026-0770-exploited-ncsc-nl-15-cve-batch
  - 2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030
  - 2026-07-25/certighost-cve-2026-54121-ad-cs-dc-impersonation-poc
  - 2026-07-21/cve-2026-2291-dnsmasq-heap-overflow-rce-exodus
  - 2026-07-20/cve-2026-42533-nginx-pcre-capture-clobber-preauth-rce
  - 2026-07-26/oracle-july-2026-cpu-fusion-middleware-cvss10-unauth
  - 2026-07-23/solarwinds-serv-u-2026-3-critical-idor-priv-esc-root
  - 2026-07-23/glpi-11-0-8-10-0-26-critical-rce-mfa-bypass
  - 2026-07-24/mitel-micollab-awv-unauth-command-injection
  - 2026-07-22/zimbra-10-1-20-snmp-command-injection-rce-plus-stored-xss
  - 2026-07-24/mz-automation-libiec61850-lib60870-ot-preauth-rce
  - 2026-07-26/gitlab-oj-json-parser-rce-notebook-diff-poc
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Consolidated trajectory of the CVEs this pipeline covered operationally in ISO week 2026-W30. Per-CVE mechanics, affected/fixed versions and primary sources are in the referenced operational entries; this roll-up records only what moved this week.

**Confirmed exploited / newly KEV-listed this week.** ServiceNow AI Platform **CVE-2026-6875** (pre-auth sandbox-escape RCE) was marked actively exploited by NCSC-CH, with activity from 2026-07-18. Microsoft SharePoint Server **CVE-2026-50522** (pre-auth deserialization RCE) went to active exploitation within hours of a public PoC, with machine-key theft giving persistence that survives patching. Check Point SmartConsole **CVE-2026-16232** (auth bypass to full admin) was confirmed exploited against a handful of internet-exposed management servers and added to CISA KEV on 2026-07-22 ([CISA, 2026-07-22](https://www.cisa.gov/news-events/alerts/2026/07/22/cisa-adds-two-known-exploited-vulnerabilities-catalog)). Langflow **CVE-2026-0770** (unauthenticated `exec_globals` RCE) was added to CISA KEV on 2026-07-21 ([CISA, 2026-07-21](https://www.cisa.gov/news-events/alerts/2026/07/21/cisa-adds-four-known-exploited-vulnerabilities-catalog)). The WordPress core "WP2Shell" chain **CVE-2026-63030** (route confusion, pre-auth) with **CVE-2026-60137** (SQL injection) moved from "no confirmed exploitation" to confirmed in-the-wild abuse and KEV-listing. A correction landed the same week: Langflow's July batch is not fully fixed in 1.10.1 — the authenticated command injection **CVE-2026-14499** needs 1.10.2 — so any org that upgraded only to 1.10.1 on the earlier advice remains exposed.

**Public exploit code or full mechanics, no confirmed in-the-wild abuse.** Windows Server AD CS "Certighost" **CVE-2026-54121** (a low-privileged domain user forges a Domain Controller certificate and DCSyncs the krbtgt hash) gained a full public PoC — weaponizable now against any AD CS estate that has not applied the July 2026 cumulative update. Exodus Intelligence published a working heap-overflow-to-RCE chain for dnsmasq **CVE-2026-2291**, materially worse than the DoS impact the NVD score implies and broad across OpenWrt and embedded gateways. And for nginx / NGINX Plus **CVE-2026-42533**, the credited discoverer demonstrated a reliable pre-auth RCE, with the exploit PoC withheld for roughly 21 days — a public-exploit clock, not a current in-the-wild threat.

**Critical-but-unexploited tail requiring scheduled or exposure-driven action.** Oracle's July 2026 Critical Patch Update carries nine distinct CVSS-10.0 unauthenticated flaws in Fusion Middleware (including Oracle Data Integrator CVE-2026-47056 and Coherence CVE-2026-60217), with NCSC-NL assessing that large-scale abuse in the short term is very likely ([NCSC-NL, 2026-07-22](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0252)). SolarWinds Serv-U 2026.3 fixes a 16-CVE IDOR/broken-access-control cluster (15 rated CVSS 9.1) letting an authenticated user escalate to root on the file-transfer host. GLPI 11.0.8 / 10.0.26 fixes a form-import RCE (CVE-2026-48482) and a complete MFA bypass (CVE-2026-52848) in an ITSM platform heavily deployed across French and EU public administration. Mitel MiCollab AWV has an unauthenticated command-injection flaw (CVSS 9.8, internal id MTLVULN-1694, CVE pending). Zimbra 10.1.20 fixed an SNMP command-injection RCE plus stored-XSS bugs. The Check Point management siblings **CVE-2026-62144** (CVSS 10.0 unauth RCE) and **CVE-2026-62145** (Gaia root escalation) sit on the same surface as the actively-attacked auth bypass. OT protocol libraries libIEC61850/lib60870 carry an unauthenticated heap-overflow RCE (**CVE-2026-49035**) embedded in IEC 61850 / IEC 60870-5-104 substation and SCADA gear. And a GitLab CE/EE RCE via the Jupyter-notebook diff renderer (two ~5-year-old Oj Ruby-parser bugs) shipped a silent, un-CVE'd dependency bump in the 10 June releases, leaving feed-gated operators exposed for 44 days before the public PoC.

The webmail-espionage CVEs of the week — Zimbra CVE-2025-66376 and SOGo CVE-2026-8496 — are treated in this week's state-nexus webmail top-story rather than repeated here.
