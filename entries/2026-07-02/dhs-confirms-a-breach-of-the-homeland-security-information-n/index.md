---
schema: 1
kind: incident
title: DHS confirms a breach of the Homeland Security Information Network (HSIN)
headline: DHS confirms a breach of the Homeland Security Information Network (HSIN)
summary: "DHS confirmed a cyber incident affecting the Homeland Security Information Network — a platform federal, state, local, international and private-sector partners use to exchange sensitive-but-unclassified information and coordinate incident response."
discovered_at: "2026-07-02T04:55:18Z"
event_date: 2026-07-01
run_id: 2026-07-02-6551f8c2
priority: notable
immediate_action: null
tags:
  - data-breach
regions:
  - us
sectors:
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.nextgov.com/cybersecurity/2026/06/hackers-breached-dhs-information-sharing-network-people-familiar-say/414534/"
    publisher: Nextgov/FCW
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/"
    publisher: BleepingComputer
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
migrated_from: briefs/2026-07-02.md
---

DHS confirmed a cyber incident affecting the Homeland Security Information Network — a platform federal, state, local, international and private-sector partners use to exchange sensitive-but-unclassified information and coordinate incident response. Nextgov/FCW first reported (citing two people familiar) that an unknown actor accessed HSIN servers and a SharePoint collaboration system, with the intrusion believed to have occurred between late May and early June 2026 ([Nextgov/FCW, 2026-06-30](https://www.nextgov.com/cybersecurity/2026/06/hackers-breached-dhs-information-sharing-network-people-familiar-say/414534/)). DHS told BleepingComputer it "immediately took action to isolate the affected systems, mitigate the vulnerability, and launch a comprehensive forensic investigation," stated there is "no indication that classified networks were impacted," and that the system remains operational ([BleepingComputer, 2026-07-01](https://www.bleepingcomputer.com/news/security/dhs-confirms-hackers-breached-hsin-info-sharing-platform/)). No initial-access vector, CVE or attribution has been disclosed; whether documents were exfiltrated remains undetermined. HSIN previously suffered a 2023 access-misconfiguration incident that exposed US-person PII.

**Why it matters to us:** no vulnerable component was named, so there is no patch action — but both this event and HSIN's 2023 incident trace to information-sharing / collaboration-platform trust boundaries (SharePoint, cross-org portals) rather than perimeter exploitation. Public-sector SOCs should review who holds standing access to their own cross-agency information-sharing portals and whether access reviews and anomalous-download alerting cover them.
