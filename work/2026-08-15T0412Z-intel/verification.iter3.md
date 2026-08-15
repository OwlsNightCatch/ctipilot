**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-15T05:42:00Z · ended_at=2026-08-15T05:58:53Z · duration_seconds=1013
**Self-telemetry:** urls_checked=27 · webfetch_calls=0 · bridge_fetches=31

## Verification report — 2026-08-15T0412Z-intel (iteration 3)

Read cold: all 13 entries end-to-end (frontmatter + body), the run record, `work/…/prior_coverage.json`, `entities/registry.yaml`, `triage.json`, and the pinned ATT&CK dataset. Every inline source URL on every entry was fetched this iteration via `tools/fetch_source.py url` (jina pool exhausted as the spawn message stated; no fetch failed, so no finding rests on my own transport). Every `cves[]` id and score was checked against the per-CVE owning authority — Fortinet's per-advisory HTML tables **and** their CSAF records, NetScaler's CNA record, CISA's CSAF for ICSA-26-225-02, VulnCheck's advisory page — not against the entries' roundup citations. Every `evidence[]` quote was string-matched against the fetched page text.

**What held.** The deep dive is accurate against watchTowr end to end (SignedInfo/`PrefixList` overflow, freelist-header corruption, write-what-where, RWX heap, `pitboss` respawn, SUID `/bin/sh`) and both NCSC-CH quotes are verbatim from post 12739, whose `created` field is indeed 2026-07-03 with the 2026-08-14 edit. Haiwell matches CISA's CSAF exactly (10.0, `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`, 3.40.1.12 → Scada-v3.50.1.19, SSVC `E:N/A:Y`, sector and worldwide statements). Flowise matches VulnCheck's record (9.0, CVSS4.0 vector, `< 3.1.3` → 3.1.3). Fortinet's 7.3 for CVE-2026-70465 — iteration 2's fix — is correct in all three places. DGFiP, The Register, BBC, Threema, BleepingComputer, NL Times, Notes from Poland, Gazeta Prawna, Securelist, Talos, SentinelLabs and Hugging Face all carry their attached claims, and all 39 `evidence[]` quotes are contiguous substrings of their live pages (only inline-`<code>`/link tag boundaries and one straight-vs-curly apostrophe differ, which is rendering, not splicing). All 26 distinct `techniques[]` ids resolve to active, correctly-named techniques in the v19.2 pin — including `T1685` Disable or Modify Tools for the Defender-exclusion behaviour. No `critical` priority, no watchlist flag, no `org_triage` block, an Admiralty rating on every entry, no IOCs, no workflow language in any entry, `entries_updated: 5` matches the five `update_of` files, and every `update_of` target exists on disk.

The defects below are concentrated where the spawn message predicted: vendor version boundaries.

### Citation does not support the claim

**F1 — `2026-08-15/fortiweb-radius-wildcard-bypass-fortimanager-fgfm`: the entry declares the FortiWeb 7.0 branch unaffected by CVE-2026-26035; Fortinet's own CSAF — the record the entry cites as its source — lists it affected with no released fix.**

The entry's sourcing note states:

> "Affected and fixed version strings, and every CVSS score, are read from Fortinet's own per-advisory version tables and CSAF records rather than from secondary summaries. **The FortiWeb 7.0 branch does not appear in the vendor's affected table for CVE-2026-26035 and is therefore not claimed as affected here.**"

and `cves[]` carries `affected: "FortiWeb 8.0.0–8.0.2, 7.6.0–7.6.6, 7.4.0–7.4.11, 7.2.0–7.2.12"`, mirrored in the body ("Affected branches are FortiWeb 8.0.0 through 8.0.2, 7.6.0 through 7.6.6, 7.4.0 through 7.4.11 and 7.2.0 through 7.2.12").

I fetched `https://filestore.fortinet.com/fortiguard/psirt/csaf_broken-access-control-in-the-radius-type-admin-group_fg-ir-26-158.json` (linked from FG-IR-26-158 itself). Its `product_status` for CVE-2026-26035 reads:

- `known_affected`: `['FortiWeb >=8.0.0|<=8.0.2', 'FortiWeb >=7.6.0|<=7.6.6', 'FortiWeb >=7.4.0|<=7.4.11', 'FortiWeb >=7.2.0|<=7.2.12', **'FortiWeb >=7.0.0|<=7.0.12'**]`
- `known_not_affected`: `['FortiWeb-8.0.3', 'FortiWeb-7.6.7', 'FortiWeb-7.4.12', 'FortiWeb-upcoming  7.2.13', **'FortiWeb-upcoming  7.0.13'**]`

Fortinet's own CVE record (assigner `fortinet`) agrees, listing `FortiWeb 7.0.0 through 7.0.12` affected. Only the rendered HTML table omits the 7.0 row — consistent with its fix being unreleased. Operationally this is the worst possible direction of error: a FortiWeb 7.0 estate is affected by a pre-auth admin-login bypass, has **no** fixed build to upgrade to, and this entry tells it the vendor does not list it. The same assertion is repeated in the run record's notes ("A version range that a research return attributed to one Fortinet advisory does not appear in the vendor's own affected-version table and was not carried into the entry") and must move with it.

