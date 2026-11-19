---
title: Smart form protection
url: https://docs.airlock.com/gateway/latest/index/1648621032215.html
hostname: airlock.com
sitename: docs.airlock.com
fingerprint: d6129c796573f6bd
---
# Smart form protection

In addition to URL encryption, it is possible to sign, and therefore protect, all form information of a web application. With the innovative (patent pending) Airlock Gateway Smart Form Protection technology, Airlock Gateway will only accept user input parameters matching the meta constraints contained in the original HTML form. The dynamic form protection technology greatly improves the protection against forceful browsing attacks. A user can only send those form parameters back to the server which was originally requested by the server. An attacker can not add other parameters to manipulate the back-end application.

**Example case:**

If an application provides an HTML form where a user can enter the amount and select the currency to create an electronic payment, he will not be able to send any other parameters or send a currency that is not in the offered option list. All constraints are strictly enforced by Airlock. The back-end application will only get requests and user input data that it actually requested, and which it can safely deal with.

To activate Airlock Gateway Smart Form Protection, it is necessary to activate [URL encryption](https://docs.airlock.com/1583435029758.html) (PBE or session-based) first.
