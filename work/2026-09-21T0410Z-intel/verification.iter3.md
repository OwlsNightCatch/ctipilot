**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-21T05:36:56Z · ended_at=2026-09-21T05:49:45Z · duration_seconds=769

## Verification report — 2026-09-21T0410Z-intel (iteration 3)

Scope: 9 new entries, 0 updated entries, the run record. Cold read of every entry end to end, `git diff`-free (no updated entries this run), literal verbatim (`grep -F`-style) check of every `evidence[]` quote against the fetched primary for all 9 entries, walk of the iteration-2 delta list against freshly-fetched sources, NVD API cross-check of all three frontmatter CVEs, ATT&CK-pin validity check on the ids the run record claims it corrected, registry/dedup cross-check.

### Prior-iteration (iteration 2) deltas — verified

All 12 iteration-2 remediations were re-checked against freshly fetched primaries this iteration:

1–2. TraderTraitor re-sequencing and evidence-quote #1: confirmed correct. SentinelOne's own timeline table (`05:00:53` first execution, `05:00:55` C2 connection, `05:00:58` xattr/chmod Gatekeeper-bypass re-arm) matches the entry's "began beaconing ... within two seconds, before ... a Gatekeeper bypass ... moments later." Evidence quote "Unlike the previous high-profile victim, this target was a much smaller organization in the IT services industry." is a contiguous verbatim substring of the source.
3–4. NightEagle evidence-quote #2 and CVE-2019-0708 status: confirmed correct. The devtunnels quote is contiguous verbatim (markdown link/backtick formatting only); `status: [exploited, patch-available]` matches Kaspersky's "In one incident, they exploited a well-known RDP implementation vulnerability, CVE-2019-0708 (BlueKeep)."
5–6. Conference-phishing Gatekeeper reattachment and ClickOnce/ClickFix parallel-path split: confirmed correct against the source (DMG/manual-download path carries the Gatekeeper-bypass instructions per "The DMG file also included Gatekeeper-bypass instructions and a password prompt"; ClickOnce/Norwegian-cert and ClickFix/PowerShell are indeed described as two separate Windows routes in the source).
7. Conference-phishing Discord/Lenovo cert ordinal: the ORDINAL fix (Discord=2nd, Lenovo=3rd) is correct, but the remediation introduced a new document/chain misattribution — see F3 finding below. This is exactly the residual the delta asked to be re-checked, and the re-check surfaced it.
8. The-Gentlemen T1219 removal: confirmed correct — no AnyDesk behavior anywhere in the entry's body, and Talos's "the remote desktop tool AnyDesk" appears only in the tool-inventory list, not the phase narrative used for techniques[] mapping.
9. REF9334/KREMLIN "resources.pak, a sibling file" fix: confirmed correct — Elastic's own path is `%PROGRAMFILES%\Google\Chrome\Application\<VERSION>\resources.pak`, the same versioned directory that holds `chrome.dll`.
10. AFPA Cyberattaque.org date revert to 2026-09-15: the frontmatter value is confirmed correct (Published Time 2026-09-15T21:41:46+00:00 via both `extract` and `jina` this iteration) — but the revert missed a body-text sibling; see F3 finding below.
11. AFPA PD-11 double-ground sourcing_note: confirmed present and adequately worded.
12. Run-record registry-hygiene retraction: confirmed correct — `entities/registry.yaml` line 103 shows `actor:gentlemen-raas-gentlekiller` already carries `merged_into: "actor:thegentlemen"`.

### Claims missing inline citation / Citation does not support the claim

**#1 — `conference-phishing-rogue-root-ca-mitm-persistence`.** Body: *"Windows victims who pasted the ClickFix command launched an encoded PowerShell command that fetched a loader — itself signed with a certificate stolen from Discord Inc., whose signature does not validate — which pulled down three further payloads: NetSupport Manager ... a TLS-intercepting local proxy ... and a Ledger-wallet implant ..."* The source (`https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows`) attaches the Discord certificate and the three named payloads to a **different** chain than the one the entry names. Its own section headers: `## You have one new message: A second document link and a second stolen cert` → *"The installer in the Windows chain was signed with a certificate stolen from Discord Inc.; the signature did not validate."* — this is explicitly the SECOND document (DropBox DocSend), not the first ClickFix chain. The three payloads are recovered specifically by reconstructing that same dead DocSend endpoint (`## Reconstructing communications from a dead endpoint` → *"the recovered stage-three payloads: `Manager.zip` - NetSupport Manager ...; `Localcertificate.zip` - a TLS-intercepting local proxy; `asusdriverld.zip` - a Ledger wallet implant"*), and `## The final stage` describes *"the loader"* (continuing that same DocSend narrative) downloading them. By contrast, the source's only statement about the original ClickFix loader is: *"Windows users who fell for the ClickFix lure in the Google Doc sidebar ended up launching an encoded PowerShell command that fetched a loader, which in turn pulled down three encrypted payloads. All three were offline by the time we went looking, but all three were already on VirusTotal, so the kit had clearly run before."* — no certificate is named for it anywhere in the source. Meanwhile the entry's own paragraph about the second document now reads *"told Windows victims to install a DocSend-branded desktop installer — reusing the same playbook against the same target"* with **no** certificate named — the exact inverse of the source. This is iteration-2's own remediation (delta #7) that fixed the Discord/Lenovo *ordinal* correctly but left the cert (and the three named payloads) attached to the wrong document's chain — the residual the spawn message specifically asked to be re-verified, and it is still present.

