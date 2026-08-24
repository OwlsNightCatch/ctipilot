---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — the actor behind France's tax-authority theft is linked by media reporting to the Education Ministry intrusion the ministry disclosed on 31 July, and social-security numbers were in scope for a subset of staff"
headline: "**ZeroBytes tied to a second French government system** — the ministry confirms the claim matches its own July disclosure"
summary: >
  ZeroBytes, the actor behind the DGFiP tax-authority intrusion this pipeline covered on 2026-08-15, publicly claimed
  on 18 August to have taken 346 million raw lines from France's Ministry of National Education. Contacted directly by
  franceinfo, the minister's office confirmed the claim corresponds to the fraudulent intrusion the ministry had
  already disclosed on 31 July, and the ministry's own account of the exposed data adds a detail the earlier coverage
  did not carry: identity and professional information for staff who worked in an académie since 2001, with postal
  address, telephone number and French social-security number for a subset. The system holds no banking data, no
  passwords and no student data, and the ministry is continuing technical work on the actor's separate claim to hold
  student records. Separately, a third French government service lost 3 million phone numbers to a fraudulently
  accessed professional account — with no actor named by any source.
discovered_at: "2026-08-21T06:45:00Z"
event_date: "2026-08-18"
run_id: 2026-08-21T0410Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity]
regions: [europe]
sectors: [public-sector, education]
entities: [actor:zerobytes, incident:france-dgfip-tax-breach-2026-08, incident:france-education-ministry-breach-2026-07, incident:france-bloctel-breach-2026-08]
techniques: [T1078]
affected_products: []
cves: []
sources:
  - url: "https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/zerobytes-a-l-origine-du-vol-de-donnees-du-fisc-revendique-un-piratage-de-donnees-visant-l-education-nationale-fin-juillet_8152235.html"
    publisher: "franceinfo"
    date: "2026-08-18"
    role: primary
  - url: "https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/"
    publisher: "DGCCRF / Ministère de l'Économie et des Finances"
    date: "2026-08-12"
    role: primary
  - url: "https://www.occrp.org/en/news/french-authorities-investigate-widespread-government-data-breaches"
    publisher: "OCCRP"
    date: "2026-08-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Les données susceptibles d'avoir été exfiltrées concernent les agents du ministère ayant exercé en académie depuis 2001."
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Pour une partie d'entre eux s'y ajoutent des coordonnées, adresse postale et numéro de téléphone, ainsi que le numéro de sécurité sociale"
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Ce système d'information ne contient ni données bancaires, ni mots de passe, ni données relatives aux élèves."
    publisher: "Ministère de l'Education nationale, quoted by franceinfo"
  - quote: "Un accès frauduleux à un compte professionnel a permis à un cybercriminel de récupérer des fichiers contenant 3 millions de numéros de téléphone, dont 600 000 inscrits sur Bloctel."
    publisher: "DGCCRF"
verification: multi-source
sourcing_note: >
  Three first-party or near-first-party sources, each authoritative for a different part of this: the Education
  Ministry's own office speaking to franceinfo, DGCCRF's own press release for the Bloctel breach, and OCCRP relaying
  French media reporting. Two corrections to what was circulating, both established by tracing the citation chain
  rather than accepting the summary. First, **no source attributes the Bloctel breach to ZeroBytes.** OCCRP's
  "same hacker" sentence is hyperlinked to an RTL report, and that report covers only DGFiP and the Education
  Ministry; its Bloctel paragraph links to DGCCRF's release, which names no actor at all. Second, **no source states a
  single investigation spanning all three intrusions** — OCCRP places the national anti-cybercrime unit on the DGFiP
  breach specifically. Both claims were in circulation and are not carried here. Note also that the actor link for the
  Education Ministry rests on media reporting plus the ministry confirming the claim matches its own disclosure, not
  on an attribution by any authority; and that the ministry's posture on the student-data claim is pending technical
  work rather than a denial. The ATT&CK mapping is scoped in the body: valid-account abuse is DGCCRF's own
  characterisation for Bloctel and was established for DGFiP in the earlier entry, but **no source states an access
  mechanism for the Education Ministry intrusion**, and none is assumed for it.
confidence: high
update_of: 2026-08-15/france-dgfip-tax-authority-credential-intrusion
references: ["2026-08-16/weekly-w33-compromised-party-was-not-the-notifying-party"]
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

