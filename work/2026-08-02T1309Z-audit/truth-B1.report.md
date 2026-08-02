# Retrospective audit — truth pass, batch B1

**Model:** Opus 5 (`claude-opus-5`)
**Run:** 2026-08-02T1309Z-audit · window 2026-07-26T13:08:25Z → 2026-08-02T13:09:58Z
**Scope:** 20 published entries (2026-07-26 → 2026-07-29)
**Counts:** clean 17 · imprecision 2 · factual-error 1
**Primary/authority URLs fetched this pass:** 42 (incl. the CISA KEV catalog via `tools/fetch_source.py cisa-kev`); every cited source on all 20 entries was retrieved. `advisories.ncsc.nl` returned a redirect shell through the bridge and was recovered via the jina reader (last-resort rung).
**Mechanical checks run:** every `techniques[]` id in all 20 entries resolved against the pinned `attack/enterprise-attack.json` (v19.1) — all 62 ids present, none revoked or deprecated; every `cves[]` id with a KEV/exploitation claim checked against the live KEV catalog.

---

## Method notes

- Evidence quotes were checked as **contiguous normalised substrings** of the fetched page text (whitespace/typographic normalisation only; markdown emphasis markers in source text were stripped before comparison). No quote in this batch failed that test.
- Version boundaries were read from **structured** vendor fields where available: Siemens CSAF `product_status` / `remediations`, Oracle's Fusion Middleware risk-matrix rows, Fortinet's version/solution table, PTC's dated change log, IBM's "Affected Products and Versions" block.
- Where a source could only be partially rendered (XLab's Chinese-language report, 7.7 KB of an 11-minute read), only the facts actually visible were treated as verified; nothing was flagged on the basis of my own fetch shortfall.

---

## Findings

### 1. `entries/2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave.md` — factual-error (machine surface)

**(a) `cves[]` type for CVE-2026-62415 contradicts the discloser.**
Entry: `- id: CVE-2026-62415 … type: rce`.
mySites.guru (the cited page for that CVE): *"One piece of nuance to that critical rating: on a default configuration the practical impact is anonymous file writes constrained to image and document types, which is serious but not a web shell. It rises to unauthenticated remote code execution only on a site whose allowed file types have been widened to include an executable type."* The page also records the vendor's `"not a remote code execution vulnerability"` claim as *"a fair description of the shipped defaults"*. `type: rce` is the default-configuration case inverted; `file-upload` / `unrestricted-upload` is what the authority supports.

**(b) Attribution of the Membership Pro disclosure to the mySites.guru campaign.**
Entry summary: *"The mySites.guru research campaign against Joomla third-party extensions produced six further disclosures between 2026-07-20 and 2026-07-23"*; body: *"The rest of the week's batch is the same research campaign continuing on its original axis"*, listing Membership Pro among them.
Source: *"We did not discover or report the Membership Pro flaw. We reported the identical anonymous upload flaw in Events Booking, which carries CVE-2026-60024 and CVE-2026-60025. The Membership Pro issue is now tracked separately as CVE-2026-62415."* Five disclosures, not six; the sixth is a read-across post.

**(c) CVSS-version and score-presence claims in `sourcing_note`.**
Entry: *"Scores are CVSS 4.0: the three EasyStore values are the Joomla CNA's … and Events Booking carries none."*
Membership Pro page: *"9.1 critical (CVSS 3.1, AV:N/AC:L/PR:N/UI:N/C:H/I:H/A:N)"* — so the blanket "CVSS 4.0" is wrong for CVE-2026-62415.
Events Booking page: *"Our assessment is CVSS 4.0 8.7 (High), vector AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:N/SI:N/SA:N … The Joomla CNA published CVE-2026-63047 for the flaw on 22 July 2026 without a score of its own, so this assessment stands."* A discloser score of 8.7 exists; `cvss: null` drops it.

**Verified correct on this entry (recorded so remediation does not overreach):** the Gridbox evidence quote is verbatim ("A critical unauthenticated authentication bypass in Gridbox let anyone become a Super User on a Joomla site by setting a single browser cookie"); the 10.0 / CVSS 4.0 / "our own assessment" framing matches the page's Disclosure-and-Severity block; CVE-2026-61425 assigned via the Joomla CNA; fixed in 2.20.1 released 20 July 2026; previous release 2.20.0.2 of 21 October 2025 (the page's own "at least nine months, and probably far longer" is slightly stronger than the entry's "shipped since the October 2025 release", but the entry's nine-month figure matches); all three EasyStore CVE↔score↔vector pairings (65759/8.7 order forgery, 65760/9.2 IDOR, 65761/9.3 SQLi) match the CNA table exactly; the EasyStore order-repayment evidence quote is verbatim; fixed versions 2.0.2 / 5.8.2 / 4.6.2 all correct; the "The vendor called it 'not a critical security issue.' The Joomla CNA disagreed" body quote is verbatim.

