**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-09T04:56:43Z · ended_at=2026-06-09T05:00:12Z · duration_seconds=209
**Self-telemetry:** urls_checked=18 · webfetch_calls=16 · bridge_fetches=4

## Verification report — briefs/2026-06-09.md (iteration 3)

Cold read as a hostile, technically-fluent Swiss/EU public-sector SOC reader. Every cited URL was fetched in this iteration. NCSC-CH (post 12615), NCSC-NL (CSAF NCSC-2026-0179), and CISA KEV were fetched via tools/fetch_source.py per host allow-list. All other links via WebFetch with the outbound-links/entities template.

**URL truth — all 18 distinct cited URLs resolve to a specific article/advisory/PSIRT/research post and support the attached claim.** No 404s, no homepage/listing redirects, no hallucinated URLs. Named-entity cross-check (CVEs, CVSS, actors, campaigns, versions, function names) traces cleanly to the fetched sources. CISA KEV confirms BOTH CVE-2026-50751 and CVE-2026-42271 present. NCSC-NL CSAF confirms the verbatim "large-scale exploitation in the near term" framing. No attacker/defender inversion: Meta acts against NSO (confirmed), GitHub is abused staging not a victim (confirmed), TeamPCP is the attacker and SLSA/Sigstore Rekor are defender concepts (confirmed). The WhatsApp/GitHub name-collision pre-WARN is benign.

The findings below are low-impact truth defects (cited-date accuracy + one technical mischaracterization). They are real and quoted, but none changes the operational thrust of any item.

### Citation does not support the claim

**F3 — §4 TeamPCP UPDATE: "Phantom Gyp campaign targeting the Gyp build-system namespace".**
Brief (line 88): "the diary names a newly-tracked **Phantom Gyp** campaign targeting the Gyp build-system namespace".
SANS ISC diary 33060 (fetched this iteration) names Phantom Gyp (attributed to StepSecurity) and describes it as targeting packages that use `binding.gyp` files to trigger `node-gyp` execution at install time. The source does NOT describe a "Gyp build-system namespace" — there is no npm scope/namespace named "Gyp"; the mechanism is install-time `node-gyp` script execution. A reader hunting for a "@gyp" namespace would be misdirected. Recommend rephrasing to "abusing `binding.gyp` / `node-gyp` install-time execution in compromised npm packages" to match the source.

### Unsupported / hallucinated facts

**F4a — Wiz citation date wrong.** Brief cites the Miasma analysis as "[Wiz, 2026-06-06]" (lines 88, 92). The fetched Wiz page is dated **June 1, 2026**. Content fully supports the @redhat-cloud-services / Miasma / Mini-Shai-Hulud claim; only the cited date is wrong. Correct to 2026-06-01.

**F4b — Oxford Careers Service statement date wrong.** Brief cites "[Oxford Careers Service, 2026-06-04]" (lines 23, 27). The fetched statement is dated **1 June 2026** (incident discovered 28 May, disclosed 1 June). Content supports the names/emails/encrypted-passwords-for-non-SSO claim. Correct cited date to 2026-06-01.

**F4c — Mandiant UNC6692 date off by one.** Brief cites "[Mandiant, 2026-04-24]" (lines 62, 66). The fetched Google Cloud / Mandiant page ("Snow Flurries: How UNC6692...") is dated **April 23, 2026**. SNOWBELT/SNOWGLAZE/SNOWBASIN, LSASS-via-Task-Manager (T1003.001) and Pass-the-Hash narrative all confirmed on the page. Possible timezone artefact; correct to 2026-04-23 for precision.

### Editorial / less-is-more flags (advisory)

**F11a — §3 Teams item: T1550.002 (Pass-the-Hash) ID assignment.** The Mandiant source describes Pass-the-Hash narratively but lists it under T1134 in its ATT&CK table, not T1550.002. The brief's T1550.002 mapping is the canonically-correct ID for Pass-the-Hash and is a defensible analytical mapping, not a fabrication — leave as-is; noted only so the next reader knows the exact source table differs.

