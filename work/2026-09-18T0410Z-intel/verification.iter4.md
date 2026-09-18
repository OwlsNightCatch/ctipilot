**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-18T06:00:45Z · ended_at=2026-09-18T06:12:30Z · duration_seconds=705

## Verification report — 2026-09-18T0410Z-intel (iteration 4)

Prior-iteration (iteration 3) deltas walked first, against the current file state and freshly fetched sources:

1. FMC entry, split CVE-2026-20324 evidence[] quotes — fetched `cisco-sa-fmc-sftunn-codex-c3O4Jft2` directly. Both records are contiguous verbatim substrings of the advisory ("A registered sftunnel peer has incorrect permissions..." and "A successful exploit could allow the attacker to write a file... valid user credentials on the affected device."). Confirmed correct.
2. Brevo entry, ClickFix Win+R/paste/Enter mechanics — fetched Brevo's write-up and Sansec's article. Brevo's write-up states "asking the visitor to press Win+R, then Ctrl+V, then Enter"; Sansec's article never states this, only "does not activate for crawlers, developers and automated scanners." Re-attribution confirmed correct.
3. Brevo entry, Trezor connection — fetched BleepingComputer's article: it states the Sept-10 SSO incident "reported on September 11 that phishing attacks reached 347,000 user email addresses" (Trezor); Brevo's own post-mortem never mentions Trezor. Re-attribution confirmed correct.
4. Revolut entry, Hudson Rock vs. Duel quote re-attribution — fetched Hudson Rock's article (via jina, since direct extract returns only a LiveChat shell). Confirmed the page has two distinct sections: an attacker-account section credited "The Duel Investigations Team" and a separate "Hudson Rock's Analysis & Intelligence > New Insight from Hudson Rock" section. Both re-attributed evidence[] quotes match their correct section verbatim. Confirmed correct.
5. NTC entry, "Switzerland has taken no equivalent step" removal — fetched SRF's article; it does not state this, only the EU/US measures now cited. Confirmed correct removal, remaining sentence accurately cites SRF.
6. Gyazo entry, ID-secrecy framing re-attribution to The Hacker News — fetched THN's article: "the link is the only thing protecting it, and the leaked image IDs are the part of the link that makes it unguessable." Confirmed correct.
7. Acronis entry, event_date correction to 2026-09-16 — fetched Help Net Security's article; its own dateline is "2026-09-16". Confirmed correct.
8. FamousSparrow entry, "government entities named among the targets" rewording — fetched ESET's article: it states "90% of the group's targets registered in our telemetry have been located in the region" and separately "we've seen the new backdoor deployed against governmental entities in [8 countries]"; ESET never quantifies a governmental-entity proportion. Confirmed correct removal — see new finding #1 below on a related but distinct overstatement elsewhere in the same entry.
9. Gyazo entry, closing-sentence citation for Helpfeel's other products — fetched Helpfeel's own notice: "(3) Impact on Other Helpfeel Services... we have not confirmed any unauthorized disclosure of information from the Helpfeel or Cosense systems." Confirmed correct.
10. Check Point entry, CISA SSVC claim removal — confirmed no such claim remains anywhere in body or sourcing_note; the remaining framing ("No source... reports observed exploitation... all three are silent") is accurate per Check Point's advisory and CERT-FR's advisory, both fetched this iteration.
11. Acronis entry, primary-source constraint (advisory, no change) — independently confirmed this iteration: `https://security-advisory.acronis.com/advisories/SEC-10986` returns only "Please enable JavaScript to continue." on direct fetch. No reachable vendor primary exists; sourcing_note is accurate.

All eleven prior-iteration remediations verified correct. Full independent cold pass follows, covering all 7 new entries, all 3 updated entries (including `git diff` against each), the run record, and the dedup context.

### Claims missing inline citation

**#1** — `ntc-swiss-solar-inverter-cybersecurity-assessment`: "NTC deliberately withheld product names and technical exploit detail, reporting findings confidentially to manufacturers, most of whom have already shipped fixes; **no CVEs were assigned** ([NTC, 2026-09-17])." No source — NTC's own page, SRF, or cash.ch — states that no CVEs were assigned to any of the findings; this is an inference from the absence of any CVE mention, presented as a flat fact with no supporting citation. Fix: cite explicitly as an editorial inference, or drop the clause.

### Editorial / less-is-more flags (advisory)

