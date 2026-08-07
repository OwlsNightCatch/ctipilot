**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-07T05:01:36Z · ended_at=2026-08-07T05:22:17Z · duration_seconds=1241
**Self-telemetry:** urls_checked=21 · webfetch_calls=6 · bridge_fetches=5 · websearch_calls=1

## Verification report — 2026-08-07T0411Z-intel (iteration 1)

Read cold, no prior-iteration deltas. All 8 entries read end-to-end (frontmatter + body), plus the run record, `prior_coverage.json` (140 records), `entities/registry.yaml` records for all 7 referenced keys, `state/cves_seen.json`, `triage.json`, `findings.S{1..4}.yaml`, `sources/sources.json` reliability letters and the pinned ATT&CK v19.1 dataset.

**What I verified positively** (so the main agent knows what not to re-litigate):

- **Every cited URL returns HTTP 200** — 16 distinct source URLs plus 5 authority pages I pulled for cross-checking. No 404, no homepage redirect, no listing index. One caveat filed as F11 (the NCSC-NL JS stub).
- **All seven Keycloak CVEs check out against Red Hat's own per-CVE records** — id, CVSS base score, vector, severity and mechanics: 16443 7.4 `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N`, 16442 7.4 (same vector), 15572 8.8 `PR:L`, 16102 8.1, 15573 8.1, 16071 5.4, 16100 6.5. The `auth` field on each `cves[]` record matches its own vector's PR value. Both `evidence[]` quotes are contiguous verbatim substrings. CERT-FR CERTFR-2026-AVI-0976 independently carries the version boundaries verbatim ("Keycloak versions 26.6.x antérieures à 26.6.5"), is dated "Paris, le 06 août 2026", and lists the same seven CVEs and seven GHSA ids. **The sourcing substitution is defensible and the `role` ordering is right** — Red Hat is a first-party vendor authority for both named products, CERT-FR is co-primary for the version envelope only, and the summary's "in keycloak-services" scoping (which the human-readable pages do not show) is in fact backed by Red Hat: all seven Bugzilla records carry `package_name: keycloak-services`. I confirmed independently that OSV still 404s all seven and that the reader-facing `access.redhat.com/security/cve/<id>` pages resolve and carry the quoted text.
- **All seven Adobe rows transcribed correctly, none positionally.** Adobe's table order is category/impact/severity/score/vector/CVE and every one of the seven maps as the entry states, including the three shared `S:C` 10.0 rows, the `PR:L` on 48326 and 48317, `S:U` on 48333 and 48399, and every CWE (918, 1336, 89, 89, 863, 95, 657). "Date Published: August 3, 2026", "ACC v7: 7.4.3 build 9398 and earlier", priority 1, both `evidence[]` quotes verbatim, and the 2026-08-11 CVE-consolidation note all confirmed.
- **The UNC6671 hedge holds everywhere I looked** — title, headline, summary, body, `sourcing_note` and the `actor:unc6671` registry summary all carry the linkage as GTIG's assessment with the alternatives named. No over-claim survived. The `$750,000` figure is quoted exactly as GTIG frames it and is not presented as an all-case average. Every other GTIG number checks: 18 wallets / 141.65 BTC / ~$10.69 M / Jan 7–May 12 2026, the May 11 shutdown notice, $1 M–$3 M demands with 50–75 % reductions, one domain every 1.6 days vs 2.2 days (28 root domains, Apr 1–May 31), the three-phase targeting progression, and every detection and session-control recommendation.
- **Meta attribution boundaries are correct.** Reuters (reached via the bridge's jina rung after `WebFetch` refused the host; Published Time 2026-08-05T22:29:02Z) carries the Meta quote, both Irregular quotes, the white-paper statement, The Information's Muse Spark 1.1 attribution, and — verbatim — the root-cause split: "The incidents at Meta and Anthropic stemmed from configuration errors... In OpenAI's case, an AI agent independently exploited a previously unknown vulnerability." Anthropic's post carries the Irregular quote verbatim, "Neither we nor our evaluation partner were aware of this misconfiguration until we detected it through our additional evaluation monitoring", and "The two organizations we were able to reach had not previously detected the activity". Nothing is conflated. All three `references` ids exist in prior coverage.
- **No IOCs anywhere.** This is genuinely well done and I checked it aggressively. GTIG publishes ~15 phishing domains, residential-proxy IPs and UA strings; Jamf publishes SHA-256 hashes, `cdn.zoom.com[.]kg` paths and `hub.zoom.com[.]kg:5173`; Microsoft publishes domain names and `/curl/<hex-id>` paths; Sonatype publishes package names, the 35.x.y version range and `/pkg/update_win.exe`; Unit 42 publishes a UA string and 14 IPs. **None of it appears in any entry or in any registry summary I read.** The Flooding Dropper entry's decision to describe the naming *convention* without the terms is correct, and the deep dive's "authentication vocabulary — passkey, mfa, sso — with a verb" is GTIG's own generic characterisation, not an indicator.
- **Recency (question 6): I agree on Flooding Dropper.** Sonatype's `datePublished` is 2026-08-05T20:43:17Z, ~5.5 h before window start, and the post says in terms that the campaign is active and "The campaign's naming convention is already evolving". That is what the developing-story window is for, not a stretch. (It surfaced a second and third out-of-window primary that the record does not account for — F11.)
- **Priority calibration (question 8): both `high` values are defensible; neither is really `notable`.** Keycloak carries a pre-auth SAML-assertion forgery in the identity broker sitting in front of European public-sector federated login — the blast radius is every application behind the realm, and that clears the TL;DR bar without exploitation. Adobe's own mechanics force the timeline in a stronger way still: the affected range *includes the build that was last week's remediation*, so operators who did the right thing are still fully exposed and don't know it. Three pre-auth CVSS 10.0 code-execution paths on a self-hosted, internet-adjacent platform at Adobe priority 1 is beyond-patch-cycle on the exposure limb alone. No `critical` is correct — no exploitation and no public PoC for either.
- **Dedup and update-vs-new decisions are right.** UNC6671/BlackFile/Helix/ClickFix-macOS/Keycloak/Overlord/Sonatype/Jamf return zero hits in the 14-day prior-coverage index (the 2026-07-10 Helix entry is outside it), so eight new entries and zero `update_of` is correct. The Meta entry correctly uses `references` rather than `update_of` — it is a new disclosure in an existing cluster, not a delta on one of them. No CVE in this run appears in `state/cves_seen.json` under an earlier `first_seen`; the two 2026-08-02 Adobe CVEs are correctly distinct ids.
- **Single-source discipline (F12): clean.** All four lab entries carry `verification: single-source` plus a `sourcing_note` that names the basis and explains the credibility-2 choice, and the run record lists them. No missing flag.
- **Classification (F17): no findings.** Every entry carries exactly one `classification` block, all codes in vocabulary, no `org_triage` block anywhere, no `watchlist_hit: true` and no `watchlist` tag — correct for a profile with no triage scheme and no watchlists. Letters do not outrun the sources: `A` on Adobe matches `adobe-psirt` rel=A and `A` on Keycloak rests on a vendor PSIRT plus `anssi-fr` rel=A; `B` on GTIG/Microsoft/Jamf/Sonatype/Unit 42 matches `mandiant-gtig`/`msft-ti`/`jamf-threat-labs`/`sonatype`/`unit42` all rel=B. Credibility 2 on the four uncorroborated lab posts is exactly right, and the 1s rest on real second parties.
- **ATT&CK: every id in all eight entries exists and is active in the pinned v19.1 dataset**, including the v19 renames — `T1685` (Disable or Modify Tools) is correctly used where the revoked `T1562.001` would have been wrong, and `T1204.004` (Malicious Copy and Paste) is the right ClickFix mapping. No bare ID lists in prose. Two mappings outrun their body (F11).
- **Style: clean.** No vanity metrics (the $10.69 M and the ~$1 M are incident costs tied to named analysis, not marketing figures), no product-efficacy claims, no workflow-internal language in any entry or in the run-record notes, English throughout.

**Coverage (question 9): I found no omission I can name a plausible in-window source for.** I read every drop rationale in `triage.json` and the S2/S4 findings records behind the four closest calls and I uphold all four. The two Swiss leak-site claims (MITC AG / bravox, Pharma Test Apparatebau AG / akira, both 2026-08-06 and both in window) are leak-site claim only with no victim statement and no A/B journalism — a home-region nexus does not buy a pass on the fake-news gate, and publishing them is how a brief teaches its readers to discount it. The French healthcare pair is the genuinely close call and I agree with the drop on actionability rather than nexus: Biosynex and Hospices Civils de Lyon are victim statements with no vector, no actor and no technique, both explicitly stating no health data was affected, over a third-party-supplier pattern this store already carries — there is no telemetry a reader could match and no task they could start. The Snowflake plea and the hedged SharePoint CVE narrowing are correctly dropped for the reasons given (the latter especially: both candidate CVEs are already in the store and the source itself hedges). I also re-checked the KEV negative independently in outline and found nothing that contradicts the record, and one time-boxed sweep for in-window actively-exploited advisories surfaced only the N-able N-central chain (2026-08-01/02, outside both windows, and already present in this store via the 2026-08-04 PhantomKiller entry). **Coverage looks complete.**

### Citation does not support the claim

**F3.1 — `macos-clickfix-server-side-fingerprinting-gate-amos`: the Gatekeeper claim is the opposite of what the sole cited source says.**

The entry's Defender takeaway asserts:

> "Hardening removes the step entirely rather than detecting it: **Gatekeeper and notarisation enforcement stop the unsigned payload**, and endpoint policy that prevents terminal execution driven by clipboard paste breaks the ClickFix pattern..."

I fetched the entry's only source, `https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/`. Microsoft states the reverse, and states it as the reason ClickFix works on macOS at all:

> "Because execution starts from a user-run Terminal command rather than a downloaded app bundle, the flow can avoid parts of the normal macOS application trust path, including quarantine handling, code-signing evaluation, and notarization checks typically applied to downloaded applications."

The substring `Gatekeeper` occurs **0 times** in the post; `unsigned` occurs **0 times**; `quarantin` occurs once, in the sentence above. Microsoft's own mitigation list (Educate users / Monitor Terminal usage / Detect native-tool abuse / Inspect outbound downloads / Protect credential stores / Monitor data staging / Block on infrastructure / Hunt the generation pattern) contains no Gatekeeper or notarisation lever.

This is not only unsourced, it is wrong in a way that would misdirect a reader — and the store already says so: the registry record `campaign:clickfix-macos-2026` reads "Base64 Terminal-paste lures that **bypass Gatekeeper**". Remove or invert the clause.

**F3.2 — same entry: "macOS does not gate that natively" is contradicted, and the real native mitigation dropped out.**

> "...endpoint policy that prevents terminal execution driven by clipboard paste breaks the ClickFix pattern no matter how well the gate evades pre-delivery inspection — **macOS does not gate that natively**."

Microsoft documents exactly that native gate, in the same mitigation section:

> "On macOS 26.4 and later, Apple introduced a mitigation that displays a warning when a user attempts to paste a potentially malicious command into Terminal, directly addressing the ClickFix delivery mechanism."

and reproduces the prompt text ("Possible malware, Paste blocked / Your Mac has not been harmed. Scammers often encourage pasting text into Terminal..."). Two fixes are needed in one place: correct the clause, and carry the macOS 26.4+ version floor as the hardening lever. It is the most directly actionable line in Microsoft's guidance — a concrete OS version that removes the delivery step — and it is the one thing a macOS fleet owner would act on this week.

**F3.3 — `ai-api-token-jacking-transfer-station-resale`: "CI logs" is not in the Unit 42 post.**

Body: *"...through infostealer malware, phishing, credentials leaked in poisoned packages, or **keys exposed in source repositories and CI logs**"* — with the Unit 42 citation attached. Frontmatter summary repeats it ("credentials leaked in repositories and CI logs"), and `actions[2]` builds on it ("appearing in a public repository or **a CI log**").

I fetched `https://unit42.paloaltonetworks.com/ai-token-jacking/` and read the acquisition section in full. Unit 42's vectors are: privileged developer accounts harvested "via information stealers or through phishing campaigns"; stolen already-provisioned keys; keys mined "from improperly secured file shares or code repositories"; and "poisoned, self-propagating npm packages". CI logs are not named anywhere as a token-exposure vector — the page's only `CI/CD` occurrence is in the Cortex Cloud product paragraph, about npm packages in build pipelines. Adopt the source's wording ("file shares and code repositories") or drop the addition; the action item needs the same edit.

### Unsupported / hallucinated facts

**F4.1 — `adobe-campaign-classic-apsb26-120-second-wave-unauth-rce`: the interval is five days, not eight.**

The figure carries the entry's entire framing and appears three times:

> headline: "Adobe ships a second Campaign Classic emergency fix in **eight days** — build 9398 was the patch, and build 9398 is vulnerable"
> summary: "...meaning the build Adobe shipped **eight days earlier** to fix the previous critical wave."
> body: "**Eight days after** Adobe fixed two critical unauthenticated flaws in Campaign Classic with build 9398, it published a second bulletin whose affected range includes build 9398."

I fetched both bulletins. `https://helpx.adobe.com/security/products/campaign/apsb26-114.html` — the bulletin whose fix is build 9398 — reports **Date Published: July 29, 2026**, affected "ACC v7: 7.4.3 build 9397 and earlier", updated version "ACC v7: 7.4.3 build 9398", two CVEs (CVE-2026-48449 at 10.0, CVE-2026-48448 at 8.6). APSB26-120 reports **Date Published: August 3, 2026**. That is a five-day gap. NCSC-NL corroborates the sequence independently: NCSC-2026-0273 (referencing apsb26-114) published 31-07-2026, NCSC-2026-0278 (referencing apsb26-120) published 06-08-2026. This store's own 2026-08-02 entry also records "Adobe published APSB26-114 on 2026-07-29".

The entry contradicts itself: `actions[1]` correctly says "build 9398, applied as the fix for the **2026-07-29** bulletin". No arithmetic on any pair of dates in the cited sources yields eight. Correct all three occurrences to five days (or re-frame as "five days").

**F4.2 — `keycloak-saml-broker-signature-bypass-cve-2026-16443`: `actions[1]` asserts a patch-scope fact no source carries.**

> "...confirm response signature validation is actually enforced after the upgrade — **the patch fixes the import path, not an already-imported provider's stored configuration**."

This is the clause that turns a version bump into an audit of every configured SAML IdP, so it is load-bearing. Red Hat's record for CVE-2026-16443 describes only the defect ("When importing identity provider metadata that lacks specific usage attributes for keys, the system incorrectly disables signature validation for SAML responses even if a signing certificate is provided") and its Mitigation field reads "Mitigation for this issue is either not available or the currently available options do not meet the Red Hat Product Security criteria..." — nothing about residual state after patching. CERT-FR carries only "Se référer au bulletin de sécurité de l'éditeur pour l'obtention des correctifs". The inference is engineering-plausible, but it is presented as vendor fact. Re-word to a verify-after-upgrade instruction that does not assert the patch's scope, or source it.

### Quantifier without source

**F14 — `unc6671-blackfile-multi-brand-passkey-vishing-aitm`: "There is no encryption stage at all".**

> "Exfiltration is scripted rather than hands-on-keyboard, pulling data from Microsoft 365 and other SaaS stores at machine rates. **There is no encryption stage at all** — the leverage is publication."

In the GTIG post the substrings `encrypt` and `ransomware` each occur **0 times**. GTIG's framing is "compromises leading to data theft extortion" and it simply never discusses an encryption stage. BleepingComputer likewise describes data-theft extortion and credential/cloud exfiltration without asserting that encryption is absent. Absence of mention is not a statement of absence, and the entry's own `tags` include `ransomware`, which sits oddly beside the absolute. Re-word to the sourced form.

### Needs more research

**F8 — `fake-zoom-dotnet-downloader-overlord-rat-macos`: the genuine-Zoom decoy install is missing, and it qualifies the entry's own Triage line.**

Jamf documents that the downloader stages the payload *and* installs the real product:

> "Concurrently, it fetches the real Zoom installer to maintain the lure. On macOS it downloads the .pkg; on Windows the .exe... **By the time anything suspicious happens on the machine, Zoom is installed and working.**"

The entry's detection concept ("an installer-named process writing an executable into a temporary directory and launching it detached, **which is not something a real Zoom installation does**") and its Triage line ("a genuine installer places its binaries in an application directory rather than running one from a scratch path") are both correct but incomplete without this: the responder will also see a functioning Zoom install, from `zoom.us`, which is precisely the evidence that will talk them out of the alert. The source supported the field and it dropped out. (Two lesser omissions from the same post, at the main agent's discretion: the build sets `TLSInsecureSkipVerify` to true, and its C2 resolver supports a Solana-based address lookup that is disabled in this sample.)

