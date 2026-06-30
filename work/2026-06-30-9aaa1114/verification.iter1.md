**Model:** Anthropic Claude (specific model not determined — env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset; runtime is Opus 4.8 (1M context), `claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-30T04:37:55Z · ended_at=2026-06-30T04:41:21Z · duration_seconds=206
**Self-telemetry:** urls_checked=16 · webfetch_calls=14 · bridge_fetches=4 · websearch_calls=0

## Verification report — briefs/2026-06-30.md (iteration 1)

Cold read end-to-end. Fetched every CVE-typed Source, the Immediate Action callout sources, all TL;DR links, every UPDATE blockquote source, the Deep Dive citation, and all §1/§3 research primaries. Mechanical gate already passed (44/5/1, the 1 being the verification-counter placeholder). Below: truth + editorial findings only.

Verified clean (fetched, claim matches source): CVE-2026-48558 SimpleHelp (Horizon3.ai ~14,000 / ~7.2% ≈1,000 — supported; BleepingComputer Djinn/TaskWeaver — supported; CCB Belgium advisory exists; note Horizon3 page itself does not carry CWE-347, Djinn, TaskWeaver, or the v5.5.16/v6.0 RC2 patch strings — those are correctly attributed to BleepingComputer / the simple-help.com advisory, acceptable). CVE-2026-8037 LoadMaster (watchTowr + ZDI-26-342 both confirm CVSS 9.8, escape_quotes/malloc/calloc, /accessv2, root, v7.2.63.2, CVE-2026-33691 second CVE — fully supported). CVE-2026-55200 libssh2 (THN + VulnCheck — supported). DirtyClone mechanics (JFrog — supported except the "variant 4" label, see F4). Rewards-for-Justice $10M / UNC5792-FSB / UNC4221-military — supported; Backup-Recovery-Key tactic correctly attributed to SecurityWeek (quoted), not to the RfJ page. Mustang Panda ZOHOMURK (THN — supported). StegoAd (Microsoft Edge + THN — the China/DarkSpectre/GhostPoster overlap is correctly attributed to THN, which carries it; the Microsoft primary alone does not). Perplexity extension (Microsoft blog — supported). DFIR deep dive incl. the Swisscom B2B CSIRT parallel-intrusion claim — explicitly supported by the DFIR Report (quoted: "...in partnership with Swisscom B2B CSIRT, which observed another intrusion tied to the same campaign"). CVE-2026-48558 KEV re-surface — genuinely fresh (KEV listing 2026-06-29 + active exploitation + Djinn follow-on), not stale re-reporting.

### Citation does not support the claim

- **F3 — SzafirHost CWE mismatch (§1).** Brief: "a classic Java parser-confusion (CWE-345, Insufficient Verification of Data Authenticity)". The cited CERT Polska page explicitly assigns **CWE-434 (Unrestricted Upload of File with Dangerous Type)** — fetched this run, quoted verbatim from the page. CWE-345 appears nowhere on the source. Fix: CWE-434, or drop the CWE label.
- **F3 — Deep-dive MITRE/method drift (§5).** (a) Brief writes DLL side-loading **T1574.002**; the DFIR Report maps the consent.exe/msimg32.dll chain to **T1574.001** (DLL Search Order Hijacking). (b) Brief writes NTDS.dit "via a VSS shadow copy"; the report describes extraction via **wbadmin.exe**. Reconcile to the source. Minor — operational takeaway unchanged.

### Unsupported / hallucinated facts

- **F4 — n8n CVE-2026-54305 CVSS 9.9 is wrong (TL;DR, §2 table, §2 entry, §2 inclusion notes, §6).** Brief states **CVSS 9.9** and attributes it to NCSC-NL. The authoritative GitHub advisory GHSA-2j5h-858j-5mpf states **8.9 / High** (fetched and re-confirmed verbatim this run). The cited NCSC-NL advisory NCSC-2026-0212 carries **no per-CVE CVSS scores at all** — only qualitative `Kans: medium / Schade: high` (fetched via bridge, plain-text format). 9.9 is supported by neither cited source. This is the headline severity figure on the second TL;DR bullet and drives the §2 inclusion rationale. Fix: correct to 8.9 throughout; cite the GHSA (not NCSC-NL) for the score. CVE-2026-54307 = 8.5 is correct.
- **F4 — SzafirHost "state-mandated across Polish government services, courts, and banking" (§1, TL;DR).** This claim is the entire EU-relevance justification for the item, but it is not stated on the cited CERT Polska page (fetched this run — no mandate discussion; vendor is Krajowa Izba Rozliczeniowa / KIR). Either source the mandate to a fetched page or soften to what CERT-PL actually carries.
- **F4 — "DirtyFrag-family variant 4" (§4 DirtyClone UPDATE).** The cited JFrog page does not use this ordinal label; it places DirtyClone in the DirtyFrag family alongside Fragnesia and the original variants but assigns no "variant 4". Drop the invented ordinal.

### Editorial / less-is-more flags (advisory)

- **F11 — Fox Rothschild quantifier / case number rest on an unverifiable primary (§1).** "48 firms ... up from 38 in April", the "2026-05-21 single attorney" detail, and case "2:26-cv-03931, EDPA" are not in the cited Bloomberg Law article (fetched this run — it confirms only the suit, SRG/Luna Moth, EDPA, and the May 21 2026 breach date). They are attributed to DataBreaches.net, a known persistent 403 (noted in §7) that the verifier cannot fetch. A source IS cited so this is not a hard truth defect, but the specific figures cannot be verifier-confirmed; main agent should confirm against DataBreaches.net or soften.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 0, advisory: 1)

Truth count = F3 (CWE-345→434) + F3 (deep-dive MITRE drift) + F4 (n8n 9.9→8.9) + F4 (SzafirHost mandate) + F4 (DirtyFrag variant 4) = note these are 5 numbered records but two share code F3 and two share F4; counted as 4 distinct truth defects above with the deep-dive MITRE drift folded as the minor 4th. The n8n CVSS and the SzafirHost mandate are the two that materially mislead a reader and should block CLEAN. Advisory: F11.

### Findings summary (machine-readable)

See sibling file work/2026-06-30-9aaa1114/verification.iter1.findings.yaml (identical payload).
