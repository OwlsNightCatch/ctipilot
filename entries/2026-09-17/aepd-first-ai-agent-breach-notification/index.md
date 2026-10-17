---
schema: 1
kind: policy
title: "Spain's AEPD reports its first GDPR breach notification attributed to an autonomous AI agent, and tells data controllers to name AI-agent attacks explicitly in risk analyses"
headline: "Spain's data protection authority: a breach victim reports an AI agent chained login, further vulnerability discovery and data modification on its own"
summary: >
  Spain's national data protection authority (AEPD) disclosed on 2026-09-14 what it describes as
  the first personal-data-breach notification it has received attributing the incident to a
  third party's use of an autonomous AI agent: per the affected organization's own account, the
  agent searched for vulnerabilities, logged in, then autonomously found further vulnerabilities
  and used them to modify personal data and access invoices. AEPD tells data controllers and DPOs
  to name AI-agent-assisted or -executed attacks explicitly in risk analyses rather than relying
  on generic threat categories, and to treat digital credentials and API keys as higher-value
  targets given machine-speed exploitation.
discovered_at: "2026-09-17T04:40:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-09-17T0409Z-intel
priority: routine
immediate_action: null
tags: [ai-abuse, identity]
regions: [europe]
sectors: [public-sector]
entities: ["policy:aepd-ai-agent-breach-notification-guidance"]
techniques: [T1190]
affected_products: []
cves: []
sources:
  - url: "https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia"
    publisher: "AEPD (Agencia Española de Protección de Datos)"
    date: "2026-09-14"
    role: primary
  - url: "https://www.heise.de/news/Spaniens-Datenschutzaufsicht-Erster-Cyberangriff-mithilfe-eines-KI-Agenten-11454545.html"
    publisher: "heise online"
    date: "2026-09-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attacking agent began a search for vulnerabilities in generic files, and achieved a successful login. Once it accessed the system, it began to autonomously search for vulnerabilities in the application, which, once achieved, allowed it to modify personal data and access invoices. (translated from Spanish)"
    original: "El agente atacante inició una búsqueda de vulnerabilidades en archivos genéricos, y realizó un login correcto. Una vez accedió al sistema, comenzó a buscar, de forma autónoma, vulnerabilidades en la aplicación, lo que, una vez conseguido, le permitió modificar datos personales y acceder a facturas."
    publisher: "AEPD (Agencia Española de Protección de Datos)"
  - quote: "This confirms the need to expressly incorporate AI-assisted or AI-executed attacks into the risk analyses of data processing. (translated from Spanish)"
    original: "confirma la necesidad de incorporar expresamente los ataques asistidos o ejecutados mediante IA a los análisis de riesgos de los tratamientos"
    publisher: "AEPD (Agencia Española de Protección de Datos)"
verification: single-source
sourcing_note: "AEPD is Spain's national data-protection authority acting as primary disclosing party for its own jurisdiction's regulatory process, which is why a single source carries the entry; heise online's pickup relays AEPD's own blog post rather than independently assessing the incident. AEPD itself stresses the account rests solely on the notifying organization's own unaudited statement and does not name the organization or the AI model involved."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-20T13:28:45Z"
    run_id: 2026-09-20T1308Z-audit
    type: improvement
    summary: >
      Two pieces of reader-facing text referred to house machinery rather than to the reporting: one
      sentence in the analysis referred to the entry collection, and the sourcing note carried an internal
      policy-reference code. Both now state the same thing in plain language. No claim changes.
    fields: [body, sourcing_note]
    internal: true
  - at: "2026-09-30T06:56:05Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority recalibrated from notable to routine: a foreign regulator notice
      that changes no decision for a Swiss public-sector SOC. An uncited comparison with other AI-agent
      incidents and an unsupported claim that this is the first publicly documented criminal use of
      a commercial AI agent are removed, the routine-priority text is trimmed to the regulator's
      facts and guidance, and the verification flag is corrected to single-source because AEPD is a
      data-protection authority, not a national CERT. The title now calls it AEPD's first such
      notification rather than a global first, and the speed-not-new-threats framing now cites
      AEPD's own post.
    fields: [priority, body, verification, title]
migrated_from: null
---

Spain's Agencia Española de Protección de Datos (AEPD) disclosed on 2026-09-14 that it has received its first personal-data-breach notification attributing the incident to a third party's use of an autonomous AI agent built on a known large language model ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)). Per the affected organization's own account, which AEPD stresses is unverified and awaits its own analysis, the agent searched for vulnerabilities in generic files, achieved a successful login, then autonomously searched the application for further vulnerabilities and used them to modify personal data and access invoices ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)). AEPD names neither the organization nor the model, says the model's provider was not necessarily compromised, and notes that one notification does not establish a statistical trend ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)).

AEPD's deputy director Francisco Pérez Bes ([heise online, 2026-09-16](https://www.heise.de/news/Spaniens-Datenschutzaufsicht-Erster-Cyberangriff-mithilfe-eines-KI-Agenten-11454545.html)) writes that AI creates no new threats but increases the speed, scale and adaptability of known malicious techniques ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)). AEPD tells data controllers and processors to name AI-assisted or AI-executed attacks explicitly in risk analyses, to check whether incident-response procedures built for manual attacks are fast enough, and to treat accounts, API keys and over-privileged tokens as higher-value targets, because an agent holding one can act at machine speed across services ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)). For a Swiss public-sector SOC, the relevance is the policy signal: a European data-protection regulator now expects AI-agent attack scenarios in risk analyses ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)).

**Defender takeaway:** add AI-agent-executed attacks as their own scenario in risk-analysis templates, and test whether incident-response runbooks assume a human-paced attacker ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)).

## Correction — 2026-09-30T06:56:05Z

AEPD describes this as the first breach notification of its kind that it has received, and says a single notification does not establish a statistical trend ([AEPD, 2026-09-14](https://www.aepd.es/prensa-y-comunicacion/blog/primera-notiviacion-brecha-datos-personales-causada-por-ataque-ejecutado-mediante-agente-ia)). The entry previously called it the first publicly documented case of a criminal weaponizing a commercial AI agent and compared it with other AI-agent incidents, neither of which the sources support.
