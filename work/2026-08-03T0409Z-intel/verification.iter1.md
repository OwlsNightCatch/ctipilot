**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-03T04:51:45Z · ended_at=2026-08-03T05:04:04Z · duration_seconds=739
**Self-telemetry:** urls_checked=14 · webfetch_calls=6 · bridge_fetches=9 · websearch_calls=3

## Verification report — 2026-08-03T0409Z-intel (iteration 1)

Read cold. Both entries and the run record read end-to-end. Every cited URL in both entries fetched
live this iteration (WebFetch for n-able.com and the GitHub wiki; `tools/fetch_source.py url` where a
rendered page was needed). All 32 Bouncy Castle CVE ids, CVSS scores and one-line notes cross-checked
against the numbering authority's own records and against the official release notes' § 2.2.4 Security
Fixes list; both N-able CVEs cross-checked against the CNA record (score, CWE, affected range,
Exploitation Maturity). All eight `techniques[]` ids validated against the pinned ATT&CK 19.1 dataset
(all active, none revoked/deprecated). All eight `evidence[]` quotes verified as contiguous verbatim
substrings of a page fetched this iteration. Prior-coverage index (128 records) and
`state/cves_seen.json` (740 records) checked for both entries' CVEs and products — no prior coverage,
so `update_of: null` is correct on both.

**What checked out and is worth recording, because it is the kind of thing that usually fails:**

- The Bouncy Castle entry's final-paragraph sourcing caution is **correct and I nearly flagged it as
  fabricated**. `WebFetch` on `https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9058062`
  returned the *stapled-OCSP* write-up, which would have made the entry wrong. Re-fetching the same URL
  through the bridge returned the actually-rendered page, whose body reads "**Title:** BCFKS keystore
  load honours unbounded KDF cost from untrusted file." — i.e. the CVE-2026-58063 write-up, exactly as
  the entry says. The raw wiki markdown at `raw.githubusercontent.com/wiki/…/CVE‐2026‐58062.md` carries
  the OCSP text, so raw and rendered genuinely diverge on that slug. Verified in both directions.
  No finding.
- The three cited wiki slugs (59638, 8763, 59650) all render the content the entry attributes to them.
- Release notes § 2.2.1 reads "Release: 1.85, 1.85.1 / Date: 2026, July 12th" — the 12 July date holds.
- § 2.2.4 lists exactly the 32 ids in the entry's `cves[]`, no more and no fewer. The "32" quantifier,
  the "four rated critical" count (58062 / 59638 / 59650 / 8763, all CVSS 4.0 9.3) and the "around
  fourteen more … integrity and authenticity bypasses" split all hold against the source.
- CVE-2026-18577: CNA CVSS 4.0 8.2, vector carries `E:A`, CWE-288, affected through 2026.3.1, unaffected
  from 2026.3.1.7 — every value in `cves[]` matches. Same for CVE-2026-18556 (8.2, CWE-288, through 2026.1).
- No IOCs leaked. Both sources the entries cite are dense with IPs and attacker domains (N-able lists six
  IPs, Huntress lists four IPs plus three hostnames) and none reached either entry. The Take Control log
  directory and the `Cloudflared` service name are legitimate-product artifacts, not IOCs.
- `priority: critical` on the N-able entry clears the bar: vendor-confirmed in-the-wild exploitation
  (`E:A` in the CNA vector), disclosed inside the window, patch released 2 August, and the day-one
  remediation path was itself bypassable — action is time-critical to the day. Not a false critical.
- KEV telemetry in the run record is accurate: catalogue version 2026.07.29, latest `dateAdded`
  2026-07-29, no N-central 2026 entry. The 2025 N-central KEV pair (CVE-2025-8875/8876) is real, which
  corroborates the "recycled-news trap" note.
- The Stadler Rail item the research pass touched (technadu, 270k-file Everest leak) is *not* a missed
  angle — it is already covered by `2026-07-31/everest-publishes-stadler-rail-supplier-archive`. Dedup
  worked.
- Alcon and CEN/CENELEC were correctly dropped: leak-site-tracker-only sourcing, no victim statement,
  no high-reliability reporting. Amgen correctly dropped: out of window and no actionable mechanics.

### Citation does not support the claim

**F3-a — N-able entry: hosted instances described as already upgraded; the cited status page says the
upgrade is scheduled, not done.**

`immediate_action.action` states:

