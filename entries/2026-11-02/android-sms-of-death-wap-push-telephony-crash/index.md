---
schema: 1
kind: vulnerability
title: "Android telephony ('SMS of Death'): one hidden WAP Push message crashes the phone process and drops calls, emergency calls included; fixed for Android 14 to 17 at the 2026-11-01 security patch level per Google's bulletin row for CVE-2026-58882, the identifier BleepingComputer gives; Android 12 and 13 stay exposed, public proof of concept"
headline: "Android 'SMS of Death': one hidden SMS drops calls, emergency calls included; Android 12 and 13 get no fix"
summary: >
  An independent researcher published a working proof of concept on 2026-10-29 for a zero-click remote denial of service in Android's
  telephony framework: one malformed WAP Push data message crashes the com.android.phone process, drops active calls including emergency
  calls and, because the message is retried, can leave a phone in a restart loop. Google's November 2026 bulletin lists CVE-2026-58882, the
  identifier BleepingComputer gives for the flaw, as a critical denial of service fixed at the 2026-11-01 security patch level for Android
  14 to 17 (the researcher had named the October update); Android 12 and 13 phones run the same code unfixed, and no source reports exploitation.
discovered_at: "2026-11-02T03:46:00Z"
updated_at: "2026-11-08T13:58:09Z"
event_date: "2026-10-29"
run_id: 2026-11-02T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, zero-click, dos, poc-public, patch-available, mobile]
regions: [global]
sectors: [public-sector]
entities: ["tool:sms-of-death-poc", "product:google-android"]
techniques: [T1499.004]
affected_products: ["Google Android"]
cves:
  - id: CVE-2026-58882
    cvss: null
    epss: null
    type: dos
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "Android 14, 15, 16, 16-qpr2 and 17 below the 2026-11-01 security patch level (Google); Android 12 and 13, which receive no fix (researcher)"
    fixed: "2026-11-01 security patch level (Google's November 2026 bulletin); the researcher says the fix shipped in the October 2026 update"
sources:
  - url: "https://smsofdeath.com/"
    publisher: "Mark B (smsofdeath.com)"
    date: "2026-10-29"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/"
    publisher: "BleepingComputer"
    date: "2026-10-31"
    role: corroborating
  - url: "https://securityaffairs.com/202184/security/sms-of-death-android-under-attack-an-invisible-sms-can-block-calls-and-emergency-services.html"
    publisher: "Security Affairs"
    date: "2026-11-01"
    role: corroborating
  - url: "https://source.android.com/docs/security/bulletin/2026/2026-11-01"
    publisher: "Google (Android Security Bulletin, November 2026)"
    date: "2026-11-02"
    role: primary
closed_sources: []
evidence:
  - quote: "The message is delivered as a data SMS and is never shown to the user: there is nothing in the inbox, and the victim never sees the sender's number."
    publisher: "Mark B (smsofdeath.com)"
    source_url: "https://smsofdeath.com/"
  - quote: "Devices updated to the October 2026 patch level or later are protected; devices on earlier patch levels remain vulnerable."
    publisher: "Mark B (smsofdeath.com)"
    source_url: "https://smsofdeath.com/"
  - quote: "the flaw is not listed in Google's October security bulletin, and older Android 12 and 13 devices remain vulnerable because they did not receive the fix."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/"
verification: single-source
sourcing_note: >
  The researcher's page signs only "Mark B"; Security Affairs gives the surname Blaszczyk and BleepingComputer writes Mark Blah. The mechanism, the reproduction on Android 12 to 16 and the statement that the fix reached Android 14 to 17 in the October 2026 update are the
  researcher's; BleepingComputer and Security Affairs restate them, and BleepingComputer describes Google's fix and reports that Google's October
  bulletin does not list it, and the researcher names no CVE. BleepingComputer gives the identifier CVE-2026-58882, and Google's November 2026 bulletin, published
  on 2026-11-02, lists that identifier as a critical denial of service in the System component for Android 14 to 17; the
  bulletin row gives no flaw description, so the link between the identifier and this flaw rests on BleepingComputer.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Move every managed Android phone below the 2026-11-01 security patch level to that level or later, phones of emergency-service and on-call staff first."
