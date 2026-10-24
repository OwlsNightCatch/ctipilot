**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-24T03:54:17Z · ended_at=2026-10-24T04:24:13Z · duration_seconds=1796

## Verification report — 2026-10-24T0255Z-intel (iteration 1)

Scope walked: all 306 ledger claims (rows in `verification.iter1.claims.yaml`: 283 ok, 23 non-ok), the ten entries read whole with `git diff HEAD` per updated entry, the run record, dedup context, the research findings and the telemetry. Mechanical contract held for every updated entry: record `fields` cover every changed frontmatter key (except the `updated_at` mirror, correct for the six `update` records and untouched for the three `improvement` records), earlier `updates[]` records are preserved, the `## <Type> - <at>` sections match their records.

### Citation does not support the claim

- #1 php-critical-release (body paragraph 5; Update 2026-10-24 paragraph 5): "Ultra-Reliable Wireless Backhaul with a fix in 27.1.1 (February 2027), and Duo Access Gateway, where the attacker must be an authenticated administrator". Cisco's table (raw HTML of cisco-sa-php-october26-Jj384Daq): `Ultra-Reliable Wireless Backhaul (URWB)<sup>1,2</sup>` ... `27.1.1 (Feb 2027)`; `<td>Duo Access Gateway</td> ... <td>3.2.0 ...Release Notes</td>` with no footnote. Footnote 1 ("For this product, the attacker must be authenticated as an administrator ... reducing the CVSS score to 6.6") and footnote 2 (workaround in the bug ID) belong to URWB. Fix: attach the admin-only condition and the workaround to URWB, give Duo Access Gateway its 3.2.0 fix.
- #2 php-critical-release (body paragraph 2): "its table no longer has separate Panorama and WildFire appliance rows, lists WF-500 and WF-500-B as unaffected". The live table still has `| WildFire Appliance WF-500 and WF-500-B | None | All |`. Only the Panorama row is gone.
- #3 pan-os entry (body paragraph 2; Detection): the Threat Prevention coverage "applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, and threat prevention is enabled on that traffic", and Detection's "the three conditions hold". The advisory lists four bullets; the omitted one is "Decrypt inbound traffic to the management interface so the firewall can inspect it." (without it the signatures cannot see an HTTPS management session). Fix both places.
- #4 pan-os entry (summary, body, cves[].affected/fixed, record summary) and php entry (Update 2026-10-24): every WF-500 and Panorama-row change is attributed to "the revision of 2026-10-24". PAN's own Timeline on the live advisory reads: `2026-10-24 Added updated threat signature and content version release details` / `2026-10-23 Updated the status of Prisma SD-WAN ION ... Also made the correction to the status of WildFire Appliance WF-500 and WF-500-B impact.` / `2026-10-23 Added estimated availability dates (ETAs) for hotfix releases across supported PAN-OS versions.` So the WF-500 reversal is a 2026-10-23 revision made after the previous run read the page; the 2026-10-24 revision only extended signatures and content versions. Re-date those statements (and drop "unchanged in the 2026-10-24 revision" as the dating of the ETAs).
- #5 (low confidence) publica entry (body paragraph on IPCT; Update 2026-10-24): "it wrote to all insured" / "It sent the letter to all insured". Ticinonline 2026-10-23: "una lettera, che verrà inviata settimana prossima" (will be sent next week). The IPCT letter says it decided to send it to all insured. Figures and fields all match the letter (about 1,800; about 1,700 + about 80; 17,000 and 10,000; 2026-10-14 call; no certain evidence but plausible), checked against the PDF text.
- #6 (low confidence) fortinet entry (body, Improvement section): "No exploitation is reported ([The Hacker News])", "and no exploitation is reported ([The Hacker News])". The article has no exploitation-status statement; Fortinet's PSIRT field `Known Exploited No` (FG-IR-26-180 raw page) is the source. Re-cite.
- #7 (low confidence) teamupdraft entry (body paragraph 3; Update 2026-10-24): "blocked only because the keys had already been deleted". Nethemba: "Our mu-plugin stopped them, and the keys no longer existed." Two blockers; "only because" drops its own mu-plugin.