> "only 2026.3.1.7 closes it, and N-able upgraded its hosted instances automatically."

and `actions[0]` repeats it:

> "hosted instances were upgraded by N-able automatically."

The entry's own source #2, `https://status.n-able.com/2026/08/02/n-central-2026-3-hotfix-1-mitigation-for-cve-2026-18577/`
(fetched this iteration), says in its Additional Information block:

> "Hosted N-central – Upgrade will be applied automatically
>  If you are on a N-central hosted instance (NCOD), you will be notified directly of the upgrade
>  schedule for your server, and you do not need to do anything at this time."

Future tense, and explicitly a *schedule* the customer has yet to be notified of. Neither the status page
nor the N-able blog states that any hosted instance has already been upgraded. An MSP on NCOD reading the
entry concludes it is already patched; the vendor is telling it the upgrade is pending. Fix: match the
source's tense ("N-able is applying the upgrade to hosted (NCOD) instances automatically on a schedule it
notifies customers of directly").

**F3-b — Bouncy Castle entry: FIPS fixed-build list omits `bc-fips 1.0.2.7`, which the cited CVE page names.**

Body ¶3 states:

> "the FIPS modules carry their own per-module fixed builds — bc-fips 2.0.2 and 2.1.3 for the provider
>  flaws, bctls-fips 1.0.24, 2.0.24 and 2.1.24 for the JSSE hostname issue."

The entry's own source #3, `https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%908763`
(fetched this iteration, rendered page and raw markdown agree), states:

> "**Fixed versions:** BC 1.85, BC-LTS 2.73.12, BC-FJA bc-fips 1.0.2.7, 2.0.2 and 2.1.3."

`bc-fips 1.0.2.7` is missing from the entry. The omission is asymmetric — the entry *does* carry the
1.0.x build for the bctls-fips side (1.0.24), so a reader will read the bc-fips list as complete and an
estate on the bc-fips 1.0.x FIPS branch will conclude no fixed build exists for CVE-2026-8763, one of the
four criticals the entry leads on. (The 58063 page independently names bc-fips 1.0.2.7 too; only the
OCSP flaw, 58062, legitimately has no 1.0.x fixed build, because it was introduced in 1.66.)
Fix: "bc-fips 1.0.2.7, 2.0.2 and 2.1.3 for the provider flaws".

### Unsupported / hallucinated facts

**F4-a — Bouncy Castle entry: CVE-2026-59650 is framed as a certificate-validation bypass in the title,
headline, summary and body; its cited write-up describes a Diffie-Hellman key-agreement flaw with no
certificate involvement.**

Four places assert the framing:

- title: "four of them certificate-validation bypasses rated critical"
- headline: "four defeat TLS/PKIX certificate validation"
- summary: "Four are rated critical, and each independently defeats a distinct certificate-validation
  guarantee: … an MTI/A0 Diffie-Hellman agreement that exponentiates an unvalidated peer value …"
- body ¶2: "they are not variations on one bug: each removes a different guarantee from certificate-chain
  validation."

The entry's own source #4, `https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059650`
(fetched this iteration), describes something else entirely: `DHAgreement.calculateAgreement(pub, message)`
in the MTI/A0 two-pass variant exponentiates a peer-supplied wire value with the local **static private
key** without range or subgroup-membership checks, and "each exchange leaks x mod r for some small prime
r; combining these via CRT recovers the full static private key (Lim–Lee 1997)". That is small-subgroup
confinement against a static DH key. The page mentions no certificate, no chain, no PKIX, no OCSP, no
SAN, and no TLS. The entry itself concedes the point two paragraphs later, where ¶4 lists "the
OCSP-binding, Diffie-Hellman and name-constraint flaws" as three distinct things.

Three of the four criticals (58062 OCSP binding, 59638 CN fallback, 8763 name constraints) genuinely are
certificate-validation bypasses; the fourth is not, and the unifying claim is the entry's own analysis
presented as if the sources supported it. Fix: say "three of the four independently defeat a distinct
certificate-validation guarantee; the fourth recovers a static Diffie-Hellman private key" and adjust the
headline accordingly (the "four defeat TLS/PKIX certificate validation" headline is the version that
fires in the rendered TL;DR).

**F4-b — N-able entry: headline and summary assert two patches inside 48 hours and date the 2026.2 fix to
1 August; the body says otherwise and so do the sources.**

headline:

> "N-able patches an exploited N-central auth bypass twice in 48 hours; the first fix left customers still exposed"

