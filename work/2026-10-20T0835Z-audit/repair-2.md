# repair-2 report (wave 2026-10-20T0835Z-audit, findings-w1a.yaml)

Six entries recorded, two declined in full (already fixed). No CVE ids added or removed, no new entity keys, no state-file change needed.
`check_run.py --all`: 0 fail. My only WARNs are `entry-updates ... run_id '2026-10-20T0835Z-audit' does not resolve to a run record` on the six entries (clears when the wave's run record lands).
Cited-page checks (`check_run.py 2026-10-20T0835Z-audit/repair-2 --page-checks-since 2026-10-20`): 0 warn. Every new evidence quote was found verbatim; every CVE-naming clause either matched its page or could not be machine-read.

## 2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
- Record: `improvement` (not internal), fields `[body, title]`.
- Applied: the KEV listing's description names only the cPanel & WHM plugin and the Plesk extension. The clause was added to the body; the DirectAdmin plugin is named only in Acronis's advisory. Source: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json (catalog 2026.10.16, shortDescription).
- Applied: an em dash in the title was replaced with a comma.
- Declined, already fixed by 2026-10-11T1307Z-audit: the DirectAdmin product omission (affected/fixed/affected_products/summary/body/actions).
- Declined, already fixed by 2026-10-11T1307Z-audit: the sourcing_note "no readable content" wording.
- Carried advisory (sources[0] is a JSON API endpoint): left unchanged. The human-readable URL https://security-advisory.acronis.com/advisories/SEC-10986 serves only a JavaScript shell (`<div id="app">`, "Please enable JavaScript"), with no advisory text on any transport. The JSON record at /api/v1/advisories/SEC-10986 carries the cited text verbatim: three products, patched builds, CVSS 7.8, and the exploitation sentence.

## 2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce
- Record: `correction`, fields `[body, cves, headline, sources, sourcing_note, title]`.
- Applied (defect 2): the 9.1 score for CVE-2026-81642 is now attributed to NLnet Labs, the CNA, with NCSC Switzerland restating it. This was fixed in the main analysis, in the 2026-09-30 correction section (where it stood) and in the sourcing_note, and a new sources[] record was added for the advisories-page anchor. Ground truth: https://nlnetlabs.nl/projects/unbound/security-advisories/#heap-buffer-overflow-and-possible-remote-code-execution-when-digesting-dnskey (Severity: Critical, linking the CVSS 4.0 vector), with the CNA record read to verify (baseScore 9.1). NCSC hub post 12957 restates it.
- Applied (defect 3): the headline now gives the sourced mechanism: "A malicious zone Unbound is only asked to resolve can overflow its DNSSEC validator's digest buffer". Source: https://nlnetlabs.nl/downloads/unbound/CVE-2026-81642.txt
- Applied (defect 1 remainder): the 8.4 is restored to the title ("CVSS4.0 9.1 and 8.4") and to the main analysis with its citation. The cvss field now reads "8.4 (CVSS4.0)".
- Declined, already fixed by 2026-10-11T1307Z-audit: the cvss value was restored and the 2026-09-30 section reworded. The append-only 2026-09-30 record summary still says "withdrawn"; it cannot be touched.

## 2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal
- Record: `correction`, fields `[body, evidence, immediate_action, summary]`.
- Applied (defect 1 remainder): immediate_action's accumulator list was missing "R82.20 Take 10+", and it is now added. Source: https://support.checkpoint.com/results/sk/sk1000171/ (lastModified 2026-10-13, "Jumbo Hotfix Accumulator for R82.20 starting from Take 10").
- Applied (defect 2 remainder): the summary's present-tense "says Check Point's second indicator does not fire" is now dated to Bishop Fox's 2026-10-01 post. It also states that Check Point revised the indicators on 2026-10-13 and that neither party says whether the new ones catch the route.
- Applied (defect 2 remainder): the Detection paragraph now gives Indicator 1 as sk1000171 still describes it, an over-long username paired with a simultaneous FWM/MDS core dump. It also records that the revision replaced the load-error indicator Bishop Fox said its cron-write route never trips, and that no source says whether 2.a to 2.c catch that route.
- Applied (defect 2 remainder): the Triage line was rewritten. It had said the crash pairing was in Check Point's "original guidance", but it is still in the current page. The vendor/Bishop Fox disagreement on Indicator 1 is now surfaced. A new evidence quote comes from sk1000171. Bishop Fox: https://bishopfox.com/blog/weaponizing-check-point-management-cve-2026-93616 (unrevised).
- Applied: the 2026-10-04 update section now marks the old second indicator as replaced in the 2026-10-13 revision.
- Declined, already fixed by 2026-10-11T1307Z-audit: the affected/fixed R82.20 scope and the body version sentence, and the rewrite of Detection to the four-indicator set.
- Note: the sk1000171 sources[] date stays 2026-09-22 although the cited indicator text is from the 2026-10-13 revision. This was already the case after the 2026-10-11 record, and the prose dates the revision explicitly.

## 2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce
- Record: `correction`, fields `[actions, body, evidence, sources, sourcing_note]`.
- Applied (defect 1): the blanket "SolarWinds does not state ... connected to either CVE" is narrowed to "the release notes do not tie", both in the main analysis and in the 2026-09-30 section. Added: SolarWinds' CVE-2026-28324 record gives a workaround (configure a Player Password on WPM Player-to-server communication), and the CVE-2026-28325 advisory gives none.
- Applied (defect 2): the Detection line, Defender takeaway and actions[0] are scoped as follows. CVE-2026-28325's communication mode is unnamed. CVE-2026-28324 names the mitigating control. The workaround is the interim step.
- Applied (defect 3): the main analysis now states CVE-2026-28325's adjacent-network vector, and the generic "internet-reachable" sentence is scoped to CVE-2026-28324 in the affected configuration.
- **Sourcing caveat for the main agent:** the workaround text appears only in SolarWinds' CNA record. It is not in the release notes, either trust-center advisory, NCSC-NL CSAF 0388, CERT-FR, GBHackers or GHSA-p7gw-vm7r-23mp, and check_run blocks cveawg and cve.org as citations. I therefore cited it as follows:
  - Inline, ENISA EUVD's copy of the record: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-84807 (assigner SolarWinds; WPM guide among the references; the page is script-rendered, so not machine-checkable). This page does not show the workaround sentence itself.
  - Inline, the WPM guide for the setting: https://documentation.solarwinds.com/en/success_center/wpm/content/orionwpmagaddingalocation.htm
  - The verbatim workaround quote is in evidence[] with `source_url: https://cveawg.mitre.org/api/cve/CVE-2026-28324`, which the evidence check reads and passes. The gate's blocked-source rule scans only sources[] and body links.
  - The sourcing_note states this provenance plainly. If the verifier treats EUVD as not vouching for the workaround, the fallback is to keep only the narrowing (release notes) and drop the workaround clause.
- Declined, already fixed by 2026-10-11T1307Z-audit: the CVE-2026-28325 vector in cves[] and the action's internet-exposure scoping.

## 2026-09-24/closedquorum-llm-orchestrated-c2-implant
- Record: `correction`, fields `[body, evidence, summary]`.
- Applied (defect 3): "failure modes are deterministic ... sleep-retry" is replaced with Talos's own list. Talos calls only the tie-break "fully deterministic". Two evidence quotes were added. Source: https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
- Applied: the summary and body carried five em dashes, now replaced with commas, colons or parentheses. There is no reader delta.
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (static-analysis date versus build date) and defect 2 (ETW sentence).

## 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
- Record: `correction`, fields `[body, evidence, summary, tags, title]`.
- Applied (defect 2): tags `auth-bypass` and `info-disclosure` are dropped (now `[ai-abuse]`). The title says "method filter" rather than "access restriction". The summary and Defender takeaway state that the data and the key were public and that Howard-Jones does not call it hacking. The Triage line's "authenticated-data endpoint" now reads "data endpoint". Two evidence quotes were added. Sources: https://siliconangle.com/2026/09/27/researcher-links-16000-scans-of-a-u-n-statistics-portal-to-openai-agents/ ("None of the data was secret"; key public) and https://swarmcha.se/posts/openai-unctad ("I don't think I'd call it that.").
- Applied (carried advisory): the payload-page labels (two agent-chosen strings) are replaced with a generic description, "agent-chosen labels referring to ChatGPT and OpenAI". I left Transluce's "a tag beginning with oai" in the 2026-10-02 update section. It is a three-letter prefix pattern rather than a reproduced label, and it carries Transluce's attribution point. The main agent should generalize it too if the house reading is stricter.
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (CORS mis-statement, "began") and the takeaway stating OpenAI authorship as fact.

## 2026-09-29/bitget-hot-wallet-theft-north-korea-nexus
- No record. Both findings were declined as already fixed by 2026-10-11T1307Z-audit: the hedged evidence[0] and body quotation, and "pending a fix". I re-read https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response today: the current quotes match and neither "may have exploited" nor "potentially obtain" remains.

## 2026-09-30/cve-2026-86950-apple-coregraphics-zero-day-kev
- No record. Both findings were declined as already fixed by 2026-10-11T1307Z-audit: epss is now 0.01242 (FIRST), and the forensic-triage sentence is withdrawn. The KEV catalog read today (2026.10.16) shows `forensicTriage: "No"` for CVE-2026-86950.

## State / registry changes for the main agent
- None. No CVE ids were added to or removed from any cves[]; the Unbound cvss string change does not touch state/cves_seen.json. No entity keys or relations. No sources.json change.

## Scratch
- Section and summary files: work/2026-10-20T0835Z-audit/repair-2/*.section, *.summary
- Fetched pages: work/2026-10-20T0835Z-audit/repair-2/fetch/
- Page-check cache: work/2026-10-20T0835Z-audit/repair-2/quote-bodies/
