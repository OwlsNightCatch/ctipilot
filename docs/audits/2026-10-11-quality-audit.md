# Quality audit, 2026-10-11

**Mandate.** This is the scheduled weekly quality audit under `prompts/quality-audit.md` (v4.19 at fire start, v4.20 at commit). It covers four things:
- truth re-verification of every entry the window touched;
- independent coverage re-sweeps;
- systemic and operational review;
- the monthly priority calibration, which no October report had run yet.

**Window.** The record anchor is the previous audit record, 2026-09-30T06:39Z (270.5 h). The last *full* audit, meaning the last one with coverage re-sweeps, was 2026-09-27T13:08Z, so the re-sweeps and the truth inventory were extended back to that time (systemic finding 1). The window closes at 2026-10-11T13:07Z.

**Run record:** [`runs/2026-10-11/2026-10-11T1307Z-audit.md`](../../runs/2026-10-11/2026-10-11T1307Z-audit.md). Working files are under `work/2026-10-11T1307Z-audit/`.

**Method.** 17 `cti-research` and `cti-verification` sub-agents, all reporting Sonnet 5.5 from their own prompt line:
- **Truth passes T1 to T8:** the 133 entries whose `discovered_at` or a changelog record falls in the window, including the five entries of the never-audited 09-27 to 09-30 stretch.
- **L1:** the next legacy batch of 20 entries from `tools/legacy_review.py`.
- **D1 and D2:** 43 entries in 17 groups of CVE-sharing duplicates and unfolded legacy "UPDATE" entries.
- **Re-sweeps G1a to G3b:** six passes, swept back to 2026-09-27, with ledgers of 25, 32, 26, 26, 27 and 36 sources, each fully attempted.

In total, 196 entries were verified against about 890 fetched primary URLs. The cited-page pre-pass checked 1,024 evidence quotes on 923 pages and 384 CVE citations on 234 pages before the passes started.

## Verdict

**35 of 196 entries clean.**

| Group | Entries | Clean | Imprecise only | Factual errors |
|---|---|---|---|---|
| Window | 133 | 35 | 84 | 14 |
| Legacy batch L1 | 20 | 0 | 0 | 20 |
| Consolidation D1/D2 | 43 | 0 | 3 | 40 |

The window entries are in reasonable shape, and the old store is not.

**Window entries.** Of the 133:
- 84 carry imprecisions: a sentence without its citation, a technique the body describes but `techniques[]` omits, a date one day off, or wording stronger than the source.
- 14 carry factual errors. Two of them changed the picture a reader acts on:
  - An encryption claim the source does not make (Kaspersky PAYLOAD).
  - A headline calling vendor-named exploitation new when the vendor had named it in July too (SonicWall SMA1000).

  The other twelve misread a source in a sentence or a field.

**Older store.** Every legacy entry checked carried at least one claim no source supports. 40 of the 43 entries in the duplicate groups did too.

**Repairs.**
- 27 duplicates were folded into 21 survivors, each survivor rewritten from its sources.
- Every CVE-sharing pair left without a link now has one, except one pair of legacy entries left for re-verification (watch items).
- 117 existing entries carry a record from this fire.
- One missed finding was recovered as a new entry (NeedyMantis).
- Two developments were recorded as updates (GitLab backports, NetScaler CVE-2026-88773 proof of concept).

**Pipeline health.**
- KEV coverage is complete: 10 additions in the window, all covered, no stale status and no unreflected ransomware flag.
- The source sweep found 237 of 238 sources relevant.
- Last audit's fixes held.

The real systemic defect was in the audit itself: its window anchor let a three-day stretch escape both audit halves. It is fixed in v4.20.

## Findings: false or erroneous published intelligence

### Window entries with factual errors (14)

Every row's fix is a `correction` record from this fire on that entry. Rows marked (internal) changed only metadata or citations.

