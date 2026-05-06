# Recommended improvements

A consolidated list of improvements for the agentic workflow, the editorial
policy, the operator tooling, the site, and the docs. Each item has a
*Why* (what failure mode or pain point it addresses) and a *How* (concrete
shape of the change). They are **independent** — pick any subset.

The ordering inside each section is rough priority (highest first). Nothing
here changes the existing prompts in `prompts/` directly; structural changes
are flagged.

---

## Agentic workflow & editorial policy

### A1 — Treat sustained 403s as a source-health signal, not a demotion trigger

**Why.** In the only run committed so far (`briefs/2026-05-06.md`), six
HIGH-reliability sources returned HTTP 403 to the agent's direct fetch:
`cisa-kev`, `cisa-advisories`, `cisa-news`, `cisa-directives`, `inside-it.ch`,
`csirt-acn-it`, `prodaft`, `ico-uk`, and `talos`. These are not dead — they
are blocking the agent's user-agent / IP class. Under the current source
lifecycle (3 consecutive failures → demotion), all of these would drop one
reliability tier within three runs and silently leave the active rotation.
That would degrade the brief without an obvious failure mode.

**How.**
- In [`docs/verification.md`](verification.md), add a "transient-fetch
  failure" classification: HTTP 403 / 429 / 503 from a previously-working
  source counts as a *fetch outage*, not a *quality outage*, and never
  demotes reliability.
- In `prompts/daily-cti-brief.md` Phase 5, separate `consecutive_failures`
  into `consecutive_403_403_403_503_429` (transport) and
  `consecutive_empty_or_404` (content). Only the latter demotes.
- For each persistent-403 source, record an alternate URL strategy in
  `notes` (publisher RSS, NVD API for CISA KEV, ANSSI feed export). The
  agent should try the alternate before incrementing the counter.

### A2 — Guard against state-file / brief-content drift

**Why.** Phase 5 (state update) and Phase 6 (commit) are sequential but the
intermediate state isn't sanity-checked. If `cves_seen.json` ends up
malformed JSON, or if a CVE in the brief is missing from
`covered_items.json`, the next run's preflight load will fail or
mis-deduplicate. The brief is on `main` with broken state — the agent's
*next* run is what surfaces the problem.

