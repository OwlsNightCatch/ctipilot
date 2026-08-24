---
schema: 1
kind: incident
horizon: operational
title: "France's tax authority confirms an intruder reached its information system after an identity usurpation and extracted data — six weeks before the claim surfaced on a criminal forum"
headline: "The DGFiP says access was cut in late June during a routine control — it took a forum sale post on 12 August for the ministry to learn what had been extracted"
summary: >
  France's Ministère de l'Action et des Comptes publics confirmed on 2026-08-13 that a malicious actor had gained
  illegitimate access to the Direction générale des Finances publiques information system in late June 2026 following
  an identity usurpation, and that the access permitted the consultation and extraction of data on both private
  individuals and businesses. The access was already cut in late June as part of a control operation, but the ministry
  did not characterise the loss until the intruder advertised the data for sale on a criminal forum on 12 August —
  roughly six weeks later. The ministry gives no victim count; the forum claims run from a file of about 678,000 lines
  to a second, separate posting alleging close to two million property owners, and the second claimant says no VPN was
  involved at all — an identifier plus an MFA bypass was enough to stay undetected.
discovered_at: "2026-08-14T05:07:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - organized-crime
regions:
  - europe
sectors:
  - public-sector
entities:
  - incident:dgfip-france-tax-authority-intrusion-2026-06
techniques:
  - T1078
  - T1213
affected_products: []
cves: []
sources:
  - url: "https://actu17.fr/faits-divers/cyberattaque-visant-la-dgfip-nom-adresse-et-numero-fiscal-dusagers-recuperes-par-un-pirate.html"
    publisher: "Actu17"
    date: "2026-08-13"
    role: primary
  - url: "https://www.zataz.com/fisc-un-acces-illegitime-confirme-a-expose-des-donnees/"
    publisher: "ZATAZ"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Mercredi 12 août 2026, un acteur malveillant a revendiqué un accès illégitime au système d'information de la Direction générale des Finances publiques (DGFiP), intervenu fin juin 2026, après une usurpation d'identité."
    publisher: "Ministère de l'Action et des Comptes publics, quoted by Actu17"
  - quote: "Cette fois, aucun VPN ou dispositif de protection particulier n’était nécessaire : un identifiant et un contournement de la MFA ont suffi pour rester longtemps non détectés."
    publisher: "Forum claimant, quoted by ZATAZ"
verification: multi-source
sourcing_note: "The ministry's press statement is quoted by both outlets but was not reachable first-party this run; CERT-FR carried nothing on it at fetch time. Every figure and every technical detail of the access path comes from the criminal claimant or from the leak-tracking site Fuites Infos as relayed by Actu17, and is attributed as such — the ministry confirms only that access occurred, that it followed an identity usurpation, and that data was consulted and extracted."
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

