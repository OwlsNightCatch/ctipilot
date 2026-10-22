**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T11:14:01Z · ended_at=2026-10-22T11:44:59Z · duration_seconds=1858

## Verification report — 2026-10-21T1148Z-audit (iteration 1, slice 3 of 3)

Scope: 23 updated entries, 510 ledger claims (495 ok, 11 F3, 3 F4, 1 F14 rows in verification.iter1.s3.claims.yaml; every claim has a row), the run record and the wave report. No new entries in this run. First pass (no deltas block). Page bodies: cached truth-pass/repair bodies where complete; fetched fresh this pass: Grafana post, SLCyber (dateline), The Record, Security Affairs, Paperjam, Huntress, Learn remediation page, vm2 GHSAs (5), Red Hat CVE pages (4) and RHSAs (2), the Keycloak issue and release notes, Drupal PSA and risk-levels page (WebFetch, because the container is challenged on drupal.org).

**Fold check (Drupal).** Read whole against `git show base:entries/2026-05-20/prepare-emergency-drupal-patch-window-for-today-17-00-21-00.md`. Nothing sourced that the duplicate carried is lost: PSA and NCSC Security Hub sources, the 17:00-21:00 UTC window, the "within hours or days" quote and the all-branches/EOL patch-file scope are in the survivor; the duplicate's "second-highest tier", "no technical mitigation pre-patch" and Swiss/EU/university exposure claims are contradicted or unsupported and were corrected in the survivor, not lost. Only the duplicate's NCSC evidence quote and its `regions`/`sectors` values (switzerland, europe, public-sector, education; unsourced) were not carried. `merged_from` is on the survivor's 16:06:42Z record; the duplicate id is referenced nowhere but that record and the legacy queue.

**Run record and wave report (checked on disk).** Hold: 74 updated ids all present with exactly one record from this run (68 corrections, 6 improvements); 25 priority moves, all downward (20 high to notable, 3 notable to routine, 2 high to routine); six kind changes as described; 64 Exposure, 53 Detection, 14 Triage lines; `actions[]` empty and Admiralty block and Defender takeaway on all 74; no changed field undeclared in any record and `updated_at` untouched; seven new non-product entities plus 39 product entities, 39 summaries rewritten, 12 relations (all listed ones present); `cves_seen` 21 added (13 vm2, 3 Nextcloud, 2 Ivanti, 33827, 43494, 47100) and 68 `last_seen`/20 title/3 primary-URL changes; legacy queue pending 330, reviewed 145, folded 2; truth-pass tallies (405 ok, 374 F4, 108 F3, 127 F5, 57 F13/F14, 5 unreadable = 1,076), token sums, durations and commit ids (bca18bd, 5a2e81b, base 7e74158) all reproduce; the table rows for the 23 entries match their records. One imprecision (F11 below): "400 ATT&CK ids" is 400 mappings, 173 distinct ids. Placeholders in the Verification and Tracker delta sections not reported, as instructed.

Coverage (F10): none to add for this slice; the run already logs the CVE-2026-41940 gap.

### Citation does not support the claim / unsupported facts / quantifiers (truth class: F3, F4, F14)

- #1 F3 | calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and | Correction 2026-10-21T20:43:20Z (claim cfe8e26f82)
  quote: JFMBackdoor offers TCP proxying and screenshots rather than SOCKS5 and self-removal ([PwC, 2026-05-21])
  PwC says JFMBackdoor supports "remote shell access, file system operations, network proxying, screenshot capture, and self-removal capabilities" and lists "Self-Management: ... uninstall itself for anti-forensic purposes"; the clause denies a capability the cited page states. Fix: drop "and self-removal" (keep the SOCKS5 contrast only if a source supports it).
- #2 F3 | storm-2949-sspr-to-key-vault-azure-kill-chain | Body, Azure control plane paragraph (claim 3695d229cb)
  quote: ...read dozens of secrets within four minutes, then used them to take over the primary production web app and change its password
  Microsoft hedges: "Among these secrets, we believe the threat actor found credentials that enabled them to access the application they coveted the most"; the entry states the takeover as fact. Restore the hedge ("Microsoft believes").