**F2 — same entry, CVE-2026-70466: the no-fix branch list omits FortiWeb 7.0, which the vendor's CSAF also lists as affected with no fixed build.**

Entry, `cves[]`: `affected: "FortiWeb 8.0.0–8.0.2, 7.6.0–7.6.5; the 7.4 and 7.2 branches at all versions"`, `fixed: "8.0.3, 7.6.6 — the 7.4 and 7.2 branches have no fixed build and must be migrated"`; body: "the 7.4 and 7.2 branches are listed as affected at all versions with 'Migrate to a fixed release' as the only remediation — there is no patch for those trains".

`https://filestore.fortinet.com/fortiguard/psirt/csaf_content-encoding-waf-evasion_fg-ir-26-157.json` gives `known_affected: ['FortiWeb >=8.0.0|<=8.0.2', 'FortiWeb >=7.6.0|<=7.6.5', 'FortiWeb 7.4 all versions', 'FortiWeb 7.2 all versions', **'FortiWeb 7.0 all versions'**]` with `known_not_affected: ['FortiWeb-8.0.3', 'FortiWeb-7.6.6']`. Three branches have no fix, not two. (The 8.0.3 / 7.6.6 boundaries, the "Migrate to a fixed release" wording and the FMWP virtual patch are all correct as written.)

### Quantifier without source

**F3 — same entry: "None of the three is reported exploited" after the entry enumerates four flaws.**

Body line 139: "**Four of the flaws** in that batch matter to a defender's next week." Body line 145: "**None of the three** is reported exploited." CVE-2026-70465 was added to this entry by an earlier remediation and the count was not carried through. The underlying fact is fine — SecurityWeek states "Fortinet makes no mention of any of these vulnerabilities being exploited in the wild" (fetched, 2026-08-13) — but the number "three" is supported by nothing and contradicts the entry's own enumeration two paragraphs earlier.

### Analytical-link-as-fact

**F4 — `2026-08-15/mustang-panda-coolclient-signed-kernel-driver-rootkit`: a China nexus is asserted as if cited; neither cited source states it.**

Frontmatter summary: "Kaspersky's GReAT team published on 2026-08-14 a new CoolClient backdoor variant, attributed to the **China-nexus actor it tracks as HoneyMyte** and also known as Mustang Panda…" plus `tags: [nation-state, espionage, china-nexus]`.

The entry has exactly two sources and I fetched both:

- `https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/` — **zero occurrences of "China" or "Chinese" anywhere in the page.** Kaspersky calls it "the HoneyMyte APT group (also known as Mustang Panda)" running "cyber-espionage campaigns targeting organizations across Asia and Russia"; its Attribution section confirms only the malware-to-group association via the PlugX→CoolClient chain. It notes a Chinese-language PDB path and a certificate issued to "Nanjing Ranyi Technology Co., Ltd." and explicitly says "our OSINT analysis did not identify any information linking these strings to a known organization, developer, or threat actor."
- `https://thehackernews.com/2026/08/mustang-panda-adds-signed-windows.html` — no China/Chinese reference in the article body either (the only page hit is an unrelated sidebar headline).

The entry's own sourcing note establishes the discipline this breaches: "Kaspersky states only that HoneyMyte is 'also known as Mustang Panda' — the other cluster names commonly applied to this actor by other trackers are not stated by this source and are therefore not claimed here." A state nexus is a heavier claim than a cluster alias. The registry record `actor:mustang-panda` opens with the same descriptor ("China-nexus cyber-espionage group, tracked by Kaspersky as HoneyMyte…"), so a fix should move both. Remediation is either a citation that states the nexus, or dropping the descriptor and the `china-nexus` tag.

### Needs more research

**F5 — `2026-08-15/netscaler-saml-signedinfo-overflow-preauth-root-rce-not-dos`: the FIPS/NDcPP builds are missing from the affected/fixed boundary a deep dive built around version verification.**

`cves[]` for both CVEs: `affected: "NetScaler ADC/Gateway 14.1 before 14.1-72.61, 13.1 before 13.1-63.18"`, and the first action reads "Verify — do not assume — that every NetScaler ADC and Gateway is actually running 14.1-72.61 or 13.1-63.18 or later".

NetScaler's own CVE records (assigner `NetScaler`) for CVE-2026-8452 and CVE-2026-8451 both add `14.1 FIPS` before `72.61` and **`13.1 FIPS and NDcPP` before `37.272`**. watchTowr reproduces only the two mainline branches, and NCSC-CH defers ("For specific versions, please check the references") — so the cited pages don't carry it, but the owning authority does, and a FIPS/NDcPP appliance is a realistic build in a Swiss federal or critical-infrastructure estate. As written, that operator checks for a build number that does not exist on their train. One clause in `affected`/`fixed` closes it.

