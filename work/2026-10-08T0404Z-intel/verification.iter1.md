**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-08T05:05:10Z · ended_at=2026-10-08T05:25:02Z · duration_seconds=1192

## Verification report — 2026-10-08T0404Z-intel (iteration 1)

Scope covered: 192 of 192 ledger claims (verdict rows in `work/2026-10-08T0404Z-intel/verification.iter1.claims.yaml`: 183 ok, 5 F3, 2 F5, 1 F14, 1 F4), the four new entries, the four updated entries read whole with `git diff HEAD` for each, the run record, `entities/registry.yaml`, `state/coverage_backlog.md`, `state/cves_seen.json` and `sources/sources.json` diffs. Every cited URL was fetched this iteration (`extract`, `pdf`, `ncsc-csh post`, `cisa-kev`; CISA pages and the unreadable SonicWall PSIRT SPA through WebFetch). Reader-facing quotes in all eight entries were checked against fetched page bodies.

### Broken / unreachable URLs
None. All cited URLs resolved to specific pages. The SonicWall PSIRT page is an SPA that the reader returns without its fixed-build table (WebFetch returns nothing); the fixed builds were confirmed on The Hacker News and CERT-FR, both of which agree.

### Generic / oversight URLs (replace with specific article)
Folded into finding #6 below (Zammad GitHub advisory listing index).

### Citation does not support the claim
- #3 (low confidence) FortiBleed, first body paragraph: "Per BleepingComputer, a Russian-speaking actor is performing systematic credential validation, offline password cracking and onward lateral movement into Active Directory ..." BleepingComputer 2026-06-18 attributes this to Bob Diachenko ("claimed the operation was conducted by a Russian-speaking multi-operator threat group", "allegedly"). Hedge dropped and claim presented as the outlet's own. Re-attribute as a claim.
- #4 (low confidence) FortiBleed, 2026-06-20 update: "cracked SSL VPN password hashes with a 45-GPU Hashtopolis cluster, after which the actors pivot into internal Active Directory" is cited to BleepingComputer 2026-06-19 (CISA warns ...), whose text has no "GPU", "Hashtopolis" or "Active Directory". The wording is in BleepingComputer 2026-06-18 and SecurityWeek 2026-06-19, as Diachenko's claim.
- #5 (low confidence) Atlassian, Update 2026-10-08: "NCSC Switzerland's advisory, edited on 2026-10-07 to add the public proof of concept, still lists the exploitation status as unknown". Post 13032 carries two lines: the original "Current exploitation status: UNKNOWN" and the line appended by the edit, "Current exploitation status: Proof of Concept Available". The latest status is the PoC line.
- #6 (low confidence) Zammad, Update 2026-10-07: "27 security advisories ... two critical, twelve high, ten medium and three low" is cited to `https://github.com/zammad/zammad/security/advisories`, a listing index that shows only the first ten records (1 critical, 2 high, 6 moderate, 1 low as read). The counts are true per the GitHub advisory-records API cited in the next clause (27 published 2026-10-06; 2/12/10/3; patched 7.2.1). Cite the API record for the counts; drop the listing index.
- #7 (low confidence) Power BI entry: the headline "a link to a public Power BI dashboard" and the body "The technique is to build a real dashboard under the attacker's own, usually compromised or throwaway, account ... set its sharing to public" present as this campaign's fact what Huntress describes as the method threat actors "have previously abused". For this campaign Huntress says only "a fake reference document on a legitimate Power BI domain".

