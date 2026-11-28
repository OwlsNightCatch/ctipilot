---
schema: 1
kind: incident
title: "French Éducation nationale: a hijacked staff account reached the agent-training system, exposing identity and NIR data for everyone who has worked in an académie since 2001"
headline: "France's education ministry confirms a third 2026 data incident, this one reached through a hijacked staff account"
summary: >
  France's Ministère de l'Éducation nationale confirmed on 2026-07-31 that a compromised professional account was used
  overnight on 2026-07-25 to reach the ministry's internal agent-training information system. Identity and professional
  data for every agent who has worked in a French académie since 2001 was present in the environment, and for a subset
  also postal address, telephone number and French social-security number (NIR); the ministry states the system held
  no passwords, no banking details and no pupil data. External access was suspended on 26 July, ANSSI and the CNIL were
  notified and a criminal complaint filed. It is the third confirmed Éducation nationale data-security incident of
  2026, after a March breach of the COMPAS trainee-management system and an April incident exposing pupil data.
discovered_at: "2026-08-01T04:25:02Z"
event_date: "2026-07-25"
run_id: 2026-08-01T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity]
regions: [europe]
sectors: [public-sector, education]
entities: [incident:france-education-nationale-agent-training-breach-2026-07]
techniques: [T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/"
    publisher: "Cyberattaque.org"
    date: "2026-07-31"
    role: primary
  - url: "https://www.franceinfo.fr/societe/education/potentiel-vol-de-donnees-personnelles-d-un-nombre-important-d-agents-de-l-education-nationale_8130599.html"
    publisher: "franceinfo (France Télévisions)"
    date: "2026-07-31"
    role: corroborating
  - url: "https://www.clubic.com/actualite-623734-nouvelle-cyberattaque-contre-l-education-nationale-les-donnees-d-un-grand-nombre-d-agents-potentiellement-dans-la-nature.html"
    publisher: "Clubic"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Dans la nuit du 25 juillet 2026, un compte professionnel compromis a permis à un attaquant d'accéder au système d'information consacré à la formation des agents."
    publisher: "Cyberattaque.org"
  - quote: "Le ministère précise que l'environnement compromis ne contenait aucun mot de passe, aucune coordonnée bancaire et aucune information relative aux élèves."
    publisher: "Cyberattaque.org"
  - quote: "Le nombre exact de personnes concernées n'est pas encore communiqué. La formule employée par le ministère indique que l'ensemble des agents enregistrés depuis 2001 est potentiellement exposé, sans établir que toutes les fiches ont effectivement été consultées ou téléchargées."
    publisher: "Cyberattaque.org"
verification: multi-source
sourcing_note: >
  Three French outlets reported the incident on 2026-07-31, each relaying the ministry's own statement; no ministry
  communiqué for this July incident was located, and the ministry page that exists on the education.gouv.fr site
  covers the separate March 2026 COMPAS incident, so it is not cited here as a source for this one. The primary source
  hedges the initial-access mechanism for this incident ("l'intrusion aurait débuté après la compromission d'un compte
  professionnel") and states explicitly that the absence of multi-factor authentication on the account has not been
  publicly confirmed; both hedges are preserved. No cited source states how the March or April incidents began, so
  this entry claims no shared access path across the three, and the April incident is described by the sources as
  exposing pupil rather than personnel data. The scope figure describes records present in the environment, not
  records confirmed accessed — the source is explicit that this distinction is unresolved.
confidence: medium
update_of: null
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

France's Ministère de l'Éducation nationale confirmed a new intrusion on 2026-07-31, and the access path is the notable part: "dans la nuit du 25 juillet 2026, un compte professionnel compromis a permis à un attaquant d'accéder au système d'information consacré à la formation des agents" — overnight on 25 July, a compromised staff account let an attacker into the information system dedicated to managing agent training ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)). franceinfo describes the same event as fraudulent access carried out during the night of 25 July following usurpation of a professional account ([franceinfo, 2026-07-31](https://www.franceinfo.fr/societe/education/potentiel-vol-de-donnees-personnelles-d-un-nombre-important-d-agents-de-l-education-nationale_8130599.html)). The reporting describes the access as running through a hijacked legitimate credential into an application that centralises personnel records, and the primary source frames it as not having required the exploitation of a complex technical vulnerability — a formulation that stops short of ruling one out entirely, and this entry keeps that register.

The scope is broad but carefully bounded by the ministry's own wording. The environment held identity and professional data — surname and forename, identity details, function, and the history of service in an académie — for every agent who has worked in a French académie since 2001, with postal address, telephone number and social-security number (NIR) present for a subset ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)). Crucially, that describes what was *in* the environment rather than what was taken: the primary source states that the exact number of people concerned has not been communicated and that the ministry's formulation indicates all agents registered since 2001 are potentially exposed "sans établir que toutes les fiches ont effectivement été consultées ou téléchargées" — without establishing that every record was actually viewed or downloaded ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)). The ministry states the compromised environment contained no passwords, no banking details and no pupil information ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)), a point Clubic reports in the same terms from the rue de Grenelle ([Clubic, 2026-07-31](https://www.clubic.com/actualite-623734-nouvelle-cyberattaque-contre-l-education-nationale-les-donnees-d-un-grand-nombre-d-agents-potentiellement-dans-la-nature.html)).

Containment and notification followed within a day: the ministry's security operations centre was alerted on 26 July, external access to the affected application was suspended, a crisis cell was activated, and checks were launched across other ministry systems for propagation, further compromised accounts or persistent access left behind; ANSSI and the CNIL have been notified and a criminal complaint filed ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)).

**Defender takeaway:** the recurrence is the lesson, not the single event. This is the third confirmed Éducation nationale data-security incident of 2026 — in March roughly 243,000 agent and trainee records were exfiltrated from the COMPAS trainee-management system, and in April a separate attack exposed pupil data through a service linked to ÉduConnect ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)). None of the cited reporting states how the two earlier intrusions began, so no shared root cause can be claimed across all three; what is established for this one is that a working staff credential against a centralised personnel platform reachable from outside was enough to reach the records, with no complex exploitation described by any source. The remediation the ministry applied — suspending external access to the application — is the posture such a system arguably warranted beforehand. The same shape exists in any public-sector body that runs a central personnel or training platform with externally reachable authentication. Note also what the exposed data enables downstream: knowing an agent's function and académie makes a fake rectorat, HR-service or training-body message highly credible, and the primary source lists exactly that set of follow-on frauds — bogus training summons, fraudulent administrative-record update requests, professional-credential theft and identity usurpation using the NIR ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)).

**Triage:** an HR or training administrator legitimately reads many personnel records, so volume alone is not the signal. The discriminating combination available in this case's telemetry is an interactive sign-in to a personnel or training application outside working hours — this intrusion ran overnight — from a staff account whose prior session history shows no bulk-record or export activity, followed immediately by broad sequential record access. Identity-provider sign-in logs (new device, unfamiliar location, off-hours) correlated against the application's own record-access and export audit trail is where that pattern surfaces; either half alone is weak. The ministry has not stated whether multi-factor authentication was in force on the account, and the primary source is explicit that this remains unconfirmed publicly ([Cyberattaque.org, 2026-07-31](https://www.cyberattaque.org/education-nationale-25-ans-de-donnees-dagents-potentiellement-exposees-apres-une-cyberattaque/)), so no inference is drawn here about which control failed.
