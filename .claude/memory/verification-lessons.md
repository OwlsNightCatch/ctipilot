---
name: verification-lessons
description: Consolidated Phase 5.7 / composition verification lessons — how to aim iterations, test findings before applying, and the recurring defect classes (inverted claims, unsourced status flags, citation-metadata errors, inherited sentences)
type: project
---

# Verification lessons (consolidated 2026-08-28 from four files + the retired weekly's traps)

## Aiming the loop

- **Iteration 1 catches content defects; iterations 3+ find almost only citation-metadata defects** (publication date vs event date; a tracker's relay voice attributed to the victim; a quote labelled with the wrong speaker; run-record prose contradicting its own frontmatter). Aim late iterations explicitly at per-clause citation labels and re-derive every count/date in the notes from the structured block (2026-08-02: 8 iterations, 13 truth findings, zero rejected).
- **Leave ≥1 iteration completely unframed.** Framing buys depth on the axes you suspect and costs the ones you don't — the unframed pass on 2026-08-07 found an inverted hardening claim and an off-by-one date two framed passes had cleared. After a NEEDS_FIXES, give the next iteration the deltas block; a confirmation pass after a CLEAN gets nothing but the fact of the CLEAN.
- **Aim ≥1 iteration at the structured blocks, not the prose.** A wrong enum in frontmatter announces nothing (2026-08-11: `cisa-kev` flags no cited source asserted; the tell — no body sentence depended on the flag).
- A single CLEAN is a hypothesis: two CLEANs were overturned by the next cold pass on one run alone. Budget ≥2 iterations for a CLEAN publish.

## Findings are evidence, not verdicts — test before applying

- **Verifiers false-positive at a material rate, most confidently on non-English text** (2026-08-05: 3 of 6 iteration-2 truth findings wrong, incl. a verbatim quote called "wholly fabricated"; 2026-08-06: a vendor's own standfirst figure called an invented sum, "verified by full-page fetch").
- Re-test every finding that changes a claim, quote or attribution against a fresh fetch (`grep -F` on the cached primary under `work/<run-id>/src/`) BEFORE applying. **Findings that merely ADD a caveat get accepted uncritically and inject unsourced claims** — one did, and the next iteration caught it as a new defect. Invert the instinct: scrutinise the additive ones.
- Record rebuttals in the run record with evidence, count them in the residual. A verifier's "no action recommended" is advice, not a ruling.
- Counterweight: on 2026-08-07 all 26 findings' truth class held — do not train reflexive scepticism; polarity findings on informal sources have run near 100% true here.
- Withholding detection depth as if it were an IOC is itself a defect: a vendor's generation-pattern hunt rule is not an indicator list — carry the pattern, withhold example hostnames.

## Inverted claims — fluent, cited, backwards

Informal prose with adjacent controls/researchers/bugs is the high-risk shape (2026-08-08: "SIP does not block" where the post says the bug does NOT bypass SIP; "read and write as root" for a download-only bug; a version number appearing 0 times on the page). **`grep` every control name, privilege level and version string on the page before writing the sentence.** If a number is in your draft, it must be grep-able on the page.

## Structured metadata is a claim too

Every value in a structured field needs a source like a sentence: each `cves[].status` flag individually (`cisa-kev` needs a source stating *this id* is listed — "everyone knows" is PD-1 recall, drop it); `techniques[]` ids name behaviors the body describes AND a source supports; credibility follows corroboration actually found this run. Before commit, name the source sentence for every status flag.

## Quote fidelity

- Verify quotes against the live page, never against the findings YAML quoting it. Strip HTML tags to the **empty string**, never a space (a space makes a cross-element splice look contiguous).
- Extraction shape is a trap: NBSP (`U+00A0`) in the source is part of the quote; whitespace-normalising before checking produces a "quote" that exists nowhere; PDF extractions break mid-word — quote short spans that genuinely hit, or paraphrase.
- Full-sweep method that works: fetch every cited primary to `work/<run-id>/src-*`, substring-test every `evidence[]` quote after Unicode punctuation folding.

## Composing from entries instead of fresh fetches (an audit's records, Background paragraphs)

- **A lifted sentence brings the prose but not the `sources[]` record** — lift the source record in the same motion, or the clause lands on whatever citation was already there (a CVE called exploited on the strength of Adobe's "not aware of any exploits" bulletin; the real observer uncited).
- **Partial remediation:** after every fix, grep the same fact across title/headline/summary/body/evidence/cves — three iterations in one run each caught an earlier fix applied to half an entry.
- **Re-derive every numeral and absolute** ("every", "all", "first") from the body's own enumeration immediately before commit.
- One citation per clause; a national-CERT relay carries less than the vendor bulletin (cite the relay for reach + timing only); a slug is not a dateline (read the page's own date field — BSI `260601` = 6 January); vendor blog URLs mutate in place (re-fetch before re-quoting); when a source has a blog + PDF, check which artifact carries the clause.
- **Drop rather than half-source:** an attribution no fetched source connects is not fixable by adding a plausible link.
