#!/usr/bin/env python3
"""Build the static-site bundle for GitHub Pages (CTI Brief v2 SSG).

Inputs (read-only):
    briefs/YYYY-MM-DD.md          daily briefs
    briefs/weekly/YYYY-Www.md     weekly summaries
    state/cves_seen.json          flat CVE index
    state/covered_items.json      rolling coverage log
    state/run_log.json            ops dashboard data (optional)
    sources/sources.json          curated source list
    site/taxonomy.yaml            controlled vocabulary
    README.md, docs/*.md          rendered into /about/
    prompts/CHANGELOG.md          rendered into /about/changelog

Outputs (written under site/_site/):
    /                             home (latest brief preview)
    /briefs/YYYY-MM-DD/           single daily brief
    /briefs/weekly/YYYY-Www/      single weekly brief
    /briefs/                      brief index
    /items/<slug>/                one page per metadata-footer item
    /cves/<CVE-ID>/               one page per CVE
    /sources/<id>/                one page per source
    /topics/<key>/                one page per covered topic
    /tags/<tag>/                  index of items with this tag
    /regions/<region>/            index of items with this region
    /ops/                         operations dashboard
    /about/                       about / docs / changelog
    /feed.xml                     daily RSS (URL preserved)
    /feed-weekly.xml              weekly RSS (NEW)
    /feed-items.xml               per-item RSS (NEW)
    /sitemap.xml                  sitemap
    /robots.txt                   crawler directives
    /data/build_manifest.json     content-hashed manifest (self-check substrate)
    /data/site.json               build metadata
    /404.html                     fallback page

Design properties:
    - stdlib-only Python; no build dependencies
    - vendored-library SHA-256 integrity check on entry (build aborts on mismatch)
    - atomic per-file writes (temp + os.replace) — a crashed build never
      publishes a half-written page
    - deterministic: two runs with identical inputs produce a byte-identical
      tree (publish moments come from git, not now(); RSS lastBuildDate is
      the most-recent-input timestamp; cache-bust hash is content-hashed)
    - every emitted HTML page contains the Umami snippet exactly once
    - strict CSP unchanged
    - end-of-build self-check: every URL in the manifest exists on disk,
      every brief article has non-empty data-tags/data-regions/data-section,
      every taxonomy value is recognized, every feed parses cleanly, no
      orphan files in _site/

The site URL is read from SITE_URL env var; falls back to the deployed Pages
URL.
"""

from __future__ import annotations

import hashlib
import html as html_mod
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent
OUT = SITE / "_site"

DEFAULT_SITE_URL = "https://owlsnightcatch.github.io/security-newsletter/"
DEFAULT_GITHUB_REPO = "OwlsNightCatch/security-newsletter"

# RSS truncation per feed (HTML archive is unbounded).
FEED_DAILY_MAX = 30
FEED_WEEKLY_MAX = 30
FEED_ITEMS_MAX = 50


# === REGEXES ============================================================

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b")
LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
PROMPT_VERSION_RE = re.compile(r"\*\*Prompt:\*\*\s*v?([0-9]+\.[0-9]+)", re.IGNORECASE)
SINGLE_SOURCE_FLAGS = ("SINGLE-SOURCE-NATIONAL-CERT", "SINGLE-SOURCE-OTHER", "SINGLE-SOURCE")

# Metadata footer (§4.7 of the v2 prompt). The footer is a single italic
# Markdown line of the form
#
#     — *Source: [Title](URL) [· Additional source: [Title](URL)] · Tags: a, b · Region: r1[, r2] [· CVE: CVE-…] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*
#
# The opening token is an em-dash + space + asterisk; the closing token is
# a trailing asterisk. Field order is fixed; field separator is a middle
# dot ` · ` (U+00B7).
FOOTER_RE = re.compile(
    r"^\s*[—-]\s*\*Source:\s*(?P<body>.+?)\*\s*$",
    re.MULTILINE,
)
# Each `[Title](URL)` group used inside the footer body.
FOOTER_LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")


# === SLUG / HOST HELPERS ================================================

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def host_of(url: str) -> str:
    try:
        h = (urllib.parse.urlparse(url).hostname or "").lower().strip()
        return h.removeprefix("www.")
    except Exception:
        return ""


def url_prefix_of(url: str) -> str:
    try:
        u = urllib.parse.urlparse(url)
        host = (u.hostname or "").lower().removeprefix("www.")
        if not host:
            return ""
        path = u.path or "/"
        if "/" in path:
            head, _, tail = path.rpartition("/")
            if "." in tail:
                path = head + "/"
        return f"{host}{path}"
    except Exception:
        return ""


# === GIT TIMESTAMP =====================================================

def git_first_commit_ts(path: Path) -> datetime | None:
    """Return the first (creation) commit timestamp on `main` for `path`,
    in UTC. Returns None when `git` is unavailable or the file is not
    tracked yet (in which case the caller falls back to mtime)."""
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path
    try:
        # --diff-filter=A — only the commit that *added* the file.
        # --reverse + head -1 — earliest match if the file was renamed.
        # %aI — author ISO 8601 timestamp.
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%aI", "--reverse", "--", str(rel)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=15,
        )
        if out.returncode != 0:
            return None
        for line in out.stdout.splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                return datetime.fromisoformat(line).astimezone(timezone.utc)
            except ValueError:
                continue
        return None
    except (FileNotFoundError, subprocess.TimeoutExpired, Exception):
        return None


def file_publish_moment(path: Path) -> datetime:
    """Best-effort UTC moment a brief became live. Tries (1) git first-commit
    timestamp; falls back to (2) file mtime. Never falls back to
    midnight-of-brief-date — that's Defect B in the issue tracker."""
    ts = git_first_commit_ts(path)
    if ts is not None:
        return ts
    try:
        mt = path.stat().st_mtime
        return datetime.fromtimestamp(mt, tz=timezone.utc)
    except OSError:
        # Last resort: now(). Should not happen on a real build.
        return datetime.now(timezone.utc)


def rfc822(ts: datetime) -> str:
    """RFC 822 timestamp string — `Wed, 02 Oct 2002 15:00:00 +0000`."""
    return ts.astimezone(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")


# === VENDORED LIBRARY INTEGRITY ========================================

def verify_vendored_hashes() -> None:
    """Abort the build if any vendored library's bytes don't match HASHES.
    Catches both silent on-disk tampering and accidental upgrades."""
    vendor = SITE / "assets" / "vendor"
    hashes_file = vendor / "HASHES"
    if not hashes_file.exists():
        print(f"warning: {hashes_file} missing; skipping integrity check", file=sys.stderr)
        return
    expected: dict[str, str] = {}
    for raw in hashes_file.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        parts = line.split()
        if len(parts) != 3:
            continue
        algo, fname, digest = parts
        if algo == "sha256":
            expected[fname] = digest
    failures: list[str] = []
    for fname, want in expected.items():
        path = vendor / fname
        if not path.exists():
            failures.append(f"{fname}: missing")
            continue
        got = hashlib.sha256(path.read_bytes()).hexdigest()
        if got != want:
            failures.append(f"{fname}: hash mismatch (expected {want}, got {got})")
    if failures:
        print("VENDORED LIBRARY INTEGRITY CHECK FAILED:", file=sys.stderr)
        for f in failures:
            print(f"  · {f}", file=sys.stderr)
        print(
            "Refuse to build a site with mismatched vendor bytes. "
            "If this is a deliberate upgrade, regenerate site/assets/vendor/HASHES.",
            file=sys.stderr,
        )
        sys.exit(2)


# === TAXONOMY ==========================================================

def parse_taxonomy(path: Path) -> dict[str, set[str]]:
    """Pure-Python YAML-list parser: read the taxonomy file as a flat set
    of `key -> {values}` dicts. Stdlib-only (no `yaml` dependency)."""
    if not path.exists():
        return {}
    out: dict[str, set[str]] = {}
    cur_key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        # Top-level key: `themes:` (no leading whitespace).
        m = re.match(r"^([a-z_][a-z0-9_]*)\s*:\s*$", line)
        if m:
            cur_key = m.group(1)
            out[cur_key] = set()
            continue
        # List item: `  - value`.
        m = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if m and cur_key is not None:
            value = m.group(1).strip().strip('"').strip("'")
            out[cur_key].add(value)
    return out


# === MARKDOWN RENDERER (build-time, pure-Python) =======================

# A focused renderer that handles every Markdown construct the briefs and
# docs actually use: H1-H4 headings, paragraphs, ordered + unordered lists,
# blockquotes, fenced code, indented code, hr, pipe tables, inline bold /
# italic / code / links, plus HTML escaping. DOMPurify is no longer in the
# pipeline — the renderer's allowlist does the sanitization.

_INLINE_LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])+)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
_INLINE_CODE_RE = re.compile(r"`([^`]+)`")
_INLINE_BOLD_RE = re.compile(r"\*\*((?:[^*]|\*(?!\*))+?)\*\*")
_INLINE_ITAL_RE = re.compile(r"(?<![\\*])\*([^*\n]+)\*(?!\*)")
_INLINE_ITAL_UNDER_RE = re.compile(r"(?<![\w_])_([^_\n]+)_(?![\w_])")
_INLINE_AUTOLINK_RE = re.compile(r"(?<![\(\"<\w])(https?://[^\s<>\)]+)")


def _escape(s: str) -> str:
    """HTML-escape a string. Used everywhere except inside `<code>` (which
    is also escaped — the rule is uniform)."""
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&#39;")
    )


def render_inline(s: str, *, base_url: str | None = None) -> str:
    """Render Markdown inline constructs to HTML.

    `base_url` (when given) absolutises relative links so the result is
    self-contained (used by RSS body rendering — RSS readers don't have a
    base URL to resolve against).
    """
    # Step 1: extract code spans first so we don't re-process their bytes.
    placeholders: dict[str, str] = {}

    def stash_code(m: re.Match) -> str:
        key = f"\x00CODE{len(placeholders)}\x00"
        placeholders[key] = "<code>" + _escape(m.group(1)) + "</code>"
        return key

    s = _INLINE_CODE_RE.sub(stash_code, s)

    # Step 2: extract links (their inner text may still take inline
    # formatting after we've stashed the URL).
    def stash_link(m: re.Match) -> str:
        text = m.group(1)
        url = m.group(2)
        if base_url and not (url.startswith("http://") or url.startswith("https://") or url.startswith("mailto:")):
            url = urllib.parse.urljoin(base_url, url)
        # Recurse on link text for inline formatting (excluding nested
        # links, which Markdown forbids anyway).
        rendered_text = render_inline_no_links(text)
        key = f"\x00LINK{len(placeholders)}\x00"
        placeholders[key] = (
            f'<a href="{_escape(url)}" rel="noopener noreferrer">{rendered_text}</a>'
        )
        return key

    s = _INLINE_LINK_RE.sub(stash_link, s)

    # Step 3: bold (greedy then italic).
    s = _INLINE_BOLD_RE.sub(lambda m: "\x00B" + m.group(1) + "\x00b", s)
    # Step 4: italic (`*...*` and `_..._`). Avoid eating bullet markers
    # by requiring no whitespace adjacent to the asterisks.
    s = _INLINE_ITAL_RE.sub(lambda m: "\x00I" + m.group(1) + "\x00i", s)
    s = _INLINE_ITAL_UNDER_RE.sub(lambda m: "\x00I" + m.group(1) + "\x00i", s)
    # Step 5: bare URL autolinks (only when not already inside an anchor).
    s = _INLINE_AUTOLINK_RE.sub(
        lambda m: f'<a href="{_escape(m.group(1))}" rel="noopener noreferrer">{_escape(m.group(1))}</a>',
        s,
    )
    # Step 6: now escape the remaining text. Markers \x00 are preserved.
    s = _escape(s)
    s = s.replace("\x00B", "<strong>").replace("\x00b", "</strong>")
    s = s.replace("\x00I", "<em>").replace("\x00i", "</em>")
    # Step 7: restore placeholders (codes + links) untouched. Their
    # values are already valid HTML.
    for key, value in placeholders.items():
        s = s.replace(_escape(key), value)
        s = s.replace(key, value)
    return s


