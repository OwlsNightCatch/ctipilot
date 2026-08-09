**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-09T14:56:33Z · ended_at=2026-08-09T15:13:50Z · duration_seconds=1037

## Verification report — 2026-08-09T1315Z-audit (iteration 5, confirmation pass)

Read cold, without the iteration-4 report and without any deltas block. Scope: the four new entries,
the run record, and `docs/audits/2026-08-09-weekly-quality-audit.md`. Ground truth came from the cached
pages under `work/2026-08-09T1315Z-audit/pages/` plus live re-fetches where a cache could have drifted
(BankInfoSecurity, the CISA ICSMA HTML render, the raw CSAF), and from re-deriving the report's numbers
from the store rather than from the report.

### What was checked, and what it returned

**Entry sourcing — every cited URL of all four entries confirmed reachable and on-claim.**
`wallix.com/support-services/alerts/` (200, cached body still current), `cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0974/`
(200, "Paris, le 06 août 2026", first and last version 06 août 2026), `github.com/advisories/GHSA-rg76-677x-56q9`
(+ its API record, `published_at 2026-08-07T18:48:59Z`, `cvss_v3.score 9.0`), `coinspect.com/blog/ill-bloom-investigation/`
(dated August 5, 2026), `cisa.gov/news-events/ics-medical-advisories/icsma-26-216-01` (re-fetched live through
the bridge this iteration), the raw CSAF JSON (HTTP 200 live), and
`bankinfosecurity.com/progress-urges-sharefile-shutdown-over-credible-threat-a-32210` (re-fetched live, dated
July 13, 2026). No homepage, listing index or NVD/MITRE per-CVE page is cited anywhere.

**Every `evidence[]` quote is a contiguous verbatim substring of the page it is attributed to.** Checked with
`grep -F` / Python `in` against the fetched bodies, not by eye: all three WALLIX quotes (including the two-sentence
"Primary indicator …" string, which is contiguous on the page), all three CryptoJS quotes, all three Thermo Fisher
quotes (matched against the CSAF `remediations[].details` strings), and the single BankInfoSecurity quote. The one
body quotation that fails a naive substring test — "That change was reverted in 3.3.0 because it was considered a
breaking change, so projects tracking the 3.x line could resolve to newer versions that still contained the weak
generator" — fails only because the fetched markdown carries `**` emphasis inside it; with emphasis markers stripped
(i.e. as the page renders) it is exact. Not a defect.

**Named facts against the owning authority.** WALLIX: CVSS 4.0 10.0 and the full vector, CWE-290/CWE-287, the
12.3.0–12.3.6 / 12.4.0 vulnerable and 12.3.7 / 12.4.1+ patched table, the 12.0.x-and-below not-affected line, the
8.7 Access Manager score and vector, the "does not grant administration of the Bastions themselves" blast-radius
limit, `/var/log/wabaudit.log` and its field list, `client_ip="127.0.0.1"` + `type="User"` + `product_administrator`,
the September disclosure commitment, and the 12.4.1-only remediation sentence the entry flags as a self-contradiction —
all present verbatim on the vendor page. CERT-FR independently carries "Bastion versions 12.3.x antérieures à 12.3.7"
and the three Access Manager boundaries the entry attributes to it. CryptoJS: 2^39/2^47, the 3.1.2-4 (June 2014)
introduction, the 3.2.0/3.2.1 exception and the 3.3.0 revert, 4.0.0's native-API replacement, the scope rule, the
six-step reconstruction, the ~$5M lower bound as of 2026-07-13, and CVSS 9.0 — all on the GHSA record; the May-2026
start, "initially attributed to a single wallet product", the twelve-year age and the active-exploitation sentence
are Coinspect's, and the entry attributes each to the right side. Thermo Fisher: the CSAF holds exactly 15
remediation records (8 `vendor_fix`, 7 `mitigation`), the five per-product fixed versions and three EoL lines match
`cves[].fixed` word for word, the affected-version list matches the product tree exactly, CVSS 3.1 8.4 `AV:L`
matches, and `tracking.version: 1` with a single revision-history row confirms "revision 1 and has never been
revised". ShareFile: the KEV catalogue at `catalogVersion 2026.08.07`, `dateReleased 2026-08-07T16:45:47Z`, 1662
entries carries neither CVE-2026-2699 nor CVE-2026-2701; the eight other identifiers are present with `dateAdded`
2026-07-14, 2026-07-14, 2026-07-15, 2026-07-14, 2026-07-14, 2026-07-16, 2026-04-14 and 2026-07-01 — the exact
values and the exact order the entry prints. "5.12.4 or any version 6" is the cited article's own wording, and
"the same day Progress ordered every on-premises Storage Zone Controller powered off" is supported by "The alert
arrived the same day that independent honeypots began detecting active, in-the-wild attempts" plus "told customers
in a Friday security alert".

