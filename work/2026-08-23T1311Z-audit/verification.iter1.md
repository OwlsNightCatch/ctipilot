**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-24T10:15:51Z · ended_at=2026-08-24T10:32:21Z · duration_seconds=990
**Self-telemetry:** urls_checked=8 · webfetch_calls=0 · bridge_fetches=7 · websearch_calls=1

## Verification report — 2026-08-23T1311Z-audit (iteration 1)

Cold read, no prior-iteration deltas block. Scope: the two new entries, the run record, and the audit report.

### What I verified and found sound (so the next iteration need not redo it)

**Entry 1 — `entries/2026-08-24/cve-2026-18963-keycloak-no-red-hat-product-unfixed.md`**

- Both source URLs fetched live this iteration via the bridge. `https://access.redhat.com/hydra/rest/securitydata/cve/CVE-2026-18963.json` returns the JSON with `package_state` holding **exactly two rows, both `"fix_state" : "Not affected"`** (JBoss EAP Expansion Pack / keycloak-services, Red Hat Single Sign-On 7 / keycloak-services) — the entry's central claim, verified against both the live endpoint and the saved copy at `work/2026-08-23T1311Z-audit/redhat-18963-hydra.json`. The entry's inline literal `"fix_state" : "Not affected"` reproduces the endpoint's own spacing exactly.
- `evidence[0]` — `disabling the "Forgot password" functionality across all realms can be used as a temporary mitigation` — is a **contiguous verbatim substring** of the hydra `mitigation.value` field. The console path in the body (Realm settings, Login, Forgot password, Off, applied to every realm) matches the same field verbatim.
- `affected_release` has 11 rows, every one carrying an RHSA, all `release_date` 2026-08-18 — supporting "every other product Red Hat lists carries a shipped erratum" and the 2026-08-18 errata date. The four RHSA ids (56519/56520/56523/56524) and their 26.4 / 26.6 stream assignments are correct against the endpoint.
- CVSS 9.1, `AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`, threat_severity Critical, root cause "improper state validation within the reset-credentials authentication flow" — all present in the hydra `cvss3` / `threat_severity` / `statement` fields; `auth: pre-auth` and `vector: zero-click` follow from `PR:N/UI:N`.
- The entry's characterisation of the superseded entry is accurate on all three counts: `entries/2026-08-19/cve-2026-18963-keycloak-reset-credentials-account-takeover.md` carries the claim in its summary, in a dedicated body paragraph ("Second, and absent from the headline advisory view, one affected product has no fix at all"), and in action item 2 (the reverse-proxy suggestion the update correctly says it supersedes).
- `update_of` target exists and is the same story; `affected_products[]` correctly drops the Expansion Pack; `techniques: [T1190, T1098]` both resolve **active** (not deprecated, not revoked) in the pinned `attack/enterprise-attack.json` v19.2, and T1098 is supported by the hydra `details` text ("directly setting new credentials"). `org_triage: null` and `watchlist_hit: false` are correct for this deployment. `classification: {A, 2}` is defensible: Red Hat is the vendor PSIRT and CNA for its own build (A), and both cited channels are the same assessor, so credibility stays 2 — which the `sourcing_note` states explicitly. `verification: single-source` + `sourcing_note` naming the vendor-PSIRT carve-out satisfies the single-source discipline (no F12). Two actions, both concrete, both derived from this finding's own mechanics, neither duplicated in the window (no F18).

**Entry 2 — `entries/2026-08-24/cve-2026-19478-gitlab-exploitation-confirmed-ncsc-ch.md`**

