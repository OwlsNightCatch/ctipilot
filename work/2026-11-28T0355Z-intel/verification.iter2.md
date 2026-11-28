**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-28T05:38:04Z · ended_at=2026-11-28T05:55:38Z · duration_seconds=1054

## Verification report — 2026-11-28T0355Z-intel (iteration 2)

Scope: post-fix pass. 6 new entries, 4 updated entries (read whole, `git diff HEAD` per path), the run record, the registry additions, the 186-claim ledger (all 186 claims answered, 186/186 in `verification.iter2.claims.yaml`: 183 ok, 2 F4, 1 F3; `claim_ledger.py --coverage 2` reports 0 missing). Coverage of the ledger: all 29 changed claims, every other claim of the nine remediated entries, and every Mitel claim (the one entry with no remediation delta; read in full rather than a quarter). Sources were re-fetched live this iteration (extract, `url --direct` raw HTML for the Kudelski tables, Hunt.io dateline, GHSA sidebars, ENISA JSON, BSI CSAF, `cisa-kev`, `ncsc-csh post`, WebFetch with the outbound-links template for the CISA alert); every `evidence[]` quote of the ten entries was substring-checked against the pages (all found; the CISA quote through WebFetch plus the gate's jina-fallback check).

### Prior-iteration deltas (all 14 walked)

1. FreeRADIUS: confirmed. The live project page gives Ada Logics' proof of concept only for the two High EAP-FAST issues; the Critical TTLS issue (Severity: Critical, "The TTLS module is enabled in the default configuration") carries no exploitation or PoC statement. Severity count 1/8/5/7 = 21 confirmed programmatically. Exposure wording matches ("EAP-TLS, TTLS, and PEAP are enabled in the default configuration"; EAP-MSCHAPv2 section has no default statement).
2. Kudelski: confirmed in the main (raw-HTML table read). Activation state now appears only as Kudelski's Section 9 recommendation in the takeaway. See F8 below for two table rows still dropped.
3. SAP: confirmed. Reuters is gone; the summary attributes the containment steps to heise's relay of Handelsblatt (heise text: "Handelsblatt berichtet unter Berufung auf Konzernkreise, SAP habe den Zugriff auf GitHub eingeschränkt ..."); references[] carries the 1Password entry (exists in the store).
4. GeoServer CVE-2026-129242: confirmed. The live watchTowr FAQ table reads Yes for 129245, 129243 and 120705 and "Not reported" for 129242 and 129244; its prose names all five. The section, sourcing_note and cves[] now say exactly that.
5. GeoServer record summary: confirmed; the "settles which flaws" clause is gone from the record and the section.
6. Cacti BSI: confirmed. The CSAF carries aggregate_severity "kritisch" and one known_affected product; the entry says only "critical".
7. RealVNC: confirmed. ENISA record datePublished "Nov 27, 2026, 5:52:17 AM"; heise dateline 2026-11-27.
8. Hunt.io: confirmed. "mainly reconnaissance targets, one attacked without success" matches "Most of it is reconnaissance; one firm has moved into hands-on attack" and the table row "Attacked, no success"; the "only case" absolute and the in-body absence claim are gone; the registry no longer carries the two orphan product records (but see F4 on the run record).
9. BACS: confirmed against SRF ("drei Betreiberinnen kritischer Infrastrukturen ... Auch KMU, welche die Vorfälle freiwillig gemeldet hätten, seien ... gehackt worden").
10. nginx update: confirmed. Synology revisions 3 and 4 read "Update fix status for APM ..."; Cisco v1.6 (2026-NOV-27) adds the Crosswork Hierarchical Controller, Secure Endpoint Private Cloud Appliance, Intersight, UCS Fabric Interconnect and Optical Network Controller rows and has no NextFusion row (0 hits); Fortinet's page lists FortiADC, FortiWeb and FortiSIEM not impacted, 29 names under investigation and the FortiVoice Cloud and FortiEdge Cloud remediation.
11. Kudelski: assessment basis and recommended detections confirmed against the page (partial; see F8).
12. Run record Cacti disposition: confirmed against `runs/2026-11-27/2026-11-27T0355Z-intel.md` line 378 (single watchTowr source, guest account must be enabled, no CVE or fix, no exploitation).
13. Missing citations and F11 items: confirmed (FreeRADIUS and nginx sentences carry links; GeoServer capitalisation fixed; Cacti body carries 4HTTP2SHELL, matching the README "This is 4HTTP2SHELL" and BleepingComputer "previously 4HTTP2ROOT").
14. GeoServer priority: judged. `critical` needs every element of the stop-reading bar; the release is 5+ weeks old, exploitation rests on CISA's undescribed KEV evidence for two chain flaws plus watchTowr's honeypot probes, no victim or scale is named, and the bar says "If unsure, it is `high`". Keeping `high` is defensible. "The product is niche" is the weakest part of the stated reason (the entry itself tags public-sector), but the conclusion stands. No finding.

### Unsupported / hallucinated facts

- **#1 (F4) run record `entities_added`**: lists `product:active-directory-domain-services` and `product:microsoft-jdbc-driver-for-sql-server`. Remediation removed both from `entities/registry.yaml`; grep of the registry finds neither and `git diff HEAD` shows 10 additions, not 12. The record names entities that do not exist. Drop the two keys.
- **#2 (F4, low confidence) cacti, Detection**: "one client requesting the guest profile page, a profile update, a graph preview and a realtime graph within seconds" and "shells or download tools started under it", cited to RavenAI and watchTowr. RavenAI: "The observable trail is correspondingly mundane: a guest profile update, a graph preview, and a realtime graph initialization"; "any newly written shell or marker are stronger investigation pivots". watchTowr: "new files created by the poller process". No source gives a timing or names download tools. Drop both or move them outside the citation as the entry's own inference.
- **#3 (F4, low confidence) kudelski, Detection**: "accounts created for people who already hold customer records and never reset a password". The page says the accounts were created "without possessing their original passwords"; nothing says no password reset, and the entry's sourcing_note says the post gives no ordered attack chain. Use the page's wording or its detection row "Newly created accounts accessing sensitive information".

### Citation does not support the claim

- **#4 (F3, low confidence) sap, body para 1**: "it gave no vector, actor, discovery date or list of affected systems" cited to BleepingComputer and tagesschau.de. tagesschau: "Welcher Art die Aktivitäten waren, wann sie entdeckt wurden und welche Bereiche betroffen sind, ließ SAP offen"; BleepingComputer: SAP "did not specify the environments". Neither says anything about an actor or an attack vector; that is Handelsblatt ("Details wie den Angriffsweg oder mögliche Täter nannte SAP nicht"), which this clause does not cite. Add the citation or trim the clause.

### Needs more research

- **#5 (F8, low confidence) kudelski**: the page's Section 4 table has nine rows, the entry's "The weaknesses it lists are ..." gives seven. Missing: "Identity information could be tested at scale" and "Authorization-related information was exposed to the client". The Section 8 table row "Source-map access by automated clients" is also absent from "Its recommended detections are". The word budget is tight (549/550), so rephrase to "Among the weaknesses it lists, all business logic ..." and swap one lower-value detection for the source-map one.

### Editorial / less-is-more flags (advisory)

- **#6 (F11, low confidence) nginx summary**: "UCS Director and about two dozen other products": the Cisco v1.6 affected-products table has 21 rows (25 affected in total with Catalyst Center, ISE, Nexus and UCS Director), so "other" overcounts by about three. The section's "among about two dozen products" is right.
- **#7 (F11, low confidence) cacti date labels**: Previdian's blog dateline is "Published: 26 November 2026" (article:published_time 2026-11-26T18:35Z, modified 2026-11-27T12:17Z) and the entry labels it 2026-11-27; the Cacti documentation and releases pages are living pages labelled with the read date. Consider "(as read 2026-11-28)".
- **#8 (F11, low confidence) mitel sourcing_note**: "Mitel's advisory page (revision 1.0 on 2026-11-28)" reads as revision 1.0 dated 2026-11-28; the page's revision table says 1.0 is 2026-11-18. Rephrase as the body does ("still at revision 1.0 when read on 2026-11-28").
- **#9 (F11, low confidence) registry `incident:sap-github-project-granite-2026-11`**: the summary still joins "DER SPIEGEL's insider and Handelsblatt's company circles" across tokens, source code and replaced signing keys, the attribution the entry summary was corrected away from. Align it with the entry.

### Coverage and other whole-run checks

- Update-vs-new: no new entry duplicates the 14-day prior-coverage index (92 records searched for Cacti, FreeRADIUS, RealVNC, Hunt.io, SAP, Kudelski, insurer, ntdsutil); the nearest items (1Password, BabidiGhost, CyberPower ntdsutil ifm) are distinct and the SAP and Kudelski entries declare them in references[] where they build on them. The four updates are the same finding each with a genuine delta; record types and `updated_at` mirrors hold (BACS 04:41:50Z, GeoServer 04:50:22Z, nginx 04:51:23Z; Mitel improvement leaves `updated_at: null`); `fields` cover every changed frontmatter line in `git diff HEAD`; earlier-section edits (nginx 2026-11-26 section, GeoServer 2026-11-26 section) are declared under `body`.
- Relevance and priority: SAP supplier and Swiss tax office victim carry a clear Swiss nexus; FreeRADIUS and RealVNC are exposure-driven `notable` entries (default-enabled pre-authentication memory-safety flaws in authentication infrastructure and remote-access software) held below `high` because no exploitation or public PoC exists; I judged inclusion defensible, not flagged.
- Style: no em dashes outside section headings, no IOCs, no registry keys, Admiralty codes or pipeline vocabulary in reader-facing text (the only grep hit was the word "product:" in prose). Classification blocks present and in vocabulary on all ten entries; single-source entries carry `single-source*` plus a sourcing_note.
- Missed angles: none evidenced. KEV catalogue 2026.11.27 adds only GeoServer (two) and Drupal, all covered; NCSC.ch hub shows nothing new beyond GeoServer 13242 and Juniper 13244; the two standard-mode searches surfaced only already-covered items (Node2Shell, N-able, Xen Orchestra). Coverage looks complete for a post-Thanksgiving window.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 1, advisory: 4)

### Findings summary (machine-readable)

See `/home/user/ctipilot/work/2026-11-28T0355Z-intel/verification.iter2.findings.yaml` (9 records). Claim verdicts: `/home/user/ctipilot/work/2026-11-28T0355Z-intel/verification.iter2.claims.yaml` (186 rows: 183 ok, 2 F4, 1 F3).
