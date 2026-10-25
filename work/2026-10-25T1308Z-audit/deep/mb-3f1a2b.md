# extract: served via trafilatura-direct
---
title: Metabase Incident Impacting Kilo Code Data
author: Kilo Blog
url: https://blog.kilo.ai/p/metabase-incident-impacting-kilo
hostname: kilo.ai
description: August 14, 2026 23:19 UTC Update
sitename: Kilo Blog
date: "2026-08-07"
fingerprint: a8b76ad204ffa79a
---
August 14, 2026 23:19 UTC Update

We updated the [Anaconda blog](https://www.anaconda.com/metabase-incident-impacting-kilo-code-customer-data) with more information on August 14, 2026 21:30 UTC.

August 9, 2026 14:50 UTC Update

We continue to investigate the impact to Kilo users from the [Metabase incident](https://www.metabase.com/blog/security-update).  

Our investigation so far has confirmed that the Kilo Slackbot was impacted and a small subset of Kilo users on that feature had their Slack access token exposed. Out of an abundance of caution, we invalidated all Kilo Slackbot authentication tokens for these users.  Affected Kilo Slackbot users were contacted.

For more information on reactivating Kilo Slackbot, please see the documentation: [https://kilo.ai/docs/code-with-ai/platforms/slack#setup](https://kilo.ai/docs/code-with-ai/platforms/slack) We updated the

[Anaconda blog](https://www.anaconda.com/metabase-incident-impacting-kilo-code-customer-data)with more information on August 9, 2026 14:46 UTC.

On August 6, 2026, we were notified of a security incident at our business intelligence provider, Metabase. Kilo user information was in the database that was accessed through Metabase. According to logs of the incident provided by [Metabase](https://www.metabase.com/blog/security-update), an unknown actor accessed our customer records in Metabase, which included some Kilo users’ names, email addresses, and other data. Our analysis indicates that this incident did not expose Kilo customer payment information, and exposed data from only some Kilo users (not all).

The incident at Metabase occurred over a period of approximately 4 hours on August 2, 2026. Kilo was notified on August 6, 2026 . We immediately took steps to contain the incident, and began an internal investigation which remains ongoing. We are sharing this update as we have it, and will share others (including updates to specific affected users, as we can) on a followup basis as soon as we have additional results from our investigation. Please watch our blog and website for additional updates.

We (Kilo and Anaconda, which recently acquired Kilo), are committed to transparency and sharing action-oriented, helpful information around this incident, as we obtain it, and further updates will be coming. Please continue to check the [Anaconda blog post](https://www.anaconda.com/metabase-incident-impacting-kilo-code-customer-data) for further updates.

For more detailed information about the Metabase incident, please refer to the [Metabase security alert](https://www.metabase.com/blog/security-update).

[The Anaconda blog](https://www.anaconda.com/metabase-incident-impacting-kilo-code-customer-data) will be updated as our investigation continues.
