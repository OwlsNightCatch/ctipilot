**Model:** Anthropic Claude Opus 4.7 (`claude-opus-4-7`)
**Timestamps:** started_at=2026-05-18T00:37:00Z · ended_at=2026-05-18T00:42:37Z · duration_seconds=337
**Self-telemetry:** urls_checked=23 · webfetch_calls=22 · bridge_fetches=3 · websearch_calls=0

## Verification report — briefs/weekly/2026-W21.md (iteration 1)

Cold-read verification of the W21 weekly summary. 22 source URLs fetched via WebFetch + 3 bridge fetches; named entities (CVEs, actor groups, version numbers, statistics, dates) cross-checked against the cited sources. Findings span truth defects (cited source contradicts the claim or does not support it), editorial defects (low primary-source quality, missing flags), and one advisory.

### Broken / unreachable URLs

None confirmed broken from this verification pass. Notes:
- F5 NGINX advisory `https://my.f5.com/manage/s/article/K000161019` returned `certificate is not yet valid` from `WebFetch`. The URL appears in BleepingComputer's outbound links so is likely real; not flagging as broken but the verifier could not independently confirm content.
- `https://www.brighttalk.com/webcast/15099/665415` (Verizon DBIR webinar) returned HTTP 403. Same situation — likely real, content unverifiable from this side.
- `https://www.dastra.eu/...` returned `certificate is not yet valid` — likely real, content unverifiable.

### Citation does not support the claim

**F3.1 — Cisco SD-WAN CVSS score (§ 1 H3 footer + § 3 table + § 3 H3 footer)**
Brief claim quoted: *"CVSS: 9.9"* and *"(CVSS 9.9)"*.
Source fetched: `https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW`. The Cisco PSIRT advisory states the score is **CVSS 10.0** (CWE-287). Brief is wrong by 0.1 in the wrong direction (downplays severity).

**F3.2 — Cisco SD-WAN patched build numbers (§ 1 H3, § 3 table)**
Brief claim quoted: *"Cisco Catalyst SD-WAN Manager 20.15.1, 20.14.2, 20.13.3, 20.12.5; older releases require upgrade"* and table row *"Patched: Yes (20.15.1, 20.14.2, 20.13.3, 20.12.5)"*.
Source: same Cisco PSIRT page. The advisory lists fixed builds **20.9.9.1, 20.12.5.4, 20.12.6.2, 20.12.7.1, 20.15.4.4, 20.15.5.2, 20.18.2.2, 26.1.1.1**. The brief's build numbers are wrong and would lead operators to install non-existent patches. Critical truth defect.

**F3.3 — Talos "financially-motivated" / "ransomware deployment" framing (§ 1 H3 Cisco SD-WAN)**
Brief claim quoted: *"actively exploited by a cluster Talos tracks as UAT-8616 — a financially-motivated actor pivoting to ransomware deployment after initial credential exfiltration."*
Source: `https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/`. The Talos post describes UAT-8616 activity (SSH key addition, privilege escalation) but does NOT characterise UAT-8616 as "financially-motivated" nor mention "ransomware deployment". The motivation/ransomware claim is unsourced.

**F3.4 — "10+ exploitation clusters per Talos" attribution drift (§ 1 H3 + § 3 H3 + spawn-message context)**
Brief claim quoted: *"Cisco's security advisory identifies that 10+ active exploitation clusters have been observed"* and *"Talos tracks 10+ exploitation clusters including UAT-8616"*.
Source: Cisco PSIRT page does NOT mention 10+ clusters. Talos post says "10 distinct threat clusters actively exploiting three previously disclosed vulnerabilities (CVE-2026-20133, CVE-2026-20128, CVE-2026-20122)" — i.e. the 10 clusters are exploiting **older** SD-WAN CVEs, not CVE-2026-20182. The brief misattributes the 10-cluster figure to CVE-2026-20182.

**F3.5 — CISA Emergency Directive ED-26-03 unsupported by either cited source (§ 1 H3 + § 3 H3 + § 4 H3)**
Brief claim quoted: *"CISA Emergency Directive ED-26-03 mandates US FCEB agency remediation"* and *"The CISA ED-26-03 deadline for US FCEB agencies was 2026-05-17"*.
Sources for the item: Cisco PSIRT + Talos post. Neither cited source mentions "CISA Emergency Directive ED-26-03". The claim has no inline citation to a CISA page. Either add a primary CISA ED reference or drop the ED claim.

