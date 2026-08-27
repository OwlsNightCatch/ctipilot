---
schema: 1
kind: incident
horizon: operational
title: >
  Coordinated two-day cyberattack disrupts operational technology at 30+ Minnesota water and
  wastewater utilities — no authority has attributed it
headline: >
  Minnesota confirms a coordinated attack on field OT at more than 30 community water systems,
  days after a US advisory update on internet-exposed PLCs
summary: >
  Minnesota IT Services announced on 2026-07-28 that more than 30 communities had water and
  wastewater utilities disrupted by a coordinated cyberattack over 26–27 July, affecting
  programmable logic controllers and cellular-connected equipment at water towers and lift
  stations. Plymouth disconnected affected cellular equipment from its network; Braham's water
  plant went offline and the city briefly asked residents to minimise use because its tower held a
  limited quantity; South St. Paul reported impact to certain automated controls with no major
  effect on treatment operations. No source reports impact to drinking-water safety or treatment
  quality. Attribution is explicitly open — the affected city says "unknown actors" and the Center
  for Internet Security states the attacks have not been attributed and it is unclear whether the
  PLC vector a recent US joint advisory warned about was involved. That advisory's documented
  tradecraft is what makes this transferable: it needs no CVE, only an internet-reachable
  controller.
discovered_at: "2026-07-29T05:45:00Z"
updated_at: "2026-08-10T04:56:00Z"
event_date: 2026-07-27
run_id: 2026-07-29T0408Z-intel
priority: high
immediate_action: null
tags:
  - ot-ics
  - actively-exploited
  - default-config
  - info-disclosure
regions:
  - us
  - global
  - europe
sectors:
  - water
  - energy
  - public-sector
entities:
  - "incident:minnesota-water-utilities-coordinated-cyberattack-2026-07"
techniques:
  - T1133
  - T1565
  - T1041
  - T1078.001
  - T1531
  - T1565.001
affected_products:
  - Rockwell Automation Allen-Bradley MicroLogix 1100
  - Rockwell Automation Allen-Bradley MicroLogix 1400
  - Siemens SIMATIC S7-1200
cves: []
sources:
  - url: "https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/"
    publisher: StateScoop
    date: 2026-07-28
    role: primary
  - url: "https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/"
    publisher: Cybersecurity Dive
    date: 2026-07-28
    role: corroborating
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a"
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
    date: 2026-07-22
    role: corroborating
  - url: "https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions"
    publisher: FBI and EPA (joint Public Service Announcement)
    date: 2026-07-30
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs"
    publisher: CISA (with EPA and FBI)
    date: 2026-07-30
    role: primary
  - url: "https://censys.com/blog/cisa-alert-water-tower-plc-targeting/"
    publisher: Censys Research
    date: 2026-07-30
    role: corroborating
  - url: "https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/"
    publisher: SecurityWeek / Associated Press
    date: 2026-07-31
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/"
    publisher: BleepingComputer
    date: 2026-07-31
    role: corroborating
  - url: "https://therecord.media/iran-cyberattacks-water-treatment"
    publisher: The Record (Recorded Future News)
    date: 2026-08-05
    role: primary
  - url: "https://www.securityweek.com/water-sector-cyberattacks-reportedly-hit-at-least-12-states/"
    publisher: SecurityWeek
    date: 2026-08-05
    role: corroborating
  - url: "https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/"
    publisher: CBS News Atlanta
    date: 2026-08-04
    role: corroborating
  - url: "https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/"
    publisher: Forescout
    date: 2026-08-05
    role: primary
  - url: "https://www.nextgov.com/cybersecurity/2026/08/cisa-still-finds-water-system-controls-exposed-online-amid-multistate-hacks/415266/"
    publisher: Nextgov/FCW
    date: 2026-08-06
    role: primary
