**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-17T22:53:29Z · ended_at=2026-05-17T23:00:38Z · duration_seconds=429
**Self-telemetry:** urls_checked=32 · webfetch_calls=22 · bridge_fetches=2

## Verification report — briefs/weekly/2026-W20.md (iteration 2)

### Broken / unreachable URLs

**F1** — § 3 CVE table, CVE-2026-46300 "Fragnesia" row.
- URL: `https://lore.kernel.org/all/cve-2026-46300-fragnesia/`
- Failure mode: ECONNREFUSED — connection refused. WebFetch returned an error; the URL does not resolve.
- Item text: "Linux kernel security advisory CVE-2026-46300"

**F2a** — § 3, § 7 Fortinet PSIRT FG-IR-26-031.
- URL: `https://fortiguard.fortinet.com/psirt/FG-IR-26-031`
- Failure mode: Page loads the Fortinet PSIRT navigation shell but returns "Unavailable - Could not retrieve this post at this time" for the advisory content. No CVE, product, or CVSS data is accessible. This is effectively a broken link for the claimed content.
- Also affects: `https://fortiguard.fortinet.com/psirt/FG-IR-26-032`

### Generic / oversight URLs (replace with specific article)

**F2b** — § 5, West Pharmaceutical Services 8-K entry.
- URL: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000105770&type=8-K&dateb=&owner=include&count=40`
- This is a search-results/listing index for all 8-K filings by the company — not the specific May 2026 8-K Item 1.05 filing itself. The source policy requires the specific filing URL.
- Suggested replacement: Navigate to the above listing page and retrieve the direct 8-K filing URL from May 2026 (the EDGAR filing detail page for that specific submission).

**F2c** — § 6 Verizon DBIR 2026.
- URL: `https://www.verizon.com/business/resources/reports/dbir/`
- This is a DBIR landing/listing index page. The specific DBIR 2026 statistics the brief cites (30% third-party, 44% ransomware, 22% credentials, 20% vulnerability exploitation, 60%+ human element) cannot be confirmed from this landing page — the full PDF has not been publicly released as of the brief date. The brief's § 10 acknowledges "page-summary level" confidence, but the source itself is still a listing page.
- Note: The brief explicitly acknowledges the full PDF is pending the 2026-05-19 webinar; § 10 flags this with reduced confidence. Given the brief's transparency about this limitation, this is advisory-level only — the landing page is the only available source.

**F2d** — § 2 Exchange / DEVCORE ZDI citation points to wrong day.
- URL cited: `https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn`
- The DEVCORE Microsoft Exchange 3-bug RCE chain (Orange Tsai, $200,000, SYSTEM) occurred on **Day Two** (2026-05-15) per the ZDI Day Two blog post. The Day Three post does not mention Exchange Server at all — DEVCORE's only Day Three entry is a Microsoft SharePoint exploit by splitline.
- Correct URL: `https://www.thezdi.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results`
- This affects: § 0 TL;DR, § 1 H3 Exchange, § 2 H3 Exchange multi-day chain, § 3 CVE table, § 9 looking-ahead bullet. All cite the Day Three ZDI post for the Exchange chain.

### Citation does not support the claim

**F3a** — § 7 Secret Blizzard / Turla, The Record citation.
- Claim: "The Record explicitly names targeting of government ministries, embassies, and defence departments across Europe and Central Asia"
- Cited source: `https://therecord.media/turla-secret-blizzard-russia-espionage-ukraine-cybercrime-tools`
- What the source actually says: This article is from **December 12, 2024** and describes Secret Blizzard hijacking Amadey malware and Storm-1837 backdoors to attack **Ukrainian military devices** (including devices with Starlink satellite internet). It mentions Secret Blizzard has "a history of targeting ministries of foreign affairs, embassies, government offices, defense departments" worldwide, but it does not name European government/embassy/defence targets and is not the 2026-05-14 Kazuar botnet analysis article.
- The Microsoft Security Blog source for the Kazuar botnet is correctly cited (`https://www.microsoft.com/en-us/security/blog/2026/05/14/kazuar-anatomy-of-a-nation-state-botnet/`) and does support "European and Central Asian" targeting broadly. The The Record citation does not support the "explicitly names" framing.