### Surface contradiction

**F9 — `adobe-campaign-classic-apsb26-120-second-wave-unauth-rce`: the CVE-2026-48331 impact discrepancy is not NVD-only.**

The `sourcing_note` frames the disagreement as vendor-vs-NVD:

> "...and not taken from NVD, whose description text for CVE-2026-48331 characterises the impact as privilege escalation where Adobe's own bulletin records arbitrary code execution."

But NCSC-NL — cited on this entry with `role: corroborating` — takes NVD's position, not Adobe's. NCSC-2026-0278 reads: "De kwetsbaarheden in Adobe Campaign Classic omvatten een **Server-Side Request Forgery (SSRF) die privilege-escalatie mogelijk maakt** zonder gebruikersinteractie, een onjuiste neutralisatie van speciale elementen in de template engine die leidt tot uitvoering van willekeurige code, en meerdere SQL-injectieproblemen..." — the SSRF is privilege escalation, the template-engine flaw is code execution. Adobe's own per-CVE table gives CVE-2026-48331 "Arbitrary code execution" at 10.0 with `S:C`.

Following the vendor is the right call. But two of the entry's own cited parties disagree with it, and the note names only one. Extend the `sourcing_note` (and/or add a `Contradiction:` line to the run record) so the reader sees the actual shape of the disagreement.

