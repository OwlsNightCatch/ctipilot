**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-09T03:50:46Z · ended_at=2026-10-09T04:10:21Z · duration_seconds=1175

## Verification report — 2026-10-09T0255Z-intel (iteration 1)

Scope covered: all 168 ledger claims (verdict rows in `verification.iter1.claims.yaml`; `claim_ledger.py --coverage 1`: 168/168 answered), 5 new entries, 3 updated entries (with `git diff HEAD`), run record, registry additions. Primary pages fetched this iteration: Citrix CTX697191 / CTX697174 / CTX697096, the Citrix Tech Zone RSS feed (full text of the 107406, 88779 and SAML-guidance blogs), AA26-281A PDF (pdf recipe, whitespace-normalised), CISA KEV feed (cisa-kev bridge), DOJ and NCSC UK pages, admin.ch / PK Softech / watson / Inside IT / Netzwoche (German originals checked literally), Talos, ESET, ReliaQuest, SentinelLabs, Zscaler, ACSC (both URL forms), CISA 2026-10-04 alert (WebFetch), BleepingComputer, watchTowr FAQ and Labs, CERT-EU, NCSC-NL, CERT.at, NCSC-CH hub post 13005, GTIG, Unit 42, Tenable, Cyber Press, heise, Apache S2-032. Translated quotes (3 Publica evidence records): originals are verbatim on the pages, translations faithful. AA26-281A PDF text decoded 72/114 streams; the claims checked sit in the decoded text.

### Broken / unreachable URLs
- #1 (F1) `2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited`: the ACSC link in `sources[]` and the body (`.../about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products`) returns upstream HTTP 404 on repeated direct fetches (other old-style cyber.gov.au paths still resolve to `/alert/...`). The page exists at `https://www.cyber.gov.au/alert/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products` (fetched this iteration; "Recent update 3 October 2026": "may induce system crashes, denial of service and potential exploitation" and "ASD's ACSC is aware of impacts to Australian organisations"). Replace the URL; the quoted claim itself holds.

### Citation does not support the claim
- #2 (F3) AA26-281A entry, Detection and Triage: "a SoftEther client presented as conhost.exe, dllhost.exe or DiagTrack"; "conhost.exe, dllhost.exe and DiagTrack are legitimate Windows names ... separate a downloaded SoftEther client from the system binary". The advisory names only "conhost.exe or dllhost.exe" for the SoftEther installers; DiagTrack.exe is the process started by the XSS-delivered `live700_v1.exe` (mailbox-targeting malware with its own C2). Remove DiagTrack from the SoftEther clauses or give it its own clause.
- #3 (F3, low confidence) TraderTraitor entry, Defender takeaway: the single Zscaler citation ends a sentence that chains SentinelLabs-only lockfile-redirect advice with Zscaler's provider-binary advice; Zscaler carries only "restrict the use of untrusted Terraform providers, verify provider checksums". Cite the lockfile clause to SentinelLabs or split the sentence.

### Unsupported / hallucinated facts
- #4 (F4) TraderTraitor entry (summary, sourcing_note, Update section): "which it links to TraderTraitor with moderate confidence" / "moderate, not high, confidence". Zscaler never says "moderate": it titles the post "Suspected TraderTraitor Group ..." and says it "has not identified unique code similarities, shared infrastructure, or cryptographic links sufficient to independently attribute this campaign to TraderTraitor with high confidence" while noting "substantial overlap in tactics and targeting". Re-word to that.
- #5 (F4, low confidence) AA26-281A entry `cves[CVE-2014-6278].affected`: "GNU Bash through 4.3 before patch bash43-026". Appendix B reads "Through 4.3 bash43-026" (affected through patch level 026); the KEV notes link bash43-027, which the entry gives as the fix. "Before 026" excludes the vulnerable patch 026 and contradicts the entry's own `fixed`.
- #6 (F4, low confidence) ReliaQuest entry (summary, Exposure, sourcing_note): "ReliaQuest names no product, victim, sector or region"; "ReliaQuest names no product or vendor". The post names Apache Tomcat, Spring Batch, SQL Server, PrintSpoofer and GodPotato (three are in `affected_products[]`); only the exposed application's vendor is unnamed.

### Strengthen primary source
- none.

