---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Berlin's state network was compromised on 14 August and both isolated Senate departments came back online on 23 August — nine days in which housing benefit stopped for more than 50,000 households and no named authority stated how the attackers got in"
headline: "Two ministries cut off the shared network, and the citizen services that stopped were in the districts"
summary: >
  Berlin's Senate Chancellery confirmed the Landesnetz, the shared network of the Berlin state
  administration, was compromised at least as early as 7 August 2026 — a week earlier than the 14
  August isolation date first reported — and that the Senate Department for Urban Development,
  Building and Housing and the Senate Department for Mobility, Transport, Climate Protection and
  Environment had been isolated from it since that Friday. The two departments stayed reachable only
  by telephone; the services that stopped were in the district offices that depend on their
  applications, including housing-benefit disbursement to more than 50,000 entitled households. On
  2026-08-23 both departments were reported back on the network, though staff reportedly still resort
  to private internet connections for some work; forensic work continues. The Senate's own
  data-exposure assessment has since widened from "harmless open geodata" to stating it cannot rule
  out personal or other non-public data. An unconfirmed press claim (RBB, 27 August, not confirmed
  internally) reports extortionists sent Berlin's Senate a ransom demand. Across every one of these
  developments, neither the Senate Chancellery, the Landeskriminalamt, the Berlin public prosecutor
  nor the BSI has stated an initial-access vector, an exploited product or a CVE.
discovered_at: "2026-08-23T23:53:00Z"
updated_at: "2026-08-28T05:10:00Z"
event_date: "2026-08-07"
run_id: 2026-08-23T2311Z-weekly
priority: high
immediate_action: null
tags: [data-breach]
regions: [europe, dach]
sectors: [public-sector, transport]
entities:
  - incident:berlin-landesnetz-compromise-2026-08
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.berlin.de/rbmskzl/aktuelles/pressemitteilungen/2026/pressemitteilung.1703898.php"
    publisher: "Presse- und Informationsamt des Landes Berlin (Senatskanzlei)"
    date: "2026-08-17"
    role: primary
  - url: "https://www.berlin.de/aktuelles/10581479-958090-hackerangriff-auf-landesnetz-arbeit-mit-.html"
    publisher: "Berlin.de (dpa/BerlinOnline)"
    date: "2026-08-19"
    role: primary
  - url: "https://www.berlin.de/en/news/10587704-5559700-after-hacker-attack-senate-departments-b.en.html"
    publisher: "Berlin.de (dpa)"
    date: "2026-08-23"
    role: primary
  - url: "https://www.tagesspiegel.de/berlin/wohngeld-kann-ausgezahlt-werden-berliner-senatsverwaltungen-sind-nach-hackerangriff-wieder-online-15973885.html"
    publisher: "Der Tagesspiegel"
    date: "2026-08-23"
    role: corroborating
  - url: "https://www.tagesspiegel.de/berlin/sie-waren-tagelang-unbemerkt-im-it-netz-unterwegs-hacker-fordern-laut-medienbericht-losegeld-vom-berliner-senat-15984600.html"
    publisher: "Der Tagesspiegel"
    date: "2026-08-27"
    role: primary
  - url: "https://www.tagesspiegel.de/berlin/keine-belastbaren-erkenntnisse-berliner-senat-tappt-nach-hackerangriff-im-dunklen-15976892.html"
    publisher: "Der Tagesspiegel"
    date: "2026-08-24"
    role: primary
