---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: Looking ahead — 2026-W26
headline: Looking ahead — 2026-W26
summary: "ShinyHunters PeopleSoft notifications are still landing — expect more named European education and public-finance victims. GTIG has notified ~100 organisations (68% higher education) and NAIC is the fresh high-profile case; patch internet-reachable PeopleSoft and hunt /PSEMHUB/ and /PSIGW/HttpListeningConnector."
discovered_at: "2026-06-29T00:21:26Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: notable
immediate_action: null
tags:
  - cloud
regions:
  - global
sectors: []
entities:
  - "campaign:icarus-klue-salesforce-oauth"
  - "actor:shinyhunters"
  - "incident:fortibleed-fortigate-credential-exposure"
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit"
    publisher: Google GTIG
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-of-credential-exposure"
    publisher: CISA
    role: corroborating
  - url: "https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/"
    publisher: SecurityWeek
    role: corroborating
  - url: "https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp"
    publisher: ENISA SRP
    role: corroborating
  - url: "https://www.edpb.europa.eu/news/edpb-meets-with-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification-template_en"
    publisher: EDPB
    role: corroborating
  - url: "https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem"
    publisher: Socket
    role: corroborating
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0210.html"
    publisher: NCSC-NL
    role: corroborating
  - url: "https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted"
    publisher: UK NCA
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W26.md
---

A focused, justified list — items already in motion, not predictions.

- **ShinyHunters PeopleSoft notifications are still landing — expect more named European education and public-finance victims.** GTIG has notified ~100 organisations (68% higher education) and NAIC is the fresh high-profile case; patch internet-reachable PeopleSoft and hunt `/PSEMHUB/` and `/PSIGW/HttpListeningConnector`. ([Google GTIG](https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit); [daily 06-28](/briefs/2026-06-28/))
- **FortiBleed is not a one-and-done credential reset — full AD domain takeover is now confirmed at a NATO-aligned contractor.** Finish session termination and credential rotation, then hunt for post-compromise AD persistence (Kerberos abuse, DCSync, DFS-backup exfiltration) rather than assuming the reset closed it. ([CISA](https://www.cisa.gov/news-events/alerts/2026/06/18/cisa-urges-hardening-fortinet-devices-after-reports-of-credential-exposure); [daily 06-24](/briefs/2026-06-24/))
- **The Klue/Icarus extortion surface is multiplying after the "resolution" — a second group is now extorting ~195 listed organisations.** Any firm with a Klue/Salesforce integration should expect renewed extortion contact regardless of Icarus's stated data deletion; complete OAuth-grant revocation and CRM-egress monitoring. ([SecurityWeek](https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/); [daily 06-27](/briefs/2026-06-27/))
- **CRA Single Reporting Platform go-live is ~75 days out (11 September); ENISA's dry-run schedule is due now.** In-scope manufacturers — including Swiss exporters to the EU — should register and wire the 24/72-hour reporting flow into their PSIRT process before the obligation binds. ([ENISA SRP](https://www.enisa.europa.eu/topics/product-security-and-certification/single-reporting-platform-srp))
- **EDPB Article 33 harmonised breach-notification template consultation closes 5 August.** Still open with no in-window change; multi-jurisdiction breach-response owners have a closing window to comment before the EDPB sets a mandatory-adoption timeline. ([EDPB](https://www.edpb.europa.eu/news/edpb-meets-with-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification-template_en))
- **npm v12 will disable install scripts by default — the week's Miasma worm wave is the reminder to audit CI now.** Miasma's `postinstall`-and-`SessionStart`-hook propagation is exactly the kill chain `--ignore-scripts` / npm v12 defaults neutralise; inventory pipelines and AI-coding-tool hook configs that rely on build scripts. ([Socket](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem); [daily 06-27](/briefs/2026-06-27/))
- **libssh2 CVE-2026-55200 has a public PoC and an upstream fix commit, but tagged releases lag across the binding ecosystem — track the embedded-dependency fix pipeline.** Inventory appliances, tooling and language bindings that ship libssh2 and chase each vendor's release rather than assuming a single library bump closes it. ([NCSC-NL](https://advisories.ncsc.nl/2026/ncsc-2026-0210.html); [daily 06-28](/briefs/2026-06-28/))
- **Scattered Spider TfL sentencing is set for 16 July.** First UK court outcome on the campaign; the vishing/social-engineering TTP precedent is directly relevant to European transport and public-sector identity-desk hardening. ([UK NCA](https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted); [daily 06-23](/briefs/2026-06-23/))
