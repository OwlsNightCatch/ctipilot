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
- **The gate now runs this sweep (v4.13, 2026-09-29):** `check_run.py` `quote-literal` and `citation-cve`, and `--page-checks-since DATE` over a range. They compare letters-and-digits skeletons, so they catch word-level splices, elisions and rewordings but not punctuation or NBSP fidelity, which stays the verifier's job. Measured over 83 verified entries: 6 real published defects (3 Securelist quotes absent from the page, 3 quotes cited to a landing page instead of its PDF), 1 stale page (CISA fixed its own typo), 0 false positives after handling JS shells, JSON escapes and Next.js-embedded article JSON. A page edited after publication shows as a mismatch: judge it, never auto-correct.

## Composing from entries instead of fresh fetches (an audit's records, Background paragraphs)

- **A lifted sentence brings the prose but not the `sources[]` record** — lift the source record in the same motion, or the clause lands on whatever citation was already there (a CVE called exploited on the strength of Adobe's "not aware of any exploits" bulletin; the real observer uncited).
- **Partial remediation:** after every fix, grep the same fact across title/headline/summary/body/evidence/cves — three iterations in one run each caught an earlier fix applied to half an entry.
- **Re-derive every numeral and absolute** ("every", "all", "first") from the body's own enumeration immediately before commit.
- One citation per clause; a national-CERT relay carries less than the vendor bulletin (cite the relay for reach + timing only); a slug is not a dateline (read the page's own date field — BSI `260601` = 6 January); vendor blog URLs mutate in place (re-fetch before re-quoting); when a source has a blog + PDF, check which artifact carries the clause.
- **Drop rather than half-source:** an attribution no fetched source connects is not fixable by adding a plausible link.

## Recap sources: fetch the fuller original they link to

A vendor "webinar recap" / talk-show-style summary post is not the primary — if it says "read the blog for full technical details" and links a fuller write-up (even weeks older), fetch and cite that fuller original as primary; the recap's spoken paraphrase of a technical detail (persistence mechanism, timing, field contents) can diverge from the more rigorous original on the *same* fact (2026-09-21: a recap said NetSupport persisted via "a Run key and a scheduled task"; the linked original said "registers its own COM object" — genuine same-publisher disagreement, not a copying error). Composing straight from the recap risks stale-news-as-new (check 8) on top of the fact-fidelity risk.

## Remediation itself is a defect-injection risk — verify fixes, don't just apply them

Three separate defects this run (2026-09-21) were the *previous* iteration's own fix: restoring a dropped hedge reassigned the hedged tool's specific scope to both tools jointly (dropping the unhedged tool's real action); a date correction moved to the wrong field; a document/cert/payload structural fix mis-attached a still-open detail. Re-verify every remediation against the primary in the *same* pass that applies it (re-read the exact sentence against the source text before moving on), not just at the next cold iteration — the next iteration existing to catch it is not a substitute for checking your own fix.

## `check_run.py`'s IOC scanner only catches hashes/IPv4 — domains need a manual sweep

The mechanical `_scan_iocs()` pattern-matches hashes and routable IPv4 only; a defanged attacker domain (`registry.hashicorp-aws[.]com`) printed in entry prose passes the gate clean while still violating CLAUDE.md's hard "no attacker domains" rule. Before publish, manually grep every entry for `[.]`/bracket-defanged strings and judge each: legitimate infrastructure the malware calls (a public relay directory, an impersonated real service) is fine to name; attacker-registered C2/staging domains are not, however defanged.

## A quote that no longer matches its page is usually news, and the top of the entry drifts (2026-09-29 audit)

Of 15 entries the cited-page backfill caught, only two were the pipeline's own quoting errors (a correction that fixed the prose but left the fabricated sentence in `evidence[]`, and a two-part quote spliced into one). The rest were publishers revising pages after publication, and four of those revisions carried developments the entries had missed: PaperCut's QA'd maintenance releases replacing the emergency patches (19 days unnoticed on a critical entry), Check Point widening a CVE to every Management Server, VenariX attributing Metabase victims to Dire Wolf, ENISA's post-launch FAQ. So triage a `page-revised` quote by reading what the page says NOW, not by patching the quote text. Second pattern, three times in one audit: a changelog record updates its own section, but the title, summary and opening analysis keep the superseded state (Metabase's title said "no CVE was ever assigned" for seven weeks). When writing any record, re-read the title, summary, `immediate_action`, `actions[]` and the first paragraphs against the new state before moving on.

## When a record moves an entry's state, sweep the whole entry for undated present tense (2026-09-29 audit, 8-pass loop)

The 2026-09-29 audit's verifier loop ran to the cap of 8 (21, 34, 37, 12, 4, 7, 12, 13 findings). The class that kept coming back was one paragraph at a time: a correction fixed the summary ("CVE-2026-59310 is exploited"), and the next pass found "nothing here is reported exploited" in the analysis, then in the sourcing note, then in the takeaway. Before the first verifier spawn on any entry whose record changes its state (exploited, fixed, root cause named, PoC public), grep the whole file (title, headline, summary, sourcing_note, actions, cves[] status/affected/fixed, main analysis, every section) for present-tense status words: `no exploitation`, `not reported`, `no fix`, `no patch`, `no workaround`, `withheld`, `not yet`, `has not`, `so far`, `currently`, `until … publishes`. Date each hit to first publication or bring it to the new state. A scan script over the whole scope is cheap; `work/2026-09-29T2134Z-audit/` shows the pattern (scratchpad sweep, iteration 6 remediation).

Two more recurring ones from the same loop:
- **Body quotes mirror evidence quotes.** When an evidence quote is split or translated, the same passage quoted in the body needs the same treatment in the same edit. Five entries were caught one pass late.
- **Folded YAML plus textwrap:** wrap record summaries with `break_on_hyphens=False`, or a hyphenated word lands on a line break and renders as "path- traversal".
- **A fix at the cap is unverified.** Rule 6 publishes on the cap with residual = final truth + editorial. Fixing those findings afterwards is fine and worth doing, but say in the record that no verifier pass read them. Never lower the residual count for them.

## A relay's wording can be the vendor's earlier text: re-read the primary before calling an entry wrong (2026-10-03 intel fire)

The FortiMail entry said Fortinet's second workaround was restricting the management interface; the live Fortinet page said webmail interface, added a WAF option and no longer showed a file table, with its timeline still listing only the initial publication. The first composition framed this as the entry having misread Fortinet ("corrected"), and the verifier showed the previous fire's own claim files had read the page with the management-interface wording and the table. So the page had been revised silently and the relays (BleepingComputer, NCSC-CH) repeated the earlier text. Frame it as "the advisory as read on <date> says X; press says Y", never as the entry's error, and attribute each clause to the source that actually carries it (file table to the outlet that reproduces it). A page's own revision history is not evidence that it has not changed. The check also cost iterations because `quote-literal` only re-runs quotes added by the current run: when you edit an existing entry, re-check every `evidence[]` quote that stays, not just the new ones.

## A reader transport's "Published Time" can be the site build time, not the page's date (2026-10-05 intel fire)

`extract` falling back to the jina reader returned "Published Time: 2 Oct 2026" for a DIVD page whose own JSON-LD `dateModified` was 2026-10-01T14:19+02:00 (a Jekyll site, rebuilt on every push; sibling cases showed the identical header). The `lookback: true` update built on it was composed, verified wrong by iteration 1 and reverted. Before a developing-window or lookback argument rests on a page date, read the page's own `datePublished`/`dateModified` (or its case timeline), not the transport header.


## A revised CERT alert strands its own evidence quotes, and a slice-between-two-phrases edit can eat an entry (2026-10-14 intel fire)

- **A national-CERT alert revised in place (CERTFR-2026-ALE-012 gained products and rewrote its guidance) makes the entry's earlier evidence quotes non-literal and its remediation text stale.** On an update, re-fetch the live page, replace every quote the new text no longer carries, and rewrite the title, Detection and takeaway where the guidance moved; a relay (NCSC.ch) keeps quoting the older sequence, so state the disagreement in the entry or the run notes cannot say it is "carried".
- **Five verifier rounds converged on three repeat shapes:** a date or interview time stated more precisely than the page gives it (a reproduction date, "told X on <date>"), a citation that closes a different clause than the one it supports after a sentence was restructured, and a per-CVE product binding the vendor bulletin only makes at bulletin level. Fix the whole class in the neighbouring clauses in one edit, not the single flagged sentence.
- **A run note that says "carried in the entries" is a claim the verifier checks.** Removing a clause from an entry to fit the word limit silently falsified the note; cut the word count elsewhere or correct the note in the same edit.
- **Editing with `text.index(a):text.index(b)` slices is unsafe.** The first occurrence of the start phrase can sit in the frontmatter `summary` while the end phrase is in the body, so the replace overwrote the middle of the file. Replace short unique phrases with `assert text.count(old) == 1`, and `git diff` or reread the file after any bulk Python edit.
- **A single verifier spawn can be lost to a container restart.** The working tree survives; re-spawn the same iteration with a note that earlier partial files are to be ignored.
- **Pair verifier findings with dispositions in each findings file's own order, never in the order the verifier's summary message lists them.** On 2026-10-11 iteration 3, dispositions built from the message order landed on the wrong findings and the iteration block had to be rewritten.

## Word cap, evidence binding, living pages (2026-10-21 intel fire)

- **The 550-word `entry-shape` cap counts the whole body before the first changelog section, labelled lines included**, with link text only. Count it the same way (strip `[text](url)` to `text`) before writing; trimming only the narrative paragraphs left three entries 40 to 190 words over.
- **`evidence[].publisher` must equal a `sources[].publisher` string** (the check is a near-exact match): a shortened label ("PHP (php.net news archive)") warns even when the source is cited.
- **A living page (vendor statement, tracker, research post updated for days) is ONE `sources[]` record**, dated to the date the cited text states and labelled "updated through <date>"; a second record for the same URL is a verifier advisory each time. Cite publication or last-updated date consistently inline.
- **The verifier re-opens a decline once the fire has edited the same field**: "pre-existing text" does not hold for a `sourcing_note` that the record's `fields` names. Rewrite the whole note to two or three provenance sentences.
- **Entry slugs are capped at 60 characters**; name the file before the first `Write` (six long names had to be renamed after writing).

## Retractions, stale quotes, run-record YAML (2026-10-26 intel fire)

- **A cited page can retract or silently drop what an entry leans on.** Unit 42's PHP2Shell brief withdrew its confirmed-intrusion report two days after the covered entry's summary, immediate action, sourcing note, Detection text, a section and two ATT&CK ids rested on it, and had also dropped a "has seen proof of concept" line a second entry still quoted; only S1 and S3 noticed. When a fire updates a covered entry, re-read the pages its exploitation claims rest on, and grep the live page for every quote of that source across the sibling entries (the `quote-literal` gate only reads entries the fire modifies). A retraction is an `update` (exploitation-status change in the world); the supersession sweep then removes the claim from every field and the techniques it alone supported.
- **Run-record frontmatter lists must be indented under their key.** PyYAML's default dump leaves top-level lists flush-left and the site parser FAILs `run-parse` ("list item inside a mapping block"); dump with a `SafeDumper` subclass whose `increase_indent` forces `indentless=False`.
- **Add a general product blog as a candidate only with `content_scope: general-news`**; `source_health.py` otherwise lists it as `needs-content-fix` (no security vocabulary) the same run.

## Update records on live entries (2026-10-29 intel fire: 8 iterations, cap fail-open)

- **Stamp a changelog record's `at` from `date -u` when you write it; never plan times ahead.** Eight records stamped 05:10 to 05:24Z were written before the clock reached them, and iteration 1 flagged it (F11). Use `tools/entry_record.py add` (it stamps) or take `date -u` first; a later edit that cites a newer fact (a vendor timeline at 05:30Z) needs an `at` after that fact.
- **A tally needs its own citation.** "Seven of 17 at 9.0 or higher" cited to one per-CVE page was F3 twice; cite the listing page for the count and each per-item page for each per-item clause (a group of per-item links is fine). A listing index is not a blocked landing page when the claim is about the listing.
- **Every added fact on an over-limit entry must be paid for in the same edit** (the 550-word cap, and "no growth" on entries already over it): count with `[text](url)` stripped before and after, and declare each removal in the record summary as "Removed from the text: ..." without the pipeline's reason (it reads as pipeline narration, F11).
- **Re-read vendor timelines (Palo Alto JSON, advisory tables) just before the commit**: PAN-OS ETAs were removed at 05:20Z and 05:30Z while the verifier loop ran, which made three entries stale and cost an extra update record and two iterations. When a fix list moves during the run, update every entry that carries it in one pass.
- **A status page has a per-incident permalink in its own HTML** (status.connectwise.com/pages/incident/<id>/<id>); look for it before citing the landing page. An anchored URL to a page that answers 403 on every transport raises a `source-urls` warning, so do not switch to it.
- **Verifier iteration cost**: iterations 5 and 7 returned CLEAN and both confirmations returned NEEDS_FIXES on one-clause wording (a superlative, an exclusivity, an unsourced order). Do the adversarial wording pass (superlatives, "only", "after", "first", causal order) on every clause the run added before the first spawn.
