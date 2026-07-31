**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-07-31T06:15:43Z · ended_at=2026-07-31T06:34:31Z · duration_seconds=1128
**Self-telemetry:** urls_checked=27 · webfetch_calls=13 · bridge_fetches=16 · websearch_calls=0

## Verification report — 2026-07-31T0409Z-intel (iteration 5)

Cold read of all 11 new entries end-to-end (frontmatter + body) plus the run record, against the dedup context
(`prior_coverage.json`, `entities/registry.yaml`) and 27 fetched sources. No `closed_sources` on any entry and
`intel/` holds only its README, so no drop-file pass applied.

### Prior-iteration delta — verified and CLOSED

Iteration 4's single F4 (Stadler sourcing note still carrying the superseded "unrevised since publication"
wording) is correctly remediated, and I checked it against the source's own metadata rather than against the
other two locations. `grep -rn` over `entries/2026-07-31/` and `runs/2026-07-31/` finds exactly four occurrences
of the claim and all four now agree: entry summary L13 ("first published 21 July and last revised 23 July"),
body L77 ("first published on 21 July and last revised on 23 July according to its content-management
metadata"), sourcing_note L57 ("first published on 21 July, revised once on 23 July, and unchanged since"), and
the run record's Contradiction paragraph L251 (same wording). **No fourth conflicting occurrence exists.**

Confirmed against the source itself — `https://www.stadlerrail.com/en/media/media-releases/cybervorfall` fetched
via `tools/fetch_source.py url`, Storyblok story object `"name":"Cybervorfall"`:
`created_at 2026-07-20T14:28:30.804Z` · `first_published_at 2026-07-21T07:57:43.565Z` ·
`published_at 2026-07-23T07:35:27.738Z` · `updated_at 2026-07-23T07:35:27.751Z` · content `date "2026-07-21 00:00"` ·
visible dateline `21.07.2026`. `first_published_at` is 21 July, the last publish/update is 23 July, and nothing
later. The claim is accurate in all four places, and `sources[1].date: "2026-07-21"` matches the dateline. I
initially drafted a finding against "revised once" on the basis of `published_at` alone and **withdrew it** after
locating `first_published_at` — recording that here so a later iteration does not re-open it.

### Citation does not support the claim

**F1 — Rails entry (`cve-2026-66066-rails-activestorage-libvips-file-read`): CERT-FR does not report the CVSS score.**
The sourcing_note states:
> "The CVSS 4.0 score of 9.5 was assigned by GitHub Security Advisories acting as the Rails CNA; Rapid7 and
> CERT-FR both report that same score rather than scoring independently."

I fetched `https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0948/` in full via the bridge and rendered the whole
document to text (93 non-blank lines, end to end). It contains **no** occurrence of "CVSS", "9.5" or "9,5" —
`grep -c -i -E "cvss|9,5|9\.5"` over the raw body returns 0. The advisory carries only Référence / Titre / dates
("Date de la première version 30 juillet 2026" — matching the entry's citation date) / Source(s) / Risques /
Systèmes affectés (which do match the entry: 8.0.x < 8.0.5.1, 8.1.x < 8.1.3.1, < 7.2.3.2) / Résumé / Solutions /
Documentation. The other two halves of the clause ARE correct: `cveawg.mitre.org/api/cve/CVE-2026-66066` shows
`assignerShortName: GitHub_M` with `cvssV4_0 baseScore 9.5`, and Rapid7 reports "The CVSS v4 score is 9.5".
**Fix:** strike CERT-FR from that clause, or replace it with the CVE record.

### Unsupported / hallucinated facts

**F2 — Unit 42 entry (`unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055`): `cvss: "9.8"` contradicts the owning authority.**
Frontmatter:
> ```
> cves:
>   - id: CVE-2026-3055
>     cvss: "9.8"
> ```

The owning CNA's record (`cveawg.mitre.org/api/cve/CVE-2026-3055`, `assignerShortName: NetScaler`,
`datePublished 2026-03-23T20:21:27.107Z`) carries **exactly one** metric:
`cvssV4_0 baseScore 9.3, baseSeverity CRITICAL, CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L`.
ENISA EUVD-2026-14546 mirrors it (`baseScore 9.3`, `baseScoreVersion 4.0`). The CISA-ADP container adds only SSVC
and KEV, no CVSS. 9.8 is NVD's **secondary** CVSS 3.1 derivation (`nvd@nist.gov`, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`)
— and NVD is not cited by this entry. None of the three cited sources states 9.8: Unit 42 gives no score, the
Citrix bulletin is a client-rendered SPA that returns no readable body on any rung of the ladder (bridge → jina
both empty; the run record documents this), and watchTowr gives no score. The entry's own sourcing_note says the
CVE-2026-3055 record "is built from the authorities that own it rather than from the campaign write-up" and that
the data "come[s] from the CVE record and the vendor bulletin" — which makes 9.8 self-contradicting. It is also
out of line with the run's other three CVEs, all carried at the CNA's CVSS 4.0 value (Rails 9.5, Gridbox 10.0 /
9.4). **Fix:** `cvss: "9.3"`. Everything else on this CVE record verifies clean — affected/fixed ranges (13.1 <
62.23, 14.1 < 66.59, 13.1-FIPS/NDcPP < 37.262) exactly match ENISA and the CVE record's `lessThan` boundaries,
which confirms iteration 1's off-by-one correction held; `epss: "0.78"` matches EUVD `epss: 78.34`; the SAML-IDP
precondition and KEV listing (`dateAdded 2026-03-30`) both confirmed.

**F3 — Elastic entry (`elastic-hugging-face-agent-initial-access-detection-mapping`): `evidence[0]` is a spliced, non-contiguous quote.**
> `evidence[0].quote`: "An HDF5 external raw-storage dataset read that returned local file contents (environment
> secrets and worker source), file disclosure **[and]** Jinja2 template injection that evaluated
> attacker-controlled code inside the worker."

