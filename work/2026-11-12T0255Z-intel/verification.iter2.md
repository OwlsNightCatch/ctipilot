**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-12T05:12:55Z · ended_at=2026-11-12T05:38:48Z · duration_seconds=1553

## Verification report — 2026-11-12T0255Z-intel (iteration 2)

Scope: post-fix pass. All 48 claims of claims.changed.iter2.yaml, every claim of the 12 entries touched by iteration-1 remediation (6 new, plus the Chrome, Certighost, PHP2Shell, Fortinet, Brotli and Publica updates), and a sample of the unremediated eMudhra and IoT2050 entries (their new sections in full plus 18 and 14 claims of the rest). 313 claim rows in verification.iter2.claims.yaml: 305 ok, 8 flagged (F3 x4, F4 x4). Pages were re-read from the gate's cached bodies and, where a page could change or the cache was lossy, live (Fortinet PSIRT pages, Siemens ProductCERT tables, Cisco, Mitel, Huntress, BleepingComputer, Edge release notes, Trend Micro advisory raw HTML, Debian tracker, Red Hat errata, GitHub advisories, KEV, MSRC API).

### Iteration-1 deltas: what I re-checked and what the sources say

| Iter-1 finding | Source now says | Remediation |
|---|---|---|
| PHP2Shell F3 (Download Center vs readmes) | Download Center rows carry only 'Critical Patch English | 2026-11-11' and 'This Critical Patch applies to Apex One Service Pack 1'; Apex Central readme: 'Apex Central is affected by PHP2Shell ... upgrades the PHP module to build 8.2.35'; Apex One readme: 'updates the PHP module to version 8.2.35 to protect against a potential security issue' and 'resolves a potential Remote Code Execution security issue', no PHP2Shell | Correct in headline, summary, actions[0], section and record summary. Residual: cves[].fixed not hedged (finding 3). |
| Chrome F3 / F9 | Extended Stable 156.0.8078.100 page (dated 2026-11-11): 72 security fixes, four Critical rows, no XML row; Stable .78/.79: 83 fixes, five Critical, no XML row; Extended page 0910980127 still lists High CVE-2026-125346 (572578603) and High CVE-2026-125350 (582442907) separately, Stable page shows both bug ids under CVE-2026-125350 | Correct; the disagreement is now stated. |
| Certighost F3 x3, F8 | CybersecurityNews: DCSync 'enabled' by the access, PoC 'available on GitHub'; Kaspersky: 'authenticate as the domain controller account'; researcher names appear only in the gist and GitHub URLs; interim step in the article is certutil plus 'Restart-Service CertSvc -Force' | F3 fixed. F8 interim step added but incomplete (finding 8). |
| Plone F3 | Plone post: 'with current AI tools it may not take long to turn them into a working exploit' | Correct. Sourcing note CVSS claims for the four sibling GHSA advisories verified (9.1 PR:H x3, plone.restapi 4.7 moderate). |
| ScreenConnect F3 / F8 / F14 / F11 | Huntress: server returns 'an encryption key, initialization vector, and a salt value', 'decryption values the script will use'; BleepingComputer live text has the tags quote and the July script | UUID, 'in every reported case' and references fixed. The F8 addition introduced a new defect (finding 2). |
| Publica F3 / F11 | cybercrimepolice.ch is conditional ('könnten Kriminelle ... nutzen'); Publica page 'Stand: 10.11.2026' says 'allgemeine Erpresserschreiben', no demand received, no darkweb indication; Publica 'Stand: 11.11.2026' is a no-change note; watson 2026-11-11 and SRF 2026-11-10 match the section | Correct; summary now 104 words, three sentences. |
| Brotli F4 / F11 | SSA-242944: 15 products, Brotli-disable for all, IIS rule on UMC and TIA Administrator, fixes for WinCC OA V3.20 and BRAUMAT/SISTAR; SSA-678870: 28 products, Teamcenter/Opcenter KB-gated, HyperLynx/PADS/Xpedition firewall block, five products with none, 8 not-affected rows; Cisco advisory live at 1.11 (2026-NOV-10) | actions[1], body, update section and record summary correct; the structured fixed field is still unscoped (finding 4). |
| GSocket F4 / F11 / F17 | Microsoft ATT&CK section maps T1090.002, T1564.001, T1222.002, T1036 (exec -a), T1070.004/.006; msft-ti is B in sources.json | Correct. |
| Apache F4 / F5 | RHSA-2026:98981 and :98978 ship mod_http2-2.0.26-7.el9_9.1 and mod_http2-2.0.29-5.el10_3.1 and fix CVE-2026-119618; project page names no fixed mod_h2 | Correct; detection line labelled as inference. |
| Fortinet F4 / F14 | I fetched FG-IR-26-176 to -290: every Critical row published 2026-11-10 is in the entry (19 CVEs, all CVSS, version tables, workaround and virtual patch verified); the self-contradicting-summary pattern appears on -202, -207, -216, -219, -277 | Correct. |
| Falcon F14 / F15 | Unit 42: 'We have no evidence of any instances affected outside of the target country'; no CrowdStrike or Jewelbug statement | Wording fixed; the edit left stray text (finding 14). |
| CCB F11 | CCB: 'phone number + one-time code, no password'; no statement on how codes were obtained | Correct. |
| Word bound (Publica 1100, eMudhra 895) | unchanged | Declined for this fire; recorded as carried advisory. |

### Citation does not support the claim

