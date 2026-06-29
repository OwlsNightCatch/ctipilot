**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-28T23:55:35Z · ended_at=2026-06-29T00:03:42Z · duration_seconds=487
**Self-telemetry:** urls_checked=38 · webfetch_calls=28 · bridge_fetches=2 · websearch_calls=3

## Verification report — briefs/weekly/2026-W26.md (iteration 4)

### Prior-iteration delta verification (iter3 F1–F5 remediations)

**Delta 1 — NCSC-NL libssh2 URL (F1):** Both `https://advisories.ncsc.nl/2026/ncsc-2026-0210.html` (§ 10 and § 3) resolve and land on the specific NCSC-NL libssh2 advisory covering CVE-2026-55200 and CVE-2026-55199. The § 3 item now cites both GHSA-r8mh-x5qv-7gg2 and NCSC-NL NCSC-2026-0210 — two-source ✓. **REMEDIATION HELD.**

**Delta 2 — libssh2 patch-status (F9):** The GHSA confirms fix commit 97acf3df. NCSC-NL confirms the advisory covers the fix. The § 3 prose now says "an upstream fix has landed (the GHSA references the fix commit), but tagged-release availability still varies" — internally consistent. The § 11 caveat explicitly states `patch-available` means "fix exists upstream," not "your appliance is fixed." **REMEDIATION HELD.**

**Delta 3 — Miasma date (F4):** Socket page is dated June 25, 2026 (confirmed by WebFetch — "Date: June 25, 2026"). Brief now says "on 2026-06-25 Socket reported." **REMEDIATION HELD — DATE CORRECT.**

**Delta 4 — Mastra date (F4):** BleepingComputer Microsoft-Mastra article dated June 20, 2026. Brief now says "(covered in the daily on 06-21)" — no false publish-date assertion remains. **REMEDIATION HELD.**

**Delta 5 — Keycloak headline (F5):** Keycloak 26.6.4 release notes confirm CVE-2026-11800 = "Authentication bypass via JWT algorithm confusion" and CVE-2026-9800 = "Authorization bypass in policy enforcer via incorrect URI comparison." The brief headline now reads "CVE-2026-11800 (JWT algorithm-confusion) and CVE-2026-9800 (policy-enforcer authz bypass)." These are correctly separated per the source. **REMEDIATION HELD.**

---

### Broken / unreachable URLs

**F1-a — ENISA EUVD pages return service-unavailable error (infrastructure)**

Section: § 3 (CVE-2026-12569 and CVE-2026-58053)
URLs:
- `https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-37831`
- `https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-58053`

Both return "The European Vulnerability Database application could not be loaded" — SPA load failure. The underlying claims are confirmed by the primary sources (The Hacker News for EUVD-2026-37831 / CVE-2026-12569; VulnCheck for EUVD-2026-58053 / CVE-2026-58053), so this is an infrastructure transient. **Advisory: monitor for recovery; if persistent before publication, replace with an alternate secondary or drop the EUVD citation.**

---

### Generic / oversight URLs (replace with specific article)

**F2 — EDPB URL resolves to a listing page, not the specific press release**

Section: § 10 (EDPB Article 33 consultation bullet)
Current URL: `https://www.edpb.europa.eu/news/news/2026/edpb-meets-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification_en`
Issue: This URL resolves to the EDPB news listing index, not the specific press release. The correct specific press release URL is: `https://www.edpb.europa.eu/news/edpb-meets-with-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification-template_en`
The correct URL resolves to the actual press release confirming the Article 33 template, consultation open until 5 August 2026.

---

### Citation does not support the claim

**F3-a — Scattered Spider sentencing "15–16 July" — source says 16 July only**

Section: § 10 (Scattered Spider TfL bullet)
Claim quoted: "Scattered Spider TfL sentencing is set for 15–16 July."
Source checked: `https://www.nationalcrimeagency.gov.uk/news/cyber-criminals-who-hacked-into-transport-for-londons-computer-network-are-convicted` (fetched this iteration)
What the source says: "They are due to be sentenced at the same court on 16 July." — only one date, not a two-day span.

