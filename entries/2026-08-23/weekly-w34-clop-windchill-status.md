---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "UPDATE — Cl0p Windchill campaign status: the implant is now reverse-engineered and one command is shown to return the whole application keystore in plaintext, while the named-victim count has stopped moving and one heavyweight name quietly left the leak site"
headline: "The victim list has plateaued; what changed this week is that the tooling is documented and the credential blast radius is measurable"
summary: >
  Status update on the Cl0p mass-extortion campaign against internet-exposed PTC Windchill and
  FlexPLM deployments, tracked here since 27 July through CVE-2026-12569 and consolidated in the two
  previous weeklies. Three in-window deltas. ReliaQuest published a reverse-engineering analysis on
  2026-08-18 attributing the custom implant to Cl0p as highly likely, and it moves the campaign from
  "web shells were deployed" to a measurable credential exposure: one command reads Windchill's
  configuration file and decrypts the application keystore in plaintext including the LDAP manager
  password, an in-built Java class loader executes attacker-supplied bytecode in memory, and every
  database query runs through the application's own connection classes so telemetry attributes the
  theft to the normal service identity. Second, the named-victim count has plateaued around 43 to 45
  since 2026-08-15 with no new names in follow-on coverage through 2026-08-21. Third, and carried as
  reported rather than confirmed, one outlet observing the leak site states General Electric is no
  longer listed on it; two
  further named companies gave first statements bounding their own exposure.
discovered_at: "2026-08-23T23:59:00Z"
event_date: "2026-08-18"
run_id: 2026-08-23T2311Z-weekly
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, data-breach, actively-exploited]
regions: [global, europe]
sectors: [manufacturing, healthcare, energy, finance]
entities:
  - actor:clop
  - campaign:clop-windchill-flexplm-extortion-2026
techniques: [T1190, T1505.003, T1555, T1552.001, T1041, T1657]
affected_products: ["PTC Windchill", "PTC FlexPLM"]
cves: []
sources:
  - url: "https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign"
    publisher: "ReliaQuest Threat Research Team"
    date: "2026-08-18"
    role: primary
  - url: "https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581"
    publisher: "GovInfoSecurity (ISMG)"
    date: "2026-08-17"
    role: primary
closed_sources: []
evidence:
  - quote: "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext"
    publisher: "ReliaQuest Threat Research Team"
  - quote: "GE is no longer on Clop's darkweb leak site of companies that have not contacted it to negotiate a payoff."
    publisher: "GovInfoSecurity (ISMG)"
  - quote: "Toast identified unauthorized access to a limited number of files; to date, the files identified contain nonsensitive internal documents,"
    publisher: "Toast spokesperson, quoted by GovInfoSecurity (ISMG)"
verification: multi-source
sourcing_note: >
  The implant analysis is ReliaQuest's own reverse engineering, first-hand. The leak-site observation
  and the two company statements are ISMG's own reporting from its outreach to the named companies;
  this run could not find a second outlet that independently checked the leak-site listing state, and
  several secondary write-ups repeat the framing without their own verification pass, so the GE
  observation is carried as reported by one outlet and not as confirmed. ISMG frames the removal as
  consistent with either a payment or a resumed negotiation and this entry does not choose between
  them. No cited source places a Swiss or European organisation in this campaign; the store's earlier
  coverage of the leak-site batch is explicit that no source links those listings to the Windchill
  exploitation, and that remains the position.
confidence: medium
update_of: 2026-08-16/weekly-w33-clop-windchill-status
references:
  - 2026-08-19/clop-windchill-custom-implant-reverse-engineered
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

**UPDATE (originally covered 2026-08-16):** the prior weekly recorded this campaign crossing from leak-site assertion to partial victim corroboration — Philips and Shell responding, European organisations among the listings, a second vendor corroborating the web-shell artefact PTC had already documented. This week the assertion side has gone quiet and the technical side has opened up.

**The implant is documented, and the credential exposure is now specific.** ReliaQuest's reverse engineering, published 2026-08-18, states the activity was highly likely conducted by Cl0p and describes something purpose-built against Windchill rather than a generic shell. The single most consequential capability is a credential dump: "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext" — implemented by reading the application's configuration file, decrypting the LDAP manager password from the keystore, and then iterating every remaining stored property to decrypt administrative account credentials, object-storage credentials and all site administrator keys ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). That converts a single application compromise into a directory compromise wherever the LDAP manager account governs authentication for the wider estate. Two further properties matter for anyone hunting: commands arrive in a custom HTTP request header rather than in a URL or body, so controls inspecting only paths and parameters see no command traffic at all; and the implant's database queries run through Windchill's own connection classes, so database telemetry attributes the theft to the application's normal service identity.

**The victim list has stopped growing.** Follow-on coverage through 2026-08-21 adds no new named victims and no new technical developments, and the count that has been in circulation since 2026-08-15 — in the low-to-mid forties, with different trackers and outlets disagreeing by one or two — has not moved. ISMG's own framing puts the group's claim at more than 40 firms ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)). A plateau is not evidence that exploitation has stopped; Cl0p's historical pattern is to publish in batches, and ReliaQuest assesses with high confidence that exploitation will expand to more organisations in the coming weeks.

**One name left the list, and two more bounded their exposure.** ISMG reports that "GE is no longer on Clop's darkweb leak site of companies that have not contacted it to negotiate a payoff", framing the removal as consistent with either a ransom payment or a resumed negotiation ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)). This run could not find a second outlet that checked the listing itself, so that observation is one outlet's and is carried as such — but it is worth recording precisely because it is the only publicly visible signal of a negotiation outcome anywhere in this campaign. Two other named companies gave first statements to the same outlet, both bounding rather than denying: Toast, from which the group claims files, said "Toast identified unauthorized access to a limited number of files; to date, the files identified contain nonsensitive internal documents," adding that it isolated the affected systems the same day it detected the activity and considers the situation contained; Fiserv, from which the group claims 874 gigabytes including computer-aided design files, said none of its customer, bank, transaction or personal data were stolen based on a comprehensive review to date ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)).

**Defender takeaway:** the status change that should reach a remediation ticket this week is the keystore, not the victim count. Any organisation that ran an internet-exposed Windchill instance during the exploitation window now has a published, specific answer to "what would the attacker have taken" — the whole application keystore, in one command — and that answer outlives the patch. The two follow-ups ReliaQuest names are the ones most likely to be skipped: rotate on the assumption that the full decrypted set left, across every downstream system where those credentials are reused, and terminate sessions, because rotated passwords alone leave existing tokens valid. For anyone still hunting, the cheapest foothold is the file system — unexpected JavaServer Pages in the Windchill codebase directories, prioritising recent modification timestamps and content referencing the application's own keystore utility class — and the cheapest gap to close is web-tier logging that records only method, path and status, which by construction cannot have captured the command channel.
