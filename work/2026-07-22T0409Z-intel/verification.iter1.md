**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-22T04:48:46Z · ended_at=2026-07-22T04:59:15Z · duration_seconds=629
**Self-telemetry:** urls_checked=13 · webfetch_calls=8 · bridge_fetches=6

## Verification report — 2026-07-22T0409Z-intel (iteration 1)

Cold read, odd iteration (no prior-iteration deltas). 7 new entries + run record. Every entry's primary source fetched and cross-checked; evidence quotes verified verbatim against fetched pages; CVE ids/CVSS verified against per-CVE authorities (NCSC CSAF, ZDI, BSI CSAF); update targets + entity keys verified against prior_coverage.json and registry.yaml.

### Unsupported / hallucinated facts

**F4 — Cavern entry overstates a low-confidence attribution as explicit.** The Kaspersky source (https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/, Attribution section) states: "we retain our **low-confidence assessment** that Project CAV3RN is associated with OilRig ... However, we identified **no direct code reuse or infrastructure overlap**," and "In our previous report, we attributed Project CAV3RN to OilRig (APT34) **with low confidence**." The entry presents this as a firm/new attribution:
- headline: "A second vendor **ties** the Outlook-calendar Graph C2 framework **to OilRig**"
- summary + body: "**attributing it to OilRig (APT34)**"
- body: "providing the **explicit attribution** that earlier coverage of this cluster lacked"

For a threat-intel audience the confidence level is load-bearing. Reword to a low-confidence association (drop "explicit"; "associates with" not "attributes to"). credibility:2 / confidence:medium are already fine; the prose is the defect. Evidence quotes on this entry both check out verbatim (intro line 14 for the DNS-AAAA quote; Attribution line 341 for the behavioural-patterns quote).

### Claims missing inline citation

**F5 — Everest entry: actor-background paragraph unsourced.** Body para 2 asserts Everest's founding ("active since December 2020"), business model ("initial-access-broker service and a paid corporate-insider recruitment programme"), initial-access vectors ("internet-exposed RDP without MFA and vulnerable VPN endpoints"), and prior victim claims ("Heathrow, Brussels and Berlin airports (September 2025) and a European electricity grid and telecom networks (October 2025)") with only "Per third-party actor tracking" — no link. The two cited sources (swissinfo.ch, itmagazine.ch) cover only the Stadler incident. findings.S4.yaml sourced this to AttackIQ/Halcyon/SOCRadar profiles; add one as a corroborating record and cite. The airport/grid claims are already correctly hedged as unconfirmed — the gap is the citation, not the caution.

**F5 — Langflow entry: "public PoC on GitHub" uncited.** Body para 1: "A public proof-of-concept is available on GitHub." None of the three cited sources (CISA KEV alert, ZDI-26-036, NCSC-2026-0251 — all fetched) mention a public GitHub PoC for CVE-2026-0770; frontmatter carries status: poc-public. Research (findings.S1.yaml) found a real repo (role corroborating) not present in sources[]. Add a source basis (ENISA EUVD EUVD-2026-4466 or a sourcing_note) or soften.

### Items verified clean (no finding)

