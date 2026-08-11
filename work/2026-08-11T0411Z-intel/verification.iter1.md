**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-11T04:50:36Z · ended_at=2026-08-11T05:03:21Z · duration_seconds=765
**Self-telemetry:** urls_checked=10 · webfetch_calls=4 · bridge_fetches=9 · websearch_calls=3

## Verification report — 2026-08-11T0411Z-intel (iteration 1)

Cold read, no prior-iteration deltas. All ten distinct cited URLs across the four entries were fetched
in this iteration (CISA AA26-222A via the bridge; Calif, Huntress, amibeingpwned, SecurityWeek, bol.com,
TechCrunch, ICTMagazine.nl, Breakglass Intelligence, plus the NVD API record for CVE-2026-65400 as the
per-CVE score authority). Every `evidence[]` quote was tested as a literal substring against the freshly
fetched body. Every `techniques[]` id was resolved against the pinned ATT&CK v19.2 dataset (all 43 ids
checked across the four entries are active, none revoked or deprecated). KEV membership of
CVE-2024-55591 and CVE-2025-24472 was confirmed against the live catalogue. Dedup was checked against
`prior_coverage.json` (166 records) and `state/cves_seen.json`.

Three of the four entries are clean on truth. All four truth findings are confined to the CEVA entry and
are cross-source-attribution / unsourced-assertion defects, not fabrications of substance.

### Citation does not support the claim

**F1 — CEVA entry: two TechCrunch-cited clauses carry facts only ICTMagazine.nl states.**

Claim (a), body ¶1: *"CEVA Logistics — the contract-logistics arm of CMA CGM — confirmed to affected
customers on 1 August 2026 that a cyber intrusion was affecting part of its European contract-logistics
operations ... ([TechCrunch, 2026-08-10])"*.
The fetched TechCrunch page contains **zero** occurrences of "CMA" — it describes CEVA only as "a
France-headquartered shipping and logistics giant". The ownership fact is carried by the co-cited
ICTMagazine.nl: *"maakt sinds 2019 onderdeel uit van de Franse scheepvaartgigant CMA CGM Group"*.

Claim (b), body ¶2: *"Valve, which told customers that it learned on 7 August that data was taken from
CEVA's systems, and alerted **European** buyers of its Steam hardware ... ([TechCrunch, 2026-08-10])"*.
TechCrunch says *"alerted customers who recently bought its Steam hardware"* — no region. "European" is
ICTMagazine's: *"zijn mogelijk ook gegevens van Europese Steam-hardwareklanten buitgemaakt"*.

