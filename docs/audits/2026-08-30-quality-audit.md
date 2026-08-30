# Quality audit — 2026-08-30 (run `2026-08-30T1312Z-audit`, prompt v4.8)

**Mandate.** Soundness and completeness over the trailing window, plus the machinery. Run record: [`runs/2026-08-30/2026-08-30T1312Z-audit.md`](../../runs/2026-08-30/2026-08-30T1312Z-audit.md).

**Window.** 2026-08-28T13:30Z → 2026-08-30T13:12Z, anchored on the previous audit record's `started`. 44 entries in scope: 8 published new by the 08-29 and 08-30 intel fires, 36 carrying a changelog record dated inside the window (34 of them from the 2026-08-28T1500Z operator-directed session).

**Duplicate-audit guard: overridden, deliberately.** The gap to the previous audit record is 47.7 h, inside the 72 h guard. The guard is not applied, because the record it measures against is not a quality audit: `2026-08-28T1500Z-audit` was an operator-directed interactive editorial session on a read-only sandbox **with no external network**. It ran no truth passes and no coverage re-sweeps, its own report states that "URL-level re-verification of the touched entries falls to the next network-enabled quality audit", and it left a named backlog for this fire. Standing down would have left 39 edited entries unverified against their sources and seven flagged residuals unadjudicated. The last audit that did this work was 2026-08-24T0902Z, six days ago.

**Method.** Three `cti-verification` truth passes over the 44 entries (batched 15/15/14), three `cti-research` coverage re-sweeps (G1 vulnerabilities, G2 incidents/regional, G3 research/APT) re-researching a 150 h window — the period since the last independent re-sweep, not since the last fire. 110 URLs fetched and logged. Systemic review over local artefacts.

---

## Verdict

**19 of 44 entries verified clean. 11 carried a factual error, 14 an imprecision.** That is the worst soundness result this pipeline has recorded, and the explanation is not that quality collapsed — it is that this is the first network-enabled cold read of a cohort that had never had one. Thirty-six of the 44 were composed by the 2026-08-28 catch-up fire (a 91 h window, 36 entries, the first Sonnet 5 intel fire, which crossed the wall-clock watchdog and landed seven verification residuals) and then edited by a session that could not reach a single source to check them. Every defect below is one those two passes could not have caught, and most are of one shape: **a quotation or an attribution that drifted from what the source actually says.** Six of the eleven factual errors are that. None is an invented event; all eleven are real findings misreported at the sentence level.

Completeness is the more serious half. **Eight items cleared the relevance gate and are in no entry at all**, including two CISA KEV additions with confirmed in-the-wild exploitation — one CVSS 10.0, unauthenticated, on internet-facing proxy infrastructure, exploited since January against a target list that is 85 % government domains. The 2026-08-28 fire read the KEV feed, surfaced four other additions from it, and never mentioned either of these two in any artefact: not as entries, not as drops. Nothing in the run distinguished "considered and dropped" from "never seen". That is fixed in code and prompt this fire.

The machinery is otherwise sound: the previous audits' fixes took, the gate is green, the ATT&CK pin is current, source health is good, and the publish chain works.

---

## Findings — false or erroneous published intelligence