- #3 F3 | storm-2949-sspr-to-key-vault-azure-kill-chain | Body, Virtual machines paragraph (3350cc7f83) and Correction (1a10bf5851)
  quote: "A Run Command PowerShell script then disabled Defender Antivirus protections ... and cleared event logs" / "weakened Defender Antivirus and cleared event logs"
  (low confidence) Microsoft writes "The script attempted to weaken Microsoft Defender Antivirus by disabling several protections" and "attempted cleanup actions"; hedge dropped (its detections table does list "Event log was cleared", so the log clearing is arguably supported).
- #4 F3 | cve-2026-45829-chromadb-python-fastapi-server-pre-auth-rce-v | Body, first sentence (claim f9d1fe1220)
  quote: HiddenLayer discovered CVE-2026-45829 ("ChromaToast") ... maximum CVSS 4.0 score of 10.0 ([BleepingComputer, 2026-05-19])
  BleepingComputer says only "It received the maximum severity score from HiddenLayer, the company that discovered it"; neither "ChromaToast" nor "CVSS 4.0" appears on that page (both are on the Hadrian page). Move the citation or add Hadrian to this clause.
- #5 F3 | webworm-china-aligned-shifts-to-eu-government-targets-echocr | Correction 2026-10-21T20:41:34Z (claim 025eb49c6a)
  quote: FishMonger (also called Aquatic Panda), SixLittleMonkeys and Space Pirates are not other names for Webworm ... ([ESET, 2026-05-20])
  (low confidence) The ESET page links Webworm to SixLittleMonkeys and FishMonger but never says "Aquatic Panda"; that alias is on the Hacker News page ("FishMonger (aka Aquatic Panda)"). Cite THN for the alias.
- #6 F4 | keycloak-26-6-2-16-cves-including-oidc-session-fixation-cve | summary (claim e34b516f34)
  quote: Red Hat build of Keycloak fixes them in 26.2.16 and 26.4.12
  (low confidence) "them" = CVE-2026-7507 and CVE-2026-37982. RHSA-2026:19594 (26.2.16) lists CVE-2026-7507, -7307 and -7504 only; CVE-2026-37982 is only in RHSA-2026:19596 (26.4.12). Body and cves[] are precise; the summary is not.
- #7 F3 | cve-2026-41091-microsoft-defender-engine-link-following-eop | Body, first paragraph (claim 6ef078714c)
  quote: The researcher Nightmare Eclipse, who published the RedSun and UnDefend exploits on 2026-04-16, has said that CVE-2026-41091 is RedSun and CVE-2026-45498 is UnDefend ([The Hacker News, 2026-05-21])
  (low confidence) THN says the exploits were "disclosed by Chaotic Eclipse ... last month"; 2026-04-16 is in Help Net Security (cited elsewhere). THN's confirmation sits in an "Update" block that cites a post dated May 23, under a 2026-05-21 dateline.
- #8 F3 | cve-2026-41091-microsoft-defender-engine-link-following-eop | Body, Detection (claim b048a88e92)
  quote: the attacker staged renamed exploit binaries in the user's Pictures and Downloads folders after running commands that mapped user privileges, stored credentials and the Active Directory structure ([Help Net Security, 2026-04-17])
  (low confidence) Help Net Security: "The attacker dropped the exploit files into the user's Pictures and Downloads folders and renamed them ... Then, before launching the exploits, they ran commands to map out ..."; the order is reversed.
- #9 F3 | sparx-enterprise-architect-pro-cloud-server-five-cve-chain-p | Body (bd8345aaf8) and Correction (0cb1791527)
  quote: the CNA's CVSS 4.0 scores are 9.3 for CVE-2026-42097, 8.7 for CVE-2026-42096 and -42098, 7.7 for CVE-2026-42099 and 7.1 for CVE-2026-42100 ([CCB, 2026-05-21])
  (low confidence) The CCB advisory lists the CVE/CVSS values and vectors but never calls them the CNA's scores; the ENISA EUVD records (assigner CERT-PL, same values, EUVD-2026-30927 to -30932) carry that and are not cited at the clause.
