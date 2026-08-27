# Entry reference templates

Read by the intel-run and quality-audit routines during their compose phase.
It contains the canonical skeleton for an entry file and a run record, a
worked example of updating an existing entry through its changelog, plus a
worked-good body fragment showing the technical-depth bar. The substantive
editorial / verification / state / publishing rules live in
`prompts/cti-run.md` and `prompts/quality-audit.md`; the NORMATIVE
frontmatter contract is [`docs/pipeline.md`](../docs/pipeline.md) — this
file only shows the rendered shape.

---

## Worked-good body fragment (illustrative, not topic guidance)

This is the technical specificity every entry body must carry where the
source supports it — exact vulnerable component path, technique class
described as behavior (the MITRE ATT&CK ids live in `techniques[]`
frontmatter, inline in prose only where essential), exploitation
prerequisites, affected and patched versions to vendor-stated precision,
named campaign clusters, behavioural detection and hardening tied to the
specificity (no IOCs, no rule code).

> A supply-chain compromise injected a malicious post-install script into the fictitious npm `@org/x-cli` package across versions 4.2.7 → 4.3.1; the script invokes `osascript` on macOS / `powershell.exe -enc` on Windows to harvest browser cookie jars from each browser's per-profile cookie store on disk and exfiltrates them via DNS-over-HTTPS to an attacker-operated edge-serverless resolver — TLS-encrypted, blends with normal browser DoH traffic, evades classic egress proxies that don't terminate DoH ([Vendor primary, YYYY-MM-DD](url)). The install-time execution is a supply-chain compromise of the package's install hook and the DoH channel is DNS-based application-layer command-and-control — both mapped in this entry's `techniques[]` frontmatter (`T1195.002`, `T1071.004`), which is where machine consumers and the ATT&CK matrix read them; the prose stays readable without the numbers. Detection concepts, telemetry-class first: in process-creation telemetry with parent lineage (e.g. Sysmon EID 1, auditd `execve`, EDR process events), alert on script interpreters (`osascript`, `powershell.exe -enc`) spawning from `node` / `npm` / `npx` parent trees; inventory installed `@org/*` package versions across developer endpoints; in egress telemetry, surface DoH resolvers other than the corporate ones. **Triage:** developer machines legitimately spawn interpreters from `node` trees during builds — the discriminators are the DoH egress to a non-corporate resolver in the same process tree and reads of browser cookie stores by a non-browser process; either alone is weak, the sequence is the signal. Hardening: pin npm dependencies via lockfile + `--ignore-scripts`; require signed packages for the affected scope. Affected versions: 4.2.7 through 4.3.1; fixed in 4.3.2.

The example is purely illustrative — actual depth is whatever the linked
primary source supports. **Better to write less than to fabricate
plausible-sounding specifics** (PD-1). Note the shape: telemetry class
leads and platform-native names (Sysmon EID 1) are *examples*, so any
stack — and an automated triage agent — can map the behavior; ATT&CK ids
live in `techniques[]` frontmatter (the canonical mapping surface,
validated against the pinned `attack/enterprise-attack.json`) and appear
inline only where essential, never as a bare list; the `**Triage:**`
discriminator derives mechanically from the cited mechanism and is
omitted entirely when the sources give no honest basis for one.

---

## Entry skeleton — vulnerability

`entries/<YYYY-MM-DD>/<slug>.md` — one `Write` per file. Field semantics:
[`docs/pipeline.md`](../docs/pipeline.md). Every taxonomy value from
`site/taxonomy.yaml`; every entity key from `entities/registry.yaml`.

````markdown
---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-YYYY-NNNNN — {Vendor} {Product}: {one-line description} (CVSS N.N)"
headline: "{Vendor} patches {an actively-exploited pre-auth RCE} in {Product}"
summary: >
  1–3 self-contained sentences naming the product, versions, exploitation
  status, and who must act. This is the TL;DR bullet, the RSS description,
  and the notification text.
discovered_at: "YYYY-MM-DDTHH:MM:SSZ"   # first publication — never changes
updated_at: null                         # == updates[-1].at once the entry has a changelog record
event_date: "YYYY-MM-DD"
run_id: YYYY-MM-DDTHHMMZ-intel           # the originating fire — never changes
priority: high
immediate_action: null
tags: [vulnerabilities, rce, actively-exploited, cisa-kev]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1190, T1505.003]   # every source-supported ATT&CK id (T####[.###]) — the canonical
                                 # mapping surface; ACTIVE ids per attack/enterprise-attack.json;
                                 # the body describes each behavior (inline ids only where
                                 # essential); NEVER [] on threat/incident/vulnerability (the
                                 # access/exploitation vector is always mappable — check_run
                                 # FAILs an empty mapping); [] only on kinds with no TTP content
