**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-16T05:52:04Z · ended_at=2026-08-16T06:08:31Z · duration_seconds=987
**Self-telemetry:** urls_checked=16 · webfetch_calls=1 · bridge_fetches=16

## Verification report — 2026-08-16T0411Z-intel (iteration 5)

Cold read. All 15 cited source URLs re-fetched independently in this iteration (14 via `tools/fetch_source.py url`, 1 via `WebFetch`); all 18 `evidence[]` quotes checked character-for-character against the fetched page text; every `cves[]` id and score checked against the owning advisory; every ATT&CK id checked against the pinned v19.2 dataset; prior-coverage and registry checked for dedup and entity-linking.

**Transport note, correcting the spawn brief:** `python3 tools/fetch_source.py url https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot` returned the full 135 KB rendered article (18.9 KB of extracted text, including the exploit table and the conclusion). The Fortinet blog did *not* require `WebFetch`. Both transports were used and agree.

**What is clean.** All 15 URLs resolve to specific articles/advisories — no homepage, index or NVD/MITRE per-CVE page. All 18 evidence quotes are contiguous verbatim substrings. CVE-2026-58231 CVSS 10.0 confirmed on NCSC-2026-0302; CVE-2026-65400 CVSS 7.1 confirmed on NCSC-2026-0280 (revision 1.0.1, 12-08-2026, revision note "Publieke PoC code beschikbaar en actief misbruik bekend"); CVE-2026-71362 CVSS 9.1 / CWE-863 / auth-not-required / admin-not-required confirmed cell-by-cell on APSB26-92, and the per-product affected and fixed strings match the vendor tables exactly, including the Magento Open Source floor at 2.4.6 (iteration 2's correction holds). Citation dates match every source's own `datePublished`. Iteration 1's Onapsis addition is correct: the rebuild-and-redeploy requirement and the IP Filter Set workaround are both stated verbatim on the Onapsis post, published 2026-08-11. Iteration 3's T1185 addition is supported ("interact with the browser as if sitting at the keyboard"). Iteration 4's Evooo1Bot `single-source` change is correct. No IOCs, no vanity metrics, no workflow-internal language in any entry body or in the run record's published notes. `tool:evooo1bot` follows the store's existing botnet-as-tool convention (`tool:apex2-botnet`, `tool:dysphoria-botnet`). No CVE- or entity-level duplication against prior coverage. Both empty `actions[]` lists (Jewelbug, ExfilSquad) are correct, and the four populated lists are one concrete task each — no F18.

**On the open questions in the spawn brief.** (1) macOS at `high` is right, not `critical` — the patch is ten days old, the store has already twice told readers to apply it, and the observed outcome is cryptomining; it does not *plainly* clear the stop-reading-and-act-now bar, and the run record documents the reasoning. No F16. (2) The four out-of-window entries each disclose their basis and each is a backlog/recency-exempt recovery; defensible. (3) The deep dive earns its length — the shared-template watering hole and the native-messaging escape are both mapped to source text, and the category-rotation note in the run record is the right handling. (4) The `exploited` rule is stated on both SAP and Adobe and applied consistently across all six entries. (5) `cves: []` on Evooo1Bot with ids named in prose is honest and consistent with the sourcing note — but see F2, where the same discipline was not applied to `affected_products[]`.

### Citation does not support the claim

**F1 — `2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay`: the two named ciphers are bound to the command-and-control channel; the cited page attributes them to compile-time string obfuscation.**

Entry body, paragraph 4: *"Command-and-control is AES-256-CTR and ChaCha20 over TCP/443 to sit inside ordinary HTTPS egress, and persistence is stacked deliberately: …"* — citation `([FortiGuard Labs, 2026-08-13](https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot))`.

What that page actually says, fetched this iteration:

- Basic Sample Identification section: *"Static strings in Evooo1Bot are protected by a multi-layer pipeline applied at compile time. The same decryption procedure handles more than 60 encrypted string blocks. The AES and ChaCha20 keys are not stored directly in the binary. Each key is split into two 32-byte constants embedded in .data and combined at runtime via XOR."*
- Conclusion: *"it features encrypted C2 communications, multiple layers of string obfuscation using AES-256-CTR, ChaCha20, and XOR-based key derivation, as well as a 28-command remote administration interface."* — the two ciphers are enumerated **under string obfuscation**, listed as a separate item from "encrypted C2 communications".
- The only thing the page says about the C2 wire: *"Once the checks pass, it begins establishing a connection with the C2 server on port 443. This port is chosen to blend in with expected HTTPS traffic at the network perimeter."*

So TCP/443 and the HTTPS-blending rationale are supported; naming AES-256-CTR and ChaCha20 as the C2 encryption is not. FortiGuard names no cipher for the C2 channel anywhere on the page (grep of the full extracted text: the only cipher mentions are the two quoted above). This matters to the entry's own audience — a detection engineer reading it is told the botnet has a known crypto profile on the wire.

Knock-on: `techniques[]` carries `T1573.001` (Encrypted Channel: Symmetric Cryptography), which rests entirely on this same unsupported binding. `T1573` (parent, Encrypted Channel) is supported by "encrypted C2 communications" and by the reverse-relay description ("establishes an outbound encrypted connection to an operator-specified relay server"); the `.001` sub-technique is not.

Suggested repair: state the C2 as "encrypted, over TCP/443 chosen to blend into HTTPS egress", and move the cipher names to where the source puts them (compile-time string obfuscation, which the body does not currently mention at all); demote `T1573.001` to `T1573` unless a source naming the C2 cipher is found.

### Unsupported / hallucinated facts

**F2 — `2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay`: three specific WSO2 product names appear in `affected_products[]` and in the action item; no cited source names any of them.**

Frontmatter: `affected_products: [… "WSO2 API Manager", "WSO2 Identity Server", "WSO2 Enterprise Integrator", …]`.
`actions[0]`: *"Check whether any internet-facing Atlassian Confluence Server or Data Center, **WSO2 API Manager, Identity Server or Enterprise Integrator**, or Kubernetes ingress-nginx admission controller in the estate is still on a version vulnerable to …"*

All three cited sources, fetched this iteration:

- FortiGuard Labs — the exploit table row reads, in full: `CVE-2022-29464 | WSO2 products | /fileupload/`. The string "API Manager" does not appear on the page; neither does "Identity Server" or "Enterprise Integrator".
- BleepingComputer (2026-08-15) — *"targeting Hikvision cameras, Atlassian Confluence, Zyxel firewalls, TP-Link routers, D-Link NAS devices, **WSO2 products**, Kubernetes ingress-nginx, and vulnerable PHP-CGI installations."*
- The Record (2026-08-13) — does not mention WSO2 at all (full text read; it names only Alcatel, D-Link, Mitsubishi Electric, Netgear, Tenda and Telesquare).

The three product names are true of CVE-2022-29464's actual scope, but they were supplied from outside the cited reporting, and the list is also partial (the CVE's own advisory covers further WSO2 products). This is the entry's own declared discipline being broken in the machine-consumed field: the `sourcing_note` says *"transcribing them from memory would be invention"* about per-CVE version boundaries, and then the product scope is transcribed from memory anyway.