summary:

> "The 1 August fix (CVE-2026-18556, fixed in 2026.2) was incomplete…"

What the sources say. The N-able blog (source #1, fetched this iteration) describes the 2026.2 fix as
already historical — "our analysis of a previously addressed vulnerability (CVE-2026-18556), which was
fixed in 2026.2" — and describes the 1 August action as an advisory plus a recommendation, not a patch:
"Yesterday, N-able posted an advisory to our Uptime Page … We had addressed this issue in later builds
and were recommending that customers on older versions upgrade to version 2026.3 as an immediate
protective measure." N-able's own status archive dates the 2026.x train well before August: "Announcing
the GA of N-central 2026.3" is posted 2026-06-30 (`https://status.n-able.com/category/n-central/`,
fetched this iteration), and the hotfix note itself says 2026.3.0 "was release on 'July 30th 2026'", so
2026.2 necessarily predates both. Only one patch — the 2026.3.1.7 hotfix of 2 August — was issued inside
any 48-hour window.

The entry's own body gets this right: "N-able first addressed the issue in 2026.2 and, on 1 August, told
customers still on older builds to move to 2026.3 as an immediate protective measure." So this is a
frontmatter⇔body contradiction in the two fields that render most prominently. Fix the headline to what
actually happened (the day-one remediation path was bypassable and a second CVE plus hotfix followed
within a day) and drop "The 1 August fix" from the summary in favour of the body's accurate sequencing.

**F4-c — Run record: the Bouncy Castle entry is described as citing six URLs; it cites four.**

Run-record § Sourcing notes:

> "The Bouncy Castle entry ships as `single-source` despite citing six URLs"

The entry's `sources[]` carries four records: the release-notes document plus the three per-CVE wiki
pages (59638, 8763, 59650). The count is simply wrong, and the run record is published. (The
`single-source` call itself is correct and well argued — one assessor, several publishers — and the
`sourcing_note` and `credibility: 2` are consistent with it. Only the number is wrong.)

### Claims missing inline citation

**F5-a — N-able entry: the "31 July" exposure boundary is used twice as an operational trigger and is
never cited or explained anywhere in the body.**

`immediate_action.action`:

> "treat any instance that was internet-reachable since 31 July as a compromise-assessment target"

body § Defender takeaway:

> "Any organisation whose managed estate ran a vulnerable N-central instance since 31 July owes itself a
>  compromise assessment of the managed endpoints, not just an upgrade of the server."

31 July appears nowhere else in the entry, carries no citation, and the reader is given no basis for it.
It is supportable — the N-able blog's Background section says "On July 31, 2026, N-able saw an increase
in licensing issues for our on-premises N-central customers … the volume was high and the engineering and
security teams were engaged" — but that sentence is the entry's whole justification for a scoping decision
and it is invisible to the reader. Fix: state the basis once in the body with the N-able citation
attached (the licensing-anomaly spike is the earliest vendor-observed signal), then the two uses inherit it.

**F5-b — Bouncy Castle entry: body ¶4 names two configuration mitigations and carries no citation at all.**

> "Two interim levers exist before a full upgrade — the JSSE hostname CN-fallback property set explicitly
>  to `false` for CVE-2026-59638, and the strict-DigestInfo property for CVE-2026-12860 — while the
>  OCSP-binding, Diffie-Hellman and name-constraint flaws have no configuration toggle and require the
>  version bump."

The whole of ¶4 is uncited. Both properties are real — the cited release notes carry
`"org.bouncycastle.pkcs1.strict_digestinfo" (also exposed as Properties.PKCS1_STRICT_DIGESTINFO)`, which
"lets callers opt in to strict RFC 8017 Appendix A.2.4 enforcement when verifying RSA PKCS#1 v1.5
signatures", and the CVE-2026-59638 page carries `JSSE_HOSTNAME_CHECK_CN_FALLBACK` — so this is a
sourcing gap, not a factual one. But `actions[1]` turns the CN-fallback property into a do-now task, and
a mitigation instruction with no link is the wrong thing to leave unsourced. Fix: attach the release-notes
citation to the DigestInfo clause and the 59638 citation to the CN-fallback clause.

### Surface contradiction

**F9 — N-able: the vendor's two primary sources disagree on whether build 2026.3.1 is affected, and the
entry smooths it over instead of surfacing it.**

