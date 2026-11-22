**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T15:11:23Z · ended_at=2026-11-22T15:37:49Z · duration_seconds=1586

## Verification report — 2026-11-22T1407Z-audit (iteration 1)

Scope: two new entries read whole, 25 updated entries (changes since base cdd8f41, whole entry read for supersession), run record, audit report, state diffs. Ledger: 202 claims, 202 verdict rows in `verification.iter1.claims.yaml` (192 ok, 5 F3, 4 F4, 1 F14, 1 unreadable: the baselland.ch FAQ page answers 403 to extract, the bridge, jina and WebFetch; the Basel-Landschaft translation was checked only against the recorded original). Sources were re-fetched this pass (CISA alerts through WebFetch, KEV through the bridge, Drupal through its advisory feed, Siemens table through the raw page, GHSA sidebars through the raw page).

### Citation does not support the claim

- #1 (F3) 2026-11-17/bundid-automated-mass-logins-lock-federal-citizen-accounts, Defender takeaway: "the operator's containment, as heise and Handelsblatt report it, was to switch off the password-only path while eID and other sign-in means stayed open, and to bring it back the same day only with an e-mail security code". heise says access via username and password was deactivated and eID or other means stay possible; Handelsblatt says the password sign-in was blocked on Monday morning; neither mentions the e-mail-code return (Spiegel and ad-hoc-news do). The clause has no citation. Cite Spiegel.
- #2 (F3, low confidence) 2026-11-22/synology-dsm-oauth-api-cve-2026-120382-unauth-file-write, sourcing_note: the older-branch builds "(6.2.4-25556-9, 7.1.1-42962-10, 7.2.1-69057-14, 7.2.2-72806-11) that its own product table still marks as OnGoing". The product table has no DSM 6.2 row.
- #3 (F3, low confidence) 2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline, "[N-able, 2026-11-16]": the page's dateline is "Published Time: 2026-11-13T22:59:21+00:00" and the agent-impersonation passage sits under "Publication 2: November 12", not under the "Update: November 16" block.
- #4 (F3, low confidence) 2026-11-20/vmware-vcenter-cve-2026-123890-auth-bypass-exploited-gtig, cves[CVE-2026-123893].affected names VMware vSphere Foundation in the same list as 5.x; the VMSA matrix's 5.x row names only VMware Cloud Foundation (SDDC Manager, fixed 5.2.5).
- #5 (F3, low confidence) 2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router, "put on registry hold" (section and record summary): Report URI says "`clientHold`", a registrar-side status.

### Unsupported / hallucinated facts

- #6 (F4) 2026-11-18/cve-2026-115731-puppet-enterprise-report-deserialization-rce: the correction removed OpenVox Server from cves[CVE-2026-115731] and states in the record summary that the server range "belongs to CVE-2026-115732". GHSA-ffr6-rwpm-p5wq, the advisory for CVE-2026-115731, lists OpenVox Agent (affected <= 9.2.0 and <= 8.31.1, patched 9.3.0 and 8.32.0) and OpenVox Server (<= 9.1.0 and <= 8.17.0, patched 9.2.0 and 8.18.0). The main analysis ("OpenVox fixes it in server 9.2.0 and 8.18.0") and the action still carry the server builds, so cves[] now contradicts both. The TD pass itself recommended adding the agent "alongside the server builds". Restore the server, cite GHSA-ffr6, reword record summary and Correction.
- #7 (F4) 2026-11-20/vmware-vcenter-cve-2026-123890-auth-bypass-exploited-gtig, body: "calls it an emergency change and states no exploitation". The replaced text read "does not state exploitation"; Broadcom's advisory and Q&A say nothing about exploitation, and the entry's own summary and sourcing_note say so.
- #8 (F4) 2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo, Defender takeaway (unchanged): "Apply Mitel's workaround articles for OpenScape SBC, SESAP and Contact Center until updates ship". Mitel rev 6.0: OpenScape SBC "Update to V11R3.4.5. Workaround available"; this fire's section and action say the SBC fix is released.
- #9 (F4) same entry, evidence[2]: "Planned update for V11R3.4.5. Workaround available, see KB article" (Mitel). The page now reads "Update to V11R3.4.5. ..."; the quote is not contiguous and states the SBC fix is planned (standing quote-literal WARN in page-checks.txt).
- #10 (F4) 2026-11-17/bundid-automated-mass-logins-lock-federal-citizen-accounts, sourcing_note: "the operator's own notice could not be read ... the report of a same-day restoration of password sign-in comes from one aggregator". This fire cites Spiegel quoting the operator's notice.
- #11 (F4, low confidence) 2026-11-22/synology-dsm-oauth-api-cve-2026-120382-unauth-file-write, body: "The advisory states no exploitation." The advisory is silent.
- #12 (F4, low confidence) 2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce: five sources[] publishers still read "Calif (discoverer)" after this fire's record says Calif is "one of two credited reporters rather than the discoverer".

