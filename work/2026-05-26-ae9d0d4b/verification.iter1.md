**Model:** Anthropic Claude (specific model not determined — `CLAUDE_FRIENDLY_NAME`/`CLAUDE_MODEL_ID` unset; runtime is Opus-class per agent rotation, spawn ran cti-verification)
**Timestamps:** started_at=2026-05-26T04:45:02Z · ended_at=2026-05-26T04:48:30Z · duration_seconds=208
**Self-telemetry:** urls_checked=10 · webfetch_calls=10 · websearch_calls=2 · bridge_fetches=0

## Verification report — briefs/2026-05-26.md (iteration 1)

Cold read, full end-to-end. Every cited Source URL was fetched (WebFetch) in this iteration. Two hosts (ENISA EUVD, Fox-IT blog) returned a local "certificate is not yet valid" TLS clock-skew error from the WebFetch sandbox — NOT a brief defect; both were independently confirmed live and claim-supporting via WebSearch and via the corroborating The Hacker News article. The mechanical gate's URL-liveness ledger already passed on both.

IOC discipline: clean. No IPs, no SHA/MD5 hashes, no defanged domains. The RemotePE C2 domain and the ACR-Stealer C2 (`yw.enhanceblabber[.]cc`) and the TrapDoor GitHub account (`ddjidd564`) that appear in the sources did NOT leak into the brief. `Iassvc.dll` is a malware-masquerade filename surfaced as a detection tell (behavioural), not an IOC — mechanical IOC gate passed.

Dedup: verified against prior_coverage.json (93 records). RemotePE / Lazarus / TrapDoor / Szafir / KnowledgeDeliver / nginx / @antv = 0 prior hits → genuinely new. TeamPCP/Shai-Hulud (12/14 prior hits) correctly framed as a consolidated UPDATE with new deltas (framework open-sourced 05-22, durabletask wiper, @antv 639/323, forged Sigstore badges). Packagist (1 prior hit) correctly dropped as dup. Charter/ShinyHunters correctly held (no delta). § 7 drops all correctly reasoned.

Anti-inversion check (§ 4 TeamPCP, high priority): PASS. SANS ISC diary 33016 confirms Datadog Security Labs *analysed* (static analysis of) the open-sourced *attacker* framework — the brief correctly describes it as an attacker toolkit that was open-sourced, NOT a defender tool. "framework open-sourced on GitHub", "forged Sigstore badges" (42 packages), and "durabletask Linux disk wiper" are each supported by the diary. No name-collision inversion (F15) found; the `name-collision` WARN on "GitHub"/"WebAuthn" is a benign common-noun false positive.

CVE checks: CVE-2026-9058 (Szafir SDK, CWE-393/637, fixed v463) and CVE-2026-5426 (KnowledgeDeliver, pre-shared machineKey ViewState RCE, zero-day pre-2026-02-24, BLUEBEAM/Godzilla in w3wp.exe, EID 1316) both confirmed real and accurately described against their primaries. CVE-2026-9256 (nginx-poolslip) and the WolfSSL flaw appear only in § 7 framed as dropped/uncorroborated — confirmed they are NOT asserted as fact.

### Citation does not support the claim

