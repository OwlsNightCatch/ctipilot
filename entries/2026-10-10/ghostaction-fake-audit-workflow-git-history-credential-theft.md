---
schema: 1
kind: threat
title: "GhostAction returns: stolen maintainer credentials push a fake security-audit workflow into the victims' own GitHub repositories, which now harvests credentials from the entire git history"
headline: "GhostAction: fake security workflows now harvest whole git histories; rotating Actions secrets is not enough"
summary: >
  StepSecurity and Socket report that on 2026-10-08 the GhostAction campaign used the GitHub credentials of two open-source maintainers to
  commit a workflow disguised as a security audit straight to the default branch of 345 to 346 repositories, including one of an Uber-owned organisation, and that
  the workflow now sends the credentials found in the working tree and in the entire git history, besides the named Actions secrets, to a hardcoded address over plain HTTP.
  StepSecurity read a run log showing the exfiltration was acknowledged four seconds after the run started; no malicious package release from the stolen credentials has been seen yet.
discovered_at: "2026-10-10T03:52:30Z"
updated_at: null
event_date: "2026-10-08"
run_id: 2026-10-10T0255Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, identity]
regions: [global]
sectors: [technology]
entities: ["campaign:ghostaction", "product:github-actions"]
techniques: [T1078.004, T1552.001, T1048.003]
affected_products: ["GitHub Actions"]
cves: []
sources:
  - url: "https://www.stepsecurity.io/blog/ghostaction-returns"
    publisher: "StepSecurity"
    date: "2026-10-09"
    role: primary
  - url: "https://socket.dev/blog/ghostaction-cloud-credentials"
    publisher: "Socket"
    date: "2026-10-09"
    role: primary
  - url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
    publisher: "GitGuardian"
    date: "2026-10-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "confirms the exfiltration completed successfully: the attacker's server acknowledged receipt four seconds after the workflow started"
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "Nothing in an audit log looks anomalous unless the workflow content itself is inspected"
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "The approval gate is worth singling out: it is the single control observed stopping this campaign's exfiltration this week."
    publisher: "StepSecurity"
    source_url: "https://www.stepsecurity.io/blog/ghostaction-returns"
  - quote: "Socket has observed no malicious package versions published to PyPI or crates.io as a result of this activity at the time of writing."
    publisher: "Socket"
    source_url: "https://socket.dev/blog/ghostaction-cloud-credentials"
  - quote: "Rotating the secrets exfiltrated by the malicious workflow is not enough. The GitHub credential that allowed the injection in the first place must be found and revoked too, or someone else will use it again."
    publisher: "GitGuardian"
    source_url: "https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/"
verification: multi-source
sourcing_note: >
  StepSecurity and Socket analysed the 2026-10-08 burst independently and GitGuardian documents the preceding wave; all three are security vendors whose claims rest
  on run logs, commit metadata and repository counts, and how the credentials were obtained is StepSecurity's and GitGuardian's assessment, not an observation.
  Socket's update line of more than 500 accounts and tens of thousands of repositories since 7 October carries no method and disagrees with the counts elsewhere, so it is not carried as fact.
confidence: high
references:
  - 2026-10-07/gentlemen-affiliate-azazel-ci-cd-secrets-mcp-attacks
  - 2026-05-23/megalodon-mass-poisons-5-561-github-repos-in-a-6-hour-window
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Run an organisation-scoped GitHub code search in every organisation your teams and suppliers administer for workflow files under .github/workflows that present themselves as a security audit, a security check or an Actions security workflow and were added since 2026-08-31; any hit means assume breach: revoke the credential that committed it and rotate every secret found anywhere in the repository's git history, not only the configured Actions secrets."
updates: []
migrated_from: null
---

StepSecurity reports that on 2026-10-08 the GhostAction GitHub Actions credential-theft campaign used the accounts of two open-source maintainers to push a workflow disguised as a security improvement to 345 repositories in two automated sweeps, among them an Uber-owned repository that one maintainer could still write to ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)); Socket's independent analysis counts 346 ([Socket, 2026-10-09](https://socket.dev/blog/ghostaction-cloud-credentials)). The operator holds a maintainer's GitHub credential, which StepSecurity assesses as most plausibly a personal access token leaked through infostealer logs or credential dumps, then commits a workflow titled to look like a security audit straight to the default branch under the victim's own identity, unsigned and without a pull request; that push runs it, and nothing in an audit log looks anomalous unless the content is read ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). GitGuardian says the technique was later reused in the Shai-Hulud campaigns and remains at the core of the Mini Shai-Hulud malware family ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)).

The newer payload sends the named Actions secrets and every cloud, AI-provider and SaaS credential pattern found in the working tree and the entire git history to a hardcoded address over plain HTTP, so no DNS lookup occurs ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). StepSecurity saw the attacker's server acknowledge the request four seconds into the run at the Uber-owned repository ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)); neither it nor Socket has seen a malicious package release from the stolen credentials yet ([Socket, 2026-10-09](https://socket.dev/blog/ghostaction-cloud-credentials); [StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). A Socket update line claims more than 500 accounts and tens of thousands of repositories since 7 October without a method, against 346 for the 8 October burst in its own body and 378 live-workflow repositories across all waves in StepSecurity's code search of 2026-10-09, so the larger figure stays unconfirmed ([Socket, 2026-10-09](https://socket.dev/blog/ghostaction-cloud-credentials); [StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

**Exposure:** any GitHub account whose token or session credential has leaked, and every repository it can write to; StepSecurity says a workflow posing as a security audit or an Actions security workflow that appeared in a repository you maintain since 2026-08-31 means treat it as a confirmed breach ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

**Detection:** source-control audit logs: workflow files added straight to default branches without a pull request by a maintainer identity, unsigned commits landing in many repositories within minutes; an organisation-scoped code search with StepSecurity's published content-marker queries for security-themed workflow files (audit, check or Actions security); runner egress logs: an HTTP POST to a bare IP address with no preceding DNS lookup ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)). Removing the workflow does not undo the theft: StepSecurity says any secret ever committed to a repository must be treated as compromised, so treat each run as an exfiltration, scan the full history and rotate every credential found ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)); GitGuardian adds that the GitHub credential that allowed the injection must be revoked too, or someone else will reuse it ([GitGuardian, 2026-10-07](https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/)).

**Triage:** the audit-log pattern separates this from a team adding a scanning workflow: no pull request, unsigned commits across many repositories, and a manual dispatch right after creation ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).

**Defender takeaway:** search the GitHub organisations your teams and suppliers administer for security-themed workflow files (audit, check or Actions security); on a hit revoke the committing credential and rotate everything in the repository's full history. StepSecurity saw requiring approval for workflow runs stop the exfiltration and names branch protection on .github/workflows so workflow changes need pull-request review ([StepSecurity, 2026-10-09](https://www.stepsecurity.io/blog/ghostaction-returns)).
