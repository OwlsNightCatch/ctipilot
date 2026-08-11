**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-11T05:21:16Z · ended_at=2026-08-11T05:37:49Z · duration_seconds=993
**Self-telemetry:** urls_checked=12 · webfetch_calls=7 · bridge_fetches=5 · websearch_calls=2

## Verification report — 2026-08-11T0411Z-intel (iteration 3)

Cold read, Opus rotation, no prior-iteration deltas block supplied. Scope: four new entries + run record.
Every one of the nine cited source URLs was fetched in this iteration (CISA via the bridge, the rest via
`WebFetch`); all nine resolve to specific advisory / research / notice pages, none is a homepage, index or
NVD/MITRE per-CVE page. All fifteen `evidence[]` quotes across the four entries were machine-checked as
contiguous verbatim substrings of the fetched page bodies — all fifteen pass.

**What was re-verified from the two prior iterations (unprompted re-derivation, not acceptance):**

- **`cisa-kev` removal (iter-2 F4) leaves no orphan.** `grep -i -E "kev|known exploited|catalog"` over the
  Gunra entry returns nothing — not in prose, `tags`, `summary`, `actions`, or the `actor:gunra` registry
  record. The surviving `exploited` status is carried: 'The FBI observed Gunra actors obtaining initial
  access ... primarily through the exploitation of known vulnerabilities in internet-facing devices',
  followed by both CVE ids. Confirmed independently: the advisory's only catalogue-adjacent text is the
  generic 'Prioritize patching known exploited vulnerabilities' key action.
- **`T1129` on the eID entry (iter-2 advisory) is body-supported, not bolted on.** The body describes 'The
  reader-enumeration command accepts a `library` parameter naming a DLL to load, relative paths included',
  and the source carries it verbatim: `{ "cmd": "GET_READERS", "library": "..\\..\\..\\..\\Downloads\\lib.dll" }`
  … 'The library property in the command allows any web page to specify which DLL they want to load, and
  relative paths are allowed.' T1129 (Shared Modules) is active and non-revoked in the pinned dataset.
- **Iteration 1's four CEVA remediations hold.** CMA CGM ownership now cites ICTMagazine ('maakt sinds 2019
  onderdeel uit van de Franse scheepvaartgigant CMA CGM Group'); the European scoping of Steam buyers now
  cites ICTMagazine ('gegevens van Europese Steam-hardwareklanten'); the early-May 2026 date is gone from
  body and `sourcing_note` and appears in none of the three sources; the summary now separates the
  ten-report count from the named affected parties. The replacement takeaway clause is correct — bol.com's
  own notice does name CEVA in its 6 August update, but ICTMagazine's claim is about the *early* notices
  ('Waar begin deze week alleen De Bijenkorf en Bol waarschuwden voor een beveiligingsincident bij een
  externe logistieke partner'), so there is no residual contradiction with the entry's primary.

**Judgement calls challenged and independently upheld** (a third look, deliberately hostile to the prior two):

- **macOS `verification: contradicted` is correct and the conflict is genuine.** Huntress, verbatim: 'The
  daemon's frame-length validator erroneously returns a stale success status, so the connection is treated
  as authenticated.' Calif, verbatim, assigns that mechanism to the *other* bug: '@osxreverser's bug is a
  single wrong return. A length check bails out early on an oversized frame and hands back a value that
  happens to be the success code from the read just before it', and CVE-2026-65400 is 'a state machine
  desync … we are withholding the details'. Two first-hand analyses of the same patch, incompatible on
  root cause, agreed on everything action-driving. Reporting both is right.
- **CEVA `T1005`-only mapping holds.** All three sources fetched; none names an access vector, malware
  family or actor. The rejection of a trusted-relationship mapping is sound — the adversary reached
  downstream data by compromising the processor, never a downstream network.
- **All four priorities calibrated.** Gunra `high` (six-agency advisory, exploited edge CVEs, sector
  match, but no new imminent action to the hour) — not `critical`, correctly. macOS `high` (pre-auth
  remote root, exploits rebuilt in four hours, ~40k exposed, no observed in-the-wild exploitation) —
  `high`, not `critical`, correctly. eID and CEVA `notable` — both fixed/closed situations with
  transferable lessons rather than do-now work. No under-alerting.
- **Gunra deep-dive earns its length,** and `ransomware-affiliate` has not been used in the last fourteen
  deep dives (rotation is clean). Its `techniques[]` list was diffed programmatically against the
  advisory's own ATT&CK table: exact match on all 36 leaf ids, with only the six parent ids (T1021, T1059,
  T1070, T1078, T1550, T1556) that appear solely as sub-technique parents omitted — correct. The
  advisory's table names match the pinned dataset exactly (T1678 Delay Execution, T1679 Selective
  Exclusion, T1685 Disable or Modify Tools).
