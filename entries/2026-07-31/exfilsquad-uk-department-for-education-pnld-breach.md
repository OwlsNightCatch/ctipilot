---
schema: 1
kind: incident
horizon: operational
title: >
  UK Department for Education confirms a breach of two public-facing portals and a police legal
  database, claimed by ExfilSquad — a five-day-old extortion brand whose other 14 claims look
  fabricated
headline: >
  One confirmed government breach inside a leak-site victim list that a threat-intel vendor
  assesses is more likely invented than real
summary: >
  The UK Department for Education confirmed that two of its public-facing portals — the DfE Help
  Desk Self-Service Portal and the Turing Scheme Portal — were compromised, exposing
  customer-service contact details, and that the Police National Legal Database was affected with
  135,000 records naming officers, their forces and work email addresses. DfE pushes back on the
  criminals' own scale figure, clarifying that the claimed 600,000 pieces of data are lines of
  data rather than individuals, and assesses the risk to individuals as not high. The claimant is
  ExfilSquad, whose Tor leak site first appeared on 2026-07-26 with 15 named victims; SOCRadar
  assesses that fabrication currently appears more likely than genuine compromise for the list as
  a whole. The operational lesson is the gap between the two facts.
discovered_at: "2026-07-31T04:09:14Z"
updated_at: "2026-08-16T04:45:00Z"
event_date: 2026-07-30
run_id: 2026-07-31T0409Z-intel
priority: high
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - cloud
  - identity
  - actively-exploited
  - default-config
  - info-disclosure
regions:
  - uk
  - europe
  - switzerland
  - global
  - us
sectors:
  - public-sector
  - education
  - defense
  - technology
  - retail
  - finance
  - manufacturing
entities:
  - "actor:exfilsquad"
  - "incident:uk-dfe-exfilsquad-breach-2026-07"
techniques:
  - T1213
  - T1190
  - T1530
  - T1078.004
affected_products:
  - Microsoft Power Pages
  - Microsoft Dataverse
  - Microsoft Power Apps
  - Microsoft Power Apps Portals
  - Microsoft Dynamics 365
cves: []
sources:
  - url: "https://therecord.media/united-kingdom-ransomware-education"
    publisher: The Record (Recorded Future News)
    date: 2026-07-30
    role: primary
  - url: "https://socradar.io/blog/dark-web-profile-exfilsquad/"
    publisher: SOCRadar
    date: 2026-07-28
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/"
    publisher: BleepingComputer
    date: 2026-07-30
    role: corroborating
  - url: "https://www.sec.gov/Archives/edgar/data/6281/000119312526324223/d158253d8k.htm"
    publisher: "Analog Devices, Inc. — SEC Form 8-K"
    date: 2026-07-29
    role: corroborating
  - url: "https://cyberinsider.com/analog-devices-says-hackers-stole-company-files-in-june-cyberattack/"
    publisher: CyberInsider
    date: 2026-07-30
    role: corroborating
  - url: "https://www.pnld.co.uk/~/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f"
    publisher: Police National Legal Database (West Yorkshire Police)
    date: 2026-08-03
    role: primary
  - url: "https://venarix.com/blog/exfilsquad-targets-misconfigured-microsoft-power-pages-portals"
    publisher: VenariX
    date: 2026-07-29
    role: primary
  - url: "https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html"
    publisher: The Hacker News
    date: 2026-08-03
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12823"
    publisher: NCSC Switzerland / GovCERT.ch
    date: 2026-08-04
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/"
    publisher: BleepingComputer
    date: 2026-08-11
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/"
    publisher: Infosecurity Magazine
    date: 2026-08-14
    role: primary
  - url: "https://www.cybersecuritydive.com/news/researchers-confirm-breach-claims-data-extortion/827926/"
    publisher: Cybersecurity Dive
    date: 2026-08-14
    role: corroborating
