**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-07T05:41:35Z · ended_at=2026-08-07T05:59:09Z · duration_seconds=1054
**Self-telemetry:** urls_checked=21 · webfetch_calls=1 · websearch_calls=2 · bridge_fetches=24

## Verification report — 2026-08-07T0411Z-intel (iteration 3)

Cold read, odd-iteration rotation, no prior-iteration deltas block. All 8 entries read end-to-end
(frontmatter + body), plus the run record, `prior_coverage.json`, `entities/registry.yaml`,
`state/cves_seen.json`, the four `findings.S*.yaml`, `triage.json`, `completeness-watchlist.md`,
`url-liveness.tsv` and the ATT&CK pin.

**Every cited URL was fetched live in this iteration** via `tools/fetch_source.py url` (16 URLs, all
resolving to substantive bodies; Reuters returns a CAPTCHA shell to every rung including jina, so the
saved run-time jina body plus BleepingComputer's independent relay of the same Meta/Irregular
statements were used — this is not scored as a broken URL). Additionally fetched, not cited by any
entry, to test specific claims: `helpx.adobe.com/.../apsb26-114.html`, `advisories.ncsc.nl/2026/ncsc-2026-0273.html`,
Red Hat's Hydra JSON for four CVEs, the CISA KEV catalog, NCSC-CH's recent-posts API,
`bleepingcomputer.com/.../hedge-fund-cyberattacks-tied-to-blackfile-linked-unc6671-extortion-group/`
(WebFetch with the outbound-links template), and two WebSearch sweeps for in-window items.

### What I verified clean (recorded so the next iteration need not re-do it)

- **All 14 `cves[]` records checked against the owning authority, not the roundup.** Seven Keycloak
  scores against Red Hat's per-CVE Hydra records (7.4/7.4/8.8/8.1/8.1/5.4/6.5 — all exact, all
  `status: verified`), including `auth` mapping against each CVSS vector (`PR:N` → pre-auth on -16443/-16442,
  `PR:L` → post-auth on the rest). Seven Adobe rows against Adobe's own per-CVE table
  (10.0/10.0/10.0/9.9/9.8/9.6/7.5, CWE-918/1336/89/89/863/95/657, impact column, and `PR:N` vs `PR:L`
  → pre/post-auth) — every one exact, including the entry's correct reading that CVE-2026-48333 is a
  privilege escalation while the other pre-auth trio is arbitrary code execution. Zero of the 14 ids
  appear in `state/cves_seen.json`, so the new-vs-update decision is right on both entries.
- **Every `evidence[]` quote is a contiguous verbatim substring** of a page I fetched (18 records
  across 8 entries, checked by whitespace-normalised `in` test). The two inline body quotes that
  failed a naive test — GTIG's "by July 2026, the target profile narrowed…" and Microsoft's "because
  execution starts from a user-run Terminal command…" — differ only by a decapitalised leading letter
  for mid-sentence integration, which is conventional, not a splice.
- **The iteration-2 F4 remediation is correct and I could not break it.** Jamf's text reads: "Overlord
  was also used by UNK_DeadDrop, a cluster Proofpoint assesses as likely North Korean, though no direct
  overlap has been identified between that activity and this campaign. The Overlord variant observed
  here shares a LaunchAgent label (com.zoom) and plist name (com.zoom.plist) with FlexibleFerret, a
  DPRK-attributed macOS malware family associated with the Contagious Interview campaign and documented
  by SentinelOne in February 2025. … Jamf Threat Labs has noted the similarities but does not currently
  attribute this malware to a specific threat actor." The entry body, the `sourcing_note` and the
  `tool:overlord-rat` registry summary now each carry the two observations **separately**, each with its
  own qualifier, and close on Jamf's own non-attribution. No re-splice: the "developer-targeting"
  descriptor appears nowhere in `entries/` or `entities/registry.yaml`. And it does not overreach the
  other way — "the DPRK-adjacent context is a naming and tooling overlap rather than an attribution"
  states the absence of an attribution, not an exclusion of a DPRK link. **No IOC was introduced**: the
  literal `com.zoom` / `com.zoom.plist` strings appear in no entry (grep-confirmed), only the abstract
  "shares its LaunchAgent label and plist name".
