**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T07:31:01Z · ended_at=2026-11-27T08:00:41Z · duration_seconds=1780

## Verification report — 2026-11-27T0355Z-intel (iteration 6)

Scope: post-fix pass after NEEDS_FIXES iteration 5. All 328 claims in `claims.iter6.yaml` carry a verdict row in `verification.iter6.claims.yaml` (328 ok, 0 F3/F4/F5/F13/F14, 0 unreadable); the 8 changed claims and the nine entries the deltas block names were re-read against freshly fetched pages, then every other claim of the 11 entries was walked cold.

### Prior-iteration deltas (each remediation checked against its source this pass)

| # | Finding | Result |
|---|---|---|
| 1 | ARTEX section lead "per-run numbering" | Fixed. Lead now reads "their intent numbering" (claim 90f18a6c7c); Wiz says one counter per installation, never reset by default, numbers climb across runs and targets; no new unsupported claim. |
| 2 | Fragnesia "first fixed build ... later than the PHP2Shell hotfix" | Fixed. Clause now cites both PAN-SA-2026-0015 (12.2.4-h3, 12.1.4-h15, 12.1.7-h15, 12.1.10-h6, 11.2.x ... 10.2.18-h15 "and all later versions") and the CVE-2026-109618 advisory (12.2.4-h1, 12.1.4-h13 ...); every train's bulletin build is later; advisory source dated 2026-10-29 matches the advisory JSON's last timeline entry (2026-10-29T23:54Z). |
| 3 | nginx CVE-2026-132779 range citations | Fixed. The two citations are labelled 2026-11-27 and the source record is "as read 2026-11-27"; security_advisories.html lists "Vulnerable: 1.21.4-1.31.9, Not vulnerable: 1.31.10+, 1.30.8+" with no dateline. |
| 4 | NFS2ROOT four versus eight fixed versions | Fixed and true. The CVE record at publication (cvelistV5 commit of 2026-11-19, datePublished 14:22:44Z) carries exactly 6.12.117, 6.18.61, 7.3.2 and 7.4-rc1, and stays at four through the 2026-11-22 revision; the 2026-11-23 revision (ENISA dateUpdated Nov 23, 8:01:56 AM) adds 5.10.275, 5.15.226, 6.1.193, 6.6.163. The run's saved raw copy of the kernel announcement (fu1/kernel_announce_raw.md) lists the same four "fixed in" lines. |
| 5 | Mitel Exposure reverse-proxy clause | Fixed. APEX cited after "protect it"; page says "Organizations that publish MiCollab through a reverse proxy, including a MiVoice Border Gateway web proxy, should not assume that the proxy protects the AWV component." |
| 6 | Puppet record summary self-reference | Fixed. Record summary now states the hunt signal (PUT to certificate-request path from a non-agent address, GET for the same name within seconds, PUT to the report path); matches Huntback's access-log sequence. |
| 7 | PAN-OS bulletin date | Fixed. Section says 2026-11-24 23:10 UTC is the timeline's initial-publication entry and the page header reads 2026-11-25 (JSON: timeline 2026-11-24T23:10Z, datePublic 2026-11-25T00:10Z). |
| 8-10 | Unresolved advisories | Judged by stated reason; left to the audit as the brief instructs, not re-raised. |

### What was checked against fetched pages this pass