### Unsupported / hallucinated facts
- #1 FortiBleed `sourcing_note` (written this run): "where the CISA guidance cited in the June update names an MD5-crypt scheme", and the 2026-06-20 section: "enforcement of PBKDF2 (replacing the older MD5-crypt admin-hash scheme)". No linked source names MD5-crypt. CISA alert via WebFetch (asked twice): the strings "MD5" and "crypt" do not appear. Fortinet's PBKDF2 tip (linked from the CISA alert): "In FortiOS v7.2.10, v7.4.7, v7.6.0, and earlier, the hash function is SHA256". Arctic Wolf (cited in the entry): "replacing the legacy SHA-256-based storage mechanism". The FBI/USSS advisory and BleepingComputer also say SHA-256. The recorded contradiction rests on a false premise; delete the sentence and correct the June update by a correction record.
- #2 FortiBleed `evidence[0]` and `evidence[1]` are not contiguous substrings of the cited pages. BleepingComputer 2026-06-22: "the alleged use of a Golang-based tool dubbed "FortigateSniffer," which abuses FortiOS's built-in diagnose sniffer packet functionality to capture authentication traffic". SecurityWeek 2026-06-22: "Fortinet says the large-scale credential-harvesting campaign ... does not exploit new vulnerabilities" and "threat actors reusing credentials from previous incidents and employing brute-force techniques ...". Quote 2 also has an inserted ellipsis and splices two sentences. The legacy rewrite listed `evidence` in `fields`; replace with verbatim text and add `source_url`.
- #9 (low confidence) BigDiskBuster: "holding a handle on the Malware Removal Tool executable". LevelBlue writes only "MRT.exe" / "MRT handle" and never expands it; Dark Reading does not mention it. The expansion is the entry's own.
- #10 (low confidence) Run record, Contradiction line: "AWP and ICTjournal say it was offered for sale on 25 September". AWP via cash.ch gives no date ("Rund einen Monat später ... zum Verkauf angeboten"). Only ICTjournal says 25 September. The entry itself is right.

### Claims missing inline citation
- #11 FortiBleed first body paragraph: "Fortinet's position is that this is **not a new vulnerability**: the corpus is a reshare of data from previous incidents combined with large-scale brute-forcing, and the credentials were validated as working." Uncited. Fortinet's PSIRT blog says credentials from previous incidents are reused with brute force and "This is not a new Fortinet vulnerability"; it does not say "reshare" or that the credentials were validated as working (that is Beaumont, Hudson Rock, SOCRadar).
- #12 FortiBleed: "**Why it matters to us:** FortiGate is ubiquitous on Swiss and EU public-sector perimeters." Uncited prevalence claim with an absolute quantifier.

### Strengthen primary source
- #13 (low confidence) FortiBleed `sources[]`: the first role-primary record is BleepingComputer; the rewritten sourcing_note names the FBI/USSS advisory as primary for the current state, listed tenth. Reorder.

### Quantifier without source
- #8 (low confidence) BigDiskBuster Exposure: "the technique needs only a process that can write to the user temp directory and a volume with free space to claim". LevelBlue shows a hidden file under %TEMP% and NT-level volume and MRT.exe handles; Dark Reading says it ran under a standard account. Neither says these are the only prerequisites.

### Editorial / less-is-more flags (advisory)
- #14 FortiBleed legacy body paragraphs carry em dashes (four paragraphs) and an inline `T1078`.
- #15 Fetch narration in reader-facing text: SonicWall sourcing_note "read here" (and it reads as though the vendor advisory lacks a fixed-build table), Ixa sourcing_note "the page read here", Zammad update "The write-up as read".
- #16 Power BI entry does not key `product:microsoft-power-bi`, which this run registered.
- #17 (low confidence) FortiMail: `type: improvement` carries a new vendor fact (Fortinet timeline "2026-10-07: FortiMail Cloud fix clarification") that narrows who must act; shape of an `update`. Leave if deliberate, to avoid re-floating a critical entry.
- #18 The 2026-09-03 (and 2026-07-14) SonicWall entries still say "Apply SonicWall's hotfix 12.4.3-03526 or 12.5.0-02952" / "Fixed in hotfix 12.4.3-03526 / 12.5.0-02952"; the new advisory shows those builds are affected. Consider an internal or improvement record there.
- #19 Atlassian summary "129 attempts from 22 addresses" was true at save time; the live Previdian page now reads 147 attempts / 23 IPs. Use "at least" or an as-of time. `state/cves_seen.json` still titles CVE-2026-21589 "no exploitation reported".
- #20 (low confidence) Atlassian actions[1] lookback "back to 2026-10-06, when exploitation attempts began": first honeypot sighting is not an exposure bound; fixes shipped 2026-10-05 and Atlassian cannot confirm absence of earlier use.
- #21 (low confidence) Ixa: "No source says how the attackers got in" and "list of affected sites are not public" over a paywalled primary, next to sites named by ICTjournal.

### Missed angles
None evidenced. The KEV catalog has no addition after 2026-10-04 (read directly: newest CVE-2026-88779, Citrix NetScaler, then the two Zammad CVEs and FortiMail, all covered). The NCSC Switzerland hub listing for the window (`ncsc-csh recent 30`) shows ILIAS (13035, 2026-10-07), SonicWall (13034), Atlassian (13032) and Citrix (13030) as in-window items; the ILIAS drop (authenticated RCE paths, no CVE ids, no exploitation) is defensible under the borderline-drop log. I could not verify the run record's HPE ClearPass or Cisco borderline drops from any fetched source. Coverage looks complete for the critical/high signal.

