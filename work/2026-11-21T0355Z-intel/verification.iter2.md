**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-21T05:12:30Z · ended_at=2026-11-21T05:32:38Z · duration_seconds=1208

## Verification report — 2026-11-21T0355Z-intel (iteration 2)

Scope: post-fix pass. All 194 ledger claims have a verdict row in `verification.iter2.claims.yaml` (the 27 changed claims, every other claim of the ten remediated entries, and also all of Roller and nginx, not a quarter). Six new entries, six updated entries (diffs read with `git diff HEAD`), the run record. Pages fetched live this iteration: Danfoss DSA-2026-12-01/-02, BSI PDF (pdf transport plus `pdftotext` on the WebFetch copy for page 1), CERT-FR, NCSC.ch hub posts 13054/13198/13203, French MFA, Midnight Blue, CCB, AFP/Khaleej Times, BleepingComputer, heise, SRF, BACS (two pages), Le Monde, ACN, BFMTV, all four Cisco advisories (Expressway, voice hardening, Snort 3, Expressway hardening) plus the Java4Shell and nginx ones, F6 (Russian), CISA KEV alert and CISA Java alert (WebFetch), Calif (raw HTML), Oracle, OpenJDK, Tenable, Talos, Upwind, Equixly, Fortinet (two), Siemens (three), Broadcom VMSA-2026-0009.1, SAP bulletin, ENISA EUVD, Basel FAQ, Polizeiticker, Inside IT, the three Hokkaido notices and ITmedia (Japanese), CdT interview, laRegione, Ticinonline, Rapid7 (two), ESET, Arctic Wolf, Apache oss-security (two), BleepingComputer Roller, Roller downloads, Xint, nginx.org, CERT-EU, CERT.at, NCSC-NL, Wiz, PAN-OS, the Rapid7 PoC README.

### Prior-iteration findings: remediation check

