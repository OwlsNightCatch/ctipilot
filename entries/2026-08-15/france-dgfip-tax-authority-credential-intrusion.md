---
schema: 1
kind: incident
horizon: operational
title: "France's tax authority cut the intruders' accounts in June and July and found no data theft — it took the criminal's sale listing two months later to establish that 678,000 records had already gone"
headline: "DGFiP confirms a 678,000-record theft via a stolen agent account and a third party's credentials — missed by its own post-intrusion access checks"
summary: >
  France's Direction générale des Finances publiques confirmed on 2026-08-14 that intrusions in June and July
  2026, using stolen credentials of a DGFiP agent and of an authorised third party, were used to view and extract
  data on 678,000 individuals and businesses. DGFiP cut the accounts when it detected the intrusions, but its
  access reviews at the time did not reveal that data had been stolen; only investigations opened after the
  attacker advertised the dataset on 2026-08-12 established the theft.
discovered_at: "2026-08-15T04:47:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: high
immediate_action: null
tags:
  - data-breach
  - identity
  - organized-crime
regions:
  - europe
sectors:
  - public-sector
entities:
  - incident:france-dgfip-tax-breach-2026-08
  - actor:zerobytes
techniques: [T1078, T1199]
affected_products: []
cves: []
sources:
  - url: "https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/"
    publisher: "Ministère de l'Économie et des Finances"
    date: "2026-08-14"
    role: primary
  - url: "https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885"
    publisher: The Register
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Mercredi 12 et jeudi 13 août 2026, un acteur malveillant a revendiqué des accès illégitimes au système d'information de la Direction générale des Finances publiques (DGFiP), intervenus en juin et juillet 2026, reposant sur des usurpations d'identifiants d'un agent de la DGFIP et d'un tiers habilité."
    publisher: "Ministère de l'Économie et des Finances"
  - quote: "Néanmoins, les contrôles d'accès réalisés à cette occasion n'ont pas permis de détecter que ces intrusions avaient conduit à des vols de données, en raison de la sophistication de l'attaque."
    publisher: "Ministère de l'Économie et des Finances"
verification: multi-source
sourcing_note: >
  The confirmed facts come from the French Ministry of Economy and Finance's own statement about its own
  incident. The attacker's own claims — a dataset of more than two million taxpayers, a
  multi-factor-authentication bypass, and retained access — are assertions reported by the press; the government
  disputed the retained-access claim and its published statement addresses neither of the others, and each is
  attributed to the source that carries it.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

France's Ministry of Economy and Finance confirmed on 2026-08-14 that a malicious actor had obtained illegitimate access to the information system of the Direction générale des Finances publiques — the national tax authority — during June and July 2026, on the basis of credential impersonation of a DGFiP agent and of an authorised third party ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)). Investigations conducted since 2026-08-12 established that before the accesses were cut, they had been used to view and extract data on a total of 678,000 individuals and businesses: tax data including the reference taxable income, the family quotient and the withholding-tax rate, and for companies the registered name and SIREN identifier, along with cadastral data on the addresses and surface areas of properties. DGFiP states that users' own *Espaces Finances publiques* accounts were not compromised, and it notified the CNIL as soon as the data theft was identified ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

The operationally interesting part is the sequence, and it is a failure mode worth copying into a playbook. DGFiP detected the intrusions and immediately cut off every account involved — the containment step worked. But in the ministry's own words, the access reviews carried out at that point did not reveal that the intrusions had led to data theft, which it attributes to the sophistication of the attack. What surfaced the exfiltration was external: an actor using the alias ZeroBytes advertised the dataset on a cybercrime forum on 2026-08-12, and only the deep investigations that followed established the scope ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/) · [The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)). Between containment and discovery lay roughly two months in which the organisation believed it had handled the incident. Two of the actor's claims go further than anything the government confirms, and the gap between them is worth holding onto. ZeroBytes advertised the database as containing details of more than 2 million French taxpayers — against the 678,000 the ministry has established — and claimed the access was obtained using stolen credentials and a multi-factor-authentication bypass technique; it also claimed to retain access to DGFiP's systems and offered to sell that alongside the data ([The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)). DGFiP disputed the claim that ZeroBytes retained access in its statement of the following day ([The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)); its own published statement addresses neither that claim nor the multi-factor element, and records instead further precautionary cut-offs of access to sensitive information systems while investigations continue to determine the precise nature and volume of extracted data ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

The access path carries no vulnerability: it is a valid agent account plus an authorised external party's credentials, which is the same shape as the compromised professional account at France's Ministère de l'Éducation nationale in July and the external service-provider account at Żabka. DGFiP's teams are working with the ministries' senior defence and security official and with ANSSI, and the authority will file a criminal complaint and contact each affected individual and business directly ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

**Defender takeaway:** cutting the compromised accounts is containment, not scoping. When a government record system is reached through valid credentials, the question that decides the incident's real size is what those sessions *read and exported* — bulk-query and export volumes per account, off-hours retrieval patterns, third-party accounts operating outside their normal scope — and that question has to be answered from query and data-access telemetry, not from the access-control review that follows an account takedown. An organisation that only verifies the accounts are closed can close an incident that is still open.

**Triage:** a legitimate tax-administration account queries citizen and business records all day, so record access is not the signal. The discriminators are volume and shape against that account's own baseline — sustained bulk retrieval or export where the role's normal pattern is individual case lookups, activity outside the agent's working hours, and an authorised third-party account reaching record classes its contracted purpose never needed.
