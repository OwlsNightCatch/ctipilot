---
schema: 1
kind: policy
horizon: strategic
weekly_section: weekly-policy
title: "NCSC UK published the first authority-issued technical control baseline for an organisation's own agentic-AI deployments — sandbox tiers, credential-lifetime scoping, named human accountability and an emergency shutdown — explicitly as interim advice that formal guidance will supersede"
headline: "The first national-authority answer to 'how do we secure the agents we are deploying', and it is written to be measured against"
summary: >
  On 2026-08-20 NCSC UK published interim practical guidance for organisations deploying agentic AI,
  framed explicitly as a stop-gap that forthcoming formal guidance will build upon and supersede. The
  substance is a proportionality model rather than a checklist: calibrate controls to the agent's
  autonomy and blast radius, threat-model the failure scenarios before deployment, pick a
  human-in-the-loop, human-on-the-loop or human-out-of-the-loop oversight tier proportionate to the
  consequence of a wrong action, and make named individuals or groups accountable for agentic-AI
  activity. The technical core is a four-level network-sandboxing maturity model running from
  unrestricted access to no external network access with the model hosted locally, with
  protocol-aware proxies where allowlists are too coarse; a credential rule that scopes permissions to
  the task and lifetimes to the shortest practicable, with a proxy injecting credentials so the agent
  never holds them; a logging requirement that treats agentic activity as user activity subject to
  24/7 security monitoring, with immutable logs; and a maintained ability to halt agent activity
  immediately. For a Swiss federal SOC the obligation is not Swiss, but this is the control language a
  procurement or governance function will be asked to evidence against.
discovered_at: "2026-08-23T23:59:40Z"
event_date: "2026-08-20"
run_id: 2026-08-23T2311Z-weekly
priority: notable
immediate_action: null
tags: [ai-abuse, cloud, identity]
regions: [uk, europe, global]
sectors: [public-sector, finance, healthcare, technology]
entities:
  - policy:ncsc-uk-agentic-ai-risk-guidance-2026
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai"
    publisher: "NCSC UK"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "The NCSC has been researching and experimenting in this area for some time and is working with partners to develop formal guidance which will build upon, and ultimately supersede, this blog."
    publisher: "NCSC UK"
  - quote: "Where possible you should restrict the credentials available to the agent. Ensure it has only the permissions it needs for the task being performed and use credentials with the shortest possible lifetime."
    publisher: "NCSC UK"
  - quote: "Agentic AI activity should be treated as a form of user activity."
    publisher: "NCSC UK"
  - quote: "Where possible, logs should be immutable so you can trust them during an investigation."
    publisher: "NCSC UK"
verification: single-source-national-cert
sourcing_note: >
  Single-source under the national-CERT carve-out: NCSC UK is the first-party publisher of its own
  guidance, so there is no second assessor to corroborate — the document is the fact. The status is
  carried exactly as the authority states it: interim advice, not a binding obligation, explicitly to
  be superseded. NCSC's own further-reading list points at the ETSI standard EN 304 223 on baseline
  cyber security requirements for AI models and systems and at two further pieces on adopting agentic
  AI; this entry records that the list exists and does not characterise the relationship between EN
  304 223 and any other standardisation process.
confidence: high
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

Prior weeklies have tracked AI three ways: as an attacker capability, as a target in its own right, and — in the W32 entry on evaluation-vendor containment failures — as a governance problem for the organisations building it. This is the first of a fourth kind that this pipeline has carried: a national authority publishing technical controls for defending an organisation's own agentic deployments. It matters less for what it says than for the fact that a named authority has now said it, because that is the moment "how are you securing your agents" stops being an internal engineering conversation and becomes something a regulator, an auditor or a customer can point at.

NCSC UK is careful about the document's status and says so twice: "The NCSC has been researching and experimenting in this area for some time and is working with partners to develop formal guidance which will build upon, and ultimately supersede, this blog," and the interim advice exists to help organisations make informed decisions about how to deploy agentic AI systems securely within their environments in the meantime ([NCSC UK, 2026-08-20](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)).

**The frame is proportionality, not a control list.** The guidance opens by insisting that the recommendations apply proportionately to how much autonomy an agent actually has — some agents make suggestions or carry out tightly constrained tasks, others take actions against production systems with little or no human intervention — and that the greater the autonomy, the greater the impact if the agent malfunctions, accesses information it should not, or takes actions outside its intended scope. It then tells organisations not to treat model-level safeguards as holistic: built-in safety controls may be bypassed, may not hold in higher-risk environments, and are not sufficient to manage risk on their own.

**The parts a SOC will care about.** Three of the seven considerations are directly operational. On oversight, the guidance names three tiers — human-in-the-loop, where humans approve actions before they happen; human-on-the-loop, where humans monitor and can intervene; and human-out-of-the-loop — and, for higher-risk scenarios, recommends human oversight alongside technically enforced controls, with named individuals or groups made responsible for agentic-AI activities. On sandboxing, it supplies a four-level network maturity model that is unusually concrete for guidance of this kind: level 1 is unrestricted network access, level 2 restricts to an allowlist of approved domains, level 3 restricts to just the model's API, and level 4 is no external network access with the model hosted locally inside the network sandbox. It also tells designers to define the sandbox boundary across five axes rather than one — execution, network, compute, credentials and data — and notes that where allowlists lack the necessary granularity, protocol- or service-aware proxies allowing connections only by exception are the alternative. On credentials, the rule is stated plainly: "Where possible you should restrict the credentials available to the agent. Ensure it has only the permissions it needs for the task being performed and use credentials with the shortest possible lifetime," with a proxy injecting credentials into requests as the pattern that keeps the agent from holding them at all ([NCSC UK, 2026-08-20](https://www.ncsc.gov.uk/blogs/managing-the-cyber-risk-of-agentic-ai)).

The observability section is the one that puts this on a SOC's plate rather than an architect's. It asks for chain-of-thought traces and transcripts from the agent alongside sandbox-environment logs, warns that the log collection infrastructure is itself attack surface an agent might abuse to escape its sandbox, and states two requirements that read as compliance language because they are: "Where possible, logs should be immutable so you can trust them during an investigation," and "Agentic AI activity should be treated as a form of user activity" — which the guidance immediately operationalises as inclusion in 24/7 security monitoring and incident response, with a suggested rollout that runs initial experiments in office hours when more human oversight is available before expanding to overnight or weekend autonomous execution. The last consideration is an emergency shutdown that covers more than stopping the agent's processes: the ability to rapidly restrict network access to the agentic infrastructure and interrupt communication between agents and the inference infrastructure.

**Defender takeaway:** for a Swiss federal SOC the obligation is British and this is guidance rather than law, so the practical use is as a measuring stick in two directions. Outward, it is the control language that public-sector procurement and third-party assurance questionnaires will start borrowing — a supplier deploying agents against your data can now be asked which of the four network-sandbox levels it operates at, what the credential lifetime is, whether agent activity reaches a monitored log, and who is the named owner. Inward, it converts an open-ended question into four answerable ones for any agentic deployment your own organisation is running or piloting today. Two of them are worth checking this week regardless of where the guidance eventually lands: whether agent activity is reaching the same monitoring as user activity — because in most estates it currently is not, and the guidance is explicit that it should — and whether the credentials an agent holds are scoped and short-lived or are a long-lived service identity with the permissions of whichever team stood the agent up. The second is the one that turns an agent malfunction into an incident.
