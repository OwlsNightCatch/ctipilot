---
title: Typosquatters Copy Big Brands’ New Domains Within a Day of Registration
author: David Tyler Threat Analyst; Enterprise Security Group; Broadcom
url: https://www.security.com/threat-intelligence/typosquatting-new-brand-domains
hostname: security.com
description: Malicious actors registered one-letter lookalikes of new domains for a series of major brands a day after each real domain appeared. They seemed to be monitoring the specialist registrars corporations use to protect their names.
sitename: SECURITY.COM
date: "2026-11-16"
fingerprint: b34899910601a7c9
language: en
image: https://www.security.com/sites/default/files/styles/blogs_hero_tiny/public/2026-11/Header.jpg.webp?h=f728280d&itok=b7vK-8NA
pagetype: article
filedate: "2026-11-25"
---
# Typosquatters Copy Big Brands’ New Domains Within a Day of Registration

## Malicious actors registered one-letter lookalikes of new domains for a series of major brands a day after each real domain appeared. They seemed to be monitoring the specialist registrars corporations use to protect their names.

- An ongoing typosquatting campaign targeted clients of two brand-protection registrars, CSC (Corporation Service Company) and MarkMonitor.
- Attackers registered 25 lookalike domains, designed to closely resemble authentic domains.
- Every lookalike was registered within the next working day of its authentic counterpart, which suggests the actors monitored new registrations made through brand-protection registrars.
- Most authentic domains appeared to be designed to host campaign sites for well-known brands, including Abbott Laboratories, Bayer, CarMax, McDonald’s, Procter & Gamble and Sanofi, such as patient-savings programs, sweepstakes, claims portals and legal settlements.
- The lookalikes served parked pages, deceptive search portals and brand-themed blogs whose ads routed visitors to scam sites.
- Daily monitoring continues to detect this activity with new lookalikes registered as recently as November 11, 2026.

When a large company registers a new domain through a corporate brand-protection registrar, it signals that the name matters. Recently, malicious actors appear to have turned that signal against the brands themselves. Each time a client of CSC (Corporation Service Company) or MarkMonitor registered a new campaign domain, a one-letter lookalike was registered the next day through a China-based registrar. The pattern repeated 27 times, across domains belonging to Abbott Laboratories, Bayer, CarMax, McDonald’s, Procter & Gamble and Sanofi, among others.

In one case, CarMax registered carmaxclaims\[.\]com and kmxclaims\[.\]com through CSC on August 26. The next day, carmaxclaim\[.\]com and kmxclaim\[.\]com, each one letter shorter, were registered through a registrar in China. The campaign has not stopped. The same pattern appeared again as recently as November 11, 2026.

## **Targeting**

Whois records show that the authentic domains belonged to large, well-known organizations. Most were campaign sites rather than corporate home pages, including patient-savings programs, sweepstakes, rebates, claims portals and legal settlements.

The authentic domains were registered to Abbott Laboratories, Arlo Technology, Bayer, Beam Suntory, Bristol-Myers Squibb, CarMax, Greystar, Immunovant, Ipsos, Kroll, McDonald’s, Procter & Gamble and Sanofi, among others.

These are addresses people type by hand. They appear on printed mailers, television advertisements, pharmacy leaflets and court-ordered settlement notices, and the pages behind them ask visitors for names, addresses, claim numbers or health details. A customer who lands accidentally on a lookalike domain is likely to arrive already expecting to hand over personal data.

## **Registration monitoring**

The operation ran in two halves. The setup was fast and likely automated. The attackers then waited for the brand to launch, publish the address and send customers looking for it.

Registration data is public. Every new .com, .claims or .network domain appears in daily zone files, and a Whois or Registration Data Access Protocol (RDAP) lookup shows which registrar holds it. A domain that arrives through CSC or MarkMonitor is very likely a name a large company cares about. The actors’ tooling was not visible to us, but the evidence is consistent with a simple pipeline that watched new registrations, filtered on brand-protection registrars, generated a one-character variant and registered it before the next day was out.

