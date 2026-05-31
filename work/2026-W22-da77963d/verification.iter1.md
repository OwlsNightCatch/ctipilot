**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8[1m]`) — env vars CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID unset; identity from runtime context
**Timestamps:** started_at=2026-05-31T22:29:57Z · ended_at=2026-05-31T22:33:18Z · duration_seconds=201

## Verification report — briefs/weekly/2026-W22.md (iteration 1)

Cold-reader weekly verification. 13 Source URLs fetched this pass (WebFetch + one fetch_source.py bridge). Truth gate prioritised the spawn-flagged items: §1/§3 CVE accuracy, §7 Gentlemen leak specifics, §7 Shai-Hulud Maven claim, §8 Swiss MSS deferral, §6 Check Point Q1 numbers, §5 Asocks count.

### Verified CLEAN (fetched, claim supported)
- **CVE-2026-0257 PAN-OS (§1/§3):** PAN PSIRT confirms pre-auth bypass, CVSS 7.8, "limited exploit attempts on unpatched PAN-OS devices." Rapid7 ETR confirms second wave 21 May, same actor via consistent MAC, and CISA KEV added 2026-05-29. Solid.
- **CVE-2026-35616 FortiClient EMS (§1/§3):** Arctic Wolf confirms active exploitation, EKZ Infostealer pushed via modified Remote Access Profile XML + on_connect PowerShell disguised as a Fortinet patch. Solid.
- **CVE-2026-26980 Ghost CMS (§1):** XLab confirms mass-compromise (700+ domains) chained into ClickFix infostealer delivery; blind/slug/9.4/GHSA specifics carried by the cited GHSA + BleepingComputer. Adequate.
- **Samba CVE-2026-4408 (§1/§3):** SAMR pre-auth RCE, CVSS 10.0, patched 4.22.10/4.23.8/4.24.3 — confirmed (but see F8 re config prerequisite).
- **Mini Shai-Hulud framework / wiper (§2):** SANS ISC diary 33016 confirms framework open-sourced 2026-05-22, trojanised Microsoft `durabletask` PyPI SDK with Linux wiper, 42 forged Sigstore badges. Solid.
- **The Gentlemen / Rocket leak (§7):** Check Point "Thus Spoke The Gentlemen" confirms Rocket backend leaked 2026-05-04 (account n7778, $10k), zeta88/hastalamuerte admin, SystemBC SOCKS5 1,570+ victims, Fortinet/Cisco edge + NTLM relay + OWA/M365 logs + GPO deployment, #3 globally. Strong. (KELA secondary cert-error transient; not failing.)
- **Check Point Q1 2026 (§6):** Blog confirms top-10 = 71% of victims, Qilin third consecutive quarter, Gentlemen reached #3, LockBit geographic diversification, published 2026-05-11. Solid.
- **BlackFile / UNC6671 (§7):** GTIG confirms AiTM-vishing, M365/Okta, DLS offline late-April → resumed 2026-05-11 "shutting down… under this name" → dark, probable-rebrand assessment, Session messenger. Strong (see F11 re sector/date nits).
- **ENISA NIS360 risk-zone list (§8):** 8 risk-zone sectors, gas exiting, railway/water newly entered — all confirmed (see F3 re high-maturity band).
- **Asocks 17M / 200 servers in NL (§5):** politie.nl confirms ≥17M devices and 200 NL-hosted servers verbatim (see F4 re the 'Asocks' name).

### Citation does not support the claim
**F3 — ENISA high-maturity band misstated (§8 ENISA NIS360).** Brief: *"Banking, electricity, telecom, trust services, aviation and financial-market infrastructures sit in the high-maturity band."* The ENISA analysis page places only **trust services, aviation and FMIs** in the high-maturity band; banking, electricity and telecom are in the **most-critical** tier, not high-maturity. Risk-zone facts are accurate. Fix the high-maturity sentence.

### Unsupported / hallucinated facts
**F4 — 'Asocks' name not in cited primary (§5).** politie.nl (bridge-fetched) confirms the numbers but never names the service 'Asocks' — it says only 'groot botnetwerk'. Confirm the name traces to NL Times (cited; could not re-fetch — cert-not-yet-valid transient) or attribute it to the reporting outfit rather than the police statement.

### Needs more research
**F8 — Samba 4408 config prerequisite omitted (§1).** The §1 framing "every unpatched Samba server exposes two unauthenticated RCE paths" overstates: CVE-2026-4408 (SAMR) requires a non-default config (`check password script` using %u AND `samba-dcerpcd` as a system service) per the Samba advisory. Add the prerequisite so responders scope correctly.

### Analytical-link-as-fact
**F13 — §7 Shai-Hulud Maven/Cargo claim unsupported by cited primaries.** Brief: *"Maven Central secondary poisoning via the `mvnpm` pipeline is now confirmed — one of the two un-hit registries flagged last week — while Cargo / crates.io remains un-hit."* Neither cited primary supports this:
- Wiz @antv article (fetched): @antv g2/g6/x6/l7 npm poisoning only — no Maven/mvnpm/Cargo.
- OX Security copycats article (fetched): npm copycat clones after the source leak — no Maven/mvnpm/Cargo.
This is load-bearing: it resolves a W21 watch item and § 10 lists "Maven Central now confirmed hit" as a closed carry-forward. Add a primary that documents the mvnpm/Maven poisoning, or downgrade to unconfirmed and reopen the watch. **Truth-class.**

### Editorial / less-is-more flags (advisory)
**F11 — two minor source-attachment nits.** (a) §2 Carnival: the 5.99M figure + four-brand framing is attached to "Carnival confirmed," but the PRNewswire notice carries neither (it confirms the social-engineering quote and passport/license exposure only). The figure plausibly comes from the cited Maine AG filing — confirm it traces there. (b) §7 BlackFile: GTIG page is dated 2026-05-15 (brief says 05-16) and does not name retail/hospitality as primary sectors (says NA/Australia/UK). Both minor.

### W-PD-1 / editorial gate
All H3 items answer a W-PD-1 question (inaction=incident in §1; cross-day pattern in §2/§4; strategic horizon in §6/§8). The §2 "AI tooling" synthesis genuinely earns weekly framing (five daily items no single daily framed whole). Primary-source strength is good throughout (PSIRTs, research labs, regulator filings, police statements). No vendor-marketing tells, no IOCs in prose, English throughout, no workflow-internal language. Single-source items are flagged in §10. The name-collision WARNs (GlobalProtect/FortiClient/ShinyHunters/Shai-Hulud) are benign same-entity reuse — no attacker/defender inversion found. No missed-angle gap material enough to flag.

### Transient / not-failed
scworld.com (SC Media, §7) and sysdig.com (§2/§3) re-check non-200 are transient (403/503) — both 200 OK in url-liveness ledger at run time; relevant, not failing. OSTIF BadHost (§3) and KELA (§7) returned transient 403 / cert-not-yet-valid this pass; both in ledger, not failing.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)

Truth = F3 (citation-not-supported), F4 (hallucinated-fact), F13 (analytical-link-as-fact). F8 is needs-more-research (editorial-class — but counted as advisory-adjacent depth; listed under editorial below). Advisory = F11.

Recount for the machine summary: truth=3 (F3, F4, F13), editorial=1 (F8), advisory=1 (F11).

### Findings summary (machine-readable)
See work/2026-W22-da77963d/verification.iter1.findings.yaml (identical payload).
