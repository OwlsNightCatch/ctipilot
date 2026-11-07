**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T04:09:03Z · ended_at=2026-11-07T04:33:29Z · duration_seconds=1466

## Verification report — 2026-11-07T0256Z-intel (iteration 1)

Scope: 7 new entries, 6 updated entries, run record. Claim ledger 224/224 answered (`verification.iter1.claims.yaml`; claim_ledger coverage check passes: 224/224, 0 missing). Verdicts: 214 ok, 4 F3, 3 F4, 3 F14, 0 unreadable. Method notes: SonicWall's PSIRT page was read from its API JSON (all four cves[] ids, scores, tables and both evidence quotes confirmed verbatim); Siemens tables via CSAF JSON; cisa.gov pages via WebFetch; the OX Security post answers 403 on every transport and WebFetch, so it was read from its RSS feed body (full text), not the page itself; the Mitel KB articles are login-gated and unread. Coverage check: no missed in-window item found (NCSC-CH recent posts 13157/13155/13144/13128/13124/13122 and the KEV window are all covered or deliberately dropped; no November ConnectWise bulletin exists).

### Generic / oversight URLs (replace with specific article)

**F2 #1** (low confidence) `2026-11-07/cve-2026-111497-brotli-...`: sources[4] and the first body citation use `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json`, the 1,769-entry catalogue feed (version 2026.11.06), not a per-CVE page; its source date 2026-10-27 does not match the cited catalogue version. Replacement fetched this iteration: `https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog` (lists CVE-2026-111497, "based on evidence of active exploitation"), already cited by the Node2Shell entry.

### Citation does not support the claim

**F3 #2** (low confidence) Brotli entry, summary / body paragraph 2 / actions[1]: "workaround articles for four", "workaround articles exist for MiVoice Business, OpenScape SBC, SESAP and Contact Center", "KB000129034 (MiVoice Business and OpenScape SESAP)". Mitel MISA-2026-0010 says "Workaround available, see KB article" only on OpenScape SBC (KB000129100), SESAP (KB000129034) and Contact Center (KB000129114); the MiVoice Business row reads "Planned update, see KB article: KB000129034". Three are supported, four are not. Fix: three, and drop MiVoice Business from the workaround clauses and the action.

**F3 #3** ARTEX update 2026-11-07T03:50:15Z: "The agents got in through hardcoded administrator passwords in JavaScript bundles, missing API authentication, command injection, insecure direct object references, weak administrative credentials and template injection ([Check Point])". Check Point introduces that list with "To gain initial access to the signing shop's infrastructure the agents used the following vulnerabilities": one campaign, not all three the preceding sentence names. Fix: attribute the list to the iOS signing-shop campaign.

### Unsupported / hallucinated facts

**F4 #4** WordPress, record 2026-11-07T03:51:45Z summary: "stays reachable at a predictable path during that update on sites running 5.9 or later, whether the package is partial or complete". The Hacker News (the entry's own source): "Not every update exposes the installer ... A smaller partial package ... exposes a site only if it happens to contain them"; and in its Update, Bayram: "whether a partial update is exposed depends on what that specific package contains ... the installer never becomes reachable." The section quotes "isn't partial versus complete" and that 7.1.3 to 7.1.4 is offered as a partial package without that caveat, so the common in-branch update reads as exposed. Fix: add the content caveat and correct the record summary.

**F4 #5** (low confidence) OpenSSH CVE-2026-123158, `status: [exploited, ...]` and tag `actively-exploited`. Previdian (reliability C): its observations "do not show that the target was vulnerable or that the attempt succeeded"; the only success is on Previdian's own honeypot via THN; CISA does not list it. Body and sourcing_note are careful; the machine-read fields are not.

**F4 #6** (low confidence) Aargau title and headline: "a Fachstelle holding directive and enforcement powers" / "a Fachstelle gets directive powers". Communique: "soll ... mit Weisungs- und Durchsetzungsbefugnissen ausgestattet werden" (is to be equipped); the entry's sourcing_note concedes "the powers are the canton's stated plan".

**F4 #7** (low confidence) TUM `techniques: [T1190, T1078]`. T1190 asserts exploitation; TUM says "Unbekannte haben das Portal myTUM angegriffen", heise says "eingedrungen" via a legacy system, and the entry states no source says how the passwords were captured. Only T1078 is evidenced.

**F4 #8** Run record notes: names `2026-11-07/kaspersky-gert-esxi-proxmox-ransomware-monitoring-root-credential`; the file is `entries/2026-11-07/kaspersky-esxi-proxmox-ransomware-monitoring-root-password.md`. The notes also give the Aargau entry as `single-source-national-cert`; its frontmatter says `single-source` (correctly, a canton is not on the carve-out list).

### Quantifier without source

**F14 #9** TUM summary and body: "well over 60,000". heise: "Insgesamt geht es um Daten von gut 60.000 Studenten und Beschäftigten" (a good 60,000). The sourcing_note says "about 60,000".

**F14 #10** (low confidence) ARTEX summary: "a third cluster, the Cambodia-based ... Storm-3358". Microsoft does not number it and the entry already names several other ARTEX users.

