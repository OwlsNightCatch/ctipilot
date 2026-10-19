**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T16:27:20Z · ended_at=2026-10-19T16:50:38Z · duration_seconds=1398

## Verification report — 2026-10-11T1307Z-audit (iteration 4, slice s3)

Scope: 27 entries, 286 ledger claims (20 changed since iteration 3, every claim of the remediated entries, a random quarter of the rest). All 286 have a verdict row in `verification.iter4.s3.claims.yaml`: 283 ok, 2 F4, 1 F3. Every cited page was fetched this iteration (extract, raw HTML for CVSS scores and dates, `pdf` for the NCSC measures document, `cisa-kev`, `ncsc-csh post`, the CERT-Bund CSAF JSON, the Curia Vista OData URL with its full query string). One page no direct rung could read (OX Security, HTTP 403 and jina challenge, WebFetch 403) was read from the gate's cached body `quote-bodies/4d3caf5c02b02df7.extract.txt` (dated 2026-08-04, fetched 2026-10-11).

### Prior-iteration deltas (all 19 checked against disk and source)

Landed and holding:
- NCSC G7 F13: the takeaway now attributes NCSC's baseline (second factor or passkey, 24-hour patching of critical internet-facing flaws, offline backups, anti-DDoS, EDR/XDR, restricted access) to its measures PDF, which says each of those and says "regardless of the current cyberthreat situation"; the credential-rotation and MFA-review steps sit with ZENDATA, which has both. The correction no longer says preparations lapsed.
- nginx: the summary says "versions per depthfirst"; the Exposure clause cites depthfirst.com/nginx-rift, which carries "unnamed regex capture ... followed by another rewrite, if, or set directive"; "UNKNOWN, Proof of Concept Available" is verbatim in NCSC-CH post 12575.
- MRSProxy: summary drops NTLM and coercion; the body relay clause states Franky's wording; MB VRED carries the PetitPotam and captured-hash material and is attributed.
- Entra SSPR: the Detection line quotes LevelBlue's status string "user is not member of the password reset users group" and its bulk-enumeration pattern; the two error codes are in LevelBlue's wording without quote marks.
- Mandiant: title, summary and headline describe attacks, failures and assessments; the case-study sentence says "Mandiant presents as observed in its own work" with a citation (the report intro: "frontline field observations from Mandiant and GTIG"); event_date is 2026-09-16 (Help Net Security).
- ShieldBreak: the evidence list now holds MSRC's "Microsoft has released an update ... addresses the vulnerability identified by CVE-2026-69414"; the 08-18 and 08-21 takeaways point to the shipped fix.
- Liechtenstein: the headline and main takeaway no longer carry the Swiss/EU administrator nexus; the 08-05 and 09-02 sections drop it or mark it analyst judgement; the 500,000 figure is the Federal Council's estimate as NZZ reported it in June 2025 ("rund 500 000 Aktiengesellschaften, GmbH, Genossenschaften und Stiftungen sowie auch gewisse Vereine"); the Inside IT date 2026-10-06 matches the visible dateline "6. Oktober 2026" (JSON-LD datePublished 2026-10-07 is a republish stamp).
- Cisco ISE 20181: releases earlier than 3.1 are named in the main text, Exposure and cves[] (Cisco: "Earlier than 3.1 | Migrate to a fixed release."), but see finding #3 below.
- ChainDrop F11: partly applied only; see finding #12.

Declined, rationale checked: ShieldBreak F11 (file-name indicator), Liechtenstein F11 (three takeaways, em dashes), Cisco ISE F7. Findings #12 to #15 and #7 restate them with the reason the rationale does not hold.

### Citation does not support the claim

**F3 #1** `cve-2026-93616-check-point-security-mgmt-path-traversal` (claim a2e02f92c9) — body: "Check Point published no fix for the end-of-support trains older than R81.10, and upgrading is the only remediation for them ([Bishop Fox, 2026-10-01])".
- Bishop Fox: "The fix ships in Jumbo Hotfix Accumulator R82.10 Take 45, R82 Take 127, R81.20 Take 170, and R81.10 Take 192, and in the R82.20 Security Hotfix. Every earlier take is affected, as are R82.20 and all of R80 through R81 (end of support)." No statement on missing fixes or on upgrade being the only remediation. sk1000171 lists no fix for R80 to R81 but does not say that either.
- Fix: cite sk1000171 and say it lists no fix for R80 to R81, or drop the "only remediation" clause.

### Unsupported / hallucinated facts

