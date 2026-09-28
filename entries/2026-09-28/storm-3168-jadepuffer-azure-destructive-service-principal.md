---
schema: 1
kind: threat
title: "Storm-3168 (JADEPUFFER): a sub-eight-minute, automated Azure resource-destruction campaign via a service-principal secret that stayed valid in a GitHub issue's edit history after the visible text was redacted"
headline: "Microsoft ties JADEPUFFER's cloud operations to a service principal that enumerated an Azure tenant for 15+ hours, then destroyed resources in minutes"
summary: >
  Microsoft Security Research documents Azure resource-destruction activity by JADEPUFFER (tracked by Microsoft as
  Storm-3168), the actor Sysdig disclosed in July 2026 as the first documented agentic-ransomware operation. Two
  compromised service principals from one tenant enumerated resources for over 15 hours before a roughly seven-minute
  destructive burst attempted 100+ storage-account deletions (most succeeded, some blocked by resource locks),
  deleted a Key Vault, a Function App and an App Service plan, and attempted to disable Azure Site Recovery and
  Backup protection locks before harvesting storage-account keys. Timing evidence
  points to automated, scripted execution; likely initial access traces to a service-principal secret an employee
  posted in plaintext in a public GitHub issue, whose text was later redacted but which remained retrievable through
  the issue's edit history; Microsoft states this specific credential's use in the activity was not confirmed.
discovered_at: "2026-09-28T04:04:46Z"
updated_at: null
event_date: "2026-09-25"
run_id: 2026-09-28T0404Z-intel
priority: high
immediate_action: null
tags: [ransomware, cloud, organized-crime]
regions: [global]
sectors: [public-sector, technology]
entities: [actor:jadepuffer]
techniques: [T1190, T1078.004, T1526, T1485, T1490]
affected_products: ["Microsoft Azure"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/"
    publisher: "Microsoft Security Blog / Microsoft Security Research"
    date: "2026-09-25"
    role: primary
closed_sources: []
evidence:
  - quote: "The issue was later edited to remove the secret, but the secret remained accessible through the issue's public edit history. Removing or redacting an exposed secret does not invalidate it; credentials exposed in any public internet location should be treated as compromised and promptly revoked or rotated. We could not confirm whether this secret was used for the activity described here."
    publisher: "Microsoft Security Blog"
  - quote: "The timing between the different operations and the division of work using multiple service principals and overlapping token streams from the same service principal strongly indicates automated or scripted execution."
    publisher: "Microsoft Security Blog"
  - quote: "However, we did not observe a ransom note or confirm successful data exfiltration in the activity described here."
    publisher: "Microsoft Security Blog"
verification: single-source
sourcing_note: >
  Microsoft Security Research is the sole assessor of this specific Azure destructive campaign. Sysdig's July 2026
  disclosure is a separate report establishing JADEPUFFER's initial identification and is not independent
  corroboration of this cloud-destruction activity.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Rotate every Azure service-principal client secret, tenant ID or connection string that has ever appeared in a public GitHub issue, PR, commit or gist, including ones since edited or deleted."
updates: []
migrated_from: null
---

Microsoft Security Research has identified Azure resource-destruction activity it attributes to JADEPUFFER, the
threat actor Sysdig disclosed in July 2026 as the first documented agentic-ransomware operation, giving the first
detailed view into the actor's cloud-native operations under Microsoft's own tracking designation Storm-3168
([Microsoft Security Blog, 2026-09-25](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)).
Two compromised service principals belonging to one tenant divided the work: the first spent roughly 15.5 hours
running 300+ read-only enumeration calls across virtual machines, subscriptions and resource groups; the second,
activated 90 minutes later, ran rapid parallel enumeration across two subscriptions in five seconds, then 16 hours
later probed Azure App Service configuration stores and Azure OpenSearch resources, apparently hunting for exposed
credentials. Within one second of a failed key-retrieval attempt against a non-existent storage account, the same
service principal began a roughly seven-minute destructive sequence: 100+ storage-account deletion attempts, mostly
successful, though Azure resource locks and storage-account-level deletion protection blocked deletion for a
subset, plus deletion of a Key Vault, Function App and App Service plan belonging to the same resource group.
Parallel attempts to delete Azure SQL databases failed only because the actor used an unsupported API version for
that resource type. The actor also made repeated, unsuccessful attempts against Azure Site Recovery locks and Azure
Backup protection locks, which Microsoft assesses as potentially intending to impair recovery, before pivoting roughly 30 minutes later to 30+
successful Storage-Account ListKeys credential-collection calls, including against Site-Recovery-related accounts,
for possible future exfiltration.

Timing evidence drives Microsoft's automation assessment: five distinct OAuth tokens were issued for the destructive
and collection work, with two active during the same 70-second window performing different resource-type deletions
in parallel: "the timing between the different operations and the division of work using multiple service
principals and overlapping token streams from the same service principal strongly indicates automated or scripted
execution"
([Microsoft Security Blog, 2026-09-25](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)).
No ransom note or confirmed
data exfiltration was observed in this specific activity, but Microsoft assesses the destruction, recovery-mechanism
targeting and credential harvesting together as consistent with a ransomware/extortion-aligned objective. Microsoft
separately notes ongoing probing from Storm-3168-linked infrastructure since the start of the year against multiple
Azure App Service customers, targeting WordPress-administration, PHP-CGI and LangFlow code-validation endpoints, but
found no App-Service-to-ARM credential path connecting that probing to the tenant affected in this campaign.

Initial access to the compromised service principal is not confirmed: it is "unclear how the service principal was
initially compromised," but its client ID, client secret and tenant ID had previously been posted in plaintext in a
public GitHub issue by an employee of the affected organization. The issue was later edited to remove the visible
secret, but the value remained retrievable through the issue's public edit history; Microsoft states plainly that
"removing or redacting an exposed secret does not invalidate it," while also stating it "could not confirm whether
this secret was used for the activity described here"
([Microsoft Security Blog, 2026-09-25](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/)).

**Detection and hunting.** In Azure Resource Manager audit-log telemetry, the signal is volume and sequencing rather
than any single call: dozens to hundreds of deletion or ListKeys operations against storage accounts, Key Vaults and
Function Apps within minutes, especially when preceded by hours of broad read-only enumeration from the same or a
paired service principal, and when it includes attempts against Site Recovery or Backup protection locks specifically,
a combination with essentially no legitimate operational counterpart. The `python-requests` user agent Microsoft
observed on both compromised principals
([Microsoft Security Blog, 2026-09-25](https://www.microsoft.com/en-us/security/blog/2026/09/25/storm-3168-agentic-driven-cloud-attacks-using-compromised-service-principals/))
is a further, if weak, signal worth correlating with the rest of the sequence rather than alerting on alone.

**Triage:** legitimate infrastructure-as-code teardown and disaster-recovery testing can also delete storage
accounts and Key Vaults in bulk, so the discriminators are the attempt against recovery-protection locks specifically
(a step with no purpose in routine teardown), the credential-harvesting ListKeys sweep that follows the destructive
burst rather than preceding it, and multiple overlapping OAuth tokens performing different destructive operations in
parallel from principals with no prior operational history of this pattern.

**Defender takeaway:** treat any service-principal secret, storage key or connection string that has ever appeared in
a public repository, issue, commit or gist as compromised the moment it is discovered, whatever its current
visibility; Microsoft's own conclusion is that an edit or redaction does not revoke the value. Independent
safeguards that do not rely on the compromised identity's own permissions, such as Azure resource locks and
storage-account deletion protection, were the only thing that stopped part of this campaign's deletions once the
service principal itself was compromised with broad rights.
