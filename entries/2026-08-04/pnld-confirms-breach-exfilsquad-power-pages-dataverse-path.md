---
schema: 1
kind: incident
horizon: operational
title: "PNLD confirms the police contact-data breach and names a second affected service; researchers trace the ExfilSquad campaign to anonymously readable Power Pages portals, but not PNLD's own root cause"
headline: "The victim's statement lands, the widely quoted record figures are not victim counts, and the Dataverse path is a campaign-level hypothesis to sweep for"
summary: >
  Update to the 2026-07-31 ExfilSquad entry. The Police National Legal Database, run by West Yorkshire Police, has now
  published its own statement: names, organisations and work email addresses of police officers, staff, criminal-justice
  professionals, government partners and customers were compromised and published on the dark web, with no evidence that
  passwords or credentials were taken. It adds a second affected service, Ask the Police, and gives no victim total —
  reporting notes the 108,429 figure in circulation is PNLD's registered user base, not a breach count. VenariX assesses
  the campaign-level access path as public Microsoft Power Pages portals granting the Anonymous Users role broad
  Dataverse table read permissions, reproduced live against one municipal portal, with no exploit and no malware — but no
  source has confirmed that path for PNLD specifically.
discovered_at: "2026-08-04T04:49:00Z"
event_date: "2026-08-03"
run_id: 2026-08-04T0411Z-intel
priority: high
immediate_action: null
tags: [data-breach, cloud, identity]
regions: [uk, europe]
sectors: [public-sector, defense]
entities: [actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07]
techniques: [T1213]
affected_products: ["Microsoft Power Pages", "Microsoft Dataverse", "Microsoft Power Apps"]
cves: []
sources:
  - url: "https://www.pnld.co.uk/~/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f"
    publisher: "Police National Legal Database (West Yorkshire Police)"
    date: "2026-08-03"
    role: primary
  - url: "https://venarix.com/blog/exfilsquad-targets-misconfigured-microsoft-power-pages-portals"
    publisher: "VenariX"
    date: "2026-07-29"
    role: primary
  - url: "https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html"
    publisher: "The Hacker News"
    date: "2026-08-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Information including the names, organisations and work email addresses of police officers, staff and other criminal justice professionals, government partners and customers has been compromised and published on the dark web."
    publisher: "Police National Legal Database"
  - quote: "There is no evidence to suggest that passwords or other security credentials have been compromised."
    publisher: "Police National Legal Database"
  - quote: "VenariX has not identified evidence of ransomware deployment, malware use, lateral movement, or exploitation of a software vulnerability."
    publisher: "VenariX"
  - quote: "That is a user-base figure, not a breach-victim count."
    publisher: "The Hacker News"
  - quote: "At this stage, the Power Pages link remains a hypothesis to test rather than an explanation of the PNLD breach."
    publisher: "The Hacker News"
sourcing_note: >
  The PNLD statement page carries no publication date; it is dated here to the 2026-08-03 reporting that first carried it
  and was retrieved on 2026-08-04. The `techniques[]` mapping carries only the collection behaviour the sources evidence
  — bulk retrieval of records from Dataverse tables. No access-vector technique is mapped: VenariX states explicitly
  that it found no exploitation of a software vulnerability, and no source identifies the route into PNLD.
verification: multi-source
confidence: high
update_of: 2026-07-31/exfilsquad-uk-department-for-education-pnld-breach
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "From an unauthenticated browser session, request /_api/contacts, /_api/accounts, /_api/incidents, /_api/emails, /_api/annotations and /_odata against every externally-reachable Power Pages or Power Apps portal your organisation operates, and treat any 200 response returning record bodies as a live data exposure to close today by removing table permissions from the Anonymous Users web role."
migrated_from: null
---

**UPDATE (originally covered 2026-07-31):** the earlier entry recorded the Police National Legal Database as "affected" with a 135,000-record figure taken from third-party reporting while the Home Office declined to comment. Three things have changed, and one of them is a correction to the numbers.

The victim has now published its own statement. PNLD, operated by West Yorkshire Police, confirms that "Information including the names, organisations and work email addresses of police officers, staff and other criminal justice professionals, government partners and customers has been compromised and published on the dark web", that "There is no evidence to suggest that passwords or other security credentials have been compromised", that the incident was identified on Sunday 2026-07-26, that all affected organisations were contacted, and that it is working with the National Crime Agency and specialist cyber-security firms with the Information Commissioner's Office notified ([PNLD, 2026-08-03](https://www.pnld.co.uk/~/article/?id=7ebf3c0e-598e-f111-8077-7ced8d3aa78f)). The statement adds a second affected service the earlier entry did not carry: Ask the Police, the public enquiry site PNLD hosts, from which names and email addresses of citizens who had previously submitted questions were also published. PNLD stresses what it is not — not the Police National Computer, not the Police National Database, not a crime-recording system, and holding no confidential material on victims, witnesses or offenders ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html)).