Lesser instance in the same list, for the main agent's judgement rather than a separate finding: `"Atlassian Confluence Server"` / `"Atlassian Confluence Data Center"` where both cited sources say only "Atlassian Confluence". Splitting to the two editions is closer to defensible product-name normalisation, since those are the only two editions CVE-2022-26134 applies to; the WSO2 trio is not, because WSO2 ships many products and the cited text names none.

Suggested repair: reduce the three WSO2 values to what the sources name (e.g. a single `"WSO2 products"` value, or drop them from `affected_products[]` and keep the CVE id in prose as the entry already does), and reword the action to "any internet-facing WSO2 product" — or add WSO2's own advisory for CVE-2022-29464 as a source and cite it at the point of claim. Every other value in the list checks out against the FortiGuard page: Hikvision IP Camera, Zyxel Firewall, TP-Link Archer AX21, Tenda AC10 (in "Tenda AC7, AC9, and AC10"), NETGEAR routers, D-Link DIR-823X, Mitsubishi Electric ME-RTU, Kubernetes ingress-nginx, and Alcatel-Lucent OmniPCX Enterprise (the page carries both "Alcatel OmniPCX Enterprise" and "rep.alcatel for Alcatel-Lucent targets").

### Missed angles

**F3 — whole-run: an Akira affiliate blinding EDR by booting into Safe Mode — a Huntress DFIR case on ground this store already tracks — is absent from the store with no drop decision recorded anywhere.**