closed_sources: []
evidence:
  - quote: "Analysis indicated the project file retained ladder logic for downstream function but added logic that overrode specific instruction sets responsible for maintaining safe operating parameters in the victim's environment."
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
  - quote: "the changes disabled critical shutdown and alarm logic, allowing systems to enter unsafe conditions without notifying operators of the anomalies."
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
  - quote: The two-day attack comes days after federal officials warned of state-linked threat groups targeting a wider set of industrial devices.
    publisher: Cybersecurity Dive
  - quote: "Since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations."
    publisher: FBI and EPA (joint Public Service Announcement)
  - quote: "After remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality."
    publisher: FBI and EPA (joint Public Service Announcement)
  - quote: At least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites.
    publisher: FBI and EPA (joint Public Service Announcement)
  - quote: Threat actors targeting exposed PLCs have modified passwords to lock out operators and disconnected the PLCs by changing their IP addresses. This activity has resulted in boil water notices and sustained manual operations.
    publisher: CISA (with EPA and FBI)
  - quote: "Censys ARC identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200. Exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers."
    publisher: Censys Research
  - quote: "After the devices are accessed remotely, the actors change the passwords and remove the ability of officials to monitor and control the devices."
    publisher: The Record (Recorded Future News)
  - quote: caused reduced water pressure in parts of the county
    publisher: CBS News Atlanta
  - quote: the CCWA issued a precautionary boil water advisory as a safety measure
    publisher: CBS News Atlanta
  - quote: federal agencies have declined to publicly attribute the attacks
    publisher: The Record (Recorded Future News)
  - quote: "Querying the Shodan search engine on August 3, 2026 returns 4,407 devices exposing port 44818."
    publisher: Forescout
  - quote: "Although we cannot confirm these particular assets were compromised in this campaign, they had some interesting characteristics"
    publisher: Forescout
  - quote: "19 of the 22 hosts (86%) were on the same mobile carrier network, connected via cellular routers"
    publisher: Forescout
  - quote: "Exposing EtherNet/IP to the internet creates an unauthenticated path that, depending on device configuration, can allow attackers to obtain information about exposed assets or even write configurations on them."
    publisher: Forescout
  - quote: "We're seeing things like [programmable logic controllers] that are open and accessible on the internet with either no password set or default password set"
    publisher: Nextgov/FCW
  - quote: "For us, we're not doing anything with attribution right now"
    publisher: Nextgov/FCW
verification: multi-source
sourcing_note: >
  Two independent outlets reporting the same event with named official and municipal statements,
  plus the joint advisory as background. The attribution boundary is the critical sourcing point
  and is held deliberately: no named authority — not the FBI, CISA, EPA, Minnesota IT Services,
  nor any affected city — has attributed the Minnesota attack to any actor. Braham's own statement
  says "unknown actors"; the Center for Internet Security's threat-intelligence director states
  the attacks have not been attributed to any particular party and that it is unclear whether the
  PLC vector CISA warned about was involved. Where press coverage places Iran near this story it
  does so as contextual juxtaposition with the concurrently updated AA26-097A advisory — one
  outlet's remark that Iran "is a reasonable guess" is that reporter's own inference, not an
  official claim, and is not repeated here as fact. AA26-097A describes a separate, ongoing
  nationwide campaign and is cited only for the tradecraft and mitigations it documents, never as
  reporting on this incident. Its indicator tables, including the IP addresses CISA itself advises
  vetting before blocking, are omitted. One nuance between the two outlets is reconciled in the
  body: Braham did briefly ask residents to minimise water use because of tank level, which the
  broader "no usage changes requested" framing does not capture. `affected_products` is
  deliberately empty and the entry carries no state-nexus tag: no source names any controller
  model involved in the Minnesota event, and no source attributes it to any actor. The four
  controller families the joint advisory names are targets of that separate campaign and are
  recorded on the entry covering it, not asserted here.
confidence: medium
references:
  - 2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Enumerate every PLC and cellular-connected field device in your water, wastewater and energy estate that is reachable from the public internet, and move remote access behind a gateway or jump host — the tradecraft in the referenced joint advisory exploits no vulnerability, only reachability, so an inventory pass answers the exposure question directly."
  - "Return any controller with a physical mode switch to the RUN position, switching to program or remote mode only briefly for a validated update — the joint advisory names this as a control precisely because the documented impact is delivered by re-uploading project logic."
  - "Enumerate every PLC and OT controller reachable from the public internet, including any attached through a cellular modem installed by an integrator or vendor and therefore absent from the asset register, and broker all remote access through a jump host instead — the FBI/EPA announcement records this exposure, not a software flaw, as the entry point."
  - "On PLCs whose project files could have been reached, compare the running ladder logic against known-good using the vendor's integrity-checking tools before returning the key switch to RUN, and validate any restore image first — one victim found modified project files across several sites."
