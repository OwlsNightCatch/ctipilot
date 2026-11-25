**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-25T04:55:27Z · ended_at=2026-11-25T05:13:14Z · duration_seconds=1067

## Verification report — 2026-11-25T0356Z-intel (iteration 1)

Scope: 6 new entries, 3 updated entries (full read plus `git diff HEAD`), run record, claim ledger `claims.iter1.yaml` (150 claims, all answered: 133 ok, 11 F3, 2 F4, 2 F14, 1 F5, 1 unreadable; rows in `verification.iter1.claims.yaml`). Sources re-read this iteration: BACS DE/EN, Netzwoche, GreyNoise, BleepingComputer, Check Point sk185169 and vendor blog, SecurityWeek, VulnCheck, EUVD records (Rejetto, Optimizely), Broadcom VMSA-2026-0009/-0011 advisories, both Q&As, KB463535/463501/463116, vCenter 9.1.2 release notes, GTIG, Rapid7, Metasploit PR 22173 (API), CISA KEV catalogue + 11/24 alert, Optimizely status page, Unit 42, ReliaQuest, GeoServer posts/announcement/18 GHSAs/CryptoCat/PoC repo, Splunk SVD-2026-1103, NCSC-NL CSAF.

### Citation does not support the claim
- #1 (F3) unit42-agentic-ai-attackers-web-shell-footholds: "the same find command ran on six endpoints, each excluding a different security vendor's directory". Unit 42: "executed the same find command on six compromised endpoints, excluding three different security vendors". Six endpoints, three vendors.
- #2 (F3, low confidence) unit42: "in another it pushed web shells to more than 40 locations on a Windows IIS server within 26 minutes and tried a vendor's GitLab credentials found on the victim's server". Unit 42 narrates the IIS push ("In one observed campaign") and the GitLab brute force ("In one campaign") separately; nothing says one intrusion.
- #3 (F3) geoserver: Exposure clause cites `geoserver.org/.../cve-update.html` for "the reporter says it works on a default installation, and the fixed releases use a random per-node key and invalidate existing remember-me cookies on upgrade"; that page has neither (CryptoCat and GHSA-hgm3 Resolution do). Detection cites GHSA-hgm3 for x/WFS slash requests, `wfs/query` folders and REST database upload/JDBC creation; those are in GHSA-rv5g-g2r9-58rj and GHSA-9wf2-fcgq-vxhq. "2.27 is end of life" is cited to GHSA-hgm3; the source is the 2.27.7 announcement ("This series has previously reached end-of-life").
- #4 (F3) geoserver: "announced on 2026-10-19 as an important upgrade for production systems without naming the flaws" cites the 3.0.2 announcement, which now has a "Security Considerations" list naming CVE-2026-129245, CVE-2026-120705, CVE-2026-129243 and others. True only of the 2026-11-06 archived copy.
- #5 (F3, low confidence) vmware-vcenter (update 2026-11-25T04:46:36Z): "8.0 U3m, VMware Cloud Foundation 5.2.5 and the Telco builds already carry that fix" cites the VMSA-0011 Q&A, which does not name the Telco builds (KB463501 does; not cited).
- #6 (F3) optimjack (improvement 2026-11-25T04:47:09Z): "lets an attacker impersonate existing customer users and modify Project JavaScript" cites the CISA alert page, which has only the title and "based on evidence of active exploitation"; the wording is the KEV record's shortDescription. "It affects the hosted service before 2026-11-17 ... no customer-side update" cites the Optimizely status page, which says "closed the vulnerability within three hours of detection" on 16 November and has no 2026-11-17 scope. `cves[].cvss: 7.1` is CVSS 4.0 per EUVD-2026-129010 (confirmed) but on no listed source.
- #7 (F3, low confidence) splunk summary: groups CVE-2026-131190 with bypasses that "rest on an empty shared secret"; advisory text: "accept a factory-default shared key".
- #8 (F3, low confidence) rejetto body, first sentence: "VulnCheck disclosed a six-CVE chain" cites a page carrying only CVE-2026-61500.

### Unsupported / hallucinated facts
- #9 (F4) greynoise-gt13: `cves[CVE-2026-16232].cvss: "9.3"`. No source listed on the entry carries it (sk185169: severityType HIGH, no score; BleepingComputer, GreyNoise: none). The Check Point blog table (https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-check-point-smartconsole-authentication-bypass-cve-2026-16232/) prints 9.3, while the stored 2026-07-23 entry carries 9.1 with an explicit NVD/vendor split note. Cite the vendor page and carry the split.
- #10 (F4, low confidence) greynoise-gt13 actions[0] and Detection: "check /root/.ssh/authorized_keys and /etc/ld.so.preload", "changes to authorized_keys and the preload file". GreyNoise's authorized_keys append was on the HFS relay; on Check Point it saw a preload error that "may indicate an implant" and private keys matching a key planted on the hop.
- #11 (F4) run record: "Splunk: `single-source-national-cert`"; the entry carries `verification: single-source`.

### Claims missing inline citation
- #12 (F5) rejetto: the five companion CVE ids and descriptions have no link; "all verified on NVD" is process narration. Values match EUVD-2026-43506 to -43511.

