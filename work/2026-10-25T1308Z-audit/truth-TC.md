**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-25T13:14:16Z · ended_at=2026-10-25T13:41:35Z · duration_seconds=1639

## Retrospective truth pass TC — quality audit 2026-10-25T1308Z-audit

Ledger note: the spawn message named `truth-TC.ledger.yaml`; the file on disk is `truth-C.ledger.yaml` (batch C, 9 entries, 338 claims), which is the ledger walked. Verdict rows: `truth-TC.claims.yaml` (338 rows: 311 ok, 23 F4, 2 F3, 2 unreadable).

### Named leads — dispositions

- **ConnectWise / Microsoft evidence quote: confirmed real defect.** 'Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants at 2,900 sign-in attempts per minute' splices two statements of the Microsoft post; 2,900 per minute is the peak of failed logons in the separate Oct 10-14 password-spray campaign. The same wrong binding is in the 2026-10-22 section body.
- **LiteLLM / GitHub #47826 quote: lead refuted, quote is verbatim.** The sentence is in maintainer ojensen-berri's status comment of 2026-10-21T16:32:49Z on issue #47826 (read through the GitHub issue-comments API; the pre-pass cached body is a trimmed extract with the comments cut, and github.com itself is walled out).
- **LiteLLM / Aikido quote: confirmed real defect (meaning-preserving).** The page reads 'PyPI has now quarantined and removed version 1.107.0.'; the evidence record drops 'and removed'.
- **Citrix 2026-10-18 audit correction (watchTowr up-to-24-hours crash-log script): verified true.** watchTowr Labs: 'The Command Injection doesn't trigger instantly, we have to wait for `ns_monuploadd_err.pl` to run, which can take up to 24 hours'; the two Pitboss messages are 'missed too many heartbeats' and 'unexpectedly died' in the script's grep.

### Pages edited since publication (noted, not defects)

