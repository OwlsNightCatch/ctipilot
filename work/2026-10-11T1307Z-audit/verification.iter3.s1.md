**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** see `verification.iter3.s1.started_at` / `.ended_at`

## Verification report — 2026-10-11T1307Z-audit (iteration 3, slice s1)

Scope: 10 entries (copy-fail, G7 NCSC, phpBB, TeamCity, Cisco Nexus, Acronis, The Gentlemen, ClosedQuorum, Flink, Citrix NetScaler), 197 ledger claims, all 197 answered (192 ok, 2 F13, 2 F4, 1 F5 as claim verdicts; see claims.yaml). Every cited page was fetched this iteration (cached bodies were not reused; one cached body existed and named a different URL).

### Prior-iteration deltas re-checked

| Entry | Prior finding | Remediation | Holds? |
|---|---|---|---|
| cisco-nexus-9000 | F11 internal record hides a wording correction | Declined | Holds. Diff is a few-word reword ("forces the device to reload" to "which could cause the device to reload"); docs/pipeline.md allows internal records for re-wording a few words; Cisco: "could cause the device to reload". |
| flink | F11 length | Declined | Holds as an editorial call (routine entry; actor, vector and transferable pivot are present). Not re-raised. |
| ncsc-g7 | F9 present-tense advice vs newest section | Past tense applied | Tense fixed, but the rewritten takeaway introduces a new F13 (below). |
| ncsc-g7 | F3 "took place" | "scheduled for 15 to 17 June" | Holds (page: "will take place from 15 to 17 June 2026", dateline 2026-06-01). |
| teamcity | F8 no main-analysis takeaway | Added | Holds (present, matches KEV ransomware flag and JetBrains indicators). |
| teamcity | F5 signing material | JetBrains wording, cited | Holds ("TeamCity data, configurations, and stored credentials ... integrity of build artifacts and downstream CI/CD pipelines"). |
| gentlemen | F4 summary Zerologon/MS17-010 | "leaves traces suggesting ... exploitation while expanding into the network" | Holds (Talos Phase 4 wording). |
| citrix | F5 reassurance uncited | Cited to CTX697096 | Holds ("14.1-73.37 and later releases", "13.1-64.23 and later releases of 13.1"). |
| citrix | F9 CCB affected range | Contradiction line | Holds; CCB lists "14.1 - 14.1-73.37" and "13.1 - 13.1-64.23"; line quotes it correctly. Minor F11 on wording below. |
| phpbb | F11 summary both scores | Applied | Holds; CNA (HackerOne) CVE records give 9.8 and 8, discoverer gives 9.4 and 8.3, heise 9.8 and 8.0. |
| acronis | F11 DirectAdmin fixed build | Applied, cited to Acronis | Holds (Acronis record: DirectAdmin plugin patched 1.2.3.238). |
| closedquorum | F11 length | Declined | Holds (not this fire's content). Not re-raised. |
| copy-fail | F4 record summary/fields | Corrected | Holds (no action claimed, `actions` not in fields, diff agrees). |
| copy-fail | F3 Detection "service or web accounts" | "unexpected accounts" | Holds. |
| copy-fail | F3 Ubuntu date | 2026-04-22 | Holds (page: "Publication date 22 April 2026"). |

### Analytical-link-as-fact

F13 #1 `entries/2026-06-03/ncsc-switzerland-warns-of-cyber-operations-around-the-g7-via.md`, Defender takeaway, Correction 2026-10-11T14:02:54Z and the record summary. The takeaway says "the warning's lasting lesson is the preparation it asked for ... DDoS mitigation playbooks staged in advance, MFA reviewed on customer-facing identity providers, administrative credentials rotated before the event window, and travelling staff briefed on mobile-device physical security", and the correction says "the pre-event preparations this warning recommended have lapsed". The NCSC measures PDF linked from the cited page (read in full via the jina reader) asks for: 2FA/passkey on remote access, prompt patching, offline backups, security.txt, business-continuity upkeep, an anti-DDoS solution, EDR/XDR, restricting access to exposed systems, log review, "regardless of the current threat situation". It names no credential rotation, no MFA review of customer-facing identity providers, no mobile-device briefing, no DDoS playbook. Those items are ZENDATA's advice to hotels, venues, transport operators and executives, and the original (pre-fix) text presented them as the entry's own advice. The iteration-2 rewrite moved them under the NCSC warning. Fix: attribute the list to the analyst or ZENDATA (or restate what NCSC asks), and drop "lapsed" for NCSC's baseline measures.

### Unsupported / hallucinated facts (all low confidence)

- F4 #1 `entries/2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce.md`, `sourcing_note`: "withholds the exploitation details". Neither JetBrains page says it withholds anything; this fire's Correction removes the same "withheld" attribution from the body.
- F4 #2 `entries/2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft.md`: "Command and control ran on the open-source AdaptixC2 post-exploitation framework"; Talos: "However, The Gentlemen may be using it in real-world attacks."
- F4 #3 `entries/2026-09-24/closedquorum-llm-orchestrated-c2-implant.md`: body quotes "the first publicly documented Windows implant to apply this model to tactical command and control" without Talos's "to our knowledge", while the title and the newest section treat it as hedged.

### Claims missing inline citation

F5 #1 teamcity, body paragraph 2 last sentence: "'all versions affected' plus 'no authentication' plus a widely deployed, easily fingerprinted product is a combination that historically closes quickly once someone reconstructs the path" (low confidence; uncited historical generalisation, not marked as judgement).

### Editorial / less-is-more flags (advisory)

- F11 #1 teamcity, Correction 2026-10-11T14:02:26Z last sentence: "The main analysis now closes with the current takeaway ..." is record-keeping narration (low confidence).
- F11 #2 citrix, Update 2026-10-11T15:11:46Z: "the entry follows Citrix, the vendor" refers to the entry itself (low confidence).

### Checked and found sound (no finding)

- Copy Fail: KEV `dateAdded` 2026-05-01, Ubuntu fixed 5.15.0-179.189 / 6.8.0-117.117, CERT-EU CVSS 7.8, Microsoft su wording, no credential-stuffing or "complementary" claim. RHEL part of the record summary ("RHEL kernel versions given were not the vendors' fixed builds") is not independently provable from the Red Hat page (it lists no fixed build); the Ubuntu half is verified and the old RHEL line cited one build for RHEL 8/9, so left unflagged.
- phpBB: CVE records, both scores, PoC date, no-workaround text, affected versions.
- Cisco: advisory text, CWE-1327 (present in the advisory HTML), ten PIDs, Not Vulnerable list, iACL/Live Protect text, TAC case, 1.0 release 2026-SEP-02.
- Acronis: JSON advisory SEC-10986 (three products, builds, CWE-276, published 2026-09-17), BleepingComputer and Help Net Security statements, KEV record.
- TeamCity: advisory, follow-up indicators, Cadence post (affected period, "should have been patched ... but it was not"), KEV (CWE-502, ransomware Known), CISA alert text.
- Flink: heise, NL Times, RETAIL-NEWS statements, figures, abuse-report/150-contacts sentence now correctly cited to heise.
- Citrix: CTX697096 table (CVSSv4 and CWEs), builds, watchTowr FAQ, CERT-EU/NCSC-NL/CERT.at same-day advisories, NCSC-CH post 13005 (published 2026-09-28), GTIG indicators, Unit 42 dates, CTX697174/CTX697191 builds, CCB PoC statement.
- Gambit date: JSON-LD says 2026-10-08, but the page's visible dateline is "September 22, 2026", which matches the citation (no finding).
- `updated_at`: Citrix equals its update record `at`; all other entries carry corrections/improvements only and leave it unchanged.

### Coverage
No missed angle named for this slice; the Citrix CCB proof-of-concept delta is captured.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 2)

### Findings summary (machine-readable)
See `verification.iter3.s1.findings.yaml`.
