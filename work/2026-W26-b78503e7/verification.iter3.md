**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-28T23:45:49Z · ended_at=2026-06-28T23:50:37Z · duration_seconds=288
**Self-telemetry:** webfetch_calls=18 · websearch_calls=2 · bridge_fetches=0 · urls_checked=18

## Verification report — briefs/weekly/2026-W26.md (iteration 3)

Cold odd-iteration read. Fetched 18 cited URLs (every § 1 escalation source, every CVE-typed § 3 item's primary, the § 2 multi-day primaries, the § 6 research primaries, § 7/§ 8 actor + campaign sources, § 10 forward-looking links). UA-filtered hosts (inside-it.ch, securityweek some, bleepingcomputer) handled per spawn note: inside-it.ch 403 not re-flagged; BleepingComputer Endgame numbers corroborated via WebSearch (Europol/THN). Verdict: NEEDS_FIXES — two truth-class date/quantifier defects, one broken/generic URL, one contradiction to surface.

### Broken / unreachable URLs

**F1 — § 10 Looking ahead (libssh2 bullet), line 268.** Cited URL `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0210` does not land on the advisory — WebFetch returns only a "Redirecting... If you are not redirected, click here" stub with zero advisory content (confirmed on two fetches). The working specific-advisory URL is `https://advisories.ncsc.nl/2026/ncsc-2026-0210.html` (surfaced via WebSearch; confirmed to carry the libssh2 advisory: OOB write in ssh2_transport_read(), companion pre-auth DoS, public PoC, published 2026-06-24). Replace the `?id=` query-param URL with the `/2026/ncsc-2026-0210.html` path URL. (Not a host-allowlist 403 — this host is reachable; the specific query-string form is the non-landing one.)

### Unsupported / hallucinated facts

**F4a — § 2 npm supply-chain worms, line 58.** Brief: "On **06-27** Socket reported a fresh Miasma / 'Mini Shai-Hulud' worm wave across LeoPlatform/RStreams packages". The cited Socket page (https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem) is dated **June 25, 2026** (publish window June 24 in its own entity list), not 06-27. The "06-27" appears to be the daily-brief covering date, not the report date. Either correct to "On 06-24/25 Socket reported…" or reword to "Socket's report (covered in [daily 06-27])…". Quantifier/date-as-fact: the date is stated as the report date in prose.

**F4b — § 2 npm supply-chain worms, line 60 / footer.** Minor companion: brief § 2 line 60 says "On 06-21 Microsoft attributed the Mastra scope compromise". Microsoft's blog (footer URL path dated 06/17) and the cited BleepingComputer reporting are dated 2026-06-19/06-20 (BleepingComputer "Microsoft links Mastra AI supply chain attack to North Korean hackers", June 20; Microsoft high-confidence Sapphire Sleet attribution June 19). "06-21" is 1–2 days late. Advisory-grade date drift; correct to 06-19/20 or attribute to the daily covering date.

### Strengthen primary source / Surface contradiction

**F9 — § 3 libssh2 item (line 116–120) patch-status vs § 10.** § 3 carries `Status: poc-public, no-patch` and prose "the library-level fix had not landed by week-end", citing ONLY GHSA-r8mh-x5qv-7gg2. Two fetched sources tension this: (a) GHSA-r8mh-x5qv-7gg2 itself references a fix commit `7acf3df` (though "Patched versions: Unknown"); (b) the NCSC-NL advisory NCSC-2026-0210 (06-24) is titled in Dutch "Kwetsbaarheden **verholpen** in libssh2" ("vulnerabilities **fixed** in libssh2"). It is plausible the upstream commit existed but no tagged release shipped in-window — but the brief asserts "no library-level fix" as fact without acknowledging the commit/advisory. Surface as a confidence caveat in § 11 (e.g. "an upstream fix commit exists; a tagged release had not shipped by week-end") rather than leaving the bald "no-patch". Note: the NCSC-NL advisory also independently corroborates the companion DoS CVE-2026-55199, which the § 3-cited GHSA did not mention — a second reason to add NCSC-NL (the corrected URL from F1) as an Additional source on the § 3 item, not only § 10.

### Editorial / less-is-more flags (advisory)

**F11a — § 3 Keycloak headline conflation (line 110–114).** Headline "CVE-2026-11800 / CVE-2026-9800 — Keycloak JWT algorithm-confusion" bundles both CVEs under "JWT algorithm-confusion", but the Keycloak 26.6.4 release notes describe CVE-2026-9800 as a *policy-enforcer authorization bypass via incorrect URI comparison* — a different flaw from the JWT algorithm-confusion (which is CVE-2026-11800, CVSS 8.1, confirmed via GHSA-gqj5-2xp5-3qmp). The detailed prose only describes the JWT flaw, so no truth defect, but the headline mislabels CVE-2026-9800. Optional: split the headline or note CVE-2026-9800 is a separate authz bypass.

### Items verified clean (no action)

- § 1 NAIC: NAIC security update confirms June 11 PeopleSoft zero-day, temporary access to data-storage areas, credit-rating-agency feed pause, suspended designations — Evidence quotes are verbatim-accurate. 3.1 TB correctly attributed to ShinyHunters' claim via TechRadar/Insurance Journal; § 11 correctly flags it as an unconfirmed-by-NAIC volume claim. CVE-2026-35273 / CVSS 9.8 / pre-auth confirmed via GTIG.
- § 1 ShapedPlugin: claims well-attributed to Wordfence/BleepingComputer (Wordfence fetch returned transient-empty; corroborated via § 1 prose + BleepingComputer detail in earlier verification chain).
- § 2 Klue/Icarus: SecurityWeek confirms "roughly two dozen", 195 total per Klue private notification, Icarus hacked + second extortion group, Salesforce disabled integration 06-17. § 11 single-source/attributed-claim note is accurate.
- § 2 ShinyHunters cluster: Computer Weekly confirms 160 UK unis / ransom paid / April 2026 / ShinyHunters; 404 Media MSG vishing correctly hedged ("names no actor"); Abnormal SSO-vishing TTP attribution correct.
- § 3 Windchill CVE-2026-12569: THN confirms KEV 06-25, JSP web shells, CVSS 9.3, pre-auth deserialization.
- § 3 Cisco SD-WAN CVE-2026-20245: GTIG confirms full chain (CVE-2026-20127/20182 auth bypass → credential manipulation → CVE-2026-20245 root via CSV upload), published 06-24.
- § 3 libssh2 CVE-2026-55200: GHSA confirms OOB write in ssh2_transport_read(), CVSS 9.2, public PoC. (Patch-status caveat is F9.)
- § 3 Keycloak CVE-2026-11800: GHSA-gqj5-2xp5-3qmp confirms JWT algorithm-confusion, CVSS 8.1, forge assertion / bypass sig / impersonate federated user. (Headline F11a.)
- § 6 Tenable "Developer Credential Economy": confirmed verbatim — phrase used, Red Hat token ~7 weeks in infostealer logs, SLSA Build L3 provenance passed despite malicious content. The "Socket enumerates at least five affected tools" parenthetical maps to Socket's five named tools (Claude, VS Code, Cursor, Gemini, Copilot); acceptable paraphrase.
- § 6 BadBlocker (Island): 11M installs, one server-side config change, no store review, <all_urls>, Salesforce PoC — confirmed.
- § 6 Bluekit (Netcraft): BitM PaaS defeats DBSC, victim authenticates into attacker's browser — confirmed verbatim ("DBSC cannot protect against Browser-in-the-Middle").
- § 6 STOCKSTAY (GTIG): .NET/Windows Forms, secure WebSocket C2, Kazuar code overlap (K1MORPHER), malicious RDP files, WinRAR CVE-2025-8088 (also Sandworm/Gamaredon/RomCom), November 2025 RAR campaign, Ukrainian gov/mil + earlier IT/NL/PL/DE foreign-policy victims — all confirmed. GTIG dates STOCKSTAY to Dec 2022; "Kazuar … staple implant since 2017" is consistent with public Kazuar documentation, not contradicted.
- § 7 ESET Gentlemen: GentleKiller 8 BYOVD variants each abusing a different driver, HexKiller(Warlock/Baidu), ThrottleBlood(ThrottleStop; MedusaLocker/DragonForce), HavocKiller(Huawei), FortiGate-misconfiguration victim selection — all confirmed. 478 victims / Switzerland-second-most rest on inside-it.ch (403/UA-filtered, not re-flagged per spawn note; iter1 already reconciled counts).
- § 5 Texas Parks: BleepingComputer confirms 3,087,721 via unnamed third-party vendor; SSN public-vs-AG-filing discrepancy correctly carried as unresolved in § 11. § 8 Operation Endgame: 326 servers / 142 domains / 27M credentials confirmed via Europol+THN+WebSearch; Microsoft is correctly cited only for infrastructure analysis. § 2 ShinyHunters PeopleSoft campaign (§ 8): GTIG confirms UNC6240, May 27–June 9 predating Oracle's June 10 advisory, MeshCentral-as-Azure, [victim]_fanout.sh, 100+ orgs / 68% higher-ed.
- W-PD-1 framing: every § 1/§ 2/§ 7/§ 8 item answers inaction=incident, cross-day-pattern, or strategic-horizon. § 11 correctly documents the W25-carry-forward dedup and the dropped items (RoguePlanet, Brazil Cell Broadcast, etc.). No prior-W25 item re-asserted without an in-window delta.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 2)

