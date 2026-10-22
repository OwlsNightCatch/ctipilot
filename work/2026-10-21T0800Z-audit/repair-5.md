# repair-5 report (cleanup wave 02, 2026-10-21T0800Z-audit)

Batch: `work/2026-10-21T0800Z-audit/batch-5.yaml`, 16 entries. Records written: 10 (8 improvement with section, 2 internal improvement). Entries without a record: 6. No W1-F hunks exist for any entry in this batch. No entry carried `legacy_duty: true`. Fetched bodies: `work/2026-10-21T0800Z-audit/repair-5/src/`; record texts: `repair-5/e*-summary.txt`, `repair-5/e*-section.md`.

## Per entry

### 2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat
- Record: improvement, `2026-10-21T08:08:29Z`, fields `body, sources, sourcing_note`, with a section.
- Applied: the three Red Hat sources[] dates and all 8 inline labels moved from 2026-09-19 (the update date) to each page's own public date: 2025-09-05, 2025-10-13 and 2026-06-01 (`public_date` with the "Public on" label on each access.redhat.com/security/cve page; all three carry `field_cve_exploit_known: true`). The fixed-release sentence now says that CISA's catalog record names each CVE's stable fix commits and that each kernel.org ChangeLog carries the matching commit. I checked all 17 ChangeLogs: each has the branch's stable commit and the upstream commit listed in the KEV `notes`, and none contains the CVE id. The sourcing note was swept the same way. Ground truth: https://access.redhat.com/security/cve/cve-2025-39682 (and -39964, -53266), https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json, https://thehackernews.com/2026/09/cisa-flags-three-linux-kernel.html ("updated ... as of September 19, 2026").
- Declined: `cves[CVE-2026-53266].affected`, because 2026-10-11T1307Z-audit already fixed it (the range includes 7.0 through 7.0.13).

### 2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10
- Record: improvement, `2026-10-21T08:09:24Z`, fields `body, sources`, with a section.
- Applied: the uncited no-exploitation sentence in the 2026-09-29 Update section now cites Oracle's advisory and the CISA KEV catalogue "as of 2026-10-20". KEV catalogVersion 2026.10.20 lists none of the entry's 50 ids. Oracle's page has only its generic boilerplate about exploitation attempts and no per-CVE exploitation status. The KEV catalogue is added to sources[] (date 2026-10-20). Ground truth: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json, https://www.oracle.com/security-alerts/cspusep2026.html.

