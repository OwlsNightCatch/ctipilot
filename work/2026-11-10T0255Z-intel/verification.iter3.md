**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-10T04:54:45Z · ended_at=2026-11-10T05:12:40Z · duration_seconds=1075

## Verification report — 2026-11-10T0255Z-intel (iteration 3)

Scope walked: all four new entries and all seven updated entries read end to end, `git diff HEAD` read for every updated entry, run record read. Claim ledger: every claim of the six entries remediated this round (OpenSSH, N-able, Ahsay, SAP, SonicWall, FreeSWITCH), every claim of IBM Aspera Faspex, BluePhishing and Barracuda, and, for Danfoss and PK Softech, every claim of the new section and the changed frontmatter plus the older claims I re-fetched (NCSC advisory 13054, EFS, Public Sénat, summary). 220 verdict rows in `verification.iter3.claims.yaml` (213 ok, 5 F3, 1 F14, 1 unreadable); all 20 claims of `claims.changed.iter3.yaml` have rows.

### Prior-iteration deltas (each remediation checked against the cited page)

- OpenSSH, BleepingComputer 2026-11-09 article added with its quote: present verbatim ("the first successful exploitation of SSHole in the wild on November 7 at 00:46 UTC"). Fixed-package table: matches Alpine's advisory row for row. Alpine's stricter cloud-image condition ("safe on first boot ... exploitable as soon as any $6$ hash exists"): correct. Detection "if a login cannot be ruled out": matches Alpine. Previdian counter (22 attempts, 14 addresses, last observed Nov 10): matches the page. NCSC sentence (last edited 2026-11-06, exploitation UNKNOWN): matches the post's lastModified and status. Actor-class sentence: BleepingComputer carries watchTowr's botnet and cryptomining observation and GreyNoise's "not representative". Remediation introduced two small defects (the "rebuild" clause cited to Alpine, the "3.1" cited to GreyNoise), listed below.
- N-able second Detection clause: Field Effect carries deployments, scripts, remote-control sessions and policy changes; Huntress carries the spraying observation; the process-creation clause is marked an inference. Correct.
- Ahsay: the Linux-copies inference is Huntress's own reading ("simply tried every likely location") and is limited to those paths; the "CBS JVM on Linux" parent is in Horizon3's indicator list; the NSSM pivot is in Huntress's first post (msedge.exe is a modified NSSM). Correct.
- SAP: "ENISA shows an EPSS value of 0.0 for each" matches all four EUVD records ("epss": 0.0). Version grouping in `cves[].affected` matches the CVE.org record order. Correct.
- SonicWall: BleepingComputer 2026-11-06 says SonicWall "says no workarounds are available"; the PSIRT page now shows Workaround true, Last Updated 2026-11-09, and the workaround text matches the evidence quote. Correct.
- FreeSWITCH actions[0]: grammatical and accurate; CISA's alert and the KEV catalogue both list CVE-2026-116779 (dateAdded 2026-11-09); the GitHub advisory sidebar confirms CVSS 9.8 (CVSS:3.1 vector), affected <= 1.11.2, patched >= 1.11.3.
- Declined items re-checked, not re-litigated: SAP patch-day relevance, GPUStack drop, raw EUVD links. The two declined truth items are addressed below because this pass found new evidence on each.

### Citation does not support the claim

#1 (F3) 2026-11-06/cve-2026-123158 Defender takeaway, "and rebuild container and cloud images from a fixed base ([Alpine Linux, 2026-11-05](...))". Alpine's advisory does not say this: it says update openssh and restart sshd, and that images built from 3.21.10, 3.22.8, 3.23.8 and 3.24.4 and later carry the fix while "Images from earlier point releases do not, so on every running instance, update openssh or disable password authentication". The rebuild advice is OX Security's ("Rebuild your images ... Rebuild them from a fixed base and redeploy"), and the OX page reads through `extract` (jina fallback). Cite OX for that clause or reword it to Alpine's image statement.

#2 (F3, low confidence) same entry, "NVD scores the flaw CVSS 3.1 8.1 ([GreyNoise, 2026-11-10](...))". GreyNoise's timeline says "Published to NVD CVE-2026-123158, CVSS 8.1." without a version; "CVSS v3.1 8.1 High" is on the OX page. Cite OX with GreyNoise or drop "3.1" (title, summary and sourcing_note repeat it).

#3 (F3, low confidence) 2026-11-10/n-able, "No source has validated the individual claims, but N-able took its hosted environments offline ... ([Huntress]; [BleepingComputer])". The first clause is Censys's statement ("no source has validated the proof-of-concept code") and Censys is not cited there; BleepingComputer adds that N-able's hotfix lends "credence to the researcher's claims that at least some of the flaws are legitimate zero-days". Add Censys and the BleepingComputer qualifier.

#4 (F3, low confidence) 2026-11-10/n-able Exposure, "so a compromised server gives a path to every device it manages ([Field Effect])". Field Effect: "a compromised N-central server can give attackers a path to downstream systems" and access "across large numbers of systems". The hedge is dropped and "every device it manages" is Censys's wording.

