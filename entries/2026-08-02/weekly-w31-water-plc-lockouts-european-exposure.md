---
schema: 1
kind: synthesis
horizon: strategic
title: >
  Water-sector PLC lockouts went from one state to seven inside the week, and the European
  exposure got counted — 86% of 4,117 internet-facing Siemens S7-1200 units sit in four EU
  countries, reached through mobile carriers
headline: >
  Water PLC attacks spread to seven states in W31, and Europe's own controller exposure is now
  quantified
summary: >
  What began as a two-day coordinated attack on more than 30 Minnesota water and wastewater
  utilities became, inside the same week, a federally-confirmed campaign across at least seven US
  states in which attackers reached internet-facing programmable logic controllers, changed their
  IP addresses and passwords, and in at least one case modified the ladder logic itself. No
  vulnerability is involved — the entry point is reachability plus credential control. The horizon
  fact for this constituency is the exposure count published the same day: a Censys scan found
  4,117 internet-exposed Siemens SIMATIC S7-1200 units with 86% of them in Greece, Spain, Italy
  and Austria, each concentration dominated by that country's leading mobile carrier — the
  connectivity path least likely to appear in a scan of corporate address space. No investigating
  body has attributed the activity, and this entry names no actor.
discovered_at: "2026-08-02T23:44:00Z"
updated_at: "2026-08-16T23:59:00Z"
event_date: 2026-07-30
run_id: 2026-08-02T2311Z-weekly
priority: high
immediate_action: null
tags:
  - ot-ics
  - actively-exploited
  - default-config
  - no-patch
  - hacktivism
  - vulnerabilities
  - cisa-kev
regions:
  - us
  - europe
  - global
sectors:
  - water
  - energy
  - public-sector
entities:
  - "incident:minnesota-water-utilities-coordinated-cyberattack-2026-07"
techniques:
  - T1133
  - T1078.001
  - T1531
  - T1565.001
  - T1190
affected_products:
  - Rockwell Automation Allen-Bradley MicroLogix 1100
  - Rockwell Automation Allen-Bradley MicroLogix 1400
  - Siemens SIMATIC S7-1200
  - Rockwell Automation MicroLogix 1100
  - Rockwell Automation MicroLogix 1400
  - Rockwell Automation Studio 5000 Logix Designer
cves:
  - id: CVE-2021-22681
    cvss: 10.0
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - cisa-kev
      - no-patch
      - mitigation-only
    affected: >
      Per CISA advisory ICSA-21-056-03: RSLogix 5000 versions 16 through 20, Studio 5000 Logix
      Designer version 21 and later, and FactoryTalk Security v2.10 and later — the advisory is titled
      Rockwell Automation Logix Controllers
    fixed: >
      No fixed version. CISA records that Rockwell Automation has determined this vulnerability cannot
      be mitigated with a patch; every remediation in the advisory is a mitigation.
sources:
  - url: "https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions"
    publisher: FBI and EPA (joint Public Service Announcement)
    date: 2026-07-30
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs"
    publisher: CISA
    date: 2026-07-30
    role: primary
  - url: "https://censys.com/blog/cisa-alert-water-tower-plc-targeting/"
    publisher: Censys Research
    date: 2026-07-30
    role: corroborating
  - url: "https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/"
    publisher: StateScoop
    date: 2026-07-28
    role: corroborating
  - url: "https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/"
    publisher: SecurityWeek / Associated Press
    date: 2026-07-31
    role: corroborating
  - url: "https://www.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know"
    publisher: Tenable Research Special Operations
    date: 2026-08-06
    role: primary
  - url: "https://therecord.media/iran-cyberattacks-water-treatment"
    publisher: The Record (Recorded Future News)
    date: 2026-08-07
    role: corroborating
  - url: "https://www.dragos.com/blog/water-utility-attacks-decade-of-gaps"
    publisher: Dragos
    date: 2026-08-13
    role: primary
  - url: "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2021/icsa-21-056-03.json"
    publisher: CISA — ICS advisory ICSA-21-056-03 (CSAF)
    date: 2021-02-25
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: CISA Known Exploited Vulnerabilities catalog
    date: 2026-08-16
    role: primary
