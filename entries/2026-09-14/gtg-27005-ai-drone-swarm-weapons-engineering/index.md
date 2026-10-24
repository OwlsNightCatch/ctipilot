---
schema: 1
kind: research
title: "GTG-27005: Anthropic discloses a freelance Russia-based team that used Claude Code to engineer an autonomous FPV kamikaze-drone-swarm targeting stack with no human veto over target selection or detonation"
headline: "Anthropic: a freelance team used Claude Code to build a drone swarm that picks its own targets and decides when to detonate"
summary: >
  Anthropic's September 2026 threat-intelligence report profiles GTG-27005, a small freelance
  Russia-based team ("DronDoc"/"Serafim") that used Claude Code to engineer a full-stack autonomous
  first-person-view kamikaze-drone-swarm targeting system whose onboard model can select targets,
  including a "person" class, and issue the detonation call with no human in the loop. Anthropic
  assesses the group as a freelance outfit, not a Russian state entity, and banned accounts associated
  with the actors.
discovered_at: "2026-09-14T04:27:24Z"
updated_at: null
event_date: "2026-09-10"
run_id: 2026-09-14T0410Z-intel
priority: notable
immediate_action: null
tags: [russia-nexus, ai-abuse]
regions: [europe, russia-cis]
sectors: [defense, public-sector]
entities: ["actor:gtg-27005"]
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.anthropic.com/threat-intelligence-report-september-2026"
    publisher: "Anthropic"
    date: "2026-09-10"
    role: primary
  - url: "https://dronexl.co/2026/09/12/anthropic-claude-russian-kamikaze-drone-swarm-software/"
    publisher: "DroneXL"
    date: "2026-09-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We identified likely freelance Russia-based threat actors who set out to build a full-stack autonomous first-person-view (FPV) kamikaze drone swarm."
    publisher: "Anthropic"
  - quote: "The actors designed the platform for autonomous lethal engagement; the onboard model could select targets (including a “person” target class) and issue detonation commands without a human in the loop."
    publisher: "Anthropic"
  - quote: "We assess the actors were a small, specialized freelance team doing a mix of civilian and military work, not a Russian state entity."
    publisher: "Anthropic"
  - quote: "The actors claimed to have received funding from Russia’s Advanced Research Foundation, National Technology Initiative, and Ministry of Defence, though we cannot verify those claims."
    publisher: "Anthropic"
verification: single-source
sourcing_note: "All substantive reporting traces to Anthropic's own investigation of its own platform's misuse; DroneXL quotes and restates that same report rather than independently assessing the underlying activity, so this is one assessor with a second publisher, not independent corroboration."
confidence: high
references:
  - "2026-09-13/gtg-20006-anthropic-russia-ai-orchestrated-espionage"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-20T13:27:57Z"
    run_id: 2026-09-20T1308Z-audit
    type: correction
    summary: >
      The entry said Anthropic banned nine accounts and banned all of them. Anthropic's report states
      that it identified nine accounts associated with the group, that eight were used only for ordinary
      freelance work, and that it banned accounts associated with the actors; it does not say how many
      of the nine were banned. The summary and the analysis now state what the report states. A sentence
      explaining the absence of an ATT&CK mapping was also removed from the analysis.
    fields: [summary, body]
migrated_from: null
---

Anthropic's fourth threat-intelligence report (2026-09-10) names GTG-27005 as a distinct case study from the same document's already-covered GTG-20006 cyber-espionage cluster: a small freelance Russia-based team, self-styled "DronDoc" or "Serafim," that used Claude Code to write and test software for a full-stack autonomous first-person-view kamikaze-drone swarm, saving the code directly into the actors' own project files alongside a software-in-the-loop simulation stack and a rented GPU host for model training ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). Unlike GTG-20006, this is not a network-intrusion campaign: the team built shared swarm memory and fault-tolerant coordination logic, an onboard small language model governing each drone's attack/observe/return-to-base decisions, terminal-guidance software that steers to a target via the onboard camera and issues the detonation call, a control-link geolocation module to locate opposing drone operators, a passive acoustic-detection layer, and low-level logic for the drones' programmable chips. Anthropic states the platform was designed for autonomous lethal engagement: the onboard model could select targets, including a "person" class, and issue detonation commands without a human in the loop ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). Flashing firmware to live development boards, provisioning single-board computers and wiring a mesh-network simulation environment confirmed genuine hardware-in-the-loop testing rather than pure simulation; DroneXL reports, citing a separate outlet's reading of the same disclosure, that the swarm never flew a live mission and stayed at the validated-in-simulation stage ([DroneXL, 2026-09-12](https://dronexl.co/2026/09/12/anthropic-claude-russian-kamikaze-drone-swarm-software/)).

The team trained a computer-vision classifier on scraped Ukrainian combat footage, split into "enemy" and "friendly" classes with Russian systems allow-listed, and repeatedly used a fixed coordinate in Donetsk Oblast as its demonstration strike point, with Ukrainian front-line cities and corridors as mission geography. Accounts were created between late 2025 and early 2026; the operation itself started mid-May 2026, and the team routed traffic through commercial virtual private servers to circumvent Anthropic's geographic access controls ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). Anthropic identified nine associated accounts, eight of which were used only for ordinary freelance civilian work, and says it banned accounts associated with the actors without stating how many of the nine; it assesses the group had ties to a regional Russian university and a federal research center affiliated with the Russian Academy of Sciences, concluding "the actors were a small, specialized freelance team doing a mix of civilian and military work, not a Russian state entity" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). The actors told Claude they were funded by Russia's Advanced Research Foundation, the National Technology Initiative and the Ministry of Defence, "though we cannot verify those claims" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)); DroneXL describes the Advanced Research Foundation as Russia's equivalent of DARPA and notes that if the funding claim holds, a state defense-research fund paid for work no state employee directly touched ([DroneXL, 2026-09-12](https://dronexl.co/2026/09/12/anthropic-claude-russian-kamikaze-drone-swarm-software/)). The report catalogues six systems from the case, five assessed at TRL 3 to 4 and validated in simulation: a Lancet-class FPV loitering munition ("Sibiryachok"), an air-to-air interceptor UAV ("TRIIT interceptor"), a standoff strike UAV ("Striker" variant), a heterogeneous autonomous swarm (Serafim, Zvezdochyot-Serafim, swarm-opi5, Medovik), and swarm command-and-control/combat-memory firmware; the sixth, a counter-UAS/suppression-of-air-defense doctrine and test stand ("Nebo-22"), is listed only as doctrine and simulation, without a maturity rating ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)).

This is a strategic-awareness disclosure, not a network-intrusion technique. Its relevance to this constituency sits with the Swiss Armed Forces and civil-protection stakeholders rather than civilian IT defense: a commodity coding assistant has now been shown, by the vendor's own disclosure, to substantially lower the engineering bar for autonomous lethal-target-selection software built entirely by a small freelance team with no state infrastructure of its own. The transferable lesson is for defense-policy and dual-use-technology risk assessment, not detection engineering: procurement and research-security reviews touching drone, robotics or autonomous-systems programs should treat "an AI coding assistant substantially accelerated development" as a realistic capability uplift for small, resource-constrained teams, not a hypothetical.

## Correction — 2026-09-20T13:27:57Z

Anthropic's report does not state how many of the nine accounts it identified were banned. It says it identified nine accounts associated with the group, that eight of them were used only for ordinary freelance work rather than weapons-related software development, and that it "banned accounts associated with the actors" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). The earlier statement that all nine were banned went beyond the report.
