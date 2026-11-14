---
schema: 1
kind: research
title: "CERT Intrinsec maps where autonomous coding agents leave evidence on disk — the same session databases and token files an investigator needs are a credential-collection target"
headline: "OpenCode and OpenAI Codex write prompt history, per-session logs and plaintext API keys to predictable per-user paths"
summary: >
  CERT Intrinsec has begun a forensic-artefact series for autonomous coding-agent CLIs, covering
  OpenCode and OpenAI Codex. Both write their state under a per-user directory: OpenCode keeps a
  SQLite database holding sessions, messages, projects and workspaces, and a separate file holding
  authentication information including API keys; Codex keeps its authentication material in auth.json
  and the operator's prompt history in history.jsonl, alongside per-session rollout logs. Read one
  way this is an incident-response artefact map for a class of tooling that now runs shells on
  developer and CI endpoints. Read the other way it is an inventory of where an attacker with any
  foothold on such a host finds cleartext provider credentials and a transcript of the work.
discovered_at: "2026-08-10T04:48:00Z"
event_date: "2026-07-31"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, identity, cloud]
regions: [global, europe]
sectors: [public-sector, technology]
entities: [report:intrinsec-ai-agents-digital-forensics-series]
techniques: [T1552.001]
affected_products: ["OpenCode", "OpenAI Codex CLI"]
cves: []
sources:
  - url: "https://www.intrinsec.com/en/opencode-forensics/"
    publisher: "CERT Intrinsec"
    date: "2026-07-27"
    role: primary
  - url: "https://www.intrinsec.com/en/ai-agents-digital-forensics-openai-codex-artifacts/"
    publisher: "CERT Intrinsec"
    date: "2026-07-31"
    role: primary
closed_sources: []
evidence:
  - quote: "The most valuable artifact is the opencode.db which is a SQLite database storing sessions, messages, projects, workspaces, etc."
    publisher: "CERT Intrinsec"
  - quote: "This file contains authentication information such as API keys."
    publisher: "CERT Intrinsec"
verification: single-source
sourcing_note: >
  Both parts are CERT Intrinsec's own publications — one assessor, two documents, so credibility is 2.
  Note a defect in the source rather than in this entry: the published path strings on both pages
  render with their placeholder tokens missing, which this run verified in the raw markup is a
  fault on the live pages themselves. Directory and file names are therefore reported as stated,
  while the subdirectory-naming convention between them is not asserted here, because the source as
  published does not legibly state it.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Autonomous coding agents now run shells, install helpers and reach networks on developer and build endpoints, and this pipeline has already covered a case of one standing up a reverse tunnel and installing persistence on a real macOS developer machine. CERT Intrinsec's contribution is the responder-side counterpart: where these tools actually leave evidence ([CERT Intrinsec, 2026-07-27](https://www.intrinsec.com/en/opencode-forensics/), [CERT Intrinsec, 2026-07-31](https://www.intrinsec.com/en/ai-agents-digital-forensics-openai-codex-artifacts/)).

For OpenCode, an open-source agent shipped as a CLI, desktop application and IDE extension, configuration lives in a per-user `opencode` directory whose `opencode.json` records how the agent was set up. The artefact that matters most is a SQLite database — Intrinsec calls `opencode.db` "the most valuable artifact", "a SQLite database storing sessions, messages, projects, workspaces, etc." Its message table distinguishes model responses from user prompts by whether a timing field is present alongside the text, so an investigator can reconstruct both halves of a conversation and bound each response in time. A separate file in the same tree holds authentication material: "This file contains authentication information such as API keys."

For OpenAI's Codex CLI the shape is the same with different names. Everything sits under a per-user `.codex` directory; `auth.json` carries authentication information including API keys and access tokens; `history.jsonl` carries the list of user prompts; and per-session rollout logs record the session itself, including token-usage events that report input, cached-input, output and reasoning-token counts for the session and for the most recent response, plus the model's context window. That last detail is more useful than it first appears — it lets a responder estimate how much material an agent session actually processed without having to reconstruct the content.

The dual reading is the point. For incident response this is a map of where to look when a coding agent is implicated in an intrusion, and the prompt history is unusually valuable evidence because it records operator intent directly rather than by inference. For threat modelling it is an inventory: an attacker who reaches a developer workstation or a CI runner with any code execution finds provider credentials in cleartext JSON at a predictable per-user path, together with a transcript of what the organisation has been building. Neither file requires privilege escalation to read if the attacker already has the user's context.

**Defender takeaway:** treat these directories as credential stores, because that is what they are — bring them into the same scope as browser credential stores and cloud CLI configuration files for endpoint monitoring, and into scope for eviction after any developer-endpoint compromise, since an API key recovered from one survives the reimage of the host it came from. For the response side, capture the session database and prompt history before reimaging a suspect developer or build endpoint; they are the only record of what an agent was actually asked to do. Note the practical caveat in the source: the exact subdirectory layout is not legible on the published pages, so verify the paths against the agent version in your own estate rather than adopting them from any write-up, this one included.