### Quantifier without source

- #13 (F14, low confidence) 2026-11-22/timeroasting-detection-ms-sntp-own-rid-check-huntress, Exposure: "every Active Directory domain controller answers MS-SNTP for computer and trust accounts". Huntress tested one patched Windows Server 2025 DC and says its behaviour "may not be representative"; Samba AD DCs lack the extended form.

### Needs more research

- #14 (F8, low confidence) 2026-11-18/oracle-november-2026-cspu-56-unauthenticated-critical-rows: the correction makes three 9.8 rows (Communications Diameter Signaling Router, Unified Assurance, PeopleSoft PeopleTools) the KEV-listed Brotli flaw, but the Defender takeaway and actions[0] still lead with Access Manager, WebLogic, E-Business Suite and APEX.

### Missed angles

- #15 (F10, low confidence) Java4Shell vendor impact: Metabase (GHSA-69v7-pwxv-xxr3, 2026-11-19) and Adobe Animate (APSB26-208) came back from G1 for the high Java4Shell entry, which the same update enriched with Keycloak and Atlassian; neither is added or named as dropped.

### Editorial / less-is-more flags (advisory)

- #16 (F11) Oracle entry title still ends "no row is marked exploited" beside the corrected headline "Brotli rows exploited".
- #17 (F11) Record summaries with pipeline vocabulary: ScreenConnect ("the headline is back within 120 characters"), ARTEX ("cut back to the length bound"), vCenter ("which the frontmatter already carried"), Danfoss ("a record-keeping sentence is removed").
- #18 (F11) Timestamps: run record completed 15:02:00Z, new entries discovered_at 15:05:00Z and 15:08:00Z, sources.json note "at about 15:15" (this pass started 15:11:23Z).
- #19 (F11) Report figures: "7 of 34 high" (8 on disk with Drupal, same base as "15 of 49"); "14 of 323" (331 iterations carry both counters, 14 mismatches, none CLEAN); G1 droppable "10" while 12 are named and 15 were returned (Metabase/Adobe Animate and eMudhra pip/pnpm unaccounted for).

### Checked and holding

Truth-pass tallies (49 entries, 24/22/3; 1,426 claims; per-batch claim counts) match truth-T*.yaml; 25 entries carry one record each (7 update, 10 correction, 8 improvement, 5 internal) and updated_at moves only on the 7 non-internal updates; state diffs match the report (CVE-2026-120382 added, 7 last_seen bumps, one acknowledgment whose cited iteration pattern matches the 2026-11-19 run record, five registry product records, igel-kb-security candidate); check-all warn counts (1 warn, 29 then 30 acknowledged) and KEV window (nine, all covered) match; Oracle's 62 rows at 9.0+, 56 unauthenticated and exactly three KEV-listed rows reproduce from the page and the catalogue; Drupal's exploitation line is verbatim in the advisory feed item; the content of the audit's other fixes (LiteLLM, ScreenConnect, Danfoss, Expressway, ARTEX, Fortinet, N-able, Confluence date, OptimJack content, Symantec, Java4Shell, Drupal, Oracle, agent-framework, RIKEN, nginx2root, tcherber, PHP, USI, MONAI) verified against fetched primaries. Coverage re-sweeps: no uncovered critical or high item found; dropped items hold.

### Verdict

NEEDS_FIXES (truth: 13, editorial: 2, advisory: 4)

Six truth findings are firm (#1, #6 to #10); the rest are marked low confidence.

### Findings summary (machine-readable)

See `work/2026-11-22T1407Z-audit/verification.iter1.findings.yaml`.
