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

# Path-segment safety: every value that becomes a URL path segment AND a
# filesystem path segment (CVE id, source id, topic key, brief name, item
# slug) MUST match this regex. The build refuses to emit otherwise — a
# state-file entry like `{"id": "../foo"}` could otherwise traverse out of
# the `_site` output directory and overwrite source files (briefs, prompts,
# state, workflows). State files are agent-written, which means they're
# only as trustworthy as the prompt is uncorrupted; we treat them as
# untrusted at this boundary.
#
# `:` is allowed because the agent uses it as a topic-key qualifier
# (`actor:Lazarus`, `campaign:mini-shai-hulud`, `incident:foo-2026`); it
# is safe in URL path segments (it gets percent-encoded by
# `urllib.parse.quote(safe='')`) and on Linux/macOS filesystems (the
# only deployment targets). The forbidden chars are `/`, `\`, `..`,
# leading `.`, leading `-`, NUL, whitespace, control characters, and
# anything outside alnum + `:` `.` `_` `-`.
_SAFE_ID_RE = re.compile(r"^[A-Za-z0-9:._-]+$")


def is_safe_path_segment(value: str) -> bool:
    """True iff `value` is a non-empty path-segment-safe string with no
    leading `.` / `-` / `:` (so `.`, `..`, `.htaccess`-style and
    `--rf`-style values are rejected)."""
    if not value or value[0] in (".", "-", ":"):
        return False
    if ".." in value:
        return False
    return bool(_SAFE_ID_RE.match(value))


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


# URL-scheme allowlist for rendered <a href> values. Briefs are LLM-generated
# from external sources; a prompt-injected source could plant a Markdown link
# of the form `[click](javascript:...)`, `[click](data:text/html,...)`,
# `[click](vbscript:...)`. The strict CSP delivered by the page would block
# `javascript:` script execution in compliant browsers, but `data:` URIs are
# still permitted by some browsers in `<a href>` and would render attacker
# HTML. Centralised allowlist enforced at every render site.
_ALLOWED_SCHEMES = ("http://", "https://", "mailto:", "tel:")


