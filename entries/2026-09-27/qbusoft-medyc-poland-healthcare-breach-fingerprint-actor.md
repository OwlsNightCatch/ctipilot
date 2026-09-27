---
schema: 1
kind: incident
title: "Qbusoft's Medyc practice-management software, used by Polish healthcare providers, is breached via SQL injection by the same actor behind August's over-18-million-patient MyDr leak"
headline: "A second Polish health-records vendor falls to the same actor, and it never told the national CERT"
summary: >
  Qbusoft Sp. z o.o., maker of the Medyc practice-management software used by
  Polish medical clinics, suffered a SQL-injection intrusion on 22-23 August
  2026 that exfiltrated an encrypted database archive; the company only
  discovered it in the night of 8-9 September and, as of late September, had
  still not made any public statement of its own, with the breach surfacing
  instead through a patient facility's own notice. Zaufana Trzecia Strona,
  the outlet that broke August's MyDr breach, identifies the same self-styled
  actor "fingerprint" behind both intrusions and reports Qbusoft never
  looped in Poland's healthcare-sector CERT or CERT Polska.
discovered_at: "2026-09-27T04:34:00Z"
updated_at: null
event_date: "2026-08-22"
run_id: 2026-09-27T0404Z-intel
priority: notable
immediate_action: null
tags: [data-breach, sqli, organized-crime]
regions: [europe]
sectors: [healthcare]
entities: ["actor:fingerprint", "incident:qbusoft-medyc-poland-breach-2026-09", "incident:mydr-poland-ehr-breach-2026"]
techniques: [T1190, T1213]
affected_products: []
cves: []
sources:
  - url: "https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/"
    publisher: "Zaufana Trzecia Strona"
    date: "2026-09-24"
    role: primary
  - url: "https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/"
    publisher: "Zaufana Trzecia Strona"
    date: "2026-09-25"
    role: primary
  - url: "https://tvpworld.com/95581628/poland-hit-by-cyberattack-weeks-after-19-million-medical-records-breach"
    publisher: "TVP World"
    date: "2026-09-26"
    role: corroborating
  - url: "https://databreaches.net/2026/09/26/poland-reports-a-second-medical-data-cyberattack-in-recent-weeks/"
    publisher: "DataBreaches.net"
    date: "2026-09-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "According to information we have, a new large leak of personal and medical data has occurred, this time from the systems of Qbusoft Sp. z o.o., the maker of the Medyc.pl practice application. The perpetrators of the leak are the same people who were behind the attack on the MyDr systems, from which the data of over 18 million Poles was stolen. (translated from Polish)"
    publisher: "Zaufana Trzecia Strona"
    source_url: "https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/"
    original: "Według posiadanych przez nas informacji doszło do nowego dużego wycieku danych osobowych i medycznych, tym razem z systemów firmy Qbusoft Sp. z o.o., producenta aplikacji gabinetowej Medyc.pl. Sprawcami wycieku są te same osoby, które stały za atakiem na systemy MyDr, skąd wykradziono dane ponad 18 milionów Polaków."
  - quote: "The Addiction and Psychiatric Treatment Center in Inowrocław reported having received information about a leak of its patients' data from the Medyc system (the same center had earlier reported a leak of its patients' data from the MyDr system, which is bad luck). (translated from Polish)"
    publisher: "Zaufana Trzecia Strona"
    source_url: "https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/"
    original: "Odwykowo-Psychiatryczny Ośrodek Leczniczy w Inowrocławiu poinformował o otrzymaniu informacji o wycieku danych swoich pacjentów z systemu Medyc (ten sam ośrodek informował wcześniej o wycieku danych swoich pacjentów z systemu MyDr, to się nazywa pech)."
  - quote: "As we read in the Inowrocław facility's own notice, the attack on Qbusoft took place on 22-23 August of this year. The perpetrators, using an SQL Injection vulnerability, stole an \"encrypted database archive.\" The company learned of the incident on the night of 8-9 September. (translated from Polish)"
    publisher: "Zaufana Trzecia Strona"
    source_url: "https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/"
    original: "Jak czytamy w komunikacie placówki z Inowrocławia, do ataku na firmę Qbusoft doszło w dniach 22-23 sierpnia tego roku. Sprawcy, wykorzystując podatność typu SQL Injection, wykradli \"zaszyfrowane archiwum bazy danych\". Firma o incydencie dowiedziała się w nocy z 8 na 9 września."
  - quote: "we ourselves assessed the scale of the incident at at least a million people; according to the perpetrators it is five million. The perpetrators also mention that they stole 8 million \"very private\" photos. (translated from Polish)"
    publisher: "Zaufana Trzecia Strona"
    source_url: "https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/"
    original: "My ocenialiśmy skalę incydentu na co najmniej milion osób, według sprawców jest to pięć milionów. Sprawcy wspominają także, że ukradli 8 milionów \"bardzo prywatnych\" zdjęć."
  - quote: "The incident at Qbusoft was also confirmed by Minister Gawkowski, who pointed out that although the victim of the attack informed the Central Office for Combating Cybercrime about it, it did not pass information to either the CSIRT CEZ team, established to handle incidents in the healthcare sector, or to the CERT Polska team, which coordinates the largest incidents and has the greatest experience in Poland in this regard (it handled, among others, the coordination of the incident at MyDr). (translated from Polish)"
    publisher: "Zaufana Trzecia Strona"
    source_url: "https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/"
    original: "Incydent w firmie Qbusoft potwierdził także minister Gawkowski, który wskazał, że choć ofiara ataku poinformowała o nim Centralne Biuro Zwalczania Cyberprzestępczości, to nie przekazała informacji ani do zespołu CSIRT CEZ, powołanego do obsługi incydentów w sektorze ochrony zdrowia, ani do zespołu CERT Polska, koordynującego największe incydenty i posiadającego w tym zakresie największe w Polsce doświadczenie (zajmował się m.in. koordynacją incydentu w firmie MyDr)."
  - quote: "Whether it’s the same attacker or whether any ransom demand has been involved has not been disclosed."
    publisher: "DataBreaches.net"
    source_url: "https://databreaches.net/2026/09/26/poland-reports-a-second-medical-data-cyberattack-in-recent-weeks/"