- #10 F3 | drupal-core-highly-critical-pre-patch-warning-unauthenticate | Body, Exposure (claim cae6cfdffb)
  quote: The same releases carry Symfony and Twig security updates that apply to every site, whatever its database ([Drupal SA-CORE-2026-004])
  (low confidence) SA-CORE-2026-004: "The Drupal releases for supported branches (11.3, 11.2, 10.6, and 10.5) in this advisory also include security updates for Symfony and Twig". "The same releases" follows a list that includes the EOL 11.1.10 and 10.4.10, which the SA does not say carry them.
- #11 F14 | drupal-core-highly-critical-pre-patch-warning-unauthenticate | Body, Detection (claim 3d399370e4)
  quote: many of them carrying Nuclei scanner template markers
  (low confidence) Imperva: "Several payloads include Nuclei-style markers".
- #12 F4 | vm2-node-js-sandbox-12-critical-cves-cve-2026-43997-43999-44 | cves[CVE-2026-26956] (claim 033a18ab7d)
  quote: affected: "vm2 3.10.4"
  (low confidence) GHSA-ffh4-j6h5-pg66: "Affected versions <= 3.10.4, Patched versions 3.10.5"; the record narrows the range to a single version (THN wording) and drops earlier builds.
- #13 F4 | vm2-node-js-sandbox-12-critical-cves-cve-2026-43997-43999-44 | cves[CVE-2026-44007] (claim e10aaaea45)
  quote: auth: pre-auth
  (low confidence) GHSA-8hg8-63c5-gwmx vector CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H (privileges required High, score 9.1); the same entry labels PR:L CVE-2026-43999 post-auth.
- #14 F4 | symantec-carbon-black-document-fast16-hook-engine-targeting | techniques[] T1014
  quote: techniques: [T1059, T1014, ...]
  (low confidence) T1014 is Rootkit (hiding programs, files, services, drivers); no cited source describes hiding behavior. Broadcom describes a filesystem filter driver that patches executables as they are read, and a service whose timestamps match a system file.
- #15 F14 | pintheft-linux-kernel-local-privilege-escalation-primitive-r | title
  quote: ...public PoC; RDS loads by default only on Arch Linux
  (low confidence) V12/oss-security: "only default on Arch Linux among the common distributions we tested"; the entry's own Improvement says V12 "did not establish that the module is off on every other distribution", yet the changed title keeps the unqualified "only".

### Surface contradiction (F9)

- #1 F9 | sparx-enterprise-architect-pro-cloud-server-five-cve-chain-p | source CCB advisory
  quote: Title: "Warning: Actively exploited critical and multiple high vulnerabilities in Sparx Pro Cloud Server ... Patch Immediately!" vs body: "There is no proof of exploitation as of the writing of this advisory, as of 2026-05-20"
  (low confidence) The cited advisory's title says actively exploited, its body says no proof of exploitation; the entry silently follows the body (correctly) with no Contradiction note.
- #2 F9 | nx-console-vs-code-extension-2-2-m-installs-compromised-via | StepSecurity vs Nx timeline
  quote: StepSecurity: "At 12:36 UTC, the attacker published nrwl.angular-console v18.95.0" vs Nx postmortem: upload registered 12:30, publisher e-mail 12:36
  (low confidence) Two cited sources disagree on the publish time; the entry takes Nx's times without a Contradiction note.
- #3 F9 | cve-2026-45829-chromadb-python-fastapi-server-pre-auth-rce-v | HiddenLayer contact attempts
  quote: HiddenLayer's repeated contact attempts went unanswered ([BleepingComputer, 2026-05-19])
  (low confidence) Hadrian (also cited): HiddenLayer "got an initial acknowledgement on 2025-12-16 followed by silence across 10+ follow-ups". The entry notes the two report dates (2025-11-28 vs February 17) but not the acknowledgement.

