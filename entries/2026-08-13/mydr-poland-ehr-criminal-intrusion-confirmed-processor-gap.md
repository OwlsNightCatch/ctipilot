---
schema: 1
kind: incident
horizon: operational
title: "MyDr, a Polish electronic health record platform serving thousands of clinics, confirms a deliberate criminal intrusion — and because it is a processor, not a controller, the people affected cannot be told directly"
headline: "A Polish health-records processor confirms an intrusion, and because it is not the data controller it cannot tell the affected people"
summary: >
  MyDr, one of Poland's largest electronic medical record providers, confirmed on 2026-08-12 that it was
  the target of a deliberate external criminal act affecting part of its data, saying the data is likely
  historical (2024 and earlier) and that it cannot yet state what was taken. Attackers who approached
  Polish outlet Zaufana Trzecia Strona claim 18,814,422 unique PESEL national identity numbers and 2.5 TB
  of data, and describe an access chain the outlet could not independently verify: remote code execution
  through an XXE flaw in PKCS#12 certificate handling, a GitHub API key, source code, then AWS. The
  transferable finding is structural: MyDr is a GDPR processor and the controllers are thousands of
  individual healthcare facilities, so affected individuals cannot be notified centrally and must wait
  for their own clinic.
discovered_at: "2026-08-13T05:05:00Z"
event_date: "2026-08-12"
run_id: 2026-08-13T0412Z-intel
priority: high
immediate_action: null
tags: [data-breach, organized-crime]
regions: [europe]
sectors: [healthcare, public-sector]
entities: [incident:mydr-poland-ehr-breach-2026]
techniques: [T1190, T1552.001, T1078.004, T1213]
affected_products: []
cves: []
sources:
  - url: "https://pro.mydr.pl/portal-info"
    publisher: "MyDr (company incident statement)"
    date: "2026-08-12"
    role: primary
  - url: "https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/"
    publisher: "Zaufana Trzecia Strona"
    date: "2026-08-10"
    role: primary
  - url: "https://databreaches.net/2026/08/12/a-serious-incident-occurred-at-mydr-a-polish-healthcare-system-provider/"
    publisher: "DataBreaches.net"
    date: "2026-08-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Na tym etapie trwającego dochodzenia potwierdzamy, że staliśmy się celem zewnętrznego, celowego działania o charakterze przestępczym, którym objęta była część danych."
    publisher: "MyDr (company incident statement)"
  - quote: "Według tego, co usłyszeliśmy od sprawców, najpierw udało im się uzyskać zdalne wykonanie kodu przez podatność typu XXE przy obsłudze certyfikatów PKCS#12."
    publisher: "Zaufana Trzecia Strona"
  - quote: "Nie byliśmy w stanie niezależnie zweryfikować tych informacji."
    publisher: "Zaufana Trzecia Strona"
  - quote: "MyDr jest jedynie \"podmiotem przetwarzającym\" zgodnie z RODO, a administratorem danych są placówki ochrony zdrowia, których są tysiące."
    publisher: "Zaufana Trzecia Strona"
verification: multi-source
sourcing_note: >
  Two independent primaries: MyDr's own statement for what the company confirms, and Zaufana Trzecia
  Strona for the attackers' claims and the outlet's own verification work. The scale figures, the
  2.5 TB volume and the entire access chain are the attackers' account relayed by the outlet, which
  states explicitly that it could not independently verify them; they are attributed as claims
  throughout and never as fact. The outlet's partial verification — matching records for three of five
  volunteered identity numbers, and a correct date of birth, identity number and phone number for a
  named politician — supports plausibility of scope, not the total. Source titles are Polish; quotes are
  reproduced in the original with English glosses in the body.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

