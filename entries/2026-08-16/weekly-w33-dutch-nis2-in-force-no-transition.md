---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "UPDATE — the Dutch NIS2 clock the prior weekly recorded as forthcoming started on 15 August, and the national CERT confirms the registration duty applies from the entry-into-force date itself with no transition window"
headline: "The Cyberbeveiligingswet is in force — registration is a live obligation from day one, not a deadline to work toward"
summary: >
  On 15 August 2026 the Cyberbeveiligingswet and the companion Wet weerbaarheid kritieke entiteiten entered
  into force, confirmed the same day by NCSC-NL, which stated the laws now apply and that organisations
  falling under them face new obligations. A prior weekly recorded this date as forthcoming; the delta is
  that it arrived and that the registration mechanics are now published. NCSC-NL's registration guidance
  states the duty applies from the entry into force of the Cyberbeveiligingswet on 15 August 2026 and
  describes no grace window, so an in-scope organisation that had not registered was out of compliance the
  moment the clock started. Registration runs through the national entity register, gated by eHerkenning at
  assurance level EH2+ or SSOnRijk for connected government bodies. For a Swiss federal SOC the obligation
  is Dutch, but the enforcement mechanics — portal registration with strong-authentication gating, no
  transition period, and supply-chain due diligence cascading onto unregulated vendors — are what Swiss
  suppliers selling into the Dutch and wider EU public sector will be asked to evidence.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-15"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [supply-chain, eu-nexus]
regions: [europe, switzerland]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities:
  - policy:netherlands-nis2-cyberbeveiligingswet-2026
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.ncsc.nl/nieuws/cbw-en-wwke-nu-van-kracht"
    publisher: "NCSC-NL (Nationaal Cyber Security Centrum)"
    date: "2026-08-15"
    role: primary
  - url: "https://www.ncsc.nl/cyberbeveiligingswet-nis2/registreren"
    publisher: "NCSC-NL (Nationaal Cyber Security Centrum)"
    date: "2026-08-15"
    role: primary
  - url: "https://ees.nl/2026/08/11/nis2-is-definitief-cyberbeveiligingswet-gaat-op-15-augustus-in/"
    publisher: "EES.nl"
    date: "2026-08-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Vanaf vandaag, 15 augustus 2026, gelden de Cyberbeveiligingswet (Cbw) en de Wet weerbaarheid kritieke entiteiten (Wwke)."
    publisher: "NCSC-NL"
  - quote: "De plicht geldt pas vanaf de inwerkingtreding van de Cyberbeveiligingswet (Cbw) op 15 augustus 2026."
    publisher: "NCSC-NL"
verification: single-source-national-cert
sourcing_note: >
  Carried on the national CERT's own announcement and its own registration guidance, which is the first-party
  authority for the legal-effect date in its own jurisdiction; Dutch compliance press corroborates the date
  independently. The absence of a transition window is stated as an absence — NCSC-NL's guidance describes
  none — rather than as a positive statement that one was ruled out. No penalty regime or first enforcement
  date is stated in the cited pages and none is asserted here.
confidence: high
update_of: 2026-08-09/weekly-w32-nis2-enforcement-phase-netherlands-germany
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-09):** the prior weekly recorded two NIS2 clocks running from opposite ends — the Dutch transposition law due to take effect on 15 August, and Germany's registration deadline already lapsed with BSI telling unregistered entities to register immediately. The Dutch half has now happened, and the mechanics that were not published then are published now.

NCSC-NL confirmed on the day: "Vanaf vandaag, 15 augustus 2026, gelden de Cyberbeveiligingswet (Cbw) en de Wet weerbaarheid kritieke entiteiten (Wwke)" — from today, 15 August 2026, the Cyberbeveiligingswet and the Critical Entities Resilience Act apply, and organisations falling under them face new obligations ([NCSC-NL, 2026-08-15](https://www.ncsc.nl/nieuws/cbw-en-wwke-nu-van-kracht)). The operative detail is in the registration guidance rather than the announcement. NCSC-NL states that the registration duty "geldt pas vanaf de inwerkingtreding van de Cyberbeveiligingswet (Cbw) op 15 augustus 2026" — applies only from the entry into force of the Act on 15 August 2026 ([NCSC-NL, 2026-08-15](https://www.ncsc.nl/cyberbeveiligingswet-nis2/registreren)). That sentence was written to answer the question organisations were asking before the date, and it answers a second one by omission: the guidance describes no transition period after it. An in-scope organisation that had not registered by the fifteenth was not working toward a deadline; it was already non-compliant. Registration runs through the national entity register and is gated by eHerkenning at assurance level EH2+, or SSOnRijk for connected government bodies — an authentication dependency that is itself a lead time for any organisation that does not already hold those credentials. Dutch compliance press reported the date independently ahead of it ([EES.nl, 2026-08-11](https://ees.nl/2026/08/11/nis2-is-definitief-cyberbeveiligingswet-gaat-op-15-augustus-in/)).

**Defender takeaway:** nothing here creates a Swiss obligation, and the contrast with Germany is the reason it is worth recording anyway. Two member states have now reached the enforcement phase by opposite routes — the Netherlands with a hard start and no grace period, Germany with a deadline that lapsed and a registration gap the federal authority has been publicly urging entities to close — which tells anyone planning against the directive that "transposition timetable" and "enforcement posture" are separate variables and the second is not predictable from the first. The concrete near-term reading for a Swiss public-sector or critical-infrastructure body is on the supplier side rather than the regulatory one: an organisation regulated under the Cbw must impose supply-chain due diligence on its own vendors, so Swiss suppliers into Dutch essential and important entities should expect those requirements to arrive contractually, and a Swiss body procuring from Dutch-regulated entities gains a lever it did not have before. The pattern to watch, since further member states will follow, is the shape rather than the dates: mandatory portal registration, strong-authentication gating, and obligations that bind from a fixed calendar date rather than phasing in.
