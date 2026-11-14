# Prior-iteration deltas (iteration 2 NEEDS_FIXES: truth 3, editorial 0, advisory 2) and remediation applied

1. F3 ScreenConnect Detection, last clause: the Sophos link was removed from "a client service named like a Windows component" (Huntress only) and moved to the "(the Sophos pattern)" clause for the curl/PowerShell download followed by silent msiexec install. verify both clauses against their pages.
2. F3 Quay para 3 CSAF sentence: reworded to "its CSAF record for the first flaw links eight Quay errata, RHSA-2026:99019 and 99021 to 99027, as its fixes and lists Red Hat Quay 5 and the mirror registry for Red Hat OpenShift 2 as affected with no fix available", cited to the CVE-2026-123710 CSAF file only; the builds 3.9.28 to 3.18.3 stay cited to the CVE-2026-110697 page.
3. F3 Danfoss cite dates: the advisories page and the AK-SM 800A readme are now cited as "[Danfoss, read 2026-11-14]" inline (main analysis and Update section), with the sources[] dates left at the read date and the publisher labels marked "as read".
4. F11 advisory, unlinked product:amazon-ec2: added to the CyberStrikeAI entry's entities.
5. F11 advisory, accreted N-able and ScreenConnect titles and summaries, and Danfoss actions[1] length: not changed (advisory; all statements true).

Scope: claims.changed.iter3.yaml (3 new or changed claims), every other claim of the entries remediated, and a random quarter of the rest, per work/2026-11-14T0255Z-intel/claims.iter3.yaml (194 claims). Write work/2026-11-14T0255Z-intel/verification.iter3.claims.yaml.
