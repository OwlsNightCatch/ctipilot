**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-29T04:47:12Z · ended_at=2026-08-29T04:57:55Z · duration_seconds=643

## Verification report — 2026-08-29T0409Z-intel (iteration 1)

Cold first pass. All 7 new entries, the 1 updated entry (body + frontmatter + `git diff`), and the run record were read in full; every inline source URL was fetched with `tools/fetch_source.py extract`/`url`/`jina` this iteration.

### Generic / oversight URLs (replace with specific article)

**#1** — `2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc`: the NCSC-NL corroborating source is cited as `https://advisories.ncsc.nl/rss/advisories`. Fetched: this is the live RSS **feed of all NCSC-NL advisories** (`<title>NCSC Security Advisories</title>`, dozens of unrelated `<item>` entries for NCSC-2026-0334, NCSC-2026-0333, NCSC-2026-0286, etc.), not the specific advisory. The specific advisory the entry actually needs is `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0289` (confirmed present in the feed, item title "NCSC-2026-0289 [1.01] [H/H] Kwetsbaarheden verholpen in Microsoft Exchange server", and its update text explicitly names CVE-2026-62911's published PoC). Fix: cite the specific advisory URL, not the feed.

### Citation does not support the claim

**#2** — `2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce`: body states "PaperCut released an initial emergency patch for v25/v26 on 28 August, which a **Home-page variant** of the same request bypassed; Emergency Patch Release 2 ... closes that bypass" cited solely to `[PaperCut Software, 2026-08-29]`. Fetched the vendor bulletin (`papercut.com/kb/...urgent-security-advisory`) in full: it never mentions "Home", "Home page", or any bypass technique for the first patch — only that Release 2 adds "additional hardening ... developed with internal security and external researchers, including Huntress and watchTowr." The "Home-page variant... bypassed" detail is stated only by Rapid7: "Additionally, the first emergency patch could be bypassed by using the Home page for display, however the newest version of the vendor patch correctly remediates this bypass." The clause needs a Rapid7 citation, not (or in addition to) PaperCut's.

**#3** — `2026-08-29/servicenow-ai-platform-four-unauth-cvss10-flaws`: body attributes the specific technical descriptions — "GraphQL Composite Data API" (CVE-2026-18885), "access-control bypass in the system-configuration image-upload processor" (CVE-2026-18886), and "dynamic-schema SQL injection" reached via an "ORDER BY clause" (CVE-2026-74820) — to `[ServiceNow, 2026-08-29]`. Fetched KB3152242 in full via `extract` (confirmed complete: covers all four CVEs, the fixed-version table, and the FAQ) and grepped it for "GraphQL", "image-upload", "access control", "ORDER BY" — zero matches. ServiceNow's own text calls CVE-2026-18885 **and** CVE-2026-18886 both "a code injection vulnerability... identified in the ServiceNow AI platform," with no mention of GraphQL, image uploads, or access control. All three technical-mechanism details are stated only by The Hacker News, not ServiceNow.

**#4** — same entry: body states "Three share the identical CVSS4.0 vector `AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H` ... ([ServiceNow, 2026-08-29])". ServiceNow's public KB3152242 text contains no CVSS vector strings at all (only "Based on the CVSS v4.0 calculator, we have assessed the risk ... to be critical/high"); the two KB articles that would carry vector data (KB3152244, KB3152251) are behind a "Requires Now Support Login" wall and were never fetched. The vector string is stated only by The Hacker News ("The three maximum-severity flaws share the vector CVSS:4.0/AV:N/...").

**#5** — `2026-08-29/german-carriers-imei-leak-call-setup-signaling`: body states "Across more than 70 test calls **captured with Wireshark** on the caller's own device..." cited to `[BR24, 2026-08-29]`. Fetched BR24's article in full: it reports the 70+ test calls but never mentions Wireshark or any capture tool. The Wireshark detail is stated only by heise: "...seien dabei in mehreren Fällen IMEIs zum Anrufer gelangt, wie **Wireshark-Mitschnitte** des Datenverkehrs zeigten."

