**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-17T00:09:11Z · ended_at=2026-08-17T00:29:47Z · duration_seconds=1236
**Self-telemetry:** urls_checked=54 · webfetch_calls=20 · bridge_fetches=26 · websearch_calls=0

## Verification report — 2026-08-16T2315Z-weekly (iteration 1)

Read cold. All 14 entries read end-to-end (frontmatter + body), plus the run record, prior_coverage.json (165 records), triage.json, findings.W1/W2.yaml, url-liveness.tsv and the 19 saved bodies under raw/. All 54 distinct source and inline URLs across the 14 entries were resolved this iteration; two remain unreachable to me and to the run (cisa.gov/news-events/... alert slug and .../cybersecurity-advisories/aa26-222a — direct HTTP 403 and all seven jina keys at HTTP 402), both already recorded in the run record's fetch_failures with mitigations, so no F1 is raised for them. Every quoted passage in every entry was literal-substring-checked against the saved bodies, and the load-bearing ones (Defused honeypot quotes, Calif four-hour timeline, NCSC-NL Dutch quotes, CrowdStrike parsing-stage quote, Check Point telemetry-teardown, Kaspersky Nsiproxy/certificate, ETSI, THN passkey, Dragos/Check Point Q2, Wiz, Sophos, Group-IB, ICO) were re-verified verbatim against the live pages. No quote failed.

**On the three points of concentrated scrutiny that came back clean:** (1) the contradiction entry's boundary holds — CISA CSAF ICSA-21-056-03 is titled 'Rockwell Automation Logix Controllers', its known_affected list is exactly RSLogix 5000 16–20 / Studio 5000 Logix Designer >=21 / FactoryTalk Security >=2.10, both CISA quotes and both Dragos quotes are verbatim, KEV dateAdded is 2026-03-05, CVE-2017-16740 is absent from KEV, and neither title, headline, summary nor body asserts what happened in Minnesota (one frontmatter defect only, F4 below); (2) all three sub-agent corrections are right — THN states verbatim that SpecterOps 'now considers the full Windows-to-Entra vulnerability chain broken' and that Microsoft 'applied mitigations for the reported issue involving passkey relay assertions'; the Dragos US figure is 431 / 38%; Symantec confines the Jewelbug watering hole to 'a Middle Eastern country' and never names Europe (the run record's *reason* for the second correction is itself wrong — F4 below); (3) priority calibration and W-PD-1 are defensible on all 14 — no critical, four highs each carrying a genuine cross-day pattern or an on-fire consequence, and no entry is a one-to-one re-list.

### Generic / oversight URLs (replace with specific article)

**F2** — `weekly-w33-clop-windchill-status` cites `https://api.ransomware.live/v2/recentvictims` for "A leak-site tracker first recorded 44 named Cl0p victim entries on 12 August". That is a rolling API listing of the 100 most recent victims. Fetched live this iteration: it currently contains **zero** Cl0p records. The URL cannot support a dated claim and will never reproduce it. Replace with a stable per-group / dated page, or attribute the count to the referenced operational entry `2026-08-13/clop-leak-site-names-44-victims-swiss-dutch-listings`.

### Citation does not support the claim

**F3.1** — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: "Switzerland's NCSC published its own advisories on the vCenter, SharePoint, NetScaler and GeoServer items inside the same week" (and summary "put four of the five in front of its own constituency inside the same week"), cited to `https://security-hub.ncsc.admin.ch/#/posts/12844`. That post is the GeoServer advisory alone. I pulled the hub's own post list this iteration (`fetch_source.py ncsc-csh recent 60`): the ONLY NCSC-CH Security Hub posts inside 2026-W33 are **12839 SAP (08-11), 12840 Microsoft Patch Tuesday (08-12), 12841 Adobe (08-12), 12844 GeoServer (08-14)**. No in-week hub advisory on vCenter, SharePoint or NetScaler; the referenced operational entries describe an *update* to a pre-existing vCenter advisory (12 Aug) and a NetScaler position held since 3 July, and nothing in the run supports an NCSC-CH SharePoint advisory at all. NCSC-CH publishes on more than one surface so this does not prove none exists — but the citation as placed claims four and carries one, and this sentence is the entry's home-region hook. (Note the hub *did* publish an in-week SAP advisory, which the entry does not count.)

**F3.2** — `weekly-w33-exfilsquad-claims-validated-status`: the sentence "concluded that the group's access claims are correct for at least 13 organisations ... with the UK Department for Education and the Police National Legal Database among them" is co-cited to Infosecurity Magazine **and** Cybersecurity Dive. Infosecurity carries all of it. Cybersecurity Dive, fetched in full this iteration, carries none of it: "Security researchers are backing claims by a newly emergent data-extortion group that it has exfiltrated sensitive data from **about 15** companies, governments and other organizations"; it names the UK Department for Education but not the Police National Legal Database, and never mentions 382.64 GB, 27 million records, the 7 August torrent or 10,000+ Power Pages instances. The sourcing_note's "reported by two outlets independently" overstates it, and the 13-vs-15 divergence is unsurfaced.

