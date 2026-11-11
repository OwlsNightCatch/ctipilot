**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-11T04:50:14Z · ended_at=2026-11-11T05:07:59Z · duration_seconds=1065

## Verification report — 2026-11-11T0256Z-intel (iteration 2)

Scope: post-fix pass. Ledger `claims.iter2.yaml` (451 claims) walked in full (all 63 changed claims, every other claim of the remediated entries, and the unremediated Chrome entry); every claim has a row in `verification.iter2.claims.yaml` (444 ok, 6 F3, 1 F4). Sources re-fetched this iteration: Apple support page (revised 2026-11-10), MSRC eMudhra post (update 2026-11-10), Cisco eMudhra advisory (v1.9), SonicWall SNWLID-2026-0021 page and API, Ubuntu tracker (updated 10 Nov), Veeam KB4966, BleepingComputer Patch Tuesday and Outlook text, MSRC SUG API for every Patch Tuesday CVE plus the full November CVRF (KBs, scores, exploited flags), Fortinet PSIRT pages (raw HTML for CVE ids and CVSS vectors) and the 50-item RSS feed, Adobe APSB26-191 (raw HTML), Onapsis/SAP/NCSC 13167, ENISA CNA records (Ivanti, N-able x7, SAP x5), Vates/BC, Atlassian/BSI CSAF, Synology SA-26:19 and SA-26:18, ESET white paper PDF, Check Point and Positive Technologies posts, Recorded Future, Wiz/Sentra/BC, watson.ch, PK Softech and BACS pages, NCSC Hub posts 13054/13092/13144/13165/13167, CISA alert and KEV feed.

### Prior-iteration deltas (each fix checked against its source)

- Outlook NTLM (F4): fixed. BleepingComputer: "exposing the user's NTLMv2 authentication hash"; MSRC FAQ also says "discloses a user's NTLMv2 hash". Claim is cited to BleepingComputer. OK.
- eMudhra Apple/Microsoft/Cisco (F3+F8): fixed in main analysis, Exposure, takeaway, actions, headline and summary. Apple page: macOS 27.2.1, 26.7.3, 15.8.3, three further roots and two parent roots leave /etc/ssl/cert.pem; Microsoft update of 2026-11-10 (10 roots from Windows, Edge/WebView2 G1/C1/ECC/Root TLS G1, Azure Linux, .NET images, MS OpenJDK); Cisco history 1.9 2026-NOV-10; block date 2026-10-22 on tracker and BleepingComputer. Residual defects: stale sourcing_note ("version 1.8"), record summary covers SonicWall only (see findings).
- Kernel/Ubuntu (F3): fixed in body/section (tracker 22.04/24.04/26.04/26.10 `linux` fixed; 20.04/18.04/16.04 in progress; CIQ 9.8 vs 8.1 restored). New defects: unscoped "22.04 to 26.10" in headline/summary/actions and a stale cves[] row (findings).
- Turla (F3): fixed; ESET PDF: "We were unable to determine the initial access method ... it is possible that they were breached by exploiting a vulnerability." OK.
- Patch Tuesday count (F14): scope now "seven ... in domain infrastructure and server roles". CVRF confirms exactly seven such 9.8 rows (Kerberos, Windows Search/Exchange, DNS, DHCP, LDAP, iSCSI, SQL) and further 9.8 rows (DirectMusic x2, Media Foundation, Color Management x2, Xbox Live). Residuals in findings.
- SAP title "three of the four": Onapsis page says it found and reported ICM2SHELL (two CVEs) and ProxyGate (one). OK.
- Qubole, CopperDragon, GhostFrame, Confluence, Synology, Vates, Adobe, Danfoss, N-able, Fortinet, Publica, Ivanti, Barracuda fixes: each re-read against the source; all correct (Fortinet FG-IR-26-265 raw page: CVE-2026-126251, 9.1, AV:N/PR:N; OSPF row AV:A confirmed in raw page; the feed holds no further unauthenticated row >= 9.0; Danfoss section matches the BACS page and Hub advisory; Publica wording matches watson.ch and PK Softech).
- F10 Cisco follow-up (`findings.F10.yaml`): accepted; the PSIRT revisions are covered by existing entries and the Meraki advisory is old. Coverage looks complete otherwise (Zyxel GS1900 and Ivanti Connect Secure zero-days from the BleepingComputer roundup are already in the store).
- Declined items: F16 Vates/SAP priority and F7 drops of Confluence/Adobe/Patch Tuesday: stand as defensible judgment calls, not re-raised. F18 action lists: stand (not a defect). F11 trimmed analysis: stands (declared through `body`). F11 attacker-chosen names: does not stand cleanly, re-raised as advisory only (rule 12 names file-name indicators).

