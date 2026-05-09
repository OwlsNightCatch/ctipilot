# Security review — ctipilot

Pre-fix walk-through of trust boundaries, the data path from publishers
through the agent into the published site, and the residual exposure each
boundary carries. Findings and fixes follow.

This is **not** a claim that the system is fully secure — it is a record of
what was hardened, what was deliberately left alone (per the user's
"accepted risks"), and what residual exposure remains.

---

## 1. Component inventory

| # | Component | Path | Trust |
|---|-----------|------|-------|
| C1 | Daily / weekly agent prompts | `prompts/daily-cti-brief.md`, `prompts/weekly-summary.md` | Semi-trusted (the agent edits them — by design) |
| C2 | Source list | `sources/sources.json` | Semi-trusted (agent-mutable; controls fetch surface) |
| C3 | State store | `state/{cves_seen,covered_items,deep_dive_history,run_log}.json` | Semi-trusted (agent-mutable working memory) |
| C4 | Brief markdown files | `briefs/YYYY-MM-DD.md`, `briefs/weekly/YYYY-Www.md` | Untrusted at render boundary (transitively reflects publisher content) |
| C5 | Vendored JS libraries | `site/assets/vendor/{marked,purify,filter}.min.js` + `HASHES` | Trusted (SHA-256 pinned; build aborts on mismatch) |
| C6 | First-party site JS | `site/assets/js/{theme,search,app,spa-redirect}.js` | Trusted |
| C7 | Site builder | `site/build.py` | Trusted (single Python file; renders Markdown → HTML; emits CSP) |
| C8 | Build smoke tests | `site/test_build.py` | Trusted |
| C9 | Brief self-check | `tools/check_brief.py` | Trusted (run by the agent in Phase 5.5) |
| C10 | Outbound fetch bridge | `tools/fetch_source.py` | Trusted (host-allowlist gated GET helper used by the agent for sites that block its UA) |
| C11 | Auto-merge workflow | `.github/workflows/auto-merge-claude.yml` | Trusted |
| C12 | Pages deploy workflow | `.github/workflows/deploy-site.yml` | Trusted |
| C13 | CSS / icons / static assets | `site/assets/css/`, `CNAME`, `.nojekyll` | Trusted |

There is **no** server-side RSS / XML ingestion in this repository. The agent
calls Claude Code's WebFetch tool (out of repo) or `tools/fetch_source.py` to
read sources, never an XML parser. RSS feeds are *emitted* by the build, not
consumed. The XXE / DTD parts of the checklist are therefore N/A for this
codebase, though we still cover their hygiene below.

---

## 2. Entry points

| Direction | Surface | Notes |
|-----------|---------|-------|
| Inbound (agent run-time) | `tools/fetch_source.py` URL → publisher | Host-allowlisted; HTTPS-only; browser UA |
| Inbound (agent run-time) | `WebFetch` from publisher pages → agent context | Outside this repo |
| Inbound (build run-time) | `state/*.json`, `sources/sources.json` → `build.py` | Validated at path-segment / footer-vocab boundary |
| Inbound (build run-time) | `briefs/*.md`, `docs/*.md`, `prompts/CHANGELOG.md` → `build.py` | Allowlist Markdown renderer |
| Inbound (browser run-time) | The published static site | No forms; no inputs ever sent server-side; the search bar is pure-client over `data/search.json` |
| Outbound (agent → repo) | `git push origin claude/<…>` | Auto-merged into main if a strict descendant |
| Outbound (build → Pages) | `gh-pages` branch force-push | One job at a time (concurrency group) |

The published site has **no server-side request handling**: every page is
static HTML from `_site/`, served by GitHub Pages.

---

## 3. Trust boundaries and data flow