### Drop (low relevance / off-audience / duplicate)
- #7 (F7) `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow`: incident floor. `prompts/cti-run.md` ("The incident floor"): an incident whose sources give no access vector, no actor and no behaviour beyond the impact "is `routine` and at most two sentences plus its transfer ground, or it is dropped"; check 5b flags F7 when longer or higher. The run-record notes themselves say "kept at `notable` because no vector, actor or behaviour is public", the sourcing_note says "No source names an access vector, an actor or a ransom demand", and the backlog row for Beyond Gravity (2026-10-06) was held under this same floor. The entry is `notable` with a ~550-word body. The home-region supplier nexus and the identity-proofing takeaway are real, so keep the item, but cut it to `routine` and two sentences plus transfer ground and takeaway, or state in the run record why the floor does not apply.

### Claims missing inline citation
- #8 (F5, low confidence) AA26-281A entry, paragraph 2: four sentences ("The chain starts with open-source scanners and MicroScan ...", "Initial access has mostly come since January 2021 ...", "The actors also spray and guess passwords with the EBurst tool ...", "Persistence is a SoftEther VPN client ...") carry no inline citation; only the paragraph's last sentence does, unlike the rest of the entry. All four are supported by the advisory.

### Needs more research
- #9 (F8) `2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow` (and the 88779 Update section, `sourcing_note`): "the bulletin states no exploitation status"; "The vendor's own bulletin is the only source ... the bulletin gives no exploitation status". Citrix's related blog (linked from the bulletin; text readable in the Tech Zone RSS feed or via extract then jina) states: "As of the publication of the bulletin, Citrix is not aware of any unmitigated exploits of this vulnerability." S1 already had it (findings.S1.yaml line 26); the entry dropped it because the permalink 403s on some transports. Cite it and correct the sourcing_note.
- #10 (F8, low confidence) AA26-281A `cves[CVE-2016-3081].fixed`: "not stated in AA26-281A or the CISA catalogue". The KEV notes link Apache S2-032, which states the fix (2.3.20.3, 2.3.24.3 or 2.3.28.1, or disable Dynamic Method Invocation); the entry uses the ONLYOFFICE changelog link for its `fixed` but leaves Struts (and the linked Strapi disclosure) unstated.

### Surface contradiction
- #11 (F9, low confidence) Talos entry: "the cheapest technique ... worked almost universally". Talos' own headline bullet says "inconsistently impactful ... the best techniques steered the outcome in the attacker's favor in about 35% of test runs" (net rate). The entry omits the 35% figure and its net-rate definition, so "almost universally" reads as near-total efficacy.

### Missed angles
- none. Coverage looks complete: the five KEV additions of 2026-10-08 are all carried in the AA26-281A entry; the other exploited items I found for the period (FortiMail CVE-2026-104286, Zammad, Apple CoreGraphics) and the NCSC-CH hub's recent posts (Atlassian, ILIAS) are covered by earlier entries or recorded borderline drops; the Inside IT Vaud/TheGentlemen item has an entry of 2026-10-08. No independent exploitation report of CVE-2026-107406 exists (web search, this iteration).

### Editorial / less-is-more flags (advisory)
- #12 (F11) TraderTraitor entry: em dashes in the Defender takeaway (rewritten this run) and the Triage line ("input — check ...", "signal — the discriminator").
- #13 (F11) 88779 update-record summary: "The upgrade action moved to the new flaw's entry and this entry keeps the signature bridge and the log-preservation step" narrates how `actions[]` was edited; the Update section says nothing about actions.
- #14 (F11) TraderTraitor `techniques[]`: Zscaler's table also maps T1059.006, T1082, T1057, T1083, T1518, T1518.001, T1217, T1071.001 and T1573.001, behaviours the new section describes; 14 of its 25 ids were added.
- #15 (F11) 107406 action writes "13.1-37.283"; Citrix's build string is "13.1.37.283" (the entry's own `fixed` and body use it).
- #16 (F11, low confidence) Publica `techniques: [T1199]`: no source says the attackers used the supplier's access to reach Publica or federal networks; keep only as the closest available id and say so in the run record.

### Single-source items missing [SINGLE-SOURCE] flag
- none (107406 `single-source`, ReliaQuest `single-source`, AA26-281A `single-source-national-cert`, all with sourcing_note).

