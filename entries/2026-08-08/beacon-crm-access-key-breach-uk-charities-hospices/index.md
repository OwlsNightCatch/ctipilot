---
schema: 1
kind: incident
title: "Beacon CRM tells around 1,500 UK charities to assume everything they stored was taken — a compromised access key, exfiltrated backups, and encryption its experts think the attacker could undo"
headline: "A charity-sector CRM breach reaches hospices, NHS-linked charities and Victim Support, with the vendor advising customers to assume total data loss"
summary: >
  Beacon, a CRM platform holding data for around 1,500 UK voluntary-sector organisations, published an
  incident update on 2026-08-04 confirming that copies of database backups were made and likely downloaded,
  and advising customers to assume all data they store in Beacon, attachments included, was taken. The entry
  point was a compromised access key, which Beacon says was "more sophisticated than a simple compromised
  username and password". Beacon stores data encrypted but says its experts assess the attacker could
  plausibly have decrypted it before copying. Affected charities include several hospices, Sheffield
  Hospital Charity and Victim Support, which reported to the ICO and the Charity Commission.
discovered_at: "2026-08-08T05:10:00Z"
event_date: "2026-08-04"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, supply-chain, cloud]
regions: [uk, europe]
sectors: [healthcare, legal-services, technology]
entities: [incident:beacon-crm-uk-charities-breach-2026-08]
techniques: [T1199, T1078, T1213]
affected_products: ["Beacon CRM"]
cves: []
sources:
  - url: "https://www.beaconcrm.org/incident"
    publisher: "Beacon CRM"
    date: "2026-08-04"
    role: primary
  - url: "https://www.victimsupport.org.uk/statement-regarding-cyber-incident-affecting-beacon-crm/"
    publisher: "Victim Support"
    date: "2026-08-04"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/healthcare-victim-charities-beacon/"
    publisher: "Infosecurity Magazine"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "our investigation has confirmed that copies of database backups were made and likely downloaded by the unauthorised third-party"
    publisher: "Beacon CRM"
  - quote: "you may want to assume that all data that you store in Beacon, including attachment files, has been downloaded"
    publisher: "Beacon CRM"
  - quote: "Beacon revealed in its public statement that a compromised access key was used to gain access to its systems."
    publisher: "Infosecurity Magazine"
  - quote: "copies of database back-ups were made and likely downloaded by an unauthorised third party"
    publisher: "Victim Support"
verification: multi-source
sourcing_note: null
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
actions:
  - "Enumerate every long-lived programmatic access key held by or issued to your SaaS suppliers and processors, and confirm each one is scoped below the level at which it could read a whole-tenant database backup — this breach turned one key into every customer's data, and no user credential or MFA control was in the path."
migrated_from: null
---

Beacon, a CRM platform built for the UK voluntary sector and holding data for around 1,500 organisations, published an incident update on 2026-08-04 that is more candid than most and worse than its early framing suggested. Its investigation "has confirmed that copies of database backups were made and likely downloaded by the unauthorised third-party", supported by evidence of a spike in activity during the incident timeline symptomatic of data leaving its systems; because it judges it highly unlikely to establish which data related to whom, its advice to customers is that "you may want to assume that all data that you store in Beacon, including attachment files, has been downloaded" ([Beacon CRM, 2026-08-04](https://www.beaconcrm.org/incident)).

The access path is the transferable part. Infosecurity Magazine reports that "Beacon revealed in its public statement that a compromised access key was used to gain access to its systems", with no detail published on how the key was obtained, and quotes the provider's characterisation that "This was more sophisticated than a simple compromised username and password" ([Infosecurity Magazine, 2026-08-07](https://www.infosecurity-magazine.com/news/healthcare-victim-charities-beacon/)). A programmatic key is not an account: it does not sit behind multi-factor authentication, does not trip impossible-travel logic, and in a multi-tenant platform it is frequently scoped to the platform rather than to a tenant — which is how a single credential becomes every customer's backup.

Encryption at rest did not close the gap either. Beacon states that while it stores data in an encrypted state, its experts have advised that on the available evidence it is possible the responsible party would have been able to decrypt it before copying it out ([Beacon CRM, 2026-08-04](https://www.beaconcrm.org/incident)). That is the expected outcome when the attacker holds an application-layer credential: the platform decrypts for its own legitimate operations, so a stolen key inherits that ability.

Downstream, individual charities are confirming and notifying separately. Victim Support published its own statement saying the evidence suggests "copies of database back-ups were made and likely downloaded by an unauthorised third party" and that it has reported the incident to the Information Commissioner's Office and the Charity Commission ([Victim Support, 2026-08-04](https://www.victimsupport.org.uk/statement-regarding-cyber-incident-affecting-beacon-crm/)). Infosecurity names Myton Hospices, Sheffield Hospital Charity, Priscilla Bacon Hospice Charity and Rowcroft Hospice in the healthcare sector, plus homelessness charity The Clock Tower Sanctuary, with affected data including names, email addresses, telephone numbers and donation records ([Infosecurity Magazine, 2026-08-07](https://www.infosecurity-magazine.com/news/healthcare-victim-charities-beacon/)). No actor has claimed the breach and no leak-site listing has appeared.

**Defender takeaway:** the population here — hospice patients and their families, victims of crime, people using homelessness services — is one where the contact data alone supports highly credible targeted social engineering, and it is now held by an unknown party with no extortion demand to signal what happens next. For any organisation that outsources case management or supporter data, the audit question this raises is narrower and more answerable than "are our suppliers secure": which programmatic keys exist against your data in a supplier's platform, what is each one scoped to, and would its theft be visible to you or only to them.

**Triage:** an access-key compromise on a supplier platform produces no telemetry on the customer side at all — that is the defining property, and it is why the detection burden sits with the provider's own audit logging of key usage and egress volume rather than with anything a downstream charity could have seen. Where you operate the platform, the discriminator is the shape of the access, not its credentials: a valid key performing bulk reads or backup retrieval at a volume and hour outside its established pattern, against tenants it has never touched before.
