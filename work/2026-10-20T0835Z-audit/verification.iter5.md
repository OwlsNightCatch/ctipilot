**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-20T10:10:51Z · ended_at=2026-10-20T10:23:54Z · duration_seconds=783

## Verification report — 2026-10-20T0835Z-audit (iteration 5)

Scope walked: 68 ledger claims, all with a row in `verification.iter5.claims.yaml` (all `ok`): the 10 changed since iteration 4 (c263d75eb5, 2ede79b075, 25924232d5, e80e866338, ec3458cc6e, cea0826acd, cea4230118, f9b0ae5171, 825f539e1c, b5a5427842); every other claim of the three entries remediated after iteration 4 (TeamCity 10, Unbound 13, Check Point 13, 36 in all with the changed ten); and a seeded quarter of the other 126 claims, 32 of them, drawn with `random.Random("2026-10-20T0835Z-audit-iter5").sample` over the ledger order of the 126 (THORChain 8, actions-cool 6, Mandiant 5, UNCTAD 4, Zammad 3, ClosedQuorum 2, VWBP 2, Acronis 1, GhostAction 1). I also read the three remediated entries end to end, read `git diff --word-diff` of all 13 entries (see the coverage note), and checked the run record's notes and the wave report against disk, git and state.

### Prior-iteration deltas (iteration 4 findings)

