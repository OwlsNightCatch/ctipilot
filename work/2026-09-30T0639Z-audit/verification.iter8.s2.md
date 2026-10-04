**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-04T11:03:04Z · ended_at=2026-10-04T11:20:57Z · duration_seconds=1073

## Verification report — 2026-09-30T0639Z-audit (iteration 8, slice s2 of 4, post-fix pass)

Scope: 364 claims in `claims.iter8.s2.scope.yaml` (every claim of the remediated entries plus the seeded quarter of the rest), 19 entries read whole, every cited page fetched this iteration (`extract`/`url`; Socket via raw HTML + trafilatura; MSRC CVRF 2020-Feb and 2019-May; Oracle risk matrix parsed programmatically against all 50 `cves[]` records; NCSC-NL advisory TXT for Kans/Schade). claims_in_scope=364, claims_checked=364 (360 ok, 4 non-ok). `check_run.py` re-run: 0 fail other than the verification block itself, 1 warn (timestamps of other-slice entries).

### Walk of the iteration-7 remediation log (9 items)
- F14 Virtualizor ("only"): FIXED. Body now says "currently suspended and paid up"; VulnCheck: "type 2, in-house-billing, currently suspended, with cur_bal >= usage: in practice a manually-suspended, paid-up account".
- F3 conference-phishing (live infrastructure): FIXED. Now "queried the live infrastructure of a sibling campaign"; Huntress recap: "we sent the reconstructed request to the live SignNow sibling".
- F4 conference-phishing (VirusTotal faking as observed): PARTLY FIXED. Title, headline and the 2026-09-30 Correction now say capability; the frontmatter summary was not changed and still states fabricated results as done (finding #1 below).
- F4 Arista (rce type/tag): FIXED. `type: path-traversal` is supported by NCSC-NL NCSC-2026-0385 ("Path Traversal"); `rce` tag gone. Residual advisory #6.
- F4 NightEagle (CVE-2020-0688 CVSS 8.8): FIXED. MSRC CVRF 2020-Feb carries no score; `cvss: null`. CVE-2019-0708 9.8 confirmed in CVRF 2019-May.
- F5 Oracle (HFM sentence): FIXED. Sentence gone (grep "consolidation" no hit).
- F8 Push Security (RPC advice): FIXED and correct. BACS: "Companies and critical infrastructure operators that do not operate in the fintech sector should restrict outbound connections to RPC providers"; the code is retrieved through RPC providers. Record public with a short Correction section.
- F11 five record summaries: FIXED. Policy narration is gone; they say where the figure came from.
- F11 Pentagon length: decline holds (takeaway is required by the actionability contract); not re-raised.

### Unsupported / hallucinated facts
- #1 F4 `2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence`, summary: "so a local proxy answers the machine's VirusTotal lookups over fully validating HTTPS with fabricated results." Huntress 2026-08-19: "Lookups can be blocked outright or answered with fabricated results. VirusTotal was the only target we observed during analysis, with no operator interaction." The 2026-09-15 recap: "allowing the operator to block lookups or return fabricated clean results". Capability only; the body and Correction already say so. Fix: "can answer ... with fabricated results".
- #2 F4 (low confidence) `2026-09-21/nighteagle-...`, cves[CVE-2019-0708].affected "Windows 7, Server 2008/2008 R2 and earlier RDP-enabled builds": MSRC CVRF 2019-May lists Windows 7 SP1, Server 2008 SP2, Server 2008 R2 SP1 only; no cited page names "earlier" builds.

### Quantifier without source
- #3 F14 (low confidence) `2026-09-12/jfrog-...`, "no legitimate administrative action originates from the anonymous identity": Wiz gives "later requests appear with an actor of token:anonymous" and lists anonymous or low-privilege identities minting tokens, enumerating users or touching plugins as the anomaly; the universal negative is not stated.

### Claims missing inline citation
- #4 F5 (low confidence) `2026-08-10/coding-agent-...`, quote "cat /proc/$PPID/environ reads the parent, not self ...": verbatim on Novee but from the Gemini CLI section, in a paragraph with no citation that does not name the Gemini finding.

### Editorial / less-is-more flags (advisory)
- #5 F11 (low confidence) Push Security: record typed `correction` whose section corrects no published statement and repeats the takeaway's new sentence; `improvement` fits.
- #6 F11 (low confidence) Arista: `type: path-traversal` rests on NCSC-NL's label while Arista and KEV carry CWE-20 (the body states CWE-20); `status` has `no-patch` although 5.2.3.16+ and 6.4.2.8+ exist.
- #7 F11 (low confidence) NCSC-CH takeaway widens BACS's trigger (suspected credential leak) to receipt of the lure notification.

### Checks that came back clean
Oracle: all 50 `cves[]` records match Oracle's risk matrix row for row (id, base score, versions, protocol); the matrix has exactly 50 rows at AV:N/PR:N/UI:N/remote-without-auth Yes and 9.8-10.0 (6 at 10.0, 44 at 9.8); none is in `kev.json`; 673, 153, 78, 159/19, 50/8, 31/23 and the release dates match; NCSC-NL TXT: Kans high, Schade high. Check Point sk1000155/sk1000171 versions and fixes match. Cisco CWE-1327 present in the advisory HTML. JFrog tables, Wiz fixed list, KEV dates (2026-09-11) match. Em dashes in lines this run added: only inside a verbatim quote. Updated entries: each Correction describes only statements the published version made (checked with `git show origin/main`).

### Verdict
NEEDS_FIXES (truth: 3, editorial: 1, advisory: 3)

### Findings summary (machine-readable)
See `work/2026-09-30T0639Z-audit/verification.iter8.s2.findings.yaml`.
