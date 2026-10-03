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
