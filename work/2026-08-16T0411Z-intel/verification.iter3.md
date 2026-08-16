**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-16T05:16:19Z · ended_at=2026-08-16T05:29:09Z · duration_seconds=770
**Self-telemetry:** urls_checked=14 · webfetch_calls=0 · bridge_fetches=16 · websearch_calls=0

## Verification report — 2026-08-16T0411Z-intel (iteration 3)

Read cold. All 12 inline source URLs across the five entries were fetched fresh this iteration through
`tools/fetch_source.py url` (the jina rung was not needed; every host answered the generic bridge), plus
two research sweeps (NCSC-NL advisories RSS, NCSC-CH focus listing, BleepingComputer security listing,
Security Affairs feed, CISA KEV) for the completeness check. Every `evidence[]` quote was byte-checked
against the freshly fetched page rather than against the run's saved captures. Prior coverage
(159 records, 14 days), `state/cves_seen.json`, `entities/registry.yaml` and `attack/enterprise-attack.json`
were checked directly.

**Truth pass: clean.** No broken URL, no generic/oversight URL, no unsupported claim, no hallucinated
entity, no uncited fact, no analytical link asserted beyond its source, no unsourced quantifier, no
name collision. Details of what was confirmed are in the closing note below the verdict.

### Missed angles

**F10 — whole-run: the one in-window story the run neither published nor recorded as a drop.**

`https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/`
— Bill Toulas, **August 15, 2026 10:14 AM** (ET; 14:14 UTC), i.e. inside this run's 26 h window
(floor 2026-08-15T02:11Z). Fetched this iteration; lede verbatim: *"A new Mirai-based modular Linux botnet
malware called Evooo1Bot has been targeting internet-facing gateway devices, turning them into SOCKS5
traffic relay nodes."* It rests on named Fortinet research, quoted in the article.

Three checks that make this a gap rather than a taste objection:

1. **In-window and on a source the run used.** The run record's S4 telemetry lists `bleepingcomputer` under
   `sources_used`, and the run cites four BleepingComputer articles. This item is the *only* story on that
   publication's chronological security listing dated inside the window — everything above it in the
   listing is 2026-08-14 or older, and the top featured strip (Plug and Pwn, Lazarus/AFD, ShieldBreak) is
   either already carried by the store (2026-08-12 Lazarus, 2026-08-12 ShieldBreak) or out of window.
2. **Not covered.** Keyword sweep over all 159 prior-coverage records for `evooo`, `mirai`, `botnet`,
   `socks5`, `plug and pwn`, `usb` returns empty. Nothing in `cves_seen.json` either.
3. **Not decided.** It appears nowhere in the run record's seven-item borderline-drop list, which is
   otherwise thorough and does record near-neighbours (a consumer-grade router auth bypass was dropped for
   "no plausible nexus"). So this was dropped silently.

Why I judge it clears the bar rather than being commodity botnet noise: the exploit module set is not
consumer-only. Fortinet, via the article, names *"Hikvision cameras, Atlassian Confluence, Zyxel firewalls,
TP-Link routers, D-Link NAS devices, WSO2 products, Kubernetes ingress-nginx, and vulnerable PHP-CGI
installations"*, and the targeted device list includes **Mitsubishi Electric** gateways — that reaches the
energy/water/transport/telco estates in this profile's additional sectors, not just home routers. The
behavioural substance a Tier 2 reader could act on is present and vendor-neutral: SOCKS5 direct and
reverse-relay modes, a credential sniffer monitoring `/proc/net/tcp` for HTTP Basic and Cookie headers, an
SSH scanner using 150 enterprise-oriented credential pairs with post-login honeypot checks, encrypted C2
over port 443, persistence across systemd / SysV init / shell profiles / rc.local with a cron job
re-downloading the payload every five minutes, and bash-history clearing after successful exploitation.

**Remediation is not necessarily "publish".** A recorded borderline-drop line with the reasoning is an
equally acceptable outcome — the defect is the silence, not the absence. Suggested query if the run wants
the primary: `Fortinet Evooo1Bot Mirai SOCKS5 relay botnet ingress-nginx`.

### Editorial / less-is-more flags (advisory)

**F11 (a) — `status: exploited` resolves in opposite directions on evidentially equivalent facts.**

SAP entry frontmatter: `status: [exploited, patch-available, mitigation-only]`. Its evidential base is
Defused honeypot telemetry — *"First exploitation attempts against CVE-2026-58231 (unauth RCE in SAP
Commerce Cloud, CVSS 10.0) is now hitting our honeypots - 3 days after patch day"* (verified verbatim on
the BleepingComputer page) plus NCSC-NL recording scanning. Its own body concedes: *"no party reports a
compromised production instance"*.