affected_products: ["{Vendor} {Product}"]   # official product names; [] when not product-specific
cves:
  - id: CVE-YYYY-NNNNN
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "≤ N.N.N"
    fixed: "N.N.N+1"
sources:
  - url: "https://vendor.example/psirt/advisory-id"
    publisher: "Vendor PSIRT"
    date: "YYYY-MM-DD"
    role: primary
  - url: "https://lab.example/blog/exploitation-analysis"
    publisher: "Research Lab"
    date: "YYYY-MM-DD"
    role: corroborating
closed_sources: []
evidence:
  # contiguous verbatim substring of a fetched page — no ellipses, no
  # splicing, no re-hedging; two passages = two records
  - quote: "verbatim exploitation-status quote from a fetched page"
    publisher: "Vendor PSIRT"
verification: multi-source
sourcing_note: null
confidence: high
references: []                   # entry ids this finding builds on; a distinct finding sharing a
                                 # CVE with an older entry MUST list it here (else the gate FAILs it
                                 # as a duplicate)
deep_dive: false
deep_dive_category: null
org_triage: null                 # triage block when the org profile configures a scheme
classification:                  # with NO triage scheme configured (the shipped default),
  reliability: A                 # vulnerability entries carry the Admiralty block like
  credibility: 1                 # every other kind — no entry ships unrated
watchlist_hit: false
actions: []                      # do-now bar (cti-run.md Phase 4 § actions[]): empty is the
  # normal case — ship an action ONLY when it is a concrete task the team
  # starts now, derived from this finding's own mechanics; never generic
  # advice, never a restatement of the body's detection/hardening guidance.
  # When one ships: "Patch {Product} to ≥ {version} now and {the
  # rotation / termination / compromise-check the mechanics demand}."
updates: []                      # the changelog — empty on a new entry; see § Updating an existing entry
migrated_from: null
---

{2–5 sentence body: what it is, prerequisites, exploitation status, who it
affects, detection + hardening — inline links at point of claim, worked-good
depth. No metadata footer line — frontmatter carries all metadata.}
````

**Classification — every entry carries exactly one rating, never zero.**
The `vulnerability` skeleton above is a triage kind
(`classification.triage_kinds`): **when the org profile configures a triage
scheme** it carries `org_triage` and `classification: null`; **when no scheme
is configured** (the shipped default) it carries the NATO Admiralty
`classification` block like every other kind — `tools/check_run.py` FAILs an
entry with neither rating. **Every non-triage kind always carries the NATO
Admiralty classification** — a source-reliability letter (A–F) and an
information-credibility number (1–6), assessed independently (the reliability
of the source never inflates the credibility of the item):

```yaml
org_triage: null
classification:
  reliability: B   # A–F — reliability of the sourcing (see the org profile scheme)
  credibility: 2   # 1–6 — truth of the item given corroboration
```

Set the reliability letter from the reporting source's nature (a national CERT
for its own jurisdiction or a vendor PSIRT for its own product is A; original
research labs and large corroborating outlets are typically B; sources that
mainly re-report are C or lower — weight primary sources over aggregators). Set
the credibility number from corroboration: two independent sources agreeing → 1;
a single uncorroborated but plausible claim from a reliable source → 2, not 1.

Variants:

- **threat / incident** — same skeleton with `kind: threat` (campaign /
  actor activity) or `kind: incident` (breach / disclosure), usually
  `cves: []`, `org_triage: null` + a `classification` block (above), body
  ends with a `**Defender takeaway:**` line and — where the cited
  mechanism supports a benign-lookalike discriminator — a `**Triage:**`
  line adjacent to it (see `prompts/cti-run.md` Phase 4 § Triage-ready
  behavioral description; omit rather than invent).
- **critical entry** — `priority: critical` plus:

  ```yaml
  immediate_action:
    title: "{short imperative title}"
    action: >
      2–4 sentences: what is happening, why it is critical right now, and
      the specific time-critical defender action.
  ```

- **deep dive** — `deep_dive: true` + `deep_dive_category: <rotation slug>`;
  body is the full deep-dive narrative (Background paragraph when PD-10
  applies, kill chain with ATT&CK links, hunt concepts, hardening).
- **policy** — `kind: policy` for a regulatory action, deadline or authority
  guidance that changes what the constituency is obliged or advised to do;
  same skeleton, usually `cves: []`, `techniques: []` allowed, Admiralty
  block, body names the obligation and its date.
- **closed-source entry** — `closed_sources: [{title, provider, date, ref}]`,
  inline attribution in the body as plain text
  `(Provider, YYYY-MM-DD — closed source)`, never a fabricated URL. There is
  no TLP gate: intel/ material is processed like any other source (a legacy
  `tlp` key, if present, is ignored). The classification block still applies —
  a single closed-source document is usually reliability `B`/`A` (per the
  provider) and credibility `2` until publicly corroborated.

---

