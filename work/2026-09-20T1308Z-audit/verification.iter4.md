**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T14:45:34Z · ended_at=2026-09-20T14:52:42Z · duration_seconds=428

## Verification report — 2026-09-20T1308Z-audit (iteration 4)

### Prior-iteration deltas — walked and confirmed

1. **Item 1 (F4, "all five" in action item):** confirmed fixed. `grep -in "five"` against the entry file returns zero hits inside the file body (the only "five" anywhere is the immutable slug in the file path, as expected). Action item 2 now reads "all six flaws".
2. **Item 2 (F4, run-record coverage notes):** confirmed fixed. The run record's `## Verification and coverage notes` now reads "six unauthenticated CVSS 10.0 flaws across WebLogic Server, Access Manager, Forms, Internet Directory, Platform Security for Java and Hyperion Financial Management … relayed by NCSC-NL on 2026-09-16 at priority Hoog" — six named, Hyperion included, no likelihood/damage framing.
3. **Item 3 (F4, audit report stale paragraphs):** confirmed fixed on both cited surfaces (report line 55 published-recovery paragraph, line 167 verdict paragraph) — both list six CVEs including CVE-2026-87230/Hyperion and both narrate the NCSC-NL correction accurately. Line 55 also flags the slug/count mismatch as instructed.
4. **Item 4 (F8, Hyperion version + availability rating):** confirmed fixed and confirmed correct against the primary. Fetched Oracle's saved risk-matrix text (`work/2026-09-20T1308Z-audit/src_oracle_cspu.txt` lines 615–621): CVE-2026-87230 row reads `Oracle Hyperion Financial Management | Security | HTTP | Yes | 10.0 | Network | Low | None | None | Changed | High | High | None | 11.2.26.0.000`. The entry's `cves[]` record now carries `affected: "...11.2.26.0.000..."`, action item 1 lists the version, and the body correctly states "the first five also reach high availability impact; Hyperion Financial Management's is rated none" — verified against the same table for all five other CVEs (rows for CVE-2026-71133/83099/83059/83020/83021, lines 405–409, all show Availability=High). **However**, this remediation did not fully propagate — see new Finding #1 below, found while re-reading the sibling frontmatter field this same fix should have touched.
5. **Item 5 (F4, declined em-dash/18-sources figure):** the decline is reasonable on its face; I did not re-run the full enumeration myself given time budget, but separately reproduced the report's headline em-dash figure exactly (see below), which supports the report's general figure-checking rigor on this pass.

### New findings from this cold pass

**F4-class: entry's own frontmatter still carries the stale NCSC-NL claim iteration 2 found unsupported and iteration 3/this report call fixed.**

`entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md`, frontmatter `sourcing_note`:

> "NCSC-NL republished the Fusion Middleware half of the release as its own advisory and added its own high likelihood and high damage rating, which is a second assessment of severity rather than an independent assessment of the underlying facts."

