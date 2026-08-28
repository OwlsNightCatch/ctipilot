**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-28T06:24:01Z · ended_at=2026-08-28T06:40:46Z · duration_seconds=1005

## Verification report — 2026-08-28T0409Z-intel (iteration 4)

Confirmation pass following iteration 3's CLEAN. Read cold: all 36 new entries end-to-end, all 7 updated entries (full body + `git diff HEAD`), and the run record. Fetched primary sources for every vulnerability entry, every KEV addition, every changelog section's citations, and sampled/fully read sources for threat/incident/research entries. Did not anchor on the prior CLEAN verdict.

### Unsupported / hallucinated facts

**#1.** `2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce` — title, summary, body and one `actions[]` item all state "Claroty's own internet-wide scan found roughly 2,765 exposed devices" / "its own measurement puts the exposed population at roughly 2,765 devices" / "treat any of the roughly 2,765 internet-exposed devices... as a priority," cited to `https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers`. I fetched that page in full (via `extract`) and searched it for any comma-formatted number — none exists anywhere in the article. The only exposure language Claroty uses is: "Our analysis began by examining the internet exposure of these devices, where we identified **thousands** of publicly accessible management interfaces." No source cited anywhere in the entry supports the specific figure 2,765; it appears fabricated and then propagated through the title, summary, body and an action item. This is the entry's own headline evidence for its `high`-adjacent framing of exposure scale, and it does not exist in the cited source.

**#2.** `2026-08-28/adobe-august-2026-coldfusion-campaign-classic-cvss10` — body states "CVE-2026-48362 ... and CVE-2026-48273 (CWE-95, eval injection, 9.9) — both unauthenticated arbitrary code execution," and frontmatter `cves[]` carries `auth: pre-auth` for CVE-2026-48273. I fetched Adobe's own APSB26-90 table directly: CVE-2026-48273's own CVSS 3.1 vector, as published by Adobe, is `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H` — `PR:L` (privileges required: low), not `PR:N`. Adobe's own vector for the flaw the entry calls "unauthenticated" states the attacker needs low privileges. This contradicts both the body's "unauthenticated" claim and the frontmatter's `auth: pre-auth` for this specific CVE (CVE-2026-48362's own vector is genuinely `PR:N` and is correctly pre-auth; only -48273 is misstated).

**#3.** `2026-08-28/gocaracal-dark-caracal-ethereum-smart-contract-c2` — the `evidence[]` quote "After repeated failures to reach primary C2, malware sends eth_getStorageAt request to public Ethereum JSON-RPC endpoint and reads value from contract storage ... Operators can update stored C2 value through blockchain transaction, deployed implants retrieve new address without receiving updated binary" is not a verbatim substring of Arctic Wolf's post (fetched directly). The source reads: "After repeated failures to reach **the** primary C2, **the** malware sends **an** eth_getStorageAt request to **a** public Ethereum JSON-RPC endpoint and reads **a** value from **the configured** contract's storage," and separately "Operators can update **the** stored C2 value through **a** blockchain transaction, **and** deployed implants **can** retrieve **the** new address without receiving **an** updated binary." Multiple articles/words are silently dropped from both halves of the quoted material (bold = removed), presented inside quotation marks as if verbatim. Same text is reused in the body prose.

**#4.** `2026-08-28/isolated-vm-toctou-type-confusion-sandbox-escape` — the `evidence[]` quote "Walk 1's IsArrayBuffer() check says nothing about the value walk 2 receives, and As<ArrayBuffer>() is an unchecked reinterpret-cast, not a conversion" does not appear anywhere in Endor Labs' post (fetched directly and searched exhaustively for "reinterpret-cast", "checked conversion", "walk 1", "walk 2"). The source's actual sentence is: "`As<ArrayBuffer>()` is **not a checked conversion**. It is a **bare reinterpret-cast** that tells V8, 'trust me, this is an `ArrayBuffer`.' The code assumes it is safe because walk 1 already checked, but that assumption only holds if the two walks see the same values." The entry's quoted sentence is a synthesized composite that does not exist as a contiguous string in the source — it recombines phrases from that sentence with the "walk 1"/"walk 2" labels from a separate code comment, into new wording ("says nothing about the value walk 2 receives") the source never states.

**#5.** `2026-08-28/kudelski-bismarck-dprk-it-worker-gambling-fakecalls-overlap` — the `evidence[]` quote "We recently observed a stealer log leak involving an actor linked to the DPRK, nicknamed 'Bismarck.' The actor used two IP addresses that overlap with indicators **[associated with the gambling-platform operation]**" misrepresents what the bracketed redaction replaces. Kudelski's actual sentence (fetched directly): "The actor used two IP addresses that overlap with indicators of compromise (IOCs) documented by Check Point Research in its analysis of FakeCalls, an Android banking trojan targeting South Korea." The overlap is with **FakeCalls IOCs**, not with "the gambling-platform operation" — Bismarck's link to gambling platforms is a separate finding from the IP overlap with FakeCalls. The sourcing_note frames this as "lightly redacted to remove literal indicators while preserving the analytic claim," but the substitution changes the claim rather than preserving it (the body prose gets this right; only the frontmatter `evidence[]` quote is wrong).