closed_sources: []
evidence:
  - quote: "135,000 pieces of data potentially identifying the names, forces and work email addresses of police officers"
    publisher: The Record (Recorded Future News)
  - quote: "the listings may involve reused data or fabricated allegations, with fabrication currently appearing more likely"
    publisher: SOCRadar
  - quote: "Information including the names, organisations and work email addresses of police officers, staff and other criminal justice professionals, government partners and customers has been compromised and published on the dark web."
    publisher: Police National Legal Database
  - quote: There is no evidence to suggest that passwords or other security credentials have been compromised.
    publisher: Police National Legal Database
  - quote: "VenariX has not identified evidence of ransomware deployment, malware use, lateral movement, or exploitation of a software vulnerability."
    publisher: VenariX
  - quote: "That is a user-base figure, not a breach-victim count."
    publisher: The Hacker News
  - quote: "At this stage, the Power Pages link remains a hypothesis to test rather than an explanation of the PNLD breach."
    publisher: The Hacker News
  - quote: "Unauthenticated attackers can access and exfiltrate sensitive personal, financial, and organizational data from public-facing portals via exposed Dataverse tables."
    publisher: NCSC Switzerland / GovCERT.ch
  - quote: "Current exploitation status: Actively Exploited"
    publisher: NCSC Switzerland / GovCERT.ch
  - quote: "We have worked with our cloud CRM vendor on the matter, and we do not believe that there is a risk to sensitive data."
    publisher: "Wesco International, via BleepingComputer"
  - quote: found no evidence of ransomware or other malicious software on its IT systems
    publisher: BleepingComputer
  - quote: The leading theory on the initial attack vector that enabled exfiltration is misconfigured Microsoft Power Page portals that allowed for public read access
    publisher: "Fortra FIRE, quoted by Infosecurity Magazine"
  - quote: "it was able to identify over 10,000 potential Power Pages instances accessible to the public"
    publisher: "Infosecurity Magazine, reporting Fortra's research"
  - quote: the total data was reported to be 382.64 GB and 27 million records across the 13 victims
    publisher: Infosecurity Magazine
verification: multi-source
sourcing_note: >
  The confirmed breach facts come from a DfE spokesperson quoted directly by The Record; the
  credibility assessment of the wider victim list is SOCRadar's. The two are deliberately kept
  apart in the body because they support different conclusions. The Analog Devices thread is cited
  per clause to the three separate sources that carry its parts — the delisting to the outlet that
  observed it, the intrusion and materiality wording to the company's own filing, and the claimed
  record count to the outlet that reports it as the group's allegation — because SOCRadar's
  profile, which lists the company among the 15 claims, carries none of them. The Home Office,
  which owns the police legal database rather than DfE, declined to comment on that element, so
  its scope rests on The Record's reporting and the NCSC's confirmation that it is supporting the
  response.
confidence: medium
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "From an unauthenticated browser session, request /_api/contacts, /_api/accounts, /_api/incidents, /_api/emails, /_api/annotations and /_odata against every externally-reachable Power Pages or Power Apps portal your organisation operates, and treat any 200 response returning record bodies as a live data exposure to close today by removing table permissions from the Anonymous Users web role."
  - "Enumerate every public-facing Power Pages and Power Apps Portals site in the estate and request its Web API and OData endpoints from an unauthenticated browser session, comparing the tables that return records against the set the portal is meant to expose — the advisory frames this as verification to perform, not an alert to wait for."
