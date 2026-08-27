---
schema: 1
kind: incident
horizon: operational
title: "Klue OAuth-token breach — victim list grows, CRM-API abuse chain detailed"
headline: "Klue OAuth-token breach — victim list grows, CRM-API abuse chain detailed"
summary: >
  UPDATE (originally covered 2026-06-19): The Klue compromise first covered on 2026-06-19 (Icarus
  obtaining a legacy Klue credential) now has a named, growing victim list and a documented
  post-access technique.
discovered_at: "2026-06-21T04:55:03Z"
updated_at: "2026-06-27T05:17:49Z"
event_date: 2026-06-19
run_id: 2026-06-21-2b75e32c
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - cloud
  - organized-crime
  - supply-chain
regions:
  - global
  - us
  - europe
sectors:
  - technology
  - telco
  - finance
entities:
  - "campaign:icarus-klue-salesforce-oauth"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://klue.com/blog/an-update-on-recent-klue-security-incident"
    publisher: Klue
    role: primary
  - url: "https://www.huntress.com/blog/klue-breach-investigation"
    publisher: Huntress
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/klue-oauth-breach-victim-list-grows-as-icarus-hackers-claim-attack/"
    publisher: BleepingComputer
    role: corroborating
  - url: "https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm"
    publisher: SEC EDGAR — 8x8 Inc Form 8-K Item 1.05
    role: primary
  - url: "https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/"
    publisher: SecurityWeek
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://thehackernews.com/2026/06/salesforce-disables-klue-app.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/"
    publisher: SecurityWeek
    role: primary
  - url: "https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/"
    publisher: TechCrunch
    role: corroborating
closed_sources: []
evidence:
  - quote: BeyondTrust also said business contact and sales-related information was stolen from its Salesforce instance
    publisher: SecurityWeek
  - quote: "an unauthorized actor was able to obtain OAuth tokens Klue held for many of its customers, including LastPass"
    publisher: Help Net Security citing LastPass