verification: multi-source
sourcing_note: >
  Zaufana Trzecia Strona (ZTS) is the same investigative outlet that broke
  and continued to cover August's MyDr breach; its two Medyc/Qbusoft posts are
  this entry's primaries. TVP World independently confirms only the base
  facts, the Qbusoft/Medyc breach itself, the Inowrocław facility's own
  notice, and a Gawkowski statement that the Central Office for Combating
  Cybercrime is investigating, without crediting ZTS, so those facts are
  corroborated by a second, independently-reporting outlet. The
  CERT-notification-gap finding (Qbusoft reported to the cybercrime office
  but never to CSIRT CEZ or CERT Polska) rests on ZTS's second post alone,
  which quotes a different, more specific Gawkowski statement TVP World does
  not carry, and is single-source accordingly. DataBreaches.net's relay adds
  no new fact and explicitly notes the same-actor question "has not been
  disclosed" from its own vantage, which this entry preserves as a caveat:
  the same-actor attribution rests on ZTS's own reporting, not on
  independent confirmation by a second assessor. The 5-million/8-million-photo
  figures are the attackers' own unverified claim, relayed by ZTS without
  independent confirmation, and are presented here as a claim, not a fact.
confidence: medium
references: ["2026-08-13/mydr-poland-ehr-criminal-intrusion-confirmed-processor-gap"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Qbusoft Sp. z o.o., the Polish company behind the Medyc practice-management application used by medical clinics across the country, was breached via an SQL-injection vulnerability on 22-23 August 2026; the attackers exfiltrated an "encrypted database archive," per the Inowrocław facility's own breach notice ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)). Qbusoft itself did not learn of the intrusion until the night of 8-9 September, roughly two and a half weeks later, and had made no public statement of its own as of this reporting, even in response to ZTS's direct press questions sent days earlier; the breach surfaced instead when the Addiction and Psychiatric Treatment Center in Inowrocław notified its own patients that their data had leaked from the Medyc system, the same facility that had earlier notified patients of the unrelated MyDr leak ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)). Stolen fields include name, surname, national PESEL identity number, residential address, phone number and email address; per the facility's own notice, the name, surname and PESEL fields were stored encrypted, but the vendor had told the facility the encryption was easy to break, so the attackers could still reach that data, and ZTS assesses there is a good chance medical discharge-summary data was taken as well ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)).

Zaufana Trzecia Strona, the outlet that first revealed August's MyDr breach of more than 18 million Polish patients' records, identifies the actor behind both intrusions as the same self-styled group or individual using the pseudonym "fingerprint": "The perpetrators of the leak are the same people who were behind the attack on the MyDr systems, from which the data of over 18 million Poles was stolen" (translated from Polish) ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)). A follow-up ZTS post relays the attackers' own claim of far greater scale than the outlet's initial estimate: "we ourselves assessed the scale of the incident at at least a million people; according to the perpetrators it is five million. The perpetrators also mention that they stole 8 million \"very private\" photos" (translated from Polish) ([Zaufana Trzecia Strona, 2026-09-25](https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/)); ZTS states plainly it could not confirm the claimed photo count reached the perpetrators, though it does not dispute that photos of some kind may have been taken, and DataBreaches.net separately notes that whether this is genuinely the same attacker "has not been disclosed" from its own reporting vantage ([DataBreaches.net, 2026-09-26](https://databreaches.net/2026/09/26/poland-reports-a-second-medical-data-cyberattack-in-recent-weeks/)); treat the same-actor link as ZTS's own attribution, not an independently confirmed fact. A second ZTS source states that, as with MyDr, Qbusoft's main company resources were stored in cloud services, specifically Microsoft Azure infrastructure, unlike MyDr's AWS-hosted environment ([Zaufana Trzecia Strona, 2026-09-25](https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/)).

Poland's Digital Affairs Minister Krzysztof Gawkowski confirmed the incident and disclosed a notification gap: although Qbusoft reported the intrusion to the Central Office for Combating Cybercrime, it never passed information to CSIRT CEZ, the CERT established specifically for the healthcare sector, or to CERT Polska, the national CERT that coordinated the MyDr incident and holds Poland's deepest incident-response experience ([Zaufana Trzecia Strona, 2026-09-25](https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/)). As of this reporting, the attackers had not published or offered the stolen data for sale, consistent with their pattern after the MyDr breach.

**Defender takeaway:** the incident-response gap is as significant as the breach itself, and directly transferable: a victim organization's own management chain does not automatically route a confirmed intrusion to the sector CERT or national CERT best placed to help, even when that help is free and the same coordinating body already has direct experience with the same actor. Any organization's supply-chain or vendor incident-response playbook should specify, in advance, which national or sectoral CERT a critical software vendor is expected to loop in on confirmation of a breach, and should not assume a vendor will do so voluntarily. Separately, "encrypted" is not a synonym for "protected": a database field description alone does not establish whether the encryption resists the effort an attacker who already has full database access will make against it.
