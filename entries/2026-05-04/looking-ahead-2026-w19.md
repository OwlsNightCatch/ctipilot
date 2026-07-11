---
schema: 1
kind: outlook
horizon: strategic
weekly_section: weekly-looking-ahead
title: Looking ahead — 2026-W19
headline: Looking ahead — 2026-W19
summary: "Canvas / Instructure extortion deadline — Tuesday 2026-05-12 (two days out). Second-intrusion claim against Instructure made 2026-05-08 despite the May 8 patches; seven Dutch universities disconnected; Dutch DPA and ICO engaged."
discovered_at: "2026-05-04T05:00:52Z"
event_date: 2026-05-10
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - lpe
regions:
  - global
sectors: []
entities:
  - "actor:thegentlemen"
  - "actor:shinyhunters"
  - "campaign:cl-sta-1132"
cves: []
sources:
  - url: "https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/"
    publisher: Techzine EU
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-0300"
    publisher: Palo Alto PSIRT
    role: corroborating
  - url: "https://www.wiz.io/blog/dirty-frag-linux-kernel-local-privilege-escalation-via-esp-and-rxrpc"
    publisher: Wiz Research
    role: corroborating
  - url: "https://bishopfox.com/blog/cve-2026-42208-pre-authentication-sql-injection-in-litellm-proxy"
    publisher: Bishop Fox
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/04/critical-moveit-automation-auth-bypass-vulnerability-fixed-cve-2026-4670/"
    publisher: Help Net Security
    role: corroborating
  - url: "https://security-hub.ncsc.admin.ch/api/posts/12551/details"
    publisher: NCSC-CH 12551
    role: corroborating
  - url: "https://www.ivanti.com/blog/may-2026-epmm-security-update"
    publisher: Ivanti PSIRT
    role: corroborating
  - url: "https://research.checkpoint.com/2026/dfir-report-the-gentlemen/"
    publisher: Check Point Research DFIR Report
    role: corroborating
  - url: "https://www.zerofox.com/intelligence/q1-2026-ransomware-wrap-up/"
    publisher: ZeroFox Q1 2026 Wrap-Up
    role: corroborating
  - url: "https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/"
    publisher: TechCrunch — Braintrust
    role: corroborating
  - url: "https://www.enisa.europa.eu/news/new-cve-numbering-authorities-under-enisa-root"
    publisher: ENISA
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

Items already in motion at the close of 2026-W19. Not predictions — each links to the in-motion reporting underneath.

