**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-31T07:09:51Z · ended_at=2026-08-31T07:24:55Z · duration_seconds=904

## Verification report — 2026-08-31T0411Z-intel (iteration 6)

### Prior-iteration deltas — walked and confirmed

All nine iteration-5 remediations were re-verified against freshly fetched sources this iteration:

1. Manchester Airports title/headline rewrite — confirmed accurate and correctly hedged ("FulcrumSec later claims credit" / "later claimed by FulcrumSec"), matches the update section and BleepingComputer's own text exactly. Fields correctly added to the record's declared `fields`. No residual issue.
2. PurpleDelta camera-model detail — confirmed verbatim against Huntress ("Registered that an `iPhone 15 Pro Max back triple camera 6.765mm f/1.78` was used to take the photos"); body prose now matches the changelog summary. No residual issue.
3. PurpleDelta PiKVM/ethernet timing — confirmed against Huntress's own timestamps (16:51:24 wireless → 21:12:31 PiKVM = ~4h21m ≈ "just hours"; 21:12:31 PiKVM → 21:26:54 ethernet = ~14m23s ≈ "roughly 15 minutes"). Both figures now check out arithmetically against the four cited timestamps. No residual issue.
4. Norway "neither…itself targeted" reword — see new finding #2 below; the reword did not remove the underlying unsupported claim, it only changed its surface form.
5. `entities_added[]` omissions — confirmed `actor:aplagroup` and `campaign:terminalfix-clickfix-reverse-tunnel-2026` are now both listed and both exist in `entities/registry.yaml`. No residual issue.
6. WatchGuard twelfth-CVE clause — confirmed against BSI's own CSAF JSON (`wid-sec-w-2026-3068.json`): 12 external CVE references including CVE-2026-81851 "Fireware OS Heap-Based Buffer Overflow in iked Allows Denial of Service," title matches verbatim; WatchGuard's own blog lists only 11. `cves_seen.json` carries the CVE-2026-81851 record. No residual issue.
7. Transparency-Register decline — confirmed both `state/coverage_backlog.md` rows exist as described (2026-08-31 rows for the FT/Swiss-wealth-managers lead and the NZZ access-vector lead). A fresh web search corroborates the FT headline is circulating only through derivative/content-farm rewrites (cryptobriefing.com, brinztech.com, a likely-spoofed "coindesk.cc") with no Swiss-domestic or FT-direct pickup found — the decline to compose is defensible.
8. Norway inclusion-rationale correction — confirmed the run record's coverage note now states the direct-nexus rationale.
9. Run-record "spawns" sweep — confirmed no `.claude/memory/` path or `spawn`/`sub-agent`/`main agent` term remains in the run record's reader-facing prose (S1–S4 letter codes retained as documented, legitimate cross-references).

### Unsupported / hallucinated facts

**#1 (high confidence).** `2026-08-31/ai-infrastructure-litellm-ragflow-kestra-intrusions` — the frontmatter `title` states "each converging on credential theft, persistence and compute monetisation" and the `summary` states "All three converged on credential harvesting, durable persistence and compute monetisation despite different initial-access paths." Both directly contradict the entry's own body, which states (Case 2, unchanged since iteration 4's fix): "Unlike the LiteLLM case, Microsoft observed no miner deployment or interactive shell here — the objective was narrowly future-credential interception," and the "pattern that matters" paragraph: "resource monetisation converged in two of the three (LiteLLM's cryptomining, Kestra's cluster-wide XMRig deployment), while the RAGFlow intrusion pursued only future-credential interception with no miner or interactive shell observed." Microsoft's own attacker-objective table (fetched this iteration) lists RAGFlow's objective as "Intercept newly configured LLM provider credentials and model metadata" only — no monetisation. Iteration 4 fixed exactly this overstatement in the intro paragraph and the "pattern that matters" paragraph but did not propagate the fix to the `title`/`summary` frontmatter fields, which still carry the pre-fix claim verbatim. Fix: reword title/summary to state monetisation converged in two of three (LiteLLM, Kestra) while RAGFlow's objective was narrower, matching the now-corrected body.

**#2 (low confidence).** `2026-08-31/norway-digdir-id-porten-ddos-third-attack` — body states "authorities warned of possible problems reaching online pharmacies and the electronic prescription system, both dependent on ID-porten for authentication rather than themselves attacked" ([The Record, 2026-08-25]). Fetched The Record this iteration: "The disruption also affected parts of Norway's health infrastructure because several health services rely on ID-porten for authentication. Authorities warned of possible problems accessing online pharmacies and Norway's electronic prescription system." The Record states the authentication dependency but never states these systems were "not themselves attacked" — that clause is still an added inference. Iteration 5 recorded this exact finding ("neither of which was itself targeted... that clause was an added inference") and applied a reword, but the reword ("rather than themselves attacked") retains the same unsupported assertion in different words rather than removing it. Fix: drop "rather than themselves attacked," ending the clause at "...both dependent on ID-porten for authentication."

### Editorial / less-is-more flags (advisory)

**#1 (moderate confidence).** `2026-08-31/ai-infrastructure-litellm-ragflow-kestra-intrusions` `techniques[]` maps `T1059.006` (Python) but omits `T1059.004` (Unix Shell) despite the body and Microsoft's own source repeatedly describing bash/shell execution as a distinct behavior: Case 1 — "a parallel shell-based delivery path provided redundancy" (source: "A second delivery path used a shell-stage downloader... invoked a shell"); Case 3 — "Two closely timed workflow-origin shell sessions followed" and "retrieved and executed a remote script via a curl-pipe-shell pattern" (source Defender-detections table: "the Java worker to spawn a bash reverse shell"). `T1059.004` is confirmed active/non-revoked in the pinned `attack/enterprise-attack.json`. This is the same kind of gap iteration 3 already fixed once for `T1518`/`T1095`; `T1059.004` appears to have been missed in that pass.

