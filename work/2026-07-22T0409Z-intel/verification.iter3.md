**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-22T05:14:13Z · ended_at=2026-07-22T05:22:21Z · duration_seconds=488

## Verification report — 2026-07-22T0409Z-intel (iteration 3, confirmation pass)

Cold read of all 7 new entries + run record. Every inline source URL fetched
(CISA/NCSC-CH/NCSC-NL/BSI via bridge; NCSC-NL CSAF JSON parsed directly). All CVE ids
and CVSS scores cross-checked against the owning CSAF authorities (NCSC-NL 0251/0237),
not just the roundup posts. Every frontmatter evidence[] quote confirmed a verbatim
contiguous substring of the fetched page (incl. the Dutch NCSC quote with its literal
double space 'van  SharePoint', and the two long XEntry quotes WebFetch had truncated —
verified verbatim against the raw Securelist page). Frontmatter⇔body, technique mapping,
priority, action discipline, Admiralty classification, org-triage(null, correct),
single-source flag (XEntry), update-vs-new decisions, and IOC discipline all check out.

Two findings — one truth, one editorial. This confirmation pass therefore refutes the
iter-2 CLEAN.

### Quantifier without source
- **F14** — `south-korea-knda-elearning-zero-day-breach`. Body: "up to ~10,000 records
  ... — reported as roughly **2,500 diplomats posted worldwide and 350 serving overseas
  officials** — including names, user IDs...". The '2,500 / 350' breakdown is in none of
  the three cited sources: Korea Herald (targeted re-fetch) does not mention either
  figure; DailySecu explicitly lacks it and instead reports '일부 보도에서는 ... 약 6000명'
  (~6,000 in some reporting); Seoul Shinmun body says only '최대 1만명' (up to 10,000) —
  its 2500/350 string occurrences are unrelated article URLs and an iframe height=350.
  The quantifier is unsupported and mildly contradicted (~6,000). Remediation: drop the
  '2,500 / 350' clause or cite a source stating it. Truth-class.

### Missed angles
- **F10** — whole-run. The CISA KEV alert cited by the Langflow entry
  (https://www.cisa.gov/news-events/alerts/2026/07/21/cisa-adds-four-known-exploited-vulnerabilities-catalog)
  added four CVEs: Langflow (published), DD-WRT CVE-2021-27137 (documented drop), and two
  WordPress **Core** CVEs — CVE-2026-63030 (Interpretation Conflict) and CVE-2026-60137
  (SQL Injection), now actively exploited. WordPress Core is widely deployed across the
  Swiss/European public sector; only DD-WRT was triaged in the run record, the two
  WordPress Core additions are neither covered nor named as a drop. Assess and either
  publish a brief entry/update or document the drop. Editorial-class (mild).

### Confirmed accurate (no finding)
- Langflow: CVE-2026-0770 KEV addition + evidence quote verbatim (CISA); ZDI-26-036
  root-cause/CVSS 9.8; NCSC-2026-0251 = 15 CVEs incl. 9202/8859/9135/7754/7755/8476;
  CSAF scores 9202=9.8(PR:N), 8859=9.9(PR:L), 9135=9.9(PR:L) match frontmatter
  auth/type/cvss exactly. iter-1 PoC-removal remediation holds (no poc-public claim).
- SharePoint 50522: CSAF 0237 CVSS 9.8 confirmed; Dutch machine-key quote verbatim
  (incl. double space); BleepingComputer quotes verbatim; PoC 'Janggggg' 2026-07-20.
  update_of target and empty-actions rationale sound.
- Zimbra: blog SNMP + mail-forwarding quotes verbatim; 9 issues; THN confirms no ITW and
  CVE-2026-50055=mail-forwarding bypass. (BSI CSAF unreachable — routine UA blocked, jina
  402; 10631/50054 sub-mapping unverified but corroborated for 50055 and non-overstating,
  no finding.)
- Everest/Stadler: both Swiss quotes verbatim; Halcyon confirms all 7 actor-background
  claims (iter-1 F5 remediation holds).
- XEntry: all 3 quotes verbatim; Securelist confirms every claim; single-source flag +
  credibility-2 correct.
- Cavern: both quotes verbatim; Securelist confirms LOW-confidence OilRig assessment +
  'no code reuse or infrastructure overlap' (iter-1 F4 remediation holds); Check Point
  corroborates Cavern Manticore / OilRig-Lyceum link.
- KNDA (other than F14): zero-day, 2022 launch, Feb-2026 discovery, vendor patch, 5-month
  disclosure gap, North-Korea-not-ruled-out — all confirmed across the three sources.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

### Findings summary (machine-readable)
```yaml
- code: F14
  category: quantifier-without-source
  section: south-korea-knda-elearning-zero-day-breach
  item: "South Korea KNDA e-learning zero-day breach"
  url_or_quote: "reported as roughly 2,500 diplomats posted worldwide and 350 serving overseas officials"
  summary: "2,500/350 breakdown in no cited source; DailySecu says ~6,000; drop or cite."
- code: F10
  category: missed-angle
  section: whole-run
  item: "Langflow CISA-KEV entry / run record coverage shape"
  url_or_quote: "https://www.cisa.gov/news-events/alerts/2026/07/21/cisa-adds-four-known-exploited-vulnerabilities-catalog"
  summary: "Two WordPress Core KEV additions (CVE-2026-63030, CVE-2026-60137) from the cited alert neither covered nor documented as a drop; assess/cover or document."
```
