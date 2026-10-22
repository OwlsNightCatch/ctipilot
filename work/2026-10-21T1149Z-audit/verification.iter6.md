**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T08:29:01Z · ended_at=2026-10-22T09:02:47Z · duration_seconds=2026

## Verification report — 2026-10-21T1149Z-audit (iteration 6)

Role: post-fix pass after iteration 5's NEEDS_FIXES. Scope: every claim row of `claims.iter6.yaml` has a verdict row (278 of 278: 275 ok, 3 unreadable; `claim_ledger.py --coverage 6` reports 0 missing). Read in full against pages fetched this iteration: the 3 claims changed since iteration 5, every YellowKey claim (37) and every Nightmare Eclipse claim (25), a seeded random 54 of the remaining 216 (seed 20261022), and the wave report, run record, tracker, registry, `cves_seen` and legacy-queue statements against disk. The other 162 claims were each checked against the staged page text with one supporting passage (every passage in the claims file was machine-checked as a substring of the page text, or is an explicit absence note). `check_run.py 2026-10-21T1149Z-audit`: 59 pass, 0 warn, 0 fail.

### Prior-iteration deltas (each fix checked against its source this iteration)

- **F4, wave report residual bullet and Dirty Frag row.** Dirty Frag `references:` holds `2026-05-09/cve-2026-31431-copy-fail-...`; its 2026-10-21 record and section name the Defender Security Research Team credit, the EPSS refresh and the link; `updates[]` record says "Red Hat's 'Copy Fail 2' nickname is dropped from the main analysis"; RHSB-2026-003 does say "Dirty Frag is also referred to as \"Copy Fail 2\"" (the 2026-09-05 section still carries it, as dated history). EPSS API: 0.94194 / 0.02617 (2026-10-20), 0.93235 / 0.92855 (2026-09-04). The row is accurate. The bullet's word "resolved" is covered by advisory #3 below.
- **F3, TPM-only Exposure lines.** YellowKey: "TPM-only BitLocker devices" is cited to BleepingComputer, whose page says the exploit "allows access to disks that are protected with TPM-only BitLocker without needing credentials"; "physical access" and the fixed builds are cited to MSRC, whose OData record gives the physical attack, `exploited: No`, and the five-product table (24H2, 25H2, 26H1, Server 2025, Server 2025 Core; no Server 2022) with fixed builds 10.0.26100.8655, 10.0.26200.8655, 10.0.28000.2269, 10.0.26100.32995. Nightmare Eclipse: "a BitLocker device not protected by TPM+PIN" cited to MSRC; MSRC's FAQ says "if you are using TPM+PIN the vulnerability is not exploitable", and "needs ... not protected by TPM+PIN" is the contrapositive of that statement. Both clauses hold on their pages.
- **F4, W4-05 row.** `twin-scan/candidates.json` (104) plus `candidates2.json` (16) give 118 unique pairs (2 overlap). Copy Fail / Dirty Frag share the Microsoft Dirty Frag post, Dirty Frag / Fragnesia share RHSB-2026-003 and the Aikido post, Cisco FMC / ISE share `cisco-sa-notice-jfxk98zp`, Check Point 2026-09-10 / 09-18 share a The Hacker News article; the pass-1 remainder shares CISA KEV JSON, NCSC-NL, CERT-Bund and nginx.org listing URLs (one pair, Qilin and The Gentlemen entries of 2026-09-21, shares a specific Talos post but covers distinct actors). Fragnesia's `references[]` is empty and the entry is unmodified; `plan.json` carries W4-11 (wave 12, open) for it.
- **F11, Verdict count.** "five twin pairs ... (four from the scan, one found in repair)" matches W4-06 to W4-09 (scan) and W4-10 (repair); W4-11 is the link row. The Tracker delta names W4-06 to W4-11, and `plan.json` wave 12 lists W4-07 to W4-11 (W4-06 is wave 08).

### Editorial / less-is-more flags (advisory)

All six are F11, none blocks publication; each is marked low confidence or pre-existing.