Eleven confirmed factual errors, every one addressed through that entry's changelog this fire. Ten took a `correction`; the eleventh (Kaltura, below) took an `update`, because the fact changed after publication rather than having been wrong when written.

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| `2026-08-28/doj-fbi-qscan-qtrouter-prc-hacking-as-a-service-takedown` | Quotation attributed to DOJ read "Among the **victims** of QTFY **computer intrusion activity** are…" | DOJ writes "Among the **targets** of QTFY are…"; the phrase "computer intrusion activity" appears nowhere on the page ([justice.gov](https://www.justice.gov/opa/pr/justice-department-and-fbi-seize-platforms-operated-and-used-china-state-sponsored-hackers)) | `correction` — quote, body sentence and title moved to "targets"; title no longer implies the 2018 dating attaches to that list |
| `2026-08-28/unisoc-volte-mpu-isolation-bypass-android-kernel` | Title, `affected_products[]` and body asserted T606/T612/T7250 and mapped three test devices one-to-one onto them | Neither reachable source contains "T606" or "T7250"; only the T612 is named, only for the Realme C33 ([Dark Reading](https://www.darkreading.com/mobile-security/video-call-exploit-chains-two-flaws-unisoc-modems)) | `correction` — chipset list removed from title, summary, products and body; scoped to the shared modem firmware line |
| `2026-08-28/owncloud-cve-2023-49105-philippines-nuclear-naval-hunt-io` | `cves[].epss: "11.07"`, uncited; no source mentions EPSS | Live FIRST API returns 0.43205 for CVE-2023-49105 | `correction` — field nulled; also added the ZKTeco BioTime dump Hunt.io lists among its own key findings and the entry had omitted |
| `2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce` | Asserted CVE-2026-21718 **is** the deterministic-password flaw | Claroty's per-CVE text for that id is generic; the narrative describing the MAC-and-date derivation names no CVE at all. The binding was elimination logic, not vendor attribution | `correction` — id binding removed from the CVE record, action and body; sourcing note states what Claroty does and does not attribute |
| `2026-08-28/cncmachinerms-babadeda-loader-enumtimeformats-shellcode` | Two LevelBlue quotations non-verbatim; one a composite of a bullet and a phrase from a different paragraph | Source sentences fetched verbatim | `correction` — both replaced with contiguous source wording |
| `2026-08-28/cve-2026-53362-linux-kernel-ipv6-udp-fraggap-kev` | `cves[].auth: pre-auth`, contradicting the entry's own quoted vector | `AV:L/AC:L/PR:L/…` — an unprivileged local user opening a UDPv6 socket, not an unauthenticated actor | `correction` — `post-auth`; exposure re-scoped to hosts running untrusted code |
| `2026-08-28/kudelski-bismarck-dprk-it-worker-gambling-fakecalls-overlap` | Said Kudelski "treats Bismarck as distinct from the already-tracked PurpleDelta cluster" | Kudelski's report never mentions PurpleDelta; it takes no position either way | `correction` — replaced with what the report does and does not say |
| `2026-08-28/manchester-airports-group-data-breach-8-7-million` | "The UK ICO has confirmed receipt of a breach report and is assessing it", in summary and body, uncited | No source says this. The Register reports only that the ICO asked MAG not to disclose the ransom note, demands or group name; MAG names no regulator | `correction` — claim removed, replaced with what the reporting establishes |
| `2026-08-28/protection-civile-france-eprotec-breach-volunteers` | "the FNPC explicitly states… neither passwords nor banking details appear in the leak" | The FNPC statement never mentions either. It is FrenchBreaches' hedged non-finding: the available elements "do not allow us to establish the presence" of them | `correction` — re-attributed and hedged; awareness date corrected to a single date (17 August) |
| `2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor` | "Zbtlink has offered nothing"; the 08-29 update called VulnCheck's guidance "the only remediation position on record" | The entry's own cited heise article reports Zbtlink announced suspending sales and pulling the firmware while developing updates — a statement predating the entry's first publication | `correction` — vendor position stated; defender guidance unchanged (no update shipped, statement does not cover DARKLANTERN/SPEAKINGSTONE) |

**The eleventh took an `update` rather than a correction, because the world changed after it was written:**

- `2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch` shipped as "no vendor response, no patch". CERT/CC updated VU#308749 at 2026-08-28 19:59 UTC — after the fire, and after the no-network editorial session — to state Kaltura has patched every affected legacy Player V2 version, and that the supported Player V7 was never affected. Both CVE records move to `patch-available`, the title and tags drop the no-patch framing, and the entry re-floats. This is the single most consequential staleness in the store: a reader acting on it yesterday would have believed there was nothing to install.

### Root causes

**Quotation fidelity is the dominant defect class and it is getting worse.** Six of eleven factual errors are a quote or attribution that does not match its source: a word substituted (`victims`/`targets`), a sentence spliced from two paragraphs, a tracker's hedged non-finding restated as an organisation's assurance, an analytic position attributed to a report that takes none. The 2026-08-24 audit already measured F3 (claim-not-supported) rising 38 → 48.9 per ten fires while F4 (hallucinated fact) fell by half — this window is that trend continuing, and the mechanism is compression: a composer paraphrasing to fit a shorter entry, then leaving the quotation marks on. The `grep -F` quote check that drove F4 down verifies quotes the verifier is *shown*; it cannot see a quotation the composer never checked. This is not fixed by a prompt line saying "quote verbatim" — that line already exists. Recorded as watch item 3 with a concrete instrumentation proposal.

**Two of the eleven are the no-network session's structural blind spot**, not a composition defect: Kaltura and Zbtlink both turned on a source the session could not fetch. That session was right to defer them and this audit was right to be the one that caught them; the loop worked.

**The remaining three are the entry disagreeing with its own evidence** — an EPSS number from nowhere, a CVE-to-mechanism binding reached by elimination and presented as the vendor's, and a `cves[].auth` field that contradicts the CVSS vector quoted three paragraphs below it. The first two are a failure to distinguish "the sources support this" from "this is the most likely reading of the sources"; the third is a frontmatter-versus-body check a cold reader should have caught and two passes did not.

---

## Findings — missing or incomplete coverage

**Eight items cleared the gate and are in no entry.** All eight are recorded as open rows in [`state/coverage_backlog.md`](../../state/coverage_backlog.md) with primary sources and gate reasoning, which makes them exempt from the recency gate and puts each one in front of the next fire. The two KEV-confirmed exploited items are additionally **recovered as entries in this fire** — a CVSS 10.0 unauthenticated flaw under active exploitation is the case PD-11 says must never be deferred into invisibility. The remaining six stay backlogged: the priority order puts truth passes and their eleven corrections first, and six full compositions on top of that would have pushed this run past its wall-clock guard. That split is the deliberate cut, recorded here so it is auditable.

**Missed by the KEV sweep (both KEV-confirmed exploited; both recovered as entries in this fire):**

1. **CVE-2026-21962** — Oracle HTTP Server / WebLogic Server Proxy Plug-in, unauthenticated access-control bypass, CVSS 3.1 base 10.0, KEV 2026-08-24. Exploited since 22 January 2026 per CloudSEK honeypot telemetry; SOCRadar's analysis of an exposed China-nexus (UNC5174/UNC6586, SNOWLIGHT) staging server lists it among nine weaponized CVEs in a campaign whose reconnaissance list is more than 85 % second-level government domains across 100+ countries. Patched in Oracle's January 2026 CPU. This is a DMZ-fronting component and a government-sector target profile, as close to a mandatory entry as PD-11(b) gets. Recovered as `2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev`.
2. **CVE-2026-60004** — Gitea diffpatch Git-hook code injection, CVSS 9.8, KEV 2026-08-25, effectively unauthenticated on a default open-registration install, confirmed exploited end-to-end (register, create repo, RCE, miner) in about 11 seconds. Fixed in 1.27.1. Recovered as `2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev`.

**Missed by the research-blog discovery path** (the path that does not route through CVE/KEV channels, and the one three consecutive audits have now found misses in):

3. **Microsoft Threat Intelligence, "TerminalFix"** (2026-08-28) — a ClickFix variant pasting into Terminal/PowerShell rather than Run, chaining `dui70.dll` side-loading, PNG-steganography delivery, locale-aware AD reconnaissance and a custom reverse-WebSocket SOCKS tunnel.
4. **Microsoft Threat Intelligence, "When AI infrastructure becomes the target"** (2026-08-26) — three named intrusions against AI control-plane components (LiteLLM, RAGFlow, Kestra); all eight CVEs it names are new to this store.
5. **Huntress, "Insights into Suspected DPRK Workers"** (2026-08-26) — five 2026 IR cases with reusable forensics (PiKVM/Guermok USB artefacts via the USB enumeration registry key and Security Event ID 6416, laptop-farm timelines, identity-document metadata). Distinct from the covered Kudelski Bismarck entry, which carries no detection methodology.

**Missed by the vendor-advisory path:**

6. **WatchGuard Fireware OS** (2026-08-27) — eleven CVEs, two pre-auth RCEs in the `iked` IKE/VPN daemon and one unauthenticated stack overflow in the deprecated Mobile Security `epm` service (no stack canary, non-PIE). Vendor's own framing: "Immediate Action Required". No exploitation observed, so this is the PD-11(b) "otherwise" limb — the same class this store has consistently published for Citrix, SonicWall and Ivanti. BSI CERT-Bund relayed it as WID-SEC-2026-3068 on 2026-08-28, and the 08-29 fire swept BSI.

**Regional:**

7. **Norway / Digdir ID-porten DDoS** (2026-08-24 to 26, ~64 h, third since June, each two to three times larger) — health, tax and business-registry logins broke although none was targeted. A direct architectural analogue to Switzerland's own eID consolidation, which passed two million users the same week.

**Unresolved lead:**

8. **inside-it.ch on Insel Gruppe (Bern hospital group)** delaying a ServiceNow migration "wegen eines Sicherheitsvorfalls" — the article 403s on every transport, so whether this is a new Swiss hospital incident or caution carried from the June ServiceNow issue could not be established.

### Correctly droppable

- **OFAC sanctions on five Mabna Institute members** (2026-08-24, Iranian hacking-for-hire, DoJ-indicted for compromising 322 universities and government agencies since 2013). US-centric, no Swiss or DACH victim, and the actor is not one with established constituency targeting. Out-of-nexus gate not cleared.
- **CVE-2019-1068 (MS SQL Server)**, in the same KEV batch as items 1–2: no exploitation narrative exists anywhere, nothing to action.
- The 08-30 fire's own **McKesson/ShinyHunters** drop was re-checked and is correct: the vishing-to-SSO-to-SaaS chain is already carried by several entries.

### Resolved false alarms

- The 08-28 fire's four KEV additions (CVE-2026-53362, CVE-2026-66384, CVE-2026-8452, CVE-2026-59310) all match the live feed on dates and descriptions.
- G3 independently re-derived the entire 08-28/29/30 published set as already covered — 40-plus items — with no duplicate-entry defects and no case where a changelog record belonged on an existing entry instead.

---

## Findings — systemic and operational

### 1. The KEV sweep was attentional, and that is now fixed

A KEV listing is jurisdiction-agnostic confirmation of in-the-wild exploitation (PD-13) — the pipeline's strongest single vulnerability signal. Sweeping it was a research sub-agent's job, and a sub-agent returns what it notices. The 08-28 fire's S1 records `cisa-kev` in both `sources_attempted` and `sources_used` and surfaced four additions from it; two more, both in window, appear in no artefact of that run. There was no mechanism by which the run, its verifier, or the operator could tell the difference between a considered drop and an unseen row.

**Live output, run this fire** (`work/2026-08-30T1312Z-audit/kev-window.txt`): 11 KEV additions since 2026-08-24, 6 not covered. Two are the genuine gaps above. The other four (CVE-2015-3246, CVE-2015-5287, CVE-2019-1068, CVE-2022-0995) are the legacy UAT-10147 batch, which the two `2026-08-23` UAT-10147 entries discuss in prose without carrying `cves[]` records for them — so they are covered for a human reader and invisible to every machine surface built on `cves[]`, including the `/cve/` pages and the store-wide dedup index. That is a real if lower-severity finding the tool surfaced on its first run, and it is exactly the class it was built to make visible. Not fixed this fire; it belongs with the next audit's pass over that cohort.

**Shipped:** `tools/kev_window_diff.py` (stdlib-only) lists every KEV addition with `dateAdded` in the window and marks the ids no entry and no `state/cves_seen.json` record has ever carried, checking both surfaces. **Phase 0 step 6b** (v4.8) runs it and requires every NOT COVERED row to end the run with a disposition: an entry, an `update` record, or an explicit `borderline-drop:` line. Judgement stays with the agent; what is no longer possible is not knowing the row existed.

### 2. ATT&CK mapping density on `threat` entries fell by two thirds

| window | `threat` | `incident` | `vulnerability` |
|---|---|---|---|
| 2026-08-01 → 08-14 | **12.57** | 2.74 | 2.86 |
| 2026-08-15 → 08-27 | **11.05** | 2.00 | 2.29 |
| 2026-08-28 → 08-30 | **4.33** | 1.78 | 1.80 |

Mean ids per entry. The collapse is specific to `threat` — the kind whose sources (campaign and actor research) support deep mapping. `incident` and `vulnerability` drift mildly and are largely explained by composition: five of this window's incident entries map exactly one technique, and all five are victim disclosures with no stated vector, where one id is the honest mapping and more would be invention.

The `threat` number is not explained that way. Two changes landed together on 2026-08-28 — the first Sonnet 5 intel fires, and the v4.2 brevity hardening — so causation cannot be separated from three fires of data, and this report does not claim it. What can be stated is a mechanism the prompt actually contained: the anti-hallucination rule binds `techniques[]` to behaviours *the body describes*, and v4.2 told the composer to shorten the body. Those two together make prose length a cap on the mapping surface, which was never the intent.

**Shipped (v4.8):** § ATT&CK in metadata now states that brevity governs prose and never the mapping, that `techniques[]` is bound to what the cited **sources** describe rather than to how many sentences the body spends on them, and that the anti-hallucination floor is source evidence, not body length. Under-mapping is invisible in the entry a reader opens — it shows only in the `/attack/` matrix, the entity TTP profiles and the Navigator exports. Effectiveness check belongs to the next audit; watch item 1.

### 3. Frontmatter that only this repo can parse

Three entries carried double-quoted YAML scalars holding a Windows path (`C:\ProgramData\…`, `.\EOMT.ps1`, `Programs\Startup`) or an unescaped inner quote. This repo's `parse_yaml_subset` is deliberately lenient and read every one of them correctly; a standards-compliant parser rejects the whole frontmatter document. The store is published as a machine-readable base for downstream triage agents, so a file only this parser can read is not that.

**Shipped:** a `frontmatter-yaml` check in `check_run.py` (WARN, never FAIL — the value on disk is correct, the serialization is not; scoped to entries in `--all`, to the run's own entries plus its record in run scope, and skipped with a stated reason when PyYAML is absent so the gate stays stdlib-only).

All three entries are re-quoted, values byte-identical under both parsers, verified. Two carried further debt that surfaced the moment the fix pulled them into run scope, and both were repaired in the same changelog record rather than deferred: `2026-05-18/cve-2026-42897-…` had no Admiralty rating and is now A1, and `2026-06-02/sekoia-consolidates-gamaredon-…` had a null rating (now B2), an empty `techniques[]` on a research entry describing WinRAR CVE-2025-8088 exploitation, Startup-folder and scheduled-task persistence, NTFS-ADS hiding, dead-drop resolvers and USB propagation (now mapped, evidence-bound), and an `evidence[]` record whose "quote" was a migration artefact reproducing this pipeline's own update summary under a publisher byline that never wrote it (replaced with two verbatim passages re-fetched from Sekoia's report). One run record (`runs/2026-05-14/2026-05-14-e05c6e6e.md`) has the same serialization defect and is **not** touched: run records are immutable, and the check does not scan historical records for that reason.

### 4. Fix effectiveness — the previous rounds took

| Fix | Shipped by | Result this window |
|---|---|---|
| `completed` stamped in Phase 6, so `duration_seconds` is true wall clock | 2026-08-24 audit | **Took.** Every post-fix record stamps `completed` after its last verifier iteration. The runaway warnings this fire acknowledged exist *because* the metric is now honest. |
| Pipeline internals out of reader-facing text | 2026-08-28 session | **Took in bodies, did not take in `sourcing_note`.** See finding 5 — this is the audit's own worst call, corrected during its verification loop. |
| English-only quotations with `original:` preserved | 2026-08-28 session | **Took.** Every non-English quote in the 08-29 and 08-30 entries carries `original:` plus a marked translation. |
| Generic `sonnet` model pins | 2026-08-28 session | **Took.** Both agent definitions pin `sonnet`. |
| `heise-sec`, `inside-it-ch` promoted to essential | 2026-08-28 session | **Half.** heise contributed cited content on both subsequent fires. `inside-it-ch` has 403'd on every transport for two fires running and is the only essential-tier source contributing nothing this window; it is also now blocking a possible Swiss hospital incident (coverage item 8). |
| No em dash in reader-facing text | v4.5, 2026-08-29 | **Took**, on a sample of one: the single post-v4.5 fire is clean; all seven 08-29 entries predate the rule. Pre-v4.5 entries still carry them; the site strips them, so there is no reader impact. Sweep on touch. |

### 5. The internals fix did not take in `sourcing_note`, and this audit first reported that wrong

The fix-effectiveness table above originally read "mostly took, one leak", citing a single `sourcing_note` on `2026-08-29/servicenow-ai-platform-four-unauth-cvss10-flaws`. That was wrong, and this audit's own Phase 5.7 verifier caught it: the second iteration re-scanned `sourcing_note` across the whole store rather than across this run's diff, and found the pattern everywhere. A store-wide count run in response: **roughly 95 entries carry production-process self-reference in a reader-facing field** — "this run", "this fire", "this pipeline", "as of this run", "located this run" — the exact shape `prompts/cti-run.md` § Style rules names as a defect requiring deletion, in the exact field its own list includes.

Two things went wrong and both are worth naming. The first is measurement: the audit scanned bodies and changelog sections for the defect and did not scan `sourcing_note`, so it reported the size of what it looked at rather than the size of the problem. The second is that this run reproduced the defect while documenting it, in both entries it composed itself and in six of the entries it corrected.

Why it matters to a reader rather than to the pipeline: `sourcing_note` renders, and "not re-fetched this run" tells a reader nothing they can use. It silently dates a caveat to an event they cannot see, where a date would have told them exactly how stale the caveat is.

**Shipped:** a `reader-text-internals` check in `check_run.py` (WARN) over `title`, `headline`, `summary`, `sourcing_note` and every non-internal changelog record's `summary`, which renders on an entry's public revision history. Deliberately **run-scope only, not `--all`**: firing on ~95 historical entries would light `--all` up permanently and drown the zero-warning discipline in backlog, while the run-scope check stops each fire adding to it. All 15 entries in this run's scope now pass. The historical backlog is an audit sweep, one changelog record at a time, and is recommendation 6.

### 6. Telemetry, publish follow-through, source health, gate and pin

- **Telemetry.** Both in-window fires are healthy: 08-29 ran 2.87 h across 8 verifier iterations (1 residual), 08-30 ran 1.24 h across 4 (2 residuals, both remediated). Neither is a runaway. Gap-derived windows self-healed correctly across a changed cadence (91 h → 13.2 h → 24.0 h) with no coverage hole between runs — the cadence itself is the operator's and is not a finding.
- **Publish follow-through.** One stale record: `2026-08-28T1500Z-audit` still read `publish_status: pending` because the operator-interactive session committed on the host and ran no Phase 7 poll. Verified on `origin/main` (record present, `briefbook.json` carries the run id) and **amended to `ok`** with a note naming this audit — publish-status fields only. Every other record in the window reads `ok`.
- **Source health.** 16 of 17 essential-tier sources contributed cited URLs since 08-24. The exception is `inside-it-ch`, above. G3's per-publisher sweep found Microsoft TI, Huntress, Check Point, Securelist, Talos, ESET, SentinelOne, Sekoia, Citizen Lab, DFIR Report, Cloudflare, 0patch and AhnLab all reachable with working recipes, and **confirmed a working recipe for Symantec/Broadcom** (`extract https://www.security.com/threat-intelligence`) — the publisher the 2026-08-24 audit's recommendation 5 named as cited seven times store-wide with no source record at all. Added as this run's one candidate source, discharging that recommendation. `google-tag`'s recipe gap persists (resolves to the general security blog, not the TAG listing).
- **Reader pool.** Not probed this fire; the trailing evidence is that it stays exhausted. It did not block this audit: 110 URLs were read across six sub-agents, essentially all through the direct rungs, and the two truth-pass fetches that failed (SSD Secure Disclosure, twice) are anti-bot challenges the reader would not clear either. The one place it still bites is a jina-pinned host, and CERT/CC needed the reader this fire when `extract` returned corrupted bodies. Context only, per v3.33; not a recommendation and not a notification.
- **Gate and pin.** `check_run.py --all` was 24 pass · 9 warn · 0 fail at Phase 0 and ends 0 fail. `attack_data.py --check`: **local v19.2 == upstream latest v19.2**, no drift, no update needed.
- **Discipline drift.** `actions[]` at 0.82 per operational entry with 48.7 % carrying none (store baseline 0.81 / 54.1 %) — the "empty is normal" shape holds and the 2026-08-24 audit's reversal is confirmed, max 3 actions, no accumulation. Classification present on 44/44. Changelog discipline is clean: no second entry where a record belonged, every record's `fields` matching its diff, no `actions[]` list that grew instead of being replaced. The one metric moving the wrong way is `high` share at 59.0 % of operational entries against 51.1 % store-wide and 46.2 % last window — see below.

---

## Priority calibration

**Not due.** The monthly duty is at most one `## Priority calibration` section per calendar month, and the 2026-08-02 report carries this month's.

Recorded for the September fire, which owns the next one: the `high` share of operational entries rose to **59.0 %** this window (24 of 39 non-`policy` operational entries), against 46.2 % over 08-15 → 08-27 and 51.1 % store-wide. One `critical` (the PaperCut pre-auth RCE). A 13-point jump inside one window is the largest single-window movement recorded, and the 2026-07-11 audit's original concern was that 37 % was already generous. This audit does not adjudicate it — the monthly cadence exists so the judgement is made once, on a month of data, against concrete entries. But it should not be read as noise by whoever picks it up.

---

## Fixes shipped in this commit

1. **Prompts v4.8** (`cti-run.md` and `quality-audit.md` banners in lockstep, CHANGELOG entry with Why / What changed / What stays): Phase 0 step 6b, the mechanical KEV disposition sweep; § ATT&CK in metadata, decoupling mapping completeness from prose brevity.
2. **`tools/kev_window_diff.py`** (new): in-window KEV additions diffed against the store, `--since` / `--window-hours` / `--json` / `--kev-file`, stdlib-only, reads the catalog through the bridge.
3. **`tools/check_run.py`**: new `frontmatter-yaml` portability check (WARN), wired into both `--all` and run scope.
4. **Ten `correction` records and one `update` record** on 11 published entries, plus two `internal: true` `improvement` records carrying the frontmatter-portability repairs and the legacy debt they surfaced (`2026-05-18/cve-2026-42897-…`: re-quoting plus a first Admiralty rating A1; `2026-06-02/sekoia-consolidates-gamaredon-…`: re-quoting, rating B2, an evidence-bound `techniques[]` mapping, and a migration-artefact evidence record replaced with verbatim Sekoia passages). Thirteen entries touched, none silently.

4b. **Two recovered entries** published through the full normal gates: `2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev` and `2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev`, with `state/cves_seen.json` and the product entities synced.
5. **`sources/sources.json`**: `symantec-security-com` added as a candidate with the confirmed working recipe (this run's one candidate slot). Discharges recommendation 5 of the 2026-08-24 audit.
6. **`runs/2026-08-28/2026-08-28T1500Z-audit.md`**: publish-status amendment to `ok`, verified against `origin/main` and the built site data. Publish-status fields only.
7. **`state/coverage_backlog.md`**: eight new open rows, one per coverage gap, each with gate reasoning and primary sources.
8. **Warning sweep.** Nine warnings, all settled run-record history, acknowledged in `state/warning_acknowledgments.json` with reasons: seven runaway `duration_seconds` (2026-08-21, 08-22, 08-23-audit, 08-24-intel, 08-24-audit, 08-28-intel, 08-28-audit) and two unconfirmed final CLEANs (2026-08-22-intel, 2026-08-28-audit). Three of the seven durations are one story — the 08-21, 08-22 and 08-23 containers all stalled and were finished on 08-24, so those figures are elapsed container lifetime rather than work, which the 08-22 record states in its own words. Each acknowledgment says why no code, prompt or state fix could clear it, and each explicitly declines the fix that would weaken the check. Existing ledger rows reviewed: all 16 still silence a live warning, none pruned. Ledger now 25 rows, each new one also carrying a `by` field naming this sweep. **`check_run.py --all` ends 0 warn · 0 fail (25 acknowledged), and `site/build.py` emits no self-check warnings.**

---

## Recommendations (operator decisions, not shipped)

1. **Fund or retire the reader pool.** *(Carried from 2026-07-26, 08-02, 08-09, 08-24.)* Downgraded in urgency, not withdrawn. This audit read 110 URLs almost entirely through the direct trafilatura rungs, and the two hard failures were anti-bot challenges no transport clears — so the 08-24 escalation ("do nothing now has a verification cost") overstates the position as of today. What remains true is that jina-pinned hosts are unreadable and CERT/CC needed the reader this fire. A monitoring hook that alerts at the warning threshold is still the cheapest of the three options.
2. **Investigate the missing fires.** *(Carried from 2026-08-24.)* Still open and now sharper: there is no run record for 25, 26 or 27 August, and the 08-28 fire opened with a 91 h catch-up. The self-heal worked, but **the two KEV misses this audit recovered both fall inside that gap** — a wide catch-up window is exactly where an attentional sweep drops rows, which is the case v4.8's step 6b is built for. Not a cadence judgement; a question of whether the scheduler is dropping fires.
3. **Populate the org-profile watchlists.** *(Carried from 2026-07-11 onward, six audits.)* Still empty, so the product and supplier sweeps remain no-ops. This window's case is WatchGuard Firebox: a product watchlist surfaces a pre-auth VPN RCE at first sight instead of leaving it to an audit three days later.
4. **Recommendation 4 of 2026-08-24 (widen the immutability-exception repair class) is retired as obsolete.** It described a world where a superseded `cves[]` record kept its wrong machine surface because `update_of` did not rewrite the original. v4.0's changelog model fixed that structurally — this audit corrected `cves[].epss`, `cves[].auth`, `cves[].status`, `cves[].fixed` and `cves[].affected` in place, on the live records, with the changelog carrying the history. Nothing is left to widen.
5. **NEW — decide whether the 08-28 cohort warrants a second full truth pass.** This audit verified all 44 in-window entries and found defects in 25. The same fire published 36 entries, and its verification loop landed seven residuals under a watchdog cut. The cohort has now had one network-enabled cold read; the defect rate suggests a second pass over the entries this audit found clean would not be wasted. This is an operator call because it costs an audit slot.

6. **NEW — sweep the ~95 entries carrying production-process self-reference in `sourcing_note`.** Finding 5. The new check stops the bleeding but deliberately does not fire on history. The sweep is mechanical (each instance is a deletion or a date substitution, no claim changes) but it is ~95 changelog records, so it is an audit slot's work rather than something to fold into a fire. An operator call because of that cost.


---

## Watch items

**Carried forward and re-checked:**

- **Boston Scientific — stays open.** No party has named a mechanism, actor, access vector or leak-site claim. The company's 2026-08-29 update names CrowdStrike as IR firm and scopes the intrusion to on-premise systems only. One search result appeared to attribute it to ShinyHunters; it could not be corroborated and looks like a summariser conflating an unrelated April 2026 case. **Resolution condition unchanged:** any source naming attacker behaviour, which is what an evidence-bound ATT&CK mapping requires.
- **Afpa — stays open, unpublished.** Unchanged since 2026-08-09: still only the Cybernox forum claim, no first-party statement or authority confirmation.
- **Zurich District Court verdict — stays open, on schedule.** Verdict expected September, 2026-09-10 unchanged. Publish the verdict, not further procedural days.
- **Model-override ladder still untested** *(from 2026-08-24)* — **stays open.** No fire in this window lost a spawn, so the ladder remains unexercised. Nothing to measure.
- **Siemens S7 joint advisory re-read, CVE-2026-16242 OpenShift, and the Keycloak Red Hat product-state correction** — all three remain open backlog rows, none re-probed this fire.

**New:**

1. **ATT&CK mapping density on `threat` entries.** v4.8 decoupled the mapping from prose length. Re-measure next audit against the table in finding 2. If `threat` density has not recovered toward 8–12, the cause is not the prompt coupling and the model hypothesis needs testing directly. **Resolution:** two consecutive windows at pre-v4.2 density, or a confirmed alternative cause.
2. **`inside-it-ch` unreadable at essential tier.** Two consecutive fires, every transport 403. It is blocking a possible Swiss hospital-group incident. **Resolution:** a working recipe recorded in the source notes, or demotion with the reason stated — an essential-tier source nothing can read is worse than an honest gap, because the essential-coverage check reports it as attempted.
3. **Quotation fidelity instrumentation.** Six of eleven factual errors this window were quote or attribution drift, and F3 was already rising before it. The prompt already says quote verbatim, so another prompt line will not help. **Proposal for the next audit to ship if the rate holds:** a `check_run.py` check that, for every `evidence[]` record whose source URL was fetched in the run, greps the captured body for the quote as a contiguous substring and FAILs on a miss — mechanical, cheap, and exactly the class of defect no cold reader reliably catches by eye. **Resolution:** the check ships, or two windows show the rate falling without it.
4. **The eight backlogged coverage items.** Each is an open row with its gate reasoning. **Resolution:** each row struck by the fire that publishes it or by a stated judgement that it no longer clears the gate. The two KEV items should be struck by the next fire; if they are still open at the next audit, step 6b did not work.
5. **`2026-08-29/servicenow-ai-platform-four-unauth-cvss10-flaws` sourcing_note.** Carries field names and a house-rules self-reference — the 08-28 fix's own defect class, one fire later, in a field its examples did not name. Not corrected here (no factual error, and this fire's correction budget went to the eleven entries that carried one). **Resolution:** rewritten on next touch, or the v4.2 rule's field list extended if a second instance appears.