Item: "Akira hackers disable EDR with Safe Mode, steal data but fail to encrypt", BleepingComputer, `datePublished` 2026-08-13T16:47:02-04:00 (= 2026-08-13T20:47Z), reporting a Huntress incident investigation. URL fetched this iteration: `https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/`.

Why it clears the gate for this constituency, from the article text I read: initial access through *"an exposed SonicWall VPN device without multi-factor authentication"* — ground the store already carries (two SonicWall/Akira records in `state/cves_seen.json`); a full sub-five-hour intrusion timeline (VPN login → RDP to domain controller → AD enumeration → application server → WinRAR staging of mapped shares → `s5cmd` upload to attacker S3 → AnyDesk); the defensive core, *"the host had no working EDR, and AV was blinded"* for ten minutes in Safe Mode with Networking, with AnyDesk added to the Safe Mode service registry to survive reboot; and named, behavioural detection guidance the pipeline's audience acts on — *"monitoring for Safe Mode boot configuration changes or remote-access tools being added to the Safe Mode service registry."* Huntress states it is the first time it has observed the tactic in an Akira attack (Snatch and AvosLocker have used it for years). Huntress is a tracked source in `sources/sources.json` (reliability B, active), so the research primary is reachable.

Why it is a gap rather than a deliberate omission: it is not in any entry (`grep -rli "safe mode" entries/` returns nothing store-wide), not in `state/coverage_backlog.md`, and not in any run record's borderline-drop list. It fell inside the **previous** fire's window — `runs/2026-08-15/2026-08-15T0412Z-intel.md` ran `window_hours: 50` from 2026-08-13T02:12Z and listed twelve borderline drops, none of them this. There is no 2026-08-14 fire (`runs/2026-08-14/` does not exist). So it is silently absent, which is the exact condition this run's own notes celebrate catching twice ("A completeness sweep of the fetch ledger recovered an item all four research passes missed") and which iteration 3 raised for Evooo1Bot on identical reasoning.

Remediation is a choice, not necessarily a sixth-plus entry: publish it as a recovery on the backlog's pipeline-race exemption (the same route the Adobe entry took this run), or open a `state/coverage_backlog.md` row for it. Either is acceptable; leaving it unrecorded is not. Suggested pivot: search `Huntress Akira Safe Mode with Networking AnyDesk s5cmd SonicWall` for the Huntress blog primary, which the BleepingComputer article links as its source ("Huntress says").

### Single-source items missing [SINGLE-SOURCE] flag

**F4 — `2026-08-16/cve-2026-65400-screen-sharing-confirmed-exploited-monero`: `verification: multi-source` contradicts the entry's own sourcing note, the run record's own bullet, and the two-source policy.**

Frontmatter: `verification: multi-source`, over exactly two `sources[]` records — NCSC-NL advisory NCSC-2026-0280 (primary) and BleepingComputer (corroborating).

The entry's own `sourcing_note` says: *"BleepingComputer reports the same NCSC-NL update rather than observing the activity independently, so this is one assessor with a second publisher — credibility 2."*

`prompts/verification.md` line 9: *"Independence is about first-hand observation, not count — six rewrites of one wire story are one source."* I confirmed the dependency directly: the BleepingComputer article is a report *of* the advisory (*"In an update to the initial advisory, the Dutch agency said it received a report…"*, then it quotes the NCSC text in English translation) and contains no independent observation of the activity.

The run record already classifies it the same way — line 238: *"Single source of assessment, two publishers: `2026-08-16/cve-2026-65400-screen-sharing-confirmed-exploited-monero`"* — so the frontmatter is the outlier against the record that describes it.

The exactly-fitting value is `single-source-national-cert`: NCSC-NL is on this deployment's carve-out list, and it is the primary disclosing party for the exploitation notification it received and for the advisory it owns. `single-source` would also be honest. The current value is not.

This is also the last remaining inconsistency in a window where the same structure was resolved twice already: iteration 4 moved the Evooo1Bot entry to `single-source` for *"one assessor with two republishing outlets"*, and the Jewelbug deep dive carries `single-source` for the same shape. This entry is the tightest case of the four — two sources, one of them an acknowledged rewrite.

