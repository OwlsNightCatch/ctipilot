**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-07T05:23:35Z · ended_at=2026-09-07T05:33:06Z · duration_seconds=571

## Verification report — 2026-09-07T0411Z-intel (iteration 4)

Walked all seven prior-iteration (iteration 3) findings against source before the cold pass; all seven remediations are correctly applied and verified against the fetched sources (Huntress blog `9/6/26` and `9/5/26` updates match the "Threat Response Unit" removal and the HF2 rewording; the Recorded Future page confirms the figures added to paragraphs 2-3; Kaspersky Securelist confirms the SharkLoader/"Perfect DLL Hijacking" clause; the referenced SDIS entry confirms the ChimeraZ five-of-seven-August / three-handle-July wording exactly; the new heise "Steuerungseinheit" article confirms the 08-14-isolation vs 08-17-disclosure timeline it cites; the ChimeraZ title now reads "customer account"). Two of the seven remediations, however, left residuals: the Berlin F9 fix (iter3 #5) reconciled the timeline in a new paragraph without updating the pre-existing contradictory text it was reconciling (F4 #1 below), and the Recorded Future F5 fix (iter3 #2) added citations to paragraphs 2-3 but missed a still-uncited sentence in paragraph 1 (F5 #3 below). Full independent cold pass follows across all five files (four new entries, one updated entry, the run record).

### Citation does not support the claim

#1. `2026-09-07/cve-2026-86206-86207-86218-n-able-n-central-third-chain` — "CVE-2026-86206, an access-control gap in N-central's internal API filter granting unauthorized access to internal-only APIs, and CVE-2026-86207 (CVSS 7.7), an authentication bypass by primary weakness reaching the same internal APIs" is cited only to `[N-able Status, 2026-09-05]`. Fetched that page directly: it says only "high-CVSS-rated vulnerabilities that could allow an unauthorized party to bypass authentication controls and gain full access to the N-central platform" — no mention of "internal API filter" or "internal-only APIs." The specific technical description (and the literal phrase "authentication bypass by primary weakness," which is the CWE-305 title) comes from OffSeq Threat Radar's CNA records (`CVE-2026-86206`: "A vulnerability in the N-central internal API access control filter allows unauthorised access to internal APIs"; `CVE-2026-86207`: "An authentication bypass in N-central < 2026.3 HF 3 leads to authentication bypass in internal only APIs") — both listed in `sources[]` as corroborating but never inline-cited in the body. Per check 2(d), the terminating citation vouches for the whole clause; the fact it doesn't carry is F3. Fix: add the two OffSeq URLs as inline citations on this sentence.

#2. `2026-09-07/chimeraz-aveyron-onrecrute-breach` — title, summary and body repeatedly hedge the compromised-account type as "a partner or customer account" / "no-MFA partner account" / "a suspected third-party or partner-account foothold," but the sole cited source for the access mechanism, FrenchBreaches, states only "compte client" (customer/client account) — "partenaire"/partner never appears in that article in connection with the compromised account (fetched directly: "Selon nos informations, la fuite aurait été rendue possible par la compromission d'un compte client dépourvu de double authentification..."; Cyberattaque.org's one use of "partenaires" describes employers who consume the CV database as a platform feature, unrelated to how ChimeraZ got in). The citation at the end of the sentence (`[FrenchBreaches, 2026-09-06]`) is present but does not carry the "partner" half of the claim — an adjacency violation (check 2d). Iteration 3 only partially fixed this (the title's headline noun was corrected to "customer account," but the "partner or customer" hedge survives in the summary and body twice). Fix: drop "partner" throughout; FrenchBreaches supports only "customer account."

#3 (low confidence). `2026-09-07/recordedfuture-h1-2026-tool-stack-reuse` — "SharkLoader itself was previously profiled by Kaspersky's GReAT as deploying Cobalt Strike via 'Perfect DLL Hijacking' against government targets." Fetched Securelist directly: the article explicitly states "the observed victimology suggests a campaign with broad geographic reach and a diverse target set rather than a narrow focus on a specific industry or region," naming a diplomatic entity (Indonesia), government orgs (Taiwan), software-development companies, and entities across Hong Kong/Lebanon/Syria/Colombia/North Macedonia/Nepal/Serbia. "Against government targets" narrows/mischaracterizes Kaspersky's own explicit disclaimer of a narrow target focus. Note: this phrasing is inherited verbatim from the pre-existing `entities/registry.yaml` summary for `campaign:strikeshark-sharkloader` ("...against government targets"), not invented fresh by this run — but it now ships in this run's new entry body too, so it reaches readers regardless of origin.

#4. `2026-09-07/recordedfuture-h1-2026-tool-stack-reuse` — `sources[]` cites Kaspersky Securelist with `date: "2026-06-27"`. Fetched the article's raw HTML: its own JSON-LD `datePublished` is `2026-06-24T10:00:03+00:00` — a 3-day drift, which per check 2(e) is F3 (not a timezone artifact). "2026-06-27" matches the pipeline's own prior-entry directory date (`2026-06-27/kaspersky-great-strikeshark-loader-deploys-cobalt-strike-via`), not the article's publish date — exactly the "pipeline processing date substituted for source date" pattern the check warns against. Fix: correct the `date` field to `2026-06-24`.

### Unsupported / hallucinated facts

#1. `2026-08-30/berlin-landesnetz-rhysida-extortion-phishing-vector` — the main analysis (unchanged since 2026-08-30) still states "the attack became public knowledge on 2026-08-14 (translated from German) ([Berliner Zeitung, 2026-08-28])." This run's own new `## Update — 2026-09-07T04:47:00Z` section — added specifically to reconcile iteration-3's F9 finding — states the opposite: "that date is when the two affected Senate departments were isolated from the Landesnetz as a containment step, while the Senate chancellery's public press statement disclosing the 'ICT incident' followed three days later, on 2026-08-17 ([heise online, 2026-09-06]) — consistent with Security Affairs' dating of Berlin's first disclosure to 2026-08-17." Confirmed directly against the fetched heise timeline: "14. August 2026: Die beiden Senatsverwaltungen werden vom Landesnetz isoliert." / "17. August 2026: Die Senatskanzlei informiert per Pressemitteilung über einen 'IKT-Vorfall im Landesnetz Berlin'." — the new paragraph is itself accurate, but the pre-existing `sourcing_note` was not updated and still reads "Berliner Zeitung, Der Tagesspiegel and rbb24 all independently state the compromise became public and the affected departments were disconnected on 2026-08-14 ... This entry follows the three-source consensus date," directly contradicting the new section's own conclusion that 08-14 was containment-only, not "became public." Per check 4c(e), this is the exact shape the checklist calls out: an update that changes the state while the entry's own standing text still asserts the old, now-contradicted claim — the remediation introduced this rather than resolving it. Fix: reword the main-analysis opening sentence (drop "became public knowledge," replace with e.g. "was internally identified and contained") and rewrite the `sourcing_note` to state the reconciliation instead of restating the superseded three-vs-one framing.

### Claims missing inline citation

#1. `2026-09-07/rapid7-ted-backdoor-curlrat-dprk-haproxy` — "Because it is compiled into the load balancer's own binary rather than exploiting a flaw in it, the technique defeats vulnerability scanning and version-string checks outright: a recompiled binary still reports the same version." carries no citation. The Hacker News (in `sources[]`) directly states this: "a recompiled HAProxy reports the same version string as a clean build," and separately "It is not a HAProxy vulnerability, and installing it requires code execution on the host and the ability to replace the running binary" (the latter already used verbatim as an `evidence[]` quote elsewhere in the entry, but not cited at this clause). Fix: add the Hacker News citation to this sentence.

#2. `2026-09-07/cve-2026-86206-86207-86218-n-able-n-central-third-chain` — "CVE-2026-86218, a pre-authentication remote-code-execution flaw (CWE-96, static code injection) rated CVSS 10.0 — the maximum possible score." carries no citation at all (this sentence ends before the next sentence's Huntress citation, which supports a different, later fact). "CWE-96, static code injection" appears nowhere in the fetched Huntress blog; it is the literal title fragment of the OffSeq CNA record (`CWE-96 Improper neutralization of directives in statically saved code ('static code injection')`), never cited inline anywhere in the body. Fix: cite the OffSeq CVE-2026-86218 record at this clause.

#3. `2026-09-07/recordedfuture-h1-2026-tool-stack-reuse` — the iteration-3 remediation added citations "throughout paragraphs 2-3" but missed paragraph 1's second sentence: "Of those, 176 (82%) were network-accessible and 146 (68%) could be exploited without prior authentication; 142 of those 146 combined both properties, and 60 of 82 remote-code-execution CVEs combined network reachability, no authentication requirement and code execution in a single package." carries zero inline citation. Confirmed accurate against the fetched Recorded Future page ("176 (82%) of the 215 CVEs were network-accessible, and 146 (68%) could be exploited without prior authentication. More significantly, 142 of those 146 were also network-accessible... Sixty of the 82 RCE vulnerabilities were also network-accessible and could be exploited without prior authentication.") — the figures are correct, the citation is simply absent. Fix: add `([Recorded Future, 2026-09-03](...))` to this sentence.

### Quantifier without source

#1 (low confidence). `2026-09-07/chimeraz-aveyron-onrecrute-breach` title — "exposing 20,000+ job candidates' CVs" reads as 20,000+ CVs exposed. Both cited sources state 20,316 is the count of exposed *people/records* (23,381 records total, predominantly basic profile/application data), while only ~1,499 PDF documents are actual CVs (FrenchBreaches: "1 499 documents PDF"; Cyberattaque.org: "1 499 documents PDF pour environ 451 Mo"). The title conflates the two counts. Fix: reword to e.g. "exposing 20,000+ job candidates' personal data, including ~1,500 CVs."

### Verdict

`NEEDS_FIXES (truth: 6, editorial: 3, advisory: 0)`

Six residual truth defects (F3 x4, F4 x1, F14 x1 — F14 counts as truth per the category split) and three editorial defects (F5 x3) survive into iteration 4, including one (F4 #1) that the iteration-3 remediation itself introduced by adding a correct new paragraph without correcting the pre-existing contradictory text it was reconciling, and one (F5 #3) where the iteration-3 remediation was simply incomplete. None of the four new entries or the run record show fabricated URLs, broken links, wrong-actor attribution, or wholesale hallucination — every fetched source substantively supports its entry's core narrative, all evidence[] quotes checked are verbatim substrings of the fetched pages, all techniques[] ids map to behavior the sources describe (including a correct proactive translation of Rapid7's own pre-v19 ATT&CK ids T1070.002/T1562.006 to the pinned dataset's current T1685.006/T1685 — not a defect, a correct update), and all CVSS/CVE/CWE facts checked against OffSeq's CNA records and N-able's own status pages are accurate. The remaining defects are the adjacency/citation-placement class check 2(d)/4c(e) exist to catch; the Berlin internal contradiction (F4 #1) is reader-visible in the published entry and should be fixed before publish. Coverage shape, priority calibration (critical/high/notable all cleared their bars), classification blocks (all five files carry a valid Admiralty or single-source-consistent rating), `org_triage`/`watchlist_hit` (null/false throughout, correct for this deployment), action-item discipline (N-able's two actions are concrete and finding-specific; all other actions[] correctly empty), and style discipline (no IOCs, no vanity metrics, no workflow-internal language in any reader-facing text) all checked clean across all five files. No additional missed-angle could be evidenced beyond what the run record's own coverage-backlog section already documents.

### Findings summary (machine-readable)

- code: F3
  category: claim-not-supported
  section: new-entry
  item: "2026-09-07/cve-2026-86206-86207-86218-n-able-n-central-third-chain"
  url_or_quote: "CVE-2026-86206, an access-control gap in N-central's internal API filter ... CVE-2026-86207 ... authentication bypass by primary weakness ([N-able Status, 2026-09-05])"
  summary: "cited N-able Status page says only 'high-CVSS-rated vulnerabilities that could allow an unauthorized party to bypass authentication controls'; the specific technical description comes from OffSeq's CNA records (listed in sources[] but not cited at this clause)."
- code: F3
  category: claim-not-supported
  section: new-entry
  item: "2026-09-07/chimeraz-aveyron-onrecrute-breach"
  url_or_quote: "a compromised partner or customer account lacking multi-factor authentication ([FrenchBreaches, 2026-09-06])"
  summary: "FrenchBreaches' own text says only 'compte client' (customer account); 'partner' is unsupported by either cited source and survives in the summary/body twice despite the title fix."
- code: F3
  category: claim-not-supported
  section: new-entry
  item: "2026-09-07/recordedfuture-h1-2026-tool-stack-reuse"
  url_or_quote: "SharkLoader itself was previously profiled by Kaspersky's GReAT as deploying Cobalt Strike via \"Perfect DLL Hijacking\" against government targets"
  summary: "(low confidence) Kaspersky's own article explicitly disclaims narrow/government-only targeting ('a campaign with broad geographic reach and a diverse target set rather than a narrow focus on a specific industry or region'), naming a diplomatic entity, software companies and multiple non-government sectors; phrasing inherited from the registry's existing campaign summary but repeated in this run's new entry."
- code: F3
  category: claim-not-supported
  section: new-entry
  item: "2026-09-07/recordedfuture-h1-2026-tool-stack-reuse"
  url_or_quote: "sources[]: Kaspersky Securelist, date: \"2026-06-27\""
  summary: "article's own JSON-LD datePublished is 2026-06-24T10:00:03+00:00, a 3-day drift; 2026-06-27 is the pipeline's own prior-entry directory date, not the source's publication date (check 2e)."
- code: F4
  category: hallucinated-fact
  section: updated-entry
  item: "2026-08-30/berlin-landesnetz-rhysida-extortion-phishing-vector"
  url_or_quote: "the attack became public knowledge on 2026-08-14 [main analysis, unchanged] vs. \"containment step ... public press statement ... followed three days later, on 2026-08-17\" [new 2026-09-07 update section]"
  summary: "main analysis and pre-existing sourcing_note still assert 2026-08-14 as the public-disclosure date; this run's own new update section reconciles the iteration-3 F9 finding by stating 08-14 was containment-only and 08-17 was the actual public disclosure, but neither the main analysis sentence nor the sourcing_note was updated to match — an unresolved internal contradiction the remediation itself introduced."
- code: F5
  category: missing-citation
  section: new-entry
  item: "2026-09-07/rapid7-ted-backdoor-curlrat-dprk-haproxy"
  url_or_quote: "the technique defeats vulnerability scanning and version-string checks outright: a recompiled binary still reports the same version."
  summary: "no citation; The Hacker News (in sources[]) states 'a recompiled HAProxy reports the same version string as a clean build' but is not cited here."
- code: F5
  category: missing-citation
  section: new-entry
  item: "2026-09-07/cve-2026-86206-86207-86218-n-able-n-central-third-chain"
  url_or_quote: "CVE-2026-86218, a pre-authentication remote-code-execution flaw (CWE-96, static code injection) rated CVSS 10.0 — the maximum possible score."
  summary: "no citation on this sentence; 'CWE-96, static code injection' is the OffSeq CNA record's title fragment, never cited inline anywhere in the body."
- code: F5
  category: missing-citation
  section: new-entry
  item: "2026-09-07/recordedfuture-h1-2026-tool-stack-reuse"
  url_or_quote: "Of those, 176 (82%) were network-accessible and 146 (68%) could be exploited without prior authentication; 142 of those 146 combined both properties, and 60 of 82 remote-code-execution CVEs combined network reachability, no authentication requirement and code execution in a single package."
  summary: "iteration-3 remediation added citations to paragraphs 2-3 but missed this sentence in paragraph 1; figures confirmed accurate against the Recorded Future page but the sentence itself is uncited."
- code: F14
  category: quantifier-without-source
  section: new-entry
  item: "2026-09-07/chimeraz-aveyron-onrecrute-breach"
  url_or_quote: "exposing 20,000+ job candidates' CVs [title]"
  summary: "(low confidence) 20,316 is the count of exposed people/records, not CVs; only ~1,499 PDF documents are actual CVs per both cited sources."