**F3-b — NL Digital Government URL does not support specific Tweede Kamer approval date**

Section: § 9 (Netherlands NIS2 item)
Claim quoted: "the Tweede Kamer approved the Cyberbeveiligingswet on 15 April 2026, with entry into force 1 July 2026."
Source cited: `[NL Digital Government]` at `https://www.nldigitalgovernment.nl/nis2-directive-cyberbeveiligingswet-cbw/`
What the source says: "expected in Q2 2026" — no specific approval date, no confirmation of 1 July entry into force. The 15 April 2026 date IS accurate (confirmed by WebSearch via rijksoverheid.nl), but the cited NL Digital Government URL does not carry it. The uComply URL (co-cited) confirms 1 July entry into force but not the specific 15 April date.
Severity: The "15 April" date is verifiable externally; the URL mismatch is an attribution gap, not a hallucinated fact. The main agent should add rijksoverheid.nl as the source for the approval date.

**F3-c — Netherlands NIS2 characterised as "done" when Eerste Kamer vote was still pending**

Section: § 9 (Netherlands NIS2 item)
Claim quoted: "The Dutch transposition is done: the Tweede Kamer approved the Cyberbeveiligingswet on 15 April 2026, with entry into force 1 July 2026."
Issue: As of the brief's publication date (2026-06-28), the Eerste Kamer had NOT yet voted — the plenary was scheduled for 6–7 July 2026 (WebSearch confirmed via Eerste Kamer legislative tracker). Describing the transposition as "done" when the Eerste Kamer approval was still pending is technically incorrect. The entry into force date of 1 July 2026 pre-dates the Eerste Kamer vote date. Note: the uComply source says "expected to take effect July 1, 2026" — a conditional phrasing the brief has firmed into a declarative.

**F3-d — CVE-2026-46331 "weaponised PoC within a day of assignment" not supported by cited source**

Section: § 3 (Linux kernel LPE item)
Claim quoted: "a companion `tc act_pedit` out-of-bounds write (`pedit COW`) gained a **weaponised PoC** within a day of assignment"
Source cited: `[Red Hat RHSB-2026-008]` at `https://access.redhat.com/security/vulnerabilities/RHSB-2026-008`
What the source says: No mention of a weaponised PoC — the bulletin describes the flaw and mitigation (blacklisting the module) but does not reference any proof-of-concept. The claim is accurate (WebSearch confirmed a weaponised PoC by researcher Massimiliano Oldani, published June 17, 2026, the day after CVE assignment), but the cited source does not support it. A source covering the PoC (e.g., The Hacker News `https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html`) should be added or substituted.

---

### Unsupported / hallucinated facts

No hallucinated facts found. All major named entities, CVEs, threat actors, victim names, counts, and dates checked in this iteration are supported by the cited sources (with the specific attribution issues in F3-a through F3-d above).

---

### Claims missing inline citation

No additional missing citations found beyond F3-d above.

---

### Strengthen primary source

No NVD/MITRE-only sourcing issues found.

---

### Drop (low relevance / off-audience / not weekly content)

No items recommended for drop. All items pass W-PD-1 (inaction=incident / cross-day pattern / strategic horizon).

---

### Needs more research

No significant gaps identified. The brief's § 11 coverage notes appropriately flag the known gaps (databreaches-net 403, Mandiant RSS IncompleteRead, inside-it.ch Cloudflare).

---

### Surface contradiction

**F9 — inside-it.ch "Switzerland second-most-targeted European country" — source is 403 / unverifiable; ESET source does not corroborate**

Section: § 0, § 8 (The Gentlemen)
The brief attributes "Switzerland the second-most-targeted European country" to "Check Point data, reported by Swiss tech press" via `[inside-it.ch]`. The inside-it.ch URL returns HTTP 403 via both WebFetch and the bridge fetcher in this iteration. The ESET WeLiveSecurity source (fetched this iteration) does NOT mention Switzerland as second-most-targeted — it describes targeting across "Southeast Asia, South America, and Western Europe" with "unusual countries like Thailand, Brazil, and France" and explicitly states the group is "notably not US-focused."

