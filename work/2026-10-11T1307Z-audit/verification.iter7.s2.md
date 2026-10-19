**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:09:14Z · ended_at=2026-10-19T18:33:10Z · duration_seconds=1436

## Verification report — 2026-10-11T1307Z-audit (iteration 7, slice s2)

Scope: 27 entries (verify-scope.iter7.s2.txt), 233 ledger claims, all answered in `verification.iter7.s2.claims.yaml` (230 ok, 2 F3, 1 F14). Post-fix pass: every ledger claim was walked, not a sample, and every entry was read whole (frontmatter, main analysis, labelled lines, every changelog section, `git diff HEAD` for this fire's change). Every cited page was fetched this iteration: `extract` for pages, `url` for raw-HTML dateline/JSON-LD/CVSS checks and the Next.js data of Check Point sk1000171 and the SolarWinds advisories, `cisa-kev` for the catalogue (KEV rows for CVE-2026-31431, -42208, -88771, -93616, -85046, -35616, -39682, -39964, -53266), `ncsc-csh post` for hub posts 12551, 12839, 12957, `pdf` for Microsoft's Q3 Cyberattack Series report, the MSRC SUG API for the MSRC update-guide page, cveawg.mitre.org for 17 CNA records, `WebFetch` (template) for the two cisa.gov alerts (read) and Computing UK (403). Computing UK and the NLnet `.txt` advisories were read through the jina fallback inside `extract`; OX Security pages were read from the gate's cached bodies (they answer 403). CVSS 4.0 scores for NLnet's CVE-2026-82717 (8.4) and CVE-2026-81642 (9.1) were recomputed from the published vectors. For the Linux kernel entry, all 17 fixed-release claims were checked by matching each KEV-listed stable commit SHA against the cited kernel.org ChangeLog: every release carries one.

### Deltas from iteration 6

| Prior finding | Remediation | Result |
|---|---|---|
| Copy Fail F8 (checksum point missing from Detection) | Applied | Holds. Detection now reads "file-integrity tools comparing on-disk checksums miss the corruption, because the on-disk file is unchanged and only the page cache is modified"; Xint: "Standard file integrity tools comparing on-disk checksums will miss it". |
| Check Point F3 (sk1000171 indicators changed 2026-10-13) | Applied | Holds against the live page (lastModified 2026-10-13). The Detection paragraph lists Indicator 1 (username over 1,000 characters) and 2.a to 2.c as sk1000171 does; immediate_action and actions no longer claim the indicators miss the route. Two readability points raised as advisory F11 below (anachronistic section stamp; Update still speaks of the old "second indicator"). |
| ChainDrop F3 ("explicitly ... rather than a new family") | Applied | Holds. Elastic: "Elastic Security Labs identified the return of Shai-Hulud"; "strings with Dune-themed references and has similarities to previous Shai-Hulud campaigns". |
| ChainDrop F11 (repeated switch passage) | Declined (attribution) | Rationale does not address repetition; kept as advisory F11. |
| PHP SOAP F3 ("no credentials" uncited) | Applied | Holds. Takeaway now: "the use-after-free is triggered by a crafted envelope" cited to GHSA-85c2, whose reproducer is a crafted SOAP envelope. |
| Storm-2570 F3 ("each of these behaviors") | Applied | Holds. "Microsoft's own post closes with Defender XDR detections and mitigations for the affiliate's toolchain": the post has "Mitigation and protection guidance" and "Microsoft Defender detections" tables; no per-behavior claim remains. |
| PHP SOAP F11 (CVE-2026-7262 CNA 2.9 vs advisory 6.3) | Declined (minor) | Evidence stands: GHSA-hmxp-6pc4-f3vv Moderate 6.3, CNA record 2.9 Low. Kept as advisory F11 (low confidence). |
| SEPPmail F11 (record summary says four retypings, section names two) | Declined | Rationale holds in part: the section names the two retypings a reader acts on, the main analysis gives all four types, and the CVE records confirm the four (CVE-2026-44125 auth-bypass, -44126 deserialization, -44127 path-traversal, -7864 info-disclosure). Not re-raised. |

### Citation does not support the claim
- F3 #1 SEPPmail (claim 2cd9ea3583): "CVE-2026-44126 (9.2), an insecure deserialization, was fixed in 15.0.3, while NCSC-CH's advisory says the vulnerabilities were fixed in 15.0.4 ([NCSC-CH, 2026-05-08])". The only citation is NCSC-CH post 12551, whose summary reads "Several vulnerabilities have been fixed in SEPPmail Secure Email Gateway 15.0.4" and which gives CVE-2026-44126 no fix version. The 15.0.3 reading is InfoGuard's table ("15.0.3 | CVE-2026-44126") and The Hacker News, neither cited here (InfoGuard is cited for the same fact only in the 2026-05-20 Contradiction line). Fix: cite InfoGuard after "15.0.3".
- F3 #2 Bitget (claim 9f934072b6, low confidence): the 2026-10-11 Correction says "Bitget's incident page, updated on 2026-10-03, now states ..." The live page reads "Updated: October 14, 2026" and carries no 3 October date (latest dated event: October 2). The quoted wording is on the page; the update date cannot be confirmed. Fix: drop the date.

### Quantifier without source
- F14 #1 SAP (claim b630166e5f, low confidence): "Three further notes Onapsis classes as HotNews matter to different estates." Onapsis lists five HotNews (3771065, 3765948, 3747367 update, 3714806, 3758900); after CVE-2026-58231 that is four further, and the entry itself says Onapsis counts "five HotNews". Fix: "Further HotNews notes ...".

### Editorial / less-is-more flags (advisory)
- F11 #1 ChainDrop containment paragraph states OX's dead man's switch and Elastic's intimidation reading twice in one paragraph and a third time in the Correction (unchanged from iteration 6).
- F11 #2 PHP CVE-2026-7262: GHSA 6.3 Moderate vs CNA record 2.9 Low not surfaced (low confidence; unchanged from iteration 6).
- F11 #3 Em dashes in reader-facing text: ChainDrop (title, summary, actions, body), Lazarus (title, actions, body), SAP (actions, body), Chrome (title), Entra (summary, body).
- F11 #4 PHP and Exchange Correction sections narrate "The priority moves from notable to routine"; priority is a frontmatter field, and the reasons already sit in the analysis.
- F11 #5 Check Point: (a) the Correction stamped 2026-10-11T13:57:22Z reports a revision "on 2026-10-13"; (b) the 2026-10-04 Update still refers to "Check Point's second indicator" and "first indicator" in the old numbering without saying it means the earlier set.

### Considered, not raised
- Check Point citation date: sk1000171 page data shows dateCreated 2026-09-20 vs the cited 2026-09-22; the page carries no visible dateline, Check Point's blog, The Hacker News and Bishop Fox ("On September 22, 2026, Check Point published sk1000171") date the public advisory 2026-09-22.
- Computing UK date: the jina reader prints "Published Time: Tue, 06 Oct 2026" for an article the 2026-09-25 update already cites; a crawl artifact, not a publication date. WebFetch answers 403, so the dateline could not be read directly.
- Gambit page JSON-LD datePublished is 2026-10-08 (CMS), but the visible dateline is "September 22, 2026", matching the entry.
- Check Point sk1000171 lists R82.20 as affected with no take qualifier; the entry's "without the Security Hotfix or Jumbo Hotfix Take 10+" follows from the same page's solution section and the Correction says so.
- SolarWinds CVE-2026-28325 advisory page metadata date 2026-02-03; the advisory's own "First Published 09/22/2026" matches the entry.
- Uncited CVE-record facts (PHP CNA 9.5 AC:H/AT:P; Check Point blog) match the CNA records; per-CVE record pages are barred as sources, so no citation is expected.
- Internal records (Lazarus references, Chrome techniques, Star Blizzard T1218.007, Storm-3068 T1556.006/T1580, Kernel affected ranges): source-supported; Storm-3068 and Kernel records touch body text, and both changes are citation or sentence additions the sources carry.
- Priority, classification and action discipline: no F16, F17 or F18 raised. Check Point's actions[0] and [1] echo immediate_action, which is the intended pairing for a critical entry; the list holds three actions.
- Coverage: no missed angle named for this slice.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 0, advisory: 5). One truth finding is firm (SEPPmail F3 #1, a missing co-citation on a true fact); the other two are low confidence (Bitget update date, SAP "Three further").

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter7.s2.findings.yaml` (8 records: 3 truth, 5 advisory).
