**Model:** Claude Opus 4.7 (1M context) (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-19T04:54:08Z · ended_at=2026-05-19T05:03:04Z · duration_seconds=536

## Verification report — briefs/2026-05-19.md (iteration 3)

### Citation does not support the claim

**F1.** § 2 CVE Summary Table and § 5 Deep Dive — wrong patched versions for three of the five n8n CVEs.

Claim quoted (brief § 2 narrative + table + § 5 deep dive): all five CVEs (CVE-2026-42231 / -42232 / -44789 / -44790 / -44791) are "Patched in n8n 1.123.32, 2.17.4, and 2.18.1." Deep dive § 5 repeats: "Apply the vendor patch (n8n `1.123.32` / `2.17.4` / `2.18.1`)". TL;DR also says "Patched in 1.123.32 / 2.17.4 / 2.18.1".

What sources actually say (verified by fetching each GHSA advisory in this iteration):
- GHSA-q5f4-99jv-pgg5 (CVE-2026-42231) → ≥1.123.32 / 2.17.4 / 2.18.1 ✓
- GHSA-hqr4-h3xv-9m3r (CVE-2026-42232) → ≥1.123.32 / 2.17.4 / 2.18.1 ✓
- **GHSA-c8xv-5998-g76h (CVE-2026-44789) → ≥1.123.43 / 2.20.7 / 2.22.1** (not 1.123.32)
- **GHSA-57g9-58c2-xjg3 (CVE-2026-44790) → ≥1.123.43 / 2.20.7 / 2.22.1** (not 1.123.32)
- **GHSA-wrwr-h859-xh2r (CVE-2026-44791) → ≥1.123.43 / 2.22.1 / 2.20.7** (not 1.123.32)

The Hacker News [`2026/05/ivanti-fortinet-sap-vmware-n8n-patch.html`] explicitly states: "Fixed in n8n versions 1.123.32, 2.17.4, and 2.18.1" for CVE-2026-42231 and CVE-2026-42232, with **"later versions (1.123.43, 2.20.7, and 2.22.1) addressing the remaining three flaws"** — direct contradiction of the brief's table and § 5 paragraph for three of five CVEs.

This is a high-impact patch-action defect: a Tier-2 responder reading the action item and patching to 1.123.32 / 2.17.4 / 2.18.1 will close two of five CVEs and leave three open, including the file-read Git-node CVE.

**F2.** § 2, § 5, CVE Summary Table — wrong GHSA→CVE mapping and wrong descriptions for CVE-2026-44789, -44790, -44791.

Claims quoted from § 2 narrative and § 5:
- "CVE-2026-44789 (GHSA-c8xv-5998-g76h)" — claim that this is XML Node injection
- "CVE-2026-44790, GHSA-wrwr-h859-xh2r" — claim that this is the Git node SSH chain
- "CVE-2026-44791 (GHSA-57g9-58c2-xjg3)" — claim that this is XML Node injection companion
- CVE table descriptions: "(XML Node injection)", "(Git node SSH chain → RCE)", "(XML Node injection companion)"

What the actual GHSA advisories say (verified by fetching each in this iteration):
- **GHSA-c8xv-5998-g76h = CVE-2026-44789** — title is **"HTTP Request Node Pagination Prototype Pollution to RCE"**, not XML Node injection
- **GHSA-57g9-58c2-xjg3 = CVE-2026-44790** — title is **"Arbitrary File Read via Git Node"** (command-line flag injection into `git push`), NOT a Git-node SSH RCE chain. The brief swaps the GHSA IDs for CVE-2026-44790 and CVE-2026-44791
- **GHSA-wrwr-h859-xh2r = CVE-2026-44791** — title is **"XML Node Prototype Pollution Patch Bypass"**, not the Git node SSH chain

The brief's Git-node-SSH-chain framing also overstates what the advisories support: the root advisory GHSA-q5f4-99jv-pgg5 mentions "the Git node's SSH operations" as a chain pivot but does NOT call out a specific companion CVE for an SSH primitive — the chained-to-RCE Git companion is the arbitrary-file-read flaw (CVE-2026-44790, GHSA-57g9-58c2-xjg3). The deep-dive § 5 paragraph "the chain's terminal sink is the n8n Git node's SSH operations (CVE-2026-44790, GHSA-wrwr-h859-xh2r)" is doubly wrong: wrong GHSA, and the linked GHSA describes a file-read primitive, not an SSH execution primitive.

### Unsupported / hallucinated facts

**F3.** TL;DR + § 4 UPDATE — Datadog Security Labs analysis date stated as 2026-05-15; actually 2026-05-13.

Claim quoted:
- TL;DR: "the leaked Shai-Hulud worm source code that Datadog Security Labs analysed on 2026-05-15"
- § 4 UPDATE: "following Datadog Security Labs' 2026-05-15 analysis of the leaked Shai-Hulud worm source code"

The brief from 2026-05-15 [`briefs/2026-05-15.md` line 97–101] cites Datadog Security Labs' analysis dated **2026-05-13** at `https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/`. The 2026-05-15 brief explicitly states "Datadog Security Labs published an analysis of the TeamPCP 'Shai-Hulud' offensive worm source code on **2026-05-13**". The current brief misstates the date as 2026-05-15 in three places. THN [`2026/05/four-malicious-npm-packages-deliver.html`] does not corroborate the 2026-05-15 date or mention Datadog at all in the context the brief implies.

**F4.** TL;DR + § 4 UPDATE — "new attacker public key"; both cited sources say "private key".

Claim quoted (§ 4 UPDATE blockquote): "`chalk-tempalte` is a near-unmodified clone of the leaked Shai-Hulud worm with a modified C2 server and a new attacker public key"

OX Security blog (cited): "almost exact copy" with "new C2 server and private key"
The Hacker News (cited): "almost without any change at all -- uploaded a working version with its own C2 server and private key into npm"

Both cited sources say **private key**; brief says **public key**. The distinction matters in asymmetric-crypto malware contexts (a victim-encrypting public key vs a C2-authentication private key the attacker holds). Either keep the source's wording verbatim or recharacterise the artefact functionally (e.g. "embedded keypair"), but do not silently flip the modifier.

### Analytical-link-as-fact (truth-class, F13 v2.53)

**F5.** TL;DR + § 1 INTERPOL — "first Algerian PhaaS takedown" / "first-of-its-kind PhaaS server takedown in the region" framed as if the source applies the quantifier to the Algerian operation.

Claim quoted:
- TL;DR: "13-country MENA cybercrime sweep: 201 arrests, 53 servers seized, first Algerian PhaaS takedown"
- § 1: "Algerian authorities dismantled a phishing-as-a-service operation — described as a first-of-its-kind PhaaS server takedown in the region"

INTERPOL's release (verified in this iteration) describes **the operation as a whole** as "first of its kind in the MENA region" — "first cyber operation of its scale coordinated by INTERPOL in the MENA region". The Algerian PhaaS dismantlement is one component within the broader operation; INTERPOL does NOT describe it specifically as a first-of-its-kind PhaaS takedown. The Hacker News (also cited) uses the same scoping — "INTERPOL has coordinated a first-of-its-kind cybercrime crackdown" — and frames the Algerian PhaaS as a component, not a standalone first.

The brief rewords the regional-operation-scale quantifier as a national-PhaaS-takedown quantifier, which is the F13 pattern: the brief asserts a connection between a quantifier and a specific entity that no cited source actually makes.

### Quantifier without source (truth-class, F14 v2.53)

**F6.** § 1 ARWINI — "approximately 11 million statutory-health-insurance (GKV) patients" — no cited source supports this figure.

Claim quoted: "the *Arbeitsgemeinschaft Wirtschaftlichkeitsprüfung Niedersachsen e.V.*, which audits prescription cost-effectiveness for approximately 11 million statutory-health-insurance (GKV) patients via data exchange with Kassenärztliche Vereinigung Niedersachsen (KVN), AOK and other insurers"

None of the cited sources state ~11 million:
- Deutsches Ärzteblatt: no patient-pool size figure
- Heise Security: no patient-pool size figure (mentions "75,000 datasets" affected and "2.87 TB" claim)
- Borns IT Blog: no patient-pool size figure (mentions "up to 80,000" affected, AOK, Techniker Krankenkasse)

Niedersachsen has ~8 million residents; ~90% in GKV would be ~7 million. "11 million" appears to be either a hallucinated number or a GKV-Germany-wide figure mis-applied to ARWINI's Niedersachsen scope. Either drop the figure, replace with the verifiable "~70,000 affected patients" figure that IS sourced, or add a source.

### Editorial / less-is-more flags (advisory)

**F7.** § 4 Grafana UPDATE — "five private repositories", "pull_request_target", "forked public repo / malicious curl injection / write-scoped GitHub token harvest", "Detection was via a triggered canary token" — the brief presents these as material new disclosures from 2026-05-18, but none of the four cited sources (SecurityWeek, BleepingComputer, The Hacker News [2026-05-17], The Register) actually disclose these technical details on 2026-05-18.

Verified by fetching all four sources in this iteration:
- SecurityWeek: confirms only "source code" + ransom refused, says nothing about repository count, workflow trigger, or canary detection
- BleepingComputer: confirms ransom refused on FBI guidance, says nothing about repository count, workflow trigger, or canary detection
- The Hacker News [2026-05-17]: confirms ransom refused on FBI guidance + 170 victims, says nothing about technical mechanism
- The Register: confirms ransom refused + FBI guidance, no technical mechanism details

These technical details (pull_request_target, fork-injected curl, canary detection) were already disclosed in the 2026-W21 weekly summary citing The Hacker News, where they appeared as the original technical reporting. The current brief's UPDATE framing — "The material new disclosures: ..." / "The root-cause confirmation is precise" — presents prior-week technical disclosures as if they are new 2026-05-18 confirmations, which they are not. The actual material new disclosures on 2026-05-18 are: ransom refused (on FBI guidance), only source code accessed, no customer/personal data, no operational impact. Recommend rewriting the UPDATE to scope the new-on-2026-05-18 material more tightly and either (a) drop the technical-mechanism re-statement, or (b) explicitly mark it as "as previously reported in the 2026-W21 weekly summary".

This is editorial rather than truth-class because the technical details themselves are not hallucinated — they were validly sourced in W21 — but the framing here drifts toward presenting prior disclosures as new and against four sources that don't restate them.

### Verdict

NEEDS_FIXES (truth: 6, editorial: 0, advisory: 1)

Truth-class breakdown: F1 (citation-doesn't-support, n8n patches), F2 (citation-doesn't-support, n8n GHSA mapping + descriptions), F3 (hallucinated date for Datadog analysis), F4 (hallucinated "public" vs "private" key), F5 (analytical-link-as-fact — INTERPOL Algerian PhaaS quantifier), F6 (quantifier-without-source — ARWINI 11 million GKV patients).

F1 and F2 in particular are high-impact patch-action defects — a defender following the § 6 action item, the § 2 table, or the § 5 deep dive will undermitigate by patching only the two-of-five fix train and leaving CVE-2026-44789/-44790/-44791 unaddressed.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "n8n CVE Summary Table + § 5 deep dive — patched versions for CVE-2026-44789 / -44790 / -44791"
  url_or_quote: "Patched in n8n 1.123.32, 2.17.4, and 2.18.1."
  summary: "Three of five n8n CVEs are patched in 1.123.43 / 2.20.7 / 2.22.1 per their GHSA advisories and per THN's explicit split (1.123.32/2.17.4/2.18.1 for -42231/-42232 only; 1.123.43/2.20.7/2.22.1 for -44789/-44790/-44791). High-impact patch-action defect."
- code: F2
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "n8n CVE Summary Table + § 5 deep dive — GHSA→CVE mapping and per-CVE descriptions"
  url_or_quote: "CVE-2026-44790, GHSA-wrwr-h859-xh2r" / "(XML Node injection)" / "(Git node SSH chain → RCE)" / "(XML Node injection companion)"
  summary: "Actual mapping per GHSA: CVE-2026-44789=GHSA-c8xv-5998-g76h='HTTP Request Node Pagination Prototype Pollution to RCE'; CVE-2026-44790=GHSA-57g9-58c2-xjg3='Arbitrary File Read via Git Node' (file-read primitive, NOT SSH RCE); CVE-2026-44791=GHSA-wrwr-h859-xh2r='XML Node Prototype Pollution Patch Bypass'. Brief swaps GHSAs for -44790/-44791 and miscategorises -44789/-44791 as XML Node when -44789 is HTTP Request Node."
- code: F3
  category: hallucinated-fact
  section: tldr+updates-to-prior-coverage
  item: "TL;DR final bullet + § 4 TeamPCP/Shai-Hulud UPDATE — Datadog analysis date"
  url_or_quote: "the leaked Shai-Hulud worm source code that Datadog Security Labs analysed on 2026-05-15"
  summary: "Datadog Security Labs published the analysis on 2026-05-13 per briefs/2026-05-15.md (which cites the article URL). Three occurrences in this brief misstate the date as 2026-05-15."
- code: F4
  category: hallucinated-fact
  section: updates-to-prior-coverage
  item: "§ 4 TeamPCP/Shai-Hulud UPDATE — chalk-tempalte key descriptor"
  url_or_quote: "a modified C2 server and a new attacker public key"
  summary: "Both cited sources (OX Security, The Hacker News) say 'private key', not 'public key'. Brief silently flips the modifier."
- code: F13
  category: analytical-link-as-fact
  section: tldr+active-threats
  item: "INTERPOL Operation Ramz — 'first Algerian PhaaS takedown' / 'first-of-its-kind PhaaS server takedown in the region'"
  url_or_quote: "described as a first-of-its-kind PhaaS server takedown in the region"
  summary: "INTERPOL's 'first-of-its-kind' applies to the operation overall, not to the Algerian PhaaS server takedown specifically. THN uses the same scoping. The brief reapplies the quantifier to a different scope than the source supports."
- code: F14
  category: quantifier-without-source
  section: active-threats
  item: "§ 1 ARWINI — ARWINI audits ~11 million GKV patients"
  url_or_quote: "audits prescription cost-effectiveness for approximately 11 million statutory-health-insurance (GKV) patients"
  summary: "None of the three cited sources (Deutsches Ärzteblatt, Heise Security, Borns IT Blog) state the 11 million figure. Niedersachsen's total population is ~8M. Replace with the verifiable ≥70,000-affected figure or drop the quantifier."
- code: F11
  category: editorial-advisory
  section: updates-to-prior-coverage
  item: "§ 4 Grafana UPDATE — technical-mechanism details framed as new 2026-05-18 disclosures"
  url_or_quote: "The material new disclosures: ... The root-cause confirmation is precise — a recently-enabled GitHub Action workflow using the `pull_request_target` event trigger..."
  summary: "The technical-mechanism details (pull_request_target trigger, forked-repo curl injection, write-scoped token, canary-token detection, five repositories) are not stated in any of the four cited 2026-05-18 sources (SecurityWeek, BleepingComputer, The Hacker News, The Register). They were previously sourced in the 2026-W21 weekly summary from THN's earlier coverage. The framing here presents prior disclosures as new — either scope the UPDATE more tightly to the genuinely new 2026-05-18 material (only-source-code, no-customer-data, FBI-guidance ransom refusal) or explicitly mark the technical-mechanism block as 'as previously reported in 2026-W21'."
```
