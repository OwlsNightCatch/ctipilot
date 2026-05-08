#!/usr/bin/env python3
"""Stdlib-only smoke tests for site/build.py.

Run with: `python3 site/test_build.py` from the repo root. Returns
exit code 0 on pass, 1 on any failure. Used as a Phase 5.5-style
gate by the agent and by CI.

Tests cover:
    - Markdown → HTML rendering: no Markdown control characters survive
      into positions where they should have been converted
    - Metadata footer parser: round-trip of normative samples
    - Taxonomy validation: unknown values are flagged
    - RSS body rendering: no `**...**` or `[..](http..)` remains
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent

sys.path.insert(0, str(SITE))
from build import (  # noqa: E402
    _cdata_safe,
    _safe_url,
    _strip_footer_metadata_in_md,
    is_safe_path_segment,
    parse_brief,
    parse_footer_line,
    parse_taxonomy,
    render_inline,
    render_markdown,
    render_footer_html,
    section_key_for,
    validate_footer,
)


FAILURES: list[str] = []


def assert_eq(name: str, got, want) -> None:
    if got == want:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}")
        print(f"  FAIL {name}: got {got!r}, want {want!r}")


def assert_in(name: str, needle: str, hay: str) -> None:
    if needle in hay:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: {needle!r} not in {hay[:200]!r}")
        print(f"  FAIL {name}")


def assert_not_in(name: str, needle: str, hay: str) -> None:
    if needle not in hay:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: {needle!r} found in {hay[:200]!r}")
        print(f"  FAIL {name}: {needle!r} found")


def assert_match(name: str, pattern: str, hay: str) -> None:
    import re

    if re.search(pattern, hay):
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: pattern {pattern!r} not in {hay[:200]!r}")
        print(f"  FAIL {name}")


# ---------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------
print("== render_inline ==")
assert_eq(
    "bold renders as strong",
    render_inline("a **bold** term"),
    "a <strong>bold</strong> term",
)
assert_eq(
    "italic renders as em",
    render_inline("a *slanted* term"),
    "a <em>slanted</em> term",
)
assert_eq(
    "inline code renders as code",
    render_inline("the `key` is here"),
    "the <code>key</code> is here",
)

link_html = render_inline("see [the advisory](https://example.com/cve)")
assert_in("link href present", 'href="https://example.com/cve"', link_html)
assert_not_in("link bracket leak", "[the advisory]", link_html)
assert_not_in("link paren leak", "(https://example.com", link_html)

# Regression: inline code inside a link label used to leak the renderer's
# placeholder marker (\x00CODE0\x00) which browsers strip to literal
# "CODE0" text. See README/about page render bug.
nested_html = render_inline("rules in [`docs/verification.md`](docs/verification.md), and `briefs/`.")
assert_in("nested code inside link rendered", "<code>docs/verification.md</code>", nested_html)
assert_in("outer code rendered", "<code>briefs/</code>", nested_html)
assert_not_in("no \\x00 marker leak", "\x00", nested_html)
assert_not_in("no CODE0 placeholder leak", "CODE0", nested_html)


print("== render_markdown ==")
md = """## Heading

