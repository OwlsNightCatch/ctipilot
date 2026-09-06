---
schema: 1
kind: threat
title: "Datadog Security Labs analyzes leaked TeamPCP \"Shai-Hulud\" offensive framework source code"
headline: "Datadog Security Labs analyzes leaked TeamPCP \"Shai-Hulud\" offensive framework source code"
summary: "UPDATE (2026-05-13 — follows TeamPCP coverage 2026-05-13): Datadog Security Labs published an analysis of the TeamPCP \"Shai-Hulud\" offensive worm source code on 2026-05-13, after the complete framework was briefly accessible as a public GitHub repository on 2026-05-12 before the account was removed (Datadog …"
discovered_at: "2026-05-15T05:00:10Z"
event_date: 2026-05-13
run_id: 2026-05-15-58b94fbd
priority: notable
immediate_action: null
tags:
  - supply-chain
  - vulnerabilities
regions:
  - global
sectors:
  - technology
entities:
  - "actor:teampcp"
cves: []
sources:
  - url: "https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/"
    publisher: "Datadog Security Labs, 2026-05-13"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: "migration: update target unresolved (no originally-covered date in v2 body)"
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-15.md
---

**UPDATE (2026-05-13 — follows TeamPCP coverage 2026-05-13):** Datadog Security Labs published an analysis of the TeamPCP "Shai-Hulud" offensive worm source code on 2026-05-13, after the complete framework was briefly accessible as a public GitHub repository on 2026-05-12 before the account was removed ([Datadog Security Labs, 2026-05-13](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)). The brief public exposure gave researchers direct visibility into the worm's internal architecture: it is a TypeScript/Bun toolkit that automates GitHub Actions pwn-request exploitation — specifically targeting `pull_request_target` workflows that perform unsanitized checkouts — to harvest OIDC tokens and `GITHUB_TOKEN` values, then propagate across npm packages using the stolen credentials. The automation is fully self-contained; victim-repository selection is not manually guided, consistent with the worm-class spread observed in the original TanStack campaign. The leaked code also exposes the environment-variable injection technique (`${{ github.event.pull_request.head.sha }}` substitution in run steps) as a key primitive. Defenders should **not** execute the leaked code. The architectural disclosure accelerates defensive posture: prioritise auditing `pull_request_target` triggers with `checkout` steps in the same job, review OIDC token permission scopes, and apply environment variable sanitization. MITRE ATT&CK: T1195.002 (Compromise Software Supply Chain), T1552.001 (Credentials in Files), T1059.004 (Unix Shell).
