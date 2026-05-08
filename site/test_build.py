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
