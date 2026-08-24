**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-24T00:44:05Z · ended_at=2026-08-24T01:06:27Z · duration_seconds=1342
**Self-telemetry:** urls_checked=51 · webfetch_calls=1 · bridge_fetches=24 · websearch_calls=1

## Verification report — 2026-08-23T2311Z-weekly (iteration 3)

Read cold. All 51 distinct URLs cited across the fourteen entries were HTTP-checked (all 200; the two
`sophos.com` posts fail plain curl through the proxy but resolve via the bridge). Twenty-eight quoted
strings were literal-substring-checked against saved or freshly fetched page bodies — 28/28 pass
(the one initial FAIL, the Talos "inverted success condition" quote, matched verbatim once the
correct Talos post — the agentic-AI one, not SPECTRE — was fetched). ENISA was re-checked directly
via the EUVD API as requested: `EUVD-2026-63693` returns `dateUpdated: Aug 22, 2026`,
`exploitedSince: Aug 21, 2026`, `baseScore 10.0`, references only the MSRC page — the entry is exact.
`CVE-2026-73570` → `EUVD-2026-58069`, published Aug 13, `exploitedSince Aug 18` — also exact.
Red Hat was re-checked against the Hydra security-data API and the CSAF/VEX document: 11 fixed
release rows, 2 `known_not_affected` rows with flags `component_not_present` (JBoss EAP Expansion
Pack) and `vulnerable_code_not_present` (RHSSO 7). **The roll-up's correction of the 19 August
operational entry is accurate and fairly stated.**

### Prior-iteration delta

The iteration-2 residual **is fixed and is accurate.** Against `pages/cash-zurich.txt`, cash.ch
carries "Den betroffenen Unternehmen entstanden durch Betriebsunterbrüche, Datenverluste und
Sanierungen Schäden in Millionenhöhe" and no total — matching the note's "cash.ch quantifies
nothing, describing damages from business interruption, data loss and remediation only as running to
millions". Against `pages/20min-zurich.txt`, 20 Minuten carries "über 100 Millionen Franken" and
"4,5 Millionen Franken" paid by three non-Swiss firms — matching "This entry carries only the two
20 Minuten figures and attributes both to it", and the body cites 20 Minuten for both. The CHF 130 m
figure is Netzwoche's, correctly described as "a third outlet not cited here". One residual wording
wobble in that same note is logged as F11.

---

### Citation does not support the claim

**F1 — `weekly-w34-two-charge-sheets-named-switzerland`: the charged period and the Nefilim family are
cited to cash.ch, which carries neither — and neither does the entry's only other Zurich source.**

Body: *"…appeared before Zurich District Court on 2026-08-17, charged in connection with ransomware
attacks between December 2018 and May 2020 using LockerGoga, MegaCortex and Nefilim; the prosecution
seeks twelve years' imprisonment and a twelve-year entry ban ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362))."*

I read the saved cash.ch body and re-fetched the page. cash.ch names «Lockergoga», «Megacortex» and a
third tool «RMS» — it does **not** name Nefilim — and it gives **no date range** at all for the
attacks. Substring test over the two cited Zurich sources:

| | LockerGoga | MegaCortex | Nefilim | "Dezember 2018" | "Mai 2020" |
|---|---|---|---|---|---|
| cash.ch | yes | yes | **no** | **no** | **no** |
| 20 Minuten | **no** | **no** | **no** | **no** | **no** |

The facts are true — this pipeline's own operational entry
`2026-08-18/zurich-trial-lockergoga-megacortex-nefilim-swiss-victims` attributes both to **Netzwoche**
("The charge sheet covers attacks between December 2018 and May 2020 involving the ransomware families
LockerGoga, MegaCortex and Nefilim ([Netzwoche, 2026-08-17](…))") — but Netzwoche is absent from this
entry's `sources[]`. The same unsupported pair also appears in the frontmatter `title`
("a Zurich indictment over LockerGoga, MegaCortex and Nefilim"), in the `summary` ("ransomware attacks
between December 2018 and May 2020 using LockerGoga, MegaCortex and Nefilim"), in `entities`
(`malware:nefilim`, with no cited source naming it), and in the closing paragraph
("the Zurich operation ended in May 2020"). Fix: add the Netzwoche record and attach it to those
clauses, or drop Nefilim and the date range from this entry.

**F2 — `weekly-w34-looking-ahead`: the three malware families are cited to 20 Minuten, which names none
of them.**

Body: *"The court intends to deliver judgment on that date in the LockerGoga, MegaCortex and Nefilim
trial ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489))."*

