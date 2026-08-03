---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: "2026-W31 looking ahead — items already in motion: a committed firmware date of 12 August, WebSphere fix packs not due before 3Q2026, an extortion campaign between exfiltration and publication, three flaws with no fix at all, and the CRA reporting clock at six weeks"
headline: "W31 outlook — the 12 August CHARX firmware deadline, WebSphere on interim fixes, and Cl0p's pending listings"
summary: >
  A watch list of items already in motion at the close of ISO week 2026-W31, each with a source and a date —
  not predictions. Phoenix Contact has committed to CHARX SEC-3xxx firmware 1.9.1 no later than 2026-08-12,
  with closed-network operation the only control until it ships. IBM's permanent WebSphere fix packs are
  targeted for 3Q2026, leaving interim APARs as the sole remediation for two CVSS 9.8 pre-auth flaws. Cl0p had
  not begun listing Windchill victims as of 22 July, placing affected organisations between exfiltration and
  publication. Three flaws have no fix at all — Langflow's exploited pre-auth RCE, fastjson 1.x, and the
  Desigo CC V7 family. The Rails Active Storage chain is fully public four weeks ahead of its planned date.
  And the CRA's reporting obligations begin 2026-09-11.
discovered_at: "2026-08-02T23:59:45Z"
event_date: "2026-07-30"
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, actively-exploited, poc-public, ot-ics, ransomware]
regions: [global, europe, switzerland]
sectors: [public-sector, energy, technology, manufacturing, transport]
entities:
  - actor:clop
  - campaign:clop-windchill-flexplm-extortion-2026
  - policy:eu-cyber-resilience-act
techniques: []
affected_products: ["Phoenix Contact CHARX SEC-3000", "IBM WebSphere Application Server", "PTC Windchill", "Langflow", "Alibaba fastjson", "Siemens Desigo CC", "Ruby on Rails Active Storage"]
cves: []
sources:
  - url: "https://certvde.com/en/advisories/VDE-2026-008/"
    publisher: "CERT@VDE"
    date: "2026-07-30"
    role: primary
  - url: "https://www.ibm.com/support/pages/node/7281631"
    publisher: "IBM PSIRT"
    date: "2026-07-28"
    role: primary
  - url: "https://www.ibm.com/support/pages/node/7281649"
    publisher: "IBM PSIRT"
    date: "2026-07-28"
    role: primary
  - url: "https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/"
    publisher: "Ransom-ISAC / eCrime.ch / DEFUSED"
    date: "2026-07-22"
    role: primary
  - url: "https://www.zerodayinitiative.com/advisories/ZDI-26-035/"
    publisher: "Zero Day Initiative (ZDI-26-035)"
    date: "2026-01-09"
    role: primary
  - url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-16723-critical-fastjson-1-x-zero-day-rce/"
    publisher: "Imperva"
    date: "2026-07-24"
    role: primary
  - url: "https://cert-portal.siemens.com/productcert/csaf/ssa-734552.json"
    publisher: "Siemens ProductCERT (SSA-734552, CSAF)"
    date: "2026-07-14"
    role: primary
  - url: "https://discuss.rubyonrails.org/t/cve-2026-66066-attack-details-and-tools-to-perform-a-forensic-investigation/91441"
    publisher: "Ruby on Rails security team"
    date: "2026-07-31"
    role: primary
  - url: "https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act"
    publisher: "Hunton Andrews Kurth"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The updated firmware will be made available as soon as possible, but no later than August 12, 2026."
    publisher: "CERT@VDE"
  - quote: "As of 22 July, Cl0p ransomware has not begun listing victims of this latest campaign on their dark web data leak site or has publicly claimed credit for this latest campaign."
    publisher: "Ransom-ISAC / eCrime.ch / DEFUSED"
  - quote: "Although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026."
    publisher: "Hunton Andrews Kurth"
verification: multi-source
sourcing_note: >
  Every item is a dated commitment or a stated status from the party in a position to know, cited individually.
  Nothing here is a forecast: where a date exists it is the vendor's or regulator's own, and where a status is
  open it is recorded as open rather than resolved in either direction. The Cl0p item states its own as-of date
  because the source does — 22 July is when the absence of victim listings was observed, not the present
  moment. Regulatory clocks prior weeklies recorded but that saw no in-window development this week — the
  Dutch NIS2 Cyberbeveiligingswet, the ENISA managed-security-services consultation, the German
  KRITIS-Dachgesetz registration window — are deliberately not restated here, because carrying them forward
  without a fresh source would be recycling rather than tracking.
