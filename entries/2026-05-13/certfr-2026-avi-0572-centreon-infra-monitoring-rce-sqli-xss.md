---
schema: 1
kind: vulnerability
horizon: operational
title: "CERTFR-2026-AVI-0572 — Centreon Infra Monitoring: RCE / SQLi / XSS cluster (April 2026 bulletin)"
headline: "CERTFR-2026-AVI-0572 — Centreon Infra Monitoring: RCE / SQLi / XSS cluster (April 2026 bulletin)"
summary: "CERT-FR's CERTFR-2026-AVI-0572 (2026-05-12) consolidates the April 2026 monthly security bulletin for Centreon Infra Monitoring — the enterprise monitoring platform widely deployed in French and EU public-sector NOCs and government ISPs (CERT-FR CERTFR-2026-AVI-0572, 2026-05-12; Centreon security bulletin, 2026-05-12)."
discovered_at: "2026-05-13T05:00:07Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - patch-available
regions:
  - europe
sectors:
  - public-sector
entities:
  - "campaign:certfr-2026-avi-0572"
  - "incident:ncsc-ch-booking-hotel-phishing-2026"
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/"
    publisher: "CERT-FR CERTFR-2026-AVI-0572, 2026-05-12"
    role: primary
  - url: "https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660"
    publisher: "Centreon security bulletin, 2026-05-12"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
---

CERT-FR's CERTFR-2026-AVI-0572 (2026-05-12) consolidates the April 2026 monthly security bulletin for Centreon Infra Monitoring — the enterprise monitoring platform widely deployed in French and EU public-sector NOCs and government ISPs ([CERT-FR CERTFR-2026-AVI-0572, 2026-05-12](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0572/); [Centreon security bulletin, 2026-05-12](https://thewatch.centreon.com/latest-security-bulletins-64/april-2026-monthly-security-bulletin-for-centreon-infra-monitoring-high-5660)). The bulletin lists command injection (effectively RCE in Centreon MBI), SQL injection, and XSS (Centreon Map, CVSS 6.8) findings spread across Centreon Anomaly Detection, Auto Discovery, AWIE, BAM, DSM, License Manager, MAP, MBI and Open Tickets — affecting 24.04.x (MBI only), 24.10.x and 25.10.x branches. Per-CVE identifiers are enumerated in the Centreon bulletin rather than the CERT-FR advisory. No ITW reported. The defender-relevant property is that Centreon stores **privileged monitored-host credentials** (SNMP communities, SSH private keys, vendor-API tokens) — compromise of a Centreon instance is a high-impact lateral-movement enabler against the entire monitored estate. Detection concepts: monitor Centreon front-end access logs for the listed component endpoints from non-NOC source networks; alert on Centreon process spawning child shells outside scheduled poller intervals. Hardening: apply the April 2026 monthly update; segment Centreon's monitoring VLAN from user / internet networks; treat Centreon credentials-vault contents as Tier-0 in the AD admin-tiering model.


#### CVE Summary Table

| CVE | Product | CVSS | EPSS | KEV | Exploited | Patch | Source |
|---|---|---|---|---|---|---|---|
| CVE-2026-44277 | Fortinet FortiAuthenticator 6.5.x / 6.6.x / 8.0.x | 9.1 | n/a | No | No | 6.5.7 / 6.6.9 / 8.0.3 | [PSIRT](https://fortiguard.fortinet.com/psirt/FG-IR-26-128) |
| CVE-2026-26083 | Fortinet FortiSandbox 4.4.x / 5.0.x / PaaS / Cloud | 9.1 | n/a | No | No | 4.4.9 / 5.0.2 / Cloud 5.0.6; Cloud 23/24 migrate | [PSIRT](https://fortiguard.fortinet.com/psirt/FG-IR-26-136) |
| CVE-2026-45185 | Exim 4.97–4.99.2 (GnuTLS builds) | 9.8 | 0.0 | No | No | Exim 4.99.3 | [XBOW](https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim) |
| CVE-2026-41089 | Windows Netlogon (all supported Windows Server) | 9.8 | n/a | No | No | May 2026 CU | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-41096 | Windows DNS Client (`dnsapi.dll`) | 9.8 | n/a | No | No | May 2026 CU | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-41103 | Microsoft SSO Plugin for Jira/Confluence | 9.1 | n/a | No | No (More Likely) | Plugin update 2026-05-12 | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-42898 | Microsoft Dynamics 365 On-Premises | 9.9 | n/a | No | No | May 2026 CU | [ZDI](https://www.thezdi.com/blog/2026/5/12/the-may-2026-security-update-review) |
| CVE-2026-40361 | Microsoft Word (Preview Pane) | 8.4 | n/a | No | No (More Likely) | Office 2026-05-12 | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-40364 | Microsoft Word (Preview Pane) | 8.4 | n/a | No | No (More Likely) | Office 2026-05-12 | [Tenable](https://www.tenable.com/blog/microsofts-may-2026-patch-tuesday-addresses-118-cves-cve-2026-41103) |
| CVE-2026-34263 | SAP Commerce Cloud HY_COM 2205 / COM_CLOUD 2211 | 9.6 | n/a | No | No | SAP Note 3733064 | [Onapsis](https://onapsis.com/blog/sap-security-patch-day-may-2026/) |
| CVE-2026-34260 | SAP S/4HANA SAP_BASIS 751–758 / 816 | 9.6 | n/a | No | No | SAP Note (May 2026 patch day) | [Onapsis](https://onapsis.com/blog/sap-security-patch-day-may-2026/) |

Vendor PSIRT pages (re-fetched at verification time) consistently publish CVSS 9.1 for both FortiAuthenticator CVE-2026-44277 and FortiSandbox CVE-2026-26083; early NCSC-CH / NVD reports cited 9.8 for one or both before convergence. § 7 documents the source discrepancy.
