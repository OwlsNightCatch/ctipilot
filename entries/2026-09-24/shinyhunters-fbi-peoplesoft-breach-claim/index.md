---
schema: 1
kind: incident
title: "The FBI says the incident at its recruitment portal resulted from a contractor failing to apply an issued security patch on a third-party-managed platform; sources name PeopleSoft, and ShinyHunters claimed the breach"
headline: "FBI: a contractor's missed security patch on a third-party platform caused the portal breach ShinyHunters claimed"
summary: >
  The extortion group ShinyHunters claims it exploited Oracle PeopleSoft to compromise the FBI's recruitment site
  (apply.fbijobs.gov), then pivoted into FBI-managed AWS GovCloud infrastructure and stole employee and applicant data; it told
  BleepingComputer it used the URL-encoded WAF bypass for the known PeopleSoft flaw CVE-2026-35273 and still claims a further
  unknown flaw. On 2026-10-06 the FBI's cyber chief said the incident resulted from a security failure of a platform managed by
  a third-party organization after a contractor failed to implement a security patch explicitly issued to secure it, and that
  the FBI has removed the contractor; Reuters' sources, as relayed by SecurityWeek, name Oracle PeopleSoft and Accenture, and
  the FBI names neither. Reuters reports psychiatric and medical files in the documents the group shared, Nextgov/FCW reports,
  citing two people familiar with the matter, that the data covers intelligence analysts and Remote Operations Unit personnel,
  and Nextgov/FCW relays Reuters' report of a suspected member detained in Jordan who is helping
  investigators.
discovered_at: "2026-09-24T04:50:00Z"
updated_at: "2026-10-07T04:53:00Z"
event_date: "2026-09-21"
run_id: 2026-09-24T0405Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime]
regions: [us, global]
sectors: [public-sector]
entities: ["actor:shinyhunters", "incident:shinyhunters-fbi-peoplesoft-breach-claim-2026-09", "product:oracle-peoplesoft", "actor:scatteredlapsusshunters"]
techniques: [T1190, T1530, T1491.002]
affected_products: ["Oracle PeopleSoft"]
cves:
  - id: CVE-2026-35273
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: Oracle PeopleSoft PeopleTools (PSEMHUB component)
    fixed: Oracle security alert CVE-2026-35273 (2026-06-10)
