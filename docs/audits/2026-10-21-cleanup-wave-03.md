# Cleanup wave 03, 2026-10-21

**Run record:** [runs/2026-10-21/2026-10-21T1149Z-audit.md](../../runs/2026-10-21/2026-10-21T1149Z-audit.md) · **Prompt:** v4.23 · **Program:** [prompts/cleanup-coordinator.md](../../prompts/cleanup-coordinator.md) · **Tracker:** [docs/cleanup/STATUS.md](../cleanup/STATUS.md) · **Lane:** A, beside waves 02, 04 and 05

## Scope

Rows W4-01, W4-03, W4-04 and W4-05 (duplicates) and W1-D (33 entries), from `work/cleanup/wave-03/findings-W1-D-and-groups.yaml`. Claim `partial 2026-10-21T11:49:47Z wave=03`, base `29364cd` (`work/2026-10-21T1149Z-audit/base.sha`).

- **W1-D:** the 2026-10-18 audit's duplicate and legacy truth passes (D1 to D3, L) found 366 defects on these 33 entries. Those passes read the store before the 2026-10-11 audit's records landed, and that audit had written a record on 30 of the 33 since, so every defect was re-derived on the current text first.
- **W4:** the duplicate pairs were decided before their members were re-verified, then the six members got a fresh whole-entry truth pass (T1, 99 claims).
- **W4-05:** a store-wide scan for twins that share no CVE (`work/2026-10-21T1149Z-audit/twin-scan/`).

## Verdict

**23 entries carry a record from this wave: 2 updates, 6 corrections (one internal) and 15 improvements (one internal). One duplicate was folded and five twin pairs went back to the tracker (four from the scan, one found in repair).** Of the 33 W1-D entries, 12 needed no record because the 2026-10-11 audit had already fixed every listed defect. On the other 21 the remainder is fixed here. The four legacy entries in scope (YellowKey, Nightmare Eclipse, the Pwn2Own Berlin roundup, the folded ClickFix twin) left the legacy queue.

Verification: eight `cti-verification` passes, the cap. Two CLEAN verdicts were each refuted by their confirmation pass, and the four findings of iteration 8 were fixed after it, so the wave publishes fail-open with residual 4. Budget: 17 of 20 spawns, about 6.88 M sub-agent tokens.

## Duplicates (W4)

| Row | Members | Decision | Outcome |
|---|---|---|---|
| W4-01 | YellowKey 2026-05-15, Nightmare Eclipse 2026-05-30 | distinct findings sharing CVE-2026-45585: link | Nightmare Eclipse now lists YellowKey in `references[]`, its CVE-2026-45585 record matches YellowKey's (security feature bypass, physical, CVSS 6.8, fixed 2026-06-09) instead of a local privilege escalation with no patch, and both entries were rewritten from their sources (below) |
| W4-03 | Ghost CMS CVE-2026-26980 ClickFix 2026-05-25, "Large-scale ClickFix campaign" 2026-05-25 | same finding: fold | the twin is folded into the rewritten ClickFix entry, whose record carries the twin's verified facts (the named universities, DuckDuckGo, the forged Cloudflare verification iframe and the visitor fingerprinting, the payload types, the Admin API key's scope). Its unsupported claims stayed behind: EU and Swiss usage, "every visitor", a browser-process-tree hunt and the europe and public-sector metadata |
| W4-04 | Pwn2Own Berlin roundup 2026-05-17, DEVCORE Exchange chain 2026-05-17 | distinct findings: link (the DEVCORE entry already lists the roundup) | the roundup was rewritten from the three ZDI day pages (below) |
| W4-05 | store-wide scan | 118 candidate pairs in two passes, 5 real beyond the known W4-03 pair | Adobe APSB26-120 (2026-08-07) now lists APSB26-114 (2026-08-02) in `references[]` (internal record). Four pairs sit on rows other waves hold and became rows W4-06 to W4-09 (§ Tracker delta). The other candidates are distinct findings: entries on distinct CVEs or products that share a vendor post or an article (Check Point 2026-09-10 and 2026-09-18, Cisco FMC 2026-08-04 and ISE 2026-09-17, Copy Fail and Dirty Frag, Dirty Frag and Fragnesia) or only a feed or listing URL. Dirty Frag now links Copy Fail. Fragnesia, which Red Hat counts in the Dirty Frag set, should link Dirty Frag, and that link went back to the tracker as W4-11 |

