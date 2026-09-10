**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-10T05:33:33Z · ended_at=2026-09-10T05:43:15Z · duration_seconds=582

## Verification report — 2026-09-10T0410Z-intel (iteration 4)

### Prior-iteration deltas — walked and confirmed

Iteration 3's remediations were re-checked against fetched primary sources this iteration, not merely re-read:

1. **CISA KEV due date (CVE-2026-87491).** Fetched the CISA alert page directly — it lists only the four added CVE names and BOD 26-04 boilerplate, no due dates, confirming iteration 3's own finding. Fetched the KEV JSON feed live: `dueDate: 2026-09-23` for CVE-2026-87491 — matches the entry's claim exactly. Fix holds.
2. **PaperCut "12 victim organizations."** Fetched the GreyNoise blog directly. Verbatim: "GreyNoise observed the adversary achieved domain admin against only 12 victim organizations." The entry's evidence-block quote and body text now match this exactly (previously "12 of the 440 instances"). Fix holds.
3. **SAP KRNL64NUC split.** Fetched CERT-EU advisory 2026-011 directly: "KRNL64NUC 7.22, 7.22EXT" / "KRNL64UC 7.22, 7.22EXT, 7.53, 8.04" — the entry's frontmatter `affected` field for CVE-2026-44756 now reproduces this exactly, component by component. Fix holds.
4. **Fortinet FortiSASE version Contradiction.** Fetched GHSA-mj8x-m8f5-x4w8 (FortiSASE 25.2.b / 25.1.a.2) and SentinelOne's page (FortiSASE 25.1.39 and 25.1.51) directly — both values confirmed as stated, and the entry's `sourcing_note` now discloses the discrepancy explicitly rather than silently resolving it. Fix holds.
5. **CVE-2026-20079 / CVE-2026-19490 KEV bookkeeping.** Fetched the live KEV JSON feed: both CVEs show `dateAdded: 2026-09-09`, `dueDate: 2026-09-12`. Both entries' new changelog sections state exactly this. The Cisco entry's `type: update` (material — status moved patch-available → exploited) and the NetScaler entry's `type: correction` (bookkeeping — already recorded exploited) are both the right record types per their actual deltas. Both diffs are internally consistent (git diff reviewed in full) with no silent edits. Fix holds.
6. **Fortinet reliability C.** Confirmed via `sources/sources.json`: `socradar -> C`. The entry's `classification.reliability: C` now matches. Fix holds.
7. **Fortinet ENISA EUVD 7.4 citation.** Fetched the EUVD API directly: `baseScore: 7.4`, vector includes `E:P/RL:W/RC:C` (a temporal-adjusted score off the CNA's 8.1 base) — matches the entry's characterization exactly, and ENISA is now in `sources[]` with an inline citation. Fix holds.
8. **Fortinet techniques T1055.002/T1027.** Fetched the SOCRadar ATT&CK table directly: it maps `run.ps1` process injection to T1055.002 (not the previously-mapped T1055, generic) and separately maps T1027 to the Base64/XOR obfuscation. Confirmed both edits.

All eight re-checks hold. No regressions found in the remediated material.

### New findings (this iteration's cold pass)

### F4 — Unsupported / hallucinated facts

**#1 — `bluemoon-exploit-kit-four-state-actors-chrome-windows-chain`, registry entity `tool:ghostchrome-x`.** The entry's frontmatter lists `entities: [..., "tool:ghostchrome-x", ...]`, and `entities/registry.yaml` (added this run, per `entities_added`) carries:
> `"Chrome/Chromium extension-integrity-bypass technique ... reused by APT31/TA412 to install the GemStone malicious extension ... (Proofpoint, 2026-09-08)."`
Fetched the entry's cited Proofpoint source in full (`https://www.proofpoint.com/us/blog/threat-insight/once-bluemoon-multiple-state-aligned-threat-actors-rapidly-adopt-novel-exploit`, 516 lines extracted): the string "GhostChrome" appears exactly once, only inside a hyperlink's URL slug — `[Rubrik Zero Labs](https://zerolabs.rubrik.com/blog/inside-ghostchrome-x-chrome-extension-integrity-bypass)` — never in Proofpoint's own visible prose. Proofpoint credits the forgery technique to "Rubrik Zero Labs" and "Synacktiv," neither of which is cited anywhere in this entry's `sources[]`. The registry record's own attribution "(Proofpoint, 2026-09-08)" for the *name* GhostChrome-X is therefore wrong — Proofpoint never names the technique that; the name comes from an uncited third source. Separately, the entry's body text never once uses the term "GhostChrome" or "GhostChrome-X" — a reader following the `tool:ghostchrome-x` entity link from the site's `/graph/` would find no textual anchor for it in this entry at all. Fix: either cite Rubrik Zero Labs directly and use the name in the body, or drop the `tool:ghostchrome-x` tag from this entry's `entities[]` and correct the registry attribution.

### F6 — Strengthen primary source (low confidence)

**#1 — `sap-september-2026-overpass-s4get-preauth-rce`.** The first `sources[]` record (role: primary) is CERT-EU's advisory. The entry's own `sourcing_note` states: "CERT-EU's advisory relays SAP's patch-day fixes and Onapsis's own research rather than independently assessing the flaws." Two genuine primaries (Onapsis Research Labs' two blog posts, the actual disclosing researchers) are already present later in the same `sources[]` list and already carry `role: primary`. Per check 6, national-CERT advisories are second-tier/corroborating; CERT-EU listed first with `role: primary` ahead of the two research-lab primaries is a minor ordering/labeling inconsistency, though not a case where CERT-EU is the *only* source (so the hard F6 bar in check 6's table does not strictly apply). Low confidence because CERT-EU is on the org profile's national-CERT carve-out list and this advisory is CERT-EU's own (`cert.europa.eu/publications/security-advisories/2026-011/`), which arguably qualifies as a "regulator filing." Suggested fix, if any: re-label CERT-EU `role: corroborating` given the two Onapsis primaries already anchor the entry.

### F11 — Editorial / less-is-more (advisory, carried forward and independently re-confirmed)

**#1 — `checkpoint-quantum-vpn-cert-preauth-rce-cvss98`.** Fetched Forkast News directly this iteration. Confirmed the aggregator pattern independently: the article cross-links five other unrelated CVE write-ups (PaperCut, N-able, Microsoft, SAP, Ivanti) all under the identical "authentication gap" framing template, and closes by citing a further aggregator (`SecurityOnline.info`) rather than original research. The two Check Point vendor advisories remain the solid primaries and every fact Forkast is cited for checks out. No action needed beyond what iteration 3 already declined.

**#2 — `2026-09-06/chaotic-eclipse-falconflank-prettyprague-edr-av-lpe-drops`.** Independently re-read the LevelBlue SpiderLabs technical detail for HardBreacher (session-namespace symlink + `NtCreateUserProcess` PPID spoofing). T1574.001 (DLL Search Order Hijacking) is a plausible but imperfect fit for a session-namespace `DosDevices` redirect rather than a classic search-order hijack; T1574.008 (Path Interception by Search Order Hijacking) is arguably no better a fit. Concur with iteration 3's own low-confidence, declined disposition — no fix needed.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 1, advisory: 2)`

All eight of iteration 3's remediations were independently re-verified against live primary sources (CISA KEV JSON feed, GreyNoise, CERT-EU, GHSA, SentinelOne, ENISA EUVD, sources.json, SOCRadar's own ATT&CK table) and all hold. The full ten-entry scope was fact-checked end to end this pass: every inline citation in the five new entries was fetched and cross-checked (Fortinet/SOCRadar/GHSA/SentinelOne/ENISA/CISA-KEV; Chrome/Google/Help Net Security/Hacker News/CERT-FR/NCSC-NL/CISA-KEV/NVD; SAP/CERT-EU/Onapsis×2; Check Point/both vendor SK advisories/Forkast; BlueMoon/Proofpoint/The Record/The Hacker News, plus both referenced entries for the declared CVE-overlap dedup), and every changed field in the five updated entries' diffs was checked against its cited source (PaperCut/GreyNoise; Berlin/heise Süddeutsche-citing article, translations verified word-for-word; Chaotic Eclipse/LevelBlue SpiderLabs; NetScaler and Cisco FMC KEV corrections against the live feed). Dedup was checked against `prior_coverage.json` (none of the six new CVEs appear in the 14-day index) and `state/cves_seen.json` (all six show `first_seen: 2026-09-10`, confirming genuinely new coverage). Entity registry additions were spot-checked for collisions (none found) and alias correctness (APT31/TA412 aliases match Proofpoint's own list) — except for the GhostChrome-X mismatch above. Classification blocks (reliability/credibility) were checked against `sources/sources.json` ratings across all five new entries and all now hold correctly (chrome-releases A, checkpoint-support A, onapsis B, proofpoint B, socradar C). No org-triage or watchlist artifacts found (correct per the no-op profile). No IOCs, vanity metrics, or workflow-internal language found. Coverage shape: the run record's own "borderline-drop" and coverage-backlog notes read as a defensible, deliberate application of the strict relevance gate; I did not identify an additional plausible in-window miss beyond what the run record already logs as backlog.

