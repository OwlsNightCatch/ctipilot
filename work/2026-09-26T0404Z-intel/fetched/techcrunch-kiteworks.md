# extract: served via trafilatura-direct
---
title: Kiteworks urges customers to shut down their servers amid 'imminent' threat of cyberattack | TechCrunch
author: Zack Whittaker
url: https://techcrunch.com/2026/09/25/kiteworks-urges-customers-to-shut-down-their-servers-amid-imminent-threat-of-cyberattack/
hostname: techcrunch.com
description: The tech giant, which allows companies to send large datasets over the internet, said it received a "credible threat" from law enforcement about an imminent attack.
sitename: TechCrunch
date: "2026-09-25"
categories: ['Security']
tags: ['cybersecurity,cyberattack,kiteworks']
---
Technology giant Kiteworks is urging customers to shut down their systems after the company received information that hackers may attempt to target them.

Kiteworks (formerly Accellion), which makes tools for transferring large files and sensitive datasets over the internet, confirmed to TechCrunch that it had notified its customers about a potential threat. The news was [first reported exclusively by German publication Heise](https://www.heise.de/en/news/Imminent-Zero-Day-Attack-KiteWorks-Urges-Customers-to-Shut-Down-Servers-11466375.html), which cited an email that Kiteworks had sent to its customers about an “imminent” attack that could happen as soon as this weekend.

When reached by email on Friday, Kiteworks chief information security officer Frank Balonis told TechCrunch that the company “received credible threat intelligence from law enforcement indicating that a threat actor may attempt to target some Kiteworks systems for customers.”

“Out of an abundance of caution, we notified customers directly and recommended a precautionary shutdown window while we and our law enforcement partners work through the matter,” said Balonis. “We are not aware of any compromise of Kiteworks systems, and this advisory is preventative rather than a response to a confirmed breach.”

Kiteworks did not say, when asked, which law enforcement agency alerted the company or which hacking group may be behind the threat. The FBI declined to comment. Marco DiSandro, a spokesperson for U.S. cybersecurity agency CISA, would not comment on the record when asked by TechCrunch about the Kiteworks alert to customers.

Balonis said that the company has fixed all known vulnerabilities in its latest software release, 9.5.1, which it recommends all customers use.

According to a copy of the email sent to customers on Friday and shared with TechCrunch, the company said it was concerned about the exploitation of vulnerabilities that are currently unknown to Kiteworks. These bugs are known as [zero-day](https://techcrunch.com/2025/04/25/techcrunch-reference-guide-to-security-terminology/#zero-day) flaws because they give the vendor — in this case Kiteworks — no time to fix the flaws before they are exploited.

In the email, Kiteworks urged customers to shut down their systems before the weekend, if not sooner, to “protect against any potential zero-day attacks,” as the company cannot confirm whether there are other potential routes for improper access.

It’s unclear exactly how many customers may be affected, but Kiteworks notes on its website that it has [thousands of customers](https://www.kiteworks.com/customers/) across healthcare, technology, education, automotive, and government, among others. Security researcher Kevin Beaumont pointed to a listing of at least [a thousand internet-facing Kiteworks systems](https://beta.shodan.io/search/facet?query=http.favicon.hash%3A-1215318992&facet=ssl.cert.subject.cn) online today, though the number is likely an overcount of affected customer systems.

One Kiteworks customer who works in healthcare told TechCrunch that they received the alert from Kiteworks and took down their organization’s server immediately. The person, who asked not to be publicly named, said the outage is causing delays and disruption to doctors’ ability to contact their patients.

Kiteworks is no stranger to cyberattacks. Prior to its rebrand from Accellion in late 2021, a vulnerability in its file-transfer application allowed an extortion gang to mass-hack and steal data from [hundreds of organizations](https://techcrunch.com/2021/07/08/the-accellion-data-breach-continues-to-get-messier/) that relied on the product to send customer or internal corporate data over the internet.

The mass hack was part of [a broader hacking campaign targeting file transfer products](https://techcrunch.com/2023/06/02/hackers-launch-another-wave-of-mass-hacks-targeting-company-file-transfer-tools/), with the goal of stealing copies of the data that had been previously sent over the internet but not deleted from the affected servers. The hackers then held the data for ransom, threatening to publicly release customers’ information if the victim organizations did not pay a ransom.

*Do you know more about the threat facing Kiteworks customers? Are you an affected Kiteworks customer? We’d love to hear from you. You can contact this reporter securely on Signal at zackwhittaker.1337, or reach him by email at zack.whittaker@techcrunch.com.*

*Updated with response from FBI and CISA.*
