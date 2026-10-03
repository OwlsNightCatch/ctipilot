---
schema: 1
kind: incident
title: "ShinyHunters claims a breach of the FBI's own recruitment infrastructure via an unconfirmed Oracle PeopleSoft zero-day; the FBI now confirms the compromise itself while still investigating scope"
headline: "The FBI confirms ShinyHunters compromised its jobs portal; a Dutch arrest exposes an internal power struggle over the ShinyHunters brand"
summary: >
  The extortion group ShinyHunters claims it exploited a new, undisclosed
  Oracle PeopleSoft zero-day on the night of 2026-09-21 to compromise the
  FBI's recruitment site (apply.fbijobs.gov), then pivoted into FBI-managed
  AWS GovCloud infrastructure and stole employee and applicant data. The FBI
  has since issued its own press release confirming the fbijobs.gov
  compromise and "alleged impact" to employee PII, while still investigating
  scope and root cause; reported stolen data includes psychiatric/medical
  files, a separate roughly 5,000-entry sample of names, addresses, phone
  numbers and relatives' information, and reporting that the exposed data
  separately identifies counterintelligence-relevant staff, including Remote
  Operations Unit personnel. Dutch police separately confirmed an arrest connected to the
  ShinyHunters investigation, and multiple sources describe a collective
  called ScatteredLapsussHunters as now directing ShinyHunters' operations.
discovered_at: "2026-09-24T04:50:00Z"
updated_at: "2026-09-29T04:45:00Z"
event_date: "2026-09-21"
run_id: 2026-09-24T0405Z-intel
priority: high
immediate_action: null
tags: [data-breach, organized-crime]
regions: [us, global]
sectors: [public-sector]
entities: ["actor:shinyhunters", "incident:shinyhunters-fbi-peoplesoft-breach-claim-2026-09", "product:oracle-peoplesoft", "actor:scatteredlapsusshunters"]
techniques: [T1190, T1530, T1491.002]
affected_products: ["Oracle PeopleSoft"]
cves: []
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
verification: multi-source
sourcing_note: "Multi-source on the facts that are independently confirmed: the FBIjobs.gov defacement and takedown, the FBI's own statements (first 'aware of claims ... investigating', now upgraded to its own press release confirming the compromise and 'alleged impact' to employee PII), and the Dutch police arrest (confirmed via a statement on X). The psychiatric/medical-file and blood/urine-test findings are attributed to Reuters and the BBC respectively as relayed by Nextgov/FCW (both outlets' own reporting was not independently fetched); the counterintelligence-role and Remote Operations Unit staffing detail and the roughly-5,000-entry sample count are Nextgov/FCW's own reporting across two of its articles (2026-09-24 and 2026-09-28), not an FBI confirmation of scope. The ScatteredLapsussHunters/Rey leadership narrative is attributed to Krebs's sourcing ('multiple sources say') and CyberScoop's independent quote from researcher Jon DiMaggio describing ShinyHunters as a 'fluid network' brand, which corroborates the fragmentation picture without confirming the specific SLSH narrative. Credibility moves from 3 to 2: the core compromise is now government-confirmed by the FBI itself, though the full data scope remains sourced to journalist review of actor-supplied samples."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Watch Oracle's own security-alert channel for an emergency PeopleSoft advisory in the coming days; any organization running an internet-facing PeopleSoft component, especially a recruitment or HR/jobs-portal instance matching the FBI's own claimed entry point, should treat unexplained PeopleSoft process activity or unusual outbound connections as a priority hunt lead until Oracle confirms or denies the claim."
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
migrated_from: null
---

