**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-10T02:09:16Z · ended_at=2026-08-10T02:19:41Z · duration_seconds=625

## Verification report — 2026-08-10T0110Z-weekly (iteration 1)

Scope: run record only (`runs/2026-08-10/2026-08-10T0110Z-weekly.md`) plus `state/coverage_backlog.md`.
Zero entry files exist for 2026-08-10; `entries/2026-08-10/` is absent, consistent with the
`duplicate-week` stand-down. Everything below was checked against on-disk artefacts, git, the saved
deep-read bodies and live re-fetches performed in this iteration.

### What verified clean

- **Checkpoints vs frontmatter.** `main.started_at` 01:10:28Z = `started`; `W1.started_at`/`W1.ended_at`
  01:15:06Z/01:34:45Z = the W1 block (1179 s exact); `W2.started_at`/`W2.ended_at` 01:15:37Z/01:31:34Z =
  the W2 block (957 s exact). The W2 discrepancy is disclosed, not hidden: `findings.W2.yaml` header
  records `ended_at 2026-08-10T01:31:25Z` / `duration_seconds: 948` and the record's W2 `note` states
  exactly that, naming the return header as authoritative. Correct handling.
- **Stand-down narrative, git-verified.** The primary `2026-08-09T2315Z-weekly` has
  `started: 2026-08-09T23:15:39Z` / `completed: 2026-08-10T00:06:31Z` / `entries_published: 16` on
  `origin/main`, and 16 `entries/2026-08-09/weekly-w32-*.md` files exist. Its commits landed on
  `origin/main` at **01:46:56Z** and **01:48:49Z** (`git log origin/main -- runs/2026-08-09/...`); before
  that the tip was the 2026-08-09T1315Z-audit commit from 2026-08-09T15:17Z. That is hard corroboration
  for the record's central claim: at the 01:10Z preflight nothing carrying `week: 2026-W32` was on
  `main`, and the primary had completed locally ~100 minutes before its push became visible. The
  characterisation of the residual guard gap does not overstate the evidence.
- **Withdrawal claims.** `entities/registry.yaml` has no `unc5537`/Moucka/Judische key; `state/cves_seen.json`
  contains neither CVE-2026-64638 nor CVE-2017-16740. `entities_added: []`, `entries_published: 0`,
  `entries_updated: 0`, `disposition: duplicate-week` all match disk. The 14-entry breakdown sums to 14.
- **Residual-row non-coverage — independently re-run.** Case-insensitive grep for
  `wordpress|xss2shell|64638|wp2shell|wp2root|freebsd|CTL HA|33824|ikeext|moucka|unc5537|snowflake|judische|iSCSI`
  across all 24 `entries/2026-08-09/*` files **and** the primary's run record on `origin/main` returns
  **zero matches**. All five residual rows are genuinely uncovered by the primary. `Zbtlink`/`CPDLC` do
  appear (3 entries), so the FreeBSD row's contrast is accurate.
- **Residual-row facts against the saved primaries.** 0patch: "unauthenticated double free in `ikeext.dll`
  … which runs as Local System inside a `svchost.exe` … on the IKEv2 fragment reassembly path. An
  unauthenticated attacker who can reach UDP 500/4500 on a host that acts as an IKEv2 responder" — the row
  is a faithful transcription. DOJ: "over 165 victim organizations", "billions of sensitive customer
  records", "scheduled to be sentenced on Oct. 27"; **0 hits** for "multi-factor"/"MFA" and **0 hits** for
  "Snowflake" — the row's own caution ("The MFA fact is Krebs's, not DOJ's … DOJ does not name the
  provider") is exactly right. Krebs carries "$2.5 million in ransom payments" and "Wagenius is set to be
  sentenced on September 3, 2026" (the row's co-conspirator date). FreeBSD: "Three pre-auth remote kernel
  exploits behind one TCP port that FreeBSD has decided to document rather than fix", "TCP port (999 by
  default) … with no authentication", zero CVE ids in the body. XSS2Shell: the `wp_strip_all_tags()` /
  `wp_kses_post()` parser disagreement, DOM clobbering, JSONP, Application-Password minting,
  "Single-site WordPress administrators have the unfiltered_html capability by default", "PHP files inside
  are directly web-accessible without activation" — all present. wp2root: Serializable `unserialize()` UAF,
  "Copy Fail", `disable_functions` escape — all present.
