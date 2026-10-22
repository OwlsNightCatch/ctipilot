**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T11:14:01Z · ended_at=2026-10-22T11:44:20Z · duration_seconds=1819

## Verification report — 2026-10-21T1148Z-audit (iteration 1, slice 2 of 3)

Scope: 24 updated entries, 493 ledger claims, one verdict row each in `verification.iter1.s2.claims.yaml` (462 ok, 31 non-ok; none unreadable). First pass, so every claim was walked; no deltas block. Pages read from the truth/repair caches, plus fresh fetches of ENISA EUVD (DHTMLX, BBB via cache, Szafir, OpenClaw), NVD (OpenClaw CVSS), NCSC-NL CSAF (AMD), the CISA KEV feed (dateReleased 2026-10-21T14:04Z) and F5/Packagist pages. The my.f5.com page is a JavaScript shell that extract, raw and WebFetch cannot read. Mechanical checks done: every changed frontmatter key is declared in the run's record `fields` (no silent edit), `updates[]` append-only and `discovered_at`/`run_id` untouched on all 24, `updated_at` unmoved (corrections), every `entities` key exists in the registry and none is tombstoned, every `techniques[]` id is active in the pinned ATT&CK v20 dataset, no hashes or IPs, em dashes only in two pre-existing record summaries.

### Generic / oversight URLs (replace with specific article)

1. **2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy** — KEV catalogue feed cited for per-CVE claims (also Nextcloud, Composer)  
   Quote: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json  
   (low confidence) The cited URL is the whole KEV catalogue feed (1,754 entries), not a per-CVE page; for the positive claim "listed since 2022-09-30" MSRC's per-CVE page (exploited: Yes) or the CISA per-CVE entry is a more specific citation. The negative "not listed as of 2026-10-21" claims on Nextcloud and Composer can only be checked against the feed.

### Citation does not support the claim

2. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — Correction section 2026-10-21T20:28:35Z and record summary: RubyDoc.info "not a RubyGems service" (claims bd4bf64cde, 7964ec0658, de97ac9d83)  
   Quote: "RubyDoc.info is a separate site that builds documentation for published gems, not a RubyGems service ([Nightingale Collective, 2026-09-11](https://rubyhack.ai/))" / "No source places RubyDoc.info inside RubyGems' trust boundary"  
   (low confidence) The cited rubyhack.ai page says only that "the site RubyDoc.info builds and hosts documentation" and its own heading reads "The agents used RubyGems' automatic build system to achieve remote code execution"; the RubyGems blog calls it "shared Ruby infrastructure". No cited page states RubyDoc.info is not a RubyGems service, and the cited page frames it the other way.

3. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — Exposure line (claim 5479e452f9)  
   Quote: "**Exposure:** no existing package or user was compromised ([Ruby Central, 2026-09-11](https://blog.rubygems.org/2026/09/11/update-may-spam-publishing-campaign.html))"  
   (low confidence) The RubyGems blog says "Gem installs and pushes for existing users remained unaffected" and found "no evidence that these attempts [key theft] succeeded"; the no-existing-package-compromised wording is Socket quoting Ruby Central in May, not on the cited page.

4. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — Triage line (claim db0c187d17)  
   Quote: "a push from a pipeline with no publishing role has no benign explanation in Socket's analysis"  
   (low confidence) Socket only recommends blocking outbound gem push in CI that does not publish gems; it never says such a push has no benign explanation.

5. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — 2026-09-19 section (claim 9c12f423ad)  
   Quote: "a contact address impersonating OpenAI ([Nightingale Collective, 2026-09-11](https://rubyhack.ai/))"  
   (low confidence) rubyhack.ai lists openaixyz65947@gmail.com under "Agents self-identified as being from OpenAI"; it does not say the address impersonates OpenAI.

6. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — 2026-09-19 section (claim 64ebd61bd4)  
   Quote: "Euractiv sets this against OpenAI's notification of July's Hugging Face incident to the AI Office ([Euractiv, 2026-09-18]...)"  
   (low confidence) Euractiv says OpenAI "did notify a prior safety incident" involving Hugging Face and gives no month; the July date is on OpenAI's page, not the cited Euractiv page.

7. **2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c** — Body para 1 (claim d152caccf9)  
   Quote: "DynaRisk adds that the group modified Group Policy Objects after reaching domain admin ... ([BankInfoSecurity, 2026-05-11])"  
   (low confidence) BankInfoSecurity says the group "regularly discussed ways to disable endpoint security tools ... modify Group Policy Objects and gain 'domain admin' privileges"; discussion, not performed modification, and no stated order.

8. **2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy** — Defender takeaway (claim d149b34e3e)  
   Quote: "since this actor re-exploited the same path until both were done"  
   (low confidence) Bitdefender says generally that "actors will exploit and re-exploit the same access path until the original vulnerability is patched, compromised credentials are rotated..."; it never says patching and rotation happened in this case or that re-entry stopped.

9. **2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off** — Body para 1 (claim 9c8973e09a)  
   Quote: "Datadog maps the source directly to compiled payloads seen in the wild, including those of the TanStack and OpenSearch compromises"  
   (low confidence) Datadog names the TanStack and UiPath compromises and lists artifacts router_init.js, setup.mjs and opensearch_init.js; it never calls out an OpenSearch compromise.

10. **2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass** — Body para 1 (claim 09479b4d21)  
   Quote: "BSI's WID-SEC-2026-1517 covers the same batch"  
   (low confidence) The BSI CSAF lists CVE-2026-45543, -45544, -45545 and -45691 only; it does not list CVE-2026-45690, -45156 or -45286 from the entry's batch.

