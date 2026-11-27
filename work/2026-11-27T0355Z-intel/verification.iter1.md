**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T05:03:26Z · ended_at=2026-11-27T05:29:31Z · duration_seconds=1565

## Verification report — 2026-11-27T0355Z-intel (iteration 1)

Scope: 2 new entries, 8 updated entries (diff against HEAD read for each), the run record, and all 283 ledger claims (every claim has a row in `verification.iter1.claims.yaml`: 266 ok, 17 non-ok). Pages were fetched live this iteration (extract, url, pdf, ncsc-csh, cisa-kev, WebFetch for the two cisa.gov alerts); the FU files were used only as a pointer.

### Citation does not support the claim (F3)

- #1 `ruby-4-0-10-...`: "NCSC.ch and watchTowr say Rails and classic-style Sinatra are exposed to the case-conversion overflow in their default configuration". watchTowr's FAQ says only "Organizations often run Ruby applications, including those built on the Rails or Sinatra frameworks" and "As of November 19, 2026, no exploitation in the wild has been reported." The default-exposure statement is NCSC.ch post 13205 ("Rails and classic-style Sinatra are exposed by default") and Veria's page. The sourcing_note repeats it ("for Rails and Sinatra, NCSC.ch and watchTowr"). Fix: attribute to NCSC.ch and Veria, keep watchTowr for no exploitation only.
- #2 `mitel-micollab-...`: "BSI rates it high" ([BSI, 2026-11-17]). BSI's CSAF WID-SEC-W-2026-4608 now has aggregate_severity "kritisch" and revision 2 (2026-11-25): "Aktive ausnutzung gemeldet, Bewertung angepasst, CVE's ergänzt". The entry's sourcing_note and update section never mention that BSI also reports exploitation, and the stale rating survives an update that is about exploitation (supersession).
- #3 `nginx-nginx2root-...`: "nginx 1.31.10 and 1.30.8 of 2026-11-23 ... (CVE-2026-132779, affecting 1.21.4 to 1.31.9)" cited to nginx.org/en/CHANGES and docs.nginx.com; the section repeats "1.31.10 and 1.30.8, both dated 2026-11-23" on CHANGES. nginx.org/en/CHANGES lists only 1.31.10 (23 Nov 2026); 1.30.8 is on CHANGES-1.30, and "Vulnerable: 1.21.4-1.31.9" is on security_advisories.html.
- #4 `ruby-4-0-10-...`: "GitHub Enterprise Server 3.22.6, 3.21.11, 3.20.13 and 3.19.17 carry the Ruby fix ... all dated 2026-11-22" cited to the enterprise-server@3.22 release notes, which carry only 3.22.6. The other three are on the @3.21, @3.20 and @3.19 pages (read this iteration, same CRITICAL Ruby line), not cited.
- #5 (low confidence) Mitel entry, five citations and sources[]: "[Accenture APEX Labs, 2026-11-26]". The page's dateline is "Published November 2026" only; the response header is Last-Modified Tue, 24 Nov 2026 18:22:52 GMT.
- #6 (low confidence) `artex-...` Triage: "a Python user agent on an application that normally calls Microsoft Graph with a .NET SDK is the anomaly". Expel: "Huntress found the ConnectWise Cloud Management and Partner Center apps it reviewed call Graph with kiota-dotnet, so a Python user agent on one of those apps is the anomaly." Generalised beyond the two named apps.

### Unsupported / hallucinated facts (F4)

- #7 `softwareok-...` title, headline, actions[0], Defender takeaway: "reinstalling does not remove it" / "because ASEC says reinstalling does not remove the remote-access tool". ASEC: "simply uninstalling and reinstalling the program may not remove a Python RAT that has already been installed." The entry's own evidence quote keeps "may not". Restore the hedge, and do not attribute the categorical form to ASEC.
- #8 `zammad-...` section: "the CISO was informed and the crisis team formed at 15:06, 19 h 23 min after the alert". DIVD report timeline: "2026-09-22T15:06:00Z DIVD CISO informed of a possible attack"; the text says only "the DIVD CISO was informed, and a crisis team was set up", no time. (The 7 h 21 min, 19 h 23 min and 27 h 41 min intervals themselves check out against 19:43:09, 03:04:00, 15:06:00 and 23:24:00 UTC.)
- #9 (low confidence) `juniper-...` section: "updated its bulletin JSA112183 on 2026-11-24, before BSI's revision and CISA's listing". SecurityWeek: "On Tuesday, Juniper updated its advisory"; BSI's revision is 2026-11-24T23:00Z, the same Tuesday. No source gives Juniper's time.
- #10 (low confidence) `cve-2026-115731-...` section: "the decoy signed the certificate, accepted the report and returned no marker, so it was not vulnerable" (Huntback reading). Huntback: "Our decoy signed the certificate, accepted the report with a 200, and returned no marker." It never says "not vulnerable".

### Quantifier without source (F14)

- #11 `pan-os-...` section: "one to three hotfixes after the PHP2Shell build". PHP2Shell advisory builds (12.2.4-h1, 12.1.4-h13, 12.1.7-h11, 12.1.10-h3, 11.2.4-h23, ...) against PAN-SA-2026-0015 (12.2.4-h3, 12.1.4-h15, 12.1.7-h15, 12.1.10-h6, 11.2.4-h25, ...): two later for most trains, three for 12.1.10 and 10.2.10, four for 12.1.7 (h11 to h15), one for none. The 20-build list itself matches the bulletin build for build.

