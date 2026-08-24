**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-22T06:33:43Z · ended_at=2026-08-22T06:41:28Z · duration_seconds=465
**Self-telemetry:** urls_checked=0 (live) · webfetch_calls=0 · bridge_fetches=0 · saved-artefact greps=31 (byte-literal `grep -F` / Python substring against `work/2026-08-22T0410Z-intel/*`)

## Verification report — 2026-08-22T0410Z-intel (iteration 3)

Confirming pass of the double-CLEAN gate. Scope as tasked: the iteration-2 remediation (priority-calibration paragraph), the newly added run-record prose, and a fresh cold read weighted toward frontmatter⇔body agreement, classification/priority calibration, action-item discipline, technique-mapping evidence support and quote byte-fidelity. Per the spawn instruction not to widen scope at 2.5 h wall clock, live URL re-fetching was NOT repeated — iteration 1 checked 48 URLs live and iteration 2 re-fetched the primaries behind every remediation; this pass verified claims byte-literally against the run directory's saved source bodies instead, and says so rather than implying live coverage.

### Priority 1 — the iteration-2 remediation is correct, not merely changed

Counted `priority:` across all sixteen files independently: **8 `high`, 8 `notable`, 0 `critical`** — reconciles with `entries_published: 16`.

All eight `high` entries named in the paragraph resolve to real files that are actually `priority: high`: TrueConf (`trueconf-server-preauth-sandbox-escape-kev-installer`), SPIP (`spip-two-unconditional-preauth-rce-releases-three-days-apart`), GitLab (`cve-2026-19478-gitlab-honeypot-exploitation-confirmed`), GTIG (`gtig-three-russian-clusters-authentication-flow-abuse`), PTC (`ptc-windchill-three-new-cves-unauth-rce-no-fixed-version`), TP-Link (`cve-2026-19586-tp-link-omada-openvpn-preauth-injection`), misp-stix (`misp-stix-trust-decision-bypass-no-released-fix`), crates.io (`crates-io-build-script-dropper-yank-lure-arrayref`). No `high` file is unaccounted for and no named item is `notable`.

The crates.io description in the paragraph — "whose payload executed at compile time with the building user's privileges on developer workstations and CI runners without the poisoned crate's code ever being called" — matches that entry's own cited mechanics (build-script execution; "Each poisoned release left the crate's own library source untouched and added exactly one thing: a new dependency on a same-day typosquat … whose build script reassembled a download URL").

Arithmetic: 8 high / 48 h = **4.0 per day** ✓. Prior fires verified from disk — `runs/2026-08-19/2026-08-19T0410Z-intel.md` `window_hours: 26`, and 7 of its 11 entries are `high` → 7 ÷ (26/24) = 6.46 → **6.5** ✓; `runs/2026-08-20/2026-08-20T0409Z-intel.md` `window_hours: 26`, 6 of its 10 entries `high` → 6 ÷ (26/24) = 5.54 → **5.5** ✓. Both prior figures are true. (Basis note carried as F3 advisory below.)

### Priority 2 — newly added prose checked against disk

- "all twenty-five iteration-1 remediations" — matches iteration 2's own accounting verbatim (`verification.iter2.md`: "re-verified all 25 iteration-1 remediations", "### Priority 2 — remediation verification (all 25 items)"). Faithful report, not an invented figure.
- Iteration-2 metadata: `model: "Sonnet 5"` / `subagent_type: cti-verification-alt` / `started_at 06:14:12Z` / `ended_at 06:25:01Z` / `truth: 1, editorial: 0, advisory: 0` — all match `verification.iter2.md`'s own Model/Timestamps lines and its single-record findings YAML. `verification_iterations: 2`, `verification_residual_count: 1` consistent.
- "the recovered crates.io entry its first cold read — iteration 1 had never seen that entry" — true: iteration 1's F10 is the coverage finding that produced it, and the R1 sub-agent ran 05:59–06:08Z, after iteration 1 ended 05:57:41Z.
- Operational-mistake paragraph: consistent with the artefacts on disk (`verify.iter2.started_at` carries 06:33 — a later overwrite by the aborted retry — while `verification.iter2.md` itself records 06:14:12Z→06:25:01Z; the paragraph's account of a race against the agent's final writes is exactly what that artefact state shows).
- "**Action items.** Nineteen actions across twelve entries; four of the sixteen ship none at all — the Swiss municipal compromise, the Spanish municipal claim, the Defender-driver research and the SPECTRE entry" — recounted from frontmatter: **19 actions across 12 entries**, and the four empty lists are exactly `martigny-combe-…`, `kairos-velilla-…`, `btr-defender-…`, `uat-10147-…` ✓.
- "returned 131 literal-verified quotes between them" (F3a + F3b) = 52 + 79 from the two sub-agent notes ✓.