### Analytical-link-as-fact
- none.

### Quantifier without source
- none beyond #4 (the unsourced "moderate").

### Name-collision unflagged
- #17 (F15) ReliaQuest entry: "a live, unauthenticated Cairn agent-orchestration dashboard". The store carries `tool:cairn-exploitation-engine` (Gambit's open-source autonomous exploitation harness "Cairn", entry `2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes`) and `tool:cairn-talos` (Talos' defender-side CAIRN, keyed on the Talos entry of this same run). The ReliaQuest entry uses the name for an attacker-side orchestrator with no disambiguation wording, no registry key and no `references[]` link; the run record concedes the link is undecided. Both descriptions (open-source harness that dispatches agents against a target and objective) fit one project. Confirm same-entity and link it (key + `references[]`), or add a one-clause disambiguation against the Gambit tool and Talos' CAIRN.

### Org-triage line missing / inconsistent
- #18 (F16) `2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow` `priority: high`. The `high` bar lists as disqualifiers "an unexploited flaw reachable only in a non-default configuration" and "Doubt resolves to `notable`". The flaw is unexploited (Citrix blog: "not aware of any unmitigated exploits"), needs a SAML SP/IdP configuration (CTX697191 precondition), is AC:H, and has no independent report; the sibling CVE-2026-88779's exploitation is context, not exposure evidence for this CVE. Calibrate to `notable` or record why a disqualifier does not apply.
- Org-triage / watchlist: none present on any entry (checked). Classification: every entry carries an Admiralty block; letters match the sources.json tiers, credibility numbers consistent with the corroboration shown.

### Classification missing / inconsistent
- none.

### Action-item discipline
- #19 (F18) 88779 entry `actions[]` after the update. The update removed this exploited, KEV-listed flaw's own task (search SAML SP/IdP configurations and upgrade to 14.1-73.41 / 13.1-64.28, including appliances already on .37 / .23) and the record summary says "The upgrade action moved to the new flaw's entry". The 107406 action covers identity providers and service providers below 14.1-73.37 only, so a service-provider-only appliance on 14.1-73.37 to .40, still affected by exploited CVE-2026-88779, is covered by no action. Conversely the 88771 `actions[0]` now repeats the identity-provider upgrade that the 107406 action carries (duplicate in the aggregated list). Correct the record summary and de-duplicate; no padding.

### Record-level and registry checks (no findings)
- Updated entries: records carry this run's id, `updated_at` equals `at` only for the two `update` records, the `improvement` on 88771 does not float, `fields` cover every changed frontmatter line in `git diff HEAD`, sections exist for all three, no silent edits.
- Registry additions: summaries match their cited sources; `overlaps-with` (not attribution) on Integrity Tech to Flax Typhoon is right; no alias duplicates in the store for the new actors.
- Run-record notes: KEV sweep (five additions, catalog 2026.10.08, none dated 2026-10-09), single-source dispositions, backlog dispositions and source-state changes agree with the files and my fetches.
- Evidence quotes: all new `evidence[]` quotes are contiguous on their pages (Talos, ESET, DOJ, NCSC UK, AA26-281A, Citrix, ReliaQuest, Zscaler, German originals for Publica).

### Verdict

NEEDS_FIXES (truth: 7, editorial: 7, advisory: 5)

Findings are listed in order of weight: #1 (broken ACSC URL), #9 + #18 (vendor exploitation statement omitted; `high` calibration), #2 (DiagTrack conflation), #4 ("moderate" confidence not in the source), #7 (incident floor), #17 (Cairn collision), #19 (action set) are the ones I would not ship. The remainder are low-confidence or advisory.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
- code: F1
  category: broken-url
  section: 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited
  item: "CVE-2026-88779 NetScaler entry: ACSC link in sources[] and body (claim d4a1afd069)"
  url_or_quote: "https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products"
  summary: "Cited ACSC path returns upstream HTTP 404 (python3 tools/fetch_source.py url --direct, repeated; other old-style cyber.gov.au paths still resolve). The alert lives at https://www.cyber.gov.au/alert/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products (fetched this iteration; 'Recent update 3 October 2026' carries 'may induce system crashes, denial of service and potential exploitation' and 'ASD's ACSC is aware of impacts to Australian organisations'). Replace the URL in sources[] and the body."
