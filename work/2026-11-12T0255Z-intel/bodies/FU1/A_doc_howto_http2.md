---
title: HTTP/2 guide
url: https://httpd.apache.org/docs/2.4/howto/http2.html
hostname: apache.org
sitename: Apache HTTP Server Version 2.4
date: "2026-01-01"
fingerprint: "7f08855e6fa24c94"
---
Apache HTTP Server Version 2.4

This is the howto guide for the HTTP/2 implementation in Apache httpd. This
    feature is *production-ready* and you may expect interfaces and directives to
    remain consistent across releases.

HTTP/2 is the evolution of the world's most successful application layer protocol, HTTP. It focuses on making more efficient use of network resources. It does not change the fundamentals of HTTP, the semantics. There are still requests and responses and headers and all that. So, if you already know HTTP/1, you know 95% about HTTP/2 as well.

The protocol is defined in [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113) (which obsoletes the original
    [RFC 7540](https://www.rfc-editor.org/rfc/rfc7540)). For a more approachable introduction, see
    [http2 explained](https://daniel.haxx.se/http2/) by Daniel Stenberg,
    the author of [curl](https://curl.haxx.se). It covers the motivation
    and design of HTTP/2 without requiring you to parse RFC notation first.

In short: there are some new terms and gotchas that need to be kept in mind while reading this document:

- HTTP/2 is a **binary protocol**, as opposed to HTTP 1.1
        that is plain text. The latter is meant to be human readable (for example
        sniffing network traffic) while the former is not. More info in the official
        FAQ [question](https://http2.github.io/faq/#why-is-http2-binary).
- **h2** is HTTP/2 over TLS (protocol negotiation via ALPN).
- **h2c** is HTTP/2 over cleartext TCP (without TLS). Note that
        h2c has been removed from the current specification but httpd still supports it.
- A **frame** is the smallest unit of communication within
        an HTTP/2 connection, consisting of a header and a variable-length sequence
        of octets structured according to the frame type. More info in the official
        documentation [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113).
- A **stream** is a bidirectional flow of frames within the
        HTTP/2 connection. The corresponding concept in HTTP 1.1 is a request/response
        message exchange. More info in the official documentation [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113).
- HTTP/2 is able to run **multiple streams** of data over
        the same TCP connection, avoiding the classic HTTP 1.1 head-of-line blocking
        of slow requests and avoiding the need to re-instantiate TCP connections
        for each request/response (KeepAlive patched the problem in HTTP 1.1 but
        did not fully solve it).

The HTTP/2 protocol is implemented by its own httpd module, aptly named
    [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`h2c`', 
    the secure one '`h2`'. For `h2c` it allows the *direct*
    mode and the `Upgrade:` via an initial HTTP/1 request.

One feature of HTTP/2 that formerly offered new capabilities for web developers is
    [Server Push](https://httpd.apache.org#push), though it is now deprecated. See the
    [Early Hints](https://httpd.apache.org#earlyhints) section for the recommended alternative.

[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)[nghttp2](https://nghttp2.org)
    as its implementation base. Building [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`libnghttp2` installed on your system.

When you `./configure` your Apache httpd source tree, you need to give it 
    '`--enable-http2`' as additional argument to trigger the build of the module.
    Should your `libnghttp2` reside in an unusual place (whatever that is on your
    operating system), you may announce its location with '`--with-nghttp2=<path>`'
    to `configure`.

While that should do the trick for most, there are people who might prefer a statically
    linked `nghttp2` in this module. For those, the option `--enable-nghttp2-staticlib-deps`
    exists. It works quite similarly to how one statically links openssl to [mod\_ssl](https://httpd.apache.org/mod/mod_ssl.html)

Speaking of SSL, you need to be aware that most browsers will speak HTTP/2 only on `https:`
    URLs, so you need a server with SSL support. But not only that, you will need an SSL library
    that supports the `ALPN` extension. If OpenSSL is the library you use, you need
    at least version 1.0.2.

When you have a `httpd` built with [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)

LoadModule http2\_module modules/mod\_http2.so

The second directive you need to add to your server configuration is

Protocols h2 http/1.1

This allows h2, the secure variant, to be the preferred protocol on your server connections. When you want to enable all HTTP/2 variants, write:

Protocols h2 h2c http/1.1

Depending on where you put this directive, it affects all connections or only those to a specific virtual host. You can nest it, as in:

Protocols http/1.1
\<VirtualHost ...>
ServerName test.example.org
Protocols h2 http/1.1
\</VirtualHost>

This allows only HTTP/1 on connections, except SSL connections to `test.example.org`
    which offer HTTP/2.

The [SSLCipherSuite](https://httpd.apache.org/mod/mod_ssl.html#sslciphersuite)[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`h2` enabled server with an inappropriate
    cipher suite causes it to refuse and fall back to HTTP 1.1. This is a common mistake
    made while configuring httpd for HTTP/2 the first time, so please keep it in mind to avoid
    long debugging sessions! If you want to be sure about the cipher suite to choose please avoid
    the ones listed in the HTTP/2 TLS reject list ([RFC 9113](https://www.rfc-editor.org/rfc/rfc9113#section-9.2.2)).

The order of protocols mentioned is also relevant. By default, the first one is the most preferred protocol. When a client offers multiple choices, the one most to the left is selected. In

Protocols http/1.1 h2

the most preferred protocol is HTTP/1 and it will always be selected unless a 
    client *only* supports h2. Since we want to talk HTTP/2 to clients that
    support it, the better order is

There is one more thing to ordering: the client has its own preferences, too. If you want, you can configure your server to select the protocol most preferred by the client:

ProtocolsHonorOrder Off

makes the order *you* wrote the Protocols irrelevant and only the client's
    ordering will decide.

A last thing: the protocols you configure are not checked for correctness
    or spelling. You can mention protocols that do not exist, so there is no need
    to guard [Protocols](https://httpd.apache.org/mod/core.html#protocols)[\<IfModule>](https://httpd.apache.org/mod/core.html#ifmodule)

For more advanced tips on configuration, see the 
    [modules section about dimensioning](https://httpd.apache.org/mod/mod_http2.html#dimensioning) and 
    [how to manage multiple hosts with the same certificate](https://httpd.apache.org/mod/mod_http2.html#misdirected).

HTTP/2 is supported in all multi-processing modules that come with httpd. However, if
    you use the [prefork](https://httpd.apache.org/mod/prefork.html)

In [prefork](https://httpd.apache.org/mod/prefork.html)[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)

[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)[prefork](https://httpd.apache.org/mod/prefork.html)

If your setup can handle it, configuring [event](https://httpd.apache.org/mod/event.html)

If you are really stuck with [prefork](https://httpd.apache.org/mod/prefork.html)[H2MinWorkers](https://httpd.apache.org/mod/mod_http2.html#h2minworkers)

All modern browsers support HTTP/2 over TLS connections
    ([source](https://caniuse.com/http2)). Support has been universal across
    major browsers since approximately 2015.

Other clients, as well as servers, are listed 
    [on the Implementations wiki](https://github.com/http2/http2-spec/wiki/Implementations),
    among them implementations for c, c++, common lisp, dart, erlang, haskell, java, nodejs,  php, 
    python, perl, ruby, rust, scala and swift.

Several of the non-browser client implementations support HTTP/2 over cleartext, h2c. The
    most versatile being [curl](https://curl.haxx.se).

The first tool to mention is of course [curl](https://curl.haxx.se). Please make sure that
    your version supports HTTP/2 checking its `Features`:

$ curl -V
curl 8.20.0 (x86\_64-pc-linux-gnu) libcurl/8.20.0 OpenSSL/3.5.7 zlib/1.3.1 nghttp2/1.69.0
Protocols: dict file ftp ftps gopher http https imap imaps ldap ldaps pop3 \[...\]
Features: IPv6 Largefile NTLM NTLM\_WB SSL libz TLS-SRP **HTTP2**

Homebrew's `curl` includes HTTP/2 support by default. Install with
    `brew install curl` and follow the displayed caveats to put it ahead
    of the system curl in your PATH.

And for really deep inspection [wireshark](https://wiki.wireshark.org/HTTP2).

The [nghttp2](https://nghttp2.org) package also includes clients, such as:

- [nghttp](https://nghttp2.org/documentation/nghttp.1.html) - useful to visualize the HTTP/2 frames and get a better idea of the protocol.
- [h2load](https://nghttp2.org/documentation/h2load-howto.html) - useful to stress-test your server.

Chrome offers detailed HTTP/2 logs on its connections via the 
    [special net-internals page](chrome://net-internals/#http2). There is also an
    interesting extension for [Chrome](https://chromewebstore.google.com/detail/http-indicator/hgcomhbcacfkpffiphlmnlhpppcjgmbl)
    and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/http2-indicator/)
    to indicate when your browser is using HTTP/2.

Server Push is deprecated in [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113#section-8.4). Major browsers
    (Chrome 106+, Edge 106+) have removed support for it. While [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)[103 Early Hints](https://httpd.apache.org#earlyhints)
    instead as a more reliable way to inform clients about needed resources.

The HTTP/2 protocol allows the server to PUSH responses to a client it never asked for. The tone of the conversation is: "here is a request that you never sent and the response to it will arrive soon..."

But there are restrictions: the client can disable this feature and the server may only ever PUSH on a request that came from the client.

The intention is to allow the server to send resources to the client that it will most likely need: a css or javascript resource that belongs to a html page the client requested. A set of images that is referenced by a css, etc.

The advantage for the client is that it saves the time to send the request which may range from a few milliseconds to half a second, depending on where on the globe both are located. The disadvantage is that the client may get sent things it already has in its cache. Sure, HTTP/2 allows for the early cancellation of such requests, but still there are resources wasted.

To summarize: there is no one good strategy on how to make best use of this feature of HTTP/2 and everyone is still experimenting. So, how do you experiment with it in Apache httpd?

[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`Link` headers
    in a certain format:

Link \</xxx.css>;rel=preload, \</xxx.js>; rel=preload

If the connection supports PUSH, these two resources will be sent to the client. As a web developer, you may set these headers either directly in your application response or you configure the server via

\<Location /xxx.html>
Header add Link "\</xxx.css>;rel=preload"
Header add Link "\</xxx.js>;rel=preload"
\</Location>

If you want to use `preload` links without triggering a PUSH, you
    can use the `nopush` parameter, as in

Link \</xxx.css>;rel=preload;nopush

or you may disable PUSHes for your server entirely with the directive

H2Push Off

And there is more:

The module will keep a diary of what has been PUSHed for each connection (hashes of URLs, basically) and will not PUSH the same resource twice. When the connection closes, this information is discarded.

There are people thinking about how a client can tell a server what it already has, so PUSHes for those things can be avoided, but no standard emerged before push was deprecated.

An experimental draft that was implemented in [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)
    [Accept-Push-Policy Header Field](https://datatracker.ietf.org/doc/html/draft-ruellan-http-accept-push-policy-00) where a client can, for each request, define
    what kind of PUSHes it accepts. This draft expired and was never adopted.

PUSH might not always trigger the request/response/performance that one expects or hopes for. There are various studies on this topic to be found on the web that explain benefits and weaknesses and how different features of client and network influence the outcome. For example: the fact that the server PUSHes a resource does not mean a browser will actually use the data.

The major thing that influences the response being PUSHed is the request that was
    simulated. The request URL for a PUSH is given by the application, but where do the
    request headers come from? For example, will the PUSH request a `accept-language`
    header and if yes with what value?

httpd will look at the original request (the one that triggered the PUSH) and copy the 
    following headers over to PUSH requests: `user-agent`, `accept`, 
    `accept-encoding`, `accept-language`, `cache-control`.

All other headers are ignored. Cookies will also not be copied over. PUSHing resources that require a cookie to be present will not work. This can be a matter of debate. But unless this is more clearly discussed with browsers, let's err on the side of caution and not expose cookies where they might ordinarily not be visible.

An alternative to PUSHing resources is to send `Link` headers to the
    client before the response is even ready. This uses the HTTP feature called "Early Hints" and
    is described in [RFC 8297](https://www.rfc-editor.org/rfc/rfc8297).

To use this, you need to explicitly enable it on the server via

H2EarlyHints on

(It is not enabled by default since some older browser tripped on such responses.)

If this feature is on, you can use the directive [H2PushResource](https://httpd.apache.org/mod/mod_http2.html#h2pushresource)

\<Location /xxx.html>
H2PushResource /xxx.css
H2PushResource /xxx.js
\</Location>

This will send out a `"103 Early Hints"` response to a client as soon
    as the server *starts* processing the request. This may be much earlier than
    the time the first response headers have been determined, depending on your web
    application.

If [H2Push](https://httpd.apache.org/mod/mod_http2.html#h2push)[H2Push](https://httpd.apache.org/mod/mod_http2.html#h2push)
