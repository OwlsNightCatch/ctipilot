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
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent

sys.path.insert(0, str(SITE))
import build  # noqa: E402  -- needed for monkey-patch in fallback test
from build import (  # noqa: E402
    _cdata_safe,
    _extract_bullets_with_footers,
    _safe_url,
    _strip_controls,
    _strip_footer_metadata_in_md,
    _verification_clean_publish,
    _xml_validate,
    file_publish_moment,
    is_safe_path_segment,
    parse_brief,
    parse_footer_line,
    parse_taxonomy,
    render_cve_pill,
    render_inline,
    render_markdown,
    render_footer_html,
    scan_for_secrets,
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
# External links must open in a new tab (the brief is a hub; reader
# clicks citations expecting to keep the brief tab open).
assert_in("external link target=_blank", 'target="_blank"', link_html)
assert_in("external link rel noopener", 'rel="noopener noreferrer"', link_html)

# In-site relative links stay in the current tab.
relative_html = render_inline("see [other section](#anchor)")
assert_in("relative link href present", 'href="#anchor"', relative_html)
assert_not_in("relative link no target", 'target="_blank"', relative_html)

# Regression: inline code inside a link label used to leak the renderer's
# placeholder marker (\x00CODE0\x00) which browsers strip to literal
# "CODE0" text. See README/about page render bug.
nested_html = render_inline("rules in [`prompts/verification.md`](prompts/verification.md), and `briefs/`.")
assert_in("nested code inside link rendered", "<code>prompts/verification.md</code>", nested_html)
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

# v2.66 — closed-source citations (unlinked; document lives under intel/).
cs_only = (
    '— *Closed-source: "Targeting of cantonal e-government portals" '
    "(ISAC-CH weekly bulletin, 2026-07-01, TLP:AMBER, ref: ISACCH-2026-27) · "
    "Tags: phishing, identity · Region: switzerland · Sector: public-sector*"
)
p_cs = parse_footer_line(cs_only)
assert p_cs is not None, "closed-source-only footer must parse"
assert_eq("closed-source sources empty", p_cs["sources"], [])
assert_eq("closed-source count", len(p_cs["closed_source"]), 1)
assert_eq("closed-source title", p_cs["closed_source"][0]["title"],
          "Targeting of cantonal e-government portals")
assert_eq("closed-source provider", p_cs["closed_source"][0]["provider"],
          "ISAC-CH weekly bulletin")
assert_eq("closed-source date", p_cs["closed_source"][0]["date"], "2026-07-01")
assert_eq("closed-source tlp", p_cs["closed_source"][0]["tlp"], "AMBER")
assert_eq("closed-source ref", p_cs["closed_source"][0]["ref"], "ISACCH-2026-27")
assert_eq("closed-source-only footer validates", validate_footer(p_cs, tax), [])

cs_mixed = (
    "— *Source: [Vendor PSIRT](https://vendor.example/psirt/adv-1) · "
    'Closed-source: "Provider flash report" (CTI Provider X, 2026-07-02, TLP:CLEAR) · '
    "Tags: vulnerabilities, actively-exploited · Region: global · "
    "CVE: CVE-2026-11111 · Vector: zero-click · Auth: pre-auth · Status: exploited*"
)
p_csm = parse_footer_line(cs_mixed)
assert p_csm is not None
assert_eq("mixed keeps the linked source", len(p_csm["sources"]), 1)
assert_eq("mixed keeps the closed-source record", len(p_csm["closed_source"]), 1)
assert_eq("mixed footer validates", validate_footer(p_csm, tax), [])

cs_bad = parse_footer_line(
    "— *Closed-source: some unquoted text without a record shape · Tags: ransomware · Region: global*"
)
assert cs_bad is not None
errs = validate_footer(cs_bad, tax)
assert any("Closed-source" in e for e in errs), f"malformed closed-source flagged: {errs}"

cs_badtlp = parse_footer_line(
    '— *Closed-source: "T" (Prov, 2026-07-01, TLP:PURPLE) · Tags: ransomware · Region: global*'
)
assert cs_badtlp is not None
errs2 = validate_footer(cs_badtlp, tax)
assert any("TLP" in e for e in errs2), f"unknown TLP flagged: {errs2}"

cs_html = render_footer_html(p_cs)
assert_in("closed-source rendered unlinked", "meta-closed-source", cs_html)
_cs_span = cs_html.split('src-closed">', 1)[1].split("</span>", 1)[0]
assert_not_in("closed-source has no anchor", "<a", _cs_span)
assert_in("closed-source provider rendered", "ISAC-CH weekly bulletin", _cs_span)

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
# render_cve_pill — multi-CVE split
# ---------------------------------------------------------------------
print("== render_cve_pill multi-CVE split ==")
single = render_cve_pill("CVE-2026-5787", prefix="../../")
assert_in("single CVE pill: anchor present", '<a class="pill pill-cve"', single)
# CVE pills now point at the unified entity URL space — `/entities/<id>/`
# is the canonical home for every entity (CVE, actor, campaign, …).
# The legacy `/cves/<id>/` URL still works as an HTML meta-refresh stub.
assert_in("single CVE pill: correct slug", 'href="../../entities/CVE-2026-5787/"', single)

multi = render_cve_pill("CVE-2026-5787, CVE-2026-6973", prefix="../../")
assert_in("multi CVE pill: first link", 'href="../../entities/CVE-2026-5787/"', multi)
assert_in("multi CVE pill: second link", 'href="../../entities/CVE-2026-6973/"', multi)
assert_not_in(
    "multi CVE pill: no broken comma slug",
    'entities/CVE-2026-5787, CVE-2026-6973/',
    multi,
)

# Boundary: junk passes through as a non-link badge instead of a 404.
junk = render_cve_pill("not-a-cve")
assert_in("non-CVE: rendered as plain pill", '<span class="pill pill-cve">', junk)
assert_not_in("non-CVE: no anchor", "<a", junk)


# ---------------------------------------------------------------------
# Security: protocol-relative URLs must be neutered (not handed to the
# browser as cross-origin redirects). [click](//evil.example/x) used to
# render as <a href="//evil.example/x">; the strict CSP blocks scripts
# from there but it would still navigate the visitor.
# ---------------------------------------------------------------------
print("== _safe_url protocol-relative defence ==")
for hostile in (
    "//evil.example/x",
    "//evil.example.com/path?q=1",
    "\\\\evil.example\\x",
    "/\\evil.example/x",
    "\\/evil.example/x",
):
    assert_eq(f"protocol-relative {hostile!r} → #", _safe_url(hostile), "#")

# Embedded in Markdown — the rendered href must be `#`.
hostile_md = "click [here](//evil.example/x)"
out = render_inline(hostile_md)
assert_in("protocol-relative neutered in render_inline", 'href="#"', out)
assert_not_in("no //evil.example in output", "//evil.example", out)


# ---------------------------------------------------------------------
# Security: control characters in input must not survive renderer's
# placeholder substitution path. The renderer uses \x00 as an internal
# placeholder marker; legitimate input never contains it.
# ---------------------------------------------------------------------
print("== _strip_controls ==")
assert_eq("strip NUL", _strip_controls("a\x00b"), "ab")
assert_eq("strip DEL", _strip_controls("a\x7fb"), "ab")
assert_eq("strip ESC", _strip_controls("a\x1bb"), "ab")
assert_eq("strip BEL", _strip_controls("a\x07b"), "ab")
assert_eq("preserve newline", _strip_controls("a\nb"), "a\nb")
assert_eq("preserve tab",     _strip_controls("a\tb"), "a\tb")
assert_eq("preserve CR",      _strip_controls("a\rb"), "a\rb")
assert_eq("empty unchanged",  _strip_controls(""), "")

# Renderer must drop control chars at the parse boundary even if the
# input contains a literal placeholder lookalike.
hostile = "look at \x00LINK0\x00 right here"
rendered = render_inline(hostile)
assert_not_in("renderer drops literal NUL", "\x00", rendered)
assert_in("placeholder lookalike text survives as plain text", "LINK0", rendered)


# ---------------------------------------------------------------------
# Security: write-time secret scan refuses common credential shapes
# ---------------------------------------------------------------------
print("== scan_for_secrets ==")
# Clean text — no hits.
assert_eq("clean text empty hits", scan_for_secrets("Just regular brief prose."), [])

# Each pattern should fire on a representative example.
for label, sample in (
    ("AWS key id", "AKIAIOSFODNN7EXAMPLE"),
    ("GitHub PAT", "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ0123456789"),
    # github_pat_<22 chars>_<≥50 chars>
    ("GitHub fine-grained PAT",
     "github_pat_AAAAAAAAAAAAAAAAAAAAAA_BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"),
    ("Anthropic key", "sk-ant-api03-aBcDeFgHiJkLmNoPqRsTuVwXyZ"),
    # AIza + 35 chars = 39 chars total. Sample below is exactly 39 chars.
    ("Google API key", "AIzaSyAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQ"),
    ("PEM key block", "-----BEGIN RSA PRIVATE KEY-----"),
    ("JWT", "eyJhbGciAB.eyJzdWIiCD.AbCdEfGh"),
):
    hits = scan_for_secrets(f"prefix {sample} suffix")
    if not hits:
        FAILURES.append(f"scan_for_secrets missed {label}: {sample[:8]}…")
        print(f"  FAIL {label}: not detected")
    else:
        print(f"  ok  {label} flagged as {hits[0][0]}")


# ---------------------------------------------------------------------
# Security: XML validator refuses DTD / entity declarations.
# The build only validates its OWN generated RSS feeds, but a defensive
# parser configuration ensures a future change that pipes untrusted XML
# through this function cannot trigger XXE or billion-laughs.
# ---------------------------------------------------------------------
print("== _xml_validate DTD/entity refusal ==")
clean = '<?xml version="1.0" encoding="UTF-8"?><rss><channel><title>x</title></channel></rss>'
assert_eq("clean XML accepted", _xml_validate(clean), [])

xxe_billion_laughs = (
    '<?xml version="1.0"?>'
    '<!DOCTYPE lolz ['
    '  <!ENTITY lol "lol">'
    '  <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">'
    ']>'
    '<rss><channel><title>&lol1;</title></channel></rss>'
)
errs = _xml_validate(xxe_billion_laughs)
assert errs, "XML validator must refuse DTD with entity declarations"
print("  ok  billion-laughs XML rejected with:", errs[0][:60])

xxe_external = (
    '<?xml version="1.0"?>'
    '<!DOCTYPE foo SYSTEM "file:///etc/passwd">'
    '<rss/>'
)
errs = _xml_validate(xxe_external)
assert errs, "XML validator must refuse external DTD reference"
print("  ok  external-DTD XML rejected with:", errs[0][:60])


# ---------------------------------------------------------------------
# _extract_bullets_with_footers — § 6 Action Items per-bullet footer
# ---------------------------------------------------------------------
print("== _extract_bullets_with_footers ==")

block_footer_md = """
- **Patch Cisco SD-WAN now** to a fixed release. See [§ 1](#x).

  — *Source: [Cisco PSIRT](https://example.com/psirt) · Tags: actively-exploited, rce · Region: global*

- **Audit NGINX configs** for vulnerable rewrite directives. See [§ 2](#y).

  — *Source: [depthfirst research](https://example.com/df) · Tags: vulnerabilities, rce · Region: global*
"""
_, bullets = _extract_bullets_with_footers(block_footer_md)
assert_eq("block footer flavour: bullet count", len(bullets), 2)
if bullets:
    assert_eq(
        "block footer flavour: first bullet tags",
        bullets[0]["footer"]["tags"],
        ["actively-exploited", "rce"],
    )
    assert_eq(
        "block footer flavour: first bullet region",
        bullets[0]["footer"]["regions"],
        ["global"],
    )
    assert_in(
        "block footer flavour: first bullet body preserved",
        "Patch Cisco SD-WAN now",
        bullets[0]["body_md"],
    )
    assert_not_in(
        "block footer flavour: footer stripped from body",
        "Source:",
        bullets[0]["body_md"],
    )

inline_footer_md = """
- **Patch Fortinet** now. See § 2 — *Source: [Fortinet PSIRT](https://example.com/fortinet) · Tags: vulnerabilities, rce · Region: global*
- **Audit npm lockfiles** for Mini Shai-Hulud. See § 5 — *Source: [StepSecurity](https://example.com/step) · Tags: supply-chain · Region: global*
"""
_, bullets = _extract_bullets_with_footers(inline_footer_md)
assert_eq("inline footer flavour: bullet count", len(bullets), 2)
if bullets:
    assert_eq(
        "inline footer flavour: first bullet tags",
        bullets[0]["footer"]["tags"],
        ["vulnerabilities", "rce"],
    )
    assert_in(
        "inline footer flavour: first bullet body preserved",
        "Patch Fortinet",
        bullets[0]["body_md"],
    )
    assert_not_in(
        "inline footer flavour: footer stripped from body",
        "Source:",
        bullets[0]["body_md"],
    )

# Mixed: one bullet has a footer, the other doesn't — the whole pattern
# fails (all-or-nothing), and the caller falls back to plain rendering.
mixed_md = """
- **Patch Cisco** now. See § 1 — *Source: [Cisco PSIRT](https://example.com/cisco) · Tags: rce · Region: global*
- **Generic advice** with no footer attached.
"""
preamble, bullets = _extract_bullets_with_footers(mixed_md)
assert_eq("mixed pattern: returns empty list", bullets, [])
assert_eq(
    "mixed pattern: preamble equals original body",
    preamble.strip(),
    mixed_md.strip(),
)

# Preamble preserved when bullets all match.
preamble_md = """
Specific, derived from today's content only.

- **Patch X** — *Source: [Vendor](https://example.com/v) · Tags: rce · Region: global*
"""
pre, bullets = _extract_bullets_with_footers(preamble_md)
assert_eq("preamble preserved: bullet count", len(bullets), 1)
assert_in("preamble preserved: preamble text", "Specific, derived", pre)


# ---------------------------------------------------------------------
# file_publish_moment filename-date fallback
#
# Regression test for the per-item RSS feed collapse: when
# git_first_commit_ts returns None (CI shallow clone, tarball build,
# git unavailable), file_publish_moment MUST still return distinct
# timestamps for distinct briefs — otherwise the per-item feed's
# stable sort lets one brief's items fill the entire 50-cap and evict
# every other brief.
# ---------------------------------------------------------------------
print("\nfile_publish_moment filename fallback:")

_orig_git_first_commit_ts = build.git_first_commit_ts
build.git_first_commit_ts = lambda _p: None
try:
    daily_15 = file_publish_moment(Path("briefs/2026-05-15.md"))
    daily_14 = file_publish_moment(Path("briefs/2026-05-14.md"))
    weekly_w19 = file_publish_moment(Path("briefs/weekly/2026-W19.md"))
finally:
    build.git_first_commit_ts = _orig_git_first_commit_ts

# Distinct briefs MUST get distinct timestamps even when git is unavailable.
if daily_15 == daily_14:
    FAILURES.append(f"fallback: daily 2026-05-15 == daily 2026-05-14 ({daily_15!r}) — feed will collapse")
    print(f"  FAIL fallback: daily timestamps collapsed to {daily_15!r}")
else:
    print("  ok  fallback: daily briefs get distinct timestamps")

if daily_15 == weekly_w19:
    FAILURES.append(f"fallback: daily 2026-05-15 == weekly 2026-W19 ({daily_15!r}) — feed will collapse")
    print(f"  FAIL fallback: daily-vs-weekly timestamps collapsed to {daily_15!r}")
else:
    print("  ok  fallback: daily vs weekly get distinct timestamps")

# Daily filename date is honoured (UTC midnight of the date in the stem).
assert_eq("fallback: daily 2026-05-15 → date", daily_15.date(), date(2026, 5, 15))
assert_eq("fallback: daily 2026-05-15 → UTC", daily_15.tzinfo, timezone.utc)

# Weekly ISO-week 19 of 2026 = Monday 2026-05-04.
assert_eq("fallback: weekly 2026-W19 → date", weekly_w19.date(), date(2026, 5, 4))
assert_eq("fallback: weekly 2026-W19 → UTC", weekly_w19.tzinfo, timezone.utc)


# ---------------------------------------------------------------------
# Umami analytics CSP — regression guard
# ---------------------------------------------------------------------
# The loader at UMAMI_SCRIPT_HOST POSTs pageview beacons to
# UMAMI_BEACON_HOST/api/send. If the CSP connect-src omits the beacon host
# (or re-lists a retired one), the browser silently blocks every beacon and
# analytics record nothing while the script appears to load fine. This is
# exactly the 2026-06-20 regression — it shipped from the first commit
# because nothing tied the CSP to the loader's real beacon endpoint.
import re  # noqa: E402  -- used for the connect-src directive match below

print("== umami CSP ==")
if build.ANALYTICS_ENABLED:
    assert_in(
        "snippet loads from the script host",
        f'src="{build.UMAMI_SCRIPT_HOST}/script.js"',
        build.UMAMI_SNIPPET,
    )
    assert_in("CSP permits the script host", build.UMAMI_SCRIPT_HOST, build.CSP_META)
    assert_in("CSP connect-src permits the beacon host", build.UMAMI_BEACON_HOST, build.CSP_META)
    assert_match(
        "beacon host is inside connect-src (not some other directive)",
        r"connect-src[^;]*" + re.escape(build.UMAMI_BEACON_HOST),
        build.CSP_META,
    )
    for _retired in build.UMAMI_RETIRED_HOSTS:
        assert_not_in(f"retired host {_retired} absent from CSP", _retired, build.CSP_META)
else:
    # analytics.provider "none" — the off switch must strip every
    # third-party origin from both the snippet and the CSP.
    assert_eq("analytics off: snippet empty", build.UMAMI_SNIPPET, "")
    assert_not_in("analytics off: no umami host in CSP", "umami", build.CSP_META)
    assert_match(
        "analytics off: connect-src is first-party only",
        r"connect-src 'self';",
        build.CSP_META,
    )


# ---------------------------------------------------------------------
# Ops dashboard — verification clean-rate
# ---------------------------------------------------------------------
# Regression guard: "clean publish" means the final verifier verdict was
# CLEAN (residual == 0), regardless of how many iterations it took. The old
# definition required iterations == 1 and so excluded every brief that
# reached CLEAN after remediation — the bulk of all runs (reported 2% when
# the true clean-publish rate was 68%).
print("== ops verification clean-rate ==")
assert_eq(
    "first-pass clean counts (iters=1, resid=0)",
    _verification_clean_publish({"verification_iterations": 1, "verification_residual_count": 0}),
    True,
)
assert_eq(
    "clean-after-remediation counts (iters=4, resid=0)",
    _verification_clean_publish({"verification_iterations": 4, "verification_residual_count": 0}),
    True,
)
assert_eq(
    "cap-breach with residuals does not count (iters=5, resid=2)",
    _verification_clean_publish({"verification_iterations": 5, "verification_residual_count": 2}),
    False,
)
assert_eq(
    "missing residual count treated as clean (iters=3, resid absent)",
    _verification_clean_publish({"verification_iterations": 3}),
    True,
)
assert_eq(
    "unrated run (no verification recorded) does not count",
    _verification_clean_publish({"verification_residual_count": 0}),
    False,
)


# ---------------------------------------------------------------------
# Branding profile (config/branding.yaml → branding_config.py)
# ---------------------------------------------------------------------
# The customization framework's core contract: the SHIPPED config is the
# upstream default (byte-identical site), every theme value is an override
# layer, unknown keys fail loud, and the analytics off switch works. See
# docs/customization.md.
import tempfile  # noqa: E402
import branding_config  # noqa: E402

print("== branding profile ==")

_shipped = branding_config.load_branding()
assert_eq(
    "shipped config/branding.yaml equals upstream DEFAULTS "
    "(byte-identical default site)",
    _shipped, branding_config.DEFAULTS,
)
assert_eq(
    "default theme emits no override CSS",
    branding_config.render_branding_css(_shipped), "",
)
assert_eq(
    "default favicon data-URI is byte-exact",
    branding_config.default_favicon_href(_shipped),
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
    "viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' "
    "fill='%23e85d75'/%3E%3Ctext x='50%25' y='52%25' text-anchor='middle' "
    "dominant-baseline='middle' font-family='ui-monospace,monospace' "
    "font-size='15' font-weight='700' fill='%230e1116'%3ECTI%3C/text%3E%3C/svg%3E",
)
# Missing file → identical defaults (a fork may delete the config).
assert_eq(
    "missing config file falls back to DEFAULTS",
    branding_config.load_branding(Path("/nonexistent/branding.yaml")),
    branding_config.DEFAULTS,
)

with tempfile.TemporaryDirectory() as _td:
    _tmp = Path(_td) / "branding.yaml"

    # Unknown key fails loud (typo protection).
    _tmp.write_text('site:\n  nmae: "typo"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: unknown key 'site.nmae' was accepted")
        print("  FAIL branding: unknown key accepted")
    except branding_config.BrandingError:
        print("  ok  unknown key fails loud")

    # Bad analytics provider fails loud.
    _tmp.write_text('analytics:\n  provider: "google"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: provider 'google' was accepted")
        print("  FAIL branding: bad provider accepted")
    except branding_config.BrandingError:
        print("  ok  unsupported analytics provider fails loud")

    # Referenced logo file must exist under site/branding/.
    _tmp.write_text('logo:\n  header_mark: "missing.svg"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: missing logo file was accepted")
        print("  FAIL branding: missing logo file accepted")
    except branding_config.BrandingError:
        print("  ok  missing logo file fails loud")

    # Partial override: unset keys inherit defaults; theme overrides emit
    # the two light-theme selector shapes styles.css uses.
    _tmp.write_text(
        'site:\n'
        '  name: "acme-cti.example"\n'
        'theme:\n'
        '  dark:\n'
        '    accent: "#00b3a4"\n'
        '  light:\n'
        '    accent: "#00776e"\n'
        'analytics:\n'
        '  provider: "none"\n',
        encoding="utf-8",
    )
    _fork = branding_config.load_branding(_tmp)
    assert_eq("override: site.name replaced", _fork["site"]["name"], "acme-cti.example")
    assert_eq(
        "override: unset tagline inherits upstream default",
        _fork["site"]["tagline"], "Switzerland, Europe & Public Sector",
    )
    assert_eq("override: analytics off", _fork["analytics"]["provider"], "none")
    _css = branding_config.render_branding_css(_fork)
    assert_in("override css: dark accent in :root", "--accent: #00b3a4;", _css)
    assert_in(
        "override css: light accent under prefers-color-scheme",
        ':root:not([data-theme="dark"])', _css,
    )
    assert_in(
        "override css: light accent under explicit data-theme",
        ':root[data-theme="light"]', _css,
    )

    # Custom trend cohorts / sector slices replace the defaults wholesale;
    # empty lists keep the upstream sets.
    _tmp.write_text(
        'trends:\n'
        '  cohorts:\n'
        '    - key: "apac"\n'
        '      title: "APAC items / week"\n'
        '      regions:\n'
        '        - "apac"\n'
        'feeds:\n'
        '  sector_slices:\n'
        '    - filename: "feed-manufacturing.xml"\n'
        '      title_suffix: "Manufacturing"\n'
        '      description: "Items affecting manufacturing."\n'
        '      sectors:\n'
        '        - "manufacturing"\n',
        encoding="utf-8",
    )
    _fork2 = branding_config.load_branding(_tmp)
    assert_eq(
        "custom cohorts replace defaults",
        branding_config.trend_cohorts(_fork2, [{"key": "default"}]),
        [{"key": "apac", "title": "APAC items / week", "tags": (),
          "sectors": (), "regions": ("apac",), "match": "any"}],
    )
    assert_eq(
        "custom sector slices replace defaults",
        branding_config.sector_feed_slices(_fork2, [("default",)]),
        [("feed-manufacturing.xml", ("manufacturing",), (),
          "Manufacturing", "Items affecting manufacturing.")],
    )
    assert_eq(
        "empty cohort list keeps upstream defaults",
        branding_config.trend_cohorts(_shipped, [{"key": "default"}]),
        [{"key": "default"}],
    )

# Module-level consistency in the imported build: snippet present iff
# analytics enabled; branding constants derive from the shipped config.
assert_eq(
    "build: snippet presence matches ANALYTICS_ENABLED",
    bool(build.UMAMI_SNIPPET), build.ANALYTICS_ENABLED,
)
assert_eq("build: SITE_NAME from config", build.SITE_NAME, _shipped["site"]["name"])
assert_eq(
    "build: default sector slices in effect with empty config list",
    build.SECTOR_FEED_SLICES is build._DEFAULT_SECTOR_FEED_SLICES,
    not _shipped["feeds"]["sector_slices"],
)
assert_eq(
    "build: default trend cohorts in effect with empty config list",
    build.TREND_COHORTS is build._DEFAULT_TREND_COHORTS,
    not _shipped["trends"]["cohorts"],
)


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