**#2 — `afpa-third-party-accommodation-tool-data-extraction`.** Body: *"claimed 1,732,811 records via an alleged insecure direct object reference (IDOR) flaw ([Cyberattaque.org, 2026-09-19](https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/))"* — the inline citation date is 2026-09-19. The entry's own frontmatter `sources[1]` for this identical URL carries `date: "2026-09-15"`, and a fresh fetch this iteration (both `extract` and `jina`, per iteration-2's own confirmation) returns `Published Time: 2026-09-15T21:41:46+00:00`. The frontmatter is correct; the body's inline citation next to the same URL was never updated to match and is a 4-day-stale leftover from iteration-1's now-reverted `dateModified` attempt — a self-contradiction against the entry's own `sources[]` block, and well past the one-day timezone-drift tolerance in check 2(e).

**#3 (low confidence) — `ref9334-kremlin-chromium-secure-preferences-hmac-forge`.** Body and sourcing_note both state *"Ethereum transaction timing consistent with São Paulo business hours"* / *"São Paulo-hours Ethereum transaction timing."* Elastic's own reasoning (`https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware`): *"In UTC-3, only around ten fall within late-night hours, without extending particularly far into the early morning. Assuming the operators are more likely to work late than wake before dawn, this distribution aligns most closely with São Paulo time."* The source's own argument is about late-night activity, not conventional business hours — the entry's "business hours" framing inverts the nuance of the source's own stated reasoning.

### Editorial / less-is-more flags (advisory)

**#1 — `the-gentlemen-open-directory-vhdx-backup-ntds-theft`.** `affected_products: []` while `cves[]` carries CVE-2025-24799 (GLPI SQLi). Naming "GLPI" in `affected_products[]` would improve automated triage matching; not a contradiction of any source, advisory only.

**#2 — `nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync`.** `affected_products: ["Microsoft Exchange Server"]` omits a Windows RDP product line despite carrying CVE-2019-0708 (BlueKeep), whose own `affected` field reads "Windows RDP (Windows 7, Server 2008/2008 R2 and earlier RDP-enabled builds)." Advisory only.

### Checks that came back clean (no findings)