- code: F3
  category: claim-not-supported
  section: 2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft
  item: "Detection and Triage lines (claims b07af63b90, 48c00725ec)"
  url_or_quote: "a SoftEther client presented as conhost.exe, dllhost.exe or DiagTrack in process and service-installation telemetry; conhost.exe, dllhost.exe and DiagTrack are legitimate Windows names, so the file's path, signature and network behaviour separate a downloaded SoftEther client from the system binary"
  summary: "AA26-281A names only 'conhost.exe or dllhost.exe' for the SoftEther installers; DiagTrack.exe is the process started by the XSS-delivered executable live700_v1.exe (mailbox-targeting malware with its own C2), not a SoftEther client. Remove DiagTrack from the SoftEther detection/triage clauses or split it into its own XSS-payload clause."
- code: F3
  category: claim-not-supported
  section: 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
  item: "(low confidence) Defender takeaway, sentence ending in the Zscaler citation (claim e68d2908ff)"
  url_or_quote: "check the source registry a lockfile's providers resolve to before running `terraform init`, since a lockfile can silently redirect a trusted command to attacker infrastructure; a provider binary can also be trojanized itself, so restrict untrusted Terraform providers and verify provider checksums ([Zscaler ThreatLabz, 2026-10-08](...))"
  summary: "The single Zscaler citation terminates a sentence that chains SentinelLabs-only lockfile-redirect advice with Zscaler's provider-binary advice; Zscaler's page carries only the latter ('restrict the use of untrusted Terraform providers, verify provider checksums'). Cite the lockfile clause to SentinelLabs or split the sentence."
- code: F4
  category: hallucinated-fact
  section: 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
  item: "'moderate' confidence attributed to Zscaler: summary, sourcing_note and Update section (claims fc533608bc, e0caaee99b)"
  url_or_quote: "which it links to TraderTraitor with moderate confidence / links the campaign to TraderTraitor with moderate, not high, confidence / which it links to TraderTraitor with moderate rather than high confidence"
  summary: "Zscaler (https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver) never says 'moderate'; it titles the post 'Suspected TraderTraitor Group' and says it 'has not identified unique code similarities, shared infrastructure, or cryptographic links sufficient to independently attribute this campaign to TraderTraitor with high confidence' while noting 'substantial overlap in tactics and targeting'. Re-word to Zscaler's own framing (suspected; substantial overlap; not attributed with high confidence)."
- code: F4
  category: hallucinated-fact
  section: 2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft
  item: "(low confidence) cves[CVE-2014-6278].affected (claim 8906bda6ec)"
  url_or_quote: "GNU Bash through 4.3 before patch bash43-026"
  summary: "AA26-281A Appendix B lists 'GNU Bash | Through 4.3 bash43-026' (affected through patch level 026) and the CISA KEV notes link bash43-027, which the same record gives as the fix; 'before patch bash43-026' excludes the vulnerable patch 026 and contradicts the entry's own fixed: bash43-027. Use 'through 4.3 patch bash43-026'."
- code: F4
  category: hallucinated-fact
  section: 2026-10-09/reliaquest-llm-agents-spring-batch-tomcat-nashorn-system
  item: "(low confidence) summary, Exposure line and sourcing_note say no product is named (claims d5761e6af3, afbeb4b7ca)"
  url_or_quote: "ReliaQuest names no product, victim, sector or region; ReliaQuest names no product or vendor; no victim, product or region is named"
  summary: "The ReliaQuest post names Apache Tomcat, Spring Batch, Microsoft SQL Server, PrintSpoofer and GodPotato, and the entry lists three of them in affected_products[]; only the vulnerable application's vendor is unnamed. Say 'names no vendor or product for the exposed application' (and drop 'product' from the sourcing_note) so the absolute is true."
