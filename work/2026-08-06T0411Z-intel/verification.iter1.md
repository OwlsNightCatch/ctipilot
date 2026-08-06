**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-06T05:00:34Z · ended_at=2026-08-06T05:12:53Z · duration_seconds=739
**Self-telemetry:** urls_checked=17 · webfetch_calls=13 · bridge_fetches=6 · websearch_calls=0

## Verification report — 2026-08-06T0411Z-intel (iteration 1)

Read cold. Every inline source URL on all nine entries was fetched in this iteration (WebFetch, or `tools/fetch_source.py url` / `jina` / `ncsc-csh` where the host required it). Every `evidence[]` quote was checked as a contiguous substring against the fetched page. Every `cves[]` id and CVSS was checked against the owning vendor advisory (Veeam KB4892/KB4893 per-CVE rows including vectors, HPE Aruba CSAF, cPanel KBs + The Hacker News for the CNA score, VulnCheck). No URL was broken, generic, or an oversight page; no NVD/MITRE per-CVE page or CERT index is cited as a primary; no IOCs, no vanity metrics, no workflow-internal language leaked into any entry.

The four pre-publication quote corrections held: all fifteen `evidence[]` quotes across the nine entries are exact contiguous substrings of their cited pages, and the corrections did not introduce new defects. The cPanel root-cause attribution (item 2 of the spawn message) is correct — The Hacker News carries "SQL mode is not preserved when a database is renamed, causing SQL to execute in root context." verbatim, neither cPanel KB contains it, and the entry attributes it to the reporting outlet rather than to the vendor. The water entry does not smuggle Iran attribution back in (item 3) — the word Iran appears nowhere in it, and the declination is explicit. The LiteLLM out-of-window-original decision (item 4) is defensible, not recycled news: the technique has no prior coverage, no CVE and no patch cycle, the in-window CSA note is a genuine secondary, and `event_date` records the original disclosure. Priority calibration (item 5) is sound — no `high` fails the TL;DR bar, no `notable` clears the critical bar, and `notable` on Veeam is defensible given no exploitation by any party. Both borderline drops (item 6) are correctly argued and I found no relevant returned item left behind.

Nine findings follow.

### Citation does not support the claim

**F2 — `entries/2026-08-06/canton-graubuenden-sharepoint-server-breach.md`: the website-downtime detail is cited to persoenlich.com, which does not carry it.**

Entry body, paragraph 1:

> AFI deployed an out-of-band update on the evening of 5 August, taking the cantonal website offline for several hours ([persoenlich.com, 2026-08-05](https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden)).

