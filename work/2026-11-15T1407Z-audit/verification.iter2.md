**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T15:54:30Z · ended_at=2026-11-15T16:20:00Z · duration_seconds=1530

## Verification report — 2026-11-15T1407Z-audit (iteration 2)

Scope: post-fix pass. All 120 in-scope claim ids answered (116 ok, 4 F3); the changed claims, every other claim of the 11 remediated entries, and the sampled remainder in `verify.iter2.scope.txt`. New entry read whole; the SonicWall entry confirmed unchanged against `base.sha`; run record and audit report checked against disk. Claim verdicts: `verification.iter2.claims.yaml`.

### Prior-iteration deltas (all 22 applied fixes walked)

- SonicWall CVE-2026-19868 entry: `git diff base.sha` empty; not in `updated_entry_ids[]` (27 ids). SNWLID-2026-0021 is the eMudhra DPI-SSL advisory (it is cited as such in the eMudhra entry). Fix correct.
- Run record and audit report SonicWall wording: corrected in both; revert logged in both. Fix correct.
- OpenSSH summary: SANS ISC first attempt 2026-11-05 (isc.sans.edu/diary/33498: "The first actual exploit attempt for sshole arrived on November 5th"), Previdian "First observed Nov 06, 2026". Fix correct.
- Dixell CVE-2026-124014: section now states the blog (lists it with the pre-2021 `.lua`-era class) versus the CNA record (4.3.0 through 5.8.8). Both verified. Fix correct.
- Chrome Edge builds: Microsoft Edge notes carry Stable 157.0.4341.46 (Nov 9) and Android 157.0.4341.53 (Nov 11); MSRC record rev 1.1 (Nov 13) and CISA ADP 8.8 verified. Fix correct, but the cited clause now also carries Chrome numbers (new low-confidence F3 below).
- Publica BPK: bpk.ch page names PK Softech AG (30 October notice); the same-company fact is AWP's (cash.ch). Old PDF returns HTTP 404. Fix correct, but the first clause of the 2026-10-10 section now mixes BPK and AWP attribution under the AWP citation (low-confidence F3).
- AhsayCBS: "CBS JVM" parenthetical gone; v9.17.0 and v10.3.6 release notes list the patchset for both CVEs; v9.17.0 on v9, v10.3.6 on v10 correct. Fix correct, but see F8 (superseded hotfix builds).
- eMudhra: Azure CLI 2.93.0 removes emSign Root CA - C1 and emSign ECC Root CA - C3 (MSRC post table, 11/16); label 2026-11-12 on a new source record. Fix correct.
- Brotli: "marked impacted" clause gone; Nexus fragment moved out of the Desigo CC clause. Fix correct.
- BluePhishing, LLMjacking, Dixell takeaway, Ghostframe, Chrome MSRC source, Fortinet section wording, Ahsay v10.3.6 naming, Ahsay and Publica record summaries: all verified correct on disk and against the pages (MC1506733: "Starting November 4 ... early November 2026 ... late November 2026"; Obsidian: CVE-2026-40217 sandbox escape, X41 on the guardrail test path, v1.83.14-stable of 2026-04-25, page dated 2026-09-08; NVD agrees CVE-2026-40217 is the `/guardrails/test_custom_code` bytecode flaw).
- Declined (not re-raised): Check Point KEV-feed record removal; rolling-page date labels.

### Citation does not support the claim

