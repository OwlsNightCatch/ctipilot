---
schema: 1
kind: synthesis
horizon: strategic
title: >
  Cl0p PTC Windchill campaign status: the extortion wave crossed from leak-site assertion to
  partial victim corroboration this week — Philips and Shell responded, European organisations
  appeared among the named listings, and a second vendor confirmed the webshell artefact PTC had
  already documented
headline: >
  Windchill campaign status — first victim responses, named European listings, and independent
  corroboration of the JSP webshell artefact
summary: >
  Status update on the Cl0p mass-extortion campaign against internet-exposed PTC Windchill and
  FlexPLM deployments, tracked here since 27 July through CVE-2026-12569. Three in-window deltas
  move it from claim to partial corroboration. A leak-site tracker recorded 44 named Cl0p victim
  listings on 12 August, among them a Swiss and a Dutch organisation alongside others in Finland,
  the United Kingdom, Italy, Slovakia, Hungary and France; separately, a vendor reviewing an
  earlier batch of 42 masked listings assessed a possible relationship with this campaign from the
  advertised data categories, while stating leak-site information alone cannot establish the
  access route for any listed organisation. Two days later Philips said an attempted attack on a
  specific company server had been brought under control with no impact on customer environments,
  and Shell said it was aware of a potential incident and investigating — the first responses from
  named organisations. ReliaQuest separately reported actors deploying JSP webshells on
  compromised product-lifecycle platforms, which corroborates rather than introduces the artefact
  class: PTC itself had already documented hexadecimal-named JSP webshells under the Windchill
  login directory. The two victim counts in circulation differ — a leak-site tracker recorded 44
  named listings, BleepingComputer counts 43 — and neither is a count of confirmed victims.
discovered_at: "2026-08-16T23:59:00Z"
updated_at: "2026-08-23T23:59:00Z"
event_date: 2026-08-14
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags:
  - ransomware
  - organized-crime
  - data-breach
  - actively-exploited
  - cisa-kev
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - energy
  - healthcare
  - manufacturing
  - finance
entities:
  - "actor:clop"
  - "campaign:clop-windchill-flexplm-extortion-2026"
techniques:
  - T1190
  - T1505.003
  - T1657
  - T1555
  - T1552.001
  - T1041
affected_products:
  - PTC Windchill
  - PTC FlexPLM
cves: []
sources:
  - url: "https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/"
    publisher: BleepingComputer
    date: 2026-08-14
    role: primary
  - url: "https://nltimes.nl/2026/08/13/russian-ransomware-group-clop-claims-cyberattacks-shell-philips"
    publisher: NL Times
    date: 2026-08-13
    role: primary
  - url: "https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/"
    publisher: Foresiet
    date: 2026-08-10
    role: corroborating
  - url: "https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign"
    publisher: ReliaQuest Threat Research Team
    date: 2026-08-18
    role: primary
  - url: "https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581"
    publisher: GovInfoSecurity (ISMG)
    date: 2026-08-17
    role: primary
closed_sources: []
evidence:
  - quote: "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext"
    publisher: ReliaQuest Threat Research Team
  - quote: "GE is no longer on Clop's darkweb leak site of companies that have not contacted it to negotiate a payoff."
    publisher: GovInfoSecurity (ISMG)
  - quote: "Toast identified unauthorized access to a limited number of files; to date, the files identified contain nonsensitive internal documents,"
    publisher: "Toast spokesperson, quoted by GovInfoSecurity (ISMG)"
verification: multi-source
sourcing_note: >
  The victim responses are the organisations' own statements to the reporting outlets and are the
  strongest evidence in this entry. The 44 named listings come from a leak-site tracker and are
  the actor's claims, not confirmations — no named victim beyond Philips and Shell has responded
  publicly, and neither of those statements attributes the incident to the Windchill flaw. The
  possible relationship between the earlier masked batch and this campaign is Foresiet's
  assessment from advertised data categories, and Foresiet itself states leak-site information
  alone cannot establish an access route. The JSP webshell finding is ReliaQuest's, relayed
  through the reporting rather than read first-hand this run; the prior PTC documentation of the
  same artefact class is carried by Foresiet, which is cited for it. The 44-listing count is not
  cited to the tracker's live API endpoint, which is a rolling window that no longer returns those
  records; it is attributed to the operational entry that recorded it on 13 August, and the
  divergent count BleepingComputer reports is stated alongside it.
confidence: medium
references:
  - 2026-06-20/ptc-windchill-cve-2026-12569-unauthenticated-java-deserializ