20 Minuten supports the verdict date exactly — "Das Gericht will das Urteil am Donnerstag,
10. September, fällen" — and supports "Four named Swiss companies are victims in this case" and the
inadmissibility argument. It contains none of the strings "LockerGoga", "MegaCortex" or "Nefilim".
Same remediation family as F1.

**F5 — `weekly-w34-ai-bought-throughput-not-capability`: both AI tools placed on the "management
server"; Talos places one of them on the C2 server, and calls the other a code scanner, not a
pen-test tool.**

Body: *"…and reports two AI tools installed on the actor's own management server — a source-code
vulnerability-scanning framework … and an AI-driven penetration-testing tool used to scan servers and
run proof-of-concept exploits."* Summary: *"a management server carrying two AI penetration-testing
tools"*.

Fetched `https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/`
this iteration. Talos: "they utilize DeepAudit for source code vulnerability scanning … we did observe
the framework installed on their **management server**" and, separately, "Talos observed the threat
actor installing the PentestGPT framework on their **C2 server**". Two different hosts in Talos's own
wording. The summary additionally labels DeepAudit a "penetration-testing tool", which Talos does not
— the body gets this right, so the summary contradicts the body as well.

**F6 — `weekly-w34-ai-bought-throughput-not-capability`: the frontmatter summary inverts Insikt's
quantifier from a floor to a ceiling.**

Summary: *"…applying to more than 1,100 companies **at up to 60 positions a day**…"*. The body says
the opposite and is correct: *"sometimes at a rate of at least 60 positions a day"*. Recorded Future
(fetched this iteration): "the operators have applied to **at least 60 positions per day** across
multiple job platforms". "Up to 60" caps a figure the source floors; the rendered brief shows the
summary.

### Unsupported / hallucinated facts

**F3 — `weekly-w34-clop-windchill-status`: "six days earlier" for General Electric's statement is in no
cited source and is contradicted by this pipeline's own record.**

Summary: *"one outlet observing the leak site states General Electric is no longer listed on it, **six
days after** the company said it was assessing the group's claims"*. Body: *"…and General Electric had
said only **six days earlier** that it was assessing the group's claims."*

