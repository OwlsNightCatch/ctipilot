---
name: operator-directives-2026-08-28
description: "v4.2 operator directives — internal changelog records (no reader-facing message, no timestamp), only type update floats updated_at, no pipeline internals in entry text, quality over quantity below the critical bar, English-only including quotations, generic sonnet pins, Concise output style, heise/inside-it essential"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 755fb1b8-9924-4bd9-a0ad-d9807c992000
  modified: 2026-08-28T19:53:38.981Z
---

# Operator directives 2026-08-28 (shipped as prompt v4.2)

1. **Pipeline internals never reach the reader.** Metadata-only fixes (frontmatter/structured-field corrections with nothing to tell the reader) are `updates[]` records with `internal: true` — no `## <Type> — <at>` section, never rendered on the site, changelog-only. Composition-rationale narration in bodies ("`actions[]` is empty because…", "`techniques[]` maps only…", registry keys, "this pipeline/store/run") is a defect; the fix is deletion. The 2026-08-28T0409Z Sonnet fire produced this shape in most of its 36 entries and in the Lazarus `cves[]` correction the operator quoted back.
2. **Only `type: update` moves `updated_at`.** A correction or improvement "is not an update to the finding or story" (operator's words) — it never re-floats the entry in /live/. `updated_at` = last non-internal `type: update` record's `at`, null when none. Reader-facing corrections keep their sections (rendered on the entry page and day-page § Updates by record `at`).
3. **Quality over quantity.** Short, relevant, actionable beats more. Completeness stays a hard duty ONLY for critical/high signal; below that, a marginal item is dropped or held to two sentences. The brief must save the team time — if they have to re-triage it, it failed. PD-11 rebalanced accordingly.
4. **Always English, quotations included.** Non-English sources are quoted in English translation marked "(translated from <language>)"; the verbatim original goes in `evidence[].original` (optional field, renderer ignores it) so the verifier can still grep it against the fetched page.
5. **Model pins are the generic `sonnet` alias**, never a dated id (see [[routine-model-assignment]]).
6. **Concise output style** is set repo-wide in `.claude/settings.json` (`"outputStyle": "Concise"`).
7. **heise-sec and inside-it-ch are operator-named critical sources** → `tier: essential` (attempted every fire). Known constraint: heise article bodies need the jina reader (`fetch_method: jina`); with the pool exhausted (7/7 keys dead on 2026-08-28) heise is headline-only until the operator refills keys.
8. **Entry content is modifiable when changelog-tracked** (shipped as prompt v4.3, same day): the residual immutability guard on earlier sections is dropped — see [[entry-lifecycle-v4]].
9. **xhigh effort everywhere:** main-agent default `effortLevel: xhigh` in `.claude/settings.json`; both sub-agent definitions carry `effort: xhigh`.
10. **Minimal tool overhead:** all five `@claude-plugins-official` plugins disabled in `.claude/settings.json` (none is referenced anywhere in the repo); workflows disabled; irrelevant bundled skills `off`, interactively-useful ones (`code-review`, `simplify`, `security-review`, `update-config`) kept `user-invocable-only`. Re-enable a plugin only when a task genuinely needs it.
11. **Memory condensed 2026-08-28:** 28 topic files merged/condensed to 18; verifier lessons live in [[verification-lessons]]; the historical immutability-exception ledger and the weekly-synthesis file are deleted (surviving lessons folded into verification-lessons; v3 edit history remains in git and docs/audits/).

**Why:** the operator reviewed the first Sonnet 5 fire (2026-08-28T0409Z) and found internals leakage, stale-entry re-floating, verbosity, and untranslated German/French quotes; goal is a briefing highly relevant to very technical IR teams with zero re-triage overhead.

**How to apply:** follow prompts/cti-run.md v4.2 § Updating an existing entry, § Style rules, § Output discipline, and PD-11 — they encode all of this. When editing published entries for these defect classes, use `internal: true` improvement records. Related: [[entry-lifecycle-v4]], [[routine-model-assignment]], [[triage-ready-entries]].
