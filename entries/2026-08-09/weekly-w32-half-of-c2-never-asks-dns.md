---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Nearly half of malware command-and-control never asks DNS a question — Unit 42 measured it across four million analysis reports, which puts a number on the blind spot in every protective-DNS and DNS-firewall deployment"
headline: "45% of C2-active malware dials a hard-coded IP with no prior name resolution — DNS-layer controls cannot see it"
summary: >
  Unit 42 analysed more than four million dynamic-analysis reports and found that 45.32% of malware samples
  showing any command-and-control activity made at least one direct-to-IP connection with no preceding DNS
  query, and that such traffic accounts for 23.17% of all C2 connection attempts. Only 1% of benign samples
  establish comparable connections to untrusted IP addresses. For the many European public-sector networks
  whose egress control is built on protective DNS, DNS firewalling, response-policy zones or sinkholing,
  the measurement identifies a structural gap rather than a tuning problem — and supplies the hunt that
  closes it: an outbound session to an external address with no prior name resolution from the same host.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-04"
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags: [botnet, infostealer, ransomware, cloud]
regions: [global, europe]
sectors: [public-sector, technology]
entities: []
techniques: [T1071, T1095, T1571]
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/malware-bypass-dns-direct-to-ip/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-04"
    role: primary
closed_sources: []
evidence:
  - quote: "Our analysis of 4 million dynamic analysis reports indicates that almost half (45.32%) of malware samples with any command-and-control (C2) activity made at least one direct-to-IP (D2IP) address connection. Measured as a fraction of all C2 connection attempts, D2IP traffic accounts for 23.17% of the total."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "Only 1% of benign samples establish connections to untrusted IP addresses after applying the same filtering criteria."
    publisher: "Palo Alto Networks Unit 42"
verification: single-source
sourcing_note: >
  Single-source: the measurement rests entirely on one vendor's sandbox population and on its own labelling
  of what constitutes malware C2, and no independent party has reproduced the proportions. The figures are
  reported as that vendor's telemetry rather than as an industry rate, and the defensive conclusion drawn
  here does not depend on the exact percentage.
confidence: medium
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

Protective DNS is one of the few controls a national or sector-level defender can deploy centrally and cheaply, which is why several European public-sector networks run one and why DNS response-policy zones, sinkholing and DNS firewalling sit at the front of many egress-control designs. Unit 42 published a measurement this week that bounds what that class of control can and cannot see, and the number is large enough to change how a SOC reads a clean DNS log.

Across more than four million dynamic-analysis reports, Unit 42 reports that "almost half (45.32%) of malware samples with any command-and-control (C2) activity made at least one direct-to-IP (D2IP) address connection," and that "measured as a fraction of all C2 connection attempts, D2IP traffic accounts for 23.17% of the total" ([Palo Alto Networks Unit 42, 2026-08-04](https://unit42.paloaltonetworks.com/malware-bypass-dns-direct-to-ip/)). The malware in question does not evade DNS monitoring by encrypting its queries or by using an unusual resolver — it simply never resolves a name, because the address is compiled in. Unit 42 attributes the behaviour across a wide span of threat classes including ransomware droppers, peer-to-peer botnets and supply-chain implants, so this is not one family's quirk.

The comparison figure is what makes it a usable detection rather than an interesting statistic: applying the same filtering, "only 1% of benign samples establish connections to untrusted IP addresses," and those that do average fewer than two such connections apiece. A behaviour present in nearly half of C2-active malware and in one percent of benign software is a discriminator, not noise. Unit 42's own proposal is a firewall-level enforcement model that verifies an outbound connection was sanctioned by a preceding DNS response, but the transferable version needs no product: correlate egress flow records against the same host's DNS telemetry and surface sessions to external addresses that no resolution preceded.

**Defender takeaway:** a quiet protective-DNS log is not evidence of a quiet network, and any control narrative that treats DNS filtering as the egress choke point has a gap this measurement sizes. Two things follow. First, confirm that egress flow or firewall logs are actually collected and retained alongside DNS logs — the hunt below is impossible without both, and in many estates the DNS logs are centralised while the flow logs are not. Second, where full correlation is not yet feasible, the cheaper interim is a default-deny egress policy for server segments and for any host class that has no business initiating arbitrary outbound sessions, which removes the technique's precondition rather than detecting it.

**Triage:** the hunt is an outbound TCP or UDP session from an internal host to an external, non-allowlisted address with no A or AAAA resolution for that address in the same host's DNS telemetry within a preceding window. The benign population that shares this shape is real and needs excluding first: time synchronisation, hard-coded public resolvers, some update and telemetry agents, content-delivery and cloud back-ends reached by IP after an earlier resolution, and peer-to-peer or real-time media protocols that negotiate addresses out of band. After those exclusions the discriminators are destination reputation, port, persistence of the beacon, and — most usefully — whether the initiating process normally resolves names at all: a browser or mail client that suddenly contacts a bare address is anomalous in a way that an NTP daemon is not.
