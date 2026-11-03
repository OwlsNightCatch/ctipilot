# extract: served via trafilatura-direct
---
title: WordPress doesn't ship Brotli. It's still exposed to CVE-2026-111497 - Patchstack
author: Patchstack
url: https://patchstack.com/articles/wordpress-doesnt-ship-brotli-its-still-exposed-to-cve-2026-111497/
hostname: patchstack.com
description: One unauthenticated POST to xmlrpc.php can take down a PHP worker on a stock WordPress install, and there is nothing unusual about the request that does it. The
sitename: Patchstack
date: "2026-10-30"
categories: ['Security Advice', 'WordPress Security']
fingerprint: b0b591119b240e10
---
One unauthenticated POST to `xmlrpc.php` can take down a PHP worker on a stock WordPress install, and there is nothing unusual about the request that does it. The attacker sends a pingback whose source URL points at a server they own. WordPress goes and fetches that URL, the server answers with a Brotli-compressed body, and `libcurl` unpacks it before WordPress sees a single byte of it. On current builds, that unpacking writes past the end of its buffer.

The flaw is [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/CVE-2026-111497), an out-of-bounds write in [Google’s Brotli decoder](<Broccoli2Shell: Brotli decoder RCE (CVE-2026-111497) in Node.js, Python and more>). Google assigned the CVE and scored it 9.2. It covers Brotli 1.0.3 through 1.2.0 and was fixed on 21 October 2026 in 1.0.10, 1.1.1 and 1.2.1. CISA added it to the Known Exploited Vulnerabilities catalog on 27 October and gave federal agencies until 10 November to deal with it.

WordPress doesn’t ship Brotli. It links whatever the operating system provides, through `libcurl`, on every outbound request it makes. So, there is nothing to update in WordPress, no plugin to upgrade, and nothing in the inbound request that marks the attack, because the payload never travels in the request. It comes back in the reply from the attacker’s server.

What you can do is close the routes that reach the decoder and change how WordPress asks for responses in the first place. Both are below. Turning off XML-RPC shuts the easiest door and leaves the rest open.

| **Path to the decoder** | **Requirements** | **What the attacker controls** | 
| `pingback.ping` over `xmlrpc.php`, which calls `wp_safe_remote_get()` | Nothing (Unauthenticated), plus a pingable published post, which a default install has | The source URL WordPress fetches, and so the response it decodes | 
| A plugin/theme calling `wp_remote_get()` or `wp_safe_remote_get()` on a user-supplied address | Whatever that plugin’s/theme’s endpoint requires, which is often nothing | The URL, and so the response | 
| oEmbed discovery on save, or the oEmbed proxy endpoint | A Contributor+ account | The embed URL | 
| Feed fetch through SimplePie | An admin-configured feed | The feed URL | 

## How WordPress Reaches the Decoder

Every outbound request WordPress makes goes through `WP_Http`, the bundled Requests library and its cURL transport. That transport sets `CURLOPT_ENCODING` to an empty string in its constructor, on every handle, with no way to opt out. An empty value is libcurl’s “accept any compression and unpack it for me”, so a reply marked `Content-Encoding: br` goes into the Brotli decoder inside `curl_exec()`. Setting `decompress => false` won’t save you, because that only tells WordPress what to do with a body libcurl has already unpacked.

A malformed stream makes the decoder write past its buffer into whatever heap memory sits next to it. Crashing it is easy and works on any build, so one request can kill a worker and a few hundred can keep a site down. Code execution is a different matter and has to be built per target.

Researchers have working shells against stock Node.js and Bun binaries, and public proofs of concept are going around, but those chains lean on a fixed offset in one specific non-PIE build and on guessing a socket number, and they fall over on anything else. PHP behind Apache or FPM is not that target, and no public chain aims at it yet. Public tooling for the WordPress path does exist, but it stops at the crash.

A lab published on 27 October drives the bug through pingback and documents two outcomes: a worker killed outright, and a worker pinned at 100% CPU by a payload of well under a hundred bytes. Its author is explicit that no code execution is included and that blind remote RCE is not established. So the denial of service is now copy and paste, and the hard part is still hard. Hard is not the same as out of reach, though. Offsets have to be worked out once per build rather than once per victim, and nobody doing that work is obliged to publish it.

The thing to plan around today is crashed workers and the downtime that comes with them. Memory disclosure and code execution are harder, and they are what the 9.2 accounts for.

