**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-27T04:51:22Z · ended_at=2026-06-27T04:57:07Z · duration_seconds=345

## Verification report — briefs/2026-06-27.md (iteration 2)

Prior-iteration deltas pass first, then full cold read. All cited Source and Additional-source URLs fetched this iteration (WebFetch; NCSC-CH bridge for post 12579). Two confirmed-403 hosts not re-fetched (inside-it.ch, ENISA EUVD SPA) — both Additional sources only, not sole primaries, consistent with iter-1 report.

---

## Prior-iteration delta verification

### F3 — Amazon Q fix version (remediation: changed to 1.65.0)
CONFIRMED CORRECT. Wiz Research page fetched this run states: "Fixed Version: language server 1.65.0." The Register states: "We have remediated this issue in language server version 1.65.0." Brief now reads "fixed in 1.65.0; confirm ≥ 1.65.0" in both prose and the Why-it-matters block. Remediation correct.

### F4 — SANS ISC auditd clause (remediation: removed)
CONFIRMED CORRECT. SANS ISC diary (isc.sans.edu/diary/33102) fetched this run. The diary documents comm/cmdline divergence detection, eBPF/Kunai as the recommended tooling, and Operation Highland — does NOT mention auditd. Brief now reads: "The detection key is the divergence between /proc/<pid>/comm (mutable) and /proc/<pid>/cmdline... The diary points to eBPF-based tooling (Kunai)." No auditd claim remains. Remediation correct.

### F4 — The Gentlemen THN date / in-window hook (remediation: corrected to 2026-06-11; in-window hook is now inside-it.ch Swiss-targeting)
CONFIRMED CORRECT. THN article fetched this run. Byline is June 11, 2026 — confirmed. Brief now cites it as "[The Hacker News, 2026-06-11]". The in-window hook is now inside-it.ch (2026-06-26) Swiss-targeting report; 478/--spread profile correctly attributed to the 2026-06-11 article. § 7 single-source note covers inside-it.ch 403 situation. Remediation correct.

### F13 — Miasma UPDATE codfish/semantic-release-action (remediation: removed the codfish tie)
**REGRESSION INTRODUCED.** The iter-1 finding F13 stated "neither cited source (Socket, JFrog) connects the RevokeAndItGoesKaboom marker to codfish/semantic-release-action." I fetched the Socket source this run and found it DOES make this connection explicitly: "One of the strongest campaign-level markers is `RevokeAndItGoesKaboom`. This marker appears in the LeoPlatform/Miasma activity and in the codfish/semantic-release-action compromise documented by StepSecurity. In the codfish case, the malicious action searched GitHub commits for `RevokeAndItGoesKaboom` messages and used them as an operator token dead-drop channel." The JFrog source does not make this connection, but the Socket source — the primary cited source — does. The iter-1 F13 finding was incorrect. The remediation that removed the codfish link stripped a factual claim the primary source supports. This is now a defect: the brief under-represents its primary source by omitting a material stated connection. See finding F3-new below.

### F9 — GTIG STOCKSTAY date (remediation: set GTIG date to 2026-06-25; § 7 note rewritten)
CONFIRMED CORRECT. GTIG article fetched this run; byline explicitly "June 25, 2026." Brief § 5 now says "GTIG published a full technical analysis of STOCKSTAY on 2026-06-25." § 7 now correctly states: "GTIG STOCKSTAY primary post is dated 2026-06-25; corroborating coverage (The Record, The Hacker News) is dated 2026-06-26. The brief cites the GTIG primary as 2026-06-25." Remediation correct; polarity in § 7 is now correct.

### F11 (advisory) — STOCKTRADER command count, cosmetic dates, Czech lure
CONFIRMED CORRECT. STOCKTRADER now "supporting 13 commands" — matches GTIG source. StrikeShark Securelist byline confirmed as 24 Jun 2026; brief shows 2026-06-24. Photo-ZIP lure languages now "Dutch, Danish and Japanese" — Microsoft source confirms these three; Czech appears only in account-naming context, not as a lure language. All F11 cosmetic fixes applied correctly.

