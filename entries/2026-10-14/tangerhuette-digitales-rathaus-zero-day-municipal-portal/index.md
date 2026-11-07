---
schema: 1
kind: incident
title: "Tangerhütte (Saxony-Anhalt): the vendor of the municipal citizen-portal software says attackers exploited a zero-day in it, classifies the intrusion as AI-driven, and four other communes took their portals offline"
headline: "German portal vendor reports an exploited zero-day and calls it AI-driven; police neither confirm nor deny that"
summary: >
  Innocon, the Tangermünde developer of the "digitales Rathaus" citizen portal, said in an MDR report of 2026-10-13 that attackers found and exploited a vulnerability it did not know of in its software, run for Tangerhütte on systems of the state municipal IT provider KID; the portal was taken offline in September and four more communes pulled theirs as a precaution. Innocon says the attackers reached only test accounts and took no real data, and classifies the intrusion as AI-driven because of command speed and on-host tool development, which is the vendor's reading: the state criminal police can neither confirm nor deny it. No CVE, product version or fix is named.
discovered_at: "2026-10-14T03:42:00Z"
updated_at: null
event_date: "2026-09-16"
run_id: 2026-10-14T0255Z-intel
priority: notable
immediate_action: null
tags: [zero-day, supply-chain]
regions: [dach]
sectors: [public-sector]
entities: ["incident:tangerhuette-digitales-rathaus-zero-day-2026-09", "product:innocon-digitales-rathaus"]
techniques: [T1190]
affected_products: ["Innocon digitales Rathaus"]
cves: []
sources:
  - url: "https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html"
    publisher: "MDR AKTUELL"
    date: "2026-10-13"
    role: primary
  - url: "https://www.mdr.de/nachrichten/sachsen-anhalt/stendal/stendal/digitales-rathaus-cyber-sicherheit-hacker-,tangerhuette-it-angriff-100.html"
    publisher: "MDR Sachsen-Anhalt"
    date: "2026-09-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We did not know about this vulnerability and it is quite tricky to find it. (translated from German)"
    original: "Wir kannten diese Schwachstelle nicht und es ist ziemlich tricky, sie herauszufinden."
    publisher: "MDR AKTUELL (Innocon managing director Hagen Woecht)"
    source_url: "https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html"
  - quote: "We classify this as an AI attack. (translated from German)"
    original: "Wir stufen das als KI-Angriff ein."
    publisher: "MDR AKTUELL (Innocon managing director Hagen Woecht)"
    source_url: "https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html"
verification: single-source
sourcing_note: "The account of the intrusion rests on the software vendor's statements to MDR; the municipality gave no technical detail in September, the municipal IT provider KID did not comment on the incident, and the state criminal police neither confirm nor deny the AI classification."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

MDR AKTUELL reports on 2026-10-13 that the vendor of Tangerhütte's "digitales Rathaus" citizen portal says attackers found and exploited a vulnerability in its software that the vendor did not know of and for which no security update existed ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)). The portal, an app-based service that went online in 2020, was taken offline in September, and MDR Sachsen-Anhalt reported on 2026-09-16 that the municipality said it had repelled an attack and gave no technical detail ([MDR Sachsen-Anhalt, 2026-09-16](https://www.mdr.de/nachrichten/sachsen-anhalt/stendal/stendal/digitales-rathaus-cyber-sicherheit-hacker-,tangerhuette-it-angriff-100.html)). The software runs on systems that the state municipal IT provider KID operates for Tangerhütte; an IT employee noticed irregularities in the morning after the attack began at night, the server was isolated and cut from the internet, and the vendor analysed the secured logs on an offline notebook ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)). Innocon told other affected communes, four of which also took their portals offline as a precaution although there was no sign of an attack on them, and says the attackers reached only test accounts and took no real data ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)). Citizens could use the services only on paper for weeks ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)).

The vendor classifies the intrusion as AI-driven for two reasons: commands were executed faster than copy-and-paste would allow, and the follow-on steps were not prepared in advance but developed on the city's server during the attack, whereas human attackers normally upload their own code and do not change it ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)). That is the vendor's reading of its own logs. The state criminal police are investigating data espionage and can neither confirm nor deny an AI attack, and two professors told MDR the reading is plausible without having seen the logs ([MDR AKTUELL, 2026-10-13](https://www.mdr.de/nachrichten/deutschland/politik/hacker-in-sachsen-anhalt-offenbar-erster,ki-angriff-100.html)). No CVE, product version, fixed release or entry vector is named.

**Exposure:** municipalities running Innocon's digitales Rathaus, which is used for Tangerhütte and at least four further communes that Innocon informed; whether any Swiss body runs it is not reported. The case matters to communal administrations as a supplier-built citizen portal hosted by a shared municipal IT provider, where the customer cannot patch an unknown flaw itself.

**Detection:** the vendor's two observations are the pattern to look for in a portal host's logs: commands issued faster than a person could type them, and follow-on scripts written and run on the host within the same session rather than uploaded once.

**Defender takeaway:** for a citizen portal built on a supplier's software, an exploited unknown flaw leaves isolation as the only lever, and this case shows what worked: isolate the server, copy the logs and analyse them offline, and have the supplier warn its other customers, four of which pulled their portals as a precaution.