### Single-source items missing [SINGLE-SOURCE] flag
None. The Power BI entry carries `verification: single-source` with a sourcing_note.

### Org-triage line missing / inconsistent
None. No `org_triage` block and no watchlist tag on any entry. Priorities checked against `prompts/cti-run.md`: SonicWall `high` (pre-authentication CVSS 10.0 path on a remote-access gateway whose two earlier sibling pairs were exploited: the PD-11(b) sibling-flaw limb), Atlassian `high` (exploitation attempts, not compromise; `critical` was considered in the run record and `high` is defensible), Zammad `high`, FortiBleed `high`, FortiMail `critical` (exploited KEV zero-day with fixes), Ixa, Power BI and BigDiskBuster `notable`: no miscalibration found.

### Classification missing / inconsistent
None. All eight entries carry A-F / 1-6 codes consistent with source tier (vendor PSIRT and government advisories A; Huntress, LevelBlue B; single-source Power BI at credibility 2).

### Action-item discipline
None raised. Each new entry carries at most one action; Atlassian, Zammad and FortiMail carry two concrete, mechanism-derived tasks.

### Verdict
NEEDS_FIXES (truth: 10, editorial: 3, advisory: 8)

The two findings to weigh first are #1 (the MD5-crypt premise, written into this run's sourcing_note and contradicted by Fortinet, Arctic Wolf, the FBI/USSS advisory and BleepingComputer) and #2 (two legacy evidence quotes that are not on their cited pages). The four new entries and the three other updates are sound on every fact checked against fetched pages: SonicWall builds, CVSS and CVE ids (PSIRT, The Hacker News, CERT-FR, NCSC-CH, Canadian Cyber Centre, BleepingComputer), the Huntress campaign chain, the LevelBlue/Dark Reading technique and statements, the Ixa details (ICTjournal, AWP, Inside IT, Le Temps lead), Atlassian fixed versions and exploitation reporting (Atlassian, The Register, BleepingComputer, Previdian, SANS ISC, Canadian Cyber Centre), the Zammad chain (DIVD, NCSC-NL, Zammad, Horizon3, the advisory records) and the FortiMail revision (Fortinet PSIRT timeline, CSAF record, BleepingComputer, NCSC-CH, NCSC-NL, Belnet, CISA).

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (sourcing_note; 2026-06-20 update)"
  item: "FortiBleed legacy admin password-hash scheme"
  url_or_quote: "sourcing_note: \"where the CISA guidance cited in the June update names an MD5-crypt scheme\"; 2026-06-20 section: \"enforcement of PBKDF2 (replacing the older MD5-crypt admin-hash scheme)\""
  summary: "No linked source names MD5-crypt. CISA alert (WebFetch, asked twice): 'MD5' and 'crypt' do not appear, only 'weaker legacy hashes'; Fortinet's own PBKDF2 tip: 'In FortiOS v7.2.10, v7.4.7, v7.6.0, and earlier, the hash function is SHA256'; Arctic Wolf (cited in the entry): 'replacing the legacy SHA-256-based storage mechanism'; the FBI/USSS advisory and BleepingComputer also say SHA-256. The contradiction recorded in sourcing_note rests on a false premise. Delete the sentence from sourcing_note and correct the June update (correction record, fields sourcing_note and body)."
- code: F4
  category: hallucinated-fact
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (evidence[0], evidence[1])"
  item: "FortiBleed legacy evidence quotes are not verbatim"
  url_or_quote: "\"Threat actors deployed a Golang-based tool called 'FortigateSniffer' that abused FortiOS's built-in diagnose sniffer packet functionality to harvest authentication credentials from network traffic\" (BleepingComputer); \"Fortinet states the attack does not exploit new vulnerabilities, but rather reuses credentials from prior incidents ... combined with brute-force techniques against systems lacking strong passwords and MFA\" (SecurityWeek)"
  summary: "Neither string is a contiguous substring of the cited pages as fetched. BleepingComputer 2026-06-22 reads 'the alleged use of a Golang-based tool dubbed \"FortigateSniffer,\" which abuses FortiOS's built-in diagnose sniffer packet functionality to capture authentication traffic' (paraphrase, 'alleged' dropped). SecurityWeek 2026-06-22 reads 'Fortinet says the large-scale credential-harvesting campaign ... does not exploit new vulnerabilities' and 'threat actors reusing credentials from previous incidents and employing brute-force techniques against devices with weak password hygiene and no multi-factor authentication (MFA)'. The second quote also carries an inserted ellipsis and splices two sentences. Replace with verbatim substrings and add source_url."