**F3b** — § 1 H3 DEVCORE Exchange chain — technical specifics not in cited source.
- Claim: "a logic flaw in SerializableTypeConverter that survives the 2023-era ProxyShell/ChainedSerializationBinder mitigations, a path normalisation flaw in the OAB virtual directory authorization filter, and an LDAP RBAC role-elevation primitive that promotes a guest mailbox to Organization Management"
- Cited source: `https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn` (and also the Day Two post)
- What the ZDI Day Two source actually says: "Orange Tsai (@orange_8361) of DEVCORE Research Team chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange" — no technical specifics about which bugs, no mention of SerializableTypeConverter, OAB virtual directory, or LDAP RBAC. The Day Three post does not mention Exchange at all.
- The specific bug descriptions in the brief are hallucinated — they appear nowhere in the ZDI sources.

**F3c** — § 1 H3 DEVCORE Exchange chain — "Exchange Server SE 2026 CU3" target version.
- Claim: "DEVCORE took Master of Pwn at Pwn2Own Berlin with a separate three-bug pre-auth SYSTEM RCE chain against Exchange Server SE 2026 CU3"
- Neither the ZDI Day Two nor Day Three post mentions "Exchange Server SE 2026 CU3" as the specific target. The ZDI Day Two post says only "Microsoft Exchange."
- This is a hallucinated version identifier not supported by the cited source.

### Unsupported / hallucinated facts

**F4a** — § 2 Cisco SD-WAN companion CVE identifiers.
- Claim: "Talos and CISA jointly identified exploiting February-2026 Catalyst SD-WAN companion CVEs (CVE-2026-12881, CVE-2026-12882, CVE-2026-13247 — patched in Q1 2026)"
- Talos source (`https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/`) actually names the companion February-2026 CVEs as: **CVE-2026-20133, CVE-2026-20128, CVE-2026-20122** (all CVE-2026-20xxx format). CVE-2026-12881, CVE-2026-12882, CVE-2026-13247 do not appear in the Talos post at all.
- The three CVEs named in the brief are hallucinated.

**F4b** — § 3 PHP patched version numbers.
- Claim: CVE-2026-6722, CVE-2026-7261, CVE-2026-7262 "Patched 2026-05-08" in PHP "8.4.8/8.3.22/8.2.30"
- Source URL: `https://www.php.net/ChangeLog-8.php#PHP_8_4_8`
- PHP changelog confirms these CVEs appear in **PHP 8.4.21** (released 07 May 2026), not in 8.4.8. The anchor `#PHP_8_4_8` in the cited URL points to a non-existent or incorrect version. The patched versions should be 8.4.21 (and equivalents in 8.3.x/8.2.x branches), not 8.4.8/8.3.22/8.2.30.

**F4c** — § 4 / § 6 Sophos: "federal government as hardest-hit CH sectors."
- Claim in § 4: "energy and federal government are named as the hardest-hit sectors in CH" 
- Claim in § 6: "energy and federal government as the hardest-hit CH sectors"
- Sophos source (`https://www.sophos.com/en-us/blog/sophos-state-of-identity-security-2026`) confirmed: Switzerland is named as having the highest breach rate (89%), but there is no Switzerland-specific sectoral breakdown in the source. The source lists energy/oil/gas/utilities globally at 80% — it does not identify federal government as a hardest-hit CH sector. This is an unsourced claim.

