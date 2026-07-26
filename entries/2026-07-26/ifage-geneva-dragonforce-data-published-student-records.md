---
schema: 1
kind: incident
horizon: operational
title: "IFAGE Geneva — DragonForce publishes the stolen data, exposing student exam results the institute had said were unaffected"
headline: "The IFAGE Geneva leak went from claim to publication, and it contradicts the victim's own scoping of the breach"
summary: >
  DragonForce published the data it stole from IFAGE, the Geneva adult-education foundation, on
  2026-07-23. The published set includes identity-document
  photographs, e-mail and postal addresses, telephone numbers and multi-year student exam
  results running to 2026 — categories that contradict the institute's earlier public position
  that the incident affected employee data rather than student and pedagogical records. The
  disclosure covers both staff and beneficiaries; the group posted a ransom ultimatum that IFAGE says never reached it; it has filed a criminal complaint and is working with cantonal police and
  federal authorities.
discovered_at: "2026-07-26T13:58:00Z"
event_date: "2026-07-23"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland, europe]
sectors: [education, public-sector]
entities: [actor:dragonforce, incident:ifage-geneva-dragonforce-leak-claim-2026-07]
techniques: [T1657, T1567.002]
affected_products: []
cves: []
sources:
  - url: "https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147"
    publisher: "20 minutes (Switzerland)"
    date: "2026-07-24"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse"
    publisher: "ICTjournal"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Des photos de pièces d'identité, des adresses e-mail et postales, ainsi que des numéros de téléphone ou encore des résultats d'examens ont été publiés."
    publisher: "20 minutes"
  - quote: "Leur divulgation par les cybercriminels concerne tant des employés de l'institut que des bénéficiaires (étudiants, entreprises, etc.)."
    publisher: "20 minutes"
verification: contradicted
sourcing_note: "The publication event itself is carried by a single Swiss outlet (20 minutes, relaying Le Temps's review of the leaked set); ICTjournal corroborates the preceding extortion threat but predates the publication. Reliability C reflects re-reporting rather than first-party or original-research sourcing."
confidence: medium
update_of: 2026-07-14/dragonforce-leak-claim-ifage-geneva-adult-education
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

**UPDATE (originally covered 2026-07-14):** the DragonForce listing against IFAGE — the Fondation pour la formation des adultes à Genève — is no longer an unverified leak-site claim. The group carried out its threat and published the data, which Le Temps reported had been done as of Thursday 2026-07-23: "Des photos de pièces d'identité, des adresses e-mail et postales, ainsi que des numéros de téléphone ou encore des résultats d'examens ont été publiés." — identity-document photographs, e-mail and postal addresses, telephone numbers and examination results ([20 minutes, 2026-07-24](https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147)). The same report states that their disclosure by the cybercriminals "concerne tant des employés de l'institut que des bénéficiaires (étudiants, entreprises, etc.)" — it covers both the institute's employees and its beneficiaries, meaning students and companies. It also cites an expert consulted by Le Temps who put the exposure at thousands of documents spanning several years and running to 2026. ICTjournal had reported the extortion threat a week earlier ([ICTjournal, 2026-07-17](https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse)).

The operationally interesting part is the gap between the victim's scoping and the published set. IFAGE's earlier public account of its incident placed the impact on employee data rather than student or pedagogical records; the leak contains multi-year examination results for students. First coverage flagged that the group's claimed volume already exceeded the institute's own disclosure, and publication has now settled that discrepancy in the attackers' favour. Nothing in the reporting identifies the initial-access vector, so no access-path lesson is available from this incident.

**Contradiction:** the sources and the victim do not agree on whether a ransom was ever demanded, and this entry does not resolve it. 20 minutes frames the publication as the consequence of an unpaid demand — "Si la rançon demandée n'était pas payée, les pirates informatiques qui s'en sont pris en avril à l'Ifage (Fondation pour la formation des adultes à Genève) promettaient de mettre en ligne les données dérobées" — while also reporting the foundation's own position that "La fondation avait aussi affirmé qu'elle n'avait pas reçu de demande de rançon, mais que, le cas échéant, elle refuserait de payer": it had received no ransom demand, but would refuse to pay if one came ([20 minutes, 2026-07-24](https://www.20min.ch/fr/story/geneve-les-hackers-de-l-institut-ifage-ont-mis-leurs-menaces-a-execution-103608147)). ICTjournal is more definite on the demand's existence, reporting a week earlier that a ransom was now being demanded and that the group threatened to publish at the expiry of the ultimatum posted on its leak site ([ICTjournal, 2026-07-17](https://www.ictjournal.ch/news/2026-07-17/cyberattaque-contre-lifage-les-pirates-de-dragonforce-menacent-de-publier-la-masse)). A leak-site ultimatum naming a ransom the victim says never reached it is a common pattern and not necessarily either party misspeaking — demands are frequently posted publicly rather than delivered.

**Defender takeaway:** for Swiss and European public-sector and education bodies, the reusable point is about disclosure discipline under extortion rather than about DragonForce's tradecraft. A scope statement issued before forensics are complete tends to describe what the victim has confirmed, not what the attacker holds, and a leak-site publication is the moment that difference becomes public — organisations should scope their public statements to what they can defend after the data is released, and plan notification obligations for the categories in the attacker's possession rather than the categories confirmed so far. Where an institution's records include identity documents and examination results, the affected-person notification set extends well beyond staff.