- **Verbatim evidence sweep** — all 21 `evidence[]` quotes across the 9 entries were checked with a literal contiguous-substring comparison against the fetched primary (Talos ×4, Kaspersky ×4, SentinelOne ×3, Huntress-VSS ×2, Huntress-GoogleDoc ×3, Elastic ×3, detect.fyi ×2, Clubic/Cyberattaque.org ×3 including `original:` French text). None had a splice, inserted ellipsis, or re-hedged word; markdown link/backtick formatting is the only cosmetic difference from the source in every case, consistent with normal formatting rather than a defect.
- **CVSS/vector/auth cross-checks against NVD API**: CVE-2025-24799 (7.5, `AV:N/AC:L/PR:N/UI:N`, matches the GitHub-Security-Advisories/CNA score used, not NVD's own conflicting 9.8 re-score — correctly following the discloser/CNA authority per PD-12); CVE-2020-0688 (8.8, `PR:L/UI:N` → post-auth/zero-click, matches); CVE-2019-0708 (9.8, `PR:N/UI:N` → pre-auth/zero-click, matches). All three entries' `cves[]` blocks are correct.
- **ATT&CK-pin validity**: T1685 active (T1562.006's revocation target, confirmed T1562.006 is revoked→T1685); T1574.001 active (T1574.002's revocation target, confirmed T1574.002 is revoked→T1574.001); T1003.002/T1003.003/T1003.006/T1219 all active. The run record's claimed mechanical corrections (T1562.006→T1685, T1574.002→T1574.001, DCSync id kept only on NightEagle) are all verified correct.
- **Dedup**: none of this run's three CVEs (CVE-2025-24799, CVE-2019-0708, CVE-2020-0688) appear in `prior_coverage.json` or `state/cves_seen.json`; no prior entry in the store mentions AFPA; the AFPA entry is correctly a new entry, not a changelog candidate.
- **Registry**: `actor:jade-sleet` aliases (TraderTraitor/UNC4899/PUKCHONG), `actor:cybernox`, `actor:xmetah`, `malware:kremlin`, `actor:thegentlemen`/`actor:gentlemen-raas-gentlekiller` (tombstoned, `merged_into` present) all checked and consistent with the entries' and run record's claims. No name-collision risk found for "KREMLIN" (registry summary explicitly disambiguates the Russian-sounding name as the malware author's own coinage).
- **Classification/org-triage/watchlist**: all 9 entries carry a valid `classification: {reliability, credibility}` block with no `org_triage` and `watchlist_hit: false`, consistent with this deployment's unconfigured triage/watchlist scheme.
- **Relevance/priority**: no entry fails the relevance gate; REF9334/KREMLIN (LatAm banking fraud, no Swiss nexus) clears the bar on "widely deployed technology" (Chromium extension-integrity bypass, transferable to any Chrome/Edge estate) rather than home-region/sector grounds; the AFPA breach entry's out-of-nexus grounds (direct primary-sector match + scale) are stated in its own `sourcing_note`, consistent with check 5's stricter breach-entry bar. Priority levels (4× high, 3× notable, 1× routine, plus AFPA notable) all look calibrated to their respective urgency.
- **Style discipline**: no IOCs, no vanity metrics reproduced from the Talos roundup (the 4.7% YoY / 80%-SME stats stay in the source, not the entries), no workflow-internal language in any entry body or the run-record notes.
- **Coverage shape / missed angles**: no gap could be evidenced against `prior_coverage.json` or the run's own fetch-failure telemetry beyond what the run record already discloses (dead RSS/feed paths, JS-rendered listings) — none of which points to a specific, nameable in-window story the run missed.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 2)

The two solid truth findings (#1 conference-phishing cert/payload-chain misattribution, #2 AFPA stale inline citation date) are both residuals of iteration-1/iteration-2 remediations that fixed the reported symptom (an ordinal error, a wrong frontmatter date) without fully propagating the fix through the rest of the entry. Finding #3 is lower-confidence and finding-class F11 is advisory only.

### Findings summary (machine-readable)

See sibling file `work/2026-09-21T0410Z-intel/verification.iter3.findings.yaml` (reproduced below).

```yaml
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "conference-phishing-rogue-root-ca-mitm-persistence"
  url_or_quote: "\"Windows victims who pasted the ClickFix command launched an encoded PowerShell command that fetched a loader — itself signed with a certificate stolen from Discord Inc., whose signature does not validate — which pulled down three further payloads: NetSupport Manager ... a TLS-intercepting local proxy ... and a Ledger-wallet implant\""
  summary: >
    The source's own section headings assign the Discord certificate and the three named payloads
    to the SECOND document (DropBox DocSend), not the first document's ClickFix/PowerShell chain the
    entry attaches them to. See report body for full quote comparison. Iteration-2's own remediation
    (delta #7) fixed the cert's ordinal (2nd, not 3rd) but left it, and the three payloads, on the wrong
    chain.
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"claimed 1,732,811 records via an alleged insecure direct object reference (IDOR) flaw ([Cyberattaque.org, 2026-09-19](...))\""
  summary: >
    Inline citation date (2026-09-19) contradicts the entry's own frontmatter for the same URL
    (date: "2026-09-15") and the page's own Published Time (2026-09-15T21:41:46+00:00, confirmed via
    extract and jina this iteration) — a 4-day-stale leftover from iteration-1's reverted dateModified fix.
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ref9334-kremlin-chromium-secure-preferences-hmac-forge"
  url_or_quote: "\"Ethereum transaction timing consistent with São Paulo business hours\""
  summary: >
    (low confidence) Elastic's own reasoning is about late-night activity aligning with the São Paulo
    timezone, not conventional business hours; the entry's "business hours" framing inverts that nuance.
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "the-gentlemen-open-directory-vhdx-backup-ntds-theft"
  url_or_quote: "affected_products: [] alongside cves: [CVE-2025-24799 (GLPI)]"
  summary: "Naming GLPI in affected_products[] would improve triage matching. Advisory only."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync"
  url_or_quote: "affected_products: [\"Microsoft Exchange Server\"] alongside cves: [CVE-2019-0708 (Windows RDP)]"
  summary: "Missing the Windows-RDP product line for BlueKeep's own affected field. Advisory only."
```