### 2026-09-21/afpa-third-party-accommodation-tool-data-extraction
- Record: improvement, internal, `2026-10-21T08:10:54Z`, fields `body`.
- Applied: the three inline labels now read "Cyberattaque.org, updated 2026-09-19" and "FrenchBreaches, updated 2026-09-19" (an existing store label form). sources[] dates stay at 2026-09-19 because the cited facts (AFPA's confirmation, 1.7 million) are in the 09-19 updates. The pages were published on 2026-09-15 (Cyberattaque.org, `Published Time`) and 2026-09-16 (FrenchBreaches `datePublished`, plus "Mise à jour le samedi 19 septembre" and `dateModified` 2026-09-19). Ground truth: https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/, https://frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8.

### 2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence
- Record: improvement, `2026-10-21T08:11:55Z`, fields `body, summary, techniques`, with a section.
- Applied: the "most novel component" superlative in the summary and main text is now attributed: "A Huntress researcher deemed that second payload ... the most interesting", quoting the recap "deemed the second payload the most interesting" verbatim. Added T1543.003, T1547.004, T1547.001 and T1053.005 (all active in pin v20.0) for the NetSupport persistence the body describes: service and Winlogon from the write-up, Run key and reinstalling scheduled task from the recap. Ground truth: https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows, https://www.huntress.com/blog/defcon-phishing-google-doc-malware.
- Declined: removal of T1546.015, because 2026-10-11T1307Z-audit already removed it. Its proposed replacements are the mappings applied above.

### 2026-09-21/nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync
- No record. Declined: T1027, because 2026-10-11T1307Z-audit already dropped it.

### 2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft
- No record. Both findings are declined because 2026-10-11T1307Z-audit already fixed them: the live-DC contrast is gone from the headline, summary and body, and the "appear to have", "traces suggesting" and "traces indicating" hedges are restored. The AdaptixC2 sentence matches Talos ("we found that The Gentlemen uses the open-source AdaptixC2 framework for command-and-control (C2) operations") and keeps the "may be using it in real-world attacks" clause.

### 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
- Record: improvement, `2026-10-21T08:13:06Z`, fields `summary`, with a section.
- Applied: the summary's last sentence is limited to SentinelLabs' sample. It now says Zscaler's ROOFDECK tries the local configuration, then the RSA-signed Pastebin dead drop, and uses Nostr metadata only as a fallback "to locate the current dead-drop Pastebin URL" (quote verified). Ground truth: https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver, https://www.sentinelone.com/labs/dont-call-us-well-call-your-apis-tradertraitor-backdoors-resurface-on-victim-with-no-crypto-ties/.

### 2026-09-23/austria-nisg-2026-bcs-transposition
- No record. W1-E item 7 stays declined on principle: removing an entry is outside the lifecycle, and relevance framing is the profile's call. W1-E item 11 stays declined: the 2026-10-11 section restates the takeaway, which is redundancy rather than a reader-facing error, and the record is append-only.

### 2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal
- No record. W1-E item 14 is declined because 2026-10-20T0835Z-audit already fixed it: the 2026-10-04 section now reads "Check Point's second indicator at the time (... as sk1000171 then listed it)".

### 2026-09-23/cve-2026-93952-arista-velocloud-orchestrator-exploited
- Record: improvement, `2026-10-21T08:14:45Z`, fields `actions, body, cves, immediate_action, summary, title`, with a section.
- Applied: the body now says "exposed" instead of "affected" and states that Arista lists the affected releases by version alone. `cves[].affected` keeps the version ranges and gives the certificate-based Edge authentication condition as a separate sentence. "Unrelated" is dropped from the July-flaw sentence (THN: "a different VCO flaw"). The section also notes that as of 2026-10-21 Arista still lists fixes only for the 5.2 and 6.4 trains, so the actions and the immediate_action remain valid. Em dashes removed: title, summary, actions[1], cves affected, body (3), plus the immediate_action title, which was not in the list but is reader text. Ground truth: https://www.arista.com/en/support/advisories-notices/security-advisory/24765-security-advisory-0183, https://thehackernews.com/2026/09/new-cvss-100-velocloud-orchestrator.html.

### 2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes
- No record. Declined: the "staging"/"within hours" overstatement survives only in the append-only 2026-09-25 record summary. The section bodies say "servers connected to the operation", and the 2026-10-11T1307Z-audit Correction already gives Computing UK's narrower wording ("repeatedly rebuilt"; no time given).

### 2026-09-23/virtualizor-billing-hook-unauth-root-rce
- Record: improvement, `2026-10-21T08:17:11Z`, fields `body, cves, sources, sourcing_note`, with a section.
- Applied: `cves[].cvss` is restored from VulnCheck's per-CVE CNA advisories as CVSS 4.0 scores of 9.3, 9.2 and 8.7 (the advisory URLs were found in the EUVD records' references, EUVD-2026-84620/84622/84624, and were not constructed). The three advisories are added as sources. CVE-2026-43643 is now stated as CWE-862 in the advisory and CWE-639 in the blog table. The 2026-09-30 Correction's "and are no longer shown" is cut, so it now says only that the blog page lacks scores. The sourcing note names the advisories. Ground truth: https://www.vulncheck.com/advisories/softaculous-virtualizor-os-command-injection-via-billing-module-handler, https://www.vulncheck.com/advisories/softaculous-virtualizor-php-object-injection-via-billing-module-handler, https://www.vulncheck.com/advisories/softaculous-virtualizor-authorization-bypass-via-billing-module-handler.
- Declined:
  - The CVSS 3.1 values (9.8/8.1/7.5) appear only on the CVE record, which the brief says cannot be cited.
  - The gadget-chain wording was already fixed by 2026-10-11T1307Z-audit.
  - The CISA SSVC "Exploitation: poc" value: only the CVE record's CISA-ADP container carries it (EUVD has no SSVC field), so it cannot be cited.
  - W1-E item 18 stays declined on principle (relevance framing; not a reader-facing error).

### 2026-09-24/microsoft-entra-id-sspr-enumeration-resetspy
- Record: improvement, `2026-10-21T08:18:20Z`, fields `body, headline, summary`, with a section.
- Applied:
  - The headline no longer claims ResetSpy enumerates admin status, and it is now 115 characters (it was over 120). The section lists the tool's four outputs and explains that likely admins are inferred from the policy state.
  - The takeaway is reworded: scoping limits method disclosure to in-group accounts and administrators but does not stop existence enumeration. The phishing-resistant-MFA clause now follows LevelBlue ("this cannot be disabled"; a strong factor raises the cost of exploitation) rather than "removes the value".
  - Em dashes removed: summary (2), body (5).
  - Ground truth: https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal.
