**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-27T04:57:09Z · ended_at=2026-09-27T05:06:20Z · duration_seconds=551

## Verification report — 2026-09-27T0404Z-intel (iteration 1)

This is the first verification pass on this run (no prior-iteration deltas). All 3 new entries, all 5 updated entries (with their `git diff` against `HEAD`), the run record, `prior_coverage.json` and `entities/registry.yaml` were read in full. Every inline source URL cited in the scope below was fetched with `tools/fetch_source.py extract` (jina fallback where the direct/trafilatura rung failed) and cross-checked against the entry's claims, quotes and `evidence[]`/`original:` fields.

### Unsupported / hallucinated facts

None found. Every named CVE, actor, date, quantity and technical claim I checked (Mandiant/GTIG's SIDEEYE/Neo-reGeorg/WAF-bypass technical detail, the Pentagon DMDC letter's contents, the Flink/LPG Group mechanics, the Qbusoft/Medyc SQLi chain, the ACSC advisory quotes) traces cleanly to the cited source's own text.

### Citation does not support the claim

**#1 (moderate confidence, truth)** `entries/2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor.md` — body states: "the outlet states plainly it could not confirm either the photo count or that photographs were taken at all" (citing Zaufana Trzecia Strona, 2026-09-25). ZTS's actual text at that URL reads: "Jeśli chodzi o rzekomo wykradzione zdjęcia, to według naszych informacji mogą one przedstawiać pacjentów w negliżu - jednak nie udało nam się potwierdzić, że faktycznie taka liczba zdjęć trafiła w ręce sprawców" — "we were unable to confirm that indeed that number of photos ended up in the perpetrators' hands." ZTS hedges only the **count** (8 million); it does not hedge whether any photos were exfiltrated at all — the entry's "or that photographs were taken at all" clause overstates the source's own caveat. Fix: narrow the clause to the count, or cite additional support for doubting exfiltration occurred at all.

### Claims missing inline citation

**#1 (moderate confidence, editorial)** `entries/2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor.md`, body paragraph 2: "A second ZTS source states the stolen database was the company's complete records reaching back roughly seven years, held on Microsoft Azure infrastructure, unlike MyDr's AWS-hosted environment." This sentence carries no inline citation of its own; the paragraph's other citations attach to earlier clauses (the same-actor quote and the Gawkowski quote). The underlying facts do appear in the 2026-09-25 ZTS post ("Inne nasze źródło potwierdziło..." / "Medyc korzysta z infrastruktury Azure, podczas gdy MyDr jest klientem AWS") — content is accurate, but the sentence itself needs its own `([Zaufana Trzecia Strona, 2026-09-25](...))` citation per check 3.

### Surface contradiction

**#1 (low confidence, editorial)** `entries/2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach.md` — the entry states the collective ransom target as "100 ETH (roughly EUR 230,000)," a figure that traces to heise ("Das entspricht derzeit etwa 230.000 Euro"). NL Times, cited in the same sentence, gives the same 100 ETH as "just shy of 237,300 euros" — a ~3% difference, most likely simple exchange-rate timing drift between the two outlets' publication times rather than a real dispute, but the entry merges both citations onto one EUR figure without acknowledging the two sources actually state two different euro equivalents.

### Needs more research

**#1 (moderate confidence, editorial)** `entries/2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach.md` — the entry's only quantification of scale is "at least 10,000 customers and employees in the Netherlands received ransom notes." Its own cited primary, NL Times, opens with a materially larger and directly relevant figure the entry never uses: "Cybercriminals claimed on Friday that they managed to steal personal information pertaining to a **million** customers of rapid grocery delivery service Flink, as well as the data of **13,000** workers." This is the attackers' own claimed total breach scope (as opposed to the subset who received extortion emails) and is squarely within the completeness a defender needs to size the incident; its total absence from the entry (summary and body alike) understates the story's scale. Suggested fix: add a sentence citing NL Times for the claimed 1M-customer/13K-worker scope, flagged as an unconfirmed criminal claim exactly as the entry already does for other unverified figures.

### Editorial / less-is-more flags (advisory)

**#1 (low confidence, advisory)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md` — the 2026-09-27T04:35:00Z changelog record's `fields:` list includes `tags`, but `git diff HEAD` shows no change to the `tags:` block in this run (only `sectors`, `techniques`, `affected_products`, etc. actually changed). Minor over-declaration; harmless to readers, but the record over-states what it touched.

### Single-source items missing [SINGLE-SOURCE] flag