**#6** — same entry: body states "SRLabs' **Karsten Nohl** added that device-model exposure also enables more targeted attacks and IMEI cloning ([BR24, 2026-08-29])." Fetched BR24's article in full: Nohl and SRLabs are not mentioned anywhere in it. The quote is heise's own reporting, obtained directly by heise, not BR: "Karsten Nohl, Gründer von SRLabs ..., **konkretisierte gegenüber heise online** diese Einschätzung: 'Neben den Tracking-Szenarien ermöglicht die IMEI auch gezieltere Angriffe etwa mit Bezug zum konkreten Smartphone-Modell oder auch IMEI-Cloning'." The clause needs a heise citation, not BR24's.

### Unsupported / hallucinated facts

**#7** — `2026-08-29/servicenow-ai-platform-four-unauth-cvss10-flaws`: frontmatter `cves[]` for CVE-2026-18886 sets `affected: "ServiceNow Now Platform — same release lines and fixed builds as CVE-2026-18885"`. The cited vendor source (KB3152242) states the opposite: "ServiceNow has remediated a code injection vulnerability that was identified in **the ServiceNow AI platform**" for CVE-2026-18886 — same platform as 18885 and 74820, not "Now Platform." Only CVE-2026-6876 is vendor-attributed to the Now Platform. The frontmatter contradicts its own cited primary source's product attribution.

**#8** — `2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor` (this run's update): the diff adds `T1090` (Proxy) to `techniques[]` alongside the DARKLANTERN/SPEAKINGSTONE update. Fetched both VulnCheck posts (`zbt-endlessdoors`, `zbt-darklantern-speakingstone`) and heise's corroborating article in full and grepped all three for "proxy", "pivot", "socks" — zero matches in any. Neither implant is described as offering proxying/pivoting (DARKLANTERN is a WAN command backdoor; SPEAKINGSTONE offers shell exec, PPPoE-credential theft, DNS-hijack-list read/write, and reverse-SSH tunnel open/close — none of which is "Proxy" in the ATT&CK sense used elsewhere in this store, e.g. RedC2's actual SOCKS5 feature). No source or body text supports this technique id.

**#9** (low confidence) — same entry: `affected_products` diff adds `"ZBT-WE826-T2 and rebrands (Deep Orange, WiFlyer)"`, implying WiFlyer specifically rebrands the WE826-T2. VulnCheck's text ties WiFlyer generically to ZBT's own USPTO trademark ("WiFlyer routers are not ZBT-derived. They are ZBT, sold ... through Amazon and Newegg") and elsewhere pairs the WiFlyer brand specifically with the **WG3526** platform ("The KuWFi WG3526 ... is the same platform sold as the WiFlyer WG3526"), not WE826-T2. The WE826-T2 rebrand VulnCheck actually demonstrates is Deep Orange only.

**#10** — `2026-08-29/swiss-cantons-eautoindex-vehicle-registry-data-harvesting`: evidence record #2's `original:` field reads "...technische Schnittstelle, die ausschliesslich den Zugang zu öffentlich einsehbaren Daten erlaubte. ... Es handle sich nicht um ein eigentliches Datenleck..." — the ellipsis splices two sentences from cash.ch that are not adjacent in the source; the article's actual intervening sentence, dropped by the splice, is "Dass gesperrte Daten abflossen, könne ausgeschlossen werden, so Probst." Each half is independently verbatim, but per check 4b an inserted ellipsis joining non-contiguous source text is itself the defect, regardless of whether the omitted content changes meaning.

### Claims missing inline citation

**#11** — `2026-08-29/swiss-cantons-eautoindex-vehicle-registry-data-harvesting`: the entry's closing paragraph ("No source names the specific bypass technique ... Cantonal officials warn of a plausible follow-on fraud vector: attackers or downstream buyers of the harvested plate/name/address/approximate-birthdate combination could send deceptively authentic-looking demands for fake fines, vehicle-inspection fees, or foreign toll charges.") carries no inline citation at all, although the fraud-vector claim is drawn from cash.ch ("Denkbar seien etwa «täuschend echt wirkende» Zahlungsaufforderungen zu angeblichen Bussen, Gebühren, Motorfahrzeugkontrollen oder ausländischen Mautgebühren") — a fact stated by a specific source and reused without attaching that source again.

