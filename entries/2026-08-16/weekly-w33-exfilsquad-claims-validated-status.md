---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "ExfilSquad status: a vendor validated the group's published data across 13 victim organisations and put the access path on misconfigured Power Pages portals — reversing the assessment, recorded here two weeks ago, that its victim list was more likely fabricated"
headline: "ExfilSquad's claims checked out — 13 victims validated, no vulnerability involved, and 10,000+ Power Pages instances publicly reachable"
summary: >
  Status update on the ExfilSquad extortion brand, tracked here since 31 July. A prior weekly recorded a
  threat-intelligence vendor assessing fabrication as the more likely explanation for the group's 15-name
  victim list, with one confirmed government breach inside it. That assessment has now been overtaken.
  Fortra's intelligence team reviewed the 382.64 GB, 27-million-record archive the group published by
  torrent on 7 August and concluded the access claims are correct for at least 13 organisations across
  government, education, financial services and manufacturing, the UK Department for Education and the
  Police National Legal Database among them. Its leading theory for the access path is misconfigured
  Microsoft Power Pages portals allowing public read access — the same configuration class Switzerland's
  NCSC put in front of its own constituency on 4 August — and it reports finding no evidence of a
  vulnerability being exploited or of ransomware being deployed, while identifying over 10,000 potentially
  publicly accessible Power Pages instances. A private-sector victim conceded a CRM incident in the same
  week while disputing its severity.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [data-breach, organized-crime, cloud, default-config]
regions: [europe, switzerland, global]
sectors: [public-sector, education, finance]
entities:
  - actor:exfilsquad
  - incident:uk-dfe-exfilsquad-breach-2026-07
techniques: [T1190, T1213, T1078.004]
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
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12823"
    publisher: "NCSC Switzerland — Cyber Security Hub"
    date: "2026-08-04"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/"
    publisher: "BleepingComputer"
    date: "2026-08-11"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  The validation is Fortra's own review of the published archive. Two outlets report it and they do not
  agree on the count — Infosecurity Magazine carries 13 organisations and the archive figures, Cybersecurity
  Dive carries about 15 and neither the archive size nor the record count — so the 13-organisation figure and
  the archive detail are cited to Infosecurity Magazine alone and the divergence is stated in the body
  rather than smoothed over.
  The access-path finding is explicitly Fortra's leading theory rather than a confirmed root cause for any
  named victim, and is carried as such; no victim organisation has confirmed a Power Pages misconfiguration
  as its own entry point. The reversal noted here is against an assessment a different vendor made about
  an earlier, 15-name list, so this is a change in the weight of evidence over time rather than one vendor
  contradicting another about the same dataset. The Swiss nexus rests on NCSC-CH's own advisory of
  4 August, which none of the reporting outlets mentions; it is cited directly and the operational entry
  covering it is referenced.
confidence: medium
update_of: null
references:
  - 2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role
  - 2026-08-05/ncsc-ch-power-pages-dataverse-anonymous-access-advisory
  - 2026-08-12/wesco-exfilsquad-crm-confirmation-dispute
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

Status update on the ExfilSquad extortion brand, tracked here since the UK Department for Education portal breaches of late July. Two weeks ago a weekly recorded a threat-intelligence vendor assessing fabrication as the more likely explanation for the group's leak-site victim list — an assessment that sat awkwardly alongside a real, government-confirmed breach inside that same list. This week the balance of evidence moved the other way, and it is worth recording precisely because the earlier scepticism is on this store's record.

Fortra's intelligence team reviewed the archive the group published by torrent on 7 August — 382.64 GB and 27 million records — and concluded that the group's access claims are correct for at least 13 organisations spanning government, education, financial services and manufacturing, with the UK Department for Education and the Police National Legal Database among them ([Infosecurity Magazine, 2026-08-14](https://www.infosecurity-magazine.com/news/exfilsquads-13-organizations/)). A second outlet reporting the same validation puts the figure differently, saying researchers are backing claims that the group exfiltrated data from about 15 organisations and naming the Department for Education but not the legal database ([Cybersecurity Dive, 2026-08-14](https://www.cybersecuritydive.com/news/researchers-confirm-breach-claims-data-extortion/827926/)); the two counts are not reconciled by either. Two findings inside that review matter more than the count. Fortra reports finding no evidence of a vulnerability being exploited or of ransomware being deployed, and its leading theory for the access path is misconfigured Microsoft Power Pages portals allowing public read access — the same configuration class Switzerland's NCSC put in front of Swiss operators on 4 August, when it advised on anonymous web roles granted excessive Dataverse table permissions ([NCSC Switzerland — Cyber Security Hub, 2026-08-04](https://security-hub.ncsc.admin.ch/#/posts/12823)). It also identified over 10,000 potentially publicly accessible Power Pages instances. In the same week a private-sector victim, Wesco International, confirmed it was investigating a CRM data-exfiltration claim while stating it found no evidence of ransomware and does not believe sensitive data is at risk, after its ransom deadline expired and the group published ([BleepingComputer, 2026-08-11](https://www.bleepingcomputer.com/news/security/wesco-confirms-security-incident-after-exfilsquad-claims-data-theft/)).

**Defender takeaway:** if Fortra's leading theory holds, this campaign has no patch, no exploit and no malware anywhere in it — the data left through a portal that was configured to hand it out, which means every control keyed to intrusion detection was structurally blind to it and nothing in a vulnerability-management programme would have surfaced the exposure. For a public-sector estate running Power Pages, the review that answers this is a configuration audit rather than a hunt: which tables the Anonymous Users web role can read, and whether any of them carry personal or case data. That audit is worth running on its own merits regardless of this campaign, and Switzerland's national authority has already told its constituency so. The second lesson is about triage discipline rather than technology. This store carried a vendor's fabrication assessment two weeks ago, correctly attributed and correctly hedged, and it has now been overtaken by a different vendor's file-level validation. The reason the earlier assessment was reasonable is the reason the correction matters: leak-site claims are cheap to make and expensive to check, so an assessment about a victim list is provisional until somebody reviews the data — and when a group's claims do check out, the interval during which defenders discounted them was time the named organisations did not spend responding.

**Triage:** anonymous data access through a portal produces no intrusion telemetry at all, so the observable is in application and platform logs rather than security tooling. The shape worth looking for is volume and breadth against an unauthenticated role: requests to table or list endpoints from unauthenticated sessions retrieving large record counts, paging steadily through a dataset, or enumerating table names — patterns that distinguish bulk collection from the handful of records a genuine public-facing form needs to serve. Legitimate anonymous use of these portals is narrow and shallow by design; a public form retrieves what it needs to render, not the table behind it.