**How.** Add a Phase 5.5 "self-check" gate in
[`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md):

1. `python -c "import json; json.load(open('state/covered_items.json'))"` — must succeed.
2. Extract all `CVE-\d{4}-\d{4,7}` from `briefs/YYYY-MM-DD.md`.
3. Each must appear in `state/cves_seen.json`.
4. Every item written to the brief's main sections (1–4) must have a
   matching `appearance` in `state/covered_items.json` for today.

If any check fails, abort the commit and emit a `state: drift` line in the
operator output. Re-running the routine after a drift error rebuilds the
state delta from the brief — the brief is the canonical artefact, not the
state.

### A3 — Bound the size of `state/covered_items.json`

**Why.** The file currently has 20 items; it gains roughly 5–15 per daily
run. After a year, this file is in the multi-megabyte range and becomes
slower for the agent to load *and* parse in Phase 0 — which is on the
critical path for every run.

**How.** Add a quarterly archival job (a tiny standalone routine, or a step
in the weekly summary):

```
state/covered_items.json                   # last 180 days, hot path
state/archive/covered_items_2026Q1.json    # frozen, read-only
state/archive/covered_items_2026Q2.json
```

The agent's Phase 0 only reads the hot file. The site's `build.py` reads
both and merges for the topics view. Archival is reversible — moving an
older item back to hot if it becomes relevant again is a single-file edit.

### A4 — Continuous CVE-validity check against NVD

**Why.** The verification policy mandates "every CVE cited resolves on
NVD/MITRE". The check happens in-context during the run. A CVE that *was*
real but later got rejected (rare but happens) would sit in
`cves_seen.json` undetected.

**How.** Add a small standalone routine: walk `state/cves_seen.json`, query
`https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={id}` for each, and
flag any that returns 404 or `vulnStatus: REJECTED`. Append flags as a
`status: REJECTED — flagged YYYY-MM-DD` notes line; do *not* delete (audit
trail). The site can surface a "rejected CVEs" badge on the CVE list. NVD
rate-limits to 5 req / 30 s without a key, 50 req / 30 s with one — a key
in repo secrets makes the whole list scannable in under a minute.

### A5 — Record per-run sub-agent allocation

**Why.** The four research sub-agents take a partitioned slice of
`sources.json`. The partition is in the prompt; the actual allocation each
run is opaque after the fact. Today, finding "which sub-agent missed
Cisco Talos" requires re-reading the brief's verification notes — and only
if the agent surfaced the gap.

**How.** New file `state/run_log.json`, a rolling list (cap at 90 days) of:

```jsonc
{
  "date": "YYYY-MM-DD",
  "model": "claude-sonnet-4-6",
  "sub_agents": {
    "S1": { "sources_attempted": [...], "sources_used": [...], "items_returned": N },
    "S2": { ... }, "S3": { ... }, "S4": { ... }
  },
  "fetch_failures": [ { "id": "talos", "code": 403 }, ... ],
  "duration_seconds": 412
}
```

The site adds an "Operations" page that surfaces fetch-failure trends and
sources that haven't contributed in N days. This is *the* thing that
catches silent rotation bias.

### A6 — Enforce dedup against the weekly summary explicitly

**Why.** The daily prompt's Phase 0 reads "the last 7 calendar days under
`briefs/`" — a directory glob that, depending on implementation,
may or may not include `briefs/weekly/`. If a topic is rolled up in
the weekly summary on Sunday, the next daily can re-report it on Monday.

**How.** In [`prompts/daily-cti-brief.md`](../prompts/daily-cti-brief.md)
Phase 0, name `briefs/weekly/YYYY-Www.md` for the current and prior ISO
week explicitly. The current language already implies this; making it
explicit removes the ambiguity.

### A7 — Editorial-invariant tests in CI

**Why.** Prompt changes can silently regress editorial discipline.
"No IOCs", "every claim has a link", "no vanity metrics" are all
auditable from the Markdown alone. Catching a regression at PR review is
far cheaper than catching it after a routine has published.

**How.** Add `.github/workflows/check-brief.yml` and `tests/check_brief.py`:

```python
# pseudocode
def test_no_md5_sha_hashes(text):     # 32/40/64-hex
    assert not re.search(r'\b[0-9a-f]{32,64}\b', text, re.I)
def test_no_ipv4_in_running_text(text):
    # Allow "x.x.x.x" placeholders, ban dotted-quad in running text
    ...
def test_every_claim_has_inline_link(brief):
    # Heuristic: every paragraph that contains a year-shaped date or
    # "according to" must contain a markdown link.
    ...
def test_cve_format(text):
    for m in re.finditer(r'\bCVE-\S+', text):
        assert re.fullmatch(r'CVE-\d{4}-\d{4,7}', m.group(0)), m.group(0)
```

Run on every push that touches `briefs/`. A failure blocks merge from a
human PR but does *not* block the agent's auto-merge — instead it opens
an issue tagged `editorial-regression`. The agent's commit lands; humans
follow up.

### A8 — Deep-dive rotation memory

**Why.** Phase 3 picks at most one deep dive per day, prioritising active
exploitation + CH/EU nexus. Without any memory of recent deep-dive picks,
the agent can pick the same *category* of vulnerability (e.g. Linux LPE)
five days running, leaving network-stack RCE, identity infrastructure,
and OT undercovered.

**How.** Add `state/deep_dive_history.json`: `[{date, topic, category}]`,
last 30 days. Phase 3 selection rule: "*if the prior week's deep-dive
categories include this candidate's category, demote unless active
exploitation makes it irreducibly urgent.*"

### A9 — Distinguish "no in-the-window news" from "fetch failure"

**Why.** The brief's § 7 currently lists both "sources with no qualifying
items" and "source failures" — but for state-update purposes, both
increment `consecutive_failures`. They are different signals. A 403 means
the agent didn't see anything; a successful fetch returning no in-window
items means the agent saw the page but nothing matched.

**How.** Distinct counters: `consecutive_fetch_failures` and
`consecutive_quiet_periods`. Demotion only fires on the first.

---

## Site & reader (this PR)

### S1 — RSS / Atom feed

**Why.** Some operators want to subscribe via a feed reader. Trivial
addition; broadens the audience.

**How.** Generate `_site/feed.xml` from `manifest.json` in `build.py`.
Each entry: brief title, date, TL;DR bullets as the body. Link in the
top-bar with a small RSS icon.

### S2 — Print stylesheet

**Why.** Defenders sometimes print briefs for handover. Currently the
sticky topbar and aside TOC clutter the print.

**How.** `@media print` block in `assets/css/styles.css`: hide topbar,
aside, footer; force black-on-white.

### S3 — Code-block syntax highlighting

**Why.** Briefs deep-dives sometimes include shell or YAML snippets.
Plain text in monospace is fine for now; a real highlighter is a small
quality bump.

**How.** Vendor `highlight.js` core + only the languages used (bash, yaml,
python, json, c). Wire in the marked `code` renderer. Adds ~30KB.

### S4 — Light-theme toggle

**Why.** The dark theme is system-preference-driven. Some operators want
to force light/dark per device.

**How.** A small button next to the search box that sets a
`data-theme="light|dark|system"` on `<html>` and persists in
`localStorage`. CSS targets `[data-theme="light"]` etc.

### S5 — Section-level deep-link in search

**Why.** A search for "ATT&CK" should land *at the ATT&CK heading inside
the brief*, not at the top of the brief.

**How.** Extend `build.py` to also index H3 sections of each brief, with a
`deep` route like `#/briefs/<name>#<heading-anchor>`. Surface separate
"section" results in the search page.

### S6 — Share / canonical-URL helper

**Why.** Briefs get forwarded on Slack / email. A single-click "copy
permalink" button on each brief reduces friction.

**How.** Tiny button in the brief header, copies `location.href` to
clipboard with a 1-second confirmation toast.

### S7 — Source URL match by URL prefix instead of hostname

**Why.** Today, `sources.json` is matched to brief citations by hostname.
That fails when a single hostname serves multiple unrelated publishers
(rare in this list but possible — e.g. multi-product `microsoft.com`).

**How.** Build longest-prefix URL match: a brief link to
`microsoft.com/security/blog/...` matches a source with
`url: https://www.microsoft.com/security/blog/` more specifically than a
generic `microsoft.com` source. Update `build.py#annotate_sources`.

### S8 — Operations dashboard

**Why.** Pairs with [A5](#a5--record-per-run-sub-agent-allocation). Once
`state/run_log.json` exists, surface it.

**How.** New route `#/ops` showing recent runs, fetch-failure trends, and
sources by last-contributed-day. Useful for the operator review pattern in
[`docs/verification.md`](verification.md).

### S9 — Surface single-source / contradiction flags as filters

**Why.** SOCs sometimes want to read only the corroborated items, or
specifically pull every `[SINGLE-SOURCE]` item across briefs to evaluate
whether a recurring single-source publisher should be promoted.

**How.** Extract the verification-flag tags during `build.py`'s brief
parse (`[SINGLE-SOURCE]`, `[SINGLE-SOURCE-NATIONAL-CERT]`,
`[SINGLE-SOURCE-OTHER]`). Add a chip filter on the Topics page and a
"verification" view.

---

## Documentation

### D1 — A "first run" walkthrough

**Why.** [`docs/routine-setup.md`](routine-setup.md) covers steps; a
narrative walkthrough with screenshots of the routine UI would be faster
to follow for a first-time operator.

**How.** Add `docs/first-run.md` and link from the README.

### D2 — Surface `prompts/CHANGELOG.md` from the site

**Why.** The CHANGELOG is the audit trail of editorial-policy changes.
It's currently buried.

**How.** Render it on the About page below the verification policy.

### D3 — Per-brief "what changed" annotation

**Why.** When the prompt's editorial rules change, briefs from different
versions read slightly differently. A small line in each brief header
showing "prompt v2.14" makes the policy version explicit.

**How.** Read `prompts/CHANGELOG.md`'s most recent version at brief-write
time; bake it into the brief metadata block. The site renders the version
as a clickable badge linking to the changelog entry.

---

---

## Security & autonomy hardening (added after the 2026-05-06 review)

These are referenced in [`docs/security-review.md`](security-review.md) by the threat IDs T1–T9. Listed here in priority order for implementation.

### SR1 — Editorial-invariant CI workflow (T1, T2)

**Why.** The single highest-leverage control. Catches IOCs, hallucinated CVEs, suspicious patterns, and multi-day [SINGLE-SOURCE] floods before a regression is established.

**How.** New workflow `.github/workflows/editorial-invariants.yml` runs on every push to `main` that touches `briefs/`. Runs `tests/check_brief.py` (also new). Failures *do not* revert the commit (the brief is already public) — they:
1. Open a new issue tagged `editorial-regression`.
2. Touch `state/BLOCKED.md` with the failure summary, which the prompt's Phase 0 step 0 now checks for.

The agent's next run aborts cleanly. A human reviews, fixes if needed, deletes `state/BLOCKED.md`. The autonomy model is preserved on the happy path; bounded on the unhappy path.

### SR2 — Prompt-drift alerting (T2)

**Why.** Even with the kill-switch, the operator wants visibility into what the agent is changing in `prompts/*.md`.

**How.** New workflow `.github/workflows/prompt-drift-alert.yml` triggers on push to `main` touching `prompts/`. Posts a comment on a pinned issue (or sends to a webhook secret) with the diff. Human-readable, no decisions taken.

### SR3 — State-file size budget (T3)

**Why.** Slow poisoning is the failure mode that's least visible. A budget catches sudden growth.

**How.** A check in the editorial-invariants workflow: `state/cves_seen.json` and `state/covered_items.json` cannot grow more than 25% in a single commit. `sources/sources.json` cannot add more than 1 candidate per commit.

### SR4 — Sub-agent toolset documentation + verification (T4)

**Why.** The sub-agent capability surface is the single most dangerous configuration. It must be explicit and auditable.

**How.** Add a *"Sub-agent capability ceiling"* subsection to [`docs/routine-setup.md`](routine-setup.md) listing exact allowed tools (`Read`, `Grep`, `Glob`, `WebFetch`, `WebSearch`) and forbidden ones (`Write`, `Edit`, `Bash`, `Task`, `NotebookEdit`). A monthly operator-checklist runbook entry verifies the live routine config matches.

### SR5 — Trusted Types CSP directive (T5)

**Why.** The strongest available defence against DOM XSS, even with DOMPurify. Catches sink-level violations.

**How.** Extend the meta-CSP in [`site/index.html`](../site/index.html) with `require-trusted-types-for 'script'; trusted-types default;`. Wrap the marked → DOMPurify pipeline in a Trusted Types policy. Refactor inline event handlers to addEventListener (already mostly there).

### SR6 — Auto-merge gated on quality CI (T6)

**Why.** The auto-merge currently fast-forwards anything pushed to `claude/*`. Gating on the editorial-invariant CI binds even a credential-compromise scenario to passing the editorial check.

**How.** Edit [`.github/workflows/auto-merge-claude.yml`](../.github/workflows/auto-merge-claude.yml) to wait for the `editorial-invariants` workflow conclusion via `gh run watch` before fast-forwarding. If the gate fails, comment on the open issue and exit cleanly. The branch stays unmerged until a human resolves it.

### SR7 — Engagement outlier suppression (T7)

**Why.** Bot-driven view spikes shouldn't influence editorial weight.

**How.** In [`.github/workflows/sync-engagement.yml`](../.github/workflows/sync-engagement.yml)'s Python step: when computing `by_brief`, drop any brief whose `views_14d` exceeds `10 × median(views_14d)`. Surface dropped entries as `outliers_suppressed` in the JSON for transparency.

### SR8 — Out-of-band hash provenance for vendored libs (T8)

**Why.** A coordinated attacker who flips both the binary and `HASHES` defeats the build's integrity check. An external provenance log makes this single-commit attack impossible.

**How.** Sign the `site/assets/vendor/HASHES` file with a key the agent doesn't have access to (operator-held), and verify the signature in CI. Or publish hashes via sigstore Rekor and verify in CI. Both require some external infra; documented as future work for when the project takes on more sensitive output.

### SR9 — Routine credential rotation policy (T9)

**Why.** Tokens that don't rotate eventually leak.

**How.** Add a "Rotation cadence" section to [`docs/routine-setup.md`](routine-setup.md): rotate the GitHub App install every 90 days; regenerate API trigger tokens whenever they appear in any logs / docs / discussion. Calendar reminder.

### SR10 — Source-add limit per run (T1, T3)

**Why.** A flood of new candidate sources in one brief is anomalous; today nothing enforces a cap.

**How.** Editorial-invariants test rejects a commit that adds more than 1 new source with `status: candidate` to `sources/sources.json`.

---

## Quick-fix shortlist (high value, low effort)

If only an afternoon is available:

1. **SR1** — editorial-invariant CI + `state/BLOCKED.md` writer (90 min). Highest-leverage single change in this whole list.
2. **SR2** — prompt-drift alert workflow (30 min).
3. **A1** — guard high-value 403'd sources from auto-demotion (1 hour).
4. **A2** — Phase 5.5 state-file sanity check (30 min in the prompt).
5. **A6** — explicit weekly-summary read in Phase 0 (5 min in the prompt).
6. **S2** — print stylesheet (15 min).
7. **SR3** — state-file size budget (30 min, in the same CI as SR1).
8. **D2** — surface CHANGELOG on About (5 min).

Together these turn the system from "self-evolving with no observability"
into "self-evolving with detect-and-correct in place" — the realistic
posture for a no-human-gate autonomous content pipeline.
