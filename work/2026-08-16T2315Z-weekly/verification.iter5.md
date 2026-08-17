**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-17T01:12:47Z · ended_at=2026-08-17T01:30:19Z · duration_seconds=1052
**Self-telemetry:** urls_checked=34 · webfetch_calls=24 · bridge_fetches=10

## Verification report — 2026-08-16T2315Z-weekly (iteration 5)

Read cold: all 15 entry files end to end (frontmatter and body), the run record, the prior-coverage index, the registry, and 9 of the run's referenced operational entries. 34 distinct source URLs fetched in this iteration (`WebFetch`, `tools/fetch_source.py url`, `cisa-kev`, `ncsc-csh post`), including every source on the five entries the spawn message flagged and every source carrying a numeral that appears in a title, headline or summary. Where a page 403'd the routine UA (ico.org.uk, etsi.org, nltimes.nl, foresiet.com, gazetaprawna.pl) I escalated to the bridge and extracted the raw body text rather than relying on a summariser.

### Prior-iteration remediations — re-derived independently

I re-derived all five intervals in `weekly-w33-disclosure-to-exploitation-interval-collapsed` from the cited primaries, not from the entry:

| product | disclosure | observed exploitation | interval | entry's claim |
|---|---|---|---|---|
| SAP Commerce Cloud CVE-2026-58231 | patch day 11 Aug (BleepingComputer) | 14 Aug, "3 days after patch day" (Defused via BleepingComputer) | 3 d | "inside three days" ✓ |
| SharePoint CVE-2026-55040 | Rapid7 PoC "on Tuesday" = 11 Aug (BleepingComputer, article 12 Aug 08:25) | 12 Aug morning | ~1 d | "inside three days" / "roughly a day" ✓ |
| GeoServer jsonArrayContains | researcher post 12 Aug (SecurityWeek) | "within hours" | <1 d | "inside three days" ✓ |
| vCenter CVE-2026-59310 | 29 Jul (THN, "five days after") | 3 Aug first contact | 5 d | "five days" ✓ |
| macOS CVE-2026-65400 | out-of-band patch 6 Aug | NCSC-2026-0280 v1.0.1, 12 Aug | 6 d | "six days" ✓ |

Headline ("Three products drew observed attacks inside three days, two more inside a week"), summary three-two split, and the title's "inside a week" are all correct. The rollup's independent correction is also right: its "eight" excludes GeoServer (no identifier, counted separately), so "two of them within seventy-two hours" (SAP, SharePoint) does not contradict the lead entry's "three inside three days" (which includes GeoServer) — the populations genuinely differ. The ETSI category fix is correct: I fetched `docbox.etsi.org/CYBER/EUSR/Open` and counted the draft filenames — EN 304-617 through 304-636 (617–627, 631–636) = 17 verticals, matching the body's list item for item, and the summary's "13 named + four consumer and IoT categories" reconciles to the same 17.

**But the class the spawn message asks about is not exhausted.** Nine truth-class defects survive, seven of them numerals or quantifiers in a title, headline or summary that the entry's own body or sources do not carry, and two of them (F1, F2) in the same MyDr thread. Details below.

### Citation does not support the claim

**F1 — `weekly-w33-compromised-party-was-not-the-notifying-party`: MyDr paragraph, two citations swapped.**
Entry: *"The following day the Deputy Prime Minister and digital affairs minister put the stolen database at nearly 19 million people and over 2 TB ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/))"*.
I fetched that page and searched its extracted body text: `TB` occurs **0** times, `terabyte` **0** times, `Deputy` **0** times. It says *"digital affairs minister Krzysztof Gawkowski"* and *"The personal data of almost 19 million people"*. Both the 2 TB figure and the Deputy-PM title belong to the **co-cited Gazeta Prawna**, which reads *"Wicepremier, minister cyfryzacji Krzysztof Gawkowski … wicepremier poinformował, że wykradziona baza ma ponad 2 TB danych."*
The converse splice sits in the next clause of the same paragraph: *"the obligation to notify affected individuals rests with the healthcare controllers that used MyDr's services — around 12,000 medical facilities ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html))"*. Gazeta Prawna carries the UODO duty finding verbatim but **no facility count** (searched `12 tys`, `12 000`, `12000`, `tysięcy`, `placówek`, `przychodni` — all 0). The 12,000 is Notes from Poland's.
**Fix: swap the two citations.**