**F3.3** — `weekly-w33-attacking-the-record-not-the-sensor`: "the theft ... was established only after the attacker **advertised the dataset for sale** on 12 August", cited to the French finance ministry release. The release (n°953, 14 août 2026, fetched this iteration) says: "Mercredi 12 et jeudi 13 août 2026, un acteur malveillant a **revendiqué des accès illégitimes**..." — claimed illegitimate access, across two days, with no mention of a sale offer.

**F3.4** — `weekly-w33-developer-credential-audits-wrong-artefact`: "had credential collection that **ended** before the poisoned LiteLLM packages were ever published". SOCRadar says "2,085 of the 2,188 organizations, or 95%, **show collection activity before** March 24" / "were already exposed before March 24", and states its records' last-seen timestamps run to "March 24 at 20:09 UTC" — after publication. "began before" matches; "ended before" does not.

**F3.5** — `weekly-w33-disclosure-to-exploitation-interval-collapsed` (and the same clause in `weekly-w33-vuln-status-rollup`): "Germany the largest single concentration ahead of the United States, Turkey, Iran and France". THN says "Most of them are located in Germany, the U.S., Turkey, Iran, and France" — an enumeration, not a ranking. The QUIRSO original is unreachable (medium.com 403 direct; all seven reader keys 402), so no available source states the ranking. Lightest of the set; minimal fix is "concentrated in Germany, the US, Turkey, Iran and France".

### Unsupported / hallucinated facts

**F4.1** — `weekly-w33-attacking-the-record-not-the-sensor`: "Four disclosures **inside 2026-W33**" / "Four of **this week's** disclosures" / title "...**this week**". Contradicted by the entry's own `sources[]` dates and confirmed live: CrowdStrike **2026-08-07**, Group-IB **2026-07-30**, Sophos **2026-08-07** (no date on the page at all), only the six-agency advisory (2026-08-10) is inside W33 (Mon 08-10 – Sun 08-16). The pipeline *covered* three of them on 2026-08-10; they were not disclosed in-week. Reframe, don't re-fact — the underlying detail is verbatim-correct.

**F4.2** — `weekly-w33-water-plc-lockout-status` frontmatter: `status: [cisa-kev, patch-available]` and `fixed: "Per Rockwell Automation's own advisory for the affected Logix families"`. The entry's own cited CISA CSAF advisory says: "**Rockwell Automation has determined this vulnerability cannot be mitigated with a patch.**" Every remediation entry is category `mitigation`; there is no fixed version. Both fields are machine-consumed.