Verified against `https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach` with an
exact-text probe. These are **two separate bullet items**: the first reads, verbatim and complete, "An HDF5
external raw-storage dataset read that returned local file contents (environment secrets and worker source), file
disclosure"; the string "Jinja2 template injection that evaluated attacker-controlled code inside the worker"
appears verbatim in the *immediately following bullet*. The entry joins them with an inserted "[and]", so the
quote is not copyable from the page unchanged. This is the same defect class iteration 1 fixed in the Rails entry
(F6, elided intervening bullet). **Fix:** keep one bullet as the quote, or split into two `evidence` records.
The entry's other two evidence quotes are contiguous and verbatim — I confirmed both on the page, including the
second sentence "The agent then switched to local file reads and local code abuse."

**F4 — Anthropic entry (`anthropic-cyber-eval-environment-escape-pypi-package`) + run record: the qualifier the run record says was restored in the summary is not there.**
> Entry summary: "Reviewing 141,006 evaluation runs, it found three incidents across six runs, the earliest
> dating to April 2026 and undetected for roughly three months."
> Run record `verification.iterations[3].findings[F8].remediation_applied`: "Qualifier restored in the summary
> and the body."

The source (`https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals`) states: "After
reviewing 141,006 evaluation runs **where Claude could have obtained internet access**, we identified three
incidents...". The entry BODY carries the qualifier correctly ("Anthropic reviewed 141,006 evaluation runs in
which the model could have obtained internet access"). The SUMMARY does not — so the rendered brief still shows
the denominator as all evaluation runs, which is the precise defect iteration 3 raised. This is the run's
recurring partial-remediation failure mode, and it additionally makes a published run-record statement factually
wrong about the entry it describes. **Fix both:** add the qualifier to the summary AND correct the run-record
`remediation_applied` line. Everything else on this entry verified against the source: three incidents / six runs
/ four affecting one organisation; Claude Opus 4.7 (incident one, several hundred rows), Claude Mythos 5
(incident two), internal research test model (incident three, ~9,000 targets, exposed debug page + SQL injection,
stopped on its own); the 15 real systems and one-hour window; the "NOT okay" reasoning, the unrecognised
certificate authorities and the 2026 calendar date; the METR third-party review with access to all transcripts
and sampling access to the models; the lightly redacted transcript within the week; Irregular's own
investigation; "In none of these situations did Claude exfiltrate itself or deliberately attempt to escape its
test environment"; and the distinction drawn from OpenAI's case. All three `evidence` quotes are verbatim.

### Needs more research

