**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-10T06:09:41Z · ended_at=2026-08-10T06:22:53Z · duration_seconds=792
**Self-telemetry:** urls_checked=11 · webfetch_calls=0 · bridge_fetches=11

## Verification report — 2026-08-10T0411Z-intel (iteration 3)

Cold read of all 18 entries end to end plus the run record, the coverage backlog and the prior-coverage
index. Prior-iteration deltas were also walked (the spawn message supplied them), and the four
confirmations requested are answered in § Prior-iteration deltas below. Transport: `tools/fetch_source.py url`
throughout; every quote check was run against tag-stripped HTML with empty-string replacement and
typographic-apostrophe / NBSP normalisation only.

### Citation does not support the claim

**F1 — `2026-08-10/retelit-qilin-italian-telco-cloud-operator-public-sector`: the Bismark chronology is
off by three days and inverts primacy.** Body: *"The listing first appeared on 11 July and a
document-and-passport sample followed on 14 July — corroborated independently the next day by an Italian
trade outlet reporting the listing with no company confirmation at that point ([Bismark.it,
2026-07-12](https://www.bismark.it/9139/retelit-nel-mirino-del-ransomware-qilin-colpito-uno-dei-principali-operatori-italiani-delle-telecomunicazioni/))"*.
I fetched that page this iteration: title *"Retelit nel mirino del ransomware Qilin…"*, and
`article:published_time` / `datePublished` = `2026-07-12T05:54:09+00:00` (visible dateline "Last updated:
12 Luglio 2026 9:12"). "The next day" attaches to the immediately preceding date, 14 July, and so reads
as 15 July. Separately, the cited primary states Bismark was **first**, not corroborating: *"A quasi due
mesi dalla scoperta dell'attacco, riportato la prima volta dal blog di settore Bismark"*. What Bismark
does support is the rest of the clause — it reports the listing and says *"al momento, non risulta
confermata ufficialmente dalla società"*. Fix: name the date ("first reported by an Italian trade outlet
on 12 July, the day after the listing appeared") instead of a relative day.

**F3 — `2026-08-10/linux-bridge-stp-timer-uaf-no-cve-public-exploit`: "independently" is not what the
advisory says.** Body: *"found by two researchers independently during its TyphoonPWN 2026 competition"*.
The cited SSD advisory (fetched this iteration; title *"Linux Bridge STP Timer Use-After-Free"*,
`datePublished` 2026-08-05) says under **Credit**: *"Two independent security researchers, n132 and sven
sze, submitted this during our TyphoonPWN 2026 and won second place in the Linux PE category."* That is
two unaffiliated researchers making one joint submission — not independent co-discovery, which is a
different and load-bearing claim (independent rediscovery is a standard exploitation-likelihood signal).
The entry's own summary is already correct ("submitted by two researchers during TyphoonPWN 2026"); only
the body sentence overstates. All three of this entry's SSD evidence quotes verified verbatim, and the
mirror-commit quote verified against the commit capture.

### Unsupported / hallucinated facts

**F2 — `2026-08-10/pam-rootok-identity-shuffle-as-anti-forensics-xmrig`: a body quote truncated with a
fabricated full stop, dropping the mechanism.** Body: *"if SOC analysts only remediated the root
compromise, the botnet implant would simply regenerate."* Group-IB's sentence reads *"…the attackers
ensured that if SOC analysts only remediated the root compromise, the botnet implant would simply
regenerate **from the shadowed accounts**."* The entry's own `evidence[]` record stops honestly at
`"…would simply regenerate from"`, so frontmatter and body disagree about where the sentence ends, and
the dropped clause is the part that names where regeneration comes from. This is the same defect class
the run record says it repaired for the Forescout and CISA quotes ("cut mid-clause with a fabricated
full stop"). Milder second instance in the same entry: *"transitions into a fileless state, running
entirely from memory."* — the source reads *"running entirely from memory (RAM)."* Fix both by extending
the quote or ending the sentence outside the quotation marks.

**F4 — run record: "seventeen entries" contradicts `entries_published: 18`.** § Verification & coverage
notes, para 2: *"Everything published here therefore comes from two places: the fifteen open rows of
`state/coverage_backlog.md`, and three uncovered items this run's own completeness sweep recovered. That
is why a quiet window produced seventeen entries, and it is not a volume increase"*. Frontmatter says
`entries_published: 18`; 18 files exist; I recounted the files and the same notes body already says "6
action items across 18 entries, with 12 entries carrying none" (my recount: 18 entries, 6 actions, 12
with none, 5 `update_of` — all three match `entries_updated: 5`). `state/coverage_backlog.md` records a
sixteenth row — Retelit — *"opened as a backlog row by this run, then published within the same run"*, so
the "two places / seventeen" arithmetic is the pre-Retelit state. Same class as iteration 1's action-item
count finding. Fix the number and let the sentence account for the in-run addition the later Retelit
paragraph already narrates.

### Surface contradiction

**F5 — `retelit-qilin…`: Retelit's "promptly informed affected customers" is contradicted inside the same
primary, and the takeaway leans on the uncontested reading.** Body: *"Retelit says it informed affected
customers promptly, which is compatible with the public silence and is exactly why the contractual
channel, not the press channel, is the one to test."* The 6 August update of the cited primary reports
the customer side: *"In seguito alla comunicazione diramata dal Cert Agid alla fine di luglio, numerosi
clienti riferiscono di aver scritto a Retelit per chiedere come mai non fosse arrivata alcuna
comunicazione in seguito al data breach"* — numerous customers say no notification reached them, and only
CERT-AGID's late-July message prompted them to ask. The same passage is what carries the "numerous
customers" and partial/total backup-failure material the entry already uses, so it was read. An entry
whose stated discipline is holding four claim tiers apart should surface this as a contradiction
(`Contradiction:` line in § Verification Notes plus one body clause), not resolve it silently toward the
company's account.

### Needs more research

**F6 — `retelit-qilin…`: the public-CERT notification path — the entry's own thesis in evidence — is
missing.** Body: *"No Italian public administration has confirmed downstream impact."* The primary carries
the concrete answer one step short of confirmation: *"Cert Agid … è invece venuta a conoscenza
dell'incidente informatico solamente il 30 luglio, data nella quale ha iniziato ad avvisare i responsabili
di sicurezza di tutte le pubbliche amministrazioni potenzialmente coinvolte o che in ogni caso si servono
dei servizi di Retelit. Tra questi anche Cineca, Lepida e Infocamere"* — the article adds that Lepida and
InfoCamere provide SPID and digital-signature services and Cineca acts as a certified digital preserver.
For this profile that is the operational fact: a national CERT on the profile's own carve-out list
learning of the incident seven weeks in and notifying every potentially affected public administration,
with named identity and preservation providers among them. It also gives the "at least three
digital-identity providers" customer figure its concrete referent. One or two sentences; same location as
F5.

### Editorial / less-is-more flags (advisory)

**F7 — `2026-08-10/interlock-volatility3-winpmem-credential-theft`: ClickFix user-execution step unmapped.**
`techniques: [T1189, T1547.001, T1069.002, T1558.003, T1021.001, T1053.005, T1003.002, T1003.005]`. The
summary says *"Initial access was a ClickFix paste-and-run lure"* and the body describes it step by step
(*"five seconds later the page read the clipboard … Thirteen seconds after that the user pasted an
attacker-supplied command into the Run dialog"*). That behaviour is `T1204.004` Malicious Copy and Paste,
which I confirmed active (not deprecated, not revoked) in the pinned dataset at ATT&CK v19.2. Everything
else on the list is body-described and Sophos-supported; the drive-by is mapped but not the user-execution
step it depends on. Advisory — the main agent may leave it.

**F8 — `2026-08-10/zabka-supplier-account-jira-access-confirmed`: the superlative survived in the headline,
and it turns out to be sourceable.** `headline: "A supplier account reached Jira at Poland's largest
convenience chain…"` while the summary deliberately reads *"a Polish convenience-store franchise chain"*.
Iteration 1's F14 remediation is logged in the run record as having dropped an *unsourced* superlative;
both halves are inaccurate. It survives in the headline — the field the rendered 24 h window shows at the
top — and it is in fact supported by a cited corroborating source: RMF FM (fetched this iteration) says
Żabka *"utrzymuje pozycję lidera na rynku sklepów convenience w Polsce"* with *"ponad 12 tys.
franczyzobiorców"*. It is absent from the Niebezpiecznik primary (checked: no `najwięks*` occurrence).
Either align the two fields or keep the superlative deliberately with RMF FM behind it; the logged
finding note should not stand as written. Advisory.

### Prior-iteration deltas — the four confirmations requested

1. **Evidence quotes and tier discipline (iter-2 F4).** All **eight** Retelit evidence quotes verify as
   contiguous substrings of `retelit_raw.html` after tag-stripping (the only deltas are U+2019 vs `'`,
   NBSP and `«»`, i.e. glyph normalisation, not splices). The two new ones are exact, including the
   guillemets: *"Secondo quanto riferito da una fonte coinvolta nell'evento, l'attacco sarebbe partito dal
   computer di un amministratore di sistema nel quale sono state carpite le password che hanno permesso
   all'attaccante di compiere dei «movimenti laterali»"* and *"è deducibile che il presidio di sicurezza
   (Soc, Security Operations Center) non abbia rilevato i movimenti laterali né la cifratura dei server se
   non quando era troppo tardi"*. Both framings hold in the body and are not hardened: the conditional is
   named as such (*"relays an account from an unnamed source involved in the incident, in the Italian
   conditional"*, *"the attack **is said to** have started"*) and the detection failure is explicitly the
   outlet's inference (*"not reported as fact either but as the outlet's inference from the volume already
   published"*, *"it **is deducible** that"*), closing with *"Neither claim comes from Retelit, and
   Retelit's own statement addresses scope rather than sequence."* The four tiers stay separate. **Holds.**
2. **T1078 / T1486 now have body behaviour, with no over-mapping.** T1078: captured administrator
   passwords authenticating to systems the endpoint legitimately reaches. T1486: *"the encryption of
   servers"* / *"the encryption stage arrives before anything flags the movement"*. No lateral-movement
   sub-technique is asserted anywhere — correctly, since the primary names no protocol; the body says only
   *"«movimenti laterali»"* / "move laterally". No T1021.* and no T1003/T1555 were added either; leaving
   the credential-store technique unmapped is the right call because the source says only *"sono state
   carpite le password"* and names no store or mechanism, so a sub-technique would be invented. **Holds.**
3. **The Triage discriminator derives from the cited mechanism.** *"an administrator account
   authenticating across many systems is precisely what administrator accounts do, so breadth alone
   discriminates nothing; what separates this from routine work is the pairing of credential-store access
   on the workstation with a subsequent authentication fan-out that does not match the operator's normal
   maintenance pattern or change window."* Both halves are the source's own two steps (credentials taken
   from an administrator's computer → lateral movement) read as telemetry; nothing is asserted that the
   mechanism does not carry, and it is framed as a discriminator rather than as a reported IR finding.
   **Holds.**
4. **Iteration-1 remediations spot-checked (6 of 21) — all hold.** Interlock: *"across the estate, not all
   endpoints were in fact running protection of any sort"* matches Sophos verbatim, and the false
   unprotected-Patient-Zero claim is gone (Sophos: *"Patient Zero was a Defender-managed endpoint running
   Windows 10"*); the "roughly 26 hours" and day-long pause check out (*"slightly over 26 hours"*, *"a
   24-hour break"*). NatJack: the partial-mitigation framing is consistent across `cves[].status:
   [mitigation-only]`, `fixed`, summary, body, sourcing note and the action item; the ephemeral-port point
   is attributed to the researcher as a rebuttal; CVSS 8.3 is stated as Microsoft's; "seven stable and
   long-term point releases plus mainline" is used throughout; the five-primitive count is enumerated in
   the body. Linux bridge: the `br_topology_change_detection()` sentence is now attributed to the kernel
   commit and the source date is 2026-06-30 with the six-week lead carried into body and takeaway; the
   capability/namespace paragraph is explicitly separated into "what the sources establish" vs "this
   entry's assessment". Coding-agent CI: CVE-2026-54316 is bound to the allowlist-scoping round with
   Anthropic's own sentence quoted, the other two rounds are stated to carry no CVE, and CVE-2026-12537 is
   cited to the OSV record; the `/proc/$PPID/environ` body quote verifies verbatim against the Novee
   capture. wp2root: the KEV listing is cited to the catalog JSON and the flaw to the kernel CVE
   announcement, and no EPSS figure appears in body, action or frontmatter. Rapid7: the entry carries no
   action item and the weaponisation-not-exploitation framing is intact.

### What I checked and found clean

- **URLs (11 fetched this iteration, all via the bridge):** Retelit ×3 (IrpiMedia, Bismark, retelit.it
  press index), Bismark re-fetch for its date, SSD advisory, cgit.freebsd.org commit, blog.calif.io,
  natjack.io, go.synack.com, securelist.com, sekurak.pl, rmf.fm. All resolved to specific pages with
  matching titles; no 404, no homepage redirect, no listing index standing in for an article. Two prior
  iterations swept the full 40-URL set; I prioritised the newest entry, the deep dive and the
  high-priority primaries and note the sampling here.
- **`https://www.retelit.it/it/stampa/comunicati-stampa` as a source record.** It is a press-release
  index, which is normally an F2. I am deliberately **not** flagging it: the claim attached to it is the
  *absence* of a statement on that channel, which is load-bearing for the headline ("in a right-of-reply,
  not a press release"), the sourcing note says exactly that, and no specific article can exist to replace
  it. The gate passes it. Flagging it would force a worse entry.
- **Quantifiers.** Retelit: 270,000 files (*"numero complessivo dei file: 270mila"*), "at least 300 GB"
  and the placeholder size (*"Sebbene sia indicata una dimensione di 0 gigabyte, IrpiMedia stima si tratti
  di almeno 300 Gb"*), 193 public administrations, 3 of 38 data centres / ~7%, Verona-Rome-Milan and the
  ACN-certified backup site (*"proprio quest'ultimo è il data center certificato da Acn per la gestione dei
  backup e la continuità dei servizi in caso di incidente informatico"*), Leonardo Genoa/Turin documents
  dated October 2025 and April 2026 — all verified. The plural "customers … complaining of partial or total
  failure of backup recovery" is supported by the 6 August update (*"numerosi clienti"*; one restored
  *"solamente del 70%"*, a north-eastern company *"perso irrimediabilmente"* everything) — I checked this
  specifically because the article's summary box mentions only one client. ESXi: "21 distinct methods",
  "six categories", SCATTERED SPIDER and Akira all present in the CrowdStrike text. BINDCLOAK: Kaspersky
  does name Central Asian **and** Syrian government organisations, so "Central Asian and Syrian government
  targets" holds.
- **Prior-coverage self-references.** Both are true: the Forescout entry's "European OT intrusion that ran
  through a mobile carrier's private network" matches the 2026-08-09 CERT Polska private-APN CHP entry, and
  the coding-agent forensics entry's macOS reverse-tunnel case matches the Elastic/Claude Code entry in the
  index.
- **Classification / triage / watchlist.** All 18 entries carry exactly one `classification` block with
  in-vocabulary codes; no `org_triage` block is non-null; no `watchlist_hit: true` and no `watchlist` tag —
  correct for this profile. Reliability letters are consistent with the cited sources' nature (A only where
  a vendor/project/DOJ primary carries the entry), and the credibility numbers track the corroboration the
  entries show, including the deliberate 2s on the single-assessor items and the lowered 2 on Forescout.
- **Style.** No IOCs, no vanity metrics, English throughout, no workflow-internal vocabulary in any entry
  or in the run-record notes. "This run confirmed…" / "this pipeline tracks…" self-references are
  editorial, not workflow leakage.
- **Coverage shape.** Every `vulnerability` entry demands action beyond the regular patch cycle
  (pre-auth reachable on a stock-default port, KEV-listed root step, public exploit with no CVE, a shipped
  Metasploit module, or an unauthenticated interconnect with no patch coming). The five `update_of` entries
  each carry a genuine delta and target the right predecessor. I found **no missed angle I can name a
  plausible in-window source for** — the four window sweeps returned zero, the backlog is drained with each
  row resolved and reasoned, the one row left open (the 1Password patch-remediation study) carries a
  defensible drop reason, and iteration 1's single coverage gap (Retelit) is now published. Coverage looks
  complete.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 2, advisory: 2)

Nothing here questions the run's shape or its hardest calls — the recency stretch, the four-tier
attribution discipline on Retelit, the weaponisation reframing and the deliberate non-updates all survive
a hostile cold read, and the two iteration-2 remediations are correct as applied. The four truth findings
are localised: two quote/paraphrase overreaches (F2, F3), one date-and-primacy slip (F1), and one stale
count in the run record (F4). The two editorial findings are the same omission in the Retelit primary read
from two directions (F5, F6) and are fixable in one place with two or three sentences.

### Findings summary (machine-readable)

See `work/2026-08-10T0411Z-intel/verification.iter3.findings.yaml` — identical payload, 8 records
(F3, F4, F3, F4, F9, F8, F11, F11 in the order F1…F8 above).
