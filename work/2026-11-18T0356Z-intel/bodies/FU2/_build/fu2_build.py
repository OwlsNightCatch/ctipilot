import sys, datetime
sys.path.insert(0, '.')
import fu2_lib as L
import fu2_oracle as O, fu2_mitel as M, fu2_agentfw as G, fu2_nable as N, fu2_axis as X

hdr = '''# FU2 deep read: primary-source claim sheets for five publishing items

Run `2026-11-18T0356Z-intel` | follow-up FU2 | worker model Sonnet 5.5 (`claude-sonnet-5-5`) | started 2026-11-18T04:36:43Z | fetched 2026-11-18 between ~04:40Z and ~05:10Z.

How to use this file
- Every table row is `claim | source URL | verbatim passage | saved body`. The passage is an exact, contiguous substring of the saved body named in the last column (under `work/2026-11-18T0356Z-intel/bodies/FU2/`). The generator checked every passage by exact substring match after writing: **%(checked)d passages checked, %(fails)d not found** (a failing row would carry the marker `[NOT FOUND IN BODY]`/`[CHECK FAILED]`). In the markdown a literal pipe inside a passage is escaped as `\\|` (table syntax only); `grep -F` the passage against the named body file, not against this markdown.
- Statements marked "assessment", "inference" or "derived" are this reader's, not a source\'s, and say so. Modality words are kept exactly as the sources use them ("could", "may", "is working on").
- Generator scripts (re-runnable) are in `bodies/FU2/_build/`.
- No IOCs are reproduced (no hashes, no exfiltration endpoint, no attacker addresses).

## 0. Headline: what changed versus the first pass

| item | one-line change |
|---|---|
| 6 Oracle CSPU | Every first-pass number reproduces from the 655 matrix rows (62 rows >= 9.0 across 57 CVEs; 56 unauthenticated rows across 51 CVEs; EBS 19; Database 9.9 rows need Create Session). But "21 product families" and "640 CVEs" are Tenable\'s figures, not Oracle\'s; the T3/IIOP row is 9.8 (only TopLink CVE-2026-91569 is 10.0); Java SE matrix includes CVE-2026-114938 at 8.1; new: the patch for EBS row CVE-2026-114918 "also addresses CVE-2025-61882" (KEV); no third-party exploitation or write-up found for any >= 9.0 row; only CVE-2026-111497 is on KEV. Full 56-row table below. |
| 7 Mitel MiCollab | First pass confirmed. Added: Mitel itself says 10.3 (10.3.0.18) and earlier is affected and needs the KB000129195 patch, while CERT-FR and BSI both say "before 10.3.0.18" (BSI lists 10.3.0.18 as fixed); 10.3.0.18 is the build that fixed MISA-2026-0006 in July, so July-patched sites are still in scope; no CVE ids in EUVD or NVD as of 2026-11-18; the MTLVULN-1864 impact sentence is garbled ("requires could allow"); advisory carries no exploitation statement either way. |
| 11 agent-framework PyPI | Three more independent detectors (Wiz, StepSecurity, Aikido) plus StepSecurity\'s PyPI quarantine times (1.26.1 at 21:06:16Z; 1.26.2 uploaded 2 min 23 s later, quarantined 21:16:44Z); the "31 substrings / 60 files" figures are the 1.26.1 profile (1.26.2: 35 / 80 per StepSecurity and Wiz); PyPI JSON shows 1.26.0 as latest and no 1.26.1/1.26.2; still NO Microsoft or PyPI statement found, and GitHub (microsoft/agent-framework) was unreadable from this session. |
| 12 N-able HF3 | Release notes confirm the first pass. New since the covered entry: Huntress (2026-11-17 8:30 ET) reports N-able CNA scores for all 17 CVEs (3 critical 9.3/9.3/9.2, 8 high, 6 medium), says public PoC code for all 17 appeared the evening of 16 Nov and that it has not observed exploitation; N-able\'s own HF3 notice and release notes still name neither 4EverAble2Shell, Agent2Shell nor the Axis CVE, so "HF3 fixes them" is unsupported, but the stated Legacy-API precondition is now permanently blocked. Extra lead: N-able Mail Assure/SpamExperts security incident (N-able, 2026-11-18 03:05Z). |
| 13 Axis OS | PDF read in full (one page). First-pass sentence "Axis phrases the advisory as an HTTP/2 flaw reachable on the device web interface" is NOT supported by the PDF (no such words); Axis lists no tracks or fixed versions, only "AXIS OS 6.50.5.10 or higher", CVSS 9.8, no known public exploits or exploitation "to Axis\' knowledge", a service release "within the next couple of weeks", and the two System.HTTP2 workaround parameters. Axis registry (page date 2026-11-17) lists no released version. |
'''

body = hdr % {'checked': L.CHECKED[0], 'fails': len(L.FAILS)}
secs = [O.SECTION, M.SECTION, G.SECTION, N.SECTION, X.SECTION]
doc = body + '\n' + '\n\n'.join(secs) + '\n'
# the header text needs the final numbers: re-render after all sections are built (CHECKED counted at import)
doc = (hdr % {'checked': L.CHECKED[0], 'fails': len(L.FAILS)}) + '\n' + '\n\n'.join(secs) + '\n'
doc += '''
## 6. Unreadable or unverified (cross-item)

- github.com/microsoft/agent-framework (repo, issues, security advisories) and api.github.com: HTTP 404 through `url`, `extract` and `WebFetch` (the sandbox proxy only enables repositories attached to the session); `gh` access not enabled. Item 11: Microsoft statement unverified.
- Mitel KB000129195 and N-able/Oracle My Oracle Support notes (CPU433, CPU454, KA923, KA1182): customer-login pages, not read.
- Oracle pre-release page (652 patches): replaced by the published advisory; only `state/coverage_backlog.md` records its numbers.
- Axis PDF: readable only through `fetch_source.py pdf` (the raw download through `url --direct` is corrupted by the proxy path); text layer is token-per-line, normalized copy saved.
- uptime.n-able.com is script-rendered: readable only through the jina reader (two of three keys were out of balance, the third worked; the pool may be dead at the next fire).

## 7. Source-health notes for the main agent (recipes that worked or failed)

- `extract` served every page here directly except the N-able HF3 release notes (served by jina) and the Axis PDF (use `pdf`).
- `safedep.io` article: `extract` silently drops the "Timeline" block (script-rendered component); recover from `url --direct` raw HTML (the section text is in the HTML).
- Oracle: `extract` reads the advisory and the "verbose" English matrices; the raw HTML carries the "Affected Products and Patch Information" table that `extract` drops.
- N-able uptime dashboard event pages: `jina <URL>` works (event/202669, event/202613); `extract` returns the empty shell.
- EUVD: `api/search?text=<vendor>&fromDate&toDate&page&size` works through `url --direct` and pages with `page=N`.
'''
open('/home/user/ctipilot/work/2026-11-18T0356Z-intel/deepread.FU2.md', 'w').write(doc)
print('doc bytes', len(doc), 'checked', L.CHECKED[0], 'fails', len(L.FAILS))
for f in L.FAILS:
    print('FAIL', f)