### Priority 3 — fresh cold read (what two passes may both have missed)

Checks performed and passed:

- **Classification.** All sixteen entries carry a `classification` block; every letter in A–F, every number in 1–6; no `org_triage` block on any entry (none configured); `watchlist_hit: false` everywhere and no `watchlist` tag (none configured) — no F16/F17. The four `credibility: 1` entries (crates.io, GitLab, TrueConf, Zoom) each show genuine independent corroboration in `sources[]`; the two deliberately-lowered ratings (`ftp-banner` C/2, `uat-10147` B/2) match their sourcing notes.
- **Primary-source kind.** No entry cites an NVD/MITRE/cve.org per-CVE page or a bare index as primary. The GitLab entry's news-outlet primaries are justified in its `sourcing_note` (watchTowr published nothing first-party; its statements exist only as on-record quotes) — defensible, not F6.
- **Technique-mapping evidence.** `ftp-banner` maps 35 ids; SOCRadar's own published mapping in the saved body contains 34 of them **identically** (set-diff: only `T1204.002` is the pipeline's, and it follows the report's stated archive-plus-shortcut/phishing assessment). `gtig`'s `T1123`/`T1125` are carried by the source's "the audio and video are recorded"; `crates-io`'s `T1568.002` by Wiz's "Falls back to a Domain Generation Algorithm … generating 10 algorithmic" — no F4/F11 on the large mappings. No `threat`/`incident`/`vulnerability` entry has an empty `techniques[]`.
- **Quote byte-fidelity (spot check, byte-literal).** GitLab 3/3 contiguous substrings of `gitlab_sw_text.txt` / `gitlab_cso_text.txt`; Martigny-Combe 3/3 of `mc_ictjournal.txt` / `mc_nouvelliste.txt` including the curly-apostrophe form `l’incident`. Martigny's uncited-looking specifics all verify in their attributed source: `Préposé cantonal à la protection des données et à la transparence`, `Office fédéral de la cybersécurité (OFCS)`, `plainte`, and `Cet incident survient quelques mois après la cyberattaque qui avait perturbé une commune valaisanne, celle de Vétroz.`
- **Adjacency spot check.** GitLab's "Its reproducibility warning came on 18 August … ([CSO Online, 2026-08-19])" — the CSO article's own `datePublished` is `2026-08-18T19:29:43-07:00` (= 08-19 UTC, the one-day render artefact the contract permits) with an "Updated August 19:" block carrying the honeypot detections, so both the 18-August dating and the day-apart separation claimed in the `sourcing_note` are carried by that page; SecurityWeek independently states "On August 18, WatchTowr warned…". Not a defect.
- **Crates.io figures.** "07:11 and 09:25 UTC" and "Twenty-four seconds after publishing … the five preceding clean releases" verify literally against `step.clean` ("the 07:11–09:25 UTC exposure window"; "Twenty-four seconds after publishing 0.3.10 … 0.3.9 at 07:15:24, then 0.3.8, 0.3.7, 0.3.6, and 0.3.5"); "alerted at 07:54 UTC" is present in the saved BleepingComputer and StepSecurity bodies. No unsourced dependent count appears in the entry at all.
- **Action-item discipline (F18).** All 19 actions read as concrete, finding-derived, start-now tasks naming a version boundary, a time window, a configuration surface, a log string or a vendor article. No generic-advice item, no duplicate across the window, no list longer than three. The four empty lists are correct for their entries. No F18.
- **Priority calibration.** Zero `critical` is right — the closest candidate (TrueConf) has a fix shipped 18 June and an out-of-constituency victim set. Each of the eight `high` entries clears the TL;DR bar on exploitation, unpatched exposure, or compile-time detonation; no `notable` entry plainly clears the critical bar. No F16.
- **Style.** No IOCs, no vanity metrics, English throughout, no workflow-internal vocabulary in any entry or in the run-record notes.
- **Update-vs-new.** One `update_of` in the run (GitLab → `2026-08-19/cve-2026-19478-gitlab-graphql-unauth-data-destruction`), matching `entries_updated: 1`; it carries a genuine delta (exploited status, NCSC status flip, two mechanism corrections).
- **Coverage completeness.** With the crates.io gap now closed and the three documented drops (Unit 42 telemetry-percentage report, uncorroborated Swiss leak-site claim, out-of-window SSD Unisoc) each carrying a stated reason, I can name no in-window story with a plausible source that the run missed. Coverage looks complete.

