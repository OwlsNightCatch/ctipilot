**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-02T05:02:06Z · ended_at=2026-11-02T05:19:05Z · duration_seconds=1019

## Verification report — 2026-11-02T0256Z-intel (iteration 4)

Scope: 4 new entries and 3 updated entries read whole (updated ones with `git diff HEAD`), the run record, the gate (`check_run.py --pre-verify` re-run: 57 pass, 1 expected warn, exit 0). Ledger: `verification.iter4.claims.yaml` carries 153 of 153 rows (`claim_ledger.py --coverage 4`: 0 missing), none unreadable: all 7 changed claims; every claim of Android, Dahua, NIK C2 and Berlin (the remediated entries, 78); and all the rest of Danfoss, QNAP/Synology and Xerox too (68 further rows, well past the random quarter: every Danfoss and QNAP section/summary/record claim plus a seeded sample, then the remainder). Pages read this iteration: gate-saved bodies under `quote-bodies/` and `deep/`, plus live `extract`/`url`/`pdf`/`ncsc-csh post`/`cisa-kev` fetches (BSI PDF re-extracted, Microsoft TerminalFix blog, heise 11444072, BSI's Mastodon post through its status API, Synology SA-26:14, QSA-26-18 and the QNAP statement, the MITRE CVE API and NVD for CVE-2026-58882, Xerox v5/v6 URLs, an AFP wire copy on Khaleej Times). CERT-UA's alert through the saved reader text (`deep/cert-ua.txt`; the in-container transports return only the SPA shell). afp.com itself answered "Under maintenance" on `extract`, `url` and `jina`; its claims are checked against the AFP wire copy (Khaleej Times) and marked ok on that page.

### Prior-iteration deltas, walked first
1. **Android PoC and source public.** smsofdeath.com: "The proof-of-concept Android app and full source code are published on GitHub."; BleepingComputer: "has published a proof-of-concept exploit". The clause now cites both: correct. The sourcing_note no longer carries "so no CVE is recorded here"; its new sentence ("no CVE record by that number exists") holds: MITRE CVE API `CVE_RECORD_DNE`, NVD `totalResults: 0`, re-queried.
2. **Berlin Triage hedge.** "may stage" matches BSI's "ggf." ("where applicable"). The new qualifier "from reporting organizations" does not: see F3 #1 (also present, unhedged, in the 2026-09-08 section).
3. **Berlin sourcing_note.** "not on a BSI statement linking TerminalFix to Berlin" matches the body, rbb24 ("bestätigt das BSI dem rbb nicht") and BSI's advisory ("Netzwerks einer staatlichen Institution"). BSI's Mastodon post (created 2026-09-04T12:18:41Z) says BSI is "intensiv in die Vorfallbearbeitung im Land Berlin eingebunden" and links the TerminalFix notice; it does not itself name TerminalFix as Berlin's vector, so the hedged "heise reads ... as confirming" is right.
4. **NIK C2.** The first paragraph's last sentence now cites Talos: "spans at least three distinct versions"; "assess with moderate confidence that NIK C2 is not merely a proof of concept, but a fully functional ... framework". T1539 (cookies), T1518.001 (`wmic ... AntiVirusProduct`), T1082 (`systeminfo`), T1057 (`Get-Process`) are all in Talos and active ids in the v20 pin.
5. **Dahua.** CERT-UA's text (reader) matches every clause cited to it: Easy4IP as main vector, outbound connection and registration by serial number, bypass of NAT and firewall, weak passwords or the bypass flaws (зокрема CVE-2021-33044, CVE-2021-33045), the DVRIP 127.0.0.1 sign, the four steps. eSecurity Planet carries "although their use in the October incidents remains unconfirmed", now attributed to it in the summary. `single-source-national-cert` and A/2 follow the 2026-07-20 CERT-UA entry; the quotes left are on pages the gate could read. Remaining defects: F4 #4, F5 #5, advisory items.
6. **Danfoss update-vs-new.** Declined by the main agent; noted once more as advisory only (F11 #10).

### Claim does not support the clause (F3)
- #1 berlin Triage line (changed claim 9563f3e443) and Update 2026-09-08: "BSI's advisory adds, from reporting organizations, that TerminalFix operators may stage exfiltration into attacker-controlled cloud storage, for example Azure, with the provider's own transfer tool" and "reporting organizations told BSI that TerminalFix operators have staged exfiltration ... azcopy". BSI's PDF: the step "Der Angreifer richtet ggf. direkt Online-Speicher z. B. in der Azure-Cloud ... azcopy im Falle von Azure" is one of eight steps of the sequence introduced by "Der Ablauf dieser Attacken stellt sich basierend auf dem Microsoft Blog sowie dem BSI bekannten Erkenntnissen wie folgt dar"; "Beim BSI eingegangene Meldungen" belongs to the later, separate sentence on ransomware and double extortion. Microsoft's blog does not mention Azure or azcopy, so "adds a detail" is fine; the attribution to reporting organizations is not in the source, and the 2026-09-08 section also drops "ggf.". Fix both places.
- #2 berlin Update 2026-09-08 (low confidence): "BSI posted on its official Mastodon account that it was intensively involved in handling the Berlin incident" is cited only to heise 11444072, which never says it. The fact is true (status API above); cite the post.
- #3 android first paragraph (low confidence): "drops active calls, emergency calls included, for one to two seconds per message": the page ends calls ("terminate with `CS_DEATH`") and separately gives "1-2 seconds of no service per message".

### Unsupported / hallucinated facts (F4)
- #4 run record notes: "CERT-UA's alert page is script-rendered and unread" and "Coverage gaps: ... CERT-UA's alert page (script-rendered, read through quoting press)" contradict the Dahua entry (CERT-UA primary, "its page was read") and `deep/cert-ua.txt`. The run record is stale on this disposition.

### Claims missing inline citation (F5)
- #5 dahua Defender takeaway (low confidence): "check the devices CERT-UA calls forgotten, and do not treat a clean password as protection ..." follows the closing parenthesis and has no citation of its own; the "forgotten" wording is Security Affairs', absent from the CERT-UA text read.

### Editorial / less-is-more flags (advisory, F11)
- #6 dahua sourcing_note "read directly" (the page renders only through the reader fallback; its metadata reads "Published Time: 24 Sep 2026", an artifact against the 2026-10-23 dating by Security Affairs, The Record and "last week" in The Hacker News).
- #7 dahua "The Hacker News links the alert to Hunt.io's earlier Operation CameraSwarm": the article says "share similarities".
- #8 berlin updates[] record summary carries "credibility to 2" and "the entry's priority moves to notable" (record-keeping, Admiralty digit).
- #9 registry notes (lines 5571, 5575, 5974) still say BSI confirms TerminalFix as the Berlin vector.
- #10 danfoss: "No actor is named on the record; none confirms ..." lost its antecedent; update-vs-new noted again, not blocking.
- #11 dahua verification `single-source-national-cert`: CERT-UA is not on the profile's carve-out list; defensible (gate host list, precedent entry).

### Whole-run checks
- Update contract (4c): QNAP/Synology, Berlin and Danfoss each carry one record with this run's id, `updated_at` equal to the record `at`, a matching `## Update` section, genuine delta, every changed frontmatter line covered by `fields`; `discovered_at`, `run_id` and path untouched. Synology-SA-26:14 read live: revisions 3 (2026-10-29) and 4 (2026-10-31) and every fixed build match section, summary and `cves[].fixed` (no PHP 8.0 build for DSM 6.2). Reuters (via Internazionale) and Nextgov match every Danfoss clause (four officials, at least six commissaries, Fort Huachuca quote, Cyber Command and Army CID, two people, late August, "not clear how exactly"). rbb24 (2026-10-21) matches every Berlin section clause (5 percent licences, entry endpoint and servers uncovered, 2024 funds, ID-card copies, BSI warnings since March 2025, ITDZ/Senatskanzlei).
- Supersession: Berlin priority, confidence, classification and sourcing_note agree with the new section; Danfoss "no actor is named on the record" holds for the French incident. Berlin's 2026-09-08 section still says "have staged" (F3 #1).
- Dedup: no recycled material; CVE-2021-33044/45 and CVE-2026-58882 (does not exist) are new to the store; Xerox declares the PHP2Shell vendor entries in `references[]`; no name collision for SMS of Death, NIK C2 or the Dahua campaign.
- Evidence quotes: Android (3), Dahua (5, all on press pages), NIK (3), Xerox (2), Berlin (new 3) and Danfoss (new 3) are verbatim on the fetched pages; the gate's `quote-literal` passed on 19.
- Relevance, priority, classification (A/2 Xerox, B/2 Android and NIK C2 and Berlin, A/2 Dahua), single-source flags, actions: hold. No org-triage or watchlist residue, no IOCs, no em dashes or workflow vocabulary in entry text.
- Missed angles (F10): none found; KEV is unchanged (catalog 2026.10.30); WebSearch for exploited flaws on 2 November and Swiss municipal or cantonal incidents returned nothing dated in the window.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 6)

The one finding that must change is #1 (the remediation of iteration 3's Triage hedge introduced "from reporting organizations", which the BSI PDF does not support); #4 is a stale run-record statement; the rest are low confidence and small.

### Findings summary (machine-readable)
See `work/2026-11-02T0256Z-intel/verification.iter4.findings.yaml` (11 records: F3 x3, F4 x1, F5 x1, F11 x6).