I fetched https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden in this iteration. Its full text carries the update itself — "führt das AFI gemäss Mitteilung am Mittwochabend ab 19 Uhr ein ausserordentliches Update auf der kantonalen Website durch" — but contains **no** statement about the site being unreachable, and no duration. The "offline for several hours" fact belongs to the other co-cited source: the cantonal press release (https://www.gr.ch/DE/Medien/Mitteilungen/MMStaka/2026/Seiten/20260805010805.aspx), which I also fetched, says "Ab diesem Zeitpunkt wird die Webseite für mehrere Stunden nicht erreichbar sein." Classic co-cited-source splice.

*Remediation:* attach the gr.ch press-release citation to the downtime clause (or split the sentence so each citation carries its own fact).

*Secondary, same entry, lower confidence:* "the cantonal ePortal and specialised applications run on separate infrastructure and were unaffected ([Kanton Graubünden, 2026-08-05])" — the release states only that they are "vom Cyberangriff nicht betroffen und bleiben auch während des Updates online". "Run on separate infrastructure" is an inference the source does not state. Softening to what the release says ("were unaffected and stayed online through the update") removes the extrapolation.

**F3 — `entries/2026-08-06/veeam-service-provider-console-veeam-one-ten-cves.md`: NCSC-NL did not carry the ten-CVE release; its advisory covers Veeam Service Provider Console only.**

Entry summary:

> Veeam's 2026-08-04 security release fixes ten vulnerabilities across two co-deployed products, carried to European constituencies by CERT-FR and NCSC-NL on 2026-08-05.

Entry body, paragraph 1 (no inline citation on this sentence):

> Veeam published two security bulletins on 2026-08-04 covering ten vulnerabilities, which CERT-FR and NCSC-NL both carried to their constituencies the following day.

I fetched https://advisories.ncsc.nl/advisory?id=NCSC-2026-0276 (WebFetch returned the JS redirect shell; recovered via `python3 tools/fetch_source.py jina`). The advisory is titled "Kwetsbaarheden verholpen in Veeam Service Provider Console", its Producten block lists **Veeam / Service Provider Console** only, its References block lists **only** https://www.veeam.com/kb4893, and its CVE list is exactly four entries: CVE-2026-58073 (9.5), CVE-2026-58072 (9.0), CVE-2026-58067 (8.7), CVE-2026-58071 (8.2). Veeam ONE and the flagship CVE-2026-64633 (10.0) are absent. I also checked https://advisories.ncsc.nl/rss/advisories — NCSC-2026-0276 is the only Veeam advisory in the current feed; there is no companion Veeam ONE advisory. CERT-FR AVI-0968, which I fetched, *does* cover both products and all ten CVEs, so the CERT-FR half of the claim holds.

*Remediation:* qualify to something like "carried to European constituencies by CERT-FR (both products) and NCSC-NL (Service Provider Console) on 2026-08-05", and attach the CERT-FR / NCSC-NL citations to the body sentence, which currently has none.

### Unsupported / hallucinated facts

**F4 — `entries/2026-08-06/litellm-callback-hook-post-inference-tool-call-forgery.md`: the researcher is named as "Johann Rehberger"; neither cited source uses that name.**

Entry summary: "Research published by Johann Rehberger on 2026-08-03". Entry body, paragraph 1: "The technique originates in Johann Rehberger's research published two days earlier ([Embrace The Red, 2026-08-03](https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/))". Entry frontmatter `sources[0].publisher`: `"Embrace The Red (Johann Rehberger)"`.

I fetched both cited pages in this iteration:
- https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/ — bylined **wunderwuzzi** ("wunderwuzzi's blog"); the fetch confirmed explicitly that "Johann Rehberger does not appear anywhere on this page."
- https://labs.cloudsecurityalliance.org/research/csa-research-note-litellm-callback-hook-hijacking-20260805-c/ — names the researcher as **Wunderwuzzi** throughout ("Security researcher Wunderwuzzi disclosed a technique, dubbed 'LLM Heist'…"; "Wunderwuzzi's research, published on the Embrace The Red blog in August 2026…"; reference [1] is credited to "Wunderwuzzi"). "Rehberger" appears nowhere on the page.

The identification is very likely correct in the real world, but no source this entry cites states it, so as written the citation vouches for a name its page does not carry.

*Remediation:* use the byline the sources use ("wunderwuzzi", optionally "wunderwuzzi (Embrace The Red)"), or keep the real name and add a citation that actually states it.

### Quantifier without source

**F1 — `entries/2026-08-06/water-plc-lockouts-twelve-states-first-consumer-impact.md`: the "first consumer-facing impact" framing is contradicted by two of the entry's own cited sources and by the entry it updates.**

This is the entry's headline claim and it appears four times:
- title: "…and a Georgia utility's pressure loss produces **the wave's first consumer-facing impact**"
- headline: "The campaign that was seven states a week ago is twelve, and **one incident reached the tap**"
- summary: "it has produced **its first consumer-facing consequence**"
- body, paragraph 2: "**Every previously reported incident in this wave was a loss of monitoring and control at the operator's console; this one crossed into distribution.**" (no citation attached)

Contradicting evidence from sources cited *on this entry*, both fetched in this iteration:
- https://www.cbsnews.com/atlanta/news/fbi-warns-of-cyber-threats-to-water-utilities-as-clayton-county-investigates-possible-attack/ — "The FBI says some affected water systems experienced pressure loss and flooding as a result." (in the same paragraph block that describes the seven-state FBI PSA)
- https://www.securityweek.com/water-sector-cyberattacks-reportedly-hit-at-least-12-states/ — quoting the FBI alert directly: "Operational effects reported to the FBI have included loss of pressure and flooding. Pressure loss in water systems could potentially allow untreated ground water to seep into pipes."

The pipeline's own prior entry `entries/2026-08-01/fbi-epa-water-plc-lockout-seven-states-eu-exposure.md` — the `update_of` target — already carried both facts: "the FBI records that reported operational effects 'have included loss of pressure and flooding'", and CISA's parallel alert stating the activity "has resulted in boil water notices and sustained manual operations". So neither pressure loss nor a boil-water notice is a first for this wave.

No cited source anywhere uses "first" of the Clayton County incident. The quantifier originates in the S4 research finding title and was carried through unchecked.

*Remediation:* the delta is real but is *named attribution to a specific utility*, not a first. Rewrite the title/headline/summary and the body sentence to something the sources support — e.g. the first named utility to publicly confirm a distribution-side consequence — and delete the "Every previously reported incident…" sentence, which the FBI's own reported effects contradict. The registry and the run record's borderline/triage note carry the same framing and should move with it.

**F5 — `entries/2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor.md`: "more than twenty" / "twenty-plus" overstates VulnCheck's "twenty models", and contradicts the entry's own body and product list.**

- title: "ENDLESSDOORS (CVE-2026-66747) — **twenty-plus** Zbtlink router models…"
- summary: "present by default on **more than twenty** Zbtlink router and CPE models"
- body, paragraph 1: "pre-installed on **more than twenty** router and CPE models"
- `cves[0].affected`: "**More than twenty** Zbtlink router and CPE models and their rebranded equivalents, as shipped"
- but body, same paragraph: "shipped across **twenty** models" (the verbatim source phrase)
- and `affected_products[]` lists exactly **20** models.

I fetched https://www.vulncheck.com/blog/zbt-endlessdoors. It consistently says twenty: the page description is "Twenty router models sold on Amazon, AliExpress, and Alibaba ship with a remote-control implant enabled by default"; the affected-models block lists exactly the 20 in the entry; "Across all twenty models it reduces to four primary and secondary endpoints"; "Check the twenty models listed above against your purchasing records". The only larger-population statement is an explicit hedge VulnCheck does not assert as fact: "The true affected population **might be** larger than the twenty models we examined, but we have no way to enumerate the rest."

*Remediation:* use "twenty" throughout (title, summary, body, `cves[].affected`), and if the larger population is worth keeping, carry VulnCheck's hedge as a hedge. The `entities/registry.yaml` record `tool:endlessdoors` repeats "more than twenty Zbtlink router and CPE models" and should move with it.

**F6 — `entries/2026-08-06/cve-2026-63077-teamcity-kev-confirmed-exploited.md`: "ten days" is nine days.**

- title: "…on the CISA KEV catalog, **ten days after** JetBrains said it had seen none"
- `sourcing_note`: "it has not been updated, so it is not a contradiction of CISA but **a snapshot from ten days earlier**."

The entry's own two dates are correct and I verified both: the JetBrains advisory is dated 2026-07-27 (`sources[1].date`, and the body twice states "has not been revised since 2026-07-27"), and the CISA KEV addition is 2026-08-05 (I fetched https://www.cisa.gov/news-events/alerts/2026/08/05/cisa-adds-one-known-exploited-vulnerability-catalog via `tools/fetch_source.py url`; "CISA has added one new vulnerability to its Known Exploited Vulnerabilities (KEV) Catalog, based on evidence of active exploitation." — CVE-2026-63077, JetBrains TeamCity Deserialization of Untrusted Data Vulnerability). 2026-07-27 → 2026-08-05 is **nine** days.

*Remediation:* "nine days" in the title and the `sourcing_note` (or drop the count and say "on 2026-08-05").

### Claims missing inline citation

**F7 — `entries/2026-08-06/cpanel-whm-cve-2026-58048-database-root-privilege-escalation.md`: the NCSC-CH dashboard claim carries no citation and no source record — and it is the entry's whole Swiss nexus.**

- headline: "A shared-hosting tenant boundary fails on a database rename, **and the Swiss NCSC put it on its own dashboard**"
- body, paragraph 2: "**That is why the Swiss NCSC placed it on its own Cyber Security Hub dashboard for its constituency**, and why it is in scope here…"

Neither statement has an inline link, and `sources[]` contains only the two cPanel KBs and The Hacker News — no NCSC-CH record at all. This is the load-bearing home-region justification for including an authenticated-prerequisite flaw in third-party hosting-panel software (the S1 finding itself flags it borderline for exactly that reason), so it is the one claim on the entry a reader would most want a link for.

I confirmed the claim is **true**: `python3 tools/fetch_source.py ncsc-csh list` returns post id 12827, created 2026-08-05T07:36:30Z, tlpStatus Clear, title "[Advisory] cPanel: Database Privilege Escalation (CVE-2026-58048)". So this is a missing-citation defect, not a false claim — do not remove the claim, source it.

*Remediation:* add the NCSC-CH Cyber Security Hub post as a corroborating `sources[]` record with its per-post detail URL and cite it inline at both places. (The run record already documents that the `/api/v1/posts/{id}/details` route was recovered and re-tested this run, so a reader-facing per-post URL is available.)

### Classification missing / inconsistent

**F8 — `entries/2026-08-06/water-plc-lockouts-twelve-states-first-consumer-impact.md`: `credibility: 1` contradicts the entry's own stated corroboration position and the rule the run applied elsewhere.**

Frontmatter: `classification: {reliability: B, credibility: 1}`. The entry's own `sourcing_note` disclaims corroboration for its headline figure:

> The twelve-state figure originates with ABC News and is relayed by both The Record and SecurityWeek rather than confirmed in a federal statement, so it is reported here as reporting rather than as an agency count.

That is one assessor with several publishers — which is precisely the situation the run record says it rated **2** elsewhere: "The same one-assessor-several-publishers reasoning sets credibility 2 rather than 1 on the Veeam and HPE Aruba entries, where CERT-FR and NCSC-NL restate vendor advisories for their constituencies without independent assessment." Both cited relays (The Record, SecurityWeek) attribute the twelve-state count to ABC News; I verified both pages carry the attribution ("ABC News reported on Tuesday that facilities in at least 12 states are now remediating cyberattacks, including several in Michigan."; "At least 12 states have been hit, according to ABC News").

*Remediation:* `credibility: 2`, consistent with the entry's own note and with the Veeam/Aruba entries in the same run. (For contrast, `credibility: 1` on the CHAINDROP entry is correct — Elastic and OX Security are two genuinely independent first-hand assessors, and I verified both pages report their own telemetry.)

### Editorial / less-is-more flags (advisory)

**F9 — ATT&CK mapping precision on three entries.** `techniques[]` is the evidence-bound surface the `/attack/` matrix and Navigator exports derive from, so these are worth a look; none produces a reader-facing false statement, so the main agent may leave them.

(a) `endlessdoors-zbtlink-router-factory-shipped-root-backdoor.md` maps **T1071.001 (Application Layer Protocol: Web Protocols)**. VulnCheck describes a custom binary protocol on TCP 7000 with a "fixed 39-byte hello" and a second connection to port 7001 for the interactive shell — "It runs as root, it uses no encryption, and it authenticates nobody" — and no HTTP/HTTPS anywhere in the C2 path. The entry's own body agrees: "an inbound-driven command channel on a **high non-standard port**". T1071 (parent) or T1571 fits what the source describes; T1071.001 asserts web protocols the source contradicts.

(b) `litellm-callback-hook-post-inference-tool-call-forgery.md` maps **T1556 (Modify Authentication Process)**, a behaviour neither the body nor either cited source describes — the chain is a config write to `api_base` plus post-call callback hooks. The primary source publishes its own ATT&CK mapping (links to T1552.001, T1078, T1583.004, **T1557**, T1119, T1550.001, **T1565.002**); T1557 (Adversary-in-the-Middle) and T1565.002 (Transmitted Data Manipulation) are the ids the discloser's own analysis supports.

(c) `cve-2026-63077-teamcity-kev-confirmed-exploited.md` maps **T1190 only**, dropping **T1059** which the original 2026-07-29 entry carried and which this body still describes ("yields command execution as the TeamCity server process"; "the server process spawning command interpreters outside build execution") on a source that states it ("execute arbitrary operating system commands").

### Coverage assessment (no findings)

Completeness looks good and I could not name an in-window omission. Specifically checked:
- **NCSC-CH Cyber Security Hub**, the source whose recipe broke and was fixed this run — I ran `ncsc-csh list` myself. Its two in-window posts are 12828 (N-able N-central CVE-2026-18577, 2026-08-05) and 12827 (cPanel, 2026-08-05). 12828 is not a miss: `state/cves_seen.json` and `prior_coverage.json` both show CVE-2026-18577 published on 2026-08-03 and updated 2026-08-05 (`n-able-n-central-post-exploitation-rmm-tunnel-driver`). 12823 (Power Pages, 2026-08-04) falls outside the 26 h window.
- **All twelve returned candidates** across `findings.S{1,2,3,4}.yaml` are accounted for in `triage.json` — nine published, two borderline drops, one folded into tooling. Both borderline drops are correctly reasoned: the Snowflake plea is a retrospective outcome whose only lesson is generic SaaS MFA hygiene, and the Cl0p phase change rests solely on a leak-site scrape with no victim disclosure, which the sourcing policy excludes. Neither should have shipped.
- **No prior-coverage collision** on the CHAINDROP entry: the 14-day window contains other npm supply-chain coverage (SANDWORM_MODE, the W30/W31 weekly status entries) but no Shai-Hulud/CHAINDROP entry, and Elastic itself frames this as a return of the same lineage, so "Shai-Hulud" is not a name collision (F15 does not apply).
- The Graubünden new-entry-rather-than-update decision is right: different victim, different intrusion date, different outcome, its own disclosure — the shared entity is a `related-to` registry edge, not a delta.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 2, advisory: 1)