- **Canvas / Instructure extortion deadline — Tuesday 2026-05-12 (two days out).** Second-intrusion claim against Instructure made 2026-05-08 despite the May 8 patches; seven Dutch universities disconnected; Dutch DPA and ICO engaged. If deadline passes with no payment and a fresh data dump lands, the second-intrusion claim will have been verified ([daily 2026-05-10 UPDATE](/briefs/2026-05-10/); [Techzine EU](https://www.techzine.eu/news/security/141149/dutch-university-disconnects-canvas-systems-after-instructure-hack/)).
- **PAN-OS CVE-2026-0300 first patch landing 2026-05-13 (Monday).** No patch exists at week-end; staged release runs 2026-05-13 → 2026-05-28 across PAN-OS branches. Retrospective hunt for `svc-health-check-NNNNNN` admin accounts and `/var/tmp/linuxupdate` / `/tmp/.c` Python implants is the open work item for organisations who were CL-STA-1132 targets between 2026-04-09 and patch deployment ([Palo Alto PSIRT](https://security.paloaltonetworks.com/CVE-2026-0300); [daily 2026-05-09](/briefs/2026-05-09/)).
- **CVE-2026-31431 "Copy Fail" patch propagation through Friday 2026-05-15.** Distro patches continuing to land; Debian 12 patch was pending at week-end; combined-use pattern with Dirty Frag means a host patched for one but not the other still has an LPE primitive available. The Microsoft Security Blog detection-pivot writeup is the right hunt reference ([daily 2026-05-09 UPDATE](/briefs/2026-05-09/)).
- **CVE-2026-43500 (Dirty Frag RxRPC) distribution patches pending.** Distro patches were pending at week-end; CVE-2026-43284 (xfrm-ESP) mainline patch landed 2026-05-08; the second primitive's patch propagation is the open work. Interim mitigation `modprobe -r esp4 esp6 rxrpc` breaks IPsec VPNs and AFS so production rollout requires impact-test ([Wiz Research](https://www.wiz.io/blog/dirty-frag-linux-kernel-local-privilege-escalation-via-esp-and-rxrpc); [daily 2026-05-09](/briefs/2026-05-09/)).
- **CVE-2026-42208 LiteLLM Proxy deadline 2026-05-11 (Monday).** Patch to ≥ 1.83.7; rotate every upstream LLM-provider API key the proxy ever held. The corollary action item — inventory of every AI-tooling SaaS vendor holding organisation-level upstream-provider keys, with rotation drills — should ship in the same change window ([Bishop Fox](https://bishopfox.com/blog/cve-2026-42208-pre-authentication-sql-injection-in-litellm-proxy); [daily 2026-05-09](/briefs/2026-05-09/)).
- **MOVEit Automation CVE-2026-4670 — exploitation still not confirmed at week-end; watch for KEV addition or first-victim disclosure.** No in-the-wild exploitation has been confirmed by Progress, CISA, or any threat-intelligence source as of 2026-05-10. The 2023 MOVEit Transfer Cl0p precedent primed expectations for rapid exploitation; the absence of ITW confirmation is itself a status worth tracking through 2026-W20. Unpatched MOVEit Automation deployments remain at risk; if KEV addition or victim disclosure lands in next week's reporting, it will be the highest-priority pivot ([Help Net Security](https://www.helpnetsecurity.com/2026/05/04/critical-moveit-automation-auth-bypass-vulnerability-fixed-cve-2026-4670/); [daily 2026-05-06](/briefs/2026-05-06/)).
- **SEPPmail CVE-2026-44128 — independent third-party security-researcher analysis.** Currently single-sourced to NCSC-CH + vendor release notes (national-CERT carve-out applies). Watch for a vendor-PSIRT-style third-party write-up that would corroborate the exploitation-path detail; the GINAv2 `/gina/diag/exec` mechanic is sufficiently specific that PoC publication is plausible ([NCSC-CH 12551](https://security-hub.ncsc.admin.ch/api/posts/12551/details); [daily 2026-05-09](/briefs/2026-05-09/)).
- **Ivanti EPMM May 2026 patch wave aftermath.** With the KEV deadline (2026-05-10) expired and 508 EU instances confirmed exposed, the public-disclosure roster of EU compromised entities is likely to expand. Watch for additional EU member-state CSIRT advisories naming victims ([Ivanti PSIRT](https://www.ivanti.com/blog/may-2026-epmm-security-update); [daily 2026-05-08 deep dive](/briefs/2026-05-08/)).
- **"The Gentlemen" RaaS — European concentration likely to continue into Q2.** W1 horizon research surfaced the operator pattern; with ZeroFox-reported 32% Q1 2026 European targeting (up from 2% in Q4 2025) and GPO-injected scheduled-task encryptor propagation across compromised AD domains, continued European victim claims through 2026-Q2 are in motion. Watch for fresh CH/EU public-sector victim disclosures ([Check Point Research DFIR Report](https://research.checkpoint.com/2026/dfir-report-the-gentlemen/); [ZeroFox Q1 2026 Wrap-Up](https://www.zerofox.com/intelligence/q1-2026-ransomware-wrap-up/); § 7).
- **AI-tooling SaaS multi-tenant credential aggregation — sector pattern still surfacing.** Braintrust (2026-05-04 AWS) and LiteLLM Proxy (KEV 2026-05-11) are the two confirmed examples of the same architectural class this week. Watch for additional AI-evaluation, AI-observability, AI-agent-gateway, or prompt-management vendor breaches; the operator class behind ShinyHunters / WorldLeaks is actively exploiting the third-party-SaaS pivot pattern ([TechCrunch — Braintrust](https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/); [daily 2026-05-10](/briefs/2026-05-10/)).
- **ABW NIS2 extension proposal — EU follow-on movement.** ABW recommended legislative action to extend NIS2 essential-entity obligations to critical-function entities regardless of headcount (currently many small municipal CI operators sit below threshold). Whether this proposal gains EU-level momentum, or whether other member-state CSIRTs / EU institutions echo the same call after the Polish-water-OT tri-attribution, is the policy-horizon story to track ([daily 2026-05-09 UPDATE](/briefs/2026-05-09/)).
- **ENISA CVE Root migration — 4 new CNA names pending disclosure.** ENISA's 2026-05-06 announcement did not disclose the four new CNAs; ~90 European CNAs remain eligible for voluntary transfer. Disclosure of the 4 named CNAs and any additional transfers in 2026-W20 will inform EU public-sector PSIRT-coordination posture ([ENISA](https://www.enisa.europa.eu/news/new-cve-numbering-authorities-under-enisa-root); [daily 2026-05-07](/briefs/2026-05-07/)).
