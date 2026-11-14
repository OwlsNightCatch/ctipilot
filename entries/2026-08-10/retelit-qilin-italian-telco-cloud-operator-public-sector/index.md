---
schema: 1
kind: incident
title: "Qilin compromised Italian telecommunications and cloud operator Retelit on 8 June — the company confirmed it only after an investigation forced the question, and one of the three affected data centres was its certified backup site"
headline: "A European carrier serving 193 public administrations disclosed a two-month-old Qilin intrusion in a right-of-reply, not a press release"
summary: >
  IrpiMedia reported on 2026-08-04 that Retelit, one of Italy's largest business telecommunications
  and cloud operators, had been compromised in an extortion attack claimed by Qilin, with roughly
  270,000 files listed on the leak site and an estimated 300 GB published across two dumps. Retelit
  made no announcement through its own channels; after the article ran it sent the outlet a
  right-of-reply confirming an 8 June 2026 attack attributed to Qilin, notified to Italy's national
  cybersecurity agency, CSIRT-ITA, the postal police and the data-protection authority, and scoping
  the damage to virtualisation infrastructure in 3 of its 38 national data centres, around 7% of
  distributed systems. IrpiMedia names those three as Verona, Rome and Milan — Milan being the site
  certified for Retelit's own backup and service continuity — and reports customers complaining of
  backup-recovery failure.
discovered_at: "2026-08-10T05:55:00Z"
event_date: "2026-06-08"
run_id: 2026-08-10T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, data-breach, supply-chain, organized-crime, cloud]
regions: [europe]
sectors: [telco, public-sector, defense]
entities: [actor:qilin, incident:retelit-qilin-2026]
techniques: [T1078, T1486]
affected_products: []
cves: []
sources:
  - url: "https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/"
    publisher: "IrpiMedia"
    date: "2026-08-04"
    role: primary
  - url: "https://www.bismark.it/9139/retelit-nel-mirino-del-ransomware-qilin-colpito-uno-dei-principali-operatori-italiani-delle-telecomunicazioni/"
    publisher: "Bismark.it"
    date: "2026-07-12"
    role: corroborating
  - url: "https://www.retelit.it/it/stampa/comunicati-stampa"
    publisher: "Retelit"
    date: "2026-08-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Tra i clienti dell'azienda figurano società strategiche quali Leonardo, almeno tre gestori di identità digitali e 193 pubbliche amministrazioni."
    publisher: "IrpiMedia"
  - quote: "Non è noto il momento in cui è avvenuto l'attacco, rivendicato da Qilin con un primo post sul proprio sito"
    publisher: "IrpiMedia"
  - quote: "L'attacco informatico attribuito al gruppo criminale Qilin è avvenuto lo scorso 8 giugno, come notificato alle autorità competenti"
    publisher: "Retelit"
  - quote: "3 dei 38 data center Retelit dislocati sul territorio nazionale e pari a circa il 7% dei sistemi distribuiti nei data center"
    publisher: "Retelit"
  - quote: "Retelit non ha nascosto quanto avvenuto. Al contrario, ha prontamente informato i clienti impattati, l'Agenzia per la Cybersicurezza Nazionale (ACN), il Computer Security Incident Response Team (CSIRT), la Polizia Postale e, in via prudenziale e cautelativa, il Garante per la Protezione dei Dati Personali."
    publisher: "Retelit"
  - quote: "IrpiMedia è in grado di rivelare esattamente quali sono: Verona, Roma e Milano."
    publisher: "IrpiMedia"
  - quote: "Secondo quanto riferito da una fonte coinvolta nell'evento, l'attacco sarebbe partito dal computer di un amministratore di sistema nel quale sono state carpite le password che hanno permesso all'attaccante di compiere dei «movimenti laterali»"
    publisher: "IrpiMedia"
  - quote: "è deducibile che il presidio di sicurezza (Soc, Security Operations Center) non abbia rilevato i movimenti laterali né la cifratura dei server se non quando era troppo tardi"
    publisher: "IrpiMedia"
