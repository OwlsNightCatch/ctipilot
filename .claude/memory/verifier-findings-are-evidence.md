---
name: Verifier findings are evidence, not verdicts
description: Phase 5.7 findings must be tested before they are applied — verifiers produce false positives, and applying one uncritically injects a defect into verified work
type: project
---

# Verifier findings are evidence, not verdicts

Established on the 2026-08-05 intel run (`2026-08-05T0412Z-intel`), which ran four verification
iterations and had verifiers contradict each other on the same quotations.

## The core fact

**Verifiers produce false positives at a material rate, and they do it most confidently on
non-English source text.** On 2026-08-05, iteration 2 (Sonnet) returned six truth findings. Three
were wrong:

- It called two German quotations from the Swiss Federal Council release spliced or altered
  ("changes 'mehreren' to '200'"). Both are exact substrings of the release's **lead paragraph**.
  The page states each fact twice — once in the lead, once at greater length in the body — and the
  verifier compared against the body occurrence.
- It called a VBS quotation "wholly fabricated", asserting the word `Rechtsverletzung` appears
  nowhere on the page and that it had fetched the page in full. The word and the whole clause are
  present verbatim. Its fetch most likely returned a partial or unhydrated render.

Iteration 3 (Opus) re-fetched both pages and upheld all three rebuttals.

## The trap that actually cost this run a defect

The asymmetry is the dangerous part. That run tested every finding that **contradicted its own
work** — and accepted, without testing, the two findings that merely **added** something. One of
those (iteration 2's F9, "Sophos's prose inverts the CVE-2026-18556 / -18577 relationship") was
false. Applying it wrote a contradiction claim into a `sourcing_note` that did not exist in the
sources, and iteration 3 had to catch it as a fresh F1 defect.

**A finding that flatters your scepticism gets scrutinised; a finding that just asks you to add a
caveat sails through. Invert that instinct — the additive findings are exactly the ones that
introduce unsourced claims.**

## Working rule

1. Every finding that changes a factual claim, a quotation, or an attribution gets re-tested
   against a freshly fetched copy of the cited page before it is applied. Cheap: one fetch, one
   `grep -F`.
2. Record rejections in the run record with the evidence, in the same detail as acceptances. The
   rebuttals are part of the verification record, not an omission from it.
3. Where a verifier and the run disagree, the next iteration adjudicates explicitly — put the
   disputed items in the spawn message and ask for a ruling. Iteration 3 settling three disputes in
   one pass is cheaper than carrying them to the cap.
4. Never write "the verifier said so" into an entry. The source said so, or it does not ship.

## Corollary for quote checks

Verify quotes against the page, not against the findings YAML that quotes the page. And strip HTML
tags to the **empty string**, never to a space: stripping to a space silently joins two adjacent
block elements and makes a cross-element splice look contiguous. On this run that exact caveat is
what surfaced a Liechtenstein quotation spanning two separate block elements (fixed by splitting it
into two `evidence[]` records) — and stripping to a space would have hidden it.

Full sweep method that ended this run's quote defects: fetch every cited primary, save under
`work/<run-id>/src-*`, then substring-test **every** `evidence[]` quote in the run after whitespace
normalisation and Unicode punctuation folding (curly quotes, en/em dashes). 40/40 verified; five
defects found that three verifier iterations had individually missed.