sources:
  - url: "https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/"
    publisher: "BleepingComputer"
    date: "2026-09-22"
    role: primary
  - url: "https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/"
    publisher: "TechCrunch"
    date: "2026-09-22"
    role: primary
  - url: "https://www.404media.co/we-hacked-the-fbi-hackers-say-they-have-data-on-all-fbi-employees/"
    publisher: "404 Media (original reporting, first to receive a data sample)"
    date: "2026-09-22"
    role: primary
  - url: "https://cyberscoop.com/shinyhunters-claims-fbi-attack/"
    publisher: "CyberScoop"
    date: "2026-09-22"
    role: corroborating
  - url: "https://www.axios.com/2026/09/22/shinyhunters-fbi-employees-data-hack"
    publisher: "Axios"
    date: "2026-09-22"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/shinyhunters-claims-fbi-breach-says-it.html"
    publisher: "The Hacker News"
    date: "2026-09-23"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/"
    publisher: "BleepingComputer"
    date: "2026-09-19 (updated 2026-09-21)"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
    publisher: "BleepingComputer"
    date: "2026-09-26"
    role: corroborating
  - url: "https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/"
    publisher: "Krebs on Security"
    date: "2026-09-28"
    role: corroborating
  - url: "https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/"
    publisher: "CyberScoop"
    date: "2026-09-28"
    role: corroborating
  - url: "https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/"
    publisher: "Nextgov/FCW"
    date: "2026-09-28"
    role: corroborating
  - url: "https://www.nextgov.com/cybersecurity/2026/09/stolen-fbi-data-reveals-employees-roles-intelligence-and-surveillance/416182/"
    publisher: "Nextgov/FCW"
    date: "2026-09-24"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2026-06-12"
    role: corroborating
  - url: "https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii"
    publisher: "FBI National Press Office"
    date: "2026-09-23"
    role: primary
  - url: "https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/"
    publisher: "Nextgov/FCW"
    date: "2026-10-06"
    role: corroborating
  - url: "https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/"
    publisher: "SecurityWeek"
    date: "2026-10-06"
    role: corroborating
  - url: "https://www.theregister.com/security/2026/10/05/fbi-confirms-multiple-arrests-related-to-shinyhunters-hack/5301178"
    publisher: "The Register"
    date: "2026-10-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The threat actors told BleepingComputer the vulnerability allows remote code execution and that they used it Monday night to access FBI systems before moving laterally into FBI-managed AWS GovCloud infrastructure."
    publisher: "BleepingComputer"
  - quote: "The FBI is aware of claims regarding unauthorized activity affecting FBIjobs.gov and is currently investigating,"
    publisher: "FBI, quoted by BleepingComputer"
  - quote: "BleepingComputer has not independently verified the alleged zero-day, lateral movement, or amount of stolen data."
    publisher: "BleepingComputer"
  - quote: "The publication said it verified that some information in the sample was accurate, including phone numbers corresponding to people with the same names and numbers associated with US Department of Justice personnel."
    publisher: "BleepingComputer, relaying 404 Media's own verification"
  - quote: "ShinyHunters told Axios in an email that the stolen data includes names, FBI agent statuses, emails, phone numbers, home addresses and \"sometimes even spouse information,\" including their Social Security numbers."
    publisher: "Axios"
  - quote: "ShinyHunters has confirmed to BleepingComputer that they used this WAF bypass against FBI Jobs, but continue to claim that they also exploited \"NEW unknown vulnerability in the same PSEMHUB component.\""
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
  - quote: "The FBI confirmed that it was investigating claims of unauthorized activity affecting FBIjobs.gov but did not confirm that its systems had been breached or that data was stolen."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/"
  - quote: "The FBI hasn't confirmed the type or amount of data compromised or attributed the breach to ShinyHunters directly. The agency said it is \"actively and aggressively investigating\" the incident, the root cause and its alleged impact to FBI employees' personally identifiable data in a statement Wednesday."
    publisher: "CyberScoop"
    source_url: "https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/"
  - quote: "Limited samples of the stolen data contain FBI agents' personal contact information, details on family members, office and duty assignments and, in some cases, information on agency personnel specialties, multiple sources said."
    publisher: "CyberScoop"
    source_url: "https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/"
  - quote: "In the days immediately following the suspect's arrest, remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the FBI and extorting the Russian ransomware group Cl0p."
    publisher: "Krebs on Security"
    source_url: "https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/"
  - quote: "Since the very beginning we had made our decision that we would never publish this data. We have never intended to nor have we ever planned to"
    publisher: "ShinyHunters, quoted by Nextgov/FCW"
    source_url: "https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/"
  - quote: "Reuters reported Friday that records circulated by the hackers included psychiatric and medical evaluations. The BBC also reported seeing blood and urine test results."
    publisher: "Nextgov/FCW"
    source_url: "https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/"
  - quote: "The FBI is aware of a cybercriminal enterprise group claiming a compromise of the fbijobs.gov portal and alleged impact to FBI employee personally identifiable information (PII)."
    publisher: "FBI National Press Office"
    source_url: "https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii"
  - quote: "the incident occurred as the result of a security failure of a platform managed by a third-party organization"
    publisher: "FBI cybersecurity chief Brett Leatherman, in a statement to Nextgov/FCW"
    source_url: "https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/"
  - quote: "a contractor failed to implement a security patch explicitly issued to secure the platform"
    publisher: "FBI cybersecurity chief Brett Leatherman, in a statement to Nextgov/FCW"
    source_url: "https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/"
  - quote: "the system in question is Oracle’s PeopleSoft human resources platform, and the outside organization is Accenture"
    publisher: "SecurityWeek, relaying Reuters' sources"
    source_url: "https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/"
