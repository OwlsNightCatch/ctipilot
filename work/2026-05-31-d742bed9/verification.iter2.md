**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-31T04:47:07Z · ended_at=2026-05-31T04:49:46Z · duration_seconds=159
**Self-telemetry:** urls_checked=18 · webfetch_calls=14 · bridge_fetches=1

## Verification report — briefs/2026-05-31.md (iteration 2)

---

### Prior-iteration delta verification (F3 OAG date fix)

The California OAG press release at `https://oag.ca.gov/news/press-releases/attorney-general-bonta-sues-chrome-holding-co-formerly-known-23andme-over-2023` was fetched. The page clearly states "Thursday, May 28, 2026" as the publication/filing date. The remediation applied in iteration 1 — changing prose to "announced suit ... on 2026-05-28" and the citation label to "[California OAG, 2026-05-28]" — is **correct**.

Corroboration of figures:
- "~6.9M / 855,541 Californians" — OAG page confirms "nearly 7 million users, including 855,541 Californians". BleepingComputer states "approximately 6.9 million customers, including 855,541 Californians." Brief's figures are accurate.
- "DNA-Relatives bulk-enumeration coding error" — OAG page confirms "coding vulnerability in the 'DNA Relatives' feature." The Register confirms "cascaded to expose millions due to genetic relationship connections." Accurate.
- "~14,000 credential-stuffed accounts" — The Register confirms "credential-stuffing attacks on roughly 14,000 accounts." Accurate.
- "ransom-payment allegation (attributed to the AG complaint, not stated as fact)" — The Register confirms "investigators discovered the company negotiated ransom payments with threat actor 'Golem' in exchange for removing posted breach information." Brief uses "additionally alleges ... negotiated and paid a ransom" — correctly attributed as allegation, not fact. Accurate.

Prior-iteration F3 remediation: **VERIFIED CORRECT**.

---

### Broken / unreachable URLs

No broken URLs detected across all fetched sources. All URLs resolve successfully to specific article/advisory pages, not homepages or listing indexes.

---

### Generic / oversight URLs (replace with specific article)

No generic or oversight URLs detected.

---

### Citation does not support the claim

**F3-a — Mautic § 1: The brief materially understates the severity of CVE-2026-9558 and CVE-2026-9559 by characterizing both as less than RCE-class.**

The brief states: "The remaining five (CVE-2026-9558, CVE-2026-9559, CVE-2026-9808, CVE-2026-9809, CVE-2026-9811) cover stored XSS executing in another user's browser, file inclusion / path traversal allowing manipulation of files outside intended directories, and JavaScript code injection."

However, the cited GHSA sources (fetched in this iteration) state:

- **CVE-2026-9558** (GHSA-9fx4-7cmj-47vg): Server-Side Template Injection (SSTI) in Theme Templates — "authenticated users with theme creation permissions can exploit this to execute arbitrary code on the server." This is **RCE**, not stored XSS. Severity is Critical/High.
- **CVE-2026-9559** (GHSA-6r9h-4h75-7q4x): Path traversal via campaign import — "allows authenticated users with import privileges to write arbitrary PHP files to sensitive system directories ... enables remote code execution under the web server user context." This is **PHP RCE**, not merely "manipulation of files outside intended directories."
- **CVE-2026-9808** (GHSA-2jrw-c95w-h43g): Authorization bypass in API v2 endpoints — "allows authenticated users with limited roles to bypass owner-scope restrictions" to "access or modify resources belonging to other users." This is an **authorization bypass**, not characterised anywhere as XSS or file inclusion. The brief does not mention authorization bypass at all among the five.
- CVE-2026-9809 and CVE-2026-9811 are correctly described as stored XSS.

The brief groups CVE-2026-9558 (SSTI/RCE) into the "stored XSS" bucket, calls CVE-2026-9559 (PHP RCE) mere "file inclusion / path traversal", and omits the authorization-bypass class entirely for CVE-2026-9808. This means two RCE-class findings and one authorization-bypass are misrepresented or absent from the brief's cluster description. For a Tier 2/3 IR audience triaging patch priority, this mischaracterization matters — SSTI and path-traversal-to-PHP-RCE are higher priority than stored XSS. **Truth-class defect.**

**Specific text to correct:** Replace "The remaining five (CVE-2026-9558, CVE-2026-9559, CVE-2026-9808, CVE-2026-9809, CVE-2026-9811) cover stored XSS executing in another user's browser, file inclusion / path traversal allowing manipulation of files outside intended directories, and JavaScript code injection." with an accurate breakdown: CVE-2026-9558 = SSTI (arbitrary server-side code execution in theme templates); CVE-2026-9559 = path traversal enabling PHP RCE via campaign import (Mautic 7 only); CVE-2026-9808 = authorization bypass in API v2 endpoints (Mautic 7 only); CVE-2026-9809 / CVE-2026-9811 = stored XSS in Projects component (Mautic 7 only). Note: CVE-2026-9559, CVE-2026-9808, CVE-2026-9809, CVE-2026-9811 affect only Mautic 7.x; CVE-2026-9558 and CVE-2026-9557 and CVE-2026-4776 affect all supported branches.

---

### Unsupported / hallucinated facts

No hallucinated facts detected. All named entities (CVEs, victim numbers, actor names, platform names, dates) were verified against at least one fetched source.

