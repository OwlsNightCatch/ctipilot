**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T05:57:22Z · ended_at=2026-11-07T06:20:42Z · duration_seconds=1400

## Verification report — 2026-11-07T0256Z-intel (iteration 5)

Scope walked: all 236 ledger claims (12 changed, every claim of the three remediated entries and of every other entry; the run record's notes read in full). Every claim has a row in verification.iter5.claims.yaml (230 ok, 6 F3 low confidence).

### Prior-iteration deltas (iteration 4 findings, re-verified against live pages)

1. Cisco SEG ECS precondition (F8): PR 22024 .diff carries 'URL Filtering and URL Retrospective Service must both be enabled.' and the scenario 'which has the URL Filtering and URL Retrospective Service features enabled for inbound mail'; Cisco's advisory says 'regardless of device configuration'; the section, cves[CVE-2026-76461].affected and the record summary now state both. PR 22024 merged 2026-11-05T19:41:01Z and PR 22018 merged 2026-10-28T01:47:42Z (page state read in this iteration). Confirmed fixed.
2. Cisco clean-grep caveat (F8, low confidence): PR 22024 'the ECS SQLi (i.e. this module) was the only one that generated this matching IOC'; PR 22018 doc 'appears to be CVE-2026-76443 rather than CVE-2026-76461 based on the IOCs available'. actions[1], immediate_action and the record summary now carry the caveat; the body Triage line does not (finding #3 below).
3. WordPress 2.7 (F9): Picus 'affects WordPress 2.7.0 through 7.1.3' and '2.7 through 4.6 did not receive a fix'; The Hacker News 'goes back to WordPress 2.7'. The Exposure line now says 'which Picus counts as affected back to 2.7'. Confirmed fixed (cves[].affected still carries Wordfence's 4.7 to 7.1.3, which the Exposure line sets against Picus; acceptable).
4. Brotli Cisco table (F3, low confidence): summary and fixed text now say the Cisco table is combined and not tied to one CVE; headline, title, affected text and Exposure line still assert the Brotli flaw reaches Cisco Duo and RoomOS (finding #1 below).
5. Run record Updates bullet (F4): now names both modules, 2026-11-05, poc-public and the unchanged absence of a fixed 16.0 build. Confirmed; the Contradiction bullet still says 'the module' (finding #6).
6. Brotli takeaway (F11): Cisco alone is credited with 'not aware of malicious use'; the three OpenScape workaround articles are named (Mitel table: SBC KB000129100, SESAP KB000129034, Contact Center KB000129114; Xpert, Endpoint Management and MiVoice Business 'Planned update'). Confirmed fixed.
7. Cisco tags (F11): poc-public is in tags and the record's fields. Confirmed.
8. Run record iteration-3 F8 summary: whole sentence restored. Confirmed.

### Citation does not support the claim

**#1** `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo` (headline, title, cves[CVE-2026-111497].affected, Exposure line, affected_products (claims 022f4ea785, c0809790f0, 9839bd780e)): (low confidence) Residual of iteration-4 F3. https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u covers four CVEs (CVE-2026-111497, -105482, -105483, -106069) in one 'Impacted Products with Software Fixes' table with no CVE column ('Duo Network Gateway 3.4.2', RoomOS 'On-premises: 11.41.2.3 26.7.4.3'); the page says the bug IDs carry platform-specific information and never states that Duo Network Gateway or RoomOS bundle the Brotli decoder. The remediation hedged the summary ('without saying which of its CVEs each fix addresses') and the Cisco fixed text ('not tied to one CVE'), but the headline and title still assert the Brotli flaw reaches Cisco Duo and RoomOS, cves[].affected and the Exposure line still list them as affected by this CVE, so the entry contradicts its own summary. Fix: word headline, title, affected and Exposure as 'Cisco lists Duo Network Gateway and RoomOS in its combined Node.js and Brotli advisory' (or drop Duo and RoomOS from the Brotli-specific affected text).

**#2** `2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole` (update 2026-11-07T03:52:19Z, summary, record summary, evidence[] Previdian quote (claims b48d66b6c9, 231d797fff, d6b5cc41a7)): (low confidence) https://previdian.com/CVE-2026-123158, fetched in this iteration, now says 'Previdian sensors have observed 15 exploitation attempts, 10 unique attacker IPs, and 8 countries ... First observed Nov 06, 2026; last observed Nov 07, 2026' (page 'Updated 07 Nov 2026'). The composer's saved body and the earlier iterations read 14 / 9 / last observed 2026-11-06, so the figures were right when read and the live counter has moved; the update section, entry summary, record summary ('all on 2026-11-06') and the evidence quote ('14 exploitation attempts, 9 unique attacker IPs') no longer match the cited page. Fix: give the figures an 'as read on 2026-11-07' qualifier (or refresh to 15 / 10 and 'last observed 2026-11-07'); it is a live counter, so the qualifier matters more than the number.

### Needs more research

**#3** `2026-09-15/cve-2026-76461-cisco-secure-email-gateway-sqli-root-rce` (body **Triage:** line (residual of iteration-4 F8 #2)): (low confidence) The remediation added the clean-grep caveat to actions[1], immediate_action and the record summary ('a clean result does not rule out the S/MIME injection, which did not leave that pattern in the module author's reproduction'; PR 22024: the ECS SQLi 'was the only one that generated this matching IOC'), but the Triage line the finding named and the new body section carry no such sentence. The Triage line is read field by field by triage agents, and the section only implies the point. Fix: append one clause to the Triage line (or the section) that a clean mail_logs result does not exclude use of the S/MIME injection.

### Editorial / less-is-more flags (advisory)

**#4** `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo` (tags and cves[CVE-2026-111497].status vs summary): (low confidence) The summary and body say CISA lists the flaw as exploited ('based on evidence of active exploitation', CISA alert of 2026-10-27, KEV record read this iteration), yet status carries no 'exploited' and the tags carry no 'actively-exploited'. The two sibling entries on the same CVE (2026-10-24 node2shell, 2026-10-26 Microsoft .NET) carry [exploited, cisa-kev ...] and 'actively-exploited'. A machine consumer filtering on those fields misses this entry. Fix: add exploited and actively-exploited, or leave as is if the omission is deliberate because Cisco reports no malicious use against its products (then say so in sourcing_note).

**#5** `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo` (summary, Cisco clause): Reads as if the Duo Network Gateway and RoomOS fixes are dated up to 2027. In the Cisco table Duo Network Gateway 3.4.2 and RoomOS on-premises 11.41.2.3 / 26.7.4.3 carry no date; the dates (November 2026 to July 2027, for example Catalyst Center 3.4.1 July 2027) belong to other products, as the body says correctly. Fix: 'lists Duo Network Gateway (3.4.2) and RoomOS among its products with fixes, a longer list of which is dated up to July 2027'.

**#6** `2026-11-07/cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo` (body **Defender takeaway:** first clause): The relative clause 'where Common Configurator runs' sits after 'Desigo CC host', so it reads as if Common Configurator ran on Desigo CC hosts; Common Configurator is an Industrial Edge application (SSA-443410), and 'remove the Industrial Edge Management Applications' is not scoped to the one application Siemens attaches the uninstall mitigation to. Fix: split into two sentences, one for Desigo CC and one for Industrial Edge instances that run Common Configurator.

**#7** `runs/2026-11-07/2026-11-07T0256Z-intel.md` (Verification & coverage notes, 'Contradiction handling' bullet): Second half of iteration-4 F4 left over: the Updates bullet now names both modules, but this bullet still speaks of 'the module' in the singular, while the entry's sourcing_note says Cisco 'does not say which flaw either module uses' and the ECS module maps to CVE-2026-76461 only at the author's medium confidence. Fix: 'either module'.

**#8** `2026-11-07/file-system-access-api-browser-persistence-chrome-edge` (regions: [global, switzerland]): (low confidence) Nothing in the entry's title, summary or body ties the technique to Switzerland; the only Swiss element is the publisher (Oneconsult AG). A region filter will surface a global browser technique as Swiss-specific. Fix: [global], or add the stated Swiss nexus to the body.

### Checked, no finding

- Cisco SEG (37 claims): every clause of the 2026-11-07 section against PR 22024 (page, .diff, raw HTML mergedTime), PR 22018 (page, .diff), the Rapid7 wrap-up of 2026-11-06 (lists only the S/MIME module, as the entry says), Cisco's two advisories (rev 1.2, hardening rev 1.1) and the KEV record (dateAdded 2026-09-14, forensicTriage Yes). Evidence quotes are literal substrings.
- WordPress (31 claims): Picus, The Hacker News, Wordfence, Patchstack, WordPress.org, Wordfence Intelligence, CISA alert, Canadian Cyber Centre; the partial-package nuance, 403-before-update advice and .htaccess caveat match Picus; 2026-11-01 and 2026-11-04 sections unchanged and correct.
- Brotli (18 claims): Siemens SSA-045512 and SSA-443410 (CSAF and HTML tables: six fixed Industrial Edge applications, Common Configurator no fix, Desigo CC V8/V9 .NET remedy), Mitel MISA-2026-0010 rev 5.0 (versions, KB ids, 8.1, note 1), Cisco v1.8, CISA alert of 2026-10-27.
- New entries SonicWall (PSIRT API JSON: seven CVEs, CVSS 7.1 vector, affected and fixed builds, no workaround; CISA alert; BleepingComputer), BOSSAI (Acronis TRU; Hermes Agent harness supports the registry relation), Kaspersky (Securelist), Oneconsult (datePublished 2026-11-02; Oz), Aargau (ag.ch communiqué, originals literal; Netzwoche), TUM (notice status 06.11.2026 12:20; heise) and the updated Danfoss (NCSC hub post 13054 edit reason, Ransom-ISAC, Unit 42), IoT2050 (SSA-834709 V1.1, CERT-FR, NCSC-NL, VulnCheck), ARTEX (Microsoft 2026-11-06, Check Point) all verified against pages fetched in this iteration. OX Security's page answers 403 on every transport; its post was read from OX's own feed (url --direct https://www.ox.security/feed/).
- Style: no em dash outside `## <Type> — <at>` headings, no IOCs, no pipeline vocabulary in any entry; every entities[] key resolves in the registry; priorities and Admiralty codes consistent with the sources.
- Dedup: no prior-coverage record for Aargau, TUM, BOSSAI, Mitel, Desigo, Oneconsult, Cambodia/Storm-3358, Proxmox; SonicWall SSLVPN not covered (only the GMS entry of 2026-11-05, a different product); the Brotli entry declares both older Brotli entries and adds vendor tables they lack.
- Missed angles: none found. The KEV additions in the window (CVE-2026-19868 only; Apple CVE-2024-27834 and WordPress earlier and covered) and the run's borderline-drop list are consistent; two WebSearch sweeps found no dated in-window item the run lacks. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 1, advisory: 5)

All three non-advisory findings are low confidence and small: two are residuals of earlier findings (Brotli Cisco wording, Cisco Triage caveat), one is live-counter drift on Previdian's page. Fixing them is a few clauses.

### Findings summary (machine-readable)

See work/2026-11-07T0256Z-intel/verification.iter5.findings.yaml (8 records).
