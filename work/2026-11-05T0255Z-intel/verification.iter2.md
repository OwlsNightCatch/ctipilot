**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-05T05:04:44Z · ended_at=2026-11-05T05:33:34Z · duration_seconds=1730

## Verification report — 2026-11-05T0255Z-intel (iteration 2)

Scope: post-fix pass after iteration 1's NEEDS_FIXES. All 252 ledger claims answered in `verification.iter2.claims.yaml` (`claim_ledger.py --coverage 2`: 252/252, 0 missing): the 23 changed claims, every claim of the seven remediated entries (Node2Shell, kernel, Zyxel, APT29, Danfoss, Xerox, SEPPmail) and, because I had read their primaries anyway, all claims of the four untouched new entries (Vaud, iSCSI, Sophos, SonicWall). Five claim rows are non-ok, each also a finding below. Sources read in this iteration, live: ELLIO, Node.js advisory, Splunk SVD-2026-1015, Citrix CTX697300 and CTX697256, Cisco, Palo Alto, Tenable, OpenSourceMalware, Envoy, .NET blog and dotnet/announcements, AWS bulletin (11/04 15:25 PST), Debian tracker, CIQ, Ubuntu tracker, XCP-ng, Vates, WatchGuard, Fortinet (raw HTML for "Known Exploited: No"), MikroTik 7.25.1 and 7.24.6, openwall, Go team post, Akamai (raw HTML for both posts), NCSC.ch 13054, 13105, 13120, NCSC-NL, KEV catalog 2026.11.04, FIRST EPSS, EUVD API (CVE-2026-107441 and the five SEPPmail records), Xerox bulletin v4 and v5 (pdf), Dixell guide (pdf), Sekoia (raw HTML), Binarly blog and advisory (page payload), SentinelLABS (WebFetch, Vercel checkpoint on every other transport), Sophos RCA and blog, cached bodies for the rest. Gate state taken as given (60 pass).