- code: F3
  category: claim-not-supported
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body, first paragraph)"
  item: "(low confidence) Russian-speaking actor claim stated as BleepingComputer's finding"
  url_or_quote: "\"Per BleepingComputer, a Russian-speaking actor is performing systematic credential validation, offline password cracking and onward lateral movement into Active Directory at fully-compromised organisations in several countries\""
  summary: "BleepingComputer 2026-06-18 attributes this to researcher Bob Diachenko ('later shared additional information that claimed the operation was conducted by a Russian-speaking multi-operator threat group'; 'allegedly'); the entry drops the claimed/alleged hedge and presents it as the outlet's own reporting in present tense. Re-attribute to Diachenko as a claim."
- code: F3
  category: claim-not-supported
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (2026-06-20 update)"
  item: "(low confidence) 45-GPU Hashtopolis cluster and Active Directory pivot cited to the wrong BleepingComputer article"
  url_or_quote: "\"a Russian-speaking actor cracked SSL VPN password hashes with a 45-GPU Hashtopolis cluster, after which the actors pivot into internal Active Directory\" ([BleepingComputer, 2026-06-19](https://www.bleepingcomputer.com/news/security/cisa-warns-fortinet-users-to-secure-devices-after-fortibleed-leak/))"
  summary: "The 2026-06-19 BleepingComputer article (CISA warns ...) as fetched contains no 'GPU', 'Hashtopolis' or 'Active Directory'. The 45-GPU/Hashtopolis/AD wording is in BleepingComputer's 2026-06-18 leak article and SecurityWeek 2026-06-19, both as Diachenko's claim. Re-cite and re-attribute."
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (Update 2026-10-08T04:56:05Z)"
  item: "(low confidence) NCSC Switzerland exploitation status"
  url_or_quote: "\"NCSC Switzerland's advisory, edited on 2026-10-07 to add the public proof of concept, still lists the exploitation status as unknown\" ([NCSC Switzerland, 2026-10-07](https://security-hub.ncsc.admin.ch/#/posts/13032))"
  summary: "Post 13032 carries two status lines: the original block says 'Current exploitation status: UNKNOWN' and the block appended by the 2026-10-07 edit says 'Current exploitation status: Proof of Concept Available'. The page's latest status is the PoC line; 'still lists ... as unknown' misdescribes the edited post. Say it lists PoC available and does not report exploitation."
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach (Update 2026-10-07T04:52:00Z; sources[])"
  item: "(low confidence) severity breakdown cited to a listing index"
  url_or_quote: "\"The release comes with 27 security advisories published the same day, rated by Zammad as two critical, twelve high, ten medium and three low ([Zammad security advisories, 2026-10-06](https://github.com/zammad/zammad/security/advisories))\""
  summary: "The cited page is the repository's advisory listing index (an F2 pattern); as read it shows only the first 10 records (1 critical, 2 high, 6 moderate, 1 low), not 27 or the 2/12/10/3 split. The counts are true only per the GitHub advisory-records API cited in the next clause (27 published 2026-10-06, 2 critical, 12 high, 10 medium, 3 low, patched 7.2.1). Cite the API record for the counts and drop the listing index from the claim."
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-08/power-bi-dashboard-phishing-rogue-screenconnect-clients (title, headline, summary, body paragraph 1)"
  item: "(low confidence) 'public dashboard' and 'build a real dashboard under the attacker's own account' stated as this campaign's facts"
  url_or_quote: "headline: \"a link to a public Power BI dashboard delivers rogue ScreenConnect clients\"; body: \"The technique is to build a real dashboard under the attacker's own, usually compromised or throwaway, account, embed a malicious link in it and set its sharing to public\""
  summary: "Huntress states that method as what threat actors 'have previously abused Power BI in phishing attacks by creating real dashboards on app.powerbi.com under their own (usually compromised or throwaway) account ... and setting the dashboard's sharing permissions to public'. For this campaign it says only that the email link 'redirected users to a fake reference document on a legitimate Power BI domain'; it does not state the account type or sharing mode of this campaign's dashboard. Frame the method as the known prior technique the campaign appears to use, or hedge."
