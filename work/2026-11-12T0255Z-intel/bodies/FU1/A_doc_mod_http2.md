---
title: Apache Module mod_http2
url: https://httpd.apache.org/docs/2.4/mod/mod_http2.html
hostname: apache.org
sitename: Apache HTTP Server Version 2.4
date: "2017-04-02"
fingerprint: dc1cb84dd9820e83
---
Apache HTTP Server Version 2.4

| [Description:](https://httpd.apache.org/module-dict.html#Description) | Support for the HTTP/2 transport layer | 
|---|---|
| [Status:](https://httpd.apache.org/module-dict.html#Status) | Extension | 
| [Module Identifier:](https://httpd.apache.org/module-dict.html#ModuleIdentifier) | http2\_module | 
| [Source File:](https://httpd.apache.org/module-dict.html#SourceFile) | mod\_http2.c | 
| [Compatibility:](https://httpd.apache.org/module-dict.html#Compatibility) | Available in version 2.4.17 and later | 

This module provides HTTP/2 ([RFC 7540](https://www.rfc-editor.org/rfc/rfc7540)) 
        support for the Apache HTTP Server.

This module relies on [libnghttp2](http://nghttp2.org/)
        to provide the core http/2 engine.

You must enable HTTP/2 via [Protocols](https://httpd.apache.org/mod/core.html#protocols)[does not require](https://http2.github.io/faq/#does-http2-require-encryption) the use of encryption so two schemes are available:
        `h2` (HTTP/2 over TLS) and `h2c` (HTTP/2 over TCP).

Two useful configuration schemes are:

Protocols h2 http/1.1

Allows HTTP/2 negotiation (h2) via TLS ALPN in a secure
        [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)[H2Direct](https://httpd.apache.org#h2direct)`h2`.

Protocols h2 h2c http/1.1

Allows HTTP/2 negotiation (h2) via TLS ALPN for secure
        [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)[H2Direct](https://httpd.apache.org#h2direct)

Refer to the official [HTTP/2 FAQ](https://http2.github.io/faq)
        for any doubt about the protocol.

Enabling HTTP/2 on your Apache Server has impact on the resource consumption and if you have a busy site, you may need to consider carefully the implications.

The first noticeable thing after enabling HTTP/2 is that your server
            processes will start additional threads. The reason for this is that
            HTTP/2 gives all requests that it receives to its own *Worker*
            threads for processing, collects the results and streams them out
            to the client.

In the current implementation, these workers use a separate thread
            pool from the MPM workers that you might be familiar with. This is
            just how things are right now and not intended to be like this forever.
            (It might be forever for the 2.4.x release line, though.) So, HTTP/2
            workers, or shorter H2Workers, will not show up in [mod\_status](https://httpd.apache.org/mod/mod_status.html)[ThreadsPerChild](https://httpd.apache.org/mod/mpm_common.html#threadsperchild)[ThreadsPerChild](https://httpd.apache.org/mod/mpm_common.html#threadsperchild)[H2MinWorkers](https://httpd.apache.org#h2minworkers)[H2MaxWorkers](https://httpd.apache.org#h2maxworkers)

Another thing to watch out for is is memory consumption. Since HTTP/2
            keeps more state on the server to manage all the open request, priorities
            for and dependencies between them, it will always need more memory
            than HTTP/1.1 processing. There are three directives which steer the
            memory footprint of a HTTP/2 connection:
            [H2MaxSessionStreams](https://httpd.apache.org#h2maxsessionstreams)[H2WindowSize](https://httpd.apache.org#h2windowsize)[H2StreamMaxMemSize](https://httpd.apache.org#h2streammaxmemsize)

[H2MaxSessionStreams](https://httpd.apache.org#h2maxsessionstreams)

[H2WindowSize](https://httpd.apache.org#h2windowsize)

And last, but not least, [H2StreamMaxMemSize](https://httpd.apache.org#h2streammaxmemsize)

Many sites use the same TLS certificate for multiple virtual hosts. The certificate either has a wildcard name, such as '\*.example.org' or carries several alternate names. Browsers using HTTP/2 will recognize that and reuse an already opened connection for such hosts.

While this is great for performance, it comes at a price: such vhosts need more care in their configuration. The problem is that you will have multiple requests for multiple hosts on the same TLS connection. And that makes renegotiation impossible, in face the HTTP/2 standard forbids it.

So, if you have several virtual hosts using the same certificate and want to use HTTP/2 for them, you need to make sure that all vhosts have exactly the same SSL configuration. You need the same protocol, ciphers and settings for client verification.

If you mix things, Apache httpd will detect it and return a special response code, 421 Misdirected Request, to the client.

This module can be configured to provide HTTP/2 related information
            as additional environment variables to the SSI and CGI namespace, as well
            as in custom log configurations (see `%{VAR_NAME}e`).

| [Variable Name:] | Value Type: | Description: | 
|---|---|---|
| `HTTP2` | flag | HTTP/2 is being used. | 
| `H2PUSH` | flag | HTTP/2 Server Push is enabled for this connection and also supported by the client. | 
| `H2_PUSH` | flag | alternate name for `H2PUSH` | 
| `H2_PUSHED` | string | empty or `PUSHED` for a request being pushed by the server. | 
| `H2_PUSHED_ON` | number | HTTP/2 stream number that triggered the push of this request. | 
| `H2_STREAM_ID` | number | HTTP/2 stream number of this request. | 
| `H2_STREAM_TAG` | string | HTTP/2 process unique stream identifier, consisting of connection id and stream id separated by `-`. | 

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine file handling in responses | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2CopyFiles on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2CopyFiles off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.24 and later. | 

This directive influences how file content is handled in
                responses. When `off`, which is the default, file handles
                are passed from the requestion processing down to the main
                connection, using the usual Apache setaside handling for
                managing the lifetime of the file.

When set to `on`, file content is copied while the
                request is still being processed and the buffered data is passed
                on to the main connection. This is better if a third party
                module is injecting files with different lifetimes into the response.

An example for such a module is `mod_wsgi` that may place
                Python file handles into the response. Those files get close down when
                Python thinks processing has finished. That may be well before
                [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | H2 Direct Protocol Switch | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2Direct on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2Direct on for h2c, off for h2 protocol` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive toggles the usage of the HTTP/2 Direct Mode. This
                should be used inside a 
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

Direct communication means that if the first bytes received by the server on a connection match the HTTP/2 preamble, the HTTP/2 protocol is switched to immediately without further negotiation. This mode is defined in RFC 7540 for the cleartext (h2c) case. Its use on TLS connections not mandated by the standard.

When a server/vhost does not have h2 or h2c enabled via
                [Protocols](https://httpd.apache.org/mod/core.html#protocols)`H2Direct`
                does not matter then. This is important for connections that
                use protocols where an initial read might hang indefinitely, such
                as NNTP.

For clients that have out-of-band knowledge about a server supporting h2c, direct HTTP/2 saves the client from having to perform an HTTP/1.1 upgrade, resulting in better performance and avoiding the Upgrade restrictions on request bodies.

This makes direct h2c attractive for server to server communication as well, when the connection can be trusted or is secured by other means.

H2Direct on

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Add a response header to be picked up in 103 Early Hints | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2EarlyHint` `name value` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.58 and later. | 

`H2EarlyHint` allows adding a response
                header before the real request processing is started. Such headers
                are picked up for "103 Early Hints" intermediate responses. The main
                purpose is to send "preload" information to client browsers.

`name` and `value` must be valid HTTP header fields
                or will lead to failed responses. `H2EarlyHints`
                must still be enabled to allow 103 intermediate responses to be sent.
                This directive can be repeated several times and header fields of the
                same names add.

H2EarlyHint Link "\</my.css>;rel=preload;as=style"

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine sending of 103 status codes | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2EarlyHints on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2EarlyHints off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.24 and later. | 

This setting controls if HTTP status 103 interim responses are forwarded to the client or not. By default, this is currently not the case since a range of clients still have trouble with unexpected interim responses.

When set to `on`, PUSH resources announced with
                [H2PushResource](https://httpd.apache.org#h2pushresource)`Link`
                headers that advise the `preload` of such resources.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum bytes inside a single HTTP/2 DATA frame | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxDataFrameLen` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2MaxDataFrameLen 0` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.58 and later. | 

`H2MaxDataFrameLen` limits the maximum
                amount of response body bytes placed into a single HTTP/2 DATA
                frame. Setting this to 0 places no limit (but the max size
                allowed by the protocol is observed).

The module, by default, tries to use the maximum size possible, which is somewhat around 16KB. This sets the maximum. When less response data is availble, smaller frames will be sent.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum size of response headers | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxHeaderBlockLen` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2MaxHeaderBlockLen 0` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.64 and later. | 

`H2MaxHeaderBlockLen` sets the limit
                on the overall size of response headers. A setting of 0
                will leave this at the default of 64 KB in nghttp2.

Responses with headers larger than this (adding all headers) will not be processed and result in a reset of the stream.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum number of active streams per HTTP/2 session. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxSessionStreams` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2MaxSessionStreams 100` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the maximum number of active streams per HTTP/2 session (e.g. connection)
                that the server allows. A stream is active if it is not `idle` or 
                `closed` according to RFC 7540.

H2MaxSessionStreams 20

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum amount of client caused errors to tolerate | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxStreamErrors` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2MaxStreamErrors 8` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.5.1 and later. | 

`H2MaxStreamErrors` sets the maxmimum amount
                of tolerated HTTP/2 stream errors caused by the client.
                When exceeding this limit, the connection will be closed.
                Stream errors are protocol violations on an individual HTTP/2
                stream that do not necessitate a connection close by the
                protocol specification, but can be a sign of malicious
                activity by a client.

Set to 0 to tolerate faulty clients.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum number of seconds h2 workers remain idle until shut down. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxWorkerIdleSeconds` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2MaxWorkerIdleSeconds 600` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the maximum number of seconds a h2 worker may 
                idle until it shuts itself down. This only happens while the number of
                h2 workers exceeds [H2MinWorkers](https://httpd.apache.org#h2minworkers)

H2MaxWorkerIdleSeconds 20

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum number of worker threads to use per child process. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MaxWorkers` `n` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the maximum number of worker threads to spawn
                per child process for HTTP/2 processing. If this directive is not used,
                [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`mpm`
                module loaded.

H2MaxWorkers 20

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Minimal number of worker threads to use per child process. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2MinWorkers` `n` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the minimum number of worker threads to spawn
                per child process for HTTP/2 processing. If this directive is not used,
                [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`mpm`
                module loaded.

H2MinWorkers 10

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Require HTTP/2 connections to be "modern TLS" only | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2ModernTLSOnly on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2ModernTLSOnly on` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.18 and later. | 

This directive toggles the security checks on HTTP/2 connections
                in TLS mode (https:). This can be used server wide or for specific
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

The security checks require that the TSL protocol is at least TLSv1.2 and that none of the ciphers listed in RFC 7540, Appendix A is used. These checks will be extended once new security requirements come into place.

The name stems from the 
                [Security/Server Side TLS](https://wiki.mozilla.org/Security/Server_Side_TLS)
                definitions at mozilla where "modern compatibility" is defined. Mozilla Firefox and
                other browsers require modern compatibility for HTTP/2 connections. As everything
                in OpSec, this is a moving target and can be expected to evolve in the future.

One purpose of having these checks in [mod\_http2](https://httpd.apache.org/mod/mod_http2.html)

Ultimately, the security of the TLS connection is determined by the
                server configuration directives for [mod\_ssl](https://httpd.apache.org/mod/mod_ssl.html)

H2ModernTLSOnly off

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine buffering behavior of output | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2OutputBuffering on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2OutputBuffering on` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.48 and later. | 

The directive `H2OutputBuffering` controls the buffering of stream output.
                The default is on, which is the behavior of previous versions. When off, all
                bytes are made available immediately to the main connection for sending them
                out to the client. This fixes interop issues with certain flavours of gRPC.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine the range of padding bytes added to payload frames | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2Padding` `numbits` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2Padding 0` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.39 and later. | 

With the default 0, no padding bytes are added to any payload frames, e.g. HEADERS, DATA and PUSH\_PROMISE. This is the behavior of previous versions. It means that under certain conditions, an observer of network traffic can see the length of those frames in the TLS stream.

When configuring numbits of 1-8, a random number in range \[0, 2^numbits\[ are added to each frame. The random value is chosen independently for each frame that the module sends back to the client.

While more padding bytes give better message length obfuscation, they are also additional traffic. The optimal number therefore depends on the kind of web traffic the server carries.

The default of 0, e.g. no padding, was chosen for maximum backward compatibility. There might be deployments where padding bytes are unwanted or do harm. The most likely cause would be a client that has a faults implementation.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | En-/Disable forward proxy requests via HTTP/2 | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2ProxyRequests  on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2ProxyRequests off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.58 and later. | 

Use `H2ProxyRequests` to enable or disable
                handling of HTTP/2 requests in a forward proxy configuration.

Similar to [ProxyRequests](https://httpd.apache.org/mod/proxy.html#proxyrequests)


| [Description:](https://httpd.apache.org/directive-dict.html#Description) | H2 Server Push Switch | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2Push on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2Push on` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.18 and later. | 

This directive toggles the usage of the HTTP/2 server push protocol feature.

The HTTP/2 protocol allows the server to push other resources to a client when it asked for a particular one. This is helpful if those resources are connected in some way and the client can be expected to ask for it anyway. The pushing then saves the time it takes the client to ask for the resources itself. On the other hand, pushing resources the client never needs or already has is a waste of bandwidth.

Server pushes are detected by inspecting the `Link` headers of
                responses (see [RFC 8288](https://www.rfc-editor.org/rfc/rfc8288) for the
                specification of Web Linking). When a link thus specified has the `rel=preload`
                attribute, it is treated as a resource to be pushed.

Link headers in responses are either set by the application or
                can be configured via [H2PushResource](https://httpd.apache.org#h2pushresource)[mod\_headers](https://httpd.apache.org/mod/mod_headers.html)

```
<Location /index.html>
    Header add Link "</css/site.css>;rel=preload"
    Header add Link "</images/logo.jpg>;rel=preload"
</Location>
```
As the example shows, there can be several link headers added to a response, resulting in several pushes being triggered. There are no checks in the module to avoid pushing the same resource twice or more to one client. Use with care.

HTTP/2 server pushes are enabled by default. On a server or virtual host, you may enable/disable this feature for any connection to the host. In addition, you may disable PUSH for a set of resources in a Directory/Location. This controls which resources may cause a PUSH, not which resources may be sent via PUSH.

H2Push off

Last but not least, pushes happen only when the client signals
                its willingness to accept those. Most browsers do, some, like Safari 9,
                do not. Also, pushes also only happen for resources from the same
                *authority* as the original response is for.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | H2 Server Push Diary Size | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2PushDiarySize` `n` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2PushDiarySize 256` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.19 and later. | 

This directive toggles the maximum number of HTTP/2 server pushes 
                that are remembered per HTTP/2 connection. This can be used inside the
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

The push diary records a digest of pushed resources (their URL) to avoid duplicate pushes on the same connection. These value are not persisted, so clients opening a new connection will experience known pushes again.

If the maximum size is reached, newer entries replace the oldest ones. A diary entry uses 8 bytes, letting a default diary with 256 entries consume around 2 KB of memory.

A size of 0 will effectively disable the push diary.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | H2 Server Push Priority | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2PushPriority` `mime-type` [after\|before\|interleaved] [`weight`] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2PushPriority * After 16` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.18 and later. For having an effect, a nghttp2 library version 1.5.0 or newer is necessary. | 

This directive defines the priority handling of pushed responses based on the content-type of the response. This is usually defined per server config, but may also appear in a virtual host.

HTTP/2 server pushes are always related to a client request. Each
                such request/response pairs, or *streams* have a dependency
                and a weight, together defining the *priority* of a stream.

When a stream *depends* on another, say X depends on Y,
                then Y gets all bandwidth before X gets any. Note that this
                does not mean that Y will block X. If Y has no data to send, 
                all bandwidth allocated to Y can be used by X.

When a stream has more than one dependent, say X1 and X2 both
                depend on Y, the *weight* determines the bandwidth
                allocation. If X1 and X2 have the same weight, they both get
                half of the available bandwidth. If the weight of X1 is twice
                as large as that for X2, X1 gets twice the bandwidth of X2.

Ultimately, every stream depends on the *root* stream which
                gets all the bandwidth available, but never sends anything. So all
                its bandwidth is distributed by weight among its children. Which
                either have data to send or distribute the bandwidth to their
                own children. And so on. If none of the children have data
                to send, that bandwidth get distributed somewhere else according
                to the same rules.

The purpose of this priority system is to always make use of available bandwidth while allowing precedence and weight to be given to specific streams. Since, normally, all streams are initiated by the client, it is also the one that sets these priorities.

Only when such a stream results in a PUSH, gets the server to
                decide what the *initial* priority of such a pushed
                stream is. In the examples below, X is the client stream. It
                depends on Y and the server decides to PUSH streams P1 and P2
                onto X.

The default priority rule is:

H2PushPriority \* After 16

which reads as 'Send a pushed stream of any content-type depending on the client stream with weight 16'. And so P1 and P2 will be send after X and, as they have equal weight, share bandwidth equally among themselves.

H2PushPriority text/css Interleaved 256

which reads as 'Send any CSS resource on the same dependency and
                weight as the client stream'. If P1 has content-type 'text/css',
                it will depend on Y (as does X) and its effective weight will be
                calculated as `P1ew = Xw * (P1w / 256)`. With P1w being 
                256, this will make the effective weight the same as the weight
                of X. If both X and P1 have data to send, bandwidth will be allocated
                to both equally.

With Pw specified as 512, a pushed, interleaved stream would get double the weight of X. With 128 only half as much. Note that effective weights are always capped at 256.

H2PushPriority application/json Before

This says that any pushed stream of content type 'application/json'
                should be send out *before* X. This makes P1 dependent
                on Y and X dependent on P1. So, X will be stalled as long as
                P1 has data to send. The effective weight is inherited from the
                client stream. Specifying a weight is not allowed.

Be aware that the effect of priority specifications is limited by the available server resources. If a server does not have workers available for pushed streams, the data for the stream may only ever arrive when other streams have been finished.

Last, but not least, there are some specifics of the syntax to be used in this directive:

1. '\*' is the only special content-type that matches all others. 'image/\*' will not work.
2. The default dependency is 'After'.
3. There are also default weights: for 'After' it is 16, 'interleaved' is 256.

H2PushPriority application/json 32         # an After rule
H2PushPriority image/jpeg before           # weight inherited
H2PushPriority text/css   interleaved      # weight 256 default

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Declares resources for early pushing to the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2PushResource [add]` `path` [critical] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.24 and later. | 

When added to a directory/location HTTP/2 PUSHes will be attempted for all paths added via this directive. This directive can be used several times for the same location.

This directive pushes resources much earlier than adding 
                `Link` headers via [mod\_headers](https://httpd.apache.org/mod/mod_headers.html)[mod\_http2](https://httpd.apache.org/mod/mod_http2.html)`103 Early Hints` interim response to the client.
                That means that clients not supporting PUSH will still get
                early preload hints.

In contrast to setting `Link` response headers 
                via [mod\_headers](https://httpd.apache.org/mod/mod_headers.html)

By adding `critical` to such a resource, the server
                will give processing it more preference and send its data, once
                available, before the data from the main request.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Serialize Request/Response Processing Switch | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2SerializeHeaders on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2SerializeHeaders off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive toggles if HTTP/2 requests shall be serialized in
                HTTP/1.1 format for processing by `httpd` core or if
                received binary data shall be passed into the `request_rec`s
                directly.

Serialization will lower performance, but gives more backward compatibility in case custom filters/hooks need it.

H2SerializeHeaders on

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum amount of output data buffered per stream. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2StreamMaxMemSize` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2StreamMaxMemSize 65536` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the maximum number of outgoing data bytes buffered in memory for an active streams. This memory is not allocated per stream as such. Allocations are counted against this limit when they are about to be done. Stream processing freezes when the limit has been reached and will only continue when buffered data has been sent out to the client.

H2StreamMaxMemSize 128000

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum time waiting when sending/receiving data to stream processing | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2StreamTimeout` `time-interval`[s] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Value of` [Timeout](https://httpd.apache.org/mod/core.html#timeout) | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.55 and later. | 

`H2StreamTimeout` specifies the maximum time that
                a stream being processed will wait for its data to be sent/received.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configure the number of seconds of idle time on TLS before shrinking writes | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2TLSCoolDownSecs` `seconds` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2TLSCoolDownSecs 1` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.18 and later. | 

This directive sets the number of seconds of idle time on a TLS
                connection before the TLS write size falls back to small (\~1300 bytes)
                length.
                This can be used server wide or for specific
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

See [H2TLSWarmUpSize](https://httpd.apache.org#h2tlswarmupsize)`H2TLSCoolDownSecs` reflects the fact
                that connections may deteriorate over time (and TCP flow adjusts)
                for idle connections as well. It is beneficial to overall performance
                to fall back to the pre-warmup phase after a number of seconds that
                no data has been sent.

In deployments where connections can be considered reliable, this timer can be disabled by setting it to 0.

The following example sets the seconds to zero, effectively disabling any cool down. Warmed up TLS connections stay on maximum record size.

H2TLSCoolDownSecs 0

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configure the number of bytes on TLS connection before doing max writes | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2TLSWarmUpSize` `amount` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2TLSWarmUpSize 1048576` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.18 and later. | 

This directive sets the number of bytes to be sent in small
                TLS records (\~1300 bytes) until doing maximum sized writes (16k)
                on https: HTTP/2 connections.
                This can be used server wide or for specific
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

Measurements by [google performance
                    labs](https://www.igvita.com) show that best performance on TLS connections is reached,
                if initial record sizes stay below the MTU level, to allow a
                complete record to fit into an IP packet.

While TCP adjust its flow-control and window sizes, longer TLS records can get stuck in queues or get lost and need retransmission. This is of course true for all packets. TLS however needs the whole record in order to decrypt it. Any missing bytes at the end will stall usage of the received ones.

After a sufficient number of bytes have been send successfully, the TCP state of the connection is stable and maximum TLS record sizes (16 KB) can be used for optimal performance.

In deployments where servers are reached locally or over reliable connections only, the value might be decreased with 0 disabling any warmup phase altogether.

The following example sets the size to zero, effectively disabling any warmup phase.

H2TLSWarmUpSize 0

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | H2 Upgrade Protocol Switch | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2Upgrade on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2Upgrade on for h2c, off for h2 protocol` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive toggles the usage of the HTTP/1.1 Upgrade method 
                for switching to HTTP/2. This
                should be used inside a 
                [\<VirtualHost>](https://httpd.apache.org/mod/core.html#virtualhost)

This method of switching protocols is defined in HTTP/1.1 and uses the "Upgrade" header (thus the name) to announce willingness to use another protocol. This may happen on any request of a HTTP/1.1 connection.

This method of protocol switching is enabled by default on cleartext (potential h2c) connections and disabled on TLS (potential h2), as mandated by RFC 7540.

Please be aware that Upgrades are only accepted for requests
                that carry no body. POSTs and PUTs with content will never
                trigger an upgrade to HTTP/2. 
                See [H2Direct](https://httpd.apache.org#h2direct)

This mode only has an effect when h2 or h2c is enabled via
                the [Protocols](https://httpd.apache.org/mod/core.html#protocols)

H2Upgrade on

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | En-/Disable WebSockets via HTTP/2 | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2WebSockets  on\|off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2WebSockets off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in version 2.4.58 and later. | 

Use `H2WebSockets` to enable or disable
                bootstrapping of WebSockets via the HTTP/2 protocol. This
                protocol extension is defined in RFC 8441.

Such requests come as a CONNECT with an extra ':protocol' header. Such requests are transformed inside the module to their HTTP/1.1 equivalents before passing it to internal processing.

This means that HTTP/2 WebSockets can be used for a
                [ProxyPass](https://httpd.apache.org/mod/mod_proxy.html#proxypass)

For (3rd party) modules that handle WebSockets directly in the server, the protocol bootstrapping itself will also work. However the transfer of data does require extra support in case of HTTP/2. The negotiated WebSocket will not be able to use the client connection socket for polling IO related events.

Because enabling this feature might break backward compatibility for such 3rd party modules, it is not enabled by default.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Size of Stream Window for upstream data. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `H2WindowSize` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `H2WindowSize 65535` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Extension | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | mod\_http2 | 

This directive sets the size of the window that is used for flow control from client to server and limits the amount of data the server has to buffer. The client will stop sending on a stream once the limit has been reached until the server announces more available space (as it has processed some of the data).

This limit affects only request bodies, not its meta data such as headers. Also, it has no effect on response bodies as the window size for those are managed by the clients.

H2WindowSize 128000
