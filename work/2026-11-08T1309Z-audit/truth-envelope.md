# Retrospective truth pass — shared brief (quality audit 2026-11-08T1309Z-audit)

This is a **retrospective audit pass**, not a Phase 5.7 iteration of an intel run. You are the cold, hostile, technically fluent reader your definition describes, applied to published entries a week after the fact. **Assume nothing; fetch ground truth.** Trust no claim because it is in the store or because an earlier verifier passed it.

- **Run id:** `2026-11-08T1309Z-audit` — checkpoint into `work/2026-11-08T1309Z-audit/` (`truth-<BATCH>.started_at`, a `truth-<BATCH>.progress` line per entry finished, `truth-<BATCH>.ended_at` last).
- **Today:** 2026-11-08 (UTC). Audit window: 2026-11-01T13:12Z → 2026-11-08T13:09Z.
- **Scope:** the entry files named in your spawn message, each **read and verified whole** (frontmatter, main analysis, labelled lines, every `## <Type> — <at>` section, every `updates[]` record summary).
- **Claim ledger:** `work/2026-11-08T1309Z-audit/truth-<BATCH>.ledger.yaml` lists every claim of your batch (citation clauses, uncited sentences, labelled lines, headline/summary/actions/cves records, record summaries). Write `work/2026-11-08T1309Z-audit/truth-<BATCH>.claims.yaml` with one row per ledger claim: `{claim_id, verdict: ok | F3 | F4 | F5 | F13 | F14 | unreadable, source_url, passage}`. Every claim gets a row.
- **Cached bodies:** `work/2026-11-08T1309Z-audit/quote-bodies/` holds bodies of cited pages the mechanical pre-pass fetched today (grep them first; fetch fresh where a page is missing or you need the current revision).

Per entry, check against **freshly fetched primaries**:

1. Every `cves[]` id, CVSS, affected and fixed version against the **per-CVE authority** (vendor PSIRT / per-CVE advisory / CSAF structured fields / the discloser's per-vulnerability page) — a roundup is never sufficient. Never cite or rely on cveawg/NVD/MITRE API endpoints as a citation (reading one to check an id is fine).
2. KEV and exploitation claims (read `tools/fetch_source.py cisa-kev` for the catalogue, incl. the `knownRansomwareCampaignUse` flag), version boundaries, affected/patched products, victim statements, attribution, and every `evidence[]` quote **verbatim** against its cited URL (contiguous substring; translated quotes on `original:`).
3. **Publisher revisions since the entry's last record.** Vendors in this window revised advisories repeatedly (the PHP2Shell and Brotli vendor waves especially: hotfixes released, fixed versions changed, products added; Danfoss and Publica incident statements; Ivanti, Cisco, Barracuda and SonicWall advisories). Where the vendor's current page says something the entry no longer matches (a fix now released, a new affected product, exploitation now confirmed), that is a finding (`imprecision` or `factual-error`, with the revision date).
4. Every `techniques[]` id **active in the pinned `attack/enterprise-attack.json`** — mechanical ground truth, e.g. `python3 tools/attack_data.py --info` or a jq/python lookup on the file; never memory. Every id must name a behaviour the body describes and a source supports.
5. `classification` (Admiralty letter/number) consistent with the sourcing actually present; `verification` / `sourcing_note` honest; no IOCs; frontmatter ⇔ body agreement.
6. **Changelog and supersession:** each section's claims against its cited sources; each record's `summary` against its section; the main analysis, title, headline, summary, labelled lines, `actions[]` and `immediate_action` against the entry's own **newest** section (a statement the newest section disproves is a factual error); `updated_at` mirrors the last non-internal `update` record.
7. Priority against the bars in `prompts/cti-run.md` Phase 4 (`critical`: in-window, exploited now or mass exploitation imminent, time-critical to the hour/day; `high`: plausible constituency exposure AND a decision within 7 days beyond the regular cycle AND in-window development; doubt → notable). Report miscalibration as F16 with the specific bar element that fails — both directions.
8. Note (do not count as truth defects) main analyses over 550 words (1,100 for a deep dive) and headlines over 120 characters.

Named leads from the mechanical cited-page pre-pass (`page-checks.txt`) are listed in your spawn message where your batch owns one: decide each (a real non-verbatim quote or a mis-bound CVE is a defect; a page edited since publication is noted and left).

**Return:** write `work/2026-11-08T1309Z-audit/truth-<BATCH>.yaml`:

```yaml
batch: <BATCH>
model: <your Model line value>
timestamps: {started: ..., ended: ...}
entries:
  - entry: <YYYY-MM-DD/slug>
    verdict: clean | imprecision | factual-error
    findings:            # empty list when clean
      - code: F3|F4|F5|F13|F14|F16|F17|...
        claim_id: <ledger id or null>
        where: <field / sentence / section at>
        defect: <what the entry says>
        ground_truth: <what the source says, verbatim passage where possible>
        ground_truth_url: <the specific URL you fetched>
        fix: <the minimal correction>
    length_note: <words / headline chars when over bound, else null>
```

Then `truth-<BATCH>.ended_at`, then return a compact summary only: `**Model:**`, `**Timestamps:**`, `**Verdict counts:** clean N · imprecision N · factual-error N`, and one line per non-clean entry. Read-only on the store: never edit entries or state. No time limit; nobody answers questions mid-run. Do not write out your internal reasoning in the return.