confidence: high
update_of: null
references:
  - 2026-08-02/phoenix-contact-charx-sec-3xxx-unauth-root-no-firmware-yet
  - 2026-08-01/ibm-websphere-cve-2026-14512-14446-preauth-no-fix-pack
  - 2026-07-27/clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569
  - 2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev
  - 2026-07-27/cve-2026-16723-fastjson-1x-spring-boot-fat-jar-rce-no-patch
  - 2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed
  - 2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling
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

Items already in motion at the close of 2026-W31, each with a source and a date. None of these is a prediction.

**A firmware release with a committed deadline — 12 August.** CERT@VDE's advisory covering 20 vulnerabilities in Phoenix Contact CHARX SEC-3xxx EV charging controllers, five of them CVSS 9.8 with an unauthenticated network vector, published without the fix: "the updated firmware will be made available as soon as possible, but no later than August 12, 2026." ([CERT@VDE, 2026-07-30](https://certvde.com/en/advisories/VDE-2026-008/)). Until then the vendor's only offered control is closed-network operation behind a firewall — and one of the flaws makes the on-device firewall unavailable for a window during every shutdown. The date is checkable and worth checking.

**Permanent WebSphere fix packs not expected before 3Q2026.** IBM has no workaround for the CVSS 9.8 missing-authentication flaw in the WebSphere Application Server traditional administrative console, and targets the permanent Fix Packs 9.0.5.29 and 8.5.5.31 for 3Q2026, leaving the interim fix under APAR DT496500 as the only remediation now ([IBM PSIRT, 2026-07-28](https://www.ibm.com/support/pages/node/7281631)); a companion bulletin the same day carries the deserialization flaw and APAR PH72166 ([IBM PSIRT, 2026-07-28](https://www.ibm.com/support/pages/node/7281649)). Estates that defer interim fixes on principle are deferring past a quarter boundary.

**An extortion campaign between exfiltration and publication.** Cl0p-affiliated actors have been sending staff-wide emails naming PTC Windchill as the breach vector, but as of the last reported observation the second shoe had not dropped: "as of 22 July, Cl0p ransomware has not begun listing victims of this latest campaign on their dark web data leak site or has publicly claimed credit for this latest campaign." ([Ransom-ISAC, 2026-07-22](https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/)). Any organisation that ran an internet-exposed, unpatched Windchill or FlexPLM instance in June sits inside that gap, and the campaign's own precedent is that listings follow.

**Three flaws with no fix, and one of them exploited.** Langflow's pre-authentication eval injection is being exploited with no documented fixed version, and ZDI's only stated mitigation is to restrict interaction with the product ([Zero Day Initiative, 2026-01-09](https://www.zerodayinitiative.com/advisories/ZDI-26-035/)). fastjson 1.x will not receive one: "FastJson 1.x is no longer actively maintained, and no patched 1.x version has been released for this vulnerability." ([Imperva, 2026-07-24](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-16723-critical-fastjson-1-x-zero-day-rce/)). And Siemens records the entire Desigo CC V7 family under remediation category `none_available`, with network segmentation as the only offered control ([Siemens ProductCERT, 2026-07-14](https://cert-portal.siemens.com/productcert/csaf/ssa-734552.json)). These three leave the vulnerability queue by being made unreachable or not at all.

**An embargo that has already broken.** The Rails security team abandoned its plan to withhold the CVE-2026-66066 Active Storage exploitation details until 2026-08-28, publishing the attack write-up four weeks early along with a forensic-evidence guide and tooling to determine whether an application was vulnerable and whether it was exploited ([Ruby on Rails security team, 2026-07-31](https://discuss.rubyonrails.org/t/cve-2026-66066-attack-details-and-tools-to-perform-a-forensic-investigation/91441)). The window in which the chain was private is closed; what remains in motion is the population of unpatched applications, and the published forensic check is how an operator establishes which side of it they are on.

**The CRA reporting clock, at six weeks.** "Although the principal obligations will apply from December 11, 2027, reporting obligations take effect on September 11, 2026." ([Hunton Andrews Kurth, 2026-07-29](https://www.hunton.com/privacy-and-cybersecurity-law-blog/european-commission-issues-guidance-on-the-cyber-resilience-act)). From that date the regulation's reporting obligations bind manufacturers of products with digital elements — which for this constituency is a change in what EU-market suppliers owe their customers, arriving more than a year before the rest of the regulation applies. The notification window and article number are deliberately not stated here: no source fetched this run carries them.