### Unsupported / hallucinated facts

- #8 pan-os entry (Defender takeaway; headline; cves[].fixed "Panorama: no separate ETA"): "Panorama, which the advisory dates only through the PAN-OS note, stays on the restriction until a build is published". The Note carries no date and the advisory never says Panorama awaits its own build. Archived advisory (https://web.archive.org/web/20261023120000/https://security.paloaltonetworks.com/CVE-2026-109618, read this iteration) had combined rows `| PAN-OS / Panorama 11.2.0 | ... >= 11.2.10-h16 (ETA: 10/26) ...`; the live rows are now labelled `PAN-OS 11.2` with `Note: This issue is applicable to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series)`. The hotfix ETAs therefore read as covering Panorama's same-numbered builds. "Panorama has no separate date" is literally true and misleads the operator who runs Panorama; say the advisory no longer distinguishes Panorama from PAN-OS and that the PAN-OS hotfix trains apply, then remove the "stays on the restriction until a build is published" clause. (Answer to your point 3: the wording needs this correction.)
- #9 (low confidence) publica entry (Defender takeaway): "the exposed files at IPCT (checks and recalculations), the Pensionskasse Stadt Zürich (migration tests) and Publica (the 2019 migration) were project, test or migration data held at the supplier". IPCT (two ongoing projects) and PKZH (data for tests of the planned system change) hold. For Publica the sources hedge: Inside IT "weshalb mutmasslich dennoch Personendaten auf den Servern lagen", 20 Minuten "offenbar"; the entry's own earlier text says "apparently". Restore the hedge. The inference sentence is otherwise sound and the closing advice (what a supplier holds outside the productive system, whether its deletion confirmation is true) follows.

### Needs more research

- #11 (low confidence) publica entry: no `**Exposure:**` line although the sources support one (which funds' insured, which data fields, how to tell: the fund's own notice or letter).

### Missed angles

- #12 (low confidence) Splunk Enterprise CVE-2026-76268 (unauthenticated Patroni REST API on search head cluster members, OS command execution, CVSS 9.8; Splunk SVD-2026-1001 of 2026-10-07, Horizon3 write-up 2026-10-22T20:25Z, a public repository claims a PoC; fixed 10.4.3 / 10.2.7, PostgreSQL-sidecar workaround). S1 marked it borderline; the run record drops it as "outside the window", yet the Horizon3 item fell inside the previous run's window and nothing covered it. Splunk is the audience's own platform. Holding it as regular cycle (cluster-network reachability, no exploitation, two newest branches only) is defensible; log that as the reason, or add it. Search: "CVE-2026-76268 Splunk Patroni". Otherwise coverage looks complete: both KEV additions covered (verified against kev-window.txt and the catalogue), the PHP2Shell, Node.js, GitLab/Ruby, PAN-OS, LiteLLM, TeamUpdraft, Publica threads are covered; the SAP Patch Day gap is already disclosed in the run record.

### Editorial / less-is-more flags (advisory)

- #13 node2shell: the Node.js release pages (v22.23.4, v24.22.1, v26.12.1, each dated 2026-10-21 and listing "(CVE-2026-111497) deps: brotli: cherry-pick 0ed4268a4401abcb44720963 ... High") carry the fixed versions first-party; cite them instead of a corroborating vendor and trim the sourcing_note.
- #14 node2shell: the EUVD link is the JSON API (the human page https://euvd.enisa.europa.eu/vulnerability/CVE-2026-111497 reads, but shows only PYSEC-2026-4323). The two PYSEC records cite the OpenSourceMalware post and OSM says it submitted them, so they do not independently corroborate the PyPI exposure; the PyPI half rests on OSM's sdist diff. State that, or hold credibility to what that half supports.
- #15 fortinet: the Improvement section restates the Horizon3 paragraph now in the main analysis; the change also moves the actionable status (poc-public, headline, "out of cycle"). Improvement is defensible (PoC predates the entry) but a reader of the 2026-10-23 entry gets no float; trim the section or use an update record.
- #16 teamupdraft: source label "Nethemba (living post, updated to 2026-10-21)" is stale (change log runs to 2026-10-23, adding a reader's test: password found on all three of a reader's premium sites and in backups back to 2022, and on one of Nethemba's three); the entry still frames it as a code reading only.
- #17 publica: 71 KB, eleven changelog sections, actions[0] of about 190 words; consider consolidating.
- #18 node2shell: `cves[0].cvss: "9.2"` lacks the version label other entries carry.

