# Retrospective audit truth pass — batch B4

**Run:** 2026-08-02T1309Z-audit
**Window:** 2026-07-26T13:08:25Z → 2026-08-02T13:09:58Z
**Entries checked:** 20
**Result:** 17 clean / 2 imprecision / 1 factual-error (clean/total = 85%)

## Methodology

Every entry's cited URLs were fetched directly (curl with a desktop-Chrome UA, `--compressed`; `tools/fetch_source.py url` bridge for CISA/NCSC/JS-walled pages; `WebFetch` for outbound-link extraction; one `WebSearch` for a CVSS cross-check where the GHSA page did not render the score). Every `evidence[]` quote was checked for exact, contiguous, verbatim substring match against the fetched source text (HTML-stripped). Every `cves[]` id/CVSS/affected/fixed record was checked against the CVE's own advisory or vendor PSIRT page, not the roundup that carried it into the entry. Every numeric/quantifier claim in the body was spot-checked against its cited source.

## Findings

### 1. `entries/2026-07-31/exfilsquad-uk-department-for-education-pnld-breach.md` — imprecision

`techniques[]` includes `T1190` (Exploit Public-Facing Application), but neither cited source for the confirmed DfE breach (The Record, SOCRadar) states an exploitation mechanism — The Record reports only that the two portals "were impacted" with no description of how access was obtained (credential-based, exploited flaw, or otherwise). The technique mapping is unsupported by the entry's own citations.

- Ground truth: The Record's article contains no vulnerability, exploit, or intrusion-vector language for the confirmed portion of the breach.
- URL: https://therecord.media/united-kingdom-ransomware-education

Everything else in this entry (135,000-record PNLD figure, DfE's "lines of data" correction, SOCRadar's fabrication assessment, the Analog Devices thread cited per-clause to three separate sources, the SEC 8-K Item 8.01 characterisation) was verified verbatim against primary sources and is accurate.

### 2. `entries/2026-07-31/octlurk-silklurk-service-dll-plugin-backdoors-government.md` — imprecision

`evidence[]` quote 1 reads: *"We assess with medium confidence that the same threat actor is behind both backdoors, and that they are Chinese-speaking. However, at the time of publication, we couldn't attribute this activity to any known group."* This is not a contiguous verbatim substring of the Kaspersky Securelist page. The source's actual sentence is: *"We assess with medium confidence that the same **actor** is behind both backdoors, and that they are Chinese-speaking."* (no "threat" before "actor" in that sentence — "threat actor" appears only in the immediately preceding, separate sentence: *"Our investigation shows that the same threat actor operates both SilkLurk and OctLurk..."*). The word "threat" was spliced in from the adjacent sentence.

- Ground truth (verbatim from source): "We assess with medium confidence that the same actor is behind both backdoors, and that they are Chinese-speaking. However, at the time of publication, we couldn't attribute this activity to any known group."
- URL: https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/

Every other technical claim (dual-XOR loader keying to C: drive serial number / computer-name hash, three in-memory plugins, PlugX co-deployment, the Kazakhstani STS TrustFall/MystRodX/SilentRaid infrastructure overlap) was verified verbatim and is accurate.

### 3. `entries/2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055.md` — factual-error

`evidence[]` quote 1 reads: *"Across all the exploitation attempts, both autonomous and manual, Unit 42 was only able to confirm three targets were successfully exploited."* This sentence does not appear on the Unit 42 page. The actual sentence is: *"Across all the exploitation attempts, both autonomous and manual, Unit 42 confirmed data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) and command execution on 11 Marimo notebook endpoints (CVE-2026-39987)."* The entry's quote drops the 11 confirmed Marimo compromises and fabricates wording that narrows the source's own claim.

This is not a cosmetic quoting error: it inflates into the entry's headline/summary framing — *"the three confirmed compromises came from the operator's own manual work against Citrix NetScaler"* — which understates Unit 42's own confirmed-compromise count. Unit 42's CVE table independently lists `CVE-2026-39987` (Marimo Notebook) as *"Manual — Active exploitation, command execution confirmed"* for 11 endpoints. Per the source, total confirmed compromises are at least 14 (3 NetScaler + 11 Marimo), not 3. The entry's own `sourcing_note` acknowledges "an unresolved tension" between Unit 42's narrative text and its CVE table, but that acknowledgment does not excuse quoting a sentence that isn't on the page, nor does it excuse leading the headline with the narrower number.