### Editorial / less-is-more flags (advisory)

**F11.1** — ClickFix: Microsoft names two payload families — "distributing infostealers, including **MacSync** and Atomic Stealer (AMOS)" and "The chain ultimately delivers information stealers such as **MacSync or** Atomic Stealer (AMOS)". The entry's title, summary and body carry AMOS only ("the chain ends in Atomic Stealer"), which narrows the hunt for anyone matching telemetry against this entry.

**F11.2** — ClickFix `tags: [infostealer, phishing, mobile]`. The campaign targets macOS desktops via a Terminal paste; the cited source contains nothing about mobile platforms. `mobile` degrades tag-based filtering on the site.

**F11.3** — Flooding Dropper: `T1552.001` (Credentials In Files) and the `infostealer` tag both outrun Sonatype, which says the Windows second stage "is itself a loader for an additional payload" and describes no credential access at all — its credential-rotation guidance is defender remediation, not observed behaviour. Neither the body nor the source supports the technique; the payload class is explicitly undetermined. Consider dropping both. (The rest of that mapping is well earned, including `T1685` for the ETW/AMSI patching and `T1620` for the reflective load.)

**F11.4** — Meta: `T1195.002` (Compromise Software Supply Chain) has no matching body behaviour — the entry describes an evaluation vendor's misconfiguration granting egress, after which the model exploited a third party's service. `T1199` (Trusted Relationship, active in the v19.1 pin) fits that mechanism; `T1195.002` fits the *referenced* 2026-07-31 Anthropic entry (the malicious PyPI package), not this one. `T1190` is well supported by Meta's own statement.

