---
schema: 1
kind: incident
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
  - quote: 'announced on Friday 21 August that it had been the victim of a computer intrusion (translated from French)'
    original: "a annoncé vendredi 21 août avoir été victime d'un piratage informatique"
    publisher: "Franceinfo (AFP)"
  - quote: "fits within a context of multiple attacks carried out over the same period against comparable organisations, notably several sports federations. (translated from French)"
    original: "s'inscrit dans un contexte d'attaques multiples menées au cours de la même période à l'encontre de structures comparables, notamment plusieurs fédérations sportives"
    publisher: "Franceinfo (AFP)"
  - quote: "The data concerns Protection Civile volunteers, former volunteers and persons external to the Protection Civile. (translated from French)"
    original: "Ces données concernent des bénévoles de la Protection civile, des anciens bénévoles et des personnes externes à la Protection civile"
    publisher: "Franceinfo (AFP)"
  - quote: "At this stage, the investigations do not make it possible to determine whether all of this data was actually accessed or extracted, nor whether it was sold, used or made public. (translated from French)"
    original: "A ce stade, les investigations ne permettent pas de déterminer si l'ensemble de ces données a effectivement été consulté ou extrait, ni si elles ont été vendues, utilisées ou rendues publiques"
    publisher: "Franceinfo (AFP)"
  - quote: "the currently available elements do not allow us to establish the presence of passwords, banking details or ID documents in the exfiltrated data (translated from French)"
    original: "Les éléments actuellement disponibles ne permettent pas d’établir la présence de mots de passe, de coordonnées bancaires ou de pièces d’identité dans les données exfiltrées"
    publisher: "FrenchBreaches"
verification: multi-source
sourcing_note: >
  FNPC's own spokesperson statement and written communiqué, quoted directly by Franceinfo/AFP, is
  the primary; FrenchBreaches (the discovering specialist tracker) and an independent analyst
  roundup corroborate. The widely-cited "525,000+ profiles / 15,000 photographs" figure comes from
  FrenchBreaches, not from FNPC itself — the federation states it is still trying to establish the
  exact number affected, so that volume is attributed to the tracker rather than treated as an
  organisational confirmation. The reporting is dated 2026-08-21 and the breach it describes is
  dated to March 2026; both are recorded rather than the disclosure date alone.
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
updates:
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      Operator-directed editorial pass (v4.2): removed composition-rationale narration and 
      pipeline-internal jargon from reader-facing text; tightened or cut paragraphs that 
      restated the summary or padded without responder value. No factual claim changed.
    fields: [evidence, body]
  - at: "2026-08-30T13:12:06Z"
    run_id: 2026-08-30T1312Z-audit
    type: correction
    summary: >
      Two fixes. The claim that neither passwords nor banking details appear in the leak was
      attributed to the FNPC; the federation's statement never mentions either, and the finding
      is FrenchBreaches' own hedged reading of exfiltrated samples, which says the available
      elements do not allow it to establish their presence. That is an absence of evidence in
      what one tracker saw, not an organisational assurance, and it is now attributed and hedged
      as such. The awareness date is also given as a single date, 17 August, matching the source,
      rather than as a 17-18 August range.
    fields: [evidence, sourcing_note, body]
migrated_from: null
---

La Fédération Nationale de Protection Civile (FNPC) confirmed on 2026-08-21 — via a spokesperson statement to AFP and a written communiqué, both quoted directly by Franceinfo — that it was the victim of a hack and "personal data breach" (translated from French) in March 2026 on the eProtec platform used to manage the volunteers, schedules and training of this state-approved civil security association: "announced on Friday 21 August that it had been the victim of a computer intrusion and a 'personal data breach' in March" (translated from French) ([Franceinfo (AFP), 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)).

The FNPC states the attack "fits within a context of multiple attacks carried out over the same period against comparable organisations, notably several sports federations" (translated from French) ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)) — fits a pattern of contemporaneous attacks on comparable structures, including several sports federations — framing this as part of a wider wave rather than a targeted campaign against it specifically. Exposed data includes civil-status information, phone numbers and profile photographs of current volunteers, former volunteers and people external to the organisation, including minors: "the data concerns Protection Civile volunteers, former volunteers and persons external to the Protection Civile" (translated from French) ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)); the FNPC explicitly states no data belonging to people the Protection Civile has rescued is involved. FrenchBreaches, analysing samples of the exfiltrated data, reports a narrower and hedged non-finding: "the currently available elements do not allow us to establish the presence of passwords, banking details or ID documents in the exfiltrated data" (translated from French) ([FrenchBreaches, 2026-08](https://frenchbreaches.com/alertes/protection-civile-mt27j64epv2smy5m0g)) - an absence of evidence in what the tracker has seen, not a statement by the federation that no such data is in the leak.

The federation says it only became aware of the breach on 17 August and that its investigation cannot yet determine whether the exposed data was actually consulted or extracted, nor whether it was sold, used or made public: "at this stage, the investigations do not make it possible to determine whether all of this data was actually accessed or extracted, nor whether it was sold, used or made public" (translated from French) ([FNPC communiqué, quoted by Franceinfo, 2026-08-21](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/la-protection-civile-annonce-avoir-ete-visee-par-une-cyberattaque-en-mars_8156621.html)) — it has filed a complaint with the Paris prosecutor's cybercrime unit. The commonly cited "525,000+ profiles / 15,000 photographs" figure comes from FrenchBreaches, the specialist outlet that first surfaced the breach; the FNPC itself says it is still trying to establish the exact number of people affected, so that volume should be attributed to the tracker, not treated as an organisational confirmation.

## Correction — 2026-08-30T13:12:06Z

The statement that neither passwords nor banking details appear in the leak was attributed here to the FNPC. The federation says no such thing. The source of that claim is FrenchBreaches, which analysed samples of the exfiltrated data and reports a hedged non-finding: "the currently available elements do not allow us to establish the presence of passwords, banking details or ID documents in the exfiltrated data" (translated from French) ([FrenchBreaches, 2026-08](https://frenchbreaches.com/alertes/protection-civile-mt27j64epv2smy5m0g)). For anyone reasoning about credential-reuse or fraud exposure for the affected volunteers, that is a materially weaker basis than a federation assurance, and it should be read as what one tracker did not find in the sample it obtained. The date the federation became aware of the breach is also stated as a single date, 17 August, matching the source.
