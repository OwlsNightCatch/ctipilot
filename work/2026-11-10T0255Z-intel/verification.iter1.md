**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-10T03:55:38Z · ended_at=2026-11-10T04:22:36Z · duration_seconds=1618

## Verification report — 2026-11-10T0255Z-intel (iteration 1)

Scope: all 10 entries (4 new, 6 updated), the run record, and the full claim ledger (252 claims; verdict rows in `verification.iter1.claims.yaml`: 233 ok, 6 F3, 2 F4, 1 F5, 1 F14, 9 unreadable). Every cited page was fetched this iteration except the OX Security post (403 on extract, url, WebFetch and jina) and the SonicWall PSIRT build table (script-built; absent from every capture). CISA 2026-11-09 and 2026-11-06 alert pages were read with WebFetch; the three quotes "based on evidence of active exploitation" are present. CISA KEV JSON, NCSC Security Hub posts 13054/13144/13155, ENISA EUVD (4 records) and the SAP CVE JSON were read directly. Prior coverage and cves_seen show no recycled material in the new entries; the N-able entry declares its two earlier entries in references[].

### Citation does not support the claim

- #1 F3 (low confidence) `n-able-n-central-33-unpatched-flaws-public-pocs-offline`, body para 1: "published technical write-ups and Python proof-of-concept code" cited to Huntress and BleepingComputer. Only Field Effect says "technical writeups, screenshots, captured output, and Python PoC code"; Huntress says "published the details ... to GitHub", BleepingComputer "proof-of-concept exploits". Cite Field Effect for that clause.
- #2 F3 (low confidence) same entry, Detection: "new technician or administrator accounts, password resets ..." cited to Huntress and Field Effect; neither names technician accounts or password resets (a password reset appears only in BleepingComputer's XXE-chain description, not cited here).
- #3 F3 (low confidence) `cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole`, Detection and the other OX-cited clauses: the OX post was unreadable on every rung. The same advice is on Alpine's advisory ("Look in /var/log/messages for sshd lines reading Accepted password for an account that has no password (alpine, root, or any key-only user)") and The Hacker News attributes it to Alpine. Cite Alpine (already in sources[]) for the detection, restart, fixed-package, container and 3.16 clauses; "OX scores the flaw CVSS 3.1 8.1" and "AWS and Azure images" rest on OX alone (GreyNoise's page shows CVSS 8.1 on NVD).
- #4 F3 (low confidence) same entry, body para 2 and Update 2026-11-10: "against one of its own deliberately exposed sensor hosts, not a customer system" attributed to GreyNoise. The tracker says "an attacker exploited a vulnerable GreyNoise gridpoint" and "we have confirmed vulnerable gridpoints deployed"; it never says "sensor hosts", "deliberately exposed" or "not a customer system". Reasonable gloss, but the "no compromised production host" conclusion leans on it.
- #5 F3 `bluephishing-entra-agent-blueprint-consent-phishing-poc`, title, summary, body para 1, sourcing_note: "Inherited permissions are not visible in the Entra portal or in Microsoft Graph". Proofpoint relays this: "According to Microsoft documentation, inherited permissions are not visible in the Entra portal or via Microsoft Graph, and only observable in the token contents at runtime", and its own testing says "silent inheritance of permissions from the blueprint principal to the agent identity was only observed for delegated permissions"; admin-consent grants showed "inherited from parent" and Figure 9 lists the agent identity's User.Read.All and Group.Read.All. The entry presents it as Proofpoint's observed behaviour (sourcing_note: "the observed permission behavior"). Attribute to Microsoft documentation and carry the caveat; "every user can soon create blueprints" is Message Center's "default Microsoft Entra users".
- #6 F3 (low confidence) `cve-2026-19868-sonicwall-sonicos-sslvpn-saml-mfa-bypass-kev`, body para 2 and cves[].affected: hardware-family and NSv-model lists (TZ, NSa, NSsp; NSv 270/470/870; XS/S/M/L) could not be verified; the PSIRT table is script-built. Versions 7.3.3-7015, 8.2.2-8015, 7.3.4-7013 and 8.2.3-8015 are confirmed by BleepingComputer.