**Frontmatter ⇔ body, techniques, calibration.** All five distinct ATT&CK ids (T1190, T1555, T1136.001, T1110.002,
T1565.001) resolve as active, non-revoked and non-deprecated in the v19.2 pin, and each names behaviour the body
actually describes and a cited source supports — T1136.001 for the attacker-created `product_administrator` the
vendor's detection section names, T1110.002 for the offline enumeration of a reduced keyspace both CryptoJS sources
describe, T1565.001 for result files alterable after the run. No entry carries `org_triage`, none carries
`watchlist_hit: true`, all four carry a `classification` block inside the vocabulary. Priorities are defensible:
`high` for a CVSS 10.0 pre-auth PAM takeover with a dated public-disclosure clock, `high` for an actively exploited
twelve-year-old randomness flaw, `high` for a correction that reverses a "no patch exists" claim aimed at forensic
and clinical labs, `notable` for a KEV-status correction with no new exposure. No `critical` is claimed, correctly.
`actions[]`: two, two, one, none — each concrete and derived from the finding's own mechanics; the empty list on the
ShareFile correction is the right output and I am not asking for one. Both `update_of` targets exist, are the same
story, and carry only the delta; I read the superseded 2026-08-05 Thermo entry and confirmed it does assert
"There is no patch to wait for" in the body and `status: [no-patch]` / `fixed: "None stated …"` in frontmatter,
exactly as the correction characterises it. The 127.0.0.1 references are a loopback discriminator in a detection
concept, not attacker infrastructure — not an IOC finding.

**Sourcing-shape checks.** The Thermo correction cites only CISA (HTML + the CSAF of the same advisory) and says so:
`verification: single-source-national-cert` with a `sourcing_note` invoking the carve-out for the authority that owns
ICSMA-26-216-01 — the correct handling, so no F12. The ShareFile correction's `verification: single-source` +
`sourcing_note` names the KEV catalogue as the mechanical basis and explains why the catalogue is named by version
rather than linked (the URL pattern is gate-blocked). I considered whether `classification.reliability: A` overstates
a lone trade-press citation there, and concluded it does not: the load-bearing fact is the catalogue's own contents,
an A-grade first-party artefact, and the note says so explicitly. Considered and dismissed, not filed.

