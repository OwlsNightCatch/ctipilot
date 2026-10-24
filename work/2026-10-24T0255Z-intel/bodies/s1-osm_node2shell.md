---
title: Python Packages Vulnerable to Node2Shell
author: OpenSourceMalware com; C
url: https://opensourcemalware.com/blog/node2shell-affects-python
hostname: opensourcemalware.com
description: Turns out that Node2Shell affects more than just Node! Python packages Brotli and brotlicffi are also affected by this vulnerability, but don't have a CVE.
sitename: OpenSourceMalware
date: "2026-10-23"
tags: ['malware, npm security, package security, open source security, threat intelligence, vulnerability reporting', 'PyPI']
fingerprint: "3830104db9747f90"
---
BLOG

# Python Packages Vulnerable to Node2Shell

Turns out that Node2Shell affects more than just Node! Python packages Brotli and brotlicffi are also affected by this vulnerability, but don't have a CVE.

By c0a15726-c5b1-4b0d-85e6-fe15553df9e2 ·

**Node2Shell ain’t just a Node.js bug: the PyPI** `Brotli` **and** `brotlicffi` **packages ship the same vulnerable C decoder.**

*I know its been a tough week...*

The last week has been hell, with the PHP2Shell, LiteLLM and Railway compromises, and the Plex and GitLab security events. Oh my gosh, its been a pretty crappy week for defenders! So, I didn't get a chance to research the latest vulnerability that dropped named "Node2Shell" until today. When I read the CVE's and took a look at the Node2Shell set of vulnerabilities, I noticed that nearly all of the coverage was talking about Node.js. In fact, the handle is "Node2Shell" modelled after "PHP2Shell", but I digress! The vulnerability isn't really in Node.js at all, but instead the real issue is in Brotli.

## tl;dr

- CVE-2026-111497 (“Node2Shell”) is a vulnerability in Google’s Brotli C decoder, not in Node.js.
- Two Python packages on PyPI are built from that same C source: `Brotli` and `brotlicffi`.
- Every `Brotli` release up to and including **1.2.0** contains the vulnerable decoder. **1.2.1**, published 22 October 2026, is the fix and is otherwise identical to 1.2.0.
- `brotlicffi` releases up to **1.2.0.2** are affected. **1.2.1.0**, published 23 October 2026 with no release notes, is the quiet fix.
- Neither release mentions the vulnerability in its release notes; both packages were silently patched.
- If you have either installed, run `pip install -U "Brotli>=1.2.1" "brotlicffi>=1.2.1.0"`.
- As of today no advisory database lists either PyPI package, so your scanners will not tell you.

## What is Node2Shell?

Node2Shell (CVE-2026-111497) is a high-severity out-of-bounds write in Google’s Brotli decompression library (`c/dec/decode.c`), disclosed on 21 October 2026 by [Imperva](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/). The decoder’s `DecodeBlockTypeAndLength()` returns an ambiguous value when a Brotli stream requests a block-type switch that the stream never validly declared, and the fast decode path discards that return value (an unchecked-return-value flaw, CWE-252), so the decoder keeps running on corrupted internal state and writes past its ring buffer (CWE-787). Because it lives in the shared C library rather than any one runtime, it reaches everything that bundles that decoder — Node.js (where it’s reachable pre-auth through `fetch()`, Express 5 / body-parser request bodies, and `node:zlib`, earning the “Node2Shell” name), Bun, and the PyPI `Brotli`/`brotlicffi` packages — and can crash a process, leak memory, or potentially lead to remote code execution. It’s rated CVSS 4.0 9.2 (Critical) and is fixed in Brotli 1.2.1 / 1.1.1 / 1.0.10 (and Node.js 22.23.4 / 24.22.1 / 26.12.1).

## Back to brotli