The only source on that paragraph is GovInfoSecurity, dated **2026-08-17** (byline "Tiffany Wang •
August 17, 2026" in the saved body); it carries the GE-removal sentence but no date for any GE
statement. I fetched the article this pipeline's own operational entry uses for the GE statement,
`https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/`
— byline "By Sergiu Gatlan **August 17, 2026** 07:25 AM", "a GE spokesperson said the company is aware
of the claim and is 'working to assess the potential issue'". Entry
`2026-08-19/clop-windchill-custom-implant-reverse-engineered` records it the same way: "General
Electric confirmed on 2026-08-17 that it is assessing Cl0p's claims". Statement and removal report are
**the same day**, not six days apart. Fix: drop the interval or replace it with the actual same-day
observation, which is a sharper point anyway.

**F4 — `weekly-w34-vuln-status-rollup`: CVE-2026-19478 (GitLab) is filed under "Critical, no
exploitation reported" and named in the takeaway as having "no exploitation signal"; it was reported
exploited inside the window.**

Section heading: *"### Critical, no exploitation reported"*, containing *"**CVE-2026-19478 — GitLab,
CVSS 9.4**, with the companion CSRF flaw CVE-2026-19650 at 7.1."* Takeaway: *"The flaws that would
actually have needed out-of-band handling this week were the ones with **no exploitation signal** and a
mechanic that forces the timeline anyway…"*

Two in-window records say otherwise, both fetched this iteration:

- SecurityWeek, **20 August 2026** (`https://www.securityweek.com/critical-gitlab-flaw-exploited-shortly-after-disclosure/`),
  headline "Critical GitLab Flaw Exploited Shortly After Disclosure": "Threat actors started
  exploiting a critical-severity GitLab vulnerability roughly two days after public disclosure,
  attack surface management company WatchTowr warns. Tracked as CVE-2026-19478 (CVSS score of 9.4)…"
- NCSC-CH Cyber Security Hub post **12856** (fetched via `tools/fetch_source.py ncsc-csh post 12856`),
  created 2026-08-18, `lastModified 2026-08-21`, history entry reason **"Updated with claims of active
  exploitation"**, content: "**Update 21.08.2026** — **Current exploitation status**: Actively
  exploited". This is the same NCSC-CH hub the entry already cites twice (posts 12844 and 12860).

This is not a placement quibble: it inverts the bullet's meaning for a reader triaging self-managed
GitLab, and it also means the roll-up's own "six flaws crossed the line" tally is short. Fix: move the
bullet into "Newly exploited or newly catalogued this week" with the SecurityWeek and NCSC-CH records
cited, and re-word the takeaway clause that names it.

### Claims missing inline citation

**F7 — `weekly-w34-vuln-status-rollup`, TrueConf bullet: Kaspersky-derived facts hang off a KEV
citation, and Kaspersky is not in `sources[]` at all.**

Bullet: *"**CVE-2026-72529 and CVE-2026-72530 — TrueConf Server.** Both catalogued 2026-08-20
([CISA KEV catalog v2026.08.21, 2026-08-21](…known_exploited_vulnerabilities.json)). Chained, they take
an unauthenticated attacker from port 4307/TCP — **open by default per the vendor's documentation** — to
command execution as SYSTEM. **Fixed 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5**, two months before the
listing, **with the coordinating CNA reporting exploitation since at least July**."*

Checked against the fetched catalogue (`pages/kev.txt`, v2026.08.21): the KEV records confirm
`dateAdded 2026-08-20` and the port-4307 wording, and carry **nothing** about the fix date, the fixed
versions, the vendor's documentation, or a July exploitation start. Checked against Kaspersky ICS CERT
(`pages/kaspersky-icscert.txt`): it carries "released on June 18, 2026", "versions 5.3.9, 5.4.9, and
5.5.5" and "port 4307/TCP (open by default, according to TrueConf documentation)" — but the string
"July" does not appear anywhere on that page. The July claim traces to **Kaspersky Securelist**, cited
by `2026-08-23/trueconf-server-kev-head-mare-trojanized-installer` but absent here. The Kaspersky ICS
CERT record is absent from this entry's `sources[]` entirely. (The same bullet pattern is repeated,
less severely, on the `misp-stix` trio bullet and on "Switzerland's NCSC and France's CERT-FR both
relayed the identifier on 2026-08-17" — CERT-FR's CERTFR-2026-AVI-1035 is named in the sourcing note
and I confirmed it is dated 17 August 2026 and references the CVE-2026-69414 bulletin of 14 August,
but its URL is in no `sources[]` record.) Fix: add the Kaspersky ICS CERT record and attach it to the
mechanism/fix clauses; either cite Securelist for the July claim or drop it.

### Missed angles

**F8 — Cisco Crosswork and Secure Workload: eight critical CVEs, three at CVSS 10.0, in-window and
absent from the entire store.**