**F4d** — § 4 IGJ / Clinical Diagnostics ~941,000 patients figure.
- Claim: "~941,000 patients affected including cervical-cancer screening data"
- IGJ source (`https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging`) does not mention any patient count. The page discusses the NEN 7510 finding and cancer screening data but provides no numeric patient figure.
- The 941,000 figure has no support in the cited IGJ source and should either cite a different source that carries this figure, or be removed/qualified as an approximate figure from a different source (possibly the original breach reporting).

**F4e** — § 0 TL;DR "~88% of on-prem Exchange Server SE deployments in EU geographies have OWA exposed to the internet."
- No cited source in the TL;DR supports this specific figure. Neither the Microsoft Security Blog source nor the NCSC.ch Security Hub post mentions this 88% figure.
- This is an unsourced quantifier in the TL;DR bullet.

### Claims missing inline citation

**F5a** — § 8 EU CRA item, claim about "Delegated Regulation (EU) 2026/881 on delayed dissemination of sensitive notifications was published 20 April 2026."
- The § 8 CRA item cites only `https://digital-strategy.ec.europa.eu/en/factpages/cyber-resilience-act-implementation`. No inline citation for the specific Delegated Regulation (EU) 2026/881 is provided in the paragraph.

**F5b** — § 1 H3 Exchange, claim: "Microsoft Security Response Center confirmed mass scanning began on or before [2026-05-14]."
- No inline citation provided for the MSRC confirmation of a specific mass-scanning date. The cited source (Microsoft Security Blog) discusses exploitation but the specific "scanning began on or before 2026-05-14" date needs a citation.

### Strengthen primary source

No standalone F6 items — the primary sources for all CVE items are vendor PSIRTs or equivalent research-lab posts. The Fortinet PSIRT URL being temporarily unavailable (F2a) is noted but not an F6 pattern.

### Drop (low relevance / off-audience / not weekly content)

No items meet the drop threshold — all items presented address W-PD-1 questions (inaction = incident, cross-day pattern, or strategic horizon) and have clear CH/EU/public-sector nexus.

### Needs more research

**F8a** — § 0 TL;DR "~88% of on-prem Exchange Server SE deployments in EU geographies have OWA exposed to the internet."
- If retained, this figure needs a source (Shodan / Censys exposure analysis, or a vendor/research post citing this number). Suggested search: `site:shodan.io OR site:censys.io Exchange OWA "EU" internet-exposed statistics 2026`

**F8b** — § 3 CVE-2026-46300 "Fragnesia" — source URL broken (lore.kernel.org connection refused).
- Suggested replacement source: `https://www.wiz.io/blog/dirty-frag-linux-kernel-local-privilege-escalation-via-esp-and-rxrpc` (the Wiz Research post already cited in § 1 for Dirty Frag and in the CVE table for CVE-2026-43284 mentions Fragnesia / CVE-2026-46300). Use this as the source instead of the broken lore.kernel.org URL.

**F8c** — § 2 / § 7 "The Gentlemen" — Bedrock Safeguard decryptor published 2026-05-14.
- The Check Point Research source does not mention Bedrock Safeguard or the decryptor. The Bedrock Safeguard GitHub repo is cited and verifies the decryptor (35/35 files, XChaCha20/X25519), but no corroborating coverage of the decryptor from a security news outlet is cited. Single-source for the decryptor claim, though the GitHub repo is a primary source.

### Surface contradiction

**F9** — § 1 H3 Exchange DEVCORE chain: "pre-auth SYSTEM RCE" vs. ZDI day 2 description.
- The brief describes the DEVCORE Exchange chain as "pre-auth" — but the ZDI Day Two post does not characterise the prerequisite level (pre-auth vs. post-auth). Orange Tsai's Pwn2Own Exchange exploit entry says only "chained 3 bugs to achieve Remote Code Execution as SYSTEM." Without technical details, the "pre-auth" characterization cannot be confirmed from the ZDI source and may contradict the actual exploit flow.

### Missed angles

