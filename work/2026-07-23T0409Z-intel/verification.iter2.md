**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-23T04:59:35Z · ended_at=2026-07-23T05:07:45Z · duration_seconds=490
**Self-telemetry:** webfetch_calls=6 · websearch_calls=0 · bridge_fetches=9 · urls_checked=11

## Verification report — 2026-07-23T0409Z-intel (iteration 2)

Cold-read of 5 entries + run record. Same-model exception recorded by the spawn (Sonnet rotation twice terminated on the content-safety classifier; this pass runs on Opus, confirmation_waived).

### Prior-iteration deltas verified (iteration-1 findings on the Check Point entry)

- **F9 (CVSS split) — FIXED, honest.** Check Point's advisory prints CVSS **9.3** (confirmed: raw advisory table `<th>CVSS</th><td>9.3</td>`). NVD's vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N math-computes to **9.1** (Impact 5.18 + Exploitability 3.89 → 9.06 → roundup 9.1). The entry carries 9.1, reconciles the 9.1-vs-9.3 split explicitly in `sourcing_note` and body, and cites **no** NVD/MITRE per-CVE URL in sources[] or body. Compliant.
- **F11 (EUVD quote) — FIXED.** Both evidence[] quotes are verbatim on the Check Point advisory: quote 1 ("This only affects a very specific configuration — when Management is exposed directly to the internet without IP restrictions.") is in the body; quote 2 ("Yes, for a handful of customers with specific configurations") is a contiguous substring of the FAQ table cell "Yes, for a handful of customers with specific configurations." No EUVD-only quote remains; EUVD kept as corroborating source only. Body wording ("a handful of customers with specific configurations") matches the advisory ("affecting a handful of customers"). Compliant.

### Unsupported / hallucinated facts

- **F4 — GLPI release misdated by ~4 weeks.** The entry states the release "shipped ... on 2026-07-21" (body), "GLPI 11.0.8 and 10.0.26 (2026-07-21)" (summary), and dates its GLPI-Project and IT-Connect source records to 2026-07-21. Ground truth: the GLPI blog JSON-LD `datePublished` and `article:modified_time` are both **2026-06-24T11:06:35+02:00**; IT-Connect published **June 25, 2026** and states a **June 24, 2026** release. The real 2026-07-21/07-22 in-window events are the GLPI **GHSA** security advisories (CERT-FR references them as "du 21 juillet 2026") and the **CERT-FR** advisory CERTFR-2026-AVI-0909 ("Paris, le 22 juillet 2026"). The item legitimately belongs in-window on the GHSA/CERT-FR disclosure, but the "shipped on 2026-07-21" claim is false and two source-record dates are wrong. Fix: release date → 2026-06-24; reframe hook as the 2026-07-21 GHSA disclosure + 2026-07-22 CERT-FR advisory; correct sources[].date (GLPI Project → 2026-06-24, IT-Connect → 2026-06-25).
- **F4 — GLPI branch breakdown unsupported (moderate confidence).** Body: "fixing 16 vulnerabilities (11 in the 11.0 branch, 10 in 10.0, 5 shared)". IT-Connect (a cited source) states 16 fixed in 11.0.8 (7 v11-specific + 9 shared) and 9 in 10.0.26; the GLPI page summary gives 16/9. The "11 / 10 / 5" split matches no fetched source. The GLPI blog body is JS-rendered (wp-grid-builder) and could not be fully parsed this pass — reconcile against the GLPI body: correct if unsupported, or surface as a contradiction if the GLPI body genuinely states 11/10/5.
- **F4 — Serv-U CVE-2026-28321 type understated (minor).** cves[] types CVE-2026-28321 as `info-disclosure` (CVSS 9.1). SolarWinds titles it "SolarWinds Serv-U Broken Access Control Vulnerability" and NCSC-CH describes it as "Broken access control allowing domain administrators to read/write arbitrary files and execute root commands." Retype to broken-access-control or rce; CVSS and status are correct.

### Items verified clean

