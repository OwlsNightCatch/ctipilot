# CTI quality audit, 2026-09-29 (operator-directed)

**Mandate.** An out-of-cycle audit the operator directed on 2026-09-29: fix every open warning and error as an audit would, correct the two published quote defects the gate had surfaced (MovieReaper, European Court of Auditors), clear the two leftover warnings from the morning fire (eight Oracle products not yet registered, a 3.1 h fire duration), and check every source in detail so that each one works and returns relevant content, with health checks that test exactly that. Window **2026-09-27T13:08Z → 2026-09-29T21:34Z** (56.4 h), anchored on the previous audit. The cited-page backfill ran wider: first over every entry active since 2026-09-01, then over every entry active since 2026-07-01. Run record: [`runs/2026-09-29/2026-09-29T2134Z-audit.md`](../../runs/2026-09-29/2026-09-29T2134Z-audit.md). Prompt v4.16 (v4.13 to v4.16 were shipped during this session, see § Fixes shipped).

**Method.** Seven sub-agents on Sonnet 5.5. Three source-repair workers (`cti-research`, SR1 to SR3) diagnosed each source the first content sweep flagged, reading it through its own recipe and every alternative transport. Four cited-page triage passes (`cti-verification`, T1 to T4) fetched the page behind every `quote-literal` and `citation-cve` flag and classified it: not verbatim, revised by the publisher, cited to the wrong page, or a checker false positive. Three full content sweeps of all 190 sources. Every entry change in the main context, each re-read against the live primary. Eight cold verifier passes then read all 43 changed entries, this report and the run record. The loop reached its cap without a clean verdict and published under the fail-open rule, with a residual count of 10. The fixes for the last pass's findings were made after the cap and have not been re-verified (run record, verification block).

---

## Verdict

**The store's quotations were mostly sound, and where they were not, the usual cause was the publisher's page changing under the entry.** The cited-page check now finds more than 1,680 evidence quotes verbatim on their cited pages across every entry active since 2026-07-01 and reports no remaining mismatch. Over the entries active since 2026-09-01, binding publisher-only quotes to the entry's own sources raised the number of checked quotes from 248 to 633. Its flags plus this audit's own re-reads found defects on 43 entries. A minority were the pipeline's own quoting errors: a sentence Unit 42 never wrote left in the evidence list after a 2026-08-02 correction, quotes spliced across attribution clauses or omitted sentences (Proofpoint, OffSeq, Google GTIG via Krebs, Kaspersky), dropped or hardened hedges (Claroty, Kudelski, BlueMoon), an attacker's claim presented as the regulator's finding (CNIL) and CVE ids cited to pages that do not carry them. Most were publishers revising pages after publication.

**Thirteen revisions carried news the entries had missed: two on critical-priority entries, one on a notable entry and the rest on high.**
- Siemens revoked its Mendix advisory on 2026-09-22 and the CVE was rejected, while an entry still told readers to re-architect Mendix access control.
- PaperCut replaced its emergency patches with tested maintenance releases on 10 September, and the critical PaperCut entry still pointed at Emergency Patch Release 3.
- Check Point widened CVE-2026-85103 to every Security Management Server whatever its configuration and published a Remote Access VPN mitigation the critical entry said did not exist.
- Cisco replaced the ASA/FTD and the FMC hot fixes with hardening releases (two entries) and removed its "rotate every credential" guidance for FMC.
- GeoServer's SQL injection was assigned CVE-2026-76904, while the entry's title still said "no CVE and no patch".
- The nginx CVE-2026-42533 proof of concept (crash, leak and RCE modes) went public, while the entry said it was withheld.
- The Gridbox 2.20.2 batch published in full, and two more of its CVEs (CVE-2026-65887 and CVE-2026-65888, both 10.0) are rated Attacked, while the entry carried neither.
- WatchGuard fixed the 12.5.x branch the CVE-2026-13368 entry called unresolved. Tobit says Rollout 528 disables the TeamDavid functionality behind 22 CVEs. VenariX tied two Metabase victims to Dire Wolf. ENISA's post-launch FAQ documented a defect in the CRA platform's 72-hour counter. WatchGuard re-rated two Fireware CVEs as having no preconditions.

