---
schema: 1
kind: incident
horizon: operational
title: "A Valais commune's secretariat mailbox was compromised on 10 August and sat quiet until the attacker used it on 18 August to mail roughly 450 of the commune's own contacts — the send is what triggered detection"
headline: "Eight days of undetected mailbox access at a Swiss communal administration, ended not by monitoring but by the attacker making noise"
summary: >
  The commune of Martigny-Combe in Valais disclosed on 2026-08-20 that its municipal secretariat's
  professional mailbox had been accessed without authorisation. Its external IT-security contractor
  traced the compromise to 10 August, when an employee opened a malicious email without realising it;
  nothing surfaced until 18 August, when the attacker used the trusted communal mailbox to send a
  fraudulent message to roughly 450 people, which is what caused the commune to notice. Around 300
  emails and their attachments were taken, described by the commune president as confidential and in
  places containing sensitive data, and two recipients are known to have clicked the fraudulent link.
  The commune blocked the mailbox, notified the federal cybersecurity office and the Valais cantonal
  data protection commissioner, has a criminal complaint with the cantonal police in progress, and says
  it will keep a year-long watch for the stolen data.
discovered_at: "2026-08-23T05:15:00Z"
event_date: "2026-08-18"
run_id: 2026-08-23T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity]
regions: [switzerland, europe]
sectors: [public-sector]
entities: []
techniques: [T1566, T1114, T1586.002]
affected_products: []
cves: []
sources:
  - url: "https://www.lenouvelliste.ch/valais/bas-valais/martigny-district/martigny-combe-commune/cyberattaque-a-la-commune-de-martigny-combe-300-courriels-contenant-des-donnees-sensibles-ont-ete-voles-1511002"
    publisher: "Le Nouvelliste"
    date: "2026-08-20"
    role: primary
  - url: "https://martigny-combe.ch/uploads/default/id-1515-Communique-presse-incident-secu--20-08-26-.pdf"
    publisher: "Commune de Martigny-Combe"
    date: "2026-08-20"
    role: primary
  - url: "https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise"
    publisher: "ICTjournal"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "L'entreprise externe gérant la sécurité informatique de la commune a pu identifier que le piratage remontait au 10 août. Une personne avait alors ouvert un mail contaminé reçu sur la messagerie du secrétariat communal, sans s'en rendre compte."
    publisher: "Le Nouvelliste"
  - quote: "L'incident a été détecté le 18 août 2026"
    publisher: "Commune de Martigny-Combe"
verification: multi-source
sourcing_note: >
  The access vector and the timeline are Le Nouvelliste's own reporting, attributed to the commune's
  external IT-security contractor and corroborated by an on-record quote from the commune president —
  the commune's own communiqué names no vector and gives no figure for the stolen mail, so the
  approximately-300 count is the newspaper's characterisation rather than an official number, and is
  presented as such. Sources are quoted in the original French with an English gloss because the
  precision of the contractor's finding is what licenses this entry's technique mapping. The
  commune's own communiqué was recovered directly from its website as a PDF. No source names the
  commune's data-protection delegate as the same firm that performed the forensic work, so this entry
  does not connect them.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The commune of Martigny-Combe, in the Bas-Valais, disclosed on 2026-08-20 that the professional mailbox of its municipal secretariat had been accessed without authorisation. Its own communiqué is brief and gives a detection date — *"L'incident a été détecté le 18 août 2026"* — the mailbox was blocked immediately, external specialists were engaged, the federal cybersecurity office and the Valais cantonal data protection and transparency commissioner were notified, and a criminal complaint with the Valais cantonal police was recorded as in progress rather than filed ([Commune de Martigny-Combe, 2026-08-20](https://martigny-combe.ch/uploads/default/id-1515-Communique-presse-incident-secu--20-08-26-.pdf)).

The part that makes this worth a defender's time is in Le Nouvelliste's reporting rather than the communiqué, and it is attributed to the commune's own external IT-security contractor: *"L'entreprise externe gérant la sécurité informatique de la commune a pu identifier que le piratage remontait au 10 août. Une personne avait alors ouvert un mail contaminé reçu sur la messagerie du secrétariat communal, sans s'en rendre compte"* — the external firm managing the commune's IT security established that the compromise dated back to 10 August, when someone opened a contaminated email received on the communal secretariat's mailbox without realising it ([Le Nouvelliste, 2026-08-20](https://www.lenouvelliste.ch/valais/bas-valais/martigny-district/martigny-combe-commune/cyberattaque-a-la-commune-de-martigny-combe-300-courriels-contenant-des-donnees-sensibles-ont-ete-voles-1511002)).

That gives the incident a shape worth naming: **eight days of access that produced no detectable signal, ended by the attacker's own outbound activity.** On 18 August the mailbox was used to send a fraudulent message to roughly 450 people — the commune's own correspondents, receiving mail from a genuine communal address — and it is that send, not any monitoring control, that surfaced the intrusion. The commune president is quoted on the record saying that to the commune's knowledge two recipients had clicked the fraudulent link at the time of reporting. Around 300 emails and their attachments were taken from the mailbox, which he characterises as confidential and in places containing sensitive data; that figure is the newspaper's own count, and the commune's communiqué gives none. The commune says it will maintain a year-long watch for the stolen data appearing online.

**Defender takeaway:** for small public administrations the operative lesson is the detection gap, not the phishing. A single mailbox compromise at a commune generates almost no telemetry that a small IT function is positioned to see — no malware on an endpoint, no lateral movement, no unusual volume — until the account is used to send. Where a full monitoring capability is out of reach, the cheap controls that would have shortened those eight days are all mailbox-level and available in any hosted mail platform: alerting on new mailbox forwarding or delegation rules, on sign-ins from unfamiliar locations to shared or role mailboxes, and on outbound volume from an account that normally sends in single digits. The second-order exposure is the one that reaches beyond the commune: a message from a real government address, to a list the government itself maintains, defeats sender-reputation and domain-authentication checks entirely, because the domain is genuine. **Triage:** a role mailbox legitimately sends bulk correspondence, so volume alone is weak; the discriminators are whether the send correlates with an actual communal mailing, whether the message carries a link to a domain the commune does not own, and whether the sending session's location matches the staff who operate that mailbox.