**F10** — Given the week's heavy Exchange coverage, the brief does not mention whether EUVD has an entry for CVE-2026-42897 and whether CERT-EU issued a standalone advisory. The ENISA EUVD (noted in § 10 Coverage Gaps as an SPA that couldn't be fetched) likely carries a CVSS-exploited rating for this CVE that would reinforce the § 3 inclusion criteria.
- Suggested search: `EUVD CVE-2026-42897 exploited CERT-EU advisory May 2026`

### Editorial / less-is-more flags (advisory)

**F11a** — § 4 Manufacturing: "The W19 cross-cutting 'AI-tooling SaaS multi-tenant credential aggregation' theme remains relevant to manufacturing IT teams via the Mini Shai-Hulud propagation (see Multi-day campaigns above)." This cross-reference is weak for a weekly synthesis — the manufacturing sector item has already been thoroughly covered and this sentence adds nothing actionable. Advisory: remove the cross-reference sentence.

**F11b** — § 8 CISA ED-26-03 item: "the second ED in 2026 to date" — this is a quantifier that cannot be verified without checking all 2026 CISA EDs, and it adds minimal operational value. Advisory: remove or source explicitly.

### Single-source items missing [SINGLE-SOURCE] flag

**F12a** — § 7 SEPPmail CVE-2026-44128 H3: The heading does not carry `[SINGLE-SOURCE]` flag. The brief states in § 10 this is still `SINGLE-SOURCE-NATIONAL-CERT`; the H3 heading itself and its Source footer do not carry the marker.
- Both NCSC-CH and CIRCL are cited in the Source line, and the brief's § 10 explains the status has improved. However, the brief acknowledges in § 10 that it remains single-source-national-cert category. Per F12 rule, the carve-out (national-CERT acting as primary disclosing party for its own jurisdiction) does apply here — CIRCL is Luxembourg's national CERT disclosing for a European email-gateway product. The carve-out is explicitly noted in § 10, satisfying the F12 contract. This is acceptable; marking as reviewed and compliant.

**F12b** — § 7 "Qilin DLS lists 65 German victims total as of 2026-05-16" — this is attributed to "W1 horizon research" in § 10 but the H3 source footer for the Qilin item cites only `https://blog.checkpoint.com/research/cyber-threats-spike-in-april-2026-as-ransomware-expands-and-attack-volumes-climb-after-short-lived-moderation/`. The Check Point blog post does not mention 65 German Qilin victims. The 65-victim figure is uncited (the W1 research note in § 10 acknowledges it as a "lower bound" but provides no URL). This is an unsourced quantifier carried from W1 sub-agent research without a primary source link.

### Analytical-link-as-fact

**F13** — § 2 TeamPCP / Shai-Hulud: "the BreachForums 'supply chain challenge' encouraging third-party use of Shai-Hulud against other package registries (PyPI, Cargo, Maven Central) is the immediate forward risk for 2026-W21."
- Neither the Datadog Security Labs source nor the Wiz Blog source mentions a "BreachForums supply chain challenge." The Datadog static analysis post describes the Shai-Hulud framework capabilities (IDE persistence, OIDC extraction, Sigstore forgery, deadman switch) but does not mention BreachForums or a "challenge." The Wiz Blog covers the TanStack compromise but does not mention BreachForums.
- The BreachForums claim is asserted as fact and treated as a forward-risk driver in both § 2 and § 9, but no cited source supports it.

### Quantifier without source

**F14a** — § 0 TL;DR: "~88% of on-prem Exchange Server SE deployments in EU geographies have OWA exposed to the internet."
- No cited source supports this specific percentage. Neither the Microsoft Security Blog nor NCSC.ch post carries this figure. This is a quantifier with no source. (See also F5b / F8a above.)

