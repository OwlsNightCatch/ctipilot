**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T03:38:10Z · ended_at=2026-11-01T03:56:31Z · duration_seconds=1101

## Verification report — 2026-11-01T0256Z-intel (iteration 1)

Scope: all 140 ledger claims (claims.iter1.yaml, iteration 1 and first pass, so every claim); coverage 140/140 per `tools/claim_ledger.py --coverage 1`. Cited pages were fetched this iteration (cached run bodies for Dream, Unit 42, GTIG, MSRC, Cisco, GitLab, vd.ch, RTS, SRF; everything else fetched with `extract`; CISA KEV through `cisa-kev`; CISA alert through WebFetch; php.net anchors read from the raw archive HTML; GitLab date from the Atom feed; NCSC.ch through `ncsc-csh post`). Non-`ok` claim rows: 12 (10 F3, 2 F4), all repeated below.

### Citation does not support the claim (F3)

1. **PAN-OS entry, body paragraph 2** (claim 0c0b801d1b). Entry: "On two firewalls of a US government-affiliated organization it added a reboot-persistent reverse SSH tunnel". Dream (https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers): the first firewall "crashed shortly after — likely from the ~900MB of exploit traffic — and never came back online"; the tunnel was built on the second ("An 8-port reverse SSH tunnel connected the compromised firewall back to the operator's infrastructure"). One firewall, not two. The PHP and CVE-2026-46300 entries already say "the second of two firewalls (the first crashed)".
2. **eMudhra entry, Exposure line and cves[CVE-2026-115557].fixed** (claim 9f60fa5abb). Entry: "the tracker lists fixed versions for Python (3.15.1, 3.14.9 and 3.13.17, and pip 26.2.2) ... and lists Bottlerocket, Godot, LibreOffice and RHEL 7 as still pending". The live tracker (https://emudhra.we-have-a-problem.com/, table rows parsed from the raw HTML) lists "Python 3.15.2, 3.14.10, 3.13.18, 3.12.16, 3.11.18", "RHEL ca-certificates ... 2026.2.92_v9.0.319-70.3.el7_9", and pending "Bottlerocket, OpenHarmony/HarmonyOS NEXT, certbot, containerd, Godot, LibreOffice". Python's release post (https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/, `<time>` 2026-10-26) lists CVE-2026-115557 "Distrust compromised eMudhra intermediate CA keys" under "Security content in all five releases". 3.15.1, 3.14.9 and 3.13.17 are not the denylist releases; RHEL 7 is no longer pending. The cves[] `fixed` string repeats the stale versions.
3. **PHP entry, body paragraph 2** (claim 23ffb19255). Entry: "with all but one of its hotfixes released and 11.1.7-h12 due on 2026-10-30". Palo Alto advisory (https://security.paloaltonetworks.com/CVE-2026-109618): "11.1.7 through 11.1.7-h* | Upgrade to 11.1.7-h12 or 11.1.16-h4 or later"; timeline 2026-10-29T23:54Z "Removed ETAs for 11.1.7-h12 as the version is released." All twenty are out, as the PAN-OS entry says.
4. **PHP entry, vendor list** (claim b95d43e914). Entry: "with fixes at 15.5.21, 27.1.1 (November 2026) and 3.2.0". Cisco v1.10 (2026-OCT-30): "26.2.1.9 (Nov 2026)" for Unified Industrial Wireless Software / URWB; ISE Portal Builder "Fix deployed, no customer action required". 27.1.1 no longer appears. The store's 2026-10-28/cisco-php2shell entry already records 26.2.1.9.
5. **ARTEX entry, summary and 2026-11-01T03:29:45Z record summary** (claims c76eff5732, 557e8f7a1e). Entry: "have seen ARTEX, PentAGI and CAIRN operated in incident-response cases by extortion groups and suspected PRC-nexus clusters". GTIG: "Since late August 2026, ARTEX has been adopted by a diverse range of threat actors ... including both financially motivated extortion groups and suspected cyber espionage operators" and "additional suspected PRC-nexus clusters". For PentAGI no actor type is given (Asian integrators and telecom; aerospace targeting), for CAIRN none. The ARTEX attribution is spread over three frameworks.
6. **Vaud entry, RTS sentence** (claim b9c33318f6). Entry: "with no context, motive or method known". RTS: "On ne connaît ni le contexte, ni les raisons, ni les objectifs de ce vol." Method is not said to be unknown (RTS quotes an expert speculating about an insider with undue privileges).
7. (low confidence) **eMudhra entry, actions[1] and Defender takeaway** (claims ccb03a5564, ffb752b310). Entry: Windows devices that do not receive automatic updates "need Microsoft's out-of-band update of 2026-10-26". MSRC: "make sure your update process delivers the updated Disallowed Certificate Trust List and the upcoming trust-list changes." The Disallowed CTL update of 2026-10-20 (the actual block of the compromised intermediates) is the part a disconnected device lacks, and it is not named.
8. (low confidence) **PHP entry, Dream chain clause** (claim 1db5576450). Cited "[Dream Research, 2026-10-27]" for "management web server of Palo Alto Networks PAN-OS (PHP 8.0.30)"; Dream's dateline is "Updated: October 29, 2026" and PAN-OS is named only in that update.

### Unsupported / hallucinated facts (F4)

9. (low confidence) **PAN-OS entry, Detection line** (claim 219e34759e). "an appliance crash or reboot after them": Dream reports one crashed firewall that "never came back online"; no reboot, no general crash signal.
10. (low confidence) **Vaud entry, Detection line** (claim f655682b73). "in mail-flow telemetry, messages to school addresses ... from senders outside the school's own mail systems" is cited to the canton, whose release only names fraudulent messages posing as the school or IT support as the main risk.
11. **Run record, Recency bullet.** "the PAN-OS update rests on Dream Research (2026-10-29), Unit 42 (2026-10-29) and Hunt.io (2026-10-30)": no entry of the run cites Hunt.io.

### Surface contradiction (F9)

12. **PAN-OS entry.** Dream: "The exploited surface is the PAN-OS management web server, which also fronts the GlobalProtect portal." Palo Alto FAQ: "GlobalProtect portal, gateway and Clientless VPN are not impacted." The entry carries Palo Alto's statement only; the run record notes concede this ("the entry carries Palo Alto's statement only"). Add a `Contradiction:` line.

### Needs more research (F8)

13. **eMudhra entry.** Python's release post of 2026-10-26 (five expedited releases, CVE-2026-115557) is not in the entry; the entry still presents pip 26.2.2 as the Python fix and cves[] says no release is named. This run also removed sourced detail: BleepingComputer's "P-384 private keys generated in April 2025 that had values smaller than 256, allowing anyone to recover them by testing just 256 possible numbers"; OpenJDK's `-Dcom.sun.net.ssl.checkRevocation=true` and `-Dcom.sun.security.enableCRLDP=true`; the tracker's note on macOS command-line tools (updated 28 October: git, curl and python3 still trust the certificates).
14. (low confidence) **PAN-OS entry.** The rewrite dropped the threat-log detection and the vendor's Threat Prevention coverage (Threat IDs and their four conditions) from the current-state analysis; they survive only in older dated sections.

### Missed angles (F10)

15. **PHP / PAN-OS entries.** GreyNoise's PHP2Shell tracker (https://php.events.greynoise.io/, last updated 2026-11-01 03:22 UTC; WebFetch summary: 1,177 exploitations confirmed from 5 attacker IPs, first on 2026-10-28, post-exploitation including reverse shells, SSH authorized_keys writes, Docker and cloud-metadata recon) is covered nowhere in the PHP2Shell cluster. Hunt.io (https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls) is the separate vantage on the PAN-OS rooting and names hand-picked government and bank targets; the run's own S3 findings carried it and the entry dropped it. Queries: "GreyNoise php2shell shells apache2 reverse shell authorized_keys October 28 2026"; "Hunt.io PHP2Shell one week later PAN-OS open directory".

### Drop (low relevance / off-audience / duplicate) (F7)

16. (low confidence) **Vaud entry.** Routine is right, but the incident floor allows two sentences plus a one-clause relevance ground; the body has four sentences and three labelled lines, no relevance-ground clause, an Exposure line that restates the headline and a Detection line that is derivation. The pupil suspicion may count as an actor, hence low confidence.

### Action-item discipline (F18)

17. **PAN-OS actions[1]** copies the Detection/takeaway text and duplicates CVE-2026-46300 actions[1] (and part of the PHP entry's third action); keep one home. (low) **eMudhra actions[2]** transcribes Cisco's table including December 2026 and April 2027 builds, which are not start-now tasks.

### Classification missing / inconsistent (F17)

18. (low confidence) **PAN-OS entry** credibility moved to 1; the entry's own sourcing note says the two reports are "not fully independent" and the CL-UNK-1280 designation is a single relay; 2 fits unless the Hunt.io capture is cited.

### Editorial / less-is-more flags (advisory) (F11)

19. **CVE-2026-46300 entry**: the 2026-10-29 section still says Dream "does not name the vendor" and "one large vendor's firewall software" with no supersession note (the PHP entry has one).
20. **Entity links**: PHP and CVE-2026-46300 entries lack `campaign:php2shell-pan-os-fragnesia-rooting-2026-10` and `actor:cl-unk-1280` (PHP also lacks `product:palo-alto-networks-pan-os`).
21. **PAN-OS techniques[]**: the nine ids are all active in the pinned ATT&CK v20 data and supported; the SOCKS5 proxy (T1090) and the decrypted LDAP service-account credential carry no id.
22. **Record summaries** narrate edits ("The summary, the chain description, the appliance action and the sourcing note name the product", "the entry now carries", "Two actions are rewritten").
23. (low confidence) **ARTEX entry**: Microsoft's "since at least September 2026" and GTIG's "dating back to at least August 2026" for the overlapping campaign sit unreconciled.

### Checks that came back clean (not findings)

All 14 evidence quotes the gate matched are verbatim on their pages (Dream, Unit 42 quotes re-read). Vaud: every figure, date, authority and the three evidence quotes (with originals) match vd.ch and RTS; SRF and Le Temps only relay the release; `single-source-victim` and the sourcing note are right; priority `routine`, classification A/2 consistent. CL-UNK-1280 is attributed exactly as Dream's relay ("Dream relays that Unit 42 tracks it as CL-UNK-1280 ... while Dream names no actor"); Unit 42's brief does not carry the designation, which the entry's sourcing note already says. 25 versus 24 rooted servers reconciles (24 firewalls plus the management server). GitLab 2026-10-29 is confirmed by the Atom feed (`<published>2026-10-29T00:00:00Z</published>`) and GitLab's page date field is wrong (2010-01-19), as the sourcing note anticipates. Microsoft (Windows trust list 2026-10-26, Edge 2026-10-27, Disallowed CTL 2026-10-20), Cisco v1.5 (2026-10-30; ISE 3.5P5 Dec 2026, 3.3P13 and 3.4P8 Apr 2027; IOS XE, MDS 9000, Nexus under investigation) and GitLab (19.5.3 line list, Runner 19.5.1, AI Gateway) match. GTIG details (2 to 25 second bursts, MySQL general-log JSP shells, UNC7228 overlap, repository takedown) match. KEV listings (2026-10-26 PHP, 2026-10-28 CVE-2026-46300 with the chaining sentence) match the catalog (version 2026.10.30). All techniques[] ids in the five touched vulnerability/threat entries and the Vaud entry resolve to active ids in the pinned data; no IOCs, no em dashes outside a verbatim quote, no workflow vocabulary in entry text. Changelog contract: `updated_at` moved only for the three `update` records, not for the two `improvement` records; each non-internal record has its section. Coverage: no relevant KEV addition is missing (the four KEV additions of 2026-10-29 and 2026-10-30 have entries); the weekend window is plausibly quiet; the GreyNoise and Python items above are the only gaps found.

### Verdict

NEEDS_FIXES (truth: 11, editorial: 7, advisory: 5)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (body, paragraph 2)
  item: "PAN-OS entry, Dream Research chain description"
  url_or_quote: "entry: \"On two firewalls of a US government-affiliated organization it added a reboot-persistent reverse SSH tunnel\" / source: https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
  summary: "Dream says the first of the two firewalls 'crashed shortly after ... and never came back online' and that the tunnel was built on the second ('An 8-port reverse SSH tunnel connected the compromised firewall back'). The tunnel is on one firewall, not two; the PHP and CVE-2026-46300 entries already say 'the second of two firewalls (the first crashed)'. Fix the clause."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates (Exposure line; cves[CVE-2026-115557].fixed)
  item: "eMudhra entry, tracker-derived fixed versions"
  url_or_quote: "entry: \"the tracker lists fixed versions for Python (3.15.1, 3.14.9 and 3.13.17, and pip 26.2.2) ... and lists Bottlerocket, Godot, LibreOffice and RHEL 7 as still pending\" / source: https://emudhra.we-have-a-problem.com/"
  summary: "The live tracker lists Python 3.15.2, 3.14.10, 3.13.18, 3.12.16, 3.11.18 (not 3.15.1, 3.14.9, 3.13.17), shows RHEL ca-certificates 2026.2.92_v9.0.319-70.3.el7_9 (RHEL 7 is not pending), and lists pending: Bottlerocket, OpenHarmony/HarmonyOS NEXT, certbot, containerd, Godot, LibreOffice. Python's own release post (blog.python.org, dated 2026-10-26) says 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 carry CVE-2026-115557 'Distrust compromised eMudhra intermediate CA keys'; 3.15.1/3.14.9 are not named as carrying it. The cves[] fixed string for CVE-2026-115557 repeats the stale versions."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (body, paragraph 2)
  item: "PHP entry, PAN-OS hotfix status"
  url_or_quote: "entry: \"with all but one of its hotfixes released and 11.1.7-h12 due on 2026-10-30\" / source: https://security.paloaltonetworks.com/CVE-2026-109618"
  summary: "The advisory now reads '11.1.7 through 11.1.7-h* | Upgrade to 11.1.7-h12 or 11.1.16-h4 or later' and its timeline (2026-10-29T23:54Z) says 'Removed ETAs for 11.1.7-h12 as the version is released.' All twenty hotfixes are out, which the PAN-OS entry updated in the same run states. The present-tense clause in the PHP entry is stale and contradicts it."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (body, vendor list)
  item: "PHP entry, Cisco fix versions"
  url_or_quote: "entry: \"with fixes at 15.5.21, 27.1.1 (November 2026) and 3.2.0\" / source: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  summary: "Version 1.10 of 2026-OCT-30 lists Unified Industrial Wireless Software (URWB) CSCwx37073 at '26.2.1.9 (Nov 2026)' and ISE Portal Builder as 'Fix deployed, no customer action required'; 27.1.1 no longer appears. The store's own 2026-10-28/cisco-php2shell entry already records 26.2.1.9 instead of 27.1.1."
- code: F3
  category: claim-not-supported
  section: 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse (summary; record summary of 2026-11-01T03:29:45Z)
  item: "ARTEX entry, GTIG attribution of three frameworks"
  url_or_quote: "entry: \"have seen ARTEX, PentAGI and CAIRN operated in incident-response cases by extortion groups and suspected PRC-nexus clusters\" / source: https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks"
  summary: "GTIG ties extortion groups and suspected PRC-nexus clusters to ARTEX only ('ARTEX has been adopted by a diverse range of threat actors ... including both financially motivated extortion groups and suspected cyber espionage operators'; 'additional suspected PRC-nexus clusters'). For PentAGI it names no actor type (Asian system integrators and telecom, aerospace targeting) and for CAIRN nothing. The summary and the record summary spread the ARTEX attribution over all three frameworks. Split the clause."
- code: F3
  category: claim-not-supported
  section: 2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils (body, RTS sentence)
  item: "Vaud entry, RTS 'no context, motive or method known'"
  url_or_quote: "entry: \"with no context, motive or method known\" / source: https://www.rts.ch/info/regions/vaud/2026/article/vaud-les-donnees-de-plus-de-40-000-eleves-et-profs-volees-29401382.html"
  summary: "RTS says only 'On ne connaît ni le contexte, ni les raisons, ni les objectifs de ce vol' (context, reasons, objectives). It does not say the method is unknown (it quotes an expert speculating about an insider with undue privileges). Replace 'method' with 'objective' or drop the word."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates (actions[1]; Defender takeaway)
  item: "(low confidence) eMudhra entry, disconnected Windows devices"
  url_or_quote: "entry: \"Windows devices that do not receive automatic certificate-trust updates need Microsoft's out-of-band update of 2026-10-26\" / source: https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys"
  summary: "(low confidence) MSRC's instruction for disconnected devices is 'make sure your update process delivers the updated Disallowed Certificate Trust List and the upcoming trust-list changes.' The entry names only the root-removal update and omits the Disallowed CTL update of 2026-10-20, which is the block of the compromised intermediates that a disconnected device lacks."
- code: F3
  category: claim-not-supported
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (body, Dream chain clause)
  item: "(low confidence) PHP entry, Dream citation date"
  url_or_quote: "entry: \"... management web server of Palo Alto Networks PAN-OS (PHP 8.0.30) ... ([Dream Research, 2026-10-27](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)\" / source dateline: \"Updated: October 29, 2026.\""
  summary: "(low confidence) Dream names PAN-OS only in its 2026-10-29 update ('The affected devices run specific versions of Palo Alto Networks PAN-OS'); the clause that now says PAN-OS still carries the 2026-10-27 label. Use the 2026-10-29 label for this clause."
- code: F4
  category: hallucinated-fact
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (Detection line)
  item: "(low confidence) PAN-OS entry, crash or reboot signal"
  url_or_quote: "entry: \"very large multipart POST requests from outside the administrator range and an appliance crash or reboot after them\" / source: https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
  summary: "(low confidence) Dream reports one firewall that 'crashed shortly after — likely from the ~900MB of exploit traffic — and never came back online'. No source reports a reboot after the POSTs or a crash as a general signal; the line states an n=1 observation as a detection signature and adds 'reboot'."
- code: F4
  category: hallucinated-fact
  section: 2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils (Detection line)
  item: "(low confidence) Vaud entry, Detection content"
  url_or_quote: "entry: \"in mail-flow telemetry, messages to school addresses that pose as the school or IT support, from senders outside the school's own mail systems\" ([Etat de Vaud, 2026-10-31])"
  summary: "(low confidence) The canton's release says only that the main risk is 'des messages frauduleux ciblés, se faisant passer pour l'école ou le support informatique'. Mail-flow telemetry and 'senders outside the school's own mail systems' are the entry's own derivation, cited to the canton as if stated."
- code: F4
  category: hallucinated-fact
  section: runs/2026-11-01/2026-11-01T0256Z-intel.md (Verification & coverage notes, Recency bullet)
  item: "Run record claims the PAN-OS update rests on Hunt.io"
  url_or_quote: "record: \"the PAN-OS update rests on Dream Research (2026-10-29), Unit 42 (2026-10-29) and Hunt.io (2026-10-30)\""
  summary: "The PAN-OS entry's sources[] and body cite Dream Research and Unit 42 only; Hunt.io (https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls) appears nowhere in any entry of the run. Either cite it (it is the only separate vantage on the PAN-OS rooting, see the F10 finding) or correct the note."
- code: F9
  category: surface-contradiction
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (body)
  item: "Dream says the PAN-OS management web server fronts the GlobalProtect portal; Palo Alto says GlobalProtect is not affected"
  url_or_quote: "Dream: \"The exploited surface is the PAN-OS management web server, which also fronts the GlobalProtect portal.\" / Palo Alto FAQ: \"GlobalProtect portal, gateway and Clientless VPN are not impacted.\""
  summary: "The entry carries only Palo Alto's statement. The run record's own notes admit 'Dream says the PAN-OS management web server also fronts the GlobalProtect portal, while Palo Alto's advisory says GlobalProtect is not affected; the entry carries Palo Alto's statement only.' Add a Contradiction line; a defender with a GlobalProtect-only exposed appliance needs to know the vendor and the discoverer differ."
- code: F8
  category: needs-more-research
  section: 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates (body, Exposure, actions)
  item: "Python expedited releases of 2026-10-26 missing; sourced root-cause and hardening detail removed this run"
  url_or_quote: "https://blog.python.org/2026/10/python-3152-31410-31318-31216-31118/ : \"Five expedited security releases to distrust the compromised eMudhra intermediate CA keys.\" Removed this run: BleepingComputer's \"all eight certificates used P-384 private keys generated in April 2025 that had values smaller than 256, allowing anyone to recover them by testing just 256 possible numbers\"; OpenJDK's -Dcom.sun.net.ssl.checkRevocation=true / -Dcom.sun.security.enableCRLDP=true flags; the tracker's macOS note"
  summary: "Python's own release post (2026-10-26) names 3.15.2, 3.14.10, 3.13.18, 3.12.16 and 3.11.18 as the releases carrying CVE-2026-115557; the entry still tells readers pip 26.2.2 is the Python fix and the cves[] record says no release is named. The run also cut the sourced root-cause specifics (P-384 keys below 256) a reverser reads first, the concrete revocation-check flags behind 'enable revocation checking', and the tracker's 28 October note that macOS developer tools (git, curl, python3) still trust the certificates and that macOS 27.2 undid user-applied fixes. Restore or re-add with citations."
- code: F8
  category: needs-more-research
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (body, Detection and Defender takeaway)
  item: "(low confidence) PAN-OS entry, vendor interim coverage dropped from the rewritten main analysis"
  url_or_quote: "removed: \"in threat logs, hits on the Threat IDs above where the signatures are active and the four conditions hold\" and the Threat IDs 543004 and 97622 to 97625 with their four conditions (all still on https://security.paloaltonetworks.com/CVE-2026-109618)"
  summary: "(low confidence) The rewrite deleted the only threat-log detection and the vendor's Threat Prevention coverage from the current-state analysis; both remain in the vendor advisory and only survive in older dated sections. Keep one clause for readers who cannot patch immediately."
- code: F10
  category: missed-angle
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619 (and the PAN-OS entry)
  item: "GreyNoise PHP2Shell exploitation tracker and Hunt.io open-directory findings not in the store"
  url_or_quote: "https://php.events.greynoise.io/ (last updated 2026-11-01 03:22 UTC; WebFetch summary: 'Of these, 1,177 exploitations were confirmed from 5 attacker IPs, with the first observed on 28 October 2026, when the web server spawned a shell'; logged post-exploitation includes reverse shells, a collection script, attempts to write SSH authorized_keys for the web user, and reconnaissance of Docker sockets and cloud metadata); https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls (2026-10-28/30: 'Operators stage these kits against hand-picked, high-value targets: a government finance ministry, a national bank, a government e-invoicing platform, telecom, and university systems')"
  summary: "No PHP2Shell entry or run-record note mentions GreyNoise (the only GreyNoise hit in entries/ is an unrelated September Zyxel entry; none in prior_coverage.json); its tracker is the only running in-the-wild dataset beyond three honeypots and shows continuing post-patch exploitation with concrete post-exploitation behaviour for a critical-priority entry. Hunt.io is the separate vantage that would corroborate the PAN-OS rooting (the run record says the update rests on it). Suggested query: 'GreyNoise php2shell shells apache2 reverse shell authorized_keys October 28 2026'; 'Hunt.io PHP2Shell one week later PAN-OS open directory'."
- code: F7
  category: drop
  section: 2026-11-01/vaud-school-it-support-platform-data-theft-teachers-pupils (body)
  item: "(low confidence) Vaud entry length against the incident floor"
  url_or_quote: "body paragraph 1: four sentences, plus Exposure, Detection and Defender takeaway lines; the sources give \"no access method, actor or platform product\" (the entry's own words)"
  summary: "(low confidence) The incident floor allows a routine incident without vector, actor or behaviour beyond the impact two sentences plus its transfer ground, and requires one plain clause stating why it is relevant. The entry is routine (correct) but runs to four sentences and three labelled lines, states no relevance-ground clause, its Exposure line restates the headline, and its Detection line is derivation (see F4). The unnamed-source pupil suspicion may count as an actor, which is why this is low confidence. Cut to two sentences plus a relevance clause (Swiss cantonal public sector, 41,500 account holders) and keep the phishing takeaway."
- code: F18
  category: action-item-discipline
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (actions[1]); 2026-10-21/emudhra-intermediate-ca-keys-recoverable-trust-store-updates (actions[2])
  item: "PAN-OS second action restates Detection/takeaway and duplicates the CVE-2026-46300 action; eMudhra Cisco action includes not-start-now items"
  url_or_quote: "PAN-OS actions[1]: \"look for a PHP file nobody deployed in a web-reachable directory of the management web server, a systemd service or rc.local entry that starts scripts from a hidden directory under /usr/local/lib and outbound SSH from the management plane\" vs the Detection line (near-verbatim) and CVE-2026-46300 actions[1]: \"look for PHP files in web-reachable directories that nobody deployed, an outbound SSH session from the host that a systemd service or an rc.local entry keeps up\"; eMudhra actions[2]: \"... ISE and ISE-PIC (3.5P5 in December 2026, 3.3P13 and 3.4P8 in April 2027), Meraki MV Smart Camera Firmware (2026-11-18) and IOS XR 26.4.1 (2026-11-30) when they ship\""
  summary: "F18(b)/(d): the PAN-OS action copies the body's Detection and takeaway text and duplicates an earlier in-window action on the CVE-2026-46300 entry (and partly the PHP entry's third action); keep one home. F18(a)/(c) low: the eMudhra Cisco action transcribes a vendor table including December 2026 and April 2027 builds, which are not start-now tasks; cut to the products with fixes available now."
- code: F17
  category: classification
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (classification)
  item: "(low confidence) credibility moved from 2 to 1"
  url_or_quote: "classification: {reliability: A, credibility: 1}; sourcing_note: \"Dream worked with Palo Alto Networks, so the two are not fully independent. The CL-UNK-1280 designation comes only from Dream's page.\""
  summary: "(low confidence) Credibility 1 means confirmed by independent sources. The entry itself says the two reports behind the chain are not fully independent and the actor claim is a single relay; the independent vantage (Hunt.io) is not cited. 2 fits the corroboration the entry shows unless the Hunt.io capture is added."
- code: F11
  category: editorial-advisory
  section: 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x (Update 2026-10-29 section)
  item: "supersession wording differs between the sibling entries"
  url_or_quote: "Fragnesia 10-29 section: \"Dream could not tell whether any of the Active Directory attacks succeeded, does not name the vendor\" and \"one large vendor's firewall software\"; the newest section does not mark it superseded, while the PHP entry's newest section says 'The earlier description of \"one unnamed vendor\" above is superseded.'"
  summary: "Advisory. The older statement is true of the page version it cites (2026-10-27) but a reader of the Fragnesia entry meets 'does not name the vendor' above a section naming it. Add the same one-line supersession note."
- code: F11
  category: editorial-advisory
  section: 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619; 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x
  item: "entity links"
  url_or_quote: "entities of both entries lack campaign:php2shell-pan-os-fragnesia-rooting-2026-10 and actor:cl-unk-1280 (the PHP entry also lacks product:palo-alto-networks-pan-os) although both now describe the chain and name PAN-OS"
  summary: "Advisory. The registry gained the campaign and actor keys this run and only the PAN-OS entry carries them; the entity pages for the campaign will miss the two sibling entries."
- code: F11
  category: editorial-advisory
  section: 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (techniques[])
  item: "behaviours described by Dream with no technique id"
  url_or_quote: "Dream: \"A SOCKS5 proxy for arbitrary internal network access\"; \"Decrypted the LDAP service account password\""
  summary: "Advisory. The mapped set (T1190, T1068, T1505.003, T1572, T1543.002, T1037.004, T1110.003, T1087.002, T1552.004) checks out against the pinned ATT&CK v20 data (all active), but the SOCKS5 proxy (T1090) and the recovered LDAP service-account credential have no id."
- code: F11
  category: editorial-advisory
  section: updates[] summaries of the PAN-OS, PHP and eMudhra records
  item: "record summaries narrate record-keeping"
  url_or_quote: "PHP record: \"The summary, the chain description, the appliance action and the sourcing note name the product.\"; PAN-OS record: \"the entry now carries the post-patch compromise check and a second action\"; eMudhra record: \"Two actions are rewritten\""
  summary: "Advisory. These sentences describe edits to the entry (field names, 'the entry now carries'), not the reader-facing change; the store has used this pattern before, so leave or trim at the main agent's discretion."
- code: F11
  category: editorial-advisory
  section: 2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse (summary vs Update 2026-11-01)
  item: "(low confidence) onset dates not reconciled"
  url_or_quote: "summary: \"since at least September 2026 Storm-0940\" vs GTIG: \"activity now dating back to at least August 2026\" for the overlapping UNC7228 campaign"
  summary: "Advisory. GTIG's earlier onset for the overlapping campaign sits beside Microsoft's September start without a note; one clause would reconcile them."
```
