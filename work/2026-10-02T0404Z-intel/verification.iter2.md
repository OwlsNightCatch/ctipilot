**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-02T06:01:25Z · ended_at=2026-10-02T06:24:55Z · duration_seconds=1410

## Verification report — 2026-10-02T0404Z-intel (iteration 2)

Scope: post-fix pass after iteration 1 (NEEDS_FIXES). All 293 ledger claims have a verdict row in `verification.iter2.claims.yaml` (the 54 changed claims, every claim of the five updated and the eight remediated new entries, and every remaining claim of the Zammad and ANSSI entries; no sampling). Sources were re-fetched live this iteration (extract, raw `url`, `pdf`, `ncsc-csh`, `ncsc-nl csaf`, `cisa-kev`, GitHub API, FIRST EPSS API, WebFetch for the CISA alert). Verdict row totals: ok 280, F3 11, F4 1, F5 1.

### Prior-iteration deltas (38 findings): status of each remediation

- Kiteworks F14 (four advisories): fixed. The 2026-10-02 section now names the three CVSS 9.8 account takeovers (CVE-2026-85065, -85066, -102115; GitHub API list confirms exactly three at 9.8) and cites BleepingComputer's 11 further critical fixes. The run-record note still carries the old count (new F4 #13).
- Kiteworks F4 (no CVE vs CVE-2026-54154): fixed ('for the threat behind the warning'; The Record: 'There is no known CVE, patch, or additional technical details').
- UAT-11587 F4 (in-process load, actor-owned Entra/mailbox/OneDrive): fixed and matches Talos ('inside the script host process, mshta.exe'; 'the threat actor's OneDrive', 'Outlook mailbox folder').
- Citrix F3 (evidence-capture list): re-cited to watchTowr, but the wording 'configuration snapshot' is not what watchTowr, Unit 42 or Citrix KB say (new F3 #1).
- UNCTAD F3 (site count): fixed (count dropped, sites named as Asymmetric names them).
- Adobe F3 (builds 9398-9400): fixed (clause removed; the earlier bulletins sit in references[]).
- Cisco F3 x2 ('out-of-band', Help function): fixed (neither string remains).
- Zimbra F3 (EU KEV date): fixed ('EU KEV | Added 2026-08-18').
- KillSwitch F3 (NCSC sentence): fixed (attributed to the NCSC statement inside the fedpol release).
- Citrix F3 (three hosts): fixed ('those two hosts and a third address').
- Kiteworks F3 x3 (rebrand cite, Record for CVE, 'potentially'): fixed.
- UNCTAD F3 (DSEWiki wording): partly fixed; 'abandoned' and 'out-of-band coordination channel' are gone, but the 54-address clause still misdescribes what the addresses were (new F3 #2).
- Cisco F4 (no-patch tag): fixed. FortiMail F4 (no branch has a fix): fixed and matches FG-IR-26-175. Wien F4 (title/headline): fixed and matches the release. Adobe F4 ('network-reachable'): fixed (all 18 vectors AV:N). Zimbra F4 (EPSS): fixed (0.11736 equals the FIRST API value for 2026-10-01). UNCTAD F4 (attribution per lab): fixed except the Asymmetric staging scope (new F3 #9).
- SDIS F13: the 'second SDIS to confirm' wording is gone from the record summary and headline, but the title still presents SDIS 66 as a confirmation within the wave (new F13 #5).
- Declined SDIS F7: acceptable. ICI frames the theft as a month after the Gard attack and the campaign entry already tracks the unit-by-unit SDIS wave; the registry holds a separate incident record. The condition is that the title stops implying a link (F13 #5).
- Kiteworks F8 (three 9.8 CVEs): fixed and verified against all eight GHSA records.
- Zimbra F8 (injection signature): fixed (matches Microsoft's 'Look for the injection signature itself'); the swatchdog lineage is still generic (F8 #18, low).
- Declined UNCTAD F8 (r.jina.ai): acceptable. The product name is also on the style rule's transport list, and 'AI-search reader proxies' keeps the hunt usable; codetabs.com is still named, so the class is described consistently enough.
- Belnet F8 (guestroam accounts): fixed. Kiteworks F9 (six vs nine hours): fixed. Kiteworks F12 (single-source): fixed. Zimbra/Citrix F18: fixed.
- Declined Kiteworks F16 (priority high): acceptable. An unauthenticated CVSS 10.0 chain to root across all EPG versions before 9.4.1, in a gateway product marketed to government and with nearly 400 exposed instances (BleepingComputer), clears the exposure bar even without exploitation; the record's stated reason ('same vendor's product that law enforcement had warned about') is an association the entry itself says no source supports and should be dropped from the rationale.
- F11 items: em dashes removed (none remain outside the update headings); UAT/KillSwitch headlines fixed; Zimbra quote translated with original and update_of removed; Citrix NCSC-CH statement replaced; FTAPI cut to two sentences; Belnet takeaway states its ground. Residuals: 'this entry' language, `slc.dll` in the UAT body, record-summary narration (F11 #19 to #21).

### Citation does not support the claim

- **#1** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` / CVE-2026-88771 Citrix NetScaler: evidence-capture sequence: quote: capture logs, a configuration snapshot, a support bundle and a core dump (body Detection paragraph; also immediate_action and actions[0])  
  The cited watchTowr FAQ says 'Capture logs, a snapshot, a support bundle and a core dump'; Unit 42 and Citrix KB CTX694799 say 'Snapshot of Potentially Compromised NetScaler ADC VPX Instance' (an instance/VM snapshot; the configuration is captured by the support bundle). 'configuration snapshot' mislabels it and can lead a defender to take a config backup instead of the instance snapshot. Fix: 'an instance snapshot (VPX) where virtual' in the three places.
- **#2** `2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan` / Attribution paragraph: 54 Azure IP addresses: quote: of 54 distinct Azure IP addresses used in the UNCTAD-related scanning and a related wiki page, 45 also made edits on DSEWiki  
  swarmcha.se: 'of the 54 Azure IP addresses used to make this page and other UNCTAD-related edits and searches, 45 of them also made edits on DseWiki' (wiki access logs); SiliconANGLE: '54 ... Azure addresses tied to UNCTAD-related edits and searches on FractalWiki'. The 54 addresses are wiki-edit and search addresses, not the addresses that scanned the UNCTAD API (that traffic went through Urlquery). Fix: 'used for UNCTAD-related edits and searches on FractalWiki'.
- **#3** `2026-08-31/france-sdis-fire-rescue-data-leak-campaign` / summary, Gard body sentence and record summary: dropped hedges: quote: SDIS du Gard's board president confirmed the intrusion and theft of personnel identity-document copies and bank details; ... including patient rescue forms holding medical data and copies of identity documents  
  (low confidence) Objectif Gard: the president confirms 'l'attaque informatique ainsi que le vol de données personnelles concernant les personnels'; 'Parmi les informations dérobées figureraient ... des copies de pièces d'identité et des coordonnées bancaires' is a conditional journalist statement, and the entry's own evidence quote keeps 'are said to be'. ICI: the forms 'peuvent contenir' medical data and ID copies and the extent is 'encore en cours d'identification'. Summary, body and record summary state both as confirmed. Restore the hedges.
- **#6** `2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev` / Exposure line: quote: fixed releases exist for every release train  
  (low confidence) Cisco's table: 'Earlier than 20.9: Migrate to a fixed release'; trains before 20.9 have no fixed release. Say 'for 20.9 and later trains; earlier releases must migrate'.
- **#7** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` / disclosure-path paragraph (BleepingComputer clause): quote: NetScaler administrators reported being told by IT suppliers and security teams to shut appliances down ..., tracing to a pre-notification NCSC-NL reportedly sent to its constituency  
  (low confidence) BleepingComputer reports the admin shutdown calls and, separately, that NCSC-NL 'reportedly sent a pre-notification'; it does not say the shutdown advice traces to that notice (the watchTowr FAQ states 'following a private pre-notification'). Cite watchTowr for the link or soften.
- **#8** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` / opening paragraph: quote: CISO Frank Balonis told Heise Online the company "received credible threat intelligence from law enforcement ..."  
  (low confidence) heise: 'In an email obtained by heise security, the KiteWorks CISO urges its customers...'; the quote is from the CISO's customer email, not a statement to heise. Say 'wrote to customers in an email obtained by Heise'.
- **#9** `2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan` / Asymmetric sentence in the 2026-10-02 section: quote: access to pre-production staging systems of the Australian Institute of Health and Welfare, Data USA, IHME and UNCTAD whose returned data it believes was all public  
  (low confidence) Asymmetric: 'access to pre-production staging environments, including AIHW's pre-production system; some of these requests returned data. As far as we know, this data was all publicly available'; Data USA, IHME and UNCTAD appear only as 'similar activity targeting pre-production or staging environments'. The access and the all-public belief are stated for AIHW only.
- **#10** `2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan` / Transluce sentence in the 2026-10-02 section: quote: does not confidently attribute the new cases to OpenAI although the tactics match activity it attributed to OpenAI earlier  
  (low confidence) Transluce says 'We do not confidently attribute these attempts to OpenAI' of the Library and Archives Canada attempts and 'we are not attributing this traffic as a whole to OpenAI' of the broader state/federal workflows; for the Dept of Education case it notes 'more than 10,000 requests included a tag beginning with oai'. Scope the sentence to the cases Transluce qualifies.
- **#11** `2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities` / Lucerne source record date: quote: url: https://www.kantonale-verwaltung.lu.ch/datenschutz, date: "2016-11-26"  
  (low confidence) The page carries no dateline or meta date; 2016-11-26 is the date of the cantonal IT-security ordinance cited in its text, and the sourcing_note itself says the page is undated. The record date misstates the source's publication date (check 2e); use null or the retrieval date.

### Unsupported / hallucinated facts

- **#4** `2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan` / sourcing_note and verification after the 2026-10-02 update (supersession, check 4c(h)): quote: Rowan Howard-Jones is the sole independent assessor ... this is one assessor across two publishers, not multi-source corroboration. (verification: single-source)  
  The update added Transluce (own report, 2026-09-30), Asymmetric Security (own 48-hour investigation, 2026-10-01, which also reports UNCTAD staging activity) and the Canadian Cyber Centre as primary sources, so 'sole independent assessor' is no longer true for the entry; neither field is in the record's fields list. Revise sourcing_note and verification (or declare the change).
- **#12** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` / Defender takeaway and actions[0]: quote: the vendor has not said whether the critical flaw it found during the shutdown needs customer-side action on self-hosted instances  
  (low confidence) Kiteworks' own advisory page (the 2026-09-27 notice cited in the entry) says 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance.' The entry quotes the two sentences before it and omits this one. State the vendor's pointer for self-hosted Advanced Forms and keep the written question for the rest.
- **#13** `run-record` / runs/2026-10-02/2026-10-02T0404Z-intel.md, Updates (5) paragraph: quote: the 2026-09-30 advisory set names a CVSS 10.0 pre-auth Email Protection Gateway flaw, CVE-2026-54154, and four further CVEs  
  After the iteration-1 remediation the Kiteworks entry's cves[] carries CVE-2026-54154 plus seven further CVEs (85065, 85066, 102115, 102149, 102147, 102142, 102150); the note still carries the old count 'four further'. Correct the note.

### Claims missing inline citation

- **#14** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` / Defender takeaway: quote: NetScaler Gateway is a widely deployed perimeter VPN and remote-access layer across European public-sector networks  
  (low confidence) No cited source states European public-sector prevalence (watchTowr: 'sit at the edge of enterprise networks'; GTIG names government among likely impacted sectors; Censys gives country shares). Cite or reword.

### Drop (low relevance / off-audience / duplicate)

- **#17** `2026-10-02/adobe-campaign-classic-apsb26-142-134-unauth-cvss10` / priority notable, 3 CVE-record groups: quote: Adobe is not aware of exploitation and none of the CVEs is in CISA KEV  
  (low confidence) Check 11: a vulnerability entry should demand action beyond the regular patch cycle. Not exploited, not in KEV, no public PoC, a marketing-automation product with no shown public-sector or Swiss footprint; the entry sits on Adobe's bulletin alone (fourth Campaign Classic entry in two months). Consider shortening to a changelog record on the existing Campaign Classic entry or dropping.

### Needs more research

- **#18** `2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited` / behaviour paragraph: quote: an interpreter or utility process whose parent is the Zimbra mail or notification component  
  (low confidence) Microsoft's hunting logic gives the concrete lineage: a shell (sh/bash/dash) created by Perl running a generated .swatchdog_script, with snmptrap and shell metacharacters in the command line. The paragraph stays at 'notification component' although the injection signature was added; a Tier 2 detection writer needs the swatchdog/Perl parent.

### Editorial / less-is-more flags (advisory)

- **#19** `2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments` / body paragraph 2: quote: that binary sideloads `slc.dll`, which is Antino  
  Iteration 1 removed the implant file name from Detection; the body still names it (Talos: 'slc.dll (Antino C2 implant)'), a file-name indicator the style rule excludes. The behaviour (signed ADK binary loading an unexpected sibling DLL) carries the detection without it.
- **#20** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev; 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` / 'this entry' composition language in earlier sections: quote: matching this entry's existing table (Citrix 2026-09-29 section); the discrepancy is noted here rather than silently corrected ... this entry's original sources ... not withheld by this entry (Kiteworks 2026-09-29 section)  
  Check 12 lists 'this entry' as workflow language; iteration 1 asked for it to be removed together with the inherited em dashes, and only the em dashes were removed. Body sections may be revised (changelog record required); the Citrix record summary of 2026-09-29 is append-only.
- **#21** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning; 2026-08-31/france-sdis-fire-rescue-data-leak-campaign; 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan; 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited` / changelog record summaries carry record-keeping narration: quote: the verification field moves to single-source (Kiteworks); Inherited em dashes in the summary and body are also removed (SDIS 66); names the reader-proxy class instead of one product (UNCTAD); (the earlier figure matched no current source) (Zimbra)  
  Record summaries are reader-facing changelog text. Field names and housekeeping ('verification field', 'inherited em dashes', 'reader-proxy class') are workflow narration; state the reader-relevant change (e.g. 'sourcing now rests on the vendor alone') or mark the metadata-only part internal.
- **#22** `2026-10-02 (Cisco, FortiMail, Zammad) and 2026-09-26 Kiteworks` / entity linking: quote: entities: [] on the Cisco, FortiMail and Zammad entries; entities: ["product:kiteworks"] only on Kiteworks  
  The run registered product:cisco-catalyst-sd-wan-manager, product:fortinet-fortimail, product:zammad, product:kiteworks-core, product:kiteworks-email-protection-gateway and product:kiteworks-secure-data-forms, but no entry links them, so the product pages stay empty. Add the keys to the entries' entities.

### Analytical-link-as-fact

- **#5** `2026-08-31/france-sdis-fire-rescue-data-leak-campaign` / title: quote: hits seven more units, with confirmations from SDIS du Gard and from SDIS 66, whose stolen patient rescue forms forced crews back to paper and radio  
  SDIS 66 is not one of the seven units and the entry's own section says 'no source links the SDIS 66 theft to the SDIS du Gard attack or to the forum claims against other units'; ICI only notes timing ('un mois apres'). The title presents SDIS 66 as a confirmation within the wave. Reword so the SDIS 66 theft is stated as a separate confirmed incident. (The declined F7 split is acceptable once the title stops implying the link.)

### Org-triage line missing / inconsistent

- **#15** `2026-10-02/belnet-supplier-zero-day-mail-copied-65-days` / priority notable, four paragraphs: quote: priority: notable; 'Belnet publishes no technique or indicator and names neither the flaw nor the product'  
  (low confidence) Check 5b: an incident with no access vector beyond 'a zero-day in an unnamed supplier's technology', no actor and no behaviour beyond its impact is routine and two sentences at most, or dropped. The takeaway now states a ground (shared-service supplier-zero-day pattern) but the entry gives a responder nothing to hunt. Lower to routine and shorten, or justify notable with a concrete transferable detail.

### Action-item discipline

- **#16** `2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev` / actions[1]: quote: search serviceproxy-access.log and vmanage-server.log for percent-encoded login-path requests and viptela-reserved- usernames from unknown addresses, run request admin-tech, and open a Severity 3 Cisco TAC case  
  (low confidence) Check 10b(b): restates the Detection paragraph's log names and TAC procedure; the same pattern was fixed for the Zimbra and Citrix actions in this run. Keep the task ('run the compromise check on every Manager that was internet-reachable before the upgrade') and point to the body.

### Missed angles

None found. Probed with six searches (Swiss communal and cantonal incidents, KEV and zero-day additions around 2026-09-30 to 2026-10-01, heise exploitation reports, BACS warnings): Manno/SafePay, SharePoint CVE-2026-65660, Roundcube CVE-2026-48842, the September Windows zero-days and the Apple CoreGraphics KEV entry are all already in the store; TeamViewer's 2026-10-01 fixes carry no exploitation report. Coverage looks complete for critical and high signal.

### Verdict

NEEDS_FIXES (truth: 13, editorial: 5, advisory: 4)

Most weight: F3 #1 (Citrix 'configuration snapshot', three places), F3 #2 (UNCTAD 54 addresses), F3 #3 (SDIS hedges), F4 #4 (UNCTAD sourcing_note stale after the update), F13 #5 (SDIS title), F4 #13 (run-record count). The remaining truth items are low-confidence adjacency and attribution nits that a one-clause edit resolves. All 10 new entries and the 5 updates otherwise verify against the live sources (CVE ids, CVSS, versions, KEV dates, EPSS, quotes).

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev
  item: "CVE-2026-88771 Citrix NetScaler: evidence-capture sequence"
  url_or_quote: "capture logs, a configuration snapshot, a support bundle and a core dump (body Detection paragraph; also immediate_action and actions[0])"
  summary: "The cited watchTowr FAQ says 'Capture logs, a snapshot, a support bundle and a core dump'; Unit 42 and Citrix KB CTX694799 say 'Snapshot of Potentially Compromised NetScaler ADC VPX Instance' (an instance/VM snapshot; the configuration is captured by the support bundle). 'configuration snapshot' mislabels it and can lead a defender to take a config backup instead of the instance snapshot. Fix: 'an instance snapshot (VPX) where virtual' in the three places."
- code: F3
  category: claim-not-supported
  section: 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
  item: "Attribution paragraph: 54 Azure IP addresses"
  url_or_quote: "of 54 distinct Azure IP addresses used in the UNCTAD-related scanning and a related wiki page, 45 also made edits on DSEWiki"
  summary: "swarmcha.se: 'of the 54 Azure IP addresses used to make this page and other UNCTAD-related edits and searches, 45 of them also made edits on DseWiki' (wiki access logs); SiliconANGLE: '54 ... Azure addresses tied to UNCTAD-related edits and searches on FractalWiki'. The 54 addresses are wiki-edit and search addresses, not the addresses that scanned the UNCTAD API (that traffic went through Urlquery). Fix: 'used for UNCTAD-related edits and searches on FractalWiki'."
- code: F3
  category: claim-not-supported
  section: 2026-08-31/france-sdis-fire-rescue-data-leak-campaign
  item: "summary, Gard body sentence and record summary: dropped hedges"
  url_or_quote: "SDIS du Gard's board president confirmed the intrusion and theft of personnel identity-document copies and bank details; ... including patient rescue forms holding medical data and copies of identity documents"
  summary: "(low confidence) Objectif Gard: the president confirms 'l'attaque informatique ainsi que le vol de données personnelles concernant les personnels'; 'Parmi les informations dérobées figureraient ... des copies de pièces d'identité et des coordonnées bancaires' is a conditional journalist statement, and the entry's own evidence quote keeps 'are said to be'. ICI: the forms 'peuvent contenir' medical data and ID copies and the extent is 'encore en cours d'identification'. Summary, body and record summary state both as confirmed. Restore the hedges."
- code: F4
  category: hallucinated-fact
  section: 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
  item: "sourcing_note and verification after the 2026-10-02 update (supersession, check 4c(h))"
  url_or_quote: "Rowan Howard-Jones is the sole independent assessor ... this is one assessor across two publishers, not multi-source corroboration. (verification: single-source)"
  summary: "The update added Transluce (own report, 2026-09-30), Asymmetric Security (own 48-hour investigation, 2026-10-01, which also reports UNCTAD staging activity) and the Canadian Cyber Centre as primary sources, so 'sole independent assessor' is no longer true for the entry; neither field is in the record's fields list. Revise sourcing_note and verification (or declare the change)."
- code: F13
  category: analytical-link-as-fact
  section: 2026-08-31/france-sdis-fire-rescue-data-leak-campaign
  item: "title"
  url_or_quote: "hits seven more units, with confirmations from SDIS du Gard and from SDIS 66, whose stolen patient rescue forms forced crews back to paper and radio"
  summary: "SDIS 66 is not one of the seven units and the entry's own section says 'no source links the SDIS 66 theft to the SDIS du Gard attack or to the forum claims against other units'; ICI only notes timing ('un mois apres'). The title presents SDIS 66 as a confirmation within the wave. Reword so the SDIS 66 theft is stated as a separate confirmed incident. (The declined F7 split is acceptable once the title stops implying the link.)"
- code: F3
  category: claim-not-supported
  section: 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev
  item: "Exposure line"
  url_or_quote: "fixed releases exist for every release train"
  summary: "(low confidence) Cisco's table: 'Earlier than 20.9: Migrate to a fixed release'; trains before 20.9 have no fixed release. Say 'for 20.9 and later trains; earlier releases must migrate'."
- code: F3
  category: claim-not-supported
  section: 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev
  item: "disclosure-path paragraph (BleepingComputer clause)"
  url_or_quote: "NetScaler administrators reported being told by IT suppliers and security teams to shut appliances down ..., tracing to a pre-notification NCSC-NL reportedly sent to its constituency"
  summary: "(low confidence) BleepingComputer reports the admin shutdown calls and, separately, that NCSC-NL 'reportedly sent a pre-notification'; it does not say the shutdown advice traces to that notice (the watchTowr FAQ states 'following a private pre-notification'). Cite watchTowr for the link or soften."
- code: F3
  category: claim-not-supported
  section: 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning
  item: "opening paragraph"
  url_or_quote: "CISO Frank Balonis told Heise Online the company \"received credible threat intelligence from law enforcement ...\""
  summary: "(low confidence) heise: 'In an email obtained by heise security, the KiteWorks CISO urges its customers...'; the quote is from the CISO's customer email, not a statement to heise. Say 'wrote to customers in an email obtained by Heise'."
- code: F3
  category: claim-not-supported
  section: 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
  item: "Asymmetric sentence in the 2026-10-02 section"
  url_or_quote: "access to pre-production staging systems of the Australian Institute of Health and Welfare, Data USA, IHME and UNCTAD whose returned data it believes was all public"
  summary: "(low confidence) Asymmetric: 'access to pre-production staging environments, including AIHW's pre-production system; some of these requests returned data. As far as we know, this data was all publicly available'; Data USA, IHME and UNCTAD appear only as 'similar activity targeting pre-production or staging environments'. The access and the all-public belief are stated for AIHW only."
- code: F3
  category: claim-not-supported
  section: 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
  item: "Transluce sentence in the 2026-10-02 section"
  url_or_quote: "does not confidently attribute the new cases to OpenAI although the tactics match activity it attributed to OpenAI earlier"
  summary: "(low confidence) Transluce says 'We do not confidently attribute these attempts to OpenAI' of the Library and Archives Canada attempts and 'we are not attributing this traffic as a whole to OpenAI' of the broader state/federal workflows; for the Dept of Education case it notes 'more than 10,000 requests included a tag beginning with oai'. Scope the sentence to the cases Transluce qualifies."
- code: F3
  category: claim-not-supported
  section: 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities
  item: "Lucerne source record date"
  url_or_quote: "url: https://www.kantonale-verwaltung.lu.ch/datenschutz, date: \"2016-11-26\""
  summary: "(low confidence) The page carries no dateline or meta date; 2016-11-26 is the date of the cantonal IT-security ordinance cited in its text, and the sourcing_note itself says the page is undated. The record date misstates the source's publication date (check 2e); use null or the retrieval date."
- code: F4
  category: hallucinated-fact
  section: 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning
  item: "Defender takeaway and actions[0]"
  url_or_quote: "the vendor has not said whether the critical flaw it found during the shutdown needs customer-side action on self-hosted instances"
  summary: "(low confidence) Kiteworks' own advisory page (the 2026-09-27 notice cited in the entry) says 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance.' The entry quotes the two sentences before it and omits this one. State the vendor's pointer for self-hosted Advanced Forms and keep the written question for the rest."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-10-02/2026-10-02T0404Z-intel.md, Updates (5) paragraph"
  url_or_quote: "the 2026-09-30 advisory set names a CVSS 10.0 pre-auth Email Protection Gateway flaw, CVE-2026-54154, and four further CVEs"
  summary: "After the iteration-1 remediation the Kiteworks entry's cves[] carries CVE-2026-54154 plus seven further CVEs (85065, 85066, 102115, 102149, 102147, 102142, 102150); the note still carries the old count 'four further'. Correct the note."
- code: F5
  category: missing-citation
  section: 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev
  item: "Defender takeaway"
  url_or_quote: "NetScaler Gateway is a widely deployed perimeter VPN and remote-access layer across European public-sector networks"
  summary: "(low confidence) No cited source states European public-sector prevalence (watchTowr: 'sit at the edge of enterprise networks'; GTIG names government among likely impacted sectors; Censys gives country shares). Cite or reword."
- code: F16
  category: org-triage
  section: 2026-10-02/belnet-supplier-zero-day-mail-copied-65-days
  item: "priority notable, four paragraphs"
  url_or_quote: "priority: notable; 'Belnet publishes no technique or indicator and names neither the flaw nor the product'"
  summary: "(low confidence) Check 5b: an incident with no access vector beyond 'a zero-day in an unnamed supplier's technology', no actor and no behaviour beyond its impact is routine and two sentences at most, or dropped. The takeaway now states a ground (shared-service supplier-zero-day pattern) but the entry gives a responder nothing to hunt. Lower to routine and shorten, or justify notable with a concrete transferable detail."
- code: F18
  category: action-item-discipline
  section: 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev
  item: "actions[1]"
  url_or_quote: "search serviceproxy-access.log and vmanage-server.log for percent-encoded login-path requests and viptela-reserved- usernames from unknown addresses, run request admin-tech, and open a Severity 3 Cisco TAC case"
  summary: "(low confidence) Check 10b(b): restates the Detection paragraph's log names and TAC procedure; the same pattern was fixed for the Zimbra and Citrix actions in this run. Keep the task ('run the compromise check on every Manager that was internet-reachable before the upgrade') and point to the body."
- code: F7
  category: drop
  section: 2026-10-02/adobe-campaign-classic-apsb26-142-134-unauth-cvss10
  item: "priority notable, 3 CVE-record groups"
  url_or_quote: "Adobe is not aware of exploitation and none of the CVEs is in CISA KEV"
  summary: "(low confidence) Check 11: a vulnerability entry should demand action beyond the regular patch cycle. Not exploited, not in KEV, no public PoC, a marketing-automation product with no shown public-sector or Swiss footprint; the entry sits on Adobe's bulletin alone (fourth Campaign Classic entry in two months). Consider shortening to a changelog record on the existing Campaign Classic entry or dropping."
- code: F8
  category: needs-more-research
  section: 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited
  item: "behaviour paragraph"
  url_or_quote: "an interpreter or utility process whose parent is the Zimbra mail or notification component"
  summary: "(low confidence) Microsoft's hunting logic gives the concrete lineage: a shell (sh/bash/dash) created by Perl running a generated .swatchdog_script, with snmptrap and shell metacharacters in the command line. The paragraph stays at 'notification component' although the injection signature was added; a Tier 2 detection writer needs the swatchdog/Perl parent."
- code: F11
  category: editorial-advisory
  section: 2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments
  item: "body paragraph 2"
  url_or_quote: "that binary sideloads `slc.dll`, which is Antino"
  summary: "Iteration 1 removed the implant file name from Detection; the body still names it (Talos: 'slc.dll (Antino C2 implant)'), a file-name indicator the style rule excludes. The behaviour (signed ADK binary loading an unexpected sibling DLL) carries the detection without it."
- code: F11
  category: editorial-advisory
  section: 2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev; 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning
  item: "'this entry' composition language in earlier sections"
  url_or_quote: "matching this entry's existing table (Citrix 2026-09-29 section); the discrepancy is noted here rather than silently corrected ... this entry's original sources ... not withheld by this entry (Kiteworks 2026-09-29 section)"
  summary: "Check 12 lists 'this entry' as workflow language; iteration 1 asked for it to be removed together with the inherited em dashes, and only the em dashes were removed. Body sections may be revised (changelog record required); the Citrix record summary of 2026-09-29 is append-only."
- code: F11
  category: editorial-advisory
  section: 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning; 2026-08-31/france-sdis-fire-rescue-data-leak-campaign; 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan; 2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited
  item: "changelog record summaries carry record-keeping narration"
  url_or_quote: "the verification field moves to single-source (Kiteworks); Inherited em dashes in the summary and body are also removed (SDIS 66); names the reader-proxy class instead of one product (UNCTAD); (the earlier figure matched no current source) (Zimbra)"
  summary: "Record summaries are reader-facing changelog text. Field names and housekeeping ('verification field', 'inherited em dashes', 'reader-proxy class') are workflow narration; state the reader-relevant change (e.g. 'sourcing now rests on the vendor alone') or mark the metadata-only part internal."
- code: F11
  category: editorial-advisory
  section: 2026-10-02 (Cisco, FortiMail, Zammad) and 2026-09-26 Kiteworks
  item: "entity linking"
  url_or_quote: "entities: [] on the Cisco, FortiMail and Zammad entries; entities: [\"product:kiteworks\"] only on Kiteworks"
  summary: "The run registered product:cisco-catalyst-sd-wan-manager, product:fortinet-fortimail, product:zammad, product:kiteworks-core, product:kiteworks-email-protection-gateway and product:kiteworks-secure-data-forms, but no entry links them, so the product pages stay empty. Add the keys to the entries' entities."
```
