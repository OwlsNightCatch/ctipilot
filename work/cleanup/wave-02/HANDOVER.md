# Wave 02 kickoff (handover from wave 01)

Start the next cleanup session with this message.

Read `prompts/cleanup-coordinator.md` on `main` and continue the store cleanup program.

Context for this session (left by the wave 01 coordinator session, 2026-10-20):

- Sync first: `git fetch origin main && git merge --no-edit origin/main`, then read `CLAUDE.md` and `prompts/cleanup-coordinator.md` in full. § C0 is done: the tracker `docs/cleanup/STATUS.md` is rendered from `work/cleanup/plan.json` (edit the plan, then `python3 work/cleanup/render_status.py`).
- Wave 01 (`2026-10-20T0835Z-audit`) is published: report `docs/audits/2026-10-20-cleanup-wave-01.md`. It shipped the record tool `tools/entry_record.py` (use it for every changelog record: `add`, `amend`, `diff`), the page-check fixes, and most standalone W5/W6/W7 rows.
- **This session runs wave 02**: rows W1-B (57 imprecisions), W1-C (5 clean legacy-pending entries), W1-E (34 carried items), W1-F (8 reference-branch hunks), W1-H. Inputs are ready under `work/cleanup/wave-02/` (`findings-W1-B.yaml`, `findings-W1-C.yaml`, `findings-W1-E.yaml`, `W1-F-reference-hunks.md`). The 2026-10-18 verdicts in them were read before the 2026-10-11 audit's records landed: in wave 01 that audit had already fixed part of the defects on 8 of 13 entries and all of them on 3 more, so repair workers must check the current text first.
- These rows carry fresh findings, so no truth pass is needed (§ C2); budget about 4 to 6 repair workers of 12 to 20 entries each, the rest for the verifier loop. Legacy-pending entries in W1-B/W1-C get the rating, ATT&CK mapping and labelled lines their kind requires and then `python3 tools/legacy_review.py --done "$RUN_ID" <ids>`.
- Lessons from wave 01: a score or workaround that only the CVE record carries cannot be cited through the CVE Services API, cve.org or NVD; ENISA EUVD per-vulnerability pages are citable and carry the CNA's score. Em dashes in reader text are fixed wherever a wave writes a record; earlier records' summaries are append-only. A corrected claim often stands in two or three places (main analysis, an earlier dated section, the record summary): sweep them all, because `tools/claim_ledger.py` does not yet list sentences edited inside earlier sections (tracker row W7-14, a good standalone fix for that session).
- Session budget: one cleanup session at a time, one wave per session, at most 20 sub-agent spawns. Do not start between Saturday 18:00Z and the Sunday audit's record landing on `main`. Merge continuously on `claude/...` branches; never push to `main`.
- End by naming wave 03 in the tracker header and queuing the next session the same way (§ C6).