Both facts are true and both live in a source the entry already cites; the defect is the adjacency.
Remediation: co-cite ICTMagazine.nl on those two clauses. Note the same descriptor ("the contract-logistics
arm of CMA CGM") also sits in the frontmatter summary and in the new registry record for
`incident:ceva-logistics-fulfilment-breach-2026-08`, which is sourced correctly there.

**F2 — CEVA entry: the "early May 2026" break-in date is not in the source it is attributed to.**

Claim, body ¶4: *"the provenance of data already circulating is disputed: Dutch reporting relays a claim
that a dataset of retail customer records offered for sale came from a CEVA break-in **in early May 2026**,
while CEVA maintains that dataset is old data from a separate 2025 incident
([ICTMagazine.nl, 2026-08-10])"*. Repeated in the frontmatter `sourcing_note`.

The fetched ICTMagazine.nl article carries **no May date at all** (zero matches for "mei" or "May") and
attaches no break-in date to the offered dataset. What it says is: *"Onderzoek van onder meer RTL Nieuws
wees uit dat buitgemaakte data van CEVA te koop worden aangeboden op het darkweb. Het betreft namen,
adresgegevens, e-mailadressen, telefoonnummers en specifieke orderinformatie. Volgens het bedrijf is dat
echter oude data van een eerdere hack uit 2025."* The CEVA-side half of the entry's sentence is exactly
supported; the attacker-side half is not. I also checked the other two cited sources: TechCrunch and
bol.com carry no May 2026 date either.

This matters more than a normal adjacency slip because the sentence's whole function is to attribute a
disputed claim precisely — and the run record repeats the same attribution ("Dutch reporting relays a
claim that ... came from a CEVA break-in in early May 2026"). The date most likely came from the
broadcaster/consumer-programme reporting the run record says was only reached through secondary
quotations; whichever source carries it must be cited, or the date dropped.

To the main agent's explicit question: the entry does **not** let either disputed claim leak into the
body as fact — the hedging is correct and the "Treating that May date as the real start ... is not
supported by anything published" sentence is the right call. The defect is only that the *relay* is
mis-attributed.

### Unsupported / hallucinated facts

**F3 — CEVA entry frontmatter summary asserts the named companies are among the ten DPA filers.**

Summary: *"the single compromise produced independent GDPR notification duties at ten organisations,
**which the Dutch data-protection authority confirmed had filed breach reports — among them** ING,
bol.com, De Bijenkorf, AFC Ajax, Ace & Tate and Valve"*.

TechCrunch reports only: *"Mark Schenkel, a spokesperson for the Dutch data protection authority, told
TechCrunch that the agency has received data breach reports from 10 organizations in relation to the
incident."* It never identifies a single filer. It names the six companies in a different context —
parties whose customers' shipping information was affected. The only confirmed filer in any cited source
is bol.com, from its own notice (*"bol has reported it to the Dutch Data Protection Authority"*); Valve is
a US company and nothing suggests it filed with the Dutch authority.

The entry **body** handles this correctly — it keeps the ten-filer count and the named downstream parties
in separate sentences and never claims membership. The defect is confined to the frontmatter summary,
which is what renders at the top of the brief. Remediation: re-phrase to "named downstream parties whose
customer data was affected include …", outside the filer clause.

### Quantifier without source

**F4 — CEVA entry: "two of the affected organisations' own customer notices did not name CEVA at all".**

Final sentence of the Defender takeaway, with no inline citation:
*"Note also that two of the affected organisations' own customer notices did not name CEVA at all, which
means an organisation monitoring for supplier incidents by watching for its suppliers' names in the press
would have missed its own exposure here."*

No cited source states this, and no cited source supports the count. ICTMagazine.nl says only that Bol
and De Bijenkorf *"waarschuwden voor een beveiligingsincident bij een externe logistieke partner"* — a
paraphrase of what those notices said, not an assertion that they omitted CEVA. And the entry's own
primary source contradicts the claim for the most likely candidate: bol.com's notice names CEVA
explicitly — *"On 5 August, we informed you about a security incident at CEVA Logistics, a logistics
service provider that bol works with"*. The run record separately concedes that "the Ajax and Ace & Tate
customer notices were not fetched first-hand", so the run is asserting the contents of documents it did
not read. Remediation: drop the sentence, or replace it with the sourced weaker version (early downstream
notices referred to "an external logistics partner" rather than naming the supplier, per ICTMagazine.nl)
and cite it.

### Editorial / less-is-more flags (advisory)

**F5 — macOS update entry: the summary fuses two distinct Huntress statements.** *"with Huntress separately
counting tens of thousands of exposed hosted bare-metal Macs **still being provisioned from vulnerable
images**"*. Huntress says (i) *"a cursory search on Censys reveals tens of thousands of potentially
vulnerable hosts"* (correctly scoped — the search is over hosted-bare-metal provider ASNs and ports, so
the entry's characterisation of *what* was counted is right) and, separately, (ii) *"at the time of
writing, some of these providers have not yet incorporated the latest Apple updates into their base
provisioning image"*. The summary's trailing clause applies (ii) to the whole of (i). The body states
both correctly and separately. Advisory; the main agent may leave it.

**F6 — run record: pipeline-internal vocabulary in the published notes.** Three instances of "sub-agent"
plus "spawned": *"A scoped follow-up sub-agent was spawned specifically to test that"*, *"The follow-up
sub-agent was sent to establish exactly that"*, *"a scoped follow-up sub-agent re-swept for any substantive
technical publication"*. The run record's notes body is published, and the style rule bars workflow-internal
language there. A prior iteration in this store logged the identical advisory, so this is a recurrence
rather than a new defect class. Reader-facing equivalents ("a scoped follow-up sweep") carry the same
meaning. Advisory; not blocking.

### What I checked and found clean (answers to the specific questions raised)

**Evidence-quote fidelity — clean.** All twelve `evidence[]` quotes across the four entries are contiguous
verbatim substrings of the live pages. One initially failed my automated substring test — the Calif quote
beginning *"screensharingd, the program answering those connections, runs as root…"* — and the failure was
an artifact of my own tag-stripping inserting spaces around the page's `<code>screensharingd</code>` and
`<code>root</code>` elements. As rendered, the sentence reads exactly as quoted. Not a defect. The CEVA
TechCrunch fragment *"such as if the company knows how much personal data was taken, or if Ceva has
received any communication from the hackers, such as a ransom demand"* matched exactly; the curly-apostrophe
avoidance worked.

**Contradiction (a), macOS root cause — real, not manufactured; `verification: contradicted` is correct.**
Huntress (2026-08-07): *"The daemon's frame-length validator erroneously returns a stale success status, so
the connection is treated as authenticated"*, explicitly of CVE-2026-65400 (*"The PoC, tracked as
CVE-2026-65400, successfully exploited a Screen Sharing service…"*). Calif (2026-08-10) assigns that same
mechanism to @osxreverser's uncredited bug — *"@osxreverser's bug is a single wrong return. A length check
bails out early on an oversized frame and hands back a value that happens to be the success code from the
read just before it"* — and then: *"Where the first bug is a stale return value, the second is a state
machine desync"*, with *"26.6.1 closed a second, independent bug (CVE-2026-65400) sitting in the same
source file"*. These are incompatible assignments of one mechanism to one CVE id, not two compatible
descriptions. Reporting both without adjudicating is the right call, and the sourcing_note states the
disagreement accurately. Everything action-bearing (pre-auth, root, fixed versions, hardening ineffective)
is agreed by both and correctly stated. `status: [poc-public]` is defensible: Huntress states a public PoC
is tracked as this CVE, even though Calif withholds its own.

**Contradiction (b), CEVA data provenance — correctly hedged in the body** (see F2 for the attribution
defect, which is separate from the hedging).

**CEVA ATT&CK mapping — both halves of the call hold.** `T1005` is not over-mapped: the sources go beyond
"may have been viewed or copied" — TechCrunch states *"The hack at Ceva also resulted in a data breach,
affecting a large amount of personal information"* and Valve *"learned on August 7 that data was taken from
Ceva's systems"*. Collection of data from the compromised systems is stated, so the minimal mapping is
evidence-bound. Rejecting `T1199` is correct: Trusted Relationship describes an adversary leveraging a
third party's access to enter the *target's* environment, and no source describes any downstream network
being entered — bol.com explicitly states *"No bol systems were affected"*. Recording the rejection with
its reason in the run record is the right treatment.

**Priority calibration — all four correct.** Gunra `high`: multi-agency advisory, KEV-listed edge access
vector, constituency sectors named, but no hour-scale new exposure — correctly not `critical`. macOS
`high`: pre-auth remote root with a public PoC and ~40k exposed hosts, but patched since 2026-08-06 and no
in-the-wild exploitation reported — `high` rather than `critical` is right, and it is well above `notable`.
Belgian eID `notable`: fully remediated 2026-06-01/2026-07-22, no CVE, value is architectural. CEVA
`notable`: no vector, no product, no actor. Nothing in the run clears the critical bar and nothing is
under-alerted. The Gunra deep-dive selection is sound — 36 evidence-bound techniques, a durable
identity-plane persistence mechanism and a recovery lever, none of which compress into a short entry; no
`ransomware-affiliate` deep dive in the prior-coverage window; the length is earned rather than padded.

**Belgian eID relevance — the justification is honest, and the entry is stronger than the framing admits.**
This is not an out-of-nexus item needing a transferable-lesson rescue: the affected software is used by
"eight of Belgium's ten largest banks and over 60 government agencies" (SecurityWeek, 2026-08-10),
i.e. European public-sector and financial-sector identity infrastructure, squarely inside the coverage
focus, and it underpins eIDAS qualified signatures — an EU-wide legal instrument the constituency relies on
in cross-border workflows. The architectural generalisation in the Defender takeaway is a bonus, not the
load-bearing justification. The out-of-window primary (2026-08-07) surviving on the in-window SecurityWeek
report (2026-08-10) is a correct call: broad disclosure landed in-window, `event_date` correctly anchors to
the primary, and the technical detail all comes from the discoverers. Every technical claim I spot-checked
against the researcher write-up is exact, including the 48-byte pinToken layout (AES-128 key from bytes
0,2,…30; ciphertext from byte 32; hardcoded IV recovered from the binary), the activationToken's
UUID/TTL/features-bitmask decode, the Doccle.be 24-hour all-operations token, the `.dll`-substring-only
constraint on the `library` parameter, the polyglot filename trick, and the full 146-day remediation
timeline.

**Gunra entry — no truth defects found.** Every claim I tested against AA26-222A is exact, including the
ones most at risk of drift: the `forticloud-sync` super-user account created via scheduled tasks on
vulnerable FortiOS (advisory Table row, verbatim), the OTP-value MFA backdoor on the VDI authentication
portal, the 22:00–06:00 activity window (advisory: "10:00 p.m. – 06:00 a.m."), ChaCha20 + RSA-4096 and
`.ENCRT`, the WMI shadow-copy deletion, the deletion of backups at both the primary and DR sites, the
tens-of-terabytes exfiltration, and the `.GNRA` Linux `srand(time(NULL))` key-reconstruction weakness with
its preserve-the-evidence instruction. The Breakglass Intelligence corroborating source resolves, is dated
2026-03-12 as cited, describes the time-seeded `rand()` weakness, and is the advisory's own note [14]. Both
Fortinet CVEs are live in the KEV catalogue, so `status: [exploited, cisa-kev, patch-available]` holds. No
IOCs leaked into the entry despite an advisory full of them.

**Frontmatter ⇔ body, sourcing, classification.** All `cves[]` records check out: CVE-2026-65400's
`cvss: "7.1"` matches the NVD record (CVSS:3.1 base 7.1, HIGH) and its affected/fixed strings match Apple's
own version list; the two Fortinet records honestly record "n/a"/"not stated in this advisory" rather than
inventing a range. All 43 `techniques[]` ids across the run resolve to active ATT&CK v19.2 techniques; the
Gunra set mirrors the advisory's own mapping table, and the macOS additions (T1543.004 Launch Daemon,
T1546.004 Unix Shell Configuration Modification) are each anchored to a Huntress-stated persistence path.
No entry is single-source, so no F12. Every primary is the right kind (joint-advisory authority, researcher
write-up, research-lab post, first-party victim notice) — no NVD/CERT-only primaries, no landing pages, no
generic URLs. Admiralty codes are consistent with `sources/sources.json` letters (cisa-advisories A →
Gunra A/1; calif-codex B and huntress B → macOS B/2; securityweek B → eID B/2; CEVA B/1 on three sources
including a first-party notice). `org_triage: null` and `watchlist_hit: false` throughout, correct for a
deployment with neither configured. The macOS entry's `update_of` target is the right entry and the body
carries only delta.

**Action items — all four shipped actions clear the bar, and both empty lists are correctly empty.** The
Gunra pair are one-time hunt/IR tasks derived from this advisory's own mechanics (authentication-file change
history plus repeated-OTP validation; evidence preservation before rebuild on `.GNRA` hosts), not
restatements of the body's standing detection concepts. The macOS pair are concrete and version-specific,
and the overlap with the 2026-08-08 entry's single action is justified by the delta — the new fact that the
usual hardening steps do not block the bug changes what the task means. The eID entry (remediated 146 days
ago, no CVE, no deployment in this constituency to patch) and the CEVA entry (no vector, no product, no
actor) correctly ship `actions: []`.

