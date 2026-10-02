---
schema: 1
kind: incident
title: "Belnet, the Belgian government and research network, confirms a supplier zero-day let attackers copy all incoming mail to Belnet-owned domains and the transfer links its FileSender and FedSender services sent directly for 65 days"
headline: "A national research and government network had mail to its domains copied for 65 days via an unnamed supplier's zero-day"
summary: >
  Belnet, the Belgian research and education network that also serves the Belgian government, says an attacker used a
  zero-day in technology from an external supplier to copy all incoming mail to Belnet-owned domains between 2026-07-22 and 2026-09-25, plus every download link its FileSender and FedSender transfer services generated and sent directly. The supplier, the product and the actor are not named.
discovered_at: "2026-10-02T04:46:00Z"
updated_at: null
event_date: "2026-09-24"
run_id: 2026-10-02T0404Z-intel
priority: routine
immediate_action: null
tags: [data-breach, supply-chain, zero-day]
regions: [europe]
sectors: [public-sector, education]
entities: []
techniques: [T1114]
affected_products: []
cves: []
sources:
  - url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
    publisher: "Belnet"
    date: "2026-10-01"
    role: primary
  - url: "https://news.risky.biz/risky-bulletin-sanctions-force-cas-to-revoke-tls-certs-in-iran-russia/"
    publisher: "Risky Bulletin"
    date: "2026-09-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On 24 September 2026, Belnet identified a security and privacy incident within its IT infrastructure. The incident was caused by the exploitation of a zero-day vulnerability affecting technology provided by an external supplier."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
  - quote: "During the affected period, emails were copied by the attackers and transferred to external infrastructure."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
  - quote: "At this stage, no further information is available regarding the identity or affiliation of the threat actor responsible for the incident."
    publisher: "Belnet"
    source_url: "https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure"
verification: single-source-victim
sourcing_note: >
  Every fact comes from Belnet's own incident notice (updated 2026-10-01); Risky Bulletin repeats it and adds the
  description of Belnet's customers. Belnet names no supplier, product, vulnerability class or actor.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Belnet identified the incident on 2026-09-24 and says an attacker exploited a zero-day in technology from an external supplier, remediated on 2026-09-25 ([Belnet, 2026-10-01](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)). Between 2026-07-22 and the morning of 2026-09-25, a window of 65 days, the attackers copied to external infrastructure all incoming mail to Belnet-owned domains (for example guest-roaming and BNIX addresses) and every download link its FileSender and FedSender services generated and sent directly, which could let them fetch the transferred files; password-protected or authenticated transfers are described as unreadable unless the password was written in the upload comment, and Risky Bulletin adds that mail sent to one of its customers was also stolen ([Belnet, 2026-10-01](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure); [Risky Bulletin, 2026-09-30](https://news.risky.biz/risky-bulletin-sanctions-force-cas-to-revoke-tls-certs-in-iran-russia/)).

**Exposure:** organizations that sent mail to Belnet-owned addresses or shared files through Belnet's FileSender or FedSender between 2026-07-22 and 2026-09-25, and any shared mail or file-transfer service run for government or education clients on technology from an external supplier ([Belnet, 2026-10-01](https://www.belnet.be/en/news-events/news/security-and-privacy-incident-affecting-belnets-it-infrastructure)).

**Detection:** Belnet publishes no technique or indicator and names neither the flaw nor the product, so nothing can be hunted for by name; the 65-day window shows the retention needed, since scoping an incident like this one takes mail-flow and transfer-link logs reaching back at least that far.

**Defender takeaway:** this is a Belgian incident, relevant here as the shared-service supplier-zero-day pattern, in which one exploited flaw in a mail or transfer service run for many public-sector customers exposes all of them at once; treat download links and unprotected attachments exchanged with Belnet in the window as exposed, and ask the suppliers of your own mail gateway and file-transfer services whether a zero-day of this kind touched their products.
