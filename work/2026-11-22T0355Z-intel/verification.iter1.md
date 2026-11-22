**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T04:47:25Z · ended_at=2026-11-22T05:05:18Z · duration_seconds=1073

## Verification report — 2026-11-22T0355Z-intel (iteration 1)

Scope: 1 new entry, 5 updated entries, run record; ledger claims.iter1.yaml, 107 of 107 claims answered (92 ok, 7 F4, 3 F3, 5 unreadable). Rows in verification.iter1.claims.yaml. The five unreadable rows cite the Basel-Landschaft FAQ page, which returns HTTP 403 on extract, url, WebFetch and the Wayback route this pass; an earlier run's verifier read it, and Polizeiticker (verbatim relay of the canton's communique) corroborates the headline facts.

### Claim-support and fact defects (F3 / F4)

**#1 F4, MONAI Label entry is stale against a public fixed release and CVE.**
Entry: entries/2026-11-22/monai-label-path-traversal-zero-day-found-by-cairn-ai-agents.md. Quotes: title "a flaw with no CVE id ... the project's fix is merged but not yet in a release"; actions[0] "because the project's fix is not yet in a release and the flaw is exploitable without credentials by default"; Exposure "the advisory names no affected version range and no released fixed version"; Defender takeaway "the project's three workarounds are the control until a release ships"; `cves: []`; tag `no-patch`; sourcing_note "The advisory carries no CVE id, no affected-version range and no released fixed version".
Evidence fetched this pass: https://github.com/Project-MONAI/MONAILabel/releases and the 0.8.6 tag page: "MONAI Label 0.8.6 / This is a security release. All MONAI Label server deployments should upgrade ... Path traversal in datastore upload endpoints (CVE-2026-133968, GHSA-qc22-rmgc-vg94, critical) ... Affects all versions up to and including 0.8.5. Fixed in #1915", release timestamp 2026-11-22T01:29:24Z, which is before the run started (03:55Z) and before the entry's discovered_at (04:42Z). https://cveawg.mitre.org/api/cve/CVE-2026-133968: published 2026-11-20T18:31:38Z, CVSS 3.1 9.8, "monailabel (aka MONAI Label) through 0.8.5 allows directory traversal, with resultant remote code execution, via the image parameter to the PUT /datastore/image endpoint, as exploited in the wild starting in September 2026", references the Register article, the GHSA and PR 1915. PR 1915 merged 2026-10-19. The GHSA page still says "next release" and carries no CVE, which is why the stale reading was easy, but the release page is public.
Fix: add the cves[] record (affected up to 0.8.5, fixed 0.8.6), rewrite title, summary, actions[0], Exposure, takeaway and sourcing_note around "upgrade to 0.8.6", drop `no-patch`, cite the release notes; priority notable still looks defensible.

**#2 F4, MONAI summary drops Amazon's hedge.** Summary: "and reused it against a second university network". Amazon: "The server that the proxy connected to was running the same vulnerable software, and we infer the actor had used the zero-day to compromise it". The body paragraph is neutral; the summary is not.

**#3 F3 (low confidence), MONAI Detection.** "parent-directory sequences, which the fix rejects with an error, so legitimate uploads do not need them". Advisory: the endpoint "reduces the image ID to its basename and rejects empty or dot-prefixed IDs with HTTP 400"; the datastore functions "reject any path outside the datastore". A "../x" value is neutralised; the error behaviour is not stated for it.

**#4 F4, nginx update contradicts the entry's own earlier section.** Update 2026-11-22: "the affected-products table now also names ... Intersight Virtual Appliance (1.1.9-0, December 2026)". Update 2026-11-21 of the same entry: "Cisco's interim advisory (version 1.0, 2026-11-20) lists ... the Intersight Virtual Appliance (1.1.9-0, December 2026)". Cisco's v1.1 table carries the facts (fetched), the revision line only says "Update affected products". Remove Intersight from the "now also names" list or correct the earlier section.

**#6 F3 (low confidence), Cisco ESA entry.** "Cisco's advisory of 2026-10-14 describes CVE-2026-76519, a relative path traversal in the Advanced Malware Protection feature" is cited to Cisco only; Cisco's page says "improper handling of email attachments" and "Arbitrary File Write". "Relative path traversal" is in BleepingComputer and the CISA KEV title.

**#7 F4 (low confidence), Cisco ESA Improvement section and record summary.** Uncited: "A gateway still below Content Scanner Tools 25.3.0.5525 is therefore open to anyone who runs the module"; record summary "for anyone who runs it against a gateway below Content Scanner Tools 25.3.0.5525". Metasploit PR 22028: "Targeting a Cisco Secure Email Gateway ... which has the AMP feature for File Reputation enabled for inbound mail"; Cisco lists File Reputation as the second condition. State both conditions.