- code: F15
  category: name-collision-unflagged
  section: 2026-10-09/reliaquest-llm-agents-spring-batch-tomcat-nashorn-system
  item: "'Cairn' agent-orchestration dashboard reused without disambiguation"
  url_or_quote: "a live, unauthenticated Cairn agent-orchestration dashboard on the address that sent the opening requests"
  summary: "The store already carries tool:cairn-exploitation-engine (Gambit's open-source autonomous exploitation harness 'Cairn', entry 2026-09-23/gambit-ai-agent-retail-skimmer-campaign-strix-cairn-hermes) and tool:cairn-talos (Talos' defender-side CAIRN, keyed on the Talos entry shipped in this same run). The ReliaQuest entry names a third, possibly the same, 'Cairn' (attacker-side orchestration platform) with no 'no relation to / not to be confused with' wording, no registry key and no references[] link; the run record admits the link is undecided. Either confirm same-entity and link it (key + references[]), or add a one-clause disambiguation against both the Gambit tool and Talos' CAIRN."
- code: F8
  category: needs-more-research
  section: 2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow
  item: "Vendor's own exploitation statement omitted (also in the 88779 Update section and the sourcing_note)"
  url_or_quote: "the bulletin states no exploitation status; The bulletin does not say whether the flaw is exploited ... no independent report of exploitation or exploit code had surfaced as of 2026-10-09; The vendor's own bulletin is the only source ... the bulletin gives no exploitation status"
  summary: "The related Citrix blog that the bulletin links ('Protecting Customers: Immediate Guidance for CVE-2026-107406 ...', published 2026-10-08, readable via https://community.citrix.com/rss/3-citrix-tech-zone-blogs.xml/ or extract then jina) states: 'As of the publication of the bulletin, Citrix is not aware of any unmitigated exploits of this vulnerability.' S1's finding (findings.S1.yaml line 26) already carried it; the entry dropped it because the permalink 403s on some transports. The exploitation status is the most decision-relevant fact for the priority; cite the blog and state it, and correct the sourcing_note."
- code: F16
  category: org-triage
  section: 2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow
  item: "priority: high"
  url_or_quote: "priority: high"
  summary: "prompts/cti-run.md `high` disqualifiers include 'an unexploited flaw reachable only in a non-default configuration' and 'Doubt resolves to notable'. The flaw is unexploited (Citrix blog: 'not aware of any unmitigated exploits'), needs a SAML SP/IdP configuration (CTX697191 precondition), is AC:H, and no independent report exists. `high` fires notification hooks; the sibling flaw's exploitation is context, not exposure evidence for this CVE. Calibrate to `notable` or record why a disqualifier does not apply."
- code: F7
  category: drop
  section: 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow
  item: "Incident floor: notable priority and a ~550-word body"
  url_or_quote: "kept at `notable` because no vector, actor or behaviour is public (run-record notes); sourcing_note: No source names an access vector, an actor or a ransom demand"
  summary: "cti-run.md 'The incident floor': an incident whose sources give no access vector, no actor and no behaviour beyond the impact 'is `routine` and at most two sentences plus its transfer ground, or it is dropped'; 5b: F7 when longer or higher. The run record itself states the floor condition, and the backlog row for Beyond Gravity (2026-10-06) was held under the same floor. The home-region/supplier nexus is strong and the identity-proofing takeaway is a real decision, so keep it, but cut to routine and two sentences plus the takeaway, or document in the run record why the floor does not apply here."
- code: F5
  category: missing-citation
  section: 2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft
  item: "(low confidence) paragraph 2, four sentences without inline citation (claims 37ccd9eba3, 75c979ecaa, 80bbcf8705, 554af87121)"
  url_or_quote: "The chain starts with open-source scanners and MicroScan, more than 1,300 Python scripts ...; Initial access has mostly come since January 2021 ...; The actors also spray and guess passwords with the EBurst tool ...; Persistence is a SoftEther VPN client ..."
  summary: "All four are supported by AA26-281A (verified) but only the paragraph's last sentence carries a citation, unlike every other paragraph of the entry. Add the advisory citation to each sentence."
- code: F8
  category: needs-more-research
  section: 2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft
  item: "(low confidence) cves[CVE-2016-3081].fixed"
  url_or_quote: "not stated in AA26-281A or the CISA catalogue"
  summary: "The CISA KEV notes for CVE-2016-3081 link Apache's S2-032 bulletin, which states the fix ('upgrade to Apache Struts versions 2.3.20.3, 2.3.24.3 or 2.3.28.1' or disable Dynamic Method Invocation; fetched https://cwiki.apache.org/confluence/display/WW/S2-032). The entry treats the ONLYOFFICE changelog link as a source for the fixed field but leaves Struts (and the linked Strapi disclosure) as 'not stated'. Add the vendor fix/workaround."
