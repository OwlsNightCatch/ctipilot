---
schema: 1
kind: incident
title: >
  France's tax authority cut the intruders' accounts in June and July and found no data theft — it
  took the criminal's sale listing two months later to establish that 678,000 records had already
  gone
headline: >
  DGFiP confirms a 678,000-record theft via a stolen agent account and a third party's credentials
  — missed by its own post-intrusion access checks
summary: >
  France's Direction générale des Finances publiques confirmed on 2026-08-14 that intrusions in
  June and July 2026, using stolen credentials of a DGFiP agent and of an authorised third party,
  were used to view and extract data on 678,000 individuals and businesses. DGFiP cut the accounts
  when it detected the intrusions, but its access reviews at the time did not reveal that data had
  been stolen; only investigations opened after the attacker advertised the dataset on 2026-08-12
  established the theft.
discovered_at: "2026-08-15T04:47:00Z"
updated_at: "2026-08-31T05:55:00Z"
event_date: 2026-08-14
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
  - education
entities:
  - "incident:france-dgfip-tax-breach-2026-08"
  - "actor:zerobytes"
  - "incident:france-education-nationale-agent-training-breach-2026-07"
  - "incident:france-bloctel-breach-2026-08"
techniques:
  - T1078
  - T1199
affected_products: []
cves: []
sources:
  - url: "https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/"
    publisher: "Ministère de l'Économie et des Finances"
    date: 2026-08-14
    role: primary
  - url: "https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885"
    publisher: The Register
    date: 2026-08-14
    role: corroborating
  - url: "https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/zerobytes-a-l-origine-du-vol-de-donnees-du-fisc-revendique-un-piratage-de-donnees-visant-l-education-nationale-fin-juillet_8152235.html"
    publisher: franceinfo
    date: 2026-08-18
    role: primary
  - url: "https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/"
    publisher: "DGCCRF / Ministère de l'Économie et des Finances"
    date: 2026-08-12
    role: primary
  - url: "https://www.occrp.org/en/news/french-authorities-investigate-widespread-government-data-breaches"
    publisher: OCCRP
    date: 2026-08-20
    role: corroborating
  - url: "https://www.zataz.com/cyberattaque-une-rentree-scolaire-sous-tension/"
    publisher: "ZATAZ.COM (Damien Bancal)"
    date: "2026-08-30"
    role: corroborating
  - url: "https://www.radiofrance.fr/francebleu/podcasts/l-invite-ici-mayenne/blocage-des-outils-informatiques-des-professeurs-devraient-manquer-a-l-appel-dans-certaines-classes-selon-le-snes-fsu-6927930"
    publisher: "ICI / France Bleu (Radio France)"
    date: "2026-08-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Mercredi 12 et jeudi 13 août 2026, un acteur malveillant a revendiqué des accès illégitimes au système d'information de la Direction générale des Finances publiques (DGFiP), intervenus en juin et juillet 2026, reposant sur des usurpations d'identifiants d'un agent de la DGFIP et d'un tiers habilité."
    publisher: "Ministère de l'Économie et des Finances"
  - quote: "Néanmoins, les contrôles d'accès réalisés à cette occasion n'ont pas permis de détecter que ces intrusions avaient conduit à des vols de données, en raison de la sophistication de l'attaque."
    publisher: "Ministère de l'Économie et des Finances"
  - quote: "Les données susceptibles d'avoir été exfiltrées concernent les agents du ministère ayant exercé en académie depuis 2001."
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Pour une partie d'entre eux s'y ajoutent des coordonnées, adresse postale et numéro de téléphone, ainsi que le numéro de sécurité sociale"
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Ce système d'information ne contient ni données bancaires, ni mots de passe, ni données relatives aux élèves."
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Un accès frauduleux à un compte professionnel a permis à un cybercriminel de récupérer des fichiers contenant 3 millions de numéros de téléphone, dont 600 000 inscrits sur Bloctel."
    publisher: DGCCRF
  - quote: "Full restoration could take around two weeks."
    original: "Le rétablissement complet pourrait nécessiter environ deux semaines."
    publisher: "ZATAZ.COM"
    source_url: "https://www.zataz.com/cyberattaque-une-rentree-scolaire-sous-tension/"
  - quote: "We risk finding ourselves on 1 September with classes lacking teachers in quite a few schools."
    original: "On risque de se retrouver au 1ᵉʳ septembre avec des classes sans professeurs dans pas mal d'établissements scolaires"
    publisher: "ICI / France Bleu (Radio France)"
    source_url: "https://www.radiofrance.fr/francebleu/podcasts/l-invite-ici-mayenne/blocage-des-outils-informatiques-des-professeurs-devraient-manquer-a-l-appel-dans-certaines-classes-selon-le-snes-fsu-6927930"
