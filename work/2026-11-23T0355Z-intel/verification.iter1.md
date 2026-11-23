**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-23T04:42:27Z · ended_at=2026-11-23T04:55:21Z · duration_seconds=774

## Verification report — 2026-11-23T0355Z-intel (iteration 1)

Scope: 3 new entries, 1 updated entry (nginx2root, improvement record 2026-11-23T04:35:59Z), run record, registry tail. All 82 ledger claims walked (82/82 rows in verification.iter1.claims.yaml; `claim_ledger.py --coverage 1`: 82/82, 0 missing). Pages read this iteration: GL.iNet notice (extract and raw HTML), BleepingComputer, RemoteToHome, pwn.ai, The Hacker News, VulnCheck, CVE JSON record (VulnCheck is the CNA, CVSS 4.0 8.5), Debian tracker, Ubuntu USN-8949-1 and CVE page, Securelist parts 1 and 2, Sophos, nginx.org, Fortinet FG-IR-26-279, CERT-EU, Rapid7 and its PoC repo, Wiz, CERT.at, NCSC-NL, NCSC.ch hub post 13203, Xint, PAN-OS and Cisco advisories (no newer revision than the entry states).

Prior-iteration deltas: none (iteration 1). Dedup: no overlap of the three new entries with the prior-coverage index, the entries store or cves_seen before this run; the five added nginx CVE ids were absent from the store (state/cves_seen.json diff matches). Registry additions match the run record (6 entities, 11 products; relations as listed). Run-record counts (66/66 slice records, 3 published, 1 updated, duration 2685 s, kaspersky-securelist and pwn-ai fetch dates, 2026-11-22 disposition of ShadowCloud) hold on disk.

### Citation does not support the claim