- Primary fetched live (`extract`): SecurityWeek, "Critical GitLab Flaw Exploited Shortly After Disclosure", author Ionut Arghire, **datePublished `2026-08-20T07:48:24+00:00`** — matches `sources[0].date` exactly (no F3(e) drift). Both `evidence[]` quotes are contiguous verbatim substrings of the fetched page body, including the curly apostrophes and quote marks (`haven’t`, `‘@gl_introduced’`) — I substring-matched them mechanically against the tag-stripped body of `work/2026-08-23T1311Z-audit/securityweek-gitlab.html`.
- The "~2 days" claim is the article's own: "Threat actors started exploiting a critical-severity GitLab vulnerability **roughly two days after public disclosure**". Patch date 2026-08-17, CVSS 9.4, fixed versions 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11, "no public exploit code is available", the honeypot observation and the `/api/graphql` endpoint are all in that page.
- Corroborating source fetched via `python3 tools/fetch_source.py ncsc-csh post 12856` (never WebFetch on that host): the post's `history[]` carries `{"reason": "Updated with claims of active exploitation", "timestamp": "2026-08-21T14:21:57Z", "type": "Edited"}`, its body's Update block reads `**Update 21.08.2026** - **Current exploitation status**: Actively exploited` and cites the SecurityWeek URL. The **2026-08-21 amendment date, the unknown→actively-exploited change, and the "citing that coverage" claim are all exactly right.** NCSC-CH also names "GitLab Community Edition (CE)" / "GitLab Enterprise Edition (EE)" verbatim, matching `affected_products[]`, and states GitLab.com and Dedicated were already patched.
- **Not on KEV, confirmed:** fetched the catalogue via `tools/fetch_source.py cisa-kev` (catalogVersion 2026.08.21, 1674 entries) — neither CVE-2026-19478 nor CVE-2026-18963 appears. The `sourcing_note`'s KEV statement holds.
- `techniques: [T1190, T1485]` both active in the v19.2 pin (Exploit Public-Facing Application, Data Destruction) and both supported by the described behaviour (unauthenticated GraphQL request; deletion of public projects and user data). `classification: {B, 2}` is consistent — `sources/sources.json` rates `securityweek` reliability **B**, and the credibility-2 reasoning (national-authority assessment adoption, not an independent second observation) is stated in the `sourcing_note`. `verification: multi-source` matches two independent publishers. One action, concrete and hunt-ready, not duplicated by the in-window W34 rollup (which carries no `actions[]`). No F18.
- I checked whether a watchTowr Labs post should have been the primary (F6): `labs.watchtowr.com` carries no post on this CVE, the SecurityWeek HTML contains **no** outbound watchtowr URL, and a web search surfaces only news outlets relaying watchTowr statements. SecurityWeek is the disclosing publication of the honeypot claim — primary role is correct, no F6.
- **Dedup / update discipline:** both `update_of` targets exist in `entries/2026-08-19/`. `entries/2026-08-23/weekly-w34-vuln-status-rollup.md` (published ~10 h earlier, in-window) mentions both developments, but it is `horizon: strategic` and does not move the operational `cves[].status` machine surface; each new entry also carries a delta the weekly lacks (the Red Hat per-realm interim mitigation; the `@gl_introduced` hunt artifact and the triage discriminator). The inclusions are correct, not duplicates — no F7.

**Run record — telemetry cross-checked against the on-disk checkpoints.** Every sub-agent timestamp in the record matches `work/2026-08-23T1311Z-audit/*.started_at` / `*.ended_at` to the second, and every `duration_seconds` is the exact difference: B1 13:13:29→13:45:14 = 1905; B2 13:13:41→13:35:23 = 1302; B3 13:13:51→13:36:25 = 1354; B5 13:14:16→13:40:22 = 1566; B6 13:14:36→13:28:50 = 854; B7 13:14:48→13:37:29 = 1361; G1 13:15:04→13:34:54 = 1190; G2 13:15:22→13:24:39 = 557; G3 13:15:41→13:37:50 = 1329. `main.started_at` = 13:11:00 = `started`. B4 has no checkpoint file (its timestamps came from the return header, and the record does not claim otherwise); its 13:14:02→13:22:24 = 502 is internally consistent. `window_hours: 335.9` = 2026-08-09T13:15:57Z→2026-08-23T13:11:00Z exactly, and that anchor is the `started` field of `runs/2026-08-09/2026-08-09T1315Z-audit.md`.

**Audit-report arithmetic and shipped-fix claims — independently recomputed.**