MyDr serves thousands of Polish healthcare facilities and, on figures the company itself gives, processes three million appointments and 2.7 million prescriptions a month ([Zaufana Trzecia Strona, 2026-08-10](https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/)). It published an incident statement updated 2026-08-12 at 18:35 CET confirming an intrusion: "Na tym etapie trwającego dochodzenia potwierdzamy, że staliśmy się celem zewnętrznego, celowego działania o charakterze przestępczym, którym objęta była część danych" — at this stage of the ongoing investigation we confirm that we became the target of an external, deliberate act of a criminal nature, which covered part of the data ([MyDr, 2026-08-12](https://pro.mydr.pl/portal-info)). The company states the affected data is most likely historical, from 2024 and earlier, and may not cover all MyDr clients or all their patients; that its systems are fully operational and safe to use; that its cybersecurity partners monitoring the dark web have found no evidence the data has been published or shared publicly; and that it cannot yet confirm the quantity and type of data disclosed until forensic analysis completes ([MyDr, 2026-08-12](https://pro.mydr.pl/portal-info)).

The claims that prompted the statement are considerably larger. People presenting themselves as the perpetrators contacted Polish security journalist Adam Haertle before the disclosure and said they hold 18,814,422 unique PESEL national identity numbers and 2.5 TB of data ([Zaufana Trzecia Strona, 2026-08-10](https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/)). The outlet's verification is careful and worth reading as a method rather than a verdict: it was sent a database record for a senior Polish politician whose date of birth, identity number, name and one of two phone numbers it independently confirmed, along with the correct national health-fund region; it asked the claimants to look up the identity numbers of four industry volunteers and received records for two, which with the author's own record makes three matches out of five checked. The outlet states it caught the claimants in no inconsistency within what it could check, while being explicit that its checking ability is limited and that it has no way to verify either the 2.5 TB volume or the 18-million figure — though it observes that the figure is consistent with the potential reach of a system serving thousands of practices. It also records that Gawkowski, whom it names as premier, wrote publicly that much suggests an unauthorised person may have gained access to the data.

**The access chain is a lead, not a finding.** Per the claimants' own account, they first obtained remote code execution through an XXE-class flaw in the handling of PKCS#12 certificates — "Według tego, co usłyszeliśmy od sprawców, najpierw udało im się uzyskać zdalne wykonanie kodu przez podatność typu XXE przy obsłudze certyfikatów PKCS#12" — which yielded a GitHub API key, from there the platform's source code, and from there the AWS infrastructure. The outlet's next sentence is the one that governs how this should be read: "Nie byliśmy w stanie niezależnie zweryfikować tych informacji" — we were not able to independently verify this information ([Zaufana Trzecia Strona, 2026-08-10](https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/)). MyDr says it cannot share technical details while the investigation runs. No CVE exists and no vendor has confirmed a vulnerability class; treat the chain as an unverified attacker narrative that is nonetheless a reasonable thing to check for in your own certificate-parsing paths.

The extortion mechanics are documented more solidly, because the outlet handled the artefacts. The claimants sent the company's chief executive a message on 5 August linking to a PDF that was supposed to self-delete after download and did not; the file was password-protected, and the claimants noted the password was the executive's own PESEL number — which the outlet points out is a low-entropy value and therefore no obstacle. The document framed the approach as an offer to purchase the results of a security audit, and contained internal corporate correspondence including personnel information and a whistleblower report, alongside a fragment of the company's partner-doctor database. The claimants also showed a message sent to company employees from the company's own bulk-SMS account, and named Jira and a HubSpot CRM among systems they say they reached in full ([Zaufana Trzecia Strona, 2026-08-10](https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/)). On attribution the outlet is deliberately unhelpful in the right way: the claimants write in English, use a Russian-style emoticon convention, and produce English that reads as though deliberately rewritten to imitate a non-native speaker from elsewhere — which it reads as an attempt to lay false trails.

**The structural finding, and the reason this matters beyond Poland.** MyDr cannot tell affected people they are affected. "MyDr jest jedynie "podmiotem przetwarzającym" zgodnie z RODO, a administratorem danych są placówki ochrony zdrowia, których są tysiące" — MyDr is only a processor under GDPR, and the controllers are the healthcare facilities, of which there are thousands ([Zaufana Trzecia Strona, 2026-08-10](https://zaufanatrzeciastrona.pl/post/hakerzy-twierdza-ze-ukradli-dane-ponad-18-milionow-polek-i-polakow-z-firmy-mydr/)). The outlet's assessment is that individuals therefore have no way to check their own exposure and must wait for MyDr to determine scope, notify each facility, and for each facility to notify its own patients — a chain it expects to take many days. MyDr's own statement is consistent with this: it says it will contact affected clients proactively once it establishes which facilities and which data are involved, will support them in reporting to the data-protection authorities and in patient communication, and that no reports from facilities are required at present.

**Defender takeaway:** the operational lesson here is not a vulnerability, it is a notification topology, and every organisation that buys a shared sector platform inherits it. When the platform is the processor and each customer is the controller, the platform is legally the only party that knows the scope and legally not the party that can tell the affected people — so the elapsed time between "the processor knows" and "our people are told" is set by how fast the processor reaches *us*, and how prepared we are to act on what it sends. For a Swiss or European public-sector body running a shared health, education or administrative platform, the question worth answering before an incident is which side of that line each supplier sits on, and what the contractual clock is for the supplier to notify the controller — because the incident response you can actually run starts when that message arrives, not when the intrusion happens.