verification: multi-source
sourcing_note: >
  The confirmed facts come from the French Ministry of Economy and Finance's own statement about
  its own incident. The attacker's own claims — a dataset of more than two million taxpayers, a
  multi-factor-authentication bypass, and retained access — are assertions reported by the press;
  the government disputed the retained-access claim and its published statement addresses neither
  of the others, and each is attributed to the source that carries it.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-21T06:45:00Z"
    run_id: 2026-08-21T0410Z-intel
    type: update
    summary: >
      ZeroBytes, the actor behind the DGFiP tax-authority intrusion this pipeline covered on
      2026-08-15, publicly claimed on 18 August to have taken 346 million raw lines from France's
      Ministry of National Education. Contacted directly by franceinfo, the minister's office
      confirmed the claim corresponds to the fraudulent intrusion the ministry had already disclosed
      on 31 July, and the ministry's own account of the exposed data adds a detail the earlier
      coverage did not carry: identity and professional information for staff who worked in an
      académie since 2001, with postal address, telephone number and French social-security number for
      a subset. The system holds no banking data, no passwords and no student data, and the ministry
      is continuing technical work on the actor's separate claim to hold student records. Separately,
      a third French government service lost 3 million phone numbers to a fraudulently accessed
      professional account — with no actor named by any source.
    fields:
      - entities
      - evidence
      - references
      - sectors
      - sources
      - body
    merged_from: 2026-08-21/zerobytes-france-education-ministry-bloctel-unattributed
  - at: "2026-08-31T05:55:00Z"
    run_id: 2026-08-31T0411Z-intel
    type: update
    summary: >
      The Ministry of National Education's precautionary access shutdown at affected académies is
      still disrupting the 2026 school-year start more than a month after the intrusion: as of
      2026-08-30, Toulouse and Nantes remain significantly impacted, with professional mailboxes
      and family access to digital workspaces cut and academies falling back to paper and phone
      procedures. Teacher unions warn some classes may begin September without an assigned teacher
      because substitute-assignment orders are sent by email.
    fields: [entities, sources, evidence, body]
migrated_from: null
---

France's Ministry of Economy and Finance confirmed on 2026-08-14 that a malicious actor had obtained illegitimate access to the information system of the Direction générale des Finances publiques — the national tax authority — during June and July 2026, on the basis of credential impersonation of a DGFiP agent and of an authorised third party ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)). Investigations conducted since 2026-08-12 established that before the accesses were cut, they had been used to view and extract data on a total of 678,000 individuals and businesses: tax data including the reference taxable income, the family quotient and the withholding-tax rate, and for companies the registered name and SIREN identifier, along with cadastral data on the addresses and surface areas of properties. DGFiP states that users' own *Espaces Finances publiques* accounts were not compromised, and it notified the CNIL as soon as the data theft was identified ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

