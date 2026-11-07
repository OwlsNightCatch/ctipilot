---
schema: 1
kind: incident
title: "Connor Moucka pleads guilty over the 2024 SaaS-tenant mass-extortion campaign — 165+ victim organisations reached with stolen credentials and no vulnerability in the platform"
headline: "Law-enforcement closure on the campaign that set the template for cloud-tenant compromise, with the access path entirely credential-based"
summary: >
  Connor Riley Moucka pleaded guilty on 2026-08-05 to four federal counts over a February–October 2024
  hacking and extortion campaign that the U.S. Department of Justice says compromised over 165 victim
  organisations, stole billions of customer records and produced over $2.5 million in ransom payments,
  with victim losses above $9.5 million affecting at least 100 million individuals. DOJ describes the
  target only as a U.S.-based software-as-a-service company
  and names no provider; the identification of the platform, the absence of enforced multi-factor
  authentication on the targeted tenants, and Moucka's aliases all come from KrebsOnSecurity rather
  than from the DOJ release. Sentencing is set for 2026-10-27.
discovered_at: "2026-08-10T04:53:00Z"
event_date: "2026-08-05"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [law-enforcement, data-breach, organized-crime, cloud, identity, infostealer]
regions: [global, us]
sectors: [public-sector, finance, retail, telco]
entities: [actor:unc5537, actor:cameron-wagenius]
techniques: [T1078.004, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.justice.gov/opa/pr/canadian-man-pleads-guilty-hacking-us-cloud-storage-provider-and-extorting-its-customers"
    publisher: "U.S. Department of Justice"
    date: "2026-08-05"
    role: primary
  - url: "https://krebsonsecurity.com/2026/08/canadian-man-pleads-guilty-in-snowflake-extortions/"
    publisher: "KrebsOnSecurity"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the compromise of over 165 victim organizations, the theft of billions of sensitive customer records and the extortion of numerous victims"
    publisher: "U.S. Department of Justice"
  - quote: "The conspirators profited from the scheme, receiving over $2.5 million in ransom payments."
    publisher: "U.S. Department of Justice"
  - quote: "Moucka pleaded guilty to four counts of the indictment, including computer fraud, wire fraud, aggravated identity theft, and a related conspiracy. He is scheduled to be sentenced on Oct. 27 and faces a mandatory minimum penalty of two years in prison on the aggravated identity theft count and a maximum penalty of 30 years in prison on the remaining counts."
    publisher: "U.S. Department of Justice"
  - quote: "The hackers targeted stolen credentials for Snowflake customer accounts that did not enforce multi-factor authentication, and extorted or attempted to extort a host of well-known companies, including TicketMaster, Lending Tree, Advance Auto Parts and Neiman Marcus. Snowflake responded to the data thefts by increasing password complexity requirements and enforcing multi-factor authentication."
    publisher: "KrebsOnSecurity"
verification: multi-source
sourcing_note: >
  The two sources carry materially different facts and are attributed separately throughout. The DOJ
  release contains no occurrence of the platform's name, of "multi-factor" or "MFA", or of any
  co-conspirator's name or alias — this run verified those absences directly against the release
  text. The provider identification, the missing-MFA precondition, Moucka's aliases and the
  co-conspirator's identity and sentencing date are KrebsOnSecurity's reporting alone.
confidence: high
update_of: null
references: []
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

The 2024 campaign that taught everyone what a mass SaaS-tenant compromise looks like has reached a guilty plea. The U.S. Department of Justice announced on 2026-08-05 that Connor Riley Moucka, 26, of Kitchener, Ontario, pleaded guilty over a February-to-October 2024 conspiracy involving "the compromise of over 165 victim organizations, the theft of billions of sensitive customer records and the extortion of numerous victims" ([U.S. Department of Justice, 2026-08-05](https://www.justice.gov/opa/pr/canadian-man-pleads-guilty-hacking-us-cloud-storage-provider-and-extorting-its-customers)). DOJ records that the conspirators received "over $2.5 million in ransom payments", that victim companies suffered over $9.5 million in actual losses excluding harm to their own customers, and that those customers total at least 100 million individuals. He "pleaded guilty to four counts of the indictment, including computer fraud, wire fraud, aggravated identity theft, and a related conspiracy", is scheduled for sentencing on 27 October, and faces a two-year mandatory minimum on the identity-theft count.

The sourcing here needs stating precisely, because the two available accounts do not carry the same facts. DOJ describes the victim platform only as a U.S.-based software-as-a-service company and never names it; the release contains no mention of multi-factor authentication and names no co-conspirator. It is KrebsOnSecurity that supplies the platform's identity and the access precondition: "The hackers targeted stolen credentials for Snowflake customer accounts that did not enforce multi-factor authentication, and extorted or attempted to extort a host of well-known companies… Snowflake responded to the data thefts by increasing password complexity requirements and enforcing multi-factor authentication" ([KrebsOnSecurity, 2026-08-06](https://krebsonsecurity.com/2026/08/canadian-man-pleads-guilty-in-snowflake-extortions/)). Krebs also supplies Moucka's operating aliases, and identifies an admitted co-conspirator — a U.S. Army soldier who pleaded guilty in July 2025 to extorting two telecommunications carriers for customer account data and who is separately scheduled for sentencing on 2026-09-03.

The reason this belongs in front of a public-sector SOC two years after the fact is the shape of the access path, which both sources agree on: stolen credentials used against customer-controlled tenants of a shared data platform. No vulnerability in the provider is alleged by either account. The platform did what platforms do — it enforced the authentication policy each tenant configured — and the tenants that had not enforced a second factor were the ones that lost data. Every public administration that has moved reporting, analytics or case data onto a shared cloud data platform holds that same risk shape, and holds it on the tenant side where the provider's own security posture is not the deciding variable.

**Defender takeaway:** the durable lesson is about where responsibility for a tenant's authentication policy actually sits, and it is not with the provider. Treat every shared-platform tenant as an independently attackable perimeter whose configuration you own — enumerate which of your data-platform tenants can still authenticate with a password alone, and treat credentials harvested by infostealers as the assumed starting position rather than an unlikely one, since that is what fed this entire campaign. The prosecution closes a case; it changes nothing about the exposure, which is a configuration state rather than a patch level.