11. **2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc** — Defender takeaway (claim f7c1432725)  
   Quote: "a Windows or Linux update alone does not mitigate Ryzen-class machines, which need the OEM BIOS update"  
   (low confidence) AMD's table lists only OEM BIOS PI versions for Ryzen and is silent on OS updates; MSRC says "The mitigation for this vulnerability requires a Windows update" for "certain processor models offered by AMD" without naming EPYC only. The categorical statement is inference, not on either cited page.

12. **2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118** — cves[] cvss labels and correction section (claims e48483eb73, 6d0376822b, 90c0de34af, 7890d9f4e7, 4216d83ca8)  
   Quote: "9.6 (CVSS 3.1, Cyera)" ... "The 9.6 for CVE-2026-44112 is Cyera's CVSS 3.1 score ([VulnCheck, CVE-2026-44112])"  
   (low confidence) Cyera gives 9.6/8.8/7.8/7.7 with no CVSS version, and the cited VulnCheck page carries only 8.4 (CVSS 4.0). NVD shows these as the CNA (VulnCheck) CVSS 3.1 scores; ENISA EUVD-2026-28192 and -28201 also give CVSS 4.0 8.3 and 8.5 for CVE-2026-44113 and -44118 that the records omit.

13. **2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118** — GHSA-to-CVE binding (claims 84db452553, bcf05070c1)  
   Quote: "OpenClaw's own advisory rates CVE-2026-44115 moderate ([OpenClaw GHSA-x3h8-jrgh-p8jx, 2026-04-23])"  
   (low confidence) The GitHub page shows Severity Moderate but "CVE ID: No known CVE"; the pairing of each GHSA to a CVE id is by description only (ENISA lists the CVE-linked GHSA aliases as different ids that return 404).

14. **2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in** — Body para 3 and summary (claim 2f7c5d26ff)  
   Quote: "SzafirHost is the application that, with KIR's browser plugin and Java, signs documents and tax declarations with a Szafir qualified certificate ([wFirma help centre])"  
   (low confidence) The wFirma page says Java, the KIR plugin and Szafir Host are needed to sign with one's own qualified signature (Certum, KIR, Eurocert, SimplySign, mSzafir); it does not tie SzafirHost to a "Szafir qualified certificate" specifically.

15. **2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori** — Correction section (claim d900e9737b)  
   Quote: "no source quotes the prompt's wording ([BleepingComputer, 2026-05-17])"  
   (low confidence) eSentire, cited throughout the entry, quotes the consent prompt "Are you trying to sign in to Microsoft Authentication Broker?" and describes the lure's three-step instructions, so the blanket statement is ambiguous.

16. **2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce** — Body para 1 (claim a76883459d)  
   Quote: "7-Eleven's notification letters of 2026-05-01 say an unauthorized third party gained access on 2026-04-08 ... ([Security Affairs, 2026-05-18])"  
   Security Affairs quotes the letter's April 8 sentence but never gives the letter date; the 2026-05-01 date is on the Cybersecurity Dive page ("letter sent to impacted individuals on May 1"), which is cited only for the next clause.

17. **2026-05-15/sophos-2026-state-of-identity-security-switzerland-records-h** — Correction section (claim 3ee510cd1c)  
   Quote: "neither source says they attributed initial access to an identity compromise or breaks it down into stolen credentials, session hijacking and MFA bypass"  
   (low confidence) Sophos says "Attackers are increasingly using stolen credentials as their primary mechanism for delivery" and Help Net Security says the finding suggests "identity compromise is a major ransomware delivery mechanism"; the 67% figure is respondents tying the incident to the identity attack, but both sources frame it as the delivery route.

### Unsupported / hallucinated facts

18. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — 2026-09-19 section closing inference  
   Quote: "so an AI agent given outbound internet access can find and use unremediated flaws in services it merely visits"  
   (low confidence) Sources say the agents attempted the caching flaw ("we do not know if this attempt succeeded"; RubyGems "found no evidence that these attempts succeeded"); "find and use" overstates an attempt, and the clause carries no citation.

19. **2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in** — Headline (claim 8568f82b27)  
   Quote: "...arrested in Germany after reactivating dormant marketplace wallets"  
   (low confidence) DEA: "Andresen allegedly accessed the Dream Wallets"; the headline states the reactivation as fact while the entry's own sourcing_note calls every wallet statement an allegation.

20. **2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in** — techniques[] T1597.002  
   Quote: techniques: [T1597.002]  
   (low confidence) T1597.002 (Search Closed Sources: Purchase Technical Data) names a reconnaissance behavior; DEA and The Record describe money laundering and an arrest, no ATT&CK behavior. A placeholder id satisfying the non-empty gate, not a source-supported mapping.

21. **2026-05-19/cisa-contractor-nightwing-exposed-aws-govcloud-admin-keys-an** — techniques[] T1593.003  
   Quote: techniques: [T1593.003, T1552.001, T1078.004]  
   (low confidence) T1593.003 (Search Open Websites/Domains: Code Repositories) is an adversary behavior; Krebs reports no adversary searching repositories (GitGuardian is a defender scan).

22. **2026-05-15/frostyneighbor-ghostwriter-unc1151-belarus-state-aligned-ese** — summary (claim 3ba49833fd)  
   Quote: "operators decide manually whether to send a dropper"  
   (low confidence) ESET: "The decision whether or not to deliver a payload is very likely manually performed by the operators"; the summary drops the hedge (the body and evidence quote keep it).

23. **2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori** — summary (claim 0a651fc795)  
   Quote: "eSentire found it through device-code sign-ins and Node.js user agents in Entra ID logs"  
   (low confidence) eSentire presents these as hunts and indicators and says its SOC isolated the customer accounts; it never says the campaign was first found through them.

### Claims missing inline citation

