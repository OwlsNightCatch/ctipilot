# Retrospective truth audit — batch A (2026-09-20T1308Z-audit)

**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T13:10:38Z · ended_at=2026-09-20T13:22:19Z · duration_seconds=701

Scope: 13 published entries (2026-09-14 through 2026-09-17). Cold, hostile re-verification against
primary sources fetched this iteration. 13/13 clean or imprecision; 0 factual-error.

## Summary

- **Clean: 8/13** — cve-2026-76461-cisco-secure-email-gateway-sqli-root-rce, salt-mobile-peripheral-system-data-incident,
  chosen-brick-iran-telegram-c2-dissident-spyware, bambootoken-mqtt-c2-tendyron-sideload,
  cve-2026-76460-cisco-ise-auth-bypass-root-rce, kairos-libercourt-commune-ransomware-confirmed,
  phantomraven-npm-llm-generated-infostealer, mandiant-ai-risk-resilience-report-2026.
- **Imprecision: 5/13** — gtg-27005-ai-drone-swarm-weapons-engineering, swiss-bitcoin-pay-neuchatel-internal-systems-breach,
  cve-2026-58704-google-pixel-modem-zero-click-eop, aepd-first-ai-agent-breach-notification,
  ddrop-dram-interposer-defeats-confidential-computing.
- **Factual-error: 0/13.**

None of the imprecisions rise to a hallucinated fact, broken URL, or a claim the cited source
contradicts. Every quoted evidence[] record on every entry verified as a verbatim (or
markdown-artifact-adjusted) substring of its cited source. All techniques[] ids across all 13
entries are active in the pinned `attack/enterprise-attack.json` (none unknown/revoked/deprecated).
No IOCs found in any entry. No closed_sources records in this batch. No blocked source patterns
(homepage/listing/NVD-MITRE-per-CVE) used as a primary.

## Per-entry findings

### 1. GTG-27005 (Anthropic drone-swarm disclosure)
Clean on every substantive fact: the freelance-team assessment, the nine-accounts /
eight-civilian-use detail, the funding claims, the six-system weapons table (names, TRL ratings),
the Donetsk demonstration coordinate, the VPS geographic-control-bypass detail, and the DroneXL
corroboration (simulation-only status, Advanced Research Foundation/DARPA framing) all verified
verbatim against Anthropic's September 2026 threat-intelligence report and the DroneXL article.

**Imprecision (low confidence):** the entry states Anthropic "banned nine accounts" / "banned all
of them." Anthropic's actual text is "We identified nine accounts associated with this group;
eight were used only for ordinary freelance work... we banned accounts associated with the
actors" — this does not explicitly confirm the ban covered all nine (as opposed to a narrower
subset). A defensible reading, but the entry states it as settled fact where the source is
ambiguous.

### 2. CVE-2026-76461 — Cisco Secure Email Gateway SQLi
Clean. Cisco's own advisory (cisco-sa-esa-inj-2bLVGmhX) confirms CVSS 9.8, the SQL-injection-to-root
mechanism, active exploitation, discovery via a TAC support case, the "no workaround" statement,
and the three fixed releases verbatim. CISA KEV (fetched via `fetch_source.py cisa-kev`) confirms
dateAdded 2026-09-14, dueDate 2026-09-17, forensicTriage: Yes. The companion hardening-release
advisory (cisco-sa-hardening-esa-dfCrfXkm) verbatim-confirms the five grouped CVEs' CWE
classifications and the "CVSS score... represents the maximum potential severity of the single
most impactful underlying vulnerability" framing the entry uses to explain the four identical 9.8
scores. NCSC-NL's advisory (after resolving its JS redirect to the underlying `/2026/ncsc-2026-0368.html`
page) confirms the Dutch evidence quote verbatim and CVSS 9.8 on its own per-CVE page.

### 3. Salt Mobile peripheral-system incident
Clean. Salt's own French-language data-incident notice (salt.ch/fr/datainfo) matches all three
French `original:` fields verbatim, including the exact personal-data-category list. Blick
independently confirms the Viola Lebel spokesperson quote verbatim. 20 Minuten independently
confirms both the "peripheral system... own or connected" quote and the "notified customers and
the relevant authorities" fact the entry attributes to it. watson.ch independently confirms the
Brinztech 1.09M-record quote and the "third-largest telecom provider" description verbatim.

### 4. Swiss Bitcoin Pay internal-systems breach
Clean on all quoted facts — all three evidence[] quotes verbatim-match Swiss Bitcoin Pay's X
statement as reproduced by both corroborating outlets.

**Imprecision:** `techniques: [T1213]` ("Data from Information Repositories") is mapped despite
the entry's own body stating no access vector or mechanism has been disclosed. None of the three
cited sources describe an information-repository access behavior; they only list which data
categories may have been exposed. This looks like a mapping applied because of the data types
compromised rather than an observed collection technique the sources actually describe.