- **Deep-dive fidelity.** Every load-bearing GTIG number and claim traced to its sentence: 18 wallets /
  141.65 BTC / ≈$10.69M / 2026-01-07→05-12 / payments past the 2026-05-11 shutdown notice / cash-outs late
  April–early May; $1M–$3M initial demands reduced 50–75%; "in over 53% of tracked cases … averaged
  $750,000 USD (~10.2 BTC)"; 1.6-days vs 2.2-days cadence (the 2.2 figure belongs to the April 1–May 31
  set of 28 root domains, and the entry attributes it to "the preceding two months" correctly); the
  Falcon/Helix shared-root-domain overlap; "identical code and design hosted simultaneously"; the
  April–May → June → July targeting progression sector-by-sector; the non-SSO password-reset and
  alert-deletion sequence; and every one of the five hardening levers the entry attributes to GTIG
  ("re-authentication at least once per work day", "IP session binding, Device-Bound Session
  Credentials", "defined network zones coming from known sources", residential-proxy conditional
  access, the abandoned-challenge and FileAccessed-vs-FileDownloaded detections). The hedge is carried
  at GTIG's own strength in the title, summary, body, `sourcing_note` and both registry records.
- **Sonatype, Microsoft and Unit 42 bodies** checked claim-by-claim: 846 components (Sonatype's own
  TL;DR figure — the entry correctly prefers it to the headline's "850"), the OpenSourceMalware
  first-report credit, the six-step first-stage loader sequence, the DNS TXT fallback, the detached
  launch, the Windows second stage (ETW/AMSI patching, debugger/VM/sandbox/security-product checks,
  AppData copy, Run key + scheduled task, encrypted payload, reflective in-memory execution), CWE-506
  at CVSS 8.7, `sonatype-2026-005660`, and the "syntactically different … different URL function and
  variable names … same behavior" variation claim — all exact. Microsoft's six-object fingerprint set,
  WebGL hardware check, timezone/iframe/touch probes, the `toString()` counter (with Microsoft's own
  "usually remains unchanged" hedge preserved), the prototype-tamper probe, the "Verified Publisher /
  Download for macOS" page, the obfuscated `curl` one-liner, the MacSync + AMOS naming, and the macOS
  26.4 paste mitigation — all exact. Unit 42's transfer-station mechanics, the new-api/one-api proxy
  layer with its Obfuscation/Rotation/Billing/Model-routing/Normalisation functions, the four
  privileged-account abuse steps, and — importantly — the user-agent signal the entry attributes to
  Unit 42, which does exist in the post's IOC table ("Go-http-client/2.0,gzip(gfe) — User Agent
  associated with malicious API calls") and which the entry correctly abstracts instead of reproducing.
- **Meta-incident attribution boundaries hold on all four sources.** Reuters carries the Meta
  statement verbatim, the two Irregular quotes verbatim, The Information's Muse Spark 1.1 attribution as
  The Information's, and the root-cause separation (config error for Meta and Anthropic; an agent
  independently exploiting an unknown vulnerability for OpenAI). Anthropic's post carries "the
  evaluation environment of Irregular, one of our third-party evaluation partners", "Neither we nor our
  evaluation partner were aware of this misconfiguration until we detected it through our additional
  evaluation monitoring", and "The two organizations we were able to reach had not previously detected
  the activity or contacted us" — the entry's three derived claims each land exactly. All three
  `references[]` entry ids resolve to files on disk.
- **Classification codes are consistent with `sources/sources.json`** (anssi-fr A, advisories-ncsc-nl A,
  adobe-psirt A, mandiant-gtig/msft-ti/jamf-threat-labs/unit42/sonatype/bleepingcomputer all B) and with
  each entry's actual corroboration; every single-source entry says "credibility is 2 rather than 1" and
  names why. No `org_triage` block, no `watchlist_hit: true`, no `watchlist` tag anywhere — correct for
  a profile with neither configured. So: **no F16, no F17.**
- **IOC-free.** No hash, IP, bracketed domain or rule code in any entry. Spot-grepped for the specific
  strings the primaries publish — `bigops`, `bnpl`, `35.x.y`, `passkeyhelpdesk`, `addssopasskey`,
  `apricotfilepoint`, `com.zoom`, `zoomMacArm`, `hub.zoom`, `update_win`, `/curl/` — zero hits. The one
  match, `ZoomMeetings`, is the masquerading binary name inside a verbatim Jamf quote and is the
  T1036.005 behaviour itself.
