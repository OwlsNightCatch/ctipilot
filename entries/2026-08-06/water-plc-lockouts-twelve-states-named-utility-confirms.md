---
schema: 1
kind: incident
horizon: operational
title: "Water-utility PLC lockouts reach at least twelve US states, and Clayton County publicly confirms a distribution-side consequence as its own"
headline: "The campaign that was seven states a week ago is twelve, and a named utility has put its own name to the impact"
summary: >
  The water-sector operational-technology campaign covered here on 2026-08-01 at seven US states has grown to at
  least twelve, with South Dakota and Georgia newly confirmed. Clayton County Water Authority in Georgia has
  publicly attached its own name to a distribution-side consequence: it reported
  unauthorised cyber activity in late July that caused reduced water pressure across part of the county and led it
  to issue a precautionary boil-water advisory before service was restored within hours. Effects of that class were
  already reported in aggregate — the FBI has recorded pressure loss and flooding among the wave's operational
  effects — so the change is attributable confirmation, not a new category of harm. The mechanism is unchanged and
  involves no vulnerability, and federal agencies have still declined to attribute the campaign publicly.
discovered_at: "2026-08-06T04:11:48Z"
event_date: "2026-08-05"
run_id: 2026-08-06T0411Z-intel
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited]
regions: [us, europe]
sectors: [water]
entities:
  - incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
techniques: [T1531, T1565]
affected_products: []
cves: []
sources:
  - url: "https://therecord.media/iran-cyberattacks-water-treatment"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-05"
    role: primary
  - url: "https://www.securityweek.com/water-sector-cyberattacks-reportedly-hit-at-least-12-states/"
    publisher: "SecurityWeek"
    date: "2026-08-05"
    role: corroborating
  - url: "https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/"
    publisher: "CBS News Atlanta"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "After the devices are accessed remotely, the actors change the passwords and remove the ability of officials to monitor and control the devices."
    publisher: "The Record (Recorded Future News)"
  - quote: "caused reduced water pressure in parts of the county"
    publisher: "CBS News Atlanta"
  - quote: "the CCWA issued a precautionary boil water advisory as a safety measure"
    publisher: "CBS News Atlanta"
  - quote: "federal agencies have declined to publicly attribute the attacks"
    publisher: "The Record (Recorded Future News)"
verification: multi-source
sourcing_note: >
  The twelve-state figure originates with ABC News and is relayed by both The Record and SecurityWeek rather than
  confirmed in a federal statement, so it is reported here as reporting rather than as an agency count. Some
  coverage describes the campaign as allegedly linked to Iranian actors; this entry does not adopt that, because the
  same reporting records that federal agencies have declined to attribute it publicly and no authority has
  connected the Clayton County incident to any actor.
confidence: high
update_of: 2026-08-01/fbi-epa-water-plc-lockout-seven-states-eu-exposure
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

**UPDATE (originally covered 2026-08-01):** two things changed in the week since the FBI and EPA confirmed water and wastewater utilities in at least seven US states had reported programmable-logic-controller lockouts. The count has grown — water utilities in at least twelve states have now reported cyberattacks on their operational technology, with South Dakota and Georgia announcing incidents and several facilities in Michigan among those remediating, a figure originating with ABC News and relayed by The Record ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)); SecurityWeek reports the same expansion and names Georgia's confirmation as following a pump-station disruption ([SecurityWeek, 2026-08-05](https://www.securityweek.com/water-sector-cyberattacks-reportedly-hit-at-least-12-states/)).

More useful than the count is the second change: a named utility has publicly confirmed a distribution-side consequence as its own. Clayton County Water Authority believes unauthorised cyber activity may have affected its systems in late July, and the incident caused reduced water pressure in parts of the county; the authority issued a precautionary boil-water advisory as a safety measure, and service was restored within hours once testing determined the water was safe ([CBS News Atlanta, 2026-08-04](https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/)). Consequences of that class were not new to the wave — the FBI has said some affected water systems experienced pressure loss and flooding as a result of the activity ([CBS News Atlanta, 2026-08-04](https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/)), and the original entry already carried CISA's statement that it had produced boil-water notices and sustained manual operations. What changes is attribution: those effects were previously federal aggregate reporting, and this is a single identified operator describing what happened on its own network, which is a materially different evidentiary object for anyone arguing an exposure case internally.

The mechanism is unchanged and remains the reason this belongs in a European brief. The FBI's description is that after the devices are accessed remotely, the actors change the passwords and remove the ability of officials to monitor and control the devices ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)). There is no vulnerability in the chain, so there is nothing to patch: the entry condition is reachability plus control of a credential, which is exactly the condition the Censys scan cited in the original entry quantified for Europe — thousands of internet-exposed controllers concentrated in a handful of EU countries and reached predominantly through mobile-carrier connectivity rather than corporate address space. Attribution remains open: federal agencies have declined to publicly attribute the attacks, and no authority has tied the Clayton County incident to any actor ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)).

**Defender takeaway:** the delta that should change a European water-sector defender's behaviour is the named, self-reported case, not the state count. An operator weighing whether controller exposure is a theoretical or an operational risk can now point at an identified utility describing pressure loss and a public health advisory on its own network, rather than at an aggregate figure in a federal alert. The actions from the original entry stand unchanged — enumerate every internet-reachable controller including those attached through integrator-installed cellular modems, and verify running logic against known-good before returning devices to service — and nothing in this week's reporting supersedes them. Because the attacker's first observable act is a successful credential-backed configuration change rather than an exploit, the detectable events are controller authentication from outside the engineering network, password or account changes on a controller outside a maintenance window, and a controller's reported state diverging from independently measured field instrumentation.