New entries: NFS2ROOT (OpenSec, watchTowr, Red Hat page and Security Data API, Debian tracker, Ubuntu page, ENISA EUVD, cve.org record via cveawg and cvelistV5 history, the run's saved raw lore copies) and SoftwareOK (ASEC post, the three SoftwareOK pages). Updated entries: Fragnesia and PAN-OS (PAN-SA-2026-0015 page and JSON, CVE-2026-109618 advisory page and JSON, Dream, Unit 42, KEV catalogue 2026.11.25, php.net); Mitel (Mitel advisory, APEX page and HTTP Last-Modified, BSI CSAF revision 2, ENISA EUVD-2026-130382, CERT-FR, MISA-2026-0006, CISA alert); nginx (nginx.org advisories, CHANGES, CHANGES-1.30, F5 NGINX Plus release notes, Veeam KB4976, GitLab 19.6.2, CERT-EU, CERT.at, Rapid7, PoC repository, Wiz, Xint, Unit 42, NCSC-NL, NCSC.ch 13203, Synology, Fortinet, Palo Alto); Ruby (Ruby announcement, GHSA-34m4, NCSC.ch 13205, watchTowr, Veria page, raw HTML and RSS feed, GitHub org repository list, Durendal, four GitHub Enterprise Server release-note pages, GitLab 19.6.2, ENISA); Juniper (SecurityWeek, NCSC.ch 13244 by hand including the evidence quote the gate could not check, ENISA 112215 and 112212, BSI CSAF 4234, KEV, CISA alert); ARTEX (Wiz intent-ID and Harvester posts, Huntback console post, DIVD report, GTIG, Microsoft 10-21, Expel, Wiz 10-22, CrowdStrike, Recorded Future, Yonhap, BleepingComputer, CERT-EU, Check Point, Microsoft 11-25); Puppet (Huntback post, CISA alert, ENISA, Red Hat, Neodyme, OpenVox GHSA, Puppet PE notes, oss-security, Vox Pupuli); Zammad (the 209-page DIVD forensic report text, case page, blog, public statements, DIVD-2026-00015 case, NCSC-NL, Zammad community, advisory, releases, GHSAs, GitHub advisory API, DIVD CVE records, Horizon3).

Run record notes: counts and dispositions hold on disk (nine `updates[]` tails are `type: update`; new registry keys and the two candidate sources exist; KEV window diff reports no additions; the Xen Orchestra and Danfoss KEV items of 2026-11-25 are covered by existing entries). `check_run.py` re-run: 61 pass, 0 warn, 0 fail.

Missed angles: NCSC.ch hub posts of 2026-11-24 to 2026-11-26 (vCenter CVE-2026-123903, GeoServer, Juniper) and the KEV additions of 2026-11-25 are all in the store; no in-window gap I can source. Coverage looks complete.

### Citation and source notes (no finding)

- Kernel announcement and linux-nfs thread (lore.kernel.org) return an Anubis bot challenge on every transport for me; the content is confirmed independently on cve.org/ENISA/Red Hat/Debian and in OpenSec's and watchTowr's pages, and the run's saved raw reads match. Marked ok on that evidence.
- Veria GitHub-organisation clause: newest repositories are docker-py (fork, 2026-10-03) and Jolt-PoC; the blog RSS newest item is 2026-10-15; no Ruby2Shell release found.
- Not re-raised by design: Red Hat/Ubuntu last-modified citation labels (NFS2ROOT), Ruby `ruby -v` hint, Zammad public-statements label, oversize summaries, Zammad and Fragnesia main-analysis length, Puppet release-notes date.

### Editorial / less-is-more flags (advisory)

1. F11 (low confidence), NFS2ROOT `sourcing_note`: "whose HTML page sits behind a bot challenge and was read through its raw form" narrates the fetch path instead of provenance.
2. F11 (low confidence), Mitel 2026-11-26 section: "No source read names an exploiting actor, a victim or the number of systems hit." now sits above APEX's report of two compromised organisations; still true for actor and named victim, stale for the count.
3. F11 (low confidence), Puppet 2026-11-27 section: "about two hours earlier" for the scout; Huntback's timestamps give 2 h 35 min, its brief "two and a half hours", its body "two hours and fifteen minutes".

### Verdict

CLEAN

(truth=0 editorial=0 advisory=3; the three F11 items are optional.)

### Findings summary (machine-readable)

See `work/2026-11-27T0355Z-intel/verification.iter6.findings.yaml` (three F11 advisory records).
