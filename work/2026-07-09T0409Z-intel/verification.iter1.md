**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-09T04:50:44Z · ended_at=2026-07-09T05:01:22Z · duration_seconds=638
**Self-telemetry:** urls_checked=23 · webfetch_calls=13 · bridge_fetches=6 · websearch_calls=1

## Verification report — 2026-07-09T0409Z-intel (iteration 1)

Cold read of 10 new entries + run record. Every inline source URL fetched (WebFetch, escalated to jina bridge on 403/anti-bot). Every evidence[] quote checked verbatim against a source fetched this pass. Dedup checked against prior_coverage.json (no overlap) and cves_seen.json (gate already validated CVE dedup). Entity registry cross-checked. Classification codes checked against sources.json reliability tiers.

**URL liveness:** all 23 cited URLs resolve to specific articles/advisories. Two transport blocks that are NOT defects: git.kernel.org commit (Anubis PoW block via WebFetch AND jina — corroborating source; BleepingComputer independently links the same commit id 81ccda30b4e8) and Plesk support page (403 via WebFetch, recovered via jina). No F1/F2 findings.

### Unsupported / hallucinated facts

**F4 — Mandiant ADFS deep dive: evidence quote 1 is not verbatim.** `evidence[0].quote` = "Attackers who obtain the active private key can forge SAML assertions for any user in a federated environment" attributed to Mandiant. I fetched the full Mandiant page via the jina bridge and grepped it end-to-end: the string does not occur ("Attackers who", "federated environment", "any user in a" all absent). The actual verbatim text is "Successfully obtaining this active key allows an attacker to forge valid SAML assertions for any user, bypassing the need for user credentials and multi-factor authentication" (or the intro "By obtaining the private key of an ADFS token-signing certificate, an attacker can authenticate as any user to any SAML-federated application"). The claim is source-accurate; only the quotation is fabricated. Replace with a verbatim substring. (The other two Mandiant evidence quotes ARE verbatim, incl. the ellipsis-bridged SACL quote.)

**F4 — Nayax: Swiss/EEA/Bank-of-Lithuania nexus facts unsupported by cited sources + geographic error.** Body: "a Bank-of-Lithuania-licensed EU payment institution serving enterprises across the EEA, including Switzerland"; headline/summary: "operating in Switzerland and 40+ European markets." These facts establish the ENTIRE constituency nexus that lets this breach entry clear the check-5 breach bar. I fetched all three cited sources: the SEC 6-K (incident text only), DataBreaches.net (no geography), and Calcalistech (WebFetch explicit: does NOT mention Switzerland, Bank of Lithuania, or payment-institution status). None support the license or the Swiss-operations claim. Separately, "across the EEA, including Switzerland" is factually wrong: Switzerland is not part of the EEA. My web search confirms Nayax does hold a Bank of Lithuania EMI/PI license (License No 85) — but that license authorises EEA operations, which exclude Switzerland; the search found no confirmation of Swiss operations. Remediation: add a citation for the license and any Swiss-operations claim (e.g. Nayax's own regulatory page), and correct the EEA/Switzerland geography. The relevance justification of the whole entry depends on getting this right.

### Classification missing / inconsistent

**F17 — Mandiant ADFS deep dive: `reliability: A` above the source's sources.json letter.** The cited primary is `mandiant-gtig`, which is `reliability=B` (tier=standard) in `sources/sources.json`. The entry sets reliability A — one letter above the source's registered letter, which F17 flags. Set to B, or reconcile sources.json if Mandiant GTIG is intended to be A-grade. `credibility: 2` is fine (corroborated by itbrief.co.uk). (All other non-triage entries' codes reconcile: UNC1151 A = cert-pl A; Sygnia/ESET/Cavern B = their sources' B; Nayax A = sec-disclosures-edgar A; Git B is borderline-defensible on the arXiv primary + public PoC despite THN being C — not flagged. Triage-kind vuln entries correctly carry no classification and null org_triage.)

### Editorial / less-is-more flags (advisory)

**F11 — Workflow-internal policy-directive shorthand leaked into reader-facing text (style hard-rule).** ESET body Defender takeaway opens: "per PD-9 this is a single reference entry for ESET's H1/H2 report cadence (predecessor: ESET Threat Report H2 2025), not a re-summary target." Nayax `sourcing_note` ends "...reported as attributed claim, not fact, per PD-6." "PD-9"/"PD-6"/"re-summary target" are internal policy-directive references meaningless to a reader; the no-workflow-internal-language style rule applies to entries. Remove the PD references and meta framing; keep the operational reads.

### Items verified clean (no finding)

- **URLs/quotes:** BleepingComputer + V4bel (Januscape, incl. "first guest-to-host exploit research triggerable on both" verbatim); CERT-PL UNC1151 (both quotes verbatim; jina Published-Time metadata = Wed 08 Jul 2026 supports event_date 2026-07-08 — the "/2026/06/" URL slug is the Polish-original month, not a date defect); Wiz + AWS GHSA-6v3r-4p5c-mrp5 (CVE-2026-12958, CVSS 8.5, quote verbatim) + Cursor GHSA-3v8f-48vw-3mjx (CVE-2026-50549, quote verbatim); CCB + Plesk (CVE-2026-48614, CVSS 9.9, vector, CWE-94, both quotes verbatim, Shutiaev credited); arXiv 2607.02820 + THN (Git malleability, all three malleation routes confirmed); Sygnia (all three quotes verbatim); ESET welivesecurity (three quotes verbatim) + GlobeNewswire (the ~11% QR figure AND the "December 2025 through May 2026" telemetry period both confirmed in the press release — quantifier sourced, no F14); Check Point (all three quotes verbatim once jina markdown emphasis stripped); SEC 6-K (both quotes verbatim); DataBreaches (quote verbatim across paragraph breaks; 1B/100TB/~1yr/11-day figures all present and correctly attributed as unverified claim per PD-6 separation); itbrief + CyberArk 2017 + Mandiant 2021 background links resolve.
- **PD-6 victim-vs-attacker separation (Nayax):** correctly executed — SEC 6-K "immediately blocked and contained" as fact vs "The Syndicate" 1B-record/100TB/~1yr as attributed leak-site claim, with the internal contradiction surfaced. No F13.
- **Priority calibration:** 2 high (Januscape guest-to-host escape w/ public PoC; UNC1151 active nation-state 2FA-defeating phishing on constituency) both TL;DR-worthy; 0 critical is correct (no actively-exploited-to-the-hour item; KEV API showed no new additions since 2026-07-07). 8 notable defensible. No F16.
- **Dedup / entities:** no prior_coverage overlap; all seven entities_added present in registry; UNC1151 correctly linked to campaign:frostyneighbor-2026-05-campaign (registry name includes UNC1151/Ghostwriter aliases). No F15.
- **GhostApproval:** Anthropic "outside our threat model" + v2.1.32 (5 Feb 2026) symlink-warning reported faithfully with no sanitisation; CVE-to-GHSA mappings correct.
- **Coverage completeness:** the three developing-window first-coverage items (Januscape 2026-07-07, ADFS 2026-07-07, Cavern 2026-07-06) have event_date matching primary pub dates. Documented coverage gaps (cisa-advisories/directives JS-shell, industrialcyber 403) are mitigated by the KEV API (no new exploited-flaw signal). No nameable in-window story with a plausible source appears missed — coverage looks complete. No F10.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 1, advisory: 1)