updates:
  - at: "2026-08-04T04:49:00Z"
    run_id: 2026-08-04T0411Z-intel
    type: update
    summary: >
      Update to the 2026-07-31 ExfilSquad entry. The Police National Legal Database, run by West
      Yorkshire Police, has now published its own statement: names, organisations and work email
      addresses of police officers, staff, criminal-justice professionals, government partners and
      customers were compromised and published on the dark web, with no evidence that passwords or
      credentials were taken. It adds a second affected service, Ask the Police, and gives no victim
      total — reporting notes the 108,429 figure in circulation is PNLD's registered user base, not a
      breach count. VenariX assesses the campaign-level access path as public Microsoft Power Pages
      portals granting the Anonymous Users role broad Dataverse table read permissions, reproduced
      live against one municipal portal, with no exploit and no malware — but no source has confirmed
      that path for PNLD specifically.
    fields:
      - actions
      - affected_products
      - evidence
      - priority
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-08-04/pnld-confirms-breach-exfilsquad-power-pages-dataverse-path
  - at: "2026-08-05T04:12:23Z"
    run_id: 2026-08-05T0412Z-intel
    type: update
    summary: >
      Switzerland's NCSC published a TLP:CLEAR advisory on 2026-08-04 stating that a Microsoft Power
      Pages misconfiguration is being actively exploited to exfiltrate sensitive data from Dataverse:
      portals are exposed where the "Anonymous Users" web role holds excessive read permissions on
      Dataverse tables, making records publicly readable without authentication. It records the
      exploitation status as actively exploited and names Power Pages and Power Apps Portals as
      affected. The campaign behind it was covered here on 2026-07-31 and 2026-08-04; the delta is
      that the Swiss home authority has now turned it into a configuration-review obligation for Swiss
      public-sector portal estates.
    fields:
      - actions
      - affected_products
      - evidence
      - regions
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-05/ncsc-ch-power-pages-dataverse-anonymous-access-advisory
  - at: "2026-08-12T04:50:00Z"
    run_id: 2026-08-12T0411Z-intel
    type: update
    summary: >
      Wesco International confirmed to BleepingComputer on 2026-08-11 that it is investigating a claim
      of CRM data exfiltration by a third party after ExfilSquad — the extortion brand behind the
      confirmed July breaches of the UK Department for Education's portals and the Police National
      Legal Database — claimed 2.6 million records from its cloud CRM and, once its ransom deadline
      expired, published the data it says it took. Wesco found no evidence of ransomware or other
      malicious software and does not believe sensitive data is at risk, offering no figure of its
      own. Researchers have tied the group's past activity to improperly configured Microsoft Power
      Pages data tables; Wesco has not said how it was breached, and the only public link to Dynamics
      365 is that Wesco may be using it.
    fields:
      - affected_products
      - evidence
      - regions
      - sectors
      - sources
      - techniques
      - body
    merged_from: 2026-08-12/wesco-exfilsquad-crm-confirmation-dispute
  - at: "2026-08-16T04:45:00Z"
    run_id: 2026-08-16T0411Z-intel
    type: update
    summary: >
      Fortra's intelligence team reviewed the 382.64 GB, 27-million-record archive ExfilSquad
      published by torrent on 2026-08-07 and concluded the group's access claims are correct for at
      least 13 organisations across government, education, financial services and manufacturing — the
      UK Department for Education and the Police National Legal Database among them. Its leading
      theory for the access path is misconfigured Microsoft Power Pages portals allowing public read
      access, the same configuration class NCSC-CH put in front of Swiss operators on 2026-08-04; it
      reports finding no evidence of a vulnerability being exploited or of ransomware being deployed.
      Fortra identified over 10,000 potential Power Pages instances publicly accessible.
    fields:
      - evidence
      - regions
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role
migrated_from: null
---

