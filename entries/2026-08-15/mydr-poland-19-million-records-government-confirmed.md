---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — Poland's government puts the MyDr breach at nearly 19 million people and over 2 TB, and the regulator confirms the notification duty sits with the ~12,000 clinics, not the platform"
headline: "Deputy PM Gawkowski calls it one of Poland's largest incidents; the regulator tells the clinics that used MyDr they must notify patients themselves"
summary: >
  On the same day MyDr confirmed a deliberate criminal intrusion, Poland's Deputy Prime Minister and digital
  affairs minister Krzysztof Gawkowski put the stolen database at nearly 19 million people and over 2 TB, and
  the data-protection authority UODO stated that the obligation to notify affected individuals rests with the
  healthcare controllers that used MyDr's services. Around 12,000 medical facilities use the platform. The
  processor/controller gap the earlier entry identified is now regulator-documented.
discovered_at: "2026-08-15T05:02:00Z"
event_date: "2026-08-13"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
regions:
  - europe
sectors:
  - healthcare
  - public-sector
entities:
  - incident:mydr-poland-ehr-breach-2026
techniques: [T1078]
affected_products: []
cves: []
sources:
  - url: "https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/"
    publisher: Notes from Poland
    date: "2026-08-13"
    role: primary
  - url: "https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html"
    publisher: Gazeta Prawna
    date: "2026-08-13"
    role: primary
  - url: "https://zaufanatrzeciastrona.pl/post/najwiekszy-wyciek-danych-osobowych-w-historii-polski-i-co-mozemy-z-nim-zrobic/"
    publisher: Zaufana Trzecia Strona
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "“We are dealing with one of the largest incidents in Poland’s history,” said digital affairs minister Krzysztof Gawkowski on Wednesday."
    publisher: Notes from Poland
  - quote: "„Powiadomienia osób, dotkniętych wyciekiem danych, spoczywa na administratorach, którzy korzystali z usług spółki MyDr” - zwrócił uwagę Urząd."
    publisher: Gazeta Prawna
verification: multi-source
sourcing_note: >
  Scale figures are the Polish government's own, stated at a press briefing after a Joint Cybersecurity
  Operations Centre meeting; the notification-duty statement is the data-protection authority's own
  communication. The attackers' earlier figure of roughly 18.8 million and their claimed access path remain
  claims and are not restated as fact here.
confidence: high
update_of: 2026-08-13/mydr-poland-ehr-criminal-intrusion-confirmed-processor-gap
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

**UPDATE (originally covered 2026-08-13):** the earlier entry recorded MyDr's own confirmation of a deliberate external criminal act, its statement that it could not yet say what was taken, and the structural observation — made at the time by the reporting outlet rather than by any authority — that because MyDr is a processor and the controllers are thousands of individual healthcare facilities, affected people could not be notified centrally. Both halves have now been settled by the Polish state.

At a press briefing following a meeting of the Joint Cybersecurity Operations Centre, Deputy Prime Minister and digital affairs minister Krzysztof Gawkowski said the leak may cover nearly 19 million people and that the stolen database exceeds 2 TB ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html)), and characterised it as "one of the largest incidents in Poland's history" ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/)). That replaces MyDr's hedged position with a government-stated figure. Gawkowski also said there is no indication of an attack from Russia or another state and that cybercriminals are "very likely" responsible — a notable framing for a country whose public sector is regularly targeted by state-linked actors, and one that shapes what kind of follow-on activity defenders should expect. Around 12,000 medical facilities use MyDr's services, per the digital affairs ministry ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/)). MyDr said in a Wednesday update that at the time of writing there was no evidence the data had been published anywhere.

The regulator has now put the notification structure in writing. Poland's data protection authority UODO stated that the obligation to notify people affected by the leak rests with the controllers that used MyDr's services, and reminded controllers that under GDPR a breach must be reported to the supervisory authority without undue delay and where feasible no later than 72 hours after becoming aware of it, with a reasoned explanation attached to any later report ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html)). UODO's advice to individuals is to lock their PESEL national identity number and to treat incoming SMS and email with more care to avoid phishing aimed at extracting further data or access to banking. Gawkowski separately urged people to use state services to check exposure and to lock their PESEL through the mObywatel portal ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/)).

**Defender takeaway:** the delta is a planning fact for any organisation that is a *processor* in a health or public-service supply chain. A breach at the processor triggers a 72-hour clock at every controller downstream, and each of those controllers has to reconstruct which of its own patients or citizens sat in the processor's dataset — from the processor's disclosure, not from its own telemetry. A SOC supporting a processor should assume it will be asked, within days and by hundreds of separate controllers, for per-controller scoping it will not have prepared; a SOC supporting a controller should know now which of its processors hold what, because that inventory is the only thing that turns a supplier's incident into a notification it can actually make.
