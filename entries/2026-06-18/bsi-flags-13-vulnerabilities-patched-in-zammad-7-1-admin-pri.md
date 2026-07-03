---
schema: 1
kind: vulnerability
horizon: operational
title: BSI flags 13 vulnerabilities patched in Zammad 7.1 — admin privilege escalation in a DACH public-sector helpdesk platform
headline: BSI flags 13 vulnerabilities patched in Zammad 7.1 — admin privilege escalation in a DACH public-sector helpdesk platform
summary: "BSI CERT-Bund advisory WID-SEC-2026-1981 (2026-06-17) rates the aggregate severity of the Zammad 7.1 release as \"hoch\" (high): an attacker can chain the patched flaws to gain administrator privileges, bypass security controls, manipulate or disclose data, or trigger denial-of-service (BSI CERT-Bund, 2026-06-17)."
discovered_at: "2026-06-18T05:10:33Z"
event_date: 2026-06-17
run_id: 2026-06-18-aa7ee817
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - priv-esc
  - auth-bypass
  - info-disclosure
  - patch-available
regions:
  - dach
  - europe
sectors:
  - public-sector
entities:
  - "trend:zammad-7-1-security-release"
cves: []
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1981"
    publisher: BSI CERT-Bund WID-SEC-2026-1981
    role: primary
  - url: "https://zammad.com/en/product/releases/zammad-7-1"
    publisher: Zammad 7.1 release
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
migrated_from: briefs/2026-06-18.md
---

BSI CERT-Bund advisory WID-SEC-2026-1981 (2026-06-17) rates the aggregate severity of the Zammad 7.1 release as "hoch" (high): an attacker can chain the patched flaws to gain administrator privileges, bypass security controls, manipulate or disclose data, or trigger denial-of-service ([BSI CERT-Bund, 2026-06-17](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1981)). Zammad — a widely-deployed open-source helpdesk/ticketing system common in German, Austrian and Swiss public-sector IT service desks — released version 7.1 on 2026-06-16 addressing 13 issues now tracked exclusively as GitHub Security Advisories ([Zammad, 2026-06-16](https://zammad.com/en/product/releases/zammad-7-1)); individual CVE identifiers are not yet enumerated in public NVD/CSAF records. Any admin-privilege path in a ticketing system exposes internal IT operations data and staff credentials; internet-exposed instances behind a reverse proxy are highest risk. Upgrade to 7.1 and hunt Zammad audit logs for unexpected role escalations and admin-API calls (e.g. to role/user-management endpoints) from unprivileged sessions.


#### CVE Summary Table

| CVE | Product | CVSS | EPSS | KEV | Exploited | Patch | Source |
|---|---|---|---|---|---|---|---|
| CVE-2026-46978 | Oracle Solaris 11.4 — Remote Administration Daemon | 10.0 | n/a | No | Not reported | June 2026 Solaris SRU | [Oracle](https://www.oracle.com/security-alerts/cspujun2026.html) |
| CVE-2026-35278 | Oracle PeopleSoft PeopleTools 8.61 / 8.62 — Performance Monitor | 9.8 | n/a | No | Not reported | June 2026 CSPU | [Oracle](https://www.oracle.com/security-alerts/cspujun2026.html) |
| CVE-2026-0647 | Rockwell 1794-AENTR / 1794-AENTRXT FLEX I/O (≤ V2.012) | 9.4 | n/a | No | Not reported | Firmware 2.013 (SD1775) | [CISA ICS-CERT](https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-05) |
| CVE-2026-11317 | Rockwell CompactLogix / ControlLogix 5370 / 5570 | 7.5 | n/a | No | Not reported | SD1772 firmware | [CISA ICS-CERT](https://www.cisa.gov/news-events/ics-advisories/icsa-26-167-03) |
