**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-02T06:51:30Z · ended_at=2026-09-02T07:00:06Z · duration_seconds=516

## Verification report — 2026-09-02T0411Z-intel (iteration 7)

Confirmation pass. Read cold, as instructed — no anchoring on iteration 6's CLEAN. Fetched every inline source URL on all three new entries and every source added by the four updated entries' 2026-09-02 changelog sections (Kaspersky Securelist primary, The Record, Republik, heise (E-ID), Inside IT, 9to5Mac, Reuters/Free Malaysia Today, heise (Dropbox), NCSC-CH posts 12902/12901, WatchGuard PSIRT CVE-2026-19318/CVE-2026-78174, The Hacker News, SecurityWeek, Inside Paradeplatz, Exxpress, NZZ (re-fetched for the new Swiss-register-architecture paragraph), ZATAZ Cybernox article). Cross-checked every quote, quantifier, date, version range and named entity against the fetched page text. Ran `tools/check_run.py 2026-09-02T0411Z-intel` and confirmed 44 pass · 2 warn (both pre-acknowledged, re-checked, still correct) · 1 fail (the confirmation-pass gate itself). Verified the run record's coverage-backlog claims against `state/coverage_backlog.md` on disk — both Struck rows and all seven dated 2026-09-02 notes are genuinely present, matching the record's narrative. Confirmed the `screening-serpens` dedup flag against `prior_coverage.json`: the 2026-08-28 TWOSTROKE entry (Group-IB, DLL search-order hijacking, C++) and this run's NodeRabbit/PollCat entry (Kaspersky, Node.js/JavaScript, npm-package delivery) are genuinely distinct findings about the same actor — correct not to fold.

Nearly everything held up. One residual defect survived six prior remediation rounds because it sits in a frontmatter field none of the prior findings' fixes touched directly.

### Unsupported / hallucinated facts

**#1.** `2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats` — `sourcing_note` field states: "The Record's article restates Kaspersky's own investigation and attribution (\"tracked by ... Kaspersky as Mirage Kitten\") rather than independently corroborating it — a press write-up of one lab's research is not a second assessor, **even where it adds extra target-country names**." I fetched `https://therecord.media/iranian-cyber-spies-target-aviation-fintech-new-malware` (`tools/fetch_source.py extract`) in full and grepped the extracted body for every country name: the article names only "Egypt, Ethiopia and Afghanistan" — twice, both times the identical three-country list Kaspersky's own Securelist post gives ("victims in fintech, aviation and aerospace sectors across the Middle East and Africa – specifically, in Egypt, Ethiopia and Afghanistan"). No other country appears anywhere in the fetched Record body. The clause "even where it adds extra target-country names" is therefore false of the source it describes — The Record does not add any country beyond Kaspersky's own three. This is a residual fragment of the exact hallucination iteration 1 found and fixed in the entry's *body* ("a claim that it 'adds Jordan, Tanzania, Pakistan and Burkina Faso' appears nowhere in the cited source... Removed the fabricated country list"); the fix touched the body paragraph but left a paraphrastic trace of the same false premise sitting in the `sourcing_note` field, which none of iterations 2–6's findings happened to re-examine because their own findings were elsewhere in the entry. Fix: drop the clause "even where it adds extra target-country names" (or replace with an accurate observation — The Record adds no facts beyond what Kaspersky's own post already states, including on victim countries).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats"
  url_or_quote: "sourcing_note: '...a press write-up of one lab's research is not a second assessor, even where it adds extra target-country names.'"
  summary: "The Record's article (fetched in full) names only Egypt, Ethiopia and Afghanistan — the same three countries Kaspersky's own post names — nowhere else; it adds no target-country names beyond Kaspersky's list. The clause is a residual trace of the country-list hallucination iteration 1 fixed in the entry body but did not clear from this frontmatter field."
```