- Ground truth (verbatim from source): "Across all the exploitation attempts, both autonomous and manual, Unit 42 confirmed data exfiltration from three Citrix NetScaler targets (CVE-2026-3055) and command execution on 11 Marimo notebook endpoints (CVE-2026-39987)." CVE table: "CVE-2026-39987 | Marimo Notebook | 9.8 | Manual | Active exploitation, command execution confirmed."
- URL: https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/

The CVE-2026-3055 record itself (CVSS 9.3 from the authoritative tracking against Citrix's own bulletin — correctly *not* borrowed from Unit 42's own mistaken 9.8 in its roundup table — the SAML-IdP precondition, and the affected/fixed version ranges 13.1-62.23/14.1-66.59/13.1-FIPS-NDcPP 13.1-37.262) was independently verified against Citrix's bulletin content (via third-party mirrors, since support.citrix.com is a JS-walled SPA that neither `curl`, `WebFetch`, nor the jina reader could render) and is accurate.

## Clean entries (17/20) — verified, no defects found

1. `elastic-hugging-face-agent-initial-access-detection-mapping.md` — every evidence quote verbatim against the Elastic Security Labs page; GPT-5.6 Sol, HDF5/Jinja2 initial-access mechanics, SSRF-then-pivot narrative, ~17,600 actions, agent-vs-human tells all confirmed.
2. `everest-publishes-stadler-rail-supplier-archive.md` — TechNadu (201 GB / 271,000 files / HackManac attribution / four named operators) and Stadler's own release (first-published 2026-07-21T07:57:43Z, last-revised 2026-07-23T07:35:27Z per CMS metadata) both confirmed verbatim.
3. `genielocker-toy-ghouls-no-ransom-note-esxi-ransomware.md` — Kaspersky Securelist quotes on OpenVPN initial access, watchdog/debugger-check thread, no-ransom-note design, CRC32 self-check all verbatim; Toy Ghouls/Bearlyfy/Labubu/Laboo.boo aliasing and "previously relied on third-party encryption Trojans like RedAlert, LockBit, and Babuk" confirmed.
4. `health-isac-shinyhunters-sso-tier0-advisory-brinks-home.md` — Health-ISAC "SSO is the control plane" quote, BleepingComputer's two unreconciled Salesforce figures (4.9M vs 1.1M rows), Brinks Home CEO statement, 13 July vishing date all confirmed verbatim.
5. `ta488-exchange-owa-cve-2026-42897-owareaper-implant.md` — MSRC record (CVSS 8.1, vector `AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N`, Exploited: Yes), Microsoft Exchange Team Blog (CU14/CU15/CU23 Period-2-ESU fix path, "does not automatically remove" mitigation language), and Proofpoint's OWAReaper mechanics all confirmed verbatim; "16-nation joint advisory" cross-checked via web search and corroborated.
6. `aimy-captcha-joomla-cve-2026-65883-object-injection-rce.md` — every VulnCheck quote (no-signature/no-allowed_classes, JForm::validate() reachability, FormattedtextLogger gadget range 3.9–5.2.1, homepage-scanner blind spot) verbatim; CVSS 9.8, version range 18.0–20.0 fixed 20.1 (2026-07-29), and the "52 CVEs in 2025, 132 through July 2026 / three KEV-listed" wave-context figures all confirmed.
7. `captivecrunch-storm-2945-hospitality-captive-portal-rat.md` — every one of ~15 inline Microsoft Threat Intelligence quotes (sub-cluster assessment, CornFlake persistence/C2, ChocoShell token-broker theft, UAC-bypass chain) and both ReliaQuest quotes (compromised-gateway geography, FrostArmada non-attribution, APT28 tradecraft similarity) verified verbatim; "since early May 2026" and "since 16 July" dates confirmed.
8. `device-code-phishing-bl-networks-second-wave-2026.md` — Huntress's "infrastructure reputation" quote, 26-incidents/23-identities figure, April 13 start date, 533 events/113 logins, ASN AS399629/Bushido Token attribution all confirmed verbatim.
9. `fbi-epa-water-plc-lockout-seven-states-eu-exposure.md` — FBI/EPA PSA quoted verbatim across five separate clauses; Censys figures (4,148 Rockwell/71.0%/59.0%; 4,117 Siemens/86.0%; 2,072 Schneider with its non-PLC-specific caveat; "exposure characterization only" disclaimer) all confirmed exactly; SecurityWeek/AP quotes on the FBI's non-attribution and the "treat it like it's Iran" outside-expert framing confirmed.
10. `france-education-nationale-agent-training-breach.md` — Cyberattaque.org quotes (compromised-account access path, no-passwords/no-banking/no-pupil-data statement, "sans établir que toutes les fiches..." hedge) confirmed verbatim; March COMPAS (~243,000 records) and April ÉduConnect incidents, ANSSI/CNIL notification, and the MFA-unconfirmed hedge all confirmed.
11. `ibm-websphere-cve-2026-14512-14446-preauth-no-fix-pack.md` — both IBM PSIRT bulletins confirmed verbatim (CVSS 9.8/9.8/7.4, CWE-306/502/532, "Workarounds and Mitigations: None," APAR DT496500/PH72166, "targeted availability 3Q2026," 9.0.5.29/8.5.5.31 fix versions).
12. `solarwinds-web-help-desk-cve-2026-28323-saml-auth-bypass.md` — both SolarWinds advisories confirmed verbatim (CVSS 9.8 on CVE-2026-28323, CVSS 8.2 on CVE-2026-28299, both vectors, Dhabaleshwar Das/Tenable credits); the release-notes-vs-advisory remediation-boundary discrepancy the entry flags (2026.2 vs 2026.2.1) is real and correctly surfaced rather than silently resolved.
13. `xcsset-v40-macos-defaults-fileless-persistence.md` — all four Unit 42 evidence quotes verbatim; "17 distinct modules," South Asia targeting, Trend Micro 2020 discovery / Microsoft March+September 2025 prior versions all confirmed.
14. `adform-trackpoint-supply-chain-clipboard-crypto-clipper.md` — Adform's own notice, The Hacker News' Beaumont quotes ("even if you notice... it keeps replacing it," "the public timeline is unresolved," six-byte XOR key, 1,800 customers/180 countries caveat), and BleepingComputer's archived-snapshot timestamp (2026-07-26 23:29:03 GMT) all confirmed verbatim.
15. `cci-nice-cote-dazur-edrh-admin-account-export-breach.md` — both cyberattaque.org quotes (unauthorised admin-account access, recruiter/adviser-impersonation risk), the 2026-07-18 date, the exposed-field list, and the undisclosed-takeover-vector framing (stolen password / phishing / credential reuse / session hijacking, none selected) all confirmed verbatim.
16. `coldcard-rng-fallback-macro-guard-seed-theft.md` — every Coinkite quote (the `#ifndef` vs nonzero-value guard defect, the review-gap admission, the AI-discovery-assumption paragraph, "both attackers and defenders have the same AI tools") confirmed verbatim; 40-bit/72-bit entropy estimates, all six firmware version numbers, and CryptoTimes' Galaxy Research figures (1,367.05 BTC / 4,585 addresses / 207.7294 BTC third wave / 27-hour wave gap) all confirmed exactly.
17. `cve-2026-66066-rails-attack-chain-public-forensic-tooling.md` — both Rails-security-team quotes, the agent-skill descriptions, the "extracted from work I did at 37signals" attribution, and the Discourse maintainer's Landlock/ImageMagick reply all confirmed verbatim on the live discuss.rubyonrails.org thread; CVSS 9.5 (CVSS v4, GitHub CNA-scored) cross-checked via web search since the GHSA page did not render the score to direct fetch.

## Assessment

The two `imprecision` findings share a root pattern with the one `factual-error`: **quote fidelity under time pressure on long, technically dense source pages** — a word spliced in from an adjacent sentence (OctLurk), a technique tag applied without a supporting behavioural description in the cited sources (ExfilSquad), and, most seriously, a paraphrase presented as a direct quote that materially undercounts what the source itself confirms (Unit 42). The Unit 42 case is the one worth escalating: it is not a cosmetic drift but a headline-load-bearing number that contradicts the cited source's own CVE table, and the entry's own `sourcing_note` shows the discrepancy was noticed and then resolved in the wrong direction (quoting a fabricated sentence rather than surfacing the true, larger confirmed-compromise count). Recommend the main agent correct the evidence quote to the verbatim sentence, and revise the headline/summary framing to state Unit 42's actual confirmed total (3 NetScaler + 11 Marimo, not "three").

No hallucinated URLs, no broken links, no IOC violations, and no NVD/MITRE-only sourcing were found in this batch. Every CVE id/CVSS/affected/fixed record checked against its per-CVE authority matched (WebSphere, SolarWinds, Rails, Aimy Captcha, Citrix NetScaler). No Admiralty classification code was found to contradict its entry's own sourcing profile.
