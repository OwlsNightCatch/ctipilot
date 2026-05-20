**Model:** Claude Opus 4.7 (1M context) (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-20T04:35:43Z · ended_at=2026-05-20T04:42:47Z · duration_seconds=424
**Self-telemetry:** urls_checked=22 · webfetch_calls=17 · websearch_calls=3 · bridge_fetches=6

## Verification report — briefs/2026-05-20.md (iteration 1)

Cold-read verification. Every claim flagged below is backed by a `WebFetch` or bridge fetch I performed during this iteration, with the cited page paraphrased above; the source URLs the brief itself references were retrieved (Microsoft Fox Tempest, Microsoft Storm-2949, Drupal PSA, Sparx CERT-PL, Sparx sploit.tech, SEPPmail InfoGuard, Huawei Recorded Future, StepSecurity actions-cool, Cisco Talos BadIIS, BleepingComputer DirtyDecrypt, Moselwal DirtyDecrypt, The Hacker News DirtyDecrypt, The Hacker News vm2, MSRC OData for CVE-2026-41091/45584/45585 via the bridge, BSI WID-SEC-2026-1579 and 1583 via CSAF, ENISA EUVD-2026-30931, both DeXpose articles, Microsoft On the Issues, The Record on Fox Tempest, BleepingComputer on Storm-2949, SecurityWeek and The Hacker News and The Register on Drupal, plus The Hacker News article on Nx Console).

Bottom line: the brief is in **good shape**. The Drupal Immediate Action callout is solidly grounded (PSA + NCSC.ch + SecurityWeek + The Register + BSI WID-SEC-2026-1579 all confirm the 20/25 score, the "exploits within hours or days" warning, and the EOL 8.9/9.5/10.4/11.1 patch-file scope). The Storm-2949 deep dive (§ 5) is **exceptionally accurate** — every Microsoft-attributed quote, every Azure operation name (`microsoft.Web/sites/publishxml/action`, `microsoft.sql/servers/firewallrules/write`, `microsoft.storage/storageaccounts/write`, `microsoft.Storage/storageAccounts/listkeys/action`), the four-account scope, the VPN-configuration-document targeting, the VMAccess + Run Command chain — all confirmed verbatim from the cited Microsoft Security Blog. The Sparx multi-CVE block is technically faithful to CERT-PL + sploit.tech + ENISA EUVD (CVSSv4 9.3 on CVE-2026-42097 confirmed by EUVD-2026-30931 lookup). SEPPmail InfoGuard `/v1/file.app` → syslog.conf → newsyslog SIGHUP chain confirmed end-to-end including the cron entry and Perl one-liner. Huawei VRP / POST Luxembourg item supports every named institutional quote (Paul Rausch, Anne Jung, Luxembourg prosecutors) against the cited Recorded Future News piece. The actions-cool/issues-helper item's Mini Shai-Hulud / Socket attribution **is** supported — The Hacker News quotes Philipp Burckhardt, head of threat intelligence at Socket, naming the `t.m-kosche[.]com` exfil domain overlap (verified via search). MSRC CVE-2026-45585 mitigation flow including the BootExecute / autofstx.exe registry edit and the FAQ quote about "physical access to the target" all verbatim from the MSRC OData record.

Five findings nonetheless — three truth-class, two editorial. Counts below.

### Claim does not support the citation (F3)

- **F3** — § 1 Fox Tempest item, attribution sentence: *"The service charged USD 5,000–9,000 per signing run via a Google Form pricing sheet and a Telegram channel labelled 'EV Certs for Sale by SamCodeSign' ([The Record, 2026-05-19](https://therecord.media/microsoft-disrupts-fox-tempest-malware-signing-service))."* The Record article was fetched and confirmed to exist; it states pricing as "thousands of dollars" and does NOT contain the $5,000-$9,000 range, the Google Form mechanism, or the Telegram channel name. These specifics come from the Microsoft Threat Intelligence blog (which IS cited elsewhere in the item paragraph). The parenthetical citation in this sentence should point to the Microsoft Threat Intelligence URL, not The Record — or the sentence should be split so the Microsoft-source-only specifics are attributed to that blog and the "thousands of dollars" generic stays with The Record.

- **F3** — § 2 vm2 item, last paragraph: *"Full patch: upgrade to **vm2 3.11.2**; no configuration workaround exists."* The brief cites BSI WID-SEC-2026-1583 as a primary source on this item. The BSI CSAF fetched via the bridge lists the product version range as `<3.11.4` (fixed version `3.11.4`), not 3.11.2. The Hacker News article does carry "3.11.2 for optimal protection." This is a genuine source contradiction: the BSI ships a comprehensive fix at 3.11.4 (likely covering additional CVEs disclosed after the 11.2 release), but the brief asserts 3.11.2 as the final patch. Either (a) reconcile by changing the body to "vm2 ≥3.11.4 per BSI; ≥3.11.2 closes the bulk of the 12-CVE set per the vm2 maintainers", (b) drop the BSI version-range mismatch via a "BSI lists 3.11.4 as the fixed-product version; vm2 maintainer GHSA advisories confirm 3.11.2 closes the disclosed cluster" footnote in § 7, or (c) verify which is current and correct.

### Unsupported / hallucinated facts (F4)

- **F4** — § 3 Cisco Talos BadIIS item, two specific quantifier claims: *"Campaign scope at the time of writing: over 1,800 Windows IIS servers compromised globally, focused on Thailand and Vietnam with confirmed infections in India, Pakistan, and Japan"*. The cited Cisco Talos blog (the only source on this item) was fetched end-to-end. It does not state any specific server count and does not name Thailand, Vietnam, India, Pakistan, or Japan; the only geographic reference is "the Asia-Pacific region (along with a few in South Africa, Europe and North America)". Both the "1,800" count and the five named countries are unsupported. Recommendation: drop the "over 1,800" count and replace the country list with the verbatim Talos phrasing ("Asia-Pacific region (along with a few in South Africa, Europe and North America)"). Sub-agent S3's findings YAML carries the same claims so the drift originated upstream of the main agent.

### Quantifier without source backing (F14)

- **F14** — § 2 DirtyDecrypt item, leading sentence: *"CVE-2026-31635 (CVSS 7.5, CWE-122) is a **page-cache write due to a missing copy-on-write guard…**"*. The two cited primaries in the body (Moselwal, BleepingComputer) do not state CVSS 7.5 or CWE-122. Moselwal explicitly puts the LPE in the "7.8-8.1 range" and provides a different CVSS string for the DoS variant. The Hacker News (cited as "Additional source") DOES carry "CVSS score: 7.5" verbatim — so the assertion is technically grounded, just not by the body's lead citations. NVD is the actual upstream source of "CVSS 7.5" but is not cited (and shouldn't be cited as primary per repo policy). Resolution: either move The Hacker News into the primary Source line for the CVSS claim, or add a half-sentence note that "CVSS 7.5 / CWE-122 per NVD; primary technical write-up [Moselwal] places the LPE in the 7.8-8.1 range".