Truth: F1 (broken/generic URL — counted as truth-adjacent broken-url), F4a (Socket date-as-fact), F9 (libssh2 patch-status contradiction surfaced as truth-class via unsupported "no-patch" assertion). F4b and F11a are advisory.
Note on counting: F1=broken-url (truth tally), F4a=quantifier/date-without-source (truth), F9=surface-contradiction (editorial by the standard taxonomy, but the underlying "no-patch" claim is unsupported-fact). Counted conservatively: truth=3 (F1, F4a, F9-as-unsupported), advisory=2 (F4b, F11a). If the main agent prefers F9 in the editorial bucket, truth=2/editorial=1.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: broken-url
  section: looking-ahead
  item: "libssh2 CVE-2026-55200 — public PoC but no library-level fix in window"
  url_or_quote: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0210"
  summary: "Query-string URL returns a 'Redirecting...' stub with no advisory content. Replace with the specific advisory page https://advisories.ncsc.nl/2026/ncsc-2026-0210.html (confirmed to carry the libssh2 advisory, 2026-06-24)."
- code: F4a
  category: quantifier-without-source
  section: multi-day-campaigns
  item: "npm supply-chain worms — a sustained wave across the week"
  url_or_quote: "On 06-27 Socket reported a fresh Miasma / 'Mini Shai-Hulud' worm wave"
  summary: "Cited Socket page is dated 2026-06-25 (publish window 06-24), not 06-27. The 06-27 is the daily covering date. Correct the report date or reword as 'covered in daily 06-27'."
