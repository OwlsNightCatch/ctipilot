Title: Disclosures/CVE-2026-84869 at main · ConnectWise-Advisories/Disclosures

URL Source: https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869

Markdown Content:
September 8, 2026

* * *

## Description

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#description)
A condition in the ScreenConnect client may allow files to be transferred and executed through an active remote session without authorization or Host confirmation in certain circumstances. ScreenConnect servers are not impacted.

* * *

## CVSS 3.1

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#cvss-31)
9.9 (Critical) - CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H

* * *

## Common Weakness Enumeration

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#common-weakness-enumeration)
CWE-862: Missing Authorization

CWE-269: Improper Privilege Management

* * *

## Details

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#details)
Earlier versions of ScreenConnect Client Support and Access sessions contained a client-side file-transfer handling condition in which file-transfer actions could be processed through an active remote session without proper authorization or Host confirmation. Under certain circumstances, this could allow files to be transferred to and executed on the Host client system, including through elevated execution actions. ScreenConnect servers are not impacted. Disabling file-transfer permissions for affected sessions may reduce exposure until the update is applied.

* * *

## Resolution

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#resolution)
### Cloud

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#cloud)
*   No action is required. ScreenConnect servers hosted in the ScreenConnect cloud environment have been updated to remediate this issue.
*   We recommend updating your host clients ([https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_client/Reinstall_the_host_client](https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_client/Reinstall_the_host_client)) and access agents ([https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_page/Reinstall_and_upgrade_an_access_agent](https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_page/Reinstall_and_upgrade_an_access_agent)).

### On-Premise

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#on-premise)
*   Upgrade to ScreenConnect version 26.6.5 or later.

*   For Automate-integrated ScreenConnect deployments: Automate partners are eligible to update their integrated on-premises ScreenConnect installation as long as their Automate Assurance subscription is active. Automate partners should apply the ScreenConnect 26.6.5 update through Automate Product Updates.

*   If your ScreenConnect license is out of maintenance, renew or upgrade the license before installing the latest supported release.

*   If you are unable to apply the update immediately due to maintenance windows or change-freeze policies, you can implement the following as a temporary mitigation to help reduce exposure until the update can be applied. This is not a substitute for installing the security update.

    1.   Navigate to the Administration > Security > Roles section.
    2.   Edit a role, review each session group that has permissions assigned to it, and deselect the TransferFiles permission if it is selected.
    3.   Save your changes. Repeat for each role.

* * *

## Affected Products

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#affected-products)
*   ScreenConnect versions prior to 26.6.5

* * *

## Fixed Version

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#fixed-version)
*   ScreenConnect 26.6.5 and later

* * *

## References

