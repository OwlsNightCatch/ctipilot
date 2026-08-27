---
schema: 1
kind: policy
horizon: strategic
title: >
  NIS2 enters its enforcement phase in two more jurisdictions from opposite ends — the
  Netherlands' transposition law takes effect on 15 August for 8,000+ organisations, while
  Germany's registration deadline has lapsed with BSI's own site telling unregistered entities to
  register immediately
headline: >
  One NIS2 clock starts on 15 August; the other has run out with a registration gap Germany has
  not closed
summary: >
  The Dutch Cyberbeveiligingswet and the companion critical-entities resilience law enter into
  force on 15 August 2026, replacing the Wbni and imposing registration, duty-of-care,
  incident-notification and board-accountability obligations on more than 8,000 organisations
  across 18 sectors, with registration in NCSC-NL's national entity register mandatory from that
  date. In Germany, BSI's own NIS2 landing page now carries the banner "Frist ist abgelaufen" and
  directs affected entities to register immediately. The only registration count traceable to an
  official document is the Federal Government's written answer to parliament: 11,388 entities
  registered as of 5 March 2026, against roughly 29,500 obligated — a gap widely reported as
  having narrowed since, on figures this run could not confirm from a BSI publication.
discovered_at: "2026-08-09T23:45:00Z"
updated_at: "2026-08-16T23:59:00Z"
event_date: 2026-08-09
run_id: 2026-08-09T2315Z-weekly
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - supply-chain
  - eu-nexus
regions:
  - europe
  - dach
  - switzerland
sectors:
  - public-sector
  - energy
  - water
  - transport
  - healthcare
  - finance
  - telco
entities:
  - "policy:netherlands-nis2-cyberbeveiligingswet-2026"
  - "policy:germany-nis2-registration-forbearance-2026"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht"
    publisher: Rijksoverheid (Ministerie van Justitie en Veiligheid)
    date: 2026-07-07
    role: primary
  - url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2"
    publisher: NCSC-NL
    date: 2026-08-09
    role: primary
  - url: "https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/nis-2-regulierte-unternehmen_node.html"
    publisher: "BSI (Bundesamt für Sicherheit in der Informationstechnik)"
    date: 2026-08-09
    role: primary
  - url: "https://dserver.bundestag.de/btd/21/046/2104657.pdf"
    publisher: Deutscher Bundestag / Bundesregierung
    date: 2026-03-13
    role: primary
  - url: "https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/260601_NIS2_BSI-Portal.html"
    publisher: BSI
    date: 2026-01-06
    role: corroborating
  - url: "https://www.ncsc.nl/nieuws/cbw-en-wwke-nu-van-kracht"
    publisher: NCSC-NL (Nationaal Cyber Security Centrum)
    date: 2026-08-15
    role: primary
  - url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2/registreren"
    publisher: NCSC-NL (Nationaal Cyber Security Centrum)
    date: 2026-08-15
    role: primary
  - url: "https://ees.nl/2026/08/11/nis2-is-definitief-cyberbeveiligingswet-gaat-op-15-augustus-in/"
    publisher: EES.nl
    date: 2026-08-11
    role: corroborating
closed_sources: []
evidence:
  - quote: De Eerste Kamer heeft op 7 juli ingestemd met de Cyberbeveiligingswet (Cbw) en de Wet weerbaarheid kritieke entiteiten (Wwke)... De wetten treden op 15 augustus 2026 in werking. Vanaf dat moment gelden nieuwe verplichtingen voor ruim 8000 organisaties in Nederland op het gebied van cyberbeveiliging.
    publisher: Rijksoverheid
  - quote: "Die gesetzliche Registrierungsfrist ist bereits abgelaufen. Von NIS-2 betroffen und noch nicht registriert? Dann jetzt umgehend im BSI-Portal registrieren!"
    publisher: BSI
  - quote: "Für rund 29.500 Unternehmen in Deutschland und Institutionen der Bundesverwaltung gelten seit Inkrafttreten des NIS-2-Umsetzungsgesetzes neue gesetzliche Pflichten in der IT-Sicherheit."
    publisher: BSI
  - quote: "Zum 5. März 2026 waren 11.388 wichtige und besonders wichtige Einrichtungen beim Bundesamt für Sicherheit in der Informationstechnik (BSI) registriert."
    publisher: Deutscher Bundestag / Bundesregierung
  - quote: "Vanaf vandaag, 15 augustus 2026, gelden de Cyberbeveiligingswet (Cbw) en de Wet weerbaarheid kritieke entiteiten (Wwke)."
    publisher: NCSC-NL
  - quote: De plicht geldt pas vanaf de inwerkingtreding van de Cyberbeveiligingswet (Cbw) op 15 augustus 2026.
    publisher: NCSC-NL