updates:
  - at: "2026-11-08T13:58:09Z"
    run_id: 2026-11-08T1309Z-audit
    type: update
    summary: >
      Google's November 2026 Android bulletin lists CVE-2026-58882, the identifier given for the SMS of
      Death flaw, as a critical denial of service fixed at the 2026-11-01 security patch level for Android
      14 to 17, so that level, not the researcher's October update, is the vendor-stated fix level.
    fields: [actions, body, cves, sources, sourcing_note, summary, title]
migrated_from: null
---

A researcher who signs as Mark B published a working proof-of-concept app on 2026-10-29 for a zero-click remote denial of service in Android's telephony framework ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). One malformed WAP Push data message to port 2948 makes `WapPushOverSms.decodeWapPdu()` cast a 64-bit header length to a signed 32-bit integer and allocate a negative-sized array; the uncaught `NegativeArraySizeException` kills the `com.android.phone` process, which drops active calls, emergency calls included, and cuts service for one to two seconds per message ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The poison message stays in the pending queue and is retried on every boot and on carrier redelivery: the researcher reports that about 20 messages leave a device unusable and that one Android 12 phone rebooted into recovery roughly every 90 seconds until the messages were deleted over ADB ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The crash reproduced on Android 12 to 16, on a Pixel 9 and on Samsung Galaxy and A-series phones ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)); Security Affairs restates the mechanism and the October fix for Android 14 to 17 ([Security Affairs, 2026-11-01](https://securityaffairs.com/202184/security/sms-of-death-android-under-attack-an-invisible-sms-can-block-calls-and-emergency-services.html)).

Google's fix, titled "Fix remote DoS in decodeWapPdu", catches the exceptions the malformed messages trigger and deletes the malicious messages from the SMS database ([BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)); per the researcher it shipped in the October 2026 update for Android 14 to 17, so Android 12 and 13 phones outside the update window run the same code unfixed ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). Google's November 2026 bulletin lists CVE-2026-58882, the identifier BleepingComputer gives, as a critical denial of service in the System component fixed at the 2026-11-01 security patch level for Android 14, 15, 16, 16-qpr2 and 17 ([Google, 2026-11-02](https://source.android.com/docs/security/bulletin/2026/2026-11-01); [BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)). BleepingComputer adds that the fix is not listed in Google's October bulletin ([BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)). The proof-of-concept app and its source are public ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/); [BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)), and none of the sources reports use in the wild.

**Exposure:** any Android phone below the 2026-11-01 security patch level, which Google names as the fix level of CVE-2026-58882, BleepingComputer's identifier for the flaw ([Google, 2026-11-02](https://source.android.com/docs/security/bulletin/2026/2026-11-01)), and Android 12 and 13 phones outside the security-update window, which receive no fix; the attack needs only the target's phone number ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The patch level in device-management inventory shows which handsets have the fix.

**Detection:** on managed handsets, repeated crashes of the `com.android.phone` process in the device log, with a `NegativeArraySizeException` raised in `WapPushOverSms.decodeWapPdu`, calls that end with disconnect cause `CS_DEATH`, and a phone that restarts into recovery about every 90 seconds ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)); the message never appears in the inbox and the sender is not shown, so the crash log is the only trace on the phone.

**Triage:** a single telephony restart has many benign causes; a restart that recurs on every boot or on each carrier redelivery, with the exception above in the crash log, matches this flaw.

**Defender takeaway:** move every managed Android handset to the 2026-11-01 security patch level or later, emergency-service and on-call staff first, and list for replacement the Android 12 and 13 phones outside the security-update window, which receive no fix and stay crashable by one message. A phone stuck in the loop should not be wiped from the recovery prompt: the researcher documents deleting the pending WAP Push rows over ADB from a computer, which avoids a factory reset ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)).

## Update — 2026-11-08T13:58:09Z

Google's Android Security Bulletin for November 2026, published on 2026-11-02, lists CVE-2026-58882 in the System component as a critical denial of service with updated AOSP versions 14, 15, 16, 16-qpr2 and 17, fixed at the 2026-11-01 security patch level ([Google, 2026-11-02](https://source.android.com/docs/security/bulletin/2026/2026-11-01)). BleepingComputer gives CVE-2026-58882 as the identifier of the SMS of Death flaw ([BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)). On BleepingComputer's identifier, the vendor-stated fix level is 2026-11-01, a month later than the October update the researcher names; handsets on the October level are not covered by Google's statement. Android 12 and 13 do not appear among the updated versions ([Google, 2026-11-02](https://source.android.com/docs/security/bulletin/2026/2026-11-01)).