- Verdict counts: parsed all seven batch YAMLs. clean 16+18+14+20+12+18+14 = **112**; factual 2+2+3+0+2+1+0 = **10**; imprecision 2+0+3+0+6+1+1 = **13**; total **135**. Per-batch line "B1 16/20 · B2 18/20 · B3 14/20 · B4 20/20 · B5 12/20 · B6 18/20 · B7 14/15" is exact, as is every `verdicts:` map in the run record. The batches name **135 unique entry paths with zero duplicates and zero nonexistent paths** — "covered every window entry exactly once" holds.
- Window census recomputed with `site/content_model.py`: 135 entries, **39 `update_of`**, **classification present 135/135**, 104 operational entries, **83 actions on operational entries = 0.798/entry**, **42.3 % actionless**, **max 3 actions on any entry**, **86 actions across all 135 entries** (the "all 86 actions" hand-review figure), **`high` share 50.0 %**, **zero criticals**, 98 behaviour-kind entries with **mean 4.08 techniques and zero empty**. 16 run records in window, **16/16 `publish_status: ok`**, **73 verifier iterations**, mean **4.56** ("4.6"), **3 confirmed double-CLEAN fires — 2026-08-09T1315Z-audit, 2026-08-17T0413Z-intel, 2026-08-18T0410Z-intel**, exactly the three named, and **no same-model consecutive pair anywhere** ("rotation held 73/73").
- Run-clock finding: `completed-inversions.json` holds **98** records. `2026-08-19T0410Z-intel` records `duration_seconds: 3963` with a last sub-timestamp of `2026-08-19T07:18:13Z` — 04:10:24→07:18:13 is **11 269 s**, matching the report to the second; `2026-08-20T0409Z-intel` 3169 recorded vs 04:09:34→07:01:59 = **10 345 s**, also exact.
- Shipped fixes present in the tree: v3.32 banners in all three master prompts; the CHANGELOG 3.32 entry with Why/What changed/What stays twice over; `tools/check_run.py` carries both new checks (`check_run_clock`, `_ack_ledger`, the `--all` dead-row report); `.claude/hooks/setup-deps.sh` exists, is executable, and is wired into `SessionStart` in `.claude/settings.json` alongside `defaultMode: bypassPermissions` and the broadened memory allow-rules; `sources/sources.json` carries `tenable-research` `rss_url https://feeds.feedburner.com/tenable/qaXL` with `fetch_method: rss`, `0patch-blog` `rss_url https://blog.0patch.com/feeds/posts/default`, and the new `symantec-broadcom` **candidate** (the only added id — the one-new-candidate-per-run rule holds); `state/coverage_backlog.md` shows **13 added rows (9 coverage + 4 corrections) and the Keycloak row struck**, matching both the report and the run record's "nine coverage items"; `work/.../trafilatura-rollout.md` states the 18/20 verdict; `url-liveness.tsv` has **463** lines; the ATT&CK pin reports `v19.2 == upstream latest v19.2`; `python3 site/build.py` completes with **no self-check warnings**; and the `csaf-msrc-transcription.md` membership-vs-verdict memory rule plus the three operator directives are in `.claude/memory/`.
- Style: no IOCs, no vanity metrics, English throughout, no rule code, and no workflow-internal language in either entry. (The run-record notes use "sub-agent"/"main agent" — settled convention across the store's run records, including 8 of the last 20; not flagged.)

Everything below is what did **not** hold.

### Citation does not support the claim

**F1 — `2026-08-24/cve-2026-18963-keycloak-no-red-hat-product-unfixed`: the `defaultStatus` corroboration is cited to a page that has no such field.**

Body, paragraph 1, final corroborating sentence:

> The published CVE record carries the same two products with `defaultStatus` `unaffected` ([Red Hat Product Security, 2026-08-18](https://access.redhat.com/security/cve/CVE-2026-18963)).

and `sourcing_note`:

> independently confirmed against the published CVE record, whose affected[] block carries the same two products with defaultStatus "unaffected".

I fetched the cited URL this iteration with `python3 tools/fetch_source.py url` (raw HTML, 217 158 bytes) and searched it case-insensitively. The page carries the product-state data as embedded Next.js payload in a **different vocabulary**: `"product":"Red Hat JBoss Enterprise Application Platform Expansion Pack", ... "state":"Not affected", ... "delegated_not_affected_justification":"Component not Present"` and `"product":"Red Hat Single Sign-On 7", ... "state":"Not affected", ... "Vulnerable Code not Present"`. The token `defaultStatus` **does not occur anywhere on that page**, and there is no `affected[]` block on it (the page's own flag reads `"isUnaffectedCveRecord":false`).

The fact itself is true, but it lives in a document the entry does not cite: `https://cveawg.mitre.org/api/cve/CVE-2026-18963` (CNA `redhat`, `datePublished 2026-08-18T17:05:07Z`) has 13 `affected[]` records, and the JBoss EAP Expansion Pack and Red Hat Single Sign-On 7 rows each carry `"defaultStatus": "unaffected"` — I fetched and enumerated all 13. This is the pipeline's dominant residual class: a true fact attached to a co-cited page that does not state it.

Two clean fixes, neither needing new research: (a) re-word to the cited page's own vocabulary — "the CVE page records both products as `Not affected`, justified `Component not Present` and `Vulnerable Code not Present`" — or (b) keep the `defaultStatus` framing and attribute it to the cve.org CVE Record rather than to the Red Hat page. Apply the same fix to the `sourcing_note` sentence.

### Unsupported / hallucinated facts

**F2 — "two corrections published this fire" overstates the repair record; only one of the ten factual errors was repaired by a published entry.**

Run record § Verification & coverage notes:

> **112/135 clean · 13 imprecisions · 10 factual errors**; two corrections published this fire as update entries, four queued on the coverage backlog with full ground truth, four documented without a repair (reasons in the report).

Audit report, § Findings — false or erroneous published intelligence:

> ### Factual errors (10) — each root-caused; fixes are `update_of` entries (2 published this run, 4 queued with full ground truth)

The report's own factual-errors table has exactly **one** row whose Fix column reads "**Published**" — the Keycloak row. The second published entry corrects no factual error: `work/2026-08-23T1311Z-audit/truth-B6.yaml` records the GitLab original as clean —

```
- entry: entries/2026-08-19/cve-2026-19478-gitlab-graphql-unauth-data-destruction.md
  verdict: clean
  defect: null
```

— and the report files it under "### Recovered and published by this audit (1)", i.e. a completeness recovery, not a correction. I re-derived the full census from the batch YAMLs: the ten factual-error entries are B1 (weekly-w32-cve-record-unreliable, weekly-w32-passkeys), B2 (coding-agent-ci-harness, wp2root), B3 (lazarus-operation-dream-job, sap-august-2026, clop-leak-site), B5 (weekly-w33-looking-ahead, weekly-w33-vuln-status-rollup), B6 (cve-2026-18963-keycloak). Their disposition is **1 published + 5 queued (as 4 backlog rows) + 4 documented**. The 2+4+4 arithmetic reaches 10 only by counting the GitLab coverage recovery as a correction.

Fix both surfaces so the split matches the table — e.g. "one correction published this fire, five queued across four backlog rows, four documented without a repair; separately, one missed coverage item recovered and published."

**F3 — "`state/cves_seen.json` re-synced for both" is false for CVE-2026-19478, and the stale record is the exact defect the entry was published to fix.**

Audit report, § Fixes shipped in this commit:

> the GitLab exploitation-status recovery (`2026-08-24/cve-2026-19478-gitlab-exploitation-confirmed-ncsc-ch`). `state/cves_seen.json` re-synced for both.

`git diff state/cves_seen.json` touches exactly one record — CVE-2026-18963 (`last_seen` 2026-08-19→2026-08-24 plus an appended product-state correction sentence). The CVE-2026-19478 record is untouched and still reads:

```
"first_seen": "2026-08-19", "id": "CVE-2026-19478", "last_seen": "2026-08-19",
"title": "GitLab CE/EE — code injection via a GraphQL directive ... no exploitation reported and GitLab withholds the mechanism for 90 days."
```

This is not a wording problem. The report's own root-cause narrative for publishing that entry is that "the `/cve/` page and any automated triage consumer had a stale exploitation answer" — and the store-wide CVE index still carries "no exploitation reported" for a CVE the same commit publishes as actively exploited. Fix by re-syncing the record (`last_seen` → 2026-08-24 and an exploitation-status sentence in the title, mirroring what was done for 18963), not by editing the sentence.

**F4 — the sources.json change count matches nothing on disk.**

Audit report, § Fixes shipped in this commit:

> **`sources/sources.json`** — 7 changes, all in `sources_changed[]`

The run record's `sources_changed[]` carries **8** bullets. A record-level diff against `HEAD` shows **11 modified** source records (`0patch-blog`, `cert-at`, `cert-eu`, `claroty-team82`, `dragos`, `enisa`, `ncsc-uk`, `nozomi-networks`, `sans-ics`, `tenable-research`, `withsecure-labs`) plus **1 added** (`symantec-broadcom`) = **12 source records touched**, zero removed. The report's own semicolon list enumerates 5 groups covering those same 12 sources. No counting basis yields 7. State "8 entries in `sources_changed[]` covering 12 source records", or drop the number.

**F5 — "Warning sweep: zero" is contradicted by `check_run.py --all` on the current tree.**

Audit report, § Fixes shipped in this commit:

> **Warning sweep: zero.** `check_run.py --all` ends 0 warn · 0 fail (14 acknowledged, all still live — none added, none pruned); `site/build.py` self-check clean.

I ran `python3 tools/check_run.py --all` this iteration. `site/build.py` is indeed clean and the 14 acknowledged rows are all still live (I counted 14 in the ACKNOWLEDGED block, matching the Phase 0 capture in `check-all.txt`, whose WARNINGS block is genuinely empty — so the finding-6 claim about Phase 0 is correct). But the current tree ends with **one WARNING, and it is this run's own**:

> WARN run-record: 2026-08-23T1311Z-audit: duration_seconds=75841 (~21.1 h) exceeded the runaway threshold — see the per-run watchdog note

The warning is not removable: the 21 h is the disclosed overnight container suspension, the Phase 6 re-stamp will make it larger, and the zero-warning discipline forbids a run acknowledging its own fresh warning. So the fix is to report the residual honestly — Phase 0 was 0 warn · 0 fail · 14 acknowledged; the commit ends with 1 warning, this run's own disclosed wall clock — rather than to assert a zero the artifact refutes. (The FAILs `--all` also reports for this record are the expected pre-loop state: `verification.iterations` is still empty.)

### Editorial / less-is-more flags (advisory)

**F6 — advisory, forward-looking: re-stamp `completed` before commit or the run ships the inversion it root-caused.** The record carries `completed: "2026-08-24T10:15:01Z"` / `duration_seconds: 75841`; this verification iteration started at `2026-08-24T10:15:51Z`. The gate passes today only because `verification.iterations` is empty. Once the iterations are stamped, the v3.32 `run-clock` check this very run shipped will FAIL the record unless Phase 6 step 0 re-stamps `completed` and `duration_seconds` after the loop closes. The report's "This run itself complies" becomes true only after that re-stamp.

**F7 — advisory: the placeholder row in the factual-errors table.** The last row — `| 2026-08-16/weekly-w33-vuln-status-rollup (second defect, counted once above) | — | — | — |` — renders as a near-empty table line and reads as a formatting defect rather than the count reconciliation it is. A one-line footnote under the table carries the same information.

### Missed angles

None. Using the run record's source-coverage telemetry (`fetch_failures: []`, `bridge_uses: []`, all ten sub-agents returned inside their caps, no batch abandoned) and the dedup context, I found no genuinely-relevant in-window item the run surfaced and then silently dropped. The nine deferred coverage items each carry a discovery trace and a stated deferral reason on `state/coverage_backlog.md` — including the one whose deferral most needed justifying, SPIP CVE-2026-77647 ("Deferred only because this audit hit its wall-clock guard; it should be the next fire's first item"), an actively-exploited pre-auth RCE with a French public-administration nexus. Coverage looks complete for an audit fire.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 0, advisory: 2)

Nothing here touches the two entries' central findings — the Keycloak product-state correction and the GitLab exploitation-status change are both true, both verified against live primaries this iteration, and both correctly scoped as `update_of` deltas. F1 is a one-clause attribution repair inside an otherwise exact entry. F2–F5 are four self-report claims in the run record and audit report that the artifacts they name do not bear out; F3 is the one with operational weight, because the stale `cves_seen` record leaves the machine surface carrying precisely the answer this fire published an entry to fix.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F1
  category: claim-not-supported
  section: entries
  item: "2026-08-24/cve-2026-18963-keycloak-no-red-hat-product-unfixed"
  url_or_quote: "The published CVE record carries the same two products with `defaultStatus` `unaffected` ([Red Hat Product Security, 2026-08-18](https://access.redhat.com/security/cve/CVE-2026-18963))"
  summary: >-
    Fetched https://access.redhat.com/security/cve/CVE-2026-18963 (bridge `url`, raw HTML, 217 KB): the page's
    embedded product-state JSON expresses the two rows as "state":"Not affected" with
    "delegated_not_affected_justification":"Component not Present" (JBoss EAP XP) and "Vulnerable Code not
    Present" (RHSSO 7). The string `defaultStatus` does not occur on that page at all, and it carries no
    `affected[]` block. The FACT is true but belongs to a different document: cveawg.mitre.org/api/cve/
    CVE-2026-18963 (CNA redhat, datePublished 2026-08-18T17:05Z) has 13 affected[] records, of which the JBoss
    EAP Expansion Pack and Red Hat Single Sign-On 7 rows carry defaultStatus "unaffected". Same defect in
    `sourcing_note` ("independently confirmed against the published CVE record, whose affected[] block carries
    the same two products with defaultStatus \"unaffected\""). Fix either by re-wording to the cited page's own
    vocabulary (state "Not affected", justification "Component not Present" / "Vulnerable Code not Present") or
    by naming the cve.org CVE Record as the document that carries defaultStatus. No new research needed.
- code: F2
  category: hallucinated-fact
  section: run-record + audit-report
  item: "runs/2026-08-23/2026-08-23T1311Z-audit.md · docs/audits/2026-08-23-weekly-quality-audit.md"
  url_or_quote: "two corrections published this fire as update entries, four queued on the coverage backlog with full ground truth, four documented without a repair / '### Factual errors (10) ... (2 published this run, 4 queued with full ground truth)'"
  summary: >-
    Only ONE of the ten factual errors was repaired by a published correction. The report's own factual-errors
    table has exactly one row marked "**Published**" (Keycloak). The second published entry (GitLab
    CVE-2026-19478) corrects no factual error: work/2026-08-23T1311Z-audit/truth-B6.yaml line 82-86 records
    `- entry: entries/2026-08-19/cve-2026-19478-gitlab-graphql-unauth-data-destruction.md / verdict: clean /
    defect: null`, and the report itself files it under "### Recovered and published by this audit (1)" as a
    completeness recovery. Verified the full factual-error census across the batch YAMLs: B1 2 (Traefik,
    Black Hat), B2 2 (coding-agent, wp2root), B3 3 (Lazarus, SAP, Cl0p), B5 2 (w33 rollup, w33 looking-ahead),
    B6 1 (Keycloak) = 10. Disposition is 1 published + 5 queued (as 4 backlog rows) + 4 documented. Correct both
    the report heading and the run-record sentence so the published/queued split matches the table.
- code: F3
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-08-23-weekly-quality-audit.md § Fixes shipped in this commit"
  url_or_quote: "`state/cves_seen.json` re-synced for both."
  summary: >-
    Only CVE-2026-18963 was re-synced. `git diff state/cves_seen.json` touches exactly one record (last_seen
    2026-08-19 -> 2026-08-24 plus an appended product-state correction sentence). The CVE-2026-19478 record is
    untouched: last_seen still "2026-08-19" and title still ends "...no exploitation reported and GitLab
    withholds the mechanism for 90 days." That is the exact stale exploitation answer the newly published entry
    exists to correct, still sitting in the store-wide CVE index the report calls the machine surface. Fix by
    re-syncing the CVE-2026-19478 record (last_seen + exploitation status in the title), not by softening the
    sentence.
- code: F4
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-08-23-weekly-quality-audit.md § Fixes shipped in this commit"
  url_or_quote: "**`sources/sources.json`** — 7 changes, all in `sources_changed[]`"
  summary: >-
    The count matches nothing on disk. The run record's `sources_changed[]` carries 8 bullets (tenable-research,
    0patch-blog, dragos, nozomi-networks, claroty-team82, sans-ics, the five-CERT bullet, symantec-broadcom), and
    a record-level diff of sources/sources.json against HEAD shows 11 modified records (0patch-blog, cert-at,
    cert-eu, claroty-team82, dragos, enisa, ncsc-uk, nozomi-networks, sans-ics, tenable-research,
    withsecure-labs) plus 1 added (symantec-broadcom) = 12 source records touched. No reading of the report's
    own semicolon-separated list yields 7 either (it enumerates 5 groups / 8 changes). State 8 entries in
    sources_changed[] covering 12 source records, or drop the number.
- code: F5
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-08-23-weekly-quality-audit.md § Fixes shipped in this commit"
  url_or_quote: "**Warning sweep: zero.** `check_run.py --all` ends 0 warn · 0 fail (14 acknowledged, all still live — none added, none pruned)"
  summary: >-
    Ran `python3 tools/check_run.py --all` against the current working tree this iteration. It ends with 1
    WARNING, and it is this run's own: "run-record: 2026-08-23T1311Z-audit: duration_seconds=75841 (~21.1 h)
    exceeded the runaway threshold — see the per-run watchdog note". The 14 acknowledged rows are correct and
    all still live (verified: 14 rows in the ACKNOWLEDGED block, same as the Phase 0 capture in
    work/2026-08-23T1311Z-audit/check-all.txt, whose WARNINGS block is genuinely empty). The warning is not
    fixable — the 21 h wall clock is the disclosed container suspension and the re-stamp at Phase 6 will make it
    larger — and a run never self-acknowledges its own fresh warning, so the fix is to state the residual
    honestly (Phase 0 was 0 warn · 0 fail · 14 ack; the commit ends 1 warn, this run's own disclosed wall clock)
    rather than to claim a zero that the artifact contradicts.
- code: F6
  category: editorial-advisory
  section: run-record
  item: "runs/2026-08-23/2026-08-23T1311Z-audit.md frontmatter"
  url_or_quote: "completed: \"2026-08-24T10:15:01Z\" / duration_seconds: 75841"
  summary: >-
    Advisory, forward-looking: `completed` currently precedes this verification iteration (started
    2026-08-24T10:15:51Z). The gate passes only because `verification.iterations` is still empty. Once the
    iterations are stamped, the v3.32 `run-clock` check this very run shipped will FAIL the record unless
    Phase 6 step 0 re-stamps `completed` / `duration_seconds` after the loop. Flagging so the run does not ship
    the exact inversion it root-caused. The report's "This run itself complies" only becomes true after that
    re-stamp.
- code: F7
  category: editorial-advisory
  section: audit-report
  item: "docs/audits/2026-08-23-weekly-quality-audit.md § Factual errors table, last row"
  url_or_quote: "| `2026-08-16/weekly-w33-vuln-status-rollup` (second defect, counted once above) | — | — | — |"
  summary: >-
    Advisory: the row renders as a near-empty line in the published table and reads as a formatting defect
    rather than as the count reconciliation it is. A footnote under the table ("the w33 rollup carries two
    distinct defects; both are counted in the 10") carries the same information without the empty row.
```
