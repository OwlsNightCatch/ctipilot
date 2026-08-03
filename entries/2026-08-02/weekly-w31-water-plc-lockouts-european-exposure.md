---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Water-sector PLC lockouts went from one state to seven inside the week, and the European exposure got counted — 86% of 4,117 internet-facing Siemens S7-1200 units sit in four EU countries, reached through mobile carriers"
headline: "Water PLC attacks spread to seven states in W31, and Europe's own controller exposure is now quantified"
summary: >
  What began as a two-day coordinated attack on more than 30 Minnesota water and wastewater utilities became,
  inside the same week, a federally-confirmed campaign across at least seven US states in which attackers
  reached internet-facing programmable logic controllers, changed their IP addresses and passwords, and in at
  least one case modified the ladder logic itself. No vulnerability is involved — the entry point is
  reachability plus credential control. The horizon fact for this constituency is the exposure count
  published the same day: a Censys scan found 4,117 internet-exposed Siemens SIMATIC S7-1200 units with 86%
  of them in Greece, Spain, Italy and Austria, each concentration dominated by that country's leading mobile
  carrier — the connectivity path least likely to appear in a scan of corporate address space. No
  investigating body has attributed the activity, and this entry names no actor.
discovered_at: "2026-08-02T23:44:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T2311Z-weekly
priority: high
immediate_action: null
tags: [ot-ics, actively-exploited, default-config, no-patch]
regions: [us, europe, global]
sectors: [water, energy, public-sector]
entities:
  - incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
techniques: [T1133, T1078.001, T1531, T1565.001]
affected_products: ["Rockwell Automation Allen-Bradley MicroLogix 1100", "Rockwell Automation Allen-Bradley MicroLogix 1400", "Siemens SIMATIC S7-1200"]
cves: []
sources:
  - url: "https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions"
    publisher: "FBI and EPA (joint Public Service Announcement)"
    date: "2026-07-30"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs"
    publisher: "CISA"
    date: "2026-07-30"
    role: primary
  - url: "https://censys.com/blog/cisa-alert-water-tower-plc-targeting/"
    publisher: "Censys Research"
    date: "2026-07-30"
    role: corroborating
  - url: "https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/"
    publisher: "StateScoop"
    date: "2026-07-28"
    role: corroborating
  - url: "https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/"
    publisher: "SecurityWeek / Associated Press"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "After remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality."
    publisher: "FBI and EPA (joint Public Service Announcement)"
  - quote: "At least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites."
    publisher: "FBI and EPA (joint Public Service Announcement)"
  - quote: "Censys ARC identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200."
    publisher: "Censys Research"
verification: multi-source
sourcing_note: >
  The campaign scale, the targeted controller families and the access mechanics are cited to the FBI/EPA joint
  announcement that states them; the sector-level consequences and the cellular-modem blind spot to CISA's
  parallel alert; the European exposure counts to the Censys scan. Attribution is deliberately absent: neither
  the FBI/EPA announcement nor the CISA alert names an actor, and reporting relayed from the Associated Press
  records that the FBI has not publicly identified a culprit and that Minnesota officials had not either. The
  Iran framing circulating around this story traces to a separate prior advisory about Iranian targeting of
  the sector generally and to one outside expert's advice, neither of which is an attribution of this
  activity — so no actor entity is registered here. The per-city impact classes are attributed to the cities
  StateScoop names rather than generalised across the 30-plus communities; what generalises on that page is
  water quality being unaffected. Censys is cited only for its own scan counts, never for its restatement of
  the CISA alert, which that post itself flags as paraphrased from user-supplied content and not
  independently re-fetched.
confidence: high
update_of: null
references:
  - 2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack
  - 2026-08-01/fbi-epa-water-plc-lockout-seven-states-eu-exposure
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

**If you did nothing this week:** an internet-reachable controller in your water, wastewater or municipal estate is exposed to a technique that needs no vulnerability and no exploit — and if it is attached through an integrator's cellular modem, it is probably not in the asset register you would check to find out.

The escalation happened inside seven days. Minnesota's technology bureau announced on 2026-07-28 that more than 30 communities had water and wastewater utilities disrupted by a coordinated attack over 26 and 27 July, with multiple utilities stating water remained safe and no treatment-quality impact reported; where the impact class was described per city it varied — in Plymouth's case the attack was limited to equipment connected via cellular communications at two water towers and multiple lift stations, while Braham's water plant went offline outright ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). Two days later the FBI and EPA put federal scope on it, stating that "since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)), and naming the targeted hardware as Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 series controllers ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

The mechanics are the reason this is a strategic item rather than a vulnerability item. The announcement records that "after remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)) — reachability and credential control, with no CVE in the chain, which means no patch cycle closes it and no vulnerability scanner reports it. Integrity, not just availability, was touched in at least one case: "at least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). CISA's parallel alert adds the sector-scale consequence, stating the activity "has resulted in boil water notices and sustained manual operations", and singles out cellular modems installed by operators, vendors or system integrators as a routine blind spot because those connections may be undocumented and excluded from attack-surface scans ([CISA, 2026-07-30](https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs)). The FBI also names a supplier-homogeneity multiplier that transfers directly to European municipal estates, noting that across several victims, similarities in network setup provided by third parties may let an actor multiply successes where the same vulnerable setups recur across a provider's customers ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

For a Swiss or European defender the decisive in-window fact is that the exposure is now measured rather than assumed, and it sits on a different vendor's hardware. Censys reported on 2026-07-30 that it "identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200", and that "exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). That carrier concentration is precisely the class of connectivity CISA flags as unscanned, on controllers in EU member states, for a technique that requires only reachability. Censys is careful about what the scan is: it frames the whole exercise as an exposure characterisation that does not confirm any specific host is a victim of the activity CISA describes ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)).

Attribution has not merely been withheld — it has been declined. Reporting relaying the Associated Press records that the FBI "has not publicly identified a culprit and a spokesperson declined to say Thursday who the bureau thought might be responsible", and that "Minnesota IT Services said state officials had yet to identify who was behind the attacks" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). The Iran framing in circulation has two origins, neither of which is a finding about this campaign: a prior multi-agency advisory concerning Iranian targeting of the water sector in general, and an outside expert quoted in the same AP report advising defenders to treat it as Iran until proven otherwise ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). Reading the calendar as evidence would be a mistake, and it is also unnecessary: nothing about the defensive work depends on who is doing it.

**Defender takeaway:** the transferable content is the exposure inventory, not the geography of the victims. The controller family with the heaviest European internet exposure belongs to a different vendor than the one under attack in the United States, and its exposure runs through mobile carriers — so an inventory pass scoped to the corporate address space will report all-clear while the actual exposure sits on an APN. Because the technique consumes no vulnerability, the question to answer is reachability, and the answer has to include every field device an integrator or vendor connected on your behalf.

**Triage:** an engineer legitimately changes a controller's IP address and sets a password during commissioning or a modem swap, so those events alone are not the signal. The discriminators are provenance, timing and reversibility: the change arrives from outside the engineering-workstation range or over the cellular path rather than the engineering VLAN, it lands outside a change window with no work order, and the password that was set is one operations cannot subsequently authenticate with — a lockout rather than a rotation. A project-file or ladder-logic checksum that moves with no matching download record from a known engineering host is the higher-confidence version of the same test, and the FBI's account of discrepancies noticed across several sites argues for comparing logic across the fleet rather than device by device.