### Editorial / less-is-more flags (advisory)

**F1 — run record, `verification.iterations[0]`: stated counts (27) exceed the enumerated `findings[]` records (26).** The record carries `truth: 17, editorial: 6, advisory: 4` (= 27, faithfully copied from iteration 1's own verdict line, which I confirmed reads `NEEDS_FIXES (truth: 17, editorial: 6, advisory: 4)`), but `findings[]` holds 26 records — 16 truth-class, 6 editorial, 4 advisory. The missing record is iteration 1's second UAT-10147 F4 (`verification.iter1.findings.yaml` record 11: "the body carries no naming overlap at all; Talos's only such statement is medium-confidence…"), which was folded into the adjacent F3 record for the same entry whose `remediation_applied` reads "…and the actor-naming overlap the note claimed was carried is now actually in the body at the source's own confidence." No remediation was lost — I confirmed the body now carries it ("Talos also associates the actor with a handle it renders as x神, again at medium confidence") — so this is a telemetry-completeness nit on the Ops-dashboard surface, not a false claim. Leave or split the merged record; either is defensible.

**F2 — `uat-10147-spectre-callback-unlinking-linux-rootkit`: the x神 association is scoped to the actor where Talos scopes it to components.** Entry body: *"Talos also associates the actor with a handle it renders as x神, again at medium confidence."* Talos (saved body `talos_spectre_flat.txt`): *"Talos also observed several SEO fraud-related components used in this campaign that we assess with medium confidence to be associated with "x神" ("xshen"), who is mentioned in a previously released Talos post."* The confidence qualifier is preserved correctly and the entry deliberately declined to create a registry alias; what shifts is the subject of the association (campaign components → the actor). Tightening to "several SEO-fraud components used in this campaign" would match the source exactly. Advisory rather than F3 because the components are the actor's own tooling in the same campaign, so the looser phrasing is a defensible paraphrase rather than an unsupported link.

**F3 — run record, priority-calibration paragraph: the per-day comparison mixes window bases.** *"That is eight `high` across a 48 h window — 4.0 per day against 6.5 and 5.5 for the two preceding 26 h fires."* The 4.0 is computed over this run's `gap_hours: 48` while its own frontmatter carries `window_hours: 50` (on which it would be 3.8), and the two prior figures are computed over those fires' `window_hours: 26` (on their `gap_hours: 24` they would be 7.0 and 6.0). The stated arithmetic is internally correct against the 48 h the same sentence names, every figure is checkable, and the conclusion ("a lower daily rate than either") holds on either basis — so this is a precision nit, not an error. Naming the basis once ("per 24 h of gap") would remove the ambiguity.

### Verdict

CLEAN

No truth defects and no editorial defects found. Three F11 advisory items above, all of which the main agent may leave; none changes a fact a reader acts on. The iteration-2 remediation is correct on every axis I could test independently — the priority counts, the eight named `high` entries, the crates.io characterisation, and all three per-day figures reconcile against the entry files and the two prior run records on disk. The newly added prose is true of what is on disk. Sampling disclosed: live URL re-fetching was not repeated this iteration (48 URLs live in iteration 1, primaries re-fetched in iteration 2); this pass verified byte-literally against the run directory's saved source bodies.

### Findings summary (machine-readable)

```yaml
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-08-22/2026-08-22T0410Z-intel.md — verification.iterations[0]"
  url_or_quote: "truth: 17 / editorial: 6 / advisory: 4 against 26 enumerated findings[] records"
  summary: "iteration-1 counts total 27 (correctly copied from its verdict line) but findings[] holds 26 records; the second UAT-10147 F4 (iter1 findings.yaml record 11) was merged into the adjacent F3 record. Remediation itself is present in the entry body — telemetry-completeness nit only."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "2026-08-22/uat-10147-spectre-callback-unlinking-linux-rootkit"
  url_or_quote: "Talos also associates the actor with a handle it renders as x神, again at medium confidence."
  summary: "Talos scopes the medium-confidence x神 association to 'several SEO fraud-related components used in this campaign', not to the actor. Confidence hedge preserved; subject broadened. Tighten to the components for an exact match."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-08-22/2026-08-22T0410Z-intel.md — Priority calibration"
  url_or_quote: "That is eight `high` across a 48 h window — 4.0 per day against 6.5 and 5.5 for the two preceding 26 h fires."
  summary: "4.0 uses gap_hours 48 while frontmatter window_hours is 50 (3.8); the prior figures use those fires' 26 h windows (6.46 and 5.54, correctly rounded). All figures check out and the conclusion holds on either basis; naming the basis once would remove the ambiguity."
```
