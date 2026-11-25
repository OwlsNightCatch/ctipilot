---
title: "Coruna, DarkSword and the Enterprise iPhone: Key Takeaways from Packet Protector"
url: https://www.iverify.com/blog/coruna-darksword-packet-protector-takeaways
hostname: iverify.com
description: Key takeaways from Packet Protector on the Coruna and DarkSword iOS exploit kits, and how enterprise teams can protect their mobile fleets.
sitename: iVerify
date: "2026-10-13"
fingerprint: bd201980cd0333e9
language: en
image: https://framerusercontent.com/images/0eQuyAh8QySuY6MY2fum7I7fh3M.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
## TL;DR

- On Packet Protector, mobile security architect Akili Akridge explained how the Coruna and DarkSword iOS exploit kits work and what enterprise defenders should do.
- Both kits started in the hands of surveillance customers or state-linked actors and are now used by financially motivated criminals. DarkSword's source code leaked publicly after disclosure.
- Patching and Lockdown Mode help, but neither is a complete answer. Lockdown Mode only protects a device if it is turned on before the malicious page loads, and it limits everyday use.
- Akridge's playbook for enterprises: visibility across the whole fleet, identity-scoped access, a loaner device bench for incident response, and executive protection that covers global admins and the CISO.
- Attacks that run at the kernel level and clean up after themselves are hard to catch with app-layer tools or network-layer tools, which is why he points teams toward mobile EDR.

