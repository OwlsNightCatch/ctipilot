---
title: Researchers Detail iPhone Flaw That Let Apps Record Audio Despite Denied Microphone Permission
author: The Hacker News
url: https://thehackernews.com/2026/11/researchers-detail-iphone-flaw-that-let.html
hostname: thehackernews.com
description: Apple patched CVE-2026-65339, which let installed apps record audio despite denied microphone permission on iPhones and iPads.
sitename: The Hacker News
date: "2026-11-17"
categories: ['Article']
tags: ['Apple', 'iOS', 'mobile security', 'Permission Bypass', 'Privacy', 'Vulnerability']
fingerprint: a86ccf87a3a692c7
language: en
image: https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjoRknesoqi26EwwYMrgBhBudDMiej0sO7-228OvrBIj2ivaPcOUo7GJgoIHAd9fI_VFlK4su0xn1L_BqUgFsldNJgAkQwE4wAvAZzUao-wHUHSoq8NQUo_UdyILYYFoshEgONLhibaGHRQ_cKFVo0Psl1kehyphenhyphenNjlCrkECk16huiU6WecKlpBr0YDN3nus/s1700-nu-rw-lo-l85-e365/iphone-recording.jpg
pagetype: article
filedate: "2026-11-25"
---
A now-patched flaw in Apple's audio service let apps on iPhones and iPads record audio even after the user tapped "Don't Allow" on the microphone prompt.

The first security updates with the fix came out on August 17. Neither Apple nor the two researchers who found the flaw report that it was used in attacks.

Nik Tsytsarkin of **Meta Red Team X** published the technical details last week. **Mustafa Calap**, a security engineer who reported the same flaw separately, published his own analysis the same day.

On iPhones, an orange indicator shows when an app is using the microphone. On one of the researchers' earlier test builds, that indicator stayed off while the app recorded.

In Tsytsarkin's tests, the prompt appeared the first time the app opened. Declining it did not stop the recording, and the prompt did not reappear on subsequent launches.

In the earlier build of his [technical analysis](https://rtx.meta.security/exploitation/2026/11/09/CVE-2026-65339.html), the system logs showed no record of the app using the microphone. They named the audio service itself as the recorder.

His demo video shows the indicator while the test app records with no microphone permission. He wrote that the video "was filmed on a later build that appears to have restored the orange microphone indicator."

Calap's test app recorded while its permission still read denied, according to his [detailed write-up](https://dbg.re/posts/cve-2026-65339-audiomxd-microphone-permission-bypass/). No orange indicator appeared in the Dynamic Island or in Control Center. He does not say which of his two test builds that was.


Neither researcher describes a way for users to check whether an app recorded them before the fix. Calap reproduced the bypass on iOS 26.6, released July 27, and on an iPadOS 27 beta.

The bypass needed an app already installed on the device. His two test apps were sandboxed apps with no added entitlements. Their only privacy key was NSMicrophoneUsageDescription, which makes the microphone prompt appear.

In his tests, recording had to start while the app was in the foreground. Once started, it continued after the app went to the background and after the device was locked. The background version also set UIBackgroundModes = audio.

Both apps were installed from Xcode and never went through App Review. So the tests do not show whether App Review would have stopped such an app.

The Meta analysis compared two iOS 27 test builds. Neither researcher reports testing macOS, tvOS, watchOS, or visionOS, though fixes are listed for those systems too.

The bypass covered microphone capture through the audio service only. It did not give the app other privacy permissions.

These releases fix the flaw, which is tracked as CVE-2026-65339:

- [iOS 26.6.1](https://support.apple.com/en-us/148282) and iPadOS 26.6.1 (August 17), for iPhone 11 and later, iPad Pro 12.9-inch 3rd generation and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd generation and later, iPad 8th generation and later, and iPad mini 5th generation and later
- [iOS 18.7.11](https://support.apple.com/en-us/149225) and iPadOS 18.7.11 (October 26), for iPhone XS, iPhone XS Max, iPhone XR, and iPad 7th generation
- [macOS Tahoe 26.6.2](https://support.apple.com/en-us/148281) (August 17)
- [macOS Sequoia 15.8](https://support.apple.com/en-us/149043) (September 14)
- [tvOS 27](https://support.apple.com/en-us/149036) (September 14), for Apple TV 4K 2nd generation and later
- [watchOS 27](https://support.apple.com/en-us/149037) (September 14), for Apple Watch Series 9 and later
- [visionOS 27](https://support.apple.com/en-us/149038) (September 14), for Apple Vision Pro (all models)

The researchers describe no setting that blocks the bypass, so installing these updates is the fix.

The [iOS 27 notes](https://support.apple.com/en-us/149034) do not list the flaw, nor do those for later iOS 27 updates as of today. Meta's timeline says the fix shipped in iOS 27.0 beta 5 on August 10.

CISA gives the flaw a CVSS score of 5.0 out of 10. The agency's catalog of known exploited vulnerabilities does not list it, as of the catalog's update late last week.

Apple's notes for the August 17 updates describe the flaw only as one that may let an app leak sensitive user information.

Tsytsarkin wrote: "That description leaves out the most striking part: the app could record after permission was denied, without the orange indicator appearing."

In his own tests, the indicator was missing only on the earlier build. An app does not decide for itself whether it may record. That decision goes through the Transparency, Consent, and Control (TCC) system, which checks which process is asking.

The audio service, called **audiomxd**, accepted the app's own word about which process was asking. An audit token identifies a process. An app could send the service a token that named audiomxd itself.

The service then treated the app as itself. It took a shortcut meant for its own internal audio and allowed recording without asking TCC. The kernel itself provided the app with the details it needed to impersonate the service.

The fix makes the service check the real caller's identity, which the kernel supplies. Outside callers now need the private entitlement com.apple.private.audio.client-audit-token-override to replace the client identity the service relies on. An app cannot grant itself that entitlement.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