- Status page (source #2): "N-able was recently made aware of a security issue affecting all N-central
  instances **not running 2026.3.1** (CVE-2026-18577)" — reads as 2026.3.1 being safe.
- N-able blog (source #1): "an attacker had identified a vulnerability on all N-central servers running a
  version **prior to 2026.3.1.7**" — reads as 2026.3.1 being vulnerable.
- CNA record for CVE-2026-18577: affected "through 2026.3.1", unaffected from 2026.3.1.7 — agrees with
  the blog.

The entry silently picks the correct reading and paraphrases the status page as "N-able's status notice
states the issue affects all instances not already on the fixed train", which is a paraphrase that hides
the discrepancy. For an MSP sitting on 2026.3.1 this one digit is the whole decision. Fix: keep the
correct reading and add a short contradiction note (the status notice's "not running 2026.3.1" phrasing
understates the affected range relative to the vendor's own blog and the CVE record; treat 2026.3.1.7 as
the only fixed build), and record it in the run record's § Verification Notes.

### Missed angles

**F10 — Gladinet CentreStack (CVE-2026-54363 / -54367 / -54368) is uncovered store-wide and was deferred
to the weekly audit rather than published.**

I verified the run record's own account of this and it is accurate in every particular: the three ids are
absent from `state/cves_seen.json` (740 records) and from the 14-day dedup index (128 records); the CNA
scores are 9.3 / 8.8 / 8.7 on CVSS 4.0 as stated; and Gladinet products have reached the KEV catalogue
exactly four times (CVE-2025-30406, CVE-2025-11371, CVE-2025-12480, CVE-2025-14611). A specific,
non-blocked primary exists and resolves — `https://www.vulncheck.com/advisories/centrestack-hardcoded-key-token-forgery-rce`,
dated 2026-07-30, which describes the static `SysNumber` entropy, token forgery against privileged API
endpoints, and "a complete unauthenticated remote code execution chain", fixed in CentreStack 17.5.

I searched for an in-window development that would reset the clock and found none: no 2026 CentreStack
entry in the KEV catalogue, and no exploitation report dated 2–3 August. So the recency rule is correctly
applied on its own terms. The problem is the outcome, not the reasoning: an internet-facing file-sharing
platform with a hardcoded key that forges administrator tokens, from a vendor with four prior KEV
listings, has now been passed over by three consecutive intel runs, and deferring it to the trailing-window
audit leaves a reader who relies on this brief alone blind to it for up to another week. That is exactly
the false-negative the completeness half of the gate exists to prevent, and a three-day-old first
publication is not "recycled news" — it has never been published here at all.

Recommendation: publish it in this run as a new `vulnerability` entry with honest dating (primaries dated
2026-07-30, surfaced now because the store carries no prior coverage), primary = the VulnCheck advisory
per CVE, and note the absence of confirmed exploitation. If the main agent judges the window rule
controlling, that is a defensible call — but then say so in the run record as a deliberate editorial
decision rather than as a gap handed to the audit. Suggested query if a second source is wanted:
`Gladinet CentreStack 17.5 CVE-2026-54363 hardcoded key token forgery advisory`.

Also noted, non-blocking: the CentreStack bundle appears to include a fourth id, CVE-2026-54365
(unauthenticated account creation via `jsonimportuserbyupn`), which the run record's out-of-window line
does not list. Worth carrying into whatever recovers this item.

### Editorial / less-is-more flags (advisory)

**F11-a — Run record § Operational note uses workflow-internal vocabulary the style rule excludes from
run-record prose.**

> "The first attempt at all four research **sub-agents** terminated on a safeguard error … The **spawn
>  messages** carried long inline recaps … **Re-spawning** with that context moved out of the prompt and
>  into a file the agents read … Worth folding into the research-agent **spawn** contract if it recurs."

The same record's own house style elsewhere is "the research pass" ("The home-region research pass
initially set it aside…", "The research pass fetched CEN-CENELEC's own news listing directly"), and I
checked the run records from 2026-07-2x and 2026-08-0x — none of them uses "sub-agent" or "spawn" in
prose. The operational lesson is worth keeping; only the vocabulary needs to change (e.g. "the four
research passes failed to start on the first attempt because their briefing carried long inline recaps of
prior coverage; re-issuing them with that context passed by file path succeeded immediately").

**F11-b — `state/cves_seen.json` records an NVD per-CVE URL as `primary_source_url` for both N-able CVEs,
contradicting the entry's own primary.**

> `"CVE-2026-18556" … "primary_source_url": "https://nvd.nist.gov/vuln/detail/CVE-2026-18556"`
> `"CVE-2026-18577" … "primary_source_url": "https://nvd.nist.gov/vuln/detail/CVE-2026-18577"`

The entry's `sources[0]` is `https://www.n-able.com/blog/n-central-security-update-august-2-2026`. The
field is documented as "URL of the primary source at first reference", and the entry deliberately avoids
NVD; the index now disagrees with the entry it was derived from, and a future run's dedup lookup surfaces
the NVD page. 14 of 740 records store-wide carry NVD URLs here, so this is drift rather than convention —
and 2 of those 14 are this run's. The 32 Bouncy Castle records correctly carry the release-notes URL.
Not blocking; worth a one-line correction while the run is still open.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 4, advisory: 2)

Truth: F3-a, F3-b, F4-a, F4-b, F4-c. Editorial: F5-a, F5-b, F9, F10. Advisory: F11-a, F11-b.

Both entries are genuinely relevant, well-sourced against real primaries, correctly deduped, correctly
prioritised and free of IOCs, marketing tells and hallucinated identifiers — the 32-CVE block in
particular survives a full id-by-id, score-by-score cross-check against the numbering authority, which is
not the usual outcome. The blocking defects are concentrated in derived text rather than in the research:
one analytical over-generalisation that reached four fields of the Bouncy Castle entry (F4-a), one
headline/summary sequencing error that the entry's own body contradicts (F4-b), two version/tense
precision losses against pages the entries themselves cite (F3-a, F3-b), and a run-record miscount
(F4-c). Coverage is complete for the window with the single exception argued at F10.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-18556 / CVE-2026-18577 — N-able N-central"
  url_or_quote: "N-able upgraded its hosted instances automatically / hosted instances were upgraded by N-able automatically"
  summary: "Cited status page says 'Hosted N-central - Upgrade will be applied automatically' and 'you will be notified directly of the upgrade schedule for your server' - scheduled future, not completed past. Rephrase to the source's tense in immediate_action.action and actions[0]."
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "Bouncy Castle for Java 1.85 — 32 CVEs"
  url_or_quote: "the FIPS modules carry their own per-module fixed builds — bc-fips 2.0.2 and 2.1.3 for the provider flaws"
  summary: "Cited source https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%908763 states 'Fixed versions: BC 1.85, BC-LTS 2.73.12, BC-FJA bc-fips 1.0.2.7, 2.0.2 and 2.1.3'. bc-fips 1.0.2.7 is omitted, so a bc-fips 1.0.x estate reads the list as having no fix for one of the four criticals. Add 1.0.2.7."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "Bouncy Castle for Java 1.85 — 32 CVEs"
  url_or_quote: "four of them certificate-validation bypasses rated critical / four defeat TLS/PKIX certificate validation / each independently defeats a distinct certificate-validation guarantee / each removes a different guarantee from certificate-chain validation"
  summary: "CVE-2026-59650 is not a certificate-validation flaw. Its cited page (https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902026%E2%80%9059650) describes MTI/A0 DHAgreement.calculateAgreement exponentiating an unvalidated peer value with the static private key, leaking 'x mod r for some small prime r' and recovering the static DH private key via CRT - small-subgroup confinement, no certificate, chain, PKIX or TLS mentioned. The entry's own body para 4 lists 'the OCSP-binding, Diffie-Hellman and name-constraint flaws' as distinct. Reframe as three certificate-validation bypasses plus one static-DH private-key recovery, in title, headline, summary and body para 2."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CVE-2026-18556 / CVE-2026-18577 — N-able N-central"
  url_or_quote: "N-able patches an exploited N-central auth bypass twice in 48 hours / The 1 August fix (CVE-2026-18556, fixed in 2026.2) was incomplete"
  summary: "Only one patch (hotfix 2026.3.1.7, 2 August) was issued inside 48 hours. N-able's blog calls 2026.2 'a previously addressed vulnerability ... fixed in 2026.2' and describes 1 August as an advisory plus a recommendation to upgrade to 2026.3, not a fix; N-able's status archive dates the 2026.3 GA to 2026-06-30 and 2026.3.0 to 30 July, so 2026.2 predates 1 August by months. The entry's own body states the sequence correctly - this is a frontmatter-vs-body contradiction in headline and summary."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "Run record § Sourcing notes"
  url_or_quote: "The Bouncy Castle entry ships as `single-source` despite citing six URLs"
  summary: "The entry's sources[] carries four records (release notes + wiki pages for 59638, 8763, 59650). Correct the count to four. The single-source call itself is correct and well argued."
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "CVE-2026-18556 / CVE-2026-18577 — N-able N-central"
  url_or_quote: "treat any instance that was internet-reachable since 31 July as a compromise-assessment target / ran a vulnerable N-central instance since 31 July"
  summary: "31 July is used twice as the compromise-assessment scoping boundary and is never cited or explained in the body. Supportable from the N-able blog's Background ('On July 31, 2026, N-able saw an increase in licensing issues for our on-premises N-central customers') - state the basis once in the body with that citation attached."
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "Bouncy Castle for Java 1.85 — 32 CVEs"
  url_or_quote: "Two interim levers exist before a full upgrade — the JSSE hostname CN-fallback property set explicitly to `false` for CVE-2026-59638, and the strict-DigestInfo property for CVE-2026-12860"
  summary: "Body para 4 is entirely uncited while naming two configuration mitigations, one of which actions[1] turns into a do-now task. Both are real: the cited release notes carry 'org.bouncycastle.pkcs1.strict_digestinfo (also exposed as Properties.PKCS1_STRICT_DIGESTINFO)' and the 59638 page carries JSSE_HOSTNAME_CHECK_CN_FALLBACK. Attach the release-notes citation to the DigestInfo clause and the 59638 citation to the CN-fallback clause."
- code: F9
  category: surface-contradiction
  section: trending-vulnerabilities
  item: "CVE-2026-18556 / CVE-2026-18577 — N-able N-central"
  url_or_quote: "N-able's status notice states the issue affects all instances not already on the fixed train"
  summary: "Status page says 'affecting all N-central instances not running 2026.3.1'; the N-able blog says 'prior to 2026.3.1.7' and the CNA record says affected 'through 2026.3.1', unaffected from 2026.3.1.7. The entry silently picks the correct reading and paraphrases the discrepancy away. Keep the correct reading, add a Contradiction line to the entry and to the run record's verification notes - for an MSP on 2026.3.1 the one digit is the whole decision."
- code: F10
  category: missed-angle
  section: coverage
  item: "Gladinet CentreStack — CVE-2026-54363 / -54367 / -54368"
  url_or_quote: "https://www.vulncheck.com/advisories/centrestack-hardcoded-key-token-forgery-rce"
  summary: "Verified uncovered store-wide (absent from cves_seen.json and the 14-day index), CNA scores 9.3/8.8/8.7 as the run record states, vendor has four prior KEV listings, and a specific non-blocked primary dated 2026-07-30 resolves and describes 'a complete unauthenticated remote code execution chain' fixed in 17.5. No in-window development found (no 2026 CentreStack KEV entry, no 2-3 August exploitation report), so the recency rule is correctly applied - but three consecutive intel runs have now passed over it and deferring to the weekly audit leaves the reader blind for another week. Publish as a new vulnerability entry with honest 2026-07-30 dating, or record the omission as a deliberate editorial decision rather than an audit hand-off. Note the bundle appears to include a fourth id, CVE-2026-54365."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "Run record § Operational note"
  url_or_quote: "The first attempt at all four research sub-agents terminated on a safeguard error ... The spawn messages carried long inline recaps ... Re-spawning with that context ... the research-agent spawn contract"
  summary: "Workflow-internal vocabulary ('sub-agent', 'spawn') in published run-record prose. The same record's house style elsewhere is 'the research pass', and no run record from 2026-07-2x or 2026-08-0x uses these terms in prose. Keep the lesson, change the vocabulary."
- code: F11
  category: editorial-advisory
  section: state
  item: "state/cves_seen.json — CVE-2026-18556 / CVE-2026-18577"
  url_or_quote: "\"primary_source_url\": \"https://nvd.nist.gov/vuln/detail/CVE-2026-18556\""
  summary: "The index records an NVD per-CVE URL as primary_source_url for both N-able CVEs while the entry's sources[0] is the N-able vendor blog, which the entry deliberately chose over NVD. 14 of 740 records store-wide carry NVD URLs here (2 of them from this run), so this is drift rather than convention; the 32 Bouncy Castle records correctly carry the release-notes URL. Non-blocking."
```