| Entry | Defect | Ground truth | Fix |
|---|---|---|---|
| `2026-09-29/kaspersky-payload-gpo-encryptionless-ransomware` | Title, summary and analysis said the PAYLOAD ESXi binary was deployed and hit the Linux servers | Kaspersky found the sample on those servers; it does not say it ran or encrypted anything | correction; title, summary and body rewritten |
| `2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection` | Headline: vendor-named exploitation new this time; builds attributed to the SonicWall advisory | SonicWall named exploitation in July ("multiple cases") and September ("a case"); the builds come from The Hacker News | correction; headline and summary |
| `2026-09-29/microsoft-storm-2570-cross-raas-toolkit` | MeshAgent bridge placed after initial access; a change-window triage discriminator attributed to Microsoft; Admiralty letters in reader text | Microsoft: the bridge runs between initial hands-on-keyboard activity and later stages, and initial access is unconfirmed; the discriminator is not Microsoft's | correction; priority high to notable |
| `2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen` (+ folded twin) | Impacket activity framed as lateral movement; hunting lines named fields no source names; the twin cited AA23-250A, a Zoho/Fortinet advisory | Arctic Wolf: SMB reconnaissance that did not progress; Rapid7 and Unit 42 saw no lateral movement | correction; twin folded |
| `2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev` | CISA said to attach forensic-triage requirements; EPSS 0.81 | The KEV record's forensicTriage is "No"; FIRST EPSS is 0.0124 (0.81 was a percentage read as a probability) | correction |
| `2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin` | eSentire forecast "more successful attacks"; CWE and ransomware flag cited to the CISA alert; no labelled lines | eSentire forecasts more attempts, after every observed attempt failed; the CWE and flag are on the KEV record | correction; Exposure, Detection and takeaway lines added |
| `2026-09-17/kairos-libercourt-commune-ransomware-confirmed` | Listing dated on 2026-09-02; "three small municipal administrations" | The tracker discovered it on 09-02; Kairos lists at least four municipalities | correction (the T1486 mapping is kept; see the declined findings) |
| `2026-09-17/mandiant-ai-risk-resilience-report-2026` | Case studies misdescribed: the RAG case as an observed leak, the Shai-Hulud entry point, data-harvesting as credential harvesting; T1554 | Mandiant's own case-study wording | correction |
| `2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` | Two affected products | Advisory SEC-10986 (its JSON record) lists three, adding the DirectAdmin plugin, fixed in 1.2.3.238 | correction; advisory made primary |
| `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` | CVE-2026-53266's range left out the 7.0 train; CVE-2025-39682 had no lower bound | Kernel CNA record: 7.0.0 to 7.0.12 affected; first affected version 6.0 | correction (internal); the ChangeLog citations were confirmed correct |
| `2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence` | AMOS "confirmed"; "conference-targeted"; COM hijacking mapped | Huntress: "highly consistent with", later "appeared to be"; the recap calls the lure a volume play; NetSupport registers its own COM object | correction; title, takeaway and a contradiction line reflect the volume-play reading, T1055.012 added, T1546.015 dropped |
| `2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes` | Infrastructure rebuilt "within hours" | Computing UK: "repeatedly rebuilt"; no time given | correction; T1070.006 added |
| `2026-09-24/openai-agent-australia-medicare-portal-breach` | ACSC alert cited at its old address, which now names the moved page as canonical | The alert moved to `cyber.gov.au/alert/…` with the same text | correction (internal); citation, source and three evidence records re-pointed |

**Root causes.** The 14 errors share three mechanisms, and none is new:
1. **Summarising past the source.**
   - A composer's inference was written as the source's claim (Storm-2570, Kemp, Kairos, Kaspersky).
   - The verifier walked the claim but accepted the inference.

   The fix that exists is the claim ledger (v4.17). Its iteration-1 findings per entry doubled between the two model generations (systemic finding 6), so it is catching more, not less. These entries predate it or slipped through it.
2. **Numbers in the wrong unit.** EPSS was read as a percentage (Apple).
3. **A structured record not read** (Acronis JSON, kernel CNA ranges, KEV `forensicTriage`).

Both 2 and 3 are covered by the existing rule to read the structured record. No new rule is warranted; the classes are named here so the next audit can count them.

### Imprecisions (84 window entries)

The passes recorded these in `work/2026-10-11T1307Z-audit/truth-T1.yaml` to `truth-T8.yaml`. Each was fixed through a record when it was real and reader-visible:
- missing inline citations;
- unmapped described techniques;
- one-day date drift;
- "this entry" or "this constituency" in reader text;
- stale exploitation wording;
- labelled lines missing on older entries.

