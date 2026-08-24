**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-24T00:09:38Z · ended_at=2026-08-24T00:28:16Z · duration_seconds=1118
**Self-telemetry:** urls_checked=41 · webfetch_calls=1 · bridge_fetches=0 · direct_curl_fetches=44 · offline_page_checks=27

## Verification report — 2026-08-23T2311Z-weekly (iteration 1)

Cold read. All 14 new entries read end-to-end (frontmatter + body), plus the run record.
Every inline URL in all 14 entries was resolved (all 200, no 404 / homepage redirect / listing
index). Every `evidence[]` quote (27 across the run) was re-checked independently as a contiguous
verbatim substring against the run's saved page bodies — **27/27 pass**; the four corrections the
run record describes appear to have held. All 39 distinct `techniques[]` ids were validated against
the pinned `attack/enterprise-attack.json` (v19.2) — all present, none deprecated, none revoked. All
38 entity keys resolve in `entities/registry.yaml`. No IOCs, no vanity metrics, no
workflow-internal language. The `techniques: []` on the Berlin entry is the honest mapping: none of
its four cited sources describes any attacker behaviour, and the entry says so.

The two disclosed transport limits (jina pool at HTTP 402; MSRC and EUVD client-rendered) are
adequately disclosed and I did not treat them as findings. I independently reached ENISA's content
through the EUVD JSON API (`euvdservices.enisa.europa.eu/api/enisaid`), which **confirms** every
ENISA claim in `weekly-w34-exploited-is-now-a-per-authority-opinion.md`: EUVD-2026-63693
`datePublished` Aug 20, `dateUpdated` Aug 22, `exploitedSince` Aug 21, `baseScore` 10.0, and a
single reference — the MSRC page. It also confirms the Zimbra record (`exploitedSince` Aug 18,
`datePublished` Aug 13) and the ShieldBreak record (7.8, `E:P`, "working to provide a high quality
security update"). Every CISA KEV `dateAdded` in both vulnerability entries reconciles exactly
against `pages/kev.txt` (catalogVersion 2026.08.21), and CVE-2026-69836 is indeed absent from the
catalogue.

The findings below are all per-citation adjacency defects plus one factual inversion. They are the
class the run was warned about, and they survived composition.

### Citation does not support the claim

**F1 — `weekly-w34-the-fix-landed-and-the-access-stayed.md`: the CISA KEV addition date is attached to a Kaspersky page published eight days earlier, and KEV is not among the entry's sources.**

Body claim, verbatim:

> "Both flaws were fixed on 2026-06-18, two months before CISA added them to its Known Exploited Vulnerabilities catalogue on 2026-08-20 ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/))."

Same fact in the `summary`: "TrueConf Server was fixed on 18 June, two months before CISA catalogued the chain as exploited".

What the cited page actually says (checked against the run's own saved body `pages/kaspersky-icscert.txt`, and the URL re-resolved 200 this iteration): it confirms the fix — *"The manufacturer addressed the vulnerabilities used by the attackers in the latest TrueConf server update (versions 5.3.9, 5.4.9, and 5.5.5), released on June 18, 2026"* — and the port detail (*"via port 4307/TCP (open by default, according to TrueConf documentation)"*). It contains **zero** occurrences of "KEV" or "Known Exploited", and it was published 2026-08-12, eight days *before* the catalogue addition it is cited for. The KEV catalogue does not appear in this entry's `sources[]` at all.

The 2026-08-20 date is itself correct (`kev.txt`: CVE-2026-72529 and CVE-2026-72530 both `dateAdded: 2026-08-20`) — the defect is the attribution, not the fact. Remedy: add the KEV feed as a corroborating `sources[]` record and split the citation, or drop the catalogue clause from the sentence.

**F2 — `weekly-w34-vuln-status-rollup.md`: the Red Hat record cited says "Not affected", the entry says "Affected with no erratum". This is asserted four times, including in the title.**

Body claim, verbatim (§ Critical, no exploitation reported):

> "Fixed 2026-08-18 in Red Hat build of Keycloak 26.4.15 and 26.6.6 — but the same component is recorded Affected with no erratum in the JBoss Enterprise Application Platform Expansion Pack, so part of the estate has nothing to apply ([Red Hat Product Security, 2026-08-18](https://access.redhat.com/security/cve/CVE-2026-18963))."

Repeated in § No fix exists: "**Keycloak in the JBoss EAP Expansion Pack** — Affected, no erratum, as above."
In the `title`: "led by an identity provider with an unfixed product".
In the `summary`: "where one affected Red Hat product has no erratum at all".
In the Defender takeaway: "an identity provider whose account-recovery path is the account-takeover path with **one product left unfixed**".

What the cited page actually carries. I parsed the product-state table out of the run's **own saved fetch** of that page (`pages/redhat-18963.txt`, fetched 2026-08-23 23:54 — so this was the page state at composition time) and re-fetched the URL live this iteration. Both give the identical record:

```
{"product":"Red Hat JBoss Enterprise Application Platform Expansion Pack",
 "advisory":[], "package":"keycloak-services", "state":"Not affected",
 "delegated_not_affected_justification":"Component not Present"}
```

The full state list on that page is: eleven rows `Fixed` (RHSA-2026:56519 / 56520 / 56523 / 56524, across Keycloak 26.4, 26.4.15, 26.6, 26.6.6), and exactly two rows `Not affected` — the JBoss EAP Expansion Pack and Red Hat Single Sign-On 7. **No product on the record is in an `Affected` state, and no affected product lacks an erratum.**

The adjacent claim in the same bullet is correct and I verified it: RHSA-2026:56523 (26.6.6) lists five CVEs — CVE-2026-9796, CVE-2026-14613, CVE-2026-15571, CVE-2026-17048, CVE-2026-18963 — while RHSA-2026:56520 (26.4.15) lists one. Only the Expansion Pack claim is wrong.

Note for remediation scope: the error originates in the 2026-08-19 operational entry
(`cve-2026-18963-keycloak-reset-credentials-account-takeover.md`, line 96), which is immutable — but
this weekly entry restates it in the present tense and cites the Red Hat page directly for it, and
the run *did* fetch that page. The title, summary, both body bullets and the takeaway all need
correcting, and the `no-patch` tag then rests only on ShieldBreak and misp-stix (which is fine).

**F3 — `weekly-w34-three-ways-to-take-the-agent-off-the-board.md`: a detection observation attributed to Talos that the Talos post does not make.**

Body claim, verbatim (Defender takeaway):

> "There is a fourth observation worth acting on independently of all three: Talos notes that a busy server going quiet for process and image-load events while it demonstrably stays up and serving traffic is itself the signal."

What the cited Talos SPECTRE post actually says. I searched the run's saved body (`pages/talos-spectre.txt`, 26,747 chars flattened) for `telemetry`, `recommend`, `gap`, `sudden`, `absence`, `silence`, `quiet`, `no longer see/receive` — **none of these strings occurs on the page.** Talos states the *effect* only: *"kernel-callback-dependent security products such as CrowdStrike Falcon, SentinelOne, Microsoft Defender, and other well-known EDR vendors are rendered completely blind to new process creations, thread creations, and image load events for the remainder of the session."* The post's only guidance section is "Coverage" (ClamAV signatures and Snort SIDs). It offers no detection observation about telemetry going quiet.

The observation is genuinely good and it is this pipeline's own — the 2026-08-23 operational entry
`spectre-uat-10147-byovd-edr-callback-unlink.md` (line 101) presents it as its own Triage
discriminator: *"That last one inverts the usual reasoning: a sudden absence of routine
callback-derived events from a busy server is itself the signal."* The weekly converted a first-person
analytic judgement into a named-source claim. Remedy: drop "Talos notes that" and present it as the
entry's own inference, which is what it is.

**F4 — `weekly-w34-vuln-status-rollup.md`: the GeoServer release post is cited for an NCSC-CH advisory update it cannot carry.**

Body claim, verbatim (§ Continuing exploitation):

> "GeoServer 3.0.1, 2.28.5 and 2.27.6 shipped on 2026-08-14 and Switzerland's NCSC appended the fixed versions to its advisory on 2026-08-17 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html))."

The cited page (fetched live this iteration, 200, 24 KB) is the GeoServer 3.0.1 release announcement dated "Aug 14, 2026 • Jody Garnett". It confirms the release date and the flaw — *"GHSA-mqjf-5f49-2fjh Unauthenticated SQL injection in the jsonArrayContains filter function against PostGIS layers (High)"* — and confirms that no CVE has been assigned yet (*"This post will be updated with an official CVE number when one is available"*). It contains **no mention of NCSC, Switzerland, or any 2026-08-17 advisory update**; `2.28.5` and `2.27.6` appear only as untitled, undated links in the site-wide "Announcements" sidebar, not as a statement that all three shipped on 14 August.

One trailing citation is carrying a Swiss-authority fact from a different (uncited) source. Remedy:
cite the NCSC-CH advisory for its own clause, or drop the clause.

Two further uncited factual clauses in the same entry that a reader cannot trace: "For this
constituency it lands on an estate already breached twice: the Swiss federal IT provider BIT and
canton Graubünden both disclosed on-premises SharePoint intrusions in early August" (§ Newly
exploited), and "Both were patched before their root causes went public, and Switzerland's NCSC put
both in front of its constituency this week" (§ Critical, WordPress bullet). Both are plausible and
both are presumably in the referenced operational entries, but neither has a citation and neither
is covered by the `sourcing_note`'s delegation, which covers "mechanism, affected and fixed
versions, exploitation evidence and detection guidance" — not third-party authority actions.

**F5 — `weekly-w34-exploited-is-now-a-per-authority-opinion.md`: technical detail folded into sentences whose only citation is the KEV feed, which does not carry it.**

Body claim, verbatim:

> "CISA added CVE-2026-33824, a pre-authentication double free in the Windows IKE and AuthIP IPsec Keying Modules service reachable on UDP 500 and 4500, to its catalogue on 2026-08-18 ([CISA KEV catalog, 2026-08-18](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))."

And in the same paragraph:

> "The same update added CVE-2026-55040, a pre-authentication authentication bypass in SharePoint Server allowing impersonation ([CISA KEV catalog, 2026-08-18](…))."

The KEV record for CVE-2026-33824, read in full from the run's own `pages/kev.txt`, is:
`vulnerabilityName: "Microsoft Internet Key Exchange (IKE) Service Extensions Double Free
Vulnerability"`, `shortDescription: "Microsoft Internet Key Exchange (IKE) Service Extensions
contains a double free vulnerability that could enable remote code execution."` — no ports, no
"pre-authentication", no "AuthIP IPsec Keying Modules". The record for CVE-2026-55040 is
`shortDescription: "Microsoft SharePoint contains a weak authentication vulnerability which allows
an unauthorized attacker to bypass a security feature over a network."` — no "impersonation", no
"pre-authentication".

Both descriptions are almost certainly true (they come from the referenced operational entries) and
the catalogue dates are exactly right, but the UDP 500/4500 pair in particular is a specific,
checkable technical fact hanging off a citation that does not state it — and the entry's own
`sourcing_note` promises the opposite: "Every claim here is a statement about what a named
authority's own record says on a named date, and each is cited to that record." Remedy: move the
mechanism detail out of the citation-bearing clause, or add the Microsoft record as the citation for
the description half.

### Unsupported / hallucinated facts

**F6 — `weekly-w34-two-charge-sheets-named-switzerland.md`: the summary's "seven countries" is in no source this entry cites.**

`summary`, verbatim:

> "the indictment names four Swiss victims — Stadler Rail, Meier Tobler, Crealogix and IHI Ionbond — among ten companies in seven countries"

The entry's three sources are DOJ, cash.ch and 20 Minuten. I searched the run's saved bodies of both
Swiss articles (`pages/cash-zurich.txt`, `pages/20min-zurich.txt`) for `sieben`, `Länder`, `Ländern`,
`Staaten` — **no match in either**. 20 Minuten gives only "In der Anklageschrift sind zehn Firmen
aufgelistet, wobei vier davon Schweizer Firmen waren"; cash.ch names three Swiss victims and no
country count. The body of this entry correctly says only "The indictment lists ten companies, four
of them Swiss" — so the frontmatter overstates what the body's cited sources support (check 4b).

The fact itself is true and traceable: Netzwoche (fetched live this iteration, 200) writes *"Angriffen
auf zehn Unternehmen in der Schweiz, Frankreich, Norwegen, Schottland, Kanada, den Niederlanden und
den USA"* — seven jurisdictions. Netzwoche is a corroborating source on the referenced operational
entry `2026-08-18/zurich-trial-lockergoga-megacortex-nefilim-swiss-victims` but is **not** in this
entry's `sources[]`. Remedy: add Netzwoche as a corroborating record, or drop "in seven countries"
from the summary.

Related, and worth fixing in the same pass: this entry's `sourcing_note` says "the two outlets give
different totals for economic damage". The two outlets this entry cites do not — 20 Minuten gives
"über 100 Millionen Franken" and cash.ch gives no total at all ("Schäden in Millionenhöhe"). The
divergence is between 20 Minuten (100 m) and Netzwoche (130 m), and Netzwoche is not cited here, so
as written the note describes a contradiction the reader cannot see in any listed source.

### Single-source items missing [SINGLE-SOURCE] flag

**F7 — `weekly-w34-ai-bought-throughput-not-capability.md`: the five-agency advisory was not read; its content is relayed from BleepingComputer, which is inline-cited but absent from `sources[]`, and the `sourcing_note` does not say so.**

Body, verbatim:

> "…with read and write access to PLC memory, configuration data and ladder-logic programs ([BleepingComputer, 2026-08-19](https://www.bleepingcomputer.com/news/security/us-warns-of-ai-powered-attacks-on-siemens-plcs-in-critical-infrastructure/), reporting the joint advisory published at [ic3.gov, 2026-08-19](https://www.ic3.gov/CSA/2026/260819.pdf))."

I verified BleepingComputer supports every element of that paragraph (fetched live, 200; Lawrence
Abrams, August 19, 2026): *"the attackers are using artificial intelligence to develop Python
exploitation scripts that use the 'snap7.dll' and 'python-snap7' libraries… These custom tools are
disguised as legitimate OT monitoring software and can provide read and write access to PLC memory,
configuration data, and ladder logic programs over the S7comm protocol… the activity appears focused
on persistent reconnaissance, potentially preparing attackers for disruption"* and *"internet scanning
services, including Censys and ZoomEye… exploit critical and high-severity vulnerabilities, outdated
software, and weak authentication."* So the content is sound. Two problems remain:

1. BleepingComputer is the load-bearing citation for the whole "advisory" paragraph but does not
   appear in `sources[]`. `prompts/cti-run.md` PD-2 is explicit: *"The frontmatter `sources[]` list
   and the body's inline links must agree."* A whole-run scan found this is the only such mismatch
   in the 14 entries (the only other is a reverse case: the EUVD Zimbra record is listed as a
   `primary` source on the roll-up and never cited inline).
2. The `sourcing_note` says "Four independent first-hand publishers plus one corroborating dataset,
   each reporting its own telemetry or its own recovered artefacts." For the joint advisory that is
   not what happened: the PDF is a scanned/binary document that the pipeline did not read (there is
   no `pages/ic3*` artefact, and it defeats `WebFetch`), and the substance is a news outlet's
   account. The run record discloses the MSRC and EUVD transport limits but not this one.

Remedy: add BleepingComputer as a `corroborating` record and add one clause to the `sourcing_note`
naming the advisory PDF as unread and BleepingComputer as the relaying source — the same treatment
the MSRC/EUVD limits already get elsewhere in the run.

### Editorial / less-is-more flags (advisory)

**F8 — CISA KEV feed cited with five different "publication" dates across two entries.**
`https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` is cited as
`[CISA KEV catalog, 2026-08-17]`, `[… 2026-08-18]`, `[… 2026-08-20]` and `[… 2026-08-21]`, and it
carries `date: "2026-08-18"` in one entry's `sources[]` and `date: "2026-08-20"` in the other's. Each
value is a per-CVE `dateAdded`, not the artefact's date; the file the run fetched is
`catalogVersion 2026.08.21`, `dateReleased 2026-08-21T17:46:43Z`. The dates are all individually
correct as facts and the surrounding prose makes the meaning clear, so this is not a truth defect —
but rendered as "[Publisher, date]" the reader reads a publication date. Consider pinning the
`sources[]` date and the inline citation date to the catalogue version (2026-08-21) and keeping the
per-CVE `dateAdded` in the prose, where it already is.

**F9 — `weekly-w34-looking-ahead.md`: the OSV record is labelled as a MISP Project advisory.**
`publisher: "MISP Project advisory (via OSV.dev)"` / inline "[MISP Project advisory via OSV.dev,
2026-08-21]". The cited page (fetched live, 200) states `Source https://cve.org/CVERecord?id=CVE-2026-77710`
and `Import Source …cve-osv-conversion/osv-output/CVE-2026-77710.json` — it is a CVE record mirrored
into OSV, not a MISP-published advisory. Everything the entry draws from it is correct
(`last_affected 2026.7.8`; fixes recorded as commits `3e5e7bda` and `66c654b9`; `Published
2026-08-21`). Minor second point: the clause "The three flaws disclosed on 21 August … have no tagged
release carrying the remediation" is cited to a single-CVE page; the other two ids
(CVE-2026-77755, CVE-2026-77761) do not appear on it.

