# Iteration 2 findings and remediation applied (verify each before the cold pass)

- F4 kernel cves[] / F3 Ubuntu scope (2026-10-31/cve-2026-98432-...): cves[].affected and .fixed now give the Ubuntu fixed builds per release (26.10 7.3.0-10.10, 26.04 7.0.0-43.43, 24.04 6.8.0-149.149, 22.04 5.15.0-203.213; 20.04/18.04/16.04 in progress as of 2026-11-10) and say the HWE, cloud, FIPS and Raspberry Pi kernels were still in progress; headline, title, summary, actions[0], Defender takeaway and the 2026-11-11 section now say "generic kernels"; the record declares `cves`.
- F4 eMudhra sourcing_note (2026-10-21/emudhra-...): Cisco version 1.9 and Microsoft's 2026-11-16 removal of the remaining roots now stated; record declares `sourcing_note`; record summary now states all four deltas (SonicWall, Apple builds, Microsoft 2026-11-16, Cisco 1.9).
- F3 SAP: the uncited "low-privileged account or a user's click" clause removed from the 2026-11-11 section (the Patch Day page carries no descriptions).
- F3 Barracuda: 9.4.0.029 now cited to Barracuda Campus.
- F3 Patch Tuesday iSCSI: CVE-2026-88234's own MSRC record added to sources[] and cited; DNS, DHCP and iSCSI rows now say "reachable by an in-network attacker calling arbitrary endpoints" (Microsoft FAQ) in body, Defender takeaway and sourcing_note; the sourcing_note's list of uncovered rows is no longer exhaustive and no longer labels cloud rows authenticated.
- F4 Vates: "ld.so.preload entry left by the actor" replaced with generic wording ("the dynamic-linker preload file"); the actions[1] artefact list made generic (an unexpected VM, cron files written by the actor, a changed dynamic-linker preload file).
- F4 run record: the Patch Tuesday borderline-drop line now states the real reason for each dropped group.
- F11 GhostFrame, CopperDragon: Detection and actions now describe the behaviour (a process masquerading as the host daemon, an unexpected executable under /opt, a Run key with an update-themed name); the malware's own file and process names stay only in the mechanism description and the Triage discriminator.
- F11 Ivanti: "no transport could read" now "could not be read".
- Declined (advisory only): N-able sources[] records for the five further ENISA records (the scores are correct; adding sources[] records would need inline citations in a section that does not otherwise cite them).
