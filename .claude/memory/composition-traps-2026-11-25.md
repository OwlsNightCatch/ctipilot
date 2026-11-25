---
name: composition-traps-2026-11-25
description: Three composition traps that cost verifier iterations on the 2026-11-25 fire — the 550-word bound counts link text, per-clause citations must match the page that carries the fact, parallel deep-read agents share a scratchpad
type: project
---

# Composition traps (2026-11-25 intel fire)

- **The 550-word main-analysis bound counts link text.** `check_run.py` keeps the `[Publisher, date]` text of every inline citation as words, so a fact-dense paragraph that cites one source four times is ~8 words over. Cite once per paragraph when the paragraph rests on one source; measure with the gate's own method (`re.sub(r"\s+"," ", MD_LINK_TEXT_RE.sub(r"\1", main))`). A changelog rewrite of an entry already at 548 words must cut as many words as it adds, so draft the replacement in a scratch file and count before applying it.
- **Re-point a citation to the page that carries the fact.** Iteration 1 found 11 F3s of one shape: a GeoServer project post cited for the reporter's "default installation" claim, a GHSA cited for details that sit in a sibling GHSA, a CISA alert cited for wording that is the KEV catalogue record's, a Q&A cited for Telco builds that sit in a KB. When a deep read returns a claim table, cite the table's URL for that row, not the entry's primary.
- **Parallel `cti-research` deep reads share one scratchpad directory**: two agents overwrote each other's generator script. Give each deep-read spawn its own `work/<run-id>/<tag>/` scratch directory.
- Other recurring defects the verifier caught: an update that rewrites a paragraph and drops detail that the summary and `actions[]` still claim (restore it, never leave the summary asserting what the body no longer says); a title/headline that overstates ("Metasploit module public" for an open, unmerged pull request); a second entry in the window carrying the same action text (keep the action on the entry that covers both cases).