### 5. CHOSEN BRICK (NCSC-UK/FBI/AIVD Iranian spyware advisory)
Clean. NCSC UK's advisory verbatim-confirms all four evidence[] quotes, the full attack chain, the
exact registry path with its embedded space in the drop location, the mutex names, and its own
MITRE ATT&CK table (which the entry's inline T-ids match exactly, including for techniques beyond
what NCSC's table itself lists inline — those are drawn from NCSC's own prose elsewhere in the
"Action on objectives" section, verified). The Record's article independently confirms the
FBI MOIS/Handala Hack/Homeland Justice attribution paragraph cited to it, verbatim. All 17
techniques[] ids are active in the ATT&CK pin.

### 6. BambooToken (Lumen Black Lotus Labs MQTT malware)
Clean. Lumen's blog post verbatim-confirms all four evidence[] quotes and every specific figure in
the body: February 2023/July 2026/December 2025 dates, the three prior MQTT-C2 families (IOCONTROL,
Korplug/PlugX, WailingCrab), the Tendyron OnKey and Kingsoft-masquerade sideload details, the
dozen-victim list (including the named Argentina biomedical company and Chile legal firm and the
Hong Kong GitLab instance with its supply-chain framing), the 150-router SNMP-scan cluster with its
Singapore/Cambodia/Vietnam geolocation, the Cloudflare Radar top-500k/top-1M rankings, and the
"diaspora" targeting hypothesis ("Lumen hypothesizes the purpose is to target the diaspora, who are
physically located outside China but remain connected to the mainland ecosystem"). BleepingComputer
independently confirms its attributed quote verbatim.

### 7. CVE-2026-76460 (+ CVE-2026-76423) Cisco ISE auth-bypass, and its 2026-09-18 update
Clean, including the changelog-contract check (4c). Cisco's two PSIRT advisories verbatim-confirm
the CVSS 10.0 vector string, "found during the resolution of a Cisco TAC support case," active
exploitation, and the "regardless of device configuration" scoping for both CVE-2026-76460 and
CVE-2026-76423. `git diff` between the two run commits (5cfe7c5 → 58cf785) shows every changed
line — the two new CVE blocks, two new sources, two new evidence records, `updated_at`, and the
new body section — is covered by the update record's declared `fields: [cves, sources, evidence,
body]`; `discovered_at`, `run_id` and the path are untouched. NCSC-NL (NCSC-2026-0382) and CERT-FR
(CERTFR-2026-AVI-1197) verbatim-confirm the update section's specific claims: 21 vulnerabilities /
13 critical / four CVSS-10.0 CVEs, CVE-2026-76460 as the only one reported exploited, and the list
of eight CVEs with no fix for ISE 3.1/3.2 before their 30 November 2027 end of maintenance.

### 8. CVE-2026-58704 — Google Pixel modem zero-click EoP
Clean on every quoted and sourced fact: bug ID A-484011314, High-severity/Modem classification
(Google's own bulletin table), the CISA KEV dateAdded/dueDate, both TechCrunch quotes, and the
surveillance-vendor framing (TechCrunch: "It's not uncommon for bugs like this one to be abused by
surveillance vendors... who sell access to their data-stealing software to governments and law
enforcement agencies").

**Imprecision:** the entry frames the vulnerability as reachable with "no additional execution
privileges and no user interaction needed for exploitation" but never surfaces the access-vector
qualifier from the same MITRE CVE record it cites: the CNA description states "remote
(proximal/adjacent) escalation of privilege," and the record's own CISA-ADP Vulnrichment CVSS
vector is `AV:A` (`ADJACENT_NETWORK`, base score 8.8) — meaning exploitation requires radio-level
cellular adjacency (e.g. a rogue base station), not unqualified remote/internet reach. The
sourcing_note correctly explains why no CVSS is transcribed into frontmatter, but the body's prose
never mentions the adjacency requirement, which materially affects how a Tier 2 responder should
weigh real-world exploitability for a `priority: high` entry.

### 9. Kairos / Ville de Libercourt ransomware
Clean. FrenchBreaches' article verbatim-confirms the commune's own French quote and every
"not yet confirmed" detail (access vector, group, data scope, ransom demand), plus the
CNIL/ANSSI notification and criminal complaint. Ransomware.live's page description matches the
second evidence quote verbatim. The Ayuntamiento de Velilla de San Antonio statement
verbatim-confirms "no se puede confirmar que se haya producido un acceso o extracción efectiva de
datos," which the entry paraphrases accurately as "could not yet confirm effective data access or
extraction had occurred" — correctly distinguishing this narrower confirmation from Libercourt's
explicit exfiltration confirmation.

### 10. AEPD first AI-agent breach notification
Clean on every quoted and paraphrased fact: both evidence[] quotes verbatim-match AEPD's own blog
post; Francisco Pérez Bes's "deputy director" title (sourced to heise, which states it explicitly
where AEPD's own byline does not) is correctly attributed; the CCN-CERT BP/36 citation and AEPD's
four practical conclusions all verbatim-match.

**Imprecision (low confidence):** `verification: single-source-national-cert` is applied to
AEPD, Spain's data-protection regulator. The org profile's enumerated national-CERT carve-out list
names CCN-CERT as Spain's authority, not AEPD — AEPD does not appear on that list at all. Whether
this is a genuine defect turns on which document governs: `prompts/cti-run.md`'s PD-5 rule is
worded more broadly ("a high-reliability national CERT / government authority as primary
disclosing party for its own jurisdiction"), which could reasonably extend to a national data
protection authority disclosing its own regulatory process. Flagging for the main agent to settle
which reading is intended; the underlying sourcing itself is transparent and well-explained either
way.

### 11. DDRop hardware interposer
Clean on every substantive claim: the $159 bill-of-materials, the DDR5 error-handling abuse
mechanism, the SEPT-write corruption path, the 50%-per-attempt debug-bit toggle, the
Cryptographic-Integrity-mode attestation-forgery bypass, and both vendors' identical "out of
scope for our threat model, no CVE, no mitigation" responses, all verbatim-matched against
ddropattack.eu, Intel's and AMD's own advisories, and heise Security's "next-generation memory
encryption" framing.

**Imprecision (low confidence):** `techniques: [T1200, T1553]` — T1553 ("Subvert Trust Controls")
is a stretch mapping. ATT&CK's T1553 subtechniques describe local software trust-control bypasses
(code signing, Gatekeeper, root-certificate installation, Mark-of-the-Web); DDRop's forgery of a
hardware-rooted remote-attestation report via physical DRAM-bus tampering is thematically adjacent
but not the behavior any T1553 subtechnique or its parent definition actually describes. No cited
source frames the attack in T1553's terms.

### 12. PhantomRaven npm infostealer
Clean. This entry surfaced a tooling lesson during verification: trafilatura's `extract` output
for the CrowdStrike blog silently dropped a paragraph containing the "active since November 2022"
detail and the bounty-platform list ("Bugcrowd, Intigriti, YesWeHack, HackenProof, and
HackerOne"). Escalating to the raw HTML (`fetch_source.py url`) recovered the paragraph and
confirmed the entry's claims verbatim — this was a gap in the extraction tool, not a defect in the
entry. Both evidence[] quotes, the preinstall-script/npm-12 mechanism, and the full MITRE ATT&CK
table match verbatim. Endor Labs' post verbatim-confirms the 126+/86,000+ first-wave figures and
the 88-package/three-wave follow-up (November 2025–February 2026).

### 13. Mandiant AI Risk and Resilience Report 2026
Clean. All eight case-study summaries verbatim-match Mandiant's report, including figures (~100
repositories, $50,000/15,000 API calls, three-hour exfiltration cycle), named mechanisms (Shai-Hulud
worm, Confused Deputy via GitHub-allowlisted domain, CLI-hook subversion, just-in-time polymorphic
malware), and the DARK CASTLE/UNC2814 case study (SSH lateral movement, agentic-triage escalation
of a low-severity alert). Two evidence[] quotes initially failed a strict literal-substring check
because the source page's markdown rendering (trafilatura output) embeds `**bold**` markers and
`[text](url)` hyperlink syntax mid-sentence; stripping that markup confirms both quotes match the
actual rendered page text exactly — not a defect. Registry cross-check confirms `actor:dark-castle`
correctly carries `UNC2814` as an alias. `sources/sources.json`'s own admiralty audit rates
`mandiant-gtig` reliability B, consistent with the entry's `classification.reliability: B`.

## Methodology notes

- All URL fetches used `tools/fetch_source.py extract` as the primary rung, `url` for raw-HTML
  escalation (used once, on the CrowdStrike PhantomRaven post, to recover content trafilatura
  dropped), and `cisa-kev` for the live KEV catalog. No `jina` calls were needed. No WebFetch calls
  were made against cisa.gov or ncsc.ch.
- `attack/enterprise-attack.json` was queried directly (Python) for every techniques[] id across
  all 13 entries; all are present, active, non-revoked, non-deprecated.
- `entities/registry.yaml` was spot-checked for `actor:kairos-extortion`, `actor:gtg-27005`,
  `actor:dark-castle` (UNC2814 alias) — all present and correctly referenced from the entries that
  cite them.
- No entry in this batch carried `closed_sources` records, so truth check 1's drop-file
  verification did not apply to this batch.

## Self-telemetry

webfetch_calls=0 · websearch_calls=0 · bridge_fetches (fetch_source.py extract/url/cisa-kev calls)=32 · urls_checked=27