**F3.6 — PAN-OS CVSS score (§ 1 H3 footer + § 3 table)**
Brief claim quoted: *"CVSS: 9.1"*.
Source fetched: `https://security.paloaltonetworks.com/CVE-2026-0300`. PSIRT page states **CVSS 9.3 (CRITICAL)**, not 9.1.

**F3.7 — PAN-OS auth-bypass framing (§ 1 H3 footer)**
Brief footer tags: *"actively-exploited, cisa-kev, auth-bypass"*.
Source: PSIRT confirms this is a **CWE-787 buffer overflow** via the User-ID Authentication Portal, not an auth-bypass. The "auth-bypass" tag is technically incorrect.

**F3.8 — PAN-OS CL-STA-1132 actor and svc-health-check rogue-admin pattern unsupported by cited source (§ 1 H3)**
Brief claim quoted: *"CL-STA-1132 continues active exploitation per CISA KEV and the Palo Alto PSIRT advisory. Audit for the svc-health-check-NNNNNN rogue-admin account pattern before patching."*
Source: Palo Alto PSIRT page does NOT mention CL-STA-1132 nor the svc-health-check-NNNNNN account pattern. These details exist in prior Unit 42 reporting but the cited PSIRT page does not support them. Add a Unit 42 / Volexity inline citation or qualify the attribution.

**F3.9 — Microsoft Kazuar module names (§ 2 H3 + § 4 H3 + § 7 H3)**
Brief claim quoted: *"three distinct modules — KazuarNode (P2P relay mesh using victim machines as C2 relay infrastructure), KazuarMain (core backdoor with encrypted-channel C2 fallback), and KazuarLoader (staged deployment with anti-analysis)"*.
Source: `https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/`. Microsoft's actual module names are **Kernel, Bridge, Worker**. The brief's three names (KazuarNode, KazuarMain, KazuarLoader) are fully hallucinated and contradict the cited source.

**F3.10 — Grafana Labs source attribution (§ 0 TL;DR + § 2 § 5 + spawn-message context)**
Brief claim quoted: *"CoinbaseCartel — a data-extortion group active since September 2025, focusing exclusively on theft without encryption — exploited a pull_request_target GitHub Actions workflow misconfiguration"* and *"Grafana detected the exfiltration via a triggered canary token embedded in the private code"* and *"Ransom was demanded and rejected. Grafana confirmed no customer data, production systems, or running infrastructure was accessed — the exposure was private source code."*
Source cited: `https://grafana.com/blog/grafana-security-update-post-incident-review-for-github-workflow-vulnerability-and-whats-next/`. This blog post is dated **May 16, 2025** (not 2026) and describes the **April 26, 2025** incident; it makes NO mention of CoinbaseCartel, canary tokens, or ransom demands/rejection. The brief's claims map to the **The Hacker News article** (`https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html`, May 17, 2026) which does describe CoinbaseCartel attribution and ransom rejection. Action: (a) demote/replace the Grafana Labs 2025 blog as the primary source since it does not support the in-window CoinbaseCartel claims, (b) confirm the THN sourcing carries the 4-private-repos detail (THN summary I fetched does not include it explicitly), or qualify "private codebase exfiltrated" to "GitHub token used to clone the repository" per THN.

**F3.11 — ESET FrostyNeighbor target country and tooling (§ 4 H3 + § 7 H3)**
Brief claim quoted: *"a March–May 2026 campaign targeting Polish government, military, and media with spear-phishing delivering a new Python-based implant via a compromised Polish government document portal"* and *"targeting Polish government, military, and media organisations with spear-phishing delivered via a compromised Polish government document portal. A Python-based implant (new tooling) provides initial foothold"*.
Source fetched: `https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/`. ESET's actual content: targets **Ukrainian** governmental organizations (not Polish), uses **PDF spear-phishing impersonating Ukrtelecom**, deploys **PicassoLoader + Cobalt Strike** (NOT a Python-based implant). The brief's national-scope and tooling details are completely wrong against the cited source. Critical truth defect.