### Surface contradiction

**#12** — `2026-08-29/servicenow-ai-platform-four-unauth-cvss10-flaws`: ServiceNow's own KB3152242 calls CVE-2026-18886 "a code injection vulnerability ... identified in the ServiceNow AI platform," while The Hacker News calls the same CVE ID "An improper access control vulnerability in the system configuration image upload processor." These are materially different vulnerability classes and different products for the identical CVE id. The entry silently adopts THN's framing (`type: auth-bypass`, "access-control flaw," "Now Platform") without a `Contradiction:` line noting that the vendor's own text disagrees.

### Editorial / less-is-more flags (advisory)

**#13** — Run record `runs/2026-08-29/2026-08-29T0409Z-intel.md`, published "Verification & coverage notes" (reader-facing per the spawn message): "**Coverage-backlog re-check (Phase 0 step 5b):** all five previously-open rows re-gated..." — "Phase 0" is one of the four terms explicitly named as prohibited workflow-internal language in check 12 / CLAUDE.md ("no workflow-internal language ('sub-agent', 'Phase N', 'spawn', 'main agent')"). The same notes section also repeatedly uses internal sub-agent labels "S1"/"S2"/"S4" and pipeline jargon "tasking" ("S1's product sweep and S4's supplier sweep were no-ops per tasking, S2 applied the sector/region lens...") and "fire" ("seventh consecutive fire blocked on the same ground" — in the entry text, not shown above but present in prior coverage; "fire" is this pipeline's own term for a scheduled run). None of this is meaningful to a reader of the published notes.

**#14** (low confidence) — `2026-08-29/german-carriers-imei-leak-call-setup-signaling`: `priority: high` for a German-carrier telecom-signaling gap with no direct action available to this constituency beyond "ask Swiss carriers" (which the body itself already flags as unconfirmed/untested) and `actions: []`. Given check 5b's bar ("high must be genuinely TL;DR-worthy... renders at the top of the 24h window"), this is defensible given the BfV/GSMA angle but borderline for a non-Swiss-carrier finding with no cited exploitation and no org-actionable step beyond an inquiry; flagging for the main agent to weigh, not asserting it is wrong.

### Name-collision unflagged

**#15** — `2026-08-29/redc2-npm-supply-chain-redshell-linux-implant` registers `tool:redc2` with alias **"Red Agent"** — an LLM-backed command-translation component of an attacker C2 framework ("RedC2 ships with an AI assistant called Red Agent, an LLM-backed command execution layer that turns natural-language intent into framework beacon commands"). `entities/registry.yaml` already carries a **distinct** entity, `tool:wiz-red-agent`, name **"Wiz Red Agent"** — Wiz's own autonomous AI-driven **offensive-security research tool** (published one day earlier, `entries/2026-08-28/wiz-red-agent-snowflake-github-actions-command-injection.md`). These are different entities (correctly separate registry keys, no merge needed), but the human-readable name "Red Agent" is now shared between a malicious C2 assistant and a defender/researcher's tool of the same name, one day apart in the same store, with **no disambiguation** anywhere ("not to be confused with," a `references[]` link, or a distinguishing note) in either entry or either registry summary. This is exactly the confusable-name pattern check 15 asks to be flagged — request the RedC2 entry (or its registry record) add a one-line disambiguation.

### Verdict

`NEEDS_FIXES (truth: 10, editorial: 2, advisory: 2)`

Truth: #2, #3, #4, #5, #6 (F3 ×5), #7, #8, #9, #10 (F4 ×4), #15 (F15 ×1) = 10.
Editorial: #11 (F5), #12 (F9) = 2.
Advisory: #13, #14 (F11 ×2) = 2.

