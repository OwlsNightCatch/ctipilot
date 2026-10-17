---
schema: 1
kind: threat
title: "Storm-3068: a successful self-service password reset became Azure DevOps pipeline abuse and stolen Kubernetes credentials, with no malware or exploit"
headline: "Microsoft DART: one reset-compromised identity became a malicious pipeline that harvested Kubernetes credentials"
summary: >
  Microsoft's incident-response team describes an intrusion by Storm-3068 that began when the actor gained a user
  account through a successful self-service password reset and registered its own authentication methods. It then
  enumerated Azure DevOps, created a malicious pipeline that collected kubeconfig files, added Atera and Chisel
  through modified pipeline scripts, and committed seven stolen kubeconfig files to a repository. Microsoft names
  no victim, sector or date, and no source says how the reset was completed.
discovered_at: "2026-09-30T04:43:00Z"
updated_at: null
event_date: "2026-09-29"
run_id: 2026-09-30T0404Z-intel
priority: notable
immediate_action: null
tags: [cloud, identity]
regions: [global]
sectors: []
entities: ["actor:storm-3068", "product:microsoft-azure-devops"]
techniques: [T1078.004, T1098.005, T1213.003, T1072, T1552.001, T1219, T1572, T1105]
affected_products: ["Microsoft Azure DevOps"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/"
    publisher: "Microsoft Defender Experts (DART)"
    date: "2026-09-29"
    role: primary
  - url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Cyberattacks-Series-Report-Q3-2026.pdf"
    publisher: "Microsoft Defender Experts (DART), Cyberattack Series report Q3 2026"
    date: "2026-09-29"
    role: primary
closed_sources: []
evidence:
  - quote: "The intrusion began with Storm-3068 gaining access to a user account through a self-service password reset process and then taking full control of the identity by registering its own authentication methods."
    publisher: "Microsoft Defender Experts (DART)"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/"
  - quote: "The threat actor added seven stolen kubeconfig files to a repository, providing the credentials needed to access targeted Kubernetes clusters."
    publisher: "Microsoft Defender Experts (DART)"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/"
  - quote: "Using Azure DevOps audit logs and Git version history, investigators reconstructed the next stage of the intrusion."
    publisher: "Microsoft Defender Experts (DART)"
    source_url: "https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/"
verification: single-source
sourcing_note: >
  Single-sourced to Microsoft's own incident-response casework; no independent report of the intrusion exists.
  Microsoft gives no victim, sector, date or attribution, and does not say how the password-reset challenge was
  passed or whether the actor used the stolen cluster credentials.
confidence: medium
references: ["2026-05-20/storm-2949-sspr-to-key-vault-azure-kill-chain", "2026-09-24/microsoft-entra-id-sspr-enumeration-resetspy"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Microsoft's Defender Experts incident-response team (DART) describes a malware-free, exploit-free intrusion by the actor it designates Storm-3068 that began when the actor gained access to a user account through a self-service password reset and took full control of the identity by registering its own authentication methods ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)). Microsoft does not say how the reset challenge was passed. With that persistent access, the actor used legitimate administrative tools and automated scripts to enumerate Azure DevOps repositories, projects, pipelines and deployment environments, then created a malicious pipeline that deployed a kube agent and ran jobs to collect kubeconfig files; that pipeline inherited the compromised account's permissions and was authorized to access more than 50 resources ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)). The actor also modified pipeline scripts to install the Atera remote-management agent and download the Chisel tunneling utility, and ran Chisel to open a reverse tunnel to an external address, which Microsoft describes as an attempt at alternative remote access and at exposing the Kubernetes API server ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)). Investigators rebuilt the sequence from Azure DevOps audit logs and Git version history and found seven stolen kubeconfig files committed to a repository ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)). The full report adds that the actor registered a new MFA method and deleted the account's legitimate MFA methods, started the kube agent by downloading and running a third-party script with several jobs, saved the kubeconfig files into an existing kubeconfigs folder of the target repository (each holding a cluster API endpoint, certificate-authority data and a service-account token), and expanded access in a matter of hours rather than days ([Microsoft Defender Experts, Cyberattack Series report Q3 2026, 2026-09-29](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Cyberattacks-Series-Report-Q3-2026.pdf)).

Where it surfaces: identity-provider audit logs show a completed password reset followed by new authentication-method registrations on the same account ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)), and the full report's attack flow adds deletion of the legitimate methods ([Microsoft Defender Experts, Cyberattack Series report Q3 2026, 2026-09-29](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/security/Cyberattacks-Series-Report-Q3-2026.pdf)), while Microsoft advises watching for repeated resets or resets against many users; DevOps audit logs show one identity enumerating repositories and pipelines and then creating or modifying pipelines; Git history shows pipeline scripts that install a remote-management agent or download a tunneling tool, and kubeconfig files committed to a repository; build-agent egress shows a reverse tunnel to an external address ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)). Microsoft's recommended controls are to keep privileged accounts out of self-service password reset or protect them with phishing-resistant multifactor authentication, enforce branch protection and approvals for code changes, restrict direct commits to critical branches, limit who can create, modify or run pipelines, and apply least privilege across identity, DevOps and cloud ([Microsoft Defender Experts, 2026-09-29](https://www.microsoft.com/en-us/security/blog/2026/09/29/beyond-source-code-a-path-to-the-keys-to-the-kingdom/)).

**Triage:** a user completing a password reset and then registering authentication methods is routine. The sequence that separates this activity is the same identity, right after the reset, enumerating Azure DevOps repositories and pipelines in bulk and then creating or editing a pipeline.

**Defender takeaway:** the DevOps pipeline was the pivot, because a DevOps identity with broad service-connection permissions turns one account into credentials for the clusters its pipelines can reach. Review which identities can create or edit pipelines, and whether any of them can complete a self-service password reset without a phishing-resistant second factor.