verification: multi-source
sourcing_note: >
  The German registration figures are deliberately split by provenance. BSI's own publications
  confirm the ~29,500 obligated-entity universe and, on its live landing page checked in this run,
  that the statutory registration deadline has expired. The only registration count traceable to
  an official document is the Federal Government's written answer to parliament (Drucksache
  21/4657): 11,388 as of 5 March 2026. A further count of roughly 18,500 by end of May 2026, and a
  31 July 2026 grace period, circulate widely attributed to BSI but could not be confirmed against
  any first-party BSI publication in this run, and are reported here as trade-press-attributed
  rather than as established fact.
confidence: medium
references: []
weekly_section: weekly-policy
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-16T23:59:00Z"
    run_id: 2026-08-16T2315Z-weekly
    type: update
    summary: >
      On 15 August 2026 the Cyberbeveiligingswet and the companion Wet weerbaarheid kritieke
      entiteiten entered into force, confirmed the same day by NCSC-NL, which stated the laws now
      apply and that organisations falling under them face new obligations. A prior weekly recorded
      this date as forthcoming; the delta is that it arrived and that the registration mechanics are
      now published. NCSC-NL's registration guidance states the duty applies from the entry into force
      of the Cyberbeveiligingswet on 15 August 2026 and describes no grace window, so an in-scope
      organisation that had not registered was out of compliance the moment the clock started.
      Registration runs through the national entity register, gated by eHerkenning at assurance level
      EH2+ or SSOnRijk for connected government bodies. For a Swiss federal SOC the obligation is
      Dutch, but the enforcement mechanics — portal registration with strong-authentication gating, no
      transition period, and supply-chain due diligence cascading onto unregulated vendors — are what
      Swiss suppliers selling into the Dutch and wider EU public sector will be asked to evidence.
    fields:
      - evidence
      - sources
      - tags
      - body
    merged_from: 2026-08-16/weekly-w33-dutch-nis2-in-force-no-transition
migrated_from: null
---

NIS2 has spent two years as a transposition story. This week it is an enforcement story in two member states at once, and the two are at opposite ends of the same process — which makes them more useful read together than separately.

