---
schema: 1
kind: threat
horizon: operational
title: "Hijacked npm and Go packages weaponise VS Code's folderOpen task autorun to drop a credential-stealing Python implant"
headline: "Hijacked npm and Go packages weaponise VS Code's folderOpen task autorun to drop a credential-stealing Python implant"
summary: "JFrog Security Research disclosed two compromised npm packages (html-to-gutenberg v4.2.11, fetch-page-assets v1.2.9, uploaded 2026-05-25) plus 16 malicious Go packages carrying an identical chain (JFrog Security Research, 2026-06-24 · The Hacker News, 2026-06-29)."
discovered_at: "2026-06-30T05:10:35Z"
event_date: 2026-06-29
run_id: 2026-06-30-9aaa1114
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - identity
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://research.jfrog.com/post/hijacked-npm-vscode-tasks-blockchain/"
    publisher: JFrog Security Research
    role: primary
  - url: "https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html"
    publisher: The Hacker News
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-30.md
---

JFrog Security Research disclosed two compromised npm packages (`html-to-gutenberg` v4.2.11, `fetch-page-assets` v1.2.9, uploaded 2026-05-25) plus 16 malicious Go packages carrying an identical chain ([JFrog Security Research, 2026-06-24](https://research.jfrog.com/post/hijacked-npm-vscode-tasks-blockchain/) · [The Hacker News, 2026-06-29](https://thehackernews.com/2026/06/hijacked-npm-and-go-packages-use-vs.html)). A hidden `eslint-check` task in `.vscode/tasks.json` is configured with `runOn: "folderOpen"`, so opening the project as a trusted workspace in VS Code or Cursor auto-executes the payload — deliberately sidestepping npm v12's lifecycle-script hardening that blocked `preinstall`/`postinstall` scripts by default. The payload (disguised as a `fa-solid-400.woff2` font) pulls AES-encrypted stages from blockchain transaction data via TronGrid and Aptos APIs (a takedown-resilient dead-drop), then runs a cross-platform Python infostealer targeting browser stores, password managers, crypto wallets, and cloud-provider configs (AWS/Azure/GCP). Mapped to `T1195.001`, `T1059.006`, `T1020`.

**Why it matters to us:** Detection teams that added EDR coverage for `node.exe`→`python` chains under `npm install` will miss this — the parent is `code.exe`→`python` triggered by *opening a folder*. Add a CI/CD repository-scan rule for `.vscode/tasks.json` containing `runOn: "folderOpen"`, and treat dependency-shipped `.vscode/` directories as untrusted; enforce VS Code Workspace Trust so untrusted folders cannot auto-run tasks.
