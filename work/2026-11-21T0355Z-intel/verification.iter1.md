**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-21T04:53:03Z · ended_at=2026-11-21T05:08:36Z · duration_seconds=933

## Verification report — 2026-11-21T0355Z-intel (iteration 1)

Scope: 190 claims (full ledger, all rows in `verification.iter1.claims.yaml`), 6 new entries, 5 updated entries (diffs read with `git diff HEAD`), run record. First pass, cold read. CISA alert read through `WebFetch` (outbound-links template); Cisco, Siemens (raw HTML for the product tables), PAN, Fortinet, Calif (raw HTML, the extract drops the write-up), BACS, CCB, BSI (PDF), NCSC.ch hub posts, NCSC-NL and Danfoss pages re-fetched live this iteration; the other pages read from the gate's saved bodies.

### Citation does not support the claim

- **F3 #1 — SAP entry, CISA clause.** `2026-11-21/sap-netweaver-enterprise-portal-cve-2025-42884-kev`: "CISA added CVE-2025-42884 to its Known Exploited Vulnerabilities catalog on 2026-11-20, naming SAP NetWeaver Enterprise Portal". CISA's alert reads "CVE-2025-42884 SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability": it names SAP NetWeaver, not Enterprise Portal. The component comes from SAP's bulletin and ENISA, not from the clause's citation.
- **F3 #2 — Danfoss entry, BSI clause (touched by this fire).** Summary "with no known exploitation (BSI)" and body "BSI knows of no active exploitation (translated from German) ([BSI, 2026-11-13](…2026-306525-1032.pdf…))". The PDF at that URL now reads "BITS-H # 2026-306525-11e2 | Version 1.1 vom 17.11.2026", overview "Gefährdung: Aktive Ausnutzung", criticality "2 / Gelb"; the exploitation text concerns Copeland XWEB EVO ("registrierten Sensoren bereits aktive Ausnutzungsversuche … CVE-2026-124014 und CVE-2026-124010"), and it states nothing about exploitation of the AK-SM 800A. The "none known" wording belonged to the 13 November version. Re-read v1.1 and attribute accordingly (or state v1.1's position).
- **F3 #3 — Danfoss entry, opening sentence (pre-existing, low confidence).** "Leclerc confirmed to AFP a cyberattack on their refrigeration systems overnight on 11 to 12 October 2026 ([AFP, 2026-10-12])". The AFP page says the chains "on Monday said they were hit"; "overnight"/"11 to 12 October" is the French foreign ministry's wording; E. Leclerc said a refrigeration supplier was affected.
- **F3 #4 — Webworm entry (low confidence).** "Rapid7 expects the branding, endpoints and watermark to be swapped out next". Rapid7: branding "is the easiest change for the threat actor to implement next. Similarly, the HTTP endpoints and watermark can be swapped out trivially."

### Unsupported / hallucinated facts

- **F4 #5 — EVTX entry, Detection line.** "carve its first chunk for records with earlier timestamps and higher record identifiers than the allocated ones". Arctic Wolf: allocated records "identifier 2,635,913" (first) to "2,636,016" (last); free-space records "Identifier 2,635,767" and "Identifier 2,635,218". The surviving records have lower identifiers. Replace "higher" with "lower" or drop the id clause.

### Analytical-link-as-fact

- **F13 #6 — USI update (low confidence).** "only to a minimal extent job applications or scholarship requests, because the affected forms software also serves event management and participation confirmations". The COO lists the data types and separately says the software is also used for events; he does not connect them causally.

### Quantifier without source

- **F14 #7 — Cisco update (low confidence).** "The one public case is F6's". No cited source says only one public case exists; F6 headlines "первый случай" (first case).

### Drop (low relevance / off-audience / duplicate)

- **F7 #8 — Basel-Landschaft (and the USI update).** Run record: published "at routine under the incident floor (no vector, actor or behaviour beyond the theft)". `prompts/cti-run.md` Phase 4 incident floor: such an incident is "routine and at most two sentences plus its transfer ground, or it is dropped". The Basel entry has a five-sentence paragraph, an Exposure line and a Defender takeaway; the USI update adds three long sentences to a routine entry with the same shape. Cut to two sentences plus the nexus clause and one concrete takeaway.

