---
schema: 1
kind: incident
horizon: operational
title: "Coordinated two-day cyberattack disrupts operational technology at 30+ Minnesota water and wastewater utilities — no authority has attributed it"
headline: "Minnesota confirms a coordinated attack on field OT at more than 30 community water systems, days after a US advisory update on internet-exposed PLCs"
summary: >
  Minnesota IT Services announced on 2026-07-28 that more than 30 communities had water and wastewater
  utilities disrupted by a coordinated cyberattack over 26–27 July, affecting programmable logic
  controllers and cellular-connected equipment at water towers and lift stations. Plymouth disconnected
  affected cellular equipment from its network; Braham's water plant went offline and the city briefly
  asked residents to minimise use because its tower held a limited quantity; South St. Paul reported
  impact to certain automated controls with no major effect on treatment operations. No source reports impact to drinking-water safety or treatment
  quality. Attribution is explicitly open — the affected city says "unknown actors" and the Center for
  Internet Security states the attacks have not been attributed and it is unclear whether the PLC vector
  a recent US joint advisory warned about was involved. That advisory's documented tradecraft is what
  makes this transferable: it needs no CVE, only an internet-reachable controller.
discovered_at: "2026-07-29T05:45:00Z"
event_date: "2026-07-27"
run_id: 2026-07-29T0408Z-intel
priority: high
immediate_action: null
tags: [ot-ics]
regions: [us, global]
sectors: [water, energy, public-sector]
entities: [incident:minnesota-water-utilities-coordinated-cyberattack-2026-07]
techniques: [T1133, T1565, T1041]
affected_products: []
cves: []
sources:
  - url: "https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/"
    publisher: "StateScoop"
    date: "2026-07-28"
    role: primary
  - url: "https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/"
    publisher: "Cybersecurity Dive"
    date: "2026-07-28"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a"
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Analysis indicated the project file retained ladder logic for downstream function but added logic that overrode specific instruction sets responsible for maintaining safe operating parameters in the victim's environment."
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
  - quote: "the changes disabled critical shutdown and alarm logic, allowing systems to enter unsafe conditions without notifying operators of the anomalies."
    publisher: "CISA, FBI, NSA, EPA, DOE, CNMF and Treasury (joint advisory AA26-097A)"
  - quote: "The two-day attack comes days after federal officials warned of state-linked threat groups targeting a wider set of industrial devices."
    publisher: "Cybersecurity Dive"
verification: multi-source
sourcing_note: >
  Two independent outlets reporting the same event with named official and municipal statements, plus the
  joint advisory as background. The attribution boundary is the critical sourcing point and is held
  deliberately: no named authority — not the FBI, CISA, EPA, Minnesota IT Services, nor any affected city
  — has attributed the Minnesota attack to any actor. Braham's own statement says "unknown actors"; the
  Center for Internet Security's threat-intelligence director states the attacks have not been attributed
  to any particular party and that it is unclear whether the PLC vector CISA warned about was involved.
  Where press coverage places Iran near this story it does so as contextual juxtaposition with the
  concurrently updated AA26-097A advisory — one outlet's remark that Iran "is a reasonable guess" is that
  reporter's own inference, not an official claim, and is not repeated here as fact. AA26-097A describes a
  separate, ongoing nationwide campaign and is cited only for the tradecraft and mitigations it documents,
  never as reporting on this incident. Its indicator tables, including the IP addresses CISA itself
  advises vetting before blocking, are omitted. One nuance between the two outlets is reconciled in the
  body: Braham did briefly ask residents to minimise water use because of tank level, which the broader
  "no usage changes requested" framing does not capture. `affected_products` is deliberately empty and the
  entry carries no state-nexus tag: no source names any controller model involved in the Minnesota event,
  and no source attributes it to any actor. The four controller families the joint advisory names are
  targets of that separate campaign and are recorded on the entry covering it, not asserted here.
confidence: medium
update_of: null
references: [2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion]
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
migrated_from: null
---