This is not a confirmed contradiction (the Check Point data may well say Switzerland), but the supporting source is unverifiable in this iteration and the secondary source (ESET) does not corroborate the Switzerland-ranking claim. The brief does correctly attribute it to "Check Point data, reported by Swiss tech press" — the attribution chain is transparent. This is surfaced as a consistency note for the operator, not a hard editorial defect.

---

### Missed angles

**F10 — Gitea companion CVE-2026-20896: no source linked**

Section: § 3 (Gitea act_runner item)
The brief mentions "The companion Gitea-core auth bypass via X-WEBAUTH-USER (CVE-2026-20896, fixed in 1.26.3/1.26.4)" in the prose but the footer Source does not include a link to the Gitea release notes for CVE-2026-20896. The cited release notes URL is `https://blog.gitea.com/release-of-1.26.3-and-1.26.4` — this appears in the brief prose as a parenthetical link but not in the footer Source line. This is consistent with the brief's design (the footer sources the primary CVE; the companion mention is inline). This is an advisory note only.

Suggested search for coverage gap: "MISP 2.5.42 CVE exploit" — noted as "folded into §§ 3–4" in § 11, but no MISP entry appears in the vulnerability roll-up. A brief check: the ILIAS SQLi (CVE-2026-12789) is mentioned in § 4 education section with BSI sourcing — that is adequate coverage.

---

### Editorial / less-is-more flags (advisory)

**F11-a — NCSC-CH security-hub hash-fragment URL is opaque to external verification**

Section: § 3 (Cisco SD-WAN item)
URL: `https://security-hub.ncsc.admin.ch/#/posts/12579`
This is a JavaScript SPA with a hash-fragment route — `fetch_source.py` and WebFetch both return the HTML shell only; the post content is loaded dynamically. The claim ("NCSC-CH posted on it, giving it direct Swiss relevance") is plausible and consistent with NCSC-CH's coverage of Cisco SD-WAN vulnerabilities, but the URL cannot be independently fetched by downstream readers or automated tools. Advisory: if NCSC-CH publishes a static permalink for the post, use that; otherwise, this is acceptable as a NCSC-CH platform limitation.

**F11-b — "seven US health systems" claim — cited source names only two; the number is confirmed by Becker's Hospital Review (not cited)**

Section: § 4 (Healthcare sector)
Claim: "[Xsolis] affecting 1,396,519 patients across seven US health systems"
Primary cited source (`hipaajournal.com`) names only two health systems (VHC Health, Rochester Regional Health). "Seven" is confirmed by Becker's Hospital Review (`https://www.beckershospitalreview.com/healthcare-information-technology/cybersecurity/1-4-million-patients-7-health-systems-caught-in-ai-company-data-breach/`). Advisory: add Becker's as a co-source or adjust the wording to "multiple US health systems" if the additional source is not added.

---

### Single-source items missing [SINGLE-SOURCE] flag

**F12 — Swiss Post Cybersecurity item already carries `[SINGLE-SOURCE]` flag — confirmed correctly flagged**

§ 7 § "Swiss Post Cybersecurity — inaugural Swiss Threat Landscape Report `[SINGLE-SOURCE]`" is correctly flagged. No other single-source items without the flag identified.

---

### Analytical-link-as-fact

No F13 findings. All actor-to-TTP and actor-to-victim connections checked this iteration are supported by the cited sources.

---

### Quantifier without source

**F14 — "15-16 July" is a quantifier not supported by the cited source** — covered in F3-a above.

No additional F14 findings.

---

### Name-collision unflagged

No F15 findings. The Miasma / "Mini Shai-Hulud" names are consistent entities across cited sources (Socket confirms same worm lineage).

---

### Verdict

NEEDS_FIXES (truth: 4, editorial: 2, advisory: 3)

