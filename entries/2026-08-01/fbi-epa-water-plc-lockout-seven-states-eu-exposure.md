---
schema: 1
kind: threat
horizon: operational
title: "Water-utility PLC lockouts spread to seven US states — FBI names the targeted controllers, and a Censys scan puts 86% of exposed Siemens S7-1200 units in four European countries"
headline: "FBI, EPA and CISA confirm water-sector PLC attacks across seven states, name the targeted Allen-Bradley controllers, and record modified ladder logic"
summary: >
  The FBI and EPA issued a joint Public Service Announcement on 2026-07-30, with a parallel CISA alert the same day,
  confirming that water and wastewater utilities in at least seven US states have reported PLC lockout incidents since
  2026-07-27 and naming Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 controllers as the targeted
  hardware. Attackers reaching internet-facing devices changed their IP addresses and set passwords, producing loss of
  view and in some cases loss of control; one organisation found modified PLC project files. A Censys scan dated
  2026-07-30 puts 4,117 Siemens SIMATIC S7-1200 units on the public internet with 86% of them in Greece, Spain, Italy
  and Austria, each concentration dominated by that country's leading mobile carrier.
discovered_at: "2026-08-01T04:31:06Z"
event_date: "2026-07-30"
run_id: 2026-08-01T0409Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited, default-config]
regions: [us, europe, global]
sectors: [water, energy, public-sector]
entities: [incident:minnesota-water-utilities-coordinated-cyberattack-2026-07]
techniques: [T1133, T1078.001, T1531, T1565.001]
affected_products: ["Rockwell Automation Allen-Bradley MicroLogix 1100", "Rockwell Automation Allen-Bradley MicroLogix 1400", "Siemens SIMATIC S7-1200"]
cves: []
sources:
  - url: "https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions"
    publisher: "FBI and EPA (joint Public Service Announcement)"
    date: "2026-07-30"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs"
    publisher: "CISA (with EPA and FBI)"
    date: "2026-07-30"
    role: primary
  - url: "https://censys.com/blog/cisa-alert-water-tower-plc-targeting/"
    publisher: "Censys Research"
    date: "2026-07-30"
    role: corroborating
  - url: "https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/"
    publisher: "SecurityWeek / Associated Press"
    date: "2026-07-31"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/"
    publisher: "BleepingComputer"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations."
    publisher: "FBI and EPA (joint Public Service Announcement)"
  - quote: "After remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality."
    publisher: "FBI and EPA (joint Public Service Announcement)"
  - quote: "At least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites."
    publisher: "FBI and EPA (joint Public Service Announcement)"
  - quote: "Threat actors targeting exposed PLCs have modified passwords to lock out operators and disconnected the PLCs by changing their IP addresses. This activity has resulted in boil water notices and sustained manual operations."
    publisher: "CISA (with EPA and FBI)"
  - quote: "Censys ARC identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200. Exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers."
    publisher: "Censys Research"
verification: multi-source
sourcing_note: >
  The seven-state count, the named controller models, the technique detail and the ladder-logic finding come from the
  FBI/EPA announcement; the boil-water-notice and manual-operations consequence and the cellular-modem blind-spot
  warning come from CISA's own alert; the exposure counts and their geography come from Censys' 2026-07-30 snapshot.
  Censys states its own report is "an exposure characterization only" and "does not confirm that any specific host is a
  victim", and that its Schneider Electric figure is vendor-wide with no PLC-model or protocol filter — both caveats are
  carried into the body. No authority has attributed the activity; the Iran line reported by SecurityWeek/AP is an open
  investigative question. The cited AP report states that the FBI declined to name a suspect and that Minnesota state
  officials had not identified one either, so the Iran framing is attributed here to its two actual origins — a prior
  sector-wide advisory and a named outside expert quoted by that report — and never to the investigating bodies.
confidence: high
update_of: 2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Enumerate every PLC and OT controller reachable from the public internet, including any attached through a cellular modem installed by an integrator or vendor and therefore absent from the asset register, and broker all remote access through a jump host instead — the FBI/EPA announcement records this exposure, not a software flaw, as the entry point."
  - "On PLCs whose project files could have been reached, compare the running ladder logic against known-good using the vendor's integrity-checking tools before returning the key switch to RUN, and validate any restore image first — one victim found modified project files across several sites."
migrated_from: null
---

**UPDATE (originally covered 2026-07-29):** The coordinated attack on Minnesota water utilities is now the visible part of a wider campaign, and three federal bodies have put names and mechanics to what was previously an unattributed disruption with an unclear vector.