**F5 — `weekly-w33-vuln-status-rollup`: Adobe exploitation clause cited to Adobe's own bulletin.**
Entry: *"**CVE-2026-71362** in Adobe Commerce is an unauthenticated customer-account takeover which Adobe's own bulletin records as needing no authentication, privileges or user interaction, and which a forensics vendor reported already blocking attempts against ([Adobe PSIRT, 2026-08-11](https://helpx.adobe.com/security/products/magento/apsb26-92.html))."*
I fetched APSB26-92. It lists CVE-2026-71362 at CVSS 9.1, `AV:N/AC:L/PR:N/UI:N`, CWE-863 — so the first half is right — and it states *"Adobe is not aware of any exploits in the wild for any of the issues addressed."* It does not mention Sansec, a WAF, or blocked attempts. That claim is Sansec's (`https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92`, quoted as *"Sansec Shield already blocks exploitation attempts."* in this pipeline's own operational entry of 2026-08-16), and **Sansec is not in this entry's `sources[]`**. This matters twice: the Sansec observation is the entry's only basis for placing CVE-2026-71362 among the eight "newly confirmed exploited" in its own summary.
**Fix: add the Sansec source record and attach the clause to it.**

**F6 — `weekly-w33-clop-windchill-status`: the BleepingComputer quotation is not verbatim and drops the hedge.**
Entry: *BleepingComputer … says Cl0p **"listed Shell among 43 victims targeted through exploiting CVE-2026-12569 in PTC Windchill and FlexPLM instances"***.
Actual page text (bridge-fetched, exact): *"the Clop gang listed it on its leak site as one of 43 new victims **likely** targeted in data theft attacks against Internet-exposed PTC Windchill and FlexPLM instances exploiting a critical improper input validation vulnerability tracked as CVE-2026-12569"*.
The quoted string is not a contiguous substring of the page, and it removes the outlet's *"likely"* — turning a hedged attribution into a flat assertion, inside the entry whose declared subject is the distance between a Cl0p claim and a confirmation, and whose own next sentence is "Neither figure is a count of confirmed victims."
**Fix: quote verbatim, or paraphrase outside quotation marks retaining "likely".**

**F9 — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: the four-hour build dated two days early.**
Entry summary: *"The Screen Sharing case also carries the week's shortest interval of a different kind — one team rebuilt two working pre-authentication root exploits from the patch diffs in about four hours, six days before that confirmation."*
I bridge-fetched the Calif post and read its timeline table: *"| Thu Aug 6 | macOS 26.6.1 (25G76) … ship out of band. |"* then *"| **Sat Aug 8 (APAC)** | We start on the 26.6.1 diff, and have a working exploit about four hours later. |"*, with the narrative *"Two pre-auth remote root exploits in four hours, on and off, across a busy weekend."* (The two-exploits figure is correct — the second came from diffing 26.5.2 against 26.6.) The build was **8 August, four days before** NCSC-NL's 12 August confirmation. Six days before that confirmation is 6 August, the *patch* date. This is the same clock-splice the previous iteration corrected in this entry, surviving in a different clause.
**Fix: "four days before that confirmation", or drop the interval and keep the dates.**

### Unsupported / hallucinated facts

**F2 — `weekly-w33-looking-ahead`: the 12,000-clinics figure has no supporting source anywhere in the entry.**
Title: *"twelve thousand Polish clinics who each owe a notification"*. Headline: *"a notification duty split across 12,000 controllers"*. Body: *"**Around 12,000 Polish medical facilities each owe their own patients a notification** over the MyDr breach … ([Gazeta Prawna, 2026-08-13](…))"*.
As established in F1, Gazeta Prawna carries no facility count, and this entry's `sources[]` (ETSI, SecurityWeek, Gazeta Prawna, NCSC-NL, BleepingComputer, Cyber Kendra, Calif) contains no Notes from Poland record. The number the title, headline and one of seven bullets all turn on is uncited across the entry.
**Fix: add the Notes from Poland source record and cite it for the count, or drop the number.**

### Claims missing inline citation

