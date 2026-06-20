**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-20T04:47:11Z · ended_at=2026-06-20T04:53:47Z · duration_seconds=396
**Self-telemetry:** webfetch_calls=12 · websearch_calls=0 · bridge_fetches=7 · urls_checked=19

## Verification report — briefs/2026-06-20.md (iteration 3)

Cold pass over the whole brief plus targeted confirmation of the five iteration-1/2 remediations. Every cited URL fetched (WebFetch for general hosts; tools/fetch_source.py bridge for CISA / NCSC-CH / BSI / NCSC-NL / PTC). Env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID unset — model self-identified from runtime per fallback.

### Status of the five prior remediations (all CONFIRMED CORRECT)
- (a) Splunk SVD-2026-0603 / CVE-2026-20253 / CVSS 9.8 / fixed 10.4.0,10.2.4,10.0.7 — verified against advisory.splunk.com/advisories/SVD-2026-0603 (title "Unauthenticated Arbitrary File Creation and Truncation in a PostgreSQL Sidecar Service Endpoint", CWE-306, 9.8, "limited exploitation" by PSIRT in June 2026). CISA-KEV add 2026-06-18 verified directly against the live KEV catalog (FOUND CVE-2026-20253, dateAdded 2026-06-18, Splunk Enterprise). NCSC-NL NCSC-2026-0198 (resolved txt) confirms "actief misbruik waargenomen van CVE-2026-20253". No stale 8.8 / SVD-0601 anywhere except the § 7 correction note that intentionally documents them.
- (b) Gogs Additional-source GHSA-qf6p-p7ww-cwr9 resolves to the specific advisory (RCE via git rebase --exec argument injection, fixed 0.14.3). Confirmed.
- (c) Windchill CVE summary table builds 12.1.2.27 / 13.0.2.12 / 13.1.2.8 / 13.1.3.4 — verified EXACTLY against Heise (patched versions: 13.1.2.8, 13.1.3.4, 13.0.2.12, 12.1.2.27). Confirmed.
- (d) § 7 verification-correction entry accurately describes the SVD-0601→SVD-0603 / 8.8→9.8 correction. Confirmed.
- (e) § 7 AutoJack-CVE note present — but see F3 below: it mischaracterises what THN actually says.

### Citation does not support the claim
- **F3 — AutoJack § 7 note.** Brief: "The Hacker News references CVE-2026-26030 and CVE-2026-25592 for the chain". THN (thehackernews.com/2026/06/autojack-attack-lets-one-web-page.html) explicitly attributes those two CVEs to a DIFFERENT Microsoft vulnerability — its Semantic Kernel RCE research ("Microsoft made a similar localhost argument in its Semantic Kernel RCE research, tracked as CVE-2026-26030 and CVE-2026-25592"), not to the AutoJack/AutoGen Studio chain. The decision not to add the CVEs is right; the stated reason misrepresents the source. Reword.
- **F3 — Kodak ShinyHunters platform sentence.** The sentence "ShinyHunters' 2026 campaign has leaned on misconfigured Salesforce Experience/Aura guest-user access, Oracle PeopleSoft (CVE-2026-35273) and Snowflake credential stuffing across 100+ victims, with the group claiming a 1.5-billion-record Salesforce corpus" is inline-cited to [Malwarebytes, 2026-06-18]. Fetched Malwarebytes carries NONE of these specifics (only ShinyHunters + 2.2M + limited-scope). BleepingComputer (cited elsewhere in the same item) DOES support Salesforce Aura / 1.5B-record corpus / Snowflake / PeopleSoft-100+-orgs. Re-point the citation to BleepingComputer. (CVE-2026-35273 + PeopleSoft are established prior-coverage entities so not hallucinated; UNC6395 alias is in neither fetched Kodak source.)

### Unsupported / hallucinated facts
- **F4 — Nintendo 859 MB.** Brief: "stole roughly 859 MB of employee data ([BleepingComputer, 2026-06-18])". BleepingComputer states ~1 GB. TechNadu (second source) article body not retrievable (returns navigation only). 859 MB is not supported by any fetched source. Correct to ~1 GB or attribute to a source that carries 859 MB.
- **F4 — AVer CWE-20.** Brief: "(CVSS 3.1 9.8, CWE-20 improper input validation)". CISA ICSA-26-169-01 lists the formal Relevant CWE as CWE-552 (Files or Directories Accessible to External Parties). 'Improper input validation' prose matches the CVE description, but the CWE-20 number is the brief's, not the source's. Replace with CWE-552 or drop the number.
- **F4 — Gogs CWE-88.** Brief: "(CVSS 4.0 9.4, CWE-88 argument injection)". GHSA-qf6p-p7ww-cwr9 assigns CWE-77 and CVSS 9.9. The mechanism prose is right; CWE-88 vs the cited primary's CWE-77 is a direct mismatch. The 9.4 (labelled v4.0) is plausibly the BSI v4.0 score (BSI page is a JS SPA, not fetchable) and is NOT contradictory with GHSA's 9.9 if that is v3.1 — so the score is left as a low-confidence item, but align the CWE to the source.

