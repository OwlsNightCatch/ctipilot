# repair-3 report (cleanup wave 02, run 2026-10-21T0800Z-audit)

Batch: `work/2026-10-21T0800Z-audit/batch-3.yaml`, 15 entries. Records written: 14, all `improvement` (5 internal, 9 with a section). No record: 1 (Netlogon, decline). Scratch: `work/2026-10-21T0800Z-audit/repair-3/` (fetched bodies under `src/`, edit scripts under `bin/`, `notes.md`, `check-all.txt`, `page-checks.txt`). No W1-F hunks covered this batch. No entry carried `legacy_duty: true`.

## Per entry

### 2026-05-08/instructure-canvas-extortion-330-institutions-across-six-cou
- improvement, internal, at 2026-10-21T08:06:50Z, fields: body.
- Applied (W1-E 21): the listed but uncited Infosecurity Magazine source is now cited inline beside The Register on the per-institution 2026-05-12 deadline sentence ("The note by ShinyHunters called for those affected to negotiate a settlement before everything is leaked on May 12."). GT: https://www.infosecurity-magazine.com/news/shinyhunters-escalates-canvas/
- Em dashes: none.

### 2026-05-09/cve-2026-44128-et-al-seppmail-secure-email-gateway-cvss-9-3
- improvement, internal, at 2026-10-21T08:07:56Z, fields: summary.
- Applied (W1-E 12, reopened as a reader-facing misattribution in the TL;DR): NCSC-CH post 12551 says "Several vulnerabilities have been fixed in SEPPmail Secure Email Gateway 15.0.4" and marks only CVE-2026-44128 "Fixed in v15.0.2.1"; the 15.0.3 fix for CVE-2026-44126 and the Perl eval() mechanism are InfoGuard's. The summary now attributes each version to its source; the body already did. GT: https://security-hub.ncsc.admin.ch/#/posts/12551 (read via `ncsc-csh post 12551`), https://labs.infoguard.ch/posts/seppmail_secure_e-mail_gateway_rce_vulnerabilities_cve-2026-2743_cve-2026-7864_cve-2026-44127_cve-2026-44128/

### 2026-05-11/cve-2026-6722-php-soap-use-after-free-in-soap-global-ref-map
- improvement, at 2026-10-21T08:09:29Z, fields: cves, sources, body. Section added.
- Applied (W1-E 17): the CVE record scores CVE-2026-7262 2.9 under CVSS 4.0, the same base vector as PHP's GHSA (6.3, "Moderate") with the threat metric E:P added; noted in `cves[].cvss` and the body, cited to EUVD. The body's uncited CNA score of 9.5 for CVE-2026-6722 now cites its EUVD record. GT: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28971, https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-28966, https://github.com/php/php-src/security/advisories/GHSA-hmxp-6pc4-f3vv

### 2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898
- No record.
- Declined (W1-E 9): `site/taxonomy.yaml` `cve_status` has no reported or disputed value. Dropping `exploited` would hide CCB's in-the-wild statement (relayed by CERT-EU) from automated readers, which is the larger error. The headline, summary and Contradiction line already carry Microsoft's dissent, and the earlier decline was on principle with no reader-facing error.

### 2026-06-09/cve-2026-42271-berriai-litellm-low-privilege-command-injecti
- improvement, internal, at 2026-10-21T08:11:25Z, fields: title, headline, summary, affected_products, cves, body.
- Applied (W1-E 3): `affected_products: ["BerriAI LiteLLM", "Starlette"]`; CVE-2026-42271 affected "1.74.2 through 1.83.6 (>= 1.74.2, < 1.83.7)", fixed "1.83.7"; CVE-2026-48710 affected "Starlette 1.0.0 and earlier", fixed "Starlette 1.0.1". GT: https://github.com/advisories/GHSA-v4p8-mg3p-g94g ("Affected versions >= 1.74.2, < 1.83.7 / Patched versions 1.83.7"), https://horizon3.ai/attack-research/vulnerabilities/cve-2026-42271-chained-with-cve-2026-48710/
- Em dashes removed: title, headline, summary, body (2).
- Legacy (pending, optional): not run beyond the finding.

