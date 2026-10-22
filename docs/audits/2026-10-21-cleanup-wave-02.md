# Cleanup wave 02, 2026-10-21

**Run record:** [runs/2026-10-21/2026-10-21T0800Z-audit.md](../../runs/2026-10-21/2026-10-21T0800Z-audit.md) · **Prompt:** v4.22 · **Program:** [prompts/cleanup-coordinator.md](../../prompts/cleanup-coordinator.md) · **Tracker:** [docs/cleanup/STATUS.md](../cleanup/STATUS.md)

## Scope

Second wave of the store cleanup program, an operator-directed partial audit (claim `partial 2026-10-21T08:00:29Z`, base `6d76995`). Its rows carry fresh findings, so no truth pass ran (§ C2):

- **W1-B:** 57 entries the 2026-10-18 audit's truth passes T1 to T9 found imprecise outside its week (13 of them legacy entries).
- **W1-C:** 5 legacy entries those passes found clean, owed the rating, mapping and labelled lines their kind requires.
- **W1-E:** 34 carried residuals and `(pre-existing)` advisories from the audits of 2026-09-27 to 2026-10-20, on 26 entries plus three em-dash lists.
- **W1-F:** the 8 entry hunks of the reference branch `cleanup/2026-10-18-carry-forward`, all on W1-B entries, re-derived on `main` and re-verified rather than copied.
- **W1-H:** the Drupal SA-CORE-2026-014 page-check lead.

The 2026-10-18 verdicts were read before the 2026-10-11 audit's records landed, so every repair worker checked the current text first. The inputs were merged per entry into six batch files (`work/2026-10-21T0800Z-audit/batch-1.yaml` to `batch-6.yaml`, 10 to 17 entries each, 85 entries in all) and handed to six repair workers under one shared brief (`work/2026-10-21T0800Z-audit/repair-brief.md`).

## Verdict

**72 of the 85 entries carry one record from this wave: 61 improvements (18 of them internal) and 11 corrections (1 internal), no update.** The other 13 needed none (listed below). The 18 legacy entries of W1-B and W1-C left the legacy queue: 406 to 388 pending.

Verification: eight `cti-verification` passes, the loop's cap, over 541 to 553 changed claims plus this report, the run record and the tracker. Iteration 5 returned CLEAN, and the confirmation pass (iteration 6) refuted it, mostly on this wave's tracker text after waves 03 to 05 changed the plan on `main`. The loop published on the fail-open rule with residual 2, two count fixes in this report and the carried W1-I file applied after iteration 8. Budget: 19 of 20 spawns, about 9.13 M sub-agent tokens. Three passes stopped at the account-wide session limit and were resumed after its resets.

## Records

One row per entry with a record from this wave. What changed and why is in each entry's own changelog record and section, and in the worker reports `work/2026-10-21T0800Z-audit/repair-1.md` to `repair-6.md`.