Unit 42 NetScaler brief (updated 2026-10-01 and 2026-10-08 after the 2026-09-30 text cited); Tenable NetScaler FAQ (updated 2026-10-04); Microsoft KB5025885 (last revision 2026-09-30, as cited); ConnectWise Trust Center advisory (updates to 2026-10-24, read from an archived copy because the live page returns 403 on every transport); ENISA EUVD-2026-108169 (updated 2026-10-24; it now carries EPSS 0.71 while the Node2Shell entry's `epss` is null, which is not a claim defect).

### Unreadable sources

- `community.citrix.com/.../security-update-guidance-for-netscaler-saml-authentication-deployments/` (Citrix, 2026-10-02): HTTP 403 on extract, url, WebFetch and jina; the claim it carries ('independent of the vulnerabilities disclosed in CTX697096') is corroborated by BleepingComputer 2026-10-04 ('Citrix also confirmed that the issue was different from the previously disclosed NetScaler vulnerabilities').
- `support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05162en_us`: JavaScript shell on every transport; the same bulletin was read from HPE's CSAF JSON and its PGP-signed text advisory on csaf.arubanetworking.hpe.com.

### Entries with defects

#### 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev — imprecision

1. **[imprecision] frontmatter cves[CVE-2026-88771] .. cves[CVE-2026-88778] `affected`**
   - Claim: All NetScaler ADC/Gateway releases before the fixed builds (default configuration, no feature required)
   - Defect: (low confidence) Citrix lists only the supported 14.1 and 13.1 branches (and FIPS/NDcPP) as affected before the fixed builds, while the entry's own body and actions[2] say Citrix has not said whether the end-of-life 12.1 and 13.0 branches are affected, so 'All ... releases before the fixed builds' over-reaches on the EOL branches.
   - Ground truth: CTX697096: 'Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1 BEFORE 14.1-73.37 / 13.1 BEFORE 13.1-64.23 / ADC FIPS BEFORE 14.1-73.37 FIPS / FIPS and NDcPP BEFORE 13.1-37.279'; Tenable: 'Citrix has not said whether they [12.1 and 13.0] are affected by these vulnerabilities.'
   - URL: https://support.citrix.com/external/article/CTX697096/citrix-netscaler-adc-and-citrix-netscale.html
   - Fix: State `affected` as the supported 14.1/13.1/FIPS/NDcPP builds before the fixed builds and note that EOL 12.1/13.0 status is unstated by Citrix.

2. **[imprecision] body, paragraph 3 (disclosure path)**
   - Claim: No public attribution of the exploiting activity exists; watchTowr's FAQ states "No attribution has been made public,"
   - Defect: (low confidence) The absolute 'no public attribution' is stale: from 2026-09-30 Mandiant's CTO publicly characterised the initial CVE-2026-88772 intrusions as likely the work of 'advanced and suspected state-sponsored threat actors' (no group named), and said broad opportunistic exploitation by various actors is expected; the entry's later sections say only that GTIG and GreyNoise 'name no actor'.
   - Ground truth: Help Net Security 2026-09-30: "'Advanced and suspected state-sponsored threat actors' are likely to be behind the initial targeted intrusions that leveraged CVE-2026-88772" (Mandiant CTO Charles Carmakal).
   - URL: https://www.helpnetsecurity.com/2026/09/30/cve-2026-88772-netscaler-exploitation-zero-day/
   - Fix: Qualify the sentence: no named actor, but Mandiant's CTO calls the initial CVE-2026-88772 intrusions likely state-sponsored.

#### 2026-10-18/connectwise-cloud-backup-skykick-m365-app-credential-abuse — factual-error

1. **[factual-error] section ## Update — 2026-10-22T03:46:23Z, second paragraph**
   - Claim: It counts attempted sign-ins to more than 2,250 tenants at up to 2,900 attempts a minute and links the activity to an automated cross-tenant password spray between 2026-10-10 and 2026-10-14 against 327 accounts at eight organizations
   - Defect: Microsoft gives no per-minute rate for the ARTEX sign-in attempts to 2,250+ tenants; 2,900 per minute is the peak of failed logons in the separate Oct 10-14 password-spray campaign (Oct 11), so the figure is bound to the wrong activity.
   - Ground truth: Microsoft: 'Following the unauthorized access, Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants.' and, for the spray: 'Microsoft telemetry captured 151,000+ failed logon events, with activity peaking on October 11 at 2,900 failures per minute'.
   - URL: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
   - Fix: Drop 'at up to 2,900 attempts a minute' from the sign-in clause, or attach it to the spray ('peaking at 2,900 failed logons a minute on 2026-10-11').

2. **[factual-error] frontmatter evidence[] (publisher: Microsoft Threat Intelligence)**
   - Claim: Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants at 2,900 sign-in attempts per minute
   - Defect: Not a contiguous passage of the cited page: it splices the sentence about 2,250 tenants with the separate '2,900 failures per minute' spray statistic and re-attributes that rate to ARTEX sign-ins (the pre-pass lead is confirmed).
   - Ground truth: 'Following the unauthorized access, Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants.' (one sentence) and, in the Password Spraying section, 'activity peaking on October 11 at 2,900 failures per minute'. The page text has no 'at 2,900 sign-in attempts per minute'.
   - URL: https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/
   - Fix: Replace with the verbatim sentence 'Storm-0940 used ARTEX to attempt to sign-in to more than 2,250 tenants.'

3. **[imprecision] section ## Update — 2026-10-22T03:46:23Z, last sentence**
   - Claim: ConnectWise publishes updates twice daily from 2026-10-22
   - Defect: Superseded by ConnectWise's own later update; as of today the cadence is once daily.
   - Ground truth: ConnectWise advisory, Update Friday Oct 23 01:00 UTC: 'Starting Friday October 23, we will move to once daily updates, with significant developments shared sooner.' (restoration target now phased partner onboarding from Monday Oct 26, per the Oct 24 14:00 UTC update).
   - URL: https://web.archive.org/web/2026/https://www.connectwise.com/company/trust/advisories
   - Fix: Add a changelog record that the cadence moved to once daily on 2026-10-23, or drop the sentence.

#### 2026-10-23/hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth — factual-error

1. **[factual-error] body, paragraph 2 (affected versions) and every cves[].affected**
   - Claim: the machine-readable CSAF lists wider known-affected ranges, AOS-10 10.8.0.0 to 10.8.1.1, 10.6.0.0 to 10.7.2.6 and 10.3.0.0 to 10.4.1.13, and AOS-8 8.12.0.0 to 8.13.3.0 and 8.10.0.0 to 8.10.0.23, which take in the 10.6, 10.3 and 8.12 branches the text omits, so treat the CSAF ranges as the scope
   - Defect: The CSAF known_affected ranges start at 10.8.0.0, 10.7.0.0, 10.4.0.0, 8.13.0.0 and 8.10.0.0; there is no 10.6, 10.3 or 8.12 range, so the 'wider CSAF scope' claim and the matching `affected` text on all 19 CVE records (e.g. '10.6.0.0 to 10.7.2.6, 10.3.0.0 to 10.4.1.13, 8.12.0.0 to 8.13.3.0 (CSAF ranges)') are invented. The CSAF agrees with HPE's text advisory.
   - Ground truth: CSAF product_tree ranges: 'vers:semver/>=10.8.0.0|<=10.8.1.1', '>=10.7.0.0|<=10.7.2.6', '>=10.4.0.0|<=10.4.1.13', '>=8.13.0.0|<=8.13.3.0', '>=8.10.0.0|<=8.10.0.23'; text advisory: 'AOS-10.8.x.x: 10.8.1.1 and below ... AOS-8.13.x.x: 8.13.3.0 and below'.
   - URL: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json
   - Fix: Set each `affected` to the CSAF ranges (10.8.0.0-10.8.1.1, 10.7.0.0-10.7.2.6, 10.4.0.0-10.4.1.13 for AOS-10; 8.13.0.0-8.13.3.0, 8.10.0.0-8.10.0.23 for AOS-8) and delete the 'wider CSAF ranges' sentence; if kept, say that HPE presumes End-of-Maintenance versions affected.

2. **[factual-error] summary and body paragraph 1**
   - Claim: 34 of them at CVSS 3.1 9.0 or higher ... (eight at 10.0, ten at 9.8, eleven at 9.6, one at 9.4 and four at 9.3); ... and the other 15 are reachable from the adjacent network
   - Defect: The CSAF (and HPE's text advisory) score 33 CVEs at 9.0 or higher, ten (not eleven) at 9.6, and 14 (not 15) adjacent-network ones; the 19 network/no-privilege figure is correct.
   - Ground truth: Per-CVE CSAF baseScore counts: 8 x 10.0, 10 x 9.8, 10 x 9.6, 1 x 9.4, 4 x 9.3 = 33; 19 AV:N/PR:N, 14 AV:A/PR:N.
   - URL: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.json
   - Fix: Change to '33 of the 72 ... ten at 9.6 ... the other 14'.

3. **[imprecision] body, Exposure paragraph**
   - Claim: any HPE Networking mobility conductor, controller, gateway, access point or virtual machine that runs a listed version; HPE says every compatible hardware model is affected and that its own hardware list is illustrative only
   - Defect: (low confidence) Neither HPE's text advisory nor its CSAF contains a hardware-model or virtual-machine statement, and the cited support.hpe.com page renders only a JavaScript shell on every transport, so the clause could not be confirmed.
   - Ground truth: HPE text advisory 'Affected Products' lists Mobility Conductors, Mobility Controllers, Mobility Gateways (Managed by HPE Networking Central), AOS-10 APs and AOS-8 Instant APs; no hardware-model list or 'illustrative' wording found.
   - URL: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt
   - Fix: Cite the passage verbatim from a readable HPE source or drop the clause.

4. **[imprecision] body (affected versions / Exposure)**
   - Claim: (omitted)
   - Defect: Material qualifier missing: HPE's advisory states that end-of-maintenance versions are presumed affected and that end-of-support deployments are 'potentially impacted', which matters for the 10.6/10.3/8.12 branches the entry discusses.
   - Ground truth: 'Product software versions that have reached End of Maintenance (EoM) are presumed to be affected by the vulnerabilities unless explicitly stated otherwise and are not covered by this security advisory. ... such installations should be considered potentially impacted by the listed CVE.'
   - URL: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05162.txt
   - Fix: Add the EoM/EoS presumption to the affected-versions paragraph.

#### 2026-10-22/litellm-1-107-0-pypi-docker-credential-stealer-lookalike — factual-error

1. **[factual-error] frontmatter evidence[] (publisher: Aikido Security)**
   - Claim: PyPI has now quarantined version 1.107.0.
   - Defect: Not a contiguous passage of the cited page: two words are dropped from inside the quotation marks (pre-pass lead confirmed). Meaning is preserved.
   - Ground truth: 'Update: PyPI has now quarantined and removed version 1.107.0.'
   - URL: https://www.aikido.dev/blog/litellm-compromised-infostealer-rat
   - Fix: Quote the full sentence: 'PyPI has now quarantined and removed version 1.107.0.'

#### 2026-10-23/blackx-uefi-bootkit-baton-drop-revocation-default-off — imprecision

1. **[imprecision] frontmatter cves[CVE-2022-21894].fixed / .affected**
   - Claim: mitigation only when the revocation steps in Microsoft's KB5025885 are applied
   - Defect: (low confidence) The cited Microsoft article (KB5025885) is titled for CVE-2023-24932 and mentions CVE-2022-21894 only as the title of a reference link, so it does not itself state that its revocation steps are the mitigation for Baton Drop; that equivalence rests on Kaspersky's statement that the Baton Drop patch is designed to revoke the Windows Production PCA 2011 certificate.
   - Ground truth: KB5025885: 'Mitigations against the Secure Boot bypass detailed in CVE-2023-24932 are included in the Windows security updates that were released on July 9, 2024, and later updates. However, these mitigations are not enabled by default.' Securelist: 'the patch for the Baton Drop vulnerability is designed to revoke the "Windows Production PCA 2011" certificate ... the user has to trigger it manually'.
   - URL: https://support.microsoft.com/en-us/servicing/os/windows/2023/03/how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023
   - Fix: Attribute the CVE-2022-21894 `fixed` text to Kaspersky's reading and keep KB5025885 as the CVE-2023-24932 reference only.

#### 2026-10-23/mythicratatoskr-yggdrasil-mesh-c2-uac-0099-sandworm-wiper — imprecision

1. **[imprecision] body, **Triage:** line**
   - Claim: ESET notes that legitimate users adopt Yggdrasil for resilient connectivity, research and hobby networking, so a single mesh connection needs a business-owner check, while a mesh peer connection together with a service named like an updater is the stronger combination
   - Defect: (low confidence) Only the first half is ESET's: the cited report says legitimate users adopt such meshes for resilient connectivity, research and hobby networking. The business-owner check and the 'stronger combination' with an updater-named service are the entry's own inference but are placed under ESET's citation.
   - Ground truth: ESET: 'Legitimate users adopt such meshes for resilient connectivity, research, and hobby networking.' and 'MythicRatatoskr is started as a Windows service with the name ieupdate.' (no triage guidance in the report)
   - URL: https://www.welivesecurity.com/en/eset-research/mythicratatoskr-yggdrasil-enabled-backdoor-deployed-uac0099-sandworm-collaboration/
   - Fix: Split the sentence so ESET's observation is cited and the triage conclusion is stated as analysis, or drop the 'stronger combination' clause.

### Clean entries

- 2026-10-23/fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes
- 2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi
- 2026-10-23/fortinet-hardening-release-fortios-fortimanager-fortimail
