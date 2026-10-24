---
schema: 1
kind: threat
title: "AdFection: Citizen Lab and Confiant document zero-click Candiru spyware delivered through targeted online ads from the ad-tech firm Discover-Tech, with ad impressions on defence-ministry, armed-forces and NATO networks"
headline: "Citizen Lab: spyware delivery through targeted ads, with defence and government networks among the impressions"
summary: >
  Citizen Lab and Confiant report that Discover-Tech, an ad-tech firm, serves targeted ads whose code decides per device whether to return JavaScript, and that for chosen devices the chain hands off to servers Citizen Lab links with high confidence to Candiru spyware;
  at least 45 devices at Al Jazeera were targeted in 2024 and 2025. Citizen Lab's bidding data shows Discover-Tech ads on networks of defence ministries, armed forces, national cyber agencies and NATO, though an impression alone does not prove infection, and neither report mentions Switzerland.
discovered_at: "2026-10-16T04:19:00Z"
updated_at: null
event_date: "2026-10-15"
run_id: 2026-10-16T0256Z-intel
priority: notable
immediate_action: null
tags: [espionage, mobile]
regions: [global]
sectors: [public-sector, defense, media]
entities: ["campaign:adfection-discover-tech-candiru-2026", "actor:discover-tech", "actor:candiru"]
techniques: [T1189, T1583.008, T1592, T1546.015, T1027, T1071.001]
affected_products: []
cves: []
sources:
  - url: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
    publisher: "Citizen Lab"
    date: "2026-10-15"
    role: primary
  - url: "https://blog.confiant.com/p/adint-weaponized-ad-tech-for-zero-click-spyware-and-mass-identity-vacuuming"
    publisher: "Confiant"
    date: "2026-10-15"
    role: primary
closed_sources: []
evidence:
  - quote: "Devices at international news network Al Jazeera were infected with mercenary spyware from Candiru"
    publisher: "Citizen Lab"
    source_url: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  - quote: "A Discover-Tech ad impression does not in and of itself confirm targeting or infection with spyware."
    publisher: "Citizen Lab"
    source_url: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  - quote: "Where possible, block online advertising at the gateway to your organization, and on work-issued and edge devices."
    publisher: "Citizen Lab"
    source_url: "https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/"
  - quote: "Even though we have not captured a full exploit chain in the wild"
    publisher: "Confiant"
    source_url: "https://blog.confiant.com/p/adint-weaponized-ad-tech-for-zero-click-spyware-and-mass-identity-vacuuming"
verification: multi-source
sourcing_note: >
  Citizen Lab and Confiant published co-timed reports as research partners; Citizen Lab holds the victim network logs and the implant and makes the Candiru attribution, on which Confiant's rests, while Confiant independently supplies the ad-delivery telemetry and the cloaking detail and says it has not captured a full exploit chain.
confidence: high
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

Citizen Lab reports that in 2024 and 2025 at least 45 devices at the news network Al Jazeera were targeted in zero-click attacks that it links with high confidence to Candiru spyware delivered through ads bought by Discover-Tech, an Israeli firm that presents itself as an ad company ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). An ad carries a script tag that calls Discover-Tech's ad-decision server with the user's cookie or mobile advertising identifier; the server decides, apparently from the source address and the identifiers, whether the device is eligible, and returns JavaScript only if so and a zero-byte response otherwise, which keeps malicious code and pointers to it out of what ad vendors can inspect ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). In Al Jazeera's network logs an infected device first contacted Discover-Tech infrastructure, which indicates an ad impression, then a Candiru validator server that checks the device, and finally a Candiru command-and-control server; a Windows implant that Al Jazeera isolated from a compromised device and Citizen Lab analysed persists through COM hijacking ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). Confiant, working from ad-delivery telemetry from April to September 2026, describes a cloaked payload that fingerprints the device and opens an encrypted channel, and found a hand-off to Candiru-attributed infrastructure, with Belgium by far the most targeted country at 56 percent of the global hits in the period; it has not captured a full exploit chain ([Confiant, 2026-10-15](https://blog.confiant.com/p/adint-weaponized-ad-tech-for-zero-click-spyware-and-mass-identity-vacuuming)).

Citizen Lab's analysis of four billion Discover-Tech bidding records shows ads on almost 200,000 websites and apps in four months, including on devices in networks of defence ministries, armed forces, national cyber agencies and intergovernmental organizations such as NATO; an impression alone does not prove targeting or infection ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). Google, IAB Europe, Beeswax, Vungle (Liftoff) and Eskimi disconnected Discover-Tech after the disclosure ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)).

**Exposure:** any device that renders third-party ads in a browser or an app, on staff whose phones or workstations an espionage buyer would want, such as defence, security and diplomatic staff; no source reports an infection in Switzerland, and neither report mentions it ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)).

**Detection:** in per-device web-proxy, DNS and egress logs the reported signature is contact with Discover-Tech infrastructure, which marks an ad impression, followed by a connection to a validator server and finally to a command-and-control server, the sequence seen in Al Jazeera's network logs ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). Confiant adds that the ad-delivered SDK resolves an operator-chosen domain over DNS-over-HTTPS and reaches it by raw IP, so it never appears as a plaintext DNS query or connection hostname and stays invisible to DNS-based monitoring and blocklists ([Confiant, 2026-10-15](https://blog.confiant.com/p/adint-weaponized-ad-tech-for-zero-click-spyware-and-mass-identity-vacuuming)). On a Windows endpoint, the implant Citizen Lab analysed persists through COM hijacking, so a new COM registration that points at an unfamiliar DLL is the artifact to look for.

**Triage:** ordinary ad tags also call identifier-bearing endpoints and sync user IDs; the reported discriminators are the eligibility gating, with an empty reply for ineligible devices and code only for chosen ones, and the validator-then-command-and-control sequence ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)).

**Defender takeaway:** the delivery is zero-click and needs no user action, and Citizen Lab says there is currently no consistently safe way to expose users and networks to targeted ads; its control is to block online advertising at the organization's gateway and on work-issued and edge devices ([Citizen Lab, 2026-10-15](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)).