NCSC-CH Cyber Security Hub post **12867**, published **2026-08-21T14:00Z** (fetched this iteration):
"[Advisory] Cisco: Multiple Critical Vulnerabilities in Crosswork and Secure Workload" —
CVE-2026-20030 (10.0, SQL injection), CVE-2026-20357 (10.0, missing authentication for critical
function), CVE-2026-20358 (10.0), CVE-2026-20359 (9.9), CVE-2026-20315 (10.0), CVE-2026-20317 (10.0),
CVE-2026-20318 (9.6), CVE-2026-20231 (9.9), with vendor advisories
`cisco-sa-hardening-crosswork-UzDTU9Vh` and `cisco-sa-hardening-csw1-shSvndWP`. `grep -rl` over
`entries/` finds no coverage of Crosswork anywhere, and `prior_coverage.json` does not contain the
string "Crosswork". The Swiss national CERT advised its own constituency on it inside the week; the
roll-up's critical tail does not mention it. Search query: `Cisco Crosswork Secure Workload August
2026 critical CVE-2026-20030 CVE-2026-20315 advisory`.

**F9 — NCSC-CH flipped CVE-2026-19490 (NetScaler) to "Actively exploited" on 2026-08-21, contradicting
the CERT-EU advisory the roll-up cites and the entry whose whole subject is that kind of divergence.**

NCSC-CH hub post **12863**, created 2026-08-20, `lastModified 2026-08-21`, edit reason "Added
additional information (Update 21.08.2026)", content: "**Update 21.08.2026** — **Current exploitation
status**: Actively exploited", sourced to a single X post. Against that: CERT-EU advisory 2026-010
(fetched, dated 19/08/2026) records no exploitation, and Rapid7's 19 August analysis states no
in-the-wild exploitation observed. The roll-up files CVE-2026-19490 under "Critical, no exploitation
reported" and the takeaway names it as one of the two flaws with "no exploitation signal". I am not
asking for the NCSC-CH claim to be adopted — its basis is a single social-media post, which this
pipeline's own sourcing rules treat with suspicion — but this is precisely the material
`weekly-w34-exploited-is-now-a-per-authority-opinion` exists to carry, and the Swiss authority is the
one the constituency reads. Surface it as a fifth divergence there, or add a hedged line to the
roll-up bullet. Search query: `CVE-2026-19490 NetScaler exploitation NCSC-CH security hub 21 August
2026`.

### Classification missing / inconsistent

**F10 — `weekly-w34-the-disclosure-arrived-the-facts-did-not`: `reliability: A` / `credibility: 1` is
not supported by the entry's own sourcing.**

Frontmatter: `classification: {reliability: A, credibility: 1}`. Of the seven `sources[]` records,
only CERT.LV is in `sources/sources.json` at reliability A (`cert-lv`, A, standard). Four of the seven
publishers appear nowhere in `sources.json` at all: `insideparadeplatz.ch` (a Zurich finance
commentary blog — the org profile names "`A` on a lone blog/forum post" as the canonical F17 case),
`escudodigital.com`, `news.inbox.eu` (a mail-portal news aggregator republishing BB.LV), and
`lenouvelliste.ch`. On credibility, the entry's own `sourcing_note` concedes the single-outlet basis
for two of the five cases: "in the HWZ case no source other than the extortion group's own leak-site
listing connects any named provider to the school", and the Castilla-La Mancha case rests on Escudo
Digital alone. Credibility `1` ("confirmed by other sources") overstates that. Suggested: `B` / `2`.
(The first-party disclosures — AK Oberösterreich's member notice, the Martigny-Combe communiqué,
CERT.LV — are genuinely A-grade and are why this is a calibration finding rather than a sourcing one.)

### Editorial / less-is-more flags (advisory)

**F11 — `weekly-w34-two-charge-sheets-named-switzerland`, `sourcing_note`: antecedent collision in the
(otherwise correct) rewritten damage/ransom paragraph.**

*"…a third outlet not cited here reports the prosecution figure as above CHF 130 million, and the
referenced operational entry carries both without resolving them. On ransoms **the same outlet**
reports CHF 4.5 million paid by three non-Swiss victims, while **the third outlet** values the largest
single payment on a different basis…"*

"The same outlet" is meant to be 20 Minuten (correct on the facts — 20 Minuten carries the CHF 4.5 m
figure, Netzwoche the 450-bitcoin valuation), but the nearest antecedent is "a third outlet" one
sentence earlier, so the sentence reads as attributing both ransom figures to Netzwoche. Naming
20 Minuten explicitly resolves it. No truth defect; leave it if the main agent prefers.

---

### What I checked and found clean (so a later iteration need not redo it)

- All 51 URLs resolve; none is a homepage, listing index, category landing or NVD/MITRE per-CVE page.
- 28/28 `evidence[]` and inline quotes are contiguous verbatim substrings (Huntress ×3, Talos ×2,
  Check Point ×2, ReliaQuest ×2, VenariX, Wiz, Kaspersky ×2, Bitdefender ×2, Red Canary, NCSC UK ×4,
  GovInfoSecurity ×2, Berlin ×3, Sophos ×3, DOJ ×1).
- ENISA (EUVD API, both records), CISA KEV (all six CVE `dateAdded` values against the fetched
  v2026.08.21 catalogue), Red Hat (Hydra + CSAF VEX), Oracle (943 patches; the three CVSS 10.0 rows
  with PR:None/UI:None), GitLab (9.4 / 7.1, 18.2 onward, GitLab.com and Dedicated already patched),
  CERT-EU (9.3, the 14.1-43.56 / 13.1-61.28 SAML precondition verbatim), GeoServer (14 Aug, "urgent
  update for production systems"; NCSC-CH post 12844's 17 August update independently carries all
  three fixed versions, so that clause is fully covered), NCSC-CH post 12860 (both WordPress CVEs at
  9.8), Rust Project (86 / 90 / 107 minutes, account locked), Recorded Future (1,100 / 22 personas /
  "even when the LLM is wrong"), the five-agency advisory (I did extract the ic3.gov PDF text: every
  snap7/ladder-logic/scanning-service claim checks out verbatim, and the AI-tooling sentence indeed
  carries no confidence qualifier while the reconnaissance assessment does — the entry's sourcing note
  is right on both), EC CRA (11 September 2026, "manufacturers are required to report actively
  exploited vulnerabilities", 19 days), OSV (last_affected 2026.7.8, two fix commits), DOJ (the
  victim-count sentence is verbatim; Switzerland appears in both lists; password spraying and the
  $20 m figure confirmed), Sophos (86 / 34 / +4 / 38 / 30 / 26 / 35 all exact), Check Point
  StopAndProtect ("close to 2,000 compromised WordPress domains"; MU-plugin behaviour verbatim),
  Acronis (Sheets API v4, per-victim tabs, HACKERAI C2 Agent → Gists), Red Canary (four debuts, three
  using dead-drop resolution, two blockchain, CastleRAT → steamcommunity), Talos SPECTRE (RTCore64 /
  DBUtil_2_3, 13-version offset table, the three callback classes, the named EDR products, "medium
  confidence" on the rootkit, "Method 1/2/3").
- All 38 distinct `entities` keys resolve in `entities/registry.yaml`.
- `techniques: []` on `weekly-w34-berlin-landesnetz-nine-days-no-vector` is honest: the Senate
  Chancellery release says "Aus ermittlungstaktischen Gründen können derzeit keine weiteren konkreten
  Informationen zu Ausmaß und Hintergründen gegeben werden", and neither Berlin.de item nor
  Tagesspiegel describes any attacker behaviour. Mapping nothing is correct.
- Priority calibration (6 high / 8 notable / 0 critical) is right; nothing here clears the
  stop-and-act-now bar, and nothing `notable` plainly clears the critical bar.
- W-PD-1: every entry answers at least one of the three questions. The weakest is
  `two-charge-sheets`, which answers (c) explicitly and carries a four-named-Swiss-victim nexus.
- The three deliberate W32/W33 distinctions hold on their content, not merely by assertion.
- Thirteen empty `actions[]` are correct; the single NetNTLMv1 action is concrete, self-contained and
  derived from the finding's own mechanics — no F18.
- No IOCs (regex sweep for hashes, IPv4, defanged URLs finds nothing), English throughout, no vanity
  metrics.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 4, advisory: 1)

### Findings summary (machine-readable)

```yaml
- code: F1
  category: claim-not-supported
  section: weekly-incidents-recap
  item: "weekly-w34-two-charge-sheets-named-switzerland"
  url_or_quote: "charged in connection with ransomware attacks between December 2018 and May 2020 using LockerGoga, MegaCortex and Nefilim ... ([cash.ch, 2026-08-17](https://www.cash.ch/news/top-news/hacker-steht-nach-attacke-auf-stadler-rail-und-andere-firmen-vor-gericht-961362))"
  summary: "cash.ch names Lockergoga, Megacortex and RMS but NOT Nefilim, and gives no date range; 20 Minuten (the only other Zurich source) names none of the three families and no date range. Both facts trace to Netzwoche, which the operational entry 2026-08-18/zurich-trial-... cites but which is absent from this entry's sources[]. Same unsupported pair also in title, summary, entities (malware:nefilim) and the closing 'the Zurich operation ended in May 2020'. Add the Netzwoche record and re-attach, or drop."
