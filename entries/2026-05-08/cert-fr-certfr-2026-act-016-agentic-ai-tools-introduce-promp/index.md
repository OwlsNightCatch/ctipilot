---
schema: 1
kind: threat
title: "CERTFR-2026-ACT-016: CERT-FR says autonomous AI assistants such as OpenClaw must not be deployed on workstations until proven secure"
headline: "CERT-FR: keep autonomous AI assistants off workstations; use them only in isolated sandboxes holding no sensitive data"
summary: >
  CERT-FR's advisory of 2026-04-13 on autonomous personal assistants such as OpenClaw and Claude Cowork,
  which run commands, drive the browser, handle files and send mail on chat-message triggers, says they
  must not be deployed on workstations or in production until stabilised and proven, and limits their use
  to isolated test sandboxes without sensitive data. Its risk list covers workstation compromise through
  flaws in these mostly beta tools, data leakage to uncontrolled external resources, excessive access to
  office applications, leakage of login secrets shared with the agents, and destructive actions beyond the
  user's control.
discovered_at: "2026-05-08T05:00:06Z"
event_date: "2026-04-13"
run_id: 2026-05-08-migrated
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - supply-chain
regions:
  - europe
sectors: []
entities:
  - "report:certfr-2026-act-016"
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/"
    publisher: "CERT-FR"
    date: "2026-04-13"
    role: primary
closed_sources: []
evidence: []
verification: single-source-national-cert
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
techniques: [T1195.001, T1059, T1567]
classification:
  reliability: A
  credibility: 2
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-10-11T14:16:35Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The earlier text described a different document: CERT-FR's advisory does not mention MCP servers, guardrails or tool-call allowlisting, and names OpenClaw and Claude Cowork rather than Copilot Studio or AutoGen. The entry is rewritten from the advisory around its actual position, no deployment on workstations or in production and sandbox-only use, with its hardening levers, the advisory date, the canonical report entity, a rating and an ATT&CK mapping.
    fields: [title, headline, summary, event_date, entities, techniques, sources, classification, body]
  - at: "2026-10-21T12:06:43Z"
    run_id: 2026-10-21T1149Z-audit
    type: improvement
    summary: >
      CERT-FR's own list of five risks is added: workstation compromise through flaws in the mostly beta
      tools, data leakage to uncontrolled external resources, excessive access to office applications,
      leakage of login credentials shared with the agents, and destructive actions beyond the user's
      control. Plugins and prompt injection are no longer presented as the advisory's core risks.
    fields: [summary, body, headline]
---

CERT-FR's advisory CERTFR-2026-ACT-016, published on 2026-04-13, addresses autonomous personal assistants such as OpenClaw, Claude Cowork and open-source equivalents, whose adoption has grown strongly since early 2026. Unlike chat assistants, they execute commands, control the browser, read and write files, manage calendars and send mail, triggered by a text message through applications such as Slack, WhatsApp or Discord ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)). Plugins can be loaded dynamically and, depending on the integration model, run as trusted code with the application's privileges, which widens the software supply chain; prompt injection is an intrinsic weakness of the underlying language models, and an agent that orchestrates operating-system-level tools raises the risk of unauthorized command execution and data exfiltration through prompt injection or hijacked messages ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)). The advisory's risk list has five items: compromise of the user's workstation through a vulnerability in these tools, most of them still in beta; leakage of sensitive data by the agents to uncontrolled external resources; excessive access rights over all of the user's office applications (mail, calendar, file manager, business and HR applications); sharing of login credentials with the agents and their potential leakage; and loss of control over the agents' actions on the workstation, including destructive actions that damage the integrity or availability of business applications or data ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)).

CERT-FR's position is that such assistants must not be deployed on workstations and their use should be prohibited until the product is stabilised and proven from a security standpoint; they must in no case be deployed in production, only in isolated test sandboxes holding no sensitive data, and the same applies to mobile deployments ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)). Where they are used, the main lever is configuration hardening: limit the tools and actions available to the strict minimum, require human validation for any system command or action with side effects, run the agent in a sandbox, and allowlist the channels and interlocutors that may trigger it, for example only on an explicit mention of the agent ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)).

**Exposure:** any workstation or phone where users have installed an autonomous assistant with access to mail, calendar, files or business applications, typically as unvalidated Shadow IT ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)).

**Defender takeaway:** treat autonomous desktop AI assistants as unapproved software on production workstations: block installations not validated by IT and security, and allow them only in isolated sandboxes without production data, secrets or personal data ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)).

## Correction — 2026-10-11T14:16:35Z

CERT-FR's advisory concerns autonomous personal assistants on workstations, not agentic orchestration platforms, and does not mention the Model Context Protocol; its supply-chain concern is plugins that load dynamically and run as trusted code ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)). Its recommendations are to keep these assistants off workstations and out of production, confine them to isolated sandboxes, restrict their tools, require human validation for system commands and allowlist the channels that may trigger them. The earlier text attributed guardrails, tool-call allowlisting and a rule to treat all agent output as untrusted to CERT-FR, and named products the advisory does not mention.

## Improvement — 2026-10-21T12:06:43Z

CERT-FR's advisory lists five risks: compromise of the user's workstation through a vulnerability in these tools, most of them still in beta; leakage of sensitive data by the agents to uncontrolled external resources; excessive access rights over the user's office applications; sharing of login credentials with the agents and their potential leakage; and loss of control over the agents' actions, including destructive ones ([CERT-FR, 2026-04-13](https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/)).