### Things I checked and found sound (recorded so the next iteration need not repeat them)

- **All 27 `evidence[]` quotes** re-verified as contiguous verbatim substrings (independent re-run of
  `qcheck.check`, not trusting the composition-time pass). Includes the two German Senatskanzlei
  quotes, the curly-apostrophe dpa quote, and both NCSC quotes the run record says were corrected.
- **Every quantifier I could reach**: Sophos 86/34/+4/38/30/26/35 and the 2 Jul 2025 – 29 Jun 2026
  window (all verbatim on the page); Rust 86/90/107 minutes and the locked account; Talos 170,000
  URLs / 17 files / nine-section guide / four Python scripts (`check_paths.py`, `deploy_implant.py`,
  `deploy_shell.py`, `exfil.py` — the page's "three companion Python scripts" is a different set, so
  "four" is right); Recorded Future 1,100 companies / 60 per day / 22 personas / face-swap service /
  ChatGPT assistants / "even when the LLM is wrong"; Oracle 943 patches and **exactly three** CVSS 10.0
  rows, all `Yes` to remote-exploit-without-auth (CVE-2026-61241 OID LDAP, CVE-2026-70880 and
  CVE-2026-70921 Hyperion); Check Point "close to 2,000 compromised WordPress domains" and the
  six BTR.sys Action IDs with Action 3 = arbitrary file write and Action 6 = arbitrary registry write;
  Talos SPECTRE's 13-version offset table, RTCore64.sys (MSI) / DBUtil_2_3.sys (Dell), and the named
  EDR vendors; Bitdefender's seven RAT families, `0123456789abcdef`, `change_this_key`; DOJ's
  14-count S2 indictment, 17 defendants, 144/178/42/11/5/2 victim counts, Switzerland in both foreign
  lists, password spraying and the $20 m figure; CERT.LV 1.2 m / 200 k / since 2008; Tagesspiegel
  "mehr als 50.000 berechtigte Haushalte"; 20 Minuten CHF 4.5 m / CHF 100 m / verdict 10 September /
  "Back-up-Dateien" / Westeuropa und Nordamerika; NCSC UK's seven considerations, four-level network
  model, five sandbox axes (Execution/Network/Compute/Credentials/Data), 24/7 + office-hours rollout,
  ETSI EN 304 223, and **no mention of Australia** (the removal the run record describes is correct);
  EC CRA 10 Dec 2024 / 11 Dec 2027 / 11 Sep 2026 / 27 Jul 2026 guidance; GitLab 9.4 + 7.1, "from 18.2",
  GitLab.com/Dedicated already patched, and "ad-hoc critical patches" vs the 2nd/4th-Wednesday cadence
  (so "outside the scheduled cadence" holds); CERT-EU's 9.3 / 8.8 and the SAML-vs-earlier-builds
  precondition split, verbatim.
