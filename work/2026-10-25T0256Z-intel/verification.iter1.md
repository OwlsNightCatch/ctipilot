**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-25T03:47:20Z · ended_at=2026-10-25T04:08:41Z · duration_seconds=1281

## Verification report — 2026-10-25T0256Z-intel (iteration 1)

Scope: 2 new entries (NTLM relay signing bypass; ZDI Linux kernel reports), 4 updated entries (eMudhra, Danfoss/Copeland, PK Softech/Publica, PHP2Shell), the run record. Full ledger walked: 226 of 226 claims have a verdict row in `verification.iter1.claims.yaml` (221 ok, 4 F3, 1 F4; the other findings are not ledger claims: evidence quote, run-record count, editorial). Cited pages were fetched live this pass (extract, raw url, pdf, ncsc-csh, cisa-kev bridge); the gate's cached bodies were used for older Swiss news and PHP vendor pages and cross-checked on load-bearing facts. The php.net archive anchors were read from the raw HTML.

Walked and found sound (not findings): both new entries' technical content against Sysdig, TuxCare, The Hacker News, Phoronix, SpecterOps and Blackfield; all Public Sénat, Le Monde Informatique and Forescout figures in the Danfoss update; the EDÖB release and Der Bund article behind the Publica update (dates, wording, "names neither the actor nor the number of insured persons"); the Tenable, Siemens and ReliaQuest facts in the PHP update; CISA KEV re-read live (catalogue 2026.10.23, neither PHP CVE listed); the Oracle second alert, OpenJDK 2026-10-24 advisory, openjdk.org/emudhra, PSF announcement, ENISA record and Cisco advisory in the eMudhra update; all `updated_at` mirrors equal the record `at`; `fields` lists cover every changed line in `git diff HEAD`; no em dash, IOC or workflow vocabulary in reader-facing text; classification blocks present and consistent with source tiers.

### Citation does not support the claim
- **#1 (F3)** `2026-10-21/emudhra-...` Exposure: "shows Node.js, Bun and FreeBSD as fixed and the Composer ca-bundle, Erlang certifi, Bottlerocket and Godot as still pending". Live tracker (https://emudhra.we-have-a-problem.com/) lists Composer ca-bundle `1.4.16, 1.6.0` and Erlang certifi `2.18.0` as patched; Bottlerocket, Godot and LibreOffice are the pending rows. The Java row now shows links without versions, so "lists fixed versions for Java" is stale too. The run rewrote this entry and left the stale state.
- **#2 (F3)** same entry, body: "Standalone Java runtimes keep their own trust store ([OpenJDK, 2026-10-21])". The page now reads: "Advice to users: Please see openjdk.org/emudhra." No statement on standalone runtimes. Re-point to https://openjdk.org/emudhra.
- **#3 (F3, low confidence)** `2026-10-13/danfoss-...` body: "BleepingComputer reports no tie". BleepingComputer: "While no information is available on how the Danfoss refrigeration controllers were compromised, ..." then lists the 2025 CVEs as context. It does not say there is no tie. Pre-existing text.
- **#4 (F3, low confidence)** same entry, Update 2026-10-25: "ANSSI says it cannot impose connection rules on retailers". Le Monde Informatique: "L'audition a aussi mis en lumière les limites du cadre actuel. L'Anssi peut alerter et conseiller, mais elle ne dispose d'aucun moyen d'imposer ..." is the outlet's gloss; Public Sénat has no such statement. Attribute it to the outlet.

### Unsupported / hallucinated facts
- **#5 (F4)** `2026-10-25/ntlm-relay-...` summary: "Microsoft fixed the SMB variant in September 2026 and the LDAP variant in the 2026-10-13 cumulative update, and Blackfield found no CVE or KB note for either" (title: "fixed it without a CVE"). Blackfield, about the SMB change only: "I could not find a CVE for this specific change, in Microsoft's update guide, the KB notes, or public trackers; it reads as silent hardening rather than a tracked fix." Its only LDAP mention is a pointer to SpecterOps, which does not address a CVE; the KB5126646 page lists no LDAP signing item. Limit the claim to the SMB change.
- **#6 (F4)** `2026-10-21/emudhra-...` evidence[5]: "If you use a standalone OpenJDK Java runtime, we recommend that you update it as soon as possible, since it likely contains the compromised certificates." (source_url .../advisories/2026-10-21). Not on that page now (live extract, raw HTML, and the gate's cached body all show only the version list, the risk matrix and the pointer to openjdk.org/emudhra), nor on openjdk.org/emudhra. Not a verbatim substring of its source.
- **#7 (F4, low confidence, run record)** "the PK Softech and Publica entry now carries twelve changelog sections": twelve `updates[]` records, eleven `##` sections (the 2026-10-18T1307Z-audit correction is internal).

