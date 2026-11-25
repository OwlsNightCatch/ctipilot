---
title: Data Processing Incidents on Inference Providers
url: https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/
hostname: openrouter.ai
description: OpenRouter off-boarded three providers, removed 125 endpoints from Zero Data Retention eligibility, and notified potentially affected customers after canary token research on inference providers.
sitename: OpenRouter Blog
date: "2026-11-22"
fingerprint: "3c33f1952cf604dd"
language: en
image: https://openrouter.ai/og.png
pagetype: article
filedate: "2026-11-25"
---
# Data Processing Incidents on Inference Providers

OpenRouter ·

Earlier this week, security [researchers reported](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) that certain inference providers had data compromised or otherwise shown evidence that their data policies were not being upheld. We have been collaborating closely with the researchers and with providers to understand the findings and encourage the providers to address them.

These findings did not show any breach or unauthorized access of OpenRouter. The results of this testing revealed new findings about specific inference providers. A live list of the security announcements we have received from providers is [below](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/#provider-security-announcements).

As the operating layer between customers and a fast-moving ecosystem of models and providers, we take data policy enforcement very seriously. We have taken the following actions:

- Off-boarded three providers from OpenRouter, based on the results of our investigations.
- Removed 125 endpoints from Zero Data Retention (ZDR) eligibility. The removals included providers flagged by researchers, plus additional endpoints that we removed as a precautionary measure.
- Notified all potentially affected customers.

The following work is underway:

- We are adapting the researchers’ testing approach so we can run these checks on an ongoing basis.
- We are conducting technical verification of network paths to identify instances where requests and responses may be being forwarded to third parties.
- We are requiring appropriate assurances and validation before restoring ZDR eligibility to any endpoint removed in this review.

We are grateful for the Dragos report. As we integrate similar testing techniques into OpenRouter, we will keep raising the bar, and providers that want to be on OpenRouter will need to meet it.

## Provider security announcements

- Atlas Cloud: [Our commitment to your security and privacy](https://www.atlascloud.ai/blog/ai-updates/security-and-privacy-commitment)
- GMI Cloud: [Security incident affecting GMI Cloud endpoints on OpenRouter](https://www.gmicloud.ai/en/blog/security-incident-affecting-gmi-cloud-endpoints-on-openrouter)
- MiniMax: [Update on URL access in forwarded API requests](https://www.minimax.io/blog/update-on-url-access-in-forwarded-api-requests-20261124)
- Novita: [Privacy notice regarding MiniMax requests on Novita](https://novita.ai/blog/minimax-requests-privacy-notice/)
- Phala: [November preliminary incident report](https://phala.com/posts/phala-november-preliminary-incident-report)
- Together: [Security event: prompt leakage for requests in June and July of 2026](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026)

*Not all affected providers have posted publicly. We have notified affected users regardless of whether there is a public post. We are encouraging all providers to create incident write-ups and will keep this list updated.*
