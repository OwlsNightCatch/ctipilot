---
schema: 1
kind: incident
title: "Qbusoft's Medyc practice-management software, used by Polish healthcare providers, is breached via SQL injection, and Zaufana Trzecia Strona attributes it to the actor behind August's MyDr leak"
headline: "A second Polish health-records vendor is breached by what Zaufana Trzecia Strona says is the MyDr actor"
summary: >
  Qbusoft Sp. z o.o., maker of the Medyc practice-management software used by
  Polish medical clinics, suffered a SQL-injection intrusion on 22-23 August
  2026 that exfiltrated an encrypted database archive; the company only
  discovered it in the night of 8-9 September, and the breach surfaced through
  a patient facility's own notice. Zaufana Trzecia Strona attributes both intrusions to the self-styled actor
  "fingerprint", a link DataBreaches.net says has not been disclosed, and reports that, as of 2026-09-25, Qbusoft had not looped in Poland's healthcare-sector CERT or CERT Polska.
discovered_at: "2026-09-27T04:34:00Z"
updated_at: null
event_date: "2026-08-22"
run_id: 2026-09-27T0404Z-intel
priority: routine
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
  Zaufana Trzecia Strona's two posts are the primaries, and TVP World independently confirms the
  breach itself, the Inowrocław facility's notice and the minister's statement that the cybercrime
  office is investigating. The finding that Qbusoft had not notified CSIRT CEZ or CERT Polska as of 2026-09-25, the
  same-actor link to August's MyDr breach and the attackers' photo counts rest on Zaufana Trzecia
  Strona alone.
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
updates:
  - at: "2026-09-30T06:56:01Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: a Polish healthcare-software breach outside Switzerland and the public sector, whose SQL-injection vector names no product or technique
      detail a defender here can act on, so it is awareness only. The body is shortened to suit that
      priority, the title, headline and summary present the link to the MyDr actor as Zaufana
      Trzecia Strona's attribution, and the sourcing note states provenance only. The attackers'
      five-million patient claim is set against Zaufana Trzecia Strona's own estimate of at least a
      million, with only the photo count unconfirmed, and the summary no longer describes the outlet
      as the one that broke the MyDr story, which none of the sources states.
    fields: [priority, sourcing_note, title, headline, summary, body]
migrated_from: null
---

Qbusoft, maker of the Medyc practice-management application used by Polish clinics, was breached through SQL injection on 22-23 August 2026 and an encrypted database archive was taken. The company learned of it only in the night of 8-9 September, and the breach surfaced through a patient notice from the Inowrocław addiction and psychiatric treatment centre. Name, surname and PESEL were stored encrypted, but the vendor told the facility the encryption was easy to break ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)).

Zaufana Trzecia Strona attributes the intrusion to "fingerprint", the pseudonym of the actor behind August's MyDr breach ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)), which exposed data on almost 19 million Poles ([TVP World, 2026-09-26](https://tvpworld.com/95581628/poland-hit-by-cyberattack-weeks-after-19-million-medical-records-breach)). DataBreaches.net notes that whether it is the same attacker has not been disclosed ([DataBreaches.net, 2026-09-26](https://databreaches.net/2026/09/26/poland-reports-a-second-medical-data-cyberattack-in-recent-weeks/)). The attackers claim data on five million patients, against ZTS's own estimate of at least a million, and 8 million photos, a count ZTS could not confirm. Poland's digital affairs minister said Qbusoft reported the intrusion to the Central Office for Combating Cybercrime but not to the healthcare-sector CSIRT CEZ or to CERT Polska ([Zaufana Trzecia Strona, 2026-09-25](https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/)).

**Defender takeaway:** a vendor's confirmed breach does not automatically reach the sector or national CERT, so vendor incident-response clauses should name the CERT a critical software vendor must notify on confirmation. Encrypted fields are not protected when the vendor itself calls the encryption easy to break ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)).

## Correction — 2026-09-30T06:56:01Z

The link between the Medyc and MyDr breaches is Zaufana Trzecia Strona's attribution ([Zaufana Trzecia Strona, 2026-09-24](https://zaufanatrzeciastrona.pl/post/sprawcy-wycieku-mydr-ponownie-atakuja-tym-razem-ofiara-aplikacja-medyc/)). DataBreaches.net notes that whether it is the same attacker has not been disclosed ([DataBreaches.net, 2026-09-26](https://databreaches.net/2026/09/26/poland-reports-a-second-medical-data-cyberattack-in-recent-weeks/)). The earlier title and headline stated the link as fact. The earlier headline also said the vendor never told the national CERT. The minister's statement relayed by Zaufana Trzecia Strona says that, as of 2026-09-25, the information had not been passed to CSIRT CEZ or CERT Polska ([Zaufana Trzecia Strona, 2026-09-25](https://zaufanatrzeciastrona.pl/post/sprawcy-ataku-na-system-medyc-twierdza-ze-ukradli-dane-5-milionow-pacjentow-i-8-milionow-zdjec/)).
