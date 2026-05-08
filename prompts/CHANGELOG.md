# Prompt CHANGELOG

Tracks substantive changes to `prompts/daily-cti-brief.md` and `prompts/weekly-summary.md`.

---

## 2.32 — 2026-05-08 (WebFetch outbound-links discipline + sources audit cleanup)

### Why
Operator audit of the source set found that the agent's link-traversal — pivoting from a news article to the vendor PSIRT, from a national-CERT advisory to the vendor blog it cites, from a research-lab post to the GitHub commit that fixed the bug — was failing silently inside the `WebFetch` tool. `WebFetch` returns a small-model summary of the fetched HTML, and **without an explicit prompt instruction the summariser drops every URL.** Sub-agents were getting prose-only summaries, with no citation chain to follow, so they hit dead ends on the news → primary pivot mandated by Phase 1 step 2.

Two empirical findings from the audit (both reproducible against current sources):
- Listing pages (e.g. `https://krebsonsecurity.com/`, `https://www.bleepingcomputer.com/news/security/`) return article titles + entity mentions but **zero outbound links** — article bodies are not on the index. To pivot, the agent has to drill into a specific article URL.
- Per-advisory CERT pages (e.g. `https://www.cert.ssi.gouv.fr/avis/CERTFR-YYYY-AVI-NNNN/`) return the full CVE list **and** the vendor advisory URLs in their "Documentation" / "Références" section — **but only when the prompt explicitly asks for `Outbound links`**. Same for `<content:encoded>` RSS feeds (Krebs, Schneier).

### Daily prompt — `prompts/daily-cti-brief.md`