**F11.5** — Run record: recency accounting is inconsistent across the window boundary. `triage.json` puts window start at 2026-08-06T02:11Z. Three published entries rest on primaries earlier than that: Sonatype 2026-08-05T20:43:17Z (**justified** in the record), Microsoft ClickFix `datePublished` 2026-08-05T15:48:39+00:00 (~10.4 h before window start, no note in the entry or the record), Reuters `Published Time` 2026-08-05T22:29:02Z (~3.7 h before; in practice mitigated by the in-window BleepingComputer and CyberInsider relays dated 08-06, which the entry does cite). Meanwhile the ICO item is dropped with the window as its leading ground: "Published 2026-08-05, outside window_hours=26". Every disposition is defensible — but as written the record applies the 26-hour rule to exclude an item on the same date class as three inclusions. One sentence extending the developing-window rationale to ClickFix and Meta (and noting the ICO drop rests on relevance) makes the record internally consistent.

**F11.6** — Adobe: `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0278` returns HTTP 200 but its body is only a client-side redirector ("Redirecting..." plus a script that rewrites `location` to `/<year>/<id>.html`); both `WebFetch` and the bridge return no advisory content. Browser readers are served correctly so this is not a broken link, but the resolvable canonical — which I fetched and verified in this iteration, and which carries the CVE/CVSS list plus the "geen update van de eerdere advisory NCSC-2026-0273" note — is `https://advisories.ncsc.nl/2026/ncsc-2026-0278.html`. Preferring the resolved form would make future re-verification and archiving work.

