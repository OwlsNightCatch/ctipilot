# Wave 08 kickoff (parallel waves)

Start the session for this wave with this message.

Read `prompts/cleanup-coordinator.md` on `main` and run cleanup wave 08.

Context for this session (left by the wave 02 session, 2026-10-21). This wave becomes ready when wave 02's record is on `main`:

- **This session runs wave 08**: rows W4-06 and W2-04. W4-06 is a duplicate pair the wave 03 twin scan found (2026-06-12/the-gentlemen-ransomware-478-claimed-leak-site-victims-self, 2026-06-27/the-gentlemen-ransomware-claims-478-victims-and-adds-worm-pr): fold or link it first, as its row says. W2-04 is the fourth legacy batch (76 entries filed 2026-06-10 to 2026-06-21), taken from the row's `entries` list in `work/cleanup/plan.json`, never from `legacy_review.py --next`. It includes the WinRAR and ShinyHunters PeopleSoft entries wave 02 improved: re-verify them whole and apply their W1-I residuals from `work/cleanup/wave-06/findings-W1-I.md` in the same record.
- These rows carry no fresh findings, so they need truth passes first (§ C2, § C3): about four `cti-verification` passes of 19 to 20 entries in one spawn message, with the envelope of `prompts/quality-audit.md` Phase 1. Then about four repair workers, and the rest of the 20 spawns for the verifier loop. Mark the batch with `python3 tools/legacy_review.py --done "$RUN_ID" <ids>`.
- Sync first: `git fetch origin main && git merge --no-edit origin/main`, then read `CLAUDE.md` and `prompts/cleanup-coordinator.md` (v4.23) in full. Waves now run in parallel, one session per wave, on lanes the tracker keeps disjoint. Before the claim, confirm on `main` that the tracker marks this wave `ready` and that `python3 work/cleanup/render_status.py --check-lanes` passes. Write the claim as `partial $STARTED wave=08`, and in the same commit set the wave `in-flight <RUN_ID>` and its rows `in-wave 08 (<RUN_ID>)` in `work/cleanup/plan.json`, then re-render `docs/cleanup/STATUS.md` (§ C1).
- Run id: before the claim, check that `work/<RUN_ID>/` does not already exist on `origin/main`. Run ids have minute precision, and on 2026-10-21 waves 03 and 05 both computed `2026-10-21T1147Z-audit`. If it exists, another wave started the same minute: take the next free minute.
- Other waves run at the same time. Touch only the entries your rows list in `work/cleanup/plan.json`. A fold partner, duplicate or defect on an entry another wave holds becomes a new tracker row and is never edited. A sync conflict on the tracker or the shared state files goes to `python3 tools/merge_state.py resolve`.
- Session budget: at most 20 sub-agent spawns, and the account-wide session limit is shared with the other waves, the daily intel fire (about 02:56Z) and the Sunday audit. A rate limit is a cut under § C8, never a retry loop. Do not start between Saturday 18:00Z and the Sunday audit's record landing on `main`.
- Lessons from waves 01 and 02 (`docs/audits/2026-10-20-cleanup-wave-01.md`, `docs/audits/2026-10-21-cleanup-wave-02.md`):
  - Write every changelog record with `tools/entry_record.py` (`add`, `amend`, `diff`).
  - The 2026-10-11 audit already fixed many listed defects, so check the current text first.
  - A score or workaround that only the CVE record carries cannot be cited (CVE Services API, cve.org and NVD are blocked citations). ENISA EUVD per-vulnerability pages are citable and carry the numbering authority's score.
  - Bind each citation to the clause its page carries. Wave 02's verifier passes kept finding a clause cited to a page that holds only part of it, or a paraphrase looser than the source.
  - Sweep a corrected claim through the main analysis, every earlier dated section and this fire's record summary.
  - An edited earlier section must not report events after its own timestamp.
  - Record summaries say nothing like "this entry".
  - Put "version" or "release" before a four-part version number (5.3.2.0), or the IOC scan reads it as an IPv4 address.
- End by updating your rows and the wave in `plan.json`, marking ready the waves this one unblocks, re-rendering the tracker, and queuing a session for each newly ready wave (§ C6).
