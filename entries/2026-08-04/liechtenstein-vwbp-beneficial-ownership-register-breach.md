---
schema: 1
kind: incident
horizon: operational
title: "Liechtenstein's beneficial-ownership register breached: copies of ~31,000 legal entities' records taken, and four more e-government systems pulled offline as a precaution"
headline: "A targeted attack on Liechtenstein's beneficial-ownership register yielded a targeting dataset on the owners behind Swiss- and EU-administered structures"
summary: >
  The Government of Liechtenstein disclosed on 2026-08-02 that an unknown actor gained unauthorised digital access to the
  Verzeichnis wirtschaftlich berechtigter Personen — the national beneficial-ownership register at the Amt für Justiz —
  overnight into 2026-07-30 and copied records for roughly 31,000 legal entities. Forensics released 2026-08-03
  characterise it as a targeted attack on that register with no attacks found on other systems, but the government
  progressively took the eMWST VAT portal, the Lides reporting platform, the central account register and the Intax tax
  system offline as a precaution. No initial-access vector has been disclosed, no actor identified and no ransom demand
  reported; the breach is declared under GDPR Article 33.
discovered_at: "2026-08-04T04:48:00Z"
event_date: "2026-07-30"
run_id: 2026-08-04T0411Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [europe, dach, switzerland]
sectors: [public-sector, finance]
entities: [incident:liechtenstein-vwbp-register-breach-2026-07]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.presseportal.ch/de/pm/100000148/100941487"
    publisher: "Regierung des Fürstentums Liechtenstein"
    date: "2026-08-02"
    role: primary
  - url: "https://www.presseportal.ch/de/pm/100000148/100941500"
    publisher: "Regierung des Fürstentums Liechtenstein"
    date: "2026-08-03"
    role: primary
  - url: "https://therecord.media/hackers-steal-records-liechtenstein-companies-foundations"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-03"
    role: corroborating
  - url: "https://www.srf.ch/news/international/31-000-geklaute-datensaetze-taeterschaft-von-cyberangriff-in-liechtenstein-weiterhin-unklar"
    publisher: "SRF"
    date: "2026-08-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Dabei wurden Datenkopien von rund 31'000 Rechtsträgern widerrechtlich abgegriffen."
    publisher: "Regierung des Fürstentums Liechtenstein"
  - quote: "Beim Angriff auf das VwbP handelt es sich um eine Verletzung des Schutzes personenbezogener Daten gemäss Art. 33 Datenschutz-Grundverordnung (DSGVO)."
    publisher: "Regierung des Fürstentums Liechtenstein"
  - quote: "Weitere Angriffe auf andere Systeme konnten nicht festgestellt werden."
    publisher: "Regierung des Fürstentums Liechtenstein"
  - quote: "Am Montag, 3. August 2026, folgten zusätzlich das Zentrale Kontenregister sowie das zentrale Steuerfachsystem Intax. Es handelt sich um reine Vorsichtsmassnahmen."
    publisher: "Regierung des Fürstentums Liechtenstein"
verification: multi-source
sourcing_note: >
  The government is the primary disclosing party for its own incident; The Record and SRF corroborate the scope
  independently. The `techniques[]` mapping deliberately carries only the collection behaviour the sources describe —
  bulk copying of records out of the register. No cited source states how access was obtained, so no access-vector
  technique is mapped.
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

The Verzeichnis wirtschaftlich berechtigter Personen (VwbP, "register of beneficial owners") exists because Liechtenstein implemented the EU's 5th Anti-Money-Laundering Directive: the VwbPG has been in force since 2021, and the register records the natural persons behind Rechtsträger — companies, foundations and trust arrangements. On 2026-08-02 the government disclosed that the register had been attacked and that "Datenkopien von rund 31'000 Rechtsträgern" ("copies of data on around 31,000 legal entities") were unlawfully taken ([Regierung des Fürstentums Liechtenstein, 2026-08-02](https://www.presseportal.ch/de/pm/100000148/100941487)). The Record and SRF both carry the same figure ([The Record, 2026-08-03](https://therecord.media/hackers-steal-records-liechtenstein-companies-foundations); [SRF, 2026-08-03](https://www.srf.ch/news/international/31-000-geklaute-datensaetze-taeterschaft-von-cyberangriff-in-liechtenstein-weiterhin-unklar)).

The government's own timeline is worth reading as a benchmark, because detection was human and internal rather than telemetry-driven. Unauthorised digital access occurred overnight into 2026-07-30; irregularities were noticed at the Amt für Justiz during that day; the Amt für Informatik was brought in, secured the data and took the affected system off the network the same day; the government was informed on 31 July that the attack had potentially succeeded, and the first confirmed preliminary findings arrived on the afternoon of 1 August. A crisis unit convened that evening under Head of Government Brigitte Haas and Justice Minister Emanuel Schädler, was formally confirmed on 2 August, and a media conference was announced for 2026-08-04. The government states there is no indication that data in the system was altered or deleted, and the register is unavailable to external users through the LLV.li portal.

The forensic update on 2026-08-03 is where the operationally interesting tension sits. First findings characterise the event as a targeted attack on the VwbP at the Amt für Justiz, and "Weitere Angriffe auf andere Systeme konnten nicht festgestellt werden" ("no further attacks on other systems could be established") — yet the government kept widening the shutdown: the eMWST VAT portal and the Lides electronic reporting and data-exchange platform came off the network on 31 July, and on 3 August the central account register and the central tax system Intax followed, explicitly as precautionary measures with no indication of unlawful access ([Regierung des Fürstentums Liechtenstein, 2026-08-03](https://www.presseportal.ch/de/pm/100000148/100941500)). Law-enforcement authorities are now engaged alongside the Amt für Informatik and external partners. No initial-access vector has been published, no actor named, and no ransom demand or criminal-market offering reported.

**Defender takeaway:** the exposure that travels beyond Liechtenstein is the nature of the dataset. This is not a credential dump; it is an authoritative mapping of the people behind companies, foundations and trusts, and the constituency that administers those structures is largely Swiss and European — the fiduciaries, trustees, banks and advisers on the other side of the border. Anyone in that business should expect pretexted contact that cites genuine, verifiable register facts about a real client entity, which is precisely the input that makes business-email-compromise and CEO-fraud attempts survive the recipient's usual sanity check. The hunt that follows from that is in mail flow and case handling rather than on the endpoint: inbound requests referencing correct entity details, ownership structures or registration facts, arriving outside an established channel, and the mandate or payment-detail changes they lead to. The second lesson is architectural and shows in the government's own actions: taking four unrelated e-government services offline "as a precaution" is what happens when blast radius cannot be proven quickly from telemetry. Per-register segmentation and retained, exportable per-principal access logs on each data service are what make "was this one reached too?" a query rather than a shutdown decision.

**Triage:** bulk read-out of a register by an external identity is a volumetric anomaly against a stable baseline, not an indicator match — a single external session enumerating tens of thousands of entities looks nothing like the handful of lookups a legitimate professional user performs, and it is detectable with no knowledge of the attacker's tooling. The benign lookalike is a sanctioned bulk export or an integrated partner system doing a scheduled sync; those are attributable to a known principal, run on a known schedule, and appear in change records, whereas this pattern is a single principal exceeding its own historical retrieval volume by orders of magnitude within one session.