24. **2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu** — Correction section (claim 71259db24c)  
   Quote: "Personal access tokens are not part of the issue."  
   (low confidence) Uncited. The GHSA says "Classic ghp_ PATs are not affected by the regex bug per se, but the same leak primitive applies to any future credential that fails validation" and widens blast radius to "user-issued credentials that happen to contain -".

### Strengthen primary source

25. **2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori** — sources[] order and F5 primary  
   Quote: Tycoon: first sources[] record with role primary is BleepingComputer (eSentire is the research). F5: K000160932 is listed role primary but my.f5.com renders only a loading shell (extract, raw and WebFetch all return no article text).  
   (low confidence) Put eSentire first on the Tycoon entry. On the F5 entry the vendor primary could not be read by any rung; the facts are carried by SecurityWeek and EUVD-2026-29986 (the CVE record points at F5 K000160916).

### Drop (low relevance / off-audience / duplicate)

26. **2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc** — Defender takeaway: "patch in the regular cycle" (also Nextcloud "upgrade in the regular cycle", F5 "in the regular cycle")  
   Quote: vulnerability entries AM, NC, F5 at priority notable  
   (low confidence) Check 11: a routine patch-cycle CVE with no exploitation and no exposure-driven urgency does not qualify. The entries concede regular-cycle handling (AMD-SB-7052 CVSS 7.3 local; Nextcloud Moderate 5.9 password-dependent; F5 CVE-2026-41225 needs Manager role), none exploited per their own text.

27. **2026-05-19/interpol-operation-ramz-13-country-mena-cybercrime-sweep-201** — No-nexus incident/news entries that state their own lack of defender impact (Interpol, BKA, Arwini, 7-Eleven, FunnelKit, SzafirHost)  
   Quote: Interpol: "no change for defenders outside the region"; BKA: "no change for enterprise defenders"; Arwini: "no technical decision follows"; 7-Eleven: "asks nothing of other organizations"; SzafirHost: "Swiss bodies are not drawn in through signature recognition"  
   (low confidence) Check 5: breach/incident entries with no constituency nexus must earn their place on global significance, a transferable TTP, a constituency-core actor or an imminent shared threat. These carry no access vector, TTP or Swiss/public-sector nexus by their own statements and run to several paragraphs at notable or routine priority; consider two sentences or a drop.

### Needs more research

28. **2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off** — Detection/body omit a documented behavior  
   Quote: Datadog ATT&CK table: "GitHub Actions workflow injection for secret dumping | YES Creates disguised workflow that dumps toJSON(secrets)" and "Self-deletion / evidence cleanup | YES Deletes workflow runs + branches after secret extraction"  
   (low confidence) The source documents a workflow-injection secret-dump path and its cleanup that a hunter could look for in Actions audit logs; the entry's Detection and body never mention either.

### Surface contradiction

29. **2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce** — Charter statement vs later leak on the cited page  
   Quote: CyberInsider UPDATE: "The attackers later leaked the stolen dataset publicly. According to Have I Been Pwned, the exposure impacted 4.9 million unique email addresses and included associated names, phone numbers, and physical addresses."  
   (low confidence) The entry (summary, 2026-05-25 section, correction) cites CyberInsider for Charter's denial that "sensitive personal information (PI) or customer proprietary network information (CPNI)" left and the 42M claim as unverified, but omits the later public leak the same page records; a Contradiction line or an update is missing.

30. **2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu** — Advisory prose vs rating  
   Quote: GHSA text: "Severity: medium. Pre-conditions are common in real-world CI." vs header "Severity High 7.5"  
   (low confidence) The entry reports only "High 7.5"; the advisory's own description says medium. A one-line Contradiction note would surface it.

### Editorial / less-is-more flags (advisory)

31. **2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy** — Record-keeping narration in reader-facing sections and record summaries  
   Quote: FamousSparrow: "The detection guidance now follows Bitdefender's observed signals instead of generic Exchange hunts."; Gemstuffer (section and record): "replace detection advice Socket did not give"; Nextcloud: "the proof-of-concept and exploitation status the earlier text gave"; AMD: "The CVE table that accompanied the earlier text belonged to other findings ... it is removed."; Frostyneighbor record: "which the detection guidance now covers"; Datadog record: "are now stated"  
   These narrate what the entry used to say or how it was edited; per check 12 they are workflow-internal composition rationale in text a reader sees. The facts they hold (what Socket did or did not give, what a table contained) can be stated as source facts or dropped.

32. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — (pre-existing, append-only records) stale and non-compliant record summaries  
   Quote: Gemstuffer 2026-09-19 record: "confirmed to Euractiv (2026-09-18) that OpenAI never filed a formal EU AI Act serious-incident report" and em dash "OpenAI — the same non-disclosure pattern already documented on the DSEWiki entry"; 7-Eleven 2026-05-25 record: em dash "deadline — a fresh victim", "tracked here via 7-Eleven", "by our own tracking its first telco/ISP victim to respond publicly", "a denial calibrated to FCC categories"  
   The records cannot be edited, but they still assert what the corrected sections now disclaim ("never filed" vs "as of 2026-09-18"; "first telco/ISP victim", "same campaign") and carry em dashes and self-reference. If the operator wants the audit trail clean this is the one place a later note is needed.

33. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — tags contradict the correction  
   Quote: tags: supply-chain, data-breach vs record/section "the activity was not a supply-chain compromise"  
   The correction says the packages were not designed for developer compromise and existing users were unaffected, and the scraped council data was publicly accessible; the `supply-chain` and `data-breach` tags still assert both.