1. SAP (F3): fixed. CISA's alert row reads "CVE-2025-42884 SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability"; the body now says "naming SAP NetWeaver" and attributes Enterprise Portal / EP-BASIS / EP-RUNTIME 7.50 to SAP's bulletin (row 3660969, Medium, 6.5) and ENISA.
2. EVTX (F4): fixed. Arctic Wolf: allocated records 2,635,913 to 2,636,016, free-space records 2,635,767 and 2,635,218; "lower record identifiers" is right.
3. Danfoss BSI (F3): partly fixed. Summary, analysis and takeaway now follow BITS-H 2026-306525-11e2 v1.1 of 2026-11-17 ("aktive Ausnutzungsversuche ... CVE-2026-124014 und CVE-2026-124010", "Geräte offline genommen werden", "alle Zugangsdaten gewechselt werden"). Two residuals still rest on version 1.0 text the URL no longer serves: an `evidence[]` quote (F4 #1) and the 2026-11-14 section (F3 #2).
4. Danfoss opening sentence: fixed. AFP page: "PUBLISHED: Mon 12 Oct 2026 ... confirmed to AFP they suffered a cyberattack".
5. Webworm: fixed. Rapid7: "this is the easiest change for the threat actor to implement next. Similarly, the HTTP endpoints and watermark can be swapped out trivially."
6. Cisco "first case": fixed. F6 headline "зафиксировала первый случай эксплуатации".
7. USI "because": removed; section is two sentences; the three clauses match the interview (names, e-mails, phones, "in minima parte" applications; event management and participation confirmations; 8000 e-mails). One residual on the count unit (F14 #5).
8. Basel / USI length: Basel narrative is two sentences with the nexus clause first; USI update is two sentences; no sourced fact from the summary or evidence was lost. Residual advisory on Basel's Exposure line (F11 A1).
9. Hokkaido: `priority: routine`; the uncited Swiss analogy is gone, replaced by "This is municipal public-sector data held through a supplier chain.", a plain nexus clause derivable from the three municipal notices.
10. SAP verification: `single-source-national-cert`, CISA first in `sources[]`: correct.
11. Webworm `references[]`: `2026-05-21/webworm-china-aligned-shifts-to-eu-government-targets-echocr` exists and is listed.
12. Narration: the Cisco, Java4Shell and Danfoss record summaries now state the delta; "as of 2026-11-21" in the Cisco body; the Danfoss 11-11 section is past tense ("At that date no CVE identifiers existed yet").
13. wombat@127.0.0.1: judgment is that it holds. F6 files it under its indicator list, but it is one protocol-level log marker (an Erlang node name in erlang.log) that is the only discriminator for a successful exploit, not an address, hash, domain or sample indicator; it carries the post-patch compromise check the actionability contract asks for. No finding.
14. vCenter `cisa-kev`: supported. CISA's alert of 2026-11-20 lists "CVE-2026-123890 VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability". The record is `type: improvement`, `internal: true`, fields [cves, tags], no body section, `updated_at` still null: correct under 4c. The five `cves[]` rows also match Broadcom VMSA-2026-0009.1 (updated 2026-11-20 to clarify the Tools versions; CVSS, fixed builds, Tools 13.1.5.0 / 12.5.5 / 12.4.10 for 32-bit). Residual advisory: no listed source carries the KEV fact (F11 A2).

### Unsupported / hallucinated facts

- **F4 #1 — Danfoss entry, `evidence[]` BSI quote.** `Nothing is known about active exploitation of the vulnerabilities found. (translated from German)`, original `Über eine bereits aktive Ausnutzung der gefundenen Schwachstellen ist nichts bekannt.`, attributed to `…/2026-306525-1032.pdf?__blob=publicationFile&v=2`. The page now is v1.1 ("BITS-H # 2026-306525-11e2 | Version 1.1 vom 17.11.2026", `Kritikalität*: 2 / Gelb`, `Gefährdung: Aktive Ausnutzung`); the full text (tool and `pdftotext`) has no "nichts bekannt". The quote is not a substring of the cited page. Drop it, or replace with the v1.1 exploitation-attempts sentence.
- **F4 #4 — Cisco entry, `techniques[]` T1210 (low confidence).** F6: "затем через одно из них получили доступ к двум другим узлам кластера" gives no mechanism for the lateral step; exploitation of a remote service is an inference. T1190 covers the stated exploitation.

### Citation does not support the claim

- **F3 #2 — Danfoss entry, 2026-11-14 section (low confidence).** "BSI's notice of 2026-11-13, criticality 3 (Orange), lists no fixed version, says nothing is known about active exploitation" cites the same PDF URL, which now reads criticality "2 / Gelb", overview "Aktive Ausnutzung", and carries no no-exploitation sentence. The clause was true of version 1.0; it should say so (version 1.0, replaced by 1.1) or be corrected.

### Analytical-link-as-fact

- **F13 #3 — Cisco entry (low confidence), four places.** summary: "F6 reports that attackers used a public proof of concept against two internet-reachable X15.5.3 devices"; actions[0]: "F6 saw a public proof of concept used against two internet-reachable nodes"; Defender takeaway: "F6 saw a public proof of concept used against internet-reachable nodes"; record summary: "F6 reports a public proof of concept used against two internet-reachable Expressway X15.5.3 devices". F6: "Вскоре после появления общедоступного эксплойта (PoC) злоумышленники успешно атаковали устройства Cisco Expressway X15.5.3". That is sequence, not use of that PoC; the Update section and the evidence quote word it correctly. The run-record note ("an F6-investigated intrusion through a public proof of concept") repeats it.

### Quantifier without source

- **F14 #5 — USI entry (low confidence).** headline "more than 8,000 people warned", title "contact details of more than 8,000 people who were warned", section and record summary "more than 8,000 people were warned". Source: "Abbiamo inviato oltre 8000 e-mail per avvertire le persone interessate dal furto di dati": e-mails, not people. The entry's own summary says "e-mails" correctly.

### Editorial / less-is-more flags (advisory)

- **F11 A1 — Basel-Landschaft (low confidence).** Narrative is two sentences, but Exposure (two sentences) and a long Defender takeaway remain on a routine incident with no vector, actor or behaviour. Optional trim.
- **F11 A2 — vCenter.** `cisa-kev` in `cves[].status` and tags is true but no source in `sources[]` carries it; add the CISA alert (and `sources` in the record's fields).
- **F11 A3 — Danfoss record summary (low confidence).** It states the BSI v1.1 point; the 2026-11-21 section does not (it sits in the main analysis only).
- **F11 A4 — Java4Shell 2026-11-21 section (low confidence).** "the earlier statements ... no longer hold" points at text that was rewritten in the 2026-11-19 section, which now says the same v1.3 facts; state the delta once.
- **F11 A5 — run record note (low confidence).** "did not grow Java4Shell": body 1,044 to 1,179 words (+135); only the analysis block stayed (546 to 548). Danfoss analysis 547 to 544, body 5,083 to 5,249, 18 records: holds.
- **F11 A6 — Hokkaido (low confidence).** Six per-municipality record counts on a routine entry; one clause would do.

### Checks with no finding

- Changelog contract (4c): every updated entry's last record carries this run's id; non-internal records have the matching `## Update — <at>` section and `updated_at` equal to `at`; the vCenter internal record has no section and `updated_at: null`; `git diff HEAD` shows no change outside the declared `fields` (Cisco, nginx, Java4Shell, Danfoss, USI, vCenter). Supersession: Cisco body, headline, summary and actions now agree with the KEV listing and F6; Java4Shell's Cisco statements agree with v1.3; the Danfoss summary and analysis no longer say "no CVE" or "no known exploitation".
- New entries: Roller (Apache announcements of 2026-11-17 and 2026-09-25, CVSS 9.8, 4.0.0 through 6.1.4 / 6.1.5, 6.1.6 or later, 6.1.7 best available, same flaw as CVE-2026-82384), SAP (SAP bulletin row, ENISA, CISA), Basel (FAQ, Polizeiticker, Inside IT), Hokkaido (three municipal notices and ITmedia read in Japanese), Webworm (Rapid7, ESET), EVTX (Arctic Wolf, 44 records / 1 allocated, 104 events, lower identifiers): every clause checked against the page it cites.
- CVE ids and scores against per-CVE authorities: Danfoss DSA-2026-12-01/-02, Cisco (four advisories), Oracle/OpenJDK, Broadcom, Apache, SAP, PAN-OS. All match. No CVE in this run appears in `state/cves_seen.json` or earlier entries outside its own entry.
- Registry keys for the new incident, malware, product and actor entities exist; `techniques[]` ids exist in the pinned ATT&CK data and map to stated behaviours (apart from F4 #4).
- Priorities: Cisco high (KEV plus an F6 root intrusion, upgrade decision within days), no critical, SAP and Roller notable, Hokkaido and Basel routine: calibrated. Classification blocks present on all six new entries; Admiralty values consistent with the sources.
- Style: no em dash outside `## Update — <at>` headings, no hash, address or attacker domain, no workflow vocabulary in reader-facing fields of the twelve entries.
- Coverage: all four KEV additions (SAP, Cisco, vCenter, Roller) have a disposition; two web searches (Swiss municipal and cantonal incidents, KEV additions of 2026-11-20) found no in-window item the run missed (the search index does not reach the window). No F10.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 0, advisory: 6)

Truth: F4 x2 (#1, #4), F3 x1 (#2), F13 x1 (#3), F14 x1 (#5). Only #1 is firm: the quote is demonstrably absent from the page as it now stands. #2, #3, #4 and #5 are low confidence; the fixes are small wording edits. Advisory items A1 to A6 may be left.

### Findings summary (machine-readable)

See `work/2026-11-21T0355Z-intel/verification.iter2.findings.yaml` (11 records).
