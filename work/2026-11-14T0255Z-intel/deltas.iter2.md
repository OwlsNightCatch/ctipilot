# Prior-iteration deltas (iteration 1 NEEDS_FIXES: truth 13, editorial 3, advisory 4) and remediation applied

Check each fix first, then do your own cold pass over the ledger scope.

1. F3 Danfoss, main analysis "the first German cases followed" cited to BleepingComputer: now split: six more countries cited to BleepingComputer, German cases cited to heise (2026-11-03). verify: the clause now cites a page that names Germany.
2. F3 ScreenConnect, console statement attributed to ConnectWise: main analysis now says "ConnectWise says clients 26.6.5 and later block the transfer, and Microsoft adds that a cloud-console update does not update technician clients"; Huntress (2026-11-11) cited for the no-successful-jump observation; the Update section now says Microsoft relays ConnectWise's 26.6.5 statement and, "in its own words", the 2026-09-08 fix date and the console-update statement; sourcing_note says the console statement is Microsoft's own.
3. F3 ScreenConnect, "RMM+ requests with no matching login" cited to Blackpoint: now cited to Huntress (2026-11-11).
4. F4 ScreenConnect, ".NET compiler" as child of the client service: removed from that list; now "a scheduled-task PowerShell watcher that compiles an executable with the .NET compiler" cited to Microsoft.
5. F3 N-able, "from 2026-11-08 onward": Huntress (2026-11-09) cited alongside Field Effect.
6. F3 N-able, "no signs of compromise" cited to Huntress: the Update section now cites Tenable (2026-11-12) for it; the main analysis no longer carries the clause.
7. F3 Quay, eight fixed builds cited to the CVE-2026-110697 page for both CVEs: now "Red Hat's page for the second flaw lists the fixed builds ..." and Red Hat's CSAF record cited for "the same fixes for both flaws".
8. F3 Quay, service_key_rotate/service_key_delete detection: now cited to the CVE-2026-123710 page; the robot-token monitoring stays on the CVE-2026-110697 page.
9. F3 Luna Moth, dropped hedge: title now "law firms that likely did not pay"; body "which ReliaQuest says suggests they likely did not pay".
10. F3 Quay, solution article date: source record and inline cites now 2026-11-13.
11. F3 GitLab, detection page date: source record and inline cites now 2026-11-12 (the page's last-verified date); the read-date sentence in the sourcing_note was replaced.
12. F4 Danfoss headline "Strict mode no barrier": now "Strict mode does not remove them".
13. F5 Danfoss Update section, uncited BACS sentence: BACS link added.
14. F9 N-able Exposure, earlier Huntress allow-list guidance: the allow-list clause was removed.
15. F16 Ivanti priority notable vs high: DECLINED, no change. Reason: the cited facts show a national CERT's statement of public PoC code (source unnamed; the only repository found models the flaw rather than running Ivanti's build), Ivanti says no evidence of exploitation, no KEV listing, and no source shows a Swiss or public-sector deployment of Endpoint Manager, so criterion (a) of the high bar (plausible exposure of the profiled constituency) is not established; doubt about severity resolves to notable here and the action already says "now".
16. F11 Ivanti Update section "the entry lacked": rewritten to "so 5.0.8.1 is the fixed build".
17. F11 Danfoss title and summary accretion: title and summary were rewritten (not appended to); verify they carry the current state and nothing false.
18. F11 actor alias split: the aliases "Luna Moth" and "UNC3753" were moved from campaign:fbi-flash-csa-260526-... to actor:silent-ransom-group (alias SRG kept), and the campaign key was removed from the Luna Moth entry's entities (no cited source ties the new activity to the FBI USB campaign).
19. F11 N-able dropped country fact: restored in the main analysis ("in North America, South Africa and Europe but not Switzerland", Huntback).

Scope of this pass: claims.changed.iter2.yaml (22 new or changed claims), every other claim of the entries remediated, and a random quarter of the rest, per the claim ledger work/2026-11-14T0255Z-intel/claims.iter2.yaml (193 claims). Write work/2026-11-14T0255Z-intel/verification.iter2.claims.yaml for those in scope.