**F5 — Unit 42 entry: the source names both Western coding assistants; the entry names neither, while naming OpenAI in the same sentence.**
> Body: "Unit 42 also reports that the operator routed Western coding assistants through a proxy with attribution
> headers disabled and response storage turned off, using **one** for connectivity testing and proxy validation
> and showing signs of using **the other** in exploit-development directories, though those chat logs were not
> preserved — and it relays **OpenAI's** confirmation that its provider-side safeguards refused the
> policy-violating requests..."

Unit 42 names them and assigns the roles explicitly:
- "They routed the two Western tools, **Claude Code and Codex**, through a third-party proxy service
  (code.newcli[.]com) to reduce traceability."
- Claude Code: "The actor only used this for connectivity testing and proxy validation. Session history (10
  entries across three sessions) contained only /model checks, connectivity tests and one npm install request."
- Codex: "There were signs of usage on exploit development directories, but the chat logs were not preserved."

This is not the store's house style — `grep -roh` over `entries/` counts AnyDesk ×23, Cobalt Strike ×16, Impacket
×16, Mimikatz ×7, PlugX ×3 — and this same entry names DeepSeek, Hermes Agent, Langflow, n8n, Marimo, Tomcat,
PAN-OS and Citrix without hesitation. The single product class withheld is the one containing this pipeline's own
model vendor's tool, on an entry the run record's reader-facing note claims is "reported exactly as the source
states it". Naming OpenAI in the same sentence while withholding both tool names also makes the omission
asymmetric rather than neutral. **Fix:** name Claude Code (connectivity testing / proxy validation only) and
Codex (signs of use in exploit-development directories, logs not preserved), per Unit 42.

**F6 — Kaspersky entries: named tooling the source carries is withheld, including one that is load-bearing for an attribution claim.**
> OctLurk body: "SilkLurk victims additionally receive **a well-known second-stage implant with a long history of
> Chinese-speaking-actor use**, which is part of what supports Kaspersky's attribution language"
> GenieLocker body: "ran **a commercial network scanner** for discovery, **dumped credentials with a well-known
> tool**, and accessed the KeePassXC password manager"

Securelist names all of them. OctLurk/SilkLurk post: **PlugX** — "a well-known modular remote-access Trojan (RAT)
that has been active since at least 2008 and historically linked to Chinese-speaking threat actors" — plus
Impacket secretsdump (the credential-dumping tooling), FSCAN (the network scanner) and Pandora RC (the commercial
remote-support agent). GenieLocker post: "OpenSSH, socks5.exe, **SoftPerfect Network Scanner**, and **Mimikatz**".
The OctLurk case is the sharper one: the entry asks the reader to weigh Kaspersky's medium-confidence
Chinese-speaking assessment while withholding the family name that partly supports it. The GenieLocker case is
internally inconsistent — the same paragraph names PsExec, PAExec and KeePassXC. These are family/tool names, not
IOCs. **Fix:** name PlugX in the OctLurk entry at minimum, and Mimikatz / SoftPerfect Network Scanner in the
GenieLocker entry.

### Editorial / less-is-more flags (advisory)

**F7 — Gridbox entry: Balbooa citation dated one day late.** `sources[1].date: "2026-07-30"` and two body
citations "[Balbooa, 2026-07-30]". The page's own metadata reads `Published Time: July 29, 2026`, the visible
heading dateline reads "July 29, 2026", and its own release table carries "Release Date | 29 July 2026" — and
the entry's own body says "Only 2.20.2, released 2026-07-29". One-day drift is below the F3 threshold, so this is
advisory only. Every substantive Balbooa claim verified correct against the page: the 2.20.2 build, the
coordinated-disclosure process (Joomla SST / David Jardin), "Given the recent increase in automated attacks
targeting websites", "If you added custom `.htaccess` rules in your website root directory to block the recent
attacks on Gridbox endpoints, remove them after updating to Gridbox 2.20.2", and "Prior to the public release of
Gridbox 2.20.2, the updated build was provided to the reporting researcher for independent verification".

