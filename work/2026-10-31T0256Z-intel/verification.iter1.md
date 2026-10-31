**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-31T04:12:26Z · ended_at=2026-10-31T04:34:58Z · duration_seconds=1352

## Verification report — 2026-10-31T0256Z-intel (iteration 1)

Scope: 6 new entries, 5 updated entries (whole files plus `git diff HEAD`), the run record, all 230 ledger claims (rows in `verification.iter1.claims.yaml`: 216 ok, 11 F3, 3 F4, 0 unreadable). Ivanti's hub advisory and Drupal's advisory page were the only unreadable primaries (hub: login shell on every transport, disclosed by the entry; drupal.org read with WebFetch, exact sentences returned). No prior-iteration deltas (first pass).

### Citation does not support the claim

- #1 `2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap` — "lists the hotfix builds 9.14.1P18HF1, 9.15.1P20HF1, 9.16.1P16HF1, 9.17.1P11HF1, 9.18.1P8HF1 and 9.19.1P3HF1" ([NetApp advisory data](https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)). Live data lists seven builds: also 9.19.1P4 (revision 10.0, 20261029, "ONTAP 9.19.1P4 added to Software Versions and Fixes"). The summary ("9.14.1P18HF1 to 9.19.1P3HF1"), cves fixed text, body sentence and the Exposure clause ("a release other than the fixed builds") all omit it, so a 9.19.1P4 cluster reads as exposed. Claims 67bfdfc3b3, ba8577abbb, a55e6659cf, de2c9ccc2e.
- #2 `2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day` — "BeyondTrust patched Privileged Remote Access too, which shares the code" and actions[0] "which BeyondTrust patched as a precaution". The blog says Engineering "built and tested the patch for all supported versions of Remote Support and Privileged Remote Access" and SaaS PRA instances were auto-patched; "shares the code" and "as a precaution" are in no source, and BT26-05 lists Remote Support (RS) as the only impacted product. Claim 39682a7bb4.
- #3 (low confidence) `2026-10-31/cve-2026-98432-...` — "CIQ had published no patched kernel for Rocky Linux 8, 9 or 10" and `affected: Rocky Linux 8, 9 and 10 (CIQ lists no patched kernel)`. CIQ: "no patched CIQ kernel had been published for any variant listed in the Patched Kernels table"; the table is RLC Pro LTS 9.6, RLC Pro LTS 8.10, RLC Pro 10; for community Rocky it says "refer to Rocky Linux Errata". Claims 1b09bce934, 0e86ae7ea6.
- #4 (low confidence) `2026-10-31/cve-2026-98432-...` — "Because the trigger is a SYN packet with IP options and a lost race only fails the handshake, so the attacker can retry ([Anthropic])". Anthropic carries the retry property only; IP options is CIQ's. Claim ee68ec7ae9.
- #5 (low confidence) `2026-10-31/cve-2026-118539-...` — "Drupal's own guidance is an order audit, so compare each order's state, totals and payment status with the payment provider's records". Drupal/SecurityWeek: "Sites should audit their orders for inconsistencies". The reconciliation method is the entry's own and unmarked as inference. Claim 58732c872a.
- #6 (low confidence) `2026-10-31/teams-help-desk-...` — "using an organisation-themed tenant name and a support-style display name". Microsoft: "Across the broader activity, organization-themed onmicrosoft.com tenant names and support-oriented display names were used", not said of the two intrusions. Claim 85102c548e.
- #7 (low confidence) `2026-10-31/progress-ws-ftp-...` — "The record for CVE-2026-84295 names versions before 2024.0.6 and 2025.0.3 ... ([EUVD-2026-113022])". That record is CVE-2026-90865 (2024.0.7/2025.0.4 only); the 84295 text is on EUVD-2026-113016. Claim cb2b97b384.
- #8 (low confidence) Citation dates of living pages are read or revision dates: Quest KB 4385046 cited 2026-10-28 (page "Published Time: 2026-10-21T09:58:20"); NetApp advisory cited 2026-10-26 (first release 20261021); NetApp KB cited 2026-10-26 (page date 2026-10-23); Red Hat CVE page cited 2026-10-31 (page date 2026-10-15). Check 2(e); fix may be a revision-date label.

### Unsupported / hallucinated facts

