**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-15T04:47:46Z · ended_at=2026-07-15T04:55:26Z · duration_seconds=460
**Self-telemetry:** webfetch_calls=5 · websearch_calls=0 · bridge_fetches=24 · urls_checked=15

## Verification report — 2026-07-15T0409Z-intel (iteration 1)

Cold read of 4 new entries + run record. Every inline source URL fetched (CISA advisories via bridge; MSRC React SPAs via jina; Rapid7/Proofpoint/Register via WebFetch + jina; GBHackers via jina after WebFetch returned empty). Every CVE id, CVSS, actor cluster, version, date, count and evidence quote cross-checked against a source read this iteration.

### Citation does not support the claim
- **F3 — xAI Grok Build CLI.** Sentence: "other users replicated it against whole home directories, exfiltrating SSH keys and a password-manager database ([GBHackers, 2026-07-14])." GBHackers does NOT carry that claim (it says only the test was "replicated with a second, unrelated codebase"). The claim IS supported by The Register (cited elsewhere in the entry): "Other Grok Build users reported similar results ... including one whose entire user directory, containing SSH keys, password manager databases, and more, was opened and uploaded." Fact true and in-entry sourced; defect is the misattributed inline citation. Fix: re-point that clause to The Register; the "reply OK" half of the sentence is correctly GBHackers-sourced (confirmed verbatim in GBHackers).

### Unsupported / hallucinated facts
- **F4 — CISA ICS batch, ABB T-MAC Plus version "4.0-25".** Entry asserts affected versions "4.0-24, 4.0-25" in title, summary, body, all four `cves[].affected` fields, and action 2. Cited advisory ICSA-26-195-03 names ONLY "ABB T-MAC Plus 4.0-24" (5 occurrences across product_tree + every per-CVE Affected Products block; confirmed in two independent renders). "4.0-25" appears in no render of the cited source. Could not read the raw CSAF JSON (GitHub raw path 404s, API blocked this session), so main agent should verify against the CSAF JSON / ABB PSIRT 9AKK108472A7840 and either drop "4.0-25" throughout or add the source that carries it.

### Editorial / less-is-more flags (advisory)
- **F11 — CISA ICS batch, CVE-2026-10577 sourcing_note.** Note claims "no v4.0 vector was published." The cited advisory page ICSA-26-195-04 publishes a v4.0 vector (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H, base 10.0) alongside the v3.1. Both are 10.0 → no published number wrong, no reader-facing claim affected; low materiality. Correct or delete the "no v4.0 vector" clause.

### Verified clean (no finding)
- **CISA Rockwell CVE-2026-10577:** CVSS v3.1 10.0, CWE-306, versions ≤3.003, sectors Energy/Water/Critical-Manufacturing, "no fixed firmware", both evidence quotes verbatim-contiguous, event_date 2026-07-14 (Initial Release) — all confirmed against ICSA-26-195-04.
- **ABB T-MAC Plus chain:** CVE-2025-14771 (9.9/CWE-552/PR:L), -14772 (8.8/CWE-639), -14773 (8.0/CWE-79 XSS), -14774 (7.4/CWE-863 DoS/AV:A/PR:N) all match ICSA-26-195-03; discloser "Angelo Catalani of ACN" confirmed; T-MAC product description verbatim from FAQ. (Version issue is F4 above.)
- **ABB Edgenius CVE-2026-31431 & Advant Master CVE-2025-13162:** 7.8/CWE-669 algif_aead local root fixed 3.2.4.1, and 4.4/CWE-427 DLL search-path — both match; Edgenius CVE correctly excluded from cves[] per prior May coverage; framing accurate.
- **Microsoft entry:** CVE-2026-55040 (9.1 critical, JWT auth-bypass, Stephen Fewer, Pwn2Own Berlin 2026, AD SID/UPN, chained RCE→August, Rapid7 PoC script shown → poc-public justified, evidence quote verbatim-contiguous); CVE-2026-55944 (9.8/PR:N pre-auth, "Exploitation More Likely", deserialization-Dynamics-NAV evidence quote verbatim); CVE-2026-50522 & -58644 (9.8, base vector PR:N BUT FAQ "an attacker authenticated as at least a Site Owner" — post-auth classification + documented discrepancy note are ACCURATE and honest). update_of target exists and covers CVE-2026-56155/56164. priority high justified.
- **Proofpoint entry:** all AADSTS codes (50034/50126/700016), the 700016-on-both-correct oracle, cluster names UNK_pyreq2323 (Jan–Mar 2026 / AWS / 700,000+) and UNK_OutFlareAZ (Dec 2025–Mar 2026 / Cloudflare / 3.7M), and both evidence quotes verbatim-contiguous against Proofpoint; corroborators Help Net Security + The Hacker News live and supportive. Recency exception (2026-07-13, 72h developing window) documented and sound. Registry entities exist.
- **xAI entry:** The Register both evidence quotes verbatim; Cereblab / Git-bundle / SpaceXAI GCS bucket / /privacy toggle / disable_codebase_upload flag / Musk pledge all confirmed; "reply OK" behavior confirmed in GBHackers. (Citation precision is F3 above.) Breach-bar cleared via transferable AI-coding-CLI governance lesson, framed around the lesson not the victim.
- **Classification / priority / actions:** Admiralty codes calibrated (CISA A/2, MSFT A/2, Proofpoint B/2, xAI B/2 — all defensible vs source nature and corroboration). No critical mis-fire; notable/high calls defensible. Action lists concise (≤2), concrete, finding-derived — no F18. techniques[] non-empty and source-supported on all four. No IOCs, no vanity metrics, no workflow language. No missed in-window angle identifiable with a nameable source (SAP/ShareFile already covered 07-14; jina-down coverage gaps reasonable).

### Verdict
NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CISA ICS batch (14 Jul) — ABB T-MAC Plus"
  url_or_quote: "'ABB T-MAC Plus 4.0-24, 4.0-25' vs advisory ICSA-26-195-03 (only 4.0-24)"
  summary: "Affected version 4.0-25 in no render of the cited advisory; drop it or add a source that lists it."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "xAI Grok Build CLI repo exfiltration"
  url_or_quote: "'... whole home directories, exfiltrating SSH keys and a password-manager database ([GBHackers, 2026-07-14])'"
  summary: "Claim not in GBHackers; supported by The Register (also cited). Re-point the citation."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CISA CVE-2026-10577 sourcing_note"
  url_or_quote: "'no v4.0 vector was published'"
  summary: "Advisory page publishes a v4.0 vector (base 10.0); correct/delete the clause. Low materiality."
```