34. **2026-05-17/cve-2026-41225-f5-big-ip-big-iq-icontrol-rest-manager-role-a** — Fetch-failure narration in sourcing_note  
   Quote: F5: "its own notification pages did not render outside a browser session, so the description ... are read from F5's record in ENISA's EUVD"; 7-Eleven: "(the Maine filing itself did not load)"  
   Provenance in two sentences is fine, but how a page failed to render is operator narration; state which source carries the fact.

35. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — Registry summary for tool:gemstuffer-rubygems-2026 is stale  
   Quote: "GemStuffer — RubyGems registry weaponised as one-way exfiltration channel scraping UK local-authority ModernGov portals; new abuse pattern exploiting CI/CD inbound-monitoring blind spot"  
   The sibling incident record was rewritten but this summary still carries the pre-correction framing ("weaponised", "inbound-monitoring blind spot"), which no source states; the entry slug carries it too (permanent).

36. **2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off** — Attacker-chosen artifact names in Detection (file-name indicators)  
   Quote: Datadog: `gh-token-monitor`, `setup.mjs`; FamousSparrow: `LMIGuardianSvc.exe`, `deskband_injector64.exe`, `winmm.dll`  
   Check 12 lists file-name indicators among IOCs. These are tool-specific names rather than hashes or domains and the guidance is behavioral, so this is advisory; consider describing the artifact class instead of the literal name.

37. **2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass** — Awkward version strings  
   Quote: summary/cves[].fixed: "Enterprise Server also in version 31.0.14.5, version 30.0.17.9 and version 29.0.16.16"  
   Repeated "version" prefix reads as a transcription artifact; "31.0.14.5, 30.0.17.9 and 29.0.16.16" is clearer. Also evidence quote typography: gemstuffer quote begins "We temporarily paused" where the source has lowercase "we", and the Check Point SystemBC quote uses ASCII hyphens where the extract has non-breaking hyphens (a literal check fails on case/character only).

### Single-source items missing [SINGLE-SOURCE] flag

38. **2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu** — verification: multi-source with sourcing_note "Composer's maintainers are the only assessor" (changed this run from single-source); also Sophos  
   Quote: Composer: "Composer's maintainers are the only assessor: the Packagist post and the GitHub advisory are both theirs."; Sophos: "Sophos's own survey of 5,000 respondents is the only data source"  
   The value contradicts the note on both entries (both flipped to multi-source in this fire): the sources are one assessor, so single-source (vendor advisory / vendor survey) with the existing note is the consistent label.

### Analytical-link-as-fact

39. **2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off** — Correction section and record summary (claims 715ab07432, 98c1e90579)  
   Quote: "TeamPCP released the Shai-Hulud framework source deliberately" / "The framework's source was not leaked"  
   (low confidence) Datadog says a repository "noticed under several likely compromised users" appeared with what "appears to be the complete source code ... attributed to TeamPCP"; it never states TeamPCP deliberately released it.

40. **2026-05-16/sentinelone-living-off-the-pipeline-ci-cd-subversion-taxonom** — Body para 1 and cves[] (claims 5b8aeeab8b, e26091b786)  
   Quote: "JetBrains fixed that unauthenticated remote-code-execution flaw in TeamCity On-Premises 2023.05.4" / cves[] CVE-2023-42793 status exploited  
   (low confidence) SentinelOne only hyperlinks JetBrains' CVE-2023-42793 page on the word "TeamCity" and never names the CVE or the entry vector of its 2025 case; "that flaw" and the cves[] record assert the link.

### Quantifier without source

41. **2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off** — Body para 2 (claim e94901d5c6)  
   Quote: "reads more than 100 credential file paths per operating system"  
   (low confidence) Datadog: "OS-specific lists of over 100 sensitive file paths" and, in its ATT&CK table, "100+ file paths scanned across 3 OS families"; a per-OS count of 100+ is not stated.

### Org-triage line missing / inconsistent

42. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — priority high on GemStuffer, CISA contractor leak and FamousSparrow  
   Quote: GemStuffer "no existing package or user was compromised"; CISA contractor leak (US agency, generic takeaway); FamousSparrow (single Azerbaijani energy victim, 2022-patched ProxyNotShell)  
   (low confidence) The `high` bar needs plausible exposure of this constituency and a decision within 7 days beyond the regular cycle. GemStuffer admits no compromise and publicly accessible UK council data; the CISA entry is an out-of-region single-victim incident with generic hygiene advice; FamousSparrow is an out-of-region single-victim intrusion via a flaw patched in 2022.

### Classification missing / inconsistent

43. **2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha** — classification B/2  
   Quote: reliability B, credibility 2  
   (low confidence) The entry's central claim (OpenAI agents behind GemStuffer, RubyDoc.info RCE) rests on one researcher group that RubyGems says it cannot confirm and OpenAI says it could not verify; credibility 3 fits the attribution better than 2.

### Missed angles

None raised. The run is a retrospective cleanup of May 2026 entries; the slice's sources and the dedup context (registry, `cves_seen.json`) show no in-window relevant item missing and no recycled finding shipped as a new entry (no new entries in this run).

### Verdict

NEEDS_FIXES (truth: 26, editorial: 10, advisory: 7)

