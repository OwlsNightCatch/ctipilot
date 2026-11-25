---
title: "Closing the Patch Gap: How to Set Minimum OS Versions for BYOD Phones"
url: https://www.iverify.com/blog/byod-minimum-os-version
hostname: iverify.com
description: Leaked iOS exploits target phones that skipped updates. How to enforce minimum iOS and Android versions on BYOD devices without full MDM.
sitename: iVerify
date: "2026-11-23"
fingerprint: bf26dc87da8432cd
language: en
image: https://framerusercontent.com/images/xUUjn6qM9Ys7O8FqTAvYGe6zyw.png?width=1024&height=576
pagetype: website
filedate: "2026-11-25"
---
## **TL;DR**

- Criminal groups aim leaked iOS toolkits at flaws Apple has already patched, a tactic known as N-day exploitation. Phones that skipped updates are the target.
- The organizations hit in iVerify's enterprise cases lean on BYOD programs whose MDM, "if it's even used, does not force iOS updates on personal phones."
- On Android, 60% of the enterprise devices iVerify monitors run a security patch more than 90 days old.
- You can't force updates on a phone you don't manage, but you can block corporate access below a minimum OS version. Pair that with on-device detection for the phones that still slip through.

## **Why the patch gap is the 2026 attack surface**

The iOS attacks of 2026 mostly exploit flaws Apple has already fixed, meaning they land in the gap between a patch's release and its installation.