- **eID org-relevance holds and the out-of-window primary is correctly carried.** European public-sector
  identity infrastructure, an eIDAS Qualified Trust Service Provider on the EU Trusted List, and a
  generalisable native-messaging-host trust-boundary lesson stated as such. Primary 2026-08-07 (outside
  the 26 h window), in-window corroboration 2026-08-10 — the standard shape, not recycled news.
- **Action-item discipline holds on all four.** Gunra's two and macOS's two are concrete, finding-derived,
  start-now tasks; the eID and CEVA empty lists are correct (fixed software; a lesson entry with nothing
  clearing the do-now bar). The macOS 'disable Screen Sharing' action does overlap the 2026-08-08 entry's,
  but that entry is outside the rendered 24 h window and the delta (pre-auth remote root, public exploits,
  the hardening caveat) genuinely changes the task. No F18.
- **Frontmatter ⇔ body agreement checked field by field.** The macOS summary's 'tens of thousands of
  potentially vulnerable hosted bare-metal Macs' is *not* an overstatement: Huntress scopes the Censys
  count to hosted-provider ASNs and ports in the same sentence. `cvss: "7.1"` on CVE-2026-65400 is not
  carried by either cited source but is verified correct against the CVE's own metrics (CISA-ADP CVSS 3.1
  base 7.1) and is inherited, sourced, from the `update_of` target — provenance is sound, not flagged.
- **Classification codes hold.** Gunra A/1 (six-agency joint advisory plus independent corroborating
  research); CEVA B/1 (three sources incl. first-party); eID and macOS B/2. No `A` on a lone blog. All four
  carry `org_triage: null` and `watchlist_hit: false` with no `watchlist` tag, correct for a deployment
  with no triage scheme and no watchlists — no F16, no F17.
- **Style.** Zero IOCs (no hashes, IPs, attacker domains or rule code — the advisory's hash tables and the
  Breakglass sample hashes were correctly left out). No vanity metrics. English throughout. No
  workflow-internal vocabulary survives in any entry or in the run-record notes; the only remaining hits
  are the `verification.iterations[]` structured block, which is the published transparency artifact
  itself, not leakage.
- **Run-record telemetry spot-checked against disk:** 'eighteen entries' (previous fire published 18, 18
  files on disk), '181 sources' (181 in `sources.json`), 'fifteen essential sources' (15 with
  `tier: essential`). All accurate.

**Completeness.** No blind spot found. Prior coverage (166 records, 14 days) carries no Gunra, Connective/
eID or CEVA entry, and the macOS `update_of` target exists and is the right story. Independent probes for
in-window exploited-vulnerability and Swiss/European government activity surfaced only TeamCity
CVE-2026-63077, N-able N-central CVE-2026-18577 and Progress LoadMaster CVE-2026-8037 — all three already
in the store's CVE index from earlier fires, correctly not re-shipped. The five recorded borderline drops I
could re-derive (ClamAV DoS, the React hook packages, Gagny, AFPA, the unconfirmed leak-site claims) are
each correctly dropped for the reason stated. Coverage looks complete; the one contestable exclusion is
recorded as F3 below, advisory only.

### Citation does not support the claim

**F1 — CEVA entry: the 'no newsroom statement' clause is carried by the other co-cited source.**

The sentence, verbatim:

> That is the whole of what the compromised party has said publicly: CEVA has published no statement
> through its own newsroom, and its spokesperson declined to answer whether the company knows how much
> personal data was taken or whether it has heard from the intruders at all, including on a ransom demand
> ([TechCrunch, 2026-08-10](https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond/)).

The trailing citation claims both clauses. Fetched live this iteration, the TechCrunch article supports
only the second: 'Ceva spokesperson Ryan Fisher would not answer TechCrunch's questions about the incident,
such as if the company knows how much personal data was taken, or if Ceva has received any communication
from the hackers, such as a ransom demand.' On the first clause it says the opposite kind of thing — 'Ceva
confirmed in a statement to TechCrunch that it was experiencing a cyberattack' — and its only remark about
CEVA's own channels is 'Ceva's website was not properly loading at the time of publication on Monday'.
Nothing about a newsroom or about the absence of a public statement.

The fact is true and is carried by the entry's own co-cited source: ICTMagazine.nl, under the heading
'Stilte bij de spil in de keten', states 'heeft CEVA Logistics zelf nog geen enkele publieke reactie
gegeven op deze recente incidenten' — a broader claim that entails the entry's narrower one.