def render_inline_no_links(s: str) -> str:
    """Inline rendering that skips link/auto-link expansion. Used inside
    link text where nested links are illegal anyway."""
    placeholders: dict[str, str] = {}

    def stash_code(m: re.Match) -> str:
        key = f"\x00CODE{len(placeholders)}\x00"
        placeholders[key] = "<code>" + _escape(m.group(1)) + "</code>"
        return key

    s = _INLINE_CODE_RE.sub(stash_code, s)
    s = _INLINE_BOLD_RE.sub(lambda m: "\x00B" + m.group(1) + "\x00b", s)
    s = _INLINE_ITAL_RE.sub(lambda m: "\x00I" + m.group(1) + "\x00i", s)
    s = _INLINE_ITAL_UNDER_RE.sub(lambda m: "\x00I" + m.group(1) + "\x00i", s)
    s = _escape(s)
    s = s.replace("\x00B", "<strong>").replace("\x00b", "</strong>")
    s = s.replace("\x00I", "<em>").replace("\x00i", "</em>")
    for key, value in placeholders.items():
        s = s.replace(_escape(key), value)
        s = s.replace(key, value)
    return s


def render_markdown(md: str, *, base_url: str | None = None) -> str:
    """Render Markdown text to HTML. Block-level constructs:
        - headings (#, ##, ###, ####)
        - paragraphs
        - unordered lists (`- ` or `* `, allowing nested by 2-space indent)
        - ordered lists (`1. `)
        - blockquotes (`> `)
        - fenced code blocks (```)
        - indented code blocks (4 spaces) — minimal
        - horizontal rules (`---` or `***`)
        - pipe tables
        - inline-only fallback for everything else.
    """
    lines = md.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    def is_blank(s: str) -> bool:
        return not s.strip()

    while i < n:
        line = lines[i]
        # Fenced code (```)
        if line.lstrip().startswith("```"):
            # Capture lang
            fence = line.lstrip()[:3]
            lang_match = re.match(r"^```\s*([a-zA-Z0-9_+-]*)\s*$", line.strip())
            lang = lang_match.group(1) if lang_match else ""
            i += 1
            buf: list[str] = []
            while i < n and not lines[i].lstrip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1  # consume closing fence
            cls = f' class="lang-{_escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{_escape(chr(10).join(buf))}</code></pre>")
            continue
        # ATX heading
        m = re.match(r"^(#{1,4})\s+(.*?)\s*#*\s*$", line)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            anchor = slugify(text)
            rendered = render_inline(text, base_url=base_url)
            out.append(f'<h{level} id="{anchor}">{rendered}</h{level}>')
            i += 1
            continue
        # Horizontal rule
        if re.match(r"^\s*([-*_])\s*\1\s*\1\s*$", line) or re.match(r"^---+$", line.strip()):
            out.append("<hr/>")
            i += 1
            continue
        # Pipe table — needs a header row + separator row.
        if (
            line.lstrip().startswith("|")
            and i + 1 < n
            and re.match(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$", lines[i + 1])
        ):
            head_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            sep_cells = [c.strip() for c in lines[i + 1].strip().strip("|").split("|")]
            aligns: list[str] = []
            for s in sep_cells:
                if s.startswith(":") and s.endswith(":"):
                    aligns.append("center")
                elif s.endswith(":"):
                    aligns.append("right")
                else:
                    aligns.append("left")
            i += 2
            rows: list[list[str]] = []
            while i < n and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            out.append('<div class="table-wrap"><table>')
            out.append("<thead><tr>")
            for idx, h in enumerate(head_cells):
                a = aligns[idx] if idx < len(aligns) else "left"
                out.append(f'<th style="text-align:{a}">{render_inline(h, base_url=base_url)}</th>')
            out.append("</tr></thead><tbody>")
            for row in rows:
                out.append("<tr>")
                for idx, c in enumerate(row):
                    a = aligns[idx] if idx < len(aligns) else "left"
                    out.append(f'<td style="text-align:{a}">{render_inline(c, base_url=base_url)}</td>')
                out.append("</tr>")
            out.append("</tbody></table></div>")
            continue
        # Blockquote
        if line.lstrip().startswith(">"):
            buf2: list[str] = []
            while i < n and (lines[i].lstrip().startswith(">") or (buf2 and not is_blank(lines[i]))):
                buf2.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            inner = render_markdown("\n".join(buf2), base_url=base_url)
            out.append(f"<blockquote>{inner}</blockquote>")
            continue
        # Unordered list
        if re.match(r"^[-*]\s+\S", line.lstrip()):
            buf3: list[tuple[int, str]] = []
            while i < n and (re.match(r"^[-*]\s+\S", lines[i].lstrip()) or (buf3 and lines[i].startswith("  "))):
                ll = lines[i]
                indent = len(ll) - len(ll.lstrip())
                m_li = re.match(r"^[-*]\s+(.*)$", ll.lstrip())
                if m_li:
                    buf3.append((indent, m_li.group(1)))
                else:
                    # continuation line: append to last item
                    if buf3:
                        ind0, txt = buf3[-1]
                        buf3[-1] = (ind0, txt + "\n" + ll.strip())
                i += 1
            out.append(_render_list(buf3, ordered=False, base_url=base_url))
            continue
        # Ordered list
        if re.match(r"^\d+\.\s+\S", line.lstrip()):
            buf4: list[tuple[int, str]] = []
            while i < n and (re.match(r"^\d+\.\s+\S", lines[i].lstrip()) or (buf4 and lines[i].startswith("  "))):
                ll = lines[i]
                indent = len(ll) - len(ll.lstrip())
                m_li = re.match(r"^\d+\.\s+(.*)$", ll.lstrip())
                if m_li:
                    buf4.append((indent, m_li.group(1)))
                else:
                    if buf4:
                        ind0, txt = buf4[-1]
                        buf4[-1] = (ind0, txt + "\n" + ll.strip())
                i += 1
            out.append(_render_list(buf4, ordered=True, base_url=base_url))
            continue
        # Blank line
        if is_blank(line):
            i += 1
            continue
        # Paragraph: gather until blank
        buf5: list[str] = [line]
        i += 1
        while i < n and not is_blank(lines[i]) and not lines[i].lstrip().startswith(("#", ">", "```", "- ", "* ", "|")):
            # also bail on ordered list start
            if re.match(r"^\d+\.\s+\S", lines[i].lstrip()):
                break
            if re.match(r"^---+$", lines[i].strip()):
                break
            buf5.append(lines[i])
            i += 1
        para = "\n".join(buf5).strip()
        if para:
            out.append(f"<p>{render_inline(para, base_url=base_url)}</p>")

    return "\n".join(out)


def _render_list(items: list[tuple[int, str]], *, ordered: bool, base_url: str | None) -> str:
    """Render a (flat) Markdown list. Nested lists are emitted by treating
    a deeper-indented run as a nested list inside the prior <li>."""
    tag = "ol" if ordered else "ul"
    if not items:
        return f"<{tag}></{tag}>"
    base_indent = items[0][0]
    out = [f"<{tag}>"]
    n = len(items)
    j = 0
    while j < n:
        indent, text = items[j]
        if indent > base_indent:
            # Collect the nested run
            nested: list[tuple[int, str]] = []
            while j < n and items[j][0] > base_indent:
                nested.append(items[j])
                j += 1
            # Re-base the indents and recurse
            min_indent = min(i for i, _ in nested)
            nested_re = [(ind - min_indent, t) for ind, t in nested]
            inner = _render_list(nested_re, ordered=False, base_url=base_url)
            # Append inner to the previous li
            if out and out[-1].endswith("</li>"):
                out[-1] = out[-1][: -len("</li>")] + inner + "</li>"
            else:
                out.append(f"<li>{inner}</li>")
            continue
        # Render the item; if its body has a paragraph break, expand
        rendered = render_inline(text, base_url=base_url)
        out.append(f"<li>{rendered}</li>")
        j += 1
    out.append(f"</{tag}>")
    return "".join(out)


# === FOOTER PARSER =====================================================

# Parse a single metadata-footer line into a structured dict.
def parse_footer_line(line: str) -> dict[str, Any] | None:
    """Parse a metadata-footer line. Returns None if the line isn't a
    footer or is malformed.

    The footer format (§4.7 of the v2 prompt):
        — *Source: [Title](URL) [· Additional source: [Title](URL)] · Tags: a, b · Region: r1[, r2] [· CVE: CVE-…] [· CVSS: …] [· Vector: …] [· Auth: …] [· Status: …]*

    Returns dict with keys:
        sources:        list[{label, url}]
        tags:           list[str]   (themes + nexus + status flags)
        regions:        list[str]
        sectors:        list[str]   (subset of tags, per taxonomy)
        cve:            str|None
        cvss:           str|None
        vector:         str|None
        auth:           str|None
        status:         list[str]   (split on `,`)
    """
    s = line.strip()
    if not s:
        return None
    # Strip leading em-dash / hyphen + asterisk; trailing asterisk.
    m = re.match(r"^[—-]\s*\*\s*Source:\s*(?P<body>.+?)\*\s*$", s)
    if not m:
        return None
    body = m.group("body").strip()

    # Pull all `[Title](URL)` first; we'll consume them by position.
    links = list(FOOTER_LINK_RE.finditer(body))
    sources: list[dict[str, str]] = []
    # Replace links with placeholders so later splits don't trip on the `· Source:`-like text inside.
    placeholder_map: dict[str, str] = {}
    body_clean = body
    for idx, lm in enumerate(links):
        ph = f"\x00LINK{idx}\x00"
        placeholder_map[ph] = f"{lm.group(1)}|||{lm.group(2)}"
        body_clean = body_clean.replace(lm.group(0), ph, 1)

    # Now split on the field separator ` · `.
    parts = [p.strip() for p in re.split(r"\s+·\s+", body_clean) if p.strip()]
    if not parts:
        return None

    out: dict[str, Any] = {
        "sources": [],
        "tags": [],
        "regions": [],
        "sectors": [],
        "cve": None,
        "cvss": None,
        "vector": None,
        "auth": None,
        "status": [],
    }

    # First part is the primary source (no "Source:" prefix in the body
    # — that prefix was stripped by the regex above).
    first = parts[0]
    # Either it's a placeholder for the link, or an inline label.
    if first in placeholder_map:
        label, url = placeholder_map[first].split("|||", 1)
        out["sources"].append({"label": label, "url": url})
    else:
        m_link = re.search(r"\x00LINK\d+\x00", first)
        if m_link:
            ph = m_link.group(0)
            label, url = placeholder_map[ph].split("|||", 1)
            out["sources"].append({"label": label, "url": url})

    for p in parts[1:]:
        # Each remaining part is `Key: value`.
        key_m = re.match(r"^([A-Za-z][A-Za-z ]*?):\s*(.*)$", p)
        if not key_m:
            continue
        key = key_m.group(1).strip().lower().replace(" ", "_")
        value = key_m.group(2).strip()
        # Substitute any link placeholders inside value.
        for ph, val in placeholder_map.items():
            if ph in value:
                lab, url = val.split("|||", 1)
                value = value.replace(ph, f"[{lab}]({url})")
        if key in ("additional_source", "additional_sources"):
            link_m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", value)
            if link_m:
                out["sources"].append({"label": link_m.group(1), "url": link_m.group(2)})
        elif key == "tags":
            out["tags"] = [t.strip() for t in value.split(",") if t.strip()]
        elif key == "region":
            out["regions"] = [t.strip() for t in value.split(",") if t.strip()]
        elif key in ("sector", "sectors"):
            out["sectors"] = [t.strip() for t in value.split(",") if t.strip()]
        elif key == "cve":
            out["cve"] = value.strip()
        elif key == "cvss":
            out["cvss"] = value.strip()
        elif key == "vector":
            out["vector"] = value.strip()
        elif key == "auth":
            out["auth"] = value.strip()
        elif key == "status":
            out["status"] = [t.strip() for t in value.split(",") if t.strip()]

    return out


def validate_footer(footer: dict[str, Any], taxonomy: dict[str, set[str]]) -> list[str]:
    """Return a list of validation errors against the controlled vocab.
    Empty list means everything is fine. The caller decides whether to
    fail the build (post-cut-over) or warn (legacy briefs)."""
    errors: list[str] = []
    if not footer.get("sources"):
        errors.append("missing primary source link")
    themes = taxonomy.get("themes", set()) | taxonomy.get("nexus", set())
    sectors = taxonomy.get("sectors", set())
    regions = taxonomy.get("regions", set())
    cve_vector = taxonomy.get("cve_vectors", set())
    cve_auth = taxonomy.get("cve_auth", set())
    cve_status = taxonomy.get("cve_status", set())

    for t in footer.get("tags", []):
        if t and t not in themes and t not in sectors:
            errors.append(f"unknown tag: {t}")
    for r in footer.get("regions", []):
        if r and r not in regions:
            errors.append(f"unknown region: {r}")
    if footer.get("vector") and footer["vector"] not in cve_vector:
        errors.append(f"unknown CVE vector: {footer['vector']}")
    if footer.get("auth") and footer["auth"] not in cve_auth:
        errors.append(f"unknown CVE auth: {footer['auth']}")
    for s in footer.get("status", []):
        if s and s not in cve_status:
            errors.append(f"unknown CVE status: {s}")
    return errors


# === BRIEF PARSER ======================================================

# Map H2 heading keywords (lower-cased) to the canonical section data-key
# used in `<section data-section>`. Keywords that don't match drop into a
# fallback `other` bucket (which the build still renders, just without
# tag/region indexing).
_SECTION_KEYWORDS: list[tuple[str, str]] = [
    # daily prompt v2
    ("tl;dr", "tldr"),
    ("immediate action", "immediate-actions"),
    ("active threats", "active-threats"),
    ("trending vulnerabilities", "trending-vulnerabilities"),
    ("notable incidents", "active-threats"),  # legacy
    ("switzerland, europe", "active-threats"),  # legacy
    ("research", "research"),
    ("updates to prior coverage", "updates"),
    ("deep dive", "deep-dive"),
    ("action items", "action-items"),
    ("verification notes", "verification-notes"),
    # weekly prompt
    ("week at a glance", "weekly-glance"),
    ("top stories", "weekly-top-stories"),
    ("multi-day", "weekly-multi-day"),
    ("vulnerability roll-up", "weekly-vuln-rollup"),
    ("sector & victim", "weekly-sector-patterns"),
    ("incidents & disclosures recap", "weekly-incidents-recap"),
    ("annual", "weekly-annual-reports"),
    ("long-running campaigns", "weekly-long-running"),
    ("policy", "weekly-policy"),
    ("looking ahead", "weekly-looking-ahead"),
    ("verification & coverage", "verification-notes"),
]


def section_key_for(heading: str) -> str:
    h = heading.lower()
    for kw, key in _SECTION_KEYWORDS:
        if kw in h:
            return key
    return "other"


def parse_brief(path: Path) -> dict[str, Any]:
    """Parse a brief Markdown file into a structured dict.

    Returns:
        name, kind ('daily'|'weekly'), path (relative), title,
        summary (first TL;DR-derived blurb), generated_by, prompt_version,
        publish_ts (datetime, UTC), publish_rfc822 (str),
        sections [
            { heading, anchor, key, h3_items: [...] }
        ],
        cves (sorted unique),
        text (raw md),
        size, items_total
        legacy_links (list of {label, url, host} for every inline link)
        item_flags ({h3_heading: ['SINGLE-SOURCE-...']})
        cve_citations ({cve_id: [{label, url, host, prefix}, ...]})
        unit_data (paragraph-level link aggregations for topic citations)
    """
    text = path.read_text(encoding="utf-8")
    name = path.stem
    is_weekly = path.parent.name == "weekly"
    rel = str(path.relative_to(ROOT))

    m = re.search(r"^# (.+?)\s*$", text, re.MULTILINE)
    title = m.group(1).strip() if m else name

    gen_match = re.search(r"\*\*Generated by:\*\*\s*([^\n·]+)", text)
    generated_by = gen_match.group(1).strip() if gen_match else None

    pv_match = PROMPT_VERSION_RE.search(text)
    prompt_version = pv_match.group(1) if pv_match else None

    publish_ts = file_publish_moment(path)

    # Walk the file by H2 boundaries to build sections.
    h2_starts: list[tuple[int, str]] = []  # (char_index, heading)
    for m in re.finditer(r"^## (.+?)\s*$", text, re.MULTILINE):
        h2_starts.append((m.start(), m.group(1).strip()))

    sections: list[dict[str, Any]] = []
    for idx, (start, heading) in enumerate(h2_starts):
        end = h2_starts[idx + 1][0] if idx + 1 < len(h2_starts) else len(text)
        body = text[start:end]
        # Strip the leading `## Heading` line itself
        first_nl = body.find("\n")
        body_text = body[first_nl + 1 :] if first_nl >= 0 else ""
        anchor = slugify(heading)
        skey = section_key_for(heading)

        # H3 boundaries within this section
        h3_starts: list[tuple[int, str]] = []
        for m3 in re.finditer(r"^### (.+?)\s*$", body_text, re.MULTILINE):
            h3_starts.append((m3.start(), m3.group(1).strip()))

        items: list[dict[str, Any]] = []
        if h3_starts:
            for j, (s3, h3heading) in enumerate(h3_starts):
                e3 = h3_starts[j + 1][0] if j + 1 < len(h3_starts) else len(body_text)
                item_md = body_text[s3:e3].strip()
                # Strip leading `### Heading` line
                first_nl_i = item_md.find("\n")
                item_body = item_md[first_nl_i + 1 :] if first_nl_i >= 0 else ""
                item_body = item_body.strip()
                # Locate footer line (last non-empty line if it matches)
                footer = None
                stripped_body = item_body
                lines = item_body.splitlines()
                while lines and not lines[-1].strip():
                    lines.pop()
                if lines:
                    fm = parse_footer_line(lines[-1])
                    if fm:
                        footer = fm
                        # Remove footer line from body for clean rendering
                        stripped_body = "\n".join(lines[:-1]).rstrip()
                items.append(
                    {
                        "heading": h3heading,
                        "anchor": slugify(h3heading),
                        "slug": f"{name}-{slugify(h3heading)}"[:80].strip("-"),
                        "body_md": stripped_body,
                        "footer": footer,
                        "section_key": skey,
                    }
                )
        else:
            # No H3 items — section may still carry footer-tagged paragraphs.
            # Future: detect paragraph-level footers. For now: keep raw body.
            pass

        sections.append(
            {
                "heading": heading,
                "anchor": anchor,
                "key": skey,
                "items": items,
                "body_md": body_text,
            }
        )

    cves = sorted(set(CVE_RE.findall(text)))

    # Legacy citation aggregation (kept for /sources and /topics pages).
    legacy_links: list[dict[str, str]] = []
    seen = set()
    for m in LINK_RE.finditer(text):
        label, url = m.group(1).strip(), m.group(2).strip()
        if url in seen:
            continue
        seen.add(url)
        legacy_links.append({"label": label, "url": url, "host": host_of(url), "prefix": url_prefix_of(url)})

    # H3 verification-flag tagging (legacy)
    item_flags: dict[str, list[str]] = {}
    for m in re.finditer(r"^### (.+?)\s*$", text, re.MULTILINE):
        heading = m.group(1).strip()
        flags = []
        for f in SINGLE_SOURCE_FLAGS:
            if f"[{f}]" in heading:
                flags.append(f)
                break
        if flags:
            item_flags[heading] = flags

    # CVE citation aggregation (paragraph-scope, preserved from legacy build).
    cve_citations: dict[str, list[dict[str, str]]] = {}

    def register(cve_id: str, label: str, url: str) -> None:
        bucket = cve_citations.setdefault(cve_id, [])
        if any(c["url"] == url for c in bucket):
            return
        bucket.append(
            {
                "label": label,
                "url": url,
                "host": host_of(url),
                "prefix": url_prefix_of(url),
            }
        )

    body_start_match = re.search(r"^## ", text, re.MULTILINE)
    body = text[body_start_match.start():] if body_start_match else text

    units: list[str] = []
    for chunk in re.split(r"\n\s*\n", body):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "\n|" in chunk and chunk.lstrip().startswith("|"):
            for ln in chunk.splitlines():
                if ln.strip().startswith("|"):
                    units.append(ln)
            continue
        if re.match(r"^[-*]\s+", chunk):
            current: list[str] = []
            for ln in chunk.splitlines():
                if re.match(r"^[-*]\s+", ln) and current:
                    units.append("\n".join(current))
                    current = [ln]
                else:
                    current.append(ln)
            if current:
                units.append("\n".join(current))
            continue
        units.append(chunk)

    for unit in units:
        cves_in_unit = set(CVE_RE.findall(unit))
        if not cves_in_unit or len(cves_in_unit) > 3:
            continue
        for m in LINK_RE.finditer(unit):
            label = m.group(1).strip()
            url = m.group(2).strip()
            for cve_id in cves_in_unit:
                register(cve_id, label, url)

    for m in LINK_RE.finditer(body):
        label = m.group(1).strip()
        url = m.group(2).strip()
        for url_cve in CVE_RE.findall(url):
            register(url_cve, label, url)

    unit_data: list[dict[str, Any]] = []
    for unit in units:
        unit_links: list[dict[str, str]] = []
        for m in LINK_RE.finditer(unit):
            unit_links.append(
                {
                    "label": m.group(1).strip(),
                    "url": m.group(2).strip(),
                    "host": host_of(m.group(2).strip()),
                    "prefix": url_prefix_of(m.group(2).strip()),
                }
            )
        if not unit_links:
            continue
        unit_data.append(
            {
                "text": unit,
                "text_lower": unit.lower(),
                "cves": sorted(set(CVE_RE.findall(unit))),
                "links": unit_links,
            }
        )

    # TL;DR derivation (still used for RSS description + home preview)
    tldr: list[str] = []
    tldr_block = re.search(r"##\s*0?\.?\s*TL;DR\s*\n(.+?)(?=\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE)
    if tldr_block:
        for raw in tldr_block.group(1).splitlines():
            line = raw.strip()
            if line.startswith("- "):
                tldr.append(line[2:].strip())

    items_total = sum(len(s["items"]) for s in sections)

    return {
        "name": name,
        "kind": "weekly" if is_weekly else "daily",
        "path": rel,
        "title": title,
        "summary": (tldr[0] if tldr else "")[:280],
        "generated_by": generated_by,
        "prompt_version": prompt_version,
        "publish_ts": publish_ts,
        "publish_rfc822": rfc822(publish_ts),
        "publish_iso": publish_ts.isoformat(),
        "sections": sections,
        "cves": cves,
        "text": text,
        "size": len(text),
        "tldr": tldr,
        "links": legacy_links,
        "item_flags": item_flags,
        "cve_citations": cve_citations,
        "unit_data": unit_data,
        "items": items_total,
    }


def collect_briefs() -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    daily_dir = ROOT / "briefs"
    weekly_dir = daily_dir / "weekly"
    for p in sorted(daily_dir.glob("*.md")):
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", p.stem):
            continue
        out.append(parse_brief(p))
    if weekly_dir.exists():
        for p in sorted(weekly_dir.glob("*.md")):
            if not re.match(r"^\d{4}-W\d{2}$", p.stem):
                continue
            out.append(parse_brief(p))
    out.sort(key=lambda b: (b["kind"], b["name"]), reverse=True)
    return out


# === ATOMIC WRITE ======================================================

_WRITE_COUNTER = {"writes": 0, "skips": 0, "deleted": 0}
_WRITTEN_PATHS: set[Path] = set()


def atomic_write_text(path: Path, content: str) -> bool:
    """Write `content` to `path` via temp + os.replace. Returns True if the
    on-disk bytes changed (or the file did not previously exist), False if
    `content` matched what was already on disk (no write). The bool drives
    the determinism check at the end of the build."""
    path.parent.mkdir(parents=True, exist_ok=True)
    _WRITTEN_PATHS.add(path.resolve())
    encoded = content.encode("utf-8")
    if path.exists():
        try:
            existing = path.read_bytes()
        except OSError:
            existing = b""
        if existing == encoded:
            _WRITE_COUNTER["skips"] += 1
            return False
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(encoded)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    _WRITE_COUNTER["writes"] += 1
    return True


def atomic_write_bytes(path: Path, data: bytes) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    _WRITTEN_PATHS.add(path.resolve())
    if path.exists():
        try:
            existing = path.read_bytes()
        except OSError:
            existing = b""
        if existing == data:
            _WRITE_COUNTER["skips"] += 1
            return False
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    _WRITE_COUNTER["writes"] += 1
    return True


def prune_orphans(out: Path) -> None:
    """Walk the output tree; delete any file we did not (re)write this
    run. Empty directories left behind are removed too. Called at the
    very end of a successful build so a partial / aborted build never
    deletes anything."""
    expected = _WRITTEN_PATHS
    # Compare resolved paths to be safe.
    for p in list(out.rglob("*")):
        if p.is_file():
            if p.resolve() not in expected:
                try:
                    p.unlink()
                    _WRITE_COUNTER["deleted"] += 1
                except OSError:
                    pass
    # Drop empty dirs (deepest first).
    for p in sorted(out.rglob("*"), key=lambda x: -len(x.parts)):
        if p.is_dir():
            try:
                p.rmdir()
            except OSError:
                pass  # not empty, fine


# === HTML LAYOUT / TEMPLATES ===========================================

UMAMI_SNIPPET = (
    '<script defer src="https://cloud.umami.is/script.js" '
    'data-website-id="abe09860-85be-4b06-8383-002f2e598061" '
    'data-exclude-search="true"></script>'
)

CSP_META = (
    '<meta http-equiv="Content-Security-Policy" content='
    "\"default-src 'self'; script-src 'self' https://cloud.umami.is; "
    "style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
    "connect-src 'self' https://cloud.umami.is https://api-gateway.umami.dev; "
    "object-src 'none'; base-uri 'self'; form-action 'none'; "
    'upgrade-insecure-requests" />'
)


def base_template(
    *,
    title: str,
    description: str,
    body: str,
    canonical: str,
    site_url: str,
    cachebust: str,
    extra_head: str = "",
    rel_alternate: list[tuple[str, str, str]] | None = None,
    home_relative_prefix: str = "",
) -> str:
    """Return a complete HTML document.

    `home_relative_prefix` is "../" * depth — used to point relative asset
    references back to the site root from a nested path.
    """
    rel_alternate = rel_alternate or []
    alt_links = "".join(
        f'<link rel="alternate" type="{_escape(t)}" title="{_escape(title_)}" href="{_escape(href)}" />'
        for t, title_, href in rel_alternate
    )
    pfx = home_relative_prefix
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="#0e1116" media="(prefers-color-scheme: dark)" />
<meta name="theme-color" content="#fafbfc" media="(prefers-color-scheme: light)" />
{CSP_META}
<meta name="referrer" content="strict-origin-when-cross-origin" />
<title>{_escape(title)}</title>
<meta name="description" content="{_escape(description)}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{_escape(canonical)}" />
<meta property="og:site_name" content="CTI Briefs" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{_escape(title)}" />
<meta property="og:description" content="{_escape(description)}" />
<meta property="og:url" content="{_escape(canonical)}" />
<meta property="og:locale" content="en_US" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{_escape(title)}" />
<meta name="twitter:description" content="{_escape(description)}" />
<link rel="stylesheet" href="{pfx}assets/css/styles.css?v={cachebust}" />
<link rel="alternate" type="application/rss+xml" title="CTI Briefs — Daily" href="{pfx}feed.xml" />
<link rel="alternate" type="application/rss+xml" title="CTI Briefs — Weekly" href="{pfx}feed-weekly.xml" />
<link rel="alternate" type="application/rss+xml" title="CTI Briefs — Per item" href="{pfx}feed-items.xml" />
<link rel="sitemap" type="application/xml" href="{pfx}sitemap.xml" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23e85d75'/%3E%3Ctext x='50%25' y='52%25' text-anchor='middle' dominant-baseline='middle' font-family='ui-monospace,monospace' font-size='15' font-weight='700' fill='%230e1116'%3ECTI%3C/text%3E%3C/svg%3E" />
{alt_links}
{UMAMI_SNIPPET}
<script defer src="{pfx}assets/js/theme.js?v={cachebust}"></script>
<script defer src="{pfx}assets/vendor/filter.min.js?v={cachebust}"></script>
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="bar-inner">
    <a class="brand" href="{pfx}" aria-label="Home — CTI Briefs">
      <span class="brand-mark" aria-hidden="true">CTI</span>
      <span class="brand-text"><strong>CTI&nbsp;Briefs</strong><small>Switzerland · Europe · Public sector</small></span>
    </a>
    <nav class="nav" aria-label="Primary">
      <a href="{pfx}">Home</a>
      <a href="{pfx}briefs/">Briefs</a>
      <a href="{pfx}cves/">CVEs</a>
      <a href="{pfx}topics/">Topics</a>
      <a href="{pfx}sources/">Sources</a>
      <a href="{pfx}ops/">Ops</a>
      <a href="{pfx}about/">About</a>
    </nav>
    <button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle colour theme" title="Theme: system">
      <svg class="theme-icon theme-icon--system" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 5h18v11H3z" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M9 20h6M12 16v4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>
      <svg class="theme-icon theme-icon--light" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" fill="currentColor"/><g stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/></g></svg>
      <svg class="theme-icon theme-icon--dark" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M21 14a8 8 0 1 1-11-11 7 7 0 0 0 11 11z" fill="currentColor"/></svg>
    </button>
  </div>
</header>
<main id="main" class="main">{body}</main>
<footer class="footer">
  <div class="footer-inner">
    <p><strong>AI-generated content, no human review.</strong> Every brief is produced autonomously by an LLM running as a Claude Code routine; every claim links to a primary source. <a href="{pfx}about/">How this works →</a></p>
    <p class="meta">
      <a href="{pfx}feed.xml">RSS — daily</a> · <a href="{pfx}feed-weekly.xml">weekly</a> · <a href="{pfx}feed-items.xml">per item</a>
    </p>
  </div>
</footer>
</body>
</html>
"""


def render_tag_pill(tag: str, *, prefix: str = "") -> str:
    return f'<a class="pill pill-tag" href="{prefix}tags/{_escape(tag)}/">{_escape(tag)}</a>'


def render_region_pill(region: str, *, prefix: str = "") -> str:
    return f'<a class="pill pill-region" href="{prefix}regions/{_escape(region)}/">{_escape(region)}</a>'


def render_cve_pill(cve: str, *, prefix: str = "") -> str:
    return f'<a class="pill pill-cve" href="{prefix}cves/{_escape(cve)}/">{_escape(cve)}</a>'


def render_footer_html(footer: dict[str, Any], *, prefix: str = "") -> str:
    """Structured HTML rendering of a per-item metadata footer (renders as
    distinct badge / pill blocks instead of raw italic text). Used inside
    every `<article>` on a brief page and in `<content:encoded>` for the
    items RSS feed."""
    parts: list[str] = []

    # Sources (primary + additional)
    if footer.get("sources"):
        src_parts = []
        for i, src in enumerate(footer["sources"]):
            label = _escape(src.get("label", ""))
            url = _escape(src.get("url", ""))
            cls = "src-primary" if i == 0 else "src-additional"
            src_parts.append(f'<a class="{cls}" href="{url}" rel="noopener noreferrer">{label}</a>')
        parts.append('<span class="meta-sources"><strong>Sources:</strong> ' + " · ".join(src_parts) + "</span>")

    if footer.get("regions"):
        parts.append(
            '<span class="meta-regions"><strong>Region:</strong> '
            + " ".join(render_region_pill(r, prefix=prefix) for r in footer["regions"])
            + "</span>"
        )
    if footer.get("tags"):
        parts.append(
            '<span class="meta-tags"><strong>Tags:</strong> '
            + " ".join(render_tag_pill(t, prefix=prefix) for t in footer["tags"])
            + "</span>"
        )
    if footer.get("cve"):
        parts.append(
            '<span class="meta-cve"><strong>CVE:</strong> '
            + render_cve_pill(footer["cve"], prefix=prefix)
            + "</span>"
        )
    if footer.get("cvss"):
        parts.append(f'<span class="meta-cvss"><strong>CVSS:</strong> {_escape(footer["cvss"])}</span>')
    if footer.get("vector"):
        parts.append(f'<span class="meta-vector"><strong>Vector:</strong> {_escape(footer["vector"])}</span>')
    if footer.get("auth"):
        parts.append(f'<span class="meta-auth"><strong>Auth:</strong> {_escape(footer["auth"])}</span>')
    if footer.get("status"):
        parts.append(
            '<span class="meta-status"><strong>Status:</strong> '
            + ", ".join(_escape(s) for s in footer["status"])
            + "</span>"
        )

    return '<aside class="item-footer">' + "".join(parts) + "</aside>"


def render_brief_page(
    brief: dict[str, Any],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Render the static HTML page for a single brief (daily or weekly)."""
    sections_html: list[str] = []
    # Toc + filter chips union
    all_tags: set[str] = set()
    all_regions: set[str] = set()
    section_keys_in_brief: list[tuple[str, str]] = []  # (key, heading)
    for sec in brief["sections"]:
        section_keys_in_brief.append((sec["key"], sec["heading"]))
        for it in sec["items"]:
            if it["footer"]:
                for t in it["footer"].get("tags", []):
                    all_tags.add(t)
                for r in it["footer"].get("regions", []):
                    all_regions.add(r)

    # Filter / TOC bar
    chips_html = ""
    if all_tags or all_regions or section_keys_in_brief:
        tag_chips = "".join(
            f'<button class="chip chip-tag" data-tag="{_escape(t)}" type="button">{_escape(t)}</button>'
            for t in sorted(all_tags)
        )
        region_chips = "".join(
            f'<button class="chip chip-region" data-region="{_escape(r)}" type="button">{_escape(r)}</button>'
            for r in sorted(all_regions)
        )
        section_toggles = "".join(
            f'<button class="chip chip-section" data-target="{_escape(slugify(h))}" type="button" aria-pressed="true">{_escape(h)}</button>'
            for k, h in section_keys_in_brief
        )
        chips_html = f"""
<div class="filter-bar" data-filter="brief">
  <details class="filter-group" open>
    <summary>Sections</summary>
    <div class="chip-row chip-row-sections">{section_toggles}</div>
  </details>
  {('<details class="filter-group"><summary>Filter by region</summary><div class="chip-row chip-row-regions">' + region_chips + '</div></details>') if region_chips else ''}
  {('<details class="filter-group"><summary>Filter by tag</summary><div class="chip-row chip-row-tags">' + tag_chips + '</div></details>') if tag_chips else ''}
  <button type="button" class="filter-clear" data-action="clear-filters">Clear filters</button>
  <p class="filter-status" data-role="filter-status" hidden></p>
</div>
"""

    # Render each section
    md_base = canonical
    for sec in brief["sections"]:
        skey = sec["key"]
        heading = sec["heading"]
        anchor = sec["anchor"]
        section_inner: list[str] = []
        if sec["items"]:
            for it in sec["items"]:
                tags_attr = " ".join(it["footer"].get("tags", [])) if it["footer"] else ""
                regions_attr = " ".join(it["footer"].get("regions", [])) if it["footer"] else ""
                # Render Markdown body
                body_html = render_markdown(it["body_md"], base_url=md_base)
                footer_html = render_footer_html(it["footer"], prefix=prefix) if it["footer"] else ""
                article_id = it["anchor"]
                slug = it["slug"]
                section_inner.append(
                    f'<article class="brief-item" '
                    f'data-tags="{_escape(tags_attr)}" '
                    f'data-regions="{_escape(regions_attr)}" '
                    f'data-section="{_escape(skey)}" '
                    f'id="{_escape(article_id)}">'
                    f'<header class="item-header"><h3>'
                    f'<a class="item-link" href="{prefix}items/{_escape(slug)}/">{_escape(it["heading"])}</a>'
                    f'</h3></header>'
                    f'<div class="item-body">{body_html}</div>'
                    f'{footer_html}'
                    f"</article>"
                )
        else:
            # Render the section body straight as Markdown if no items
            section_inner.append(render_markdown(sec["body_md"], base_url=md_base))

        sections_html.append(
            f'<section class="brief-section" data-section="{_escape(skey)}" id="{_escape(anchor)}">'
            f'<h2><a class="section-anchor" href="#{_escape(anchor)}">{_escape(heading)}</a></h2>'
            + "".join(section_inner)
            + "</section>"
        )

    nav_html = (
        f'<nav class="brief-meta">'
        f'<p>Published {_escape(brief["publish_iso"][:10])}'
        + (f' · Prompt v{_escape(brief["prompt_version"])}' if brief.get("prompt_version") else "")
        + (f' · {_escape(brief["generated_by"])}' if brief.get("generated_by") else "")
        + "</p>"
        + "</nav>"
    )

    article = f"""
<article class="brief brief-{_escape(brief['kind'])}" data-brief="{_escape(brief['name'])}">
  <header class="brief-header">
    <h1>{_escape(brief['title'])}</h1>
    {nav_html}
    <p class="brief-notice"><strong>AI-generated content — no human review.</strong> This brief was produced autonomously by an LLM. Every claim links inline to its primary source. Verify any operationally critical claim before acting.</p>
  </header>
  {chips_html}
  <div class="brief-body">
    {''.join(sections_html)}
  </div>
</article>
"""
    description = brief.get("summary") or f"{brief['kind'].capitalize()} CTI brief — {brief['title']}"
    return base_template(
        title=brief["title"],
        description=description,
        body=article,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_item_page(
    item: dict[str, Any],
    *,
    brief: dict[str, Any],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Render the static HTML page for a single brief item (one per
    metadata-footer block)."""
    body_html = render_markdown(item["body_md"], base_url=canonical)
    footer_html = render_footer_html(item["footer"], prefix=prefix) if item["footer"] else ""
    brief_url = f"{prefix}briefs/" + ("weekly/" if brief["kind"] == "weekly" else "") + f"{brief['name']}/"
    description = (item["heading"][:280]) if item.get("heading") else f"Item from {brief['title']}"
    body = f"""
<article class="item single-item">
  <nav class="breadcrumb"><a href="{prefix}">Home</a> · <a href="{prefix}briefs/">Briefs</a> · <a href="{_escape(brief_url)}">{_escape(brief['title'])}</a></nav>
  <header><h1>{_escape(item['heading'])}</h1>
    <p class="item-meta">From <a href="{_escape(brief_url)}#{_escape(item['anchor'])}">{_escape(brief['title'])}</a> · published {_escape(brief['publish_iso'][:10])}</p>
  </header>
  <div class="item-body">{body_html}</div>
  {footer_html}
</article>
"""
    return base_template(
        title=item["heading"],
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_cve_page(cve: dict[str, Any], *, site_url: str, cachebust: str, prefix: str, canonical: str) -> str:
    title = f"{cve['id']} — {cve.get('title') or 'CTI brief coverage'}"
    apps_html = (
        '<ul class="appearances">'
        + "".join(
            f'<li><a href="{prefix}briefs/{_escape(b)}/">{_escape(b)}</a></li>'
            for b in cve.get("appearances", [])
        )
        + "</ul>"
    )
    cites_html = (
        '<ul class="citations">'
        + "".join(
            f'<li><a href="{_escape(c["url"])}" rel="noopener noreferrer">{_escape(c.get("label", c["url"]))}</a> '
            f'<span class="hint">{_escape(c.get("host", ""))}</span></li>'
            for c in cve.get("citations", [])
        )
        + "</ul>"
    )
    body = f"""
<article class="cve">
  <nav class="breadcrumb"><a href="{prefix}">Home</a> · <a href="{prefix}cves/">CVEs</a></nav>
  <header><h1>{_escape(cve['id'])}</h1>
    <p class="hint">{_escape(cve.get('title') or '')}</p>
    {('<p><a class="primary-link" href="' + _escape(cve['primary_source_url']) + '" rel="noopener noreferrer">Primary source: ' + _escape(cve['primary_source_url']) + '</a></p>') if cve.get('primary_source_url') else ''}
    <p class="hint">First seen: {_escape(cve.get('first_seen','?'))} · Last seen: {_escape(cve.get('last_seen','?'))}</p>
  </header>
  <section><h2>Appearances</h2>{apps_html}</section>
  <section><h2>All cited sources for this CVE</h2>{cites_html}</section>
</article>
"""
    return base_template(
        title=title,
        description=cve.get("title") or f"{cve['id']} — appearances across CTI briefs",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_source_page(
    source: dict[str, Any], *, site_url: str, cachebust: str, prefix: str, canonical: str
) -> str:
    title = f"{source.get('publisher', source['id'])} — Source"
    apps_html = (
        '<ul class="appearances">'
        + "".join(
            f'<li><a href="{prefix}briefs/{_escape(b)}/">{_escape(b)}</a></li>'
            for b in source.get("appearances", [])
        )
        + "</ul>"
    )
    cats = ", ".join(source.get("category", []))
    body = f"""
<article class="source">
  <nav class="breadcrumb"><a href="{prefix}">Home</a> · <a href="{prefix}sources/">Sources</a></nav>
  <header><h1>{_escape(source.get('publisher', source['id']))}</h1>
    <p class="hint"><a href="{_escape(source.get('url', ''))}" rel="noopener noreferrer">{_escape(source.get('url', ''))}</a></p>
    <p class="hint">Reliability: {_escape(source.get('reliability', '?'))} · Status: {_escape(source.get('status', '?'))} · Category: {_escape(cats)}</p>
  </header>
  <section><h2>Appearances</h2>{apps_html}</section>
</article>
"""
    return base_template(
        title=title,
        description=f"{source.get('publisher', source['id'])} — {cats}",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_topic_page(topic: dict[str, Any], *, site_url: str, cachebust: str, prefix: str, canonical: str) -> str:
    title = f"{topic.get('title', topic['key'])} — Topic"
    apps_html = (
        '<ul class="appearances">'
        + "".join(
            f'<li><a href="{prefix}briefs/{_escape(b)}/">{_escape(b)}</a></li>'
            for b in topic.get("briefs", [])
        )
        + "</ul>"
    )
    cites_html = (
        '<ul class="citations">'
        + "".join(
            f'<li><a href="{_escape(c["url"])}" rel="noopener noreferrer">{_escape(c.get("label", c["url"]))}</a></li>'
            for c in topic.get("citations", [])
        )
        + "</ul>"
    )
    body = f"""
<article class="topic">
  <nav class="breadcrumb"><a href="{prefix}">Home</a> · <a href="{prefix}topics/">Topics</a></nav>
  <header><h1>{_escape(topic.get('title', topic['key']))}</h1>
    <p class="hint">Type: {_escape(topic.get('type', '?'))} · First covered {_escape(topic.get('first_covered', '?'))} · Last covered {_escape(topic.get('last_covered', '?'))}</p>
    {('<p class="hint">Verification flags: ' + ", ".join(_escape(f) for f in topic.get('flags', [])) + '</p>') if topic.get('flags') else ''}
  </header>
  <section><h2>Briefs that mentioned this topic</h2>{apps_html}</section>
  <section><h2>Cited sources</h2>{cites_html}</section>
</article>
"""
    return base_template(
        title=title,
        description=topic.get("title", topic["key"]),
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_index_page(
    *,
    title: str,
    intro: str,
    items: list[tuple[str, str, str]],  # (label, href, hint)
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
    description: str,
) -> str:
    """Generic listing page."""
    rows = "".join(
        f'<li class="index-row"><a class="index-label" href="{_escape(href)}">{_escape(label)}</a>'
        + (f' <span class="index-hint">{_escape(hint)}</span>' if hint else "")
        + "</li>"
        for label, href, hint in items
    )
    body = f"""
<section class="index-page">
  <h1>{_escape(title)}</h1>
  <p class="intro">{_escape(intro)}</p>
  <ul class="index-list">{rows}</ul>
</section>
"""
    return base_template(
        title=title,
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_home_page(
    latest: dict[str, Any] | None,
    recent_daily: list[dict[str, Any]],
    recent_weekly: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    canonical: str,
) -> str:
    pfx = ""  # home is at /
    latest_block = ""
    if latest:
        url = f"briefs/{'weekly/' if latest['kind'] == 'weekly' else ''}{latest['name']}/"
        tldr_html = ""
        if latest.get("tldr"):
            tldr_html = "<ul class='tldr'>" + "".join(
                f"<li>{render_inline(t, base_url=canonical)}</li>" for t in latest["tldr"][:6]
            ) + "</ul>"
        latest_block = f"""
<section class="home-latest">
  <h2><a href="{_escape(url)}">{_escape(latest['title'])}</a></h2>
  <p class="hint">Published {_escape(latest['publish_iso'][:10])}</p>
  {tldr_html}
  <p><a class="cta" href="{_escape(url)}">Read the full brief →</a></p>
</section>
"""

    def list_block(title_: str, items: list[dict[str, Any]], kind_path: str) -> str:
        rows = "".join(
            f'<li><a href="{_escape("briefs/" + kind_path + b["name"] + "/")}">{_escape(b["title"])}</a> '
            f'<span class="hint">{_escape(b["publish_iso"][:10])}</span></li>'
            for b in items[:10]
        )
        return f"<section class='home-list'><h3>{_escape(title_)}</h3><ul>{rows}</ul></section>"

    recent_html = ""
    if recent_daily:
        recent_html += list_block("Recent daily briefs", recent_daily, "")
    if recent_weekly:
        recent_html += list_block("Recent weekly summaries", recent_weekly, "weekly/")

    body = f"""
<section class="home-hero">
  <h1>CTI Briefs</h1>
  <p class="lede">Daily and weekly cyber threat intelligence — Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.</p>
</section>
{latest_block}
{recent_html}
<script>
(function(){{
  // Bootstrap redirect for the legacy SPA hash routes. One-time, indexed
  // hash URLs that crawlers may have picked up get a clean URL.
  var h = window.location.hash || "";
  if (!h) return;
  var m;
  m = h.match(/^#\\/briefs\\/(\\d{{4}}-\\d{{2}}-\\d{{2}})$/);
  if (m) {{ window.location.replace("briefs/" + m[1] + "/"); return; }}
  m = h.match(/^#\\/briefs\\/(\\d{{4}}-W\\d{{2}})$/);
  if (m) {{ window.location.replace("briefs/weekly/" + m[1] + "/"); return; }}
  m = h.match(/^#\\/cves\\/(CVE-[0-9]+-[0-9]+)$/);
  if (m) {{ window.location.replace("cves/" + m[1] + "/"); return; }}
  m = h.match(/^#\\/sources\\/(.+)$/);
  if (m) {{ window.location.replace("sources/" + decodeURIComponent(m[1]) + "/"); return; }}
  m = h.match(/^#\\/topics\\/(.+)$/);
  if (m) {{ window.location.replace("topics/" + decodeURIComponent(m[1]) + "/"); return; }}
  m = h.match(/^#\\/(briefs|cves|topics|sources|ops|about)$/);
  if (m) {{ window.location.replace(m[1] + "/"); return; }}
}})();
</script>
"""
    return base_template(
        title="CTI Briefs — Switzerland, Europe & Public Sector",
        description="Daily and weekly cyber threat intelligence (CTI) briefs covering Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=pfx,
    )


def render_static_doc(
    *, md_text: str, title: str, description: str, prefix: str, canonical: str, site_url: str, cachebust: str
) -> str:
    body = f"""
<article class="static-doc">
  {render_markdown(md_text, base_url=canonical)}
</article>
"""
    return base_template(
        title=title,
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_ops_page(
    run_log: dict[str, Any] | None, *, prefix: str, site_url: str, cachebust: str, canonical: str
) -> str:
    if not run_log or not run_log.get("runs"):
        body = "<section><h1>Operations</h1><p>No run log available yet.</p></section>"
    else:
        rows = []
        for r in reversed(run_log["runs"][-30:]):
            rows.append(
                f'<tr><td>{_escape(r.get("date","?"))}</td>'
                f'<td>{_escape(r.get("model","?"))}</td>'
                f'<td>{_escape(str(r.get("items_published","")))}</td>'
                f'<td>{_escape(r.get("deep_dive") or "—")}</td></tr>'
            )
        body = (
            "<section class='ops-page'><h1>Operations</h1>"
            "<table class='ops-runs'><thead><tr><th>Date</th><th>Model</th><th>Items</th><th>Deep dive</th></tr></thead><tbody>"
            + "".join(rows)
            + "</tbody></table></section>"
        )
    return base_template(
        title="Operations dashboard — CTI Briefs",
        description="Recent runs, sub-agent allocation, and source maintenance signals.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === RSS BUILDERS ======================================================

def _xml_validate(content: str) -> list[str]:
    try:
        ET.fromstring(content)
        return []
    except ET.ParseError as e:
        return [str(e)]


def _channel_rss(
    *,
    title: str,
    link: str,
    self_link: str,
    description: str,
    last_build: str,
    items_xml: str,
) -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<rss version="2.0" '
        'xmlns:atom="http://www.w3.org/2005/Atom" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/">'
        '<channel>'
        f'<title>{_escape(title)}</title>'
        f'<link>{_escape(link)}</link>'
        f'<atom:link href="{_escape(self_link)}" rel="self" type="application/rss+xml"/>'
        f'<description>{_escape(description)}</description>'
        '<language>en</language>'
        f'<lastBuildDate>{last_build}</lastBuildDate>'
        f'{items_xml}'
        '</channel></rss>'
    )


def _fallback_lastbuild(briefs: list[dict[str, Any]]) -> datetime:
    """If a feed has no entries, use the most-recent input timestamp across
    *all* briefs as the lastBuildDate. Deterministic and meaningful (the
    site as a whole was last built at this moment) without falling back to
    `now()`."""
    if not briefs:
        # No briefs at all — extremely unlikely. Use a stable epoch so
        # the build is still deterministic.
        return datetime(2000, 1, 1, tzinfo=timezone.utc)
    return max(b["publish_ts"] for b in briefs)


def build_daily_feed(briefs: list[dict[str, Any]], *, site_url: str) -> tuple[str, datetime]:
    """Daily feed: one item per daily brief. Last 30."""
    daily = [b for b in briefs if b["kind"] == "daily"][:FEED_DAILY_MAX]
    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for b in daily:
        url = f"{site_url}briefs/{b['name']}/"
        # Render full brief HTML body for content:encoded.
        body_md = b["text"]
        # Strip the H1 line + blockquote notice from the rendered body so the
        # feed shows the actual content. Keep TL;DR onwards.
        body_md_clean = re.sub(r"\A# .+?\n+(> .+?\n+)?\*\*Generated by:\*\*[^\n]*\n+", "", body_md)
        body_html = render_markdown(body_md_clean, base_url=url)
        # TL;DR -> description
        if b.get("tldr"):
            desc_html = "<ul>" + "".join(f"<li>{render_inline(t, base_url=url)}</li>" for t in b["tldr"][:6]) + "</ul>"
        else:
            desc_html = f"<p>{_escape(b.get('summary',''))}</p>"
        cats = "".join(f"<category>{_escape(c)}</category>" for c in b.get("cves", [])[:8])
        items_xml.append(
            f"<item>"
            f"<title>{_escape(b['title'])}</title>"
            f"<link>{_escape(url)}</link>"
            f'<guid isPermaLink="true">{_escape(url)}</guid>'
            f"<pubDate>{b['publish_rfc822']}</pubDate>"
            f"<dc:date>{_escape(b['publish_iso'])}</dc:date>"
            f"{cats}"
            f"<description><![CDATA[{desc_html}]]></description>"
            f"<content:encoded><![CDATA[{body_html}]]></content:encoded>"
            f"</item>"
        )
        if b["publish_ts"] > most_recent:
            most_recent = b["publish_ts"]
    feed = _channel_rss(
        title="CTI Briefs — Daily (Switzerland, Europe & Public Sector)",
        link=site_url,
        self_link=site_url + "feed.xml",
        description="Daily cyber threat intelligence briefs covering Switzerland, Europe, and the public sector — autonomously generated, source-linked, IOC-free.",
        last_build=rfc822(most_recent if daily else _fallback_lastbuild(briefs)),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


def build_weekly_feed(briefs: list[dict[str, Any]], *, site_url: str) -> tuple[str, datetime]:
    weekly = [b for b in briefs if b["kind"] == "weekly"][:FEED_WEEKLY_MAX]
    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for b in weekly:
        url = f"{site_url}briefs/weekly/{b['name']}/"
        body_md = b["text"]
        body_md_clean = re.sub(r"\A# .+?\n+(> .+?\n+)?\*\*Generated by:\*\*[^\n]*\n+", "", body_md)
        body_html = render_markdown(body_md_clean, base_url=url)
        desc_html = f"<p>{_escape(b.get('summary',''))}</p>" if b.get("summary") else f"<p>Weekly CTI summary — {_escape(b['name'])}</p>"
        cats = "".join(f"<category>{_escape(c)}</category>" for c in b.get("cves", [])[:8])
        items_xml.append(
            f"<item>"
            f"<title>{_escape(b['title'])}</title>"
            f"<link>{_escape(url)}</link>"
            f'<guid isPermaLink="true">{_escape(url)}</guid>'
            f"<pubDate>{b['publish_rfc822']}</pubDate>"
            f"<dc:date>{_escape(b['publish_iso'])}</dc:date>"
            f"{cats}"
            f"<description><![CDATA[{desc_html}]]></description>"
            f"<content:encoded><![CDATA[{body_html}]]></content:encoded>"
            f"</item>"
        )
        if b["publish_ts"] > most_recent:
            most_recent = b["publish_ts"]
    feed = _channel_rss(
        title="CTI Briefs — Weekly (Switzerland, Europe & Public Sector)",
        link=site_url,
        self_link=site_url + "feed-weekly.xml",
        description="Weekly cyber threat intelligence summaries — multi-day campaigns, sector patterns, policy horizon.",
        last_build=rfc822(most_recent if weekly else _fallback_lastbuild(briefs)),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


def build_items_feed(briefs: list[dict[str, Any]], *, site_url: str) -> tuple[str, datetime]:
    """Per-item feed: one entry per brief item that carried a metadata footer."""
    item_entries: list[dict[str, Any]] = []
    for b in briefs:
        for sec in b["sections"]:
            # TL;DR + Verification Notes do not become items.
            if sec["key"] in ("tldr", "verification-notes"):
                continue
            for it in sec["items"]:
                if not it["footer"]:
                    continue
                slug = it["slug"]
                url = f"{site_url}items/{slug}/"
                item_entries.append(
                    {
                        "url": url,
                        "title": it["heading"],
                        "publish_ts": b["publish_ts"],
                        "publish_rfc822": b["publish_rfc822"],
                        "publish_iso": b["publish_iso"],
                        "body_md": it["body_md"],
                        "footer": it["footer"],
                        "section_key": sec["key"],
                    }
                )
    item_entries.sort(key=lambda x: x["publish_ts"], reverse=True)
    item_entries = item_entries[:FEED_ITEMS_MAX]

    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for it in item_entries:
        body_html = render_markdown(it["body_md"], base_url=it["url"]) + render_footer_html(it["footer"], prefix=site_url)
        # categories: tags + regions + status flags + cve id
        cat_parts = list(it["footer"].get("tags", [])) + list(it["footer"].get("regions", [])) + list(it["footer"].get("status", []))
        if it["footer"].get("cve"):
            cat_parts.append(it["footer"]["cve"])
        cats = "".join(f"<category>{_escape(c)}</category>" for c in cat_parts[:16])
        # description = first paragraph of body
        desc_md = it["body_md"].split("\n\n", 1)[0] if it["body_md"] else ""
        desc_html = render_markdown(desc_md, base_url=it["url"])
        items_xml.append(
            f"<item>"
            f"<title>{_escape(it['title'])}</title>"
            f"<link>{_escape(it['url'])}</link>"
            f'<guid isPermaLink="true">{_escape(it['url'])}</guid>'
            f"<pubDate>{it['publish_rfc822']}</pubDate>"
            f"<dc:date>{_escape(it['publish_iso'])}</dc:date>"
            f"{cats}"
            f"<description><![CDATA[{desc_html}]]></description>"
            f"<content:encoded><![CDATA[{body_html}]]></content:encoded>"
            f"</item>"
        )
        if it["publish_ts"] > most_recent:
            most_recent = it["publish_ts"]
    feed = _channel_rss(
        title="CTI Briefs — Per item",
        link=site_url,
        self_link=site_url + "feed-items.xml",
        description="Individual content blocks from CTI briefs (Immediate Actions, Active Threats, Trending Vulnerabilities, Research, Updates, Deep Dive).",
        last_build=rfc822(most_recent if item_entries else _fallback_lastbuild(briefs)),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


# === SOURCE / CVE / TOPIC ANNOTATION ===================================

def annotate_sources(sources: dict[str, Any], briefs: list[dict[str, Any]]) -> dict[str, Any]:
    prefixes: list[tuple[str, str, str]] = []
    for s in sources["sources"]:
        pfx = url_prefix_of(s["url"])
        host = host_of(s["url"])
        if pfx or host:
            prefixes.append((pfx, host, s["id"]))
    prefixes.sort(key=lambda t: (len(t[0]), len(t[1])), reverse=True)

    src_appearances: dict[str, set[str]] = defaultdict(set)
    for b in briefs:
        for link in b["links"]:
            link_pfx = link.get("prefix", "")
            link_host = link.get("host", "")
            if not link_pfx and not link_host:
                continue
            best_id = None
            for pfx, host, sid in prefixes:
                if pfx and link_pfx.startswith(pfx):
                    best_id = sid
                    break
            if best_id is None:
                for _, host, sid in prefixes:
                    if not host:
                        continue
                    if link_host == host or link_host.endswith("." + host):
                        best_id = sid
                        break
            if best_id:
                src_appearances[best_id].add(b["name"])
    enriched = []
    for s in sources["sources"]:
        appearances = sorted(src_appearances.get(s["id"], []), reverse=True)
        enriched.append({**s, "appearances": appearances})
    return {**sources, "sources": enriched}


def annotate_cves(cves: dict[str, Any], briefs: list[dict[str, Any]], sources: dict[str, Any]) -> dict[str, Any]:
    by_id: dict[str, set[str]] = defaultdict(set)
    citations_by_id: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)

    src_prefixes: list[tuple[str, str, str]] = []
    for s in sources.get("sources", []):
        pfx = url_prefix_of(s["url"])
        host = host_of(s["url"])
        if pfx or host:
            src_prefixes.append((pfx, host, s["id"]))
    src_prefixes.sort(key=lambda t: (len(t[0]), len(t[1])), reverse=True)

    def resolve_source(host: str, prefix: str) -> str | None:
        for pfx, _h, sid in src_prefixes:
            if pfx and prefix.startswith(pfx):
                return sid
        for _p, h, sid in src_prefixes:
            if not h:
                continue
            if host == h or host.endswith("." + h):
                return sid
        return None

    for b in briefs:
        for cve in b["cves"]:
            by_id[cve].add(b["name"])
        for cve_id, cites in (b.get("cve_citations") or {}).items():
            bucket = citations_by_id[cve_id]
            for cite in cites:
                key = cite["url"]
                if key in bucket:
                    if b["name"] not in bucket[key]["briefs"]:
                        bucket[key]["briefs"].append(b["name"])
                    continue
                bucket[key] = {
                    "label": cite["label"],
                    "url": cite["url"],
                    "host": cite.get("host", ""),
                    "source_id": resolve_source(cite.get("host", ""), cite.get("prefix", "")),
                    "briefs": [b["name"]],
                }

    enriched = []
    seen_ids = set()
    for c in cves.get("cves", []):
        appearances = sorted(by_id.get(c["id"], []), reverse=True)
        cites = sorted(citations_by_id.get(c["id"], {}).values(), key=lambda x: x.get("host") or x["url"])
        enriched.append({**c, "appearances": appearances, "citations": cites})
        seen_ids.add(c["id"])
    for cid, briefs_set in by_id.items():
        if cid in seen_ids:
            continue
        cites = sorted(citations_by_id.get(cid, {}).values(), key=lambda x: x.get("host") or x["url"])
        enriched.append(
            {
                "id": cid,
                "first_seen": min(briefs_set),
                "last_seen": max(briefs_set),
                "title": "",
                "primary_source_url": "",
                "appearances": sorted(briefs_set, reverse=True),
                "citations": cites,
            }
        )
    enriched.sort(key=lambda c: c["last_seen"], reverse=True)
    return {**cves, "cves": enriched}


def annotate_topics(items: dict[str, Any], briefs: list[dict[str, Any]], sources: dict[str, Any]) -> dict[str, Any]:
    flag_lookup: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for b in briefs:
        for heading, flags in b.get("item_flags", {}).items():
            flag_lookup[b["name"]].append((heading.lower(), flags[0] if flags else ""))

    src_prefixes: list[tuple[str, str, str]] = []
    for s in sources.get("sources", []):
        pfx = url_prefix_of(s["url"])
        host = host_of(s["url"])
        if pfx or host:
            src_prefixes.append((pfx, host, s["id"]))
    src_prefixes.sort(key=lambda t: (len(t[0]), len(t[1])), reverse=True)

    def resolve_source(host: str, prefix: str) -> str | None:
        for pfx, _h, sid in src_prefixes:
            if pfx and prefix.startswith(pfx):
                return sid
        for _p, h, sid in src_prefixes:
            if not h:
                continue
            if host == h or host.endswith("." + h):
                return sid
        return None

    def topic_phrase(t: dict[str, Any]) -> str:
        title = (t.get("title") or "").strip()
        if not title:
            return (t.get("key") or "").strip()
        for sep in (" — ", " – ", ": "):
            if sep in title:
                title = title.split(sep, 1)[0]
                break
        return title.strip()

    topic_match: list[dict[str, Any]] = []
    for it in items.get("items", []):
        ttype = (it.get("type") or "").lower()
        phrase = topic_phrase(it).lower()
        cve_match = (it.get("key") or "").upper() if ttype == "cve" else None
        topic_match.append({"key": it["key"], "phrase": phrase, "cve_match": cve_match})

    citations_by_key: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for b in briefs:
        for unit in b.get("unit_data") or []:
            text_lower = unit["text_lower"]
            cves_in_unit = unit["cves"]
            if len(cves_in_unit) > 3:
                continue
            matched_keys: list[str] = []
            for tm in topic_match:
                if tm["cve_match"] and tm["cve_match"] in cves_in_unit:
                    matched_keys.append(tm["key"])
                elif tm["phrase"] and len(tm["phrase"]) >= 4 and tm["phrase"] in text_lower:
                    matched_keys.append(tm["key"])
            if not matched_keys or len(matched_keys) > 3:
                continue
            for link in unit["links"]:
                for k in matched_keys:
                    bucket = citations_by_key[k]
                    if link["url"] in bucket:
                        if b["name"] not in bucket[link["url"]]["briefs"]:
                            bucket[link["url"]]["briefs"].append(b["name"])
                        continue
                    bucket[link["url"]] = {
                        "label": link["label"],
                        "url": link["url"],
                        "host": link["host"],
                        "source_id": resolve_source(link["host"], link.get("prefix", "")),
                        "briefs": [b["name"]],
                    }

    enriched = []
    for it in items.get("items", []):
        names = []
        flags: set[str] = set()
        title_norm = (it.get("title") or "").lower()
        key_norm = (it.get("key") or "").lower()
        for app in it.get("appearances", []):
            bp = app.get("brief_path", "")
            m = re.search(r"(\d{4}-\d{2}-\d{2}|\d{4}-W\d{2})", bp)
            if m:
                bn = m.group(1)
                names.append(bn)
                for heading_lower, flag in flag_lookup.get(bn, []):
                    if not flag:
                        continue
                    if title_norm and (title_norm in heading_lower or heading_lower in title_norm):
                        flags.add(flag)
                    elif key_norm and key_norm in heading_lower:
                        flags.add(flag)
        names = sorted(set(names), reverse=True)
        cites = sorted(citations_by_key.get(it["key"], {}).values(), key=lambda x: x.get("host") or x["url"])
        enriched.append({**it, "briefs": names, "flags": sorted(flags), "citations": cites})
    enriched.sort(key=lambda i: i.get("last_covered", ""), reverse=True)
    return {**items, "items": enriched}


# === SITE ASSETS COPY ==================================================

def copy_assets() -> None:
    """Copy site/assets to _site/assets via atomic_write_bytes so unchanged
    files aren't re-written. Strip sourceMappingURL from vendored libs in
    the deployed copy (kept pristine in source tree for HASHES integrity
    verification)."""
    src = SITE / "assets"
    dst = OUT / "assets"
    sourcemap_re = re.compile(rb"\n?//# sourceMappingURL=[^\n]+", re.MULTILINE)
    for src_path in src.rglob("*"):
        if not src_path.is_file():
            continue
        rel = src_path.relative_to(src)
        dst_path = dst / rel
        body = src_path.read_bytes()
        if src_path.suffix == ".js" and src_path.parent.name == "vendor":
            cleaned = sourcemap_re.sub(b"", body)
            if cleaned != body:
                body = cleaned
        atomic_write_bytes(dst_path, body)


def cachebust_value() -> str:
    """A short content-hashed fingerprint over the JS + CSS assets +
    taxonomy. Deterministic across runs with the same inputs."""
    h = hashlib.sha256()
    for p in sorted((SITE / "assets").rglob("*")):
        if p.is_file() and p.suffix in (".js", ".css"):
            h.update(p.relative_to(SITE).as_posix().encode("utf-8"))
            h.update(b"\x00")
            h.update(p.read_bytes())
            h.update(b"\x00")
    tax = SITE / "taxonomy.yaml"
    if tax.exists():
        h.update(tax.read_bytes())
    return h.hexdigest()[:10]


# === SITEMAP / ROBOTS ==================================================

def write_sitemap(urls: list[tuple[str, str]], *, out_path: Path) -> None:
    """`urls` is a list of (loc, lastmod). Emit /sitemap.xml."""
    body = "".join(
        "<url>"
        f"<loc>{_escape(loc)}</loc>"
        + (f"<lastmod>{_escape(lastmod)}</lastmod>" if lastmod else "")
        + "</url>"
        for loc, lastmod in urls
    )
    atomic_write_text(
        out_path,
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + body
        + "</urlset>",
    )


def write_robots(out_path: Path, *, sitemap_url: str) -> None:
    atomic_write_text(
        out_path,
        f"User-agent: *\nAllow: /\nSitemap: {sitemap_url}\n",
    )


# === SELF-CHECK =========================================================

def self_check(
    *,
    manifest: dict[str, Any],
    feed_files: list[Path],
    site_url: str,
) -> list[str]:
    errors: list[str] = []
    # Every page in the manifest exists on disk.
    for url_path, info in manifest.get("pages", {}).items():
        path = OUT / info["path"]
        if not path.exists():
            errors.append(f"manifest page missing on disk: {url_path} -> {info['path']}")
    # Every emitted HTML file contains the Umami snippet exactly once.
    for path in OUT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if text.count("cloud.umami.is/script.js") != 1:
            errors.append(f"umami snippet count != 1 in {path.relative_to(OUT)}")
    # No raw `**Markdown**` survives in any RSS content.
    for fp in feed_files:
        text = fp.read_text(encoding="utf-8")
        if not text:
            continue
        # Strip all CDATA payload comparisons: only inspect content:encoded
        # bodies.
        for m in re.finditer(r"<content:encoded><!\[CDATA\[(.+?)\]\]></content:encoded>", text, re.DOTALL):
            payload = m.group(1)
            # Markdown emphasis tokens that should have rendered to HTML
            if re.search(r"\*\*[^\n*]{1,80}\*\*", payload):
                errors.append(f"feed {fp.name}: unrendered Markdown `**...**` in content:encoded")
                break
            if re.search(r"\[[^\]\n]{1,80}\]\((https?://)", payload):
                errors.append(f"feed {fp.name}: unrendered Markdown `[..](http..)` in content:encoded")
                break
    # All three feeds parse as valid XML.
    for fp in feed_files:
        if fp.exists():
            errs = _xml_validate(fp.read_text(encoding="utf-8"))
            for e in errs:
                errors.append(f"feed {fp.name}: XML parse error — {e}")
    # No UTM parameters in any URL on the site. Scan all emitted HTML and
    # XML files for `?utm_` or `&utm_` (URL-context only — the literal
    # token `utm_` is fine inside prose, e.g. inside docs/analytics.md).
    utm_re = re.compile(r"[?&]utm_[a-z_]+=", re.IGNORECASE)
    for path in list(OUT.rglob("*.html")) + list(OUT.rglob("*.xml")):
        text = path.read_text(encoding="utf-8")
        if utm_re.search(text):
            errors.append(f"UTM parameter present in URL inside {path.relative_to(OUT)}")
            break
    return errors


# === MAIN ==============================================================

def main() -> int:
    if not (ROOT / "briefs").exists():
        print(f"error: no briefs/ directory at {ROOT}", file=sys.stderr)
        return 1

    verify_vendored_hashes()
    taxonomy = parse_taxonomy(SITE / "taxonomy.yaml")

    site_url = os.environ.get("SITE_URL", DEFAULT_SITE_URL).rstrip("/") + "/"

    OUT.mkdir(exist_ok=True)
    # Clear our scratch directory if any prior build left one behind.
    tmp_dir = OUT / ".tmp"
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)

    copy_assets()
    cachebust = cachebust_value()
    atomic_write_bytes(OUT / ".nojekyll", b"")

    briefs = collect_briefs()

    # ---- Validate footer-tagged items against taxonomy ----------------
    # Post-cut-over rule: any item with a footer fails the build if its
    # values aren't in the taxonomy. Pre-cut-over (no footer) is fine.
    fatal_errors: list[str] = []
    for b in briefs:
        for sec in b["sections"]:
            for it in sec["items"]:
                if not it["footer"]:
                    continue
                errs = validate_footer(it["footer"], taxonomy)
                for e in errs:
                    fatal_errors.append(
                        f"taxonomy error in {b['name']}#{it['anchor']}: {e}"
                    )
    if fatal_errors:
        print("TAXONOMY VALIDATION FAILED:", file=sys.stderr)
        for e in fatal_errors:
            print(f"  · {e}", file=sys.stderr)
        return 3

    # ---- Load supporting state ----------------------------------------
    cves_raw = json.loads((ROOT / "state" / "cves_seen.json").read_text())
    topics_raw = json.loads((ROOT / "state" / "covered_items.json").read_text())
    sources_raw = json.loads((ROOT / "sources" / "sources.json").read_text())

    sources = annotate_sources(sources_raw, briefs)
    cves = annotate_cves(cves_raw, briefs, sources)
    topics = annotate_topics(topics_raw, briefs, sources)

    manifest_pages: dict[str, dict[str, Any]] = {}
    sitemap: list[tuple[str, str]] = []  # (loc, lastmod)

    def emit_html(rel_url: str, html: str, *, lastmod: str = "") -> None:
        """`rel_url` looks like 'briefs/2026-05-07/' or '' for home. The
        path on disk becomes `<rel_url>index.html`."""
        rel_path = rel_url + "index.html" if rel_url.endswith("/") or rel_url == "" else rel_url
        if rel_url == "":
            rel_path = "index.html"
        out_path = OUT / rel_path
        atomic_write_text(out_path, html)
        h = hashlib.sha256(html.encode("utf-8")).hexdigest()
        manifest_pages[rel_url or "/"] = {"path": rel_path, "hash": h}
        sitemap.append((site_url + rel_url, lastmod))

    # ---- Per-brief pages ----------------------------------------------
    items_index: dict[str, dict[str, Any]] = {}  # slug -> {item, brief}
    tag_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    region_index: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for b in briefs:
        rel_url = ("briefs/weekly/" if b["kind"] == "weekly" else "briefs/") + b["name"] + "/"
        prefix = "../" * (rel_url.count("/") - 1)  # path back to root
        canonical = site_url + rel_url
        html = render_brief_page(b, site_url=site_url, cachebust=cachebust, prefix=prefix, canonical=canonical)
        emit_html(rel_url, html, lastmod=b["publish_iso"][:10])

        for sec in b["sections"]:
            for it in sec["items"]:
                if not it["footer"]:
                    continue
                slug = it["slug"]
                items_index[slug] = {"item": it, "brief": b}
                for t in it["footer"].get("tags", []):
                    tag_index[t].append({"slug": slug, "title": it["heading"], "brief": b["name"], "publish_ts": b["publish_ts"]})
                for r in it["footer"].get("regions", []):
                    region_index[r].append({"slug": slug, "title": it["heading"], "brief": b["name"], "publish_ts": b["publish_ts"]})

        # Also write the raw .md for any reader that wants it.
        md_dir = OUT / ("briefs/weekly/" if b["kind"] == "weekly" else "briefs/")
        atomic_write_text(md_dir / (b["name"] + ".md"), b["text"])

    # ---- Per-item pages -----------------------------------------------
    for slug, entry in items_index.items():
        rel_url = f"items/{slug}/"
        prefix = "../" * (rel_url.count("/") - 1)
        canonical = site_url + rel_url
        html = render_item_page(
            entry["item"],
            brief=entry["brief"],
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
        )
        emit_html(rel_url, html, lastmod=entry["brief"]["publish_iso"][:10])

    # ---- Per-CVE pages ------------------------------------------------
    for c in cves["cves"]:
        rel_url = f"cves/{c['id']}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_cve_page(c, site_url=site_url, cachebust=cachebust, prefix=prefix, canonical=canonical)
        emit_html(rel_url, html, lastmod=(c.get("last_seen") or "")[:10])

    # ---- Per-source pages ---------------------------------------------
    for s in sources["sources"]:
        rel_url = f"sources/{s['id']}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_source_page(s, site_url=site_url, cachebust=cachebust, prefix=prefix, canonical=canonical)
        emit_html(rel_url, html, lastmod=(s.get("last_successful_fetch") or "")[:10])

    # ---- Per-topic pages ----------------------------------------------
    for t in topics["items"]:
        rel_url = f"topics/{urllib.parse.quote(t['key'], safe='')}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_topic_page(t, site_url=site_url, cachebust=cachebust, prefix=prefix, canonical=canonical)
        emit_html(rel_url, html, lastmod=(t.get("last_covered") or "")[:10])

    # ---- Tag and region indexes ---------------------------------------
    def tag_or_region_page(facet: str, value: str, entries: list[dict[str, Any]]) -> str:
        rel_url = f"{facet}/{value}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        entries.sort(key=lambda e: e["publish_ts"], reverse=True)
        items = [
            (
                e["title"],
                f"{prefix}items/{e['slug']}/",
                f"in {e['brief']}",
            )
            for e in entries
        ]
        return render_index_page(
            title=f"{facet[:-1].capitalize()}: {value}",
            intro=f"All items tagged {value}.",
            items=items,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
            description=f"CTI brief items tagged {value}.",
        )

    for tag, entries in tag_index.items():
        rel_url = f"tags/{tag}/"
        emit_html(rel_url, tag_or_region_page("tags", tag, entries))
    for region, entries in region_index.items():
        rel_url = f"regions/{region}/"
        emit_html(rel_url, tag_or_region_page("regions", region, entries))

    # ---- List pages (briefs, weekly, cves, topics, sources) -----------
    def list_briefs_page(kind: str) -> str:
        rel_url = "briefs/" if kind == "daily" else "briefs/weekly/"
        prefix = "../" * (rel_url.count("/") - 1)
        canonical = site_url + rel_url
        items = [
            (
                b["title"],
                f"{prefix}{rel_url}{b['name']}/",
                f"published {b['publish_iso'][:10]}",
            )
            for b in briefs
            if b["kind"] == kind
        ]
        return render_index_page(
            title="Daily briefs" if kind == "daily" else "Weekly summaries",
            intro="Every brief, newest first." if kind == "daily" else "Weekly consolidating summaries, newest first.",
            items=items,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
            description="Index of CTI briefs.",
        )

    emit_html("briefs/", list_briefs_page("daily"))
    emit_html("briefs/weekly/", list_briefs_page("weekly"))

    def list_facet_page(facet_dir: str, title: str, items: list[tuple[str, str, str]]) -> str:
        rel_url = f"{facet_dir}/"
        prefix = "../"
        canonical = site_url + rel_url
        return render_index_page(
            title=title,
            intro="",
            items=items,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
            description=title,
        )

    emit_html(
        "cves/",
        list_facet_page(
            "cves",
            "CVEs",
            [(c["id"], f"../cves/{c['id']}/", c.get("title", "")[:140]) for c in cves["cves"]],
        ),
    )
    emit_html(
        "topics/",
        list_facet_page(
            "topics",
            "Topics",
            [(t.get("title", t["key"]), f"../topics/{urllib.parse.quote(t['key'], safe='')}/", t.get("type", "")) for t in topics["items"]],
        ),
    )
    emit_html(
        "sources/",
        list_facet_page(
            "sources",
            "Sources",
            [(s.get("publisher", s["id"]), f"../sources/{s['id']}/", ", ".join(s.get("category", []))) for s in sources["sources"]],
        ),
    )

    # ---- Home / about / ops -------------------------------------------
    daily_briefs = [b for b in briefs if b["kind"] == "daily"]
    weekly_briefs = [b for b in briefs if b["kind"] == "weekly"]
    latest = briefs[0] if briefs else None
    home_html = render_home_page(
        latest, daily_briefs, weekly_briefs, site_url=site_url, cachebust=cachebust, canonical=site_url
    )
    emit_html("", home_html, lastmod=latest["publish_iso"][:10] if latest else "")

    # /about/ from README.md + docs index
    readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else "# About"
    emit_html(
        "about/",
        render_static_doc(
            md_text=readme,
            title="About — CTI Briefs",
            description="What this project is, how the briefs are produced, and how to read them.",
            prefix="../",
            canonical=site_url + "about/",
            site_url=site_url,
            cachebust=cachebust,
        ),
    )
    # Mirror the docs/ folder under /about/<doc>/
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        for p in sorted(docs_dir.glob("*.md")):
            rel_url = f"about/{p.stem}/"
            emit_html(
                rel_url,
                render_static_doc(
                    md_text=p.read_text(encoding="utf-8"),
                    title=p.stem.replace("-", " ").title() + " — CTI Briefs",
                    description=p.stem.replace("-", " ").title(),
                    prefix="../../",
                    canonical=site_url + rel_url,
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )
    # Changelog
    changelog = (ROOT / "prompts" / "CHANGELOG.md")
    if changelog.exists():
        emit_html(
            "about/changelog/",
            render_static_doc(
                md_text=changelog.read_text(encoding="utf-8"),
                title="Prompt CHANGELOG — CTI Briefs",
                description="Editorial-policy audit trail.",
                prefix="../../",
                canonical=site_url + "about/changelog/",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )

    # /ops/
    run_log = None
    rl_src = ROOT / "state" / "run_log.json"
    if rl_src.exists():
        try:
            run_log = json.loads(rl_src.read_text())
        except Exception:
            run_log = None
    emit_html(
        "ops/",
        render_ops_page(run_log, prefix="../", site_url=site_url, cachebust=cachebust, canonical=site_url + "ops/"),
    )

    # /404.html
    err = base_template(
        title="404 — CTI Briefs",
        description="Not found",
        body="<section><h1>404 — Not found</h1><p>That page is not on this site. <a href=\"./\">Return home</a>.</p></section>",
        canonical=site_url + "404.html",
        site_url=site_url,
        cachebust=cachebust,
    )
    atomic_write_text(OUT / "404.html", err)

    # ---- RSS feeds ----------------------------------------------------
    daily_xml, daily_recent = build_daily_feed(briefs, site_url=site_url)
    weekly_xml, weekly_recent = build_weekly_feed(briefs, site_url=site_url)
    items_xml, items_recent = build_items_feed(briefs, site_url=site_url)
    atomic_write_text(OUT / "feed.xml", daily_xml)
    atomic_write_text(OUT / "feed-weekly.xml", weekly_xml)
    atomic_write_text(OUT / "feed-items.xml", items_xml)

    # ---- Sitemap / robots ---------------------------------------------
    write_sitemap(sorted(sitemap, key=lambda x: x[0]), out_path=OUT / "sitemap.xml")
    write_robots(OUT / "robots.txt", sitemap_url=site_url + "sitemap.xml")

    # ---- Manifest -----------------------------------------------------
    manifest = {
        "version": 2,
        "site_url": site_url,
        "cachebust": cachebust,
        "feeds": {
            "feed.xml": hashlib.sha256(daily_xml.encode("utf-8")).hexdigest(),
            "feed-weekly.xml": hashlib.sha256(weekly_xml.encode("utf-8")).hexdigest(),
            "feed-items.xml": hashlib.sha256(items_xml.encode("utf-8")).hexdigest(),
        },
        "pages": manifest_pages,
        "counts": {
            "briefs": len(briefs),
            "daily": len(daily_briefs),
            "weekly": len(weekly_briefs),
            "items": len(items_index),
            "cves": len(cves["cves"]),
            "topics": len(topics["items"]),
            "sources": len(sources["sources"]),
            "tags": len(tag_index),
            "regions": len(region_index),
        },
    }
    atomic_write_text(OUT / "data" / "build_manifest.json", json.dumps(manifest, indent=2, sort_keys=True))

    # site.json (deterministic — no now())
    site_meta = {
        "site_url": site_url,
        "cachebust": cachebust,
        "latest_brief": briefs[0]["publish_iso"] if briefs else None,
        "counts": manifest["counts"],
    }
    atomic_write_text(OUT / "data" / "site.json", json.dumps(site_meta, indent=2, sort_keys=True))

    # ---- Prune orphans ------------------------------------------------
    # Only after all writes succeed; a build that fails mid-way leaves the
    # previous live site untouched.
    prune_orphans(OUT)

    # ---- Self-check ---------------------------------------------------
    feed_files = [OUT / "feed.xml", OUT / "feed-weekly.xml", OUT / "feed-items.xml"]
    errors = self_check(manifest=manifest, feed_files=feed_files, site_url=site_url)
    if errors:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  · {e}", file=sys.stderr)
        return 4

    print(
        f"built {OUT} · briefs={manifest['counts']['briefs']} "
        f"items={manifest['counts']['items']} cves={manifest['counts']['cves']} "
        f"sources={manifest['counts']['sources']} topics={manifest['counts']['topics']} "
        f"tags={manifest['counts']['tags']} regions={manifest['counts']['regions']} "
        f"cachebust={cachebust} "
        f"· writes={_WRITE_COUNTER['writes']} skips={_WRITE_COUNTER['skips']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