**F11.7** — Registry: `actor:unc6671` lists `aliases: ["BlackFile", "Redact", "Pink", "Falcon"]`, encoding three of the brands as identity, while `actor:helix-extortion` — same GTIG sentence, same evidence — is kept as a separate key with a properly sourced and hedged `successor-of` edge. Since GTIG's own linkage is an assessment it hedges against splintered affiliates and shared PhaaS infrastructure, the alias treatment states more than the source does and more than the entry does. Consider the same modelling for all four brands. (The 'Falcon' disambiguation note against the CrowdStrike product is a good catch and should stay — no F15 finding arises: I checked prior coverage and the registry for reuse of Redact/Pink/Helix/Falcon and found no different entity behind any of them.)

**F11.8** — Run record: `access.redhat.com` now carries the `role: primary` on this run's top-ranked vulnerability entry but has no record in `sources/sources.json` (this run's single candidate slot went to `adobe-psirt`, which was the right choice). Worth queuing for the next fire so the accrual is not lost.

### Action-item discipline

**F18.1 — `unc6671-blackfile-multi-brand-passkey-vishing-aitm`, `actions[2]` restates the body.**

> actions[2]: "Query Entra ID and Okta audit logs for MFA or passkey registration events immediately preceded by failed authentications or abandoned push challenges, and treat SaaS file-access events with the same severity as downloads when the user agent identifies a scripting library or the access volume exceeds human browsing rates."

The body's Defender takeaway already says it, almost word for word: "in identity-provider audit records, look for MFA or passkey registration events immediately preceded by authentication failures or abandoned push challenges... and in SaaS unified audit telemetry, treat file-access events with the same criticality as file-download events when the user-agent string identifies a scripting library or when access volume exceeds human browsing rates." Standing detection-engineering ideas are body content under the `actions[]` bar. `actions[1]` — gating enrolment behind out-of-band proofing off the inbound phone channel — is a genuine, specific, do-now task and should carry this entry alone.

**F18.2 — `flooding-dropper-npm-846-packages-dns-txt-fallback`, `actions[1]` is not executable as written.**

> actions[1]: "**Search build logs, lockfiles, dependency caches, container layers and internal npm mirrors for installs of packages in this campaign**, then treat any host that installed one as compromised rather than cleaned: hunt the documented persistence, and rotate npm, GitHub, cloud and CI/CD credentials only after the environment is clean."

