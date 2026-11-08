---
title: Android Security Bulletin—November 2026 | Android Open Source Project
url: https://source.android.com/docs/security/bulletin/2026/2026-11-01
hostname: android.com
sitename: Android Open Source Project
date: "2026-11-01"
fingerprint: "9e22fc559cac6782"
---
*Published November 2, 2026 | Updated November 6, 2026*

This Android Security Bulletin contains details of security vulnerabilities
that affect Android devices. Security patch levels of
2026-11-05 or later address all of these issues.
To learn how to check a device's security patch level, see
[Check and update your Android version](https://support.google.com/pixelphone/answer/4457705).

Within 48 hours after the initial publication of this bulletin, we will release the corresponding source code patches to the Android Open Source Project (AOSP) repository. We will then revise this bulletin with the AOSP links.

The most severe of these issues is a critical security vulnerability in the Framework
component that could lead to remote code execution with no additional execution privileges
needed. User interaction is not needed for exploitation.
The [severity assessment](https://source.android.com/security/overview/updates-resources.html#severity) is based on the effect that exploiting the vulnerability
would possibly have on an affected device, assuming the platform and service mitigations are
turned off for development purposes or if successfully bypassed.

For more details on the Android security platform protections and Google
  Play Protect, which improve the security of the Android platform,
  refer to the [Android and Google Play Protect
  mitigations](https://source.android.com#mitigations) section.

We notify our Android partners of all issues at least a month before publishing the bulletin.

## Android and Google service mitigations

This is a summary of the mitigations provided by the
[Android security platform](https://source.android.com/security/enhancements) and service
protections such as
[Google Play
Protect](https://developers.google.com/android/play-protect). These capabilities reduce the likelihood that security
vulnerabilities could be successfully exploited on Android.

- Exploitation for many issues on Android is made more difficult by enhancements in newer versions of the Android platform. We encourage all users to update to the latest version of Android where possible.
- The Android security team actively monitors for abuse through
  [Google Play
  Protect](https://developers.google.com/android/play-protect) and warns users about [Potentially
  Harmful Applications](https://source.android.com/static/security/reports/Google_Android_Security_PHA_classifications.pdf). Google Play Protect is enabled by default on devices
  with [Google Mobile
  Services](http://www.android.com/gms), and is especially important for users who install apps from
  outside of Google Play.

## 2026-11-01 security patch level vulnerability details

In the sections below, we provide details for each of the security
    vulnerabilities that apply to the 2026-11-01 patch level.
    Vulnerabilities are grouped under the component they affect.
    Issues are described in the tables below and include CVE ID, associated
    references, [type of vulnerability](https://source.android.com#type),
    [severity](https://source.android.com/security/overview/updates-resources#severity),
    and updated AOSP versions (where applicable).
    When available, we link the public change that addressed the issue to the
    bug ID, like the AOSP change list.
    When multiple changes relate to a single bug, additional references are
    linked to numbers following the bug ID.
      Devices with Android 10 and later may receive security updates as well as
      [Google Play
      system updates](https://support.google.com/android/answer/7680439).

### Android runtime

The most severe vulnerability in this section could lead to local information disclosure with no additional execution privileges needed. User interaction is not needed for exploitation.

| CVE | References | Type | Severity | Updated AOSP versions | 
|---|---|---|---|---|
| CVE-2026-58988 | A-269456968 | ID | High | 14, 15, 16, 16-qpr2, 17 | 

### Framework

The most severe vulnerability in this section could lead to remote code execution with no additional execution privileges needed. User interaction is not needed for exploitation.

| CVE | References | Type | Severity | Updated AOSP versions | 
|---|---|---|---|---|
| CVE-2026-58868 | A-486464711 | RCE | Critical | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58857 | A-503553199 | RCE | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2025-22424 | A-350456241 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2025-22426 | A-365086157 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2025-22442 | A-382064697 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2025-26433 | A-385347977 | EoP | High | 14, 15 | 
| CVE-2026-28588 | A-475232460 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-28597 | A-262884935 | EoP | High | 14, 15, 16, 16-qpr2 | 
| CVE-2026-28645 | A-466379326 | EoP | High | 15, 16, 16-qpr2, 17 | 
| CVE-2026-45514 | A-465446148 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-49923 | A-498857374 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55257 | A-472968114 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55271 | A-499298430 | EoP | High | 17 | 
| CVE-2026-55287 | A-472955222 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58836 | A-349318333 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-58837 | A-525133623 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58853 | A-503542266 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58866 | A-494816520 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58886 | A-527035500 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58934 | A-527038637 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58944 | A-527036864 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58946 | A-527034642 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-58957 | A-500368515 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58961 | A-527039128 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58962 | A-527035781 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58965 | A-514861143 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58966 | A-511632970 | EoP | High | 16-qpr2, 17 | 
| CVE-2026-58970 | A-478861451 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58974 | A-527036176 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58975 | A-506176085 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58978 | A-459460815 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58979 | A-527038421 | EoP | High | 17 | 
| CVE-2026-58986 | A-514738229 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-58989 | A-429182079 | EoP | High | 15, 16, 16-qpr2 | 
| CVE-2026-58995 | A-505748392 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59004 | A-472701802 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59014 | A-505573349 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2025-22436 | A-277076451 | ID | High | 14, 15 | 
| CVE-2026-28586 | A-477935679 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-28621 | A-356604577 | ID | High | 14, 15, 16 | 
| CVE-2026-49935 | A-495409704 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55264 | A-498162425 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58838 | A-482947423 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58933 | A-501467247 | ID | High | 16, 16-qpr2, 17 | 
| CVE-2026-58951 | A-527037031 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58969 | A-514738573 | ID | High | 16-qpr2, 17 | 
| CVE-2026-58971 | A-511027559 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58997 | A-513648011 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59002 | A-519884370 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59006 | A-493560718 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59011 | A-484925508 | ID | High | 16, 16-qpr2, 17 | 
| CVE-2026-59015 | A-497659915 | ID | High | 15, 16, 16-qpr2, 17 | 
| CVE-2026-59022 | A-517377899 | ID | High | 15, 16, 16-qpr2, 17 | 
| CVE-2026-28643 | A-495646742 | DoS | High | 16, 16-qpr2, 17 | 
| CVE-2026-49924 | A-451602444 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55272 | A-492093013 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58817 | A-429417238 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58875 | A-515038894 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58937 | A-464276781 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58938 | A-503554506 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58949 | A-503551664 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59008 | A-281543351 | DoS | High | 16-qpr2, 17 | 
| CVE-2026-59020 | A-515039372 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59021 | A-515039631 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59031 | A-514737201 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 

### System

The most severe vulnerability in this section could lead to remote code execution with no additional execution privileges needed. User interaction is not needed for exploitation.

| CVE | References | Type | Severity | Updated AOSP versions | 
|---|---|---|---|---|
| CVE-2026-58876 | A-503543341 | RCE | Critical | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58936 | A-496614216 | RCE | Critical | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55275 | A-522376559 | EoP | Critical | 16, 16-qpr2, 17 | 
| CVE-2026-55283 | A-522375782 | EoP | Critical | 16, 16-qpr2, 17 | 
| CVE-2026-58984 | A-514731794 | EoP | Critical | 15, 16, 16-qpr2, 17 | 
| CVE-2026-58814 | A-517378147 | DoS | Critical | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58882 | A-517376969 | DoS | Critical | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-0053 | A-368376056 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-28580 | A-481967442 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-28665 | A-488559440 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-45522 | A-482024712 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-49922 | A-504612754 | EoP | High | 14, 15, 16, 16-qpr2 | 
| CVE-2026-49934 | A-508585261 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55261 | A-503545851 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-55262 | A-505067993 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55263 | A-472976054 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55289 | A-505203996 | EoP | High | 17 | 
| CVE-2026-58867 | A-515051007 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58871 | A-511543870 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58879 | A-517593332 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58884 | A-515051745 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58885 | A-517377188 | EoP | High | 17 | 
| CVE-2026-58943 | A-313418699 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58956 | A-461507723 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58964 | A-515712425 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58968 | A-503554745 | EoP | High | 16, 16-qpr2, 17 | 
| CVE-2026-58994 | A-532588581 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59000 | A-517378646 | EoP | High | 16-qpr2, 17 | 
| CVE-2026-59005 | A-517376786 | EoP | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59016 | A-546680461 | EoP | High | 17 | 
| CVE-2026-59028 | A-522373825 | EoP | High | 15, 16, 16-qpr2, 17 | 
| CVE-2025-48600 | A-435188844 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-28632 | A-444443479 | ID | High | 14, 15, 16, 16-qpr2 | 
| CVE-2026-49912 | A-478725173 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-49931 | A-490916793 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-55292 | A-503550880 | ID | High | 16, 16-qpr2, 17 | 
| CVE-2026-58821 | A-463363325 | ID | High | 16, 16-qpr2, 17 | 
| CVE-2026-58870 | A-515047710 | ID | High | 15, 16, 16-qpr2, 17 | 
| CVE-2026-58877 | A-500705928 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58945 | A-465140520 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58953 | A-478124606 | ID | High | 16, 16-qpr2, 17 | 
| CVE-2026-58976 | A-496454250 | ID | High | 15, 16, 16-qpr2, 17 | 
| CVE-2026-58990 | A-511263142 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59003 | A-515391495 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59007 | A-514742326 | ID | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-59012 | A-527424853 | ID | High | 14 | 
| CVE-2026-55288 | A-517377278 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58883 | A-517377202 | DoS | High | 16-qpr2, 17 | 
| CVE-2026-58955 | A-503434084 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58963 | A-517377034 | DoS | High | 14, 15, 16, 16-qpr2, 17 | 
| CVE-2026-58985 | A-514745329 | DoS | High | 16-qpr2, 17 | 
| CVE-2026-59010 | A-509578318 | DoS | High | 14, 15, 16, 16-qpr2 | 

### Google Play system updates

The following issues are included in Project Mainline components.

| Subcomponent | CVE | 
|---|---|
| Media Codecs | CVE-2026-58933 | 
| Media Codecs, Media Framework components | CVE-2026-58938 | 
| MediaProvider | CVE-2026-59011, CVE-2026-59022 | 
| Media Codecs | CVE-2026-58876, CVE-2026-58953, CVE-2026-58968 | 
| MediaProvider | CVE-2026-58821 | 
| Profiling | CVE-2026-59016 | 
| Telephonycore | CVE-2026-49922, CVE-2026-49934, CVE-2026-55289, CVE-2026-58883 | 
| WiFi | CVE-2026-58867, CVE-2026-58870, CVE-2026-58877, CVE-2026-58884 | 

## 2026-11-05 security patch level vulnerability details

In the sections below, we provide details for each of the security
    vulnerabilities that apply to the 2026-11-05 patch level.
    Vulnerabilities are grouped under the component they affect.
    Issues are described in the tables below and include CVE ID, associated
    references, [type of vulnerability](https://source.android.com#type),
    [severity](https://source.android.com/security/overview/updates-resources#severity),
    and updated AOSP versions (where applicable).
    When available, we link the public change that addressed the issue to the
    bug ID, like the AOSP change list.
    When multiple changes relate to a single bug, additional references are
    linked to numbers following the bug ID.

### Kernel components

The most severe vulnerability in this section could lead to remote escalation of privilege with no additional execution privileges needed. User interaction is not needed for exploitation.

| CVE | References | Type | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-53256 | A-508702285 [Upstream kernel](https://android.googlesource.com/kernel/common/+/529c9d587ac146586f9817ee994bd8cfa609769b) \[[2](https://android.googlesource.com/kernel/common/+/1542c05a4e0c4d0e76670e356bb5322a7e85b083)\] | EoP | Critical | Bluetooth | 
| CVE-2026-59044 | A-508702141 [Upstream kernel](https://android.googlesource.com/kernel/common/+/a4e59da7cad6b445229ae67c0ebed83a7b18dcb5) | EoP | Critical | pKVM | 
| CVE-2026-59045 | A-512428751 [Upstream kernel](https://android.googlesource.com/kernel/common/+/c47ebb7427d5011de67b526eac67b42da640bdc5) \[[2](https://android.googlesource.com/kernel/common/+/f0a2d3087b73b442b69fe0a9617ab920400abe15)\] \[[3](https://android.googlesource.com/kernel/common/+/eb970aae88c0f45056f4501b7815a9b5c7ab0435)\] \[[4](https://android.googlesource.com/kernel/common/+/f6510cfbc728061d7a8d4ea4ac91e5fc270aaf6b)\] \[[5](https://android.googlesource.com/kernel/common/+/9f965dd09cad69d0064f8a862d68cfc2163ba9d3)\] \[[6](https://android.googlesource.com/kernel/common/+/22ae719f35b14f88e551f0e858a1087a4b721204)\] \[[7](https://android.googlesource.com/kernel/common/+/bd9aaec66cf50ea3ade2b537d9b730e40fe512e6)\] \[[8](https://android.googlesource.com/kernel/common/+/f89e83e20aa69fbdd5b2f2de284dafcaadbda7c7)\] \[[9](https://android.googlesource.com/kernel/common/+/acce19149cb8ebe92218d0e66c08bc36552ddbdf)\] \[[10](https://android.googlesource.com/kernel/common/+/e10fb80c80387aa1f26695b57df95afe0ef00481)\] \[[11](https://android.googlesource.com/kernel/common/+/01ff2abe4905798e330a70f2970ee33a44419d24)\] | EoP | Critical | pKVM | 
| CVE-2026-80604 | A-517387820 [Upstream kernel](https://android.googlesource.com/kernel/common/+/15475ee563738135a9978f2a0481b1cf972b3b72) \[[2](https://android.googlesource.com/kernel/common/+/e684fde80e17d695cd52aaefb735fa2c76b0866e)\] | EoP | Critical | HID | 
| CVE-2026-89774 | A-508702364 [Upstream kernel](https://android.googlesource.com/kernel/common/+/315636ba7cbf03382cfa7bd8887118f59fe96c5f) \[[2](https://android.googlesource.com/kernel/common/+/598dbca6a3f78f038650c434935c86d8c3a6edfb)\] \[[3](https://android.googlesource.com/kernel/common/+/84728e305ff666fc2bf2be382b422b51912d7b1c)\] \[[4](https://android.googlesource.com/kernel/common/+/a377ba61de42bb336732bd273330fcbfd3d51f3a)\] | EoP | Critical | Bluetooth | 
| CVE-2026-59048 | A-512433296 [Upstream kernel](https://android.googlesource.com/kernel/common/+/e46b3a946c957ab463a8abf9333dea702e8a485e) \[[2](https://android.googlesource.com/kernel/common/+/5e31aa53a963b254ddac8a88b48e5b64cfc38eea)\] | ID | Critical | pKVM | 
| CVE-2025-38627 | A-499041514 [Upstream kernel](https://android.googlesource.com/kernel/common/+/5d604d40cd3232b09cb339941ef958e49283ed0a) \[[2](https://android.googlesource.com/kernel/common/+/4e9efe0d56e73d10e2f72e0328b537cea93198ec)\] \[[3](https://android.googlesource.com/kernel/common/+/84b5a9e56e50b8222cd5999cd8e44d0bdf7fed4f)\] \[[4](https://android.googlesource.com/kernel/common/+/eb95d43efb6bc27e17a5b98031ee41b5f9eee3a8)\] | EoP | High | Flash-Friendly File System | 
| CVE-2026-23240 | A-500321403 [Upstream kernel](https://android.googlesource.com/kernel/common/+/a5de36d6cee74a92c1a21b260bc507e64bc451de) | EoP | High | Transport Layer Security | 
| CVE-2026-31533 | A-504553976 [Upstream kernel](https://android.googlesource.com/kernel/common/+/0e43e0a3c94044acc74b8e0927c27972eb5a59e8) \[[2](https://android.googlesource.com/kernel/common/+/aa9facde6c5005205874c37db3fd25799d741baf)\] | EoP | High | TLS | 
| CVE-2026-43284 | A-510777270 [Upstream kernel](https://android.googlesource.com/kernel/common/+/f6d22ea6ae50acbc3f811a14fb2e55a2c129007d) \[[2](https://android.googlesource.com/kernel/common/+/32b16e61d1a02c4554d48b544ea4739d12e450e7)\] \[[3](https://android.googlesource.com/kernel/common/+/c7fb8c4114577c9f5b34a82259f3d7b8addbacb1)\] \[[4](https://android.googlesource.com/kernel/common/+/055c84c410288cf5169e180f8aca0792b6b8c9de)\] | EoP | High | Networking | 
| CVE-2026-43499 | A-496407345 [Upstream kernel](https://android.googlesource.com/kernel/common/+/5339d13d8b945cd5841d0e70728ee67474ea74f7) \[[2](https://android.googlesource.com/kernel/common/+/e7d9bd94fbdbf9842ea6f1b6d5af45758e87e3d6)\] \[[3](https://android.googlesource.com/kernel/common/+/63493728373acb0b79eb6c94cf462cece1d8110f)\] \[[4](https://android.googlesource.com/kernel/common/+/eb88e44c4e7ac2f5a13b2b51b9dfa2aea677e3e1)\] | EoP | High | Locking | 
| CVE-2026-46242 | A-509838226 [Upstream kernel](https://android.googlesource.com/kernel/common/+/58c9b016e12855286370dfb704c08498edbc857a) \[[2](https://android.googlesource.com/kernel/common/+/4a33cb8c9fe2dd18962c39568401e35b5de0ae59)\] \[[3](https://android.googlesource.com/kernel/common/+/c7a8aea27b87b74f62a2b2a5d16100caa2cba79c)\] \[[4](https://android.googlesource.com/kernel/common/+/5255cec633890d782c8a1daf792801eb527d0ac8)\] \[[5](https://android.googlesource.com/kernel/common/+/035da2cab032309d387d2935543743fb36c722c3)\] \[[6](https://android.googlesource.com/kernel/common/+/59f29da4ef0793f38ad1dbc01a9ee11bd4df636c)\] \[[7](https://android.googlesource.com/kernel/common/+/b51793e6880dff374dfcd95f8335bfa1e556fadb)\] \[[8](https://android.googlesource.com/kernel/common/+/e0384993ef8206abe4e644c0cb4bdb59d2c7bb4b)\] \[[9](https://android.googlesource.com/kernel/common/+/02f217a4bffc8a00313bf52ebb96003d7ae1d5d8)\] \[[10](https://android.googlesource.com/kernel/common/+/500d67e5110ab44ec1501113db76aa07287c112b)\] \[[11](https://android.googlesource.com/kernel/common/+/690d6106eec64f970d6b2bf87599838b016b1b00)\] \[[12](https://android.googlesource.com/kernel/common/+/3de54f8c502a7ac39095c2b5d30dfe8c17f8a411)\] \[[13](https://android.googlesource.com/kernel/common/+/3dff0800fae61e0de35ef20694c86106da64266d)\] \[[14](https://android.googlesource.com/kernel/common/+/64cea30f9b932d729e64a4098ad00d64e65f4813)\] \[[15](https://android.googlesource.com/kernel/common/+/2d6bc6abd42ae07fa460c0a0de524ed439a61207)\] \[[16](https://android.googlesource.com/kernel/common/+/f01453f20745731644a2bcc8c2a904e73f4db323)\] \[[17](https://android.googlesource.com/kernel/common/+/257b1c2c78c25643526609dee0c15f1544eb3252)\] \[[18](https://android.googlesource.com/kernel/common/+/58c9b016e12855286370dfb704c08498edbc857a)\] | EoP | High | Fs | 
| CVE-2026-58824 | A-503395542 [Upstream kernel](https://android.googlesource.com/kernel/common/+/8be8949794c96f10348fdd3d8dc7740fdfecd4e2) \[[2](https://android.googlesource.com/kernel/common/+/5a6735b89ba7c8684d36e2ecd9b02e834e97de9c)\] | EoP | High | Protected Kernel-Based Virtual Machine | 
| CVE-2026-58825 | A-499361237 [Upstream kernel](https://android.googlesource.com/kernel/common/+/efe16a3021b9f95eb1cb83e98d0d1db9bff94ce4) \[[2](https://android.googlesource.com/kernel/common/+/009c5006c969826d37a2c5fc2721a7bb20d72555)\] | EoP | High | Direct Memory Access Buffer | 
| CVE-2026-58826 | A-498850457 [Upstream kernel](https://android.googlesource.com/kernel/common/+/13beada2dac38c2d7303f1700aa16fb5053b919d) \[[2](https://android.googlesource.com/kernel/common/+/efe16a3021b9f95eb1cb83e98d0d1db9bff94ce4)\] \[[3](https://android.googlesource.com/kernel/common/+/f7d26609785ce56170645d56f306db38e8ba277a)\] \[[4](https://android.googlesource.com/kernel/common/+/009c5006c969826d37a2c5fc2721a7bb20d72555)\] | EoP | High | Direct Memory Access Buffer | 
| CVE-2026-58827 | A-499359964 [Upstream kernel](https://android.googlesource.com/kernel/common/+/769fa413e80cca30ff767f6f3e18f920d0353f67) \[[2](https://android.googlesource.com/kernel/common/+/6642375b48bea1fc287a9281db591a8edc74db79)\] | EoP | High | Direct Memory Access Buffer | 
| CVE-2026-58828 | A-496996374 [Upstream kernel](https://android.googlesource.com/kernel/common/+/b597ddd55fd100d3eca5b9c2024a5a09dcc950ec) \[[2](https://android.googlesource.com/kernel/common/+/0285abdfbfb9f99898d647dafb2ea7d4bdd22527)\] \[[3](https://android.googlesource.com/kernel/common/+/dd1ca7920b1eb7db5dbd34590c811cd99e2c3fdf)\] \[[4](https://android.googlesource.com/kernel/common/+/f118039ccd1a98d1c4931816832b28c3c9e8e471)\] | EoP | High | Direct Memory Access Buffer | 
| CVE-2026-58829 | A-498749316 [Upstream kernel](https://android.googlesource.com/kernel/common/+/984713cde654f06871c542c469e3c226c8a79d9b) \[[2](https://android.googlesource.com/kernel/common/+/517040c192cebb334766f43604e6a7ebb79d43ae)\] | EoP | High | FUSE | 
| CVE-2026-58844 | A-503384798 [Upstream kernel](https://android.googlesource.com/kernel/common/+/329d7c6e7215f52bb5922b4bcaa6bf713fa4ccff) \[[2](https://android.googlesource.com/kernel/common/+/f4633d3767965e89b835bca04981b67cc8aa78bd)\] \[[3](https://android.googlesource.com/kernel/common/+/8c62fa09cc8a04cbaaa5d00b5dcd51279bee3bdb)\] \[[4](https://android.googlesource.com/kernel/common/+/f0a3950f0fa3988e9af43b5656f72fa675672c82)\] \[[5](https://android.googlesource.com/kernel/common/+/7d6d4a26e7ead0bc501f3ed6809a66c2f3d49365)\] \[[6](https://android.googlesource.com/kernel/common/+/82cd807f41d89d5cf2b4c3ac7affdb91188baea7)\] \[[7](https://android.googlesource.com/kernel/common/+/2f86c81dc9453ed385c4f0703d6bd664d0997567)\] \[[8](https://android.googlesource.com/kernel/common/+/d518f4cc29a9a95f631c8c811fe6791ad08c4f56)\] \[[9](https://android.googlesource.com/kernel/common/+/d9b4efaed7a573d245dc5873c7d6c304a9936fdd)\] | EoP | High | Protected Kernel-Based Virtual Machine | 
| CVE-2026-58845 | A-498369302 [Upstream kernel](https://android.googlesource.com/kernel/common/+/3b9b40df51bda90ffb2833dcef11905e751dafdb) \[[2](https://android.googlesource.com/kernel/common/+/ed0e57e1e27a9eecd6c1a3dd1dd9ed1b8d1a06b4)\] | EoP | High | Memory Management | 
| CVE-2026-58847 | A-503385812 [Upstream kernel](https://android.googlesource.com/kernel/common/+/8c62fa09cc8a04cbaaa5d00b5dcd51279bee3bdb) | EoP | High | Protected Kernel-Based Virtual Machine | 
| CVE-2026-58942 | A-498371235 [Upstream kernel](https://android.googlesource.com/kernel/common/+/27d9c79c71ceaaee3c31337658a699364ec7d833) \[[2](https://android.googlesource.com/kernel/common/+/019d909caeb85547b9aed2beea73101ea73b958f)\] | EoP | High | Memory Management | 
| CVE-2026-59042 | A-503427706 [Upstream kernel](https://android.googlesource.com/kernel/common/+/1569a00286640e452ce917ee8b3cec04c5cc3715) \[[2](https://android.googlesource.com/kernel/common/+/382cffbd3842b64260993d2438926a9f2a0a447e)\] | EoP | High | pKVM | 
| CVE-2026-59043 | A-503379315 [Upstream kernel](https://android.googlesource.com/kernel/common/+/82cd807f41d89d5cf2b4c3ac7affdb91188baea7) | EoP | High | pKVM | 
| CVE-2026-64011 | A-500030631 [Upstream kernel](https://android.googlesource.com/kernel/common/+/be7eb82f26606f1965d7d4b053e82570ea5f48a1) \[[2](https://android.googlesource.com/kernel/common/+/e63aaa33966a89eca6ec07492b0525f0db045bc4)\] \[[3](https://android.googlesource.com/kernel/common/+/1188bc5d16e4f9511414b35b6c56a79f2a5d9529)\] \[[4](https://android.googlesource.com/kernel/common/+/0ad33340b17e71d9764987f0cd30530ad850e817)\] | EoP | High | NFC | 
| CVE-2026-64427 | A-489036052 [Upstream kernel](https://android.googlesource.com/kernel/common/+/17843f6d225d81b6f210b89bd54123611de7bba7) \[[2](https://android.googlesource.com/kernel/common/+/c47a6316399f7dfbddb1d383578838e3969ae90f)\] \[[3](https://android.googlesource.com/kernel/common/+/5db2dcc7b20c370157de9a46978d5a3d005b169c)\] \[[4](https://android.googlesource.com/kernel/common/+/6f13426533c438eaf78caf2a8171fc839417dd45)\] \[[5](https://android.googlesource.com/kernel/common/+/a1f098e5a82ad297062244ee20a44b6131c199c1)\] \[[6](https://android.googlesource.com/kernel/common/+/2b71b414641a5cac8a3bf2a736518e09a73badf5)\] | EoP | High | Human Interface Device | 
| CVE-2026-64560 | A-533808379 [Upstream kernel](https://android.googlesource.com/kernel/common/+/585f2c9c9560f7e0dadafbba251183cea83d9dc4) \[[2](https://android.googlesource.com/kernel/common/+/8eff909dd82da10a599468a514cc1ad07e90c3cc)\] | EoP | High | Kernel | 
| CVE-2026-46232 | A-508701836 [Upstream kernel](https://android.googlesource.com/kernel/common/+/a5dca2389c9e2e3c43bedb72f556bf0eafe0cffd) \[[2](https://android.googlesource.com/kernel/common/+/aab498d0885fd97d010a0cd1013a3479269f41d0)\] \[[3](https://android.googlesource.com/kernel/common/+/60eed3576bb0cf3ceb11625240beb63b48f6e3c2)\] \[[4](https://android.googlesource.com/kernel/common/+/cf8ba5678385b2b8832ed2e87c035925eb12bc4a)\] | ID | High | HID | 
| CVE-2026-23184 | A-468680876 [Upstream kernel](https://android.googlesource.com/kernel/common/+/1c8fffa12a81f62411312825521d63a81d1ca92e) | DoS | High | Binder | 
| CVE-2026-59046 | A-508541359 [Upstream kernel](https://android.googlesource.com/kernel/common/+/4a75aa4e840f294efd47084e083a6e91069bce58) \[[2](https://android.googlesource.com/kernel/common/+/525cfccadb92e7c9314d03cce600fed7335874d9)\] | DoS | High | pKVM | 
| CVE-2026-59047 | A-503393436 [Upstream kernel](https://android.googlesource.com/kernel/common/+/ba356506706b7bd953c501ea91ee7c0d55c1ad83) | DoS | High | pKVM | 

### Arm components

These vulnerabilities affect Arm components and further details are available directly from Arm. The severity assessment of these issues is provided directly by Arm.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2025-0647 | A-476123052 [\*](https://source.android.com#asterisk) |  | High | CPU | 
| CVE-2026-9040 | A-527031175 [\*](https://source.android.com#asterisk) |  | High | Mali | 
| CVE-2026-11891 | A-527047523 [\*](https://source.android.com#asterisk) |  | High | Mali | 

### Imagination Technologies

These vulnerabilities affect Imagination Technologies components and further details are available directly from Imagination Technologies. The severity assessment of these issues is provided directly by Imagination Technologies.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-22165 | A-489972410 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-65587 | A-542541019 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-15466 | A-531596246 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-16280 | A-508272003 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-18629 | A-524406423 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-19199 | A-545553862 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-41155 | A-499033076 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-45199 | A-520408029 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-45201 | A-530643753 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-45204 | A-524198442 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-65586 | A-508237844 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 
| CVE-2026-74912 | A-545799269 [\*](https://source.android.com#asterisk) |  | High | PowerVR-GPU | 

### MediaTek components

These vulnerabilities affect MediaTek components and further details are available directly from MediaTek. The severity assessment of these issues is provided directly by MediaTek.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-20499 | A-528209854 M-MOLY01857954 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20519 | A-541967271 M-MOLY01778993 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20520 | A-541967273 M-MOLY01778988 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20545 | A-557043202 M-MOLY01774038 [\*](https://source.android.com#asterisk) M-MOLY01879158 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20546 | A-557043203 M-MOLY01876654 [\*](https://source.android.com#asterisk) M-MOLY01774038 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20547 | A-557043204 M-MOLY01874018 [\*](https://source.android.com#asterisk) M-MOLY01774038 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20548 | A-557043205 M-MOLY01872867 [\*](https://source.android.com#asterisk) M-MOLY01774038 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20549 | A-557051694 M-MOLY01775865 [\*](https://source.android.com#asterisk) |  | Critical | Modem | 
| CVE-2026-20521 | A-541960865 M-ALPS11375674 [\*](https://source.android.com#asterisk) |  | High | Video HAL | 
| CVE-2026-20522 | A-541965929 M-ALPS11249050 [\*](https://source.android.com#asterisk) |  | High | neuropilot | 
| CVE-2026-20523 | A-541965931 M-ALPS11249062 [\*](https://source.android.com#asterisk) |  | High | neuropilot | 
| CVE-2026-20524 | A-541960867 M-ALPS11249004 [\*](https://source.android.com#asterisk) |  | High | apu | 
| CVE-2026-20526 | A-541967277 M-MOLY01898195 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20553 | A-557060234 M-ALPS11468968 [\*](https://source.android.com#asterisk) |  | High | DA | 
| CVE-2026-20554 | A-557065686 M-MOLY01911177 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20556 | A-557051697 M-MOLY01876662 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20557 | A-557051698 M-MOLY01877236 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20558 | A-557065687 M-ALPS11365070 [\*](https://source.android.com#asterisk) |  | High | GPU pdma | 
| CVE-2026-20559 | A-557051699 M-ALPS11365081 [\*](https://source.android.com#asterisk) |  | High | GPU pdma | 
| CVE-2026-20565 | A-557060238 M-MOLY01778991 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20586 | A-546432839 M-ALPS11383899 [\*](https://source.android.com#asterisk) |  | High | vdec | 
| CVE-2026-20589 | A-546432840 M-ALPS11383899 [\*](https://source.android.com#asterisk) |  | High | vdec | 
| CVE-2026-20525 | A-541960869 M-MOLY01870473 [\*](https://source.android.com#asterisk) M-MOLY00814393 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20527 | A-541967278 M-MOLY01864925 [\*](https://source.android.com#asterisk) M-MOLY01210562 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20555 | A-557051696 M-MOLY01876664 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20560 | A-557065688 M-MOLY01870543 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20561 | A-557060235 M-MOLY01750090 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20562 | A-557060236 M-MOLY01775984 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20563 | A-557051700 M-MOLY01777997 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-20564 | A-557060237 M-MOLY01780439 [\*](https://source.android.com#asterisk) |  | High | Modem | 

### Unisoc components

These vulnerabilities affect Unisoc components and further details are available directly from Unisoc. The severity assessment of these issues is provided directly by Unisoc.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-66086 | A-539342791 U-3406715 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-79405 | A-553145530 U-3457076 [\*](https://source.android.com#asterisk) |  | High | Modem | 
| CVE-2026-80335 | A-553139427 U-3502927 [\*](https://source.android.com#asterisk) |  | High | uboot | 
| CVE-2026-80336 | A-553139428 U-3502931 [\*](https://source.android.com#asterisk) |  | High | uboot | 

### Qualcomm components

These vulnerabilities affect Qualcomm components and are described in further detail in the appropriate Qualcomm security bulletin or security alert. The severity assessment of these issues is provided directly by Qualcomm.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-25291 | A-532129554 [QC-CR#4403192](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/c6c74d057c0c1d128ad30da9460765bc02ea85f4) |  | High | Security | 
| CVE-2026-25301 | A-542224505 [QC-CR#4424931](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/be1b91c10f5d045f608e88e99598766f3865bfef) |  | High | Security | 
| CVE-2026-57537 | A-532130350 [QC-CR#4252624](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/dsp-kernel/-/commit/3dacc0ac01d64242ffb367c949b36b3e54368950) |  | High | Security | 
| CVE-2026-57545 | A-532130662 [QC-CR#4478735](https://git.codelinaro.org/clo/la/kernel/msm-5.10/-/commit/874311dc075047c51c9231e3de1bae0a7677b3b7) |  | High | Security | 
| CVE-2026-57548 | A-542224386 [QC-CR#4488190](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/af2e26b0b01a5ca8ef30bf20ee17a1360563bb70) \[[2](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/73214990504422a964b091964cde3c59780b7ff2)\] |  | High | Security | 
| CVE-2026-57549 | A-542225265 [QC-CR#4491000](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/graphics-kernel/-/commit/9f382f0cbb0c69b0ddc90e298ca5226b4ecd80a9) |  | High | Security | 
| CVE-2026-57554 | A-532129432 [QC-CR#4499506](https://git.codelinaro.org/clo/la/platform/vendor/qcom/opensource/dsp-kernel/-/commit/f6ddd79f650d61c7406faf52530d1a4716a5613a) \[[2](https://git.codelinaro.org/clo/la/kernel/msm-5.15/-/commit/099b47ce9f7d0104ef131b1e7b407367c756bf72)\] \[[3](https://git.codelinaro.org/clo/la/kernel/msm-5.10/-/commit/a065d4bacdae2cea6678a7528df8008d16452a63)\] |  | High | Security | 
| CVE-2026-66113 | A-542225657 [QC-CR#4531192](https://git.codelinaro.org/clo/la/platform/vendor/opensource/display-core/-/commit/1d51d6c52ccc5e9ac759aded27a4ec62a7ccf702) |  | High | Security | 
| CVE-2026-66114 | A-542225732 [QC-CR#4532353](https://git.codelinaro.org/clo/la/platform/vendor/opensource/display-core/-/commit/0a615ffd20a5677ca18acb53e9b4b1292b836078) |  | High | Security | 

### Qualcomm closed-source components

These vulnerabilities affect Qualcomm closed-source components and are described in further detail in the appropriate Qualcomm security bulletin or security alert. The severity assessment of these issues is provided directly by Qualcomm.

| CVE | References |  | Severity | Subcomponent | 
|---|---|---|---|---|
| CVE-2026-25285 | A-509524400 [\*](https://source.android.com#asterisk) |  | Critical | Closed-source component | 
| CVE-2026-6726 | A-542224547 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-25286 | A-509524956 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-25287 | A-509525554 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-25302 | A-532130009 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-57546 | A-532130527 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-57547 | A-532130053 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 
| CVE-2026-65076 | A-542225318 [\*](https://source.android.com#asterisk) |  | High | Closed-source component | 

## Common questions and answers

This section answers common questions that may occur after reading this bulletin.

**1. How do I determine if my device is updated to address these
issues?**

To learn how to check a device's security patch level, see
[Check and update your Android version](https://support.google.com/pixelphone/answer/4457705#pixel_phones&nexus_devices).

- Security patch levels of 2026-11-01 or later address all issues associated with the 2026-11-01 security patch level.
- Security patch levels of 2026-11-05 or later address all issues associated with the 2026-11-05 security patch level and all previous patch levels.

Device manufacturers that include these updates should set the patch string level to:

- \[ro.build.version.security\_patch\]:\[2026-11-01\]
- \[ro.build.version.security\_patch\]:\[2026-11-05\]

For some devices on Android 10 or later, the Google Play system update
will have a date string that matches the 2026-11-01
security patch level.
Please see [this article](https://support.google.com/android/answer/7680439) for more details on how to install
security updates.

**2. Why does this bulletin have two security patch levels?**

This bulletin has two security patch levels so that Android partners have the flexibility to fix a subset of vulnerabilities that are similar across all Android devices more quickly. Android partners are encouraged to fix all issues in this bulletin and use the latest security patch level.

- Devices that use the 2026-11-01 security patch level must include all issues associated with that security patch level, as well as fixes for all issues reported in previous security bulletins.
- Devices that use the security patch level of 2026-11-05 or newer must include all applicable patches in this (and previous) security bulletins.

Partners are encouraged to bundle the fixes for all issues they are addressing in a single update.

**3. What do the entries in the *Type* column mean?**

Entries in the *Type* column of the vulnerability details table
reference the classification of the security vulnerability.

| Abbreviation | Definition | 
|---|---|
| RCE | Remote code execution | 
| EoP | Elevation of privilege | 
| ID | Information disclosure | 
| DoS | Denial of service | 
| N/A | Classification not available | 

**4. What do the entries in the *References* column mean?**

Entries under the *References* column of the vulnerability details
table may contain a prefix identifying the organization to which the reference
value belongs.

| Prefix | Reference | 
|---|---|
| A- | Android bug ID | 
| QC- | Qualcomm reference number | 
| M- | MediaTek reference number | 
| N- | NVIDIA reference number | 
| B- | Broadcom reference number | 
| U- | UNISOC reference number | 

**5. What does an \* next to the Android bug ID in the *References*
column mean?**

Issues that are not publicly available have an \* next to the corresponding
reference ID. The update for that issue is generally contained in the latest
binary drivers for Pixel devices available from the
[Google Developer site](https://developers.google.com/android/drivers).

**6. Why are security vulnerabilities split between this bulletin and
device / partner security bulletins, such as the
Pixel bulletin?**

Security vulnerabilities that are documented in this security bulletin are
required to declare the latest security patch level on Android
devices. Additional security vulnerabilities that are documented in the
device / partner security bulletins are not required for
declaring a security patch level. Android device and chipset manufacturers
may also publish security vulnerability details specific to their products,
such as
[Google](https://source.android.com/security/bulletin/pixel),
[Huawei](https://consumer.huawei.com/en/support/bulletin/),
[LGE](https://lgsecurity.lge.com/security_updates_mobile.html),
[Motorola](https://motorola-global-portal.custhelp.com/app/software-security-page/g_id/6806),
[Nokia](https://www.nokia.com/phones/en_int/security-updates), or
[Samsung](https://security.samsungmobile.com/securityUpdate.smsb).

## Versions

| Version | Date | Notes | 
|---|---|---|
| 1.0 | November 2, 2026 | Bulletin Published | 
| 1.1 | November 6, 2026 | Issues list updated |