- **Weekly dedup polarity.** I read the three prior entries the run claims distinction from. All three
  distinctions hold: W32 `the-vendor-fix-was-not-the-end-state` is about fixes that were bypassable,
  reintroduced the bug, or shipped as the affected version — genuinely the other failure mode; W32
  `cve-record-unreliable-in-both-directions` is about fabricated and missing identifiers, not about
  the exploitation flag on correct ones; W33 `kernel-rootkits-edit-what-windows-reports` is FudModule
  and a Nsiproxy-hooking CoolClient driver falsifying reported state, distinct from this week's
  "does the agent run / is it called" framing (the SPECTRE callback-unlink is the closest overlap, but
  the actors, disclosures and control conclusions differ).
- **W-PD-1.** Every entry answers at least one of the three questions; none is a one-to-one re-list.
  The roll-up's empty `cves[]` is correct, not a contract miss — `check_run.py check_dedup` states
  "per-CVE metadata belongs to the operational entry that owns it and must not be duplicated upward",
  and the `sourcing_note` explains it.
- **`actions[]`.** Thirteen empty lists are the right output for strategic synthesis. The single
  NetNTLMv1 action is concrete, unhedged, self-contained and derived from that entry's own mechanics
  (LAN Manager authentication level on DCs and legacy-exception host groups). No F18.
