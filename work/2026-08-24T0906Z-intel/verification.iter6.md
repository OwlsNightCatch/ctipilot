**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-14T07:40:08Z · ended_at=2026-08-14T07:47:10Z · duration_seconds=422

## Verification report — 2026-08-14T0417Z-intel (iteration 6)

### Priority focus: GeoServer entry (zero prior verification)

All three inline evidence quotes and the two inline body quotes were re-derived against the live pages via the bridge fetcher (`tools/fetch_source.py url`), not just re-summarised:

- **The Hacker News** (thehackernews.com/2026/08/unpatched-geoserver-zero-day-targeted.html): raw HTML confirms every quoted string verbatim, including the @q1uf3ng attribution, the "sa [system administrator]" bracket, the watchTowr "hundreds of attempts ... small pool of IP addresses" line, and Jake Knott's "probe to identify vulnerable systems ... triggering errors and not proceeding further" line. The article names no CVE for the current flaw (only references CVE-2024-36401 as unrelated background); entry correctly ships `cves: []`.
- **CSO Online** (JSON-LD `articleBody`, fetched raw): confirms the "administrator permissions on Microsoft SQL Server" mechanism, the "another user confirmed on X ... reproduce the flaw in a non-default configuration" claim (matches the entry's "second-hand claim on X of reproduction ... which no technical write-up corroborates"), and "haven't seen any malicious payloads or commands being sent, and the attempts look more like probes" — matching the entry's "probing that triggers errors and goes no further, not payload delivery" framing exactly.
- **OSV GHSA-7g5f-wrx8-5ccf** (raw page): confirms the exact 2023 patched-version list (2.21.4, 2.22.2, 2.20.7, 2.19.7, 2.18.7) and the quoted scoping clause is a verbatim substring of the page (see F11 below for a cosmetic note on where the copy starts).
- **geoserver.org/blog/**: confirms the top/most-recent post is the "GeoServer 3.0.0 Release" dated 2026-06-11, with no advisory for this flaw — matches the entry's claim precisely.

**Claim-strength check (as requested):** confirmed correct throughout — "hundreds of attempts" is consistently presented as watchTowr's own reported figure, never as independently confirmed; the observed activity is consistently framed as probing/fingerprinting, never exploitation; RCE is consistently conditioned on the database account holding SQL Server admin rights, never asserted as a property of the flaw itself.

**No-CVE check:** confirmed — `cves: []`, and no CVE identifier of any kind appears anywhere in the entry (frontmatter or body). The entry's own sourcing_note correctly flags and rejects the circulating (wrong) SAP Commerce Cloud CVE mapping.

**2023 history claim:** confirmed accurate against the OSV/GHSA record — the 2023 jsonArrayContains fix covered PostGIS and Oracle datastores only; the current reporting centres on a Microsoft SQL Server backend, a genuinely different datastore. The entry does not overstate what the 2023 history implies (it correctly frames it as "being patched against the 2023 issue says nothing about today's").

**priority/confidence:** `priority: high` / `confidence: medium` is well calibrated — unpatched, no CVE, single-vendor self-reported telemetry relayed through press rather than published research, no independent confirmation of exploitation, but a real pre-auth SQLi-to-possible-RCE with active scanning against internet-facing European public-sector infrastructure. The single action item (inventory + datastore-privilege reduction) is concrete, do-now, and derived directly from the finding's own risk model.

### Unsupported / hallucinated facts

**F14.** The entry's sourcing_note states "the flaw is not on the CISA exploited-vulnerabilities catalogue, which does carry **two** earlier GeoServer entries," and the body states "**Two** GeoServer flaws are already on the exploited-vulnerabilities catalogue, and the mass exploitation of the 2024 one is the precedent this most resembles." I fetched the live CISA KEV catalogue (`python3 tools/fetch_source.py cisa-kev`) and it carries **three** GeoServer entries: CVE-2025-58360 (added 2025-12-11, XXE via GetMap), CVE-2024-36401 (added 2024-07-15, GeoTools eval injection), and CVE-2022-24816 (added 2024-06-26, JAI-EXT code injection). Neither cited source states a specific count — The Hacker News says only "multiple vulnerabilities listed in CISA's Known Exploited Vulnerabilities catalog," with no number given. "Two" is an invented, incorrect quantifier appearing in two places. Trivial one-word fix ("two" → "three") in both the sourcing_note and the body paragraph.

### Editorial / less-is-more flags (advisory)

**F11.** The body's 2023-history quote — "jsonArrayContains</code> function, when used with a String or JSON field and with a PostGIS or Oracle DataStore (GeoServer 2.22.0+ only)" — is a verbatim substring of the raw OSV page (confirmed via bridge fetch of the raw HTML), but the copied span starts one character inside a `<code>` tag, leaving a stray `</code>` fragment visible at the front of the rendered quote. The fact and attribution are correct; this is a copy-paste hygiene nit, not a truth defect. Optional trim before publish.

### Prior-iteration deltas (iteration 5, Opus) — verified

1. **jwr entry, T1566.002 → T1566:** confirmed. `techniques[]` now reads `T1566, T1111, T1071.001, T1056.001, T1027` — no `.002` sub-technique present, and the body's delivery description is SMS-only (smishing via toll/postal/courier lures) throughout, consistent with the parent technique. No remaining unsupported ids.
2. **fortinet entry, T1078 removed:** confirmed. `techniques[]` is now `T1190, T1557, T1068` — no T1078. All three remaining ids are supported: T1190 (exploiting the internet-facing FortiWeb/FortiManager management interfaces), T1557 (FortiClient flaw requires a position to craft/alter DNS responses), T1068 (FortiClient flaw is classed by Fortinet as escalation of privilege).
3. **fortinet entry, FG-IR-26-163 clause/citation:** confirmed. Fetched `https://www.fortiguard.com/psirt/FG-IR-26-163` directly — the page is titled "HTTP/2 Bomb CVE-2026-49975," describes CVE-2026-49975 as an Apache HTTP Server (mod_http) memory-allocation flaw, and its affected-versions table names FortiPAM (1.0–1.9), FortiProxy (7.2/7.4/7.6) and FortiSwitchManager (7.2) exactly as the entry's clause states. The clause and its citation are now correct.

### Other nine entries — publishing-error scan

Read all nine remaining entries end-to-end plus spot-verified primary sources for the ones carrying the highest risk of overstatement (langflow update, checkpoint ransomware report — quotes verified verbatim against the live page; city-forum deep dive — quotes, the ShinyHunders attribution nuance, and the 560,000-events figure all verified verbatim against both Reco's own page and The Register's; dgfip breach — sourcing transparency checked; clop/windchill/philips update — hedging checked; beacon-crm update — reliability/credibility self-consistency checked; ncsc-uk bitlocker — confirmed the Nightmare Eclipse entity links are legitimate per the registry, YellowKey is explicitly named in both the actor and campaign registry summaries; haiwell and adobe entries — read for internal consistency and carve-out correctness).

Found no publishing error in any of the nine — no broken link, no fabricated fact, no wrong CVE, no unjustified priority. One new source was added to `sources/sources.json` this run (`reco-ai-research`), consistent with the "one new candidate source per run" rule; the other untracked hosts cited (CSO Online, Actu17, WKZO, Cryptika-adjacent search noise) are ordinary ad-hoc citations, not new tracked candidates, so no violation there either.

On the volume question: 13 entries in a ~26-hour window is high but each one clears the relevance/actionability gate on its own terms — five unpatched/actively-scanned vulnerabilities with genuine European public-sector or widely-deployed-tech exposure (GeoServer, FortiWeb, Langflow, Haiwell, Adobe Commerce), one hardening update with a real operational delta (NCSC UK BitLocker), two nation-state/organized-crime tradecraft pieces with explicit transferable-lesson framing (JWR, Armored Likho), one structural ecosystem report (Check Point), three breach/incident updates with genuine EU/public-sector nexus or a materially new root-cause finding (DGFiP, Clop/Windchill/Philips-Shell, Beacon CRM), and one deep dive (City-Forum) that earns its length. None reads as padding; none is a marginal item riding along.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)

### Findings summary (machine-readable)

```yaml
- code: F14
  category: quantifier-without-source
  section: entries/2026-08-14/geoserver-jsonarraycontains-unauth-sqli-zeroday-unpatched.md
  item: "GeoServer jsonArrayContains zero-day"
  url_or_quote: "sourcing_note: 'the flaw is not on the CISA exploited-vulnerabilities catalogue, which does carry two earlier GeoServer entries.' / body: 'Two GeoServer flaws are already on the exploited-vulnerabilities catalogue, and the mass exploitation of the 2024 one is the precedent this most resembles.'"
  summary: "CISA's KEV catalogue (fetched live via `python3 tools/fetch_source.py cisa-kev`) carries THREE GeoServer entries, not two: CVE-2025-58360 (added 2025-12-11, XXE), CVE-2024-36401 (added 2024-07-15, GeoTools eval injection), and CVE-2022-24816 (added 2024-06-26, JAI-EXT code injection). Neither cited source states a specific count. One-word fix in two places ('two' -> 'three')."
- code: F11
  category: editorial-advisory
  section: entries/2026-08-14/geoserver-jsonarraycontains-unauth-sqli-zeroday-unpatched.md
  item: "GeoServer jsonArrayContains zero-day -- 2023 history quote"
  url_or_quote: "'jsonArrayContains</code> function, when used with a String or JSON field and with a PostGIS or Oracle DataStore (GeoServer 2.22.0+ only)'"
  summary: "Verbatim substring of the raw OSV page but the copied span starts mid-tag, leaving a stray '</code>' fragment. Cosmetic only."
```
