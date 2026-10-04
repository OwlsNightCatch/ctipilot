---
schema: 1
kind: research
title: "Coding-agent CI harnesses broke on the same trust boundary three different ways — and the two findings that matter most carry no CVE at all"
headline: "A validator that strips quoted text before inspecting it, and an agent instruction file rewritten between two passes of one shared checkout"
summary: >
  Novee Security's Black Hat USA 2026 write-up root-causes trust-boundary failures in AI coding-agent
  CI harnesses, each tested against the vendor's own public repository in default configuration.
  Against Claude Code Action it reports three successive rounds of patch-and-bypass, of which only
  the last — an allowlist entry that pre-approved a bare hostname for the fetch tool — carries
  CVE-2026-54316; the two more instructive rounds, a command validator that strips single-quoted
  content before inspecting it and a read-only allowlist exempt from path checking, carry no
  identifier. A Gemini CLI harness flaw is tracked as CVE-2026-12537. The third finding, an OpenAI
  Codex workflow whose two agent passes shared one checkout so the first could rewrite the
  instruction file the second treats as authoritative, has no CVE and was fixed only in the vendor's
  own repository.
discovered_at: "2026-08-10T04:59:00Z"
updated_at: null
event_date: "2026-08-05"
run_id: 2026-08-10T0411Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse, supply-chain, patch-available, identity]
regions: [global, europe]
sectors: [public-sector, technology]
entities: [trend:coding-agent-ci-harness-trust-boundary-2026-08, trend:claude-code-action-github-issue-supply-chain]
techniques: [T1195.002, T1552, T1567, T1059.004]
affected_products: ["Anthropic Claude Code", "Google Gemini CLI", "OpenAI Codex"]
cves:
  - id: CVE-2026-54316
    cvss: "6.0"
    epss: null
    type: logic-flaw
    vector: user-interaction
    auth: pre-auth
    status: [patch-available]
    affected: "claude-code from 0.2.54 until 2.1.163"
    fixed: "2.1.163"
  - id: CVE-2026-12537
    cvss: "10.0 (Google)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "@google/gemini-cli < 0.39.1; google-github-actions/run-gemini-cli < 0.1.22"
    fixed: "gemini-cli 0.39.1; run-gemini-cli 0.1.22"
sources:
  - url: "https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/"
    publisher: "Novee Security"
    date: "2026-08-05"
    role: primary
  - url: "https://github.com/anthropics/claude-code/security/advisories/GHSA-fg94-h982-f3mm"
    publisher: "Anthropic (GitHub Security Advisory)"
    date: "2026-06-13"
    role: corroborating
  - url: "https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g"
    publisher: "OSV"
    date: "2026-04-24"
    role: corroborating
  - url: "https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g"
    publisher: "Google (GitHub Security Advisory)"
    date: "2026-04-24"
    role: primary
closed_sources: []
evidence:
  - quote: "It is loaded from disk on every single invocation and injected as instructions the model treats as authoritative"
    publisher: "Novee Security"
  - quote: "3 Days after our report they fixed it and the two passes on openai/codex were split into separate jobs, each with its own checkout"
    publisher: "Novee Security"
  - quote: "Because the hostname huggingface.co was pre-approved as a bare hostname for the WebFetch tool, any path on that domain—including attacker-controlled model repositories—was auto-approved without a permission prompt or being subject to --allowedTools restrictions."
    publisher: "Anthropic (GitHub Security Advisory)"
verification: multi-source
sourcing_note: >
  The write-up is the technical primary. Identifier binding is stated carefully because it is easy to
  get wrong: Anthropic's advisory assigns CVE-2026-54316 specifically to the pre-approved bare
  hostname in the fetch-tool allowlist, not to the command-validator or path-check rounds described
  alongside it, which carry no identifier. Google's advisory gives the rating, vector and fixed
  versions but lists no CVE. The CVE-2026-12537 alias comes from the OSV record for that advisory.
  Both CVEs predate this write-up by weeks to months and were already fixed, so the value here is
  the mechanism plus one new finding, not fresh vulnerability news. The OpenAI Codex finding carries
  no CVE or advisory from any party, an absence confirmed rather than an omission.
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
actions:
  - "Audit any CI workflow where two or more agent passes share a single checkout — the Codex fix was to split the passes into separate jobs each with its own checkout, and that change has to be made in your own pipelines because no vendor patch reaches them."
updates:
  - at: "2026-08-28T04:55:00Z"
    run_id: 2026-08-28T0409Z-intel
    type: correction
    summary: >
      CVE-2026-12537 (Google Gemini CLI) carries two sharply divergent official severity
      ratings: the assigning CNA rates it CVSS 4.0 10.0 CRITICAL with no user interaction and
      no authentication required, while NVD's own CVSS 3.1 assessment is 7.8 with a local
      vector and user interaction required. Both ratings are now recorded here; the CNA's
      unauthenticated zero-click rating is the more severe and should drive triage.
    fields:
      - cves
      - body
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      v4.2 migration: the 2026-08-28 CVSS-divergence correction rewritten reader-facing 
      (record-field narration removed); updated_at recomputed under the new float rule.
    fields: [updated_at, body]
  - at: "2026-09-30T07:18:24Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The severity of CVE-2026-12537 came from the NVD record rather than a cited advisory, and showed a 7.8 rating with a local, user-interaction vector beside the 10.0. The rating, vector
      and fixed versions now cite Google's own advisory, which gives only the network-reachable
      10.0, with OSV kept for the CVE alias. The 7.8 figure is removed from the text and the
      structured score, and a self-reference to other coverage is removed from the text.
    fields: [cves, body, sourcing_note, sources]
