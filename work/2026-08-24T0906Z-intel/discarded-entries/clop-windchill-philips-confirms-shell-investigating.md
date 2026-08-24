---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — Cl0p's batch gets its first named-victim confirmation: Philips says it contained an attempted compromise of an enterprise server, Shell is investigating, Fiserv disputes any loss"
headline: "Four named companies gave four different answers on the same day — and no source establishes how any of them was reached"
summary: >
  Cl0p added Philips and Shell to its leak site on 2026-08-12, and a Reuters report the next day put the batch at
  nearly 50 companies worldwide including Fiserv and GE. Philips confirmed it had identified and contained an
  attempted compromise of a specific enterprise server holding internal data, and says customer environments are not
  affected; Shell says it is aware of a possible incident and is investigating; GE has initiated its cyber response
  protocols; Fiserv says its review to date found no evidence that customer, banking, transaction or personal data was
  compromised. This is the first named-victim confirmation in a campaign this pipeline has tracked as claim-only —
  but Reuters is explicit that it is not clear how the companies were allegedly accessed, and the PTC Windchill and
  FlexPLM link rests on an industry advisory of 22 July rather than on any statement about these victims.
discovered_at: "2026-08-14T05:10:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - organized-crime
regions:
  - europe
  - global
sectors:
  - healthcare
  - energy
  - manufacturing
  - finance
entities:
  - actor:clop
  - campaign:clop-windchill-flexplm-extortion-2026
techniques:
  - T1190
  - T1657
affected_products:
  - "PTC Windchill"
  - "PTC FlexPLM"
cves:
  - id: CVE-2026-12569
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "PTC Windchill and FlexPLM — see the campaign's earlier coverage for the version detail"
    fixed: "per PTC's advisory in the earlier coverage"
sources:
  - url: "https://wkzo.com/2026/08/13/philips-shell-targeted-by-hacking-group/"
    publisher: "Reuters (via WKZO)"
    date: "2026-08-13"
    role: primary
  - url: "https://www.zataz.com/cl0p-cible-philips-et-shell-deux-geants-europeens/"
    publisher: "ZATAZ"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Philips has identified and contained an attempted ‌cybersecurity compromise ​of a specific enterprise server related to internal data"
    publisher: "Reuters (via WKZO)"
  - quote: "While it’s not clear how the hackers ‌allegedly accessed the companies, Ransom-ISAC, an industry information sharing group, issued a notice July 22 warning that the hacking group was exploiting vulnerabilities in PTC Windchill and FlexPLM, software used to aid in engineering and manufacturing processes."
    publisher: "Reuters (via WKZO)"
verification: multi-source
sourcing_note: "The CVE record carries the score and exploitation status forward from this campaign's earlier coverage so the store stays consistent on one identifier; neither source cited here mentions a CVE at all. Reuters carries the four company statements directly and is the primary here; ZATAZ reports the leak-site additions and the claimed data volumes independently in French. The claimed volumes come from Cl0p alone and ZATAZ says so. The link between these named victims and the PTC Windchill and FlexPLM campaign is an inference from an industry advisory of 22 July, not a statement by any victim, PTC or an investigating authority — and this entry does not assert it."
confidence: medium
update_of: 2026-08-13/clop-leak-site-names-44-victims-swiss-dutch-listings
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-13):** yesterday's entry recorded 44 named Cl0p listings appearing in a single tracker batch, with no named victim confirming anything and no source linking that batch to the group's PTC Windchill and FlexPLM campaign. Both halves of that gap have now moved, in opposite directions.

**A victim has confirmed.** Cl0p added Philips and Shell to its leak site on 12 August, and Reuters reported the companies' responses the following day, putting the total claim at nearly 50 companies worldwide including Fiserv and GE. Philips — the Dutch health-technology group — stated that ["Philips has identified and contained an attempted ‌cybersecurity compromise ​of a specific enterprise server related to internal data"](https://wkzo.com/2026/08/13/philips-shell-targeted-by-hacking-group/), adding that the incident does not impact customer environments. That is the first time in this campaign a named organisation has acknowledged a real technical event rather than leaving a criminal listing unanswered, and the distinction Philips draws matters: an internal enterprise server can hold sensitive material without any consequence for the systems its customers use, and nothing in the available reporting establishes an operational impact on Philips products or services ([ZATAZ, 2026-08-13](https://www.zataz.com/cl0p-cible-philips-et-shell-deux-geants-europeens/)). The other three answers differ from each other and from Philips: Shell said it is aware of a recent possible incident and is working with its security teams and external experts to investigate; GE said it has initiated its cyber response protocols and is working to assess the potential issue; and Fiserv said that based on its comprehensive review to date it had found no evidence that customer, banking, transaction or personal data had been compromised, or that its operating environment had been affected ([Reuters via WKZO, 2026-08-13](https://wkzo.com/2026/08/13/philips-shell-targeted-by-hacking-group/)). Cl0p claims roughly 89 GB from Shell — project plans, technical drawings, facility photographs and test reports — and 13.5 GB from Philips in the form of PDF drawings, diagrams and plans; ZATAZ states plainly that these volumes come from the criminals alone and have not been independently verified ([ZATAZ, 2026-08-13](https://www.zataz.com/cl0p-cible-philips-et-shell-deux-geants-europeens/)).

**The access route did not move.** Reuters is careful about the one thing a defender most wants: ["While it’s not clear how the hackers ‌allegedly accessed the companies, Ransom-ISAC, an industry information sharing group, issued a notice July 22 warning that the hacking group was exploiting vulnerabilities in PTC Windchill and FlexPLM, software used to aid in engineering and manufacturing processes"](https://wkzo.com/2026/08/13/philips-shell-targeted-by-hacking-group/). The advisory's author, Brandon Parsons of Ascent Solutions, told Reuters some companies began receiving notices from Cl0p on 19 or 20 July, and characterised the group as professional data extortionists who target a specific vulnerability rather than a specific company. So the campaign attribution for these named victims remains circumstantial — the data categories Cl0p advertises (engineering drawings, product-lifecycle content) fit a product-lifecycle-management platform, and the timing fits, but no victim, no vendor and no authority has connected them.

**Defender takeaway:** for anyone running PTC Windchill or FlexPLM the practical position is unchanged from this campaign's earlier coverage, and this update adds nothing to patch. What it does add is calibration for how a claim-only listing should be treated while it is unresolved. Four organisations named in one batch produced a confirmed-and-contained event, an unresolved investigation, an opened response process, and a review finding nothing — which is the expected distribution, not a contradiction, and is why an unanswered listing supports neither an assumption of compromise nor an assumption of fabrication. The operationally useful signal in the batch is the data categories rather than the names: engineering drawings, facility photographs and test reports are what an extortion group takes from a product-lifecycle platform, and an organisation that runs one and received an extortion notice in the 19-20 July window has a specific date range and a specific system to reconstruct against.