def _safe_url(url: str) -> str:
    """Return `url` unchanged if its scheme is on the allowlist, an anchor /
    relative path is acceptable too. Otherwise return '#' so the link
    becomes inert (defence-in-depth alongside CSP). Whitespace and control
    characters are stripped — they can be used to obfuscate `javascript:`
    payloads (e.g. `java\\nscript:alert(1)`)."""
    if not url:
        return "#"
    # Strip leading/trailing whitespace and any embedded ASCII control
    # characters (incl. NUL, tab, newline, CR) so an attacker can't smuggle
    # `java\tscript:` through the scheme check.
    stripped = "".join(c for c in url if ord(c) > 0x20 and c not in ("\x7f",)).strip()
    if not stripped:
        return "#"
    lower = stripped.lower()
    # Anchor-only or fragment links are safe.
    if lower.startswith("#") or lower.startswith("?"):
        return stripped
    # Relative path (no scheme). A scheme always has a colon before any '/'
    # or '?' or '#'. Find the first occurrence of any of those.
    first_special = min(
        (i for i in (lower.find(c) for c in (":", "/", "?", "#")) if i >= 0),
        default=-1,
    )
    if first_special < 0 or lower[first_special] != ":":
        # No scheme present — relative URL.
        return stripped
    # A scheme is present; must match the allowlist.
    for s in _ALLOWED_SCHEMES:
        if lower.startswith(s):
            return stripped
    return "#"


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
        # Defence-in-depth URL-scheme allowlist (alongside CSP). A
        # prompt-injected source could plant a `[click](javascript:…)` or
        # `[click](data:text/html,…)` Markdown link in a brief; reject
        # anything outside the allowlist by neutering the href.
        url = _safe_url(url)
        # Recurse on link text for inline formatting (excluding nested
        # links, which Markdown forbids anyway).
        rendered_text = render_inline_no_links(text)
        key = f"\x00LINK{len(placeholders)}\x00"
        # External links (anything starting with http/https/mailto) open in a
        # new tab; in-site relative links stay in the current tab. The reader
        # is consuming a brief and clicking citations to verify them — losing
        # the brief tab on every click is bad UX.
        is_external = url.startswith("http://") or url.startswith("https://") or url.startswith("mailto:")
        target_attr = ' target="_blank"' if is_external else ""
        placeholders[key] = (
            f'<a href="{_escape(url)}"{target_attr} rel="noopener noreferrer">{rendered_text}</a>'
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
    # Step 7: restore placeholders (codes + links) — fixed-point loop so
    # nested markers (e.g. an inline-code span inside a link's label,
    # which got stashed as `\x00CODE0\x00` while the surrounding link
    # was stashed as `\x00LINK1\x00`) get fully expanded.
    for _ in range(8):  # bounded; placeholders are flat by construction
        changed = False
        for key, value in placeholders.items():
            new_s = s.replace(_escape(key), value).replace(key, value)
            if new_s != s:
                s = new_s
                changed = True
        if not changed:
            break
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
    for _ in range(8):
        changed = False
        for key, value in placeholders.items():
            new_s = s.replace(_escape(key), value).replace(key, value)
            if new_s != s:
                s = new_s
                changed = True
        if not changed:
            break
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
    # Match the italic footer line. Source: prefix is no longer required —
    # the TL;DR section emits an aggregate `— *Tags: ... · Region: ...*`
    # tail line that has no Source. We still validate downstream that the
    # parsed result contains at least one recognised footer field, so
    # this regex change does NOT cause arbitrary italic prose to be
    # treated as a footer.
    m = re.match(r"^[—-]\s*\*\s*(?P<body>.+?)\*\s*$", s)
    if not m:
        return None
    body = m.group("body").strip()

    # Sanity gate: the line must contain at least one of the footer field
    # labels somewhere in the body. Otherwise we'd treat any italic line
    # ending in `*` as a footer, which would corrupt prose paragraphs.
    if not re.search(r"\b(?:Sources?|Tags|Region|Sector|Sectors|CVE|CVSS|Vector|Auth|Status|Additional source|Additional sources):", body):
        return None

    # Pull all `[Title](URL)` first; we'll consume them by position.
    links = list(FOOTER_LINK_RE.finditer(body))
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

    # Strip the optional `Source:` / `Sources:` prefix from the first
    # part — historical shape. After this normalisation every part is
    # either a bare link placeholder (additional source) or a typed
    # `Key: value` field.
    parts[0] = re.sub(r"^Sources?:\s*", "", parts[0]).strip()

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

    KNOWN_TYPED_KEYS = {
        "tags", "region", "sector", "sectors", "cve", "cvss",
        "vector", "auth", "status", "additional_source", "additional_sources",
        "source", "sources",
    }

    def _add_source_from_placeholder(ph: str) -> None:
        if ph not in placeholder_map:
            return
        label, url = placeholder_map[ph].split("|||", 1)
        if any(s["url"] == url for s in out["sources"]):
            return
        out["sources"].append({"label": label, "url": url})

    for p in parts:
        # Try `Key: value`.
        key_m = re.match(r"^([A-Za-z][A-Za-z ]*?):\s*(.*)$", p)
        if key_m:
            key = key_m.group(1).strip().lower().replace(" ", "_")
            value = key_m.group(2).strip()
            # Substitute any link placeholders inside value.
            for ph, val in placeholder_map.items():
                if ph in value:
                    lab, url = val.split("|||", 1)
                    value = value.replace(ph, f"[{lab}]({url})")
            if key in KNOWN_TYPED_KEYS:
                if key in ("additional_source", "additional_sources", "source", "sources"):
                    link_m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", value)
                    if link_m and not any(s["url"] == link_m.group(2) for s in out["sources"]):
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
                continue
            # Unknown typed key — fall through and try bare-link extraction.
        # Bare link(s): every link placeholder in this part becomes an
        # additional source. This handles the deep-dive footer shape:
        # `— *Source: [a](u) · [b](u) · [c](u) · Tags: ...*` where a / b /
        # c are all sources (not Additional-source-prefixed).
        for ph in re.findall(r"\x00LINK\d+\x00", p):
            _add_source_from_placeholder(ph)

    # Final gate: require at least ONE recognised footer field after
    # parsing — sources, tags, regions, sectors, cve, status. Without
    # this, a `— *some italic comment*` line could otherwise pass the
    # earlier sanity gate via false matches.
    has_field = bool(
        out["sources"] or out["tags"] or out["regions"]
        or out["sectors"] or out["cve"] or out["status"]
    )
    if not has_field:
        return None

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
    ("updates on previously covered", "updates"),
    ("previously covered items", "updates"),
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


# Skip trailing blanks and Markdown horizontal rules (`---` / `***` /
# `___`) when locating the footer line — sections are separated in the
# prompt by `---` dividers, and that divider falls inside the last
# item's body when the slice runs to the end of the section.
def _is_skippable_trailer(s: str) -> bool:
    t = s.strip()
    if not t:
        return True
    return bool(re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", t))


def _split_trailing_footer(body: str) -> tuple[dict[str, Any] | None, str]:
    """If the trailing line of `body` (after stripping blanks and
    horizontal rules) is a metadata footer, return `(parsed, body
    without footer line)`. Otherwise return `(None, body unchanged)`."""
    lines = body.splitlines()
    while lines and _is_skippable_trailer(lines[-1]):
        lines.pop()
    if not lines:
        return None, body
    fm = parse_footer_line(lines[-1])
    if not fm:
        return None, body
    return fm, "\n".join(lines[:-1]).rstrip()


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

    cls_match = re.search(r"\*\*Classification:\*\*\s*([^\n·]+)", text)
    classification = cls_match.group(1).strip() if cls_match else None

    lang_match = re.search(r"\*\*Language:\*\*\s*([^\n·]+)", text)
    language = lang_match.group(1).strip() if lang_match else None

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

        # Item boundaries within this section. Sections normally use H3
        # per item; § 4 Trending Vulnerabilities in the v2 layout uses H4
        # because the section opens with a CVE summary table at H3-equivalent
        # depth and emits per-CVE detail blocks underneath. We detect H4
        # only when no H3 is present, so a section that mixes both does
        # not lose its H3-level grouping.
        h3_starts: list[tuple[int, str]] = []
        for m3 in re.finditer(r"^### (.+?)\s*$", body_text, re.MULTILINE):
            h3_starts.append((m3.start(), m3.group(1).strip()))
        item_starts = h3_starts
        if not item_starts:
            for m4 in re.finditer(r"^#### (.+?)\s*$", body_text, re.MULTILINE):
                item_starts.append((m4.start(), m4.group(1).strip()))

        items: list[dict[str, Any]] = []
        for j, (s_item, item_heading) in enumerate(item_starts):
            e_item = item_starts[j + 1][0] if j + 1 < len(item_starts) else len(body_text)
            item_md = body_text[s_item:e_item].strip()
            # Strip the leading heading line itself (### or ####).
            first_nl_i = item_md.find("\n")
            item_body = item_md[first_nl_i + 1 :] if first_nl_i >= 0 else ""
            item_body = item_body.strip()
            footer, stripped_body = _split_trailing_footer(item_body)
            items.append(
                {
                    "heading": item_heading,
                    "anchor": slugify(item_heading),
                    "slug": f"{name}-{slugify(item_heading)}"[:80].strip("-"),
                    "body_md": stripped_body,
                    "footer": footer,
                    "section_key": skey,
                }
            )

        # Section-level footer for sections with no items. The v2 prompt
        # places aggregate metadata at the tail of the TL;DR section
        # (`— *Tags: ... · Region: ...*`) and a structured Source/Tags
        # footer at the tail of the Deep Dive section. Both used to
        # render as raw italic Markdown — promote them into the same
        # structured-footer path so the rendered page and the per-item
        # RSS feed see them as first-class metadata.
        section_footer: dict[str, Any] | None = None
        section_body_md = body_text
        if not items:
            section_footer, section_body_md = _split_trailing_footer(body_text)

        sections.append(
            {
                "heading": heading,
                "anchor": anchor,
                "key": skey,
                "items": items,
                "body_md": section_body_md,
                "section_footer": section_footer,
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

    # TL;DR derivation (still used for RSS description + home preview).
    # Matches the H2 heading regardless of the prefix the prompt uses for
    # section numbering (`## 1. TL;DR`, `## § 1 — TL;DR`, `## TL;DR`, etc.)
    # — anything before the literal token `TL;DR` on the heading line is
    # absorbed.
    tldr: list[str] = []
    tldr_block = re.search(r"^##[^\n]*?TL;DR[^\n]*\n(.+?)(?=\n##\s|\Z)", text, re.DOTALL | re.IGNORECASE | re.MULTILINE)
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
        "classification": classification,
        "language": language,
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
#
# The DOM emitted here mirrors the previous SPA's render.js so the
# existing CSS (entity-list, panel, data table, brief-layout, brief-cited,
# cite-list, e-meta, e-tag, badges) renders cleanly. The user-facing
# difference vs. the previous SPA is that all content is now in HTML on
# first paint (no JS-driven rendering, no Markdown fetched-and-parsed
# client-side). JS still handles topbar wiring, search autocomplete,
# list-page filter chips, and the brief-page tag/region/section toggles.

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

GH_ICON_SVG = (
    '<svg class="github-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>'
    '</svg>'
)

THEME_TOGGLE_SVG = (
    '<svg class="theme-icon theme-icon--system" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path d="M3 5h18v11H3z" fill="none" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M9 20h6M12 16v4" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
    '</svg>'
    '<svg class="theme-icon theme-icon--light" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<circle cx="12" cy="12" r="4" fill="currentColor"/>'
    '<g stroke="currentColor" stroke-width="1.6" stroke-linecap="round">'
    '<path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>'
    '</g></svg>'
    '<svg class="theme-icon theme-icon--dark" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
    '<path d="M21 14a8 8 0 1 1-11-11 7 7 0 0 0 11 11z" fill="currentColor"/>'
    '</svg>'
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
    body_class: str = "",
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
    body_attr = f' class="{_escape(body_class)}"' if body_class else ""
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
<!-- Path prefix back to the site root, used by app.js to build URLs. -->
<meta name="cti-site-prefix" content="{pfx}" />
<script defer src="{pfx}assets/js/theme.js?v={cachebust}"></script>
<script defer src="{pfx}assets/js/search.js?v={cachebust}"></script>
<script defer src="{pfx}assets/js/app.js?v={cachebust}"></script>
<script defer src="{pfx}assets/vendor/filter.min.js?v={cachebust}"></script>
{extra_head}
</head>
<body{body_attr}>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar">
  <div class="bar-inner">
    <a class="brand" href="{pfx}" aria-label="Home — CTI Briefs">
      <span class="brand-mark" aria-hidden="true">CTI</span>
      <span class="brand-text"><strong>CTI&nbsp;Briefs</strong><small>Switzerland · Europe · Public sector</small></span>
    </a>

    <form class="searchbox" role="search" data-search-form>
      <label class="visually-hidden" for="q">Search briefs, CVEs, topics, sources</label>
      <input id="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search    /" aria-label="Search" />
      <kbd class="kbd-hint" aria-hidden="true">/</kbd>
      <ul id="suggestions" class="suggestions" role="listbox" hidden></ul>
    </form>

    <a class="github-link" id="github-link" href="https://github.com/{DEFAULT_GITHUB_REPO}" target="_blank" rel="noopener noreferrer" aria-label="GitHub repository" title="View source on GitHub">
      {GH_ICON_SVG}
      <span class="github-stars" id="github-stars" hidden></span>
    </a>

    <button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle colour theme" title="Theme: system">
      {THEME_TOGGLE_SVG}
    </button>

    <button class="nav-toggle" id="nav-toggle" type="button" aria-expanded="false" aria-controls="primary-nav" aria-label="Open navigation menu">
      <span class="nav-toggle-bar" aria-hidden="true"></span>
      <span class="nav-toggle-bar" aria-hidden="true"></span>
      <span class="nav-toggle-bar" aria-hidden="true"></span>
    </button>

    <nav class="nav" id="primary-nav" aria-label="Primary">
      <a href="{pfx}">Home</a>
      <a href="{pfx}briefs/">Briefs</a>
      <a href="{pfx}cves/">CVEs</a>
      <a href="{pfx}topics/">Topics</a>
      <a href="{pfx}sources/">Sources</a>
      <a href="{pfx}ops/">Ops</a>
      <a href="{pfx}about/">About</a>
    </nav>
  </div>
</header>
<main id="main" class="main"><div class="view">{body}</div></main>
<footer class="footer">
  <div class="footer-inner">
    <p>
      <strong>AI-generated content, no human review.</strong>
      Every brief is produced autonomously by an LLM running as a Claude Code routine; every claim links to a primary source. <a href="{pfx}about/">How this works →</a>
    </p>
    <p class="meta" id="footer-meta">
      <a href="{pfx}feed.xml">RSS — daily</a> · <a href="{pfx}feed-weekly.xml">weekly</a> · <a href="{pfx}feed-items.xml">per item</a>
    </p>
  </div>
</footer>
</body>
</html>
"""


# Small inline-pill helpers used inside per-item metadata footers and
# scattered across detail pages.

def render_tag_pill(tag: str, *, prefix: str = "") -> str:
    return f'<a class="pill pill-tag" href="{prefix}tags/{_escape(tag)}/">{_escape(tag)}</a>'


def render_region_pill(region: str, *, prefix: str = "") -> str:
    return f'<a class="pill pill-region" href="{prefix}regions/{_escape(region)}/">{_escape(region)}</a>'


def render_cve_pill(cve: str, *, prefix: str = "") -> str:
    """Render one or more CVE pills.

    The footer's `CVE:` field is a single string that may contain a
    comma-separated list (multi-CVE entries — e.g. an Ivanti EPMM
    auth-bypass + admin-RCE chain reported as one item). Render one
    clickable pill per individual CVE-YYYY-NNNNN id, otherwise the
    pill links to a non-existent slug like `cves/CVE-A, CVE-B/` and
    the reader hits a 404. Anything that does not match the canonical
    CVE shape is rendered as a plain badge (no link)."""
    pieces: list[str] = []
    for raw in cve.split(","):
        token = raw.strip()
        if not token:
            continue
        if re.match(r"^CVE-\d{4}-\d{4,7}$", token):
            pieces.append(
                f'<a class="pill pill-cve" href="{prefix}cves/{_escape(token)}/">{_escape(token)}</a>'
            )
        else:
            pieces.append(f'<span class="pill pill-cve">{_escape(token)}</span>')
    return " ".join(pieces) if pieces else f'<span class="pill pill-cve">{_escape(cve)}</span>'


def reliability_badge(r: str) -> str:
    cls = "badge--high" if r == "HIGH" else ("badge--med" if r == "MEDIUM" else "badge--low")
    return f'<span class="badge {cls}">{_escape(r or "")}</span>'


def status_badge(s: str) -> str:
    if s == "active":
        return '<span class="badge badge--high">active</span>'
    if s == "candidate":
        return '<span class="badge badge--med">candidate</span>'
    if s == "demoted":
        return '<span class="badge badge--low">demoted</span>'
    return f'<span class="badge">{_escape(s or "")}</span>'


def cisa_kev_search_url(cve_id: str) -> str:
    return (
        "https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
        "?search=" + urllib.parse.quote(cve_id)
        + "&field_date_added_wrapper=all&field_cve=&sort_by=field_date_added&items_per_page=20&url="
    )


def render_footer_html(footer: dict[str, Any], *, prefix: str = "", sources_only: bool = False) -> str:
    """Structured HTML rendering of a per-item metadata footer (badge /
    pill blocks instead of raw italic Markdown). Used inside every
    `<article>` on a brief page and inside `<content:encoded>` for the
    items RSS feed.

    When `sources_only=True`, only the Sources line is rendered — Tags,
    Region, CVE, CVSS, Vector, Auth, Status are all suppressed. The RSS
    feeds use this mode so the feed body stays focused on the source
    links and does not duplicate the per-item taxonomy that already
    appears in the structured `<category>` feed metadata.
    """
    parts: list[str] = []

    if footer.get("sources"):
        src_parts = []
        for i, src in enumerate(footer["sources"]):
            label = _escape(src.get("label", ""))
            url = _escape(_safe_url(src.get("url", "")))
            cls = "src-primary" if i == 0 else "src-additional"
            src_parts.append(
                f'<a class="{cls}" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
            )
        parts.append('<span class="meta-sources"><strong>Sources:</strong> ' + " · ".join(src_parts) + "</span>")

    if sources_only:
        return '<aside class="item-footer">' + "".join(parts) + "</aside>"

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


# === BRIEF DETAIL ======================================================

def render_brief_page(
    brief: dict[str, Any],
    *,
    cves_in_brief: list[dict[str, Any]],
    topics_in_brief: list[dict[str, Any]],
    sources_in_brief: list[dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Render a daily / weekly brief page. Layout is two-column on desktop
    (content + aside-toc), single-column on mobile with a collapsible
    on-this-page details element. The body is the brief's Markdown
    rendered server-side; the leading H1 is stripped because the page
    template provides its own."""
    # Strip the leading H1 line (we render our own <h1>).
    raw = brief["text"]
    body_md = re.sub(r"\A# .+\n+", "", raw)

    # Walk parsed sections + items first to gather (a) section list, (b)
    # union of tags + regions across items with v2 metadata footers. These
    # drive the merged page-overview / filter UI on the right.
    section_index: list[tuple[str, str, str]] = []  # (anchor, heading, key)
    all_tags_set: set[str] = set()
    all_regions_set: set[str] = set()
    for sec in brief["sections"]:
        section_index.append((sec["anchor"], sec["heading"], sec["key"]))
        for it in sec["items"]:
            if it["footer"]:
                all_tags_set.update(it["footer"].get("tags", []))
                all_regions_set.update(it["footer"].get("regions", []))

    # Sections list — each entry is BOTH a scroll-anchor link (text)
    # AND a small toggle button (visibility). The text scrolls; the
    # toggle hides/shows the section. Default state: all visible.
    sections_toc = "".join(
        '<li class="toc-row" data-section-row="' + _escape(a) + '">'
        f'<a class="toc-link" href="#{_escape(a)}">{_escape(h)}</a>'
        f'<button type="button" class="toc-toggle" data-section-toggle="{_escape(a)}" '
        f'aria-pressed="true" aria-label="Toggle section visibility" title="Hide / show section">'
        '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
        '<path class="eye-open" d="M8 3.5c-3 0-5.5 2.4-6.5 4.5 1 2.1 3.5 4.5 6.5 4.5s5.5-2.4 6.5-4.5C13.5 5.9 11 3.5 8 3.5zm0 7.2a2.7 2.7 0 1 1 0-5.4 2.7 2.7 0 0 1 0 5.4z" fill="currentColor"/>'
        '<path class="eye-shut" d="M2 3l12 10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
        '</svg>'
        '</button>'
        '</li>'
        for a, h, _k in section_index
    )

    # Tag + region filter groups (collapsed by default for subtlety).
    # Default state: all chips active (everything shown). Click a chip
    # to negate — items carrying that tag/region are then hidden.
    def _filter_chip_row(items: list[str], facet: str) -> str:
        attr = facet[:-1] if facet.endswith("s") else facet
        return "".join(
            f'<button type="button" class="filter-chip" '
            f'data-filter-{attr}="{_escape(v)}" aria-pressed="true" '
            f'title="Toggle {_escape(v)}">{_escape(v)}</button>'
            for v in sorted(items)
        )

    tag_group = (
        '<details class="filter-group" open><summary>Tags <span class="filter-count">'
        f'<span class="muted">({len(all_tags_set)})</span></span></summary>'
        f'<div class="filter-chip-row">{_filter_chip_row(sorted(all_tags_set), "tags")}</div>'
        '</details>'
    ) if all_tags_set else ''
    region_group = (
        '<details class="filter-group" open><summary>Regions <span class="filter-count">'
        f'<span class="muted">({len(all_regions_set)})</span></span></summary>'
        f'<div class="filter-chip-row">{_filter_chip_row(sorted(all_regions_set), "regions")}</div>'
        '</details>'
    ) if all_regions_set else ''

    filter_bar = (
        '<div class="toc-filters">'
        f'{tag_group}{region_group}'
        '<button type="button" class="filter-reset" data-action="clear-filters" hidden>Reset filters</button>'
        '<p class="filter-status" data-role="filter-status" hidden></p>'
        '</div>'
    )

    # Collapsible references block under the TOC.
    refs_block = ""
    if cves_in_brief or topics_in_brief or sources_in_brief:
        cve_lis = "".join(
            f'<li><a href="{prefix}cves/{_escape(c["id"])}/" class="mono">{_escape(c["id"])}</a>'
            + (f' <span class="badge badge--accent" title="Appears in {len(c["appearances"])} briefs">×{len(c["appearances"])}</span>' if len(c.get("appearances", [])) > 1 else '')
            + '</li>'
            for c in cves_in_brief
        )
        topic_lis = "".join(
            f'<li><a href="{prefix}topics/{urllib.parse.quote(t["key"], safe="")}/">{_escape(t.get("title") or t["key"])}</a></li>'
            for t in topics_in_brief
        )
        cited_short = sources_in_brief[:30]
        source_lis = "".join(
            f'<li><a href="{prefix}sources/{urllib.parse.quote(s["id"], safe="")}/">{_escape(s.get("publisher") or s["id"])}</a></li>'
            for s in cited_short
        )
        if len(sources_in_brief) > 30:
            source_lis += f'<li class="muted">+ {len(sources_in_brief) - 30} more sources</li>'
        n_refs = len(cves_in_brief) + len(topics_in_brief) + min(len(sources_in_brief), 30)
        refs_block = (
            f'<details><summary>References ({n_refs})</summary>'
            f'<ul>{cve_lis}{topic_lis}{source_lis}</ul>'
            f'</details>'
        )

    toc_html = (
        '<h3>On this page</h3>'
        f'<ul class="toc-sections">{sections_toc or "<li class=\"muted\">—</li>"}</ul>'
        f'{filter_bar}'
        f'{refs_block}'
    )

    # Cited footer below the brief body.
    cited_footer = ""
    if cves_in_brief or topics_in_brief or sources_in_brief:
        sections = []
        if cves_in_brief:
            cve_items = "".join(
                f'<li><a href="{prefix}cves/{_escape(c["id"])}/" class="mono">{_escape(c["id"])}</a>'
                + (f' <span class="badge badge--accent" title="Appears in {len(c["appearances"])} briefs">×{len(c["appearances"])}</span>' if len(c.get("appearances", [])) > 1 else '')
                + '</li>'
                for c in cves_in_brief
            )
            sections.append(
                f'<section><h3>CVEs in this brief ({len(cves_in_brief)})</h3><ul>{cve_items}</ul></section>'
            )
        if topics_in_brief:
            topic_items = "".join(
                f'<li><a href="{prefix}topics/{urllib.parse.quote(t["key"], safe="")}/">{_escape(t.get("title") or t["key"])}</a>'
                + (f' <span class="badge badge--accent" title="Appears in {len(t.get("briefs", []))} briefs">×{len(t.get("briefs", []))}</span>' if len(t.get("briefs", [])) > 1 else '')
                + '</li>'
                for t in topics_in_brief
            )
            sections.append(
                f'<section><h3>Tracked topics ({len(topics_in_brief)})</h3><ul>{topic_items}</ul></section>'
            )
        if sources_in_brief:
            cited60 = sources_in_brief[:60]
            source_items = "".join(
                f'<li><a href="{prefix}sources/{urllib.parse.quote(s["id"], safe="")}/">{_escape(s.get("publisher") or s["id"])}</a></li>'
                for s in cited60
            )
            if len(sources_in_brief) > 60:
                source_items += f'<li class="muted">+ {len(sources_in_brief) - 60} more</li>'
            sections.append(
                f'<section><h3>Sources cited ({len(sources_in_brief)})</h3><ul>{source_items}</ul></section>'
            )
        cited_footer = '<footer class="brief-cited">' + "".join(sections) + "</footer>"

    prompt_badge = ""
    if brief.get("prompt_version"):
        prompt_badge = (
            f'<a class="badge badge--accent" href="{prefix}about/changelog/" '
            f'title="Editorial-policy version that produced this brief">'
            f'prompt v{_escape(brief["prompt_version"])}'
            f'</a>'
        )

    md_anchor_base = canonical

    # Walk the parsed sections to emit a structured body: every H2 becomes
    # a `<section data-section>`, every H3 a `<article class="brief-item"
    # data-tags data-regions data-section>`. The metadata footer (when
    # present) renders to a structured `<aside class="item-footer">` with
    # tag / region / CVE pills that link to /tags/ and /regions/. Legacy
    # items without a footer still get an article wrapper so the filter UI
    # can hide them via section toggles, but their body renders as plain
    # Markdown without tag pills.
    preamble_md = body_md
    first_h2 = re.search(r"^## ", body_md, re.MULTILINE)
    if first_h2:
        preamble_md = body_md[: first_h2.start()]
    # The metadata line (`**Generated by:** ... · **Classification:** ...`)
    # is already parsed and rendered by the brief-meta strip above the
    # body, plus shown as the prompt-version badge — drop it from the
    # preamble so the same information doesn't appear twice. Same for
    # any standalone `**Audience:**` / `**Prompt:**` lines older briefs
    # may carry.
    preamble_md = re.sub(
        r"^\s*\*\*Generated by:\*\*[^\n]*\n+",
        "",
        preamble_md,
        flags=re.MULTILINE,
    )
    preamble_md = re.sub(
        r"^\s*\*\*(?:Audience|Classification|Language|Prompt):\*\*[^\n]*\n+",
        "",
        preamble_md,
        flags=re.MULTILINE,
    )
    preamble_html = render_markdown(preamble_md, base_url=md_anchor_base) if preamble_md.strip() else ""

    sections_html: list[str] = []
    for sec in brief["sections"]:
        skey = sec["key"]
        sec_anchor = sec["anchor"]
        inner: list[str] = []
        for it in sec["items"]:
            tags_attr = ""
            regions_attr = ""
            if it["footer"]:
                tags_attr = " ".join(it["footer"].get("tags", []))
                regions_attr = " ".join(it["footer"].get("regions", []))
            article_id = it["anchor"]
            slug = it["slug"]
            item_body_html = render_markdown(it["body_md"], base_url=md_anchor_base)
            footer_html = render_footer_html(it["footer"], prefix=prefix) if it["footer"] else ""
            heading_html = (
                f'<h3 id="{_escape(article_id)}">'
                f'<a class="item-link" href="{prefix}items/{_escape(slug)}/">{_escape(it["heading"])}</a>'
                f'</h3>'
                if it["footer"]
                else f'<h3 id="{_escape(article_id)}">{_escape(it["heading"])}</h3>'
            )
            inner.append(
                f'<article class="brief-item" '
                f'data-tags="{_escape(tags_attr)}" '
                f'data-regions="{_escape(regions_attr)}" '
                f'data-section="{_escape(skey)}">'
                f'{heading_html}'
                f'{item_body_html}'
                f'{footer_html}'
                f'</article>'
            )
        if not sec["items"]:
            # No items inside this section — render its raw body
            # Markdown directly. Common for TL;DR (bullets only) and
            # Verification Notes. The footer line, if any, has already
            # been split out by parse_brief and is rendered as a
            # structured pill block below the section body.
            inner.append(render_markdown(sec["body_md"], base_url=md_anchor_base))
            if sec.get("section_footer"):
                inner.append(render_footer_html(sec["section_footer"], prefix=prefix))
        sections_html.append(
            f'<section class="brief-section" '
            f'data-section="{_escape(skey)}" '
            f'id="{_escape(sec_anchor)}">'
            f'<h2><a class="section-anchor" href="#{_escape(sec_anchor)}">{_escape(sec["heading"])}</a></h2>'
            + "".join(inner)
            + '</section>'
        )

    body_html = preamble_html + "".join(sections_html)

    cve_count = len(brief.get("cves", []))
    items_count = brief.get("items", 0)
    raw_path = f"{prefix}briefs/{'weekly/' if brief['kind'] == 'weekly' else ''}{_escape(brief['name'])}.md"

    body = f"""
<h1>{_escape(brief['title'])}</h1>
<article class="brief-layout" data-brief="{_escape(brief['name'])}">
  <div>
    <div class="brief-meta">
      <span><strong>{_escape(brief['kind'])}</strong></span>
      <span class="mono">{_escape(brief['name'])}</span>
      {('<span title="Generated by"><strong>by</strong> ' + _escape(brief['generated_by']) + '</span>') if brief.get('generated_by') else ''}
      {('<span title="Classification" class="meta-tag">' + _escape(brief['classification']) + '</span>') if brief.get('classification') else ''}
      {('<span title="Language">' + _escape(brief['language']) + '</span>') if brief.get('language') else ''}
      {prompt_badge}
      <span>{items_count} item{'' if items_count == 1 else 's'}</span>
      {('<span>' + str(cve_count) + ' CVE' + ('' if cve_count == 1 else 's') + '</span>') if cve_count else ''}
      <span class="meta-actions">
        <button type="button" data-action="share" data-brief="{_escape(brief['name'])}" title="Copy permalink">Copy link</button>
        <a href="{raw_path}" target="_blank" rel="noopener noreferrer" title="View raw Markdown">Raw .md</a>
      </span>
    </div>
    <details class="toc-mobile" data-filter="brief">
      <summary>On this page</summary>
      <div class="toc-mobile-body aside-toc">{toc_html}</div>
    </details>
    <div class="brief-prose">{body_html}</div>
    {cited_footer}
  </div>
  <aside class="aside-toc aside-toc--desktop" aria-label="In this brief" data-filter="brief">
    {toc_html}
  </aside>
</article>
"""
    description = brief.get("summary") or f"{brief['kind'].capitalize()} CTI brief — {brief['title']}"
    return base_template(
        title=brief["title"],
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === SINGLE ITEM (one per metadata-footer block) =======================

def render_item_page(
    item: dict[str, Any],
    *,
    brief: dict[str, Any],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    body_html = render_markdown(item["body_md"], base_url=canonical)
    footer_html = render_footer_html(item["footer"], prefix=prefix) if item["footer"] else ""
    brief_url = f"{prefix}briefs/" + ("weekly/" if brief["kind"] == "weekly" else "") + f"{brief['name']}/"
    description = (item["heading"][:280]) if item.get("heading") else f"Item from {brief['title']}"
    body = f"""
<article class="single-item">
  <p class="subtitle"><a href="{prefix}">Home</a> · <a href="{prefix}briefs/">Briefs</a> · <a href="{_escape(brief_url)}">{_escape(brief['title'])}</a></p>
  <h1>{_escape(item['heading'])}</h1>
  <p class="muted">From <a href="{_escape(brief_url)}#{_escape(item['anchor'])}">{_escape(brief['title'])}</a> · published {_escape(brief['publish_iso'][:10])}</p>
  <div class="brief-prose">{body_html}</div>
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


# === CVE LIST ==========================================================

def render_cve_list_page(
    cves: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    rows = []
    for c in cves:
        appearances = c.get("appearances", [])
        app_links = "".join(
            f'<a href="{prefix}briefs/{_escape(n)}/" class="mono" style="margin-right:0.4rem">{_escape(n)}</a>'
            for n in appearances
        )
        rows.append(
            f'<tr>'
            f'<td class="cve-id"><a href="{prefix}cves/{_escape(c["id"])}/">{_escape(c["id"])}</a></td>'
            f'<td>{_escape(c.get("title", "") or "")}</td>'
            f'<td class="mono muted">{_escape(c.get("first_seen", "") or "")}</td>'
            f'<td class="mono muted">{_escape(c.get("last_seen", "") or "")}</td>'
            f'<td>{app_links}</td>'
            f'</tr>'
        )
    table = (
        '<div class="data-wrap"><table class="data" data-filter-table="cves">'
        '<thead><tr><th>CVE</th><th>Title</th><th>First seen</th><th>Last seen</th><th>Appears in</th></tr></thead>'
        '<tbody>' + "".join(rows) + '</tbody>'
        '</table></div>'
    ) if rows else '<div class="empty">No CVEs match.</div>'

    body = f"""
<h1>CVEs</h1>
<p class="subtitle">{len(cves)} CVE{'' if len(cves) == 1 else 's'} referenced across all briefs. Click an ID for the full appearance trail.</p>
<div class="toolbar">
  <input class="input" id="cves-q" type="search" placeholder="Filter by CVE id, title, or brief date…" autocomplete="off" spellcheck="false" data-filter-input="cves" />
</div>
{table}
"""
    return base_template(
        title="CVEs — CTI Briefs",
        description=f"{len(cves)} CVEs referenced across all briefs.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === SINGLE CVE ========================================================

def render_cve_page(
    cve: dict[str, Any],
    *,
    briefs_index: dict[str, dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    citations = cve.get("citations", []) or []
    primary_host = host_of(cve.get("primary_source_url", "") or "")

    # Group by host so same-publisher rows cluster, primary-source host first.
    grouped: dict[str, list[dict[str, Any]]] = {}
    for cite in citations:
        key = cite.get("host") or cite.get("url") or ""
        grouped.setdefault(key, []).append(cite)
    sorted_hosts = sorted(grouped.keys(), key=lambda h: (h != primary_host, h))

    cite_items: list[str] = []
    for h in sorted_hosts:
        cites_here = grouped[h]
        is_primary = h == primary_host and primary_host
        for c in cites_here:
            briefs_set = sorted({n for n in (c.get("briefs") or [])}, reverse=True)
            brief_links = ", ".join(
                f'<a href="{prefix}briefs/{_escape(n)}/" class="mono">{_escape(n)}</a>'
                for n in briefs_set
            )
            source_id = c.get("source_id")
            cite_url = _safe_url(c.get("url", ""))
            cite_items.append(
                '<li class="cite">'
                f'<a class="cite-link" href="{_escape(cite_url)}" target="_blank" rel="noopener noreferrer" title="Open the article in a new tab">'
                f'<span class="cite-host">{_escape(h)}</span>'
                + ('<span class="badge badge--accent" title="Primary source recorded by the agent">primary</span>' if is_primary else '')
                + f'<span class="cite-label">{_escape(c.get("label") or c.get("url",""))}</span>'
                f'<span class="cite-url muted">{_escape(c.get("url", ""))}</span>'
                '</a>'
                '<div class="cite-meta muted">'
                + (f'<a href="{prefix}sources/{urllib.parse.quote(source_id, safe="")}/" title="Source profile">source profile</a> · ' if source_id else '')
                + 'cited in ' + (brief_links or '<span class="muted">—</span>')
                + '</div>'
                '</li>'
            )

    citations_block = ""
    if cite_items:
        citations_block = (
            f'<h3 style="margin-top:1.2rem">All cited sources for this CVE ({len(citations)})</h3>'
            f'<ul class="cite-list">{"".join(cite_items)}</ul>'
        )

    appearances = cve.get("appearances", []) or []
    if appearances:
        app_lis = []
        for n in appearances:
            b = briefs_index.get(n)
            title = b["title"] if b else n
            meta = ""
            if b:
                meta = f'<div class="e-meta"><span class="e-tag">{_escape(b["kind"])}</span><span>{b.get("items", 0)} items</span></div>'
            app_lis.append(
                f'<li><span><a class="e-title" href="{prefix}briefs/{_escape(n)}/">{_escape(title)}</a>{meta}</span><span class="mono muted">{_escape(n)}</span></li>'
            )
        appearances_block = f'<ul class="entity-list">{"".join(app_lis)}</ul>'
    else:
        appearances_block = '<p class="muted">No briefs reference this CVE yet.</p>'

    body = f"""
<h1 class="mono">{_escape(cve['id'])}</h1>
<p class="subtitle">{_escape(cve.get('title', '') or 'No title recorded.')}</p>

<div class="panel">
  <div class="row" style="justify-content:space-between">
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">First seen</div>
      <div class="mono">{_escape(cve.get('first_seen', '') or '—')}</div>
    </div>
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Last seen</div>
      <div class="mono">{_escape(cve.get('last_seen', '') or '—')}</div>
    </div>
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Appearances</div>
      <div class="mono">{len(appearances)}</div>
    </div>
  </div>

  <h3 style="margin-top:1.2rem">External references</h3>
  <p>
    <a href="https://nvd.nist.gov/vuln/detail/{_escape(cve['id'])}" target="_blank" rel="noopener noreferrer">NVD</a> ·
    <a href="https://www.cve.org/CVERecord?id={_escape(cve['id'])}" target="_blank" rel="noopener noreferrer">cve.org</a> ·
    <a href="{_escape(cisa_kev_search_url(cve['id']))}" target="_blank" rel="noopener noreferrer" title="CISA KEV catalog filtered to this CVE">CISA KEV</a>
  </p>

  {citations_block}
</div>

<h2 class="section-head" style="margin-top:1.5rem">Brief appearances</h2>
{appearances_block}
"""
    return base_template(
        title=f"{cve['id']} — CTI Briefs",
        description=cve.get("title", "") or f"{cve['id']} — appearances across CTI briefs",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === TOPIC LIST + DETAIL ===============================================

def render_topic_list_page(
    topics: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    types = sorted({t.get("type", "") for t in topics if t.get("type")})
    type_chips = "".join(
        f'<span class="chip" data-filter-chip="topic-type" data-value="{_escape(t)}">{_escape(t)}</span>'
        for t in types
    )

    rows = []
    for t in topics:
        n = len(t.get("briefs", []))
        flag_badges = "".join(
            f'<span class="badge badge--low" title="Verification flag">{_escape(f)}</span>'
            for f in t.get("flags", [])
        )
        brief_links = "".join(
            f'<a href="{prefix}briefs/{_escape(b)}/" class="mono" style="margin-left:0.35rem">{_escape(b)}</a>'
            for b in (t.get("briefs", []) or [])[:5]
        )
        rows.append(
            '<li data-topic-type="' + _escape(t.get("type", "")) + '" data-topic-flags="' + _escape(",".join(t.get("flags", []))) + '">'
            f'<span>'
            f'<a class="e-title" href="{prefix}topics/{urllib.parse.quote(t["key"], safe="")}/">{_escape(t.get("title") or t["key"])}</a>'
            f'<div class="e-meta">'
            f'<span class="e-tag">{_escape(t.get("type", "") or "—")}</span>'
            f'<span class="mono">{_escape(t["key"])}</span>'
            f'<span>last covered {_escape(t.get("last_covered", "") or "—")}</span>'
            + (f'<span class="badge badge--accent" title="Story unfolds across {n} briefs">×{n} appearances</span>' if n > 1 else '')
            + flag_badges
            + '</div></span>'
            f'<span>{brief_links}</span>'
            '</li>'
        )

    list_html = (
        '<ul class="entity-list" data-filter-list="topics">' + "".join(rows) + '</ul>'
    ) if rows else '<div class="empty">No topics match.</div>'

    body = f"""
<h1>Topics</h1>
<p class="subtitle">CVEs, actors, campaigns, incidents, tools, and annual reports tracked across briefs. The badge marks items covered in more than one brief — these are the "stories that unfolded".</p>

<div class="toolbar">
  <input class="input" id="topics-q" type="search" placeholder="Filter topics…" autocomplete="off" spellcheck="false" data-filter-input="topics" />
  <span class="chip active" data-filter-chip="topic-type" data-value="all">All types</span>
  {type_chips}
</div>
<div class="toolbar" style="margin-top:-0.5rem">
  <span class="chip active" data-filter-chip="topic-flag" data-value="all">All verification</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="multi" title="Items where two-source verification held">Corroborated</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE">Single-source (any)</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE-NATIONAL-CERT">National-CERT only</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE-OTHER">Other single-source</span>
</div>

{list_html}
"""
    return base_template(
        title="Topics — CTI Briefs",
        description=f"{len(topics)} tracked topics — CVEs, actors, campaigns, incidents, tools.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_topic_page(
    topic: dict[str, Any],
    *,
    briefs_index: dict[str, dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    apps = sorted(topic.get("appearances", []) or [], key=lambda a: a.get("date") or "", reverse=True)
    citations = topic.get("citations", []) or []

    # Citation rendering — same DOM as the CVE page.
    primary_host = host_of(topic.get("primary_source_url", "") or "")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for cite in citations:
        key = cite.get("host") or cite.get("url") or ""
        grouped.setdefault(key, []).append(cite)
    sorted_hosts = sorted(grouped.keys(), key=lambda h: (h != primary_host, h))
    cite_items = []
    for h in sorted_hosts:
        is_primary = h == primary_host and primary_host
        for c in grouped[h]:
            briefs_set = sorted({n for n in (c.get("briefs") or [])}, reverse=True)
            brief_links = ", ".join(
                f'<a href="{prefix}briefs/{_escape(n)}/" class="mono">{_escape(n)}</a>'
                for n in briefs_set
            )
            source_id = c.get("source_id")
            cite_url = _safe_url(c.get("url", ""))
            cite_items.append(
                '<li class="cite">'
                f'<a class="cite-link" href="{_escape(cite_url)}" target="_blank" rel="noopener noreferrer">'
                f'<span class="cite-host">{_escape(h)}</span>'
                + ('<span class="badge badge--accent" title="Primary source recorded by the agent">primary</span>' if is_primary else '')
                + f'<span class="cite-label">{_escape(c.get("label") or c.get("url",""))}</span>'
                f'<span class="cite-url muted">{_escape(c.get("url", ""))}</span>'
                '</a>'
                '<div class="cite-meta muted">'
                + (f'<a href="{prefix}sources/{urllib.parse.quote(source_id, safe="")}/">source profile</a> · ' if source_id else '')
                + 'cited in ' + (brief_links or '<span class="muted">—</span>')
                + '</div>'
                '</li>'
            )
    citations_block = ""
    if cite_items:
        citations_block = (
            f'<h3 style="margin-top:1.2rem">All cited sources for this topic ({len(citations)})</h3>'
            f'<ul class="cite-list">{"".join(cite_items)}</ul>'
        )

    timeline_lis = []
    for a in apps:
        bp = a.get("brief_path", "")
        m = re.search(r"(\d{4}-\d{2}-\d{2}|\d{4}-W\d{2})", bp)
        name = m.group(1) if m else ""
        b = briefs_index.get(name)
        b_title = b["title"] if b else (name or "?")
        timeline_lis.append(
            '<li><span>'
            f'<span class="mono" style="margin-right:0.6rem">{_escape(a.get("date", "") or name)}</span>'
            f'<a href="{prefix}briefs/{_escape(name)}/">{_escape(b_title)}</a>'
            '<div class="e-meta" style="margin-top:0.2rem">'
            f'<span class="e-tag">{_escape(a.get("section", "") or "—")}</span>'
            + (f'<span class="muted">{_escape(a["delta_summary"])}</span>' if a.get("delta_summary") else '')
            + '</div></span></li>'
        )
    timeline_block = (
        f'<ol class="entity-list" style="list-style:none">{"".join(timeline_lis)}</ol>'
    ) if timeline_lis else '<p class="muted">No recorded appearances.</p>'

    body = f"""
<h1>{_escape(topic.get('title') or topic['key'])}</h1>
<p class="subtitle"><span class="badge badge--accent">{_escape(topic.get('type', '') or '—')}</span> · <span class="mono">{_escape(topic['key'])}</span></p>

<div class="panel">
  <div class="row" style="justify-content:space-between">
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">First covered</div>
      <div class="mono">{_escape(topic.get('first_covered', '') or '—')}</div>
    </div>
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Last covered</div>
      <div class="mono">{_escape(topic.get('last_covered', '') or '—')}</div>
    </div>
    <div>
      <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Appearances</div>
      <div class="mono">{len(apps)}</div>
    </div>
  </div>
  {citations_block}
</div>

<h2 class="section-head" style="margin-top:1.5rem">Story timeline</h2>
{timeline_block}
"""
    return base_template(
        title=f"{topic.get('title') or topic['key']} — Topic",
        description=topic.get("title") or topic["key"],
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === SOURCE LIST + DETAIL ==============================================

def render_source_list_page(
    sources: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    cats = sorted({c for s in sources for c in (s.get("category") or [])})
    stats = sorted({s.get("status") or "" for s in sources if s.get("status")})

    cat_chips = "".join(
        f'<span class="chip" data-filter-chip="source-cat" data-value="{_escape(c)}">{_escape(c)}</span>'
        for c in cats
    )
    status_chips = "".join(
        f'<span class="chip" data-filter-chip="source-status" data-value="{_escape(s)}">{_escape(s)}</span>'
        for s in stats
    )

    rows = []
    for s in sources:
        appearances = s.get("appearances", []) or []
        app_links = "".join(
            f'<a href="{prefix}briefs/{_escape(n)}/" class="mono" style="margin-right:0.3rem">{_escape(n)}</a>'
            for n in appearances[:6]
        )
        if len(appearances) > 6:
            app_links += f' <span class="muted">+{len(appearances) - 6}</span>'
        cat_tags = "".join(
            f'<span class="e-tag">{_escape(c)}</span>'
            for c in (s.get("category") or [])
        )
        rows.append(
            f'<tr data-source-cats="{_escape(",".join(s.get("category") or []))}" '
            f'data-source-status="{_escape(s.get("status") or "")}">'
            f'<td>'
            f'<a href="{prefix}sources/{urllib.parse.quote(s["id"], safe="")}/"><strong>{_escape(s.get("publisher") or s["id"])}</strong></a>'
            f'<div class="muted mono" style="font-size:0.75rem">{_escape(s["id"])}</div>'
            '</td>'
            f'<td>{reliability_badge(s.get("reliability") or "")}</td>'
            f'<td>{status_badge(s.get("status") or "")}</td>'
            f'<td><div class="e-meta">{cat_tags}</div></td>'
            f'<td>{app_links}</td>'
            '</tr>'
        )

    table = (
        '<div class="data-wrap"><table class="data" data-filter-table="sources">'
        '<thead><tr><th>Publisher</th><th>Reliability</th><th>Status</th><th>Categories</th><th>Cited in</th></tr></thead>'
        '<tbody>' + "".join(rows) + '</tbody>'
        '</table></div>'
    ) if rows else '<div class="empty">No sources match.</div>'

    body = f"""
<h1>Sources</h1>
<p class="subtitle">{len(sources)} curated source{'' if len(sources) == 1 else 's'}. Each source can be searched and shows the briefs that have cited it.</p>

<div class="toolbar">
  <input class="input" id="sources-q" type="search" placeholder="Filter by name, id, notes, URL…" autocomplete="off" spellcheck="false" data-filter-input="sources" />
  <span class="chip active" data-filter-chip="source-cat" data-value="all">All categories</span>
  {cat_chips}
</div>
<div class="toolbar" style="margin-top:-0.5rem">
  <span class="chip active" data-filter-chip="source-status" data-value="all">All statuses</span>
  {status_chips}
</div>

{table}
"""
    return base_template(
        title="Sources — CTI Briefs",
        description=f"{len(sources)} curated CTI sources.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_source_page(
    source: dict[str, Any],
    *,
    briefs_index: dict[str, dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    cats = source.get("category", []) or []
    langs = source.get("language", []) or []
    fetch_failures = source.get("consecutive_fetch_failures")
    quiet_periods = source.get("consecutive_quiet_periods")

    e_tags: list[str] = []
    for c in cats:
        e_tags.append(f'<span class="e-tag">{_escape(c)}</span>')
    for l in langs:
        e_tags.append(f'<span class="e-tag">lang: {_escape(l)}</span>')
    if isinstance(fetch_failures, int):
        e_tags.append(f'<span class="e-tag">fetch failures: {fetch_failures}</span>')
    elif isinstance(source.get("consecutive_failures"), int):
        e_tags.append(f'<span class="e-tag">failures: {source["consecutive_failures"]}</span>')
    if isinstance(quiet_periods, int):
        e_tags.append(f'<span class="e-tag">quiet periods: {quiet_periods}</span>')
    e_tags.append(
        f'<span class="e-tag">last fetch: {_escape(source.get("last_successful_fetch") or "never")}</span>'
    )

    notes_html = ""
    if source.get("notes"):
        notes_html = f'<p class="muted" style="margin-top:0.7rem">{_escape(source["notes"])}</p>'

    appearances = source.get("appearances", []) or []
    if appearances:
        app_lis = []
        for n in appearances:
            b = briefs_index.get(n)
            title = b["title"] if b else n
            meta = ""
            if b:
                meta = f'<div class="e-meta"><span class="e-tag">{_escape(b["kind"])}</span><span>{b.get("items", 0)} items</span></div>'
            app_lis.append(
                f'<li><span><a class="e-title" href="{prefix}briefs/{_escape(n)}/">{_escape(title)}</a>{meta}</span><span class="mono muted">{_escape(n)}</span></li>'
            )
        appearances_block = f'<ul class="entity-list">{"".join(app_lis)}</ul>'
    else:
        appearances_block = '<p class="muted">Not cited in any brief yet.</p>'

    body = f"""
<h1>{_escape(source.get('publisher') or source['id'])}</h1>
<p class="subtitle"><span class="mono">{_escape(source['id'])}</span> · {reliability_badge(source.get('reliability') or '')} · {status_badge(source.get('status') or '')}</p>

<div class="panel">
  <p><a href="{_escape(_safe_url(source.get('url', '') or ''))}" target="_blank" rel="noopener noreferrer">{_escape(source.get('url', '') or '')}</a></p>
  <div class="e-meta" style="margin-top:0.4rem">
    {''.join(e_tags)}
  </div>
  {notes_html}
</div>

<h2 class="section-head" style="margin-top:1.5rem">Cited in {len(appearances)} brief{'' if len(appearances) == 1 else 's'}</h2>
{appearances_block}
"""
    return base_template(
        title=f"{source.get('publisher') or source['id']} — Source",
        description=f"{source.get('publisher') or source['id']} — {', '.join(cats) or 'curated CTI source'}",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === BRIEFS LIST =======================================================

def render_briefs_list_page(
    briefs: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Briefs index: filter chips by kind, optional search filter, grouped
    by month."""
    # Group by month (daily) or "Weekly summaries" (weekly).
    groups: dict[str, dict[str, Any]] = {}
    for b in briefs:
        if b["kind"] == "weekly":
            key, label = "weekly", "Weekly summaries"
        else:
            key = b["name"][:7]
            try:
                dt = datetime.strptime(b["name"], "%Y-%m-%d")
                label = dt.strftime("%B %Y")
            except ValueError:
                label = key
        groups.setdefault(key, {"key": key, "label": label, "items": []})["items"].append(b)

    section_html: list[str] = []
    for grp in groups.values():
        items_html = "".join(
            '<li data-brief-kind="' + _escape(b["kind"]) + '" '
            f'data-brief-haystack="{_escape((b["title"] + " " + b["name"] + " " + " ".join(b.get("tldr", [])) + " " + " ".join(b.get("cves", []))).lower())}">'
            '<span>'
            f'<a class="e-title" href="{prefix}briefs/{_escape("weekly/" if b["kind"] == "weekly" else "")}{_escape(b["name"])}/">{_escape(b["title"])}</a>'
            '<div class="e-meta">'
            f'<span class="e-tag">{_escape(b["kind"])}</span>'
            f'<span>{b.get("items", 0)} item{"" if b.get("items", 0) == 1 else "s"}</span>'
            + (f'<span>{len(b.get("cves", []))} CVE{"" if len(b.get("cves", [])) == 1 else "s"}</span>' if b.get("cves") else '')
            + (f'<span>{len(b.get("tldr", []))} TL;DR bullet{"" if len(b.get("tldr", [])) == 1 else "s"}</span>' if b.get("tldr") else '')
            + '</div>'
            '</span>'
            f'<span class="mono muted">{_escape(b["name"])}</span>'
            '</li>'
            for b in grp["items"]
        )
        section_html.append(
            f'<section style="margin-top:1.4rem"><h2 class="section-head">{_escape(grp["label"])}</h2>'
            f'<ul class="entity-list" data-filter-list="briefs">{items_html}</ul>'
            f'</section>'
        )

    body = f"""
<h1>Briefs</h1>
<p class="subtitle">{len(briefs)} brief{'' if len(briefs) == 1 else 's'}, newest first. Each brief is a Markdown file under <code>briefs/</code>; click through for the full text.</p>

<div class="toolbar">
  <input class="input" id="briefs-q" type="search" placeholder="Filter by title, CVE, or TL;DR…" autocomplete="off" spellcheck="false" data-filter-input="briefs" />
  <span class="chip active" data-filter-chip="brief-kind" data-value="all">All</span>
  <span class="chip" data-filter-chip="brief-kind" data-value="daily">Daily</span>
  <span class="chip" data-filter-chip="brief-kind" data-value="weekly">Weekly</span>
  <a class="chip" href="{prefix}feed.xml" target="_blank" rel="noopener noreferrer" title="Daily RSS feed">RSS · daily</a>
  <a class="chip" href="{prefix}feed-weekly.xml" target="_blank" rel="noopener noreferrer" title="Weekly RSS feed">RSS · weekly</a>
  <a class="chip" href="{prefix}feed-items.xml" target="_blank" rel="noopener noreferrer" title="Per-item RSS feed">RSS · per item</a>
</div>
{''.join(section_html) or '<div class="empty">No briefs published yet.</div>'}
"""
    return base_template(
        title="Briefs — CTI Briefs",
        description=f"{len(briefs)} CTI briefs published, newest first.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === GENERIC INDEX (used for tag and region indexes) ==================

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
    rows = "".join(
        '<li>'
        f'<span>'
        f'<a class="e-title" href="{_escape(href)}">{_escape(label)}</a>'
        + (f'<div class="e-meta"><span class="muted">{_escape(hint)}</span></div>' if hint else '')
        + '</span>'
        '</li>'
        for label, href, hint in items
    )
    body = f"""
<h1>{_escape(title)}</h1>
{('<p class="subtitle">' + _escape(intro) + '</p>') if intro else ''}
{('<ul class="entity-list">' + rows + '</ul>') if rows else '<div class="empty">No items.</div>'}
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


# === HOME ==============================================================

def render_home_page(
    latest: dict[str, Any] | None,
    recent_daily: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    canonical: str,
) -> str:
    """Decluttered home: a hero (project name + lede), today's brief
    (title + date + TL;DR + ONE CTA), and a list of recent daily briefs.
    No banner gradient, no "Continue exploring" stat grid, no inline
    build timestamp. Per-section single link to the latest brief — the
    title isn't itself a link; the CTA below is the click target.
    RSS feeds live in the global footer."""
    # Bootstrap that converts old SPA hash URLs (`#/briefs/<name>`) to
    # clean URLs. Loaded as an external script so the strict CSP can keep
    # `'self'` and refuse all inline scripts.
    redirect_js = (
        f'<script src="assets/js/spa-redirect.js?v={cachebust}"></script>'
    )

    if not latest:
        body = f"""
<section class="home-hero">
  <h1>CTI Briefs</h1>
  <p class="lede">Daily and weekly cyber threat intelligence — Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.</p>
</section>
<section class="home-empty">
  <p>The first daily routine run will publish a brief here.</p>
  <p><a href="about/">About this newsletter →</a></p>
</section>
{redirect_js}
"""
        return base_template(
            title="CTI Briefs — Switzerland, Europe & Public Sector",
            description="Daily and weekly cyber threat intelligence briefs covering Switzerland, Europe, and the public sector.",
            body=body,
            canonical=canonical,
            site_url=site_url,
            cachebust=cachebust,
            home_relative_prefix="",
        )

    tldr_lis = "".join(
        f'<li>{render_inline(t, base_url=canonical)}</li>'
        for t in (latest.get("tldr") or [])[:5]
    )
    tldr_html = (
        f'<ul>{tldr_lis}</ul>' if tldr_lis else '<p class="muted">No TL;DR bullets in this brief.</p>'
    )

    # Recent briefs list — exclude today's brief from the list to avoid
    # a second link to it (the user asked for one link per section to
    # the brief of today). Show the next ~10 daily briefs.
    recent_lis = "".join(
        f'<li>'
        f'<a href="briefs/{_escape(b["name"])}/">{_escape(b["title"])}</a> '
        f'<span class="muted mono">{_escape(b["publish_iso"][:10])}</span>'
        f'</li>'
        for b in recent_daily[1:11]
    )
    recent_section = (
        '<section class="home-recent">'
        '<h3>Recent daily briefs</h3>'
        f'<ul class="home-recent-list">{recent_lis}</ul>'
        '</section>'
    ) if recent_lis else ''

    body = f"""
<section class="home-hero">
  <h1>CTI Briefs</h1>
  <p class="lede">Daily and weekly cyber threat intelligence — Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.</p>
</section>

<section class="home-today">
  <h2>{_escape(latest['title'])}</h2>
  <p class="muted">Published {_escape(latest['publish_iso'][:10])}</p>
  {tldr_html}
  <p class="home-today-cta"><a class="cta" href="briefs/{_escape(latest['name'])}/">Read the full brief →</a></p>
</section>

{recent_section}
{redirect_js}
"""
    return base_template(
        title="CTI Briefs — Switzerland, Europe & Public Sector",
        description="Daily and weekly cyber threat intelligence (CTI) briefs covering Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix="",
    )


# === STATIC DOC (about / docs / changelog) =============================

_ABOUT_LINK_RE = re.compile(
    r'<a\s+href="([^"#?][^"]*)"',
    re.IGNORECASE,
)


def _rewrite_about_links(html: str, *, prefix: str) -> str:
    """Rewrite relative repo paths in rendered Markdown to URLs that
    actually resolve on the deployed static site.

    Inputs are README.md / docs/*.md / prompts/CHANGELOG.md, all of which
    use relative links like `[`docs/verification.md`](docs/verification.md)`
    or `[briefs](briefs/)`. Those resolve correctly on github.com but
    404 on the deployed Pages site (everything is rendered into
    /about/<doc>/, not /about/docs/<doc>.md).

    Mapping rules:
        docs/<name>.md            → <prefix>about/<name>/
        docs/                     → <prefix>about/
        briefs/                   → <prefix>briefs/
        briefs/<name>.md          → <prefix>briefs/<name>/   (only daily / weekly)
        briefs/weekly/<name>.md   → <prefix>briefs/weekly/<name>/
        prompts/CHANGELOG.md      → <prefix>about/changelog/
        anything else relative    → https://github.com/<repo>/blob/main/<path>
                                    (state files, source list, scripts, etc.)
    """
    repo = os.environ.get("GITHUB_REPO", DEFAULT_GITHUB_REPO)
    repo_blob = f"https://github.com/{repo}/blob/main/"

    def remap(path: str) -> str:
        # Drop a leading `./` if the author wrote one.
        p = path[2:] if path.startswith("./") else path
        # Strip optional fragment / query so we can route by extension.
        frag = ""
        if "#" in p:
            p, frag = p.split("#", 1)
            frag = "#" + frag
        # docs/<name>.md → about/<name>/
        m = re.match(r"^docs/([^/]+)\.md$", p)
        if m:
            return prefix + f"about/{m.group(1)}/" + frag
        # docs/ index → about/ (the README is at /about/)
        if p == "docs/" or p == "docs":
            return prefix + "about/" + frag
        # prompts/CHANGELOG.md → about/changelog/
        if p == "prompts/CHANGELOG.md":
            return prefix + "about/changelog/" + frag
        # briefs/<YYYY-MM-DD>.md → briefs/<YYYY-MM-DD>/
        m = re.match(r"^briefs/(\d{4}-\d{2}-\d{2})\.md$", p)
        if m:
            return prefix + f"briefs/{m.group(1)}/" + frag
        # briefs/weekly/<YYYY-Www>.md → briefs/weekly/<YYYY-Www>/
        m = re.match(r"^briefs/weekly/(\d{4}-W\d{2})\.md$", p)
        if m:
            return prefix + f"briefs/weekly/{m.group(1)}/" + frag
        if p == "briefs/" or p == "briefs":
            return prefix + "briefs/" + frag
        # Everything else (state/, sources/, tools/, scripts/, .github/) —
        # link to the file on GitHub at HEAD of `main`.
        return repo_blob + p + frag

    def sub(m: re.Match) -> str:
        new = remap(m.group(1))
        # If the rewritten URL is external (e.g. relative paths the agent
        # typed in docs/*.md got remapped to github.com/.../blob/main/...),
        # add target="_blank" so it opens in a new tab. The original render
        # pass only set target on hrefs that were already external before
        # the rewrite.
        is_external = new.startswith("http://") or new.startswith("https://") or new.startswith("mailto:")
        attrs = f'href="{_escape(new)}"'
        if is_external:
            attrs += ' target="_blank"'
        return f'<a {attrs}'

    return _ABOUT_LINK_RE.sub(sub, html)


def render_static_doc(
    *, md_text: str, title: str, description: str, prefix: str, canonical: str,
    site_url: str, cachebust: str, subtitle: str | None = None,
) -> str:
    # No base_url here — we want relative repo paths like
    # `docs/verification.md` to stay relative so _rewrite_about_links
    # can route them to /about/verification/ instead of letting urljoin
    # resolve them against the canonical URL (which would 404).
    rendered = render_markdown(md_text)
    rendered = _rewrite_about_links(rendered, prefix=prefix)
    body = f"""
<article class="static-doc">
  {('<p class="subtitle">' + _escape(subtitle) + '</p>') if subtitle else ''}
  <div class="brief-prose">{rendered}</div>
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


# === OPS DASHBOARD =====================================================

def render_ops_page(
    run_log: dict[str, Any] | None,
    sources: list[dict[str, Any]] | None,
    *,
    prefix: str,
    site_url: str,
    cachebust: str,
    canonical: str,
) -> str:
    runs = list(reversed((run_log or {}).get("runs") or []))[:30]

    # Stale active sources (>7 days since last_successful_fetch).
    today = datetime.now(timezone.utc).date()
    stale: list[dict[str, Any]] = []
    for s in sources or []:
        if s.get("status") != "active":
            continue
        lf = s.get("last_successful_fetch")
        if not lf or not re.match(r"^\d{4}-\d{2}-\d{2}$", lf):
            stale.append({"id": s["id"], "publisher": s.get("publisher", s["id"]), "days": -1, "last": lf or ""})
            continue
        try:
            dt = datetime.strptime(lf, "%Y-%m-%d").date()
            days = (today - dt).days
            if days > 7:
                stale.append({"id": s["id"], "publisher": s.get("publisher", s["id"]), "days": days, "last": lf})
        except ValueError:
            stale.append({"id": s["id"], "publisher": s.get("publisher", s["id"]), "days": -1, "last": lf})
    stale.sort(key=lambda x: -x["days"] if x["days"] >= 0 else 1 << 30, reverse=True)

    if runs:
        run_rows = []
        for r in runs:
            sa = r.get("sub_agents") or {}

            def fmt(k: str) -> str:
                a = sa.get(k)
                if not a:
                    return '<span class="muted">—</span>'
                if a.get("returned") is False:
                    return '<span class="badge badge--low">stalled</span>'
                used = len(a.get("sources_used") or [])
                attempted = len(a.get("sources_attempted") or [])
                items = a.get("items_returned") or 0
                return f'{items} <span class="muted">({used}/{attempted} src)</span>'

            failures = len(r.get("fetch_failures") or [])
            failures_html = (
                f'<span class="badge badge--med">{failures}</span>'
                if failures
                else '<span class="muted">0</span>'
            )
            run_rows.append(
                '<tr>'
                f'<td class="mono"><a href="{prefix}briefs/{_escape(r.get("date", ""))}/">{_escape(r.get("date", ""))}</a></td>'
                f'<td class="mono muted">{_escape(r.get("model", "") or "")}</td>'
                f'<td>{fmt("S1")}</td>'
                f'<td>{fmt("S2")}</td>'
                f'<td>{fmt("S3")}</td>'
                f'<td>{fmt("S4")}</td>'
                f'<td>{failures_html}</td>'
                f'<td>{_escape(str(r.get("items_published", "") or ""))}</td>'
                f'<td class="mono muted">{_escape(r.get("deep_dive") or "—")}</td>'
                '</tr>'
            )
        runs_html = (
            '<div class="data-wrap"><table class="data">'
            '<thead><tr><th>Date</th><th>Model</th><th>S1</th><th>S2</th><th>S3</th><th>S4</th><th>Failures</th><th>Items</th><th>Deep dive</th></tr></thead>'
            '<tbody>' + "".join(run_rows) + '</tbody>'
            '</table></div>'
        )
    else:
        runs_html = (
            '<div class="empty">'
            '<p>No <code>state/run_log.json</code> yet.</p>'
            '<p class="muted">The agent populates this file at the end of every run (Phase 5). The first scheduled run after the v2 prompt change will create it.</p>'
            '</div>'
        )

    if stale:
        stale_lis = "".join(
            '<li><span>'
            f'<a class="e-title" href="{prefix}sources/{urllib.parse.quote(s["id"], safe="")}/">{_escape(s["publisher"])}</a>'
            '<div class="e-meta">'
            f'<span class="e-tag">{("never fetched" if s["days"] < 0 else (str(s["days"]) + " days"))}</span>'
            + (f'<span class="muted">last: {_escape(s["last"])}</span>' if s.get("last") else '')
            + '</div></span>'
            f'<span class="mono muted">{_escape(s["id"])}</span></li>'
            for s in stale
        )
        stale_html = f'<ul class="entity-list">{stale_lis}</ul>'
    else:
        stale_html = '<p class="muted">No active source has been silent for more than a week.</p>'

    body = f"""
<h1>Operations</h1>
<p class="subtitle">Run log and source-rotation health. Sourced from <code>state/run_log.json</code> (per-run sub-agent allocation) and <code>sources/sources.json</code> (last-successful-fetch timestamps).</p>

<h2 class="section-head">Recent runs</h2>
{runs_html}

<h2 class="section-head" style="margin-top:1.8rem">Stale active sources (&gt;7 days since last successful fetch)</h2>
{stale_html}

<p class="muted" style="font-size:0.78rem; margin-top:1rem">
  See <a href="{prefix}about/architecture/">Architecture</a> for how the run log is produced.
</p>
"""
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

def _cdata_safe(s: str) -> str:
    """Make `s` safe to embed inside `<![CDATA[ … ]]>`. The current
    Markdown renderer always HTML-escapes `>` (so `]]>` never appears
    organically in rendered output), but defence-in-depth: split a literal
    `]]>` across two CDATA sections so a future renderer change cannot
    silently allow a CDATA-break injection that would let attacker XML
    leak into the RSS feed body."""
    return s.replace("]]>", "]]]]><![CDATA[>")


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


_FOOTER_META_KEY_RE = re.compile(
    r"\s+·\s+(?:Tags|Region|Sector|Sectors|CVE|CVSS|Vector|Auth|Status):"
)


def _strip_footer_metadata_in_md(body_md: str) -> str:
    """Inside any italic metadata-footer line (`— *Source: ...*` or
    `— *Tags: ...*`), drop every field other than Source / Sources /
    Additional source(s). Used for RSS body rendering so feed bodies
    only show the source links — Tags / Region / CVE / CVSS / Vector /
    Auth / Status appear as `<category>` feed metadata instead.

    A footer line is recognised by the same shape `parse_footer_line`
    accepts: starts with `— *` (em-dash + space + asterisk) or `- *`,
    ends with `*`, and contains at least one footer field label. A
    footer line whose only fields are non-Source (e.g. the TL;DR
    aggregate `Tags + Region` footer) collapses to nothing and the
    entire line is dropped.
    """
    out_lines: list[str] = []
    for line in body_md.splitlines():
        stripped = line.strip()
        is_footer = (
            (stripped.startswith("— *") or stripped.startswith("- *"))
            and stripped.endswith("*")
            and re.search(
                r"\b(?:Sources?|Tags|Region|Sector|Sectors|CVE|CVSS|Vector|Auth|Status|Additional source|Additional sources):",
                stripped,
            )
        )
        if is_footer:
            m = re.match(r"^(?P<lead>\s*[—-]\s*\*\s*)(?P<body>.+?)\*\s*$", line)
            if m:
                inner = m.group("body")
                # Case A: the line begins directly with a non-Source
                # field (e.g. `*Tags: ... · Region: ...*`). There is no
                # Source content to preserve — drop the whole line.
                if re.match(
                    r"^(?:Tags|Region|Sector|Sectors|CVE|CVSS|Vector|Auth|Status):",
                    inner,
                ):
                    continue
                # Case B: the line begins with a Source (explicit
                # `Source:` prefix or a bare `[Title](URL)` link). Drop
                # everything from the first ` · (Tags|...)` onwards.
                cut = _FOOTER_META_KEY_RE.search(inner)
                if cut:
                    inner = inner[: cut.start()].rstrip()
                inner = inner.rstrip(" ·").rstrip()
                if not inner.strip() or inner.strip().lower() in {"source:", "sources:"}:
                    continue
                line = m.group("lead") + inner + "*"
        out_lines.append(line)
    result = "\n".join(out_lines)
    # Preserve the input's trailing newline if there was one — important
    # for callers that splice the result back into a larger document.
    if body_md.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result


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
        # In RSS body, keep only the Sources portion of every metadata
        # footer line — Tags / Region / CVE / CVSS / Vector / Auth /
        # Status are RSS-feed metadata (`<category>`) and should not be
        # duplicated as visible italic text inside the feed body.
        body_md_clean = _strip_footer_metadata_in_md(body_md_clean)
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
            f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
            f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
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
        body_md_clean = _strip_footer_metadata_in_md(body_md_clean)
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
            f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
            f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
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
    """Per-item feed: one entry per content block that carries a metadata
    footer. Every H3 / H4 item with a footer becomes an entry; sections
    that have a section-level footer instead of per-item footers (Deep
    Dive in the v2 layout) also become a single entry."""
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
            # A section without per-item footers but with a section-level
            # footer (Deep Dive in v2) is itself a publishable unit. The
            # sec_footer carries Sources / Tags / CVE / etc that the
            # reader expects to land on as a single feed entry.
            if not sec["items"] and sec.get("section_footer"):
                slug = f"{b['name']}-{sec['anchor']}"[:80].strip("-")
                url = f"{site_url}briefs/{b['name']}/#{sec['anchor']}"
                item_entries.append(
                    {
                        "url": url,
                        "title": sec["heading"],
                        "publish_ts": b["publish_ts"],
                        "publish_rfc822": b["publish_rfc822"],
                        "publish_iso": b["publish_iso"],
                        "body_md": sec["body_md"],
                        "footer": sec["section_footer"],
                        "section_key": sec["key"],
                    }
                )
    item_entries.sort(key=lambda x: x["publish_ts"], reverse=True)
    item_entries = item_entries[:FEED_ITEMS_MAX]

    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for it in item_entries:
        body_html = render_markdown(it["body_md"], base_url=it["url"]) + render_footer_html(it["footer"], prefix=site_url, sources_only=True)
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
            f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
            f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
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
    # Every emitted HTML file contains the Umami snippet exactly once and
    # carries no inline `<script>` block (CSP `script-src 'self'` would
    # refuse to execute it).
    inline_script_re = re.compile(r"<script(?:\s[^>]*)?>(?!\s*</script>)[^<]", re.IGNORECASE)
    # Match the actual `<script>` tag that loads Umami, not stray textual
    # mentions of the URL (which can appear in docs that describe the
    # analytics setup).
    umami_tag_re = re.compile(r'<script[^>]*\bsrc=(?:"|&quot;)https://cloud\.umami\.is/script\.js', re.IGNORECASE)
    for path in OUT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        umami_count = len(umami_tag_re.findall(text))
        if umami_count != 1:
            errors.append(f"umami <script> tag count = {umami_count} (expected 1) in {path.relative_to(OUT)}")
        if inline_script_re.search(text):
            errors.append(
                f"inline <script> body in {path.relative_to(OUT)} — "
                "CSP would refuse to execute it. Move to an external file under assets/js/."
            )
        # Markdown-renderer placeholder leakage: `\x00CODE0\x00` markers
        # are stripped to literal "CODE0" text by browsers. If any survive
        # into the published HTML, the renderer's fixed-point substitution
        # is broken.
        if "\x00" in text or re.search(r"\bCODE\d+\b", text) or re.search(r"\bLINK\d+\b(?!\.html)", text):
            # Filter false positives: the literal word "CODE" can appear
            # in legitimate prose. Only flag when adjacent to digits in the
            # exact placeholder shape and not part of a real word.
            if "\x00" in text or re.search(r"(?<![A-Za-z])CODE\d+(?![A-Za-z])", text):
                errors.append(
                    f"markdown placeholder leak in {path.relative_to(OUT)} — "
                    "inline-code or link substitution is broken (renderer fixed-point regressed)"
                )
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
        # Defence-in-depth: refuse any rel_path that resolves outside OUT.
        # All ID-bearing call sites already validate via is_safe_path_segment,
        # but keep this last-line check so future call sites can't regress.
        try:
            resolved = out_path.resolve()
            out_resolved = OUT.resolve()
            if not (resolved == out_resolved or out_resolved in resolved.parents):
                raise RuntimeError(
                    f"refused: rel_url {rel_url!r} resolves outside _site/ "
                    f"({resolved} not under {out_resolved})"
                )
        except RuntimeError:
            raise
        except Exception as e:  # noqa: BLE001
            raise RuntimeError(f"refused: cannot resolve {rel_url!r}: {e}")
        atomic_write_text(out_path, html)
        h = hashlib.sha256(html.encode("utf-8")).hexdigest()
        manifest_pages[rel_url or "/"] = {"path": rel_path, "hash": h}
        sitemap.append((site_url + rel_url, lastmod))

    # ---- Per-brief auxiliary indexes ----------------------------------
    # Pre-compute per-brief CVE / topic / source lists so the brief detail
    # page can render its References block + cited footer.
    briefs_by_name = {b["name"]: b for b in briefs}
    cves_by_brief: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for c in cves["cves"]:
        for n in c.get("appearances", []):
            cves_by_brief[n].append(c)
    topics_by_brief: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for t in topics["items"]:
        for n in t.get("briefs", []):
            topics_by_brief[n].append(t)
    sources_by_brief: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for s in sources["sources"]:
        for n in s.get("appearances", []):
            sources_by_brief[n].append(s)

    items_index: dict[str, dict[str, Any]] = {}  # slug -> {item, brief}
    tag_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    region_index: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for b in briefs:
        # `b["name"]` was validated against the canonical YYYY-MM-DD or
        # YYYY-Www regex in collect_briefs(), but enforce again at the
        # path-construction boundary so an arbitrary code path adding a
        # brief later cannot bypass it.
        if not is_safe_path_segment(b["name"]):
            print(f"warning: skipping brief with unsafe name {b['name']!r}", file=sys.stderr)
            continue
        rel_url = ("briefs/weekly/" if b["kind"] == "weekly" else "briefs/") + b["name"] + "/"
        prefix = "../" * rel_url.count("/")  # path back to root
        canonical = site_url + rel_url
        html = render_brief_page(
            b,
            cves_in_brief=cves_by_brief.get(b["name"], []),
            topics_in_brief=topics_by_brief.get(b["name"], []),
            sources_in_brief=sources_by_brief.get(b["name"], []),
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
        )
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
        if not is_safe_path_segment(slug):
            print(f"warning: skipping item with unsafe slug {slug!r}", file=sys.stderr)
            continue
        rel_url = f"items/{slug}/"
        prefix = "../" * rel_url.count("/")
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
        if not is_safe_path_segment(c["id"]) or not CVE_RE.fullmatch(c["id"]):
            print(
                f"warning: skipping CVE entry with unsafe id {c['id']!r}; "
                "expected canonical CVE-YYYY-NNNN format",
                file=sys.stderr,
            )
            continue
        rel_url = f"cves/{c['id']}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_cve_page(
            c,
            briefs_index=briefs_by_name,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
        )
        emit_html(rel_url, html, lastmod=(c.get("last_seen") or "")[:10])

    # ---- Per-source pages ---------------------------------------------
    for s in sources["sources"]:
        if not is_safe_path_segment(s.get("id", "") or ""):
            print(
                f"warning: skipping source entry with unsafe id {s.get('id')!r}",
                file=sys.stderr,
            )
            continue
        rel_url = f"sources/{urllib.parse.quote(s['id'], safe='')}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_source_page(
            s,
            briefs_index=briefs_by_name,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
        )
        emit_html(rel_url, html, lastmod=(s.get("last_successful_fetch") or "")[:10])

    # ---- Per-topic pages ----------------------------------------------
    for t in topics["items"]:
        if not is_safe_path_segment(t.get("key", "") or ""):
            print(
                f"warning: skipping topic entry with unsafe key {t.get('key')!r}",
                file=sys.stderr,
            )
            continue
        rel_url = f"topics/{urllib.parse.quote(t['key'], safe='')}/"
        prefix = "../" * 2
        canonical = site_url + rel_url
        html = render_topic_page(
            t,
            briefs_index=briefs_by_name,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=canonical,
        )
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
        if not is_safe_path_segment(tag):
            print(f"warning: skipping tag index with unsafe tag {tag!r}", file=sys.stderr)
            continue
        rel_url = f"tags/{tag}/"
        emit_html(rel_url, tag_or_region_page("tags", tag, entries))
    for region, entries in region_index.items():
        if not is_safe_path_segment(region):
            print(f"warning: skipping region index with unsafe region {region!r}", file=sys.stderr)
            continue
        rel_url = f"regions/{region}/"
        emit_html(rel_url, tag_or_region_page("regions", region, entries))

    # ---- Briefs list page (grouped by month) --------------------------
    emit_html(
        "briefs/",
        render_briefs_list_page(
            briefs,
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "briefs/",
        ),
    )
    # Weekly subset list page (mirror of the legacy /weekly/ page).
    weekly_only = [b for b in briefs if b["kind"] == "weekly"]
    emit_html(
        "briefs/weekly/",
        render_briefs_list_page(
            weekly_only,
            site_url=site_url,
            cachebust=cachebust,
            prefix="../../",
            canonical=site_url + "briefs/weekly/",
        ),
    )

    # ---- CVE / Topic / Source list pages ------------------------------
    emit_html(
        "cves/",
        render_cve_list_page(
            cves["cves"],
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "cves/",
        ),
    )
    emit_html(
        "topics/",
        render_topic_list_page(
            topics["items"],
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "topics/",
        ),
    )
    emit_html(
        "sources/",
        render_source_list_page(
            sources["sources"],
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "sources/",
        ),
    )

    # ---- Home / about / ops -------------------------------------------
    daily_briefs = [b for b in briefs if b["kind"] == "daily"]
    latest = daily_briefs[0] if daily_briefs else (briefs[0] if briefs else None)
    counts = {
        "briefs": len(briefs),
        "daily": len(daily_briefs),
        "weekly": sum(1 for b in briefs if b["kind"] == "weekly"),
        "cves": len(cves["cves"]),
        "topics": len(topics["items"]),
        "sources": len(sources["sources"]),
    }
    home_html = render_home_page(
        latest,
        daily_briefs,
        site_url=site_url,
        cachebust=cachebust,
        canonical=site_url,
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
        render_ops_page(
            run_log,
            sources["sources"],
            prefix="../",
            site_url=site_url,
            cachebust=cachebust,
            canonical=site_url + "ops/",
        ),
    )

    # /404.html
    # GitHub Pages serves this for any unknown path under the project site,
    # but the browser's URL stays at the requested deep path (e.g.
    # `/security-newsletter/cves/CVE-A,%20CVE-B/`). That means relative asset
    # paths in the served HTML resolve against the deep path and 404 in turn,
    # leaving the page unstyled. To survive any depth, the 404 uses
    # *absolute* asset paths derived from `site_url` — this is the one page
    # in the build that needs them.
    site_base_path = urllib.parse.urlparse(site_url).path or "/"
    if not site_base_path.endswith("/"):
        site_base_path += "/"

    # Latest items the visitor likely meant.
    latest_briefs_html = ""
    if briefs:
        recent = briefs[:5]
        latest_briefs_html = "<ul class=\"entity-list\">" + "".join(
            f'<li><span><a class="e-title" href="{site_base_path}briefs/{_escape(b["name"])}/">{_escape(b["title"])}</a>'
            f'<div class="e-meta"><span class="e-tag">{_escape(b["kind"])}</span>'
            f'<span class="muted">{b.get("items", 0)} items</span></div></span>'
            f'<span class="mono muted">{_escape(b["name"])}</span></li>'
            for b in recent
        ) + "</ul>"

    err_body = f"""
<section style="max-width:62rem;margin-top:1rem">
  <p class="mono muted" style="font-size:0.78rem;letter-spacing:0.06em;text-transform:uppercase">Error 404</p>
  <h1 style="margin-top:0.2rem">That page is not on this site.</h1>
  <p class="subtitle" style="margin-top:0.6rem">
    The link you followed may be wrong, the page may have moved, or the brief that referenced it may have been corrected.
    <strong>CVE pages take a single ID</strong> — multi-CVE links like <code>cves/CVE-X,&nbsp;CVE-Y/</code> are not valid.
  </p>

  <div class="panel" style="margin-top:1.2rem">
    <h3 style="margin-top:0">Common ways here</h3>
    <ul style="margin-top:0.4rem">
      <li><strong>Renamed CVE / source / topic page.</strong> Use the search box above (also at the top of every page).</li>
      <li><strong>Old bookmark.</strong> Indexes refresh on every brief; the canonical URLs for items are stable but listings move.</li>
      <li><strong>Multi-CVE link from an older brief.</strong> Each CVE has its own page — use the search box or the
        <a href="{site_base_path}cves/">full CVE list</a>.</li>
    </ul>
  </div>

  <div class="row" style="gap:0.8rem;flex-wrap:wrap;margin-top:1.4rem">
    <a class="cta" href="{site_base_path}">Return home</a>
    <a class="cta cta--secondary" href="{site_base_path}briefs/">Browse briefs</a>
    <a class="cta cta--secondary" href="{site_base_path}cves/">All CVEs</a>
    <a class="cta cta--secondary" href="{site_base_path}topics/">Topics</a>
    <a class="cta cta--secondary" href="{site_base_path}sources/">Sources</a>
    <a class="cta cta--secondary" href="{site_base_path}ops/">Operations</a>
  </div>

  {f'<h2 class="section-head" style="margin-top:1.8rem">Latest briefs</h2>{latest_briefs_html}' if latest_briefs_html else ''}

  <p class="muted" style="margin-top:1.6rem;font-size:0.82rem">
    If you think this is a broken link inside the site, please open an issue at
    <a href="https://github.com/OwlsNightCatch/security-newsletter/issues" target="_blank" rel="noopener noreferrer">github.com/OwlsNightCatch/security-newsletter</a>.
  </p>
</section>
"""

    err = base_template(
        title="404 — Not found · CTI Briefs",
        description="The page you requested is not on this site. Search or use the suggested links to find what you were looking for.",
        body=err_body,
        canonical=site_url + "404.html",
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=site_base_path,
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
        "counts": dict(counts, items=len(items_index), tags=len(tag_index), regions=len(region_index)),
    }
    atomic_write_text(OUT / "data" / "build_manifest.json", json.dumps(manifest, indent=2, sort_keys=True))

    # ---- Search index (consumed by topbar autocomplete) ---------------
    # Same flat shape as the previous SPA expected. Keys: kind, id, title,
    # hint, route, tags. We use clean URLs as `route` so the JS can
    # `window.location = entry.route` directly.
    search_idx: list[dict[str, Any]] = []
    for b in briefs:
        kind_path = "weekly/" if b["kind"] == "weekly" else ""
        route = f"briefs/{kind_path}{b['name']}/"
        hint = (b.get("tldr") or [""])[0][:240] if b.get("tldr") else f"{b['kind'].capitalize()} brief · {b.get('items', 0)} items"
        search_idx.append({
            "kind": "brief",
            "id": b["name"],
            "title": b["title"],
            "hint": hint,
            "route": route,
            "tags": [b["kind"]] + b.get("cves", [])[:6],
        })
    for c in cves["cves"]:
        search_idx.append({
            "kind": "cve",
            "id": c["id"],
            "title": c["id"],
            "hint": (c.get("title") or "")[:240],
            "route": f"cves/{urllib.parse.quote(c['id'], safe='')}/",
            "tags": [],
        })
    for t in topics["items"]:
        search_idx.append({
            "kind": "topic",
            "id": t["key"],
            "title": t.get("title") or t["key"],
            "hint": f"{t.get('type', '')} · last covered {t.get('last_covered', '?')}",
            "route": f"topics/{urllib.parse.quote(t['key'], safe='')}/",
            "tags": [t.get("type") or ""] + (t.get("flags") or []),
        })
    for s in sources["sources"]:
        cats_str = ", ".join(s.get("category") or [])
        search_idx.append({
            "kind": "source",
            "id": s["id"],
            "title": s.get("publisher") or s["id"],
            "hint": f"{s.get('reliability', '')} · {cats_str}",
            "route": f"sources/{urllib.parse.quote(s['id'], safe='')}/",
            "tags": (s.get("category") or []) + [s.get("reliability") or "", s.get("status") or ""],
        })
    atomic_write_text(OUT / "data" / "search.json", json.dumps(search_idx))

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