**F11b — §2 LiteLLM: "typically listens internally on port 4000".** Horizon3.ai (the cited analysis) does not mention port 4000; it is general LiteLLM default-config knowledge and not load-bearing for any action. Advisory only — either drop the sentence or leave it; no source needed for the operational point.

**F11c — Deep dive §5 sk185033 as version-list reference.** support.checkpoint.com/results/sk/sk185033 renders as a portal/SPA shell to a fetcher (no version trains visible) — the same SPA limitation that dropped the Kemp item this run. It is acceptable here because it is a vendor SK hotfix pointer (not a sole primary), and the affected version trains (R80.20.X … R82.10) are independently confirmed in the Check Point blog and NCSC-CH content I fetched. No action required; flagged for transparency.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 0, advisory: 3)

Truth count = F3 + F4a + F4b + F4c. All four are quoted against a source fetched this iteration and are low-impact (three cited-date corrections + one technical-phrasing fix). No URL, CVE, actor, campaign, version, attribution, or KEV/CVSS defect found. Once the four are corrected this brief is publishable; the remaining advisory items can be left at the main agent's discretion.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: updates-prior-coverage
  item: "UPDATE: TeamPCP open-sources Mini Shai-Hulud — Phantom Gyp derivative"
  url_or_quote: "Phantom Gyp campaign targeting the Gyp build-system namespace"
  summary: "SANS ISC 33060 describes Phantom Gyp as abusing binding.gyp/node-gyp install-time execution, not a 'Gyp build-system namespace'; no such npm scope exists. Rephrase to match source."
- code: F4a
  category: hallucinated-fact
  section: updates-prior-coverage
  item: "UPDATE: TeamPCP / Miasma Wiz citation"
  url_or_quote: "[Wiz, 2026-06-06](https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages)"
  summary: "Cited date 2026-06-06 wrong; fetched Wiz page dated 2026-06-01. Content correct. Fix date to 2026-06-01."
- code: F4b
  category: hallucinated-fact
  section: active-threats
  item: "Oxford University CareerConnect breach"
  url_or_quote: "[Oxford Careers Service, 2026-06-04](https://www.careers.ox.ac.uk/article/careerconnect-secured-and-safe-to-use-following-data-security-incident)"
  summary: "Cited date 2026-06-04 wrong; fetched statement dated 2026-06-01 (discovered 28 May, disclosed 1 June). Content correct. Fix date to 2026-06-01."
- code: F4c
  category: hallucinated-fact
  section: research-investigative
  item: "Unit 42 Teams phishing — Mandiant UNC6692 additional source"
  url_or_quote: "[Mandiant, 2026-04-24](https://cloud.google.com/blog/topics/threat-intelligence/unc6692-social-engineering-custom-malware)"
  summary: "Cited date 2026-04-24; fetched page dated 2026-04-23. Content (SNOW suite, T1003.001, PtH) confirmed. Fix date to 2026-04-23."
- code: F11a
  category: editorial-advisory
  section: research-investigative
  item: "Unit 42 Teams phishing — T1550.002 mapping"
  url_or_quote: "moving laterally with Pass-the-Hash (T1550.002)"
  summary: "Mandiant table lists T1134, not T1550.002, for PtH; brief's ID is the canonically-correct mapping. Defensible analytical mapping; leave as-is."
- code: F11b
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-42271 LiteLLM"
  url_or_quote: "The proxy management API typically listens internally on port 4000."
  summary: "Horizon3.ai (cited) does not mention port 4000; general default-config knowledge, not load-bearing. Drop or leave."
- code: F11c
  category: editorial-advisory
  section: deep-dive
  item: "Deep dive — sk185033 version-list reference"
  url_or_quote: "https://support.checkpoint.com/results/sk/sk185033"
  summary: "SPA shell to a fetcher; acceptable as vendor SK hotfix pointer (not sole primary). Version trains independently confirmed in Check Point blog + NCSC-CH. No action."
```