### Claims missing inline citation

**F5 #11** (low confidence) sourcing_note clauses without links: SonicWall "other trackers carry 7.5" (the 7.5 exists only as the CISA-ADP score in the CVE record); Aargau "two Swiss outlets relay it without adding facts" (outlets unnamed; the only second source listed, Netzwoche 2025-02-24, does not relay the 2026 communique).

### Drop (low relevance / off-audience / duplicate)

**F7 #12** (low confidence) Brotli new entry: same CVE and same Cisco advisory URL as `2026-10-24/cve-2026-111497-node2shell-...`, which already files vendor product lists (Splunk, Citrix, Broadcom, Palo Alto, Cisco) as changelog records. The entry declares both references so the gate passes; the question is whether it is a genuinely distinct finding. If kept, the building-management and telephony angle must be the stated reason.

**F7 #13** (low confidence) BOSSAI: no Swiss or European victim, confirmed harm is commodity weak-authentication on Taiwanese systems, single vendor source with no defender guidance, and the entry names no out-of-nexus ground (the run notes cite (b)/(d)). Keep at routine length with the transferable point stated, or drop.

**F7 #14** (low confidence) TUM: priority routine is right, but three paragraphs plus two labelled lines for an incident with no stated vector or actor, and no ground named. Two sentences, or name the ground.

### Needs more research

**F8 #15** WordPress Detection line only checks `wp-config.php` and its database. Picus: in the fixing update the wp-config skip already works, but the attacker can "log in to it, and execute PHP code ... read or write files in the live WordPress directory"; Wordfence lists unfamiliar administrator accounts, unexpected plugins and PHP files under wp-content/upgrade. A site that took the fixing update with the folder reachable needs the broader check.

**F8 #16** (low confidence) The cited Hacker News article reports public GitHub repositories claiming an exploit ("Whether the code works has not been established"); the entry carries none of it.

### Surface contradiction

**F9 #17** (low confidence) The same article: "WordPress's own advisory rates the flaw low"; Wordfence 8.1, CISA KEV. The entry gives 8.1 and Patchstack's AC:H, not the vendor's rating.

### Action-item discipline

**F18 #18** (low confidence) Kaspersky actions[0]: four tasks restating the Defender takeaway. Keep one (the credential inventory).

**F18 #19** (low confidence) SonicWall actions[1]: near-verbatim restatement of the Detection paragraph; the advisory states no such check (labelled "from the stated mechanism").

### Editorial / less-is-more flags (advisory)

**F11 #20** WordPress main analysis: "in the first 21 hours, ([Wordfence ...](...))" and "currently through 4.7 ([WordPress.org ...](...)); During a core update" (comma before cite; semicolon then capital), left where clauses were cut.
**F11 #21** Cisco update 2026-11-07T03:49:14Z: nested straight quotes, `"which has the "S/MIME Public Key Harvesting" feature enabled for inbound mail"`.
**F11 #22** FSA entry: run-on list about Oz's write-up (no conjunction); takeaway says "Chrome and Edge policies Oneconsult names" where the article names Chrome Enterprise policy names.
**F11 #23** The run registered product:mitel-mivoice-business, -mitel-openscape-sbc, -mitel-openscape-contact-center, -siemens-industrial-edge, -cisco-roomos, -proxmox-ve, -paessler-prtg-network-monitor, -microsoft-onedrive and the three IoT2050 variants, but the entries naming those products do not carry them in `entities[]` (Brotli: only desigo-cc; Kaspersky: actors only; FSA and Siemens IoT2050: empty).
**F11 #24** BOSSAI tag `organized-crime` vs Acronis "a single individual ... unclear if the attacker has any specific affiliation".
**F11 #25** "Fachstelle" stays German throughout the Aargau entry's reader-facing fields.
**F11 #26** Siemens IoT2050 body: "CERT-FR and NCSC-NL carried the advisory" now sits beside a four-variant list; both relays still list only the Advanced variant with "4.3.4.1".

### Checked and fine (no finding)
Priority and classification calibration (SonicWall high, Brotli notable, TUM/Aargau routine; Admiralty codes match sources.json tiers and corroboration); no IOCs, em dashes (outside `## Update — ` headings), pipeline vocabulary, TLP, org_triage or watchlist use in any entry; every `evidence[]` quote on the new entries and the updates is a verbatim substring of its page (SonicWall via PSIRT JSON; translated quotes carry matching `original:`); the six changelog records name the fields the diffs changed and each section carries a genuine, cited delta; all updated `updated_at` mirrors equal the record `at`; cves[] ids and scores match the per-CVE authority (SonicWall PSIRT, Siemens CSAF, Mitel, Cisco hardening and injection advisories); all source dates match the pages' own dates (Picus published 2026-11-04T20:53Z vs cited 2026-11-05, timezone-level).

### Verdict

NEEDS_FIXES (truth: 10, editorial: 9, advisory: 7)

### Findings summary (machine-readable)

See `work/2026-11-07T0256Z-intel/verification.iter1.findings.yaml` (26 records).
