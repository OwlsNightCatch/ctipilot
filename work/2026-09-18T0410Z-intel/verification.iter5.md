**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-18T06:18:18Z · ended_at=2026-09-18T06:29:10Z · duration_seconds=652

## Verification report — 2026-09-18T0410Z-intel (iteration 5)

### Prior-iteration (iteration 4) deltas — verified

1. **F5+F3 (ntc-swiss-solar-inverter-cybersecurity-assessment)** — checked all three re-cited claims against fresh fetches of `en.ntc.swiss` and `cash.ch`:
   - The 338,000-installation figure now reads "of the kind installed in thousands of Swiss homes ([NTC]) among Switzerland's roughly 338,000 grid-connected photovoltaic installations ([cash.ch])" — NTC's own page says "devices like those installed in thousands of Swiss homes" (verbatim match) and cash.ch says "Ende 2025 waren in der Schweiz rund 338'000 netzverbundene Anlagen installiert" (verbatim match). **Correctly fixed** — no more "representative of" gloss.
   - The Federal Office of Energy confirmation, cited to SRF, is supported: SRF states "Das Bundesamt für Energie bestätigt die Analyse: Das Risiko eines koordinierten Angriffs könne nicht ausgeschlossen werden." **Correctly fixed.**
   - The fix-status clause: **not fully fixed** — see new F3 finding #2 below, a residual on the exact clause iteration 4 believed it had closed.
2. **F11 (run-record)** — grepped the full "Verification & coverage notes" body for `phase|sub-?agent|main.agent|S1|S2|S3|S4|spawn|deepread`: zero hits. **Confirmed clean**, no internal jargon remains.
3. **F10 (revolut, low confidence)** — CyberInsider's page confirms "Separate reporting states that Revolut has contacted around 680 affected customers." The entry's added sentence — "a figure this entry cannot independently verify" — reads as properly hedged, not presented as fact. **Confirmed correct.**
4. **F14 (famoussparrow, low confidence)** — ESET's own text: "which then quickly replaced SparrowDoor as FamousSparrow's **main implant**." The body now reads "the group's main implant," matching ESET's own wording exactly and consistent with the frontmatter summary's "flagship." **Confirmed correct and consistent.**

Then did a full independent cold pass below.

### Citation does not support the claim

**#1.** `ntc-swiss-solar-inverter-cybersecurity-assessment` — body: "no CVEs were assigned to any of the findings ([NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems))." Fetched NTC's English page in full (`fetch_source.py extract`) and searched it for "CVE": zero occurrences anywhere in the page text. The cited source never states, and never mentions, CVE assignment at all. This is the clause iteration 4 reported fixing ("added a citation to the no-CVEs-assigned clause") — the citation was added, but it does not support the claim it is attached to.

**#2.** `ntc-swiss-solar-inverter-cybersecurity-assessment` — body: "most manufacturers have already closed the reported gaps, though work is still under way for some products (translated from German) ([cash.ch, 2026-09-17](https://www.cash.ch/news/studie-findet-kritische-cyberlucken-bei-schweizer-solaranlagen-969350))." Fetched cash.ch in full: its only relevant sentence is "Die meisten Hersteller hätten rasch auf die gemeldeten Schwachstellen reagiert und bereits Lücken geschlossen" ("Most manufacturers reacted quickly to the reported vulnerabilities and have already closed gaps") — cash.ch never states or implies that work is still under way for any product; if anything its framing is unhedged ("already closed"). The "work is still under way for some products" half of the sentence is NTC's own English-page wording ("Most responded quickly, while work to fix the vulnerabilities is still under way for some products"), which is cited elsewhere in the same paragraph for a different clause but not attached here. This is the exact clause iteration 4's remediation note claims to have "re-cited... to cash.ch's own stronger German text" — the re-citation covers only half the sentence's content; the hedge clause is still spliced from the co-cited NTC source without its own citation. A residual instance of the pipeline's dominant defect class (check 2d).

### Unsupported / hallucinated facts

**#3 (low confidence).** `entities/registry.yaml` — new entity `actor:famoussparrow` (added this run), summary: "exclusive known user of the SparrowDoor backdoor and, since August 2025, its successor SparroWocky." ESET's article ([welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/](https://www.welivesecurity.com/en/eset-research/beware-sparrowock-backdoor-bites-commands-catch/)) states "FamousSparrow is the only known user of the SparrowDoor backdoor" — but for SparroWocky it only says "we attribute the latest campaign and the SparroWocky backdoor to FamousSparrow with high confidence" via circumstantial evidence (co-deployment with SparrowDoor, victimology overlap), never asserting exclusivity of SparroWocky the way it does for SparrowDoor. The registry sentence's grammar extends "exclusive known user of" across both backdoors, which the cited reporting does not support for the second one. This is in the registry entity (which renders on entity pages), not the entry body itself, and the underlying attribution confidence is genuinely high — hence low confidence — but the "exclusive" framing for SparroWocky specifically is not sourced.

### Needs more research

**#4 (low confidence).** `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` — Help Net Security's article states plainly: "There's currently no signs of its active exploitation on Plesk deployments," narrowing Acronis's own exploitation claim to cPanel & WHM only. The entry's body correctly quotes the cPanel-scoped exploitation sentence, but never surfaces the explicit Plesk-negative statement, and the frontmatter `cves[].status: [exploited, ...]` is a single blanket status covering a CVE whose `affected_products[]` includes both cPanel & WHM and Plesk. A defender running only the Plesk build loses a genuinely source-supported prioritization signal (confirmed-exploited vs. patch-available-only).