After the Coruna and DarkSword toolkits leaked, criminal groups copied and modified them, turning them into N-day campaigns against devices that haven't been updated. iVerify's [2026 Advanced Mobile Threat Report](https://www.iverify.com/advanced-mobile-threat-report-2026) sums up the shift: "Attackers no longer need to find new bugs (though with AI even that is much easier). They need to find phones that haven't been patched, and there are plenty."

The fixes are already out. [Google Threat Intelligence Group's DarkSword analysis](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain) found that iOS 26.3 patched every vulnerability in the chain, most of them earlier, so the criminal variants are built for phones that skipped those updates. Attempts to move DarkSword onto newer iOS haven't worked so far: when claims spread of a variant that could infect iOS 26.5, iVerify tested the published samples against devices on iOS 26.0 and later, and none of them worked.

Attackers are finding those phones, too. By September, Coruna attacks against devices on vulnerable iOS versions had reached 5% of devices, up from 1.5% in August, according to the report.

Meanwhile, the volume of fixes keeps climbing. Apple's iOS and iPadOS updates fixed 485 unique CVEs by September 28, 2026, against 243 by the same point in 2025, and as the report notes, "every fix also tells an attacker where to look." A phone that falls a few releases behind is carrying a growing list of publicly documented flaws.

### Why BYOD phones often fall behind

Personal phones lag on updates because many BYOD programs are designed not to force them.

The organizations in iVerify's enterprise cases lean heavily on bring-your-own-device programs. Their mobile device management, "if it's even used, does not force iOS updates on personal phones, and employees can stay out of compliance for months without consequence." Executives, the report notes, are more likely to already have managed devices, enforced updates, and closer attention from security teams.

Organizations often accept a lighter touch on personal phones because traditional mobile security ties protection to device management, which means enrolling the phone and seeing more of it than employees are comfortable with. As the report puts it, "the trade-off comes from the tools, not from privacy itself." The cost is a weaker security posture on a large share of the devices that touch corporate data, and those are the phones this year's campaigns keep landing on. Every enterprise detection of Coruna and DarkSword that iVerify recorded in 2026 involved an employee at or below managing-director level.

Android shows the same pattern in iVerify's fleet telemetry, where 60% of monitored enterprise Android devices run a security patch more than 90 days old, 15% run one more than a year old, and 68% aren't on the latest Android version.

## **Step 1: Set the floor at the latest OS version**

Start with a written rule: corporate data is reachable only from phones running the latest OS release, with a grace window for users who haven't updated yet. Every release behind the current one carries publicly documented flaws, and those are the flaws this year's criminal campaigns target. A workable policy has three parts:

- **The latest iOS version as the floor.** When Apple ships an update, it becomes the new requirement. iPhones that can't run the current major release should be on the latest security update Apple provides for that hardware.
- **The latest Android version and security patch level as the floor.** Android versions and monthly patch levels move separately, so a recent version with an old patch can still be exposed. Manufacturers release patches on their own schedules, so expect some devices to trail Google's monthly bulletin.
- **A grace window.** Some users will lag behind every release, so warn first, then block. A hard cutoff on day one generates help desk tickets faster than it closes risk.

Keep the window as short as your workforce can absorb, and shorten it further for updates that fix vulnerabilities known to be exploited in the wild. Write the policy down before you configure anything, so the help desk, HR, and employees all see the same rule.

### **Step 2: Enforce it at the access layer**

On a phone you don't manage, you can't make the update happen, but you can make access depend on it. The worked examples below use Microsoft Intune, Entra ID, and Apple's own deployment docs, and most MDM, MAM, and identity platforms offer equivalent controls.

**Enrolled devices: compliance plus conditional access**

For phones enrolled in Intune, a compliance policy sets the floor. Microsoft's [iOS compliance settings](https://learn.microsoft.com/mem/intune/protect/compliance-policy-create-ios) state that "a device that doesn't meet the minimum OS version requirement is considered to be noncompliant," and the user sees a link explaining how to upgrade. The [Android Enterprise compliance settings](https://learn.microsoft.com/mem/intune/protect/compliance-policy-create-android-for-work) add a minimum security patch level as well.

Compliance alone only labels the device. Conditional Access in Microsoft Entra ID acts on the label. According to Microsoft's [Conditional Access documentation](https://learn.microsoft.com/azure/active-directory/conditional-access/require-managed-devices), Intune sends compliance information to Entra "so Conditional Access can decide to grant or block access to resources."

**Unenrolled BYOD: app protection policies**

Many employees won't enroll a personal phone. For those devices, Intune [app protection policies](https://learn.microsoft.com/en-us/intune/app-management/protection/overview) protect company data at the app level without managing the device. Their [conditional launch settings](https://learn.microsoft.com/en-us/intune/app-management/protection/configure-conditional-launch) include a minimum OS version for iOS and Android, with three possible actions: warn, block access, or wipe the corporate data from the app. Min OS version takes one value per action, so you can warn at your new floor while blocking only below the old one, then raise the block when the grace window ends. [App-based Conditional Access](https://learn.microsoft.com/en-us/intune/app-based-conditional-access-intune) can then require an app protection policy before a corporate app connects.

Keep in mind what these policies do and don't cover. They decide whether an app may reach corporate data. They don't protect a phone that's already compromised: the report warns that containerization won't save an enterprise, because exploits like DarkSword can puncture common mobile data-governance tools.

**Managed Apple devices: forced updates with a deadline**

Where you do manage the device, Apple's [software update declarative configuration](https://support.apple.com/guide/deployment/depca14ecd4d/web) sets a target OS version and a deadline: "If the user doesn't trigger the software update before this time, the device force installs it." Microsoft's [guide to Apple software updates in Intune](https://learn.microsoft.com/en-us/intune/device-updates/apple/) lists support for Device Enrollment and Automated Device Enrollment on iOS and iPadOS 17 and later. User Enrollment, the method many BYOD programs use, isn't on that list, so for most personal phones the access-layer controls above remain the main lever.

### **Step 3: Close sideloading on Android**

On Android, the patch gap has a companion problem in phones that will install apps from outside Google Play.

Sideloading is a main delivery path for the Android remote access trojans iVerify tracked this year. In iVerify's fleet, 22% of enterprise Android devices allow it, and 21% actually sideloaded an app in the last six months. None of these kits break Android: every RAT iVerify observed gets in by persuading the victim to install an app and grant it Accessibility access. So even a fully patched phone is exposed if it accepts an unknown app.

On managed devices, the [Android Management API's untrustedAppsPolicy](https://developers.google.com/android/management/reference/rest/v1/enterprises.policies) controls installs from unknown sources. Its default, DISALLOW\_INSTALL, blocks them device-wide. On BYOD phones with a work profile, ALLOW\_INSTALL\_IN\_PERSONAL\_PROFILE\_ONLY keeps the work side closed while leaving the personal side open, so the personal side still needs other controls. Our post on [Android RATs for rent](https://www.iverify.com/blog/android-rat-malware-as-a-service) covers how these kits work.

### **Step 4: Assume some phones will still be exposed**

A minimum version policy shrinks the exposed fleet. It doesn't empty it, so plan for the phones it misses. Four gaps remain even with good enforcement:

- **The window between release and install.** Every phone is behind for some time after Apple or Google ships a fix, and that's the window N-day attackers work in. The report warns that vulnerabilities are now exploited faster than patches can be deployed.
- **Threats that don't need an old OS.** Android RATs need no exploit at all, only a user who can be talked into installing an app.
- **Threats that arrive through trusted channels.** In September, an App Store app called [FomoPeek carried a working exploitation toolkit](https://www.iverify.com/blog/fomopeek-app-store-exploit). Its exploits targeted older iOS versions, but users got it from the official store, so allowing only App Store apps doesn't replace visibility into what actually runs on the phone.
- **Phones that were compromised before the policy reached them.** Blocking access doesn't remove an implant that's already there.

That's why the report's recommendations go beyond patching: detect on the device rather than after the fact, collect telemetry in real time or, failing that, within hours, and treat a compromised phone as compromised credentials by rotating every credential stored on it, including SSO, email, VPN, and messaging accounts. Don't count on a warning from Apple either: to iVerify's knowledge, no device it detected under DarkSword or Coruna attack received an Apple Threat Notification. On-device EDR that works on personal phones covers the exposure that access controls can't.

## **Checklist: closing the BYOD patch gap**

- Write a minimum version policy: an iOS floor, an Android version and patch-level floor, and a warn-then-block grace window.
- Enforce it at the access layer: compliance plus conditional access for enrolled phones, app protection policies for unenrolled ones, forced update deadlines where you manage the device.
- Restrict sideloading on Android, and know what your work-profile setting leaves open on the personal side.
- Put detection on every employee's phone, with real-time telemetry, for the exposure that access controls can't close.
- If a phone is compromised, rotate every credential stored on it.

## **FAQ**

**Can you force iOS updates on personal phones?**

Not without managing the device. Apple's forced update deadline works through Device Enrollment and Automated Device Enrollment, which most personal phones aren't on. What you can do is block corporate access below a minimum iOS version through compliance policies or app protection policies.

**Does updating iOS protect against DarkSword?**

Yes. According to Google Threat Intelligence Group, iOS 26.3 patched every vulnerability in the DarkSword chain, and most were fixed earlier. For iPhones that can't run iOS 26, Apple released fixes in iOS 18.7.7. The criminal variants circulating now are built for phones that skipped those updates.

**What minimum iOS version should we require?**

The latest one. Require the current iOS release, give employees a short grace window with warnings before blocking access, and shorten that window when Apple patches an actively exploited flaw. For iPhones that can't run the current major version, require the latest security update Apple provides for that hardware.

**How do we enforce minimum OS versions without full MDM?**

Use app protection policies. They apply to corporate apps on unenrolled phones and can warn, block access, or wipe corporate data when a device runs below your minimum OS version. They control access, not compromise, so pair them with on-device detection.

**Should we turn on Lockdown Mode?**

For a few people likely to face mercenary spyware, yes: Apple told TechCrunch it defends against DarkSword, and Google Threat Intelligence Group recommends it where an update isn't possible. But it isn't a workforce control. It restricts features most employees won't accept on a personal phone, and iVerify's 2026 detections show ordinary employees, not executives, are the ones getting hit. Minimum OS versions and on-device detection cover the people Lockdown Mode can't.

Subscribe to our blog to receive the latest research and industry trends delivered straight to your inbox. Our blog content covers sophisticated mobile threats, unpatched vulnerabilities, smishing, and the latest industry news to keep you informed and secure.