### The Unauthenticated Path

`pingback.ping` sits in the default XML-RPC method map and needs no account. It takes a source URL, and `pingback_ping()` fetches it with `wp_safe_remote_get()`. A stock install has XML-RPC on, `default_ping_status` set to open and at least one pingable post, so the attacker only has to point the source at their own server and answer with the bad stream. The worker that picked up the request decodes it and dies.

Plenty of sites never had this route open in the first place. Managed hosts often block `xmlrpc.php` at the edge, and hardening snippets have been switching it off for years, so there’s a fair chance it’s already shut on your install. Confirm that rather than assume it, because “XML-RPC is disabled” covers two different things. A block at the web server closes the route. The one-line `xmlrpc_enabled` filter, which is what a lot of plugin toggles use underneath, does not: it gates the methods that need a login, and pingback isn’t one of them. A site running that filter answers a pingback exactly the way an untouched site does.

One request tells you which of the two you have. The source address below is a local one that WordPress rejects before it fetches anything, so this is safe to point at your own site:

```
curl -s -i -X POST https://example.com/xmlrpc.php \
  -H 'Content-Type: text/xml' \
  --data '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://127.0.0.1/</string></value></param><param><value><string>https://example.com/?p=1</string></value></param></params></methodCall>'
```
A 403, a 404, or anything that isn’t XML, means the route is blocked and this path doesn’t apply to you. A fault reading `requested method pingback.ping does not exist` means the method has been unregistered, which also closes it. Any other `methodResponse`, fault or not, means `pingback_ping()` ran and the route is open. None of this touches the plugin, oEmbed and feed paths in the table above, so a closed pingback route narrows what you’re exposed to rather than removing it.

### The Plugin Paths

Because the problem is in the transport, it isn’t confined to XML-RPC. Any plugin that fetches a visitor-supplied address server-side lands in the same decoder: link previews, URL and image importers, webhook verifiers, avatar proxies. The safe wrapper doesn’t help you here. All `wp_safe_remote_get()` adds over `wp_remote_get()` is `reject_unsafe_urls`, an SSRF filter that rejects internal IPs and any port other than 80, 443 and 8080. It never looks at `Content-Encoding`, so an ordinary attacker server on 443 walks straight past it.

## Why a WAF Can’t See It in the Request

A WAF makes its decision from what the visitor sent, and that is the one place this attack isn’t. A `pingback.ping`, or a plugin call, carries a URL and little else, and the URL looks like any other. The interesting part arrives later, from the attacker’s own server. To separate this request from a legitimate one, a WAF would have to fetch the URL itself and decode the Brotli reply, which is the step that crashes. A PHP firewall can’t get that far anyway: it runs inside WordPress, and the decode happens underneath it in `libcurl`, before any PHP executes. Here is the exchange, and where a rule could act:

| **Step** | **What happens on the wire** | **What a WAF can do about it** | 
| 1 | Attacker sends `POST /xmlrpc.php`, a `pingback.ping` whose source is `https://attacker.example/x` | It sees the request, and it can block pingback outright. What it can’t do is tell this pingback from a real one. | 
| 2 | WordPress runs its SSRF check; a public `https` host on 443 passes | Nothing to do. The URL is allowed by design. | 
| 3 | WordPress fetches `https://attacker.example/x` (outbound) | Usually blind to egress. This isn’t an inbound request. | 
| 4 | The attacker’s server replies with `Content-Encoding: br` and a malformed stream | Too late. The request was already allowed, and the payload is in this reply. | 
| 5 | `libcurl` hands the body to the Brotli decoder, which writes out of bounds | Below PHP. Nothing left to intercept. | 

The only step a rule can touch is the first, and there the attack is indistinguishable from a real pingback. So, the rule has to remove the whole method rather than the attack. That is worth doing, and it’s the second option below, but it closes one route. It doesn’t reach the bug, and it does nothing about the plugin paths.

## Fixing It

Update Brotli and rebuild the image. It’s the only change that reaches the vulnerable code, which makes it the only thing that actually fixes this. Move to 1.0.10, 1.1.1 or 1.2.1, or take your distribution’s security update for `libbrotli1`. Two things make the check less obvious than it sounds.

Pulling the official image again won’t currently help you. `wordpress:latest` still installs a vulnerable `libbrotli1` today. Until the base image is rebuilt, upgrade the package in your own layer:

