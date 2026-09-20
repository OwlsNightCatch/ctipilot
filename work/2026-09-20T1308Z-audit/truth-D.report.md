**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T13:11:23Z · ended_at=2026-09-20T13:17:19Z

## Truth pass — batch D — 2026-09-20T1308Z-audit

Entry: `entries/2026-09-09/windows-september-2026-two-exploited-lpe-zero-days-kev.md`

### Method
- Fetched both MSRC per-CVE records via the SUG OData bridge (`msrc cve CVE-2026-81963`, `msrc cve CVE-2026-85880`) and the full September 2026 CVRF document (`msrc cvrf 2026-Sep`) for the authoritative ProductStatuses/ProductTree affected-build lists and remediation KBs.
- Fetched the live CISA KEV catalog (`fetch_source.py cisa-kev`) and cross-checked both CVE IDs.
- Fetched the CISA alert page (`fetch_source.py cisa page ...`) — specific advisory, not a listing/index.
- Fetched BleepingComputer and Zero Day Initiative articles via `fetch_source.py extract` and grepped both cited evidence[] quotes as literal substrings.
- Diffed the correction commit (`git show fb163a3 -- <path>`) against the prior state to verify the changelog contract.
- Grepped `attack/enterprise-attack.json` for T1068 (active, not revoked, tactic privilege-escalation) — matches the described SYSTEM-elevation behavior.

### 1. CVEs and CVSS against MSRC per-CVE authority
- CVE-2026-81963: MSRC baseScore **7.8**, severity Important, `exploited: Yes`, description matches evidence[] quote verbatim, vectorString `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:F/RL:O/RC:C` — confirms the body's "functional exploit (E:F)" claim. Affected products per CVRF ProductStatuses: Windows Server 2025 + Windows 11 23H2/24H2/25H2/26H1 (ARM64+x64) — exact match to `cves[0].affected`.
- CVE-2026-85880: MSRC baseScore **7.8**, severity Important, `exploited: Yes`, description and FAQ text match the entry's evidence[] quote verbatim. Affected products per CVRF: Windows 10 1607/1809/21H2/22H2 + Windows Server 2012/2012 R2/2016/2019/2022, explicitly excluding Windows 11 / Server 2025 — exact match to `cves[1].affected`, but see F3 finding below on the citation used for this fact in the body.
- Both CVSS scores in frontmatter (7.8/7.8) and `status: [exploited, cisa-kev, patch-available]` hold.