Findings declined, with reasons:
- **SonicWall CVE-2026-102255, F4 (version wording):** the entry follows SonicWall's own table.
- **Kiteworks, F16 (keep high):** the decision is the 2026-10-02 fire's, and it holds while the vendor-directed shutdown and the 9.8 account takeovers stand.
- **Nx/TanStack, F14:** the claimed omission is outside the cited source's scope.
- **Gambit, record-summary wording:** earlier records are append-only.
- **Em dashes the site already strips at render:** style only, outside the reader text this fire rewrote.
- **Low-confidence `public-sector` sector findings:** the constituency-relevance tag is the profile's call, not a source claim.
- **AFPA, F3 (citation dates):** the cited content arrived with the 2026-09-19 updates, so the dates are right.
- **Pentagon DMDC, F7 (length):** within the incident floor.
- **Bitget, techniques:** the two proposed ids rest on the company's hedged wording, which the page has since dropped.
- **nginx CVE-2026-42945 "exploited" status:** VulnCheck saw honeypot attempts only, so the status stays as published; the main analysis now dates NCSC-CH's "unknown" rating ahead of VulnCheck's report.
- **Kairos, T1486:** the commune itself calls the incident a ransomware attack ("attaque par rançongiciel"); no source describes encryption, so the mapping rests on that statement and is kept for the impact it names.
- **SonicWall CVE-2026-83548/83549, EPSS dating:** the stored EPSS values carry no as-of date; left for the next record that touches the entry.

### Legacy batch L1 (20 entries, 2026-05-08 to 2026-05-09)

All 20 carried claims their sources do not make. Each was re-verified whole and corrected where it stands, or rewritten from its sources when most of it was unsupported (Instructure Canvas, Dirty Frag). Each gained the Admiralty rating and ATT&CK mapping its kind now requires. Examples:
- The MuddyWater "Chaos as false flag" entry cited a Deep Instinct report that does not exist. It was rewritten from Rapid7's report, which links the Chaos-branded extortion, with no files encrypted, to MuddyWater with moderate confidence (rated B3).
- Copy Fail became `kind: vulnerability` with verbatim Xint evidence.
- LiteLLM gained Sysdig's exploitation evidence.
- The SEPPmail survivor gained the vendor's contact-page source.

The DENIC DNSSEC outage, a non-adversarial operational failure, was recorded as `policy`, the only kind that does not require an ATT&CK mapping, because no mapping is honest (recommendation 4).

Priorities moved down on ten entries: to routine for GLPI, xrdp, Spring, Kaspersky Q1, DENIC, ENISA, the German court ruling and Inditex; high to notable for Instructure Canvas and DAEMON Tools. The polyfill entry, a carried watch item, was also re-verified and rewritten this fire (watch items). The legacy queue now stands at **408 pending, 69 reviewed** (468 pending at fire start).

### Duplicate consolidation D1 and D2 (43 entries, 17 groups)

40 of 43 entries carried errors. 27 duplicates were folded with `tools/fold_entries.py` into 21 survivors, each brought to the verified state first:

| Folded into | Survivor |
|---|---|
| 4 entries | PAN-OS CVE-2026-0300 (2026-05-12; headline shortened) |
| 2 entries | Exchange CVE-2026-42897 (2026-05-18; it had named the wrong mitigation host and still said no fix existed, though one shipped in June; priority critical to high) |
| 2 entries | Cisco SD-WAN CVE-2026-20182 (2026-05-15) |
| 2 entries | Oracle EBS CVE-2026-46817 (2026-07-16) |
| 1 entry each | the rest |

The singles went into:
- Cisco SD-WAN CVE-2026-20245;
- nginx CVE-2026-42945;
- Netlogon CVE-2026-41089 (priority critical to high: Microsoft still reports no evidence of the exploitation CCB claimed);
- SEPPmail;
- 11 duplicates from May to July in 11 groups: Semantic Kernel, PHP SOAP, n8n, Ghost, FortiClient EMS, Cisco UCM, Everest Forms, SimpleHelp, Splunk, SD-WAN CVE-2026-20262 and ISE CVE-2026-20181/20190;
- PAN-OS CVE-2026-0257 (the RANSOMWARE row the 10-05 fire left pending a fold);
- the CVE-2026-50751 twins, which disagreed about which CVE was exploited.

Distinct findings that share a CVE are now linked through `references[]`: the Pwn2Own DEVCORE chain against Exchange CVE-2026-42897, SAP August against nginx, and every other unlinked pair the scan found. A re-scan finds **one unlinked CVE-sharing pair** (43 at fire start): the 2026-05-30 Nightmare Eclipse entry and the 2026-05-15 YellowKey entry, both legacy. The verifier found the 05-30 entry wrong in several places, so the link waits for that entry's re-verification (watch items). The build keeps every folded permalink as a redirect.

## Findings: missing or incomplete coverage

The six re-sweeps confirmed 89 findings as covered and returned 79 items that needed a decision. They had already dropped 69 further leads with recorded reasons. The window's fires had disposed of most of the 79 as a `borderline-drop`; the audit re-checked each against PD-11.