The extortion group ShinyHunters claims it breached the FBI's own recruitment infrastructure using a new, undisclosed remote-code-execution zero-day in Oracle PeopleSoft, often used by human resources and recruiters to store job applicants' personal information ([TechCrunch, 2026-09-22](https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/)). "The threat actors told BleepingComputer the vulnerability allows remote code execution and that they used it Monday night to access FBI systems before moving laterally into FBI-managed AWS GovCloud infrastructure" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters claims it stole 2-3TB of data — names, agent statuses, emails, phone numbers, home addresses and in some cases spouses' information including Social Security numbers ([Axios, 2026-09-22](https://www.axios.com/2026/09/22/shinyhunters-fbi-employees-data-hack)) — spanning current and former FBI employees and job applicants, and that it compromised additional internal services including Criminal Justice, HR and Medlink systems along the way ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The group defaced the FBI's careers site, apply.fbijobs.gov, with its Umbreon Pokémon logo and a message claiming the theft; the FBI took the site offline, and it now shows a maintenance page. The FBI's confirmed response is limited to a single statement: "The FBI is aware of claims regarding unauthorized activity affecting FBIjobs.gov and is currently investigating," ([FBI, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)) — the bureau has not confirmed a breach occurred, its scope, or the claimed PeopleSoft zero-day, and "BleepingComputer has not independently verified the alleged zero-day, lateral movement, or amount of stolen data" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)).

404 Media first reported the claim after receiving a sample of roughly 5,000 alleged FBI personnel records; "the publication said it verified that some information in the sample was accurate, including phone numbers corresponding to people with the same names and numbers associated with US Department of Justice personnel" ([BleepingComputer, relaying 404 Media, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)), which supports that some genuine personnel data changed hands without confirming the exploitation mechanism or the full claimed volume. ShinyHunters' own account of the vulnerability is unusually specific but still entirely self-reported: "The Oracle product we exploited the 0day in is PeopleSoft. We found another one yesterday and immediately exploited it on the FBI," ([ShinyHunters, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)) and the group says it is now exploiting the same alleged flaw against other organizations, including Fortune 500 companies, after previously targeting the education sector with a PeopleSoft campaign ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters frames the FBI intrusion as retaliation for a May 2026 FBI/IC3 flash report naming the group, demanding a correction within one week rather than a ransom and claiming the demand is not financially motivated ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The same week, ShinyHunters separately defaced the ransomware group Clop's own Tor leak site over an unrelated dispute, using it to extort Clop directly ([BleepingComputer, 2026-09-19](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)) — a parallel campaign against a different victim that this entry does not otherwise cover.

**Defender takeaway:** treat this strictly as an unconfirmed claim under active investigation, not a confirmed vulnerability or breach. No CVE, Oracle advisory, or independent technical analysis of the alleged PeopleSoft zero-day exists as of 2026-09-24. The transferable lesson for any government security function, including the national and cantonal police forces this constituency includes, is that ShinyHunters has both the intent and a demonstrated pattern of targeting law-enforcement and HR/recruitment infrastructure directly; any organization running an internet-facing Oracle PeopleSoft deployment, particularly a recruitment or applicant-facing instance, should watch Oracle's own security-alert channel closely in the coming days and treat unexplained PeopleSoft activity as a priority hunt item until the claim is confirmed or refuted.

## Update — 2026-09-27T04:36:00Z

Part of this entry's central open question, whether ShinyHunters' claimed FBI-specific zero-day was real, is now partially resolved. Mandiant/GTIG's report on a separate, wider mass-exploitation wave against the already-known CVE-2026-35273 documents a URL-encoded WAF-bypass technique (requesting `/%50SEMHUB/` in place of `/PSEMHUB/`), and BleepingComputer reports: "ShinyHunters has confirmed to BleepingComputer that they used this WAF bypass against FBI Jobs, but continue to claim that they also exploited "NEW unknown vulnerability in the same PSEMHUB component."" ([BleepingComputer, 2026-09-26](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/)). At least part of the FBI Jobs intrusion therefore used a known technique against a known CVE rather than the wholly undisclosed zero-day this entry originally reported, though ShinyHunters still claims an additional, still-unconfirmed vulnerability was also involved; the FBI has not updated its own statement and no party has confirmed or denied either technical claim.

**Defender takeaway (updated):** any organization running Oracle PeopleSoft, not only recruitment or applicant-facing instances, should treat the WAF-bypass technique as active and in use against government targets specifically; a WAF rule blocking the literal `/PSEMHUB/` path is not sufficient, since ShinyHunters is confirmed using the URL-encoded `/%50SEMHUB/` variant, and Mandiant warns further encoded or mixed-case variants may follow. Patch to a supported PeopleTools release or remove PSEMHUB rather than relying on WAF string-matching alone.

