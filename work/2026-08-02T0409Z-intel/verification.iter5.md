**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-02T05:30:07Z · ended_at=2026-08-02T05:42:15Z · duration_seconds=728
**Self-telemetry:** urls_checked=10 (all cited source URLs) · webfetch_calls=2 · bridge_fetches=17 · websearch_calls=2

## Verification report — 2026-08-02T0409Z-intel (iteration 5)

Confirmation pass, read cold: no deltas supplied, no prior-iteration findings consulted before the truth pass.
All ten inline/frontmatter source URLs across the four entries were re-fetched live in this iteration
(`tools/fetch_source.py url` for nine; `WebFetch` for the GHSA, which 403s the bridge and cannot reach the jina
reader while the credential pool is exhausted). Every evidence quote was byte-compared against the raw page text.
The GHSA record was additionally cross-checked against the machine-readable mirror
(`raw.githubusercontent.com/github/advisory-database/.../GHSA-xr9x-r78c-5hrm.json`) for score, vector and the
three affected ranges. **I do not confirm the previous iteration's CLEAN.** Three defects survive, two of them
citation-accuracy defects that a summarising read would not surface.

### Citation does not support the claim

**F1 — `2026-08-02/adform-trackpoint-supply-chain-clipboard-crypto-clipper`: the vendor notice is cited with a
publication date four days earlier than the date the page itself carries.**

Frontmatter:

```
sources:
  - url: "https://site.adform.com/resources/newsroom/security-incident-company-update/"
    publisher: "Adform"
    date: "2026-07-27"
    role: primary
```