closed_sources: []
evidence:
  - quote: "After remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality."
    publisher: FBI and EPA (joint Public Service Announcement)
  - quote: At least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites.
    publisher: FBI and EPA (joint Public Service Announcement)
  - quote: "Censys ARC identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200."
    publisher: Censys Research
  - quote: "The FBI stated that reported operational effects have included pressure loss and flooding, and identified Rockwell Automation MicroLogix 1100 and 1400 series PLCs as the targeted devices. The PSA does not attribute the activity to any specific actor, referring only to \"malicious cyber actors.\""
    publisher: Tenable Research Special Operations
  - quote: "activity caused a pressure drop at the Clayton County Water Authority, prompting a boil-water advisory for the utility's 300,000 customers in the Atlanta area. The authority restored service within hours."
    publisher: Tenable Research Special Operations
  - quote: "In Minnesota, it was dozens of PLCs reachable over cellular links, exploitable through a known authentication bypass vulnerability, (CVE-2021-22681) that was first disclosed in 2021 and added to CISA’s Known Exploited Vulnerabilities catalog in March 2026, five years after initial disclosure."
    publisher: Dragos
  - quote: Attackers reached MicroLogix 1100 and 1400 series programmable logic controllers that were directly exposed to the internet through cellular links at water towers and lift stations.
    publisher: Dragos
  - quote: Studio 5000 Logix Designer uses a key to verify Logix controllers are communicating with the affected Rockwell Automation products.
    publisher: CISA — ICS advisory ICSA-21-056-03
  - quote: Successful exploitation of this vulnerability could allow a remote unauthenticated attacker to bypass the verification mechanism and connect with Logix controllers.
    publisher: CISA — ICS advisory ICSA-21-056-03
verification: multi-source
sourcing_note: >
  The campaign scale, the targeted controller families and the access mechanics are cited to the
  FBI/EPA joint announcement that states them; the sector-level consequences and the
  cellular-modem blind spot to CISA's parallel alert; the European exposure counts to the Censys
  scan. Attribution is deliberately absent: neither the FBI/EPA announcement nor the CISA alert
  names an actor, and reporting relayed from the Associated Press records that the FBI has not
  publicly identified a culprit and that Minnesota officials had not either. The Iran framing
  circulating around this story traces to a separate prior advisory about Iranian targeting of the
  sector generally and to one outside expert's advice, neither of which is an attribution of this
  activity — so no actor entity is registered here. The per-city impact classes are attributed to
  the cities StateScoop names rather than generalised across the 30-plus communities; what
  generalises on that page is water quality being unaffected. Censys is cited only for its own
  scan counts, never for its restatement of the CISA alert, which that post itself flags as
  paraphrased from user-supplied content and not independently re-fetched.
confidence: high
references:
  - 2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack
weekly_section: weekly-top-stories
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Inventory Rockwell Automation MicroLogix 1100 and 1400 controllers across water, wastewater and energy estates and establish, per unit, whether it is reachable from outside the operator's own network — including over a mobile-carrier link — and whether it still carries vendor-default access credentials."
updates:
  - at: "2026-08-09T23:45:00Z"
    run_id: 2026-08-09T2315Z-weekly
    type: update
    summary: >
      Status update on the US water-sector PLC lockout campaign a prior weekly consolidated for its
      European exposure. The in-window delta is a targeting fact European operators can act on: per
      Tenable's tracking of the FBI and EPA joint public service announcement of 30 July, the agencies
      identified Rockwell Automation MicroLogix 1100 and 1400 series controllers as the targeted
      devices and recorded operational effects including pressure loss and flooding. CBS independently
      confirmed the twelve-state scope on 6 August, and a pressure drop at the Clayton County Water
      Authority in Georgia prompted a boil-water advisory for the utility's 300,000 customers. No US
      authority has publicly attributed the campaign. The mechanism is unchanged and involves no
      vulnerability — reachability plus credential control.
    fields:
      - actions
      - affected_products
      - evidence
      - references
      - sources
      - tags
      - body
    merged_from: 2026-08-09/weekly-w32-water-plc-lockout-status
  - at: "2026-08-16T23:59:00Z"
    run_id: 2026-08-16T2315Z-weekly
    type: update
    summary: >
      Status update on the US water-sector PLC lockout campaign a prior weekly consolidated for its
      European exposure. The in-window delta is a sourcing problem rather than a technical one. Dragos
      published a decade-spanning retrospective on 13 August comparing the 2013 Bowman Dam intrusion
      to the July 2026 Minnesota campaign, and states the Minnesota controllers were exploitable
      through a known authentication bypass vulnerability, CVE-2021-22681, added to CISA's catalogue
      in March 2026. The catalogue date checks out. The product scope does not: CISA's own ICS
      advisory for that CVE is titled "Rockwell Automation Logix Controllers", describes Studio 5000
      Logix Designer using a key to verify Logix controllers, and lists the affected products as
      RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later, and
      FactoryTalk Security — while the controllers Dragos itself names in the same piece, and that the
      FBI and EPA identified, are MicroLogix 1100 and 1400. No investigating body has named a CVE or
      an actor for these intrusions; the published technique remains reachability plus credential
      control, involving no vulnerability at all.
    fields:
      - affected_products
      - cves
      - evidence
      - references
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-16/weekly-w33-water-plc-lockout-status
migrated_from: null
---

