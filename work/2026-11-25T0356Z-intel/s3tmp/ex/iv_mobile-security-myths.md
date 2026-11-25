---
title: "5 Mobile Security Myths That Leave Enterprises Exposed"
url: https://www.iverify.com/blog/mobile-security-myths
hostname: iverify.com
description: Five common mobile security myths, from "just block mobile access" to "MDM keeps us safe," and what the evidence shows about each one.
sitename: iVerify
date: "2026-10-15"
fingerprint: be251d979863b3e9
language: en
image: https://framerusercontent.com/images/MkcTsUW8XCvjPq17x7u0LofZ36k.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
Most security leaders we talk to have thought hard about mobile risk. Even so, a few assumptions keep showing up in those conversations, and they shape how programs budget for and govern the phone. Some of them hold up. Plenty don't, especially once you check them against what attackers have actually done in the past year.

Below are five of the most common, along with what the data shows about each one.

## **TL;DR**

- Blocking work on phones doesn't remove the phone from the attack path. Social engineering campaigns go after employees' phones directly, whether or not those phones are managed.
- Advanced iOS exploit kits no longer stay with nation-state operators. Coruna started as a commercial surveillance tool and was used by financially motivated criminals within a year; in August 2026, a [new DarkSword variant](https://www.linkedin.com/feed/update/urn:li:activity:7514074056074354688) reached a financial institution employee through a malicious ad.
- MDM tells you how a device is configured. It can't tell you whether the device has been compromised.
- Zero trust depends on device posture. Strong identity controls work best when they have a trustworthy signal about the phone making the request.
- Containing the blast radius and closing exposure quickly work together. 29% of known exploited vulnerabilities in 2025 were exploited on or before disclosure day.

## **Myth 1: The safest mobile strategy is to keep work off the phone**

**Reality:** Restricting phones to email and chat reduces what an attacker can reach through a compromised device, but it does nothing to stop attackers from using the phone to reach your employees, and that is how many of the recent identity breaches began.

The pattern shows up clearly in an August 2026 incident at ReliaQuest, documented in a [Health-ISAC report](https://www.aha.org/h-isac-white-reports/2026-08-24-h-isac-tlp-white-cyber-incidents-shinyhunters-linked-social-engineering-and-identity-targeting). Actors linked to ShinyHunters called several employees, posing as internal security staff, and directed them to a lookalike single sign-on page. One employee entered their credentials there and then approved the [MFA](https://www.iverify.com/blog/why-mfa-alone-no-longer-protects-the-enterprise) push on their mobile device, which gave the attacker an authenticated session. Device-trust controls kept the attacker from getting any further, but the phone was still the way in, and it would have been whatever that phone was allowed to access. Campaigns like this are also becoming far more common, with [CrowdStrike's 2025 Global Threat Report](https://securitymagazine.com/articles/101439-vishing-attacks-increased-by-442-in-the-second-half-of-2024) recording a 442% increase in voice phishing between the first and second halves of 2024.

Locking phones down also carries a cost that grows over time. When a phone can only reach email and chat, anything beyond reading and replying has to wait until the employee is back at a laptop, whether that's approving an expense, opening a file in a customer system, or checking a dashboard during an incident. For people whose jobs keep them away from a desk, such as clinicians, field engineers, and branch staff, a large part of the workday happens on a device the organization has decided not to trust. The share of work done on phones is also growing. In [Verizon's 2025 Mobile Security Index](https://www.securityweek.com/mobile-security-verizon-says-attacks-soar-ai-powered-threats-raise-alarm/), nearly all organizations said their employees regularly use generative AI tools on their phones.

When the approved route is too narrow, employees usually find another one, and the work moves somewhere the security team can't see. In [CyberArk's 2024 Employee Risk Survey](https://www.businesswire.com/news/home/20241203942566/en) of more than 14,000 employees, 65% said they often bypass cybersecurity policies to make their lives easier, and 80% said they access workplace applications from personal devices. Forwarding a document to a personal inbox or finishing a task in a consumer app takes seconds, and once the data leaves the managed channel, nobody has visibility into where it goes. A more durable approach starts by asking what you would need to know about a phone before you could trust it with more access, which is a question the rest of these myths keep coming back to.

## **Myth 2: We're not an interesting enough target for advanced mobile attacks**

**Reality:** Advanced mobile exploits used to stay with nation-state operators who spent them carefully on high-value targets, but that is no longer a safe assumption, because the same tools now pass into criminal hands and get used against anyone they can reach.

Coruna shows how quickly that can happen. [Google's Threat Intelligence Group](https://thehackernews.com/2026/03/coruna-ios-exploit-kit-uses-23-exploits.html) first captured parts of the kit in early 2025, when it was being used by a customer of a commercial surveillance company. By July 2025, a suspected Russian espionage group was delivering it through compromised legitimate Ukrainian websites, though only to iPhone users in particular locations. By December, a financially motivated actor was serving it from fake Chinese finance sites with no geographic filtering and using it to install a loader that targets cryptocurrency wallet data. In under a year, a kit built for targeted surveillance had become a tool for opportunistic theft, and iVerify described the campaign as the [first observed mass exploitation of iOS devices](https://www.iverify.com/press-releases/first-known-mass-ios-attack).

DarkSword has taken a similar path. In August 2026, an employee at a financial institution clicked a malicious ad and ended up with spyware on their iPhone. Nobody had singled them out, since the ad led to a watering hole serving a new DarkSword variant that iVerify's threat intelligence team has since named [P7 DarkSword](https://www.iverify.com/blog/darksword-variant-threat-research). The institution had Mobile EDR in place, so iVerify alerted its SOC before the attacker could move from the phone into the network. Someone put skilled development work into an exploit chain Apple has already patched, which shows how much money there still is in known vulnerabilities on phones that haven't updated. That also points to a practical defense. Mobile EDR shows which iOS version every phone is running, so a security team can cut off corporate network access for any phone still on a version vulnerable to DarkSword or another known exploit, as long as the fixed version is supported in their environment, and restore it once the employee updates.

Social engineering has moved in the same direction. Attackers are looking for access, so any employee with enterprise credentials and an MFA app is worth a phone call, whatever their job title. The phishing kits used in this year's healthcare campaigns let attackers [change page content and display authentication prompts in real time](https://bleepingcomputer.com/news/security/health-isac-warns-of-rising-shinyhunters-data-theft-attacks-on-healthcare) while keeping the victim on the line, making it cheap to work through a long list of targets. An organization doesn't have to stand out to end up on that list.

## **Myth 3: Our MDM keeps our phones secure**

**Reality:** MDM is a management tool that handles inventory, configuration policy, and remote wipe, and while those controls are worth having, they tell you how a device is set up rather than whether it has been compromised.

The limitation comes from how [MDM](https://www.iverify.com/videos/why-mdm-not-suitable-enterprise-security-solution) works. It communicates with the phone through device management APIs, which report settings and compliance state but offer no view of process-level activity while an attack is underway. A fully enrolled iPhone running an exploit chain like Coruna would therefore look exactly like a clean one in the MDM console. Security teams already accept this distinction on laptops, where nobody treats configuration management as a substitute for EDR, and [Mobile EDR](https://www.iverify.com/resources/iverify-enterprise-mobile-edr-overview) fills the same role on phones by collecting OS-level telemetry and analyzing it for signs of compromise.

## **Myth 4: If our identity controls are strong, a compromised phone doesn't matter**

**Reality:** Phishing-resistant MFA and zero standing access work by making a stolen credential useless on its own. They're still the right priorities, but a hacked phone gets around them. The attacker can use apps that are already signed in, read the messages and one-time codes that MFA depends on, and pull stored secrets straight off the device. [DarkSword](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword) and its P7 variant both extract keychain data, where iOS stores saved passwords and encryption keys. To the identity provider, the activity that follows looks like a legitimate user on a trusted device.

[Zero trust](https://www.iverify.com/blog/zero-trust-mobile-security) was designed with this problem in mind. Its premise is that no user or device is trusted by default, so every access request has to be checked against both who is asking and the state of the device they're asking from. The US National Institute of Standards and Technology's reference architecture for zero trust, [NIST SP 800-207](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf), makes device health part of every access decision and says organizations should monitor "the integrity and security posture of all owned and associated assets." On laptops, EDR provides that device signal. Most personal phones provide none, so the identity system can't tell a healthy phone from a compromised one, leaving a gap in the zero trust model exactly where employees log in most.

Closing that gap is what lets strong identity controls hold up on mobile. Mobile EDR can pass a compromise signal from the phone to identity providers such as [Okta and Microsoft Entra ID](https://www.iverify.com/integrations), so the same access policies that already check laptops can check phones too. A phone showing signs of compromise can then lose access to enterprise systems before an attacker can use the sessions and secrets stored on it. That protection matters more as employees connect their phones to AI assistants and agents that can take actions inside those systems, because a compromised phone with that kind of access can do far more damage than one limited to email.

## **Myth 5: Patching speed doesn't matter if we've limited the blast radius**

**Reality:** Limiting what an attacker can do after getting in is a sound strategy, and racing attackers on patch speed alone is a contest defenders tend to lose; but on mobile, the fixes often already exist, and the exposure comes from not knowing which devices are missing them.

The window between disclosure and exploitation keeps shrinking. [VulnCheck found](https://www.infosecurity-magazine.com/news/zeroday-exploits-surge-vulncheck) that 28.96% of known exploited vulnerabilities in 2025 were exploited before or on the day they were disclosed, up from 23.6% in 2024, which means that for a growing share of flaws there is no patching window at all. That is a strong argument for containment. Mobile exploitation has worked differently over the past year, though. Coruna and DarkSword relied on vulnerabilities Apple had already fixed, and CISA added three of the Coruna CVEs to its Known Exploited Vulnerabilities catalog on March 5, 2026, so the devices at risk were simply the ones still running old versions. An organization that chooses not to enforce OS updates on personal phones still needs to know which of those phones are vulnerable, so that access policy can respond to them.

## **What the myths have in common**

Each of these assumptions treats the phone as something to restrict or manage, which made sense when phones mostly handled email. Today the phone carries employees' identities, approves their MFA prompts, and increasingly does their work, so it needs the detection and posture checks that laptops already get. Programs that close that gap can extend mobile access with confidence, and they can withdraw it quickly when a device is compromised.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