**Coverage completeness — no gap found.** The four published entries plus the six documented borderline
drops account for every item in the sub-agent findings files. Each drop is defensible: the two leak-site
claims (Elixi International SA, Université Libre de Bruxelles) are unconfirmed extortion listings that
correctly do not ship; the React-hook package backdoors are a May incident that never reached the npm
registry; ClamAV DoS is routine patch-cycle; Liechtenstein carries no forensic delta; Gagny is recycled. I
probed independently for omissions: NCSC-CH's security hub has published nothing since 2026-08-07 (outside
the window); the actively-exploited items surfacing in search for this period (TeamCity CVE-2026-63077,
N-able N-central CVE-2026-18577, Cisco Secure FMC) all pre-date the window and appear in prior coverage
(2026-08-02 weekly management-plane entry, 2026-08-02 vuln status roll-up); the Canton Graubünden
SharePoint incident that a Swiss-region search surfaced is already covered at 2026-08-06 and in the W32
weekly. Coverage looks complete for this window — I could not name a plausible in-window source for
anything the run missed.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 0, advisory: 2)

All four truth findings are in one entry
(`entries/2026-08-11/ceva-logistics-fulfilment-breach-ten-controllers-notified.md`) and all four are
attribution/sourcing repairs rather than substantive corrections — none requires the entry to be dropped or
re-researched, and none of the other three entries or the run-record telemetry needs a truth fix. F5 and F6
are advisory and may be left.

### Findings summary (machine-readable)

See `work/2026-08-11T0411Z-intel/verification.iter1.findings.yaml` (identical payload).