The UK Department for Education has confirmed a breach of two public-facing portals, the DfE Help Desk Self-Service Portal and the Turing Scheme Portal, with the compromised material described as customer-service contact details — names, email addresses and phone numbers belonging to parents, officials, school leaders and university staff ([The Record, 2026-07-30](https://therecord.media/united-kingdom-ransomware-education)). Separately affected was the Police National Legal Database, where 135,000 records identify police officers by name, force and work email address; The Record notes the database holds no protected information from investigations or witnesses, and that the Home Office, which owns it, declined to comment. The NCSC has confirmed it is supporting law enforcement colleagues on the response. The extortionists are demanding a ransom; The Record notes that as a matter of policy the British government does not make ransom payments, and that the government has moved forward with plans, not yet law, to make such payments illegal for public-sector entities.

Two details in DfE's own response are worth carrying rather than the headline number. It explicitly corrects the criminals' framing, clarifying that the claimed figure of more than 600,000 pieces of data refers to lines of data rather than the count of individuals affected — a victim disputing the arithmetic behind an extortion claim rather than repeating it. And it assesses the risk to individuals as not high, which is consistent with contact-detail exposure rather than anything more sensitive.

**The claimant is where this gets interesting.** ExfilSquad's Tor leak site first appeared on 2026-07-26 and immediately listed 15 organisations across government, education, finance and technology. SOCRadar's profile of the group is unusually direct about what that list is worth: it assesses that the listings may involve reused data or fabricated allegations, with fabrication currently appearing more likely ([SOCRadar, 2026-07-28](https://socradar.io/blog/dark-web-profile-exfilsquad/)). No forensic evidence, data samples, victim confirmations or technical detail about initial access are publicly available for the group, and SOCRadar found no aliases, predecessor operations or rebranding history — this is a brand with no track record at all. It also documents the group posting on social media tagging a major vendor's security-intelligence account with a screenshot resembling an internal directory record, authenticity unconfirmed, which reads as publicity-seeking rather than proof.

So the same list contains one independently confirmed national-government breach and fourteen claims a credible vendor thinks are probably invented. One of the listed companies, semiconductor manufacturer Analog Devices, was added and then quietly removed — the outlet that reported the removal says the reason is unknown and notes that delisting is common when ransom negotiations begin ([BleepingComputer, 2026-07-30](https://www.bleepingcomputer.com/news/security/analog-devices-discloses-data-breach-says-operations-unaffected/)). Analog Devices separately filed a regulatory disclosure stating it identified unauthorized access to certain systems on 23 June 2026, that its investigation found certain files were exfiltrated, and that it does not believe the incident is reasonably likely to materially impact its business — filed under the non-material "Other Events" item despite the acknowledged exfiltration, which is itself a useful materiality-threshold data point for anyone calibrating their own disclosure playbook ([Analog Devices, 2026-07-29](https://www.sec.gov/Archives/edgar/data/6281/000119312526324223/d158253d8k.htm)). The company has not attributed that intrusion to ExfilSquad or confirmed the group's claims are related, and the record count circulating alongside it is the group's own allegation rather than a company figure ([CyberInsider, 2026-07-30](https://cyberinsider.com/analog-devices-says-hackers-stole-company-files-in-june-cyberattack/)). Those are two threads, and the available reporting does not join them.

**Defender takeaway:** the transferable item here is a triage discipline, not an indicator. When a new extortion brand appears with a long victim list, the volume of claims is not evidence — the base rate for a five-day-old handle with no history is heavily weighted toward recycled or invented data, and acting on a listing before victim or regulator confirmation means spending analyst hours on someone's marketing. The workable test is what happened here: one entry on the list was corroborated by the victim itself, so it is real and scoped; the rest stay unactioned until something outside the leak site says otherwise. The secondary point for the constituency is that both confirmed elements were externally-reachable service portals holding contact data — the sort of help-desk and scheme-administration systems that rarely appear on a crown-jewels inventory but sit on the public internet with real personal data behind them.

## Update — 2026-08-04T04:49:00Z

The earlier entry recorded the Police National Legal Database as "affected" with a 135,000-record figure taken from third-party reporting while the Home Office declined to comment. Three things have changed, and one of them is a correction to the numbers.

The victim has now published its own statement. PNLD, operated by West Yorkshire Police, confirms that "Information including the names, organisations and work email addresses of police officers, staff and other criminal justice professionals, government partners and customers has been compromised and published on the dark web", that "There is no evidence to suggest that passwords or other security credentials have been compromised", that the incident was identified on Sunday 2026-07-26, that all affected organisations were contacted, and that it is working with the National Crime Agency and specialist cyber-security firms with the Information Commissioner's Office notified ([PNLD, 2026-08-03](https://www.pnld.co.uk/~/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f)). The statement adds a second affected service the earlier entry did not carry: Ask the Police, the public enquiry site PNLD hosts, from which names and email addresses of citizens who had previously submitted questions were also published. PNLD stresses what it is not — not the Police National Computer, not the Police National Database, not a crime-recording system, and holding no confidential material on victims, witnesses or offenders ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html)).

On scope, the correction runs the other way from the usual pattern. PNLD's notice describes the exposed fields and gives no victim total at all, and as of 2026-08-03 it had not disclosed how many people were affected, when the intrusion began, how long access lasted or how much data was taken. The 108,429 figure circulating alongside this incident comes from PNLD's own 2025-26 annual summary of police registrations across all 43 Home Office forces — and the reporting is explicit that "That is a user-base figure, not a breach-victim count." Treat both that number and the earlier 135,000 as unconfirmed for scope purposes.

The access path is the transferable part, and it is a campaign-level finding rather than a PNLD root cause. VenariX reviewed data samples associated with 11 of the 15 organisations ExfilSquad listed and found the structure and field formatting consistent with Microsoft Dataverse exports across all 11 — `@odata.etag`, `@OData.Community.Display.V1.FormattedValue` and `@Microsoft.Dynamics.CRM.lookuplogicalname` artefacts across contacts, accounts, incidents, emails, annotations, leads, system users and business units. Its assessment is that the data came out of public Microsoft Power Pages portals configured to let anonymous visitors read Dataverse records, through the portal Web API `/_api/<EntitySetName>` route or a legacy `/_odata` feed. Crucially there is no exploit in the chain: "VenariX has not identified evidence of ransomware deployment, malware use, lateral movement, or exploitation of a software vulnerability." VenariX reproduced the condition once, against the City of Houston's public Power Apps portal serving Houston 311, which returned incident records without authentication in a form consistent with what ExfilSquad published ([VenariX, 2026-07-29](https://venarix.com/blog/exfilsquad-targets-misconfigured-microsoft-power-pages-portals)). VenariX is equally explicit about its own limit: the evidence does not confirm that every listed organisation was reached the same way, or through the same configuration issue. PNLD is not mentioned anywhere in that research at all, and the reporting that connects the two is explicit about the gap — as of 2026-08-03 neither PNLD's notice nor VenariX's report identified a PNLD-specific endpoint, permission setting, API route or supporting log, so "At this stage, the Power Pages link remains a hypothesis to test rather than an explanation of the PNLD breach" ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html)). What is corroborated is only the platform: PNLD's 2023-24 annual summary states the database uses Microsoft Power Platform, and the breach-notice page references assets on Microsoft's `content.powerapps.com` domain.

This also revises the earlier entry's editorial line. That entry carried an assessment that ExfilSquad's 15-victim list was more likely fabricated than genuine. The correct current read is narrower and more useful: the individual claim still deserves base-rate scepticism, but the *method* is now evidenced — 11 structurally consistent Dataverse sample sets, one reproduced live, one listed company (Frontier Airlines) having already confirmed unauthorised access to a data storage account on 2026-07-09 without attributing it — so the method should be swept for locally regardless of whether any given listing is real.

**Defender takeaway:** Power Pages and Dynamics portals are a standard build pattern across European public administration for service-request forms, licence applications, grant portals and help desks, and the failure here is a permissions decision, not a CVE — nothing to patch, no vendor advisory to wait for, and no EDR signal, failed-authentication burst or malware artefact to detect after the fact. Microsoft's documented behaviour is the whole mechanism: VenariX notes that "Microsoft states that when the Anonymous Users web role is granted access to a table, any visitor to the site can access that table's data", that those permissions apply to records reached through forms, lists, Liquid and the Web API alike, and that "Microsoft recommends testing /_odata from an unauthenticated browser session because enabled feeds may be available anonymously depending on the portal's security configuration." Beyond the per-site sweep, there is a tenant-level governance control that blocks unauthenticated reads of Dataverse data while still permitting public form submissions, and it is the durable fix for an estate with more portals than owners. **Triage:** the only telemetry this technique produces is web and application access logs, so hunt there for high-volume anonymous `/_api/` or `/_odata` retrieval sequences carrying paging parameters. The benign lookalike is a legitimate portal integration or a search crawler; the discriminators are the entity sets requested — a crawler fetches rendered pages, not `contacts` and `annotations` — and the paging pattern, since a genuine integration authenticates and a crawler does not walk record collections to exhaustion.

## Update — 2026-08-05T04:12:23Z

Switzerland's NCSC published a TLP:CLEAR advisory on 2026-08-04 stating that unauthenticated attackers can access and exfiltrate sensitive personal, financial and organizational data from public-facing portals via exposed Dataverse tables, and recording the current exploitation status as actively exploited ([NCSC Switzerland / GovCERT.ch, 2026-08-04](https://security-hub.ncsc.admin.ch/#/posts/12823)). The exposure arises where the "Anonymous Users" web role has been granted excessive read permissions on Dataverse tables, which makes the underlying records publicly readable to anyone who asks; NCSC-CH names Microsoft Power Pages and Microsoft Power Apps Portals as the affected products.

The campaign is not new here — the access-path analysis and the confirmed UK victim disclosures were covered on 2026-07-31 and 2026-08-04. What changed is the jurisdiction and the standing: until now this was foreign-incident reporting about portals belonging to other governments. The Swiss national authority issuing its own advisory to its own constituency converts it into a configuration-review duty for Swiss federal, cantonal and communal Power Pages estates, which are a common vehicle for exactly this kind of citizen-facing service.

NCSC-CH's recommended actions are to disable anonymous access, review table permissions, disable unnecessary Web API and OData feeds, and validate endpoint restrictions from an unauthenticated browser session ([NCSC Switzerland / GovCERT.ch, 2026-08-04](https://security-hub.ncsc.admin.ch/#/posts/12823)).

**Defender takeaway:** this is a configuration exposure, not a vulnerability, and it therefore has no patch and no version to check — which also means no scanner keyed on software versions will find it. The advisory's framing is the right one operationally: the detection method is verification rather than alerting. Enumerate the portals, ask their data endpoints as an anonymous caller, and compare what comes back against what the portal was designed to publish. An organisation that cannot quickly list its public Power Pages sites has a prior problem to solve first, and that inventory gap is the reason this class of exposure persists — these portals are frequently stood up by business units rather than by IT.

**Triage:** anonymous read access is a legitimate and intended configuration for genuinely public content, so its presence is not by itself a finding. The discriminator is which tables answer: a portal publishing a public register is doing its job, while the same anonymous role returning contact records, case data or internal identifiers is the misconfiguration the advisory describes.

## Update — 2026-08-12T04:50:00Z

The ExfilSquad campaign — whose leak-site list a threat-intelligence vendor assessed was more likely fabricated than real, but which contained a genuine UK government breach — has produced its first victim to answer on the record in partial terms. Wesco International, a US industrial and electrical distributor, confirmed to BleepingComputer that it is investigating a claim of CRM data exfiltration by a third party, after ExfilSquad claimed 2.6 million records taken from its cloud CRM environment ([BleepingComputer, 2026-08-11](https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/)). The company's spokesperson states "We have worked with our cloud CRM vendor on the matter, and we do not believe that there is a risk to sensitive data", and the company "found no evidence of ransomware or other malicious software on its IT systems", with no business disruption reported.

Two things happened in sequence and both matter. After the deadline for Wesco to enter ransom negotiations expired, ExfilSquad published the data it says it exfiltrated ([BleepingComputer, 2026-08-11](https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/)) — so this is a completed publication event, not a pending threat. And Wesco's posture is a third distinct response pattern from this campaign's victims: the UK Department for Education and the Police National Legal Database both issued full confirmations with corrected scope, other named victims have said nothing at all, and Wesco concedes the incident while contesting its severity. A triage queue that ingests leak-site feeds now has three calibration points from one actor: confirmed-and-detailed, confirmed-but-disputed, and unanswered.

The technical half needs its hedge stated plainly, because the reporting is careful and it would be easy to over-read. What BleepingComputer says is two separate things: that research from Resecurity and VenariX indicates the group "has targeted in the past improperly configured Microsoft Power Pages data tables", and that while Wesco has not shared how it was breached, "publicly available information indicates that Wesco may be using Microsoft Dynamics 365" ([BleepingComputer, 2026-08-11](https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/)). No source joins those two into a finding that this breach used a Dynamics 365 surface, and no source states the group's targeting has widened. The honest read is that the documented mechanism remains anonymously readable Power Pages data tables — no exploit, no malware, just data a portal was configured to serve to anyone — and that this victim's root cause is undisclosed.

**Defender takeaway:** Switzerland's national authority already turned this campaign's mechanism into a standing configuration-review obligation for federal and cantonal portal estates on 2026-08-04, and the useful framing for that review is an entitlement question rather than a product question: which Dataverse tables can an unauthenticated web role read, across every Power Platform surface the organisation publishes. That is answered in the environment's own role configuration, not in a vulnerability scan — and unlike a patch, it stays answered only as long as nobody adds a table to the anonymous role.

**Triage:** exfiltration through an over-permissioned anonymous web role produces no exploit signature and no malware, so endpoint and network telemetry will be silent by construction — which is consistent with Wesco finding no ransomware or malicious software on its systems while an incident had nonetheless occurred. What it does produce is bulk read volume against Dataverse tables attributed to the anonymous or portal service identity rather than to a named user; the discriminator against a legitimately public portal is the breadth of tables touched and the sequential, high-rate access pattern, not the identity itself, which is supposed to be reading something.

## Update — 2026-08-16T04:45:00Z

The open question across this pipeline's ExfilSquad coverage has been whether the group's claims were real and how it obtained the data. A second intelligence team has now answered the first and narrowed the second. Fortra's intelligence and research team reviewed the data samples the group made public and concluded that its claim to hold sensitive data is correct, tying at least 13 victims to leaked data across government, education, financial services and manufacturing ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). The archive was published by torrent on 2026-08-07 after the group said those organisations did not meet its terms, totalling 382.64 GB and 27 million records across the 13 ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). Two organisations from the original list of 15 — a bank and a semiconductor manufacturer — were absent from the dump.

The victim set is broader than the UK public-sector cases this pipeline has carried. Alongside the UK Department for Education and the Police National Legal Database, it includes the City of Atlanta and District of Columbia Public Schools, where 60,000 records containing student names, dates of birth and unique student identifiers were leaked in a version the group said it had censored ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

On the access path, Fortra's finding is a narrowing rather than a confirmation, and the distinction is worth preserving: its leading theory is misconfigured Power Pages portals allowing public read access, with the leaked data structures consistent with Dataverse exports and no evidence found of a vulnerability being exploited or ransomware deployed ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/); [Cybersecurity Dive, 2026-08-14](https://www.cybersecuritydive.com/news/researchers-confirm-breach-claims-data-extortion/827926/)). Fortra reasons that because the campaign reached roughly 15 victims rather than tens of thousands, a platform vulnerability is unlikely to be the source — a configuration error reproduces per tenant, a product flaw would not ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

What is new against this pipeline's 2026-08-04 and 2026-08-05 entries is the mechanism stated at field precision and the exposure counted. The known Power Pages issue Fortra points to is that when the Anonymous Users web role is assigned to a table permission, that table's data can be read by anyone visiting the site, reachable through the portal's own API path, and Microsoft's documentation advises against using that role on publicly exposed sites ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). Fortra reports it was able to identify over 10,000 potential Power Pages instances accessible to the public, and notes that automated scanning for exposed Power Pages sites is a known technique — victims were likely found by crawling for misconfigured portals rather than targeted ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

**Defender takeaway:** the evidential gap narrows on two axes without closing on the third. When NCSC-CH told its constituency on 2026-08-04 to review anonymous web-role permissions on Power Pages portals, the campaign behind that advice rested on one researcher's live reproduction against a single municipal portal. A second team has now validated that the published data is genuine across 13 victims, and has put a five-figure number on how many Power Pages portals are potentially exposed — but it still describes the configuration as the leading theory for how the data was taken, not as an established root cause, so the link between that exposure count and these 27 million records remains an assessment rather than a finding. The exposure remains a configuration review rather than a hunt — there is no exploit, no malware and no anomalous authentication to detect, because the reads are anonymous and by design. The check that matters is per table, not per portal: enumerate which Dataverse tables the Anonymous Users role holds read permission on and compare that set against what the site is meant to publish.

**Triage:** for an estate running these portals, alert-side evidence of this activity is close to absent by construction — an anonymous read through the portal API is indistinguishable in authentication telemetry from a legitimate public page view, and neither a failed-logon spike nor a new-account artifact appears. The available signals are volumetric rather than behavioural: sustained sequential requests to the portal's API path from a single source, request patterns that walk table or record identifiers in order, and response sizes far larger than the site's ordinary page traffic. Treat an absence of alerts here as uninformative, and settle the question from the permission configuration instead.