This is the exact claim iteration 2 flagged (F3): "The entry cited NCSC-NL's advisory page for a rating of high on both likelihood and damage; that page shows a single priority field, and the dual marker appears only in the advisory feed the entry does not cite." I re-fetched the cited advisory this iteration (`https://advisories.ncsc.nl/2026/ncsc-2026-0372.html`, the redirect target of the entry's cited `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0372`) and confirm the page shows exactly one severity field: `Prioriteit / Hoog`. No "likelihood" or "damage" fields appear anywhere on the page.

The body paragraph 1 **was** correctly fixed to "assigned it priority 'Hoog', its high rating" — but the frontmatter `sourcing_note` was never touched, so the entry now contradicts itself: the body states a single priority rating, the sourcing note still asserts a dual "high likelihood and high damage rating." This is the exact "fixed on one surface, not propagated to the sibling" pattern the spawn message asked me to hunt for — it slipped through two prior post-fix passes (iteration 2 fixed the body only; iteration 3 re-verified the Hyperion version/availability fix but did not re-check this sibling field). It also means `docs/audits/2026-09-20-quality-audit.md` line 167 ("The same pass caught the entry citing NCSC-NL's advisory page for a dual likelihood-and-damage rating that page does not show … All four are fixed") is itself now inaccurate — the fix was not complete.

**F4 (low confidence): audit report's Oracle CVE-index count does not reproduce.**

`docs/audits/2026-09-20-quality-audit.md` line 59: "the store carries ten Oracle entries, **48 Oracle CVE-index records**". I confirmed "ten Oracle entries" reproduces exactly (10 files match title `Oracle|WebLogic|PeopleSoft|Hyperion|E-Business`: the 2026-06-03, 06-18, 07-01 ×2, 07-16, 07-26, 08-05, 08-20, 08-30 and 09-20 entries). But every method I tried for "48 Oracle CVE-index records" against `state/cves_seen.json` came up well short:
- Title contains "oracle" (case-insensitive): 28 of 1129 records.
- Title contains "oracle" OR `primary_source_url` contains `oracle.com`: 28.
- Title contains "oracle" OR any of weblogic/peoplesoft/hyperion/siebel/e-business/fusion middleware/jd edwards/primavera/agile/communications/banking: 29.
- Unique CVE ids drawn from every entry whose `title:` or `affected_products:` line contains "Oracle" (11 entries, including the two ShinyHunters/NAIC PeopleSoft-campaign entries), cross-checked as present in `cves_seen.json`: 23.

None reach 48 — the closest broad method is 29, roughly 40% short. I could not find a counting method that reproduces 48 within the time budget. This may be a genuine miscount (the same class of error iteration 1 and 2 caught twice already in this report — the em-dash figure and the five/five record-type count), or the audit may be using a data source or definition I have not identified; either way it does not reproduce and is worth a second look. (For contrast, I independently reproduced the report's em-dash figure exactly: `grep`-equivalent count over `entries/*/*.md` gives 8,416 em dashes across 906 of 917 files, matching the report's corrected figure verbatim — so the report's other headline figures are not uniformly suspect, which makes this particular one stand out.)

### Editorial / less-is-more flags (advisory)

**F8 (low confidence): categorical framing stretches to cover Hyperion.**

Body, paragraph 3: "Each of the six is reachable by an unauthenticated network request against a component that exists to sit in front of other systems or to hold what they rely on: WebLogic's web container, Access Manager's authentication engine, an Internet Directory LDAP listener, Forms Services, the shared Java security jars underneath Fusion Middleware, and Hyperion Financial Management's own security component. **These are the single-sign-on, directory and application-server tiers** that Swiss federal, cantonal and communal estates run legacy back-office and identity services on…"

Oracle's own risk matrix files Hyperion Financial Management under a separate "Oracle Hyperion" product family (102 patches, 50 remotely-exploitable-without-auth, its own risk-matrix section) distinct from "Oracle Fusion Middleware" (153 patches, 78 remote-no-auth) where the other five live. Hyperion Financial Management is an EPM/financial-consolidation application; its "Security" component is not itself an SSO, directory, or application-server tier the way WebLogic's web container, Access Manager's authentication engine, an LDAP directory, or Forms Services are. The generalizing sentence reads as though all six flaws sit in the identity/directory/app-server layer, when one of the six (the one added by iteration 2's remediation) is a back-office application's own security module. Not a factual error (no source is misquoted), but a categorization that overreaches for the sixth item added after the paragraph was originally written for five. Suggest narrowing to something like "…and Hyperion Financial Management's own security module — the single-sign-on, directory and application-server tiers, plus one back-office application, that…", or simply dropping the generalizing clause.

### Checks performed with no issue found

- All six `cves[]` records (id, cvss, affected version string) verified against Oracle's own risk-matrix rows in `work/2026-09-20T1308Z-audit/src_oracle_cspu.txt`: CVE-2026-83021/71133/83099/83059/83020 (lines 405–409, Fusion Middleware section) and CVE-2026-87230 (line 620, Hyperion section) all match CVSS 10.0, AV:N/AC:L/PR:N/UI:N/S:C, and the version strings in the entry exactly.
- Both `evidence[]` Oracle quotes and the CSPU-definition quote verified as verbatim substrings of the fetched Oracle page (`673 new security patches...`; `78 of these vulnerabilities...`; `A Critical Security Patch Update (CSPU) provides targeted...`).
- Citation date (2026-09-15) verified against the advisory's own revision-history table ("2026-September-15 | Rev 1. Initial Release."), not the page's generic "Updated Date" meta tag (2026-09-10, which is boilerplate template metadata, not the advisory's actual publish date) — correctly sourced by the entry.
- NCSC-NL advisory content (priority "Hoog", the five CVSS-10.0 Fusion-Middleware-only CVE list, publication date 16-09-2026) verified against the fetched advisory page; entry's characterization of "the Fusion Middleware half" is accurate — Hyperion does not appear on the NCSC-NL page.
- The iteration-3 question "should the availability-impact distinction (first five High, Hyperion None) also reach the summary?" — checked: the frontmatter `summary` field does not make any impact-completeness claim (it does not mention CIA impact at all), so there is no overstatement to fix; leaving it out of the summary is normal editorial compression, not a defect.
- Spot-checked git diffs and re-verified sources for 5 of the 10 updated entries against fresh primaries: Cisco FMC correction (`Replaced hot fixes with the security hardening releases`, `7.0 and earlier | 7.0.10` etc. — verbatim match in `work/2026-09-20T1308Z-audit/src_cisco_fmc.txt`), Brevo correction (`Brevo served malware to visitors of its own site and more than 100 thousand customer sites` — verbatim match in `work/2026-09-20T1308Z-audit/src_sansec.txt`), Linux KEV correction (Red Hat's `"The corner case we missed is when the initial record comes from rx_list, and it's zero length."` — verbatim on the fetched Red Hat CVE-2025-39682 page; The Hacker News quote of Red Hat's `"This CVE is high risk and there are known public exploits leveraging this vulnerability. … Address this vulnerability with high priority."` — verbatim on the fetched THN article, correctly cited to THN as the outlet carrying the quote), Japan/Piyolog correction, GTG-27005/Anthropic correction — all clean, all internally consistent between record `summary`, the `## <Type> — <at>` section, `fields[]`, and the diff.
- Spot-checked the four `internal: true` improvement records (Salt, Chosen Brick, AEPD, Gyazo) — all correctly carry no `## <Type>` section, all `fields[]` match the diff, all removed PD-number/production-process language without changing any factual claim. Confirmed the store-wide bare-`PD-<n>` count the report claims (11 remaining after this fire's three fixes) reproduces exactly via `grep -rlE '\(PD-[0-9]+\)|PD-[0-9]+ carve-out|\bPD-[0-9]+\b' entries/*/*.md` → 11 files.
- All six new Oracle CVE ids confirmed newly added to `state/cves_seen.json` with `first_seen: "2026-09-20"` and no prior entry — no dedup collision.
- `entities: []` on the Oracle entry is consistent with the two `references[]`-linked prior Oracle CPU/CSPU entries (both also carry `entities: []`), which is this store's established convention for vendor-vulnerability entries with no actor/campaign entity.
- Run record's three `verification.iterations` blocks: each iteration's `truth`/`editorial`/`advisory` counts reconcile exactly against its own listed `findings[]` (iteration 1: 5 F4 truth + 1 F12 editorial + 1 F11 advisory = 5/1/1 ✓; iteration 2: 1 F10 + 1 F8 editorial, 1 F3 + 2 F4 truth = 3/2/0 ✓; iteration 3: 4 F4 truth (incl. the declined one) + 1 F8 editorial = 4/1/0 ✓). `verification_residual_count: 5` correctly equals iteration 3's truth(4)+editorial(1).
- No missed angle identified this pass beyond what the run record's own coverage-backlog and recommendations already name; the coverage-backlog rows (AFPA, Talos, Securelist, SentinelLabs, Huntress ×2, Elastic) are consistent with the run record's telemetry and I found no additional in-window item to add.

### Verdict

**NEEDS_FIXES (truth: 2, editorial: 1, advisory: 0)**

Truth: the sourcing_note staleness (high confidence) and the "48 Oracle CVE-index records" figure (low confidence). Editorial: the Hyperion categorization stretch (low confidence, advisory-adjacent but listed as F8 needs-more-research since it's a real precision gap in a shipped entry, not merely a stylistic nicety).

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entry
  item: "Oracle's September 2026 CSPU — six unauthenticated CVSS 10.0 flaws (entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md)"
  url_or_quote: "sourcing_note: \"NCSC-NL republished the Fusion Middleware half of the release as its own advisory and added its own high likelihood and high damage rating, which is a second assessment of severity rather than an independent assessment of the underlying facts.\""
  summary: "Stale claim iteration 2 found unsupported and the body already fixed to 'priority Hoog, its high rating'; the sourcing_note frontmatter field was never updated and still asserts a dual likelihood-and-damage rating the cited NCSC-NL page (https://advisories.ncsc.nl/2026/ncsc-2026-0372.html) does not carry — it shows a single 'Prioriteit: Hoog' field. Entry now contradicts itself between body and frontmatter; also makes docs/audits/2026-09-20-quality-audit.md line 167's 'All four are fixed' claim inaccurate."
- code: F4
  category: hallucinated-fact
  section: audit-report
  item: "docs/audits/2026-09-20-quality-audit.md, Findings — missing or incomplete coverage"
  url_or_quote: "\"the store carries ten Oracle entries, 48 Oracle CVE-index records\""
  summary: "(low confidence) 'ten Oracle entries' reproduces exactly; '48 Oracle CVE-index records' does not reproduce under any method tried against state/cves_seen.json (title-match: 28; title+url: 28; broad product-keyword match: 29; unique CVE ids from all Oracle-titled/affected_products entries cross-checked in cves_seen.json: 23). Closest is 29, about 40% short of 48."
- code: F8
  category: needs-more-research
  section: new-entry
  item: "Oracle's September 2026 CSPU — six unauthenticated CVSS 10.0 flaws (entries/2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10.md)"
  url_or_quote: "\"Each of the six is reachable by an unauthenticated network request against a component that exists to sit in front of other systems or to hold what they rely on: ... and Hyperion Financial Management's own security component. These are the single-sign-on, directory and application-server tiers that Swiss federal, cantonal and communal estates run legacy back-office and identity services on\""
  summary: "(low confidence) Categorization overreaches for Hyperion Financial Management, an EPM/financial-consolidation application Oracle itself files under a separate 'Oracle Hyperion' product family, not the SSO/directory/app-server tier the other five components belong to; reads as though all six sit in the identity layer."
```