### Recovered

**NeedyMantis (new entry `2026-10-11/needymantis-modular-post-compromise-framework-storm-3069`, notable, B2, single-source).** Microsoft Threat Intelligence's 2026-09-28 analysis covers:
- a China-origin modular post-compromise framework, found by pivoting from the DAEMON Tools supply-chain investigation;
- intrusions at telecoms, universities, intergovernmental organizations and government contractors;
- Storm-3069 as one operator.

Three fires (09-30, 10-02, 10-03) dropped it as "out of window", but msft-ti is a rotational source and a post a few days old sits inside the PD-7(d) lookback. The re-sweep also hit a transport limit: `msft-secblog recent` returns only the newest 10 posts, which on the audit's 11-day lookback no longer reached the 09-28 post. The `msft-ti` recipe note now pairs it with the topic page for long lookbacks.

The DAEMON Tools legacy entry, rewritten in this fire's L1 batch, is linked from the new entry. The registry gains `malware:needymantis` and `actor:storm-3069`, and the DAEMON Tools incident is `attributed-to` Storm-3069, each edge sourced to the new entry.

**GitLab CVE-2026-85706 / CVE-2026-87719 backports (`update` record on `2026-09-12/cve-2026-85706-gitlab-unauth-path-traversal-file-read`).** GitLab shipped fixes to 19.0.9 and 18.11.12 on 2026-09-23, which the entry's fixed-version list lacked.

**Citrix NetScaler CVE-2026-88773 (`update` record on `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev`).** Belgium's CCB reported a public proof of concept on 2026-10-06 for this unauthenticated request-smuggling flaw (CVSS 4.0 9.3), with no exploitation seen. The flaw's status gains `poc-public`, and the September fixed builds already close it.

### Correctly droppable (the fires' reasons stand, or the audit's own call)

**Unexploited vendor bundles: the PD-11(b) drops stand.** None was reported exploited and none is on KEV:
- Cisco 2026-10-07: unauthenticated root RCE on Nexus 3000/9000 through NX-API, MPLS OAM and NGOAM;
- HPE ClearPass (seven CVSS 9.8 flaws), AOS-S and Instant On;
- IBM Verify Identity Access;
- Splunk SVD-2026-1001;
- Veeam Backup Viewer to SYSTEM;
- ILIAS;
- WatchGuard;
- Bricksforge;
- the GitLab 19.4.1 release;
- Zimbra password recovery;
- the Exchange out-of-band OWA EoP.

HPE Instant On was never assessed by a fire, and G1a assessed it: fixes are pushed automatically through the cloud portal and HPE reports no exploitation.

G1a found the 10-08 Cisco drop resting partly on an unsupported premise ("NGOAM off by default"; Cisco says only that NGOAM must be enabled). The drop still holds on exploitation status. Whether bundles of this class should publish at high, as many September ones did, is recommendation 1.

**Already-covered findings, no new decision:**
- the Kiteworks CVE assignment (NCSC-NL lists the 61 CVE ids for the 2026-09-30 release the entry already directs to);
- Horizon3's Rejetto HFS mechanism write-up (same fix, honeypot-only attempts);
- the Metabase detail on ANSSI's own and DINUM's instances (same CVE and fix as the REACTIV entry).

**Law-enforcement actions with no defender decision:**
- the NRW infiltration of Qilin and the extradition from Japan of a suspected developer ("Operation Albus");
- the FBI arrest of a ransomware negotiator in the ShinyHunters case;
- the French dismantling of the Reacher/Stryxx lookup platform;
- the MonsterCloud indictment.

**Incidents below the incident floor** (no vector, actor or behaviour public):
- SRG SSR staff data;
- Ricardo;
- the T-Systems test system;
- LMU Munich;
- the Hauts-de-France suppliers;
- CNAF/VACAF;
- AP-HP;
- Saint-Pierre-des-Corps;
- Fakturownia;
- DTU;
- the Brandenburg memorials foundation's second outage.

**Claim-only items (PD-6):**
- the rolling French forum leak claims;
- the University of Rostock listing;
- the SafePay Swiss tempo (8 Swiss listings, 2 confirmed; the ARA Lyss-Limpachtal row stays on the backlog to 10-14);
- the Silent Ransom Group chat leak (unverified provenance).