**UPDATE (originally covered 2026-08-15):** the earlier entry recorded that France's Direction générale des Finances publiques confirmed intrusions in June and July 2026 using stolen credentials of a DGFiP agent and of an authorised third party, and that only the attacker's sale listing — two months later — established that data on 678,000 individuals and businesses had gone. The delta is that the same actor's footprint now reaches a second French government system, and that the ministry involved has put its own words to what was taken.

**The Education Ministry link.** ZeroBytes claimed on 18 August to have absorbed 346 million raw lines from the Ministry of National Education some weeks earlier, asserting it had been detected but not cut off. Contacted directly by franceinfo, the minister's office confirmed the claim corresponds to the fraudulent intrusion into one of its information systems that the ministry had already announced on 31 July ([franceinfo, 2026-08-18](https://www.franceinfo.fr/internet/securite-sur-internet/cyberattaques/zerobytes-a-l-origine-du-vol-de-donnees-du-fisc-revendique-un-piratage-de-donnees-visant-l-education-nationale-fin-juillet_8152235.html)). The linkage of the two thefts to one actor comes from French media reporting rather than from any authority, and this entry carries it at that weight.

What the ministry itself said about the data is the materially new fact. The information at risk concerns ministry staff who worked in an académie since 2001 — identity elements and professional information, status and functions — and for a portion of them the ministry adds contact details, postal address, telephone number and the French social-security number. It also draws a boundary: that information system contains no banking data, no passwords and no student data. On the actor's separate assertion to hold student records, the ministry's position is that its technical examination continues — pending, not a denial. The social-security-number exposure is the detail this pipeline's DGFiP-only coverage did not carry, and it changes the downstream risk for the affected staff from contactability to identity fraud.

**The third breach, and why it is not part of this story.** In the same period France's consumer-protection directorate disclosed a separate incident: "Un accès frauduleux à un compte professionnel a permis à un cybercriminel de récupérer des fichiers contenant 3 millions de numéros de téléphone, dont 600 000 inscrits sur Bloctel" — a fraudulent access to a professional account let a cybercriminal retrieve files containing 3 million phone numbers, 600,000 of them registered on the Bloctel telemarketing opt-out list ([DGCCRF, 2026-08-12](https://presse.economie.gouv.fr/la-dgccrf-met-en-garde-les-consommateurs-a-la-suite-dune-fuite-de-donnees-sur-bloctel/)). DGCCRF states no personal data such as name or address was disclosed, that the compromised account was blocked as soon as the incident was noticed and all professional accounts subsequently reviewed, and that the Bloctel database itself was not compromised.

It is worth being explicit about what is *not* established, because the opposite was circulating: no source names an actor for Bloctel, and none ties it to ZeroBytes. The "same hacker" claim in international coverage traces, through its own hyperlink, to a French broadcast report that discusses only the tax authority and the Education Ministry ([OCCRP, 2026-08-20](https://www.occrp.org/en/news/french-authorities-investigate-widespread-government-data-breaches)). Nor does any source describe one investigation spanning all three; the national anti-cybercrime unit is placed on the DGFiP breach.

**Triage:** across the intrusions where a mechanism is stated at all, the access is a legitimate account used by someone who should not have it — an agent's and an authorised third party's credentials at DGFiP, a professional account at DGCCRF. There is no malware, no exploited vulnerability and no CVE anywhere in this cluster, so nothing here produces a detection signal on an endpoint. The discriminator is behavioural on the identity plane: a valid account performing bulk record retrieval at a volume and rate no human workflow generates, from a session that is otherwise unremarkable. The DGFiP case established the harder half of the problem — its own post-intrusion access reviews, run when the accounts were cut, did not reveal that data had already been taken. The Education Ministry case adds the same shape from the other side: the actor's claim to have been detected without being evicted is unaddressed by the ministry's published statements.

**Defender takeaway:** for an administration whose exposure runs through authorised third parties, the control this cluster keeps pointing at is not authentication but **egress volume accounting on legitimate sessions** — knowing what a normal day's record access looks like per account and per third-party integration, so that a bulk export is visible while it happens rather than when a listing appears for sale. Two months elapsed between the DGFiP intrusions and the discovery that data had gone, and the discovery came from the criminal market, not from the victim. Where a third-party account holds query access to a personal-data system, the reviewable question is whether anyone would notice that account reading a hundred thousand records, and the honest answer in three separate French cases this summer was no.