Brotli is a popular lossless compression algorithm written in C and maintained by Google on [GitHub](https://github.com/google/brotli).  It has 15 thousand stars, 131 contributors and is used by more than 100k other packages!

Now the thing with Node2Shell is that you don't need to load or import the brotli NPM package to be vulnerable to the bug. Node bundles the C code into all versions of Node 20.x, 22.x and 24.x (before they were patched). But there absolutely is a NPM package named [brotli](https://www.npmjs.com/package/brotli).

At OpenSourceMalware, we don't usually do software vulnerabilities. We're known for software supply chain malware research. But because I'm familiar with the library, I knew there was at least one Python package too, so I decided to take a closer look. That’s when I noticed the maintainers had quietly updated the official [brotli](https://pypi.org/project/brotli/) PyPI package today.

Hmmm, that's a bit suspicious!  I did a comparison between version 1.2.0 and 1.2.1 and sure enough there was a difference.  It turns out that there's another brotli package named [brotlicffi](https://pypi.org/project/brotlicffi/) that was also updated quietly today:

I then went looking for an existing vulnerability record for the Python `Brotli` package in OSV, PYSEC and GHSA, and I didn’t find one. The rest of this post is what I found.

## "Node2Shell" Background

On 21 October 2026, Node.js shipped versions 22.23.4, 24.22.1 and 26.12.1 for CVE-2026-111497, a critical-severity out-of-bounds write in its bundled Brotli decoder, reachable through `fetch()`, Express 5 / body-parser 2.x request bodies, and `node:zlib`. Imperva and others reproduced code execution against stock Node builds, and the bug picked up the name Node2Shell.

What most coverage glossed over is that the vulnerable code lives in `c/dec/decode.c` in [google/brotli](https://github.com/google/brotli). Node.js vendors a copy. So do Bun, several Linux distros, and — the subject of this post — two Python packages on PyPI (Google’s official `Brotli` binding and the CFFI-based `brotlicffi`). The CVE record confirms this. It was assigned by Google, not by Node.js, and names `github.com/google/brotli` as the affected product, versions 1.0.3–1.2.0.

## Root cause

`DecodeBlockTypeAndLength()` handles a “block switch”, where a Brotli stream changes which Huffman tree is used for literals, commands or distances. In the vulnerable code it returns a plain boolean:

```
static BROTLI_INLINE BROTLI_BOOL DecodeBlockTypeAndLength(
    int safe, BrotliDecoderState* s, int tree_type) {
  brotli_reg_t max_block_type = s->num_block_types[tree_type];
  ...
  if (max_block_type <= 1) {
    return BROTLI_FALSE;   /* stream is invalid: a switch with only one block type */
  }
  ...
  if (!SafeReadSymbol(type_tree, br, &block_type)) return BROTLI_FALSE;  /* need more input */
```
`BROTLI_FALSE` means two different things here: “this stream is malformed” and “I ran out of input”. The callers can’t tell them apart, and on the fast (“unsafe”) path the return value is discarded outright:

```
#define BROTLI_SAFE(METHOD)                       \
  {                                               \
    if (safe) {                                   \
      if (!Safe##METHOD) {                        \
        result = BROTLI_DECODER_NEEDS_MORE_INPUT; \
        goto saveStateAndReturn;                  \
      }                                           \
    } else {                                      \
      METHOD;                                     \
    }                                             \
  }
```
So a stream that declares a single block type and then exhausts that block’s length forces a switch that can’t succeed. The decoder either reports “needs more input” for a stream that is complete, or carries on with the block state it had, which is where the out-of-bounds write comes from.

The upstream fix, [google/brotli@0ed4268](https://github.com/google/brotli/commit/0ed4268a4401abcb44720963) (“Detect and report invalid stream earlier”), changes the function to return a `BrotliDecoderErrorCode`, adds a new error `BROTLI_DECODER_ERROR_FORMAT_BLOCK_SWITCH` (−17), and replaces `BROTLI_SAFE` with a `BROTLI_SAFE_WITH_STATUS` macro at the three block-switch call sites so a format error stops decoding on both paths. The CWE pairing in the CVE record is apt: CWE-252 (unchecked return value) leading to CWE-787 (out-of-bounds write).

## Why the PyPI packages are affected by Nodes2Shell

The `Brotli` package on PyPI is Google’s own CPython extension. Its sdist contains the full `c/` tree and compiles `c/dec/decode.c` into the module. Diffing the 1.2.0 and 1.2.1 sdists:

```
$ diff -rq brotli-1.2.0 brotli-1.2.1 | grep -v PKG-INFO
Files brotli-1.2.0/c/common/version.h and brotli-1.2.1/c/common/version.h differ
Files brotli-1.2.0/c/dec/decode.c and brotli-1.2.1/c/dec/decode.c differ
Files brotli-1.2.0/c/include/brotli/decode.h and brotli-1.2.1/c/include/brotli/decode.h differ
```
Three files. `version.h` is the version bump. The `decode.c` and `decode.h` changes are commit 0ed4268, line for line. 1.2.1 is a pure security release for CVE-2026-111497, yet the release notes make no mention of the vulnerability. It was silently patched.

Looking further back, the same unchecked `DecodeBlockTypeAndLength` → `BROTLI_SAFE` pattern is present in every PyPI release we checked: 1.2.0, 1.1.0, 1.0.9, 1.0.7, 0.6.0 and 0.5.2. The 0.x decoders predate the `max_block_type <= 1` early return that Google’s record treats as the introduction point, but they also fail to report the invalid transition, so there is no safe older version to fall back to.

`brotlicffi` is a separate project (the CFFI alternative used on PyPy) that vendors the same C source, so it inherits the bug. Its release history lines up with the upstream timeline: 1.2.0.1 (6 March 2026) and 1.2.0.2 (22 August 2026) bundle the vulnerable 1.2.0 decoder, and 1.2.1.0 (23 October 2026) is a quiet update published a day after the upstream fix. Like `Brotli` 1.2.1, its release notes make no mention of the CVE or the vulnerability; it was silently patched. We have not diffed or fuzzed the `brotlicffi` sdists the way we did for `Brotli` below.

### Testing

To see if the Python packages were indeed susceptible to the same vulnerability, we built the `Brotli` 1.2.0 and 1.2.1 sdists from PyPI with AddressSanitizer and ran a crafted stream through the decoder. That gave us a single literal and distance block type, and enough commands to run the distance block counter to zero, forcing the invalid switch. We used both a C harness against each sdist’s decoder (to see the exact error code) and the Python module itself.

Input

Brotli 1.2.0

Brotli 1.2.1

Crafted stream, one shot

consumes all \~23 MB, returns `NEEDS_MORE_INPUT`

`ERROR −17 FORMAT_BLOCK_SWITCH`

Same stream in 1-, 13-, 4096- and 65536-byte chunks

`NEEDS_MORE_INPUT` every time

`ERROR −17` every time

That is the vulnerable behaviour exactly as described by [Imperva](https://www.imperva.com/blog/node2shell-from-brotli-data-to-remote-code-execution/) and in the fix commit: the decoder treats a malformed, complete stream as incomplete and keeps going with invalid state. The patched decoder rejects it before any further processing. We did not pursue the memory-corruption or code-execution side in the Python extension; the Node.js write-ups cover that, and the code is the same.

Note for anyone reproducing this from Python: `brotli.decompress()` raises a bare `brotli.error: decoder failed` for any error, so you can’t see which error code fired from Python alone. A `Decompressor()` fed the stream incrementally will simply never finish on 1.2.0.

### Affected versions

`Brotli`

`brotlicffi`

Registry

PyPI

PyPI

Affected

all releases ≤ 1.2.0 (0.5.2, 0.6.0, 1.0.1, 1.0.4, 1.0.6, 1.0.7, 1.0.8, 1.0.9, 1.1.0, 1.2.0)

releases bundling the 1.2.0 decoder, including 1.2.0.1 (6 March 2026) and 1.2.0.2 (22 August 2026); earlier releases not checked

Fixed

1.2.1 (22 October 2026)

1.2.1.0 (23 October 2026)

Upstream

google/brotli 1.0.3–1.0.9, 1.1.0, 1.2.0 → fixed in 1.0.10, 1.1.1, 1.2.1

CVE

CVE-2026-111497 (CNA: Google), CVSS 4.0 9.2

In practice 1.1.0 and 1.2.0 are the `Brotli` versions that matter. 1.1.0 was the only release between August 2023 and October 2025, so it is what most environments have pinned. For `brotlicffi`, the 1.2.0.x line is the one to look for.

### Who is exposed on the Python side

The exposure mirrors Node’s. If `Brotli` is importable, the common HTTP clients advertise `Accept-Encoding: br` and decode Brotli responses automatically:

- `urllib3` (and therefore `requests`) when `Brotli` or `brotlicffi` is installed
- `httpx` with the `brotli` extra
- `aiohttp` when `Brotli` is installed
- Scrapy, and anything built on the above

So any Python service that fetches from servers it does not control — webhook delivery, URL previews, crawlers, SSRF-adjacent “fetch this URL” features — is handing attacker-controlled data to the vulnerable decoder. On the inbound side, any framework or middleware that decodes `Content-Encoding: br` request bodies is the equivalent of the Express 5 case.

## How to remediate

1. `pip install -U "Brotli>=1.2.1" "brotlicffi>=1.2.1.0"` and rebuild any container images or wheels that bundle either.
2. Check `pip show Brotli` and `pip show brotlicffi` in every environment; `pip-audit`. Tools like Dependabot and Safety will **not** flag this yet.
3. If you can’t upgrade immediately, you can uninstall `Brotli` and `brotlicffi` (the HTTP clients above fall back to gzip/deflate without them) or strip `br` from `Accept-Encoding` on outbound requests and reject `Content-Encoding: br` on inbound ones.

## Advisory status

As of 23 October 2026:

- The CVE record lists `github.com/google/brotli` as the affected product with commit and version ranges. It does not mention PyPI.
- OSV has the CVE, imported from the record, with a Git range only. A query for `PyPI/Brotli 1.2.0` or `PyPI/brotlicffi 1.2.0.2` returns nothing for this bug.
- The GitHub Advisory Database entry for the CVE lists no PyPI package.
- google/brotli has published no repository security advisory.

We are submitting PYSEC entries to the PyPA advisory database for both packages and a PyPI package mapping to the GitHub advisory so that tooling picks this up. Until then, treat this post as the advisory.
