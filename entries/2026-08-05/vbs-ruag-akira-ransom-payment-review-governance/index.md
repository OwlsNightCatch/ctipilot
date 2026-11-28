---
schema: 1
kind: policy
title: "Swiss Defence Department closes its RUAG review: the Akira ransom payment broke no law, but the risk weighing and the owner notification were deficient — and the federal no-payment recommendation stands"
headline: "Bern rules a federally-owned firm's ransom payment lawful, faults the governance, and reaffirms not to pay"
summary: >
  On 2026-08-04 the Swiss Defence Department (VBS) published the outcome of its ownership review into
  how RUAG MRO handled the Akira ransomware attack on its US subsidiary RUAG LLC, detected 9-10 October
  2025, in which data was stolen and a ransom was paid. VBS finds no indication of a legal violation —
  the decision sat with the company's own corporate bodies and required no prior consent from the
  Confederation as owner — but faults RUAG MRO for weighing the decision mainly on legal and economic
  grounds without sufficient regard for political and reputational consequences, and for not informing
  the owner before communicating publicly. The federal recommendation not to pay is explicitly
  unchanged.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-04"
run_id: 2026-08-05T0412Z-intel
priority: notable
immediate_action: null
tags: [ransomware, law-enforcement]
regions: [switzerland]
sectors: [public-sector, defense]
entities: [actor:akira, incident:ruag-mro-akira-ransom-payment-review-2026]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.vbs.admin.ch/de/newnsb/5bBC1HPXGI21"
    publisher: "Eidgenössisches Departement für Verteidigung, Bevölkerungsschutz und Sport (VBS)"
    date: "2026-08-04"
    role: primary
  - url: "https://www.srf.ch/news/schweiz/nach-cyberangriff-loesegeldzahlung-der-ruag-an-hackergruppe-war-gesetzeskonform"
    publisher: "SRF"
    date: "2026-08-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Die Untersuchung kommt zum Schluss, dass der Entscheid der RUAG MRO zur Zahlung eines Lösegelds im Rahmen ihrer unternehmerischen Verantwortung getroffen wurde und keine Anhaltspunkte für eine Rechtsverletzung bestehen."
    publisher: "VBS"
  - quote: "Nach Einschätzung des VBS wurden politische und reputationsbezogene Auswirkungen sowie weitere übergeordnete Interessen nicht ausreichend berücksichtigt."
    publisher: "VBS"
  - quote: "Das VBS und der Bund halten unverändert an ihrer Empfehlung fest, im Falle von Cyber-Angriffen kein Lösegeld zu bezahlen."
    publisher: "VBS"
verification: multi-source
sourcing_note: "VBS is the primary and the disclosing party for its own review; SRF corroborates and adds that RUAG leadership described the sum paid as small without naming a figure. Neither source describes the intrusion vector, dwell time or tooling, so this entry maps no attacker techniques."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The Swiss Defence Department published the result of its ownership review into RUAG MRO on 2026-08-04, covering the Akira ransomware attack on its US subsidiary RUAG LLC detected on 9 and 10 October 2025, in which data was stolen from the subsidiary's systems and a ransom was subsequently paid ([VBS, 2026-08-04](https://www.vbs.admin.ch/de/newnsb/5bBC1HPXGI21)). The finding is the first written federal position on a Swiss state-owned company paying an extortion crew, and it separates two questions that are usually argued as one.

On legality, VBS concludes that RUAG MRO's decision to pay was taken within its own corporate responsibility and that there are no indications of a legal violation ([VBS, 2026-08-04](https://www.vbs.admin.ch/de/newnsb/5bBC1HPXGI21)). The company checked the lawfulness of the payment under applicable US law before paying, and as a company organised under private law the decision sat with its own corporate bodies, requiring no prior consent from the Confederation as owner. SRF reports that RUAG leadership described the amount as small without naming a figure ([SRF, 2026-08-04](https://www.srf.ch/news/schweiz/nach-cyberangriff-loesegeldzahlung-der-ruag-an-hackergruppe-war-gesetzeskonform)).

On governance, the department is critical. VBS assesses that political and reputational consequences, along with further overriding interests, were not sufficiently taken into account ([VBS, 2026-08-04](https://www.vbs.admin.ch/de/newnsb/5bBC1HPXGI21)) — the weighing ran on legal and economic considerations alone. The second fault is sequencing: the Federal Council's strategic objectives for RUAG MRO require the owner to be informed before public communication, and that did not happen in a coordinated way. RUAG MRO's own post-incident analysis identified escalation processes at subsidiaries, IT governance including the role of the group IT lead, crisis-communication processes and minimum IT security requirements as the weak points, and is remediating them under reporting duties to the VBS general secretariat and the Federal Finance Administration. The Confederation as owner additionally directs RUAG MRO to review its protective measures with the Bundesamt für Cybersicherheit and have the overall adequacy of its cyber protection assessed. No further ownership-law measures follow.

The policy line is stated without ambiguity in the same document: VBS and the Confederation maintain their recommendation not to pay a ransom in the event of cyberattacks ([VBS, 2026-08-04](https://www.vbs.admin.ch/de/newnsb/5bBC1HPXGI21)). A finding of lawfulness is not an endorsement, and the review says so.

**Why this matters past RUAG.** Three things transfer to any Swiss or European state-owned entity, cantonal utility or critical-infrastructure operator. First, the decision rights are now on the record: for a company under private law, paying is a corporate decision that does not require the owner's consent — while the owner's standing recommendation against it is reaffirmed in the same breath. Anyone drafting or reviewing a ransom-decision playbook now has a concrete precedent for how that tension resolves in practice, and for the fact that the reputational and political dimension is expected to appear in the decision record rather than only the legal and economic one. Second, the named failure mode is subsidiary escalation, not the encryption event: the incident happened at a foreign subsidiary, and the weaknesses the company itself identified are group-level escalation, governance and minimum security baselines that stopped at the parent's own perimeter. Group incident response that does not reach into subsidiaries is where this went wrong. Third, notification obligations turned out to be ordered rather than merely present — informing the owner before going public is a sequencing duty, and missing the order was itself a finding.
