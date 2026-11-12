---
title: "Pre-announcement: Plone security fix 20261110"
author: Mauritsvanrees
url: https://community.plone.org/t/pre-announcement-plone-security-fix-20261110/23303
hostname: plone.org
description: On behalf of the Plone/Zope Security Team, this is a pre-announcement for a fix we plan to release Tuesday next week. It is a remote code execution vulnerability. All currently supported Plone versions are affected, and many versions before it as well, for example Plone 4.3. A security fix will be released on Tuesday 10 November 2026, around 1300 UTC. This is a fix for all Plone 6 versions (6.0, 6.1, 6.2). Older versions are not supported. We encourage everyone to configure a workaround bef...
sitename: Plone Community
date: "2026-11-02"
fingerprint: b6a83397afc5f283
---
              On behalf of the Plone/Zope Security Team, this is a pre-announcement for a fix we plan to release Tuesday next week.

It is a **remote code execution** vulnerability.

All currently supported Plone versions are affected, and many versions before it as well, for example Plone 4.3.

A security fix will be released on Tuesday 10 November 2026, around 1300 UTC.

This is a fix for all Plone 6 versions (6.0, 6.1, 6.2). Older versions are not supported.

We encourage everyone to configure a workaround before that time. This will work for any Plone version, and will keep you safe once the details have been published.

Specifically, you should block access to urls containing `portal_modifier`.

These urls should not be needed in everyday Plone usage.

Note that in these days an AI might be able to create an exploit based on this information alone. So do not delay until the last moment, but **block the url now**.

If you have any questions about this, you can mail us at [security@plone.org](mailto:security@plone.org).

If the question is not security-sensitive, you can also ask it by replying to the [https://community.plone.org](https://community.plone.org) announcement.

# `portal_modifier` in Apache, nginx, Traefik and Varnish

Zope acquisition makes `portal_modifier` reachable at any depth, so block it

anywhere in the path, not only at the root:

- `https://domain.tld/portal_modifier/...`
- `https://domain.tld/folder/page/portal_modifier/...`

Apache, nginx and Traefik decode percent-encoding before matching, so an

encoded variant like `/%70ortal_modifier` is caught too. Varnish does not;

see the caveat in its section.

## 

If you proxy to Plone with mod\_rewrite (the usual setup), add a rule

**before** your proxy `RewriteRule`:

```
RewriteEngine On
# Block portal_modifier anywhere in the path (Zope acquisition makes it reachable at any depth)
RewriteRule portal_modifier - [F,L]
# ... your existing proxy rule, e.g.
RewriteRule ^/(.*)$ http://127.0.0.1:8080/VirtualHostBase/https/%{SERVER_NAME}:443/Plone/VirtualHostRoot/$1 [P,L]
```

You can also do it with mod\_authz instead of rewrites:

```
<LocationMatch "portal_modifier">
    Require all denied
</LocationMatch>
```

Both return 403. To return 404 instead, use

`RewriteRule portal_modifier - [R=404,L]`.

## 

```
server {
    # ...
    # Regex locations take precedence over plain prefix locations like "location /"
    location ~ portal_modifier {
        return 403;   # or 404
    }
    location / {
        proxy_pass http://plone;
        # ...
    }
}
```

nginx checks regex locations in the order they appear and uses the first

match. If you have other `location ~ ...` blocks, put this one first. Also

make sure no prefix location uses `^~`, because that skips the regex check.

`$uri` is decoded and normalised (double slashes are merged, `..` is

resolved), so tricks like `//portal_modifier` are covered.

## 

Traefik has no built-in "deny" middleware, so the usual workaround is an

`ipAllowList` that only admits an address that can never be the source of a

real connection. Every request then gets a 403. Put it on a high-priority

router.

Use a TEST-NET address, not `127.0.0.1`. By default, `ipAllowList` checks

the source address of the TCP connection, so anything on the same machine

gets through a `127.0.0.1` allow list. That includes another Traefik that

proxies to this one over localhost, health checks and local `curl` calls.

Don't add an `ipStrategy` (`depth` or `excludedIPs`) to this middleware.

That makes it read `X-Forwarded-For`, which a client can influence.

### 

```
http:
  middlewares:
    deny-all:
      ipAllowList:
        sourceRange:
          - "192.0.2.1/32"   # TEST-NET-1 (RFC 5737), never a real source
  routers:
    block-portal-modifier:
      rule: "Host(`domain.tld`) && PathRegexp(`portal_modifier`)"
      priority: 10000          # must beat your normal router
      middlewares:
        - deny-all
      service: plone           # never reached, but a service is required
      entryPoints:
        - websecure
      tls: {}
    plone:
      rule: "Host(`domain.tld`)"
      service: plone
      entryPoints:
        - websecure
      tls: {}
```

### 

```
labels:
  - "traefik.http.middlewares.deny-all.ipallowlist.sourcerange=192.0.2.1/32"
  - "traefik.http.routers.block-pm.rule=Host(`domain.tld`) && PathRegexp(`portal_modifier`)"
  - "traefik.http.routers.block-pm.priority=10000"
  - "traefik.http.routers.block-pm.middlewares=deny-all"
  - "traefik.http.routers.block-pm.service=plone"
  - "traefik.http.routers.block-pm.entrypoints=websecure"
  - "traefik.http.routers.block-pm.tls=true"
```

`PathRegexp` is unanchored, so it matches at any depth.

### 

The middleware is called `ipWhiteList` in v2, and v2 has no `PathRegexp`.

Use this rule instead:

```
Host(`domain.tld`) && PathPrefix(`/{p:.*portal_modifier.*}`)
```

### 

If one Traefik forwards to another, put the block on the one that faces the

internet. Adding it on the inner one as well is cheap defence in depth, and

with the TEST-NET address it blocks there too, no matter where the request

came from.

## 

```
sub vcl_recv {
    if (req.url ~ "portal_modifier") {
        return (synth(403, "Access Denied"));
    }
    # ...
}
```

Caveat: unlike the servers above, Varnish does not decode `req.url`, so

percent-encoded variants like `/%70ortal_modifier` get through. Zope does

decode them, so they still reach `portal_modifier`. Rely on the rule in the

front server (Apache, nginx or Traefik) for those, and treat this one as

an extra layer.

## 

- **False positives:** the substring match also blocks any content whose id
contains `portal_modifier`, for example a page named
`about-portal_modifier`. That's normally fine. To be stricter, use
`/portal_modifier(/|$)`, but the loose match is safer.
- **Case:** Zope ids are case-sensitive, so `Portal_Modifier` won't resolve.
Matching case-sensitively is enough.
- **Direct access:** these rules only help if Zope's own port (for example
8080) can't be reached directly from outside. Bind it to `127.0.0.1` or an
internal network.