- **ATT&CK claim.** `attack/enterprise-attack.json` (v19.2, upstream_modified 2026-08-05) records
  `T1562.001` with `"revoked": true, "revoked_by": "T1685"`, and `T1685` live. `python3 tools/attack_data.py
  --check` returns "up to date: local v19.2 == upstream latest v19.2". Both claims hold.
- **Source health.** `state/source_health.json` latest probe (fetched_at 2026-08-10T02:01:24Z): 179 results,
  `Counter({'ok': 100, 'bridge-ok': 77, 'jina-ok': 1, 'client-error': 1})`, all 179 `action: none`; `pwn-ai`
  probed 200. Exactly as stated.
- **Bridge re-verification.** `tools/fetch_source.py url https://www.sygnia.co/blog/` → 173,175 bytes;
  `… https://www.prodaft.com/resources` → 271,834 bytes. The record's "173 KB and 271 KB" is accurate and
  the "not a broken transport" conclusion stands.
- **New source.** `sources/sources.json` `pwn-ai` matches the record: publisher "PWN.AI (Nigusu Kasahun)",
  `https://pwn.ai/blog/`, `category [research, vulns]`, `reliability B`, `status candidate`. One candidate,
  cap respected.
- **Style.** No IOCs. English throughout. Workflow shorthand ("Phase 0", "verifier", "pre-verifier") is
  present but matches the house style of the 2026-08-03 and 2026-07-27 stand-down records for the
  operator-facing notes body — not raised as a defect. The record does not oversell the run: it leads with
  the stand-down, states plainly that the queue mechanism "has moved the problem rather than solved it",
  and puts the operator items last but unhedged.

### Unsupported / hallucinated facts

**F1 — `sources_changed[3]` misstates which counters moved for `sygnia` and `prodaft`.**
Record: *"sygnia, prodaft, paradigm-shift-research, ibm-xforce, socket-dev-blog: no usable content;
consecutive_fetch_failures incremented"*. Diffing `HEAD:sources/sources.json` against the working tree,
only three records moved that field: `paradigm-shift-research` 0→1, `ibm-xforce` 0→1, `socket-dev-blog` 0→1.
`sygnia` kept `consecutive_fetch_failures: 0` and took `consecutive_quiet_periods` 1→2 with
`last_successful_fetch` 2026-07-31→2026-08-10; `prodaft` kept `consecutive_fetch_failures: 0` and took
`consecutive_quiet_periods` 3→4 with `last_successful_fetch` 2026-08-07→2026-08-10. The disk state is the
*correct* one — it is what the record's own body argues for ("**Two reported fetch failures were not
failures.**"). The telemetry line contradicts it. Same drift in operator item (4): *"`prodaft` has failed
four consecutive runs"* — the counter reading 4 is `consecutive_quiet_periods`, and its
`consecutive_fetch_failures` is 0.

**F2 — the narrative's 02:05Z stand-down time contradicts the record's own completion stamp.**
Record: *"The stand-down was reached at 02:05Z, roughly 55 minutes in"* and *"By the pre-verifier re-check at
02:05Z its record and sixteen strategic entries were on `main`."* Frontmatter: `completed:
"2026-08-10T02:01:25Z"`, `duration_seconds: 3057` (01:10:28Z → 02:01:25Z = 50 m 57 s, i.e. ~51 minutes, not
~55). Checkpoint `work/2026-08-10T0110Z-weekly/main.ended_at` contains `2026-08-10T02:01:25Z`. The record
therefore claims to have completed 3.5 minutes before the decision it narrates. Reconcile: either correct
both 02:05Z mentions and "roughly 55 minutes" to the checkpoint values, or re-stamp
`completed`/`duration_seconds` from a genuine later checkpoint.

**F3 — "fourteen of those rows predate this run" is sixteen.**
`git show HEAD:state/coverage_backlog.md` carries **16** open rows (8 with Surfaced 2026-08-03, 8 with
Surfaced 2026-08-09 by `2026-08-09T1315Z-audit`); the working tree carries 19 after this run added 3. The
stated total (19) and the "eight surfaced by the 2026-08-03 stand-down" clause are both correct; only the
"fourteen" is wrong. Fourteen is the number of pre-existing rows this run left untouched (16 − the 2 it
restored) — if that is the intended meaning it needs saying, since as written it understates the backlog age
problem the operator item exists to raise.

**F4 — the wp2root row's new caution misattributes the CVE-2026-31431 identifier.**
Clause added by this run: *"The \"Copy Fail\" identifier CVE-2026-31431 rests on calif.io's authority only —
verify against a per-CVE record before it enters `cves[]`."* This run's own W1 return says otherwise:
`findings.W1.yaml` item 10 lists `{ url: "https://copy.fail", publisher: "Theori / xint.io (Copy Fail —
CVE-2026-31431 disclosure)", date: "2026-04-29", role: "corroborating" }`, and `url-liveness.tsv` logs
`https://copy.fail  200  2026-08-10T01:31:19Z`. Re-fetched in this iteration via
`tools/fetch_source.py url https://copy.fail`: `<title>Copy Fail — CVE-2026-31431</title>`,
`<meta name="author" content="Xint">`, description *"Copy Fail (CVE-2026-31431): a 732-byte Linux LPE …
Found by Xint Code."* A dedicated discloser page owns the identifier. The caution should point the future
run at copy.fail (and note calif.io's "patched upstream April 2026, present since 2017" framing came with
it), not tell it the id is single-authority.

