---
title: Stable Channel Update for Desktop
author: Google
url: https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_12.html
hostname: googleblog.com
description: The Stable channel has been updated to 146.0.7680.75/76 for Windows/Mac and 146.0.7680.75 for Linux, which will roll out over the coming d...
sitename: Chrome Releases
date: "2026-03-12"
fingerprint: "75960c925cb50799"
---
## 
[Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_12.html)

The Stable channel has been updated to 146.0.7680.75/76 for Windows/Mac  and 146.0.7680.75 for Linux, which will roll out over the coming days/weeks. A full list of changes in this build is available in the [Log](https://chromium.googlesource.com/chromium/src/+log/146.0.7680.71..146.0.7680.76?pretty=fuller&n=10000)

Security Fixes and Rewards

Updated 2026-03-13: The previous version of these notes included CVE-2026-3909, the fix

for which will instead be available in a future update.

*Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.*

[1](https://issues.chromium.org/issues?q=customfield1223088:1-M146)security fix. Please see the

[Chrome Security Page](https://www.chromium.org/Home/chromium-security)for more information.

\[N/A\]\[

[491410818](https://issues.chromium.org/issues/491410818)\] High CVE-2026-3910: Inappropriate implementation in V8. Reported by Google Threat Analysis Group on 2026-03-10

Google is aware that an exploit for CVE-2026-3910 exists in the wild.

We would also like to thank all security researchers that worked with us during the development cycle to prevent security bugs from ever reaching the stable channel.

Many of our security bugs are detected using

[AddressSanitizer](https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer),

[MemorySanitizer](https://code.google.com/p/memory-sanitizer/wiki/MemorySanitizer),

[UndefinedBehaviorSanitizer](https://www.chromium.org/developers/testing/undefinedbehaviorsanitizer),

[Control Flow Integrity](https://www.chromium.org/developers/testing/control-flow-integrity/),

[libFuzzer](https://chromium.googlesource.com/chromium/src/+/HEAD/testing/libfuzzer/README.md), or

[AFL](https://github.com/google/afl).

Interested in switching release channels? Find out how [here](https://www.chromium.org/getting-involved/dev-channel). If you find a new issue, please let us know by [filing a bug](https://crbug.com/). The [community help forum](https://support.google.com/chrome/community) is also a great place to reach out for help or learn about common issues.

Srinivas Sista
