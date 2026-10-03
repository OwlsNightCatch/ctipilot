---
schema: 1
kind: threat
title: "Operation KillSwitch: Europol-coordinated takedown of the KillSec ransomware group, with Swiss fedpol and the Federal Prosecutor's Office, who have investigated its attacks on Swiss companies since 2025"
headline: "Police seize KillSec's leak site and five servers; the Swiss Federal Prosecutor has pursued the group since 2025"
summary: >
  On 2026-09-30 a German-led, Europol- and Eurojust-coordinated operation took control of the KillSec ransomware
  group's leak site and five servers, secured at least 110 TB of stolen data, made three provisional arrests and identified
  a 16-year-old as suspected main operator. fedpol and the Office of the Attorney General took part: the OAG has run
  proceedings since 2025-07-31 over KillSec attacks on several Swiss companies between October 2023 and June 2025.
discovered_at: "2026-10-02T04:48:00Z"
updated_at: null
event_date: "2026-09-30"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [ransomware, law-enforcement, organized-crime, data-breach]
regions: [switzerland, europe]
sectors: [public-sector]
entities: ["actor:killsec", "incident:operation-killswitch-killsec-takedown-2026-09"]
techniques: [T1190, T1530, T1486, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc"
    publisher: "fedpol and the Office of the Attorney General of Switzerland"
    date: "2026-10-01"
    role: primary
  - url: "https://www.presseportal.de/blaulicht/pm/6337/6363236"
    publisher: "Polizei Hamburg"
    date: "2026-10-01"
    role: primary
  - url: "https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site"
    publisher: "Europol"
    date: "2026-10-01"
    role: primary
closed_sources: []
evidence:
  - quote: "cyber-attacks carried out against several Swiss companies by the ransomware group KillSec (or “KillSecurity”) between October 2023 and June 2025"
    publisher: "fedpol and the Office of the Attorney General of Switzerland"
    source_url: "https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc"
  - quote: "The authorities were thereby able to recover at least 110 terabytes of stolen data."
    publisher: "fedpol and the Office of the Attorney General of Switzerland"
    source_url: "https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc"
  - quote: "Investigators also uncovered how the group used AI to build and maintain its ransomware infrastructure and identify potential victims."
    publisher: "Europol"
    source_url: "https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site"
verification: multi-source
sourcing_note: >
  The takedown, the counts and the Swiss proceedings come from the authorities' own releases; the figures of about
  1,000 suspected attacks and about 500 successful ones are provisional per Polizei Hamburg. No source names a Swiss
  victim or says whether any Swiss public body is among them.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

On 2026-09-30 law enforcement took control of the KillSec extortion group's leak site and secured at least 110 terabytes of stolen data in Operation KillSwitch, led by the Hamburg State Criminal Police Office and Public Prosecutor's Office and coordinated by Europol and Eurojust ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236); [fedpol and OAG, 2026-10-01](https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc)). Three suspects were provisionally arrested and eight properties searched in Greece, Romania, Spain and the United Kingdom; five servers, including the main server and several exfiltration servers, were taken over, and investigators identified a 16-year-old as suspected administrator and main operator, a developer, a negotiator and an affiliate ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236)). The authorities count about 1,000 suspected attacks worldwide, at least 70 of them in Germany, and about 500 of the 1,000 are so far identified as successful, and say the figures may change ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236)).

fedpol and the Office of the Attorney General took part as operational and strategic partners; since 2025-07-31 the OAG has run proceedings against persons unknown over KillSec's attacks on several Swiss companies between October 2023 and June 2025, and fedpol, with cantonal police and the NCSC, mapped the group's modus operandi before the action ([fedpol and OAG, 2026-10-01](https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc)). Polizei Hamburg says KillSec is said to have obtained data by exploiting software vulnerabilities and poorly secured access points to organisations' systems, in particular cloud storage, and to have copied internal data to infrastructure it controlled, listed victims on a leak site and, when a victim did not pay, could offer the files for free download; Europol adds that the group used AI to build and run its ransomware infrastructure and to identify victims ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236); [Europol, 2026-10-01](https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site)). No source names a Swiss victim, a product or a specific vulnerability, and the seized evidence may identify further victims ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236)).

**Exposure:** organizations that were extorted by KillSec or whose data appeared on its leak site, and any organization with software vulnerabilities or poorly secured access points, in particular cloud storage, the entry points Polizei Hamburg says KillSec is said to have used ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236)); the NCSC says in the release that a public entity, a business or an individual can be a target ([fedpol and OAG, 2026-10-01](https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc)).

**Detection:** the stated entry points map to external attack-surface review of internet-facing software and cloud storage access policies, and to cloud audit records showing bulk reads or copies by an unfamiliar identity.

**Defender takeaway:** a takedown does not undo a leak: data KillSec already held was exposed to publication, and the NCSC says in the release that victims are urged to report attacks to the authorities or file a complaint ([fedpol and OAG, 2026-10-01](https://www.fedpol.admin.ch/en/newnsb/cBOoSTI5a7sc)), which matters now because the seized evidence may help identify further victims ([Polizei Hamburg, 2026-10-01](https://www.presseportal.de/blaulicht/pm/6337/6363236)); organizations that dealt with a KillSec extortion since October 2023 should report it if they have not.
