**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-17T00:47:41Z · ended_at=2026-08-17T00:56:52Z · duration_seconds=551
**Self-telemetry:** urls_checked=14 · webfetch_calls=4 · bridge_fetches=14

## Verification report — 2026-08-16T2315Z-weekly (iteration 3)

Read cold. All 15 new entries read end-to-end (frontmatter + body), run record read in full, dedup
context and triage/week-review artefacts consulted. Fourteen distinct source URLs fetched and read in
this iteration (Truesec, ETSI docbox, Check Point Q2, Check Point Lazarus, Dragos Q2, Wiz personal-repos,
BleepingComputer SAP, BleepingComputer SharePoint, ICO/ACRO, Infosecurity ExfilSquad, Cybersecurity Dive
ExfilSquad, SecurityWeek GeoServer, DGFiP press release, Kaspersky Securelist, NCSC-CH hub post 12844).

### The three named fixes — all three verified good

1. **Truesec fabricated-quote fix — HOLDS.** Fetched the live page and literal-substring-checked every
   quoted passage in the entry, not just the repaired one. All four hold verbatim: the "target
   signalling: intimidation, information operations and possible enabling of future targeting by
   sympathizers or recruited proxies" clause, the GRU logistics/shipment-data passage, "The focus is no
   longer limited to intelligence collection, sabotage or disruption of logistics", and the Unit 26165
   attribution sentence. The page's own reference list also matches the sourcing_note exactly (Die Zeit /
   The Insider, CNN, BBC, Euractiv, IntelliNews, CISA/NSA/FBI/NCSC-UK April 2026 joint advisory).
   `article:published_time` is 2026-08-14 — citation date correct.
2. **vuln-status-rollup six→eight — HOLDS.** Headline, summary and body all say eight, and the body's
   enumeration sums to eight: ShieldBreak (1) + three FreeBSD CTL HA primitives (4) + GeoServer (5) +
   three of five NatJack primitives (8).
3. **looking-ahead seven — HOLDS.** Title, summary and bullet header all say seven, the bullet sums to
   seven (ShieldBreak 1 + three FreeBSD 4 + three NatJack 7), and the scoping against the separately
   bulleted GeoServer item is coherent. The two entries now differ by exactly the GeoServer item (8 vs 7),
   which is the correct relationship.

### Unsupported / hallucinated facts

