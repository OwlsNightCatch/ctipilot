**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-14T06:05:28Z · ended_at=2026-08-14T06:27:36Z · duration_seconds=1328
**Self-telemetry:** urls_checked=41 · webfetch_calls=18 · bridge_fetches=47 · websearch_calls=3

## Verification report — 2026-08-14T0417Z-intel (iteration 3)

Read cold: all 12 entries end-to-end plus the run record, `prior_coverage.json` (164 records), `entities/registry.yaml`, and the 2026-05-20 and 2026-08-05 update targets. Every inline source URL on every entry was fetched in this iteration except where noted under *Transport limits* below. Every `evidence[]` quote was tested as a contiguous verbatim substring of the fetched page — all 24 passed, including the double-space artefact in Fortinet's FG-IR-26-158 summary and the zero-width characters in the Reuters Philips quote.

### Citation does not support the claim

**F2 — `2026-08-14/fortinet-august-2026-fortiweb-radius-wildcard-admin-bypass`: the Dutch 5.3 figure is still cited only to Fortinet's own feed.**

The entry says:

> "a FortiWeb WAF Content-Encoding evasion (FG-IR-26-157 / CVE-2026-70466, which Fortinet scores CVSS v3 4.8 and the Dutch advisory 5.3), a stack buffer overflow in the FortiOS explicit-proxy daemon (FG-IR-26-161) … ([Fortinet PSIRT advisory feed](https://filestore.fortinet.com/fortiguard/rss/ir.xml))"

The only citation terminating that sentence is the Fortinet RSS feed. I fetched `https://filestore.fortinet.com/fortiguard/rss/ir.xml` and parsed all 50 items: the FG-IR-26-157 item reads `CVSSv3 Score: 4.8` followed by the CWE-184 summary, and no item in the feed carries a national-CERT score of any kind. The 5.3 comes from `https://advisories.ncsc.nl/2026/ncsc-2026-0300.html`, which I also fetched — its CVE list reads `CVE-2026-26035 - CVSS (v3) 9.8` / `CVE-2026-70466 - CVSS (v3) 5.3`. That advisory is cited elsewhere in the entry but not on this clause, which makes the omission an internal inconsistency too: the entry attaches an inline NCSC-NL link to both of its other divergence claims (9.8 and 8.1) and only this one goes uncited. Attach the NCSC-2026-0300 URL to the 5.3.

### Unsupported / hallucinated facts

**F1 — `2026-08-14/fortinet-august-2026-fortiweb-radius-wildcard-admin-bypass`: the frontmatter summary undercounts what the Dutch CERT carried, and contradicts the entry's own body.**

Frontmatter `summary`:

> "Fortinet published eight advisories on 2026-08-12, two of which the Dutch national CERT carried the following day."

I fetched both Dutch advisories. NCSC-2026-0300 (published 13-08-2026 15:26) lists under *Referenties*: `https://fortiguard.fortinet.com/psirt/FG-IR-26-157` **and** `https://fortiguard.fortinet.com/psirt/FG-IR-26-158`. NCSC-2026-0299 (13-08-2026 15:24) lists `https://fortiguard.fortinet.com/psirt/FG-IR-26-160`. That is **three** of the eight Fortinet advisories, carried in **two** Dutch bulletins — which is exactly what the body and the sourcing note say:

> body: "of which the Dutch national CERT carried the FortiWeb pair and the FortiManager flaw to European constituents in two separate advisories the next day"
> sourcing_note: "The two Dutch advisories cover the FortiWeb pair and the FortiManager flaw separately"

The summary's "two of which" attaches to the eight Fortinet advisories and is therefore wrong on its own terms and inconsistent with the rest of the entry. The summary is the machine-consumed field and renders at the top of the brief. Rewrite to something like "three of which the Dutch national CERT carried the following day in two advisories".