**F10 — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: SAP rebuild-and-redeploy.**
Entry: *"The fix for this component only takes effect after a rebuild and redeploy, so an estate that merely applied the note is in the exposed population rather than the patched one."*
No citation. The preceding citation, NCSC-2026-0302, I fetched in full: `rebuild` 0, `redeploy` 0, no Dutch equivalent — it says only *"SAP heeft updates uitgebracht om de kwetsbaarheden te verhelpen."* The BleepingComputer article cited earlier in the paragraph does not mention it either. This pipeline's operational entry of 2026-08-12 sources the claim correctly, to Onapsis Research Labs (`https://onapsis.com/blog/sap-security-patch-day-august-2026/`), which is absent from this entry's `sources[]`. The claim is load-bearing — it tells a reader their change record is wrong.
**Fix: add the Onapsis source record, or attribute it in prose the way the Gunra and Forescout claims are attributed elsewhere in this run.**

### Quantifier without source

**F3 — `weekly-w33-kernel-rootkits-edit-what-windows-reports`.**
Entry: *"Check Point Research published the analysis behind CVE-2026-68820 on 11 August, **the sole exploitation-detected flaw in that day's Microsoft updates**."*
I fetched the Check Point post. It carries the AFD.sys use-after-free, the FudModule v3.1 deployment, the MSRC timeline (reported 28 Jul, confirmed 31 Jul, CVE assigned 5 Aug, fixed 11 Aug), the *"successful targeting observed in Western Europe, including France and Germany"* line, the telemetry-teardown sentence and the reused French organisation — every other fact in the paragraph checks out — but it makes **no statement whatever about the rest of the August 2026 Microsoft updates**. No Microsoft advisory or patch-roundup source appears in the entry. (For what it is worth, the KEV catalogue I fetched shows exactly one Microsoft CVE added 2026-08-11; that is corroborative, is not the same claim, and is not cited.)

**F4 — `weekly-w33-vuln-status-rollup`: same quantifier, independently.**
Entry: *"**CVE-2026-68820** was the sole exploitation-detected flaw in August's Microsoft updates, and Check Point's analysis records that … ([Check Point Research, 2026-08-11](…))"*. Same page, same gap.
**Fix (both): cite a source that carries the quantifier, or drop the clause — the entries lose nothing without it.**

**F7 — `weekly-w33-clop-windchill-status`: summary says two deltas, body says three.**
Summary: *"**Two in-window deltas** move it from claim to partial corroboration."* It then describes three — the 44 named European listings, the Philips and Shell responses, and the ReliaQuest webshell corroboration. The body: *"**Three things changed this week**"*, and later *"**The third delta** is corroboration rather than novelty"*. The title also enumerates three: *"Philips and Shell responded, European organisations appeared among the named listings, and a second vendor confirmed the webshell artefact"*.
**Fix: say three in the summary, or say two and explicitly place the ReliaQuest item outside the delta count.**

**F8 — `weekly-w33-compromised-party-was-not-the-notifying-party`: "seven" against six enumerated.**
Title: *"A third party was on the access path or holding the data in **every** European public-sector and critical-infrastructure disclosure this week"*. Summary: *"**Seven** European disclosures across 2026-W33 share a structure rather than a sector"*. Body: *"in **all seven** of the week's European public-sector and critical-infrastructure disclosures a third party stood somewhere on the line"*.
The entry enumerates **six** incidents in both summary and body: MyDr, CEVA Logistics, DGFiP, Retelit, Żabka, ACRO. `entities[]` carries exactly six `incident:`/case keys. The seven `references[]` include two entries covering the *same* MyDr incident (`mydr-…-processor-gap` and `mydr-…-19-million`). The only candidate seventh is bol.com, which appears solely as one of the ten organisations that had to notify *because of* the CEVA intrusion — a downstream notification of case two, not a separate disclosure — and which is neither public-sector nor critical infrastructure. (I verified the CEVA facts against TechCrunch: *"The agency has received data breach reports from 10 organizations in relation to the incident"* ✓.)
**Fix: state six, or name the seventh explicitly and justify it against the title's own scope.**

### Editorial / less-is-more flags (advisory)