- #9 `2026-10-14/cve-2026-104935-...` sourcing_note — "the Canadian Centre for Cyber Security's bulletin and Rapid7's table name the middle 25.x line differently (25.2.2 and prior versus 25.1.2.2 and prior)". The bulletin as updated 2026-10-30 lists only "Versions prior to 25.1.1.3 / 25.1.3.1 / 22.8R2.6"; no 25.2.2. The matching Exposure sentence was dropped from the body this run but the sourcing_note still carries it.
- #10 (low confidence) `2026-10-16/cve-2026-102764-...` headline "now has a public Metasploit module" and `status: poc-public`. Rapid7: "A Metasploit module now implements the chain with PHP and Unix Command targets." The page never says it is published; `modules/exploits/linux/http/beyondtrust_rs_mrs_file_upload.rb` is 404 on metasploit-framework master (fetched this iteration). Claims 38c07a5f5f, 1002797d29.
- #11 (low confidence) `2026-10-31/progress-ws-ftp-...` — "since two of the flaws are command execution (an inference from the described flaws)". Of the three described flaws only CVE-2026-90865 is command injection. EUVD carries other command-execution records the entry omits (CVE-2026-90868, 9.9, PR:L; CVE-2026-90863, PR:H). Claim 907a4eaf79.

### Needs more research

- #12 `2026-10-29/php2shell-trend-micro-...` — the Quest KB it cites ends "October 29th, 2026: A new KACE SDA hotfix version 9.3.313 published ... accommodates updates for systems in hotfix versions 9.3.305-9.3.111 in addition to GA version 9.3.304"; 9.3.312 needs no further action only where already applied. Body, cves fixed and actions[1] name only 9.3.312.
- #13 (low confidence) `2026-10-31/cve-2026-98432-...` — BleepingComputer (cited): "Other Linux vendors, including Oracle Linux, Amazon Linux, and SUSE, have also released fixes for some affected kernel versions"; NCSC-NL (cited) lists Oracle Linux, SUSE, RESF Rocky, Azure Linux 3, Nutanix AHV, NetApp. The patch-state paragraph and affected_products stop at Debian, Ubuntu, RHEL.

### Surface contradiction

- #14 `2026-10-31/cursor-marketplace-...` — NCSC Switzerland post 13121 (cited as "carried the incident"): backdoor in the extension "on Open VSX", "Anthropic has removed the associated release the Open VSX extension, additionally pulling NPM and VSCode versions for 2.1.313 from their relevant registries", check VSCode for 2.1.313. Microsoft (cited): the malicious packages "were never published nor distributed from Microsoft Visual Studio Marketplace and from npm"; Cursor and Phorion: Cursor marketplace only. The entry takes Microsoft's side silently; add a `Contradiction:` line.

### Drop (low relevance / off-audience / duplicate)

- #15 (low confidence) `2026-10-31/progress-ws-ftp-...` — vulnerability entry with no exploitation, no PoC, Progress's bulletin and exploitation statement unread, no named Swiss exposure; priority argument is CVSS 10.0 on republished CNA records plus 2023 precedent (check 11). Shorten to a few sentences or drop unless the bulletin or a Swiss nexus is found. Run-record PD-11(b) rationale is arguable; main agent may leave.

### Classification missing / inconsistent

- #16 (low confidence) `2026-10-31/cve-2026-118539-...` — `credibility: 1`, but SecurityWeek, The Hacker News and NCSC post 13124 all restate Drupal's advisory; exploitation has no independent confirmation. Credibility 2.

### Action-item discipline

- #17 (low confidence) `2026-10-31/teams-help-desk-...` actions[0] — restates the Defender takeaway's hardening list (HTTPS and EPA, drop unused endpoints, review templates) as generic AD CS hardening; the start-now task is the inventory step only.

### Editorial / less-is-more flags (advisory)

