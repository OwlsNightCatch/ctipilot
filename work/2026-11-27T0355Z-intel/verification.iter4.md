**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T06:35:53Z · ended_at=2026-11-27T06:58:12Z · duration_seconds=1339

## Verification report — 2026-11-27T0355Z-intel (iteration 4)

Scope: post-fix pass after NEEDS_FIXES iteration 3. All 325 claims of `claims.iter4.yaml` have a verdict row in `verification.iter4.claims.yaml` (317 ok, 3 F4, 2 F3, 1 F5, 2 unreadable; `claim_ledger.py --coverage 4`: 325/325). Gate-cached page bodies were reused, and the deltas pages (Expel, F5 NGINX Plus release notes, Huntback, NCSC.ch 13244, DIVD case page and report PDF, Veeam KB4976, PAN-SA-2026-0015 HTML and JSON, PHP2Shell advisory JSON, BSI CSAF, Veria page, blog and GitHub org, CVE.org record) were fetched fresh this iteration.

### Prior-iteration deltas (all 10 re-read against sources)

| # | Remediation | Result |
|---|---|---|
| 1 ARTEX F3 | triage line names Huntress as reviewer | True. Expel: "Huntress found the ConnectWise Cloud Management and Partner Center apps it reviewed call Graph with kiota-dotnet, so a Python user agent on one of those apps is the anomaly." |
| 2 nginx F4 | CVE-2026-123634 fixed builds from F5 notes | True. The notes list the resolver use-after-free (CVE-2026-123634) under PLS.37.0.8.1 LTS and PLS.37.3.0.1 CR (both November 18, 2026); no affected ranges. |
| 3 Puppet F4 | clause Huntback does not state dropped | True. Section now says only "signed the certificate, accepted the report with a 200 and returned no marker", which is Huntback's wording. |
| 4 Juniper F4 | NCSC.ch summary credited | True. Post 13244 summary: "Juniper has confirmed malicious exploitation, and CISA has added the flaw to its Known Exploited Vulnerabilities catalog"; it carries neither the SIRT sentence nor the update date. |
| 5 Zammad F3 | case page dated 2026-11-25 | True. Page header "Last modified 25 Nov 2026 14:10 CET"; the quoted sentence is on it. |
| 6 nginx F3 | KB4976 labelled last modified | True. "Published: 2026-11-20 / Last Modified: 2026-11-25"; sources[] and the evidence publisher say "last modified 2026-11-25". |
| 7 Puppet F3 | declined (pre-existing release-notes date) | Not re-raised by design. Page says "Released November 2026". |
| 8 Fragnesia F9 | vendor FAQ framing added | True. Section now matches the FAQ ("a fixed PAN-OS listed in the CVE-2026-109618 advisory, you are protected"; next maintenance interval where management access is restricted; immediately where internet-reachable) and agrees with the PAN-OS entry. |
| 9 Fragnesia F11 | cross-entry pointer removed | Confirmed absent. |
| 10 summaries F11 | left to the audit | Not re-raised by design. |

### Citation does not support the claim (F3)
- #2 (low confidence) **Zammad** body, first paragraph: "DIVD assesses the attack as driven by AI agents, because the attacker's scripts carry notes in which the agent justifies its own actions, and its forensic report says the attacker likely used ARTEX and names no actor" now ends on the forensic report alone. The report bases the agentic conclusion on script volume and says the comments "provide a slight peek into the LLM's inner monologue"; the "justifies its own actions" wording is DIVD's public-statements page, which the sentence cited at HEAD. Re-add that citation.
- #4 (low confidence) **Mitel** body: "MITRE published CVE records for all five on 2026-11-19" cites EUVD-2026-130382, which carries CVE-2026-133323 only. The other four EUVD records (-130372, -130376, -130381, -130384, all published Nov 19) are cited only in the 2026-11-20 section. Cite all five or narrow the clause.

### Unsupported / hallucinated facts (F4)
- #1 (low confidence) **ARTEX** summary and record summary: "ARTEX and Cairn write a per-run numeric intent ID" / "a per-run numeric intent ID from a never-reset counter". Wiz: an ARTEX installation "runs its own counter and never resets it by default", numbers "climb across runs and targets"; only Cairn resets per project. The body's "a counter never reset" also drops Wiz's "by default".
- #3 (low confidence) **Zammad** 2026-11-27 section: "the client secret for the two shared mailboxes" was taken. The report's credential table lists XOAUTH2 tokens, the IMAP cleartext password, the Elastic credential, the Jira OAuth consumer private key and database credentials; NVISO only says Gmail API access is "indicating the exfiltration of OAuth client secrets, credentials, or tokens".

### Claims missing inline citation (F5)
- #5 (low confidence) **Fragnesia** 2026-11-27 section and its record summary: "later than the hotfix that fixes PHP2Shell". PAN-SA-2026-0015 does not state the comparison; it needs the CVE-2026-109618 advisory, which the entry does not cite.

### Unreadable
- `6c2d56f937` and `cb45aff710` (NFS2ROOT): both lore.kernel.org pages answer every transport (extract, `url --direct`, `/raw`, WebFetch 403) with an Anubis bot challenge. Content is consistent with the ENISA/CVE.org record (published Nov 19, updated Nov 23, eight unaffected versions), OpenSec's timeline (fix posted 17 Aug 2026) and watchTowr. I could not confirm that the announcement itself lists only four fixed versions; the "record was later updated" chronology rests on the entry's reading of the ENISA dates.

### Not raised on purpose
- Zammad main analysis (1,031 words), the oversize summary fields, and the Puppet release-notes citation date, all logged in the run record for the audit.
- Removed reader-useful detail in the trims (PAN-OS Threat Prevention coverage, nginx network-flow hint) is already acknowledged by the run.

### Whole-run checks
- Update contract (4c): nine `update` records, each with a matching `## Update` section, `updated_at` equal to the record `at`, `fields` matching `git diff HEAD`, no silent edit found; every delta is the same finding as its entry. Main analyses agree with the newest sections.
- Dedup: CVE-2026-99362 and the SoftwareOK/ASEC story have no prior coverage in `prior_coverage.json` or `state/cves_seen.json`; registry keys exist.
- Priority and classification: no miscalibration found; classification present on all eleven entries; SoftwareOK single-source B2 consistent; no org_triage or watchlist use.
- Style: no em dash outside headings, no IOCs or hashes in the new text, no pipeline vocabulary in reader-facing fields.
- Missed angles: standard searches for in-window exploited flaws and Swiss municipal incidents returned nothing new; GeoServer, Drupal, Xen Orchestra and Danfoss items from the 2026-11-26 SecurityWeek page are already in the store. Coverage looks complete for critical and high signal.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 0)

All five findings are low confidence and one-clause fixes; none touches an action, a priority or a fixed version.

### Findings summary (machine-readable)
See `work/2026-11-27T0355Z-intel/verification.iter4.findings.yaml` (5 records).
