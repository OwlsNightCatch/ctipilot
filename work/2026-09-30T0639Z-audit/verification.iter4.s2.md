**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-01T04:40:29Z · ended_at=2026-10-01T05:04:32Z · duration_seconds=1443

## Verification report — 2026-09-30T0639Z-audit (iteration 4, slice s2)

Scope: 20 entries of scope.iter1.s2.txt, all 456 ledger claims in claims.iter4.s2.yaml walked (verdict rows in verification.iter4.s2.claims.yaml: 452 ok, 3 F3, 1 F4). Every cited page was fetched this iteration (cached bodies for the Securelist, SentinelOne, JFrog and Google GHSA pages), the Oracle risk matrix was parsed programmatically (50 qualifying rows, all 50 cves[] records compared to the matrix), the KEV feed was read from work/2026-09-30T0639Z-audit/kev.json, EPSS values were re-read for the dated queries.

### Iteration-3 delta walk (remediation log, slice s2)
- JFrog F4 #1 (Correction vs takeaway): fixed. Correction, immediate_action, actions[0] and the Defender takeaway now agree: 7.133.11 or later closes CVE-2026-42016 (JFrog table: "< 7.133.11", patched 7.133.11), the CVE-2026-42018 fix for the target branch is a separate requirement (JFrog 7.133.28 inclusive range, Wiz 7.133.29), and Wiz says "Neither vulnerability grants administrative control on its own".
- JFrog F4 #2 (HTTP 200): fixed. Wiz: "returned HTTP 200" for both requests in "Every exploitation". immediate_action and the Correction carry the same condition. actions[1] still says "Where found, treat the instance as compromised" without the 200 condition; harmless (more conservative).
- Oracle F14 (five): fixed. Matrix: CVSS 10.0 rows for Access Manager, Forms, Internet Directory, Platform Security for Java, WebLogic Server (5) plus Hyperion Financial Management (6 total).
- Virtualizor tag/summary: fixed. VulnCheck "This is not precondition-free"; summary states the suspended in-house-billing account precondition.
- F3 date labels (RHSB 2026-07-03, Cyberattaque.org / FrenchBreaches 2026-09-19): decline accepted. RHSB shows "Public Date May 7, 2026 / Updated July 3, 2026"; FrenchBreaches carries "Mise a jour le samedi 19 septembre" containing the AFPA confirmation; Cyberattaque.org carries the same confirmation. The as-of date is defensible; the rationale is no longer recorded in the AFPA sourcing note.
- NCSC-CH F5 (uncited tail): citation added, but see F3 below: one sentence's advice is not BACS's.
- Oracle F11 (summary): fixed, reads cleanly and matches the matrix (6 at 10.0, 44 at 9.8).
- Virtualizor subject shift: fixed.
- Cisco Nexus record summary: fixed (names takeaway rewrite).
- AEPD / Pentagon F11: NOT fully fixed, the remediation log is wrong that the bodies no longer carry the wording (see F11 below).

### Citation does not support the claim
- #1 (F3, low confidence) cve-2026-46300, Update 2026-09-05: "...from process logs alone ([Microsoft Security Blog, 2026-05-08])". Microsoft: "may be indicative of techniques associated with either 'Dirty Frag' or 'Copy Fail'". "Process logs alone" is Aikido's phrase. Drop or re-cite.
- #2 (F3, low confidence) jfrog-artifactory-cve-2026-42016-42018: "(a default-configuration join-key bypass, disclosed 28 August 2026)" cited to Wiz. Wiz: "critical authentication-bypass vulnerability ... under its default configuration"; no join-key bypass wording (join key appears only as post-exploitation theft). Claim 2e309341ea.
- #3 (F3, low confidence) ncsc-ch-google-recovery: "audit and restrict app-password issuance on any Google account, and treat an app-password creation event with the same sensitivity as a new OAuth grant" cited to BACS. BACS recommends deleting all App-Passwoerter entries and checking recovery addresses and forwarding rules; neither "restrict issuance" nor the OAuth-grant equivalence is there. Claim 5db9d59dca.

### Unsupported / hallucinated facts
- #4 (F4, low confidence) nighteagle: "Initial access used compromised VPN credentials". Securelist: "In most incidents, the attackers used compromised valid credentials to gain access to corporate VPNs". Hedge dropped. Claim d91abae3a4.

### Editorial / less-is-more flags (advisory)
- #5 (F11) "the constituency" in reader-facing text: AEPD body ("The relevance for the constituency is the policy signal"), Push Security body ("home-region infrastructure the constituency's users may encounter"), and four record summaries written this run (gtig, conference-phishing, tradertraitor, virtualizor). gtig and node-ipc record summaries also say "source rating".
- #6 (F11) pentagon body: "Its relevance is sectoral: ..." not one of the four grounds; remediation log says it was removed, it was not.

### Checked and clean (no finding)
Style: no em dash in text added by this run (only the "## Correction — <at>" headings; remaining em dashes are in earlier-run text or verbatim quotes), no KEV deadline used as a reason to act, no IOC values (Arista artifact paths, hashes, IPs and the header name are described, not listed). Priority moves this run (GTIG, Oracle, Virtualizor, conference-phishing, TraderTraitor, NightEagle, Push, Mandiant to notable; AEPD, AFPA, Pentagon to routine) are consistent with the sources (no exploitation or no Swiss nexus). Evidence quotes spot-checked verbatim on all 20 entries, translated quotes (AEPD, AFPA, NCSC-CH) checked against their original: fields. CVE ids and scores: Oracle 50/50 against the matrix; CVE-2026-93952 10.0/9.5 against Arista; CVE-2026-46300 7.8 against Red Hat; KEV dates for CVE-2026-32202, 42016, 42018, 93952, 2020-0688, 2019-0708 against kev.json. EPSS 0.0948 / above 0.92 (cve-2026-46300) and 0.0027 / 0.0035 (JFrog) confirmed with dated queries (2026-09-04, 2026-09-10).
Missed angles (check 13): not assessed for this correction slice; no gap surfaced.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 0, advisory: 2)

### Findings summary (machine-readable)
See verification.iter4.s2.findings.yaml.