### Quantifier without source
- **F14 — FortiBleed 63.3%.** Brief: "generic admin plus built-in Fortinet system accounts make up 63.3% of compromised credentials ([BleepingComputer, 2026-06-19])". Neither cited source (BleepingComputer, SecurityWeek) surfaces 63.3% in fetched text. BleepingComputer reports 73,932-74,000 devices / 21,632 domains / 194 countries / 1.16B attempts; SecurityWeek confirms 86,644 / 194 countries / Russian actor / 45-GPU Hashtopolis / AD pivot but not 63.3%. Source the figure or drop the clause. Load-bearing specific quantifier → truth-class.

### Editorial / less-is-more flags (advisory)
- **F11 — usbliter8 timing.** "completes in roughly one second" is more precise than the sources support (THN: "under two seconds"; Paradigm Shift gives no duration in fetched text). Soften.

### Items verified clean (no finding)
- Windchill CVSS 3.1 10.0 / 4.0 9.3, active exploitation + backdoors, BSI 2:30 AM call, patch 2026-06-15 — all in Heise; NCSC-CH 12713 confirms "Actively Exploited" + CVSS 4.0 9.3 + deserialization. PTC PSIRT URL reachable via bridge and independently linked by Heise as the PTC advisory.
- AVer CVE-2026-40624 9.8 / four models / firmware fix / status UNKNOWN — CISA + NCSC-CH 12720 both confirm. § 7 correctly states exploitation unknown; matches § 0 wording.
- Gogs --exec git rebase argument injection, fixed 0.14.3, default open-registration framing — GHSA confirms mechanism + fixed version.
- usbliter8 A12/A13/S4/S5, DWC2 USB DMA underflow, A14+ unaffected, RP2350 PoC, PAC bypass via heap corruption, device list — Paradigm Shift + THN + Apple Insider all corroborate.
- AutoJack three-weakness chain (CWE-1385/306/78), 0.4.3.dev1/.dev2 vulnerable, 0.4.2.2 unaffected, no ITW — Microsoft + THN confirm.
- FortiBleed 86,644 / 194 countries / Russian-speaking actor / 45-GPU Hashtopolis / AD pivot / CISA PBKDF2+session-termination+MFA guidance — SecurityWeek + BleepingComputer + CISA alert (specific advisory page) confirm.
- Gentlemen/Mackay Sugar: external access ~10 June, 2 of 3 mills, 90% affiliate RaaS — The Record confirms. Krebs confirms Yapaev/Izhevsk/Hastalamuerte-Zeta88/OSINT-not-indictment/AI tooling. § 7 reduced-confidence note accurate.
- Kodak: 17 June acknowledgement + exact "limited amount of company data" quote (BleepingComputer 06-17 + SecurityWeek), 2.2M claimed / 15 June listing / 18 June deadline — confirmed; § 7 reduced-confidence note accurate.
- All MITRE ATT&CK technique links (T1190, T1505.003, T1542.003) are standard canonical URLs.

### Whole-brief checks
- Coverage shape: § 0/§ 1 lead with DACH/public-sector (Windchill, AVer cameras, FortiBleed). § 2 inclusion gates honoured (Windchill KEV-class active exploitation; AVer CVSS 9.8 + CISA ICS; Gogs BSI kritisch). Deep dive (Windchill) earns its length and is the actively-exploited highest-severity item. Immediate Action callout meets the "act now" bar (active exploitation + backdoors + after-hours BSI escalation).
- Style: no IOCs, no vanity metrics, English throughout, no workflow-internal language in published prose.
- Dedup: Splunk/Gentlemen/usbliter8 are legitimate UPDATEs or fresh research, not recycled. § 7 drop list is well-reasoned.

### Verdict
NEEDS_FIXES (truth: 6, editorial: 0, advisory: 1)

Truth-class records (6): F3 AutoJack note, F3 Kodak Malwarebytes citation, F4 Nintendo 859 MB, F4 AVer CWE-20, F4 Gogs CWE-88, F14 FortiBleed 63.3%. Advisory (1): F11 usbliter8 timing. Highest-priority: F14 (63.3% unsourced quantifier), F3 AutoJack-note source mischaracterisation, F3 Kodak Malwarebytes mis-attribution, F4 Nintendo figure. The two CWE-number items are lower-severity source mismatches. None are blocking-severe, but each is a statement the cited source does not support.

### Findings summary (machine-readable)
(see sibling verification.iter3.findings.yaml)