**Statistics or awareness only:**
- MDDR 2026;
- the Zscaler ransomware report;
- GTIG vulnerability trends;
- ReliaQuest's quarterly;
- the HSLU/Fribourg measurement of Swiss communal mail authentication (DMARC enforced on 13.4 %). The 10-06 fire judged this a hardening baseline with no near-term decision; the audit upholds it as a judgment call, since it is the one item squarely about the constituency.

**Regional scope or no new capability:**
- TA419;
- ARTEX;
- MATCHBOIL;
- UAT-11985;
- the DragonForce second backdoor;
- Huntress Akira;
- MSP360 to ScreenConnect;
- the TeamViewer TV-2026-1010 flaw (authentication needed, not exploited);
- GlassWorm themes;
- the AISI GPT-6 simulation;
- DarkSword.

**Held on the backlog:**
- Beyond Gravity, the Confederation-owned space supplier, stays on its 10-06 hold (to 2026-10-20): no vector, actor or data has been published.
- Guardium CVE-2026-85542 stays held to 10-14 and is re-gated by the next fire.

### Coverage-adjacent gaps

The re-sweeps hit these feed caps, which bound how far back a single fire can see after an outage:
- bsi-de (250 items reach only 10-08);
- cccs-alerts (50 items reach 10-01);
- CERT-FR avis (40);
- NCSC-NL (25);
- `msft-secblog recent` (10).

The 10-02 fire's outage backfill used vendor listings for that reason.

Three pages were unreadable on every rung:
- the presseportal.de Hamburg police release (captcha or 503);
- three community.citrix.com blogs (403);
- the F5 K000161019 and BSI WID-SEC-2026-1536 pages (D1).

## Findings: systemic and operational

### 1. The audit window let a stretch escape both halves (fixed, v4.20)

