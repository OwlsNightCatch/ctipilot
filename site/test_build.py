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
    parse_footer_line,
    parse_taxonomy,
    render_inline,
    render_markdown,
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