**Report and run-record numbers — re-derived, not re-read.** Every quantitative claim I could reproduce, reproduced
exactly: window population 80 entries / 65 operational / 34 `high` (52.3 %) / 71 actions (1.09 per operational entry)
/ 15 with none (23.1 %) / classification 80 of 80 / 3.64 mean techniques with zero empty on behaviour kinds, over 9
distinct producing run ids and 10 in-window run records; store baseline excluding this run's four entries 817
operational / 43.1 % / 0.58 / 61.6 %; previous window 60 / 41.7 % / 0.88 / 41.7 % / 4.27 / 71 of 71; 135 `cves[]`
records across the window (the report's "~135 CVE records"); 96 of 157 active sources with zero cited host in the
window; the 12 August records' iteration sequence 8, 8, 8, 4, 8, 8, 8, 5, 5, 4, 2, 2 with mean 5.83 and confirmed
two-model double-CLEAN on exactly 2 of 12, all 12 carrying `publish_status: ok`; per-10-run finding rates F3 49 → 38,
F4 59 → 65, F17 2 → 7, F18 0 → 3; 13 of 21 research-blog items duplicate; all six in-window KEV additions already
published (CVE-2026-8037, -63077, -18556, -34486, -9198, -18577 — the report's N-able ×2, Tomcat, Langflow, TeamCity,
Kemp LoadMaster); 16 open backlog rows, 8 + 8, none struck; 14 acknowledgment rows with exactly 3 dated 2026-08-09.
The "4 of 9" and "7 of 10" comparators are quoted faithfully from the 2026-08-02 report's own text.

**Claimed fixes against the working tree.** All present: v3.31 banners in `cti-run.md`, `weekly-summary.md` and
`quality-audit.md` with a matching CHANGELOG head; `state/coverage_backlog.md` new and populated; the four
`check_run.py` additions (`verification-rotation` across the whole chain, either-key waiver honouring, the
`credibility: 1` + `single-source*` FAIL, the composition-report rates against a 28-day baseline); ATT&CK pin at
19.2 with `upstream_modified 2026-08-05T21:33:58Z`; `coinspect-research` in `sources.json` as a candidate with its
working transport; both CVSS-provenance lessons in `.claude/memory/csaf-msrc-transcription.md`. The systemic claims
about other fires check out on their records: 2026-08-06 did run all five iterations on `cti-verification`/Opus,
did record its waiver at the top-level key, and did lose two research spawns to safeguards; the 2026-08-03 weekly did
lose four Sonnet-pinned research spawns and did recover them with a `model: opus` override; the pre-change
`check_verification_confirmation` docstring does say NEEDS_FIXES finals "are out of scope here". The 2026-08-03
weekly did list nine residual items, and spot-grepping five of them (pam_rootok, Digital Omnibus / Article 113,
SBOM minimum elements, forensic observability, OT-isolation) across 2026-08-03 → 2026-08-09 finds none published.

**Gate arithmetic.** `check_run.py "2026-08-09T1315Z-audit"` currently returns 38 pass · 0 warn · 1 fail, the single
FAIL being this confirmation pass's own absence; `--all` returns 21 pass · 1 warn · 0 fail · 14 acknowledged from the
same cause. Both reconcile exactly with the run record's "39 pass · 0 warn · 0 fail" and "21 pass · 0 warn · 0 fail ·
14 acknowledged" once the block is populated. The forecast is arithmetically correct, not optimistic.

**Coverage completeness.** I reconciled all 35 sweep returns against the store, the backlog and the report. G2 (5 of 5)
and G3 (8 of 8 non-duplicates) are fully accounted for — published, backlogged, or in the documented droppable list.
G1 leaves three items with no recorded disposition; I judge all three correct drops on their own facts and file the
omission as advisory only (F11 below). No item the sweeps surfaced is a genuine coverage gap left unaddressed, and
I found no additional in-window story of my own the run should have carried. Coverage looks complete.

### Editorial / less-is-more flags (advisory)

**F11.1 — run record generalises one backlog item's reason.** The record states: *"Eight further items cleared the
relevance gate but could not be composed inside this run's wall clock, and they were queued rather than dropped
alongside eight recoverable residuals seeded from the 2026-08-03 stand-down — sixteen open rows in total."* Two
paragraphs later the same record, and the report's § "Deliberately not published, and why (1)", give Wazuh 4.14.6 —
which the report's § Fixes lists first among those eight — a different and better reason: the CVE-identifier-to-advisory
pairing could not be confirmed, and `state/coverage_backlog.md` names that verification as its precondition. Nothing
here is false and the disposition recorded on disk is right; the friction is that one sentence attributes to wall
clock a decision the same document attributes to evidence. A half-clause ("seven for wall clock; Wazuh for an
unconfirmable CVE pairing") settles it. **No change required.**

**F11.2 — three sweep returns have no recorded disposition.** The report's § "Correctly-droppable borderlines" is
subtitled *"documented so the completeness judgement is auditable"* and documents five items. Reconciling every
non-duplicate return leaves three G1 items undocumented anywhere: n8n's 17 advisories of 2026-08-05 (all
authenticated, none pre-auth), the Cisco Catalyst SD-WAN August hardening release (five CWE-grouped CVEs, aggregate
CVSS 9.9 but `PR:L`, internally discovered, not known exploited), and Sophos Intercept X / Sophos Home for macOS
CVE-2026-18367 (local privilege escalation, no evidence of exploitation, auto-updating). I checked each against
PD-11 myself and agree with dropping all three — and the Cisco case is a *principled* asymmetry rather than an
oversight, since its already-published IOS XE sibling was `PR:N` where this batch is `PR:L`. The only gap is in the
auditability the section promises. One line naming the three, with "no exploitation, not pre-auth" as the reason,
would close it. **No change required.**

### Verdict

**CLEAN** — no truth findings, no editorial findings, two F11 advisory items the main agent may leave. The four
entries are accurate against their sources, correctly calibrated, correctly deduplicated and correctly classified;
the run record and the audit report make no quantitative claim I could not reproduce from the artefacts, and every
fix they claim to ship is in the working tree. This is an independent confirmation on Opus, not a rubber stamp: I
re-derived the disputed and the undisputed figures alike, re-fetched three sources live rather than trusting the
cache, and reconciled the coverage sweeps end to end before agreeing.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F11
  category: editorial-advisory
  section: run-record-notes
  item: "runs/2026-08-09/2026-08-09T1315Z-audit.md — § Verification & coverage notes"
  url_or_quote: "Eight further items cleared the relevance gate but could not be composed inside this run's wall clock, and they were queued rather than dropped"
  summary: "Blanket wall-clock reason covers all eight backlog rows, but the audit report's own § 'Deliberately not published, and why (1)' gives Wazuh 4.14.6 — the first of those eight — a different and better reason (the CVE-identifier-to-advisory pairing could not be confirmed). Advisory only; the disposition recorded on disk is correct."
- code: F11
  category: editorial-advisory
  section: audit-report — Correctly-droppable borderlines
  item: "docs/audits/2026-08-09-weekly-quality-audit.md"
  url_or_quote: "Correctly-droppable borderlines (documented so the completeness judgement is auditable)"
  summary: "Three G1 non-duplicate returns have no disposition anywhere (n8n 2026-08-05 advisory batch, Cisco Catalyst SD-WAN August hardening release, Sophos macOS CVE-2026-18367). All three are correct drops under PD-11 on my own reading; only the stated auditability is incomplete."
```
