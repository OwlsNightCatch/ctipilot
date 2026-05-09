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
    README.md                     landing page at /about/
    docs/*.md                     rendered into /about/docs/<name>/
    prompts/*.md                  rendered into /about/prompts/<name>/
    prompts/CHANGELOG.md          rendered into /about/prompts/changelog/

Outputs (written under site/_site/):
    /                             home (latest brief preview)
    /briefs/YYYY-MM-DD/           single daily brief
    /briefs/weekly/YYYY-Www/      single weekly brief
    /briefs/                      brief index
    /briefs/<date>/<slug>/        one page per metadata-footer item, scoped under its parent brief
    /cves/<CVE-ID>/               one page per CVE
    /sources/<id>/                one page per source
    /topics/<key>/                one page per covered topic
    /tags/<tag>/                  index of items with this tag
    /regions/<region>/            index of items with this region
    /ops/                         operations dashboard
    /about/                       landing page (Documentation + Prompts sections)
    /about/docs/                  documentation index
    /about/docs/<name>/           one page per docs/*.md
    /about/prompts/               prompts index + recent CHANGELOG headings
    /about/prompts/<name>/        one page per prompts/*.md (excl. CHANGELOG)
    /about/prompts/changelog/     full prompt CHANGELOG
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
import math
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

DEFAULT_SITE_URL = "https://ctipilot.ch/"
DEFAULT_GITHUB_REPO = "OwlsNightCatch/ctipilot"

# RSS truncation per feed (HTML archive is unbounded).
FEED_DAILY_MAX = 30
FEED_WEEKLY_MAX = 30
FEED_ITEMS_MAX = 50

# === RESOURCE CAPS ======================================================
#
# Per-file ceilings for everything the build reads from disk. A poisoned
# state file or a runaway agent run could plant a multi-hundred-MB
# Markdown file; the build would otherwise attempt to load and render it
# and OOM the runner. Caps fail the build with a clear message instead.
#
# These ceilings are loose by design — the largest legitimate brief on
# record is ~80 KB; the largest state file (covered_items.json) is ~40 KB.
# We pick caps an order of magnitude above current usage so the agent has
# room to grow but a runaway / poisoned input is still blocked.
MAX_BRIEF_BYTES = 4 * 1024 * 1024            # 4 MB per brief / docs file
MAX_STATE_BYTES = 16 * 1024 * 1024           # 16 MB per state file
MAX_VENDOR_BYTES = 4 * 1024 * 1024           # 4 MB per vendored JS file
MAX_BRIEFS_DIR_BYTES = 256 * 1024 * 1024     # 256 MB total briefs/ tree


def _read_text_capped(path: Path, max_bytes: int, *, encoding: str = "utf-8") -> str:
    """Read `path` as text but refuse if its on-disk size exceeds the
    ceiling. Used at every input boundary."""
    size = path.stat().st_size
    if size > max_bytes:
        raise RuntimeError(
            f"refused: {path} is {size} bytes, exceeds cap of {max_bytes}"
        )
    return path.read_text(encoding=encoding)


# === SECRET REDACTOR (write-time) =======================================
#
# Last-line guard against the agent accidentally pasting a credential
# into a brief, the docs, or the search index. Runs at the emit boundary,
# inspecting every emitted page / feed / JSON blob for known
# secret-shaped tokens. Refuses the build (non-zero exit) if any pattern
# hits — failing the build is preferable to silently propagating a
# secret to the public site, RSS feeds, and gh-pages.
#
# This is *not* a substitute for keeping secrets out of the runner. It
# is a defence-in-depth check for the autonomous-agent failure mode where
# the agent paraphrases the runner's environment into prose.
_SECRET_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("AWS secret access key (heuristic)",
     re.compile(r"(?i)\baws_secret_access_key\s*[:=]\s*[\"']?[A-Za-z0-9/+=]{40}[\"']?")),
    # GitHub fine-grained PAT format: github_pat_<22 chars>_<59 chars>.
    # `\b` is unreliable around the underscore, so we drop it and rely on
    # the surrounding non-word context being absent of word characters.
    ("GitHub fine-grained PAT",
     re.compile(r"github_pat_[A-Za-z0-9]{22}_[A-Za-z0-9_]{50,}")),
    ("GitHub classic / OAuth token",
     re.compile(r"\b(?:ghp|gho|ghs|ghr|ghu)_[A-Za-z0-9]{36,255}\b")),
    ("Anthropic API key",
     re.compile(r"\bsk-ant-(?:api|admin|sid)[A-Za-z0-9]*-[A-Za-z0-9_-]{20,}\b")),
    ("OpenAI API key",
     re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{30,255}\b")),
    ("Slack token",
     re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}\b")),
    ("Stripe live key",
     re.compile(r"\b(?:sk|pk|rk)_live_[A-Za-z0-9]{20,}\b")),
    # Google API keys are exactly 39 chars including the AIza prefix
    # (4 + 35 = 39). Match exactly that to avoid false-positives on
    # arbitrary base64 substrings starting with AIza.
    ("Google API key",
     re.compile(r"(?<![A-Za-z0-9_-])AIza[0-9A-Za-z_-]{35}(?![A-Za-z0-9_-])")),
    ("PEM private key block",
     re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED |PGP )?PRIVATE KEY-----")),
    # Real JWTs have base64url segments. Each segment is at least 6
    # chars in practice (a header alone is ~30); we accept ≥6 to keep
    # the test sample short while still excluding obvious non-JWT
    # 3-segment dotted strings.
    ("JWT (eyJ. style)",
     re.compile(r"\beyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]{6,}\b")),
]


def scan_for_secrets(text: str) -> list[tuple[str, str]]:
    """Return [(pattern_label, matched_excerpt), …] for any hits in `text`.
    Empty list means clean."""
    out: list[tuple[str, str]] = []
    for label, pat in _SECRET_PATTERNS:
        m = pat.search(text)
        if m:
            sample = m.group(0)
            # Truncate so we don't echo the secret whole into stderr.
            redacted = sample[:8] + "…" + sample[-4:] if len(sample) > 16 else "***"
            out.append((label, redacted))
    return out


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


def _brief_url_path(brief: dict[str, Any]) -> str:
    """Path segment for a brief, relative to the site root, with trailing
    slash. Daily: ``briefs/2026-05-09/``; weekly: ``briefs/weekly/2026-W19/``.
    Used as the parent path for per-item permalinks
    (``/briefs/<date>/<slug>/``) — keeping the helper in one place avoids
    drift between the brief-detail page, the RSS item URLs, and the
    per-item-page emit path."""
    return ("briefs/weekly/" if brief.get("kind") == "weekly" else "briefs/") + brief["name"] + "/"


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
    Catches both silent on-disk tampering and accidental upgrades.

    Verifies *both* the sha256 and sha384 lines in HASHES so a future
    attacker cannot defeat the check by colliding only one algorithm.
    """
    vendor = SITE / "assets" / "vendor"
    hashes_file = vendor / "HASHES"
    if not hashes_file.exists():
        print(f"warning: {hashes_file} missing; skipping integrity check", file=sys.stderr)
        return
    # algo -> {fname -> digest}
    expected: dict[str, dict[str, str]] = {"sha256": {}, "sha384": {}}
    for raw in hashes_file.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        parts = line.split()
        if len(parts) != 3:
            continue
        algo, fname, digest = parts
        if algo in expected:
            expected[algo][fname] = digest
    failures: list[str] = []
    files_seen = set(expected["sha256"]) | set(expected["sha384"])
    for fname in sorted(files_seen):
        path = vendor / fname
        if not path.exists():
            failures.append(f"{fname}: missing")
            continue
        body = path.read_bytes()
        for algo in ("sha256", "sha384"):
            want = expected[algo].get(fname)
            if want is None:
                # Not every file has both lines — only validate what is
                # listed.
                continue
            got = hashlib.new(algo, body).hexdigest()
            if got != want:
                failures.append(
                    f"{fname}: {algo} mismatch (expected {want}, got {got})"
                )
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
    # Refuse protocol-relative URLs (`//evil.example/x`) and any URL that
    # leads with backslashes (`\\evil.example\x`, `\\\\…`). A Markdown
    # link `[click](//evil/x)` would otherwise render as
    # `<a href="//evil/x">` and the browser would navigate to
    # `https://evil/x` — neither XSS nor blocked by the strict CSP, but a
    # cross-origin redirect that brief content should never be able to
    # cause. The legitimate Markdown shape for an external link is the
    # explicit-scheme form, which the allowlist below admits.
    if stripped.startswith("//") or stripped.startswith("\\"):
        return "#"
    # Some renderers normalise backslash in URL paths; reject any URL that
    # starts with a `/\` or `\/` mix as well.
    if stripped[:2] in ("/\\", "\\/"):
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


# === INPUT SANITISATION =================================================

# ASCII control chars (excluding `\t`, `\n`, `\r`) and DEL. These never
# appear in legitimate brief / docs Markdown; they can confuse the
# renderer's `\x00`-prefixed placeholder substitution loop and should
# not survive into the output (the end-of-build self-check already
# refuses output that contains `\x00`, but stripping at the input
# boundary makes the renderer pipeline impossible to confuse in the
# first place).
_CONTROL_CHAR_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")


def _strip_controls(text: str) -> str:
    """Strip ASCII control characters that have no place in Markdown
    input. Tab / newline / carriage-return are preserved."""
    if not text:
        return text
    return _CONTROL_CHAR_RE.sub("", text)


def render_inline(s: str, *, base_url: str | None = None) -> str:
    """Render Markdown inline constructs to HTML.

    `base_url` (when given) absolutises relative links so the result is
    self-contained (used by RSS body rendering — RSS readers don't have a
    base URL to resolve against).
    """
    # Strip ASCII control characters at the parse boundary, same reasoning
    # as in render_markdown. The renderer's placeholder markers all use
    # \x00 — keeping that byte out of the input keeps the substitution
    # loop unambiguous.
    s = _strip_controls(s)
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
    link text where nested links are illegal anyway.

    Note: deliberately does NOT call `_strip_controls` here. This function
    is invoked from inside `render_inline`'s link-substitution loop on
    text that already contains the renderer's `\\x00CODE…\\x00`
    placeholder markers; stripping at this depth would remove those
    markers and leak placeholder digits ("CODE0") into the output. The
    top-level entry points (`render_inline`, `render_markdown`) already
    stripped controls at the parse boundary.
    """
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
    # Strip ASCII control characters at the parse boundary. Briefs are
    # generated by an LLM from publisher prose; legitimate output never
    # contains \x00..\x08 / \x0B / \x0C / \x0E..\x1F / \x7F. A literal
    # \x00 in input would otherwise collide with the renderer's
    # `\x00CODE…\x00` / `\x00LINK…\x00` placeholder markers and could
    # smuggle attacker text into the placeholder substitution loop.
    md = _strip_controls(md)
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
            # UPDATE-block extension: when an item opens with the
            # `> **UPDATE (originally covered ...):**` callout, the agent
            # routinely writes the body that follows as plain paragraphs
            # rather than as `> `-prefixed lines, so the rendered HTML
            # closes the blockquote after the label and leaves the
            # update content visually outside the callout. Detect that
            # shape and absorb the following paragraphs into the same
            # blockquote until we hit a heading, HR, fenced code,
            # another blockquote, or a metadata-footer line.
            extras_class = ""
            if buf2 and re.search(r"\*\*UPDATE\b", buf2[0]):
                extras_class = ' class="callout-update"'
                while i < n:
                    la = lines[i]
                    stripped = la.lstrip()
                    if not stripped:
                        buf2.append("")
                        i += 1
                        continue
                    if (stripped.startswith("#")
                            or stripped.startswith("```")
                            or re.match(r"^\s*([-*_])\s*\1\s*\1\s*$", la)
                            or re.match(r"^---+$", stripped)
                            or re.match(r"^[—-]\s*\*", stripped)
                            or stripped.startswith(">")):
                        break
                    buf2.append(la)
                    i += 1
                while buf2 and not buf2[-1].strip():
                    buf2.pop()
            inner = render_markdown("\n".join(buf2), base_url=base_url)
            out.append(f"<blockquote{extras_class}>{inner}</blockquote>")
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
    without footer line)`. Otherwise return `(None, body unchanged)`.

    Scans backwards through the body so an item whose tail carries an
    aggregation (e.g. a § 3 CVE Summary Table appended after the per-CVE
    H3's footer) still surfaces the footer pills — the table stays in
    the body, only the footer line is lifted out."""
    lines = body.splitlines()
    while lines and _is_skippable_trailer(lines[-1]):
        lines.pop()
    if not lines:
        return None, body
    # Fast path: the footer is the trailing line.
    fm = parse_footer_line(lines[-1])
    if fm:
        return fm, "\n".join(lines[:-1]).rstrip()
    # Fallback: scan backwards for the most-recent footer-shaped line.
    # Anything between that line and the end of the body is preserved
    # in-place — we only lift the footer itself out.
    for j in range(len(lines) - 2, -1, -1):
        fm = parse_footer_line(lines[j])
        if fm:
            stripped = "\n".join(lines[:j] + lines[j + 1:]).strip("\n")
            return fm, stripped
    return None, body


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
    text = _read_text_capped(path, MAX_BRIEF_BYTES)
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
            # Slug is the heading slug only — uniqueness comes from the
            # parent brief in the URL (`/briefs/<date>/<slug>/`). Older
            # builds prefixed the brief name into the slug because the
            # item lived at `/items/<slug>/`; that prefix is now redundant.
            items.append(
                {
                    "heading": item_heading,
                    "anchor": slugify(item_heading),
                    "slug": slugify(item_heading)[:80].strip("-"),
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

COPY_ICON_SVG = (
    '<svg class="md-split__icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"/>'
    '<path fill="currentColor" d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"/>'
    '</svg>'
)

CARET_DOWN_SVG = (
    '<svg class="md-split__chevron" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M12.78 5.22a.749.749 0 0 1 0 1.06l-4.25 4.25a.749.749 0 0 1-1.06 0L3.22 6.28a.749.749 0 1 1 1.06-1.06L8 8.939l3.72-3.719a.749.749 0 0 1 1.06 0Z"/>'
    '</svg>'
)

EXTERNAL_LINK_SVG = (
    '<svg class="md-split__ext" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
    '<path fill="currentColor" d="M3.75 2A1.75 1.75 0 0 0 2 3.75v8.5C2 13.216 2.784 14 3.75 14h8.5A1.75 1.75 0 0 0 14 12.25v-3.5a.75.75 0 0 0-1.5 0v3.5a.25.25 0 0 1-.25.25h-8.5a.25.25 0 0 1-.25-.25v-8.5a.25.25 0 0 1 .25-.25h3.5a.75.75 0 0 0 0-1.5Z"/>'
    '<path fill="currentColor" d="M9.25 2a.75.75 0 0 0 0 1.5h2.19L6.22 8.72a.749.749 0 1 0 1.06 1.06l5.22-5.22v2.19a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-.75-.75Z"/>'
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
<meta property="og:site_name" content="ctipilot.ch" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{_escape(title)}" />
<meta property="og:description" content="{_escape(description)}" />
<meta property="og:url" content="{_escape(canonical)}" />
<meta property="og:locale" content="en_US" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{_escape(title)}" />
<meta name="twitter:description" content="{_escape(description)}" />
<link rel="stylesheet" href="{pfx}assets/css/styles.css?v={cachebust}" />
<link rel="alternate" type="application/rss+xml" title="ctipilot.ch — Daily" href="{pfx}feed.xml" />
<link rel="alternate" type="application/rss+xml" title="ctipilot.ch — Weekly" href="{pfx}feed-weekly.xml" />
<link rel="alternate" type="application/rss+xml" title="ctipilot.ch — Per item" href="{pfx}feed-items.xml" />
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
    <a class="brand" href="{pfx}" aria-label="Home — ctipilot.ch">
      <span class="brand-mark" aria-hidden="true">CTI</span>
      <span class="brand-text"><strong>ctipilot.ch</strong><small>Switzerland · Europe · Public sector</small></span>
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

    sections_toc_html = sections_toc or '<li class="muted">—</li>'
    toc_html = (
        '<h3>On this page</h3>'
        f'<ul class="toc-sections">{sections_toc_html}</ul>'
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
            f'<a class="badge badge--accent" href="{prefix}about/prompts/changelog/" '
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
    # Drop the trailing horizontal rule that the prompt convention places
    # between the metadata block and the first H2 — once the metadata line
    # has been stripped above, the lone `---` becomes a stray <hr/> that
    # introduces an empty band of whitespace before § 0.
    preamble_md = re.sub(r"\n\s*-{3,}\s*\n*\Z", "\n", preamble_md)
    preamble_md = preamble_md.rstrip() + "\n" if preamble_md.strip() else ""
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
                f'<a class="item-link" href="{prefix}{_brief_url_path(brief)}{_escape(slug)}/">{_escape(it["heading"])}</a>'
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

    copy_split = f"""
<div class="md-split" data-md-split>
  <button type="button" class="md-split__primary" data-action="copy-md" data-raw-url="{raw_path}" title="Copy the raw Markdown content">
    {COPY_ICON_SVG}<span class="md-split__label">Copy as Markdown</span>
  </button>
  <button type="button" class="md-split__caret" aria-haspopup="menu" aria-expanded="false" aria-label="More copy options">
    {CARET_DOWN_SVG}
  </button>
  <div class="md-split__menu" role="menu" hidden>
    <button type="button" role="menuitem" class="md-split__item" data-action="copy-md" data-raw-url="{raw_path}">
      <span class="md-split__item-title">Copy as Markdown</span>
      <span class="md-split__item-sub">Copy the raw .md content</span>
    </button>
    <button type="button" role="menuitem" class="md-split__item" data-action="share">
      <span class="md-split__item-title">Copy link</span>
      <span class="md-split__item-sub">Copy permalink to this brief</span>
    </button>
    <a role="menuitem" class="md-split__item" href="{raw_path}" target="_blank" rel="noopener noreferrer">
      <span class="md-split__item-title">View raw .md{EXTERNAL_LINK_SVG}</span>
      <span class="md-split__item-sub">Open the .md file in a new tab</span>
    </a>
  </div>
</div>
"""
    body = f"""
<header class="brief-page-head">
  <h1>{_escape(brief['title'])}</h1>
  <div class="brief-page-head__actions">{copy_split}</div>
</header>
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
        title="CVEs — ctipilot.ch",
        description=f"{len(cves)} CVEs referenced across all briefs.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_embedded_items_section(
    items: list[dict[str, Any]],
    *,
    heading: str,
    empty_text: str,
    prefix: str,
) -> str:
    """Render the parsed brief items that match the surrounding entity (a
    CVE id, a topic key) as full cards — heading + brief lineage + body
    Markdown + per-item footer. Used on the CVE and Topic detail pages
    so the reader sees the actual analysis instead of just a list of
    brief dates. Items are sorted by publish timestamp, newest first."""
    if not items:
        return f'<h2 class="section-head" style="margin-top:1.5rem">{_escape(heading)}</h2><p class="muted">{_escape(empty_text)}</p>'

    # De-duplicate when an item appears multiple times in the bucket
    # (same brief + same slug). Newer briefs first.
    seen: set[tuple[str, str]] = set()
    ordered = sorted(items, key=lambda r: r["brief"]["publish_ts"], reverse=True)
    cards: list[str] = []
    for record in ordered:
        it = record["item"]
        b = record["brief"]
        slug = it["slug"]
        key = (b["name"], slug)
        if key in seen:
            continue
        seen.add(key)
        item_url = f"{prefix}{_brief_url_path(b)}{_escape(slug)}/"
        brief_url = f"{prefix}{_brief_url_path(b)}"
        body_html = render_markdown(it.get("body_md") or "", base_url=item_url)
        footer_html = render_footer_html(it["footer"], prefix=prefix) if it.get("footer") else ""
        publish_date = (b.get("publish_iso") or "")[:10]
        cards.append(
            '<article class="embedded-item">'
            '<header class="embedded-item__head">'
            f'<h3 class="embedded-item__heading"><a href="{item_url}">{_escape(it["heading"])}</a></h3>'
            '<p class="embedded-item__lineage muted">'
            f'From <a href="{brief_url}">{_escape(b["title"])}</a>'
            f' · published {_escape(publish_date)}'
            f' · <a class="embedded-item__permalink" href="{item_url}">view item permalink &rarr;</a>'
            '</p>'
            '</header>'
            f'<div class="embedded-item__body brief-prose">{body_html}</div>'
            f'{footer_html}'
            '</article>'
        )

    return (
        f'<h2 class="section-head" style="margin-top:1.5rem">{_escape(heading)} ({len(cards)})</h2>'
        f'<div class="embedded-items">{"".join(cards)}</div>'
    )


# === SINGLE CVE ========================================================

def render_cve_page(
    cve: dict[str, Any],
    *,
    briefs_index: dict[str, dict[str, Any]],
    matching_items: list[dict[str, Any]] | None = None,
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

{render_embedded_items_section(
    matching_items or [],
    heading=f"Items in briefs that mention {cve['id']}",
    empty_text=(
        "No item in any parsed brief carries this CVE in its metadata footer yet. "
        "Once a brief surfaces this CVE in an item-level footer, the analysis will appear here in full."
    ),
    prefix=prefix,
)}

<h2 class="section-head" style="margin-top:1.5rem">Brief appearances</h2>
{appearances_block}
"""
    return base_template(
        title=f"{cve['id']} — ctipilot.ch",
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
        title="Topics — ctipilot.ch",
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
    matching_items: list[dict[str, Any]] | None = None,
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

{render_embedded_items_section(
    matching_items or [],
    heading=f"Items in briefs about {topic.get('title') or topic['key']}",
    empty_text=(
        "No parsed item heading or body matches this topic yet. The match rules are "
        "an exact CVE id (for cve-typed topics) or the topic's title appearing in the "
        "item heading or body — once that lands in a brief, the full analysis will appear here."
    ),
    prefix=prefix,
)}

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
        title="Sources — ctipilot.ch",
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
        title="Briefs — ctipilot.ch",
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
  <h1>ctipilot.ch</h1>
  <p class="lede">Daily and weekly cyber threat intelligence — Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated by an LLM.</p>
</section>
<section class="home-empty">
  <p>The first daily routine run will publish a brief here.</p>
  <p><a href="about/">About this newsletter →</a></p>
</section>
{redirect_js}
"""
        return base_template(
            title="ctipilot.ch — Switzerland, Europe & Public Sector",
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
  <h1>ctipilot.ch</h1>
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
        title="ctipilot.ch — Switzerland, Europe & Public Sector",
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

    Inputs are README.md / docs/*.md / prompts/*.md (including CHANGELOG),
    all of which use relative links like `[`prompts/verification.md`](prompts/verification.md)`
    or `[briefs](briefs/)`. Those resolve correctly on github.com but
    404 on the deployed Pages site (everything is rendered into
    /about/docs/<name>/ or /about/prompts/<name>/, not the original .md path).

    Mapping rules:
        docs/<name>.md             → <prefix>about/docs/<name>/
        docs/                      → <prefix>about/docs/
        prompts/CHANGELOG.md       → <prefix>about/prompts/changelog/
        prompts/<name>.md          → <prefix>about/prompts/<name>/
        prompts/                   → <prefix>about/prompts/
        briefs/                    → <prefix>briefs/
        briefs/<name>.md           → <prefix>briefs/<name>/   (only daily / weekly)
        briefs/weekly/<name>.md    → <prefix>briefs/weekly/<name>/
        anything else relative     → https://github.com/<repo>/blob/main/<path>
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
        # docs/<name>.md → about/docs/<name>/
        m = re.match(r"^docs/([^/]+)\.md$", p)
        if m:
            return prefix + f"about/docs/{m.group(1)}/" + frag
        # docs/ index → about/docs/
        if p == "docs/" or p == "docs":
            return prefix + "about/docs/" + frag
        # prompts/CHANGELOG.md → about/prompts/changelog/
        if p == "prompts/CHANGELOG.md":
            return prefix + "about/prompts/changelog/" + frag
        # prompts/<name>.md → about/prompts/<name>/
        m = re.match(r"^prompts/([^/]+)\.md$", p)
        if m:
            return prefix + f"about/prompts/{m.group(1)}/" + frag
        # prompts/ index → about/prompts/
        if p == "prompts/" or p == "prompts":
            return prefix + "about/prompts/" + frag
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
    # `prompts/verification.md` to stay relative so _rewrite_about_links
    # can route them to /about/prompts/verification/ instead of letting urljoin
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
#
# The Ops page renders directly from state/run_log.json and sources/sources.json.
# It is read-only — no JavaScript chart libraries — so every visualisation is
# built as inline SVG. CSP is `script-src 'self' https://cloud.umami.is` which
# excludes 'unsafe-inline'; charts must therefore be static SVG with no event
# handlers.
#
# Every helper below returns a str of HTML (or SVG) that goes straight into
# render_ops_page.


def _ops_format_duration(seconds: float | int | None) -> str:
    """Compact human-readable duration. 0 / None / negative → '—'."""
    if not seconds or seconds <= 0:
        return "—"
    s = int(seconds)
    if s < 90:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}m {s % 60:02d}s"
    h = s // 3600
    m = (s % 3600) // 60
    return f"{h}h {m:02d}m"


def _ops_svg_sparkline(values: list[float], *, width: int = 220, height: int = 36,
                       stroke: str = "var(--accent)", fill: str = "rgba(232,93,117,0.18)",
                       label: str = "") -> str:
    """Inline SVG line + filled-area sparkline. Empty values → placeholder."""
    if not values or all(v <= 0 for v in values):
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    n = len(values)
    if n == 1:
        values = [values[0], values[0]]
        n = 2
    vmax = max(values) or 1.0
    vmin = min(values)
    span = max(vmax - vmin, 1e-9)
    pad = 2
    x_step = (width - 2 * pad) / max(n - 1, 1)
    pts = []
    for i, v in enumerate(values):
        x = pad + i * x_step
        # Invert Y because SVG y grows downward.
        y = pad + (1 - (v - vmin) / span) * (height - 2 * pad)
        pts.append((x, y))
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    area_pts = f"{pad},{height - pad} {line} {width - pad},{height - pad}"
    last_x, last_y = pts[-1]
    aria = _escape(label or "trend")
    return (
        f'<svg class="ops-spark" viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="none" role="img" aria-label="{aria}">'
        f'<polygon points="{area_pts}" fill="{fill}" stroke="none"/>'
        f'<polyline points="{line}" fill="none" stroke="{stroke}" stroke-width="1.5" '
        f'stroke-linejoin="round" stroke-linecap="round"/>'
        f'<circle cx="{last_x:.1f}" cy="{last_y:.1f}" r="2.4" fill="{stroke}"/>'
        f'</svg>'
    )


def _ops_svg_bars(values: list[float], *, width: int = 220, height: int = 56,
                   color: str = "var(--accent-soft)", track: str = "var(--bg-elev-2)",
                   label: str = "") -> str:
    """Inline SVG vertical-bar chart (one bar per value)."""
    if not values:
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    n = len(values)
    vmax = max(max(values), 1.0)
    pad = 1
    bar_gap = 1
    available = width - 2 * pad - bar_gap * (n - 1)
    bar_w = max(available / n, 1)
    rects: list[str] = []
    for i, v in enumerate(values):
        x = pad + i * (bar_w + bar_gap)
        h = (v / vmax) * (height - 2 * pad)
        y = height - pad - h
        rects.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{h:.1f}" '
            f'fill="{color}" rx="1"/>'
        )
    aria = _escape(label or "bars")
    return (
        f'<svg class="ops-spark" viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="none" role="img" aria-label="{aria}">'
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="{track}" rx="3"/>'
        + "".join(rects)
        + '</svg>'
    )


def _ops_svg_stacked_bars(stacks: list[list[tuple[float, str]]], *, width: int = 220,
                           height: int = 56, track: str = "var(--bg-elev-2)",
                           label: str = "") -> str:
    """Inline SVG stacked vertical bars. Each entry in `stacks` is a list of
    (value, color) tuples drawn from bottom to top."""
    if not stacks:
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    n = len(stacks)
    totals = [sum(v for v, _ in s) for s in stacks]
    vmax = max(totals + [1.0])
    pad = 1
    bar_gap = 1
    available = width - 2 * pad - bar_gap * (n - 1)
    bar_w = max(available / n, 1)
    rects: list[str] = []
    for i, stack in enumerate(stacks):
        x = pad + i * (bar_w + bar_gap)
        cursor_y = height - pad
        for value, color in stack:
            if value <= 0:
                continue
            h = (value / vmax) * (height - 2 * pad)
            cursor_y -= h
            rects.append(
                f'<rect x="{x:.1f}" y="{cursor_y:.1f}" width="{bar_w:.1f}" '
                f'height="{h:.1f}" fill="{color}"/>'
            )
    aria = _escape(label or "stacked bars")
    return (
        f'<svg class="ops-spark" viewBox="0 0 {width} {height}" '
        f'preserveAspectRatio="none" role="img" aria-label="{aria}">'
        f'<rect x="0" y="0" width="{width}" height="{height}" fill="{track}" rx="3"/>'
        + "".join(rects)
        + '</svg>'
    )


def _ops_svg_donut(slices: list[tuple[str, float, str]], *, size: int = 110,
                    hole: float = 0.55, label: str = "") -> str:
    """Donut chart from (label, value, color) slices. Returns ``(svg, legend)``
    bundled in a wrapping <figure>. Tiny slices collapse into 'other' visually
    but stay listed in the legend."""
    total = sum(v for _, v, _ in slices if v > 0)
    if total <= 0:
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    cx = cy = size / 2
    r_outer = size / 2 - 2
    r_inner = r_outer * hole
    paths: list[str] = []
    legend_items: list[str] = []
    angle = -90.0  # start at 12 o'clock
    for name, value, color in slices:
        if value <= 0:
            continue
        sweep = (value / total) * 360.0
        if sweep >= 359.99:
            # full circle — draw as ring with two arcs
            paths.append(
                f'<circle cx="{cx}" cy="{cy}" r="{r_outer}" fill="{color}"/>'
                f'<circle cx="{cx}" cy="{cy}" r="{r_inner}" fill="var(--bg)"/>'
            )
        else:
            a0 = math.radians(angle)
            a1 = math.radians(angle + sweep)
            large = 1 if sweep > 180 else 0
            x0o = cx + r_outer * math.cos(a0)
            y0o = cy + r_outer * math.sin(a0)
            x1o = cx + r_outer * math.cos(a1)
            y1o = cy + r_outer * math.sin(a1)
            x0i = cx + r_inner * math.cos(a1)
            y0i = cy + r_inner * math.sin(a1)
            x1i = cx + r_inner * math.cos(a0)
            y1i = cy + r_inner * math.sin(a0)
            d = (
                f"M {x0o:.2f} {y0o:.2f} "
                f"A {r_outer} {r_outer} 0 {large} 1 {x1o:.2f} {y1o:.2f} "
                f"L {x0i:.2f} {y0i:.2f} "
                f"A {r_inner} {r_inner} 0 {large} 0 {x1i:.2f} {y1i:.2f} Z"
            )
            paths.append(f'<path d="{d}" fill="{color}"/>')
        angle += sweep
        pct = value / total * 100
        legend_items.append(
            '<li class="ops-legend__item">'
            f'<span class="ops-legend__swatch" style="background:{color}"></span>'
            f'<span class="ops-legend__label">{_escape(name)}</span>'
            f'<span class="ops-legend__value mono">{int(value)} <span class="muted">({pct:.0f}%)</span></span>'
            '</li>'
        )
    aria = _escape(label or "distribution")
    svg = (
        f'<svg class="ops-donut" viewBox="0 0 {size} {size}" '
        f'role="img" aria-label="{aria}">' + "".join(paths) + '</svg>'
    )
    legend_html = f'<ul class="ops-legend">{"".join(legend_items)}</ul>' if legend_items else ""
    return f'<div class="ops-donut-wrap">{svg}{legend_html}</div>'


def _ops_svg_heatmap(rows: list[tuple[str, list[tuple[float, str]]]], *, cell: int = 22,
                      gap: int = 3, label: str = "") -> str:
    """Heatmap with row labels. Each row is (label, [(value 0–1, tooltip)]).
    Cell colour interpolates between bg-elev-2 (0) and accent (1).

    With only a few runs in the window the heatmap cells dwarf the row
    labels visually if the cell size is small, so we default to a 22 px
    cell — comfortable on desktop, still legible on narrow viewports
    because the wrapping `<div class="ops-heatmap-wrap">` provides
    horizontal scroll."""
    if not rows:
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    max_cols = max((len(cells) for _, cells in rows), default=0)
    if max_cols == 0:
        return f'<div class="ops-spark ops-spark--empty" aria-label="{_escape(label)}">no data</div>'
    label_col = 36
    width = label_col + max_cols * cell + (max_cols - 1) * gap + 4
    height = len(rows) * cell + (len(rows) - 1) * gap + 4
    parts: list[str] = []
    for ri, (rlabel, cells) in enumerate(rows):
        y = 2 + ri * (cell + gap)
        parts.append(
            f'<text x="0" y="{y + cell - 6:.0f}" class="ops-heatmap__label" '
            f'font-family="var(--mono)" font-size="11" fill="var(--text-muted)">{_escape(rlabel)}</text>'
        )
        for ci, (value, tip) in enumerate(cells):
            x = label_col + ci * (cell + gap)
            v = max(0.0, min(1.0, float(value)))
            # Mix accent colour with elevation; alpha encodes intensity.
            alpha = 0.18 + 0.82 * v
            colour = f"rgba(232,93,117,{alpha:.2f})" if v > 0 else "var(--bg-elev-2)"
            parts.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="2" '
                f'fill="{colour}"><title>{_escape(tip)}</title></rect>'
            )
    aria = _escape(label or "heatmap")
    # `width` / `height` attributes pin the natural render size — the SVG would
    # otherwise scale to fill the parent container (CSS `width: 100%` default
    # behaviour) and the cells become huge on desktop. We still keep viewBox
    # so the SVG remains responsive when the parent is narrower than `width`.
    return (
        f'<svg class="ops-heatmap" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        f'role="img" aria-label="{aria}">{"".join(parts)}</svg>'
    )


_MODEL_PALETTE: list[str] = [
    "#e85d75", "#79c0ff", "#56d364", "#ffd866", "#d2a8ff",
    "#ff9b6b", "#56b3d3", "#bd9bff", "#9bdc4d",
]


def _ops_color_for_model(name: str, assigned: dict[str, str]) -> str:
    """Stable palette assignment; 'unknown' always renders muted."""
    key = (name or "").strip()
    if not key or key.lower() in ("unknown", "—"):
        return "var(--text-muted)"
    if key in assigned:
        return assigned[key]
    colour = _MODEL_PALETTE[len(assigned) % len(_MODEL_PALETTE)]
    assigned[key] = colour
    return colour


def _ops_pill(text: str, *, kind: str = "neutral") -> str:
    return f'<span class="ops-pill ops-pill--{kind}">{_escape(text)}</span>'


def render_ops_page(
    run_log: dict[str, Any] | None,
    sources: list[dict[str, Any]] | None,
    *,
    prefix: str,
    site_url: str,
    cachebust: str,
    canonical: str,
) -> str:
    """Operations dashboard.

    Reads from `state/run_log.json` and `sources/sources.json`. Renders KPI
    tiles, charts (inline SVG, no JS), per-run tables, sub-agent telemetry,
    verification breakdown, and a stale-source watch list. Every visualisation
    degrades gracefully when the underlying data is missing — the agent's
    sparse-record consequence is visible as "no data" rather than blank panels.
    """
    all_runs = list((run_log or {}).get("runs") or [])
    # Newest first for the table; chronological for the time-series charts.
    runs_desc = list(reversed(all_runs))[:30]
    runs_asc = list(reversed(runs_desc))

    daily_runs = [r for r in runs_desc if r.get("kind", "daily") != "weekly"]
    weekly_runs = [r for r in runs_desc if r.get("kind") == "weekly"]
    today = datetime.now(timezone.utc).date()

    # ----- KPI computation --------------------------------------------------
    total_runs = len(all_runs)
    last_run = all_runs[-1] if all_runs else None
    last_run_date = last_run.get("date") if last_run else None
    days_since_last = -1
    if last_run_date and re.match(r"^\d{4}-\d{2}-\d{2}$", last_run_date):
        try:
            days_since_last = (today - datetime.strptime(last_run_date, "%Y-%m-%d").date()).days
        except ValueError:
            days_since_last = -1

    durations = [r.get("duration_seconds") or 0 for r in runs_desc if r.get("duration_seconds")]
    avg_duration = sum(durations) / len(durations) if durations else 0
    items_published = [r.get("items_published") or 0 for r in runs_desc if r.get("items_published") is not None]
    avg_items = sum(items_published) / len(items_published) if items_published else 0
    total_items = sum(items_published)

    # Verification cleanliness: iterations == 1 AND residual == 0 ⇒ clean publish.
    clean_runs = sum(
        1 for r in runs_desc
        if (r.get("verification_iterations") or 0) == 1
        and (r.get("verification_residual_count") or 0) == 0
    )
    rated_runs = sum(1 for r in runs_desc if r.get("verification_iterations") is not None)
    clean_rate = (clean_runs / rated_runs * 100) if rated_runs else None

    # Aggregate failure / stall counts across the window.
    total_failures = sum(len(r.get("fetch_failures") or []) for r in runs_desc)
    stalled_subagents = 0
    sub_agent_returns = 0
    for r in runs_desc:
        for a in (r.get("sub_agents") or {}).values():
            if not isinstance(a, dict):
                continue
            sub_agent_returns += 1
            if a.get("returned") is False:
                stalled_subagents += 1

    # Distinct models across main agent + sub-agents + verifiers.
    distinct_models: set[str] = set()
    for r in runs_desc:
        m = r.get("model")
        if isinstance(m, str) and m and m.lower() != "unknown":
            distinct_models.add(m)
        for a in (r.get("sub_agents") or {}).values():
            if not isinstance(a, dict):
                continue
            am = a.get("model")
            if isinstance(am, str) and am and am.lower() != "unknown":
                distinct_models.add(am)
        for it in ((r.get("verification") or {}).get("iterations") or []):
            if isinstance(it, dict):
                vm = it.get("model")
                if isinstance(vm, str) and vm and vm.lower() != "unknown":
                    distinct_models.add(vm)

    # ----- Sparkline series (chronological order) ---------------------------
    duration_series = [r.get("duration_seconds") or 0 for r in runs_asc]
    items_series = [r.get("items_published") or 0 for r in runs_asc]
    failures_series = [len(r.get("fetch_failures") or []) for r in runs_asc]

    # Verification stacks: clean (green) + needs_fixes (yellow) + residuals (red).
    verification_stacks: list[list[tuple[float, str]]] = []
    for r in runs_asc:
        clean = 1 if (r.get("verification_iterations") or 0) == 1 and not (r.get("verification_residual_count") or 0) else 0
        needs = max(0, (r.get("verification_iterations") or 0) - 1)
        residuals = r.get("verification_residual_count") or 0
        verification_stacks.append([
            (clean, "var(--ok)"),
            (needs, "var(--warn)"),
            (residuals, "var(--crit)"),
        ])

    # ----- Model distribution (donut) --------------------------------------
    model_role_counts: dict[str, dict[str, int]] = {}  # model → {main, research, verify}
    palette: dict[str, str] = {}

    def _bump(role: str, name: str | None) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            return
        bucket = model_role_counts.setdefault(name.strip(), {"main": 0, "research": 0, "verify": 0})
        bucket[role] += 1

    for r in runs_desc:
        _bump("main", r.get("model"))
        for a in (r.get("sub_agents") or {}).values():
            if isinstance(a, dict):
                _bump("research", a.get("model"))
        for it in ((r.get("verification") or {}).get("iterations") or []):
            if isinstance(it, dict):
                _bump("verify", it.get("model"))

    donut_slices: list[tuple[str, float, str]] = []
    for name, roles in sorted(model_role_counts.items(), key=lambda kv: -sum(kv[1].values())):
        total = sum(roles.values())
        donut_slices.append((name, total, _ops_color_for_model(name, palette)))
    donut_html = _ops_svg_donut(donut_slices, size=130, label="Model distribution") if donut_slices else \
        '<p class="muted">No model data recorded yet.</p>'

    role_table_rows: list[str] = []
    for name, roles in sorted(model_role_counts.items(), key=lambda kv: -sum(kv[1].values())):
        colour = _ops_color_for_model(name, palette)
        total = sum(roles.values())
        role_table_rows.append(
            '<tr>'
            f'<td><span class="ops-legend__swatch" style="background:{colour}"></span> {_escape(name)}</td>'
            f'<td class="mono">{roles["main"]}</td>'
            f'<td class="mono">{roles["research"]}</td>'
            f'<td class="mono">{roles["verify"]}</td>'
            f'<td class="mono"><strong>{total}</strong></td>'
            '</tr>'
        )
    if role_table_rows:
        models_table_html = (
            '<table class="data ops-models-table">'
            '<thead><tr><th>Model</th><th>Main</th><th>Research</th><th>Verify</th><th>Total</th></tr></thead>'
            '<tbody>' + "".join(role_table_rows) + '</tbody></table>'
        )
    else:
        models_table_html = ""

    # ----- Sub-agent allocation heatmap ------------------------------------
    sa_keys = ["S1", "S2", "S3", "S4", "W1", "W2"]
    heatmap_rows: list[tuple[str, list[tuple[float, str]]]] = []
    for k in sa_keys:
        cells: list[tuple[float, str]] = []
        present = False
        for r in runs_asc:
            a = (r.get("sub_agents") or {}).get(k)
            if not isinstance(a, dict):
                cells.append((0.0, f"{r.get('date','?')} {k}: not in this run"))
                continue
            present = True
            if a.get("returned") is False:
                cells.append((0.0, f"{r.get('date','?')} {k}: stalled"))
                continue
            attempted = len(a.get("sources_attempted") or [])
            used = len(a.get("sources_used") or [])
            ratio = (used / attempted) if attempted else 0.0
            cells.append((ratio, f"{r.get('date','?')} {k}: {used}/{attempted} sources used, {a.get('items_returned', 0)} items"))
        if present:
            heatmap_rows.append((k, cells))
    heatmap_html = _ops_svg_heatmap(heatmap_rows, cell=14, gap=2, label="Sub-agent fetch density (used/attempted)") \
        if heatmap_rows else '<p class="muted">No sub-agent allocation recorded yet.</p>'

    # ----- Latest run deep panel -------------------------------------------
    latest_panel_html = _ops_render_latest_run_panel(last_run, palette, prefix=prefix) \
        if last_run else '<p class="muted">No runs recorded yet.</p>'

    # ----- Verification iteration timeline ---------------------------------
    iter_rows: list[str] = []
    for r in list(reversed(runs_desc))[-10:][::-1]:
        iters = ((r.get("verification") or {}).get("iterations") or [])
        if not iters:
            continue
        for it in iters:
            if not isinstance(it, dict):
                continue
            verdict = it.get("verdict", "?")
            kind = "ok" if verdict == "CLEAN" else ("warn" if verdict == "NEEDS_FIXES" else "neutral")
            mname = it.get("model") or "unknown"
            colour = _ops_color_for_model(mname, palette)
            counts = (
                f'truth {it.get("truth", 0)} · '
                f'editorial {it.get("editorial", 0)} · '
                f'advisory {it.get("advisory", 0)}'
            )
            tele = it.get("telemetry") or {}
            tele_bits: list[str] = []
            if tele.get("urls_checked"):
                tele_bits.append(f'{tele["urls_checked"]} URLs')
            if tele.get("duration_seconds"):
                tele_bits.append(_ops_format_duration(tele["duration_seconds"]))
            tele_str = " · ".join(tele_bits)
            iter_rows.append(
                '<tr>'
                f'<td class="mono"><a href="{prefix}briefs/{_escape(r.get("date", ""))}/">{_escape(r.get("date", ""))}</a></td>'
                f'<td class="mono">#{int(it.get("n", 0)) if isinstance(it.get("n"), int) else "?"}</td>'
                f'<td>{_ops_pill(verdict, kind=kind)}</td>'
                f'<td><span class="ops-legend__swatch" style="background:{colour}"></span>'
                f' <span class="mono">{_escape(mname)}</span></td>'
                f'<td class="mono muted">{_escape(counts)}</td>'
                f'<td class="mono muted">{_escape(tele_str)}</td>'
                '</tr>'
            )
    if iter_rows:
        verif_table_html = (
            '<div class="data-wrap"><table class="data">'
            '<thead><tr><th>Date</th><th>Iter</th><th>Verdict</th>'
            '<th>Verifier model</th><th>Findings</th><th>Telemetry</th></tr></thead>'
            '<tbody>' + "".join(iter_rows) + '</tbody></table></div>'
        )
    else:
        verif_table_html = '<p class="muted">No per-iteration verification records yet (v2.43+).</p>'

    # ----- Recent runs table ------------------------------------------------
    runs_table_html = _ops_render_runs_table(runs_desc, palette, prefix=prefix)

    # ----- Stale active sources --------------------------------------------
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

    # ----- KPI tiles --------------------------------------------------------
    last_run_label = _escape(last_run_date or "—")
    if days_since_last >= 0:
        last_run_label += f' <span class="muted ops-kpi__delta">({days_since_last}d ago)</span>'
    clean_rate_str = f"{clean_rate:.0f}%" if clean_rate is not None else "—"
    clean_rate_sub = f"{clean_runs}/{rated_runs} clean publish" if rated_runs else "no telemetry yet"
    distinct_models_str = str(len(distinct_models)) if distinct_models else "—"
    distinct_models_sub = ", ".join(sorted(distinct_models)[:3]) if distinct_models else "no model recorded"

    kpi_tiles = (
        '<div class="ops-kpi-grid">'
        + _ops_kpi_tile("Total runs (window)", str(min(total_runs, len(runs_desc))),
                        sub=f"{len(daily_runs)} daily · {len(weekly_runs)} weekly",
                        chart=_ops_svg_bars([1] * len(runs_desc) if runs_desc else [],
                                              width=140, height=28,
                                              color="var(--accent)", track="var(--bg)",
                                              label="Run cadence"))
        + _ops_kpi_tile("Avg duration",
                        _ops_format_duration(avg_duration),
                        sub=f"min {_ops_format_duration(min(durations) if durations else 0)} · "
                            f"max {_ops_format_duration(max(durations) if durations else 0)}",
                        chart=_ops_svg_sparkline(duration_series, width=140, height=28,
                                                  stroke="var(--info)", fill="rgba(121,192,255,0.2)",
                                                  label="Run duration over time"))
        + _ops_kpi_tile("Items published",
                        str(total_items),
                        sub=f"avg {avg_items:.1f} per run",
                        chart=_ops_svg_bars(items_series, width=140, height=28,
                                              color="var(--ok)",
                                              label="Items per run"))
        + _ops_kpi_tile("Verification clean-rate", clean_rate_str, sub=clean_rate_sub,
                        chart=_ops_svg_stacked_bars(verification_stacks, width=140, height=28,
                                                      label="Verification verdicts"))
        + _ops_kpi_tile("Sub-agent stalls", str(stalled_subagents),
                        sub=f"out of {sub_agent_returns} returns",
                        kind=("crit" if stalled_subagents > 0 else "ok"),
                        chart=_ops_svg_bars(failures_series, width=140, height=28,
                                              color="var(--warn)",
                                              label="Fetch failures over time"))
        + _ops_kpi_tile("Last run", last_run_label,
                        sub=f"{total_failures} fetch failure{'s' if total_failures != 1 else ''} in window",
                        kind=("warn" if days_since_last > 1 else "neutral"))
        + _ops_kpi_tile("Distinct models", distinct_models_str, sub=distinct_models_sub)
        + '</div>'
    )

    body = f"""
<h1>Operations</h1>
<p class="subtitle">Live telemetry from <code>state/run_log.json</code> (per-run sub-agent allocation, model split, verification verdicts, fetch failures, wall-clock duration) and <code>sources/sources.json</code> (last-successful-fetch timestamps). Last {len(runs_desc)} run{'' if len(runs_desc) == 1 else 's'} shown.</p>

{kpi_tiles}

<section class="ops-section">
  <h2 class="section-head">Latest run</h2>
  {latest_panel_html}
</section>

<section class="ops-section">
  <h2 class="section-head">Models in use</h2>
  <p class="subtitle ops-subtitle">Distinct Claude models that signed work in this window — main agent, research sub-agents, verification sub-agents. Tracking the split lets you spot runs where the runtime config changed and runs where a sub-agent forgot to self-identify.</p>
  <div class="ops-models">
    <div class="ops-models__chart">{donut_html}</div>
    <div class="ops-models__table">{models_table_html}</div>
  </div>
</section>

<section class="ops-section">
  <h2 class="section-head">Sub-agent fetch density</h2>
  <p class="subtitle ops-subtitle">Each cell is one run × one sub-agent. Intensity = used / attempted source ratio. Empty rows = sub-agent not in this routine (S1–S4 daily, W1–W2 weekly). White cells = stalled or absent.</p>
  <div class="ops-heatmap-wrap">{heatmap_html}</div>
</section>

<section class="ops-section">
  <h2 class="section-head">Verification iterations</h2>
  <p class="subtitle ops-subtitle">Per-iteration verdicts and verifier-model assignments for the last 10 runs that recorded the v2.43+ <code>verification.iterations[]</code> block. Truth findings (F1–F4) get fresh re-research; editorial (F5–F10) get inline edits; advisory (F11) are typically ignored.</p>
  {verif_table_html}
</section>

<section class="ops-section">
  <h2 class="section-head">Recent runs</h2>
  {runs_table_html}
</section>

<section class="ops-section">
  <h2 class="section-head">Stale active sources (&gt;7 days since last successful fetch)</h2>
  {stale_html}
</section>

<p class="muted ops-footnote">
  See <a href="{prefix}about/docs/architecture/">Architecture</a> for how the run log is produced. Per-agent self-identification is documented in <a href="{prefix}about/prompts/daily-cti-brief/">prompts/daily-cti-brief.md</a> § Self-identification.
</p>
"""
    return base_template(
        title="Operations dashboard — ctipilot.ch",
        description="Live agent telemetry: run cadence, durations, model split, sub-agent allocation, verification verdicts, fetch failures, source-rotation health.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def _ops_kpi_tile(label: str, value: str, *, sub: str = "", kind: str = "neutral",
                   chart: str = "") -> str:
    """One KPI tile. `value` may contain HTML (e.g. embedded muted span)."""
    sub_html = f'<div class="ops-kpi__sub">{_escape(sub)}</div>' if sub else ""
    chart_html = f'<div class="ops-kpi__chart">{chart}</div>' if chart else ""
    return (
        f'<div class="ops-kpi ops-kpi--{kind}">'
        f'<div class="ops-kpi__label">{_escape(label)}</div>'
        f'<div class="ops-kpi__value">{value}</div>'
        f'{sub_html}'
        f'{chart_html}'
        f'</div>'
    )


def _ops_render_latest_run_panel(run: dict[str, Any], palette: dict[str, str], *,
                                   prefix: str) -> str:
    """Detailed panel for the most recent run — main-agent model, every
    sub-agent's contribution + telemetry, verification roll-up. The 'one
    glance, full picture' card."""
    date = run.get("date") or "?"
    kind = run.get("kind", "daily")
    main_name = run.get("model") or "unknown"
    main_id = run.get("model_id") or ""
    main_colour = _ops_color_for_model(main_name, palette)
    pv = (run.get("prompt_version") or "?").lstrip("v")
    duration = _ops_format_duration(run.get("duration_seconds"))
    items_pub = run.get("items_published")
    items_pub_str = str(items_pub) if items_pub is not None else "—"
    deep_dive = run.get("deep_dive") or "—"
    failures = run.get("fetch_failures") or []

    # Sub-agent cards.
    sub_keys_for_kind = ("W1", "W2") if kind == "weekly" else ("S1", "S2", "S3", "S4")
    sa_cards: list[str] = []
    for k in sub_keys_for_kind:
        a = (run.get("sub_agents") or {}).get(k) or {}
        sa_cards.append(_ops_render_subagent_card(k, a, palette))
    sa_grid = f'<div class="ops-sa-grid">{"".join(sa_cards)}</div>'

    # Failures.
    if failures:
        chips = "".join(
            f'<span class="ops-pill ops-pill--warn">{_escape(f.get("id", "?"))} '
            f'<span class="muted">{_escape(str(f.get("code", f.get("status", ""))))}</span></span>'
            for f in failures
        )
        failures_html = f'<div class="ops-chip-row">{chips}</div>'
    else:
        failures_html = '<p class="muted">No fetch failures recorded.</p>'

    # Verification summary
    iters = ((run.get("verification") or {}).get("iterations") or [])
    if iters:
        v_chips = "".join(
            f'<span class="ops-pill ops-pill--{("ok" if it.get("verdict") == "CLEAN" else "warn")}">'
            f'#{_escape(str(it.get("n", "?")))} {_escape(it.get("verdict", "?"))} '
            f'<span class="muted">· {_escape(it.get("model", "unknown"))}</span>'
            '</span>'
            for it in iters if isinstance(it, dict)
        )
        verif_html = f'<div class="ops-chip-row">{v_chips}</div>'
    else:
        vi = run.get("verification_iterations")
        vr = run.get("verification_residual_count")
        if vi is not None:
            verif_html = (
                f'<p class="muted">{vi} iteration{"s" if (vi or 0) != 1 else ""} · '
                f'{vr or 0} residual{"s" if (vr or 0) != 1 else ""} '
                '(legacy scalar — per-iteration breakdown not recorded)</p>'
            )
        else:
            verif_html = '<p class="muted">No verification telemetry recorded.</p>'

    return f"""
<div class="ops-latest">
  <div class="ops-latest__head">
    <div>
      <a class="ops-latest__date mono" href="{prefix}briefs/{_escape(date)}/">{_escape(date)}</a>
      <span class="ops-pill ops-pill--neutral">{_escape(kind)}</span>
      <span class="ops-pill ops-pill--accent">prompt v{_escape(pv)}</span>
    </div>
    <div class="ops-latest__meta">
      <span class="mono">{_escape(duration)}</span>
      <span class="muted">duration</span>
      <span class="mono">{_escape(items_pub_str)}</span>
      <span class="muted">items</span>
    </div>
  </div>
  <div class="ops-latest__main">
    <span class="ops-legend__swatch" style="background:{main_colour}"></span>
    <span class="mono"><strong>{_escape(main_name)}</strong></span>
    {f'<span class="mono muted">({_escape(main_id)})</span>' if main_id else ''}
    <span class="muted">main agent</span>
  </div>
  {sa_grid}
  <div class="ops-latest__row">
    <div>
      <h3 class="ops-mini-head">Verification</h3>
      {verif_html}
    </div>
    <div>
      <h3 class="ops-mini-head">Fetch failures</h3>
      {failures_html}
    </div>
    <div>
      <h3 class="ops-mini-head">Deep dive</h3>
      <p class="mono ops-deep">{_escape(deep_dive)}</p>
    </div>
  </div>
</div>
"""


def _ops_render_subagent_card(key: str, data: dict[str, Any], palette: dict[str, str]) -> str:
    if not data:
        return (
            f'<div class="ops-sa-card ops-sa-card--missing">'
            f'<div class="ops-sa-card__head"><strong>{_escape(key)}</strong>'
            ' <span class="ops-pill ops-pill--neutral">absent</span></div>'
            '<p class="muted">No record for this sub-agent.</p>'
            '</div>'
        )
    if data.get("returned") is False:
        model_name = data.get("model") or "unknown"
        return (
            f'<div class="ops-sa-card ops-sa-card--stalled">'
            f'<div class="ops-sa-card__head"><strong>{_escape(key)}</strong>'
            ' <span class="ops-pill ops-pill--crit">stalled</span></div>'
            f'<p class="muted mono">{_escape(model_name)}</p>'
            '<p class="muted">Past 10-min wall-clock budget; abandoned.</p>'
            '</div>'
        )

    model_name = data.get("model") or "unknown"
    model_id = data.get("model_id") or ""
    colour = _ops_color_for_model(model_name, palette)
    used = len(data.get("sources_used") or [])
    attempted = len(data.get("sources_attempted") or [])
    items = data.get("items_returned") or 0
    tele = data.get("telemetry") or {}

    def _t(name: str) -> str:
        v = tele.get(name)
        if v is None or v == "":
            return ""
        return f'<span class="ops-sa-card__tele-item"><span class="mono">{_escape(str(v))}</span> <span class="muted">{_escape(name.replace("_", " "))}</span></span>'

    tele_html = "".join(_t(n) for n in ("duration_seconds", "webfetch_calls", "websearch_calls", "bridge_fetches", "tokens_in", "tokens_out", "urls_checked"))
    if tele_html:
        tele_block = f'<div class="ops-sa-card__tele">{tele_html}</div>'
    else:
        tele_block = '<p class="muted ops-sa-card__tele-empty">No self-telemetry reported.</p>'

    used_pct = int((used / attempted) * 100) if attempted else 0
    bar = (
        '<div class="ops-sa-card__bar">'
        f'<div class="ops-sa-card__bar-fill" style="width:{used_pct}%"></div>'
        '</div>'
    )

    return f"""
<div class="ops-sa-card">
  <div class="ops-sa-card__head">
    <strong>{_escape(key)}</strong>
    <span class="ops-legend__swatch" style="background:{colour}"></span>
    <span class="mono">{_escape(model_name)}</span>
    {f'<span class="mono muted">({_escape(model_id)})</span>' if model_id else ''}
  </div>
  <div class="ops-sa-card__stats">
    <div><span class="mono">{items}</span><span class="muted"> items</span></div>
    <div><span class="mono">{used}/{attempted}</span><span class="muted"> sources</span></div>
  </div>
  {bar}
  {tele_block}
</div>
"""


def _ops_render_runs_table(runs: list[dict[str, Any]], palette: dict[str, str], *,
                            prefix: str) -> str:
    if not runs:
        return (
            '<div class="empty">'
            '<p>No <code>state/run_log.json</code> yet.</p>'
            '<p class="muted">The agent populates this file at the end of every run (Phase 5). The first scheduled run after the v2 prompt change will create it.</p>'
            '</div>'
        )

    def _sa_cell(a: dict[str, Any] | None) -> str:
        if not a:
            return '<span class="muted">—</span>'
        if a.get("returned") is False:
            return '<span class="ops-pill ops-pill--crit">stalled</span>'
        used = len(a.get("sources_used") or [])
        attempted = len(a.get("sources_attempted") or [])
        items = a.get("items_returned") or 0
        m = a.get("model") or ""
        colour = _ops_color_for_model(m, palette) if m else "var(--text-muted)"
        return (
            f'<span class="ops-legend__swatch" style="background:{colour}" '
            f'title="{_escape(m or "unknown")}"></span>'
            f' <span class="mono">{items}</span>'
            f'<span class="muted"> ({used}/{attempted})</span>'
        )

    rows: list[str] = []
    for r in runs:
        sa = r.get("sub_agents") or {}
        kind = r.get("kind", "daily")
        keys = ("W1", "W2") if kind == "weekly" else ("S1", "S2", "S3", "S4")
        cells = "".join(f'<td>{_sa_cell(sa.get(k))}</td>' for k in keys)
        # Pad weekly rows out to four sub-agent columns so columns align.
        if kind == "weekly":
            cells += '<td><span class="muted">—</span></td><td><span class="muted">—</span></td>'
        failures = len(r.get("fetch_failures") or [])
        failures_html = (
            f'<span class="ops-pill ops-pill--warn">{failures}</span>'
            if failures
            else '<span class="muted">0</span>'
        )
        main_name = r.get("model") or "unknown"
        main_colour = _ops_color_for_model(main_name, palette)
        verif_iters = r.get("verification_iterations")
        verif_residual = r.get("verification_residual_count") or 0
        if verif_iters is None:
            verif_html = '<span class="muted">—</span>'
        elif verif_residual:
            verif_html = (
                f'<span class="ops-pill ops-pill--crit" '
                f'title="{verif_iters} iteration(s); {verif_residual} unresolved finding(s)">'
                f'{verif_iters}↻ · {verif_residual}r</span>'
            )
        elif verif_iters > 1:
            verif_html = (
                f'<span class="ops-pill ops-pill--warn" '
                f'title="{verif_iters} iteration(s); cleaned up">'
                f'{verif_iters}↻</span>'
            )
        else:
            verif_html = '<span class="ops-pill ops-pill--ok">clean</span>'
        duration = _ops_format_duration(r.get("duration_seconds"))
        items_pub = r.get("items_published")
        items_pub_str = str(items_pub) if items_pub is not None else "—"

        rows.append(
            '<tr>'
            f'<td class="mono"><a href="{prefix}briefs/{_escape(r.get("date", ""))}/">{_escape(r.get("date", ""))}</a></td>'
            f'<td><span class="ops-pill ops-pill--neutral">{_escape(kind)}</span></td>'
            f'<td><span class="ops-legend__swatch" style="background:{main_colour}"></span>'
            f' <span class="mono">{_escape(main_name)}</span></td>'
            f'<td class="mono muted">v{_escape(str(r.get("prompt_version", "?")).lstrip("v"))}</td>'
            f'<td class="mono">{_escape(duration)}</td>'
            f'<td class="mono">{_escape(items_pub_str)}</td>'
            f'{cells}'
            f'<td>{failures_html}</td>'
            f'<td>{verif_html}</td>'
            '</tr>'
        )

    return (
        '<div class="data-wrap"><table class="data ops-runs-table">'
        '<thead><tr><th>Date</th><th>Kind</th><th>Main model</th><th>Prompt</th><th>Duration</th>'
        '<th>Items</th><th>S1/W1</th><th>S2/W2</th><th>S3</th><th>S4</th>'
        '<th>Fetch fail</th><th>Verif</th></tr></thead>'
        '<tbody>' + "".join(rows) + '</tbody></table></div>'
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


_DOCTYPE_RE = re.compile(r"<!\s*DOCTYPE\b", re.IGNORECASE)
_ENTITY_DECL_RE = re.compile(r"<!\s*ENTITY\b", re.IGNORECASE)


def _xml_validate(content: str) -> list[str]:
    """Sanity-parse the build's own RSS output. The input is XML the build
    generated from already-escaped data, but the parser is configured
    defensively so any future change that pipes untrusted XML through this
    function cannot trigger XXE / billion-laughs.

    Defense layers:
      1. Refuse any document that contains a `<!DOCTYPE …>` or `<!ENTITY
         …>` declaration. The build's own RSS feeds never declare a
         DOCTYPE, so this is a no-cost rejection that blocks both
         billion-laughs (which requires nested entity declarations) and
         classic XXE (which requires a DOCTYPE).
      2. Use stdlib `xml.etree.ElementTree.fromstring` for well-formedness
         parsing. Python 3.7.1+ stdlib does not load external DTDs by
         default; combined with rule (1), no external entity reference
         can be triggered.
    """
    if _DOCTYPE_RE.search(content) or _ENTITY_DECL_RE.search(content):
        return ["refused: DOCTYPE / ENTITY declarations not permitted in feed XML"]
    # The pre-filter above blocks DOCTYPE and ENTITY declarations, so the
    # parse below cannot trigger XXE or billion-laughs. Bandit's B314
    # rule warns about ET.fromstring on untrusted input; the input here
    # is sanitised, so we suppress the warning.
    try:
        ET.fromstring(content)  # nosec B314
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
        title="ctipilot.ch — Daily (Switzerland, Europe & Public Sector)",
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
        title="ctipilot.ch — Weekly (Switzerland, Europe & Public Sector)",
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
                url = f"{site_url}{_brief_url_path(b)}{slug}/"
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
            f'<guid isPermaLink="true">{_escape(it["url"])}</guid>'
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
        title="ctipilot.ch — Per item",
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
        # Belt-and-braces size cap on every asset. Vendored JS lives in
        # site/assets/vendor/ and is also covered by the SHA-256 + SHA-384
        # check; the size cap here is the cheaper first check.
        size = src_path.stat().st_size
        if src_path.parent.name == "vendor" and size > MAX_VENDOR_BYTES:
            raise RuntimeError(
                f"refused: vendor asset {src_path} is {size} bytes, "
                f"exceeds cap of {MAX_VENDOR_BYTES}"
            )
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


def write_security_txt(out_path: Path, *, repo: str, expires: str) -> None:
    """RFC 9116 security.txt. Routes reports through GitHub Private
    Vulnerability Reporting so we never need to publish a contact email."""
    body = (
        f"# Report a vulnerability privately via GitHub PVR:\n"
        f"#   https://github.com/{repo}/security/advisories/new\n"
        f"# Repo Settings -> Code security -> Private vulnerability reporting\n"
        f"# must be enabled for the link above to accept submissions.\n"
        f"Contact: https://github.com/{repo}/security/advisories/new\n"
        f"Expires: {expires}\n"
        f"Preferred-Languages: en\n"
        f"Canonical: https://ctipilot.ch/.well-known/security.txt\n"
    )
    atomic_write_text(out_path, body)


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

    # No known-shape secret tokens in any emitted file. Last-line guard
    # against the autonomous agent accidentally pasting an env var or
    # credential into a brief / docs / state file: failing the build is
    # always preferable to silently propagating a secret to gh-pages and
    # the RSS feeds.
    for path in list(OUT.rglob("*.html")) + list(OUT.rglob("*.xml")) + list(OUT.rglob("*.md")) + list(OUT.rglob("*.json")) + list(OUT.rglob("*.txt")):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        hits = scan_for_secrets(text)
        for label, sample in hits:
            errors.append(
                f"secret-shaped token in {path.relative_to(OUT)}: {label} ({sample})"
            )
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
    # Each state file is read through `_read_text_capped` so a poisoned
    # state JSON (e.g. an agent that wrote 200 MB of garbage) cannot
    # OOM the build. Caps are loose vs. real on-disk sizes.
    cves_raw = json.loads(
        _read_text_capped(ROOT / "state" / "cves_seen.json", MAX_STATE_BYTES)
    )
    topics_raw = json.loads(
        _read_text_capped(ROOT / "state" / "covered_items.json", MAX_STATE_BYTES)
    )
    sources_raw = json.loads(
        _read_text_capped(ROOT / "sources" / "sources.json", MAX_STATE_BYTES)
    )

    # Total briefs/ tree size guard — defends against a flood of small
    # poisoned files that individually pass the per-file cap.
    if (ROOT / "briefs").exists():
        total_briefs = sum(
            p.stat().st_size for p in (ROOT / "briefs").rglob("*") if p.is_file()
        )
        if total_briefs > MAX_BRIEFS_DIR_BYTES:
            print(
                f"error: briefs/ tree is {total_briefs} bytes, exceeds cap of {MAX_BRIEFS_DIR_BYTES}",
                file=sys.stderr,
            )
            return 5

    sources = annotate_sources(sources_raw, briefs)
    cves = annotate_cves(cves_raw, briefs, sources)
    topics = annotate_topics(topics_raw, briefs, sources)

    manifest_pages: dict[str, dict[str, Any]] = {}
    sitemap: list[tuple[str, str]] = []  # (loc, lastmod)

    def emit_html(rel_url: str, html: str, *, lastmod: str = "") -> None:
        """`rel_url` looks like 'briefs/2026-05-07/' or '' for home. The
        path on disk becomes `<rel_url>index.html`, with percent-encoded
        characters decoded back to their literal form (so a URL like
        `/topics/incident%3Afoo/` is served from `topics/incident:foo/`,
        not from a directory whose name literally contains `%3A`).
        GitHub Pages decodes `%3A` → `:` before file lookup, so the disk
        layout MUST use the decoded form or every topic page 404s."""
        rel_path = rel_url + "index.html" if rel_url.endswith("/") or rel_url == "" else rel_url
        if rel_url == "":
            rel_path = "index.html"
        # Decode the URL form for the filesystem. is_safe_path_segment
        # already restricts raw IDs to alnum + `:._-`, so the only
        # `%`-encodings that survive `urllib.parse.quote(safe='')` are
        # for `:` (→ `%3A`); decoding can never reintroduce `/` or `..`.
        fs_path = urllib.parse.unquote(rel_path)
        out_path = OUT / fs_path
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
        manifest_pages[rel_url or "/"] = {"path": fs_path, "hash": h}
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

    items_index: dict[str, dict[str, Any]] = {}  # "<brief>/<slug>" -> {item, brief}
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
                # Key by (brief, slug). With items emitted under
                # /briefs/<date>/<slug>/, two briefs can each carry an
                # item whose heading slugifies the same way without
                # colliding. The composite key keeps both reachable.
                ib_key = f"{b['name']}/{slug}"
                items_index[ib_key] = {"item": it, "brief": b}
                tag_region_entry = {
                    "slug": slug,
                    "title": it["heading"],
                    "brief": b["name"],
                    "kind": b["kind"],
                    "publish_ts": b["publish_ts"],
                }
                for t in it["footer"].get("tags", []):
                    tag_index[t].append(tag_region_entry)
                for r in it["footer"].get("regions", []):
                    region_index[r].append(tag_region_entry)

        # Also write the raw .md for any reader that wants it.
        md_dir = OUT / ("briefs/weekly/" if b["kind"] == "weekly" else "briefs/")
        atomic_write_text(md_dir / (b["name"] + ".md"), b["text"])

    # ---- CVE → items + Topic → items indexes -------------------------
    # The CVE and Topic detail pages used to be a thin appearance list.
    # Now that we've already parsed every item from every brief, we can
    # embed the full body of each matching item directly on the CVE /
    # Topic page so a reader hitting `/cves/CVE-…/` sees the actual
    # writeups instead of just a list of brief dates. The match rules:
    # CVE — split the item footer's `cve` field on commas and bucket the
    # item under every CVE id it covers.  Topic — for each topic, build
    # a phrase from the topic's title (its first segment before " — " /
    # " – " / ": "), case-fold both heading and topic phrase, and match
    # when the phrase is in the item's heading; CVE-typed topics also
    # match when the topic's key equals one of the item's footer CVEs.
    # An item may match multiple CVEs and/or multiple topics.
    items_by_cve: dict[str, list[dict[str, Any]]] = defaultdict(list)
    items_by_topic: dict[str, list[dict[str, Any]]] = defaultdict(list)

    topic_match_specs: list[dict[str, Any]] = []
    for tp in topics["items"]:
        ttype = (tp.get("type") or "").lower()
        title = (tp.get("title") or "").strip()
        for sep in (" — ", " – ", ": "):
            if sep in title:
                title = title.split(sep, 1)[0]
                break
        phrase = title.strip().lower()
        topic_match_specs.append({
            "key": tp["key"],
            "phrase": phrase,
            "cve_id": tp["key"].upper() if ttype == "cve" else None,
        })

    for ib_key, entry in items_index.items():
        it = entry["item"]
        item_record = {"item": it, "brief": entry["brief"]}
        cve_field = (it.get("footer") or {}).get("cve") or ""
        item_cves = {
            cve_token.strip().upper()
            for cve_token in cve_field.split(",")
            if cve_token.strip() and CVE_RE.fullmatch(cve_token.strip())
        }
        for cve_id in item_cves:
            items_by_cve[cve_id].append(item_record)
        heading_lower = (it.get("heading") or "").lower()
        body_lower = (it.get("body_md") or "").lower()
        for spec in topic_match_specs:
            if spec["cve_id"] and spec["cve_id"] in item_cves:
                items_by_topic[spec["key"]].append(item_record)
                continue
            phrase = spec["phrase"]
            if phrase and len(phrase) >= 4 and (phrase in heading_lower or phrase in body_lower):
                items_by_topic[spec["key"]].append(item_record)

    # ---- Per-item pages -----------------------------------------------
    # Items live at /briefs/<date>/<slug>/ (or /briefs/weekly/<date>/<slug>/
    # for weekly summaries) so the URL itself reflects the parent brief —
    # readers can edit the URL in the address bar to jump back up the
    # hierarchy. Older builds emitted /items/<slug>/ which forced the
    # date prefix into the slug to keep slugs unique; the date is now in
    # the URL path, so the slug is just slugify(item_heading).
    for ib_key, entry in items_index.items():
        slug = entry["item"]["slug"]
        if not is_safe_path_segment(slug):
            print(f"warning: skipping item with unsafe slug {slug!r}", file=sys.stderr)
            continue
        rel_url = _brief_url_path(entry["brief"]) + slug + "/"
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
            matching_items=items_by_cve.get(c["id"], []),
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
            matching_items=items_by_topic.get(t["key"], []),
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
                f"{prefix}{('briefs/weekly/' if e.get('kind') == 'weekly' else 'briefs/')}{e['brief']}/{e['slug']}/",
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

    # /about/ — landing page with two clear sections (Documentation + Prompts).
    # Built from README.md plus a generated section-nav block prepended at the
    # top so the reader sees the two-column layout before scrolling into the
    # README content.
    readme = (
        _read_text_capped(ROOT / "README.md", MAX_BRIEF_BYTES)
        if (ROOT / "README.md").exists()
        else "# About"
    )
    docs_dir = ROOT / "docs"
    prompts_dir = ROOT / "prompts"
    docs_files = sorted(docs_dir.glob("*.md")) if docs_dir.exists() else []
    prompt_files = sorted(p for p in prompts_dir.glob("*.md") if p.name != "CHANGELOG.md") if prompts_dir.exists() else []
    about_landing_md = "# About\n\n"
    about_landing_md += "Two reading paths into how this project works.\n\n"
    about_landing_md += "## [Documentation](docs/)\n\n"
    about_landing_md += "System reference for operators, contributors, and curious readers. End-to-end map, runbook, privacy disclosure, open backlog.\n\n"
    for p in docs_files:
        title = p.stem.replace("-", " ").capitalize()
        about_landing_md += f"- [{title}](docs/{p.stem}.md)\n"
    about_landing_md += "\n## [Prompts](prompts/)\n\n"
    about_landing_md += "Everything the routine loads at runtime — the full text of the master prompts, the verification policy, the brief template, the check-brief fix recipes, and the version-history changelog.\n\n"
    for p in prompt_files:
        title = p.stem.replace("-", " ").capitalize()
        about_landing_md += f"- [{title}](prompts/{p.stem}.md)\n"
    about_landing_md += "- [Prompt CHANGELOG](prompts/CHANGELOG.md) — version-by-version evolution\n\n"
    about_landing_md += "---\n\n## README\n\n"
    about_landing_md += readme
    emit_html(
        "about/",
        render_static_doc(
            md_text=about_landing_md,
            title="About — ctipilot.ch",
            description="What this project is, how the briefs are produced, and how to read them.",
            prefix="../",
            canonical=site_url + "about/",
            site_url=site_url,
            cachebust=cachebust,
        ),
    )

    # /about/docs/ — index page listing every doc.
    if docs_files:
        docs_index_md = "# Documentation\n\nSystem reference for operators, contributors, and curious readers. Pure docs — none of the files here are loaded by the prompt at runtime (that material lives under [`prompts/`](../prompts/)).\n\n"
        for p in docs_files:
            title = p.stem.replace("-", " ").capitalize()
            docs_index_md += f"- [**{title}**](../docs/{p.stem}.md)\n"
        emit_html(
            "about/docs/",
            render_static_doc(
                md_text=docs_index_md,
                title="Documentation — ctipilot.ch",
                description="System reference: architecture, operating, analytics, improvements.",
                prefix="../../",
                canonical=site_url + "about/docs/",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )
        # /about/docs/<name>/ — each doc.
        for p in docs_files:
            rel_url = f"about/docs/{p.stem}/"
            title = p.stem.replace("-", " ").capitalize()
            emit_html(
                rel_url,
                render_static_doc(
                    md_text=_read_text_capped(p, MAX_BRIEF_BYTES),
                    title=f"{title} — ctipilot.ch",
                    description=f"{title} — system documentation.",
                    prefix="../../../",
                    canonical=site_url + rel_url,
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )

    # /about/prompts/ — index page listing every prompt + recent CHANGELOG headings.
    changelog_path = ROOT / "prompts" / "CHANGELOG.md"
    if prompt_files or changelog_path.exists():
        prompts_index_md = "# Prompts\n\nEverything the routine loads at runtime. The two master prompts (`daily-cti-brief.md`, `weekly-summary.md`) drive every run; the supporting files (`verification.md`, `brief-template.md`, `check-brief-fixes.md`) are read by the prompts at runtime as policy, template, and remediation guide.\n\n"
        if prompt_files:
            prompts_index_md += "## Prompts and runtime policies\n\n"
            for p in prompt_files:
                title = p.stem.replace("-", " ").capitalize()
                prompts_index_md += f"- [**{title}**](../prompts/{p.stem}.md)\n"
            prompts_index_md += "\n"
        prompts_index_md += "## Version history\n\n"
        prompts_index_md += "Every substantive prompt edit ships with a [CHANGELOG](../prompts/CHANGELOG.md) entry explaining *why* the editorial policy shifted between two committed briefs. Recent versions:\n\n"
        if changelog_path.exists():
            cl_text = changelog_path.read_text(encoding="utf-8", errors="replace")
            version_headings = re.findall(r"^## (\d+\.\d+ — \d{4}-\d{2}-\d{2}.*)$", cl_text, re.MULTILINE)
            for h in version_headings[:10]:
                prompts_index_md += f"- {h}\n"
            prompts_index_md += "\n[Full version history →](../prompts/CHANGELOG.md)\n"
        emit_html(
            "about/prompts/",
            render_static_doc(
                md_text=prompts_index_md,
                title="Prompts — ctipilot.ch",
                description="The prompts the routine loads at runtime, plus their version-history changelog.",
                prefix="../../",
                canonical=site_url + "about/prompts/",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )
        # /about/prompts/<name>/ — each prompt file.
        for p in prompt_files:
            rel_url = f"about/prompts/{p.stem}/"
            title = p.stem.replace("-", " ").capitalize()
            emit_html(
                rel_url,
                render_static_doc(
                    md_text=_read_text_capped(p, MAX_BRIEF_BYTES),
                    title=f"{title} — ctipilot.ch",
                    description=f"{title} — runtime prompt / policy.",
                    prefix="../../../",
                    canonical=site_url + rel_url,
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )
        # /about/prompts/changelog/ — full version history.
        if changelog_path.exists():
            emit_html(
                "about/prompts/changelog/",
                render_static_doc(
                    md_text=_read_text_capped(changelog_path, MAX_BRIEF_BYTES),
                    title="Prompt CHANGELOG — ctipilot.ch",
                    description="Editorial-policy audit trail — every prompt-version change explained.",
                    prefix="../../../",
                    canonical=site_url + "about/prompts/changelog/",
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
    # GitHub Pages serves this for any unknown path under the site, but the
    # browser's URL stays at the requested deep path (e.g.
    # `/cves/CVE-A,%20CVE-B/`). That means relative asset paths in the served
    # HTML resolve against the deep path and 404 in turn, leaving the page
    # unstyled. To survive any depth, the 404 uses *absolute* asset paths
    # derived from `site_url` — this is the one page in the build that needs
    # them.
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
    <a href="https://github.com/OwlsNightCatch/ctipilot/issues" target="_blank" rel="noopener noreferrer">github.com/OwlsNightCatch/ctipilot</a>.
  </p>
</section>
"""

    err = base_template(
        title="404 — Not found · ctipilot.ch",
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
    write_security_txt(
        OUT / ".well-known" / "security.txt",
        repo="OwlsNightCatch/ctipilot",
        expires="2027-05-08T00:00:00Z",
    )

    # ---- CNAME (GitHub Pages custom domain) ---------------------------
    # Routed through atomic_write_text so prune_orphans doesn't delete it.
    # Cap at 1 KB — CNAME is a single hostname; anything larger is junk
    # the build refuses to publish.
    cname_src = ROOT / "CNAME"
    if cname_src.exists():
        atomic_write_text(OUT / "CNAME", _read_text_capped(cname_src, 1024))

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