- code: F2
  category: claim-not-supported
  section: weekly-looking-ahead
  item: "weekly-w34-looking-ahead"
  url_or_quote: "the LockerGoga, MegaCortex and Nefilim trial ([20 Minuten, 2026-08-17](https://www.20min.ch/story/ransomware-angriffe-auf-schweizer-firmen-12-jahre-haft-gefordert-103618489))"
  summary: "20 Minuten supports the 10 September verdict date, the four Swiss victims and the inadmissibility argument, but contains none of the strings LockerGoga, MegaCortex or Nefilim. Cite Netzwoche for the family names or drop them from the clause."
- code: F3
  category: hallucinated-fact
  section: weekly-long-running
  item: "weekly-w34-clop-windchill-status"
  url_or_quote: "General Electric had said only six days earlier that it was assessing the group's claims"
  summary: "No cited source carries any interval. GovInfoSecurity is dated 2026-08-17; GE's 'working to assess the potential issue' statement was published the same day (BleepingComputer, 2026-08-17 07:25 AM), and this pipeline's own entry 2026-08-19/clop-windchill-custom-implant-reverse-engineered records 'General Electric confirmed on 2026-08-17'. Same claim in the frontmatter summary ('six days after the company said it was assessing'). Drop the interval or replace with the same-day observation."