- #18 Drupal sourcing_note: "its page was read through a summarising reader" (fetch-transport vocabulary).
- #19 Broadcom body: "described in the entry on the PHP release" (internal cross-reference).
- #20 Trend update section "which the entry had as due on 2026-10-30" and QNAP sourcing_note "covered by the related PHP, PAN-OS and NetScaler entries" (self-reference).
- #21 Non-internal record summaries narrate record-keeping in all five updated entries ("the CVE records, the targets in the action and the analysis follow"; "The summary, CVE records, action and analysis follow."; "the CVE record gains the public-exploit status"); check 4c(d) says no more than the section states.
- #22 Ivanti body: "and Volexity found log entries removed; The operator then went after ..." (capital T after a semicolon).
- #23 Linux evidence quote carries two kernel commit hashes (style rule "no hashes"); a shorter verbatim substring avoids it.
- #24 Ivanti: CISA's alert, updated 2026-10-30, states the three chain CVEs affect "versions 25.1.1.2 and prior, 25.1.2.2 and prior, and 22.8R2.5 and prior"; it corroborates the headline's "25.1.1.2 and 22.8R2.5 fall short" and is already a cited URL (used only for the 2026-10-13 KEV date).

### Verdict

NEEDS_FIXES (truth: 11, editorial: 6, advisory: 7)

Changelog contract (check 4c): all five records carry this run's `run_id`, `updated_at` equals each record's `at`, each non-internal record has its matching `## Update` section, `fields` match the git diff, and no silent edit found. Dedup: no new entry overlaps `prior_coverage.json` or `state/cves_seen.json`; the Drupal, Linux, Broadcom, Cursor, Teams and WS_FTP findings are new. Missed angles: none evidenced; the SecurityWeek leads of 2026-10-29/30 (ESXi CVE-2026-41709, GitLab CVE-2026-97229 at Alpine, Silent Train, Cisco SD-WAN) are already in the store, and the borderline-drops in the run record are defensible. Coverage looks complete.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  item: "NetApp ONTAP fixed-build list (summary, cves[CVE-2026-109618].fixed, body, Exposure)"
  url_or_quote: "NetApp's advisory ... lists the hotfix builds 9.14.1P18HF1, 9.15.1P20HF1, 9.16.1P16HF1, 9.17.1P11HF1, 9.18.1P8HF1 and 9.19.1P3HF1 (https://security.netapp.com/adv_api/advisory/NTAP-20261021-0021)"
  summary: "Live advisory data lists seven fixed builds: the six named plus 9.19.1P4 (revision 10.0, 20261029: 'ONTAP 9.19.1P4 added to Software Versions and Fixes'). The summary ('9.14.1P18HF1 to 9.19.1P3HF1'), the cves fixed text, the body sentence and the Exposure clause ('a release other than the fixed builds') all omit it, so a cluster on 9.19.1P4 reads as exposed. Add 9.19.1P4 in all four places."
- code: F4
  category: hallucinated-fact
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "sourcing_note (superseded statement about the Canadian Cyber Centre bulletin)"
  url_or_quote: "the Canadian Centre for Cyber Security's bulletin and Rapid7's table name the middle 25.x line differently (25.2.2 and prior versus 25.1.2.2 and prior)"
  summary: "The bulletin as updated 2026-10-30 (https://cyber.gc.ca/en/alerts-advisories/ivanti-security-advisory-av26-1035) lists only 'Versions prior to 25.1.1.3 / 25.1.3.1 / 22.8R2.6' and carries no '25.2.2' line; the body dropped the matching Exposure sentence this run but the sourcing_note still asserts it. Remove or rewrite the clause."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "Privileged Remote Access 'shares the code' / 'patched as a precaution' (body Exposure and actions[0])"
  url_or_quote: "BeyondTrust patched Privileged Remote Access too, which shares the code ([BeyondTrust, 2026-10-15](https://www.beyondtrust.com/blog/entry/bt26-05)); actions[0]: 'apply it to self-hosted Privileged Remote Access appliances too, which BeyondTrust patched as a precaution'"
  summary: "The BeyondTrust blog says Engineering 'built and tested the patch for all supported versions of Remote Support and Privileged Remote Access' and that SaaS PRA instances were auto-patched; it never says PRA shares the code or that the patch was precautionary, and advisory BT26-05 names Remote Support (RS) as the only impacted product. Drop 'which shares the code' and 'as a precaution', or cite a source for them."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "headline 'now has a public Metasploit module' and cves[].status poc-public"
  url_or_quote: "BeyondTrust Remote Support zero-day now has a public Metasploit module; the actor's persistence survives reset"
  summary: "(low confidence) Rapid7 writes 'A Metasploit module now implements the chain with PHP and Unix Command targets.' and shows an msfconsole 'use exploit/linux/http/beyondtrust_rs_mrs_file_upload' screenshot but never says the module is published; that path returns 404 on metasploit-framework master when fetched this iteration. Say 'Rapid7 reports a Metasploit module' or confirm the merge."