Two truth defects: a fabricated (non-verbatim) evidence quote on the deep dive (F4), and an uncited + geographically-inaccurate nexus fact that the Nayax breach entry's entire relevance rests on (F4). One editorial: a classification reliability letter above its source's registered tier (F17). One advisory: workflow-internal policy-directive shorthand leaked into reader-facing text (F11). No broken/generic URLs, no dedup violations, no priority miscalibration, coverage complete.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: deep-dive (research)
  item: "mandiant-adfs-machine-dpapi-golden-saml-key-recovery"
  url_or_quote: "evidence[0] quote 'Attackers who obtain the active private key can forge SAML assertions for any user in a federated environment'"
  summary: "Non-verbatim evidence quote; not present in the fetched Mandiant page. Replace with verbatim text (e.g. 'Successfully obtaining this active key allows an attacker to forge valid SAML assertions for any user, bypassing the need for user credentials and multi-factor authentication')."
- code: F4
  category: hallucinated-fact
  section: incident
  item: "nayax-cloud-account-incident-the-syndicate-claim"
  url_or_quote: "'a Bank-of-Lithuania-licensed EU payment institution serving enterprises across the EEA, including Switzerland' / 'operating in Switzerland and 40+ European markets'"
  summary: "Nexus facts unsupported by any of the 3 cited sources (fetched all three); 'EEA, including Switzerland' is geographically wrong (Switzerland not in EEA; Bank of Lithuania EMI/PI license is EEA-scoped). Add citation + correct geography; the breach-inclusion nexus depends on it."
- code: F17
  category: classification
  section: deep-dive (research)
  item: "mandiant-adfs-machine-dpapi-golden-saml-key-recovery"
  url_or_quote: "classification.reliability: A"
  summary: "reliability A exceeds mandiant-gtig's sources.json letter (B). Set to B or reconcile sources.json."
- code: F11
  category: editorial-advisory
  section: annual-report / incident
  item: "eset-threat-report-h1-2026 (and nayax sourcing_note)"
  url_or_quote: "'per PD-9 ... not a re-summary target' (ESET body); 'per PD-6' (Nayax sourcing_note)"
  summary: "Workflow-internal policy-directive shorthand leaked into reader-facing text; remove PD references and meta framing."
```