#5 (F3, low confidence, unreadable) 2026-11-07/sonicwall cves[CVE-2026-19868].affected, "NSv 270, 470, 870 ... NSv XS, S, M, L". The PSIRT build table is script-built; extract, jina and WebFetch all return the advisory text without it. SecurityWeek confirms the families and builds (Gen7 TZ, NSa, NSsp and NSv up to 7.3.3-7015; Gen8 TZ, NSa and NSv up to 8.2.2-8015; fixes 7.3.4-7013 and 8.2.3-8015) but gives no NSv model numbers. Suggest "Gen7 and Gen8 NSv" in the record, or log it as a residual. (The Canadian Cyber Centre alert AV26-1133 reads the Gen8 boundary as "prior to 8.2.2-8015", which differs from PSIRT, BleepingComputer and SecurityWeek; the entry does not cite it, so this is context, not an F9.)

#6 (F3, low confidence, one-day drift) 2026-11-06/freeswitch, "BSI CERT-Bund relayed it as a critical advisory on 2026-11-05" and the BSI citation date. Read through jina, the portal shows "SignalWire FreeSWITCH <1.11.3" and a date line "04.11.2026"; BSI's advisory listing gives classification "kritisch" and published 2026-11-06T10:29:56Z (status UPDATE). The rating, the CVE and "before 1.11.3" are confirmed; no readable surface shows 2026-11-05.

### Quantifier without source

#7 (F14, low confidence) 2026-11-06/openssh Update section, "Every success described so far is on a GreyNoise gridpoint or a honeypot, and no source reports a compromised production host." BleepingComputer: watchTowr "observed SSHole being exploited in attacks associated with botnets and cryptomining activity" and Previdian sensors "confirmed successful SSHole exploitation"; SecurityWeek: "only botnets and crypto miners have picked it up so far". None says whose hosts, and the entry's own body cites watchTowr's botnet and cryptomining use. Scope the quantifier or keep only the absence claim.

### Editorial / less-is-more flags (advisory)

#8 (F11) 2026-11-06/openssh sourcing_note, "OX Security's analysis gives the mechanism and could not be re-read on 2026-11-10". Fetch-failure narration in a reader-facing field, and no longer true: OX reads (dateline 2026-11-05, mechanism, "CVSS v3.1 8.1 High", rebuild advice, doas on the cloud images). Two sentences of provenance are enough.

### Checks that came back clean

- Updated-entry contract (4c) for all seven: each last `updates[]` record carries run_id 2026-11-10T0255Z-intel, non-internal `update` records have a matching `## Update` section with the same `at`, `updated_at` equals that `at`, diffs show no change outside the named `fields`, record summaries state what the sections state, no superseded statement survives (Barracuda "no source reports attacks", SonicWall "no workaround", FreeSWITCH "the vendor's alone" were all replaced; the SonicWall Detection and takeaway carry the workaround consequence).
- New entries: IBM Aspera Faspex (bulletin 2026-11-07, CVSS 9.8, 5.0.19 PL1, Workarounds None, KEV 2026-11-09, description "authorized" vs "authenticated" disclosed), SAP (four EUVD records, notes, versions, EPSS 0.0, 10.0 vectors), BluePhishing (Proofpoint JSON-LD datePublished and visible dateline 2026-11-09; every attributed statement found on the page; the Microsoft-documentation attribution is correct) and N-able (Huntress, BleepingComputer, Field Effect, Censys all agree with the body apart from #3 and #4).
- Danfoss new section: foreign-ministry attribution text, CERT-FR "faisceau d'indices", FOFA (footnote 2 defines "mode opératoire d'attaque"), CyberbanNews from 13 October, Farsi traces, Schneider Electric hydro installations, Modbus 502, Sekoia honeypot numbers, Reuters via NBC on the arrest-warrant request: all found. The summary's "French documents cover that campaign only" holds.
- PK Softech Zug section: Inside IT 2026-11-09 carries every statement (outsourced to Libera, mid-October notice, "erhöhtes Risiko", data fields, informed insured and the EDÖB, assets safe).
- Barracuda: Barracuda's Nov 9 9:00pm EST update, Canadian Cyber Centre Update 1, Mandiant 0041/0042, Campus 9.4.0.029, NCSC 13144 (still UNKNOWN, last edited 2026-11-06) all match.
- Ahsay: Huntress first post, Huntress follow-up 2026-11-09, Horizon3, Ahsay announcement, SecurityWeek, BleepingComputer, release notes all match.
- Style (check 12): no em dash outside headings, no IOCs, no workflow vocabulary in entry text, English throughout. Classification blocks present and within vocabulary on every entry; no org_triage, no watchlist.
- Run record notes: counts (four new, seven records, ledger sizes 19/26/14/10, dispositions of the four KEV rows) hold against the entries and `kev-window.txt`.

### Missed angles

None evidenced. The 2026-11-05 Zyxel GS1900 zero-day (CVE-2026-107441) and the Cisco/WatchGuard advisories I looked at are outside the 26 h window; Patch Tuesday and SAP Patch Day publish after the run clock, as the record says. Considered and not raised: FreeSWITCH stays `notable` after the KEV listing; I found no Swiss-constituency exposure evidence either way, so I do not call it plainly `high`.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 0, advisory: 1). Six of the truth findings are marked low confidence; #1 is the one with a clear page-versus-claim gap. Everything else I walked held.
