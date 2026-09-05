---
schema: 1
kind: incident
title: "Thomson Reuters' C-Track court case-management platform breach reaches at least 13 US states, the US Virgin Islands and three Ontario courts"
headline: "A court case-management SaaS vendor held undisclosed backup copies of sealed court data outside the courts' own visibility or control"
summary: >
  Thomson Reuters' West Publishing subsidiary disclosed on 2026-09-02 that an unauthorized party
  accessed its C-Track court case-management platform between March and 30 June 2026, exposing
  records — some sealed or confidential — tied to appellate courts in at least 13 US states plus the
  US Virgin Islands and three Ontario courts. No party has named an access vector or attacker identity;
  the exposure was architecturally inconsistent, with some courts' data held in an undisclosed backup
  copy and Ohio's accessed on its live production platform.
discovered_at: "2026-09-05T04:45:00Z"
updated_at: null
event_date: "2026-09-02"
run_id: 2026-09-05T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, cloud]
regions: [us, global]
sectors: [public-sector]
entities: ["incident:thomson-reuters-ctrack-court-breach-2026-09"]
techniques: [T1530]
affected_products: ["Thomson Reuters C-Track"]
cves: []
sources:
  - url: "https://www.ctracknotification.com/"
    publisher: "C-Track / West Publishing Corporation (Thomson Reuters)"
    date: "2026-09-02"
    role: primary
  - url: "https://www.ctracknotification.ca/"
    publisher: "C-Track Canada (Thomson Reuters Canada Limited)"
    date: "2026-09-02"
    role: primary
  - url: "https://www.ontariocourts.ca/en/public-statement-cybersecurity.htm"
    publisher: "Chief Justices of Ontario's Court of Appeal, Superior Court of Justice and Court of Justice"
    date: "2026-09-02"
    role: primary
  - url: "https://therecord.media/thomson-reuters-cyberattack-data"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-03"
    role: corroborating
  - url: "https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm"
    publisher: "Tech Times"
    date: "2026-09-04"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html"
    publisher: "The Hacker News"
    date: "2026-09-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Certain confidential, redacted or sealed information may have been impacted for certain affected courts."
    publisher: "C-Track / West Publishing Corporation (Thomson Reuters)"
  - quote: "Thomson Reuters has not said how the attacker gained access, who was responsible or how much data was taken."
    publisher: "The Record (Recorded Future News)"
  - quote: "in a backup file within the company's cloud environment"
    publisher: "West Publishing, quoted by Tech Times (Alabama Appellate Courts' account)"
  - quote: "neither requested nor known about"
    publisher: "Alabama Chief Justice Sarah Stewart, quoted by Tech Times"
  - quote: "the unauthorized access took place on the Court's production platform"
    publisher: "Thomson Reuters Court Management Solutions, quoted by Tech Times (statement to the Ohio Supreme Court)"
  - quote: "deeply troubled that our court users' data has been compromised"
    publisher: "Minnesota Supreme Court Chief Justice Natalie Hudson, quoted by The Hacker News"
verification: multi-source
sourcing_note: >
  No Swiss or home-region nexus and no confirmed initial-access vector or attacker identity from any
  party as of 2026-09-04. Included under the breach/incident inclusion gate on ground (a), scale: the
  compromise reaches sealed and confidential judicial records across court systems in two sovereign
  jurisdictions — at least 13 US states plus the US Virgin Islands, and three Ontario, Canada courts —
  a genuinely large, multi-jurisdictional footprint from a single vendor compromise, distinct from a
  single-country, single-organization breach. No new or evolved TTP is asserted (no access vector is
  stated at all, so ground (b) does not apply here), no actor is named, and no imminent shared threat
  is stated; the entry rests on ground (a) alone. `techniques[]` is limited to T1530 because that is
  the only behavior any source states; no initial-access technique is asserted by any party.
confidence: medium
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