### Needs more research
- #13 (F8) vmware-vcenter update: the rewrite removed GTIG's observed chain and its detection items (SSH enabled then disabled via the management API, internal sweeps of 2012/5480/9080 from a non-management appliance, VMFS hidden directory) and kept only Rapid7's lab artefacts. summary still claims "forge administrator SAML sessions and extract domain-controller data from guest virtual disks on ESXi" and actions[1] "the actor extracted the SAML signing key and created accounts"; the body states neither now. GTIG supports all of it.
- #14 (F8) splunk: Splunk's CVE-2026-76535 workaround says "Use the same value on each node that participates in the service" and names no `[clustering]` stanza. Action and takeaway say "strong, unique pass4SymmKey ... in the [clustering] stanza ... on every instance"; the caveat is missing and per-instance keys could break clustered peers.
- #15 (F8) geoserver Exposure: dropped the reporter's preconditions "The stock `admin` account enabled in the `default` user service" and "A Linux host, because the payload runs `/bin/sh -c`" (https://cryptocat.me/blog/research/analysis/geoserver_preauth_rce/).

### Surface contradiction
- #16 (F9) greynoise-gt13: entry says "confirmed activity from 2026-10-17 to 2026-11-02"; GreyNoise's timeline says "We observed GT13 attack activity between 2026-10-02 13:17:45 and 2026-11-02 03:19:46 UTC" and that Check Point access pre-dated the HFS compromise. The entry never states 2 October (the Rejetto entry does) or the discrepancy; it sets the hunt window.
- #17 (F9, low confidence) vmsa-2026-0011: Q&A "8.5 for ESX" vs matrix 8.4 (entry follows 8.4 silently); vCenter 9.1.2 release notes list only CVE-2026-123906 to -123909 and omit CVE-2026-123903. Only the sourcing_note mentions a release-note disagreement; add a `Contradiction:` line.

### Drop (low relevance / off-audience / duplicate)
- #18 (F7, low confidence) splunk-enterprise-svd-2026-1103: no exploitation, no PoC, vulnerable state not shown to be default, management API normally internal; rests on CVSS. Keep at two sentences or drop unless SOC-owned SIEM exposure is the stated reason.

### Editorial / less-is-more flags (advisory)
- #19 (F11) updates[].summary on vCenter, Rejetto, OptimJack narrate field names ("the headline, summary, action and detection guidance now reflect it"; "its status, summary, action and takeaway now say it is exploited"; "the entry's CVE record carries it").
- #20 (F11) vCenter title still lists 9.0.2.0200/9.1.1.0200 as the fixed builds while headline/actions say 9.1.2/9.0.2.0300; headline "Metasploit module public" overstates an open, unmerged pull request.
- #21 (F11) Rejetto: headline does not reflect exploitation; entities `[]` omit actor:gt13 and product:rejetto-hfs; sourcing_note still attributes the exploitation assessment to VulnCheck's advisory.
- #22 (F11) OptimJack tags lack actively-exploited and cisa-kev though cves[] carries both.
- #23 (F11, low confidence) BACS entities `[]` although ARTEX and CyberStrikeAI are registry keys; defensible given the body's caution.

### Quantifier without source
- #24 (F14) splunk: "Two further unauthenticated rows are rated 7.5" (also in title). Advisory has three: CVE-2026-131190, -131192 and -131196 (S2S receiver DoS).
- #25 (F14, low confidence) bacs: "shares technical indicators only with critical-infrastructure operators"; the page has no "only".
- #26 (F14, low confidence) unit42: "Unit 42 gives no command lines or thresholds beyond the two timing medians"; Figures 3, 7, 8, 9 are images (not extractable) and the text gives other quantities. Claim row marked unreadable.

### Action-item discipline
- #27 (F18) vmware-vcenter actions[0] and vmsa-2026-0011 actions[0] are the same vCenter update task in two in-window entries; keep one.

### Checks that held
BACS quotes (DE and EN) and Netzwoche; GT13 counts (22, 24, 17 countries, seven sectors, 100+ tasks); Check Point fixed builds and audit-log query; VMSA-0011 CVE list (23), matrices, KB463535 port 9080, Q&A re-patch guidance; Rapid7 root cause and log trail; PR 22173 open and unmerged; KEV dates (CVE-2026-16232 2026-07-22, CVE-2026-123890 2026-11-20, CVE-2026-132224 2026-11-24); GeoServer 18 GHSAs, CVSS values and version ranges, PoC repo created 2026-11-23T22:43Z; Splunk 38 rows, 9.4/9.1/7.5 scores, fixed versions, NCSC-NL Kans medium/Schade high; Rejetto companion scores; ledger coverage 150/150. Classification codes consistent with source tiers. updated_at mirrors correct; no silent edit found; no em dash, IOC or workflow vocabulary in reader text. Coverage: the 18 borderline drops are defensible; no relevant in-window item found missing (Veria Labs Rails exploit is correctly parked for next fire).

### Verdict
NEEDS_FIXES (truth: 14, editorial: 8, advisory: 5)

### Findings summary (machine-readable)
See `work/2026-11-25T0356Z-intel/verification.iter1.findings.yaml` (27 records).