updates:
  - at: "2026-08-01T04:31:06Z"
    run_id: 2026-08-01T0409Z-intel
    type: update
    summary: >
      The FBI and EPA issued a joint Public Service Announcement on 2026-07-30, with a parallel CISA
      alert the same day, confirming that water and wastewater utilities in at least seven US states
      have reported PLC lockout incidents since 2026-07-27 and naming Rockwell
      Automation/Allen-Bradley MicroLogix 1100 and 1400 controllers as the targeted hardware.
      Attackers reaching internet-facing devices changed their IP addresses and set passwords,
      producing loss of view and in some cases loss of control; one organisation found modified PLC
      project files. A Censys scan dated 2026-07-30 puts 4,117 Siemens SIMATIC S7-1200 units on the
      public internet with 86% of them in Greece, Spain, Italy and Austria, each concentration
      dominated by that country's leading mobile carrier.
    fields:
      - actions
      - affected_products
      - evidence
      - regions
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-01/fbi-epa-water-plc-lockout-seven-states-eu-exposure
  - at: "2026-08-06T04:11:48Z"
    run_id: 2026-08-06T0411Z-intel
    type: update
    summary: >
      The water-sector operational-technology campaign covered here on 2026-08-01 at seven US states
      has grown to at least twelve, with South Dakota and Georgia newly confirmed. Clayton County
      Water Authority in Georgia has publicly attached its own name to a distribution-side
      consequence: it reported unauthorised cyber activity in late July that caused reduced water
      pressure across part of the county and led it to issue a precautionary boil-water advisory
      before service was restored within hours. Effects of that class were already reported in
      aggregate — the FBI has recorded pressure loss and flooding among the wave's operational effects
      — so the change is attributable confirmation, not a new category of harm. The mechanism is
      unchanged and involves no vulnerability, and federal agencies have still declined to attribute
      the campaign publicly.
    fields:
      - evidence
      - sources
      - body
    merged_from: 2026-08-06/water-plc-lockouts-twelve-states-named-utility-confirms
  - at: "2026-08-10T04:56:00Z"
    run_id: 2026-08-10T0411Z-intel
    type: update
    summary: >
      Forescout queried Shodan on 2026-08-03 and found 4,407 devices exposing the EtherNet/IP
      engineering port used by Rockwell Automation controllers, 65% in the United States with Canada
      and Spain next. Of the 22 it located in cities targeted by the water-utility campaign, 19 were
      on the same mobile carrier network reached through cellular routers, and 19 of 22 ran firmware
      susceptible to CVE-2017-16740 — two separate findings that share a number. Forescout cannot
      confirm any of those assets were compromised and states no CVE is confirmed as exploited in the
      campaign. CISA's acting director, interviewed at Black Hat, says exposed controllers are being
      found with no password or a default one, and that the agency is doing nothing on attribution
      right now.
    fields:
      - evidence
      - sources
      - tags
      - body
    merged_from: 2026-08-10/forescout-rockwell-plc-exposure-census-cellular-carrier-path
migrated_from: null
---

The confirmed facts are narrow and worth stating precisely. Minnesota's technology bureau announced on 2026-07-28 that more than 30 communities had their water and wastewater utilities disrupted by a coordinated cyberattack on 26 and 27 July ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)), a two-day event rather than a single-utility incident ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). Where individual utilities described impact, it fell on field equipment rather than treatment processes: Plymouth stated the attack was limited to equipment connected via cellular communications at two water towers and multiple lift stations, and disconnected that equipment from the network to stop the attack and avoid retargeting during reconfiguration; Braham's water plant went offline, and the city later stated the outage was the result of a malicious cyberattack of computerised operating systems by unknown actors ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). Braham did ask residents to minimise water use while its tower held a limited quantity, and a later notice reported the plant back online ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)) — a real if temporary consumption instruction. Separately, authorities in South St. Paul said they identified a cyberattack on Monday that impacted certain automated controls, and after implementing contingency procedures confirmed no major impact to drinking and wastewater treatment operations ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). Multiple utilities stated water remained safe and no treatment-quality impact has been reported. Minnesota IT Services coordinated a response alongside the FBI, CISA and the EPA, with its chief information security officer describing a whole-of-government response that helped prevent more serious impacts ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)).

What is *not* established matters as much. No authority has named an actor. The Center for Internet Security's senior director of threat intelligence stated the Minnesota attacks have not yet been attributed to any particular party and that it is unclear whether the programmable logic controllers CISA had warned about were involved, and separately noted that of the nation-state attacks on US water facilities in recent years, none has documented major downstream health impacts ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). The FBI confirmed only that it is aware and in contact with victims ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). The reason Iran appears in coverage of this event is timing: the attack landed days after federal officials warned of state-linked groups targeting a wider set of industrial devices ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)) — a juxtaposition, not a finding. Treating it as attribution would be reading the calendar as evidence.