## Update — 2026-09-29T04:45:00Z

The FBI has now issued its own press release confirming the fbijobs.gov compromise and "alleged impact" to
employee personally identifiable information, superseding its prior "aware of claims ... investigating"
holding statement: "The FBI hasn't confirmed the type or amount of data compromised or attributed the breach
to ShinyHunters directly. The agency said it is 'actively and aggressively investigating' the incident, the
root cause and its alleged impact to FBI employees' personally identifiable data in a statement Wednesday"
([CyberScoop, 2026-09-28](https://cyberscoop.com/fbi-data-breach-shinyhunters-agent-safety-risk/)). Nextgov/FCW
reports that Reuters found the circulated records included psychiatric and medical evaluations, and that the
BBC separately reported seeing blood and urine test results: "Reuters reported Friday that records circulated
by the hackers included psychiatric and medical evaluations. The BBC also reported seeing blood and urine test
results"
([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)).
The group separately provided Nextgov/FCW a roughly 5,000-entry sample of names, home addresses, phone numbers
and relatives' information, and Nextgov/FCW's own earlier reporting found the exposed data identifies
employees working intelligence matters involving Russia, China, Hezbollah and cartels, plus personnel in the
Bureau's Remote Operations Unit, which develops tools to target computers and networks
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
([Nextgov/FCW, 2026-09-28](https://www.nextgov.com/cybersecurity/2026/09/shinyhunters-says-it-wont-publish-fbi-data/416280/)),
and states the intrusion's motive is coercive rather than financial: it is demanding the FBI retract or amend a
May 2026 public advisory (PSA260515) describing the group's operations and tactics, disputes any affiliation
with "The Com" cybercrime ecosystem, and denies using sextortion-style threats.

Dutch police separately confirmed, via a statement on X on 2026-09-28, the arrest of a 24-year-old suspect
connected to the ShinyHunters investigation; three sources identify him to Krebs on Security as Pepijn van der
Stap ("Umbreon"), a previously convicted cybercriminal who volunteered at the Dutch Institute for Vulnerability
Disclosure and worked as a software engineer at a Dutch cybersecurity firm. Dutch police are separately asking
the public to help identify a voice in a recorded February 2026 call in which a ShinyHunters member
social-engineered access into Odido, the country's largest mobile carrier; Krebs states it remains unclear
whether police have matched that voice to a confirmed identity, so this entry does not treat the Odido case as
resolved or connected to the September arrest. Krebs reports: "In the days immediately following the suspect's arrest,
remaining ShinyHunters members dramatically escalated their attacks, stealing highly sensitive data from the
FBI and extorting the Russian ransomware group Cl0p"
([Krebs on Security, 2026-09-28](https://krebsonsecurity.com/2026/09/dutch-police-arrest-reformed-hacker-in-shiny-hunters-investigation/)).
Multiple sources cited by Krebs describe a collective calling itself ScatteredLapsussHunters, led by a
Jordan-based teenage cybercriminal known as "Rey," as having taken effective control of ShinyHunters' operations
and driven its 2026 pivot toward high-risk, non-financially-motivated targets including the FBI and Cl0p; the
FBI defacement reused van der Stap's old "Umbreon" artwork, which sources say may have been an attempt to pin
the FBI intrusion on the arrested Dutch hacker rather than the group's current operators. CyberScoop separately
quotes DiMaggio's independent assessment that "ShinyHunters" today operates as a criminal brand used by a fluid
network rather than a single fixed group, corroborating the brand-fragmentation picture without itself
confirming the ScatteredLapsussHunters/Rey narrative.

**Defender takeaway (updated):** treat "ShinyHunters" as a brand a fluid, currently fragmenting network of
operators uses, not a fixed group with stable objectives; its current operators have demonstrated willingness to
target law-enforcement and national-security-adjacent personnel data specifically, and to pursue coercive,
non-financial demands rather than the financially motivated pattern this constituency may have hunted for
previously. For a national or cantonal police service or defense IT estate, the transferable lesson is that
staff-directory and personnel-system data (contact details, duty assignments, family information) carries a
counterintelligence and physical-safety value to this actor class independent of any ransom potential, and
should be protected and monitored accordingly.
