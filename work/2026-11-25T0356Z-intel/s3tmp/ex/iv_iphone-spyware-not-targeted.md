---
title: iPhone Spyware Doesn’t Pick Its Targets Anymore
url: https://www.iverify.com/blog/iphone-spyware-not-targeted
hostname: iverify.com
description: Mercenary spyware used to target a chosen few. Leaked iOS exploit kits now reach anyone on a vulnerable iPhone through compromised sites and ads.
sitename: iVerify
date: "2026-11-13"
fingerprint: "3da489859c06bbcb"
language: en
image: https://framerusercontent.com/images/llKy6Am3JABlreSwDJ0wZYsSAs.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
Ask a security leader why phones sit outside their detection program and a common answer is some version of "we're not interesting enough to be targeted." Their company isn't a defense contractor or a ministry, their staff aren't dissidents or journalists, and so they think people who buy iPhone spyware have no reason to come after them. For most of the past decade that reasoning held up, because a working iOS exploit chain was too expensive to be used on “just anyone”. In 2026, that’s no longer true. Government-grade exploit kits leaked, criminal groups picked them up, and they are now delivered through compromised websites and ads to anyone running a vulnerable version of iOS, whether or not anyone has heard of them.

## **TL;DR**

- "We're not interesting enough to be targeted" assumes attackers still choose their victims. With today's leaked iOS exploit kits, most of them don't.
- Coruna and DarkSword, two kits built for government customers, reached criminal hands within weeks of being exposed in March 2026.
- Attackers deliver them through compromised websites and online ads, so the victim is whoever visits or scrolls past on a vulnerable iOS version.
- In iVerify's 2026 data, three in four detections were criminal rather than state-sponsored, every enterprise detection from criminal actors involved a rank-and-file employee, and none of the devices under Coruna or DarkSword attack received an Apple threat notification.
- Exposure now depends on which iOS version a phone runs and whether anyone would see a compromise, so closing the patch gap and getting detection onto the device matter far more than a company's profile.

## **Why "we're not interesting enough" used to be a safe bet**