**#2 (moderate confidence, pre-existing — not introduced by this run).** `2026-08-15/france-dgfip-tax-authority-credential-intrusion` — six of the entry's eight `evidence[]` records carry the `quote` field in French with no English translation and no `original:`/`(translated from French)` marker (the French government primary, the Ministry of Education quotes via franceinfo, and the DGCCRF quote). This is the reader-facing v4.2 translation contract this same entry's two newest evidence records (added by this run, 2026-08-31) correctly follow (English `quote:` + French `original:` + "translated from French" in body prose). The six untranslated records were already present before this run (git diff confirms this run did not touch them) — flagging for awareness/future correction since the whole entry was in scope to read this iteration, not as a defect this run caused.

**#3 (low confidence, pre-existing, already surfaced by `check_run.py`).** `2026-08-15/france-dgfip-tax-authority-credential-intrusion` — the 2026-08-21 `updates[]` record's `summary` contains "this pipeline is covered" style phrasing ("the DGFiP tax-authority intrusion this pipeline covered on 2026-08-15"), a workflow-internal term. `check_run.py --pre-verify` already flags this as a `reader-text-internals` WARN and the run's own confirmation notes correctly identify it as settled history on an append-only prior record, not something this run introduced or can fix without a new correction record. Included here only for completeness per the "read the whole entry" instruction.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 3)

Everything else checked this iteration was clean: all inline URLs across the 6 new entries and the 3 updated entries' new sections resolved to specific articles/advisories and supported the attached claims (WatchGuard PSIRT ×3 + BSI CSAF; Digdir status page + The Record; ZATAZ ×3 + Clubic + Objectif Gard; Microsoft TerminalFix blog; Microsoft AI-infrastructure blog + 3 GHSA/CIRCL CVE authorities; BleepingComputer + Security Affairs; Huntress DPRK report; DGFiP govt release + radiofrance.fr); every `cves[]` id/CVSS/vector/affected-range cross-checked directly against its owning PSIRT/GHSA/CIRCL page; entity-registry links resolved to canonical (non-tombstoned) keys including the France-Éducation-nationale merge fixed in iteration 2; no IOCs, no vanity metrics, no remaining workflow-internal language in reader-facing text found beyond the pre-existing item noted above; classification blocks present and plausible on all 9 entries; `actions[]` lists are short and concrete (4 total across 9 entries, matching `check_run.py`'s own count); relevance/priority calibration reasonable across the run (WatchGuard `high` for an unauthenticated pre-auth RCE pair with patch available and no exploitation — correctly not `critical`; Norway `notable` with a correctly-stated direct-nexus rationale; SDIS `notable`; TerminalFix and the AI-infrastructure deep dive both `high`, matching the do-now bar for genuinely new techniques/confirmed real-world intrusions). No further missed-angle candidates identified beyond the ones already logged to `state/coverage_backlog.md` this run.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-31/ai-infrastructure-litellm-ragflow-kestra-intrusions"
  url_or_quote: "title: \"...each converging on credential theft, persistence and compute monetisation\"; summary: \"All three converged on credential harvesting, durable persistence and compute monetisation...\""
  summary: "Contradicts the entry's own body (Case 2/RAGFlow: 'Microsoft observed no miner deployment or interactive shell here... narrowly future-credential interception'; 'pattern that matters' paragraph: 'resource monetisation converged in two of the three... while the RAGFlow intrusion pursued only future-credential interception') and Microsoft's own attacker-objective table (RAGFlow objective: credential/metadata interception only, no monetisation). Iteration 4 fixed this exact overstatement in the body but the frontmatter title/summary still carry the pre-fix claim."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-31/norway-digdir-id-porten-ddos-third-attack"
  url_or_quote: "\"...both dependent on ID-porten for authentication rather than themselves attacked\""
  summary: "(low confidence) The Record states the authentication dependency but never states these systems were 'not themselves attacked' — this is a residual unsupported inference; iteration 5's reword changed the wording but retained the same unsupported claim in different form."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-08-31/ai-infrastructure-litellm-ragflow-kestra-intrusions"
  url_or_quote: "techniques: [..., T1059.006, ...] (no T1059.004)"
  summary: "(moderate confidence) techniques[] maps T1059.006 (Python) but omits T1059.004 (Unix Shell) despite body/source describing shell-based execution ('a parallel shell-based delivery path', Kestra 'bash reverse shell', 'curl-pipe-shell pattern', 'workflow-origin shell sessions'). T1059.004 is confirmed active in the pinned ATT&CK dataset."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-15/france-dgfip-tax-authority-credential-intrusion"
  url_or_quote: "evidence[0..5].quote fields in French, no original:/translation marker"
  summary: "(moderate confidence, pre-existing, not introduced by this run) Six of eight evidence[] records carry untranslated French quote text with no original:/'(translated from French)' marker, unlike this run's two newly added records which correctly follow the v4.2 translation contract. Pre-existing since before this run per git diff; flagged for awareness under the 'read the whole entry' instruction."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-15/france-dgfip-tax-authority-credential-intrusion"
  url_or_quote: "updates[2026-08-21T06:45:00Z].summary: \"...this pipeline covered on 2026-08-15...\""
  summary: "(low confidence, pre-existing, already surfaced by check_run.py as a reader-text-internals WARN) Workflow-internal phrasing on an append-only prior changelog record; settled history, not introduced or fixable by this run."
```
