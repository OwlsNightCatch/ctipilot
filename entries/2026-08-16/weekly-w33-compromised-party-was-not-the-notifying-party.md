---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: "A third party was on the access path or holding the data in all six European public-sector and critical-infrastructure disclosures this week — and where the third party held the data, the duty to notify landed on organisations with no facts to write"
headline: "W33's European breaches all ran through a third party, and in two of them the notification duty landed where the intrusion did not"
summary: >
  Six European disclosures across 2026-W33 share a structure rather than a sector: in each, a supplier,
  processor or contractor sat either on the access path into the victim or in possession of the data — and
  in two of them that displaced the duty to tell the affected people onto organisations that had no facts
  to write. Poland's MyDr, an electronic health record platform, confirmed a criminal intrusion
  reported at nearly 19 million people, and the data-protection authority confirmed that because
  MyDr is a processor the notification duty rests with the roughly 12,000 clinics that used it. One
  intrusion at CEVA Logistics put ten organisations into breach reporting with the Dutch regulator at once.
  France's tax authority was reached partly through an authorised third party's credentials. Retelit, an
  Italian operator serving 193 public administrations, disclosed only in a right-of-reply after a press
  investigation. Żabka's intrusion came through an external service provider's account. And the UK's
  Information Commissioner reprimanded the national criminal-records office for contracting patch management
  out without establishing who internally owned it.
discovered_at: "2026-08-16T23:56:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T2315Z-weekly
priority: high
immediate_action: null
tags: [data-breach, supply-chain, ransomware, identity]
regions: [europe, switzerland]
sectors: [public-sector, healthcare, transport, telco, finance]
entities:
  - incident:mydr-poland-ehr-breach-2026
  - incident:ceva-logistics-fulfilment-breach-2026-08
  - incident:france-dgfip-tax-breach-2026-08
  - incident:retelit-qilin-2026
  - actor:qilin
  - incident:zabka-supplier-account-jira-gitlab-secrets-2026-07
  - incident:acro-criminal-records-office-cms-breach-2022
techniques: [T1199, T1078, T1078.004, T1213, T1005, T1190]
affected_products: []
cves: []
sources:
  - url: "https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/"
    publisher: "Notes from Poland"
    date: "2026-08-13"
    role: primary
  - url: "https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html"
    publisher: "Gazeta Prawna"
    date: "2026-08-13"
    role: primary
  - url: "https://pro.mydr.pl/portal-info"
    publisher: "MyDr (company incident statement)"
    date: "2026-08-12"
    role: primary
  - url: "https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/"
    publisher: "TechCrunch"
    date: "2026-08-10"
    role: primary
  - url: "https://partnerplatform.bol.com/en/nadp/security-incident-logistics-partner-of-bol"
    publisher: "bol.com"
    date: "2026-08-06"
    role: primary
  - url: "https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/"
    publisher: "Ministère de l'Économie et des Finances"
    date: "2026-08-14"
    role: primary
  - url: "https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/"
    publisher: "IrpiMedia"
    date: "2026-08-04"
    role: primary
  - url: "https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/08/acro-reprimanded-following-cyber-security-failings/"
    publisher: "UK Information Commissioner's Office"
    date: "2026-08-12"
    role: primary
  - url: "https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/"
    publisher: "Niebezpiecznik"
    date: "2026-08-03"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: >
  Each incident rests on its own disclosing party or its own regulator: MyDr's company statement and the
  Polish data-protection authority's position as reported by Gazeta Prawna and Notes from Poland; bol.com's
  own customer notice and TechCrunch's reporting for CEVA Logistics; the French finance ministry's press
  release for DGFiP; IrpiMedia's investigation and Retelit's right-of-reply; the ICO's own reprimand notice
  for ACRO; Polish outlets for Żabka's written statement. The MyDr scale figure is the reporting outlets'
  own, not a company or forensic finding and not a ministerial statement — the minister is quoted on the
  incident's significance rather than its size — and MyDr itself states it cannot yet say what was taken. The notification duty is displaced in two cases, MyDr and CEVA — and through CEVA it
  reaches bol.com and nine other clients; in the DGFiP, Żabka, Retelit and ACRO cases the compromised body is
  also the notifying body, and the third party sits on the access path or owns the outsourced control instead.
confidence: high
update_of: null
references:
  - 2026-08-13/mydr-poland-ehr-criminal-intrusion-confirmed-processor-gap
  - 2026-08-15/mydr-poland-19-million-records-government-confirmed
  - 2026-08-11/ceva-logistics-fulfilment-breach-ten-controllers-notified
  - 2026-08-15/france-dgfip-tax-authority-credential-intrusion
  - 2026-08-10/retelit-qilin-italian-telco-cloud-operator-public-sector
  - 2026-08-10/zabka-supplier-account-jira-access-confirmed
  - 2026-08-13/ico-acro-reprimand-patch-ownership-gap-segmentation
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

