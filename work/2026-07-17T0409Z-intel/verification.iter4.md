**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-17T05:21:27Z · ended_at=2026-07-17T05:27:19Z · duration_seconds=352

## Verification report — 2026-07-17T0409Z-intel (iteration 4)

Cold read of all 8 new entries + run record. Both iteration-3 prior findings independently re-verified against the primary sources (fresh `WebFetch` in this iteration, not assumed):

1. **ACR Stealer "Chromium/Firefox" fix (prior F4).** Fetched the Microsoft source directly: it states "The malware also accesses credential stores belonging to Chromium-based browsers, including Google Chrome and Microsoft Edge" — no Firefox mention anywhere. The entry now reads "Chromium-based browser credential stores" in both frontmatter summary and body. **Confirmed correctly fixed.**
2. **Talos Polygon-address removal (prior F11).** Fetched the Talos source directly: it does carry the raw contract address `0x6ae382ed2154cc84c6672e4e908cd2c69c1b35ba`. Read the entry's evidence[] (now 1 record) and full body text end-to-end — the address does not appear anywhere in the entry; the blockchain-dead-drop technique is described without the IOC. **Confirmed correctly fixed**, no-IOC posture holds.

Full fresh F1–F18 pass followed, all 8 entries + run record, cold. `WebFetch`/bridge-fetched every inline source URL (Microsoft, Talos, NCA, CPS, The Register, Kaspersky Securelist, CISA alert, MSRC via jina, Mozilla MFSA, NCSC-NL via `ncsc-nl csaf`, Garante x2, NCSC-CH via `ncsc-csh post`, both Abacus PSIRT pages). All URLs resolve to specific articles/advisories and land where cited. All named CVEs, version numbers, CVSS scores, fine amounts, sentencing figures, and quoted facts cross-checked against the fetched pages and confirmed accurate, with two exceptions below.

### Unsupported / hallucinated facts

**F4.** `2026-07-17/scattered-spider-tfl-sentencing-helpdesk-vishing` — evidence[] quote:
> "148 systems became inoperable, including critical ones that required significant manual workarounds."
attributed to UK National Crime Agency. Fetched the NCA page directly (twice, including a targeted re-fetch isolating every sentence containing "148 systems" or "manual workarounds") — the only matching sentence on the page reads:
> "All 27,000 of TfL's employees were forced to attend a TfL office for a password reset and a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays."
The entry's quote truncates before "and delays" and closes with a period that does not exist at that point in the source (the source's period falls after "delays," not after "workarounds"). The underlying fact (148 systems, manual workarounds) is accurate and not in dispute — this is a quote-fidelity defect (the printed quote is not a copy-pasteable, unchanged substring of the page per check 4b), not a fact fabrication. Minor severity but flagged per the strict verbatim-substring rule this run has otherwise applied consistently (iteration 1 flagged and fixed a similar splice on this same entry).

### Surface contradiction

**F9.** `2026-07-17/firefox-152-0-6-wasm-site-isolation-public-exploit` — the entry cites NCSC-NL as a full `role: primary` source (not corroborating) and its headline/summary/sourcing_note carry only Mozilla's own qualitative advisory-impact label: "critical-impact flaws" / "both CVEs carry advisory impact 'Critical'" (confirmed via direct fetch of `mfsa2026-67`: "Both CVEs carry a critical impact rating"). Fetching NCSC-NL's own structured CSAF record for this advisory (`python3 tools/fetch_source.py ncsc-nl csaf NCSC-2026-0242`) shows NCSC-NL independently computed CVSS 3.1 base scores of **5.4 (MEDIUM)** for CVE-2026-15719 and **4.3 (MEDIUM)** for CVE-2026-15718 — a materially different severity read than Mozilla's qualitative "Critical" label, from a second cited primary source. The entry's `cvss: null` frontmatter fields and sourcing_note explain only that "Mozilla does not assign a numeric CVSS" — they do not disclose that NCSC-NL, the entry's other primary source, does assign a numeric CVSS, and that it disagrees with the "Critical" framing. This does not by itself argue for a different `priority` (the CVSS-medium read, if anything, supports the current `notable` rather than an escalation), but per check 9 a contradiction between sources cited for the same item should be surfaced in the entry (e.g. a `Contradiction:` clause) rather than silently carried only from the source that supports the higher-drama framing.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)`

Both iteration-3 fixes independently confirmed correct and holding. Two new findings from this cold pass, both minor: one quote-fidelity defect (F4) and one unsurfaced cross-source severity contradiction (F9). No broken URLs, no generic/oversight URLs, no unsupported entity/CVE/actor claims beyond the above, no missing citations, no drop-worthy relevance issues, no single-source flag drift (all `verification`/`sourcing_note` values checked and correct), no classification/org-triage drift found (all `classification` blocks present, letters/numbers consistent with source tier and corroboration pattern used consistently across this run's single-source vs multi-source entries), ATT&CK ids spot-checked against the pinned dataset (`attack/enterprise-attack.json`) and all active/valid, `actions[]` reviewed on all 8 entries and none padded or generic, dedup/update_of targets confirmed to exist and be genuinely the same story with a real delta (SharePoint CVE-2026-58644, TfL sentencing). No missed angle identified with enough confidence to name a plausible in-window source beyond what the run record already logs as coverage gaps.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: operational
  item: "2026-07-17/scattered-spider-tfl-sentencing-helpdesk-vishing"
  url_or_quote: "148 systems became inoperable, including critical ones that required significant manual workarounds."
  summary: "NCA source's actual sentence is '...a total of 148 systems became inoperable, including critical ones that required significant manual workarounds and delays.' The entry's evidence[] quote truncates before 'and delays' and closes with a period that is not present at that point in the source — the printed quote is not copyable unchanged from the page. Minor (fact itself — 148 systems — is correct), but the quote-fidelity rule is violated."
- code: F9
  category: surface-contradiction
  section: operational
  item: "2026-07-17/firefox-152-0-6-wasm-site-isolation-public-exploit"
  url_or_quote: "Mozilla mfsa2026-67 rates both CVE-2026-15718 and CVE-2026-15719 advisory-impact 'Critical' (confirmed via WebFetch: 'Both CVEs carry a critical impact rating'). NCSC-NL's own CSAF record (fetched via `tools/fetch_source.py ncsc-nl csaf NCSC-2026-0242`) independently scores CVE-2026-15719 CVSS 3.1 baseScore 5.4 (MEDIUM) and CVE-2026-15718 CVSS 3.1 baseScore 4.3 (MEDIUM)."
  summary: "The entry cites NCSC-NL as a full 'primary' source (not just corroborating) yet carries only Mozilla's qualitative 'Critical' impact framing in the headline/summary/sourcing_note ('both CVEs carry advisory impact Critical') without disclosing that NCSC-NL's own numeric CVSS scoring for the same two CVEs is MEDIUM severity (4.3/5.4) — a genuine severity discrepancy between the two cited primary sources that the entry does not surface. Does not change priority calibration (notable is still defensible either way) but the contradiction should be surfaced per check 9, not silently resolved in Mozilla's favor."
```