None — every entry in scope carries `verification: multi-source` with a `sourcing_note` that is consistent with what I found on fetching the cited sources (including the Qbusoft entry's explicit hedge that the same-actor attribution itself is single-source-ZTS even though the entry overall is multi-source).

### Action-item discipline

**#1 (high confidence, editorial)** `entries/2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access.md` — `actions[]` (unchanged by this run; not named in the 2026-09-27 record's `fields:`) still carries: `"**Block perimeter access to `/PSEMHUB/*` on Oracle PeopleSoft** and treat any externally-reachable Environment Management Hub as compromised pending forensic review (CVE-2026-35273)."` This action is now **directly contradicted by this run's own new content**: the same entry's new `immediate_action` states "a WAF rule alone no longer stops this" and the new body section quotes Mandiant/GTIG explaining that UNC6240 now bypasses exactly this class of perimeter/path block via URL-encoding (`/%50SEMHUB/`), i.e. "This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure." An on-shift responder working the action list top-to-bottom would be told to rely on a control the entry's own analysis, published the same run, says no longer works. This is the canonical "actions[] accumulated a superseded action instead of being replaced" case (check 4c / F18): the 2026-09-27 update touched `immediate_action`, `techniques`, `sources`, `evidence`, `sectors`, `affected_products`, `classification` and `body` but left `actions` untouched, so the contradiction survived. Separately, actions #1 and #2 in the same list substantially duplicate each other ("Patch Oracle PeopleSoft out-of-band..." / "Patch internet-exposed Oracle PeopleSoft... now") from earlier accumulated updates — the same class of defect this run's own Metabase update (`entries/2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally.md`) correctly fixed by consolidating five accumulated actions down to two clean ones under its own `fields: [..., actions, ...]` declaration in the same run. Fix: replace all three actions with a version consistent with the "block on normalized path, not literal string" guidance the new body section itself gives, and drop the perimeter-blocking-only action.

### Analytical-link-as-fact / Quantifier without source / Name-collision unflagged

None found with sufficient evidence to flag beyond the items above. Checked in particular and confirmed sourced: Mandiant/GTIG's "a quarter of the threat actor's commands executed as `root` or `NT Authority\SYSTEM`" (verbatim in source); the Metabase/Shipup update's "700+ e-commerce brands" (verbatim "plus de 700 marques" in Cyberattaque.org); the Pentagon entry's "approximately four million" (verbatim in Military Times, correctly hedged as "two people familiar with the incident"); the new registry keys `actor:lpg-group` and `actor:fingerprint` (no collision with any other registry entity of the same name).

### Coverage shape / missed angles

No additional in-window gap identified beyond what the run record's own coverage-backlog notes already surface (DIVD kept open correctly, Familea correctly dropped, Siemens S7 correctly deprioritized). The three new entries' relevance justifications are all explicitly borderline per the run record's own framing (no Swiss/public-sector nexus) but each states a specific, checkable ground per check 5 (TTP-evolution for Flink/LPG Group, PD-11(a) scale + transferable lesson for Pentagon/DMDC, same-actor repeat-targeting + IR-lesson for Qbusoft/Medyc). I did not find these grounds pretextual on inspection, though the Qbusoft inclusion is the thinnest of the three (a second Polish vendor breach, attacker-claimed same actor at `credibility: 2`, three weeks after the same pipeline covered the first one at the same store). Not filed as F7, but flagged for the main agent's own weighing given the "quality over quantity" directive.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 4, advisory: 1)`

- Truth (1): F3 #1 (Qbusoft/Medyc citation overstates ZTS's photo-count hedge).
- Editorial (4): F5 #1 (Qbusoft/Medyc missing inline citation), F9 #1 (Flink ETH/EUR figure merge), F8 #1 (Flink entry omits attacker-claimed 1M-customer/13K-worker scope), F18 #1 (ShinyHunters PeopleSoft entry's `actions[]` retains a perimeter-blocking action this run's own new content contradicts).
- Advisory (1): F11 #1 (ShinyHunters PeopleSoft record over-declares `tags` in `fields:` with no corresponding diff change).

None of these findings individually blocks publication-worthiness of the underlying facts — the truth finding is a narrow overstatement of a hedge, not a hallucination, and the editorial findings are completeness/consistency gaps rather than wrong facts. But they are evidenced, actionable, and in the F18 case materially important (a live action item that contradicts the entry's own new guidance). Recommend remediation before the next CLEAN chain starts. The pipeline's own mechanical gate (`check_run.py`) currently exits with 1 FAIL (`verification.iterations missing or empty` — expected at this stage, pre-dates my verdict being appended to the run record) and 2 WARN (the pre-existing, disclosed `evidence-binding` WARN on the 2026-06-11 entry that predates this run, and a transient non-200 on the live URL check against the Cyberattaque.org URL that I successfully retrieved twice this iteration via the `extract`→jina fallback path) — neither of those two WARNs is a new content defect from this run.