### Single-source items missing [SINGLE-SOURCE] flag

- **F12 #9 — SAP entry (low confidence).** `verification: single-source` with three listed sources (SAP bulletin, CISA, ENISA). The single-sourced element is exploitation, resting on CISA's own KEV listing, a carve-out authority for its own catalogue: set `single-source-national-cert` (the sourcing_note already explains) or `multi-source`.

### Org-triage line missing / inconsistent

- **F16 #10 — Hokkaido priority (low confidence).** `priority: notable` for an out-of-region municipal incident with no confirmed exfiltration; the stated ground is an uncited analogy ("the same shape as a Swiss supplier retaining administration data"), which is none of the four out-of-nexus grounds. `routine` fits the cited facts.

### Editorial / less-is-more flags (advisory)

- **F11 #11 — Webworm `references[]` (low confidence).** `2026-05-21/webworm-china-aligned-shifts-to-eu-government-targets-echocr` covers the same actor and the SoftEther shift; link it as the earlier entry.
- **F11 #12 — narration in reader-facing text.** Cisco body "when read on 2026-11-21" (say "as of"); changelog summaries that describe the editing rather than the delta: Cisco "The entry now reads as exploited, moves to high, and carries F6's log marker and the post-upgrade compromise check", Java4Shell "the Cisco statements elsewhere in the entry are corrected to match", Danfoss "the summary and the main analysis no longer say no identifier exists". Low-confidence extra: the Danfoss 2026-11-11 section still says "No CVE identifiers exist yet" in the present tense below the new 2026-11-21 section.
- **F11 #13 — Cisco literal indicator (low confidence).** "nodeup record for a node named wombat@127.0.0.1" is a fixed attacker-side string, functionally a mutex-style indicator against the zero-IOC rule; F6 publishes it as its key marker, so the main agent may keep it.
- **F11 #14 — vCenter `cves[].status` (low confidence).** `2026-11-20/vmware-vcenter-cve-2026-123890-auth-bypass-exploited-gtig` lacks `cisa-kev` although CISA listed it in the same 2026-11-20 alert; the Roller, SAP and Cisco entries carry it. An internal record would align it.

### Checks with no finding (for the main agent's orientation, not defects)

- Updated-entry contract (4c): every updated entry's last record carries this run's id, `updated_at` equals the record `at`, each has a matching `## Update — <at>` section, `git diff` shows no silent change beyond `fields` (Cisco, nginx, Java4Shell, Danfoss, USI). Sections cite genuine deltas: Cisco KEV + F6; PAN-OS builds and ETA, Cisco v1.0 table, Siemens SSA-935812, Fortinet FG-IR-26-279; Cisco v1.3 and Siemens SSA-810379/SSA-272816; Danfoss DSA-2026-12-01/-02; USI interview. Supersession: Cisco body no longer says "no exploitation" unqualified; Java4Shell's earlier Cisco sentences were rewritten to v1.3.
- CVE ids and scores against per-CVE authorities: Roller (Apache announcements), SAP (SAP bulletin row, ENISA), Cisco (four advisories incl. the Snort 3 9.0/AC:H and Unified CM 9.8 rows), Danfoss (both DSAs), Java4Shell (Oracle table), nginx (PAN, Cisco, Siemens, CERT.at). All match.
- Run record notes: counts, dispositions, KEV sweep, backlog strikes, entities_added (11) and the Danfoss 18 records / ~5,000 words hold on disk.
- Coverage: all four KEV additions have a disposition; no in-window item surfaced by my searches that the run missed (the search index does not reach the window; nothing evidenced, so no F10).

### Verdict

NEEDS_FIXES (truth: 7, editorial: 3, advisory: 4)

Truth count: F3 x4 (#1-#4), F4 x1 (#5), F13 x1 (#6), F14 x1 (#7). Editorial: F7, F12, F16. Advisory: F11 x4. The three findings the main agent should treat as definite: #1 (SAP product naming), #2 (BSI now at v1.1, clause rewritten this fire), #5 (EVTX id direction); #3, #4, #6, #7 and the editorial ones are marked low confidence where the evidence is interpretive.

### Findings summary (machine-readable)

See `work/2026-11-21T0355Z-intel/verification.iter1.findings.yaml` (14 records).
