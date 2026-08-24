# Weekly quality audit — 2026-08-24

**Run record:** [`runs/2026-08-24/2026-08-24T0902Z-audit.md`](../../runs/2026-08-24/2026-08-24T0902Z-audit.md) · **prompt version:** v3.32

**Mandate.** Re-verify everything the pipeline published in the window against primary sources (soundness), re-research the window independently and diff against the store (completeness), and ask whether the machinery is drifting. Every confirmed defect is root-caused and either fixed here or raised as a numbered operator recommendation.

**Window.** 2026-08-09T13:15:57Z → 2026-08-24T09:02Z — **355 hours**, roughly fifteen days, inside the 21-day cap and audited in full. Double the usual length because no audit fired on 2026-08-16.

**Method.** 149 entries across 18 fires, partitioned into nine retrospective truth batches of 16–17 entries, alternating Opus and Sonnet. Six independent coverage re-sweeps, three per half of the window (vulnerabilities & exploitation; incidents & ransomware; threat research & APT by per-publisher listing sweep). One scoped deep read of the will-publish set. **Every one of the 149 entries was covered by exactly one truth pass.** 301 rows were appended to the run's URL-liveness ledger; the four truth batches that reported a fetch count total 129 primary URLs between them and the other five did not report one, so no store-wide total is claimed. Every ATT&CK id in every audited entry was checked mechanically against the pinned v19.2 dataset rather than from memory.

---

## Verdict

**125 of 149 entries verified clean on a cold re-read against primary sources. Four confirmed factual errors, all four in weekly strategic entries, all four corrected by new entries. Nineteen imprecisions documented.**

The content is in good shape and the direction of travel is right: the `actions[]` inflation that three consecutive audits escalated has reversed, verifier convergence recovered from 2-of-12 to 5-of-18, hallucinated-fact findings fell by nearly half per fire, and every one of the eighteen fires landed its publish-status amendment. What this audit found instead is that two of the pipeline's *measurement* surfaces were lying to it — the wall-clock guard has been reading a number that cannot see an overrun, and a recurring coverage miss turned out to be a source pinned to a dead transport rather than an editorial failure. Both are fixed here. The single most pressing item is not a defect at all: the metered reader pool is fully exhausted and has begun to block verification.

This fire also has to report on itself. It booted with a wrong clock and a stale clone, computed the wrong window, briefed eight sub-agents on it, and caught the error mid-run. That is written up in full below because a routine that can silently audit the wrong week is a more serious finding than anything it found in the content.

---

## The audit's own preflight failure

The container's clock read **2026-08-16T13:13Z** at boot and the first `git fetch origin main` returned refs eight days stale. The two errors corroborated each other: the newest visible run record was 2026-08-16T0411Z and the clock agreed it was the 16th, so nothing looked wrong. The fire computed a 168-hour window ending 2026-08-16, inventoried 81 entries, partitioned five truth batches and three coverage sweeps, and dispatched all eight.

For several minutes the evidence read as an **eight-day pipeline outage** — the shape a scheduled routine is specifically meant to catch and escalate. Ground truth came from an external HTTP `Date` header and a second fetch: the true time was 2026-08-24T09:02Z, `origin/main` was eight fires further on, and there was no outage. No operator notification was sent about it.

**Recovery.** Re-anchored to run id `2026-08-24T0902Z-audit`, the true 355-hour window and a re-inventory at 149 entries; four further truth batches and three further coverage sweeps were spawned to cover 2026-08-16 → 2026-08-24, which the first eight sub-agents had been told was out of window. The five truth batches already returned were kept — a wrong window *label* does not affect a check of a published entry against its primary source — and the three first-half sweeps were kept as valid for their half. Their checkpoint timestamps are preserved verbatim in the run record with the +7d19h49m offset stated, rather than silently rewritten.

**Root cause and fix.** Nothing in Phase 0 validated either input. `date -u` was trusted absolutely, and one `git fetch` was assumed authoritative. Both are now checked (v3.32, below), and every spawn message states today's date explicitly, because a sub-agent inherits the same bad clock and cannot detect it alone.

**What this cost.** Roughly fifteen minutes of wall clock and eight sub-agent spawns whose framing had to be supplemented rather than discarded. What it could have cost, on an intel fire rather than an audit, is a full run researching, deduplicating and publishing against a week-old window — with dedup silently passing everything, because a candidate from the true present looks new against a stale index.

---

## Findings — false or erroneous published intelligence