Registry relations whose source entry is gone (W5-06): 0 after the fold. `tools/fold_entries.py` re-pointed nothing, since no relation or other entry's `references[]` named the twin.

## Findings applied and declined

| Entry | Record | Applied | Declined |
|---|---|---|---|
| 2026-05-15 YellowKey and GreenPlasma (legacy) | update | fixed in the 2026-06-09 Windows updates (MSRC CVE-2026-45585 revision 2, fixed builds), GreenPlasma assigned CVE-2026-45586 and fixed the same day. "No CVE" and "no patch" removed throughout, both actions dropped, the invented "actively investigating" quotation and the uncited "four" total deleted. The mechanism now says USB reproduced and the EFI partition did not, and a Contradiction line sets the researcher's TPM+PIN claim against MSRC. T1542.001 out (no firmware is touched). Rating, mapping and labelled lines added, priority high to notable | the reciprocal link to Nightmare Eclipse (links point from the newer entry), T1006 (weak fit) |
| 2026-05-30 Nightmare Eclipse (legacy) | update | rewritten: the statement is MSRC's blog post of 2026-05-27 (reported 2026-05-29), quoted as written ("will continue bringing cases"), with The Record's "stopped short of directly threatening legal action" beside heise. The 14 July threat is on the July Patch Tuesday, the wrong "10 June" is gone, the three May drops are fixed since 2026-06-09, and the incomplete-fix claim is the researcher's. The "UPDATE (originally covered 2026-W21)" framing and the uncited AppLocker advice are removed | none |
| 2026-05-25 Ghost CMS ClickFix (fold survivor) | improvement | the twin's verified facts (W4-03) and the full XLab chain. "Self-hosted" dropped from Exposure (no source distinguishes Ghost(Pro)), more than 700 domains as of XLab's 2026-05-17 enumeration, CVSS 9.4 attributed to Ghost's advisory | the finding on the 2026-10-11 record's summary (records are append-only) and the D3 leads, already fixed by 2026-10-11T1307Z-audit |
| 2026-05-17 Pwn2Own Berlin roundup (legacy) | correction | rewritten from ZDI's day pages, announcement and rules. "Unauthenticated" removed from the Exchange chain, ZDI's real categories (AI Databases, Coding Agents, Local Inferences, NVIDIA), the outcome of each AI target (Chroma a success, Oracle a failure), the 90-day patch window as BleepingComputer states it. The forecasts, the rejected-researcher PoC wave, the Swiss and EU framing, the uncited hardening bullets and the action are gone. Kind threat to research, priority high to routine, no longer a deep dive, Hackread and ZDI Day One dates fixed | the reciprocal link to the DEVCORE entry |
| 2026-05-17 DEVCORE Exchange chain | improvement | MSRC's CVE-2026-62911 page cited for the fix, the fixed builds and the credit to Orange Tsai working with ZDI. The link between CVE-2026-62911 and the contest chain is attributed to Franky's Web and to MB VRED's analysis, since Microsoft's record does not name Pwn2Own | seven D1 leads, already fixed |
| 2026-05-09 Copy Fail CVE-2026-31431 | correction | the `algif_aead` blacklist does not work on RHEL, where the module is built in: Red Hat's RHSB-2026-002 gives an `initcall_blacklist=` boot argument instead. Red Hat's "all fixes are now available" and Xint's seccomp option added | five, already fixed |
| 2026-05-09 DENIC DNSSEC outage | correction | `event_date` 2026-05-05 (the outage) rather than 2026-05-08, DENIC's final report of 2026-06-11 and its measures added, Cloudflare's post dated 2026-05-06. The 2026-05-10 section no longer reports DENIC's 11 May addendum | retyping to incident (a non-adversarial outage has no honest ATT&CK mapping) |
| 2026-05-15 nginx CVE-2026-42945 | correction | code execution is not limited to hosts with ASLR disabled (depthfirst, and F5's CVE description of 2026-09-10 cited through ENISA EUVD-2026-30010). Six evidence quotes added, and a Defender takeaway with the fixed releases and depthfirst's named-capture workaround | marking it exploited (honeypot attempts only) |
| 2026-07-16 Oracle EBS CVE-2026-46817 | correction | Oracle's advisory is dated 2026-05-28 by its own revision table, so the 2026-10-11 re-dating to the page's metadata date was itself wrong. "Roughly six weeks" is attributed to Defused, and labelled lines are split out | none |
| 2026-05-19 n8n prototype pollution | correction (internal) | T1078 mapped (every advisory requires an authenticated workflow editor), T1059.007 dropped | 2.21.1 against 2.22.1 (only the uncitable CVE record says 2.21.1) |
| 2026-05-08 CERT-FR ACT-016 | improvement | the advisory's own five risks | five, already fixed |
| 2026-05-08 GLPI CERTFR-2026-AVI-0551 | improvement | the sources disagree on which branches CVE-2026-5385 affects, which is now stated. CVE-2026-42321 narrowed to 10.0.4 and later | four, already fixed |
| 2026-05-09 Spring Cloud Config CVE-2026-40982 | improvement | HeroDevs' read-only, information-disclosure impact stated beside the integrity-High score, and an Exposure clause that cited Spring for something Spring does not say is fixed | four, already fixed |
| 2026-05-09 LiteLLM CVE-2026-42208 | improvement | Sysdig observed the first exploitation attempt 36 hours after the advisory reached the global database, with no confirmed compromise | five, already fixed |
| 2026-05-09 Dirty Frag | improvement | EPSS refreshed to 2026-10-20 (CVE-2026-43500 fell from 0.9286 to 0.0262), Microsoft's Defender Security Research Team credited, Red Hat's "Copy Fail 2" nickname dropped from the main analysis and the Copy Fail entry linked | the Debian DSA (no URL in the finding) |
| 2026-05-18 Exchange CVE-2026-42897 | improvement | the Emergency Mitigation Service cannot fetch new mitigations on builds older than March 2023. T1552 replaced by T1555.003 and T1528 (Proofpoint's two credential behaviours), and the headline cut from 157 to 116 characters | the Proofpoint date (the visible byline says 29 July) |
| 2026-05-29 FortiClient EMS CVE-2026-35616 | improvement | the 9.8 base score first, Arctic Wolf's Elevation Service wording, its ProgramData staging and log-exfiltration hunts | none |
| 2026-06-30 SimpleHelp CVE-2026-48558 | improvement | the 10.0 score labelled CVSS 3.1 (CCB Belgium), 6.0 scope narrowed to some beta and release-candidate builds, login setting off by default for new Groups, interim technician-login IP restriction | the 2026-05-26 fix date (on no readable vendor page) |
| 2026-06-06 Catalyst SD-WAN CVE-2026-20245 | improvement | all three upload scripts Cisco names, Mandiant's surviving log traces, the edge-configuration push and its check. The shield is "only temporary partial protection", also in the 2026-10-11 section | none |
| 2026-06-16 Catalyst SD-WAN CVE-2026-20262 | improvement | "path traversal" cited to the KEV row, exact WildFly paths and log locations, internet-exposed Managers at risk, link to the CVE-2026-20245 entry | none |
| 2026-06-24 Unified CM CVE-2026-20230 | improvement | SSD's documented request chain in the narrative and Detection, SSD added as a source | the proof-of-concept sentence (revision 1.1's wording does not settle it) |
| 2026-09-12 Japan Digital Agency GSS | improvement | the dead Jiji page replaced by the Digital Agency's own notice of 2026-09-11 (detection timeline, the 189,000 and 57,000 split). The 2026-09-13 section no longer calls it undisclosed whether the flaw was known: the minister said at the 2026-09-11 press conference that the agency knew of it beforehand (Piyolog) | none |
| 2026-08-07 Adobe Campaign Classic APSB26-120 | improvement (internal) | links APSB26-114 (W4-05), and three pipeline phrases in the sourcing note are reworded | none |
| 12 W1-D entries with no record | none | | every listed defect already fixed by 2026-10-11T1307Z-audit: Amazon SES, Kaspersky Q1, MuddyWater, xrdp, DAEMON Tools, ENISA CVE root, German court, Semantic Kernel, PAN-OS CVE-2026-0300, Catalyst SD-WAN CVE-2026-20182, Cisco ISE, Everest Forms Pro |

State from the records: `last_seen` moved to 2026-10-21 for CVE-2026-35616, 48558, 42321, 43284, 43500, 45585 and 45586, and the stale titles of CVE-2026-35616, 48558, 46817 and 45586 were refreshed. Registry: the summaries of `campaign:nightmare-eclipse-microsoft-dcu-threat-greenplasma-miniplasmaaac` (the summary no longer says criminal action was threatened, and the three drops are fixed) and `incident:pwn2own-berlin-2026` (not every AI target fell, and no source calls the participant Swiss) are corrected. `tools/sync_products.py` added five product records from the rewritten roundup (Chroma, LM Studio, NVIDIA Container Toolkit, NVIDIA Megatron Bridge, Red Hat Enterprise Linux for Workstations) and moved `first_seen` earlier on eight existing ones that the rewritten roundup, YellowKey and Nightmare Eclipse entries now name.

## Verification

Eight passes of `cti-verification`, the iteration cap. Every pass answered every claim in its scope.

| Iteration | Role | Claims | Verdict | Truth / editorial / advisory |
|---|---|---|---|---|
| 1 | first pass | 266 | NEEDS_FIXES | 7 / 7 / 13 |
| 2 | post-fix | 155 | NEEDS_FIXES | 3 / 2 / 6 |
| 3 | post-fix | 157 | NEEDS_FIXES | 2 / 0 / 2 |
| 4 | post-fix | 145 | CLEAN | 0 / 0 / 3 |
| 5 | confirmation | 277 | NEEDS_FIXES | 3 / 0 / 2 |
| 6 | post-fix | 278 | CLEAN | 0 / 0 / 6 |
| 7 | confirmation | 278 | NEEDS_FIXES | 4 / 0 / 7 |
| 8 | post-fix at the cap, full scope | 278 | NEEDS_FIXES | 3 / 1 / 3 |

The substantive fixes came from iteration 1: the Japan entry's dead primary source, the Copy Fail identification Dirty Frag had lost, the TPM+PIN dispute flattened in YellowKey's summary, two disagreements between cited sources (nginx on ASLR, DEVCORE on authentication), and file-name indicators on the FortiClient and Ghost CMS entries. From iteration 3 on, the findings were citation-precision points: a clause bound to a page that carries only part of it, or a paraphrase stronger than its source. The two confirmation passes refuted both CLEANs on such points. Iteration 8's four findings were fixed after the pass and published on the fail-open rule without re-verification, so the residual is 4. Full findings with their remediation: the run record's `verification.iterations`.

## Budget

17 of 20 spawns (`work/2026-10-21T1149Z-audit/budget.tsv`): one truth pass, five repair workers, eight verifier passes and three continuations after account session limits (repair-5 and verifier iterations 1 and 3), about 6.88 M sub-agent tokens in all (truth pass 0.47 M, repairs 1.68 M, verifier 4.74 M). No spawn was refused by the content classifier. The first truth-pass attempt as the named `cti-verification` type was refused because the type was not registered, so no spawn happened and none is counted.

## Not reached and carried forward

- PAN-OS CVE-2026-0300 (2026-05-12) and the ENISA CVE root entry (2026-05-09) have no Defender takeaway line. Neither got a record this wave, so the gap is carried to the next pass that touches them.
- Priority calibration, for the next monthly calibration review (pre-existing, raised by verifier iteration 1): SimpleHelp CVE-2026-48558 stays `critical` although exploitation needs a Group setting that is off by default, and Dirty Frag stays `high` although its exploitation is unconfirmed.
- Pre-existing advisories from verifier iteration 6: the YellowKey 2026-05-20 section's "disclosed on 2026-05-12" has no citation, and the Japan GSS entry's split of the affected records omits the individuals the Digital Agency names beside contracted businesses.
- Residuals the workers noticed outside their findings, left unfixed: n8n `cves[].type` values are inconsistent and its `supply-chain` tag has no source. FortiClient's mapping omits the download, exfiltration, encoding and deletion behaviours Arctic Wolf states, and its takeaway omits the port-8013 restriction. SimpleHelp has an unsupported public-sector sector and undated sources. CCB Belgium alone says a SimpleHelp PoC exists. One of repair-1's seven residuals, that Copy Fail and Dirty Frag did not reference each other, was resolved after verifier iteration 1: Dirty Frag now lists Copy Fail, and Copy Fail, the earlier finding, needs no link back. Full lists: `work/2026-10-21T1149Z-audit/repair-<n>.md`.

## Process notes

- **Run-id collision.** Waves 03 and 05 both computed `2026-10-21T1147Z-audit` in the same minute. Wave 05's claim landed first, so this wave withdrew its claim and re-claimed as `2026-10-21T1149Z-audit` (commit `7e74158`). Row W7-17 asks § C1 for a uniqueness check. It ships with C9 or when no wave is in flight, because a version bump fails every in-flight record's prompt-version check.
- **Verifier type.** The session started outside the repository, so `.claude/agents/` was not registered when the truth pass spawned. Truth pass T1 ran as a `claude` sub-agent on `sonnet` at `xhigh` effort with the `cti-verification` definition loaded by instruction, and reported Sonnet 5.5 from its own model line. The named type became available afterwards and ran every Phase 5.7 iteration.
- **Session limit.** The account-wide limit cut three spawns while waves 02, 04 and 05 ran beside this one (HTTP 429): repair-5 at its first source reads, verifier iteration 1 at 10 of 23 entries and verifier iteration 3 after its first entry. Per § C8 none was retried in a loop. Each was resumed once after the reset, as a continuation counted in the budget.
- **Record tool gap.** `tools/entry_record.py add` stops on the 581 entries without an `updates:` key. Workers added `updates: []` first, and row W7-16 asks for the fix.

## Tracker delta

Rows done this wave: W4-01, W4-03, W4-04, W4-05, W1-D. New rows: W4-06 (The Gentlemen 2026-06-12 and 2026-06-27, wave 08, with the 2026-06-27 entry moved out of W2-05 and the 2026-06-12 entry out of W2-04), W4-07 (Calypso and Red Lamassu 2026-05-22), W4-08 (7-Eleven 2026-05-19 and 2026-05-27), W4-09 (the Drupal PSA-2026-05-18 pair inside W2-01), W4-10 (the 2026-05-19 MiniPlasma entry, an unfolded legacy update of the YellowKey thread) and W4-11 (the Fragnesia entry should list Dirty Frag in `references[]`), all five in the new wave 12 after waves 04 and 05. Also W7-16 (record tool), W7-17 (run-id uniqueness, wave 11) and a lead on W2-04 (the 2026-06-11 RoguePlanet entry gives GreenPlasma as CVE-2026-50507, which MSRC lists as a BitLocker bypass). Wave 11 now waits on wave 12 too.