### Analytical-link-as-fact

- #10 (low confidence) php entry (summary, body, Update 2026-10-24): "Unit 42 reports a confirmed intrusion of a European government entity with agentic post-exploitation". The brief says "within two hours of the initial exploitation" and names no flaw for the foothold; the run's own S3 note says "the brief does not say which flaw or exploit delivered the initial foothold". Only sourcing_note says "without naming the victim or the initial vector". Carry the qualifier in the summary and body. Everything else in the Unit 42 passage (two hours, hashes and MFA secrets, NTLM-relay tunnel, Domain Admin attempt, the ==SHELLUSER== / ==PASSWD== markers) matches the brief updated 2026-10-23 12:30 PT. The set-against block is accurate: CrowdStrike "has not observed successful exploitation ... in the wild or within our honeypot environments", Wordfence "have not observed any confirmed compromises" (74,000+ attempts), Sophos corrected 2026-10-22 21:21 UTC to scanning and failed attempts (blocked Mirai-derived payload), SANS ISC "building a universal, reliable, one click exploit is quite difficult".

### Points you asked about

1. PHP2Shell: critical stays (newly weaponised per VulnCheck, active attack traffic, CERT-EU/ENISA/BACS joint urgency, Swiss federal exposure). CVE-2026-115560 is correctly described (php.net 2026-10-23: unusual serialize-handler switch, "unlikely RCE vector", keep session.upload_progress.enabled=0, full advisory with the next release; THN: no versions, no score, no exploitation); omitting it from cves[] has no dedup cost: state/cves_seen.json carries it. VulnCheck figures (8.4.10 to 8.4.26, 8.5.10 and 8.5.11, 7 PM ET 10-22 ASLR bypass for 8.4.26 only, 5:30 PM ET 10-23 matrix) verified on the live page. Findings #1, #2, #4, #10 touch this entry.
2. Node2Shell: Node.js page lists no fixed versions (confirmed: no match for 22.23.4/24.22.1/26.12.1), Node.js releases and Imperva ("The project released fixes in 22.23.4, 24.22.1, and 26.12.1") carry them; CVSS 4.0 9.2 vector AV:N/AC:L/AT:P/PR:N/UI:N confirmed in the EUVD record (assigner Google); the PYSEC supersession is accurate (PYSEC-2026-4322/4323 dated 2026-10-23) but see #14. Entry body, evidence quotes, windows and package ranges all check out.
3. PAN-OS: see #3, #4, #8.
4. Publica: IPCT numbers and fields match the letter; see #5, #9, #11.
5. Priority calibration: critical (PHP2Shell) and high (Publica, TeamUpdraft, Zimbra) hold. Notable holds for PAN-OS (no exploitation, vendor rates impact availability-only, urgency moderate), GitLab (CVSS 10.0 unauthenticated but no exploitation or public PoC; defensible, borderline for high on exposure grounds), LiteLLM (exposure window closed), Fortinet (FortiSIEM PoC public; reachability-dependent), ARTEX, and Node2Shell (independent working RCE demonstration, no exploitation, no public PoC; clears the soundness gate on its own mechanics). Record types: the six `update` records each carry a new fact; the three `improvement` records are defensible. Wiz's ARTEX post is dated 2026-10-22, after the entry's creation, so it would also stand as an update; the Fortinet PoC predates the entry (see #15).

Checks with no finding: no IOCs, no em dashes outside section headings, no workflow-internal vocabulary in reader-facing text, classification present and in vocabulary on all ten, no org_triage/watchlist use, verification values match source counts, registry additions exist (`tool:node2shell`, five product keys), run-record notes hold (KEV sweep, backlog row, S1 reconstruction: nine items, 28-row ledger, `ended_at: PENDING`).

### Verdict

NEEDS_FIXES (truth: 10, editorial: 2, advisory: 6)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: php-critical-release-pre-announced-cve-2026-109618-109619 (body paragraph 5, Update 2026-10-24 paragraph 5)
  item: "Cisco lists ... Ultra-Reliable Wireless Backhaul with a fix in 27.1.1 (February 2027), and Duo Access Gateway, where the attacker must be an authenticated administrator"
  url_or_quote: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq"
  summary: "Cisco's table puts footnote 1 (attacker must be an authenticated administrator, CVSS 6.6) and footnote 2 (workaround in the bug) on the URWB row (<sup>1,2</sup>); the Duo Access Gateway row has no footnote and lists fixed release 3.2.0. Move the admin-only condition (and the workaround) to URWB, give Duo its 3.2.0 fix. Claims 1f615be412, fc15293702."
- code: F3
  category: claim-not-supported
  section: php-critical-release-pre-announced-cve-2026-109618-109619 (body paragraph 2)
  item: "its table no longer has separate Panorama and WildFire appliance rows, lists WF-500 and WF-500-B as unaffected"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-109618"
  summary: "The live table still carries a WildFire row: '| WildFire Appliance WF-500 and WF-500-B | None | All |' (now in the Unaffected column). Only the separate Panorama row is gone. Claim 71c5d0e883."
- code: F3
  category: claim-not-supported
  section: pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (body paragraph 2, Detection)
  item: "applies only when management traffic is routed through a dataplane interface, the certificate for inbound management traffic has been replaced, and threat prevention is enabled on that traffic ... the three conditions hold"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-109618"
  summary: "The advisory lists four conditions; the entry omits 'Decrypt inbound traffic to the management interface so the firewall can inspect it', the one that decides whether the signatures can see an HTTPS management session at all. Detection's 'three conditions' is wrong. Claims 8102fecba1, 13b5919f7a."
- code: F3
  category: claim-not-supported
  section: pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (summary, body, cves[], update record) and php-critical-release (Update 2026-10-24)
  item: "Palo Alto Networks' advisory ... revised on 2026-10-24 ... WF-500 and WF-500-B ... are now listed as unaffected ... drops the separate Panorama row"
  url_or_quote: "https://security.paloaltonetworks.com/CVE-2026-109618 (Timeline)"
  summary: "PAN's own timeline dates the WF-500/WF-500-B correction to 2026-10-23 ('2026-10-23 Updated the status of Prisma SD-WAN ION ... Also made the correction to the status of WildFire Appliance WF-500 and WF-500-B impact.'); the only 2026-10-24 entry is '2026-10-24 Added updated threat signature and content version release details'. The WF-500 reversal and the Panorama relabel are 10-23 revisions that happened after the previous run read the page; say so (and 'unchanged in the 2026-10-24 revision' in cves[].fixed is wrong in kind). Claims f64f33f3c3, 5cbb098901, 06f2133fd0, 6036d20336, 7f145fb837, f3fd94a9a3, 1f6ac79aea."
- code: F3
  category: claim-not-supported
  section: publica-pk-softech-supplier-malware-intrusion-data-outflow (body, Update 2026-10-24)
  item: "it wrote to all insured because it cannot exclude that more was affected / It sent the letter to all insured because its information is partial"
  url_or_quote: "https://www.tio.ch/ticino/attualita/1958742/dati-stati-cantone-istituto-ticino-attacco-pensioni-casse-previdenza"
  summary: "(low confidence) Ticinonline of 2026-10-23 says the letter 'verrà inviata settimana prossima' (will be sent next week); the IPCT letter itself says it decided to send it to all insured. Past tense 'wrote'/'sent' is not supported; use 'decided to write' / dated 2026-10-23. Claims d44c2f1190, 922bcbc231."
- code: F3
  category: claim-not-supported
  section: fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes (body, Improvement section)
  item: "No exploitation is reported (The Hacker News) / the fixed build, 7.5.1, and the port restriction are unchanged, and no exploitation is reported (The Hacker News)"
  url_or_quote: "https://thehackernews.com/2026/10/critical-fortisiem-flaw-gets-public.html"
  summary: "(low confidence) The THN article says nothing about in-the-wild status. The statement is supported by the Fortinet PSIRT field 'Known Exploited No' on FG-IR-26-180 (raw page); cite that instead. Claims c61ea26e1b, c8b5e9ea99."
- code: F3
  category: claim-not-supported
  section: teamupdraft-updraftcentral-stolen-keys-backdoor-plugins (body paragraph 3, Update 2026-10-24)
  item: "sent UpdraftCentral commands to two of Nethemba's sites ... blocked only because the keys had already been deleted"
  url_or_quote: "https://nethemba.com/updraftcentral-backdoor-analysis/"
  summary: "(low confidence) Nethemba: 'Our mu-plugin stopped them, and the keys no longer existed.' Two blockers (its own blocking mu-plugin and the deleted keys); 'only because' drops the first. Claims 294aa51733, 8e74827772."
- code: F4
  category: hallucinated-fact
  section: pan-os-panorama-php2shell-mgmt-interface-no-fixed-release (Defender takeaway, headline, cves[].fixed)
  item: "Panorama, which the advisory dates only through the PAN-OS note, stays on the restriction until a build is published"
  url_or_quote: "https://web.archive.org/web/20261023120000/https://security.paloaltonetworks.com/CVE-2026-109618"
  summary: "The note carries no date, and the advisory never says Panorama is waiting for its own build. The advisory's earlier table had combined rows '| PAN-OS / Panorama 11.2.0 | ... >= 11.2.10-h16 (ETA: 10/26) ...' and the live rows (now 'PAN-OS 11.2') carry a note that the issue applies to PAN-OS software on PA-Series, VM-Series and Panorama (virtual and M-Series): the hotfix ETAs read as covering Panorama. 'Panorama has no separate date' (headline/summary) is literally true but misleads Panorama operators; state that the advisory no longer distinguishes Panorama and that the PAN-OS hotfix trains apply, and drop 'stays on the restriction until a build is published' and 'Panorama: no separate ETA'. Claims db6ffc5fa3, f4c7662c51."
- code: F4
  category: hallucinated-fact
  section: publica-pk-softech-supplier-malware-intrusion-data-outflow (Defender takeaway)
  item: "the exposed files at IPCT (checks and recalculations), the Pensionskasse Stadt Zürich (migration tests) and Publica (the 2019 migration) were project, test or migration data held at the supplier"
  url_or_quote: "https://www.inside-it.ch/publica-wollte-pensionskassendaten-loeschen-lassen-20261022"
  summary: "(low confidence) For Publica the sources hedge: Inside IT/Publica 'weshalb mutmasslich dennoch Personendaten auf den Servern lagen', 20 Minuten 'offenbar'. The new sentence states it as fact, losing the 'apparently' the entry's own earlier text keeps. IPCT and PKZH parts hold. Claim f8b20522ac."
- code: F13
  category: analytical-link-as-fact
  section: php-critical-release-pre-announced-cve-2026-109618-109619 (summary, body, Update 2026-10-24)
  item: "Unit 42 reports a confirmed intrusion of a European government entity with agentic post-exploitation"
  url_or_quote: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
  summary: "(low confidence) Unit 42's brief says 'within two hours of the initial exploitation' but never states which flaw gave the foothold; the run's own research notes say 'the brief does not say which flaw or exploit delivered the initial foothold'. Only sourcing_note says 'without naming ... the initial vector'; the summary and body read as a PHP2Shell intrusion. Add the qualifier to body and summary. Claims 47c6a8905f, 8d58887e82."
- code: F8
  category: needs-more-research
  section: publica-pk-softech-supplier-malware-intrusion-data-outflow
  item: "no **Exposure:** labelled line (Detection and Defender takeaway only)"
  url_or_quote: "entries/2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow.md"
  summary: "(low confidence) The sources clearly support an Exposure line (who is affected: staff insured with Publica, PKZH, Pensionskasse Post, BPK, BLVK, IPCT, Libera-managed funds; data fields; how to tell: the fund's own notice or letter). Pre-existing, but the entry was rewritten three times this week."
- code: F10
  category: missed-angle
  section: run record notes (borderline-drop Splunk Enterprise CVE-2026-76268)
  item: "Splunk Enterprise CVE-2026-76268: unauthenticated Patroni REST API on search head cluster members gives OS command execution (CVSS 9.8), Horizon3 write-up 2026-10-22, public repository claims a PoC"
  url_or_quote: "https://horizon3.ai/attack-research/vulnerabilities/cve-2026-76268/"
  summary: "(low confidence) S1 flagged it borderline; the run record drops it as 'both outside the window', but the Horizon3 item (2026-10-22T20:25Z) fell inside the previous run's window and no earlier fire covered it. Splunk is the SOC audience's own platform, unauthenticated, claimed public PoC, fixed in 10.4.3/10.2.7, workaround exists. Reasonable to hold as regular-cycle (cluster-network reachability, no exploitation), but reconsider or log it as a deliberate drop with that reason. Search: 'CVE-2026-76268 Splunk Patroni exploit'."
- code: F11
  category: editorial-advisory
  section: cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi (sources, sourcing_note)
  item: "the fixed Node.js versions come from Imperva and OpenSourceMalware"
  url_or_quote: "https://nodejs.org/en/blog/release/v24.22.1/"
  summary: "The Node.js release pages (v22.23.4, v24.22.1, v26.12.1, all dated 2026-10-21, 'deps: brotli: cherry-pick 0ed4268a4401abcb44720963 ... (CVE-2026-111497) High') carry the fixed versions first-party; cite them for the fix claim instead of a corroborating vendor."
- code: F11
  category: editorial-advisory
  section: cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi (sources, body paragraph 3)
  item: "ENISA's record now carries two PyPI advisories for them dated 2026-10-23 ([ENISA EUVD](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-108169))"
  url_or_quote: "https://euvd.enisa.europa.eu/vulnerability/CVE-2026-111497"
  summary: "Reader-facing link is the JSON API; the human EUVD page reads (but lists only PYSEC-2026-4323). The two PYSEC records cite the OpenSourceMalware post as their reference and OSM says it submitted them, so they are not independent corroboration of the PyPI exposure (the PyPI claims rest on OSM's sdist diff). Say so, or keep credibility at the level the PyPI half supports."
- code: F11
  category: editorial-advisory
  section: fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes (Improvement section, record type)
  item: "## Improvement - 2026-10-24T03:43:50Z repeats the Horizon3 paragraph already in the rewritten main analysis"
  url_or_quote: "entries/2026-10-23/fortinet-fortisandbox-fortisiem-pre-auth-critical-fixes.md"
  summary: "The dated section restates what paragraph 3 of the main analysis now says. The change moves the actionable status (poc-public tag, headline, 'out of cycle now that a proof of concept is public'), so a reader who saw the 2026-10-23 entry gets no float: improvement is defensible because the PoC predates the entry, but consider an update record, or trim the section to one sentence."
- code: F11
  category: editorial-advisory
  section: teamupdraft-updraftcentral-stolen-keys-backdoor-plugins (sources)
  item: "Nethemba (living post, updated to 2026-10-21)"
  url_or_quote: "https://nethemba.com/updraftcentral-backdoor-analysis/"
  summary: "The post's own change log runs to 2026-10-23, including a reader's test and counts of how often the teamupdraft.com password stays in the database (found on all three of a reader's premium sites, backups back to 2022; on one of Nethemba's three); the entry still frames it only as a code reading and the label is stale."
- code: F11
  category: editorial-advisory
  section: publica-pk-softech-supplier-malware-intrusion-data-outflow (length)
  item: "71 KB body, eleven changelog sections, one action of about 190 words"
  url_or_quote: "entries/2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow.md"
  summary: "Length no longer earns itself for a reader who works the brief; consider consolidating the per-fund statements and splitting actions[0] into the call-back rule and the per-fund list."
- code: F11
  category: editorial-advisory
  section: cve-2026-111497-node2shell-brotli-decoder-rce-nodejs-pypi (cves[].cvss)
  item: "cvss: \"9.2\""
  url_or_quote: "cves[0].cvss"
  summary: "Other entries label the CVSS version ('9.2 (CVSS 4.0)'); the body says 4.0 but the field does not."
```