- **Classification.** All 14 entries carry a `classification` block; every letter in A–F and every
  number in 1–6; no `org_triage`, no `watchlist_hit: true`, no `watchlist` tag anywhere — correct for
  this profile. `A` is used only where a first-party authority document anchors the entry (MSRC/CISA/
  ENISA, Senatskanzlei, DOJ, NCSC UK, Red Hat/Oracle/GitLab/CERT-EU, the AK OÖ / CERT.LV / commune
  first-party disclosures); `B` elsewhere. `2` correctly marks the two genuinely single-source items.
- **Coverage.** I found no in-window gap I can name a plausible source for. The run record's negative
  policy sweep is specific enough to check, and `weekly-annual-reports` being empty is the correct
  rendering rather than an omission. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 1, advisory: 2)

F2 is the one that matters most: a four-times-repeated claim, including in an entry title, that the
cited vendor record contradicts in the run's own saved copy of that page. F1, F3, F4, F5 are all the
same shape — a true fact carried by a citation that does not state it — and F3 additionally puts
words in a named vendor's mouth. F6 is a summary asserting a number no cited source carries. None of
these requires new research; all six are fixable by re-citing or narrowing.

### Findings summary (machine-readable)

```yaml
- code: F1
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w34-the-fix-landed-and-the-access-stayed"
  url_or_quote: "Both flaws were fixed on 2026-06-18, two months before CISA added them to its Known Exploited Vulnerabilities catalogue on 2026-08-20 ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/))"
  summary: "The Kaspersky page was published 2026-08-12, eight days before the KEV addition, and contains no occurrence of 'KEV' or 'Known Exploited'; it supports only the 2026-06-18 fix. The KEV catalogue is not in this entry's sources[]. Same claim also in the summary. Add the KEV feed as a corroborating source and split the citation, or drop the catalogue clause."
- code: F2
  category: claim-not-supported
  section: weekly-vuln-rollup
  item: "weekly-w34-vuln-status-rollup"
  url_or_quote: "the same component is recorded Affected with no erratum in the JBoss Enterprise Application Platform Expansion Pack, so part of the estate has nothing to apply ([Red Hat Product Security, 2026-08-18](https://access.redhat.com/security/cve/CVE-2026-18963))"
  summary: "The cited Red Hat record states the opposite. Its product-state table (in the run's own pages/redhat-18963.txt and on the live page) has eleven Fixed rows and exactly two Not-affected rows: 'Red Hat JBoss Enterprise Application Platform Expansion Pack' with state 'Not affected' / justification 'Component not Present', and Red Hat Single Sign-On 7. No product is Affected and no affected product lacks an erratum. Correct the title ('an identity provider with an unfixed product'), the summary ('one affected Red Hat product has no erratum at all'), the Critical bullet, the 'No fix exists' bullet and the Defender takeaway ('one product left unfixed')."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w34-three-ways-to-take-the-agent-off-the-board"
  url_or_quote: "Talos notes that a busy server going quiet for process and image-load events while it demonstrably stays up and serving traffic is itself the signal."
  summary: "The Talos SPECTRE post makes no such observation — the strings telemetry, recommend, gap, sudden, absence, silence and quiet do not occur on it; its only guidance section is ClamAV/Snort coverage. Talos states only the effect ('rendered completely blind to new process creations, thread creations, and image load events'). The observation is this pipeline's own (operational entry spectre-uat-10147-byovd-edr-callback-unlink, Triage line). Drop 'Talos notes that' and present it as the entry's inference."
- code: F4
  category: claim-not-supported
  section: weekly-vuln-rollup
  item: "weekly-w34-vuln-status-rollup"
  url_or_quote: "GeoServer 3.0.1, 2.28.5 and 2.27.6 shipped on 2026-08-14 and Switzerland's NCSC appended the fixed versions to its advisory on 2026-08-17 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html))"
  summary: "The GeoServer 3.0.1 release announcement mentions no NCSC, no Switzerland and no 2026-08-17 advisory update; 2.28.5 and 2.27.6 appear only as undated sidebar links. One trailing citation carries a Swiss-authority fact from an uncited source. Cite the NCSC-CH advisory for its own clause or drop it. Two further uncited factual clauses in the same entry: the BIT / canton Graubünden SharePoint sentence, and 'Switzerland's NCSC put both in front of its constituency this week' on the WordPress bullet."
- code: F5
  category: claim-not-supported
  section: weekly-multi-day
  item: "weekly-w34-exploited-is-now-a-per-authority-opinion"
  url_or_quote: "CISA added CVE-2026-33824, a pre-authentication double free in the Windows IKE and AuthIP IPsec Keying Modules service reachable on UDP 500 and 4500, to its catalogue on 2026-08-18 ([CISA KEV catalog, 2026-08-18](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))"
  summary: "The KEV record carries only 'Microsoft Internet Key Exchange (IKE) Service Extensions contains a double free vulnerability that could enable remote code execution' — no ports, no pre-authentication, no AuthIP. Same shape on the next sentence: KEV says CVE-2026-55040 is a 'weak authentication vulnerability which allows an unauthorized attacker to bypass a security feature over a network', not 'allowing impersonation'. The catalogue dates are exactly right; only the mechanism detail is mis-attached, and the entry's own sourcing_note promises each claim is cited to the record that states it."
- code: F6
  category: hallucinated-fact
  section: weekly-incidents-recap
  item: "weekly-w34-two-charge-sheets-named-switzerland"
  url_or_quote: "among ten companies in seven countries"
  summary: "No cited source carries a country count: cash.ch and 20 Minuten contain no occurrence of sieben / Laender / Staaten, and 20 Minuten gives only 'zehn Firmen ... vier davon Schweizer Firmen'. The body correctly omits it, so the summary overstates the body's sourcing. The fact is true and comes from Netzwoche ('zehn Unternehmen in der Schweiz, Frankreich, Norwegen, Schottland, Kanada, den Niederlanden und den USA'), a corroborating source on the referenced operational entry but not on this one. Add Netzwoche as a corroborating record or drop 'in seven countries'. Also fix the sourcing_note clause 'the two outlets give different totals for economic damage' — the two outlets cited here do not; the 100m/130m divergence is 20 Minuten vs Netzwoche."
- code: F7
  category: single-source-flag-missing
  section: weekly-research
  item: "weekly-w34-ai-bought-throughput-not-capability"
  url_or_quote: "https://www.bleepingcomputer.com/news/security/us-warns-of-ai-powered-attacks-on-siemens-plcs-in-critical-infrastructure/"
  summary: "BleepingComputer is the load-bearing inline citation for the whole joint-advisory paragraph but is absent from sources[] — the only such mismatch in the run, and PD-2 requires sources[] and inline links to agree. The ic3.gov PDF listed as primary was not read (no pages/ic3 artefact; the PDF defeats WebFetch), so the sourcing_note's 'Four independent first-hand publishers ... each reporting its own telemetry or its own recovered artefacts' overstates. Content itself verified correct against BleepingComputer. Add BleepingComputer as a corroborating record and add a clause to the sourcing_note naming the PDF as unread and BleepingComputer as the relaying source, matching the MSRC/EUVD disclosures elsewhere in the run."
- code: F8
  category: editorial-advisory
  section: weekly-multi-day
  item: "weekly-w34-exploited-is-now-a-per-authority-opinion + weekly-w34-vuln-status-rollup"
  url_or_quote: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
  summary: "The same feed URL is cited with four different inline dates (2026-08-17/18/20/21) and two different sources[] dates (08-18 and 08-20). Each is a per-CVE dateAdded, not the artefact date; the fetched file is catalogVersion 2026.08.21, dateReleased 2026-08-21T17:46:43Z. All dates reconcile against kev.txt so this is not a truth defect, but rendered as '[Publisher, date]' a reader reads a publication date. Consider pinning the citation date to the catalogue version and leaving dateAdded in the prose."
- code: F9
  category: editorial-advisory
  section: weekly-looking-ahead
  item: "weekly-w34-looking-ahead"
  url_or_quote: "publisher: \"MISP Project advisory (via OSV.dev)\" — https://osv.dev/vulnerability/CVE-2026-77710"
  summary: "The OSV record states Source https://cve.org/CVERecord?id=CVE-2026-77710 and Import Source cve-osv-conversion; it is a CVE record mirrored into OSV, not a MISP-published advisory. Relabel the publisher. Secondary: the clause 'The three flaws disclosed on 21 August ... have no tagged release' is cited to a single-CVE page that does not mention CVE-2026-77755 or CVE-2026-77761. Every fact drawn from the page (last_affected 2026.7.8, two fix commits, published 2026-08-21) is correct."
```
