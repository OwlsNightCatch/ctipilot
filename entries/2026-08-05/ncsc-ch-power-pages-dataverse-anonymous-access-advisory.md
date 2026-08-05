---
schema: 1
kind: threat
horizon: operational
title: "NCSC-CH advises its own constituency on the actively exploited Power Pages misconfiguration — anonymous web roles granted excessive Dataverse table permissions"
headline: "Switzerland's national authority makes the Power Pages Dataverse exposure a standing check for federal and cantonal portals"
summary: >
  Switzerland's NCSC published a TLP:CLEAR advisory on 2026-08-04 stating that a Microsoft Power Pages
  misconfiguration is being actively exploited to exfiltrate sensitive data from Dataverse: portals are
  exposed where the "Anonymous Users" web role holds excessive read permissions on Dataverse tables,
  making records publicly readable without authentication. It records the exploitation status as
  actively exploited and names Power Pages and Power Apps Portals as affected. The campaign behind it
  was covered here on 2026-07-31 and 2026-08-04; the delta is that the Swiss home authority has now
  turned it into a configuration-review obligation for Swiss public-sector portal estates.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-04"
run_id: 2026-08-05T0412Z-intel
priority: notable
immediate_action: null
tags: [data-breach, cloud, actively-exploited, default-config, identity]
regions: [switzerland, europe]
sectors: [public-sector]
entities: [actor:exfilsquad]
techniques: [T1190, T1530]
affected_products: ["Microsoft Power Pages", "Microsoft Power Apps Portals"]
cves: []
sources:
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12823"
    publisher: "NCSC Switzerland / GovCERT.ch"
    date: "2026-08-04"
    role: primary
closed_sources: []
evidence:
  - quote: "Unauthenticated attackers can access and exfiltrate sensitive personal, financial, and organizational data from public-facing portals via exposed Dataverse tables."
    publisher: "NCSC Switzerland / GovCERT.ch"
  - quote: "Current exploitation status: Actively Exploited"
    publisher: "NCSC Switzerland / GovCERT.ch"
verification: single-source-national-cert
sourcing_note: "Single-source under the national-CERT carve-out: NCSC-CH is the disclosing authority for its own advisory to its own jurisdiction. The underlying campaign and the access-path research were covered here on 2026-07-31 and 2026-08-04 from separate sources."
confidence: high
update_of: 2026-08-04/pnld-confirms-breach-exfilsquad-power-pages-dataverse-path
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Enumerate every public-facing Power Pages and Power Apps Portals site in the estate and request its Web API and OData endpoints from an unauthenticated browser session, comparing the tables that return records against the set the portal is meant to expose — the advisory frames this as verification to perform, not an alert to wait for."
migrated_from: null
---

**UPDATE (originally covered 2026-08-04):** Switzerland's NCSC published a TLP:CLEAR advisory on 2026-08-04 stating that unauthenticated attackers can access and exfiltrate sensitive personal, financial and organizational data from public-facing portals via exposed Dataverse tables, and recording the current exploitation status as actively exploited ([NCSC Switzerland / GovCERT.ch, 2026-08-04](https://security-hub.ncsc.admin.ch/#/posts/12823)). The exposure arises where the "Anonymous Users" web role has been granted excessive read permissions on Dataverse tables, which makes the underlying records publicly readable to anyone who asks; NCSC-CH names Microsoft Power Pages and Microsoft Power Apps Portals as the affected products.

The campaign is not new here — the access-path analysis and the confirmed UK victim disclosures were covered on 2026-07-31 and 2026-08-04. What changed is the jurisdiction and the standing: until now this was foreign-incident reporting about portals belonging to other governments. The Swiss national authority issuing its own advisory to its own constituency converts it into a configuration-review duty for Swiss federal, cantonal and communal Power Pages estates, which are a common vehicle for exactly this kind of citizen-facing service.

NCSC-CH's recommended actions are to disable anonymous access, review table permissions, disable unnecessary Web API and OData feeds, and validate endpoint restrictions from an unauthenticated browser session ([NCSC Switzerland / GovCERT.ch, 2026-08-04](https://security-hub.ncsc.admin.ch/#/posts/12823)).

**Defender takeaway:** this is a configuration exposure, not a vulnerability, and it therefore has no patch and no version to check — which also means no scanner keyed on software versions will find it. The advisory's framing is the right one operationally: the detection method is verification rather than alerting. Enumerate the portals, ask their data endpoints as an anonymous caller, and compare what comes back against what the portal was designed to publish. An organisation that cannot quickly list its public Power Pages sites has a prior problem to solve first, and that inventory gap is the reason this class of exposure persists — these portals are frequently stood up by business units rather than by IT.

**Triage:** anonymous read access is a legitimate and intended configuration for genuinely public content, so its presence is not by itself a finding. The discriminator is which tables answer: a portal publishing a public register is doing its job, while the same anonymous role returning contact records, case data or internal identifiers is the misconfiguration the advisory describes.