1. **F3** `2026-11-12/cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce`, actions[0]: "where no fixed package exists yet, as on Debian forky and the SUSE products still in progress". Debian tracker read this iteration: "forky, sid | 2.4.71-1 | fixed" (and unstable 2.4.71-1). The main analysis ("forky is still vulnerable", labelled 2026-11-13) is likewise now stale. Drop forky from the action and add a record.
2. **F3 (low confidence)** `2026-11-11/cve-2026-125350-chrome-...`, Exposure: Chrome 157.0.8103.50 and Extended Stable 156.0.8078.96 numbers sit under the Microsoft Edge notes citation, which carries only Edge 157.0.4341.46 and Android 157.0.4341.53; Brave and Vivaldi appear in no cited source (KEV names Opera).
3. **F3 (low confidence)** `2026-11-07/cve-2026-111497-...`, cves[].affected/fixed: Cisco's combined advisory covers CVE-2026-111497, -105482, -105483 and -106069; the Nexus Guest Shell rows cite bug CSCwx56979 with no CVE. Duo and RoomOS carry a "no per-CVE column" caveat; Nexus does not.
4. **F3 (low confidence)** `2026-10-09/publica-...`, section 2026-10-10: "The Bernische Pensionskasse (BPK) states in a notice dated 2026-10-09 ... ([cash.ch (AWP)])": the 9 October notice is on bpk.ch, which this clause does not cite; AWP carries the same-company fact and "Ende September".
5. **F3 (low confidence)** `2026-11-12/cve-2026-119618-...`, section 2026-11-15T14:51:17Z: "Red Hat and SUSE give CVSS 3.1 9.8 ... CISA ADP gives 8.1" cited to Red Hat only; the Red Hat page shows Red Hat 9.8 and cve.org 8.1, SUSE's 9.8 is on the SUSE CVE page.

### Unsupported / hallucinated facts

6. **F4** `docs/audits/2026-11-15-quality-audit.md`, findings row "2026-10-10 AhsayCBS" ("analysis 576 words, headline 111") and recommendation 3 ("AhsayCBS 576 (from 705)"): disk shows headline 100 characters and a 579-word analysis (same count method gives 705 for base and 878 for eMudhra, which the report states correctly).

### Needs more research

7. **F8** `2026-10-10/ahsaycbs-...`: Ahsay's advisory of 2026-10-27 (https://www.ahsay.com/en/company/announcements/release-915278-103455) names v9.15.2.78 as "the latest" v7 to v9 hotfix and v10.3.4.55 as "the latest v10 official hotfix"; the entry's summary, `cves[].fixed`, action 0 and takeaway offer the superseded v9.15.2.70 and v10.3.4.45. Exposure and `affected` still read "below the hotfix builds" although the standard releases carry the fix.
8. **F8 (low confidence)** `2026-10-23/fortinet-...`, Exposure: FortiAnalyzer and FortiManager named only on 8.0.0 to 8.0.2, while FG-IR-26-244 lists 7.6, 7.4, 7.2 and 7.0 builds as affected.

### Action-item discipline

9. **F18 (low confidence)** `2026-10-31/cve-2026-98432-...`: actions[0] ends with XCP-ng's interim iptables mitigation and actions[2] restates the interim IP-options drop; the takeaway says it a third time.

### Editorial / less-is-more flags (advisory)

10. **F11** Chrome headline "update Chrome and Edge (157.0.4341.46 or later)" reads as one build for both; Chrome's is 157.0.8103.50.
11. **F11** Brotli summary lead-in "Between 2026-10-27 and 2026-11-10" contradicts the 2026-11-13 Cisco 1.13 and tvOS items in the same summary.
12. **F11 (low confidence)** Record typing: OpenSSH (QNAP not-affected advisory, NCSC.ch rating) filed as `correction`; eMudhra (Microsoft's 2026-11-12 product table) filed as `improvement`; docs/pipeline.md puts a material new development under `update`. Leave if the no-float choice is deliberate.

### Checked and clean

New entry (ARTEX in AWS): every sentence matches the Datadog post (S3 anonymous reads, FilterLogEvents limit 1000, 2026-10-20 widening, Cognito PreSignUp/token trade, ListBuckets..ListFunctions failures, Mandarin consoles, .gov/.edu blocklist) and the Wiz post (`/zzz-nonexistent-xyz123`); Storm-0940 link is Datadog's citation of Microsoft; no IOC, no em dash; references exist; classification B/2 consistent with a single Datadog primary (sources.json reliability B). Run record: 27 updated ids, record counts (6 update, 10 correction, 11 improvement, 12 internal) and 16 `last_seen` bumps, six registry products, `ambiguous_labels` verified on disk; KEV window re-derived (Aspera, Barracuda, Outlook, Chrome, FreeSWITCH, OpenSSH, Check Point covered). Coverage: no uncovered critical or high item found.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 3, advisory: 3)

### Findings summary (machine-readable)

See `work/2026-11-15T1407Z-audit/verification.iter2.findings.yaml` (12 records).
