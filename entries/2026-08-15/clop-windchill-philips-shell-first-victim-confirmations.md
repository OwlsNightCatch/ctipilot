---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — the Cl0p Windchill wave gets its first victim confirmations: Philips says a server was hit and contained, Shell says it is investigating, and a second vendor puts JSP webshells on the compromised platforms"
headline: "Philips and Shell respond to Cl0p's claims, moving the PTC Windchill/FlexPLM campaign from leak-site assertion to partial victim corroboration"
summary: >
  Two organisations named in Cl0p's PTC Windchill and FlexPLM extortion batch have now responded. Philips
  describes an attempted cyberattack on a specific company server holding internal data, says it has been
  brought under control and states no impact on customer environments; Shell says it is aware of a potential
  incident and is investigating. ReliaQuest separately reports the actors deploying JSP webshells on compromised
  PLM platforms — the first post-exploitation detail published for this campaign.
discovered_at: "2026-08-15T05:00:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - actively-exploited
  - organized-crime
regions:
  - europe
  - uk
  - global
sectors:
  - healthcare
  - energy
  - manufacturing
entities:
  - actor:clop
  - campaign:clop-windchill-flexplm-extortion-2026
techniques: [T1190, T1505.003]
affected_products:
  - PTC Windchill
  - PTC FlexPLM
cves:
  - id: CVE-2026-12569
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "internet-exposed PTC Windchill and FlexPLM instances"
    fixed: "per PTC advisory"
sources:
  - url: "https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/"
    publisher: BleepingComputer
    date: "2026-08-14"
    role: primary
  - url: "https://nltimes.nl/2026/08/13/russian-ransomware-group-clop-claims-cyberattacks-shell-philips"
    publisher: NL Times
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "\"We are aware of a potential incident. We are working with our security teams and relevant experts to investigate,\" a Shell spokesperson told BleepingComputer when asked to confirm Clop's data theft claims."
    publisher: BleepingComputer
  - quote: "Philips describes the incident as “an attempted cyberattack on a specific company server containing internal data.” The healthcare technology company says the incident has since been brought under control. “This has no impact on customer environments,” a spokesperson added."
    publisher: NL Times
  - quote: "Clop's Windchill and FlexPLM attacks were also confirmed by the Ransomware Information Sharing and Analysis Centre (Ransom-ISAC), a non-profit organization dedicated to the tracking and defense against ransomware threats, and by cybersecurity company ReliaQuest, which said that the threat actors have been deploying JSP webshells that allow them to steal sensitive data from victims' compromised PLM platforms."
    publisher: BleepingComputer
verification: multi-source
sourcing_note: >
  The victim statements are the companies' own, given to two outlets independently. The exfiltration volumes
  remain Cl0p's own claims relayed by a leak-site monitoring platform, which cautions the figures come directly
  from the attackers and are not independently verified; they are attributed as claims throughout.
confidence: high
update_of: 2026-08-13/clop-leak-site-names-44-victims-swiss-dutch-listings
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-13):** yesterday's entry recorded that no organisation named in Cl0p's batch had confirmed a compromise and that leak-site information alone could not establish an access route for any listed victim. Two of them have now spoken, and a second security vendor has published the first post-exploitation detail for the campaign.

Philips, the Netherlands-headquartered health-technology group, describes the incident as an attempted cyberattack on a specific company server containing internal data, says it has since been brought under control, and states it has no impact on customer environments ([NL Times, 2026-08-13](https://nltimes.nl/2026/08/13/russian-ransomware-group-clop-claims-cyberattacks-shell-philips)). Shell told BleepingComputer it is aware of a potential incident and is working with its security teams and relevant experts to investigate ([BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)). Neither statement confirms the volumes Cl0p advertises: the group claims 89 GB from Shell and 13.5 GB from Philips, figures that reach the reporting through a leak-site monitoring platform which cautions they come directly from the attackers and are not independently verified ([NL Times, 2026-08-13](https://nltimes.nl/2026/08/13/russian-ransomware-group-clop-claims-cyberattacks-shell-philips)). BleepingComputer counts Shell among 43 new victims Cl0p listed, likely targeted through internet-exposed PTC Windchill and FlexPLM instances via CVE-2026-12569, and reports General Electric named in the same batch with no comment yet from GE, Philips or PTC to that outlet ([BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)).

The genuinely new defender-facing detail is the tradecraft. BleepingComputer reports the campaign confirmed independently by the Ransomware Information Sharing and Analysis Centre and by ReliaQuest, which says the actors have been deploying JSP webshells that let them steal sensitive data from victims' compromised PLM platforms ([BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/shell-investigates-potential-incident-after-clop-data-theft-claims/)). Until now this campaign was visible only as an exploited CVE at one end and a leak-site listing at the other; a webshell on the application server is the middle of the chain, and it is a durable artefact that outlives the patch. The same report notes PTC warned customers of heightened threat activity on 26 June and that CISA subsequently confirmed active exploitation and added the flaw to its Known Exploited Vulnerabilities catalog.

**Defender takeaway:** the delta changes what an owner of a patched Windchill or FlexPLM instance should do next. Patching closed the entry, but a JSP webshell dropped before the patch survives it — so an instance that was internet-exposed between PTC's June warning and its upgrade warrants a file-integrity review of the application's deployed web content and a look at servlet-container access logs for requests to JSP paths that are not part of the shipped application, rather than an assumption that the upgrade settled the question.

**Triage:** PLM platforms legitimately serve large volumes of engineering drawings and CAD content, so bulk document retrieval alone is weak signal. The discriminators are the requester and the path: retrieval driven by requests to a JSP endpoint absent from the vendor's shipped file manifest, and document access that does not correspond to any authenticated product-lifecycle user session.
