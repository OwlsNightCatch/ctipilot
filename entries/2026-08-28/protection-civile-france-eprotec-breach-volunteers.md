---
schema: 1
kind: incident
horizon: operational
title: "La Protection Civile (France): eProtec volunteer-management platform breach, 525,000+ profiles including minors, intrusion dated to March 2026 discovered mid-August"
headline: "A French civil-security federation confirms a five-month-old intrusion the same week several comparable sports federations were also hit"
summary: >
  La Fédération Nationale de Protection Civile (FNPC) confirmed on 2026-08-21 a hack and personal-
  data breach dated to March 2026 on its eProtec volunteer-management platform, discovered only
  in mid-August. Exposed data includes civil-status information, phone numbers and photographs of
  current and former volunteers and externals, including minors — no passwords or banking data.
  FNPC frames it as part of a wider wave of contemporaneous attacks on comparable structures,
  including several sports federations.
discovered_at: "2026-08-28T06:44:00Z"
updated_at: null
event_date: "2026-08-21"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach]
regions: [europe]
sectors: [public-sector]
entities: [incident:protection-civile-eprotec-breach-2026-08]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html"
    publisher: "Franceinfo (AFP)"
    date: "2026-08-21"
    role: primary
  - url: "https://frenchbreaches.com/alertes/protection-civile-mt27j64epv2smy5m0g"
    publisher: "FrenchBreaches (specialist breach tracker; discoverer)"
    date: "2026-08-21"
    role: corroborating
  - url: "https://christophemazzola.fr/en/articles/fuites-donnees-france-aout-2026"
    publisher: "Christophe Mazzola (independent security analyst)"
    date: "2026-08-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "a annoncé vendredi 21 août avoir été victime d'un piratage informatique et d'une \"violation de données à caractère personnel\" au mois de mars"
    publisher: "Franceinfo (AFP)"
  - quote: "s'inscrit dans un contexte d'attaques multiples menées au cours de la même période à l'encontre de structures comparables, notamment plusieurs fédérations sportives"
    publisher: "Franceinfo (AFP)"
  - quote: "Ces données concernent des bénévoles de la Protection civile, des anciens bénévoles et des personnes externes à la Protection civile"
    publisher: "Franceinfo (AFP)"
  - quote: "A ce stade, les investigations ne permettent pas de déterminer si l'ensemble de ces données a effectivement été consulté ou extrait, ni si elles ont été vendues, utilisées ou rendues publiques"
    publisher: "Franceinfo (AFP)"
verification: multi-source
sourcing_note: >
  FNPC's own spokesperson statement and written communiqué, quoted directly by Franceinfo/AFP, is
  the primary; FrenchBreaches (the discovering specialist tracker) and an independent analyst
  roundup corroborate. The widely-cited "525,000+ profiles / 15,000 photographs" figure comes from
  FrenchBreaches, not from FNPC itself — the federation states it is still trying to establish the
  exact number affected, so that volume is attributed to the tracker rather than treated as an
  organisational confirmation. Publication date (2026-08-21) predates this run's recency window
  but is exempt as a coverage-backlog item carrying its own event_date.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

La Fédération Nationale de Protection Civile (FNPC) confirmed on 2026-08-21 — via a spokesperson statement to AFP and a written communiqué, both quoted directly by Franceinfo — that it was the victim of a hack and "violation de données à caractère personnel" in March 2026 on the eProtec platform used to manage the volunteers, schedules and training of this state-approved civil security association: "a annoncé vendredi 21 août avoir été victime d'un piratage informatique et d'une 'violation de données à caractère personnel' au mois de mars" ([Franceinfo (AFP), 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)).

The FNPC states the attack "s'inscrit dans un contexte d'attaques multiples menées au cours de la même période à l'encontre de structures comparables, notamment plusieurs fédérations sportives" ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)) — fits a pattern of contemporaneous attacks on comparable structures, including several sports federations — framing this as part of a wider wave rather than a targeted campaign against it specifically. Exposed data includes civil-status information, phone numbers and profile photographs of current volunteers, former volunteers and people external to the organisation, including minors: "ces données concernent des bénévoles de la Protection civile, des anciens bénévoles et des personnes externes à la Protection civile" ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)); the FNPC explicitly states no data belonging to people the Protection Civile has rescued is involved, and that neither passwords nor banking details appear in the leak.

The federation says it only became aware of the breach around 17–18 August and that its investigation cannot yet determine whether the exposed data was actually consulted or extracted, nor whether it was sold, used or made public: "à ce stade, les investigations ne permettent pas de déterminer si l'ensemble de ces données a effectivement été consulté ou extrait, ni si elles ont été vendues, utilisées ou rendues publiques" ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)) — it has filed a complaint with the Paris prosecutor's cybercrime unit. The commonly cited "525,000+ profiles / 15,000 photographs" figure comes from FrenchBreaches, the specialist outlet that first surfaced the breach; the FNPC itself says it is still trying to establish the exact number of people affected, so that volume should be attributed to the tracker, not treated as an organisational confirmation.

No access vector is stated by any source; `techniques[]` carries only T1213 (Data from Information Repositories) for the confirmed outcome — personal-data records extracted from the eProtec volunteer-management platform's own data store — since nothing about how the attacker first got in is disclosed. `actions[]` is empty: no defender-actionable mechanism is disclosed for this organisation-specific incident.
