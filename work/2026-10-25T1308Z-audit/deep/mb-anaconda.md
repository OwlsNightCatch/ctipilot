# extract: served via trafilatura-direct
---
title: Metabase Incident Impacting Kilo Code Data
author: Anaconda Team
url: https://www.anaconda.com/blog/metabase-incident-impacting-kilo-code-data
hostname: anaconda.com
description: Learn more about metabase incident impacting kilo code customer data.
sitename: Anaconda
date: "2026-08-07"
categories: ['Product']
fingerprint: "2c9f7ad20c3fe688"
---
**August 14, 2026 21:30 UTC Update**

We have completed notifications to users affected by [Metabase’s security incident](https://www.metabase.com/blog/security-update). Should further investigation identify any additional Kilo users who may have been affected by the incident, we will contact those individuals directly.

Anaconda offers a process for any user to request deletion of their Kilo account and its data. Submit your request at [kilo.ai/support](http://kilo.ai/support).

Should you have any questions about your Kilo account, please contact us at [\[email protected\]](https://www.anaconda.com/cdn-cgi/l/email-protection#4c2d20293e383f0c2d222d2f2322282d622f2321) and we’ll get back to you as quickly as we can.


August 9, 2026 17:00 UTC Update

While our investigation of [Metabase’s incident](https://www.metabase.com/blog/security-update) continues, we identified a subset of Kilo users or organizations who may have had partial or full prompts or user data (such as name, email address, billing address, and/or location) exposed. At this time we do not have any reason to believe other information (such as the payment card information you provided to Kilo) was exposed. We do not have the ability to confirm whether your data was actually used.

We are in the process of sending notification emails to affected users. We will update this blog to confirm when we have completed notifications.

**We recommend that Kilo users take the following actions, as appropriate to your use of Kilo Code, to protect your data:**

1. **Remain diligent:** Be on alert for phishing/social engineering awareness; and maintain credential hygiene (including auditing, reviewing, and rotating credentials regularly) and spam monitoring.
2. **Examine your data:** You may review your own [session history](https://app.kilo.ai/cloud/sessions) within your Kilo account. For users without registered Kilo accounts, you can [query your own local sessions](http://kilo.ai/docs/code-with-ai/agents/session-history).

We are committed to transparency and sharing action-oriented, helpful information around this incident, as we obtain it, and further updates will be coming. Please watch this blog for additional updates.

If you have questions, please contact us at [\[email protected\]](https://www.anaconda.com/cdn-cgi/l/email-protection#0968656c7b7d7a496867686a66676d68276a6664) and we’ll get back to you as quickly as we can.


August 9, 2026 14:46 UTC Update

We continue to investigate the impact to Kilo users from the [Metabase incident](https://www.metabase.com/blog/security-update).

Our investigation so far has confirmed that the Kilo Slackbot was impacted and a small subset of Kilo users on that feature had their Slack access token exposed. Out of an abundance of caution, we invalidated all Kilo Slackbot authentication tokens for these users. Affected Kilo Slackbot users were contacted.

For more information on reactivating Kilo Slackbot, please see the documentation: [https://kilo.ai/docs/code-with-ai/platforms/slack#setup](https://kilo.ai/docs/code-with-ai/platforms/slack) 



**On August 6, 2026,** Kilo Code (recently acquired by Anaconda) was notified of a security incident at its business intelligence provider, [Metabase](https://www.metabase.com/blog/security-update). Kilo uses Metabase for analyzing data to improve the Kilo user experience. Kilo user information was in the database that was accessed through Metabase. According to logs of the incident provided by Metabase, an unknown actor accessed our customer records in Metabase, which included some Kilo users’ names, email addresses, and other data. Our analysis indicates that this incident did not expose Kilo customer payment information, and exposed data from only some Kilo users (not all).

The Metabase incident affected only users of Kilo Code. Anaconda customers who were not Kilo users were unaffected.

The incident at Metabase occurred over a period of approximately 4 hours on August 2, 2026. Kilo was notified on August 6, 2026. We immediately took steps to contain the incident, and began an internal investigation to fully understand the impact to affected Kilo users, which will remain ongoing. We will be sharing updates as we have them, starting with this blog, and will continue to share updates (including updates to specific affected users) until we complete our investigation.

Anaconda and the Kilo team are committed to transparency and sharing action-oriented, helpful information around this incident, as we obtain it. Please watch this blog for additional updates.

For more detailed information about the Metabase incident, please refer to the [Metabase security alert](https://www.metabase.com/blog/security-update).
