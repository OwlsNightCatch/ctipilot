**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-15T05:11:58Z · ended_at=2026-07-15T05:19:42Z · duration_seconds=464
**Self-telemetry:** webfetch_calls=5 · websearch_calls=0 · bridge_fetches=6 · urls_checked=14

## Verification report — 2026-07-15T0409Z-intel (iteration 3)

Cold read of all four new entries + run record. Prior-iteration deltas re-verified first, then a full independent truth/editorial pass. Ground truth: local CSAF mirror (icsa-26-195-01..04), MSRC OData mirror (4 CVEs), and live fetches of Rapid7, Proofpoint, The Register (jina), GBHackers (jina), and all four CISA advisories (bridge).

### Prior-delta re-verification (both confirmed holding)
- **iter2 F4 (Rockwell 3.011 fix):** CONFIRMED corrected. CSAF icsa-26-195-04 remediations: `vendor_fix — update to 1715-AENTR ... version 3.011 and later`; CVSS v3.1 10.0; affected ≤3.003; CWE-306. Entry now reads fixed=3.011, status=[patch-available] throughout title/headline/summary/body/cves[0]/tags/takeaway/action. No residual "no fix / no-patch" language. CISA page evidence quotes verbatim ("Successful exploitation of this vulnerability could allow an attacker to read or delete files...", "No known public exploitation specifically targeting this vulnerability has been reported to CISA at this time.").
- **iter2 F5 (Proofpoint uncited hardening claim):** CONFIRMED removed. No "all cloud apps CA still applies regardless of client_id" claim remains. The retained point — application-scoped Conditional Access is the control bypassed — is source-supported ("Spoofed client IDs won't trigger CA policies that are scoped to a specific application"). "Block ROPC grant type" is sound analyst inference entailed by the mechanism (technique relies on ROPC), not an uncited source-fact.
- **iter1 deltas (ABB affected/fixed 4.0-24→4.0-25; xAI citation split; Rockwell CVSS-vector note):** all independently re-verified holding. ABB CSAF: known_affected=4.0-24, fixed=4.0-25 for all four CVEs. xAI home-dir/SSH claim now on The Register (which supports it); GBHackers supports the core exfiltration finding.

### Unsupported / hallucinated facts
- **F4 — microsoft-july-patch-tuesday-sharepoint-dynamics-followup — CVE-2026-55040 "public PoC" contradicted by cited source.** The Rapid7 primary (the PoC author) states: "Microsoft requests a 30 day stay on disclosure of technical details and publication of PoC" and "Rapid7 will be publishing full technical details for CVE-2026-55040 within 30 days of this disclosure" (exception only for ITW exploitation / third-party disclosure). So as of 2026-07-15 there is NO public PoC — it is embargoed. Yet the entry asserts a public PoC in four places: title ("a SharePoint pre-auth JWT bypass with a public PoC (CVE-2026-55040)"), summary ("Rapid7 published a PoC..."), cves[0].status ([poc-public, patch-available]) and tags ([...poc-public...]); action[0] also says "breaks Rapid7's public Pwn2Own chain". The body prose never claims a public PoC ("still-undisclosed RCE"), so the frontmatter/title/summary overstate both source and body and inflate urgency (poc-public is a triage-signalling status). Fix: drop poc-public from cves[0].status (leave [patch-available]) and from tags (taxonomy has no poc-private variant); reword title/summary/action[0] to a Pwn2Own-demonstrated chain whose PoC is under a 30-day embargo. Priority `high` still holds after correction (pre-auth Dynamics 365 deserialization RCE "Exploitation More Likely" + SharePoint auth-bypass, patches available).

### Everything else verified clean
- **CVE/CVSS/version truth:** All four MSRC CVEs (55040 9.1 SFB/CWE-1390; 55944 9.8 RCE/CWE-502 pre-auth AV:N/AC:L/PR:N/UI:N; 50522 & 58644 9.8 RCE, base PR:N but FAQ "attacker authenticated as at least a Site Owner" — post-auth classification correctly source-grounded and flagged in sourcing_note) match the OData mirror. All CISA/CSAF facts (Rockwell 10577; ABB T-MAC 14771–14774 scores/CWEs/vectors incl. stored-XSS per CSAF description, adjacent-network DoS, PR:L post-auth split; Edgenius Copy Fail CVE-2026-31431 fixed 3.2.4.1; 800xA CVE-2025-13162 CVSS 4.4 DLL search-path) verified. ABB researcher attribution "Angelo Catalani / Italian National Cybersecurity Agency (ACN)" confirmed in CSAF document acknowledgments.
- **Evidence quotes:** All verbatim-contiguous against fetched pages (CISA Rockwell x2; Rapid7 exploit-chain quote; Proofpoint blank-app-name + fragmentation quotes; MSRC Dynamics deserialization; The Register "Grok Build packages entire repos and uploads them as Git bundles..." and Musk "all user data ... completely and utterly deleted").
- **Dedup / update_of:** update_of target 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days exists; none of 55040/55944/50522/58644/10577/14771 appear in 14-day prior coverage; genuine delta (base covered 56155/56164). ESET UEFI duplicate correctly dropped.
- **Classification (Admiralty):** all four present, in-vocab, consistent (CISA A/2; Microsoft A/2; Proofpoint B/2; xAI B/2). No org_triage, no watchlist (correct — none configured).
- **Single-source flag:** CISA batch verification=single-source-national-cert with sourcing_note (F12 satisfied). Others multi-source.
- **Priority / relevance:** CISA notable, Microsoft high, Proofpoint notable, xAI notable — all calibrated. xAI incident clears the breach bar on transferable AI-coding-CLI governance lesson + concrete credential-rotation action, not victim-framing. Proofpoint 2026-07-13 recency exception documented and legitimate (72h developing window, not previously covered).
- **Action items (F18):** all concrete and finding-derived; no generic advice, no padded lists (max 2). Empty where appropriate.
- **Style:** no IOCs, English throughout, no workflow-internal language. URLs all resolve (GBHackers 403 to routine UA is anti-bot only; jina confirms a real 2026-07-14 article).
- **Coverage completeness:** no nameable in-window relevant omission; documented drops (law-enforcement items, D1R debunked leak claim) are defensible.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "microsoft-july-patch-tuesday-sharepoint-dynamics-followup — CVE-2026-55040 'public PoC'"
  url_or_quote: "title 'with a public PoC (CVE-2026-55040)'; summary 'Rapid7 published a PoC'; cves[0].status [poc-public, patch-available]; tags poc-public; actions[0] 'public Pwn2Own chain'"
  summary: "Rapid7 primary states the PoC/technical details are under a 30-day embargo ('Microsoft requests a 30 day stay on disclosure of technical details and publication of PoC'); no public PoC exists at composition. Drop poc-public from status+tags; reword title/summary/action to a Pwn2Own-demonstrated, embargoed-PoC framing. Body never claimed public PoC, so frontmatter overstates source+body."
```