```
publisher CMS              ─────► agent context (untrusted text)
  (untrusted, may be             │
   prompt-injected by             │
   third-party XSS)               ▼
                          briefs/*.md  (still untrusted at build-time
                          state/*.json   — the renderer treats every
                          covered_items   string as opaque text)
                                  │
                                  ▼
                       site/build.py renderer
                       (Markdown allowlist → HTML;
                        scheme allowlist on every <a href>;
                        path-segment allowlist;
                        no raw HTML pass-through;
                        no template-rendered shell-out)
                                  │
                                  ▼
                        _site/ static tree
                        (every page emits a strict CSP
                         <meta>, no inline <script>)
                                  │
                                  ▼
                       gh-pages branch (force-push)
                                  │
                                  ▼
                       reader's browser
                       (CSP self + Umami;
                        no cookies, no localStorage exfil
                        surface; no per-visitor identifier)
```

Untrusted data crosses the boundary at **render** in `site/build.py`. Every
mitigation against XSS, path traversal, scheme smuggling, and open-redirect
behaviour lives there or in the vendored asset integrity check.

---

## 4. Pre-fix findings

### F1 — `tools/fetch_source.py` follows redirects without re-validating the destination (SSRF defence-in-depth)

**Location.** `tools/fetch_source.py:138-161` (`fetch()` calls
`urllib.request.urlopen()`, which uses Python's default opener — the default
follows up to ~10 HTTP redirects without invoking `_check_host()` on the
destination).

**Why it's exploitable.** The hostname allowlist on initial request is
defeated if any allowed publisher returns a 30x redirect to an
attacker-controlled host (or, in worst case, to `127.0.0.1`,
`169.254.169.254`, `[fd00:ec2::254]`, link-local, RFC1918, etc.). A
compromised CMS at any allowlisted publisher could pivot the bridge into
fetching arbitrary local URLs. There is no port restriction either.

**Fix.** Override the redirect handler to re-run `_check_host()` on every
redirect destination, refuse non-HTTPS hops, and refuse loopback / link-local
/ private / cloud-metadata hosts (including IPv6). Cap response size and add
a connection timeout in addition to the existing socket timeout. Pin the IP
once after DNS lookup so resolver-rebinding cannot sneak the request to a
different IP after the host check.

---

### F2 — `tools/fetch_source.py` reads the entire body without an inflate / decompression-bomb cap

**Location.** `tools/fetch_source.py:158` (`resp.read()` returns the full
body; no size ceiling).

**Why it's exploitable.** A malicious publisher (or attacker via the
redirect path in F1) can serve an arbitrarily large body, exhausting the
runner's memory. With the existing `Accept-Encoding: identity` header,
gzip-bombs are precluded, but uncompressed multi-GB bodies are still
possible.

**Fix.** Read in bounded chunks; abort with `RuntimeError` after a hard cap
(default 25 MB for HTML / 50 MB for the CISA KEV JSON, which legitimately
hits ~6 MB).

---

### F3 — `tools/check_brief.py` URL-liveness probe follows redirects unbounded

**Location.** `tools/check_brief.py:846-848` (`urlopen(req, timeout=…)` with
default redirect handler; default opener follows up to 10 redirects without
host re-validation).

**Why it's exploitable.** Same shape as F1, but for a script the operator
runs locally. A redirect to `http://127.0.0.1:8080/admin/` or to
`http://169.254.169.254/latest/meta-data/iam/security-credentials/` would be
followed when the operator runs `check_brief.py` on a host where local
services exist. Liveness is a defensive operator tool — it should not become
an SSRF foothold.

**Fix.** Use a redirect handler that refuses non-https hops and any
loopback / link-local / private / cloud-metadata destination. Cap response
size during liveness checks (we only need the status code).

---

### F4 — Markdown renderer does not strip ASCII control characters in input

**Location.** `site/build.py:478-628` (`render_markdown` and
`render_inline`); `_safe_url` strips control chars from URLs but not from
text.

**Why it's exploitable today.** Mostly a defence-in-depth concern. The
renderer uses `\x00CODE…\x00` and `\x00LINK…\x00` placeholder markers for
code spans and links during inline rendering. If an attacker can place a
literal `\x00` in a brief, an injected `\x00LINKn\x00` token may collide
with a legitimate placeholder and substitute attacker-controlled text into
the link's place. The end-of-build self-check refuses output that contains
`\x00` (line 3495), so this manifests as a build-fail — bad for service
availability but not XSS. Still, controls characters in the input have no
legitimate purpose and should be stripped at the parse boundary.

