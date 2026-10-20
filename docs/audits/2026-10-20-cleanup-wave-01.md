# Cleanup wave 01, 2026-10-20

**Run record:** [runs/2026-10-20/2026-10-20T0835Z-audit.md](../../runs/2026-10-20/2026-10-20T0835Z-audit.md) · **Prompt:** v4.22 · **Program:** [prompts/cleanup-coordinator.md](../../prompts/cleanup-coordinator.md) · **Tracker:** [docs/cleanup/STATUS.md](../cleanup/STATUS.md)

## Scope

First wave of the store cleanup program, run by the coordinator session after § C0 (tracker and plan on `main` as `0f2be64`; claim `partial 2026-10-20T08:35:28Z`, base `0f2be64`).

- **W1-A:** the 16 entries the 2026-10-18 audit's truth passes T1 to T9 found with factual errors outside its week (`work/2026-10-20T0835Z-audit/findings-w1a.yaml`). Those passes read the store before the 2026-10-11 audit's records landed, so each defect was re-checked against the current text first.
- **W7-01, W7-02:** the record tool and the gate false positives (§ C7 items 1 and 2).
- **W6-04:** the one open store warning.
- Standalone W5, W6 and W7 rows that needed no sub-agent, each shipped as its own merge during the wave (§ Tool, doc and state changes).

## Verdict

**13 of the 16 W1-A entries carry a record from this wave: 9 corrections, 3 updates and 1 improvement.** The other three (Kairos Libercourt, Bitget, Apple CoreGraphics) needed none: the 2026-10-11 audit had already fixed every defect the passes listed. Of the 13, the 2026-10-11 audit had fixed part of the listed defects on eight; the remainder is fixed here. Two of the 13 are legacy entries (THORChain, actions-cool), which also received the labelled lines their kind requires and left the legacy queue (408 to 406 pending).

Verification: five `cti-verification` passes (152 to 158 claims each for the full passes). Iteration 3's CLEAN was refuted by the confirmation pass on three citation-precision points, all fixed; iteration 5 confirmed those and found one more instance of the Check Point wording, fixed after the pass and published on the early-exit rule with residual 1. Budget: 8 of 20 spawns, about 2.93 M sub-agent tokens.

## Findings applied and declined (W1-A)

| Entry | Record | Applied | Declined |
|---|---|---|---|
| 2026-10-02 Zammad CVE-2026-102489 | update | "6.5 and older receive no security fixes" superseded by Zammad 6.5.5 (2026-10-15), an emergency fix for CVE-2026-102489 on the unsupported 6.5 series from a new package repository; headline, summary, fixed version, action, takeaway and the 2026-10-10 section moved with it | none |
| 2026-10-10 GhostAction | update | GitGuardian's 2026-10-13 update replaces "the larger figure stays unconfirmed": more than 30,000 repositories, about 1,900 compromised accounts, GitHub blocking the workflow from 2026-10-09 | none |
| 2026-05-18 THORChain (legacy) | correction | One of five vaults and about $10.7M by THORChain's count, with The Record's six vaults and TRM Labs' more than USD 11M attributed to them; the GG20 exploit confirmed and the analysis rewritten from THORChain's two reports; labelled lines added | none |
| 2026-05-20 actions-cool (legacy) | update | GitHub disabled both repositories on 2026-05-19, not one; both came back on 2026-09-16 with the malicious tags intact, SafeDep reported new infections, both disabled again by 2026-09-25 (Socket, The Hacker News); T1204.002 mapped; labelled lines rewritten | none |
| 2026-07-29 TeamCity CVE-2026-63077 | correction | CVSS 9.8 from the CVE record JetBrains published as numbering authority, cited through ENISA's EUVD page (EUVD-2026-49369); the 2026-08-06 wording dated; actions match JetBrains' advice to restrict external access | none |
| 2026-08-04 Liechtenstein VWBP | correction | Only the several-hours download is attributed to Fabian Schmid; the access mechanism is NZZ's own reporting | five, already fixed by 2026-10-11T1307Z-audit |
| 2026-09-17 Mandiant AI report | correction | The headline no longer says the poisoned package spread the worm (an attacker used a hijacked AI coding-assistant session); the hardening and hunt lines of cases 1 to 7 and the closing narrative of case 8 carry their citation | five, already fixed by 2026-10-11T1307Z-audit |
| 2026-09-18 Acronis CVE-2026-87886 | improvement | The KEV listing names only the cPanel & WHM plugin and the Plesk extension | two, already fixed; the JSON primary stays because the human-readable advisory page is an empty script shell |
| 2026-09-19 Unbound CVE-2026-81642 | correction | The 9.1 score is NLnet Labs' own (NCSC-CH restates it); the headline gives the sourced digest-buffer overflow; 8.4 restored for CVE-2026-82717 | one, already fixed |
| 2026-09-23 Check Point CVE-2026-93616 | correction | R82.20 Take 10 and later added to the immediate action; detection and triage follow Check Point's 2026-10-13 revision of sk1000171, and the disagreement with Bishop Fox over the first indicator is stated | one, already fixed |
| 2026-09-24 SolarWinds Observability | correction | "SolarWinds connects the WPM changes to neither CVE" narrowed to what the release notes say; neither trust-center advisory gives a workaround; only CVE-2026-28324 is network-reachable | one, already fixed; a CVE-2026-28324 workaround the repair worker found only in the CVE record, which no citable page carries (main-agent decision, see below) |
| 2026-09-24 ClosedQuorum | correction | The failure modes are Talos's own list; Talos calls only the tie-break deterministic | two, already fixed |
| 2026-09-28 UNCTAD scan | correction | Tags reduced to `ai-abuse`; the data and the API key were public, and the researcher's own caveat (such queries look like a hacker's to a site administrator) and Alex Stamos's "borderline" are quoted beside his "I don't think I'd call it that"; the payload pages' agent-chosen labels described, not reproduced (a carried advisory) | one, already fixed |
| 2026-09-17 Kairos Libercourt | none | | all, already fixed |
| 2026-09-29 Bitget | none | | both, already fixed |
| 2026-09-30 Apple CVE-2026-86950 | none | | both, already fixed |