The transferable content sits in that separate advisory, and it is why this belongs in front of European water and energy operators despite the victims being American. AA26-097A documents actors using leased third-party infrastructure and the vendors' *own* engineering software — Rockwell Studio 5000 Logix Designer, Schneider EcoStruxure Control Expert, Siemens TIA Portal — to reach misconfigured, internet-facing controllers and pull down device project files, then re-upload files with modified or deleted logic ([CISA and partners, 2026-07-22](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)). At one victim the FBI observed a malicious project file downloaded to a PLC that retained ladder logic for downstream function but added logic overriding the instruction sets responsible for maintaining safe operating parameters, and the changes disabled critical shutdown and alarm logic, allowing systems to enter unsafe conditions without notifying operators ([CISA and partners, 2026-07-22](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)). CISA is explicit that this represents no new vulnerability in the named products — it is opportunistic targeting of misconfiguration. The affected controller families are the same Rockwell, Schneider and Siemens lines that run European water, wastewater and district-energy plants, and in one instance access came through Dropbear SSH on a victim's *modem*, which is precisely the class of device Plymouth found affected.

**Defender takeaway:** the exposure this describes cannot be closed by patching, because there is nothing vulnerable to patch — a controller reachable from the internet with vendor engineering software able to talk to it is the whole attack surface, and a cellular modem at an unstaffed lift station is as much a perimeter as any firewall. Two things follow. First, the inventory question ("which of our controllers and field modems can be reached from outside, including over cellular?") is answerable this week and is the actual control. Second, integrity of logic becomes a monitoring target in its own right: because the documented impact silently removes shutdown and alarm behaviour, an operator watching only for alarms would see a quieter plant, not a compromised one, so periodic comparison of running project files against known-good logic — Add-On Instructions included — is the detection that catches this class rather than the alerting the attacker just disabled.

**Triage:** engineering software connecting to a PLC and writing a project file is exactly what commissioning and maintenance look like, so the activity class is not the signal. The discriminators the advisory's own mechanics supply are provenance and timing: a project-file write originating from outside the engineering network or from leased hosting rather than an engineering workstation; a controller left in program or remote mode outside a change window rather than in RUN; and a logic change with no corresponding maintenance record. On the network side, protocol functions that modify programs or change controller mode are the ones to surface — connection attempts to controller-associated ports are ubiquitous background noise, whereas a mode change or program write is a discrete, auditable act.

## Update — 2026-08-01T04:31:06Z

The coordinated attack on Minnesota water utilities is now the visible part of a wider campaign, and three federal bodies have put names and mechanics to what was previously an unattributed disruption with an unclear vector.

The FBI and EPA issued a joint Public Service Announcement on 2026-07-30 stating that "since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). The same announcement names the targeted hardware as Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 series controllers — while cautioning that "while the FBI has only observed this behavior with the referenced Rockwell PLCs, similar considerations should also be made with other branded PLCs" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). The prior entry recorded the vector as an open question; the announcement closes it: "after remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). No CVE is involved — the access is unauthenticated exposure plus credential control, not a software flaw.

Two details go beyond the disruption itself. First, integrity: "at least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)) — meaning at least one operator's control logic, not just its access, was touched. Second, a shared-supplier multiplier: the FBI notes that "across several victims, similarities in network setup provided by third parties may provide MCA the opportunity to multiply successes when vulnerable network and hardware setups exist across customers" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). CISA's parallel alert adds the consequence at sector scale, stating the activity "has resulted in boil water notices and sustained manual operations", and singles out cellular modems installed by operators, vendors or system integrators as a common blind spot because those connections may be undocumented and excluded from routine attack-surface scans ([CISA, 2026-07-30](https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs)). On the physical side, the FBI records that reported operational effects "have included loss of pressure and flooding", and that "pressure loss in water systems could potentially allow untreated ground water to seep into pipes" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

The European relevance is now quantified rather than assumed. A Censys internet scan dated 2026-07-30 found 4,148 exposed Rockwell/Allen-Bradley EtherNet/IP hosts, 71.0% of them in the United States, with combined cellular carriers accounting for 59.0% of that total — but also 4,117 hosts fingerprinting as Siemens SIMATIC S7-1200, where "exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). That carrier concentration is the same cellular-modem exposure class CISA flags as the routinely-unscanned blind spot, sitting on a different vendor's controllers in EU member states. Censys also counts 2,072 hosts fingerprinting as Schneider Electric hardware but states explicitly that this query "has no PLC-model or protocol filter" and "should not be read as Schneider Electric PLC exposure specifically" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). The whole scan is framed as "an exposure characterization only: it does not confirm that any specific host is a victim of the activity CISA describes" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)).