**If you did nothing this week:** an internet-reachable controller in your water, wastewater or municipal estate is exposed to a technique that needs no vulnerability and no exploit — and if it is attached through an integrator's cellular modem, it is probably not in the asset register you would check to find out.

The escalation happened inside seven days. Minnesota's technology bureau announced on 2026-07-28 that more than 30 communities had water and wastewater utilities disrupted by a coordinated attack over 26 and 27 July, with multiple utilities stating water remained safe and no treatment-quality impact reported; where the impact class was described per city it varied — in Plymouth's case the attack was limited to equipment connected via cellular communications at two water towers and multiple lift stations, while Braham's water plant went offline outright ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). Two days later the FBI and EPA put federal scope on it, stating that "since 27 July 2026, Water and Wastewater Sector (WWS) utility companies in at least seven states have reported incidents to the FBI, and some of that activity degraded water operations" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)), and naming the targeted hardware as Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 series controllers ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

The mechanics are the reason this is a strategic item rather than a vulnerability item. The announcement records that "after remotely accessing internet-facing devices, the actors changed the IP addresses and passwords, resulting in a loss of monitoring and control functionality" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)) — reachability and credential control, with no CVE in the chain, which means no patch cycle closes it and no vulnerability scanner reports it. Integrity, not just availability, was touched in at least one case: "at least one organization reported modified PLC project files after noticing ladder logic discrepancies across several sites" ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)). CISA's parallel alert adds the sector-scale consequence, stating the activity "has resulted in boil water notices and sustained manual operations", and singles out cellular modems installed by operators, vendors or system integrators as a routine blind spot because those connections may be undocumented and excluded from attack-surface scans ([CISA, 2026-07-30](https://www.cisa.gov/news-events/alerts/2026/07/30/cisa-urges-water-and-wastewater-systems-sector-protect-ot-against-activity-targeting-plcs)). The FBI also names a supplier-homogeneity multiplier that transfers directly to European municipal estates, noting that across several victims, similarities in network setup provided by third parties may let an actor multiply successes where the same vulnerable setups recur across a provider's customers ([FBI and EPA, 2026-07-30](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions)).

For a Swiss or European defender the decisive in-window fact is that the exposure is now measured rather than assumed, and it sits on a different vendor's hardware. Censys reported on 2026-07-30 that it "identified 4,117 Internet-exposed hosts that fingerprint as Siemens SIMATIC S7-1200", and that "exposure concentrates heavily in southern and central Europe: Greece, Spain, Italy, and Austria together account for 86.0% of the total, each dominated by that country's leading mobile carrier rather than fixed-line or hosting providers" ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)). That carrier concentration is precisely the class of connectivity CISA flags as unscanned, on controllers in EU member states, for a technique that requires only reachability. Censys is careful about what the scan is: it frames the whole exercise as an exposure characterisation that does not confirm any specific host is a victim of the activity CISA describes ([Censys Research, 2026-07-30](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)).