Thomson Reuters' West Publishing subsidiary disclosed on 2026-09-02 that an unauthorized party obtained files from C-Track, its court case-management SaaS platform, in March 2026, discovered on 30 June 2026 ([C-Track official notice, 2026-09-02](https://www.ctracknotification.com/)). Public disclosure did not follow until 64 days after that detection date; Thomson Reuters separately advised Ontario's Ministry of the Attorney General of the Ontario courts' exposure on 23 July 2026, itself 23 days after detection and still six weeks before any public notice ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm); [Ontario Courts, 2026-09-02](https://www.ontariocourts.ca/en/public-statement-cybersecurity.htm)). West Publishing's notice ([C-Track official notice, 2026-09-02](https://www.ctracknotification.com/)) names 24 affected court bodies: appellate courts in Alabama, Kentucky, Montana, Nevada, New Hampshire, North Dakota, Ohio (ten of twelve appellate districts, per [Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)), Pennsylvania (several county-level courts plus one former client), South Carolina, Tennessee, Wyoming and the U.S. Virgin Islands Supreme and Superior Courts, plus three Ontario courts — the Court of Appeal, Superior Court of Justice and Court of Justice — disclosed in a parallel notice by their Chief Justices ([Ontario Courts, 2026-09-02](https://www.ontariocourts.ca/en/public-statement-cybersecurity.htm)). Neither Minnesota nor Oregon appears in West Publishing's own list above; both states' courts disclosed the exposure independently, bringing the count to at least 13 US states. Minnesota's Judicial Branch disclosed independently that its appellate courts were affected — a gap the company has not publicly explained ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)). Oregon's Judicial Department likewise disclosed its appellate courts were affected, and Oregon's Chief Justice Meagan Flynn called the incident unacceptable and demanded full accountability from Thomson Reuters ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)). Potentially exposed data includes names, Social Security numbers, driver's license numbers, dates of birth, and medical and health-insurance information; the company states certain confidential, redacted or sealed information may have been impacted for certain affected courts. The exposure's scope varies further by jurisdiction: Nevada officials said the type of data involved differs court by court and cautioned against assuming what was exposed in one state was exposed in another, while Montana officials said most of their affected information already appeared to be publicly available, though some driver's license numbers and dates of birth were also involved ([The Record, 2026-09-03](https://therecord.media/thomson-reuters-cyberattack-data)). As of 2026-09-04, no party — Thomson Reuters, law enforcement, or any affected court — had published the method by which the files were obtained or the identity of whoever was responsible ([The Hacker News, 2026-09-04](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)); The Record separately confirms Thomson Reuters itself has not said how the attacker gained access ([The Record, 2026-09-03](https://therecord.media/thomson-reuters-cyberattack-data)).

Individual court statements reveal the exposure was architecturally inconsistent across jurisdictions: West Publishing told Alabama's Appellate Courts that their data existed as a copy held "in a backup file within the company's cloud environment," which Alabama's Chief Justice said her courts had "neither requested nor known about"; Montana's court reported the same backup/troubleshooting-copy pattern, stating the material taken was drawn from database copies "supplied to TR for the purpose of troubleshooting the applications" ([The Hacker News, 2026-09-04](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)). Montana and Minnesota each stated that court documents specifically were not part of the accessed data ([The Hacker News, 2026-09-04](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)), though West Publishing's own notice states sealed material may have been affected for certain courts. The Supreme Court of Ohio, by contrast, was told by Thomson Reuters Court Management Solutions that "the unauthorized access took place on the Court's production platform" — the live system hosting current filing data for its ten affected appellate districts, not a backup ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)). Minnesota responded by terminating Thomson Reuters' access to its court systems outright and forcing a password reset for all C-Track users; North Dakota confirmed an active criminal investigation ([The Hacker News, 2026-09-04](https://thehackernews.com/2026/09/thomson-reuters-court-software-breach.html)). Thomson Reuters is offering 12 months of Experian credit monitoring to affected US individuals ([C-Track official notice, 2026-09-02](https://www.ctracknotification.com/)) and a parallel 12-month TransUnion Canada myTrueIdentity membership to affected Canadian individuals ([C-Track Canada notice, 2026-09-02](https://www.ctracknotification.ca/)), and states C-Track remains fully operational, though Ohio's court says it has not yet received details of the security measures the vendor told it had been deployed ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)).

This is not the first time Thomson Reuters has accumulated personal data beyond what affected individuals authorized: in February 2025 a federal judge granted final approval to a $27.5 million class-action settlement over the company's CLEAR platform, which had collected identifying data on roughly 40 million Californians and sold access to it as a law-enforcement and investigative tool without subject consent ([Tech Times, 2026-09-04](https://www.techtimes.com/articles/326594/20260904/sealed-court-records-breached-when-thomson-reuters-lost-control-its-cloud.htm)). The mechanism differs — backup copies from routine SaaS operations here, deliberate data aggregation there — but both cases show data accumulating in Thomson Reuters' systems beyond what the affected individuals knew about or authorized.

**Defender takeaway:** the operationally significant fact here is not the still-unnamed intrusion technique but the governance gap it exposed — a case-management SaaS vendor held copies of court data, in some jurisdictions on production systems and in others in undisclosed backups, that the courts themselves had neither requested nor could see. Any public-sector body outsourcing case management, records or filing systems to a third-party platform should confirm, in the vendor contract itself, exactly which environments its data is replicated into, whether backup or troubleshooting copies exist outside the primary system, and whether the vendor is obligated to disclose their existence and location before an incident forces the question.
