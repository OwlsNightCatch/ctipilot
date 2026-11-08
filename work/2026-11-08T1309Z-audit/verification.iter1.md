**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-08T14:25:54Z · ended_at=2026-11-08T14:54:32Z · duration_seconds=1718

## Verification report — 2026-11-08T1309Z-audit (iteration 1)

Scope: first pass, cold. Ledger `claims.iter1.yaml` (223 claims) walked in full, one verdict row each (`verification.iter1.claims.yaml`: 219 ok, 3 F3, 1 F4). The three new entries were read whole against freshly fetched primaries (Keycloak 26.8.2 notes and Red Hat CVE page, both IBM API Connect bulletins, Elastic report page and PDF); the 27 updated entries were checked on the claims this fire changed (new sections, changed sentences, changed frontmatter, record summaries) against the cited pages, most re-fetched this iteration (Ubuntu, Splunk, Android, QNAP, Todyl, Fortinet, LiteLLM, Siemens, NetApp, Sophos, Cisco, Xerox via the cached primary), each entry read whole for supersession. Run record and audit report claims checked on disk: records by type (9 update, 11 correction, 7 improvement, 6 internal) and `updated_entry_ids` (27) match the entry files; `cves_seen.json` 18 added and 40 `last_seen` bumps; registry additions (4 records; 58 and 35 reproduce from first_seen 2026-11-02 onward excluding this audit's four); sources.json (balbooa-blog candidate, novee-security demoted, seven recipe notes); the warning acknowledgment (text consistent with the 2026-11-05 run record); the `.gitignore` negation (gate.log no longer ignored); truth-pass counts (47 entries: 23 clean, 19 imprecision, 5 factual-error; 1,380 claims, TE 4 unreadable); KEV window (3 additions, all covered); fire telemetry (iterations 6, 6, 8, 8, 6, 8, 2; durations 1.0 to 5.2 h; all publish_status ok; the two partial-claim passes 229/211 and 237/236); over-length word counts (Publica 1,141, eMudhra 909, LiteLLM 854, ARTEX 726, Danfoss 711, Berlin 705); ATT&CK pin 20.1.

### Citation does not support the claim
- #1 (F3) `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow`, claim 4ac3f0e3fa: "Publica confirmed the sequence to the paper: it asked PK Softech in September 2025 to delete all legacy data ... ([Inside IT, 2026-10-22](https://www.inside-it.ch/publica-wollte-pensionskassendaten-loeschen-lassen-20261022))". The fetched Inside IT page has no 2025 date (only "im Januar 2026 schriftlich bestätigt" and Publica's "Als Konsequenz aus dem Fall Xplain haben wir PK Softech aufgefordert ... zu löschen"). The month is watson.ch 2026-11-03 ("Forderung der Publica im September 2025"), whose citation this fire removed from the sentence together with "more than two years after the Xplain leak according to watson.ch". Fix: restore the watson.ch citation after "September 2025" or drop the month.
- #2 (F3, low confidence) same entry, summary, claim f30604d73e: "the Bernische Pensionskasse says more data left the supplier than first thought". BPK 2026-10-20: "ist davon auszugehen, dass ... mehr Daten abgeflossen sind als bis anhin gedacht" (to be assumed). The Correction section says "assumes"; the summary states it as BPK's assertion.
- #3 (F3, low confidence) `2026-11-08/elastic-threats-etc-report-...`, claim f05564088c: "from an anonymized hosting address". The PDF's 9 July case reads "from an anonymized IP known to be malicious"; "Anonymized IP from hosting provider" is the label for the recurring late-June/July pattern.

### Unsupported / hallucinated facts
- #4 (F4, low confidence) `2026-11-08/cve-2026-117691-keycloak-...`, claim ba7daad0da, Defender takeaway: "because the bypass needs one unauthenticated request and Red Hat offers no workaround". No fetched source says "one request". The Red Hat page also carries a "CME Mitigation Guidance (2026-11-06)" block (AI-assisted courtesy guidance) naming an interim lever ("Audit and restrict account registration on external Identity Providers to prevent attackers from capturing legitimately signed redirect-binding messages") and describing a request that places the encoded unsigned parameter before a legitimately signed one, a prerequisite the entry omits. The formal Mitigation statement ("not available or ... do not meet the Red Hat Product Security criteria") supports "no mitigation that meets its criteria", not "no workaround".

### Analytical-link-as-fact
- #5 (F13, low confidence) `2026-11-02/android-sms-of-death-...`, title "CVE-2026-58882, fixed for Android 14 to 17 at the 2026-11-01 security patch level". The CVE-to-flaw link is BleepingComputer's ("tracked as CVE-2026-58882", patched "in its October 2026 Android security updates"); Google's bulletin row (A-517376969, DoS, Critical, System, 14 to 17) has no description. Summary, body and sourcing note hedge it; title does not.

### Needs more research
- #6 (F8) Keycloak entry: the same 26.8.2 release notes list "[#54333] [CVE-2026-111497] Out-of-bounds write in bundled Brotli decoder dist/quarkus", the CISA-KEV exploited Node2Shell flaw the store covers in `2026-10-24/cve-2026-111497-node2shell-...` and `2026-11-07/cve-2026-111497-brotli-desigo-...`. The Keycloak entry mentions neither and has `references: []`. Add a sentence and a `references[]` link.
- #7 (F8, low confidence) IBM API Connect entry: the bulletins carry about 200 CVE rows (207 distinct ids across both pages by my parse) and 18 unauthenticated rows at CVSS 9.0 to 9.9 (matches G1's count). The entry gives no count and lists 7; omitted equally critical rows include CVE-2026-17313 (9.8, gateway-configuration takeover via authentication bypass), CVE-2026-17409 (9.4, unauthorized administrative operations) and CVE-2026-16884 (9.9, XXE). State the count and that cves[] is a selection.

### Surface contradiction
- #8 (F9, low confidence) Publica entry: the 2026-10-17 section still says "Bernische Pensionskasse told the NZZ that ... it must be assumed that personal data left, which replaces its earlier statement that it had no indication of theft" (and keeps the NZZ evidence quote), while BPK's own notices (2026-10-15, 2026-10-30) say it does not know whether its insured persons' data left. The new Correction states the second; no Contradiction line ties them.

### Missed angles
- #9 (F10) Node2Shell entry (and the 2026-11-07 Brotli entry): Keycloak 26.8.2 (2026-11-05) fixes CVE-2026-111497 in its bundled decoder; a changelog update naming Keycloak and the fixed release is missing. Query: "Keycloak 26.8.2 CVE-2026-111497 bundled Brotli decoder quarkus". Otherwise coverage looks complete: all three KEV additions of the week are covered, the re-sweeps' drop list (Plex2Shell, Chrome 157, Android November bulletin, LXD, HPE Fabric Composer, Aspera Faspex, Entra device registration) is defensible on the recorded reasons (HPE's advisory itself offers a workaround, IBM's lists none, which separates the two hard-coded-credential rows).

### Editorial / less-is-more flags (advisory)
- #10 (F11) Keycloak, IBM and Elastic `sourcing_note`: three to four sentences each, arguing the tier ("count as one assessor/source"); Keycloak adds "the project's main sponsor" with no source. Two sentences of provenance suffice.
- #11 (F11, low confidence) Keycloak "[Red Hat, 2026-11-06]": the page's public date is 2026-11-05 (changed 2026-11-07); one-day drift.
- #12 (F11) QNAP record 2026-11-08T13:55:30Z summary: "so every QNAP product the entry names now has a fixed build" ("the entry" in a reader-visible line).
- #13 (F11) Elastic: the "eight minutes from infostealer infection to login" figure (body and evidence) is a vendor breakout-time statistic, the class check 7 names; no decision hangs on it.
- #14 (F11) Record summaries narrower than their sections: Node2Shell (ELLIO correction absent from the record), Publica (Inside IT/AWP fix, T1486), ARTEX (remediation-cycle point); the Brotli/Desigo correction also silently trims four source-supported clauses (Siemens "the affected functionality is not used or exposed", Mitel "still lists several products as under investigation", Cisco "revised often", the takeaway's Cisco/CISA exploitation sentence).
- #15 (F11) Node2Shell body: Splunk "updated on 2026-11-04" next to "(as revised on 2026-11-06)"; the page's changelog lists 11-04, 11-05 and 11-06.
- #16 (F11) Linux TCP headline/title "WatchGuard and Fortinet still have none": the new section says Fortinet shipped an IPS virtual patch (FMWP 26.113) and no fixed build; "no fixed build" is exact.
- #17 (F11) Gridbox summary stops at 2.20.4.2 while the headline, action and takeaway now say 2.20.5.0.
- #18 (F11, pre-existing, low confidence) Danfoss record 2026-10-25 summary: "so a firmware update alone does not close the exposure" is the entry's inference inside the sentence reporting ANSSI. The audit declined it with a reason that is plausible; noted only.

### Checked and clean (no finding)
Keycloak, IBM and Elastic entries otherwise match their primaries (CVSS 9.1 and vector, fixed version, CVE ids and one-line descriptions, IBM scores, affected ranges, fixed builds and "None" workarounds, Elastic cases and quotes; all evidence quotes verbatim); priority, classification, kind and actions fit; no IOCs. Updated entries: Gridbox, Berlin, Cisco SEG (internal re-point), Zyxel (technique and re-entry claim removed), Synology, Ivanti (internal re-grade, upgrade and compromise-check actions kept), eMudhra, ARTEX, LiteLLM (both replacement quotes verbatim), QNAP (QSA-26-19 V1.1), Cisco PHP2Shell (v1.11), NetApp (rev 12.0), WordPress, Linux TCP, Vaud, Android, Xerox (v6), Barracuda (repo created 2026-11-03T19:20Z), cPGuard, Sophos RCA (dateline 20 October 2026), FreeSWITCH, exposed-app credentials (Todyl 11/6 update), Brotli/Desigo (SSA-045512 V1.2), Apple/BSI all hold against fetched pages. Records: every non-internal record has its section and matching `updated_at` mirror (updates only); internal records carry no section; declared fields cover the changed frontmatter.

### Verdict
NEEDS_FIXES (truth: 5, editorial: 4, advisory: 9)

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: updated-entry-body
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow, 2026-10-10..2026-10-22 section, sentence 'Publica confirmed the sequence to the paper: it asked PK Softech in September 2025 to delete all legacy data'"
  url_or_quote: "https://www.inside-it.ch/publica-wollte-pensionskassendaten-loeschen-lassen-20261022"
  summary: "Claim 4ac3f0e3fa. The cited Inside IT page carries no 2025 date at all (it says only that Publica asked PK Softech to delete legacy data and got written confirmation in January 2026). 'September 2025' is stated by watson.ch 2026-11-03 ('Forderung der Publica im September 2025'), whose citation this fire removed from the sentence (it also dropped 'more than two years after the Xplain leak according to watson.ch'). Restore the watson.ch citation after 'September 2025' or drop the month."
- code: F3
  category: claim-not-supported
  section: updated-entry-frontmatter
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow, summary: 'the Bernische Pensionskasse says more data left the supplier than first thought but can neither confirm nor rule out...'"
  url_or_quote: "https://bpk.ch/hauptnavigation/cybervorfall"
  summary: "(low confidence) Claim f30604d73e. BPK's notice of 2026-10-20 says 'ist davon auszugehen, dass ... mehr Daten abgeflossen sind als bis anhin gedacht' (it is to be assumed, after press reports); the summary drops the assumption and states it as BPK's assertion, while the Correction section (correctly) says 'what it assumes ... is that more data left'. Align the summary to 'assumes'."
- code: F4
  category: hallucinated-fact
  section: new-entry-body
  item: "2026-11-08/cve-2026-117691-keycloak-saml-http-redirect-signature-bypass, Defender takeaway: 'because the bypass needs one unauthenticated request and Red Hat offers no workaround'"
  url_or_quote: "https://access.redhat.com/security/cve/CVE-2026-117691"
  summary: "(low confidence) Claim ba7daad0da. Neither the Keycloak release notes nor the Red Hat page says the bypass 'needs one unauthenticated request'. The Red Hat page also carries a 'CME Mitigation Guidance (2026-11-06)' block (labelled AI-assisted, courtesy) that names an interim lever ('Audit and restrict account registration on external Identity Providers to prevent attackers from capturing legitimately signed redirect-binding messages') and describes a request that places the encoded unsigned parameter before a legitimately signed one, i.e. a prerequisite the entry omits. Say 'Red Hat's formal mitigation statement offers none that meets its criteria', drop 'one request', and mention the prerequisite/lever or state that the page's courtesy guidance exists."
- code: F3
  category: claim-not-supported
  section: new-entry-body
  item: "2026-11-08/elastic-threats-etc-report-november-2026-signed-ai-assistant: 'A compromised university account reached Azure Resource Manager over the ROPC grant from an anonymized hosting address'"
  url_or_quote: "https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf"
  summary: "(low confidence) Claim f05564088c. The PDF says the 9 July case came 'from an anonymized IP known to be malicious'; 'Anonymized IP from hosting provider' is the label it gives to the source of the recurring late-June/July pattern ('The same shape recurs ... the source is repeatedly logged as ...'). Write 'an anonymized, known-malicious address' for the case, keep 'hosting' for the pattern."
- code: F13
  category: analytical-link-as-fact
  section: updated-entry-title
  item: "2026-11-02/android-sms-of-death-wap-push-telephony-crash, title: 'CVE-2026-58882, fixed for Android 14 to 17 at the 2026-11-01 security patch level'"
  url_or_quote: "https://source.android.com/docs/security/bulletin/2026/2026-11-01"
  summary: "(low confidence) The link between this flaw and Google's November bulletin row rests on BleepingComputer's 'tracked as CVE-2026-58882'; the bulletin row (A-517376969, DoS, Critical, System, 14 to 17) has no description, and BleepingComputer says Google patched it in the October updates. The summary, body and sourcing note hedge this ('the identifier BleepingComputer gives'); the title and cves[] state it as fact. Add the hedge to the title or keep the CVE out of it."
- code: F8
  category: needs-more-research
  section: new-entry-body
  item: "2026-11-08/cve-2026-117691-keycloak-saml-http-redirect-signature-bypass (Exposure / Defender takeaway)"
  url_or_quote: "https://www.keycloak.org/2026/11/keycloak-2682-released"
  summary: "The same 26.8.2 release notes list '[#54333] [CVE-2026-111497] Out-of-bounds write in bundled Brotli decoder dist/quarkus', the CISA-KEV exploited Node2Shell/Brotli flaw the store covers in 2026-10-24/cve-2026-111497-node2shell-... and 2026-11-07/cve-2026-111497-brotli-desigo-... Neither the Keycloak entry nor `references[]` mentions it, so a reader upgrading for the SAML flaw is not told the release also closes an exploited decoder flaw in the bundled runtime. Add one sentence and a `references[]` link to the Node2Shell entry."
- code: F10
  category: missed-angle
  section: coverage
  item: "2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi (and 2026-11-07 Brotli entry): Keycloak is not among the affected products"
  url_or_quote: "https://www.keycloak.org/2026/11/keycloak-2682-released"
  summary: "Keycloak 26.8.2 (2026-11-05) fixes CVE-2026-111497 in its bundled Brotli decoder (release note #54333); a changelog `update` on the Node2Shell entry naming Keycloak and the fixed release is missing. Suggested search: 'Keycloak 26.8.2 CVE-2026-111497 bundled Brotli decoder quarkus'."
- code: F8
  category: needs-more-research
  section: new-entry-body
  item: "2026-11-08/ibm-api-connect-hard-coded-administrative-credentials-unauth: 'fix a long list of CVEs; among the rows that need no privileges is ...'"
  url_or_quote: "https://www.ibm.com/support/pages/node/7295635"
  summary: "(low confidence) The two bulletins carry about 200 CVE rows (207 distinct ids by my parse of both pages) and 18 unauthenticated rows at CVSS 3.1 9.0 to 9.9 (it matches the re-sweep's own count). The entry never gives the count and lists 7; equally critical rows it omits include CVE-2026-17313 (9.8, authentication bypass taking control of gateway configuration), CVE-2026-17409 (9.4, unauthorized administrative operations) and CVE-2026-16884 (9.9, XXE). One clause with the count would let a reader size the update; cves[] is a selection and should say so."
- code: F9
  category: surface-contradiction
  section: updated-entry-older-sections
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow, 2026-10-17 section ('Bernische Pensionskasse told the NZZ that ... it must be assumed that personal data left, which replaces its earlier statement that it had no indication of theft') and the NZZ evidence quote"
  url_or_quote: "https://bpk.ch/hauptnavigation/cybervorfall"
  summary: "(low confidence) BPK's own notices (2026-10-15, 2026-10-30) say it does not know whether its insured persons' data left; the new Correction section states that, but the older NZZ-attributed sentence and the NZZ evidence quote remain with no Contradiction line pointing at the difference."
- code: F11
  category: editorial-advisory
  section: new-entries-sourcing-note
  item: "Keycloak, IBM API Connect and Elastic entries, sourcing_note"
  url_or_quote: "sourcing_note: 'describe the same fixes, so they count as one assessor' / 'so they count as one source' / 'the summary page and the full report are one source'"
  summary: "Each sourcing_note runs three to four sentences and argues the verification tier ('count as one assessor/source'); two sentences of provenance suffice. The Keycloak note also asserts 'the project's main sponsor' with no source."
- code: F11
  category: editorial-advisory
  section: new-entry-citation-date
  item: "Keycloak entry: '[Red Hat, 2026-11-06]' and sources[].date 2026-11-06"
  url_or_quote: "https://access.redhat.com/security/cve/CVE-2026-117691"
  summary: "(low confidence) The Red Hat page's public date is 2026-11-05 (field_cve_public_date 2026-11-05T00:00:00Z); 2026-11-06 is the date of the CME guidance block and the page was changed 2026-11-07. One-day drift, may be a timezone artifact."
- code: F11
  category: editorial-advisory
  section: updated-entry-record-summary
  item: "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed, record 2026-11-08T13:55:30Z summary: 'so every QNAP product the entry names now has a fixed build'"
  url_or_quote: "so every QNAP product the entry names now has a fixed build"
  summary: "'the entry' is composition language in a reader-visible changelog line; say 'so QTS, QuTS hero, QuTScloud, QVR, TVR OS, Notes Station 3 and QNE (ADRA) all have fixed builds'."
- code: F11
  category: editorial-advisory
  section: new-entry-vanity-metric
  item: "2026-11-08/elastic-threats-etc-report-november-2026-signed-ai-assistant: 'the average time from an infostealer infection to the actor logging in with the same credentials is eight minutes' (body and evidence[] quote)"
  url_or_quote: "https://www.elastic.co/security-labs/reports/threats-etc-report-november-2026-trouble-with-trust"
  summary: "A vendor breakout-time statistic ('in some cases', no method), the class check 7 names as a vanity metric; the entry draws no defender decision from it and uses it as one of three evidence quotes. Drop it or tie it to a decision."
- code: F11
  category: editorial-advisory
  section: updated-entry-record-summary
  item: "Record summaries narrower than their sections: Node2Shell (record 2026-11-08T13:53:39Z omits the ELLIO 'statement already outdated' correction its section carries), Publica (omits the Inside IT/AWP attribution fix and the T1486 mapping), ARTEX (omits the remediation-cycle point); Brotli/Desigo correction also trims four source-supported clauses the record does not name (Siemens 'affected functionality is not used or exposed', Mitel 'still lists several products as under investigation', Cisco 'revised often', and the takeaway's Cisco/CISA exploitation sentence)"
  url_or_quote: "https://cert-portal.siemens.com/productcert/html/ssa-443410.html"
  summary: "The record summary should state what the section states, no more, no less. The trimmed Siemens clause explains why an Industrial Edge setup without Management Applications needs no action (supported by SSA-443410: 'the affected functionality is not used or exposed')."
- code: F11
  category: editorial-advisory
  section: updated-entry-body
  item: "2026-10-24/cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi: 'Splunk's advisory SVD-2026-1015, published on 2026-10-28 and updated on 2026-11-04 ...' followed by '(as revised on 2026-11-06)'"
  url_or_quote: "https://advisory.splunk.com/advisories/SVD-2026-1015"
  summary: "The page's changelog lists updates on 2026-11-04, -05 and -06 (Last Updated 2026-11-06); the first date in the sentence is now stale next to the second. Say 'updated through 2026-11-06'."
- code: F11
  category: editorial-advisory
  section: updated-entry-headline
  item: "2026-10-31/cve-2026-98432-linux-kernel-tcp-uaf-mptcp-remote-root, headline and title: 'WatchGuard and Fortinet still have none'"
  url_or_quote: "https://fortiguard.fortinet.com/psirt/FG-IR-26-188"
  summary: "Same-run section states Fortinet shipped an IPS virtual patch (FMWP database update 26.113, 2026-11-07) and no fixed build; 'have none' reads as no remedy. Say 'no fixed build' in the headline."
- code: F11
  category: editorial-advisory
  section: updated-entry-frontmatter
  item: "2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave, summary ends at 'Gridbox 2.20.4.2 (27 October) ...'"
  url_or_quote: "https://www.balbooa.com/blog/gridbox/gridbox-2-20-5-0-security-deep-dive"
  summary: "The headline, action and takeaway now point to 2.20.5.0 but the summary (what a reader of the summary alone sees) still stops at 2.20.4.2 and omits the four 2.20.5.0 fixes."
- code: F11
  category: editorial-advisory
  section: updated-entry-record-summary
  item: "(pre-existing) 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack, record 2026-10-25T03:37:30Z summary: 'not vulnerabilities researchers had published, so a firmware update alone does not close the exposure'"
  url_or_quote: "https://www.publicsenat.fr/actualites/politique/des-defauts-de-securisation-elementaire-et-des-mots-de-passe-faibles-ont-permis-la-cyberattaque-contre-les-frigos-de-supermarches"
  summary: "(low confidence, pre-existing, declined by the audit with a reason) The 'so ...' clause is the entry's inference, written inside the sentence that reports ANSSI's statement. The audit's reasoning (it follows from ANSSI's wording) is plausible; noted for the record."
```