**F5 — "Sonatype" is not in this run's evidence.**
`fetch_failures[socket-dev-blog].mitigation_applied`: *"The npm supply-chain thread was covered from Elastic,
Unit 42 and Sonatype instead, so no coverage was lost."* Elastic and Unit 42 are both cited in
`findings.W1.yaml` item 1. Case-insensitive grep for "sonatype" across `findings.W1.yaml`,
`findings.W2.yaml`, `url-liveness.tsv` and `week-review.json` returns **0 hits**; `sonatype` appears in
`sources/sources.json` only as a source attempted by the 2026-08-08 intel fire. Drop the name.

### Missed angles

**F6 — the residual list is presented as exhaustive but at least two verified in-window items are neither
published nor queued.** Record: *"Residual coverage — five items the primary did not carry, now queued
rather than narrated."*
(a) `findings.W1.yaml` item 6 — Forescout's exposure scan on the water-PLC campaign this store already
tracks: 4,407 internet-facing Rockwell PLCs on EtherNet/IP, 22 sitting in the cities already hit, 19 of
those 22 on firmware vulnerable to CVE-2017-16740, >70 % of the US-exposed population on mobile-carrier
rather than fixed enterprise links, plus CISA's Black Hat briefing detail ("either no password set or
default password set"). The run deep-read both primaries (`deepread/forescout.txt`, `deepread/nextgov.txt`),
so it is verified work. The primary weekly's `weekly-w32-water-plc-lockout-status.md` carries the FBI/EPA
device naming and the twelve-state scope but has **zero** hits for "Forescout", "4,407" or "16740", and
`prior_coverage.json` has zero hits for all three. This is an inventory-actionable exposure delta on tracked
ground with a European read-across, and it fell through both the publish path and the queue.
(b) `findings.W1.yaml` item 13 — Trail of Bits' four AWS Nitro Enclaves ↔ KMS trust-boundary pitfalls that
survive attestation; zero hits for "Nitro" or "Trail of Bits" in the primary's entries and in
`prior_coverage.json`.
Fix: queue both rows, or add one clause to the record saying they were judged not to clear the gate and why.
As it stands the "five items" framing reads as the complete carry-forward, which is the exact failure mode
(`state/coverage_backlog.md` preamble: "Do not silently drop a row") the file was created to prevent.

### Editorial / less-is-more flags (advisory)

**F7 — `sub_agents.W1.sources_used` omits hosts W1 actually cited.** The listed 12 hosts exclude
`unit42.paloaltonetworks.com`, `www.elastic.co`, `copy.fail`, `www.helpnetsecurity.com`, `health-isac.org`,
`ransom-isac.org` and `mysites.guru`, all of which carry source records in `findings.W1.yaml`. The record
then leans on two of them (Elastic, Unit 42) in the `socket-dev-blog` mitigation. Defensible if
`sources_used` means "yielded published content" (nothing was published), but the asymmetry is worth one
clarifying clause. Advisory — leaveable.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 1, advisory: 1)

All five truth findings are internal contradictions between the record (or the backlog rows it wrote) and
artefacts on disk in the same commit — none require re-research, and none touch the stand-down narrative's
substance, which git independently corroborates. F6 is the one that costs the reader something: a verified
exposure delta on tracked ground currently has no path to publication.

### Findings summary (machine-readable)

See `work/2026-08-10T0110Z-weekly/verification.iter1.findings.yaml` (identical payload, unfenced).