The operationally interesting part is the sequence, and it is a failure mode worth copying into a playbook. DGFiP detected the intrusions and immediately cut off every account involved — the containment step worked. But in the ministry's own words, the access reviews carried out at that point did not reveal that the intrusions had led to data theft, which it attributes to the sophistication of the attack. What surfaced the exfiltration was external: an actor using the alias ZeroBytes advertised the dataset on a cybercrime forum on 2026-08-12, and only the deep investigations that followed established the scope ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/) · [The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)). Between containment and discovery lay roughly two months in which the organisation believed it had handled the incident. Two of the actor's claims go further than anything the government confirms, and the gap between them is worth holding onto. ZeroBytes advertised the database as containing details of more than 2 million French taxpayers — against the 678,000 the ministry has established — and claimed the access was obtained using stolen credentials and a multi-factor-authentication bypass technique; it also claimed to retain access to DGFiP's systems and offered to sell that alongside the data ([The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)). DGFiP disputed the claim that ZeroBytes retained access in its statement of the following day ([The Register, 2026-08-14](https://www.theregister.com/security/2026/08/14/french_tax_authority_admits_data_heist_after_crook_touts_2m_records/5287885)); its own published statement addresses neither that claim nor the multi-factor element, and records instead further precautionary cut-offs of access to sensitive information systems while investigations continue to determine the precise nature and volume of extracted data ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

The access path carries no vulnerability: it is a valid agent account plus an authorised external party's credentials, which is the same shape as the compromised professional account at France's Ministère de l'Éducation nationale in July and the external service-provider account at Żabka. DGFiP's teams are working with the ministries' senior defence and security official and with ANSSI, and the authority will file a criminal complaint and contact each affected individual and business directly ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)).

**Defender takeaway:** cutting the compromised accounts is containment, not scoping. When a government record system is reached through valid credentials, the question that decides the incident's real size is what those sessions *read and exported* — bulk-query and export volumes per account, off-hours retrieval patterns, third-party accounts operating outside their normal scope — and that question has to be answered from query and data-access telemetry, not from the access-control review that follows an account takedown. An organisation that only verifies the accounts are closed can close an incident that is still open.

**Triage:** a legitimate tax-administration account queries citizen and business records all day, so record access is not the signal. The discriminators are volume and shape against that account's own baseline — sustained bulk retrieval or export where the role's normal pattern is individual case lookups, activity outside the agent's working hours, and an authorised third-party account reaching record classes its contracted purpose never needed.

## Update — 2026-08-21T06:45:00Z

The earlier entry recorded that France's Direction générale des Finances publiques confirmed intrusions in June and July 2026 using stolen credentials of a DGFiP agent and of an authorised third party, and that only the attacker's sale listing — two months later — established that data on 678,000 individuals and businesses had gone. The delta is that the same actor's footprint now reaches a second French government system, and that the ministry involved has put its own words to what was taken.

**The Education Ministry link.** ZeroBytes claimed on 18 August to have absorbed 346 million raw lines from the Ministry of National Education some weeks earlier, asserting it had been detected but not cut off. Contacted directly by franceinfo, the minister's office confirmed the claim corresponds to the fraudulent intrusion into one of its information systems that the ministry had already announced on 31 July ([franceinfo, 2026-08-18](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/zerobytes-a-l-origine-du-vol-de-donnees-du-fisc-revendique-un-piratage-de-donnees-visant-l-education-nationale-fin-juillet_8152235.html)). The linkage of the two thefts to one actor comes from French media reporting rather than from any authority, and this entry carries it at that weight.

What the ministry itself said about the data is the materially new fact. The information at risk concerns ministry staff who worked in an académie since 2001 — identity elements and professional information, status and functions — and for a portion of them the ministry adds contact details, postal address, telephone number and the French social-security number. It also draws a boundary: that information system contains no banking data, no passwords and no student data. On the actor's separate assertion to hold student records, the ministry's position is that its technical examination continues — pending, not a denial. The social-security-number exposure is the detail this pipeline's DGFiP-only coverage did not carry, and it changes the downstream risk for the affected staff from contactability to identity fraud.

**The third breach, and why it is not part of this story.** In the same period France's consumer-protection directorate disclosed a separate incident: "Un accès frauduleux à un compte professionnel a permis à un cybercriminel de récupérer des fichiers contenant 3 millions de numéros de téléphone, dont 600 000 inscrits sur Bloctel" — a fraudulent access to a professional account let a cybercriminal retrieve files containing 3 million phone numbers, 600,000 of them registered on the Bloctel telemarketing opt-out list ([DGCCRF, 2026-08-12](https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/)). DGCCRF states no personal data such as name or address was disclosed, that the compromised account was blocked as soon as the incident was noticed and all professional accounts subsequently reviewed, and that the Bloctel database itself was not compromised.

