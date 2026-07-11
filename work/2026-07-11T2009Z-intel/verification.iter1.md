**Model:** Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-11T20:30:44Z · ended_at=2026-07-11T20:36:44Z · duration_seconds=360

## Verification report — 2026-07-11T2009Z-intel (iteration 1)

Scope: one new entry (`entries/2026-07-11/praisonai-agentic-framework-three-cves-code-exec-rce-ddli.md`) + run record. Read cold. Every cited URL fetched; all three CVE ids + CVSS scores cross-checked against NVD and EUVD; all four evidence quotes confirmed verbatim; affected/fixed ranges traced to the owning GHSA + NVD; dedup checked against prior_coverage.json.

### What verified clean (for the record)
- **All three GHSA primaries** (GHSA-2xv2-w8cq-5gxw, GHSA-9mp3-24cc-77mg, GHSA-wf65-4jjx-q444) fetched via jina — resolve, are specific advisory pages, and support their attached claims.
- **CVE ids + CVSS**: NVD confirms CVE-2026-61447 (CVSS 4.0 base 10.0, PR:N), CVE-2026-61445 (9.4, PR:L → post-auth), CVE-2026-60090 (9.3, PR:N), all VulnCheck-assigned, all published 2026-07-11. Entry's scores/auth match exactly. The entry's use of the VulnCheck CVSS 4.0 scores over the 3.1 primaries is transparently disclosed in `sourcing_note`.
- **Affected/fixed ranges**: GHSA-wf65 states "praisonai >= 3.10.0, <= 4.6.64" verbatim (matches entry); fixed 4.6.78 traces to NVD fix commit 3aa9cbc. Both endpoints authority-backed.
- **Evidence quotes** (all 4): contiguous verbatim substrings of the cited GHSAs.
- **EUVD ids** in sourcing_note (43182/43181/43175): EUVD-2026-43182 confirmed to map to CVE-2026-61447 via jina.
- **TheHackerWire corroborating URL**: specific article, resolves, confirms CVE-2026-61447 / CVSS 10.0 and the "No public PoC available" aggregator line that the run record correctly overrode with the PoC-bearing GHSA primaries.
- **techniques[]** T1190/T1059.006/T1059.004/T1552 — all active, all behavior-supported. **Priority `notable`** defensible (pre-auth RCE + PoC, but narrow deployment, no ITW). **verification: multi-source** correct. **classification A/2** defensible for a vendor-maintainer GHSA corroborated by NVD/EUVD. **actions[]** single concrete versioned upgrade task — not generic. **Dedup**: PraisonAI / CVE-2026-61447 / CVE-2026-44338 absent from 14-day prior coverage; `update_of: null` correct. Run-record's "prior disclosure (CVE-2026-44338)" reference verified real and PraisonAI-related.

### Unsupported / hallucinated facts
- **F4** — Entry: summary states "**All are reachable through prompt injection**"; body intro states the three CVEs "share one root cause: **the framework treats model output as trusted, so an attacker who can influence the LLM (via prompt injection in agent input, ingested documents, or tool results) reaches code execution**". This is not supported for **CVE-2026-60090** by its owning advisory GHSA-wf65, which I fetched: it frames the vector as "A caller that can influence collection creation dimensions" and "Applications that expose RAG collection creation, tenant workspace provisioning, plugin-managed vector-store setup, or similar **lower-trust configuration** … can let a **lower-privileged caller** append database statements … the attacker must influence the collection dimension." GHSA-wf65 contains no mention of prompt injection, LLM output, or model-output trust (and its author self-classifies the flaw "Medium severity"). The body's own per-CVE sentence for 60090 is accurate ("caller-supplied dimension value"), so the defect is confined to the summary's blanket "All are reachable through prompt injection" and the intro's unifying model-output-trust thesis generalising 60090's config-parameter injection into the prompt-injection class. Suggested remediation: scope the claim — e.g. "CVE-2026-61447 and -61445 are reachable through prompt injection; CVE-2026-60090 requires a lower-trust caller able to influence the vector-store collection dimension" — and qualify the shared-root-cause sentence so it does not assert 60090 stems from trusting model output.

### Editorial / less-is-more flags (advisory)
- **F11** — Source-record date drift (metadata only, does not block publish). The `sources[]` record for GHSA-9mp3-24cc-77mg carries `date: "2026-07-11"`, but GitHub renders "MervinPraison published GHSA-9mp3-24cc-77mg **Jun 25, 2026**". The reader-facing framing ("Three CVEs disclosed … on 2026-07-11") is accurate — NVD published all three CVE records 2026-07-11T14:16 — so `event_date` is right; only that one source record's `date` field is off by ~2 weeks. Main agent may correct the field to 2026-06-25 or leave it.

### Coverage / missed angles
No gap flagged. Quiet intraday window (gap 5.57 h); S2/S3/S4 returned zero after full sweeps; the one borderline item (Qilin/Retelit leak-site claim) was correctly excluded under the leak-site verification gate and logged as a watch item. No in-window source identified that the run should have surfaced. Coverage looks complete for the window.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)

The run is very strong on sourcing and accuracy — every CVE, score, version, and quote checks out against primary + NVD/EUVD. The one blocking issue is the over-generalised prompt-injection / model-output-trust framing applied to CVE-2026-60090, whose owning advisory describes a lower-trust caller-controlled config parameter, not an LLM/prompt-injection sink. Fixing the summary line and the intro thesis to scope the SQLi vector correctly resolves it.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "PraisonAI agent framework: three CVEs — CVE-2026-61447 / -61445 / -60090"
  url_or_quote: "summary: 'All are reachable through prompt injection'; body: 'share one root cause: the framework treats model output as trusted, so an attacker who can influence the LLM (via prompt injection …) reaches code execution'"
  summary: "GHSA-wf65 (CVE-2026-60090) frames the vector as a lower-trust/lower-privileged CALLER influencing the collection dimension (RAG collection creation / tenant provisioning / plugin config) with no prompt-injection or LLM-output nexus; scope the 'all are prompt-injection-reachable' summary line and the shared model-output-trust thesis so they do not cover 60090."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "PraisonAI agent framework: three CVEs — CVE-2026-61447 / -61445 / -60090"
  url_or_quote: "sources[] GHSA-9mp3-24cc-77mg date: '2026-07-11'"
  summary: "GitHub shows GHSA-9mp3 published Jun 25, 2026; source-record date field off by ~2 weeks. event_date (2026-07-11) is correct per NVD. Correct the field to 2026-06-25 or leave — non-blocking."
```
