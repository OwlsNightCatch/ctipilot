# Project memory — ctipilot.ch

This file is the index of `.claude/memory/`. Claude Code's built-in auto-memory feature is **redirected here** by the SessionStart hook (`.claude/hooks/setup-memory.sh`), which symlinks the system auto-memory directory (`~/.claude/projects/<project-hash>/memory/`) to this repo-local directory. Result: every memory Claude writes is **version-controlled** and **shared across all sessions** — local Claude Code, the cloud routine, every operator, every worktree.

The first 200 lines or 25 KB of this file are loaded into every session by the auto-memory feature. Topic files in this directory are loaded on demand when Claude reads them. Keep this index lean — move detail into topic files and shorten index entries.

## How it works

- **Local Claude Code:** the SessionStart hook fires, computes the project hash from the current working directory, and creates the symlink. Subsequent `/memory` writes land here. Approve the hook once when prompted.
- **Cloud routine:** same hook fires in the routine container. Memory writes land in the cloned repo. The routine's Phase 5 commits `.claude/memory/` alongside `state/` files, so the next routine fire (or a local session, or another operator) sees the accumulated memory.
- **Worktrees:** each git worktree has its own auto-memory directory by hash, but the hook in each worktree symlinks to *that worktree's* `.claude/memory/`. Since the directory is committed, all worktrees see the same content via git.

## Conventions for topic files

- One topic per file. Filename = short kebab-case slug. Examples: `source-failures.md`, `webfetch-quirks.md`, `deep-dive-rotation.md`, `check-run-drift.md`, `publishing-races.md`.
- Front the file with a short YAML block: `name`, `description`, `type` (`user` / `feedback` / `project` / `reference`).
- Keep entries factual and dated when relevant. "Why" lines are useful — a fact without a why decays.
- Index entries here: `- [Title](file.md) — one-line hook` (≤150 chars).
- Update this index when you add, rename, merge, or remove a topic file.

## Index

- [Auto-commit/push/deploy for routine fixes](auto-publish-routine-fixes.md) — go end-to-end through commit→push→auto-merge→deploy-site→live URL without pausing; memory writes are pre-authorized in settings.json (`permissions.allow`) so they never prompt/interrupt
- [Changelog hygiene](changelog-hygiene.md) — version history lives only in prompts/CHANGELOG.md; never annotate rules with vN.M; check_run.py `prompt-version` gates it
- [Customization framework](customization-framework.md) — branding.yaml + org-profile.yaml carry ALL org/brand values; never reintroduce identity literals in build.py or lens phrases in prompt prose; PYTHONHASHSEED=0 for build byte-diffs
- [Design system](design-system.md) — the site's visual language = the "CTI Pilot Design Modernization" Claude Design project; component classes + brandable surface (nav/hero/ai-bar copy, accent-rgb auto-derived); DOM/JS contract for the new shell + live timeline; routes are /live/ (rolling), /daily/ (completed days only, excludes rolling day), /weekly/
- [UI writing style](ui-writing-style.md) — NEVER use em dashes (—) in UI chrome (titles, labels, tooltips, footer, hero/ai-bar); use ·/:/, instead; empty cells use en dash –; entry/brief CONTENT may use them sparingly (agent freedom)
- [Model identity & verifier rotation](model-identity-and-rotation.md) — self-ID primary source (v3.15) is the harness-injected "You are powered by…" line in each agent's OWN system prompt: pin-aware, probe-verified 2026-07-09 (pinning/rotation DO work); CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID are container-scoped, blind to `model:` pins, marked-fallback only; uniform env-fallback reports ≠ rotation failure
- [Source fetch blocks & primary-source substitutes](source-fetch-blocks.md) — fetch ladder RSS→WebFetch→jina→bridge; r.jina.ai reader is now a GENERAL transport (`jina <URL>`, universal fallback, recovered group-ib + ccn-cert); github.com egress-proxy-blocked → OSV.dev; CISA Akamai → `cisa page/feed/csaf`; kernel.org Anubis → distro trackers; coe.int/seppmail 401 even to reader = still blocked
- [Entity registry graph conventions](entity-registry-graph.md) — v3.16: name = canonical entity name only, aliases load-bearing (dedup + phrase matching); duplicates → `merged_into` tombstones (referenced keys) or deletion (orphans); `related: []` = curated evidence-bound edges; never reference a tombstone in new entries
- [State-file serialization](state-file-serialization.md) — sources.json canonical format is `indent=1, ensure_ascii=False`; re-dumping with indent=2/ascii flips every line into a ~6400-line churn diff; bump in place
- [Triage-ready entries](triage-ready-entries.md) — v3.13 actionability shape: observable behavior in vendor-neutral telemetry classes, `techniques[]`/`affected_products[]` frontmatter, `**Triage:**` discriminator omitted-never-invented; migrated_from != null = lower-fidelity tier
- [MITRE ATT&CK layer](attack-layer.md) — v3.17: pinned `attack/enterprise-attack.json` (tools/attack_data.py; weekly --check duty; NEVER hardcode tactic tables — v19 renamed them); `techniques[]` = canonical complete mapping surface, prose readable without T-numbers; entity/CVE TTPs derived evidence-bound; /attack/ overlap matrix + Navigator layers; revoked ids forward like tombstones
- [Scheduler outages & workflow races](scheduler-and-workflow-races.md) — 2026-07-07 62h gap was a CONFIRMED scheduler outage (not repo-side); compose-profile × auto-merge branch-delete race fixed via fallback-to-main; sources.json ensure_ascii drift symptom
- [Entry immutability exceptions](entry-immutability-exceptions.md) — audit log of operator-authorized entry edits; 2026-07-09: the four v2→v3 dangling update_of links repaired (frontmatter repoint only), --all now fully green
