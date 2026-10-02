---
title: "Revolut Data Breach: Inside the Extortion Site"
author: KELA Cyber Intelligence Center
url: https://www.kelacyber.com/blog/revolut-data-breach/
hostname: kelacyber.com
description: KELA traced the Revolut data breach extortion site to free public hosting built in 6.5 hours, with deleted files recoverable from its public commit history.
sitename: Kelacyber
date: "2026-09-14"
---
# Revolut Data Breach: Tracing the Extortion Site Infrastructure

Revolut confirmed on 12 September 2026 that it disclosed customer files to a third party who submitted fraudulent information requests from a legitimate government agency email domain. A threat actor then published an extortion site demanding payment. KELA analyzed that site's public infrastructure and found it was assembled in roughly six and a half hours on free public hosting, leaving a public repository, commit metadata, and recoverable deleted files behind.

Updated September 15, 2026

## Background

Revolut recently suffered a data [breach](https://techcrunch.com/2026/09/12/revolut-confirms-customer-data-breach-through-fake-government-requests/) resulting from a sophisticated social engineering scheme rather than a direct database hack. Fraudsters exploited a legitimate government email domain that passed Revolut’s technical authentication checks (SPF/DKIM/DMARC) to send deceptive information requests. Mistaking these demands for authentic official orders, Revolut’s compliance and legal team manually released sensitive files for a limited group of users, exposing KYC documents, identity details, bank statements, and cryptocurrency transaction histories.

In addition, an initial Telegram channel claiming the breach named “iamnotavillain” was taken down shortly after it appeared but was later revived with a dedicated website (imnotavillain[.]xyz). Around the same time, another Telegram channel operating under a different name with a different website, "Revolut Smilik", emerged and claimed responsibility for the breach. However, the actor “iamnotavillain” later stated that an impersonator and scammer who had previously worked with them obtained a small sample of the data they had provided and subsequently began falsely claiming responsibility for the breach.

*One of the posts as seen on the actor’s Telegram channel*

## The Website

The website is a PR site set up by a threat actor claiming to hold a Revolut customer database. It opens with a notice asserting that Revolut was warned about the data and ignored the report, and that the actor holds the full set of KYC documents, verification selfies, addresses, phone numbers, emails, bank account identifiers, and both fiat and crypto transaction records. The notice appears to have been created using a default HTML based template in Claude chats, indicating the use of standard LLM models by criminals.

Three screenshots presented on the website are embedded as claimed proof, one as evidence of Revolut sending data in response to a request, and a separate section accuses the bank of moving customer records across jurisdictions. The site closes with a press pitch inviting journalists to get Revolut on record, and a contact block offering Telegram and a Session ID, explicitly addressed to Revolut staff, press, and affected users alike.

The proof screenshots identify the channel used: correspondence with Revolut's Italian certified email address operated through InfoCert, alongside courtorders@revolut.com. The exchange shows Revolut requesting destruction of the documents it had sent, stating the accounts fall under a different jurisdiction bound by banking. A further screenshot shows nineteen "Document Revolut" archives and a folder of 326 MB containing 688 files.

*The Website’s main page*

*Subdomains of the threat actor’s website*

## OSINT Traces

KELA investigated the website infrastructure and determined that it is a static page on GitHub Pages with domain and DNS at GoDaddy. An additional finding is “pay.” subdomain, which resolves through the GoDaddy Payments platform. That platform requires in most cases full KYC, a TIN, and a US bank account, so GoDaddy likely holds a legal identity for the operator or for a stolen one.

An initial investigation of the webpage by KELA identified the “btres9kijob[.]github.io” domain, which was indexed via a GitHub Pages custom-domain redirect. However, further examination found the associated GitHub profile to be empty, although it may have been one of the threat actor's former GitHub accounts. Further investigation of the website's domain identified another GitHub Pages site associated with a different username. The account, registered in July 2026, was confirmed to host the website's files, with the associated repository containing both the site's CNAME and index.html files.

*The actor’s GitHub profile and repository*

Moreover, although the account was created on 4 July 2026, it shows no public activity until the day of the incident, suggesting either a deliberately aged account or one obtained from a third party. The account's updated_at timestamp is 14 September 2026 at 13:39 UTC, approximately thirty minutes before the repository was created at 14:09 UTC, indicating that some change was made to the account profile immediately prior to the operation. GitHub does not disclose which field was modified, so this should not be read as confirmation of a username or email change specifically.

Analyzing the repository, a CNAME file with the domain and an index.html matching the live site's eTag were found. All commits were authored using an Outlook.com email address, with one commit recorded from a UTC-07:00 timezone, consistent with locations in western Canada and the western United States. This repository was built in roughly six and a half hours on 14 September 2026, entirely via GitHub's web UI. The wider infrastructure predates it: the domain's TLS certificate was issued at 04:38 UTC that day, meaning the domain was already bound to a GitHub Pages site almost ten hours earlier, consistent with the btres9kijob observation and indicating a possibly an account switch mid operation.

*Commit history reveal a potential Email address*

Git history, as seen by KELA, also preserves material the operator discarded. Earlier index.html revisions reference filenames since removed (proof.jpg, jurisdiction.jpg, and an "imagers/" folder typo), and a deleted Screenshot_35.jpg and logo.jpg were both recoverable. Operator fingerprints run throughout: the "screenshit" misspelling, commit messages like "123" and "Update image sources in index.html123", and the repo name's own "123" suffix. EXIF was stripped from all images, leaving only a Chromium signature.

The Outlook.com email address appears to be associated with a Microsoft account registered under the name “Izael Wong” in Brazil (which is likely an alias), the GitHub account, and an Etsy account under the name "Calvin." Notably, the Etsy account was registered at 22:18 on 4 July 2026, one minute before the GitHub account at 22:19, indicating the accounts were opened in a single sitting. The Microsoft account is linked to the same address but carries no registration timestamp. However, it has yet to be determined whether the GitHub account and email address are genuinely associated with the threat actor, were compromised and subsequently used by him, or whether the names identified across these accounts are simply aliases used by the same individual.

*The actor was observed by KELA editing the website in real time*

## **Bottom Line**

The operator's tradecraft is markedly weaker than the operation itself. The extortion site was built on free public infrastructure over a single day, leaving a public repository, and a possibly real email address embedded in commit metadata, with discarded files recoverable from version history. Three linked accounts were opened in a single sitting in July 2026 and left dormant until the day of the operation. Together these leave several viable routes to identification, though it remains undetermined whether the accounts belong to the actor, were compromised, or are aliases. The gap between a well-executed intrusion and careless supporting infrastructure is the most actionable characteristic of this campaign.

Revolut Breach FAQ

What happened in the Revolut data breach?

Revolut confirmed on 12 September 2026 that it disclosed customer information to an unauthorized third party. The company described a sophisticated external impersonation scam in which the third party used a legitimate government agency domain email to submit fraudulent requests for information. Revolut has not named the agency or the markets involved, and has described the number of affected customers only as limited. A customer notification reviewed by TechCrunch listed identity and contact details and copies of identity documents including passports and driver's licenses, and stated that verification selfies, account statements, and transaction histories may also have been disclosed.

Were Revolut's systems hacked?

No. Revolut has stated that its systems and customer funds were unaffected. The data left the company through its own legal and information request intake process, which handled the fraudulent requests as though they were authentic. The takeaway is that no perimeter control would have caught this, because nothing was bypassed: the process worked exactly as designed and the input was forged.

What did KELA find on the extortion site?

KELA analyzed the site's publicly available infrastructure. The site is a static page on free public hosting, with domain and DNS at a commercial registrar and a payments subdomain resolving through that registrar's payment platform. It was assembled in roughly six and a half hours on 14 September 2026, entirely through a web browser. The operator left the source repository public. Commit metadata carries an email address, two deleted image files remain recoverable from version history, and earlier page revisions reference filenames removed before launch.