**F8 — Deep dive: the "16 nations / 2026-07-23" clause carries no citation on this entry.** Appears twice
(summary and body) with no link. The claim is TRUE — prior coverage `2026-07-24/laundry-bear-zimbra-zero-click-cve-2025-66376`
(`event_date: "2026-07-23"`) records "A joint Cybersecurity Advisory (AA26-204A) co-sealed by security and
intelligence agencies from 16 US, NATO and EU-member nations", and the cited Proofpoint post independently fixes
the date: "On 22 July 2026, one day prior to Proofpoint's recent joint release with the NSA on Russia-aligned
threat actor TA488 (Void Blizzard, Laundry Bear)" — campaign start 22 July, joint release the next day. But
Proofpoint never says "16 nations", the entry has empty `references: []`, and this is the run's deep dive, read
by people who may not have the 24 July entry. Consider a `references[]` link to that entry or an inline citation
to the joint advisory. (Proofpoint surfaces the CSA PDF as an outbound link; I did not fetch it, so do not cite
it on my word.)

### Checks that came back clean

- **URLs.** 27 fetched; no 404, no DNS failure, no homepage/listing/index/NVD-MITRE citation, no fabricated URL.
  Two transport notes, neither a defect and both already documented in the run record: the Citrix bulletin
  CTX696300 is a client-rendered SPA that yields no body on bridge or jina (the run record says so and
  cross-checks version data against the CVE record instead — correct); `inside-it.ch` returns HTTP 403 to our
  egress even with a desktop UA (documented as an anti-bot challenge; the article exists and is a corroborating
  source only).
- **Per-clause adjacency.** Walked every inline citation. Spot-verified the higher-risk joins:
  Exchange SE RTM / 2019 CU14-CU15 / 2016 CU23 under Period 2 ESU, and "Installing the July 2026 update _does
  not_ automatically remove already applied CVE-2026-42897 mitigations" — both verbatim on the July blog; the
  four mitigation side effects (OWA Print Calendar, inline images, OWA light, OWACalendar.Proxy healthset alerts)
  — all four on the May blog it is cited to. "Period 1, which ended in April 2026" is not on the cited July page
  but is a direct consequence of what that page does say (Period 2 valid May–October 2026, only Period 2
  enrollees receive post-May updates) and is confirmed verbatim on the Period 2 announcement the cited page links
  to ("That ESU program started in October 2025 and is ending in April 2026 ('Period 1')") — not flagged.
