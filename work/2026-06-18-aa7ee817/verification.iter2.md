**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-18T04:44:55Z · ended_at=2026-06-18T04:49:58Z · duration_seconds=303

## Verification report — briefs/2026-06-18.md (iteration 2)

---

## Prior-iteration delta walkthrough (iter 1, Opus, NEEDS_FIXES truth=3 editorial=0 advisory=4)

**F3 — CVE-2026-21962 removal:** CONFIRMED CLEAN. Grep of brief returns zero matches for CVE-2026-21962. The item does not appear anywhere in the document.

**F3 — Oracle CVE table sourcing (CVE-2026-46978 / CVE-2026-35278 → Oracle advisory):** CONFIRMED CLEAN. Oracle CSPU bridge fetch confirms both CVEs are present in https://www.oracle.com/security-alerts/cspujun2026.html: CVE-2026-35278 is in the PeopleSoft Risk Matrix under "PeopleSoft Enterprise PT PeopleTools / Performance Monitor"; CVE-2026-46978 is in the Solaris Risk Matrix under "Oracle Solaris / Oracle Solaris". CVE Summary Table Source cells point to the Oracle advisory. CORRECT.

**F4 — Mastra deep dive (ehindero / offboarding-root-cause):** CONFIRMED CLEAN. The name "ehindero" does not appear anywhere in the brief. The deep dive § 5 explicitly states: "the cited primaries (JFrog, Socket) document the result but do **not** disclose how the publishing account was obtained, so the brief makes no claim about the initial-access vector." The word "offboarding" appears once, in § 6 Action Items as a general npm hygiene recommendation ("automate publish-access revocation on contributor offboarding") — this is not an access-vector claim and is independently supportable npm security guidance. JFrog confirms the two-stage loader architecture, 88-minute sweep, postinstall hook, NVM-masquerading persistence, and C2 pattern. Socket confirms 140+ packages, timeline, and the ehindero/sergey2016 account names (though the mechanism of account compromise is not disclosed by either source). CORRECT.

**F9 — FortiBleed sourcing precision:** CONFIRMED CLEAN. BleepingComputer fetch confirms: Russian-speaking multi-operator threat group mentioned, and "lateral movement into Active Directory environments" by threat actors confirmed. Arctic Wolf fetch confirms: 194 countries mentioned explicitly; SHA-256→PBKDF2 hash migration detail present (FortiOS 7.2.11, 7.4.8, 7.6.1). Brief now attributes Russian-actor/AD-lateral to BleepingComputer and 194-country reach to Arctic Wolf. The SHA-256→PBKDF2 detail is carried by Arctic Wolf and the brief does not cite it as a fact — § 7 correctly notes Arctic Wolf carries it. CORRECT.

---

## Full cold-read findings

### Citation does not support the claim

**F1 — § 3 JetBrains item: "JetBrains has pulled the plugins"**

The brief states (§ 3): "JetBrains has pulled the plugins."

