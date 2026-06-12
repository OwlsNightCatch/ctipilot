**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-06-12T04:54:31Z · ended_at=2026-06-12T04:58:19Z · duration_seconds=228
**Self-telemetry:** webfetch_calls=14 · websearch_calls=0 · bridge_fetches=4 · urls_checked=18

## Verification report — briefs/2026-06-12.md (iteration 3)

Read cold from disk. WebFetched/bridged every truth-bearing URL: Mandiant GTIG, Oracle alert (bridge), NCSC-CH 12627 + 12622 (bridge), MariaDB Foundation, SecurityWeek GreatXML, The Register, Krebs, THN Gentlemen, CCB Belgium, NCSC-NL 0189 (resolved real URL), Imperva, Varonis, GitHub npm, CISA BOD 26-04 + Patch Smarter (bridge), ESET, BleepingComputer Maine + Nottingham, Secret Service (bridge), Europol, THN Oracle. MSRC SPA pages returned placeholder content (JS-rendered) — URLs resolve to the correct CVE pages (titles confirmed) but body text could not be content-verified; not flagged as broken.

Most of the brief verifies clean: Oracle/Mandiant §0 callout, MariaDB §5 core bug, GreatXML+Dormann, Nottingham UPDATE figures, AudiA6 takedown, OpenClaw research, npm v12, CISA BOD, ESET OceanLotus, Maine/VRChat verbatim quote — all fully supported by the cited sources. The findings below are the residual truth defects, concentrated in the FortiSandbox and The Gentlemen items.

### Citation does not support the claim