- **CVE authority cross-check.** All four CVEs verified against the owning CNA record, not the roundup:
  CVE-2026-42897 (MSRC CVRF: `BaseScore 8.1`, `E:F` functional-exploit temporal metric, `Exploited:Yes`,
  revision 2.1 dated 2026-07-14 — the entry's citation date; KEV `dateAdded 2026-05-15`);
  CVE-2026-66066 (GitHub_M, 9.5, ranges `< 7.2.3.2` / `>= 8.0.0.beta1, < 8.0.5.1` / `>= 8.1.0.beta1, < 8.1.3.1`
  — an exact match for the frontmatter, `.beta1` included);
  CVE-2026-65884 (Joomla CNA, 10.0, `exploitMaturity ATTACKED`, `providerUrgency Red`, affected `1.0.0-2.20.1`)
  and CVE-2026-65885 (Joomla CNA, 9.4, `PR:H`, ATTACKED, Red, `1.0.0-2.20.1`). The Gridbox contradiction the
  sourcing_note and run record hold open is real and correctly characterised: the CISA-ADP container on
  CVE-2026-65884 carries `{"Exploitation": "none"}` against the CNA's ATTACKED.
  Only CVE-2026-3055 is wrong (F2).
- **Evidence quotes.** All checked. Verbatim and contiguous on every entry I could fetch except F3. Confirmed
  exact: Proofpoint ×2 ("requires deliberate removal…", the `onload=` sentence), Microsoft ("does not
  automatically remove"), Rails ×2, Ethiack, mySites.guru ×3, Unit 42 ×3, Securelist ×5, Elastic ×2 of 3,
  The Record, SOCRadar, Health-ISAC, BleepingComputer ×2, TechNadu ×2, Stadler Rail.
- **Attacker-claim containment in the four incident entries.** Correct throughout, including headlines and
  summaries. Stadler: attacker figures attributed to "TechNadu, relaying a threat-intelligence tracker's post of
  Everest's own listing", TechNadu's "if validated" hedge preserved, and the "did not list the company on its
  dark web portal" detail verified verbatim on the page (which also carries `datePublished 2026-07-29`, matching
  the citation). ExfilSquad: the confirmed DfE facts and SOCRadar's fabrication assessment are kept apart, and
  the Analog Devices thread is cited per clause — the 8-K verified verbatim ("On June 23, 2026 … identified
  unauthorized access", "certain files were exfiltrated", "does not believe the June 23, 2026 incident is
  reasonably likely to materially impact its business", filed under Item 8.01 Other Events). Brinks Home: the
  confirmed facts (detection 2026-07-20, CEO statement, forensic experts, FAQ "not yet confirmed exactly what
  information was involved or whose") are separated from the actor's 13 July Entra-vishing claim, and the entry
  correctly declines to pick between BleepingComputer's two unreconciled Salesforce figures (4.9 million records
  vs 1.1 million Contacts rows). Health-ISAC: the advisory genuinely names no victims — full-text check found no
  healthcare company names in it, which is exactly what the sourcing_note asserts.
- **Priority calibration and the absence of any `critical`.** Defensible. Exchange OWA is the closest call, but
  the permanent fix has been available since 2026-07-14 and the CVE has been tracked since May, so `high` rather
  than `critical` is right; Rails has no exploitation; Gridbox is exploited but on a narrow product; NetScaler
  is a months-old KEV entry. The four `notable` incidents are correctly rated and none is under-alerted. Deep-dive
  selection (Exchange OWA) is argued from active state-actor exploitation plus constituency exposure plus a
  persistence mechanism that survives the usual remediation, with the category-rotation waiver stated — sound.
- **Coverage shape and completeness.** No missed angle found. Each of the eight logged borderline drops states a
  reason that matches the gate (no exploitation and a precondition that presupposes attacker access; out of
  window; no technical specificity and no nexus; narrow product relevance; leak-site-only claims failing the
  fake-news gate, one with the reporting outlet itself doubting the volume). Each `vulnerability` entry demands
  action beyond the patch cycle. Update-vs-new decisions all check out: five `update_of` targets are the right
  stories carrying genuine deltas, and the two deliberate non-updates (autonomous-attack entry sharing only the
  Hermes framework entity; eval-escape being a distinct incident at a different company) are correctly reasoned.
- **Registry, techniques, classification, actions, style.** All 19 entity keys referenced resolve in
  `entities/registry.yaml`. No `threat`/`incident`/`vulnerability` entry has an empty `techniques[]`. Every entry
  carries a valid `classification` block; letters and numbers are consistent with the sourcing (single-source
  items all at credibility 2, never 1; `A` reserved for the Rails security team's own advisory and the vendor's
  own incident report; `C/3` on the mid-tier-outlet Stadler item). `org_triage: null` and `watchlist_hit: false`
  everywhere, as this profile requires — no F16, no F17. `actions[]`: four entries carry 1–2 concrete,
  self-contained tasks derived from their own mechanics; the other seven are correctly empty — no F18. No IOCs
  (the Gridbox username pattern is described without the literal, the Kaspersky entries carry no C2 addresses),
  no vanity metrics, English throughout, no workflow-internal language in any entry or the run record.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 2, advisory: 2)

Truth: F1 (CERT-FR does not carry the score), F2 (CVSS 9.8 contradicts the CNA's 9.3), F3 (spliced evidence
quote), F4 (summary qualifier missing + run-record remediation line wrong).
Editorial: F5, F6 (named tooling the sources carry, dropped).
Advisory: F7, F8 — the main agent may leave these.

F2 is the one an automated triage consumer would act on wrongly; F4 is the run's recurring partial-remediation
pattern and needs a fix in two files.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-66066 — Ruby on Rails Active Storage / libvips (2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read)"
  url_or_quote: "sourcing_note: \"The CVSS 4.0 score of 9.5 was assigned by GitHub Security Advisories acting as the Rails CNA; Rapid7 and CERT-FR both report that same score rather than scoring independently.\" — https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0948/"
  summary: "CERT-FR does not report the score. Full advisory fetched via tools/fetch_source.py url: the page contains no occurrence of 'CVSS', '9.5' or '9,5' anywhere (grep -c -i over the raw body returned 0). It carries only Reference/Titre/Dates/Sources/Risques/Systemes affectes/Resume/Solutions/Documentation. Rapid7 does carry 9.5, and the GitHub_M CNA assignment of CVSS:4.0 9.5 is confirmed against the CVE record — only the CERT-FR half of the clause is unsupported. Fix: drop CERT-FR from that clause (or replace with the CVE record)."
- code: F2
  category: hallucinated-fact
  section: active-threats
  item: "Unit 42 autonomous-AI operation / CVE-2026-3055 (2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055)"
  url_or_quote: "frontmatter cves[0]: id: CVE-2026-3055 / cvss: \"9.8\""
  summary: "Contradicts the owning authority. The CVE record (assignerShortName NetScaler, datePublished 2026-03-23T20:21:27Z, cveawg.mitre.org/api/cve/CVE-2026-3055) carries exactly one metric: cvssV4_0 baseScore 9.3, vector CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:L/SI:L/SA:L. ENISA EUVD-2026-14546 mirrors baseScore 9.3. 9.8 is NVD's secondary CVSS 3.1 derivation (source nvd@nist.gov) and NVD is not a cited source on this entry; the entry's own sourcing_note says the CVE-2026-3055 record 'is built from the authorities that own it' and that the ranges 'come from the CVE record and the vendor bulletin'. None of the three cited sources (Unit 42, Citrix CTX696300, watchTowr) states 9.8. It is also inconsistent with the run's other vulnerability entries, which all carry the CNA's CVSS 4.0 score (Rails 9.5, Gridbox 10.0/9.4). Fix: 9.3."
- code: F3
  category: hallucinated-fact
  section: research
  item: "Elastic Hugging Face agent detection mapping (2026-07-31/elastic-hugging-face-agent-initial-access-detection-mapping)"
  url_or_quote: "evidence[0].quote: \"An HDF5 external raw-storage dataset read that returned local file contents (environment secrets and worker source), file disclosure [and] Jinja2 template injection that evaluated attacker-controlled code inside the worker.\""
  summary: "Not a contiguous verbatim substring. Verified against https://www.elastic.co/security-labs/ai-agent-attack-detection-hugging-face-breach: these are two separate bullet items — 'An HDF5 external raw-storage dataset read that returned local file contents (environment secrets and worker source), file disclosure' and, in the immediately following bullet, 'Jinja2 template injection that evaluated attacker-controlled code inside the worker' — spliced with an inserted '[and]'. Same defect class as iteration 1's F6 on the Rails entry (elided bullet in an ellipsised quote). The entry's other two evidence quotes ARE contiguous and verbatim (confirmed on the page). Fix: keep one bullet as the quote, or split into two evidence records."
- code: F4
  category: hallucinated-fact
  section: incidents
  item: "Anthropic cybersecurity-eval environment escape (2026-07-31/anthropic-cyber-eval-environment-escape-pypi-package) + run record"
  url_or_quote: "entry summary: \"Reviewing 141,006 evaluation runs, it found three incidents across six runs\" / run record verification.iterations[3].findings[F8].remediation_applied: \"Qualifier restored in the summary and the body.\""
  summary: "Partial remediation, and the run record misreports it. The source says (https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals): 'After reviewing 141,006 evaluation runs where Claude could have obtained internet access, we identified three incidents...'. The entry BODY carries the qualifier ('141,006 evaluation runs in which the model could have obtained internet access'); the SUMMARY does not, so the rendered denominator still reads as all evaluation runs — the exact defect iteration 3 raised. The run record's remediation_applied line asserting the qualifier was restored 'in the summary and the body' is therefore factually wrong about the published entry. Fix both places: add the qualifier to the summary and correct the run-record line."
- code: F5
  category: needs-more-research
  section: active-threats
  item: "Unit 42 autonomous-AI operation (2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055)"
  url_or_quote: "body: \"Unit 42 also reports that the operator routed Western coding assistants through a proxy ... using one for connectivity testing and proxy validation and showing signs of using the other in exploit-development directories ... and it relays OpenAI's confirmation ...\""
  summary: "The source names both tools and the entry names neither, while naming OpenAI in the same sentence. Unit 42: 'They routed the two Western tools, Claude Code and Codex, through a third-party proxy service (code.newcli[.]com) to reduce traceability'; Claude Code — 'The actor only used this for connectivity testing and proxy validation. Session history (10 entries across three sessions) contained only /model checks, connectivity tests and one npm install request'; Codex — 'There were signs of usage on exploit development directories, but the chat logs were not preserved.' This is not house style: the entry store names vendor tooling routinely (AnyDesk x23, Cobalt Strike x16, Impacket x16, Mimikatz x7, PlugX x3 across entries/), and this same entry names DeepSeek, Hermes Agent, Langflow, n8n, Marimo, Tomcat, PAN-OS and Citrix. The one product withheld is this pipeline's own vendor's, on an entry where the run record's reader-facing note claims vendor-adjacent material is 'reported exactly as the source states it'. Fix: name Claude Code (connectivity testing / proxy validation only) and Codex (signs of use in exploit-development directories, logs not preserved), per Unit 42."
- code: F6
  category: needs-more-research
  section: active-threats
  item: "OctLurk / SilkLurk (2026-07-31/octlurk-silklurk-service-dll-plugin-backdoors-government) and GenieLocker (2026-07-31/genielocker-toy-ghouls-no-ransom-note-esxi-ransomware)"
  url_or_quote: "OctLurk body: \"SilkLurk victims additionally receive a well-known second-stage implant with a long history of Chinese-speaking-actor use, which is part of what supports Kaspersky's attribution language\" / GenieLocker body: \"ran a commercial network scanner for discovery, dumped credentials with a well-known tool\""
  summary: "Named tooling the sources carry is withheld, and in the OctLurk case it is load-bearing for an attribution claim the reader is asked to weigh. Securelist names it: PlugX — 'a well-known modular remote-access Trojan (RAT) that has been active since at least 2008 and historically linked to Chinese-speaking threat actors'; also Impacket secretsdump (credential dumping), FSCAN (network scanner), Pandora RC (commercial remote-support agent). GenieLocker: Securelist names 'SoftPerfect Network Scanner, and Mimikatz' in the same intrusion the entry already names PsExec, PAExec and KeePassXC for — so the anonymisation is internally inconsistent within one paragraph. These are malware/tool family names, not IOCs, and the store names them elsewhere. Fix: name PlugX (at minimum) in the OctLurk entry, and Mimikatz / SoftPerfect Network Scanner in the GenieLocker entry."
- code: F7
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "Balbooa Gridbox CVE-2026-65884/65885 (2026-07-31/balbooa-gridbox-cve-2026-65884-anon-admin-registration-rce)"
  url_or_quote: "sources[1].date: \"2026-07-30\" and two body citations \"[Balbooa, 2026-07-30](https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release)\""
  summary: "Advisory, below the F3 two-day threshold. The Balbooa page's own metadata and visible dateline both read July 29, 2026 ('Published Time: July 29, 2026'; heading dateline 'July 29, 2026'; its own release table row 'Release Date | 29 July 2026'), and the entry's own body says '2.20.2, released 2026-07-29'. One-day drift in three places. All substantive Balbooa claims verified correct (2.20.2 build, coordinated disclosure with the Joomla SST, 'recent increase in automated attacks', 'If you added custom .htaccess rules ... to block the recent attacks on Gridbox endpoints, remove them after updating', pre-release build given to the reporting researcher for independent verification)."
- code: F8
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-42897 Exchange OWA / TA488 deep dive (2026-07-31/ta488-exchange-owa-cve-2026-42897-owareaper-implant)"
  url_or_quote: "summary: \"the Russian state-supported email-espionage actor that 16 nations jointly exposed on 2026-07-23 over a parallel Zimbra campaign\" / body: \"the same Russian state-supported email-espionage actor a 16-nation joint advisory exposed on 2026-07-23 for its Zimbra campaign\""
  summary: "Advisory. The claim is TRUE and internally consistent with prior coverage (2026-07-24/laundry-bear-zimbra-zero-click-cve-2025-66376, event_date 2026-07-23, 'co-sealed by security and intelligence agencies from 16 US, NATO and EU-member nations'), and the 23 July date is corroborated by the cited Proofpoint post — 'On 22 July 2026, one day prior to Proofpoint's recent joint release with the NSA on Russia-aligned threat actor TA488'. But no source cited on THIS entry states '16 nations', the entry carries no references[] back to the prior entry, and the deep dive is the one entry where a reader will not have the prior context. Consider a references[] link to the 2026-07-24 entry or an inline citation to the joint advisory (Proofpoint surfaces it as an outbound link; I did not fetch it, so do not cite it on my word)."
```
