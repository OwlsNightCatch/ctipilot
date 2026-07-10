**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-10T05:06:11Z · ended_at=2026-07-10T05:13:03Z · duration_seconds=412

## Verification report — 2026-07-10T0409Z-intel (iteration 2)

### Prior-iteration deltas verified (iteration 1 → this iteration)

- **F4 (nextcloud, truth) — HELD.** Fetched `https://cybernews.com/security/nextcloud-cloud-provider-data-leak/` via jina reader (WebFetch 403'd). The quote "The issue was caused by a misconfiguration of our hosting infrastructure and is not related to the Nextcloud solution. No other Nextcloud servers belonging to our customers, partners or other users have been affected by this issue" appears verbatim, attributed on-page to "the company's spokesperson." `evidence[2].publisher` is now `Cybernews` in the entry — correct. Fix held.
- **F5 (citrixbleed, editorial) — HELD.** Fetched Huntress's own blog (`https://www.huntress.com/blog/citrixbleed-2-dragonforce-ransomware`) and the IT Security Guru corroboration. Confirmed Huntress states only "Patch Citrix NetScaler appliances to the latest software version, and regularly review the appliance for updates" — no specific build strings anywhere in either cited source. The entry's `cves[].fixed` and action #1 now correctly point to Citrix's bulletin without restating unsourced build numbers. Fix held.
- **F11 (odido, advisory) — HELD, but see new F3/F17 below.** The entry is now a standalone `incident` (`update_of: null`) cross-linking `2026-06-26/shinyhunters-used-a-single-vishing-call-into-the-company-s-i` via `references[]` (confirmed present in `prior_coverage.json`). The framing is coherent, the in-window hook (9 July voice-analysis attribution) is the anchor, and the underlying vishing TTP is referenced rather than re-taught ("This extends the ShinyHunters vishing-to-spoofed-portal playbook … already covered in this store"). Structural fix held — but my own fresh read of this entry surfaced two new issues below.

### Citation does not support the claim

**F3.** Entry: `2026-07-10/odido-shinyhunters-vishing-dutch-police-attribution`. Body claim: "the operators had already bulk-exported 6.2 million customer records (name, address, contact details, customer number, bank account number, date of birth, and passport/driver's-license numbers) — the CEO's Dutch quote via NOS: …" The nearest/only inline citation carrying this sentence is `[NOS, 2026-05-12]` → `https://nos.nl/artikel/2614128-odido-ontdekte-pas-na-bericht-van-hackers-dat-klantgegevens-waren-gestolen`, which I fetched in full via jina. That article states Odido sent "6,2 miljoen berichten" (6.2 million *notification messages*) to customers/ex-customers, and "Odido blokkeerde het account … binnen een uur" (account blocked within an hour) — it does **not** itemise any data-field types at all, and does not state 6.2 million *records were exported*. I checked the other two cited sources in this entry (`politie.nl` primary and `nos.nl/2622288`) — neither mentions the field-type breakdown either. The actual field-type list (name, address, city, phone, customer number, "rekeningnummer"/account number, DOB, passport/driver's-license numbers + validity dates) is stated in a different NOS article, `https://nos.nl/artikel/2602080-hack-bij-odido-gegevens-miljoenen-klanten-in-handen-van-criminelen` ("Onder de klantgegevens vallen onder meer volledige naam, adres en woonplaats, telefoonnummer, klantnummer, e-mailadres, rekeningnummer, geboortedatum en nummers en geldigheidsdatum van identiteitsbewijzen…"), and the explicit "bankrekeningen" (bank accounts) wording is in yet another NOS article, `2604072`. **Neither is in this entry's `sources[]` list.** The specific facts are true and traceable, but as written they read as sourced to a citation that does not contain them. Fix: add the `2026-02-12` NOS article (2602080) as a corroborating source and re-point the parenthetical's citation, or drop the parenthetical to the two facts the cited sources actually carry (account count, hour-blocked).

### Needs more research

**F8.** Entry: `2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns`. Frontmatter carries `tags: [identity, phishing, cloud, ai-abuse]`. I fetched the primary Huntress source and confirmed it does support an AI-abuse angle — the EvilTokens phishing-as-a-service platform is described as *"a commercial product, with a storefront, AI-assisted lure generation, 24/7 support team, and customer reviews included"* (Huntress's own outbound link to its EvilTokens writeup is titled `eviltokens-ai-powered-phishing-report`). The entry body never mentions this — the only body reference to EvilTokens is "it was attributed to a phishing-as-a-service operation Huntress tracks as EvilTokens," with no mention of AI-assisted lure generation anywhere in the prose. A reader scanning by the `ai-abuse` tag gets nothing to act on; the source clearly supported a sentence on this (e.g., noting the construction-RFP lures were AI-generated at scale, relevant to why they reached 344 orgs). Suggested fix: add one clause in paragraph 2 naming the AI-assisted lure-generation capability, or drop the `ai-abuse` tag if it's judged not worth the body real estate.

### Classification missing / inconsistent

**F17.** Entry: `2026-07-10/odido-shinyhunters-vishing-dutch-police-attribution`. The entry's own `sourcing_note` states: *"Primary is the Dutch National Police statement (Admiralty A for its own investigation)…"* — but the `classification` block two fields below it sets `reliability: B`. This is an internal self-contradiction: the entry asserts Admiralty A reliability for its primary source in prose, then codes it B in the structured field the reader/machine actually consumes. For comparison, this run's other national-authority-primary entry (`cert-lv-lvm-olpha-ransomware`) codes its CERT.LV primary as `reliability: A` — consistent treatment would put the Dutch National Police statement (a government law-enforcement authority reporting on its own investigation) at the same letter, or the prose should be corrected to match B. Either the `classification.reliability` value or the `sourcing_note` text is wrong; they must agree.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 2, advisory: 0)**

All three prior-iteration (iteration 1) fixes verified held on fresh re-fetch of their respective sources. Every other URL across all six entries (Huntress ×3, IT Security Guru, Sophos, The Hacker News, CERT.LV ×2, The Record, BNN News, Cybernews, heise, Politie.nl, NOS ×3, SentinelLabs, Express Tribune) was fetched in this iteration and supports its attached claim; no broken links, no other hallucinated entities, no priority-calibration or org-triage/watchlist violations found. Coverage shape (soundness + completeness) matches the run record's documented drop rationale (Sonatype stats roundup, Gitea/Hermes CVEs, uncorroborated leak-site claims) — no additional in-window gap identified within this iteration's budget.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: incidents
  item: "Odido ShinyHunters vishing — Dutch police attribution"
  url_or_quote: "the operators had already bulk-exported 6.2 million customer records (name, address, contact details, customer number, bank account number, date of birth, and passport/driver's-license numbers)"
  summary: "Cited NOS article (2614128) discusses 6.2M notification messages and the hour-long block, not the record field-type breakdown or an export count; the field-type list is stated in an uncited NOS article (2602080/2604072)."
- code: F8
  category: needs-more-research
  section: research
  item: "M365 Conditional Access gaps — Railway/LSHIY campaigns"
  url_or_quote: "tags: [identity, phishing, cloud, ai-abuse]"
  summary: "Huntress source describes EvilTokens PhaaS as having 'AI-assisted lure generation'; entry tags ai-abuse but body never mentions this capability."
- code: F17
  category: classification
  section: incidents
  item: "Odido ShinyHunters vishing — Dutch police attribution"
  url_or_quote: "sourcing_note: \"Primary is the Dutch National Police statement (Admiralty A for its own investigation)...\" vs classification.reliability: B"
  summary: "Entry's own sourcing_note asserts Admiralty A for its primary source; classification block codes reliability B. Self-contradictory; compare cert-lv entry in same run which codes its national-CERT primary as A."
```
