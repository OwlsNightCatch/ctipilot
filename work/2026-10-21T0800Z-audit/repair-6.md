# repair-6 report (cleanup wave 02, 2026-10-21T0800Z-audit)

Batch: `work/2026-10-21T0800Z-audit/batch-6.yaml`, 17 entries. Fetched bodies and helpers under `work/2026-10-21T0800Z-audit/repair-6/` (`src/`, `html2text.py`, record summary and section files). No legacy duties in this batch (every entry `legacy_duty: false`), and no em dashes were listed for removal.

Records written: 14 (correction 2, of them 1 internal; improvement 12, of them 3 internal). Entries without a record: 3 (QBUSOFT/Medyc, Storm-3168, Drupal).

## Per entry

### 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning
- Record: improvement, internal, at 2026-10-21T08:06:57Z, fields [body].
- Applied: the shutdown recommendation "even where they are not directly internet-facing, since the possible access route is unconfirmed" is attributed to Kiteworks with its own Heise citation, no longer to the CISO email. Kept to a two-word re-attribution plus the re-pointed citation so the internal record stays inside the changelog-fields word limit. Ground truth: https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html ("KiteWorks recommends shutting down the servers even before this time – even if they are not accessible from the internet. It cannot be said with certainty what potential access routes there might be.").
- Declined: finding 1 (GHSA citation on the 9.4.1 / CVE-2026-54154 clause), already fixed by 2026-10-11T1307Z-audit. Finding 3 ("quoting the advisory"), already fixed by 2026-10-11T1307Z-audit (now "reporting Kiteworks' explanation").

### 2026-09-27/flink-lpg-group-crowdfund-extortion-order-hub-breach
- Record: improvement, at 2026-10-21T08:08:02Z, fields [body, evidence], with section.
- Applied: (1) "The extortion actor behind the breach" becomes "claiming the breach in its emails"; a new evidence row gives heise's sentence in English with the German original. (2) The abuse-report sentence now says the curbing is Flink's account, holds "for now", and the extortionists may look for other routes; "by the Saturday" replaces "as of reporting". (3) The takeaway treats such an email wave as "evidence that an actor holds data from that breach", not as corroboration of its scope. Ground truth: https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html and https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data.
- Declined: none.

### 2026-09-27/pentagon-dmdc-military-personnel-data-breach-unencrypted-ssn
- Record: improvement, at 2026-10-21T08:08:53Z, fields [body, summary], with section.
- Applied: the body's lesson sentence says unauthorized users accessed unencrypted identity data for nine months before discovery, instead of saying the store "kept identity numbers unencrypted and readable for nine months". The summary no longer calls the server "unencrypted"; the files on it held unencrypted data. The takeaway now follows CNN ("encrypt sensitive personnel data ... which the stolen DMDC data lacked") and drops "identifying fields at rest". Ground truth: https://www.cnn.com/2026/09/25/politics/pentagon-data-personnel-breach and https://www.militarytimes.com/news/pentagon-congress/2026/09/24/military-personnel-data-exposed-in-breach-agency-warns/.
- Declined: the headline part of finding 1 was already fixed by 2026-10-11T1307Z-audit.

### 2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor
- No record. Declined: the TVP World date is already 2026-09-25 in the source record and in the body citation, fixed by 2026-10-11T1307Z-audit.

### 2026-09-28/cve-2019-18935-telerik-godzilla-webshell-virtualpathprovider
- Record: improvement, at 2026-10-21T08:11:10Z, fields [body, cves, evidence, summary], with section.
- Applied: Telerik's two prerequisites (encryption the attacker can break or custom keys it knows, plus RadAsyncUpload type whitelisting not enabled) and the per-version table are now in the summary, cves[0].affected/fixed and the Exposure line: encryption breakable up to 2017.2.621, keys needed from 2017.2.711, whitelisting opt-in at 2019.3.1023 and on by default from 2020.1.114, with the recommended settings on every version. The unsourced interim control "restrict or disable the RadAsyncUpload handler" is dropped. AhnLab's mitigation is the upgrade. The 2026-10-11 section's "keys known stays exposed" sentence gains the whitelisting condition. Added a Telerik KB evidence row. Ground truth: https://www.telerik.com/products/aspnet-ajax/documentation/knowledge-base/common-allows-javascriptserializer-deserialization and https://asec.ahnlab.com/en/95561/.
- Declined: none. Part of finding 1 (the 2020.1.114+ key caveat) was already in place from 2026-10-11T1307Z-audit.

### 2026-09-28/openai-agents-unctad-double-encoding-proxy-chain-scan
- Record: improvement, at 2026-10-21T08:12:55Z, fields [body], with section.
- Applied (W1-E item 33): the Triage line no longer names "link-safety checks, uptime monitors". Its premise is now Howard-Jones's description of Urlquery as a scanner that opens any site handed to it in a sandboxed browser, so a relayed request only shows someone submitted the URL; the source-backed request-pattern discriminator is kept. Ground truth: https://swarmcha.se/posts/openai-unctad.
- Declined: W1-E item 4 (label strings), already applied by 2026-10-20T0835Z-audit. The `CHATGPTTEST1`-style strings were replaced by "agent-chosen labels referring to ChatGPT and OpenAI".