- **`actions[]` discipline.** Eight entries carry six actions total, two of them empty (`fake-zoom…`,
  `meta-ai-eval…`) — correct for an awareness item and an out-of-nexus lesson entry. Every action
  present is concrete, self-contained and derived from its own finding's mechanics; none duplicates an
  in-window action; none exceeds two per entry. **No F18.**
- **Run-record telemetry matches the files.** `entries_published: 8` = 8 files. Candidate arithmetic
  reconciles: S1+S2+S3+S4 `items_returned` = 1+2+4+3 = 10 raw, minus the S3/S4 UNC6671 duplicate = 9
  unique from research, of which 7 published, 2 dropped (the SharePoint-CVE narrowing and the Snowflake
  plea), plus the sweep-recovered Sonatype item = 8. The url-liveness ledger is 89 rows / 48 hosts as
  stated. `sources.json` now holds 176 records against the "175/175 probed" claim — exactly consistent
  with adobe-psirt having been added this run. ATT&CK: local pin v19.1, and `tools/attack_data.py --check`
  independently reports "upstream v19.2 (published 2026-08-05T21:33:58.496Z)" — the record's claim is
  precise. All 54 technique ids across the 8 entries resolve in the v19.1 pin, none revoked or
  deprecated.
- **The KEV negative result is real.** I re-pulled the catalog: `catalogVersion 2026.08.06`, released
  2026-08-06T18:15:23Z, newest addition dated 2026-08-05 = CVE-2026-63077 JetBrains TeamCity (already
  published here on 08-06), nothing dated 08-06 or 08-07. Exactly as the record states.
- **Coverage looks complete.** Independent probes found no missed in-window item: NCSC-CH's newest post
  is 2026-08-05 (N-able N-central, already covered on 08-05); a targeted search for in-window actively
  exploited advisories surfaced only N-able N-central and Cisco FMC, both already in the store; a Swiss
  in-window sweep surfaced only the BIT/FOITT SharePoint story the run deliberately treated as a
  borderline drop with reasoning I agree with. The upheld drop list is unusually well argued — the
  French healthcare pair and the two Swiss leak-site claims are the right calls on sourcing strength
  despite the nexus. **No F10.**
- **Relevance and priority calibration.** Two `high` vulnerability entries both clear the
  beyond-the-patch-cycle bar (pre-auth account takeover on identity-broker software fronting European
  e-government federated login; three pre-auth CVSS-10.0 code-execution paths whose affected range
  swallows the fix this store told readers to apply five days earlier). No `critical` — correct, since
  neither has exploitation or public PoC. Four `notable` lab-research entries all carry transferable
  tradecraft. The out-of-nexus Meta incident earns its place on the shared-vendor-assurance lesson and
  is framed on that lesson rather than the victim's name, with `actions: []` — the right shape. No F7.