weekly_section: weekly-long-running
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-23T23:59:00Z"
    run_id: 2026-08-23T2311Z-weekly
    type: update
    summary: >
      Status update on the Cl0p mass-extortion campaign against internet-exposed PTC Windchill and
      FlexPLM deployments, tracked here since 27 July through CVE-2026-12569 and consolidated in the
      two previous weeklies. Three in-window deltas. ReliaQuest published a reverse-engineering
      analysis on 2026-08-18 attributing the custom implant to Cl0p as highly likely, and it moves the
      campaign from "web shells were deployed" to a measurable credential exposure: one command reads
      Windchill's configuration file and decrypts the application keystore in plaintext including the
      LDAP manager password, an in-built Java class loader executes attacker-supplied bytecode in
      memory, and every database query runs through the application's own connection classes so
      telemetry attributes the theft to the normal service identity. Second, the named-victim count
      has plateaued around 43 to 45 since 2026-08-15 with no new names in follow-on coverage through
      2026-08-21. Third, and carried as reported rather than confirmed, one outlet observing the leak
      site states General Electric is no longer listed on it; two further named companies gave first
      statements bounding their own exposure.
    fields:
      - evidence
      - references
      - regions
      - sectors
      - sources
      - techniques
      - body
    merged_from: 2026-08-23/weekly-w34-clop-windchill-status
migrated_from: null
---

Status update on the Cl0p extortion campaign against internet-exposed PTC Windchill and FlexPLM product-lifecycle platforms, which this pipeline has tracked since 27 July on CVE-2026-12569. Prior coverage recorded the campaign in a state that is common for this actor and unsatisfying for defenders: a KEV-listed flaw, an extortion wave under way, and a set of leak-site listings that no victim had acknowledged. Three things changed this week, and together they move it from assertion toward evidence without closing the central gap.

The listings became European and named. This pipeline's operational entry of 13 August recorded a leak-site tracker carrying 44 named Cl0p victim entries on 12 August, among them a Swiss and a Dutch organisation, alongside others in Finland, the United Kingdom, Italy, Slovakia, Hungary and France — a shift from the masked entries the campaign had been posting. The count is not stable across sources: BleepingComputer, reporting Shell's response two days later, reports that "the Clop gang listed it on its leak site as one of 43 new victims likely targeted in data theft attacks against Internet-exposed PTC Windchill and FlexPLM instances exploiting a critical improper input validation vulnerability tracked as CVE-2026-12569" ([BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)). Neither figure is a count of confirmed victims. Separately, Foresiet reviewed an earlier batch of 42 masked listings and assessed a possible relationship with the Windchill and FlexPLM campaign on the basis of the advertised data categories — project repositories, CAD files, engineering drawings and product-lifecycle content — while stating explicitly that leak-site information alone cannot establish the access route for any listed organisation ([Foresiet, 2026-08-10](https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/)). That caveat is the one to carry: the categories are consistent with a PLM platform and consistent with a dozen other sources of the same file types.