[](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#references)
*   [https://www.cve.org/cverecord?id=CVE-2026-84869](https://www.cve.org/cverecord?id=CVE-2026-84869)
*   [https://www.connectwise.com/company/trust/advisories](https://www.connectwise.com/company/trust/advisories)

Links/Buttons:
- [Skip to content](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#start-of-content)
- [](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#references)
- [Sign in](https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2FConnectWise-Advisories%2FDisclosures%2Ftree%2Fmain%2FCVE-2026-84869)
- [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)
- [GitHub Copilot appDirect agents from issue to merge](https://github.com/features/ai/github-app)
- [MCP RegistryIntegrate external tools](https://github.com/mcp)
- [ActionsAutomate any workflow](https://github.com/features/actions)
- [CodespacesInstant dev environments](https://github.com/features/codespaces)
- [IssuesPlan and track work](https://github.com/features/issues)
- [Code ReviewManage code changes](https://github.com/features/code-review)
- [Code QualityEnforce quality at merge](https://github.com/features/code-quality)
- [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)
- [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)
- [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)
- [Why GitHub](https://github.com/why-github)
- [Documentation](https://docs.github.com/)
- [Blog](https://github.blog/)
- [Changelog](https://github.blog/changelog)
- [Marketplace](https://github.com/marketplace)
- [View all features](https://github.com/features)
- [Enterprises](https://github.com/enterprise)
- [Small and medium teams](https://github.com/team)
- [Startups](https://github.com/enterprise/startups)
- [Nonprofits](https://github.com/solutions/industry/nonprofits)
- [App Modernization](https://github.com/solutions/use-case/app-modernization)
- [DevSecOps](https://github.com/solutions/use-case/devsecops)
- [DevOps](https://github.com/resources/articles?topic=devops)
- [CI/CD](https://github.com/solutions/use-case/ci-cd)
- [View all use cases](https://github.com/solutions/use-case)
- [Healthcare](https://github.com/solutions/industry/healthcare)
- [Financial services](https://github.com/solutions/industry/financial-services)
- [Manufacturing](https://github.com/solutions/industry/manufacturing)
- [Government](https://github.com/solutions/industry/government)
- [View all industries](https://github.com/solutions/industry)
- [View all solutions](https://github.com/solutions)
- [AI](https://github.com/resources/articles?topic=ai)
- [Software Development](https://github.com/resources/articles?topic=software-development)
- [Security](https://github.com/security)
- [View all topics](https://github.com/resources/articles)
- [Customer stories](https://github.com/customer-stories)
- [Events & webinars](https://github.com/resources/events)
- [Ebooks & reports](https://github.com/resources/whitepapers)
- [Business insights](https://github.com/solutions/executive-insights)
- [GitHub Skills](https://skills.github.com/)
- [Customer support](https://support.github.com/)
- [Community forum](https://github.com/orgs/community/discussions)
- [Trust center](https://github.com/trust-center)
- [Partners](https://github.com/partners)
- [View all resources](https://github.com/resources)
- [GitHub SponsorsFund open source developers](https://github.com/open-source/sponsors)
- [Security Lab](https://securitylab.github.com/)
- [Maintainer Community](https://maintainers.github.com/)
- [GitHub Stars](https://stars.github.com/)
- [Archive Program](https://archiveprogram.github.com/)
- [Topics](https://github.com/topics)
- [Trending](https://github.com/trending)
- [Collections](https://github.com/collections)
- [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)
- [Premium SupportEnterprise-grade 24/7 support](https://github.com/enterprise/premium-support)
- [Pricing](https://github.com/pricing)
- [Sign up](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E%2Ffiles%2Fdisambiguate&source=header-repo&source_repo=ConnectWise-Advisories%2FDisclosures)
- [ConnectWise-Advisories](https://github.com/ConnectWise-Advisories)
- [Disclosures](https://github.com/ConnectWise-Advisories/Disclosures/tree/main)
- [Notifications](https://github.com/login?return_to=%2FConnectWise-Advisories%2FDisclosures)
- [Issues 0](https://github.com/ConnectWise-Advisories/Disclosures/issues)
- [Pull requests 0](https://github.com/ConnectWise-Advisories/Disclosures/pulls)
- [Actions](https://github.com/ConnectWise-Advisories/Disclosures/actions)
- [Projects](https://github.com/ConnectWise-Advisories/Disclosures/projects)
- [Security and quality 0](https://github.com/ConnectWise-Advisories/Disclosures/security)
- [Insights](https://github.com/ConnectWise-Advisories/Disclosures/pulse)
- [Add advisory for](https://github.com/ConnectWise-Advisories/Disclosures/commit/5dd36e7881ca62a111985533e68244290158dab3)
- [CVE-2026-84869](https://github.com/advisories/GHSA-rc8v-f46m-jcgm)
- [History](https://github.com/ConnectWise-Advisories/Disclosures/commits/main/CVE-2026-84869)
- [README.md](https://github.com/ConnectWise-Advisories/Disclosures/tree/main/CVE-2026-84869#readme)
- [https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_client/Reinstall_the_host_client](https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_client/Reinstall_the_host_client)
- [https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_page/Reinstall_and_upgrade_an_access_agent](https://docs.connectwise.com/ScreenConnect_Documentation/Get_started/Host_page/Reinstall_and_upgrade_an_access_agent)
- [https://www.cve.org/cverecord?id=CVE-2026-84869](https://www.cve.org/cverecord?id=CVE-2026-84869)
- [https://www.connectwise.com/company/trust/advisories](https://www.connectwise.com/company/trust/advisories)
- [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
- [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
- [Status](https://www.githubstatus.com/)
- [Community](https://github.community/)
- [Contact](https://support.github.com/?tags=dotcom-footer)
