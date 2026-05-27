**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-27T05:06:44Z · ended_at=2026-05-27T05:09:55Z · duration_seconds=191

## Verification report — briefs/2026-05-27.md (iteration 4)

### Prior-iteration delta verification

**F14 (iter-3) — Elastic "first" superlative**: Confirmed remediated. The § 5 Background paragraph now reads "a detailed detection-engineering treatment of the kit's current operator architecture" — the word "first" is absent. The Elastic article (fetched this iteration) makes no "first/first-ever" claim for detection-engineering treatment; it only says "First observed in August 2023" for the kit itself. Remediation is correct and clean.

**F3 (iter-3) — 7-Eleven "franchise applicants"**: Partially remediated. "franchise applicant" / "franchise-applicant" phrasing no longer appears in the brief (confirmed by grep). The body now says "job/recruitment applicants" and the TL;DR says "job-applicant records." However, a new discrepancy surfaces (see F9 below): the BleepingComputer 7-Eleven article actually describes the affected individuals as "franchisee document holders" — not "job applicants" — and does not mention SSNs or driver's licences. The CyberInsider article does describe "job applicants" with SSNs. The two cited sources give conflicting descriptions of the victim population. The iter-3 remediation moved from one inaccuracy (franchise-applicant) to a partial inaccuracy (job-applicant is supported by CyberInsider but contradicted by BleepingComputer).