### Analytical-link-as-fact (F13), with F9

- #12 `zammad-...` section: "DIVD's 19 hours is therefore the time to the formal response, not to the first look". DIVD case page: "it took us 19 hours to initiate our first response on 22 September 2026"; report: "The first response to these alerts was observed on Sep 22nd 2026 at 03:04 UTC." DIVD's two statements conflict and the entry picks a reading with "therefore". Quote both and add a `Contradiction:` line.

### Claims missing inline citation (F5)

- #13 (low confidence) `zammad-...`: "DIVD published the forensic report ... on 2026-11-25"; the cited PDF is dated 2026-11-24 (v1.5). The 25 November date is the dateline of https://csirt.divd.nl/2026/11/25/full-disclosure-our-hack/, which is not cited.
- #14 (low confidence) `pan-os-...` cves[CVE-2026-46300].status includes `cisa-kev`. True (catalogue 2026.11.25, dateAdded 2026-10-28) but no source on the entry carries it (the KEV sources are 2026.10.26 and 2026.10.27).

### Needs more research (F8)

- #15 (low confidence) `juniper-...`: actions[0] and Exposure cover the Conductor only; CISA's record, NCSC.ch ("Session Smart Router" in affected products) and SecurityWeek ("patched in Session Smart Router and Session Smart Conductor versions 7.2.3, 7.1.7, and 7.0.5") name the Router.
- #16 (low confidence) `nginx-...`: Veeam KB4976 also lists the Plug-In for AWS, Google Cloud and Microsoft Azure appliances and Veeam Backup for Salesforce 3.2.1 as affected; the entry names only the two 13.1 appliances.

### Action-item discipline (F18)

- #17 (low confidence) nginx actions[1] bundles nginx, Veeam, Ubuntu-advisory and HTTP/2 clauses and its PAN-OS counterpart in actions[0] duplicates the PAN-OS entry's hotfix task; Mitel actions[0] restates the body's Detection and Defender takeaway; Zammad actions[0] carries informational clauses. Keep one start-now task per action.

### Editorial / less-is-more flags (advisory, F11)

- #18 `pan-os-...`: "which the entry had from Dream's account alone" and sourcing_note "which is why a severity filter drops it" are pipeline self-reference.
- #19 `softwareok-...`: install path and scheduled-task name in prose and in the action are host indicators; the behaviour is already in Detection.
- #20 `zammad-...`: main analysis is 1,030 words against the 550 limit (run record acknowledges the debt) while five other entries were trimmed to 538 to 549 words, cutting detail such as nginx's network-flow hint and the PAN-OS Threat Prevention coverage.
- #21 `mitel-...`: headline states pre-disclosure exploitation as fact (one vendor, one victim); techniques[] omits T1068, T1041, T1105, T1087.002, T1552.001, T1572 that APEX's table maps.
- #22 `cve-2026-99362-...`: event_date 2026-11-25 (OpenSec) against a primary dated 2026-11-19.
- #23 (low confidence) `cve-2026-115731-...`: a post-publication decoy capture of the exploit chain is typed `improvement`; arguably an `update`.

### Checks that came out clean (no finding)

NFS2ROOT: fixed branch strings (4 in the announcement, 8 in EUVD updated 2026-11-23), Debian (trixie and bookworm linux-6.12 fixed, bookworm 6.1 vulnerable), Red Hat API (RHEL 8 RHSA-2026:103817 on 2026-11-26, RHEL 9 and 10 Affected), Ubuntu (every release 16.04 to 26.10 Vulnerable, updated 25 Nov), the three evidence quotes (verbatim) and the linux-nfs 2026-08-17 thread. SoftwareOK: all versions and release dates, 1,206 names, hedges on the update path and absence of vendor notice (download page has a SHA256 table and no notice). Mitel update: every APEX offset (T+1, 9, 12, 15 to 30, 32 minutes; 20 to 23 hours), the 23:00 UTC bound and its UTC-12 to UTC+1 gloss, second victim since 9 Nov, no claim beyond APEX's hedges. PAN-OS: bulletin timestamp 2026-11-24T23:10Z, zero CVSS block, exploitation sentence, FAQ quote and all 20 build strings. Ruby: Veria table (GHES 3.22.5 unfixed, updated 21 Nov), PoC date 25 Nov, no release on page, blog or GitHub org, GitLab five-branch backport, Sanft/OpenAI 2026-11-07. Zammad: every chain timestamp, persistence, credentials, 990/3,259 counts, 41 thousand ticket titles, 39 hours, 209 pages. ARTEX: Wiz, Huntback, GTIG statements. Puppet: Huntback chain, 1.47 s, four other products, KEV 17 Nov. Classification letters match sources.json tiers; every changelog record's `fields` covers its diff; `updated_at` equals the update `at` on all seven update records.

Coverage: the 2026-11-25 KEV Vates Xen Orchestra addition (CVE-2026-133469) is already covered by entries/2026-11-11/vates-xen-orchestra-vsa-2026-062-auth-bypass-exploited.md; the Danfoss and Mitel additions were handled by the previous fire. I can name no in-window omission with a source; coverage looks complete for the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 12, editorial: 5, advisory: 6)

### Findings summary (machine-readable)

See `work/2026-11-27T0355Z-intel/verification.iter1.findings.yaml` (23 records).