### Factual errors (4 entries, 2 distinct defects)

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| `2026-08-16/weekly-w33-vuln-status-rollup`, `weekly-w33-looking-ahead`, `weekly-w33-disclosure-to-exploitation-interval-collapsed` | All three state that GeoServer's actively exploited `jsonArrayContains` SQL injection had no CVE and **no vendor patch**; the outlook entry tells readers that until OSGeo ships something, taking query endpoints off the public internet "is the whole remediation" | OSGeo released GeoServer 3.0.1, 2.28.5 and 2.27.6 on **2026-08-14**, two days before these entries published (23:5xZ on 08-16), carrying the GeoTools 35.1 / 34.5 / 33.6 fixes. The flaw now also carries CVE-2026-76904, assigned when the advisory published 2026-08-21 ([GeoServer project](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html); [OSV](https://api.osv.dev/v1/vulns/GHSA-mqjf-5f49-2fjh)) | New entry `2026-08-24/correction-geoserver-w33-no-vendor-fix-claim-patch-existed`, `update_of` the status roll-up and referencing the other two plus the 08-18 operational entry |
| `2026-08-23/weekly-w34-exploited-is-now-a-per-authority-opinion` | Asserts three times that Microsoft's record for CVE-2026-33824 was never revised since 14 April, and describes the interval as weeks. Separately attributes to CERT-EU advisory 2026-010 the relaying of a research firm's no-exploitation finding | MSRC carries `latestRevisionDate` **2026-08-20** — two days *after* the KEV listing the entry argues about — revision note "Added clarifying information to the mitigation. This is an informational change only", `exploited: No`. 14 April to 21 August is four months. CERT-EU 2026-010's entire reference list is one Citrix knowledge-base article and the word "exploit" does not occur anywhere in it (both re-fetched by this audit directly) | New entry `2026-08-24/w34-exploited-flag-correction-msrc-ike-record-revised`, `update_of` the original |

Both root causes are the same shape in different clothing: **a claim about the state of a vendor record, sourced to something other than that record.** The GeoServer entries inherited "unpatched" from a 2026-08-14 news article whose headline was already stale when it published — the vendor's release went out the same day — and from a national advisory that did not append the fixed-version links until 08-17, the day *after* the weekly. Neither source was the party that would ship the fix. The W34 entry asserted an absence of revision without re-reading the revision field.

The GeoServer defect is the one with a reader cost: it published the wrong remediation for an actively exploited flaw. A team triaging off that weekly was told to isolate when it could have patched, and may since have relaxed the isolation believing nothing more was available. The pipeline's *operational* coverage self-corrected on 2026-08-18; the strategic surface did not, so for a week the two surfaces told readers different things.

### One reported error adjudicated down to a development

Batch B3 reported `2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves` as factually wrong for stating that two CVEs had been assigned and that the other primitives carried none, on the grounds that the researcher's page now lists three. **CVE-2026-56179 was published 2026-08-11 — one day after that entry.** The entry was correct when written. This is an update, not an error, and it is recorded here explicitly because an audit that logs a stale entry as a false one is manufacturing a finding.

It still warranted publication, and for a better reason than bookkeeping: the researcher records that the Windows mitigation for the newly-identified primitive is **initial-sequence-number randomisation shipped disabled by default and enabled only via a registry key**. A Hyper-V host that installed the August update and nothing else remains exposed while every scanner reports it compliant. Published as `2026-08-24/natjack-upstream-spoofing-cve-2026-56179-isn-randomisation`.

### Imprecisions (19) — documented, no repair warranted