closed_sources: []
evidence:
  - quote: "Im Zuge forensischer Untersuchungen hat sich eine Inkriminierung des Landesnetzes Berlin ergeben."
    publisher: "Presse- und Informationsamt des Landes Berlin (Senatskanzlei)"
  - quote: "Aus ermittlungstaktischen Gründen können derzeit keine weiteren konkreten Informationen zu Ausmaß und Hintergründen gegeben werden."
    publisher: "Presse- und Informationsamt des Landes Berlin (Senatskanzlei)"
  - quote: "All Senate departments are once again connected to Berlin’s state network and are, in principle, operational,"
    publisher: "Berlin.de (dpa)"
  - quote: "hat die Senatsverkehrsverwaltung erstmals am 7. August einen Datenabfluss gemeldet. Warum die Behörde genau wie die ebenfalls betroffene Senatsverwaltung für Stadtentwicklung erst sieben Tage später – am 14. August – vom Netz getrennt wurde, ist unklar."
    publisher: "Der Tagesspiegel, citing the Senatskanzlei's response to an inquiry"
  - quote: "Es kann nicht ausgeschlossen werden, dass im Geschäftsbereich der Senatsverwaltung für Mobilität, Verkehr, Klimaschutz und Umwelt auch personenbezogene oder sonstige nicht-öffentliche Daten betroffen sind"
    publisher: "Senatskanzlei Berlin press statement, quoted by Der Tagesspiegel"
  - quote: "Wir haben dazu keine belastbaren Erkenntnisse"
    publisher: "Florian Hauer (CDU), Staatssekretär für Digitalisierung, quoted by Der Tagesspiegel"
  - quote: "Nach dem erfolgreichen Hackerangriff auf die Berliner Verwaltung fordern Erpresser laut RBB-Abendschau nun Lösegeld. […] Dem Tagesspiegel gegenüber wurde die Darstellung am Donnerstagabend nicht bestätigt."
    publisher: "Der Tagesspiegel, citing RBB Abendschau; unconfirmed by the Senate"
verification: multi-source
sourcing_note: >
  The compromise, the isolation and the participating authorities come from the Senate Chancellery's
  own press release of 17 August. The 19 and 23 August items are Berlin.de's own news pages, authored
  by dpa and dpa/BerlinOnline respectively, carrying quotes from the Governing Mayor, the Interior
  Senator and the Senate Chancellery; they are the official portal's record of the press conference
  and of the restoration, not further Chancellery releases, and are cited as such. The household
  figure is Tagesspiegel's. This entry deliberately carries no initial-access vector: an unattributed
  press claim of a malicious email attachment circulated early and has not been repeated by the
  Senate Chancellery, the Landeskriminalamt, the public prosecutor or the BSI, so it is recorded here
  as an unconfirmed claim and used for nothing. `techniques` is empty for the same reason — no cited
  source describes any attacker behaviour to map, and inventing an access vector to fill the field
  would be a fabrication.
confidence: medium
update_of: null
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
  - at: "2026-08-28T05:10:00Z"
    run_id: 2026-08-28T0409Z-intel
    type: update
    summary: >
      The Senate Chancellery confirmed to Der Tagesspiegel that the intrusion began at least as
      early as 7 August, a week before the 14 August isolation this entry originally recorded as
      the start; CDO Florian Hauer told parliament on 24 August he still could not state how the
      attackers gained access. The Senate's data-exposure assessment has widened from "harmless
      open geodata" to stating it cannot rule out personal or non-public data. An unconfirmed
      press claim (27 August, not confirmed internally) reports a ransom demand. No authority has
      yet named a vector, product or CVE.
    fields:
      - event_date
      - priority
      - summary
      - evidence
      - sources
      - body
migrated_from: null
---

This is the week's clearest example of an incident that a technical intelligence pipeline cannot publish operationally and a reader nonetheless needs to know about. This pipeline surfaced Berlin's Landesnetz compromise on 20 August, re-worked it with a scoped deep read on 23 August, and could not publish either time — because an entry describing attacker activity has to describe attacker activity, and after nine days there is none on the public record. What there is instead is a complete account of the *consequences* of isolating two ministries from a shared state network, and that is the part with a transferable lesson for any administration built the same way.