### Single-source items missing [SINGLE-SOURCE] flag (F12)

- **F12** — § 1 Microsoft DCU / Fox Tempest item. Cited sources: Microsoft Threat Intelligence blog + Microsoft On the Issues blog + The Record. Two of the three are both Microsoft properties. The third (The Record) is corroborating, not primary. For the disclosure-specific technical claims (1,000+ certificates, signspace[.]cloud seizure, downstream customer list, $5,000-$9,000 pricing, Telegram channel name), Microsoft is effectively the only voice. National-CERT-style vendor-as-primary carve-out applies (Microsoft is the disclosing party and court action filer) so [SINGLE-SOURCE] need not appear on the heading — but § 7 Verification Notes should acknowledge "Fox Tempest — Microsoft-as-primary; The Record corroborates the disruption but not the granular pricing / Telegram-channel-name specifics" alongside the existing vendor-as-primary entries (CVE-2026-45584, CVE-2026-45585, CVE-2026-41091). Editorial-class because the reader benefits from seeing the source structure made explicit, not because the brief is wrong.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 1)

- Truth-class (F3 × 2, F4 × 1, F14 × 1): F3 Fox Tempest citation mismatch, F3 vm2 patch-version contradiction, F4 Cisco Talos BadIIS unsupported quantifier + country list, F14 DirtyDecrypt CVSS-not-in-primaries (the F14 is borderline — Hacker News additional-source does carry it, but the primary-source line should support the lead-paragraph value, so I'm scoring it truth-class).
- Editorial (F12 × 1): Fox Tempest single-org-source acknowledgement in § 7.
- Advisory: none in this iteration (no F11 advisory-only items).

Total finding count is deliberately small — every other claim I checked stood up to its source. The brief is unusually disciplined for an 18-item daily; the four genuine defects above are the only ones I could substantiate with quoted source paraphrases from this iteration's fetches.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: research-and-investigative-reporting
  item: "Cisco Talos demo.pdb BadIIS — campaign scope claims"
  url_or_quote: "over 1,800 Windows IIS servers compromised globally, focused on Thailand and Vietnam with confirmed infections in India, Pakistan, and Japan"
  summary: "The cited Cisco Talos article (https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/) does not state any specific number of compromised servers and does not name Thailand, Vietnam, India, Pakistan or Japan. Article only says 'Asia-Pacific region (along with a few in South Africa, Europe and North America)'. Two quantifier-class claims unsupported by the sole cited primary."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Microsoft DCU disrupts Fox Tempest — pricing / Telegram / Google Form sentence"
  url_or_quote: "The service charged USD 5,000–9,000 per signing run via a Google Form pricing sheet and a Telegram channel labelled \"EV Certs for Sale by SamCodeSign\" ([The Record, 2026-05-19])"
  summary: "The Record article confirmed to exist but does NOT contain the $5,000-$9,000 pricing, the Google Form pricing sheet, or the Telegram channel name 'EV Certs for Sale by SamCodeSign'. These specifics come from the Microsoft Threat Intelligence blog (which is cited elsewhere in the item). Either re-attribute the parenthetical citation to the Microsoft Threat Intelligence URL or move these details under that primary."
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "vm2 Node.js sandbox — patched version"
  url_or_quote: "Full patch: upgrade to **vm2 3.11.2**; no configuration workaround exists"
  summary: "BSI WID-SEC-2026-1583 (cited as primary in the brief) lists the fixed version as 3.11.4 (product_version_range '<3.11.4'). The brief asserts the full-set patch is 3.11.2; The Hacker News carries 3.11.2, but the cited BSI WID contradicts. Either reconcile (3.11.4 per BSI is the comprehensive fix; 3.11.2 may close the bulk of CVEs but not all 12) or surface the contradiction in § 7 Verification Notes."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "DirtyDecrypt — CVSS 7.5, CWE-122"
  url_or_quote: "CVE-2026-31635 (CVSS 7.5, CWE-122) is a page-cache write due to a missing copy-on-write guard"
  summary: "The two body primaries (Moselwal, BleepingComputer) do not state CVSS 7.5 or CWE-122. Moselwal explicitly puts the LPE in the '7.8-8.1 range'. The Hacker News (Additional source) does confirm 'CVE-2026-31635 (CVSS score: 7.5)'. Adequate when the additional-source is the only carrier — but the primary Source line should explicitly support the value. Move The Hacker News citation closer to the CVSS claim or add a half-sentence reconciling the primary-vs-NVD CVSS difference."
- code: F12
  category: single-source-flag-missing
  section: active-threats
  item: "Microsoft DCU disrupts Fox Tempest"
  url_or_quote: "Source: [Microsoft Threat Intelligence] · [Microsoft On the Issues] · Additional source: [The Record]"
  summary: "Two of three cited sources are both Microsoft properties; The Record corroborates the disruption but not the granular pricing / Telegram-channel-name specifics. National-CERT-style vendor-as-primary carve-out applies (Microsoft is the disclosing party and court-action filer) — [SINGLE-SOURCE] heading flag not required, but § 7 Verification Notes should acknowledge Microsoft-as-primary alongside the existing vendor-as-primary entries (CVE-2026-45584, 45585, 41091)."
```
