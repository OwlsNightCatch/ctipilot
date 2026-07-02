# Project memory — ctipilot.ch

This file is the index of `.claude/memory/`. Claude Code's built-in auto-memory feature is **redirected here** by the SessionStart hook (`.claude/hooks/setup-memory.sh`), which symlinks the system auto-memory directory (`~/.claude/projects/<project-hash>/memory/`) to this repo-local directory. Result: every memory Claude writes is **version-controlled** and **shared across all sessions** — local Claude Code, the cloud routine, every operator, every worktree.

The first 200 lines or 25 KB of this file are loaded into every session by the auto-memory feature. Topic files in this directory are loaded on demand when Claude reads them. Keep this index lean — move detail into topic files and shorten index entries.

## How it works

- **Local Claude Code:** the SessionStart hook fires, computes the project hash from the current working directory, and creates the symlink. Subsequent `/memory` writes land here. Approve the hook once when prompted.
- **Cloud routine:** same hook fires in the routine container. Memory writes land in the cloned repo. The routine's Phase 5 commits `.claude/memory/` alongside `state/` files, so the next routine fire (or a local session, or another operator) sees the accumulated memory.
- **Worktrees:** each git worktree has its own auto-memory directory by hash, but the hook in each worktree symlinks to *that worktree's* `.claude/memory/`. Since the directory is committed, all worktrees see the same content via git.

## Conventions for topic files

- One topic per file. Filename = short kebab-case slug. Examples: `source-failures.md`, `webfetch-quirks.md`, `deep-dive-rotation.md`, `check-brief-drift.md`, `publishing-races.md`.
- Front the file with a short YAML block: `name`, `description`, `type` (`user` / `feedback` / `project` / `reference`).
- Keep entries factual and dated when relevant. "Why" lines are useful — a fact without a why decays.
- Index entries here: `- [Title](file.md) — one-line hook` (≤150 chars).
- Update this index when you add, rename, merge, or remove a topic file.

## Index

- [Auto-commit/push/deploy for routine fixes](auto-publish-routine-fixes.md) — go end-to-end through commit→push→auto-merge→deploy-site→live URL without pausing for confirmation
- [Changelog hygiene](changelog-hygiene.md) — version history lives only in prompts/CHANGELOG.md; never annotate rules with vN.M; check_brief.py `prompt-version` gates it
- [Customization framework](customization-framework.md) — branding.yaml + org-profile.yaml carry ALL org/brand values; never reintroduce identity literals in build.py or lens phrases in prompt prose; PYTHONHASHSEED=0 for build byte-diffs