The confirmed facts are narrow and worth stating precisely. Minnesota's technology bureau announced on 2026-07-28 that more than 30 communities had their water and wastewater utilities disrupted by a coordinated cyberattack on 26 and 27 July ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)), a two-day event rather than a single-utility incident ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). Where individual utilities described impact, it fell on field equipment rather than treatment processes: Plymouth stated the attack was limited to equipment connected via cellular communications at two water towers and multiple lift stations, and disconnected that equipment from the network to stop the attack and avoid retargeting during reconfiguration; Braham's water plant went offline, and the city later stated the outage was the result of a malicious cyberattack of computerised operating systems by unknown actors ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). Braham did ask residents to minimise water use while its tower held a limited quantity, and a later notice reported the plant back online ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)) — a real if temporary consumption instruction. Separately, authorities in South St. Paul said they identified a cyberattack on Monday that impacted certain automated controls, and after implementing contingency procedures confirmed no major impact to drinking and wastewater treatment operations ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). Multiple utilities stated water remained safe and no treatment-quality impact has been reported. Minnesota IT Services coordinated a response alongside the FBI, CISA and the EPA, with its chief information security officer describing a whole-of-government response that helped prevent more serious impacts ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)).

What is *not* established matters as much. No authority has named an actor. The Center for Internet Security's senior director of threat intelligence stated the Minnesota attacks have not yet been attributed to any particular party and that it is unclear whether the programmable logic controllers CISA had warned about were involved, and separately noted that of the nation-state attacks on US water facilities in recent years, none has documented major downstream health impacts ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/)). The FBI confirmed only that it is aware and in contact with victims ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)). The reason Iran appears in coverage of this event is timing: the attack landed days after federal officials warned of state-linked groups targeting a wider set of industrial devices ([Cybersecurity Dive, 2026-07-28](https://www.cybersecuritydive.com/news/authorities-investigating-a-coordinated-cyberattack-against-minnesota-water/826427/)) — a juxtaposition, not a finding. Treating it as attribution would be reading the calendar as evidence.

The transferable content sits in that separate advisory, and it is why this belongs in front of European water and energy operators despite the victims being American. AA26-097A documents actors using leased third-party infrastructure and the vendors' *own* engineering software — Rockwell Studio 5000 Logix Designer, Schneider EcoStruxure Control Expert, Siemens TIA Portal — to reach misconfigured, internet-facing controllers and pull down device project files, then re-upload files with modified or deleted logic ([CISA and partners, 2026-07-22](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)). At one victim the FBI observed a malicious project file downloaded to a PLC that retained ladder logic for downstream function but added logic overriding the instruction sets responsible for maintaining safe operating parameters, and the changes disabled critical shutdown and alarm logic, allowing systems to enter unsafe conditions without notifying operators ([CISA and partners, 2026-07-22](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)). CISA is explicit that this represents no new vulnerability in the named products — it is opportunistic targeting of misconfiguration. The affected controller families are the same Rockwell, Schneider and Siemens lines that run European water, wastewater and district-energy plants, and in one instance access came through Dropbear SSH on a victim's *modem*, which is precisely the class of device Plymouth found affected.

**Defender takeaway:** the exposure this describes cannot be closed by patching, because there is nothing vulnerable to patch — a controller reachable from the internet with vendor engineering software able to talk to it is the whole attack surface, and a cellular modem at an unstaffed lift station is as much a perimeter as any firewall. Two things follow. First, the inventory question ("which of our controllers and field modems can be reached from outside, including over cellular?") is answerable this week and is the actual control. Second, integrity of logic becomes a monitoring target in its own right: because the documented impact silently removes shutdown and alarm behaviour, an operator watching only for alarms would see a quieter plant, not a compromised one, so periodic comparison of running project files against known-good logic — Add-On Instructions included — is the detection that catches this class rather than the alerting the attacker just disabled.

**Triage:** engineering software connecting to a PLC and writing a project file is exactly what commissioning and maintenance look like, so the activity class is not the signal. The discriminators the advisory's own mechanics supply are provenance and timing: a project-file write originating from outside the engineering network or from leased hosting rather than an engineering workstation; a controller left in program or remote mode outside a change window rather than in RUN; and a logic change with no corresponding maintenance record. On the network side, protocol functions that modify programs or change controller mode are the ones to surface — connection attempts to controller-associated ports are ubiquitous background noise, whereas a mode change or program write is a discrete, auditable act.