### Quantifier without source

(Folded into Unsupported/hallucinated facts #1 above — the "2,765" figure is the canonical case this check exists for.)

### Needs more research

**#6.** `2026-08-28/splunk-svd-2026-0801-embedded-report-session-hijack` — the entry's own `sourcing_note` states: "Splunk's advisory does not itself describe any CVE as reaching 'the credential store' via privileged SPL escalation." I fetched Splunk's SVD-2026-0801 advisory directly and this is false on its face: **CVE-2026-76253** ("Privilege Escalation through Scheduled Search Alert Action Configuration in Splunk Enterprise," CVSS 3.1 8.8, CWE-269) states verbatim: "a user that holds a role with the schedule_search capability could run arbitrary Search Processing Language (SPL) commands with the highest level of system privilege **and read every credential stored in the credential store**, which can allow for disclosure and modification of all relevant data and affect system integrity and availability." This CVE is not in the entry's `cves[]`, not named in the body's "further high-severity items" paragraph (which names only CVE-2026-76350 and CVE-2026-76351), and not distinguished from CVE-2026-76350 (a different flaw, PDF-attachment-triggered SPL execution) anywhere. CVE-2026-76253 is arguably more severe from a triage standpoint than either of the two "further" CVEs the entry does cover — full credential-store disclosure via a low, schedule-only capability — and its total omission from an entry whose whole premise is "session hijack against the SIEM itself" is a real gap, not just a sourcing_note inaccuracy.

### Editorial / less-is-more flags (advisory)

**#7.** (low confidence) `2026-08-28/nimbus-manticore-twostroke-backdoor-europe` — the `evidence[]` quote "Specific targets include European nations such as the UK, France, Albania, and Belarus, alongside Middle Eastern regions." ends with a period at a point where Group-IB's actual sentence continues: "...alongside Middle Eastern regions **including Israel, Turkey, and GCC member states**." The quote is truncated without an ellipsis marking the cut, presented as if it were the complete sentence. Same pattern (leading-clause trimmed without ellipsis) in `2026-08-28/ta4922-packclient-telegram-rat-tax-lures`'s first evidence quote — Proofpoint's actual sentence opens "**With this new payload,** TA4922 is expanding its arsenal..." and the entry's quote drops the opening clause silently.

**#8.** (low confidence) `2026-08-28/yootheme-zoo-joomla-unauth-file-upload-rce-sqli` — body states the CVSS correction for CVE-2026-76613 moved "from 9.2 with an erroneous PR:N... to 8.6 with the accurate PR:H, which YOOtheme confirmed to the CNA." mySites.guru's own post (the entry's sole source) does not call PR:H "accurate" — it explicitly flags an unresolved tension: "One mismatch survives the correction. The revised vector says PR:H... while the description still says 'any contributor-level user'... We have not audited YOOtheme Pro ourselves, so we cannot settle which reading is right." The entry drops this caveat and presents PR:H with more confidence than the source itself claims.

### Classification missing / inconsistent

**#9.** Two KEV-addition entries in this same run apply different `verification` values to functionally identical sourcing patterns (a vendor/technical primary + the CISA KEV JSON feed as a second primary, with the KEV entry itself carrying no technical detail beyond the CWE-level description). `2026-08-28/cve-2026-53362-linux-kernel-ipv6-udp-fraggap-kev` — kernel commit (technical primary) + CISA KEV (exploitation-status primary) — is rated `verification: multi-source`, with the sourcing_note explicitly reasoning "the technical mechanism is confirmed directly against the upstream kernel-tree fix commit message; the CISA KEV listing is the independent confirmation of active exploitation." `2026-08-28/cve-2026-66384-jfrog-artifactory-docker-cache-traversal-kev` — JFrog's own advisory (technical primary) + the same CISA KEV feed (exploitation-status primary) — is rated `verification: single-source`, with the sourcing_note reasoning "JFrog's own advisory is the sole technical source; no independent researcher write-up or exploitation narrative was located this run beyond the KEV catalog listing itself." Both entries have the identical two-source shape (vendor/technical + KEV); the run classifies one as multi-source and the other as single-source with no stated basis for the differing treatment.

### Missed angles

None identified with a nameable in-window source this iteration — S1–S4's coverage-backlog clearance and outage-backfill sweep (documented in the run record) appear to have closed the gaps a fresh search would surface; the run record's own stated residual backlog (Zurich trial verdict not due until 2026-09-10, Siemens S7 PDF residual quotes, npm RedC2 aggregator-only gap, out-of-window OpenShift CVE, Keycloak VEX meta-correction) is not defender-actionable on its own terms and is already carried forward transparently.

### Verdict

`NEEDS_FIXES (truth: 5, editorial: 2, advisory: 2)`

Findings #1–#5 are truth-class (F4), confirmed against sources fetched this iteration. #6 is F8 (needs-more-research: a significant CVE omitted from a Splunk KEV-adjacent entry, plus a sourcing_note claim the same advisory directly contradicts) — editorial-class per the F8 category but flagged with the weight the credential-store exposure deserves. #7 and #8 are low-confidence F11 advisory notes on quote-boundary fidelity. #9 is an editorial classification-consistency finding (F17). None of the seven updated entries' changelog sections, diffs, or the run record's published body/telemetry produced a confirmed defect — all changelog citations I independently re-fetched (METR, BleepingComputer, NVD CVE 2.0 API, Onapsis, Check Point, CISA KEV JSON ×2, Der Tagesspiegel ×2, Infosecurity Magazine, The Hacker News) matched the entries' claims exactly.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "Claroty Team82: Danfoss AK-SM 800A refrigeration system managers"
  url_or_quote: "roughly 2,765 internet-exposed devices"
  summary: "Claroty's article (fetched in full) never states this figure anywhere — only 'thousands of publicly accessible management interfaces.' The number appears in title, summary, body and an actions[] item, cited to the same Claroty URL that does not contain it."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "Adobe August 2026 Patch Day: ColdFusion / Campaign Classic"
  url_or_quote: "CVE-2026-48273 ... both unauthenticated arbitrary code execution"
  summary: "Adobe's own APSB26-90 table gives CVE-2026-48273 the vector AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H (PR:L, low privileges required) — contradicts 'unauthenticated' framing and frontmatter auth: pre-auth for this CVE specifically."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "GoCaracal: Dark Caracal's new Go-based malware framework"
  url_or_quote: "After repeated failures to reach primary C2, malware sends eth_getStorageAt request to public Ethereum JSON-RPC endpoint and reads value from contract storage ... Operators can update stored C2 value through blockchain transaction, deployed implants retrieve new address without receiving updated binary."
  summary: "Not a verbatim substring of Arctic Wolf's post — multiple articles (the/a/an) silently dropped from both quoted segments; actual text confirmed via direct fetch."
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "isolated-vm sandbox escape (GHSA-864f-rcv7-6rh4)"
  url_or_quote: "Walk 1's IsArrayBuffer() check says nothing about the value walk 2 receives, and As<ArrayBuffer>() is an unchecked reinterpret-cast, not a conversion."
  summary: "This sentence does not exist anywhere in Endor Labs' post (searched exhaustively). It is a synthesized composite of a separate sentence ('not a checked conversion... bare reinterpret-cast...') and a code comment label ('walk 1'/'walk 2'), presented as one direct quote."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Kudelski Security: North Korean IT-worker infrastructure overlaps a Bismarck-linked gambling-platform operation"
  url_or_quote: "The actor used two IP addresses that overlap with indicators [associated with the gambling-platform operation]."
  summary: "Kudelski's actual text: the IPs overlap with 'indicators of compromise (IOCs) documented by Check Point Research in its analysis of FakeCalls' — the bracketed redaction substitutes a different, incorrect referent (gambling operation instead of FakeCalls) rather than preserving the claim."
- code: F8
  category: needs-more-research
  section: trending-vulnerabilities
  item: "Splunk Enterprise August 2026 hardening release (SVD-2026-0801)"
  url_or_quote: "sourcing_note: 'Splunk's advisory does not itself describe any CVE as reaching \"the credential store\" via privileged SPL escalation'"
  summary: "False per Splunk's own advisory: CVE-2026-76253 (CVSS 8.8) states a schedule_search-capable user 'could run arbitrary SPL commands with the highest level of system privilege and read every credential stored in the credential store.' This CVE is omitted entirely from cves[] and body despite being one of the more severe items in the batch."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Nimbus Manticore (Tortoiseshell/UNC1549) toolset refresh"
  url_or_quote: "...alongside Middle Eastern regions."
  summary: "(low confidence) Quote truncated at a period where Group-IB's sentence continues '...including Israel, Turkey, and GCC member states,' with no ellipsis marking the cut. Same pattern (leading clause dropped) in the TA4922/PackClient entry's first evidence quote."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "YOOtheme ZOO for Joomla unauthenticated file-upload RCE"
  url_or_quote: "8.6 with the accurate PR:H, which YOOtheme confirmed to the CNA"
  summary: "(low confidence) mySites.guru's own post flags an unresolved mismatch between PR:H and the still-published 'contributor-level' description and explicitly declines to say which is right; the entry presents PR:H as settled/'accurate' without carrying that caveat."
- code: F17
  category: classification
  section: trending-vulnerabilities
  item: "cve-2026-66384-jfrog-artifactory-docker-cache-traversal-kev vs cve-2026-53362-linux-kernel-ipv6-udp-fraggap-kev"
  url_or_quote: "verification: single-source (JFrog entry) vs verification: multi-source (kernel entry)"
  summary: "Both entries use an identical sourcing shape (vendor/technical primary + CISA KEV feed as second primary); the run rates one multi-source and the other single-source with no stated basis for the differing treatment."
```