(The rest of the Fortinet entry re-derives clean from the primaries. I fetched all eight FG-IR-26-15x/16x advisory pages: the batch is exactly eight dated 2026-08-12 per both the advisory pages and the feed; CVE-2026-26035 / 8.8 / internally discovered / Known Exploited: No / 8.0.0–8.0.2, 7.6.0–7.6.6, 7.4.0–7.4.11, 7.2.0–7.2.12 → 8.0.3 / 7.6.7 / 7.4.12 / 7.2.13 / wildcard workaround; CVE-2026-70468 / 7.3 / CWE-288 / FortiManager 8.0 not affected / `fgfm-peercert-withoutsn`; CVE-2026-70465 / 7.3 / CWE-120 / Impact "Escalation of privilege" / Nir Chako of Pentera / 7.4.4 and 7.2.12 / EMS application-based-filtering workaround; and the five uncovered advisories are each correctly characterised and are all lower-severity. The SecurityWeek wildcard quote and the "makes no mention of any of these vulnerabilities being exploited in the wild" line are both verbatim.)

### Needs more research

**F3 — `2026-08-14/ncsc-uk-bitlocker-pin-winre-fallback-controls`: the guidance names four mitigations, not three, and the fourth is the one the other three do not cover.**

Headline: *"three named alternatives cover the devices that cannot take one"*; body: *"gives three alternatives with different trust models rather than leaving those endpoints uncovered"*.

I fetched `https://www.ncsc.gov.uk/blogs/how-bitlocker-pins-help-protect-your-data-and-devices`. Under "What if I can't use a PIN?" it carries four headed techniques: *Use the same PIN*, *Use Network Unlock*, *Create a Startup Key*, and *Conditional access* — "Finally, if there is no way to add pre-boot authentication to your device, consider how you are going to manage that additional risk. For example, you may wish to use conditional access policies to prevent these high-risk devices from accessing sensitive resources." The fourth is absent from the entry entirely, and the source's own framing refutes the claim that the three *cover* the devices that cannot take a PIN: conditional access exists precisely for the residue the three do not reach. For the constituency this entry is written for — a public-administration laptop estate whose exception list is the risk register, as the entry itself argues — a device-risk-based conditional-access policy is the most directly actionable item in the guidance. Add it and correct the count and the "cover" framing.

Everything else in this entry checks out against the page: both evidence quotes verbatim; "Whilst this issue was quickly patched" follows immediately after the YellowKey/WinRE sentence, so the entry's reading of *this issue* as YellowKey is right; "In 2025, Microsoft found and patched four very similar bugs"; "considerably more protection than not using a PIN"; "For desktop devices, this is often the best option"; the TPM-**and**-Startup-Key caveat; "don't do nothing". The page names no CVE and no CVSS, and the `cves[]` record's 6.8 / `AV:P` / `poc-public` carries forward from the 2026-05-20 update target's MSRC sourcing, which is consistent with the store and with the registry's YellowKey → `actor:nightmare-eclipse` linkage.

### Missed angles

**F4 — WordPress 7.0.4 / CVE-2026-65640 is in-window, was published by a source this run used, and is neither in the brief nor in the documented drops.**

`https://www.securityweek.com/wordpress-7-0-4-patches-remote-code-execution-vulnerability/` — Ionut Arghire, 13 August 2026 08:53 ET, squarely in the 26-hour window and the same author/outlet/news-cycle as the Fortinet entry's corroborating source. WordPress 7.0.4 fixes CVE-2026-65640, CVSS 8.8: "Attackers with Author-level user or higher permissions could exploit the flaw via malicious Postscript files", limited to installations with Imagick and Ghostscript, with the fix "backported to all branches back to 4.7" and no exploitation reported.

I do not assert this clears the vulnerability gate — it is post-auth with a component precondition, and a defensible drop. What makes it a finding is that it is a *silent* one: the run record enumerates its drops (GitLab, Palo Alto and Chrome August batches, the stale MOVEit re-mirror, the twelve-advisory Siemens/JCI/AVEVA/Hitachi ICS batch) and WordPress is not among them, while WordPress Core is one of the store's most active threads with a direct home-region nexus — `2026-08-08/ncsc-ch-clickfix-wp2shell-etherhiding-vidar-swiss-websites` (Swiss websites compromised through WP2Shell), `2026-08-10/wordpress-core-xss2shell-cve-2026-64638-preauth-xss-to-rce`, `2026-08-10/wp2root-php-uaf-copy-fail-kev-kernel-lpe-to-native-root`. A reader on this store alone, running a multi-author WordPress estate, currently learns nothing about the release. Publish short or record the drop. Suggested query: `WordPress 7.0.4 CVE-2026-65640 Imagick Ghostscript`.