## Updating an existing entry — the changelog (worked example)

A finding has ONE entry for its whole life. A development, correction or
improvement on covered ground is appended to that entry — never a second
file (`prompts/cti-run.md` Phase 4 § Updating an existing entry; normative:
`docs/pipeline.md` § Entry lifecycle). `Read` the entry, then land the
record, the section and the frontmatter changes in one `Edit`/`Write`.

The frontmatter after two changes — a KEV listing (an `update`) and a later
audit correction of the fixed version:

````yaml
discovered_at: "2026-07-03T04:21:09Z"      # unchanged
updated_at: "2026-07-11T14:40:12Z"         # == the last record's at
run_id: 2026-07-03T0412Z-intel             # unchanged — updating fires appear in updates[]
priority: high                             # moved from notable by the 07-05 record
cves:
  - id: CVE-YYYY-NNNNN
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]   # current state — moved by the 07-05 record
    affected: "≤ 4.2.1"
    fixed: "4.2.2"                                   # corrected by the 07-11 record (was "4.3.0")
actions:                                   # the CURRENT do-now set — replaced, never accumulated
  - "Patch {Product} to ≥ 4.2.2 now; hunt for {the artifact the exploitation reporting names}."
updates:
  - at: "2026-07-05T04:40:12Z"
    run_id: 2026-07-05T0410Z-intel
    type: update
    summary: >
      CISA added CVE-YYYY-NNNNN to the Known Exploited Vulnerabilities catalog on 2026-07-04 and
      {Lab} reports in-the-wild exploitation since 2026-07-02; status moves from PoC-only to
      exploited and priority to high.
    fields: [cves, priority, tags, actions, summary]
  - at: "2026-07-11T14:40:12Z"
    run_id: 2026-07-11T1435Z-audit
    type: correction
    summary: >
      The fixed version was stated as 4.3.0; the vendor advisory's fix table names 4.2.2 as the
      first fixed release. Corrected in the CVE record, the action and the body.
    fields: [cves, actions, body]
````

The body: the main analysis first (corrected where it was wrong — the
correction record's `fields` says `body`), then one section per record,
same order, heading exactly `## <Type> — <at>`:

````markdown
{The main analysis — a complete, readable entry on its own. Where the
07-11 correction applies, this text now says 4.2.2, not 4.3.0.}

## Update — 2026-07-05T04:40:12Z

CISA added CVE-YYYY-NNNNN to the Known Exploited Vulnerabilities catalog on 2026-07-04
([CISA, 2026-07-04](https://…)). {Lab} observed exploitation against internet-exposed
{Product} instances beginning 2026-07-02, with {the observable behaviour the source
describes — telemetry class first} ([{Lab}, 2026-07-04](https://…)). The delta only —
no recap of the original analysis.

## Correction — 2026-07-11T14:40:12Z

The entry stated the first fixed release as 4.3.0. The vendor advisory's fix table names
4.2.2 ([Vendor PSIRT, YYYY-MM-DD](https://…)); the CVE record, the action item and the
analysis above now say 4.2.2. Readers who patched to 4.2.2 on the original guidance were
already fixed; the misstatement affected only the version boundary.
````

Rules the gate enforces: one record ⇔ one section, in order, same `at`;
`at` strictly later than `discovered_at` and than the previous record;
`updated_at` mirrors the last record; every new source cited in a section is
appended to `sources[]`; `discovered_at` / `run_id` / the path never change;
an entry file modified in the working tree without a record for the modifying
run FAILs (`silent-edit`). The updating run lists the entry id in its run
record's `updated_entry_ids[]` and counts it in `entries_updated`.

---

## Run-record skeleton

`runs/<YYYY-MM-DD>/<run-id>.md` — frontmatter telemetry per
[`docs/pipeline.md`](../docs/pipeline.md) § Run records (schema, run_id,
kind, timing, models, window/gap hours, entry counters — `entries_published`
for new files, `entries_updated` + `updated_entry_ids[]` for the entries this
fire appended a changelog record to — sub_agents blocks, fetch_failures,
bridge_uses, sources_changed, entities_added, verification iterations). Body:

````markdown
## Verification & coverage notes

- {borderline-drop: <title> — <reason>}
- {Single-source: <entry id> — <carve-out or [SINGLE-SOURCE] note>}
- {Contradiction: <topic> — A says X; B says Y; entries report <framing>.}
- {out-of-window: <title> — primary source <date>, window_hours=<N>}
- Coverage gaps: source-id (reason); source-id (reason); source-a, source-b — not fetched in this run.
- Watchlist: products checked=N, hits=N; suppliers checked=M, hits=M   *(only when configured)*
- Closed-source intake: files=N, items=M, folded-into-entries=K  *(only when intel present)*
- Essential-coverage: missed=source-id (reason)                          *(only on a miss)*
````