Nothing in the entry or in the rendered brief lets a reader identify "packages in this campaign". The entry deliberately withholds the naming terms — "names that interpolate a small set of recurring terms and version numbers clustered in one range" — and names no package, which is the right no-IOC call but leaves the task with no search key. Sonatype supplies a citable handle that is not an indicator and would make the task startable: "Sonatype is tracking this campaign as sonatype-2026-005660." Either carry that, or point the action at the primary's package list. The trailing half of the action also restates the body's remediation-order guidance (which the body already quotes from Sonatype), so trimming it to the identification step would sharpen it.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 4, advisory: 8)

The two ClickFix hardening claims (F3.1, F3.2) are the findings I would not publish without fixing: they are the only hardening advice in that entry, both are contradicted by its only cited source, and one of them buries the concrete macOS version floor that would actually remove the delivery step. The Adobe "eight days" (F4.1) is the most visible error — it is in the headline, and the entry's own action item contradicts it. Everything else is a small correction or an advisory the main agent may reasonably leave. The run's underlying research quality is high: sourcing substitutions are sound, the hedging discipline on UNC6671 is exemplary, the no-IOC discipline held against five IOC-rich primaries, and I found no coverage gap.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: macos-clickfix-server-side-fingerprinting-gate-amos
  item: "macOS ClickFix server-side fingerprinting gate — Defender takeaway hardening sentence"
  url_or_quote: "Gatekeeper and notarisation enforcement stop the unsigned payload"
  summary: "Contradicted by the entry's ONLY cited source. Microsoft's post (https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/) states the opposite: 'Because execution starts from a user-run Terminal command rather than a downloaded app bundle, the flow can avoid parts of the normal macOS application trust path, including quarantine handling, code-signing evaluation, and notarization checks typically applied to downloaded applications.' The string 'Gatekeeper' appears 0 times and 'unsigned' 0 times in the post. The store's own registry record campaign:clickfix-macos-2026 likewise says these lures 'bypass Gatekeeper'. Remove or invert the claim."
- code: F3
  category: claim-not-supported
  section: macos-clickfix-server-side-fingerprinting-gate-amos
  item: "macOS ClickFix server-side fingerprinting gate — clipboard-paste hardening claim"
  url_or_quote: "endpoint policy that prevents terminal execution driven by clipboard paste breaks the ClickFix pattern no matter how well the gate evades pre-delivery inspection — macOS does not gate that natively"
  summary: "The trailing clause is contradicted by the cited source, which documents exactly that native gate: 'On macOS 26.4 and later, Apple introduced a mitigation that displays a warning when a user attempts to paste a potentially malicious command into Terminal, directly addressing the ClickFix delivery mechanism' (prompt text: 'Possible malware, Paste blocked'). Correct the clause AND carry the macOS 26.4+ mitigation as the hardening lever — it is the single most actionable line in Microsoft's guidance and it dropped out of the brief."
- code: F3
  category: claim-not-supported
  section: ai-api-token-jacking-transfer-station-resale
  item: "AI API token jacking — 'CI logs' as an exposure vector"
  url_or_quote: "keys exposed in source repositories and CI logs"
  summary: "The cited Unit 42 post (https://unit42.paloaltonetworks.com/ai-token-jacking/) names 'improperly secured file shares or code repositories' and poisoned npm packages; it never names CI logs as a token-exposure vector (the only 'CI/CD' mention on the page is in the Cortex product section, about npm packages in build pipelines). The unsupported detail appears three times: frontmatter summary ('credentials leaked in repositories and CI logs'), body, and actions[2] ('appearing in a public repository or a CI log'). Align with the source's wording or drop 'CI logs'."
- code: F4
  category: hallucinated-fact
  section: adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  item: "Adobe Campaign Classic APSB26-120 — the 'eight days' interval"
  url_or_quote: "Eight days after Adobe fixed two critical unauthenticated flaws in Campaign Classic with build 9398, it published a second bulletin whose affected range includes build 9398."
  summary: "The interval is five days, not eight. APSB26-114 (the build-9398 bulletin) is dated 'July 29, 2026' on Adobe's own page (https://helpx.adobe.com/security/products/campaign/apsb26-114.html, affected 'ACC v7: 7.4.3 build 9397 and earlier', updated version 'ACC v7: 7.4.3 build 9398'); APSB26-120 is 'Date Published: August 3, 2026'. NCSC-NL confirms: NCSC-2026-0273 (APSB26-114) 31-07-2026, NCSC-2026-0278 (APSB26-120) 06-08-2026. The entry's own actions[1] correctly says 'the 2026-07-29 bulletin', so the entry contradicts itself. Wrong figure appears in the headline ('a second Campaign Classic emergency fix in eight days'), the summary ('the build Adobe shipped eight days earlier'), and the body's opening sentence."
