# Prior-iteration (1) findings and the remediation applied — verify each in iteration 2

| # | code | entry | remediation_applied |
|---|---|---|---|
| 1 | F3 | php-critical-release… | VulnCheck sentence now carries the page's 7 PM ET October 22 wording (one PoC bypassed ASLR on x86-64 for PHP 8.4.26 with default heap configuration; did not work outside that setup; exploit supports 8.4.10–8.4.26) |
| 2 | F3 | emudhra-intermediate-ca… | Apple block date changed to 2026-10-22 |
| 3 | F3 | emudhra-intermediate-ca… | Exposure sentence replaced with the tracker's current state (Node.js, Bun, FreeBSD fixed; pending list as the tracker shows); Java content from the earlier update kept |
| 4 | F3 | fortinet-hardening-release… | "published 2026-10-22" → "scheduled for 2026-10-22, after recent FortiMail and FortiAuthenticator releases" (the post's own wording) |
| 5 | F3 | publica-pk-softech… 2026-10-23 section | the 2019-migration / January detail moved to the Inside IT clause (dated "January 2026" there); Tages-Anzeiger clause now states only what its readable lede says |
| 6 | F4 | pan-os-panorama-php2shell… | advisory re-fetched (work/…/bodies/v1-pan.txt); hotfix ETAs per train added; only Panorama and WF-500/WF-500-B remain undated; record amended |
| 7 | F4 | php-critical-release… | Palo Alto statement updated to the same current state |
| 8 | F4 | php-critical-release… evidence[] | watchTowr and VulnCheck quotes re-pointed to current page wording |
| 9 | F4 | fortinet-hardening-release… | references[] now carries the FortiMail zero-day entry; a paragraph cites FG-IR-26-175 (now in sources[]) and says the FortiMail builds already fix CVE-2026-104286, reported exploited; "unknown exploitation" framing limited to the other products |
| 10 | F6 | publica-pk-softech… | Frontaliere Ticino replaced by TicinoNews (originating article) in sources[], body and evidence |
| 11 | F7 | cve-2026-102785-yootheme… | entry dropped: file removed, cves_seen record removed, counters decremented, borderline-drop line in the run record |
| 12 | F7 | cve-2026-76466-cisco-expressway… | update reverted (`git checkout`), record dropped from entries_updated/updated_entry_ids; PHP2Shell on Expressway stays one clause on the PHP entry; the NetScaler entry's reference to the Cisco entry removed |
| 13 | F9 | publica-pk-softech… | summary and main-analysis sentences reworded and dated ("at that date", "as of 2026-10-21", "no first-hand statement … available to cite"); record summary amended |
| 14 | F9 | hpesbnw05162… | body states both the bulletin text ranges and the wider CSAF ranges; cves[].affected carry the CSAF ranges |
| 15 | F10 | coverage | NEW entry fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes (FG-IR-26-185 / FG-IR-26-180), read in full by the main agent (work/…/bodies/v2-fg185.*, v2-fg180.*); needs a complete first-pass read |
| 16 | F18 | php-critical-release… | actions[1] removed |
| 17 | F11 | m365, php, publica | process wording removed from sourcing_notes, the PHP update section (last sentence deleted) and the PK section |
| 18 | F11 | mythicratatoskr… | literal service name removed from prose and evidence |
| 19 | F11 | blackx… | CVE-2023-24932 named with Kaspersky's attribution; Kaspersky's caveat on the driver's tampering routines added; three clauses shortened to stay within 550 words |
| 20 | F11 | netscaler, m365, fortinet-hardening | "is hit by" → "is affected by"; "12 minutes … four minutes"; "change windows … that Fortinet suggested" |
