---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — Cl0p named 44 victims on its leak site in a single batch, including a Swiss and a Dutch organisation, and one vendor assesses an earlier masked batch as possibly the Windchill campaign"
headline: "Cl0p's leak site went from masked entries to named European victims in one batch, with no stated intrusion route"
summary: >
  A leak-site tracker first recorded 44 named Cl0p victim listings on 2026-08-12,
  among them a Swiss and a Dutch organisation, alongside others in Finland, the United Kingdom, Italy,
  Slovakia, Hungary and France. Separately, Foresiet reviewed an
  earlier batch of 42 masked Cl0p listings on 2026-08-10 whose advertised data categories — project
  repositories, CAD files, engineering drawings and product-lifecycle content — led it to assess a
  possible relationship with the group's PTC Windchill and FlexPLM campaign (CVE-2026-12569), while
  stating that leak-site information alone cannot establish the access route for any listed organisation.
  No named victim has confirmed a compromise, and no source links the named batch to the campaign.
discovered_at: "2026-08-13T05:12:00Z"
event_date: "2026-08-12"
run_id: 2026-08-13T0412Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach, organized-crime]
regions: [europe, switzerland, global]
sectors: [manufacturing, healthcare, technology]
entities: [actor:clop, campaign:clop-windchill-flexplm-extortion-2026]
techniques: [T1190, T1505.003, T1657]
affected_products: ["PTC Windchill", "PTC FlexPLM"]
cves:
  - id: CVE-2026-12569
    cvss: "9.8"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Internet-exposed PTC Windchill PDMLink and FlexPLM deployments prior to the vendor's June 2026 fixes"
    fixed: "See PTC's advisory for the per-release fixed versions"
sources:
  - url: "https://api.ransomware.live/v2/recentvictims"
    publisher: "Ransomware.live"
    date: "2026-08-12"
    role: primary
  - url: "https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/"
    publisher: "Foresiet"
    date: "2026-08-10"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-08-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the available leak-site information alone cannot establish the initial-access vector used against each listed organization"
    publisher: "Foresiet"
verification: single-source
sourcing_note: >
  The listing batch was read directly from the Ransomware.live tracker's recent-victims endpoint this
  run — 44 Cl0p records first recorded on 2026-08-12, with country codes including CH, NL, FI, GB, IT,
  SK, HU and FR. The tracker's timestamps reflect its own crawl, not the leak site's posting behaviour,
  so no publication window or ordering claim is made from them. That tracker mirrors leak-site posts and does not verify them, and the company
  descriptions it carries are machine-generated, so nothing is taken from those descriptions; the
  victims are characterised only by the tracker's own country and activity fields.
  Foresiet supplies the campaign-linkage assessment for a different, earlier masked batch, hedged in its
  own words. No mainstream outlet was found reporting the named batch, and no named victim has confirmed
  an incident, so this ships single-source with the claim boundaries stated in the body rather than as a
  confirmed breach of any named organisation.
confidence: medium
update_of: 2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-27):** the entry on Cl0p's mass-extortion campaign against internet-exposed PTC Windchill and FlexPLM deployments recorded that no victims had yet been listed on the group's leak site. Victims are now being listed, and the shape of the batch — rather than any individual name — is the delta.

Read directly from the Ransomware.live tracker's recent-victims feed this run, 44 named Cl0p listings were all first recorded by the tracker on 2026-08-12 ([Ransomware.live, 2026-08-12](https://api.ransomware.live/v2/recentvictims)). The tracker's own record timestamps advance at a near-constant 33 to 40 seconds apart, which is its crawl cadence rather than anything about the leak site — so the feed establishes that these listings were picked up in one sweep, and nothing at all about when Cl0p actually posted them. This entry therefore makes no claim about a publication window. The country codes attached to the records include Switzerland, the Netherlands, Finland, the United Kingdom, Italy, Slovakia, Hungary and France alongside a larger United States contingent; the tracker files the Dutch listing under healthcare and the Swiss one under retail and e-commerce. That tracker mirrors what the leak site publishes and verifies none of it; the company descriptions it prints alongside each record are machine-generated and are not used here. What the feed establishes is that the listings exist, when they appeared, and that European organisations are among them — nothing about whether any of those organisations was in fact compromised.

**On whether this batch is the Windchill campaign, the honest answer is that nobody has said so.** Foresiet reviewed a batch of 42 *masked* Cl0p listings and published on 2026-08-10, noting that the advertised data categories recurred with unusual consistency — project repositories, databases, CAD files, engineering drawings, backups and product documentation, with three listings spelling the Windchill product name directly — and that this pattern resembles product-lifecycle-management content more than a general file share. Its conclusion is carefully bounded: it assesses a possible relationship with the broader Cl0p activity involving CVE-2026-12569, while stating that "the available leak-site information alone cannot establish the initial-access vector used against each listed organization", and that it had no forensic access to any affected environment ([Foresiet, 2026-08-10](https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/)). Foresiet's batch is an earlier, masked one; whether the 12 August named batch is the same set unmasked is not stated by any source read this run, and is not asserted here.

What is independently confirmed is the underlying vulnerability's status. CVE-2026-12569, the unauthenticated deserialization remote-code-execution flaw in PTC Windchill PDMLink and FlexPLM, has been in the CISA Known Exploited Vulnerabilities catalog since 2026-06-25 and carries "Known" in its ransomware-campaign-use field, checked directly against catalog version 2026.08.11 ([CISA KEV catalog, 2026-08-11](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Foresiet also restates the post-exploitation behaviour PTC itself documented: web shells planted under the Windchill login directory, which provide persistent access and command execution after the initial exploitation and which survive patching unless separately found and removed ([Foresiet, 2026-08-10](https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/)).

**Defender takeaway:** for anyone running Windchill or FlexPLM the operational instruction has not changed since July — patch, remove unnecessary external exposure, and hunt historically rather than assume the fix was sufficient. What the listing batch changes is the timing assumption behind that instruction. Cl0p's established pattern on mass-exploitation campaigns is a long gap between exfiltration and publication, and a batch of named listings is what the end of that gap looks like: for organisations in the affected population, the negotiation window is closing rather than opening, which makes the retrospective question — was data taken from our environment in June, and is a web shell still there — considerably more urgent than the prospective one. The presence of a Swiss and a Dutch organisation in the batch is a reminder that this campaign's European tail is real; it is not, on this evidence, a confirmation that either was breached, and neither company has said anything publicly that this run could find.
