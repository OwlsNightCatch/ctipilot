**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`) — CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID were unset in the container; identity taken from runtime configuration.
**Timestamps:** started_at=2026-07-03T18:31:50Z · ended_at=2026-07-03T18:38:22Z · duration_seconds=392
**Self-telemetry:** urls_checked=7 · webfetch_calls=7 · websearch_calls=2 · bridge_fetches=2

## Verification report — 2026-07-03T1809Z-intel (iteration 1)

Cold read of 3 new entries + run record. Every inline source URL fetched (WatchGuard PSIRT, BSI CERT-Bund, CCB Belgium via bridge, CWP changelog, Citizen Lab, The Record), the WatchGuard advisories index cross-checked, and both dedup context files consulted. All CVEs, versions, dates, entities, and both entries' evidence quotes traced to a source fetched in this iteration.

### What verified clean

- **cve-2026-13368-watchguard-fireware-iked-pre-auth-rce** — Primary WatchGuard PSIRT WGSA-2026-00023 supports every claim: CVSS 9.2, race-condition/use-after-free in `iked`, remote unauthenticated RCE, prerequisite = Mobile VPN with IKEv2 + external LDAP auth server, affected 11.0–11.12.4_Update1 / 12.0–12.12 / 12.5–12.5.18 / 2025.1–2026.2, fixed 2026.2.1 & 12.12.1, 12.5.x unresolved, 11.x EOL, no workaround/PoC/ITW (all corroborated via search of the PSIRT page). Evidence quote is a verbatim substring of the advisory. The "one of ten advisories, WGSA-2026-00014 through -00023" quantifier is CONFIRMED against the WatchGuard advisories index — exactly ten, all dated 2026-07-02, CVE-2026-13368 in -00023 (no F14). Entry correctly does NOT conflate this new UAF with the separate, actively-exploited late-2025 Firebox RCE (CVE-2025-9242 / WGSA-2025-00027) that dominates the search noise. priority: high is calibrated (pre-auth edge-appliance RCE, patch available, no ITW). verification: multi-source justified (vendor PSIRT primary + BSI relay; BSI URL is a specific advisory-detail URL that resolves, JS-rendered).
- **citizen-lab-pega-committee-mep-infected-with-pegasus** — Both evidence quotes are exact verbatim substrings of the Citizen Lab report ("We found with high confidence…October 21, 2022, and again on March 6 and 7, 2023." and the PWNYOURHOME NSKeyedArchive/HomeKit/MessagesBlastDoorService sentence). iOS 15.5, non-attribution (no Greek-government responsibility), and the Russian/Belarusian-exile-campaign overlap all supported by both Citizen Lab (primary) and The Record (corroborating). Registry entity incident:pegasus-mep-kouloglou-pega-committee-2026 exists and is correctly linked; no standalone actor:nso-group / malware:pegasus key exists to additionally link (checked registry). event_date 2023-03-07 is the underlying-event date — defensible under the pipeline.md definition ("date of the underlying event / primary publication"). priority: notable calibrated (historical forensic confirmation, no new technique, no time-critical action). The analytical link ("suggesting a single Pegasus customer with multi-country authorization") is source-supported and correctly hedged (no F13).
- **cve-2026-57517-control-web-panel-pre-auth-sqli-to-rce** — CCB Belgium primary resolves (direct WebFetch 403 is a UA block; canonical live page confirmed via `tools/fetch_source.py url`, matching the run record's successful bridge fetch). Both evidence quotes are exact verbatim substrings of the live advisory ("This blind SQL injection vulnerability in the userRes parameter…achieve remote code execution." and "There is no evidence of exploitation in the wild, however…high-priority risk."). CWP changelog corroborates version 0.9.8.1225 shipped 06/05/2026 (matches "silent fix ~2 months before disclosure"); it does NOT mention a security fix, consistent with the entry's "shipped silently" framing. priority: high calibrated. See F11 for a non-blocking carve-out-list note on the single-source designation.

### Editorial / less-is-more flags (advisory)
- F11 — CVE-2026-57517 (CWP). The `single-source-national-cert` carve-out is invoked, but CCB Belgium / CERT.be is not on the org-profile national-CERT carve-out list, and the carve-out's "primary disclosing party / owns the advisory" condition is not met for a third-party product CVE. CCB is nonetheless a legitimate national CSIRT; the advisory is detailed and both quotes verbatim-verified; the vendor fixed silently (no PSIRT to cite); the sourcing_note is fully transparent. Non-blocking — substance clears the reader's needs. Options for the main agent: reclassify to plain `single-source`, extend the org carve-out list, or leave as-is. Recorded so the choice is deliberate.

### Whole-run checks
- Dedup: neither CVE (CVE-2026-13368, CVE-2026-57517) appears in prior_coverage or cves_seen; the prior Citizen Lab entry (Cellebrite/UFED) is a distinct incident correctly referenced, not duplicated. update_of: null correct on all three. No entity-linking miss.
- Coverage shape: 3 operational entries, rolling 24 h = 7 (within band), 0 critical, deep-dive budget untouched — run record's justification checks out. Vulnerability inclusion gates honoured (both are pre-auth RCE, CVSS 9.2 / 9.8). borderline-drops (Rancher, GHES) correctly excluded and documented.
- Style: no IOCs, no vanity metrics, English throughout, no workflow-internal language in entries or run-record notes.

### Verdict
CLEAN — one F11 advisory item the main agent may leave. Zero truth defects, zero blocking editorial defects. All URLs live and supporting; all evidence quotes verbatim; all quantifiers, versions, dates, and entities traced to sources fetched this iteration.

### Findings summary (machine-readable)
```yaml
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-57517 — Control Web Panel: pre-auth blind SQL injection to web-shell RCE (CVSS 9.8)"
  url_or_quote: "verification: single-source-national-cert / primary: https://ccb.belgium.be/advisories/warning-cve-2026-57517-cvss-98-blind-sql-injection-control-web-panel-lets"
  summary: "CCB Belgium not on org carve-out list and not the disclosing party for a third-party CVE; carve-out not formally met. CCB is a bona fide national CSIRT, advisory detailed, both quotes verbatim-verified, vendor fixed silently (no PSIRT), sourcing_note transparent. Non-blocking; main agent may reclassify to single-source, extend the list, or leave as-is."
```