Recorded so the pattern is auditable, not because each needs an entry. The distribution is informative: **ten of the nineteen are sourcing-attribution or classification defects rather than wrong facts.** (Nineteen imprecision verdicts, one per entry across nineteen distinct entries — recounted directly from the nine truth-B*.yaml files. One of the nineteen, the Keycloak CVE-2026-18963 record, is also escalated beyond documentation into a correction owed: it appears in the watch-item table and on the backlog, annotated with this audit's independent confirmation. The four themes below sum to nineteen and are a distribution over the same nineteen entries, so a single entry may appear in more than one bucket where a real defect spans them — the screensharingd entry is the one such case, listed once for an unattributed CVSS and once for the inherited 7.1 under a body arguing pre-auth remote root.)

- **Attribution drift (6).** A fact cited to a source that does not carry it, while being true. Two W32 entries attribute a "Rollout 524" version bound to a discloser's blog post that contains neither word — the bound comes from the CVE records. A W32 entry asserts a Black Hat USA 2026 briefing as fact with neither cited source mentioning it. A W32 entry upgrades a source's "supply chain risks" to "supply-chain implants". One entry attaches a CVSS to sources that publish no score. One PurpleDelta entry prints a reworded hedge inside quotation marks ("at least ten organizations" for the report's "ten or more organizations").
- **Classification over-award (4).** `credibility: 1` on items whose own sourcing notes describe a single assessor — a KEV determination "alone and nothing more", an advisory relayed by three publishers, a Swiss communal incident where every distinguishing fact is one newspaper's. This is the "one assessor, several publishers" pattern the previous audit sharpened the definition for; the verifier is now catching it reliably and composition is still over-awarding.
- **Machine-surface gaps (4).** A CVE record omitting an entire affected branch that the cited source names as having *no* fixed release (Rails 6.0–6.1.7.10 under a non-default configuration); `cvss: null` where the cited authority publishes a score; a 7.1 inherited from a parent entry and carried without attribution under a body arguing the flaw is pre-auth remote root; a `techniques[]` id (Cloud Accounts) contradicting an entry's own "anonymous web role" description.
- **Overstated precision (5).** A "first authority-issued control baseline" claim contradicted by another authority's May publication linked from the very page cited; "compromised on 14 August" where sources establish only detection that day; a patch date asserted to the day where three dates circulate and the cited authority was unreachable; a Fortinet 7.0 branch that appears in neither cited advisory; a "vendor vs researcher disagree" framing attributing to an advisory a statement it does not contain.

Store-wide, `cves[]` records with a null CVSS run at 8.3% of the window's 84 — worth watching as a machine-surface metric, since an automated triage consumer reading the store cannot prioritise what has no score.

---

## Findings — missing or incomplete coverage

### What the sweeps confirmed clean

The great majority of what six independent re-sweeps surfaced was already published. The second-half research sweep alone independently confirmed roughly twenty distinct stories as correctly covered, and the incidents sweep marked 18 of its 24 returns as matches. Two items the first-half sweeps flagged as gaps — an Akira Safe Mode EDR-blinding case and an Austrian Chamber of Labour intrusion — had been published on 08-17 and 08-18 by fires the stale clone could not see; they are matches, not misses, and are recorded as such.

### Genuine misses, and what this fire did with them

Seventeen items cleared the gate and were not in the store. **Two were published; fifteen were queued on `state/coverage_backlog.md` with the reason for each**, which is the fifteen rows this fire appended (28 open in total against 13 before it). The publish set was capped deliberately to keep the verifier loop and publishing chain inside the wall-clock guard — not because the queued items are weak. Several are unauthenticated near-maximum-severity flaws, and saying so plainly matters more than a tidy number.

Published:

- **`2026-08-24/spip-4-4-20-and-4-4-21-two-preauth-rce-security-screen-blind`** — the strongest miss in the window. SPIP shipped 4.4.20 on 08-17 for CVE-2026-77647 (unauthenticated RCE, exploited in the wild per the CVE record), then shipped 4.4.21 on 08-20 for a *second* unconditional pre-authentication RCE affecting 4.4.20 itself; CERT-FR's advisory of 08-21 records the vendor reporting active exploitation, and on 2026-08-24 — while this audit's verifier loop was running — that advisory was updated to add the second flaw's own identifier, CVE-2026-77806. Both bulletins state the flaw is not covered by SPIP's security screen. SPIP is the default CMS across a great deal of French-speaking public administration. The operational trap is exact: a process tracking CVE-2026-77647 marks itself done at 4.4.20, and for the week between the two releases the second flaw had no identifier to track at all, so the estate read as patched and was not. **The audit's assigned reading paired that CVE with the CERT-FR advisory as one flaw; the deep read established they are two, three days apart** — which is the finding.
- **`2026-08-24/natjack-upstream-spoofing-cve-2026-56179-isn-randomisation`** — see above.

Queued with reasons (fifteen rows): Adobe ColdFusion APSB26-90 and Campaign Classic APSB26-123; the GitLab CVE-2026-19478 exploitation delta; the vCenter CVE-2026-59310 KEV-plus-attribution delta; a SPIP identifier watch; Cisco Crosswork and Secure Workload; Splunk SVD-2026-0801; the Joomla extension wave; Johnson Controls C-CURE 9000; Zalktis CVE-2026-59109; Bloctel; La Protection Civile; SUEZ Eau France; the Winnipeg hospital building-management ransomware case; GTIG's agentic vulnerability-discovery harness; and the TheHatman Azure/Entra directory claim.

Two of those deserve a note on *why* they are queued rather than published. **ColdFusion was held back deliberately:** the coverage sweep and the deep read disagreed on the CVE count (15 or 16 versus 13), and shipping a multi-CVE roundup whose identifier surface has not been read row-by-row off Adobe's own table is precisely the defect class this audit exists to catch. **The vCenter attribution** must ship as one assessor, not two: the China-nexus assessment and the Babuk-derived-ransomware finding both trace to the same incident-response firm, whose own posts were unreachable this run.

### The Joomla stream: a third recovery, and this time the cause

A Joomla third-party-extension disclosure stream produced two unauthenticated CVSS 10.0 flaws (YOOtheme ZOO, Sourcerer) and a CVSS 9.2 SQL injection (iCagenda) inside this window. None was published. Two prior audits — 2026-07-26 (Balbooa Gridbox) and 2026-08-02 (SP Page Builder) — recovered a miss from this same publisher's stream, making this the third. They are not consecutive: the 2026-08-09 audit recovered nothing from it and judged PD-8(b) "Took" on exactly that ground, which is why the rule looked fixed. (An earlier draft of this report said fourth, counting the 2026-07-18 audit; that audit's recoveries were WordPress WP2Shell, Kaspersky GoSerpent and Moodle local_o365, none of them from this publisher.)

**It was not an editorial failure.** `mysites-guru`, the original disclosing party and the only source in the list that publishes these, carries `fetch_method: jina` with `rss_url: null` — and every reader key is exhausted. The source had effectively ceased to exist while reporting `consecutive_quiet_periods: 0` and a recent successful fetch. `https://mysites.guru/rss.xml` returns HTTP 200 with dated items including all three of the missed disclosures. Fixed this run.

The general lesson is worth more than the fix: **a source pinned to a metered transport whose credit is gone looks identical to a quiet source.** Any recurring miss traced to one publisher should have its transport checked before its editorial handling is re-litigated.

### Correctly-droppable borderlines, documented

- **Royal Elementor Addons (CVE-2026-17123, CVE-2026-19217)** — authenticated-contributor SSRF and stored XSS, bundled in the same national advisory as the Forminator and User Profile Builder flaws the store did publish. Authenticated and lower severity; correctly below the bar that admitted its siblings.
- **DINUM / cloud.numerique.gouv.fr** and **Capgemini Engineering/Altran** — two French extortion claims with genuine public-sector-supplier relevance that fail the fake-news guard on current evidence. Unpublished, and correctly so.
- **1Password "FLAWED" study** — already an open backlog row judged a borderline drop; unchanged.
- **Group-IB's Mexican banking phishing-as-a-service and payment-fraud items** — reviewed and judged below the constituency bar; the notable part was the source recovery, not the content.
- **Seven industrialcyber.co in-window items** — standards, certification and legislative press releases with no original technical content.
- **CE-TCO presidential memorandum** — two OT labs independently flagged its implications for industrial operators. Genuinely interesting, but US policy with no near-term action for this constituency; a candidate for weekly strategic treatment rather than an operational entry.

### Watch items re-checked

- **Bloctel — RESOLVED.** The French consumer-protection authority confirmed the leak in a 2026-08-12 press release (3 million phone numbers, ~600,000 registrants, CNIL notified). That is exactly the first-party statement the watch item named as its resolution condition. Queued for publication.
- **Afpa — stays open, unpublished.** No confirmation since 2026-08-09.
- **BANATIC / Interior Ministry / four SDIS — stays closed.** Re-checked; no first-party statement. Not reopened.

---

## Findings — systemic and operational

### 1. Every `duration_seconds` in the store is a floor, and the wall-clock guard was reading it

The most consequential finding of this audit. Through v3.31 the record's `completed` was stamped in **Phase 5** — before the mechanical gate and before the Phase 5.7 verifier loop — so every fire's recorded duration stopped roughly where its verifier loop began.

**The majority of stored run records are affected**, with the worst skew at **125 minutes** (`2026-08-04T0411Z-intel`). No precise fraction is published here on purpose: three independent recomputations during this run's own verification loop landed on 103 of 146, 100 of 141 and 104 of 148, because the result moves with how the denominator is defined (records carrying a completion timestamp at all, versus records also carrying at least one child timestamp) and with whether this fire's own record is included. The two figures that reproduced identically every time are the ones that matter and are stated exactly: the worst skew, and the illustration below. `2026-08-10T0411Z-intel` records `duration_seconds: 3103` (~52 minutes) for a fire its own notes place at ~2 h 55 m, with its final verifier iteration returning at 06:58Z against a recorded completion of 05:02Z.

Why it matters: `RUNAWAY_RUN_SECONDS` is checked against exactly this value, so the three-hour guard had **no machine-auditable signal capable of seeing an overrun**. Every audit line reading "no runaway this window" — the previous audit's "longest 2.2 h, inside the ~3 h watchdog" included — was reading a floor.

And it had already been diagnosed. The 2026-08-10 weekly's own verifier caught the shape on that record, naming the cause precisely ("a `main.ended_at` stamp taken at the end of the state phase"), the run corrected its own frontmatter, and the mechanism stayed broken for every fire after it. **A verifier finding repaired only in the record it was found in is a fix that did not ship** — the generalisable lesson, now in memory.

### 2. Verifier convergence recovered, but not for the reason the fix intended

| metric | this window | previous | before |
|---|---|---|---|
| confirmed two-model double-CLEAN | **5 / 18** (27.8%) | 2 / 12 (16.7%) | 4 / 9 (44%) |
| mean verifier iterations | 4.9 | 5.8 | 6.6 |
| fires with a blocked alternate spawn | **0** | — | several |

The previous audit's watch item said: re-measure after v3.31's model-override ladder has had a week, and if the share does not recover, examine the early-exit rule. The share did recover, and four of the eight fires from 08-17 onward converged. But **the rotation held on all eighteen fires with zero blocked spawns**, so the override ladder — shipped precisely to rescue fires losing two-model agreement to blocked alternates — was never exercised. What changed is that iteration counts stopped collapsing to 2. The ladder is untested, not vindicated; the watch item stays open on that basis rather than closing on a number that moved for another reason.

### 3. Discipline drift reversed

| metric | this window | previous | store |
|---|---|---|---|
| operational entries | 104 | 65 | — |
| `high` share (operational) | 50.0% | 52.3% | 43.1% |
| actions per operational entry | **0.80** | 1.09 | 0.58 |
| entries with **no** action | **42.3%** | 23.1% | 61.6% |
| verifier F18 (action-item discipline) findings | **2** (1.1 per ten fires) | 3 (3.0 per ten) | — |
| `techniques[]` on behaviour kinds | 4.07 mean, 0 empty | 3.64, 0 empty | — |
| classification present | 149/149 | 80/80 | — |

The three-window monotonic rise in `actions[]` density (0.53 → 0.88 → 1.09) **broke**, and the "empty is normal" shape moved back toward the store baseline. No entry carries more than three actions. The verifier raised two action-item findings against three last window — 1.1 per ten fires against 3.0. The instrumentation the previous audit shipped is printing correctly every run, and this audit read the trend from it rather than recomputing — which is what it was for. The `high` share eased 2.3 points and remains above baseline; no calibration section ships (below).

Verifier finding rates, per ten fires and counted the same way the previous audit counted them (its published F3 38 and F4 65 reproduce exactly, which is how the method was validated): **F4 (hallucinated fact) 65 → 36.7**, a fall ofnearly half and the first real movement since the `grep -F` quote check shipped; **F17 7 → 3.3**; **F18 3 → 1.1**. Two rates went the wrong way: **F3 (claim-not-supported) 38 → 48.9**, so per-clause attribution is now the dominant residual defect and is getting worse, and **F1 (broken URL) 2 → 9.4**. An earlier draft of this report published much lower figures from a regex that only matched inline-flow findings and silently missed block-style ones; the corrected counts are above.

### 4. Source health: reachability, readability, and a measurement error

The previous audit's headline figure — five essential-tier sources green while contributing nothing across a full week — was **partly a measurement artefact**. It was computed by matching cited URL hosts against each source record's own `url`, which misses a publisher reached on a different host or one whose content arrives summarised in a weekly roll-up. Over the true window `dragos` contributed two cited sources, and the Swiss security-hub feed was the highest-yield source of the second half.

Four essential-tier records still contributed nothing: `cert-at`, `enisa`, `ncsc-ch-focus`, `ncsc-ch-incidents`. This run's sweeps established **by full-body fetch, not assumption**, that each is reachable and carries non-vulnerability content by design (policy, press, consumer-fraud pages). That is a genuinely quiet source, not a dark one.

The OT/ICS surface is better than reported and better understood. `nozomi-networks` had reached `consecutive_quiet_periods: 4` while being fully reachable with two in-period posts — the gap was date extraction, not transport, and the working recipe (read each post's JSON-LD `datePublished`) is now recorded. `industrialcyber-co` and `sans-ics` are reachable with working recipes. `claroty-team82` remains genuinely unresolved.

Also corrected: three publishers the previous audit listed among "seven research sources G3 could not read" are not tracked in `sources.json` **at all** — `symantec-broadcom`, `cybereason`, `forescout-vedere`. That is a registry gap, not a transport failure, and a materially more fixable problem. Symantec/Broadcom research is cited by two entries in this window — both on 2026-08-16 and both the same article — and by seven entries across six distinct articles store-wide, all with no source record, so it reaches the store only by news-pivot luck. `cybereason` is reachable but has published nothing in over six months — a dormant publisher.

### 5. Availability: four missing fires in fifteen days

No run record exists for 14, 21 or 22 August, and no audit fired on 16 August. Cadence is the operator's to set and is explicitly not a finding — but a *record-less* gap on a schedule that was otherwise firing is an availability signal, and four in fifteen days is worth surfacing. The self-healing worked correctly every time: the 08-15 fire computed a 48 h catch-up window and the 08-23 fire a 72 h one, both disclosed in their records, and the 08-15 fire additionally walked publisher listing pages for the gap dates rather than relying on catalogue feeds. **No coverage hole opened.** The consequence that did land is this audit's own: its window was twice its normal length because the 08-16 audit slot was missed.

### 6. Publish follow-through and the gate: clean

All 18 fires carry `publish_status: ok`. `check_run.py --all` ended 0 warn · 0 fail (14 acknowledged) at preflight and again after this run's fixes, with the single later exception being this run's own record — see the zero-warning sweep below. The ATT&CK pin is current (v19.2, local == upstream). No store-wide FAIL, no unmentioned pin drift.

### Fix effectiveness — the previous audit's v3.31 changes

| Fix | Evidence | Verdict |
|---|---|---|
| `state/coverage_backlog.md` + Phase 0 read duty | **25 rows struck**, 13 open at the start of this fire. The 2026-08-10 intel fire drained fifteen rows in one run, publishing fourteen and striking one on relevance — hours after that morning's weekly complained the queue was not being worked | **Took, decisively.** The watch item closes |
| Weekly duplicate-week branch sweep | Caught nothing new; the 08-10 weekly's stand-down was reached by the pre-verifier re-check instead, and its record documents why the branch sweep could not see the primary (the interval between a primary completing locally and its push becoming visible) | **Took as designed; the residual blind spot is unchanged and correctly identified** |
| Blocked-alternate model-override ladder | **Never exercised** — zero blocked spawns across 18 fires | **Untested.** Convergence recovered for an unrelated reason |
| `check_run.py` whole-chain rotation integrity | Rotation held on all 18 fires; no violation to catch | **In force, nothing to report** |
| `credibility: 1` + `single-source*` mechanical FAIL | Zero violations. But four `credibility: 1` over-awards this window all sit on `multi-source` entries whose own notes describe one assessor — outside what the check can see | **Took for the shape it covers; the residual shape is not mechanisable** |
| Composition report instrumentation | Printing every run; this audit read the actions and `high`-share trend from it rather than recomputing | **Took** |
| PD-8(b) disclosure-stream scoping (v3.30, re-check) | Third audit recovering this publisher's Joomla stream (not consecutive — 08-09 found nothing from it), but the cause is a dead transport, not the editorial rule | **The rule holds; the miss had a different cause, now fixed** |

---

## Priority calibration

**Not due.** The monthly duty is at most one `## Priority calibration` section per calendar month across audit reports, and the 2026-08-02 report carries this month's. The `high` share is recorded above (50.0% operational, against 43.1% store-wide) for the September fire to judge, with the note that both halves of this window were exploitation-dense.

---

## Fixes shipped in this commit

**Prompts v3.32** (`cti-run.md`, `weekly-summary.md`, `quality-audit.md` banners in lockstep; CHANGELOG entry with Why / What changed / What stays):

- **`completed` and `duration_seconds` now cover the whole fire.** The Phase 5 `main.ended_at` stamp is marked provisional; Phase 6 step 0 re-stamps immediately before staging, after the verifier loop closes. Phase 7 polling stays outside the figure by design.
- **Phase 0 establishes ground truth for "now" and "latest" instead of assuming them.** The container clock is cross-checked against an external HTTP `Date` header with multi-host fallback; the clone is checked by listing the newest run record on `origin/main` and re-fetching before concluding a suspicious gap is an outage. Every spawn message states today's date. *The snippet was tested on both paths before shipping, and testing it caught two real bugs in the author's own first draft: a stray CRLF that made `date` parse to midnight, and — worse — an empty header making `date -d ""` return today at midnight, which would have "corrected" a good clock into a bad one. Both are guarded.*
- **A "no patch exists" claim must come from the vendor's own release or advisory channel** (Phase 2 item 4b), cited to that check, in the run that publishes it. The vendor's page saying nothing is itself the citation, and a different claim. A relay's "unpatched" corroborates the exploitation, never the absence of a fix. The mirror case — a *patched* claim — needs the vendor's version table.

**`tools/check_run.py`** — one addition, `check_completion_covers_run`: FAILs a v3.32+ record whose `completed` precedes any `verification.iterations[].ended_at` or `sub_agents.*.ended_at` it carries, naming the worst offender and the skew; WARNs under `--all`. Scoped to v3.32+ records so those 100 immutable pre-rule records do not become 100 acknowledgment-ledger rows. Exercised against five cases (fresh FAIL, fresh PASS, legacy informational, store WARN, legacy silence) before shipping.

**`sources/sources.json`** — four record changes and one new candidate (the per-run cap):

- `mysites-guru`: `fetch_method` jina → rss, `rss_url` set. The root cause of a miss three audits have now recovered (2026-07-26, 08-02 and this one).
- `tenable-research`: `rss_url` set to the verified `/blog/feed` path; the recorded "feed parses to count=0" note was stale.
- `nozomi-networks`: working date-extraction recipe recorded (JSON-LD `datePublished` per post).
- `claroty-team82`: unresolved state and the next transport to try recorded, explicitly not demoted — a date-extraction gap is not a transport failure.
- **`forescout-vedere` added as candidate**, with a sitemap-via-bridge recipe verified end-to-end. Already cited by a published 2026-08-10 entry while absent from the list under any id.

**Four new entries** — two corrections (`correction-geoserver-w33-no-vendor-fix-claim-patch-existed`, `w34-exploited-flag-correction-msrc-ike-record-revised`), one recovered miss (`spip-4-4-20-and-4-4-21-two-preauth-rce-security-screen-blind`) and one development update (`natjack-upstream-spoofing-cve-2026-56179-isn-randomisation`), each through dedup, the mechanical gate and this run's verifier loop. `state/cves_seen.json` gains three records.

**Fifteen backlog rows** appended with a reason each, and the existing Keycloak correction-owed row annotated with this audit's independent confirmation of the same defect.

**`.claude/memory/scheduler-and-workflow-races.md`** gains the completion-timestamp defect, its measurement, and the generalisable lesson that a verifier finding naming a *mechanism* must be fixed at the mechanism rather than in the record where it surfaced.

**`state/warning_acknowledgments.json` — unchanged.** All 14 rows still silence a live warning; none was pruned and none added. Nothing this fire found needed the ledger: every warning-class defect it touched had a real fix. **One mechanical check was deliberately not shipped:** flagging `no-patch` alongside `patch-available`, or a `no-patch` status with a prose `fixed` string, would have caught the GeoServer defect's shape but flags **27 correct records across 15 entries** — 3 carry both statuses in one record and 26 carry a `no-patch` status alongside a prose `fixed` string that exists precisely to explain why there is no fix. A partially-fixed estate legitimately carries both (Siemens Desigo CC V7/V8/V9, Check Point end-of-support trains). A check that warns on 27 correct records to catch one defect is a worse trade than the prompt rule.

**Zero-warning sweep complete, with one disclosed exception:** `python3 tools/check_run.py --all` ends **1 warn · 0 fail** (14 acknowledged) and `python3 site/build.py` emits no self-check warnings. The one warning is this audit record's own runaway duration (11.4 h — two provider session-limit outages, explained in the record's Wall clock section). It is the class the discipline says survives a run: a true telemetry fact about the fire itself, which the run must not self-acknowledge — the next audit reviews it, and acknowledging it then is the expected outcome since the record is immutable and the cause is documented.

---

## Recommendations (operator decisions, not shipped)

1. **Fund or retire the reader pool — it is now blocking verification, not just fetching.** *(Carried from 2026-07-26, 08-02, 08-09; escalated.)* Every configured key reports exhausted with a combined balance far below zero. Concrete costs inside this audit: a truth pass could not verify a patch date because the vendor's record is a JavaScript-only page; several sources could not be read; and a source-coverage fix this audit wanted to ship cannot be, because the publisher's site is client-rendered and the only transport that reads it is down. Options unchanged — a paid plan sized to the observed rate, a monitoring hook that alerts at the warning threshold rather than letting a fire discover it, or an explicit decision to accept the affected sources as best-effort. **What has changed is that "do nothing" now has a verification cost, not merely a coverage cost.**
2. **Investigate the four missing fires (14, 21, 22 August, and the 16 August audit slot).** Not a cadence question. The pipeline self-healed every gap with no coverage hole, so this is purely about whether the scheduler is dropping fires. The audit slot matters most: a missed audit doubles the next one's window, and a 21-day cap means two consecutive misses would start truncating.
3. **Populate the org-profile watchlists.** *(Carried from 2026-07-11, 07-18, 07-26, 08-02, 08-09.)* Still empty, so the product and supplier sweeps remain no-ops. This window's case: SPIP is the default CMS across French-speaking public administration and had two exploited unconditional pre-auth RCEs in four days; a product watchlist is what surfaces that at first sight instead of leaving it to a fortnightly audit.
4. **Widen the immutability-exception repair class to `cves[].type`, `cves[].fixed`, `cves[].affected` and a null `cves[].cvss` where a citable authority publishes one.** *(Carried from 2026-07-26, 08-02, 08-09.)* This window adds four supporting cases from the imprecision list, including an omitted affected branch that the cited source names as having no fixed release at all. An automated triage consumer reading the superseded record keeps reading it, because `update_of` does not rewrite the original's machine surface.
5. **NEW — add source records for the publishers the store already cites but does not track.** `symantec-broadcom` (two citations this window, seven store-wide across six articles), plus `0patch-blog`-adjacent gaps and the dormant-publisher question for `cybereason`. This is not the same work item as the OT/ICS recipe pass: these publishers are *reachable*, they are simply not in the list, so they never enter a rotation slice. The audit's one-candidate-per-run cap is why only `forescout-vedere` shipped here. Symantec specifically is blocked on recommendation 1.

Recommendation 4 of the 2026-08-09 audit — diagnose the dark OT/ICS surface as a scoped work item — is **discharged**: this audit's sweeps established per-source reachability by full-body fetch, fixed two recipes, recorded a third, and narrowed the genuinely-unresolved set to one source (`claroty-team82`) with a named next step.

---

## Watch items

| Item | Status | Resolution condition |
|---|---|---|
| Verifier-loop convergence | **Open — recovered, but the shipped fix is untested.** 5/18 confirmed double-CLEAN (from 2/12), mean 4.9 iterations, four of the eight fires from 08-17 converging. Zero blocked spawns, so the v3.31 override ladder was never exercised | Next audit re-measures the same three numbers. If a fire *does* lose its alternate spawn, check the record shows the ladder walked (retry → override → recorded exception) rather than a straight waiver. If the confirmed-CLEAN share falls again with the rotation intact, the early-exit rule is the thing to examine — specifically whether an exit at iteration 2 should require the residual re-checked rather than counted |
| `actions[]` density | **Open — reversing, downgraded from escalated.** 1.09 → 0.80, no-action share 23% → 42%, verifier F18 3.0 → 1.1 per ten fires, none above three actions | Read the composition report's trend each audit. Two consecutive windows near the 0.58 store baseline closes this |
| Dark OT/ICS and essential-tier sources | **Largely resolved; narrowed to one source.** The prior figure was partly a host-matching artefact. Two recipes fixed, one recorded, four essential-tier records confirmed reachable-and-quiet-by-design by full-body fetch | `claroty-team82` alone remains: probe `claroty.com/sitemap.xml` via the bridge (the route that worked for Forescout). Closes when that resolves or the source contributes |
| Coverage backlog is worked down | **CLOSED — the mechanism took.** 25 rows struck; the 08-10 intel fire drained fifteen in one run | Discharged. Volume is now the thing to watch, not consumption: 28 open rows after this fire's fifteen additions, and the file's own ~30-day rule starts expiring the oldest in early September |
| Reader pool exhausted | **NEW — open, and now a verification blocker.** Every key exhausted; one truth pass and one source fix blocked by it inside this audit | Recommendation 1 is decided either way. A refilled pool, or an explicit operator decision to treat reader-only hosts as out of scope |
| Missing fires / scheduler availability | **NEW — open.** Four record-less slots in fifteen days (14, 21, 22 August, plus the 16 August audit) on schedules otherwise firing; every gap self-healed with no coverage hole | Recommendation 2. Closes on an operator answer, or on a window with no record-less gap |
| SPIP second flaw identifier | **CLOSED in-run.** CERT-FR added CVE-2026-77806 to its advisory on 2026-08-24 while this fire's verifier loop was running; the published entry carries both identifiers and the backlog row was struck the same run | Discharged. The week in which the flaw had no identifier is the part worth remembering: any estate triaged in it shows a closed CVE and an exposed server |
| Keycloak CVE-2026-18963 correction owed | **Open — independently confirmed twice.** The 08-23 weekly queued it; this audit's batch B7 found the same defect cold. Red Hat's product-state table now reads Not affected for the product the entry says has no fix | The `update_of` entry ships from the backlog. Row annotated with both readings |
| Afpa leak-site claim | **Open — correctly unpublished.** No confirmation since 2026-08-09 | A first-party statement, or A/B-grade journalism confirming scope |
| Unconfirmed French leak-site claims (BANATIC / Interior Ministry / four SDIS) | **Closed — stays closed.** Re-checked; nothing new | Reopens only on a first-party statement |
| Bloctel | **CLOSED — resolved as confirmed.** The French consumer-protection authority's 2026-08-12 press release is the first-party statement the item required | Discharged; queued for publication as a backlog row |


---

## Post-merge addendum — what the Phase 6 sync revealed, and which claims above it supersedes

Written after this audit's verification loop closed, when the pre-publish sync pulled a set of **late-promoting fires** onto `main` that were invisible to every fetch this run made — including a second, independent quality audit. Everything below supersedes the corresponding claims in the body above; the body is left as written because it accurately reports what was knowable when it was written, which is itself part of this audit's story about stale clones.

**A second audit ran on 2026-08-23 and reached `main` first.** `2026-08-23T1311Z-audit` covered 2026-08-09 → 2026-08-23 (135 entries, 112 clean) and its work late-promoted during this run's blocked hours. The two audits overlap on thirteen days of window and **independently found the same two headline defects**: the completion-timestamp inversion (their v3.33 "run clock" fix reached `main` first and stands; this run's duplicate gate check was discarded in the merge rather than shipped twice) and the W33 GeoServer no-patch error (they queued the correction; this run published it, striking their backlog row). Two independent cold audits converging on the same defects is the strongest corroboration either could have received; the cost was duplicated work neither could see.

