**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-19T05:13:20Z · ended_at=2026-07-19T05:20:39Z · duration_seconds=439

## Verification report — 2026-07-19T0408Z-intel (iteration 4)

### Iteration-3 fix verification (Poland-as-government inversion)

CONFIRMED FIXED, no residual anywhere in currently-published material. Searched all three entry
files, `entities/registry.yaml`, and the run record's frontmatter + prose notes for "Poland":

- Entry `ancpi-romania-cadastre-cyberattack-bytetobreach.md` body: "a bank in Poland among the
  organizations that acknowledged their breaches" — matches KELA verbatim ("such as a bank in
  Poland, acknowledging the breaches").
- `entities/registry.yaml` `actor:bytetobreach`: "KELA names a bank in Poland among the
  organizations that acknowledged their breaches, and Romania's ANCPI cadastre agency is the
  government registry hit in July 2026" — correctly separates the two.
- Run record § Verification & coverage notes, "Published" bullet: "tracked data-leak operator
  ByteToBreach with a documented cross-country victimology spanning government, banking and other
  sectors (KELA)" — no Poland-as-government claim; Poland is not named at all in this line, which
  is the correct, safe framing.
- The only remaining "Poland" + old-inversion-text hits are inside `verification.iterN.md` /
  `verification.iterN.findings.yaml` historical finding records under `work/`, which the spawn
  message explicitly says are intentionally unchanged (they document history, not current claims).

No residual. This class of defect (Poland mischaracterised as a government victim) is fully closed.

### Fresh cold-read verification performed this iteration

Re-fetched and cross-checked, independent of prior iterations' notes:

- KELA blog (`kelacyber.com/blog/bytetobreach-...`) — confirmed victimology quote, Poland-as-bank
  quote, and initial-access tradecraft quote all verbatim-consistent with the ANCPI entry's evidence
  and body prose.
- Public Record (`publicrecord.ro/2026/07/17/atac-cibernetic-ancpi/`, Romanian) — confirmed the
  ~1.5M-lei contract's 24/7 call-centre and annual-audit requirements, the vendor owner's "eMAG
  licence" self-characterisation, the ANAR December 2025 attack (~1,000 systems), and the backup-
  deletion claim, all verbatim-consistent with the entry.
- Help Net Security — confirmed both evidence quotes (systems down since 14 July; ByteToBreach's
  theft/GitLab/ransomware claim; ANCPI's data-not-compromised statement) verbatim.
- California OAG breach-notification page + the linked PDF notice letter itself (`EY Notice Letter
  US General.pdf`, read directly) — confirmed the March 28 / April 23 date fields, the "financial
  information contained in or used to prepare tax filings" data-type language (no SSN/payment-card
  specifics — the iteration-2 fix holds), and that the letter itself redacts `[DATA ELEMENTS]`. Also
  confirmed `article:published_time` metadata on the OAG page is 2026-07-15T15:51:01-07:00, matching
  the entry's "filed... on 2026-07-15" despite the letter template being dated July 13 — not a
  discrepancy (OAG publication date vs. letter template date are different, both legitimate).
- BleepingComputer + CyberInsider (EY) — confirmed the March 28–April 12 access window, April 23
  detection date, and the "personal information as well as certain financial information contained
  in or used to prepare tax filings" data-type framing; the Atlassian/ServiceNow mentions in
  BleepingComputer are unconfirmed reader-comment speculation, not something the entry repeats.
- Group-IB ClickLock blog (fetched via jina reader after a 503 on direct WebFetch) — confirmed all
  four evidence[] quotes verbatim, including the exact "pkill or killall... no legitimate use case"
  detection line. Confirmed the "Infrastructure" section's explicit statement "No dedicated
  command-and-control infrastructure was observed" — this directly supports the entry's parenthetical
  "(Group-IB observed no dedicated command-and-control infrastructure...)", validating the
  iteration-2/3 remediation of the Telegram/C2 wording.
- BleepingComputer + Forbes (ClickLock) — confirmed the 100-victims/33-countries/83-hour claims and
  the GSocket-persists-while-others-self-delete detail; no contradictions with Group-IB.
- ATT&CK cross-check: all 25 distinct technique ids used across the three entries (including T1685
  "Disable or Modify Tools", used for the anti-investigation kill-loop and NotificationCenter
  suppression) resolve to active, non-deprecated, non-revoked techniques in the pinned
  `attack/enterprise-attack.json`; each maps to a behavior the body actually describes.
- Classification codes: ClickLock (B/2 — Group-IB sole originating research, re-reported not
  independently corroborated) matches sources.json's own B rating for group-ib and the credibility-2
  criterion exactly. EY (A/2 — first-party regulatory filing, undisclosed scope) is correct. ANCPI
  (B/2) blends a C-rated primary (Help Net Security) with a B-rated corroborating research source
  (KELA) plus an uncatalogued investigative outlet (Public Record); this is a defensible multi-source
  blend, not a "letter well above the source's own rating" violation — not flagged.
- No IOCs (hashes, IPs, domains) appear in any of the three entries, despite the Group-IB source
  containing several (panalobet[.]ph, store.grafsynergy[.]com, gsnc[.]eu) — correctly excluded per
  pipeline policy.
- `actions[]` empty on all three entries — correct per the do-now bar; nothing here clears it.
- Entity/registry linkage, `event_date` fields, and `verification: multi-source` values all check out
  against the sources fetched this iteration.

No new truth or editorial defects found.

### Verdict

CLEAN

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
[]
```