### 2026-09-28/storm-3168-jadepuffer-azure-destructive-service-principal
- No record. Declined: `sectors: []` and `priority: notable` were already applied by 2026-10-11T1307Z-audit.

### 2026-10-02/cve-2026-104286-fortimail-path-traversal-zero-day-kev
- Record: improvement, internal, at 2026-10-21T08:13:40Z, fields [body, sources].
- Applied: the CSAF record now carries current_release_date 2026-10-07 and initial_release_date 2026-10-01, and its revision history lists only the initial publication. The 2026-10-06 section therefore no longer dates the record 2026-10-05. The record's source date and citation are now 2026-10-01, its initial release, the same convention the entry uses for the FG-IR-26-175 page; this avoids citing a 2026-10-07 date inside a 2026-10-06 section. The not-affected list (8.0.2, 7.6.7, 7.4.9) is verified unchanged. Ground truth: https://filestore.fortinet.com/fortiguard/psirt/csaf_improper-limitation-of-a-pathname-to-a-restricted-directory_fg-ir-26-175.json.

### 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev
- Record: correction, internal, at 2026-10-21T08:14:16Z, fields [body, sources].
- Applied (W1-B and W1-F, re-derived): the Live Protect guide's source date and section citation are 2026-09-22, the page's "Updated: September 22, 2026"; no July date appears on the page (date meta Oct 6 2026). Content claims re-verified: release 20.18.3, the monitoring and enforce modes, and the two-preceding-releases policy. Ground truth: https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html.

### 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities
- Record: improvement, internal, at 2026-10-21T08:14:50Z, fields [summary].
- Applied (W1-B and W1-F, re-derived): "FTAPI Software of Munich" becomes "FTAPI of Munich". heise and Cybernews both say only Munich-based FTAPI. Ground truth: https://www.heise.de/en/news/Cyber-attack-on-data-exchange-service-FTAPI-11469688.html.

### 2026-10-04/cve-2026-88779-citrix-netscaler-saml-overflow-exploited
- Record: improvement, at 2026-10-21T08:16:07Z, fields [body, evidence, sources], with section.
- Confirmed against the Citrix TechZone blog, which jina can read (last updated 2026-10-03 PDT). It names no indicator-of-compromise script and says only to "follow their standard incident response processes if they identify signs of compromise", so "The Citrix pages for this flaw list no signs of compromise" is kept (narrowed with "for this flaw").
- Applied: the Detection line adds watchTowr's statement as The Register reports it: Citrix provides an indicator-of-compromise script for exposed appliances, though a clean result is not definitive proof. The Register is a new source and evidence row. Ground truth: https://www.theregister.com/security/2026/10/05/citrix-netscaler-security-snafus-get-even-worse-amid-more-0-day-reports/5301232.
- Declined in part: the script is not presented as the vendor's own compromise check for this CVE, and the "nobody process" false-positive note is not added. No Citrix page read carries either, and the watchTowr FAQ URL was not given.

### 2026-10-07/gentlemen-affiliate-azazel-ci-cd-secrets-mcp-attacks
- Record: improvement, at 2026-10-21T08:16:35Z, fields [body], with section.
- Applied: the Exposure line drops "self-hosted" and "unmasked or unprotected" as an observed state and now names GitLab instances whose CI/CD variables or git history hold tokens, keys and database credentials, including removed secrets still in history. Masking and protecting variables is CloudSEK's mitigation. Ground truth: https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files.

### 2026-10-07/ninja-forms-wpc-bundles-stored-xss-hidden-admin-campaign
- Record: improvement, at 2026-10-21T08:17:54Z, fields [body, cves, evidence, sources], with section.
- Applied: CVE-2026-92438 is added to cves[] as the same Ninja Forms flaw, published by another CNA (cvss null, exploited, patch-available, fixed 3.15.4). The body and an evidence row cite the Patchstack database page, which is also added as a source dated 2026-09-22. Ground truth: https://patchstack.com/database/WordPress/Plugin/ninja-forms/vulnerability/wordpress-ninja-forms-contact-form-builder-with-calculators-quizzes-signatures-ai-form-builder-plugin-3-15-3-stored-cross-site-scripting-vulnerability.
- Declined in part: "WPScan" and "CVSS 8.8" are not written, since only the uncitable CVE record carries them.