**F3.12 — SzafirHost CVE-2026-44088 vulnerability description (§ 4 H3)**
Brief claim quoted: *"Poland's CERT-PL disclosed CVE-2026-44088 in SzafirHost, a vendor providing JAR-signed qualified electronic signature services to public administration — a Magecart-style skimmer injection via the WooCommerce plugin vector."*
Source: `https://cert.pl/en/posts/2026/05/CVE-2026-44088/`. Actual CVE-2026-44088 is a **JAR zip-polyglot bypass / class-loading split-brain**, not a Magecart/WooCommerce skimmer. The brief has confused the SzafirHost item with the FunnelKit WooCommerce Magecart item from the same daily (2026-05-17). Daily 2026-05-17 itself correctly describes both items separately; the weekly summary fused them.

**F3.13 — BWH Hotels 181-day duration and payment metadata (§ 5 H3)**
Brief claim quoted: *"BWH Hotels disclosed 181-day unauthorised access to a web application handling guest reservation data. Affected data includes names, email addresses, booking details, and partial payment metadata."*
Source: `https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/...`. Article says unauthorised access spanned **October 14, 2025 → April 22, 2026** (~190 days, described as "approximately six months"), and explicitly states **"No payment or financial information was exposed"**. The brief's 181-day specific count and the "partial payment metadata" claim are not in the cited source — and the payment claim is directly contradicted.

**F3.14 — Verizon DBIR specific statistics (§ 6 H3)**
Brief claim quoted (multiple): *"Credential abuse remains the dominant initial-access vector (22% of breaches)"*, *"Vulnerability exploitation … (20% of breaches)"*, *"Third-party breaches doubled to 30% of incidents (from 15% the prior period)"*, *"14% of employees accessed GenAI tools on corporate devices; 72% of those did so via personal email accounts"*, *"EMEA at 18% espionage share; APAC at 34%"*, *"70% of espionage breaches used vulnerability exploitation on unpatched VPNs and edge devices"*.
Source: `https://www.verizon.com/business/resources/reports/dbir/`. The Verizon page only confirms the timeframe (Nov 2024 – Oct 2025) and that "the most frequent causes continue to heavily involve the human element". **None of the specific percentages are in the cited page**. The brief acknowledges this as `[SINGLE-SOURCE for specific statistics]` with a "pending webinar" caveat, but the statistics themselves are essentially uncited — they appear to be either pre-publication estimates or sourced from a different DBIR teaser that the brief does not cite. Either link a source that actually carries each percentage, or rewrite the section to omit specific percentages and frame as "the 2026 DBIR is forthcoming, expect coverage post-webinar".

**F3.15 — EU cyber sanctions named entities (§ 8 H3)**
Brief claim quoted: *"19 individuals and 7 entities subject to asset freezes, travel bans, and fund-transfer prohibitions, including Integrity Technology Group and Anxun Information Technology Co. Ltd (Chinese private companies added March 2026) and Emennet Pasargad (Iranian)"*.
Source: `https://dig.watch/updates/council-of-the-eu-extends-cyber-sanctions-framework-until-2027`. The dig.watch page confirms the 19/7 count and the date but does NOT name Integrity Technology Group, Anxun Information Technology, or Emennet Pasargad. The named-entity details are uncited.

**F3.16 — Germany NIS2 60% non-compliance statistics (§ 0 TL;DR + § 8 H3)**
Brief claim quoted: *"approximately 11,500 entities registered against an expected scope of ~29,500+ organisations (~38% compliance rate)"*.
Source: `https://blog.gdatasoftware.com/2026/03/38383-nis2-end-registration-period-management-teams`. The G DATA page describes the 6 March 2026 registration deadline and management training obligations but does NOT carry the 11,500 / 29,500 numbers. The 60% headline and 38% compliance figure have no supporting citation.

**F3.17 — German NIS2 specific penalty figures (§ 8 H3)**
Brief claim quoted: *"Non-registration fines reach €100,000 per § 65 para. 1 BSIG; substantive NIS2 failures reach €10 million or 2% of global annual turnover."*
Source: `https://www.klgates.com/...`. K&L Gates alert states fines "up to EUR€500,000" — neither the €100,000 figure nor the €10M / 2% turnover figure appears in this specific source. The €10M/2% likely matches the NIS2 directive itself; cite the directive (Article 34) inline if retaining the figure.