`LAST_AUDIT` was the newest audit record of any kind. The partial audits of 2026-09-29T2134Z and 2026-09-30T0634Z/0639Z (source repairs and a correction run, with no re-sweep) each moved it. So 2026-09-27T13:08 to 09-30T06:39 was never re-swept, and five entries published in it were never truth-checked:
- WWAHost (the 09-27 audit's own recovery);
- Storm-2570;
- Manno;
- Star Blizzard;
- Storm-3068.

NeedyMantis was published by Microsoft inside that stretch. A partial audit could also have tripped the 72-hour duplicate guard and cancelled the scheduled full one.

This fire extended the re-sweeps and truth inventory by addendum. v4.20 anchors the window on the newest audit whose record carries a `G…` re-sweep key and lists later partial audits for carry-forward. The duplicate guard now measures from the last full audit.

### 2. The one-time page-check backfill would have re-run forever (fixed, v4.20)

Step 5b's clause looked for the string `--page-checks-since` in the audit reports. The 2026-09-29 report records its backfill (from 2026-07-01) in prose, so every audit would have re-run it. This fire ran it from 2026-09-01 (255 entries; 923 pages for the quote check, 234 for the CVE check). The clause is removed, with a note that the backfill is done.

### 3. Two false-positive classes in the cited-page gate (fixed)

- **Mastodon posts.** On a JS-shell page such as a CERT-Bund post on social.bund.de, the text lives only in the `description` and `og:description` meta tags, and the tag strip deleted it. Two verbatim Exchange MRSProxy quotes were flagged.
- **Image-only PDFs.** `tools/fetch_source.py pdf` "extracted" ANSSI's image-only CERTFR-2026-CTI-006 as 467 KB of JPEG bytes, because an uncompressed image stream held the bytes `BT` and `Tj`. The CVE-citation check then searched those bytes and flagged CVE-2026-72898.

Both are fixed, with a new test for the PDF case (14/14 pass). A re-run of the page checks from 2026-08-29 (314 entries) ends with every citation-cve check passing (421 found on their page, 68 not machine-checkable). The one quote-literal warning it raised was Bitget's incident page, which the company edited after publication ("Updated: October 3, 2026", hedges removed); the evidence quote now follows the page's current wording, which clears it.

### 4. Fires that did not happen

- **10-01 intel fire: no record.** The 10-02 fire's 48-hour gap and window, with S3's outage-backfill sweep, self-healed the coverage. The KEV diff and the re-sweeps found nothing lost.
- **10-04 scheduled audit: no record.** The weekly Sunday audits fired 09-20 and 09-27. The 09-30T0639Z operator session stayed open until 10-04T11:30Z. This is an availability signal for the operator, not a cadence judgment (recommendation 3).

### 5. The older store is the quality problem now

The window is mostly sound: 14 of 133 entries had factual errors, and 84 more had imprecisions. The legacy and duplicate batches are not: 60 of 63 entries were wrong.

This is the third audit in a row to find this, after 2026-09-30 and its correction run. At about 20 legacy entries a week, the 408-entry queue takes about five months, while the reader's search, entity pages and agent endpoints serve those entries today (recommendation 2).

### 6. Model-generation baseline (Phase 3 item 9)

Intel fires on Sonnet 5 (2026-09-22 to 09-29) against Sonnet 5.5 (2026-09-30 to 10-11):

| | Sonnet 5 (n = 8) | Sonnet 5.5 (n = 11) |
|---|---|---|
| Fire duration, median | 2.50 h | 2.79 h |
| Verifier iterations, mean | 7.2 | 5.6 |
| Confirmed double-CLEAN | 3/8 | 5/11 |
| Iteration-1 truth findings per entry touched | 0.78 | 1.55 |
| Research sub-agent duration, mean | 9 min | 23 min |
| Research items returned per fire | 9.8 | 25.2 |

The confound: v4.17's claim ledger landed with the model change. Iteration 1 now walks every claim instead of sampling, so the higher finding rate and faster convergence cannot be attributed to the model alone. The research workers go deeper (2.6 times the items) for 2.5 times the time, and fire duration rose 12 %. Recommendation: keep the current effort setting, since convergence improved: two of the eleven Sonnet 5.5 fires ended at the eight-iteration cap on NEEDS_FIXES, against four of the eight Sonnet 5 fires.

### 7. Fix effectiveness and discipline: clean

**Last audit's fixes held:**
- `kev-window.txt` was written by all 10 fires (v4.10).
- The PAN-OS CVE-2026-0257 RANSOMWARE row surfaced on 10-05 and was dispositioned on 10-06 (v4.19); its fold landed in this fire.
- `cisa-advisories` was swept by 10 of 10 fires, `cisa-news` by 3 and `cisa-directives` by 2, which is rotation, not breakage (v4.18).
- Top-of-entry drift after a record, the 09-29 watch item: of the window's 41 reader-facing `update` records from fires, 39 moved the title, headline or summary. The two that did not are from the 09-29 fire (Kiteworks, Citrix), and both were re-verified this fire.

**Discipline over the 34 new October entries:**
- `actions[]` lengths 0/1/2 = 19/6/9 (empty is the norm).
- Priority 2 critical, 6 high, 23 notable, 3 routine.
- Ratings B2 15, A2 13, A1 4, B1 2.
- Mean techniques as published: threat 10.6, vulnerability 4.5, incident 2.8, research 2.7 (after this fire's records, threat 10.9 and incident 3.0).
- Exploitation-consistency passes on every window entry.
- 30 non-product entities first seen in October, one attached from prose only (a genuine mention).

**Gaps left for the fires:**
- Seven entries exceed the `entry-shape` length guide (nine WARNs): seven main analyses over 550 words, two of which (Zammad, Denmark CPR) also carry 125-character headlines. The check WARNs only in a fire's own scope, and the fires shipped them. They are listed for the fires to see, not cut by the audit.
- The NCSC-CH dead-link watch item is resolved: no entry cites `ncsc.admin.ch/ncsc/` any more.

### 8. Sources

The sweep this fire probed 238 sources:
- 237 relevant;
- threatpost stale (demoted and archive-only since 2022, as its record says);
- no repair order open.

The re-sweeps' recipe notes fixed 13 records:
- **Feed recipes** for jpcert, elastic-seclabs, kaspersky-securelist, proofpoint, malwarebytes, socket-dev-blog and frenchbreaches.
- **Notes**:
  - `msft-ti` (the 10-item cap of `msft-secblog recent`);
  - `redcanary` (its blog now redirects to Zscaler);
  - `chrome-releases`;
  - `heise-sec`;
  - `ccb-belgium` (`extract` reads the listing and pages);
  - `eset` (its feed recipe also reached `main` through a later fire).

Candidate sources the re-sweeps proposed, not added this fire:
- UK AISI blog;
- veeam-kb;
- hashicorp security bulletins;
- Apache httpd vulnerabilities;
- solutions-numeriques;
- leto-legal-news;
- presseportal-ch.

### 9. Registry drift

Three registry summaries still carried claims their entries had since corrected (DENIC, MuddyWater, DAEMON Tools), and the polyfill incident's name and summary carried the defanged domain. All four are rewritten. `tools/sync_products.py` added 20 product entities from the rewritten entries' `affected_products[]` and moved 11 existing product records' `first_seen` dates earlier.

### 10. Taxonomy gap for non-adversarial items

DENIC's DNSSEC outage has no adversary. Its kind options are:
- `incident` or `threat`: need ATT&CK ids (FAIL);
- `research`: WARNs when empty;
- `policy`: whose definition does not fit.

It was recorded as `policy` (recommendation 4).

## Priority calibration

No October report carried this section, so this fire owns the monthly review.

| Scope | n | critical | high | notable | routine |
|---|---|---|---|---|---|
| Store (997 entries before folds) | 997 | 30 (3 %) | 408 (41 %) | 540 (54 %) | 19 (2 %) |
| August 2026 | 196 | 1 | 96 (49 %) | 98 | 1 |
| September 2026 | 128 | 13 (10 %) | 36 (28 %) | 66 | 13 |
| Trailing 30 days | 113 | 10 (9 %) | 20 (18 %) | 67 | 16 |
| October 1 to 11 | 34 | 2 (6 %) | 6 (18 %) | 23 | 3 |

**Movement.** September's `high` share fell from about 50 % mid-month to 28 % after two changes: v4.17's exposure-graded `high` bar, and the 09-30 audit's 36 recalibrations (23 high to notable, 2 high to routine, 11 notable to routine). October holds at 18 %. The store-wide 41 % is the legacy corpus, which carries the v2-era bar. This fire's legacy and duplicate repairs moved it further:
- Exchange CVE-2026-42897 and Netlogon CVE-2026-41089: critical to high;
- Instructure Canvas, DAEMON Tools, polyfill, Storm-2570, Storm-3168 and ShieldBreak: high to notable;
- eight legacy entries, Virtualizor, the G7 warning (high), and PHP SOAP, n8n, Cisco ISE CVE-2026-20181/20190, RoguePlanet and the Pwn2Own DEVCORE result (notable): to routine.

**F16.** The month's run records carry 12 priority findings, six of them in October:
- Kiteworks: keep high (declined, 10-02);
- Belnet: to routine;
- Liechtenstein: high to notable;
- Citrix CVE-2026-107406: high to notable;
- PaperCut: critical to high (patched for over a week, no new exploitation);
- IDC Frontier: to routine.

All lean generous, and none under-alerts.

**Criticals.** September and October carry 15. Every one is an exploited or KEV-listed flaw on internet-facing infrastructure the constituency runs:
- JFrog (two);
- MikroTik;
- N-able;
- Magento;
- Check Point (two, one of them the VPN);
- Cisco SEG, ISE and SD-WAN;
- Arista VeloCloud;
- F5 APM;
- WordPress;
- Citrix NetScaler;
- FortiMail.

The September rate (10 %) tracks a heavy month of edge exploitation, not a drifted bar, and October's 6 % is moving back toward the store's 3 %.

**Verdict.** The bars hold, and no calibration edit to `prompts/cti-run.md` ships. One inconsistency is real and left to the operator (recommendation 1). Several unexploited critical vendor bundles in September published at `high`. October's fires dropped the same class under PD-11(b): Cisco's 2026-10-07 Nexus bundle, HPE ClearPass, IBM Verify Access and Splunk SVD-2026-1001. Either is defensible; both together are not.

## Fixes shipped in this commit

- **Prompts v4.20** (`prompts/quality-audit.md`, banner bump in both master prompts, `prompts/CHANGELOG.md`):
  - the window anchors on the last full audit;
  - partial audits are listed for carry-forward;
  - the duplicate guard measures from the last full audit;
  - the stale backfill clause is removed.

  `docs/architecture.md` follows.
- **`tools/check_run.py`:** the cited-page check keeps description meta text, so Mastodon posts are quote-checkable.
- **`tools/fetch_source.py`:** the PDF reader skips image streams. New test in `tools/test_fetch_source_pdf.py`.
- **Entries:**
  - 117 existing entries carry a record from this fire;
  - 27 duplicates were folded (their permalinks redirect);
  - one entry was recovered (NeedyMantis).
- **`sources/sources.json`:** 13 records, with seven feed recipes and six notes (a later fire had already switched eset to its feed, so this fire's change there is the note).
- **`entities/registry.yaml`:**
  - `malware:needymantis` and `actor:storm-3069` with sourced relations;
  - the DAEMON Tools incident `attributed-to` Storm-3069;
  - four summaries corrected (DENIC, MuddyWater, DAEMON Tools, polyfill);
  - 20 product entities from `tools/sync_products.py`, which also moved 11 product `first_seen` dates earlier.
- **`state/cves_seen.json`:** CVE-2026-55008 added, five titles refreshed after the folds.
- **`state/legacy_review.json`:** the L1 batch, the consolidation entries and the polyfill entry are marked. The queue went from 468 to 408 pending.
- **`state/source_health.json`:** unchanged; the 2026-10-18 weekly snapshot on `main` supersedes this fire's 2026-10-11 sweep, whose result (237 of 238 relevant) the run record summarises.
- **Warning sweep.** `check_run.py --all` started at 1 warning and 23 acknowledged. The one warning, the 09-30T0639Z audit record's 100.8-hour duration, is acknowledged in `state/warning_acknowledgments.json`: an interactive operator session that paused on API usage limits, so settled history on an immutable record. No other acknowledgment was added or removed.

## Recommendations (operator decisions, not shipped)

1. **Unexploited critical vendor bundles.** Decide whether a bundle of unauthenticated CVSS 9.8 flaws on infrastructure the constituency runs publishes without exploitation. September published several at `high`; October drops them under PD-11(b). The prompt can then say which.
2. **Legacy repair pace** (carried from 2026-09-30, sharpened). 60 of the 63 legacy and duplicate entries checked this fire were wrong, and 408 remain at about 20 a week. One or two dedicated repair runs (the same mechanics, 60 to 80 entries each) would clear the oldest months in weeks. Your call on cost.
3. **The 2026-10-04 audit did not fire.** Check the routine's schedule; the operator session that ran until 10-04T11:30Z may have held it. With v4.20 a partial audit no longer moves the window, so a missed full audit costs a longer window, not a blind stretch.
4. **Non-adversarial items.** Decide whether resilience incidents without an adversary (DENIC's DNSSEC outage) stay in scope. If they do, add a kind, or a rule exempting them from ATT&CK mapping; `policy` is a stopgap.
5. **Red Canary** now redirects to the Zscaler blog and its feed stopped on 2026-08-20. Retire or repoint the record.
6. **`ssd-disclosure`** stays blocked on every transport. Accept the gap or drop the record.
7. **Google TAG and Mandiant/GTIG overlap** (carried from 2026-09-29): consider folding `google-tag` into `mandiant-gtig`.

Retired:
- 2026-09-29 recommendation 1, CISA transport (adopted in v4.18);
- 2026-09-29 recommendation 2, the IT half of CISA advisories (v4.18's `WebFetch` recipe);
- 2026-09-29 recommendation 4, effort measurement (the baseline is in systemic finding 6).

## Watch items

- **Legacy queue.** 408 pending. Resolution: queue empty.
- **Non-CVE duplicates.** The CVE-sharing scan is at zero, but actor and incident twins without a shared CVE escape it. Known candidates:
  - the RoguePlanet entries of 2026-06-19 and 2026-07-09;
  - the 2026-05-17 Pwn2Own roundup, which itself needs legacy re-verification before any fold.

  Resolution: folded or linked.
- **Nightmare Eclipse 2026-05-30 (legacy).** This fire's verifier found it wrong in several places: Microsoft's statement is the MSRC blog of 2026-05-27 rather than a Digital Crimes Unit statement of 28 to 29 May, The Record says Microsoft stopped short of threatening legal action, June's Patch Tuesday fell on 9 June, most of its technical detail is uncited, and YellowKey is typed as a local privilege escalation although it is a physical-access BitLocker bypass. The link to the 2026-05-15 YellowKey entry waits for its re-verification. Resolution: re-verified ahead of the queue order, rewritten from its sources and linked.
- **`webfetch-only` sources and their quotes** (carried from 2026-09-30). These quotes rest on the verifier's hand check. Resolution: a direct transport for cisa.gov, or none needed.
- **Publisher revisions** (carried from 2026-09-29). This week's case is Bitget's incident page, edited 2026-10-03. Resolution: the weekly pre-pass keeps catching them; a 90-day re-run is still open.
- **Backlog rows due this week.** Guardium CVE-2026-85542, ARA Lyss-Limpachtal and Payload/Netech (all to 10-14), and Beyond Gravity (to 10-20). Resolution: dispositioned by the fires.

Closed this fire:
- **Duplicate consolidation:** closed, except the one pair in the Nightmare Eclipse item above.
- **Polyfill defanged indicator:** the entry is rewritten without it, and its advice to move the script to the relaunch domains is withdrawn.
- **KEV RANSOMWARE rows:** dispositioned by the fires, as designed.
- **Top-of-entry drift:** 39 of 41.
- **NCSC-CH dead links:** none left.
- **Three unreadable sources:** v4.18.