**Fix.** Strip ASCII control characters (`\x00-\x08`, `\x0B-\x0C`,
`\x0E-\x1F`, `\x7F`) from brief / docs / state-string input before rendering
and from placeholder substrings before substitution. Keep `\t`, `\n`, `\r`.

---

### F5 — Markdown renderer accepts protocol-relative URLs that escape the site origin

**Location.** `site/build.py:338-369` (`_safe_url`).

**Why it's exploitable today.** A Markdown link `[click](//evil.com/x)`
goes through `_safe_url`, which detects the first special character is `/`
(at position 0), concludes "no scheme present", and returns the URL
unchanged. The browser interprets `//evil.com/x` as a protocol-relative URL
and navigates to `https://evil.com/x` on click. This is **not** XSS — the
strict CSP would still block any script — but it lets brief content open
visitor browsers to attacker domains with neither `http(s)://` nor a
recognisable scheme in the rendered href.

**Fix.** In `_safe_url`, treat any URL starting with `//` or whose path
begins with `\\` as needing the same scheme allowlist treatment as one
with an explicit scheme. Either reject (`#`) or rewrite to a relative path.

---

### F6 — No write-time secret redactor before commit / page render

**Why it matters.** The agent is allowed to mutate its own prompt and to
write briefs autonomously. A hallucinating run could paste an environment
variable value, a token from the runner shell, or a string the agent
recognised as a credential, into a brief or state file. Once on `main`,
auto-merge propagates it to Pages and to RSS readers within minutes.

**Fix.** Add a redactor that scans every emitted brief, every page, and the
search-index JSON for known secret-shaped patterns (GitHub tokens
`ghp_…`/`ghs_…`/`github_pat_…`, AWS access keys `AKIA…`, Anthropic API
keys `sk-ant-…`, generic JWTs `eyJ…`, PEM blocks). Refuse the build with
a clear error. This is *not* a substitute for keeping secrets out of the
runner — it is a last-ditch guard against the autonomous agent
accidentally leaking one.

---

### F7 — No hard cap on input file sizes processed by the build

**Location.** `site/build.py` `parse_brief()` (line 910), the loop in
`main()` reads every `briefs/*.md` and renders it.

**Why it's exploitable.** A poisoned state file or a runaway agent run
could plant an oversize markdown file (hundreds of MB) and the build would
attempt to load and render it, potentially OOM'ing the runner. Resource
exhaustion → no daily site update → covertly silenced feed.

**Fix.** Per-file ceilings: 4 MB for an individual brief, 4 MB per docs
file, 16 MB for the longest state file (covered_items.json), and a global
ceiling of ~100 MB for the briefs directory. Refuse the build above the
cap with a clear stderr message.

---

### F8 — Vendored library integrity check uses the SHA-256 line but does not also check the SHA-384 line listed in `HASHES`

**Location.** `site/build.py:233-270` (`verify_vendored_hashes`) only reads
lines whose first column is `sha256`. The `HASHES` file also lists
`sha384` digests for cross-check; those are silently ignored.

**Why it matters.** Defence-in-depth: a single-algorithm collision is
infeasible today, but checking both algorithms makes a future tampered
binary fail a hash family the attacker did not know was checked. Cost is
trivial.

**Fix.** Verify both `sha256` and `sha384` lines in `HASHES` against the
on-disk bytes; abort on either mismatch.

---

### F9 — `urljoin` lets a brief use a base URL to bypass the scheme allowlist

**Location.** `site/build.py:392-401`.

**Why it's exploitable.** `urljoin(base_url, url)` is called *before*
`_safe_url(url)`. If `url` is `mailto:?body=javascript:alert(1)`, `urljoin`
returns the same string and `_safe_url` sees `mailto:`, allowed. That is
fine. But if `url` is `\\\\attacker.com\\x` (URI-relative reference with
backslashes — interpreted as a UNC path on Windows browsers and as
`//attacker.com/x` on others), `urljoin` may pass it through unchanged and
`_safe_url` does not handle leading-backslash URLs.

