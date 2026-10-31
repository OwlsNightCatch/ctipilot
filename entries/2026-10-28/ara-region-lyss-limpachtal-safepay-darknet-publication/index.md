---
schema: 1
kind: incident
title: "ARA-Region Lyss-Limpachtal (canton Bern, communal wastewater-treatment association): SafePay has put about 49 GB into the darknet, which Risikomonitor's analysis, relayed by Inside IT, finds holds personal records, bank statements, weak passwords and a third party's monitoring credentials; the association declines to comment"
headline: "Inside IT: SafePay published about 49 GB from a Bernese wastewater association; the association declines to comment"
summary: >
  SafePay claimed an attack on the Bernese wastewater-treatment association ARA-Region Lyss-Limpachtal on 2026-09-15, and Inside IT reports of
  2026-10-27 that the group has now put about 49 GB of stolen data into the darknet. Risikomonitor's analysis, which Inside IT relays and which is
  not verified independently, finds data on more than 1,200 identifiable persons, bank statements, 255 password hits in files and a third
  party's monitoring-portal credentials stored on the association's server; the association will not comment, and no source says how the
  attackers got in.
discovered_at: "2026-10-28T03:53:00Z"
updated_at: null
event_date: "2026-10-27"
run_id: 2026-10-28T0256Z-intel
priority: routine
immediate_action: null
tags: [ransomware, data-breach]
regions: [switzerland]
sectors: [public-sector, water]
entities: ["actor:safepay", "incident:ara-region-lyss-limpachtal-ransomware-2026-09"]
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
    publisher: "Inside IT (article with Risikomonitor's analysis)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.dexpose.io/safepay-ransomware-attack-on-ara-lyss-in-switzerland/"
    publisher: "DeXpose (leak-site tracker, claim record)"
    date: "2026-09-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "SafePay has put stolen data packages from these two attacks into the darknet, about 30 gigabytes in the case of Manno, 49 gigabytes for ARA Lyss. (translated from German)"
    original: "Safepay hat erbeutete Datenpakete aus diesen beiden Angriffen ins Darknet gestellt – rund 30 Gigabyte im Fall von Manno, 49 Gigabyte der ARA Lyss."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "According to the analysis, these also contain 255 hits on passwords, 195 of them very weak. (translated from German)"
    original: "Laut Analyse enthalten diese auch 255 Treffer auf Passwörter, davon 195 sehr schwache."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "The ARA management replied to questions from inside-it.ch that it did not want to comment on the incident. (translated from German)"
    original: "Auf Fragen von inside-it.ch antwortete die ARA-Geschäftsführung, man wolle sich nicht zum Vorfall äussern."
    publisher: "Inside IT"
    source_url: "https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027"
  - quote: "The full leak will be published soon, unless a company representative contacts us via the channels provided."
    publisher: "DeXpose (leak-site tracker, claim record)"
    source_url: "https://www.dexpose.io/safepay-ransomware-attack-on-ara-lyss-in-switzerland/"
verification: single-source
sourcing_note: >
  Inside IT is the only source for the publication of the data and for its contents, which come from an analysis by the security firm
  Risikomonitor that has not been verified independently; the association has not confirmed or denied the incident. SafePay's claim of
  2026-09-15 rests on a leak-site tracker's record. No source states how the attackers got in or that data was encrypted at the association.
confidence: medium
references: ["2026-09-30/manno-ti-commune-ransomware-safepay-claim", "2026-10-21/aa26-293a-safepay-ransomware-edge-flaws-backup-nas-reset"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

The tracker DeXpose recorded on 2026-09-15 that SafePay had claimed an attack on ARA Lyss, the wastewater-treatment association at ara-lyss.ch, posting that the full leak would be published soon unless a company representative made contact ([DeXpose, 2026-09-15](https://www.dexpose.io/safepay-ransomware-attack-on-ara-lyss-in-switzerland/)). Inside IT reported on 2026-10-27 that SafePay has put the stolen data into the darknet, about 49 GB in the case of the Bernese association ARA-Region Lyss-Limpachtal, that the security firm Risikomonitor analysed it, and that the association's management declined to comment ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). Risikomonitor's analysis, relayed by Inside IT and not verified independently, finds about 3,200 e-mail addresses and data on more than 1,200 identifiable persons; user folders and a data store with content up to March 2026 that hold 255 password hits, 195 of them very weak; bank statements and a transaction list with more than 100 payments by private persons with name and address; the full login data to the monitoring portals of the photovoltaic plants of another company's customers, stored on the same server; and a 2015 applicant list with birth dates, civil status, former employer and interview notes that was never deleted ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)).

BACS told Inside IT that SafePay, which relies on double extortion, is among the more active ransomware groups in Switzerland and, together with The Gentlemen, the third most active in 2026 after Akira and Payload, that it has no clear focus on Switzerland, and that it was first observed there in May 2025 ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)). No source says how the attackers got in or that data was encrypted at the association.

**Defender takeaway:** a communal body or association should look for credentials, bank statements and applicant files on its own file servers before an attacker does: Risikomonitor found 255 password hits in files, another company's portal logins and a 2015 applicant list that had never been deleted, and those are what a published dump gives fraudsters ([Inside IT, 2026-10-27](https://www.inside-it.ch/kritische-schweizer-infrastrukturen-attackiert-20261027)).