- Declined: "alone" and "very likely", already fixed by 2026-10-11T1307Z-audit.

### 2026-09-24/openai-agent-australia-medicare-portal-breach
- Record: improvement, `2026-10-21T08:20:00Z`, fields `body, sources`, with a section.
- Applied:
  - The 2026-09-27 Update section no longer calls the ACSC alert a "formal, government-level response" or says its pattern "matches it closely". It now says the alert names no organization, and that Cyber Daily reports the ACSC gave no further information on the incident or where it occurred.
  - The ACSC source is now dated by its own page, "Published 25 Sep 2026": the sources[] date and 5 inline labels moved from 2026-09-24 to 2026-09-25, and the 24 September date is attributed to Cyber Daily.
  - The "internal file names and aggregate health statistics" detail is moved from Albanese's account to OpenAI's statement.
  - The section clarifies the 2026-09-26 record summary: The Record says the agent "may not have needed to find a workaround at all" and that no activity logs were released.
  - Ground truth: https://www.cyber.gov.au/alert/risks-of-ai-misalignment-to-australian-organisations, https://www.cyberdaily.au/security/14225-alert-australian-cyber-security-centre-issues-warning-over-ai-misalignment-risks, https://www.cnn.com/2026/09/23/business/australia-openai-agent-hack-intl-hnk, https://therecord.media/openai-australia-breach-cyber.

### 2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim
- Record: improvement, internal, `2026-10-21T08:20:43Z`, fields `cves, evidence, sources`.
- Applied: `cves[0].affected` is now "Oracle PeopleSoft Enterprise PeopleTools 8.61 and 8.62 (Updates Environment Management component, PSEMHUB)". Oracle's Security Alert is added as a source (2026-06-10) and bound by the verbatim evidence quote "PeopleSoft Enterprise PeopleTools, versions 8.61, 8.62". Ground truth: https://www.oracle.com/security-alerts/alert-cve-2026-35273.html.
- Declined:
  - The present-tense FBI non-confirmation in the 2026-09-27 section: 2026-10-11T1307Z-audit already re-attributed it to BleepingComputer's recap of the first response.
  - The 2026-09-29 record summary: it is append-only, and the 2026-09-30 Correction already records the disputed "confirmation" and motive wording.
  - The CyberScoop citation on the DiMaggio/Kaiser sentence: already added by 2026-10-11T1307Z-audit.

### 2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209
- No record. Declined: "where possible" is already in the summary and body (fixed by 2026-10-11T1307Z-audit).

## Gate results
- `check_run.py --all`: no FAIL on batch entries. The only lines naming them are the expected "run_id '2026-10-21T0800Z-audit' does not resolve to a run record" warnings, one per record. The store-wide FAIL (`cve-sync` CVE-2026-92438, ninja-forms entry) is on another worker's entry.
- `--page-checks-since 2026-10-21` (`repair-5/page-checks.txt`): no `quote-literal` or `citation-cve` line on batch entries. The one `quote-literal` warning is on 2026-09-17/cve-2026-58704 (not in this batch).

## State changes for the main agent
- `state/cves_seen.json`: bump `last_seen` to 2026-10-21 for these changed CVE records:
  - CVE-2026-93952 (Arista; affected text)
  - CVE-2026-43641, CVE-2026-43642, CVE-2026-43643 (Virtualizor; cvss restored)
  - CVE-2026-35273 (ShinyHunters entry; affected text)
- `entities/registry.yaml`: no changes.

## Residuals noticed outside the findings (nothing fixed)
- austria-nisg-2026-bcs-transposition: the 2026-09-30 Correction quotes the German word "strafbar" with an English gloss rather than as a marked translation.
- openai-agent-australia-medicare-portal-breach: sources[] publisher "ABC News (Australia) — exclusive, Cam Wilson" contains an em dash.
- oracle-september-2026-cspu-five-unauthenticated-cvss-10: the sourcing note's "No exploitation reporting or KEV listing exists" is an undated negative claim.
- the-gentlemen-open-directory-vhdx-backup-ntds-theft: the body says the upload went "to Wasabi cloud storage"; Talos writes "cloud storage services such as Wasabi".
- shinyhunters-fbi-peoplesoft-breach-claim: the 2026-09-27 section still ends "no party has confirmed or denied either technical claim" in undated present tense.
- virtualizor-billing-hook-unauth-root-rce: VulnCheck's three advisory descriptions read "before 3.2.9 (Patch 9) and 3.0.0", an odd CNA string the entry does not reflect; the CNA's CVSS 3.1 scores stay unshown because only the CVE record carries them.
