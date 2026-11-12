---
title: Fireworks AI incident
url: https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor-nov9
hostname: notion.com
description: "First published: November 9, 2026 The most current version is available here. On November 6, 2026, one of our vendors, Fireworks AI, notified us of a security incident impacting fewer than 1% of Notion workspaces. For the latest on the Fireworks AI incident, see their official updates here. We have contacted our customers who were affected by the Fireworks incident. If you haven't heard from us, we haven't identified your workspace as affected, and no action is needed right now. Our investigation is ongoing. If we determine that your workspace was impacted, we will contact you directly. What happened and how we addressed it: On the evening of November 2, Fireworks notified us that a small set of data had been accessed by malicious actors. Upon investigation, the dataset included Notion AI synthetic testing data, and no Notion AI customer data was involved. Out of an abundance of caution, by the morning of November 3, we had disconnected our systems from Fireworks, deleted all data in the Fireworks system, and stopped all communication from our systems with Fireworks. On November 6, Fireworks notified us that malicious actors may have accessed potential customer data. Our team immediately began another internal investigation. On November 8, Fireworks confirmed this new dataset for us. Upon analysis of the new data, we discovered that it included Notion AI chat transcripts used for the Insights feature, which for the vast majority of impacted workspaces were unattributable. \"Unattributable\" means the chats weren't labeled with who wrote them or which workspace they came from, and the transcripts did not contain tool call results. Beyond what’s in the chat transcript itself, there’s no information tying the chat back to workspaces, users, or companies. No other Notion features were affected, and we continue to monitor this incident. What is Fireworks AI and how we used them: Fireworks is one of the most used global AI infrastructure platforms powering tens of thousands of customers and used by hundreds of thousands of developers. We used Fireworks for classification jobs to help customers understand their own AI usage through a feature in Notion called Insights, and we used them as a general inference provider to serve open-weight models inside our product. The Insights feature has been disabled as we investigate this incident, and we are no longer serving open-weight models through Fireworks. What we recommend for affected customers: Affected customers are able to retrieve and review the impacted data securely inside their workspace, with instructions sent via email. We also recommend that affected customers treat this data as if it were exposed. If those with affected workspaces have pasted sensitive information, passwords, API keys, or other credentials into Notion AI during the timeframe of the incident, rotate them. We will update this page as we learn more. We take your privacy and the security of your data seriously. Even though this was not a breach of our systems, keeping your data safe is fundamental to using Notion for your life’s work. It is our mission to make sure this never happens again. We will raise the standard for how your data is protected."
sitename: Notion
date: "2026-11-09"
fingerprint: d9d5ba9a9c3d67c9
---
[All security advisories](https://www.notion.com/security/advisories)

# Fireworks AI incident

**First published: November 9, 2026** The most current version is available [here](https://www.notion.com/security/advisories/security-incident-involving-a-third-party-ai-vendor).

On November 6, 2026, one of our vendors, Fireworks AI, notified us of a security incident impacting fewer than 1% of Notion workspaces. For the latest on the Fireworks AI incident, see their [official updates here](https://fireworks.ai/security/bulletins).

We have contacted our customers who were affected by the Fireworks incident. **If you haven't heard from us, we haven't identified your workspace as affected, and no action is needed right now.** Our investigation is ongoing. If we determine that your workspace was impacted, we will contact you directly.

**What happened and how we addressed it**: On the evening of November 2, Fireworks notified us that a small set of data had been accessed by malicious actors. Upon investigation, the dataset included Notion AI synthetic testing data, and no Notion AI customer data was involved. Out of an abundance of caution, by the morning of November 3, we had disconnected our systems from Fireworks, deleted all data in the Fireworks system, and stopped all communication from our systems with Fireworks.

On November 6, Fireworks notified us that malicious actors may have accessed potential customer data. Our team immediately began another internal investigation. On November 8, Fireworks confirmed this new dataset for us.

Upon analysis of the new data, we discovered that it included Notion AI chat transcripts used for the [Insights](https://www.notion.com/help/notion-ai-settings-overview#insights) feature, which for the vast majority of impacted workspaces were unattributable. "Unattributable" means the chats weren't labeled with who wrote them or which workspace they came from, and the transcripts did not contain tool call results. Beyond what’s in the chat transcript itself, there’s no information tying the chat back to workspaces, users, or companies.

No other Notion features were affected, and we continue to monitor this incident.

**What is Fireworks AI and how we used them:** Fireworks is one of the most used global AI infrastructure platforms powering tens of thousands of customers and used by hundreds of thousands of developers. We used Fireworks for classification jobs to help customers understand their own AI usage through a feature in Notion called Insights, and we used them as a general inference provider to serve open-weight models inside our product. The Insights feature has been disabled as we investigate this incident, and we are no longer serving open-weight models through Fireworks.

**What we recommend for affected customers:** Affected customers are able to retrieve and review
the impacted data securely inside their workspace, with instructions sent via email. We also recommend that affected customers treat this data as if it were exposed. If those with affected workspaces have pasted sensitive information, passwords, API keys, or other credentials into Notion AI during the timeframe of the incident, rotate them.

We will update this page as we learn more.

We take your privacy and the security of your data seriously. Even though this was not a breach of our systems, keeping your data safe is fundamental to using Notion for your life’s work. It is our mission to make sure this never happens again. We will raise the standard for how your data is protected.

Originally published
