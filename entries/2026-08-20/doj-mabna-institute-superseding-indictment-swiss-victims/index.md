---
schema: 1
kind: incident
title: "DOJ's superseding indictment against Iran's Mabna Institute names Switzerland twice — among the countries whose universities were compromised, and among those whose companies had employee mailboxes taken"
headline: "Eight more defendants, a password-spray campaign against government entities, and a victim list a Swiss reader is on"
summary: >
  The US Department of Justice unsealed a 14-count superseding indictment on 2026-08-18 charging 17 members of
  the Mabna Institute, an Iran-based company that has run intrusions on behalf of the Islamic Revolutionary
  Guard Corps since at least 2013; nine were charged in 2018 and eight are new. The indictment covers 144 US and
  178 foreign universities, at least 42 US and 11 foreign companies, at least five US federal and state agencies
  and two NGOs. DOJ's own release names Switzerland in both foreign-victim lists. The tradecraft is
  unglamorous and still current: spearphishing against academic staff, reuse of stolen credentials to log into
  professor accounts and pull research, and — for the corporate and government intrusions the new defendants are
  charged with — password spraying, which DOJ says cost victims more than $20 million to investigate and
  remediate.
discovered_at: "2026-08-20T05:10:00Z"
event_date: "2026-08-18"
run_id: 2026-08-20T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, law-enforcement, identity, phishing]
regions: [global, europe, switzerland]
sectors: [education, public-sector]
entities: [actor:mabna-institute]
techniques: [T1566, T1078, T1110.003]
affected_products: []
cves: []
sources:
  - url: "https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary"
    publisher: "U.S. Department of Justice, Office of Public Affairs"
    date: "2026-08-18"
    role: primary
  - url: "https://www.nextgov.com/cybersecurity/2026/08/doj-charges-17-iranians-cybertheft-campaign/415511/"
    publisher: "Nextgov/FCW"
    date: "2026-08-19"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/us-charges-iranian-hackers-over-34-billion-intellectual-property-theft/"
    publisher: "BleepingComputer"
    date: "2026-08-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "178 universities located in foreign countries, including Australia, Canada, China, Denmark, Finland, Germany, Ireland, Israel, Italy, Japan, Malaysia, Netherlands, Norway, Poland, Saudi Arabia, Singapore, South Korea, Spain, Sweden, Switzerland, Turkey and the United Kingdom."
    publisher: "U.S. Department of Justice, Office of Public Affairs"
  - quote: "at least approximately 11 foreign companies based in Germany, Italy, Switzerland, Sweden, and the United Kingdom"
    publisher: "U.S. Department of Justice, Office of Public Affairs"
verification: multi-source
sourcing_note: >
  The country lists that carry this entry's relevance come from the Department of Justice's own release for the
  freshly unsealed indictment, not from coverage of the 2018 predicate case — neither corroborating outlet names
  any country for the foreign universities or foreign companies. The conduct behind those lists is historical:
  DOJ dates the university spearphishing campaign from approximately 2013 through at least December 2017 and
  does not date the foreign-company intrusions separately, so this entry treats the Swiss footprint as an
  established past fact newly stated in an in-window filing, not as evidence of current intrusions. The
  allegations are untested in court and every defendant is presumed innocent. The parallel release from the
  prosecuting US Attorney's office could not be read this run — an anti-bot challenge on one transport and an
  HTTP 401 on the other, with the reader pool exhausted — so the entry rests on the department-level release,
  which was read in full. DOJ's description of the university campaign says spearphishing and reuse of stolen
  credentials; no source describes cloned login pages, so no such mechanism is claimed here.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

A 14-count superseding indictment unsealed on 2026-08-18 charges 17 members of the Mabna Institute, an Iran-based company that, in the Department of Justice's words, "since at least 2013, has conducted a coordinated campaign of cyber intrusions into computer systems for 144 U.S.-based universities, 178 foreign universities, at least 42 U.S.-based private sector companies, at least 11 foreign private sector companies, at least five U.S. federal and state government agencies, and at least two non-governmental organizations (NGOs)" ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)). Nine of the seventeen were previously charged in a seven-count indictment announced in March 2018 ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)); the new filing adds eight defendants ([Nextgov/FCW, 2026-08-19](https://www.nextgov.com/cybersecurity/2026/08/doj-charges-17-iranians-cybertheft-campaign/415511/)). The institute worked on behalf of the Islamic Revolutionary Guard Corps, and the stolen academic material was resold through operator-run websites.

For a European reader the load-bearing detail is in DOJ's own victim breakdown rather than in the headline. The department names the countries hosting the 178 compromised foreign universities — a list that runs from Australia and Canada through Germany, Ireland, Italy, the Netherlands, Norway, Poland, Spain, Sweden and Switzerland to the United Kingdom — and separately describes "at least approximately 11 foreign companies based in Germany, Italy, Switzerland, Sweden, and the United Kingdom" whose employee email accounts were compromised ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)). Swiss universities and Swiss companies are, on the government's own account, inside this campaign's victim set. The conduct is historical — the university campaign is dated from around 2013 through at least December 2017 — so this is not notice of a live intrusion; it is a state-directed collection programme against European academic and corporate research being described, with country-level specificity, in a document published this week.

The tradecraft is worth restating precisely because it is so ordinary. Against universities, DOJ describes members of the conspiracy using stolen account credentials to obtain unauthorised access to professor accounts and using that access to steal research and other academic data; one defendant's specific role was tracking the progress of spearphishing campaigns, exchanging credentials for compromised accounts with co-conspirators, building targeting lists, conducting reconnaissance and crafting phishing messages. Against companies and at least two governmental entities, the new charges name a different method: DOJ alleges three defendants "participated in the Mabana Institute's efforts to hack into private sector companies and at least two governmental entities — including through password spray attacks, obtaining unauthorized access to victim systems, and exfiltrating data — causing victims to suffer an excess of $20 million in costs to investigate and remediate the intrusions" ([U.S. Department of Justice, 2026-08-18](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)). Nextgov describes the same operating model from the outside: the institute employed or contracted hackers who ran phishing attacks, looked for vulnerable systems and traded credentials for compromised accounts ([Nextgov/FCW, 2026-08-19](https://www.nextgov.com/cybersecurity/2026/08/doj-charges-17-iranians-cybertheft-campaign/415511/)).

**Defender takeaway:** the enduring observable here is authentication behaviour, not malware. Password spraying against a tenant shows up as a low-and-slow authentication pattern — a small number of common passwords tried against a large number of distinct accounts from a limited set of source addresses, producing many failures spread thinly across identities rather than many failures against one — and the successful outcome looks like an ordinary sign-in, which is why the follow-on signal is a valid session from an unusual location or client, followed by bulk reading of mailboxes or research repositories. **Triage:** an individual failed sign-in against an academic or corporate identity is noise, and legitimate bulk failures do occur after a password-policy change or an expired-credential event affecting many users at once; the discriminators are that the sprayed attempts distribute one credential across many accounts rather than many credentials against one, that they arrive from infrastructure with no prior relationship to the tenant, and that a small number of them succeed and are immediately followed by data access rather than by normal interactive work. For research-intensive institutions in the constituency — universities, federal research bodies, their industrial partners — the value of this filing is the reminder that the collection target is the research itself and the access route is the staff account, so multi-factor coverage on academic and contractor identities, and alerting on the spray shape above, are what actually raise the cost of this programme. The allegations remain untested in court.