Attribution has not merely been withheld — it has been declined. Reporting relaying the Associated Press records that the FBI "has not publicly identified a culprit and a spokesperson declined to say Thursday who the bureau thought might be responsible", and that "Minnesota IT Services said state officials had yet to identify who was behind the attacks" ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). The Iran framing in circulation has two origins, neither of which is a finding about this campaign: a prior multi-agency advisory concerning Iranian targeting of the water sector in general, and an outside expert quoted in the same AP report advising defenders to treat it as Iran until proven otherwise ([SecurityWeek / AP, 2026-07-31](https://www.securityweek.com/cyberattacks-on-minnesota-water-systems-investigated-as-officials-warn-about-iranian-hackers/)). Reading the calendar as evidence would be a mistake, and it is also unnecessary: nothing about the defensive work depends on who is doing it.

**Defender takeaway:** the transferable content is the exposure inventory, not the geography of the victims. The controller family with the heaviest European internet exposure belongs to a different vendor than the one under attack in the United States, and its exposure runs through mobile carriers — so an inventory pass scoped to the corporate address space will report all-clear while the actual exposure sits on an APN. Because the technique consumes no vulnerability, the question to answer is reachability, and the answer has to include every field device an integrator or vendor connected on your behalf.

**Triage:** an engineer legitimately changes a controller's IP address and sets a password during commissioning or a modem swap, so those events alone are not the signal. The discriminators are provenance, timing and reversibility: the change arrives from outside the engineering-workstation range or over the cellular path rather than the engineering VLAN, it lands outside a change window with no work order, and the password that was set is one operations cannot subsequently authenticate with — a lockout rather than a rotation. A project-file or ladder-logic checksum that moves with no matching download record from a known engineering host is the higher-confidence version of the same test, and the FBI's account of discrepancies noticed across several sites argues for comparing logic across the fleet rather than device by device.

## Update — 2026-08-09T23:45:00Z

The prior weekly consolidated this campaign for its European exposure, on the observation that the entry point is reachability plus credential control rather than any vulnerability, and that a scan had counted thousands of internet-exposed programmable logic controllers in EU countries concentrated behind mobile carriers. Three things changed inside 2026-W32, and only one of them is directly actionable outside the United States.

The actionable one is a device family. Per Tenable's tracking of the FBI and EPA joint public service announcement issued on 30 July, "the FBI stated that reported operational effects have included pressure loss and flooding, and identified Rockwell Automation MicroLogix 1100 and 1400 series PLCs as the targeted devices" ([Tenable Research Special Operations, 2026-08-06](https://www.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know)). Until this week the campaign had been described to defenders in terms of what the attackers did — changing controller addresses and passwords, in at least one case modifying ladder logic — without a controller family to inventory against. A European water or wastewater operator now has a concrete, bounded question to answer about its own estate rather than a general exhortation about exposure.

The second is scale of consequence. The same source records that the "activity caused a pressure drop at the Clayton County Water Authority, prompting a boil-water advisory for the utility's 300,000 customers in the Atlanta area. The authority restored service within hours." The pipeline covered Clayton County's own confirmation on 6 August; the population figure is the part that was not carried, and it is the largest disclosed single-utility impact of the campaign. Tenable also records that CBS independently confirmed the twelve-state scope on 6 August, following the ABC report of 4 August that first put the count there.

The third is a gap that has now persisted long enough to be a finding in its own right. No US authority has publicly attributed the campaign: the joint announcement "does not attribute the activity to any specific actor, referring only to 'malicious cyber actors'," even as reporting describes a campaign allegedly linked to Iranian hackers and records that, while federal agencies have declined to publicly attribute the attacks, multiple sources pointed the finger at Iran ([The Record, 2026-08-07](https://therecord.media/iran-cyberattacks-water-treatment)). For a European defender the practical effect is that no sanctions listing, no joint advisory naming a cluster, and no attributed threat profile will arrive to trigger internal escalation processes keyed on those things — the exposure-reduction work has to be justified on the mechanism alone.

**Defender takeaway:** nothing about the mechanism has changed and that is precisely why the device naming matters. This campaign requires no exploit and no malware, so patching contributes nothing; the controls are inventory and reachability. The prior weekly's exposure count established that the European equivalent of this attack surface reaches controllers over mobile-carrier connections rather than corporate address space, which means an external scan of the organisation's own IP ranges will not find them — the inventory has to come from the engineering side, asset by asset and link by link.

## Update — 2026-08-16T23:59:00Z

The prior weekly recorded the water-sector PLC lockout campaign in a state that had held since it began — a device family European operators could inventory, an operational effect on real utilities, and an attribution that no US authority would make. This week produced the campaign's first vendor attribution to a specific vulnerability, and it does not survive a check against that vulnerability's own record.

Dragos published a decade-spanning retrospective on 13 August setting the 2013 Bowman Dam intrusion against the July 2026 Minnesota campaign. Its description of the target is consistent with everything published before: "Attackers reached MicroLogix 1100 and 1400 series programmable logic controllers that were directly exposed to the internet through cellular links at water towers and lift stations." The new claim is the mechanism: "In Minnesota, it was dozens of PLCs reachable over cellular links, exploitable through a known authentication bypass vulnerability, (CVE-2021-22681) that was first disclosed in 2021 and added to CISA's Known Exploited Vulnerabilities catalog in March 2026, five years after initial disclosure" ([Dragos, 2026-08-13](https://www.dragos.com/blog/water-utility-attacks-decade-of-gaps)). Half of that checks out: CISA added CVE-2021-22681 to the catalogue on 5 March 2026 ([CISA Known Exploited Vulnerabilities catalog, 2026-08-16](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

The product scope does not. CISA's own ICS advisory for that CVE is titled "Rockwell Automation Logix Controllers", and states that "Studio 5000 Logix Designer uses a key to verify Logix controllers are communicating with the affected Rockwell Automation products", with successful exploitation allowing "a remote unauthenticated attacker to bypass the verification mechanism and connect with Logix controllers". The products it lists as affected are RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later, and FactoryTalk Security version 2.10 and later ([CISA ICS advisory ICSA-21-056-03, 2021-02-25](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2021/icsa-21-056-03.json)). MicroLogix appears nowhere in it, and the flaw concerns a key used by Rockwell's Logix engineering software to verify Logix controllers — a different product line and a different mechanism from the MicroLogix 1100 and 1400 units Dragos names two paragraphs earlier. CISA's catalogue summary frames it the same way, around Studio 5000 Logix Designer and Logix controllers. The same advisory records a second divergence from Dragos's account that is worth stating given this entry's subject: Dragos gives the flaw a CVSS score of 9.8, while CISA's advisory reads "A CVSS v3 base score of 10.0 has been calculated". This entry carries CISA's 10.0, and notes that the advisory also records that Rockwell "has determined this vulnerability cannot be mitigated with a patch" — so a reader who took the retrospective's framing and went looking for a patch to apply would find none. What the FBI and EPA have published about Minnesota, and what this pipeline recorded from that reporting, describes no vulnerability at all: attackers reached internet-exposed controllers, changed their IP addresses and passwords, and locked operators out — reachability plus credential control.

**Defender takeaway:** the operational consequence for a European water or wastewater operator is that this campaign still gives you nothing to patch, and a vendor claim that it does should not redirect the work. The controls that address the published technique are architectural — whether any controller answers on a routable address, whether the cellular or carrier-provided path is treated as untrusted, and whether default or weak credentials survive on management interfaces — and none of them are a patch cycle. The wider point is a sourcing habit worth applying generally: a CVE identifier in a vendor narrative is a claim like any other, and it is cheap to check against the CVE's own affected-product list. Here the check takes one page load and changes the conclusion, and the same check applied to an internal inventory would prevent an operator from concluding their MicroLogix estate is covered because they patched something else. This pipeline separately recorded a genuinely MicroLogix-relevant flaw, CVE-2017-16740, present in firmware on 19 of 22 devices one census found in campaign-targeted cities — that one is not in the KEV catalogue, and no source claims it was exploited either.

**Triage:** unchanged from prior coverage, because the technique is unchanged. The observables for this campaign are administrative rather than exploit-shaped: a controller-mode or configuration change with no corresponding maintenance window, a management session to a field device originating from outside the engineering workstation subnet — particularly from the carrier-side of a cellular router rather than from the operator's own network — and credential or network-configuration changes on a controller that the engineering team cannot attribute to a change record. Legitimate remote maintenance produces the same protocol events, which is why origin and change-record correlation, not the event type, is what separates them.
