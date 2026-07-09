---
schema: 1
kind: vulnerability
horizon: operational
title: "GhostApproval (CVE-2026-12958, CVE-2026-50549) — symlink + confirmation-UI misrepresentation lets a malicious repo write outside six AI coding assistants' workspace sandbox"
headline: "Wiz \"GhostApproval\": malicious repos escape the workspace sandbox of six AI coding assistants via symlink + fake confirmation dialog"
summary: >
  Wiz Research disclosed GhostApproval, a pattern combining symlink-following (CWE-61)
  with confirmation-dialog UI misrepresentation (CWE-451) across Amazon Q Developer,
  Cursor, Google Antigravity, Augment, Windsurf and Anthropic Claude Code. A malicious
  repository plants an in-workspace symlink resolving to a sensitive path (e.g.
  ~/.ssh/authorized_keys); the agent writes to the true target while the approval dialog
  shows the harmless in-workspace name — enabling host compromise. AWS (CVE-2026-12958)
  and Cursor (CVE-2026-50549) shipped fixes; Augment and Windsurf were unpatched at disclosure.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-08"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, ai-abuse, rce, poc-public, patch-available]
regions: [global]
sectors: [technology, public-sector, finance, telco]
entities: ["tool:ghostapproval-ai-coding-assistant-symlink"]
cves:
  - id: CVE-2026-12958
    cvss: "8.5"
    epss: null
    type: path-traversal
    vector: user-interaction
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "AWS Language Servers / Amazon Q Developer (@aws/lsp-codewhisperer) < 1.69.0 / < 0.0.117"
    fixed: "language-servers 1.69.0 / @aws/lsp-codewhisperer 0.0.117"
  - id: CVE-2026-50549
    cvss: null
    epss: null
    type: path-traversal
    vector: user-interaction
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "Cursor < 3.0"
    fixed: "Cursor 3.0"
sources:
  - url: "https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants"
    publisher: "Wiz Research"
    date: "2026-07-08"
    role: primary
  - url: "https://github.com/aws/language-servers/security/advisories/GHSA-6v3r-4p5c-mrp5"
    publisher: "AWS GitHub Security Advisory (GHSA-6v3r-4p5c-mrp5)"
    date: "2026-06-23"
    role: corroborating
  - url: "https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx"
    publisher: "Cursor GitHub Security Advisory (GHSA-3v8f-48vw-3mjx)"
    date: "2026-06-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The user approves what they believe is a harmless local edit; the agent writes to a sensitive file outside of the project workspace."
    publisher: "Wiz Research"
  - quote: "Missing symlink validation in Language Servers for AWS may allow an arbitrary file write outside of the workspace trust boundary."
    publisher: "AWS GitHub Security Advisory (GHSA-6v3r-4p5c-mrp5)"
  - quote: "A malicious agent could write arbitrary files outside the workspace under the user's privileges. This enables non-sandboxed Remote Code Execution."
    publisher: "Cursor GitHub Security Advisory (GHSA-3v8f-48vw-3mjx)"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Patch AWS language-servers to ≥ 1.69.0 (@aws/lsp-codewhisperer ≥ 0.0.117) and Cursor to ≥ 3.0 now; for Augment and Windsurf, restrict use against untrusted/external repositories until a fix ships."
  - "Alert on any AI-coding-assistant agent process writing to credential/dotfile paths (~/.ssh/*, shell rc files, cloud-credential files) and on git-clone operations that create symlinks resolving outside the repository root."
migrated_from: null
---

Wiz Research published **GhostApproval** on 8 July, a systematic vulnerability pattern combining `CWE-61` (symbolic-link following) with `CWE-451` (UI misrepresentation of critical information) found, in varying severity, across six AI coding assistants: Amazon Q Developer, Cursor, Google Antigravity, Augment, Cognition Labs' Windsurf and Anthropic's Claude Code ([Wiz Research, 2026-07-08](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants)). A malicious repository plants a symlink inside the workspace that resolves to a sensitive path outside it — e.g. a file named `project_settings.json` that is actually a link to `~/.ssh/authorized_keys` — then a README or prompt instructs the agent to "update" the file. In several tools the agent's own reasoning identifies the true target, yet the confirmation dialog still shows the harmless in-workspace name, so the user rubber-stamps a write to the real target, enabling persistent passwordless SSH access or other host compromise. Windsurf exhibited a **pre-authorization write** — the file was modified on disk before the Accept/Reject buttons even rendered, making the prompt an "undo" button rather than a gate.

AWS assigned **CVE-2026-12958** (missing symlink validation in Language Servers for AWS, CVSS 8.5, fixed in language-servers 1.69.0 / `@aws/lsp-codewhisperer` 0.0.117) and Cursor assigned **CVE-2026-50549** (sandbox escape via symlink + failed path canonicalization, fixed in Cursor 3.0), both confirming arbitrary out-of-workspace file write as the impact ([AWS GHSA-6v3r-4p5c-mrp5, 2026-06-23](https://github.com/aws/language-servers/security/advisories/GHSA-6v3r-4p5c-mrp5); [Cursor GHSA-3v8f-48vw-3mjx, 2026-06-05](https://github.com/cursor/cursor/security/advisories/GHSA-3v8f-48vw-3mjx)). Google fixed Antigravity (CVE pending at publication). Augment and Windsurf acknowledged the report but were still testable-vulnerable at disclosure ([Wiz Research, 2026-07-08](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants)). Anthropic assessed the report as outside its threat model for Claude Code — its stated rationale is that a user who starts a session in a directory has already extended trust to it — while noting it had shipped a symlink warning in the Edit/Write permission dialog in v2.1.32 (5 Feb 2026) as unrelated proactive hardening ([Wiz Research, 2026-07-08](https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants)). Mapped to `T1195.002 Compromise Software Supply Chain`, `T1222 File and Directory Permissions Modification` (via symlink) and `T1552.004 Unsecured Credentials` (authorized_keys write).

**Defender takeaway:** any public-sector or enterprise engineering team running these assistants against externally-sourced repositories is exposed regardless of the tool's own confirmation-dialog behaviour. Beyond patching, the durable control is to treat every AI-coding-assistant file write to credential/dotfile paths as high-severity and to canonicalize symlink targets before trusting an "Accept" prompt — the confirmation must be a gate, not an undo.