A prior weekly recorded European government's own operating infrastructure being compromised directly. This week the shape is different and, for planning purposes, harder: in all six of the week's European public-sector and critical-infrastructure disclosures a third party stood somewhere on the line — supplying the credentials the intruder used, holding the data that was taken, or owning the security work that was not done. In two of them that separation ran all the way to the notification, so the organisation that knows what happened and the organisation that owes an answer are not the same body.

Poland supplies the extreme case. MyDr, one of the country's largest electronic medical record providers, confirmed on 12 August that it was the target of a deliberate external criminal act, said the data is likely historical, and stated it cannot yet say what was taken ([MyDr, 2026-08-12](https://pro.mydr.pl/portal-info)). The following day the theft was reported at almost 19 million patients' data, with Poland's digital affairs minister Krzysztof Gawkowski quoted calling it one of the largest incidents in the country's history ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/)); Gazeta Prawna puts the stolen database at over 2 TB ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html)), and the data-protection authority UODO stated that the obligation to notify affected individuals rests with the healthcare controllers that used MyDr's services ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html)) — around 12,000 medical facilities ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/)). That is not a technicality. It means the single organisation that knows what happened has no duty to tell anyone, and the twelve thousand organisations that have the duty know only what they read in the press. The same structure produced a smaller, cleaner illustration in the Netherlands: one intrusion at CEVA Logistics, the contract-logistics arm of CMA CGM, generated breach reports to the Dutch data-protection authority from ten separate organisations, because CEVA processes fulfilment data on behalf of unrelated clients ([TechCrunch, 2026-08-10](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)); bol.com, one of them, told its own partners that two order-processing systems at one fulfilment centre were involved and that customer data may have been viewed or copied ([bol.com, 2026-08-06](https://partnerplatform.bol.com/en/nadp/security-incident-logistics-partner-of-bol)).

Where the third party is on the access path rather than the data path, the same asymmetry shows up as a detection problem. France's Direction générale des Finances publiques confirmed that intrusions in June and July used the stolen credentials of a DGFiP agent *and* of an authorised third party, and were used to view and extract data on 678,000 individuals and businesses ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)). Żabka's confirmed intrusion reached its ticketing system through an external service provider's account ([Niebezpiecznik, 2026-08-03](https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/)). Retelit, one of Italy's largest business telecommunications and cloud operators, was compromised on 8 June in an extortion attack claimed by Qilin, and made no announcement through its own channels — the confirmation came as a right-of-reply after IrpiMedia published, scoping the damage to virtualisation infrastructure in three of its 38 data centres, one of them the site certified for Retelit's own backup and service continuity ([IrpiMedia, 2026-08-04](https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/)). Retelit serves 193 public administrations; those customers learned about a two-month-old intrusion from a newspaper.

The week's regulator supplied the governance version of the same gap, and it is the most directly usable finding here. The UK Information Commissioner's Office reprimanded ACRO Criminal Records Office on 12 August after an intruder held access to its public website and content management system from August 2022 to March 2023 and staged the data of up to 10,920 people for theft. The ICO's stated cause is not a technology failure: ACRO had contracted patch management to third parties without establishing who internally was responsible for identifying and monitoring critical updates, and did not adequately investigate security alerts that would have surfaced the intrusion earlier. The ICO also names network segmentation among the mitigating factors it weighed, because it kept the attacker out of core systems ([UK Information Commissioner's Office, 2026-08-12](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/08/acro-reprimanded-following-cyber-security-failings/)).

**Defender takeaway:** the transferable lesson is that outsourcing an activity does not outsource the accountability for it, and this week a regulator said so in a published enforcement action against a government body. Two concrete implications for a public-sector estate. First, on the response side: for every processor holding your data, the question worth answering before an incident is who notifies, on whose determination, and with what information — because the MyDr case shows the controller can be left owing a notification it has no facts to write. Second, on the detection side: the DGFiP and Żabka intrusions both entered on legitimate third-party credentials, which produce no exploit, no malware and no anomaly in a vulnerability-centric monitoring programme; the observable is the account behaviour, and third-party and service-provider accounts are the ones most likely to sit outside both the joiner-mover-leaver process and the baseline that would make deviation visible. The ACRO reprimand names the specific governance artefact that closes the first-order version of this: a named internal owner for each security activity performed by a supplier, responsible for confirming it happened.

**Triage:** third-party account misuse is hard to separate from third-party account use, and the discriminators are contextual rather than atomic. A supplier or contractor account is defined by a narrow, repetitive and scheduled access pattern — a fixed set of systems, a working-hours profile matching the supplier's own jurisdiction, a stable set of source addresses belonging to the supplier's estate. The signals worth alerting on are deviations from that shape rather than the access itself: authentication from a network range with no prior relationship to that supplier, access to systems outside the contracted scope, use of the platform's own bulk export or reporting functions by an account that has never used them before, and activity continuing outside the contract's active periods. The DGFiP case adds the timing discriminator that matters most for scoping: the account was cut when the intrusion was detected, and the theft had already happened — so the review that establishes impact has to reconstruct what the account reached before containment, not merely confirm it stopped afterwards.