### 2. `entries/2026-07-28/cve-2025-68686-fortios-ssl-vpn-symlink-persistence-kev.md` — imprecision (machine surface)

`cves[].cvss: "5.9"`. The cited per-CVE authority (FG-IR-25-934) displays, in its own fields, `Severity Medium … Known Exploited No … CVSSv3 Score 5.3`. No cited source in the entry carries 5.9. The `sourcing_note` transparently explains the divergence (5.3 = temporal-adjusted `E:P/RL:O/RC:C` over the same base vector, whose base value is 5.9) and that reasoning is internally coherent, but the vector string itself was not present in the fetched page body, so the base score rests on an authority the entry does not cite. Recording as imprecision rather than error: the number is defensible, its provenance is not sourced.

Everything else on this entry verified exactly against Fortinet: all three PSIRT evidence quotes verbatim; the version table (`7.6.0 through 7.6.1 → 7.6.2 or above`, `7.4.0 through 7.4.6 → 7.4.7 or above`, `7.2 / 7.0 / 6.4 all versions → migrate to a fixed release`); `Virtual Patch … FMWP db update 26.033`; `Products that never had SSL-VPN enabled, are not impacted`; the "Known Exploited: No" / last-updated-2026-03-12 staleness the sourcing_note calls out; and CISA KEV `CVE-2025-68686 / Fortinet / FortiOS / dateAdded 2026-07-27`.

### 3. `entries/2026-07-26/ifage-geneva-dragonforce-data-published-student-records.md` — imprecision (machine surface)

**(a)** `techniques: [T1657, T1567.002]`. T1567.002 is *Exfiltration to Cloud Storage*; no behavior in the body and nothing in either cited source describes exfiltration to a cloud-storage service. The body itself states *"Nothing in the reporting identifies the initial-access vector"*, and the only described attacker action beyond extortion is leak-site publication. The mapping is unevidenced.
**(b)** Summary: *"multi-year student exam results running to 2026"*. 20 minutes attributes the multi-year span to documents in general — *"D'après un expert sollicité par le quotidien, des milliers de documents, sur plusieurs années, jusqu'en 2026, ont ainsi été dévoilés"* — not to exam results specifically. The body states this correctly; the summary tightens it beyond the source.
**(c)** Summary: *"it has filed a criminal complaint and is working with cantonal police and federal authorities"*. Source: *"Révélée par la « Tribune de Genève », cette cyberattaque fait l'objet d'une plainte pénale. L'enquête est menée par la police cantonale, Fedpol (police fédérale) et les autorités judiciaires."* The complainant is not named.

All four `evidence[]`-relevant French quotations in the body (publication contents, employees-and-beneficiaries scope, the ransom-demand contradiction pair) are verbatim, and the `verification: contradicted` / Contradiction paragraph is a fair statement of what the two sources say.

---

## Clean entries — what was actually checked