Coverage-shape note: the run record's own telemetry already logs its coverage gaps (searchlight-cyber, team-cymru, sans-ics, paradigm-shift-research consent/ad-redirect/SPA failures; inside-it.ch's 403'd ServiceNow-incident lead; cisa/cert-pl no-in-window-item) and three borderline drops (Minea, Qare, Boston Scientific) with defensible reasoning for each. I found no additional in-window gap beyond what is already self-identified — coverage looks complete for this window.

### Findings summary (machine-readable)
```yaml
- code: F2
  category: generic-url
  section: new-entries
  item: "CVE-2026-62911 — Microsoft Exchange Server MRSProxy auth bypass, PoC"
  url_or_quote: "https://advisories.ncsc.nl/rss/advisories"
  summary: "cited URL is the full NCSC-NL advisory RSS feed listing, not the specific advisory; specific URL is https://advisories.ncsc.nl/advisory?id=NCSC-2026-0289"
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "PaperCut NG/MF Tapestry request-confusion pre-auth RCE (deep dive, critical)"
  url_or_quote: "PaperCut released an initial emergency patch for v25/v26 on 28 August, which a Home-page variant of the same request bypassed ... ([PaperCut Software, 2026-08-29])"
  summary: "PaperCut's own bulletin never mentions a Home-page bypass; only Rapid7 states it (\"the first emergency patch could be bypassed by using the Home page for display\")"
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ServiceNow AI Platform / Now Platform four unauthenticated CVSS 10.0 flaws"
  url_or_quote: "CVE-2026-18885 is a code-injection flaw in the GraphQL Composite Data API ... CVE-2026-18886 is an improper-access-control flaw in the system-configuration image-upload processor ... CVE-2026-74820 is a SQL injection reached through a dynamic database-schema query ([ServiceNow, 2026-08-29])"
  summary: "ServiceNow's public KB3152242 text contains none of GraphQL/image-upload/access-control/ORDER BY; it calls both 18885 and 18886 \"code injection\" with no further mechanism detail. These specifics are stated only by The Hacker News."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ServiceNow AI Platform / Now Platform four unauthenticated CVSS 10.0 flaws"
  url_or_quote: "Three share the identical CVSS4.0 vector AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H ... ([ServiceNow, 2026-08-29])"
  summary: "ServiceNow's public KB3152242 carries no CVSS vector strings at all; the vector string is stated only by The Hacker News"
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "German mobile carriers IMEI leak in call-setup signaling"
  url_or_quote: "Across more than 70 test calls captured with Wireshark on the caller's own device ... ([BR24, 2026-08-29])"
  summary: "BR24's article never mentions Wireshark or a capture method; heise's corroborating article states \"wie Wireshark-Mitschnitte des Datenverkehrs zeigten\""
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "German mobile carriers IMEI leak in call-setup signaling"
  url_or_quote: "SRLabs' Karsten Nohl added that device-model exposure also enables more targeted attacks and IMEI cloning ([BR24, 2026-08-29])"
  summary: "Nohl/SRLabs are not mentioned anywhere in BR24's article; the quote is heise's own reporting (\"konkretisierte gegenüber heise online diese Einschätzung\")"
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "ServiceNow AI Platform / Now Platform four unauthenticated CVSS 10.0 flaws"
  url_or_quote: "cves[].CVE-2026-18886.affected: \"ServiceNow Now Platform — same release lines and fixed builds as CVE-2026-18885\""
  summary: "ServiceNow's own KB3152242 states CVE-2026-18886 \"was identified in the ServiceNow AI platform\", not Now Platform — frontmatter contradicts its cited primary source"
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "ENDLESSDOORS / DARKLANTERN / SPEAKINGSTONE (2026-08-06 entry, updated this run)"
  url_or_quote: "techniques: [T1059, T1571, T1036, T1572, T1090]"
  summary: "T1090 (Proxy) added this run; neither VulnCheck post nor heise's article nor the update-section body mentions proxying/pivoting for DARKLANTERN or SPEAKINGSTONE (grepped both VulnCheck posts and heise for proxy/pivot/socks — zero matches)"
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "ENDLESSDOORS / DARKLANTERN / SPEAKINGSTONE (2026-08-06 entry, updated this run)"
  url_or_quote: "affected_products: \"ZBT-WE826-T2 and rebrands (Deep Orange, WiFlyer)\""
  summary: "(low confidence) VulnCheck ties WiFlyer generically to ZBT's trademark, and specifically pairs the WiFlyer brand with the WG3526 platform elsewhere in the same post, not WE826-T2; only Deep Orange is demonstrated as a WE826-T2 rebrand"
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "Six Swiss cantons eAutoIndex/ecari vehicle-registry data-harvesting"
  url_or_quote: "original: \"Der Abruf der Daten erfolgte gemäss bisherigen Erkenntnissen über eine technische Schnittstelle, die ausschliesslich den Zugang zu öffentlich einsehbaren Daten erlaubte. ... Es handle sich nicht um ein eigentliches Datenleck ...\""
  summary: "ellipsis splices two non-adjacent cash.ch sentences, dropping the intervening sentence \"Dass gesperrte Daten abflossen, könne ausgeschlossen werden, so Probst.\" — each half verbatim but the record is not a contiguous substring"
- code: F5
  category: missing-citation
  section: new-entries
  item: "Six Swiss cantons eAutoIndex/ecari vehicle-registry data-harvesting"
  url_or_quote: "Cantonal officials warn of a plausible follow-on fraud vector: attackers or downstream buyers of the harvested plate/name/address/approximate-birthdate combination could send deceptively authentic-looking demands for fake fines, vehicle-inspection fees, or foreign toll charges."
  summary: "no inline citation anywhere in this closing paragraph, though the fraud-vector claim is cash.ch's own reporting restated without re-attaching the source"
- code: F9
  category: surface-contradiction
  section: new-entries
  item: "ServiceNow AI Platform / Now Platform four unauthenticated CVSS 10.0 flaws"
  url_or_quote: "ServiceNow: \"a code injection vulnerability that was identified in the ServiceNow AI platform\" (CVE-2026-18886) vs. The Hacker News: \"An improper access control vulnerability in the system configuration image upload processor\" (same CVE)"
  summary: "vendor and corroborating outlet disagree on CVE-2026-18886's vulnerability class and product; entry silently adopts THN's framing with no Contradiction: line"
- code: F11
  category: editorial-advisory
  section: run-record
  item: "runs/2026-08-29/2026-08-29T0409Z-intel.md — Verification & coverage notes"
  url_or_quote: "Coverage-backlog re-check (Phase 0 step 5b): all five previously-open rows re-gated on today's facts."
  summary: "\"Phase 0\" is an explicitly-prohibited workflow-internal term (check 12 / CLAUDE.md); same notes also repeatedly use internal labels S1/S2/S4 and jargon \"tasking\"/\"fire\" in reader-facing text"
- code: F16
  category: org-triage
  section: new-entries
  item: "German mobile carriers IMEI leak in call-setup signaling"
  url_or_quote: "priority: high"
  summary: "(low confidence) borderline high — no cited exploitation, no org-actionable step beyond an unconfirmed inquiry to Swiss carriers, actions: [] — flagging for the main agent to weigh, not asserting miscalibration"
- code: F15
  category: name-collision-unflagged
  section: new-entries
  item: "Fourteen trojanized npm packages drop RedC2 4.0's RedShell Linux implant (RedC2 entity alias \"Red Agent\")"
  url_or_quote: "aliases: [\"RedShell\", \"RedShell Linux\", \"Red Agent\"] (tool:redc2) vs. tool:wiz-red-agent name \"Wiz Red Agent\" (entries/2026-08-28/wiz-red-agent-snowflake-github-actions-command-injection.md)"
  summary: "the name \"Red Agent\" is shared between RedC2's malicious LLM-backed C2 command-translation component and Wiz's own defensive/offensive-security research AI tool published one day earlier in this same store; distinct entities, correctly separate registry keys, but zero disambiguation in either entry or registry summary"
```
