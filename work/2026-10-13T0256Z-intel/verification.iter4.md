**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-13T04:14:52Z · ended_at=2026-10-13T04:24:53Z · duration_seconds=601

## Verification report — 2026-10-13T0256Z-intel (iteration 4)

Scope: post-fix pass. All 104 claims in `claims.iter4.yaml` carry a verdict row in `verification.iter4.claims.yaml` (the 3 changed claims, every claim of the Danfoss, MikroTik, Publica entries and the run record, and every claim of the SonicWall and GitLab entries; no sampling). `claim_ledger.py --coverage 4`: 104/104 answered. Sources were read this pass from the run's cached bodies plus live re-reads of CERT-FR ALE-012 and AVI-1275 (raw HTML version history), the MikroTik notice, the CISA KEV catalogue (still 2026.10.08; none of CVE-2026-84411, CVE-2026-102255, CVE-2026-97229), NCSC Security Hub posts 13034 and 13051 and the 25 newest hub posts, Publica's own page, AFP, and CISA ICSA-26-272-06 via WebFetch (outbound-links template).

### Iteration 3 remediations, checked against the sources

1. Run-record notes: CORRECT. They now say iteration 2 fixed all but one declined F11 and that the Danfoss entry says counts moved during the day; the entry says exactly that (BFMTV: "deux fois plus élevé que les premières estimations, qui faisaient état de 150"; Infosecurity quotes 150). One new count slip in the same notes (F4 #5 below).
2. Danfoss first sentence: CORRECT. "AFP reports from the retailers' statements at least 300 Intermarché or Netto shops and more than 100 Coopérative U outlets" matches AFP ("the retailers told AFP in separate statements").
3. Danfoss sourcing_note "no other source reports them independently": CORRECT. AFP relays BFMTV, Infosecurity quotes BFMTV, BleepingComputer cites French outlets.
4. Publica improvement section and record summary: CORRECT. They state the data classes directly (Publica page, Stand 08.10.2026: Zivilstand, Angaben zu Ehepartner/Lebenspartner, IBAN; "vermutlich Personendaten ... abgeflossen"; cash.ch/AWP: "eher kleine Datenmenge", "Geschäftsdaten") with no narration of the entry's history.
5. MikroTik CISA date: CORRECT. WebFetch of ICSA-26-272-06: "Initial Release Date: 2026-09-29", revision history "2026-09-29 | 1 | Initial Publication"; source record and inline citation both read 2026-09-29.

Registry record `incident:danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack-2026-10`: CORRECT (defrost attributed to BFMTV, compromises to CERT-FR, `affects` notes match AFP "AK-SM800 and AK-SC355 ... notably affected"; products keyed separately from `product:danfoss-ak-sm-800a`).

### Unsupported / hallucinated facts

- F4 #1 — SonicWall, "Update — 2026-10-10T03:44:08Z": "...so Previdian is the only observer named in the sources read". The BleepingComputer 2026-10-09 article cited in that paragraph states "Previdian's reports were also confirmed by threat intelligence firm Defused, which said that 'Since yesterday we have been observing unauthenticated SSRF traffic against our SonicWall SMA decoys.'", and the 2026-10-13 section now carries Defused as a second operator. The earlier clause is superseded (and was already contradicted by its own cited page). Reword or drop it; the 2026-10-13 record already names `body` in `fields`.
- F4 #2 (low confidence) — MikroTik, Exposure: "a RouterOS device on a version before 7.24 whose www or www-ssl service an attacker can reach" (same wording in `cves[].affected`). After the correction the entry says 7.23.8 and 6.49.23, both below 7.24, carry the fix ("Owners of long-term and v6 devices can therefore upgrade"), so a device on 7.23.8 or 6.49.23 reads as exposed in Exposure but as fixed in the takeaway. MikroTik's notice itself says "before 7.24"; state the range per channel.
- F4 #3 (low confidence) — Publica, actions[1]: "the funds that have spoken say they see no indication of theft or that it is under review". Publica is a fund that has spoken and its page says "dass dabei vermutlich Personendaten von versicherten Personen abgeflossen sind", which the new improvement section carries. Name the funds (BPK, BLVK, Pensionskasse Post).
- F4 #5 — Run-record notes: "the probe covered 241 records and its UNSOLVED list held one record, ico-uk". `source_health.out`: "# sweep complete: 242/242 probed", verdicts 241 relevant + 1 stale; `state/source_health.json` by_verdict {relevant: 241, stale: 1}. The probe covered 242 records.

### Citation does not support the claim

- F3 #4 (low confidence) — SonicWall, "[Previdian, 2026-10-10](https://previdian.com/CVE-2026-102255)" (source record and inline citations, re-used in the 2026-10-13 section). The page's JSON-LD gives datePublished 2026-10-07T13:07:13Z and dateModified 2026-10-12T15:21:59Z (visible "Updated 13 Oct 2026"); 2026-10-10 is only its last-observed date. A live tracker page, so the date is ambiguous; use the publication or modified date.

### Verified without findings

- Danfoss: every body claim re-checked against AFP (300 Intermarché/Netto, over 100 Coopérative U, Danfoss legacy/no updates, AK-SM800 and AK-SC355 "notably affected", "long advised supermarkets to update from those models", PM aide on ANSSI), BFMTV (conditional "auraient", 50 degrees, "antérieures à la version 4", 300 = twice 150, "moins d'une centaine"), CERT-FR (both evidence quotes verbatim; remediation steps scoped to "En cas de suspicion de compromission"; first and last version 12 octobre 2026), Infosecurity (150, vulnerable consoles, Belgium and the Netherlands) and BleepingComputer (no vector known). No overlap with the store (the Claroty entry is declared in `references[]`). No Swiss victim in any source; the entry says so.
- GitLab (CVE-2026-97229): GitLab 19.4.2 page (integer overflow, CVSS:3.1 10.0 PR:N, affected 19.2 before 19.2.8, 19.3 before 19.3.5, 19.4 before 19.4.2, 19.3.4 merge-request bug, 90-day issue disclosure, single-node downtime, no workaround section); CERT-EU and BleepingComputer both say 19.3.4; NCSC post 13051 status UNKNOWN and the prerequisite quote verbatim; 19.4.1 page CVE-2026-89078 and CVE-2026-93577 both "authenticated user", reporter joaxcar. No overlap in cves_seen or prior coverage.
- MikroTik: 7.23.8 changelog (2026-10-08) and the 6.49.23 forum post (2026-10-07) carry "system - improve stability (includes CVE-2026-84411);"; the notice, re-read live, still lists both long-term releases as pending; correction record fields match `git diff HEAD`; `updated_at` stays null; KEV 2026.10.08 has no entry for the CVE.
- SonicWall: NCSC post 13034 history ("updated with Active exploitation claims", Defused "since oct. 8th", Previdian "since oct. 9th"); SecurityWeek, The Hacker News (135 attempts, two unique US addresses, both operators dated to 8 October), Previdian (First observed 09 Oct 2026), BleepingComputer and CERT-FR AVI-1275 (dated 07 octobre 2026) agree with the section; record fields match the diff; CVE status correctly stays patch-available.
- Publica: all body citations re-check against admin.ch, PK Softech, watson, Netzwoche, BPK, BLVK, Pensionskasse Post, Inside IT, Publica and cash.ch; evidence quotes and translations faithful.
- Run record: entries_published 2, entries_updated 3, updated_entry_ids, entities_added, sub-agent item counts (4, 8, 4, 4), KEV diff (0 additions), the S2 and S4 returns of Danfoss and the S1 and S2 returns of GitLab, the sources.json changes (cash-ch-awp promoted with 4 prior citing runs, znuny-advisories added, cybercrimepolice-ch rss, msrc-blog url, ico-uk probe_timeout 120), the `tools/source_health.py` change, the four backlog rows and their expiries, and the iteration 1 to 3 counts all hold on disk.
- Missed angles: none found. NCSC Security Hub's newest posts are the two entries' advisories; the 2026-10-12 hub edits on Atlassian CVE-2026-21589 and PaperCut were assessed by S1 and S2 as carrying no delta (the store already records the attempts); the live KEV catalogue shows no addition since 2026-10-08; Microsoft's 2026-10-13 Patch Tuesday is correctly deferred to the next fire.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 0, advisory: 0). F4 #1 is a clear contradiction inside the SonicWall entry (older section against its own cited page and the new section); the other four are small, low-confidence consistency, date and count slips.

### Findings summary (machine-readable)

See `work/2026-10-13T0256Z-intel/verification.iter4.findings.yaml` (5 records).