verification: multi-source
sourcing_note: "Multi-source on the defacement and takedown, the FBI's statements and the Dutch arrest. The CVE-2026-35273 link rests on ShinyHunters' own statement to BleepingComputer, the psychiatric, medical and blood-test findings are Reuters' and the BBC's as relayed by Nextgov/FCW, the analyst-role detail is Nextgov/FCW's reporting from two people familiar with the matter, and the ScatteredLapsussHunters leadership account rests on Krebs's sources. Sources differ on whether the FBI's 2026-09-23 statement confirms the compromise. The FBI cyber chief's statement of 2026-10-06 reaches the reader through Nextgov/FCW and SecurityWeek; the product and the contractor are named only by anonymous sources (Reuters' sources via SecurityWeek, a person with knowledge of the matter via Nextgov/FCW), and Reuters is cited only as relayed."
confidence: medium
references:
  - 2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-27T04:36:00Z"
    run_id: 2026-09-27T0404Z-intel
    type: update
    summary: >
      ShinyHunters has confirmed to BleepingComputer that the FBI Jobs intrusion used the same
      URL-encoded WAF-bypass technique Mandiant documents in a separate, wider mass-exploitation
      wave against CVE-2026-35273, partially resolving what was an entirely unconfirmed zero-day
      claim; the group still claims it also exploited a further, still-undisclosed vulnerability in
      the same PSEMHUB component. No party has confirmed the additional vulnerability, and the FBI
      has not updated its statement.
    fields: [evidence, sources, body]
  - at: "2026-09-29T04:45:00Z"
    run_id: 2026-09-29T0405Z-intel
    type: update
    summary: >
      The FBI has issued its own press release confirming the fbijobs.gov compromise and "alleged
      impact" to employee PII, upgrading its prior "aware of claims" holding statement, while stating
      it still has not confirmed scope or attributed the breach to ShinyHunters by name. Nextgov/FCW
      reports Reuters and BBC findings of psychiatric/medical files in the stolen sample, and its own
      reporting identifies counterintelligence-relevant staff (including Remote Operations Unit
      personnel) among roughly 5,000 exposed entries; researchers warn of physical-safety and
      counterintelligence exposure. ShinyHunters says it will not publish the data, and states its
      motive is coercive (forcing retraction of a May FBI advisory), not financial. Dutch police
      confirmed the arrest of a suspect tied to the ShinyHunters investigation, and multiple sources
      describe a collective calling itself ScatteredLapsussHunters as now directing ShinyHunters'
      operations.
    fields: [title, headline, summary, entities, classification, sources, evidence, sourcing_note, body]
  - at: "2026-09-30T06:56:58Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The takeaway said no CVE or Oracle advisory was involved, although ShinyHunters told
      BleepingComputer it used the WAF bypass for CVE-2026-35273 against FBI Jobs. That link is now
      attributed to the group, the CVE is recorded with a link to the PeopleSoft campaign entry that
      carries the patch and hunt actions, the watch-for-an-advisory action is removed, and the
      priority moves from high to notable because the defender value lies in the already-covered
      CVE. The FBI's 2026-09-23 statement leaves the point of breach undetermined, and sources
      differ on whether it confirms the compromise: Krebs on Security reads it as confirmation,
      while CyberScoop reports no confirmed scope or attribution. The
      group's motive is now given in its own words, including its later description of the
      confrontation as a marketing campaign. Figures and the analyst-role detail are cited to the
      outlets that carry them, the takeaways are folded into one, and the arrested suspect is no
      longer named.
    fields: [priority, cves, references, actions, sources, body, title, headline, summary, classification, sourcing_note, evidence]
  - at: "2026-10-07T04:53:00Z"
    run_id: 2026-10-07T0404Z-intel
    type: update
    summary: >
      The FBI's cyber chief said on 2026-10-06 that the incident resulted from a security failure of a platform managed by a
      third-party organization after a contractor failed to implement a security patch explicitly issued to secure it, and that
      the FBI removed the contractor; Reuters' sources, as relayed by SecurityWeek, name Oracle PeopleSoft and Accenture. This
      replaces the 2026-09-23 position that the point of breach was undetermined. Nextgov/FCW also relays Reuters' report of a
      suspected member of the group detained in Jordan and helping investigators.
    fields: [title, headline, summary, classification, sources, evidence, sourcing_note, body]
migrated_from: null
---

