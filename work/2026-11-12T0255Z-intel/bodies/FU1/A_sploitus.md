---
title: "💀 realslimsud0 — PoC exploit for CVE-2026-119618 | Sploitus"
url: https://sploitus.com/exploit?id=5E84C426-E374-5A47-AEDC-37EE818778BB
hostname: sploitus.com
description: Race condition in Apache HTTP Server mod_http2 assign_headers leads to RCE. (CVE-2026-119618)
sitename: Sploitus
date: "2026-11-11"
fingerprint: b30b8d7ada6e5b8b
---
````
## https://sploitus.com/exploit?id=5E84C426-E374-5A47-AEDC-37EE818778BB
# CVE-2026-119618 — Apache HTTP Server mod_http2 assign_headers RCE
Race condition (CWE-362) in `mod_http2`'s `assign_headers()` → heap corruption → RCE.
Affected: Apache httpd **2.4.55–2.4.70** (mod_h2 2.0.8–2.0.42). Fixed: **2.4.71** (2026-11-11).
## Root cause
`modules/http2/h2_request.c` `assign_headers()`:
```c
r->headers_in = apr_table_clone(r->pool, req->headers);   // clone FIRST
...
apr_table_setn(req->headers, "Content-Length", "0");      // BUG: writes SHARED table
```
`req->headers` is written unsynchronized from the session/master thread
(`h2_request_end_headers`) while `assign_headers` runs on worker threads
(`h2_c2.c`/`h2_c2_filter.c`) → concurrent apr_table mutation → heap corruption.
Fix (commit 5ed3928): write `r->headers_in` instead.
## Detection oracle (deterministic, race-free, banner-independent)
h2 request with `Content-Type` set, **no** `Content-Length`, END_STREAM on HEADERS:
- **Vulnerable 2.4.55–2.4.70**: CL:0 lands in shared `req->headers` *after* the clone
  → handler `CONTENT_LENGTH` **unset**
- **Fixed 2.4.71+**: CL:0 written to `r->headers_in` → handler `CONTENT_LENGTH`=0
A/B verified on stock 2.4.70 vs 2.4.71 builds (event MPM, h2c). Works with
`ServerTokens Prod`. Requires an endpoint reflecting `CONTENT_LENGTH`
(CGI, PHP, proxy backend).
## Scanner
```
./scanner/scanner.py HOST PORT [--scheme https] [--reflect-path /clprobe] [--json]
```
Tiered: (1) h2 active, (2) banner range, (3) CL oracle.
Verdicts: VULNERABLE / NOT-VULNERABLE / NOT-AFFECTED / UNKNOWN(exit 3).
## Mitigations (pre-2.4.71)
- Upgrade to 2.4.71
- Or drop `h2`/`h2c` from `Protocols` (disables the vulnerable code path)
````