---

## Cold read findings

### Citation does not support the claim

**F3 — Miasma UPDATE (§ 4): codfish/semantic-release-action link removed by iter-1 remediation, but the Socket primary source explicitly supports it.**

The current brief states only: "again carries the family's recurring `RevokeAndItGoesKaboom` dead-drop marker." This is technically true but materially incomplete given what the primary source says.

The Socket Security article (the primary Source for this item) states verbatim: "One of the strongest campaign-level markers is `RevokeAndItGoesKaboom`. This marker appears in the LeoPlatform/Miasma activity and in the codfish/semantic-release-action compromise documented by StepSecurity. In the codfish case, the malicious action searched GitHub commits for `RevokeAndItGoesKaboom` messages and used them as an operator token dead-drop channel."

The iter-1 F13 finding was incorrect about Socket not making this connection; the remediation based on that incorrect finding stripped a well-sourced claim. The brief should restore something to the effect of: "the `RevokeAndItGoesKaboom` dead-drop marker, which the Socket report traces back to the earlier codfish/semantic-release-action compromise (per StepSecurity analysis)." Classification: F3 (citation supports a claim the brief currently omits/understates, representing a regression). This is a truth-class finding because the brief currently presents an incomplete and misleading description of what the primary source says about the marker's significance.

### Surface contradiction

**F9 — Canvas/Instructure ransom payment: contradiction between Computer Weekly (paid) and Infosecurity Magazine + Instructure (agreement, unclear payment).**

The brief states: "Instructure paid an undisclosed ransom to have the stolen data destroyed" — presented as confirmed fact.

Sources say:
- Computer Weekly (primary): "Infrastructure gave in to ShinyHunters demands and paid an undisclosed sum of money to destroy the stolen data." Supports the claim (though with the "Infrastructure" OCR error).
- Infosecurity Magazine (additional source): "reached an agreement with the unauthorized actor" but "did not state whether money exchanged hands." Explicitly ambiguous.
- Instructure incident page (additional source, additional): "Instructure reached an agreement with the unauthorized actor involved in this incident. As part of that agreement: The data was returned to us. We received digital confirmation of data destruction." Does NOT confirm money exchanged hands.

Two of three sources either explicitly say the payment is unknown or do not confirm monetary payment. Only Computer Weekly says a ransom was paid. The brief states it as confirmed fact without any qualification. This contradiction should be surfaced in § 7 (or the brief should hedge: "reportedly paid an undisclosed ransom" citing Computer Weekly, noting Instructure's public statement does not confirm monetary payment). This is a factual accuracy concern since the claim influences how readers assess incident severity.

---

### Editorial / less-is-more flags (advisory)

**F11 — CyberScoop additional source for Signal (§ 1): date tag "2026-06-26" is wrong; the article is dated March 20, 2026.**

The brief line 18: "([CyberScoop, 2026-06-26](https://cyberscoop.com/fbi-cisa-issue-psa-on-russian-intelligence-campaign-to-target-messaging-apps/))"

CyberScoop article fetched this run is dated March 20, 2026 and covers the March PSA (PSA260320), not the June 26 PSA (PSA260626). The March article does not address the Backup Recovery Key tactic — that is a June-specific addition. The Backup Recovery Key claim is fully supported by the FBI IC3 primary source, so this is not an F3, but the date tag is incorrect. Advisory: correct the CyberScoop date to 2026-03-20 or find the June 26 CyberScoop article (if one exists).

---

### Missed angles

**F10 — The Gentlemen Switzerland coverage: Inside-it.ch article body unverified (403 in both runs).**

The brief's most Switzerland-specific claim in § 4 UPDATE — "Switzerland as the second-most-targeted European country" — rests solely on inside-it.ch, which returned 403 to both the iter-1 verifier and this iteration via WebFetch and bridge. The claim was read from the publisher's RSS summary only. This is correctly disclosed in § 7. No additional action needed, but this is the strongest CH-specific claim in today's brief and remains unverified at the source level. For the ops dashboard: suggested follow-up search: "Check Point Research Switzerland ransomware targeting 2026" to find if Check Point published the underlying data directly.

---

### Confirmations (no action)

- F3 Amazon Q fix version: 1.65.0 confirmed correct in Wiz + Register sources.
- F4 SANS ISC auditd: diary contains no auditd mention — brief is clean.
- F4 Gentlemen THN: date 2026-06-11 confirmed; in-window hook correctly is inside-it.ch.
- F9 GTIG STOCKSTAY date: 2026-06-25 confirmed; § 7 polarity now correct.
- F11 STOCKTRADER 13 commands: confirmed in GTIG source.
- F11 StrikeShark 2026-06-24: confirmed in Securelist source.
- F11 Photo-ZIP lure languages: Dutch/Danish/Japanese confirmed; Czech correctly not listed as lure language.
- Klue/Icarus: Lucanet and Link11 confirmed as EU victims in SecurityWeek source. ~24 victim count confirmed. Article dated 2026-06-26. Brief is accurate.
- SD-WAN Mandiant: evil_tenant.csv, troot, /etc/passwd confirmed in GTIG source dated 2026-06-24.
- STOCKSTAY architecture: MARKETMAKER, STOCKMARKET, STOCKBROKER, STOCKTRADER, WM_COPYDATA, RSA-4096, websocket-sharp, K1MORPHER, Render.com/Glitch, CVE-2025-8088 — all confirmed in GTIG source. Working hours 09:00–18:00 confirmed.
- Signal PSA: UNC5792, UNC4221, Backup Recovery Key tactic all confirmed in FBI IC3 source.
- No IOCs in brief (despite THN Windchill and GTIG STOCKSTAY sources containing IPs/hashes — brief correctly omitted them).
- § 7 single-source notes, § 2 inclusion gate note, contradictions note all present and accurate.

---

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 1)