Truth findings (F3-a, F3-b, F3-c, F3-d):
- F3-a: Sentencing date "15–16 July" — source says 16 July only
- F3-b: NL Digital Government URL doesn't support the 15 April Tweede Kamer date (attribution gap)
- F3-c: Netherlands NIS2 described as "done" when Eerste Kamer vote was still pending as of 06-28
- F3-d: CVE-2026-46331 "weaponised PoC" claim not supported by cited Red Hat source

Editorial findings (F2, F9):
- F2: EDPB URL is news listing, not specific press release
- F9: Switzerland second-most-targeted claim rests on 403-unverifiable inside-it.ch source without corroboration from the ESET source (which doesn't mention Switzerland rank); attribution is transparent but unverifiable

Advisory findings (F1-a, F11-a, F11-b):
- F1-a: ENISA EUVD infrastructure outage (transient)
- F11-a: NCSC-CH hash-fragment URL opaque to external fetch
- F11-b: "Seven US health systems" — number accurate but Becker's source not cited

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: looking-ahead
  item: "Scattered Spider TfL sentencing is set for 15–16 July"
  url_or_quote: "They are due to be sentenced at the same court on 16 July."
  summary: "NCA source says 16 July only; brief claims 15-16 July. Drop '15–' from the date."

- code: F3
  category: claim-not-supported
  section: policy-regulatory-horizon
  item: "Netherlands NIS2 — Tweede Kamer approval on 15 April 2026"
  url_or_quote: "https://www.nldigitalgovernment.nl/nis2-directive-cyberbeveiligingswet-cbw/"
  summary: "Cited NL Digital Government source says only 'expected Q2 2026', not 15 April. Add rijksoverheid.nl (https://www.rijksoverheid.nl/actueel/nieuws/2026/04/15/tweede-kamer-stemt-in-met-wetsvoorstellen-cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten) as the source for the specific approval date."

- code: F3
  category: claim-not-supported
  section: policy-regulatory-horizon
  item: "Netherlands NIS2 — 'The Dutch transposition is done'"
  url_or_quote: "The Dutch transposition is done: the Tweede Kamer approved the Cyberbeveiligingswet on 15 April 2026, with entry into force 1 July 2026."
  summary: "Eerste Kamer vote was still pending as of 2026-06-28 (scheduled for July 6-7). Brief should say 'The Tweede Kamer has approved ... pending Eerste Kamer ratification; entry into force expected 1 July' or note the bill is before the Eerste Kamer."

- code: F3
  category: claim-not-supported
  section: vulnerability-rollup
  item: "CVE-2026-46331 (pedit COW) — weaponised PoC within a day of assignment"
  url_or_quote: "a companion tc act_pedit out-of-bounds write (pedit COW) gained a weaponised PoC within a day of assignment"
  summary: "Cited Red Hat RHSB-2026-008 does not mention a weaponised PoC. Add or substitute a source that covers the PoC: https://thehackernews.com/2026/06/new-linux-pedit-cow-exploit-enables.html"

- code: F2
  category: generic-url
  section: looking-ahead
  item: "EDPB Article 33 breach-notification consultation closes 5 August"
  url_or_quote: "https://www.edpb.europa.eu/news/news/2026/edpb-meets-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification_en"
  summary: "URL resolves to EDPB news listing, not the specific press release. Correct URL is: https://www.edpb.europa.eu/news/edpb-meets-with-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification-template_en"

- code: F9
  category: surface-contradiction
  section: week-at-a-glance, long-running-campaigns
  item: "Switzerland second-most-targeted European country by The Gentlemen"
  url_or_quote: "Check Point data, reported by Swiss tech press, makes Switzerland the second-most-targeted European country"
  summary: "inside-it.ch source (sole primary) returns 403 and cannot be verified in this iteration. The ESET WeLiveSecurity source (also cited) does not mention Switzerland ranking at all — it names Thailand, Brazil, France as notable targeted countries. Attribution is transparent ('Check Point data, reported by Swiss tech press') but unverifiable. Add to § 11 as a single-source claim or add [SINGLE-SOURCE] tag to the inside-it.ch citation in § 8."
```
