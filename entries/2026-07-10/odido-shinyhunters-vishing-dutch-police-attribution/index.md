---
schema: 1
kind: incident
title: "ShinyHunters' Odido (NL telecom) breach: Dutch police voice analysis points to Dutch-national involvement; same vishing-into-spoofed-portal playbook, now against an EU telco"
headline: "Dutch police tie ShinyHunters' Odido telecom breach to Dutch nationals via voice analysis — the vishing-to-spoofed-portal playbook now hits an EU telco"
summary: >
  Dutch National Police announced on 9 July 2026 that its investigation into the February 2026 ShinyHunters breach of telecom operator Odido (and its Ben brand) found strong indications of Dutch-national involvement, based on forensic voice analysis of a call recorded during the intrusion. The intrusion used the ShinyHunters playbook already tracked in this store: a vishing call impersonating IT staff persuaded a customer-service employee to authenticate into a spoofed corporate portal, harvesting credentials used to bulk-export 6.2M+ customer records before the account was blocked within an hour. The new signal is the EU-telco victim, the law-enforcement attribution, and two open Dutch DPA investigations; the underlying TTP is the ShinyHunters playbook already tracked in this store.
discovered_at: "2026-07-10T04:36:19Z"
event_date: "2026-07-09"
run_id: 2026-07-10T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity, organized-crime, law-enforcement]
regions: [europe]
sectors: [telco]
entities: [actor:shinyhunters, incident:odido-telecom-breach-netherlands-2026]
techniques: [T1566.004, T1684.001, T1078, T1213]
affected_products: []
cves: []
sources:
  - url: "https://www.politie.nl/nieuws/2026/juli/8/onderzoek-naar-hack-odido-wijst-op-mogelijke-betrokkenheid-nederlanders.html"
    publisher: "Politie (Dutch National Police)"
    date: "2026-07-09"
    role: primary
  - url: "https://nos.nl/artikel/2622288-bellende-odido-hacker-vermoedelijk-nederlander-politie-dreigt-stem-openbaar-te-maken"
    publisher: "NOS (Dutch public broadcaster)"
    date: "2026-07-09"
    role: corroborating
  - url: "https://nos.nl/artikel/2614128-odido-ontdekte-pas-na-bericht-van-hackers-dat-klantgegevens-waren-gestolen"
    publisher: "NOS (Dutch public broadcaster)"
    date: "2026-05-12"
    role: corroborating
  - url: "https://nos.nl/artikel/2602080-hack-bij-odido-gegevens-miljoenen-klanten-in-handen-van-criminelen"
    publisher: "NOS (Dutch public broadcaster)"
    date: "2026-02-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In het onderzoek heeft de politie sterke aanwijzingen gevonden dat Nederlandse criminelen betrokken zijn bij de Odido-hack."
    publisher: "Politie (Dutch National Police)"
  - quote: "De hacker wist deze medewerker over te halen om in te loggen op een valse versie van de werkomgeving. Zo heeft hij de inloggegevens van die persoon gestolen."
    publisher: "NOS (Dutch public broadcaster)"
verification: multi-source
sourcing_note: "Primary is the Dutch National Police statement (Admiralty A for its own investigation); the vishing mechanism is on-record from Odido's CEO via NOS. Original-language Dutch quotes carry English glosses in the body."
confidence: high
update_of: null
references: [2026-06-26/shinyhunters-used-a-single-vishing-call-into-the-company-s-i]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Reinforce helpdesk/customer-service verification: require out-of-band callback confirmation before any staff member authenticates in response to an inbound call claiming to be internal IT — the control that would have stopped both the Odido and the earlier tracked ShinyHunters vishing intrusions."
  - "Alert on a single account performing a bulk export from a customer-contact or CRM repository shortly after an interactive sign-in from an unusual location; Odido's operators bulk-downloaded 6.2M records before the account was blocked within the hour."
migrated_from: null
---

Dutch National Police (Team High Tech Crime) announced on 9 July that its investigation into the February 2026 breach of Dutch telecom operator Odido — and its Ben brand — has produced strong indications of Dutch-national involvement, based on forensic voice analysis of a call recorded at the time of the intrusion; police assess the caller as very likely a genuine human speaker (while not fully ruling out synthetic voice) and are publicly appealing for the caller to come forward before the recording is released ([Politie, 2026-07-09](https://www.politie.nl/nieuws/2026/juli/8/onderzoek-naar-hack-odido-wijst-op-mogelijke-betrokkenheid-nederlanders.html); [NOS, 2026-07-09](https://nos.nl/artikel/2622288-bellende-odido-hacker-vermoedelijk-nederlander-politie-dreigt-stem-openbaar-te-maken)).

This extends the ShinyHunters vishing-to-spoofed-portal playbook (registry: `actor:shinyhunters`) already covered in this store to a new victim class — an EU telecommunications operator. The mechanism, confirmed on-record by Odido CEO Tisha van Lammeren, is the same one documented previously: a caller impersonating Odido IT-department staff (`T1684.001`) used a voice-phishing pretext (`T1566.004`) to persuade a customer-service employee to log into a spoofed copy of the corporate work environment, harvesting that employee's real credentials (`T1078`) for the customer-contact system ([NOS, 2026-05-12](https://nos.nl/artikel/2614128-odido-ontdekte-pas-na-bericht-van-hackers-dat-klantgegevens-waren-gestolen)). Odido blocked the account within an hour of noticing the intrusion ([NOS, 2026-05-12](https://nos.nl/artikel/2614128-odido-ontdekte-pas-na-bericht-van-hackers-dat-klantgegevens-waren-gestolen)), but the operators had already bulk-exported 6.2 million customer records (name, address, contact details, customer number, bank account number, date of birth, and passport/driver's-licence numbers) ([NOS, 2026-02-12](https://nos.nl/artikel/2602080-hack-bij-odido-gegevens-miljoenen-klanten-in-handen-van-criminelen)) — the CEO's Dutch quote via NOS: "De hacker wist deze medewerker over te halen om in te loggen op een valse versie van de werkomgeving. Zo heeft hij de inloggegevens van die persoon gestolen" ("the hacker persuaded this employee to log into a fake version of the work environment, and so stole that person's login credentials") (`T1213`). The Dutch Data Protection Authority has two open investigations — into the adequacy of Odido's customer-system security and into whether it retained former-customer data longer than permitted.

**Defender takeaway:** no software vulnerability was involved in this or the earlier tracked case — the single control that breaks the chain is out-of-band callback verification before any credential entry prompted by an inbound "IT" call, and the actor's speed (bulk export before same-day incident response detected the theft) means bulk-read alerting on customer/CRM repositories is the detection worth prioritising. **Triage:** a helpdesk agent logging into an internal portal is routine; the discriminator is a login into a portal reached via a link or address supplied during an inbound call, followed by an out-of-pattern bulk data read from a single session.