migrated_from: null
---

Three AI coding-agent CI harnesses were broken in different ways by the same underlying question: what, inside an automated pipeline, is the agent allowed to treat as authoritative? Novee Security tested each against the vendor's own public repository in default configuration ([Novee Security, 2026-08-05](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/)).

The Claude Code Action work is best read as three successive rounds of patch-and-bypass, and only the last of them carries an identifier. Round one turned on an ordering mistake in defensive code: the command-injection validation pipeline strips single-quoted content before inspecting a command, a sensible-looking measure to avoid false positives on shell metacharacters inside string literals. That means an injected payload placed inside single quotes is examined only after the interesting part has been removed. A validator that sanitises its input before deciding whether the input is dangerous is checking something other than what will execute. Round two was an asymmetry in the allowlist itself, where commands classed as read-only were exempted from path checking, so a read-only utility could be pointed at any file on the runner. Neither round carries a CVE. The identifier belongs to the third round, and Anthropic's own advisory states what it covers: "Because the hostname huggingface.co was pre-approved as a bare hostname for the WebFetch tool, any path on that domain—including attacker-controlled model repositories—was auto-approved without a permission prompt or being subject to --allowedTools restrictions." The advisory records the affected range as 0.2.54 up to 2.1.163 and the fix in 2.1.163 ([Anthropic, 2026-06-13](https://github.com/anthropics/claude-code/security/advisories/GHSA-fg94-h982-f3mm)). The Google finding is tracked as CVE-2026-12537 ([OSV, 2026-04-24](https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g)). Google's own advisory rates it Critical, CVSS 10.0, and fixes it in `@google/gemini-cli` 0.39.1 and `run-gemini-cli` 0.1.22 ([Google, 2026-04-24](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g)).

Both of those were patched weeks to months before the write-up appeared, so for those two vendors the action is a version check, not an incident. Their mechanics are still worth carrying, because the lesson generalises to anyone building command allowlists rather than merely consuming these products. In the Gemini CLI finding, where the environment was sanitised only for a child process, the write-up's phrasing of the step that reached the runner's secrets is worth quoting for how narrow the distinction is: "cat /proc/$PPID/environ reads the parent, not self, and pulls from the process that still holds every single thing the isolation was built to keep away." ([Novee Security, 2026-08-05](https://novee.security/blog/critical-flaws-in-anthropic-google-and-openais-coding-agents/))

The third finding is the one that is genuinely current, and it has no CVE because, as the researchers observe, nobody files one for newly documented behaviour. In an OpenAI Codex workflow, two agent passes ran over a single shared checkout, and the agent's own default instruction file sat in that checkout outside the protected-metadata set. That file "is loaded from disk on every single invocation and injected as instructions the model treats as authoritative" — so a first pass induced to modify it dictates what the second pass believes it has been told to do. The fix was structural rather than a patch: "3 Days after our report they fixed it and the two passes on openai/codex were split into separate jobs, each with its own checkout." That change landed in the vendor's own repository. It does not propagate to anyone else's pipeline, because the flaw is not in a shipped component — it is in a workflow shape.

**Defender takeaway:** the transferable rule is that an agent's instruction file is executable input, and any pipeline stage that can write it controls every later stage that reads it. Where a public-sector organisation runs coding agents in CI, the questions to ask are whether multiple agent passes share a workspace, whether the agent's instruction file is treated as protected metadata or as ordinary repository content, and — for the two patched products — whether the versions in use are past the fixed releases. The first of those has no vendor answer at all, and it is also the one no CVE feed will ever tell you about.

## Correction — 2026-08-28T04:55:00Z

Google rates the flaw CVSS 10.0, the maximum score, in its own advisory, with a network-reachable, no-privilege, no-interaction CVSS 3.1 vector, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`, and the fixes in `@google/gemini-cli` 0.39.1 and `run-gemini-cli` 0.1.22 ([Google, 2026-04-24](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g)). OSV maps that advisory to CVE-2026-12537 ([OSV, 2026-04-24](https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g)). Triage should follow that zero-click, unauthenticated rating.

## Correction — 2026-09-30T07:18:24Z

Google's own advisory, GHSA-wpqr-6v78-jr5g, rates the flaw Critical, CVSS 10.0, with a network-reachable, no-privilege, no-interaction vector, and fixes it in `@google/gemini-cli` 0.39.1 and `run-gemini-cli` 0.1.22 ([Google, 2026-04-24](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g)). OSV maps that advisory to CVE-2026-12537 ([OSV, 2026-04-24](https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g)). Google's advisory carries only that network-reachable 10.0 rating, not the 7.8 rating with a local, user-interaction vector shown earlier, so triage follows Google's rating.