**F3.18 — BleepingComputer MiniPlasma identification (§ 2 H3)**
Brief claim quoted: *"a third PoC — \"MiniPlasma\" — appeared, apparently a variant of the same CTFMON IPC mechanism attributed to the same researcher ecosystem"*.
Source: `https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/`. BleepingComputer describes MiniPlasma as exploiting the **Cloud Filter driver `cldflt.sys`** (CVE-2020-17103 / claimed-patched-but-still-exploitable), NOT a CTFMON IPC variant. The brief's claim that MiniPlasma is a CTFMON IPC variant of GreenPlasma is factually wrong against the cited source.

**F3.19 — GTIG BlackFile victim sector profile (§ 7 H3)**
Brief claim quoted: *"Watch for a new data-leak site using the same victim profile (mid-market professional services, legal, and financial firms with SharePoint-based document storage)."*
Source: `https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/`. GTIG describes BlackFile victims as "dozens of organizations across North America, Australia, and the UK" without the specific "mid-market professional services / legal / finance" profile the brief asserts. The sector profile is uncited inference.

### Unsupported / hallucinated facts

**F4.1 — Foxconn data scope (§ 5 H3)**
Brief claim quoted: *"The group claimed theft of data belonging to Apple and Nvidia."*
Source: `https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144`. The Register article lists **Apple, Nvidia, Google, Dell, and Intel** as named-but-unverified victims. The brief's omission of Google/Dell/Intel under-reports the scope of the Nitrogen claim. Either list all five named or qualify "including Apple and Nvidia".

**F4.2 — Kimsuky article date (§ 7 H3)**
Brief claim quoted: *"Kaspersky GReAT's 2026-05-17 analysis"*.
Source: `https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/`. Article is dated **May 14, 2026**, not May 17. Minor date drift.

### Strengthen primary source

**F6.1 — Verizon DBIR 2026 (§ 6 H3 source row)**
Currently cited: Verizon DBIR landing page + BrightTalk webinar reservation page. Both are pre-publication / hub URLs that do not carry the specific statistics quoted. Promote a dated press release, analyst summary article, or — if not yet available — restructure the section to omit specific percentages until the full report drops.

**F6.2 — Grafana CoinbaseCartel item (§ 0 TL;DR + § 5 H3)**
Brief leads with the Grafana Labs blog as primary, but that blog (May 16, 2025) does not describe the May 2026 CoinbaseCartel incident. Promote The Hacker News (`https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html`) as primary (which carries the CoinbaseCartel attribution + ransom-rejection narrative + the FBI guidance framing), and demote / drop the 2025 Grafana blog.

### Single-source items missing [SINGLE-SOURCE] flag

The brief's § 10 already flags single-source items for Verizon DBIR statistics, Europol Anti-Scam Platform, ENISA CNA, MiniPlasma, The Gentlemen status, and the GTIG BlackFile rebrand assessment. The spawn message notes "check_brief.py WARN: 8 single-source items in §§ 1/3/7/8 without [SINGLE-SOURCE] flags in headings". Specific cases the verifier surfaces:

**F12.1 — PAN-OS § 1 H3 — only PA PSIRT cited as Source**
The PAN-OS H3 in § 1 ("PAN-OS CVE-2026-0300 — active exploitation ongoing; wave 2 patch builds delayed to 2026-05-28") cites only the Palo Alto PSIRT page + the daily-brief backlink. PSIRT is the canonical primary disclosing party; the national-CERT carve-out logic applies analogously (vendor PSIRT is single-source acceptable for its own product). Either add the carve-out reference inline ("vendor PSIRT acting as primary disclosing party for its own product — single-source acceptable") or add a corroborating Unit 42 / CISA-KEV inline link. Same shape for the Exchange CVE-2026-42897 § 1 H3 (cites MSRC + Exchange Team Blog + ZDI — multi-source, no flag needed).