**F4 #2** `cve-2026-93616-check-point-security-mgmt-path-traversal` — body, cves[].fixed, immediate_action (low confidence). After this fire removed "(all takes)" from R82.20, the entry lists R82.20 as affected with only "the R82.20 Security Hotfix" as its fix. sk1000171: "The fix is also included in: Jumbo Hotfix Accumulator for R82.20 starting from Take 10 ...". An R82.20 host on that accumulator reads as unpatched. Fix: add the R82.20 accumulator from Take 10 to the fixed list.

**F4 #3** `cisco-ise-cve-2026-20181-cve-2026-20190-an-unauthenticated-c` (claim 628115e224, low confidence) — Correction section: "CVE-2026-20181 requires valid administrative credentials and affects releases from 3.1"; headline "across ISE 3.1 to 3.5". Cisco table: "Earlier than 3.1 | Migrate to a fixed release. | Not vulnerable." (columns CVE-2026-20181 | CVE-2026-20190). The main text and Exposure line were fixed; the newest section and headline were not. Fix: say 3.1 to 3.5 plus earlier releases with no fix.

**F4 #4** `instructure-canvas-extortion-330-institutions-across-six-cou` (claim 09b88d6cc1, low confidence) — record summary "44 confirmed Dutch institutions ... appear nowhere" and Correction "No source supports the earlier figures of ... 44 confirmed Dutch institutions". NL Times 2026-05-05 (same outlet the entry cites): "The Dutch impact affects 44 universities, applied sciences universities, and secondary schools across the country, according to a list of victims shared on the dark web by the hacking group ShinyHunters, which was reviewed by BNR." The unsupported part is SURF confirming 44, not the figure. Fix: reword as an actor claim.

**F4 #5** `cve-2026-42945-nginx-...` — event_date 2026-05-15 (NCSC-CH post date) against the primary depthfirst/F5 date 2026-05-13 that the body itself gives (low confidence).

**F4 #6** `cisco-ise-cve-2026-20181-...` — event_date 2026-06-18 against Cisco's advisory dated 2026-06-17 (summary and sources[0] say 06-17) (low confidence).

### Drop (low relevance / off-audience / duplicate)

**F7 #7** `cisco-ise-cve-2026-20181-...` (low confidence, standing) — the declined rationale answers length, not check 11. The entry calls itself "a patch-cycle item", Cisco knows of no exploitation, one flaw needs administrator credentials, no sourced constituency nexus.

**F7 #8** `glpi-certfr-2026-avi-0551-...` (low confidence) — seven post-authentication flaws, "No source reports exploitation", "a standard patch-cycle upgrade", no sourced nexus after the audit removed the unsourced deployment claim.

**F7 #9** `n8n-prototype-pollution-chain-...` (low confidence) — five flaws each needing an authenticated workflow editor, no exploitation, already routine.

**F7 #10** `pentagon-dmdc-military-personnel-data-breach-unencrypted-ssn` (low confidence) — US military breach, no vector/class/actor (the body says so), no constituency nexus, generic "encrypt at rest" lesson, body still three sentences plus takeaway and three dated sections; no stated out-of-nexus ground (check 5, 5b).

### Needs more research

**F8 #11** `cve-2026-42945-nginx-...` (low confidence, claim 9e91d9ddb3) — cves[].affected and .fixed are null although nginx.org ("Not vulnerable: 1.31.0+, 1.30.1+ ... Vulnerable: 0.6.27-1.30.0") and the body give them.

### Editorial / less-is-more flags (advisory)

**F11 #12** `chaindrop-shai-hulud-...` sourcing_note — still carries "Each number is attributed to the vendor that published it rather than merged into a single total. Elastic's write-up carries the fuller execution-chain and C2 detail." Only "and is used as the primary" was removed (git diff).

**F11 #13** `shieldbreak-defender-...` — "nothing here supersedes what the original entry carried" (08-18), "the compensating control named in the earlier coverage" (08-18), "The prior entry had the identifier and Microsoft's rating but not how the chain works" (08-21); the file-name indicator decline rests on "append-only", but only updates[] record summaries are append-only (CLAUDE.md allows revising earlier sections in place).

**F11 #14** `cve-2026-20212-...` and `cve-2026-93616-...` — internal records that change reader-facing body text carrying a factual claim ("forces the device to reload" to "could cause"; "R82.20 (all takes)" to "R82.20").

**F11 #15** em dashes in reader-facing text across Liechtenstein (3/6), ChainDrop (3/9), ShieldBreak (2/46), Exchange (1/15), Mandiant (1/17), Entra (2/5), nginx (2/2), plus the Nexus and CHOSEN BRICK titles; Mandiant keeps six inline ATT&CK ids in prose; Liechtenstein keeps three coexisting takeaways.

### Missed angles / coverage

None raised. This slice is existing entries; no in-window omission can be evidenced from it.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 5, advisory: 4)
