# extract: served via trafilatura-direct
---
title: Revolut Exposed KYC Data After Fraudulent Government Email Passed Security Checks
author: Pierluigi Paganini
url: https://securityaffairs.com/198922/data-breach/revolut-exposed-kyc-data-after-fraudulent-government-email-passed-security-checks.html
hostname: securityaffairs.com
description: Revolut handed over KYC docs, selfies, and BTC transaction histories after a fake gov email with valid domain credentials passed its checks.
sitename: Security Affairs
date: "2026-09-12"
categories: ['Breaking News', 'Data Breach', 'Security']
tags: ['Cybercrime', 'data breach', 'Hacking', 'hacking news', 'information security news', 'IT Information Security', 'KYC', 'Pierluigi Paganini', 'Revolut', 'Security Affairs']
---
Revolut confirmed on September 12, 2026, that it disclosed sensitive customer data to an unauthorized third party after receiving fraudulent information requests sent from an email address operating inside an actual government agency’s domain infrastructure. TechCrunch [reported](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/). The customer notification, which began circulating on September 11, stated that the communication carried valid domain authentication credentials, meaning the email passed the checks that are supposed to confirm a message genuinely comes from a government authority.

*“Revolut received a request for customer information that appeared to come from a legitimate government agency. The request came from an unauthorised email account sent directly using the official government agency’s email domain.” reads the Revolut’s notification. “As the communication carried valid domain authentication credentials, it was fulfilled under the reasonable belief that it was an authentic government agency request.”*

*“The exposed data included customers’ identity and contact details, including their birth date, postal and email addresses, and phone numbers, as well as copies of their identity documents including passports and driver’s licenses, according to a notification emailed to affected customers and reviewed by TechCrunch.” [reported](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/) TechCrunch. “The data may have also included verification selfies, account statements, and transaction histories, the firm said in its notification.”* 

Multiple outlets including CoinDesk and Crypto Times confirm the transaction histories covered Bitcoin. What Revolut handed over is essentially everything a regulated fintech is required to collect for identity verification, in one package, sent to the wrong people.

Below are the details of the handed-over data reported in the notification:

- **Identity details:** full name, date of birth, occupation
- **Contact details:** postal address, email address, and telephone number
- **Document and verification data:** a copy of your identity document (passport and/or driver’s licence) and facial verification image (the selfie you provided for verification). Please note that no biometric facial telemetry data was involved or compromised
- **Financial data:** account statements (including IBAN, account status, opening date, wallet reference number), withdrawal records and full transaction history (including Bitcoin)

This is not a technical breach in the usual sense. No systems were compromised, no malware was used, and Revolut’s servers were not accessed by an outsider. The attacker either created a rogue account within an official government agency’s domain or compromised an existing one, then used that account to submit what appeared to be a legitimate data request. Revolut staff processed it. The company only discovered the fraud afterward, by independently contacting the government agency to verify the request, at which point the agency confirmed it had not made it.

Revolut said that the incident impacted a limited number of customers and immediately contacted them, but did not disclose the scope of the incident.

Revolut also declined to name the government agency involved or specify whether the breach affected a particular country or market. Naming the agency would allow other regulated platforms to search their own legal-request logs for messages from the same mailbox. The silence on that point is a gap in the public record that matters for other fintechs who may have received similar requests.

Crypto security researcher ZachXBT, who posted about Revolut’s notification to affected customers, assessed that the incident appeared to be targeted at high-net-worth users.

If this assessment is correct, this was not a large-scale data theft. It appears to have been a targeted operation aimed at building detailed profiles of wealthy individuals, using their KYC documents and cryptocurrency transaction history linked to their real identities. Combined with IBANs and account statements, this information could be very useful for fraud, impersonation, or extortion.

Revolut says it blocked the email address, alerted the government agency involved, notified law enforcement, and reported the incident to financial regulators. Revolut also says its systems and customer funds were not affected. That may be technically true, but it misses the main point: the attackers did not need to hack Revolut’s systems to get the data.

The breach comes as Revolut seeks greater regulatory credibility, TechCrunch argued. The company recently won conditional U.S. approval to become a national bank, is reportedly considering a $200 billion IPO, and serves 80 million customers worldwide. The incident also highlights weaknesses in fintech data-request processes: relying mainly on email authentication can allow attackers with access to a government domain to bypass checks and obtain sensitive customer data.

**Follow me on Twitter:** **@securityaffairs** **and** **Facebook** **and** **Mastodon**

**(****SecurityAffairs** **– hacking, Revolut)**