- **F3a — § 2 / § 0, CVE-2026-9058 affected-systems attribution.** Brief (§ 2) states: "**CERT Polska names ZUS (Zakład Ubezpieczeń Społecznych...) and the e-Gate system at Centrum e-Zdrowia ... among affected deployments**"; § 0 TL;DR repeats "Named affected systems include ZUS (social security) and Centrum e-Zdrowia's e-Health gateway." I fetched the cited CERT Polska page (https://cert.pl/en/posts/2026/05/CVE-2026-9058/) — it names only Szafir SDK, KIR (Krajowa Izba Rozliczeniowa), the CVE, CWE-393/637, version 463, the "nondetermined" trust status / result code 0, and credits researcher Michał Leszczyński (icedev.pl). It does **not** name ZUS, Centrum e-Zdrowia, or e-Gate anywhere in its text. The ZUS / e-Gate / Centrum e-Zdrowia naming originates from the researcher's separate write-up (zaufanatrzeciastrona.pl, "Ominięcie uwierzytelniania w ZUS-ie i systemach e-Zdrowia… CVE-2026-9058"), which I confirmed via WebSearch. The underlying fact is TRUE and corroborated — but it is mis-attributed to CERT Polska, which did not state it. Remediation: re-attribute the affected-systems detail to the researcher's write-up (add it as an Additional source) or soften the attribution to "the disclosing researcher names ZUS and Centrum e-Zdrowia's e-Gate". Truth-class.

- **F3b — § 4, The Hacker News citation date.** Brief cites the @antv wave to "**[The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)**" (inline at line 73 and in the § 4 footer at line 77). I fetched the article: the URL resolves and supports every @antv claim (639 versions / 323 packages, echarts-for-react ~1.1M, size-sensor), but its actual publication date is **May 19, 2026**, not 2026-05-23. The cited date is wrong by 4 days in two places. (The 42-forged-Sigstore-badges claim is NOT in this THN article but IS supported by the primary SANS ISC diary 33016, so that claim itself is fine.) Remediation: correct both citation dates to 2026-05-19. Truth-class (date accuracy).

### Quantifier without source

- **F14 — § 0 / § 3, GTIG PhaaS platform count.** Brief (§ 3) states GTIG "published a teardown of **at least 13** Chinese-language phishing-as-a-service (PhaaS) platforms"; § 0 TL;DR repeats the framing ("at least 13 Chinese-language phishing services" — also the source of the mechanical `quantifier-evidence` WARN). I fetched the GTIG source twice (https://cloud.google.com/blog/topics/threat-intelligence/chinese-language-phishing-services/). The verbatim wording is: "Google Threat Intelligence Group (GTIG) analyzed **a dozen** current PhaaS offerings in the Chinese underground." The page does NOT contain "13" or "at least 13" anywhere and does not enumerate a count beyond "a dozen" (≈12). The brief inflated/over-specified an approximate "a dozen" into a harder, larger "at least 13". Remediation: change to "a dozen" / "around a dozen" / "roughly twelve" to match the source, or quote the source phrase verbatim. Truth-class.

### Editorial / less-is-more flags (advisory)

- **F11 — § 3 CVSS-9.3 attribution depth (minor).** The brief attributes "CVSS 4.0 9.3" with full vector to "CERT Polska / ENISA EUVD". The CERT Polska page I fetched does NOT carry a CVSS score (it links to cve.org). I could not fetch the ENISA EUVD page (local TLS clock skew), so I cannot confirm the 9.3/vector is on the EUVD page — but EUVD is the more plausible carrier and the URL-liveness ledger passed. No action required unless the main agent can cheaply confirm; flagged only so the residual is visible. Not counted as a defect.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 0)

Three truth-class findings, all defensible with quoted source text fetched this iteration: F3a (ZUS/Centrum e-Zdrowia mis-attributed to CERT Polska — fact true but wrong source), F3b (THN citation date 2026-05-23 should be 2026-05-19), F14 ("at least 13" PhaaS vs source's "a dozen"). All are low-effort corrections. Everything else — URLs, dedup, anti-inversion, IOC discipline, CVE accuracy, coverage shape, single-source flags (§ 1 ACR Stealer, § 3 GTIG both correctly flagged `[SINGLE-SOURCE]`), § 7 drop reasoning — is clean.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-9058 — Szafir SDK (KIR)"
  url_or_quote: "CERT Polska names ZUS ... and the e-Gate system at Centrum e-Zdrowia among affected deployments"
  summary: "Cited CERT Polska page (cert.pl/en/posts/2026/05/CVE-2026-9058/) names only Szafir SDK/KIR/CVE/v463/researcher; does NOT name ZUS, Centrum e-Zdrowia or e-Gate. Fact is true but sourced from the researcher's zaufanatrzeciastrona.pl write-up, not CERT Polska. Re-attribute or add researcher write-up as Additional source. Also affects the § 0 TL;DR bullet."
- code: F3
  category: claim-not-supported
  section: updates
  item: "UPDATE: TeamPCP / Mini Shai-Hulud"
  url_or_quote: "[The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/mini-shai-hulud-pushes-malicious-antv.html)"
  summary: "Cited THN article resolves and supports the @antv claims, but its publication date is 2026-05-19, not 2026-05-23. Correct the date in the inline citation (line 73) and the § 4 footer (line 77)."
- code: F14
  category: quantifier-without-source
  section: research
  item: "GTIG Chinese-language PhaaS ecosystem [SINGLE-SOURCE]"
  url_or_quote: "a teardown of at least 13 Chinese-language phishing-as-a-service (PhaaS) platforms"
  summary: "GTIG source (cloud.google.com/blog/topics/threat-intelligence/chinese-language-phishing-services/) says verbatim 'analyzed a dozen current PhaaS offerings' (~12); never says '13' or 'at least 13'. Brief over-specified. Change to 'a dozen' / 'around a dozen'. Also affects the § 0 TL;DR bullet."
```
