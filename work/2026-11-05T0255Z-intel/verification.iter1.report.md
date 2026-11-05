**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-05T04:32:39Z · ended_at=2026-11-05T04:57:42Z · duration_seconds=1503

## Verification report — 2026-11-05T0255Z-intel (iteration 1)

Scope: first pass, all 249 ledger claims answered (`verification.iter1.claims.yaml`, `claim_ledger.py --coverage 1`: 249/249, 0 missing; 6 non-ok rows, each also a finding below). Six new entries, five updated entries (whole entry read plus `git diff HEAD`), run record. Sources read this iteration: cached `quote-bodies` first, then live fetches for everything the gate could not read (EUVD API for all five SEPPmail records, SonicWall PSIRT, SentinelLABS via WebFetch, Akamai raw HTML, NCSC.ch posts 13054/13105/13120, NCSC-NL, AWS bulletin, MikroTik 7.26beta5, CERT-FR date, CVE record and EPSS for CVE-2026-107441). The hand-checks the gate listed as not machine-checkable all hold except the AWS quote (F4 #3). The SonicWall affected/fixed table was read from the run's saved reader copy (my own `extract` fetch of the advisory omitted the table but matched everything else).

### Citation does not support the claim
- **#1 (F3)** `2026-10-24/cve-2026-111497-node2shell-...`: "Fixes are in Node.js 22.23.4, 24.22.1 and 26.12.1; end-of-life lines stay affected ([Node.js project, 2026-10-21](…october-2026-security-releases))". The Node.js advisory names only the lines "26.x, 24.x, and 22.x" and says EOL versions are always affected; none of the three version numbers is on the page. HEAD co-cited ELLIO (its table carries them); this run's rewrite dropped it. Re-add ELLIO or the release pages.
- **#2 (F3)** `2026-10-31/cve-2026-98432-linux-kernel-...`: "Debian, CIQ and Amazon Linux kernels are fixed, Ubuntu 22.04 to 26.10 are still marked vulnerable … ([Canonical, 2026-11-04])". The Ubuntu tracker lists only Ubuntu releases; it never mentions Debian, CIQ or Amazon Linux. HEAD cited the Debian tracker, CIQ and AWS; the rewrite collapsed the citations onto Canonical. Re-add them.
- **#3 (F3, low confidence)** Node2Shell entry labels Citrix CTX697300 `2026-11-03` and Splunk SVD-2026-1015 `2026-11-04`; the pages' publication dates are 2026-10-30 (Citrix initial publication) and 2026-10-28 (Splunk first published); the dates used are revision dates. Splunk's section discloses both; Citrix's does not.
- **#4 (F3, low confidence)** SEPPmail entry cites the administration-guide Home page as `2026-11-05`; the page has no such dateline (metadata 2023-01-01). The cited fact is right; the date is the retrieval date.

### Unsupported / hallucinated facts
- **#5 (F4)** Kernel entry `evidence[]`: "Network Load Balancer TCP listeners pass client packets, including IP options, to targets." is not on https://aws.amazon.com/security/security-bulletins/2026-160-aws/ as fetched (Last Updated 11/04/2026 15:25 PST); the page now says only that TLS listeners on NLB "do not receive TCP connections from untrusted sources directly". The rewrite also removed the body sentence that used it, so the record is orphaned and no longer verbatim.
- **#6 (F4, low confidence)** Zyxel entry Detection (rewritten this run): "The exfiltration leaves no persistent artifact on the switch". GreyNoise shows `cp /tmp/info /home/web/tmp/info.txt` staging and says nothing on persistence; the entry's own body says the data is staged to a file on the switch.
- **#7 (F4, low confidence)** APT29 entry: "the sources name no on-device artefact" vs Sekoia's replay-guard cookie `VDGH_TOKEN_REF` and read paths; and the sourcing_note ("withholds delivery hosts, exfiltration hosts") disagrees with the Detection line ("Sekoia's report carries indicators for the delivery and exfiltration infrastructure"); Sekoia's own text is mixed (IOC tables list delivery/exfiltration domains; the IOC section says several are not shared).

### Needs more research
- **#8 (F8)** Node2Shell: to hold the analysis at 549 words the rewrite removed correct, cited content (HEAD: "process.versions.brotli reads 1.2.0 on patched and vulnerable builds alike", "the fixed 24.22.1 rejected the same input", "Cisco and Palo Alto say they know of no malicious use…", Zscaler's 402 events). The version-reading caveat now lives only in `actions[0]`, uncited; the summary still asserts the Cisco/Palo Alto point with no body support.
- **#9 (F8)** Kernel entry Exposure lost its "how to tell": Go team page ("As of Go 1.24, Go programs enable MPTCP by default for listen sockets on Linux"), Akamai (`ss -M -l -n -p -e`; request-socket migration via `net.ipv4.tcp_migrate_req` or a BPF reuseport program is a second path), and the earlier sysctl check.

### Strengthen primary source / missing citation
- **#10 (F5, low confidence)** CVE-2024-27834 `affected/fixed` names iOS 17.5, Safari 17.5, Sonoma 14.5, tvOS 17.5, watchOS 10.5 (Apple pages 120905/120896/120903/120901/120902, listed in CISA's KEV notes) and the kernel entry's `fixed` names MikroTik 7.26beta5; true on the pages I read, but none is in `sources[]`.

### Surface contradiction
- **#11 (F9, low confidence)** Kernel entry: "XCP-ng released a kernel fix on 2026-11-04" vs Vates VSA-2026-056 "As of 2026-11-03, the kernel package for XCP-ng 8.3 have been updated".

### Org-triage / priority / classification / actions
- **#12 (F16, low confidence)** Vaud device-code entry is `notable`; cantonal warning of an active campaign with several organisations affected, constituency tenants plausibly exposed, 7-day decision, no `high` disqualifier; the earlier Kali365 device-code entry was `high`.
- **#13 (F17, low confidence)** Zyxel entry `classification` B/1 not revisited after the update; the new central claim rests on Binarly alone (summary says so), which fits credibility 2.
- **#14 (F18, low confidence)** Danfoss `actions[0]` bundles five tasks in ~170 words and restates CERT-FR/CSIRT Italia body guidance; "in writing" is in no source.

### Single-source flag
- **#15 (F12, low confidence)** Run-record note calls SEPPmail "single-source-national-cert"; the entry carries `single-source`.

### Editorial / less-is-more flags (advisory)
- **#16 (F11)** `sourcing_note` fetch-transport language ("in some readers … text extraction drops", Sophos; "Sekoia's own table, which text extraction drops", APT29), longer than two provenance sentences.
- **#17 (F11)** Xerox record typed `improvement` carries a genuine post-publication vendor revision (bulletin v5, 2026-11-03, new interim mitigations); typed `update` it would re-float.
- **#18 (F11)** Zyxel headline states Binarly's attribution as fact (summary hedges "Binarly alone"); iSCSI headline "lets any host read shared disks" drops the stated precondition.
- **#19 (F11)** 15 product keys in `entities_added` are linked by no entry (SonicWall GMS entry has `entities: []`; iSCSI entry omits `product:microsoft-iscsi-target-server`).
- **#20 (F11, low confidence)** Sophos entry tag `supply-chain` is unsupported by its sources.

### Missed angles
None evidenced. Checked: the NCSC.ch hub listing (all in-window advisories are covered or dated outside the 26 h window and already in the store: WS_FTP, Drupal Commerce, Barracuda, Veeam), the KEV window diff (one addition, covered), and two web searches (exploited-vulnerability advisories of 2026-11-04; Swiss municipal/cantonal incidents of November 2026) that surfaced nothing new. Coverage looks complete. Priority calibration of the other entries (SEPPmail notable given conditional exposure, SonicWall GMS routine, kernel notable, Xerox notable) is defensible.

### Prior-iteration deltas
None (first pass).

### Verdict
NEEDS_FIXES (truth: 7, editorial: 8, advisory: 5)

Hard defects to fix first: #1, #2, #5 (a re-cite or two and one stale evidence record); #8/#9 are the rewrite-by-deletion side effects of the word-count rule and are best fixed by restoring one cited sentence each.

### Findings summary (machine-readable)
See `work/2026-11-05T0255Z-intel/verification.iter1.findings.yaml` (20 records).