- code: F18
  category: action-item-discipline
  section: 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited
  item: "actions[] after the update; record summary 'The upgrade action moved to the new flaw's entry'"
  url_or_quote: "Where the upgrade has to wait and NetScaler Console virtual patching is available, confirm with `show appfw signatures` ...; record: The upgrade action moved to the new flaw's entry and this entry keeps the signature bridge and the log-preservation step."
  summary: "The update deleted this KEV-listed, exploited flaw's own start-now task (find SAML SP/IdP matches and upgrade to 14.1-73.41/13.1-64.28 incl. appliances on .37/.23). The replacement in the CVE-2026-107406 entry covers identity providers and service providers below 14.1-73.37 only, so a service-provider-only appliance on 14.1-73.37 to .40 (still affected by exploited CVE-2026-88779) is covered by no action: 'moved' is inaccurate. Conversely the 88771 actions[0] now repeats the identity-provider upgrade that the 107406 action carries (duplicate in the aggregated list). Fix the record summary and de-duplicate; do not add padding."
- code: F9
  category: surface-contradiction
  section: 2026-10-09/talos-ai-analysis-evasion-instructions-aimed-at-llm-triage
  item: "(low confidence) efficacy of the evasion strings"
  url_or_quote: "the cheapest technique, a direct instruction to ignore the sample, worked almost universally, the more complex ones had little effect or backfired"
  summary: "Talos' own headline bullet says the technique is 'inconsistently impactful: the best techniques steered the outcome in the attacker's favor in about 35% of test runs' (net rate: pairs shifted toward benign minus toward malicious, over total pairs) while its Evaluation section says the cheapest technique 'worked almost universally'. The entry carries only the second and omits the 35% net-rate figure, so 'almost universally' reads as near-total efficacy; state both or the net-rate definition."
- code: F11
  category: editorial-advisory
  section: 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
  item: "em dashes in reader-facing text (lines edited this run)"
  url_or_quote: "should treat an unfamiliar or newly-cloned repository's lockfile as untrusted input — check the source registry ...; so the command itself is not the signal — the discriminator is ..."
  summary: "Rule: no em dash in reader-facing entry text (only the '## <Type> — <at>' heading is exempt). The Defender takeaway line was rewritten by this run's update and still carries one; the Triage line carries another."
- code: F11
  category: editorial-advisory
  section: 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited
  item: "update record summary narrates record-keeping"
  url_or_quote: "The upgrade action moved to the new flaw's entry and this entry keeps the signature bridge and the log-preservation step."
  summary: "updates[].summary is rendered; 'this entry keeps ...' narrates how actions[] was edited and the Update section says nothing about actions (4c(d): record summary states more than the section). Drop the sentence."
- code: F11
  category: editorial-advisory
  section: 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
  item: "techniques[] incomplete against the added source"
  url_or_quote: "techniques: ... T1560.001 (last id added)"
  summary: "Zscaler's ATT&CK table also maps T1059.006, T1082, T1057, T1083, T1518, T1518.001, T1217, T1071.001 and T1573.001 (Python stealer, discovery, web-protocol and AES C2), all behaviours the update section describes; 14 of its 25 ids were added."
- code: F11
  category: editorial-advisory
  section: 2026-10-09/cve-2026-107406-citrix-netscaler-saml-idp-overflow
  item: "build string differs from the vendor's"
  url_or_quote: "13.1-37.283 (13.1-FIPS and NDcPP)"
  summary: "Citrix's fixed build is '13.1.37.283' (as the same entry's fixed field and body write it); the action uses a hyphen form, which a defender comparing build strings would not match."
- code: F11
  category: editorial-advisory
  section: 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow
  item: "(low confidence) techniques: [T1199]"
  url_or_quote: "techniques: [T1199]"
  summary: "T1199 (Trusted Relationship) describes an adversary using a third party's access to reach the target; the sources say only that the supplier's own infrastructure was breached by malware and that Publica data may be in it. No source says the attackers used the supplier's access to enter Publica or federal networks. The gate requires a non-empty mapping, so the main agent may keep it; at minimum the run record should say it is the closest available id."
```