Truth = F3 (Miasma/codfish link regression — primary source supports the connection; remediation incorrectly removed it). Editorial = F9 (Canvas ransom payment presented as confirmed fact; two of three sources do not confirm monetary payment; contradiction should appear in § 7). Advisory = F11 (CyberScoop Signal additional-source date tag says 2026-06-26, article is from 2026-03-20).

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: updates
  item: "UPDATE: Miasma / Mini Shai-Hulud npm worm — RevokeAndItGoesKaboom marker"
  url_or_quote: "again carries the family's recurring RevokeAndItGoesKaboom dead-drop marker"
  summary: "Regression introduced by iter-1 remediation. Socket primary source explicitly states: 'This marker appears in the LeoPlatform/Miasma activity and in the codfish/semantic-release-action compromise documented by StepSecurity.' The iter-1 F13 finding was incorrect. Brief currently omits the codfish/semantic-release-action link that the primary source supports. Restore the connection to the Socket-sourced claim."
- code: F9
  category: surface-contradiction
  section: active-threats
  item: "Canvas/ShinyHunters breach — Instructure ransom payment"
  url_or_quote: "Instructure paid an undisclosed ransom to have the stolen data destroyed"
  summary: "Computer Weekly (primary) says ransom was paid; Infosecurity Magazine says payment status unknown; Instructure incident page says only 'reached an agreement' and received data destruction confirmation — no monetary payment stated. Brief presents the claim as confirmed fact without qualification. Add § 7 contradiction note or hedge to 'reportedly paid' citing Computer Weekly, noting Instructure's statement does not confirm monetary payment."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Signal — FBI/CISA PSA (§ 1) CyberScoop additional source"
  url_or_quote: "[CyberScoop, 2026-06-26](https://cyberscoop.com/fbi-cisa-issue-psa-on-russian-intelligence-campaign-to-target-messaging-apps/)"
  summary: "CyberScoop article at that URL is dated March 20, 2026 (covers the March PSA260320, not the June PSA260626). Date tag in brief says 2026-06-26 — incorrect. The Backup Recovery Key claim is supported by the FBI IC3 primary; this is an advisory date-accuracy issue on the additional source. Correct date to 2026-03-20 or find the June 26 CyberScoop article."
```