**Re-confirmations (items cleared in prior iterations):**
- Mini Shai-Hulud § 4 UPDATE: No French-victim-confirmation claim in the UPDATE body text itself. However, see F9 below — the CERT-FR bulletin text does assert ANSSI awareness of French victims, which creates a tension with the § 7 note.
- Package list (@tanstack/*, @squawk/*, @antv, @mistralai/mistralai, guardrails-ai, lightning): Confirmed matching CERTFR-2026-ACT-023 as fetched this iteration. The bulletin lists exactly these packages (plus some additional cap-js packages in the April wave).
- CVE-2026-9312 ENISA EUVD source: URL returns HTTP 200 (confirmed in url-liveness.tsv); page is a JavaScript SPA that WebFetch cannot render. Cannot verify content independently — not a broken URL finding.
- GitHub Enterprise Server release notes URL: HTTP 200 (url-liveness.tsv); similarly JS-rendered and unverifiable via WebFetch. Not a broken URL finding.
- CVE-2026-9642 Tenable TRA-2026-44: Fetched and confirmed. Tenable Research advisory exists, covers Delta Electronics DIAView V4.4, CVE-2026-9642 is a patch bypass for CVE-2025-62582, CVSS 9.8, no patch as of 2026-05-26. All brief claims confirmed against source.
- Nimbus Manticore Check Point Research source: Fetched and confirmed. Check Point article (2026-05-22) covers MiniFast, Zoom scheduled-task hijacking, SEO poisoning, AppDomain hijacking, two SSL.com code-signing certificates (Gray Matter Software S.R.L. and Kirubel Kerie Negeya). No Security Affairs URL present in brief. Confirmed clean.

---

### Citation does not support the claim

**F3-A — TL;DR line: SSN/driver's-licence claim attached to wrong BleepingComputer URL**

The TL;DR bullet (line 10) states: "7-Eleven confirmed roughly 185,000 job-applicant records including SSNs and driver's licences; both trace to the vishing → Entra → Salesforce-Aura pattern ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/))."

The URL cited here is the *Charter* BleepingComputer article, not the 7-Eleven article. The Charter article makes no mention of 7-Eleven, SSNs, or driver's licences. Separately, the 7-Eleven BleepingComputer article (`bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/`) describes the 185,300 affected individuals as "franchisee document holders" and lists data exposed as "names, dates of birth, email addresses, phone numbers, and physical addresses" — with no mention of SSNs or driver's licences.

The SSN and driver's-licence detail is supported only by CyberInsider (`cyberinsider.com/7-eleven-data-breach-exposes-personal-information-of-185000-applicants/`), which also uses the "job applicants" framing. Both BleepingComputer sources (Charter and 7-Eleven) do NOT support the SSN/driver's-licence claim.

In § 4 the inline citation for these details reads: "([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/7-eleven-data-breach-exposes-personal-information-of-185-000-people/); [CyberInsider, 2026-05-26](https://cyberinsider.com/7-eleven-data-breach-exposes-personal-information-of-185000-applicants/))". The § 4 attribution is acceptable because CyberInsider does support the claim. But in the TL;DR, only the Charter BleepingComputer URL appears, which neither covers 7-Eleven nor mentions SSNs.

**Action needed:** TL;DR bullet should add the CyberInsider 7-Eleven URL as the citation for the SSN/driver's-licence claim, or the § 4 citation pattern should be replicated inline.

---

### Surface contradiction

**F9 — CERT-FR bulletin states French victims exist; § 4 UPDATE and § 7 Verification Notes say "does not name a confirmed French victim"**

The § 4 UPDATE body states: "The bulletin issues detection and remediation recommendations (search developer/CI environments for the listed packages); it does not name a confirmed French victim."

The § 7 Verification Notes state: "the UPDATE reports the bulletin's widened package scope, source-code-leak note and remediation guidance — not a French victim confirmation (the bulletin does not name one)."

However, the CERTFR-2026-ACT-023 bulletin text (fetched this iteration, line 664 of the HTML source) explicitly states:

> "L'ANSSI a connaissance de plusieurs victimes françaises actuellement affectées par cette campagne."

Translation: "ANSSI is aware of several French victims currently affected by this campaign."

The bulletin IS asserting that French victims are affected by the campaign. The § 4 UPDATE text and § 7 note that "does not name a confirmed French victim" are technically accurate (no specific organisation names are given), but the phrasing in context reads as if the bulletin is silent on French victims, when in fact it explicitly says the opposite. A Tier-2 reader acting on this brief would miss that ANSSI confirms French victims.

**Action needed:** Add a `Contradiction:` note to § 7 Verification Notes stating that while the bulletin does not name specific victims, it does explicitly state ANSSI is aware of several French victims currently affected. The § 4 UPDATE body could add: "The bulletin notes that ANSSI is aware of several French victims currently affected by this campaign but does not name them individually."

---

### Missed angles

**F10 — 7-Eleven victim-population discrepancy unresolved between two cited sources**

BleepingComputer describes the 185,000 individuals as "franchisee document holders" whose data (names, DOBs, emails, phones, addresses) was exposed; the article makes no mention of SSNs or driver's licences. CyberInsider describes them as "job/recruitment applicants" with SSNs and driver's licence numbers. These are materially different characterisations of the same incident. The current brief (post iter-3 remediation) adopts the CyberInsider framing throughout but does not surface the discrepancy. Neither source can be dismissed — BleepingComputer is a primary breach-journalism outlet and its framing (franchisee documents, no SSNs) may reflect different subset of the disclosed data.

**Suggested search query:** `7-Eleven 185000 breach notification letter SSN driver licence franchise applicant 2026` — to locate the breach notification letter or 7-Eleven's official statement for the authoritative victim and data-field description. If the notification letter cannot be located, the brief should note "sources differ on victim population description (job applicants per CyberInsider; franchisee document holders per BleepingComputer)" and qualify the SSN/driver's-licence detail to CyberInsider only.

---

### Editorial / less-is-more flags (advisory)

**F11-A — EUVD and GitHub release notes URLs are JavaScript SPAs; content unverifiable**

Both `https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-32027` and `https://docs.github.com/en/enterprise-server@3.21/admin/release-notes#3.21.1` return HTTP 200 (per url-liveness.tsv at 04:16 UTC) but render content via JavaScript that WebFetch cannot parse — only a generic page header is visible. The underlying content may be fully accurate; this is not a broken-URL finding. Advisory note: the main agent should verify GHES patch version list (3.16.20 / 3.17.17 / 3.18.11 / 3.19.8 / 3.20.4 / 3.21.1) and CVSS 9.2 against a source that can be independently read — e.g. the GitHub GHSA advisory at `https://github.com/advisories/GHSA-fwfp-h68w-2hcr` which is a static HTML page.

---

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 1)

- F3-A: Truth — TL;DR bullet cites only the Charter BleepingComputer URL for the 7-Eleven SSN/driver's-licence claim; that URL does not support the claim. CyberInsider needs to be cited inline in the TL;DR for these specific details, or the § 4 citation pattern repeated.
- F9: Editorial — Brief characterises CERT-FR bulletin as not confirming French victims; the bulletin explicitly states ANSSI is aware of several French victims. § 4 UPDATE body and § 7 Verification Notes need correction.
- F11-A: Advisory — EUVD and GHES release-notes URLs are JS-rendered; content unverifiable via WebFetch. Main agent should verify patch-version list via GHSA-fwfp-h68w-2hcr.

F10 is an advisory-level missed angle; the main agent may add a contradiction note rather than fully rewriting the victim description, since CyberInsider (a cited source) does support the current phrasing.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: tl-dr
  item: "ShinyHunters Salesforce extortion — two fresh victim confirmations"
  url_or_quote: "7-Eleven confirmed roughly 185,000 job-applicant records including SSNs and driver's licences; both trace to the vishing → Entra → Salesforce-Aura pattern ([BleepingComputer, 2026-05-26](https://www.bleepingcomputer.com/news/security/charter-confirms-data-breach-after-shinyhunters-extortion-threat/))"
  summary: "The cited BleepingComputer URL is the Charter article; it says nothing about 7-Eleven, SSNs, or driver's licences. The 7-Eleven BleepingComputer article (separate URL) describes victims as 'franchisee document holders' with no SSN/DL data. SSN/driver's-licence detail is supported only by CyberInsider. TL;DR needs the CyberInsider 7-Eleven URL cited inline for the SSN/DL claim."
- code: F9
  category: surface-contradiction
  section: "§ 4 UPDATE Mini Shai-Hulud + § 7 Verification Notes"
  item: "UPDATE: Mini Shai-Hulud (TeamPCP) — CERT-FR bulletin widens affected-package scope"
  url_or_quote: "it does not name a confirmed French victim (§4); the bulletin does not name one (§7)"
  summary: "CERTFR-2026-ACT-023 (fetched this iteration) explicitly states 'L'ANSSI a connaissance de plusieurs victimes françaises actuellement affectées par cette campagne' — ANSSI is aware of several French victims. The brief implies the bulletin is silent on French victims, which is incorrect. §4 UPDATE body and §7 should note that ANSSI confirms French victims exist (unnamed)."
- code: F11
  category: editorial-advisory
  section: "§ 2 CVE-2026-9312"
  item: "CVE-2026-9312 — GitHub Enterprise Server release notes URL"
  url_or_quote: "https://docs.github.com/en/enterprise-server@3.21/admin/release-notes#3.21.1"
  summary: "Advisory only: URL returns HTTP 200 but is a JS-rendered SPA; patch version list (3.16.20/3.17.17/3.18.11/3.19.8/3.20.4/3.21.1) and CVSS 9.2 cannot be verified via WebFetch. Recommend verifying against https://github.com/advisories/GHSA-fwfp-h68w-2hcr (static HTML)."
```
