---
schema: 1
kind: incident
title: "7-Eleven confirms breach of franchisee documents after ShinyHunters claims 600,000+ Salesforce records"
headline: "7-Eleven confirms a breach of franchisee documents after ShinyHunters claims 600,000+ Salesforce records"
summary: >
  7-Eleven's notification letters of 2026-05-01, public from 2026-05-18, say an unauthorized party accessed systems storing franchisee documents
  on 2026-04-08, exposing information from franchise applications; filings in Massachusetts, Maine and Vermont count about 50 affected people.
  ShinyHunters had listed 7-Eleven on 2026-04-17 claiming more than 600,000 Salesforce records, a claim 7-Eleven has not addressed, and SecurityWeek
  traces the group's Salesforce intrusions since mid-2025 to phishing, third-party-integration abuse or misconfigurations rather than Salesforce flaws.
  In May the group also listed Charter Communications, which confirmed an incident but denied that sensitive personal or network data left.
discovered_at: "2026-05-19T05:00:03Z"
updated_at: "2026-05-25T05:00:03Z"
event_date: 2026-05-18
run_id: 2026-05-19-2505c918
priority: routine
immediate_action: null
tags:
  - data-breach
  - identity
  - cloud
  - organized-crime
regions:
  - us
sectors:
  - retail
  - telco
entities:
  - "actor:shinyhunters"
  - "incident:7-eleven-confirms-shinyhunters-salesforce-breach-600k-recor"
  - "incident:shinyhunters-charter-spectrum-listing-42m-claim"
techniques: [T1213.004, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/"
    publisher: SecurityWeek
    date: "2026-05-18"
    role: primary
  - url: "https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html"
    publisher: Security Affairs
    date: "2026-05-18"
    role: corroborating
  - url: "https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/4fe778c0-a3a9-4dbe-8e79-2c229ac5c36b.html"
    publisher: "7-Eleven notification to the Maine Attorney General"
    role: corroborating
  - url: "https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/"
    publisher: "CyberInsider"
    date: "2026-05-23"
    role: primary
  - url: "https://www.troyhunt.com/weekly-update-505/"
    publisher: "Troy Hunt (Weekly Update 505)"
    date: "2026-05-24"
    role: corroborating
  - url: "https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/"
    publisher: "Cybersecurity Dive"
    date: "2026-05-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We recently discovered that on April 8, 2026, an unauthorized third party gained access to certain 7-Eleven systems used to store franchisee documents."
    publisher: 7-Eleven (letter quoted by Security Affairs)
    source_url: "https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html"
  - quote: "The intrusions resulted from phishing, abuse of third-party integrations, or misconfigurations, rather than vulnerabilities in Salesforce products or systems."
    publisher: SecurityWeek
    source_url: "https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/"
  - quote: "The breach impacted 47 people in Massachusetts, 2 in Maine and one in Vermont, according to each state’s filing."
    publisher: Cybersecurity Dive
    source_url: "https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/"
  - quote: "We are aware of the situation, following our security protocols, and are in the process of alerting appropriate authorities. No sensitive personal information (PI) or customer proprietary network information (CPNI) data was exfiltrated by the threat actor."
    publisher: Charter (via CyberInsider)
    source_url: "https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/"
verification: multi-source
sourcing_note: >
  The breach and its scope come from 7-Eleven's own letters and state filings as reported by SecurityWeek, Security Affairs and Cybersecurity Dive;
  the 600,000-record and 42-million-record figures are ShinyHunters' unverified claims, and Charter's position
  comes from its statement to CyberInsider.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-05-25T05:00:03Z"
    run_id: 2026-05-25-d675ef38
    type: update
    summary: >
      ShinyHunters listed Charter Communications (Spectrum), claiming 42M records with a 27 May
      deadline — a fresh victim in the Salesforce-credential campaign tracked here via 7-Eleven
      (2026-05-19), and by our own tracking its first telco/ISP victim to respond publicly. Charter
      denies any "sensitive PI or CPNI" exfiltration, a denial calibrated to FCC categories; the 42M
      figure is the actor's unverified claim (CyberInsider, 2026-05-23).
    fields:
      - sectors
      - sources
      - body
    merged_from: 2026-05-25/shinyhunters-lists-charter-communications-spectrum-telco-vic
  - at: "2026-10-21T20:33:26Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      7-Eleven confirmed a breach of systems storing franchisee documents affecting about 50 people in
      three US state filings; the 600,000+ Salesforce records are ShinyHunters' unverified claim, which
      7-Eleven has not addressed. SecurityWeek describes ShinyHunters' Salesforce intrusions in general as
      phishing, third-party-integration abuse or misconfigurations and lists Instructure, Vimeo, Wynn
      Resorts, Vercel and Medtronic as other recent claims, without tying them or a vector to the 7-Eleven
      breach. CyberInsider links Charter's listing to the Salesforce-focused campaign but gives no access
      vector for it.
    fields: [body, classification, entities, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, techniques, title]
migrated_from: briefs/2026-05-19.md
---

7-Eleven's notification letters went out on 2026-05-01 ([Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)) and say an unauthorized third party gained access on 2026-04-08 to systems used to store franchisee documents ([Security Affairs, 2026-05-18](https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html)), which held personal information from the franchise application process, including names and addresses; the Vermont filing adds Social Security numbers and the Massachusetts filing Social Security numbers and driver's license data ([Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)). Filings in Massachusetts, Maine and Vermont count 47, 2 and 1 affected people, the letters offer up to 24 months of IDX identity-theft protection, and 7-Eleven says it has no reason to believe customer data was affected ([Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)); the notices became public on 2026-05-18 ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)). ShinyHunters had listed 7-Eleven on its leak site on 2026-04-17 claiming more than 600,000 Salesforce records with personal and corporate data, demanded a ransom by 2026-04-21 and then offered the data for $250,000 on a hacker forum ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)); 7-Eleven did not respond when asked about that claim ([Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)). Its relevance lies in the actor: SecurityWeek says ShinyHunters has targeted organizations' Salesforce instances since mid-2025 through phishing, abuse of third-party integrations or misconfigurations rather than Salesforce vulnerabilities, and that the group and affiliated actors recently claimed Instructure, Vimeo, Wynn Resorts, Vercel and Medtronic ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)), while Security Affairs lists the European Commission among its earlier claims ([Security Affairs, 2026-05-18](https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html)). No source says how the 7-Eleven systems were accessed.