### 2026-06-10/year-old-winrar-flaw-cve-2025-8088-still-fuels-ukraine-intru
- improvement, internal, at 2026-10-21T08:11:57Z, fields: title, headline, summary, event_date, body.
- Applied (W1-E 16): event_date 2026-06-09 changed to 2026-06-08, Trend Micro's own page date (first primary). GT: https://www.trendmicro.com/en_us/research/26/f/old-winrar-flaw-fuels-attacks-on-ukraine.html
- Em dashes removed: title, headline, summary (2), body (2). Title and headline are now quoted YAML scalars, since they carry a colon.
- Legacy (pending, optional): not run.

### 2026-06-11/shinyhunters-oracle-peoplesoft-campaign-gadget-chain-access
- improvement, at 2026-10-21T08:13:55Z, fields: actions, body. Section added.
- Applied (W1-E 20): the hunt line said SSH attempts "from external or unexpected source ranges". Mandiant's recovered `_fanout.sh` "automates SSH credential spraying against internal hosts by parsing hostnames from the local `/etc/hosts` file", then copies a marker file into the WebLogic and Process Scheduler directories. The line now hunts spraying from a PeopleSoft server toward internal PeopleSoft hosts, correlated with that file write. GT: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/
- Applied (W1-E 19): the action's "rotate every credential" now follows Mandiant: "rotate all credentials accessible from the PeopleSoft tier", naming PeopleSoft configuration files and database connection strings as what the service accounts reach, and prioritising hosts where WebLogic runs as `root` or `SYSTEM`. GT: https://cloud.google.com/blog/topics/threat-intelligence/shinyhunters-renewed-mass-exploitation-campaign-targeting-oracle-peoplesoft/
- Applied (W1-E 23): the 7 body em dashes are removed (earlier record summaries left append-only).
- Legacy (pending, optional): not run. See residuals: the main analysis has no canonical Exposure, Detection or Defender takeaway label.

### 2026-06-14/cve-2026-20253-splunk-enterprise-unauthenticated-pre-auth-rc
- improvement, internal, at 2026-10-21T08:12:10Z, fields: event_date.
- Applied (W1-E 16): event_date 2026-06-12 (watchTowr) changed to 2026-06-10, SVD-2026-0603 "Published: 2026-06-10". GT: https://advisory.splunk.com/advisories/SVD-2026-0603

### 2026-07-09/ncsc-ch-rogueplanet-cve-2026-50656-defender-lpe-fixed
- improvement, at 2026-10-21T08:15:06Z, fields: title, body. Section added.
- Applied (W1-E 1): `**Exposure:**` (mpengine.dll at or below 1.1.26050.11, in Defender, which "runs on all supported version of Windows", and in SCEP and MSE; Defender-disabled hosts are "not in an exploitable state") and `**Defender takeaway:**` (automatic engine updates; verify on pinned, WSUS-gated or offline estates at 1.1.26080.3 or later, the ShieldBreak fix). The existing prose moved into the lines instead of being repeated. GT: MSRC CVE-2026-50656 and CVE-2026-69414 (read via `msrc cve`): https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50656, https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414
- Em dashes removed: title, body (1).

### 2026-07-13/servicenow-ai-platform-sandbox-escape-cve-2026-6875
- improvement, at 2026-10-21T08:16:34Z, fields: title, headline, summary, cves, actions, body. Section added.
- Applied (W1-B 1): the 2026-07-21 section no longer says the hosted estate is "already remediated" or names "MSP-run" deployments. It now says ServiceNow deployed a security update to hosted instances and provided updates to self-hosted customers and partners, and that its spokesperson still encourages self-hosted and ServiceNow-hosted customers to patch. GT: https://www.bleepingcomputer.com/news/security/critical-servicenow-code-execution-flaw-now-exploited-in-attacks/, https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB3137947
- Applied (W1-B 2): "partner-managed" swept from the headline (now 120 chars), summary (hosted customers kept in the patch-if-not-done clause), `cves[].affected`, actions[0], the takeaway (2) and the 2026-07-21 section.
- Declined (W1-B 3): the 2026-07-21 record summary is append-only; the 2026-09-30 Correction renders beside it.
- Em dashes removed: title.