Attribution is not merely open — the investigating bodies have declined to offer one. SecurityWeek, relaying the Associated Press, reports that the FBI "has not publicly identified a culprit and a spokesperson declined to say Thursday who the bureau thought might be responsible", and that "Minnesota IT Services said state officials had yet to identify who was behind the attacks" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). Neither the FBI/EPA announcement nor the CISA alert names an actor. The Iran framing in circulation has two separate origins, neither of which is an attribution of this activity: a prior multi-agency advisory warning that Iranian actors target the water and wastewater sector generally — the advisory tracked as AA26-097A, which this pipeline covered on 2026-07-24 and which the Censys report cited here names in its own subtitle ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)) — and an outside expert quoted by the same AP report, a former FBI cyber deputy assistant director now in the private sector, advising defenders to "treat it like it's Iran until proven otherwise" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). BleepingComputer's account of the CISA alert likewise names no actor ([BleepingComputer, 2026-07-31](https://www.bleepingcomputer.com/news/security/cisa-warns-of-cyberattacks-disrupting-us-water-utilities/)). This entry carries no attribution and registers no actor entity.

**Defender takeaway:** the transferable content for a European water, energy or municipal OT operator is the exposure inventory, not the geography of the victims. The controller family with the heaviest European internet exposure is a different vendor's from the one under attack in the US, and its exposure runs through mobile carriers — the connectivity path least likely to appear in a scan of the corporate address space. The FBI and EPA's own checklist is the concrete work: remove inbound port exposure and broker remote access through a secure gateway or jump host, secure and log cellular modems used for field connectivity, set complex unique device passwords, restrict access with ACLs to expected control-system devices, keep physical and software key switches in the RUN position outside maintenance windows, review project files against known-good using vendor integrity-checking tools, and maintain a tested ability to run manually ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

**Triage:** an engineer legitimately changes a controller's IP address and sets a password during commissioning or a modem swap, so the events themselves are not the signal. The discriminators are provenance and sequence: the change arrives from outside the engineering-workstation address range or over the cellular path rather than the engineering VLAN, it lands outside a change window with no corresponding work order, and the password set is one operations cannot subsequently authenticate with — a lockout rather than a rotation. A project-file or ladder-logic checksum that moves without a matching download record from a known engineering host is the higher-confidence version of the same test, and the FBI's account of discrepancies noticed "across several sites" suggests comparing logic across a fleet rather than device by device.

## Update — 2026-08-06T04:11:48Z

Two things changed in the week since the FBI and EPA confirmed water and wastewater utilities in at least seven US states had reported programmable-logic-controller lockouts. The count has grown — water utilities in at least twelve states have now reported cyberattacks on their operational technology, with South Dakota and Georgia announcing incidents and several facilities in Michigan among those remediating, a figure originating with ABC News and relayed by The Record ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)); SecurityWeek reports the same expansion and names Georgia's confirmation as following a pump-station disruption ([SecurityWeek, 2026-08-05](https://www.securityweek.com/water-sector-cyberattacks-reportedly-hit-at-least-12-states/)).

More useful than the count is the second change: a named utility has publicly confirmed a distribution-side consequence as its own. Clayton County Water Authority believes unauthorised cyber activity may have affected its systems in late July, and the incident caused reduced water pressure in parts of the county; the authority issued a precautionary boil-water advisory as a safety measure, and service was restored within hours once testing determined the water was safe ([CBS News Atlanta, 2026-08-04](https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/)). Consequences of that class were not new to the wave — the FBI has said some affected water systems experienced pressure loss and flooding as a result of the activity ([CBS News Atlanta, 2026-08-04](https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/)), and the original entry already carried CISA's statement that it had produced boil-water notices and sustained manual operations. What changes is attribution: those effects were previously federal aggregate reporting, and this is a single identified operator describing what happened on its own network, which is a materially different evidentiary object for anyone arguing an exposure case internally.