### What I checked and found clean

- **Adobe Commerce (`cve-2026-71362-…`), re-derived from Adobe's own per-CVE table via the bridge.** APSB26-92, 11 August 2026, seven CVEs of which five are Critical. The CVE-2026-71362 row reads: Incorrect Authorization (CWE-863) · Privilege escalation · Critical · Authentication required to exploit: **No** · Exploit requires admin privileges: **No** · **9.1** · `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`. Every one of those matches the entry's body and `cves[]` record exactly. Affected-version tables match: Commerce 2.4.4–2.4.9, B2B 1.3.3/1.3.4/1.4.2/1.5.2/1.5.3, Magento Open Source 2.4.6–2.4.9, all "-2026-jul and earlier", remediated to the matching "-2026-aug". "Adobe is not aware of any exploits in the wild for any of the issues addressed in these updates" is verbatim. On the exploitation split: Sansec's page (fetched raw) says only "Sansec Shield already blocks exploitation attempts" with **no timing and no observation of arrival**, and the timed claim appears only in SecurityWeek ("Shortly after Adobe's advisory was published, Sansec warned that it blocked the first exploitation attempts targeting the CVE." — verbatim). The entry attributes the timing to SecurityWeek in title, headline, summary, body and sourcing note, and says plainly what Sansec's own page does and does not carry. No claim about exploitation is stronger than its source. Sansec's isolated-patch / no-Composer-package / latest-`-p`-release points are all verbatim on its page.
- **Langflow.** All three GHSAs fetched. GHSA-cf6m-vc3m-7cgm: Critical, `>= 1.7.0, <= 1.9.0`, patched 1.9.1, `WEBHOOK_AUTH_ENABLE` default-False quote and the flow-UUID quote both verbatim, no CVE. GHSA-jxw3-mjmx-3pqm: Critical 9.1, `<= 1.10.0` → 1.10.1, Mersenne-Twister seeding, raw-key-as-Fernet-key for ≥32 chars, SHA-256 fix, the "MCP path traversal in this repo" quote verbatim, the re-enter-credentials-under-32-chars instruction present. GHSA-w584-2h2r-2hvf: `/api/v1/validate/code` uses `exec()`, decorators evaluated at definition time, no authentication until v1.7.2, any user under `AUTO_LOGIN` from v1.7.2–v1.10.0, fixed 1.10.1, and it explicitly resolves the duplicate default-argument advisory GHSA-xjq8-cqrm-7m4x. `update_of` correctly targets the 2026-08-05 CVE-2026-9198 KEV entry, and the entry states its three paths are distinct root causes.
- **City-Forum (deep dive).** Reco and The Register both fetched. Verbatim: the UI-API/no-public-tool quote; v56.0→v66.0; passive DNS to March 2025; `POST /api/now/sp/search` returning HTTP 201 for authenticated and anonymous alike; the target-sector list; "Allow guest users to access public APIs" and the explicit statement that removing `API Enabled` does not close it; `AuraRequest`/`Sites` `EventLogFile` types and the `/webruntime/api/services/data/v` tell; `sp_portal` → `m2m_sp_portal_search_source` → `sp_search_source`, `gs.isLoggedIn()`, `GlideRecordSecure`; "the log records the request, not the POST body"; ShinyHunters named. The Register: the Bachrach quote verbatim, "the busiest Salesforce target logged more than 560,000 events", the self-registration probing, ServiceNow's statement, Salesforce's non-response, "at least 17 months". The cross-reference to "the Swiss authority's advisory of 2026-08-04" is correct — `2026-08-05/ncsc-ch-power-pages-dataverse-anonymous-access-advisory` carries `event_date: 2026-08-04`.
- **JWR (Talos).** Both evidence quotes verbatim; medium confidence on the Outsider-variant assessment is Talos's own wording; 44 pages and 40+ instructions; the FBI "Ghost Hook" takedown of June 2026; the Singapore land-transport / national-postal / UAE-toll / SEA-courier lure set. `verification: single-source` with an accurate no-carve-out note.
- **Armored Likho (Securelist).** All three evidence quotes verbatim; Eagle Werewolf alias; May 2026; Rust/Tauri donation-app dropper; exactly three `SeBackupPrivilege` fallbacks including Shadow Copy and Robocopy backup mode; Telegram session used to authenticate to the API; dead-drop resolver after three days of C2 silence in a forked repository; Russia-only victimology across individuals, corporate, government, IT and education. The entry states the absence of a regional nexus and justifies inclusion on transferable tradecraft. No IOCs carried over from a source that is full of them.
- **Check Point Q2 2026.** Both evidence quotes verbatim and contiguous, including the trailing "genuine first party evidence…" clause. Every figure re-derived from the page: 57.6% / 71% / 71→93 / 2,139 victims flat (+0.8%) QoQ / Qilin 279 for a fourth straight quarter with its count down 17% / The Gentlemen +62% to 269 and outpacing Qilin in June / payment rates near 23% from 85% in 2019 / US share 50%→42%. Framed throughout as Check Point's leak-site measurement.
- **DGFiP.** Actu17 and ZATAZ both fetched (ZATAZ 403s WebFetch; the bridge returns it). The ministry quote, the late-June cut during a control operation, 678,000 lines with a ~1,100-line sample, the internal-VPN-to-taxpayer-search-application route as Fuites Infos's account, the field list, "aucun mot de passe ni identifiant de connexion ne serait concerné", the unsubstantiated tens-of-millions estimate, ANSSI/CNIL/plainte — all present. ZATAZ's lede confirms the second claim appeared "dans le même forum pirate" and concerns "près de deux millions de propriétaires", and the "Cette fois, aucun VPN…" quote is verbatim and does belong to the ~2 million claim (the same quote block carries the 2,041,778 figure and the still-connected-to-the-panel offer). Attribution discipline is exact throughout: the ministry confirms only access, usurpation, and consultation/extraction.
- **Cl0p / Philips / Shell.** Both Reuters(WKZO) evidence quotes verbatim including their embedded zero-width characters; all four company statements match; Ransom-ISAC 22 July; Brandon Parsons of Ascent Solutions and the 19–20 July notice window. ZATAZ confirms the 12 August leak-site addition, 89 GB / 13.5 GB, the Shell and Philips data categories, and that the volumes are the criminals' unverified claims. The entry does not assert the Windchill link and says so.
- **Beacon.** Both sources fetched; every claim supported, including the 01:20:16 UTC 27 July start, one hour 27 minutes, the 27–28 July transfer spike, no persistence, all AWS-integrated credentials reset, "no indication that the threat actor has published the stolen data online or otherwise misused it", and the ICO's conclusion that The Survivor's Trust holds no responsibility. Simpson's quote verbatim from The Register.
- **Coverage shape.** All four `update_of` targets are the right stories and each entry carries only its delta. No new entry duplicates in-window coverage: I walked the 164 prior-coverage records against every CVE and entity in this run. Twelve entries in 26 hours is a large window, and I looked hard for a marginal inclusion — I could not defend a drop on any of them. The three softest (Haiwell, Armored Likho, Check Point) each carry an explicit, honest relevance argument: an unpatched pre-auth root on an OT edge gateway in named energy/water sectors where the only response is an exposure check; three actor-agnostic primitives with a stated absence of regional nexus; and a scoping correction that breaks brand-based leak-site triage. Volume follows relevance here rather than padding.
- **Style, actions, classification.** Zero IOCs, zero rule code, no vanity self-metrics, English throughout, no workflow-internal vocabulary in any entry or in the run-record notes. Eight `actions[]` items across twelve entries, every one concrete and derived from its own entry's mechanics; four entries correctly ship empty. No `org_triage` block and no `watchlist_hit`/`watchlist` anywhere, which is correct for this profile. Every entry carries an Admiralty `classification` with in-vocabulary codes, and the reliability letters match the source tier (A for vendor PSIRT / CISA / NCSC UK primaries, B for research labs and news-sourced incidents); the credibility numbers match the corroboration each entry actually shows, and the run record explains the one-assessor-two-publishers reasoning that keeps Langflow, Beacon and City-Forum at 2.

