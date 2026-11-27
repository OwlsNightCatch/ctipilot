---
title: "Beyond Branch Protection: Understanding GitHub Attack Paths"
author: Jared Atkinson
url: https://specterops.io/blog/2026/11/25/beyond-branch-protection-understanding-github-attack-paths/
hostname: specterops.io
description: Discover how GitHub permissions, branch protection, and workload identity federation can create enterprise attack paths and expose Microsoft Entra ID.
sitename: SpecterOps
date: "2026-11-25"
categories: ['Blog', 'BloodHound']
fingerprint: "875096911cf5c2cb"
language: en
image: https://specterops.io/wp-content/uploads/sites/3/2026/11/Blog_GitHub-Attack-Paths.png
pagetype: article
filedate: "2026-11-27"
---
# Beyond Branch Protection: Understanding GitHub Attack Paths

**How the compromise of a single employee can have consequences across an entire enterprise.**

## **How Could This Happen?**

In the aftermath of the [1Password security incident](https://1password.com/blog/update-on-nov-2026-security-incident), I’ve seen a considerable amount of discussion questioning how the compromise of a single employee’s GitHub account could have such significant consequences, particularly at a company whose business revolves around security.

What about multifactor authentication? What about branch protection? What about mandatory code review? Surely, a security-conscious organization would have implemented these controls.

These are reasonable questions, but I think they reflect a broader misunderstanding of how modern enterprise environments work and, more specifically, how the security relationships between different technology platforms interact.

Rather than speculate about the specifics of the 1Password incident, I want to demonstrate how similar consequences could arise in an enterprise environment that has implemented many of the security practices we actively encourage organizations to adopt.

To do this, we’ll use K-Nexus Global, a fictional enterprise that we maintain at SpecterOps for research, product development, testing, and demonstrations. Many of the configurations in this environment are modeled after configurations we’ve encountered in actual production environments.

Our objective is to understand how the compromise of an ordinary employee could have consequences that extend well beyond the systems that employee is expected to access.

## **Compromising a GitHub Identity**

When we talk about the compromise of a GitHub account, it’s worth considering what that actually means in a modern enterprise.

Many organizations have integrated GitHub with their corporate identity provider. GitHub Enterprise Managed Users (EMU), for example, allows organizations to provision and manage GitHub identities through an external identity provider, such as Okta or Microsoft Entra ID, and delegate authentication to that provider.

Consequently, the security of a GitHub identity is not necessarily something we can evaluate exclusively within GitHub.

In K-Nexus Global, employees have identities in Active Directory, which are integrated with Okta through mechanisms including password synchronization. Okta, in turn, facilitates authentication to other applications, including GitHub.

The security boundary of an employee’s GitHub identity therefore extends into the corporate identity infrastructure.

There are also security considerations associated with the employee’s workstation. Authentication controls, including MFA, provide protection during the authentication process, but credentials and authenticated sessions remain security-sensitive artifacts. The compromise of an employee’s workstation can therefore have implications for the employee’s corporate identity and the applications to which they have authenticated.

In K-Nexus Global, for example, we can see that EDAVIS@CORP.K-NEXUSGLOBAL.COM has sessions on three Active Directory computers. The security of Elizabeth’s identity, and consequently the identities associated with it in other platforms, depends in part on the security of these computers.

None of this is particularly unique to GitHub. These are characteristics of modern enterprise identity architectures.

For the purposes of this article, we will assume that an adversary has obtained control of an employee’s GitHub identity. The more interesting question is what that identity can actually do.

## **Understanding Effective Permissions in GitHub**

Like most enterprise platforms, GitHub provides several mechanisms for assigning permissions to users.

Users can be assigned roles at the organization level, receive permissions through team membership, inherit permissions through nested teams, and receive role assignments associated with individual repositories.

Understanding the permissions explicitly assigned to a user is therefore not necessarily sufficient to understand their effective permissions.

One particularly interesting configuration is the organization’s default repository permission, which establishes a baseline level of access that organization members receive to applicable repositories.

In K-Nexus Global, the k-nexus-global-infra GitHub organization has its default repository permission configured as write.

This means that organization members receive write permissions to applicable repositories without requiring an explicit repository role assignment.

An administrator reviewing the role assignments associated with a particular repository might see a relatively small number of teams and users. However, when we account for the organization’s default repository permission, we discover a substantially larger population of users with effective write access.

In the following graph, we can see several mechanisms through which users receive permissions to the same repository. Some users receive permissions through team membership, while others receive permissions through their organization role and the organization’s default repository permission. BloodHound models not only the permissions that users possess, but also the relationships through which those permissions are derived.

Whether this represents a meaningful security problem depends on what those repositories are capable of doing.

To understand that, we need to discuss GitHub Actions and workload identity federation.

## **GitHub Repositories as Security Boundaries**

Historically, we have primarily thought about source code management platforms as places where developers store, collaborate on, and manage changes to source code.

GitHub Actions substantially expands the security significance of a GitHub repository.

A repository is no longer simply a place where source code is stored. It is also a context in which computation occurs, credentials become available, and external systems establish trust.

For example, an organization might configure GitHub Actions to interact with resources in AWS or Microsoft Azure. Historically, this might have involved creating credentials in the destination platform and storing them as GitHub Actions secrets.

Today, organizations increasingly accomplish this through workload identity federation.

Workload identity federation allows an external platform to authenticate a workload based on assertions made by GitHub about the context in which that workload is executing.

GitHub Actions uses OpenID Connect (OIDC) to issue tokens containing claims that describe the execution context. These claims can include information about the repository, branch, or deployment environment associated with the workload. The destination platform evaluates these claims against its configured trust conditions to determine whether authentication is permitted.

This eliminates the need to maintain persistent credentials for the external identity in GitHub and represents a meaningful improvement over traditional credential management approaches. However, it also establishes a security relationship between resources in GitHub and identities in the destination platform.

In Microsoft Entra ID, this relationship is represented by a federated identity credential, or FIC. The configuration of the FIC determines which claims Entra is willing to trust.

Depending on the configuration, that trust might encompass an entire repository, a specific branch, or a particular GitHub environment.

In BloodHound, we represent these relationships using the GH\_CanAssumeIdentity edge. The source of this edge reflects the GitHub resource associated with the trust conditions configured on the federated identity credential.

This distinction is important because GitHub provides different mechanisms for governing control over repositories, branches, and environments.

To understand the security of a federated Entra identity, we must understand which GitHub resources Entra trusts and who has effective control over those resources.

## **Branch Protection Is Not Repository Protection**

One of the recurring questions I’ve seen in discussions about the compromise of GitHub accounts is whether the organization had implemented branch protection.

The assumption seems to be that if changes to the main branch require peer review and approval, the compromise of a single developer’s account should not be sufficient to have a significant impact.

This line of reasoning conflates two distinct security boundaries.

Branch protection is primarily concerned with protecting the integrity of branches that match a particular rule. However, many of the security-sensitive capabilities associated with a GitHub repository are scoped to the repository itself rather than to a particular branch.

Repository-level secrets, for example, are not inherently restricted to protected branches. Similarly, a federated identity credential configured to trust an entire repository is not inherently restricted to its protected branches.

Consider the following federated trust configuration from K-Nexus Global:

repo:k-nexus-global-infra/k-nexus-global-infra:\*

The subject (sub) claim in a GitHub-issued OIDC token describes the context in which a workload is executing. In this example, repo: indicates that the subject describes a repository context, the first k-nexus-global-infra identifies the GitHub organization, and the second k-nexus-global-infra identifies the repository within that organization.

The remaining portion of the subject would ordinarily describe a more specific execution context, such as a branch or deployment environment. However, in this example, the federated identity credential uses flexible claims matching with a wildcard (\*), meaning that trust is not restricted to a particular branch or environment within the repository.

An organization might have implemented extensive protections for its main branch while intentionally allowing developers to create other branches as part of their normal development workflow. This is a perfectly reasonable configuration when the objective is to protect the integrity of the main branch.

However, the introduction of repository-level Actions secrets and repository-scoped workload identity federation changes the security implications of repository write access. These capabilities are not inherently restricted to protected branches.

In K-Nexus Global, the organization grants its members write access to repositories by default. The Entra federated identity credential, meanwhile, establishes trust at the repository level.

Because the organization has not restricted the creation of arbitrary branches, the protection of the main branch does not prevent other repository contexts from satisfying the federated trust conditions.

When we combine these relationships with the privileges of the corresponding Entra service principal, we discover that every member of the GitHub organization has an attack path to Tier Zero in Entra. In this context, Tier Zero represents the collection of identities and resources that have effective control over the Entra tenant.

Consider the implications of this configuration. A review of privileged role assignments in Entra would not necessarily identify any of these GitHub users as privileged identities. However, from an attack path perspective, the entire GitHub organization effectively falls within the Entra tenant’s Tier Zero security boundary.

Notice that branch protection does not need to be defeated for this exposure to exist. It can continue to provide exactly the security guarantees it was designed to provide.

The problem is that the scope of the protection does not match the scope of the trust.

## **When Development Has Production Privileges**

An organization that recognizes the risks associated with repository-wide workload identity federation might choose to establish more granular trust relationships.

In K-Nexus Global, we have reproduced another configuration pattern that we’ve encountered frequently in production GitHub environments.

The organization maintains separate branches for development, staging, and production, with a corresponding federated identity credential for each branch.

For example, the production branch is associated with the following subject. This example uses a customized subject format that incorporates both the names and numeric identifiers of the GitHub organization and repository. The final portion, ref:refs/heads/production, restricts trust to the production branch.

repo:k-nexus-global-infra@267752584/kng-release-orchestrator@1421569575:ref:refs/heads/production

At first glance, this appears to establish meaningful separation between the three environments.

During normal operation, the development branch affects development resources, the staging branch affects staging resources, and the production branch affects production resources.

However, this separation exists in the deployment code rather than in the authorization model.

All three federated identity credentials facilitate authentication to the same Entra application. Although each FIC establishes a distinct set of authentication conditions, the privileges available to the workloads are determined by the same service principal.

Consequently, although the code associated with the development branch only references development resources, the privileges available to that workload are not restricted to those resources.

The code describes what the workload does. The authorization model determines what the workload can do.

This distinction becomes particularly important when we examine the branch protection configuration.

The organization has implemented branch protection for production and staging, but not for development. This is understandable from a software development perspective, where the integrity of production code is considered more important than the integrity of development code.

From an identity security perspective, however, all three branches are equally sensitive because they facilitate authentication to the same privileged identity.

The organization has determined the importance of each branch based on the resources its code is intended to manage, rather than the privileges available to workloads executing in that context.

There is an important distinction between establishing a convention that users are expected to follow and implementing a technical control that enforces that convention.

In this example, the organization expects code in the development branch to interact exclusively with development resources. As long as everyone operates in good faith, this configuration appears to achieve the intended separation between development, staging, and production.

However, the organization has not implemented an authorization boundary that enforces this separation. It is relying on users to voluntarily restrict their use of privileges that are considerably broader than those required for their intended responsibilities.

When evaluating the security of a system, we cannot assume that an adversary will operate in accordance with the organization’s intentions. We must instead consider what the system actually permits.

A more appropriate configuration would establish distinct workload identities for development, staging, and production, with the privileges of each identity restricted to the resources it is intended to manage. This would transform an operational convention into a technically enforced security boundary.

## **What Does This Have to Do With Customer Data?**

One of the reasons these relationships are so consequential is that the privileges associated with workload identities can extend well beyond GitHub.

Organizations use GitHub Actions to deploy applications, manage infrastructure, configure identities, administer databases, and perform numerous other operations across their enterprise environments.

The particular technology used to perform these operations is largely inconsequential from an attack path perspective. What matters is the trust relationship between the GitHub execution context and the identity in the destination platform, and the effective privileges of that identity.

In our K-Nexus Global examples, the corresponding Entra service principals possess the ability to grant Microsoft Graph application roles. BloodHound represents this capability using the AZMGGrantAppRoles edge, which reflects the security implications of being able to assign highly privileged application permissions within the Entra tenant.

This is a substantially different security implication from what we might initially associate with write access to a GitHub repository.

Depending on the privileges assigned to a workload identity, the consequences of compromise could extend to production infrastructure, application services, storage systems, databases, or other identities.

Of course, access to infrastructure does not necessarily imply access to all customer data. Application architecture, encryption, key management, and other security boundaries can substantially limit the consequences of an infrastructure compromise.

Nevertheless, understanding the potential consequences requires understanding the complete set of security relationships, rather than evaluating GitHub in isolation.

## **From a Compromised Workstation to an Entra Tenant**

Now that we’ve established the individual relationships, we can begin to understand how they interact.

Consider the following attack path in K-Nexus Global.

The path originates at a corporate workstation and incorporates relationships across four different technology platforms.

Active Directory provides the employee’s corporate identity. Okta facilitates authentication to other applications. GitHub provides the authorization and workload execution context. Entra establishes trust in that context and assigns privileges to the corresponding workload identity.

Each platform is responsible for a portion of the security relationship. The native security and administrative interfaces of these platforms generally provide visibility into their respective portions of the path, rather than the path in its entirety.

This is an important consideration when we evaluate the security posture of an organization.

The Active Directory administrator, the Okta administrator, the GitHub administrator, and the Entra administrator may each have a reasonably good understanding of the security configuration of their respective platforms.

However, none of them necessarily understands the collective security implications of those configurations.

This is how attack paths emerge even in organizations that take security seriously.

## **From an Incident to an Exposure**

When we read about a security incident, we tend to focus on the specific sequence of events that led to the compromise.

We ask how the adversary compromised a particular employee, what privileges that employee possessed, and how those privileges facilitated access to sensitive resources.

These are important questions, but they can obscure a more fundamental problem.

In our previous example, we examined how the compromise of a single corporate workstation could have consequences extending to the organization’s Entra tenant.

However, there is nothing particularly unique about that workstation or employee.

When we reverse our perspective and examine the population of identities and computers that have paths to the same GitHub repository, we discover that numerous other initial compromises could lead to an equivalent outcome.

An incident report describes the path an adversary took. It does not describe the population of paths the adversary could have taken.

From a defensive perspective, this distinction is incredibly important. The objective is not simply to understand how a particular compromise occurred, but to understand the conditions that made that outcome possible.

If we focus exclusively on the employee involved in an incident, we might conclude that the appropriate remediation is to improve the security of that particular identity or workstation.

But if numerous other identities and workstations have paths to the same sensitive resources, that remediation does relatively little to address the underlying problem.

We need to understand where these paths converge and which changes would meaningfully reduce the organization’s overall exposure.

In our K-Nexus Global example, the paths converge on a relatively small number of shared resources and trust relationships. By addressing the configurations responsible for that convergence, we can potentially eliminate exposure originating from numerous identities and workstations through a small number of configuration changes.

This is one of the fundamental advantages of approaching security from an attack path perspective. Rather than attempting to secure every possible starting point independently, we can identify and prioritize changes that reduce exposure across the environment.

## **The Scale of the Problem**

It is worth noting that K-Nexus Global is a relatively small environment.

We have encountered customer environments containing tens of thousands of federated identity credentials associated with GitHub alone.

Enumerating these federated identity credentials is relatively straightforward. Understanding their security implications is not. An inventory of federated identity credentials tells us which GitHub contexts Entra trusts, but it does not tell us who has effective control over those contexts or what privileges that control conveys.

Consider what it would take to manually evaluate the security of these relationships at that scale.

For each federated identity credential, we would need to understand its trust conditions, identify the corresponding GitHub resources, evaluate the security controls governing those resources, calculate the effective permissions of GitHub identities, and understand the privileges of the corresponding workload identity in the destination platform.

We would then need to incorporate the security relationships associated with the corporate identity providers and endpoints that facilitate access to those GitHub identities.

And we would need to continuously reevaluate this information as employees change roles, teams are reorganized, repositories are created, branch protection rules are modified, and new workload identities are provisioned.

The individual relationships are often relatively straightforward to understand. Understanding their collective security implications at enterprise scale is an entirely different problem.

This is particularly challenging because the information necessary to perform this analysis is distributed across platforms that are often administered by different teams.

A GitHub administrator might not know which Entra identities trust a particular repository. An Entra administrator might not know which GitHub users have effective control over the contexts their applications trust.

Both administrators might have a thorough understanding of their respective platforms while remaining unaware of the exposure created by the combination of their configuration decisions.

The problem is not necessarily a lack of security expertise. It is a lack of visibility into the relationships that span these platforms.

## **You Cannot Fix What You Cannot See**

The purpose of this article is not to discourage organizations from using GitHub Actions, branch protection, or workload identity federation.

These are valuable capabilities. Workload identity federation, in particular, addresses significant problems associated with the management of persistent credentials.

The problem is that implementing these capabilities creates security relationships that organizations must understand and manage.

Before an organization can determine whether its workload federation configuration is appropriate, it needs to understand which resources are trusted, who can effectively control those resources, and what privileges that trust conveys.

This is precisely the problem we are addressing with BloodHound.

By modeling the authentication, authorization, and trust relationships across platforms, BloodHound allows organizations to evaluate the security implications of configurations that would otherwise be considered independently.

Rather than simply identifying the existence of a privileged service principal or a permissive GitHub repository, we can understand how those configurations interact, which identities have paths to sensitive resources, and where remediation would have the greatest impact.

This visibility is a prerequisite for effective remediation. Without it, organizations are left making configuration changes based on assumptions about their security implications. With it, they can identify the relationships responsible for their exposure, prioritize changes, and verify that those changes have achieved the intended outcome.

Security-conscious organizations are not immune to attack paths. The complexity of modern enterprise environments makes it extraordinarily difficult to understand the collective consequences of thousands of individually reasonable configuration decisions.

Before an organization can meaningfully reduce its attack path exposure, it must first be able to see it.