**#2** — Run record `runs/2026-09-18/2026-09-18T0410Z-intel.md`, "Verification & coverage notes" section (published reader-facing text per the spawn message). Contains repeated workflow-internal language the hard rule in CLAUDE.md and check 12 both prohibit ("no workflow-internal language... in any entry or in the run-record notes"):
- `"**Phase 4 deep-read pass (follow-up sub-agent, will-publish set of 10 items exceeding the ~8-item main-agent threshold):**"` — contains "Phase 4", "sub-agent", and "main-agent" in one heading.
- `"Independently surfaced by both S2 (English NTC page) and S3 (German NTC page + SRF); composed once, merging both discovery traces."` — "S2"/"S3" are internal sub-agent worker identifiers.
- `"S2 independently reached the day's NTC solar-inverter story through the RSS listing and a WebSearch pivot, bypassing the blocked article entirely."` — same.
- `"...all re-checked (S4), no change on any..."` and `"...all re-checked (S1/S3), no material development on any..."` — same pattern repeated twice more in the coverage-backlog paragraph.

This is a systemic pattern (5+ instances), not a one-off slip, and it appears in text the spawn message states is published. Fix: rewrite the coverage-notes section in workflow-neutral language (e.g., "the English-language NTC page" / "the German-language NTC page and SRF" instead of "S2"/"S3"; drop "Phase 4"/"sub-agent"/"main-agent" from the deep-read-pass heading).

### Missed angles

**#3** — (low confidence) `revolut-fake-government-request-kyc-breach`: CyberInsider's 2026-09-16 article (fetched this iteration) states "Separate reporting states that Revolut has contacted around 680 affected customers" — a specific customer count from a source CyberInsider does not itself cite by name. The entry's sourcing_note states Revolut "declines to name... the number of customers affected," which remains true of Revolut itself, but a citable third-party customer-count claim may exist and is not chased down. Suggested pivot: search for the originating outlet behind CyberInsider's "separate reporting" (likely UK trade press covering the Computing.co.uk/DataBreaches.net thread) for a nameable, citable source of the 680 figure.

### Quantifier without source

**#4** — (low confidence) `famoussparrow-sparrowocky-backdoor-latam-gov`, main-analysis first sentence: "ESET documents FamousSparrow's shift to a new flagship backdoor, SparroWocky, replacing SparrowDoor as **the group's exclusive implant** since August 2025." ESET's own article (fetched this iteration) never calls SparroWocky the group's "exclusive" implant — it states SparroWocky "quickly replaced SparrowDoor as FamousSparrow's **main** implant" and, separately, "quickly became the group's new **flagship** implant, replacing SparrowDoor." The entry's own frontmatter `summary` correctly uses "flagship implant" (ESET's own wording); the body's "exclusive implant" is a stronger, unsourced word substituted in the same paragraph, and the registry record (`entities/registry.yaml`, `actor:famoussparrow`) repeats it: "exclusive known user of the SparrowDoor backdoor and, since August 2025, its successor SparroWocky." "Exclusive" for SparrowDoor is ESET's own claim ("FamousSparrow is the only known user of the SparrowDoor backdoor"); extending "exclusive" to SparroWocky is the entry's own inference, not a stated ESET claim. Fix: replace "exclusive implant" with "flagship implant" (matching both ESET and the entry's own summary) in the body, and soften the registry summary's "and... its successor SparroWocky" clause to avoid implying ESET stated SparroWocky-exclusivity.

### Citation does not support the claim

**#5** — (low confidence) `ntc-swiss-solar-inverter-cybersecurity-assessment`, opening sentence: "...seven solar inverters and four energy-management systems from eight manufacturers, **representative of** Switzerland's roughly 338,000 grid-connected photovoltaic installations ([cash.ch, 2026-09-17])." cash.ch's article (fetched this iteration) states the 338,000-installation figure as separate background context ("Ende 2025 waren in der Schweiz rund 338'000 netzverbundene Anlagen installiert") — it never frames the eleven tested products as "representative of" that fleet. NTC's own page similarly only says the tested devices are "like those installed in thousands of Swiss homes," a much weaker claim. The "representative of" framing is the entry's own gloss, not stated by the cited source.

**#6** — (low confidence) `ntc-swiss-solar-inverter-cybersecurity-assessment`: "...reporting findings confidentially to manufacturers, **most of whom have already shipped fixes** ([NTC, 2026-09-17])." NTC's own English page (fetched this iteration) states only "Most responded quickly, while work to fix the vulnerabilities is still under way for some products" — hedged, and short of "already shipped fixes." The stronger claim is actually supported by cash.ch's German text ("Die meisten Hersteller hätten rasch... bereits Lücken geschlossen" — "already closed the gaps"), fetched this iteration, but cash.ch is not the source cited for this clause. Fix: either cite cash.ch alongside NTC for this specific clause, or soften to match NTC's own hedged wording.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 2, advisory: 1)`

