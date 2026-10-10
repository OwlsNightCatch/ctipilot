---
schema: 1
kind: incident
title: "FTAPI, a file-transfer vendor whose customers include authorities, confirms ransomware on an internal server; The Gentlemen list it on their leak site"
headline: "A file-transfer supplier to authorities had ransomware on one internal server; the vendor says its platform is untouched"
summary: >
  FTAPI Software of Munich, whose secure file-transfer service is used by authorities and companies, told heise that
  unauthorised parties installed ransomware on a single internal server, detected on 2026-09-14, and says its platform,
  customer systems and exchanged data were not affected. The Gentlemen ransomware group listed FTAPI on its leak site
  with a countdown that heise read as about five days on 2026-09-29.
discovered_at: "2026-10-02T04:52:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-10-02T0404Z-intel
priority: routine
immediate_action: null
tags: [ransomware, supply-chain, data-breach]
regions: [europe, dach]
sectors: [public-sector, technology]
entities: ["actor:thegentlemen", "incident:ftapi-ransomware-gentlemen-claim-2026-09"]
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html"
    publisher: "heise online"
    date: "2026-09-29"
    role: primary
  - url: "https://cybernews.com/security/ftapi-eu-data-transfer-platform-data-breach/"
    publisher: "Cybernews"
    date: "2026-09-30"
    role: corroborating
  - url: "https://www.kantonale-verwaltung.lu.ch/datenschutz"
    publisher: "Kanton Luzern (portal data-protection page)"
    date: null
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unauthorized individuals gained access to a single, locally operated internal server"
    publisher: "heise online (relaying FTAPI's statement)"
    source_url: "https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html"
  - quote: "The company emphasizes that the FTAPI platform, customer systems, and data exchanged by customers via it were not affected."
    publisher: "heise online (relaying FTAPI's statement)"
    source_url: "https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html"
verification: single-source-victim
sourcing_note: >
  The incident facts are FTAPI's own statement to heise; Cybernews repeats it. The Gentlemen's claim is a leak-site
  listing with no data shown, and FTAPI has not said how the server was reached. The Canton of Lucerne page is
  undated in its metadata and its current use of FTAPI SecuTransfer is unconfirmed.
confidence: medium
references:
  - 2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

FTAPI told heise it detected ransomware on a single internal server on 2026-09-14 and says its platform, customer systems and exchanged data were not affected, while The Gentlemen listed it on their leak site with a countdown heise read as about five days and FTAPI has not said how the server was reached ([heise online, 2026-09-29](https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html); [Cybernews, 2026-09-30](https://cybernews.com/security/ftapi-eu-data-transfer-platform-data-breach/)). The Canton of Lucerne's portal names FTAPI SecuTransfer as its secure file-transfer service and lists the notification data it collects: names, phone number, email address, company and position ([Kanton Luzern](https://www.kantonale-verwaltung.lu.ch/datenschutz)).

**Exposure:** customers of FTAPI SecuTransfer; the vendor's statement covers the platform and the exchanged data, not what the compromised internal server held.

**Defender takeaway:** ask FTAPI in writing which data categories sat on the affected server and whether any of your users' contact data was among them, and note that the leak-site countdown ran to about 2026-10-04.