**F11 — `weekly-w33-disclosure-to-exploitation-interval-collapsed`: "the trigger differed every time".**
Summary: *"Five unrelated products were reported under exploitation close behind their own disclosure … and **the trigger differed every time**."* The title names four trigger types for five products (*"a patch day, a proof-of-concept, a researcher's post and a binary diff"*), and the body describes SAP's attackers' starting material as *"the patch itself"* and Calif's as *"a patch diff alone"* — the same class. Leave-able; "the trigger was different almost every time" carries the point without the absolute.

### Checks that came back clean

Worth recording, because the spawn message asks for a sweep and a negative result is a result:

- **Every other numeral and quantifier in a title, headline or summary reconciles.** Rollup: eight newly exploited/catalogued (8 named in summary; 3 + 5 in body) ✓; "eight flaws with no fix" (ShieldBreak 1 + FreeBSD 3 + GeoServer 1 + NatJack 3 = 8, and NatJack's "three of five" checks against the 2026-08-10 entry: five primitives, two CVEs) ✓; looking-ahead "seven further flaws" (8 minus GeoServer) ✓; ETSI 17 ✓; Q2 reports (1,140 / 1,020 = 12% ✓, 747 = 65% ✓, 431 = 38% ✓, 37→68 = 84% ✓, 2,139 ✓, 57.6% / 71% / 71→93 ✓, all verbatim in the two reports); Wiz 09:14–14:55 UTC = "about six" hours ✓, 102 IPs ✓, 56% / Forbes AI 50 ✓; SOCRadar 2,085 of 2,188 = 95% ✓; ExfilSquad 13 orgs / 382.64 GB / 27 M records / 10,000+ Power Pages ✓; ACRO 10,920 and Aug 2022–Mar 2023 ✓; DGFiP 678,000 ✓; Retelit 3 of 38 data centres, 193 public administrations, ACN-certified Milan site ✓; CrowdStrike 21 techniques / six categories / ESX 7.0.3 ✓; Jewelbug "more than 15 government webmail tenants … in a Middle Eastern country" ✓.
- **Every `evidence[]` quote I checked is a contiguous verbatim substring** of the page it is attributed to — including the two long CISA ICSA-21-056-03 passages (I parsed the CSAF JSON: the Vulnerability Summary and the Risk Evaluation notes both match character for character), the Dutch NCSC-NL and NCSC-2026-0302 sentences, the Dragos and Check Point Q2 passages, the Group-IB, Sophos, Kaspersky and Calif lines. The one non-verbatim quotation in the run is F6, and it is in body prose rather than `evidence[]`.
- **The water-PLC contradiction entry is the strongest entry in the run.** Every element checks: Dragos's two quotes verbatim; Dragos's CVSS 9.8 against CISA's *"A CVSS v3 base score of 10.0 has been calculated"*; the CSAF product tree exactly as the entry states it (RSLogix 5000 16–20, Studio 5000 Logix Designer ≥21, FactoryTalk Security ≥2.10, title "Rockwell Automation Logix Controllers"); *"Rockwell Automation has determined this vulnerability cannot be mitigated with a patch"* verbatim; KEV `dateAdded` 2026-03-05 for CVE-2021-22681 and CVE-2017-16740 absent; and the 19-of-22 Forescout ratio matches the 2026-08-10 entry's own quoted figure.
- **Frontmatter ⇔ body.** No `cves[]` record overstates its source (CVE-2026-34348 CVSS 6.5 and CVE-2021-22681 CVSS 10.0 both verified against the owning authority). `affected_products[]` values are all named in cited sources. No `techniques[]` id lacks a body behaviour; no attacker-behaviour entry ships an empty list. `verification` values match the sourcing in every case, including `single-source`, `single-source-national-cert` and `contradicted`. `update_of` targets are the right stories and each update carries a real delta.
- **F12/F16/F17/F18: none.** Both single-source entries carry the correct `verification` value plus a `sourcing_note` naming the basis, and both are surfaced in the run record. No `org_triage` block is non-null; no `watchlist_hit: true`; no `watchlist` tag — correct for a profile with neither configured. All fifteen entries carry a valid Admiralty `classification`, and each letter/number pair is defensible against the entry's own sourcing (A/1 ETSI with independent corroboration, A/2 NCSC-NL single authority, C/2 the single-source passkey entry, B/3 the contradicted water entry, B/1 the multi-source syntheses). All fifteen carry `actions: []`, which is correct for strategic entries.
- **Style.** No IOCs in any entry — no hash, IP, attacker domain or rule fragment, including in the entries whose sources are dense with them. No vanity metrics presented as findings. English throughout. No workflow-internal vocabulary in any entry body.
- **Coverage.** I looked for a nameable in-window omission and did not find one. The run record's borderline-drop reasoning (Recorded Future crypting-service survey, NCSC-UK water OT worked example, the incidents-recap pairing) is defensible on the profile's own bar; the tracked-waves-with-no-delta note (Joomla, npm/Shai-Hulud, ShinyHunters) makes three absences read as checked rather than unswept; the coverage-gaps list names the sources that could not be reached and why. The Truesec item the telemetry flags as fetched-but-untriaged did ship, as `weekly-w33-russia-europe-ukraine-defence-supply-chain`. No F10.

### Verdict

**NEEDS_FIXES (truth: 9, editorial: 1, advisory: 1)**

Direct answer to the publish question: **the defect class is not exhausted, and I would not publish this run as it stands.** But the shape of what is left has changed, and that is the useful signal. Iterations 1–4 were finding *arithmetic* errors — a count that was wrong about the world (macOS was not exploited inside three days; there were not three flaws inside seventy-two hours; sixteen categories were named where seventeen exist). Those are gone: I re-derived every interval and every enumeration from the primaries and they now hold. What survives is a different and shallower failure — **attribution drift in the last citation of a clause**: a true fact hung on a page that does not carry it (F1, F2, F5, F10), a true figure hung on the wrong date (F9), a real quotation trimmed of its hedge (F6), and three summary-level counts that disagree with the body they sit above (F4/F7/F8, plus F3). Every one is a one-line repair, none requires re-reporting anything, and none of the underlying facts is wrong.

That distinction matters for the decision: this is not the same defect resurfacing, it is the residue left after the arithmetic was fixed — the class the pipeline's own guidance names as the dominant residual, a true fact cited to a co-cited source that does not state it. It is exactly what a citation-by-citation sweep is supposed to surface, and it does not recur once the citations are moved. I would expect iteration 6 to close all eleven and iteration 7 to confirm clean.

One process observation for the operator, offered as an observation and not a finding: F1, F2, F5 and F10 are all the same mechanic — a fact carried forward from an operational entry into a weekly entry that inherited the *claim* but not the *source record*. Three of the four are repairable by adding a `sources[]` record that already exists in the referenced operational entry. If weekly composition copied the source record along with the sentence, this class would largely disappear.

### Findings summary (machine-readable)

See `work/2026-08-16T2315Z-weekly/verification.iter5.findings.yaml` — identical payload, unfenced, for `yq` parsing.

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: weekly-sector-patterns
  item: "weekly-w33-compromised-party-was-not-the-notifying-party — MyDr paragraph citation swap"
  url_or_quote: "the Deputy Prime Minister and digital affairs minister put the stolen database at nearly 19 million people and over 2 TB ([Notes from Poland, 2026-08-13](https://notesfrompoland.com/2026/08/13/poland-hit-by-theft-of-19-million-patients-data-from-medical-platform/))"
  summary: "Fetched Notes from Poland this run: the string 'TB' occurs 0 times and 'Deputy' occurs 0 times; it calls Gawkowski only 'digital affairs minister' and gives 'almost 19 million'. Both the 2 TB figure and the Deputy-PM title belong to the co-cited Gazeta Prawna ('Wicepremier, minister cyfryzacji Krzysztof Gawkowski ... wykradziona baza ma ponad 2 TB danych'). Converse splice in the same paragraph: 'around 12,000 medical facilities ([Gazeta Prawna, 2026-08-13])' - Gazeta Prawna contains no 12,000 figure (searched '12 tys', '12 000', '12000', 'tysiecy', 'placowek' - all 0); Notes from Poland carries '12,000 medical facilities'. Fix: swap the two citations."
- code: F4
  category: hallucinated-fact
  section: weekly-looking-ahead
  item: "weekly-w33-looking-ahead — 12,000 Polish clinics figure has no supporting source in the entry"
  url_or_quote: "**Around 12,000 Polish medical facilities each owe their own patients a notification** over the MyDr breach ... ([Gazeta Prawna, 2026-08-13](https://www.gazetaprawna.pl/prawnik/artykuly/11289449,uodo-reaguje-na-gigantyczny-wyciek-danych-wazny-apel-do-polakow.html))"
  summary: "Gazeta Prawna, fetched this run, carries the UODO notification-duty finding but no facility count. The 12,000 figure is in Notes from Poland, which is not among this entry's sources[] at all. The title ('twelve thousand Polish clinics who each owe a notification'), headline ('a notification duty split across 12,000 controllers') and summary all turn on the number. Fix: add the Notes from Poland source record and cite it for the count, or drop the number."
- code: F14
  category: quantifier-without-source
  section: weekly-top-stories
  item: "weekly-w33-kernel-rootkits-edit-what-windows-reports — 'the sole exploitation-detected flaw'"
  url_or_quote: "Check Point Research published the analysis behind CVE-2026-68820 on 11 August, the sole exploitation-detected flaw in that day's Microsoft updates."
  summary: "Fetched research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/ this run: it documents CVE-2026-68820, its AFD.sys use-after-free root cause, the MSRC timeline (reported 28 Jul, confirmed 31 Jul, CVE assigned 5 Aug, fixed 11 Aug) and the FudModule v3.1 deployment, but makes no statement about the rest of August 2026 Patch Tuesday. No Microsoft or patch-roundup source is cited in this entry. The KEV catalogue (fetched this run) shows exactly one Microsoft CVE added 2026-08-11, which is corroborative but is neither the same claim nor cited. Fix: cite a source that carries the quantifier, or drop the clause."
- code: F14
  category: quantifier-without-source
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup — 'the sole exploitation-detected flaw in August's Microsoft updates'"
  url_or_quote: "**CVE-2026-68820** was the sole exploitation-detected flaw in August's Microsoft updates, and Check Point's analysis records that ... ([Check Point Research, 2026-08-11](https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/))"
  summary: "Same defect, independently, in the second entry: the only citation on the clause is the Check Point post, which I fetched and which says nothing about the composition of the August Microsoft updates. Fix as above."
- code: F3
  category: claim-not-supported
  section: weekly-vuln-rollup
  item: "weekly-w33-vuln-status-rollup — Adobe Commerce exploitation clause cited to Adobe's own bulletin"
  url_or_quote: "which a forensics vendor reported already blocking attempts against ([Adobe PSIRT, 2026-08-11](https://helpx.adobe.com/security/products/magento/apsb26-92.html))"
  summary: "Fetched APSB26-92 this run: it lists CVE-2026-71362 (CVSS 9.1, no authentication, no privileges, no user interaction) and states 'Adobe is not aware of any exploits in the wild for any of the issues addressed'. It never mentions Sansec, a WAF, or blocked attempts. The blocking claim is Sansec's (https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92, cited in this pipeline's own operational entry of 2026-08-16), and Sansec is not in this entry's sources[]. This matters twice over: the Sansec observation is the entry's only basis for listing CVE-2026-71362 among the eight 'newly confirmed exploited'. Fix: add the Sansec source record and attach the clause to it."
- code: F3
  category: claim-not-supported
  section: weekly-long-running
  item: "weekly-w33-clop-windchill-status — quotation of BleepingComputer is not verbatim and drops the source's hedge"
  url_or_quote: "BleepingComputer ... says Cl0p \"listed Shell among 43 victims targeted through exploiting CVE-2026-12569 in PTC Windchill and FlexPLM instances\""
  summary: "Fetched the article this run. Its actual text: 'the Clop gang listed it on its leak site as one of 43 new victims likely targeted in data theft attacks against Internet-exposed PTC Windchill and FlexPLM instances exploiting a critical improper input validation vulnerability tracked as CVE-2026-12569'. The entry's quoted string is not a contiguous substring of the page and it removes 'likely', converting a hedged attribution into a flat one - in the entry whose whole subject is the gap between actor claim and confirmation. Fix: quote verbatim or paraphrase without quotation marks, retaining 'likely'."
- code: F14
  category: quantifier-without-source
  section: weekly-long-running
  item: "weekly-w33-clop-windchill-status — summary says two deltas, body says three"
  url_or_quote: "Two in-window deltas move it from claim to partial corroboration."
  summary: "The summary then describes three (the 44 named European listings; the Philips and Shell responses; the ReliaQuest JSP-webshell corroboration). The body says 'Three things changed this week' and later 'The third delta is corroboration rather than novelty'. The title also enumerates three ('Philips and Shell responded, European organisations appeared among the named listings, and a second vendor confirmed the webshell artefact'). Fix: make the summary say three, or say two and explicitly exclude the ReliaQuest item from the delta count."
- code: F14
  category: quantifier-without-source
  section: weekly-sector-patterns
  item: "weekly-w33-compromised-party-was-not-the-notifying-party — 'Seven European disclosures' against six enumerated"
  url_or_quote: "Seven European disclosures across 2026-W33 share a structure rather than a sector" / "in all seven of the week's European public-sector and critical-infrastructure disclosures a third party stood somewhere on the line"
  summary: "The entry enumerates six incidents, in both summary and body: MyDr, CEVA Logistics, DGFiP, Retelit, Zabka, ACRO. entities[] carries exactly six incident keys. The seven references[] include two entries covering the same MyDr incident (mydr-...-processor-gap and mydr-...-19-million). bol.com is the only candidate seventh and it appears solely as one of the ten organisations that had to notify because of the CEVA intrusion - a downstream notification of case two, not a separate disclosure, and neither public-sector nor critical infrastructure. The title's 'every European public-sector and critical-infrastructure disclosure this week' rests on the same count. Fix: state six, or name the seventh explicitly."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w33-disclosure-to-exploitation-interval-collapsed — four-hour exploit build dated to the wrong day"
  url_or_quote: "one team rebuilt two working pre-authentication root exploits from the patch diffs in about four hours, six days before that confirmation"
  summary: "Fetched blog.calif.io/p/no-country-for-old-passwords this run and read its timeline table: 'Sat Aug 8 (APAC) | We start on the 26.6.1 diff, and have a working exploit about four hours later', and the post's own strapline 'Two pre-auth macOS remote root exploits in four hours' / 'Two pre-auth remote root exploits in four hours, on and off, across a busy weekend'. The two-exploits-in-four-hours figure is correct. The date is not: the work happened on 8 August, four days before NCSC-NL's 12 August confirmation. Six days before that confirmation is 6 August - the patch date, not the exploit-build date. This is the same clock-splice class the previous iteration corrected in this entry, surviving in a different clause. Fix: 'four days before that confirmation', or drop the interval and keep the dates."
- code: F5
  category: missing-citation
  section: weekly-top-stories
  item: "weekly-w33-disclosure-to-exploitation-interval-collapsed — SAP rebuild-and-redeploy claim carries no citation"
  url_or_quote: "The fix for this component only takes effect after a rebuild and redeploy, so an estate that merely applied the note is in the exposed population rather than the patched one."
  summary: "No inline citation. The preceding citation is NCSC-2026-0302, which I fetched: it contains 'rebuild' 0 times, 'redeploy' 0 times and no Dutch equivalent, and says only that SAP has released updates. The BleepingComputer article cited earlier in the paragraph does not mention it either. This pipeline's own operational entry of 2026-08-12 sources the claim to Onapsis Research Labs (https://onapsis.com/blog/sap-security-patch-day-august-2026/), which is not in this entry's sources[]. Fix: add the Onapsis source record and cite it, or attribute the claim to the referenced operational entry in the prose the way the Gunra and Forescout claims are attributed elsewhere in this run."
- code: F11
  category: editorial-advisory
  section: weekly-top-stories
  item: "weekly-w33-disclosure-to-exploitation-interval-collapsed — 'the trigger differed every time'"
  url_or_quote: "Five unrelated products were reported under exploitation close behind their own disclosure in the week to 2026-08-16, and the trigger differed every time."
  summary: "Advisory only - leave-able. Five products, but the entry names four trigger types (title: 'a patch day, a proof-of-concept, a researcher's post and a binary diff'), and the body describes SAP's attackers' starting material as 'the patch itself' and Calif's as 'a patch diff alone' - the same trigger class. 'Differed every time' is a rhetorical overreach against the entry's own enumeration. 'and the trigger was different almost every time' or 'and no two triggers were quite the same' would carry the point without the absolute."
```
