**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-16T06:13:39Z · ended_at=2026-08-16T06:18:13Z · duration_seconds=274

## Verification report — 2026-08-16T0411Z-intel (iteration 6)

### Prior-iteration deltas verified (all eight remediations checked against saved captures / registry / backlog — all correctly applied)

1. Evooo1Bot C2 cipher/string-obfuscation rewrite — confirmed against `txt.fortinet-evooo.txt` line 867 ("multiple layers of string obfuscation using AES-256-CTR, ChaCha20, and XOR-based key derivation") and line 665 (port 443, "chosen to blend in with expected HTTPS traffic"). The entry's current prose correctly places the two ciphers on string obfuscation and leaves the C2 channel described only as encrypted-on-443, matching the source. `techniques[]` carries `T1573` (not `T1573.001`) — correct, since no channel cipher is named.
2. Evooo1Bot product names — confirmed `txt.fortinet-evooo.txt` lines 836/842 read exactly "Atlassian Confluence" and "WSO2 products"; entry's `affected_products[]` and action item now use exactly those strings, no invented sub-product names remain.
3. Akira Safe Mode EDR-blinding case — confirmed present in `state/coverage_backlog.md` Open table, correctly described as a pipeline-race miss (reported 2026-08-13, inside the *previous* fire's window) with detection guidance named; run record's iteration-5 findings entry matches.
4. macOS entry `verification: single-source-national-cert` with sourcing note claiming the carve-out — confirmed. Deliberately not cascaded to the SAP entry, which I independently confirmed carries a genuinely distinct third source (Onapsis) plus a first-hand SAP statement to BleepingComputer ("SAP told BleepingComputer it is aware of and investigating") — the non-cascade is correct.
5. Evooo1Bot persistence mapping — `T1546.004` (shell-config modification / profile.d) and `T1037.004` (RC scripts / rc.local) both present and both correctly map to body text ("a profile.d injection and an rc.local append").
6. Jewelbug `references: [2026-05-04/uat-8302-china-nexus-talos-se-european-government-victims]` — confirmed that entry's body line 45 names "Jewelbug" among UAT-8302's tooling-overlap clusters. No registry relation edge added between the two actors and no attribution claim leaked into the Jewelbug entry's prose — correct restraint.
7. Source registry gap — `fortinet-fortiguard-blog` confirmed added to `sources/sources.json` as a `candidate` (this run's one-per-run cap). **However, see F11 below: this remediation was incomplete** — a stale/consolidated source id survives elsewhere in the same run record's telemetry.
8. ExfilSquad headline/takeaway hedge — confirmed "potentially exposed" / "potential" is present in both the headline and the summary's "over 10,000 potential Power Pages instances."

### Unsupported / hallucinated facts

**F1 (per this report's own numbering, category `claim-not-supported`).** Entry `2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay`, body paragraph 2:

> "the Kubernetes ingress-nginx admission-controller flaw known as IngressNightmare (CVE-2025-1974), alongside PHP-CGI argument injection on Windows (CVE-2024-4577) and a Zyxel firewall command injection ([FortiGuard Labs, 2026-08-13](https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot))"

I re-fetched all three of the entry's cited sources this iteration and none of them use the name "IngressNightmare":
- `txt.fortinet-evooo.txt` (FortiGuard primary, saved capture): `grep -i nightmare` returns zero hits; the source's own table (line 841) reads only `CVE-2025-1974 Kubernetes ingress-nginx /apis/networking/v1/ingresses` — no name attached.
- BleepingComputer corroborating source (re-fetched this iteration via `fetch_source.py url`): body text reads only "Kubernetes ingress-nginx" with no CVE id and no name.
- The Record corroborating source (re-fetched this iteration via `WebFetch` with the outbound-links template): confirmed explicitly — "IngressNightmare": Not mentioned; "CVE-2025-1974": Not mentioned; "ingress-nginx": Not mentioned.

The CVE id itself is correctly sourced to FortiGuard. The name "IngressNightmare" is a real, industry-recognized name for this flaw class, but it is not stated by the citation attached to it, or by either other source on the entry — this is exactly the per-citation-adjacency defect class (truth check 2d): a true fact attached to a citation that does not carry it. Fix: either drop "known as IngressNightmare" (the CVE id alone is sufficient and fully sourced), or cite an independent source that actually uses the name.

### Editorial / less-is-more flags (advisory)

**F2 (category `editorial-advisory`).** The run record's telemetry still carries a stale/consolidated source id in two places: `sub_agents.followup-completeness.sources_attempted` (line 68: `..., sansec, techcrunch, ...`) and `bridge_uses` (line 142: `{id: sansec, method: url, outcome: ok}`). `sources/sources.json`'s own `sansec-research` record documents this explicitly in its 2026-06-20 audit note: *"CANONICAL Sansec entry (duplicate id `sansec` consolidated here)"* — i.e., `sansec` is a retired id and the canonical one is `sansec-research`. This is the same defect class iteration 5's F11 remediation #7 claimed to have fully corrected ("the two telemetry ids that named non-existent registry records corrected or removed") — one instance evidently survived. Advisory only (run-record telemetry hygiene, not reader-facing), but worth sweeping since it directly repeats a just-claimed fix. Not blocking.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)**

One truth-class finding (F3-equivalent, the IngressNightmare naming unsupported by its citation) and one advisory-only telemetry note (stale `sansec` id, F11-equivalent). Both prior-iteration remediations (all eight) verified correctly applied via independent re-fetch of primary sources — no regression found. Everything else checked this iteration (all six entries' frontmatter⇔body agreement, CVE/CVSS/version tables against vendor advisories fetched fresh, classification/org_triage compliance, action-item discipline, entity registry links, dedup/update_of correctness, style discipline) came back clean.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: operational
  item: "evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay"
  url_or_quote: "the Kubernetes ingress-nginx admission-controller flaw known as IngressNightmare (CVE-2025-1974)"
  summary: "cited to FortiGuard Labs, 2026-08-13, but neither that source nor the two corroborating sources (BleepingComputer, The Record) use the name 'IngressNightmare' anywhere; only the CVE id is sourced. Re-fetched all three sources this iteration to confirm."
- code: F11
  category: editorial-advisory
  section: run-record-telemetry
  item: "runs/2026-08-16/2026-08-16T0411Z-intel.md"
  url_or_quote: "sub_agents.followup-completeness.sources_attempted: [..., sansec, ...]; bridge_uses: {id: sansec, method: url, outcome: ok}"
  summary: "sansec is a retired/consolidated source id per sources/sources.json's own audit note ('duplicate id sansec consolidated here' into sansec-research); this is the same defect class iteration 5's F11 #7 claimed fully fixed. Advisory only, not reader-facing."
```
