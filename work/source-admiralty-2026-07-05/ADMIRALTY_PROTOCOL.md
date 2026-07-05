# Source reliability re-classification — NATO Admiralty code (2026-07-05)

You are re-classifying the reliability of CTI sources for an autonomous threat-intel
pipeline serving a Swiss federal SOC (Tier 2/3 IR, threat hunters, detection engineers).
The pipeline is migrating source `reliability` from the old `HIGH`/`MEDIUM`/`LOW` scale to
the **NATO / Admiralty source-reliability code (letters A–F)**. Your job: **investigate each
source in your assigned batch in detail** — visit its page, see what it actually publishes,
work out *who is behind it* and *where its information originates* (original reporting vs.
re-reporting) — and assign the correct Admiralty **reliability letter**, plus recommend any
status change. You do **not** edit `sources/sources.json`; you only fetch, assess, and
**write one results JSON file** plus return a short summary.

Today's date is **2026-07-05**. "Recent" means within the last ~30 days.

## The Admiralty reliability scale (letters A–F) — assign ONE per source

The letter rates the **source itself** (its authority, track record and originality), NOT any
single story. It is independent of the credibility of a given item.

- **A — Completely reliable.** Authoritative *primary/original* source with essentially no
  history of error and direct authority over what it reports. Reserve for: national CERTs /
  government cybersecurity authorities publishing their own advisories for their own
  jurisdiction (NCSC-CH/GovCERT.ch, CISA, BSI/CERT-Bund, ANSSI/CERT-FR, CERT-EU, ENISA,
  NCSC-NL, NCSC-UK, CCN-CERT, national CSIRTs), and first-party vendor PSIRTs publishing
  advisories for their *own* products (Microsoft MSRC, Cisco, Fortinet, Ivanti, Palo Alto,
  etc.). These are the ground truth for their own disclosures.
- **B — Usually reliable.** Strong *original* research or reporting with consistent editorial
  standards and only minor, infrequent issues. Most reputable vendor/independent threat-research
  labs publishing their own telemetry and analysis (Mandiant, Talos, Unit 42, ESET, Kaspersky
  GReAT, Microsoft MSTIC, Sekoia, Volexity, etc.); established security journalism that does its
  own original reporting and correction (e.g. Krebs, The Record, BleepingComputer for their
  original scoops). Large, well-known news outlets with rigorous editorial process and
  multi-source corroboration also sit here.
- **C — Fairly reliable.** Useful but with some doubt about consistency, OR sources that
  mostly *aggregate/re-report* others' work rather than originate it: news aggregators, general
  tech press, smaller/newer research blogs with a short track record, community trackers with
  reasonable methodology. Corroboration recommended before acting.
- **D — Not usually reliable.** Significant doubt: low-signal aggregators, sources that
  frequently carry unverified or promotional claims but occasionally valid intelligence.
- **E — Unreliable.** History of invalid information, propaganda, or fabrication. (Rare in a
  curated list — if you land here, also recommend `demoted`.)
- **F — Reliability cannot be judged.** No track record to evaluate yet — brand-new source,
  or one you genuinely cannot assess. Natural fit for a `candidate` with no fetch history.

### Weighting rules (apply these — they are the point of this exercise)

1. **Original/primary beats aggregator.** A source that *originates* intelligence (does the
   research, owns the advisory, has first-hand telemetry) outranks one that re-reports it.
   Pure aggregators/republishers cap at **C** unless they add substantial original reporting.
2. **First-party authority = A.** A CERT for its own jurisdiction, or a vendor PSIRT for its
   own products, is A for those disclosures — they are the definitive source.
3. **Corroboration lifts reliability.** A large, well-known news outlet whose editorial
   process cross-checks multiple sources is more reliable than a lone blog — such outlets earn
   **B** even though they are not "primary", precisely because their process corroborates.
4. **Don't inflate.** A is rare and reserved for authoritative first-party/primary sources.
   Most good research labs are B. Most journalism/aggregation is B (original, corroborated) or
   C (re-reporting). When genuinely unsure between two letters, pick the **lower** and say why.