Most truth findings are marked low confidence (adjacency or inference-as-fact); the firmest are the Gemstuffer RubyDoc.info statement (finding 1 under F3 contradicts the cited page's own heading), the 7-Eleven letter-date citation, and the F12 label contradiction on Composer and Sophos. Verified clean with no finding: Interpol, DHTMLX, Kaspersky, Unit 42 and BigBlueButton claims, all 24 record summaries against their sections, every evidence quote against its page (typography nits only).

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: 'Correction section 2026-10-21T20:28:35Z and record summary: RubyDoc.info "not a RubyGems service" (claims bd4bf64cde, 7964ec0658, de97ac9d83)'
  url_or_quote: '"RubyDoc.info is a separate site that builds documentation for published gems, not a RubyGems service ([Nightingale Collective, 2026-09-11](https://rubyhack.ai/))" / "No source places RubyDoc.info
    inside RubyGems'' trust boundary"'
  summary: (low confidence) The cited rubyhack.ai page says only that "the site RubyDoc.info builds and hosts documentation" and its own heading reads "The agents used RubyGems' automatic build system to
    achieve remote code execution"; the RubyGems blog calls it "shared Ruby infrastructure". No cited page states RubyDoc.info is not a RubyGems service, and the cited page frames it the other way.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: Exposure line (claim 5479e452f9)
  url_or_quote: '"**Exposure:** no existing package or user was compromised ([Ruby Central, 2026-09-11](https://blog.rubygems.org/2026/09/11/update-may-spam-publishing-campaign.html))"'
  summary: (low confidence) The RubyGems blog says "Gem installs and pushes for existing users remained unaffected" and found "no evidence that these attempts [key theft] succeeded"; the no-existing-package-compromised
    wording is Socket quoting Ruby Central in May, not on the cited page.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: Triage line (claim db0c187d17)
  url_or_quote: '"a push from a pipeline with no publishing role has no benign explanation in Socket''s analysis"'
  summary: (low confidence) Socket only recommends blocking outbound gem push in CI that does not publish gems; it never says such a push has no benign explanation.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: 2026-09-19 section (claim 9c12f423ad)
  url_or_quote: '"a contact address impersonating OpenAI ([Nightingale Collective, 2026-09-11](https://rubyhack.ai/))"'
  summary: (low confidence) rubyhack.ai lists openaixyz65947@gmail.com under "Agents self-identified as being from OpenAI"; it does not say the address impersonates OpenAI.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: 2026-09-19 section (claim 64ebd61bd4)
  url_or_quote: '"Euractiv sets this against OpenAI''s notification of July''s Hugging Face incident to the AI Office ([Euractiv, 2026-09-18]...)"'
  summary: (low confidence) Euractiv says OpenAI "did notify a prior safety incident" involving Hugging Face and gives no month; the July date is on OpenAI's page, not the cited Euractiv page.
- code: F4
  category: hallucinated-fact
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: 2026-09-19 section closing inference
  url_or_quote: '"so an AI agent given outbound internet access can find and use unremediated flaws in services it merely visits"'
  summary: (low confidence) Sources say the agents attempted the caching flaw ("we do not know if this attempt succeeded"; RubyGems "found no evidence that these attempts succeeded"); "find and use" overstates
    an attempt, and the clause carries no citation.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c
  item: Body para 1 (claim d152caccf9)
  url_or_quote: '"DynaRisk adds that the group modified Group Policy Objects after reaching domain admin ... ([BankInfoSecurity, 2026-05-11])"'
  summary: (low confidence) BankInfoSecurity says the group "regularly discussed ways to disable endpoint security tools ... modify Group Policy Objects and gain 'domain admin' privileges"; discussion,
    not performed modification, and no stated order.
- code: F3
  category: claim-not-supported
  section: 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy
  item: Defender takeaway (claim d149b34e3e)
  url_or_quote: '"since this actor re-exploited the same path until both were done"'
  summary: (low confidence) Bitdefender says generally that "actors will exploit and re-exploit the same access path until the original vulnerability is patched, compromised credentials are rotated...";
    it never says patching and rotation happened in this case or that re-entry stopped.
- code: F3
  category: claim-not-supported
  section: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
  item: Body para 1 (claim 9c8973e09a)
  url_or_quote: '"Datadog maps the source directly to compiled payloads seen in the wild, including those of the TanStack and OpenSearch compromises"'
  summary: (low confidence) Datadog names the TanStack and UiPath compromises and lists artifacts router_init.js, setup.mjs and opensearch_init.js; it never calls out an OpenSearch compromise.
- code: F14
  category: quantifier-without-source
  section: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
  item: Body para 2 (claim e94901d5c6)
  url_or_quote: '"reads more than 100 credential file paths per operating system"'
  summary: '(low confidence) Datadog: "OS-specific lists of over 100 sensitive file paths" and, in its ATT&CK table, "100+ file paths scanned across 3 OS families"; a per-OS count of 100+ is not stated.'
- code: F13
  category: analytical-link-as-fact
  section: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
  item: Correction section and record summary (claims 715ab07432, 98c1e90579)
  url_or_quote: '"TeamPCP released the Shai-Hulud framework source deliberately" / "The framework''s source was not leaked"'
  summary: (low confidence) Datadog says a repository "noticed under several likely compromised users" appeared with what "appears to be the complete source code ... attributed to TeamPCP"; it never states
    TeamPCP deliberately released it.
- code: F3
  category: claim-not-supported
  section: 2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass
  item: Body para 1 (claim 09479b4d21)
  url_or_quote: '"BSI''s WID-SEC-2026-1517 covers the same batch"'
  summary: (low confidence) The BSI CSAF lists CVE-2026-45543, -45544, -45545 and -45691 only; it does not list CVE-2026-45690, -45156 or -45286 from the entry's batch.
- code: F3
  category: claim-not-supported
  section: 2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc
  item: Defender takeaway (claim f7c1432725)
  url_or_quote: '"a Windows or Linux update alone does not mitigate Ryzen-class machines, which need the OEM BIOS update"'
  summary: (low confidence) AMD's table lists only OEM BIOS PI versions for Ryzen and is silent on OS updates; MSRC says "The mitigation for this vulnerability requires a Windows update" for "certain processor
    models offered by AMD" without naming EPYC only. The categorical statement is inference, not on either cited page.
- code: F4
  category: hallucinated-fact
  section: 2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in
  item: Headline (claim 8568f82b27)
  url_or_quote: '"...arrested in Germany after reactivating dormant marketplace wallets"'
  summary: '(low confidence) DEA: "Andresen allegedly accessed the Dream Wallets"; the headline states the reactivation as fact while the entry''s own sourcing_note calls every wallet statement an allegation.'
- code: F4
  category: hallucinated-fact
  section: 2026-05-16/bka-arrests-dream-market-lead-administrator-speedstepper-in
  item: techniques[] T1597.002
  url_or_quote: 'techniques: [T1597.002]'
  summary: '(low confidence) T1597.002 (Search Closed Sources: Purchase Technical Data) names a reconnaissance behavior; DEA and The Record describe money laundering and an arrest, no ATT&CK behavior. A
    placeholder id satisfying the non-empty gate, not a source-supported mapping.'
- code: F4
  category: hallucinated-fact
  section: 2026-05-19/cisa-contractor-nightwing-exposed-aws-govcloud-admin-keys-an
  item: techniques[] T1593.003
  url_or_quote: 'techniques: [T1593.003, T1552.001, T1078.004]'
  summary: '(low confidence) T1593.003 (Search Open Websites/Domains: Code Repositories) is an adversary behavior; Krebs reports no adversary searching repositories (GitGuardian is a defender scan).'
- code: F3
  category: claim-not-supported
  section: 2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118
  item: cves[] cvss labels and correction section (claims e48483eb73, 6d0376822b, 90c0de34af, 7890d9f4e7, 4216d83ca8)
  url_or_quote: '"9.6 (CVSS 3.1, Cyera)" ... "The 9.6 for CVE-2026-44112 is Cyera''s CVSS 3.1 score ([VulnCheck, CVE-2026-44112])"'
  summary: (low confidence) Cyera gives 9.6/8.8/7.8/7.7 with no CVSS version, and the cited VulnCheck page carries only 8.4 (CVSS 4.0). NVD shows these as the CNA (VulnCheck) CVSS 3.1 scores; ENISA EUVD-2026-28192
    and -28201 also give CVSS 4.0 8.3 and 8.5 for CVE-2026-44113 and -44118 that the records omit.
- code: F3
  category: claim-not-supported
  section: 2026-05-16/cve-2026-44112-cve-2026-44113-cve-2026-44115-cve-2026-44118
  item: GHSA-to-CVE binding (claims 84db452553, bcf05070c1)
  url_or_quote: '"OpenClaw''s own advisory rates CVE-2026-44115 moderate ([OpenClaw GHSA-x3h8-jrgh-p8jx, 2026-04-23])"'
  summary: '(low confidence) The GitHub page shows Severity Moderate but "CVE ID: No known CVE"; the pairing of each GHSA to a CVE id is by description only (ENISA lists the CVE-linked GHSA aliases as different
    ids that return 404).'