**Remediation:** attach `([ICTMagazine.nl, 2026-08-10](https://www.ictmagazine.nl/nieuws/datalek-bij-ceva-logistics-groeit-uit-tot-ketencrisis/))`
to the newsroom clause, or split the sentence so each clause carries its own source. No fact needs to
change. This is the same defect class iteration 1 found twice on this entry, on a third clause neither
prior iteration examined.

### Claims missing inline citation

**F2 — macOS entry: the headline 40,000 figure has no link in the body.**

`headline`: '…exploits rebuilt from the patch in hours, ~40,000 hosts exposed'. `summary`: 'a researcher
scan cited by Calif found roughly 40,000 Macs with Screen Sharing reachable from the internet'. Body,
verbatim:

> **Exposure.** Calif cites the scan by the researcher who started the affair, which found around 40,000
> Macs with Screen Sharing reachable from the internet — mostly residential addresses, but including
> university and company hosts. Huntress reports a separate concern for managed estates: … ([Huntress,
> 2026-08-07](https://www.huntress.com/blog/macos-screen-sharing-rce-patched)).

The paragraph's only link is the Huntress one, attached to the following sentence, and Huntress carries a
*different* figure for a *different* population — 'a cursory search on Censys reveals tens of thousands of
potentially vulnerable hosts', scoped in the same sentence to hosted bare-metal provider ASNs and ports.
So the entry's headline number has no supporting link anywhere in the body.

The figure itself is correct — Calif quotes @osxreverser: 'My last scan shown around 40k open screen
sharing hosts on the internet, mostly residential IPs but many in universities, companies' — and the
attribution chain in the prose ('Calif cites the scan by the researcher who started the affair') is exact.
This is a missing link, not a fabricated number.

**Remediation:** add `([Calif, 2026-08-10](https://blog.calif.io/p/no-country-for-old-passwords))` to that
sentence. Every other attributed figure across the four entries carries its own link, so this is an outlier
in the entry's own citation style rather than a house convention.

### Editorial / less-is-more flags (advisory)

**F3 — the Liechtenstein drop is the run's most contestable call (no change required).**

Run record, verbatim: 'borderline-drop: Liechtenstein takes its Commercial Register offline as a precaution
… It is an availability and compliance fact for downstream fiduciaries, not a decision a Tier 2/3 responder
makes differently.'

Read cold, this is the only in-window home-region government item in a window whose four entries are
otherwise Korean/American, Belgian, global-macOS and Dutch. The research return marked it `borderline:
false` and supplied an in-window primary (the Government of Liechtenstein's own wire release, 2026-08-10)
with three verbatim evidence quotes, and the store already carries the incident, so the `update_of`
mechanism was available and cheap.

Against that, the item's own notes concede: 'This is a scope/operational-impact delta on the tracked VwbP
incident, not a new technical finding: it adds a fifth precautionarily-isolated system but discloses no new
detail on the original intrusion vector, actor, or exfiltration scope', and the government states there are
no indications of an attack on the newly isolated system. Measured against a profile whose audience is
Tier 2/3 IR, threat hunters and detection engineers, the drop holds and the run record states the reason
honestly. Recorded so the operator can see that a third independent reader weighed it; the main agent may
leave this as is.

**F4 — the run record's borderline-drops list omits two of the four dropped leak-site claims.**

The research return recorded four unconfirmed extortion claims dropped under the fake-news gate: 'Elixi
International SA (Chiasso, Switzerland — pharma distributor, Space Bears claim …); Quironsalud (Spain —
hospital group, DireWolf claim …); Statista GmbH (Germany, DireWolf claim …); Université Libre de Bruxelles
(Belgium, Qilin claim …)'. The run record's borderline-drops list names only Elixi and ULB. Quironsalud is
a Spanish hospital group — healthcare is an additional sector on this deployment's profile — and the list's
stated purpose is 'recorded so a wrong call is recoverable', which the omission defeats for two of the
four. All four were correctly dropped; one added clause naming the other two and their shared reason closes
it. Recording gap, not a coverage gap.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 1, advisory: 2)**

Both actionable findings are single-clause citation repairs that change no fact and carry no regression
risk. Neither touches an entry's analysis, priority, mapping, classification or action list, and I found no
defect in the two remediations this iteration was asked to re-verify. Everything else in the run — four
entries, thirty-six ATT&CK mappings, fifteen evidence quotes, nine URLs, four classification blocks, four
action lists and the run record's telemetry — verified clean against sources fetched in this iteration.

### Findings summary (machine-readable)

See `work/2026-08-11T0411Z-intel/verification.iter3.findings.yaml` (identical payload).
