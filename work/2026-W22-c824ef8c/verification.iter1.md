**Model:** Claude Opus 4.7 (`claude-opus-4-7`) — env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset; identity from runtime
**Timestamps:** started_at=2026-05-25T00:59:30Z · ended_at=2026-05-25T01:04:26Z · duration_seconds=296
**Self-telemetry:** webfetch_calls=13 · websearch_calls=0 · bridge_fetches=3 · urls_checked=14

## Verification report — briefs/weekly/2026-W22.md (iteration 1, Opus cold read)

Cold read of the 2026-W22 weekly. 14 cited URLs fetched (WebFetch + bridge). Mechanical gate already covered structure/allowlist/footer/CVE-sync; this pass is truth + editorial. No IOCs present (clean). One mechanical FAIL outstanding (run-log-verification iterations[] empty — resolved once this iteration is recorded). Substantive truth defects found below.

### Broken / unreachable URLs

**F1 — CVE-2026-20223 Cisco Secure Workload PSIRT URL is a 404.** § 3 roll-up table row AND § 3 deep-dive both cite `https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-csw-authbypass-CVE-2026-20223`. WebFetch returned Cisco's "The Page You Have Requested Is Not Available" 404 page. Replace with the correct PSIRT advisory URL for CVE-2026-20223 or mark the CVSS-10.0 claim unverified.

**F1 — CVE-2026-42231 n8n advisory URL 404s + malformed GHSA id.** § 3 roll-up cites `https://github.com/n8n-io/n8n/security/advisories/GHSA-n8n-rcv-2026-42231`. 404. GHSA IDs are `GHSA-xxxx-xxxx-xxxx`; embedding the CVE number ("GHSA-n8n-rcv-2026-42231") is not a real identifier — appears guessed/fabricated. Replace with the actual GHSA advisory or n8n release notes.

### Generic / oversight URLs (replace with specific article)

**F2 — CVE-2026-43997 vm2 advisory is a listing index.** § 3 roll-up cites `https://github.com/patriksimek/vm2/security/advisories` — the paginated advisories INDEX for the repo, not the specific advisory for CVE-2026-43997. NEVER-cite listing-index pattern. Replace with the specific GHSA advisory URL.

### Citation does not support the claim

**F3 — Sparx "actively exploited" contradicted by the CCB advisory body.** The brief asserts in § 0, § 1, § 2, § 4, § 7 and the § 3 roll-up ("Active ITW") that CCB Belgium "explicitly labels all five CVEs as actively exploited" / instances are "currently being actively exploited." The CCB advisory BODY (fetched via bridge) states verbatim: *"There is a publicly available Proof-of-Concept (PoC) for all five vulnerabilities. There is no proof of exploitation as of the writing of this [advisory]."* Only the advisory TITLE says "Actively exploited." The brief's load-bearing exploitation claim rests on the title and is contradicted by the body. Reframe: public PoC for all five, NO confirmed exploitation per CCB body; correct the roll-up "Active ITW" → "PoC-public, no confirmed ITW."

**F3 — PoC misattributed to CERT Polska.** § 1 Sparx item: "All five CVEs carry public PoC code published by CERT Polska." The CERT Polska page (`cert.pl/en/posts/2026/05/CVE-2026-42096/`) does NOT mention public PoC and does NOT state active exploitation. The "PoC for all five" statement is CCB Belgium's. Attribute to CCB.

