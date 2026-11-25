---
title: "Half-Click Attacks: How Online Ads Now Deliver iPhone Exploits"
url: https://www.iverify.com/blog/half-click-attacks-iphone-ads
hostname: iverify.com
description: Attackers now deliver iOS exploits through targeted ads that run as the ad loads. How half-click attacks work and how to defend against them.
sitename: iVerify
date: "2026-11-10"
fingerprint: "95a59c85c087c3c3"
language: en
image: https://framerusercontent.com/images/iyxBLJUSeEbN3T6DNc3Voc8k.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
## **TL;DR**

- A half-click attack starts the exploit as soon as an ad loads, so the victim never has to tap anything.
- iVerify recorded one served on Instagram while the user was simply scrolling. The payload was a DarkSword variant, and the likely goal was cryptocurrency theft.
- Ad platforms let buyers target by device, OS version, location, and interests, so an attacker can show an exploit only to phones it will work on.
- Forgotten web plumbing is being hijacked too. An expired analytics domain sent online shoppers to a site serving DarkSword ([Report URI](https://blog.report-uri.com/abandoned-analytics-domain-funnels-store-visitors-to-darksword-iphone-exploits/)).
- Blocking "risky sites" won't stop this. The defense is a patched OS plus detection running on the phone itself.

## **What is a half-click attack?**

A half-click attack is an exploit delivered through a display ad that starts running as soon as the ad loads on the page, so the victim never has to tap anything. It places half-click attacks between the two attack types most security teams already plan for:

| **Attack type** | **What the victim does** | **Typical delivery** | 
| One-click | Taps a link | Phishing SMS, email, chat message or watering hole attack | 
| Half-click | Opens an app or page that shows ads | Targeted display ad carrying exploit code | 
| Zero-click | Nothing at all | A message or call handled by the OS in the background | 

What makes the category hard to defend against is that the victim does nothing risky. They don't open an attachment, follow a link, or install an app; they simply use an app or website that shows advertising, which describes most phones for most of the day. Some press coverage of similar ad-based attacks has called them zero-click. Whichever label you prefer, the consequence for defenders is the same: user awareness training can't stop an attack the user never gets a chance to notice.

## **Why attackers moved from watering holes to ads**

Attackers are moving to ads because ad platforms solve a targeting problem that watering holes never could.

Earlier this year, watering holes were the main delivery route for the leaked iOS kits. Google Threat Intelligence Group and iVerify found DarkSword served through a malicious script tag on [compromised Ukrainian websites](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain), an approach that works only up to a point. A compromised site reaches whoever happens to visit it, and many of those visitors run iOS versions the exploit can't touch. DarkSword supports iOS 18.4 through 18.7, so every visitor on iOS 26 is wasted effort for the attacker.

Advertising removes that waste. Ad platforms let a buyer choose who sees an ad by device, OS version, location, and interests, so an attacker with an exploit for iOS 18.5 can buy placements that appear only on iPhones running 18.5, then narrow the audience further to people interested in crypto. As [iVerify's 2026 Advanced Mobile Threat Report](https://www.iverify.com/advanced-mobile-threat-report-2026) states, ads offer "the reach of a mass campaign with the precision of a targeted one."

### **The mercenary precedent**

The technique was proven in mercenary spyware before criminals adopted it. In October, Citizen Lab [published research](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) on Discover-Tech, an Israeli ad tech firm whose platform bought placements through mainstream ad exchanges. When one of its ads rendered, Discover-Tech's server checked the device's IP address and advertising identifiers, then sent additional JavaScript to chosen targets and "a 0-byte response" to everyone else. Citizen Lab found at least 45 targeted devices at Al Jazeera and linked the attacks "with high confidence" to Candiru.

The ad buying behind the operation ran at real scale. Between March and June 2026, one demand-side platform involved appeared to win 441,954,291 of the 3,770,286,576 bids it placed, according to Citizen Lab's data. [iVerify](https://www.iverify.com/) assesses that the same technique has since moved well beyond journalists and mercenary vendors into criminal campaigns at mass scale, and its telemetry has recorded what that looks like on an ordinary person's phone.

## **Case study: one person, two attacks**

iVerify telemetry recorded two separate DarkSword attacks on the same person. Nothing about them would mark them as a high-value target.

The first attack came during an Instagram browsing session, through an ad served from ad-track\[.\]live. The infection began without the person clicking anything, and the payload was a DarkSword variant.

The second came later. This time the person clicked a link, and the attack involved a different threat actor using a second, distinct [DarkSword](https://www.iverify.com/darksword-exploit-hub) variant.

In both cases, iVerify assesses the goal was cryptocurrency theft. The domains behind the ads were themed around this year's [World Cup](https://www.iverify.com/resources/case-studies/schibsted), bait chosen for reach rather than for any one person.

Two independent actors reached the same ordinary user through everyday browsing. The report's conclusion: "any ad-supported platform may carry similar risk." Nothing here suggests a failure by the platform the ad appeared on. Ad exchanges move huge volumes of creative between buyers and publishers, and that pipeline is what attackers are buying their way into.

## **Forgotten web plumbing: the ecomtrack\[.\]io hijack**

Ads aren't the only shared web infrastructure being turned into an exploit channel. Abandoned third-party scripts are too.

In October, Scott Helme of Report URI [documented](https://blog.report-uri.com/abandoned-analytics-domain-funnels-store-visitors-to-darksword-iphone-exploits/) how ecomtrack\[.\]io, an expired e-commerce analytics domain, was re-registered by a new owner on 15 September 2026. Its tracking tag "was still sitting in the theme of stores that had long since stopped thinking about it," so those online stores began loading code controlled by whoever now held the domain.

The chain that followed:

1. The tag collected device data from each shopper and sent it to the new owner's server.
2. Scanners and crawlers were sent to a random YouTube video or google.com.
3. Traffic brokers sold real visitors to three buyers: an investment scam page, an online casino, and a fake crypto trading site.
4. The fake trading site checked for Safari on iOS 18.4.0 to 18.7.2 and served DarkSword.

Report URI later matched the implant to P7, the DarkSword variant [iVerify documented](https://www.iverify.com/blog/darksword-variant-threat-research) in October, with two modules "byte-for-byte identical" to iVerify's samples.

The shoppers did nothing riskier than browse a store whose owners had forgotten a script in their theme. None of those stores was malicious, which is why URL reputation and site blocklists offer so little protection against this kind of attack.

## **Why these attacks are hard to investigate later**

Ad-delivered and script-delivered exploits are built to show nothing to anyone who isn't a chosen target, including investigators.

Both delivery routes above filter their audience. In the ecomtrack\[.\]io chain, Report URI found that "datacentre and VPN IPs consistently received empty responses," and some residential visitors got a payload on their first request and nothing after. Discover-Tech's server behaved the same way, returning "a 0-byte response" to any device it hadn't selected ([Citizen Lab](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)). By the time an analyst tries to reproduce an infection, the page serves nothing, so the evidence has to come from the phone itself.

That's harder than it used to be. DarkSword has no persistence, so a reboot or update removes the running implant along with many of the traces an investigator would look for. According to iVerify's report, some DarkSword indicators exist on a device for only a very short time, so continuous on-device monitoring has to catch them during that window, or it will miss them entirely.

## **How to defend against ad-delivered exploits**

Users can't avoid half-click attacks by being careful, so the controls have to sit on the device and its OS version.

1. **Patch.** Every vulnerability in the DarkSword chain was fixed by iOS 26.3, and most were fixed earlier, according to [Google Threat Intelligence Group and iVerify](https://www.iverify.com/darksword-exploit-hub). Criminal variants in circulation target phones that skipped those updates.
2. **Enforce minimum OS versions on BYOD.** The organizations hit in iVerify's enterprise cases lean heavily on BYOD, and their MDM doesn't force iOS updates on personal phones. Blocking corporate access below a version floor closes much of that gap.
3. **Put detection on the phone.** A filtered exploit server leaves investigators nothing to retrieve. On-device EDR can see the side effects exploitation leaves in system logs, diagnostics, and on-device artifacts.
4. **Collect telemetry in real time.** Where that isn't possible, collect it within 2 hours, before short-lived indicators age off the device.
5. **Use Lockdown Mode for the highest-risk staff.** Google recommends it [where an update isn't possible](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain), and an Apple spokesperson told [TechCrunch](https://techcrunch.com/2026/03/23/someone-has-publicly-leaked-an-exploit-kit-that-can-hack-millions-of-iphones/) it would block the DarkSword attacks. It changes how the phone works, so it fits a short list of users rather than a whole fleet.

## **FAQ**

### **Can you get hacked just by seeing an ad on your iPhone?**

Yes, if the iPhone runs a vulnerable iOS version. iVerify recorded a DarkSword variant delivered through an Instagram ad, with the infection starting before the user clicked anything.

### **What is a half-click attack?**

It's an exploit delivered through a display ad that runs as soon as the ad loads. The victim only has to view a page or app that shows the ad.

### **Which iOS versions does DarkSword affect?**

DarkSword supports iOS 18.4 through 18.7, according to [the Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain). All of the vulnerabilities it uses were patched by iOS 26.3.

### **Do ad blockers prevent half-click attacks?**

They can reduce exposure in the browser, but they don't cover every app that shows ads, and they don't address the hijacked-script route. Keeping iOS updated and running detection on the phone are the controls that hold up across both.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
