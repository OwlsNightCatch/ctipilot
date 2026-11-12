---
title: Stable Channel Update for Desktop
author: Google
url: https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html
hostname: googleblog.com
description: The Stable channel has been updated to 157.0.8103.50/.51 for Windows and Mac and 157.0.8103.50 to Linux which will roll out over the comi...
sitename: Chrome Releases
date: "2026-11-09"
fingerprint: "1086fcb254b446e9"
---
## 
[Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html)

The Stable channel has been updated to 157.0.8103.50/.51 for Windows and Mac and 157.0.8103.50 to Linux which will roll out over the coming days/weeks. A full list of changes in this build is available in the [Log](https://chromium.googlesource.com/chromium/src/+log/157.0.8103.39..157.0.8103.50?pretty=fuller&n=10000).

Security Fixes and Rewards

Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.

This update includes [9](https://issues.chromium.org/issues?q=customfield1223088:1-M157) security fixes. Please see the [Chrome Security Page](https://www.chromium.org/Home/chromium-security) for more information.

\[N/A\]\[[550525698](https://issues.chromium.org/issues/550525698)\] High CVE-2026-125345: Uninitialized resource in WebGL. Reported by Google on 2026-08-21

\[N/A\]\[[561996724](https://issues.chromium.org/issues/561996724)\] High CVE-2026-125347: Incorrect authorization in FileSystem. Reported by Google on 2026-09-15

\[N/A\]\[[561998123](https://issues.chromium.org/issues/561998123)\] High CVE-2026-125343: Buffer overflow in Compositing. Reported by Google on 2026-09-15

\[N/A\]\[[563358700](https://issues.chromium.org/issues/563358700)\] High CVE-2026-125348: Out of bounds write in GPU. Reported by Google on 2026-09-18

\[N/A\]\[[568893995](https://issues.chromium.org/issues/568893995)\] High CVE-2026-125344: Type confusion in V8. Reported by Google on 2026-10-02

\[TBD\]\[[572578603](https://issues.chromium.org/issues/572578603)\]\[[582442907](https://issues.chromium.org/issues/582442907)\] High CVE-2026-125350: Use after free in XML. Reported by Arni Hardarson (Neonix Security) on 2026-10-12 and anonymous on 2026-11-06

\[N/A\]\[[536663516](https://issues.chromium.org/issues/536663516)\] Medium CVE-2026-125349: Uninitialized resource in GPU. Reported by Google on 2026-07-20

\[TBD\]\[[566384898](https://issues.chromium.org/issues/566384898)\] Medium CVE-2026-125342: Uninitialized resource in GPU. Reported by Vo Duc Thang (ugvxb) on 2026-09-26

Google is aware that an exploit for CVE-2026-125350 exists in the wild.

We would also like to thank all security researchers that worked with us during the development cycle to prevent security bugs from ever reaching the stable channel.

Many of our security bugs are detected using [AddressSanitizer](https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer), [MemorySanitizer](https://code.google.com/p/memory-sanitizer/wiki/MemorySanitizer), [UndefinedBehaviorSanitizer](https://www.chromium.org/developers/testing/undefinedbehaviorsanitizer), [Control Flow Integrity](https://www.chromium.org/developers/testing/control-flow-integrity/), [libFuzzer](https://chromium.googlesource.com/chromium/src/+/HEAD/testing/libfuzzer/README.md), or [AFL](https://github.com/google/afl).

Interested in switching release channels? Find out how [here](https://www.chromium.org/getting-involved/dev-channel). If you find a new issue, please let us know by [filing a bug](https://crbug.com/). The [community help forum](https://support.google.com/chrome/community) is also a great place to reach out for help or learn about common issues.