France's Ministère de l'Action et des Comptes publics confirmed in a press statement on 2026-08-13 that ["un acteur malveillant a revendiqué un accès illégitime au système d'information de la Direction générale des Finances publiques (DGFiP), intervenu fin juin 2026, après une usurpation d'identité"](https://actu17.fr/faits-divers/cyberattaque-visant-la-dgfip-nom-adresse-et-numero-fiscal-dusagers-recuperes-par-un-pirate.html) — a malicious actor claimed illegitimate access to the tax authority's information system, obtained in late June 2026 after an identity usurpation. The ministry states that the access, which had already been cut in late June in the course of a control operation, nonetheless permitted the consultation and extraction of data concerning private individuals and businesses, and that deeper investigations continue to establish precisely which data and how many users are affected ([Actu17, 2026-08-13](https://actu17.fr/faits-divers/cyberattaque-visant-la-dgfip-nom-adresse-et-numero-fiscal-dusagers-recuperes-par-un-pirate.html)). France's national cybersecurity agency ANSSI and the ministries' own specialist services are taking part in the investigation, the incident is to be notified to the CNIL, and a criminal complaint is planned ([ZATAZ, 2026-08-13](https://www.zataz.com/fisc-un-acces-illegitime-confirme-a-expose-des-donnees/)).

**The interval is the finding.** The intrusion dates to late June and the connection was severed at the time, yet what had been taken only became known when the actor posted the data for sale on a criminal forum on 12 August — the ministry's own account has the confirmation following the claim, not preceding it. That is a detection-and-scoping gap of roughly six weeks on a national tax administration, and it is the part that transfers: cutting an anomalous session during routine control is not the same as establishing what that session read, and an authority that does not reconstruct the query history at the time of disconnection learns the answer from the buyer's advertisement.

**Two claims, two different access stories, neither confirmed by the ministry.** The first, relayed by the leak-tracking site Fuites Infos and reported by Actu17, describes a file of roughly 678,000 lines with a sample of about 1,100 lines offered as proof, and attributes the intrusion to the compromise of an internal VPN which then gave access to an application for searching taxpayers, with extraction interrupted by a disconnection — a sequence that lines up with the ministry's reference to access being cut during a control ([Actu17, 2026-08-13](https://actu17.fr/faits-divers/cyberattaque-visant-la-dgfip-nom-adresse-et-numero-fiscal-dusagers-recuperes-par-un-pirate.html)). A second, separate posting on the same forum concerns close to two million French property owners, and its author describes a materially different route: ["Cette fois, aucun VPN ou dispositif de protection particulier n’était nécessaire : un identifiant et un contournement de la MFA ont suffi pour rester longtemps non détectés"](https://www.zataz.com/fisc-un-acces-illegitime-confirme-a-expose-des-donnees/) — this time no VPN or particular protective device was needed; an identifier and an MFA bypass sufficed to remain undetected for a long time. That claimant also asserts they still hold access to a DGFiP account and offers it for sale, an assertion Bercy does not address, and which leaves investigators to determine whether the second claim stems from the same access or a separate incident ([ZATAZ, 2026-08-13](https://www.zataz.com/fisc-un-acces-illegitime-confirme-a-expose-des-donnees/)). The field list circulating for the first file — civil-status details, full postal address, telephone and email, tax reference number, number of tax shares, withholding rate, and the history of exchanges with tax officials, plus company registration numbers for businesses — is not confirmed by the ministry, and Actu17 records that no passwords or login credentials are understood to be involved. Fuites Infos judges the claimant's further assertion that tens of millions of taxpayers could be affected to be neither substantiated nor verified.

**Defender takeaway:** the confirmed mechanism is impersonation of a legitimate identity, not the exploitation of a flaw, and the confirmed consequence is that data on individuals and businesses was consulted and extracted. The specific route — an internal VPN leading to an application for searching taxpayers — is the leak-tracking site's account rather than the ministry's, so treat it as the reported hypothesis it is. It is nonetheless the shape worth planning against, because any public administration running a search-oriented citizen or subject-lookup application behind staff authentication faces the same problem, and the controls that matter there are volumetric rather than perimeter: a rate and cardinality baseline per operator account on the lookup application itself, alerting on a single session enumerating far more subjects than a caseworker plausibly handles, and retaining that query history long enough that a session cut for anomalous behaviour can afterwards be reconstructed into a list of exactly which records were returned. The second claimant's account of an identifier plus an MFA bypass, if it holds, points the same way — enrolment and re-enrolment of authentication factors is where an impersonation lands, and helpdesk-driven factor resets without out-of-band identity proofing are the recurring route.

**Triage:** a compromised staff identity used against a lookup application produces authentication and application-access telemetry that is individually unremarkable — a valid credential, a successful MFA outcome, legitimate queries against a system the account is entitled to use. The separators are the shape of the session rather than its authenticity: subject-lookup volume far outside the account's own historical baseline, queries that show no case-management context around them, and access originating from a network position or device the account has not used before. The downstream data exposure this produces is, for the affected population, indistinguishable from any other tax-themed phishing pretext — which is why Actu17 flags impersonation of the tax administration as the expected follow-on abuse.