1. **F11 (pre-existing, low confidence), YellowKey, 2026-05-20 section.** "disclosed by \"Nightmare Eclipse\" on 2026-05-12" has no inline citation and no cited source states that date (BleepingComputer dated 2026-05-13 gives none; The Register, published 2026-05-13T16:16Z, says "dropping them just after Microsoft's monthly Patch Tuesday update"; NCSC-CH #12574 created 2026-05-14). Unchanged by this fire.
2. **F11 (pre-existing, low confidence), Japan GSS, paragraph 1.** "no general citizen data, only GSS-using-agency staff, associated public servants, and contracted businesses" cites Rocket Boys; that page and the Digital Agency notice name "事業者及び個人" (businesses and individuals, about 57,000 records), and the entry's own 2026-10-21 section says "the businesses and individuals involved". Only the em dash changed in this sentence this fire.
3. **F11 (low confidence), wave report, residuals bullet.** "that Copy Fail and Dirty Frag did not reference each other, was resolved ... Dirty Frag now lists Copy Fail." repair-1.md states the residual as "neither lists the other"; the Copy Fail entry's `references[]` still names only the WP2Shell entry. Iteration 5 advised rewording to the reverse direction. Defensible under the report's newer-to-older link convention; say so or name the reverse direction.
4. **F11 (low confidence), tracker totals.** Measure "Known duplicate groups open (W4)" reads "open: W4-02, W4-06 to W4-10" while W4-11 is a W4 row with status open (same wave-12 row set as W4-10).
5. **F11 (low confidence), run record iteration 1 block.** SimpleHelp critical and Dirty Frag high are "carried forward for calibration", but neither the report's carry-forward section nor any tracker row names them.
6. **F11 (low confidence), SimpleHelp, three CCB-only claims.** `ccb.belgium.be` is unreadable on every rung (extract and url fall to jina and return the 503 maintenance page; WebFetch returns HTTP 403), so claims 67a2cb0628, b3d0654cb8 and 1b7635154c are `unreadable`. No defect asserted: the NVD API (VulnCheck CNA, cross-check only) gives CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, 10.0, and the repair worker's saved copy reads "CVSS 10 (CVSS:3.1/...)".

### Checks that found nothing (for the record)

- YellowKey and Nightmare Eclipse: every clause matches its page. The three changed claims hold. Frontmatter `cves[]` (6.8 and 7.8, fixed builds, `exploited: No`), `techniques[]` (all ids active in the pinned ATT&CK v20: T1059.003, T1005, T1068, T1685), evidence quotes (verbatim in BleepingComputer, MSRC, The Record, heise, the MSRC blog), `updated_at` equal to the `update` record's `at`, `fields` lists covering the diff, and no em dash, IOC or workflow vocabulary in the added reader text.
- Wave report: counts (23 records = 2 updates, 6 corrections of which one internal, 15 improvements of which one internal; 21 W1-D + Pwn2Own + Adobe), 366 defects on 33 entries, 30 of 33 carrying a 2026-10-11 record, 12 entries without a record (names match), four legacy entries now `reviewed` (402 pending), `cves_seen` (seven `last_seen`, four titles), registry (two summaries, five new product keys, eight earlier `first_seen`), 581 entries without `updates:` at HEAD, claim and re-claim commits, budget.tsv cuts, the RoguePlanet lead (MSRC lists CVE-2026-50507 as a BitLocker bypass), W4-01 to W4-05 outcomes against the entries on disk.
- Run record: durations equal the stamps for T1, repair-1 to repair-5 and iterations 1 to 5; iteration claim counts equal the claims files (266, 155, 157, 145, 277); finding tallies equal the findings files; no fold residue (`merged_from` only; no relation with a missing source entry).
- Entries: classification present on all 23 (A to B, 1 to 2), no `org_triage`, no watchlist flag; `actions[]` at most one concrete task; Adobe's em dash in title and headline is pre-existing and its record is internal.

### Process note

I ran `python3 work/cleanup/render_status.py` once while checking the tracker totals; it rewrites `docs/cleanup/STATUS.md` from `plan.json`. The `git diff HEAD` of that file read before and after the run is identical line for line (1001 entries, 402 pending, 58 rows, 29 / 2 / 7 / 20), so the file is unchanged in content. No other repository file outside `work/2026-10-21T1149Z-audit/verification.iter6.*` and `verify.iter6.*` was written.

### Verdict

CLEAN

Counts: truth=0, editorial=0, advisory=6. No truth or editorial defect remains in the 278 claims, the entries, the wave report or the run record; the six items above are F11 advisories the main agent may leave or fix with a one-line edit each.

### Findings summary (machine-readable)

```yaml
- code: F11
  category: editorial-advisory
  section: 2026-05-15/windows-bitlocker-yellowkey-and-ctfmon-greenplasma-zero-days (## Update 2026-05-20T05:00:11Z)
  item: YellowKey and GreenPlasma, 2026-05-20 section, first sentence
  url_or_quote: disclosed by "Nightmare Eclipse" on 2026-05-12
  summary: '(pre-existing, low confidence) The sentence carries no inline citation and no cited source states a 2026-05-12 drop date: BleepingComputer is dated 2026-05-13 and gives no drop date, The Register
    (published 2026-05-13T16:16Z) says only "dropping them just after Microsoft''s monthly Patch Tuesday update", NCSC-CH #12574 was created 2026-05-14. The main analysis says "On 2026-05-13 BleepingComputer
    and The Register reported". Cite it or state the reported date. Text not changed this fire.'
- code: F11
  category: editorial-advisory
  section: 2026-09-12/japan-digital-agency-gss-vpn-breach-maintenance-account (main analysis, paragraph 1)
  item: Japan Digital Agency GSS, scope of affected people
  url_or_quote: no general citizen data, only GSS-using-agency staff, associated public servants, and contracted businesses
  summary: '(pre-existing, low confidence) The cited Rocket Boys page and the Digital Agency notice name businesses and individuals: "GSS利用機関の業務に携わった事業者及び個人" (about 57,000 records); the clause says "only
    ... contracted businesses" and drops the individuals, while the entry''s own 2026-10-21 section says "the businesses and individuals involved". The sentence is unchanged by this fire apart from the
    em dash. Reword to "businesses and individuals".'
- code: F11
  category: editorial-advisory
  section: docs/audits/2026-10-21-cleanup-wave-03.md (Not reached and carried forward)
  item: Residuals bullet, Copy Fail and Dirty Frag link
  url_or_quote: 'that Copy Fail and Dirty Frag did not reference each other, was resolved after verifier iteration 1: Dirty Frag now lists Copy Fail.'
  summary: (low confidence) repair-1.md states the residual as "neither lists the other in references[]". Only Dirty Frag lists Copy Fail now; the Copy Fail entry's references[] still names only 2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.
    Iteration 5 had advised rewording the residual to the reverse direction. "Resolved" is defensible under the report's own newer-to-older link convention; say so ("the link points from Dirty Frag, the
    later flaw") or name the reverse direction as still open.
- code: F11
  category: editorial-advisory
  section: work/cleanup/plan.json totals and docs/cleanup/STATUS.md (Totals table)
  item: Measure "Known duplicate groups open (W4)"
  url_or_quote: 'W4-01, W4-03 to W4-05 done (wave 03); open: W4-02, W4-06 to W4-10'
  summary: (low confidence) Row W4-11 (Fragnesia link, wave 12) was added after iteration 5 and is status open, but the cell still ends at W4-10 while the row table beneath lists W4-11 open; the Rows measure
    (58 rows, 29 / 2 / 7 / 20) already counts it. Extend the cell to W4-06 to W4-11, or state that W4-11 is a link row, not a duplicate group.
- code: F11
  category: editorial-advisory
  section: runs/2026-10-21/2026-10-21T1149Z-audit.md (iteration 1 block) vs docs/audits/2026-10-21-cleanup-wave-03.md
  item: Declined priority calibrations carried forward
  url_or_quote: 'SimpleHelp critical (pre-existing): declined this fire; carried forward for calibration. / Dirty Frag high (pre-existing): declined this fire; carried forward for calibration.'
  summary: (low confidence) The record says two pre-existing priority calibrations (SimpleHelp critical after its improvement section narrowed exposure to a non-default Group setting; Dirty Frag high with
    exploitation unconfirmed) are carried forward, but neither the report's "Not reached and carried forward" section nor any tracker row names them, so the carry-forward has no destination. Name them in
    the report (to the next priority calibration) or drop the phrase.
- code: F11
  category: editorial-advisory
  section: 2026-06-30/cve-2026-48558-simplehelp-rmm-oidc-sso-authentication-bypass
  item: Three claims citing only CCB Belgium (67a2cb0628, b3d0654cb8, 1b7635154c)
  url_or_quote: https://ccb.belgium.be/advisories/warning-simplehelp-patched-cve-2026-48558-critical-authentication-bypass-vulnerability
  summary: '(low confidence) The page is unreadable on every rung this iteration: extract and url fall to jina and return a 503 maintenance page, WebFetch returns HTTP 403. Claim rows are `unreadable`,
    no defect asserted: the NVD API (VulnCheck CNA, cross-check only) gives CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H, base 10.0, and the repair worker''s saved copy reads "CVSS 10 (CVSS:3.1/...)". Re-read
    the page when CCB is back.'
```