### 2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev
- improvement, at 2026-10-21T08:17:58Z, fields: summary, cves, sources, actions, body. Section added.
- Applied (W1-B 1): the summary and narrative now say VulnCheck observed initial access "using exploits targeting both CVE-2026-0769 and CVE-2026-5027", and that the post-exploitation behaviour is not split per CVE. GT: https://www.vulncheck.com/blog/state-of-exploitation-1h-2026
- Declined (W1-B 1, headline part): the headline says only that the RCE is being exploited, which VulnCheck supports; it attributes no post-exploitation behaviour.
- Applied (W1-B 2): ZDI's CVE record lists Langflow 1.3.2 as the only affected version (EUVD-2026-4475, assigner zdi; GHSA-5v3c-9g74-93w7 shows "Unknown"). This now stands in `cves[].affected`, the narrative, the Exposure line ("affected range is undefined") and the 2026-09-30 section ("so the version detail is removed" dropped). GT: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-4475, https://www.zerodayinitiative.com/advisories/ZDI-26-035/
- Em dashes removed: actions[0].

### 2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce
- improvement, at 2026-10-21T08:19:49Z, fields: body. Section added.
- Applied (W1-E 32): the Hardening sentence moved out of `**Triage:**` into `**Defender takeaway:**`, with the interim access-restriction and VPN advice. The takeaway also gains the 2026-07-27 advisory's note that TeamCity 2024.03 and newer download the security patch plugin automatically, to be applied from Administration | Updates, under Available security updates (the section's delta). GT: https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/, https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/

### 2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach
- improvement, at 2026-10-21T08:22:05Z, fields: evidence, body. Section added.
- Applied (W1-E 31): the first eight `evidence[]` rows now carry an English `quote:` marked "(translated from German)", the verbatim German in `original:`, and the specific release as `source_url`. All eight originals were grep-verified on presseportal 100941487, 100941500 and 100941523. The three German quotations in the main analysis are now English translations. The section's delta is the government's GDPR Art. 33 personal-data-breach classification, which an evidence row carried but no sentence stated. GT: https://www.presseportal.ch/de/pm/100000148/100941487 (also /100941500, /100941523)
- W1-E 23 (em dashes): already resolved for reader text; the remaining em dashes sit only in earlier record summaries (append-only).

### 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver
- improvement, at 2026-10-21T08:24:07Z, fields: title, summary, actions, body. Section added.
- Declined (W1-B 1 and W1-B 3): already fixed by 2026-10-11T1307Z-audit (the Dune strings and similarities are stated separately; the opensearch-js three-variable path is explicit).
- Applied (W1-B 2): the containment paragraph gains Unit 42's finding that the August sample's installer for OS-level token-monitor persistence "was decrypted but never invoked ... treat OS-level persistence as latent capability, not observed behavior". GT: https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/
- Applied (W1-B 4): the artifact name `gh-token-monitor` is removed from actions[1] and the 2026-10-11 section; the persistence is described by type.
- Applied (W1-E 15): the duplicated dead-man's-switch and intimidation statements are merged so each is stated once. The OX wording is unchanged: ox.security returned 403 to `extract`, `url` and WebFetch, so the 2026-10-11 verifier's OX ground truth stands. Elastic GT: https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain
- Em dashes removed: title, summary (2), actions[0], body (9).

