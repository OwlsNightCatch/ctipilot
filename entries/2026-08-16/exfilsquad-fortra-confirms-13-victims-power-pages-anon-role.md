---
schema: 1
kind: threat
horizon: operational
title: "ExfilSquad's claims check out: Fortra validated the published data for 13 victims, and puts the leading access theory on Power Pages portals granting the Anonymous Users role read access to Dataverse tables"
headline: "Fortra confirms ExfilSquad's data is genuine across 13 victims and counts over 10,000 potentially exposed Power Pages instances"
summary: >
  Fortra's intelligence team reviewed the 382.64 GB, 27-million-record archive ExfilSquad published by
  torrent on 2026-08-07 and concluded the group's access claims are correct for at least 13
  organisations across government, education, financial services and manufacturing — the UK Department
  for Education and the Police National Legal Database among them. Its leading theory for the access
  path is misconfigured Microsoft Power Pages portals allowing public read access, the same
  configuration class NCSC-CH put in front of Swiss operators on 2026-08-04; it reports finding no
  evidence of a vulnerability being exploited or of ransomware being deployed. Fortra identified over
  10,000 potential Power Pages instances publicly accessible.
discovered_at: "2026-08-16T04:45:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T0411Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime, cloud, identity, info-disclosure]
regions: [uk, europe, us, global]
sectors: [public-sector, education, finance, manufacturing]
entities: [actor:exfilsquad, incident:uk-dfe-exfilsquad-breach-2026-07]
techniques: [T1190, T1213]
affected_products: ["Microsoft Power Pages", "Microsoft Dynamics 365"]
cves: []
sources:
  - url: "https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/"
    publisher: "Infosecurity Magazine"
    date: "2026-08-14"
    role: primary
  - url: "https://www.cybersecuritydive.com/news/researchers-confirm-breach-claims-data-extortion/827926/"
    publisher: "Cybersecurity Dive"
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The leading theory on the initial attack vector that enabled exfiltration is misconfigured Microsoft Power Page portals that allowed for public read access"
    publisher: "Fortra FIRE, quoted by Infosecurity Magazine"
  - quote: "it was able to identify over 10,000 potential Power Pages instances accessible to the public"
    publisher: "Infosecurity Magazine, reporting Fortra's research"
  - quote: "the total data was reported to be 382.64 GB and 27 million records across the 13 victims"
    publisher: "Infosecurity Magazine"
verification: multi-source
sourcing_note: >
  Fortra's own report could not be fetched from this environment (the vendor blog returns HTTP 403 to
  the routine transport and the reader proxy was unavailable for the whole run), so both cited sources
  are outlets quoting it directly rather than the primary. They agree on the substance and neither
  contradicts the other. Fortra's access-path finding is explicitly a leading theory, not a confirmed
  root cause, and it is reported that way here. Volumes attributed to individual named organisations
  in Cybersecurity Dive's list are the group's own claims and remain unconfirmed by those
  organisations; only the archive totals and the 13-victim validation are Fortra's. Both cited sources
  are dated 2026-08-14 and so predate this run's window: the entry ships because it is an evidentiary
  delta on ground the store has carried since 2026-07-31 that the fire whose window covered it did not
  publish, not because the reporting is fresh.
confidence: medium
update_of: 2026-07-31/exfilsquad-uk-department-for-education-pnld-breach
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

**UPDATE (originally covered 2026-07-31):** the open question across this pipeline's ExfilSquad coverage has been whether the group's claims were real and how it obtained the data. A second intelligence team has now answered the first and narrowed the second. Fortra's intelligence and research team reviewed the data samples the group made public and concluded that its claim to hold sensitive data is correct, tying at least 13 victims to leaked data across government, education, financial services and manufacturing ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). The archive was published by torrent on 2026-08-07 after the group said those organisations did not meet its terms, totalling 382.64 GB and 27 million records across the 13 ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). Two organisations from the original list of 15 — a bank and a semiconductor manufacturer — were absent from the dump.

The victim set is broader than the UK public-sector cases this pipeline has carried. Alongside the UK Department for Education and the Police National Legal Database, it includes the City of Atlanta and District of Columbia Public Schools, where 60,000 records containing student names, dates of birth and unique student identifiers were leaked in a version the group said it had censored ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

On the access path, Fortra's finding is a narrowing rather than a confirmation, and the distinction is worth preserving: its leading theory is misconfigured Power Pages portals allowing public read access, with the leaked data structures consistent with Dataverse exports and no evidence found of a vulnerability being exploited or ransomware deployed ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/); [Cybersecurity Dive, 2026-08-14](https://www.cybersecuritydive.com/news/researchers-confirm-breach-claims-data-extortion/827926/)). Fortra reasons that because the campaign reached roughly 15 victims rather than tens of thousands, a platform vulnerability is unlikely to be the source — a configuration error reproduces per tenant, a product flaw would not ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

What is new against this pipeline's 2026-08-04 and 2026-08-05 entries is the mechanism stated at field precision and the exposure counted. The known Power Pages issue Fortra points to is that when the Anonymous Users web role is assigned to a table permission, that table's data can be read by anyone visiting the site, reachable through the portal's own API path, and Microsoft's documentation advises against using that role on publicly exposed sites ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). Fortra reports it was able to identify over 10,000 potential Power Pages instances accessible to the public, and notes that automated scanning for exposed Power Pages sites is a known technique — victims were likely found by crawling for misconfigured portals rather than targeted ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)).

**Defender takeaway:** the evidential gap narrows on two axes without closing on the third. When NCSC-CH told its constituency on 2026-08-04 to review anonymous web-role permissions on Power Pages portals, the campaign behind that advice rested on one researcher's live reproduction against a single municipal portal. A second team has now validated that the published data is genuine across 13 victims, and has put a five-figure number on how many Power Pages portals are potentially exposed — but it still describes the configuration as the leading theory for how the data was taken, not as an established root cause, so the link between that exposure count and these 27 million records remains an assessment rather than a finding. The exposure remains a configuration review rather than a hunt — there is no exploit, no malware and no anomalous authentication to detect, because the reads are anonymous and by design. The check that matters is per table, not per portal: enumerate which Dataverse tables the Anonymous Users role holds read permission on and compare that set against what the site is meant to publish.

**Triage:** for an estate running these portals, alert-side evidence of this activity is close to absent by construction — an anonymous read through the portal API is indistinguishable in authentication telemetry from a legitimate public page view, and neither a failed-logon spike nor a new-account artifact appears. The available signals are volumetric rather than behavioural: sustained sequential requests to the portal's API path from a single source, request patterns that walk table or record identifiers in order, and response sizes far larger than the site's ordinary page traffic. Treat an absence of alerts here as uninformative, and settle the question from the permission configuration instead.