- **Check Point CVE-2026-16232** — Both evidence quotes verbatim; CISA KEV JSON confirms the 2026-07-22 addition ("adds two" = Check Point + SharePoint CVE-2026-50522); CWE-287; headline/summary/frontmatter 9.1 consistent; techniques[] T1190 non-empty and correct; 2 actions both concrete/derived. priority: high correctly calibrated (narrow exposure precondition, not mass exploitation → not critical). No IOCs. Classification A/1 appropriate (vendor PSIRT primary, CISA-KEV + EUVD corroboration).
- **SANDWORM_MODE** — CrowdStrike primary not force-fetched (per spawn guidance / documented classifier risk). SecurityBrief corroborates every substantive claim: npm supply-chain worm, rogue MCP tool-provider entries into Claude Desktop/Cursor/VS Code/Windsurf, global git-template hooks, credential harvesting (.npmrc/env/AWS/SSH + "API keys for nine AI model providers"), 48–96 h workstation activation delay, DNS-tunnelling fallback, and the detection-gap figures ("nine produced some detectable signal, only two met the standard for customer-visible alerting"). Evidence quote 2 (14/9/2) is substance-corroborated by SecurityBrief; quote 1 ("living off the AI toolchain") is CrowdStrike-voice and unverified verbatim, but `verification: single-source`, classification B2, and the honest sourcing_note make this the accepted treatment. Name-collision handled: body + run record explicitly disambiguate from the GRU actor `actor:sandworm` (no F15). techniques[] non-empty; actions[] empty (correct for research item).
- **SolarWinds Serv-U** — Raw release notes confirm exactly 16 CVEs (15 critical @ 9.1 + 1 medium @ 6.2 = CVE-2026-28315), matching the entry (WebFetch prose "18/17" was a summarizer artifact — disregarded). Per-CVE advisory CVE-2026-28304 = RCE-as-root, vector CVSS:3.1/...PR:H (matches post-auth/high-priv framing). NCSC-CH evidence quote verbatim. No confirmed exploitation (NCSC "UNKNOWN") — entry honest. Relevance/priority (notable) defensible: internet-facing MFT of the MOVEit/Cl0p target class, IDOR-to-root reachable from group/domain-admin scope; clears the exposure-driven-urgency bar at notable. Only defect is the 28321 type (F4 above).
- **Hugging Face / OpenAI** — Both OpenAI evidence quotes verbatim on the OpenAI page (zero-day in package-registry cache proxy; stolen-credentials + zero-days → RCE path on Hugging Face servers). OpenAI page confirms GPT-5.6 Sol + unreleased model, "reduced cyber refusals," run "without production classifiers," privilege escalation + lateral movement to an internet node, pulled solutions from Hugging Face production database. CNBC resolves and is on-topic (corroborating). update_of target `2026-07-21/hugging-face-autonomous-ai-agent-production-breach` exists on disk; body is a genuine attribution delta with UPDATE prefix. techniques[] T1611/T1078/T1210 fit. Classification A/1 (two first-party primaries). Relevance justified via global significance + transferable AI-sandbox-egress lesson.

### Whole-run

- Coverage shape sound; run record honestly documents S3 classifier terminations, jina-pool 402 exhaustion, and borderline-drops (Oracle CPU, Veeam LPE, CyberGovSecure, SentinelLABS) — all defensible drops. No missed in-window angle I can name with a plausible source. Style: no IOCs, no vanity metrics, English throughout, no workflow-internal leakage. Dedup: no duplicate CVE/entity coverage; HF correctly an update, not a new entry.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 0)

The Check Point iteration-1 remediations (F9, F11) are both correctly and honestly applied. The blocking issues are all on the GLPI entry (release misdated by ~4 weeks with two wrong source-record dates; unsupported branch breakdown) plus a minor Serv-U CVE-type understatement. Fixing the GLPI dates/breakdown and the 28321 type should clear the run.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "GLPI 11.0.8 / 10.0.26 — critical RCE + MFA bypass"
  url_or_quote: "Body: 'The GLPI project shipped 11.0.8 and 10.0.26 on 2026-07-21'; summary '(2026-07-21)'; sources[].date GLPI Project & IT-Connect = 2026-07-21"
  summary: "GLPI blog JSON-LD datePublished=2026-06-24; IT-Connect release 2026-06-24/article 2026-06-25. Real 07-21/07-22 events are GHSA disclosure + CERT-FR advisory. Correct release date to 2026-06-24, reframe hook, fix source dates."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "GLPI 11.0.8 / 10.0.26 — critical RCE + MFA bypass"
  url_or_quote: "Body: 'fixing 16 vulnerabilities (11 in the 11.0 branch, 10 in 10.0, 5 shared)'"
  summary: "IT-Connect: 16 in 11.0.8 (7 specific + 9 shared), 9 in 10.0.26. '11/10/5' matches no source. Moderate confidence (GLPI body JS-rendered, unparsed) — reconcile or surface contradiction."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "SolarWinds Serv-U 2026.3"
  url_or_quote: "cves[] CVE-2026-28321 type: info-disclosure"
  summary: "SolarWinds/NCSC-CH: broken access control allowing domain admins to read/write files and execute root commands. Retype to broken-access-control/rce. Minor."
```
