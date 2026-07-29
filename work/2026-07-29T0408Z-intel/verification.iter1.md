**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-07-29T05:06:07Z · ended_at=2026-07-29T05:29:35Z · duration_seconds=1408
**Self-telemetry:** urls_checked=24 · webfetch_calls=7 · bridge_fetches=21 · websearch_calls=2

## Verification report — 2026-07-29T0408Z-intel (iteration 1)

Read cold. Every inline source URL on all 11 entries was fetched in this iteration (Siemens CSAF ×2, CISA
ICSA ×2 + AA26-097A via the bridge, openwall + openssl-library.org raw, seclists, BSI CSAF, JetBrains,
MITRE CVE API ×3, live CISA KEV, ZDI, VulnCheck (jina), Rapid7, Securelist, Talos, Sophos, LevelBlue,
StateScoop, Cybersecurity Dive, aradon.ro, radioromania.ro, sportarad.ro), plus OSV, the GitHub advisory
record GHSA-5v3c-9g74-93w7, the GitHub PoC repo behind the Desigo CC claim, `entities/registry.yaml`,
`state/cves_seen.json`, `work/<run>/prior_coverage.json`, the six research/deep-read findings YAMLs and
`triage.json`. No URL was unreachable and none is generic — **no F1 and no F2 findings**.

The run is strong: every mechanism claim on the Rapid7, Talos, Sophos, LevelBlue, ZDI, Siemens-CSAF and
Romanian-press material checked out verbatim, including the harder ones (the decompiled
`authenticateRemoteApplication` diff Take 146→158, the CSAF `remediations` split proving only Desigo CC V7
carries `none_available`, the `NtCreateDirectoryObjectEx`/`NtCreateSymbolicLinkObject` hunting sentence, the
`datePublished 2026-07-27T14:07:50.000Z` metadata, the 16-row NightLedger command table, and every Talos
percentage including "For the second quarter in a row"). Dedup is clean. Findings below are concentrated in
citation adjacency and in frontmatter that outruns its own body.

### Citation does not support the claim

**F1 — Desigo CC: the public-exploit claim is attributed to CISA, and no cited source states it.**
Entry: `entries/2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed.md`.
Body claim, verbatim: *"Siemens is affected because Desigo CC, its building-management platform, vendors the
library for that parsing path, and CISA's republication notes a public command-execution proof-of-concept
already exists ([CISA, 2026-07-28](https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-01))."*
The same claim propagates to the headline (*"for an OpenSSL CMS overflow with a public exploit"*), the
summary (*"and a public command-execution proof-of-concept exists"*), `cves[0].status: [poc-public, ...]`,
`tags: [... poc-public ...]`, and action 1 (*"since a public command-execution exploit already exists"*).
What the cited page says: I fetched `https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-01` with
`python3 tools/fetch_source.py cisa page` (173 non-empty lines) and grepped it — zero occurrences of
"proof", "PoC", "public exploit" or "exploit code". The page carries an explicit *Advisory Conversion
Disclaimer*: *"This ICSA is a verbatim republication of Siemens ProductCERT SSA-734552 …"*. The run's own
saved CSAF (`work/2026-07-29T0408Z-intel/icsa-26-209-01.json`) likewise contains no "proof"/"poc" string.
Siemens' own CSAF (`ssa-734552.json`, fetched) has no PoC statement. OpenSSL's advisory (fetched both at
the cited openwall mirror and at `https://openssl-library.org/news/secadv/20260127.txt`) has none either.
The fact is *true* — the run's `findings.S1.yaml` cites
`https://github.com/guiimoraes/CVE-2025-15467`, which I fetched and which is titled *"Command Execution PoC
for OpenSSL Stack buffer overflow CVE-2025-15467"* — but that source was dropped from the entry's
`sources[]`. Remediation: cite the PoC source for that clause (and for `poc-public`), or remove the CISA
attribution and the `poc-public` status/tag.

**F2 — Minnesota: the South St. Paul facts, and Braham's lifted advisory, are cited to StateScoop, which
carries neither.** Entry: `entries/2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack.md`.
(a) Body, verbatim: *"… South St. Paul identified impact to certain automated controls and reported no major
effect on drinking-water or wastewater treatment operations after invoking contingency procedures; Braham's
water plant went offline … ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/))"*
— one trailing citation claiming all three utilities' statements. I fetched the StateScoop article and
grepped the extracted text: **0 occurrences of "South St", "automated control" or "contingency"**. The facts
are in the co-cited Cybersecurity Dive piece, verbatim: *"authorities in South St. Paul, Minn., said they
identified a cyberattack on Monday that impacted certain automated controls. After implementing contingency
procedures, officials confirmed no major impact to drinking and wastewater treatment operations."* The
summary repeats it (*"South St. Paul reported impact to certain automated controls"*). Remediation: attach
the Cybersecurity Dive citation to that clause.
(b) Same paragraph: *"Braham did ask residents to minimise water use while its tower held a limited
quantity, **lifting the request once the plant was back online**"*. StateScoop says only *"A second notice
later that day noted that the plant was back online, explaining that the outage had been the result of 'a
malicious cyber-attack …'"* — it does not state the minimise-use request was lifted.