This is the same class as F5 with a different syntactic shape.

**Fix.** Same as F5 — normalise URLs with leading `/` `\` runs to relative
paths, or reject.

---

### F10 — No `.well-known/security.txt` constraint on path traversal

**Location.** `site/build.py:3443-3456` (`write_security_txt`).

This was not actually a finding — the path is hard-coded under `OUT`.
Removed from the list before final write.

---

### F11 — `python3 site/build.py` requires Python ≥ 3.12 at line 1695 (f-string with backslash in expression)

**Location.** `site/build.py:1695`. `f-string expression part cannot
include a backslash` on Python < 3.12 (PEP 701 lifted the restriction in
3.12).

**Why it matters (security-adjacent).** This is a correctness regression
that prevents the build from running on Python 3.11. GitHub Actions'
`ubuntu-latest` image currently ships Python 3.12, so CI is unaffected,
but a slightly older runner (or a local operator on Ubuntu 22.04) would
fail to build. A "site cannot be rebuilt" condition is a soft availability
issue rather than security; documented here so the operator can decide.

**Fix.** Refactor the f-string to remove the backslash (use a temporary).

---

### F12 — `style-src 'unsafe-inline'` in CSP

**Location.** `site/build.py:1288` (`CSP_META`).

**Why it's a residual risk.** The build emits inline `style="…"`
attributes throughout the templates (panel layouts, helper offsets). The
renderer never lets brief content emit a `<style>` block (no Markdown
construct produces one) or a `style="..."` attribute, so the practical
attack surface is small — an injection would need a renderer bug *and* a
useful inline-style payload. Removing `'unsafe-inline'` would require
sweeping the templates for inline styles or moving them to CSS classes;
a meaningful refactor outside this review.

**Decision.** Documented as residual; not changed in this review.

---

### F13 — `frame-ancestors` cannot be delivered from a `<meta>` CSP, and GitHub Pages does not support custom HTTP headers

**Why it's a residual risk.** Clickjacking defence relies on
`X-Frame-Options` or `frame-ancestors`. GitHub Pages does not let us send
either. This is a deployment-platform limitation. The site has no forms,
no actions, and no per-visitor state, so a successful frame would only
display to a victim what a public reader sees anyway.

**Decision.** Documented as residual; cannot be fixed in-repo.

---

### F14 — `X-Content-Type-Options: nosniff` and `Referrer-Policy: no-referrer` are not delivered

**Why.** Same as F13: GitHub Pages strips arbitrary headers. The closest
in-document approximation is `<meta name="referrer">` (already set to
`strict-origin-when-cross-origin`). MIME sniffing is not pertinent for the
site's outputs (every served file has the correct extension), so the
practical impact of missing `nosniff` is minimal.

**Decision.** `<meta name="referrer">` already present. `nosniff`
documented as residual.

---

## 5. Accepted risks (per user instruction)

The user explicitly carved these out as out-of-scope:

- **The agent edits its own prompt and the docs autonomously.** `prompts/*`
  and `docs/improvements.md` are mutable by the agent; we do not add a
  signing or human-review gate. Drift control is editorial (CHANGELOG
  discipline, the build's footer-taxonomy validator, and the existing
  `docs/security-review.md` runbook).
- **`claude/*` → `main` auto-merges, and Pages auto-deploys.** No human in
  the loop. The auto-merge workflow's existing fast-forward-only check
  (`merge-base --is-ancestor main origin/<branch>`) and its branch-name
  allowlist (`[A-Za-z0-9._/-]` only, refuses `claude/foo$(curl evil)`)
  are the only gates we add.

These were not changed.

---

## 6. Findings → fixes (post-fix summary)

| ID | Status | Fix location |
|----|--------|--------------|
| F1 SSRF / redirect-rebinding in `fetch_source.py` | **Fixed** | `tools/fetch_source.py` — `SafeRedirectHandler`, `_check_url`, `_resolve_and_check`, `_ip_is_blocked` |
| F2 No body-size cap in `fetch_source.py` | **Fixed** | `tools/fetch_source.py` — `_read_capped`, `MAX_BODY_BYTES_HTML`, `MAX_BODY_BYTES_JSON` |
| F3 SSRF / redirect in `check_brief.py` URL-liveness | **Fixed** | `tools/check_brief.py` — `_SafeRedirectHandler`, `_host_is_blocked`, `_ip_is_blocked_local` |
| F4 Renderer doesn't strip ASCII control characters | **Fixed** | `site/build.py` — `_strip_controls`, `_CONTROL_CHAR_RE`; called at `render_inline`, `render_markdown` entry |
| F5 Protocol-relative URLs survive scheme-allowlist | **Fixed** | `site/build.py` — `_safe_url` rejects `//…`, `\\…`, `/\…`, `\/…` |
| F6 No write-time secret redactor | **Fixed** | `site/build.py` — `scan_for_secrets`, `_SECRET_PATTERNS`, wired into `self_check` |
| F7 No file-size caps on inputs | **Fixed** | `site/build.py` — `_read_text_capped`, `MAX_BRIEF_BYTES`, `MAX_STATE_BYTES`, `MAX_VENDOR_BYTES`, `MAX_BRIEFS_DIR_BYTES` |
| F8 Vendored-library check verified only SHA-256 | **Fixed** | `site/build.py` — `verify_vendored_hashes` now also verifies SHA-384 |
| F9 `urljoin` could pass leading-backslash URLs | **Fixed (covered by F5)** | Same `_safe_url` change handles backslash leads |
| F11 Build required Python ≥ 3.12 (f-string-with-backslash) | **Fixed** | `site/build.py:1696` and `:3310` rewritten without backslash-in-expression |
| F12 `style-src 'unsafe-inline'` | **Accepted residual** | Refactor would touch every template; out of scope for this review. Documented. |
| F13 `frame-ancestors` cannot be delivered via `<meta>` | **Accepted residual** | GitHub Pages limitation; documented. |
| F14 `X-Content-Type-Options: nosniff` not delivered | **Accepted residual** | GitHub Pages limitation; documented. |
| Defense-in-depth: XML validator could be tricked into XXE/billion-laughs if input ever became untrusted | **Hardened** | `site/build.py` `_xml_validate` now refuses any document containing `<!DOCTYPE` or `<!ENTITY` declarations. |

### Fixed-finding tests

The following regression tests were added to `site/test_build.py`:

- `_safe_url` neuters `//evil.example/x`, `\\evil.example\x`, `/\evil.example/x`, `\/evil.example/x` (protocol-relative defence).
- `render_inline` neuters protocol-relative URLs in Markdown link form.
- `_strip_controls` strips NUL / DEL / ESC / BEL / other C0 controls; preserves `\t`, `\n`, `\r`.
- `render_inline` drops literal NUL bytes from input even when the input mimics the renderer's internal placeholder shape.
- `scan_for_secrets` flags AWS access-key IDs, GitHub classic and fine-grained PATs, Anthropic keys, Google API keys, PEM private-key blocks, and JWT-shaped tokens.
- `_xml_validate` refuses billion-laughs and external-DTD XML inputs.

End-to-end check: planting `AKIAIOSFODNN7EXAMPLE` in a brief and running
the build produces a non-zero exit (`return 4`) and prints
`secret-shaped token in …: AWS access key id`.

### Other corrections during the review

- Tightened the regex for AWS access keys, GitHub PATs, Anthropic and
  Google API keys, and JWT tokens (initial drafts had length boundaries
  that produced false negatives on real-shape examples).
- Added explicit IPv6 coverage to the `_ip_is_blocked` helpers — the
  `ipaddress.ip_address` check now covers `::1`, `fd00::/8`, link-local
  `fe80::/10`, multicast, etc.

### Scanners — final state

- **`bandit -ll site/build.py tools/`** — 0 medium / 0 high. 8 low
  findings remain, all accepted: `B101` (asserts in test code), `B404` /
  `B603` / `B607` (subprocess invocations of `git` / `sys.executable`
  with arg arrays, no shell), `B110` (try/except/pass for
  best-effort cleanup paths), and one `B310` urlopen flagged in
  `check_brief.py` and `fetch_source.py` — both call sites are now
  wrapped in the `_SafeRedirectHandler` / allowlist gate.
- **`gitleaks` / equivalent grep over full history** — no API keys,
  PEMs, JWTs, or credential-shaped tokens found in any branch or tag.
  The `_SECRET_PATTERNS` set is now baked into the build's self-check
  so future regressions fail-closed.
- **No `pickle`, no `yaml.load`, no `eval`, no `exec`, no `Function`,
  no `vm.runInThisContext`** anywhere in the codebase.

### Existing controls that were verified and left in place

- Path-segment allowlist (`is_safe_path_segment`) on every state-file
  ID before it becomes a URL or filesystem path; defence-in-depth
  realpath check in `emit_html` refuses any output path that resolves
  outside `_site/`.
- Atomic writes (`tempfile.mkstemp` + `os.replace`) for every emitted
  file. Skipping rewrites of unchanged content keeps the build
  deterministic and idempotent.
- Strict CSP `<meta>` with no `'unsafe-eval'`, `script-src` restricted
  to `'self'` plus the Umami CDN, no third-party `connect-src` beyond
  the Umami beacon.
- Vendored-library SHA-256 + SHA-384 check; build aborts on mismatch.
- End-of-build self-check refuses to publish: an HTML page without
  exactly one Umami `<script>` tag, an HTML page with an inline
  `<script>` block, a markdown-renderer placeholder leak (`\x00CODE…`),
  a UTM parameter on any URL, an XML feed that fails to parse, an XML
  feed containing a `<!DOCTYPE>` or `<!ENTITY>`, or any file containing
  a known secret-shaped token.
- Auto-merge workflow's branch-name allowlist (`[A-Za-z0-9._/-]`) and
  fast-forward-only check (`merge-base --is-ancestor`).
- Both workflows: untrusted strings (`github.event.inputs.branch`,
  `github.ref_name`) are passed via `env:` rather than spliced into
  `run:` shell bodies.
- Both workflows: no third-party Actions; per-job
  `permissions: contents: write` only; concurrency groups in place.

---

## 7. Residual risk

What remains, in plain words:

1. **A renderer bug** that lets a forbidden HTML construct slip through
   `render_markdown`. Bounded by the small set of constructs the
   renderer supports, the `_safe_url` allowlist, the strict CSP, and
   the regression tests; not impossible.
2. **Compromise of the Claude Code routine credential.** The auto-merge
   workflow trusts whatever lands on a `claude/*` branch as long as
   it's a strict descendant of `main`. A leaked GitHub App token or
   API trigger token allows arbitrary publication. Mitigation lives
   outside this repo (rotate the token, scope the App install).
3. **Correlated prompt injection across two HIGH-reliability
   publishers.** Two-source verification fails when the same vendor
   release is reproduced verbatim. The agent's editorial discipline
   and the `[SINGLE-SOURCE-…]` flagging are the ad-hoc gates here;
   no automated check distinguishes "two sources, independently
   verified" from "two sources, same press release".
4. **Missing transport-layer headers** (`X-Frame-Options`,
   `X-Content-Type-Options: nosniff`, HTTP-header CSP). GitHub Pages
   does not let us send them. The site has no per-visitor state, no
   forms, and no privileged client API, so the practical impact is
   small; clickjacking would frame public read-only content.
5. **Subtle prompt drift** that weakens an editorial rule but does
   not change the brief structure. Handled out of band by the
   CHANGELOG discipline and the human reading `git log --
   prompts/` periodically. Not automated.

These are the failure modes worth re-examining at the next review.
The system is hardened in the layers it can be hardened in — input
allowlists, output sanitisation, transport-layer minimums where the
host platform permits, build-time integrity checks, and a
fail-closed self-check at every stage.

It is **not** "fully secure" or "perfectly hardened". This document
records what was hardened, what was deliberately accepted as
residual, and where the next round of work should focus.