The Senate Chancellery's own release of 17 August states the finding in one sentence — "Im Zuge forensischer Untersuchungen hat sich eine Inkriminierung des Landesnetzes Berlin ergeben," forensic investigations having established a contamination of the Berlin state network — and records that the Landeskriminalamt, the Berlin public prosecutor and the Bundesamt für Sicherheit in der Informationstechnik were all involved, with an ICT emergency crisis team under the state's information-security commissioner stood up that day. The two affected administrations, the Senate Department for Urban Development, Building and Housing and the Senate Department for Mobility, Transport, Climate Protection and Environment, had been separated from the Landesnetz since the preceding Friday, 14 August, as a precaution. The release closes the door on the question every defender asks next: "Aus ermittlungstaktischen Gründen können derzeit keine weiteren konkreten Informationen zu Ausmaß und Hintergründen gegeben werden" — for investigative reasons no further concrete information on scope or background can currently be given ([Senatskanzlei, 2026-08-17](https://www.berlin.de/rbmskzl/aktuelles/pressemitteilungen/2026/pressemitteilung.1703898.php)).

**What the isolation actually cost is the strategic content.** At a press conference on 19 August the Governing Mayor said Berlin had been the victim of a hacker attack, that the incident was serious, and that on current knowledge no sensitive data had flowed out; the Interior Senator said the state election of 20 September was not endangered by the attack. The two administrations were reachable only by telephone, and services around housing benefit — both application and disbursement — were unavailable ([Berlin.de (dpa/BerlinOnline), 2026-08-19](https://www.berlin.de/aktuelles/10581479-958090-hackerangriff-auf-landesnetz-arbeit-mit-.html)). Note where that failure lands: not in the two ministries that were isolated, but in the district offices whose citizen-facing processes run on applications those ministries host. Tagesspiegel puts the population figure on it — disbursement of housing benefit to more than 50,000 entitled households was not possible ([Der Tagesspiegel, 2026-08-23](https://www.tagesspiegel.de/berlin/wohngeld-kann-ausgezahlt-werden-berliner-senatsverwaltungen-sind-nach-hackerangriff-wieder-online-15973885.html)). Berlin.de's English news item of 23 August adds that the disruption also reached benefits under the education and participation package for children and adolescents ([Berlin.de (dpa), 2026-08-23](https://www.berlin.de/en/news/10587704-5559700-after-hacker-attack-senate-departments-b.en.html)).

Nine days later the Governing Mayor announced that "All Senate departments are once again connected to Berlin’s state network and are, in principle, operational," with the Senate Chancellery noting that the specialised procedures used in the districts are in principle available again and that occasional disruptions and delays may persist at the outset; both administrations have implemented immediate measures including continuously increased monitoring of their IT systems, and the forensic work continues in the coming weeks ([Berlin.de (dpa), 2026-08-23](https://www.berlin.de/en/news/10587704-5559700-after-hacker-attack-senate-departments-b.en.html)).

**Defender takeaway:** for a Swiss federal, cantonal or communal administration the transferable question is not how Berlin was breached — nobody outside the investigation knows — but what the same containment decision would cost here. The Berlin case makes two properties of a shared administrative network legible that are usually invisible until they are exercised. First, the blast radius of *containment* is not the blast radius of the *intrusion*: isolating two ministries was the correct and fast response, and it stopped a citizen payment for more than 50,000 households because the dependency ran outward from the isolated ministries into district offices that were never compromised. The mapping worth having in a drawer is therefore not an asset inventory but a service-dependency inventory — which citizen-facing processes stop if any given administrative unit is cut from the shared network, and which of them have a manual or offline fallback. Second, nine days is what a competent, well-resourced, three-authority response took to reconnect, with forensics still running afterwards; a continuity plan that assumes hours is planning for a different incident. **Triage:** none is offered, and that is the point — with no vector, product, CVE or attacker behaviour on the public record from any named authority, there is nothing here to hunt for, and this entry maps no ATT&CK technique rather than invent one. Where an authority does eventually name a surface, that is the moment this becomes an operational finding rather than a continuity one.

## Update — 2026-08-28T05:10:00Z

Two named-authority facts have changed since the original entry, and the vector question it was built around has not.

**The intrusion is now dated a week earlier than first understood.** The Senate Chancellery confirmed to Der Tagesspiegel that the Senate Department for Mobility, Transport, Climate Protection and Environment "hat die Senatsverkehrsverwaltung erstmals am 7. August einen Datenabfluss gemeldet" — first reported a data leak on 7 August, a full week before the 14 August isolation this entry originally treated as the incident's start; the Chancellery itself states it is unclear why the department was disconnected only seven days after that report ([Der Tagesspiegel, citing the Senatskanzlei, 2026-08-27](https://www.tagesspiegel.de/berlin/sie-waren-tagelang-unbemerkt-im-it-netz-unterwegs-hacker-fordern-laut-medienbericht-losegeld-vom-berliner-senat-15984600.html)). `event_date` above now records 7 August rather than 14 August accordingly.

**The data-exposure assessment has widened.** CDO/Staatssekretär Florian Hauer told the Innenausschuss on 2026-08-24 that officials still "keine belastbaren Erkenntnisse" — have no solid findings — on how the attackers gained access, and could not make a statement on the access mechanism at all ([Florian Hauer, quoted by Der Tagesspiegel, 2026-08-24](https://www.tagesspiegel.de/berlin/keine-belastbaren-erkenntnisse-berliner-senat-tappt-nach-hackerangriff-im-dunklen-15976892.html)). The Senatskanzlei's own subsequent statement moves the exposure assessment for the Mobility department from Hauer's earlier "harmless open geodata" characterisation to: "Es kann nicht ausgeschlossen werden, dass im Geschäftsbereich der Senatsverwaltung für Mobilität, Verkehr, Klimaschutz und Umwelt auch personenbezogene oder sonstige nicht-öffentliche Daten betroffen sind" — personal or other non-public data in that department's business area cannot be ruled out ([Senatskanzlei Berlin, quoted by Der Tagesspiegel, 2026-08-27](https://www.tagesspiegel.de/berlin/sie-waren-tagelang-unbemerkt-im-it-netz-unterwegs-hacker-fordern-laut-medienbericht-losegeld-vom-berliner-senat-15984600.html)).

**An unconfirmed ransom-demand claim surfaced on 27 August.** Der Tagesspiegel reports, citing RBB Abendschau: "Nach dem erfolgreichen Hackerangriff auf die Berliner Verwaltung fordern Erpresser laut RBB-Abendschau nun Lösegeld. […] Dem Tagesspiegel gegenüber wurde die Darstellung am Donnerstagabend nicht bestätigt" — extortionists are reported demanding a ransom, a characterisation the Senate did not confirm when asked ([Der Tagesspiegel, citing RBB Abendschau, 2026-08-27](https://www.tagesspiegel.de/berlin/sie-waren-tagelang-unbemerkt-im-it-netz-unterwegs-hacker-fordern-laut-medienbericht-losegeld-vom-berliner-senat-15984600.html)). This is carried here as an unattributed, unconfirmed press claim, on exactly the same footing as the earlier unattributed email-attachment claim this entry has always declined to use — neither is treated as fact, and `techniques` stays empty on the same basis as before: no named authority states an attacker behaviour to map.

**Priority moves to `high`** on the strength of the widened, authority-confirmed data-exposure assessment and the extended intrusion timeline, not on the unconfirmed ransom claim. **Defender takeaway, updated:** a "no sensitive data" assessment given nine days into an incident is a snapshot, not a conclusion — Berlin's own revision, three weeks in, moved from ruling out personal data to being unable to rule it out. Any continuity plan built on an early damage assessment should treat that assessment as provisional until an authority states it has completed its forensic review, not merely reconnected the network. **Triage:** unchanged — still nothing to hunt, because still no authority has named a surface, a product or a CVE.
