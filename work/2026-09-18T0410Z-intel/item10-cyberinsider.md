---
title: Revolut hackers used infostealer to hijack Italian government emails
author: Amar Ćemanović
url: https://cyberinsider.com/revolut-hackers-used-infostealer-to-hijack-italian-government-emails/
hostname: cyberinsider.com
description: The hackers behind the recent Revolut data breach used infostealer-compromised Italian government email accounts for five months.
sitename: CyberInsider
date: "2026-09-16"
categories: ['News', 'Security']
---
Attackers behind the recent Revolut data exposure allegedly used compromised Italian government email accounts for months to submit fraudulent customer information requests, according to new findings from Duel and Hudson Rock.

The hackers are also reportedly demanding 10,000 Bitcoin, worth about $782 million at the time of the demand, and have threatened to publish additional customer data if Revolut does not pay.

[Duel's investigations team](https://www.hudsonrock.com/blog/revolut-hackers-used-infostealers-for-elaborate-social-engineering) says it established contact with a hacker claiming responsibility for the incident, who described a campaign lasting roughly five months.

According to the attacker, access to government employee accounts came through infostealer malware. Once inside a mailbox, the attacker allegedly added a recovery address, monitored communications continuously, and deleted fraudulent outgoing messages after sending them.

The attacker reportedly downloaded replies from targeted organizations as .eml files and deleted them before the legitimate account owner could see them.

Screenshots published with the investigation show communications with Revolut from addresses using pec.interno.it, a domain associated with Italy's Ministry of the Interior.

This would explain why the fraudulent requests passed normal email authentication checks. Revolut [previously told CyberInsider](https://cyberinsider.com/revolut-handed-customer-data-to-fraudsters-using-a-government-email-domain/) that the requests came from a legitimate government agency domain and appeared authentic based on the technical indicators available to its staff.

The attacker told Duel that the campaign initially involved attempts to use forged court orders, but the focus later shifted to Lithuania-based Revolut Bank UAB and requests framed around European Investigation Orders.

Revolut Bank UAB is the group's licensed European bank and handles customers across the European Economic Area.

Duel says the first successful fraudulent request was sent about five months before the incident became public. The attacker claims similar requests continued during that period without being challenged.

In one alleged case, the hacker submitted an incorrectly prepared document and Revolut staff reportedly explained how to correct it rather than flagging the request as suspicious.

Those claims have not been independently verified, and Revolut has not publicly confirmed the alleged five-month timeline.

Hudson Rock's investigation supports the use of compromised Italian government accounts but questions the attacker's account of how they obtained them.

The cybersecurity firm said it identified approximately 300 compromised pec.interno.it webmail credentials in its cybercrime database, originating from systems previously infected with infostealers.

Hudson Rock therefore assesses that the attackers may have obtained existing stolen credentials rather than directly infecting Italian government employees themselves.

Infostealers commonly collect passwords, browser cookies, session tokens, cryptocurrency wallet data, and other credentials that cybercrime markets later sell or trade.

The incident has also escalated into an extortion campaign.

Hackers claiming responsibility have reportedly published samples of allegedly stolen Revolut customer data in Telegram groups and threatened to release more each day unless the company pays 10,000 BTC.

Separate reporting states that Revolut has contacted around 680 affected customers.

The exposed information may include identity documents, addresses, phone numbers, facial verification images, IBANs, withdrawal records, account statements, and complete transaction histories.

Revolut maintains that its internal systems and customer funds were not compromised and says it blocked the offending address after detecting the activity.

Customers notified about the incident should be particularly cautious of targeted phishing, SIM-swapping attempts, and scams that reference genuine transaction or identity information. Any unexpected contact claiming to come from Revolut, law enforcement, or a government agency should be verified through an independent channel.

## Leave a Reply Cancel reply
