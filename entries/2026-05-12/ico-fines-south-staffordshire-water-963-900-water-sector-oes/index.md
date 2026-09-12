---
schema: 1
kind: incident
title: "ICO fines South Staffordshire Water £963,900 — water-sector OES with partial SIEM coverage; Cl0p attribution and ZeroLogon kill-chain detail sourced to The Record"
headline: "ICO fines South Staffordshire Water £963,900 — water-sector OES with partial SIEM coverage; Cl0p attribution and ZeroLogon kill-chain detail sourced to The"
summary: "ICO fines South Staffordshire Water £963,900 for the 2020–2022 Cl0p intrusion. Regulator-side findings call out inadequate vulnerability management, unpatched critical systems, obsolete unsupported software (Windows Server 2003) and partial SIEM coverage; 633,887 individuals' data was published on the dark web from a total holding of about 1.85 million customer records (ICO notice, 2026-05-11). Reporting by The Record adds the ZeroLogon / two-DC kill-chain detail"
discovered_at: "2026-05-12T05:00:00Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: high
immediate_action: null
tags:
  - ransomware
  - data-breach
  - law-enforcement
regions:
  - uk
  - europe
sectors:
  - water
  - public-sector
entities:
  - "incident:south-staffordshire-water-ico-2026"
cves: []
sources:
  - url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/"
    publisher: "UK ICO — Fine of nearly £1m issued against South Staffordshire Plc and South Staffordshire Water Plc, 2026-05-11"
    role: primary
  - url: "https://therecord.media/uk-water-company-had-hackers-lurking-for-years"
    publisher: "The Record, 2026-05-11"
    role: corroborating
  - url: "https://www.theregister.com/cyber-crime/2026/05/11/ico-fines-south-staffordshire-963k-over-2022-breach/5237875"
    publisher: "The Register, 2026-05-11"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: "migration: CVE fields incomplete in v2 footer (CVE-2020-1472)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
---

The UK Information Commissioner's Office on [2026-05-11](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/05/fine-of-nearly-1m-issued-against-south-staffordshire-plc-and-south-staffordshire-water-plc/) issued a £963,900 fine against South Staffordshire Plc and its water-supply subsidiary for the 2020–2022 intrusion. The ICO's published findings cite **inadequate vulnerability management**, **unpatched critical systems**, **obsolete unsupported software** (the estate still contained Windows Server 2003, EOL since July 2015), and incomplete SIEM coverage; the regulator does not name a CVE or threat actor in its public notice. The technical kill-chain detail — phishing initial access in September 2020 → [CVE-2020-1472 (ZeroLogon, T1068)](https://attack.mitre.org/techniques/T1068/) against two unpatched domain controllers → domain admin → ~20 months of unimpeded lateral movement → detection in July 2022 when IT performance degraded — comes from [The Record's reporting](https://therecord.media/uk-water-company-had-hackers-lurking-for-years), as does the Cl0p attribution. The ICO press release records that data on **about 1.85 million customers** (approximately 750,000 current and 1.1 million former) was held by the company, of which **633,887 individuals** had data published on the dark web, and that the published dataset totalled **over 4.1 TB** including customer credentials, bank account/sort codes, Priority Services Register data (from which disability status can be inferred) and HR records ([The Register, 2026-05-11](https://www.theregister.com/cyber-crime/2026/05/11/ico-fines-south-staffordshire-963k-over-2022-breach/5237875)). The fine was reduced 40% on the basis of early admission and cooperative engagement; South Staffordshire agreed not to appeal.

**Why it matters to us:** The ICO action is the first significant post-Cyber-Security-and-Resilience-Bill UK regulatory action against a water-sector OES, and the regulator's operational findings transfer verbatim to NIS2 Article 21 technical measures and the German KRITIS-DachG public-administration scope that came into force this spring. Concrete defender takeaway: (a) measure your *actual* SIEM/XDR coverage percentage by hostname inventory rather than by sensor-licence count — partial coverage on a high-value subset is materially worse than uniform sampling; (b) the ZeroLogon pivot reported by The Record is a long-tail patch-management hygiene point on domain controllers any SOC can audit against; (c) detection logic that survives this case maps to Sysmon-class auditing of DC authentication events — `4742` (account changes) and `4769` Kerberos service-ticket anomalies — after vendor disclosure of any DC-impacting CVE.
