**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T03:55:54Z · ended_at=2026-10-11T04:04:59Z · duration_seconds=545

## Verification report — 2026-10-11T0256Z-intel (iteration 2)

Scope: post-fix pass. All 113 claims of the ledger (`claims.iter2.yaml`) were walked, i.e. every changed claim and every other claim of all five entries (all five were remediated); rows in `verification.iter2.claims.yaml` (113 rows, 107 ok, 6 non-ok). Every cited page was fetched this iteration with `extract` (22 pages); the IDC Frontier fourth report (2026-10-09) was also read and neither contradicts nor changes the entry. Prior-iteration deltas 1 to 11 checked: 1 (Denmark ministry URL now at the Ritzau copy, resolves, dateline 5.10.2026 matches sources[0]), 2 (21 days 17 hours cited to the Copenhagen Post, verbatim), 3 (Socket framing cited to Socket, verbatim), 4 (ccTLD "registries compromised" matches Google's "attackers compromised the third-party ccTLDs"; Triage narrowed to google.com.gh, google.sl, google.as as THN states), 5 (Denmark sourcing_note attributions match the pages, but see F4 #1 for a surviving contradiction), 6 ('the hacker'/'they' now used), 7 (Register dropped from the note; the run record's mention of it is accurate, S3 fetched the article), 8 (IDCF routine, shorter; see F7), 9 (ccTLD classification B/1 matches the google-tag record in sources.json), 10 (libgcrypt and port list removed; references added and resolve), 11 (T1053.005, T1543.002, T1543.001, T1485, T1552.005 are each supported by Socket's persistence and dead-man-switch text and are declared in the record's fields). Missed angles: two spot searches (zero-day exploitation this week; Swiss municipal/cantonal incidents) found only items already in the store (CVE-2026-104286, CVE-2026-76504, CVE-2026-86950, the NetScaler zero-day entry) or unconfirmed claims; coverage looks complete for the window.

### Citation does not support the claim
- #1 (F3, low confidence) 2026-10-06/denmark-cpr-population-register-third-party-access-breach, Defender takeaway: "shows that password quality and multi-factor sign-in on the accounts that hold register lookup access are part of the register's own exposure" is cited to the Copenhagen Post page, which reports three accounts incl. the administrator using 123456 and says nothing about multi-factor sign-in. Iteration 1 raised this; the remediation removed 'intermediary' and 'delegated' but kept the MFA clause. Remove it from the cited clause or mark it as the entry's own inference.
- #2 (F3, low confidence) 2026-10-11/cctld-registry-hijacks-gh-sl-as-certificates-for-google, summary (and the registry summary): "obtained unauthorized HTTPS certificates for Google domains and for domains of other organizations; Chrome blocked them and the issuing authorities revoked them." Google: "We also worked with the issuing CAs to ensure the certificates were revoked" (the Google certificates); for the other organizations' certificates: "we proactively blocked these certificates in Chrome", no revocation stated. Align with the body.
- #3 (F3, low confidence) 2026-10-11/poellm-botnet-github-poem-c2-exposed-ai-and-gitea-servers, body: "mostly in the United States and Western Europe" ends on a BleepingComputer citation; BleepingComputer says "the operation targeted systems across the United States and Western Europe". "Predominantly" is Lumen's word.
- #4 (F3, low confidence) entities/registry.yaml malware:poellm: "Lumen assesses with moderate confidence an Italian-speaking operator". Lumen's page: "We assess that PoeLLM is associated with an Italian-speaking threat actor" (no confidence level); "moderate confidence" is on Lumen's page for the administrative-interface server, and BleepingComputer is where "assess with moderate confidence that the operator is Italian" appears.

### Unsupported / hallucinated facts
- #5 (F4) 2026-10-06/denmark-cpr-population-register-third-party-access-breach, sourcing_note: "so every statement on how the breach happened comes from the register's side" is disproved by the update of 2026-10-11 and by the same note's last sentence ("the account of how access began is an anonymous hacker's claim to Politiken"; "the password finding is Politiken's reporting"). Supersession per 4c(h): rewrite or delete the clause.

### Drop (low relevance / off-audience / duplicate)
- #6 (F7, low confidence) 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups: no vector, no actor, priority routine; the rubric allows two sentences at most or a drop. The narrative is four long sentences (plus Exposure and Defender takeaway) and relays the attacker's 554,153-snapshot claim. Trim or accept as a residual.

### Editorial / less-is-more flags (advisory)
- #7 (F11) IDCF body: "the entry is carried for its supplier-concentration lesson, because ..." is composition rationale in reader-facing text; say the lesson directly.
- #8 (F11) Denmark sourcing_note: "(Politiken's own article is behind a paywall and only its lede was read)" is reading-depth narration; the note is also six sentences.
- #9 (F11, low confidence) ChainDrop: 12 em dashes in pre-existing reader-facing text (summary, actions[0], main analysis); none added by this run.
- #10 (F11, low confidence) registry product:tensorlake-npm-sdk first_seen 2026-08-06 predates the 2026-10-08 compromise.

### Analytical-link-as-fact
- #11 (F13, low confidence) 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver, actions[1]: the instruction to "remove the gh-token-monitor persistence that Socket and OX Security describe (a systemd user unit on Linux, a LaunchAgent on macOS, a scheduled task on Windows)" is attached to hosts that "installed a package from the keyv family since 2026-08-04". Sources: Socket 2026-10-08 and OX 2026-10-08 describe that persistence for tensorlake@0.5.144; OX 2026-08-04 says only "dead man's switch ... to delete the current machine" and persistence "through local AI agents and IDEs"; Elastic names none. The sequencing advice is sound for both waves, the artefact names are sourced for tensorlake only.

### Quantifier without source
- #12 (F14, low confidence) ChainDrop update section and record summary: "A second package carrying this payload family"; no cited source counts tensorlake as a second package, and the entry itself reports over 400 packages from the August wave. Use "a further package".

### Verdict
NEEDS_FIXES (truth: 7, editorial: 1, advisory: 4)

Passed without finding: all new-entry evidence quotes (Google, THN, Let's Encrypt forum, Lumen, BleepingComputer, IDC Frontier incl. the Japanese original and its translation) are verbatim; dates on sources[] match the pages' own datelines (Ritzau page metadata says 2026-09-29, its visible dateline 5.10.2026 07:00 CEST); IDC Frontier second and third reports, Jiji and BleepingComputer support every IDCF clause; the ChainDrop update's tensorlake facts (01:12:07 UTC publication, 11 minutes to flag, removal, 0.5.143 clean, valid provenance after main-branch modification, about 30 RPC endpoints, ONLOGON scheduled-task monitor, systemd/LaunchAgent/scheduled-task removal steps, OX's independent-actor caveat) match Socket, Endor Labs and OX; the changelog records of both updated entries carry every changed field in `fields`, `updated_at` equals the non-internal update `at`, and the record summaries match their sections.

### Findings summary (machine-readable)
See `verification.iter2.findings.yaml` (12 records).
