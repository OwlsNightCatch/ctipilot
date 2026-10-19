**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:49Z · ended_at=2026-10-18T13:57:17Z · duration_seconds=1828

## Retrospective truth pass T3, run 2026-10-18T1307Z-audit

20 entries read whole, 457 ledger claims decided (443 ok, 9 F3, 5 unreadable). 14 clean, 5 imprecision, 1 factual-error.

### 2026-10-12/cve-2026-85097-bricksforge-pro-forms-upload-php-exploited (factual-error)
- **Where:** body paragraph 1; summary; headline; cves[CVE-2026-85097].fixed; Defender takeaway
  - Claim: "The vendor's changelog lists the fix in 4.0.1 / fixed: "release 4.0.1 (vendor changelog); build 3.1.8.10 on the 3.x line (Patchstack)""
  - Defect (factual-error): The vendor changelog's 4.0.1 entry now says CVE-2026-85097 "was fixed earlier in 3.1.8.10 and in 4.0.0" and that 4.0.1 fixes a related, separate upload issue; so 4.0.1 is not the changelog's fix for this CVE and 4.0.0 is a fixed release. The sentence was added after publication (the publication-time body of the page read "Full details will follow once the disclosure process is complete" and did not name the CVE), so the entry was sourced correctly on 2026-10-12 but is wrong against the vendor channel today.
  - Ground truth: 4.0.1, 8 October 2026: "A security issue in the Pro Forms file upload has been fixed. ... Related: CVE-2026-85097, an arbitrary file upload in the same area that was fixed earlier in 3.1.8.10 and in 4.0.0." (4.0.2, 13 October: "The upload check introduced in 4.0.1 could refuse a perfectly normal image") (https://bricksforge.io/version-changelog/)
  - Fix: Correction record: fixed = 3.1.8.10 (3.x line) and 4.0.0; 4.0.1 adds a related upload hardening and 4.0.2 (2026-10-13) corrects a false rejection in it; advise updating to the current 4.x release; reword headline, summary and the vendor-changelog sentence.
- **Where:** Exposure paragraph
  - Claim: "its changelog gives no affected range, so whether 4.0.0 is affected is not stated"
  - Defect (factual-error): The vendor now states the CVE was fixed in 4.0.0, so 4.0.0 is stated as not affected (affected range stays <= 3.1.8.9).
  - Ground truth: "CVE-2026-85097, an arbitrary file upload in the same area that was fixed earlier in 3.1.8.10 and in 4.0.0." (https://bricksforge.io/version-changelog/)
  - Fix: Replace the sentence with the vendor statement that 4.0.0 and 3.1.8.10 carry the fix.
- **Where:** body paragraph 1 and sourcing_note
  - Claim: "Patchstack names 3.1.8.10 as the fixed build of the 3.x line, which the public changelog does not list / "does not list build 3.1.8.10""
  - Defect (imprecision): The public changelog now names 3.1.8.10 (in the 4.0.1 entry).
  - Ground truth: "...was fixed earlier in 3.1.8.10 and in 4.0.0." (https://bricksforge.io/version-changelog/)
  - Fix: Drop the "which the public changelog does not list" clause and the matching sourcing_note sentence.

### 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack (imprecision)
- **Where:** Defender takeaway (and the matching evidence quote use is fine)
  - Claim: "CERT-FR says a factory reset on an unpatched end-of-life unit removes the implant but leaves the device vulnerable and almost certainly compromised again"
  - Defect (imprecision): CERT-FR does not say "implant"; it says a Factory Reset removes "les persistances d'une instance compromise" (the compromised instance's persistence mechanisms).
  - Ground truth: "N'effectuer qu'un Reset Factory est dans ce cas insuffisant, les persistances d'une instance compromise seront supprimées mais l'équipement restera vulnérable et sera certainement de nouveau compromis." (https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)
  - Fix: Replace "removes the implant" with "removes the compromised instance's persistence".

### 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev (imprecision)
- **Where:** cves[CVE-2026-111357].cvss
  - Claim: "cvss: null"
  - Defect (imprecision): The CVE record (MITRE CNA, published 2026-10-15, updated 2026-10-16T18:41Z, i.e. before the entry's 2026-10-17 improvement) carries a CVSS 3.1 base score, so the field should not be null.
  - Ground truth: cvssV3_1 baseScore 7.0, vector CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H (GitHub Advisory Database: "High severity") (https://cveawg.mitre.org/api/cve/CVE-2026-111357)
  - Fix: Set cvss to "7.0 (CVSS 3.1, CVE record)" in an improvement record.
- **Where:** cves[CVE-2026-104935].fixed; summary; Exposure; sourcing_note
  - Claim: "Fixed builds are 25.1.1.2, 25.1.3.1 and 22.8R2.5 (Rapid7 also lists 25.1.3.0, which CERT-FR counts as affected)"
  - Defect (imprecision): Ivanti's own CNA record lists 25.1.3.0 as unaffected ("ICS before version 25.1.3.0"), which settles the Rapid7 vs CERT-FR disagreement in Rapid7's favour; the entry leaves it open and omits 25.1.3.0 from the fixed list (25.1.3.1 as the upgrade target remains safe advice).
  - Ground truth: CNA ivanti affected.versions status "unaffected": 25.1.3.0, 25.1.3.1, 22.8R2.5, 22.7R2.14; description "Authentication bypass by spoofing in ICS before version 25.1.3.0 ... does not impact ICS version 22.7R2.14 or prior" (https://cveawg.mitre.org/api/cve/CVE-2026-104935)
  - Fix: Add 25.1.3.0 to fixed with the Ivanti CVE record as authority and note that CERT-FR's list is the outlier.

### 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day (imprecision)
- **Where:** cves[CVE-2026-102764].status; tags
  - Claim: "status: [exploited, patch-available]"
  - Defect (imprecision): CISA added CVE-2026-102764 to KEV on 2026-10-16 (after the entry's 04:16Z publication); the entry carries no cisa-kev status or tag.
  - Ground truth: KEV catalogVersion 2026.10.16: cveID CVE-2026-102764, "BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability", dateAdded 2026-10-16, dueDate 2026-10-19, forensicTriage Yes (https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
  - Fix: Improvement/update record adding cisa-kev to status and tags and one cited sentence on the listing.

### 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager (imprecision)
- **Where:** cves[CVE-2025-61624].status; tags
  - Claim: "status: [exploited, patch-available, no-patch]"
  - Defect (imprecision): CISA added CVE-2025-61624 to KEV on 2026-10-16 (after the entry's 04:22Z publication); the entry carries no cisa-kev status or tag.
  - Ground truth: KEV catalogVersion 2026.10.16: cveID CVE-2025-61624, "Fortinet Multiple Products Path Traversal Vulnerability", dateAdded 2026-10-16, dueDate 2026-10-19 (https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
  - Fix: Improvement/update record adding cisa-kev to status and tags.

### 2026-10-18/rank-math-seo-pro-3-0-123-malware-supply-chain (imprecision)
- **Where:** frontmatter cves[]
  - Claim: "cves: []"
  - Defect (imprecision): Wordfence, the entry's own corroborating source, carries "CVSS Rating 9.8 (Critical)" for this incident, and the Wordfence Intelligence record linked from that post assigns CVE-2026-111862 ("Rank Math SEO PRO 3.0.123 - Unauthenticated Embedded Malicious Code", published 2026-10-16, updated 2026-10-17, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H, affected 3.0.123, patched 3.0.124). The entry has no CVE record, so scanners and tickets keyed on the id do not match it (the id does not resolve at the CVE services today: 404).
  - Ground truth: Wordfence record: CVE CVE-2026-111862, CVSS 9.8 (Critical), Publicly Published October 16, 2026, Affected 3.0.123, Patched 3.0.124 (https://www.wordfence.com/threat-intel/vulnerabilities/id/81cd7a2c-ad0c-4dbc-b5dc-07ec866d5c1f)
  - Fix: Improvement record adding cves[] CVE-2026-111862 (cvss 9.8 per Wordfence, status patch-available, affected 3.0.123, fixed 3.0.124) with one cited sentence, noting that cve.org does not yet resolve the id.

### Leads decided
- Bricksforge, Previdian evidence quote: not a contiguous passage of the page today, but verbatim in the publication-time snapshot (work/2026-10-12T0256Z-intel/bodies/previdian.md). Page rewritten since publication; noted and left.
- Exchange, evidence quotes "Installation of October 2026 Exchange updates is not required for issues to occur." and "We are investigating this with our Windows partners.": the 15 October banner was replaced on 16 October (blog lastPublishTime 2026-10-17T01:07Z); both sentences are verbatim in the publication-time verifier passages of run 2026-10-16T0256Z-intel. Page edited since publication; noted and left. The two Improvement-section claims that cite the banner are marked unreadable against today's page.

### Unreadable
- ConnectWise advisory (https://www.connectwise.com/company/trust/advisories) returns HTTP 403 on every transport (direct, trafilatura, jina, WebFetch); claims 00652d1a93, 6b82ce3674, cb3c9f7ee1 rest on it alone. Prior-iteration passages quote the page; all other claims of that entry verify against Huntress, Todyl and BleepingComputer.
