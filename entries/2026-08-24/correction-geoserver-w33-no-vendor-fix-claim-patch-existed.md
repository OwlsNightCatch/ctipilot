---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: null
title: "CORRECTION — the 2026-W33 weekly told readers GeoServer's exploited SQL injection had no vendor fix and that taking endpoints off the internet was the whole remediation; the fix had shipped two days earlier"
headline: "A patch existed when the weekly said none did, so the remediation it published was the wrong one"
summary: >
  Three 2026-W33 weekly entries published 2026-08-16T23:5xZ stated that the actively exploited
  jsonArrayContains SQL injection in GeoServer had no CVE and no vendor patch, and one of them told
  readers that removing query endpoints from the public internet was the whole remediation. OSGeo had
  released GeoServer 3.0.1, 2.28.5 and 2.27.6 on 2026-08-14 — two days before those entries published —
  carrying the GeoTools 35.1, 34.5 and 33.6 fixes for exactly this flaw. The flaw now also has an
  identifier, CVE-2026-76904, assigned when the advisory published on 2026-08-21. The correct remediation
  is and was to upgrade. The pipeline's own operational coverage caught up on 2026-08-18, but the weekly
  entries are immutable and still carry the wrong instruction, which is what this entry exists to fix.
discovered_at: "2026-08-24T10:00:00Z"
event_date: "2026-08-14"
run_id: 2026-08-24T0902Z-audit
priority: high
immediate_action: null
tags: [vulnerabilities, sqli, pre-auth, actively-exploited, patch-available]
regions: [europe, global]
sectors: [public-sector, energy, water, transport]
entities: []
techniques: [T1190]
affected_products: ["GeoServer", "GeoTools"]
cves:
  - id: CVE-2026-76904
    cvss: "9.8"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "GeoTools gt-jdbc-postgis from 35.0 before 35.1, from 34.0 before 34.5, and from 30.5 before 33.6 — shipped in GeoServer before 3.0.1, 2.28.5 and 2.27.6 respectively"
    fixed: "GeoServer 3.0.1, 2.28.5, 2.27.6 (released 2026-08-14), carrying GeoTools 35.1, 34.5 and 33.6"
sources:
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
    publisher: "GeoServer project (OSGeo)"
    date: "2026-08-14"
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-28-5-released.html"
    publisher: "GeoServer project (OSGeo)"
    date: "2026-08-14"
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-27-6-released.html"
    publisher: "GeoServer project (OSGeo)"
    date: "2026-08-14"
    role: primary
  - url: "https://api.osv.dev/v1/vulns/GHSA-mqjf-5f49-2fjh"
    publisher: "OSV (mirroring the GeoTools GitHub Security Advisory)"
    date: "2026-08-21"
    role: primary
evidence:
  - quote: "GeoServer 3.0.1 is made in conjunction with GeoTools 35.1, and GeoWebCache 2.0.1."
    publisher: "GeoServer project (OSGeo)"
    url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
verification: multi-source
sourcing_note: >
  All four sources were fetched in this run. The vendor's three separate release announcements are each the authority
  for their own release date and paired GeoTools version — the 3.0.1 announcement carries only 3.0.1's,
  which is why all three are cited rather than one standing in for the set; the advisory's structured record is the authority for the
  identifier and the three affected-and-fixed ranges. Those ranges are worth stating from the structured
  data specifically, because the advisory's own prose patch summary lists a different and incorrect set of
  GeoTools versions than its own machine-readable ranges and its linked release tags — so a reader who
  takes the prose at face value patches to versions that do not exist as fixes. cves[].cvss carries 9.8, taken from the
  CVSS 3.1 vector the cited advisory record itself publishes (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H) rather
  than from any aggregator: an unauthenticated, low-complexity, no-interaction path to full confidentiality,
  integrity and availability impact. The `exploited` status is not asserted by any of the four sources cited
  here — the three release announcements call the update urgent and note prior public disclosure, and the
  advisory record carries no exploitation field. It is carried forward from the referenced 2026-08-18 entry,
  whose Swiss national-advisory source records the flaw as actively exploited with a public proof of concept;
  this entry corrects the patch claim, not the exploitation one.
confidence: high
update_of: 2026-08-16/weekly-w33-vuln-status-rollup
references:
  - 2026-08-16/weekly-w33-looking-ahead
  - 2026-08-16/weekly-w33-disclosure-to-exploitation-interval-collapsed
  - 2026-08-18/geoserver-jsonarraycontains-patched-wfs10-stacked-copy
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
classification:
  reliability: A
  credibility: 1
actions:
  - "If a GeoServer estate was triaged off the 2026-W33 weekly, re-triage it: upgrade to GeoServer 3.0.1, 2.28.5 or 2.27.6 on the matching branch rather than relying on network isolation, and disregard any internal note recording this flaw as having no vendor fix."
---

**UPDATE (originally covered 2026-08-16):** the correction is to a remediation instruction, so it is worth stating before the reasoning. GeoServer's actively exploited `jsonArrayContains` SQL injection had a vendor fix at the time the 2026-W33 weekly published, and the weekly said it did not.

OSGeo released three versions on 2026-08-14, each announced separately and each paired with the GeoTools release carrying the fix: 3.0.1, which "is made in conjunction with GeoTools 35.1, and GeoWebCache 2.0.1" ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html)); 2.28.5, made in conjunction with GeoTools 34.5 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-28-5-released.html)); and 2.27.6, made in conjunction with GeoTools 33.6 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-27-6-released.html)). The advisory's structured record gives the three fixed ranges precisely: the `org.geotools.jdbc:gt-jdbc-postgis` module is affected from 35.0 before 35.1, from 34.0 before 34.5, and from 30.5 before 33.6, and the flaw now carries the identifier CVE-2026-76904, assigned when the advisory published on 2026-08-21 ([OSV, 2026-08-21](https://api.osv.dev/v1/vulns/GHSA-mqjf-5f49-2fjh)). Three W33 entries — the vulnerability status roll-up, the outlook, and the disclosure-to-exploitation piece — each recorded the flaw as having no CVE and no vendor patch, and the outlook went further, telling readers that until OSGeo shipped something, taking query endpoints off the public internet was the remediation.

Two things went wrong, and only one of them is about GeoServer. The reporting the weekly relied on was a 2026-08-14 news article headlined around an unpatched zero-day, published the same day as the vendor's release and therefore already stale as it went out; and the national advisory the weekly also cited did not append the fixed-version links until 2026-08-17, the day after the weekly. So both of the weekly's sources said "no patch" while the vendor's own release channel said otherwise. Nobody checked the release channel. A claim that no fix exists is a negative claim with an expiry date, and the only source that can carry it is the party that would ship the fix.

There is a second, still-live trap in the advisory itself: its human-readable patch summary names a different set of GeoTools versions than its own structured ranges and its linked release tags. A defender following the prose upgrades to versions that are not the fixes. Take the versions from the vendor's release announcements or the advisory's machine-readable ranges, both cited above.

**Defender takeaway:** if this flaw was triaged off the W33 weekly, the estate was probably given a network-isolation instruction when an upgrade was available, and the isolation may since have been relaxed on the belief that nothing more could be done. Re-triage on version numbers. More generally, the store's operational coverage corrected itself on 2026-08-18 and the strategic surface did not, so a reader who works from the weekly and a reader who works from the daily entries were told different things for a week — when a status roll-up and a later operational entry disagree, the more recent entry and the vendor's own release page win.