**F12.2 — Kazuar § 7 H3 — Microsoft only**
The Kazuar status-update H3 cites only the Microsoft Security Blog post + the daily backlink. Microsoft is the disclosing primary; either add the vendor-PSIRT/disclosing-party carve-out call-out or add a corroborating secondary (Unit 42 Pensive Ursa earlier reporting, CISA AA23-129A, etc., already linked from the Microsoft post itself).

**F12.3 — FrostyNeighbor § 7 H3 — ESET only**
Currently cites only ESET WeLiveSecurity + daily backlink. Once F3.11 is fixed (correct target country + tooling), the ESET source becomes single-source disclosing party — flag as `[SINGLE-SOURCE]` or add a corroborating CERT-UA / SentinelOne / HarfangLab link (ESET's own post links to all three).

**F12.4 — Kimsuky § 7 H3 — Kaspersky only**
Cites only Kaspersky GReAT / Securelist + daily backlink. Single-source — flag or corroborate (the Securelist post itself links to Microsoft, AhnLab, Darktrace, Gen Digital coverage of related Kimsuky activity).

**F12.5 — BlackFile § 7 H3 — GTIG only**
Single-source on GTIG. The rebrand assessment is already flagged `[SINGLE-SOURCE-OTHER]` in § 10, but the parent H3 should carry `[SINGLE-SOURCE]` in the heading per the brief's own convention.

### Surface contradiction

**F9.1 — § 10 self-acknowledges Grafana / CoinbaseCartel reverse-attribution risk pattern not present**
§ 10 explicitly notes the verifier should check "Exchange CVE-2026-42897 vs. DEVCORE Pwn2Own three-bug chain" framing consistency — that consistency check passed (the brief carefully separates the two surfaces and explicitly notes Microsoft has not formally linked them). No contradiction to surface there.

However, the Grafana / CoinbaseCartel item creates a date contradiction the brief does not flag: the cited Grafana Labs blog is from 2025 and discusses a 2025 incident, while the TL;DR + § 2 + § 5 frame the incident as in-window May 2026 (which is correct per THN sourcing). The mismatch between the primary source (2025) and the in-window narrative needs either a contradiction line in § 10 or a re-pivot to THN as primary (see F6.2).

### Editorial / less-is-more flags (advisory)

**F11.1 — Verbose key strings in § 7 H3 headings**
The § 7 headings carry verbose `(key: item:...)` strings inside the heading (e.g. `(key: item:secret-blizzardevolves-kazuar-into-a-three-module-peer-to-pe)`). These appear to be internal coverage-log keys leaking into the published prose. They are noise for the reader. Strip the `(key: item:...)` parentheticals from § 7 headings.

**F11.2 — § 6 Verizon DBIR length vs uncertainty**
The Verizon DBIR section runs ~5 paragraphs with named statistics that the cited sources do not carry (per F3.14). If the source-quality cannot be hardened to support each percentage, shrink the section to a 2-paragraph "DBIR 2026 forthcoming — webinar 2026-05-19, full PDF expected after; here are the four daily-brief patterns the new edition is expected to validate" frame.

### Verdict

NEEDS_FIXES (truth: 21, editorial: 6, advisory: 2)

Truth tally counts: F3.1, F3.2, F3.3, F3.4, F3.5, F3.6, F3.7, F3.8, F3.9, F3.10, F3.11, F3.12, F3.13, F3.14, F3.15, F3.16, F3.17, F3.18, F3.19, F4.1, F4.2 (21).
Editorial: F6.1, F6.2, F12.1, F12.2, F12.3, F12.4, F12.5 (7, but F12.1 reads as advisory-style since vendor-PSIRT carve-out reasoning is straightforward; counting 6 to be conservative — see machine-readable summary).
Advisory: F11.1, F11.2 (2).

**Correction to verdict line counts**: editorial = 7 if we count F6.1, F6.2, F9.1, F12.1, F12.2, F12.3, F12.4, F12.5 → that's 8; better: F6.1, F6.2 (strengthen-primary), F9.1 (contradiction), F12.1, F12.2, F12.3, F12.4, F12.5 (single-source) = 8 editorial. Truth = 21. Advisory = 2.

**Authoritative tally**: truth=21, editorial=8, advisory=2.

The dominant pattern is **citation-claim mismatches on the highest-impact items** — Cisco SD-WAN (CVSS, builds, ED attribution, motivation framing, cluster count), PAN-OS (CVSS, actor cluster), Kazuar (module names), Grafana (wrong-year source), FrostyNeighbor (wrong country + wrong tooling), SzafirHost (item-fused with FunnelKit), BWH Hotels (duration + payment-metadata contradicted), Verizon DBIR (no source for any percentage), Germany NIS2 (no source for compliance numbers + wrong fine figures), EU cyber sanctions (uncited named entities). This level of source-versus-claim drift on the most-prominent items is publish-blocking — the daily briefs themselves are largely correct; the weekly's compositional pass introduced or compounded the errors.

### Findings summary (machine-readable)

```yaml
- code: F3.1
  category: claim-not-supported
  section: highest-impact-events
  item: "Cisco Catalyst SD-WAN CVE-2026-20182 — pre-auth authentication bypass under active exploitation"
  url_or_quote: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW"
  summary: "Brief says CVSS 9.9; Cisco PSIRT says CVSS 10.0"
- code: F3.2
  category: claim-not-supported
  section: highest-impact-events
  item: "Cisco SD-WAN CVE-2026-20182 patched-build list"
  url_or_quote: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa2-v69WY2SW"
  summary: "Brief lists 20.15.1, 20.14.2, 20.13.3, 20.12.5; PSIRT actually lists 20.9.9.1, 20.12.5.4, 20.12.6.2, 20.12.7.1, 20.15.4.4, 20.15.5.2, 20.18.2.2, 26.1.1.1 — operators would install non-existent builds"
- code: F3.3
  category: claim-not-supported
  section: highest-impact-events
  item: "Cisco SD-WAN UAT-8616 motivation"
  url_or_quote: "https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/"
  summary: "Brief calls UAT-8616 'financially-motivated' pivoting to 'ransomware deployment after initial credential exfiltration'; Talos post does not characterise motivation nor mention ransomware"
- code: F3.4
  category: claim-not-supported
  section: highest-impact-events
  item: "Cisco SD-WAN 10+ exploitation clusters attribution"
  url_or_quote: "https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/"
  summary: "Brief says 10+ clusters for CVE-2026-20182; Talos says 10 clusters target older CVE-2026-20133/-20128/-20122, not -20182"
- code: F3.5
  category: missing-citation
  section: highest-impact-events
  item: "CISA Emergency Directive ED-26-03 (§ 1, § 3, § 4)"
  url_or_quote: "'CISA Emergency Directive ED-26-03 in force' / 'CISA ED-26-03 deadline ... was 2026-05-17'"
  summary: "Neither Cisco PSIRT nor Talos cited sources mention ED-26-03; no CISA URL cited inline"
- code: F3.6
  category: claim-not-supported
  section: highest-impact-events
  item: "PAN-OS CVE-2026-0300 CVSS score"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-0300"
  summary: "Brief footer says CVSS 9.1; PSIRT says CVSS 9.3"
- code: F3.7
  category: claim-not-supported
  section: highest-impact-events
  item: "PAN-OS auth-bypass tag"
  url_or_quote: "PAN-OS CVE-2026-0300 footer 'Tags: ... auth-bypass'"
  summary: "PSIRT classifies as CWE-787 buffer overflow via crafted packets, not auth-bypass — tag is incorrect"
- code: F3.8
  category: claim-not-supported
  section: highest-impact-events
  item: "PAN-OS CL-STA-1132 and svc-health-check-NNNNNN account pattern"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-0300"
  summary: "PSIRT does not mention CL-STA-1132 nor the svc-health-check-NNNNNN rogue-admin pattern; brief attributes both to PSIRT — add Unit 42/Volexity inline citation or remove"
- code: F3.9
  category: hallucinated-fact
  section: multi-day-campaigns
  item: "Secret Blizzard / Turla Kazuar P2P module names"
  url_or_quote: "https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/"
  summary: "Brief names modules KazuarNode, KazuarMain, KazuarLoader; Microsoft post names them Kernel, Bridge, Worker — module names hallucinated"
- code: F3.10
  category: claim-not-supported
  section: incidents-and-disclosures
  item: "Grafana Labs / CoinbaseCartel breach"
  url_or_quote: "https://grafana.com/blog/grafana-security-update-post-incident-review-for-github-workflow-vulnerability-and-whats-next/"
  summary: "Cited Grafana blog is dated May 16, 2025 about an April 26 2025 incident; does not mention CoinbaseCartel, canary tokens, ransom, or 4 private repos — primary source must be the THN article instead"
- code: F3.11
  category: claim-not-supported
  section: sector-and-victim-patterns
  item: "FrostyNeighbor / Ghostwriter targets and tooling"
  url_or_quote: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
  summary: "Brief says targets Polish gov/military/media with Python-based implant via compromised Polish government portal; ESET says targets Ukrainian gov with PicassoLoader + Cobalt Strike via PDF spear-phishing impersonating Ukrtelecom"
- code: F3.12
  category: claim-not-supported
  section: sector-and-victim-patterns
  item: "SzafirHost CVE-2026-44088 description"
  url_or_quote: "https://cert.pl/en/posts/2026/05/CVE-2026-44088/"
  summary: "Brief says Magecart-style WooCommerce skimmer; CERT-PL describes JAR zip-polyglot bypass / class-loading split-brain (RCE via signed-JAR + ZIP combination) — weekly fused two separate daily items"
- code: F3.13
  category: claim-not-supported
  section: incidents-and-disclosures
  item: "BWH Hotels 181-day access and payment metadata"
  url_or_quote: "https://www.theregister.com/security/2026/05/11/best-western-hotels-confirms-web-app-data-breach/5238020"
  summary: "Brief says 181 days and 'partial payment metadata'; Register says ~190 days (Oct 14 2025 – Apr 22 2026, 'approximately six months') and explicitly 'No payment or financial information was exposed'"
- code: F3.14
  category: claim-not-supported
  section: annual-periodic-reports
  item: "Verizon DBIR 2026 specific statistics"
  url_or_quote: "https://www.verizon.com/business/resources/reports/dbir/"
  summary: "Brief quotes 22% credentials, 20% vulnerabilities, 30% third-party (doubled from 15%), 14% GenAI / 72% personal-email, 18% EMEA / 34% APAC espionage, 70% espionage via VPN/edge; Verizon page carries none of these percentages — entire stat block uncited"
- code: F3.15
  category: claim-not-supported
  section: policy-and-regulatory
  item: "EU cyber sanctions named entities"
  url_or_quote: "https://dig.watch/updates/council-of-the-eu-extends-cyber-sanctions-framework-until-2027"
  summary: "Brief names Integrity Technology Group, Anxun Information Technology Co. Ltd, Emennet Pasargad; dig.watch confirms 19/7 and dates but does not name any of the three entities"
- code: F3.16
  category: claim-not-supported
  section: policy-and-regulatory
  item: "Germany NIS2 60% non-compliance numbers"
  url_or_quote: "https://blog.gdatasoftware.com/2026/03/38383-nis2-end-registration-period-management-teams"
  summary: "Brief says ~11,500 of ~29,500+ registered (38% compliance, 60% non-compliance); G DATA page does not carry the 11,500 or 29,500 figures"
- code: F3.17
  category: claim-not-supported
  section: policy-and-regulatory
  item: "Germany NIS2 fine schedule"
  url_or_quote: "https://www.klgates.com/New-Cybersecurity-Regulations-in-GermanyRegistration-Requirement-Expires-on-6-March-2026-3-5-2026"
  summary: "Brief says €100,000 per § 65 BSIG for non-registration + €10M / 2% turnover for substantive; K&L Gates source carries only 'up to €500,000'. Cite the NIS2 directive Article 34 inline if retaining €10M/2%"
- code: F3.18
  category: claim-not-supported
  section: multi-day-campaigns
  item: "Windows MiniPlasma CTFMON attribution"
  url_or_quote: "https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/"
  summary: "Brief calls MiniPlasma 'a variant of the same CTFMON IPC mechanism' as GreenPlasma; BleepingComputer describes MiniPlasma as CVE-2020-17103 in Cloud Filter driver cldflt.sys — different vulnerability class"
- code: F3.19
  category: claim-not-supported
  section: long-running-campaigns
  item: "GTIG BlackFile victim sector profile"
  url_or_quote: "https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/"
  summary: "Brief says 'mid-market professional services, legal, and financial firms with SharePoint-based document storage'; GTIG only characterises victims as 'dozens of organizations across North America, Australia, UK' — sector profile uncited"
- code: F4.1
  category: hallucinated-fact
  section: incidents-and-disclosures
  item: "Foxconn / Nitrogen victim scope"
  url_or_quote: "https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144"
  summary: "Brief mentions only Apple and Nvidia; Register article lists Apple, Nvidia, Google, Dell, Intel as claimed victims"
- code: F4.2
  category: hallucinated-fact
  section: long-running-campaigns
  item: "Kaspersky Kimsuky article date"
  url_or_quote: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
  summary: "Brief cites '2026-05-17 analysis'; Securelist article dated May 14 2026"
- code: F6.1
  category: strengthen-primary-source
  section: annual-periodic-reports
  item: "Verizon DBIR 2026 H3"
  url_or_quote: "https://www.verizon.com/business/resources/reports/dbir/"
  summary: "Page is pre-publication landing page that does not carry any of the percentages quoted; either find a press release / dated summary that carries each percentage, or restructure section to omit specific percentages until full PDF drops"
- code: F6.2
  category: strengthen-primary-source
  section: incidents-and-disclosures
  item: "Grafana / CoinbaseCartel breach"
  url_or_quote: "https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html"
  summary: "Promote THN as primary (carries CoinbaseCartel attribution + ransom-rejection); demote 2025 Grafana Labs blog or remove (it does not describe the May 2026 incident)"
- code: F9.1
  category: surface-contradiction
  section: verification-and-coverage-notes
  item: "Grafana primary-source year mismatch"
  url_or_quote: "Grafana Labs blog dated 2025-05-16 vs. brief's in-window May 2026 framing"
  summary: "If primary remains the 2025 Grafana blog, add a contradiction line in § 10 noting the primary source is from a prior year incident; preferred: re-pivot per F6.2"
- code: F12.1
  category: single-source-flag-missing
  section: highest-impact-events
  item: "PAN-OS CVE-2026-0300 § 1 H3"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-0300"
  summary: "Only PSIRT cited; PSIRT is the disclosing primary so single-source acceptable, but either add the carve-out note or add a corroborating Unit 42 / CISA-KEV inline citation"
- code: F12.2
  category: single-source-flag-missing
  section: long-running-campaigns
  item: "Kazuar § 7 H3"
  url_or_quote: "https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/"
  summary: "Microsoft only cited; either flag [SINGLE-SOURCE] in heading or add a corroborating secondary"
- code: F12.3
  category: single-source-flag-missing
  section: long-running-campaigns
  item: "FrostyNeighbor § 7 H3"
  url_or_quote: "https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/"
  summary: "ESET only; flag [SINGLE-SOURCE] or add CERT-UA / SentinelOne / HarfangLab corroborating link"
- code: F12.4
  category: single-source-flag-missing
  section: long-running-campaigns
  item: "Kimsuky § 7 H3"
  url_or_quote: "https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/"
  summary: "Kaspersky only cited; flag [SINGLE-SOURCE] in heading"
- code: F12.5
  category: single-source-flag-missing
  section: long-running-campaigns
  item: "BlackFile § 7 H3"
  url_or_quote: "https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/"
  summary: "GTIG only cited; rebrand assessment flagged in § 10 but parent heading should carry [SINGLE-SOURCE]"
- code: F11.1
  category: editorial-advisory
  section: long-running-campaigns
  item: "§ 7 headings"
  url_or_quote: "'(key: item:secret-blizzardevolves-kazuar-into-a-three-module-peer-to-pe)' etc."
  summary: "Internal coverage-log keys leaking into published headings; strip the '(key: item:...)' parentheticals"
- code: F11.2
  category: editorial-advisory
  section: annual-periodic-reports
  item: "Verizon DBIR length vs uncertainty"
  url_or_quote: "§ 6 H3 — ~5 paragraphs of named percentages with no source carrying any of them"
  summary: "If F3.14 / F6.1 cannot be hardened, shrink the section to 2 paragraphs framed as 'DBIR 2026 forthcoming, expect coverage post-webinar' and drop the specific percentages"
```