Truth findings: #4, #5, #6 (all low confidence — F14, F3, F3). Editorial findings: #1 (F5), #3 (F10, low confidence). Advisory: #2 (F11).

No F1/F2 (broken or generic URLs) — every cited URL this iteration resolved to a specific article/advisory and was reachable (BSI CERT-Bund's human page needed jina to render past its Angular shell, but this only affects a corroborating, non-quote-bearing source and was already the run's own documented behavior). No F4/F13 hallucinated facts or analytical-link-as-fact issues found — every named entity, CVE id, CVSS score, date, and version I cross-checked (Check Point sk1000155, CERT-FR AVI-1193 and AVI-1197, BSI WID-SEC-2026-3429, CISA KEV JSON for CVE-2026-87886/76460/20079, Help Net Security + BleepingComputer for Acronis, NTC/SRF/cash.ch for the solar-inverter entry, ESET's full SparroWocky article including its 34-id ATT&CK table, Kaspersky's MovieReaper article including both its "Victims" and introduction country lists, Helpfeel's own notice + The Hacker News for Gyazo, Brevo's post-mortem + Sansec + BleepingComputer for the Brevo incident, the two new Cisco PSIRT advisories for CVE-2026-20324/20242, NCSC-NL's CSAF JSON for the two Dutch-original evidence quotes, and Hudson Rock + CyberInsider for the Revolut update) held up. All three updated entries' `git diff` output showed only the declared changelog-record fields changing, with matching `## Update` sections, correct `updated_at` floats, and unchanged `discovered_at`/`run_id`/path. `org_triage: null` and `watchlist_hit: false` hold on all 10 entries (no F16). Classification blocks present and plausible on all 10 entries (no F17 defect found). No IOCs, no vanity metrics, English throughout in every entry (F16/F17/style checks pass) — the sole style-discipline defect is the run-record's workflow-internal language (#2).

### Findings summary (machine-readable)

```yaml
- code: F5
  category: missing-citation
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "no CVEs were assigned"
  summary: "No source (NTC, SRF, cash.ch) states that no CVEs were assigned; presented as fact with no citation."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-09-18/2026-09-18T0410Z-intel.md — Verification & coverage notes"
  url_or_quote: "Phase 4 deep-read pass (follow-up sub-agent, will-publish set of 10 items exceeding the ~8-item main-agent threshold)"
  summary: "Workflow-internal language ('Phase 4', 'sub-agent', 'main-agent', and repeated 'S1'/'S2'/'S3'/'S4' sub-agent identifiers) appears repeatedly in the published run-record coverage notes, violating check 12 / CLAUDE.md's hard rule."
- code: F10
  category: missed-angle
  section: revolut-fake-government-request-kyc-breach
  item: "Revolut discloses a customer KYC data breach..."
  url_or_quote: "Separate reporting states that Revolut has contacted around 680 affected customers (CyberInsider, 2026-09-16)"
  summary: "(low confidence) A specific, potentially citable customer count exists in third-party reporting CyberInsider references but does not name; not chased down or included. Suggested query: find the outlet behind CyberInsider's '~680 affected customers' claim (likely UK trade press in the Computing.co.uk/DataBreaches.net thread)."
- code: F14
  category: quantifier-without-source
  section: famoussparrow-sparrowocky-backdoor-latam-gov
  item: "FamousSparrow retires SparrowDoor for SparroWocky..."
  url_or_quote: "replacing SparrowDoor as the group's exclusive implant since August 2025"
  summary: "(low confidence) ESET calls SparroWocky the group's 'main'/'flagship' implant, never 'exclusive'; the entry's own frontmatter summary correctly says 'flagship' while the body and the registry summary say 'exclusive', an unsourced strengthening."
- code: F3
  category: claim-not-supported
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "representative of Switzerland's roughly 338,000 grid-connected photovoltaic installations ([cash.ch, 2026-09-17])"
  summary: "(low confidence) cash.ch states the 338,000 figure as separate background context, not as a claim that the tested products are 'representative of' the fleet; NTC's own page makes only the weaker claim 'like those installed in thousands of Swiss homes'."
- code: F3
  category: claim-not-supported
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "most of whom have already shipped fixes ([NTC, 2026-09-17])"
  summary: "(low confidence) NTC's own English page is hedged ('work to fix vulnerabilities is still under way for some products'); the stronger 'already shipped fixes' claim matches cash.ch's German text ('bereits Lücken geschlossen'), which is not cited for this clause."
```
