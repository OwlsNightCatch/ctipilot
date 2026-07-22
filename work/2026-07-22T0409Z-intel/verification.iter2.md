**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-22T05:04:57Z · ended_at=2026-07-22T05:12:36Z · duration_seconds=459

## Verification report — 2026-07-22T0409Z-intel (iteration 2)

Scope: 7 new entries + run record `runs/2026-07-22/2026-07-22T0409Z-intel.md`. Even iteration — walked the three prior-iteration (1) deltas first, then read the full set cold.

### Prior-iteration deltas verified

1. **F4 (cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback)** — RESOLVED. Fetched https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/ directly. Kaspersky's own text: "we retain our low-confidence assessment that Project CAV3RN is associated with OilRig" / "we identified no direct code reuse or infrastructure overlap." The entry's title, headline, summary, body, and `sourcing_note` now use exactly this low-confidence framing; the registry `actor:oilrig → tool:cavern-c2-framework` relation is `related-to` (not `uses`), carries the correct hedge note, and no `overlaps-with` edge remains anywhere in the registry for this cluster. Matches source verbatim.
2. **F5 (everest-ransomware-stadler-rail-supplier-platform-breach)** — RESOLVED. Fetched https://www.halcyon.ai/threat-group/everest and confirmed every background fact now cited inline: December 2020 emergence, BlackByte code-level connection, IAB services since November 2021, insider recruitment since October 2023 (cash/profit-sharing), RDP-without-MFA/VPN/IAB-credential vectors, and the group's October 2025 leak-site claims (airports, electricity grid, telecom) — all present in the Halcyon profile and now attributed to it inline, hedged as the group's own unverified claims. (Note: the Halcyon page itself contains an internal date wobble between "September 2025" and "in October" for the airport claim specifically — a source-side inconsistency, not an entry defect, since the entry's "October 2025" wording is textually present in the source.)
3. **F5 (langflow-cve-2026-0770-exploited-ncsc-nl-15-cve-batch)** — RESOLVED. Confirmed no PoC/GitHub sentence remains in the body, and `poc-public` is absent from both `tags` and `cves[0].status`. Active-exploitation status rests solely on the CISA KEV listing, which is cited.

### Fresh cold-read findings

None. Full source-by-source walk performed this iteration (not a sample):

- CISA KEV alert page — confirms CVE-2026-0770 + CVE-2021-27137 listing, title text matches entry's evidence quote verbatim.
- ZDI-26-036 — CVSS 9.8, exec_globals/root-execution quote verbatim, Jan 2026-01-09 disclosure after ~6 months unanswered vendor contact confirmed (2025-07-18 → 2026-01-09).
- NCSC-2026-0251 CSAF JSON (15 CVEs) — cross-checked CVE-2026-9202, CVE-2026-8859, CVE-2026-9135 individually against both the CSAF per-CVE notes and IBM's own per-CVE security-bulletin pages (nodes 7278920/7278924/7278929): CVSS (9.8/9.9/9.9) and affected-version range (1.0.0–1.10.0 in all three IBM "Affected Products and Versions" tables) match the entry's frontmatter exactly. The free-text CVE-2026-9135 IBM description mentions a specific "up to 1.9.2" discovery commit, but IBM's own structured affected-range table for that same CVE states 1.0.0–1.10.0 — same as the entry — so this is not a discrepancy.
- Zimbra's own 10.1.20 blog post — confirms SNMP command-injection framing, "permanent fix ... disclosed ... 26th June 2026," "industry best practices" language, mail-forwarding-bypass/EWS/mailbox-delegation/XSS/SSRF issue list, release date 2026-07-20 — all verbatim matches to entry claims and evidence quotes.
- swissinfo.ch Stadler Rail article — every quoted German sentence (ransom amount/non-payment, IT/production unaffected, no security-relevant/personal data stolen, criminal complaint filed, unnamed-supplier data-exchange platform) matches the entry's evidence and body text exactly.
- BleepingComputer SharePoint CVE-2026-50522 article (fetched via bridge after WebFetch 403) — watchTowr Attacker Eye honeypot quote, BinaryFormatter/SecurityContextToken/`_trust/default.aspx` chain, Janggggg PoC (2026-07-20), and the "execute code over a network without authentication" line all match verbatim.
- Kaspersky Securelist XEntry Team article — RDP/8TB storage, xp_cmdshell MSSQL abuse, RMM tooling (ManageEngine/Mesh Agent/Tactical RMM), GPO BitLocker push, ~$3,000 ransom, printer ransom notes, ShrinkLocker lineage reference, Colombia (June)/Mexico (May) cases — all confirmed verbatim.
- Korea Herald KNDA article — zero-day framing, April/May 2025 intrusion window, February 2026 discovery via another agency's tip, ~10,000 records/data types, explicit non-attribution ("not ruling out ... hacking organizations backed by foreign states") all confirmed verbatim.

Other checks performed, no issues found:
- ATT&CK ids across all 7 entries (T1190, T1059.006, T1136, T1552.001, T1114.003, T1199, T1133, T1505.001, T1505.003, T1219, T1484.001, T1486, T1102.002, T1071.004, T1008, T1573, T1552.004, T1606, T1059) all resolve to active, non-deprecated, non-revoked ids in the pinned `attack/enterprise-attack.json`.
- Classification blocks present on all 7 entries; reliability letters cross-checked against `sources/sources.json` (kaspersky-securelist=B, bleepingcomputer=B, checkpoint-research=B, securityaffairs=C) — entry ratings consistent; single-source XEntry entry correctly carries `verification: single-source` + `sourcing_note` naming the basis (F12 satisfied).
- `org_triage: null` on all 7 entries (no scheme configured — correct); no `watchlist` tags or `watchlist_hit: true` anywhere (none configured — correct).
- Priority calibration (F16): high/notable assignments all defensible against the stop-and-act-now vs. TL;DR bar; no under- or over-alerting found.
- Action-item discipline (F18): every non-empty `actions[]` entry (Langflow, Zimbra) is a concrete do-now task derived from the finding's own mechanics; SharePoint/Everest/XEntry/Cavern/KNDA correctly carry empty `actions[]` (SharePoint explicitly because the patch/key-rotation tasks are already carried by the in-window 2026-07-15/07-17 SharePoint entries — correct dedup discipline).
- Registry (`entities/registry.yaml`): all 5 new/updated entity records (`actor:everest-ransomware`, `incident:stadler-rail-everest-supplier-breach-2026`, `actor:xentry-team`, `actor:oilrig`, `incident:south-korea-knda-diplomatic-academy-zero-day-breach-2026`) have typed, sourced `relations[]` where applicable; no untyped/legacy relation fields.
- Dedup/update_of: both `update_of` targets (`2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup`, `2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern`) exist on disk and the delta content is genuinely new (machine-key exploitation escalation; DNS AAAA fallback + revised attribution confidence).
- No IOCs (hashes/IPs/domains/rule code) in any entry body. English throughout. No workflow-internal language leaked.
- Coverage/missed-angles: run record's borderline-drops (DD-WRT KEV dedup, SentinelLabs Iran assessment, Estée Lauder/Cl0p, Anubis/Coca-Cola) and recency drops (Expel CylindricalCanine, Symantec Spirals) are reasoned and logged; no additional plausible in-window gap identified given the source-coverage telemetry (cert-eu/cert-pl/cert-at/ncsc-uk/enisa low-cadence, chrome-releases jina-credit-exhaustion documented as a coverage gap with no material loss claimed).

### Verdict

CLEAN

### Findings summary (machine-readable)

```yaml
[]
```