**F1 — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: the headline and summary assert a
three-day universal the entry's own summary contradicts.**
Headline: *"Five products went from disclosure to observed attacks inside three days in W33"*. Summary
opening: *"Across 2026-W33 five unrelated products moved from public disclosure to observed exploitation
in three days or less"*. Four sentences later the same summary says of the fifth: *"A vCenter flaw
disclosed unexploited on 29 July had 361 victim addresses across 47 countries ... with first contact five
days after disclosure."* The body says the same ("first contacting attacker domains on 3 August — five
days later"). The vCenter interval is also entirely outside 2026-W33 (10–16 Aug): disclosure 29 July,
first contact 3 August; only QUIRSO's reporting is in-window. The title is correctly scoped and needs no
change — it says "days or hours" and attaches the seventy-two-hour claim to four named triggers (patch
day, proof-of-concept, binary diff, researcher's post). Fix the headline and the summary's first
sentence.

**F4 — `weekly-w33-compromised-party-was-not-the-notifying-party`: the title, headline and opening
sentence assert a universal that four of the entry's own cases refute.**
Title: *"In every European public-sector and critical-infrastructure disclosure this week the
organisation that was compromised and the organisation that owes the notification were different bodies
— and in the largest, the people affected cannot be told at all"*. Body ¶1: *"in all seven of the week's
European public-sector and critical-infrastructure disclosures, the organisation inside which the
intrusion happened was not the organisation that owes the affected people an answer."*
- **DGFiP**: the intrusion was inside DGFiP and DGFiP notifies. The ministry press release (fetched this
  iteration) states the intrusions rested on *"usurpations d'identifiants d'un agent de la DGFIP et d'un
  tiers habilité"* — a third party on the access path, not the notification path.
- **Żabka**: intrusion inside Żabka's ticketing system via a supplier account; Żabka notifies.
- **Retelit**: compromised body and disclosing body are the same.
- **ACRO**: the ICO notice (fetched this iteration) says the hacker *"gained unauthorised access to
  ACRO's website and content management system (CMS)"*; the third party held patch management. The ICO
  reprimanded ACRO itself.
Only MyDr→~12,000 clinics, CEVA→ten controllers and bol.com actually satisfy the stated claim. The entry
knows this — ¶2 opens *"Where the third party is on the access path rather than the data path..."* — so
the defect is confined to the title/headline/opening, which promise a stronger pattern than the body
delivers. Separately, the title's closing clause *"in the largest, the people affected cannot be told at
all"* is supported by nothing in this entry: the body says the controllers *"know only what they read in
the press"* and that MyDr *"cannot yet say what was taken"* — a scoping failure, not an impossibility of
notification. (The case where receivers genuinely cannot be identified is the NHSBT pager broadcast, which
lives in a different entry.)

**F5 — run record: two wrong counts in the published verification notes.**
*"Every inline citation date in the fourteen entries is either the publication date read from a source
fetched by this run..."* — the run published fifteen entries (`entries_published: 15`), so the
citation-discipline assertion excludes exactly one, and it is the fifteenth, i.e. the entry whose quote
iteration 2 found fabricated. And *"Fourteen entries share entity keys with earlier strategic or
operational entries"* — only twelve entries carry any entities at all; three
(`weekly-w33-disclosure-to-exploitation-interval-collapsed`, `weekly-w33-vuln-status-rollup`,
`weekly-w33-russia-europe-ukraine-defence-supply-chain`) carry `entities: []`.

**F6 — run record: a borderline-drop note asserts a disposition the output does not implement.**
*"a separate incidents-recap entry pairing the ICO/ACRO reprimand with the UNC5537 guilty plea ... Both
are carried inside the sector-patterns entry instead ... Nothing relevant was lost."* Only ACRO is
carried. `UNC5537` appears in no entry of this run — grep over `entries/2026-08-16/` returns the run
record alone. Correct the note to record the guilty plea as a straight drop with its own reason, or carry
it.

### Quantifier without source

**F2 — `weekly-w33-vuln-status-rollup`: "ten" is not what the entry enumerates.**
Headline: *"ten newly exploited or newly catalogued, one exploited with no identifier at all, and eight
flaws with no fix in existence"*; title: *"ten flaws crossed into confirmed exploitation or the federal
catalogue this week"*. The summary's own list of "Newly confirmed exploited or newly KEV-listed" names
eight CVEs. CVE-2026-45659 is explicitly excluded by the summary's own wording (*"gained a
ransomware-campaign-use flag rather than a new exploitation finding"*) and by the body (*"a status
refinement rather than a new finding ... Nothing about its exploitation changed"*); it also cannot have
"crossed into ... the federal catalogue this week" because it has been catalogued since 1 July. The
GeoServer injection is listed by the headline as a *separate* item ("one exploited with no identifier at
all"), so it cannot also sit inside the ten. Under the entry's own accounting the number is eight. This
is the third count in this entry to fail its own enumeration; iteration 1 fixed two→one and six→eight but
the "ten" was never re-derived.

**F3 — `weekly-w33-vuln-status-rollup`: "Four more" followed by five.**
Body ¶2 opens *"Four more moved on the exploitation axis on their own timelines"* and then bolds five:
CVE-2026-20349, CVE-2026-68820, CVE-2026-72898, CVE-2026-59310 and CVE-2026-71362. Correct to "Five
more", and re-derive the headline/title count in the same edit so the two numbers agree.

### Claims missing inline citation

**F7 — `weekly-w33-exfilsquad-claims-validated-status`: the Swiss nexus is uncited.**
*"the same configuration class Switzerland's NCSC put in front of Swiss operators on 4 August, when it
advised on anonymous web roles granted excessive Dataverse table permissions"*, repeated in the Defender
takeaway as *"Switzerland's national authority has already told its constituency so."* No inline
citation, no source record, no `references[]` link. I fetched both cited outlets: neither the
Infosecurity Magazine page nor the Cybersecurity Dive page contains the string "Switzerland" or "NCSC".
The claim is true and already in the store —
`entries/2026-08-05/ncsc-ch-power-pages-dataverse-anonymous-access-advisory.md`, `event_date`
2026-08-04, source `https://security-hub.ncsc.admin.ch/#/posts/12823`. Add the entry id to
`references[]` and/or cite the hub post inline. This matters because it is the entry's only home-region
hook.

### Editorial / less-is-more flags (advisory)

**F8** — `weekly-w33-vuln-status-rollup`: the entry's first `evidence[]` quote (the Defused SAP honeypot
message) is verbatim on
`https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/`
(verified via the bridge this iteration) and that URL is cited inline in the body, but it is absent from
`sources[]` — the only BleepingComputer record there is the SharePoint article. Add it.

**F9** — `weekly-w33-vuln-status-rollup` and `weekly-w33-looking-ahead`: both derive a load-bearing count
from *"three of the five NatJack NAT primitives"*. The claim is accurate —
`entries/2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves.md` records five primitives, two
CVEs, "the other three primitives carry no identifier and no vendor fix at all", and the Linux change as
"not a complete fix" — but that entry appears in neither `references[]`, though both entries reference
every other contributing operational entry. Add it to both.

**F10** — `weekly-w33-russia-europe-ukraine-defence-supply-chain`: the `sourcing_note` contains *"A prior
research sub-agent surfaced this piece and set it aside as a retrospective compilation"*. `sourcing_note`
is rendered verbatim onto the reader-facing entry page (`site/build.py`, `assess-note` block ~line 3852),
so workflow-internal language ships to readers — the explicit style-discipline prohibition. Rephrase
without the pipeline mechanics. The body's opening sentence ("The week's strategic entries are otherwise
about criminal and espionage tradecraft against the estate") is the same register and reads oddly on a
standalone entry page; worth trimming in the same edit, though it breaks no rule.

### What I checked and found clean

- **Every number I could reach against its own authority holds.** Check Point Q2: 2,139 victims / "up
  0.8%" / 33% YoY / 57.6% / 71→93 groups / Qilin 279 at −17% / The Gentlemen +62% to 269 / US share
  50%→42% / the Krybit-and-Gentlemen explanation / the "exploitation window kept narrowing, with AI
  increasingly cited as the accelerant" sentence — all verbatim. Dragos Q2: 1,140 / +12% / 1,020 / 747
  (65%) / 117 / 431 (38%) / Germany 37→68 / the Stage-2 negative finding — all verbatim; the entry's
  derived "eighty-four per cent rise" is correct arithmetic. ICO: "up to 10,920 people", August 2022 to
  March 2023, the patch-ownership finding and the segmentation mitigating factor — all present.
  Infosecurity: 13 organisations, 382.64 GB, 27 million records, DfE and Police National Legal Database,
  "over 10,000 potential Power Pages instances accessible to the public" — all present. DGFiP: 678,000,
  the 12 and 13 August claim dates, the agent-plus-authorised-third-party credential path, and the
  access reviews that did not reveal the theft — all present. Kaspersky: the Nsiproxy quote and "The
  certificate was valid from August 2013 to September 2014" verbatim, `datePublished` 2026-08-14.
  Check Point Lazarus: the FudModule sentence (modulo link-markup whitespace), the telemetry-teardown
  list, "successful targeting observed in Western Europe, including France and Germany", the compromised
  French organisation reused for spear-phishing, and the 28 Jul / 31 Jul / 5 Aug / 11 Aug disclosure
  timeline. BleepingComputer: both Defused quotes verbatim, Shadowserver's "over 8,500" SharePoint
  servers, Rapid7 publishing "on Tuesday". SecurityWeek: the watchTowr quote verbatim and the Wednesday
  (12 August) disclosure. Wiz: "56% of company-impacting secrets lived in employees' personal
  repositories" verbatim, with Forbes AI 50 as the study set. NCSC-CH hub post 12844 exists, is dated
  2026-08-14 and is the GeoServer advisory the entry claims.
- **The `weekly-w33-exfilsquad` "no evidence of a vulnerability being exploited or of ransomware being
  deployed" clause** is NOT in the Infosecurity article, but the citation immediately preceding it is
  Cybersecurity Dive, which carries it verbatim ("Researchers did not find any evidence of a
  vulnerability being exploited or ransomware being deployed"). Adjacency holds; not a finding.
- **The ETSI docbox URL** (`https://docbox.etsi.org/CYBER/EUSR/Open`) resolves and is a directory listing
  — but it is the specific document store carrying the draft filenames the entry cites it for
  (EN_304-617 Browsers, EN_304-618 Password-managers, EN_304-619 Antivirus, EN_304-620
  Virtual-Private-Networks, EN_304-621 Network-Management-Systems visible in the listing), and the entry
  discloses exactly that. Not a generic-URL finding.
- **Priority calibration is right.** Four `high` (the two top stories, the multi-day evasion synthesis,
  the sector-patterns entry, plus the vuln roll-up), the rest `notable`, no `critical`. Nothing in the
  window clears the stop-and-act-now bar, and nothing `notable` plainly clears it either.
- **Classification codes** are within vocabulary and consistent with the run's own applied convention
  (B/1 for cross-sourced synthesis, B/2 or C/2 for single-assessor and single-outlet items, A for the
  two first-party regulator/standards-body items, B/3 for the contradicted water entry). No F17.
- **`actions: []` on all fifteen** is correct for strategic weekly content. No F18.
- **No org-triage blocks, no watchlist flags, no `watchlist` tags** — correct for this profile. No F16.
- **Style**: no IOCs, no vanity metrics, English throughout. The only workflow-language leak is F10.
- **The fifteenth entry earns its place, marginally but genuinely.** It is honestly framed as an
  assessment resting on reporting Truesec cites rather than new telemetry, the sourcing_note is candid
  to the point of self-incrimination, and the operational content — the shipment-data classes, and a
  Triage section that scopes a hunt on account breadth rather than indicators — is real and usable for a
  transport or logistics operator, which is a profiled sector inside the coverage focus. It answers
  W-PD-1's strategic-horizon question. I would not drop it. Its defects are F10 (style) only.
- **Coverage looks complete.** The drop reasoning in the run record and `triage.json` is specific and
  defensible for all three borderline items; the tracked-wave nulls (Joomla, npm/Shai-Hulud, ShinyHunters)
  are recorded as checked results; the source-coverage telemetry accounts for every unreachable source.
  I could not name a further in-window story with a plausible source that this run missed. No F10
  missed-angle finding.

### Verdict

**NEEDS_FIXES (truth: 6, editorial: 1, advisory: 3)**

None of these is a sourcing failure — the run's citation fidelity is, on my independent sample of fourteen
sources, excellent. What survives two iterations is a single recurring failure mode: **derived counts and
universal quantifiers in titles, headlines and summaries that were never re-derived against the body they
sit above.** F1, F2, F3 and F4 are all that same defect in four different entries, and F5 and F6 are the
same thing in the run record. They are cheap to fix and they are exactly what a technical reader notices
first, because each one is refuted by the entry's own next paragraph.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — iteration 3
- code: F1
  category: hallucinated-fact
  section: weekly-top-stories
  item: "weekly-w33-disclosure-to-exploitation-interval-collapsed"
  url_or_quote: "headline: \"Five products went from disclosure to observed attacks inside three days in W33\" / summary: \"Across 2026-W33 five unrelated products moved from public disclosure to observed exploitation in three days or less\" — vs the SAME summary: \"A vCenter flaw disclosed unexploited on 29 July ... with first contact five days after disclosure.\""
  summary: >-
    Headline and summary assert a universal "inside three days" / "three days or less" across all five
    products; the entry's own summary and body state the fifth (CVE-2026-59310, vCenter) at five days
    (disclosed 29 July, first attacker contact 3 August, per The Hacker News quoting QUIRSO — fetched
    this iteration, confirms the 29 July / 3 August pair). The vCenter disclosure-to-exploitation
    interval also falls entirely outside 2026-W33 (10–16 Aug); only its reporting is in-window, so
    "Across 2026-W33 five unrelated products moved from public disclosure to observed exploitation" is
    wrong on two axes for that case. The title ("closed to days or hours ... a patch day, a
    proof-of-concept, a binary diff and a researcher's post each produced attacks within seventy-two
    hours") is correctly scoped to four triggers and does not need changing. Fix the headline and the
    summary's opening sentence to scope the seventy-two-hour claim to the four cases that clear it and
    state the vCenter case as five days, reported in-window.
- code: F2
  category: quantifier-without-source
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup"
  url_or_quote: "headline: \"W33 CVE trajectory — ten newly exploited or newly catalogued, one exploited with no identifier at all, and eight flaws with no fix in existence\"; title: \"ten flaws crossed into confirmed exploitation or the federal catalogue this week\""
  summary: >-
    The "ten" is not supported by the entry's own enumeration. The summary's list of "Newly confirmed
    exploited or newly KEV-listed" names exactly eight CVEs (20349, 68820, 72898, 59310, 55040, 65400,
    58231, 71362). CVE-2026-45659 is explicitly excluded by the summary's own wording ("gained a
    ransomware-campaign-use flag rather than a new exploitation finding") and by the body ("a status
    refinement rather than a new finding ... Nothing about its exploitation changed"), and it did not
    cross into the catalogue this week (catalogued since 1 July), so it fails the title's own
    definition. The GeoServer injection is listed by the headline as a SEPARATE item ("one exploited
    with no identifier at all"), so it cannot also be inside the ten. Under the entry's own accounting
    the number is eight. This is the same defect class iteration 1 fixed for the no-identifier count
    (two→one) and the no-fix count (six→eight); the "ten" was never re-derived.
- code: F3
  category: quantifier-without-source
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup"
  url_or_quote: "body ¶2: \"Four more moved on the exploitation axis on their own timelines.\" — followed by five bolded entries: CVE-2026-20349, CVE-2026-68820, CVE-2026-72898, CVE-2026-59310, CVE-2026-71362"
  summary: >-
    The paragraph announces four and then enumerates five. Adobe Commerce CVE-2026-71362 is the fifth
    bolded item in the same paragraph. Correct to "Five more" (and re-derive the headline/title count
    per F2 in the same edit so the two numbers stay consistent).
- code: F4
  category: hallucinated-fact
  section: weekly-sector-patterns
  item: "weekly-w33-compromised-party-was-not-the-notifying-party"
  url_or_quote: "title: \"In every European public-sector and critical-infrastructure disclosure this week the organisation that was compromised and the organisation that owes the notification were different bodies — and in the largest, the people affected cannot be told at all\"; headline: \"W33's European breaches all ran through a third party, and the notification duty landed somewhere the intrusion did not\"; body ¶1: \"in all seven of the week's European public-sector and critical-infrastructure disclosures, the organisation inside which the intrusion happened was not the organisation that owes the affected people an answer.\""
  summary: >-
    The universal claim is contradicted by four of the entry's own cases, and the entry itself
    concedes the distinction two paragraphs later ("Where the third party is on the access path rather
    than the data path..."). DGFiP: the intrusion was inside DGFiP and DGFiP notifies (the third party
    supplied stolen credentials — the ministry press release, fetched this iteration, states
    "usurpations d'identifiants d'un agent de la DGFIP et d'un tiers habilité"). Zabka: intrusion
    inside Zabka, Zabka notifies. Retelit: compromised and disclosing body are the same. ACRO: the ICO
    notice fetched this iteration says the hacker "gained unauthorised access to ACRO's website and
    content management system" — the third party held patch management, not the data or the
    notification, and the ICO reprimanded ACRO itself. Only MyDr→~12,000 clinics, CEVA→ten controllers
    and bol.com actually clear the stated claim. Separately, the title's trailing clause "in the
    largest, the people affected cannot be told at all" is supported by nothing in this entry: the body
    says the controllers "know only what they read in the press" and MyDr "cannot yet say what was
    taken" — a scoping failure, not an impossibility of notification (the pager case where receivers
    genuinely cannot be identified is in a different entry). Restate title, headline and the opening
    sentence as the pattern the body actually establishes — a third party on the data path or the
    access path in every case, with the notification duty displaced in three of them.
- code: F5
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-08-16/2026-08-16T2315Z-weekly.md — verification notes"
  url_or_quote: "\"Every inline citation date in the fourteen entries is either the publication date read from a source fetched by this run...\" and \"Fourteen entries share entity keys with earlier strategic or operational entries.\""
  summary: >-
    Both counts are wrong in the published notes. The run published fifteen entries
    (frontmatter entries_published: 15), so the citation-discipline assertion excludes exactly one
    entry — and it is the fifteenth (weekly-w33-russia-...), i.e. the one whose quotation iteration 2
    found fabricated. Separately, only twelve of the fifteen entries carry any entities at all
    (disclosure-to-exploitation, vuln-status-rollup and russia-europe-ukraine all carry entities: []),
    so "Fourteen entries share entity keys" cannot be right either.
- code: F6
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-08-16/2026-08-16T2315Z-weekly.md — Borderline drops"
  url_or_quote: "\"a separate incidents-recap entry pairing the ICO/ACRO reprimand with the UNC5537 guilty plea as retrospective accountability — two items is too thin a pattern to carry a section. Both are carried inside the sector-patterns entry instead ... Nothing relevant was lost\""
  summary: >-
    Only ACRO is carried in the sector-patterns entry. The string UNC5537 appears in no entry of this
    run (grep over entries/2026-08-16/ returns only the run record itself). The published note asserts
    a disposition the output does not implement. Either correct the note to record the UNC5537 guilty
    plea as a straight drop with its own reason, or carry it.
- code: F7
  category: missing-citation
  section: weekly-long-running
  item: "weekly-w33-exfilsquad-claims-validated-status"
  url_or_quote: "body ¶2: \"the same configuration class Switzerland's NCSC put in front of Swiss operators on 4 August, when it advised on anonymous web roles granted excessive Dataverse table permissions\"; Defender takeaway: \"Switzerland's national authority has already told its constituency so.\""
  summary: >-
    The entry's entire Swiss nexus rests on this claim, it is asserted twice, and it carries no inline
    citation, no source record and no references[] link. None of the three cited sources mentions
    Switzerland or NCSC — verified this iteration: the Infosecurity Magazine and Cybersecurity Dive
    pages were fetched and neither contains the strings "Switzerland" or "NCSC". The fact is true and
    already in the store at entries/2026-08-05/ncsc-ch-power-pages-dataverse-anonymous-access-advisory.md
    (event_date 2026-08-04, source https://security-hub.ncsc.admin.ch/#/posts/12823). Add that entry id
    to references[] and/or cite the hub post inline.
- code: F8
  category: editorial-advisory
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup"
  url_or_quote: "evidence[0] quote \"First exploitation attempts against CVE-2026-58231 (unauth RCE in SAP Commerce Cloud, CVSS 10.0) is now hitting our honeypots - 3 days after patch day\" / inline citation https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/"
  summary: >-
    The quote is verbatim on that page (verified this iteration via the bridge) and the URL is cited
    inline in the body, but the URL is absent from the entry's sources[] — the only BleepingComputer
    record in sources[] is the SharePoint article. The sourcing_note names Defused's SAP telemetry as
    load-bearing, so the machine-consumed source list understates the entry's own sourcing. Add the
    record.
- code: F9
  category: editorial-advisory
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup; weekly-w33-looking-ahead"
  url_or_quote: "\"three of the five NatJack NAT primitives\" (roll-up) / \"Three of the five NatJack NAT primitives carry no identifier and no vendor fix, and the Linux change for the one that does is recorded by the researcher as a partial mitigation\" (looking-ahead)"
  summary: >-
    The claim is accurate — entries/2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves.md
    states five primitives, two CVEs, "the other three primitives carry no identifier and no vendor fix
    at all" and the Linux change recorded as "not a complete fix". But that entry is in neither
    entry's references[], though both derive a load-bearing count from it and both reference every
    other contributing operational entry. Add 2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves
    to both references[] lists.
- code: F10
  category: editorial-advisory
  section: weekly-research
  item: "weekly-w33-russia-europe-ukraine-defence-supply-chain"
  url_or_quote: "sourcing_note: \"A prior research sub-agent surfaced this piece and set it aside as a retrospective compilation; that reading is fair as to the underlying facts...\""
  summary: >-
    Workflow-internal language in reader-visible published text. site/build.py renders sourcing_note
    verbatim onto the entry page (assess-note block, build.py ~line 3852), so "research sub-agent"
    ships to readers. This is the explicit style-discipline prohibition. Rephrase without the pipeline
    mechanics, e.g. "this piece was initially set aside as a retrospective compilation; that reading is
    fair as to the underlying facts". The body's opening sentence ("The week's strategic entries are
    otherwise about criminal and espionage tradecraft against the estate") is the same register and
    reads oddly on a standalone entry page — worth trimming in the same edit, though it breaks no rule.
```