**The availability finding shrinks to one day.** The body reports 14, 21 and 22 August as record-less and counts four missing fires. After the late promotions, `runs/2026-08-21/` and `runs/2026-08-22/` exist (the 08-22 fire published 16 entries over a 50 h catch-up window), and the 08-23 audit occupied the missed 08-16 audit slot's duty. **Only 2026-08-14 remains genuinely record-less**, and the 08-15 fire's catch-up window covered it at the time. Recommendation 2 narrows accordingly: the question for the operator is why promotions from several fires sat unmerged long enough for two audits to plan against a stale picture — a pipeline-latency question at least as much as a scheduler one — plus the separate fact that **two fires on 2026-08-24 booted with clocks reading 2026-08-16** (this one, which recovered mid-run, and `2026-08-24T0906Z-intel`, which stood down), which points at a container-image or host clock fault worth raising with the platform.

**The SPIP "miss" was not a miss.** The body calls SPIP the strongest miss in the window; the late-promoting `2026-08-22T0410Z-intel` had already published `2026-08-22/spip-two-unconditional-preauth-rce-releases-three-days-apart`, a thorough entry whose closing warning — the second flaw has no CVE to track — is exactly what changed on 2026-08-24. This audit's SPIP entry was accordingly rewritten before commit as an `update_of` delta on that entry, carrying only the new identifiers (CVE-2026-77806, and CVE-2026-77647's addition to CERT-FR's companion advisory, both 2026-08-24). The 08-23 audit had *also* queued SPIP as a miss — all three fires were blind to each other, which is the stale-clone lesson again, this time at the cost of near-duplicate work rather than a wrong instruction.

