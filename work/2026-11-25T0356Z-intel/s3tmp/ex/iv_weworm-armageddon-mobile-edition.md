---
title: "WeWorm(s) Armageddon: Mobile Edition"
url: https://www.iverify.com/blog/weworm-armageddon-mobile-edition
hostname: iverify.com
description: WeWorm is the first zero-click mobile worm, spreading through WeChat calls on iOS and Android. What it reveals about AI-built exploits and third-party app risk.
sitename: iVerify
date: "2026-09-29"
fingerprint: bfa49b129026774d
language: en
image: https://framerusercontent.com/images/SnTP9UhIdbTSvfvV5EZ7qS7uc.png?width=1920&height=1080
pagetype: website
filedate: "2026-11-25"
---
In September 2026, the security research firm [Calif published the details](https://calif.io/research/weworm) of “WeWorm”, the first known mobile-based, zero-click worm that spreads through WeChat calls on both iOS and Android. While the bug has been patched, the research says a lot about how fast mobile exploits can now be built, and a part of the mobile attack surface that is hard to see into.

## Key takeaways

Three things stand out. The first is speed. Calif says that, working with AI, a small team went from finding the bug to a working remote code execution exploit in about two days, and to a self-spreading worm in roughly another week. When you contrast that with the traditional 30-90 day patch cycle, it creates an untenable gap. While vendors have responded by increasing patching cadence, the advantage is still in favor of the attacker as it takes time for organizations to implement patches and test them for compatibility.

Second is where the risk sits. Third-party messaging apps run on top of iOS and Android but don’t consistently use the platforms’ strongest defenses, and app store listings don’t tell you which ones do. In fact, because the operating system generally has the strongest security, attackers are increasingly looking to apps to find their way in. No escalation is needed if all the information the attacker is looking for is within the app, and super apps such as WeChat contain a trove of information. This is why scammers like to move conversations from native messaging apps to third-party apps; they can bypass many in-built security features that might otherwise trigger.

Lastly, this attack highlights the danger of super apps. WeChat has many features and each comes with their own data from location history and messaging, to a full overview of contacts and even banking information, all without taking over the device.

## What Calif built

The attack needs nothing from the victim beyond receiving a call. In Calif’s demo, an attacker’s Android phone calls an iPhone and takes over the WeChat app whilst it is still ringing. The compromised iPhone then calls another Android phone and takes it over the same way. Calif sums it up in one line: “Attacker calls victim, victim becomes attacker, victim calls the next victim.” The victim doesn’t even have to answer. If they do, they hear silence while the exploit finishes. Declining the call only stops that attempt, and the attacker can call again later.

Calif noted the takeover only needs seconds and gives full control of the WeChat account. Because the vulnerability sat within the WeChat app and didn’t escalate beyond the app sandbox, the worm was interoperable with both Android and iOS which is noteworthy as generally attacks are siloed to one platform or the other.

## The timeline is the story

Calif’s disclosure log says its AI found the bug before its engineers knew about it. Work like this used to take a larger team months but this round, the humans mostly decided what to target and how to test it safely. It is important to note that Calif’s team is highly skilled so were likely able to work at an accelerated pace over someone less experienced leveraging the same AI tools. What they didn’t disclose was the effort cost in compute or tokens so unclear how well resourced a threat actor(s) would need to be to pull something similar off. We know finding bugs is increasingly automated, but turning a bug into a working exploit can still take specialized knowledge… for now.

The implication is straightforward. If the Calif team was able to do it in a short time, there will be others who can too, particularly if we look at heavily resourced and skilled spyware developers such as NSO Group, Intellexa, Paragon Solutions and Candiru, or nation-state actors. Software has too many code paths to formally verify. As long as part of the stack uses memory-unsafe languages, and as long as logic bugs exist, there will be more to find even if the pathway Calif used has been closed.

## The blind spot: third-party apps

Mobile platforms are much harder to attack than desktops. On a desktop, an attacker often just needs someone to click a file. On iOS and Android, apps are tightly sandboxed, so attackers need real vulnerabilities. That pushes them toward the apps that are easiest to break.

Native messaging apps such as iMessage ship with the platform’s newest defenses: pointer authentication codes (PAC), memory tagging (MTE), and hardened memory allocators. Third-party messaging apps don’t all meet that standard making them the new meta game for iOS zero-click. And that list is long: WhatsApp, Signal, Instagram, Discord, TikTok, Snapchat, KakaoTalk, QQ, Viber, Kik, etc. Each has its own protocol, and many are built on security budgets that are much more limited than WeChat, which is backed by Tencent, a major company with a large security team. The riskiest apps are those that process incoming data in the background: calls, notifications, media, files, audio, etc.

Compromising an app doesn’t hand over the whole device but the right app alone can be enough, particularly a super app that contains a multitude of data such as messages, location, and the network of people someone communicates with, which attackers value in its own right. For example, a phone number can often reveal which services someone is on, so pulling the contacts list allows an attacker to pick whichever of those apps is easiest to break.

With mass attacks like WeWorm, it’s generally an app’s popularity that determines whether building an exploit is worth it. Attackers are not going to bother if the app is used in some small population, unless that population is the target such as high-value individuals. The second consideration is the range of features, which determines how much information the attacker can get and a financially motivated attack would likely pick one connected to a wallet.

That calculation is why everything apps are such attractive targets. When one app holds messages, payments, location, and contacts, a single exploit exposes all of it. Dedicated apps from separate developers are safer and spreading functions across apps limits how much data any one company holds.

## What you can’t see today

Right now, adopting the platform’s security features is a recommendation for app developers, not a requirement. App store listings show permissions like location and photo access. They don’t show whether an app uses PAC, enforces control flow in its native code, uses MTE, or is written in a memory-safe language. Reducing this attack surface will take industry-wide effort, since some of it depends on the platform owners.

The bar for app vendors covers exactly what’s invisible from the outside:

- Use the platform’s defenses, such as PAC and MTE.
- Write in memory-safe languages like Swift and Rust.
- Sandbox unknown senders so they can’t reach complex parsers, protocols, or bundled open-source code.
- Test those restrictions for bypasses, including spoofing a known contact.

That last point matters. WeWorm required the attacker to be in the victim’s contacts. That barrier falls once any one of the victim’s friends is compromised.

WeWorm is the first in a planned Calif series on zero-click attack surfaces in messaging apps, expect more to come and for frontier models to begin training on this data. App developers need to adapt to reduce the overall risk they pose to devices. Just like businesses can’t rely on patch-only strategies, neither can app vendors. There’s currently no way to measure the quality of a patch or know whether the implemented solution also inadvertently introduced new bugs that can be exploited. AI is too advanced to not implement best practices as a default.

## The bottom line

This WeWorm exploit has been mitigated, but the conditions that made it possible haven’t changed. Working with AI, a small team needed about two days to go from bug to working exploit and roughly a week more to build a self-spreading worm. Organizations still need time to test and roll out patches after they arrive. The attack didn’t target the operating system. It went after a third-party app, where defenses are inconsistent and can’t be seen from outside. And because that app was a super app, compromising it alone exposed messages, contacts, location, and payment data without taking over the device.

No single party can close those gaps. App vendors need to adopt the platform’s defenses, and platform owners have a role in raising the bar. Until both happen, security teams can’t rely on patch schedules and app store listings to tell them whether the phones in their fleet are at risk. They can’t control how every app on those devices is built, but they can control whether they have visibility into the devices themselves.

That visibility is standard on laptops and servers, yet the phones that hold the same sensitive data and are even used to authenticate access to those devices often go without it. iVerify brings that visibility to iOS and Android, so security teams aren’t left waiting on someone else’s patch cycle to understand their mobile risk.

Calif calls WeWorm the first in a series, and AI keeps shortening the time from bug to exploit. The question for security leaders isn’t whether another attack like this is coming, but whether they’ll have visibility into their mobile fleet when it does.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