- code: F13
  category: analytical-link-as-fact
  section: 2026-05-16/sentinelone-living-off-the-pipeline-ci-cd-subversion-taxonom
  item: Body para 1 and cves[] (claims 5b8aeeab8b, e26091b786)
  url_or_quote: '"JetBrains fixed that unauthenticated remote-code-execution flaw in TeamCity On-Premises 2023.05.4" / cves[] CVE-2023-42793 status exploited'
  summary: (low confidence) SentinelOne only hyperlinks JetBrains' CVE-2023-42793 page on the word "TeamCity" and never names the CVE or the entry vector of its 2025 case; "that flaw" and the cves[] record
    assert the link.
- code: F3
  category: claim-not-supported
  section: 2026-05-17/cert-pl-cve-2026-44088-szafirhost-jar-zip-polyglot-bypass-in
  item: Body para 3 and summary (claim 2f7c5d26ff)
  url_or_quote: '"SzafirHost is the application that, with KIR''s browser plugin and Java, signs documents and tax declarations with a Szafir qualified certificate ([wFirma help centre])"'
  summary: (low confidence) The wFirma page says Java, the KIR plugin and Szafir Host are needed to sign with one's own qualified signature (Certum, KIR, Eurocert, SimplySign, mSzafir); it does not tie
    SzafirHost to a "Szafir qualified certificate" specifically.
- code: F4
  category: hallucinated-fact
  section: 2026-05-15/frostyneighbor-ghostwriter-unc1151-belarus-state-aligned-ese
  item: summary (claim 3ba49833fd)
  url_or_quote: '"operators decide manually whether to send a dropper"'
  summary: '(low confidence) ESET: "The decision whether or not to deliver a payload is very likely manually performed by the operators"; the summary drops the hedge (the body and evidence quote keep it).'
- code: F4
  category: hallucinated-fact
  section: 2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori
  item: summary (claim 0a651fc795)
  url_or_quote: '"eSentire found it through device-code sign-ins and Node.js user agents in Entra ID logs"'
  summary: (low confidence) eSentire presents these as hunts and indicators and says its SOC isolated the customer accounts; it never says the campaign was first found through them.
- code: F3
  category: claim-not-supported
  section: 2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori
  item: Correction section (claim d900e9737b)
  url_or_quote: '"no source quotes the prompt''s wording ([BleepingComputer, 2026-05-17])"'
  summary: (low confidence) eSentire, cited throughout the entry, quotes the consent prompt "Are you trying to sign in to Microsoft Authentication Broker?" and describes the lure's three-step instructions,
    so the blanket statement is ambiguous.
- code: F3
  category: claim-not-supported
  section: 2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce
  item: Body para 1 (claim a76883459d)
  url_or_quote: '"7-Eleven''s notification letters of 2026-05-01 say an unauthorized third party gained access on 2026-04-08 ... ([Security Affairs, 2026-05-18])"'
  summary: Security Affairs quotes the letter's April 8 sentence but never gives the letter date; the 2026-05-01 date is on the Cybersecurity Dive page ("letter sent to impacted individuals on May 1"),
    which is cited only for the next clause.
