---
title: October 30th, 2026 Data Security Incident
url: https://workos.com/security/bulletins/october-30th-2026-data-security-incident
hostname: workos.com
description: We are investigating unauthorized access to an internal tool used by our sales and customer-facing teams. This update explains our response and observations on AI-assisted attacks.
sitename: workos.com
date: "2026-11-02"
fingerprint: ec1b08875cd3a185
---
# October 30th, 2026 Data Security Incident

We are investigating unauthorized access to an internal tool used by our sales and customer-facing teams. This update explains our response and observations on AI-assisted attacks.

On October 30, 2026, we identified unauthorized access to an internal WorkOS application used by our sales team.

The information accessed included business contact details and summaries of customer communications. We are reviewing the affected records to determine the impact for individual organizations.

Our investigation identified the use of an AI-assisted offensive security framework to automate reconnaissance and exploitation attempts.

## Data involved

The affected internal application provided access to the following categories of information:

- **Business contact details:** Names, email addresses, phone numbers, job titles, and company affiliations held in our customer relationship management (CRM) systems.
- **Business account and relationship information:** Customer account histories and information about sales and customer-relationship information.
- **Customer communications:** Summaries and excerpts from sales calls, support discussions, and customer Slack conversations.
- **Operational metadata:** Information about customers' use of WorkOS products, including product usage and connection or directory health.

## What we are doing

We disabled external access to the affected application and are conducting a broader review of access controls on internal tools. We have retained an independent digital forensics and incident response firm to help establish the full scope of the activity and evaluate its impact. Our security and engineering teams continue to review the evidence and address the issues identified.

## The rise of agentic attacks

Recent reporting from [Wiz](https://www.wiz.io/blog/artex-in-the-wild-storm-0940-expands-targeting-of-it-and-software-vendors), [Google](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks), and [CrowdStrike](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) documents growing use of AI agents in real-world intrusions. These systems can choose follow-up actions based on a target's responses and automate multi-step attack sequences.

This increases the speed and scale of attacks that exploit weaknesses such as exposed applications and stolen credentials. It increases the need for timely remediation and monitoring that can connect suspicious activity across systems. The linked reports above provide additional context on this broader trend.

## Stay alert to phishing and social engineering

Business contact information and details from previous conversations can help an attacker make fraudulent requests look legitimate. Even when a message references a real colleague or support conversation, verify unexpected requests before sharing sensitive information or taking action.

## What happens next

The investigation is ongoing. We will contact affected customers directly and provide further updates as we verify additional information.