One clarification: the brief uses "JavaScript code injection" as a descriptor for the XSS cluster — this is not a GHSA term but is a reasonable lay synonym for stored XSS; not flagging as hallucination but noting the imprecision.

---

### Claims missing inline citation

No uncited claims found.

---

### Strengthen primary source

No NVD/CERT-only sourcing detected. The primary sources are: BSI CERT-Bund (national regulator advisory, qualifies as first-tier for its own jurisdiction) + Mautic GHSA; TechCrunch + Malwarebytes; California OAG + BleepingComputer + The Register; Cisco Talos primary research blog. All are acceptable.

F11 advisory from iter1 (Mautic footer CVSS: n/a × 7) stands — the BSI advisory is a JS SPA that does not render CVSS scores, and per-CVE GHSA scores vary. This is correctly marked as honest. No new information changes this judgment.

---

### Drop (low relevance / off-audience / not weekly content)

No items warrant dropping. All three § 1 items and the § 3 item are CH/EU/public-sector relevant with clear defender actions.

---

### Needs more research

No items flagged. The brief accurately notes the Talos DICOM study defers exploit-level detail to a non-public PDF; the brief's § 5 correctly declines to fabricate depth.

---

### Surface contradiction

No contradictions surfaced between sources covering the same item.

---

### Missed angles

**F10-a (advisory):** The brief covers Gitea CVE-2026-27771 in § 7 as a forward-rolled candidate but the § 1 Mautic cluster's CVE-2026-9559 (path traversal / PHP RCE) only affects Mautic 7.x. A brief mention of which version branch is affected (7.x vs. 6.x vs. all) would help operators running Mautic 6 understand their actual risk surface — but this overlaps with F3-a above. Suggested search query for future runs: `Mautic CVE-2026-9559 exploitation 7.x campaign import RCE`.

---

### Editorial / less-is-more flags (advisory)

**F11-a (advisory — no change required):** Mautic footer lists CVSS: n/a × 7. Iter1 judged this honest; this iteration concurs. The GHSA scores retrieved range from CVSS 5.4 (CVE-2026-9811) to 7.6 (CVE-2026-4776 / CVE-2026-9809). The n/a is likely because the main agent was working from the BSI advisory (JS SPA, no CVSS rendered) and the single fetched GHSA (GHSA-fcmw-wx57-9p75, CVE-2026-4776) rather than all seven advisories. This advisory observation is not blocking.

---

### Single-source items missing [SINGLE-SOURCE] flag

§ 3 Cisco Talos DICOM/Orthanc is correctly flagged `[SINGLE-SOURCE]` in the H3 heading and § 7. No drift found.

---

### Analytical-link-as-fact

No analytical-link-as-fact defects detected. The 23andMe item correctly attributes the ransom-payment allegation to the AG complaint ("The AG additionally alleges"). The brief does not assert unattributed connections.

---

### Quantifier without source

No unsupported quantifiers detected. All numeric claims (6.9M, 855,541, 14,000, 7 CVEs) are supported by fetched sources.

---

### Name-collision unflagged

The check_brief.py flagged a `name-collision` WARN: "Mautic 7.1.2 / 6.0.9 — seven authenticated flaws..." shares name "GitHub" with prior coverage. This is a script false positive — "GitHub" is the hosting platform for the GHSA advisory, not a threat actor or campaign codename. The entity "GitHub" in prior coverage and in this brief refer to the same platform. No attacker/defender inversion. **Warn is benign; no F15 finding.**

---

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)**

**F3-a is the sole truth finding:** The brief's description of the "remaining five" CVEs in the Mautic cluster materially understates CVE-2026-9558 (SSTI/RCE) as "stored XSS", understates CVE-2026-9559 (PHP RCE) as "file inclusion / path traversal allowing manipulation of files outside intended directories", and omits the authorization-bypass class for CVE-2026-9808 entirely. For a patch-triage audience, misclassifying RCE-class vulns as XSS is a material defect. The fix is narrow: replace the "remaining five" sentence with an accurate per-CVE breakdown.

F11-a (Mautic CVSS n/a × 7) remains advisory only — the main agent can add available CVSS scores from the fetched GHSAs if desired but it does not block CLEAN.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Mautic 7.1.2 / 6.0.9 — seven authenticated flaws"
  url_or_quote: "The remaining five (CVE-2026-9558, CVE-2026-9559, CVE-2026-9808, CVE-2026-9809, CVE-2026-9811) cover stored XSS executing in another user's browser, file inclusion / path traversal allowing manipulation of files outside intended directories, and JavaScript code injection."
  summary: "GHSA-9fx4-7cmj-47vg (CVE-2026-9558) describes SSTI with arbitrary server-side code execution (RCE), not stored XSS. GHSA-6r9h-4h75-7q4x (CVE-2026-9559) describes path traversal enabling PHP RCE via campaign import, not merely file manipulation. GHSA-2jrw-c95w-h43g (CVE-2026-9808) describes an authorization bypass, a class entirely absent from the brief's description of the five. Fix: replace the 'remaining five' sentence with accurate per-CVE descriptions: CVE-2026-9558=SSTI/RCE (theme templates, all branches); CVE-2026-9559=path-traversal/PHP-RCE (campaign import, Mautic 7 only); CVE-2026-9808=authorization bypass in API v2 (Mautic 7 only); CVE-2026-9809/CVE-2026-9811=stored XSS in Projects (Mautic 7 only)."
```