- **#1 (F3) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — GL.iNet GoodCloud: an exploited cloud remote-management flaw ...
  - Quote: GL.iNet says it identified on 2026-11-20 a vulnerability in its GoodCloud cloud remote-management service ... ([GL.iNet, 2026-11-20](https://www.gl-inet.com/en-us/blogs/blog/glinet-security-notice-2026-11-20)); summary: "GL.iNet says an unauthorized party exploited a vulnerability in its GoodCloud remote-management service"
  - The GL.iNet notice says 'a vulnerability in its cloud remote management services' and never names GoodCloud (raw HTML: only an image filename enterprise_goodcloud.jpg). BleepingComputer ('Its GoodCloud platform allows customers to remotely manage...') and RemoteToHome name GoodCloud, and RemoteToHome says GL.iNet has not confirmed the GoodCloud client as the entry point. Body clause 1 and the summary attribute the GoodCloud name to GL.iNet's own statement; say 'cloud remote management services' for the vendor and attribute GoodCloud to BleepingComputer/RemoteToHome. Claim ids 9f58090f7d, f4ce2f4492.
- **#2 (F3) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2** — Defender takeaway
  - Quote: because both backdoors hide their command channel in that traffic and Kaspersky found the entry point unknown ([Kaspersky, 2026-11-17](https://securelist.com/operation-shadowcloud-graphdoor/122005/))
  - Part 2 (graphdoor/122005) carries no statement that the entry point is unknown (grep: only 'the initial infection chain' in its introduction). The statement 'The exact entry point that let the attackers install the agent is unknown' is in part 1 (gitdoor/122004). Cite part 1 for that clause (or both parts). Claim id d460003e0d.

### Unsupported / hallucinated facts

- **#3 (F4) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2** — 'signed' program/binary
  - Quote: summary: 'sideload a loader DLL into a legitimate signed program'; body: 'drop a legitimate signed binary'; Detection: 'a signed legitimate program (... a CEF helper)'; Triage: 'drops a signed binary'
  - Kaspersky part 1 says 'A legitimate binary used for DLL sideloading' and Sophos says 'legitimate Sandboxie executables'; neither source says the binaries are signed (grep 'signed' finds nothing relevant). Remove 'signed' in all four places. Also (low confidence) the Detection clause lists 'a CEF helper' and cites only Kaspersky, who names libcef.dll only as a loader; the Jcef_helper.exe host appears only in Sophos's table. Claim ids 57c02d7d6a, 2b62e961cb, e9cac55f88, ee0d85bdc7.
- **#4 (F4) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2** — summary: 'an intrusion set active since early 2026'
  - Quote: Kaspersky part 1: 'In early 2026, we identified a new, active intrusion campaign'; 'the threat actor has been preparing the infrastructure of this operation since at least the end of 2024'; Sophos: 'incidents between August 2025 and August 2026'
  - The sources say the campaign was identified in early 2026, not that it has been active since then; Kaspersky dates infrastructure preparation to late 2024 and Sophos (a fragment) lists victims from August 2025. The body correctly says 'identified in early 2026'; the summary contradicts it. Change to 'identified in early 2026'. Claim id ee0d85bdc7.
- **#5 (F4) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2** — title: '... entering through an abused MeshCentral agent and DLL sideloading'
  - Quote: Kaspersky part 1: 'The exact entry point that let the attackers install the agent is unknown, but evidence points to the reuse of a prior infection already present on the network.'
  - (low confidence) 'entering through' reads as the initial-access vector, which Kaspersky says is unknown; the MeshCentral agent is the post-access delivery channel for the backdoors. Use 'delivered through' / 'planted via' (the headline already says 'planted via').
- **#6 (F4) nginx-nginx2root-five-unauth-memory-corruption-flaws** — cves[] CVE-2026-118899, -120967, -125283, -123640, -120993 (improvement 2026-11-23T04:35:59Z)
  - Quote: vector: zero-click / auth: pre-auth on all five; type: logic-flaw for CVE-2026-123640
  - (low confidence) nginx.org lists only a title, severity and vulnerable range for each, and Fortinet only a severity and range; neither states attack vector, authentication requirement or flaw class. Zero-click/pre-auth is asserted without a source for flaws that are configuration- or position-dependent (alias+try_files overflow, PROXY protocol v2 NULL dereference from a trusted proxy, ssl_preread validation). Either drop vector/auth or state what the sources say. Claim ids 9aea0db114, b4e2aead8e, 9cd8e283db, 5d490f0a85, e441dbd9db.

### Claims missing inline citation

- **#7 (F5) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — Exposure line
  - Quote: **Exposure:** any GL.iNet router or Comet KVM with the cloud service switched on ({R}).
  - The sentence carries a stray template token '({R})' in place of a citation and no inline link. The scoping condition 'with the cloud service switched on' is RemoteToHome's ('any such router with GoodCloud switched on'; 'If your router or KVM had GL.iNet's cloud service switched on, check it now'); GL.iNet's notice states no such condition and says to install the firmware for the exact model even when checks find nothing. Cite RemoteToHome, drop the token, and say the condition is RemoteToHome's reading. Claim id 8d879a02bb.

### Needs more research

- **#8 (F8) nginx-nginx2root-five-unauth-memory-corruption-flaws** — cves[] cvss 'n/a' on the five added records
  - Quote: cvss: "n/a" (CVE-2026-118899, -120967, -125283, -123640, -120993)
  - NCSC-NL advisory NCSC-2026-0506, already a source of this entry, lists CVSS v4 for all ten: CVE-2026-118899 8.7, CVE-2026-120967 6.3, CVE-2026-120993 6.9, CVE-2026-123640 6.9, CVE-2026-125283 6.9 (https://advisories.ncsc.nl/2026/ncsc-2026-0506.html). The scores were available in a cited source and dropped; fill cvss, and consider citing NCSC-NL in the improvement section.
- **#9 (F8) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — separate older backdoor and months-long compromise omitted
  - Quote: RemoteToHome: 'A separate, older backdoor is installed and running on 49 routers we manage ... with file dates from September 2025 to May 2026 ... adds itself to the list of files kept across upgrades'; BleepingComputer: 'Some of the malicious files recovered from GL.iNet devices had timestamps dating to December 2025'
  - (low confidence) The entry frames the compromise as the 2026-11-20 event and says only that 'start-up entries it does not name survived' an upgrade. The primaries say a separate older persistent backdoor (not detected by GL.iNet's check, with its own keep-list line, only partly cleaned by the fixed firmware) predates the incident by months, and that some devices may have been compromised for months. A responder deciding 'reinstall with settings discarded' needs to know what persists; add one sentence on the older backdoor (behavioral, no file names) and that infection may predate 2026-11-20.

### Surface contradiction

- **#10 (F9) ghostscript-cve-2026-125396-upload2shell-sandbox-escape** — summary: 'Debian and Ubuntu ship fixed packages'; cves[].fixed 'Ubuntu per USN-8949-1'
  - Quote: https://ubuntu.com/security/CVE-2026-125396 lists every Ubuntu release (16.04 to 26.10) as 'Needs evaluation'
  - (low confidence) USN-8949-1 (2026-10-21) does describe the font-operand finding by Paulos Yibelo and predates the CVE assignment, so pwn.ai's mapping is plausible, but Ubuntu's own CVE page has not mapped it. A reader checking the CVE id in Ubuntu's tracker sees 'Needs evaluation'. Add one clause that the USN carries no CVE id and Ubuntu's CVE page has not caught up.

### Editorial / less-is-more flags (advisory)

- **#11 (F11) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — indicator strings in Detection
  - Quote: `crond -i /tmp/.log`, `ps | grep tmp`, chain 'SDWAN_IP_MAPPING', file `/etc/mp_ip_mapping_info`
  - The house rule is zero IOCs (no mutex or file-name indicators, no rule code). These are vendor- and researcher-published check strings and the actionable core of the entry, so the main agent may keep them, but the file path and chain name are file-name/rule indicators; consider describing them behaviorally (an empty state file dated on or after the incident on a router not using the SD-WAN feature).
- **#12 (F11) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix; ghostscript-cve-2026-125396-upload2shell-sandbox-escape** — sourcing_note length and composition rationale
  - Quote: GL.iNet: six sentences incl. 'RemoteToHome's device counts come from routers it owns or manages' and 'The KVM firmware versions are cited to RemoteToHome and BleepingComputer'; Ghostscript: 'so Debian's page is cited for that row'
  - sourcing_note should be two sentences of provenance. The GL.iNet note discusses device counts that appear nowhere in the body and says the KVM versions are cited to BleepingComputer, while the body cites only RemoteToHome for them; the Ghostscript note carries a composition-rationale clause. Trim both.
- **#13 (F11) operation-shadowcloud-gitdoor-graphdoor-meshagent-gov-c2** — entities[] omits actor:famoussparrow
  - Quote: entities: [campaign:operation-shadowcloud, malware:gitdoor, malware:graphdoor, actor:bronze-sandcastle, product:meshcentral-meshagent]
  - The body and the registry edge name FamousSparrow (actor:famoussparrow, with two earlier entries in the store, 2026-09-18 and 2026-05-14) but the entry neither lists it in entities nor links those entries in references[]. Add the entity key so the overlap surfaces on the actor page.
- **#14 (F11) nginx-nginx2root-five-unauth-memory-corruption-flaws** — closing sentence of the Improvement section
  - Quote: The same two fixed releases cover all ten, so the update does not change.
  - Uncited and loosely worded: the same section says CVE-2026-120993 'is fixed in 1.31.9 alone' (nginx.org: Not vulnerable 1.31.9+; the 1.30 branch is unaffected). Fortinet words it as 'versions 1.30.7 stable; 1.31.9 mainline are fixing the issues', so the claim is defensible; say 'updating to 1.31.9 or 1.30.7 covers all ten' and cite nginx.org.

### Classification missing / inconsistent

- **#15 (F17) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — classification A/1
  - Quote: reliability: A, credibility: 1
  - (low confidence) Credibility 1 means confirmed by independent sources and consistent with other information. The incident is confirmed (vendor plus BleepingComputer plus RemoteToHome), but the entry itself records an unresolved contradiction between the vendor ('removes the malware ... settings kept') and RemoteToHome (clean-up partial) and an unconfirmed root cause; 2 fits better.

### Action-item discipline

- **#16 (F18) glinet-goodcloud-exploited-routers-kvm-malware-survives-fix** — actions[0]
  - Quote: Find every GL.iNet router and Comet KVM ... install the security firmware ... capture the process list, connections and firewall rules before restarting it, reinstall the firmware with settings discarded, rotate every key, password and VPN profile ... remove its peers on the server side ...
  - (low confidence) One action bundles five tasks and restates the body's Defender takeaway almost verbatim (check 10b b). Keep the start-now task (inventory GL.iNet routers and KVMs and install the security firmware for each exact model) and leave the compromised-device procedure to the Defender takeaway.

### Considered and not flagged

- Ghostscript, GL.iNet, ShadowCloud priority `notable` and relevance: Ghostscript clears PD-11(b) "otherwise" limb (anonymous print job and viewed Roundcube attachment to command execution, fix diff public, partial PoC); GL.iNet is vendor-confirmed exploitation with a post-fix compromise check; ShadowCloud is substantive primary tradecraft (PD-11(d)). No F7.
- Missed angles: coverage looks complete for a quiet window. KEV diff empty, Cisco and Palo Alto nginx pages unchanged since the entry's last record. GPGME CVE-2026-129975 (GnuPG calls it critical; THN 2026-11-21, no exploitation, no unauthenticated path stated) and BabidiGhost (SOCRadar 2026-11-20, Swiss websites crawled for IBANs, no Swiss victim) are defensible borderline drops as the run record states; revisit GPGME if exploitation or a mail-client trigger path appears.
- Citation dates on living pages (RemoteToHome page metadata 2026-11-21, visible "Last reviewed 2026-11-23"; Debian tracker) are disclosed in the sourcing note or are the page's current state; not flagged.
- ATT&CK mappings checked against the pinned v20.1 dataset: T1574.001 is now "DLL" (T1574.002 revoked into it), so the ShadowCloud mapping is correct; T1211 is "Exploitation for Stealth" and acceptable for a sandbox escape.
- Evidence quotes: 11 of 11 present verbatim on the cited pages in my reads (GL.iNet x2, BleepingComputer, RemoteToHome, THN, pwn.ai x2, VulnCheck, Securelist x3 incl. the part-2 attribution sentence).
- nginx Improvement record: five added flaws match nginx.org (ids, titles, ranges, severities, 120993 mainline-only) and Fortinet (high for 118899, medium for the others); `fields` [cves, body] matches the git diff, `updated_at` untouched, section and record summary agree, main analysis not contradicted.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 6, advisory: 4)

Firm items to fix first: #2 (Defender takeaway cites part 2 for an entry-point statement that is only in part 1), #4 (summary "active since early 2026" contradicts "identified in early 2026" and the late-2024 infrastructure date), #3 ("signed" in four places, no source), #1 (GoodCloud attributed to GL.iNet's own words) and #7 (stray `{R}` token, uncited Exposure line). The remaining items are low confidence as marked.

### Findings summary (machine-readable)

See work/2026-11-23T0355Z-intel/verification.iter1.findings.yaml (16 records).