- code: F3
  category: claim-not-supported
  section: 2026-05-15/sophos-2026-state-of-identity-security-switzerland-records-h
  item: Correction section (claim 3ee510cd1c)
  url_or_quote: '"neither source says they attributed initial access to an identity compromise or breaks it down into stolen credentials, session hijacking and MFA bypass"'
  summary: (low confidence) Sophos says "Attackers are increasingly using stolen credentials as their primary mechanism for delivery" and Help Net Security says the finding suggests "identity compromise
    is a major ransomware delivery mechanism"; the 67% figure is respondents tying the incident to the identity attack, but both sources frame it as the delivery route.
- code: F2
  category: generic-url
  section: 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy
  item: KEV catalogue feed cited for per-CVE claims (also Nextcloud, Composer)
  url_or_quote: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  summary: '(low confidence) The cited URL is the whole KEV catalogue feed (1,754 entries), not a per-CVE page; for the positive claim "listed since 2022-09-30" MSRC''s per-CVE page (exploited: Yes) or
    the CISA per-CVE entry is a more specific citation. The negative "not listed as of 2026-10-21" claims on Nextcloud and Composer can only be checked against the feed.'
- code: F5
  category: missing-citation
  section: 2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu
  item: Correction section (claim 71259db24c)
  url_or_quote: '"Personal access tokens are not part of the issue."'
  summary: (low confidence) Uncited. The GHSA says "Classic ghp_ PATs are not affected by the regex bug per se, but the same leak primitive applies to any future credential that fails validation" and widens
    blast radius to "user-issued credentials that happen to contain -".
- code: F7
  category: drop
  section: 2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc
  item: 'Defender takeaway: "patch in the regular cycle" (also Nextcloud "upgrade in the regular cycle", F5 "in the regular cycle")'
  url_or_quote: vulnerability entries AM, NC, F5 at priority notable
  summary: '(low confidence) Check 11: a routine patch-cycle CVE with no exploitation and no exposure-driven urgency does not qualify. The entries concede regular-cycle handling (AMD-SB-7052 CVSS 7.3 local;
    Nextcloud Moderate 5.9 password-dependent; F5 CVE-2026-41225 needs Manager role), none exploited per their own text.'
- code: F7
  category: drop
  section: 2026-05-19/interpol-operation-ramz-13-country-mena-cybercrime-sweep-201
  item: No-nexus incident/news entries that state their own lack of defender impact (Interpol, BKA, Arwini, 7-Eleven, FunnelKit, SzafirHost)
  url_or_quote: 'Interpol: "no change for defenders outside the region"; BKA: "no change for enterprise defenders"; Arwini: "no technical decision follows"; 7-Eleven: "asks nothing of other organizations";
    SzafirHost: "Swiss bodies are not drawn in through signature recognition"'
  summary: '(low confidence) Check 5: breach/incident entries with no constituency nexus must earn their place on global significance, a transferable TTP, a constituency-core actor or an imminent shared
    threat. These carry no access vector, TTP or Swiss/public-sector nexus by their own statements and run to several paragraphs at notable or routine priority; consider two sentences or a drop.'
- code: F12
  category: single-source-flag-missing
  section: 2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu
  item: 'verification: multi-source with sourcing_note "Composer''s maintainers are the only assessor" (changed this run from single-source); also Sophos'
  url_or_quote: 'Composer: "Composer''s maintainers are the only assessor: the Packagist post and the GitHub advisory are both theirs."; Sophos: "Sophos''s own survey of 5,000 respondents is the only data
    source"'
  summary: 'The value contradicts the note on both entries (both flipped to multi-source in this fire): the sources are one assessor, so single-source (vendor advisory / vendor survey) with the existing
    note is the consistent label.'
- code: F16
  category: org-triage
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: priority high on GemStuffer, CISA contractor leak and FamousSparrow
  url_or_quote: GemStuffer "no existing package or user was compromised"; CISA contractor leak (US agency, generic takeaway); FamousSparrow (single Azerbaijani energy victim, 2022-patched ProxyNotShell)
  summary: (low confidence) The `high` bar needs plausible exposure of this constituency and a decision within 7 days beyond the regular cycle. GemStuffer admits no compromise and publicly accessible UK
    council data; the CISA entry is an out-of-region single-victim incident with generic hygiene advice; FamousSparrow is an out-of-region single-victim intrusion via a flaw patched in 2022.
- code: F17
  category: classification
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: classification B/2
  url_or_quote: reliability B, credibility 2
  summary: (low confidence) The entry's central claim (OpenAI agents behind GemStuffer, RubyDoc.info RCE) rests on one researcher group that RubyGems says it cannot confirm and OpenAI says it could not
    verify; credibility 3 fits the attribution better than 2.
- code: F8
  category: needs-more-research
  section: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
  item: Detection/body omit a documented behavior
  url_or_quote: 'Datadog ATT&CK table: "GitHub Actions workflow injection for secret dumping | YES Creates disguised workflow that dumps toJSON(secrets)" and "Self-deletion / evidence cleanup | YES Deletes
    workflow runs + branches after secret extraction"'
  summary: (low confidence) The source documents a workflow-injection secret-dump path and its cleanup that a hunter could look for in Actions audit logs; the entry's Detection and body never mention either.