- code: F3
  category: claim-not-supported
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "Rocky Linux 8, 9 and 10 'CIQ had published no patched kernel' (body and cves[].affected)"
  url_or_quote: "and CIQ had published no patched kernel for Rocky Linux 8, 9 or 10 ([CIQ, 2026-10-30](https://kb.ciq.com/article/security-advisories/cve-2026-98432-mitigation))"
  summary: "(low confidence) CIQ says 'no patched CIQ kernel had been published for any variant listed in the Patched Kernels table', and that table lists RLC Pro LTS 9.6, RLC Pro LTS 8.10 and RLC Pro 10 only; for Rocky Linux community releases it says 'refer to Rocky Linux Errata'. The claim should name the CIQ LTS/Pro variants, not Rocky 8/9/10."
- code: F3
  category: claim-not-supported
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "Detection clause cited to Anthropic"
  url_or_quote: "Because the trigger is a SYN packet with IP options and a lost race only fails the handshake, so the attacker can retry ([Anthropic, 2026-10-27](https://www.anthropic.com/research/discovering-vulnerabilities-with-claude))"
  summary: "(low confidence) The Anthropic page carries the retry property ('a lost race only fails the handshake') but says nothing about IP options; the SYN-with-IPv4-options trigger is CIQ's statement. Split the citation."
- code: F3
  category: claim-not-supported
  section: 2026-10-31/cve-2026-118539-drupal-commerce-core-access-bypass-exploited
  item: "Detection line attributes an order-reconciliation method to Drupal"
  url_or_quote: "Drupal's own guidance is an order audit, so compare each order's state, totals and payment status with the payment provider's records and look for orders that do not reconcile ([SecurityWeek, 2026-10-30])"
  summary: "(low confidence) Drupal/SecurityWeek say only 'Sites should audit their orders for inconsistencies'; the comparison against payment-provider records (also in actions[0]) is the entry's own method and is not marked as inference, unlike the next sentence."
- code: F3
  category: claim-not-supported
  section: 2026-10-31/teams-help-desk-impersonation-quick-assist-ad-cs-esc1-esc8
  item: "organisation-themed tenant name and support-style display name attributed to these two intrusions"
  url_or_quote: "that began with an external Teams contact, using an organisation-themed tenant name and a support-style display name"
  summary: "(low confidence) Microsoft: 'Across the broader activity, organization-themed onmicrosoft.com tenant names and support-oriented display names were used'; it does not say so of the two investigated intrusions. Reword to 'across the broader activity'."
- code: F3
  category: claim-not-supported
  section: 2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10
  item: "version text of CVE-2026-84295 cited to another CVE's record"
  url_or_quote: "The record for CVE-2026-84295 names versions before 2024.0.6 and 2025.0.3 as affected, and the records for the other two name versions before 2024.0.7 and 2025.0.4 ([ENISA EUVD, 2026-10-29](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-113022))"
  summary: "(low confidence) EUVD-2026-113022 is CVE-2026-90865 and carries only the 2024.0.7/2025.0.4 text; the 2024.0.6/2025.0.3 text for CVE-2026-84295 is on EUVD-2026-113016. Cite both records."
- code: F4
  category: hallucinated-fact
  section: 2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10
  item: "Detection line: 'two of the flaws are command execution'"
  url_or_quote: "process creation by the service or its web worker, since two of the flaws are command execution (an inference from the described flaws)"
  summary: "(low confidence) Of the three flaws the entry describes, only CVE-2026-90865 is a command injection (CVE-2026-84295 is credential access, CVE-2026-90867 admin-console access control); no second command-execution flaw is named in the entry or its cited records. EUVD does carry other command-execution records (e.g. CVE-2026-90868, 9.9, authenticated) the entry omits; either name them or say 'one'."
- code: F3
  category: claim-not-supported
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap; 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "citation dates of living status pages carry read or revision dates, not publication dates"
  url_or_quote: "Quest KB 4385046 cited 2026-10-28 (page 'Published Time: 2026-10-21T09:58:20'); NetApp advisory cited 2026-10-26 (first release 20261021) and NetApp KB cited 2026-10-26 (page date 2026-10-23); Red Hat CVE page cited 2026-10-31 (page date 2026-10-15)"
  summary: "(low confidence) Check 2(e): two or more days of drift between the citation date and the page's own publication date. These are living pages, so the fix may be to label them as revision dates rather than change them."
