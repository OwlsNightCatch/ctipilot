**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-15T04:53:13Z · ended_at=2026-11-15T05:00:26Z · duration_seconds=433

## Verification report — 2026-11-15T0356Z-intel (iteration 3)

Scope: all 73 ledger claims (claims.iter3.yaml) were walked, including the 6 in claims.changed.iter3.yaml and every claim of the three remediated entries (ScreenConnect, Gentlemen, Cursor); PolinRider was also read whole. Every cited URL was re-fetched live this iteration with `extract` (Huntress, Cursor x2, Ransom-ISAC, Apiiro, Sonatype, JFrog, StepSecurity, Fireworks, heise, Microsoft, Phorion, Sophos) or `ncsc-csh post 13121`. Rows: work/2026-11-15T0356Z-intel/verification.iter3.claims.yaml (72 ok, 1 F3).

### Prior-iteration deltas (all six confirmed)

1. ScreenConnect F14 fix. Entry: "to register a guest client needs the server's relay address, which is embedded in that server's guest installer". Huntress: "To register, a guest client needs a ScreenConnect server's relay address, which is embedded in that server's guest installer." Facts correct, exclusivity gone. The sentence is ungrammatical (advisory below).
2. ScreenConnect F4 fix. Entry: "It considers the public suggestion ... unlikely". Huntress: "after further investigation, this doesn't seem likely." Correct.
3. Run record completed/duration: placeholders, not re-raised. Iteration timings recheck: iteration 1 04:32:53 to 04:42:26 = 573 s, iteration 2 04:44:55 to 04:51:57 = 422 s, both as recorded.
4. Gentlemen F5 fix. Entry: "Ransom-ISAC advises that a GPO of this shape found in a domain be unlinked and deleted, with its Preferences task file, before hosts are cleaned or credentials rotated" with citation. Ransom-ISAC: "Neutralize the GPO first, before cleaning hosts or rotating anything: 1. Unlink the GPO. 2. Delete the GPO and its Preferences task file." Correct.
5. Cursor F8 fix. Entry Exposure: "coding-agent traces from sessions outside Privacy Mode were exposed for fewer than 0.05% of users, all notified, so a user with no notice was not among them". Cursor (security-incident-update): "coding agent traces were exposed for fewer than 0.05% of users. We have identified these users and notified each of them directly. If you did not receive a notification, your data was not in these traces." Correct, cited to Cursor. Main analysis still reads coherently after the trim.
6. Gentlemen T1490. Source table: "T1490 | Shadow-copy deletion and change-journal deletion"; id active in the ATT&CK 20.1 pin (Inhibit System Recovery). Correct. All technique ids of the four entries are active in the pin.

### Citation does not support the claim

- #1 F3 (low confidence), polinrider-forged-commits-npm-hijacks-fake-recruiter, "the same wallet appears in GitGuardian's GhostAction report, which Sonatype says does not establish a shared operator" (cited to Sonatype). "The same wallet" binds back to "a hard-coded Ethereum wallet" in the Apiiro-cited clause, whose decoded sample reads wallet 0xa322 (Apiiro's table: A-family A4-A11 = 0xa322, fake-font wave = 0x1eEf, "reads a different wallet, 0x1eEf", plus 0x33ff). Sonatype says "This exact wallet appears in GitGuardian's October 27, 2026 report" about its own wallet, 0x1eef, in the 12 hijacked npm releases. Fix: "the wallet in the hijacked npm releases also appears in GitGuardian's GhostAction report ...", as the registry relation note already words it.

### Editorial / less-is-more flags (advisory)

- #2 F11, screenconnect-crypto-bait-guest-sessions-118-servers: "and to register a guest client needs the server's relay address, which is embedded in that server's guest installer" has no subject for "needs". Suggest "and a guest client needs the server's relay address, embedded in that server's guest installer, to register".
- #3 F11 (low confidence), cursor-marketplace-claude-code-extension-ssh-backdoor update section: Fireworks says the group is "aimed at selling tokens from unauthorized access to Large Language Models (LLMs) to illicit routing gateways" and files the 2026-10-23/24 cloud-provider event under "Further activity" of the same incident; the entry writes "sells access to language models" and "a second incident". Cosmetic.
- #4 F11 (low confidence), screenconnect Detection: literal guest version string; Huntress calls it "context indicator, not unique on its own" and the entry already says so. May be left.

### Checks that came back clean

- Frontmatter/body agreement, classification (B/2, B/2, C/2, B/1 consistent with sources.json letters and the corroboration shown), priority (all notable), techniques, evidence quotes, single-source flags with sourcing_note, no IOCs, no em dash in reader-facing prose (the only one is inside a verbatim Cursor evidence quote and the heading), no workflow vocabulary, references[] targets exist, check_run gate reproduced: 57 pass, 1 warn (the declared actor:thegentlemen dedup advisory; the Kaspersky 2026-11-07 entry is a different incident, so a new entry is right).
- Cursor changelog contract (4c): the update record covers every changed frontmatter line in `git diff HEAD` (summary, sources, evidence, techniques, actions, sourcing_note, body, updated_at mirror equals `at`); section carries a genuine, cited delta; main analysis, summary and Exposure now state the new origin and Open VSX position; no stale "not disclosed" text remains.
- Run record notes: KEV 0 additions (kev-window.txt), Security Hub post 13178 of 2026-11-13 (re-fetched), backlog row struck (diff of state/coverage_backlog.md), entry ids correct, publish counts match.

### Missed angles

None found. Spot searches for in-window exploited flaws and Swiss communal incidents returned only items the store already carries (Cisco SD-WAN CVE-2026-20245 on 2026-06-06, Node2Shell/Brotli on 2026-10-24 and 2026-11-07, FortiOS Swiss scan list on 2026-11-13) or nothing dated 2026-11-14/15. Coverage looks complete for the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 3). The single truth item is low confidence and a one-clause fix; everything else the previous iteration raised is correctly remediated.

### Findings summary (machine-readable)

See work/2026-11-15T0356Z-intel/verification.iter3.findings.yaml (4 records: F3 x1, F11 x3).