- code: F14
  category: quantifier-without-source
  section: "entries/2026-10-08/bigdiskbuster-defender-update-starvation-disk-exhaustion-poc (body, Exposure)"
  item: "(low confidence) 'needs only' prerequisites"
  url_or_quote: "\"the technique needs only a process that can write to the user temp directory and a volume with free space to claim\""
  summary: "LevelBlue says the PoC creates a GUID-named hidden file under %TEMP% and opens the volume device and MRT.exe through NT calls; Dark Reading says it ran under a standard user account. Neither states that temp-write plus free space are the only prerequisites. Soften to what the sources show (it ran from a standard account in LevelBlue's lab)."
- code: F4
  category: hallucinated-fact
  section: "entries/2026-10-08/bigdiskbuster-defender-update-starvation-disk-exhaustion-poc (body, Detection and Triage)"
  item: "(low confidence) 'Malware Removal Tool executable'"
  url_or_quote: "\"a non-Defender, non-TrustedInstaller process holding a handle on the Malware Removal Tool executable\""
  summary: "LevelBlue only writes 'MRT.exe' / 'MRT handle' and never expands the name; Dark Reading does not mention it. The expansion is the entry's own. Write 'MRT.exe' as LevelBlue does, or use the product name only if a fetched source supports it."
- code: F4
  category: hallucinated-fact
  section: "runs/2026-10-08/2026-10-08T0404Z-intel (verification notes, Contradiction line)"
  item: "(low confidence) AWP date attributed to 25 September"
  url_or_quote: "\"Inside IT says the Ixa data was published at the end of September, while AWP and ICTjournal say it was offered for sale on 25 September\""
  summary: "AWP via cash.ch gives no date: 'Rund einen Monat später seien die gestohlenen Dokumente im Darknet zum Verkauf angeboten worden' (about a month after the end-of-August attack). Only ICTjournal says 25 September. The entry itself attributes the date correctly; fix the run-record sentence."
- code: F5
  category: missing-citation
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body, first paragraph)"
  item: "Fortinet's position sentence"
  url_or_quote: "\"Fortinet's position is that this is **not a new vulnerability**: the corpus is a reshare of data from previous incidents combined with large-scale brute-forcing, and the credentials were validated as working.\""
  summary: "No citation on the sentence. Fortinet's published statement says threat actors are 'reusing credentials from previous incidents' and 'employing brute-force techniques against devices with weak password hygiene and no multi-factor authentication', and 'This is not a new Fortinet vulnerability'; it does not call the corpus a reshare and does not say the credentials were validated as working (that is Beaumont, Hudson Rock and SOCRadar). Cite Fortinet's PSIRT blog and move the validation clause to its own sources."
- code: F5
  category: missing-citation
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body, Why it matters to us)"
  item: "FortiGate prevalence claim"
  url_or_quote: "\"**Why it matters to us:** FortiGate is ubiquitous on Swiss and EU public-sector perimeters.\""
  summary: "Uncited factual claim with an absolute quantifier ('ubiquitous'); no source linked in the entry states FortiGate prevalence in Swiss or EU public-sector networks. Cite a source, reduce to 'widely deployed' with a link, or drop the sentence."
- code: F6
  category: strengthen-primary-source
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (sources[])"
  item: "(low confidence) first sources[] record is a news outlet"
  url_or_quote: "first record: https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/ (role: primary)"
  summary: "The rewritten sourcing_note names the FBI and U.S. Secret Service advisory as the primary source for the current state, yet it is listed tenth; the first role-primary record is BleepingComputer (SecurityWeek and a second BleepingComputer article are also role primary). Reorder so the FBI/USSS advisory and Fortinet PSIRT lead."
