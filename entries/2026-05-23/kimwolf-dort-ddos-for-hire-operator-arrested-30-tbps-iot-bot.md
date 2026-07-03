---
schema: 1
kind: threat
horizon: operational
title: "Kimwolf / \"Dort\" DDoS-for-hire operator arrested — 30+ Tbps IoT botnet, U.S. DoD-range targeting, AISURU variant"
headline: "Kimwolf / \"Dort\" DDoS-for-hire operator arrested — 30+ Tbps IoT botnet, U.S. DoD-range targeting, AISURU variant"
summary: "Kimwolf / \"Dort\" arrested in Ottawa — 30+ Tbps DDoS-for-hire infrastructure. Jacob Butler, 23, charged in U.S. and Canada for operating the AISURU-variant Kimwolf botnet; >25,000 attack commands including against DoD IP space; coordinated C2 takedown March 2026 dismantled Kimwolf alongside AISURU/JackSkid/Mossad (KrebsOnSecurity, 2026-05-22)."
discovered_at: "2026-05-23T05:00:01Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: high
immediate_action: null
tags:
  - law-enforcement
  - botnet
  - ddos
  - organized-crime
regions:
  - global
  - us
sectors:
  - defense
  - telco
  - public-sector
entities: []
cves: []
sources:
  - url: "https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos"
    publisher: U.S. Department of Justice press release
    role: primary
  - url: "https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada/"
    publisher: KrebsOnSecurity
    role: corroborating
  - url: "https://therecord.media/canadian-man-arrested-charged-running-kimwolf-botnet"
    publisher: The Record
    role: corroborating
  - url: "https://thehackernews.com/2026/05/kimwolf-ddos-botnet-operator-arrested.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-05-23.md
---

Canadian authorities (Ontario Provincial Police) arrested Jacob Butler, 23, of Ottawa — alias **Dort** — earlier this week on a U.S. extradition warrant; the U.S. Department of Justice unsealed the criminal complaint in the District of Alaska on **Thursday 2026-05-21** ([U.S. Department of Justice, 2026-05-21](https://www.justice.gov/usao-ak/pr/canadian-man-arrested-international-authorities-charged-administrating-kimwolf-ddos) · [KrebsOnSecurity, 2026-05-22](https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada/) · [The Record, 2026-05-22](https://therecord.media/canadian-man-arrested-charged-running-kimwolf-botnet)). Butler is alleged to have developed and operated **Kimwolf**, a DDoS-for-hire botnet assessed as a variant of AISURU. Kimwolf infected primarily consumer IoT — digital photo frames, webcams and other internet-exposed devices — via default credentials and known public CVEs, issued more than 25,000 DDoS attack commands, and peaked at **nearly 30 Tbps** per the DOJ and KrebsOnSecurity (The Hacker News reports the peak as 31.4 Tbps — the discrepancy is between the DOJ-cited figure used in the unsealed complaint and a secondary number cited by THN; treat the DOJ number as the reference for capacity-planning purposes). Targets included U.S. Department of Defense IP ranges and at least one victim with confirmed losses exceeding $1 million per incident. Kimwolf C2 infrastructure was seized 2026-03-19 in a coordinated multi-jurisdiction action alongside three sibling botnets — AISURU, JackSkid and Mossad — collectively infecting >3 million devices.

The complaint also documents that Butler conducted DDoS, doxing and swatting attacks against researchers who investigated him, including Synthient's Ben Brundage who had helped identify a Kimwolf-exploited vulnerability. Defender takeaway for Swiss and EU operators: the 30 Tbps capability is now demonstrably in range of a single operator's commercial service, and DDoS-for-hire infrastructure reorganises within weeks of takedowns. Re-baseline ISP scrubbing SLAs against a 10–30 Tbps reference, audit citizen-facing portals' application-layer rate limits, and segment consumer-grade IoT (frames, cameras, NVRs) off any path that touches critical infrastructure or admin networks.

**Why it matters to us:** Kimwolf belongs to the IoT-amplification class of botnets that target Swiss/EU public-sector portals; the arrest is an opportunity to re-test scrubbing capacity and IoT segmentation, not to assume the supply has shrunk.
