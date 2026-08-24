**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-24T15:35:43Z · ended_at=2026-08-24T15:49:06Z · duration_seconds=803

## Verification report — 2026-08-23T1311Z-audit (iteration 5, confirmation pass)

Cold full read of the four in-scope files. Every cited URL fetched this iteration via
`tools/fetch_source.py` (`url` for verbatim/JSON checks, `extract` for article bodies,
`ncsc-csh post` and `cisa-kev` bridge recipes). Every quantifier in the audit report and the
run-record notes recomputed from the store and from `work/2026-08-23T1311Z-audit/` ground data.

### Truth pass — entries

**Keycloak correction** (`entries/2026-08-24/cve-2026-18963-keycloak-no-red-hat-product-unfixed.md`)
- Red Hat hydra JSON: `package_state` carries exactly two rows, both `"fix_state" : "Not affected"`
  — JBoss EAP Expansion Pack (`keycloak-services`) and Red Hat Single Sign-On 7. Entry's central
  claim verified verbatim.
- Customer-portal page HTML: 2 × `"state":"Not affected"` with `"Component not Present"` (EAP XP)
  and `"Vulnerable Code not Present"` (RHSSO 7); 11 × `"state":"Fixed"`, 0 × `Affected`. Supports
  "every other product Red Hat lists carries a shipped erratum". `defaultStatus` appears 0 times on
  the page — the iteration-1 F1 remediation holds; the entry now uses the page's own vocabulary.
- Evidence quote is a contiguous verbatim substring of the hydra `mitigation.value`.
- Errata / versions / dates cross-check: 26.4.15 → RHSA-2026:56520, images RHSA-2026:56519;
  26.6.6 → RHSA-2026:56523, images RHSA-2026:56524; all `release_date` 2026-08-18. CVSS 9.1,
  `threat_severity` Critical. Citation date 2026-08-18 vs hydra `public_date` 2026-08-17 is a
  one-day errata-vs-disclosure offset, inside the tolerance.
- Update fidelity: the superseded 2026-08-19 entry does state EAP XP "Affected with no erratum" in
  its summary (l.14), `cves[].affected`/`fixed` (ll.38-39), body paragraph (l.96) and action (l.86),
  and does carry the reverse-proxy control — every characterisation of the original is accurate,
  and the correction does not overreach (RHSSO 7 was already right in the original).
- Frontmatter ⇔ body, classification A/2 (vendor PSIRT, two channels of one assessor — matches the
  store convention on Red Hat-sourced Keycloak entries), `verification: single-source` + carve-out
  `sourcing_note`, `techniques[T1190, T1098]` both supported by the hydra flaw description,
  2 actions both concrete and delta-derived. No defect.

**GitLab exploitation update** (`entries/2026-08-24/cve-2026-19478-gitlab-exploitation-confirmed-ncsc-ch.md`)
- SecurityWeek (dateline 2026-08-20, matches the citation): "Threat actors started exploiting …
  roughly two days after public disclosure", patched August 17, honeypot network caught the first
  in-the-wild attempts, both `evidence[]` quotes present as contiguous verbatim substrings
  (curly quotes included), fixed versions 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11, `/api/graphql`.
- NCSC-CH post 12856 (bridge): `lastModified` 2026-08-21T14:21:57Z, history reason "Updated with
  claims of active exploitation", body update "**Current exploitation status**: Actively exploited"
  citing the SecurityWeek URL, previous state "UNKNOWN". Supports the amendment claim, the date,
  the adoption framing, CE/EE product names and CVSS 9.4.
- Per-CVE authority (GitLab patch release, fetched): "all versions from 18.2 before 18.11.11,
  19.0 before 19.0.8, 19.1 before 19.1.6, and 19.2 before 19.2.4", CVSS 9.4, GitLab.com and
  Dedicated already patched — `cves[].affected`/`fixed` and the body's unchanged-mechanics
  paragraph all check out.
- CISA KEV catalogue fetched (catalogVersion 2026.08.21, 1674 entries): CVE-2026-19478 absent —
  the `sourcing_note`'s "not on the CISA KEV catalogue as of this run's check" is true, and no
  `cisa-kev` status tag was claimed.
- `verification: multi-source` with a `sourcing_note` that honestly discloses NCSC-CH as an
  assessment adopter rather than an independent observer, credibility held at 2; classification
  B/2 matches securityweek's `reliability: B` in sources.json. Priority `high` is calibrated —
  patch available six days, honeypot probing rather than confirmed mass compromise, no KEV.
