# Repair worker repair-1, cleanup wave 03 (2026-10-21T1149Z-audit)

Batch: `work/2026-10-21T1149Z-audit/batch-1.yaml`, 14 entries. No groups, no legacy duties (all `legacy_duty: false`), no em dashes listed. Every defect was re-derived on the current text after the 2026-10-11T1307Z-audit records. Fetched bodies are under `work/2026-10-21T1149Z-audit/repair-1/src/`; section and summary files are beside them. Gates: `check_run.py --all` exit 0 (my entries show only the expected "run id has no run record yet" warning), and the page checks show 4 pass, 0 warn, 0 fail (`repair-1/page-checks.txt`).

Records written: 7 (2 correction, 5 improvement). No record: 7.

## Per entry

### 2026-05-08/amazon-ses-weaponised-for-authenticated-phishing-and-bec-kas: no record
- All five defects declined, already fixed by 2026-10-11T1307Z-audit: Securelist 119623 and BleepingComputer are cited; the European manufacturing claim is gone; SPF, DKIM and DMARC plus the blocklist point are stated; leaked IAM keys, their locations and TruffleHog are given; the staleness sentence is gone and `event_date` is 2026-05-04.

### 2026-05-08/cert-fr-certfr-2026-act-016-agentic-ai-tools-introduce-promp: improvement, 2026-10-21T12:06:43Z, fields summary, body, headline
- Applied (residual of defect 2): the advisory's five-item Risques list, in English paraphrase, added to the body and summary. The summary no longer calls plugins and prompt injection "the core risks". Ground truth: https://www.cert.ssi.gouv.fr/actualite/CERTFR-2026-ACT-016/
- Headline cut from 136 to 118 characters with the same meaning.
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (scope), defect 2's MCP and three-classes claims, defect 3 (recommendations), defect 4 (Copilot Studio and AutoGen), defect 5 (`event_date` 2026-04-13; only the `report:` key remains).

### 2026-05-08/glpi-certfr-2026-avi-0551-seven-cves-including-ssrf-and-xss: improvement, 2026-10-21T12:07:30Z, fields cves, body
- Applied (residual of defect 3): the body now states that both release notes list CVE-2026-5385, while GHSA-2fg5-jg72-h338 gives only ">= 11.0.0" as affected (patched 11.0.7). CVE-2026-42321 `affected` narrowed to "10.0.4 and later before 10.0.25" per GHSA-hwjc-8228-55x4 (">= 10.0.4, < 11.0.0"). The CVE-2026-5385 `affected` string keeps both branches, the conservative reading of the release notes. Ground truth: https://github.com/glpi-project/glpi/security/advisories/GHSA-2fg5-jg72-h338 , https://github.com/glpi-project/glpi/security/advisories/GHSA-hwjc-8228-55x4 , https://github.com/glpi-project/glpi/releases/tag/10.0.25
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (type per CVE), defect 2 (vector; checked against the GHSA CVSS 4.0 vectors), defect 3 otherwise (scores and ranges match the GHSAs), defect 4 (deployment claim), defect 5 (Swiss sentence).

### 2026-05-08/kaspersky-q1-2026-exploits-and-vulnerabilities-report-docume: no record
- All four defects declined, already fixed by 2026-10-11T1307Z-audit. The current text (veteran CVE list, the 21509/21514/21513 chain, Metasploit back on top) matches https://securelist.com/vulnerabilities-and-exploits-in-q1-2026/119733/

### 2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag: no record
- All five defects declined, already fixed by 2026-10-11T1307Z-audit (Rapid7 primary, no encryption, moderate confidence, single intrusion chain, prose ids gone). The current claims check out against the Rapid7 post.

### 2026-05-09/cve-2025-68670-xrdp-pre-authentication-stack-overflow-arbitr: no record
- All four defects declined, already fixed by 2026-10-11T1307Z-audit. The GHSA page carries the 9.1 vector, the canary text and the `xrdp -v` instruction; Securelist carries the timeline and the backports.