| Entry | Authority evidence |
|---|---|
| `ancpi-romania-dnsc-report-2m-epayment-records-exfiltrated` | All four Romanian evidence quotes verbatim in psnews.ro / go4it.ro; the GitLab source-code theft (eTerra, GIS, ePayment, security modules) and the seven-minute WAF log retention both present in the cited pages; five techniques valid. |
| `fakeagent-claude-artifact-lure-sectoprat-dll-sideloading` | All three Huntress quotes verbatim; "at least 29 organizations", SectopRAT, JetBrains CEF + IBM SPSS side-loading, EtherHiding/Ethereum C2 all in the Huntress post; the 7,100 page-view figure present in the cited Help Net Security article. |
| `langflow-1-10-2-required-cve-2026-0770-precondition-fix` | IBM bulletin: CVE-2026-14499 description verbatim, CVSS 8.8, "Langflow OSS 1.0.0-1.10.1", "upgrading Langflow OSS to version 1.10.2". ZDI-26-036: CVE-2026-0770, 9.8, "Authentication is not required to exploit this vulnerability", `exec_globals`/validate endpoint, mitigation sentence verbatim, dated 2026-01-09. |
| `oracle-july-2026-cpu-fusion-middleware-cvss10-unauth` | Oracle CPU page parsed row-by-row: 355 new FMW patches / 219 unauthenticated verbatim; **exactly 10 rows at base 10.0 across 9 distinct CVE ids**, with CVE-2026-60365 duplicated under Oracle HTTP Server and the WebLogic Server Proxy Plug-in — the entry's central reconciliation is correct. CVE-2026-47056 (Data Integrator Rest Service, HTTP, 12.2.1.4.0 / 14.1.2.0.0), CVE-2026-60217 (Coherence Core, TCP, four versions) and CVE-2026-61211 (RDBMS DBMS_CLOUD, 9.9, "Exploit without Auth? No") all match the matrix. The nine component families named in the action item match the nine 10.0 rows. NCSC-NL's page could not be retrieved through the bridge (redirect shell), so the Dutch quote is unverified — not counted as a defect. |
| `rapid7-exposed-webdav-delivery-lab-cve-2025-33053-clickfix` | Every quantifier present in the Rapid7 post: 1,048 / 453 / 236 / 146 / 89 / 2,384, plus PureRAT, Mexico, CVE-2025-33053, `search-ms`, and both evidence quotes ("the attacker used LLMs to operate more like a modern software product team", "NO SmartScreen, NO MoTW warnings!"). CVE-2025-33053 confirmed in KEV (Microsoft Windows, added 2025-06-10), consistent with `status: [exploited, patch-available]`. |
| `teleshim-bindcloak-volume-serial-keying-government-espionage` | All three Zscaler quotes verbatim including the full moderate-to-high-confidence attribution sentence; `RegSchdTask.exe`, `AsTaskSched.dll`, `shimgen.exe`, MIXEDKEY, BINDCLOAK and volume-serial keying all present. `verification: single-source` is honest. |
| `wp2shell-cve-2026-63030-60137-confirmed-exploited-kev` | Rapid7 quotes verbatim including "both CVEs were added to CISA's Known Exploited Vulnerabilities (KEV) catalog on July 21"; independently confirmed in the live KEV catalog — **both** CVE-2026-63030 and CVE-2026-60137, WordPress Core, dateAdded 2026-07-21. Version boundaries 6.9.4/7.0.1 → 6.9.5/7.0.2 present. |
| `clop-windchill-flexplm-mass-extortion-wave-cve-2026-12569` | PTC change log verified date-by-date: `6/18/2026 at 10:25 AM ET Patch for Windchill version 13.0.2 now available`; `6/19/2026 at 10:30 PM ET Patches for Windchill versions 11.0. M030 and 13.1.1 now available`; `7/14/2026 … SUPs: 13.1.3, 13.1.2; CPSXB Stand-Alone Patches: 13.1.1, 13.0.2, 12.1.2, 12.0.2, 11.2.1, 11.1 M020, 11.0 M030` — the entry's `fixed` string reproduces this exactly, and 14 July is indeed the first *release* naming FlexPLM. eSupport CS473270 confirmed as the authoritative per-version list. KEV: CVE-2026-12569, PTC Windchill and FlexPLM, dateAdded 2026-06-25, ransomware use "Known" — matching the body's "CISA's KEV confirmation on 25 June". |
| `cve-2026-16723-fastjson-1x-spring-boot-fat-jar-rce-no-patch` | Maintainer advisory: the stock-default RCE sentence is verbatim (source renders "stock default configuration" in bold; the entry's plain-text rendering is the same contiguous string); `1.2.83_noneautotype`, SafeMode and the Kirill Firsov / FearsOff credit all present. CVE-2026-16723 correctly **absent** from KEV, consistent with `status: [exploited, no-patch, mitigation-only]` resting on Imperva telemetry only, as the sourcing_note states. |
| `cybernox-chat-control-doxing-french-eu-officials` | ZATAZ: both evidence quotes verbatim, the "24" figure, and all six named politicians (Morano, Glucksmann, Guetta, Loiseau, Canfin, Bellamy) present. The entry's careful separation of what ZATAZ says from what Cyberattaque.org says (the "Cybernox" handle, the second group, the unstated total) is reflected in the sourcing_note. |
| `cve-2026-16812-arista-velocloud-orchestrator-exploited` | Arista SA-0144: all three evidence quotes verbatim, CWE-78, 10.0, "privileged internal functionality", and the fixed builds 5.2.3.14 / 6.1.3.4 / 6.4.2.4 plus the 7.0.0.1 affected boundary. KEV: CVE-2026-16812, Arista VeloCloud Orchestrator, dateAdded 2026-07-27 — same day as the advisory, as claimed. `priority: critical` is earned (vendor-stated active exploitation + exposed-by-default + no configuration mitigation). |
| `cve-2026-61511-vbulletin-preauth-rce-public-exploit` | SSD advisory: both evidence quotes verbatim; `vB5_Template_Runtime::runMaths()` in `/includes/vb5/template/runtime.php`, the `preg_replace` allowlist feeding `@eval`, the "phpfuck" construction, `pagenav`, and the Vendor Response section linking **both** the 6.2.2 announcement and the 6.2.1/6.2.0/6.1.6 security-patch announcement without dates — exactly as the entry describes. SSD's "Affected Versions: vBulletin 6.2.1 and prior / vBulletin 6.1.6 and prior" matches the entry's characterisation of SSD's narrower range vs. the CNA range. Correctly absent from KEV. |
| `dysphoria-iot-botnet-ens-sns-c2-upnp-relay-mesh` | XLab report (partial render): the Chinese evidence quote 「该样本不再具备 DDoS 攻击功能，而是纯粹作为中继/代理节点运作」 is verbatim; "BOT数量超过20万" supports "exceeding 200,000 bots"; the jackskid/fbot lineage, ENS/SNS resolution and the ~155 UPnP port-forwarding rules all present. Scale figures held in the sourcing_note (4,401 / 239,000) fell outside the rendered portion and are neither confirmed nor contradicted. |
| `ey-itsm-breach-shinyhunters-attribution-claim` | BleepingComputer: both evidence quotes verbatim, including the explicit non-verification sentence; the 31 July deadline and the Experian identity-monitoring detail present. `verification: single-source` with credibility 3 is a correct reading of an uncorroborated actor claim. |
| `medusahvnc-hidden-desktop-browser-session-hijacking` | BlackFog: the browser-profile quote and the charmap.exe injection quote are both verbatim; ChaCha20 layer, "Browser Recovery" and the "Mem Exec" panel feature present. The sourcing_note's caveats (capability set derived from imports and sales material; AMSI/ETW as advertised rather than observed) match what the page actually supports. |
| `check-point-cve-2026-16232-sic-dn-substitution-root-cause` | Rapid7 Labs: **all four** evidence quotes verbatim, including the full FWM `gen-sso-token` authorization-shortcut sentence; Take 146 (vulnerable) and Take 158 (patched), the `CN=siclocal` loopback narrowing, and TCP 18190 / 19009 all present. `verification: single-source` and the carried Rapid7-vs-Check-Point Trusted-Clients contradiction are correctly surfaced rather than resolved. |
| `cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed` | Siemens CSAF SSA-734552 parsed as JSON: `product_status.known_affected` = Desigo CC family V7 (`vers:all/*`), family V8 (`vers:all/*`), family V9 (`vers:intdot/<9.0.1`); `remediations` = `none_available` / "Currently no fix is available", `vendor_fix` / "Update to V9.0 QU1 or later version", `vendor_fix` / "Update to patch V8.0 QU2.0021"; CVSS base score 9.8. Every structured value in the entry's `affected` and `fixed` strings matches the CSAF field-for-field, and both Siemens evidence quotes are verbatim. Correctly absent from KEV. |

---

## Second sweep — corroborating sources (all previously-unverified attributions now closed)

A second fetch round retrieved every remaining cited source. No new defects; the following attributions are now confirmed rather than assumed:

- **NCSC-2026-0252** (recovered via the jina reader): the Dutch evidence quote is verbatim, and the advisory's own prose reads *"Het totaal aantal kwetsbaarheden dat is verholpen in deze updates is 345. De ernstigste kwetsbaarheden, 9 stuks, hebben de hoogste score van 10.0 gekregen"* — confirming both halves of the Oracle entry's reconciliation (NCSC's nine-at-10.0 and its 345 total against Oracle's ten rows and 355). CVE-2026-47056 and CVE-2026-60217 both appear in NCSC's 10.0 list, as the entry states.
- **SecurityWeek (WP2Shell)**: the Hexastrike evidence quote is verbatim, and *"WatchTowr has also seen in-the-wild exploitation attempts"* supports the entry's watchTowr clause.
- **Ransom-ISAC**: both evidence quotes verbatim, and the entry's paraphrase of the delivery pattern tracks the source exactly — *"The extortion emails appear to originate from randomly compromised accounts, are sent to hundreds of users within an impacted organization and include Cl0p's latest contact information … This extortion approach is consistent with what we observed with the Oracle EBS campaign last year, except for the use of new email addresses."*
- **BleepingComputer (Cl0p)**: the ReliaQuest quote is verbatim, typo (`unconfirmed. however`) included.
- **Imperva**: both quotes verbatim; Singapore, Canada and the ~30% Ruby/Go tooling share all present.
- **Cyberattaque.org**: the evidence quote is verbatim (the page renders a space before the closing period around the bolded handle); the unstated-total sentence, the NIR mention and the loyalty-programme heterogeneity all present, as is the entry's caveat that the two-group split is the actor's own labelling.
- **VulnCheck (CNA)**: CVE-2026-61511, CVSS 9.3, CWE-95, `pagenav`, the `ajax/render` route and the 5.0.0–5.7.5 / 6.x affected range all confirmed — the entry's choice of the wider CNA range over SSD's narrower one is correctly sourced.
- **Karma(In)Security KIS-2026-13**: disclosure timeline reads `[30/06/2026] – Vendor released security patch` and `[01/07/2026] – Vendor released version 6.2.2`, exactly the two dates the entry attributes to it.
- **vBulletin vendor announcement**: *"Note: vBulletin Cloud has been already been patched."* verbatim; Patch Level 1 for 6.2.1 / 6.2.0 / 6.1.6 confirmed.
- **Fortinet PSIRT blog (2025-04-10)**: both symlink-persistence quotes verbatim, including the "even if the customer device was updated … may have been left behind" sentence.
- **SecurityWeek (MedusaHVNC)** and **BleepingComputer (FakeAgent)**: quoted/attributed claims confirmed.

---

## Residual coverage gaps in this pass (none material)

Every cited URL across the 20 entries was fetched and checked. The only partial retrieval was `blog.xlab.qianxin.com/dysphoria/`, which rendered roughly 7.7 KB of an 11-minute Chinese-language report: the evidence quote, the >200,000-bot figure (「BOT数量超过20万」), the jackskid/fbot lineage, ENS/SNS resolution and the ~155 UPnP rules were all verified in the rendered portion; the finer scale figures held in that entry's `sourcing_note` (4,401 in-China bots, 239,000 overseas peak, the 2026-06-25 relay-variant date) fell outside it and are neither confirmed nor contradicted — not counted as a defect, since a verifier's own fetch shortfall is not the entry's.
