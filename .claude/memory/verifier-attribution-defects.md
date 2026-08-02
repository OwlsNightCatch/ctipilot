---
name: Verifier loop — attribution defects outlast content defects
description: Where the Phase 5.7 loop actually finds things after iteration 1, and how to aim later iterations
type: project
---

# Verifier loop — attribution defects outlast content defects

## The 2026-08-02 run ran all 8 iterations. Every cold pass overturned the CLEAN before it.

Verdict chain: NEEDS_FIXES(6) → CLEAN → NEEDS_FIXES(1) → CLEAN → NEEDS_FIXES(3) → NEEDS_FIXES(1) → NEEDS_FIXES(2) → CLEAN(cap, `confirmation_waived`). 13 truth findings, **zero rejected** — every one was real when checked against source.

**The distribution is the lesson.** Iteration 1 found the content defects (over-attribution, a dropped precondition, a wrong technique mapping, an uncited superlative). After that, essentially nothing further was wrong with the *content*: quotes, URL liveness, CVE scores and version ranges were re-checked by five separate passes and held every time. Iterations 3–7 found **only attribution-precision and citation-metadata defects**:

- a source cited with the date the vendor *detected* an incident rather than the date the page was *published* (the page's own CMS `publishedOn` field disagreed by 4 days; no visible dateline)
- an observation credited to a victim organisation that its *relaying tracker* had made in its own voice
- a quoted forum reply labelled with the wrong speaker and the wrong date — the other post in the same thread — contradicting the entry's own prose in the same sentence
- published tooling credited to a project when its author says it was his work at a different company
- two claims in the run record's prose that contradicted the run record's own structured fields (a count of nine that the `fetch_failures` block put at eight; a "first reported ~5 h before the window" that the researcher's own post dated 36 h earlier)

## How to aim the loop

1. **Iteration 1 catches content. Later iterations should be pointed at metadata.** From iteration 3 on, tell the verifier explicitly: for every inline citation, check that the publisher label and date match *the specific clause it is attached to and the specific artifact at that URL* — and check every `sources[]` date and every date asserted in registry additions the same way.
2. **Cross-check the run record's prose against its own frontmatter.** Two defects lived in exactly that gap. Counts, dates and status classes stated in the notes must be re-derived from the structured block, not written from memory of it.
3. **A publication date is not the event date.** Get it from the page's own metadata (`datePublished`, `article:published_time`, a CMS payload) — a vendor incident notice will happily narrate a detection date with no dateline anywhere.
4. **A tracker relaying a victim notification is not the victim speaking.** Attribute the tracker's own analysis to the tracker.
5. **Tell late iterations the pattern.** Iterations 7 and 8 were briefed that defects were clustering in attribution metadata; 7 found two more there, and 8 (given the same steer) verified cleanly and cheaply. Naming the residual defect class in the spawn message measurably focuses the pass.

## On the double-CLEAN gate

Two CLEANs were overturned by the next cold pass on this run alone. That is the gate working exactly as designed — a single CLEAN really is a hypothesis. Budget for it: a CLEAN publish takes ≥2 iterations, and on a run with dense citations it can take all 8.