The lookalikes were registered through Cloud Yuqu LLC (Internet Assigned Numbers Authority (IANA) ID 3824), which registered 18 of the 25, and Chengdu West Dimension Digital Technology Co., Ltd. (IANA ID 1556), which registered the other seven. A domain registered the day before is rarely promoted yet, so each lookalike was in place before the public had seen the real address. By the time a patient-savings card, sweepstakes or settlement notice reached the public, its typo twin may have been waiting for weeks.

## **One-character edits**

Whois records confirm that every lookalike was registered within 24 hours of its authentic counterpart. Figure 3 lists all 27 pairs with the date each authentic domain was created; the letter in red is the one the squatter changed.

The name changes were small. Classic typosquatting techniques such as keyboard-adjacent swaps, homoglyphs or hyphen insertion were absent. Instead, the actors favored edits that kept the name readable and plausible, which a hurried reader would be unlikely to notice.

Of the 27 pairs, 15 dropped a plural or possessive “s” (fyzadasavings became fyzadasaving), six left out a single letter (greystarbenefits became greystarbenfits) and four collapsed a double letter (mywayconnect became mywayconect). That makes 25 plain deletions. Only two pairs did anything else. One added a letter (tradealgotcpasettlement became tradealgotcpassettlement) and one swapped a vowel (yourmsdbenefits became yourmsdbenifits).

The dropped plural “s” was the most common edit. Savings became saving, claims became claim and sweeps became sweep. People often say and type the singular form, which may make these the most effective typos. The actors also folded novelty top-level domains (TLDs) back into .com, likely because users default to it; carmax\[.\]claims became carmaxclaim\[.\]com and mcdonaldsmedia\[.\]network became mcdonaldmedianetwork\[.\]com. A single lookalike could also shadow several authentic domains. For example, carmaxclaim\[.\]com covered both carmax\[.\]claims and carmaxclaims\[.\]com, while yourmsdbenefits\[.\]com drew three separate variants from two registrars.

## **Monetization**

When queried, the lookalikes served one of three kinds of content. Some were parked placeholder pages that earned money from pay-per-click advertising feeds. Others were deceptive search portals whose results led to scam blogs, or brand-themed blogs written around the typosquatted name and packed with ads that routed visitors to scam sites.

This low-grade scam traffic may not be the end goal. Advertising networks of this kind can also be abused for malvertising and credential harvesting, and a domain that serves ads today could serve a fake claims form tomorrow with a single Domain Name System (DNS) or content change. Visitors who reach these domains are already primed to enter personal details. Symantec continues to track the campaign’s scope and persistence.

## 

**Protection**

WebPulse, the collaborative intelligence cloud behind Symantec web security, placed the identified domains in security categories and can catch new variants through shared detection patterns.

For more information on Symantec protection against this campaign, see the [Protection Bulletin](https://www.broadcom.com/support/security-center/protection-bulletin/protection-highlight-one-keystroke-one-day-behind-the-brand).

## 

**Indicators of Compromise**

ontherockrebate\[.\]com

mypgsweep\[.\]com

asrelbisaving\[.\]com

fyzadasaving\[.\]com

ijornisavings\[.\]com

healthspringproducer\[.\]com

arlocareheath\[.\]com

hithebeamsweeps\[.\]com

mywayconect\[.\]com

sunharbosaving\[.\]com

getpgsoffer\[.\]com

celmodpharmacy\[.\]com

mcdonaldmedianetwork\[.\]com

aveirwirless\[.\]com

insulinsavingprogram\[.\]com

ukvaluestudy\[.\]com

greystarbenfits\[.\]com

carmaxclaim\[.\]com

kmxclaim\[.\]com

aildatasettlment\[.\]com

tradealgotcpassettlement\[.\]com

tradealgotcpsettlement\[.\]com

youmsdbenefits\[.\]com

yourmsdbenefit\[.\]com

yourmsdbenifits\[.\]com

myolinhuntsmanbenefit\[.\]com

myolinhuntsmanbenifits\[.\]com
