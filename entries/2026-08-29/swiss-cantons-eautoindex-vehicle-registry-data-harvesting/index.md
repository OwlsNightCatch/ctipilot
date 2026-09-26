---
schema: 1
kind: incident
title: "Six Swiss cantons disclose bulk-harvesting of vehicle-owner data after an unknown actor bypassed per-person rate limits on public lookup portals, with extortion attempts against the platform operator and canton Vaud"
headline: "An attacker defeated Switzerland's cantonal vehicle-registry rate limits at scale, and two operators were then extorted"
summary: >
  Five Swiss cantons (Vaud, Aargau, Lucerne, Schaffhausen, Zug) and canton Valais separately disclosed on 2026-08-28
  that an unknown party bypassed the built-in per-person daily query limit on their public vehicle-owner lookup
  portals to harvest plate/name/address data at scale in mid-August; Valais's separate "ecari" platform also leaked
  approximate owner birthdates through additional, non-standard extractions. Both the eAutoIndex operator (Viacar AG)
  and canton Vaud report subsequent extortion attempts, which they did not act on. No core government IT system was
  compromised — only the public-facing lookup interfaces were abused.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-28"
run_id: 2026-08-29T0409Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [switzerland, dach]
sectors: [public-sector]
entities:
  - incident:swiss-cantons-eautoindex-databulk-harvest-2026-08
techniques: [T1119]
affected_products: ["eAutoIndex (Viacar AG)", "ecari"]
cves: []
sources:
  - url: "https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337"
    publisher: "cash.ch (AWP/Keystone-SDA wire, relaying the joint cantonal statement)"
    date: "2026-08-28"
    role: primary
  - url: "https://www.derbund.ch/eautoindex-fuenf-kantone-vermuten-datenmissbrauch-653056770416"
    publisher: "Der Bund (Tamedia)"
    date: "2026-08-28"
    role: corroborating
  - url: "https://www.blick.ch/fr/suisse/romande/tentatives-de-chantage-les-donnees-personnelles-dautomobilistes-vaudois-et-valaisans-ont-fuite-id22217676.html"
    publisher: "Blick (Romandie), relaying the État de Vaud / canton Valais statements"
    date: "2026-08-28"
    role: corroborating
  - url: "https://www.watson.ch/fr/!908053274"
    publisher: "watson.ch/fr (ATS wire)"
    date: "2026-08-28"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ordinarily, the number of queries on 'eAutoIndex' per person and per day is limited to five."
    original: "Für gewöhnlich ist die Anzahl Anfragen auf «eAutoIndex» pro Person und Tag auf fünf beschränkt."
    publisher: "cash.ch (AWP/Keystone-SDA wire, relaying the joint cantonal statement)"
  - quote: "According to current findings, the retrieval of the data occurred via a technical interface that exclusively permitted access to publicly viewable data. It can be ruled out that blocked data was exposed, according to Probst. It is not an actual data leak but rather the abusive use of a public information-lookup facility."
    original: "Der Abruf der Daten erfolgte gemäss bisherigen Erkenntnissen über eine technische Schnittstelle, die ausschliesslich den Zugang zu öffentlich einsehbaren Daten erlaubte. Dass gesperrte Daten abflossen, könne ausgeschlossen werden, so Probst. Es handle sich nicht um ein eigentliches Datenleck, sondern um die missbräuchliche Nutzung einer öffentlichen Auskunftsmöglichkeit."
    publisher: "cash.ch (AWP/Keystone-SDA wire, relaying the joint cantonal statement)"
  - quote: "The public-data leak also affected Valais: the 'ecari' search module, supplied by a partner external to the road-traffic and navigation service, was likewise targeted. Through additional extractions, the hacker was also able to access approximate date-of-birth data that is not normally accessible via an ordinary query."
    original: "La fuite de données publiques a également touché le Valais, le module de recherche «ecari», fourni par un partenaire externe au Service de la circulation routière et de la navigation ayant aussi été pris pour cible. Grâce à des extractions supplémentaires, le hacker a également pu accéder à des données approximatives liées à la date de naissance, qui ne sont généralement pas accessibles lors d'une requête ordinaire."
    publisher: "Blick (Romandie), relaying the État de Vaud / canton Valais statements"