- **URLs**: all primaries resolve to specific advisory/article/PSIRT pages and support their claims — CISA KEV alert (bridge), ZDI-26-036, NCSC-2026-0251 + 0237 (jina; CSAF cross-checked), Zimbra 10.1.20 blog, NCSC-CH post 12782 (bridge), BSI CSAF WID-SEC-2026-2429, THN, BleepingComputer SharePoint, swissinfo Stadler, Korea Herald KNDA, Kaspersky XEntry + Cavern, Check Point (confirmed as a real article via Kaspersky's own outbound link). No 404s/homepages/generic indexes.
- **CVE/CVSS truth**: Langflow batch CVSS verified against NCSC CSAF (9202=9.8, 8859=9.9, 9135=9.9; 15 CVEs = 15); Langflow 0770 9.8 via ZDI; Zimbra CVE-2026-50055/10631/50054 all present in BSI CSAF (RESERVED on NVD, entry states this). SharePoint 50522 CVSS 9.8 consistent with pre-auth deserialization RCE and prior 07-15 coverage (MSRC page JS-only; not independently re-scored this pass — flagged as non-blocking).
- **Evidence-quote verbatim/contiguity**: Langflow (ZDI + CISA), Zimbra (SNMP + mail-forwarding, matched to Zimbra blog), Stadler (both German quotes matched to swissinfo), SharePoint (Dutch NCSC quote + BleepingComputer honeypot/no-auth quotes matched), XEntry (all three Kaspersky quotes matched), Cavern (both matched), KNDA (both Korea Herald quotes matched). All verbatim.
- **Update decisions**: SharePoint 50522 → 2026-07-15 July-cluster (target exists, lists 50522; delta = escalation to active exploitation; actions[] correctly empty to avoid duplicating in-window 07-15/07-17 SharePoint actions). Cavern → 2026-07-21 HOLLOWGRAPH (target exists; delta = OilRig low-conf attribution + DNS AAAA fallback). Both correct.
- **Entity linking**: all keys exist in registry (everest-ransomware, xentry-team, oilrig, cavern-manticore, cavern-c2-framework, hollowgraph-malware, both incidents); oilrig relations correctly typed (uses cavern-c2-framework; overlaps-with cavern-manticore — conservative, not attributed-to).
- **Priority calibration**: high (Langflow, SharePoint) and notable (rest) all defensible; no false critical, no under-alerting.
- **Technique mapping**: every techniques[] id maps to a body behaviour and source; no empty attacker-kind mappings; no bare-ID dumps in prose.
- **Classification (F17)**: every entry rated; A/B reliability and 1/2 credibility all consistent with source nature and corroboration shown. No defect.
- **Action-item discipline (F18)**: Langflow + Zimbra actions concrete and entry-specific; empty actions[] on the five incident/threat/update entries all correct. No padding, no body-restatement.
- **Coverage completeness**: WordPress CVE-2026-63030/-60137 KEV additions correctly deduped (WP2Shell covered 4× in prior window incl. public PoC + KEV trajectory); DD-WRT KEV-only deduped; out-of-nexus drops (Estée Lauder, Anubis/Coca-Cola, SentinelLABS Iran) justified; recency drops logged. No missed in-window relevant story identified. Coverage looks complete.
- **Style**: no IOCs (Cavern uses "attacker-controlled nameservers"/"newly-registered domains", no domain/IP), no vanity metrics, no workflow-internal language, English throughout (source-language quotes legitimate).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 2, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback
  item: "Kaspersky corroborates the Cavern/HOLLOWGRAPH cluster, attributes it to OilRig (APT34)..."
  url_or_quote: "'providing the explicit attribution that earlier coverage of this cluster lacked' / headline 'ties ... to OilRig'"
  summary: "Source states low-confidence assessment associating CAV3RN with OilRig, no direct code reuse/infra overlap, and already attributed it in a prior report; entry presents as explicit/new attribution. Reword to low-confidence association."
- code: F5
  category: missing-citation
  section: everest-ransomware-stadler-rail-supplier-platform-breach
  item: "Everest ransomware breaches a Stadler Rail supplier data-exchange platform..."
  url_or_quote: "'Per third-party actor tracking the group has previously claimed compromises of aviation systems at Heathrow, Brussels and Berlin airports...'"
  summary: "Actor-background paragraph uncited; cited sources are Stadler-only. Add AttackIQ/Halcyon/SOCRadar profile (per findings.S4.yaml) as corroborating and cite."
- code: F5
  category: missing-citation
  section: langflow-cve-2026-0770-exploited-ncsc-nl-15-cve-batch
  item: "CVE-2026-0770 — Langflow: CISA confirms active exploitation..."
  url_or_quote: "'A public proof-of-concept is available on GitHub.'"
  summary: "No cited source supports the GitHub-PoC claim; research found a repo not in sources[]. Add source basis (EUVD-2026-4466 / sourcing_note) or soften."
```