**F6 — `2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited`: two cited sources qualify the observed activity as probing without confirmed compromise; the entry never says so.**

Entry summary: "is under active exploitation"; body: "attackers began exploiting it the same day". Both are defensible against NCSC-CH's status line, but the entry drops the qualifier its own co-cited sources put on the same telemetry:

- The Hacker News (fetched): Knott, directly — "**Currently, we're seeing attackers probe to identify vulnerable systems across the internet, triggering errors and not proceeding further.** However, this is unlikely to remain the case for long…"
- Field Effect (fetched, 2026-08-13): "**The observed activity consisted primarily of scanning and probing for vulnerable systems. Public reporting has not described confirmed compromises associated with this vulnerability as of August 13, 2026.**"
- SecurityWeek carries the same ("no follow-up activity has been observed").

For an exposure with no patch, whether the hundreds of hits are mass probing or landed compromises is the difference between "take it off the internet this week" and "assume breach". One clause restores it, and it strengthens rather than weakens the entry's argument.

### Missed angles

**F7 — the 2,500-organisation supply-chain compromise was re-scoped in-window to Trivy rather than LiteLLM, and the run neither published nor dropped it.**

`https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/`, `datePublished` 2026-08-14T11:35:23Z — squarely inside the 2026-08-13T04:12Z → 2026-08-15T04:12Z window. I fetched it: SOCRadar examined the per-organisation records (2,188 entities with first/last-seen timestamps) and found that for 2,085 of them — 95% — collection ended **before** the poisoned LiteLLM packages were published on 24 March, tracing them to the upstream Aqua Security **Trivy** build compromise instead ("The 40 minutes everyone reported was the closing act, not the whole play"); earliest collection 18 minutes after the malicious Trivy build went live, surging while malicious Trivy images were on Docker Hub. This pipeline carries LiteLLM twice in the dedup window (2026-08-06 callback hooks, 2026-08-08 Wiz highlights) and neither the run record's coverage-gaps paragraph nor `triage.json`'s `dropped[]` mentions this thread at all, so it looks unsurfaced rather than considered. It changes which tool a CI/CD estate audits and which credentials it rotates. Suggested query: `SOCRadar Trivy LiteLLM 2500 organizations TeamPCP March 2026 timeline`.

### Single-source items missing [SINGLE-SOURCE] flag

**F8 — the run record's single-source list omits the NHSBT entry.**

`2026-08-15/nhsbt-transplant-data-unencrypted-pager-network` carries `verification: single-source`, one source (`https://www.bbc.co.uk/news/articles/clyj92j210do`) and a correct sourcing note. The run record's § Verification & coverage notes names five single-source entries (mustang-panda, jwr, flowise, haiwell, threema-as-victim) and misses this sixth. The entry itself is correctly flagged — only the run-record line is missing. Add: `Single-source: 2026-08-15/nhsbt-transplant-data-unencrypted-pager-network — the BBC's own investigation is the sole first-hand account, carrying NHSBT's, the network operator's and the ICO's statements directly.`

### Editorial / less-is-more flags (advisory)

**F9 — Fortinet entry, CVE-2026-70465 sourcing note: 7.3 vs 8.1 is base-vs-temporal on one Fortinet vector, not a disagreement between authorities.**

The note reads "the NVD entry for the same flaw carries a higher base score, and the assigning authority's number is the one that travels with the CVE." Nothing there is false, but NVD's 8.1 is recorded with `source: psirt@fortinet.com` and vector `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H` — Fortinet's own base vector — while 7.3 is that same vector with `E:P/RL:O/RC:C` applied (the same relationship holds for CVE-2026-26035's 9.8 base / 8.8 published and CVE-2026-70466's 5.3 / 4.8). A reader comparing this entry against a scanner feed will see 8.1 and conclude the entry is wrong. Saying "7.3 is Fortinet's temporal-adjusted score for the same 8.1 base vector" removes the ambiguity. Advisory — the main agent may leave it.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 4, advisory: 1)

Truth: F1, F2 (claim-not-supported), F3 (quantifier-without-source), F4 (analytical-link-as-fact). Editorial: F5, F6 (needs-more-research), F7 (missed-angle), F8 (single-source-flag-missing). Advisory: F9.

Coverage otherwise looks sound: the 12 borderline drops in the run record match `triage.json` line for line and each names a defensible reason; the 48-hour catch-up window's obvious candidates (ShieldBreak, the Lazarus AFD zero-day, Metabase's CVE assignment, the Cl0p batch, MyDr) are all already in the store from the 2026-08-12/13 runs; the only in-window story I can name a fetched source for and cannot find accounted anywhere is F7.

### Findings summary (machine-readable)

See `work/2026-08-15T0412Z-intel/verification.iter3.findings.yaml` (identical payload).