**Entries this audit's truth passes never saw.** The late promotions added the 08-21 and 08-22 fires' entries (5 + 7 files now on disk in their day folders, plus two 08-24 entries the 08-23 audit published) after this audit's batches were partitioned. They were **not truth-checked by this run**; the 08-23 audit's window covered the days in question, but its passes ran before some of those promotions too. **The un-audited residue is bounded and named: the next audit's window should explicitly confirm the 2026-08-21 and 2026-08-22 entries were covered by the 08-23 audit's batches, and truth-check whatever was not.** This is recorded as a watch item in spirit; the backlog and both audit reports carry the pointers.

**Prompt versioning.** The body describes this run's changes as v3.32. In the merge they ship as **v3.34** on top of the 08-23 audit's v3.33: the run-clock half was dropped as redundant (theirs stands), and the two halves v3.33 does not cover — the preflight ground-truth checks and the no-patch-from-vendor rule — carry over. The CHANGELOG entry discloses the collision.

**Warning state after the merge.** The late promotions brought four further store-wide warnings with them — three runaway-duration telemetry facts on the 08-21, 08-22 and 08-23 fires' own immutable records (each explained in its own record; the 08-21 and 08-22 figures are elapsed container lifetime around the same blocked hours this run experienced) and one recorded confirmation waiver on the 08-22 fire. All are settled history of the class the next audit acknowledges or sweeps; none is fixable by this run, and none was visible when this run's zero-warning sweep ran. `check_run.py --all` at commit time therefore ends 5 warn · 0 fail (14 acknowledged): this record's own duration plus the four inherited ones.

**Backlog reconciliation.** Their queue and this run's were merged: their base was kept, their GeoServer correction-owed row was struck as fulfilled by this run's published correction, this run's Cisco Crosswork and Bloctel rows were dropped (theirs published the first on 2026-08-24 and carries its own row for the second), the Keycloak row was already struck by their published correction, the SPIP watch row resolved in-run, and this run's remaining twelve rows were re-appended. The merged file is the authority.