### 2. Total-count claim
- BleepingComputer states verbatim: "security updates released for a **record-breaking 966 flaws**" — matches entry's corrected "966" figure exactly (both in frontmatter `summary` and body).
- Zero Day Initiative's opening line states verbatim: "With **nearly 1,000 CVEs** coming out from Microsoft" — matches the Correction section's quote exactly. (Elsewhere in the same ZDI post the author separately tallies "972 new CVEs" / "997" total using a different counting methodology than BleepingComputer's Patch-Tuesday-day-only count of 966; this is a benign methodology difference between the two outlets, not a contradiction the entry needs to surface, since the entry only ever cites BleepingComputer for the "966" figure it uses.)
- No per-category counts are asserted in the entry, so nothing to check there.

### 3. KEV listing
- Live CISA KEV catalog (pulled 2026-09-20, `catalogVersion 2026.09.18`) lists both:
  - CVE-2026-81963, `dateAdded: 2026-09-08`, "Microsoft Windows Update Stack contains a link following vulnerability that allows a local attacker to escalate privileges locally up to SYSTEM."
  - CVE-2026-85880, `dateAdded: 2026-09-08`, "...heap-based buffer overflow vulnerability that allows an attacker to elevate privileges locally."
  Both match the entry's "CISA added both to its Known Exploited Vulnerabilities catalog on 2026-09-08" claim and `status: cisa-kev`.
- The cited CISA alert page (`.../cisa-adds-four-known-exploited-vulnerabilities-catalog`) is a specific advisory (not a listing/index) and names both CVE IDs among the four added that day.

### 4. Correction section
- Diffing the 2026-09-13 audit commit against the pre-correction state confirms: the only prior defect was the unsupported "roughly 1,170" total-count figure, cited (pre-correction) only to MSRC + ZDI — neither of which states that number. The correction (a) changed `summary` and the body's leading sentence to "966," (b) moved the citation for that clause onto BleepingComputer (which does state 966), and (c) declared `fields: [summary, body]` — matching exactly what changed; no silent edit. `updated_at` correctly stayed `null` (type: correction, per the no-refloat rule). `discovered_at`, `run_id`, and the path are untouched. The corrected figure is right, and the `updates[].summary` matches the section's content and scope exactly ("no more, no less"). Main analysis does not contradict frontmatter post-correction.

### 5. Evidence[] quotes — literal substring check
- All three evidence[] quotes (MSRC CVE-2026-81963 description, MSRC CVE-2026-85880 FAQ, ZDI CVE-2026-81963 commentary) confirmed as exact, contiguous substrings of the fetched source bodies (grep -F / Python `in` check).

### 6. techniques[]
- T1068 ("Exploitation for Privilege Escalation") confirmed active (`"revoked": false`, `"deprecated": false`) in the pinned `attack/enterprise-attack.json`, tactic `privilege-escalation`. Body describes exactly this behavior (foothold-to-SYSTEM escalation via local vulnerability exploitation) without dumping the ID into prose — compliant.

### 7. Classification / IOCs / source patterns / em dashes
- `classification: {reliability: A, credibility: 1}` — reliability A is justified (two vendor-PSIRT/government primaries: MSRC ×2, CISA); credibility 1 ("confirmed by other independent sources") is justified given four independent corroborating sources (MSRC, CISA, ZDI, BleepingComputer) agreeing on every material fact.
- No IOCs anywhere in the entry.
- All five `sources[]` URLs are specific advisory/article pages — no homepage, listing, or NVD/MITRE per-CVE pattern.
- Two em dashes found in reader-facing (site-rendered) text: `cves[0].affected` ("... — the newest generation") and `cves[1].affected` ("... — the legacy/long-support line only..."). The `## Correction — <at>` heading also contains an em dash but that is the pipeline's own mandated header syntax, not a style defect. Flagged as a low-severity style note only.

### Findings (both citation-adjacency / misattribution, not factual errors)
1. Main body, CVE-2026-85880 sentence: the affected-build clause ("Windows 10 and Windows Server 2012 through 2022, and not Windows 11 or Server 2025") is cited to BleepingComputer, but BleepingComputer's CVE-2026-85880 section (verified by full-text read) contains only the title, the MSRC description quote, and researcher credits — no version/build breakdown. The fact is true (confirmed via Microsoft's own CVRF ProductStatuses) but is the wrong source's citation; MSRC's per-CVE record is the correct citation.
2. Main body, second paragraph: the parenthetical "(its own Threat Intelligence Center with Romain Deperne for the Update Stack bug; Volexity and Proofpoint for the ALPC bug)" sits in a sentence whose sole citation is the ZDI blog post. Full-text search of the fetched ZDI post shows zero mentions of Volexity, Proofpoint, Deperne, or MSTIC/"Threat Intelligence Center." Those exact researcher-credit facts are stated verbatim by BleepingComputer instead (cited earlier in the same paragraph, but not for this clause).

### Verdict: imprecision (no factual errors found)

Every named CVE ID, CVSS score, affected-build list, exploitation/KEV status, evidence[] quote, and the correction's own claims check out true against Microsoft's per-CVE authority, the live CISA KEV catalog, and the two corroborating outlets. The two defects found are citation-attribution slips (true facts pinned to a citation that does not carry them) rather than wrong facts, plus a minor em-dash style note in reader-facing frontmatter fields.
