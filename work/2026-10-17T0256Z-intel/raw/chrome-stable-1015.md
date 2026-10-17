---
title: Stable Channel Update for Desktop
author: Google
url: https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_01886704284.html
hostname: googleblog.com
description: The Stable channel has been updated to 155.0.8059.84/.85 for Windows and Mac and 155.0.8059.84 to Linux which will roll out over the comin...
sitename: Chrome Releases
date: "2026-10-15"
fingerprint: "74b6bc3242b446f1"
---
## 
[Stable Channel Update for Desktop](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_01886704284.html)

The Stable channel has been updated to 155.0.8059.84/.85 for Windows and Mac and 155.0.8059.84 to Linux which will roll out over the coming days/weeks. A full list of changes in this build is available in the [Log](https://chromium.googlesource.com/chromium/src/+log/155.0.8059.80..155.0.8059.85?pretty=fuller&n=10000)

# Security Fixes and Rewards

Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.


This update includes [10](https://issues.chromium.org/issues?q=customfield1223088:2-M155) security fixes. Please see the [Chrome Security Page](https://www.chromium.org/Home/chromium-security) for more information.

\[N/A\]\[[568719351](https://issues.chromium.org/issues/568719351)\] Critical CVE-2026-110922: Use after free in Prerender. Reported by Xinyang Ge on 2026-10-02

\[N/A\]\[[567638392](https://issues.chromium.org/issues/567638392)\] High CVE-2026-110913: Memory corruption in DOM. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-09-29

\[N/A\]\[[568831769](https://issues.chromium.org/issues/568831769)\] High CVE-2026-110919: Use after free in V8. Reported by Xinyang Ge on 2026-10-02

\[N/A\]\[[568937999](https://issues.chromium.org/issues/568937999)\] High CVE-2026-110918: Memory corruption in Core. Reported by Google on 2026-10-03

\[TBD\]\[[569038297](https://issues.chromium.org/issues/569038297)\] High CVE-2026-110917: Memory corruption in SVG. Reported by C0rk1 on 2026-10-03

\[N/A\]\[[569286602](https://issues.chromium.org/issues/569286602)\] High CVE-2026-110921: Use after free in V8. Reported by Xinyang Ge on 2026-10-05

\[N/A\]\[[569659194](https://issues.chromium.org/issues/569659194)\] High CVE-2026-110920: Memory corruption in V8. Reported by Xinyang Ge on 2026-10-05

\[N/A\]\[[501886301](https://issues.chromium.org/issues/501886301)\] Medium CVE-2026-110916: Improper input validation in Desktop. Reported by Google on 2026-04-12

\[N/A\]\[[556272421](https://issues.chromium.org/issues/556272421)\] Medium CVE-2026-110915: Use after free in Compositing. Reported by Google on 2026-09-02

\[N/A\]\[[563194341](https://issues.chromium.org/issues/563194341)\] Medium CVE-2026-110914: Memory corruption in Workers. Reported by Google on 2026-09-18

We would also like to thank all security researchers that worked with us during the development cycle to prevent security bugs from ever reaching the stable channel.

Many of our security bugs are detected using [AddressSanitizer](https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer), [MemorySanitizer](https://code.google.com/p/memory-sanitizer/wiki/MemorySanitizer), [UndefinedBehaviorSanitizer](https://www.chromium.org/developers/testing/undefinedbehaviorsanitizer), [Control Flow Integrity](https://www.chromium.org/developers/testing/control-flow-integrity/), [libFuzzer](https://chromium.googlesource.com/chromium/src/+/HEAD/testing/libfuzzer/README.md), or [AFL](https://github.com/google/afl).

[here](https://www.chromium.org/getting-involved/dev-channel). If you find a new issue, please let us know by

[filing a bug](https://crbug.com/). The

[community help forum](https://support.google.com/chrome/community)is also a great place to reach out for help or learn about common issues.
