---
title: GitLab Patches Critical 9.9 AI Gateway Flaw Allowing Command Execution on Self-Hosted Servers
author: The Hacker News
url: https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html
hostname: thehackernews.com
description: GitLab fixed CVE-2026-90970, a 9.9 AI Gateway flaw that could let logged-in Duo Agent Platform users run commands on self-hosted gateways.
sitename: The Hacker News
date: "2026-10-02"
categories: ['Article']
---
A critical flaw in GitLab's AI Gateway could let a logged-in user with Duo Agent Platform access run commands on the gateway under certain conditions, GitLab [said in an advisory](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-19-4-1-released/).

The gateway is the service that connects a GitLab instance to AI models, and only organizations that host their own gateway need to act. The flaw is fixed in gateway versions 19.2.4, 19.3.2, and 19.4.1.

The flaw is tracked as [CVE-2026-90970](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/90xxx/CVE-2026-90970.json). GitLab disclosed it on October 2 and rated it critical, with a CVSS score of 9.9 out of 10.

GitLab runs AI Gateways for its customers and has already fixed them. Customers on GitLab.com, GitLab Dedicated, and self-managed instances that use a GitLab-hosted gateway do not need to act, the company said.

Self-managed customers can instead [host their own gateway](https://docs.gitlab.com/administration/gitlab_duo_self_hosted/), an option GitLab offers for keeping AI request and response data inside the customer's own environment. GitLab strongly recommends that those customers update immediately. It sent that guidance to customers with self-hosted gateways before it published the advisory.

The advisory does not say whether the flaw has been used in attacks. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added an assessment to the CVE record on October 2 that lists exploitation as "none." CISA's other two values cover a public proof of concept and active exploitation.


### Affected and Fixed Versions

The versions below are AI Gateway versions. The gateway is installed as its own Docker image or Helm chart and has its own update steps.

| Gateway version in use | First fixed version | 
|---|---|
| 18.1.6 or later, before 19.2.4 | 19.2.4 | 
| 19.3, before 19.3.2 | 19.3.2 | 
| 19.4, before 19.4.1 | 19.4.1 | 

To [update a Docker deployment](https://docs.gitlab.com/install/install_ai_gateway/#upgrade-the-ai-gateway-docker-image), stop and remove the running container, then pull and run the new image tag, for example self-hosted-v19.4.1-ee. Helm deployments set the new tag in the chart's image setting.

No fixed version is listed below 19.2.4. That leaves every gateway release from 18.1.6 through the 19.1 line inside the affected range.

GitLab's install guide tells administrators to use the gateway image that matches their GitLab minor version. The advisory does not say whether a 19.2.4 gateway works with GitLab 19.1 or earlier, or whether fixes for the older lines are planned.

As of October 2, GitLab's [maintenance policy](https://docs.gitlab.com/policy/maintenance/#maintained-versions) listed 19.4, 19.3, and 19.2 as the GitLab releases that get security fixes. Those are the same three lines that got the gateway fix.

No workaround is listed for gateways that cannot be updated yet. The advisory also gives no way to check whether a gateway was attacked before it was updated.

### What Is Known About the Flaw

The flaw is in the prompt template of a custom flow, according to the advisory's title. A custom flow is an AI-powered workflow that users create on the Duo Agent Platform to automate multi-step tasks.

A logged-in user with Duo Agent Platform access could have used the flaw to "escape the prompt template sandbox via a specially crafted flow configuration," GitLab said. The escape could lead to arbitrary command execution on the gateway.

The conditions the attack needs are not described, and no user role is named beyond Duo Agent Platform access.

A self-hosted gateway holds signing keys for JSON Web Tokens (JWT), which GitLab's install guide says must be treated as sensitive credentials. It also connects to the GitLab instance and to the organization's AI model providers.

GitLab credited the HackerOne user invisiblemeerkat with reporting the flaw.

In February, GitLab [fixed another gateway flaw](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-18-8-1-released/), CVE-2026-1868, which it also rated 9.9. A logged-in user could reach that flaw through a crafted flow definition, and it could lead to denial of service or code execution on the gateway.

Both flaws are template engine weaknesses of the same class, CWE-1336. The new advisory does not mention the February flaw.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
