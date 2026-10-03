---
schema: 1
kind: incident
title: "Unauthorized users had nine months of unencrypted access to a Pentagon HR file-sharing server; a defense official counts 2.76 million living and 294,000 deceased people affected, with Social Security numbers exposed"
headline: "A vulnerable Pentagon HR file server sat unencrypted and reachable for nine months before anyone noticed"
summary: >
  A breach-notification letter reviewed independently by Military Times and
  CNN discloses that unauthorized users accessed an unencrypted file-sharing
  server operated by the Defense Manpower Data Center (DMDC), the Pentagon's
  central personnel-data repository holding 60+ million records, between
  October 2025 and 16 July 2026. Social Security numbers and other
  identifying data were exposed; DoD states it has no indication of misuse,
  and a U.S. defense official told ABC News the breach affected 2.76 million
  living people and another 294,000 who are deceased.
discovered_at: "2026-09-27T04:33:00Z"
updated_at: "2026-09-30T04:52:00Z"
event_date: "2026-09-24"
run_id: 2026-09-27T0404Z-intel
priority: high
immediate_action: null
tags: [data-breach]
regions: [us, global]
sectors: [defense, public-sector]
entities: ["incident:pentagon-dmdc-military-personnel-breach-2026-09"]
techniques: [T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/"
    publisher: "Military Times"
    date: "2026-09-24"
    role: primary
  - url: "https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach"
    publisher: "CNN"
    date: "2026-09-25"
    role: primary
  - url: "https://databreaches.net/2026/09/26/pentagon-data-breach-of-military-personnel-raises-national-security-concerns/"
    publisher: "DataBreaches.net"
    date: "2026-09-26"
    role: corroborating
  - url: "https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909"
    publisher: "ABC News"
    date: "2026-09-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "“Unauthorized users” gained access to a vulnerable computer server belonging to the Defense Manpower Data Center (DMDC) beginning last October, but it wasn’t until nine months later, in July, that the Pentagon discovered and remediated the issue, according to a letter the center sent to victims of the breach reviewed by CNN."
    publisher: "CNN"
    source_url: "https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach"
  - quote: "The unauthorized users gained access to the Social Security number of the letter’s recipient, as well as at least one additional piece of identifying information, such as a name, date of birth, contact information, sex, race or military personnel information, including occupational specialty, according to the notification."
    publisher: "Military Times"
    source_url: "https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/"
  - quote: "The stolen data wasn’t encrypted, according to the letter."
    publisher: "CNN"
    source_url: "https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach"
  - quote: "Two people familiar with the incident told Military Times that approximately four million Defense Department personnel may be affected."
    publisher: "Military Times"
    source_url: "https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/"
  - quote: "The breach affected 2.76 million living people and another 294,000 who are deceased, the official said."
    publisher: "ABC News"
    source_url: "https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909"
  - quote: "A Defense Manpower Data Center (DMDC) information system experienced unauthorized access of personally identifiable information by a small number of unauthorized users between October 2025 and July 2026."
    publisher: "ABC News (statement attributed to a U.S. defense official)"
    source_url: "https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909"
verification: multi-source
sourcing_note: >
  Military Times and CNN each independently reviewed and quote the same
  breach-notification letter, and Military Times separately had its
  authenticity confirmed by two defense officials; DataBreaches.net's
  same-window relay corroborates recency but adds no independent fact.
  Neither original report, nor the letter itself, names a CVE, exploit
  class, or whether the affected server was reachable from outside DMDC's
  own network, so this entry does not map an initial-access technique
  beyond what is stated.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T04:52:00Z"
    run_id: 2026-09-30T0404Z-intel
    type: update
    summary: >
      A U.S. defense official told ABC News on 2026-09-29 that the DMDC breach affected 2.76 million living people and
      another 294,000 who are deceased, replacing the earlier estimate of about four million from two unnamed people. The
      official's statement describes unauthorized access by a small number of unauthorized users between October 2025 and
      July 2026 and says the vulnerability was remediated on discovery.
    fields: [title, summary, sources, evidence, body]
migrated_from: null
---

A breach-notification letter dated September 2026 and sent 18 September to affected individuals, reviewed independently by both Military Times and CNN and confirmed authentic by two defense officials, discloses that unauthorized users accessed a vulnerable file-sharing server operated by the Defense Manpower Data Center (DMDC) ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)). DMDC describes itself as the Pentagon's central source for identifying, authenticating, authorizing and providing information on personnel during and after their affiliation with the department, and its own website says it maintains more than 60 million records on military and civilian personnel, contractors, family members, retirees and veterans ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)). Access to the server ran from October 2025 through 16 July 2026, roughly nine months, before DMDC discovered what the notification letter calls a "security vulnerability," patched it and restored the system; neither the letter nor either outlet names a CVE, exploit class, or states whether the server was reachable from outside DMDC's own network ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)).

Data taken from each affected individual's own record included an unencrypted Social Security number plus at least one further identifying field: name, date of birth, contact information, sex, race, or military-personnel and occupational-specialty data ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)). "The stolen data wasn’t encrypted, according to the letter" ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)) despite that being, in CNN's framing, standard security practice for data of this sensitivity. DoD states it has no indication the data has been misused and is offering affected individuals one year of credit monitoring and identity-restoration services through contractor IDX. Two people familiar with the incident first told Military Times that approximately four million Department of Defense personnel may be affected ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)); a U.S. defense official later put the count at 2.76 million living people and another 294,000 who are deceased ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909)).

CNN frames the exposure as a counterintelligence concern, not only a fraud one: combined with other datasets using identifiers like Social Security numbers, the accessed occupational-specialty data could give foreign adversaries a clearer read on who does what for the US military in various parts of the world ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)). A bad actor could pair the DMDC data with other commercial datasets to “learn about or even target [defense personnel] based on their earnings, debts, marriages, spending habits, browsing activities, and worse,” according to Justin Sherman, CEO of Global Cyber Strategies ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)). No party has publicly named who was behind the intrusion.

**Defender takeaway:** the transferable lesson is not a specific vulnerability but a data-handling failure that any organization running a central personnel or HR data store, including a Swiss Armed Forces or civil-protection records system, should treat as a standing audit item: identifying data of this sensitivity, particularly a national identity number, sat unencrypted on a server for nine months without the exposure being detected through the organization's own monitoring, only surfacing when the underlying vulnerability was found. Verify that personnel data stores encrypt identifying fields at rest regardless of the access-control layer in front of them, and confirm that access logging on those stores is sufficient to answer, retroactively, who read what and when, since that is precisely the question this incident could not answer for nine months.

## Update — 2026-09-30T04:52:00Z

A U.S. defense official told ABC News that the breach affected 2.76 million living people and another 294,000 who are deceased, about 3.05 million in all, against the roughly four million the earlier reporting carried ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909)). The official's statement says a DMDC information system experienced unauthorized access to personally identifiable information by "a small number of unauthorized users" between October 2025 and July 2026, and that DMDC remediated the vulnerability on discovery ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909)). Defense officials told ABC they have found no evidence so far that the exposed information has been misused and are offering identity-protection and credit-monitoring resources ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909)). The statement still names no vulnerability class, access vector or actor.