Neither cited source supports this claim:
- Aikido Security (https://www.aikido.dev/blog/multiple-jetbrains-ide-plugins-caught-stealing-ai-keys): does not mention JetBrains removing the plugins.
- Infosecurity Magazine (https://www.infosecurity-magazine.com/news/fifteen-jetbrains-marketplace/): does not confirm plugin removal.

BleepingComputer (https://www.bleepingcomputer.com/news/security/malicious-jetbrains-marketplace-plugins-steal-ai-api-keys-from-developers/), found via web search and fetched in this iteration, explicitly states: "at the time of writing, the plugin remained available for download" and "BleepingComputer has contacted JetBrains... but has not received a response as of publication."

The claim is directly contradicted by a fetchable primary source and unsupported by both sources cited. The sentence should be removed or rewritten as "JetBrains has been notified; as of publication the plugins remained listed on the Marketplace."

Category: **F3 (citation does not support the claim)** — truth defect.

### Citation does not support the claim

**F2 — § 2 Zammad item: "including a webhook SSRF" claim**

The brief states (§ 2): "Zammad released version 7.1 on 2026-06-16 addressing 13 issues now tracked exclusively as GitHub Security Advisories (including a webhook SSRF)."

Fetch of the Zammad 7.1 release page (https://zammad.com/en/product/releases/zammad-7-1) returns a list of 13 GHSAs: GHSA-7fwx-3xr4-qm6w, GHSA-p3mg-2jxr-hww2, GHSA-q3cr-3wq3-29hx, GHSA-p9xp-gx8r-4397, GHSA-4m54-p3mr-22g2, GHSA-pf47-8964-pp23, GHSA-96hh-fmj3-h4hp, GHSA-jvcg-5539-vvc3, GHSA-6rmm-28j9-q99q, GHSA-56jc-34c8-2xq4, GHSA-45cx-9mrq-mmcj, GHSA-pv3q-74g5-w7fv, GHSA-374g-4f73-g7m7.

The webhook SSRF advisory (GHSA-2vgc-vfh2-rw75) is NOT among these 13. Per web search (https://github.com/zammad/zammad/security/advisories/GHSA-2vgc-vfh2-rw75), the webhook SSRF was patched in Zammad 7.0.1 (published April 8, 2026), not in 7.1. The BSI advisory page (https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1981) renders as a JavaScript SPA and returns no parseable content from either direct fetch or bridge — the BSI source for this parenthetical cannot be verified and the Zammad primary source does not support the claim.

The parenthetical "(including a webhook SSRF)" should be dropped, as it refers to a 7.0.1 fix, not a 7.1 fix.

Category: **F3 (citation does not support the claim)** — truth defect.

### Missed angles

**F3 — Possible follow-on: Oracle CVE-2026-35273 / ShinyHunters active exploitation**

The SecurityWeek article fetched in this iteration mentions: "Oracle notes active exploitation attempts against unpatched systems, specifically mentioning CVE-2026-35273 affecting PeopleSoft, which the ShinyHunters group reportedly exploited against over 100 organizations." This is a KEV-level active exploitation of a PeopleSoft CVE bundled into the same June 2026 CSPU that the brief covers. The brief correctly covers the CSPU but focuses on CVE-2026-46978 and CVE-2026-35278 as the standout high-CVSS items. CVE-2026-35273 and ShinyHunters exploitation of PeopleSoft is not mentioned and may have been outside the sub-agents' scope or the 36-hour window (Oracle issued a Security Alert for CVE-2026-35273 on June 10 per the Oracle advisory). This is a missed angle for a Swiss public-sector audience that may run PeopleSoft.

Suggested search: `site:securityweek.com OR site:bleepingcomputer.com CVE-2026-35273 ShinyHunters PeopleSoft exploitation 2026`

Category: **F10 (missed angle)** — advisory/editorial.

---

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

F1 and F2 are truth-class (citation does not support the claim). F3 is advisory/editorial (missed angle).

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: section-3-research
  item: "JetBrains IDE plugins — 15 plugins catch stealing AI keys"
  url_or_quote: "JetBrains has pulled the plugins."
  summary: "Neither cited source (Aikido, Infosecurity Magazine) confirms plugin removal. BleepingComputer (fetched this iteration) explicitly states 'at the time of writing, the plugin remained available for download' and JetBrains had not responded. Claim directly contradicted — remove or replace with 'JetBrains has been notified; plugins remained listed as of publication.'"

- code: F3
  category: claim-not-supported
  section: section-2-vulnerabilities
  item: "BSI flags 13 vulnerabilities patched in Zammad 7.1"
  url_or_quote: "addressing 13 issues now tracked exclusively as GitHub Security Advisories (including a webhook SSRF)"
  summary: "The Zammad 7.1 release page lists 13 specific GHSAs; GHSA-2vgc-vfh2-rw75 (webhook SSRF) is not among them — it was patched in 7.0.1 (April 2026). The BSI advisory page is a JS SPA returning no parseable content. The parenthetical '(including a webhook SSRF)' is unsourced for the 7.1 release and should be dropped."

- code: F10
  category: missed-angle
  section: section-2-vulnerabilities
  item: "Oracle June 2026 CSPU"
  url_or_quote: "SecurityWeek article mentions CVE-2026-35273 / ShinyHunters actively exploited PeopleSoft against 100+ orgs — not in brief"
  summary: "CVE-2026-35273 ShinyHunters active exploitation of PeopleSoft (Oracle Security Alert June 10) is actionable for public-sector orgs running PeopleSoft. Brief covers same CSPU but focuses on higher-CVSS items. Suggested search: site:securityweek.com OR site:bleepingcomputer.com CVE-2026-35273 ShinyHunters PeopleSoft exploitation 2026"
```
