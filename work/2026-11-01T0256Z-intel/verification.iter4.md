**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T04:53:09Z · ended_at=2026-11-01T05:08:57Z · duration_seconds=948

## Verification report — 2026-11-01T0256Z-intel (iteration 4)

Scope: all 148 ledger claims of claims.iter4.yaml (the 6 changed claims, every other claim of all six entries; coverage 148/148 per `tools/claim_ledger.py --coverage 4`). Verdict rows: 144 ok, 4 F4 (three rows are one finding), written to verification.iter4.claims.yaml. Pages read this iteration: run bodies (Dream, Unit 42, GTIG, MSRC, Cisco eMudhra and PHP, GitLab, Python post, tracker, Oracle alert revision 2, vd.ch, RTS, SRF, Hunt.io, GreyNoise html and text); fetched fresh with `extract` / `url` / `cisa-kev`: Palo Alto PSIRT page and JSON, Internet Archive copy of 2026-10-27, php.net archive (raw HTML), both GHSA pages, Karimi report, SecurityWeek, BleepingComputer (PHP and eMudhra), VulnCheck, Sansec, Cloudflare, Wordfence (both), Sophos, CrowdStrike, Red Hat, SANS ISC, watchTowr, Fortinet, Splunk, Tenable, Siemens, WatchGuard, Cisco PHP advisory, BACS, ENISA, CERT-EU, ReliaQuest, nau.ch (two), Publica, SRF, Blick, THN, Inside IT, Le Temps, Google, Mozilla, Go, OpenJDK (three pages), Oracle alert 1, ENISA EUVD, Python security-announce, GitLab Atom feed, Python Insider feed, live tracker (raw HTML), live GreyNoise page (raw), CISA KEV catalogue 2026.10.30, NCSC.ch hub. The Citrix page answers 403 on `extract` and WebFetch and was read through the `url` command's reader fallback.

### Iteration-3 deltas (checked first)
- php2shell-main Detection: "AWS, as relayed by Inside IT, advises an operator who cannot exclude a compromise to start the investigation at least from 2026-10-17, its earliest honeypot exploit attempt" matches Inside IT ("Wer eine Kompromittierung nicht ausschliessen kann, sollte laut AWS die Untersuchung mindestens ab dem 17. Oktober ansetzen"; the 17 October honeypot attempt is stated). Remediation correct.
- PAN-OS Exposure: the GlobalProtect clause now cites Dream and the 2026-10-30 advisory; the advisory FAQ says "GlobalProtect portal, gateway and Clientless VPN are not impacted." Remediation correct.
- PAN-OS Detection: "bulk LDAP enumeration and password-spray bursts against all users, launched from the firewall management server" matches Dream ("Enumerated every user and group ... Sprayed passwords against every user account", run from the management server). Remediation correct.
- PAN-OS actions: systemd/rc.local/outbound-SSH hunt dropped from action 2; the residual overlap with the Fragnesia action is finding #3 below.
- Vaud composition sentence removed; first sentence reads "The Swiss canton of Vaud says ..."; every figure, date and the three evidence quotes (with originals) match vd.ch and RTS; Le Temps and SRF only relay the release.
- php2shell-main techniques T1105 and T1552.001 (and T1552.005): GreyNoise's table shows curl downloads of linPEAS and gitleaks, gitleaks dir scans of /srv and /var/www/html, and 169.254.169.254 queries. Remediation correct.
- eMudhra frontmatter: three product keys and the Hospitality SPMS affected_products entry added; see finding #4 (the Hospitality key is in the registry but not in entities).
- PAN-OS section: the 0.02 percent statistic is gone; the section now carries only "customers who applied the available patches are not affected" and "not exposed to the internet by default", both in Unit 42.
- Run record entities_added lists the three product keys (registry diff confirms).

### Unsupported / hallucinated facts
#1 (low confidence) php-critical-release-pre-announced-cve-2026-109618-109619, Detection line, 2026-11-01 section and the record summary: "create a .ssh directory in the web server account's home" / "creation of /var/www/.ssh in the web server account's home". GreyNoise lists only `mkdir -p /var/www/.ssh` and `chmod 600 /var/www/.ssh/authorized_keys` (2026-10-29/30/31) and a `getent passwd www-data` lookup; it never says /var/www is the account's home. Say "a .ssh directory under /var/www" (three places) or drop "home".

#2 (low confidence) emudhra-intermediate-ca-keys-recoverable-trust-store-updates, cves[CVE-2026-115557].affected: "CPython before 3.16.0 per ENISA's record". The EUVD record fetched this iteration lists "3.15.0 <3.15.2", "3.14.0 <3.14.10", "3.13.0 <3.13.18", "3.12.0 <3.12.16", "0 <3.11.18" and "3.16.0a1 <3.16.0", so the field misstates the record and contradicts the entry's own fixed field. Use the per-branch ranges.

### Action-item discipline
#3 (low confidence) cve-2026-46300 actions[1] vs pan-os-panorama actions[1]: both tell the team to look for a PHP file nobody deployed in a web-reachable directory on a PHP2Shell-exposed host; the PAN-OS action also restates its Detection line and takeaway. Keep the PAN-OS action (key rotation is its own task) and trim the Fragnesia action, or fold the hunt into one of them.

### Editorial / less-is-more flags (advisory)
#4 (low confidence) emudhra entities omit product:oracle-hospitality-cruise-shipboard-property-management although affected_products lists "Oracle Hospitality Cruise Shipboard Property Management" and the registry now holds the key.

### Not findings (checked)
- Coverage looks complete: kev_window_diff and the live catalogue (2026.10.30) show no uncovered addition; NCSC.ch hub items of 2026-10-29/30 (Linux TCP RCE CVE-2026-98432, Drupal Commerce CVE-2026-118539, WatchGuard Fireware, TeamViewer, VSCode extension) are covered by entries of 2026-10-29 to 2026-10-31 or held in the run record's borderline-drop list; no in-window Swiss item found by two web searches beyond the Vaud entry.
- GreyNoise live figures are stable against the saved page (1,177 confirmed, 5 attacker IPs; last updated moved from 03:48 to 04:48 UTC).
- Hunt.io page date: raw HTML carries time datetime 2026-10-30 (the extract metadata date of 2026-10-28 is stale), so the 2026-10-30 citation date is right.
- Updated-entry contract (4c): updated_at equals `at` for the four `update` records; the Fragnesia `improvement` leaves updated_at untouched; every section has a record and vice versa; summaries match sections. Registry diff is consistent (CL-UNK-1280 attributed-to relation sourced to the PAN-OS entry; UNC7228 overlaps-with Storm-0940).
- No em dash in reader text, no workflow vocabulary, no IOCs; priorities and Admiralty blocks consistent with the sources.

### Verdict
NEEDS_FIXES (truth: 2, editorial: 1, advisory: 1)

### Findings summary (machine-readable)
See work/2026-11-01T0256Z-intel/verification.iter4.findings.yaml (4 records).