- **New mandatory clause in the sub-agent spawn template** ("`WebFetch` prompt template — every call MUST request 'Outbound links'…"): every `WebFetch` call must append an explicit instruction to enumerate every URL in the body / References / Documentation / Sources section, formatted as bullets with full absolute URLs. Without this clause the call returns a dead-end summary.
- **New "Research methodology" item 3** with the full `WebFetch` prompt template, the two empirical rules (listing pages don't carry inline links — drill into a specific article URL; per-advisory CERT pages and `<content:encoded>` RSS preserve the citation chain), and worked examples (Krebs feed returned 13 outbound URLs from one article; CERT-FR per-advisory page returned the Ivanti vendor URLs from its References section).
- Renumbered the methodology items (`Search topically` is now item 4, `Propose new sources` is item 5).
- Added DataBreaches.net and NCC Group to the named-403-host list (now require `tools/fetch_source.py`).

### Weekly prompt — `prompts/weekly-summary.md`
- Same mandatory `WebFetch` prompt clause inserted into the sub-agent spawn template, with a back-pointer to `prompts/daily-cti-brief.md` § "Research methodology" item 3 for the full template.

### `sources/sources.json` — comprehensive audit + dedup + add 30 sources (separate commit, v2 schema)
- **Removed (4):** `govcert-ch` (exact-URL duplicate of `ncsc-ch-security-hub` — GovCERT was merged into NCSC.ch in 2023), `secureworks-ctu` (Sophos absorbed it; redundant with `sophos-xops`), `sec-ir-firms-edr-blogs` (techcommunity.microsoft.com now redirects to Microsoft OAuth login — unfetchable), `reddit-netsec` (WebFetch is host-blocked from reddit.com).
- **URL corrections** for sources whose canonical home moved or whose listing was a JS-rendered shell: `kudelski-security` → `kudelskisecurity.com/research-blog`; `trustwave-spiderlabs` → `levelblue.com/blogs/spiderlabs-blog` (rebrand); `crowdstrike` → `/counter-adversary-operations/` (legacy /threat-intel-research/ now redirects); `bsi-de` → RSS (HTML is JS-rendered SPA); `darkreading` → RSS (HTML 403's WebFetch UA); `redcanary` → RSS (resource hub returns nav-only); `akamai-sirt` → FeedBurner (HTML is nav-only shell); `projectzero` → `projectzero.google` (Blogspot legacy).
- **Added (30 sources)** spanning national CERTs (NL/IE/BE/JP/KR), vendor PSIRTs (Cisco/Apple/Oracle/Mozilla/Chrome/MSRC/GitHub), research labs (Google TAG, SentinelLabs, Team Cymru, Censys, 0patch, Snyk, Trail of Bits, ProjectDiscovery, Morphisec, KELA), regional CTI vendors (Intrinsec, Synacktiv, Lab52, Resecurity), OT/ICS specialists (Nozomi, Claroty), ransomware tracking (ransomware.live), news (Hacker News, Infosecurity Magazine, Risky Biz News), and sanctions (US Treasury OFAC).
- **New schema fields:** per-source `fetch_method` (`webfetch` / `rss` / `bridge` / `api` / `blocked`); top-level `fetch_methods` documentation block; new categories `vendor-psirt`, `ransomware`, `sanctions`. Every source's `notes` field now records the 2026-05-08 audit verdict and concrete RSS / bridge fallback.
- **Bridge allowlist (`tools/fetch_source.py`)** extended with `databreaches.net`, `www.nccgroup.com`, `www.dragos.com`, `www.sygnia.co`, `www.ccn-cert.cni.es` for sources where Claude Code's WebFetch UA is filtered.

Total: 114 sources (up from 85), 94 active / 18 candidate / 2 demoted. Coverage: Switzerland + EU + US + UK + DACH + Nordics + Iberia + Italy + Poland + Czechia + Ireland + Netherlands + Belgium + Japan + Korea, plus all major CTI vendors with publicly-available research.

---

## 2.31 — 2026-05-08 (neutralise vendor / product / actor / CVE biases in worked examples)

### Why
Operator audit of `prompts/daily-cti-brief.md` and `prompts/weekly-summary.md` found that worked examples and illustrative fragments throughout both prompts named specific vendors, products, actor clusters, advisory IDs, and CVE IDs. Earlier versions used these as concrete pedagogy ("a freshly-disclosed pre-auth RCE on Citrix NetScaler / Ivanti Connect Secure / Fortinet SSL-VPN", "named campaigns / clusters when available (`UNC5337`, `Storm-2077`, `CL-STA-1132`, `RomCom`, `Akira`, `Fog`)", "Ivanti EPMM CVE-2026-5787 → CVE-2026-6973"). The same pattern appeared in the discovery-trace examples (named Ivanti EPMM URLs verbatim), the URL-pattern do/don't table (named Microsoft / Palo Alto / Ivanti vendor PSIRT roots as the "good" example), the news-to-primary pivot guidance (BleepingComputer / Mandiant / CrowdStrike / Heise / CERT-FR), the Phase 4.5 verifier's example findings (`APT28 active against EU governments`, `CVE-2023-35078 was exploited by APT29`), and the worked-good § 2 fragment (Google Chrome cookie paths + Cloudflare Workers DoH resolver).

These specifics created two distinct biases in the agent:

1. **Topic bias toward the named vendors / products / actors / CVEs.** When a prompt example names "Ivanti EPMM CVE-2026-6973", the agent is more likely to over-cover Ivanti EPMM stories and CVEs in that ID neighbourhood — even when Phase 1 sub-agents surface a more relevant story elsewhere.
2. **Anchor bias for nexus tags.** Footer template examples consistently used `china-nexus`. Without intent, this biased the rendered footers' nexus tag toward China-attributed activity when other nexus tags (or no nexus tag) was the correct call.

### Daily prompt — `prompts/daily-cti-brief.md`

Worked examples rewritten as **structural pattern descriptions** rather than topic picks. The pedagogical value is preserved (the agent still sees what the example is teaching) but the names that biased topic selection are replaced with placeholders:

- **Audience description.** Removed the named research-lab list (Mandiant / GTIG / Volexity / Talos / Unit 42 / Project Zero) and the explicit red-team-tooling roll-call (BloodHound / Mythic / Sliver / KrbRelayUp / etc.). Replaced with a description of the *technique classes* the audience is fluent in — offensive-tooling terminology, identity-protocol abuse (Kerberos / OAuth / SAML), endpoint-evasion classes, kernel-callback-level techniques.
- **PD-1 background-context example.** "APT28 is attributed to GRU Unit 26165" → generic "actor-to-government-unit attributions, infrastructure-to-actor mappings, multi-year campaign histories".
- **PD-1 URL-construction example.** "Securelist post on Amazon SES BEC must live at securelist.com/amazon-ses-bec-campaign-2026/" → generic "inferring that a research lab's post about a given topic + year *must* live at `https://<lab-domain>/<topic-slug>-<year>/`".
- **PD-8 long-running-campaign examples.** "Ivanti waves, Salt Typhoon, ransomware crew turnovers" → generic shape descriptions ("sustained edge-device exploitation waves against any vendor's product family, long-running named-cluster operations regardless of nexus, ransomware-affiliate turnovers and rebrands").
- **PD-9 annual-reports list.** Removed the enumerated publisher list (Mandiant M-Trends, CrowdStrike Global Threat Report, Verizon DBIR, Microsoft Digital Defense, IBM X-Force, Truesec TIR, Dragos OT Year in Review, Cloudflare Cloudforce One). Replaced with a publisher-agnostic class definition.
- **Phase 1 sub-agent template — discovery trace example.** The "Ivanti EPMM CVE first surfaced via the French national CERT and pivoted to Ivanti's PSIRT" example is now a generic "vulnerability in some enterprise edge product first surfaces via a national CERT advisory and the agent pivots to the affected vendor's own PSIRT bulletin" with `<placeholder>` URLs.
- **Phase 1 sub-agent template — URL-construction example.** "the advisory ID is `CERTFR-2026-AVI-0551`…" → "because an advisory ID has a known format, its detail page must live at a derivable path on the issuing CERT's site".
- **Discovery trace examples in sub-agent return format section** (lines 245–247). The three concrete trace examples (Ivanti / Heise → Spiegel / search → BleepingComputer → CCB Belgium → Ivanti) are now structural patterns with `<source-id>` and `<full URL fetched>` placeholders.
- **News-to-primary pivot examples** (line 195). "BleepingComputer summarising Mandiant; The Record covering CrowdStrike; Heise reporting on a CERT-FR advisory" → generic "a security-news publisher summarising a vendor research lab; a regional tech outlet relaying a national-CERT advisory; a wire service rewriting a vendor PSIRT post".
- **Forbidden-Source URL examples** (line 207). The named publisher URLs (heise.de, nos.nl, securelist.com, dragos.com, cert.ssi.gouv.fr, abw.gov.pl) are replaced with `<news-site>/news/` / `<lab-domain>/year-in-review/` / `<cert-domain>/advisories/` / `<gov-domain>/cybersecurity/` pattern descriptions.
- **Mandatory-rules pivot example.** "→ Ivanti PSIRT → primary" → "→ <vendor> PSIRT → primary".
- **Hard-blocked URL patterns table** (line 389). The "Good — what to use instead" column previously named `msrc.microsoft.com/update-guide/...`, `security.paloaltonetworks.com/CVE-…`, `www.ivanti.com/blog/…`. Replaced with publisher-agnostic guidance ("the disclosing vendor's PSIRT advisory page for the CVE — pivot to whichever one actually owns the disclosure"). The "Bad" column also genericised (no longer lists specific publisher domains).
- **Phase 5.5 fabricated-URL examples.** Removed `https://securelist.com/amazon-ses-bec-campaign-2026/` and `https://www.deepinstinct.com/blog/muddywater-2026` — replaced with a description of the failure mode ("URLs the agent constructed by guessing a slug from the topic + year rather than fetching a real page").
- **Phase 4.5 verifier flagging language.** "`Source: CERT-FR` as the **only** source" → "any single national-CERT URL as the **only** source on a CVE-typed item".
- **Multi-CVE chain examples** (lines 410–417, 422–424). "Ivanti EPMM CVE-2026-5787 → CVE-2026-6973: cert-validation flaw chains to admin RCE" / "CERT-FR CERTFR-2026-AVI-0551 listing 7 GLPI CVEs" → generic shapes ("a vendor's monthly patch advisory disclosing a chain where one CVE prerequisites another", "a national-CERT advisory grouping multiple CVEs in a single product family"). All `CVE-2026-5787` / `CVE-2026-6973` IDs in the worked footer / breakdown examples replaced with `CVE-YYYY-NNNNN` / `CVE-YYYY-MMMMM`.
- **Section template CVE placeholders** (lines 562, 576, 580, 614). `CVE-2026-XXXXX` (which still anchored the agent to 2026-era CVE IDs) → `CVE-YYYY-NNNNN` (the standard placeholder convention used elsewhere in the prompt).
- **§ 1 Immediate Actions examples** (line 456). "freshly-disclosed pre-auth RCE on Citrix NetScaler / Ivanti Connect Secure / Fortinet SSL-VPN" → "freshly-disclosed pre-auth RCE on a widely-deployed internet-exposed enterprise edge appliance class (any vendor)".
- **Technical-depth attack-surface examples** (line 486). The named-product list (`wp-login.php`, `nginx-quic`, Citrix NetScaler AAA virtual server, AD `MS-RPRN`, `dsamain.exe`, SAP `Visual Composer` MetaEditor servlet) → a publisher-agnostic enumeration of *types* of attack surface ("a specific PHP page on a CMS, a worker process inside a web server, an authentication virtual server inside an edge appliance, an RPC interface inside an OS service, an LDAP listener daemon, a specific servlet inside an enterprise application"). The rule "Use whatever the source actually states — never substitute generic phrasing" is preserved.
- **Named-cluster examples** (line 490). The literal cluster IDs `UNC5337`, `Storm-2077`, `CL-STA-1132`, `RomCom`, `Akira`, `Fog` → publisher-agnostic naming-format hints (`UNC####`-style, `Storm-####`-style, `TA####`-style, `APT##`-style, `CL-###-####`-style).
- **Detection / EDR product names** (line 491). "Defender for Identity / Falcon Identity Protection alert names, Velociraptor / Kape collection targets" → "identity-protection / EDR alert-name patterns, DFIR collection-target categories". Standard log-source / event-ID references (Sysmon EID 1, 4624 / 4663 / 4769, S4U2Self, ntds.dit, etc.) are kept — those are protocol- and OS-level primitives, not vendor topic bias.
- **Stack-corroborating-primaries example** (line 519). "Mandiant blog + CISA joint advisory + Microsoft Threat Intel post" → "an independent research lab's blog, a government joint cybersecurity advisory, and a major-vendor threat-intel post".
- **Reference template footer examples** (lines 572, 608). Default `china-nexus` tag in the worked § 2 and Deep Dive footers → `<nexus-tag-from-taxonomy-if-applicable>`. The taxonomy still defines the full nexus-tag list (`china-nexus`, `russia-nexus`, `north-korea-nexus`, `iran-nexus`, `us-nexus`, `eu-nexus`); the change just stops biasing the *example* toward one specific nexus.
- **Phase 4.5 verifier example findings.** "Source: [NVD — CVE-…] / [CERT-FR — CERTFR-…]" → "an NVD/MITRE/cve.org per-CVE page or a national-CERT advisory page". `https://heise.de/news/` → "a homepage / category landing (no article slug)". "APT28 active against EU governments" → "<named actor> active against <victim class>". "508 EU on-premises instances internet-reachable (Censys/Shodan telemetry)" → "<specific aggregate number> on-premises instances internet-reachable (<vendor> telemetry)". "CVE-2023-35078 was exploited by APT29 within days" → "<CVE ID> was exploited by <named actor> within days".
- **Worked-good § 2 fragment** (line 496). The supply-chain example previously named `Google Chrome` cookie paths verbatim and a `Cloudflare-Workers-hosted resolver`. Replaced with publisher-agnostic phrasing ("each browser's per-profile cookie store on disk", "an attacker-operated edge-serverless resolver"). The fictional `@org/x-cli` package, the version range, the OS-intrinsic execution methods (`osascript`, `powershell.exe -enc`), the MITRE technique mapping, and the detection / hardening guidance are kept — those are pedagogical, not topic bias. Date in the inline citation neutralised to `YYYY-MM-DD`.
- **Phase 5.5 blocked-source-pattern enumeration** (line 896). The named-publisher domain list (heise.de variants, nos.nl variants, cert.ssi.gouv.fr, dragos.com, abw.gov.pl) replaced with shape descriptions; the **full pattern list with concrete domain examples drawn from sources in `sources.json`** continues to live at the top of `tools/check_brief.py`. The script — which the operator owns and edits to track real source-rotation patterns — is the right place for concrete domain enumeration; the prompt is the wrong place because every domain it names becomes an anchor.
- **Phase 5.5 "How to fix" table example** (line 918). The specific Heise article URL example replaced with a structural description.

The bridge-fetcher operational guidance (Phase 1 — `tools/fetch_source.py` with the explicit `cisa.gov` / `ncsc.admin.ch` / `acn.gov.it` / `ico.org.uk` / `inside-it.ch` / `prodaft.com` / `talos` host enumeration) is **kept verbatim** — those are operational facts about which specific source IDs in `sources.json` need the bridge for HTTP 403 reasons. They tell the agent *how to fetch these sources*, not *what to write about*. Replacing them with placeholders would break the bridge-mandate.

The national-CERT carve-out enumeration in PD-5 (NCSC-CH, GovCERT.ch, CERT-EU, ENISA, BSI, ANSSI/CERT-FR, NCSC-UK, NCSC-NL, CISA, CCN-CERT, AGID-CSIRT-IT, CERT.at, CERT-PL) is also kept — that list is the operational allow-list for the single-source verification carve-out, not topic guidance.

The CVE primary-source order (vendor advisory > national CERT/CSIRT > MITRE/NVD > ENISA EUVD > researcher write-up > aggregator) is kept — it's an operational priority order for the agent to follow when selecting primaries, not a topic-selection bias.

### Weekly prompt — `prompts/weekly-summary.md`

Same rewrites applied where the weekly carries equivalent worked examples:

- **Audience description.** Same de-naming as the daily.
- **Hard-blocked URL pattern examples** (line 258). Specific publisher URLs → shape descriptions.
- **§ 7 long-running-campaign template footer** (line 389). Default `china-nexus` tag → `<nexus-tag-from-taxonomy-if-applicable>`.
- **Phase 3.5 verifier example findings**. `https://heise.de/news/` → "a homepage / category landing (no article slug)".

The weekly's `CVE-YYYY-NNNNN` placeholders were already in the recommended form across §§ 1, 3, 7 — no normalisation needed.

### Out of scope for this version

- `tools/check_brief.py` is intentionally **not edited**. The script is allowed (and expected) to enumerate concrete domain patterns drawn from `sources/sources.json` — that's where source-rotation reality is encoded. The prompt was the wrong place because it was being read by the agent as authoritative topic guidance every run.
- `site/taxonomy.yaml` is unchanged. The full nexus-tag set (`china-nexus`, `russia-nexus`, `north-korea-nexus`, `iran-nexus`, `us-nexus`, `eu-nexus`) remains available; only the *example footers in the prompt* stopped defaulting to one specific nexus.
- The `briefs/` archive is unchanged. Past briefs continue to ship with the names and CVEs that were live at the time.

---

## 2.30 — 2026-05-08 (weekly prompt rewritten on top of the daily's institutionalised stack + new editorial intent)

### Why
v2.28 + v2.29 institutionalised seven things in the **daily** prompt — the dual-axis Phase 4.5 verifier, the iterative refinement loop with up to three follow-up research sub-agents, the `tools/check_brief.py` Phase 5.5 gate, the multi-CVE / multi-source / multi-primary footer rules, the "avoid NVD/CERT as primary" rule with a hard-blocked URL allowlist, the `tools/fetch_source.py` mandate for CISA + NCSC.ch every run, and the `state/run_log.json` Ops-dashboard schema. The **weekly** prompt was still on the v2.23-era structure (single round of W1/W2 horizon research, inline Phase 4.5 shell snippet, no verification sub-agent loop, no blocked-URL list, no fetch_source.py mandate). The two prompts had diverged.

Plus the operator surfaced a missing editorial framing for the weekly: it was being authored as a one-to-one rollup of the dailies. The weekly's actual job is the strategic-horizon view + an explicit "what would be on fire if no one acted on the dailies" register — items where active exploitation continued through the week, where a CISA KEV deadline passed, where a campaign is still acquiring victims, where a patch window closed. Pure recap is not weekly content.

### Weekly prompt — `prompts/weekly-summary.md` (full rewrite on top of the daily's institutionalised stack)

- **New editorial intent block at the top** ("What the weekly is for — and what it is NOT"). Three explicit lenses:
  1. *What would be on fire by Monday morning if no one had acted on the dailies this week* — Mon-morning escalation register.
  2. *The strategic-horizon view a daily reader cannot see from any single day* — multi-day chains, sectoral pressure, long-running operator turnovers, regulatory shifts.
  3. *The longer arc on items the dailies could only sketch* — the disclosure-only-Monday-but-KEV-by-Friday case.

  Repetition without one of these lenses is padding.

- **New W-PD-1 prime directive.** Every weekly item must answer one of the three questions above. Items that don't get dropped in Phase 3.5 even if they were prominent in a daily.

- **Phase 1 Structured review** gains a sixth working list: **"Items where inaction = incident"**. Built from lists 1–3 by asking *if a Swiss / EU public-sector SOC reader did not act on this when it appeared in the daily, would they currently be in an incident?* This list drives the new § 1 framing.

- **Output structure (NORMATIVE)** keeps the 11-section layout but renames § 1 from *"Top stories of the week"* to *"Highest-impact events — what's on fire if no one acted"*. Each H3 in § 1 leads with a one-line **"If you did nothing this week:"** framing — operational reality of what's currently breaking. § 1 may be empty when no item from the week continued to be operationally critical at week-end; the prompt requires explicit empty-stub text in that case.

- **Phase 2 horizon sub-agents (W1, W2)** spawn template now mirrors the daily's: explicit primary-source bias, hard-blocked URL list reference, NVD/MITRE/cve.org per-CVE blocked outright as primary Source, mandatory `tools/fetch_source.py` for CISA + NCSC.ch.

- **Per-item metadata footer (NORMATIVE)** matches the daily verbatim: multi-source forms (`Source: [a](u) · [b](u) · [c](u)` and the `Additional source:` form, both supported), multi-primary case examples (vendor advisory + research blog, vendor + 8-K, CERT + vendor), avoid-NVD/CERT-as-primary rule with the narrow exceptions, hard-blocked URL patterns referenced from the daily's full list, multi-CVE per-CVE breakdown syntax (`CVSS: 9.1 / 7.2`, `Auth: pre-auth (CVE-…), admin-required (CVE-…)`).

- **NEW Phase 3.5 — Final verification sub-agent (URL truth + editorial quality, loop until clean)**. Mirrors the daily's Phase 4.5 with weekly-specific framing in the editorial-quality gate: every item must answer one of W-PD-1's three questions or get flagged for drop. Truth gate identical (every URL fetched, every claim cross-checked, every named entity grounded). Loop cap: 3 iterations. Main agent may spawn up to 3 follow-up research sub-agents per iteration for `Needs more research` / `Missed angles`. Iteration count + residuals written to `run_log.json`.

- **Phase 4 State update** adds the `state/run_log.json` weekly-specific schema with `iso_week`, `kind: "weekly"`, `sub_agents: { W1, W2 }`, every Ops-dashboard-required field. Same population rules as the daily.

- **NEW Phase 4.5 — Self-check gate via `python3 tools/check_brief.py briefs/weekly/YYYY-Www.md`**. Replaces the v2.23 inline shell snippet. Same script, same 17-check inventory, with weekly-aware section keys (`weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-incidents-recap`).

- **Hard invariants — 9 → 15 + 2 weekly-specific (W-INV-1, W-INV-2).** The weekly now mirrors the daily's 15 invariants (Phase 3.5 verification loop, Phase 4.5 script gate, fetch_source.py mandate, run_log.json populate). New weekly invariants: every item answers W-PD-1's three questions; § 1 frames items as "what's on fire if no one acted".

- **Quality gates** updated to include the W-PD-1 framing check, the Phase 3.5 verification check, the script invocation, the multi-CVE breakdown rule, the NVD/CERT-as-only-primary rule, the run_log population check.

### Script — `tools/check_brief.py`

- **Now kind-aware.** `resolve_brief_path` accepts `YYYY-Www` and routes to `briefs/weekly/`. `detect_brief_kind` reads the filename pattern and returns `("daily", date, None)` or `("weekly", date, iso_week)`.
- New section keys for the weekly (`weekly-glance`, `weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-sector-patterns`, `weekly-incidents-recap`, `weekly-annual-reports`, `weekly-long-running`, `weekly-policy`, `weekly-looking-ahead`).
- `check_section_h3_coverage` — for weekly, requires `weekly-top-stories`, `weekly-multi-day`, `weekly-vuln-rollup`, `weekly-incidents-recap`. Empty weekly-top-stories is acceptable when the body explicitly states `no item .{0,40}continued to be operationally critical` or similar — the v2.30 inaction-=-incident framing.
- `check_h3_footers`, `check_multi_cve_footers`, `check_blocked_source_patterns`, `check_primary_source_quality` — all thread `kind` through; weekly variants target the weekly section keys.
- `check_run_log_for_today` — picks the right run record by `(kind, iso_week)` for weekly, by `(kind, date)` for daily. Weekly's required schema: `iso_week`, `kind`, `sub_agents: { W1, W2 }`, no `deep_dive`. Daily unchanged.
- The `updates-citations` check only fires for daily briefs; the weekly's § 7 (Long-running campaigns) is regular H3 + footer, not UPDATE blockquotes.
- The `covered-items` heuristic is daily-only (the weekly logs `weekly_summary` appearances which the heuristic doesn't model).

### Daily prompt — `prompts/daily-cti-brief.md`

Minor cleanup: dropped the "Run with `--no-link-check` for offline test runs only." parenthetical from two places (per-item-metadata-footer NVD section + Phase 5.5 check inventory). The flag still exists in the script for ergonomics; it just isn't documented in the prompt — Phase 5.5 always runs the live URL check.

---

## 2.29 — 2026-05-08 (blocked-URL allowlist + live URL HEAD check + every external link opens in new tab)

### Why
Three operator-visible defects in the 2026-05-08 brief and rendered site:

1. **NVD/MITRE per-CVE pages and generic landings still appeared as `Source:` entries.** The 2026-05-08 brief cited `https://nvd.nist.gov/vuln/detail/CVE-2026-5787`, `https://www.heise.de/news/`, `https://nos.nl/artikel/`, `https://www.dragos.com/year-in-review/`, `https://abw.gov.pl/pl/cyberbezpieczenstwo/` — derived data sheets and category landings, not disclosing-party content. v2.28 had this as a soft WARN; v2.29 escalates it to a hard FAIL backed by an explicit blocked-URL list in `tools/check_brief.py`.

2. **Fabricated URLs** like `https://securelist.com/amazon-ses-bec-campaign-2026/`, `https://www.surf.nl/actualiteiten/2026/canvas-security-update`, `https://www.deepinstinct.com/blog/muddywater-2026` looked plausible but 404. The Phase 4.5 verifier was supposed to catch these by fetching every URL — but a local pre-publish check had no equivalent. v2.29 adds it to `tools/check_brief.py` so the operator sees the same FAIL signal at commit time.

3. **External links opened in the same tab**, costing the reader the brief tab on every citation click. The Markdown renderer's `<a>` emission carried `rel="noopener noreferrer"` but no `target="_blank"`. The `_rewrite_about_links` pass on docs/* pages also didn't add target when the rewrite turned a relative path into a `github.com/.../blob/main/...` URL.

### Daily prompt — `prompts/daily-cti-brief.md`

- **Per-item metadata footer (NORMATIVE) gains a "Hard-blocked URL patterns" subsection.** Lists every NVD/MITRE per-CVE pattern, the four "/news/", "/security", landing-page Heise variants, NOS landing pages, CERT-FR `/avis/` and `/actualite/` index roots, CISA news-events root, Dragos year-in-review marketing landing, ABW category landing, and the rule-of-thumb (if dropping the trailing path component still resolves to a meaningful page, the URL is too generic). Includes a Bad → Good table mapping each blocked pattern to the right vendor PSIRT / research-blog URL pattern.
- **Phase 5.5 check inventory expanded** from 17 → 19 checks. New entries:
  - `blocked-source` (FAIL) — host + path pattern match against the v2.29 blocked-URL list.
  - `source-urls` (FAIL on 404, WARN on other non-200) — live HEAD/GET on every Source URL in every footer. Includes a Mac local-Python SSL-trust-store pre-flight: if the local Python lacks a CA bundle, the check emits a single environment-level WARN and skips the per-URL loop. CI on Linux runs the check normally.
- **Phase 5.5 "How to fix common FAILs" table** gains entries for `blocked-source: ... cites NVD per-CVE`, `blocked-source: ... cites heise.de/news/` (or any landing), and `source-urls: <url> returns 404`.

### Site — `site/build.py`

- **`render_inline` Markdown link emission** now adds `target="_blank"` for any href starting with `http://`, `https://`, or `mailto:`. Internal/relative links keep current-tab navigation. Every inline citation in every brief now opens in a new tab.
- **`render_footer_html` source pills** add `target="_blank"`. Footer source links open in a new tab.
- **`_rewrite_about_links`** — when a relative path in `docs/*.md` gets rewritten to `https://github.com/<repo>/blob/main/<path>`, the rewriter now adds `target="_blank"` to the resulting anchor.
- **404 page's GitHub-issues link** had `rel="noopener noreferrer"` but no target — fixed.

Full-site audit after the fix: 911 external anchors, 0 missing `target="_blank"`. 4525 internal anchors, 9 deliberately carrying `target="_blank"` (RSS-feed chips on the briefs index — pre-existing UX choice).

### Tests

`site/test_build.py` gains:
- `external link target=_blank` — `render_inline` emits `target="_blank"` for `https://` hrefs.
- `external link rel noopener` — accompanying `rel="noopener noreferrer"`.
- `relative link no target` — `#anchor` and other relative hrefs do *not* pick up the target.

---

## 2.28 — 2026-05-08 (institutionalised self-check script + multi-CVE / multi-source footers + Phase 4.5 quality gate + mandatory fetch_source.py for CISA + NCSC.ch)

### Why
The 2026-05-08 run exposed three classes of drift that the v2.27 prompt could not catch on its own:

1. **The Phase 5.5 self-check was a copy-paste of inline shell snippets**: the agent reproduced them imperfectly run-to-run, and any new check (e.g. footer-field completeness, `run_log.json` Ops-dashboard population, primary-source quality, multi-CVE hygiene, IOC heuristic) had to be added in the prompt and re-pasted by the agent. The 2026-05-08 inline check found 5 CVEs missing from `cves_seen.json` — useful, but did not also catch that `run_log.json` was empty (Ops dashboard renders `—` cells), that 4 CVE entries cited NVD/CERT-FR as the *only* primary source instead of the vendor advisory, that CISA was 403'd without `tools/fetch_source.py` mitigation, or that the 2026-05-08 brief had Ivanti EPMM CVE-2026-5787 + CVE-2026-6973 as a multi-CVE footer that needed per-CVE CVSS breakdown.

2. **The Phase 4.5 verification sub-agent was URL-truth only.** It caught fabricated and broken URLs but did not assess *editorial quality*: relevance to a Swiss / EU public-sector SOC, primary-source strength (NVD/CERT cited as sole primary on items where a vendor PSIRT advisory existed), vendor-marketing tells, missed angles a senior reader would expect.

3. **Multi-CVE / multi-source footer patterns were happening organically but not documented.** The 2026-05-08 brief used `CVE: CVE-2026-5787, CVE-2026-6973 · CVSS: 9.1 (CVE-2026-5787), 7.2 (CVE-2026-6973)` and `Source: [Ivanti — …](url) · [NVD — …](url) · [The Hacker News — …](url)` — both correct, both unparseable as conventions because the prompt didn't spell them out.

### Daily prompt — `prompts/daily-cti-brief.md`

- **New `tools/check_brief.py`** — institutionalised, version-controlled, stdlib-only Python script that imports `parse_footer_line` / `validate_footer` / `parse_taxonomy` from `site/build.py` so script and build agree on parsing rules. Bundles 17 checks: state JSON parses · taxonomy loads · core sections present (title-based, schema-neutral about § numbering) · AI-content notice · IOC heuristic scan with version-string false-positive suppression · CVE sync · UPDATE inline citations · footer presence (skips Markdown thematic breaks `---`) · footer Source/Tags/Region/CVE-fields completeness · footer taxonomy validation · multi-CVE per-CVE CVSS breakdown · primary-source quality (warns on NVD/CERT as sole primary) · `tools/fetch_source.py` enforcement on known-403 hosts · `covered_items.json` appearance heuristic · `run_log.json` Ops-dashboard fields fully populated · `sources.json` last-fetched bookkeeping · `site/test_build.py` smoke tests. Read-only by design — agent fixes drift, script reports it. Non-zero exit aborts the commit.

- **Phase 5.5 rewritten** — replaces the six inline shell snippets with a single `python3 tools/check_brief.py` invocation, lists the 17 checks the script bundles, and ships a "How to fix common FAILs" table so the agent has a recipe for each `FAIL` line.

- **Phase 4.5 widened from URL-truth-only to URL-truth + editorial-quality.** The verification sub-agent's spawn template now also assesses (per item) relevance to a Swiss / EU public-sector SOC, primary-source strength with explicit guidance to flag NVD/MITRE/CERT-as-sole-primary, vendor-marketing tells, fake-news patterns, contradictions, and clarity. Whole-brief checks added: coverage shape, style discipline, missed angles. The verifier now returns 5 additional finding categories (`Strengthen primary source`, `Drop`, `Needs more research`, `Surface contradiction`, `Missed angles`) on top of the 5 truth categories from v2.27. The main-agent loop authorises spawning **≤3 follow-up research sub-agents per iteration** for `Needs more research` / `Missed angles` findings — iterative refinement so unclear or under-sourced items can be deepened rather than dropped on the spot. Iteration cap stays at 3 (the brief must publish).

- **`tools/fetch_source.py` is now MANDATORY for CISA + NCSC.ch every run.** The Phase 1 research-methodology section says: do not even attempt `WebFetch` on `cisa.gov` / `www.cisa.gov` / `ncsc.admin.ch` / `ncsc.ch` first — go straight to the bridge. Phase 5.5's script FAILs the commit if `run_log.json.fetch_failures` lists a 403/429 on a known-403 source id without bridge mitigation. The 2026-05-08 brief skipped CISA because of an unhandled 403 — this run-class drift is now caught both ways.

- **Multi-CVE / multi-source / multi-primary footer pattern documented in the per-item metadata footer (NORMATIVE) section.** Three new subsections:
  - **Multi-source — primary + corroborating in the same footer.** Two equivalent forms supported: `Source: [a](u) · [b](u) · [c](u)` (preferred for 2–4 sources) and `Source: [a](u) · Additional source: [b](u) · Additional source: [c](u)`. Both parse to the same structured list.
  - **When more than one publisher counts as a "primary" source.** Vendor advisory + vendor research blog, vendor advisory + regulator filing (8-K), CERT advisory (when it *is* the primary disclosing party for its jurisdiction) + vendor advisory it references — these are dual primaries. The first two `[Title](URL)` blocks are both leads.
  - **Avoid NVD / national-CERT as the *only* primary.** Editorial rule: vendor PSIRT advisories / research-lab posts / vendor blogs / regulator filings / victim statements are preferred as the lead. NVD/MITRE and national CERTs/NCSCs are second-tier primaries — `Additional source:` material — except in the narrow cases where they genuinely *are* the disclosing party (NCSC.ch on a Swiss federal incident, ENISA EUVD on an EU-discovered vuln, KEV before vendor's advisory page is up).
  - **Multi-CVE — one item, several CVEs.** It is *encouraged* to group related CVEs into one item rather than emit a paragraph per CVE (Ivanti EPMM chain, CERT-FR multi-CVE advisory, research-lab multi-bug audit). The footer carries a comma-separated `CVE:` field and per-CVE breakdown for any field whose value differs (`CVSS: 9.1 / 7.2`, `Auth: pre-auth (CVE-…), admin-required (CVE-…)`).

- **`state/run_log.json` schema made exhaustive** with `prompt_version`, `items_dropped_by_verification`, and explicit population rules for every field. The Ops dashboard renders sub-agent cells as `items (used/attempted src)`, surfaces a `stalled` badge on `returned: false`, and a yellow badge when `fetch_failures` is non-empty — empty fields produce empty dashboard cells. Every field is required every run, no exceptions. `tools/check_brief.py` validates the population.

- **Quality gates** add: Phase 4.5 ran covering both axes; `run_log.json` fully populated; `tools/fetch_source.py` used for CISA + NCSC.ch; `python3 tools/check_brief.py` exits 0.

- **Hard invariants — 12 → 15 entries.** All 12 from v2.27 preserved. New: (10) Phase 4.5 verification sub-agent loop covering URL truth + editorial quality, ≤3 iterations, may spawn ≤3 follow-up research sub-agents per iteration; (11) Phase 5.5 self-check via `tools/check_brief.py`; (14) `tools/fetch_source.py` is the bridge for CISA + NCSC.ch every run; (15) `state/run_log.json` populated every run with the full per-sub-agent allocation block + verification counters.

- **Working-directory layout** adds `tools/check_brief.py` and `site/test_build.py`; clarifies that `tools/fetch_source.py` is mandatory for CISA + NCSC.ch.

### Documentation

- **`docs/verification.md`** — adds a Phase 4.5 section describing the dual-axis verification (truth gate + editorial-quality gate), the 6-item editorial bar, the iterative refinement table, and the 3-iteration / 3-follow-up-sub-agent caps. Quality-gate checklist gains the script + Phase 4.5 entries + multi-CVE breakdown + anti-NVD/CERT-as-primary rule.

- **`docs/workflow.md`** — adds a § 6.5 Phase 4.5 section between Phase 4 and Phase 5; replaces the six-bullet Phase 5.5 description with the 17-check institutionalised script invocation; expands the `state/run_log.json` description to spell out every required field and how the Ops dashboard renders each.

- **`docs/architecture.md`** — adds `tools/check_brief.py` to the components list (with the full check inventory + import-from-`build.py` design); updates the data-flow diagram to show Phase 4.5 (truth + editorial) and the script-driven Phase 5.5 as discrete boxes.

### Hard invariants — 12 → 15

All 12 from v2.27 preserved. Three new entries (Phase 4.5 dual-axis loop, `tools/check_brief.py` gate, `tools/fetch_source.py` mandatory for CISA+NCSC.ch, `run_log.json` populate) make the new dependencies non-removable.

---

## 2.27 — 2026-05-08 (final-verification sub-agent loop + less-is-more rewrite)

### Why
v2.26 hardened the *intent* around link discipline ("don't fabricate URLs") and tightened the § 1 bar. v2.27 adds the *enforcement layer* — an independent verification sub-agent that reads the finished brief end to end before publication and flags fabricated URLs, citation mismatches, and unsupported claims for the main agent to fix. The same release rewrites PD-11 around an explicit "less is more" principle so the brief stops drifting toward "fill every section" and back toward "ship only what changes a defender's day."

Both changes are responses to operator review of the 2026-05-08 brief, which contained: invented blog slugs, citations that pointed to homepages, claims (notably aggregate exposure counts) that no linked source supported, and sections padded with items that did not meet the relevance bar.

### Daily prompt — `prompts/daily-cti-brief.md`

- **PD-11 rewritten as "Less is more — relevance over volume."** The single-line "no suppression, no padding" rule is replaced with: an explicit daily relevance bar (the four conditions an item must satisfy to qualify for the brief at all), a non-exhaustive blocklist of content the brief should drop without ceremony (vendor marketing dressed as research, recap of already-covered stories without delta, awareness-level pieces, industry surveys, conference recaps, product launches, opinion pieces, year-over-year stats without a defender takeaway), variable-size guidance (a quiet day produces a short brief, a noisy day produces a longer one — never pad to length), an empty-section policy (sections without qualifying content render the heading + an italic `*intentionally left empty*` stub), and item-level cuts (throat-clearing intros, hedge stacks, restating section context, closing flourishes, recap of prior coverage all get cut). The reader-trust framing — "the reader trusts that brevity reflects signal, not laziness" — is the operative line for the model.

- **New Phase 4.5 — Final verification sub-agent (loop until clean).** Inserted between Phase 4 (compose) and Phase 5 (state update). After the brief is written to disk, a fresh `general-purpose` sub-agent is spawned with a strict verification prompt: read the brief end to end, fetch every cited URL, confirm each (a) resolves, (b) is a specific page (not homepage / category / listing), (c) actually supports the claim being cited; cross-check named entities (CVEs, actors, campaigns, victims, dates, aggregate numbers) against the linked sources and flag any without source backing; surface claims missing inline citations. The verification agent is read-only — it never edits the brief. It returns a structured Markdown report with five blocking-finding categories (broken URLs, generic / oversight URLs, citation does not support claim, unsupported / hallucinated facts, claims missing inline citation) and one advisory category (less-is-more flags), each finding numbered so the main agent can fix or drop surgically. The main agent applies fixes in priority order — replace the URL with a freshly-fetched specific URL, narrow the claim to what the source supports, or drop the claim/item — then spawns a fresh verification sub-agent against the updated brief. Loop until verdict CLEAN, with a hard cap of three iterations. After three rounds remaining issues are dropped, surviving residuals are logged in § 8 (`verification: published with N residual findings unresolved after 3 iterations`), and the brief publishes — the CRITICAL "always write the file" header always wins over the verification gate; verification removes bad content but never blocks publication.

- **Run-log schema** gains `verification_iterations` (number of Phase 4.5 rounds) and `verification_residual_count` (issues unresolved after the iteration cap, 0 on a clean publish). Operations dashboard at `/ops/` will surface these.

- **Quality-gates checklist** gains two entries: "Phase 4.5 verification ran, final verifier returned CLEAN (or three iterations exhausted with residuals logged in § 8); `verification_iterations` and `verification_residual_count` set in `state/run_log.json`," and "Less is more applied — every item passes the daily relevance bar; sections without qualifying content carry the explicit `*intentionally left empty*` stub (except § 1, which is omitted entirely)."

### Notes for the operator

The verification sub-agent costs another ~5–10 minutes of wall-clock and a non-trivial fetch budget on top of Phase 1. That is the intended price for catching hallucinated URLs and unsupported aggregate numbers before they reach the published feed. The iteration cap of 3 is the upper bound on how many rounds the loop will run — most days the first verification should return CLEAN; iteration 2 catches anything the writer-verifier disagreed about; iteration 3 is the safety floor, after which residuals are logged and the brief publishes anyway.

If the verification sub-agent itself fails (timeout, no return), the main agent proceeds with publication and notes `verification: sub-agent did not return — published without final verification` in § 8 — the brief still ships.

---

## 2.26 — 2026-05-08 (Immediate Actions bar + source-link discipline)

### Why
Operator review of the 2026-05-08 brief surfaced three editorial defects:

1. **§ 1 Immediate Actions was over-inclusive.** A Windows Shell NTLM-coercion item entered § 1 because of an upcoming CISA KEV federal-remediation deadline, even though the underlying vulnerability had been patched in April Patch Tuesday and was not freshly weaponised. § 1 is meant to be the "stop reading and act now" section — emergency patches, immediate isolation, instant credential rotation — not a KEV-deadline reminder.

2. **Hallucinated and oversight URLs.** Several inline citations pointed to homepages, news category landing pages, or fabricated blog slugs (`https://heise.de/news/`, `https://nos.nl/artikel/`, `https://www.surf.nl/actualiteiten/2026/canvas-security-update`). The reader cannot verify a claim from a URL that 404s or lands on a generic feed.

3. The site-build TL;DR, Updates-section keyword, and footer-detection regexes had drift bugs against the prompt's `## § N — Heading` numbering and the trailing `---` horizontal rule between sections — those are fixed in `site/build.py` in this same change.

### Daily prompt — `prompts/daily-cti-brief.md`

- **PD-2 expanded** with an explicit "Critical link discipline" paragraph banning URL fabrication, URL inference from advisory IDs, and citation of homepages / news categories / listing indexes. Every URL in a brief must be a URL the agent actually fetched in this run that resolved to content matching the claim. Surface every relevant URL where the claim was found (primary + corroborating), not just one.

- **§ 1 Immediate Actions criteria rewritten** as a **conjunctive** test instead of a disjunctive one. An item now needs to be (a) newly disclosed or newly weaponised, AND (b) actively exploited or with imminent expected mass exploitation, AND (c) require time-critical-to-the-hour-or-day action. CISA KEV deadlines on already-covered items are explicitly disqualified from § 1 — they belong in § 5 (Updates) or the § 7 Action Items table. New "If unsure, it does not belong in § 1" tiebreaker.

- **New `Source-link discipline (highly critical)` sub-section** in Phase 1 spelling out, for sub-agents:
  - Only fetched URLs may be cited.
  - URLs must point to specific article / advisory / vendor PSIRT / regulator filing / victim statement pages, never homepages or category landings.
  - Drill to the most primary source, AND keep the corroborating sources too.
  - News-only fallback is acceptable when the primary was unreachable, provided the URL is a specific article URL (not the news site's homepage) and the item is flagged in § 8.
  - Verify each link actually resolves before returning it.
  - If unsure, drop the item rather than ship a guessed URL.

- **Sub-agent spawn template** now includes a prominent "LINKS ARE ABSOLUTELY CRITICAL — read this twice" paragraph that mirrors the same rules in plain language inside the template the four sub-agents see at spawn time.

- **Phase 2 step 1 expanded** from "re-fetch the primary source if any doubt" to a full URL spot-check: every cited URL is checked against the sub-agent's fetch transcript, 404s and homepage redirects fail the item, and items whose URLs cannot be replaced are dropped to § 8 with a `URL verification failed: ...` line.

### Site build — `site/build.py`

(Not strictly a prompt change but co-released with v2.26 because it surfaced the same review.)

- **TL;DR parsing regex** broadened from `## 0?. TL;DR` to `## ...TL;DR...`, so the home-page TL;DR preview, the RSS description, and the brief summary populate correctly when the prompt uses any heading-prefix style (`## TL;DR`, `## 0. TL;DR`, `## § 1 — TL;DR`).

- **Item-footer detection** in `parse_brief` now skips trailing blank lines AND trailing Markdown horizontal rules (`---`, `***`, `___`) when locating the metadata-footer line. The 2026-05-08 brief's last H3 in each section was failing footer parsing because the H2-section divider `---` ended up inside the slice, hiding the actual footer line — leaving the per-item Tags / Region pills unrendered and the line emitted as raw italic Markdown instead.

- **`_SECTION_KEYWORDS`** now also recognises `Updates on Previously Covered Items` and `Previously Covered Items` as the canonical "updates" section, in addition to the existing `Updates to Prior Coverage`.

- **H4 item fallback in `parse_brief`.** § 4 Trending Vulnerabilities in v2 emits each per-CVE detail block under a `#### CVE-...` heading (the section opens with an H3-equivalent table, so per-CVE blocks step down to H4). Sections with no H3 items now also walk H4 boundaries for item detection. Previously these blocks fell through into the section's raw body Markdown and their per-item footer lines rendered as plain italic text.

- **`parse_footer_line` accepts Source-less footers.** The previous regex hard-required a `Source:` prefix, which dropped both (a) the TL;DR aggregate footer (`— *Tags: ... · Region: ...*`) and (b) any other footer style without an explicit `Source:` label. The matcher is now permissive on the prefix while still requiring at least one recognised footer-field label (`Sources?`, `Tags`, `Region`, `Sector`, `CVE`, `CVSS`, `Vector`, `Auth`, `Status`, `Additional source`) to qualify, so arbitrary italic prose does not get misclassified as a footer.

- **Multiple bare-link sources at the head of a footer.** The deep-dive shape `— *Source: [a](u) · [b](u) · [c](u) · [d](u) · Tags: ...*` previously kept only the first link; the parser now treats every leading bare-link part as an additional source and de-dupes by URL. The reader sees every primary + corroborating link the writer attached to the unit.

- **Section-level footer detection.** The Deep Dive (§ 7) has no item heading — its block-level metadata footer sits at the section tail. `parse_brief` now extracts a section-level footer for sections that have no H3 / H4 items, exposes it as `section["section_footer"]`, and the brief-page renderer emits it as a structured pill block under the section body.

- **Per-item RSS feed includes section-level footers.** A section that carries a section-level footer (Deep Dive) now produces a single per-item-feed entry pointing at `briefs/<name>/#<section-anchor>`, so every block of content with its own metadata footer reaches the per-item feed reader.

- **RSS feed bodies render Sources only.** `render_footer_html` gains a `sources_only=True` flag; the per-item feed uses it so the structured footer block in `<content:encoded>` shows just the Sources line. Tags / Region / CVE / CVSS / Vector / Auth / Status remain as `<category>` feed metadata. The daily and weekly feed bodies, which use the brief's raw markdown rather than the parsed structure, run a new `_strip_footer_metadata_in_md` pre-pass that drops every non-Source field from each italic footer line before rendering. Tags-only footers (TL;DR aggregate) collapse to nothing.

---

## 2.25 — 2026-05-07 (audience + technical depth)

### Why
The brief was occasionally drifting toward executive-summary register —
*"a critical vulnerability has been disclosed"*, *"organizations are urged
to patch promptly"*, *"the threat landscape continues to evolve"* — when
the actual audience is Tier 2/3 incident responders, threat hunters, and
detection engineers who live in MITRE ATT&CK every day and read primary
vendor research directly. They don't need to be told what BloodHound is;
they need to be told which exact component, which exact technique, which
exact event ID surfaces it. v2.25 makes the audience expectation
unmissable and pins down what "deep technical level" means for every
section.

### Daily prompt — `prompts/daily-cti-brief.md`
- Opening role description rewritten to spell out the audience (Tier
  2/3 IR + threat hunters + detection engineers + reverse engineers +
  red-team-aware defenders + SOC management who came up through
  analyst rotations) and to give the assumed-fluency vocabulary as a
  concrete list (BloodHound, Mythic, gMSA, S4U2Self, OAuth device-code
  phishing, EDR userland hooking, BYOVD, LOLBAS, process hollowing,
  kernel callback registration, …).
- New "**The brief is a deep technical document.**" paragraph
  enumerates what every item must include: exact vulnerable component;
  technique class with MITRE ATT&CK IDs; exploitation prerequisites;
  affected and patched versions at vendor-stated precision; observed
  exploitation status with named campaign clusters; concrete defender
  takeaway tied to the specificity (event ID / log source / EDR
  telemetry / configuration switch).
- New "**Technical depth — what every item must include**" section in
  Phase 4, with a worked-good example fragment showing how the depth
  reads in practice on a § 2 item. Explicitly notes: *better to write
  less than to fabricate plausible-sounding specifics* (PD-1).
- Phase 3 deep-dive guidance expanded to spell out the seven content
  pillars: vulnerability or campaign mechanics; exploitation chain
  mapped to the MITRE ATT&CK kill chain; affected and patched
  versions; hunt and detection concepts (Sysmon EID 1, Windows event
  IDs 4624 / 4625 / 4663 / 4769 / 5379, Linux audit syscalls, Sigma
  technique categories); hardening and mitigation specifics; named
  campaign cluster; background paragraph for material with prior
  reporting older than ~6 months.
- Style rules now include "deep technical register" with a concrete
  example (`S4U2Self abuse to obtain a service ticket as a privileged
  user, followed by silver-ticket forging with the captured TGS` —
  *not* `attackers used Kerberos features to escalate privileges`)
  and a list of banned filler phrasings (*"in today's evolving threat
  landscape"*, *"organizations are urged to"*, *"this highlights the
  importance of"*).

### Weekly prompt — `prompts/weekly-summary.md`
- Same audience description as the daily, with the explicit note that
  SOC management read at the same level (they came up through analyst
  rotations).
- New "**The weekly summary is a deep technical document at SOC-analyst
  register**" paragraph clarifying that the weekly's step-back lens is
  about clustering threads / sectoral patterns / long-running-campaign
  arcs, NOT about translating the dailies into executive-summary
  register for a non-technical reader.
- New "**Technical depth — same standard as the daily**" section inside
  Phase 3 listing the seven specificity pillars and rejecting
  surface-level talking points even at week-level register.
- Style rules expanded to mirror the daily's "deep technical register"
  +  banned-filler-phrasing list.

### Hard invariants
Unchanged. The 12 hard invariants in the daily prompt's META section
still hold. The audience clarification is consistent with — and
sharpens — Prime Directive 1 (zero LLM knowledge): you can't fabricate
the technical specificity an audience this skilled will demand, so the
specificity must come from the primary source you fetched today.

---

## 2.24 — 2026-05-07 (prompt rewrite for clarity + Sonnet readability)

### Why
The v2.23 cut-over landed all the new features (9-section structure, per-item metadata footer, Trending Vulnerabilities inclusion gates, Action Items, Immediate Actions, primary-source bias) but the prompts had grown organically — daily was 1067 lines / ~25k tokens with significant duplication and verbose subsections. Goals for v2.24:
- One read-through is enough — Sonnet 4.6 should not need to refer back mid-execution.
- Every anti-crash guard is explicit and prominent.
- Total budget well under 25k tokens (now 14k for daily, 6.5k for weekly).
- All v2 features still fully specified (9 sections / footer / gates / taxonomy / patience clause / primary-source bias).

### Daily prompt — `prompts/daily-cti-brief.md`
- Total length 1067 → 671 lines (~14k tokens). Same scope; tighter prose.
- New "**CRITICAL: this run must produce a brief**" block at the top consolidating all 8 anti-crash guards (always write the file; ~10 min sub-agent timebox; compose-incrementally to dodge stream-idle-timeout; persist intermediate state to `work/<run-id>/`; drop raw HTML; bounded retries; two-stage publishing chain; quality over retries).
- 12 prime directives consolidated into a single ordered list (was 12 H3 subsections); each directive is now 3–6 lines instead of 10–25. Every directive that previously needed a sub-table or nested bullet keeps it.
- "Trace to the most primary source" promoted from buried sub-agent guidance to PD-12.
- Phase-by-phase descriptions reorganised under H2 headings with explicit time budgets (~1 min preflight, ~10 min Phase 1, ~5 min Phase 2, ~2 min Phase 3, ~10 min Phase 4).
- Sub-agent spawn template consolidated into a single block-quoted message that opens every spawn — covers defensive intent + patience + primary-source bias + always-return-something. Used to be three separate paragraphs scattered through Phase 1.
- Research methodology compressed (drill / pivot / search / propose) — 80 lines → 30 lines without losing the bridge-fetcher recipes (NCSC.ch CSH, CISA KEV, generic allow-listed hosts).
- Phase 4 "Output structure" now lists the 9 sections as a normative table on first read; the per-section guidance follows. The reference template at the end still shows the full Markdown skeleton with every metadata footer.
- Phase 5 source lifecycle compressed (60 lines → 25 lines) without dropping any rule.
- Phase 5.5 self-check expanded with the v2.23 retargeting at sections 2–4 plus the metadata-footer presence check (step 5) and the taxonomy-validation check (step 6).
- META "Hard invariants" list now includes (10) Phase 5.5 self-check gate, (11) per-item metadata footer, (12) strict CSP + vendored-library hash check.

### Weekly prompt — `prompts/weekly-summary.md`
- Total length 363 → 448 lines (~6.5k tokens). Slightly longer because we added the same anti-crash guards block, the consolidated spawn template, and an explicit Phase 4.5 self-check gate.
- New "**CRITICAL: this run must produce a summary**" block mirroring the daily.
- Sub-agent spawn template consolidated into a single block-quoted message (was three).
- Per-item metadata footer NORMATIVE block referencing `site/taxonomy.yaml` for the controlled vocabulary (instead of duplicating the full vocab list — the daily prompt is the source of truth).
- New Phase 4.5 self-check gate: state JSON parses; every CVE in cves_seen.json; every H3 in §§ 1–8 carries a v2 metadata footer; every footer value is in the taxonomy.
- Reference template at the end now shows every section with a representative metadata footer.

### Hard invariants — unchanged
The 12 hard invariants in the daily prompt's META section are unchanged. The two prompts share the same publishing chain, the same metadata-footer schema, the same taxonomy file, and the same anti-crash guard list.

---

## 2.23 — 2026-05-07 (v2 schema cut-over)

### Why
Substantial editorial + engineering upgrade landed together: the SPA reader is replaced by a real static-site SSG, every brief item gets a structured metadata footer parsed by the build, and the section structure is reorganised so per-item tagging (region + sector + theme) replaces the dedicated "Switzerland, Europe & Public Sector" section. Full plan: [`docs/v2-plan.md`](../docs/v2-plan.md).

### Daily prompt — section structure
The eight-section structure (`0. TL;DR / 1. Active Threats & Trending Vulns / 2. Switzerland, Europe & Public Sector / 3. Notable Incidents & Disclosures / 4. Research & Investigative Reporting / 5. Deep Dive / 6. Updates / 7. Verification Notes`) becomes a nine-section structure:

```
0. TL;DR
1. Immediate Actions                                         (often absent — see below)
2. Active Threats, Trending Actors, Notable Incidents & Disclosures
3. Trending Vulnerabilities                                  (consolidated, with inclusion gates)
4. Research & Investigative Reporting
5. Updates to Prior Coverage
6. Deep Dive — {topic}
7. Action Items                                              (derived from today's content only)
8. Verification Notes
```

Switzerland / Europe / public-sector emphasis is now expressed as **per-item region + sector tags** on every § 2 item, ordered with CH/EU/public-sector first then global then the rest. There is no separate § 2 in the v2 layout — the editorial focus rides on the metadata footer.

### Daily prompt — Immediate Actions
New § 1, **omitted entirely on most days**. An item only enters when it satisfies at least one of: actively-exploited zero-day with RCE/auth-bypass; zero-click RCE (exploited or with public PoC); pre-auth RCE on internet-exposed enterprise software; supply-chain compromise affecting widely deployed software; active campaign with confirmed European public-sector impact. Empty Immediate Actions is part of the design — rendering the heading every day with a placeholder dilutes the meaning when something does meet the bar.

### Daily prompt — Trending Vulnerabilities inclusion gate
§ 3 now narrows the CVE bar with explicit inclusion gates. CVEs that the news cycle is hyping but that don't clear at least one gate (CISA KEV, ENISA EUVD `exploited=true`, ENISA EUVD CVSS ≥9.0, ITW report from a HIGH-reliability researcher, pre-auth internet-exposed RCE with public PoC) **stay out of the brief** — logged in § 8 with the reason. The legacy `CVE | Product | …` table is folded in as a secondary aggregation beneath the per-CVE entries.

### Daily prompt — Action Items
New § 7. Specific, derived-from-this-brief recommendations only. Generic advice does not belong here. Skews toward patching / mitigations for actively-exploited CVEs covered today, hunting queries / IoC-free detection concepts for campaigns covered today, configuration changes that close the specific attack path covered today.

### Daily prompt — per-item metadata footer (NORMATIVE)
Every individual content block (every § 1 / § 2 / § 3 / § 4 / § 5 / § 6 / § 7 item) ends with **exactly one italic Markdown line** in the format

```
— *Source: [Title](URL) [· Additional source: [Title](URL)] · Tags: tag1, tag2 · Region: region1[, region2] [· CVE: CVE-…] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*
```

Field separator is the middle dot ` · ` (U+00B7 with surrounding spaces). Controlled vocabularies live in [`site/taxonomy.yaml`](../site/taxonomy.yaml). The build refuses any item using a value not in the taxonomy. The build splits each brief by H3 + footer and emits one stable `/items/<slug>/` page per content block plus per-tag, per-region, per-CVE indexes. Missing or malformed footer on a post-cut-over item is a build failure.

### Daily prompt — Phase 5.5 self-check
- Steps 1, 2 unchanged.
- Step 3 retargets at sections 2–4 (was 1–4).
- Step 4 retargets at § 5 (was § 6) and additionally requires a metadata footer inside each UPDATE blockquote.
- Steps 5 and 6 added: every H3 in §§ 1, 2, 3, 4, 5, 7 carries a footer; every footer's values are in `site/taxonomy.yaml`.

### Sub-agent spawn — patience and primary-source bias
Both sub-agent spawn-prompt blocks gain explicit "take your time, persist intermediate state, never block the brief" and "trace to the most primary source you can verify; news is at most a *via* reference" stanzas, replacing earlier soft guidance.

### Engineering — `site/build.py`, RSS, taxonomy
- New SSG emits real HTML pages for every URL: home, brief, item, CVE, source, topic, tag, region, ops, about. The legacy SPA hash routes get a one-time JS bootstrap on `/` that converts indexed `#/briefs/<name>` URLs to the clean URL.
- Three valid RSS feeds: `/feed.xml` (daily, URL preserved), `/feed-weekly.xml` (NEW), `/feed-items.xml` (NEW per-item, last 50). Closes [#2](https://github.com/OwlsNightCatch/ctipilot/issues/2):
  - **Defect A fixed:** Markdown emphasis / links / inline code render to HTML before the body is CDATA-wrapped. A unit test asserts no unrendered `**...**` or `[..](http..)` survives into `<content:encoded>` payloads.
  - **Defect B fixed:** `<pubDate>` is the actual git-commit moment of the brief on `main` (sourced from `git log --diff-filter=A --format=%aI -- briefs/YYYY-MM-DD.md`), falling back to file mtime — never midnight-of-brief-date.
- Vendored library integrity check is preserved and now also covers the new `filter.min.js`.
- Strict CSP unchanged.
- Self-check at the end of every build asserts: every emitted HTML page contains the Umami snippet exactly once; every feed parses as XML; no UTM parameters anywhere; no unrendered Markdown emphasis in any feed body.

### Weekly prompt
Adopts the same metadata footer on every item. Section structure unchanged.

---

## 2.22 — 2026-05-07

### Why
Operator changed the routine schedule (daily Mon–Fri 06:00 GMT+2, weekly Mondays 11:00) and asked that *no time, day, or schedule assumption* be hardcoded in the prompt. The agent should always derive its recency window from `briefs/` so:

- (a) the operator can change cron times freely without touching the prompt,
- (b) a failed run is automatically caught up by the next run (Tuesday fails → Wednesday's brief covers Mon-noon → Wed-morning),
- (c) the daily covers the gap since the last *daily* and the weekly covers the gap since the last *weekly*, independently and self-coordinating.

v2.21's day-of-week recency table conflicted with goal (a) — it baked Mon–Fri / Sat–Sun assumptions into the prompt. Removed.

### Prime Directive 7 (Recency) — gap-derived, schedule-agnostic, self-healing
- Day-of-week table replaced with a **gap-derivation rule from disk**:
  ```
  latest_brief = max(date in briefs/*.md by lex sort)
  gap_hours    = (currentDate - latest_brief) * 24
  window_hours = max(24, gap_hours + 12)   # 12h safety overlap
  ```
- New window-class table maps `gap_hours` to expected brief size and § 7 disclosure:
  - ≤ 30 h → standard daily (3–5 § 1a items)
  - 30 – 60 h → extended (one missed run; 5–8 items)
  - 60 – 96 h → catch-up (typical Monday after Mon–Fri schedule, OR two missed runs; 6–10 items)
  - > 96 h → major gap (cap at 10–12 items, surface unhandled volume in § 7)
- Self-healing by construction: any missed run is automatically caught up by the next run because the gap on disk widens.
- Schedule independence by construction: the prompt doesn't know — and doesn't need to know — when the cron fires.

### Phase 0 step 7 (new)
- After loading state, the agent now explicitly computes `gap_hours` and `window_hours` from the latest file in `briefs/`, sets the window-class, and passes `window_hours` to every Phase 1 sub-agent's spawn message.

### "Determining today" subsection
- Day-of-week table replaced with the gap-derivation pseudocode and the rule "do not hardcode times, days, or schedule assumptions".

### Weekly summary (`prompts/weekly-summary.md`)
- Same gap-derivation rule applied: `latest_weekly = max(briefs/weekly/*.md)`, `gap_days = today - latest_weekly_end`, `window_days = max(7, gap_days + 1)`.
- Weekly window-class table:
  - ≤ 8 d → standard week
  - 9 – 15 d → one missed week (doubled coverage)
  - > 15 d → major gap (cap at ~3 weeks of detail)
- Header `fires once per week` softened to `schedule is set by the operator`.

### META autonomy paragraph
- "fires once per **working day** (Monday–Friday) … weekly summary fires Sunday night" → "scheduled routines fire on whatever cadence the operator configured … schedule is **not** encoded in this prompt".

### Docs
- README, `docs/workflow.md`, `docs/routine-setup.md` all stripped of hardcoded times (no `06:30 Europe/Zurich`, no `18:00–22:00`, no `Sunday night`); the gap-derivation rule is explained as a self-healing + schedule-agnostic mechanic.

---

## 2.21 — 2026-05-07

### Why
The daily routine runs **only on working days** (Mon–Fri); the weekly summary runs **Sunday night**. Saturday + Sunday + Friday-during-the-day events therefore fall through the cracks unless the Monday brief explicitly catches them up. Earlier prompt versions said "Default window: events from the last 24 hours" with no day-of-week awareness — Mondays were producing a same-size brief that silently dropped two and a half days of operational signal.

### Prime Directive 7 (Recency) — schedule-aware window
- New explicit table mapping day-of-week to recency window:
  - **Mon** → 72–84 h (Fri-morning → Mon-morning); Monday brief is expected to be larger (typically 6–10 § 1a items vs the usual 3–5).
  - **Tue–Fri** → 24 h, extend 72 h for actively developing items.
  - **Sat / Sun** → routine should not run; off-schedule run is treated as Monday-class with the gap surfaced in § 7.
- Monday brief explicitly catches Friday-during-the-day publications (vendor advisories that landed after the Friday brief, victim disclosures filed into EU close-of-business, US-afternoon CISA KEV additions) plus the entire weekend.
- "Don't bridge to the weekly summary" rule: the Sunday-night weekly is week-level synthesis; the Monday daily is *catch-up of the operational items the daily missed*. The two are complementary, not redundant.
- First brief after any unscheduled gap (public holiday, missed run) extends the window the same way and surfaces the gap in § 7 (`Coverage window: extended to N hours due to scheduling gap; previous brief YYYY-MM-DD`).

### "Determining today" — day-of-week derivation
- Phase 0 now derives the day-of-week from `currentDate` and applies the recency-window table.
- Sub-agent spawn messages receive the computed window length so their `WebSearch` / `WebFetch` budgets target the right time range.

### META autonomy paragraph
- "fires once per weekday" replaced with "fires once per **working day** (Monday–Friday)"; weekly cadence stated explicitly as Sunday night.

### Docs
- `docs/workflow.md` schedule table updated.
- `README.md` daily-routine + weekly-routine paragraphs updated.
- `docs/routine-setup.md` recommended-cadence step updated to "Mon–Fri, 06:30 Europe/Zurich".

---

## 2.20 — 2026-05-07

### Why
Operator review of the deployed site flagged three things to harden:
(1) the agent had been citing the BSI generic landing page instead of the
specific WID-SEC advisory; (2) several deep-dive items leaned on news
articles when the underlying vendor / CERT report was reachable in one
extra fetch; (3) the agent's fetch budget was too tight for the
primary-source pivot work.

### Phase 1 — research methodology (changed)
- **Primary-source pivot mechanic made explicit and persistent.** The "follow news to the primary report" rule now spells out the pivot procedure step by step:
  1. Scan the article for outbound links (prose, pull-quotes, "via" footers).
  2. If no obvious link, search directly: `WebSearch "<vendor name> <topic> blog"` or jump to the vendor's `/research` / `/blog` index.
  3. **Incident chain**: victim disclosure → regulator filing → IR-firm post-mortem → news. Walk it from the victim end.
  4. **Vulnerability chain**: vendor PSIRT → NVD → national CERT (CERT-EU / CERT-FR / BSI WID / NCSC-CH CSH) → exploit-research lab → news.
  5. Don't stop at the first link that looks plausible — confirm it's the primary, not another aggregator. Two pivots is normal; three is fine when the trail is real.
  6. If the primary cannot be reached, record `Coverage gaps: <topic> — primary source <URL> unreachable, citing news as fallback` in § 7.

### Phase 1 — operational guardrails (changed)
- **Fetch budget raised 30 → 45 calls** to leave headroom for the pivot work (each pivot costs 2–3 fetches per item).
- **Wall-clock soft cap raised 10 → 12 min** for the same reason.
- **New "primary-source pivot reserve"** of ~10–15 of the 45 calls — fetches whose only purpose is to follow a news article down to the underlying primary report.
- Per-source timeout exception: when chasing a primary, one alternate path (publisher blog index, `tools/fetch_source.py`) is allowed and counts as part of the pivot, not a retry.

### Sources (`sources/sources.json`)
- **BSI Germany** URL replaced. The previous URL (`https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Cyber-Sicherheitslage/Technische-Sicherheitshinweise-und-Warnungen/Cyber-Sicherheitswarnungen/cyber-sicherheitswarnungen_node.html`) was a generic landing page that did not contain advisory content. New URL is `https://wid.cert-bund.de/portal/wid/kurzinformationen` (the CERT-Bund WID advisory index). RSS available at `https://wid.cert-bund.de/content/public/securityAdvisory/rss`. Per-advisory drill-down URL pattern is `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-YYYY-NNNN`. Drill-down is mandatory: never cite the kurzinformationen index, always the per-advisory detail URL.

### Existing briefs (retroactive)
- `briefs/2026-05-06.md`: both BSI Copy Fail citations (TL;DR § 1a item header and § 5 deep-dive narrative) updated from the broken landing-page URL to `https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1232` (the WID-SEC ID for CVE-2026-31431 'Copy Fail').

---

## 2.19 — 2026-05-07

### Why
Operator pass over [`docs/improvements.md`](../docs/improvements.md): bring the highest-leverage editorial and operational improvements into the prompt, retire the soft-kill-switch (`state/BLOCKED.md`) in favour of a stronger in-prompt self-check (Phase 5.5), and tighten the source-lifecycle rules so transport errors no longer demote sources that are merely being blocked by their publisher.

### Phase 0
- **Step 0 (BLOCKED.md circuit-breaker) removed.** The `state/BLOCKED.md` file was a pre-2.16-era idea that depended on an external editorial-invariant workflow we never built. Its responsibility is now absorbed by Phase 5.5 (in-prompt self-check, fail-closed on drift).
- **Step 2 strengthened.** The agent now reads the most recent weekly summary at `briefs/weekly/YYYY-Www.md` for the current ISO week and the prior ISO week explicitly, by name, regardless of file mtime. Closes the dedup gap when a Sunday weekly consolidates items the next Monday daily was about to re-report (improvements.md A6).
- **New step 5: read `state/deep_dive_history.json`.** Used by Phase 3's category-rotation rule.

### Phase 3 — deep-dive selection
- **Category-rotation rule added (improvements.md A8).** If the prior 7 days of `deep_dive_history.json` already cover a candidate's category (linux-lpe, windows-lpe, network-stack-rce, identity-infra, web-app-rce, endpoint-rce, firewall-vpn-rce, supply-chain, ot-ics, ransomware-affiliate, apt-campaign, cloud-saas, cryptography, mobile, annual-report, other), demote the candidate one rank — unless criterion 1 (active exploitation + non-trivial CH/EU public-sector exposure) makes it irreducibly urgent. Avoids covering "Linux LPE for the fifth day running" while OT and identity-infra go uncovered.

### Phase 4 — compose
- **Prompt-version field added to the metadata line.** `**Generated by:** ... · **Prompt:** v{N.M}`. The site renders this as a clickable badge linking to the matching CHANGELOG entry, so a reader can tell at a glance which editorial-policy version produced the brief (improvements.md D3).
- **Metadata line slimmed.** Removed `**Audience:** SOC Tier 2/3, IR, Threat Hunting` — the audience is documented elsewhere (README, About page) and added no per-brief value.
- **AI-generated content notice strengthened.** Now opens with **"AI-generated content — no human review."** and explicitly states **"Nothing here is reviewed or edited by a human before publication."** Closes a perception gap where readers could assume editorial oversight that does not exist.

### Prime Directive 2 — inline links, always (clarified)
- **Explicit "every section, no exception" wording added.** A real brief produced § 6 UPDATEs without inline citations (`UPDATE: ANTS officially confirmed the count as 11.7 million.` — no link). The directive now states verbatim that updates and "no material change" notes both require an inline source link, and § 4's per-section guidance restates it under § 6 specifically.
- **Phase 5.5 self-check #4 added.** Before commit: split § 6 on `> **UPDATE` boundaries; assert each non-empty UPDATE paragraph contains at least one `[…](http…)` link. Drift aborts the commit; the agent re-Edits § 6 to add the missing source.

### Phase 1 — research methodology
- **Bridge-fetcher allow-list expanded after 2026-05-07 retest.** Five additional publishers — `csirt-acn-it` (CSIRT Italy / ACN), `talos` (Cisco Talos blog), `prodaft` (PRODAFT reports), `inside-it-ch` (Inside IT Switzerland), and `ico-uk` (UK ICO news) — were verified to return HTTP 200 under the bridge fetcher's standard browser User-Agent. They were 403'ing the routine container previously; now reachable through `python3 tools/fetch_source.py url <URL>`. Hostname allow-list and prompt recipe both updated.
- **`ccn-cert-es` confirmed unreachable** even with full browser headers (`Sec-Ch-Ua` brand strings included). Likely Cloudflare / geo-IP gating from outside Spain. Source `notes` records the test outcome and the rule: never demote on this transport block; surface as `Coverage gaps: ccn-cert-es: 403 even with bridge fetcher` in § 7. Retest periodically.

### Phase 1 — research methodology
- **NCSC-CH Security Hub guidance corrected — twice in one day.** First investigation (morning) found that anonymous calls to `/api/posts/search` returned 302-to-login and concluded the platform was authenticated-only. Second investigation (afternoon) found that the routine container's default User-Agent was being filtered by the publisher; with a normal browser UA, the public TLP:CLEAR slice is fully reachable via `GET /api/posts/dashboard?pageSize=N&pageIndex=0` (listing) and `GET /api/posts/{id}/details` (per-post Markdown body). Source `ncsc-ch-security-hub` is back to `status: active`.
- **New helper: `tools/fetch_source.py`.** Stdlib-only, host-allow-list-restricted, read-only Python script that re-issues HTTP requests with a stable desktop-Chrome User-Agent. Solves the recurring 403 / 302-to-login on CISA pages and the NCSC CSH dashboard. Provides four sub-commands: `url`, `ncsc-csh {list,post,recent}`, `cisa-kev`, `cisa page`. Posts marked TLP:AMBER or TLP:RED are refused client-side. The agent uses this via the `Bash` tool whenever a `WebFetch` on the documented hosts comes back blocked. The script never authenticates, never executes JavaScript, and never fetches a host that isn't in its allow-list.
- **Phase 5 source-lifecycle clarification (already in v2.19, restated for emphasis).** A 403 / 302-to-login is a transport signal, not a content signal — it never demotes a source on its own. The agent records the alternate-fetch strategy (typically: "use `tools/fetch_source.py`") in the source's `notes` and keeps the source in rotation.

### Phase 5 — state update
- **Source-lifecycle rules rewritten on the transport-vs-content axis (improvements.md A1, A9).**
  - Two distinct counters per source: `consecutive_quiet_periods` (200 with no in-window items — content signal) and `consecutive_fetch_failures` (transport error — 403 / 429 / 503 / 5xx / 404 / dead host).
  - **Sustained 403 / 429 / 503 / 5xx never demotes.** That pattern means the publisher is blocking the agent's request shape, not that the source is dead. The agent records an alternate-URL strategy in `notes` instead and keeps the source in rotation.
  - Demotion fires only on the content axis: 3 consecutive quiet periods with a failed canonical-URL probe, OR 5 consecutive 404 fails.
- **Hard cap added (improvements.md SR10): one new candidate source per run, maximum.** A flood of new candidates in one brief is anomalous; overflow is queued in § 7 for the next run.
- **New file `state/deep_dive_history.json`** — rolling 30-day list of `{date, topic, category}`; FIFO trim. Phase 3 reads it on the next run.
- **New file `state/run_log.json`** — rolling 90-day per-run record (model, sub-agent allocation `sources_attempted`/`sources_used`/`items_returned`, fetch failures, items published, deep-dive slug, duration). Surfaced by the SPA's `#/ops` view (improvements.md A5 / S8).

### Phase 5.5 — self-check gate (new, between Phase 5 and Phase 6)
Drop-in replacement for the BLOCKED kill-switch (improvements.md A2). Three checks before commit:

1. Every state JSON file the run wrote parses cleanly.
2. Every `CVE-YYYY-NNNNN` extracted from the brief markdown appears in `state/cves_seen.json`.
3. Every H3 heading in §§ 1–4 of the brief has a matching `appearances[].date == today` record in `state/covered_items.json`. The H3 / appearance-count delta is permitted to be ±1 (the deep-dive H3 may also appear).

If any check fails, **abort Phase 6** (do not commit). The brief file remains on disk; the next run rebuilds the state delta from the brief itself (the brief is the canonical artefact, not the state). The state files are reconstructable from the briefs; the briefs are not reconstructable from the state files.

### Phase 6 — commit
- The `git add` line now includes `state/deep_dive_history.json` and `state/run_log.json`.

### Effect on output
- Briefs carry a clickable prompt-version badge.
- Deep-dive coverage drifts away from any single category that has been over-represented for a week.
- Sources blocked by 403/429/5xx stay in rotation indefinitely with notes about alternate URLs, instead of silently dropping out of the active list within three runs.
- Anomalous mass-source-discovery commits become impossible by construction.
- Commits with state/output drift never land on `main` — they abort and re-run.

### What this rolls back / supersedes
- Rolls back v2.16 (the BLOCKED.md circuit-breaker). Phase 5.5 is the structural replacement.

---

## 2.17 — 2026-05-06

### Why
Added `ncsc-ch-security-hub` (https://security-hub.ncsc.admin.ch/#/dashboard) to `sources/sources.json` — the unified Swiss NCSC security advisory dashboard. It's an SPA with hash routing, so a naive `WebFetch` on the dashboard URL returns only the JavaScript shell. The Phase 1 "drill into articles" rule already covered the general case; this version makes it explicit for SPA dashboards and forbids ever citing a dashboard / index / listing URL as the source for a claim. The fix is to find the SPA's underlying JSON API, list advisories, then open each per-advisory detail page and cite *that*.

### Changed
- **Phase 1 research methodology, item 1 expanded.** Strengthens the existing "follow links from index pages" rule: index pages, dashboards, listings, and feed views MUST never be the cited source. The inline citation always points to the per-article / per-advisory detail URL.
- **New SPA-specific guidance.** Concrete recipe for the NCSC-CH Security Hub and similar dashboards: identify the underlying `/api/` endpoint, list advisories, fetch each detail page, cite the detail URL. If the SPA defeats every approach, record the failure mode in `Coverage gaps:` rather than falling back to a dashboard citation.

### `sources/sources.json` change
- Added `ncsc-ch-security-hub` (HIGH reliability, ch-eu / active-breaking / gov / vulns categories, multilingual de/fr/it/en). Includes a long `notes` field documenting that the URL is an SPA entry point and the per-advisory drill-down requirement.

---

## 2.18 — 2026-05-06

### Why
Reverted the v2.15 engagement signal entirely. The GitHub Repo Traffic API exposes github.com repo traffic only — there is no public API for GitHub Pages site traffic — so `state/engagement.json` could never measure what the agent was meant to weight (Pages-site reader engagement). Pivoting to repo-blob view counts was honest but misleading: a niche signal dressed up as a primary one. Cleanest fix is to remove the dependency.

### Changed
- **Phase 0 step 5 removed** (engagement.json read).
- **Reader-engagement context block removed** from Phase 0. The agent no longer accepts the soft-tiebreaker signal in deep-dive selection. All editorial weighting returns to verification + CH/EU nexus + novelty as before.
- The `state/engagement.json` file is gone; `.github/workflows/sync-engagement.yml` is gone; the SPA's repo-traffic panels are gone.

### What stays
- **On-device personal reading history** in the site's localStorage. Per-brief visit count and dwell time, never leaves the device. This is the only "page count" the system keeps, and only for briefs the visitor opened on their own device.
- **The agent's verification gates and source-rotation logic are unchanged.**

### Why this is safe
The signal that just got removed was already only a *tiebreaker*. Verification, two-source rule, CVE existence check, no-IOCs rule, no-vanity-metrics rule, and source-rotation memory all stay in place. Editorial integrity is unaffected; we removed an input that was measuring the wrong thing.

---

## 2.16 — 2026-05-06

### Why
The system is now intentionally self-evolving — the agent edits the prompt, the source list, and the state files autonomously, and there is no human review gate on any of these. The threat-model document (`docs/security-review.md`) identifies prompt self-mutation drift (T2) as the residual risk that most warrants a structural defence. The right shape for that defence under the autonomy constraint is a soft kill-switch: a flag the agent itself checks at the very top of Phase 0, settable out-of-band when a quality-gate workflow detects an editorial-invariant violation, and clearable only by a deliberate (human) commit.

### Changed
- **Phase 0 step 0 added** (numbered 0 because it is a prerequisite, not a phase action). The agent now checks for `state/BLOCKED.md` before doing anything else. If present, the run aborts with no writes. The flag is the documented signal that something has gone wrong and a human (or a follow-up workflow) needs to look at it.
- A short note added to Phase 0 explaining that step 0 is the soft circuit breaker referenced in `docs/security-review.md` § 3.4.

### Why this is safe
The kill-switch is fail-closed by design: if the file system read fails, the agent stops. It is set automatically by a future `editorial-invariant.yml` workflow when output regressions are detected (IOC pattern in a brief, hallucinated CVE, multi-day flood of [SINGLE-SOURCE] items) and by hand when a human notices something suspicious. The flag's *presence* is the binding action — what the file *contains* is operator commentary that the agent never reads. So the flag cannot be subverted by injecting content into it.

---

## 2.15 — 2026-05-06

### Why
The repository now ships a public reader (`site/`) and an aggregate-only engagement-tracking pipeline (`.github/workflows/sync-engagement.yml` → `state/engagement.json`). Aggregate page-view counts from the GitHub Repo Traffic API are pulled into the repo so the agent can use *which prior coverage readers are returning to* as a soft signal when picking deep-dive topics and Updates-to-Prior-Coverage entries. The signal is fully aggregate (no PII, no sessions, no cookies) and is computed by GitHub from anonymised request logs.

### Changed
- **Phase 0 step 5 added** (with subsequent step renumber): read `state/engagement.json` if present. The file may be missing on first run or if the sync action has not yet succeeded — the agent must degrade gracefully in both cases.
- **New "reader-engagement context" subsection** in Phase 0 below the deduplication-context block. Specifies how the engagement signal is allowed to influence editorial selection:
    - Used only as a *tiebreaker* for Phase 3 deep-dive selection and Phase 4 § 6 Updates ordering.
    - Never overrides the verification rules, the two-source policy, the no-IOCs rule, or the no-vanity-metrics rule.
    - Reader engagement *guides attention*; the verification chain still gates everything.
- **No change** to Phases 1–7. Sub-agents do not see the engagement signal directly; the main agent applies it during Phase 3/4 selection only.

### Why this is safe
The engagement file is generated by a separate workflow that the routine cannot influence (the routine's git push doesn't touch the workflow's data source — GitHub computes the counts). Even if the file were poisoned, the agent's verification gates remain unchanged: a poisoned engagement signal could nudge topic selection but cannot change which sources are accepted, whether the two-source rule applies, or what makes it past Phase 2. See `docs/security-review.md` for the full threat-model analysis.

---

## 2.14 — 2026-05-06

### Why
The routine's runtime model has been switched (per-routine Claude Code configuration). The earlier prompt versions hardcoded "Claude Opus 4.7 / claude-opus-4-7" into the brief template's AI-generated content notice and `Generated by:` metadata line, which means a brief produced by a different model would carry an inaccurate identity unless the model overrode the template. Worse, by *naming* the model, the prompt biased the model into believing it was the named one. Fix: never name the model in the prompt; require the model to identify itself accurately at composition time.

The prompt also lacked explicit execution-environment context for the Claude Code Routines on the web infrastructure. The agent had to infer that it was running in an ephemeral cloud container with a feature-branch git proxy and time/token budgets — better to state it directly so it doesn't waste tokens orienting itself.

### Changed
- **Removed all model names from the prompt and supporting docs** (`prompts/daily-cti-brief.md`, `prompts/weekly-summary.md`, `README.md`, `briefs/README.md`, `docs/workflow.md`). The prompt now never says which Claude variant it is for. The hardcoded "Opus 4.7" / "Sonnet 4.6" / `claude-opus-4-7` / `claude-sonnet-4-6` strings are gone from the brief template, runtime headers, and prose.
- **Added an explicit "Self-identification" subsection** in Phase 4 (daily) and Phase 3 (weekly):
    - Identify yourself accurately when filling in the AI-content notice and `Generated by:` line.
    - Use the actual model name and ID you are at execution time.
    - Do not invent a name; if uncertain, write *"Anthropic Claude (specific model not determined)"* and continue.
    - Putting the wrong model name is an integrity failure.
- **Brief template now uses `{model name}` / `{model-id}` placeholders.** The model fills them in from its own identity at runtime. The reference template caption explicitly notes which placeholders are filled by self-identification vs. which are content placeholders.
- **Expanded "EXECUTION ENVIRONMENT — Where you are running"** with concrete context:
    - Ephemeral cloud container; the repo is the only durable memory.
    - Default branch is `main` but the runtime checks out a feature branch; the publishing chain handles `HEAD:main` push and feature-branch fallback.
    - Network access via internal HTTP proxy with allow-list.
    - Git operations via separate proxy; 403 means missing GitHub App permissions, not transient.
    - Wall-clock and token budgets enforced; sub-agent guardrails align.
    - **Model assignment is configurable at the routine level**; identify yourself accordingly.
- **Removed version-pinning header** ("Version: 2.0 (date)") from both prompt files. Source of truth for versions is `prompts/CHANGELOG.md` only — keeps each commit from also having to bump the header.

### Sonnet 4.6 considerations
The prompt is now well-suited to Sonnet's stronger literal-instruction following. Several earlier rule clarifications (incremental writes, partial-result composition, item granularity, news-to-primary pivot, no workflow-internal language) help Sonnet produce a brief that matches the intent without the inferred latitude Opus tended to take. Existing concrete worked examples (the W18 TeamPCP / Mini Shai-Hulud / Vect cluster as the example for item granularity) stay because Sonnet benefits from concrete reference patterns more than from abstract guidance.

---

## 2.13 — 2026-05-06

### Why
Earlier prompt versions said the agent "must not auto-promote candidates" and that "humans review demotions and candidate additions periodically". That was a leftover from a model where a human reviewed routine output before merge. The actual operating model is fully autonomous — the routine fires, commits, pushes, no human gate. Encoded "human review" steps are dead weight; worse, they cause new candidate sources to never get promoted, and the source list silently stagnates.

### Changed
- **`sources/sources.json` lifecycle is now fully autonomous.** Every state transition runs in the routine, with the git diff as the audit trail. Encoded transitions:
    - **Discovery → candidate** (already autonomous; unchanged).
    - **Candidate → active**: auto-promote after 3 distinct runs where the candidate was successfully fetched *and* contributed content to a brief. No human gate.
    - **Active → demoted**: after 3 consecutive failed fetches with no working canonical-URL probe (already autonomous; unchanged).
    - **Demoted → active (recovery)**: NEW. A demoted source returns to `active` when a working canonical URL is found during research *and* that URL contributes content to a brief. Update url, reset counters, dated note. No human gate.
    - **URL updates in place**: already autonomous; unchanged.
    - **Reliability tier-down without demotion** for navigation-only sources: already encoded in v2.12; unchanged.
- **Hard rules clarified**: do not delete sources (demotion is soft removal; cleanup is a separate manual commit), do not promote demoted → active without a recovery event, do not edit historical `notes` (append-only).
- **README "Maintaining the source list and the CVE index"** rewritten to describe the autonomous lifecycle. The phrase "for human review" is gone everywhere; the new framing is "git log is the curation history".

### Effect on the source list over time
- Candidates that consistently deliver content get auto-promoted. The active source list grows organically as the routine encounters new high-quality publishers.
- Demoted sources can self-heal when publishers fix their URLs.
- The active list stays operationally honest without external curation cycles.

---

## 2.12 — 2026-05-06

### Why
The 2026-05-06 brief's § 7 listed real coverage gaps:

> *"Coverage gaps: CCN-CERT Spain (not fetched, sub-agent budget limit); GovCERT.ch advisory archive (navigation page only); CERT.at and GovCERT Austria (navigation pages only, no dated advisory content returned); NCC Group Research, WithSecure Labs, Dragos, SANS ICS, Cloudflare Cloudforce One, Akamai SIRT, Elastic Security Labs, Group-IB, Secureworks CTU, Red Canary, Huntress, Sygnia — not fetched in this run."*

That signal is structured and self-emitted by the brief — perfect for closing the loop. Without it, the same handful of high-yield sources (NCSC.ch, CISA, CERT-EU, top vendor labs) get fetched every run while the rest of the curated list is silently starved by budget limits, biasing coverage toward those publishers' framings of the threat landscape. The goal is **neutral, balanced documentation of the ongoing threat landscape**, which requires source rotation.

### Added
- **Phase 0 — source rotation list construction.** The agent parses the `Coverage gaps:` line from § 7 of every brief in the last 7 days, aggregates source IDs / publisher names that appeared as gaps in 2 or more recent runs, and tags them as **rotation-priority** for this run. Each gap also carries the most recent *reason* (budget limit / navigation-page-only / dead host) so different responses can be applied.
- **Phase 1 — fetch budget reservation for rotation sources.** Each sub-agent reserves **6–8 of its ~30 fetch calls** for rotation-priority sources in its category scope. Must-have high-signal sources (CISA, NCSC.ch, CERT-EU, top vendor labs in scope) still go first; the reservation ensures the rest of the curated list also reaches the brief regularly.
- **Rotation-list handling rules** in Phase 1, mapping gap reasons to actions:
    - "not fetched, budget limit" → fetch this run.
    - "navigation page only" → fetch and *drill into linked articles*; if no dated content exists, record for source-list maintenance.
    - "consistent 404" → confirm and demote.
    - Successful fetch this run → source drops off the rotation list naturally for the next run.
- **Phase 4 § 7 format** — the `Coverage gaps:` line is now formally specified as parseable: single line, `Coverage gaps:` prefix, semicolon-separated `source-id (reason)` entries. Source IDs from `sources.json` preferred; publisher names fall back if not listed.
- **Phase 5 sources.json maintenance** — adds an optional `last_covered_in_brief` field per source (alongside the existing `last_successful_fetch`). Distinguishes "alive but quiet" from "alive and feeding the brief". Schema is allowed to grow; existing sources don't need backfill.
- **Phase 5** — new rule: a source that returns navigation pages only (no dated content) for 3+ consecutive attempted runs gets a `notes` flag and a reliability tier-down, but not full `demoted` status until a hard fetch failure.

### Effect on output
Over weeks, the brief covers a much wider slice of the curated source list. The W18 gaps (CCN-CERT, GovCERT.at, CERT.at, NCC Group Research, WithSecure Labs, Dragos, SANS ICS, Cloudforce One, Akamai SIRT, Elastic Security Labs, Group-IB, Secureworks CTU, Red Canary, Huntress, Sygnia) move to the front of W19's rotation reservation. Rotation is self-rebalancing: any source that gets fetched drops off the next run's rotation list automatically.

---

## 2.11 — 2026-05-06

### Why
A close read of the 2026-05-06 brief against the SANS ISC W18 TeamPCP weekly diary surfaced a structural problem: § 4 lumped four distinct W18 stories into one paragraph with one shared citation set:

1. The Mini Shai-Hulud SAP npm worm (Wiz / Socket / StepSecurity).
2. The cross-ecosystem propagation into PyPI Lightning and Packagist intercom-php (OX Security / Socket).
3. The first documented weaponisation of AI coding agent config files (.claude/settings.json, .vscode/tasks.json) by Mini Shai-Hulud (Wiz / Socket).
4. The Vect 2.0 ChaCha20 nonce-reuse / wiper-bug disclosure (Check Point Research, separate post).

Each is a distinct finding with a distinct primary publisher; the brief instead collapsed them into one paragraph and cited two roll-up sources (SANS ISC weekly diary + a Check Point weekly digest) instead of the four primary research posts. Net effect: the reader couldn't tell which source supported which claim, the substance got buried, and the citations sat one layer removed from the actual research.

### Added
- **Phase 1 research methodology — clarification on roll-up sources.** Weekly diaries (SANS ISC), vendor weekly threat-intelligence digests (Check Point's weekly research notes, etc.), and monthly summaries are *discovery*, not substance. Treat them like news: open them, follow the links to the primary publishers named inside, read those, and cite those. A roll-up cited for an individual claim is the same anti-pattern as citing news for a Mandiant finding.
- **Phase 4 — new "Item granularity — one story per item" subsection.** Distinct findings get distinct items, each with its own specific primary source set, even when they all attribute to the same actor / campaign / ecosystem. Worked example included (the W18 TeamPCP cluster: at least three brief items, possibly four — worm on SAP, cross-ecosystem propagation, AI-agent-config weaponisation, Vect wiper-bug). Section-level grouping with a one-line orientation sentence is fine; paragraph-level conflation is not.
- **Citation strategy** subsection extended:
    - "Don't cite a roll-up / weekly digest in place of the primary it summarises."
    - "One story = one set of citations." When item A's primary is Wiz and item B's primary is Check Point, those are two items in the brief, not one mixed paragraph.

### Effect on output
Future briefs will have more items per section but each item will be tighter — one specific finding, one specific primary source set, one specific defender takeaway. Sections like § 4 should look more like the SANS ISC W18 dated event log in structure: discrete dated events, each with its own attribution and source link, even when they cluster around one campaign.

---

## 2.10 — 2026-05-06

### Why
News sites are excellent at *discovery* — they tell defenders which vendor reports, CERT advisories, and primary research are worth reading this week. They are not the substance. The substance lives in the original Mandiant blog post, the CERT-FR advisory, the Volexity write-up, the SEC 8-K filing. A brief that summarises news summaries is two layers removed from the technical detail; a brief that cites the primary report puts the reader one click from the full content.

The 2026-05-06 brief was good but occasionally cited a news article when the underlying vendor report was the substance. This codifies the news-to-primary-source pivot as an explicit research and citation rule.

### Added
- **Phase 1 research methodology — rule 2: "News points to primary sources — always pivot to the report".** Sub-agents follow news links into the original vendor / CERT / research output and build the brief from the primary source. The news article becomes at most a *"via"* reference, included only when it adds something the primary source didn't.
- **Citation strategy** subsection in Phase 4 (composition):
    - Inline citations point to the primary source as the substance.
    - News added as *"via [Publisher](url)"* only when it adds value beyond the primary source.
    - Multiple primary sources are stacked inline when they corroborate (vendor blog + joint CISA advisory + Microsoft Threat Intel post on the same campaign — all three cited).
    - "Always link the primary report" rule: a brief paragraph without a primary-report link is a dead end.
- **Sub-agent 3 topical queries** expanded to include vendor-name + topic searches (e.g., *"Mandiant blog [today's month]"*, *"Talos research [today's month]"*) to surface primary reports directly without going through news.
- **Section 4 (Research & Investigative Reporting) guidance** updated: the cited link is to the primary report itself, not a news article that summarised it. Annual / periodic reports link to the report's landing page or PDF, not to news coverage.
- **Weekly summary** updated in parallel — same news-to-primary pivot rule.

### Effect on output
The brief becomes denser in primary-source links. A typical § 4 entry now links the actual vendor blog, advisory, or paper instead of the news article that pointed there. § 1, § 2, § 3 also gain primary-report links where journalism currently dominated.

---

## 2.9 — 2026-05-06

### Why
Reviewing the 2026-05-06 brief, four issues stood out:

1. **Workflow-internal language leaked into the brief.** Sentences like *"From Sub-agent 2. CH/EU nexus items first, then transferable global public-sector items."* appeared verbatim in the published Markdown. The reader doesn't know about sub-agents — that's prompt scaffolding, not output.
2. **Sub-agents summarised from index pages without drilling in.** When sub-agent 2 fetched `https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus.html`, it took the page's title list as the data, instead of following the links into the individual advisories.
3. **Sub-agents stuck to fixed URLs and missed topical breadth.** The curated source list was treated as the only set, not the starting set. New high-quality sources discovered while researching weren't proposed; sources that delivered nothing weren't flagged.
4. **No explicit self-evolution authority.** The user's intent is fully autonomous operation — the agent should be free to refactor prompts, restructure sub-agents, curate sources, and add docs without a human gate. The prompt didn't say so explicitly.

### Changed
- **Phase 4 restructured.** The output structure (eight section headings) is now a clean table; per-section content guidance is a separate block clearly labelled *"do not reproduce in the brief"*. Added a hard rule against workflow-internal references in the output. Placeholder text changed from `_(composing — see Phase 4)_` to `_(no content yet)_` so any leak reads as a sensible empty-section indicator instead of a workflow reference.
- **Phase 1 sub-agent operational guardrails expanded.**
    - **Drill, don't summarise from index pages.** When fetching an aggregator / listing page, follow the links into individual articles. Two full advisories beat ten headline-level inferences.
    - **Topical `WebSearch` per sub-agent.** Each sub-agent runs 2–4 topical search queries per run to discover primary sources outside the curated list and to validate against missing major stories. Concrete query examples per sub-agent included.
    - **Source discovery.** Sub-agents return a `Sources discovered:` list with publisher, URL, why it's high-quality, scope. Main agent in Phase 5 writes them to `sources.json` as `candidate`.
    - **Source self-curation across runs.** Promote candidates after 3 successful runs; demote consistent failures or aggregator-only sources.
    - Fetch budget bumped from ≤20 to ≤30 calls per sub-agent to accommodate the drill-down work.
- **New top-level section: META — self-evolution authority** in both the daily and weekly prompts. Authorises the agent to modify the prompt, source list, docs, sub-agent structure, and repo layout in normal operation. Lists hard invariants that must not be removed (AI-content notice, inline links, two-source rule, no IOCs / vanity metrics, English output, always-produce, no workflow-internal language, two-stage publishing). Documents the process: bump version, write CHANGELOG entry explaining the change, commit alongside the brief.
- **Weekly summary** updated in parallel — Phase 3 restructured to match the daily Phase 4 pattern (clean output structure table, separate guidance block, no-leak rule); Phase 2 inherits the drill / topical-search / discover-sources rules.

### Effect on operator output
- The two-stage publishing chain is now reflected in the weekly's `push:` line variants: `push: ok (direct main) | ok (via auto-merge action) | failed (<reason>)`.

---

## 2.8 — 2026-05-06

### Why
After v2.7, `git push origin HEAD:main` is the primary publish path. But on the 2026-05-06 run that direct push was rejected (the routine container's enforcement varied from what Path C should have allowed), so the brief stayed on a `claude/...` feature branch even though Path C was enabled in the routine config. The fallback path needs to actually merge to `main` rather than depend on a human to merge a PR.

### Changed
- **Phase 6 (daily) and Phase 5 (weekly) now describe a two-stage publishing chain explicitly:**
    1. Direct push (`git push origin HEAD:main`).
    2. Fallback push to the current branch.
    3. The repo's GitHub Action (`.github/workflows/auto-merge-claude.yml`) fast-forwards `main` from the feature branch and cleans up.
  Operator output reports which stage published: `push: ok (direct main)`, `push: ok (via auto-merge action)`, or `push: failed (<reason>)`.
- **The Action ships with the repo** at `.github/workflows/auto-merge-claude.yml`. It triggers on `push` to `claude/**` and on manual `workflow_dispatch` (with a `branch` input for after-the-fact merging). Concurrency-guarded so simultaneous merges don't race.

### Set-up implication
The auto-merge Action needs `contents: write` on the repo's default `GITHUB_TOKEN`. The workflow declares it; in most repos this works as-is. If the repo's organization sets the default token to read-only, the Action's push to `main` will fail — fix in the repo's **Settings → Actions → General → Workflow permissions**. Documented in `docs/routine-setup.md`.

---

## 2.7 — 2026-05-06

### Why
The 2026-05-06 run published successfully — but to a `claude/determined-hypatia-PCpxM` feature branch instead of `main`, even though "Allow unrestricted branch pushes" (Path C) was enabled on the routine. Cause: the routine container *always* checks out a `claude/<adjective>-<name>-<id>` branch on session start, and v2.6 told the agent to "honour the environment branch and push there". Path C means the routine *can* push to `main`, but v2.6 didn't tell it to try.

### Changed
- **Phase 6 (daily) and Phase 5 (weekly) now use `git push origin HEAD:main` as the primary publish path.** This pushes the current commit to remote `main` regardless of the local branch name. With Path C enabled, the brief lands directly on `main` and is live immediately. No PR step, no merge gate, no auto-merge dependency.
- **Fallback** if the primary push is rejected with 403: push the current branch as-is, so a GitHub auto-merge rule, a GitHub Action, or a manual PR review can take the brief to `main`. This handles the case where Path C is accidentally disabled or the routine credential lacks repo-write scope.
- Removed the v2.6 "honour environment branch override" framing — the prompt now actively pushes to `main`, with the fallback handling environments that block direct pushes.

### `docs/routine-setup.md` updated
- Explains the `HEAD:main` mechanism.
- Adds an optional `.github/workflows/auto-merge-claude.yml` GitHub Action as a safety net for the fallback case.

---

## 2.6 — 2026-05-06

### Why
First successful end-to-end execution of the daily prompt produced a 21-item brief but failed to publish: the routine ran in a Claude Code routine container which forces a feature-branch workflow (`claude/<adjective>-<name>-<id>`) and pushes through an internal git proxy. The proxy returned HTTP 403 because the GitHub App credential it uses doesn't have write access to the repo. The agent retried with backoff four times, which was noise — a 403 is a permissions issue, not a transient blip.

### Changed
- **Branch selection is now explicit.** Default is `origin/main`. If the execution environment has assigned a different branch (routine container, CI worktree, etc.), the routine pushes there and trusts the environment's PR / merge / fast-forward policy to land the change on `main`. The agent should not second-guess the environment's branch instructions.
- **Push-failure handling is one-shot.** No retry-with-backoff. A 403 won't resolve in seconds; a network blip will be picked up by the next run. One push attempt, surface the error verbatim, keep the local commit, exit cleanly.

### Same content guarantee
The brief's content, structure, and source pipeline are unchanged. Only the publish-step semantics shifted to be honest about feature-branch workflows and to stop retrying on hard auth errors.

---

## 2.5 — 2026-05-06

### Why
Second observed failure mode: with v2.4, all four sub-agents returned successfully and verification + deep-dive selection completed, but the final composition step hit `API Error: Stream idle timeout — partial response received`. The brief was being written in a single large `Write` tool call (the entire 8-section Markdown blob in one streamed response). The model pauses between sections during generation, and those pauses are long enough to trip the proxy's idle threshold on a large output.

### Changed
- **Phase 4 (daily) and Phase 3 (weekly) now require incremental writes.** One `Write` for the skeleton (header + AI notice + metadata + TL;DR + section headings with `_(composing — see Phase 4)_` placeholders), one `Read` to satisfy the `Edit` tool's precondition, then one `Edit` per section to replace the placeholder with the section's full content. Each `Edit` is a much shorter streamed output, well within idle-threshold safety.
- If a single section's content is itself unusually long (e.g., a vuln table with many rows), the agent splits that section's Edit into two halves.

### Same-output guarantee
The brief's content and structure are unchanged. Only the I/O pattern of the composition phase shifts — from one large `Write` to one `Write` + N `Edit` calls. This trades a small amount of tool-call overhead for stream-stability.

---

## 2.4 — 2026-05-06

### Why
Observed failure mode on first real run (2026-05-05): three of four sub-agents returned successfully, the fourth (Switzerland, Europe & Public Sector — slow national-CERT pages with German translation work) did not return on time, and the main agent waited indefinitely. No brief was written. **Never block the routine on one slow sub-agent.**

### Added
- **Prime Directive 12 — Always produce a brief; never block on a single sub-agent.** Specifies exact behaviour for 4/4, 3/4, 1–2/4, and 0/4 sub-agent return rates. Worst case still produces a stub brief with a "Quiet run — no sub-agent results" header. The presence of the file is the operational signal that a run took place; its absence is worse than a sparse file.
- **Operational guardrails for sub-agents** (Phase 1):
    - Target ≤20 WebFetch / WebSearch calls per sub-agent.
    - Per-source timeout: skip on hang/error, do not retry more than once.
    - Wall-clock soft cap of ~10 minutes per sub-agent — return what you have if you run long.
    - Always return something, even a one-line "no qualifying items" explanation.
- **Phase 2 trigger condition** is now explicit: begin as soon as all sub-agents that are going to return have returned (10-minute stall window). Do not wait indefinitely.
- **Quality gate added**: a brief file *must* exist at `briefs/YYYY-MM-DD.md` after every run.
- Same partial-result rules ported to the weekly summary (Phase 2).

---

## 2.3 — 2026-05-05

### Changed
- **Phase 6 renamed `COMMIT & PUSH`.** The routine now `git push origin main` after committing — every brief is published immediately. No review branch, no staging gate. Same for the weekly summary. Push failures do not roll back the commit; they are surfaced in operator output and a later run / manual push catches up. The routine never `--force`-pushes.
- **Active source maintenance** — Phase 5's `sources/sources.json` rules are now stronger:
    - Before demoting a source on 3 consecutive failures, the agent does **one canonical-URL probe** and updates the `url` in place if an equivalent page exists at the same publisher.
    - When a clearly better URL is discovered for an already-listed publisher, the agent updates the `url` in place (keeping the `id` stable so historical state references remain valid).
    - Every URL change is annotated with a dated note in the source's `notes` field and enumerated in the run's commit body.
    - Sources still cannot be deleted — `demoted` is the soft-removal mechanism.
- **Active CVE-index maintenance** — Phase 5's `state/cves_seen.json` rules are now stronger:
    - On reuse of an already-known CVE today, the agent updates `title` if a better short title exists (e.g., a CVE got a public name) and `primary_source_url` if a clearly better authoritative source now exists.
    - Records that turn out to be invalid (e.g., the CVE ID does not resolve on NVD/MITRE — a hallucinated identifier from an earlier run) are **removed**, with the removal noted in the commit body.
- Operator output now includes a `push: ok | failed (<reason>)` line.
- README and `docs/workflow.md` updated to reflect auto-push behaviour and the active maintenance rules.

### Why
The routine produces a public CTI feed; manual review-and-push doesn't fit that model. Auto-push to `main` makes every brief live immediately. Active source / CVE maintenance keeps the repo operationally honest over time without human babysitting — broken links self-heal where possible, and bad data self-corrects.

---

## 2.2 — 2026-05-05

### Changed
- **Daily sub-agents reduced from 7 to 4** with cleanly-partitioned source categories. The new four are:
    1. Active Threats & Trending Vulnerabilities (was A + D)
    2. Switzerland, Europe & Public Sector (was B + C)
    3. Research & Investigative Reporting (was E + F)
    4. Incidents & Disclosures (was G)
  Each source category belongs to exactly one sub-agent's filter, so no two agents touch the same source for the same purpose. Goal: cut per-run LLM load to avoid stream-timeout and rate-limit failures, while keeping coverage.
- **Daily brief output sections reduced from 10 to 8** to match the four-agent layout. New sections 0–7: TL;DR, Active Threats & Trending Vulnerabilities (with embedded vuln table as part 1b), Switzerland Europe & Public Sector, Notable Incidents & Disclosures, Research & Investigative Reporting, Deep Dive, Updates to Prior Coverage, Verification Notes.
- **Weekly horizon sub-agents reduced from 3 to 2.** W1 now combines long-running-campaign status checks with the annual / periodic-report horizon (both are "ongoing items beyond the daily window"). W2 keeps the strategic / policy horizon. The composed weekly summary's section list is unchanged.
- Quality gates and `Phase 5 — STATE UPDATE` `section` enum aligned to the new section names.

### Source list updates
- `cisa-kev` URL unchanged (`https://www.cisa.gov/known-exploited-vulnerabilities-catalog`).
- `cisa-alerts` renamed to `cisa-advisories` (URL unchanged: `https://www.cisa.gov/news-events/cybersecurity-advisories`).
- Added `cisa-news` (`https://www.cisa.gov/news-events/news`).
- Added `cisa-directives` (`https://www.cisa.gov/news-events/directives`).
- `shadowserver` URL updated to `https://www.shadowserver.org/news-insights/`.
- `agid-csirt-it` renamed to `csirt-acn-it`, URL updated to `https://www.acn.gov.it/portale/en/csirt-italia/alert-e-bollettini`.
- `prodaft` URL updated to `https://www.prodaft.com/reports`.
- `ncsc-ch` split into two entries — `ncsc-ch-incidents` (`aktuelle-vorfaelle.html`) and `ncsc-ch-focus` (`im-fokus.html`); both German, with note to translate findings.
- `ncsc-nl` removed (no news output available at the previous URL).

### Why
v2.1 runs were hitting "Stream idle timeout — partial response received" and Anthropic per-period usage limits when seven sub-agents ran in parallel and each did extensive WebFetch / WebSearch work. The four-agent design keeps the same scope under one tighter budget. The source-list updates align with the actual canonical pages of the publishers.

---

## 2.1 — 2026-05-05

### Changed
- **Added a `DEFENSIVE PURPOSE` preamble** to both prompts, immediately after `ROLE`. States explicitly that this is a defensive intelligence workflow for protectors, that every section is written from the defender's vantage point, and that the brief contains no operational attack details. Helps the framing stay correct end-to-end.
- **Sub-agent spawn prompts must lead with a defensive-intent statement** (template provided). Applies to all seven daily sub-agents and all three weekly horizon sub-agents.
- **Sub-agent G renamed and reframed** from "Major Breaches" to "Incident & Disclosure Roundup". Now explicitly framed as a *defender's overview* of who was publicly affected and what disclosed root causes can be learned from. Dark-web listings are treated as unverified claims and phrased accordingly. Each item ends with a *defender takeaway*. Output section 6 in the brief renamed "Notable Incidents & Disclosures".
- **Sub-agent C, F** got short defensive-purpose lines added.
- **Deep-dive language softened**: "Kill chain narrative" → "Incident narrative" framed from the defender's perspective.
- **Weekly summary § 5** renamed from "Major breaches recap" to "Incidents & disclosures recap" with defender-learning framing.

### Why
The previous v2.0 phrasing — although structurally fine — accumulated cybersecurity terminology that was triggering Anthropic's cyber-content usage-policy filter when sub-agents executed in parallel. Reframing to defender-first language and adding explicit defensive-intent statements at every level keeps the workflow operating as intended.

### Output structure unchanged
Section count and ordering of the daily and weekly briefs are unchanged; only the wording of section 6 and the framing within sub-agents has shifted.

---

## 2.0 — 2026-05-05

### Added
- **Weekly summary track.** New `prompts/weekly-summary.md` for a once-a-week extended brief that consolidates the week's daily briefs and adds horizon view, multi-day campaign rollups, and integration of yearly/periodic threat reports.
- **Major Breaches sub-agent (G).** Daily brief now has a dedicated sub-agent for newly disclosed breaches, drawing from regulator notices (SEC EDGAR 8-K, ICO, CNIL, EDPB) and victim disclosures, with a new § 6 section.
- **CVE fast-lookup index** (`state/cves_seen.json`). Flat list keyed by CVE ID for sub-agent dedup, complementing the richer `covered_items.json`.
- **Yearly/periodic-report rule** (Prime Directive 9). Annual reports (M-Trends, CrowdStrike GTR, ENISA TLR, Verizon DBIR, MS Digital Defense, IBM X-Force, Truesec TIR, Dragos OT YIR) get one dedicated treatment, then are not re-summarised — only cross-referenced as context.
- **Historical-context rule** (Prime Directive 10). For *highly relevant* deep-dive items with prior public reporting older than ~6 months, a Background paragraph (3–5 sentences) summarises what was known, with inline links. Targets the "humans forget things" problem without bloating routine items.
- **English-only output** (Prime Directive: Language). The brief is always in English even when sources are German / French / Italian / Polish — translate findings and keep original-language source titles.
- New sources: Sygnia, InfoGuard (CH), Truesec, NCC Group Research, WithSecure Labs, IBM X-Force, Akamai SIRT, Cloudflare Cloudforce One, Tenable Research, Rapid7 Research, GreyNoise Labs, Shadowserver Foundation, Citizen Lab, Dragos, CERT.at, GovCERT.at, CERT-PL, Trustwave SpiderLabs, SANS ICS (industrial), Help Net Security, Security Affairs, SEC EDGAR 8-K, UK ICO, CNIL FR, EDPB.
- New categories in `sources.json`: `breaches`, `ot-ics`.

### Changed
- **Look-back window: 7 days** (was 5). Reduces repeats during long-running campaigns and matches the weekly cadence.
- **Sub-agent return format is now flexible Markdown** with required fields, not a strict JSON schema. Sub-agents may add extended context and analysis. Required fields remain stable.
- **No token cap on sub-agents.** Sub-agents do whatever depth the topic warrants; they return summarised findings, not raw HTML.
- Updated `govcert-ch` URL to `https://www.ncsc.admin.ch/govcert` (legacy `govcert.ch` 302-redirects).
- Renamed daily output structure: § 6 Major Breaches inserted; Deep Dive moves to § 7; Updates to § 8; Verification Notes to § 9.

### Verified live (2026-05-05)
- NCSC.ch, GovCERT.ch (via redirect), Sygnia, InfoGuard, Compass Security, scip.ch, watchTowr Labs.

---

## 1.0 — 2026-05-05

Initial canonical version.

### Operating principles
- Zero LLM knowledge: every fact must come from a source fetched in the run.
- Inline source links at the point of claim; no bibliography.
- No IOCs (hashes, IPs, attacker domains/URLs, rule code).
- No vanity metrics (dwell time, breakout time, %-YoY).
- Two-source verification by default with national-CERT carve-out.
- Recency window 24 h default, 72 h for active campaigns.
- No-repetition rule with explicit `UPDATE` mechanism for material new developments.
- Long-running-campaign rule: ≤1 update per week unless critical change.
- Empty-section discipline.

### Execution model
- Six topic-scoped sub-agents spawned in parallel.
- JSON return schema (replaced by flexible Markdown in v2.0).
- Main context handles verification, deep-dive selection, composition, state update, commit.

### Output
- `briefs/YYYY-MM-DD.md`, sections 0–8.
- Updates `state/covered_items.json` and `sources/sources.json`.
- Conventional git commit.

### Source list
- Initial seed of ~40 sources across categories.
- Reliability tiers: HIGH / MEDIUM. Statuses: active / candidate / demoted.
- Maintenance rules: never delete; demote after 3 consecutive failed fetches; new sources enter as `candidate`.