### Needs more research (F8)

- #1 F8 | storm-2949-sspr-to-key-vault-azure-kill-chain | Detection
  quote: Entra ID records reset and registration activity in the Self-Service Password Management audit category ([Microsoft Learn])
  (low confidence) The same Learn page puts combined MFA registration events under Security > Authentication Methods; the attacker's new Authenticator registration is found there, which Detection omits.
- #2 F8 | sonicwall-gen6-ssl-vpn-incomplete-patching-cve-2024-12802-ak | affected_products / cves[].affected / fixed
  quote: SNWLID-2025-0001 impacted platforms table
  (low confidence) The cited advisory also lists SMA100 10.2.1.13-72sv and older (fixed 10.2.1.14-75sv), Gen7 7.0.1-5161 / 7.1.1-7058 lines (fixed 7.0.1-5169) and Gen6 NSv fixed 6.5.4.4-44v-21-2472; the entry carries only Gen6, Gen7 7.1.2 and Gen8 builds.
- #3 F8 | keycloak-26-6-2-16-cves-including-oidc-session-fixation-cve | cves[CVE-2026-6856] cvss
  quote: cvss: "n/a"
  (low confidence) Red Hat's CVE-2026-6856 page carries a preliminary Red Hat base score 3.1 (CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:N/I:L/A:N); the entry cites only the GitHub issue for this CVE.

### Drop (low relevance / routine patch-cycle) (F7)

- #1 F7 | cve-2026-45584-microsoft-defender-engine-heap-buffer-overflo | whole entry (notable)
  quote: Defender takeaway: no out-of-band step where Defender updates itself
  (low confidence) Unexploited, not publicly disclosed at release, auto-updating engine flaw needing multiple user actions; a routine patch-cycle CVE with no exposure-driven urgency (pre-existing entry, retained as notable).
- #2 F7 | cve-2026-42822-microsoft-azure-local-disconnected-operations | whole entry (notable)
  quote: with an insider precondition and no exploitation known it is a planned update, not an emergency
  (low confidence) Unexploited CVE in a restricted allow-listed offering with an internal-network/insider precondition; the entry says itself there is no decision beyond the planned update, and names no exposure of the constituency.
- #3 F7 | b1ack-s-stash-carding-marketplace-publicly-releases-4-6m-car | whole entry (notable)
  quote: organizations without a card portfolio or merchant estate have no decision to make
  (low confidence) Incident entry with no Swiss/EU-public-sector nexus (about 70% US cardholders, Europe only through UK and French cards) and no TTP beyond a marketplace announcement; does not clear the stricter breach/incident bar.

### Priority calibration (F16)

- #1 F16 | calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and | priority: high
  quote: neither source places European telecoms in the targeting
  (low confidence) Asia/Middle East telecom espionage (Afghanistan ISP, Azerbaijan, Kazakhstan/India targeting); no plausible exposure of the Swiss public-sector constituency is shown, so the 7-day decision bar for high is not met.

### Editorial / less-is-more flags (advisory) (F11)

- #1 F11 | all 23 slice entries | Correction/Improvement sections retell the retracted text
  quote: e.g. "No source places Grafana in Swiss or EU public-sector monitoring estates ..."; "not 7.8"; "The hunt signals given earlier ... have no source"; "No source says ALDO is common in German or Swiss federal administrations"; "not as an `_api/data` request"; "not SD-WAN gateways"
  The bodies were rewritten wholesale, so the sections mostly narrate what the entry used to say, which a reader never saw (check 4c(i)). The genuine deltas (CVSS source, fixed builds, attribution limits) are worth keeping; the negations of removed claims (grafana, chaotic-eclipse, fast16 LABScon/centrifuges, cve-2026-41091, cve-2026-45584, cve-2026-31635, cve-2026-42822, cve-2026-45829, huawei, sparx, storm-2949, thegentlemen, webworm, sonicwall, b1ack, keycloak, pintheft, verizon, calypso, drupal) could be dropped or marked internal.