- Truth (6): F1, F5, F6 are quantifier-class (F14); F2, F3 are claim-not-supported (F3); F4 is hallucinated-fact (F4).
- Editorial (2): F7 (missing citation), F8 (classification).
- Advisory (1): F9 (ATT&CK mapping precision).

No entry needs to be dropped. F1 is the one that changes what a reader takes away and should be fixed first.

### Findings summary (machine-readable)

```yaml
- code: F14
  category: quantifier-without-source
  section: incidents
  item: "2026-08-06/water-plc-lockouts-twelve-states-first-consumer-impact"
  url_or_quote: "a Georgia utility's pressure loss produces the wave's first consumer-facing impact / Every previously reported incident in this wave was a loss of monitoring and control at the operator's console; this one crossed into distribution."
  summary: "No cited source says 'first'. Two sources cited ON this entry say the opposite: CBS News Atlanta — 'The FBI says some affected water systems experienced pressure loss and flooding as a result.'; SecurityWeek quoting the FBI alert — 'Operational effects reported to the FBI have included loss of pressure and flooding.' The update_of target (2026-08-01/fbi-epa-water-plc-lockout-seven-states-eu-exposure) already carried both that FBI quote and CISA's 'has resulted in boil water notices'. Rewrite title/headline/summary to the supportable delta (first named utility to publicly confirm a distribution-side consequence) and delete the 'Every previously reported incident' sentence."
- code: F3
  category: claim-not-supported
  section: incidents
  item: "2026-08-06/canton-graubuenden-sharepoint-server-breach"
  url_or_quote: "https://www.persoenlich.com/digital/nach-dem-bund-trifft-es-auch-graubunden — 'AFI deployed an out-of-band update on the evening of 5 August, taking the cantonal website offline for several hours'"
  summary: "persoenlich.com carries the update ('führt das AFI ... am Mittwochabend ab 19 Uhr ein ausserordentliches Update ... durch') but says nothing about downtime. The 'offline for several hours' fact is in the co-cited gr.ch press release ('wird die Webseite für mehrere Stunden nicht erreichbar sein'). Re-attach the citation. Secondary, same entry: 'run on separate infrastructure' is an inference the gr.ch release does not state — it says only that ePortal and Fachapplikationen were unaffected and stay online during the update."
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "2026-08-06/veeam-service-provider-console-veeam-one-ten-cves"
  url_or_quote: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0276 — 'fixes ten vulnerabilities across two co-deployed products, carried to European constituencies by CERT-FR and NCSC-NL on 2026-08-05'"
  summary: "NCSC-2026-0276 is titled 'Kwetsbaarheden verholpen in Veeam Service Provider Console', lists Service Provider Console as its only product, references only veeam.com/kb4893, and lists exactly four CVEs (58073/58072/58067/58071). Veeam ONE and CVE-2026-64633 (10.0) are absent; the NCSC-NL feed carries no companion Veeam ONE advisory. CERT-FR AVI-0968 does cover both products and all ten. Qualify the NCSC-NL half and add inline citations to the body sentence, which currently has none."
- code: F4
  category: hallucinated-fact
  section: research
  item: "2026-08-06/litellm-callback-hook-post-inference-tool-call-forgery"
  url_or_quote: "Research published by Johann Rehberger on 2026-08-03 / sources[0].publisher: 'Embrace The Red (Johann Rehberger)'"
  summary: "Neither cited source names Rehberger. https://embracethered.com/blog/posts/2026/hijacking-litellm-for-fun-and-profit/ is bylined 'wunderwuzzi'; the CSA note names 'Wunderwuzzi' throughout and credits reference [1] to 'Wunderwuzzi'. Use the byline the sources use, or add a citation that states the real name."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor"
  url_or_quote: "twenty-plus Zbtlink router models / more than twenty Zbtlink router and CPE models"
  summary: "VulnCheck says twenty consistently ('Twenty router models sold on Amazon, AliExpress, and Alibaba ship with a remote-control implant enabled by default'; 'Across all twenty models'; 'Check the twenty models listed above'), and hedges the larger population rather than asserting it ('The true affected population might be larger than the twenty models we examined'). The entry's own body says 'shipped across twenty models' and affected_products[] lists exactly 20. Use 'twenty' in title/summary/body/cves[].affected; the entities/registry.yaml tool:endlessdoors summary repeats the same overstatement."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "2026-08-06/cve-2026-63077-teamcity-kev-confirmed-exploited"
  url_or_quote: "ten days after JetBrains said it had seen none / a snapshot from ten days earlier"
  summary: "JetBrains advisory 2026-07-27 (verified; entry states this twice), CISA KEV addition 2026-08-05 (verified via tools/fetch_source.py url). That is nine days, not ten. Fix the title and the sourcing_note."
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "2026-08-06/cpanel-whm-cve-2026-58048-database-root-privilege-escalation"
  url_or_quote: "and the Swiss NCSC put it on its own dashboard / That is why the Swiss NCSC placed it on its own Cyber Security Hub dashboard for its constituency"
  summary: "The entry's whole home-region nexus, stated in the headline and body, has no inline link and no NCSC-CH record in sources[]. The claim is TRUE — verified via `python3 tools/fetch_source.py ncsc-csh list`: post 12827, created 2026-08-05T07:36:30Z, TLP Clear, '[Advisory] cPanel: Database Privilege Escalation (CVE-2026-58048)'. Add the CSH per-post detail URL as a corroborating source and cite it at both places; do not remove the claim."
- code: F17
  category: classification
  section: incidents
  item: "2026-08-06/water-plc-lockouts-twelve-states-first-consumer-impact"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "The entry's own sourcing_note disclaims corroboration for its headline figure ('originates with ABC News and is relayed by both The Record and SecurityWeek rather than confirmed in a federal statement'), which is the one-assessor-several-publishers case the run record says it rated 2 on the Veeam and HPE Aruba entries. Set credibility: 2. (credibility: 1 on the CHAINDROP entry is correct — Elastic and OX Security are independent first-hand assessors.)"
- code: F11
  category: editorial-advisory
  section: whole-run
  item: "ATT&CK mapping precision on three entries"
  url_or_quote: "endlessdoors T1071.001 / litellm T1556 / teamcity techniques: [T1190]"
  summary: "(a) ENDLESSDOORS maps T1071.001 (Web Protocols) but VulnCheck describes a custom binary protocol on TCP 7000/7001 with no encryption, and the entry body itself says 'a high non-standard port' — T1071 parent or T1571 fits. (b) LiteLLM maps T1556 (Modify Authentication Process), a behaviour neither the body nor either source describes; the primary source publishes its own mapping including T1557 and T1565.002. (c) TeamCity dropped T1059, which the original 2026-07-29 entry carried and this body still describes ('the server process spawning command interpreters'). Advisory — main agent may leave."
```