Then two named organisations responded, which had not happened before in this campaign. Philips described an attempted cyberattack on a specific company server holding internal data, said it had been brought under control, and stated there was no impact on customer environments; Shell said it was aware of a potential incident and was investigating ([NL Times, 2026-08-13](https://nltimes.nl/2026/08/13/russian-ransomware-group-clop-claims-cyberattacks-shell-philips); [BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)). Neither statement attributes its incident to the Windchill flaw, and neither confirms the actor's claimed scope — Philips's account in particular describes a contained single-server event rather than the archive the leak site advertises. The third delta is corroboration rather than novelty, and this entry corrects its own earlier framing of it: ReliaQuest reported the actors deploying JSP webshells on compromised product-lifecycle platforms, relayed in the same reporting — but the artefact class was already public. Foresiet's 10 August analysis records that "PTC went on to report heightened threat activity and documented attackers deploying JSP webshells inside Windchill login directories", naming hexadecimal-named webshells under `/Windchill/login/`, a custom `X-windchill-req` HTTP request header, and `flst.txt` as an artefact of attacker file-listing activity ([Foresiet, 2026-08-10](https://foresiet.com/blog/cl0p-windchill-flexplm-cve-2026-12569/)). ReliaQuest's report is a second, independent observation of what the vendor had already described.

**Defender takeaway:** for an organisation running Windchill or FlexPLM the hunt has been available longer than this week's reporting suggests, which is the more useful correction — PTC documented the webshell artefact class, down to the directory and the custom request header, before this week, and ReliaQuest has now independently observed the same thing. A JSP webshell on a Java application server is a well-understood hunt: unexpected `.jsp` files under the application's deployment directories with modification times outside any change window, and application-server worker processes spawning command interpreters. That hunt does not depend on the actor's claims being accurate, which is why it is worth running on an exposed instance regardless of whether the organisation appears on the leak site. The broader calibration point is unchanged from earlier coverage and reinforced by this week: a Cl0p listing is an assertion about data the actor holds, not evidence about how it was obtained, and Philips's response is a concrete instance of the gap between the two. For a triage queue ingesting leak-site feeds, a named listing warrants a scoped exposure check of the platform the campaign is known to target — not an incident declaration.

**Triage:** the discriminator for the webshell artefact is provenance rather than content, because legitimate JSP files live in exactly the same directories. A file written into a deployed web application outside a deployment or patch window, owned by the application-server service account rather than by the deployment tooling, and not present in the build artefact the platform team can reproduce, is the signal — a legitimate deployment replaces a whole application archive and leaves a matching record in the change system. The corresponding runtime observable is the application-server process becoming a parent to a shell or command interpreter, which a product-lifecycle platform has no routine reason to do.

## Update — 2026-08-23T23:59:00Z

The prior weekly recorded this campaign crossing from leak-site assertion to partial victim corroboration — Philips and Shell responding, European organisations among the listings, a second vendor corroborating the web-shell artefact PTC had already documented. This week the assertion side has gone quiet and the technical side has opened up.

**The implant is documented, and the credential exposure is now specific.** ReliaQuest's reverse engineering, published 2026-08-18, states the activity was highly likely conducted by Cl0p and describes something purpose-built against Windchill rather than a generic shell. The single most consequential capability is a credential dump: "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext" — implemented by reading the application's configuration file, decrypting the LDAP manager password from the keystore, and then iterating every remaining stored property to decrypt administrative account credentials, object-storage credentials and all site administrator keys ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). That converts a single application compromise into a directory compromise wherever the LDAP manager account governs authentication for the wider estate. Two further properties matter for anyone hunting: commands arrive in a custom HTTP request header rather than in a URL or body, so controls inspecting only paths and parameters see no command traffic at all; and the implant's database queries run through Windchill's own connection classes, so database telemetry attributes the theft to the application's normal service identity.

**The victim list has stopped growing.** Follow-on coverage through 2026-08-21 adds no new named victims and no new technical developments, and the count that has been in circulation since 2026-08-15 — in the low-to-mid forties, with different trackers and outlets disagreeing by one or two — has not moved. ISMG's own framing puts the group's claim at more than 40 firms ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)). A plateau is not evidence that exploitation has stopped; Cl0p's historical pattern is to publish in batches, and ReliaQuest assesses with high confidence that exploitation will expand to more organisations in the coming weeks.

**One name left the list, and two more bounded their exposure.** ISMG reports that "GE is no longer on Clop's darkweb leak site of companies that have not contacted it to negotiate a payoff", framing the removal as consistent with either a ransom payment or a resumed negotiation ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)). This run could not find a second outlet that checked the listing itself, so that observation is one outlet's and is carried as such — but it is worth recording precisely because it is the only publicly visible signal of a negotiation outcome anywhere in this campaign. Two other named companies gave first statements to the same outlet, both bounding rather than denying: Toast, from which the group claims files, said "Toast identified unauthorized access to a limited number of files; to date, the files identified contain nonsensitive internal documents," adding that it isolated the affected systems the same day it detected the activity and considers the situation contained; Fiserv, from which the group claims 874 gigabytes including computer-aided design files, said none of its customer, bank, transaction or personal data were stolen based on a comprehensive review to date ([GovInfoSecurity, 2026-08-17](https://www.govinfosecurity.com/clop-claims-data-theft-from-more-than-40-companies-a-32581)).

**Defender takeaway:** the status change that should reach a remediation ticket this week is the keystore, not the victim count. Any organisation that ran an internet-exposed Windchill instance during the exploitation window now has a published, specific answer to "what would the attacker have taken" — the whole application keystore, in one command — and that answer outlives the patch. The two follow-ups ReliaQuest names are the ones most likely to be skipped: rotate on the assumption that the full decrypted set left, across every downstream system where those credentials are reused, and terminate sessions, because rotated passwords alone leave existing tokens valid. For anyone still hunting, the cheapest foothold is the file system — unexpected JavaServer Pages in the Windchill codebase directories, prioritising recent modification timestamps and content referencing the application's own keystore utility class — and the cheapest gap to close is web-tier logging that records only method, path and status, which by construction cannot have captured the command channel.