## Per-source procedure (do this for EVERY source in your batch)

1. **Fetch the source** using its documented `fetch_method` and the recipe in `notes_tail`.
   - `webfetch` → WebFetch the `url` with the outbound-links template below.
   - `rss` → `python3 tools/fetch_source.py feed <rss_url or url> 5`.
   - `bridge`/`api` → `python3 tools/fetch_source.py url <url>` or the documented subcommand
     named in `notes_tail` (e.g. `cisa-kev`, `ncsc-csh recent`, `ncsc-nl csaf <ID>`).
   - `blocked` → still retest with `url <url>` then `wayback <url>`.
   - WebFetch template (ALWAYS use it so URLs survive the summariser):
     > "List this page's main content. Return: (1) page title; (2) whether it shows a list of
     > dated articles/advisories or only navigation/marketing; (3) the 3 most recent item
     > titles WITH publication dates AND full absolute URLs (Outbound links — include every
     > href verbatim, do not summarise them away); (4) one sentence on what security content
     > this source publishes and whether it is ORIGINAL reporting/research or re-reporting."
2. **Investigate provenance.** From what you fetched (plus your own knowledge of the publisher),
   determine: **who runs it** (government / vendor / independent lab / news outlet / individual /
   community), and **where its content originates** (first-hand advisory or telemetry vs.
   summarising others). One `WebSearch` is fine to confirm ownership/track record if unclear.
3. **Assign the Admiralty letter** per the scale + weighting rules above. Write a one-sentence
   justification grounded in what you actually observed (provenance + track record), not a guess.
4. **Recommend status** (`active` | `candidate` | `demoted`):
   - Promote `candidate` → `active` if it is live, drillable, clearly relevant, and its notes
     show a track record of successful fetches (recent `last_successful_fetch`,
     `consecutive_failures` 0, positive prior audit).
   - Keep `candidate` if live but genuinely unproven / very new / niche.
   - Recommend `demoted` only if NO method yields drillable relevant content (dead host, 404,
     removed blog, SPA with no feed/API/wayback). A UA-403 that the bridge defeats is NOT a
     demotion.
5. **Never fabricate** a date, title, or URL. If you didn't fetch it, say `null` /
   `"not verified"`. Be terse but concrete. ~2 calls for a healthy source, up to ~6 for a
   failing one; if the first method + a drill works, stop and move on.

## Output — TWO things

**(A) Write** `work/source-admiralty-2026-07-05/results/batch-<NN>.json` (EXACT number from your
input filename) — a JSON array, one object per source:

```json
[
  {
    "id": "source-id",
    "publisher": "…",
    "provenance": "who runs it + where content originates (e.g. 'independent vendor threat-research lab, first-hand telemetry')",
    "origin_type": "primary-authority | vendor-psirt | research-lab | original-journalism | aggregator | community-tracker | discovery | other",
    "live": true,
    "reliability_current": "HIGH",
    "recommended_admiralty": "A",
    "admiralty_rationale": "one sentence grounded in observed provenance + track record",
    "status_current": "candidate",
    "recommended_status": "active",
    "observed_recent": {"title": "…", "date": "2026-07-01", "url": "https://…"},
    "attempts": ["feed … -> 200, 5 dated items", "drill … -> substantive"],
    "notes_for_operator": "2026-07-05 admiralty audit: <letter> — <one-line justification + any status change>."
  }
]
```

**(B) Return a short summary** in your final message: one line per source —
`id: <origin_type> reliability <HIGH/MED/LOW>→<A–F> status <cur>→<rec> — <1-line why>`.
Then 2–3 lines on any dead/blocked sources and any A/E assignments (justify every A and E).

## Hard rules
- Do NOT edit `sources/sources.json` or any file except your `results/batch-<NN>.json`.
- Everything you can read is fair game — there is no TLP filter in this pipeline.
- Stay within your batch. Finish every source — partial is worse than terse.
- If `tools/fetch_source.py` errors on a subcommand, fall back to `url <URL>`.
