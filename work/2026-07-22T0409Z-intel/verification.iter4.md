**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-22T05:25:21Z · ended_at=2026-07-22T05:31:03Z · duration_seconds=342

## Verification report — 2026-07-22T0409Z-intel (iteration 4)

### Prior-iteration (3) delta verification

1. F14 (south-korea-knda-elearning-zero-day-breach, unsupported "2,500/350" diplomat breakdown) — CONFIRMED RESOLVED. The body now reads only "Up to ~10,000 records of current and former diplomats and mission staff were exposed" / "up to ~10,000 records of current and former diplomats, overseas-mission officials and embassy/consulate administrative staff." Re-fetched The Korea Herald (koreaherald.com/article/10815199): "The compromised system contained about 10,000 personnel records... The figure is that of personnel records stored on the server, not the confirmed number of people whose information was taken." No 2,500/350 breakdown reintroduced. Resolved.
2. F10 (whole-run, WordPress Core CVE-2026-63030 / CVE-2026-60137 in the same CISA KEV batch) — CONFIRMED CORRECT DEDUP. Re-fetched the CISA KEV alert (cisa.gov/news-events/alerts/2026/07/21/cisa-adds-four-known-exploited-vulnerabilities-catalog via bridge/jina): confirms exactly four CVEs added — CVE-2021-27137 (DD-WRT), CVE-2026-0770 (Langflow), CVE-2026-63030 (WordPress Core), CVE-2026-60137 (WordPress Core). Cross-checked work/2026-07-22T0409Z-intel/prior_coverage.json: both WordPress CVEs are recorded under 2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030 and updated 2026-07-21/gpt56-autonomous-wordpress-wp2shell-exploit-chain. The run record's "Borderline drops" section documents this dedup decision. No blind spot — resolved correctly.

### Fresh cold-read findings

### Analytical-link-as-fact

- **F13** — `2026-07-22/xentry-team-bitlocker-lotl-extortion-rmm-gpo`. The entry states: *"Kaspersky's GERT team documented two 2026 extortion cases by a crew it tracks as 'XEntry Team'"* and *"In the analysed cases initial access was an internet-exposed RDP service and a misconfigured Microsoft SQL Server whose xp_cmdshell extended stored procedure allowed OS command execution."* I fetched the cited Securelist source (https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/) in full. It covers two distinct incidents: "First case: abusing RDP to encrypt data" (Colombia, June — RDP exposure, $3,000 demand, no actor name given) and "Second case: meet the XEntry Team" (Mexico, May — MSSQL xp_cmdshell, RMM, GPO; victim machines displayed "Hacked by XEntry Team"). The name "XEntry Team" originates ONLY from the second case. Kaspersky's own Conclusions section explicitly hedges the link between the two cases: *"Although the ransom notes do not reveal a clear connection between the actors, certain words used in the messages, as well as the method of delivery and communication, may confirm a link"* — i.e., an unconfirmed stylistic-similarity hypothesis, not an established single-actor attribution. The entry (and the registry's `actor:xentry-team` record, which I also read) presents both cases as the unified work of one named crew, combining both initial-access vectors into a single actor playbook — an analytical link the source itself does not make as fact.

### Unsupported / hallucinated facts

- **F4** — `runs/2026-07-22/2026-07-22T0409Z-intel.md`, `### Published` section, the Project CAV3RN / Cavern bullet. Text reads: *"Kaspersky independently corroborates the Cavern/HOLLOWGRAPH cluster, attributes it to OilRig (APT34), and adds a DNS AAAA-record C2 config-recovery fallback... Registered `actor:oilrig` and typed relations (oilrig `uses` cavern; oilrig `overlaps-with` cavern-manticore)."* This contradicts both the entry itself and the current registry state. I re-fetched the Securelist Cavern article and confirmed the entry's own body correctly reflects it: *"we retain our low-confidence assessment that Project CAV3RN is associated with OilRig... we identified no direct code reuse or infrastructure overlap"* — i.e. a low-confidence association, not an "attribution." I also `Read` `entities/registry.yaml`: `actor:oilrig`'s only relation is `{to: tool:cavern-c2-framework, type: related-to, ...}` with a low-confidence note — there is no `overlaps-with` edge to `actor:cavern-manticore` at all (iteration 1's remediation record states this edge was dropped). The run record's own narrative was never updated after iteration 1's remediation changed the entry and registry, so the published run-record notes now misstate both the confidence level and the actual typed relations shipped.

### Verdict

`NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)`

Both findings are truth-class (F13, F4) and both are backed by a source I fetched in this iteration and a file I `Read` in this iteration (entities/registry.yaml). Recommended remediation: (1) reword the XEntry Team entry/registry summary to reflect Kaspersky's own hedge — treat the two cases as related-but-unconfirmed (e.g. only the Mexico/MSSQL case is confirmed as "XEntry Team"; the Colombia/RDP case is a similar-pattern candidate, not a confirmed same-actor case), or restrict the `actor:xentry-team` registry record and entry framing to the case that actually carries the name, describing the RDP case as an analogous prior incident Kaspersky notes only a stylistic-similarity hypothesis for; (2) correct the run record's Published-section CAV3RN bullet to match the entry's own low-confidence-association language and the registry's actual `related-to` relation (no `overlaps-with` edge).

### Findings summary (machine-readable)

```yaml
- code: F13
  category: analytical-link-as-fact
  section: threats
  item: "2026-07-22/xentry-team-bitlocker-lotl-extortion-rmm-gpo"
  url_or_quote: "Kaspersky's GERT team documented two 2026 extortion cases by a crew it tracks as \"XEntry Team\""
  summary: "Kaspersky's Securelist article covers two separate cases and explicitly hedges the link between them ('do not reveal a clear connection between the actors ... may confirm a link'); the name 'XEntry Team' comes only from the second (Mexico/MSSQL) case. Entry and registry present both cases (including the first, RDP-based, unnamed case) as one confirmed crew's playbook."
- code: F4
  category: hallucinated-fact
  section: run-record-notes
  item: "runs/2026-07-22/2026-07-22T0409Z-intel.md — ### Published bullet for Project CAV3RN / Cavern"
  url_or_quote: "attributes it to OilRig (APT34) ... Registered actor:oilrig and typed relations (oilrig uses cavern; oilrig overlaps-with cavern-manticore)."
  summary: "Stale text left over from before iteration 1's remediation. Contradicts the entry's own (correct) low-confidence-association language and the registry's actual related-to-only relation (no overlaps-with edge exists)."
```
