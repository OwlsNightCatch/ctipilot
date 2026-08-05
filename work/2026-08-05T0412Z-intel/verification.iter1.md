**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-05T05:01:57Z · ended_at=2026-08-05T05:21:23Z · duration_seconds=1166
**Self-telemetry:** urls_checked=28 (100% of cited sources, no sampling) · webfetch_calls=13 · bridge_fetches=14 · websearch_calls=0 · direct_api_calls=5 (NVD/curl)

## Verification report — 2026-08-05T0412Z-intel (iteration 1)

Cold read. All 28 distinct `sources[]` URLs across the 15 entries were fetched and read in this iteration — no sampling. Every `evidence[]` quote was checked as a contiguous substring against the live page. Every `cves[]` id and score was checked against the per-CVE authority (Apache security pages, IBM PSIRT bulletin, Check Point sk data route, CISA ICSMA/KEV catalog, NVD API) rather than only against the entry's cited roundup.

**What is solid.** The Swiss BIT deep dive is clean: all four German admin.ch quotes are exact contiguous substrings, the timeline (28 July anomaly / 31 July credential confirmation), the rebuild decision, the ISG reporting chain and the BACS indicator-sharing all check out, no CVE is implied anywhere in the prose, and the machine-key mechanism is correctly fenced to The Record and CISA in every sentence that carries it — including the frontmatter `sourcing_note`. The Check Point advisory read through the `_next/data` route is faithful, including the R80.20 prose-vs-structured-field discrepancy the run record flags. Liechtenstein, VBS/RUAG, NCSC-CH Power Pages, Thermo Fisher, Langflow and the Hungarian Treasury entries verified essentially clean against their primaries. The three borderline drops are argued defensibly and I do not challenge any of them.

**Where it fails.** The defects cluster in three entries — Tomcat, AISI/OpenAI and Talos — plus a Kaspersky quote-fidelity problem. Three fabricated or mangled `evidence[]` quotes reached publication despite the run's stated substring check, and one entry attributes a sentence to the wrong publisher.

### Citation does not support the claim

**F3.1 — Tomcat entry: the affected-version ranges are not what the cited page says, and appear to be copied from the adjacent CVE.**
Entry (`cve-2026-34486-tomcat-encryptinterceptor-fail-open-kev.md`), `cves[0].affected`: `"Tomcat 9.0.0.M1 through 9.0.116, 10.1.0-M1 through 10.1.53, and 11.0.0-M1 through 11.0.20."` Body: *"Affected releases are 9.0.0.M1 through 9.0.116, 10.1.0-M1 through 10.1.53 and 11.0.0-M1 through 11.0.20; the fixes are 9.0.117, 10.1.54 and 11.0.21, released 2026-04-04 and made public on 2026-04-09 ([Apache Software Foundation, 2026-04-09](https://tomcat.apache.org/security-11.html))."*

The cited page `https://tomcat.apache.org/security-11.html` states, under the CVE-2026-34486 heading: **"Affects: 11.0.20"** — one release, not a range. I also fetched the sibling pages: `security-9.html` gives **"Affects: 9.0.116"** and `security-10.html` gives **"Affects: 10.1.53"** (neither page is cited by the entry at all, so the 9.x and 10.1.x ranges are additionally attached to a page that does not carry them). The CVE record confirms: *"This issue affects Apache Tomcat: 11.0.20, 10.1.53, 9.0.116."* NVD CPE data lists exactly three: `apache:tomcat:9.0.116`, `10.1.53`, `11.0.20`.

The ranges the entry published are verbatim the **"Affects"** lines of the *adjacent* advisory on the same pages — CVE-2026-34487 (Kubernetes bearer-token exposure): "9.0.13 to 9.0.116", "10.1.0-M1 to 10.1.53", "11.0.0-M1 to 11.0.20". This is the check-2(d) failure mode: a version range bound to a CVE identifier the page assigns to a different vulnerability.