### Unsupported / hallucinated facts

- #7 F4 (low confidence) N-able sourcing_note: "The researcher's repository holds working exploit code". Censys: "no source has validated the proof-of-concept code"; the same sourcing_note says no source validated the flaws. Say "proof-of-concept exploit code".
- #8 F4 `cve-2026-116606-barracuda-esg-auth-bypass-root-rce`, headline: "Barracuda confirms exploitation of its no-login chain to root". Barracuda says only "We have identified exploitation activity affecting a small number of organizations" (no flaw, no chain); the entry's body and sourcing_note say "without naming the flaw". Only the Canadian Cyber Centre names CVE-2026-116606, on unnamed open-source reporting.
- #9 F4 (low confidence) `danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack`, body: "The attacks reached healthcare cold storage." Uncited, and it ties the 2026-11-02 blood-service incident to "the attacks" while the paragraph ends "None of these sources names Danfoss, Copeland or Dixell equipment for the blood-service case"; the French attribution covers only 11 to 12 October.

### Quantifier without source

- #10 F14 (low confidence) N-able, body para 2: "The same product had three separate flaw waves earlier in 2026" cited to Field Effect, which says "several significant N-central security events" and lists two bullets covering four CVE ids; Huntress groups five CVEs under two months.

### Claims missing inline citation

- #11 F5 `ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig`, Update 2026-11-10: "The operator planted five JSP webshell families ... also in Linux-style and decoy directories." has no citation; Huntress supports the five families and calls the path spread its inference ("suggests the exploit was not designed for a specific operating system ... simply tried every likely location").

### Drop (low relevance / off-audience / duplicate)

- #12 F7 (low confidence) `sap-november-2026-cna-records-four-unauth-cvss-10-rows`: patch-day CVEs published hours before SAP's regular cycle, no exploitation, no public PoC, no readable fixed releases. The run's own rule is that a routine patch-cycle CVE with high CVSS alone does not qualify. Keep only if exposure-driven urgency for Swiss SAP estates is stated in one clause.

### Needs more research

- #13 F8 (low confidence) Ahsay Detection: the run's diff removed Huntress's Sigma-rule mention, WinRing0 command lines, Horizon3's request-level artifacts (FromServlet field, X-RSW-Request headers) and the "404 unless a parameter is supplied" tell; all are still supported by Huntress and Horizon3, and the record summary says only that the detection text "carries the new behaviours".
- #14 F8 (low confidence) OpenSSH body: the rewrite dropped NCSC's caveat that other software with similar authentication paths may be affected ("The root cause appears to lie outside OpenSSH, likely at the libc level, so other software using similar authentication paths may also be affected"), without the record summary saying so.

### Missed angles

- #15 F10 `cve-2026-116779-freeswitch-sip-message-api-command-execution` (not updated this run): summary says "the exploitation claim is the vendor's alone"; CISA added CVE-2026-116779 to KEV on 2026-11-09 (KEV JSON dateAdded 2026-11-09, alert "based on evidence of active exploitation") and cves[].status lacks cisa-kev. The run record treats the row as COVERED, but this is a sourcing and status change that needs an update record. Query: CISA KEV 2026-11-09 SignalWire FreeSwitch CVE-2026-116779.
- #16 F10 (low confidence) Danfoss sourcing_note cites "Reuters, as relayed by NBC News" but NBC is not in sources[], and the same article (fetched) reports "the Paris prosecutor's office said it had requested international arrest warrants against the leader of Shahid Kaveh ... and his two deputies", which the entry omits.
- #17 F10 (low confidence) GPUStack CVE-2026-102895 (KEV 2026-11-09: unauthenticated administrative access, persistent admin API-key creation, secret disclosure, code execution) was dropped on an assumed footprint; consider two routine sentences or keep the drop. Query: GPUStack CVE-2026-102895 exploited.
- Coverage otherwise looks complete: no Swiss public-sector incident or exploited edge CVE in the window was found beyond what the run covers (searches for Swiss administration incidents and an N-able hotfix update found nothing newer; Patch Tuesday and SAP Patch Day publish after the run clock).