### 2026-05-09/cve-2026-31431-copy-fail-cisa-kev-deadline-2026-05-15-approa: correction, 2026-10-21T12:08:24Z, fields summary, body, sources, evidence
- Applied (residual of defect 2's ground truth): the summary and takeaway gave the `algif_aead` blacklist as the interim fix for every distribution. Red Hat says the module "cannot be blocklisted due to being built into the kernel" and gives `initcall_blacklist=algif_aead_init` (or `af_alg_init`), with a performance warning. Also added: Red Hat's "All fixes are now available" and Xint's seccomp AF_ALG block. New source and evidence quote: RHSB-2026-002 (public 2026-04-30, updated 2026-05-13), which the Red Hat CVE page (the finding's ground-truth URL) links to. Ground truth: https://access.redhat.com/security/vulnerabilities/RHSB-2026-002 , https://xint.io/blog/copy-fail-linux-distributions
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (KEV date 2026-05-01, confirmed in KEV catalogue 2026.10.20), defect 2's FIPS clause, defect 3 (wrong package versions gone, Ubuntu's fixed versions correct), defect 4 (Microsoft "pair" framing), defect 5 (SSH credential stuffing), defect 6 (summary and CVE record).
- Not done: Debian DSA-6243-1. The finding gives no URL for it, and getting one would mean constructing it.

### 2026-05-09/cve-2026-40982-spring-cloud-config-server-pre-authentication: improvement, 2026-10-21T12:08:56Z, fields body, headline
- Applied (residual of defect 4): the body gives HeroDevs' read-only endpoints and information-disclosure impact next to its "read or write" sentence and the I:H vector. The Exposure line cited Spring for what the server can read, which Spring's advisory does not say; it now cites HeroDevs. Headline cut from 154 to 118 characters. Ground truth: https://www.herodevs.com/blog-posts/cve-2026-40982-critical-spring-cloud-config-server-directory-traversal-cvss-9-8
- Declined, already fixed by 2026-10-11T1307Z-audit: defect 1 (CVSS 9.1), defect 2 (type), defect 3 (ranges and fix table; HeroDevs NES not needed), defect 5 (EU claim).

### 2026-05-09/cve-2026-42208-litellm-proxy-pre-authentication-sql-injectio: improvement, 2026-10-21T12:09:39Z, fields title, summary, body, evidence, headline
- Applied (residual of defect 4): Sysdig saw an exploitation attempt with no follow-through, "not a confirmed compromise", but still advises treating exposed instances as compromised. This now appears in the title, summary and body, with a new Sysdig evidence quote. Headline cut from 143 to 119 characters. Ground truth: https://www.sysdig.com/blog/cve-2026-42208-targeted-sql-injection-against-litellms-authentication-path-discovered-36-hours-following-vulnerability-disclosure
- Declined, already fixed by 2026-10-11T1307Z-audit: defects 1, 2, 3, 5 and 6, and defect 4's 36-hour timing. KEV dateAdded 2026-05-08 confirmed.

### 2026-05-09/cve-2026-43284-cve-2026-43500-linux-dirty-frag-deterministic: improvement, 2026-10-21T12:10:33Z, fields cves, sources, sourcing_note, body, headline
- Applied (defect 12): EPSS refreshed from the 2026-09-04 values to FIRST 2026-10-20: CVE-2026-43284 0.9419, CVE-2026-43500 0.0262 (was 0.9286). The new source is the date-pinned query `https://api.first.org/data/v1/epss?cve=CVE-2026-43284,CVE-2026-43500&date=2026-10-20`, the same pattern as the entry's existing 2026-09-04 citation. I fetched it and it returns those values. The finding's undated URL drifts daily.
- Applied (residual of defect 8): the 2026-05-11 section now names "Microsoft's Defender Security Research Team", the post's author. Ground truth: https://www.microsoft.com/en-us/security/blog/2026/05/08/active-attack-dirty-frag-linux-vulnerability-expands-post-compromise-risk/
- Headline cut from 140 to 118 characters. The main analysis was 580 words before this run; it is now 546, after removing the "Copy Fail 2" naming sentence, which the 2026-09-05 section still carries.
- Declined, already fixed by 2026-10-11T1307Z-audit: defects 1 to 7, defect 8 otherwise, 9, 10, 11 and 13. On defect 10, "since 2023" stays: V4bel's README gives 2dc334f1a63a (2023-06-08), and the CNA's 5.3 is only in the uncitable CVE record. On defect 5, the stable version numbers were not added (optional).

