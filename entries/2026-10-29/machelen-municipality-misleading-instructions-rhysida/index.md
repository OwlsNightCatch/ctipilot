---
schema: 1
kind: incident
title: "Machelen (Belgium) municipality: its own timeline shows a foothold through misleading instructions on an external website on 2026-08-20, found 22 days later after a high-privilege user was reached, with personal data confirmed stolen and Rhysida now listing municipal and social-welfare files"
headline: "Machelen municipality: foothold from a website's misleading instructions, 22 days to detection; Rhysida lists its files"
summary: >
  The Belgian municipality of Machelen published a timeline in which attackers gained access to an internal laptop through misleading instructions on an external website on 2026-08-20,
  reached a user with high privileges on 2026-09-10 and were found on 2026-09-11; it confirms that personal data was stolen. Ransomware.live recorded on 2026-10-27 that the Rhysida group had listed the municipal and
  social-welfare file servers on its leak site, a claim the municipality has not confirmed.
discovered_at: "2026-10-29T04:44:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-29T0255Z-intel
priority: routine
immediate_action: null
tags: [ransomware, data-breach]
regions: [europe]
sectors: [public-sector]
entities: ["incident:machelen-municipality-cyberincident-2026-09", "actor:rhysida"]
techniques: [T1204]
affected_products: []
cves: []
sources:
  - url: "https://www.machelen.be/tijdslijn-cyberincident"
    publisher: "Municipality of Machelen (incident timeline)"
    date: "2026-09-22"
    role: primary
  - url: "https://www.machelen.be/faq-cyberincident-persoonsgegevens"
    publisher: "Municipality of Machelen (FAQ on personal data)"
    date: "2026-09-22"
    role: primary
  - url: "https://itdaily.com/news/security/machelen-municipality-hit-by-cyberattack-via-phishing/"
    publisher: "ITdaily"
    date: "2026-09-23"
    role: corroborating
  - url: "https://www.ransomware.live/id/TWFjaGVsZW4gKEJlbGdpdW0pQHJoeXNpZGE="
    publisher: "Ransomware.live"
    date: "2026-10-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "hackers gain access to an internal laptop through misleading instructions on an external website (translated from Dutch)"
    original: "hackers krijgen toegang tot interne laptop via misleidende instructies op externe website"
    publisher: "Municipality of Machelen (incident timeline)"
    source_url: "https://www.machelen.be/tijdslijn-cyberincident"
  - quote: "hackers have access to a user with high access rights and other IT systems within the organisation (translated from Dutch)"
    original: "hackers hebben toegang tot een gebruiker met hoge toegangsrechten en andere IT-systemen binnen de organisatie"
    publisher: "Municipality of Machelen (incident timeline)"
    source_url: "https://www.machelen.be/tijdslijn-cyberincident"
  - quote: "We can confirm that personal data has been leaked. (translated from Dutch)"
    original: "We kunnen bevestigen dat er persoonsgegevens zijn gelekt."
    publisher: "Municipality of Machelen (FAQ on personal data)"
    source_url: "https://www.machelen.be/faq-cyberincident-persoonsgegevens"
verification: single-source-victim
sourcing_note: >
  The municipality's own timeline and FAQ are the source for the dates, the foothold and the data theft, as a victim's statement about its own incident; ITdaily restates them. The
  Rhysida listing, its volume and its contents are the group's claim as Ransomware.live records them, and the municipality has not confirmed them or named the group. The timeline does not say
  which website or what the instructions asked the user to do, and does not say how the high-privilege user was reached.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Machelen's own timeline records that on 2026-08-20 attackers gained access to an internal laptop through misleading instructions on an external website, explored it extensively from 24 August to 1 September, and on 10 September had access to a user with high access rights and other IT systems; the municipality found the incident on 11 September, isolated all systems, reported to the Belgian CCB-CERT, restarted part of its systems from a backup of a safe date on 14 September and recorded the first evidence of leaked data on 17 September ([Municipality of Machelen, 2026-09-22](https://www.machelen.be/tijdslijn-cyberincident)). It confirms that personal data was leaked and says the scope is still being investigated ([Municipality of Machelen, 2026-09-22](https://www.machelen.be/faq-cyberincident-persoonsgegevens)); the mayor had said on 14 September that no personal data appeared to be affected, and ITdaily reports that this proved wrong ([ITdaily, 2026-09-23](https://itdaily.com/news/security/machelen-municipality-hit-by-cyberattack-via-phishing/)). Ransomware.live recorded on 2026-10-27 that Rhysida listed Machelen on its leak site, describing the listing as municipal and social-welfare file servers of about 1.3 million files, with client files that include passports and identity cards, nursing-home medical files and civil-status records, which are the group's own claims ([Ransomware.live, 2026-10-27](https://www.ransomware.live/id/TWFjaGVsZW4gKEJlbGdpdW0pQHJoeXNpZGE=)).

**Detection:** the timeline puts 22 days between first access and detection, with the first laptop explored from 24 August to 1 September; it names neither the website nor the commands, so the telemetry to review includes endpoint process creation after a user followed instructions on a web page and later use of a high-privilege account from that workstation, which is an inference from the timeline.

**Defender takeaway:** treat a user who followed instructions from a website on a work laptop as a possible intrusion that can sit unseen for weeks; review high-privilege account activity from the user's workstation for the weeks after the event, not only the day it is reported.
