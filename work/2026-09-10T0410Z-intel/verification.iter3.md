**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-10T05:15:26Z · ended_at=2026-09-10T05:24:59Z · duration_seconds=573

## Verification report — 2026-09-10T0410Z-intel (iteration 3)

### Prior-iteration deltas walk (iteration 2 → this pass)

1. **sourcing_note NVD/CNA/EUVD scores (cve-2025-25249):** re-fetched NVD live API (`services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2025-25249`) — confirms `nvd@nist.gov` Primary CVSS 3.1 = 9.8, `psirt@fortinet.com` Secondary = 8.1; ENISA EUVD API confirms `baseScore: 7.4`. The remediated sourcing_note ("NVD's own analyst-assigned score is 9.8... CNA/GHSA-published score... is 8.1... ENISA EUVD's temporal score is 7.4") is accurate. **Holds.**
2. **T1055.002/T1059.001 + body injection sentence (cve-2025-25249):** fetched SOCRadar's full ATT&CK table (via jina) — it maps "the threat actors executed run.ps1 to perform process injection using OpenProcess, VirtualAllocEx, and WriteProcessMemory into svchost.exe" to exactly T1055.002 + T1059.001. The body's added sentence and the narrowed techniques[] match verbatim. **Holds.**
3. **CISA KEV due-date citation (cve-2026-87491):** fetched the cited CISA alert page in full (`cisa page` bridge) — it lists the four added CVEs and BOD 26-04 boilerplate but contains **no due date anywhere in the page**. The due date (2026-09-23) is real (confirmed via `cisa-kev` JSON and NVD's `cisaActionDue` field) but is not stated on the page cited for it. **The remediation introduced a new F3 (citation-adjacency) defect** — see #1 below.
4. **berlin-landesnetz sources[] cleanup:** `git diff` confirms only the one heise/Krempl article was added, and all three new evidence[] quotes cite it. Fetched the article directly — all three quotes (Kiesewetter "gravierendem Ausmaß"/national-security, the rbb/Lichtenberg quote, the Meike Kamp guidance quote) are verbatim substrings of the page, and the English translations are faithful. **Holds.**

### Citation does not support the claim

#1 (F3) `cve-2026-87491-chrome-v8-oob-write-seventh-2026-zero-day`: body clause "CISA added the CVE to KEV the same day with a due date of 2026-09-23 ([CISA, 2026-09-09](https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog))." Fetched that exact URL in full — it only lists the four CVE names/titles and generic BOD 26-04 text; it never states a due date for any CVE. The due date lives only in the separate KEV catalog JSON (`cisa-kev` / NVD's `cisaActionDue`), which is not cited here. The fact is true, the citation does not carry it (adjacency failure per check 2d) — this is the exact defect class iteration 2's own remediation (for the prior F5) introduced.

#2 (F3, low confidence) `entries/2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce.md` Update — 2026-09-10T05:00:00Z: body states "Domain admin was ultimately reached against only twelve of the 440 compromised instances — 'GreyNoise observed the adversary achieved domain admin against only 12 victim organizations'". GreyNoise's own text (confirmed via extract) says domain admin was reached against "12 victim organizations", not 12 of the 440 *instances* — 395 organizations hosted the 440 instances, so "twelve of the 440... instances" mischaracterizes the unit the source itself uses.

### Unsupported / hallucinated facts

#3 (F4, low-moderate confidence) `sap-september-2026-overpass-s4get-preauth-rce`: `cves[CVE-2026-44756].affected` reads "SAP kernel KRNL64NUC/KRNL64UC 7.22(+7.22EXT)/7.53/8.04..." — CERT-EU's advisory (fetched) lists KRNL64NUC only at "7.22, 7.22EXT" and KRNL64UC at "7.22, 7.22EXT, 7.53, 8.04"; the entry's condensed notation implies KRNL64NUC also reaches 7.53/8.04, which the cited source does not support.

### Surface contradiction

#4 (F9) `cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat`: the entry's `affected` field states "FortiSASE 25.1.a.2, 25.2.b", sourced from GHSA-mj8x-m8f5-x4w8's own description (confirmed verbatim: "FortiSASE 25.2.b, FortiSASE 25.1.a.2"). But SentinelOne — also cited in this entry's `sources[]` as corroborating — states a completely different version scheme for the same product: "Fortinet FortiSASE versions 25.1.39 and 25.1.51" (confirmed via extract). Two cited sources disagree on which FortiSASE builds are affected, using incompatible version-numbering conventions, and the entry silently uses only GHSA's numbers with no `Contradiction:` note.

### Missed angles

#5 (F10, high confidence, high severity): This run's own CISA alert citation (`https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog`, already fetched and cited twice this run) lists **four** CVEs added to KEV on 2026-09-09, not two. This run researched and published entries for two of them (CVE-2025-25249 Fortinet, CVE-2026-87491 Chrome) but the other two are CVEs the store **already has entries for**, and neither was updated to reflect the KEV addition:
  - `entries/2026-08-04/cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix.md` — status still `[patch-available]`, summary still says "Cisco reports no malicious use of this CVE." Confirmed via the live `cisa-kev` JSON: CVE-2026-20079 was added 2026-09-09, `dueDate: 2026-09-12` (2 days out), `forensicTriage: Yes`.
  - `entries/2026-08-20/cve-2026-19490-netscaler-gateway-aaa-auth-bypass.md` — its most recent body line explicitly says "CVE-2026-19490 has not been added to CISA's KEV catalog as of this update" (2026-09-08 update), which the very next day's CISA alert falsified. Confirmed via `cisa-kev` JSON: added 2026-09-09, `dueDate: 2026-09-12`, `forensicTriage: Yes`.
  Both are pre-auth RCE/auth-bypass on internet-facing edge devices (Cisco Secure FMC, Citrix NetScaler) newly confirmed under active exploitation with a 3-day federal remediation window — exactly the critical/high signal check 11 says a miss on is negligence. Suggested fix: append an `update` changelog record to each existing entry noting the 2026-09-09 KEV addition, citing the same CISA alert URL already in hand, and moving `cves[].status` to include `exploited`/`cisa-kev`. Suggested search to confirm no other angle was missed: re-run `tools/kev_window_diff.py` against `state/cves_seen.json` for full-catalog CVEs, not only never-seen ones.

### Editorial / less-is-more flags (advisory)

#6 (F11, low confidence) `cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat`: `techniques[]` includes `T1555` (Credentials from Password Stores). SOCRadar's own ATT&CK table maps the entry's cited credential-harvest behavior (FortiGate config/credential-store files) to `T1552.001` only (already present) — `T1555` has no distinct supporting behavior in the body or the source's own mapping.

#7 (F11, low confidence) `cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat`: the body describes "downloads and XOR-decrypts a payload" (PowerShell/run.ps1), which SOCRadar's own ATT&CK table maps to `T1027` (Obfuscated Files or Information: "Base64 encoding, custom XOR encryption keys"). `T1027` is absent from `techniques[]` despite the behavior being described and source-mapped.

#8 (F11, carried forward, no action needed) `checkpoint-quantum-vpn-cert-preauth-rce-cvss98`: Forkast News (corroborating role) re-confirmed as formulaic aggregator content — the fetched article recurs its own "authentication gap" glossary term across PaperCut, N-able, Microsoft, SAP and Ivanti items in near-identical paragraph structure. Facts checked against it are accurate (CWE-295/CWE-122, R82.20 unaffected, distinction from CVE-2026-50751). This is the same item iteration 1 flagged and the main agent left in place (role is corroborating, the two Check Point sk advisories are the real primaries) — re-confirming the observation still holds, no further action needed.

#9 (F11, low confidence) `entries/2026-09-06/chaotic-eclipse-falconflank-prettyprague-edr-av-lpe-drops.md` update: `techniques[]` added `T1574.001` (DLL Search Order Hijacking) for HardBreacher's mechanism — LevelBlue's own description is a session-namespace DOS-device symbolic-link redirect of an absolute DLL path (`\Sessions\0\DosDevices\{AuthId}\` → fake `C:` tree), not an unqualified-search-order hijack. `T1574.008` (Path Interception by Search Order Hijacking, which covers junction/symlink-based redirection) may be the closer fit; flagging the mapping as uncertain rather than asserting it is wrong.

### Classification missing / inconsistent

#10 (F17) `cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat`: `classification.reliability: B`. The entry's own `sourcing_note` states the entire exploitation narrative (PivotC2, actor, victim counts) "rests solely on SOCRadar." `sources/sources.json` rates SOCRadar `reliability: C` explicitly ("CTI blog mostly aggregation with occasional original TRU research; corroborate single-vendor claims"). CISA (A) only supports the KEV-addition fact, not the substantive technical narrative the entry is actually built on. A `B` overstates the source basis for the entry's core content by a full letter grade against sources.json's own rating of that source.

### Single-source items missing [SINGLE-SOURCE] flag

#11 (F5, low severity) `cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat`: `sourcing_note` states "ENISA EUVD's temporal score is 7.4" as a specific, checkable fact, but ENISA EUVD appears nowhere in `sources[]` and is never cited with a URL anywhere in the entry (unlike the Chrome entry in the same run, which lists and cites ENISA EUVD explicitly). The figure is correct (confirmed via the EUVD API this iteration) but the entry gives the reader no way to verify it themselves.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 4, advisory: 4)`

Coverage note: no other missed angle beyond #5 was identified with a nameable in-window source this pass — the borderline-drop rationale for Veradigm and Mantax Otax in the run record both hold up against § Organization context's stricter breach-entry bar (checked qualitatively, not re-researched). Style discipline (no IOCs, no vanity metrics, English throughout, no workflow-internal language) held across all 8 entries in scope. `actions[]` discipline held on all 5 new entries and the 2 updated entries that added actions (concrete, single-item, finding-specific; PaperCut now carries 3 actions total, at the stated ~3 ceiling but each still finding-specific). No org_triage or watchlist_hit usage found (compliant with the no-scheme-configured deployment rule). This is not the second of two consecutive CLEANs — iteration 2 was NEEDS_FIXES, and this pass also returns NEEDS_FIXES, so the CLEAN chain has not started.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "cve-2026-87491-chrome-v8-oob-write-seventh-2026-zero-day"
  url_or_quote: "https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog"
  summary: "Body cites this URL for 'a due date of 2026-09-23'; the fetched page lists only the four added CVE names and BOD 26-04 boilerplate, no due date anywhere. Due date (confirmed true via cisa-kev JSON / NVD cisaActionDue) is uncited. Iteration 2's remediation for the prior F5 introduced this adjacency defect."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce (low confidence)"
  url_or_quote: "Domain admin was ultimately reached against only twelve of the 440 compromised instances"
  summary: "GreyNoise's own text says domain admin was reached against '12 victim organizations', not 12 of the 440 instances; entry conflates instances with organizations."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "sap-september-2026-overpass-s4get-preauth-rce (low-moderate confidence)"
  url_or_quote: "SAP kernel KRNL64NUC/KRNL64UC 7.22(+7.22EXT)/7.53/8.04"
  summary: "CERT-EU's advisory lists KRNL64NUC only at 7.22/7.22EXT; only KRNL64UC extends to 7.53/8.04. Entry's condensed notation overstates KRNL64NUC's affected range."
- code: F9
  category: surface-contradiction
  section: new-entries
  item: "cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat"
  url_or_quote: "affected: ... FortiSASE 25.1.a.2, 25.2.b"
  summary: "GHSA-mj8x-m8f5-x4w8 states FortiSASE 25.2.b/25.1.a.2 (used by entry); SentinelOne, also cited as corroborating, states FortiSASE 25.1.39 and 25.1.51 — a different version scheme for the same product. Entry silently follows GHSA with no Contradiction note."
- code: F10
  category: missed-angle
  section: whole-run
  item: "entries/2026-08-04/cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix.md and entries/2026-08-20/cve-2026-19490-netscaler-gateway-aaa-auth-bypass.md"
  url_or_quote: "https://www.cisa.gov/news-events/alerts/2026/09/09/cisa-adds-four-known-exploited-vulnerabilities-catalog"
  summary: "This alert (already cited twice this run) added 4 CVEs to KEV on 2026-09-09; 2 became new entries but the other 2 (CVE-2026-20079 Cisco FMC, CVE-2026-19490 Citrix NetScaler) are already-covered CVEs whose existing entries were not updated, despite dueDate 2026-09-12 and forensicTriage:Yes on both per cisa-kev JSON. Suggested query: re-run tools/kev_window_diff.py against state/cves_seen.json (full catalog), not only never-seen CVEs."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat (low confidence)"
  url_or_quote: "techniques: [... T1555 ...]"
  summary: "SOCRadar's own ATT&CK table maps the credential-harvest behavior to T1552.001 only (already present); T1555 has no distinct supporting behavior."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat (low confidence)"
  url_or_quote: "downloads and XOR-decrypts a payload"
  summary: "SOCRadar's own ATT&CK table maps this XOR/obfuscation behavior to T1027, which is described in the body but absent from techniques[]."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "checkpoint-quantum-vpn-cert-preauth-rce-cvss98"
  url_or_quote: "https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/"
  summary: "Re-confirmed formulaic aggregator content (recurring 'authentication gap' framing across many unrelated CVEs); facts checked accurate. Carried forward from iteration 1's F11, main agent already left it as-is (corroborating role only); no further action needed."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-09-06/chaotic-eclipse-falconflank-prettyprague-edr-av-lpe-drops (low confidence)"
  url_or_quote: "techniques: [... T1574.001 ...]"
  summary: "HardBreacher's mechanism (session-namespace DOS-device symlink redirect of an absolute DLL path) may fit T1574.008 (path interception via junction/symlink) better than T1574.001 (unqualified DLL search-order hijacking); flagging as uncertain."
- code: F17
  category: classification
  section: new-entries
  item: "cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat"
  url_or_quote: "classification: {reliability: B, credibility: 2}"
  summary: "Entry's own sourcing_note says the substantive narrative rests solely on SOCRadar, which sources.json rates reliability C (not B); CISA (A) only supports the KEV-addition fact. B overstates the source basis by a letter grade."
- code: F5
  category: missing-citation
  section: new-entries
  item: "cve-2025-25249-fortinet-fortios-capwap-pivotc2-rat"
  url_or_quote: "ENISA EUVD's temporal score is 7.4"
  summary: "ENISA EUVD is not in sources[] and is never cited with a URL anywhere in the entry, though its score is stated as fact in sourcing_note (confirmed correct via API, but unverifiable to a reader)."
```