It is worth being explicit about what is *not* established, because the opposite was circulating: no source names an actor for Bloctel, and none ties it to ZeroBytes. The "same hacker" claim in international coverage traces, through its own hyperlink, to a French broadcast report that discusses only the tax authority and the Education Ministry ([OCCRP, 2026-08-20](https://www.occrp.org/en/news/french-authorities-investigate-widespread-government-data-breaches)). Nor does any source describe one investigation spanning all three; the national anti-cybercrime unit is placed on the DGFiP breach.

**Triage:** across the intrusions where a mechanism is stated at all, the access is a legitimate account used by someone who should not have it — an agent's and an authorised third party's credentials at DGFiP, a professional account at DGCCRF. There is no malware, no exploited vulnerability and no CVE anywhere in this cluster, so nothing here produces a detection signal on an endpoint. The discriminator is behavioural on the identity plane: a valid account performing bulk record retrieval at a volume and rate no human workflow generates, from a session that is otherwise unremarkable. The DGFiP case established the harder half of the problem — its own post-intrusion access reviews, run when the accounts were cut, did not reveal that data had already been taken. The Education Ministry case adds the same shape from the other side: the actor's claim to have been detected without being evicted is unaddressed by the ministry's published statements.

**Defender takeaway:** for an administration whose exposure runs through authorised third parties, the control this cluster keeps pointing at is not authentication but **egress volume accounting on legitimate sessions** — knowing what a normal day's record access looks like per account and per third-party integration, so that a bulk export is visible while it happens rather than when a listing appears for sale. Two months elapsed between the DGFiP intrusions and the discovery that data had gone, and the discovery came from the criminal market, not from the victim. Where a third-party account holds query access to a personal-data system, the reviewable question is whether anyone would notice that account reading a hundred thousand records, and the honest answer in three separate French cases this summer was no.

## Update — 2026-08-31T05:55:00Z

The delta here is operational, not technical. The Ministry of National Education's precautionary decision to cut network and mailbox access for affected académies, taken after the intrusion this entry already tracks, is still causing real disruption to the 2026 school-year start more than a month later. As of 2026-08-30, most académies report normal access restored, but Toulouse and Nantes remain significantly impacted: at Toulouse, professional mailboxes and applications stay cut "until further notice," family access to the digital workspace is also suspended, the rector describes it as an unprecedented start of term, and "full restoration could take around two weeks" — all translated from French ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/cyberattaque-une-rentree-scolaire-sous-tension/)) — with the digital workspace targeted for relaunch on 7 September. Because substitute-teacher assignment orders are sent by email, the mailbox shutdown has left some substitute and contract teachers without their assigned school days before term starts; teacher unions warn some classes may open in September with no assigned teacher: "we risk finding ourselves on 1 September with classes lacking teachers in quite a few schools" (translated from French) ([Thomas Cabioch, SNES-FSU Mayenne, via ICI/France Bleu, 2026-08-26](https://www.radiofrance.fr/francebleu/podcasts/l-invite-ici-mayenne/blocage-des-outils-informatiques-des-professeurs-devraient-manquer-a-l-appel-dans-certaines-classes-selon-le-snes-fsu-6927930)). Toulouse has fallen back to paper timetables and phone or messaging-app communication with families ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/cyberattaque-une-rentree-scolaire-sous-tension/)). The ministry states payroll will still be paid on the usual schedule, and the Toulouse rector separately states all students will be accommodated in schools on the planned dates, allowing for possible last-minute adjustments — both translated from French ([ZATAZ.COM, 2026-08-30](https://www.zataz.com/cyberattaque-une-rentree-scolaire-sous-tension/)).

**Defender takeaway:** a precautionary, security-driven access shutdown following a breach can itself become the primary operational-impact event, particularly where downstream HR and scheduling workflows — payroll routing, staff assignment, credential issuance — have no offline fallback built in. That is a business-continuity gap worth stress-testing before an incident forces the exercise, not during one: identify which HR and scheduling processes depend on email or a single digital workspace with no manual fallback, and pre-stage the paper or phone alternative for exactly the window between detection and full restoration.
