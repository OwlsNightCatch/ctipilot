---
schema: 1
kind: vulnerability
title: "Android telephony ('SMS of Death'): one hidden WAP Push message crashes the phone process and drops calls, emergency calls included; fixed for Android 14 to 17 in the October 2026 update according to the researcher, Android 12 and 13 stay exposed, public proof of concept"
headline: "Android 'SMS of Death': one hidden SMS drops calls, emergency calls included; Android 12 and 13 get no fix"
summary: >
  An independent researcher published a working proof of concept on 2026-10-29 for a zero-click remote denial of service in Android's
  telephony framework: one malformed WAP Push data message crashes the com.android.phone process, drops active calls including emergency
  calls and, because the message is retried, can leave a phone in a restart loop. Per the researcher, Google's fix shipped in the October 2026
  update for Android 14 to 17, so Android 12 and 13 phones run the same code unfixed; no source reports exploitation.
discovered_at: "2026-11-02T03:46:00Z"
updated_at: null
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
cves: []
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
  bulletin does not list it, so which release carries the fix rests on the researcher's word. BleepingComputer gives the identifier
  CVE-2026-58882; no CVE record by that number exists and the researcher names none.
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
  - "Install the October 2026 Android security update on every managed Android phone below that patch level, phones of emergency-service and on-call staff first."
updates: []
migrated_from: null
---

A researcher who signs as Mark B published a working proof-of-concept app on 2026-10-29 for a zero-click remote denial of service in Android's telephony framework ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). One malformed WAP Push data message to port 2948 makes `WapPushOverSms.decodeWapPdu()` cast a 64-bit header length to a signed 32-bit integer and allocate a negative-sized array; the uncaught `NegativeArraySizeException` kills the `com.android.phone` process, which drops active calls, emergency calls included, and cuts service for one to two seconds per message ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The poison message stays in the pending queue and is retried on every boot and on carrier redelivery: the researcher reports that about 20 messages leave a device unusable and that one Android 12 phone rebooted into recovery roughly every 90 seconds until the messages were deleted over ADB ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The crash reproduced on Android 12 to 16, on a Pixel 9 and on Samsung Galaxy and A-series phones ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)); Security Affairs restates the mechanism and the October fix for Android 14 to 17 ([Security Affairs, 2026-11-01](https://securityaffairs.com/202184/security/sms-of-death-android-under-attack-an-invisible-sms-can-block-calls-and-emergency-services.html)).

Google's fix, titled "Fix remote DoS in decodeWapPdu", catches the exceptions the malformed messages trigger and deletes the malicious messages from the SMS database ([BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)); per the researcher it shipped in the October 2026 update for Android 14 to 17, so Android 12 and 13 phones outside the update window run the same code unfixed ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). BleepingComputer adds that the fix is not listed in Google's October bulletin ([BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)). The proof-of-concept app and its source are public ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/); [BleepingComputer, 2026-10-31](https://www.bleepingcomputer.com/news/security/new-android-sms-of-death-exploit-can-remotely-crash-unpatched-phones/)), and none of the sources reports use in the wild.

**Exposure:** any Android phone on a patch level before October 2026, and Android 12 and 13 phones outside the security-update window, which receive no fix; the attack needs only the target's phone number ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)). The patch level in device-management inventory shows which handsets have the fix.

**Detection:** on managed handsets, repeated crashes of the `com.android.phone` process in the device log, with a `NegativeArraySizeException` raised in `WapPushOverSms.decodeWapPdu`, calls that end with disconnect cause `CS_DEATH`, and a phone that restarts into recovery about every 90 seconds ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)); the message never appears in the inbox and the sender is not shown, so the crash log is the only trace on the phone.

**Triage:** a single telephony restart has many benign causes; a restart that recurs on every boot or on each carrier redelivery, with the exception above in the crash log, matches this flaw.

**Defender takeaway:** move every managed Android handset to the October 2026 patch level, emergency-service and on-call staff first, and list for replacement the Android 12 and 13 phones outside the security-update window, which receive no fix and stay crashable by one message. A phone stuck in the loop should not be wiped from the recovery prompt: the researcher documents deleting the pending WAP Push rows over ADB from a computer, which avoids a factory reset ([smsofdeath.com, 2026-10-29](https://smsofdeath.com/)).
