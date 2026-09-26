---
schema: 1
kind: incident
title: "ShinyHunters claims a breach of the FBI's own recruitment infrastructure via an unconfirmed Oracle PeopleSoft zero-day; the FBI confirms only that it is investigating"
headline: "A serial extortion actor claims it rooted the FBI through an undisclosed Oracle PeopleSoft flaw and pivoted into an AWS-hosted government data store"
summary: >
  The extortion group ShinyHunters claims it exploited a new, undisclosed
  Oracle PeopleSoft zero-day on the night of 2026-09-21 to compromise the
  FBI's recruitment site (apply.fbijobs.gov), then pivoted into FBI-managed
  AWS GovCloud infrastructure and stole 2-3TB of employee and applicant data,
  defacing the jobs portal before the FBI took it offline. The FBI's only
  confirmed statement is that it "is aware of claims ... and is currently
  investigating" — the bureau has not confirmed the breach, its scope, or the
  claimed zero-day, and no CVE or Oracle advisory exists for it as of
  2026-09-24.
discovered_at: "2026-09-24T04:50:00Z"
updated_at: null
event_date: "2026-09-21"
run_id: 2026-09-24T0405Z-intel
priority: high
immediate_action: null
tags: [data-breach, organized-crime]
regions: [us, global]
sectors: [public-sector]
entities: ["actor:shinyhunters", "incident:shinyhunters-fbi-peoplesoft-breach-claim-2026-09", "product:oracle-peoplesoft"]
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
verification: multi-source
sourcing_note: "Multi-source on the facts that are independently confirmed: the FBIjobs.gov defacement and takedown (multiple outlets directly observed the live site), and the FBI's own 'aware of claims ... investigating' statement (given to BleepingComputer, TechCrunch and CyberScoop identically). The core technical claim — the existence and mechanism of a PeopleSoft zero-day, the AWS GovCloud lateral movement, and the 2-3TB volume — is sourced only to ShinyHunters itself and is composed here as an unconfirmed actor claim, not a confirmed fact. 404 Media's partial verification (DOJ-consistent phone numbers in a small sample) supports that some genuine personnel data changed hands but does not confirm the RCE mechanism or full scope. Credibility is set at 3 (possibly true), not 2, because the entry's central claim rests on an uncorroborated, self-interested party's own account, which BleepingComputer explicitly states it has not independently verified."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions:
  - "Watch Oracle's own security-alert channel for an emergency PeopleSoft advisory in the coming days; any organization running an internet-facing PeopleSoft component, especially a recruitment or HR/jobs-portal instance matching the FBI's own claimed entry point, should treat unexplained PeopleSoft process activity or unusual outbound connections as a priority hunt lead until Oracle confirms or denies the claim."
updates: []
migrated_from: null
---

The extortion group ShinyHunters claims it breached the FBI's own recruitment infrastructure using a new, undisclosed remote-code-execution zero-day in Oracle PeopleSoft, often used by human resources and recruiters to store job applicants' personal information ([TechCrunch, 2026-09-22](https://techcrunch.com/2026/09/22/hacking-group-shinyhunters-claims-it-breached-the-fbi-stole-agents-and-applicants-data/)). "The threat actors told BleepingComputer the vulnerability allows remote code execution and that they used it Monday night to access FBI systems before moving laterally into FBI-managed AWS GovCloud infrastructure" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters claims it stole 2-3TB of data — names, agent statuses, emails, phone numbers, home addresses and in some cases spouses' information including Social Security numbers ([Axios, 2026-09-22](https://www.axios.com/2026/09/22/shinyhunters-fbi-employees-data-hack)) — spanning current and former FBI employees and job applicants, and that it compromised additional internal services including Criminal Justice, HR and Medlink systems along the way ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The group defaced the FBI's careers site, apply.fbijobs.gov, with its Umbreon Pokémon logo and a message claiming the theft; the FBI took the site offline, and it now shows a maintenance page. The FBI's confirmed response is limited to a single statement: "The FBI is aware of claims regarding unauthorized activity affecting FBIjobs.gov and is currently investigating," ([FBI, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)) — the bureau has not confirmed a breach occurred, its scope, or the claimed PeopleSoft zero-day, and "BleepingComputer has not independently verified the alleged zero-day, lateral movement, or amount of stolen data" ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)).

404 Media first reported the claim after receiving a sample of roughly 5,000 alleged FBI personnel records; "the publication said it verified that some information in the sample was accurate, including phone numbers corresponding to people with the same names and numbers associated with US Department of Justice personnel" ([BleepingComputer, relaying 404 Media, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)), which supports that some genuine personnel data changed hands without confirming the exploitation mechanism or the full claimed volume. ShinyHunters' own account of the vulnerability is unusually specific but still entirely self-reported: "The Oracle product we exploited the 0day in is PeopleSoft. We found another one yesterday and immediately exploited it on the FBI," ([ShinyHunters, quoted by BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)) and the group says it is now exploiting the same alleged flaw against other organizations, including Fortune 500 companies, after previously targeting the education sector with a PeopleSoft campaign ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). ShinyHunters frames the FBI intrusion as retaliation for a May 2026 FBI/IC3 flash report naming the group, demanding a correction within one week rather than a ransom and claiming the demand is not financially motivated ([BleepingComputer, 2026-09-22](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-fbi-hack-data-theft-in-peoplesoft-zero-day-breach/)). The same week, ShinyHunters separately defaced the ransomware group Clop's own Tor leak site over an unrelated dispute, using it to extort Clop directly ([BleepingComputer, 2026-09-19](https://www.bleepingcomputer.com/news/security/shinyhunters-hacks-clop-leak-site-threatens-to-extort-ransomware-gang/)) — a parallel campaign against a different victim that this entry does not otherwise cover.

**Defender takeaway:** treat this strictly as an unconfirmed claim under active investigation, not a confirmed vulnerability or breach. No CVE, Oracle advisory, or independent technical analysis of the alleged PeopleSoft zero-day exists as of 2026-09-24. The transferable lesson for any government security function, including the national and cantonal police forces this constituency includes, is that ShinyHunters has both the intent and a demonstrated pattern of targeting law-enforcement and HR/recruitment infrastructure directly; any organization running an internet-facing Oracle PeopleSoft deployment, particularly a recruitment or applicant-facing instance, should watch Oracle's own security-alert channel closely in the coming days and treat unexplained PeopleSoft activity as a priority hunt item until the claim is confirmed or refuted.