### Prior-iteration deltas (walked first)
1. Node2Shell fixed versions: ELLIO page carries "Node.js 22.23.4, 24.22.1, 26.12.1" and "end-of-life 20.x, 23.x and 25.x lines ... will not get a fix"; supported. Held.
2. Kernel fixed-kernel statement: Debian tracker (bookworm 6.1.190-1, trixie 6.12.115-2 fixed), CIQ patched-kernels table, AWS ("Amazon Linux 2 and Amazon Linux 2023 kernel packages ... are available") each support their clause. Held.
3. Kernel AWS evidence record removed; no evidence[] orphan and no main-analysis sentence relies on it. The older Update 2026-11-03 section still states the old AWS wording as AWS's: contradicted by the current page (finding #1).
4. Zyxel Detection: GreyNoise shows `cp /tmp/info /home/web/tmp/info.txt` staging and describes no implant; no unsupported "no persistent artifact" any more. Held (wording nit, F11 #12).
5. APT29 Detection: Sekoia names VDGH_TOKEN_REF as a replay-guard marker cookie and says "Several indicators, including delivery hosts, exfiltration hosts, YARA rules ... are not shared"; Detection and sourcing_note now agree. Held.
6. Node2Shell Splunk and Citrix dates: Splunk Published 2026-10-28, Last Updated 2026-11-04; Citrix "2026-10-30 Initial Publication | 2026-11-03 Updated 'Remediation Action' ..."; labels and section text now match. Held.
7. SEPPmail admin-guide citation: "retrieved 2026-11-05", source record "undated"; the page has no dateline. Held.
8. XCP-ng date: removed from summary and record; body and Update keep Vates 2026-11-03 published / 2026-11-04 updated and the XCP-ng post of 2026-11-04, all as the pages state. Held.
9. Node2Shell F8: version-reading caveat (ELLIO), Cisco and Palo Alto statements (both pages), Splunk and Citrix wording restored and accurate; analysis 539 words. Held.
10. Kernel Exposure: sysctl check (CIQ), Go 1.24 default (Go team), request-socket migration (Akamai) restored; the `ss -M` command is still absent and is now evidenced (finding #7); "every Go program" overstates the Go post (finding #2).
11. CVE-2024-27834: iOS 17.5 page (Apple 120905) added and cited; affected/fixed now only name builds on cited pages; MikroTik 7.26beta5 gone. Held.
12. Vaud notable to high: a cantonal authority warns of an active campaign in the home region with several organisations affected, the decision (audit, then block device code flow in report-only first) fits seven days, and no `high` disqualifier applies. Judged correct.
13. Zyxel credibility 1 to 2 with `classification` in `fields`: the central new claim rests on Binarly alone (BleepingComputer relays it, Zyxel only credits Binarly). Judged correct.
14. Danfoss actions[0]: only the unsourced clause was dropped; still a bundle (finding #8, low confidence).
15. SEPPmail run-record label now `single-source`, as the entry. Held.
16. Sophos/APT29 sourcing notes: transport wording gone. Held.
17. Xerox retyped `update`: `updated_at` = record `at` = section `at` (2026-11-05T03:51:20Z); content is a genuine post-publication vendor revision (v5 of 2026-11-03 adds the mitigation section). Entry-side correct; the run-record note was not updated (finding #6).
18. Zyxel and iSCSI headlines reworded as stated. Held.
19. Product keys linked: SonicWall, iSCSI, APT29 (Plerdy, Adreno), kernel (Citrix x3, XCP-ng, XOA, WatchGuard AP), Node2Shell (Splunk x5, Citrix Scout) all present in `entities` and in the registry. Held.
20. Sophos tag: `supply-chain` gone. Held.

### Citation does not support the claim
- **#1 (F3, low confidence)** `cve-2026-98432-...`, section Update 2026-11-03: "AWS says ... that Network Load Balancer TCP listeners pass client packets, including IP options, to targets, and that Linux targets behind them, Global Accelerator, PrivateLink and VPC Lattice layer 4 need the kernel update ([AWS, 2026-11-02])". The AWS page now (Last Updated 11/04/2026 15:25 PM PST) has no NLB TCP-listener paragraph and says "Global Accelerator does not support IP options on IPv4 TCP packets ... all endpoints behind Global Accelerator are not affected by this issue"; PrivateLink and VPC Lattice still hold. The 11/02 version (saved in `work/2026-11-03T0256Z-intel/bodies/k-aws.md`) did say it. True of the version it dates, contradicted by the page it links; this run removed the matching evidence record for that reason. Date the clause to the 2026-11-02 version and state the 2026-11-04 revision.
- **#3 (F3, low confidence)** kernel, Update 2026-11-05: "Both say a public exploit exists that relies on MPTCP, which the XCP-ng 8.3 kernel does not have ... other ways to exploit it cannot be ruled out ([XCP-ng, 2026-11-04])". Vates says "It leverages an MPTCP listener ... the exploit does not affect XCP-ng"; the "kernel doesn't have MPTCP" and "can't be ruled out" wording is XCP-ng's alone.
- **#4 (F3, low confidence)** Zyxel, Update 2026-11-05: "fixed on 2026-10-22 ... ([Zyxel PSIRT, 2026-11-03])". The Zyxel advisory's only date is "2026-11-3: Initial release"; 2026-10-22 is on Binarly ("On Oct. 22, 2026 ... they released new firmware") and BleepingComputer ("security updates on October 22"). The body paragraph cites both; the section does not.
- **#5 (F3, low confidence)** Zyxel body paragraph 2 and the Update: "Binarly, which recovered the Python exploit GreyNoise described from Red Heron infrastructure ([Binarly])". Binarly's prose never says Red Heron (only the Acronis link slug does); it says the exploit sat in an open directory on the JITTERLY/SIXZUT C&C server. BleepingComputer states it ("While investigating Red Heron infrastructure linked to the JITTERLY backdoor and SIXZUT rootkit, Binarly researchers found an exposed archive ..."), cited later in the paragraph, not on the clause.

### Quantifier without source
- **#2 (F14, low confidence)** kernel Exposure: "which every Go program listening on Linux has been since Go 1.24". Go team: "As of Go 1.24, Go programs enable MPTCP by default for listen sockets on Linux. This default may be changed by setting the \"multipathtcp\" GODEBUG ...; Programs may also explicitly enable or disable MPTCP on a per-socket basis". Say "by default" and name the overrides.

### Unsupported / hallucinated facts
- **#6 (F4)** run record, notes: "leaving 5 updates: ... and the Xerox PHP2Shell entry (improvement, no float)." The Xerox record is now `type: update` and floats (`updated_at: 2026-11-05T03:51:20Z`). Same paragraph's counts lag the remediation: "Node2Shell (549 to 549)" is 539 now, "the Zyxel analysis ... (574 words)" is 586 by the same count.

### Surface contradiction
- **#9 (F9, low confidence)** Danfoss, Update 2026-11-05: "[Coolworld's statement] does not say that attackers exploited that component". BleepingComputer (cited in the same section) says "Coolworld says the attackers exploited a vulnerability in a third-party component"; Coolworld's text is only "relates to a component from a third-party supplier and was outside Coolworld's direct control". The entry follows the primary without telling the reader a cited outlet reads it the other way; add a `Contradiction:` line.

### Needs more research
- **#7 (F8, low confidence)** kernel Exposure lacks the direct listener check the Akamai page gives: "To determine whether any applications are listening on MPTCP sockets, run: sudo ss -M -l -n -p -e", plus `sysctl net.mptcp.enabled` and `sysctl net.ipv4.tcp_migrate_req` to read both settings (CIQ: `ss -Mltn` works on RLC Pro LTS 9.6 and RLC Pro 10, not LTS 8.10). Iteration 1's remediation skipped it because the passage had not been read; it is on the raw page.

### Strengthen primary source / missing citation
- **#11 (F5, low confidence)** kernel `cves[].fixed`: "MikroTik RouterOS 7.25.1 (stable) and 7.24.6 (long-term)". The cited changelogs carry no channel; the labels come from the NEWEST7 channel listing the run read, which is in no `sources[]` record.

### Action-item discipline
- **#8 (F18, low confidence)** Danfoss actions[0] is still one ~150-word sentence bundling inventory, take-off-internet, VPN restore, stop-gap and insurance caveats, EOL replacement and an independent temperature check, largely restating the body's CERT-FR and CSIRT Italia paragraphs. Keep the first task; move or drop the rest.

### Classification missing / inconsistent
- **#10 (F17, low confidence)** Sophos entry rated reliability A; its cited sources are sophos.com pages (blog = `sophos-xops`, tier B; the RCA page has no source record, metadata date 2025-11-25, CMS publish time 2026-11-04). A victim's own account is arguably A for its own estate, but the profile rule flags A outside the A tier: use B or justify in a clause.

### Editorial / less-is-more flags (advisory)
- **#12 (F11)** Zyxel: "GreyNoise describes ... and no implant" is literally true (the section names none) but reads as an asserted absence; the takeaway's "the flaw Binarly shows is exploited" over-asserts against the entry's own "Binarly alone calls it the exploited zero-day" and BleepingComputer's "unclear".
- **#13 (F11)** Xerox: "the bulletin reports no attack on these devices" and sourcing_note "reports no exploitation of Xerox devices" read as a vendor negative assurance; the bulletin says nothing on exploitation either way (HEAD's "gives no statement" was exact).

### Missed angles
None evidenced. KEV catalog 2026.11.04 holds one addition in the window (CVE-2024-27834, covered); two further searches (exploited vulnerabilities of 2026-11-04; Swiss municipal and cantonal incidents, November 2026) surfaced nothing new (the Chrome V8 CVE-2026-11645 the search returned is already a 2026-06-10 entry). No duplicate of an existing entry among the six new ones (prior-coverage and cves_seen checked; references declared where entries are related). Coverage looks complete.

### Verdict
NEEDS_FIXES (truth: 6, editorial: 5, advisory: 2)

No finding is high severity: all six truth findings are adjacency or wording defects with the facts true on some page (#1 is a stale-version issue, #2 an overstated universal, #3 to #5 citations that sit one sentence away from the page that carries the fact, #6 a stale note in the run record). Fix #1, #3 to #6 first; they are one-line edits.

### Findings summary (machine-readable)
See `work/2026-11-05T0255Z-intel/verification.iter2.findings.yaml` (13 records).
