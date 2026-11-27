**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T08:28:06Z · ended_at=2026-11-27T08:48:54Z · duration_seconds=1248

## Verification report — 2026-11-27T0355Z-intel (iteration 8)

Role: post-fix pass after NEEDS_FIXES iteration 7; final permitted iteration. Scope: all 329 claims of claims.iter8.yaml (every row answered, `tools/claim_ledger.py --coverage 8`: 329/329, 0 missing), including the 4 changed claims, all 11 entries read whole, run record read, `git diff HEAD` consulted for the 9 updated entries. 327 claims ok, 2 F3 (low confidence).

### Prior-iteration deltas (each source re-read this pass)
1. Zammad Contradiction paragraph (F4, iter 7 #1): DIVD case page metrics table read: "Mean Time to Acknowledge 07:20:51, Time between first alert and SOC pickup" and "Mean Time to Respond (MTTR) 19:16:51, Time between first attack and formal response" (quoted correctly). Alert 19:43:09 + 07:20:51 = 03:04:00, the report's pickup; alert + 19:16:51 = 15:00:00, six minutes before the report's CISO time of 15:06; MTTC 27:40:51 = 23:24:00. "neither source reconciles" is gone. Remediation true to source, no new unsupported claim.
2. Zammad "artex- plus a number ... artex.ops" (F3, iter 7 #2): report credential/IOC table lists API token artex-i13033 and account artex.ops@divd.nl. Correct.
3. NFS2ROOT sourcing_note (F11): fetch narration removed; provenance now says announcement for the flaw and four fixes, the later-updated CVE record (ENISA, watchTowr) for the four older branches. Correct (ENISA dateUpdated Nov 23; watchTowr table lists 5.10.275, 5.15.226, 6.1.193, 6.6.163).
4. Mitel "As of that revision, no source read named ..." (F11): correct and now dated.
5. Puppet "about two and a half hours" (F11): Huntback scout 06:04:17, chain 08:39:58 (2 h 35 min), brief "Two and a half hours earlier". Correct.
6. Mitel Detection without path strings (F11): no /pictures, /awcuser, cgi-bin string remains (grep); "web pictures directory" is APEX's wording. Correct.

### Lore pages
The two lore.kernel.org claims (and the linux-nfs patch citation) return the Anubis bot challenge to me this pass (re-tried the /raw form). Verified against the saved raw copies under work/2026-11-27T0355Z-intel/fu1/ (kernel_announce_raw.md: fixes in 6.12.117, 6.18.61, 7.3.2, 7.4-rc1, introduced in 3.16, nfsd4_sequence() root cause; lore_jean_patch_raw.md: 2026-08-17 patch) and against ENISA EUVD-2026-130020, OpenSec and watchTowr, which carry the same text. NCSC.ch post 13244 (not machine-checkable) read by hand via ncsc-csh: "Audit the fleet list for router names your team did not create." is verbatim.

### Citation does not support the claim
- F3 #1 (low confidence), nginx entry, Defender takeaway (claim e30638e785): "disabling HTTP/2 on exposed listeners blocks only the two HTTP/2 flaws and, if it stays on elsewhere, leaves connection pressure ([Unit 42, 2026-11-24](...))". Unit 42's Mitigations section covers CVE-2026-123633 only ("disable HTTP/2 on exposed listeners ... the extra HTTP/1.1 connections can push the same worker closer to its worker_connections limit"). "blocks only the two HTTP/2 flaws" is Xint's ("It does not block the other three nginx vulnerabilities"), cited only later in the sentence. Older text, not in this run's diff. Fix: end the first clause with the Xint citation.
- F3 #2 (low confidence), Puppet entry, 2026-11-27 section (claim 1096cd85c5): the entry says Huntback advises refusing at a reverse proxy "any report that contains a type definition, which no agent sends". Huntback step 6: "No agent sends a type definition in a report. A reverse proxy rule that refuses any report containing `RubyMethod` stops this payload and its variants." The entry attributes a broader rule than Huntback gives. Fix: name RubyMethod, keep "no agent sends a type definition" as Huntback's observation.

### Editorial / less-is-more flags (advisory)
- F11 #1 (low confidence), Zammad 2026-11-27 section: "Jira's OAuth consumer key" vs report "Jira RSA-SHA1 OAuth consumer private key exfiltrated (app-level credential)". Say "consumer private key".
- F11 #2 (low confidence), SoftwareOK body: "(the entry's reading, since ASEC gives no window)" is a self-reference to the entry in reader-facing prose. The caveat is right; rephrase as "an inference".

### Carried and already logged (not counted, not grown)
Zammad main analysis 1,033 words (logged for audit); Fragnesia, Mitel and ARTEX main analyses at 550; long summary fields; Puppet release-notes citation label 2026-11-12 (page says only "Released November 2026"; logged in the run record notes); Ruby Exposure line's `ruby -v` hint not in NCSC.ch's post (iteration 5 advisory, unresolved by design).

### Other checks, no finding
- Dedup: NFS2ROOT (CVE-2026-99362, trend key new) and SoftwareOK have no prior coverage in prior_coverage.json or the CVE index; the nine updates are the same findings (CVE ids / entities match); record types fit (update records carry new in-the-wild or vendor evidence).
- Changelog contract: each of the nine entries has one new record for this run_id, a matching "## Update" section, updated_at equal to the record's at; summaries match sections; no silent edit seen in the diff; no internal-only language in reader-facing text; no IOCs (APEX/Huntback/ASEC/DIVD hosts, paths, hashes, task names not reproduced); no em dash outside headings.
- cves[] authority: Zammad scores (DIVD records 8.7, 8.5, 9.4 chained), PAN-OS fixed builds (advisory table, 20 builds) and CVE-2026-46300 builds (PAN-SA-2026-0015, 20 builds), Mitel (MISA-2026-0012 table, five ids, KEV five), nginx per-CVE ranges (nginx.org) and NCSC-NL scores, Juniper (ENISA 9.8, ranges), Puppet (EUVD 9.4, Red Hat 9.9), Ruby (EUVD 7.4), NFS2ROOT (9.8 CVE record, Red Hat 9.4) all match. F5 K-articles remain unreadable (run record logs it).
- Missed angles: KEV window carries no addition after 2026-11-26 (kev-window.txt; the 2026-11-25 additions were handled by the previous fire); NCSC.ch hub newest post is 13244 (covered); no gap found. Coverage looks complete for the critical/high signal.
- Priority/classification: no miscalibration I can evidence; NFS2ROOT and SoftwareOK notable, B/2 consistent with single-vendor-research sourcing.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 0, advisory: 2). All four findings are low confidence and small; none touches an action, a CVE field or a version number. Iteration 8 is the cap, so the run publishes with these as residuals.

### Findings summary (machine-readable)
See verification.iter8.findings.yaml (4 records).
