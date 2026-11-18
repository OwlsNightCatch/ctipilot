---
schema: 1
kind: vulnerability
title: "Drupal core: a critical security release for all supported branches (11.4.x, 11.3.x and 10.6.x) is scheduled for 2026-11-18 between 17:00 and 21:00 UTC; the Security Team says at least one flaw can be exploited by anonymous users and that exploits might follow within hours or days"
headline: "Drupal core critical release due 18 Nov 17:00 to 21:00 UTC; at least one flaw reachable by anonymous users"
summary: >
  The Drupal Security Team announced in PSA-2026-11-16 a core security release for Drupal 11.4.x, 11.3.x and 10.6.x on 2026-11-18 between 17:00 and 21:00 UTC. It rates the vulnerabilities critical (18 of 25), says at least one can be exploited by anonymous users and that exploits might be developed within hours or days, and publishes no CVE id, component or fixed version before the release. End-of-life lines are to get interim mitigation steps in the advisory.
discovered_at: "2026-11-18T05:09:00Z"
updated_at: null
event_date: "2026-11-16"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190]
affected_products: ["Drupal Core"]
cves: []
sources:
  - url: "https://www.drupal.org/psa-2026-11-16"
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    date: "2026-11-16"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13196"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The Drupal Security Team urges you to reserve time for core updates at that time because exploits might be developed within hours or days."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "The vulnerabilities are currently rated as critical and at least one can be exploited by anonymous users."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
  - quote: "Neither the Security Team nor any other party is able to release any more information about this vulnerability until the announcement is made."
    publisher: "Drupal Security Team (PSA-2026-11-16)"
    source_url: "https://www.drupal.org/psa-2026-11-16"
verification: single-source
sourcing_note: >
  The Drupal Security Team is the disclosing party and the only source for the flaws; NCSC.ch's Security Hub restates the pre-announcement and rates exploitation unknown. The release was not published at the time of writing; the first Drupal advisory for it will carry the CVE ids, component and fixed versions.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Reserve time on the evening of 2026-11-18 (the release window is 17:00 to 21:00 UTC, 18:00 to 22:00 in Switzerland) to update every Drupal 10.6, 11.3 and 11.4 site as soon as the security release publishes, after moving each site to the latest patch release of its branch now as the Security Team recommends; plan interim mitigation for sites on end-of-life Drupal lines."
updates: []
migrated_from: null
---

The Drupal Security Team announced on 2026-11-16 that a core security release for all supported branches will ship on 2026-11-18 between 17:00 and 21:00 UTC and urges administrators to reserve time for core updates then, because exploits might be developed within hours or days ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). It rates the vulnerabilities critical, 18 of 25, with access complexity Complex, exploit status Proof of concept and target distribution Uncommon, which the Security Team defines as only uncommon module configurations being exploitable; it also says at least one can be exploited by anonymous users and that more than one configuration is affected, so sites should not assume they are safe ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). Neither the team nor any other party can release more until the announcement, so no CVE id, component or fixed version has been published ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). The affected lines are Drupal 11.4.x, 11.3.x and 10.6.x, plus the pre-releases 12.0.0-beta3 and 11.5.0-beta1; Drupal before 10.6 and Drupal 11 before 11.3 are end-of-life and are to get interim mitigation steps in the advisory ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). Sites that use Drupal Steward are already protected from known attack vectors, and other advisories released the same day may lack Steward mitigation ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). The NCSC.ch Security Hub rates exploitation unknown ([NCSC.ch, 2026-11-17](https://security-hub.ncsc.admin.ch/#/posts/13196)).

**Exposure:** any Drupal 10.6.x, 11.3.x or 11.4.x site, and every site on an end-of-life line (Drupal before 10.6 and Drupal 11 before 11.3); the PSA names no module, and although it rates only uncommon module configurations as exploitable it warns that more than one configuration is affected, so the version decides until the advisory publishes ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)).

**Defender takeaway:** update each site to the latest patch release of its branch before the window, so that other upgrade problems are settled beforehand, and apply the security release as soon as it publishes ([Drupal Security Team, 2026-11-16](https://www.drupal.org/psa-2026-11-16)). Sites on end-of-life lines apply the interim mitigation from the advisory and move to a supported branch.