The two new findings are modest: one genuine truth-class defect (an entity tag with a misattributed source and no textual anchor in the body) and one low-confidence editorial nitpick (source ordering). Neither blocks a defensible remediation in a single pass, but per the loop contract this is not yet CLEAN.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "bluemoon-exploit-kit-four-state-actors-chrome-windows-chain — entities[] tool:ghostchrome-x"
  url_or_quote: "registry.yaml: '...reused by APT31/TA412 to install the GemStone malicious extension... (Proofpoint, 2026-09-08)'"
  summary: "the string GhostChrome only appears in a Proofpoint hyperlink's URL slug (to Rubrik Zero Labs, uncited in this entry's sources[]); Proofpoint's own visible text never names the technique GhostChrome-X, and the entry body never uses the term at all — attribution to Proofpoint is wrong and the entity has no textual anchor in the entry."
- code: F6
  category: strengthen-primary-source
  section: new-entries
  item: "sap-september-2026-overpass-s4get-preauth-rce"
  url_or_quote: "https://cert.europa.eu/publications/security-advisories/2026-011/ (role: primary, listed first)"
  summary: "(low confidence) CERT-EU is listed first with role:primary even though the entry's own sourcing_note says CERT-EU merely relays SAP/Onapsis's findings; two genuine Onapsis research-lab primaries are already present later in sources[]. CERT-EU is on the national-CERT carve-out list and this is its own advisory, so this may be defensible as-is."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "checkpoint-quantum-vpn-cert-preauth-rce-cvss98"
  url_or_quote: "https://forkast.news/check-point-quantum-vpn-drops-two-cvss-9-8-cves-in-the-same-certificate-path-vpn-infrastructure-joins-the-auth-gap/"
  summary: "independently re-confirmed as formulaic aggregator content (identical 'authentication gap' template cross-linked across five unrelated CVE posts); facts checked out; role remains corroborating, no action needed."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-09-06/chaotic-eclipse-falconflank-prettyprague-edr-av-lpe-drops"
  url_or_quote: "T1574.001 vs T1574.008 for HardBreacher's session-namespace symlink redirect"
  summary: "concur with iteration 3's low-confidence, declined finding — both sub-techniques are an imperfect fit; no fix needed."
```
