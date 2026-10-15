**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-15T03:58:17Z · ended_at=2026-10-15T04:10:07Z · duration_seconds=710

## Verification report — 2026-10-15T0256Z-intel (iteration 2)

Scope: iteration 2, post-fix pass. Whole ledger: all 100 claims of `claims.iter2.yaml` have a verdict row in `verification.iter2.claims.yaml` (97 ok, 1 F14, 2 F4; 0 unreadable). Four new entries and the two updated entries read whole; `git diff HEAD` read for both updated entries; run record read. Every cited page was fetched this iteration (`extract` for Cisco, PAN-OS, BleepingComputer x3, GitHub advisory, GitHub issue 354, Nextcloud forum, Huntress, PKZH, Publica, Censys, CERT-FR, AFP, BFMTV, Infosecurity, Cooling Post, Blick; `ncsc-csh post 13054`; `cisa-kev` plus `WebFetch` for the CISA alert; `pdf` and the gate's saved body for the BPK and BLVK notices; CVE Services record for CVE-2026-110447; Claroty page for the run-record note). Plus one page no earlier pass read: the Collabora vendor advisory GHSA-g3vx-3m76-fghh, linked from the last comment of issue 354. That page is the source of the firm finding below.

### Prior-iteration deltas, each remediation checked against its source

- F3 PAN-OS (BleepingComputer's questions): CORRECT. BleepingComputer: "BleepingComputer contacted Palo Alto Networks to learn when exploitation began, who is behind the attacks, and whether attackers compromised firewalls or used them to access internal networks." The entry now says exactly those three questions, and the credential-source gap is the advisory's own omission.
- F3 WatchGuard (Bing query): CORRECT. Huntress: administrator "had searched Bing for 'watchguard vpn sll download.'"; the entry no longer quotes and says "a WatchGuard VPN download with a typo in the query".
- F4 Cisco (cluster rebuild): CORRECT. Cisco: "private SSH keys used for this communication could be accessed on a compromised appliance" and "Cisco strongly recommends restoring to a secure configuration each member of a cluster that contains at least one compromised appliance". `immediate_action` and the Defender takeaway now carry "strongly recommends restoring ... could be accessed".
- F4 Publica (PKZH "not yet a customer"): CORRECT. PKZH: "arbeitet derzeit mit einem anderen Softwareanbieter. Der Wechsel auf das Verwaltungssystem von PK Softech AG ist für Anfang 2027 vorgesehen." Record summary, sourcing_note and actions[1] now say "currently uses another provider, plans to move ... early 2027".
- F4 run record (wrong entry id in the Single-source line): CORRECT. It now names `2026-10-15/fake-watchguard-vpn-client-site-credential-capture`, which exists.
- F13 Danfoss (Censys "candidates"): CORRECT. Censys: "Danfoss patched several vulnerabilities in its AK-SM 800A controllers more than a year earlier" (CVE-2025-41450, -41451, -41452) and "operators don't appear to be patching their controllers; they're simply taking them off the Internet". Main text, section, record summary and sourcing_note say "points to three flaws Danfoss patched" and attribute the reading to Censys. Figures check: 1,825 (11 Oct) to 537 (14 Oct), -71 percent; -71 / -68 / -72 percent per build group; 1,166 to 966 elsewhere; Poland 81, Romania 80 percent; below 4.2 all three, 4.2.4 two open, 4.3.1 or later patched; current 5.3.2.
- F13 WatchGuard (managed-service clause): CORRECT. Huntress: "a user account at a managed service provider"; the Exposure line now says only that.
- F14 Publica ("first communal pension fund"): CORRECT, "first" is gone and no "first" remains in the section.
- F18 Publica actions[1]: CORRECT. Imperative kept ("ask the supplier or the fund in writing whether your data, test data included, was in the affected environment and what it holds"), per-fund recap dropped.
- F11 run-record Claroty note: ACCURATE. Claroty: "Successful authentication through this hidden mechanism results in a fully authenticated administrative session"; Censys: "allowed an unauthenticated actor to log in as an administrator"; the older entry `2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce` says the bypass "discloses a web report with internal IPs, usernames and store names", and Claroty's page (extract and raw HTML) contains none of those words. "Probably needs a correction record" is a fair, hedged wording; the older entry was not touched.
- F11 Collabora forum hedge: CORRECT, "as far as the poster knew" matches "since AFAIK no warning or CVE has been published". The BFMTV paragraph is pre-existing and was left.
- F16 Collabora priority (declined): judged below. I do not think the rebuttal holds.

### Unsupported / hallucinated facts

- F4 #1 `2026-10-15/cve-2026-110447-collabora-code-server-nextcloud-rce`, actions[0]: "Update the Collabora Online Built-in CODE Server app (richdocumentscode) to 26.4.303 on every Nextcloud server that runs it, or disable the app until you can" and Defender takeaway: "or disable it meanwhile as the reporting hoster did". The vendor's own advisory (https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh, published 2026-10-14, linked from the last comment of the cited issue) says: "It is not sufficient to disable the app to avoid the problem, it must be upgraded to >= 26.4.303 or removed." The cited issue 354 itself carries a commenter's report after deactivation: "The http request from above still uses proxy.php from the deactivated app. Is this a correct behavior?" The entry recommends an interim step the vendor says does not stop the attack. Fix: "update to 26.4.303 or remove the app; disabling does not stop the request".

### Quantifier without source

- F14 #2 (low confidence) same entry, title "exploited since 10 September to plant PHP web shells", headline "has been exploited for web shells since 10 September", actions[1] "search the web access logs back to 2026-09-10". Issue 354 (posted 2026-09-11): "Since yesterday we're experiencing succesful hacks on our systems", first log line 10/Sep/2026. The advisory says "exploited in the wild in September and October 2026". 10 September is the first date one hoster logged, not a documented start. Fix: "first reported by a hoster on 10 September", hunt window "back to at least early September".

### Strengthen primary source

- F6 #3 same entry, sources[0] is "https://github.com/advisories/GHSA-f97p-r72q-64h2" (an unreviewed database record). The vendor advisory https://github.com/CollaboraOnline/online/security/advisories/GHSA-g3vx-3m76-fghh ("Unauthenticated OS command injection in the richdocumentscode proxy", Critical 9.2, patched 26.4.303, author caolanm, 2026-10-14) was fetched this iteration. Make it the primary.

### Needs more research

- F8 #4 same entry, Exposure and Defender takeaway lack three vendor-advisory facts: "Users of EOL Nextcloud <= 29 should upgrade their Nextcloud or remove this app"; the attack "only works while the built-in CODE server is not running. So on a container restart, an upgrade, or after a crash" (the entry says only "for example right after a restart"); "This is not the same path as CVE-2025-66208, and the fix for that issue does not prevent it" (a server patched against the earlier flaw is still open).

### Drop / priority

- F16 #5 (low confidence) same entry, `priority: notable`. The declined rebuttal says no source puts a constituency deployment on the internet. The high bar asks for plausible exposure, not demonstrated exposure, and its disqualifiers (unexploited flaw, non-default configuration, out-of-nexus incident) do not describe an exploited, unauthenticated, Critical 9.2 command injection whose web shells survive the update. The store already rated a Nextcloud Server 2FA bypass `high` (`2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass`) and carries a Nextcloud entry with sector public-sector (`2026-07-10/nextcloud-gmbh-elasticsearch-exposure-msb-nrw`). The narrower deployment mode ("rather rarer", per the maintainers) is a fair discount on breadth, not a reason to sit below the bar. Raise to `high`, or add one sentence on why the Built-in CODE mode is implausible in the constituency. This one is a judgement call.

### Checks that came back clean

- Cisco CVE-2026-76519: advisory dated 2026-10-14, CVSS 3.1 9.8, CWE-23 on the page, exploitation sentence, no workaround, fixed Content Scanner Tools 25.3.0.5525, AsyncOS 15.5.5-014 and 16.5.0-780, 16.0 "Migrate to a fixed release", Secure Email and Web Manager and Secure Web Appliance not affected, Cloud Gateway "no action is required", log messages, cluster-key note, forensic-data warning. KEV: CVE-2026-76519 added 2026-10-14 (catalog JSON and the CISA alert). BleepingComputer: CVE-2026-76461 "last month". Priority critical is within the bar; classification A/2 matches the PSIRT tier.
- PAN-OS CVE-2026-0322: ATTACKED tag, "Very limited exploitation", CVSS-B 8.6 and 8.5 jump box, Threat IDs 510046 and 510047 with limits, 11.2.16 "(ETA: 10/15)", full fixed-build table, FAQ lists three addresses (none reproduced). `high` fits (credentials plus management reach).
- Collabora entry apart from the findings: GitHub advisory text, CVE record (CNA CVSS 4.0 baseScore 9.2, affected "< 26.4.303"), issue 354 narrative (hoster, shell substitution, encoded traversal, web shells, wallet and password-manager search, no archiving commands, integrity-check report, sudo mail, maintainers' replies by the repository owner), forum post (affected and not-affected lists, "AFAIK").
- WatchGuard entry: every claim holds against Huntress (Bing click-through, 150-line popup.js, JSON to a collector, forced "Incorrect data" first attempt, genuine Authenticode-signed installer from WatchGuard's CDN, 21 seconds, registration dates, thin detections, domain offline 2026-10-13, January Secplicity and March Microsoft/Storm-2561 context relayed by Huntress). Single-source and B/2 are consistent.
- Publica update and Danfoss improvement: changelog contract holds (`run_id` this run; `updated_at` moved only by the Publica `update`; matching section `at` values; no silent edits in either diff; `fields` name what moved; summaries match sections; no supersession conflict). PKZH and Publica evidence quotes are verbatim and the English is faithful. BPK "keine Hinweise ... Jedoch kann dies nicht restlos ausgeschlossen werden" and BLVK "ob und in welchem Umfang" hold for actions[0].
- Dedup: none of the three new CVE ids appeared in the store before this run (`git diff HEAD -- state/cves_seen.json` adds them); AhsayCBS pair already covered; references[] on the Cisco and PAN-OS entries point to existing, distinct entries.
- Style: no IOCs, no em dashes, no workflow vocabulary in reader-facing text, no KEV deadline used as a reason. `immediate_action` plus `actions[]` overlap on the Cisco entry matches the store's practice on earlier critical entries.
- Run record: counts, KEV sweep file, registry additions, `sources_changed` rows against the `sources.json` diff, the Single-source line, the Claroty note and the previous record's `publish_status: ok` all hold. Gate: 55 pass, 0 warn, 3 fail, the three being the bookkeeping items the main agent resolves.
- Missed angles (F10): none I can evidence. NCSC.ch hub posts of 2026-10-13 and 14 (Danfoss 13054, Ivanti Connect Secure 13055, Adobe 13061, Citrix XenServer 13059, Microsoft 13056) are all covered by earlier entries or by this run's drop lines; two web searches found no further in-window exploited or Swiss public-sector item. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 3, advisory: 0)

F4 #1 is the firm finding: a reader following the entry would disable the app and believe the server protected, while the vendor says it is not. F14, F6, F8 and F16 are the supporting or low-confidence items; F6 and F8 are cured by adding the vendor advisory the cited issue already links.

### Findings summary (machine-readable)

See `work/2026-10-15T0256Z-intel/verification.iter2.findings.yaml` (5 records). Claim rows: `work/2026-10-15T0256Z-intel/verification.iter2.claims.yaml` (100 rows).
