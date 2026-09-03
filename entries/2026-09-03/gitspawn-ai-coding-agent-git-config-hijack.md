---
schema: 1
kind: vulnerability
title: "GitSpawn (CVE-2026-72718) — a hostile repository's own git config runs arbitrary commands during AI coding agents' routine startup housekeeping, before any trust prompt"
headline: "Opening a repository received as files, not cloned, can hand an attacker a shell before the agent has asked a single question"
summary: >
  Manifold Security discloses GitSpawn: seven CLI AI coding agents (Claude Code, Grok Build, Qwen Code, Hermes Agent,
  Goose, OpenAI Codex, Cursor) run ordinary git commands to gather repository context at startup, and those commands
  honour a repository's own `.git/config` — including the `core.fsmonitor` performance hook, which can name an
  arbitrary command git then executes with the developer's full privileges. Four of eight findings across the seven
  agents remain unpatched; delivery requires the `.git` directory to arrive as files (a zip, sync folder, or USB
  stick) rather than a clone.
discovered_at: "2026-09-03T05:13:00Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-03T0410Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, supply-chain, ai-abuse, rce, patch-available]
regions: [global]
sectors: [technology, public-sector]
entities:
  - tool:gitspawn-ai-coding-agent-git-config-hijack
techniques: [T1204.002, T1059]
affected_products: ["Anthropic Claude Code", "xAI Grok Build", "Alibaba Qwen Code", "Nous Research Hermes Agent", "Block Goose", "OpenAI Codex", "Cursor"]
cves:
  - id: CVE-2026-72718
    cvss: "7.0 (CVSS4.0)"
    epss: null
    type: rce
    vector: local
    auth: pre-auth
    status: [patch-available]
    affected: "Goose < 1.44.0"
    fixed: "1.44.0"
  - id: CVE-2026-19592
    cvss: "7.3 (CVSS3.1)"
    epss: null
    type: rce
    vector: local
    auth: pre-auth
    status: [patch-available]
    affected: "OpenAI Codex CLI 0.102.0 through 0.130.0"
    fixed: "0.131.0"
sources:
  - url: "https://www.manifold.security/blog/ai-coding-agents-git-hijack"
    publisher: "Manifold Security"
    date: "2026-09-01"
    role: primary
  - url: "https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html"
    publisher: "The Hacker News"
    date: "2026-09-02"
    role: corroborating
  - url: "https://www.heise.de/news/KI-Agenten-fuehren-git-Schadcode-beim-Starten-automatisch-aus-11437165.html"
    publisher: "heise Security"
    date: "2026-09-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Open a folder with Claude Code and it runs `git status` before you type anything. Before the workspace-trust prompt. On some agents, before you have even authenticated."
    publisher: "Manifold Security"
  - quote: "Delivery is worth being precise about, because git never carries this. Cloning a hostile URL does nothing, and neither does fetch or pull. The repository has to arrive as files with its `.git` directory already inside, so the vector is anything that moves a directory instead of cloning it: a shared `.zip`, a shared drive, a sync folder, a USB stick."
    publisher: "Manifold Security"
verification: multi-source
sourcing_note: >
  Goose's finding (CVE-2026-72718) and OpenAI's own Codex CVE (CVE-2026-19592) both carry published, NVD-resolvable
  CVE records with CVSS scores; the Hacker News source states OpenAI filed three CVEs of its own for the Codex
  variant, credited to three unrelated research groups, but only CVE-2026-19592 is named in the cited reporting —
  the other two are not carried here since no source names them. VulnCheck has separately assigned CVE-2026-71963
  to the equivalent Hermes Agent finding, per Manifold's own disclosure and independent Hacker News reporting, but
  that identifier had no published record in NVD, MITRE's CVE List, or CIRCL as of 2026-09-03 and is therefore not
  carried in this entry's structured cves[] record.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Before opening any repository received as files rather than cloned (a zip, sync folder, or USB stick), inspect its `.git/config` for a `core.fsmonitor` entry or any other setting naming an external program — treat any such entry as a live command, not configuration."
  - "Update every AI coding agent in use to its patched build now (Claude Code ≥ 2.1.196 for the `core.fsmonitor` sink, Goose ≥ 1.44.0, OpenAI Codex and Cursor current); Qwen Code, Grok Build, Hermes Agent, and Claude Code's separate `claude ultrareview` sink remain unpatched as of 1 September 2026 — restrict or avoid running these against repositories of uncertain provenance until fixed."