Adobe entry frontmatter: `status: [patch-available]`. Its evidential base is *"Sansec Shield already blocks
exploitation attempts."* (verified verbatim on sansec.io) plus BleepingComputer's *"Attempts to exploit a
critical vulnerability (CVE-2026-71362) in Adobe's Commerce and Magento e-commerce platforms have been
detected"* (verified verbatim). Its own body concedes: *"Nobody reports a confirmed compromised store"*.

Same evidential shape — exploitation attempts observed by one vendor's sensors, no confirmed compromise —
opposite machine-readable outcome, in the same 24 h render window. Each sourcing note is internally honest;
together they are inconsistent, and a reader or triage agent filtering on `status: exploited` gets one and
not the other. (If anything the Adobe case is the stronger of the two: Sansec Shield sits in front of real
merchant storefronts, Defused's sensors are honeypots.) The taxonomy offers no finer value than `exploited`,
so either choice is defensible in isolation — advisory, and the main agent may leave it, but the divergence
should be a decision rather than an accident.

**F11 (b) — recency disclosure is asymmetric across the run's three out-of-window entries.**

`2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role` ships on two sources both dated
2026-08-14 (Cybersecurity Dive's JSON-LD `datePublished` reads `2026-08-14T11:32:51`; Infosecurity's dateline
reads `14 August 2026`), roughly two days before this run's floor. Neither the entry's `sourcing_note` nor
the run record says why a two-day-old item ships now. The run's other two out-of-window entries both do:
the Adobe entry's sourcing note carries *"This flaw was disclosed on 2026-08-11 and is outside this run's
window; it is published now because earlier fires whose windows covered it did not"*, and the deep dive and
the macOS entry are accounted for in the run record's backlog and completeness-sweep paragraphs. On content
the ExfilSquad entry plainly earns its place (it is the second-assessor validation on Power Pages
anonymous-role ground the store carries from 2026-08-04 and 2026-08-05, and NCSC-CH turned that
configuration into a Swiss obligation on 2026-08-04 — both confirmed in prior coverage). One clause naming
the recency basis would close the asymmetry.

**F11 (c) — T1185 missing from the deep dive's ATT&CK mapping.**

`techniques: [T1189, T1176.001, T1204.002, T1059.003, T1539, T1056.003, T1102.001, T1102.002, T1113, T1115,
T1014, T1556.003, T1090]`. Every one of those resolves to an active, unrevoked, non-deprecated technique in
the pinned `attack/enterprise-attack.json`, and every one has a matching behaviour in the body — I checked
each individually. **T1185 (Browser Session Hijacking)** is also active in the pin and is arguably the
central technique of this implant, but is absent. The body maps it explicitly: *"A background service worker
gave the operator a full bridge into the browser API: any Chrome or Firefox function invocable by name,
arbitrary JavaScript injected into any page"*, and Symantec's own sentence is *"interact with the browser as
if sitting at the keyboard"*. Advisory — the mapping is unusually thorough as it stands.

### Verdict

`NEEDS_FIXES (truth: 0, editorial: 1, advisory: 3)`

The truth surface of this run is in good shape and the editorial surface is close. Only F10 stands between
this run and CLEAN; the three F11s are leave-able.

**What I confirmed, so the next iteration need not re-walk it:**

- **Every URL live and specific** (12/12, all fetched this iteration via the bridge): the two NCSC-NL
  advisory detail pages, four BleepingComputer article URLs, the Adobe PSIRT bulletin, the Sansec research
  post, the Onapsis patch-day post, the Symantec/security.com report, Infosecurity Magazine and
  Cybersecurity Dive. No homepage, listing index, NVD/MITRE per-CVE page or category landing among them.
- **Every citation date matches the source's own dateline**: NCSC-2026-0302 `15-08-2026 09:41`;
  NCSC-2026-0280 `[1.0.1] 12-08-2026`; BleepingComputer SAP `August 14, 2026`; BleepingComputer macOS
  `August 14, 2026`; BleepingComputer Adobe `August 12, 2026`; BleepingComputer Jewelbug `August 13, 2026`;
  Adobe APSB26-92 `August 11, 2026`; Sansec `August 11, 2026`; Onapsis `Published: August 11, 2026`;
  Symantec `13 Aug 2026`; Infosecurity `14 August 2026`; Cybersecurity Dive `2026-08-14T11:32:51`.
- **All 15 `evidence[]` quotes are contiguous verbatim substrings** of the freshly fetched pages, including
  the three Dutch-language quotes (the source's own typo `kwetbaarheid` is faithfully reproduced) and the
  Defused tweet text carried inside the BleepingComputer article.
- **The pointed correction is right.** Adobe's affected-versions table reads: Commerce
  `2.4.9-2026-jul … 2.4.4-2026-jul`, B2B `1.5.3 / 1.5.2 / 1.4.2 / 1.3.4 / 1.3.3-2026-jul`, Magento Open
  Source `2.4.9 / 2.4.8 / 2.4.7 / 2.4.6-2026-jul`, each "and earlier"; the solution table reads Commerce
  `2.4.9-2026-aug … 2.4.4-2026-aug`, B2B `1.5.3-aug … 1.3.3-aug`, MOS `2.4.9-aug … 2.4.6-aug`. The entry's
  `affected`, `fixed` and body paragraph now transcribe all three product lines cell-for-cell. CVSS 9.1,
  CWE-863, "Authentication required to exploit: No", "Exploit requires admin privileges: No" and `UI:N` in
  the vector all confirmed on the vendor table, as are "seven vulnerabilities" and "five rated Critical".
- **SAP `exploited` is honestly framed in prose.** The body states what is confirmed (attempts against
  sensors, scanning) and what is not (no compromised production instance, SAP has not flagged it), and each
  clause is cited to the source that actually carries it — iteration 1's F3 split is correctly applied
  (scanning to NCSC-NL, honeypot attempts and the SAP no-flag statement to BleepingComputer). Onapsis
  genuinely carries the rebuild/redeploy requirement and the IP Filter Set workaround verbatim, and the
  page supports the "works with SAP on its patch cycle" descriptor ("Eleven of the twenty-nine new Security
  Notes were published in contribution with the Onapsis Research Labs"). My only reservation is the
  cross-entry consistency in F11(a), not the prose.
- **macOS at `high` rather than `critical` is correctly reasoned.** The critical bar requires *newly*
  disclosed/weaponised plus time-critical action; Apple fixed this on 2026-08-06 (confirmed on the
  BleepingComputer page: "Apple fixed CVE-2026-65400 on August 6"), the store has carried the patch
  instruction twice (2026-08-08 and 2026-08-11, both present in prior coverage), and the observed outcome
  is cryptomining. `high` is the right call and the run record's reasoning holds.
- **The deep dive is earned.** Every substantive claim in it — the shared-hosting watering hole across 15+
  tenants, the nine-domain server-side qualification filter, the `com.microsoft.runedge` native-messaging
  escape, the HKCU registry write, the 37 ClientKing builds and five C2 transports, the Google Docs payload
  channel, the 1M/580k/2,300 database figures, the Changsha attribution and its documentary basis, the
  clipboard module present but with no rules deployed — is carried by the Symantec page I fetched. Nothing
  drifts beyond the source, no IOC reaches the entry, and the transferable architectural lesson to Swiss
  shared e-government hosting is the entry's own clearly-labelled analysis. Category reuse is disclosed in
  the run record and does not weaken the item.
- **Coverage otherwise looks complete.** NCSC-NL's advisory feed carries nothing newer than NCSC-2026-0302
  (this run's SAP entry). NCSC-CH's focus page has published nothing since 11.08.2026. CISA KEV has zero
  additions since 2026-08-12. Security Affairs' in-window items are the SAP entry, the macOS entry, the
  GeoServer zero-day (already carried at 2026-08-15) and an expired-domains malware-delivery piece that
  does not clear the gate. The one gap is F10.
- **Frontmatter contract holds across all five.** No `org_triage` block is non-null; no `watchlist_hit:
  true` and no `watchlist` tag (correct — no watchlist is configured); every entry carries a
  `classification` block inside the A–F / 1–6 vocabulary, and each `credibility: 2` is consistent with the
  one-assessor situation each sourcing note describes. No IOC pattern (hash, IP, `hxxp`) appears in any
  entry. No workflow-internal vocabulary leaks into any entry body or the run-record notes.
- **Dedup and entity linking are correct.** The three `update_of` targets each exist in prior coverage and
  each new entry carries a genuine delta over its parent (SAP parent recorded "No exploitation is reported
  by any party"; macOS parent recorded no confirmed exploitation; the ExfilSquad line had no second
  assessor). CVE-2026-71362 is genuinely new to `cves_seen.json`. The five new registry keys are absent
  from 14 days of prior coverage under every alias Symantec names (Earth Alux, REF7707, CL-STA-0049), and
  the four `uses` relations on `actor:jewelbug` are typed correctly and sourced to the full entry id.
- **Action discipline is right on all five.** Two entries carry one action each, three carry none. Both
  actions are concrete, self-contained and derived from their own finding's mechanics, and both repeat a
  parent's instruction only where the delta changes it (the SAP action adds redeploy verification plus a
  compromise-assessment obligation dated to 2026-08-14; the macOS action adds a compromise assessment on
  the confirmed root-plus-miner outcome). The three empty lists are correct: the ExfilSquad Power Pages
  enumeration task already shipped as an action on both 2026-08-04 and 2026-08-05, and the deep dive's
  hardening levers are body content by design.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F10
  category: missed-angle
  section: active-threats
  item: "whole-run — Evooo1Bot Mirai-derived Linux gateway botnet (Fortinet research, 2026-08-15)"
  url_or_quote: "https://www.bleepingcomputer.com/news/security/new-evooo1bot-linux-botnet-turns-routers-into-traffic-relay-nodes/"
  summary: "In-window (2026-08-15 10:14 ET / 14:14 UTC, floor 2026-08-15T02:11Z), on a source the run fetched and used (bleepingcomputer, S4 sources_used), resting on named Fortinet research. Absent from all 159 prior-coverage records (keyword sweep: evooo/mirai/botnet/socks5 all empty) and absent from the run record's borderline-drop list, so it was dropped silently rather than decided. Content reaching this constituency: modular Mirai-derived Linux botnet on internet-facing gateway devices (Alcatel, NETGEAR, Tenda, Mitsubishi Electric, Telesquare, D-Link) with an exploit module set covering Hikvision cameras, Atlassian Confluence, Zyxel firewalls, TP-Link routers, D-Link NAS, WSO2, Kubernetes ingress-nginx and PHP-CGI; SOCKS5 direct and reverse relay, credential sniffer reading /proc/net/tcp for HTTP Basic and Cookie headers, SSH brute-force with 150 enterprise credential pairs and post-login honeypot checks, encrypted C2 on 443, systemd/SysV/shell-profile/rc.local persistence with a five-minute cron re-download, bash-history clearing. Either publish it or record the drop reasoning in the run record's borderline-drop list. Suggested query: 'Fortinet Evooo1Bot Mirai SOCKS5 relay botnet ingress-nginx'"
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "2026-08-16/cve-2026-58231-sap-commerce-cloud-exploitation-attempts vs 2026-08-16/cve-2026-71362-adobe-commerce-customer-account-takeover"
  url_or_quote: "SAP: status: [exploited, patch-available, mitigation-only] / Adobe: status: [patch-available]"
  summary: "Two entries in the same window resolve evidentially equivalent facts to opposite cve status values. SAP rests on 'First exploitation attempts against CVE-2026-58231 ... is now hitting our honeypots' (Defused via BleepingComputer) plus NCSC-NL scanning, and its body concedes 'no party reports a compromised production instance' -> status carries exploited. Adobe rests on 'Sansec Shield already blocks exploitation attempts' (Sansec) plus BleepingComputer's 'Attempts to exploit a critical vulnerability (CVE-2026-71362) ... have been detected', and its body reaches the same conclusion, 'Nobody reports a confirmed compromised store' -> status omits exploited. Both sourcing notes are individually honest but reason to opposite machine-readable outcomes; a reader or agent filtering on status: exploited gets one and not the other. Advisory: pick one rule and state it, or leave with the divergence acknowledged."
- code: F11
  category: editorial-advisory
  section: updates
  item: "2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role"
  url_or_quote: "sources dated 2026-08-14 (Infosecurity Magazine) and 2026-08-14 (Cybersecurity Dive); verified datePublished 2026-08-14T11:32:51 on Cybersecurity Dive"
  summary: "Both sources predate this run's 26 h floor (2026-08-15T02:11Z) by roughly two days, yet neither the entry's sourcing_note nor the run record explains the out-of-window publication. The run's other two out-of-window entries each do carry that disclosure — the Adobe entry's sourcing note ('This flaw was disclosed on 2026-08-11 and is outside this run's window; it is published now because earlier fires whose windows covered it did not') and the deep dive / macOS entry via the run record's backlog and completeness-sweep paragraphs. Content clearly earns publication (Swiss-relevant Power Pages anonymous-role ground the store carries from 2026-08-04 and 2026-08-05); only the disclosure is asymmetric. Advisory: add one clause naming the recency basis."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole"
  url_or_quote: "techniques: [T1189, T1176.001, T1204.002, T1059.003, T1539, T1056.003, T1102.001, T1102.002, T1113, T1115, T1014, T1556.003, T1090]"
  summary: "T1185 (Browser Session Hijacking) is active in the pinned dataset and is arguably the central technique of this implant, but is absent from an otherwise 13-deep mapping. The body maps the behaviour explicitly: 'A background service worker gave the operator a full bridge into the browser API: any Chrome or Firefox function invocable by name, arbitrary JavaScript injected into any page', and Symantec's own text is 'interact with the browser as if sitting at the keyboard'. Advisory only — every listed id is active, unrevoked and body-supported."
```
