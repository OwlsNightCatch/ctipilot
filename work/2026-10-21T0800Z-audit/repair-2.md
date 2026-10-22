# Repair worker repair-2, cleanup wave 02 (2026-10-21T0800Z-audit)

Batch: `work/2026-10-21T0800Z-audit/batch-2.yaml` (11 entries). Scratch, fetched bodies and record texts: `work/2026-10-21T0800Z-audit/repair-2/` (`src/`, `e<NN>-summary.txt`, `e<NN>-section.md`). No W1-F drafts existed for this batch.

Records written: 10 (4 correction, 6 improvement, 0 update, 0 internal). Entry without a record: 1 (FortiSandbox).

## Per entry

### 2026-06-03/ncsc-switzerland-warns-of-cyber-operations-around-the-g7-via
- Record: improvement, at 2026-10-21T08:21:06Z, fields [body].
- W1-C clean. Legacy duties: rating A/3 and [T1498] already present; added **Exposure** (NCSC: DDoS on Swiss organisations' websites and services, participants and their organisations as likely targets; the analyst-judgement scope sentence moved here unchanged; ZENDATA supply-chain framing) and **Detection** (traffic volume and availability; ZENDATA's under-ten-minute attacks and post-event hunt). Triage omitted: no honest discriminator in the sources. Takeaway present.
- Ground truth: https://www.bacs.admin.ch/en/26-cyberresilienz-g7-en , https://zendata.security/2026/05/03/g7-evian-2026-the-cyber-risk-map-and-recommendations/

### 2026-06-04/ncsc-switzerland-booking-com-breach-feeds-two-pronged-whatsa
- Record: improvement, at 2026-10-21T08:21:35Z, fields [body, techniques].
- W1-C clean. Legacy duties: rating A/2 present; added T1684.001 (Impersonation of Booking.com and hotel customer service; T1656 is revoked in ATT&CK v20); added **Exposure**, **Detection**, **Triage** (NCSC: a refund never asks for login details or a QR-code scan; booking details do not make a message genuine); takeaway rewritten on NCSC's out-of-band verification advice, replacing its unsourced detection claim.
- Ground truth: https://www.bacs.admin.ch/en/26w22-en

### 2026-06-09/cve-2026-50751-check-point-security-gateway-ikev1-vpn-authen
- Record: improvement, at 2026-10-21T08:17:26Z, fields [actions, body, immediate_action, sources].
- Applied finding 2 (lookback criterion): `immediate_action` and `actions[0]` now use Check Point's sk185033 hunt (completed IKEv1 Quick Mode "Key Install" events before the fix, from unrecognised users or source IPs) instead of "VPN sessions without a matching MFA/password event". sk185033 added to sources. Ground truth: https://support.checkpoint.com/results/sk/sk185033 (decoded body: `repair-2/src/cp-sk185033.txt`).
- Declined finding 1 (watchTowr "earlier" analysis): already fixed by 2026-10-11T1307Z-audit (2026-06-17 section and its own correction say analysis and PoC came together on 2026-06-12).
- Declined finding 3 (sectors): sector tags are the profile's relevance framing, not a source claim; the body names no victim sector. Same disposition as W1-E item 6.
- Legacy duties: rating A/1 and [T1190, T1133] present; Detection gains the sk185033 hunt, its 7 May to 5 June range and the IPS visibility protection; **Triage** added (sk185033: inspect pre-fix Quick Mode events for unrecognised users or source IPs).

### 2026-06-10/ncsc-ch-week-23-coordinated-surge-in-job-seeker-targeting-fa
- Record: improvement, at 2026-10-21T08:21:59Z, fields [body, techniques].
- W1-C clean. Legacy duties: rating A/2 present; added T1684.001 (fake recruiter, fake "Swiss social welfare") and T1005 (wallet files); takeaway's embedded detection concept split into **Exposure**, **Detection** (marked inference, as before), **Triage** (NCSC: running a repository's commands is common in IT work; discriminator is origin plus credential/cookie/wallet-store reads), and a takeaway on revoking sessions and rotating stored credentials. Dropped the unsourced "HR or talent teams handling candidate code" vector.
- Ground truth: https://www.bacs.admin.ch/en/26w23-en

