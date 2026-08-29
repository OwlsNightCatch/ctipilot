# Project memory — ctipilot.ch

Index of `.claude/memory/`. The SessionStart hook (`.claude/hooks/setup-memory.sh`) symlinks Claude Code's auto-memory directory here, so every memory write is version-controlled and shared across sessions (local, cloud routine, worktrees). This index loads into every session; topic files load on demand. Keep index lines short — detail belongs in the topic file.

Conventions: one topic per file, kebab-case filename, YAML front block (`name`, `description`, `type`: user/feedback/project/reference). Dated facts with why-lines; update the index on add/rename/merge/remove. Don't duplicate what CLAUDE.md or docs/pipeline.md already state — record the non-obvious delta.

## Index

- [Operator directives 2026-08-28](operator-directives-2026-08-28.md) — internal records, only `update` floats updated_at, no internals in reader text, quality>quantity, English-only quotes, v4.3 modifiability, xhigh effort, minimal plugins/skills
- [Permission rules: Edit covers Write](permission-rules-edit-covers-write.md) — Write(path) allow rules are dead; only Edit(path) matches file tools
- [Entry lifecycle](entry-lifecycle-v4.md) — one living entry per finding; changelog records + sections; what stays untouchable; the weekly's entries and schema are deleted (2026-08-29)
- [STIX export layer](stix-export-layer.md) — /stix/ bundles, uuid5 id-stability contract, relation collapse table, canonical ATT&CK ids, no TAXII by decision
- [Routine model assignment](routine-model-assignment.md) — Sonnet 5 intel / Opus 5 audit, generic `sonnet` pins at xhigh, single verifier, double-CLEAN; self-ID protocol (prompt line, not env vars)
- [Verification lessons](verification-lessons.md) — aiming iterations, testing findings before applying, inverted claims, unsourced status flags, quote fidelity, composing-from-entries traps
- [Source fetch blocks & recipes](source-fetch-blocks.md) — fetch ladder, blocked-host recipes, jina pool rules, PDF extraction honesty, probe/health traps
- [CSAF/MSRC/CVE transcription](csaf-msrc-transcription.md) — structured fields over prose; verdict vs membership; base vs temporal CVSS; CNA vs ADP vs NVD
- [Dedup: store-wide CVE index](dedup-store-wide-cve-index.md) — 14-day read is a floor; check `cves.ids` store-wide; read the covered entry's body
- [Scheduler & workflow races](scheduler-and-workflow-races.md) — operator-owned cadence, overtaken-run recovery, two local sessions in one worktree, pre-v3.33 durations are floors
- [Classifier trips on spawns](classifier-trips-on-spawns.md) — safeguards-flagged spawns: framing + checkpointing + pointer-not-enumeration; quiet output ≠ dead spawn
- [Classification policy](classification-policy.md) — one rating per entry; a press write-up of one lab report is not a second source
- [ATT&CK layer](attack-layer.md) — pinned dataset, revoked-id forwarding, evidence floor on mandatory mappings, never hardcode tactic tables
- [Product entities](product-entities.md) — affected_products[] resolves to `product:` keys at render; alias-merge not migration; products never phrase-match prose
- [Entity registry graph](entity-registry-graph.md) — typed relations[], tombstones, alias discipline, only relate what a source states
- [Triage-ready entries](triage-ready-entries.md) — actionability shape footnotes: migrated tier, vector vs auth semantics
- [State-file serialization](state-file-serialization.md) — derive JSON format from the live file, `git diff --stat` after; the constant has flipped twice
- [Auto-publish routine fixes](auto-publish-routine-fixes.md) — commit→push→merge→deploy→probe end-to-end without pausing; permissions pre-authorized
- [Customization framework](customization-framework.md) — branding.yaml + org-profile.yaml carry all identity; shipped profile = generic "Swiss Government Entities" example/POC (no concrete org anywhere); slices/cohorts/certs/policy-watch/site_url are config-only, no in-code defaults; never re-literal build.py; PYTHONHASHSEED=0 for byte diffs
- [Site landing = live brief](site-landing-live-brief.md) — 2026-08-29: / is the brief; findings lead, positioning at the foot, § Do now, phone-first timeline
- [Design system](design-system.md) — component/DOM contract, brandable surface, CSS invariants (no dlig, badge guards, trends honesty) + document contract (one heading outline, unique ids, AA in both themes)
- [UI writing style](ui-writing-style.md) — no em dash ANYWHERE a reader sees it; build.py normalises at render, self-check FAILs, <pre>/<code> exempt
- [Changelog hygiene](changelog-hygiene.md) — version history only in prompts/CHANGELOG.md; no vN.M annotations in rules