| Entry | Rows | Record | Fields | Batch |
|---|---|---|---|---|
| 2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after | W1-B | improvement | techniques, body | 1 |
| 2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou | W1-E | improvement (internal) | body | 3 |
| 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n | W1-B/W1-F | improvement (internal) | headline, summary | 1 |
| 2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3 | W1-E | improvement (internal) | summary | 3 |
| 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u | W1-B/W1-F | improvement | tags, sectors, techniques, body | 1 |
| 2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map | W1-E | improvement | cves, sources, body | 3 |
| 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x | W1-B | correction | title, headline, summary, body | 1 |
| 2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s | W1-B/W1-F | improvement (internal) | techniques | 1 |
| 2026-05-16/node-ipc-npm-package-backdoored-via-expired-domain-account-t | W1-B | improvement | sources, body | 1 |
| 2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv | W1-B/W1-F | improvement (internal) | summary, techniques, sources | 1 |
| 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands | W1-B/W1-F | improvement (internal) | cves, sources, techniques | 1 |
| 2026-05-29/cve-2026-9170-ibm-http-server-websphere-application-server-p | W1-B | correction | summary, cves, sources, body | 1 |
| 2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen | W1-B | correction | actions, cves, body | 1 |
| 2026-06-03/ncsc-switzerland-warns-of-cyber-operations-around-the-g7-via | W1-C | improvement | body | 2 |
| 2026-06-04/ncsc-switzerland-booking-com-breach-feeds-two-pronged-whatsa | W1-C | improvement | body, techniques | 2 |
| 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti | W1-E | improvement (internal) | title, headline, summary, affected_products, cves, body | 3 |
| 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen | W1-B | improvement | actions, body, immediate_action, sources | 2 |
| 2026-06-10/ncsc-ch-week-23-coordinated-surge-in-job-seeker-targeting-fa | W1-C | improvement | body, techniques | 2 |
| 2026-06-10/year-old-winrar-flaw-cve-2025-8088-still-fuels-ukraine-intru | W1-E | improvement (internal) | title, headline, summary, event_date, body | 3 |
| 2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access | W1-E | improvement | actions, body | 3 |
| 2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc | W1-E | improvement (internal) | event_date | 3 |
| 2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti | W1-B | correction | body, sources, summary | 2 |
| 2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following | W1-B | correction | body, cves, sources, summary | 2 |
| 2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed | W1-B | correction | body | 2 |
| 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default | W1-C | improvement | body | 2 |
| 2026-06-25/ncsc-ch-active-microsoft-365-voicemail-phishing-wave-in-swit | W1-C | improvement | body, techniques | 2 |
| 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin | W1-B | correction | affected_products, body, cves, sources, summary, title | 2 |
| 2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed | W1-E | improvement | title, body | 3 |
| 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875 | W1-B | improvement | title, headline, summary, cves, actions, body | 3 |
| 2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev | W1-B | improvement | summary, cves, sources, actions, body | 3 |
| 2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce | W1-E | improvement | body | 3 |
| 2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach | W1-E | improvement | evidence, body | 3 |
| 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver | W1-B/W1-E | improvement | title, summary, actions, body | 3 |
| 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass | W1-B | improvement | title, cves, sources, sourcing_note, body | 3 |
| 2026-08-10/coding-agent-ci-harness-trust-boundary-shared-checkout | W1-B | improvement | actions, body, evidence, summary, title | 4 |
| 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce | W1-E | improvement | actions, body, cves, sources | 4 |
| 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix | W1-E | correction | body, cves, evidence, headline, title, sources | 4 |
| 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited | W1-B | improvement (internal) | cves, sourcing_note | 4 |
| 2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc | W1-E | improvement | actions, body, cves, sourcing_note, title | 4 |
| 2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection | W1-E | improvement (internal) | summary | 4 |
| 2026-09-10/sap-september-2026-overpass-s4get-preauth-rce | W1-B | improvement (internal) | body, cves, sources, title | 4 |
| 2026-09-12/jfrog-artifactory-cve-2026-42016-42018-token-chain-takeover | W1-B | improvement | actions, body, cves, evidence, headline, immediate_action, sources, sourcing_note, summary, title | 4 |
| 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware | W1-B | correction | body, evidence, title | 4 |
| 2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop | W1-B | improvement | body, cves, evidence, headline, sources, sourcing_note, summary | 4 |
| 2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce | W1-B | improvement | body, cves, immediate_action, summary | 4 |
| 2026-09-17/ddrop-dram-interposer-defeats-confidential-computing | W1-B | improvement (internal) | body, sources | 4 |
| 2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain | W1-B | improvement | actions, body, summary | 4 |
| 2026-09-18/cve-2026-91843-check-point-security-mgmt-stack-overflow | W1-B | improvement | actions, body, cves, sourcing_note, title | 4 |
| 2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat | W1-B | improvement | body, sources, sourcing_note | 5 |
| 2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10 | W1-B | improvement | body, sources | 5 |
| 2026-09-21/afpa-third-party-accommodation-tool-data-extraction | W1-B | improvement (internal) | body | 5 |
| 2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence | W1-B | improvement | body, summary, techniques | 5 |
| 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop | W1-B | improvement | summary | 5 |
| 2026-09-23/cve-2026-93952-arista-velocloud-orchestrator-exploited | W1-B | improvement | actions, body, cves, immediate_action, summary, title | 5 |
| 2026-09-23/virtualizor-billing-hook-unauth-root-rce | W1-B/W1-E | improvement | body, cves, sources, sourcing_note | 5 |
| 2026-09-24/microsoft-entra-id-sspr-enumeration-resetspy | W1-B | improvement | body, headline, summary | 5 |
| 2026-09-24/openai-agent-australia-medicare-portal-breach | W1-B | improvement | body, sources, summary | 5 |
| 2026-09-24/shinyhunters-fbi-peoplesoft-breach-claim | W1-B | improvement (internal) | cves, evidence, sources | 5 |
| 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning | W1-B | improvement (internal) | body | 6 |
| 2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach | W1-B | improvement | body, evidence | 6 |
| 2026-09-27/pentagon-dmdc-military-personnel-data-breach-unencrypted-ssn | W1-B | improvement | body, summary | 6 |
| 2026-09-28/cve-2019-18935-telerik-godzilla-webshell-virtualpathprovider | W1-B | improvement | body, cves, evidence, summary | 6 |
| 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan | W1-E | improvement | body | 6 |
| 2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev | W1-B | improvement (internal) | body, sources | 6 |
| 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev | W1-B/W1-F | correction (internal) | body, sources | 6 |
| 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities | W1-B/W1-F | improvement (internal) | summary | 6 |
| 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited | W1-B | improvement | body, evidence, sources | 6 |
| 2026-10-07/gentlemen-affiliate-azazel-ci-cd-secrets-mcp-attacks | W1-B | improvement | body | 6 |
| 2026-10-07/ninja-forms-wpc-bundles-stored-xss-hidden-admin-campaign | W1-B | improvement | body, cves, evidence, sources | 6 |
| 2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale | W1-B/W1-F | correction | summary | 6 |
| 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev | W1-E | improvement | body, evidence, sources, sourcing_note, summary | 6 |
| 2026-10-14/exchange-oct-2026-su-cve-2026-70571-last-2016-2019-update | W1-E | improvement | body | 6 |

