**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:57Z · ended_at=2026-10-18T13:50:03Z · duration_seconds=1386

## Retrospective truth pass T4, run 2026-10-18T1307Z-audit

14 entries read whole, 375 ledger claims each given a verdict row (361 ok, 14 flagged), sources fetched fresh this pass (cached quote bodies held none of the entries' primaries). Prior-audit (2026-09-30T0639Z) iteration-8 remediations for these entries all held: the Die Linke Contradiction line (BleepingComputer headline vs text) is correct, the Nx Console / TanStack Exposure and Detection additions match GHSA-g7cv-rxg3-hmpx, and the actions-cool priority decision was a declined finding (see below).

### Factual errors (2)

**2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac**
- Claim: "lost about $11M across nine blockchains after one of its six vaults was compromised" (summary; body paragraph 1 repeats "one of its six vaults").
  Ground truth: THORChain Exploit Report #1 (2026-05-20): "approximately $10.7M from a single vault (out of five)", "The remaining four vaults were unaffected" (The Record and CryptoTimes say six; TRM says more than USD 11 million). https://blog.thorchain.org/thorchain-exploit-report-1
  Fix: one vault (THORChain: one of five; The Record: six), about $10.7M per THORChain, with TRM's 11M+ noted or a Contradiction line.
- Claim: "GG20 Threshold Signature Scheme flaw suspected" (title), "the reported working theory" (headline), working theory in summary and body (imprecision).
  Ground truth: THORChain confirmed it on 2026-05-15 19:10 ("the leading theory is confirmed as an exploit in the GG20 TSS implementation allowing progressive key material leakage"); Exploit Report #2 (2026-07-03) is the post-mortem (multi-prime Paillier modulus, 864 deliberately failed signing rounds over two and a half days, three combined weaknesses). Neither primary is cited. https://blog.thorchain.org/thorchain-exploit-report-2
  Fix: replace "suspected / working theory" with the confirmed account and cite Reports #1 and #2.

**2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags**
- Claim (2026-09-30 record summary): "GitHub disabled the companion maintain-one-comment repository, not issues-helper".
  Ground truth: Socket, 2026-09-24: "GitHub security team disabled both repositories on May 19, 2026, one day after the malicious content was introduced." BleepingComputer 2026-09-26: GitHub removed both. https://socket.dev/blog/mini-shai-hulud-actions
  Fix: GitHub disabled both repositories on 2026-05-19; drop the "not issues-helper" contrast.
- Missing material development (imprecision): both actions were re-enabled on 2026-09-16 with every release tag still pointing at the May payload (workflows referencing a tag resumed running it), SafeDep found six more repositories infected 2026-09-20 to 09-24, GitHub disabled both again by 2026-09-25 (https://thehackernews.com/2026/09/compromised-github-actions-came-back.html). The entry says only that GitHub disabled maintain-one-comment, and the takeaway window ("on or after 2026-05-18") now has an open-ended 2026-09-16 to 09-25 leg.
  Fix: changelog update with the re-enable, the ~15,000 dependents on the issues-helper dependency graph, the re-disable, "review runs since 2026-09-16, pin to a SHA that predates 2026-05-18".
- Priority note: priority high is defensible only because of the September reactivation; as the entry stands (no September facts) it rests on a 2026-05-18 event.

### Imprecisions (8)

**2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n** (headline, summary): "had taken its infrastructure offline". Die Linke: "Teile der IT-Infrastruktur wurden vorsorglich vom Netz genommen" (parts of the IT infrastructure); the entry body already says "parts". https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/ Fix: "parts of its IT infrastructure".

**2026-05-08/eurail-breach-308-777-travellers-notified-three-months-after** (low confidence): `techniques: [T1005]`, a collection technique, while the sources say only "an unauthorized actor transferred files from our network on December 26, 2025". https://www.bleepingcomputer.com/news/security/eurail-says-december-data-breach-impacts-300-000-individuals/ Fix: drop or map only what is stated.

**2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u**: (1) tag `infostealer` contradicts the body: Sophos "a relatively simple backdoor" with commands uninstall, cmd, upload, download, mkdir, rename, ls, rm. (2) (low confidence) `sectors: technology`: no source names a sector, and the 2026-09-30 correction says Sophos does not say who the lures target. https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor

**2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x** (low confidence): "Kubernetes-context proof-of-concept exploits are public" (summary, 2026-09-05 section, evidence[2]) rests on Aikido's sentence about "Dirty Frag" as a whole (all three CVEs; its Ubuntu link is the CVE-2026-43284 page); no source states a Kubernetes PoC for CVE-2026-46300. https://www.aikido.dev/blog/dirty-frag Fix: attribute it to the Dirty Frag family or cite only the public Fragnesia PoC. Verified clean otherwise: CVSS 7.8 (Red Hat, NVD, cve.org), not in KEV, EPSS 0.0948 on 2026-09-04 (today 0.0243, the undated cves[].epss value is stale).

**2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s** (low confidence): T1556 (Modify Authentication Process) is described nowhere; the behavior is MFA device registration (T1098.005) and MFA relay (T1111, T1557). https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/ Fix: remove T1556.

**2026-05-16/node-ipc-npm-package-backdoored-via-expired-domain-account-t** (both low confidence): (1) "[CSO Online, 2026-05-14]": the article's datePublished is 2026-05-15. https://www.csoonline.com/article/4171926/expired-domain-leads-to-supply-chain-attack-on-node-ipc-npm-package.html (2) The correction's "No source says the malicious versions were removed from the registry" is true of the sources but stale: registry.npmjs.org/node-ipc no longer lists 9.1.6, 9.2.3 or 12.0.1 (publish timestamps remain), latest is 14.0.0. Priority note: priority high on a 2026-05-14 event with no later development does not meet the in-window high bar on today's facts.

**2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv** (low confidence): summary "Vanilla Tempest (Rhysida)" reads as Vanilla Tempest being Rhysida; Microsoft: "Vanilla Tempest also deployed Rhysida ransomware". https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/

**2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands**: cves[] carry `cvss: n/a` and null affected/fixed for all three CVEs; the CNAs publish CVE-2026-48027 CVSS v4.0 9.3 (affected "= 18.95.0", fixed 18.100.0), CVE-2026-45321 CVSS v3.1 9.6, CVE-2026-8398 CVSS v4.0 9.3 / v3.1 9.8 (12.5.0.2421 to 12.5.0.2434, clean 12.6). https://cveawg.mitre.org/api/cve/CVE-2026-45321 KEV: all three added 2026-05-27, ransomware use Known for 48027 and 45321.

### Clean (4)
2026-05-08 Ivanti EPMM (all five CVE ids, CVSS 7.2 / 8.9 / 8.8 / 7.0 / 7.4 and affected/fixed builds match the CNA records, only CVE-2026-6973 in KEV since 2026-05-07, quotes verbatim); 2026-05-08 ABW water plants (PDF passages, PL/EN dates 06.05 / 25.05.2026 on the ABW page); 2026-05-08 CVE-2026-32202 (MSRC CVSS 4.3, exploited, rev 2 on 2026-07-28, KEV 2026-04-28, no actor for this CVE); 2026-05-08 Dragos (every figure on the Dragos pages).

### Out-of-scope observations (entities/registry.yaml summaries that still carry retracted or unsupported statements)
- incident:eurail-breach-2026: "308,777 travellers notified in April 2026; the Dutch DPA and EDPS are reviewing the delayed notification" (the entry's correction: letters 2026-03-27, no source for a DPA/EDPS review).
- incident:daemon-tools-supply-chain-2026: "EU governments targeted" (Kaspersky: backdoor on about a dozen machines in government, scientific and manufacturing organizations in Russia, Belarus and Thailand).