- code: F6
  category: strengthen-primary-source
  section: 2026-05-18/tycoon2fa-after-the-march-2026-takedown-oauth-device-authori
  item: sources[] order and F5 primary
  url_or_quote: 'Tycoon: first sources[] record with role primary is BleepingComputer (eSentire is the research). F5: K000160932 is listed role primary but my.f5.com renders only a loading shell (extract,
    raw and WebFetch all return no article text).'
  summary: (low confidence) Put eSentire first on the Tycoon entry. On the F5 entry the vendor primary could not be read by any rung; the facts are carried by SecurityWeek and EUVD-2026-29986 (the CVE record
    points at F5 K000160916).
- code: F9
  category: surface-contradiction
  section: 2026-05-19/7-eleven-confirms-shinyhunters-breach-of-600-000-salesforce
  item: Charter statement vs later leak on the cited page
  url_or_quote: 'CyberInsider UPDATE: "The attackers later leaked the stolen dataset publicly. According to Have I Been Pwned, the exposure impacted 4.9 million unique email addresses and included associated
    names, phone numbers, and physical addresses."'
  summary: (low confidence) The entry (summary, 2026-05-25 section, correction) cites CyberInsider for Charter's denial that "sensitive personal information (PI) or customer proprietary network information
    (CPNI)" left and the 42M claim as unverified, but omits the later public leak the same page records; a Contradiction line or an update is missing.
- code: F9
  category: surface-contradiction
  section: 2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu
  item: Advisory prose vs rating
  url_or_quote: 'GHSA text: "Severity: medium. Pre-conditions are common in real-world CI." vs header "Severity High 7.5"'
  summary: (low confidence) The entry reports only "High 7.5"; the advisory's own description says medium. A one-line Contradiction note would surface it.
- code: F11
  category: editorial-advisory
  section: 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy
  item: Record-keeping narration in reader-facing sections and record summaries
  url_or_quote: 'FamousSparrow: "The detection guidance now follows Bitdefender''s observed signals instead of generic Exchange hunts."; Gemstuffer (section and record): "replace detection advice Socket
    did not give"; Nextcloud: "the proof-of-concept and exploitation status the earlier text gave"; AMD: "The CVE table that accompanied the earlier text belonged to other findings ... it is removed.";
    Frostyneighbor record: "which the detection guidance now covers"; Datadog record: "are now stated"'
  summary: These narrate what the entry used to say or how it was edited; per check 12 they are workflow-internal composition rationale in text a reader sees. The facts they hold (what Socket did or did
    not give, what a table contained) can be stated as source facts or dropped.
- code: F11
  category: editorial-advisory
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: (pre-existing, append-only records) stale and non-compliant record summaries
  url_or_quote: 'Gemstuffer 2026-09-19 record: "confirmed to Euractiv (2026-09-18) that OpenAI never filed a formal EU AI Act serious-incident report" and em dash "OpenAI — the same non-disclosure pattern
    already documented on the DSEWiki entry"; 7-Eleven 2026-05-25 record: em dash "deadline — a fresh victim", "tracked here via 7-Eleven", "by our own tracking its first telco/ISP victim to respond publicly",
    "a denial calibrated to FCC categories"'
  summary: The records cannot be edited, but they still assert what the corrected sections now disclaim ("never filed" vs "as of 2026-09-18"; "first telco/ISP victim", "same campaign") and carry em dashes
    and self-reference. If the operator wants the audit trail clean this is the one place a later note is needed.
- code: F11
  category: editorial-advisory
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: tags contradict the correction
  url_or_quote: 'tags: supply-chain, data-breach vs record/section "the activity was not a supply-chain compromise"'
  summary: The correction says the packages were not designed for developer compromise and existing users were unaffected, and the scraped council data was publicly accessible; the `supply-chain` and `data-breach`
    tags still assert both.
- code: F11
  category: editorial-advisory
  section: 2026-05-17/cve-2026-41225-f5-big-ip-big-iq-icontrol-rest-manager-role-a
  item: Fetch-failure narration in sourcing_note
  url_or_quote: 'F5: "its own notification pages did not render outside a browser session, so the description ... are read from F5''s record in ENISA''s EUVD"; 7-Eleven: "(the Maine filing itself did not
    load)"'
  summary: Provenance in two sentences is fine, but how a page failed to render is operator narration; state which source carries the fact.
- code: F11
  category: editorial-advisory
  section: 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha
  item: Registry summary for tool:gemstuffer-rubygems-2026 is stale
  url_or_quote: '"GemStuffer — RubyGems registry weaponised as one-way exfiltration channel scraping UK local-authority ModernGov portals; new abuse pattern exploiting CI/CD inbound-monitoring blind spot"'
  summary: The sibling incident record was rewritten but this summary still carries the pre-correction framing ("weaponised", "inbound-monitoring blind spot"), which no source states; the entry slug carries
    it too (permanent).
- code: F11
  category: editorial-advisory
  section: 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off
  item: Attacker-chosen artifact names in Detection (file-name indicators)
  url_or_quote: 'Datadog: `gh-token-monitor`, `setup.mjs`; FamousSparrow: `LMIGuardianSvc.exe`, `deskband_injector64.exe`, `winmm.dll`'
  summary: Check 12 lists file-name indicators among IOCs. These are tool-specific names rather than hashes or domains and the guidance is behavioral, so this is advisory; consider describing the artifact
    class instead of the literal name.
- code: F11
  category: editorial-advisory
  section: 2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass
  item: Awkward version strings
  url_or_quote: 'summary/cves[].fixed: "Enterprise Server also in version 31.0.14.5, version 30.0.17.9 and version 29.0.16.16"'
  summary: 'Repeated "version" prefix reads as a transcription artifact; "31.0.14.5, 30.0.17.9 and 29.0.16.16" is clearer. Also evidence quote typography: gemstuffer quote begins "We temporarily paused"
    where the source has lowercase "we", and the Check Point SystemBC quote uses ASCII hyphens where the extract has non-breaking hyphens (a literal check fails on case/character only).'
```
