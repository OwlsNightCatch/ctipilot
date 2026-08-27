---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "European government's own operating infrastructure was the target this week — a federal document platform, a national beneficial-ownership register, a state treasury and a heat plant, with two of the entry points on no internet-facing asset inventory"
headline: "European public bodies in five jurisdictions compromised in one week, and two of the entry points were on no asset inventory"
summary: >
  Between 3 and 9 August 2026 the Swiss Confederation's own IT provider, a Swiss canton, Liechtenstein's
  beneficial-ownership register, Hungary's State Treasury and a Polish combined heat and power plant all
  disclosed compromises, and a Flemish Government agency confirmed a North Korean intrusion on one of its workstations.
  What was taken was not customer data but the state's own operating machinery — an authoritative identity
  dataset, domain-administrator rights across a payments agency, turbine controls. Two of the disclosed entry
  points appear on no internet-facing asset inventory: a mobile carrier's private APN, with a controller
  answering on factory credentials on its WAN side, and an Oracle WebLogic server whose last patches date to
  a 2017 cycle.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-08"
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags: [data-breach, ot-ics, nation-state, vulnerabilities, actively-exploited]
regions: [switzerland, europe, dach]
sectors: [public-sector, energy, finance]
entities:
  - incident:foitt-bit-sharepoint-breach-2026-07
  - incident:graubuenden-canton-sharepoint-breach-2026-08
  - incident:liechtenstein-vwbp-register-breach-2026-07
  - incident:hungary-treasury-mvh-bytetobreach-2026-08
  - incident:poland-energy-grid-attack-2025-12-29
  - incident:nk-contagious-interview-flemish-government-2026-08
  - actor:bytetobreach
techniques: [T1190, T1078, T1078.001, T1133, T1199, T1213, T1572]
affected_products: ["Microsoft SharePoint Server", "Oracle WebLogic Server"]
cves: []
sources:
  - url: "https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL"
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
    date: "2026-08-04"
    role: primary
  - url: "https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx"
    publisher: "Kanton Graubünden — Standeskanzlei"
    date: "2026-08-05"
    role: primary
  - url: "https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden"
    publisher: "persoenlich.com (Keystone-SDA)"
    date: "2026-08-05"
    role: corroborating
  - url: "https://www.presseportal.ch/de/pm/100000148/100941487"
    publisher: "Regierung des Fürstentums Liechtenstein"
    date: "2026-08-02"
    role: primary
  - url: "https://www.presseportal.ch/de/pm/100000148/100941523"
    publisher: "Regierung des Fürstentums Liechtenstein"
    date: "2026-08-04"
    role: primary
  - url: "https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/"
    publisher: "CERT Polska (NASK)"
    date: "2026-08-08"
    role: primary
  - url: "https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf"
    publisher: "CERT Polska (NASK) — incident follow-up report"
    date: "2026-08-08"
    role: primary
  - url: "https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach"
    publisher: "Telex.hu"
    date: "2026-08-03"
    role: corroborating
  - url: "https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/"
    publisher: "WIRED"
    date: "2026-08-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Im Rahmen der Analyse des Vorfalls wurde festgestellt, dass rund 200 Konten kompromittiert wurden."
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
  - quote: "Dabei wurden Datenkopien von rund 31'000 Rechtsträgern widerrechtlich abgegriffen."
    publisher: "Regierung des Fürstentums Liechtenstein"
  - quote: "To the best of our knowledge, the use of a private APN to gain access to the OT network was the first instance of this attack vector being observed in a real-world cyberattack."
    publisher: "CERT Polska (NASK)"
  - quote: "Surveys conducted among organizations using similar solutions indicated that this configuration was commonly encountered in Poland."
    publisher: "CERT Polska (NASK)"
verification: multi-source
sourcing_note: >
  Each incident rests on its own disclosing authority's statement — the Swiss Confederation, the Canton of
  Graubünden, the Government of Liechtenstein and CERT Polska are first-party authorities for their own
  jurisdictions. The Hungarian Treasury intrusion is carried by Telex.hu reporting on attacker-leaked
  material and expert assessment, not by a victim statement, and is presented as such.
confidence: high
update_of: null
references:
  - 2026-08-05/bit-foitt-swiss-federal-sharepoint-breach-200-accounts
  - 2026-08-06/canton-graubuenden-sharepoint-server-breach
  - 2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach
  - 2026-08-05/hungary-state-treasury-mvh-bytetobreach-weblogic
  - 2026-08-09/cert-polska-private-apn-pivot-into-ot-chp-plant-shutdown
  - 2026-08-08/dprk-contagious-interview-blast-radius-flemish-government
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** peer institutions in five European jurisdictions disclosed compromises of the machinery they run the state with — and in two of them the way in was connectivity and legacy infrastructure that appears on no internet-facing asset inventory.