- No contradiction beyond the one already surfaced (Adobe CVE-2026-48331 impact wording, correctly
  recorded in both the `sourcing_note` and the record's § Contradiction). **No F9.** No F12 — all four
  single-source entries carry `verification: single-source` plus a `sourcing_note` naming the basis, and
  the record lists them. No F1, no F2, no F6, no F13, no F15.

---

### Citation does not support the claim

**F1 — Keycloak entry: the disclosure date is 2026-08-05, not 2026-08-06, and the cited pages say so.**

The entry's summary states:

> "CERT-FR relayed seven Keycloak CVEs **disclosed on 2026-08-06** in keycloak-services…"

and all four `sources[]` records for `access.redhat.com` carry `date: "2026-08-06"`, which renders as
four inline citations of the form `([Red Hat Product Security, 2026-08-06](https://access.redhat.com/security/cve/CVE-2026-16443))`.

Fetched live in this iteration. The cited page for CVE-2026-16443 embeds
`"field_cve_public_date":"2026-08-05T13:39:33.000Z"` and `"changed":"2026-08-05T16:18:03.000Z"`, and the
RHSA advisories it lists (RHSA-2026:50846/50847/50848/50849) carry
`"release_date":"2026-08-05T16:17:59+00:00"` … `"2026-08-05T16:20:31+00:00"`. The string `2026-08-05`
occurs 13 times on that page; `2026-08-06` occurs **zero** times. Red Hat's Hydra records agree:
`public_date` = 2026-08-05T13:39:33Z for CVE-2026-16443 and 2026-08-05T02:02:00Z for CVE-2026-16442,
CVE-2026-15572 and CVE-2026-16102.

So the batch was disclosed and patched on **2026-08-05**; CERT-FR relayed it on 2026-08-06 ("Paris, le
06 août 2026", `N° CERTFR-2026-AVI-0976` — verified). This is not a UTC-rendering artefact: the primary
carries an explicit 13:39Z timestamp on 08-05 and its fixes shipped at 16:17–16:20Z on 08-05.

To fix: the four `sources[].date` values, the four inline citation dates, the summary's "disclosed on
2026-08-06", and `event_date` (which the frontmatter contract binds to the primary source's publication
date — Red Hat is `sources[0]`). The body's separate sentence "CERT-FR carried the batch to European
constituents on 2026-08-06" is correct and should stay. The run record's § Sourcing and classification
repeats the same off-by-one and should move with it — "OSV had not yet ingested advisories published the
previous day" implies 08-06, where the advisories are two days older than the run.

### Unsupported / hallucinated facts

**F2 — Adobe entry: `T1505.003` (Web Shell) has no matching body behaviour and no source basis.**

Frontmatter: `techniques: [T1190, T1059, T1505.003]`.

I fetched and read APSB26-120 in full. Its seven-row vulnerability table is: CWE-918 SSRF, CWE-1336
template-engine injection, CWE-89 SQL injection (×2), CWE-863 incorrect authorization, CWE-95 eval
injection, CWE-657 violation of secure design principles. No persistence mechanism of any kind is
described, and the words "web shell" appear nowhere. NCSC-2026-0278 (fetched) mirrors the same six
`Kenmerken` categories and adds nothing about persistence. The entry's own body describes only
execution-side behaviour — "unexpected egress initiated by the ACC process" and "unexpected child
processes spawned by the web or template-rendering service" — and explicitly says "no cited source
describes an actual attack against these CVEs".

A web shell is a plausible *post*-exploitation choice, but nothing in the entry or its sources
describes one, so the id is inference presented as mapping. This is the same defect class iteration 1
caught on the Meta entry (`T1195.002` with no matching behaviour); the fix is the same — drop it and
leave `T1190` + `T1059`, which the body and the CWE set both support.

**F3 — Unit 42 entry: "insider variant" is a threat model Unit 42 does not describe.**

Three places assert it:

- title: `"…Unit 42 documents the 'transfer station' market and **the insider variant that mints its own keys**"`
- summary: `"A **privileged-insider variant** uses a compromised developer account to mint new keys, remove billing limits and disable usage alerts and logging."`
- `actions[0]`: `"…**the insider variant** in this report works by removing billing limits and disabling usage alerts with the same account that spends the budget."`

The word "insider" appears **zero** times in `https://unit42.paloaltonetworks.com/ai-token-jacking/`
(fetched this iteration). What Unit 42 actually describes is external account takeover: "Attackers can
use privileged corporate developer accounts they've **harvested via information stealers or through
phishing campaigns** to perform the following activities: Creating new API keys / Provisioning models /
Removing billing limits / Disabling critical usage alerts and logging", followed by "These developer
accounts are readily available for **sale by access brokers on dark web marketplaces**."

The body gets this right — "an attacker holding a compromised corporate developer account uses that
account's own privileges to…" — so the mechanics are sound and only the label is wrong. But for this
audience "insider" is a load-bearing word: it points a reader at insider-threat controls (monitoring,
HR-linked triggers, separation of duties) rather than at credential theft and stealer hygiene, which is
what the cited mechanism calls for. And the title and summary are the machine-consumed surfaces that
render at the top of the brief. Replace with "account-takeover variant" or
"compromised-developer-account variant" in all three places; the body needs no change.

### Claims missing inline citation

**F4 — Adobe entry: the APSB26-114 facts and the three-wave count appear in neither cited source and carry no link.**

The entry's hook, its opening sentence, and its only action item all rest on facts about the *previous*
bulletin, which is not among its sources:

> "**Five days after Adobe fixed two critical unauthenticated flaws in Campaign Classic with build 9398**, it published a second bulletin whose affected range includes build 9398."

> "**This is the third distinct wave of critical unauthenticated code-execution-class disclosures against this product line since early July, each at Adobe's top priority**, which is itself the planning signal…"

> `actions[0]`: "…build 9398, **applied as the fix for the 2026-07-29 bulletin APSB26-114**, is inside the affected range for all seven of these flaws."

APSB26-120, which terminates the first of those sentences, states only the affected range ("ACC v7:
7.4.3 build 9398 and earlier"), the fix ("ACC v7 7.4.3 build 9399"), its own date ("August 3, 2026") and
its own Priority 1. It never names APSB26-114, never gives its date, never says it fixed two flaws or
shipped build 9398, and says nothing about a wave count. NCSC-2026-0278 names only its own predecessor —
"NB: Dit is geen update van de eerdere advisory NCSC-2026-0273 … Deze advisory betreft nieuw gevonden
kwetsbaarheden" — and never mentions APSB26-114 either.

The facts are true; I checked each one rather than assume. `helpx.adobe.com/security/products/campaign/apsb26-114.html`
(fetched) is dated "July 29, 2026", Priority 1, updated version "ACC v7: 7.4.3 build 9398", with two
CVEs — CVE-2026-48449 (CWE-863, arbitrary code execution, 10.0, `PR:N`) and CVE-2026-48448 (CWE-89,
arbitrary file system read, 8.6, `PR:N`) — so "two critical unauthenticated flaws … build 9398" and
"2026-07-29" are both right, and the store carries the matching entry
`entries/2026-08-02/adobe-campaign-classic-apsb26-114-cvss10-unauth-rce.md`. The third wave also checks
out: `entries/2026-07-02/cve-2026-48276-…-adobe-coldfusio.md` records "a CVSS 10.0 authorization-bypass
code-execution flaw in Campaign Classic — all Priority 1" for APSB26-68/69.

But a reader following the citation cannot get to any of it. Cleanest fix: add
`https://helpx.adobe.com/security/products/campaign/apsb26-114.html` as a corroborating `sources[]`
record (I fetched it successfully this iteration) and cite it on the opening sentence and the action.

Two smaller points inside the same sentence family, fixable in the same edit:

- "NCSC-NL … is explicit that it is not an update of **its earlier advisory covering APSB26-114**" — the
  cited page names `NCSC-2026-0273` by id and URL only. I fetched NCSC-2026-0273 to check: it is dated
  31-07-2026, references `apsb26-114.html`, and lists CVE-2026-48449/48448, so the identification is
  correct — but it is a hop the cited page does not make, and naming the advisory id would remove the
  gap outright.
- "since **early July**" — APSB26-68/69 carries `event_date: 2026-06-30` in this store's own entry, so
  "since the end of June" is the accurate framing. The run record's `sources_changed` note for
  adobe-psirt repeats "since early July" and can move with it.

### Needs more research

**F5 — ClickFix entry drops Microsoft's own network-side hunting pivot, which is the one that survives the cloaking the entry is built around.**

The entry's whole argument is that the gate destroys URL-level verdicts — "a scanner's verdict on one of
these URLs is close to worthless", "treat a clean verdict on one of these URLs as no evidence at all,
and move detection to the endpoint, where the gate has no vote" — and its detection guidance is
explicitly domain-agnostic ("the sequence to alert on regardless of which domain served it"). The
infrastructure is reduced to:

> "The gate is hosted across **a large set of algorithmically generated domains following a consistent naming pattern**"

Microsoft's post (fetched this iteration) supplies both the scale and the pattern, and recommends
hunting on the pattern precisely because individual domains are disposable:

> "Microsoft Threat Intelligence confirmed **more than 250 ClickFix front-end domains** during the tracking window, and many followed a repeated naming pattern using the token **'file' with dictionary-style words**"

> "**Hunt the generation pattern.** Where feasible, alert the `file<word><word>` domain pattern rather than maintaining a list of individual domains."

That is a source-supported, immediately implementable DNS/proxy-side detection concept, and it is not an
IOC — it is a generation pattern, the same construct the run carries without hesitation in two other
entries the same day ("Root domains pair authentication vocabulary — passkey, mfa, sso — with a verb" on
UNC6671; "names that interpolate a small set of recurring terms and version numbers clustered in one
range" on Flooding Dropper). So the omission is both a loss of depth the source clearly supported and
internally inconsistent with the run's own handling of the identical problem elsewhere. Add the pattern
shape and the >250 count, and give the reader one network-side pivot alongside the endpoint sequence.

### Editorial / less-is-more flags (advisory)

**F6 — run-record notes body carries workflow-internal vocabulary; recorded, but no action recommended this run.**

Style check 12 names these terms specifically, and the published notes body uses them throughout:
`sub-agent` ×9, `main agent` ×2, `Phase N` ×2, `spawn` ×1, and the worker labels S1/S2/S3/S4 ×13 —
e.g. "S1 surfaced it, judged it outside its own CVE/advisory remit, and handed it to S3 and S4; neither
returned it. Rather than let a cross-domain hand-off fall through the gap, the main agent fetched the
primary and decided directly", "the main agent re-checked the catalog directly in Phase 2", and "no
intake sub-agent was spawned".

**I do not recommend changing it in this run.** It matches settled store convention rather than drift
this run introduced — the 2026-08-06 record uses `spawn` ×9 and S1–S4 ×6, 2026-08-05 uses `sub-agent`
×5 / `spawn` ×4 / S1–S4 ×21, 2026-08-04 uses `spawn` ×3 / S1–S4 ×12 — and the notes' operational value
depends on saying which worker did what. Rewriting one record against a store-wide pattern would make
this run inconsistent with its neighbours for no reader gain. Logged once so the tension between check
12 and the convention is visible to the weekly quality audit, which is the right venue to settle it.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 2, advisory: 1)`

Truth = F1 (claim-not-supported) + F2, F3 (hallucinated-fact). Editorial = F4 (missing-citation) + F5
(needs-more-research). Advisory = F6.

The run is in good shape and the two prior iterations' remediations all hold — in particular the
iteration-2 Jamf attribution rewrite is faithful in all three locations, does not re-splice, does not
imply Jamf excludes a DPRK link, and introduced no IOC. The three truth findings are all narrow and
mechanically fixable: one date corrected in six places, one technique id dropped, one word replaced in
three places. F4 and F5 each want one added source or one added sentence. None of the six calls the
soundness of an entry into question, and I found no coverage gap.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-16443 — Keycloak SAML broker signature bypass (keycloak-saml-broker-signature-bypass-cve-2026-16443)"
  url_or_quote: "\"CERT-FR relayed seven Keycloak CVEs disclosed on 2026-08-06\" + sources[].date \"2026-08-06\" on https://access.redhat.com/security/cve/CVE-2026-16443 (and -16442, -15572, -16102)"
  summary: "The cited Red Hat pages carry public_date 2026-08-05 (CVE-2026-16443 = 2026-08-05T13:39:33Z; -16442/-15572/-16102 = 2026-08-05T02:02:00Z), and the RHSA fixes released 2026-08-05T16:17-16:20Z. Fetched live this iteration: the string 2026-08-06 appears zero times on the CVE-2026-16443 page. Disclosure was 2026-08-05; CERT-FR relayed on 2026-08-06 (its page: 'Paris, le 06 aout 2026'). Fix the four sources[].date values, the four inline '[Red Hat Product Security, 2026-08-06]' citations, the summary's 'disclosed on 2026-08-06', and event_date (should be the primary source's publication date, 2026-08-05). The run record's Keycloak sourcing paragraph repeats the same off-by-one ('advisories published the previous day')."
- code: F2
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "Adobe Campaign Classic APSB26-120 (adobe-campaign-classic-apsb26-120-second-wave-unauth-rce)"
  url_or_quote: "techniques: [T1190, T1059, T1505.003]"
  summary: "T1505.003 (Web Shell) names a behaviour neither cited source describes and the body does not map. Adobe's APSB26-120 per-CVE table (fetched and read in full this iteration) lists CWE-918 SSRF, CWE-1336 template injection, CWE-89 SQLi x2, CWE-863 incorrect authorization, CWE-95 eval injection, CWE-657 secure-design violation - no persistence mechanism and no web shell; NCSC-2026-0278 likewise. The entry's own detection concepts are outbound egress from the ACC process and unexpected child processes of the web/template-rendering service - execution, not a persistent web shell. Drop T1505.003; T1190 + T1059 are the honest evidence-bound set."
- code: F3
  category: hallucinated-fact
  section: research
  item: "AI API token jacking / transfer-station resale (ai-api-token-jacking-transfer-station-resale)"
  url_or_quote: "title: \"...and the insider variant that mints its own keys\"; summary: \"A privileged-insider variant uses a compromised developer account to mint new keys\"; actions[0]: \"the insider variant in this report works by removing billing limits\""
  summary: "Unit 42 describes no insider. The word 'insider' appears zero times in https://unit42.paloaltonetworks.com/ai-token-jacking/ (fetched this iteration); the post says 'Attackers can use privileged corporate developer accounts they've harvested via information stealers or through phishing campaigns' and that 'These developer accounts are readily available for sale by access brokers on dark web marketplaces' - i.e. external account takeover, the opposite of an insider threat. The body itself is correct ('an attacker holding a compromised corporate developer account'), so the defect is confined to the title, summary and action label, which point a reader at the wrong threat model. Replace 'insider variant' with 'account-takeover variant' / 'compromised-developer-account variant' in all three places."
- code: F4
  category: missing-citation
  section: trending-vulnerabilities
  item: "Adobe Campaign Classic APSB26-120 (adobe-campaign-classic-apsb26-120-second-wave-unauth-rce)"
  url_or_quote: "\"Five days after Adobe fixed two critical unauthenticated flaws in Campaign Classic with build 9398\"; \"This is the third distinct wave of critical unauthenticated code-execution-class disclosures against this product line since early July, each at Adobe's top priority\"; actions[0] \"the 2026-07-29 bulletin APSB26-114\""
  summary: "The entry's whole hook rests on APSB26-114 facts that appear in neither cited source. APSB26-120 (fetched in full) states only 'ACC v7: 7.4.3 build 9398 and earlier', 'ACC v7 7.4.3 build 9399', 'August 3, 2026', Priority 1 - it never names APSB26-114, its date, its two CVEs or a wave count; NCSC-2026-0278 (fetched) names only its own earlier advisory ('Dit is geen update van de eerdere advisory NCSC-2026-0273') and never mentions APSB26-114. The facts are true - I fetched https://helpx.adobe.com/security/products/campaign/apsb26-114.html (July 29 2026, Priority 1, fixed in ACC v7 7.4.3 build 9398, CVE-2026-48449 + CVE-2026-48448, both PR:N) and NCSC-2026-0273 does reference apsb26-114.html - but the reader gets no link. Fix: add the APSB26-114 bulletin as a corroborating source and cite it on those clauses. Two smaller points in the same sentence family: 'its earlier advisory covering APSB26-114' is a one-hop inference the cited 0278 page does not itself state, and 'since early July' should be end of June - the store's own 07-02 entry dates APSB26-68/69 to event_date 2026-06-30."
- code: F5
  category: needs-more-research
  section: active-threats
  item: "macOS ClickFix server-side fingerprinting gate (macos-clickfix-server-side-fingerprinting-gate-amos)"
  url_or_quote: "\"The gate is hosted across a large set of algorithmically generated domains following a consistent naming pattern\" / detection guidance \"regardless of which domain served it\""
  summary: "Microsoft's post (fetched this iteration) carries the one network-side pivot that survives the cloaking this entry is built around, and it dropped out: 'Microsoft Threat Intelligence confirmed more than 250 ClickFix front-end domains during the tracking window, and many followed a repeated naming pattern using the token \"file\" with dictionary-style words', and under mitigation 'Hunt the generation pattern. Where feasible, alert the file<word><word> domain pattern rather than maintaining a list of individual domains.' The entry withholds both the count and the pattern shape and moves detection entirely to the endpoint. This is not an IOC - it is a generation pattern - and the run's own other two entries carry exactly this construct (UNC6671: 'Root domains pair authentication vocabulary - passkey, mfa, sso - with a verb'; Flooding Dropper: 'names that interpolate a small set of recurring terms and version numbers clustered in one range'), so the omission is internally inconsistent as well as a loss of depth."
- code: F6
  category: editorial-advisory
  section: run-record
  item: "runs/2026-08-07/2026-08-07T0411Z-intel.md - Verification & coverage notes"
  url_or_quote: "\"S1 surfaced it, judged it outside its own CVE/advisory remit, and handed it to S3 and S4; neither returned it. Rather than let a cross-domain hand-off fall through the gap, the main agent fetched the primary and decided directly.\" / \"the main agent re-checked the catalog directly in Phase 2\" / \"no intake sub-agent was spawned\""
  summary: "The published notes body carries workflow-internal language that style check 12 names explicitly: 'sub-agent' x9, 'main agent' x2, 'Phase N' x2, 'spawn' x1, S1/S2/S3/S4 x13. NO ACTION RECOMMENDED THIS RUN - this matches settled store convention (2026-08-06 record: spawn x9, S1-S4 x6; 2026-08-05: sub-agent x5, spawn x4, S1-S4 x21; 2026-08-04: spawn x3, S1-S4 x12), so it is a store-wide policy question for the weekly quality audit rather than a defect this run introduced. Logged once so it is visible."
```