Mercenary spyware was built around a target list. A government customer chose a person, paid a vendor for access, and accepted the risk of burning an expensive exploit to reach them. Each new iPhone mitigation raised the cost of a working chain, and researchers who could build one began [selling their work for millions of dollars](https://www.iverify.com/blog/apple-ios-exploit-history) instead of publishing it. Scarcity did the rest. Exploits were used sparingly because getting caught meant losing them, and most people with an iPhone could reasonably assume nobody would spend one on them.

Apple still describes the threat this way. Its [guidance on threat notifications](https://support.apple.com/en-us/102174) says mercenary spyware attacks cost "millions of dollars" and target "a very small number of specific individuals," such as journalists, activists, politicians and diplomats. Until this year, that matched what iVerify saw on real devices where earlier detections were overwhelmingly Pegasus, an expensive tool aimed at a person someone had picked. For an enterprise outside government, defense and the media, "we're not interesting enough" was a fair reading of how that market worked.

## **How leaked kits spread in 2026**

That model broke in March. Google's Threat Intelligence Group and iVerify disclosed [Coruna](https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit) on March 3, 2026, describing "five full iOS exploit chains and a total of 23 exploits" covering iOS 13.0 through 17.2.1. Fifteen days later, GTIG, Lookout and iVerify disclosed DarkSword, a JavaScript exploit chain and infostealer covering iOS 18.4 through 18.7 that had been used by commercial surveillance vendors and suspected state actors. Five days after that, a newer version of DarkSword [appeared on GitHub](https://techcrunch.com/2026/03/23/someone-has-publicly-leaked-an-exploit-kit-that-can-hack-millions-of-iphones/).

The vulnerabilities in DarkSword had already been patched, so the leak mattered for what came with them. Turning a bug into a working chain takes private techniques for bypassing pointer authentication, escaping the sandbox and gaining reliable access to the operating system. A handful of companies and governments had held those techniques closely. Once DarkSword's code was public, anyone could study and reuse them, and many did. iVerify has since tracked [multiple clusters of DarkSword variants](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword), along with operators who combine both kits on a single page, a deployment iVerify calls DarkCoruna, so that one visit can attack a wider range of iOS versions. By September, live and historic Coruna attacks against devices on vulnerable iOS versions had reached 5% of devices, up from 1.5% in August.

AI is speeding the cycle up. Apple's latest iOS security update fixed almost 120 vulnerabilities, a sharp jump from the release before it, and iVerify's 2026 Advanced Mobile Threat Report finds that AI is accelerating how quickly flaws are found and turned into attacks. Not every AI-built attack works, and much of that code is low quality, but some of it does. Every fix also tells attackers where to look, and the leaked techniques shorten the distance from a published patch to a working attack on phones that haven't installed it.

## **Watering holes and ads put every vulnerable iPhone in range**

Once an exploit chain is cheap or free, nobody has a reason to ration it, and the people running Coruna and DarkSword haven't. GTIG found Coruna hidden in iFrames on compromised Ukrainian websites and later on "a very large set of fake Chinese websites mostly related to finance." iVerify's [early analysis of DarkSword](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained) found it on a Ukrainian news site and a government site, served to every visitor from a Ukrainian IP address whose iPhone ran a vulnerable version. In a watering hole attack like these, the target list is simply everyone who visits.

Online ads go further, because ad platforms let buyers target by device, OS version, location and interests, so an attacker can show an exploit only to the iPhones it works on. Citizen Lab’s [AdFection research](https://bleepingcomputer.com/news/security/zero-click-attacks-used-targeted-ads-to-deliver-candiru-spyware) showed the technique in mercenary spyware, and criminals now use it at scale. iVerify observed a “half-click” attack, where the exploit starts as soon as the ad loads, from an ad served on Instagram while the user was simply scrolling. In August, iVerify detected a new DarkSword fork, [P7](https://www.iverify.com/blog/darksword-variant-threat-research), on the iPhone of an employee at a financial institution. Nobody had singled the employee out; they were simply infected after clicking a malicious ad. Someone invested that effort in an exploit chain Apple had already patched, which shows how much money attackers expect to make from phones that haven't updated.

None of these methods involve deciding who is worth attacking, so an enterprise can be of no interest to the people running them and still have dozens of employees in range.

## **Who actually gets hit**

The 2026 Advanced Mobile Threat Report puts numbers on the shift. Across the consumer iPhones iVerify monitors, the iOS spyware infection rate is 1.07 per 1,000 devices, or at least one in 900, which iVerify reports as the conservative end of its estimate. Enterprise customers now see close to one confirmed attack every week.

The people being hit also look nothing like the profile behind "we're not interesting enough." In every enterprise case of Coruna and DarkSword detections iVerify has recorded, the device belonged to a rank-and-file employee below managing director level, and in none of them did iVerify find evidence that an executive was targeted.

The cases outside the enterprise follow the same pattern. In Ottawa, attackers targeted the children of a bus driver and a stay-at-home mom with spyware, and in Australia they targeted a limousine driver. None of these cases involved high-risk travel to places like China. The victims were at their desks, in their workplaces and in their homes.

These infections also arrived without warning. To iVerify's knowledge, none of the devices it confirmed as infected with Coruna or DarkSword received an Apple threat notification, which makes sense given that Apple designs those notifications for people who "may have been individually targeted." A security team that waits for one before investigating would never have heard about any of these cases.

## **Being uninteresting is no longer a defense**

"We're not interesting enough to be targeted" rested on the idea that attackers had to choose, and that choosing was expensive. What determines an organization's exposure now is how many of its employees' phones run a vulnerable iOS version, and whether anyone would notice if one of them were compromised.

**How to defend phones nobody chose to target**

Attackers are exploiting the gap between a patch being released and a patch being installed, so the first step is to set a minimum iOS version for access to corporate apps and enforce it through conditional access, so that an out-of-date personal phone loses access instead of staying out of compliance indefinitely. *Every exploit in DarkSword was patched before the kit leaked.*

Security teams also need visibility on the device itself, using detection that works at the OS level, runs on personal phones without requiring MDM enrollment, and doesn't depend on the employee noticing anything. That visibility is what turned an unusual DarkSword alert into the P7 discovery, and it's what let the financial institution's SOC act before the attacker reached the network. If a phone is compromised, treat every credential stored on it as compromised too, because DarkSword and its forks go straight for the keychain. For the small group of employees at the highest risk, Lockdown Mode is worth enabling, since Apple has said it blocks the DarkSword attacks, though it has to be on before exposure and changes how the phone works.

That coverage has to reach every employee and every platform, because ordinary staff are the ones getting caught on iPhone and Android alike. Android is going through its own version of this shift, with remote access trojans now sold by subscription to criminals with little technical skill. Cellik, for example, rents for $150 a month, wraps its payload around real Google Play apps, and intercepts the one-time passcodes used to confirm logins. Finally, collect telemetry from phones in real time, or within hours of a suspected attack if that isn't possible. Attackers now clean up aggressively, and the traces they leave age off the device quickly, so an investigation that starts days later may find nothing.

The full findings, including detection data, case studies and recommendations, are in the 2026 Advanced Mobile Threat Report. [Read it here](https://www.iverify.com/advanced-mobile-threat-report-2026).

## **Frequently asked questions**

### **What is a watering hole attack on iPhones?**

A watering hole attack plants an exploit on a website that potential victims are likely to visit, then attacks any vulnerable device that loads the page. Coruna and DarkSword have both been delivered this way, through compromised news and government sites and fake finance sites, so the victims are simply whoever visits on a vulnerable iOS version.

### **Can iPhone spyware be delivered through ads?**

Yes. iVerify observed a "half-click" attack from an ad served on Instagram, where the exploit started as soon as the ad loaded. Citizen Lab has also documented mercenary spyware delivered through targeted ads bought on mainstream ad exchanges. Because ad platforms let buyers target by device and OS version, attackers can aim an exploit at the phones running versions it works on.

### **Does updating iOS protect against Coruna and DarkSword?**

Yes. Every vulnerability DarkSword uses was patched before the kit leaked, and Coruna doesn't work on the latest iOS. The risk comes from phones that haven't installed those updates, which is common on personal devices whose MDM doesn't enforce a minimum version.

### **Will Apple warn me if my phone is infected?**

Not necessarily. [Apple's threat notifications](https://www.iverify.com/blog/so-you-ve-got-an-apple-threat-notification-what-now) are designed for people who may have been individually targeted. To iVerify's knowledge, none of the devices it confirmed as infected with Coruna or DarkSword received one.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
