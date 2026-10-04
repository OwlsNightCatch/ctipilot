---
title: Chrome Releases
author: Google
url: https://chromereleases.googleblog.com/
hostname: googleblog.com
description: Release updates from the Chrome team
sitename: Chrome Releases
date: "2026-10-02"
---
# Security Fixes and Rewards

Note: Access to bug details and links may be kept restricted until a majority of users are updated with a fix. We will also retain restrictions if the bug exists in a third party library that other projects similarly depend on, but haven’t yet fixed.


This update includes [11](https://issues.chromium.org/issues?q=customfield1223088:2-M154) security fixes. Please see the [Chrome Security Page](https://www.chromium.org/Home/chromium-security) for more information.


[N/A][[549995090](https://issues.chromium.org/issues/549995090)] Critical CVE-2026-103628: Out of bounds write in WebGL. Reported by Google on 2026-08-21

[N/A][[553114097](https://issues.chromium.org/issues/553114097)] High CVE-2026-103626: Incorrect authorization in FileSystem. Reported by Google on 2026-08-26

[N/A][[556268833](https://issues.chromium.org/issues/556268833)] High CVE-2026-103621: Integer overflow in Compositing. Reported by Google on 2026-09-02

[TBD][[557323166](https://issues.chromium.org/issues/557323166)] High CVE-2026-103630: Use after free in FedCM. Reported by xinyang on 2026-09-04

[N/A][[559893859](https://issues.chromium.org/issues/559893859)] High CVE-2026-103625: Type confusion in V8. Reported by Google on 2026-09-11

[TBD][[561660166](https://issues.chromium.org/issues/561660166)] High CVE-2026-103624: Use after free in Contextual Tasks. Reported by xuanocto1221 on 2026-09-15

[N/A][[562038679](https://issues.chromium.org/issues/562038679)] High CVE-2026-103629: Integer overflow in Skia. Reported by Google on 2026-09-15

[TBD][[565742179](https://issues.chromium.org/issues/565742179)] High CVE-2026-103622: Use after free in SVG. Reported by xinyang on 2026-09-24

[TBD][[565742180](https://issues.chromium.org/issues/565742180)] High CVE-2026-103623: Use after free in MediaStream. Reported by xinyang on 2026-09-24

[TBD][[567088927](https://issues.chromium.org/issues/567088927)] High CVE-2026-103631: Buffer overflow in WebRTC. Reported by Xinyang Ge (Anthropic), assisted by Claude on 2026-09-28

[N/A][[553147154](https://issues.chromium.org/issues/553147154)] Medium CVE-2026-103627: Information leak in SVG. Reported by Google on 2026-08-26


We would also like to thank all security researchers that worked with us during the development cycle to prevent security bugs from ever reaching the stable channel.


Many of our security bugs are detected using [AddressSanitizer](https://code.google.com/p/address-sanitizer/wiki/AddressSanitizer), [MemorySanitizer](https://code.google.com/p/memory-sanitizer/wiki/MemorySanitizer), [UndefinedBehaviorSanitizer](https://www.chromium.org/developers/testing/undefinedbehaviorsanitizer), [Control Flow Integrity](https://www.chromium.org/developers/testing/control-flow-integrity/), [libFuzzer](https://chromium.googlesource.com/chromium/src/+/HEAD/testing/libfuzzer/README.md), or [AFL](https://github.com/google/afl).
