---
schema: 1
kind: vulnerability
title: "CVE-2026-94504 / CVE-2026-93836, Ninja Forms and WPC Product Bundles for WooCommerce: stored XSS exploited to plant a hidden WordPress administrator and four persistence routes that survive the update"
headline: "Exploited WordPress plugin XSS ends in a hidden admin and persistence that patching does not remove"
summary: >
  Patchstack reports that since 2026-10-04 one campaign has been exploiting two unrelated stored cross-site scripting flaws,
  CVE-2026-93836 in WPC Product Bundles for WooCommerce up to 8.6.6 and CVE-2026-94504 in Ninja Forms up to 3.15.3, by planting
  a script in an order or a form submission that runs when a logged-in administrator opens it. The script uses the
  administrator's own session to install a malicious plugin and create administrators, one of them hidden from the Users
  screen, and leaves four independent ways back in, so updating to Ninja Forms 3.15.4 or WPC Product Bundles 8.6.7 stops new
  injections but does not evict an implant. Patchstack says exploitation volume is limited so far and that the second stage
  works with any stored XSS that reaches an administrator.
discovered_at: "2026-10-07T04:45:00Z"
updated_at: null
event_date: "2026-10-06"
run_id: 2026-10-07T0404Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, pre-auth, actively-exploited, patch-available]
regions: [global]
sectors: [technology, public-sector]
entities: ["product:ninja-forms", "product:wpc-product-bundles-for-woocommerce"]
techniques: [T1190, T1059.007, T1185, T1136, T1505.003, T1070.006, T1027, T1105]
affected_products: ["Ninja Forms", "WPC Product Bundles for WooCommerce"]
cves:
  - id: CVE-2026-94504
    cvss: "7.2"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "Ninja Forms up to and including 3.15.3"
    fixed: "3.15.4"
  - id: CVE-2026-93836
    cvss: "7.2"
    epss: null
    type: xss
    vector: user-interaction
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "WPC Product Bundles for WooCommerce up to and including 8.6.6"
    fixed: "8.6.7"
sources:
  - url: "https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/"
    publisher: "Patchstack"
    date: "2026-10-06"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/ninja-forms-plugin-flaw-exploited-to-hack-wordpress-sites/"
    publisher: "BleepingComputer"
    date: "2026-10-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "exploitation volume remains limited in our telemetry"
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/"
  - quote: "It is a fully privileged administrator the site owner cannot see."
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/"
  - quote: "Removing the vulnerable plugin, or even the malicious one, closes none of the last three."
    publisher: "Patchstack"
    source_url: "https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/"
  - quote: "Updating the vulnerable plugin prevents further exploitation but does not clean an existing infection."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/ninja-forms-plugin-flaw-exploited-to-hack-wordpress-sites/"
verification: single-source
sourcing_note: >
  The exploitation claim rests on Patchstack's own telemetry; BleepingComputer restates Patchstack and adds nothing independent.
  BleepingComputer says both flaws require an authenticated session, while Patchstack's analysis shows an unauthenticated
  attacker planting the script and the authenticated session being the administrator's, and Patchstack's account is followed. The
  CVSS 3.1 score of 7.2 for each flaw is the Wordfence CNA record's; Patchstack's database lists 7.1. The WPC Product Bundles fix
  version is Patchstack's reading of the plugin's upstream changelog.
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
  - "Update Ninja Forms to 3.15.4 or later and WPC Product Bundles for WooCommerce to 8.6.7 or later on every WordPress site, then check each site for an implant the update does not remove, starting with a comparison of the database's administrator list against the Users screen and an inspection of the must-use plugins directory by content."
  - "On any site where an administrator opened a Ninja Forms submission or a WooCommerce order since 2026-10-04 and an implant turns up, rotate all privileged credentials and the WordPress authentication salts and treat the oldest administrator account as compromised, because a login URL planted by the implant authenticates as that account."
updates: []
migrated_from: null
---

Patchstack reports two unrelated stored cross-site scripting flaws that deliver the same second-stage script, first seen on 2026-10-04 against WPC Product Bundles for WooCommerce (CVE-2026-93836) and on 2026-10-05 against Ninja Forms (CVE-2026-94504) ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). No account is needed: a numeric-prefixed quantity keeps attacker markup in WooCommerce order data, and a textarea submission sent through the normal form endpoint is stored and rendered without safe encoding in the legacy Ninja Forms submission editor ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). The script runs when a logged-in administrator opens the order or submission, rides that session in wp-admin without reading the cookie, so HttpOnly does not help ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)).

With that session it uploads a plugin through WordPress' own installer, creates an administrator and calls a persistence installer ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). Patchstack counts four ways back in: the visible administrator; a second administrator that a dropped must-use plugin hides from the Users list, its filters and its role counts; a login URL, backed by another must-use plugin, that authenticates as the site's oldest administrator; and an unauthenticated file manager in the uploaded plugin that runs only on a direct request and can write files anywhere writable ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). The must-use plugins are backdated to the oldest file time in the WordPress root, so a search for recently changed files misses them ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)).

Both flaws were disclosed on 2026-09-22; Patchstack says exploitation volume is limited and that the second stage works with any stored XSS that reaches an administrator ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). The fixed versions are Ninja Forms 3.15.4 and WPC Product Bundles 8.6.7, and updating does not clean an existing infection ([BleepingComputer, 2026-10-06](https://www.bleepingcomputer.com/news/security/ninja-forms-plugin-flaw-exploited-to-hack-wordpress-sites/)).

**Exposure:** WordPress sites running Ninja Forms 3.15.3 or older, or WPC Product Bundles for WooCommerce 8.6.6 or older, where an administrator opens form submissions or orders in wp-admin ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)).

**Detection:** in web server logs, public POSTs to the plugin's form-submit endpoint or to a product URL whose fields carry script or an image error handler that loads a remote script; in WordPress audit and database records, a plugin-upload install, a user creation and a call to a persistence installer around the time an administrator opens a submission or an order, administrator rows in the users and metadata tables that the Users screen does not list, PHP files under the must-use plugins directory that the Plugins screen never shows, and requests to the login page carrying a token parameter ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)). Updating does not evict an implant: Patchstack says to remove the unauthorised accounts and plugins and the dropped files, rotate privileged credentials and authentication salts, and treat the oldest administrator's password as compromised even though it was never directly stolen ([Patchstack, 2026-10-06](https://patchstack.com/articles/four-ways-back-in-the-wordpress-xss-campaign-that-hides-its-own-admin-account/)).

**Triage:** a legitimate administrator installing a plugin from a ZIP produces the same plugin-install and user-creation events; the discriminators are that they follow an administrator opening a stored submission or order, that the installed plugin poses as a thumbnail cache and does nothing when WordPress loads it, and that the new administrator is missing from the Users list.

**Defender takeaway:** update both plugins now, then treat any site where an administrator opened a stored order or submission since 2026-10-04 as possibly compromised until the database administrator list, the must-use plugins and the oldest administrator's credentials have been checked, because the patch closes the injection and none of the persistence routes.