### Needs more research
- **#8 (F8)** eMudhra actions[1] and the Cisco paragraph present five items as the advisory's impacted list; Cisco advisory v1.1 also lists Duo Agentic Authorization Connector 1.0.1, Meraki MV Smart Camera Firmware (Nov 18, 2026) and Ultra Cloud Core SMI 2026.04.1 (Nov 2026) under software fixes, and a long under-investigation list (Secure Client, Webex, ISE, ASA/FTD, Catalyst).
- **#9 (F8, low confidence)** eMudhra, Python: status `patch-available` and "a Python release that carries the ssl denylist" imply an installable release. The tracker lists Python 3.15.1, 3.14.9, 3.13.17 (blog.python.org: these bundle pip 26.2.2 with certifi 2026.10.19) and the Python Discourse thread says pip below 26.2.2 keeps trusting the intermediates whatever the system store holds. CPython issue 160040 (the denylist) still carries `release-blocker`, "In Progress", and a request for security releases "ASAP". The entry omits pip 26.2.2 and shows no release carrying the denylist.
- **#10 (F8, low confidence)** eMudhra: the run's own bodies (`bodies/emudhra-pr.txt`, `bodies/thn-emudhra.txt`) carry eMudhra's 2026-10-22 decision to exit global SSL/TLS, about 30,800 unexpired certificates under the G3 root (99.9 percent via InCommon) and Chrome's point that standard ACME clients do not replace certificates outside their renewal window without ARI. This bears directly on the "replace before 2026-10-27" action and is not in the entry.
- **#11 (F8, low confidence)** NTLM: "(KB5126646 and KB5122882 are the Windows Server 2025 and 2022 packages)" pairs the October package for 2025 with the September package for 2022; a Server 2022 DC owner cannot tell that KB5122882 is not the LDAP fix for 2022, and no October 2022 or September 2025 number is given. `affected_products` names only Windows Server while Blackfield says workstations got the SMB change too.

### Action-item discipline
- **#12 (F18, low confidence)** ZDI actions[0] restates the Defender takeaway as a three-part hardening list and ends with "install the distribution kernel ... on the day it ships" (no fixed kernel exists). Keep the inventory plus sysctl stop-gap as the task.
- **#13 (F18, low confidence)** eMudhra actions[0] (about 170 words) bundles ten toolchains, two stop-gaps, an image rebuild, a verification step and a deadline; split or shorten.

### Editorial / less-is-more flags (advisory)
- **#14 (F11)** Summaries: Danfoss 1,407 chars (5 sentences), Publica 1,491, PHP 1,290, eMudhra 886 against a 1 to 3 sentence contract; Publica Defender takeaway is one ~300-word sentence and the entry has 12 records (consolidation already suggested by the previous fire). ZDI body: missing space in "bypassed)([Sysdig".

### Missed angles
None above the critical/high bar found. Checked: KEV (no addition in window), the run's dropped items (the CrowdStrike agentic-campaigns post is dated 2026-10-23, before the window start of 2026-10-24T00:56Z, so the drop reason holds), the S2 Swiss PHP2Shell measurement and the ConnectWise status update (both change no decision on entries that already say update/keep disabled). Coverage looks complete for critical/high signal; the eMudhra exit/ACME point above is the only candidate delta.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 6, advisory: 1)

Priority for remediation: #5, #6, #1, #2 (all evidenced against live pages); #3, #4, #7 are low confidence.

### Findings summary (machine-readable)
See `work/2026-10-25T0256Z-intel/verification.iter1.findings.yaml`.