Switzerland took two of them in 48 hours, at both levels of government. The Bundesamt für Informatik und Telekommunikation, which operates the Confederation's own data centres, disclosed on 4 August that its on-premises SharePoint Servers were compromised and that "rund 200 Konten kompromittiert wurden" — user accounts and technical service accounts alike ([Der Bundesrat / BIT, 2026-08-04](https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL)). The detail that matters for anyone still running on-premises SharePoint is the timing: BIT had begun installing the July updates immediately on release, and staff spotted the anomalies on 28 July while that work was in progress, so the servers are being rebuilt from scratch rather than patched in place. One day later the Canton of Graubünden's IT office reported a compromise of a SharePoint server hosting the cantonal administration's public web presence, reporting on first analysis no accounts compromised and no data exfiltrated ([Kanton Graubünden, 2026-08-05](https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx)); Keystone-SDA reporting adds that two files were placed on the server and their code was not executed ([persoenlich.com, 2026-08-05](https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden)). Neither Swiss disclosure names a CVE, which is why an estate-wide compromise assessment keyed on the July SharePoint exploitation window — not a CVE-scoped patch check — is the operation this pair calls for.

Two further disclosures show the objective shifting from the citizen's data to the state's own authoritative record. Liechtenstein's Amt für Justiz lost copies of the beneficial-ownership register: "Datenkopien von rund 31'000 Rechtsträgern widerrechtlich abgegriffen" ([Regierung des Fürstentums Liechtenstein, 2026-08-02](https://www.presseportal.ch/de/pm/100000148/100941487)), and the government's follow-up media conference published the exact field set — legal-entity name plus surname, first name, date of birth, nationality and country of residence, with no address, telephone number or financial data recorded ([Regierung des Fürstentums Liechtenstein, 2026-08-04](https://www.presseportal.ch/de/pm/100000148/100941523)). That composition is the point: what was taken is an identity-verification kit tied to the natural persons behind Swiss- and EU-administered structures, not a marketing list. In Hungary, Telex.hu reports that the Magyar Államkincstár's Agricultural and Rural Development Office was breached in late July by ByteToBreach — the actor already tracked here for the attack on Romania's national land registry — with experts consulted on attacker-leaked screenshots assessing entry through an Oracle WebLogic server whose fixes date to an October 2017 patch cycle, escalating to Windows domain-administrator rights ([Telex.hu, 2026-08-03](https://telex.hu/techtud/2026/08/03/magyar-allamkincstar-nki-kiberbiztonsag-kibertamadas-naih-bytetobreach)).

The week's most consequential access path was published on its last day. CERT Polska's follow-up forensic report on the 29 December 2025 attacks on Poland's energy sector discloses a second, previously unnamed victim — a combined heat and power plant supplying about 50,000 residents, where three Siemens PLCs were switched to STOP mode and password-locked, shutting down a steam turbine and the process-water treatment system. The attacker reached it from an already-compromised wind-farm substation by tunnelling over SSH through a cellular router into the distribution system operator's private APN, a mobile network shared by both sites, and then into a WAGO PFC200 controller whose WAN-side web interface answered on factory credentials ([CERT Polska incident follow-up report, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). CERT Polska states that "the use of a private APN to gain access to the OT network was the first instance of this attack vector being observed in a real-world cyberattack," and — the sentence European operators should act on — that surveys of organisations using similar solutions "indicated that this configuration was commonly encountered in Poland" ([CERT Polska, 2026-08-08](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/)). Belgium supplies the fifth shape: Digitaal Vlaanderen confirmed to WIRED that Belgium's Centre for Cybersecurity notified it on 3 March 2026 of a North Korean compromise, that the affected workstation was isolated and exposed credentials rotated, and that the incident is contained — one organisation inside a victim set the researcher built from nearly two years of access to the actors' own servers ([WIRED, 2026-08-05](https://www.wired.com/story/a-security-pro-hacked-north-korean-hackers-he-found-theyd-breached-hundreds-of-networks-worldwide/)).

**Defender takeaway:** the common property across the Polish and Hungarian cases is that the entry point was not on anyone's list of internet-facing assets — a carrier-provided private APN treated as a private network, and a legacy application server nine years behind its patch cycle. An exposure review scoped to "what answers on our public IP ranges" would have missed both. The Swiss pair adds the complementary lesson that being mid-patch is not the same as being patched: both estates were inside a known exploitation window when the intrusions happened, so the artefact hunt matters more than the version string.

**Triage:** a compromised administrative estate of this kind produces telemetry that reads as ordinary operations, so the discriminators are relational rather than atomic. For the SharePoint cases, look for web-application process trees spawning script interpreters and for service-account authentication from hosts those accounts never normally touch — a service account is defined by its narrow, repetitive access pattern, and the deviation is the signal. For the OT path, the discriminator is direction and origin: an inbound management session to a field controller arriving from a peer device inside the carrier APN rather than from the operator's own engineering workstation subnet, and a controller-mode change (run to STOP) with no corresponding change-management window. Legitimate remote maintenance produces the same protocol events; it does not normally originate from another site's equipment.
