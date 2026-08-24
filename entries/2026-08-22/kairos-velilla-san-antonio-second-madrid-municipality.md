---
schema: 1
kind: incident
horizon: operational
title: "Kairos claims 77.6 GB from a second Madrid-region municipality in three months, and the town hall confirms a security incident while stating it cannot yet confirm that any data was actually accessed or taken"
headline: "An encryption-free extortion brand is working through Spanish municipal administrations, where the first visible symptom is the claim itself"
summary: >
  The Ayuntamiento de Velilla de San Antonio, a municipality in the Community of Madrid, published a
  statement confirming it detected a security incident that could have allowed the exposure of information
  held in its systems, and stating that the investigation remains open and effective access to or
  extraction of data cannot yet be confirmed. The extortion actor Kairos claims to have taken 77.6 GB
  including administrative and personnel records, electronically signed official documents, municipal
  motions and national identity documents. Municipal services are unaffected, the National Cryptologic
  Centre and other authorities have been notified, and the Madrid regional cybersecurity agency has
  offered technical and coordination support. Kairos claimed a second Madrid-region town hall, Valdemoro,
  in May 2026. No source states an access vector for either.
discovered_at: "2026-08-22T05:09:30Z"
event_date: "2026-08-21"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime]
regions: [europe]
sectors: [public-sector]
entities: [actor:kairos-extortion, incident:velilla-san-antonio-kairos-breach-2026-08]
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://ayto-velilla.es/posible-exposicion-de-informacion-en-los-sistemas-del-ayuntamiento-de-velilla-de-san-antonio/"
    publisher: "Ayuntamiento de Velilla de San Antonio"
    date: "2026-08-21"
    role: primary
  - url: "https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html"
    publisher: "EscudoDigital"
    date: "2026-08-21"
    role: corroborating
  - url: "https://www.escudodigital.com/ciberseguridad/ayuntamiento-valdemoro-ciberataque-ransomware.html"
    publisher: "EscudoDigital"
    date: "2026-05-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "El Ayuntamiento de Velilla de San Antonio ha detectado una incidencia de seguridad que podría haber permitido la exposición de determinada información alojada en sus sistemas informáticos."
    publisher: "Ayuntamiento de Velilla de San Antonio"
  - quote: "La investigación continúa abierta y, por el momento, no se puede confirmar que se haya producido un acceso o extracción efectiva de datos."
    publisher: "Ayuntamiento de Velilla de San Antonio"
  - quote: "La incidencia no ha afectado a la prestación de los servicios municipales, que continúan funcionando con normalidad."
    publisher: "Ayuntamiento de Velilla de San Antonio"
  - quote: "La Agencia de Ciberseguridad de la Comunidad de Madrid ha ofrecido su apoyo técnico y de coordinación al Ayuntamiento en el marco de sus competencias, de acuerdo con el modelo regional de respuesta ante incidentes."
    publisher: "Ayuntamiento de Velilla de San Antonio"
  - quote: "Según la información difundida por el grupo, entre los archivos supuestamente obtenidos figurarían registros administrativos y de personal, documentos oficiales firmados electrónicamente, mociones municipales, datos personales y documentos nacionales de identidad (DNI)."
    publisher: "EscudoDigital"
  - quote: "La coincidencia del grupo atacante y de la localización geográfica convierte el caso de Velilla en una reivindicación especialmente relevante, aunque no permite establecer por sí sola ninguna relación entre ambos incidentes."
    publisher: "EscudoDigital"
verification: multi-source
sourcing_note: >
  The municipality's own statement is the only primary and is the authority for everything the
  administration confirms; the Spanish outlet is the source for what the actor claims and is rated C
  because its role here is largely to relay a leak-site claim, though it states it contacted the town hall
  itself and subsequently had access to its official communication. A check for an AI-assistance
  disclosure on the two fetched article pages found none, and both carry named human bylines. The
  distinction the entry is built on is the municipality's own: an incident is confirmed, an exposure is
  possible, and effective access or extraction is not confirmed — those are three different claims and the
  actor's volume figure belongs to none of them. Two further limits are carried rather than smoothed. The
  outlet's own hedge on the pattern is preserved: it says the coincidence of attacker and geography makes
  the case notable but does not by itself establish any relationship between the two incidents. And its
  May reporting on the earlier Valdemoro claim is internally inconsistent, describing that case as
  ransomware in its headline while its own background material describes Kairos as focused on data theft
  without encryption; the entry reports the contradiction rather than picking a side. The technique
  mapping covers only the extortion model the sources describe — no access vector, no exfiltration
  mechanism and no dwell time is stated by anyone, so none is mapped.
