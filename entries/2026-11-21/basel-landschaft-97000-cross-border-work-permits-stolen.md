---
schema: 1
kind: incident
title: "Canton Basel-Landschaft: attackers took about 97,000 records from a database of work permits for cross-border commuters (permit G) in the cyberattack on the cantonal administration; the canton cannot say which records, assumes all, and names no entry point or actor"
headline: "Basel-Landschaft: attackers took about 97,000 cross-border work-permit records; no entry point or actor named"
summary: >
  On 2026-11-20 the canton of Basel-Landschaft said that forensic analysis by external experts confirmed the attackers reached a database of work permits for cross-border commuters (permit G) and took data from it: about 97,000 records from applications lodged through its online platform since 2016-11-28, with names, addresses, birth dates, civil status, occupation, the ZEMIS identification number and employers' contact details. The canton cannot say which records left and assumes all did; it names no entry point, tool or actor, took the platform off the network and filed a criminal complaint against unknown persons.
discovered_at: "2026-11-21T04:47:00Z"
updated_at: null
event_date: "2026-11-20"
run_id: 2026-11-21T0355Z-intel
priority: routine
immediate_action: null
tags: [data-breach]
regions: [switzerland]
sectors: [public-sector]
entities: ["incident:basel-landschaft-cantonal-administration-cyberattack-2026-11"]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/"
    publisher: "Canton Basel-Landschaft (FAQ-Data page)"
    date: "2026-11-20"
    role: primary
  - url: "https://www.baselland.ch/politik-und-behorden/regierungsrat/medienmitteilungen/cyberangriff-auf-die-it-infrastruktur-der-kantonalen-verwaltung-basel-landschaft"
    publisher: "Canton Basel-Landschaft (media release on the attack)"
    date: "2026-11-18"
    role: primary
  - url: "https://polizeiticker.ch/artikel/basel-landschaft-97000-datensaetze-bei-cyberangriff-gestohlen-295633"
    publisher: "Polizeiticker Schweiz (relays the canton's communiqué)"
    date: "2026-11-20"
    role: corroborating
  - url: "https://www.inside-it.ch/cyberangriff-auf-baselbieter-verwaltung-fuehrte-zu-datenabfluss-20261120"
    publisher: "Inside IT"
    date: "2026-11-20"
    role: corroborating
  - url: "https://www.watson.ch/schweiz/digital/951471601-20-kantonale-applikationen-von-cyberangriff-im-baselbiet-betroffen"
    publisher: "watson.ch (Keystone-SDA)"
    date: "2026-11-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The forensic investigations carried out in the meantime have confirmed that the perpetrators were able to gain access to a database related to work permits for cross-border commuters and to extract data from it. (translated from German)"
    original: "hat sich bestätigt, dass sich die Täterschaft Zugriff auf eine Datenbank im Zusammenhang mit Arbeitsbewilligungen für Grenzgängerinnen und Grenzgänger verschaffen und daraus Daten abziehen konnte"
    publisher: "Canton Basel-Landschaft (FAQ-Data page)"
    source_url: "https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/"
  - quote: "According to the current state of knowledge, around 97,000 records are affected. (translated from German)"
    original: "Nach aktuellem Kenntnisstand sind rund 97'000 Datensätze betroffen."
    publisher: "Canton Basel-Landschaft (FAQ-Data page)"
    source_url: "https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/"
verification: single-source-victim
sourcing_note: >
  The canton's own FAQ page is the source and Polizeiticker relays the communiqué verbatim; Inside IT reports the same figures. The canton's first media release of 2026-11-18 carries the start of the attacks and the isolated servers; the number of applications and servers comes from watson.ch (Keystone-SDA), which relays the canton's update of that evening, and the earlier scope of the attack from Inside IT. The canton names no vector, tool or actor.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-11-22T04:35:05Z"
    run_id: 2026-11-22T0355Z-intel
    type: improvement
    summary: >
      The canton's media release of 2026-11-18 puts the start of the attacks at Sunday 2026-11-15 and
      reports isolated servers; its evening update counts about twenty applications on six servers being
      reinstalled and says rescue and security IT was never affected, and an Alertswiss warning that the
      emergency numbers might be restricted was withdrawn within hours, the numbers having stayed
      reachable.
    fields: [sources, sourcing_note, body, summary]
migrated_from: null
---

A confirmed data theft from a Swiss cantonal administration: the canton of Basel-Landschaft said on 2026-11-20 that forensic analysis showed the attackers reached a database of work permits for cross-border commuters (permit G) and took about 97,000 records for applications lodged through its online platform since 2016-11-28 ([Canton Basel-Landschaft, 2026-11-20](https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/)). It cannot establish which records were taken and assumes all, took the platform off the network, filed a criminal complaint against unknown persons and names no entry point, tool or actor ([Canton Basel-Landschaft, 2026-11-20](https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/); [Polizeiticker, 2026-11-20](https://polizeiticker.ch/artikel/basel-landschaft-97000-datensaetze-bei-cyberangriff-gestohlen-295633)), after other cantonal applications had been switched off earlier in the week ([Inside IT, 2026-11-20](https://www.inside-it.ch/cyberangriff-auf-baselbieter-verwaltung-fuehrte-zu-datenabfluss-20261120)).

**Exposure:** persons for whom a permit-G application was lodged, renewed or changed through the cantonal platform since 2016-11-28, and the contact persons of their employers in the canton; the database kept completed procedures too, so people whose permits ended are affected as well ([Canton Basel-Landschaft, 2026-11-20](https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/)). The canton cannot exclude that uploaded documents such as contracts or ID copies were taken but has no indication of it ([Canton Basel-Landschaft, 2026-11-20](https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/)).

**Defender takeaway:** an online application platform that keeps every historic procedure puts the whole archive in play when it is reached, so check how much completed data your own citizen-facing and supplier-run platforms retain; employers of cross-border commuters in the canton should expect phishing and social engineering that quotes correct personal details, because the canton warns that such messages can be built from the stolen data ([Canton Basel-Landschaft, 2026-11-20](https://www.baselland.ch/politik-und-behorden/direktionen/sicherheitsdirektion/amt_fuer_migration/bewilligungen/faq-data/)).

## Improvement — 2026-11-22T04:35:05Z

The canton's media release of Wednesday 2026-11-18 says diverse attacks on the cantonal IT had run since Sunday 2026-11-15, that individual servers had to be isolated from the internet and that further measures would be announced through the AlertSwiss app (translated from German) ([Canton Basel-Landschaft, 2026-11-18](https://www.baselland.ch/politik-und-behorden/regierungsrat/medienmitteilungen/cyberangriff-auf-die-it-infrastruktur-der-kantonalen-verwaltung-basel-landschaft)). Its update of that evening, relayed by Keystone-SDA, counts about twenty applications on six servers being reinstalled and says the IT of the rescue and security organisations was never affected; the Alertswiss warning of the night that the emergency numbers 112, 117 and 118 might be restricted was withdrawn a few hours later, and a government spokesperson said the numbers had stayed reachable and the warning was issued as a precaution ([watson.ch, 2026-11-18](https://www.watson.ch/schweiz/digital/951471601-20-kantonale-applikationen-von-cyberangriff-im-baselbiet-betroffen)).