### 2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale
- Record: correction, at 2026-10-21T08:18:36Z, fields [summary], with section.
- Applied (W1-B and W1-F, re-derived; the draft's "this entry listed" section wording was not reused): the summary separates the firm's customers (police authorities, banks, hospitals, schools, prisons, per AWP) from the organisations reported as concerned (the Établissements de la plaine de l'Orbe and other judicial entities, gendarmerie premises, several banks, several dozen companies, per ICTjournal). Neither report names a hospital or school among them. Ground truth: https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois and https://www.cash.ch/news/top-news/hacker-erbeuten-schweizer-sicherheitsdaten-von-gefangnissen-und-banken-974664.

### 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
- Record: improvement, at 2026-10-21T08:20:53Z, fields [body, evidence, sources, sourcing_note, summary], with section.
- Applied (W1-E item 27): the 25.1.3.0 framing in the summary, Exposure line and sourcing note now rests on Ivanti's own description as numbering authority, read through ENISA EUVD-2026-98816: "Authentication bypass by spoofing in ICS before version 25.1.3.0 ...". Rapid7's table and CERT-FR's contrary list ("25.1.3.x antérieures à 25.1.3.1") stand beside it, and 25.1.3.1 stays the target. The section adds Rapid7's relay that part of the flaw was patched in the July 2026 release 25.1.3.0. EUVD page added as source and evidence. EUVD is a JS-rendered host, so the verifier checks that quote by hand; the API body is saved at `repair-6/src/euvd/ivanti-search.json`. Ivanti's hub advisory remains a JS shell to extract and WebFetch. Ground truth: https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-98816, https://www.rapid7.com/blog/post/etr-ivanti-connect-secure-zero-day-exploited-in-the-wild-cve-2026-104935/, https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-013/.

### 2026-10-14/exchange-oct-2026-su-cve-2026-70571-last-2016-2019-update
- Record: improvement, at 2026-10-21T08:21:59Z, fields [body], with section.
- Applied (W1-E item 26, the pre-existing part): the 2026-10-16 section is re-cited to what each page carries now. The release post's change log records the 2026-10-15 banner and its 2026-10-16 replacement by a link. The follow-up post carries the KB list, MapiExceptionMdbOffline with event 1006, and the growing queues. "Investigating with its Windows partners" and "names no workaround" appear on no page now and are dropped. Ground truth: https://techcommunity.microsoft.com/blog/exchange/released-october-2026-exchange-server-security-updates/4563014 and https://techcommunity.microsoft.com/blog/exchange/exchange-servers-may-become-unstable-after-installation-of-october-2026-windows-/4565382.
- Declined: the duplicate-evidence half of item 26, already handled by 2026-10-18T1307Z-audit.

### 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce
- No record. Decision on W1-H / W1-E item 30: neither a publisher edit nor a wrong entry. Read through jina, the advisory carries "CVE IDs: CVE-2026-108097", both evidence quotes verbatim and the Critical 19/25 risk line.
- Cause of the flags: the container gets drupal.org's "Client Challenge" JavaScript wall on both direct transports. check_run keeps script blocks in page text, so the challenge body has a 1016-character skeleton, above the 600-character floor, and is compared as if it were the advisory. It contains neither the id nor the quote. Body saved at `repair-6/src/drupal-sa-jina.md`, challenge body at `repair-6/src/drupal-sa.md`.

## State changes the main agent must apply

- `state/cves_seen.json`: add `CVE-2026-92438` with first_seen and last_seen 2026-10-21, primary_source_url the Patchstack database URL above, and title "Ninja Forms up to 3.15.3 stored XSS, the same flaw as CVE-2026-94504 published by another CVE Numbering Authority; fixed in 3.15.4". Until this lands, `check_run --all` FAILs `cve-sync` on the Ninja Forms entry. This is the only FAIL on this batch's entries.
- `state/cves_seen.json`: bump `CVE-2019-18935` last_seen to 2026-10-21, because its cves[] record changed. Its title still says "patched since 2020.1.114"; optionally align it with the prerequisite wording.
- `entities/registry.yaml`: `incident:ftapi-ransomware-gentlemen-claim-2026-09` summary starts "FTAPI Software of Munich". Change it to "FTAPI of Munich" to match the entry and its sources.

## Residuals noticed (not fixed)

- tools/check_run.py page checks: drupal.org's "Client Challenge" wall clears `_MIN_PAGE_SKELETON` because script blocks are kept, so every drupal.org citation gets false quote-literal and citation-cve flags. Either add drupal.org to `_JS_RENDERED_HOSTS` or detect challenge bodies. `fetch_source.py url` also does not treat this challenge as a block, so it does not fall back to jina.
- UNCTAD entry, 2026-10-02 section: it still cites Transluce's request tag beginning with "oai", an attribution marker string. This is borderline for the no-marker-indicator rule; it is not the payload labels of item 4.
- Telerik and UNCTAD entries label their detection paragraph "**Detection and hunting.**" rather than the fixed "**Detection:**" string the site lifts.
- Flink takeaway: "is itself worth watching for as this technique's next evolution" is an unsourced forecast.
- Citrix TechZone blog: the jina read shows Published Time 2026-10-04T01:42Z, which is 2026-10-03 PDT and matches the page's "Last Updated on: October 3, 2026". The cited date is fine; no action.