```
FROM wordpress:latest
RUN apt-get update \
 && apt-get install -y --no-install-recommends --only-upgrade libbrotli1 \
 && rm -rf /var/lib/apt/lists/*
```
And the upstream version number won’t tell you whether you’re patched. Debian and Ubuntu backport the fix into their existing 1.1.0 package instead of moving to 1.1.1, so a fully patched box still reports Brotli 1.1.0 and still has a `libbrotlidec.so.1.1.0` sitting on disk. Check the package revision instead:

```
dpkg-query -W -f='${Version}
' libbrotli1
# vulnerable: 1.1.0-2+b7
# patched:    1.1.0-2+deb13u1   (Debian 13 "trixie"; the suffix
#                                differs by distribution and release)
```
### If You Can’t Update Yet

None of what follows fixes the bug. It cuts off the ways to reach it while you arrange the real update. Since there’s nothing useful to match on in the inbound request, the lever is your own code, and specifically how WordPress asks for the response. The first option is the broad one, and it stops every path at once.

**Stop WordPress decoding Brotli at all.** Drop this in a must-use plugin (`wp-content/mu-plugins/`) or your theme’s `functions.php`. It tells libcurl not to decompress anything, so an attacker’s body never reaches the Brotli decoder, and it covers pingback, oEmbed, feeds and plugin fetches in one go. The cost is that WordPress stops asking for compressed responses on its own outbound requests, which is not worth worrying about. It also fails softly: if a server sends a compressed body anyway, WordPress still unpacks gzip itself, in PHP, well away from the vulnerable code.

```
add_action( 'http_api_curl', function ( $handle ) {
    // Don't let libcurl auto-decompress responses, so the Brotli
    // decoder is never handed an attacker-controlled body.
    curl_setopt( $handle, CURLOPT_ENCODING, 'identity' );
    curl_setopt( $handle, CURLOPT_HTTP_CONTENT_DECODING, 0 );
}, 10, 1 );
```
**Turn off pingback.** On its own, this removes the unauthenticated path. Be aware that the usual `add_filter( 'xmlrpc_enabled', '__return_false' )` does *not* do it: that only disables the XML-RPC methods that require a login and pingback requires none. Unset the method instead. Doing it this way also beats matching the method name in a rule, because WordPress decodes XML character references and CDATA before dispatch, and an attacker can spell `pingback.ping` in ways a string match won’t catch:

```
add_filter( 'xmlrpc_methods', function ( $methods ) {
    unset( $methods['pingback.ping'] );
    unset( $methods['pingback.extensions.getPingbacks'] );
    return $methods;
} );
```
**Or block `xmlrpc.php` at the web server**, which drops the request before PHP starts. On Apache 2.4:

```
<Files xmlrpc.php>
    Require all denied
</Files>
```
And on nginx:

```
location = /xmlrpc.php {
    deny all;
}
```
Blocking `xmlrpc.php` only closes the pingback route. oEmbed, feeds and any plugin that fetches a URL still reach the decoder, so pair it with the Brotli filter above. Beyond that, audit the plugins that fetch visitor-supplied URLs, and where you can, push WordPress’s outbound HTTP through a proxy that only allows hosts you know. None of it replaces updating the library.

## Detecting It

Outbound traffic is where this shows up most clearly. A WordPress install making a request that comes back `Content-Encoding: br` is already strange, because brotli is a browser encoding and WordPress’s own fetches don’t normally get it. A tiny compressed body that balloons on unpacking, or a chunked reply that stalls halfway, is stranger still. A forward proxy with logging will show all of it.

At the edge, look for unauthenticated `POST /xmlrpc.php` carrying a `pingback.ping` whose source URL points somewhere the site has no business contacting, particularly in bursts or toward domains registered last week. Watch plugin endpoints that accept a URL the same way.

On the host, the crash is hard to miss. Apache logs `AH00051: child pid N exit signal Segmentation fault (11)`, and PHP-FPM logs a child exiting on signal 11. A core dump with `libbrotlidec.so` in the backtrace settles it. Not every hit leaves one, though: the public lab also produces a worker stuck at full CPU and no crash at all, so pair the segfault check with an eye on pinned workers and requests that time out. The same crash on the same kind of request, over and over, is either someone knocking the site over or someone trying to do more than that. If they managed the latter, the tell is the web server user spawning a shell or `curl`: a `www-data` process whose parent is PHP or Apache, talking to a host you don’t recognize.