confidence: medium
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

The Ayuntamiento de Velilla de San Antonio, a municipality in the Community of Madrid, states it has detected a security incident that could have allowed the exposure of certain information held in its computer systems, and is explicit about the limits of what it knows: the investigation remains open and, for now, it cannot be confirmed that effective access to or extraction of data has occurred ([Ayuntamiento de Velilla de San Antonio, 2026-08-21](https://ayto-velilla.es/posible-exposicion-de-informacion-en-los-sistemas-del-ayuntamiento-de-velilla-de-san-antonio/)). Work is under way to determine the scope and nature of the potentially affected information, municipal services have not been affected and continue to operate normally, the matter has been notified to the National Cryptologic Centre and other competent authorities, and the Community of Madrid's cybersecurity agency has offered technical and coordination support under the regional incident-response model ([Ayuntamiento de Velilla de San Antonio, 2026-08-21](https://ayto-velilla.es/posible-exposicion-de-informacion-en-los-sistemas-del-ayuntamiento-de-velilla-de-san-antonio/)). Against that carefully bounded statement sits the actor's claim: the extortion group Kairos says it accessed the municipal infrastructure and took 77.6 GB, and per the group's own published list the files would include administrative and personnel records, officially signed electronic documents, municipal motions, personal data and national identity documents ([EscudoDigital, 2026-08-21](https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html)). Nothing in that list is confirmed by anyone but the group claiming it.

Kairos is already in this store as a data-theft-only extortion brand, with no encryptor ever confidently linked to it, and the outlet's description of the model matches: the attacker enters the organisation, locates information of interest, copies it, and then threatens to publish it if the victim does not pay ([EscudoDigital, 2026-08-21](https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html)). The same outlet reported a Kairos claim against another Madrid-region municipality, Valdemoro, in May 2026, of 1.8 TB said to include police reports, citizens' identity documents and administrative files, following an incident that town hall acknowledged on its own website as having been detected on 5 May and having affected its servers ([EscudoDigital, 2026-05-12](https://www.escudodigital.com/ciberseguridad/ayuntamiento-valdemoro-ciberataque-ransomware.html)). That earlier report is internally inconsistent in a way worth flagging rather than averaging: its headline frames the Valdemoro case as ransomware, while the background it carries on the same page describes Kairos as a group focused on data theft without encryption. Two Madrid-region town halls claimed by the same brand inside four months is a pattern worth naming, and the outlet is careful about how far it can be pushed: it says the coincidence of attacker and geography makes the Velilla case particularly relevant but does not on its own establish any relationship between the two incidents ([EscudoDigital, 2026-08-21](https://www.escudodigital.com/ciberseguridad/kairos-asegura-haber-robado-776-gb-de-datos-del-ayuntamiento-de-velilla-de-san-antonio.html)). No access vector has been disclosed for either case.

**Defender takeaway:** for a cantonal or communal administration the transferable content is not the victim but the detection sequence, and it runs backwards from the way an intrusion is supposed to be found. With no encryption there is no service outage, no ransom note on a workstation and no locked file share — the events that make a ransomware intrusion announce itself. What remains is a volume of data leaving over some period, followed by an extortion contact or a leak-site post, and the municipality's own statement shows what that does to an investigation: the incident is confirmed while the exposure is still a maybe, days after the actor has already published a figure. A small administration that wants a chance of seeing this before the claim arrives has to be watching outbound data volume from its records-management, document-signature and personnel systems against those systems' own baselines, and authenticated sessions against those systems from unfamiliar clients or at unusual hours — not endpoint symptoms, which will not appear. **Triage:** the absence of ransomware indicators is not evidence against an active intrusion of this class; it is consistent with it. Treat a leak-site claim naming your own organisation as an investigative trigger for the exfiltration question specifically, and note the shape the municipality's disclosure takes — an early public statement that confirms an incident and declines to confirm the theft is the honest position for a body that cannot yet answer the question, and it is also the position an administration will be in if it has no egress baseline to check against.
