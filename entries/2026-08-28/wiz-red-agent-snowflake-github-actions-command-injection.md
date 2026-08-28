---
schema: 1
kind: research
horizon: operational
title: "Wiz's autonomous AI red-teaming agent found and exploited a GitHub Actions command-injection flaw in Snowflake's public connector repo, exfiltrating live Jira credentials via an out-of-band callback"
headline: "An AI red-team agent hit a syntax error mid-exploit, diagnosed it, fixed its own payload, and retried — without a human in the loop"
summary: >
  Wiz Research's autonomous "Red Agent" AI red-teaming tool independently discovered and exploited
  a GitHub Actions script-injection vulnerability in Snowflake's public snowflake-connector-net
  repository, undetected by GitHub Advanced Security despite sitting directly in the analysed
  workflow. When its initial payload hit a syntax error, the agent autonomously adjusted and
  retried, then received Jira API credentials via an out-of-band callback within seconds.
  Snowflake patched the same day.
discovered_at: "2026-08-28T06:34:00Z"
updated_at: null
event_date: "2026-06-23"
run_id: 2026-08-28T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, ai-abuse]
regions: [global]
sectors: [public-sector]
entities: [tool:wiz-red-agent]
techniques: [T1059, T1195.002, T1552.001]
affected_products: ["GitHub Actions", "snowflake-connector-net"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug"
    publisher: "Wiz Research"
    date: "2026-08-17"
    role: primary
closed_sources: []
evidence:
  - quote: "The injectable pattern was added to jira_issue.yml in commit 094038e and became live when PR #1218 was squash-merged as commit 4a1b8ce."
    publisher: "Wiz Research"
  - quote: "autonomously analyzed the syntax execution error"
    publisher: "Wiz Research"
  - quote: "adjusted its payload to use ; echo ' to properly close the shell block, and"
    publisher: "Wiz Research"
  - quote: "Within seconds, our listener received the callback from a GitHub Actions runner containing base64-encoded credentials."
    publisher: "Wiz Research"
  - quote: "Snowflake patched the workflow on June 23, 2026 (1dc7766, PR #1402), fully restoring the safe env: variable and jq --arg parsing pattern."
    publisher: "Wiz Research"
verification: single-source
sourcing_note: >
  Vendor-authored research about the vendor's own tool finding a real flaw in a third party's
  public repository — single-source narratively, but the underlying commits (PR #1218, commit
  4a1b8ce, PR #1402) are independently verifiable on GitHub, which anchors the technical claim
  beyond Wiz's own account.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Wiz Research's autonomous "Red Agent" AI red-teaming tool independently discovered and exploited a GitHub Actions script-injection vulnerability in Snowflake's public `snowflake-connector-net` repository, introduced via PR #1218 (18 June 2026) and undetected by GitHub Advanced Security despite the flaw sitting directly in the analysed workflow. The injectable pattern entered the `jira_issue.yml` workflow in commit `094038e` and went live when PR #1218 was squash-merged as commit `4a1b8ce`: "the injectable pattern was added to jira_issue.yml in commit 094038e and became live when PR #1218 was squash-merged as commit 4a1b8ce" ([Wiz Research, 2026-08-17](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)), allowing an unauthenticated actor to inject shell commands via a crafted GitHub issue title interpolated unsanitised into the workflow's shell step.

When the agent's initial payload (using `#` to comment out the rest of the line) hit an unexpected bash syntax error — the comment character also consumed the closing parenthesis of the shell's `TITLE=$(...)` construct — it did not stop or fail. Instead it "autonomously analyzed the syntax execution error" and "adjusted its payload to use ; echo ' to properly close the shell block, and" ([Wiz Research, 2026-08-17](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)) retried — recovering from its own exploitation error without human direction. Within seconds, Wiz's listener received an out-of-band callback from the GitHub Actions runner carrying base64-encoded Jira API credentials tied to a `qa@snowflake.net` account: "within seconds, our listener received the callback from a GitHub Actions runner containing base64-encoded credentials" ([Wiz Research, 2026-08-17](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug)). Snowflake patched the workflow the same day of disclosure (23 June 2026, commit `1dc7766`/PR #1402), restoring safe `env:` variable interpolation and `jq --arg` parsing.

This is a further, vendor-independent data point in the CI/CD trust-boundary thread this store has been building around GitHub Actions script injection. The autonomous-error-recovery behaviour — diagnosing a failed exploitation attempt and adjusting the payload without human intervention — is itself a capability marker worth tracking regardless of which side deploys it: the same recovery loop that let Wiz's defensive tool self-correct mid-exploit is available to an offensive operator running comparable tooling against any organisation's own public CI/CD workflows. **Triage:** GitHub Actions workflows that interpolate untrusted issue or pull-request titles directly into shell steps, rather than passing them through `env:` variables with `jq --arg`-style safe parsing, are the systemic pattern this flaw exemplifies — an audit of any organisation's public-repository workflows for this exact interpolation shape is the actionable takeaway, independent of this specific incident.
