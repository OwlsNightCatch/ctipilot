# Retrospective truth pass — batch B3

**Model:** Opus 5 (`claude-opus-5`)
**Run:** 2026-08-09T1315Z-audit · batch B3 of 4 · 20 entries (2026-08-05 → 2026-08-07)
**Structured findings:** `work/2026-08-09T1315Z-audit/truth-B3.yaml`
**URL ledger:** `work/2026-08-09T1315Z-audit/url-liveness.tsv` (45 URLs appended across two passes)

## Verdict tally — all 20 entries

| verdict | n |
|---|---|
| factual-error | 1 |
| imprecision | 6 |
| clean | 13 |

**Coverage: 19 of 20 `fetched`, 1 `partial`.** Every entry carries a real verdict backed by a source read in
this pass. The single `partial` is Canton Graubünden, whose primary (`www.gr.ch`) is serving a site-wide
maintenance page; its two corroborating sources were fetched and independently support the entry's substance.

Every `cves[]` id and CVSS across the nine CVE-bearing entries — 32 CVEs in total — was checked against the
per-CVE authority (vendor PSIRT page, CSAF JSON, or the `cveawg.mitre.org` CNA container), never against a
roundup. Every one of the ~40 `evidence[]` quotes in the batch was checked as a literal contiguous substring.
Every ATT&CK id on all 20 entries was resolved against the pinned dataset.

---

## The one factual error

**`entries/2026-08-05/thermo-fisher-genetic-analyzer-dna-file-integrity.md` — the "no patch" framing is
false, and it is the entry's whole thesis.**

The entry says, in the title, headline, summary, `cves[0].status: [no-patch]`, `cves[0].fixed`, the
`no-patch` tag, the body twice, and its single action item, that Thermo Fisher offers no fix and that the
control must be architectural because there is nothing to wait for. CISA's ICSMA-26-216-01 — the entry's sole
cited source — carries eight `vendor_fix` remediations. Five name concrete patched versions with download
URLs (3500/3500xL DCS 4.0.3, 3730/3730xL DCS 5.0.3, SeqStudio DCS 1.2.6, SeqStudio Flex 1.2.1, GeneMapper
ID-X 1.7.4); only the three legacy ABI PRISM / 3130 products are EoL with no update.

The fix is not incidental to the entry's argument — it is the exact control the entry says does not exist:

> "The security updates implement the use of digital signatures on the instrument software that adds an
> extralayer of protection. Moving forward, this will help users verify that data files have not been
> modified."

The entry's takeaway argues at length that the instrument software "will never notice" a post-hoc edit and
that only an append-only archive makes tampering detectable. The vendor shipped file signing.

No timing excuse: CSAF tracking shows `version: 1`, one revision, `initial_release_date` =
`current_release_date` = `2026-08-04T06:00:00Z`. The advisory has never been amended, so the vendor fixes
were on the page when the run read it.

### Transport lesson (generalises beyond this finding)

The Mitigations block did not surface in the CISA **HTML** render for two of three transports. Only the CSAF
JSON exposed it reliably. **For CISA ICS/ICSMA advisories, treat
`raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/...` as ground truth, not the HTML page.** The
same JSON also gives the revision history, which is what let this pass rule out the "published later"
defence.

---

## The six imprecisions

1. **Talos AI prompt-log** — "scanned on the order of 18 million target hosts" converts a checkpoint *line
   offset* into a host count. Talos: *"a checkpoint file recording a resume position at line 18,222,511"*,
   and separately *"The pipeline's input list ("target.txt") contained 9,180 unique hosts"*. The entry drops
   the 9,180 figure — the one that measures real targeting breadth — and inflates hosts by three orders of
   magnitude.

2. **Unit 42 NOVA** — "5,421 findings tied to 1,280 vulnerable dependencies" collapses a sum into a ratio.
   Unit 42 gives 5,421 as the **total** of two disjoint buckets: *"1,280 flaws in dependency packages"* plus
   *"4,141 downstream exposures where an application could reach a vulnerable dependency through its own
   code"*. The 4,141 figure — which quantifies exactly the downstream consuming-application exposure that is
   the entry's own analytical point — never appears. The follow-on "a majority validated as exploitable"
   does hold (2,776 of 4,141).

3. **TeamCity KEV** — substitutes a generic transport for a named protocol in three places. JetBrains says
   exploitation runs *"via the TeamCity agent polling protocol"*; the entry renders this as "an
   unauthenticated attacker with HTTP(S) access", then builds the summary ("needs only HTTP(S) reachability")
   and the takeaway ("requires only network reachability") on it. Compounding this, the entry asserts CISA's
   catalog entry does not name "the observed intrusion path" — the KEV `shortDescription` names the protocol.

