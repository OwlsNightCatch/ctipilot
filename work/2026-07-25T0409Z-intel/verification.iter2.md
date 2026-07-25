**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-25T05:11:09Z · ended_at=2026-07-25T05:22:30Z · duration_seconds=681

## Verification report — 2026-07-25T0409Z-intel (iteration 2)

### Prior-iteration (iter 1) remediation verification

Both iter-1 fixes hold up:

1. **F4 — Certighost.** Fetched `https://cybersecuritynews.com/certighost-active-directory-cs-flaw/` via `fetch_source.py url` (jina fallback). Confirmed: no mention of `certpdef.dll`, `_LoadPrincipalObject`, or `certsrv.exe` anywhere in the article — the binary/function names iter-1 flagged are gone from the entry and were never in the source. Every remaining claim checks out against the article: the `cdc`/`rmd` chase mechanism ("The vulnerable CA code trusted whatever host was supplied in `cdc` without verifying it was an actual Domain Controller"), the DCSync/krbtgt outcome, the `SERVER_TRUST_ACCOUNT` (8192) + SID-comparison patch gate, and the `ms-DS-MachineAccountQuota` (default 10) detail. MSRC's own API record (`msrc cve CVE-2026-54121`) independently confirms CVSS 8.8, `publiclyDisclosed: No`, `exploited: No`, and the MSRC description quote used verbatim in `evidence[]`. Remediation verified good.
2. **F5 — Stiftung Autismuslink.** Read the full entry: no mention of "Lynx," "FortiGate," or a FortiGate hardening recommendation anywhere in body or frontmatter. The `actions[]` array is empty (appropriately — no do-now action follows from an undisclosed vector). Extracted the actual victim PDF (`autismuslink.ch/wp-content/uploads/2026_07_Informationsschreiben_zum_Serverausfall_Extern.pdf`, decompressed the FlateDecode text stream directly) and confirmed both `evidence[]` quotes verbatim, the 2026-06-29 detection date, Infoguard forensics engagement, the criminal-complaint filing, and every affected-data category (IV/BKD service agreements, teacher contracts, doctors' certificates, 2016–2023 client dossier archive) match the source exactly. Remediation verified good.

### Citation does not support the claim

**F3.** `microsoft-email-threat-landscape-q2-2026-teams-vishing-surge` — body text: *"the OAuth redirect chain — which "obscured true destination from scanners and recipients" — ultimately delivered a BAT dropper..."* cites Microsoft Threat Intelligence, 2026-07-23. Fetched the source and searched exhaustively for "obscured" (zero hits) and "scanners" (two hits, neither matching). The source's actual sentence is: *"Because the link routed through Microsoft authentication infrastructure, both recipients and URL scanners saw a login.microsoftonline[.]com link."* The entry presents an invented phrase in quotation marks as if it were a direct quote from the cited source; it is not present anywhere in the article. The underlying fact (redirect obscures the real destination) is a fair paraphrase, but formatting a non-existent phrase as a quoted citation is a sourcing-integrity defect distinct from a paraphrase — a reader clicking through to verify cannot find the quoted words.

### Unsupported / hallucinated facts

**F4.** `laundry-bear-zimreaper-app-password-persistence` — `evidence[]` quote: *"Proofpoint has not observed TA458 using CVE-2025-66376, despite the group's regular access to webmail XSS zero-days...it is possible TA488 was given this exploit for its operations from upstream Russian intelligence taskmasters."* Fetched `https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits` and located the exact paragraph, which reads verbatim: *"Proofpoint has not observed TA458 using CVE-2025-66376, despite the group's regular access to webmail XSS zero-days. While it cannot be confirmed, it is possible TA488 was given this exploit for its operations from upstream Russian intelligence taskmasters, and its use was deconflicted from TA458's operations."* The entry's `evidence[]` field splices the two sentences with "..." and drops the hedge clause "While it cannot be confirmed," — exactly the ellipsis-splice / dropped-hedge pattern the frontmatter⇔body contract (check 4b) prohibits. The evidence field must be a contiguous, unedited verbatim substring; this one is not copyable from the page unchanged.

### Surface contradiction

**F9.** `ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496` — the entry's "Background" paragraph presents Proofpoint's TA458 as the straightforward continuation of "Operation RoundPress," the campaign ESET first documented in 2025 (cited as a corroborating source), without surfacing a real attribution divergence between the two cited sources. Fetched ESET's original report (`welivesecurity.com/en/eset-research/operation-roundpress/`): ESET explicitly attributes the original Operation RoundPress campaign to **Sednit (APT28 / Fancy Bear / Forest Blizzard / Sofacy), medium confidence**. Fetched Proofpoint's 2026-07-23 report (the entry's primary source): Proofpoint explicitly states *"At the time of writing, there is no indication of targeting overlap in Proofpoint telemetry between TA458 and TA422 (Sofacy, APT28, Fancy Bear, Forest Blizzard)"* and separately assesses *"it is plausible that TA458 is linked to Unit 20728"* — a **different** GRU unit than APT28's tracked Unit 26165. So: ESET's own attribution for the campaign the entry treats as TA458's direct predecessor is a different actor cluster than the one Proofpoint's current tracking explicitly disclaims overlap with. The entry never states ESET's Sednit/APT28 attribution and never flags that Proofpoint's own TA458 designation is explicitly NOT the APT28-tracked cluster — a materially relevant fact for a reader trying to correlate telemetry (conflating TA458 with APT28/Sofacy indicators would be a mis-hunt). Recommend a `Contradiction:` line in § Verification Notes or an added sentence in the entry noting ESET's original Sednit/APT28 attribution and that Proofpoint's TA458 explicitly excludes overlap with that cluster.

### Classification missing / inconsistent

**F17.** `ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496` — `classification: {reliability: B, credibility: 1}`. Per `config/org-profile.yaml`, credibility `1` = "Confirmed — corroborated by other independent sources." The entry's own `sourcing_note` states: *"The new SOGo zero-day CVE-2026-8496 is Proofpoint's own disclosure, corroborated by the Alinto 5.12.8 release."* The Alinto GitHub release confirms only that a patch exists, not that TA458 exploited a zero-day in it — that claim is Proofpoint-only. ESET's report corroborates only the background/naming of the 2025 campaign, not the entry's headline new finding (the standing five-platform zero-day supply and the SOGo zero-day). The entry's central, novel claim is single-vendor-sourced and not independently confirmed — credibility should be `2` ("Probably true — not independently confirmed"), not `1`.

**F17.** `laundry-bear-zimreaper-app-password-persistence` — `classification: {reliability: B, credibility: 1}`. Same pattern: this is an `update_of` entry whose entire delta (the CSS-@import sanitizer bypass mechanics, DNS-tunnelled exfiltration detail, and the load-bearing "ZimbraWeb" app-password persistence finding) comes exclusively from Proofpoint's blog. The corroborating source (CISA joint advisory AA26-204A) covers the *original* CVE-2025-66376 campaign, not these mechanics — the advisory does not mention ZimReaper, the app-specific-password persistence trick, or the CSS-tag-splitting technique (confirmed by reading the fetched AA26-204A text). The entry's actual new content is single-vendor-sourced; credibility `1` overclaims independent corroboration. Should be `2`.

### Action-item discipline (advisory)

**F18.** `ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496` — second action: *"Inventory internet-reachable self-hosted Zimbra, mDaemon, Roundcube, Kerio and SOGo webmail; where a patch lags, apply compensating WAF rules on the message-render endpoint, since exploitation needs only a viewed email."* The WAF clause restates the body's own hardening line almost verbatim: *"treat any external-facing self-hosted webmail as requiring compensating WAF coverage between patch cycles."* The inventory clause is a genuine distinct task and should stay; recommend trimming the action to the inventory instruction alone (or rephrasing the WAF part into a genuinely new, more specific configuration step) so it doesn't double as a restatement of body guidance.

### Verified clean (no findings)

- `check-point-mgmt-cve-2026-62144-62145-siblings` — both CVSS scores (Check Point's own 9.3/7.5, NCSC-NL's v4 10.0/9.4) verified against the CVE.org CNA record and the NCSC-NL advisory page respectively; both `evidence[]` quotes verbatim-confirmed on the Check Point sk185152/sk185153 pages; CERT-FR publication date and active-exploitation claim (CVE-2026-16232 only) confirmed.
- `thailand-mof-hermes-ai-agent-post-exploitation` — every technical claim (YOLO-mode quote, 585 files/470 MB, HiveServer2 SASL-PLAIN/UDF registration, Ambari, GlassFish WAR/JSP webshell, Hades implant persistence/beaconing, both `evidence[]` quotes, ThaiCERT/NCSA 2026-07-15 notification) confirmed verbatim against Hunt.io and BleepingComputer. The "second AI-agent-driven autonomous-attack disclosure this pipeline has tracked in roughly a week" claim checked against `prior_coverage.json`: the Hugging Face autonomous-agent breach (2026-07-21) is the first, the 2026-07-22 OpenAI piece is an update of that same incident (not a second disclosure), so "second… in roughly a week" is accurate.
- `microsoft-email-threat-landscape-q2-2026-teams-vishing-surge` — aside from the F3 above, every other quantified claim (weekly vishing ~10x mid-2025 baseline, 94–96% credential-phishing share, the 67,000-user/42,000-org SES campaign under 3 hours, DKIM-configured `.sk` domain, 1×1 tracking pixel, the EML/Teams-voicemail/OAuth/BAT chain, PDF→DOC drift, Tycoon2FA 92% decline) confirmed verbatim or near-verbatim against the source.
- `certighost-cve-2026-54121-ad-cs-dc-impersonation-poc` — see remediation verification above.
- `stiftung-autismuslink-bern-inc-ransom-breach` — see remediation verification above; ransomware.live claim date (2026-07-24) confirmed.

### Verdict

`NEEDS_FIXES (truth: 2, editorial: 4, advisory: 0)`

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: operational
  item: "microsoft-email-threat-landscape-q2-2026-teams-vishing-surge"
  url_or_quote: "the OAuth redirect chain — which \"obscured true destination from scanners and recipients\" — ultimately delivered a BAT dropper"
  summary: "Quoted phrase does not appear in the cited Microsoft source (searched exhaustively for 'obscured' and 'scanners' — no match); actual source sentence is 'Because the link routed through Microsoft authentication infrastructure, both recipients and URL scanners saw a login.microsoftonline[.]com link.'"
- code: F4
  category: hallucinated-fact
  section: operational
  item: "laundry-bear-zimreaper-app-password-persistence"
  url_or_quote: "Proofpoint has not observed TA458 using CVE-2025-66376, despite the group's regular access to webmail XSS zero-days...it is possible TA488 was given this exploit for its operations from upstream Russian intelligence taskmasters."
  summary: "evidence[] quote is an ellipsis-spliced, hedge-dropped composite of two sentences; verbatim source reads '...zero-days. While it cannot be confirmed, it is possible TA488 was given this exploit...and its use was deconflicted from TA458's operations.' Not a contiguous verbatim substring."
- code: F9
  category: surface-contradiction
  section: operational
  item: "ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496"
  url_or_quote: "ESET first documented Operation RoundPress in 2025 ... Proofpoint's 2026-07-23 report is the first to consolidate the current actor (which it tracks as TA458)"
  summary: "ESET's original 2025 report attributes Operation RoundPress to Sednit/APT28 (medium confidence); Proofpoint's current TA458 tracking explicitly states no telemetry overlap with TA422 (Sofacy/APT28/Fancy Bear/Forest Blizzard) and suggests a different GRU unit (20728 vs APT28's 26165). Entry does not surface this divergence."
- code: F17
  category: classification
  section: operational
  item: "ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "Entry's own sourcing_note admits the headline new finding (SOGo zero-day CVE-2026-8496 exploited by TA458) is Proofpoint's own disclosure, corroborated only by a patch-existence release (not an independent confirmation of exploitation). Credibility '1' (confirmed by independent sources) overclaims; should be '2' (probably true, not independently confirmed)."
- code: F17
  category: classification
  section: operational
  item: "laundry-bear-zimreaper-app-password-persistence"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "Entry's entire delta (CSS-@import bypass mechanics, DNS-tunnelling detail, ZimbraWeb app-password persistence) is sourced exclusively to one Proofpoint blog; the corroborating CISA AA26-204A advisory does not mention any of these mechanics (confirmed by fetching the advisory text). Credibility '1' overclaims independent corroboration; should be '2'."
- code: F18
  category: action-item-discipline
  section: operational
  item: "ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496"
  url_or_quote: "apply compensating WAF rules on the message-render endpoint, since exploitation needs only a viewed email"
  summary: "Restates body's own hardening line ('treat any external-facing self-hosted webmail as requiring compensating WAF coverage between patch cycles') almost verbatim. Keep the distinct inventory task; trim or sharpen the WAF clause."
```