- code: F9
  category: surface-contradiction
  section: vulnerability-roll-up
  item: "CVE-2026-55200 / CVE-2026-55199 — libssh2 heap OOB write [SINGLE-SOURCE]"
  url_or_quote: "Status: poc-public, no-patch / 'the library-level fix had not landed by week-end'"
  summary: "GHSA-r8mh-x5qv-7gg2 references fix commit 7acf3df and NCSC-NL NCSC-2026-0210 (06-24) is titled 'vulnerabilities FIXED in libssh2'. Brief asserts 'no library-level fix' as fact. Add a § 11 confidence caveat distinguishing upstream commit vs tagged release, and add NCSC-NL (which also corroborates the companion DoS CVE-2026-55199 absent from the cited GHSA) as an Additional source on the § 3 item."
- code: F4b
  category: quantifier-without-source
  section: multi-day-campaigns
  item: "npm supply-chain worms — Mastra attribution"
  url_or_quote: "On 06-21 Microsoft attributed the Mastra scope compromise"
  summary: "Advisory: Microsoft blog (06/17 path) and cited BleepingComputer reporting are dated 06-19/06-20, not 06-21. Minor date drift."
- code: F11a
  category: editorial-advisory
  section: vulnerability-roll-up
  item: "CVE-2026-11800 / CVE-2026-9800 — Keycloak"
  url_or_quote: "Keycloak JWT algorithm-confusion (headline bundles both CVEs)"
  summary: "Advisory: CVE-2026-9800 is a separate policy-enforcer authorization bypass via incorrect URI comparison per Keycloak 26.6.4 release notes, not the JWT algorithm-confusion (CVE-2026-11800). Detailed prose is accurate; only the headline conflates. Optionally split or relabel."
```