**Exposure:** organizations whose Salesforce tenants can be reached through phished accounts, third-party integrations or misconfigurations, the paths SecurityWeek gives for the group's campaign ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)); CyberInsider describes recent victims whose environments allegedly held exposed credentials, authentication tokens or improperly secured integrations ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)).

**Defender takeaway:** the 7-Eleven breach itself, about 50 franchise applicants, asks nothing of other organizations ([Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)); for Salesforce tenants, review which third-party integrations hold access and which credentials and tokens they keep, the weaknesses ShinyHunters' recent victims allegedly had ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)).

## Update — 2026-05-25T05:00:03Z

ShinyHunters added Charter Communications, which operates the Spectrum brand, to its leak site in the week of 2026-05-23, claiming over 42 million records containing personal information and threatening to leak them unless negotiations opened before 2026-05-27; the nature of the data had not been independently verified ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). Charter confirmed a cybersecurity incident and told CyberInsider it was "following our security protocols" and alerting authorities, adding: "No sensitive personal information (PI) or customer proprietary network information (CPNI) data was exfiltrated by the threat actor." ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). Charter did not disclose how the attackers gained access, and CyberInsider links the claim to the ongoing campaign against Salesforce environments ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). Troy Hunt's weekly update of 2026-05-24 relays a post listing Charter among three new ShinyHunters claims ([Troy Hunt, 2026-05-24](https://www.troyhunt.com/weekly-update-505/)).

## Correction — 2026-10-21T20:33:26Z

7-Eleven confirmed a breach of systems storing franchisee documents, not ShinyHunters' claim of 600,000+ Salesforce records: its notification letters date the access to 2026-04-08, the filings in Massachusetts, Maine and Vermont count 47, 2 and 1 affected people, and 7-Eleven did not respond when asked about the 600,000-record claim ([Security Affairs, 2026-05-18](https://securityaffairs.com/192336/data-breach/shinyhunters-hack-7-eleven-franchisee-data-and-salesforce-records-exposed.html); [Cybersecurity Dive, 2026-05-20](https://www.cybersecuritydive.com/news/7-eleven-cyberattack-franchisee-data/820698/)). SecurityWeek lists Instructure, Vimeo, Wynn Resorts, Vercel and Medtronic as recent claims by ShinyHunters and affiliated actors and describes the group's Salesforce intrusions since mid-2025 as phishing, third-party-integration abuse or misconfigurations; it does not place those victims in one campaign with 7-Eleven or name a vector for the 7-Eleven breach ([SecurityWeek, 2026-05-18](https://www.securityweek.com/7-eleven-data-breach-confirmed-after-shinyhunters-ransom-demand/)). Likewise, Charter did not disclose how the attackers got in, and CyberInsider only links the Charter claim to the Salesforce-focused campaign ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)). CyberInsider later updated its report: the attackers leaked the Charter dataset publicly, and Have I Been Pwned counts 4.9 million unique email addresses with names, phone numbers and physical addresses ([CyberInsider, 2026-05-23](https://cyberinsider.com/charter-communications-confirms-data-breach-as-hackers-threaten-leak-of-42-million-records/)).