- **TeamCity F3, remediation correct.** The follow-up (https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/) says: "If your TeamCity server is publicly accessible over the internet and you are unable to apply one of the available mitigation options immediately, we strongly recommend temporarily restricting external access until you have done so." and, separately, "Internet-facing TeamCity servers should also consider requiring connections through a VPN or implementing an additional security layer". The Hardening sentence and the 2026-10-20 section now carry exactly that split. The 9.8 / CVSS 3.1 / JetBrains-as-CNA claim holds on EUVD-2026-49369 (API: baseScore 9.8, vector AV:N/AC:L/PR:N/UI:N, assigner JetBrains, published 2026-07-27); the advisory's "pointer since 2026-08-07" holds ("August 7, 2026 update: Please also see this follow-up").
- **Unbound F3, remediation correct for the two passages it named.** EUVD-2026-80291 API: assigner NLnet Labs, baseScore 9.1, CVSS 4.0, vector identical to the one NLnet's advisories page links from "Severity: Critical". The advisory page carries the vector link and the rating and no numeral, and the entry now cites it only for those. The 2026-10-11 section no longer calls NLnet the numbering authority for CVE-2026-82717. NCSC-CH post 12957 states "CVE-2026-81642 CVSS4.0: 9.1 (CRITICAL)", so "restates" holds.
- **Check Point F3, remediation correct in two places, incomplete in a third (finding #1).** Bishop Fox (2026-10-01): "The route in this post never calls that service, so it leaves neither the ERROR line nor a ../"; sk1000171 (lastModified 2026-10-13) lists indicator 1 and 2a to 2c and no load-error grep, so "the revised sk1000171 no longer lists that indicator" holds. The main analysis, the 2026-10-20 section and this fire's record summary are right. The 2026-10-04 Update section still says "replaced in the 2026-10-13 revision of sk1000171" on a Bishop Fox-cited sentence.
- **F11 (check_run.py change), remediation correct.** `git diff HEAD -- tools/check_run.py` adds `_iter_no` and uses it in three verification-confirmation messages; the report's change table and the record's notes name it.

### Citation does not support the claim

- **#1 (F3, low confidence), 2026-09-23 Check Point, section "Update — 2026-10-04T05:12:00Z".** Quote: "Bishop Fox says Check Point's second indicator at the time (an upgrade-tools load-error grep, replaced in the 2026-10-13 revision of sk1000171) fires only when an upgrade-tools load fails and is never reached by this route ... ([Bishop Fox, 2026-10-01](https://bishopfox.com/blog/weaponizing-check-point-management-cve-2026-93616))". Bishop Fox's post (dated 2026-10-01) cannot report a 2026-10-13 replacement; sk1000171 (https://support.checkpoint.com/results/sk/sk1000171/, lastModified 2026-10-13) lists "Authentication bypass indicator" plus 2a, 2.b, 2.c and says nothing of a replacement. Same class as iteration 4's finding #3, left standing in this third place, and it narrates a 2026-10-13 event inside a section dated 2026-10-04. Fix: delete the parenthetical, or write "as sk1000171 then listed it".

### Editorial / less-is-more flags (advisory)

- **#2 (F11, low confidence), THORChain:** "Verichains' TSSHOCK attacks on weak zero-knowledge proofs": the page lists three attacks (alpha-shuffle on ambiguous encoding, c-split and c-guess on dlnproof soundness); the phrase fits two and the third only indirectly.
- **#3 (F11, low confidence), Mandiant case 6:** "define per-agent cost-cap thresholds and bounded recursion limits": Mandiant says "cost-cap thresholds" and "financial caps, bounded recursion limits and rate-limits ... at the Service ID and project-level"; "per-agent" is the entry's gloss, now vouched for by the citation this run added.
- **#4 (F11, low confidence), Unbound:** the 2026-10-20 record summary does not mention the title's added "and 8.4" or the "(CVSS4.0)" label on CVE-2026-82717's cvss; both are in `fields` and correct (EUVD-2026-80292: 8.4, CVSS 4.0).

### Coverage note (process, not a run defect)

`claims.iter5.yaml` has no rows for sentences this run edited inside earlier sections: TeamCity 2026-08-06, Unbound 2026-09-30, Check Point 2026-10-04. I read all three from the word-level diff. TeamCity's ("as of 2026-08-06 that advisory had not been revised since 2026-07-27", "the ransomware use and the Cadence breach came later (2026-09-30 update)") holds and is consistent with the advisory's 2026-08-07 update note. Unbound's ("The CVSS 4.0 score of 9.1 for CVE-2026-81642 is the score of NLnet Labs' own vector ([NLnet Labs])") holds by derivation (the linked vector is identical to EUVD's 9.1 record) and I did not flag it; the main agent may prefer to cite EUVD-2026-80291 there too. Checked and not flagged: the UNCTAD section's flat "involved no authentication bypass" (three earlier verifiers passed it; the record summary hedges it correctly and the key is public per swarmcha.se "It is not a secret key").

### Other checks, all holding

- **Run record notes:** 13 updated ids, 13 records of this run (9 correction, 3 update, 1 improvement, none internal; the three `update` records equal `updated_at`: Zammad 08:40:20Z, GhostAction 08:42:29Z, actions-cool 08:49:45Z); THORChain and actions-cool 408 to 406 pending (`state/legacy_review.json`); registry diff (THORChain summary, actions-cool `part-of` campaign:mini-shai-hulud, Socket 2026-09-24 "compromised in the May 2026 Mini Shai-Hulud campaign"); `cves_seen` last_seen moves; the SolarWinds workaround removal (EUVD-2026-84807 carries four references and no workaround; neither trust-center page has one).
- **Wave report:** every commit hash resolves in `git log` (6c75002, 4ca3e3b, bfded2c, f06331d, 11ff607, 7864387, f037aa0, f5df6fe, 8678b51); 2,407 lines removed (2003 + 404); 98 backlog rows removed; 654 entries carry `update_of`; acknowledgment rows 25 to 26 and the new row's facts match runs/2026-10-18/2026-10-18T1307Z-audit.md (14:12Z to 16:15Z pause, 117266 s); em dashes absent from the reader text of all 13 entries (only earlier records' summaries on VWBP keep them, append-only); the VWBP entry's first eight evidence quotes are untranslated German; W1-H's Drupal row exists in the tracker.
- `python3 tools/check_run.py 2026-10-20T0835Z-audit`: 58 pass, 0 warn, 0 fail (quote-literal 12, citation-cve 4).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 3)

### Findings summary (machine-readable)

See `work/2026-10-20T0835Z-audit/verification.iter5.findings.yaml`.
