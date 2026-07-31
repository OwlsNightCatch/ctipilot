---
schema: 1
kind: incident
horizon: operational
title: "UK Department for Education confirms a breach of two public-facing portals and a police legal database, claimed by ExfilSquad — a five-day-old extortion brand whose other 14 claims look fabricated"
headline: "One confirmed government breach inside a leak-site victim list that a threat-intel vendor assesses is more likely invented than real"
summary: >
  The UK Department for Education confirmed that two of its public-facing portals — the DfE Help Desk
  Self-Service Portal and the Turing Scheme Portal — were compromised, exposing customer-service contact details,
  and that the Police National Legal Database was affected with 135,000 records naming officers, their forces and
  work email addresses. DfE pushes back on the criminals' own scale figure, clarifying that the claimed 600,000
  pieces of data are lines of data rather than individuals, and assesses the risk to individuals as not high. The
  claimant is ExfilSquad, whose Tor leak site first appeared on 2026-07-26 with 15 named victims; SOCRadar
  assesses that fabrication currently appears more likely than genuine compromise for the list as a whole. The
  operational lesson is the gap between the two facts.
discovered_at: "2026-07-31T04:09:14Z"
event_date: "2026-07-30"
run_id: 2026-07-31T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime]
regions: [uk, europe]
sectors: [public-sector, education]
entities: [actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07]
techniques: [T1213, T1190]
affected_products: []
cves: []
sources:
  - url: "https://therecord.media/united-kingdom-ransomware-education"
    publisher: "The Record (Recorded Future News)"
    date: "2026-07-30"
    role: primary
  - url: "https://socradar.io/blog/dark-web-profile-exfilsquad/"
    publisher: "SOCRadar"
    date: "2026-07-28"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/"
    publisher: "BleepingComputer"
    date: "2026-07-30"
    role: corroborating
  - url: "https://www.sec.gov/Archives/edgar/data/6281/000119312526324223/d158253d8k.htm"
    publisher: "Analog Devices, Inc. — SEC Form 8-K"
    date: "2026-07-29"
    role: corroborating
  - url: "https://cyberinsider.com/analog-devices-says-hackers-stole-company-files-in-june-cyberattack/"
    publisher: "CyberInsider"
    date: "2026-07-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "135,000 pieces of data potentially identifying the names, forces and work email addresses of police officers"
    publisher: "The Record (Recorded Future News)"
  - quote: "the listings may involve reused data or fabricated allegations, with fabrication currently appearing more likely"
    publisher: "SOCRadar"
verification: multi-source
sourcing_note: >
  The confirmed breach facts come from a DfE spokesperson quoted directly by The Record; the credibility
  assessment of the wider victim list is SOCRadar's. The two are deliberately kept apart in the body because they
  support different conclusions. The Analog Devices thread is cited per clause to the three separate sources that
  carry its parts — the delisting to the outlet that observed it, the intrusion and materiality wording to the
  company's own filing, and the claimed record count to the outlet that reports it as the group's allegation —
  because SOCRadar's profile, which lists the company among the 15 claims, carries none of them. The Home Office, which owns the police legal database rather than DfE, declined
  to comment on that element, so its scope rests on The Record's reporting and the NCSC's confirmation that it is
  supporting the response.
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

The UK Department for Education has confirmed a breach of two public-facing portals, the DfE Help Desk Self-Service Portal and the Turing Scheme Portal, with the compromised material described as customer-service contact details — names, email addresses and phone numbers belonging to parents, officials, school leaders and university staff ([The Record, 2026-07-30](https://therecord.media/united-kingdom-ransomware-education)). Separately affected was the Police National Legal Database, where 135,000 records identify police officers by name, force and work email address; The Record notes the database holds no protected information from investigations or witnesses, and that the Home Office, which owns it, declined to comment. The NCSC has confirmed it is supporting law enforcement colleagues on the response. The extortionists are demanding a ransom; The Record notes that as a matter of policy the British government does not make ransom payments, and that the government has moved forward with plans, not yet law, to make such payments illegal for public-sector entities.

Two details in DfE's own response are worth carrying rather than the headline number. It explicitly corrects the criminals' framing, clarifying that the claimed figure of more than 600,000 pieces of data refers to lines of data rather than the count of individuals affected — a victim disputing the arithmetic behind an extortion claim rather than repeating it. And it assesses the risk to individuals as not high, which is consistent with contact-detail exposure rather than anything more sensitive.

**The claimant is where this gets interesting.** ExfilSquad's Tor leak site first appeared on 2026-07-26 and immediately listed 15 organisations across government, education, finance and technology. SOCRadar's profile of the group is unusually direct about what that list is worth: it assesses that the listings may involve reused data or fabricated allegations, with fabrication currently appearing more likely ([SOCRadar, 2026-07-28](https://socradar.io/blog/dark-web-profile-exfilsquad/)). No forensic evidence, data samples, victim confirmations or technical detail about initial access are publicly available for the group, and SOCRadar found no aliases, predecessor operations or rebranding history — this is a brand with no track record at all. It also documents the group posting on social media tagging a major vendor's security-intelligence account with a screenshot resembling an internal directory record, authenticity unconfirmed, which reads as publicity-seeking rather than proof.

So the same list contains one independently confirmed national-government breach and fourteen claims a credible vendor thinks are probably invented. One of the listed companies, semiconductor manufacturer Analog Devices, was added and then quietly removed — the outlet that reported the removal says the reason is unknown and notes that delisting is common when ransom negotiations begin ([BleepingComputer, 2026-07-30](https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/)). Analog Devices separately filed a regulatory disclosure stating it identified unauthorized access to certain systems on 23 June 2026, that its investigation found certain files were exfiltrated, and that it does not believe the incident is reasonably likely to materially impact its business — filed under the non-material "Other Events" item despite the acknowledged exfiltration, which is itself a useful materiality-threshold data point for anyone calibrating their own disclosure playbook ([Analog Devices, 2026-07-29](https://www.sec.gov/Archives/edgar/data/6281/000119312526324223/d158253d8k.htm)). The company has not attributed that intrusion to ExfilSquad or confirmed the group's claims are related, and the record count circulating alongside it is the group's own allegation rather than a company figure ([CyberInsider, 2026-07-30](https://cyberinsider.com/analog-devices-says-hackers-stole-company-files-in-june-cyberattack/)). Those are two threads, and the available reporting does not join them.

**Defender takeaway:** the transferable item here is a triage discipline, not an indicator. When a new extortion brand appears with a long victim list, the volume of claims is not evidence — the base rate for a five-day-old handle with no history is heavily weighted toward recycled or invented data, and acting on a listing before victim or regulator confirmation means spending analyst hours on someone's marketing. The workable test is what happened here: one entry on the list was corroborated by the victim itself, so it is real and scoped; the rest stay unactioned until something outside the leak site says otherwise. The secondary point for the constituency is that both confirmed elements were externally-reachable service portals holding contact data — the sort of help-desk and scheme-administration systems that rarely appear on a crown-jewels inventory but sit on the public internet with real personal data behind them.