### 2026-05-09/daemon-tools-lite-supply-chain-quic-rat-deployed-via-signed: no record
- All seven defects declined, already fixed by 2026-10-11T1307Z-audit. The cited `securelist.com/tr/...` URL is Securelist's canonical English page (the finding's URL serves the same article) and carries "12.6.0.2445".

### 2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption: correction, 2026-10-21T12:11:29Z, fields event_date, sources, body, headline
- Applied (defect 6): `event_date` was 2026-05-08, the analysis date; it is now 2026-05-05.
- Applied (defect 5): DENIC's Final Report of 2026-06-11 added as a source. The main analysis gains its findings: it confirms the initial analysis, rules out compromise and Knot or HSM malfunction, and says the single-HSM test environment did not fully execute the faulty code. The new section lists its measures.
- The 2026-05-10 section reported the "addendum of 11 May 2026", which is after its own timestamp. It now gives the 2026-05-08 interim account and calls that text DENIC's initial analysis; the addendum remains in the 2026-10-11 section.
- Cloudflare post dated 2026-05-06 (was "2026-05") in `sources[]` and in three inline labels. Headline cut from 134 to 116 characters.
- Ground truth: https://blog.denic.de/en/final-report-dns-outage-of-5-may-2026/ , https://blog.denic.de/analyse-des-dns-ausfalls-vom-5-mai-2026/ , https://blog.cloudflare.com/de-tld-outage-dnssec/
- Declined, already fixed by 2026-10-11T1307Z-audit: defects 1 to 4. Defect 6's retype: kind `policy` was set by the 2026-10-11 audit, and the vulnerabilities tag is already gone. `incident` would need a `techniques[]` mapping that a non-adversarial outage cannot support.

### 2026-05-09/enisa-expands-cve-root-four-new-european-organisations-onboa: no record
- Both defects declined, already fixed by 2026-10-11T1307Z-audit (CRA sentence, entity and speculation gone). The current claims match the ENISA release.

### 2026-05-09/german-court-finds-bank-liable-for-sophisticated-phishing-lo: no record
- All three defects declined, already fixed by 2026-10-11T1307Z-audit (no PSD2 or SCA duty; Borncity cited for EUR 218,000 and non-finality; anwalt.de gone; generalisation gone). Checked against heise and Borncity.

## Legacy duties
None in this batch.

## State changes for the main agent
- `state/cves_seen.json`: bump `last_seen` to 2026-10-21 for CVE-2026-42321 (affected range changed), CVE-2026-43284 and CVE-2026-43500 (EPSS changed).
- `entities/registry.yaml`: no change.

## Residuals noticed outside the findings (nothing fixed)
- 2026-05-08/cert-fr-certfr-2026-act-016-agentic-ai-tools-introduce-promp is `kind: threat` for an authority guidance bulletin; `policy` may fit better.
- 2026-05-09/enisa-expands-cve-root-four-new-european-organisations-onboa (`policy`) has no `**Defender takeaway:**` line.
- 2026-05-08/kaspersky-q1-2026-exploits-and-vulnerabilities-report-docume has no `**Exposure:**` or `**Detection:**` line.
- 2026-05-08/muddywater-iran-mois-deploys-chaos-ransomware-as-false-flag omits Rapid7's statement that the actor later published the stolen data on the Chaos leak site.
- 2026-05-09/cve-2026-31431-copy-fail-cisa-kev-deadline-2026-05-15-approa and 2026-05-09/cve-2026-43284-cve-2026-43500-linux-dirty-frag-deterministic each discuss the other through Microsoft's hedge, but neither lists the other in `references[]`. There is no group note, so no link was added.
- In the Dirty Frag entry, the 2026-05-11 section cites RHSB-2026-003 for "CVE-2026-43500 does not affect Red Hat products". The bulletin was updated on 2026-07-03, so that statement may postdate the section; this could not be verified.
- 2026-05-09/denic-de-dnssec-outage-faulty-key-rollover-3-5-h-disruption is `kind: policy` for an operational outage, a stopgap against the empty-`techniques[]` rule.
