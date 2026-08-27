# Weekly synthesis — the citation traps that only appear when you compose from entries

> **HISTORICAL context (weekly routine retired 2026-08-27, see [[entry-lifecycle-v4]]) — lessons still live.** No weekly is composed any more, but the same traps bite any prose composed from ENTRIES rather than fresh fetches: an audit's `improvement` / `correction` records, a Background paragraph, a consolidated campaign update. Read "the weekly" below as "whoever re-frames a fact they did not fetch".

The weekly re-frames facts it did not fetch. Iteration 1 of the 2026-W32 verifier found 17 truth
defects and **every one was a sourcing defect, not a content defect** — the analysis was right, the
citation was pointed at the wrong page. Five reusable shapes:

1. **Blog post vs. the PDF underneath it.** CERT Polska's incident write-up carries the narrative;
   the linked PDF report carries the mechanics (device names, protocols, credentials). The operational
   entry cited both; the weekly inherited only the blog URL and attached PDF-only facts to it.
   **Check which of a source's two artefacts actually carries the clause.**
2. **Vendor blog URLs mutate in place.** `n-able.com/blog/n-central-security-update-august-2-2026`
   now serves an *August 6* update; the August 2 quote is simply gone. A quote verified when the
   operational entry was written can fail days later at the same URL. Re-fetch before re-quoting, and
   take the source date from the page's current metadata, not from the slug.
3. **Slugs are not datelines.** `Presse2026/260601_NIS2_BSI-Portal.html` reads as 1 June to an
   English eye; the page's own `Datum` field says `06.01.2026` = **6 January** (DD.MM.YYYY). The
   internal contradiction gave it away — a portal opened in June cannot have 11,388 registrations
   recorded in March. **When a date is load-bearing, read the dateline field, never the URL.**
4. **National-CERT relays carry less than the vendor bulletin.** CERT-FR's WALLIX advisory has the
   affected/fixed versions and nothing else — no CVSS, no "unauthenticated", no scope. Attributing the
   vendor's own severity and scope to the relay is the single most repeatable F3 in this pipeline.
   Cite the relay for what the relay adds (that it reached the constituency, and when).
5. **Two facts, one clause.** Telex.hu describes a Windows domain-admin escalation *and*, separately,
   a virtualisation-environment compromise with a VM count. Merging them into one clause invents a
   claim neither source makes. Same shape as the CVE-labelled-clause rule: one citation per clause.

**Sub-agent figures are candidates, not facts.** Three numbers a research agent attributed to Socket
(package count, poisoned-version count, mean detection latency) were absent from the fetched body.
`grep -F` every number against the saved text before it reaches an entry.

**Drop rather than half-source.** A sentence naming a researcher and a CVE that no fetched source
connects is not fixable by adding a plausible link — the W32 passkey entry lost its fourth disclosure
and was retitled and renamed instead. That is the cheap outcome; a half-sourced attribution is not.

**Gate contradiction to reconcile (CLOSED 2026-08-27 — moot, the weekly and `weekly-vuln-rollup` are retired):** `prompts/weekly-summary.md` Phase 4 said
`weekly-vuln-rollup` entries carry per-CVE `cves[]`, but `check_run.py`'s cross-run dedup FAILs any
non-update entry sharing CVE ids with the last 14 days — which a roll-up does by definition. Three
consecutive weeklies have resolved it the same way: per-CVE trajectory as a **body table**, `cves: []`
in frontmatter. Either the prompt or the check should say so.

## 2026-W33 (7 iterations, 51 findings) — two mechanics behind almost all of it

**1. The inherited sentence brings the prose but not the `sources[]` record.** Iteration 5 named this
explicitly after four of its ten findings turned out to share it: a fact is carried from an operational
entry into a weekly entry, the sentence survives the copy, the source record does not, and the citation
that ends up on the clause is whatever else was already cited there. The sharpest instance — the roll-up's
only basis for listing Adobe Commerce among the newly-confirmed-exploited was cited to Adobe's own
bulletin, which says *"Adobe is not aware of any exploits in the wild"*; the exploitation observation was
Sansec's and Sansec was in no `sources[]` list. Same shape: the SAP rebuild-and-redeploy claim (Onapsis,
uncited), the 12,000-clinic count in the outlook (Notes from Poland, absent), and a MyDr paragraph whose
two figures were each cited to the *other* co-cited outlet. **Fix: when you lift a sentence from an
operational entry, lift its source record in the same motion.** That one habit would have removed roughly a
third of this run's findings.

**2. A fix applied to one half of an entry.** Iterations 4, 6 and 7 each found a defect that was a *partial
remediation* of an earlier one — the four-days correction reached the summary but not the body; the
citation swap moved the figures but not the ministerial title; the seven→six disclosure correction never
reached the "in three of them" count derived from it. After every remediation, grep the same fact across
title, headline, summary, body, `evidence[]` and `cves[]` in that entry before moving on.

**3. Derived counts are the weekly's signature defect.** Four consecutive iterations caught a number in a
title/headline/summary that its own body refuted (ten vs eight CVEs; six vs eight no-fix flaws; "four
inside three days" when macOS was six; "every disclosure" against four counter-examples in the same
entry). Re-derive every numeral and every absolute ("every", "all", "first", "only", "sole") from the
body's own enumeration immediately before commit — none of these came from a source being wrong, all came
from prose written before the list underneath it settled.

**4. Two clocks, one sentence.** The lead entry merged time-to-working-exploit with
time-to-observed-exploitation and produced a wrong interval twice (once corrected, once resurfacing in a
different clause). When an entry's subject *is* an interval, name the endpoints in the sentence.

**5. `cves: []` on weekly roll-up/synthesis entries — now four weeklies running.** The dedup FAIL fires
again every time; the body table plus `cves: []` remains the resolution. This is settled practice, not a
per-run discovery.
