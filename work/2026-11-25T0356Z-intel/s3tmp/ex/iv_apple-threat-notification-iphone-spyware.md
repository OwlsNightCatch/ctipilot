---
title: Will Apple Warn You? Why Threat Notifications and Forensics Miss Today's iPhone Attacks
url: https://www.iverify.com/blog/apple-threat-notification-iphone-spyware
hostname: iverify.com
description: Apple threat notifications are built for individually targeted users. Why criminal iPhone attacks go unflagged and forensics finds little.
sitename: iVerify
date: "2026-11-16"
fingerprint: a50cc98d1a26b3ca
language: en
image: https://framerusercontent.com/images/3PyS5GPchviDPxWjW9FcI7zorDo.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
[Blog](https://www.iverify.com/blog)

# Will Apple Warn You? Why Threat Notifications and Forensics Miss Today's iPhone Attacks

iVerify Team

## **TL;DR**

- Apple sends threat notifications to users who "may have been individually targeted by mercenary spyware attacks" ([Apple](https://support.apple.com/en-us/102174)). The 2026 criminal campaigns don't fit that profile.
- To iVerify's knowledge, none of the devices it confirmed as infected with Coruna or DarkSword received a notification.
- When iVerify investigated a dozen notifications this year, it found limited evidence of exploitation. Attackers clean up, and traces age off devices fast.
- Investigating after the fact rarely works anymore. Detection has to be on the phone, collecting telemetry in real time or within hours.

## **What Apple Threat Notifications are designed to catch**

Apple Threat Notifications warn people who may have been singled out by mercenary spyware, and for that threat the program does its job well.

Apple's own description sets the scope. Mercenary spyware attacks "cost millions of dollars" and target "a very small number of specific individuals," and notifications go to users who "may have been individually targeted by mercenary spyware attacks, likely because of who they are or what they do" ([Apple](https://support.apple.com/en-us/102174)). The warning appears on the iPhone Lock Screen and in Settings, arrives by email, and shows as a banner on the user's Apple Account page. The program is also growing: Apple's August 13 wave reached users in 110 countries, and Apple says it has now notified people in more than 150 ([MacTech](https://www.mactech.com/2026/08/14/apple-sends-out-notifications-to-users-targeted-with-spyware-in-110-countries/)).

Apple is also open about the limits. Its notifications rely on internal threat intelligence and investigations, which "can never achieve absolute certainty." Notifications also go out in batches rather than at the moment of attack, so by the time one arrives, the attack may be long over.

## **Why criminal campaigns don't trigger them**

The attacks hitting enterprise phones in 2026 are criminal, untargeted, and aimed at whoever runs a vulnerable iOS version, which puts them outside the threat Apple's notifications are scoped to.

[iVerify's 2026 Advanced Mobile Threat Report](https://www.iverify.com/advanced-mobile-threat-report-2026) found that 75% of this year's detections were criminals stealing credentials and cryptocurrency rather than state-sponsored actors, and every enterprise detection involved an employee below managing-director level. The leaked Coruna and DarkSword kits reached those employees through compromised websites, hijacked scripts, and targeted ads, served to anyone whose phone matched. Our post on \[half-click attacks\] covers how that delivery works.

The result is a gap in coverage. To iVerify's knowledge, none of the devices it confirmed as infected with Coruna or [DarkSword](https://www.iverify.com/darksword-exploit-hub) received an Apple threat notification, even though those were the most prevalent strains in iVerify's data. That says more about the program's scope than its quality, since a system built for individually targeted users isn't designed to flag a mass campaign. A security team that waits for a notification before investigating will be waiting for an alert that never comes.

## **The going-dark problem**

Even when a notification does arrive, after-the-fact forensics now finds less than it used to.

Most of what the public knows about iPhone spyware came from forensic work. Someone got a warning or noticed something odd, researchers pulled a backup, a full file system extraction, or a sysdiagnose, and went looking for traces. That's how [Pegasus](https://www.iverify.com/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update) and much of the mercenary spyware industry were exposed, and iVerify's report notes it worked largely because "early implants were careless," leaving persistent artifacts with little obfuscation or cleanup.

That's no longer the case. iVerify investigated a dozen Apple threat notifications this year and found limited evidence of exploitation, with no forensically sound, high-confidence evidence in any of them. Several of the people fit the profile of past mercenary spyware targets, some had received more than one notification, and some correlate strongly with earlier Pegasus activity. iVerify has good reason to believe some were targeted, and it could not prove it from what remained on the device.

Mercenary spyware hasn't gone away. In October, Citizen Lab [linked attacks on Al Jazeera devices](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) to Candiru "with high confidence." What's changed is how much these tools leave behind. iVerify has recorded no novel Pegasus detections since 2023, and the report reads that as "a visibility problem, not as evidence that Pegasus, Predator, Candiru, or their peers have stopped operating."

The 2026 kits push this further. DarkSword has no persistence, so a reboot or update removes the running implant along with many of the traces an investigator would look for ([DarkSword explained](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained)), and some of its indicators exist on a device for only a short time. An investigation that starts days after the attack has almost no chance of finding them, which is why iVerify treats its DarkSword numbers as a floor.

## **What arriving late costs**

*This is a composite drawn from enterprise detections, with details changed to protect iVerify's customers.*

An in-house attorney at a large US technology company was among the first employees to receive iVerify in a staged rollout. Within about an hour of the app reaching the phone, iVerify flagged signs of compromise, even though the infection predated the install. The attacker had come and gone but hadn't cleaned up every indicator, which is the only reason the compromise was visible at all, and iVerify recovered evidence that a full file system dump had been taken.

The employee had done a lot right. They used Safari's private browsing by default and had turned on every privacy feature Apple offers, but they hadn't enabled Lockdown Mode, the one setting designed to block this kind of attack. As one of iVerify's researchers put it, they had every protection except the one that would have mattered.

Because iVerify arrived after the fact, the team could say the phone had been compromised but not when or how, which is the normal outcome of a late investigation. iVerify's data records the iOS version at the time of a scan rather than at infection, and some Coruna artifacts persist across reboots and iOS updates, so without a full forensic submission it's often impossible to say which version was exploited. When iVerify is already on a device before an infection, it can place an alert against the device's own event history and build a confident timeline.

## **What being on the device looks like**

The P7 variant was found because detection was already running on the phone when the attack happened.

1. In August, iVerify received a DarkSword alert from the iPhone of a financial institution employee who had clicked a malicious ad. The detection "differed slightly from the usual DarkSword detections," enough for iVerify's threat hunters to look closer.
2. With the customer's consent, iVerify collected artifacts from the phone, including suspicious files written to /private/var/tmp around the time of infection.
3. The team used those artifacts to hunt for related infrastructure in Validin. That led to a domain hosting another build of the same spyware family, a recovered sample, and the P7 variant.
4. iVerify published indicators of compromise in its [full write-up](https://www.iverify.com/blog/darksword-variant-threat-research).
5. A day later, Report URI matched an implant served through hijacked store scripts to the same family, with two modules "byte-for-byte identical to iVerify's samples" ([Report URI](https://blog.report-uri.com/abandoned-analytics-domain-funnels-store-visitors-to-darksword-iphone-exploits/)).

Meanwhile, the customer's SOC was alerted before any lateral movement into its network. The whole chain, from a small anomaly on one phone to a public analysis other defenders could use within days, depended on catching the attack while the evidence still existed.

## **What to do**

Treat Apple threat notifications as one valuable signal, and build detection that doesn't depend on them.

1. **Get on the device**. Rely on EDR running on the phone, not on post-incident forensics or Apple threat notifications alone.
2. **Collect telemetry in real time.** Where you can't, collect it within hours, before the evidence ages off.
3. **Deploy before you need it.** A tool installed after an infection can tell you a phone was compromised, but rarely when or how.
4. **Take notifications seriously when they arrive.** Follow [Apple's guidance](https://support.apple.com/en-us/102174), including Lockdown Mode and expert help, and treat the device as an incident.
5. **Cover every employee**. The people being hit in 2026 are rank-and-file staff, so a detection program limited to executives and travelers misses them.

## **FAQ**

### **Will Apple tell me if my iPhone has spyware?**

Not necessarily. Apple's threat notifications are for users who may have been individually targeted by mercenary spyware. To iVerify's knowledge, none of the devices it confirmed as infected with the criminal Coruna or DarkSword kits received one.

### **What should I do if I get an Apple threat notification?**

Follow [Apple's guidance](https://support.apple.com/en-us/102174). It recommends enabling Lockdown Mode and getting expert help, such as Access Now's Digital Security Helpline. For a work device, also bring in your security team and treat it as an incident.

### **Can iPhone spyware be found after a reboot?**

It depends on the spyware. DarkSword has no persistence, so a reboot removes its running implant and many of its traces. Some Coruna artifacts do survive reboots and iOS updates.

### **How do you detect spyware on an iPhone?**

The most reliable way is on-device monitoring that's in place before an attack, collecting telemetry in real time. After-the-fact forensic tools still have a role, but against self-cleaning kits, they often find too little to reach a firm conclusion.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
