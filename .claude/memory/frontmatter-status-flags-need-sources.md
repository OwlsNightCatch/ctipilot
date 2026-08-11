# Structured metadata is a claim too — `cves[].status` flags need a source like any sentence

**The defect (2026-08-11, `2026-08-11T0411Z-intel`).** The Gunra deep dive shipped both its
FortiOS CVE records with `status: [exploited, cisa-kev, patch-available]`. The `exploited` flag was
carried by the cited joint advisory. **`cisa-kev` was not carried by anything.** The advisory's only
catalogue-adjacent text is generic `#StopRansomware` remediation boilerplate ("Prioritize patching
known exploited vulnerabilities … and the CVEs in this advisory") plus a footer navigation link to
the catalogue — neither asserts catalogue membership for those two identifiers, and the
corroborating research never mentions the catalogue at all.

The flag was almost certainly true in the world. That is exactly why it is a PD-1 violation: it came
from knowing the CVEs rather than from reading a source in this run.

## Why the loop nearly missed it

Iteration 1 (Opus) read the entries and cleared the deep dive on truth entirely — all four of its
findings were prose-citation defects in a different entry. Iteration 2 (Sonnet) caught it only
because it read the whole 631-line advisory end to end and checked the structured block against it.

**Prose defects announce themselves; a wrong enum value in frontmatter does not.** A verification
pass that reads for narrative plausibility will slide straight past a four-token YAML list. The
catalogue flag also has no sentence anywhere in the entry depending on it, so removing it left no
orphan — which is the tell that nothing had ever justified it.

## The rule

Every value in a structured field is a claim and needs the same sourcing as a clause:

- `cves[].status` — each flag individually. `cisa-kev` needs a source stating *this id* is listed.
  `exploited` needs a source stating exploitation. A ransomware advisory naming a CVE as an actor's
  initial-access vector supports `exploited`; it supports nothing about the catalogue.
- `cves[].cvss` / `affected` / `fixed` — from the record that owns them (see
  `csaf-msrc-transcription.md`).
- `techniques[]` — every id names a behavior the body describes and a source supports.
- `classification` — the credibility number follows corroboration actually found this run.

**Mechanical check before commit:** for each status flag, name the source sentence that carries it.
If the answer is "everyone knows that CVE is in KEV", drop the flag. The KEV catalogue is fetchable
in-run via `fetch_source.py cisa-kev` — either source it properly or leave it out. Note that the
catalogue URL itself is a listing page and is FAIL-blocked as a `sources[]` entry, so a KEV claim
usually has to ride on an advisory that states the listing.

## Related

- A KEV *listing* that flips a store-covered CVE from not-confirmed-exploited to confirmed-exploited
  is a material delta worth an `update_of` (PD-13) — but only when a source this run says so.
- `verifier-attribution-defects.md` — the prose-side sibling of this defect class.
- Aim at least one verifier iteration at the structured blocks specifically, not just the prose.