- code: F8
  category: needs-more-research
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  item: "Quest KACE SDA fixed build"
  url_or_quote: "the SDA 9.3 hotfix 9.3.312 with PHP 8.3.36 followed; actions[1]: 'Install KACE SMA 15.0 CU5 or 15.1 CU2 and the SDA 9.3 hotfix 9.3.312'"
  summary: "The Quest KB the entry cites ends with 'October 29th, 2026: A new KACE SDA hotfix version 9.3.313 published'; 9.3.313 'accommodates updates for systems in hotfix versions 9.3.305-9.3.111 in addition to GA version 9.3.304', and '9.3.312 ... no further action is required' only for systems already on it. The entry, which was updated this run, still names only 9.3.312 in the body, the cves fixed text and the action."
- code: F9
  category: surface-contradiction
  section: 2026-10-31/cursor-marketplace-claude-code-extension-ssh-backdoor
  item: "NCSC Switzerland post 13121 versus Microsoft on where the package was published"
  url_or_quote: "Anthropic told Microsoft its systems were not compromised and that it did not build the package, and Microsoft confirms the packages were never published to the Visual Studio Marketplace or npm; NCSC Switzerland carried the incident on 2026-10-30 ([NCSC Switzerland](https://security-hub.ncsc.admin.ch/#/posts/13121))"
  summary: "Post 13121 says the backdoor was in the extension 'on Open VSX', that 'Anthropic has removed the associated release the Open VSX extension, additionally pulling NPM and VSCode versions for 2.1.313 from their relevant registries', and tells readers to check VSCode for 2.1.313. Microsoft: the malicious packages 'were never published nor distributed from Microsoft Visual Studio Marketplace and from npm'; Phorion and Cursor place it in the Cursor marketplace only. The entry cites the NCSC post as corroboration without surfacing the conflict; add a Contradiction line (Swiss readers will see the NCSC wording first)."
- code: F8
  category: needs-more-research
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "other distributions' status omitted"
  url_or_quote: "Debian's security kernels are fixed while Ubuntu 22.04 to 26.10 and RHEL 8 to 10 had no fixed kernel on 2026-10-30"
  summary: "(low confidence) BleepingComputer (cited): 'Other Linux vendors, including Oracle Linux, Amazon Linux, and SUSE, have also released fixes for some affected kernel versions'; NCSC-NL (cited) lists Oracle Linux, SUSE, RESF Rocky, Azure Linux 3, Nutanix AHV and NetApp as affected products. affected_products and the patch-state paragraph name only Linux kernel, Ubuntu and RHEL, so a SUSE or Oracle shop gets no status."
- code: F7
  category: drop
  section: 2026-10-31/progress-ws-ftp-server-cve-2026-84295-unauth-cvss-10
  item: "no-exploitation, no-PoC CVSS-driven vulnerability entry"
  url_or_quote: "No source reports exploitation: CISA's catalog holds no 2026 WS_FTP flaw"
  summary: "(low confidence) check 11: a vulnerability entry should demand action beyond the patch cycle (exploited, imminent mass exploitation, public PoC on an exposed edge). This one rests on a CVSS 10.0 vector from CNA records republished by EUVD, Progress's bulletin and exploitation statement are unread, there is no PoC and no named Swiss exposure. The run record's PD-11(b) rationale is exposure-based and arguable; shorten to a few sentences or drop unless Progress's bulletin or a Swiss nexus is found."
- code: F17
  category: classification
  section: 2026-10-31/cve-2026-118539-drupal-commerce-core-access-bypass-exploited
  item: "classification credibility 1"
  url_or_quote: "classification: {reliability: A, credibility: 1}"
  summary: "(low confidence) All three corroborating sources (SecurityWeek, The Hacker News, NCSC post 13124) restate Drupal's advisory ('Drupal has confirmed the attacks'); none independently confirms exploitation, and the entry's own sourcing_note says no source says how or since when. Credibility 2 fits the corroboration shown."
