---
title: Update for October 30th, 2026 Data Security Incident
url: https://workos.com/security/bulletins/update-for-october-30th-2026-data-security-incident
hostname: workos.com
description: "We've identified the source of the unauthorized access to our internal tool: a security researcher whose AI agent escaped its testing environment. This update shares our findings, the root cause, and the improvements we've made."
sitename: workos.com
date: "2026-11-06"
fingerprint: "7c5ff3875cd75089"
---
# Update for October 30th, 2026 Data Security Incident

We've identified the source of the unauthorized access to our internal tool: a security researcher whose AI agent escaped its testing environment. This update shares our findings, the root cause, and the improvements we've made.

On October 30, 2026, WorkOS identified a high volume of unauthorized requests to an internal tool used by our go-to-market teams. This update follows our [November 2 post](https://workos.com/security/bulletins/october-30th-2026-data-security-incident) and shares what we have learned since.

### Attribution to Security Researcher

After we published our original post, a security researcher contacted our team and accepted responsibility for the unauthorized activity. The researcher was conducting cybersecurity benchmark evaluations using ARTEX when their agent escaped its isolated testing environment. Its interaction with WorkOS was unintended.

At our request, the researcher provided technical evidence, including request details, timestamps, and artifacts left by their activity. Our security team and an independent forensics firm correlated that evidence with our logs and validated the claim. **The researcher confirmed they deleted all WorkOS data obtained by their agent and did not share it with anyone else.**

We appreciate the researcher coming forward, sharing the technical details of their activity, and coordinating with us during our investigation. If you believe you have found a vulnerability in WorkOS, please report it to [security@workos.com](mailto:security@workos.com).

## Response

Our response began on October 30, 2026, when we noticed an unusually high volume of CRM queries and traced them to the internal tool. The timeline below summarizes the unauthorized activity and our response.****

- **October 25**: The first confirmed unauthorized access to the internal tool’s API occurred.
- **October 30**: Records were retrieved in bulk from the internal tool. We removed public access to the tool and began remediation to limit further potential impact
- **October 30–31**: We secured the tool's authentication, revoked or rotated credentials for connected services, and restricted access to all internally developed tools.****
- **November 2**: We shared our initial post and began notifying customers.****
- **November 3–5**: The researcher contacted us and provided evidence. An independent forensics firm validated our attribution. The researcher confirmed that they had deleted the data.

## Impact

Our investigation found that this incident affected only data held in our sales and customer support systems. An independent forensics firm validated these findings.

The exposed information included the following:

- **Business contact details:** Names, email addresses, phone numbers, job titles, and company affiliations held in our customer relationship management (CRM) systems.****
- **Business account and relationship information:** Customer account histories and information about sales and customer-relationship information.****
- **Customer communications:** Summaries and excerpts from sales calls, support discussions, and customer Slack conversations. A limited number of support communications included end-user email addresses.
- **Operational metadata:** Information about customers' use of WorkOS products, including product usage and connection or directory health.

## Root Cause

The affected tool is an internal application our go-to-market teams use to look up and manage account information. It aggregates data from our CRM and our customer support and customer communication systems.

The tool was hosted on a legacy internal tools platform. While we had already transitioned the majority of our internal tooling to an updated platform equipped with stronger baseline controls, this specific internal tool had not yet been migrated and therefore lacked the platform-level safeguards.

Four gaps in the tool’s protections contributed to this incident:

1. **Public Network Exposure**: The tool should not have been reachable from the internet. Overly permissive access controls exposed its API endpoints publicly. As a result, anyone who found the API could send requests to it.****
2. **Weak Credentials**: The API accepted a weak credential intended for local development, which did not meet our security requirements. Our controls did not stop it from being deployed to the tool's production instance. Because the credential was predictable, the agent was able to authenticate after discovering the endpoint.****
3. **Missing Rate Limits**: The API lacked rate limiting or throttling mechanisms. Following authentication, the agent executed rapid requests to extract records in bulk on October 30.****
4. **Telemetry and Detection Gaps**: Our monitoring did not detect the activity soon enough. The agent first accessed the tool on October 25, but we did not identify the unauthorized activity until October 30 — after the bulk retrieval had ended — when an employee noticed unusually high usage of one of the connected systems.

Had these controls been in place, this incident would have been mitigated or prevented entirely. Detailed remediation actions for each of the contributing factors are outlined below.

## Security Improvements

We recognize the trust you place in WorkOS and our responsibility to protect the information you share with us. Below are the improvements we have made and those still in progress, as of November 5, 2026.

### In Progress

- Moving our remaining internal applications from the legacy internal tools platform to the updated platform.
- Adding controls to stop weak or development-only secrets from being deployed to production systems.
- Adding alerts for unusual access patterns and request volumes on internal tools and the systems they connect to.

### Completed

- **October 30:** Removed internet access to the affected tool.****
- **October 30–31:** Removed the weak credential authentication path and revoked or rotated credentials for every connected service.****
- **October 31:** Blocked internet access to all internally developed tools at our network edge.****
- **November 2:** Verified centralized logging of network traffic to internal tools.****
- **November 3:** Began regularly testing our internet-facing systems with ARTEX, the same tool used in this incident. The testing focuses on finding systems that are unnecessarily exposed and credentials that can be guessed.

## Indicators

The table below lists the indicators we identified during our investigation.

Recent reporting from [Wiz](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors), [Google](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks), and [CrowdStrike](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) shows that AI agents built with ARTEX are increasingly used in intrusions. These reports describe similar activity and offer guidance on defending against AI-driven attacks.