- code: F11
  category: editorial-advisory
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body)"
  item: "legacy body style: em dashes and an inline ATT&CK id"
  url_or_quote: "em dashes in the body paragraphs beginning \"A dataset branded\", \"**Why it matters to us:**\", \"Fortinet's PSIRT response confirms\", \"The delta for defenders\"; \"valid-account abuse (`T1078`)\""
  summary: "Reader-facing entry text carries em dashes (only the section heading is exempt) and an inline T-id that techniques[] already carries. The record's fields name body, so the legacy paragraphs are in this run's scope; replace dashes with commas or colons and drop the id."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-08/cve-2026-102255-sonicwall-sma1000-workplace-ssrf (sourcing_note); entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale (sourcing_note); entries/2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach (update 2026-10-08)"
  item: "fetch narration in reader-facing text"
  url_or_quote: "\"The SonicWall advisory text read here lists the four flaws and their scores but no fixed-build table\"; \"the page read here carries the standfirst and the opening paragraphs\"; \"The write-up as read does not name the Zammad version it was reproduced on\""
  summary: "'read here' and 'as read' narrate the pipeline's fetch, and the SonicWall sentence reads as if the vendor advisory lacks a fixed-build table (the reader simply returned none; the PSIRT page says 'upgrade to the mentioned fixed release version'). Keep two sentences of provenance: fixed builds come from The Hacker News and CERT-FR; Le Temps is paywalled; Horizon3 names no Zammad version."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-08/power-bi-dashboard-phishing-rogue-screenconnect-clients (entities[])"
  item: "entity-linking miss"
  url_or_quote: "entities: [\"product:connectwise-screenconnect\"]  (affected_products also names \"Microsoft Power BI\")"
  summary: "This run registered product:microsoft-power-bi (run record entities_added) but the entry does not key it; the abused platform is a subject of the entry. Add the key."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev (updates[] 2026-10-08T04:59:39Z)"
  item: "(low confidence) record type"
  url_or_quote: "type: improvement; \"## Improvement\" / \"Fortinet's revision of 2026-10-07 states that it remediated FortiMail Cloud on 2026-10-05\""
  summary: "The section carries a new vendor fact (Fortinet timeline entry '2026-10-07: FortiMail Cloud fix clarification') that narrows who must act, which is the shape of a type: update record rather than an improvement. The operator may deliberately avoid re-floating a critical entry for a scope-narrowing change; if so, leave it."
- code: F11
  category: editorial-advisory
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection; entries/2026-07-14/sonicwall-sma1000-ssrf-cve-2026-15409-actively-exploited"
  item: "older SonicWall entries now carry superseded actions"
  url_or_quote: "2026-09-03 actions[0]: \"Apply SonicWall's hotfix 12.4.3-03526 or 12.5.0-02952 to every SMA1000 6210/7210/8200v appliance now\""
  summary: "The new entry (correctly a separate finding with references[]) shows those builds are themselves affected by CVE-2026-102255, so the older entry's action and 'Fixed in hotfix 12.4.3-03526 / 12.5.0-02952' text now mislead a reader who lands on it. Consider an internal or improvement record on the 2026-09-03 entry pointing to the new advisory."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (summary; Update 2026-10-08T04:56:05Z); state/cves_seen.json"
  item: "live counter drift and stale index title"
  url_or_quote: "\"Previdian's sensors have recorded 129 attempts from 22 addresses\""
  summary: "True when saved (bodies/atl-previdian.txt: 129 / 22) but the live Previdian page now reads 147 attempts, 23 unique attacker IPs, same 8 countries and 3 sensors. Prefer 'at least 129' or an as-of time. Separately, the state/cves_seen.json title for CVE-2026-21589 still says 'no exploitation reported'."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (actions[1])"
  item: "(low confidence) lookback start date"
  url_or_quote: "\"search the web server and proxy logs back to 2026-10-06, when exploitation attempts began\""
  summary: "2026-10-06 is the first attempt Previdian and SANS observed on honeypots, not a bound on exposure: Atlassian published fixes on 2026-10-05, says it cannot confirm whether any instance was affected, and the fix diff exposes the technique. Start the lookback at 2026-10-05 (advisory date) or earlier."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale (body; summary; Exposure)"
  item: "(low confidence) negative claims over a paywalled primary"
  url_or_quote: "\"No source says how the attackers got in.\"; summary: \"the access vector and the list of affected sites are not public\"; Exposure: \"no source names the affected sites beyond the client categories above\""
  summary: "The primary (Le Temps) is readable only to its standfirst, so 'no source says' cannot be asserted for its full text; say 'none of the reports read states the vector'. The summary's 'list of affected sites are not public' also sits next to named sites in the body (Etablissements de la plaine de l'Orbe and Banque cantonale vaudoise per ICTjournal)."
```
