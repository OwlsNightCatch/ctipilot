# FU1 — scoped follow-up research: two verified-but-unpublished backlog items (state/coverage_backlog.md, rows surfaced 2026-09-27)

Both rows are exempt from the recency gate (each was verified in-window by the 2026-09-27 audit); they are being published now, so each needs the deep read of its primary.

## Item A — IBM MQ and Langflow, bundled by NCSC-NL on 2026-09-23
- IBM MQ CVE-2026-10747 (CVSS 10.0, pre-auth heap overflow) — IBM's own security bulletin is the primary.
- Langflow OSS CVE-2026-79724, CVE-2026-81204, CVE-2026-85025 (three unauthenticated RCEs, CVSS 9.8) — Langflow's GitHub security advisories / release notes are the primary.
- Starting lead: the NCSC-NL advisory of 2026-09-23 that bundled them (advisories.ncsc.nl feed; `ncsc-nl csaf` recipe).
For each CVE: per-CVE authority for id + CVSS vector (vendor bulletin / CNA record, not the NCSC-NL roundup); affected versions and first fixed versions per branch from the vendor's structured table; authentication/exposure prerequisites; whether the vulnerable listener or API is internet-facing by default; public PoC or exploitation status AS OF today (check the CISA KEV catalog fresh and look for any exploitation report); which Langflow CVE maps to which flaw (explicit mapping only, never positional); the vendor's mitigation. Also note which existing store entries these relate to (Langflow entries exist under entries/2026-07-*/ and entries/2026-05-22/; list their ids).

## Item B — Adobe September 2026 security-bulletin cycle
- APSB26-142 Adobe Campaign Classic (eight CVSS 10.0 unauthenticated, nine further criticals).
- APSB26-150 Adobe Connect (up to 9.9).
- Adobe Experience Manager Forms on JEE (up to 9.8) — find its APSB number.
Read each bulletin's own structured table (affected versions, fixed versions, CVE id, severity, CVSS, vector, authentication requirement). For each CVE that is unauthenticated, network-reachable and CVSS >= 9.0, list id, CVSS, weakness type, affected and fixed builds. State whether Adobe reports exploitation (bulletin text "Adobe is not aware of any exploits in the wild" or the contrary) and check the CISA KEV catalog fresh. The store already carries earlier Adobe Campaign Classic entries (entries/2026-08-02/adobe-campaign-classic-apsb26-114-*, entries/2026-08-07/adobe-campaign-classic-apsb26-120-*, entries/2026-08-28/adobe-august-2026-coldfusion-campaign-classic-cvss10*): say what is new relative to them.

Return: findings YAML at work/2026-10-02T0404Z-intel/findings.FU1.yaml in the standard findings format (items, evidence quotes verbatim from the fetched pages, discovery traces, source_ledger), then the compact return with **Model:** and **Timestamps:** lines, and write work/2026-10-02T0404Z-intel/FU1.ended_at last.