**F3 — TeamCity: "the agent-polling protocol … by design does not require authentication" is not what
JetBrains says, and the Triage discriminator is built on it.**
Entry: `entries/2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce.md`.
Body, verbatim: *"The reachable surface is the agent-polling protocol — the channel distributed build agents
use to check in with the central server for job assignments and configuration — **which by design does not
require authentication**, so there is no credential, session, or user interaction standing between a
network-reachable server and command execution ([JetBrains, 2026-07-27](https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/))"*.
Triage line, verbatim: *"the agent-polling endpoint is *supposed* to receive a steady stream of
unauthenticated check-ins, so volume alone tells you nothing"*.
What the cited page says (I fetched it and extracted the *Technical details* section): *"This vulnerability
affects TeamCity servers that are reachable over HTTP(S). **Exploitation of this vulnerability does not
require authentication.** An unauthenticated attacker could exploit the vulnerability via the TeamCity agent
polling protocol to bypass authentication checks and execute arbitrary operating system commands with the
privileges of the TeamCity server process."* That is a statement about *exploitation of the flaw*, not about
the protocol's design; nothing on the page says the agent-polling channel is unauthenticated as designed
(the advisory's own framing is that the flaw *bypasses* authentication checks). The Triage line converts the
unsupported premise into a live triage rule — "volume alone tells you nothing" because unauthenticated
check-ins are expected — which is check-10's "a `**Triage:**` discriminator that does not follow from the
cited mechanism". Remediation: restate as "exploitation requires no authentication" and rebuild the Triage
discriminator on the source-address-set / process-lineage grounds the entry already has.

### Unsupported / hallucinated facts

**F4 — Minnesota: frontmatter asserts the attribution and the vector the body explicitly denies.**
Entry: `entries/2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack.md`.
The body is unambiguous: *"No authority has named an actor. The Center for Internet Security's senior
director of threat intelligence stated the Minnesota attacks have not yet been attributed to any particular
party and that it is unclear whether the programmable logic controllers CISA had warned about were
involved"* (verified verbatim in StateScoop: *"affirmed that the Minnesota attacks have not yet been
attributed to any particular party, and that 'it is unclear' whether the attacks involved the programmable
logic controllers CISA warned about"*), and *"Treating it as attribution would be reading the calendar as
evidence."* Two frontmatter fields contradict that:
(a) `tags: [ot-ics, nation-state]` — the `nation-state` tag attaches to *this incident*, whose attribution
the entry says is open. Nothing in any cited source attributes the Minnesota event to a state actor.
(b) `affected_products: ["Rockwell Automation CompactLogix", "Rockwell Automation Micro850", "Schneider
Electric Modicon M340", "Siemens SIMATIC S7-1200"]` — I fetched AA26-097A; those four families are named
there as targets of the *separate* Iranian campaign (*"Rockwell Automation: CompactLogix and Micro850 PLCs /
Schneider Electric: BMX P34/Modicon M340 PLCs / Siemens: S7-1200 series PLCs"*), and no source names any
controller model involved in Minnesota. `entries/2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion.md`
already carries exactly this list, which is where it belongs. Note also a product-name drift: the cited
source says "S7-1200 series PLCs" and the store's existing value is "Siemens S7-1200", while this entry
writes "Siemens SIMATIC S7-1200".

**F5 — Langflow: `poc-public` has no basis in any cited source.**
Entry: `entries/2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev.md`.
Frontmatter: `cves[0].status: [exploited, no-patch, poc-public]` and `tags: [..., poc-public]`.
Sources fetched: ZDI-26-035 publishes no exploit and its only mitigation is *"Given the nature of the
vulnerability, the only salient mitigation strategy is to restrict interaction with the product"*; the MITRE
record `CVE-2026-0769` (fetched) references only the ZDI advisory; VulnCheck says *"we've seen attackers
gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027"* — attacker exploitation
in the wild, not a public proof-of-concept. Contrast the Check Point update, where `poc-public` **is**
correctly supported: Rapid7's page links its PoC at `https://github.com/sfewer-r7/CVE-2026-16232` (confirmed
in the page's embedded content). Remediation: drop `poc-public` from status and tags on this entry.

**F6 — three `evidence[]` quotes are not contiguous verbatim substrings of the pages they cite.**
All three are meaning-preserving and none misrepresents its source, but each fails the copyable-unchanged
rule, so a machine consumer verifying evidence by substring match will reject them.
(a) `entries/2026-07-29/cve-2026-59243-airflow-fab-azure-ad-jwt-signature-bypass.md` — quote
`"Credit: MalHyuk (finder), Jarek Potiuk (remediation developer)"`. The oss-sec post (fetched and
tag-stripped) has three separate lines: `Credit:` / `MalHyuk (finder)` / `Jarek Potiuk (remediation
developer)`. The comma is inserted.
(b) `entries/2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed.md` — quote
`"Stack buffer overflow in CMS AuthEnvelopedData parsing (CVE-2025-15467) === Severity: High"`. The openwall
page (fetched raw) has the heading on line 162, a 71-character `=` underline on line 163, a blank line, then
`Severity: High` on line 165. `===` is a compression of the underline.
(c) `entries/2026-07-29/stac4749-teams-vishing-certificate-pinned-golang-chaos.md` — quote
`"Sophos analysts have found no evidence linking STAC4749 activity to that group. Instead, limited
hands-on-keyboard artifacts suggest a Russian-language connection... However, there is insufficient evidence
for attribution."` The `...` elides *"For example, Sophos analysts observed a mistyped command (вшк) that is
consistent with the operator attempting to enter "dir" while using a Russian keyboard layout."* (confirmed
present in the fetched page).

### Claims missing inline citation

**F7 — UVVG Arad: the entire Qilin claim is uncited and unsourced.**
Entry: `entries/2026-07-29/uvvg-arad-romania-university-cyberattack-qilin-claim.md`.
The claim appears in the title (*"a Qilin leak-site listing is the only thing linking an actor to it"*), the
summary (*"the Qilin ransomware operation listed the university on its leak site with an estimated attack
date of 2026-07-26"*), the body (*"The Qilin ransomware operation listed the university on its leak site
with an estimated attack date of 2026-07-26, two days before the university's disclosure"*), and in
`entities: [… actor:qilin]`, `techniques: [T1486]` and `tags: [ransomware, data-breach]` — with **no inline
citation and no `sources[]` record**. I fetched all three cited sources (aradon.ro, radioromania.ro,
sportarad.ro): none contains "Qilin" or "ransomware", which the entry itself states. So no reader can verify
the listing, the group name, or the 2026-07-26 attack date. The source exists and the run had it: the run's
`findings.S4.yaml` records it as a corroborating source —
`https://www.ransomware.live/id/VW5pdmVyc2l0YXRlYSBkZSBWZXN0IOKAnlZhc2lsZSBHb2xkaciZ4oCdIGRpbiBBcmFkQHFpbGlu`
(ransomware-live, reliability C in `sources/sources.json`) — and seven already-published entries cite
ransomware.live, so the convention is established. Remediation: add the mirror as a corroborating
`sources[]` record and cite it at the claim (the entry's careful "claim, not fact" framing is otherwise
exactly right and should be kept).

**F8 — TeamCity: the CVE-2023-42793 / Russian SVR precedent carries no citation.**
Summary, verbatim: *"the same product's CVE-2023-42793 was exploited at scale by Russian SVR-attributed
actors in 2023."* Body, verbatim: *"CVE-2023-42793 in TeamCity was exploited at scale in 2023 against
internet-facing servers, an event significant enough to draw a joint advisory naming Russian SVR-attributed
actors."* No inline link, and neither cited source carries it — I fetched the JetBrains advisory and the
MITRE record for CVE-2026-63077 and neither mentions CVE-2023-42793. A second CVE id plus a state
attribution plus an implied joint advisory needs a link (the joint advisory itself is the obvious citation).

### Classification missing / inconsistent

**F9 — Airflow: `credibility: 1` contradicts the entry's own sourcing note.**
Entry: `entries/2026-07-29/cve-2026-59243-airflow-fab-azure-ad-jwt-signature-bypass.md`,
`classification: {reliability: A, credibility: 1}`. The sourcing_note says, verbatim: *"Two publishers, but
they are not independent assessments of the same facts: BSI CERT-Bund's advisory is a republication of
Apache's disclosure, so the technical claims rest on Apache's own account of its own codebase."* I fetched
the BSI CSAF (`bsi-csaf WID-SEC-2026-2551`) and confirmed it: its only external references are the same
oss-sec post and the Apache GitHub PR, and it carries no scores block. Admiralty credibility `1`
("confirmed by other sources") is inconsistent with an entry that states there is no independent
corroboration; `2` is the correct code. Reliability `A` on Apache's own security team is fine. (For
contrast, the Siemens entry's `A/1` **is** defensible: OpenSSL's upstream advisory independently confirms
the flaw, its High rating and the affected branch list, which I verified.)

**F10 — UVVG Arad: `reliability: A` on a regional-news transcription.**
`classification: {reliability: A, credibility: 2}` with `sources[0]` = `https://www.aradon.ro/aradon-stirile-judetului-arad/atac-cibernetic-la-uvvg-arad-2225370/`,
an untracked regional Arad news portal (Sportarad.ro, also cited, is a local sports portal — its own
structured metadata files this piece under `"articleSection":"Diverse"`). The entry's own sourcing_note
concedes the ranking: *"with Radio România — the national public broadcaster — carried as the
highest-reliability relay"*, and *"No copy of the statement could be located on the university's own domain
despite fetching its homepage and news subdomain and running a site-restricted search"*. In
`sources/sources.json` the `A` letter is held by first-party authorities (bsi-de, siemens-productcert-csaf)
while established original-research labs (kaspersky-securelist, talos, sophos-xops, rapid7-research,
trustwave-spiderlabs) sit at `B`. `A` on a press-release relay with no verifiable first-party copy plainly
contradicts the cited source's nature; `B` is the defensible letter. Credibility `2` is correct.

### Action-item discipline

**F11 — Minnesota action 2 restates the body's own guidance and re-issues an action already published on the
same advisory.** Action, verbatim: *"Verify PLC project files against known-good ladder logic using the
vendor's integrity-checking tools, explicitly including Add-On Instructions, and return controllers with a
physical mode switch to RUN — the documented impact is added logic that overrides safe-operating-parameter
instructions and disables shutdown and alarm logic without alerting operators."* The body's Defender
takeaway already carries it: *"periodic comparison of running project files against known-good logic —
Add-On Instructions included — is the detection that catches this class rather than the alerting the
attacker just disabled."* And `entries/2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion.md`
already ships the same task as its single action: *"Baseline the running logic and Add-On Instructions on
any internet-reachable Rockwell, Schneider Modicon M340 or Siemens S7-1200 PLC against a known-good copy,
and alert on unauthorised changes …"*. The Minnesota incident supplies no new basis for it — its own body
records that whether the PLC vector was involved at all is unclear. Action 1 (enumerating internet-reachable
PLCs **and cellular-connected field devices**) is the genuine delta this incident earns and should stay.
Remediation: drop action 2, or narrow it to the one element not already published (the physical mode switch
to RUN, which AA26-097A does state: *"For controllers with a physical mode switch, place the physical mode
switch into run position to prevent remote modification."*).

### Editorial / less-is-more flags (advisory)

**F12 — the run record's published notes carry workflow-internal language** (check 12). Three instances in
`runs/2026-07-29/2026-07-29T0408Z-intel.md`: *"The scoped **Phase 4** re-read of the **will-publish**
primaries changed four things that would otherwise have shipped wrong"*; *"all 15 essential-tier sources
across **S1 and S2** were attempted and reached"*; *"worth noting as a small signal that a **sub-agent**
proposing a source did not find it in the slice it was given"*. "Phase N" and "sub-agent" are the named
prohibited patterns. Trivially rewritable ("the second-pass re-read of the primaries selected for
publication", "all 15 essential-tier sources across the vulnerability and home-region slices", "a research
pass proposing a source").

**F13 — Talos sourcing_note undercounts the ids added beyond Talos's own table.** It says: *"Two ATT&CK ids
in the mapping, Windows Service persistence and NTDS credential dumping, describe steps Talos narrates in
prose for the Sinobi chain but did not list in its own summary table."* Both named ids are correct
(T1543.003 for *"installed as a SYSTEM-level auto-start service"*, T1003.003 for *"obtained from the domain
credential store, ntds.dit"* — both verified verbatim). But I extracted Talos's summary table and it lists
T1021.001 and T1021.004 without T1021.006, and contains neither T1557 nor T1098.005 — all three of which
are in the entry's `techniques[]`, all three body-described (*"adversary-in-the-middle proxies"*,
*"registration of attacker-controlled devices for authentication"*, *"moved through the network over RDP and
WinRM"*) and all three source-supported. The mapping is sound; only the count in the note is wrong.

**F14 — the new registry key bakes the unconfirmed Qilin attribution into a permanent namespace.**
`incident:uvvg-arad-qilin-ransomware-2026-07`. The record's display name is correct ("UVVG Arad cyberattack
(July 2026)") and the entry's body holds the attribution boundary rigorously, but the key itself reads as
settled attribution wherever keys surface (entity pages, `/graph/`). Registry keys are permanent, so this
run is the only window to choose differently (e.g. `incident:uvvg-arad-cyberattack-2026-07`, with the Qilin
claim carried by the `actor:qilin` link the entry already has).

**F15 — Check Point update mislabels the CVSS provenance.** Its sourcing_note says *"The CVSS is repeated
from the original entry's **vendor** sourcing — Rapid7's write-up does not assign one."* The original
`entries/2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232.md` states the opposite: *"this
entry uses 9.1 (the NVD-assigned score …) while Check Point's PSIRT advisory prints 9.3"*. The number itself
is consistent across both entries (no CVSS drift); only the provenance label is wrong.

**F16 — Langflow sourcing_note characterises CVE-2026-5027 in a way the referenced entry contradicts.** It
says *"CVE-2026-5027 … is a distinct **low-privilege** path-traversal flaw this pipeline covered on
2026-06-11"*. That referenced entry is titled *"CVE-2026-5027 — Langflow: unauthenticated path traversal to
arbitrary file write, exploited in the wild"* and carries `auth: pre-auth`, with the summary *"made
effectively pre-auth by Langflow's default auto-login"*. "low-privilege" is defensible against the CVSS
`PR:L` vector but reads as a contradiction of the store's own record for the same CVE — a store an automated
triage consumer reads for exactly this field.

### Points I tested at the operator's request and found sound (no finding)

- **The two out-of-window carries are defensible, and stronger than the run record claims.** TeamCity's
  advisory (`datePublished 2026-07-27T16:44:32Z` on the MITRE record; blog same day) and LegacyHive
  (`datePublished 2026-07-27T14:07:50.000Z`, confirmed from the page's own JSON-LD) both fall **inside the
  preceding 2026-07-28T0409Z fire's window**, not merely inside a 72 h allowance — so publishing them now
  closes a prior blind spot rather than recycling stale news. `event_date: 2026-07-27` on both, plus the
  run-record disclosure, means no reader is misled. Dropping an all-versions unauthenticated RCE on a CI/CD
  server for a 13-hour overshoot would have been the defect.
- **Siemens `event_date: 2026-07-14` is handled honestly.** The body states the split plainly (*"CISA
  republished Siemens ProductCERT advisory SSA-734552 on 2026-07-28"* in the summary; *"The in-window
  trigger is CISA's republication on 2026-07-28; Siemens ProductCERT itself published both advisories on
  2026-07-14, which `event_date` records so the age is not obscured"* in the sourcing_note). Verified:
  both CSAF documents carry `initial_release_date 2026-07-14`, and the CISA page's revision history reads
  `2026-07-28 | 2 | Initial CISA Republication`.
- **`cves[].cvss: null` on CVE-2026-59243 is correct on all three counts.** Apache's post carries only
  `Severity: moderate` (no vector, no score); BSI's CSAF carries `aggregate_severity: {text: "hoch"}` at
  document level and **no `scores` block** on the vulnerability entry; `https://cveawg.mitre.org/api/cve/CVE-2026-59243`
  returns `{"error":"CVE_RECORD_DNE"}` today. The moderate-vs-hoch divergence is surfaced, as it should be.
- **CVE-2026-0769 vs CVE-2026-0770 is right, verified independently of the run's snapshot.** I pulled the
  live catalog (`fetch_source.py cisa-kev`, catalogVersion 2026.07.27, 1655 records): exactly five Langflow
  entries — CVE-2026-0770 (added 2026-07-21), CVE-2026-55255, CVE-2025-34291, CVE-2026-33017, CVE-2025-3248
  — matching the entry's list; **CVE-2026-0769 absent; CVE-2026-5027 absent**. The two are genuinely
  different flaws: KEV describes 0770 as *"inclusion of functionality from untrusted control sphere"* while
  ZDI-26-035/CWE-95 makes 0769 an `eval_custom_component_code` eval injection. No fixed version exists for
  0769: ZDI documents none, GHSA-5v3c-9g74-93w7 has empty Affected/Patched sections, and
  `https://api.osv.dev/v1/vulns/GHSA-5v3c-9g74-93w7` returns 404 — exactly as the entry states. (OSV does
  carry a CVE-keyed record for 0769, with `introduced 1.3.2` / `last_affected 1.3.2` and no `fixed` event,
  which corroborates rather than contradicts.) No transposition anywhere.
- **The Desigo CC V8 correction is right.** Siemens' CSAF `remediations` block: product 1 (family V7) →
  `category: none_available`, *"Currently no fix is available"*; product 2 (family V8) → `vendor_fix`,
  *"Update to patch V8.0 QU2.0021"*; product 3 (V9 < 9.0.1) → `vendor_fix`, *"Update to V9.0 QU1 or later
  version"*. `known_affected: ["1","2","3"]`. The entry's `affected`/`fixed` fields reproduce this exactly.
- **Minnesota attribution boundary holds in title, headline, summary and body** (the failure is confined to
  the two frontmatter fields in F4). The Iran juxtaposition is handled correctly — StateScoop does contain
  *"though Iran is a reasonable guess"* as the reporter's own aside, and the entry explicitly refuses it.
- **UVVG Arad keeps the two streams unlinked** in prose (*"the two available pieces of information do not
  actually touch"*), and I confirmed by fetching all three Romanian sources that none mentions Qilin,
  ransomware or any actor. The defects are the missing citation (F7), the reliability letter (F10) and the
  registry key (F14) — not the framing.
- **Talos percentages are never presented as landscape base rates.** Every figure checked verbatim: 65% /
  35% authentication abuse, 42% / 18% logging, 31% exposed infrastructure, "almost 15 percent" outbound
  email, "For the second quarter in a row, health care led … 17 percent … public administration and
  manufacturing following at 14 percent each", 6,600 messages, 80+ API endpoints, 90 days retention,
  *"Almost all targeted public administration organizations were local governments"*. The sourcing_note's
  base-rate caveat is exactly right, and the two ids it names are correctly body-described (see F13 for the
  count only).
- **The six drops are all defensible.** MOVEit 2026.0.3: the gate is actionability beyond the patch cycle,
  and CVSS 7.1–7.5 with an adjacent-network/high-complexity auth bypass, no exploitation and no public
  exploit does not clear it — the NCSC-CH freshness flag is a relevance signal, not an urgency mechanic, and
  the run recorded the counter-signal rather than hiding it. VulnCheck-as-report: correctly dropped as
  statistics while the one operational fact was mined into its own entry — the right shape. Netcraft: the
  leftover-LLM-refusal-text tell is genuinely novel but the piece is carried by abuse-report volume growth
  figures, which is the vanity-metric class; closest call of the six, still within range. Garante fine: no
  hunt or detection consequence. Della Casa Group AG: leak-site-only with no victim confirmation and a
  sector outside the profiled list — consistent with the same run's UVVG treatment (which has victim
  confirmation) and with the entry's own *"a leak-site listing is a lead for monitoring rather than a fact
  to act on"*. NCSC-CH consumer-fraud post: citizen-facing, no TTP. I re-read all six findings YAMLs and
  found nothing left behind that should have shipped.
- **Coverage looks complete.** The apple-security recipe gap was the only one with real miss potential; I
  probed it independently and the 2026-07-28 Apple batch is image/file-parsing flaws (ImageIO, AppleDouble,
  SceneKit) with no actively-exploited language — the run's "routine patch cycle" assessment holds. An
  independent German-language search for in-window Swiss incidents surfaced nothing newer than the
  2026-07-23 Western-Switzerland item, corroborating the zero home-region return. Dedup is clean:
  `state/cves_seen.json` shows all five new CVEs at `first_seen: 2026-07-29` and CVE-2026-16232 at
  `first_seen 2026-07-23 / last_seen 2026-07-29`; the Check Point `update_of` target exists and the update
  carries only the delta; the Chaos-entity non-update decision is correct (Sophos explicitly declines to
  attribute STAC4749, and the shared entity is the payload at the end of the chain, recorded as a typed
  `collaborates-with` edge). Registry hygiene is good — "Mirage Kitten" was folded as an alias onto the
  existing `actor:screening-serpens-…` record rather than creating a second key.
- **Priority calibration is defensible, including zero criticals.** Seven `high` on a window carrying five
  serious pre-auth vulnerabilities (two 9.8, one with an unpatched product family, one actively exploited
  with no patch at all) is the honest output of the bar, not inflation; nothing clears the
  stop-and-act-to-the-hour critical bar, and the run's own rationale for that is sound.
- **Zero IOCs.** Grepped all 11 entries for hashes, IPv4 literals, bracketed domains and the specific
  attacker infrastructure present in the sources (`businessmixture.com`, `smartconnect.azurewebsites.net`,
  `legio[.]name`, `readme.chaos.txt`, the вшк artifact, the username-gate value, AA26-097A's IP tables) —
  none present. The `.top` TLD and the Realtek/WinAudio/SecurityHealth naming *patterns* are behaviour
  descriptions, correctly kept.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 5, advisory: 5)

None of the truth findings requires new research: F1, F2 and F7 are citation moves to sources the run
already fetched (a GitHub PoC repo, the co-cited Cybersecurity Dive article, the ransomware.live mirror in
`findings.S4.yaml`); F3 is a one-clause rewording plus a Triage rebuild on grounds the entry already has;
F4 and F5 are frontmatter deletions; F6 is three quote corrections. F9 and F10 are single-character
classification changes. Fix these and the run is publishable — the underlying research quality here is high
and the sourcing is unusually well documented.

### Findings summary (machine-readable)

```yaml
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2025-15467 — Siemens Desigo CC (2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed)"
  url_or_quote: "\"CISA's republication notes a public command-execution proof-of-concept already exists ([CISA, 2026-07-28](https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-01))\""
  summary: "Fetched icsa-26-209-01 (bridge, 173 lines) plus work/<run>/icsa-26-209-01.json, Siemens ssa-734552.json and the OpenSSL advisory at both openwall and openssl-library.org: none contains 'proof'/'PoC'/'public exploit'; the CISA page is an explicit verbatim republication of the Siemens CSAF. Claim also drives the headline, summary, cves[0].status poc-public, the poc-public tag and action 1. The PoC does exist — findings.S1.yaml cites https://github.com/guiimoraes/CVE-2025-15467 ('Command Execution PoC for OpenSSL Stack buffer overflow CVE-2025-15467', fetched and confirmed) — but it is absent from the entry's sources[]. Cite it for the clause, or drop the CISA attribution and the poc-public status/tag."
- code: F2
  category: claim-not-supported
  section: incidents
  item: "Minnesota 30+ water utilities (2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack)"
  url_or_quote: "\"South St. Paul identified impact to certain automated controls and reported no major effect on drinking-water or wastewater treatment operations after invoking contingency procedures … ([StateScoop, 2026-07-28](https://statescoop.com/coordinated-cyberattack-disrupts-water-utilities-in-30-minnesota-communities/))\""
  summary: "Fetched StateScoop: zero occurrences of 'South St', 'automated control' or 'contingency'. The facts are verbatim in the co-cited Cybersecurity Dive article ('authorities in South St. Paul, Minn., said they identified a cyberattack on Monday that impacted certain automated controls. After implementing contingency procedures, officials confirmed no major impact to drinking and wastewater treatment operations.'). Attach the Cybersecurity Dive citation to that clause; the summary repeats the same claim. Second instance in the same paragraph: 'lifting the request once the plant was back online' — StateScoop says only that a second notice noted the plant was back online, not that the minimise-use request was lifted."
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-63077 — JetBrains TeamCity (2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce)"
  url_or_quote: "\"The reachable surface is the agent-polling protocol … which by design does not require authentication\" and Triage: \"the agent-polling endpoint is *supposed* to receive a steady stream of unauthenticated check-ins, so volume alone tells you nothing\""
  summary: "JetBrains' Technical details section (fetched, extracted verbatim) says 'Exploitation of this vulnerability does not require authentication. An unauthenticated attacker could exploit the vulnerability via the TeamCity agent polling protocol to bypass authentication checks…' — a statement about exploitation of the flaw, not about the protocol's design; the advisory's own framing is that the flaw BYPASSES authentication checks. Nothing on the page says the agent-polling channel is unauthenticated by design. The Triage discriminator is built on that unsupported premise (check 10). Reword to 'exploitation requires no authentication' and rebuild the Triage line on the source-address-set and process-lineage grounds the entry already carries."
- code: F4
  category: hallucinated-fact
  section: incidents
  item: "Minnesota 30+ water utilities (2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack)"
  url_or_quote: "tags: [ot-ics, nation-state] and affected_products: [\"Rockwell Automation CompactLogix\", \"Rockwell Automation Micro850\", \"Schneider Electric Modicon M340\", \"Siemens SIMATIC S7-1200\"]"
  summary: "Frontmatter asserts what the body denies. Body: 'No authority has named an actor… it is unclear whether the programmable logic controllers CISA had warned about were involved' and 'Treating it as attribution would be reading the calendar as evidence.' No cited source attributes the Minnesota event to a state actor, so the nation-state tag is unsupported. AA26-097A (fetched) names those four families as targets of the separate Iranian campaign ('Rockwell Automation: CompactLogix and Micro850 PLCs / Schneider Electric: BMX P34/Modicon M340 PLCs / Siemens: S7-1200 series PLCs'); no source names any controller involved in Minnesota, and entries/2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion.md already carries this exact list. Also a name drift: source says 'S7-1200 series', store value is 'Siemens S7-1200', entry writes 'Siemens SIMATIC S7-1200'. Drop the nation-state tag and empty (or narrow) affected_products."
- code: F5
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CVE-2026-0769 — Langflow (2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev)"
  url_or_quote: "cves[0].status: [exploited, no-patch, poc-public] and tags: [..., poc-public]"
  summary: "No cited source supports a public proof-of-concept. ZDI-26-035 (fetched) publishes none and offers only 'restrict interaction with the product'; the MITRE record for CVE-2026-0769 (fetched) references only the ZDI advisory; VulnCheck (fetched) says 'attackers gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027' — in-the-wild attacker exploitation, not a public PoC. Contrast the Check Point update, where poc-public IS supported (Rapid7 links its PoC at https://github.com/sfewer-r7/CVE-2026-16232, confirmed in the page's embedded content). Remove poc-public from status and tags."
- code: F6
  category: hallucinated-fact
  section: whole-run
  item: "Airflow entry — evidence[] quote 2 (2026-07-29/cve-2026-59243-airflow-fab-azure-ad-jwt-signature-bypass)"
  url_or_quote: "\"Credit: MalHyuk (finder), Jarek Potiuk (remediation developer)\""
  summary: "Not a contiguous verbatim substring: the oss-sec post (fetched, tag-stripped) has three separate lines 'Credit:' / 'MalHyuk (finder)' / 'Jarek Potiuk (remediation developer)'. The comma is inserted. Meaning-preserving but fails the copyable-unchanged rule. Quote a single line, or reproduce the block exactly."
- code: F6
  category: hallucinated-fact
  section: whole-run
  item: "Siemens entry — evidence[] quote 1 (2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed)"
  url_or_quote: "\"Stack buffer overflow in CMS AuthEnvelopedData parsing (CVE-2025-15467) === Severity: High\""
  summary: "Not a contiguous verbatim substring: the openwall page (fetched raw) carries the heading on line 162, a 71-character '=' underline on line 163, a blank line, then 'Severity: High' on line 165; '===' compresses the underline. Split into two quotes or quote 'Severity: High' alone."
- code: F6
  category: hallucinated-fact
  section: whole-run
  item: "STAC4749 entry — evidence[] quote 5 (2026-07-29/stac4749-teams-vishing-certificate-pinned-golang-chaos)"
  url_or_quote: "\"Sophos analysts have found no evidence linking STAC4749 activity to that group. Instead, limited hands-on-keyboard artifacts suggest a Russian-language connection... However, there is insufficient evidence for attribution.\""
  summary: "Inserted ellipsis elides an intervening sentence (confirmed present in the fetched page: 'For example, Sophos analysts observed a mistyped command (вшк) that is consistent with the operator attempting to enter \"dir\" while using a Russian keyboard layout.'). Split into two separate evidence records, each contiguous."
- code: F7
  category: missing-citation
  section: incidents
  item: "UVVG Arad (2026-07-29/uvvg-arad-romania-university-cyberattack-qilin-claim)"
  url_or_quote: "\"Separately, the Qilin ransomware operation listed the university on its leak site with an estimated attack date of 2026-07-26\" — no inline citation, no sources[] record"
  summary: "The Qilin claim carries the title, summary, body, entities: [actor:qilin], techniques: [T1486] and tags: [ransomware] with no citation and no source record. I fetched all three cited Romanian sources (aradon.ro, radioromania.ro, sportarad.ro): none contains 'Qilin' or 'ransomware', which the entry itself states — so the listing, the group name and the 2026-07-26 date are unverifiable by a reader. The run had the source: findings.S4.yaml records https://www.ransomware.live/id/VW5pdmVyc2l0YXRlYSBkZSBWZXN0IOKAnlZhc2lsZSBHb2xkaciZ4oCdIGRpbiBBcmFkQHFpbGlu (ransomware-live, reliability C in sources/sources.json), and seven published entries already cite ransomware.live. Add it as a corroborating sources[] record and cite it at the claim; keep the existing 'claim, not fact' framing."
- code: F8
  category: missing-citation
  section: trending-vulnerabilities
  item: "CVE-2026-63077 — JetBrains TeamCity (2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce)"
  url_or_quote: "\"CVE-2023-42793 in TeamCity was exploited at scale in 2023 against internet-facing servers, an event significant enough to draw a joint advisory naming Russian SVR-attributed actors.\" (also in the summary)"
  summary: "A second CVE id plus a state attribution plus an implied joint advisory, with no inline link. Neither cited source mentions CVE-2023-42793 — I fetched the JetBrains advisory and the MITRE record for CVE-2026-63077 and confirmed. Cite the joint advisory that carries the SVR attribution, or drop the attribution clause."
- code: F9
  category: classification
  section: trending-vulnerabilities
  item: "CVE-2026-59243 — Apache Airflow FAB (2026-07-29/cve-2026-59243-airflow-fab-azure-ad-jwt-signature-bypass)"
  url_or_quote: "classification: {reliability: A, credibility: 1}"
  summary: "Credibility 1 ('confirmed by other sources') contradicts the entry's own sourcing_note: 'they are not independent assessments of the same facts: BSI CERT-Bund's advisory is a republication of Apache's disclosure, so the technical claims rest on Apache's own account of its own codebase.' I fetched the BSI CSAF (bsi-csaf WID-SEC-2026-2551) and confirmed pure republication — its only external references are the same oss-sec post and the Apache GitHub PR, and it carries no scores block. Change credibility to 2; reliability A on Apache's own security team is correct."
- code: F10
  category: classification
  section: incidents
  item: "UVVG Arad (2026-07-29/uvvg-arad-romania-university-cyberattack-qilin-claim)"
  url_or_quote: "classification: {reliability: A, credibility: 2} with sources[0] = https://www.aradon.ro/aradon-stirile-judetului-arad/atac-cibernetic-la-uvvg-arad-2225370/"
  summary: "Reliability A on an untracked regional Arad news portal transcribing a press release, with no first-party copy verifiable (the entry itself: 'No copy of the statement could be located on the university's own domain…'). The entry's own note ranks Radio România above it as 'the highest-reliability relay'. In sources/sources.json the A letter is held by first-party authorities (bsi-de, siemens-productcert-csaf) while established original-research labs sit at B. Change reliability to B; credibility 2 is correct."
- code: F11
  category: action-item-discipline
  section: incidents
  item: "Minnesota 30+ water utilities (2026-07-29/minnesota-30-water-utilities-coordinated-ot-attack) — action 2"
  url_or_quote: "\"Verify PLC project files against known-good ladder logic using the vendor's integrity-checking tools, explicitly including Add-On Instructions, and return controllers with a physical mode switch to RUN — the documented impact is added logic that overrides safe-operating-parameter instructions and disables shutdown and alarm logic without alerting operators.\""
  summary: "Restates the body's own hardening guidance ('periodic comparison of running project files against known-good logic — Add-On Instructions included — is the detection that catches this class') and re-issues the action already published on the same advisory: entries/2026-07-24/cyberav3ngers-plc-aa26-097a-schneider-siemens-expansion.md ships 'Baseline the running logic and Add-On Instructions on any internet-reachable Rockwell, Schneider Modicon M340 or Siemens S7-1200 PLC against a known-good copy…'. This incident supplies no new basis — its own body says whether the PLC vector was involved is unclear. Drop it, or narrow to the one unpublished element (physical mode switch to RUN, which AA26-097A does state). Keep action 1 — the cellular-field-device exposure question is the genuine delta."
- code: F12
  category: editorial-advisory
  section: whole-run
  item: "runs/2026-07-29/2026-07-29T0408Z-intel.md — verification & coverage notes"
  url_or_quote: "\"The scoped Phase 4 re-read of the will-publish primaries…\" · \"all 15 essential-tier sources across S1 and S2 were attempted and reached\" · \"a sub-agent proposing a source did not find it in the slice it was given\""
  summary: "Workflow-internal language in the published run-record notes (check 12: 'Phase N' and 'sub-agent' are named prohibited patterns). Rewrite in reader-facing terms, e.g. 'the second-pass re-read of the primaries selected for publication', 'all 15 essential-tier sources across the vulnerability and home-region slices', 'a research pass proposing a source'."
- code: F13
  category: editorial-advisory
  section: deep-dive
  item: "Talos IR Trends Q2 2026 (2026-07-29/talos-ir-trends-q2-2026-rmm-weaponization-auth-abuse) — sourcing_note"
  url_or_quote: "\"Two ATT&CK ids in the mapping, Windows Service persistence and NTDS credential dumping, describe steps Talos narrates in prose for the Sinobi chain but did not list in its own summary table.\""
  summary: "Both named ids are correct and body-described (T1543.003 for 'installed as a SYSTEM-level auto-start service', T1003.003 for 'obtained from the domain credential store, ntds.dit' — both verified verbatim). But I extracted Talos's summary table: it lists T1021.001 and T1021.004 without T1021.006, and contains neither T1557 nor T1098.005 — all three are in techniques[], all three body-described ('adversary-in-the-middle proxies', 'registration of attacker-controlled devices for authentication', 'moved through the network over RDP and WinRM') and source-supported. The mapping is sound; only the count is wrong. Say 'several' or name all five."
- code: F14
  category: editorial-advisory
  section: whole-run
  item: "entities/registry.yaml — incident:uvvg-arad-qilin-ransomware-2026-07"
  url_or_quote: "incident:uvvg-arad-qilin-ransomware-2026-07"
  summary: "A permanent registry key that bakes the unconfirmed leak-site attribution into the namespace, against the entry's own attribution-boundary discipline. The record's display name ('UVVG Arad cyberattack (July 2026)') is correct, but keys surface on entity pages and /graph/. Registry keys are permanent, so this run is the only window to choose e.g. incident:uvvg-arad-cyberattack-2026-07, with the claim carried by the actor:qilin link the entry already has."
- code: F15
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-16232 root cause (2026-07-29/check-point-cve-2026-16232-sic-dn-substitution-root-cause) — sourcing_note"
  url_or_quote: "\"The CVSS is repeated from the original entry's vendor sourcing — Rapid7's write-up does not assign one.\""
  summary: "The original entry (entries/2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232.md) states the opposite: 'this entry uses 9.1 (the NVD-assigned score …) while Check Point's PSIRT advisory prints 9.3'. The 9.1 value itself is consistent across both entries (no CVSS drift); only the provenance label is wrong. Say 'carried from the original entry, where 9.1 is the NVD-assigned score against Check Point PSIRT's 9.3'."
- code: F16
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-0769 — Langflow (2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev) — sourcing_note"
  url_or_quote: "\"CVE-2026-5027 … is a distinct low-privilege path-traversal flaw this pipeline covered on 2026-06-11\""
  summary: "The referenced entry is titled 'CVE-2026-5027 — Langflow: unauthenticated path traversal to arbitrary file write, exploited in the wild', carries auth: pre-auth, and summarises it as 'made effectively pre-auth by Langflow's default auto-login'. 'low-privilege' is defensible against the CVSS PR:L vector but reads as a contradiction of the store's own record for the same CVE, which automated triage consumers read for exactly this field. Say 'CVSS PR:L but effectively pre-auth via Langflow's default auto-login, as the 2026-06-11 entry recorded'."
```