**#8 F3 (low confidence), Basel Improvement section.** "The canton's update of the evening of 2026-11-18 ... says ... individual servers had been cut off from the internet". watson.ch: "seien einzelne Server vom Internet getrennt worden, hiess es am Mittwochmorgen": the cut-off belongs to the morning communique.

**#9 F4, Basel sourcing_note.** "The canton's first communiqué of 2026-11-18 could not be read on any transport". https://www.baselland.ch/politik-und-behorden/regierungsrat/medienmitteilungen/cyberangriff-auf-die-it-infrastruktur-der-kantonalen-verwaltung-basel-landschaft reads through extract this pass ("Seit Sonntag finden diverse Cyberangriffe auf die kantonale IT-Struktur statt ... Einzelne Server mussten vom Internet isoliert werden"); findings.S2.yaml records it as read. The record's fields name sourcing_note, so the false sentence was carried through an edit of that field.

**#10 F3 (low confidence), citation dates.** Veria Labs is labelled 2026-11-20 throughout the Ruby entry; the page's datePublished is 2026-11-19T03:45Z and dateModified 2026-11-21T03:52Z. Ubuntu (java4shell) is labelled 2026-11-20 against "Publication date 18 November 2026, Last updated 20 November 2026", Citrix 2026-11-19 against initial publication 2026-11-18; those two follow the last-updated convention used for living vendor pages, so advisory only.

### Strengthen primary source (F6)
**Basel:** cite the canton's own first-phase communique (URL in #9) as a primary next to the watson relay.

### Needs more research (F8)
**nginx actions[1]/Update:** "Ubuntu lists the fixes in USN-9159-1 for 16.04 LTS to 26.10" (low confidence): the USN table marks 20.04, 18.04 and 16.04 "Ubuntu Pro Fix available with Ubuntu Pro". Add the caveat.

### Surface contradiction (F9)
**Java4Shell:** Update 2026-11-19 says "as of 2026-11-18 Red Hat and Ubuntu had released no fix and Debian had fixed only its unstable branch, so hosts on those distributions had no stable vendor build yet"; the Improvement section lists Ubuntu and Debian fixes without reconciling. Ubuntu's CVE page dates USN-9155-1 to 9158-1 "18 November 2026"; Tenable's current text says Ubuntu released fixes on November 18 and "As of November 19, Red Hat has released fixed OpenJDK packages". Red Hat is missing from the new section.

### Missed angles (F10)
**Synology DSM and nginx2root:** Synology-SA-26:20 (Critical, CVE-2026-123007, DSM 7.4/7.3 fixed 7.4.1-90080-2 / 7.3.2-86009-6, 7.2/7.1/BeeStation/APM ongoing, mitigation disable HTTP/2) was composed and withdrawn as out of window while Cisco and Fortinet rows were added to the same high entry; the store already carries two Synology DSM entries. Consider an update record on the nginx2root entry. Query: "Synology-SA-26:21 CVE-2026-120382 DSM OAuth". Otherwise coverage looks complete: no KEV addition inside the window (catalog 2026.11.20 checked), no Java4Shell or nginx2root exploitation confirmation found by search.

### Editorial / less-is-more (F11, advisory)
Java4Shell Improvement record summary "The entry now states the distribution and further vendor status it lacked" (narration); Ruby Detection "as no source gives detection guidance" (composition rationale); Basel length against the two-sentence rule for a no-vector, no-actor incident (low confidence; the Swiss nexus justifies the entry).

### Action-item discipline (F18)
**MONAI actions (low confidence):** both restate the body's Defender takeaway and Detection lines; actions[0] bundles the advisory's three workarounds. Rebuild around "upgrade to 0.8.6" plus a separate compromise-check action.

### Checked and clean
Style (no em dash outside headings, no workflow vocabulary in reader text), ATT&CK ids for the MONAI entry (all active in the pin), classification blocks, record-to-section-to-fields agreement and `updated_at` mirrors for all five updated entries, quote-literal evidence for the new entry, KEV and registry claims in the run record, the Java4Shell, nginx and Ruby cited pages (CERT-EU, CERT.at, NCSC-NL, NCSC.ch 13198/13203/13205, Rapid7, Wiz, Xint, Calif, Talos, Tenable, Upwind, Equixly, Oracle, OpenJDK, Cisco, Fortinet, PAN, GitLab, Veria, watchTowr, EUVD, Ruby announcement and GHSA, CISA both alerts, Citrix, Mitel, Debian, Ubuntu).

### Verdict
NEEDS_FIXES (truth: 9, editorial: 5, advisory: 3)

### Findings summary (machine-readable)
See work/2026-11-22T0355Z-intel/verification.iter1.findings.yaml (17 records).