**SolarWinds decision.** The repair worker cited ENISA's EUVD page for a Player Password workaround on CVE-2026-28324 and put the quote in `evidence[]` against the CVE Services API. The EUVD record read today carries the description and four SolarWinds references but not the workaround sentence, neither SolarWinds advisory nor its secure-configuration page carries it, and the CVE record endpoint may not be cited. The workaround clause, its two sources and the evidence row were removed; the narrowing stays.

Registry and state from the records: `incident:thorchain-gg20-tss-vault-drain-11m-nine-chains-switzerland` summary rewritten to the corrected figures; `incident:actions-cool-issues-helper-github-action-compromised-53-tag` gains a `part-of` edge to `campaign:mini-shai-hulud` (Socket, 2026-09-24: both actions "were compromised in the May 2026 Mini Shai-Hulud campaign"); `last_seen` moved to 2026-10-20 for CVE-2026-102489 and CVE-2026-63077. Em dashes were removed from the reader text of the VWBP, Mandiant, Acronis and ClosedQuorum entries; those left in earlier records' summaries are append-only.

## Folds

None this wave: W4 is wave 03.

## Tool, doc and state changes

Each shipped as its own merge to `main` during the wave, except the two rows marked "wave commit".

| Row | Commit | Change |
|---|---|---|
| W7-01 | `6c75002` | `tools/entry_record.py` (`add`, `amend`, `diff`) with `tools/test_entry_record.py`; `CLAUDE.md` Key commands row. Both repair workers wrote every record with it. |
| W7-02 | `4ca3e3b` | `check_run.py` `_page_text`: extract mode skips the tag stripper, link labels "(opens in a new window)" and the cache header are dropped, an image-only or near-empty PDF is unreadable rather than "does not mention"; `tools/test_check_run.py` |
| W7-03 | `bfded2c` | `tools/migrate_briefs.py` and `tools/migrate_updates.py` removed (2,407 lines), their mentions updated |
| W6-06, W7-07 | `f06331d` | 98 struck backlog rows older than 30 days removed; `.pyc`, `*.tmp`, `.log` files and a KEV catalogue copy removed from `work/`, and `.gitignore` keeps them out |
| W7-09, W7-10, W7-11 | `11ff607` | unused `marked.min.js` and `purify.min.js` removed with their hash rows; `#/weekly` hash routes land on the brief; root `.nojekyll` removed; the build's one Python deprecation warning fixed |
| W7-04, W7-06 | `7864387` | README file tree, `site/README.md`, `docs/architecture.md` and `docs/pipeline.md` brought up to date |
| W7-13 | `f037aa0` | `check_run.py` runs every `tools/test_*.py` suite next to `site/test_build.py` |
| W6-01, W6-02, W6-03 | `f5df6fe` | the 2026-10-11 recommendations 5 to 7 decided and noted on the source records: Red Canary already repointed to the Zscaler feed by 2026-10-20T0256Z-intel; `ssd-disclosure` kept (it reads again); `google-tag` kept separate from `mandiant-gtig` (different content) |
| W5-01, W5-03 | `8678b51` | registry summaries corrected: Eurail (the retracted DPA/EDPS review), BeaverTail (not "an initial loader" in the 2026-09-18 joint advisory) and InvisibleFerret (no "after BeaverTail loader execution") |
| W6-04 | wave commit | `state/warning_acknowledgments.json`: the 2026-10-18 audit's 32.6 h duration acknowledged (its own notes say it spans the rate-limit pause) |
| (loop) | wave commit | `check_run.py` `verification-confirmation` messages name the iteration from the record's `iteration:` key (they printed `iteration None`) |

Checked and left unchanged: no registry orphan duplicates a live key (W5-04, 179 records), no orphan product has a canonical twin (W5-05, 4 records), and all 25 earlier acknowledgment rows still match a warning. Declined: removing the `update_of: null` default (W7-05; 654 entries carry the key) and the `/live/` redirect (W7-12; an operator-documented legacy route).

## Not reached

Wave 02 and later, as planned in the tracker: W1-B (57 imprecisions), W1-C (5), W1-E (34 carried items), W1-F (8 reference-branch hunks), W1-H, then W4, W1-D, the legacy queue (406 pending), W3 (71 entries) and the 4 entry-scoped acknowledgments (W6-05). Inputs for waves 02 and 03 are prepared under `work/cleanup/wave-02/` and `work/cleanup/wave-03/`. New items noticed this wave and added to W1-E: the VWBP entry's first eight evidence quotes are untranslated German (the running text glosses its German quotes), and the Drupal SA-CORE-2026-014 entry has an evidence quote and a CVE clause the cited page no longer carries (W1-H).

## Tracker delta

New row W7-14: `tools/claim_ledger.py` lists no claims for sentences a fire edits inside earlier `## <Type> — <at>` sections, so post-fix passes can miss them (iteration 5 found one by reading the diff). Rows done this wave: W7-01, W7-02, W7-03, W7-04, W7-06, W7-07, W7-09, W7-10, W7-11, W7-13, W6-01, W6-02, W6-03, W6-04, W6-06, W5-01, W5-03, W5-04, W5-05, W1-A, W1-G. Declined: W7-05, W7-12. New: W1-H. Next: wave 02.