verification: multi-source
sourcing_note: null
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-06-23T04:52:51Z"
    run_id: 2026-06-23-165387f6
    type: update
    summary: >
      UPDATE (originally covered 2026-06-21): At least nine Klue customers have now publicly confirmed
      Salesforce-CRM data impact from the 11–12 June Icarus intrusion: HackerOne, Huntress, Jamf,
      OneTrust, Recorded Future, Snyk, Tanium, Insurity and Sprout Social (SecurityWeek, 2026-06-22).
    fields:
      - regions
      - sources
      - tags
      - body
    merged_from: 2026-06-23/klue-icarus-oauth-token-breach-named-victim-list-expands-to
  - at: "2026-06-24T05:11:56Z"
    run_id: 2026-06-24-de656486
    type: update
    summary: >
      UPDATE (originally covered 2026-06-19; campaign delta 2026-06-23): US cloud-communications
      provider 8x8 (NASDAQ: EGHT) filed a Form 8-K Item 1.05 on 2026-06-23 disclosing that an
      unauthorised party accessed its Salesforce environment on 2026-06-11/12 via a **third-party
      integration — the Klue …
    fields:
      - entities
      - sectors
      - sources
      - body
    merged_from: 2026-06-24/8x8-confirms-klue-icarus-salesforce-exfiltration-in-an-sec-8
  - at: "2026-06-25T04:59:09Z"
    run_id: 2026-06-25-da7fbd23
    type: update
    summary: >
      UPDATE (originally covered 2026-06-19): BeyondTrust and LastPass have both disclosed that
      business-contact and sales-related data was exfiltrated from their Salesforce environments via
      the compromised Klue integration, pushing the confirmed named-victim count past 14
      (SecurityWeek, 2026-06-24 · Help Net Security …
    fields:
      - evidence
      - sectors
      - sources
      - body
    merged_from: 2026-06-25/klue-icarus-salesforce-oauth-breach-beyondtrust-and-lastpass
  - at: "2026-06-27T05:17:49Z"
    run_id: 2026-06-27-40e791d4
    type: update
    summary: >
      Klue/Icarus Salesforce breach widens to ~24 firms — newly named EU victims include Germany's
      Lucanet and Link11; the attacker was itself hacked and a second extortion actor has emerged
      (SecurityWeek, 2026-06-26).
    fields:
      - priority
      - sources
      - body
    merged_from: 2026-06-27/klue-icarus-salesforce-breach-widens-to-24-firms-the-attacke
migrated_from: briefs/2026-06-21.md
---

**UPDATE (originally covered 2026-06-19):** The Klue compromise first covered on 2026-06-19 (Icarus obtaining a legacy Klue credential) now has a named, growing victim list and a documented post-access technique. Klue confirms the attacker harvested customer-provisioned OAuth tokens for connected platforms — principally Salesforce, plus Gong, HubSpot, SharePoint and others — and used them to query customer CRM instances directly ([Klue, 2026-06-19](https://klue.com/blog/an-update-on-recent-klue-security-incident)).

Huntress forensics show the stolen tokens were used to hit Salesforce REST endpoints at `/services/data/v59.0/query/<STRING>` with a `python-urllib` User-Agent — anomalous in a legitimate Klue-integration context ([Huntress, 2026-06-18](https://www.huntress.com/blog/klue-breach-investigation)). Confirmed affected organisations now include Huntress, Recorded Future, Tanium, Jamf and Sprout Social; Icarus has publicly claimed the attack and is demanding contact via Session messenger ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/klue-oauth-breach-victim-list-grows-as-icarus-hackers-claim-attack/)). The chain — compromise an integration platform's legacy credential, harvest downstream OAuth tokens, query customer CRM APIs from the platform's legitimate IP range — bypasses perimeter controls. Detection surface: Salesforce Event Monitoring for a `python-urllib` API caller, unusual `/services/data/v*/query/` volumes from non-user principals, and out-of-hours API sessions from unexpected source orgs. Hardening: audit and revoke OAuth grants to third-party SaaS vendors (especially inactive integrations), enforce IP restrictions on Salesforce connected-app policies, and scope integration-platform credentials so one compromised account cannot chain to every downstream tenant.

## Update — 2026-06-23T04:52:51Z

At least nine Klue customers have now publicly confirmed Salesforce-CRM data impact from the 11–12 June Icarus intrusion: HackerOne, Huntress, Jamf, OneTrust, Recorded Future, Snyk, Tanium, Insurity and Sprout Social ([SecurityWeek, 2026-06-22](https://www.securityweek.com/more-cybersecurity-firms-disclose-impact-from-klue-hack/)). Exposed data is sales-account and contact information — names, business emails, job titles, phone numbers and addresses — exfiltrated via OAuth tokens from a dormant Klue→Salesforce integration; the actor (Icarus, also tracked as UNC6395) had set a 22 June publication deadline.

The concentration of cybersecurity vendors in the victim list is the notable delta: contact data for security-operations staff at those firms' customers now sits in a threat-actor corpus and is prime material for precision spear-phishing aimed at security roles. The structural lesson is unchanged from first coverage — enumerate and revoke unused third-party OAuth grants in Salesforce (`Setup → Identity → OAuth Usage`), scope active grants to minimum-necessary objects, and alert via Salesforce Event Monitoring on a connected app pulling thousands of account records in a single short session.

## Update — 2026-06-24T05:11:56Z

US cloud-communications provider 8x8 (NASDAQ: EGHT) filed a Form 8-K Item 1.05 on 2026-06-23 disclosing that an unauthorised party accessed its Salesforce environment on 2026-06-11/12 via a **third-party integration — the Klue competitive-intelligence platform** — the OAuth-integration vector behind the Icarus extortion campaign already tracked in prior briefs ([SEC EDGAR — 8x8 Form 8-K, 2026-06-23](https://www.sec.gov/Archives/edgar/data/0001023731/000102373126000084/eght-20260617.htm)).

The filing states the accessed data is limited to contract information, internal sales notes and business contact data (names, business emails, phone numbers, mailing addresses). As a publicly-listed company's mandatory material-incident disclosure, it is the formal confirmation that 8x8 is a named Klue-integration victim, extending the campaign's confirmed-victim list.

Defender takeaway for anyone running SaaS-to-Salesforce OAuth integrations (including EU public-sector users of competitive-intel tooling): audit Connected Apps in Salesforce Setup → App Manager for unexpected or stale OAuth grants, scope connected-app permissions to least privilege, and monitor `EventType=OAuthToken` in Salesforce Event Monitoring for anomalous token use (`T1078.004` Valid Accounts: Cloud, `T1550.001` token abuse).

## Update — 2026-06-25T04:59:09Z

BeyondTrust and LastPass have both disclosed that business-contact and sales-related data was exfiltrated from their Salesforce environments via the compromised Klue integration, pushing the confirmed named-victim count past 14 ([SecurityWeek, 2026-06-24](https://www.securityweek.com/beyondtrust-lastpass-impacted-by-klue-salesforce-incident/) · [Help Net Security, 2026-06-24](https://www.helpnetsecurity.com/2026/06/24/lastpass-klue-data-breach-salesforce-environment/)).

The BeyondTrust exposure is the notable delta: a privileged-access-management vendor losing its CRM contact and support-case data to a SaaS supply-chain compromise illustrates that security-vendor customer lists are a deliberate targeting priority for the Icarus extortion crew. LastPass states customer vaults were not affected. Salesforce had already disabled the Klue Battlecards connection on 17 June ([The Hacker News, 2026-06-19](https://thehackernews.com/2026/06/salesforce-disables-klue-app.html)). Any organisation receiving a Salesforce "Connected App disabled" notice for Klue should treat it as an incident trigger and audit Event Log File `ApiTotalUsage` / `ApiAnomalyEventStore` records for bulk REST API reads in the June 11–17 window (`T1199`, `T1528`, `T1213.003`).

## Update — 2026-06-27T05:17:49Z

Roughly two dozen companies have now publicly notified customers of the Klue–Salesforce OAuth-integration breach, up from eleven on June 25, with newly named EU-domiciled victims including Germany's Lucanet and Link11 alongside Blackbaud, Deel, Camunda and Tines ([SecurityWeek, 2026-06-26](https://www.securityweek.com/more-klue-breach-victims-identified-as-hackers-get-hacked/)).

Klue reportedly told customers that the attacker ("Icarus") was itself compromised and that the stolen dataset is now in the hands of a second, unnamed actor running an independent extortion campaign; Icarus's Tor leak site went offline ([TechCrunch, 2026-06-25](https://techcrunch.com/2026/06/25/hacked-klue-says-criminals-are-deleting-stolen-customer-data-but-now-other-hackers-are-making-threats/)). The root cause is unchanged — a single over-privileged legacy OAuth integration credential granting bulk Salesforce access across ~195 customer orgs — reinforcing the standing action: audit and revoke dormant Connected Apps with export scopes, and alert on anomalous bulk `ReportExport`/API activity from integration service accounts.