- code: F4
  category: hallucinated-fact
  section: weekly-vuln-rollup
  item: "weekly-w34-vuln-status-rollup"
  url_or_quote: "### Critical, no exploitation reported ... **CVE-2026-19478 — GitLab, CVSS 9.4**"
  summary: "CVE-2026-19478 was reported exploited in-window: SecurityWeek 2026-08-20 'Critical GitLab Flaw Exploited Shortly After Disclosure' (WatchTowr, exploitation ~2 days after disclosure), and NCSC-CH Cyber Security Hub post 12856 edited 2026-08-21 with reason 'Updated with claims of active exploitation' -> 'Current exploitation status: Actively exploited'. The takeaway also names it among flaws with 'no exploitation signal'. Move the bullet to 'Newly exploited or newly catalogued this week' with both records cited and re-word the takeaway clause."
- code: F5
  category: claim-not-supported
  section: weekly-research
  item: "weekly-w34-ai-bought-throughput-not-capability"
  url_or_quote: "reports two AI tools installed on the actor's own management server"
  summary: "Talos (https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/) places DeepAudit on 'their management server' and PentestGPT on 'their C2 server' — two different hosts. The frontmatter summary additionally calls both 'AI penetration-testing tools' while Talos describes DeepAudit as source-code vulnerability scanning; the body gets this right, so the summary also contradicts the body."
- code: F6
  category: claim-not-supported
  section: weekly-research
  item: "weekly-w34-ai-bought-throughput-not-capability"
  url_or_quote: "applying to more than 1,100 companies at up to 60 positions a day"
  summary: "Recorded Future says 'the operators have applied to at least 60 positions per day'; the body correctly says 'at least 60 positions a day'. The frontmatter summary turns a floor into a ceiling and contradicts its own body. Change 'up to' to 'at least'."
