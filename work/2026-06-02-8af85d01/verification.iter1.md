**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8`) — env vars CLAUDE_FRIENDLY_NAME/CLAUDE_MODEL_ID unset; identified from runtime context.
**Timestamps:** started_at=2026-06-02T04:41:03Z · ended_at=2026-06-02T04:44:05Z · duration_seconds=182

## Verification report — briefs/2026-06-02.md (iteration 1)

Read cold. Fetched every TL;DR link, every §2 CVE Source, the §4 UPDATE sources, the §5 deep-dive primary + additional, and the §1/§3 item sources. Two SPA advisory pages (EUVD-2026-33648, BSI WID-SEC-2026-1740) returned empty Angular shells to the fetcher/bridge and could not be content-verified — noted inline, not flagged as defects (they resolve, are specific advisory-detail URLs, and the mechanical gate passed them).

### Citation does not support the claim

**F3 — Disig Web Signer (§2, CVE-2026-8931): the primary Source does not support the RCE / CVSS-9.4 / eIDAS-context claims framed around it, and is mis-dated.**
Brief states: "CVE-2026-8931 (CVSS 4.0 9.4) is a remote-code-execution flaw in Disig Web Signer 2.0.3–2.5.3 ... used to apply qualified electronic signatures ... in Slovak government portals (slovensko.sk), banking and notarial systems ([Disig advisory, 2026-06-01])". The cited Disig advisory (https://www.disig.sk/en/news/important-update-of-the-web-signer-application/) — fetched this iteration — is dated **2026-05-11** (not 2026-06-01), assigns **no CVE**, does **not** classify the flaw as RCE, gives **no CVSS score**, and does **not** mention eIDAS, slovensko.sk, SK-CERT, or banking/notarial use. It confirms only: a "critical vulnerability", affected versions 2.0.3–2.5.3, fix 2.5.5, and researcher Marek Alakša (Binary House). The RCE/CVSS-9.4/eIDAS/SK-CERT specifics must rest on the EUVD additional source (EUVD-2026-33648), which returned an empty SPA shell and could not be confirmed this iteration. Fix: either re-anchor the RCE/CVSS/eIDAS claims to a source that actually carries them (verify EUVD content), or soften to what Disig states; and correct the Disig advisory date to 2026-05-11.

### Unsupported / hallucinated facts

(none — see F13 for the misattributed analytical link, which is the closest call.)

### Analytical-link-as-fact

**F13 — Dragon Weave (§5): the SteppeDriver / UNC5221 tooling-overlap is attributed to Seqrite, but the Seqrite primary makes no such link.**
Brief §5 Attribution: "Seqrite attributes the activity to a China-based cluster and reports tooling overlaps it links to previously documented **SteppeDriver and UNC5221** activity". The Seqrite primary (https://www.seqrite.com/blog/operation-dragon-weave-...) — fetched this iteration — attributes the activity only to a "China-based threat actor" assessed with **moderate confidence and no specific named group**, and contains **no mention of SteppeDriver or UNC5221**. The SteppeDriver/UNC5221/NegativeGlimmer grouping comes from the additional source, The Hacker News (https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html), as part of THN's *broader* China-nexus roundup framing — not as Seqrite's specific assessment of Dragon Weave's tooling. The brief's "Seqrite ... reports tooling overlaps it links to ... SteppeDriver and UNC5221" mis-binds THN's editorial grouping to the Seqrite researcher. The brief's hedge ("treat the nexus as the researcher's assessment ... overlap claim is the analytical thread") is good, but the *attribution of the overlap to Seqrite* is the defect. Fix: attribute the SteppeDriver/UNC5221 overlap to The Hacker News's broader reporting, OR state that Seqrite assessed China-nexus at moderate confidence WITHOUT a named-group overlap and that THN situates it among SteppeDriver/UNC5221-class activity. NB: the January-2026 Cobalt-Strike / Cambodia / South-Korea detail (also not in Seqrite) IS supported by THN and is fine as written since the brief does not bind it specifically to Seqrite.

### Surface contradiction

**F9 — Miasma (§1): weekly-download count differs between the two cited sources; brief picks Wiz's figure silently.**
Brief: "96 releases that together draw roughly 80,000 weekly downloads ([Wiz] · [Aikido])". Wiz (fetched) gives ~80,000 weekly downloads; Aikido (fetched, https://www.aikido.dev/blog/red-hat-npm-packages-compromised-credential-stealing-worm) gives "downloaded 116,991 times per week". Both are cited on the same clause. The 80,000 figure binds correctly to Wiz, so this is not a misattribution — but the two cited primaries disagree by ~37k. Advisory-grade: consider a one-line "(Wiz ~80k / Aikido ~117k weekly downloads)" or pick the higher with attribution. The 32-packages/96-releases figures, TeamPCP attribution, OIDC trusted-publishing abuse, and the new GCP/Azure cloud-identity collectors are ALL confirmed across Wiz + Aikido — no defect there.

### Editorial / less-is-more flags (advisory)

**F11a — WP Maps Pro (§2): citation date and CVSS provenance.** BleepingComputer (fetched, https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites/) is dated **2026-05-31**, not 2026-06-01 as cited; it confirms the flaw is "critical" and Wordfence blocked 3,600 attempts in 24h, but does **not** state CVSS 9.8 (the 9.8 must come from The Hacker News, which is the additional source — acceptable). Fix is minor: correct the inline date to 2026-05-31. The fix-version 6.1.1 (released 2026-05-20 per the article) and the live-exploitation framing are supported. Note §7 already candidly flags the absence of a vendor PSIRT for this item.

**F11b — Charter §4 UPDATE: vishing→Entra→Salesforce chain not in the in-window source.** The §4 update asserts "attributing the breach to a vishing-driven compromise of an employee Microsoft Entra account followed by a Salesforce export". The cited Security Affairs article (fetched) does NOT carry this chain. It is, however, well-established in prior coverage (2026-05-27 Charter item + the W22 ShinyHunters Salesforce arc) and the brief frames it as "the same access pattern seen across the broader ShinyHunters Salesforce campaign" — a legitimate callback. Advisory only: no fix required, but if tightening, anchor that clause to the prior-coverage Source. The 4.9M unique emails / HIBP, 30-May publication after ransom refusal, ~85k employee-directory subset with job titles, and 42M-vs-CPNI / Charter's no-CPNI statement are ALL confirmed in Security Affairs.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 2)

Truth: F3 (Disig primary does not support RCE/CVSS/eIDAS + wrong date), F13 (SteppeDriver/UNC5221 overlap mis-attributed to Seqrite). Advisory: F9 (download-count contradiction), F11a (WP Maps date), F11b (Charter chain provenance). F11 items are leave-able; F3 and F13 should be remediated before publish.

Items verified clean and well-sourced: CVE-2026-41089 Netlogon (CCB attribution correct, no port/protocol asserted, Microsoft-not-updated correctly stated, CVSS/component all supported by BleepingComputer + Help Net Security); Gamaredon GammaPhish/GammaWorm (Sekoia primary supports every detail incl. CVE-2025-8088, 20k-line VBScript, NTFS-ADS, dead-drop resolvers, LitterDrifter subsumption); GoDaddy/Steam (~1,980 sites, six Unicode chars, two-stage PHP, access vectors all confirmed); Spain doxer (arrest 27 May, Court No. 22, BreachForums "Police-ESP-Doxed", INCIBE no-direct-compromise all confirmed); Meta AI/Instagram (Telegram circulation, pro-Iran defacement of Obama WH + Space Force handles, MFA-immune, Meta resolved — all confirmed by Krebs); Miasma core facts (32/96, TeamPCP, OIDC, GCP/Azure collectors); Charter core facts. §7 drop rationales (PHANTOMPULSE, Check Point AI digest, CIFSwitch LPE, Vodafone, CVE-2024-21182 KEV, Dashlane, Anthropic Mythos) are all coherent and correctly out-of-window or gate-failing. No IOCs, no vanity metrics, English throughout, no workflow-language leakage. Coverage shape leads CH/EU public-sector correctly. MITRE technique IDs in §5 (T1566.001, T1059.001, T1574.002, T1102.001, T1071.001) all match the Seqrite ATT&CK list.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-8931 — Disig Web Signer"
  url_or_quote: "https://www.disig.sk/en/news/important-update-of-the-web-signer-application/"
  summary: "Cited Disig primary (dated 2026-05-11, not 2026-06-01) assigns no CVE, no RCE classification, no CVSS 9.4, and no eIDAS/slovensko.sk/SK-CERT context — all of which the brief frames around it; those rest on EUVD additional source which could not be content-verified (SPA shell). Re-anchor claims or soften, and fix date to 2026-05-11."
- code: F13
  category: analytical-link-as-fact
  section: deep-dive
  item: "Operation Dragon Weave"
  url_or_quote: "Seqrite attributes the activity to a China-based cluster and reports tooling overlaps it links to previously documented SteppeDriver and UNC5221 activity"
  summary: "Seqrite primary names no group and never mentions SteppeDriver/UNC5221 (China-nexus moderate confidence only). The SteppeDriver/UNC5221 grouping comes from The Hacker News's broader roundup, not from Seqrite. Re-attribute the overlap to THN, not Seqrite."
- code: F9
  category: surface-contradiction
  section: active-threats
  item: "Miasma worm — Red Hat npm"
  url_or_quote: "96 releases that together draw roughly 80,000 weekly downloads (Wiz / Aikido)"
  summary: "Wiz says ~80,000 weekly downloads; Aikido (same clause) says 116,991. Brief silently uses Wiz figure. Advisory: surface both or attribute. 32/96/TeamPCP/OIDC/GCP-Azure collectors all confirmed."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-8732 — WP Maps Pro"
  url_or_quote: "https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites/"
  summary: "BleepingComputer article dated 2026-05-31 not 2026-06-01; does not carry CVSS 9.8 (THN does). Correct inline date. Core facts (live exploitation, 6.1.1 fix, 3600 blocked attempts/24h) confirmed."
- code: F11
  category: editorial-advisory
  section: updates
  item: "Charter §4 UPDATE — ShinyHunters"
  url_or_quote: "attributing the breach to a vishing-driven compromise of an employee Microsoft Entra account followed by a Salesforce export"
  summary: "vishing/Entra/Salesforce chain not in cited Security Affairs source but well-established in prior coverage and framed as a callback. Leave-able; optionally anchor to prior-coverage Source. 4.9M/HIBP/85k/42M-vs-CPNI all confirmed."
```