The mechanism is unchanged and remains the reason this belongs in a European brief. The FBI's description is that after the devices are accessed remotely, the actors change the passwords and remove the ability of officials to monitor and control the devices ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)). There is no vulnerability in the chain, so there is nothing to patch: the entry condition is reachability plus control of a credential, which is exactly the condition the Censys scan cited in the original entry quantified for Europe — thousands of internet-exposed controllers concentrated in a handful of EU countries and reached predominantly through mobile-carrier connectivity rather than corporate address space. Attribution remains open: federal agencies have declined to publicly attribute the attacks, and no authority has tied the Clayton County incident to any actor ([The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)).

**Defender takeaway:** the delta that should change a European water-sector defender's behaviour is the named, self-reported case, not the state count. An operator weighing whether controller exposure is a theoretical or an operational risk can now point at an identified utility describing pressure loss and a public health advisory on its own network, rather than at an aggregate figure in a federal alert. The actions from the original entry stand unchanged — enumerate every internet-reachable controller including those attached through integrator-installed cellular modems, and verify running logic against known-good before returning devices to service — and nothing in this week's reporting supersedes them. Because the attacker's first observable act is a successful credential-backed configuration change rather than an exploit, the detectable events are controller authentication from outside the engineering network, password or account changes on a controller outside a maintenance window, and a controller's reported state diverging from independently measured field instrumentation.

## Update — 2026-08-10T04:56:00Z

The water-sector controller-lockout campaign has been tracked here through its growth to at least twelve US states and the FBI's naming of the targeted controller families. What was missing was a measurement of the exposed estate. Forescout has now published one ([Forescout, 2026-08-05](https://www.forescout.com/blog/ot-security-analysis-exposed-devices-attacked-in-us-water-systems/)).

"Querying the Shodan search engine on August 3, 2026 returns 4,407 devices exposing port 44818" — the EtherNet/IP engineering protocol used by the Rockwell Automation and Allen-Bradley families the joint federal advisory named. "The vast majority (65%) are located in the U.S., followed by Canada (12%) and Spain (3%)." Forescout also notes the exposed population has fallen substantially from its 2020 peak, so the trend is downward even as the absolute number stays material.

The finding worth carrying into a European estate is not the headline count but what Forescout found inside it. Of the devices located in cities the campaign targeted, "Although we cannot confirm these particular assets were compromised in this campaign, they had some interesting characteristics" — and the first of those is that "19 of the 22 hosts (86%) were on the same mobile carrier network, connected via cellular routers." That is a connectivity path, not an IT-network path: controllers reachable through a mobile carrier do not appear in a scan of an organisation's own address space, do not sit behind its perimeter, and are frequently owned operationally by an integrator rather than by the utility. Separately, and confusingly sharing the same ratio, "Approximately 86% (19 of 22) hosts observed in the affected cities were susceptible to this CVE based on firmware versions" — referring to CVE-2017-16740, which Forescout names but does not describe further. These are two different observations about the same 22 devices and should not be read as one.

Forescout is careful about what that CVE means here, and the care is worth preserving: "Exploitation would require Modbus TCP to be enabled, which was not confirmed", and "There is no confirmation of any CVE exploited in this campaign". The vulnerability is a patch-currency signal on devices that were already exposed and already targeted — the point being that controllers left on the public internet in attacked cities were also running eight-year-old firmware. The exposure itself needs no vulnerability at all: "Exposing EtherNet/IP to the internet creates an unauthenticated path that, depending on device configuration, can allow attackers to obtain information about exposed assets or even write configurations on them."

CISA's acting director, interviewed on the sidelines of Black Hat, described what the agency keeps finding: "We're seeing things like [programmable logic controllers] that are open and accessible on the internet with either no password set or default password set" ([Nextgov/FCW, 2026-08-06](https://www.nextgov.com/cybersecurity/2026/08/cisa-still-finds-water-system-controls-exposed-online-amid-multistate-hacks/415266/)). Asked about attribution he was equally direct — "For us, we're not doing anything with attribution right now" — with the agency's focus on assisting affected operators instead.

**Defender takeaway:** the transferable finding for European water, energy and transport operators is the carrier path, not the American device count. An asset inventory built by scanning the organisation's own ranges will not see a controller that reaches the internet through a cellular router on an operator's network, which is precisely where most of the exposed devices in attacked cities turned out to sit — and this pipeline has already recorded a European OT intrusion that ran through a mobile carrier's private network. Enumerate OT assets by their connectivity contract as well as by IP range: ask which controllers have a SIM, who pays for it, and what that link can reach. The firmware-currency observation is the secondary lesson — devices that nobody can reach to attack are also devices nobody has reached to patch.