On a recent episode of [Packet Protector](https://www.youtube.com/watch?v=7oWRiDmvjNs), host Drew Conry-Murray spoke with [Akili Akridge](https://www.linkedin.com/in/akili-akridge/) about Coruna and DarkSword, two iOS exploit kits that iVerify's research team helped expose earlier this year. Akridge is a mobile security expert and principal architect at a major US airline. The conversation covers where the kits came from, how they compromise an iPhone, and what enterprise security teams should change in response. 

*Listen to the full episode here, then read on for the main takeaways and links to iVerify's research.*

## What Coruna and DarkSword are

Coruna and DarkSword are exploit kits: each bundles several exploits into a chain that takes an iPhone from a single web page visit to full device compromise. [Google Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/coruna-powerful-ios-exploit-kit) counted five full exploit chains and 23 exploits in Coruna, covering iOS 13.0 through 17.2.1. [DarkSword](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained), which iVerify disclosed in March 2026 with Lookout and Google, chains six vulnerabilities to target iOS 18.4 through 18.7.

During the podcast, Akridge walked through the attack sequence. A user lands on a compromised or fake website. A WebKit vulnerability gives the attacker code execution in the browser; the chain escapes the sandbox, and a kernel exploit grants read and write access to memory. From there, the implants run inside privileged system processes. Coruna also checks whether a target is worth pursuing: according to Google's analysis, it backs out if the device is in Lockdown Mode or the user is browsing privately.

The data these kits collect is what makes them an enterprise problem. iVerify's DarkSword analysis found implants targeting keychain contents, Wi-Fi passwords, messages, Telegram and WhatsApp data, location history, and crypto wallet files. Akridge's advice for security teams: if a device used for work is compromised, treat every credential stored on it as compromised too.

## Government-grade tools are now in criminal hands

Much of the episode traces how these kits changed hands. Google followed Coruna from a customer of a surveillance vendor, to a suspected Russian espionage group running watering hole attacks against Ukrainian users, to a financially motivated actor in China using fake finance sites. iVerify has since [linked](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword) Coruna to L3 Harris subdivision Trenchant, where former employee Peter Williams was convicted of stealing zero-day exploits and selling them to a Russian broker.

*Akridge compared this market to arms dealing. Exploits built for government missions cost a great deal to develop and are in high demand. They leak through insider theft, external breaches, or trades between states and proxy groups*.

DarkSword moved even faster. Soon after iVerify published its findings, a third party leaked its source code, and iVerify has since tracked several clusters of new variants. Google has also seen DarkSword used in Saudi Arabia, Turkey, and Malaysia. Attackers have also started pairing the two kits. At Black Hat 2026, iVerify's Matthias Frielingsdorf showed both deployed together from a single site, a setup iVerify calls DarkCoruna, which lets one visit target a wider range of iOS versions.

iVerify's telemetry shows the trend. In September 2026, live and historic Coruna attacks against devices on vulnerable iOS versions affected 5% of devices, more than triple the 1.5% seen in August ([*source*](https://www.iverify.com/blog/proliferation-of-coruna-and-darksword)).

## Why patching and Lockdown Mode aren't enough on their own

Updating iOS closes the vulnerabilities each kit relies on, and it remains the first step. Akridge's concern is pace. In his view, every patch tells them where to look next, and AI tools are shrinking the time between a fix and a working exploit. iVerify's research suggests AI's help is uneven so far. Many recent DarkSword variants appear to be failed, LLM-assisted attempts to add iOS 26 support. Not every variant is that clumsy, though. The authors of [P7 DarkSword](https://www.iverify.com/blog/darksword-variant-threat-research) clearly understood the code they were changing, and their version steals keychain data and crypto wallets directly on the device.

Lockdown Mode offers some protection. It disables some of the web features these chains depend on, and Coruna is built to back off when it detects it. Akridge’s main caveat is timing: it only protects a device if it’s switched on before the user opens the malicious page. Cost is the other problem. He compared a phone in Lockdown Mode to a flip phone, and [Apple’s list of restrictions](https://support.apple.com/en-us/105120) shows why. Most message attachment types are blocked, incoming FaceTime calls are blocked unless you’ve contacted that person in the past 30 days, some websites break, and shared albums disappear. It’s fair to ask whether a phone set up this way still works for remote work, and few employees would accept it as the everyday setting on their own device.

Lockdown Mode also clashes with device management. A device can’t enroll in MDM while it’s on, and configuration profiles can’t be installed. For any device that isn’t already enrolled, security teams end up choosing between Lockdown Mode and the tools that depend on MDM enrollment. iVerify doesn’t require MDM, but many mobile security products need it for some of their features. In practice, Lockdown Mode fits best as a short-term control for specific people or high-risk trips.

## Akridge's playbook for enterprise mobile fleets

Akridge closed with a set of steps for enterprise teams. In summary:

1. Get visibility on every device. Watering hole attacks don't choose their victims, so any unmonitored phone in the fleet can be caught in one, and attackers look for those gaps.
2. Audit what each identity can reach from a mobile device, and trim access that goes beyond what the role needs.
3. Run MDM and mobile application management as a baseline, but don't expect them to catch an attack. MDM reports what a device is, such as its configuration and OS version, and can't see what's running on it. App management doesn't help either, because these exploits run as JavaScript in the browser and never go through managed apps.
4. Keep a loaner bench of ready-to-issue devices. When a device is suspected compromised, swap it out, isolate the original in airplane mode or a Faraday bag, and preserve it for investigation.
5. Build an executive protection program that includes global admins and the CISO alongside the C-suite. He ranked those two groups as the most attractive targets because of their access. Board members matter too, since many sit on several boards.
6. Monitor identity activity alongside device activity.
7. Evaluate newer tools built around behavioral analysis and low-level device telemetry, rather than waiting for a known signature to fire.

The loaner bench connects to how iVerify approaches response. Preserving the affected device is what makes a forensic investigation possible. In the P7 DarkSword case, an alert on a customer's device led, with the customer's consent, to incident response work that recovered forensic artifacts and identified a previously unknown variant.

## What it takes to catch these attacks

These kits are hard to spot because of where they run. Once a chain reaches the kernel, its implants work inside legitimate system processes, and many delete their own traces when they're done. Akridge pointed out that most mobile threat defense tools sit at the application layer, so they have little view of activity at that depth. A tool that checks in on a device every few minutes can also miss an infection that starts and cleans up in between.

Network-layer tools run into a similar wall. As Akridge explained, the first connection to a watering hole site looks like ordinary HTTPS traffic to a legitimate website, so it only stands out if that domain is already flagged as malicious. Everything after that happens on the device, outside the network's view, and adapting network security products to cover on-device threats doesn't close that gap.

His answer was continuous, low-level telemetry, which is the approach behind mobile EDR. With the right data coming off the device, a security team can see what happened and respond quickly.

The cleanup usually leaves something behind, too. iVerify found that some Coruna artifacts persist across reboots and iOS updates, so a past infection can still be detected on a device that wasn't being monitored when it was hit. DarkSword's cleanup is incomplete as well: [iVerify's analysis](https://www.iverify.com/blog/darksword-ios-exploit-kit-explained) found it misses some crash logs and leaves Safari history in place, both of which forensic tools can pick up.

iVerify Mobile EDR collects kernel-adjacent telemetry from iOS and Android devices to detect threats like Coruna and DarkSword. For indicators of compromise and technical analysis of both kits, visit the [DarkSword exploit hub](https://www.iverify.com/darksword-exploit-hub).

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