**Sources: 162 of 190 returned relevant, current content on the first content sweep, and 185 do now.** The old probe reported every one of the other 28 as healthy because it tested reachability only. Of the 28, 23 now return relevant content after repairs, two are demoted (the `threatpost` archive, and `paradigm-shift-research`, whose blog was pulled), and three remain unreadable in the container for want of a transport, which is an operator decision.

---

## Findings: false or erroneous published intelligence

Every change is a changelog record on the entry, one per entry for this run. Records marked internal carry no reader-facing section.

| Entry | Defect | Record |
|---|---|---|
| 2026-07-29 Siemens Desigo CC / Mendix | Mendix advisory SSA-814963 revoked on 2026-09-22, CVE-2026-7891 rejected. The entry carried the CVE, the product and a Mendix action. | update |
| 2026-07-31 Unit 42 autonomous-AI campaign | A quotation Unit 42 did not write stayed in the evidence list. The title, summary, headline and opening analysis said the three NetScaler cases were the only confirmed compromises, although Unit 42 also confirms 11 Marimo endpoints. | correction |
| 2026-07-30 Amazon DPRK npm attribution | Amazon corrected its post on 2026-08-11: the maintainer social engineering applies to debug, chalk and axios only. The entry applied it to every compromise. | correction |
| 2026-08-23 SPECTRE (UAT-10147) | Talos removed the EDR product names the entry attributed to it. | correction |
| 2026-08-28 Manchester Airports Group | The spokesperson statement was cited to a reworded help page, and the analysis still said the incident was unclaimed with no known vector. | correction |
| 2026-09-18 MovieReaper | Kaspersky revised its report. All three quoted passages, the Victims-section list and the distribution description changed. The analysis also misdescribed the third stage's masquerade (an Edge-named binary in a Telemetry folder). | correction |
| 2026-09-04 CNIL fine, Hôpital privé de la Loire | The title, headline and analysis called the account the attacker used a physician's, which was the attacker's own claim. CNIL says only "a single user account". | correction |
| 2026-09-10 BlueMoon exploit kit | The analysis called the kit's spread deliberate distribution. Proofpoint says the kit is shared and could not determine the channel. | correction |
| 2026-08-28 TeamPCP arrests | The headline and analysis called the AFP, FBI and WA Police action TeamPCP's first law-enforcement disruption, which neither source states. The GTIG quotation was also joined across its attribution clause. | correction |
| 2026-08-28 Kudelski, Bismarck | The analysis stated Kudelski's hedged "may have" as "most plausibly" and narrowed it to Bismarck alone. | correction |
| 2026-09-23 ECA NIS2 report | Quotes were cited to a landing page instead of the PDF. The audit scope named the wrong mechanism, and the summary overstated the NIS2 transposition finding. | correction |
| 2026-09-06 agent collusion (collusion.wiki) | A distinction the publisher only says it believes was stated as explicit. | correction |
| Top-of-entry state left behind (five entries) | ShareFile (title said no root cause and no patch, both published 2026-07-14), VMware VMSA-2026-0006 (summary said none exploited, CVE-2026-59310 KEV-listed 2026-08-18, and QUIRSO's single-appliance CVE-2026-59309 finding was missing), WP2Shell (title said exploitation expected, KEV-listed 2026-07-21), NetScaler CVE-2026-19490 (summary said no exploitation, KEV-listed 2026-09-09), Kaltura mwEmbed (first action said no vendor fix, patched 2026-08-28). | correction |
| 2026-08-28 Zalktis PEPPOL e-invoicing | Rated high for a vendor-patched, unexploited flaw in a Latvian desktop product. Now notable. | correction |
| Quoting and citation form (13 internal improvements) | GhostLock, RSFiles, PraisonAI, July Patch Tuesday, OctLurk, Windchill, TrueConf, Claroty, Group-IB (Nimbus Manticore), Proofpoint (TA4922), Tenable and Taiwan ACS, Wiz, MikroTik: quotes aligned with the live text, splices split, hedges restored, translated quotes marked and given their originals, CVE ids re-cited to pages that carry them, a live counter and superseded CISA wording dated. The same kind of fix on the entries in the other rows (Zalktis, Kaltura, VMware, WP2Shell, ShareFile, NetScaler, Gridbox) rides in that entry's own record. | improvement, internal |

## Findings: missing or incomplete coverage

| Entry | What the entry missed | Record |
|---|---|---|
| 2026-08-29 PaperCut NG/MF (critical) | Maintenance releases 26.0.5, 25.0.13 and 24.1.10 replaced the emergency patches on 10 September. The immediate action, actions and fixed-version fields still pointed at Emergency Patch Release 3, and the KEV listing of 2026-08-31 was unrecorded. | update |
| 2026-09-10 Check Point VPN certificate flaws (critical) | Every Security Management Server is vulnerable to CVE-2026-85103 whatever its configuration. A Remote Access VPN mitigation now exists, and pre-shared-key-only communities are not exposed to CVE-2026-85102. | update |
| 2026-08-15 GeoServer jsonArrayContains | Assigned CVE-2026-76904 (CVSS 9.8). Title, summary, headline and first action still said no CVE and no patch. | update |
| 2026-07-20 nginx CVE-2026-42533 | The proof of concept and full write-up are public, and the revised write-up puts a single exploit attempt on a stock deployment at about two thirds, down from the original post's 10/10. | update |
| 2026-08-12 Cisco ASA/FTD CVE-2026-20349 | Hardening releases replace the hot fixes (advisory v1.1, 2026-09-16). | update |
| 2026-07-30 Cisco Secure FMC CVE-2026-20316 | Hardening releases replace the hot fixes. The "rotate every credential" guidance was replaced with "contact TAC", with a warning that the fix does not address an existing compromise. | update |
| 2026-07-03 WatchGuard CVE-2026-13368 | T15/T35 fixed in 12.5.19 and EUCC in 12.11.9, and the affected range on the standard platform narrowed to 2025.1 to 2026.2. The advisory moved to psirt.watchguard.com. | update |
| 2026-08-09 TeamDavid (22 CVEs) | The vendor says Rollout 528 (30 June) disables the affected functionality. InfoGuard revised its post on 2026-09-25, and the CVE records now give every build before Rollout 528 as affected, up from "through Rollout 524". | update |
| 2026-08-09 Metabase CVE-2026-72898 | Fifteen confirmed downstream victims, two tied to Dire Wolf. The title still said no CVE was ever assigned. | update, `actor:dire-wolf` registered |
| 2026-07-26 Gridbox for Joomla | All eleven CVE records of the 2.20.2 batch published. Four are rated Attacked, and two of those (CVE-2026-65887 password reset, CVE-2026-65888 social login, both 10.0) were missing from the entry. Gridbox 2.20.3.1 (21 September) also fixes an unauthenticated blind SQL injection with no CVE yet, so the action now points at 2.20.3.1. | update |
| 2026-08-31 WatchGuard Fireware IKE | Two CVEs re-rated as unauthenticated with no preconditions. | update |
| 2026-08-29 EU CRA reporting | Platform live, portal address, EU Login MFA, and a 72-hour counter defect. | improvement |

**Not gaps.** WordPress 7.1.2 is covered by the 2026-09-24 entry on CVE-2026-87902. WordPress 7.1.1 (11 fixes, mostly authenticated, none exploited, delivered by auto-update) does not clear the relevance gate. **Handed on:** Apple CVE-2026-86950 (CoreGraphics, CISA KEV 2026-09-29) has no entry yet. It falls to the next intel fire's KEV-window duty.

## Findings: systemic and operational

### 1. "Healthy" meant "answers", and 28 sources answered with nothing usable

The probe recorded HTTP status and a byte count, so a JS shell, a bot wall, a homepage served for a moved listing, a feed of general news and a publisher silent since spring all read as green. The first content sweep classified 28 of 190: 11 stale, 7 irrelevant, 5 shell, 5 unreadable. One is the demoted `threatpost` archive. The rest had five root causes:
- Recipe drift. Google TAG's URL now redirects to the generic security blog, BfV's recorded path serves the homepage, CCN-CERT moved domains, and Adobe's bulletin index became a stub.
- Client-rendered listings read as HTML (CERT.at, ACN, Sansec, WithSecure, malware.news).
- The wrong surface of a working source (EDGAR, EUVD, ICO).
- Ordinary low cadence mistaken for a dead source (Project Zero, Exodus, XLab).
- False positives of the new check itself (IBM X-Force's hub, whose own metadata date is old, and swarmcha.se's three-link static index). Their records now carry the diagnosis, and the three CISA records note that WebFetch reads their listings, which CLAUDE.md forbids.

28 source records were changed: 27 of the 28 flagged sources (every one but `threatpost`) and `lab52`, whose HTML listing a later sweep read as stale and which now reads its feed. 23 of the flagged sources now return relevant content, `paradigm-shift-research` was demoted (the blog was pulled), and `cisa-directives` and `ssd-disclosure` were changed but stay unreadable. `tools/source_health.py` now reads every source through its own recipe and gives a content verdict with evidence (v4.16).

### 2. The PDF reader returned mojibake for Microsoft Word advisories

`fetch_source.py pdf` merged every font's ToUnicode map into one table and chose one decode for the whole file. Word writes spaces through a simple font and every other glyph through Type0 fonts whose codes are glyph ids. The byte-wise decode therefore turned "North Korean" into "1RUWK.RUHDQ" and dropped every digit. Because it also decoded embedded font programs as "prose", it outscored the correct decode ten to one. The 2026-09-18 NPA/FBI WaterPlum joint advisory came back unreadable on all nine pages, so any agent reading a Word-produced advisory through the bridge got nothing usable.

The reader now resolves each page's fonts and decodes each string with the font active at that point. It takes that result whenever the page walk recovers text, never on a volume comparison. The WaterPlum advisory now reads cleanly, digits included. Of the 15 PDFs the store cites, the container could fetch 12, and on all 12 the new decode is equal or better. Five regression tests pin it, one of them failing under the old selection rule (`python3 tools/test_fetch_source_pdf.py`, 13/13).

### 3. Other bridge and gate defects found by the triage

- **kb.cert.org ignores `Accept-Encoding: identity`** and sent gzip bytes that every CERT/CC note returned as noise. The bridge now decodes an unrequested gzip or deflate body, with the same size cap.
- **The quote check compared against markdown link targets** inside extracted sentences, and **the CVE-citation check flagged a clause as mis-cited when one of its pages simply could not be read.** Both are fixed.
- **EUVD, git.kernel.org and lore.kernel.org** (an Angular app and two Anubis walls) are now in the unverifiable-host list, and cached CERT/CC bodies saved before the gzip fix were cleared. After that, the check over every entry active since 2026-07-01 reports no mismatched quote and no mis-cited CVE.
- **The IOC scanner read four-part version numbers as IP addresses** when the nearby cue word was plural ("releases", "builds", "trains"). The cue list now covers the plurals.

### 4. Changelog records leave the top of the entry behind

This was the most frequent defect class after publisher revisions. It showed up on eleven entries: Unit 42, Metabase, MAG, GeoServer, NetScaler, PaperCut, ShareFile, VMware, WP2Shell, Kaltura and Gridbox. A record updated its own section and some fields, but the title, headline, summary or opening analysis kept the superseded state. GeoServer's title said "no CVE and no patch" for six weeks after the patch shipped. The prompt already requires the frontmatter and main analysis to move to the current state, and the truth passes catch it where the fire does not. It stays a watch item.

### 5. Warnings

The 3.1 h duration warning was retired by the v4.14 directive (the stall threshold is now 24 h), and the 14 acknowledgment rows that existed only for 3 to 24 h runs were pruned (37 rows down to 23). The eight Oracle products were registered by `sync_products`. Older entries touched by this audit were brought up to today's rules where the gate required it: two gained their missing Admiralty rating and ATT&CK mapping, reader-text wording naming the pipeline was replaced, one action list was trimmed to three, and an NVD data-sheet link was removed. `check_run.py --all` ends with 0 FAIL.

### 6. Transparency: WebFetch on cisa.gov

Triage pass T1 read one CISA alert through `WebFetch` to recover its current text, against the CLAUDE.md rule. Source-repair worker SR1 also sampled it and recorded in three source notes that it worked. Those notes told future agents to "use WebFetch first". They now record the observation only and point to recommendation 1.

## Fixes shipped (this session)

- **v4.13** Series 5.5 prompt optimisation: unattended turn endings, the rotational lookback, and the cited-page checks (`quote-literal`, `citation-cve`) in the gate and the audit pre-pass.
- **v4.14** Operator directive: no time limits, every run still ends by structure, inactivity-based hang detection with progress lines, and every count is a guide.
- **v4.16** Content-aware source health, 28 source records changed, ops-dashboard groups for the two new actions, and the quote check bound to the entry's sources.
- **Tools:** `fetch_source.py` gains per-font PDF decoding, `bfrange` array destinations, skipping of marked-content property lists, and decoding of unrequested gzip. `check_run.py` gains markdown-link stripping, unreadable-page semantics for CVE citations, three more unverifiable hosts and plural version cues in the IOC scanner.
- **Content:** 43 entries corrected, improved or updated, and 9 registry records added (eight Oracle products and `actor:dire-wolf`).

## Recommendations (operator decisions, not shipped)

1. **CISA transport.** `cisa-news`, `cisa-directives` and the IT half of `cisa-advisories` have no in-container reader: Akamai refuses every direct UA and the reader pool is empty. The agent-side `WebFetch` tool read cisa.gov every time it was tried today. CLAUDE.md forbids it, so the choice is yours. You can allow `WebFetch` for CISA listing pages (existence and dates only, bodies still through the bridge), or refill the reader pool. The same choice applies to `ssd-disclosure`: its host serves the container a captcha on every path, while `WebFetch` read its advisory list and articles cleanly, and the record keeps its reader recipe until you decide.
2. **`cisa csaf-recent` covers ICS/OT only.** It is now the `cisa-advisories` health surface. That proves the source works but not that IT advisories are reachable. A recipe for the IT advisories feed would close the gap.
3. **Google TAG and Mandiant/GTIG overlap.** The TAG URL now redirects to Google's general security blog, which carries GTIG posts. Consider folding `google-tag` into `mandiant-gtig`.
4. **Effort measurement.** No fire has run on the 5.5 generation yet, so the model-generation baseline (quality audit Phase 3 item 9) starts with the 2026-10-04 audit.

## Watch items

- **Top-of-entry drift after a record** (finding 4). Measure it in the 2026-10-04 audit: of the window's update records, how many left the title, headline or summary stale.
- **Publisher revisions.** Most quote defects are pages changing after publication, and thirteen of this audit's carried news. The weekly pre-pass catches them. A monthly re-run over the trailing 90 days would catch the slow ones.
- **Three unreadable sources** until the CISA and SSD transport question is decided.
- **NCSC-CH moved to bacs.admin.ch.** Four June entries (the G7 events warning and the week 22, 23 and 25 reviews) cite `ncsc.admin.ch/ncsc/...` pages that now answer 404. They sit outside this audit's scope, and the next audit should repoint them through changelog records, as this one did for WP2Shell.