- code: F18
  category: action-item-discipline
  section: 2026-10-31/teams-help-desk-impersonation-quick-assist-ad-cs-esc1-esc8
  item: "actions[0]"
  url_or_quote: "In every forest with an enterprise CA, require HTTPS and Extended Protection for Authentication on each AD CS Web Enrollment and Certificate Enrollment Web Service endpoint and remove the ones nobody needs, and list the certificate templates that accept requester-supplied identity with broad enrollment rights"
  summary: "(low confidence) check 10b(b): the action restates the Defender takeaway's hardening list (HTTPS and EPA on enrollment endpoints, drop unused endpoints, review templates) as canonical AD CS ESC1/ESC8 hardening that is equally true without this finding. A start-now task would be the inventory step only (enumerate /certsrv and CES endpoints and templates that accept requester-supplied subject names)."
- code: F11
  category: editorial-advisory
  section: 2026-10-31/cve-2026-118539-drupal-commerce-core-access-bypass-exploited
  item: "sourcing_note names a fetch transport"
  url_or_quote: "its page was read through a summarising reader, so its wording is carried from that reading"
  summary: "Fetch-transport vocabulary in a reader-facing field; the fix is two sentences of provenance (vendor primary; wording carried from SecurityWeek, The Hacker News and NCSC Switzerland, which quote it)."
- code: F11
  category: editorial-advisory
  section: 2026-10-31/php2shell-broadcom-sepm-carbon-black-app-control-casma
  item: "reference to another entry in reader-facing prose"
  url_or_quote: "The flaw is in the PHP runtime and is described in the entry on the PHP release."
  summary: "Composition-rationale cross-reference; state what the flaw is (two PHP memory-safety flaws, CVE-2026-109618 and CVE-2026-109619) and let references[] carry the link."
- code: F11
  category: editorial-advisory
  section: 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap; 2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed
  item: "self-reference to 'the entry' and 'related ... entries' in reader-facing text"
  url_or_quote: "Update section: 'which the entry had as due on 2026-10-30'; QNAP sourcing_note: 'are covered by the related PHP, PAN-OS and NetScaler entries'"
  summary: "Workflow-internal self-reference (check 12). Say 'which Trend Micro had listed as due on 2026-10-30' and name the vendor advisories or drop the clause."
- code: F11
  category: editorial-advisory
  section: all five updated entries
  item: "non-internal record summaries narrate record-keeping"
  url_or_quote: "'the CVE records, the targets in the action and the analysis follow' (Ivanti); 'the title, summary, CVE records, action and analysis now say so, and the superseded table-row quote is replaced' (QNAP); 'The summary, CVE records, action and analysis follow.' (Trend); 'the summary, CVE records, sources, evidence and analysis follow' (Cisco); 'the CVE record gains the public-exploit status' (BeyondTrust)"
  summary: "Check 4c(d): the summaries state more than the sections do (which fields moved); that is what fields[] is for. Trim each summary to the delta the section states."
- code: F11
  category: editorial-advisory
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "typo in rewritten analysis"
  url_or_quote: "and Volexity found log entries removed; The operator then went after the Active Directory service account"
  summary: "Capital T after a semicolon (the rewrite fused two sentences); use a full stop."
- code: F11
  category: editorial-advisory
  section: 2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root
  item: "evidence quote carries two kernel commit hashes"
  url_or_quote: "Issue introduced in 4.4 with commit 079096f103faca2dd87342cca6f23d4b34da8871 and fixed in 6.12.113 with commit 11a03ce3c4a62d84c10ccdfe47f8075006498568"
  summary: "Style rule 'no hashes': git commit ids are not attacker IOCs but a mechanical scan will read them as hashes; a shorter verbatim substring ('Issue introduced in 4.4') avoids it."
- code: F11
  category: editorial-advisory
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "stronger source for the headline claim not cited"
  url_or_quote: "headline: '25.1.1.2 and 22.8R2.5 fall short'"
  summary: "CISA's alert (https://www.cisa.gov/news-events/alerts/2026/10/13/cisa-urges-patching-newly-exploited-vulnerability-ivanti-connect-secure, updated 2026-10-30) states the three chain CVEs affect 'versions 25.1.1.2 and prior, 25.1.2.2 and prior, and 22.8R2.5 and prior'. It corroborates the Cyber Centre list and lets the entry cite a primary-authority source for the headline instead of resting on one bulletin; the entry cites that URL only for the 2026-10-13 KEV date."
```