**F14b** — § 2 Cisco SD-WAN: "10+ additional intrusion clusters."
- Talos source confirms exactly **10 clusters** (Cluster #1 through #10). The "10+" overstatement implies more than ten, which is not supported by the source.

**F14c** — § 7 Qilin: "Qilin DLS lists 65 German victims total as of 2026-05-16."
- Not confirmed in the cited Check Point source. The 65-victim figure has no cited primary source (per F12b above).

### Name-collision unflagged

No name-collision issues identified. "Shai-Hulud" is used consistently to refer to the TeamPCP framework; no prior coverage in the gap window uses the name for a different entity (this iteration confirms the Datadog article names it as the TeamPCP offensive framework, consistent with prior W19 coverage).

---

### Verdict

NEEDS_FIXES (truth: 12, editorial: 2, advisory: 2)

**Truth findings (F1, F3, F4, F13, F14):**
- F1: 2 broken/unreachable URLs (lore.kernel.org CVE-2026-46300, Fortinet PSIRT FG-IR-26-031/032)
- F2d: ZDI citation wrong day (Day 3 instead of Day 2 for DEVCORE Exchange)
- F3a: The Record Kazuar citation doesn't support W20 claims (December 2024 article about Ukraine military)
- F3b: SerializableTypeConverter / OAB virtual directory / LDAP RBAC technical specifics hallucinated — not in ZDI source
- F3c: "Exchange Server SE 2026 CU3" version identifier not in ZDI source
- F4a: Cisco companion CVEs hallucinated (CVE-2026-12881/12882/13247 — actual: CVE-2026-20133/20128/20122)
- F4b: PHP patched versions wrong (says 8.4.8, actual: 8.4.21)
- F4c: "federal government as hardest-hit CH sector" — not in Sophos source
- F4d: ~941,000 patients figure — not in IGJ source
- F13: BreachForums "supply chain challenge" — not in any cited source
- F14a: "~88% OWA exposed in EU" — no source
- F14b: "10+" clusters — source says exactly 10

**Editorial findings (F2b, F5a, F5b, F12b):**
- F2b: West Pharmaceutical SEC URL is listing index, not specific filing
- F5a: Delegated Regulation (EU) 2026/881 claim — no inline citation
- F5b: "mass scanning confirmed on or before 2026-05-14" — no inline citation
- F12b: Qilin 65 German victims — uncited quantifier in source footer

**Advisory findings (F11a, F11b):**
- F11a: Manufacturing sector weak cross-reference sentence
- F11b: "second ED in 2026 to date" — unverifiable claim, low value

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: broken-url
  section: vulnerability-rollup
  item: "CVE-2026-46300 Linux kernel xfrm ESP-in-TCP LPE Fragnesia"
  url_or_quote: "https://lore.kernel.org/all/cve-2026-46300-fragnesia/"
  summary: "ECONNREFUSED — connection refused on WebFetch; replace with Wiz Research Dirty Frag post which mentions CVE-2026-46300 (https://www.wiz.io/blog/dirty-frag-linux-kernel-local-privilege-escalation-via-esp-and-rxrpc)"

- code: F1
  category: broken-url
  section: vulnerability-rollup-h3-and-sector-pattern"
  item: "CVE-2026-44277 FortiAuthenticator unauthenticated RCE / CVE-2026-26083 FortiSandbox"
  url_or_quote: "https://fortiguard.fortinet.com/psirt/FG-IR-26-031 and https://fortiguard.fortinet.com/psirt/FG-IR-26-032"
  summary: "PSIRT advisory pages return unavailable error — could not retrieve advisory content. No CVE, CVSS, or product data accessible at these URLs as of verification time."

- code: F2
  category: generic-url
  section: incidents-disclosures
  item: "West Pharmaceutical Services — SEC Form 8-K Item 1.05 [SINGLE-SOURCE-OTHER]"
  url_or_quote: "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000105770&type=8-K&dateb=&owner=include&count=40"
  summary: "This is a search-results listing index for all 8-K filings by the company, not the specific 8-K Item 1.05 filing from May 2026. Replace with the specific EDGAR filing detail URL for the May 2026 8-K submission."

- code: F2
  category: generic-url
  section: exchange-devcore-chain-multiple-sections"
  item: "Microsoft Exchange / DEVCORE Pwn2Own three-bug RCE chain — ZDI citation"
  url_or_quote: "https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn"
  summary: "The DEVCORE Exchange exploit (Orange Tsai, 3-bug chain, $200,000, SYSTEM RCE) occurred on Day TWO (2026-05-15), not Day Three. The Day Three ZDI post does not mention Exchange Server at all — DEVCORE's Day Three entry is a SharePoint exploit. Replace with https://www.thezdi.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results"

- code: F3
  category: claim-not-supported
  section: long-running-campaigns
  item: "Secret Blizzard / Turla — The Record citation"
  url_or_quote: "https://therecord.media/turla-secret-blizzard-russia-espionage-ukraine-cybercrime-tools"
  summary: "This article is from December 12, 2024 and covers Ukraine military device targeting via Amadey/Storm-1837 hijacking. It does not describe the 2026-05-14 Kazuar P2P botnet evolution with European ministry/embassy/defence-department targeting. The claim that The Record 'explicitly names targeting of government ministries, embassies, and defence departments across Europe and Central Asia' is not supported by this article — it mentions those as historical targeting patterns, not current W20 named victims."

- code: F3
  category: claim-not-supported
  section: highest-impact-events-h3-exchange
  item: "DEVCORE three-bug Exchange chain technical specifics"
  url_or_quote: "SerializableTypeConverter / OAB virtual directory authorization filter / LDAP RBAC role-elevation primitive / Exchange Server SE 2026 CU3"
  summary: "Neither the ZDI Day Two post (https://www.thezdi.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results) nor the Day Three post mentions any of these technical details. The Day Two post says only 'chained 3 bugs to achieve Remote Code Execution as SYSTEM on Microsoft Exchange.' The specific bug descriptions and the 'Exchange Server SE 2026 CU3' target version are hallucinated."

- code: F4
  category: hallucinated-fact
  section: multi-day-campaigns-cisco-sdwan
  item: "Cisco Catalyst SD-WAN companion CVE identifiers"
  url_or_quote: "CVE-2026-12881, CVE-2026-12882, CVE-2026-13247"
  summary: "Talos source (https://blog.talosintelligence.com/sd-wan-ongoing-exploitation/) confirms the February-2026 companion CVEs are CVE-2026-20133, CVE-2026-20128, CVE-2026-20122. The three CVEs named in the brief (CVE-2026-12881, CVE-2026-12882, CVE-2026-13247) do not appear in the Talos post."

- code: F4
  category: hallucinated-fact
  section: vulnerability-rollup
  item: "PHP SOAP UAF CVE-2026-6722 patched version"
  url_or_quote: "Patched 2026-05-08 in PHP 8.4.8 / 8.3.22 / 8.2.30"
  summary: "PHP changelog confirms these CVEs are fixed in PHP 8.4.21 (released 07 May 2026), not 8.4.8. The source URL anchor #PHP_8_4_8 is incorrect; the patched version is 8.4.21. The release date of 07 May 2026 is close to the stated 2026-05-08 date so the date is approximately correct, but the version number is wrong."

- code: F4
  category: hallucinated-fact
  section: sector-patterns-public-administration
  item: "Sophos: federal government as hardest-hit CH sector"
  url_or_quote: "energy and federal government are named as the hardest-hit sectors in CH"
  summary: "Sophos source confirms Switzerland has the highest breach rate (89%) but provides no Switzerland-specific sectoral breakdown. The source lists energy/oil/gas/utilities globally at 80% — no 'federal government' sector is named as specifically hardest-hit in Switzerland."

- code: F4
  category: hallucinated-fact
  section: incidents-disclosures-clinical-diagnostics
  item: "~941,000 patients affected — Clinical Diagnostics / NMDL"
  url_or_quote: "~941,000 patients affected including cervical-cancer screening data"
  summary: "IGJ source (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging) does not mention any patient count. The page discusses NEN 7510 non-conformity and cancer screening data but provides no numeric patient figure. A different source carrying this figure must be cited, or the figure removed."

- code: F13
  category: analytical-link-as-fact
  section: multi-day-campaigns-teampcp
  item: "BreachForums supply chain challenge"
  url_or_quote: "the BreachForums 'supply chain challenge' encouraging third-party use of Shai-Hulud against other package registries (PyPI, Cargo, Maven Central) is the immediate forward risk for 2026-W21"
  summary: "Neither the Datadog Security Labs source nor the Wiz Blog source mentions a BreachForums supply chain challenge. The Datadog post describes framework capabilities; the Wiz Blog covers the TanStack compromise. This claim is asserted as established fact and used as a forward-risk driver in both § 2 and § 9 with no cited source."

- code: F14
  category: quantifier-without-source
  section: tl-dr-week-at-a-glance
  item: "~88% of on-prem Exchange Server SE deployments in EU geographies have OWA exposed to the internet"
  url_or_quote: "~88% of on-prem Exchange Server SE deployments in EU geographies have OWA exposed to the internet"
  summary: "No cited source supports this specific percentage. The Microsoft Security Blog and NCSC.ch post confirm active exploitation but neither cites an 88% EU OWA exposure figure."

- code: F14
  category: quantifier-without-source
  section: highest-impact-events-h3-cisco-sdwan
  item: "10+ additional intrusion clusters"
  url_or_quote: "10+ additional intrusion clusters exploiting February-2026 Catalyst SD-WAN companion CVEs"
  summary: "Talos source documents exactly 10 clusters (Cluster #1 through #10). '10+' implies more than ten, which is not supported. Should read 'approximately 10' or 'at least 10 distinct' per source language."

- code: F14
  category: quantifier-without-source
  section: long-running-campaigns-qilin
  item: "Qilin DLS lists 65 German victims total as of 2026-05-16"
  url_or_quote: "Qilin DLS lists 65 German victims total as of 2026-05-16"
  summary: "The cited Check Point Research source does not mention 65 German victims. The figure is attributed in § 10 to 'W1 horizon research' but has no primary source URL in the H3 Source footer."

- code: F5
  category: missing-citation
  section: policy-regulatory-cra
  item: "Delegated Regulation (EU) 2026/881 on delayed dissemination"
  url_or_quote: "Delegated Regulation (EU) 2026/881 on delayed dissemination of sensitive notifications was published 20 April 2026"
  summary: "No inline citation is provided for this specific regulation. The section cites only the EC CRA implementation factpage which does not contain this specific delegated regulation reference."

- code: F5
  category: missing-citation
  section: highest-impact-events-h3-exchange
  item: "MSRC confirmed mass scanning began on or before 2026-05-14"
  url_or_quote: "Microsoft Security Response Center confirmed mass scanning began on or before that date"
  summary: "No inline citation provided for the specific scanning-start-date confirmation. The Microsoft Security Blog is cited but the specific claim about mass scanning confirmation date needs a direct link."

- code: F11
  category: editorial-advisory
  section: sector-patterns-manufacturing
  item: "W19 cross-cutting theme cross-reference sentence"
  url_or_quote: "The W19 cross-cutting 'AI-tooling SaaS multi-tenant credential aggregation' theme remains relevant to manufacturing IT teams via the Mini Shai-Hulud propagation"
  summary: "Advisory: this sentence adds no actionable content for a defender. The manufacturing section should stand on its own without weak cross-references to a different week's theme."

- code: F11
  category: editorial-advisory
  section: policy-regulatory-cisa-ed
  item: "second ED in 2026 to date"
  url_or_quote: "the second ED in 2026 to date"
  summary: "Advisory: this cardinal claim cannot be easily verified and adds minimal operational value. Remove or add an explicit citation."
```