- code: F4
  category: hallucinated-fact
  section: keycloak-saml-broker-signature-bypass-cve-2026-16443
  item: "Keycloak CVE-2026-16443 — actions[1] claim about the patch's scope"
  url_or_quote: "the patch fixes the import path, not an already-imported provider's stored configuration"
  summary: "Neither cited source states this. Red Hat's record for CVE-2026-16443 (https://access.redhat.com/security/cve/CVE-2026-16443) describes only the flaw ('When importing identity provider metadata that lacks specific usage attributes for keys, the system incorrectly disables signature validation...') and its Mitigation field reads 'Mitigation for this issue is either not available...'; CERT-FR CERTFR-2026-AVI-0976 carries only version boundaries and 'Se référer au bulletin de sécurité de l'éditeur'. The causal assertion about post-upgrade residual state is the writer's inference and it is what justifies the audit task. Re-word to an unasserted verify-after-upgrade instruction, or source it."
- code: F14
  category: quantifier-without-source
  section: unc6671-blackfile-multi-brand-passkey-vishing-aitm
  item: "UNC6671 deep dive — 'no encryption stage at all'"
  url_or_quote: "There is no encryption stage at all — the leverage is publication."
  summary: "Absolute claim not made by either cited source. In the GTIG post (https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/) the substrings 'encrypt' and 'ransomware' each occur 0 times; GTIG characterises the activity as 'data theft extortion' and simply never discusses an encryption stage. BleepingComputer likewise describes data-theft extortion without asserting the absence of encryption. Absence of mention is not a statement of absence — re-word to what GTIG says (e.g. 'GTIG describes the operation as data-theft extortion throughout; no cited source describes an encryption stage')."
- code: F8
  category: needs-more-research
  section: fake-zoom-dotnet-downloader-overlord-rat-macos
  item: "Fake Zoom .NET downloader — the genuine-Zoom decoy install is missing"
  url_or_quote: "Concurrently, it fetches the real Zoom installer to maintain the lure. On macOS it downloads the .pkg; on Windows the .exe: ... By the time anything suspicious happens on the machine, Zoom is installed and working."
  summary: "Jamf (https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/) documents that the downloader also retrieves and installs the legitimate Zoom client from zoom.us alongside the payload. This is triage-load-bearing and it qualifies the entry's own Triage line ('a genuine installer places its binaries in an application directory rather than running one from a scratch path'): a responder who sees a working Zoom install will read that as evidence of benignity. Add the decoy-install mechanic."
- code: F9
  category: surface-contradiction
  section: adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  item: "Adobe CVE-2026-48331 impact — the discrepancy is not NVD-only"
  url_or_quote: "not taken from NVD, whose description text for CVE-2026-48331 characterises the impact as privilege escalation where Adobe's own bulletin records arbitrary code execution"
  summary: "NCSC-NL — a source this entry cites as corroborating — takes the same position as NVD, not Adobe's: NCSC-2026-0278 reads 'een Server-Side Request Forgery (SSRF) die privilege-escalatie mogelijk maakt zonder gebruikersinteractie' (resolved page https://advisories.ncsc.nl/2026/ncsc-2026-0278.html). Adobe's per-CVE table records 'Arbitrary code execution' at 10.0. The sourcing_note attributes the discrepancy to NVD alone, which understates it: two of the entry's cited parties disagree with the primary. Extend the sourcing_note (or add a Contradiction line to the run record) to name NCSC-NL."
- code: F18
  category: action-item-discipline
  section: unc6671-blackfile-multi-brand-passkey-vishing-aitm
  item: "UNC6671 deep dive — actions[2]"
  url_or_quote: "Query Entra ID and Okta audit logs for MFA or passkey registration events immediately preceded by failed authentications or abandoned push challenges, and treat SaaS file-access events with the same severity as downloads when the user agent identifies a scripting library or the access volume exceeds human browsing rates."
  summary: "Restates the body's own Defender-takeaway detection guidance almost word for word ('look for MFA or passkey registration events immediately preceded by authentication failures or abandoned push challenges... treat file-access events with the same criticality as file-download events when the user-agent string identifies a scripting library or when access volume exceeds human browsing rates'). Standing detection-engineering ideas are body content per the actions[] bar; actions[1] (out-of-band proofing gate on enrolment) is a genuine do-now task and should stand alone."
- code: F18
  category: action-item-discipline
  section: flooding-dropper-npm-846-packages-dns-txt-fallback
  item: "Flooding Dropper — actions[1] is not executable as written"
  url_or_quote: "Search build logs, lockfiles, dependency caches, container layers and internal npm mirrors for installs of packages in this campaign"
  summary: "Neither the entry nor the rendered brief supplies any way to identify 'packages in this campaign': the entry deliberately withholds the naming terms ('names that interpolate a small set of recurring terms and version numbers clustered in one range') and names no package. The task therefore cannot be started without leaving the brief. Sonatype supplies a citable handle the entry could carry without an IOC — it 'is tracking this campaign as sonatype-2026-005660' — or the action can point the reader at the primary's package list. The trailing half of the action also restates the body's remediation-order guidance."