**#5 (low confidence).** `gyazo-helpfeel-data-breach-image-upload-rce` — The Hacker News draws a real distinction Gyazo's own help pages support: the default "unguessable link" privacy relies on ID secrecy (defeated by the leak), but the "Only me" and password-locked private settings are described as not viewable via the link alone even by someone who has it ("Both settings are available only on paid plans, and Helpfeel has not said which it means or how such images could have been viewed" — THN's own hedge). The entry's sentence — "Gyazo's default access-control model for a 'private' image relies entirely on the image ID staying secret... the leaked IDs directly defeat that model" — blurs the "default" (unlisted, not truly access-controlled) case with the stricter "private" settings the source itself flags as a separate, unresolved question. Not a hallucination (the entry correctly carries Helpfeel's own hedge, "cannot rule out," in the next clause), but the technical nuance the source draws is worth restoring for a Tier 2 reader assessing actual exposure of password-protected/"Only me" images.

### Editorial / less-is-more flags (advisory)

**#6.** No new advisory-only items beyond what's already resolved. The run's action-item lists (Check Point, Acronis, NTC/none, FamousSparrow/none, MovieReaper/none, Gyazo/none, Brevo) all pass the do-now bar on this read; none read as generic or padded.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 2, advisory: 0)`

Two genuine truth residuals on `ntc-swiss-solar-inverter-cybersecurity-assessment` survived iteration 4's remediation of the *same sentence* — the "no CVEs assigned" citation doesn't support the claim at all, and the "work still under way for some products" half of the fix-status clause is still spliced from a co-cited source (NTC) onto a citation (cash.ch) that doesn't state it. Both are narrow, single-sentence fixes (attach the NTC citation to the hedge clause; either drop the "no CVEs assigned" claim or cite something that actually states it — note NTC's page never mentions CVEs at all, so this may need to be dropped rather than re-cited). The registry entity overclaim (#3) and the two research-depth notes (#4, #5) are lower-severity and lower-confidence. Every other entry, every updated entry's diff (Cisco FMC, Cisco ISE, Revolut), and the run record's rewritten notes body checked clean on a full fresh read: every inline citation I fetched (Check Point sk1000155, BSI WID-SEC-2026-3429, CERT-FR AVI-1193/AVI-1197, NCSC-NL NCSC-2026-0382 via the CSAF bridge, Help Net Security, BleepingComputer ×2, Kaspersky Securelist, ESET WeLiveSecurity, Helpfeel's own notice, The Hacker News, Brevo's post-mortem, Sansec, TechCrunch, Security Affairs, DataBreaches.net, Hudson Rock via jina, CyberInsider) supports the claim attached to it, all `evidence[]` quotes I checked are contiguous verbatim substrings, the FamousSparrow `techniques[]` 34-id list matches ESET's own ATT&CK table id-for-id in the same order, and `check_run.py` still exits 0 (48 pass · 0 warn · 0 fail). No missed-angle or coverage-shape defect found; the dropped OpenAI item and the "Pays de l'Aigle" backlog note both read as correctly reasoned quality-over-quantity calls.

### Findings summary (machine-readable)

- code: F3
  category: claim-not-supported
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "no CVEs were assigned to any of the findings ([NTC, 2026-09-17], https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)"
  summary: "NTC's English page never mentions CVEs anywhere; the citation does not support the claim."
- code: F3
  category: claim-not-supported
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "though work is still under way for some products (translated from German) ([cash.ch, 2026-09-17])"
  summary: "cash.ch's own German text only says gaps were already closed, with no hedge about ongoing work for some products; that hedge is NTC's own English-page wording, cited elsewhere in the paragraph but not attached to this clause."
- code: F14
  category: quantifier-without-source
  section: famoussparrow-sparrowocky-backdoor-latam-gov
  item: "entities/registry.yaml — actor:famoussparrow"
  url_or_quote: "exclusive known user of the SparrowDoor backdoor and, since August 2025, its successor SparroWocky"
  summary: "(low confidence) ESET calls FamousSparrow the only known user of SparrowDoor but only attributes SparroWocky with high confidence via circumstantial evidence, never asserting exclusivity of SparroWocky itself."
- code: F8
  category: needs-more-research
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "CVE-2026-87886 — Acronis Backup plugin for cPanel/WHM and extension for Plesk"
  url_or_quote: "There's currently no signs of its active exploitation on Plesk deployments. (Help Net Security)"
  summary: "(low confidence) Entry's blanket exploited status doesn't surface the source's explicit Plesk-negative exploitation statement, a real prioritization signal for Plesk-only deployments."
- code: F8
  category: needs-more-research
  section: gyazo-helpfeel-data-breach-image-upload-rce
  item: "Gyazo (Helpfeel) image-upload-server breach"
  url_or_quote: "Gyazo's default access-control model for a 'private' image relies entirely on the image ID staying secret... the leaked IDs directly defeat that model"
  summary: "(low confidence) Blurs The Hacker News's own distinction between the default unguessable-link privacy (defeated by the leak) and the 'Only me'/password-locked settings the source flags as a separate, unresolved question."