**F1 — FortiSandbox CVSS 9.1 is supported by NO cited source; the §7 "contradiction" is fabricated.** §2 states "CVE-2026-25089 ... (CVSS 9.1)" citing NCSC-NL, the CVE Summary Table row shows 9.1, and §7 states: "NCSC-NL records CVSS 9.1 (used in this brief); CCB Belgium's advisory states CVSS 9.8." I fetched both. CCB Belgium states **9.8** (`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`). NCSC-NL (resolved real URL https://advisories.ncsc.nl/2026/ncsc-2026-0189.html) also states **9.8 (v3)**. Neither cited source records 9.1. The 9.1 figure is unsupported, and the §7 contradiction note is false — both sources agree on 9.8. Fix: change FortiSandbox CVSS to 9.8 across §2 prose, CVE Summary Table, and the footer CVSS field; remove or rewrite the fabricated §7 "Contradiction — FortiSandbox CVSS" note.

**F2 — FortiSandbox PoC quote attributed to CCB is not verbatim in CCB (or NCSC-NL).** §2: CCB Belgium urges patching and warns that "a proof-of-concept exploit is publicly available, heightening exploitation risk" ([CCB Belgium]). CCB's actual text is: "The publicly availability of a proof-of-concept (PoC) exploit increases the likelihood..." — different wording. NCSC-NL 0189 contains no public-PoC sentence at all. The substance (a public PoC exists, per CCB) is supported, but the quoted string is fabricated. Fix: replace the quotation marks with a paraphrase, or quote CCB's actual wording.

**F3 — "Krebs ... lists Germany and the UK among the most-affected countries" is not in the Krebs article.** Appears in §0 TL;DR bullet ("Germany and the UK among the most-affected"), §1 body ("Krebs separately lists Germany and the UK among the most-affected countries ([KrebsOnSecurity, 2026-06-10])"), and §7 ("Krebs: Germany/UK"). I fetched the Krebs piece: it covers handles, the named Russian national, Intel 471/Constella/Flashpoint corroboration, 332 victims — but "Germany and the UK among most-affected countries" is ABSENT. The geography is supported by THN (Thailand/UK/Brazil/Germany/India), not Krebs. Fix: drop the Krebs attribution for the Germany/UK geography (re-attribute to THN, which does support it) in all three locations.

### Unsupported / hallucinated facts

**F4 — "478 claimed victims across 66 countries" — the "66 countries" figure is unsourced and the brief's own §7 says it was removed.** §1 H3 heading: "478 claimed victims across 66 countries". THN (the cited source for the 478 figure) does NOT contain "66 countries". §7 explicitly states: "an unsupported '66 countries / France / sector-list' claim from a sub-agent return was dropped in verification as unsourced." The heading retains the very claim §7 says was dropped — internal self-contradiction. Fix: remove "across 66 countries" from the §1 heading.

**F5 — "the administrator supplies affiliates with ... Fortinet SSL-VPN credentials" is uncited, absent from Krebs, and contradicted by Check Point.** §1: "...per an 11 June PRODAFT update — 'with high confidence'; PRODAFT adds that the administrator supplies affiliates with initial access, primarily Fortinet SSL-VPN credentials from brute-force or the group's own leak database". No PRODAFT URL is cited anywhere on the item (the sentence's only link is Krebs, 2026-06-10, which mentions Intel 471/Constella/Flashpoint but not PRODAFT high-confidence corroboration). Check Point Research (cited on the same item) directly contradicts the framing: it describes affiliates obtaining Fortinet VPN credentials independently as access brokers ("Mamba acting as an access broker for Fortinet VPNs sourced from ramp"), NOT the administrator distributing them. This is an analytical-link-as-fact / unsupported-attribution defect. Fix: either add an inline PRODAFT source URL that actually states this, or drop the "administrator supplies affiliates with credentials" claim and the unsourced PRODAFT high-confidence attribution.

**F6 — §5 "CVE-2026-48165 and CVE-2026-48163 (both CVSS 8.0)" — the 8.0 scores are in no cited source.** §5: "Two companion flaws disclosed in the same cycle, CVE-2026-48165 and CVE-2026-48163 (both CVSS 8.0), add similar parameter-injection surfaces in the wsrep State Snapshot Transfer (SST) handshake ([NCSC-CH CSH, 2026-06-11])." The cited NCSC-CH post 12627 mentions ONLY CVE-2026-49261 — it does not name the two companion CVEs, give CVSS 8.0, or mention the SST handshake. The MariaDB Foundation page (cited elsewhere in §5) names all three CVEs and references state snapshot transfer but gives NO CVSS scores for them. The "8.0" figure is unsupported by either source. Fix: drop "(both CVSS 8.0)" or attach a source that states it; correct the inline citation to MariaDB Foundation for the companion-CVE existence/SST detail (the only source that carries it).

### Verdict

NEEDS_FIXES (truth: 6, editorial: 0, advisory: 0)

All six are truth-class: F1/F2/F6 are claim-not-supported (CVSS and quote drift against fetched sources), F3 is claim-not-supported (false source attribution), F4 is a quantifier-without-source contradicted by the brief's own §7, F5 is analytical-link-as-fact (uncited + source-contradicted attribution). All concentrate in two items (FortiSandbox, The Gentlemen) plus the §5 companion-CVE aside; the rest of the brief verified clean.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-25089 — Fortinet FortiSandbox"
  url_or_quote: "(CVSS 9.1) ... NCSC-NL records CVSS 9.1 (used in this brief); CCB Belgium's advisory states CVSS 9.8"
  summary: "Both cited sources record 9.8 — NCSC-NL (https://advisories.ncsc.nl/2026/ncsc-2026-0189.html) says 9.8 v3, CCB says 9.8. The 9.1 figure is unsupported and the section-7 contradiction is fabricated. Set CVSS to 9.8 in prose/table/footer and remove the false contradiction note."
- code: F2
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-25089 — Fortinet FortiSandbox"
  url_or_quote: "\"a proof-of-concept exploit is publicly available, heightening exploitation risk\" ([CCB Belgium])"
  summary: "Not verbatim in CCB (CCB: 'The publicly availability of a proof-of-concept (PoC) exploit increases the likelihood...') nor NCSC-NL. Substance (public PoC) is fine; replace quotation with paraphrase or CCB's actual wording."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "The Gentlemen ransomware"
  url_or_quote: "Krebs separately lists Germany and the UK among the most-affected countries ([KrebsOnSecurity, 2026-06-10])"
  summary: "Krebs article does not mention Germany/UK as most-affected. Geography is supported by THN, not Krebs. Re-attribute to THN in TL;DR bullet, section 1 body, and section 7."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "The Gentlemen ransomware (H3 heading)"
  url_or_quote: "478 claimed victims across 66 countries"
  summary: "THN does not contain '66 countries'; section 7 itself states this claim was dropped as unsourced. Remove 'across 66 countries' from the heading."
- code: F5
  category: analytical-link-as-fact
  section: active-threats
  item: "The Gentlemen ransomware"
  url_or_quote: "PRODAFT adds that the administrator supplies affiliates with initial access, primarily Fortinet SSL-VPN credentials from brute-force or the group's own leak database"
  summary: "No PRODAFT URL cited; not in Krebs; contradicted by Check Point (affiliates obtain Fortinet VPN creds independently as access brokers). Add a PRODAFT source that states it or drop the administrator-supplies-credentials claim and the PRODAFT high-confidence attribution."
- code: F6
  category: claim-not-supported
  section: deep-dive
  item: "MariaDB CVE-2026-49261 deep dive (companion CVEs)"
  url_or_quote: "CVE-2026-48165 and CVE-2026-48163 (both CVSS 8.0) ... in the wsrep State Snapshot Transfer (SST) handshake ([NCSC-CH CSH, 2026-06-11])"
  summary: "NCSC-CH post 12627 names only CVE-2026-49261, no companion CVEs, no CVSS 8.0, no SST. MariaDB Foundation names all three but gives no CVSS. The 8.0 figure is unsourced; drop it or cite a source, and re-attribute the companion-CVE/SST detail to MariaDB Foundation."
```