### Citation does not support the claim
- #1 (F3) `2026-10-31/cve-2026-98432-...`: headline "Ubuntu 22.04 to 26.10 kernels out", summary "Ubuntu has fixed 22.04 to 26.10", actions[0] "Ubuntu 22.04 to 26.10 ... updates are out". Ubuntu tracker (updated 10 November 2026): `linux` fixed on those releases, but linux-hwe-6.8 (22.04), linux-hwe-7.0 (24.04), linux-azure-7.0/-fde/-nvidia (24.04), linux-fips (22.04, 24.04), linux-raspi/linux-nvidia (26.04) read "Vulnerable work in progress". Scope the statement to the generic kernel and say HWE/cloud/FIPS kernels are pending.
- #2 (F3, low confidence) `2026-11-10/sap-...`: "each needs a low-privileged account or a user's click, according to the notes' descriptions" cited to the SAP Patch Day page, which carries only title/product/priority/CVSS; descriptions are in the CNA records (EUVD-2026-120657 "An attacker with low privileges", -120680, -120686, -120682, -120665).
- #3 (F3, low confidence) `2026-11-04/cve-2026-116606-barracuda-...`: "update every Email Security Gateway to 9.4.0.029 or later ... ([Barracuda, 2026-11-05](trust.barracuda.com/...))": the Trust Center page does not name 9.4.0.029 (Campus does).
- #4 (F3) `2026-11-11/microsoft-november-2026-...`: "a release of an invalid pointer in Windows iSCSI (CVE-2026-88234), each described only as code execution over a network ([Microsoft](.../CVE-2026-88218))": CVE-2026-88234 is not on the cited DNS record and its own record is not in sources[] (it exists in the MSRC API: 9.8, AV:N/PR:N/UI:N).

### Unsupported / hallucinated facts
- #5 (F4) `2026-10-31/cve-2026-98432-...` cves[]: `affected` "(fix in progress as of 2026-11-07)" and `fixed` "other Ubuntu releases in progress as of 2026-11-07" were not updated (record `fields` omits `cves`), contradicting the newest section and summary (22.04/24.04/26.04 fixed per the 2026-11-10 tracker).
- #6 (F4) `2026-10-21/emudhra-...` sourcing_note: "Cisco's advisory is at version 1.8." Cisco history table: 1.9 2026-NOV-10; the entry's own summary and actions[2] say 1.9.
- #7 (F4, low confidence) `2026-11-11/microsoft-november-2026-...` sourcing_note: "Authenticated rows ... (SharePoint, Azure DevOps Server, developer tools, the cloud services) and further 9.8 rows in DirectMusic, Media Foundation and Xbox Live Networking Service". Omits Color Management CVE-2026-96078 (9.8; FAQ "An unauthenticated attacker ... crafted packet to an affected service over the network") and -96067; the cloud rows Entra Device Registration CVE-2026-109469 (10.0), Azure OpenAI CVE-2026-119990 (9.8), Azure Managed Grafana CVE-2026-114160 (9.8) are PR:N, and VS Code CVE-2026-120779 is PR:N/UI:R.
- #8 (F4, low confidence) `2026-11-11/vates-...` Detection: "an ld.so.preload entry left by the actor": VSA-2026-062 only lists `ls -la /etc/ld.so.preload /.ustar* ...` as a check.
- #9 (F4) run record notes: "Media Foundation and Color Management parsers, Xbox, the cloud-service records ...; each authenticated, user-driven or cloud-side": CVE-2026-96078 (Color Management), CVE-2026-96157 (Media Foundation) and CVE-2026-112967 (Xbox Live) are 9.8 PR:N/UI:N rows (FAQ: unauthenticated crafted packet to a service / in-network attacker calling arbitrary endpoints).

### Needs more research
- #10 (F8, low confidence) Patch Tuesday entry: DNS/DHCP/iSCSI MSRC FAQs say "remote code execution via an in-network attacker calling arbitrary endpoints" (the only stated prerequisite); the entry says "described only as code execution over a network" and "with no mechanism". Add the in-network prerequisite to Exposure.

### Editorial / less-is-more flags (advisory)
- #11 (F11) eMudhra record 2026-11-11T03:55:02Z: summary covers SonicWall only; the section also carries Apple, Microsoft and Cisco 1.9 (4c(d) "no more, no less"). Amend the record summary.
- #12 (F11) File/process/VM/registry-name indicators in Vates (pivot2, zz-ustar, ld.so.preload), GhostFrame (/opt/vmhostd-core, vmhostd, local.sh) and CopperDragon (WindowsUpdateAssist) against rule 12 ("mutex or file-name indicators").
- #13 (F11) N-able: CVSS for five CVEs rests on ENISA records EUVD-2026-122958, -122963, -122959, -122956, -122964 that are not in sources[] (values verified correct).
- #14 (F11) Ivanti sourcing_note "no transport could read": pipeline vocabulary; say "could not be read".

### Verdict

NEEDS_FIXES (truth: 9, editorial: 1, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-11-11T0256Z-intel/verification.iter2.findings.yaml`.