**F3 — Megalodon date conflict (2026-05-23 vs CSA source's May 18).** § 0, § 1, § 2 assert "TeamPCP released the full worm as Megalodon on 2026-05-23, mass-backdooring 5,561 GitHub repos in six hours." The cited CSA research note dates Megalodon Wave 2 to **May 18, 2026** and counts **5,718 malicious commits to 5,561 repos**. The brief's date conflicts with its named primary. Reconcile: either correct to May 18, or explicitly attribute the 2026-05-23 framing to the daily brief (daily 2026-05-23) and note the CSA note's differing date — do not present 2026-05-23 as CSA-sourced.

**F3 — GitHub-internal-breach attached to wrong citation in § 0.** § 0 bullet attributes "GitHub's own ~3,800 internal repos were breached via the campaign" to the CSA research note. The CSA note does NOT mention GitHub internal repos. The fact itself is real and supported by the separately-cited GitHub Security Blog (confirmed: "~3,800 repositories ... directionally consistent," disclosed May 20, 2026). Ensure the ~3,800 claim is attributed to the GitHub blog, not CSA. (Minor: § 1/§ 2 say GitHub "confirmed" on 2026-05-21; the blog is dated 2026-05-20.)

**F3 — WebWorm attribution adds unsourced CrowdStrike mapping.** § 1: "FishMonger (a China-nexus cluster tracked separately as Aquatic Panda by CrowdStrike)." ESET links the cluster to SixLittleMonkeys and FishMonger; the "Aquatic Panda by CrowdStrike" equivalence does not appear in the ESET source. Drop it or cite a source that makes the mapping. (Minor: brief says "400+ decrypted operator messages"; ESET says 433+ — align.)

**F3 — Europol "removed" vs source's "identified."** § 8 Europol IRGC item: "14,200 posts, accounts, and hyperlinks removed across 19 countries." The Europol page title/headline states links were "IDENTIFIED" ("Investigators identified 14 200 links tied to IRGC activity"). The page rendered only as a loading screen on two fetch attempts, so "removed" vs "identified" and the 19-countries count could not be fully confirmed. Soften "removed" → "identified" unless the body confirms removal; reconcile internal "19 countries participated" vs later "14 EU member states."

### Unsupported / hallucinated facts

**F4 — Three of six German hospital names are fabricated.** § 0, § 4, § 5 name the six university hospitals as "Ludwig Maximilian University Munich, TU Munich, Heidelberg, Freiburg, Tübingen, and Würzburg." The cited The Record article names them as **Cologne, Freiburg, Heidelberg, Tübingen, Ulm, and Mannheim** (with per-hospital counts Cologne 30k / Freiburg 54k / Heidelberg 11k / Ulm 1.6k summing to ~97,600). LMU Munich, TU Munich, and Würzburg are NOT in the source. Three of six hospital names are wrong. Heise is the other cited source — neither aggregator supports the Munich/Würzburg list. Correct the hospital list to match the sources, or remove the specific names if they cannot be verified. This is the most serious truth defect in the brief.

### Quantifier without source

**F14 — "50+ unique government victims" overstates ESET.** § 0 and § 4 (WebWorm): "ESET documents 50+ unique victims" / "50+ unique government victims." The ESET source describes ~50+ reconnaissance targets across 56 scanned hosts, with confirmed government compromises in five named countries — not "50+ unique GOVERNMENT victims." Reframe to ESET's actual phrasing (recon targets / scanned hosts vs confirmed victims). NOTE — the other three check_brief quantifiers are source-backed and benign: "174 distinct threat actors" (CERT-EU TLR 2025 verbatim — confirmed), "five distinct stages" (brief-internal narrative framing of the daily timeline, acceptable), and the MSS-prohibition "as of 25 May 2026" absolute (Greenberg Traurig states verbatim "As of 25 May 2026, the provision of managed security services ... is prohibited" — confirmed).

### Strengthen primary source / single-source flags

**F12 — 14 single-source items lack the `[SINGLE-SOURCE]` heading flag.** check_brief lists: WebWorm (welivesecurity), Kali365 (ic3.gov), MS Defender pair (msrc), Cisco CSW (cisco), ChromaDB (bleepingcomputer), SonicWall (cybersecuritydive), GitHub PIR (github.blog), Sparx (ccb.belgium.be), TheGentlemen (checkpoint), BlackFile (cloud.google.com), WebWorm-status (welivesecurity), Rhysida (heise), EU-sanctions-renewal (dig.watch). National-CERT carve-out applies to NONE (none is a national CERT acting as primary disclosing party for its own jurisdiction). Add `[SINGLE-SOURCE]` to each heading and name the single source in § 7/§ 10, OR add a corroborating second primary. (EU-sanctions-renewal carries the flag in prose but not in the heading.)

**F12 — German hospitals aggregator-only + wrong names.** § 5 item sourced only to therecord.media + heise.de (both aggregators). Add the `reduced confidence — only aggregator sources` note in § 10 and re-pivot to a hospital statement / DPA notification primary. Compounds with F4.

### Editorial / less-is-more flags (advisory)

**F11 — AI-content notice verifier placeholder inconsistency.** Line 3 prose notice names "Claude Opus 4.7 — verification" as if completed; line 5 Generated-by says "verify: unknown (pending)"; § 10 says "Phase 4.7 pending." After this iteration, finalise: set `verify:` to the actual per-iteration verifier model(s) and update the § 10 Verification line. This iteration ran on **Claude Opus 4.7 (`claude-opus-4-7`)**.

**F11 — ChromaDB CVSS phrasing garbled.** § 3 deep-dive: "CERT Polska assigns CVSS 4.0 = 10.0 in their advisory." This is incoherent and unsupported — the only Source on the item is BleepingComputer (no CERT Polska link). Either source the 10.0 reassessment or drop the confusing "4.0 = 10.0" construction.

### Items verified clean (no finding)

- CERT-EU TLR 2025 (174 actors / 7-of-9 / agentic AI first-documented) — all three claims confirmed verbatim on cert.europa.eu.
- CERT-EU Cyber Brief 26-05 (Finland Valtori ~50k, France ANTS ~19M, Hungary 795 creds / 12-of-13 ministries) — all confirmed.
- Drupal SA-CORE-2026-004 / CVE-2026-9082 (pre-auth SQLi, PostgreSQL, fixed versions) — confirmed. NCSC.ch post #12584 confirmed via bridge (title "[Advisory] Drupal: Upcoming critical security release"; active-exploitation edit dated 2026-05-22, brief says 2026-05-23 — minor date drift, advisory; the brief's "NCSC.ch flipped to Actively exploited" framing is defensible).
- FBI PSA260521 / Kali365 OAuth device-code — confirmed.
- SonicWall CVE-2024-12802 (incomplete patch, Akira, UPN/SAM) — confirmed.
- DeXpose DEVO-Tech AG (CH, 2026-05-18 DLS listing) — confirmed (vendor-blog kind, single-source → F12).
- Unit 42 / StepSecurity npm/SLSA analysis — confirmed (SLSA Build L3 provenance insufficient).
- MSS prohibition "as of 25 May 2026" (Greenberg Traurig) — confirmed verbatim.
- No IOCs (no hashes/IPs/domains/rule-code). English throughout. No workflow-internal language in published prose.

### Verdict

NEEDS_FIXES (truth: 9, editorial: 2, advisory: 2)

Truth (F1×2, F2×1, F3×6, F4×1, F14×1 = 11 truth-class findings; counted as 9 distinct defects after grouping the two § 0/§ 1 Shai-Hulud attribution items): the F4 hospital-name fabrication and the F3 Sparx active-exploitation contradiction are BLOCK-level — both put materially wrong operational facts in front of responders. The two 404s (F1) and the listing-index (F2) are BLOCK. Editorial: F12 single-source flags + aggregator note. Advisory: F11 notice finalisation + ChromaDB phrasing.

### Findings summary (machine-readable)

See sibling file `work/2026-W22-c824ef8c/verification.iter1.findings.yaml`.
