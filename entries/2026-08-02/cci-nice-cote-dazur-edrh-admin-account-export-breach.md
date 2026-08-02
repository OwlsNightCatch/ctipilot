---
schema: 1
kind: incident
horizon: operational
title: "CCI Nice Côte d'Azur: a compromised administrator account on the chamber's jobseeker platform was used to run the platform's own export function"
headline: "A French public-law chamber of commerce confirms bulk candidate-data exports run from a hijacked admin account, with the takeover route undisclosed"
summary: >
  The Chambre de commerce et d'industrie Nice Côte d'Azur, the French public-law chamber of commerce for the
  Alpes-Maritimes, has notified affected individuals that an unauthorised party reached an administrator account
  on its eDRH candidate-and-company platform on 2026-07-18 and used it to generate several data exports.
  Exposed fields include name, email, phone number, date of birth, professional history, education level and
  account timestamps — enough to impersonate a recruiter or a chamber adviser convincingly. The chamber has not
  disclosed how the account was taken over, how long the access lasted, or how many people are affected.
discovered_at: "2026-08-02T04:09:57Z"
event_date: "2026-07-18"
run_id: 2026-08-02T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity, phishing]
regions: [europe]
sectors: [public-sector, education]
entities: [incident:cci-nice-cote-dazur-edrh-breach-2026-07]
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/"
    publisher: "Cyberattaque.org"
    date: "2026-08-01"
    role: primary
  - url: "https://frenchbreaches.com/alertes/chambre-de-commerce-et-d-industrie-nice-c-te-d-azur-ms9972qijqoesdq8cu"
    publisher: "FrenchBreaches.com"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "un accès non autorisé à un compte administrateur a permis la réalisation de plusieurs exports contenant des informations sur des candidats et des entreprises"
    publisher: "Cyberattaque.org"
  - quote: "Un attaquant connaissant le parcours, le niveau d'études et les coordonnées d'un candidat peut se faire passer pour un recruteur, une entreprise ou un conseiller de la CCI."
    publisher: "Cyberattaque.org"
verification: single-source
sourcing_note: >
  Both cited sites are French breach-notification trackers reproducing the same underlying document — the
  chamber's own notification to affected individuals — so they are two write-ups of one source rather than two
  independent confirmations. No official CCI Nice Côte d'Azur incident page and no mainstream-press pickup was
  found. The facts below are therefore the chamber's own account as relayed, and the record is graded and framed
  accordingly.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

The Chambre de commerce et d'industrie Nice Côte d'Azur — the public-law chamber of commerce serving businesses and project founders in the Alpes-Maritimes — has confirmed a security incident affecting its eDRH platform, which brings together candidate profiles and registered companies around employment and recruitment. On 2026-07-18, "un accès non autorisé à un compte administrateur a permis la réalisation de plusieurs exports contenant des informations sur des candidats et des entreprises" — an unauthorised party reached an account holding administrator rights and used it to generate several exports covering registered candidates and enrolled companies ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)). This was not a blocked attempt — files were actually produced — and the chamber has not published the number of people affected or the total volume exported ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)). A second French breach tracker reproduces the same notification ([FrenchBreaches.com, 2026-07-31](https://frenchbreaches.com/alertes/chambre-de-commerce-et-d-industrie-nice-c-te-d-azur-ms9972qijqoesdq8cu)).

Per the notification sent to affected individuals, the fields that may have been consulted or exported are surname and first name, email address, telephone number, date of birth, professional experience and career history, education level, profile title and stated attributes, contact and notification preferences, account-creation date and last-login date ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)). The chamber says it engaged technical measures with its service provider on detection to end the unauthorised access and secure the platform, and it does not say how long the account remained accessible or how many exports ran before it was blocked. Cyberattaque.org adds in its own voice — not as a statement from the chamber — that nothing disclosed supports a conclusion that the chamber's wider IT estate was compromised ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)).

How the account was taken over is explicitly not stated. The relayed account lists a stolen password, a phishing campaign, credential reuse and session hijacking as the possibilities without selecting one ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)) — a gap worth stating plainly rather than filling, because it is the one fact that would tell another public body which control to check first.

Detection concepts follow from what the attacker actually did after authenticating, which is the reason this is worth carrying despite the thin technical detail: no tooling was deployed and nothing was exploited on the way out. Once holding administrator rights, the intruder used the platform's own legitimate export functions to retrieve candidate and company lists. How those rights were obtained is a separate and undisclosed question — the possibilities the notification's relay lists include session hijacking, which can itself involve a software flaw, so this is not a case where the absence of a vulnerability has been established. The telemetry that catches this sits in the SaaS or hosted application's own audit log rather than in endpoint or network telemetry — administrative authentication events assessed against the account's normal geography, hours and device, followed by export or bulk-read operations assessed against that account's normal export volume and cadence. **Triage:** administrators of an HR or CRM platform legitimately run exports, so the export event alone discriminates nothing; the separating signals are an export by an account that has never run one, a run of exports compressed into a single session, and an export whose result-set size has no precedent for that account — and, upstream, an administrative sign-in whose source or timing breaks that account's own pattern.

**Defender takeaway:** for any public body whose candidate, citizen or client data lives on a third-party-operated HR or CRM platform, the control that mattered here is not on the perimeter — it is administrator-account protection on the platform itself plus export-volume alerting inside it, and both are usually the provider's to configure rather than the customer's to deploy. The secondary risk is downstream and specific: the exposed combination of career history, education level and contact details is exactly what a convincing fake recruiter, fake application follow-up or fake chamber-adviser message needs, and the relayed notification names precisely that — an attacker holding a candidate's background and contact details "peut se faire passer pour un recruteur, une entreprise ou un conseiller de la CCI" ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/)).