**Do not cascade this to the SAP entry.** `2026-08-16/cve-2026-58231-sap-commerce-cloud-exploitation-attempts` carries `multi-source` over three sources and is materially different: alongside NCSC-NL and BleepingComputer (both carrying Defused's telemetry) it cites Onapsis, whose 2026-08-11 analysis I fetched and which is a genuinely independent first-hand contribution — the fixed release levels, the rebuild-and-redeploy requirement and the IP Filter Set workaround are Onapsis's own, and BleepingComputer separately carries a first-hand SAP spokesperson statement. Its sourcing note already discloses that the *exploitation* observation is single-assessor. Leaving that entry at `multi-source` is defensible; changing it would be an over-correction.

### Editorial / less-is-more flags (advisory)

**F5 — `2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay`: two of the four persistence mechanisms the body names are unmapped in `techniques[]`.**

Body: *"a systemd unit impersonating an Apache cache-manager service with automatic restart, a SysV init script, a cron entry re-fetching the loader every five minutes, **a profile.d injection and an rc.local append**"*. FortiGuard's Persistence Mechanisms section confirms all five (*"Shell profile: /etc/profile.d/ injection executed on login"*, *"rc.local: appends script to download the script in '/etc/rc.local.'"*).

`techniques[]` maps the systemd unit (`T1543.002`) and the cron entry (`T1053.003`) but not the shell-profile injection (`T1546.004`, Unix Shell Configuration Modification) or the rc.local/SysV init persistence (`T1037.004`, RC Scripts). Both ids are present, active and non-revoked in the pinned dataset (`attack/enterprise-attack.json`, ATT&CK v19.2). `techniques[]` is the canonical complete mapping surface, so mapping two of four persistence primitives leaves the `/attack/` overlap matrix short on a botnet whose persistence stack the entry itself calls "stacked deliberately".

**F6 — `2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole`: `references: []` although the store already names this actor in a European-government context.**

`entries/2026-05-04/uat-8302-china-nexus-talos-se-european-government-victims.md` states: *"Tooling overlap links UAT-8302 to multiple Chinese-quartermaster-shared clusters (Ink Dragon, Earth Alux, Jewelbug, REF7707, LongNosedGoblin, Erudite Mogwai / Space Pirates)"* — i.e. this run's new `actor:jewelbug` (aliases `Earth Alux`, `REF7707`) was already named in the store, in an entry about a cluster with *southeastern European government* victims. The run record acknowledges the absence of historical context only in terms of unfetched vendor reports ("No historical-context paragraph on the deep dive despite the actor having older prior reporting under three other vendor names") and does not mention the store's own prior mention.

A `references: [2026-05-04/uat-8302-china-nexus-talos-se-european-government-victims]` entry costs nothing and gives the reader the European-government thread that the deep dive's own "the transferable exposure is architectural, not geographic" framing has to argue for from scratch. **Caution for the remediation:** the prior entry attributes the overlap to Talos and frames it as tooling overlap only — do not let a reference become an asserted relationship in prose, and if the registry gains an edge it must be `overlaps-with`, sourced to the 2026-05-04 entry, not `attributed-to`.

**F7 — whole-run: two of the six entries rest on a `role: primary` from a publisher absent from `sources/sources.json`, and no candidate is proposed.**

`sources/sources.json` holds 182 source records. None of them is Symantec / security.com, Fortinet / FortiGuard Labs, or Cybersecurity Dive (verified by full-file grep for `security.com`, `fortinet.com` and `dive`, and by parsing every record's `id`/`url`). Yet:

- `2026-08-16/jewelbug-…` cites `https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage` as `role: primary` (and it is the deep dive's sole assessor);
- `2026-08-16/evooo1bot-…` cites `https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot` as `role: primary` (also sole assessor);
- `2026-08-16/exfilsquad-…` cites Cybersecurity Dive as corroborating.

`prompts/verification.md` line 9 allows *"a previously unseen publisher with a clearly verifiable editorial track record (**in which case the agent also proposes them as a `candidate` source**)"*. The run record's `sources_changed` block carries nine records, all notes-appended or metadata corrections, and proposes no candidate — although the guardrail allows one per run and two sole-assessor primaries this window came from untracked publishers.

Related telemetry drift in the same record: `sub_agents.S4.sources_attempted` / `sources_used` names `cybersecuritydive` and `bridge_uses` names `securitycom-symantec` as though they were registry ids. Neither string exists in `sources/sources.json`, nor in this run's own `work/2026-08-16T0411Z-intel/source_allocation.json`, so source-health and coverage tooling cannot attribute either.

**F8 — `2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role`: the headline hardens a hedge the summary and body both keep.**

Headline: *"Fortra confirms ExfilSquad's data is genuine across 13 victims and **counts over 10,000 publicly reachable Power Pages instances**"*. Infosecurity Magazine's wording, verified: *"it was able to identify over 10,000 **potential** Power Pages instances accessible to the public"*. The `summary` and the body both preserve "potential"; only the headline (and, more mildly, the takeaway's *"a five-figure number on how many Power Pages portals are publicly reachable"*) drop it. The word carries the fingerprint-identification hedge, and this store's own standard is to keep it — the SAP entry in the same window carefully renders Shadowserver's figure as *"IP addresses carrying a SAP Commerce Cloud fingerprint"* plus the honeypot caveat. One-word fix.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 4)

Truth = F1 (F3, claim-not-supported), F2 (F4, hallucinated-fact). Editorial = F3 (F10, missed-angle), F4 (F12, single-source-flag-missing). Advisory = F5, F6, F7, F8 (all F11).

Both truth findings are on the Evooo1Bot entry, which is the only entry of the six that no prior iteration read against a full independent fetch of its research primary (the spawn brief records the Fortinet blog as reachable only by `WebFetch`; the bridge in fact serves the whole article). The other five entries survived a hostile line-by-line pass with no truth defect. The remaining editorial finding, F4, is the last unresolved instance of a `verification`-value inconsistency this loop has already fixed twice in the same window.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay"
  url_or_quote: "Command-and-control is AES-256-CTR and ChaCha20 over TCP/443 to sit inside ordinary HTTPS egress"
  summary: "FortiGuard attributes AES-256-CTR and ChaCha20 to compile-time string obfuscation ('multiple layers of string obfuscation using AES-256-CTR, ChaCha20, and XOR-based key derivation'), listed separately from 'encrypted C2 communications'; the page names no cipher for the C2 channel. Port 443 and the HTTPS-blending rationale ARE supported. Knock-on: techniques[] T1573.001 (Symmetric Cryptography) rests on the same unsupported binding — demote to T1573 or source the cipher."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay"
  url_or_quote: "affected_products: [... \"WSO2 API Manager\", \"WSO2 Identity Server\", \"WSO2 Enterprise Integrator\" ...] and actions[0] 'WSO2 API Manager, Identity Server or Enterprise Integrator'"
  summary: "No cited source names any of the three: FortiGuard's exploit table row reads 'CVE-2022-29464 | WSO2 products | /fileupload/', BleepingComputer says 'WSO2 products', The Record does not mention WSO2 at all. Reduce to what the sources name (e.g. a single 'WSO2 products' value) and reword the action, or add WSO2's own CVE-2022-29464 advisory as a source. Lesser same-shape case for judgement: 'Atlassian Confluence Server' / 'Atlassian Confluence Data Center' where both sources say only 'Atlassian Confluence'. Every other affected_products value checks out against the FortiGuard page."
- code: F10
  category: missed-angle
  section: whole-run
  item: "Akira affiliate disables EDR via Safe Mode with Networking (Huntress DFIR case, BleepingComputer 2026-08-13T20:47Z)"
  url_or_quote: "https://www.bleepingcomputer.com/news/security/akira-hackers-disable-edr-with-safe-mode-steal-data-but-fail-to-encrypt/"
  summary: "Not in any entry (store-wide grep for 'safe mode' returns nothing), not in state/coverage_backlog.md, not in any run record's drop list — silently absent. Fell inside the previous fire's window (runs/2026-08-15, window_hours 50 from 2026-08-13T02:12Z; no 2026-08-14 fire exists). Relevance: SonicWall VPN without MFA as initial access (tracked ground), sub-5-hour intrusion timeline, ten minutes with 'no working EDR, and AV was blinded', AnyDesk added to the Safe Mode service registry, and named detection guidance (Safe Mode boot configuration changes; remote-access tools added to the Safe Mode service registry). Huntress is a tracked source (reliability B, active). Remediate by publishing as a backlog/pipeline-race recovery OR opening a backlog row — not by leaving it unrecorded. Query: 'Huntress Akira Safe Mode with Networking AnyDesk s5cmd SonicWall'."
- code: F12
  category: single-source-flag-missing
  section: trending-vulnerabilities
  item: "2026-08-16/cve-2026-65400-screen-sharing-confirmed-exploited-monero"
  url_or_quote: "verification: multi-source (sources: https://advisories.ncsc.nl/2026/ncsc-2026-0280.html + https://www.bleepingcomputer.com/news/security/hackers-exploit-macos-screen-sharing-flaw-to-deploy-monero-miner/)"
  summary: "Two sources, one of which the entry's own sourcing_note calls a non-independent rewrite ('BleepingComputer reports the same NCSC-NL update rather than observing the activity independently, so this is one assessor with a second publisher'); verification.md line 9 says independence is first-hand observation, not count. The run record already lists it under 'Single source of assessment, two publishers'. Correct value: single-source-national-cert (NCSC-NL is on the carve-out list and owns the advisory). DO NOT cascade to the SAP entry, which has a genuinely independent third source (Onapsis's own patch analysis) plus a first-hand SAP statement and is defensible at multi-source."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "2026-08-16/evooo1bot-mirai-derivative-enterprise-exploits-socks5-relay"
  url_or_quote: "techniques: [T1190, T1110.001, T1090.002, T1040, T1573.001, T1543.002, T1053.003, T1497.001, T1498, T1027, T1584.005]"
  summary: "Body names four persistence mechanisms; only systemd (T1543.002) and cron (T1053.003) are mapped. The profile.d injection (T1546.004, Unix Shell Configuration Modification) and the rc.local / SysV init persistence (T1037.004, RC Scripts) are unmapped; both are active and non-revoked in the pinned ATT&CK v19.2 dataset and both are stated on the FortiGuard page."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole"
  url_or_quote: "references: []"
  summary: "entries/2026-05-04/uat-8302-china-nexus-talos-se-european-government-victims.md already names 'Earth Alux, Jewelbug, REF7707' as Talos-reported tooling-overlap clusters with UAT-8302, an actor the store covers for southeastern European government victims. Adding that entry to references[] gives the deep dive the European-government thread its 'architectural, not geographic' framing currently argues from scratch. Caution: keep it a reference; any registry edge must be overlaps-with sourced to the 2026-05-04 entry, never attributed-to, and no attribution claim in prose."
- code: F11
  category: editorial-advisory
  section: whole-run
  item: "runs/2026-08-16/2026-08-16T0411Z-intel.md — source registry gap and telemetry id drift"
  url_or_quote: "sources[0] role: primary = https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage and https://www.fortinet.com/blog/threat-research/multi-functional-linux-botnet-evooo1bot"
  summary: "Neither publisher (nor Cybersecurity Dive) exists in sources/sources.json (182 records; verified by full-file grep and by parsing every id/url), yet both are sole-assessor primaries this window. verification.md line 9 requires proposing a previously unseen publisher as a candidate source; sources_changed proposes none, and the one-candidate-per-run ceiling leaves room. Separately, S4's sources_attempted/sources_used names 'cybersecuritydive' and bridge_uses names 'securitycom-symantec' as registry ids; neither string exists in sources/sources.json or in this run's own source_allocation.json, so source-health tooling cannot attribute them."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "2026-08-16/exfilsquad-fortra-confirms-13-victims-power-pages-anon-role"
  url_or_quote: "headline: '... counts over 10,000 publicly reachable Power Pages instances'"
  summary: "Infosecurity Magazine says 'over 10,000 POTENTIAL Power Pages instances accessible to the public'; the summary and body both keep 'potential', only the headline (and, mildly, the takeaway's 'how many Power Pages portals are publicly reachable') drop the fingerprint hedge. The SAP entry in the same window preserves the analogous Shadowserver hedge. One-word fix."
```