The Dutch clock starts in six days. The Eerste Kamer approved the Cyberbeveiligingswet and the companion Wet weerbaarheid kritieke entiteiten on 7 July, and the government's announcement states that "de wetten treden op 15 augustus 2026 in werking. Vanaf dat moment gelden nieuwe verplichtingen voor ruim 8000 organisaties in Nederland op het gebied van cyberbeveiliging" — the laws enter into force on 15 August 2026, from which point new cyber-security obligations apply to more than 8,000 Dutch organisations ([Rijksoverheid, 2026-07-07](https://www.rijksoverheid.nl/actueel/nieuws/2026/07/07/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-15-augustus-2026-van-kracht)). The Cyberbeveiligingswet replaces the existing Wbni and covers essential and important service providers across 18 sectors including energy, drinking water, digital infrastructure, healthcare, government and transport. NCSC-NL's own page confirms the date and the first duty: registration in the national entity register is mandatory from 15 August ([NCSC-NL, checked 2026-08-09](https://www.ncsc.nl/cyberbeveiligingswet-nis2)). Three further duties attach — a duty of care to manage network and information-system security risks, an incident-notification duty to the organisation's CSIRT and competent authority, and board-level accountability with a training requirement — and organisations are themselves responsible for determining whether they fall in scope, which is the provision that generates the most work.

Germany shows what the same process looks like eighteen months later. BSI's NIS2 landing page, fetched during this run, carries the banner "Frist ist abgelaufen" over the text "Die gesetzliche Registrierungsfrist ist bereits abgelaufen. Von NIS-2 betroffen und noch nicht registriert? Dann jetzt umgehend im BSI-Portal registrieren!" ([BSI, checked 2026-08-09](https://www.bsi.bund.de/DE/Themen/Regulierte-Wirtschaft/NIS-2-regulierte-Unternehmen/nis-2-regulierte-unternehmen_node.html)) — the statutory deadline is past, and the authority is directing non-compliant entities to register immediately rather than describing an active grace period. BSI's own press release establishes the population: "für rund 29.500 Unternehmen in Deutschland und Institutionen der Bundesverwaltung gelten seit Inkrafttreten des NIS-2-Umsetzungsgesetzes neue gesetzliche Pflichten in der IT-Sicherheit" ([BSI, 2026-01-06](https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/260601_NIS2_BSI-Portal.html)). Against that, the only registration count this run could trace to an official document is the Federal Government's written answer to a parliamentary question: "Zum 5. März 2026 waren 11.388 wichtige und besonders wichtige Einrichtungen beim Bundesamt für Sicherheit in der Informationstechnik (BSI) registriert" ([Deutscher Bundestag, 2026-03-13](https://dserver.bundestag.de/btd/21/046/2104657.pdf)) — roughly 39% of the obligated population, counted the day before the statutory deadline. Higher figures for later dates, and an extension to 31 July 2026, circulate widely with attribution to BSI; this run could not confirm either against a first-party BSI publication, and they are noted here as such rather than repeated as fact.

**Defender takeaway:** two things follow for a Swiss organisation, neither of which is a Swiss obligation. First, the supplier tail: an organisation with Dutch entities, Dutch service providers or Dutch public-sector counterparts acquires a counterparty with a registration duty and an incident-notification duty from 15 August, and the notification duty in particular changes what a supplier will and will not tell you, and how fast, when it has an incident. Second, the German case is a calibration point for anyone estimating how quickly EU-wide NIS2 duties actually bind: the gap between an obligated population and a registered one remained large enough at the statutory deadline that the authority is still chasing registrations months later. Planning that assumes an EU supplier is NIS2-compliant because the deadline has passed is planning on the deadline rather than on the evidence.

## Update — 2026-08-16T23:59:00Z

The prior weekly recorded two NIS2 clocks running from opposite ends — the Dutch transposition law due to take effect on 15 August, and Germany's registration deadline already lapsed with BSI telling unregistered entities to register immediately. The Dutch half has now happened, and the mechanics that were not published then are published now.

NCSC-NL confirmed on the day: "Vanaf vandaag, 15 augustus 2026, gelden de Cyberbeveiligingswet (Cbw) en de Wet weerbaarheid kritieke entiteiten (Wwke)" — from today, 15 August 2026, the Cyberbeveiligingswet and the Critical Entities Resilience Act apply, and organisations falling under them face new obligations ([NCSC-NL, 2026-08-15](https://www.ncsc.nl/nieuws/cbw-en-wwke-nu-van-kracht)). The operative detail is in the registration guidance rather than the announcement. NCSC-NL states that the registration duty "geldt pas vanaf de inwerkingtreding van de Cyberbeveiligingswet (Cbw) op 15 augustus 2026" — applies only from the entry into force of the Act on 15 August 2026 ([NCSC-NL, 2026-08-15](https://www.ncsc.nl/cyberbeveiligingswet-nis2/registreren)). That sentence was written to answer the question organisations were asking before the date, and it answers a second one by omission: the guidance describes no transition period after it. An in-scope organisation that had not registered by the fifteenth was not working toward a deadline; it was already non-compliant. Registration runs through the national entity register and is gated by eHerkenning at assurance level EH2+, or SSOnRijk for connected government bodies — an authentication dependency that is itself a lead time for any organisation that does not already hold those credentials. Dutch compliance press reported the date independently ahead of it ([EES.nl, 2026-08-11](https://ees.nl/2026/08/11/nis2-is-definitief-cyberbeveiligingswet-gaat-op-15-augustus-in/)).

**Defender takeaway:** nothing here creates a Swiss obligation, and the contrast with Germany is the reason it is worth recording anyway. Two member states have now reached the enforcement phase by opposite routes — the Netherlands with a hard start and no grace period, Germany with a deadline that lapsed and a registration gap the federal authority has been publicly urging entities to close — which tells anyone planning against the directive that "transposition timetable" and "enforcement posture" are separate variables and the second is not predictable from the first. The concrete near-term reading for a Swiss public-sector or critical-infrastructure body is on the supplier side rather than the regulatory one: an organisation regulated under the Cbw must impose supply-chain due diligence on its own vendors, so Swiss suppliers into Dutch essential and important entities should expect those requirements to arrive contractually, and a Swiss body procuring from Dutch-regulated entities gains a lever it did not have before. The pattern to watch, since further member states will follow, is the shape rather than the dates: mandatory portal registration, strong-authentication gating, and obligations that bind from a fixed calendar date rather than phasing in.