### Transport limits (not findings)

- **CISA (`icsa-26-225-02`, the Haiwell entry's sole source) could not be reached from this container.** I escalated the full ladder: `fetch_source.py cisa page`, `fetch_source.py url`, the CSAF JSON path under `/sites/default/files/csaf/`, the ICS-advisories RSS, `raw.githubusercontent.com/cisagov/CSAF` on all three branch names, the GitHub code-search API, and two third-party mirrors. Direct returns HTTP 403 and every jina key in the pool returns HTTP 402 balance-exhausted (the run record already logs the pool exhaustion under `zscaler-threatlabz`). NVD's API returns nothing for CVE-2026-19188 and WebSearch surfaces no substantive coverage. I therefore raise **no finding** against this entry — I did not verify it independently, and the rule is that a finding must not rest on my own fetch failure. As a consistency check only, the entry matches the page text the research pass captured in `work/2026-08-14T0417Z-intel/p_cisa_haiwell.clean.txt` on every point (CVE id, the cmdPing/`/setting` quote verbatim, root privileges, version 3.40.1.12, CVSS 10 on both 3.1 and 4.0 with the vector string the entry prints, the Energy / Critical Manufacturing / Water and Wastewater sector list, the Fiqram Akmal credit, and the absence of any vendor fix line), and its `verification: single-source-national-cert` value, carve-out sourcing note and A/2 classification are all correct for that basis. This is the second consecutive iteration unable to reach the host; the operator signal is the exhausted reader pool, not the entry.
- **BSI CERT-Bund WID-SEC-2026-2828** (corroborating source on the Langflow entry) resolves HTTP 200 but renders as an Angular shell; the portal's JSON path is not reachable without the reader. The URL is live and is not a broken or generic link, and the entry's three vendor primaries carry every claim, so no finding — but its content is unverified this iteration.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 0)