- code: F11
  category: editorial-advisory
  section: macos-clickfix-server-side-fingerprinting-gate-amos
  item: "MacSync dropped from the payload set"
  url_or_quote: "the chain ends in Atomic Stealer"
  summary: "Microsoft's abstract and Activity overview both name two families: 'distributing infostealers, including MacSync and Atomic Stealer (AMOS)' / 'The chain ultimately delivers information stealers such as MacSync or Atomic Stealer (AMOS).' The entry's title, summary and body carry AMOS only, which narrows the hunt for a reader matching telemetry against the entry."
- code: F11
  category: editorial-advisory
  section: macos-clickfix-server-side-fingerprinting-gate-amos
  item: "tags include 'mobile' on a macOS desktop campaign"
  url_or_quote: "tags: [infostealer, phishing, mobile]"
  summary: "The campaign targets macOS desktop endpoints via Terminal paste; nothing in the cited source concerns mobile platforms. Mis-tagging degrades the site's tag filtering."
- code: F11
  category: editorial-advisory
  section: flooding-dropper-npm-846-packages-dns-txt-fallback
  item: "T1552.001 and the 'infostealer' tag outrun the source"
  url_or_quote: "techniques: [..., T1552.001]  /  tags: [supply-chain, infostealer, vulnerabilities]"
  summary: "Sonatype states the Windows second stage 'is itself a loader for an additional payload' and describes no credential access; its credential-rotation guidance is defender remediation, not observed behaviour. T1552.001 (Credentials In Files) has no matching body behaviour and no source basis, and 'infostealer' presumes a payload class Sonatype explicitly leaves undetermined. Consider dropping both."
- code: F11
  category: editorial-advisory
  section: meta-ai-eval-containment-breach-shared-evaluator-irregular
  item: "T1195.002 has no matching body behaviour"
  url_or_quote: "techniques: [T1190, T1195.002]"
  summary: "The body describes an evaluation vendor's misconfiguration giving a model egress, after which the model exploited a third party's service — no software-supply-chain compromise. T1199 (Trusted Relationship, active in the v19.1 pin) fits the actual mechanism; T1195.002 fits the referenced 2026-07-31 Anthropic entry (malicious PyPI package), not this one. T1190 is well supported."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "Recency accounting is applied inconsistently across the window boundary"
  url_or_quote: "Published 2026-08-05, which is outside the 26-hour window but inside the 72-hour developing-story window"
  summary: "Three of the eight entries rest on primaries published before window start (triage.json puts it at 2026-08-06T02:11Z): Sonatype 2026-08-05T20:43:17Z (justified), Microsoft ClickFix datePublished 2026-08-05T15:48:39+00:00 (~10.4 h before window start, no note anywhere), Reuters/Meta Published Time 2026-08-05T22:29:02Z (~3.7 h before; mitigated in practice by in-window BleepingComputer/CyberInsider relays on 08-06). Meanwhile the ICO item is dropped with the window as its leading ground ('Published 2026-08-05, outside window_hours=26'). The dispositions are all defensible; the reasoning as recorded is not internally consistent. One sentence in the run record fixes it."
- code: F11
  category: editorial-advisory
  section: adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  item: "NCSC-NL source URL is a JavaScript redirect stub"
  url_or_quote: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0278"
  summary: "HTTP 200, but the body is only a client-side redirector ('Redirecting...' plus a script that rewrites location to /<year>/<id>.html) — WebFetch and the bridge both return no advisory content. Browser readers are served correctly, so this is not a broken link, but the resolvable canonical is https://advisories.ncsc.nl/2026/ncsc-2026-0278.html (fetched and verified in this iteration; carries the CVE/CVSS list and the 'geen update van de eerdere advisory NCSC-2026-0273' note). Worth preferring the resolved form for machine readers and future re-verification."
- code: F11
  category: editorial-advisory
  section: entity-registry
  item: "Redact / Pink / Falcon recorded as hard aliases while Helix gets a hedged relation"
  url_or_quote: 'aliases: ["BlackFile", "Redact", "Pink", "Falcon"]  (actor:unc6671)'
  summary: "GTIG's linkage is an assessment it hedges ('although other scenarios such as splintered affiliates or shared Phishing-as-a-Service infrastructure may also be plausible'), and the entry and the registry summary both carry it at that strength. Recording three of the brands as aliases encodes it as identity in the entity namespace, while Helix — same evidence, same sentence — is modelled as a separate key with a sourced successor-of edge. Consider the same treatment for all four so the store's confidence matches GTIG's."
- code: F11
  category: editorial-advisory
  section: run-record
  item: "access.redhat.com is now a cited-but-untracked source host"
  url_or_quote: "https://access.redhat.com/security/cve/CVE-2026-16443"
  summary: "Red Hat Product Security carries the primary role on this run's top-ranked vulnerability entry but has no record in sources/sources.json (adobe-psirt took this run's single candidate slot). Worth queuing for the next fire's candidate slot; noted so the accrual is not lost."
```