verification: multi-source
sourcing_note: >
  cash.ch (AWP wire) and watson.ch/fr (ATS wire) carry near-identical phrasing traceable to the same underlying
  Keystone-ATS wire dispatch of the joint cantonal press release, rather than independent reporting on it; Der Bund
  appears to draw on the same dispatch. Only Blick adds visibly original material — an interview-sourced detail from
  canton Valais's own separate statement on the "ecari" incident. Credibility reflects two independent government
  disclosures (the five-canton joint statement and Valais's separate one) relayed largely through a single wire
  service, rather than fully independent multi-outlet verification of the same facts.
confidence: medium
references: []
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

On 2026-08-28, five Swiss cantons — Vaud, Aargau, Lucerne, Schaffhausen and Zug — issued a joint statement, and
canton Valais a separate one, disclosing that an unknown party had automatically harvested vehicle-owner data at
scale from their public online lookup services in mid-August ([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).
For the five-canton group the vector was eAutoIndex, a shared lookup platform operated by Viacar AG (Aarau) for
multiple cantonal road-traffic offices; the platform normally
receives more than 10,000 legitimate owner queries a day across the five cantons
([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).
The joint statement records that the actor circumvented eAutoIndex's own anti-abuse control — ordinarily capped at
five queries per person per day — to compile registration-plate numbers together with the associated owner's name
and address at volume ([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).
Cantonal officials characterise this as abuse of a legitimate public-disclosure mechanism rather than a conventional
data breach: no authentication was bypassed, the retrieval interface exposed only data already publicly disclosable
under Swiss federal road-traffic law, and no data that owners had opted to block from public disclosure was exposed
([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).

Canton Valais reported a separate incident the same day affecting "ecari", a different vehicle-lookup module
supplied by an external partner to its own cantonal road-traffic and navigation service. There, the actor went
beyond the intended query logic of the lookup interface through additional extractions to also obtain approximate
owner birthdates — a materially more sensitive field than the plate/name/address set exposed via eAutoIndex, and one
not normally reachable through an ordinary query
([Blick, 2026-08-28](https://www.blick.ch/fr/suisse/romande/tentatives-de-chantage-les-donnees-personnelles-dautomobilistes-vaudois-et-valaisans-ont-fuite-id22217676.html)).
Both the eAutoIndex operator (Viacar AG) and the canton of Vaud state they were subject to extortion attempts
following the harvesting, which they did not act on
([Blick, 2026-08-28](https://www.blick.ch/fr/suisse/romande/tentatives-de-chantage-les-donnees-personnelles-dautomobilistes-vaudois-et-valaisans-ont-fuite-id22217676.html)).
The five eAutoIndex cantons have filed or plan to file criminal complaints, and Viacar AG has introduced additional
technical access restrictions on eAutoIndex and is evaluating further controls
([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).
Valais separately states it has filed its own criminal complaint and has hardened access security on the affected
"ecari" system
([Blick, 2026-08-28](https://www.blick.ch/fr/suisse/romande/tentatives-de-chantage-les-donnees-personnelles-dautomobilistes-vaudois-et-valaisans-ont-fuite-id22217676.html)).
Neither the identity nor the number of actors involved is known, and no exploitation of the underlying road-traffic
office IT systems — as opposed to the public lookup interfaces — is reported by any cantonal authority
([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337);
[Blick, 2026-08-28](https://www.blick.ch/fr/suisse/romande/tentatives-de-chantage-les-donnees-personnelles-dautomobilistes-vaudois-et-valaisans-ont-fuite-id22217676.html)).

No source names the specific bypass technique (IP rotation, missing server-side session or device fingerprinting,
distributed request sourcing, or another anti-abuse gap) — an open question worth flagging for any defender who
operates a similar public per-identity rate-limited lookup service. Cantonal officials warn of a plausible follow-on
fraud vector: attackers or downstream buyers of the harvested plate/name/address/approximate-birthdate combination
could send deceptively authentic-looking demands for fake fines, vehicle-inspection fees, or foreign toll charges
([cash.ch, 2026-08-28](https://www.cash.ch/news/mehrere-kantone-vermuten-missbrauch-von-fahrzeughalterdaten-964337)).
**Defender takeaway:** a per-identity rate limit alone is not a reliable anti-scraping control if it can be defeated
by distributing requests across sources; any public-sector agency running a similarly throttled public-lookup
service should confirm its own rate limiting cannot be bypassed the same way, and should log and alert on aggregate
query volume against the service as a whole, not only per apparent requester.