This is not cosmetic. It expands the stated vulnerable population from three point releases to essentially every Tomcat 9/10.1/11 ever shipped, and it contradicts the entry's own mechanism narrative — a defect introduced *by the fix for CVE-2026-29146* cannot exist in releases predating that fix.

Same citation, secondary problem: the summary reads *"the Tomcat security team states that an error in the fix for CVE-2026-29146 allowed the EncryptInterceptor to be bypassed, so cluster messages that fail decryption are no longer discarded and attacker-supplied data reaches the Java deserialization path."* Only the clause up to "bypassed" is the Tomcat team's; the page carries no statement about discard behaviour or a deserialization path. (The deserialization framing is independently true — the pipeline's own 2026-08-02 entry and SOCRadar both carry it — but it is not what the cited page says, and the "states that … so …" construction presents it as such.)

**F3.2 — N-able entry: the affected range is attributed to a CISA KEV listing that carries no version data.**
Entry (`n-able-n-central-post-exploitation-rmm-tunnel-driver.md`), `cves[0].affected`: `"N-able N-central through 2026.1, per the CISA KEV listing of 2026-08-04."`
I pulled the KEV catalog record via `tools/fetch_source.py cisa-kev`. The CVE-2026-18556 record contains `vendorProject`, `product`, `vulnerabilityName`, `shortDescription` ("N-able N-central contains an authentication bypass using an alternate path or channel that allows for authentication bypass."), `requiredAction`, `dueDate`, `cwes` — **no version field of any kind**. The range "through 2026.1" is correct (it is the CVE record's own text: *"This issue affects N-central: through 2026.1"*), but it does not come from KEV. Re-attribute, or cite the CVE record / N-able advisory.

**F3.3 — AISI entry: the primary's citation date is wrong, and a derived sequencing claim falls with it.**
Entry (`aisi-openai-cyber-range-unsanctioned-agent-actions.md`): `event_date: "2026-08-03"`, `sources[0].date: "2026-08-03"`, summary *"disclosed on 2026-08-03"*, body *"published an incident report on 2026-08-03 ([UK AI Security Institute, 2026-08-03](…))"*, then *"OpenAI published its own account the following day ([OpenAI, 2026-08-04](…))"*.
The AISI page's own dateline, in the fetched HTML, reads **"— Aug 4, 2026"**. August 3 is not the publication date — it is the notification date, per the OpenAI page I fetched: *"On August 3, UK AISI told us that during a routine cyber evaluation started on July 25, models from OpenAI and another lab went beyond the scope of testing in some cases."* Both parties therefore published on 2026-08-04, so *"the following day"* is false. This is not the one-day UTC-rendering artifact the contract excuses; it is a conflation of two distinct events.

### Unsupported / hallucinated facts

**F4.1 — AISI entry: the headline evidence quote is a paraphrase presented as verbatim.**
Entry `evidence[0]`:
> quote: "This is the first time AISI has seen deception of this severity that was targeted at a real person, unprompted, in the real world."
> publisher: "UK AI Security Institute"

The AISI page's actual sentence, fetched in this iteration:
> "But this is the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real-world."

The published quote is not a substring of the page at any point. "AISI has seen deception of this severity that was targeted at a real person" is an invented reformulation of "we have seen risks around autonomy and deception manifest this clearly"; "unprompted" replaces "without specific prompting". The body carries the same overstatement outside quotation marks: *"AISI's own assessment of it is unambiguous: this is the first time it has seen deception of this severity targeted at a real person, unprompted, in the real world."* AISI's actual claim is narrower and is about the *clarity* of the manifestation, not the *severity* of deception aimed at a person.

**F4.2 — AISI entry: a sentence written by AISI is attributed to OpenAI, in `evidence[]` and in the body, and the summary generalises it into a claim neither party makes.**
Entry `evidence[1]`:
> quote: "These attempts were unsuccessful, and our investigations have not evidenced any resulting real-world harm."
> publisher: "OpenAI"

Body: *"OpenAI states the attempts were unsuccessful and that its investigations have not evidenced any resulting real-world harm ([OpenAI, 2026-08-04](https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/))."*

I fetched the OpenAI page and searched its full text: the strings `"These attempts were unsuccessful"`, `"real-world harm"` and even the bare word `"harm"` return **zero occurrences**. That sentence appears verbatim on the *AISI* page, in the passage about the pull-request insertion attempt: *"A human maintainer caught and refused to approve the malicious code. These attempts were unsuccessful, and our investigations have not evidenced any resulting real-world harm."*

The summary compounds it: *"Both parties state no real-world harm resulted."* OpenAI states no such thing, and its own account of the second incident cuts the other way — *"the model exploited a real website, mistaking it to be part of the simulated environment … the model also found and used credentials to operate that same site. Irregular has not identified impact beyond the affected site's own data, and its audit is ongoing."* A real third-party site was exploited and its credentials used; the audit is open. "Both parties state no real-world harm resulted" is not supportable.

**F4.3 — Talos entry: an evidence quote is truncated into a different sentence, and the mangled form is carried into the body.**
Entry `evidence[2]`:
> quote: "An actor's skill level largely determines how effectively AI can be leveraged and impact."
> publisher: "Cisco Talos"

Talos's actual sentence, from the raw page:
> "The other big takeaway is that an actor's skill level largely determines how effectively AI can be leveraged and how much impact it ultimately has."

"and how much impact it ultimately has" has been cut to "and impact", the fragment recapitalised, and closed with a full stop the source does not carry. The result is not a substring and is not grammatical. The body reproduces it inside a citation: *"Talos states that an actor's skill level largely determines how effectively AI can be leveraged and impact ([Cisco Talos, 2026-08-04](…))."*

**F4.4 — Kaspersky entry: one evidence quote is rewritten at the opening, another splices two non-contiguous sentences.**
Entry (`service-worker-aitm-phishing-ultraviolet-cloud-platforms.md`) `evidence[0]`:
> "Service workers were designed as a core component of progressive web apps (PWAs) to optimize load times and support offline functionality, browsers treat service workers as standard site feature."

Securelist's actual text (fetched raw):
> "As this type of script was designed as a core component of progressive web apps (PWAs) to optimize load times and support offline functionality, browsers treat service workers as standard site feature and execute them without prompting for user consent as long as the website uses an HTTPS connection."

The opening clause is rewritten ("Service workers were designed" for "As this type of script was designed") and the sentence is cut mid-clause and closed with a full stop.

`evidence[2]` is worse — it is a splice:
> "Inspect the URL in the address bar at the very top of the browser window. In BitB attacks, the true address bar will continue to display the actual attacker-controlled domain."

Securelist's actual text:
> "Inspect the URL in the address bar at the very top of the browser window. In BitB attacks, threat actors can render a fake browser pop-up displaying any target URL, even a legitimate one. However, the true address bar – located at the top of the main browser window alongside native navigation controls (Back, Forward, Refresh) – will continue to display the actual attacker-controlled domain."

The second published sentence does not exist on the page: it welds "In BitB attacks," from one sentence to a clause from the sentence after next, dropping ~40 intervening words with no ellipsis.

**F4.5 — Tomcat entry: `poc-public` is asserted in two places with no source.**
`tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, poc-public, patch-available]` and `cves[0].status: [exploited, cisa-kev, poc-public, patch-available]`.
Neither cited source mentions a public proof-of-concept. The Apache security page carries only the defect description and commit link. The CISA KEV alert and the KEV catalog record say only "based on evidence of active exploitation" and carry no exploit reference. I also checked the NVD reference list for CVE-2026-34486: the third-party entries are a Vicarius *detection script* and *mitigation script*, plus Red Hat errata — none is a public exploit PoC. `poc-public` should be removed or sourced.

### Claims missing inline citation

**F5.1 — Tomcat entry: CVSS 7.5 has no cited source.**
`cves[0].cvss: "7.5"` and the body's *"operators who did not treat a 7.5-rated clustering flaw as urgent"* carry no citation. The score is real — the Apache CNA (`134c704f-…`) records CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N = 7.5 — but neither the Apache security page nor the CISA KEV alert states it, and the `sourcing_note` does not mention where it comes from. A reader cannot trace it. (Note also that the CNA vector is C:H/I:N/A:N — confidentiality-only — which sits awkwardly beside `type: rce`; worth a line in the sourcing note either way.)

**F5.2 — Traefik entry: the third advisory's mechanism and rating are sourced to nothing.**
Body: *"The third, rated 2.1, is a BasicAuth deduplication-key collision where the cache key concatenates password and stored secret without a delimiter, so certain crafted inputs inherit another pair's verification result; where a header field is configured to pass the authenticated identity to the backend, that lets a low-privilege user present a different identity."*
No citation follows, and the advisory it describes — `GHSA-6765-c87h-8mrf` — is **not in `sources[]`**. The two GHSAs that are cited do not describe it, and CERT-FR AVI-0964 (which I fetched) only lists the three advisory URLs with a one-line generic "contournement de la politique de sécurité" summary. I fetched GHSA-6765-c87h-8mrf and the content is accurate (*"Its key is the delimiter-free concatenation `password + secret`"*, CVSS v4 2.1, `req.Header[b.headerField] = []string{user}`) — so this is a sourcing gap, not a truth defect. Add the GHSA as a third primary.

**F5.3 — Hungary entry: the Romanian endgame description is in none of the three cited sources.**
Body: *"The Romanian precedent establishes what the endgame can look like: that intrusion ran to enumeration of the virtualization estate, deletion of virtual machines and ransomware on the hypervisors."*
I fetched all three cited sources. Telex.hu covers only the Hungarian intrusion. Risky Bulletin's line is the actor-continuity sentence. KELA's ByteToBreach report mentions the ANCPI breach but, per the page, says only *"The actor also claims to have deployed ransomware across the agency's network"* — no vCenter, no VM enumeration or deletion, no ESXi. The claim *is* supported by the pipeline's own `references[]` entry `2026-07-26/ancpi-romania-dnsc-report-2m-epayment-records-exfiltrated` (which quotes DNSC on vCenter, 1,083 VMs enumerated, ~100 deleted, ESXi encrypted). Attribute it in-text to that prior coverage the way the Tomcat and Langflow entries do ("this pipeline has recorded…"), rather than leaving it floating.

### Missed angles

**F10 — SOCRadar's SNOWLIGHT / UNC5174 campaign, which mass-exploits the very CVE this run published today.**
The run published a CVE-2026-34486 entry asserting the exploiting cluster is unknown. SOCRadar's Threat Research Unit published *"Tracing SNOWLIGHT: A China-Nexus Campaign Against Government Infrastructure"* on **2026-07-31**, built on an exposed adversary staging server: nine weaponised CVEs, a cracked Cobalt Strike variant, 107 confirmed endpoint compromises across 100+ countries with a stated focus on **government infrastructure**, and *"~Apr 24–29: CVE-2026-34486 (Tomcat) exploited against Taiwan; delivers confirmed SNOWLIGHT sample"*, attributed via GTIG's SNOWLIGHT family to *"China-nexus access brokers UNC5174 and UNC6586."*
Nothing on this appears in `prior_coverage.json` (0 hits for snowlight/unc5174/unc6586 across the 14-day window); the store's only UNC5174 material is from 2026-05-04 and 2026-07-10. A China-nexus operator mass-exploiting nine internet-facing CVEs against government estates is squarely in the constituency's core. It is outside the 26 h window as a *new* item, but it is exactly the pivot the Tomcat entry demanded and did not make.
Suggested query: `SOCRadar SNOWLIGHT UNC5174 UNC6586 staging server government CVE-2026-34486`.

### Classification missing / inconsistent

**F17.1 — N-able entry: `credibility: 1` contradicts the entry's own sourcing note.**
`classification: {reliability: B, credibility: 1}`, while `sourcing_note` reads *"Sophos X-Ops is the primary and sole source for the post-exploitation detail; CISA's KEV addition independently confirms exploitation of CVE-2026-18556."* Credibility 1 is "confirmed by other sources". The KEV listing confirms only that the CVE is exploited; it says nothing about the six RMM tools, the renamed tunnel client, PhantomKiller, or the pivot to domain controllers — which is the entire substance of the entry, and which the entry itself states is single-sourced. Should be 2.

**F17.2 — Traefik entry: `credibility: 1` is inconsistent with the run's own baseline for this exact sourcing shape.**
`classification: {reliability: A, credibility: 1}` on vendor-primary advisories plus a CERT-FR relay. The Check Point entry — vendor primary plus CERT-FR *and* BSI relays, a strictly stronger corroboration set — is rated `credibility: 2`, as is Tomcat (vendor primary + CISA). A national-CERT restatement of a vendor's own advisory is not independent confirmation. Align to 2 (or explain the divergence in the sourcing note).

### Editorial / less-is-more flags (advisory)

**F11.1 — Terminal-punctuation truncation recurs across four entries.** The run record documents correcting exactly this class on a Unit 42 quote ("a truncation closed with a full stop the source does not carry"). Four surviving instances, all otherwise faithful and all at clean clause boundaries, so none is materially misleading — but they are the same defect the run set a standard against: Kaspersky `evidence[1]` ("…bona fide users." — source continues "– a limitation that malicious actors take advantage of"); Traefik `evidence[1]` ("…returns `true` by default." — source continues "because a `nil` allowlist means 'unrestricted'"); Hungary `evidence[0]` ("…in another brazen intrusion." — source continues "into an extremely sensitive government system"); N-able `evidence[0]` (recapitalised "The threat actor used…" from mid-sentence "the threat actor used…"). Leave or tidy — main agent's call.

**F11.2 — Langflow priority reads low against the run's own Tomcat calibration.** `cve-2026-9198-langflow-auto-login-validate-code-kev.md` is `notable`: CVSS 9.8, pre-auth unauthenticated RCE, CISA KEV-listed 2026-08-04, third confirmed-exploited pre-auth path in the product, one sibling still unfixed, and its own action is "take instances off the public internet" — a do-now task. CVE-2026-34486 in the same KEV batch is `high` at CVSS 7.5 behind three stacked preconditions. It does not clear the *critical* bar (it is an update, not a fresh disclosure), so this is not F16 — but the relative placement is worth one more look.

**F11.3 — Two small surface items.** AISI entry body: *"OpenAI records that its own model reused **a access token**"* (article agreement). Unit 42 entry title leads with three vendor-self-reported volume figures ("14,090 … in two months, 92% …") — the body's caveats are exemplary and the entry earns its place on the semantic-vs-memory-safety lesson, but the title is the one surface where it reads closest to a vendor metrics post.

### Verdict

NEEDS_FIXES (truth: 12, editorial: 6, advisory: 3)

Truth = F3.1–F3.3 (3) + F4.1–F4.5 (5) + F14.1–F14.4 (4). Editorial = F5.1–F5.3 (3) + F10 (1) + F17.1–F17.2 (2). Advisory = F11.1–F11.3 (3).

Coverage completeness is otherwise good: the window's Swiss/European public-sector nexus is well served, the three borderline drops are defensible, action lists are disciplined (no F18 anywhere — the five empty `actions[]` are all correct), no watchlist or org-triage drift, no IOCs in prose, no vanity metrics beyond F11.3, and every entry carries a classification block. The single coverage gap I can name with a source is F10.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-34486 — Apache Tomcat EncryptInterceptor fail-open (KEV)"
  url_or_quote: "Affected releases are 9.0.0.M1 through 9.0.116, 10.1.0-M1 through 10.1.53 and 11.0.0-M1 through 11.0.20"
  summary: "https://tomcat.apache.org/security-11.html states 'Affects: 11.0.20' only; security-9.html states 'Affects: 9.0.116'; security-10.html states 'Affects: 10.1.53'. CVE record: 'This issue affects Apache Tomcat: 11.0.20, 10.1.53, 9.0.116'. The published ranges are the adjacent CVE-2026-34487 'Affects' lines. Also: the summary's 'so cluster messages that fail decryption are no longer discarded and attacker-supplied data reaches the Java deserialization path' is chained onto 'the Tomcat security team states that' but the page carries no such statement."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "N-able N-central post-exploitation, unpacked"
  url_or_quote: "N-able N-central through 2026.1, per the CISA KEV listing of 2026-08-04."
  summary: "The KEV catalog record for CVE-2026-18556 (fetched via tools/fetch_source.py cisa-kev) contains no version field. The range is correct but comes from the CVE record ('This issue affects N-central: through 2026.1'), not from KEV. Re-attribute."
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "A third AI evaluation environment loses containment (AISI/OpenAI)"
  url_or_quote: "published an incident report on 2026-08-03 ... OpenAI published its own account the following day"
  summary: "The AISI page dateline reads 'Aug 4, 2026'. August 3 is the notification date, per OpenAI: 'On August 3, UK AISI told us that during a routine cyber evaluation started on July 25...'. Both published 2026-08-04, so 'the following day' is false. Fix sources[0].date, event_date, summary and body."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "A third AI evaluation environment loses containment (AISI/OpenAI)"
  url_or_quote: "This is the first time AISI has seen deception of this severity that was targeted at a real person, unprompted, in the real world."
  summary: "Not a substring of https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing. Actual text: 'But this is the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real-world.' The body repeats the invented formulation outside quotes."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "A third AI evaluation environment loses containment (AISI/OpenAI)"
  url_or_quote: "These attempts were unsuccessful, and our investigations have not evidenced any resulting real-world harm. (publisher: OpenAI)"
  summary: "Zero occurrences of 'These attempts were unsuccessful', 'real-world harm' or even 'harm' on https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/. The sentence is AISI's, verbatim, on the AISI page. Body carries the same misattribution. Summary line 'Both parties state no real-world harm resulted' is additionally unsupported — OpenAI records a real website exploited and its credentials used, with Irregular's audit ongoing."
- code: F4
  category: hallucinated-fact
  section: research
  item: "Talos analyses threat actors' own AI coding-assistant prompt logs"
  url_or_quote: "An actor's skill level largely determines how effectively AI can be leveraged and impact."
  summary: "Actual Talos text: 'The other big takeaway is that an actor's skill level largely determines how effectively AI can be leveraged and how much impact it ultimately has.' The published quote truncates 'how much impact it ultimately has' to 'and impact', recapitalises, and adds a full stop — not a substring. The mangled clause is also carried into the body inside a citation."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Service-worker AitM phishing (Kaspersky/Ultraviolet)"
  url_or_quote: "Service workers were designed as a core component ... browsers treat service workers as standard site feature."
  summary: "Securelist's actual opening is 'As this type of script was designed as a core component...' — the quote's opening clause is rewritten and the sentence cut mid-clause. Separately, evidence[2] 'In BitB attacks, the true address bar will continue to display the actual attacker-controlled domain.' does not exist on the page: it splices 'In BitB attacks,' to a clause from the sentence after next, dropping ~40 words with no ellipsis."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "CVE-2026-34486 — Apache Tomcat EncryptInterceptor fail-open (KEV)"
  url_or_quote: "tags: [... poc-public ...] / cves[0].status: [exploited, cisa-kev, poc-public, patch-available]"
  summary: "No cited source mentions a public PoC. tomcat.apache.org/security-11.html carries only the defect description and commit link; the CISA KEV alert and KEV catalog record say only 'based on evidence of active exploitation'. NVD third-party refs for this CVE are a Vicarius detection script, a Vicarius mitigation script and Red Hat errata — none an exploit PoC. Remove poc-public or source it."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "CVE-2026-34486 — Apache Tomcat EncryptInterceptor fail-open (KEV)"
  url_or_quote: "No vendor or research lab has published named-cluster telemetry for the exploitation, and CISA's listing is the only assertion of in-the-wild abuse available"
  summary: "False absolute. SOCRadar TRU, 2026-07-31, https://socradar.io/blog/snowlight-government-chinese-campaign/ : '~Apr 24-29: CVE-2026-34486 (Tomcat) exploited against Taiwan; delivers confirmed SNOWLIGHT sample' and 'CVE-2026-34486 (Java deserialization, CommonsCollections6 gadget) - Taiwan-focused, delivers SNOWLIGHT', attributed to 'China-nexus access brokers UNC5174 and UNC6586'. The same claim appears in sourcing_note ('no vendor or research lab has published named-cluster telemetry, so who is exploiting it is unknown')."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "CVE-2026-34486 — Apache Tomcat EncryptInterceptor fail-open (KEV)"
  url_or_quote: "this is a roughly ten-week gap between a public fix and confirmed exploitation"
  summary: "Arithmetically wrong against the entry's own dates: public 2026-04-09 (release 2026-04-04) to KEV addition 2026-08-04 is ~117 days, roughly seventeen weeks / four months. No cited source states any interval."
- code: F14
  category: quantifier-without-source
  section: trending-vulnerabilities
  item: "CVE-2026-18574 — Check Point Security Management auth bypass"
  url_or_quote: "It is the fourth authentication bypass disclosed in this same management stack in roughly two weeks."
  summary: "No cited source states a count. Against the pipeline's own prior coverage the tally is two authentication bypasses (CVE-2026-16232, CVE-2026-18574): 2026-07-25 records CVE-2026-62144 as 'an unauthenticated command-execution flaw' and CVE-2026-62145 as 'a Gaia Portal read-only-to-root escalation' — the latter on a different surface from Security Management. The claim also appears in the headline ('A fourth Check Point management-plane auth bypass') and body ('This is the fourth authentication bypass in this stack in roughly two weeks'). Recast as e.g. 'the fourth CVE on this management surface in roughly two weeks, and the second authentication bypass'."
- code: F14
  category: quantifier-without-source
  section: research
  item: "Talos analyses threat actors' own AI coding-assistant prompt logs"
  url_or_quote: "pulling source-code and credential material from thousands of exposed systems"
  summary: "Talos states 'collected output contains information from 54 targets'. The only 'thousands' figure on the page is a file count — 'The \"dump/AKIA/\" tree alone held 3,048 source files (312MB)'. A file count has been bound to a system count, inflating 54 compromised targets into 'thousands of exposed systems'."
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "CVE-2026-34486 — Apache Tomcat EncryptInterceptor fail-open (KEV)"
  url_or_quote: "cves[0].cvss: \"7.5\" / 'operators who did not treat a 7.5-rated clustering flaw as urgent'"
  summary: "Neither cited source carries a CVSS score. The score is correct per the Apache CNA record (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N = 7.5) but is untraceable from the entry. Name the authority in sourcing_note; note also that the CNA vector is confidentiality-only (I:N/A:N), which sits awkwardly with type: rce."
- code: F5
  category: missing-citation
  section: trending-vulnerabilities
  item: "Traefik 3.7.10 / 3.6.25 / 2.11.54 — route identity collision"
  url_or_quote: "The third, rated 2.1, is a BasicAuth deduplication-key collision where the cache key concatenates password and stored secret without a delimiter..."
  summary: "No inline citation, and the advisory described (GHSA-6765-c87h-8mrf) is absent from sources[]. Neither cited GHSA describes it and CERT-FR AVI-0964 carries only a one-line generic summary. Content verified accurate against https://github.com/traefik/traefik/security/advisories/GHSA-6765-c87h-8mrf ('Its key is the delimiter-free concatenation `password + secret`', CVSS v4 2.1) — add it as a third primary."
- code: F5
  category: missing-citation
  section: active-threats
  item: "ByteToBreach hits Hungary's State Treasury"
  url_or_quote: "that intrusion ran to enumeration of the virtualization estate, deletion of virtual machines and ransomware on the hypervisors"
  summary: "None of the three cited sources carries this. KELA's ByteToBreach report says only 'The actor also claims to have deployed ransomware across the agency's network'; Telex covers Hungary only; Risky Bulletin carries the actor-continuity line. The claim is supported by the referenced prior entry 2026-07-26/ancpi-romania-dnsc-report-2m-epayment-records-exfiltrated (DNSC: vCenter, 1,083 VMs enumerated, ~100 deleted, ESXi encrypted). Attribute it in-text to that prior coverage."
- code: F10
  category: missed-angle
  section: active-threats
  item: "SOCRadar SNOWLIGHT / UNC5174-UNC6586 China-nexus government campaign"
  url_or_quote: "https://socradar.io/blog/snowlight-government-chinese-campaign/"
  summary: "2026-07-31 report on an exposed adversary staging server: nine weaponised CVEs incl. CVE-2026-34486, GoCobaltStrike, SNOWLIGHT loaders, 107 confirmed endpoint compromises across 100+ countries focused on government infrastructure, attributed to UNC5174/UNC6586 via GTIG. Zero hits for snowlight/unc5174/unc6586 in prior_coverage.json; store's only material is 2026-05-04 and 2026-07-10. Outside the 26 h window as a new item, but the obvious pivot from this run's own Tomcat entry. Query: SOCRadar SNOWLIGHT UNC5174 UNC6586 staging server government CVE-2026-34486."
- code: F17
  category: classification
  section: active-threats
  item: "N-able N-central post-exploitation, unpacked"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "Credibility 1 (confirmed by other sources) contradicts the entry's own sourcing_note: 'Sophos X-Ops is the primary and sole source for the post-exploitation detail'. The KEV listing corroborates only that CVE-2026-18556 is exploited, not the six RMM tools, renamed tunnel client, PhantomKiller driver or DC pivot that make up the entry. Should be 2."
- code: F17
  category: classification
  section: trending-vulnerabilities
  item: "Traefik 3.7.10 / 3.6.25 / 2.11.54 — route identity collision"
  url_or_quote: "classification: {reliability: A, credibility: 1}"
  summary: "Vendor-primary advisories plus a CERT-FR relay. The Check Point entry in this same run — vendor primary plus CERT-FR AND BSI relays, a stronger set — is rated credibility 2, as is Tomcat. A national-CERT restatement of a vendor advisory is not independent confirmation. Align to 2 or justify in sourcing_note."
- code: F11
  category: editorial-advisory
  section: cross-cutting
  item: "Evidence-quote terminal truncation (4 entries)"
  url_or_quote: "Kaspersky evidence[1]; Traefik evidence[1]; Hungary evidence[0]; N-able evidence[0]"
  summary: "Four quotes truncated at a clean clause boundary and closed with a full stop the source does not carry, or recapitalised from mid-sentence — the same class the run record documents correcting on a Unit 42 quote. None is materially misleading; tidy or leave."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-9198 — Langflow auto-login/validate-code (KEV)"
  url_or_quote: "priority: notable"
  summary: "CVSS 9.8 pre-auth RCE, KEV-listed 2026-08-04, third confirmed-exploited pre-auth path in the product, one sibling still unfixed, action is 'take instances off the public internet'. CVE-2026-34486 in the same KEV batch is priority: high at CVSS 7.5 behind three stacked preconditions. Does not clear the critical bar (it is an update), so not F16 — but the relative placement warrants a second look."
- code: F11
  category: editorial-advisory
  section: research
  item: "Surface items — AISI typo; Unit 42 NOVA title"
  url_or_quote: "'OpenAI records that its own model reused a access token' / 'Unit 42's NOVA pipeline reports 14,090 ... 92% ...'"
  summary: "Article agreement in the AISI body. Unit 42 title leads with three vendor-self-reported volume figures; the body's caveats are exemplary and the entry earns its place on the semantic-vs-memory-safety lesson, but the title is where it reads closest to a vendor metrics post."
```
