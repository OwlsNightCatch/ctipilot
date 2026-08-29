---
schema: 1
kind: incident
title: "A Flemish Government agency confirms a DPRK compromise reached it through a contractor's workstation — one of 1,640 organisations a researcher counted from inside the actors' own servers"
headline: "Two years inside North Korean C2 infrastructure produces a victim count, an EU government confirmation, and a contractor with access to 30 companies"
summary: >
  Researcher Vangelis Stykas disclosed at Black Hat USA on 2026-08-05 that nearly two years of maintained
  access to North Korean actors' servers let him identify 1,640 impacted organisations across 57 countries,
  700 to 800 of them with intrusions he calls "really damaging". Digitaal Vlaanderen, part of the Flemish
  Government in Belgium, confirmed to WIRED that Belgium's Centre for Cybersecurity notified it on
  2026-03-03, that the affected workstation was isolated and exposed credentials rotated, and that the
  incident is contained. The dominant access route is the fake-job-interview lure, and the multiplier is
  compromised external contractors — Stykas saw some holding access to up to 30 companies.
discovered_at: "2026-08-08T04:57:00Z"
event_date: "2026-08-05"
run_id: 2026-08-08T0409Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, data-breach, phishing, supply-chain]
regions: [europe, global]
sectors: [public-sector, technology, finance, healthcare]
entities: [incident:nk-contagious-interview-flemish-government-2026-08, campaign:contagious-interview]
techniques: [T1566, T1204.002, T1199, T1078.004]
affected_products: []
cves: []
sources:
  - url: "https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/"
    publisher: "WIRED"
    date: "2026-08-05"
    role: primary
  - url: "https://databreaches.net/2026/08/07/boston-childrens-hospital-named-in-north-korean-hacking-operation/"
    publisher: "DataBreaches.net"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "1,640 companies across 57 countries"
    publisher: "WIRED"
  - quote: "We can confirm that we were notified of this incident on March 3, 2026 by the Centre for Cybersecurity Belgium (CCB), following the researcher’s disclosure,"
    publisher: "WIRED (spokesperson for the Flemish government)"
  - quote: "I have seen a couple of contractors that had access to up to 30 companies,"
    publisher: "WIRED (Vangelis Stykas)"
verification: multi-source
sourcing_note: "The primary disclosure is dated 2026-08-05, inside the developing-story window rather than the 26-hour window; it reached this run through a 2026-08-07 pickup and the story is still producing named-victim statements. The victim count and the actors' internal detail rest on one researcher's access, reported by WIRED; the Belgian government confirmation and Japan's CERT confirmation are independent statements from the affected parties."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Enumerate which external contractors and their personally-managed devices currently hold developer keys or standing access to your systems, and scope each one by what a compromise of that single device would reach — this campaign's blast radius came from contractors holding access to many organisations at once, not from breaching each organisation separately."
migrated_from: null
---

The interesting number in this disclosure is not the victim count. Researcher Vangelis Stykas told Black Hat USA on 2026-08-05 that nearly two years of maintained access to North Korean actors' servers — in some cases reaching the operators' own infected workstations — let him identify "1,640 companies across 57 countries" affected by the country's operations, with around 700 to 800 of them suffering intrusions he describes as "really damaging": company access, root access to servers, root access to AWS ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/)).

The number that changes a defender's model is 30. For many of the impacted organisations, Stykas says, compromised external contractors — who often held developer keys or access to multiple systems — vastly increased the blast radius of a single successful attack: "I have seen a couple of contractors that had access to up to 30 companies" ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/)). The initial access is the long-documented one: developers lured with fake job offers at high salaries and asked to download a program as a coding test, which silently installs malware — the technique Microsoft tracks as the Contagious Interview campaign, running since as early as 2022 ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/)).

One European government body is named and has confirmed. A spokesperson for the Flemish government told WIRED: "We can confirm that we were notified of this incident on March 3, 2026 by the Centre for Cybersecurity Belgium (CCB), following the researcher's disclosure," adding that the affected workstation was isolated, potentially exposed credentials and access were revoked and rotated, and that on its investigation the incident has been contained and remediated ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/)). Japan's CERT says it confirmed the researcher's findings and worked with AEON Smart Technology on remediation. Boston Children's Hospital, also named, says the incident involved a former contractor's personal device rather than its own systems ([DataBreaches.net, 2026-08-07](https://databreaches.net/2026/08/07/boston-childrens-hospital-named-in-north-korean-hacking-operation/)). Other named organisations did not respond to WIRED. Stykas attributes broadly to North Korean operations and names no tracked cluster.

**Defender takeaway:** the Belgian case is the shape to plan against, and it is the mundane one — not a breach of the agency's perimeter, but a contractor's workstation that held access to it. The disclosure route is worth noting too: the agency learned of its own compromise from its national CERT relaying an outside researcher, five months before the public disclosure, which is the realistic detection path for this class rather than internal telemetry. For a public-sector estate the practical question is not "are our contractors trained against fake recruiters" but "what would one compromised contractor device reach", and the answer is usually broader than the contract implies, because the same person is working for several other organisations at the same time.

**Triage:** this campaign's initial access looks like ordinary developer behaviour by design — an engineer running an unfamiliar project as part of a hiring process is a developer running an unfamiliar project. The discriminator available in telemetry is not the execution itself but its provenance and timing: a build or interpreter chain originating from a freshly cloned repository or a downloaded archive that no ticket, project or repository in the organisation accounts for, on an endpoint belonging to someone who is not being onboarded to that work.
