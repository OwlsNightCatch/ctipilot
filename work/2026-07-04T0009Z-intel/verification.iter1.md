**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`) — env vars CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID unset; identified from runtime context.
**Timestamps:** started_at=2026-07-04T00:31:53Z · ended_at=2026-07-04T00:36:33Z · duration_seconds=280
**Self-telemetry:** webfetch_calls=6 websearch_calls=0 bridge_fetches=0 urls_checked=4 (2 primaries curl-fallback after WebFetch 503)

## Verification report — 2026-07-04T0009Z-intel (iteration 1)

Cold read of 2 new entries + run record. All 4 cited URLs fetched and confirmed live + specific + on-point. Sysdig and THN 503'd via WebFetch (UA-based bot block); both retrieved HTTP 200 via desktop-UA curl and verified in full text. Both entries are substantively solid; one editorial sourcing gap and one advisory nit.

### Claims missing inline citation
- **F5 — JADEPUFFER.** `CVSS 9.8` (title, summary, and frontmatter `cves[].cvss: "9.8"`) and the literal endpoint path `/api/v1/validate/code` (body + first action) appear in the entry but in NEITHER cited source. I fetched the Sysdig primary (full HTML, 291 KB) and the THN corroborating article (full HTML) this iteration: neither contains "9.8", "CVSS", "validate", or "/api/v1". Both describe the flaw functionally only — Sysdig: "CVE-2025-3248 is a missing-authentication flaw in its code validation endpoint that allows an unauthenticated attacker to execute arbitrary Python on the host." Both values are externally correct (NVD rates CVE-2025-3248 CVSS 9.8; the endpoint is the documented Langflow path), so this is an uncited-fact gap, not a fabrication (hence F5, not F4). Fix: add a corroborating advisory stating the CVSS + endpoint (Horizon3 disclosure / EUVD record) as a second corroborating source, or drop the unsourced "CVSS 9.8" from the headline. NOTE: the "fixed in Langflow 1.3.0" and "added to CISA KEV in May 2025" claims ARE sourced — verbatim in THN — and need no change.

### Editorial / less-is-more flags (advisory)
- **F11 — NetNut (Popa), advisory only.** The reused entity key `campaign:popa-vo1d-residential-proxy-botnet` is correct (no second key invented — good). But "NetNut", now the lead name in both new sources, lives only in the entity's `name` string, not in `aliases: []`. Consider adding "NetNut" (and "Popa") as formal registry aliases so future NetNut-named items link cleanly. Not a publish blocker.

### Verified clean (no findings)
- **All 4 URLs**: live, specific-article/advisory/PSIRT-class, on-point. No homepages/indexes. Primary sources are strong (Sysdig research blog; Google GTIG blog) — no NVD/CERT-only sourcing (no F6).
- **JADEPUFFER evidence quotes** #1 ("first documented case of agentic ransomware…") and #2 (CVE-2025-3248 missing-auth flaw) — verbatim substrings of the Sysdig page. Quote #3 (1.3.0 fix + KEV May 2025) — verbatim in THN. All body numbers confirmed in Sysdig: 31-second diagnose-correct loop, 1,342 Nacos config items via AES_ENCRYPT(), minioadmin:minioadmin, 30-min crontab beacon (port 4444), random-UUID AES key never persisted, Nacos default JWT signing key, MySQL OUTFILE/LOAD_FILE Docker-socket container-escape probe.
- **NetNut evidence quotes** — both verbatim in the GTIG blog (2M devices; 316 clusters in one week June 2026). FBI netnut.com seizure + Shadowserver partner corroborated by BleepingComputer (GTIG says only "FBI, Lumen, and others"; the entry sources those two claims to BleepingComputer, which states both). "also known as Popa" present in both sources — no F15 name-collision (same campaign, correctly matched to the June 21 entity).
- **Update-vs-new (F-none):** Popa entry correctly `update_of: 2026-06-21/krebs-and-qurium-tie-the-popa-android-tv-residential-proxy-b` (target file exists on disk; outside the 7-day dedup window so absence from prior_coverage.json is expected). Body is delta-only (law-enforcement action + 316-cluster scale); original entry untouched. Correct decision.
- **Priority calibration:** both `notable` correct. JADEPUFFER — novel AI-abuse framing but the initial-access CVE is a year-old KEV item with no new time-critical action; not `high`/`critical`. NetNut — a takedown/incident with no urgent defender action. Neither under- nor over-called.
- **Recency judgment (JADEPUFFER):** 3-day-old primary (Sysdig 2026-07-01) pegged to an in-window syndication is defensible — high technical substance, first-time non-recycled coverage, `event_date: 2026-07-01` honestly records the research date. No drop.
- **Org relevance (Swiss federal SOC):** both clear the bar — widely-deployed OSS (Langflow) + KEV CVE + transferable hardening for JADEPUFFER; residential-proxy/fraud-detection + managed Android-TV/IoT hunting for NetNut.
- **Style/hard rules:** no IOCs in either entry (the Sysdig C2 IP 45.131.66[.]106 correctly excluded; netnut.com is the takedown subject, not a detection IOC); English throughout; no workflow-internal language; no vanity metrics; frontmatter⇔body agree (summaries attribute the "first" claim to Sysdig's assessment — no F14 quantifier defect).
- **Missed angles:** none evident. Quiet 8h weekend window; S1/S2 zero in-window; ARToken drop (dup) and Armored Likho drop (out-of-window/weak nexus) both justified in the run record.

### Verdict
NEEDS_FIXES (truth: 0, editorial: 1, advisory: 1)

### Findings summary (machine-readable)
```yaml
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "JADEPUFFER — Sysdig autonomous LLM-driven ransomware via Langflow CVE-2025-3248"
  url_or_quote: "CVSS 9.8 (title/summary/frontmatter) and /api/v1/validate/code (body/actions)"
  summary: "CVSS 9.8 and the literal endpoint path appear in the entry but in neither cited source (Sysdig + THN both fetched in full; neither contains 9.8/CVSS/validate). Externally correct but uncited. Add corroborating advisory (Horizon3/EUVD) stating CVSS+endpoint, or drop unsourced CVSS from headline. 1.3.0 fix + KEV May-2025 ARE sourced (THN)."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "NetNut (Popa) residential-proxy botnet disruption"
  url_or_quote: "campaign:popa-vo1d-residential-proxy-botnet aliases: []"
  summary: "Advisory: reused key correct, but add 'NetNut'/'Popa' as formal registry aliases. Not a blocker."
```