- code: F7
  category: missing-citation
  section: weekly-vuln-rollup
  item: "weekly-w34-vuln-status-rollup (TrueConf bullet)"
  url_or_quote: "Fixed 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5, two months before the listing, with the coordinating CNA reporting exploitation since at least July."
  summary: "Only citation on the bullet is the CISA KEV catalogue, which carries the dateAdded and the port-4307 wording but nothing about the fix date, fixed versions, vendor documentation or a July exploitation start. Kaspersky ICS CERT carries the first three but the string 'July' does not appear on that page and the record is absent from sources[]; the July claim traces to Kaspersky Securelist, cited only by the operational entry. Add the Kaspersky ICS CERT record and attach it; cite Securelist for July or drop the clause."
- code: F8
  category: missed-angle
  section: weekly-vuln-rollup
  item: "Cisco Crosswork / Secure Workload — eight critical CVEs, three at CVSS 10.0"
  url_or_quote: "NCSC-CH Cyber Security Hub post 12867, published 2026-08-21T14:00Z"
  summary: "CVE-2026-20030, -20357, -20358 (10.0), -20315, -20317 (10.0), -20359, -20231 (9.9), -20318 (9.6); vendor advisories cisco-sa-hardening-crosswork-UzDTU9Vh and cisco-sa-hardening-csw1-shSvndWP. In-window, relayed by the Swiss national CERT, and absent from the entire entry store and from prior_coverage.json. Search: 'Cisco Crosswork Secure Workload August 2026 critical CVE-2026-20030 CVE-2026-20315 advisory'."
- code: F9
  category: missed-angle
  section: weekly-multi-day
  item: "weekly-w34-exploited-is-now-a-per-authority-opinion / weekly-w34-vuln-status-rollup"
  url_or_quote: "NCSC-CH Cyber Security Hub post 12863, lastModified 2026-08-21: 'Update 21.08.2026 — Current exploitation status: Actively exploited'"
  summary: "The Swiss authority flipped CVE-2026-19490 (NetScaler) to actively exploited on 21 August on the basis of a single X post, while CERT-EU advisory 2026-010 (19 August, cited by the roll-up) and Rapid7 record no exploitation — a fifth per-authority divergence, in the constituency's own national feed, in the same week as the entry devoted to that exact phenomenon. The roll-up meanwhile files the CVE under 'Critical, no exploitation reported'. Surface the divergence (hedged on the weak basis) rather than adopting the flag."
- code: F10
  category: classification
  section: weekly-sector-patterns
  item: "weekly-w34-the-disclosure-arrived-the-facts-did-not"
  url_or_quote: "classification: {reliability: A, credibility: 1}"
  summary: "Only CERT.LV is an A-tier record in sources/sources.json; insideparadeplatz.ch (a finance commentary blog), escudodigital.com, news.inbox.eu and lenouvelliste.ch appear nowhere in sources.json. The entry's own sourcing_note concedes single-outlet sourcing for the HWZ and Castilla-La Mancha cases, which is inconsistent with credibility 1 ('confirmed by other sources'). Suggested B / 2."
- code: F11
  category: editorial-advisory
  section: weekly-incidents-recap
  item: "weekly-w34-two-charge-sheets-named-switzerland (sourcing_note)"
  url_or_quote: "a third outlet not cited here reports the prosecution figure as above CHF 130 million ... On ransoms the same outlet reports CHF 4.5 million paid by three non-Swiss victims, while the third outlet values the largest single payment on a different basis"
  summary: "Facts are correct (CHF 4.5m is 20 Minuten's, the 450-bitcoin valuation is Netzwoche's) but 'the same outlet' sits immediately after 'a third outlet', so it reads as attributing both ransom figures to Netzwoche. Name 20 Minuten explicitly. Advisory only."
```