The FBI and EPA issued a joint Public Service Announcement on 2026-07-30 stating that "since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). The same announcement names the targeted hardware as Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 series controllers — while cautioning that "while the FBI has only observed this behavior with the referenced Rockwell PLCs, similar considerations should also be made with other branded PLCs" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). The prior entry recorded the vector as an open question; the announcement closes it: "after remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). No CVE is involved — the access is unauthenticated exposure plus credential control, not a software flaw.

Two details go beyond the disruption itself. First, integrity: "at least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)) — meaning at least one operator's control logic, not just its access, was touched. Second, a shared-supplier multiplier: the FBI notes that "across several victims, similarities in network setup provided by third parties may provide MCA the opportunity to multiply successes when vulnerable network and hardware setups exist across customers" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). CISA's parallel alert adds the consequence at sector scale, stating the activity "has resulted in boil water notices and sustained manual operations", and singles out cellular modems installed by operators, vendors or system integrators as a common blind spot because those connections may be undocumented and excluded from routine attack-surface scans ([CISA, 2026-07-30](https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs)). On the physical side, the FBI records that reported operational effects "have included loss of pressure and flooding", and that "pressure loss in water systems could potentially allow untreated ground water to seep into pipes" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

The European relevance is now quantified rather than assumed. A Censys internet scan dated 2026-07-30 found 4,148 exposed Rockwell/Allen-Bradley EtherNet/IP hosts, 71.0% of them in the United States, with combined cellular carriers accounting for 59.0% of that total — but also 4,117 hosts fingerprinting as Siemens SIMATIC S7-1200, where "exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). That carrier concentration is the same cellular-modem exposure class CISA flags as the routinely-unscanned blind spot, sitting on a different vendor's controllers in EU member states. Censys also counts 2,072 hosts fingerprinting as Schneider Electric hardware but states explicitly that this query "has no PLC-model or protocol filter" and "should not be read as Schneider Electric PLC exposure specifically" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). The whole scan is framed as "an exposure characterization only: it does not confirm that any specific host is a victim of the activity CISA describes" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)).

Attribution is not merely open — the investigating bodies have declined to offer one. SecurityWeek, relaying the Associated Press, reports that the FBI "has not publicly identified a culprit and a spokesperson declined to say Thursday who the bureau thought might be responsible", and that "Minnesota IT Services said state officials had yet to identify who was behind the attacks" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). Neither the FBI/EPA announcement nor the CISA alert names an actor. The Iran framing in circulation has two separate origins, neither of which is an attribution of this activity: a prior multi-agency advisory warning that Iranian actors target the water and wastewater sector generally — the advisory tracked as AA26-097A, which this pipeline covered on 2026-07-24 and which the Censys report cited here names in its own subtitle ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)) — and an outside expert quoted by the same AP report, a former FBI cyber deputy assistant director now in the private sector, advising defenders to "treat it like it's Iran until proven otherwise" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). BleepingComputer's account of the CISA alert likewise names no actor ([BleepingComputer, 2026-07-31](https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/)). This entry carries no attribution and registers no actor entity.

**Defender takeaway:** the transferable content for a European water, energy or municipal OT operator is the exposure inventory, not the geography of the victims. The controller family with the heaviest European internet exposure is a different vendor's from the one under attack in the US, and its exposure runs through mobile carriers — the connectivity path least likely to appear in a scan of the corporate address space. The FBI and EPA's own checklist is the concrete work: remove inbound port exposure and broker remote access through a secure gateway or jump host, secure and log cellular modems used for field connectivity, set complex unique device passwords, restrict access with ACLs to expected control-system devices, keep physical and software key switches in the RUN position outside maintenance windows, review project files against known-good using vendor integrity-checking tools, and maintain a tested ability to run manually ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

**Triage:** an engineer legitimately changes a controller's IP address and sets a password during commissioning or a modem swap, so the events themselves are not the signal. The discriminators are provenance and sequence: the change arrives from outside the engineering-workstation address range or over the cellular path rather than the engineering VLAN, it lands outside a change window with no corresponding work order, and the password set is one operations cannot subsequently authenticate with — a lockout rather than a rotation. A project-file or ladder-logic checksum that moves without a matching download record from a known engineering host is the higher-confidence version of the same test, and the FBI's account of discrepancies noticed "across several sites" suggests comparing logic across a fleet rather than device by device.