- Triage discriminator follows from the cited hunt guidance; no IOC-class content
  (`@gl_introduced` is a protocol artifact quoted from the vendor's own hunting advice).
- The primary is a news article, but the origin (WatchTowr) published its honeypot claim through
  press statements — a targeted search surfaced only secondary coverage (THN, GovInfoSecurity,
  SecurityAffairs), no first-party post to promote. No F6.

### Truth pass — run record and audit report (every quantifier recomputed)

| Claim | Recomputed | Result |
|---|---|---|
| 112/135 clean · 13 imprecisions · 10 factual errors; per-batch 16/18/14/20/12/18/14 | `truth-B*.yaml` verdict tallies | exact |
| "every window entry exactly once" | `batch-B*.txt` = 135 lines, 135 unique, 0 dupes, 0 missing vs `window-entries.txt` | exact |
| 101 of 153 clock inversions | `completed-inversions.json` = 103 records incl. the two mid-audit weeklies (both present); store minus this run minus the two = 153 | exact |
| 48 non-migrated legacy records | `--all` prints 50 today; minus the two mid-audit weeklies = 48 on the Phase 0 basis the same sentence declares | consistent |
| 2026-08-19T0410Z-intel: 3 963 s, iteration 7 ended 07:18:13Z, true ≥ 11 269 s | record: `duration_seconds: 3963`, `started 04:10:24Z`, 7th iteration `ended_at 07:18:13Z` → 11 269 s | exact |
| waiver quote "passed the ~3 h guard at iteration 7 (186 min elapsed)" | verbatim in that record's `confirmation_waived` | exact |
| 2026-08-20T0409Z-intel "same shape" | completed 05:02:23Z vs last iteration 07:01:59Z | holds |
| 463 URLs in the liveness ledger | 474 rows now − 11 verifier-appended (iter3 ×7, iter4 ×4) = 463 at composition | exact |
| 16 run records, 16/16 publish_status ok, 73 iterations, mean 4.6, 3/16 confirmed CLEAN (08-09 audit, 08-17, 08-18), rotation held, iteration-2 exits on 08-12 and 08-13 | recomputed over the window | exact on every element |
| 0.80 actions/operational entry · 42.3 % actionless · 86 actions · 50.0 % high · 39 update_of · techniques mean 4.08, zero empty · classification 135/135 | recomputed over the 135 window entries | exact on every element |
| 8 `sources_changed[]` entries covering 12 source records | git diff: 11 changed + 1 added = 12; 8 bullets | exact |
| backlog 1 struck, 13 added (9 coverage + 4 corrections) | git diff of `state/coverage_backlog.md` | exact |
| `cves_seen` re-synced for both | both `last_seen: 2026-08-24`; the 19478 title carries the exploitation status and the KEV caveat | holds |
| trafilatura 18/20 hosts need no reader | `trafilatura-rollout.md` table: 20 hosts, 2 jina-pinned failures | exact |
| ATT&CK pin v19.2 == upstream; `site/build.py` self-check clean | gate output; build ran clean (entries=1336) | holds |
| SAP / Cl0p / credibility-1 table rows | match the batch YAML defect + ground-truth fields | holds |

Census arithmetic of the factual-error disposition (1 published + 5 queued via 4 rows + 4
documented = 10) reconciles against the table, including the footnoted two-defect w33 row.

### Editorial pass

Both entries clear the strict gate: an actively-exploited pre-auth flaw in a widely deployed
self-managed platform with a Swiss-authority nexus, and a correction that *withdraws* a
non-existent exposure — the second is exactly the case where an update earns its place, because
the superseded machine surfaces (`cves[].affected`, an action item) told operators to hold an open
risk item. Both are correctly `update_of` with the delta only and no re-litigation of the original.
No `org_triage`, no `watchlist_hit`, no `watchlist` tag anywhere (correct for this profile — no
scheme, no watchlists configured). Every entry carries an Admiralty block. No IOCs, no vanity
metrics, English throughout, no workflow-internal vocabulary in either entry. The run record's and
report's use of "sub-agent"/"main agent" is the audit's own subject matter and matches the
precedent set by `runs/2026-08-09/2026-08-09T1315Z-audit.md`; not a leak.

Coverage completeness: the nine queued items (SPIP CVE-2026-77647 first) are handled through
`state/coverage_backlog.md` with discovery traces, which is the sanctioned handoff — the next
fire's Phase 0 read duty drains them (`prompts/cti-run.md` § 5b), and the report names the
deferral reason for each. No omission I can name a plausible unqueued in-window source for.
Coverage looks complete.

### Editorial / less-is-more flags (advisory)

- **F1 (advisory, non-blocking, outside the four-file scope).** `tools/check_run.py` line 2765,
  new text in this commit: `# warned per record (98 of them would drown the store report).` The
  98 is the pre-correction figure iteration 3 replaced with 101 in the report, the run record,
  the CHANGELOG, `prompts/cti-run.md` and check_run.py's *other* new comment (line 2107). In this
  particular sentence neither figure is the right one: the count of per-record warnings actually
  suppressed is 50, the number `--all` prints (`PASS run-clock: 50 pre-v3.32 record(s) …`). No
  reader-facing artifact is affected and the run record's remediation claim is literally satisfied
  by line 2107, so this does not block publication — noted so the next audit does not re-derive it.

### Verdict

**CLEAN** (truth: 0, editorial: 0, advisory: 1)

The previous iteration's CLEAN is independently confirmed on a full cold read: both entries'
claims are supported by the pages actually cited, both `evidence[]` quotes are contiguous verbatim
substrings, both `cves[]` records agree with the owning vendor authority, and every quantifier in
the audit report and the run-record notes reconciles against ground data I recomputed myself —
including the 101/153 count iteration 3 corrected and the 463-URL ledger figure. The single
advisory item is a stale number in a code comment, which the main agent may leave.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F1
  category: editorial-advisory
  section: systemic
  item: "tools/check_run.py (out of the four-file scope; traceable to the iteration-3 remediation the run record claims complete)"
  url_or_quote: "# warned per record (98 of them would drown the store report)."
  summary: "New comment added by this commit still carries the superseded 98 figure that iteration 3 corrected to 101 everywhere else; in this sentence the suppressed per-record count is actually 50, the number `--all` prints. Non-blocking advisory; no reader-facing artifact affected."
```
