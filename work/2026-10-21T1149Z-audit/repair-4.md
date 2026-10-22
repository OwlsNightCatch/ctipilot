# Repair worker 4, cleanup wave 03 (2026-10-21T1149Z-audit)

Batch: `work/2026-10-21T1149Z-audit/batch-4.yaml`, 5 entries. Records written: 2 correction (1 internal), 2 improvement; 1 entry without a record. All records stamped `at: 2026-10-21T12:07:28Z`, run_id `2026-10-21T1149Z-audit`. Fetched bodies are under `work/2026-10-21T1149Z-audit/repair-4/src/`, record texts under `repair-4/rec/`. `check_run.py --all` exits 0, and the only lines on these entries are the expected "run_id does not resolve to a run record" WARNs. Page checks (`repair-4/page-checks.txt`): 4 pass, 0 warn, 0 fail. No legacy duties in this batch (all `legacy_duty: false`).

## 2026-05-19/n8n-prototype-pollution-chain-cve-2026-42231-et-al-authentic

- Record: `correction`, internal, at 2026-10-21T12:07:28Z, fields `[techniques]`.
- Applied: `techniques` T1190, T1059.007, T1005 became T1190, T1078, T1005. T1078 (Valid Accounts) maps the precondition every GHSA states ("An authenticated user with permission to create or modify workflows could exploit this", https://github.com/n8n-io/n8n/security/advisories/GHSA-q5f4-99jv-pgg5). T1059.007 (JavaScript) is dropped: no advisory describes JavaScript execution ("pollute the JavaScript object prototype" is the mechanism, not the execution), and the group note marks the 3b mapping it came from as `verified: false`.
- Declined, already fixed by 2026-10-11T1307Z-audit: per-advisory dates (2026-04-22 and 2026-05-13); vector zero-click / auth post-auth on all five; CVE-2026-44790 type info-disclosure; non-verbatim THN evidence and spliced GHSA evidence (evidence now empty, allowed for a non-exploited entry); "chained" and "root cause / root flaw" framing; GHSA workarounds (now in the takeaway); the 1.123.32 / 2.17.4 / 2.18.1 "only remediation" contradiction; CVE-2026-44791 as a bypass of the CVE-2026-42232 XML node fix; Swiss/EU public-sector, webhook-exposure and payload-token claims; classification and techniques present.
- Declined, not fixable from a citable page: the 2.21.1 versus 2.22.1 discrepancy. Only the CVE record (cveawg, a blocked citation) lists a 2.21.x branch fixed in 2.21.1. All three GHSAs list affected "< 2.22.1" and patched ">= 2.22.1" (https://github.com/n8n-io/n8n/security/advisories/GHSA-c8xv-5998-g76h), so the entry follows the vendor advisory. No release page was fetched, because that would mean constructing a URL.

## 2026-05-29/forticlient-ems-cve-2026-35616-ekz-infostealer-kill-chain

- Record: `improvement`, at 2026-10-21T12:07:28Z, fields `[cves, body]`, with an `## Improvement` section.
- Applied:
  - `cves[].cvss` "9.1 (CVSS 3.1 temporal; base 9.8)" became "9.8 (CVSSv3 base; temporal 9.1)". The PSIRT metadata block reads "CVSSv3 Score 9.8 / CVSSv3 Temporal Score 9.1" (https://fortiguard.fortinet.com/psirt/FG-IR-26-099, raw page).
  - The Chromium clause "to get past app-bound encryption" now reads "relaunches from there to pass Chromium Elevation Service path validation before decrypting the browser's master key", matching Arctic Wolf's wording.
  - The Detection line adds Arctic Wolf's file and process hunts: the fake patch running from `C:\ProgramData`, its self-copy into a browser `Application` directory, and `C:\ProgramData\log.txt` read by PowerShell, sent by HTTP POST, then deleted with the payload. This replaces the wrong profile-directory hunt that the 10-11 audit removed without a successor. Source: https://arcticwolf.com/resources/blog/forticlient-ems-exploited-via-cve-2026-35616-to-deliver-ekz-infostealer-disguised-as-a-fortinet-patch/
- Declined, already fixed by 2026-10-11T1307Z-audit: fronting reverse-proxy mechanism; "signed under fortitray.exe"; browser profile-directory self-copy; Swiss/EU deployment claim; event_date (now 2026-05-27); NVD-cited KEV link (now the KEV JSON); hotfix mention; non-verbatim evidence (the PSIRT quote is verbatim); A:N vector; SharePoint CVE-2026-45659 comparison; Update-task / update-channel delivery and `-enc`; "first public" claim; undated EPSS; T1072 mapping; uncited AD/MFA claim; classification and techniques present.

## 2026-06-08/cve-2026-3300-unauthenticated-eval-injection-in-a-commercial

- No record. Every finding is already fixed by 2026-10-11T1307Z-audit, re-derived against https://www.wordfence.com/blog/2026/06/attackers-actively-exploiting-critical-vulnerability-in-everest-forms-pro-plugin/. The checked items:
  - no "sustained / still active 6 June" claim;
  - no "vendor-confirmed" sentence;
  - the evidence quote is verbatim on Wordfence;
  - the Wordfence label is 2026-06-03;
  - prerequisite stated as "a form that uses complex calculations";
  - no "§ 5" references;
  - affected 1.9.12 and earlier, fixed 1.9.13, priority notable;
  - headline has no "June campaign";
  - no BleepingComputer citation for process_filter();
  - install base of about 4,000 stated, no public-sector claim, no SEO-spam claim;
  - no workflow taglines; actions empty.
- CVE-2026-3300 is still absent from CISA KEV (catalog 2026.10.20).
- Declined: adding "most of the 29,300 blocked requests came from one IP". The exploitation statement is accurate as written, and the concentration detail does not change a defender's decision.

## 2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass

- Record: `improvement`, at 2026-10-21T12:07:28Z, fields `[title, cves, sources, body]`, with an `## Improvement` section.
- Applied:
  - The score is labelled CVSS 3.1 in the title, `cves[].cvss` ("10.0 (CVSS 3.1)") and the main analysis, cited to CCB Belgium, which gives "CVSS 10 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)" (https://ccb.belgium.be/advisories/warning-simplehelp-patched-cve-2026-48558-critical-authentication-bypass-vulnerability). The CVSS 4.0 9.5 is only on the CVE record, so it is not added.
  - 6.0 scope narrowed from "the 6.0 prerelease" to "some 6.0 beta and release-candidate builds" in the body, Exposure and `cves[].affected`, per the vendor guide: "Some 6.0 beta and release candidate builds are affected" (https://guides.simple-help.com/kb---security-vulnerabilities-05-2026). The guide is added to `sources[]` as a SimpleHelp primary.
  - Exposure now names the configuration conditions and says "Allow group authenticated logins" is off by default for new Groups and that servers without such a Group cannot be exploited this way (same guide).
  - The takeaway adds the interim technician login IP restriction under Administration > Login Security. Horizon3: "If you cannot patch in a timely manner, consider applying IP restrictions to where Technicians can authenticate from" (https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/). The vendor guide says these restrictions block logins from excluded ranges.
- Declined, already fixed by 2026-10-11T1307Z-audit: IdP-MFA claim (now first-login MFA self-registration, with a verbatim Horizon3 evidence quote); signature clause now cited to CCB Belgium (which carries it verbatim); poc-public dropped; ShinyHunters entity and PeopleSoft row gone; Horizon3 IOCs in Detection; T1078.004 replaced by T1078; "European MSP estates" gone; TaskWeaver scheduled-task / launchd persistence gone; the "~1,000 measured" claim now reads as 7.2% of a sample; process hunts now Blackpoint's; classification and techniques present.
- Declined, unverifiable: dating the fix 2026-05-26. Neither readable SimpleHelp page shows the build date (the security page gives only the `5.5.16_202605` update URL), so no date is written and `sources[]` keeps the SimpleHelp records undated.

## 2026-07-16/cve-2026-46817-oracle-ebs-payments-preauth-rce-kev-listed

- Record: `correction`, at 2026-10-21T12:07:28Z, fields `[headline, sources, body]`, with a `## Correction` section.
- Applied:
  - Oracle release date. The 2026-10-11 record re-dated the advisory to 2026-05-21, but that is only the page's CMS `<meta name="Updated Date">`. The advisory's visible revision table reads "2026-May-28 | Rev 1. Initial Release." (https://www.oracle.com/security-alerts/cspumay2026.html), and Help Net Security says it was patched "in late May 2026". So `sources[0].date` is now 2026-05-28, and every "Oracle CSPU, 2026-05-21" label is relabelled 2026-05-28: two in the main analysis, one in the 2026-10-11 Correction section.
  - "Roughly six weeks" is now attributed to Defused, with the actual gap stated (Oracle's 28 May release to the 27 June first exploitation is 30 days). Source: https://www.helpnetsecurity.com/2026/06/30/oracle-payments-cve-2026-46817-exploitation/
  - The takeaway's 28 May threshold is now stated as Oracle's release date. It was described as only "the threshold Help Net Security gives".
  - The closing paragraph is split into `**Exposure:**`, `**Detection:**` and `**Defender takeaway:**`, using the existing cited facts only, and the restated "pre-auth, no-interaction path" sentence is dropped.
  - Em dashes removed from the headline (now 119 characters) and the main analysis (2). The em dash inside the verbatim Defused `evidence[0]` quote is kept.
  - CISA alert evidence quote checked through WebFetch: the opening sentence ends "based on evidence of active exploitation.", matching `evidence[2]`.
- Declined, already fixed by 2026-10-11T1307Z-audit: "RCE" in title, type and body (now takeover, type auth-bypass); "mechanics not public" (the ibytransmit file read is stated); CPU versus CSPU naming; cisa-kev status and affected / fixed fields; migrated self-quotes as evidence; "§ 5" references; ShinyHunters / UNC6240 entity and claims; uncited public-sector usage profile; "servlet"; CWE labels now attributed to the CISA catalog.

## Links between batch entries

- None needed. The five entries share no CVE and no group note links two of them. The duplicates named in the groups were already folded by 2026-10-11T1307Z-audit.

## State changes the main agent must apply

- `entities/registry.yaml`: none.
- `state/cves_seen.json`:
  - CVE-2026-35616: `last_seen` to 2026-10-21 (cvss changed). The title still carries the retired "spoof mTLS state on X-SSL-CLIENT-VERIFY header" framing and an em dash. Suggested title: "Fortinet FortiClient EMS 7.4.5/7.4.6 API authentication bypass (CVSSv3 9.8); exploited ITW to push EKZ Infostealer through VPN on-connect scripts per Arctic Wolf 2026-05-27".
  - CVE-2026-48558: `last_seen` to 2026-10-21 (cvss and affected changed). Optional title touch: "(CVSS 10.0)" to "(CVSS 3.1 10.0)", and the em dash removed.
  - CVE-2026-46817: the CVE record is unchanged, so no bump is required. Its title still says "RCE/takeover" and "Oracle May 2026 CPU"; suggested title: "Oracle E-Business Suite / Oracle Payments File Transmission unauthenticated takeover (CVSS 9.8); CISA KEV 2026-07-15, exploited ITW since 2026-06-27; fixed Oracle May 2026 CSPU (12.2.3-12.2.15)".

## Residuals noticed outside the findings (nothing fixed)

- n8n: `cves[].type` is logic-flaw for CVE-2026-42231 and CVE-2026-44789, whose GHSA titles say "to RCE", while CVE-2026-42232 and CVE-2026-44791, with the same "combined with other nodes" RCE wording, are rce. The typing is inconsistent.
- n8n: the `supply-chain` tag has no source basis (no supply-chain element in any advisory).
- FortiClient: `techniques` omits behaviors that the body and Arctic Wolf state: payload download (T1105), HTTP POST exfiltration (T1041), base64-encoded PowerShell (T1027) and payload / log deletion (T1070.004).
- FortiClient: the takeaway omits Arctic Wolf's mitigation of restricting the EMS management port 8013 to trusted IP ranges.
- FortiClient: the Bishop Fox page was in scheduled maintenance (HTTP 503) on 2026-10-21, so the unchanged mechanism sentence was not re-read this run.
- SimpleHelp: CCB Belgium states "A proof of concept is available"; no other source shows one and Horizon3 withheld details, so `poc-public` was not re-added. The verifier may want to weigh this.
- SimpleHelp: `sectors` includes public-sector, but no cited source names public-sector victims or use.
- SimpleHelp: both SimpleHelp `sources[]` records are undated, because neither page carries a reliable publication date.