- #2 F11 | record summaries of drupal, sparx, nx-console, huawei, cve-2026-41091, cve-2026-45584, vm2, storm-2949, webworm, sonicwall, b1ack, cve-2026-42822, cve-2026-45829, keycloak, pintheft, calypso, verizon | updates[].summary
  quote: "with exposure, detection and takeaway guidance added"; "the analysis is rebuilt from ..."; "unsourced Sysmon hunt signals give way to ..."; "a table of unrelated Drupal, Azure, ChromaDB and SonicWall CVEs is dropped"; "so the priority moves from high to notable"; "so the analysis is rewritten from the Drupal advisories ..."
  Record summaries render on the site; these clauses narrate the rewrite process and field changes rather than what the section tells a reader (pipeline self-reference).
- #3 F11 | cve-2026-41091-microsoft-defender-engine-link-following-eop | summary, body and 2026-05-22 Update
  quote: CVE-2026-45498 (CVSS 4.0)
  MSRC gives a CVSS 3.1 base score of 4.0 (vector CVSS:3.1/AV:L/AC:L/PR:N/...); in prose "CVSS 4.0" reads as CVSS version 4.0 (the Sparx entry uses that form for v4 scores). Write "CVSS 3.1 base score 4.0".
- #4 F11 | verizon-2026-dbir-vulnerability-exploitation-overtakes-crede | body
  quote: 31% vs 20%, 22% to 13%, 26% vs 38%, 32 to 43 days, 60%, 48%
  (low confidence) Body is a run of year-over-year percentages with a one-sentence takeaway (check 7); the DBIR is primary research and priority is notable, so advisory only.
- #5 F11 | drupal-core-highly-critical-pre-patch-warning-unauthenticate | sources[] bk.admin.ch
  quote: https://www.bk.admin.ch/en/standard-service-websites (role: corroborating)
  (low confidence) The Federal Chancellery page says the federal standard web platform is based on Livingdocs; it supports only a negative nexus remark in the Correction, not the finding, so it is not a corroborating source for CVE-2026-9082.
- #6 F11 | run record and wave report | "Together they map 400 ATT&CK ids, all active" / "400 active ATT&CK ids are mapped"
  quote: 400 ATT&CK ids
  Counting techniques[] across the 74 updated entries gives 400 mappings but 173 distinct ids; all are active in the pinned v20 dataset. Say "400 mappings (173 distinct ids)".
- #7 F11 | entities/registry.yaml | campaign:calypso-red-lamassu-showboat-jfmbackdoor-linux-windows-telco (pre-existing)
  quote: aliases: ['Red Lamassu', 'Bronze Medley']; summary "Calypso (Red Lamassu / Bronze Medley) telco-espionage campaign"
  (low confidence, pre-existing) Neither Lumen nor PwC, the entry's sources, uses the name Bronze Medley; the record was not among the 39 summaries rewritten.

### Checks with no finding

F1/F2 (every cited URL resolved to a specific page; the KEV JSON feed on the Drupal entry is a data feed, left as is), F5, F6, F12, F15, F17 (Admiralty codes inside vocabulary and consistent with sourcing), F18 (`actions[]` empty everywhere), techniques[] ids all active in the pinned v20 dataset, no IOCs, no em dash outside `## Type — at` headings, no TLP/watchlist/org_triage use. All evidence[] quotes in the 23 entries are verbatim substrings of the pages read (checked individually).

### Verdict

NEEDS_FIXES (truth: 15, editorial: 10, advisory: 7)

Of the 15 truth items 3 are firm (calypso: the Correction denies JFMBackdoor self-removal that PwC states; storm-2949: Microsoft's "we believe" dropped from the production-web-app takeover; chromadb: "ChromaToast" and "CVSS 4.0" cited to a page that carries neither) and 12 are marked low confidence in their summaries. All 10 editorial items are low confidence.

### Findings summary (machine-readable)

See work/2026-10-21T1148Z-audit/verification.iter1.s3.findings.yaml (32 records).