A paragraph with **bold** and a [link](https://example.com).

- bullet one
- bullet two

```python
print("hi")
```
"""
html = render_markdown(md)
assert_in("h2 emitted", "<h2", html)
assert_in("strong emitted", "<strong>bold</strong>", html)
assert_in("link emitted", 'href="https://example.com"', html)
assert_in("ul emitted", "<ul>", html)
assert_in("pre code emitted", "<pre>", html)
assert_not_in("no raw bold tokens", "**bold**", html)
assert_not_in("no raw link tokens", "[link]", html)


# ---------------------------------------------------------------------
# Footer parsing
# ---------------------------------------------------------------------
print("== parse_footer_line ==")
tax = parse_taxonomy(SITE / "taxonomy.yaml")

cve_footer = (
    "— *Source: [Palo Alto Networks Security Advisory]"
    "(https://security.paloaltonetworks.com/CVE-2026-0300) · "
    "Tags: rce, zero-day, actively-exploited, cisa-kev · "
    "Region: global · CVE: CVE-2026-0300 · CVSS: 9.3 · "
    "Vector: zero-click · Auth: pre-auth · "
    "Status: exploited, cisa-kev, no-patch*"
)
parsed = parse_footer_line(cve_footer)
assert parsed is not None, "footer parsed"
assert_eq("source url", parsed["sources"][0]["url"], "https://security.paloaltonetworks.com/CVE-2026-0300")
assert_eq("tags", parsed["tags"], ["rce", "zero-day", "actively-exploited", "cisa-kev"])
assert_eq("regions", parsed["regions"], ["global"])
assert_eq("cve", parsed["cve"], "CVE-2026-0300")
assert_eq("cvss", parsed["cvss"], "9.3")
assert_eq("vector", parsed["vector"], "zero-click")
assert_eq("auth", parsed["auth"], "pre-auth")
assert_eq("status", parsed["status"], ["exploited", "cisa-kev", "no-patch"])
assert_eq("validation passes", validate_footer(parsed, tax), [])

multi = (
    "— *Source: [The Record](https://therecord.media/a) · "
    "Additional source: [BleepingComputer](https://www.bleepingcomputer.com/b) · "
    "Tags: ransomware, supply-chain, china-nexus · Region: europe, dach*"
)
p2 = parse_footer_line(multi)
assert p2 is not None
assert_eq("two sources", len(p2["sources"]), 2)
assert_eq("two regions", p2["regions"], ["europe", "dach"])
assert_eq("multi validation passes", validate_footer(p2, tax), [])

# Non-footer lines
assert_eq("non-footer rejected", parse_footer_line("just a paragraph"), None)
assert_eq(
    "non-footer with em-dash rejected",
    parse_footer_line("— some prose"),
    None,
)
assert_eq(
    "italic non-footer (no field labels) rejected",
    parse_footer_line("— *just an italic remark, not a footer*"),
    None,
)

# TL;DR aggregate footer (no Source — Tags + Region only).
tldr_agg = "— *Tags: vulnerabilities, actively-exploited, cisa-kev · Region: global, europe*"
p_tldr = parse_footer_line(tldr_agg)
assert p_tldr is not None, "Tags-only footer must parse"
assert_eq("tldr-agg sources empty", p_tldr["sources"], [])
assert_eq("tldr-agg tags",
          p_tldr["tags"],
          ["vulnerabilities", "actively-exploited", "cisa-kev"])
assert_eq("tldr-agg regions", p_tldr["regions"], ["global", "europe"])

# Deep-dive shape: multiple bare-link sources at the head of the footer
# without "Additional source:" prefixes.
deep = (
    "— *Source: [Ivanti Advisory](https://www.ivanti.com/blog/x) · "
    "[NVD CVE-2026-5787](https://nvd.nist.gov/vuln/detail/CVE-2026-5787) · "
    "[NVD CVE-2026-6973](https://nvd.nist.gov/vuln/detail/CVE-2026-6973) · "
    "[Hacker News](https://thehackernews.com/2026/05/ivanti-rce.html) · "
    "Tags: vulnerabilities, actively-exploited, rce, cisa-kev · "
    "Region: global · CVE: CVE-2026-5787, CVE-2026-6973*"
)
p_deep = parse_footer_line(deep)
assert p_deep is not None
assert_eq("deep-dive collects all four bare-link sources",
          len(p_deep["sources"]), 4)
assert_eq("deep-dive primary source url",
          p_deep["sources"][0]["url"], "https://www.ivanti.com/blog/x")
assert_eq("deep-dive last source url",
          p_deep["sources"][3]["url"], "https://thehackernews.com/2026/05/ivanti-rce.html")
assert_eq("deep-dive tags survive",
          p_deep["tags"],
          ["vulnerabilities", "actively-exploited", "rce", "cisa-kev"])


# ---------------------------------------------------------------------
# Taxonomy validation flags unknown values
# ---------------------------------------------------------------------
print("== validate_footer ==")
bad = {
    "sources": [{"label": "x", "url": "https://x"}],
    "tags": ["nope-tag"],
    "regions": ["mars"],
    "sectors": [],
    "cve": None,
    "cvss": None,
    "vector": "telepathy",
    "auth": "guess",
    "status": ["sat"],
}
errs = validate_footer(bad, tax)
assert_in("unknown tag flagged", "unknown tag: nope-tag", " ".join(errs))
assert_in("unknown region flagged", "unknown region: mars", " ".join(errs))
assert_in("unknown vector flagged", "unknown CVE vector: telepathy", " ".join(errs))
assert_in("unknown auth flagged", "unknown CVE auth: guess", " ".join(errs))
assert_in("unknown status flagged", "unknown CVE status: sat", " ".join(errs))


# ---------------------------------------------------------------------
# Issue #2 Defect A — RSS bodies must not carry raw Markdown emphasis.
# Take a representative bullet from a real brief and render it; assert
# the result has `<strong>` and no `**`.
# ---------------------------------------------------------------------
print("== Defect A regression ==")
sample = "**CVE-2026-0300** — *summary*. See [Palo Alto](https://example.com/x)."
rendered = render_inline(sample)
assert_in("rendered strong", "<strong>CVE-2026-0300</strong>", rendered)
assert_in("rendered em", "<em>summary</em>", rendered)
assert_in("rendered link", 'href="https://example.com/x"', rendered)
assert_not_in("no `**` survives", "**", rendered)
assert_not_in("no Markdown link `]( ` survives", "](", rendered)


# ---------------------------------------------------------------------
# Security: URL-scheme allowlist on rendered links
# ---------------------------------------------------------------------
print("== _safe_url ==")
# Allowed schemes pass through unchanged.
assert_eq("http allowed",  _safe_url("http://example.com/x"),  "http://example.com/x")
assert_eq("https allowed", _safe_url("https://example.com/x"), "https://example.com/x")
assert_eq("mailto allowed",_safe_url("mailto:a@b.c"),          "mailto:a@b.c")
assert_eq("tel allowed",   _safe_url("tel:+12345"),            "tel:+12345")
assert_eq("anchor allowed",_safe_url("#section"),              "#section")
assert_eq("relative allowed", _safe_url("foo/bar"),            "foo/bar")

# Dangerous schemes are neutered to '#'.
for hostile in (
    "javascript:alert(1)",
    "JaVaScRiPt:alert(1)",
    "data:text/html,<script>alert(1)</script>",
    "vbscript:msgbox(1)",
    "file:///etc/passwd",
    "about:blank",
    "blob:https://example.com/x",
    "  javascript:alert(1)",
    "java\nscript:alert(1)",
    "java\x00script:alert(1)",
    "java\tscript:alert(1)",
):
    assert_eq(f"hostile {hostile[:25]!r} → #", _safe_url(hostile), "#")
assert_eq("empty url → #", _safe_url(""), "#")

print("== render_inline scheme allowlist ==")
hostile_md = "click [here](javascript:alert(1)) and **bold**"
out = render_inline(hostile_md)
assert_in("hostile link neutered", 'href="#"', out)
assert_not_in("no js: in output",   "javascript:", out)
assert_in("bold still rendered",    "<strong>bold</strong>", out)

hostile_md = "[click](data:text/html,<script>alert(1)</script>)"
out = render_inline(hostile_md)
assert_in("data: neutered", 'href="#"', out)
assert_not_in("no script tag", "<script>", out)
assert_not_in("no data: scheme", "data:text/html", out)


# ---------------------------------------------------------------------
# Security: render_footer_html scheme allowlist
# ---------------------------------------------------------------------
print("== render_footer_html scheme allowlist ==")
footer = {
    "sources": [
        {"label": "Hostile", "url": "javascript:alert(1)"},
        {"label": "Benign",  "url": "https://example.com/article"},
    ],
    "tags": [], "regions": [], "sectors": [],
    "cve": None, "cvss": None, "vector": None, "auth": None, "status": [],
}
html = render_footer_html(footer)
assert_in("benign source survives", 'href="https://example.com/article"', html)
assert_not_in("hostile source neutered", "javascript:", html)
assert_in("hostile source has '#'", 'href="#"', html)


# ---------------------------------------------------------------------
# Security: path-segment allowlist (state-file IDs cannot escape _site/)
# ---------------------------------------------------------------------
print("== is_safe_path_segment ==")
for ok in ("CVE-2026-31431", "ncsc-ch-incidents", "actor.lazarus",
           "tag_name", "actor:Lazarus", "campaign:foo-bar"):
    assert is_safe_path_segment(ok), f"safe id rejected: {ok!r}"
    print(f"  ok  {ok!r} accepted")
for bad in ("..", ".", "./foo", "../etc/passwd", "foo/bar", "foo bar",
            "foo\\bar", "foo\x00bar", "-leading", "", "foo%2Fbar",
            "..foo", "foo..bar", "/abs", ":leading-colon", ".leading-dot"):
    assert not is_safe_path_segment(bad), f"unsafe id accepted: {bad!r}"
    print(f"  ok  {bad!r} rejected")


# ---------------------------------------------------------------------
# Security: CDATA-break defence in RSS body wrappers
# ---------------------------------------------------------------------
print("== _cdata_safe ==")
assert_eq("plain unchanged",
          _cdata_safe("<p>hello</p>"), "<p>hello</p>")
assert_eq("split CDATA terminator",
          _cdata_safe("foo]]>bar"),
          "foo]]]]><![CDATA[>bar")
# A doubled occurrence stays safe.
assert_not_in("no '\\]\\]>' surives doubled", "]]>", _cdata_safe("a]]>b]]>c").replace("]]]]><![CDATA[>", ""))


# ---------------------------------------------------------------------
# Brief parser — heading-prefix variants for TL;DR, Updates section,
# and trailing-divider footer recovery (regressions from 2026-05-08
# brief review).
# ---------------------------------------------------------------------
print("== parse_brief heading variants ==")

_section_brief = """# CTI Daily Brief — 2026-05-08

**Generated by:** Test Model (`test`) · **Classification:** TLP:CLEAR · **Language:** English · **Prompt:** v2.26

## § 1 — TL;DR

- First TL;DR bullet about an Ivanti zero-day.
- Second TL;DR bullet about an APT28 campaign.

---

## § 2 — Immediate Actions

### CVE-TEST-001 — Headline

Body paragraph. Final claim ([Vendor, 2026-05-08](https://example.com/x)).

— *Source: [Vendor PSIRT](https://example.com/x) · Tags: vulnerabilities, actively-exploited · Region: global · CVE: CVE-TEST-001 · CVSS: 9.1 · Vector: zero-click · Auth: pre-auth · Status: exploited, cisa-kev*

---

## § 6 — Updates on Previously Covered Items

### UPDATE — Something

Body. ([Source, 2026-05-08](https://example.com/y)).

— *Source: [Source](https://example.com/y) · Tags: ransomware · Region: europe*

---
"""

# parse_brief computes paths relative to ROOT, so the temp file must
# live inside the repo. Drop it next to the real briefs and clean up.
_tmpdir = ROOT / "briefs" / ".test-tmp"
_tmpdir.mkdir(parents=True, exist_ok=True)
_p = _tmpdir / "2026-05-08.md"
try:
    _p.write_text(_section_brief, encoding="utf-8")
    _b = parse_brief(_p)
finally:
    if _p.exists():
        _p.unlink()
    if _tmpdir.exists():
        _tmpdir.rmdir()

assert_eq("TL;DR bullets parsed under '§ N — TL;DR' heading", len(_b["tldr"]), 2)
assert_in("first TL;DR bullet content", "Ivanti zero-day", _b["tldr"][0])

# Section-key mapping: 'Updates on Previously Covered Items' must map
# to 'updates' (not 'other').
assert_eq("'Updates on Previously Covered' maps to 'updates'",
          section_key_for("§ 6 — Updates on Previously Covered Items"),
          "updates")

# Footer detection survives a trailing '---' horizontal rule that ends
# the H2 section. The CVE-TEST-001 item is the last H3 in § 2 and is
# directly followed by a '---' divider, which used to bury the actual
# footer line.
_imm = next(s for s in _b["sections"] if s["key"] == "immediate-actions")
_first_imm = _imm["items"][0]
assert _first_imm["footer"] is not None, (
    "footer must parse despite trailing '---' divider"
)
assert_eq("footer tags survived ---", _first_imm["footer"]["tags"],
          ["vulnerabilities", "actively-exploited"])
assert_eq("footer status survived ---", _first_imm["footer"]["status"],
          ["exploited", "cisa-kev"])

# Body should NOT include the footer line text or the trailing divider.
assert_not_in("footer line stripped from body", "— *Source:", _first_imm["body_md"])
assert_not_in("trailing divider stripped from body",
              "\n---\n", _first_imm["body_md"] + "\n")


# ---------------------------------------------------------------------
# H4-item fallback + section-level footer detection (Trending Vulns
# uses H4; Deep Dive has no item heading, just a section footer).
# ---------------------------------------------------------------------
print("== parse_brief H4 fallback + section_footer ==")

_h4_brief = """# CTI Daily Brief — 2026-05-08-h4

**Generated by:** Test Model (`test`) · **Classification:** TLP:CLEAR · **Language:** English · **Prompt:** v2.27

## § 1 — TL;DR

- A bullet.

— *Tags: vulnerabilities, actively-exploited · Region: global, europe*

---

## § 4 — Trending Vulnerabilities

#### CVE-TEST-100 — Some product

Body.

— *Source: [NVD](https://nvd.nist.gov/vuln/detail/CVE-TEST-100) · Tags: vulnerabilities, actively-exploited · Region: global · CVE: CVE-TEST-100 · CVSS: 9.0 · Vector: zero-click · Auth: pre-auth · Status: exploited, cisa-kev*

#### CVE-TEST-200 — Another product

Body.

— *Source: [NVD](https://nvd.nist.gov/vuln/detail/CVE-TEST-200) · Tags: vulnerabilities, patch-available · Region: europe · CVE: CVE-TEST-200 · CVSS: 7.5 · Vector: user-interaction · Auth: post-auth · Status: patch-available*

---

## § 7 — Deep Dive: Some Topic

Body of the deep dive.

More body.

— *Source: [Vendor](https://example.com/x) · [NVD](https://nvd.nist.gov/vuln/detail/CVE-TEST-100) · Tags: vulnerabilities, rce, actively-exploited · Region: global · CVE: CVE-TEST-100 · CVSS: 9.0 · Vector: zero-click · Auth: pre-auth · Status: exploited, cisa-kev*

---
"""

_p2 = _tmpdir
_p2.mkdir(parents=True, exist_ok=True)
_pp2 = _p2 / "2026-05-08-h4.md"
try:
    _pp2.write_text(_h4_brief, encoding="utf-8")
    _b2 = parse_brief(_pp2)
finally:
    if _pp2.exists():
        _pp2.unlink()
    if _p2.exists():
        _p2.rmdir()

# H4 items in Trending Vulns.
_tv = next(s for s in _b2["sections"] if s["key"] == "trending-vulnerabilities")
assert_eq("H4 fallback finds 2 items", len(_tv["items"]), 2)
assert_eq("H4 first item heading starts with CVE-TEST-100",
          _tv["items"][0]["heading"].startswith("CVE-TEST-100"), True)
assert _tv["items"][0]["footer"] is not None, "H4 item footer parsed"
assert_eq("H4 footer cve", _tv["items"][0]["footer"]["cve"], "CVE-TEST-100")

# TL;DR aggregate (Tags + Region only) → captured as section_footer.
_tldr_sec = next(s for s in _b2["sections"] if s["key"] == "tldr")
assert _tldr_sec.get("section_footer") is not None, (
    "TL;DR aggregate footer must parse as section_footer"
)
assert_eq("TL;DR section_footer has no source",
          _tldr_sec["section_footer"]["sources"], [])
assert_eq("TL;DR section_footer tags",
          _tldr_sec["section_footer"]["tags"],
          ["vulnerabilities", "actively-exploited"])

# Deep Dive section-level footer with multiple bare-link sources.
_dd = next(s for s in _b2["sections"] if s["key"] == "deep-dive")
assert _dd.get("section_footer") is not None, "Deep Dive section_footer must parse"
assert_eq("Deep Dive section_footer has 2 sources",
          len(_dd["section_footer"]["sources"]), 2)
assert_not_in("Deep Dive section body has no footer line text",
              "— *Source:", _dd["body_md"])


# ---------------------------------------------------------------------
# render_footer_html sources_only mode (RSS body)
# ---------------------------------------------------------------------
print("== render_footer_html sources_only ==")
_full_footer = {
    "sources": [
        {"label": "Vendor", "url": "https://example.com/x"},
        {"label": "NVD", "url": "https://nvd.nist.gov/vuln/detail/CVE-FAKE"},
    ],
    "tags": ["vulnerabilities", "actively-exploited", "rce"],
    "regions": ["global"],
    "sectors": [],
    "cve": "CVE-FAKE",
    "cvss": "9.0",
    "vector": "zero-click",
    "auth": "pre-auth",
    "status": ["exploited", "cisa-kev"],
}
_full_html = render_footer_html(_full_footer)
assert_in("full footer keeps Tags", "Tags:", _full_html)
assert_in("full footer keeps Region", "Region:", _full_html)
assert_in("full footer keeps CVSS", "CVSS:", _full_html)

_so_html = render_footer_html(_full_footer, sources_only=True)
assert_in("sources_only keeps Sources", "Sources:", _so_html)
assert_in("sources_only keeps primary source link",
          'href="https://example.com/x"', _so_html)
assert_not_in("sources_only drops Tags label", "Tags:", _so_html)
assert_not_in("sources_only drops Region label", "Region:", _so_html)
assert_not_in("sources_only drops CVSS label", "CVSS:", _so_html)
assert_not_in("sources_only drops Vector label", "Vector:", _so_html)
assert_not_in("sources_only drops Auth label", "Auth:", _so_html)
assert_not_in("sources_only drops Status label", "Status:", _so_html)
assert_not_in("sources_only drops CVE pill label", "CVE:", _so_html)


# ---------------------------------------------------------------------
# RSS body strip: footer Markdown lines lose their non-Source fields
# but keep the Source(s) intact.
# ---------------------------------------------------------------------
print("== _strip_footer_metadata_in_md ==")
_body_md = (
    "Some intro paragraph.\n\n"
    "— *Source: [Vendor](https://example.com/x) · [NVD](https://nvd.nist.gov/y) · "
    "Tags: vulnerabilities, actively-exploited · Region: global · "
    "CVE: CVE-FAKE · CVSS: 9.0 · Vector: zero-click · Auth: pre-auth · "
    "Status: exploited, cisa-kev*\n"
)
_stripped = _strip_footer_metadata_in_md(_body_md)
assert_in("RSS body keeps primary Source link",
          "[Vendor](https://example.com/x)", _stripped)
assert_in("RSS body keeps secondary Source link",
          "[NVD](https://nvd.nist.gov/y)", _stripped)
assert_not_in("RSS body drops Tags",     "Tags:",   _stripped)
assert_not_in("RSS body drops Region",   "Region:", _stripped)
assert_not_in("RSS body drops CVE",      "CVE:",    _stripped)
assert_not_in("RSS body drops CVSS",     "CVSS:",   _stripped)
assert_not_in("RSS body drops Vector",   "Vector:", _stripped)
assert_not_in("RSS body drops Auth",     "Auth:",   _stripped)
assert_not_in("RSS body drops Status",   "Status:", _stripped)

# Tags-only footer (TL;DR aggregate) collapses to nothing — there is
# no Source to preserve, so the entire italic line is dropped.
_tags_only = "intro\n\n— *Tags: vulnerabilities, actively-exploited · Region: global, europe*\n"
_tags_stripped = _strip_footer_metadata_in_md(_tags_only)
assert_not_in("RSS body drops Tags-only footer entirely",
              "Tags:", _tags_stripped)
assert_not_in("RSS body drops Region-only footer entirely",
              "Region:", _tags_stripped)
assert_in("RSS body keeps the actual prose", "intro", _tags_stripped)

# Regular paragraph italic must NOT be stripped.
_normal = "Some line with *italic emphasis* in it.\n"
assert_eq("italic prose unchanged", _strip_footer_metadata_in_md(_normal), _normal)


# ---------------------------------------------------------------------
# Result
# ---------------------------------------------------------------------
print()
if FAILURES:
    print(f"{len(FAILURES)} failure(s):")
    for f in FAILURES:
        print(f"  · {f}")
    sys.exit(1)
print(f"All tests passed.")
sys.exit(0)
