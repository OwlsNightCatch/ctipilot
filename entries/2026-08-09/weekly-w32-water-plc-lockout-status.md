---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Water-sector PLC lockout status: the FBI has now named the targeted controller family — Rockwell MicroLogix 1100 and 1400 — while still declining to name an actor, and a 300,000-customer boil-water advisory in Georgia is the largest disclosed population impact so far"
headline: "Water campaign status — a device family European operators can inventory, and an attribution that no US authority will make"
summary: >
  Status update on the US water-sector PLC lockout campaign a prior weekly consolidated for its European
  exposure. The in-window delta is a targeting fact European operators can act on: per Tenable's tracking of
  the FBI and EPA joint public service announcement of 30 July, the agencies identified Rockwell Automation
  MicroLogix 1100 and 1400 series controllers as the targeted devices and recorded operational effects
  including pressure loss and flooding. CBS independently confirmed the twelve-state scope on 6 August, and
  a pressure drop at the Clayton County Water Authority in Georgia prompted a boil-water advisory for the
  utility's 300,000 customers. No US authority has publicly attributed the campaign. The mechanism is
  unchanged and involves no vulnerability — reachability plus credential control.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-06"
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags: [ot-ics, default-config, hacktivism]
regions: [us, europe, global]
sectors: [water, public-sector, energy]
entities:
  - incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
techniques: [T1133, T1078.001]
affected_products: ["Rockwell Automation MicroLogix 1100", "Rockwell Automation MicroLogix 1400"]
cves: []
sources:
  - url: "https://www.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know"
    publisher: "Tenable Research Special Operations"
    date: "2026-08-06"
    role: primary
  - url: "https://therecord.media/iran-cyberattacks-water-treatment"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The FBI stated that reported operational effects have included pressure loss and flooding, and identified Rockwell Automation MicroLogix 1100 and 1400 series PLCs as the targeted devices. The PSA does not attribute the activity to any specific actor, referring only to \"malicious cyber actors.\""
    publisher: "Tenable Research Special Operations"
  - quote: "activity caused a pressure drop at the Clayton County Water Authority, prompting a boil-water advisory for the utility's 300,000 customers in the Atlanta area. The authority restored service within hours."
    publisher: "Tenable Research Special Operations"
verification: multi-source
sourcing_note: >
  The FBI and EPA joint public service announcement (Alert I-073026-PSA, 2026-07-30) is the authority for the
  device naming and the operational effects, but a direct fetch of the IC3 page returned no usable content in
  this run; the facts are therefore cited to Tenable's continuously-updated tracking page, which states them
  as the FBI's, rather than presented as read from the PSA itself. That page was first published 2026-07-28
  and last updated 2026-08-06, and the 2026-08-06 update is what carries the in-window facts used here.
confidence: medium
update_of: 2026-08-02/weekly-w31-water-plc-lockouts-european-exposure
references:
  - 2026-08-06/water-plc-lockouts-twelve-states-named-utility-confirms
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory Rockwell Automation MicroLogix 1100 and 1400 controllers across water, wastewater and energy estates and establish, per unit, whether it is reachable from outside the operator's own network — including over a mobile-carrier link — and whether it still carries vendor-default access credentials."
migrated_from: null
---

**UPDATE (originally covered 2026-08-02):** the prior weekly consolidated this campaign for its European exposure, on the observation that the entry point is reachability plus credential control rather than any vulnerability, and that a scan had counted thousands of internet-exposed programmable logic controllers in EU countries concentrated behind mobile carriers. Three things changed inside 2026-W32, and only one of them is directly actionable outside the United States.

The actionable one is a device family. Per Tenable's tracking of the FBI and EPA joint public service announcement issued on 30 July, "the FBI stated that reported operational effects have included pressure loss and flooding, and identified Rockwell Automation MicroLogix 1100 and 1400 series PLCs as the targeted devices" ([Tenable Research Special Operations, 2026-08-06](https://www.tenable.com/blog/coordinated-cyberattack-on-minnesota-water-utilities-what-you-need-to-know)). Until this week the campaign had been described to defenders in terms of what the attackers did — changing controller addresses and passwords, in at least one case modifying ladder logic — without a controller family to inventory against. A European water or wastewater operator now has a concrete, bounded question to answer about its own estate rather than a general exhortation about exposure.

The second is scale of consequence. The same source records that the "activity caused a pressure drop at the Clayton County Water Authority, prompting a boil-water advisory for the utility's 300,000 customers in the Atlanta area. The authority restored service within hours." The pipeline covered Clayton County's own confirmation on 6 August; the population figure is the part that was not carried, and it is the largest disclosed single-utility impact of the campaign. Tenable also records that CBS independently confirmed the twelve-state scope on 6 August, following the ABC report of 4 August that first put the count there.

The third is a gap that has now persisted long enough to be a finding in its own right. No US authority has publicly attributed the campaign: the joint announcement "does not attribute the activity to any specific actor, referring only to 'malicious cyber actors'," even as reporting describes a campaign allegedly linked to Iranian hackers and records that, while federal agencies have declined to publicly attribute the attacks, multiple sources pointed the finger at Iran ([The Record, 2026-08-07](https://therecord.media/iran-cyberattacks-water-treatment)). For a European defender the practical effect is that no sanctions listing, no joint advisory naming a cluster, and no attributed threat profile will arrive to trigger internal escalation processes keyed on those things — the exposure-reduction work has to be justified on the mechanism alone.

**Defender takeaway:** nothing about the mechanism has changed and that is precisely why the device naming matters. This campaign requires no exploit and no malware, so patching contributes nothing; the controls are inventory and reachability. The prior weekly's exposure count established that the European equivalent of this attack surface reaches controllers over mobile-carrier connections rather than corporate address space, which means an external scan of the organisation's own IP ranges will not find them — the inventory has to come from the engineering side, asset by asset and link by link.