On scope, the correction runs the other way from the usual pattern. PNLD's notice describes the exposed fields and gives no victim total at all, and as of 2026-08-03 it had not disclosed how many people were affected, when the intrusion began, how long access lasted or how much data was taken. The 108,429 figure circulating alongside this incident comes from PNLD's own 2025-26 annual summary of police registrations across all 43 Home Office forces — and the reporting is explicit that "That is a user-base figure, not a breach-victim count." Treat both that number and the earlier 135,000 as unconfirmed for scope purposes.

The access path is the transferable part, and it is a campaign-level finding rather than a PNLD root cause. VenariX reviewed data samples associated with 11 of the 15 organisations ExfilSquad listed and found the structure and field formatting consistent with Microsoft Dataverse exports across all 11 — `@odata.etag`, `@OData.Community.Display.V1.FormattedValue` and `@Microsoft.Dynamics.CRM.lookuplogicalname` artefacts across contacts, accounts, incidents, emails, annotations, leads, system users and business units. Its assessment is that the data came out of public Microsoft Power Pages portals configured to let anonymous visitors read Dataverse records, through the portal Web API `/_api/<EntitySetName>` route or a legacy `/_odata` feed. Crucially there is no exploit in the chain: "VenariX has not identified evidence of ransomware deployment, malware use, lateral movement, or exploitation of a software vulnerability." VenariX reproduced the condition once, against the City of Houston's public Power Apps portal serving Houston 311, which returned incident records without authentication in a form consistent with what ExfilSquad published ([VenariX, 2026-07-29](https://venarix.com/blog/exfilsquad-targets-misconfigured-microsoft-power-pages-portals)). VenariX is equally explicit about its own limit: the evidence does not confirm that every listed organisation was reached the same way, or through the same configuration issue. PNLD is not mentioned anywhere in that research at all, and the reporting that connects the two is explicit about the gap — as of 2026-08-03 neither PNLD's notice nor VenariX's report identified a PNLD-specific endpoint, permission setting, API route or supporting log, so "At this stage, the Power Pages link remains a hypothesis to test rather than an explanation of the PNLD breach" ([The Hacker News, 2026-08-03](https://thehackernews.com/2026/08/pnld-breach-exposes-uk-police-and.html)). What is corroborated is only the platform: PNLD's 2023-24 annual summary states the database uses Microsoft Power Platform, and the breach-notice page references assets on Microsoft's `content.powerapps.com` domain.

This also revises the earlier entry's editorial line. That entry carried an assessment that ExfilSquad's 15-victim list was more likely fabricated than genuine. The correct current read is narrower and more useful: the individual claim still deserves base-rate scepticism, but the *method* is now evidenced — 11 structurally consistent Dataverse sample sets, one reproduced live, one listed company (Frontier Airlines) having already confirmed unauthorised access to a data storage account on 2026-07-09 without attributing it — so the method should be swept for locally regardless of whether any given listing is real.

**Defender takeaway:** Power Pages and Dynamics portals are a standard build pattern across European public administration for service-request forms, licence applications, grant portals and help desks, and the failure here is a permissions decision, not a CVE — nothing to patch, no vendor advisory to wait for, and no EDR signal, failed-authentication burst or malware artefact to detect after the fact. Microsoft's documented behaviour is the whole mechanism: VenariX notes that "Microsoft states that when the Anonymous Users web role is granted access to a table, any visitor to the site can access that table's data", that those permissions apply to records reached through forms, lists, Liquid and the Web API alike, and that "Microsoft recommends testing /_odata from an unauthenticated browser session because enabled feeds may be available anonymously depending on the portal's security configuration." Beyond the per-site sweep, there is a tenant-level governance control that blocks unauthenticated reads of Dataverse data while still permitting public form submissions, and it is the durable fix for an estate with more portals than owners. **Triage:** the only telemetry this technique produces is web and application access logs, so hunt there for high-volume anonymous `/_api/` or `/_odata` retrieval sequences carrying paging parameters. The benign lookalike is a legitimate portal integration or a search crawler; the discriminators are the entity sets requested — a crawler fetches rendered pages, not `contacts` and `annotations` — and the paging pattern, since a genuine integration authenticates and a crawler does not walk record collections to exhaustion.
