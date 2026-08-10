---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — the water-campaign exposure gets counted: 4,407 internet-facing Rockwell controllers, and 19 of the 22 in already-attacked cities sat on the same mobile carrier network"
headline: "Forescout puts numbers on the exposed estate, and CISA says the devices it finds have no password or a default one"
summary: >
  Forescout queried Shodan on 2026-08-03 and found 4,407 devices exposing the EtherNet/IP engineering
  port used by Rockwell Automation controllers, 65% in the United States with Canada and Spain next.
  Of the 22 it located in cities targeted by the water-utility campaign, 19 were on the same mobile
  carrier network reached through cellular routers, and 19 of 22 ran firmware susceptible to
  CVE-2017-16740 — two separate findings that share a number. Forescout cannot confirm any of those
  assets were compromised and states no CVE is confirmed as exploited in the campaign. CISA's acting
  director, interviewed at Black Hat, says exposed controllers are being found with no password or a
  default one, and that the agency is doing nothing on attribution right now.
discovered_at: "2026-08-10T04:56:00Z"
event_date: "2026-08-05"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [ot-ics, default-config, info-disclosure]
regions: [us, europe, global]
sectors: [water, energy, public-sector]
entities: [incident:minnesota-water-utilities-coordinated-cyberattack-2026-07]
techniques: [T1078.001]
affected_products: ["Rockwell Automation Allen-Bradley MicroLogix 1400", "Rockwell Automation Allen-Bradley MicroLogix 1100"]
cves: []
sources:
  - url: "https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/"
    publisher: "Forescout"
    date: "2026-08-05"
    role: primary
  - url: "https://www.nextgov.com/cybersecurity/2026/08/cisa-still-finds-water-system-controls-exposed-online-amid-multistate-hacks/415266/"
    publisher: "Nextgov/FCW"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "Querying the Shodan search engine on August 3, 2026 returns 4,407 devices exposing port 44818."
    publisher: "Forescout"
  - quote: "Although we cannot confirm these particular assets were compromised in this campaign, they had some interesting characteristics"
    publisher: "Forescout"
  - quote: "19 of the 22 hosts (86%) were on the same mobile carrier network, connected via cellular routers"
    publisher: "Forescout"
  - quote: "Exposing EtherNet/IP to the internet creates an unauthenticated path that, depending on device configuration, can allow attackers to obtain information about exposed assets or even write configurations on them."
    publisher: "Forescout"
  - quote: "We're seeing things like [programmable logic controllers] that are open and accessible on the internet with either no password set or default password set"
    publisher: "Nextgov/FCW"
  - quote: "For us, we're not doing anything with attribution right now"
    publisher: "Nextgov/FCW"
verification: multi-source
sourcing_note: >
  Both primaries were fetched directly for this entry rather than relayed through secondary
  reporting, so the figures are attributed to the parties that produced them. Two distinct findings
  in the source share the ratio 19 of 22 — carrier connectivity and firmware susceptibility — and are
  kept separate here rather than merged. Credibility is 2, not 1: the two primaries carry disjoint
  facts and corroborate nothing of each other's — the census figures rest solely on Forescout and the
  quotes solely on the interviewing outlet. CVE-2017-16740 is reported as a firmware-currency signal on
  already-exposed devices, which is Forescout's own framing; it is explicitly not claimed as the
  campaign's exploited vector, and no cves[] record is asserted for it because no source states an
  exploitation or remediation status for it in this context.
confidence: high
update_of: 2026-08-06/water-plc-lockouts-twelve-states-named-utility-confirms
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

**UPDATE (originally covered 2026-08-06):** the water-sector controller-lockout campaign has been tracked here through its growth to at least twelve US states and the FBI's naming of the targeted controller families. What was missing was a measurement of the exposed estate. Forescout has now published one ([Forescout, 2026-08-05](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)).

"Querying the Shodan search engine on August 3, 2026 returns 4,407 devices exposing port 44818" — the EtherNet/IP engineering protocol used by the Rockwell Automation and Allen-Bradley families the joint federal advisory named. "The vast majority (65%) are located in the U.S., followed by Canada (12%) and Spain (3%)." Forescout also notes the exposed population has fallen substantially from its 2020 peak, so the trend is downward even as the absolute number stays material.

The finding worth carrying into a European estate is not the headline count but what Forescout found inside it. Of the devices located in cities the campaign targeted, "Although we cannot confirm these particular assets were compromised in this campaign, they had some interesting characteristics" — and the first of those is that "19 of the 22 hosts (86%) were on the same mobile carrier network, connected via cellular routers." That is a connectivity path, not an IT-network path: controllers reachable through a mobile carrier do not appear in a scan of an organisation's own address space, do not sit behind its perimeter, and are frequently owned operationally by an integrator rather than by the utility. Separately, and confusingly sharing the same ratio, "Approximately 86% (19 of 22) hosts observed in the affected cities were susceptible to this CVE based on firmware versions" — referring to CVE-2017-16740, which Forescout names but does not describe further. These are two different observations about the same 22 devices and should not be read as one.

Forescout is careful about what that CVE means here, and the care is worth preserving: "Exploitation would require Modbus TCP to be enabled, which was not confirmed", and "There is no confirmation of any CVE exploited in this campaign". The vulnerability is a patch-currency signal on devices that were already exposed and already targeted — the point being that controllers left on the public internet in attacked cities were also running eight-year-old firmware. The exposure itself needs no vulnerability at all: "Exposing EtherNet/IP to the internet creates an unauthenticated path that, depending on device configuration, can allow attackers to obtain information about exposed assets or even write configurations on them."

CISA's acting director, interviewed on the sidelines of Black Hat, described what the agency keeps finding: "We're seeing things like [programmable logic controllers] that are open and accessible on the internet with either no password set or default password set" ([Nextgov/FCW, 2026-08-06](https://www.nextgov.com/cybersecurity/2026/08/cisa-still-finds-water-system-controls-exposed-online-amid-multistate-hacks/415266/)). Asked about attribution he was equally direct — "For us, we're not doing anything with attribution right now" — with the agency's focus on assisting affected operators instead.

**Defender takeaway:** the transferable finding for European water, energy and transport operators is the carrier path, not the American device count. An asset inventory built by scanning the organisation's own ranges will not see a controller that reaches the internet through a cellular router on an operator's network, which is precisely where most of the exposed devices in attacked cities turned out to sit — and this pipeline has already recorded a European OT intrusion that ran through a mobile carrier's private network. Enumerate OT assets by their connectivity contract as well as by IP range: ask which controllers have a SIM, who pays for it, and what that link can reach. The firmware-currency observation is the secondary lesson — devices that nobody can reach to attack are also devices nobody has reached to patch.