F3 #1 (2026-11-12/screenconnect-sckit-toolkit-pushed-to-hundreds-of-endpoints, claim ee2bf993a8): "Huntress says sequential attacker-assigned tags suggest other MSPs were compromised earlier, and a batch script first uploaded on 2026-07-25 searches for one of its two rogue client IDs" ([BleepingComputer]). BleepingComputer: "BleepingComputer found an earlier malicious batch script that references one of the rogue ScreenConnect client IDs listed by Huntress", "Huntress declined to comment on the specific July incident", "The relationship between the July malware activity and the current ScreenConnect attacks remains unclear." The script is BleepingComputer's finding, and the unclear link is dropped. Attribute it and add the caveat.

F3 #2 (low confidence, Fortinet, claim 32feb7f499): CVE-2026-126157 grouped as an "IBE webmail" flaw; FG-IR-26-209 says "gain access to other users' secure email accounts", no IBE.

F3 #3 (low confidence, Falcon summary ecb6a834d2): "does not know how the operator reaches the pages"; Unit 42 only says "We are currently unaware of how an operator is deploying these browser extensions."

F3 #4 (low confidence, GSocket 87d038d36a): "Microsoft attributes to exposure"; Microsoft says "Exposure is the more likely factor".

### Unsupported / hallucinated facts

F4 #1 (2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root, headline): "VulnCheck saw Node-RED exploitation on Siemens IoT2050". VulnCheck: "(Note that VulnCheck Canaries have not observed exploitation of this vulnerability in Siemens products.)"; the entry body: "The target was a canary, not a Siemens device". The headline was rewritten this run, so it is in scope.

F4 #2 (low confidence, PHP2Shell cves[].fixed x2): Apex One build 20113 listed as the fix with no hedge; its readme names no flaw or CVE.

F4 #3 (low confidence, Brotli cves[].fixed): mitigation parenthetical not scoped to the SSA-242944 products; five SSA-678870 products have no mitigation.

### Needs more research

F8 #1 (Certighost actions[0] / takeaway): add 'Restart-Service CertSvc -Force' and the staging warning ('any legitimate workflows relying on the chase fallback will break') that the cited page gives with the certutil command.

F8 #2 (low confidence, Apache): omit-reason for RHEL 9/10 'Important': Red Hat says each HTTP/2 stream uses a separate allocator, 'which substantially increases the complexity of exploiting the flaw'.

F8 #3 (low confidence, Brotli actions[1]): the 'no fix' product list omits COMOS Walkinside, Project Server Web Administration Tool, WinCC Companion, Profiling Tool (SSA-242944) and Process Preparation X (SSA-678870).

### Missed angles

F10 (low confidence): KEV additions of 2026-11-09/10 with no store coverage: CVE-2026-20320 (Cisco BroadWorks XXE, unauthenticated), CVE-2026-102895 (GPUStack, unauthenticated admin and code execution), CVE-2026-111793 (Openwave Webtop Media Transcoder). They pre-date this run's window. Otherwise coverage looks complete: kev_window_diff shows no in-window additions, the Fortinet 2026-11-10 release is covered to the last critical row, and the search sweep (exploited-vulnerability news of 11-10/11, Swiss incident news) found nothing else uncovered (SonicWall CVE-2026-19868, Apple CVE-2024-27834, AhsayCBS are all in the store).

### Org-triage line missing / inconsistent

F16 (low confidence): Apache CVE-2026-119618 at notable; see findings file.

### Action-item discipline

F18 (low confidence): Brotli actions[1] and Certighost actions[0] restate body guidance as compound task lists.

### Editorial / less-is-more flags (advisory)

F11: (1) Falcon body line 61 carries a stray 'paloaltonetworks.com/falcon-c2-browser-compromise/))' fragment and 'the Jewelbug entry's extension'; (2) eight registry keys added this run (product:plone and seven Siemens products) are linked from no entry, and several existing keys are not linked (Apache, Entra ID, ScreenConnect, Roundcube); (3) eMudhra summary 278 words, main analyses of eMudhra (895) and Publica (1100) over the 550 bound (carried); (4) Fortinet's 2026-11-12 record is a correction although it adds ten new critical rows and a no-fix status, so the entry does not re-float; (5) Certighost 'full' and 'working' PoC adjectives unsourced; (6) Chrome update section ends on composition narration.

### Checked and clean

Chrome update (Stable .78/.79 83 fixes and five Critical, Extended .100 72 fixes and four Critical, Edge for Android 157.0.4341.53, newest Edge desktop 157.0.4341.42 of 2026-11-05, KEV date 2026-11-10); PHP2Shell update section (Download Center dates, readme quotes, advisory last updated 2026-11-04 with ETAs Nov. 11, Nov. 12, Nov. 17, KEV dates 2026-10-26); IoT2050 update (SSA-834709 V1.2, eight rows, Example Image no fix); eMudhra update (Mozilla bug: cessationOfOperation on 7 Nov 2026, last G2C certificate 3 Nov 2026, independent review 04-Dec-2026, G1 issuance to stop before 16 Nov); Publica update; CCB, Plone, GSocket, Apache, Falcon and ScreenConnect body claims other than the flagged ones; Fortinet's 19 cves[] records; Siemens, Mitel and Cisco facts in the Brotli entry; all references[] targets exist; updates[] records match the entry_record.py diff field sets and updated_at mirrors; no em dash or workflow vocabulary in reader-facing text; classification letters match sources.json tiers; the run record's file claims hold (the six stray root files exist, registry additions and candidate sources match).

### Verdict

NEEDS_FIXES (truth: 7, editorial: 6, advisory: 6)

The two findings that must be fixed before publish are F4 #1 (IoT2050 headline contradicts VulnCheck and the entry's own body) and F3 #1 (ScreenConnect clause misattributes BleepingComputer's July script and drops the 'unclear' caveat); the Falcon stray fragment and the Certighost restart omission should go in the same edit. The rest are low-confidence or advisory.

### Findings summary (machine-readable)

See work/2026-11-12T0255Z-intel/verification.iter2.findings.yaml (19 records, same content).
