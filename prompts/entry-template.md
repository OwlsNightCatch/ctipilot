# Entry reference templates

Read by the intel-run and weekly routines during their compose phase. It
contains the canonical skeleton for an entry file and a run record, plus a
worked-good body fragment showing the technical-depth bar. The substantive
editorial / verification / state / publishing rules live in
`prompts/cti-run.md` and `prompts/weekly-summary.md`; the NORMATIVE
frontmatter contract is [`docs/pipeline.md`](../docs/pipeline.md) — this
file only shows the rendered shape.

---

## Worked-good body fragment (illustrative, not topic guidance)

This is the technical specificity every entry body must carry where the
source supports it — exact vulnerable component path, technique class with
MITRE ATT&CK IDs, exploitation prerequisites, affected and patched versions
to vendor-stated precision, named campaign clusters, behavioural detection
and hardening tied to the specificity (no IOCs, no rule code).

> A supply-chain compromise injected a malicious post-install script into the fictitious npm `@org/x-cli` package across versions 4.2.7 → 4.3.1; the script invokes `osascript` on macOS / `powershell.exe -enc` on Windows to harvest browser cookie jars from each browser's per-profile cookie store on disk and exfiltrates them via DNS-over-HTTPS to an attacker-operated edge-serverless resolver — TLS-encrypted, blends with normal browser DoH traffic, evades classic egress proxies that don't terminate DoH ([Vendor primary, YYYY-MM-DD](url)). Mapped to `T1195.002 Supply Chain Compromise: Compromise Software Supply Chain` and `T1071.004 Application Layer Protocol: DNS`. Detection concepts: alert on unsigned `osascript` / `powershell.exe -enc` invocations from `node` / `npm` / `npx` parent-process trees (Sysmon EID 1 + parent-image filter); inventory installed `@org/*` package versions across developer endpoints; block egress DoH resolvers other than the corporate ones. Hardening: pin npm dependencies via lockfile + `--ignore-scripts`; require signed packages for the affected scope. Affected versions: 4.2.7 through 4.3.1; fixed in 4.3.2.

The example is purely illustrative — actual depth is whatever the linked
primary source supports. **Better to write less than to fabricate
plausible-sounding specifics** (PD-1).

---

## Entry skeleton — vulnerability (operational)

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
discovered_at: "YYYY-MM-DDTHH:MM:SSZ"
event_date: "YYYY-MM-DD"
run_id: YYYY-MM-DDTHHMMZ-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, actively-exploited, cisa-kev]
regions: [global]
sectors: [technology]
entities: []
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
  - quote: "verbatim exploitation-status quote from a fetched page"
    publisher: "Vendor PSIRT"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions:
  - "Patch {Product} to ≥ {version} now; {rotation / isolation / hunt step tied to this entry's facts}."
migrated_from: null
---

{2–5 sentence body: what it is, prerequisites, exploitation status, who it
affects, detection + hardening — inline links at point of claim, worked-good
depth. No metadata footer line — frontmatter carries all metadata.}
````

**Classification.** The `vulnerability` skeleton above is a triage kind
(`classification.triage_kinds`), so it carries `org_triage` (a triage block
when a scheme is configured) and `classification: null`. **Every other kind
carries the NATO Admiralty classification instead of `org_triage`** — a
source-reliability letter (A–F) and an information-credibility number (1–6),
assessed independently (the reliability of the source never inflates the
credibility of the item):

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
  ends with a `**Defender takeaway:**` line.
- **critical entry** — `priority: critical` plus:

  ```yaml
  immediate_action:
    title: "{short imperative title}"
    action: >
      2–4 sentences: what is happening, why it is critical right now, and
      the specific time-critical defender action.
  ```

- **update note** — `update_of: <YYYY-MM-DD/slug>`; body opens
  `**UPDATE (originally covered YYYY-MM-DD):**` and carries only the delta.
- **deep dive** — `deep_dive: true` + `deep_dive_category: <rotation slug>`;
  body is the full deep-dive narrative (Background paragraph when PD-10
  applies, kill chain with ATT&CK links, hunt concepts, hardening).
- **weekly strategic** — `horizon: strategic` + `weekly_section: <weekly-*>`
  + `references: [<entry ids>]`; a `weekly-top-stories` body opens with
  `**If you did nothing this week:**`. The `weekly-looking-ahead` entry is
  `kind: outlook` with the justified watch list as its body.
- **closed-source entry** — `closed_sources: [{title, provider, date, ref}]`,
  inline attribution in the body as plain text
  `(Provider, YYYY-MM-DD — closed source)`, never a fabricated URL. There is
  no TLP gate: intel/ material is processed like any other source (a legacy
  `tlp` key, if present, is ignored). The classification block still applies —
  a single closed-source document is usually reliability `B`/`A` (per the
  provider) and credibility `2` until publicly corroborated.

---

## Run-record skeleton

`runs/<YYYY-MM-DD>/<run-id>.md` — frontmatter telemetry per
[`docs/pipeline.md`](../docs/pipeline.md) § Run records (schema, run_id,
kind, timing, models, window/gap hours, entry counters, sub_agents blocks,
fetch_failures, bridge_uses, sources_changed, entities_added, verification
iterations). Body:

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
