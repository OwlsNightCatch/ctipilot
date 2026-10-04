---
schema: 1
kind: incident
title: "Unauthorized users read unencrypted Social Security numbers on a Pentagon DMDC personnel file server for nine months; a defense official counts about 3 million people affected"
headline: "A vulnerable Pentagon HR file server sat unencrypted and reachable for nine months before anyone noticed"
summary: >
  Unauthorized users accessed an unencrypted file-sharing server of the Defense Manpower Data Center
  (DMDC), the Pentagon's central personnel-data repository, between October 2025 and 16 July 2026,
  exposing Social Security numbers and other identifying data. A U.S. defense official told ABC News
  the breach affected 2.76 million living people and another 294,000 who are deceased.
discovered_at: "2026-09-27T04:33:00Z"
updated_at: "2026-09-30T04:52:00Z"
event_date: "2026-09-24"
run_id: 2026-09-27T0404Z-intel
priority: routine
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
  Military Times and CNN each independently reviewed and quote the same breach-notification letter,
  and two defense officials confirmed its authenticity to Military Times; ABC News carries a defense
  official's later count. No report names a CVE, an exploit class or whether the server was
  reachable from outside DMDC's network, so no initial-access technique is mapped beyond what is
  stated.
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
  - at: "2026-09-30T07:31:59Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority is lowered from high to routine: a US military data breach with no vector or
      tradecraft defenders can act on. The title, summary, body and the earlier
      2026-09-30 update section are trimmed to routine-incident length, and the sourcing note is
      plain provenance. The exposed data is now described as the letter recipient's rather than every affected person's, and the takeaway drops an access-logging recommendation no source makes.
    fields: [priority, sourcing_note, title, summary, body]
migrated_from: null
---

Unauthorized users accessed files holding unencrypted personal data on a vulnerable file-sharing server of the Defense Manpower Data Center (DMDC), the Pentagon's central personnel-data repository, from October 2025 until DMDC discovered the vulnerability on 16 July 2026 and patched it, and the notification letter says they reached its recipient's Social Security number and at least one further identifying field ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/) · [CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)). A U.S. defense official put the count at 2.76 million living and 294,000 deceased people, and no report names a vulnerability class, access vector or actor ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909)). The lesson for public administrations: a government's central personnel-data store kept identity numbers unencrypted and readable for nine months before discovery ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)).

**Defender takeaway:** check that central personnel and HR data stores encrypt identifying fields at rest, which CNN notes is standard security practice and which DMDC's server lacked ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)).

## Update — 2026-09-30T04:52:00Z

A U.S. defense official told ABC News the breach affected 2.76 million living and 294,000 deceased people, against the roughly four million earlier reported, and described access by "a small number of unauthorized users" between October 2025 and July 2026 that DMDC remediated on discovery ([ABC News, 2026-09-29](https://abcnews.com/Politics/pentagon-breach-exposed-sensitive-data-3-million-people/story?id=136832909) · [Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)).

## Correction — 2026-09-30T07:31:59Z

Military Times quotes the notification letter as exposing its recipient's Social Security number and at least one further identifying field ([Military Times, 2026-09-24](https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/)). The entry previously generalised this to every affected person and advised access logging, which no cited report discusses. CNN reports that the data was not encrypted and that encrypting sensitive data is a standard security practice ([CNN, 2026-09-25](https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach)).