## Entries without a record

| Entry | Reason |
|---|---|
| 2026-05-13 Netlogon CVE-2026-41089 (W1-E) | The `exploited` status stays: the taxonomy has no reported or disputed value, and dropping it would hide CCB's in-the-wild report from automated readers. The headline, summary and Contradiction line already carry Microsoft's dissent. |
| 2026-06-12 FortiSandbox CVE-2026-25089 (W1-B, W1-E) | The 4.2-range finding was already fixed by 2026-10-11T1307Z-audit. The sector-tag item stays declined on principle (sector tags are the profile's relevance call). Its title keeps one em dash until its next record. |
| 2026-09-06 MikroTik (W1-E) | The word "frontmatter" stands only in the 2026-09-11 record summary, which is append-only. |
| 2026-09-18 Acronis CVE-2026-87886 (W1-E) | The JSON primary stays: the human-readable advisory page is a script shell with none of the cited text. The title em dash was already gone. |
| 2026-09-21 NightEagle, 2026-09-21 The Gentlemen open directory, 2026-09-23 Gambit, 2026-09-25 motion 24.3209, 2026-09-27 QBUSOFT/Medyc, 2026-09-28 Storm-3168 (W1-B) | Every listed defect was already fixed by 2026-10-11T1307Z-audit. |
| 2026-09-23 Check Point CVE-2026-93616 (W1-E) | The 2026-10-04 section's indicator numbering was already fixed by 2026-10-20T0835Z-audit. |
| 2026-09-23 Austrian NISG transposition (W1-E) | Both items stay declined on principle: removing an entry is outside the changelog lifecycle, and the Improvement section states its delta once. |
| 2026-10-16 Drupal SA-CORE-2026-014 (W1-H) | The entry is right and the advisory unchanged. The container receives drupal.org's "Client Challenge" wall instead of the page, and the page checks compared the quote against it. Fixed in the gate as W7-15. |

## Notable fixes

- **W1-F drafts:** all eight re-derived. The Nx cascade's CVE-2026-8398 carries the 9.3 (CVSS 4.0) its EUVD page shows. The 9.8 (CVSS 3.1) that the finding and the draft proposed stands only on the CVE record, which cannot be cited, so it was not used. The Beagle tag and sector change went into a reader-facing improvement together with that entry's legacy duties, and the Ixa Systems summary correction has its own section. The other six, the Nx cascade among them, are internal records.
- **Superseded remediation:** IBM's interim fix IFPH71594 is superseded by IFDT503301 (IBM HTTP Server CVE-2026-9170). PAN-OS CVE-2026-0257 no longer tells readers to force a re-authentication: Palo Alto Networks says users must re-authenticate once after the upgrade anyway, because the firewall regenerates the cookie.
- **Attribution:** the Fragnesia Kubernetes claim is attributed to Aikido and the whole Dirty Frag family. The FortiBleed counts are attributed to Hudson Rock and Beaumont. The Kemp scores are given as Progress's 9.6 and ZDI's 9.8. The PHP SOAP CVE-2026-7262 numbering-authority score (2.9) now stands beside the advisory's 6.3. Pixel CVE-2026-58704 cites Google's own exploitation note.
- **Wrong hunting guidance:** ShieldBreak's 2026-08-18 section no longer hunts for a process tree rooted at the Defender engine, since LevelBlue shows the SYSTEM stage running under `wermgr.exe`.
- **English quotations:** the Liechtenstein VWBP entry's eight German evidence rows carry an English quote with the German original beside it, and three German quotes in the body are translated.
- **Labelled lines:** owed lines added on RoguePlanet 2026-07-09, SAP August, the five W1-C entries and the legacy entries where their sources support them. A Triage line was added only where a source gives an honest discriminator.

## Declined findings

Beyond the entries above, findings were declined in four classes. Each decline is listed per entry in the worker reports.

- **Already fixed by an earlier audit**, mostly 2026-10-11T1307Z-audit: every listed defect on the seven entries above, and part of them on many of the 72.
- **Append-only record summaries.** A finding that asked to edit an earlier `updates[]` summary was declined (Fragnesia, PAN-OS, ServiceNow, Pixel, Cisco ISE, ShinyHunters FBI, Gambit). Where the wrong statement also stood in the body, it was fixed there.
- **Uncitable values.** A score or SSVC value that only the CVE record carries was left out (Virtualizor CVSS 3.1 and SSVC, Nx CVE-2026-8398 CVSS 3.1). The Ninja Forms alias CVE-2026-92438 also stays without a score, but its ENISA record (EUVD-2026-84282) carries WPScan's 8.8, so wave 06 can add it.
- **Principle.** Sector tags and relevance framing are the profile's call (FortiSandbox, Check Point IKEv1, Kemp, Virtualizor). Citrix's own pages name no compromise-check script for CVE-2026-88779, so the script is attributed to watchTowr instead of being presented as the vendor's check.

The W1-E em-dash lists are fixed on every entry this wave wrote a record on. The entries in those lists that received no record (Oracle EBS, Lazarus, Nexus, Sekoia, nginx, GitLab 2026-09-12, FortiSandbox, MikroTik) keep theirs until their next record, since the site strips them at render.

## Registry and state

- `state/cves_seen.json`: CVE-2026-92438 added (the Ninja Forms flaw, published by a second numbering authority as the same issue as CVE-2026-94504), `last_seen` moved to 2026-10-21 for 33 records, and four titles brought in line with their entries (CVE-2026-44772, CVE-2026-73570, CVE-2026-58704, CVE-2026-33691).
- `entities/registry.yaml`: the FTAPI incident summary names the vendor "FTAPI of Munich" as its sources do. `tools/sync_products.py` added four product records (Progress ECS Connections Manager, Progress MOVEit WAF, Progress Object Scale Connection Manager, Starlette) and moved BerriAI LiteLLM's `first_seen` to 2026-06-09.
- `state/legacy_review.json`: 18 entries marked reviewed under this run id.

## Folds

None this wave. The W4 rows run in waves 03, 06, 08 and 12.

## Tool, doc and state changes

| Row | Commit | Change |
|---|---|---|
| W7-14 | `731706f` | `tools/claim_ledger.py` lists the sentences a fire edits inside earlier dated sections, diffed against the base like the main analysis, with `tools/test_claim_ledger.py`. On wave 01's record it lists 14 sentences in earlier sections that the old ledger skipped, among them the Check Point wording that wave found only by reading the diff. |
| W7-15 | `1f8d69e` | `tools/check_run.py` treats a bot-challenge interstitial (drupal.org's "Client Challenge", Cloudflare, Anubis) as an unread page instead of page text, pinned in `tools/test_check_run.py`. |
| (wave) | `ea6e509` | The wave's plan, batch files and worker brief, committed while the workers ran. |
| (program) | `b511bbe` | Prompt v4.23, by operator directive during the wave: cleanup waves run in parallel, one session per wave, on lanes the tracker keeps disjoint. `tools/merge_state.py` merges `state/legacy_review.json` and `work/cleanup/plan.json` and re-renders `docs/cleanup/STATUS.md`. `work/cleanup/render_status.py --check-lanes` proves the ready and in-flight waves share no entry. This wave's claim gained its `wave=02` tag, and its rows were marked in flight on `main`. |
| (program) | `17506d0` | Lane fix: the 2026-06-19 RoguePlanet entry moved from W1-D (wave 03) to W1-D2 (wave 06), with the W4-02 fold that takes it. |

At the gate the main agent amended one record and two sentences: the IOC scan read the LiteSpeed versions 5.3.2.0 and 5.3.2.1 and the Ivanti release 25.1.3.0 as IPv4 addresses, and the word "version" or "release" now stands beside them.

## Not reached and carried forward

- **W1-I (new row, wave 06):** 45 residuals the workers noticed outside their findings and left unfixed, on 73 entries, among them headlines over 120 characters, `**Detection and hunting.**` labels the site does not lift, stale `cves_seen` titles, `priority: critical` on June and September findings (Check Point IKEv1, PeopleSoft, JFrog), and a tool defect: `tools/sync_products.py --report` writes the registry although its docstring calls it a report. Input: `work/cleanup/wave-06/findings-W1-I.md`, which also carries the seven verifier advisories this wave did not fix (Kemp twice, ShieldBreak twice, the RoguePlanet citation label, the Check Point IKEv1 priority and the Ninja Forms alias score). The residuals on the three legacy entries in W2-03 and W2-04 (LiteLLM, WinRAR, ShinyHunters PeopleSoft) travel with those batches.
- **W7-17 (run-id collision, tracked by wave 03 in wave 11):** run ids have minute precision, so two parallel waves started in the same minute compute the same one. Waves 03 and 05 both computed `2026-10-21T1147Z-audit`, and wave 03 re-claimed as `2026-10-21T1149Z-audit`. The kickoff files of waves 06 to 08 tell a session to take the next free minute, until a versioned change to the coordinator's C1 does.
- **Pixel CVE-2026-58704:** the gate's `quote-literal` check cannot find Google's exploitation note on the bulletin, because the container receives an older copy of the page without its 2026-09-30 revision. The worker read the note verbatim through WebFetch (`work/2026-10-21T0800Z-audit/repair-4/src/e11-pixel-webfetch.txt`).
- **Unreadable from the container:** ox.security (403 to every reader), the SonicWall PSIRT page and Ivanti's hub advisory (script shells), and Progress's community bulletin. Each fix there rests on the readable sources the entry already cites.

## Tracker delta

Rows done this wave: W1-B, W1-C, W1-E, W1-F, W1-H, W7-14, W7-15 (new). New: W1-I (45 residuals) and W1-D2 (the W1-D verdicts on 10 entries that wait for this wave), both in wave 06. The W1-E row now lists all 26 entries its items touch. Under v4.23 the next waves run in parallel: 03, 04 and 05 (lanes A, B and C) were ready on `main` while this wave ran, and 06, 07 and 08, which waited for it, are ready once its record is on `main`. Each has its kickoff in `work/cleanup/wave-<NN>/HANDOVER.md`.
