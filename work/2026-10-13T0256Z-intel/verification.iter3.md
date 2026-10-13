**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-13T04:04:37Z · ended_at=2026-10-13T04:13:47Z · duration_seconds=550

## Verification report — 2026-10-13T0256Z-intel (iteration 3)

Scope: post-fix pass. All 104 claims in `claims.iter3.yaml` carry a verdict row in `verification.iter3.claims.yaml` (all 9 changed claims, every claim of the Danfoss, MikroTik and SonicWall entries, and every claim of the GitLab and Publica entries; no sampling). Sources were read this pass from the run's cached bodies (`quote-bodies/`, `bodies/`) plus live re-reads of CERT-FR ALE-012 (raw HTML for the version-history dates), the AFP page, NCSC Security Hub posts 13034 and 13051 (`ncsc-csh post`), the GitLab 19.4.2 release page, the MikroTik notice and the CISA KEV catalogue (still 2026.10.08; none of CVE-2026-84411, CVE-2026-102255, CVE-2026-97229 present).

### Iteration 2 remediations, checked against the sources

1. Danfoss Exposure (Belgium/Netherlands): CORRECT. Infosecurity: "Supermarkets in Belgium and the Netherlands were also reportedly affected." The entry says Infosecurity reports this without naming them, and that no source names a Swiss deployment; Albert Heijn is only listed as contacted, so "without naming them" holds.
2. Registry incident summary: CORRECT. Defrost attributed to BFMTV ("which BFMTV reports as a remotely forced defrost"), compromises to CERT-FR, confirmation to AFP; the two `affects` relation notes match AFP ("its AK-SM800 and AK-SC355 fridge regulator systems were notably affected").
3. Danfoss body/Triage conditional: CORRECT. BFMTV: "les pirates auraient détourné cette fonction en imposant un dégivrage forcé et continu, avec une consigne de température fixée à 50 degrés"; the entry carries "said to have" and "writing in the conditional". (The "older than version 4" scope is stated flatly by BFMTV, so the hedge over-covers it; harmless.)
4. Takeaway scope "may have been taken over": CORRECT. CERT-FR lists the factory-reset/rotate sequence under "En cas de suspicion de compromission".
5. Store counts: CORRECT for the Intermarché figure. BFMTV: "Un bilan deux fois plus élevé que les premières estimations, qui faisaient état de 150 points de vente"; Infosecurity quotes 150. Coopérative U (AFP "over 100", BFMTV "moins d'une centaine") is carried as a visible discrepancy.
6. MikroTik CISA date: still 2026-09-30 against the page's "Initial Release Date: 2026-09-29" (advisory only, restated below).
7. MikroTik / SonicWall narration: fixed in those two entries. The same pattern remains in the Publica improvement section (below).
8. Run-record placeholder: gone; the replacement text carries two stale statements (F4 below).

Main-analysis trim of the Danfoss entry (269-word main paragraph, 548 words total): no claim lost its support; every sentence still has its citation and every fact re-checks against AFP, BFMTV, CERT-FR, Infosecurity and BleepingComputer.

### Unsupported / hallucinated facts

- F4 #1 (low confidence) — run record, Verification & coverage notes. "Iteration 2 (truth 4, advisory 4) found ... all were fixed." The record's own iteration 2 findings list the MikroTik CISA-date F11 as "declined". And: "(3) Danfoss: ... the entry carries AFP's figure and says counts differ by outlet." The entry now says "Counts moved during the day" (BFMTV's 300 is twice the first estimate of 150 that Infosecurity quotes). Fix the two sentences; the notes are restamped in Phase 6 anyway.

### Editorial / less-is-more flags (advisory)

- F11 #2 (low confidence) — Danfoss first body sentence: "...overnight on 11 to 12 October 2026, which reports from the retailers' statements at least 300 Intermarché or Netto shops ..." — the relative pronoun has no antecedent that can report; AFP is the reporter. Reword.
- F11 #3 (low confidence) — Danfoss sourcing_note: "...BFMTV's reporting and no other source states them." Infosecurity repeats the 50 °C figure (quoting BFMTV), AFP relays BFMTV's forced defrost, BleepingComputer states the defrost in its own voice. Say "no other source reports them independently".
- F11 #4 (low confidence) — Publica Improvement section and record summary: "lists more data classes than the entry carried" / "which the entry lacked" narrates the entry's own history (the pattern iteration 2 fixed elsewhere).
- F11 #5 (low confidence, carried and declined last round) — MikroTik CISA citation dated 2026-09-30; the page says Initial Release 2026-09-29.

### Verified without findings

- GitLab (CVE-2026-97229): GitLab 19.4.2 page confirms the integer overflow in the CI/CD regular-expression compiler, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H = 10.0, affected "19.2 before 19.2.8, 19.3 before 19.3.5, and 19.4 before 19.4.2", 19.3.4 merge-request bug, 90-day issue disclosure, single-node downtime, no workaround section. CERT-EU and BleepingComputer do give 19.3.4. NCSC post 13051: exploitation status UNKNOWN, prerequisite quote verbatim. 19.4.1 page: CVE-2026-89078 (double free, regex parser) and CVE-2026-93577 (integer overflow, regex compiler), both "authenticated user", reporter joaxcar. No overlap with the store (cves_seen, prior_coverage).
- MikroTik: 7.23.8 changelog (2026-10-08) and the 6.49.23 forum post (changelog 2026-10-07) both carry "system - improve stability (includes CVE-2026-84411);"; the vendor notice, re-read live, still reads "v7 long-term - release pending" and "v6 long-term - release pending". Correction record fields match the diff; `updated_at` stays null.
- SonicWall: NCSC post 13034 history shows the 2026-10-12 edit "updated with Active exploitation claims" with Defused "since oct. 8th" and Previdian "since oct. 9th"; SecurityWeek, The Hacker News (135 attempts, two US addresses, both operators dated to 8 October) and Previdian's own page (first observed 09 Oct) agree with the section; SonicWall PSIRT read 2026-10-13 still says no evidence. CVE status correctly stays patch-available. Priority `high` is defensible (attempts against decoys only, vendor denies evidence).
- Publica: Publica's own page (Stand 08.10.2026) lists Zivilstand, partner details and IBAN and "vermutlich Personendaten ... abgeflossen"; cash.ch (AWP) carries "eher kleine Datenmenge" and "Geschäftsdaten" without a named speaker; all body citations re-check against admin.ch, PK Softech, watson, Netzwoche, BPK, BLVK, Pensionskasse Post.
- Danfoss: CERT-FR page dates (first and last version 12 octobre 2026), both evidence quotes verbatim with faithful translations; AFP, BFMTV, Infosecurity and BleepingComputer dates 2026-10-12. Classification A/2, priority high and `actions[]` (one task, not duplicating the Claroty entry's firmware-upgrade action) hold; Swiss-nexus limit stated in Exposure.
- Missed angles: none found. Patch Tuesday of 2026-10-13 is acknowledged as unpublished at fire time and queued for the next fire; the live KEV catalogue shows no addition since 2026-10-08; NCSC Security Hub's newest posts are the two entries' advisories.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 4). The single truth-class item is a pair of stale disposition statements in the run-record notes; every entry and the registry record verify clean against their sources.

### Findings summary (machine-readable)

See `work/2026-10-13T0256Z-intel/verification.iter3.findings.yaml` (5 records).