### 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass
- improvement, at 2026-10-21T08:25:45Z, fields: title, cves, sources, sourcing_note, body. Section added.
- Applied (W1-B 1): the CVE record's 9.8 (CVSS 3.1, PR:N/UI:N) now stands beside NCSC-NL's 7.1 (PR:L) in `cves[].cvss`, the sourcing note and the narrative, cited to EUVD-2026-54216 (EUVD does not label it ADP, so the entry says "the CVE record"). GT: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-54216; NCSC-NL CSAF via `ncsc-nl csaf NCSC-2026-0280`.
- Declined (W1-B 2): NCSC-NL's CSAF carries `document/notes` `{title: "CWE-287", text: "Improper Authentication"}`, so "NCSC-NL classed it CWE-287" is accurate.
- Applied (W1-B 3): the Contradiction line now says Apple credits CVE-2026-65400 to "Alfredo Pesoli (@__rev) via Bynario Atlas", not to fG!, and that Calif says fG! never reported his bug to Apple. GT: https://support.apple.com/en-us/148170, https://blog.calif.io/p/no-country-for-old-passwords
- Em dashes removed: title, body (4, all in the 2026-08-11 section).

## State changes the main agent must apply

- `entities/registry.yaml`: run `python3 tools/sync_products.py` to add the new product spelling **Starlette** (`product:starlette`, from the LiteLLM entry). Expect `product:berriai-litellm` `first_seen` to move from 2026-08-31 to 2026-06-09, since the LiteLLM entry now names it. The same sync also adds three Progress products from another batch's entries.
- `state/cves_seen.json`: bump `last_seen` to 2026-10-21 for the changed CVE records: CVE-2026-7262 (cvss), CVE-2026-42271 (affected/fixed), CVE-2026-48710 (affected/fixed), CVE-2026-6875 (affected), CVE-2026-0769 (affected), CVE-2026-65400 (cvss). No CVE was added.
- Note: `sync_products.py --report` writes `entities/registry.yaml` (it printed "wrote entities/registry.yaml"). I ran it once by mistake and restored the file to HEAD content (`git show HEAD:entities/registry.yaml`, no index change; base..HEAD carries no registry change). `git diff -- entities/registry.yaml` is empty.

## Checks

- `check_run.py --all`: no FAIL on my entries. Each of the 14 shows only the expected "run_id does not resolve to a run record" WARN. The one FAIL (`cve-sync` for CVE-2026-92438, Ninja Forms) is another batch's.
- `check_run.py 2026-10-21T0800Z-audit --page-checks-since 2026-10-21` (`repair-3/page-checks.txt`): no `quote-literal` or `citation-cve` line on my entries (the single WARN is the 2026-09-17 Pixel entry).
- Em dash scan of title, headline, summary, sourcing_note, actions, cves text and body (headings excluded) on all 15 entries: none left.

## Residuals noticed (not fixed)

- `tools/sync_products.py --report` writes the registry despite being described as a report mode (tool defect).
- `update_of: null` (retired key) still present on the LiteLLM, PHP, WinRAR, RoguePlanet and Langflow entries.
- LiteLLM: title and headline are identical; the main analysis keeps a legacy "#### CVE Summary Table".
- PeopleSoft: `priority: critical` with `immediate_action` on a June/September wave (calibration); inline T-ids in prose; a non-canonical "**Detection and hunting concepts (no IOCs).**" label and no main-analysis Exposure or Defender takeaway (legacy pass); "Confidence ... is MEDIUM" pipeline wording in the 2026-06-16 section.
- `state/cves_seen.json` titles are stale: CVE-2026-6722 says "patched in PHP 8.4.8" (entry: 8.4.21 etc.); CVE-2026-7261/7262 say "patched 2026-05-08" (entry: 2026-05-07); CVE-2026-65400 names only CVSS 7.1.
- ServiceNow: the EUVD source URL uses the path `/enisa/EUVD-2026-43520`, unlike the store's `/vulnerability/` and `/enisa/eu_vulnerability_database/` forms; it may not resolve.
- SEPPmail: `sources[]` lists the vendor contact page (https://www.seppmail.com/about-us/contact/) as a corroborating source.
- TeamCity: the 2026-08-06 section's sentence on the KEV deadline having "no operational meaning for Swiss organisations" is profile framing.
- CHAINDROP: the 2026-08-08 section puts `**Defender takeaway:**` and `**Triage:**` in one paragraph.
- macOS CVE-2026-65400: the KEV record now carries `forensicTriage: Yes` and BOD 26-04 required-action text the entry does not mention.
- ox.security blog posts are unreadable from this container by every transport (403), WebFetch included.