updates: []
migrated_from: null
---

Manifold Security's GitSpawn research starts from an operational fact about how CLI AI coding agents behave: on
opening a folder, several gather repository context by running ordinary git commands — `git status`, `git diff` —
before the agent has received a prompt, shown a workspace-trust dialog, or in some cases completed authentication
([Manifold Security, 2026-09-01](https://www.manifold.security/blog/ai-coding-agents-git-hijack)). Any git command
that refreshes the index honours the repository's own `.git/config`, including `core.fsmonitor`, a performance hook
where git hands the index refresh off to an external helper program named in that config file. A hostile
`.git/config` setting `[core] fsmonitor = <arbitrary command>` turns the agent's own routine startup housekeeping
into unconditional command execution, with no approval prompt and nothing shown on screen
([Manifold Security, 2026-09-01](https://www.manifold.security/blog/ai-coding-agents-git-hijack)). Delivery is
narrower than a typical supply-chain vector: cloning, fetching or pulling from a hostile URL does not carry
`.git/config` across, so the repository has to arrive as files with its `.git` directory already present — a
shared zip, a sync folder, a shared drive, or a USB stick, the way colleagues and consultants routinely hand off
projects ([Manifold Security, 2026-09-01](https://www.manifold.security/blog/ai-coding-agents-git-hijack)).

Manifold reports eight findings across seven agents, four of which remain unpatched at publication. Confirmed
patched: Goose's `git diff` sink during `goose review` (CVE-2026-72718, CVSS 4.0 7.0, fixed in 1.44.0), Claude
Code's `core.fsmonitor` sink (fixed in 2.1.196), OpenAI Codex, and Cursor. OpenAI separately disclosed and patched
three of its own CVEs for a distinct Codex helper mechanism in the same vulnerability class, crediting three
unrelated research groups; only CVE-2026-19592 is named in the cited reporting, describing a helper
that runs outside Codex's command sandbox without a user-approval prompt and can read, change or delete the user's
files
([The Hacker News, 2026-09-02](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html)).
Confirmed unpatched as of Manifold's
1 September 2026 recheck: Claude Code carries a second, separate sink in `claude ultrareview` — "not `core.fsmonitor`
... a different git setting of the same kind, one the review path does not strip," per Manifold, which withholds
the specific config key while it remains unfixed; Qwen Code's `git status` fires at startup, before authentication;
Grok Build's payload fires on the first keystroke, with an earlier July report on the same class closed by xAI as
"informative"; and Hermes Agent's `git status` on first message remains unpatched despite six contact attempts
across five channels, with VulnCheck assigning CVE-2026-71963 in the vendor's place
([Manifold Security, 2026-09-01](https://www.manifold.security/blog/ai-coding-agents-git-hijack);
[The Hacker News, 2026-09-02](https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html)).
Manifold states the underlying pattern is not limited to the named agents and spans both major AI labs and large
software companies
([heise Security, 2026-09-02](https://www.heise.de/news/KI-Agenten-fuehren-git-Schadcode-beim-Starten-automatisch-aus-11437165.html)).

Mitigation is two-sided: a defender receiving a repository as files should inspect `.git/config` before opening it
in any agent — any entry naming an external program is suspicious — and an agent vendor's own fix is to sanitise
the git config on context-gathering calls, e.g. `git -c core.fsmonitor=false status`
([Manifold Security, 2026-09-01](https://www.manifold.security/blog/ai-coding-agents-git-hijack)). **Triage:** a
git subprocess spawned by an AI coding agent that itself spawns a further, unrelated child process — particularly
one launched before the agent has logged any user prompt or shown a trust dialog — is not normal agent startup
behaviour and is the observable signature the mechanism supports. **Defender takeaway:** any organisation
standardising on a CLI AI coding agent should treat "received as files, not cloned" as its own trust boundary,
confirm which of the four still-unpatched sinks apply to the agents actually in use, and patch or restrict them
rather than assuming clone-based delivery covers every path a repository reaches a developer's machine.