and the body renders that date three times — e.g. "it says it detected the activity on 2026-07-27, contained the
incident, removed the malicious code and reported it to the authorities ([Adform, 2026-07-27](https://site.adform.com/resources/newsroom/security-incident-company-update/))".

The page's own CMS payload carries exactly one publication field:

```
"publishedOn":"2026-07-31T19:00:00Z", ... "showPublishedOn":true, "meta":{"title":"Security Incident - Adform"...}
```

The same value is present in this run's own capture of the page (`work/2026-08-02T0409Z-intel/deepread/adform.txt`),
so this is not fetch drift. The page carries no visible dateline and no `datePublished`/`article:published_time`
meta tag, so `publishedOn` is the page's own publication date. Corroborating: the Wayback availability API returns
no snapshot of that URL earlier than `20260801085109` when queried for `20260728`.

Drift is four days, well past the one-day UTC-rendering tolerance, so this is F3 under check 2(e). It is not
cosmetic here: the entry's central argument is that the vendor's single-affected-day framing is contested
("Two questions are openly contested and defenders should not resolve them in Adform's favour by default"). Dated
2026-07-27 the notice reads as a same-day first statement; dated 2026-07-31T19:00Z it is a statement published
*after* BleepingComputer's 2026-07-31 story and Beaumont's week-long claim were already public, which strengthens
rather than weakens the entry's own point. Fix: correct the `sources[].date` to `2026-07-31` and the three inline
citation labels. The same date also propagates into `entities/registry.yaml`
(`incident:adform-supply-chain-crypto-clipper-2026-07` summary ends "(Adform, 2026-07-27; BleepingComputer,
2026-07-31; The Hacker News, 2026-08-01)"). `event_date: "2026-07-27"` is correct as-is — that is the incident
date and matches the store's incident-entry convention.

**F2 — `2026-08-02/cci-nice-cote-dazur-edrh-admin-account-export-breach`: an assessment made by the reporting
outlet is attributed to the victim organisation.**

Entry, paragraph 2:

> "The chamber says it engaged technical measures with its service provider on detection to end the unauthorised
> access and secure the platform, **and states that nothing disclosed supports a conclusion that its wider IT
> estate was compromised**; it does not say how long the account remained accessible or how many exports ran
> before it was blocked ([Cyberattaque.org, 2026-08-01](https://www.cyberattaque.org/cci-nice-cote-dazur-un-compte-administrateur-pirate-les-donnees-rh-de-candidats-exportees/))"

The first clause is supported — the article says "la CCI Nice Côte d'Azur indique avoir engagé des mesures
techniques avec son prestataire afin de mettre fin à l'accès non autorisé et de sécuriser la plateforme". The
bolded clause is not. Its basis is this sentence, which sits in the outlet's own descriptive section ("Une
plateforme RH gérée par la CCI Nice Côte d'Azur"), immediately after "L'incident concerne cet environnement
spécifique", and is framed as the outlet reasoning about what the chamber has *not* said:

> "Aucun élément communiqué ne permet d'affirmer que l'ensemble du système informatique de la Chambre de commerce
> a été compromis."

("No communicated element allows one to affirm that the chamber's entire IT system was compromised.") The
corroborating tracker does not carry the claim either: FrenchBreaches' "Ce qui reste à confirmer" list has
"Les circonstances techniques ayant permis l'accès non autorisé" and makes no wider-estate statement at all. The
entry therefore turns an absence-of-information observation by a breach tracker into a reassurance issued by the
victim — the same over-attribution class the run already corrected once on the Adform entry. Fix: reattribute the
clause to the relaying outlet (or drop it), e.g. "…and neither tracker's account contains anything establishing
whether the chamber's wider IT estate was affected".

### Unsupported / hallucinated facts

**F3 — `2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling`: the secret-rotation scope binds the
decryption relationship to the wrong key and under-scopes the advisory's own rotation list.**

Body (defender takeaway): "Because the flaw yields `secret_key_base` **and the credentials it decrypts**, an
application that was internet-reachable … is a key-rotation candidate, not merely an upgrade candidate".

`actions[0]`: "… **and rotate secret_key_base and the credentials it decrypts** for any application the exploited
skill flags — the patch does not invalidate a key that was already read."

No cited source states that `secret_key_base` decrypts the credentials. The GHSA cited by this entry
(fetched this iteration; identical text in the advisory-database mirror) assigns that role to a different key and
lists five rotation classes:

> "- `secret_key_base`
>  - The master key, whether stored in `config/master.key` or supplied as `RAILS_MASTER_KEY`, along with
>    everything in `config/credentials.yml.enc` **that it decrypts**
>  - Credentials for the Active Storage service, such as S3, GCS, or Azure keys
>  - Database credentials
>  - Tokens and keys for any third-party service the application calls"

The entry's predecessor got this right ("secret_key_base, the master key and everything `credentials.yml.enc`
decrypts, storage and database credentials and third-party tokens"), so this is a regression introduced in the
update. Two consequences: (a) a factual error visible to the Rails-fluent reader this brief writes for —
`credentials.yml.enc` is decrypted by the master key, while `secret_key_base` derives cookie/message-encryptor
keys; (b) the action item — which is what lands in the rendered brief's aggregated § Action Items — tells a team
whose forensic run came back positive to rotate a scope narrower than the advisory demands, omitting the master
key, storage/database credentials and third-party tokens. Fix: mirror the advisory's own list in both places
(one clause is enough: "rotate `secret_key_base`, the master key and everything `credentials.yml.enc` decrypts,
plus storage, database and third-party credentials reachable from the process").

### Checks that passed (recorded so the next iteration need not redo them)

- **URL liveness and specificity (10/10).** Rails Discourse thread, GHSA advisory, Adform notice, The Hacker News,
  BleepingComputer, Coinkite backgrounder, CryptoTimes, Block Engineering, Cyberattaque.org, FrenchBreaches — all
  resolve, all are specific article/advisory/vendor-post URLs, none is a homepage, listing or NVD/MITRE page. No
  `closed_sources` on any entry, so no drop-file checks apply.
- **Evidence quotes (10/10 contiguous verbatim).** Two near-misses were run down to ground truth rather than
  reported: the Coinkite `#ifndef` quote differs from my extraction only because the page wraps `#ifndef` in a
  code element (rendered text matches exactly), and the Cyberattaque quote differs only in apostrophe glyph
  (U+2019 → ASCII), which is house typographic normalisation, not a splice.
- **CVE authority cross-check.** CVE-2026-66066: CVSS 9.5 / `CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H`,
  and all three affected ranges (`<7.2.3.2`; `>=8.0.0.beta1 <8.0.5.1`; `>=8.1.0.beta1 <8.1.3.1`) plus the
  `libvips >= 8.13` condition confirmed against the advisory that owns the record and its machine-readable mirror.
  `vector: zero-click` / `auth: pre-auth` consistent with `UI:N`/`PR:N`. The other three entries carry no `cves[]`.
- **Adjacency sweep, per citation.** Every inline citation on all four entries was checked against its own clause.
  Notably confirmed rather than flagged: the Discourse-maintainer paragraph in the Rails entry (Sam Saffron's
  2026-08-01 reply in the same thread — the ImageMagick/allowed-coder and Landlock "write to 1 spot" details are
  all on the cited page, and the entry's caveat that this is about the attack *class* is warranted by the same
  post); the "agent skill, not a script" distinction (verified against `github.com/rails/rails-forensics-CVE-2026-66066`,
  which carries `skills/` with `SKILL.md` entry points); the Galaxy Research wave-3 figures, 27-hour spacing,
  output-type differences, unspent-funds observation and March-2021 firmware date (all in the CryptoTimes relay,
  correctly attributed as a relayed estimate); BleepingComputer's archived-snapshot time of 23:29 GMT on
  2026-07-26; THN's "The public timeline is unresolved."; and the 1,800-customers / 180-countries figures, which
  the entry correctly carries with THN's own "describe the platform, not this incident" hedge.
- **Citation dates.** CryptoTimes is dated 2026-08-01 in the entry while its URL slug reads `/2026/08/02/`; its
  `datePublished` is `2026-08-02T02:06:51+05:30` = 2026-08-01T20:36Z, so the entry's UTC date is right. Rails
  thread 2026-07-31 (post timestamp 12:51am), GHSA 2026-07-29, BleepingComputer 2026-07-31, THN 2026-08-01,
  Cyberattaque 2026-08-01T07:00Z, FrenchBreaches 2026-07-31T20:04+02:00 — all match. Only the Adform record (F1)
  drifts.
- **Quantifiers (F14), analytical links (F13), name collisions (F15).** None found. "five years", "two days
  rather than four weeks", "1,367.05 BTC across 4,585 addresses", "roughly a week", "about 40 bits"/"about 72 bits"
  all trace to a cited source or to arithmetic on two cited dates. No comparative superlative survives on the
  COLDCARD entry. No proper noun in this run collides with a differently-scoped entity in the 14-day index.
- **Dedup / update discipline.** The 121-record prior-coverage index contains exactly one overlapping record
  (`2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read`), which is the update target; the update
  carries only the delta (embargo collapse, forensic repository, Discourse reply) and does not re-tell the
  original. Adform, COLDCARD and CCI Nice appear nowhere in the index or elsewhere in the store.
- **Classification / org-triage / watchlist.** All four entries carry a valid Admiralty block and `org_triage: null`,
  as the profile requires (no triage scheme, no watchlists). A/2 on the single-source first-party Rails update,
  A/1 on the two multi-source first-party-primary entries, C/2 on the tracker-sourced chamber entry — each
  consistent with the corroboration actually shown. No `watchlist_hit: true`, no `watchlist` tag.
- **Single-source flags (F12).** Rails update: `verification: single-source` + sourcing_note explaining that a
  maintainer statement is not one of the named carve-outs + matching run-record line. CCI: `single-source` +
  sourcing_note stating both trackers reproduce one notification + matching run-record line. Both correct.
- **Priority calibration.** No entry claims `critical`; nothing here clears the stop-and-act-now bar (Rails is
  patched with a public chain, Adform is contained, COLDCARD is out-of-nexus, CCI is a notification). The two
  `high` values are TL;DR-worthy; the two `notable` values are not under-alerting.
- **Actions (F18).** Two entries carry one concrete, self-contained action each, both derived from their own
  mechanics; two carry `actions: []`, which is the correct output for an out-of-nexus lesson entry and for a
  notification-only breach. No generic advice, no body restatement, no padding. (The Rails action's rotation
  *scope* is F3 above, not an F18 discipline defect.)
- **Style.** No IOCs (the entry omits the C2 address both outlets published, and `s2.adform.net` is the legitimate
  vendor host, not an attacker domain); no vanity metrics presented as findings; English throughout; no
  workflow-internal vocabulary in any entry body or in the run record's reader-facing notes.
- **Completeness.** Checked independently: CISA KEV catalog version 2026.07.29 with no addition after
  CVE-2026-20316 (2026-07-29, already covered 2026-07-30); NCSC-CH's freshest post is 2026-07-31T12:06Z (IBM
  WebSphere, already covered); BleepingComputer, The Hacker News and SecurityWeek feeds show only four in-window
  substantive items — Rails, Adform, COLDCARD and the hotel captive-portal cluster (already published
  2026-08-01 as CaptiveCrunch). The one in-window item the run neither published nor logged is THN's
  2026-08-01T07:12Z Adobe Campaign Classic story (CVE-2026-48449, CVSS 10.0, plus eight Adobe Bridge CVEs); I am
  **not** raising it as F10 because Adobe states it is not aware of exploitation, no PoC is reported, and the
  product is not exposed-edge infrastructure — it is exactly the routine-patch-cycle CVE the inclusion gate
  excludes. Coverage of this window looks complete.
- **Run record.** Telemetry internally consistent (eight reader-credential failures plus one HTTP 503 with the
  reader never attempted — I re-counted the `fetch_failures` block and the prose matches); the borderline-include
  and drop rationales hold; the contradiction paragraph accurately carries both open disagreements; the
  "first reported roughly five hours before this window opened" claim checks out against BleepingComputer's
  2026-07-31 21:09Z publication versus the 2026-08-01T02:09Z window start.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: incidents
  item: "2026-08-02/adform-trackpoint-supply-chain-clipboard-crypto-clipper"
  url_or_quote: "https://site.adform.com/resources/newsroom/security-incident-company-update/ — sources[].date: \"2026-07-27\""
  summary: "Citation date is four days earlier than the page's own publication date. The notice's CMS payload carries \"publishedOn\":\"2026-07-31T19:00:00Z\" (same value in this run's deepread/adform.txt capture), there is no visible dateline or datePublished meta tag, and Wayback holds no snapshot before 20260801085109. Correct sources[].date and the three inline [Adform, 2026-07-27] labels to 2026-07-31; the same date is repeated in entities/registry.yaml under incident:adform-supply-chain-crypto-clipper-2026-07. event_date 2026-07-27 is correct and should not change."
- code: F3
  category: claim-not-supported
  section: incidents
  item: "2026-08-02/cci-nice-cote-dazur-edrh-admin-account-export-breach"
  url_or_quote: "\"The chamber says it engaged technical measures with its service provider on detection to end the unauthorised access and secure the platform, and states that nothing disclosed supports a conclusion that its wider IT estate was compromised\""
  summary: "The second clause is the reporting outlet's observation, not the chamber's statement. Cyberattaque.org writes it in its own descriptive section as 'Aucun élément communiqué ne permet d'affirmer que l'ensemble du système informatique de la Chambre de commerce a été compromis' — an absence-of-information note about what the chamber has not said. FrenchBreaches makes no such statement either. Reattribute to the relaying outlet or drop the clause; the first clause is correctly sourced."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling"
  url_or_quote: "\"Because the flaw yields `secret_key_base` and the credentials it decrypts\" (body) / \"rotate secret_key_base and the credentials it decrypts\" (actions[0])"
  summary: "No cited source says secret_key_base decrypts the credentials. GHSA-xr9x-r78c-5hrm assigns that to the master key ('The master key, whether stored in config/master.key or supplied as RAILS_MASTER_KEY, along with everything in config/credentials.yml.enc that it decrypts') and lists five rotation classes, of which the entry names one and a half. The predecessor entry stated it correctly, so this is an update regression, and it under-scopes the single action item that reaches the aggregated task list. Mirror the advisory's list in both the takeaway and the action."
```