The extortion group ShinyHunters claims it breached the FBI's own recruitment infrastructure using a new Oracle PeopleSoft zero-day ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). PeopleSoft is often used by human resources and recruiters to store job applicants' personal information ([TechCrunch, 2026-09-22](https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/)). "The threat actors told BleepingComputer the vulnerability allows remote code execution and that they used it Monday night to access FBI systems before moving laterally into FBI-managed AWS GovCloud infrastructure" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters claims it stole between 2TB and 3TB of data spanning current and former FBI employees and job applicants, and that it compromised additional internal services including Criminal Justice, HR and Medlink systems along the way ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). It told Axios the data includes names, agent statuses, emails, phone numbers, home addresses and in some cases spouses' information including Social Security numbers, a claim Axios reports as more than 2 terabytes ([Axios, 2026-09-22](https://www.axios.com/2026/09/22/shinyhunters-fbi-employees-data-hack)). According to the group, which shared a screenshot, it defaced the FBI's careers site, apply.fbijobs.gov, with its Umbreon Pokémon logo and a message claiming the theft ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)); the site was down on 2026-09-22 ([TechCrunch, 2026-09-22](https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/)) and remained offline on 2026-09-28 ([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)). The FBI's first response was a single statement: "The FBI is aware of claims regarding unauthorized activity affecting FBIjobs.gov and is currently investigating," ([FBI, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)), and "BleepingComputer has not independently verified the alleged zero-day, lateral movement, or amount of stolen data" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The FBI did not then confirm whether its systems were breached or data was stolen ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). Its statement of 2026-09-23, titled "FBI Statement on Compromise of fbijobs.gov Portal and Alleged Impact to FBI Employee PII", says it is aware of a group "claiming a compromise" of the portal, that "the point of breach is still undetermined" between a third party and the FBI's own enterprise, and that it is investigating with the third-party providers that support fbijobs.gov ([FBI, 2026-09-23](https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii)); on 2026-10-06 its cyber chief placed the cause at a third-party-managed platform and a contractor's unapplied patch (see the update of 2026-10-07). **Contradiction:** Krebs on Security describes that release as a brief statement "confirming the hack" ([Krebs on Security, 2026-09-28](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)), while CyberScoop reports that the FBI "hasn't confirmed the type or amount of data compromised or attributed the breach to ShinyHunters directly" ([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)) and BleepingComputer, recapping the FBI's first response, that it "did not confirm that its systems had been breached or that data was stolen" ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)).

404 Media first reported the claim after receiving a sample of roughly 5,000 alleged FBI personnel records; "the publication said it verified that some information in the sample was accurate, including phone numbers corresponding to people with the same names and numbers associated with US Department of Justice personnel" ([BleepingComputer, relaying 404 Media, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)), which supports that some genuine personnel data changed hands without confirming the exploitation mechanism or the full claimed volume. ShinyHunters' own account of the vulnerability is unusually specific but still entirely self-reported: "The Oracle product we exploited the 0day in is PeopleSoft. We found another one yesterday and immediately exploited it on the FBI," ([ShinyHunters, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)) and the group says it is now exploiting the same alleged flaw against other organizations, including Fortune 500 companies, after previously targeting the education sector with a PeopleSoft campaign ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters frames the FBI intrusion as retaliation for a May 2026 FBI/IC3 flash report naming the group, demanding a correction within one week rather than a ransom and claiming the demand is not financially motivated ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The week before, ShinyHunters separately defaced the ransomware group Clop's own Tor leak site over an unrelated dispute, using it to extort Clop directly ([BleepingComputer, 2026-09-19](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)).

**Defender takeaway:** ShinyHunters says it reached FBI Jobs through the URL-encoded WAF bypass for CVE-2026-35273 in PeopleSoft's PSEMHUB component, and still claims a further unknown flaw in the same component ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)). The FBI's cyber chief said on 2026-10-06 that "a contractor failed to implement a security patch explicitly issued to secure the platform", a platform managed by a third-party organization, and the FBI removed the contractor ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)); the FBI names neither the product nor a CVE ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)), the link to CVE-2026-35273 rests on ShinyHunters' account ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)), and Reuters' sources name PeopleSoft and Accenture ([SecurityWeek, 2026-10-06](https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/)). The lesson is where the patch lag sat: a platform run by a supplier, with the fix issued and not applied. For Swiss police and other government security functions, any internet-facing PeopleSoft instance, particularly an applicant-facing one, is a priority patch-and-hunt target. A WAF rule that blocks the literal `/PSEMHUB/` path misses the encoded `/%50SEMHUB/` form, and Google warns of other percent-encoded or mixed-case variants, so install the security update, and ask any supplier that runs a PeopleSoft platform for you to show that it has applied it, rather than rely on WAF string matching, and search WebLogic access logs for requests to `/PSEMHUB/` and its encoded variants ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)). Patch and hunting guidance for the flaw is in the [PeopleSoft campaign entry of 2026-06-11](../2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md). Researchers quoted by CyberScoop warn that the assignment and contact data in the samples creates counterintelligence and safety risk for personnel ([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)), which makes staff-directory and personnel-system data worth protecting and monitoring independent of any ransom potential.