4. **Traefik multi-tenancy** — "No CVE identifiers have been assigned" was **correct at compose time** (run
   2026-08-05T0412Z; CVEs reserved 2026-08-05T18:14Z, published 2026-08-06T16:24–16:38Z) but the store is now
   stale. GHSA-fgjj-px3w-67xx = CVE-2026-71327, GHSA-62fc-8686-hfmq = CVE-2026-71325, GHSA-6765-c87h-8mrf =
   CVE-2026-71326. Three real flaws are currently invisible to the CVE dedup index. Wants an `update_of`.

5. **Adobe APSB26-120** — the CVE table is flawless. One citation-adjacency defect: "the third distinct wave
   ... since late June" is cited to APSB26-114, one bulletin covering one wave, which carries no wave count
   and no since-late-June framing. The quantifier rests on this brief's own prior coverage.

6. **Jamf fake-Zoom** — a first-ness quantifier hardened past its source in the body: "introduces a runtime
   macOS malware has not used before as a downloader stage" is categorical about macOS malware generally.
   Jamf claims only its own observation and narrows it to a campaign class: *"The use of .NET as a macOS
   downloader is a technique we had not previously observed in campaigns of this kind."* The title and
   summary hedge correctly; the body sentence drops both the observer and the qualifier.

---

## Verified clean — highlights

- **cPanel** — the strongest sourcing discipline in the batch. It separates what the vendor page says
  (impact, versions, mitigation) from what only the HackerOne CNA record says (root cause, both CVSS v4.0
  scores), and every attribution is exactly right.
- **Keycloak** — all seven Red Hat CNA scores match (7.4 / 7.4 / 8.8 / 8.1 / 8.1 / 5.4 / 6.5), every `auth`
  value matches its vector's PR field, and each per-flaw mechanism matches the Red Hat description.
- **Veeam** — all ten CVEs, all ten CVSS v4.0 scores, both build pairs, both quotes, and the AC:H observation
  on CVE-2026-58073 verified against KB4892/KB4893 directly.
- **HPE Aruba** — verified line by line against the PGP-signed CSAF, including the 9.6.x-only scoping and the
  workaround text. HPE's own Resolution section lists a 9.7.0.x target while its Affected section excludes
  that branch — the internal oddity that makes CERT-FR's wider scoping plausible. The entry surfaces the
  disagreement instead of resolving it, which is right.
- **LiteLLM** — wunderwuzzi's own ATT&CK mapping in the originating post lists T1557 and T1565.002: the exact
  two ids the entry carries. Independent confirmation of a mapping choice, not just a claim.
- **Water-PLC** — attribution restraint materially better than its own primary. The Record's framing includes
  *"multiple sources pointed the finger at Iran"*; the entry explicitly declines to adopt it, citing the same
  article's record that federal agencies have not attributed publicly. SecurityWeek carries the pump-station
  detail verbatim.
- **CHAINDROP** — every Elastic figure confirmed, and the OX Security dead-man's-switch contradiction is
  handled exactly as a contradiction should be: reported, attributed, not merged, and sequenced around.
- **ENDLESSDOORS** — all twenty model names match VulnCheck's list exactly, and the entry's refusal to invent
  a CVSS where the discloser publishes none is correct and stated.

## The one partial

**Canton Graubünden.** `www.gr.ch` is serving a site-wide maintenance page (*"Wartungsarbeiten - Lavurs da
mantegniment - Lavori di manutenzione"*) on every path including the site root. All three transport rungs
were tried and all returned the same page: `WebFetch`, the bridge (`tools/fetch_source.py url`), and the
last-resort jina reader. The URL is live-but-temporarily-blanked, not broken. The two `gr.ch` `evidence[]`
quotes remain unverified pending the maintenance window closing — **the only outstanding re-check in B3.**

Everything reachable independently supports the entry: the persoenlich.com (Keystone-SDA) quote is verbatim,
and Lorenz Tanner's name and role, the 29 July afternoon intrusion, the hedged federal-link hypothesis, the
5 August out-of-band update and the BACS coordination are all confirmed there.

## Mechanical checks — all 20

- **ATT&CK ids:** every id on all 20 entries resolved in the pin (ATT&CK 19.1; 697 active techniques / 475
  active sub-techniques). **Zero unknown, zero revoked, zero deprecated.** Each was also judged for
  behavioural fit against the body and its sources; all hold.
- **IOCs:** none found. Several entries explicitly record that they are withholding hashes, hostnames,
  package names and a contract address their sources publish.
- **Frontmatter ⇔ body:** no contradictions on any of the 20 beyond those recorded as findings above.
- **`closed_sources`:** empty on all 20 — nothing to trace.

## Residual for the audit

1. **Re-fetch the two `gr.ch` quotes** once the canton's maintenance window closes (only open item).
2. **Traefik CVE backfill** — three flaws missing from the CVE dedup index; needs an `update_of` entry.
3. Two second-order claims not re-fetched, both internally coherent and neither load-bearing: CERT-FR
   AVI-0969's 9.7.0.x scoping (HPE Aruba entry) and NCSC-2026-0276's four-CVE scope (Veeam entry).