**F4.3** — run record, verification notes: "W1 reported a Dragos figure of 514 incidents for North America. **That number does not appear in the report**". It does: "North America: Recorded 514 incidents in Q2 2026 (up from 480 recorded in Q1 2026), remaining the second-most impacted region." (in the run's own `raw/dragos_q2.txt` line 3145 and live). The correction's outcome is right; the stated reason is false, and the notes publish.

### Quantifier without source

**F14.1** — `weekly-w33-clop-windchill-status`: "the **first** post-exploitation detail published for this campaign" (title, summary), "the **first** technical detail anyone has published about what the actors do after exploitation" (body), "until this week the campaign offered **no** post-exploitation artefact to hunt for" (Defender takeaway). Refuted by the entry's OWN cited Foresiet post (2026-08-10, fetched this iteration): "PTC went on to report heightened threat activity and **documented attackers deploying JSP webshells inside Windchill login directories**" and "PTC identified hexadecimal-named JSP webshells under /Windchill/login/, a custom HTTP request header named X-windchill-req, and flst.txt". The webshell artefact class was public before this week; ReliaQuest is corroboration, not a first, and the takeaway is wrong on the entry's own evidence.

**F14.2** — `weekly-w33-vuln-status-rollup` headline: "**two** exploited with no identifier at all". The body's dedicated section names exactly one (GeoServer), as does the summary. The only candidate second is CVE-2026-72898 (Metabase), which the same entry files under "newly exploited or newly KEV-listed" and which now has both an identifier and a KEV entry (dateAdded 2026-08-11, verified).

**F14.3** — `weekly-w33-disclosure-to-exploitation-interval-collapsed` summary: "**Two researchers** rebuilt working pre-authentication root exploits ... in about four hours". Calif's post is subtitled "**Two pre-auth macOS remote root exploits** in four hours" and closes "Two pre-auth remote root exploits in four hours, on and off, across a busy weekend" — two exploits, one team ("we", "our engineers are in APAC"). The only other named researcher, @osxreverser, found the *first* bug, did not report it and did not do the diffing. The body renders the same fact correctly; only the frontmatter drifts.

### Claims missing inline citation

**F5.1** — `weekly-w33-etsi-cra-harmonised-standards-approval`: the EN 304 category list ("VPNs, network management systems, SIEM, boot managers, PKI certificate-issuance software, network interfaces, operating systems, routers, modems and switches, virtualization and container platforms, and firewalls") carries no citation, and neither cited source has it — the ETSI release names only "password managers, anti-virus software, smart home assistants, connected toys, and wearables", and Help Net Security reproduces exactly that short list. The sourcing_note attributes it to `https://docbox.etsi.org/CYBER/EUSR/Open`, which the ETSI release links, which this run's url-liveness ledger records at 200, and which is not in `sources[]`. The list is load-bearing — it is what makes the entry a procurement item. Add the docbox URL and cite the sentence.

**F5.2** — `weekly-w33-looking-ahead`: the Cl0p bullet is the only one of seven with no inline citation, against the entry's own contract ("Each carries a source and a date"). The Swiss ISMS bullet is explicitly exempted in the sourcing_note; this one is not.

### Surface contradiction

**F9.1** — `weekly-w33-water-plc-lockout-status`: Dragos states "CVE-2021-22681 carried a CVSS score of 9.8"; the co-cited CISA advisory states "A CVSS v3 base score of **10.0** has been calculated", and the frontmatter silently takes 10.0. A second discrepancy in the very paragraph the entry interrogates — worth a clause, given the entry's thesis.

**F9.2** — `weekly-w33-clop-windchill-status`: entry says 44 named listings (tracker); co-cited BleepingComputer says Clop "listed Shell among **43** victims". Unsurfaced.

### Missed angles

**F10** — The week ships no Russia / Ukraine-nexus content at all. Truesec, **14 August 2026** (in-window), "Russia Targets Businesses and Officials Behind Europe's Ukraine Defense Supply Chain" — GRU Unit 26165 and Russian services running combined surveillance, sabotage and cyber operations against European defence manufacturers, drone start-ups, component suppliers and **logistics firms**, including cyber access attempts against logistics and technology companies transporting aid to Ukraine to obtain "train schedules, manifests, routes, cargo contents and sender/recipient details", plus published target addresses and a matured assassination plot against a named CEO. Transport is a profiled additional sector; the coverage focus is European critical infrastructure and government. This was surfaced by the run and then silently lost: the run's own `url-liveness.tsv` records the Truesec index **and this exact article** at HTTP 200 at 2026-08-16T23:19:58Z; `truesec` is in W1's `sources_attempted` but not `sources_used`; it is **not** in `triage.json` "dropped"; and it is **not** in the run record's coverage-gaps list. Prior coverage carries zero records matching "Ukraine" or "truesec" across all 165 records, so this is not dedup suppression. Publish it or record it as a reasoned drop. Query: `GRU Unit 26165 European defence logistics targeting August 2026`.

### Classification missing / inconsistent

**F17.1** — `weekly-w33-vuln-status-rollup`, `reliability: A`. sources.json letters for the outlets carrying the entry's load-bearing findings: bleepingcomputer **B**, securityweek **B**, hackernews **C**, checkpoint-research **B**. The entry's own sourcing_note concedes the exposure ("Where a status change rests on a single observer (Defused's ..., QUIRSO's ..., watchTowr's), that observer is named"). The sibling top-story entry, built on the same set, correctly carries **B**. Use B.

**F17.2** — `weekly-w33-looking-ahead`, `reliability: A`. The "six flaws with no fix" bullet rests entirely on cyberkendra.com, an aggregator blog that is not tracked in `sources/sources.json` at all, alongside securityweek (B) and calif (B). A ("no doubt of authenticity, trustworthiness or competency") does not describe that set. Use B.

### Editorial / less-is-more flags (advisory)

**F11** — "six flaws with no fix in existence" does not match either entry's own enumeration. Roll-up: ShieldBreak + three FreeBSD + GeoServer + "three of the five NatJack NAT primitives" = 8. Looking-ahead: ShieldBreak + three FreeBSD + three NatJack = 7, with GeoServer as a separate bullet. A reader adding up either list gets seven or eight. Make the number and the enumeration agree in both.

### Coverage assessment (no finding)

Soundness holds: every one of the 14 clears W-PD-1, none is a one-to-one re-list, `weekly-incidents-recap` is legitimately empty, and the three recorded drops are defensible on their stated grounds — the Recorded Future crypting-market survey is inventory rather than tradecraft for this audience; the NCSC-UK water-sector worked example is voluntary guidance with no clock and a prior weekly already carried the four-nation OT-isolation lane; and two retrospective enforcement items is genuinely too thin for a section when ACRO is carried inside the sector-patterns entry, where it is the strongest instance of that entry's own lens. No blind spot from any of those three. `actions: []` on all 14 is correct — no F18. No IOCs, no vanity metrics, English throughout, no `org_triage`, no `watchlist_hit`. The one completeness gap is F10.

### Verdict

NEEDS_FIXES (truth: 12, editorial: 7, advisory: 1)

### Findings summary (machine-readable)

See `work/2026-08-16T2315Z-weekly/verification.iter1.findings.yaml` (same payload, 20 records).