### Action-item discipline

- #18 F18 (low confidence) N-able actions[1]: restates the Detection paragraph and Defender takeaway (log review, endpoint review, rotation) and is conditional ("where activity looks unauthorised"). Keep actions[0].

### Editorial / less-is-more flags (advisory)

- #19 F11 Barracuda Update 2026-11-10: "The earlier statement that no source reports attacks no longer holds." refers to wording no longer in the entry; delete.
- #20 F11 Publica Update 2026-11-10: "The fund's own notice is not linked; Inside IT's report of its statement is the source." is record-keeping narration; delete or move to sourcing_note.
- #21 F11 (low confidence) IBM: event_date 2026-11-09 vs primary source dated 2026-11-07; Exposure says "on Linux" though IBM's affected table lists no platform.
- #22 F11 (low confidence) SAP: the four links are raw ENISA JSON API responses; the human-readable page https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-120700 exists (fetched for one id). The API form has precedent.
- #23 F11 (low confidence) entity linking: IBM and BluePhishing `entities: []`, SAP omits product:sap-gateway, N-able omits product:n-able-n-central, although the run record lists the new product keys.
- #24 F11 Danfoss: "Cyber-Electronic Command" (summary, body) vs "electronic and cyber centre" (section) for one unit, the former attached to a ministry citation that uses "centre électronique et cyber"; the summary rewrite also dropped unrelated clauses (Pentagon, CISA fact sheet, Coop, BACS) while the record summary mentions only the attribution.
- #25 F11 (low confidence) N-able: BleepingComputer dates publication to late 2026-11-08, Censys dates the PoC release to 2026-11-09; the entry spans both with no Contradiction line.

### Checks that passed (not findings)

Fetched and confirmed: IBM bulletin (CVSS 9.8, 5.0.0 to 5.0.19, 5.0.19 PL1, no workaround) and CISA KEV text; SAP four records (CVSS 3.1 10.0 vectors, note numbers, version lists; component grouping matches the CVE JSON order); Barracuda advisory timeline, patch ids, Mandiant records, watchTowr chain, CCCS update; SonicWall PSIRT text, workaround and revision date; OpenSSH release notes, NCSC 13155 (last edited 2026-11-06, exploitation unknown), Alpine fixed-package table, GreyNoise sessions (00:46:51 UTC on 2026-11-07, doas, authorized_keys, apk add python3, 150 s poll, "enrollment never succeeded"), CCCS AV26-1130; Huntress AhsayCBS follow-up, Horizon3, Ahsay announcement; French foreign ministry statement (French original in `original:` is verbatim, translation faithful), CERT-FR CTI-009 content (broken PDF text still carries the indicators), Sekoia, NCSC 13054; Inside IT Zug article, IPCT letter, Publica/BPK/PKZH/Post pages; Proofpoint (JSON-LD datePublished 2026-11-09 and visible dateline match the entry date). Record types and updated_at mirrors are correct; sections match record summaries; no IOCs, em dashes or workflow vocabulary in reader-facing text; classification blocks are present and within vocabulary; no org_triage or watchlist use. Run-record notes are consistent with the files (4 new, 6 updated, KEV dispositions, registry additions).

### Verdict

NEEDS_FIXES (truth: 10, editorial: 8, advisory: 7)

### Findings summary (machine-readable)

See `work/2026-11-10T0255Z-intel/verification.iter1.findings.yaml` (25 records).