verification: multi-source
sourcing_note: >
  Three claim tiers are kept apart deliberately. Retelit's own account, quoted from the right-of-reply
  it sent IrpiMedia after publication, supplies the 8 June date, the Qilin attribution, the
  three-of-38 scope and the regulator notifications; Retelit has issued no public statement through
  its own press channel, which this run confirmed against that channel directly. IrpiMedia supplies
  the customer-roster figures, the volume estimate, the naming of the three sites and — separately and
  more strongly — its own examination of the published dump. Qilin's leak-site post supplies only the
  file count and the claim itself, and is never treated as fact. The customer roster is a statement
  about who Retelit serves, not about whose data was taken; no Italian public administration has
  confirmed downstream impact, and the entry does not imply one.
confidence: high
update_of: null
references: []
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

Retelit is one of Italy's largest business telecommunications and cloud operators, co-owner of a transcontinental submarine fibre cable and operator of 38 data centres across the country. On 2026-08-04 the investigative outlet IrpiMedia reported that it had been compromised in an extortion attack claimed by Qilin, with hundreds of gigabytes of files taken and part of them already published ([IrpiMedia, 2026-08-04](https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/)). Qilin's leak-site page, screenshotted by the outlet on 1 August, listed 270,000 files; IrpiMedia estimated at least 300 GB, because the site itself displayed an apparent placeholder size. The listing first appeared on 11 July and a document-and-passport sample followed on 14 July. The first outlet to report it was not IrpiMedia but an Italian trade blog on 12 July, which IrpiMedia credits as having "riportato la prima volta" the attack ([Bismark.it, 2026-07-12](https://www.bismark.it/9139/retelit-nel-mirino-del-ransomware-qilin-colpito-uno-dei-principali-operatori-italiani-delle-telecomunicazioni/)) — so the compromise was public knowledge in the Italian trade press for over three weeks before the investigation that finally drew a company response.

Why this reaches a Swiss or European public-sector reader is the customer roster rather than the victim's name: "Tra i clienti dell'azienda figurano società strategiche quali Leonardo, almeno tre gestori di identità digitali e 193 pubbliche amministrazioni" — among the company's customers are strategic firms such as Leonardo, at least three digital-identity providers, and 193 public administrations. That is a statement about who Retelit serves, and it must not be read as a statement about whose data was taken. On that narrower question there is one concrete finding, and it is the outlet's own rather than a criminal claim: IrpiMedia says it examined the published dump and found Internet connectivity provisioning documents for the defence and aerospace group Leonardo's Genoa and Turin offices, dated October 2025 and April 2026. No Italian public administration has confirmed downstream impact.

The disclosure behaviour is the second half of the story. As IrpiMedia recorded before publication, "Non è noto il momento in cui è avvenuto l'attacco, rivendicato da Qilin con un primo post sul proprio sito" — the timing of the attack was unknown, and the company had not communicated the incident publicly nearly two months after its probable discovery. What broke that was the article. Afterwards Retelit sent the outlet a right-of-reply, published in full, which is where the company's own account appears for the first time: "L'attacco informatico attribuito al gruppo criminale Qilin è avvenuto lo scorso 8 giugno, come notificato alle autorità competenti" — an 8 June attack attributed to Qilin, notified to the competent authorities. Retelit adds that it "non ha nascosto quanto avvenuto. Al contrario, ha prontamente informato i clienti impattati, l'Agenzia per la Cybersicurezza Nazionale (ACN), il Computer Security Incident Response Team (CSIRT), la Polizia Postale e, in via prudenziale e cautelativa, il Garante per la Protezione dei Dati Personali" — that it did not conceal the incident and promptly informed affected customers, the national cybersecurity agency, CSIRT, the postal police and, as a precaution, the data-protection authority. It also stood up a war room with the agency and CSIRT alongside external incident-response and forensics firms. Retelit's own scoping is narrower than the reporting implies: "3 dei 38 data center Retelit dislocati sul territorio nazionale e pari a circa il 7% dei sistemi distribuiti nei data center" — a limited part of the virtualisation infrastructure in 3 of 38 national data centres, around 7% of distributed systems. This pipeline reports both characterisations and resolves neither; the gap between them is itself the finding. Separately, this run confirmed against Retelit's own press-release index that no public statement about the incident appears there.

On mechanism the reporting is thinner than on chronology, and its own sourcing tier is lower, which is worth carrying rather than smoothing over. IrpiMedia relays an account from an unnamed source involved in the incident, in the Italian conditional: "Secondo quanto riferito da una fonte coinvolta nell'evento, l'attacco sarebbe partito dal computer di un amministratore di sistema nel quale sono state carpite le password che hanno permesso all'attaccante di compiere dei «movimenti laterali»" — the attack is said to have started from a system administrator's computer, from which passwords were captured that let the attacker move laterally. The detection failure is not reported as fact either but as the outlet's inference from the volume already published: "è deducibile che il presidio di sicurezza (Soc, Security Operations Center) non abbia rilevato i movimenti laterali né la cifratura dei server se non quando era troppo tardi" — it is deducible that the security operations centre did not detect the lateral movement or the encryption of servers until it was too late. Neither claim comes from Retelit, and Retelit's own statement addresses scope rather than sequence.

That sequence is nonetheless the part a responder can act on, because it is ordinary rather than exotic: a privileged administrator endpoint yields stored credentials, those credentials authenticate to systems the endpoint legitimately reaches, and the encryption stage arrives before anything flags the movement between the two. Telemetry-wise it lands in three classes — credential access on administrator workstations, authentication events showing an administrator account reaching hosts it does not normally touch, and volume anomalies on file and virtualisation infrastructure. **Triage:** an administrator account authenticating across many systems is precisely what administrator accounts do, so breadth alone discriminates nothing; what separates this from routine work is the pairing of credential-store access on the workstation with a subsequent authentication fan-out that does not match the operator's normal maintenance pattern or change window.

Two further facts cut against Retelit's account of its own communications and belong next to it. The company says it "ha prontamente informato i clienti impattati" — promptly informed affected customers — but the same article's 6 August update records the opposite experience from the customer side: after a notification circulated by Italy's public-administration CERT at the end of July, "numerosi clienti riferiscono di aver scritto a Retelit per chiedere come mai non fosse arrivata alcuna comunicazione in seguito al data breach" — numerous customers report having written to Retelit to ask why no communication had arrived after the breach. This pipeline does not adjudicate between the two; both are reported and attributed.

The second fact is the one with the most direct public-sector consequence, and it establishes a notification path that ran around the company rather than through it. IrpiMedia records that Italy's CERT for public administration learned of the incident only on 30 July, and on that date began warning the security officers of every public administration potentially involved or otherwise using Retelit's services — "Tra questi anche Cineca, Lepida e Infocamere", among them a university and research consortium that also acts as a certified digital-preservation provider, and two organisations the article describes as providing Italy's digital-identity and digital-signature services. Those organisations are named as recipients of a precautionary warning, not as confirmed-impacted parties, and the distinction matters: what the record shows is a sector CERT propagating a supplier incident to downstream public bodies seven weeks after it happened, because the supplier had not.

One detail deserves emphasis because it inverts the reassurance the 7% figure is meant to offer. "IrpiMedia è in grado di rivelare esattamente quali sono: Verona, Roma e Milano" — the outlet names the three affected sites, and reports that the Milan site is the one certified by the national agency for Retelit's own backup management and service continuity in the event of a cyber incident. It also reports that customers contacted the newsroom complaining of partial or total failure of backup recovery. A small percentage of an estate is not a small incident when the affected fraction includes the continuity capability itself.

**Defender takeaway:** the transferable exposure here is not Retelit's, it is the pattern of depending on a connectivity or hosting provider whose incident you will learn about from journalism rather than from the provider. Two questions follow for any public-sector body with a comparable supplier. First, what is the contractual notification trigger and timeline, and would a two-month gap between an incident and public disclosure have breached it — Retelit says it informed affected customers promptly, which is compatible with the public silence and is exactly why the contractual channel, not the press channel, is the one to test. Second, and more concretely: if that provider also holds your backups or your continuity capability, the provider's own incident scope and your recovery capability are the same variable. Establish now whether your restore path depends on infrastructure that shares a failure domain with the provider's production estate, because that is the question the affected customers in this case discovered the answer to during a live recovery.