## Update — 2026-09-27T04:36:00Z

ShinyHunters has now given a partial answer of its own to the central open question, whether its claimed FBI-specific zero-day was real. Mandiant/GTIG's report on a separate, wider mass-exploitation wave against the already-known CVE-2026-35273 documents a URL-encoded WAF-bypass technique (requesting `/%50SEMHUB/` in place of `/PSEMHUB/`), and BleepingComputer reports: "ShinyHunters has confirmed to BleepingComputer that they used this WAF bypass against FBI Jobs, but continue to claim that they also exploited "NEW unknown vulnerability in the same PSEMHUB component."" ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)). By the group's own account, at least part of the FBI Jobs intrusion used a known technique against a known CVE rather than the wholly undisclosed zero-day it first claimed, though ShinyHunters still claims an additional, still-unconfirmed vulnerability was also involved. The FBI has not confirmed that its systems were breached or that data was stolen ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)), and no party has confirmed or denied either technical claim.

## Update — 2026-09-29T04:45:00Z

The FBI has issued a further statement on the fbijobs.gov incident ([FBI, 2026-09-23](https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii)). CyberScoop reports: "The FBI hasn't confirmed the type or amount of data compromised or attributed the breach
to ShinyHunters directly. The agency said it is 'actively and aggressively investigating' the incident, the
root cause and its alleged impact to FBI employees' personally identifiable data in a statement Wednesday"
([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)). Nextgov/FCW
reports that Reuters found the circulated records included psychiatric and medical evaluations, and that the
BBC separately reported seeing blood and urine test results: "Reuters reported Friday that records circulated
by the hackers included psychiatric and medical evaluations. The BBC also reported seeing blood and urine test
results"
([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)).
The group separately provided Nextgov/FCW a roughly 5,000-entry sample of names, home addresses, phone numbers
and relatives' information, and Nextgov/FCW's earlier reporting, citing two people familiar with the matter, says the exposed data covers intelligence analysts working on Russia, China, Hezbollah and cartel matters, plus personnel in the Bureau's Remote Operations Unit, which develops tools to target computers and networks
([Nextgov/FCW, 2026-09-24](https://www.nextgov.com/cybersecurity/2026/09/stolen-fbi-data-reveals-employees-roles-intelligence-and-surveillance/416182/)).
CyberScoop separately reports: "Limited samples of the stolen data contain FBI agents'
personal contact information, details on family members, office and duty assignments and, in some cases,
information on agency personnel specialties, multiple sources said"
([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)). Security
researchers Jon DiMaggio (Arkem Cyber) and Cynthia Kaiser (a former FBI official, now at Halcyon) warn the
exposure creates counterintelligence and physical-safety risk for agents on sensitive cases, and that data
already shared with journalists as proof samples is irretrievably disseminated regardless of any later takedown.
ShinyHunters told Nextgov/FCW it will not publish the stolen data: "Since the very beginning we had made our
decision that we would never publish this data. We have never intended to nor have we ever planned to"
([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)).
The group had earlier said the attack was retaliation for the FBI's May 2026 advisory on its operations (PSA260515), gave the FBI one week to correct or remove it while calling the demand neither financially motivated nor extortion, rejected claims that it is part of "The Com", and disputed the advisory's claims that it harasses victims and their relatives, conducts swatting attacks and falsely claims to hold compromising material ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). In its later statement to Nextgov/FCW, it called the confrontation "a marketing campaign to protect our business and actively combat disinformation", said "This was not a threat. It may have been worded like a threat", and claimed it had never expected compliance ([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)).

Dutch police separately confirmed, via a statement on X on 2026-09-28, the arrest of a 24-year-old suspect connected to the ShinyHunters investigation ([Krebs on Security, 2026-09-28](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)). Dutch police are separately asking
the public to help identify a voice in a recorded February 2026 call in which a ShinyHunters member
social-engineered access into Odido, the country's largest mobile carrier; Krebs states it remains unclear
whether police have matched that voice to a confirmed identity, so the Odido case should not be read as resolved or connected to the September arrest. Krebs reports: "In the days immediately following the suspect's arrest,
remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the
FBI and extorting the Russian ransomware group Cl0p"
([Krebs on Security, 2026-09-28](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)).
Multiple sources cited by Krebs describe a teenage cybercriminal known as "Rey," who operates as part of a collective calling itself ScatteredLapsussHunters, as having taken effective control of ShinyHunters' operations
and driven what they call "a major pivot away from the more measured tenor of the hacking gang's operations", toward high-risk targets including the FBI and Cl0p; sources say the FBI defacement reused artwork associated with the arrested suspect, possibly to pin the FBI intrusion on him rather than on the group's current operators. CyberScoop separately
quotes DiMaggio's independent assessment that "ShinyHunters" today operates as a criminal brand used by a fluid
network rather than a single fixed group, corroborating the brand-fragmentation picture without itself
confirming the ScatteredLapsussHunters/Rey narrative.

## Correction — 2026-09-30T06:56:58Z

ShinyHunters told BleepingComputer it used the URL-encoded WAF bypass against FBI Jobs, and it still claims a further unknown flaw in the same PSEMHUB component ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)). That bypass is the technique used against CVE-2026-35273, which CISA listed as exploited on 2026-06-12 ([CISA KEV catalog, 2026-06-12](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The takeaway previously said no CVE was involved. The CVE link is the group's own account, and the FBI said on 2026-09-23 that the point of breach, a third party or its own enterprise, was still undetermined ([FBI, 2026-09-23](https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii)).

The FBI's statement of 2026-09-23 is titled as a statement on the "Compromise of fbijobs.gov Portal" but says a group is "claiming a compromise" ([FBI, 2026-09-23](https://www.fbi.gov/news/press-releases/fbi-statement-on-compromise-of-fbijobsgov-portal-and-alleged-impact-to-fbi-employee-pii)). Krebs on Security reads it as confirming the hack ([Krebs on Security, 2026-09-28](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)), while CyberScoop reports that the FBI has not confirmed the type or amount of data or attributed the breach to ShinyHunters ([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)). The 2026-09-29 update presented the statement as a confirmation without noting that this reading is disputed, and is corrected in place.

The 2026-09-29 update also called the group's motive coercive rather than financial. The group had framed its demand that the FBI correct or remove its May advisory as neither financially motivated nor extortion ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)), and later told Nextgov/FCW the confrontation was "a marketing campaign" and "not a threat", claiming it had never expected compliance ([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)).

## Update — 2026-10-07T04:53:00Z

FBI cybersecurity chief Brett Leatherman gave Nextgov/FCW the bureau's clearest account of the cause so far: "the incident occurred as the result of a security failure of a platform managed by a third-party organization", because "a contractor failed to implement a security patch explicitly issued to secure the platform", and the FBI has removed the contractor ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)). A person with knowledge of the matter told Nextgov/FCW that Accenture is responsible for software patch management and maintaining custom code at the FBI, and that Oracle, whose PeopleSoft platform ShinyHunters claimed as the initial access point, provided the security patches that were not integrated ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)). SecurityWeek, citing Reuters' sources, says the system is Oracle's PeopleSoft human resources platform and the outside organization is Accenture; Accenture did not answer questions about the patching failure and said only that it is proud to support the mission of the FBI ([SecurityWeek, 2026-10-06](https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/)).

This replaces the FBI's statement of 2026-09-23 that the point of breach, a third party or its own enterprise, was undetermined: the failure is now placed at a third-party-managed platform. The FBI's statement names neither the product, the contractor nor a CVE, and Nextgov/FCW notes it does not say why the patch was missed ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)). The link to CVE-2026-35273 stays ShinyHunters' account, given to BleepingComputer ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)).

Nextgov/FCW relays Reuters' report of 2026-10-03 that a suspected ShinyHunters member had been detained in Jordan and was helping investigators ([Nextgov/FCW, 2026-10-06](https://www.nextgov.com/cybersecurity/2026/10/fbi-removes-accenture-contractor-after-missed-security-patch-led-breach/416441/)). SecurityWeek says this is the member known as Rey ([SecurityWeek, 2026-10-06](https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/)). An FBI spokesperson told The Register on 2026-10-05 that the bureau has "already worked with partners to arrest multiple subjects" while declining to comment on specific arrests ([The Register, 2026-10-05](https://www.theregister.com/security/2026/10/05/fbi-confirms-multiple-arrests-related-to-shinyhunters-hack/5301178)). SecurityWeek adds that a post urging organizations to pay has been removed from the group's site while its most recent victim post is dated 2026-09-22 ([SecurityWeek, 2026-10-06](https://www.securityweek.com/fbi-blames-contractors-missed-patch-for-shinyhunters-breach/)).
