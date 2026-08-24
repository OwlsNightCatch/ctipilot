---
schema: 1
kind: incident
horizon: operational
title: "Martigny-Combe (Valais): a Swiss communal secretariat's mailbox was used to mail the administration's own contact list, and the municipality can still only say data 'could' have been disclosed"
headline: "A Valais municipality detected the compromise only when the mailbox mailed everyone it knew — the second Valais communal case this year"
summary: >
  The Valais municipality of Martigny-Combe states it detected unauthorised access to its communal
  secretariat's professional mailbox on 2026-08-18, when that mailbox was used to send a fraudulent message
  to the administration's contacts. Its own communiqué goes no further than saying the incident could have
  led to personal data in the mailbox being disclosed to an unauthorised third party, and it is still
  determining the extent with external specialists; regional reporting states that around 300 emails
  containing sensitive data were taken and dates the attack to 10 August, eight days before detection. The
  municipality notified the Federal Office for Cybersecurity and the cantonal data-protection commissioner
  and is filing a criminal complaint with Valais cantonal police.
discovered_at: "2026-08-22T04:45:00Z"
event_date: "2026-08-18"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity]
regions: [switzerland]
sectors: [public-sector]
entities: [incident:martigny-combe-email-compromise-2026-08]
techniques: [T1078, T1114, T1534]
affected_products: []
cves: []
sources:
  - url: "https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise"
    publisher: "ICTjournal"
    date: "2026-08-21"
    role: primary
  - url: "https://www.lenouvelliste.ch/valais/bas-valais/martigny-district/martigny-combe-commune/cyberattaque-a-la-commune-de-martigny-combe-300-courriels-contenant-des-donnees-sensibles-ont-ete-voles-1511002"
    publisher: "Le Nouvelliste"
    date: "2026-08-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "La commune de Martigny-Combe, en Valais, a détecté le 18 août un accès non autorisé à la messagerie professionnelle de son secrétariat communal."
    publisher: "ICTjournal"
  - quote: "l’incident pourrait avoir entraîné la divulgation à un tiers non autorisé de données personnelles contenues dans cette messagerie"
    publisher: "ICTjournal"
  - quote: "La messagerie du secrétariat communal de Martigny-Combe a été piratée. Des courriels ont été récupérés et un message frauduleux a été massivement envoyé à des contacts de la commune"
    publisher: "Le Nouvelliste"
verification: multi-source
sourcing_note: >
  Two reputable Swiss outlets carry this, which is why the verification value is multi-source, but they are
  two publishers of one assessment rather than two independent assessors: both rest on the municipality's own
  communiqué, so the credibility rating is 2 rather than 1. The split between them matters and is preserved
  per claim rather than merged. ICTjournal reproduces the communiqué's own hedge — that the incident could
  have led to disclosure — while Le Nouvelliste's headline and lede assert that emails were taken and put the
  figure at around 300; the eight-day interval before detection rests on that outlet's dating of the attack to
  10 August, carried in an image caption. Le Nouvelliste's article body is behind a paywall, so only its
  title, lede and caption were readable this run, and every claim attributed to it here comes from those. No
  source states how access to the mailbox was obtained, so the technique mapping covers only the abuse of the
  mailbox account, the retrieval of mail from it and the onward send — there is no access-vector mapping
  because no cited source describes one.
confidence: high
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

The municipality of Martigny-Combe, in Valais, detected unauthorised access to the professional mailbox of its communal secretariat on 18 August, and the compromise had already been used to send a fraudulent message to contacts of the administration ([ICTjournal, 2026-08-21](https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise)). What the municipality itself will commit to is narrower than the headlines: per its communiqué the incident *could* have led to the disclosure of personal data held in that mailbox to an unauthorised third party, and it names phishing and identity impersonation as the resulting risks, particularly for the people who received the fraudulent message ([ICTjournal, 2026-08-21](https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise)). Regional reporting is firmer than the administration is: Le Nouvelliste states the secretariat mailbox was breached, that emails were retrieved and that a fraudulent message was mass-sent to the municipality's contacts, puts the figure at around 300 emails containing sensitive data, and dates the attack itself to 10 August — eight days before the detection ([Le Nouvelliste, 2026-08-20](https://www.lenouvelliste.ch/valais/bas-valais/martigny-district/martigny-combe-commune/cyberattaque-a-la-commune-de-martigny-combe-300-courriels-contenant-des-donnees-sensibles-ont-ete-voles-1511002)). Both framings are reported here as their own sources state them, because the gap between "could have been disclosed" and "were stolen" is exactly the space a communal administration occupies in the first week of an investigation.

The response is on the record and follows the Swiss reporting path: the municipality blocked the affected access immediately, applied technical hardening measures, and is continuing the analysis with external specialists to establish the precise extent of the compromise; it notified the Federal Office for Cybersecurity (OFCS/BACS) and the cantonal Data Protection and Transparency Commissioner, and a criminal complaint with the Valais cantonal police is in progress ([ICTjournal, 2026-08-21](https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise)). No source names an initial-access mechanism, an actor, a product or a vulnerability. The same report places this a few months after the cyberattack that disrupted another Valais municipality, Vétroz ([ICTjournal, 2026-08-21](https://www.ictjournal.ch/news/2026-08-21/cyberattaque-en-valais-une-messagerie-de-la-commune-de-martigny-combe-compromise)) — the second communal administration in one canton inside a year, in a tier of Swiss government that typically has no dedicated security staff at all.

**Defender takeaway:** the operationally interesting fact is not the compromise but the detection path. On the dating available, the attacker held a live municipal mailbox for roughly eight days and produced no signal anyone acted on; what ended the intrusion was the attacker's own noisy step, a single send to the whole contact list. That inverts the usual assumption for small-administration mail estates: the mailbox itself is the asset, and the alert that arrives is the one the attacker chooses to generate. The telemetry that would have closed the gap earlier is available in any hosted mail tenant without a SOC — per-mailbox send-volume and recipient fan-out measured against that mailbox's own historical baseline, mailbox audit records for sign-ins from unfamiliar locations or clients, and the creation of inbox rules or forwarding rules, which is the standard persistence step for this intrusion class and is worth checking on any mailbox that has been in an attacker's hands. **Triage:** a communal secretariat mailbox legitimately mails large recipient sets — invoices, council notices, school circulars — so volume alone is not the discriminator; what separates this from ordinary business is a send whose recipient set is drawn from the whole address book rather than a mailing list, at a time of day out of pattern for that mailbox, and unaccompanied by the message-approval or template artefacts the administration's normal bulk sends carry. For anyone downstream, the second-order risk is the one the municipality itself named: recipients now hold a genuine message from a genuine government address, which is a far better phishing pretext than any spoofed sender.