### 2026-06-12/cve-2026-25089-fortinet-fortisandbox-unauthenticated-os-comm
- No record (legacy_duty false; nothing applies).
- Declined W1-B finding 1 (sectors) and W1-E item 6: declined on principle earlier (profile's relevance call); no reader-facing error, the body names no sectors.
- Declined W1-B finding 2 (NCSC-NL 4.2 range): already fixed by 2026-10-11T1307Z-audit (Exposure line covers 4.2; its Correction section carries the Contradiction; vendor range kept as authoritative in cves[]).
- Em dash in the title stays: the brief forbids a record only to fix em dashes.

### 2026-06-16/cve-2026-48611-cve-2026-48612-phpbb-unauthenticated-authenti
- Record: correction, at 2026-10-21T08:17:59Z, fields [body, sources, summary].
- Applied: 9.8 and 8.0 are the CVE records' CVSS 3.0 scores from HackerOne as numbering authority (cves[] already carried them since the 2026-10-11 internal record); summary and body now attribute them to the CVE record beside Pentest-Tools' 9.4/8.3, with heise as reporter. The 2026-09-30 Correction section no longer presents the "OAuth implementation" wording as the error; it now names the OAuth stop-gap as what did not hold (CVE record: reachable even when OAuth is not configured or enabled). Two EUVD pages added to sources.
- Ground truth (citable stand-in for the CVE record): https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-36375 , https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-36380 (API JSON in `repair-2/src/`).
- Legacy duties: all present already (B/2, [T1190], Exposure, Detection with post-patch check, Triage, takeaway).

### 2026-06-16/cve-2026-54420-litespeed-cpanel-whm-plugin-symlink-following
- Record: correction, at 2026-10-21T08:18:43Z, fields [body, cves, sources, summary].
- Applied finding 1: the CVE record's "exploited in the wild in May 2026" is restored in summary, body and the 2026-09-30 Correction section, with 2026-05-31 as LiteSpeed's alert date (EUVD-2026-36657; THN's quote of the description stops before that clause).
- Applied finding 2: `affected` "LiteSpeed user-end cPanel plugin before 2.4.8", `fixed` "cPanel plugin 2.4.8 (bundled with WHM PlugIn 5.3.2.1)"; `vector` local to zero-click, because the taxonomy defines `vector` as the victim-interaction axis only (`auth: post-auth` keeps the FTP/web-shell precondition, which the body states).
- Applied finding 3: body notes the CVE description's WHM PlugIn 5.3.2.0 boundary beside LiteSpeed's 5.3.2.1 (cited to THN, which quotes it).
- Legacy duties: A/1 and [T1068] present; LiteSpeed's false-positive discriminators moved into a **Triage** line; Detection gains the post-upgrade compromise check.
- Ground truth: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-36657 , https://blog.litespeedtech.com/2026/06/01/security-update-for-litespeed-cpanel-plugin-2/

### 2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed
- Record: correction, at 2026-10-21T08:19:18Z, fields [body].
- Applied finding 1: paragraph 1 now says firewall URLs and apparently valid credentials (some confirmed authentic by Beaumont), with 73,932 URLs / 194 countries / 21,632 domains attributed to Hudson Rock and ~75,000 devices to Beaumont. Sweep: the 2026-06-20 section's "73,932 internet-facing FortiGate devices" now reads "73,932 firewall URLs".
- Applied finding 2: SOCRadar's Lynx / INC attribution dated to its 29 June update (SOCRadar page), BleepingComputer kept for the negotiation-panel detail.
- Legacy duties: A/1 and 12 techniques present; Detection gains the FBI/USSS configuration comparison (accounts not previously on the device, deleted or changed originals).
- Ground truth: https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/ , https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/ , https://www.ic3.gov/CSA/2026/261006.pdf

### 2026-06-23/cve-2026-20896-gitea-docker-trust-all-reverse-proxy-default
- Record: improvement, at 2026-10-21T08:22:12Z, fields [body].
- W1-C clean. Legacy duties: everything present except Triage; added **Triage** from the GHSA (legitimate logins carry the header from the proxy; the exploit sends it on a direct connection and signs in with no password and no cookie).
- Ground truth: https://github.com/go-gitea/gitea/security/advisories/GHSA-f75j-4cw6-rmx4

### 2026-06-25/ncsc-ch-active-microsoft-365-voicemail-phishing-wave-in-swit
- Record: improvement, at 2026-10-21T08:22:37Z, fields [body, techniques].
- W1-C clean. Legacy duties: rating A/2 present; added T1684.001 (imitated Microsoft notifications); takeaway split into **Exposure**, **Detection** (mail flow first, chain-phishing burst, the existing marked M365 audit inference), **Triage** (audio-file tell, check voice messages in the official app) and a takeaway adding NCSC's resale/resurfacing warning.
- Ground truth: https://www.bacs.admin.ch/en/26w25-en

### 2026-06-30/cve-2026-8037-progress-kemp-loadmaster-pre-auth-rce-via-unin
- Record: correction, at 2026-10-21T08:20:39Z, fields [affected_products, body, cves, sources, summary, title].
- Applied finding 1: cvss 9.8 to 9.6 (Progress as numbering authority, adjacent-network vector; eSentire's 9.6 is that score), 9.8 kept as ZDI's; vendor ranges GA 7.2.60.0 to 7.2.63.1 and LTSF 7.2.54.12 to 7.2.54.17 in cves[], body, Exposure and the 2026-07-02 section; watchTowr's "and older" kept only as watchTowr's wording; added Progress ECS Connections Manager, Progress Object Scale Connection Manager, Progress MOVEit WAF to affected_products. Ground truth: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-34260 (the Progress community bulletin is a JS shell no transport reads).
- Applied finding 2: CVE-2026-33691 restored as an OWASP Core Rule Set flaw, cited to Progress's own release notes (https://docs.progress.com/bundle/release-notes_loadmaster-7-2-63-2/page/Security-Updates.html), CVE score 6.8 medium beside THN's "high-severity" (https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-18352); the 2026-09-30 Correction section reworded so it no longer calls the CRS statement an error.
- Declined finding 3 (KEV description cited to the alert page): already fixed by 2026-10-11T1307Z-audit.
- Declined finding 4 ("more successful attacks"): already fixed by 2026-10-11T1307Z-audit.
- Finding 5 (detection inference): the 2026-10-11 audit had flagged it only in its own section; now marked inline as inference in the 2026-08-08 and 2026-07-02 sections, and the unsupported "repeated probing from related sources" clause is dropped.
- Declined finding 6 (sectors): profile's relevance framing, as above.
- Em dashes removed: title (1), 2026-07-02 section (2).
- Legacy duties: B/1 and [T1190, T1059] present; **Triage** line added to the main text from watchTowr's request shape (the 2026-08-08 section's inline Triage is not what the site lifts).

## State changes the main agent must apply

- `entities/registry.yaml`: run `python3 tools/sync_products.py`. It adds `product:progress-ecs-connections-manager`, `product:progress-moveit-waf`, `product:progress-object-scale-connection-manager` (first_seen 2026-06-30) for the Kemp entry; in the same pass it also adds `product:starlette` and moves `product:berriai-litellm` first_seen to 2026-06-09, both from other workers' entries.
- `state/cves_seen.json`: `last_seen` to 2026-10-21 for CVE-2026-8037 and CVE-2026-54420 (CVE records changed). If records on an entry bump every CVE it names, also CVE-2026-50751, CVE-2026-48611, CVE-2026-48612, CVE-2026-33691, CVE-2026-20896. The CVE-2026-33691 title says "(high)" and has an em dash; its CVE score is 6.8 medium.
- Incident: `python3 tools/sync_products.py --report` wrote the registry (08:24:17Z) although the flag reads as a report. I restored the file byte-for-byte to HEAD (`git show HEAD:…` into the file; no index or checkout change); `git diff entities/registry.yaml` is empty and `--check` confirms the drift is still pending for the main agent.

## Checks run

- `check_run.py --all`: no FAIL on my entries; only the expected "run_id does not resolve to a run record" WARN on each of the 10. The one FAIL (cve-sync CVE-2026-92438, ninja-forms entry) belongs to another worker.
- `check_run.py 2026-10-21T0800Z-audit --page-checks-since 2026-10-21` (`repair-2/page-checks.txt`): no quote-literal or citation-cve line on my entries; the single WARN is another worker's Pixel entry.
- No em dash in any line I added (headings and append-only record summaries excluded).

## Residuals noticed (not fixed)

- Kemp: Progress's release notes describe the CVE-2026-8037 fix as command injection "in the cipher set UI and API command", while ZDI and watchTowr place it in `/accessv2` `apiuser` handling (KEV: "multiple command endpoints"); the entry gives only the latter.
- Kemp: the 2026-08-08 section's inline Triage ("small, stable set of management sources") is uncited inference.
- Kemp: no cves[] record for CVE-2026-33691 although the body treats it as the bulletin's second CVE.
- Check Point: still `priority: critical` with an `immediate_action` on a June finding; Help Net Security source carries `role: primary`.
- G7 summary: "Geneva–Vaud corridor" has no source wording behind it (ZENDATA says delegations land at Geneva and stay on the Swiss side).
- FortiSandbox: title em dash remains until the entry next gets a record.
- Tool: `sync_products.py --report` writes `entities/registry.yaml`; its docstring presents it as read-only ("what resolved where").