Two of the four are narrow and mechanical (F1, F2, both on the Fortinet entry — one a count in the summary that its own body contradicts, one a citation that the previous iteration's remediation moved but did not finish). F3 adds a mitigation the source names and the entry dropped. F4 is a completeness signal on a thread with a home-region nexus and does not necessarily require a new entry. Nothing here touches the run's attribution discipline, quote fidelity or relevance shape, which are the strongest I found in this read.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: trending-vulnerabilities
  item: "2026-08-14/fortinet-august-2026-fortiweb-radius-wildcard-admin-bypass"
  url_or_quote: "Fortinet published eight advisories on 2026-08-12, two of which the Dutch national CERT carried the following day."
  summary: "Three of the eight were carried, in two Dutch advisories: NCSC-2026-0300 references FG-IR-26-157 and FG-IR-26-158, NCSC-2026-0299 references FG-IR-26-160. The body and sourcing_note both say it correctly; only the summary is wrong."
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "2026-08-14/fortinet-august-2026-fortiweb-radius-wildcard-admin-bypass"
  url_or_quote: "which Fortinet scores CVSS v3 4.8 and the Dutch advisory 5.3 ... ([Fortinet PSIRT advisory feed](https://filestore.fortinet.com/fortiguard/rss/ir.xml))"
  summary: "The feed carries 4.8 for FG-IR-26-157 and no national-CERT score; the 5.3 is in NCSC-2026-0300, which is not cited on this clause though it is cited on the entry's other two divergence claims."
- code: F8
  category: needs-more-research
  section: trending-vulnerabilities
  item: "2026-08-14/ncsc-uk-bitlocker-pin-winre-fallback-controls"
  url_or_quote: "three named alternatives cover the devices that cannot take one"
  summary: "NCSC UK names four techniques, the fourth being conditional access for devices where no pre-boot authentication is possible; the entry omits it and the 'cover' framing contradicts the source."
- code: F10
  category: missed-angle
  section: trending-vulnerabilities
  item: "WordPress 7.0.4 / CVE-2026-65640 — Imagick/Ghostscript RCE"
  url_or_quote: "https://www.securityweek.com/wordpress-7-0-4-patches-remote-code-execution-vulnerability/"
  summary: "In-window (13 Aug 2026), published by a source this run used, absent from both the brief and the documented drops, on a WordPress Core thread with a live home-region nexus. Publish short or record the drop."
```
