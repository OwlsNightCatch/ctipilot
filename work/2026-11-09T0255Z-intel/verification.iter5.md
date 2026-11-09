**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** see work/2026-11-09T0255Z-intel/verify.iter5.started_at and verify.iter5.ended_at

## Verification report — 2026-11-09T0255Z-intel (iteration 5, confirmation pass)

Scope: new entry `2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale`, updated entry `2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole` (improvement record at 2026-11-09T03:25:45Z, `git diff HEAD` read in full: every changed line is covered by the record's `fields`; `updated_at` untouched), run record. All 45 ledger claims have a verdict row in `verification.iter5.claims.yaml` (45 ok). Every cited page was fetched in this iteration: GTIG, Wiz, Datadog, SANS ISC, Previdian (extract and raw HTML for the timeline dates), Alpine, heise, OpenSSH release notes, The Hacker News, NCSC ncsc-csh post 13155, CISA KEV via the bridge (catalogue 2026.11.06, CVE-2026-123158 absent). The OX Security post answers 403 on extract, url, jina and WebFetch; its full text was read from OX's own live RSS feed (https://www.ox.security/feed/, item of 2026-11-05 20:03 UTC) and matched against every OX-cited claim.

### Editorial / less-is-more flags (advisory)
- F11 #1 (low confidence): sshole summary, "Previdian's page, as read on 2026-11-09, reports 20 exploitation attempts from 13 addresses since 2026-11-06 and, according to The Hacker News, a successful root login on an Alpine honeypot": the honeypot login is not on Previdian's page (the page only carries sensor counters and states they "do not show that ... the attempt succeeded"); the 2026-11-07 section already says so. Optional: split the clause.
- F11 #2 (low confidence): sshole title, "NCSC Switzerland issued an advisory (CVSS 3.1 8.1)": the NCSC advisory carries no CVSS score, OX Security's does. Pre-existing text. Optional: move the score beside the CVE id.

### Checks with no finding
- Truth: every figure, name, date, version and attribution in both entries and the improvement section matches the fetched pages (ISC counts 232/713/246/51 and the 11-05 first-attempt statement; Previdian 20/13/9 countries, last 2026-11-08; Datadog 12 organizations in 30 days with failed ListFoundationModels in the majority; GTIG event names, LiteLLM /key/regenerate, UNC6993 tooling, default-off Data Access logs, "high severity" for non-IaC logging calls; Wiz billing-account chain). All 11 evidence quotes verbatim on their pages. Source dates equal the pages' own dates (Previdian 2026-11-05, ISC 2026-11-08, Wiz 2026-10-20, Datadog 2026-10-06, GTIG 2026-11-02). Fixed-package table and CVSS 8.1 match OX and Alpine.
- Dedup: no CVE on the LLMjacking entry; CVE-2026-40217 correctly left out (store carries it as the Obsidian LiteLLM guardrail flaw, run record carries the Contradiction line); `references[]` names the 2026-08-07 token-jacking entry; no other in-window LLMjacking entry. UNC6993 is a new registry key, `product:litellm` exists.
- Style: no IOCs, no em dash in reader-facing text outside the section headings, no workflow vocabulary, main analyses at 546 and 549 words. Classification B/2 (GTIG source record is B) and A/2 (NCSC-CH is A) consistent; `org_triage` null, no watchlist; actions: LLMjacking empty, sshole one concrete task.
- Changelog contract (4c): the improvement adds a second independent sensor set and refreshes a counter, decision and priority unchanged, so type `improvement` is defensible; the main analysis ("now that exploitation attempts are reported") does not contradict the newest section; no silent edit.
- Run record notes: KEV window (0 additions, catalogue newest addition 2026-11-06), Patch Tuesday 2026-11-10, `android-security-bulletin` promotion (entries from 3 distinct runs), CVE-2026-40217 contradiction all hold on disk. Borderline-drops read as sound; two web searches for in-window items found nothing the run missed (coverage looks complete for a quiet weekend window).

### Verdict
CLEAN (truth: 0, editorial: 0, advisory: 2)

### Findings summary (machine-readable)
See work/2026-11-09T0255Z-intel/verification.iter5.findings.yaml (two F11 advisories).
