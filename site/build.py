#!/usr/bin/env python3
"""Build the static-site bundle for GitHub Pages (CTI pipeline v3 SSG).

Inputs (read-only — the v3 content model, see docs/pipeline.md):
    entries/YYYY-MM-DD/<slug>.md   per-finding entry files (via site/content_model.py)
    entities/registry.yaml         global entity registry
    runs/YYYY-MM-DD/<run-id>.md    per-run records (telemetry + verification notes)
    state/cves_seen.json           flat CVE index
    state/source_health.json       source accessibility snapshots (optional)
    sources/sources.json           curated source list
    site/taxonomy.yaml             controlled vocabulary
    README.md / docs/*.md / prompts/*.md   rendered under /about/

Outputs (written under site/_site/):
    /                              home — live-brief / latest-day / latest-weekly cards
    /brief/                        THE DYNAMIC BRIEF — default 24 h window server-rendered;
                                   assets/js/brief.js re-renders from data/briefbook.json
    /briefs/                       day-page index, grouped by month
    /briefs/YYYY-MM-DD/            static day archive (canonical daily structure)
    /weekly/ + /weekly/YYYY-Www/   weekly index + weekly pages (v2 12-section structure)
    /briefs/weekly/YYYY-Www/       meta-refresh redirect stubs → /weekly/YYYY-Www/
    /entries/YYYY-MM-DD/<slug>/    per-entry permalinks (badges, update chain, run link)
    /entities/ /entities/<key>/    unified entity pages (registry + CVE universe)
    /cves/ /topics/                type-filtered entity list views (+ legacy redirects)
    /sources/ /sources/<id>/       source catalogue + per-source pages
    /tags/<t>/ /regions/<r>/       per-tag / per-region entry indexes
    /trends/                       entries-per-ISO-week cohort dashboard
    /ops/                          run telemetry dashboard (from runs/**)
    /feeds/ + feed*.xml            daily / weekly / per-entry + 8 sector slices
    /about/**                      README, docs (incl. docs/pipeline.md), prompts
    /data/briefbook.json           last-35-days entries+runs with pre-rendered card HTML
    /data/alerts.json              last-7-days critical|high entries (notification hooks)
    /data/search.json              search index (day / weekly / entry / entity / source)
    /data/site.json /data/build_manifest.json /sitemap.xml /robots.txt /404.html

Design properties (unchanged from v2):
    - stdlib-only Python; no build dependencies
    - vendored-library SHA-256/384 integrity check on entry
    - atomic per-file writes (temp + os.replace) + orphan pruning
    - deterministic: identical inputs produce a byte-identical tree; every
      timestamp derives from entry/run frontmatter, never now()
    - strict CSP; end-of-build self-check (manifest, feeds, secrets)

The site URL is read from SITE_URL env var; falls back to the deployed Pages
URL. Schema-invalid entries or a broken registry ABORT the build (fail-loud,
same philosophy as v2 taxonomy validation); sparse migrated run records
render gracefully with em-dash cells.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent
OUT = SITE / "_site"

# Shared v3 content model — THE parser/loader/validator for entries,
# the entity registry and run records (sibling module; sys.path[0] is
# site/ when invoked as `python3 site/build.py`).
sys.path.insert(0, str(SITE))
import content_model  # noqa: E402
from content_model import (  # noqa: E402
    KIND_DAILY_SECTION,
    KIND_WEEKLY_SECTION,
    WEEKLY_SECTIONS,
    collect_entries,
    collect_runs,
    load_registry,
    parse_taxonomy,
    parse_ts,
    validate_entry,
    validate_registry,
)


# === BRANDING PROFILE ===================================================
#
# Every site-identity / theme / analytics value comes from
# config/branding.yaml via the sibling loader module (fail-loud on unknown
# keys; upstream defaults on a missing file/key, so the upstream-shipped
# config builds a byte-identical site). Downstream forks customize ONLY
# config/branding.yaml + site/branding/ and merge upstream freely — no
# identity literal may be reintroduced below this point. See
# docs/customization.md.
import branding_config  # noqa: E402  (sibling module; sys.path[0] is site/)

BRANDING = branding_config.load_branding()

SITE_NAME = BRANDING["site"]["name"].strip()
WORDMARK_STRONG = BRANDING["site"]["wordmark_strong"]
WORDMARK_ACCENT = BRANDING["site"]["wordmark_accent"]
TAGLINE = BRANDING["site"]["tagline"].strip()
HOME_LEDE = BRANDING["site"]["lede"].strip()
HOME_META_DESCRIPTION = BRANDING["site"]["meta_description"].strip()
FOOTER_TAGLINE = BRANDING["site"]["footer_tagline"].strip()
SITE_LANG = BRANDING["site"]["lang"].strip()
SITE_LOCALE = BRANDING["site"]["locale"].strip()

DEFAULT_SITE_URL = BRANDING["site"]["url"].rstrip("/") + "/"
DEFAULT_GITHUB_REPO = BRANDING["site"]["github_repo"].strip()

# Theme override layer — empty strings across config/branding.yaml (the
# upstream default) yield an empty override, no branding.css is emitted,
# and styles.css keeps owning every design token.
BRANDING_CSS = branding_config.render_branding_css(BRANDING)
BRANDING_ASSETS_DIR = SITE / "branding"
HAS_CUSTOM_CSS = (BRANDING_ASSETS_DIR / "custom.css").is_file()
THEME_COLOR_DARK = BRANDING["theme"]["dark"]["bg"].strip() or "#0e1116"
THEME_COLOR_LIGHT = BRANDING["theme"]["light"]["bg"].strip() or "#fafbfc"

# Build-generated SVG chart colors (Ops / Trends / entities).
CHART_ACCENT_RGB = BRANDING["charts"]["accent_rgb"].strip() or "232,93,117"
CHART_INFO_RGB = BRANDING["charts"]["info_rgb"].strip() or "121,192,255"

# RSS channel descriptions (channel titles derive from SITE_NAME + TAGLINE).
FEED_DAILY_DESCRIPTION = BRANDING["feeds"]["daily_description"].strip()
FEED_WEEKLY_DESCRIPTION = BRANDING["feeds"]["weekly_description"].strip()
FEED_ITEMS_DESCRIPTION = BRANDING["feeds"]["items_description"].strip()

# RSS truncation per feed (HTML archive is unbounded).
FEED_DAILY_MAX = 30
FEED_WEEKLY_MAX = 30
FEED_ITEMS_MAX = 50


# === RESOURCE CAPS ======================================================
#
# Per-file ceilings for everything the build reads from disk. A poisoned
# state file or a runaway agent run could plant a multi-hundred-MB file;
# the build would otherwise attempt to load and render it and OOM the
# runner. Caps fail the build with a clear message instead. Loose by
# design — the largest legitimate entry on record is a few tens of KB.
MAX_BRIEF_BYTES = 4 * 1024 * 1024            # 4 MB per entry / run / docs file
MAX_STATE_BYTES = 16 * 1024 * 1024           # 16 MB per state file
MAX_VENDOR_BYTES = 4 * 1024 * 1024           # 4 MB per vendored JS file
MAX_ENTRIES_DIR_BYTES = 256 * 1024 * 1024    # 256 MB total entries/ + runs/ trees


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
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


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
#
# The taxonomy parser is the shared one in site/content_model.py
# (imported above as `parse_taxonomy`) so build, check_run and migration
# can never drift. It returns {key: set(values)}.


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


# Callout labels we lift out of paragraph prose into a styled aside block.
# These are conventional editorial markers in the daily/weekly brief:
# the "Defender takeaway" line is the operationally-actionable summary
# closing every item, "Action items" / "Detection guidance" / "Hunting
# hints" are occasional auxiliary callouts. By promoting the leading
# `<strong>Label:</strong>` paragraph into `<aside class="callout
# callout--takeaway">…</aside>`, the brief reader gets a visual anchor
# at the bottom of each item without the agent having to learn new
# Markdown syntax.
_CALLOUT_LABELS = {
    "defender takeaway":  "callout--takeaway",
    "defender note":      "callout--takeaway",
    "defender action":    "callout--takeaway",
    "action":             "callout--action",
    "action item":        "callout--action",
    "action items":       "callout--action",
    "detection guidance": "callout--detection",
    "detection":          "callout--detection",
    "hunting hints":      "callout--detection",
    "hunting hint":       "callout--detection",
}
_CALLOUT_LABEL_RE = re.compile(
    r"<p>\s*<strong>\s*("
    + "|".join(re.escape(lbl) for lbl in _CALLOUT_LABELS)
    + r")\s*[:—–-]\s*</strong>(?P<rest>.*?)</p>",
    re.IGNORECASE | re.DOTALL,
)


def enhance_brief_item_html(html: str) -> str:
    """Promote leading `**Defender takeaway:**`-style paragraphs inside
    rendered brief items into structured callout asides.

    The agent writes the operational summary at the close of each item
    as a Markdown paragraph that opens with a bold label. The renderer
    has already turned that into `<p><strong>Label:</strong> …</p>`.
    Lift it into an `<aside class="callout callout--takeaway">` so the
    stylesheet can give it dedicated visual weight (accent border, label
    badge) without changing how the agent writes briefs.

    Idempotent — calling twice has no effect because the regex requires
    the surrounding `<p>` wrapper which only appears in fresh-rendered
    Markdown."""

    def _wrap(m: re.Match[str]) -> str:
        raw_label = m.group(1).strip()
        cls = _CALLOUT_LABELS.get(raw_label.lower(), "callout--takeaway")
        # Title-case the label so "defender takeaway" → "Defender takeaway"
        # but preserve "Defender Takeaway" if the agent already cased it.
        display = raw_label if raw_label[:1].isupper() else raw_label.capitalize()
        rest = m.group("rest").strip()
        return (
            f'<aside class="callout {cls}" role="note">'
            f'<span class="callout__label">{_escape(display)}</span>'
            f'<div class="callout__body">{rest}</div>'
            f'</aside>'
        )

    return _CALLOUT_LABEL_RE.sub(_wrap, html)


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

# Umami analytics — config-driven via config/branding.yaml `analytics:`.
# `provider: "umami"` injects the snippet on every page and allows exactly
# its two hosts in the CSP; `provider: "none"` is the one-line off switch —
# no snippet, first-party-only CSP. UMAMI_SNIPPET and CSP_META below are
# BUILT from the same constants so the script's loader host and the CSP's
# allowed hosts can never silently drift apart again.
#
# REGRESSION GUARD (2026-06-20). The loader served from UMAMI_SCRIPT_HOST
# (`cloud.umami.is/script.js`) POSTs its pageview beacon to a *different*
# host — `gateway.umami.is/api/send` (the script's built-in default; see the
#   const K=`${(x||"https://gateway.umami.is").replace(/\/$/,"")}/api/send`
# in the minified loader). The CSP `connect-src` MUST list that beacon host
# or the browser silently blocks every beacon: the script loads fine and not
# one pageview is recorded. The original integration hard-coded the now-RETIRED
# `api-gateway.umami.dev` beacon host and nothing tied the CSP to the loader's
# real endpoint, so the mismatch shipped from the very first commit and went
# undetected until analytics were noticed to be empty. Before ever changing
# UMAMI_BEACON_HOST, re-derive it from the live script (the `/api/send` default
# host above) — do not trust memory/training data for this value — and never
# reintroduce a host listed in UMAMI_RETIRED_HOSTS. The import-time assertion
# after CSP_META enforces both rules on every build (including the deploy-site
# CI step, which runs `python3 site/build.py`).
ANALYTICS_ENABLED = BRANDING["analytics"]["provider"] == "umami"
UMAMI_WEBSITE_ID = BRANDING["analytics"]["umami"]["website_id"].strip()
UMAMI_SCRIPT_HOST = BRANDING["analytics"]["umami"]["script_host"].strip().rstrip("/")
UMAMI_BEACON_HOST = BRANDING["analytics"]["umami"]["beacon_host"].strip().rstrip("/")
UMAMI_RETIRED_HOSTS = ("https://api-gateway.umami.dev",)  # NEVER reintroduce

UMAMI_SNIPPET = (
    f'<script defer src="{UMAMI_SCRIPT_HOST}/script.js" '
    f'data-website-id="{UMAMI_WEBSITE_ID}" '
    'data-exclude-search="true"></script>'
) if ANALYTICS_ENABLED else ""

_CSP_SCRIPT_SRC = "'self'" + (f" {UMAMI_SCRIPT_HOST}" if ANALYTICS_ENABLED else "")
_CSP_CONNECT_SRC = "'self'" + (
    f" {UMAMI_SCRIPT_HOST} {UMAMI_BEACON_HOST}" if ANALYTICS_ENABLED else ""
)
CSP_META = (
    '<meta http-equiv="Content-Security-Policy" content='
    f"\"default-src 'self'; script-src {_CSP_SCRIPT_SRC}; "
    "style-src 'self' 'unsafe-inline'; img-src 'self' data:; "
    f"connect-src {_CSP_CONNECT_SRC}; "
    "object-src 'none'; base-uri 'self'; form-action 'none'; "
    'upgrade-insecure-requests" />'
)

# Structural guard — runs at import, so a bad edit aborts `python3 site/build.py`
# (and the deploy) with a clear message before a single page is written, rather
# than shipping a CSP that silently blocks analytics. Deterministic: a pure
# function of the constants above, never of brief content, so it can never
# false-positive on editorial drift.
if ANALYTICS_ENABLED:
    assert UMAMI_SCRIPT_HOST in CSP_META, "CSP is missing the Umami script host (script-src/connect-src)"
    assert UMAMI_BEACON_HOST in CSP_META, (
        f"CSP connect-src is missing the Umami beacon host {UMAMI_BEACON_HOST!r}; "
        "the loader POSTs pageviews to <beacon-host>/api/send and the browser blocks "
        "every beacon otherwise (analytics silently dead)"
    )
    for _retired_host in UMAMI_RETIRED_HOSTS:
        assert _retired_host not in CSP_META, (
            f"retired Umami host {_retired_host!r} reappeared in the CSP — it no longer "
            f"receives beacons; the live host is {UMAMI_BEACON_HOST!r}. See UMAMI_RETIRED_HOSTS."
        )
else:
    assert UMAMI_SNIPPET == "" and "umami" not in CSP_META, (
        "analytics.provider is 'none' but an analytics host survived into the "
        "snippet or CSP — the off switch must remove every third-party origin"
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

# --- Branding-driven template fragments ---------------------------------
#
# Each helper resolves to the built-in upstream default when the matching
# config/branding.yaml value is empty, and to the operator's override
# (a file under site/branding/, copied to /branding/ in the output) when
# set. Byte-identical to the pre-branding template in the default state.

FAVICON_DATA_URI = branding_config.default_favicon_href(BRANDING)

_DEFAULT_BRAND_MARK_SVG = (
    '<svg viewBox="0 0 24 24" focusable="false" aria-hidden="true">\n'
    '          <path d="M3.5 12a8.5 8.5 0 0 1 17 0" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>\n'
    '          <path d="M7.5 12a4.5 4.5 0 0 1 9 0" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" opacity="0.55"/>\n'
    '          <circle cx="12" cy="12" r="2" fill="currentColor"/>\n'
    '        </svg>'
)


def _branding_asset_url(rel: str, *, pfx: str, cachebust: str) -> str:
    return f"{pfx}branding/{_escape(rel)}?v={cachebust}"


def _brand_mark_html(*, pfx: str, cachebust: str) -> str:
    rel = BRANDING["logo"]["header_mark"].strip()
    if rel:
        return (
            f'<img class="brand-logo" '
            f'src="{_branding_asset_url(rel, pfx=pfx, cachebust=cachebust)}" alt="" />'
        )
    return _DEFAULT_BRAND_MARK_SVG


def _footer_mark_html(*, pfx: str, cachebust: str) -> str:
    rel = BRANDING["logo"]["footer_mark"].strip()
    if rel:
        return (
            f'<img class="footer-brand__mark" '
            f'src="{_branding_asset_url(rel, pfx=pfx, cachebust=cachebust)}" '
            'alt="" aria-hidden="true" />'
        )
    text = _escape(BRANDING["logo"]["footer_mark_text"].strip())
    return f'<span class="footer-brand__mark" aria-hidden="true">{text}</span>'


def _favicon_href(*, pfx: str, cachebust: str) -> str:
    rel = BRANDING["logo"]["favicon"].strip()
    if rel:
        return _branding_asset_url(rel, pfx=pfx, cachebust=cachebust)
    return FAVICON_DATA_URI


def _branding_css_links(*, pfx: str, cachebust: str) -> str:
    """Extra stylesheet <link>s after styles.css: the generated theme
    override (assets/css/branding.css) and the operator's free-form
    site/branding/custom.css — each only when it exists."""
    links = ""
    if BRANDING_CSS:
        links += f'\n<link rel="stylesheet" href="{pfx}assets/css/branding.css?v={cachebust}" />'
    if HAS_CUSTOM_CSS:
        links += f'\n<link rel="stylesheet" href="{pfx}branding/custom.css?v={cachebust}" />'
    return links


_WORDMARK_HTML = (
    f"<strong>{_escape(WORDMARK_STRONG)}</strong>"
    + (f"<em>{_escape(WORDMARK_ACCENT)}</em>" if WORDMARK_ACCENT else "")
)
_FOOTER_TAGLINE_HTML = (
    f"\n            <small>{_escape(FOOTER_TAGLINE)}</small>" if FOOTER_TAGLINE else ""
)
_FOOTER_LEDE_HTML = "\n          ".join(
    _escape(ln) for ln in BRANDING["site"]["footer_lede"].strip().splitlines()
)
_COPYRIGHT_NOTE_HTML = "\n        ".join(
    _escape(ln) for ln in BRANDING["site"]["copyright_note"].strip().splitlines()
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
<html lang="{_escape(SITE_LANG)}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="theme-color" content="{_escape(THEME_COLOR_DARK)}" media="(prefers-color-scheme: dark)" />
<meta name="theme-color" content="{_escape(THEME_COLOR_LIGHT)}" media="(prefers-color-scheme: light)" />
{CSP_META}
<meta name="referrer" content="strict-origin-when-cross-origin" />
<title>{_escape(title)}</title>
<meta name="description" content="{_escape(description)}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="{_escape(canonical)}" />
<meta property="og:site_name" content="{_escape(SITE_NAME)}" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{_escape(title)}" />
<meta property="og:description" content="{_escape(description)}" />
<meta property="og:url" content="{_escape(canonical)}" />
<meta property="og:locale" content="{_escape(SITE_LOCALE)}" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:title" content="{_escape(title)}" />
<meta name="twitter:description" content="{_escape(description)}" />
<link rel="stylesheet" href="{pfx}assets/css/styles.css?v={cachebust}" />{_branding_css_links(pfx=pfx, cachebust=cachebust)}
<link rel="alternate" type="application/rss+xml" title="{_escape(SITE_NAME)} — Daily" href="{pfx}feed.xml" />
<link rel="alternate" type="application/rss+xml" title="{_escape(SITE_NAME)} — Weekly" href="{pfx}feed-weekly.xml" />
<link rel="alternate" type="application/rss+xml" title="{_escape(SITE_NAME)} — Per item" href="{pfx}feed-items.xml" />
<link rel="sitemap" type="application/xml" href="{pfx}sitemap.xml" />
<link rel="icon" href="{_favicon_href(pfx=pfx, cachebust=cachebust)}" />
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
    <a class="brand" href="{pfx}" aria-label="Home — {_escape(SITE_NAME)}">
      <span class="brand-mark" aria-hidden="true">
        {_brand_mark_html(pfx=pfx, cachebust=cachebust)}
      </span>
      <span class="brand-text">{_WORDMARK_HTML}</span>
    </a>

    <form class="searchbox" role="search" data-search-form>
      <label class="visually-hidden" for="q">Search briefs, CVEs, topics, sources</label>
      <input id="q" type="search" autocomplete="off" spellcheck="false" placeholder="Search    /" aria-label="Search" />
      <kbd class="kbd-hint" aria-hidden="true">/</kbd>
      <ul id="suggestions" class="suggestions" role="listbox" hidden></ul>
    </form>

    <a class="github-link" id="github-link" href="https://github.com/{os.environ.get('GITHUB_REPO', DEFAULT_GITHUB_REPO)}" target="_blank" rel="noopener noreferrer" aria-label="GitHub repository" title="View source on GitHub">
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
      <a href="{pfx}brief/">Brief</a>
      <a href="{pfx}briefs/">Archive</a>
      <a href="{pfx}weekly/">Weekly</a>
      <a href="{pfx}entities/">Entities</a>
      <a href="{pfx}sources/">Sources</a>
      <a href="{pfx}trends/">Trends</a>
      <a href="{pfx}ops/">Ops</a>
      <a href="{pfx}about/">About</a>
    </nav>
  </div>
</header>
<div class="read-progress" aria-hidden="true"></div>
<main id="main" class="main"><div class="view">{body}</div></main>
<footer class="footer" role="contentinfo">
  <div class="footer-inner">
    <div class="footer-grid">
      <section class="footer-brand">
        <a class="footer-brand__home" href="{pfx}" aria-label="{_escape(SITE_NAME)} home">
          {_footer_mark_html(pfx=pfx, cachebust=cachebust)}
          <span class="footer-brand__title">
            <strong>{_escape(SITE_NAME)}</strong>{_FOOTER_TAGLINE_HTML}
          </span>
        </a>
        <p class="footer-brand__lede">
          {_FOOTER_LEDE_HTML}
        </p>
        <p class="footer-brand__notice">
          <span class="footer-brand__notice-label">AI-generated · no human review</span>
          <a href="{pfx}about/">How this works →</a>
        </p>
      </section>

      <nav class="footer-col" aria-label="Read">
        <h4 class="footer-col__label">Read</h4>
        <ul>
          <li><a href="{pfx}brief/">Live brief</a></li>
          <li><a href="{pfx}briefs/">Day archive</a></li>
          <li><a href="{pfx}weekly/">Weekly summaries</a></li>
          <li><a href="{pfx}entities/">Entities</a></li>
          <li><a href="{pfx}sources/">Sources</a></li>
          <li><a href="{pfx}trends/">Trends</a></li>
          <li><a href="{pfx}ops/">Operations</a></li>
        </ul>
      </nav>

      <nav class="footer-col" aria-label="Subscribe">
        <h4 class="footer-col__label">Subscribe</h4>
        <ul>
          <li><a href="{pfx}feed.xml">RSS — Daily</a></li>
          <li><a href="{pfx}feed-weekly.xml">RSS — Weekly</a></li>
          <li><a href="{pfx}feed-items.xml">RSS — Per item</a></li>
          <li><a href="{pfx}feeds/">All feeds + sectors</a></li>
        </ul>
      </nav>

      <nav class="footer-col" aria-label="About">
        <h4 class="footer-col__label">About</h4>
        <ul>
          <li><a href="{pfx}about/">How this works</a></li>
          <li><a href="{pfx}about/prompts/changelog/">Editorial policy</a></li>
          <li><a href="{pfx}about/prompts/verification/">Verification</a></li>
          <li><a href="https://github.com/{os.environ.get('GITHUB_REPO', DEFAULT_GITHUB_REPO)}" target="_blank" rel="noopener noreferrer">Source on GitHub ↗</a></li>
        </ul>
      </nav>
    </div>

    <div class="footer-bottom">
      <p class="footer-bottom__copy">
        © {datetime.now(timezone.utc).year} {_escape(SITE_NAME)} — {_COPYRIGHT_NOTE_HTML}
      </p>
      <p class="footer-bottom__build" id="footer-meta">
        <span class="mono">build {_escape(cachebust[:8])}</span>
      </p>
    </div>
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
                f'<a class="pill pill-cve" href="{prefix}entities/{_escape(token)}/">{_escape(token)}</a>'
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


# === ENTRY MODEL (v3) ===================================================
#
# Entries are loaded through content_model.collect_entries() and are the
# atomic intelligence unit. Everything below derives render-time
# groupings from the entry frontmatter — nothing is parsed out of
# Markdown headings any more.

# Priority sort rank (lower renders first).
PRIORITY_RANK = {"critical": 0, "high": 1, "notable": 2, "routine": 3}

# Org-lens regions render first inside the threat sections (mirrors the
# v2 editorial ordering; the same tuple is exported to brief.js through
# the /brief/ data island so server and client grouping cannot drift).
ORG_LENS_REGIONS = ("switzerland", "dach", "europe")

# Canonical daily / window brief structure (docs/pipeline.md § Rendering).
# Section keys `tldr`, `action-items` and `verification-notes` are
# synthesised; the rest bucket entries via `entry_section_key`.
DAILY_SECTIONS: list[tuple[str, str]] = [
    ("tldr", "0. TL;DR"),
    ("active-threats", "1. Active Threats, Trending Actors, Notable Incidents & Disclosures"),
    ("trending-vulnerabilities", "2. Trending Vulnerabilities"),
    ("research", "3. Research & Investigative Reporting"),
    ("updates", "4. Updates to Prior Coverage"),
    ("deep-dive", "5. Deep Dive"),
    ("action-items", "6. Action Items"),
    ("verification-notes", "7. Verification Notes"),
]

# Compact section labels for dense UI (the recent-runs overview breakdown).
SECTION_SHORT: dict[str, str] = {
    "active-threats": "Threats",
    "trending-vulnerabilities": "Vulns",
    "research": "Research",
    "updates": "Updates",
    "deep-dive": "Deep dive",
}

# Weekly structure — the v2 12-section order with the v2 headings.
# `weekly-glance` is derived (one bullet per critical/high strategic
# entry); `verification-notes` renders the week's run-record bodies.
WEEKLY_STRUCTURE: list[tuple[str, str]] = [
    ("weekly-glance", "0. Week at a glance"),
    ("weekly-top-stories", "1. Highest-impact events — what's on fire if no one acted"),
    ("weekly-multi-day", "2. Multi-day campaigns and chains"),
    ("weekly-vuln-rollup", "3. Vulnerability roll-up"),
    ("weekly-sector-patterns", "4. Sector & victim patterns"),
    ("weekly-incidents-recap", "5. Incidents & disclosures recap"),
    ("weekly-research", "6. Research & threat-actor developments"),
    ("weekly-annual-reports", "7. Annual / periodic threat reports"),
    ("weekly-long-running", "8. Long-running campaigns — status update"),
    ("weekly-policy", "9. Policy & regulatory horizon"),
    ("weekly-looking-ahead", "10. Looking ahead — what to watch next week"),
    ("verification-notes", "11. Verification & coverage notes"),
]

VERIFICATION_BADGE_LABEL = {
    "single-source": "single-source",
    "single-source-national-cert": "single-source · national CERT",
    "single-source-victim": "single-source · victim disclosure",
    "contradicted": "contradicted",
}


def entry_url_path(entry: dict[str, Any]) -> str:
    """Site-root-relative permalink path for an entry, with trailing
    slash — `entries/2026-07-03/coolify-cve-2026-34038-rce/`."""
    return f"entries/{entry['date']}/{entry['slug']}/"


def entry_section_key(entry: dict[str, Any]) -> str | None:
    """Daily-brief section for an operational entry. Orthogonal flags
    relocate at render time: update_of → updates, deep_dive → deep-dive.
    Strategic-only kinds map to None (not rendered in the window/day
    view)."""
    if entry.get("update_of"):
        return "updates"
    if entry.get("deep_dive"):
        return "deep-dive"
    return KIND_DAILY_SECTION.get(entry.get("kind") or "")


def weekly_section_key(entry: dict[str, Any]) -> str:
    """Weekly section for a strategic entry: explicit `weekly_section`
    wins, else the kind-based default from content_model."""
    ws = entry.get("weekly_section")
    if ws in WEEKLY_SECTIONS:
        return ws
    return KIND_WEEKLY_SECTION.get(entry.get("kind") or "", "weekly-top-stories")


def entry_cve_ids(entry: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for c in entry.get("cves") or []:
        if isinstance(c, dict) and c.get("id"):
            cid = str(c["id"])
            if cid not in out:
                out.append(cid)
    return out


def entry_cve_status_union(entry: dict[str, Any]) -> list[str]:
    out: list[str] = []
    for c in entry.get("cves") or []:
        for st in (c.get("status") or []) if isinstance(c, dict) else []:
            if st not in out:
                out.append(str(st))
    return out


def _entry_region_lens_hit(entry: dict[str, Any]) -> bool:
    return bool(set(entry.get("regions") or []) & set(ORG_LENS_REGIONS))


def entry_sort_key(entry: dict[str, Any]) -> tuple:
    """Section-body ordering: org-lens regions first, then priority,
    then discovered_at descending (mirrored in brief.js)."""
    ts = entry.get("discovered_at") or ""
    return (
        0 if _entry_region_lens_hit(entry) else 1,
        PRIORITY_RANK.get(entry.get("priority") or "notable", 2),
        # invert the timestamp string for a descending sort inside an
        # ascending tuple sort (fixed-width ISO-8601 Z strings compare
        # lexically, so a codepoint-wise complement inverts the order).
        "".join(chr(0x10FFFF - ord(ch)) for ch in ts),
        entry.get("id") or "",
    )


def operational_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [e for e in entries if (e.get("horizon") or "operational") == "operational"]


def strategic_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [e for e in entries if e.get("horizon") == "strategic"]


def entries_in_window(entries: list[dict[str, Any]], since: datetime,
                      until: datetime | None = None) -> list[dict[str, Any]]:
    return content_model.entries_in_window(entries, since, until)


def entries_by_day(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group OPERATIONAL entries by their UTC folder date. A day page
    exists iff the date has at least one operational entry."""
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in operational_entries(entries):
        out[e["date"]].append(e)
    return dict(sorted(out.items()))


def _iso_week_of(date_str: str) -> str | None:
    """Convert YYYY-MM-DD to YYYY-Www. Returns None on bad input."""
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", (date_str or "").strip())
    if not m:
        return None
    try:
        dt = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        iso_year, iso_week, _ = dt.isocalendar()
        return f"{iso_year}-W{iso_week:02d}"
    except (ValueError, OverflowError):
        return None


def iso_week_of_entry(entry: dict[str, Any]) -> str | None:
    """ISO week (`YYYY-Www`) of the entry's discovered_at date."""
    m = DATE_RE.match(entry.get("date") or "")
    if not m:
        return None
    try:
        y, mo, d = (int(x) for x in entry["date"].split("-"))
        iso = date(y, mo, d).isocalendar()
        return f"{iso[0]:04d}-W{iso[1]:02d}"
    except (ValueError, OverflowError):
        return None


def entries_by_week(entries: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group STRATEGIC entries by ISO week of discovered_at. A weekly
    page exists iff the week has at least one strategic entry."""
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in strategic_entries(entries):
        wk = iso_week_of_entry(e)
        if wk:
            out[wk].append(e)
    return dict(sorted(out.items()))


def build_update_chains(entries: list[dict[str, Any]]) -> dict[str, list[str]]:
    """`update_of` back-references: entry id → ids of entries updating
    it, ascending by discovered_at (entries arrive pre-sorted)."""
    updated_by: dict[str, list[str]] = defaultdict(list)
    for e in entries:
        target = e.get("update_of")
        if target:
            updated_by[str(target)].append(e["id"])
    return dict(updated_by)


def reference_ts(entries: list[dict[str, Any]], runs: list[dict[str, Any]]) -> datetime:
    """The build's deterministic 'now': the newest content moment across
    entry discovered_at and run started/completed timestamps. Anchors
    the /brief/ default window, briefbook/alerts windows and RSS
    lastBuildDate without ever calling now()."""
    best: datetime | None = None
    for e in entries:
        ts = parse_ts(e.get("discovered_at"))
        if ts and (best is None or ts > best):
            best = ts
    for r in runs or []:
        for field in ("completed", "started"):
            ts = parse_ts(r.get(field))
            if ts and (best is None or ts > best):
                best = ts
    return best or datetime(2000, 1, 1, tzinfo=timezone.utc)


def select_tldr_entries(window_entries: list[dict[str, Any]], cap: int = 6) -> list[dict[str, Any]]:
    """TL;DR bullet selection: every critical first, then every high;
    if that yields fewer than 3 bullets, pad with the newest notable
    entries. Hard cap 6. (Mirrored in brief.js.)"""
    by_recency = sorted(
        window_entries,
        key=lambda e: (str(e.get("discovered_at") or ""), e.get("id") or ""),
        reverse=True,
    )
    crit = [e for e in by_recency if e.get("priority") == "critical"]
    high = [e for e in by_recency if e.get("priority") == "high"]
    picked = crit + high
    if len(picked) < 3:
        notable = [e for e in by_recency if e.get("priority") == "notable"]
        picked = picked + notable[: 3 - len(picked)]
    return picked[:cap]


def runs_in_window(runs: list[dict[str, Any]], since: datetime,
                   until: datetime | None = None) -> list[dict[str, Any]]:
    """Run records whose completed (fallback started) moment falls in
    [since, until). Newest first."""
    out: list[dict[str, Any]] = []
    for r in runs or []:
        ts = parse_ts(r.get("completed")) or parse_ts(r.get("started"))
        if ts is None:
            continue
        if ts >= since and (until is None or ts < until):
            out.append(r)
    out.sort(key=lambda r: str(r.get("completed") or r.get("started") or ""), reverse=True)
    return out


# === ENTRY CARD RENDERERS (v3) =========================================
#
# One server-side card renderer feeds every consumer: /brief/, the day
# pages, the per-entry embeds on entity pages, the RSS bodies AND
# data/briefbook.json (whose `html` field is this exact card, so
# brief.js only ever regroups + concatenates — no client-side Markdown).


def _fmt_discovered(ts_str: str | None) -> str:
    """`2026-07-03T04:21:09Z` → `discovered 2026-07-03 04:21 UTC`."""
    ts = parse_ts(ts_str)
    if ts is None:
        return ""
    return "discovered " + ts.strftime("%Y-%m-%d %H:%M") + " UTC"


def render_priority_badge(priority: str) -> str:
    cls = {
        "critical": "badge--crit",
        "high": "badge--low",       # red-ish accent — leads the window
        "notable": "badge--med",
        "routine": "badge--high",
    }.get(priority or "", "badge--med")
    return f'<span class="badge {cls}">{_escape(priority or "notable")}</span>'


def render_entry_badges(entry: dict[str, Any], *, prefix: str = "") -> str:
    """Top status strip on an entry card: priority, kind, discovered-at
    timestamp, and the status badges (verification single-source*, deep
    dive, watchlist, org-triage). The taxonomy pills (tags / regions /
    CVEs) render BELOW the entry body via `render_entry_taxonomy` — the
    v2 footer placement, restored."""
    parts: list[str] = [render_priority_badge(entry.get("priority") or "notable")]
    parts.append(f'<span class="badge">{_escape(entry.get("kind") or "")}</span>')
    disc = _fmt_discovered(entry.get("discovered_at"))
    if disc:
        parts.append(f'<span class="entry-discovered mono muted">{_escape(disc)}</span>')
    ver = entry.get("verification")
    if ver in VERIFICATION_BADGE_LABEL:
        parts.append(
            f'<span class="badge badge--low" title="{_escape(entry.get("sourcing_note") or "verification status")}">'
            f'{_escape(VERIFICATION_BADGE_LABEL[ver])}</span>'
        )
    if entry.get("deep_dive"):
        parts.append('<span class="badge badge--accent">deep dive</span>')
    if entry.get("watchlist_hit"):
        parts.append('<span class="badge badge--accent" title="Included via an org-profile watchlist match">watchlist</span>')
    ot = entry.get("org_triage")
    if isinstance(ot, dict) and ot.get("category"):
        parts.append(
            f'<span class="badge badge--cve" title="{_escape(str(ot.get("rationale") or "org triage"))}">'
            f'{_escape(str(ot["category"]))}</span>'
        )
    return '<div class="entry-badges">' + " ".join(parts) + "</div>"


def render_entry_taxonomy(entry: dict[str, Any], *, prefix: str = "") -> str:
    """Below-the-entry metadata pills — tag / region / CVE — the v2
    footer, restored under each item. Empty entries render nothing."""
    pills: list[str] = []
    for t in entry.get("tags") or []:
        pills.append(render_tag_pill(t, prefix=prefix))
    for r in entry.get("regions") or []:
        pills.append(render_region_pill(r, prefix=prefix))
    for cid in entry_cve_ids(entry):
        pills.append(render_cve_pill(cid, prefix=prefix))
    if not pills:
        return ""
    return '<div class="entry-taxonomy">' + " ".join(pills) + "</div>"


def _entry_source_by_publisher(entry: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """publisher (lower-cased) -> its source dict, from the entry's own
    source list — lets an evidence quote link back to the article it was
    taken from."""
    out: dict[str, dict[str, Any]] = {}
    for s in entry.get("sources") or []:
        if isinstance(s, dict) and s.get("publisher"):
            out.setdefault(str(s["publisher"]).strip().lower(), s)
    return out


def _cite_attribution_html(pub: str, src_by_pub: dict[str, dict[str, Any]]) -> str:
    """One attribution caption for a quoted source. Links to the matching
    source URL (with its date) when we have it, so the quote is checkable
    against the original; plain publisher name otherwise."""
    if not pub:
        return ""
    src = src_by_pub.get(pub.lower())
    if src and src.get("url"):
        url = _escape(_safe_url(str(src["url"])))
        date = str(src.get("date") or "")
        date_html = (
            f' <span class="entry-cite__date mono">{_escape(date)}</span>' if date else ""
        )
        inner = (
            f'<a href="{url}" target="_blank" rel="noopener noreferrer">{_escape(pub)}</a>'
            f"{date_html}"
        )
    else:
        inner = _escape(pub)
    return f'<figcaption class="entry-cite__attr">{inner}</figcaption>'


def render_entry_evidence(entry: dict[str, Any]) -> str:
    """Verbatim source quotes rendered as a distinct "cited from the
    reporting" block — deliberately neutral so it never reads as the
    pipeline's own voice (that is the accent Defender-takeaway callout).
    Consecutive quotes from the same publisher are grouped under a single
    attribution, so a source is cited once no matter how many lines it
    backs (no citation-in-citation repetition)."""
    evs = [
        ev for ev in (entry.get("evidence") or [])
        if isinstance(ev, dict) and ev.get("quote")
    ]
    if not evs:
        return ""
    src_by_pub = _entry_source_by_publisher(entry)

    groups: list[tuple[str, list[str]]] = []
    for ev in evs:
        pub = str(ev.get("publisher") or "").strip()
        quote = str(ev["quote"])
        if groups and groups[-1][0] == pub:
            groups[-1][1].append(quote)
        else:
            groups.append((pub, [quote]))

    figures: list[str] = []
    for pub, quotes in groups:
        quote_html = "".join(
            f'<p class="entry-cite__quote">{_escape(q)}</p>' for q in quotes
        )
        figures.append(
            '<figure class="entry-cite">'
            f"{quote_html}{_cite_attribution_html(pub, src_by_pub)}"
            "</figure>"
        )
    return (
        '<div class="entry-cites" role="group" aria-label="Quoted from the reporting">'
        + "".join(figures)
        + "</div>"
    )


def render_entry_sources(entry: dict[str, Any], *, with_roles: bool = False) -> str:
    """Sources line (aside.item-footer) — open-web sources with roles +
    closed-source citations (never linked; cited by reference only)."""
    parts: list[str] = []
    srcs = entry.get("sources") or []
    if srcs:
        bits: list[str] = []
        for i, s in enumerate(srcs):
            if not isinstance(s, dict):
                continue
            url = _escape(_safe_url(str(s.get("url") or "")))
            label = _escape(str(s.get("publisher") or s.get("url") or "source"))
            sdate = str(s.get("date") or "")
            role = str(s.get("role") or ("primary" if i == 0 else "corroborating"))
            cls = "src-primary" if role == "primary" else "src-additional"
            role_html = f' <span class="muted">({_escape(role)})</span>' if with_roles else ""
            date_html = f' <span class="muted mono">{_escape(sdate)}</span>' if sdate else ""
            bits.append(
                f'<a class="{cls}" href="{url}" target="_blank" rel="noopener noreferrer">{label}</a>'
                f"{date_html}{role_html}"
            )
        parts.append('<span class="meta-sources"><strong>Sources:</strong> ' + " · ".join(bits) + "</span>")
    closed = entry.get("closed_sources") or []
    if closed:
        cs_bits: list[str] = []
        for c in closed:
            if not isinstance(c, dict):
                continue
            extras = [str(b) for b in (c.get("provider"), c.get("date")) if b]
            if c.get("tlp"):
                extras.append(f"TLP:{str(c['tlp']).upper()}")
            if c.get("ref"):
                extras.append(f"ref: {c['ref']}")
            label = f'“{c.get("title", "")}”' + (f' ({", ".join(extras)})' if extras else "")
            cs_bits.append('<span class="src-closed">' + _escape(label) + "</span>")
        parts.append(
            '<span class="meta-closed-source"><strong>Closed source:</strong> '
            + " · ".join(cs_bits) + "</span>")
    if not parts:
        return ""
    return '<aside class="item-footer">' + "".join(parts) + "</aside>"


def render_immediate_action_callout(entry: dict[str, Any], *, prefix: str = "") -> str:
    """The v2 Immediate-Action bar for a `priority: critical` entry —
    title, action, entry link, first evidence quote. brief.js rebuilds
    this exact shape client-side via DOM APIs."""
    ia = entry.get("immediate_action")
    if not isinstance(ia, dict):
        return ""
    url = f"{prefix}{entry_url_path(entry)}"
    quote_html = ""
    for ev in entry.get("evidence") or []:
        if isinstance(ev, dict) and ev.get("quote"):
            pub = str(ev.get("publisher") or "").strip()
            src_by_pub = _entry_source_by_publisher(entry)
            quote_html = (
                '<figure class="entry-cite entry-cite--inline">'
                f'<p class="entry-cite__quote">{_escape(str(ev["quote"]))}</p>'
                f"{_cite_attribution_html(pub, src_by_pub)}"
                "</figure>"
            )
            break
    return (
        '<aside class="callout callout--action immediate-action" role="note" '
        f'data-entry-id="{_escape(entry["id"])}">'
        '<span class="callout__label">Immediate action</span>'
        '<div class="callout__body">'
        f'<p><strong>{_escape(str(ia.get("title") or ""))}</strong> — '
        f'{_escape(str(ia.get("action") or "").strip())} '
        f'<a href="{_escape(url)}">{_inline_text(entry.get("headline") or entry.get("title") or entry["id"])} →</a></p>'
        f"{quote_html}"
        "</div></aside>"
    )


def render_update_lead(entry: dict[str, Any], *, prefix: str = "",
                       entries_by_id: dict[str, dict[str, Any]] | None = None) -> str:
    """`originally covered <link>` lead paragraph for update entries."""
    target = str(entry.get("update_of") or "")
    if not target:
        return ""
    orig = (entries_by_id or {}).get(target)
    label = orig.get("title") if orig else target
    tdate = target.split("/", 1)[0]
    return (
        '<p class="update-lead"><strong>UPDATE</strong> — originally covered '
        f'<a href="{_escape(prefix)}entries/{_escape(target)}/">'
        f'{_escape(str(label))}</a> <span class="mono muted">({_escape(tdate)})</span></p>'
    )


def render_entry_card(
    entry: dict[str, Any],
    *,
    prefix: str = "",
    section_key: str | None = None,
    base_url: str | None = None,
    entries_by_id: dict[str, dict[str, Any]] | None = None,
    heading_level: int = 3,
) -> str:
    """The canonical item card — used on /brief/, day pages, weekly
    pages, entity-page embeds, feed bodies and briefbook.json. Carries
    data-tags/data-regions/data-section so the existing filter chips
    keep working, plus data-entry-id/data-priority/data-discovered for
    brief.js."""
    skey = section_key or entry_section_key(entry) or ""
    url = f"{prefix}{entry_url_path(entry)}"
    hl = max(2, min(int(heading_level), 4))
    body_html = enhance_brief_item_html(
        render_markdown(entry.get("body") or "", base_url=base_url)
    )
    is_update = bool(entry.get("update_of"))
    inner = (
        render_entry_badges(entry, prefix=prefix)
        + body_html
        + render_entry_evidence(entry)
    )
    refs = [str(r) for r in (entry.get("references") or [])]
    if refs:
        ref_links = " · ".join(
            f'<a href="{_escape(prefix)}entries/{_escape(r)}/" class="mono">{_escape(r)}</a>'
            for r in refs
        )
        inner += f'<p class="entry-references muted"><strong>Builds on:</strong> {ref_links}</p>'
    if is_update:
        inner = (
            f'<blockquote class="callout-update">'
            + render_update_lead(entry, prefix=prefix, entries_by_id=entries_by_id)
            + inner
            + "</blockquote>"
        )
    heading_html = (
        f'<h{hl} id="{_escape(entry["slug"])}">'
        f'<a class="item-link" href="{_escape(url)}">{_escape(entry.get("title") or entry["id"])}</a>'
        f"</h{hl}>"
    )
    return (
        f'<article class="brief-item entry-card" '
        f'data-entry-id="{_escape(entry["id"])}" '
        f'data-tags="{_escape(" ".join(entry.get("tags") or []))}" '
        f'data-regions="{_escape(" ".join(entry.get("regions") or []))}" '
        f'data-section="{_escape(skey)}" '
        f'data-priority="{_escape(entry.get("priority") or "notable")}" '
        f'data-discovered="{_escape(entry.get("discovered_at") or "")}">'
        f"{heading_html}"
        f"{inner}"
        f"{render_entry_taxonomy(entry, prefix=prefix)}"
        f"{render_entry_sources(entry)}"
        f"</article>"
    )


# === CANONICAL BRIEF ASSEMBLER (v3) ====================================

SECTION_EMPTY_STUB = (
    "No qualifying items in window — this section is intentionally left empty."
)


def _section_shell(key: str, title: str, inner: str, *, collapsed: bool = False) -> str:
    """One `<section class="brief-section">` with the anchor + collapse
    chevron the existing CSS/app.js already wire (same DOM as v2)."""
    anchor = slugify(title)
    classes = "brief-section" + (" section-collapsed" if collapsed else "")
    chevron_svg = (
        '<svg class="section-collapse-chevron" viewBox="0 0 20 20" '
        'aria-hidden="true" focusable="false">'
        '<path fill="none" stroke="currentColor" stroke-width="2" '
        'stroke-linecap="round" stroke-linejoin="round" '
        'd="M5 8l5 5 5-5"/></svg>'
    )
    return (
        f'<section class="{classes}" data-section="{_escape(key)}" id="{_escape(anchor)}">'
        f"<h2>"
        f'<a class="section-anchor" href="#{_escape(anchor)}">{_escape(title)}</a>'
        f'<button type="button" class="section-collapse-toggle" '
        f'data-section-collapse-toggle="{_escape(anchor)}" '
        f'aria-expanded="{"false" if collapsed else "true"}" '
        f'aria-controls="{_escape(anchor)}-body" '
        f'aria-label="Toggle {_escape(title)} section">'
        f"{chevron_svg}"
        f"</button>"
        f"</h2>"
        f'<div class="brief-section__body" id="{_escape(anchor)}-body">{inner}</div>'
        f"</section>"
    )


def _empty_stub_html() -> str:
    return f'<p class="muted section-empty"><em>{_escape(SECTION_EMPTY_STUB)}</em></p>'


def _inline_text(s: str) -> str:
    """Headline / summary fields are *mostly* plain text, but migrated v2
    content may carry inline Markdown emphasis. Render it (escaped, no
    links) so `**bold**` never leaks verbatim into pages or feeds."""
    return render_inline_no_links((s or "").strip())


def render_tldr_bullets(picked: list[dict[str, Any]], *, prefix: str = "") -> str:
    lis: list[str] = []
    for e in picked:
        url = f"{prefix}{entry_url_path(e)}"
        headline = (e.get("headline") or e.get("title") or e["id"]).strip().strip("*").rstrip(".")
        lis.append(
            "<li>"
            f"<strong>{_inline_text(headline)}.</strong> "
            f'{_inline_text(e.get("summary") or "")} '
            f'<a href="{_escape(url)}">→</a>'
            "</li>"
        )
    return f"<ul>{''.join(lis)}</ul>" if lis else _empty_stub_html()


def render_run_note(run: dict[str, Any], *, base_url: str | None = None) -> str:
    """One run record's verification & coverage notes under a compact
    header (run_id, models, window_hours, entries_published)."""
    rid = str(run.get("run_id") or "?")
    bits: list[str] = []
    model = run.get("model")
    if model:
        bits.append(_escape(str(model)))
    wh = run.get("window_hours")
    if isinstance(wh, (int, float)):
        bits.append(f"window {wh:g} h")
    ep = run.get("entries_published")
    if isinstance(ep, int):
        bits.append(f"{ep} entr{'y' if ep == 1 else 'ies'} published")
    header_meta = " · ".join(bits)
    body_html = render_markdown(run.get("body") or "", base_url=base_url)
    return (
        f'<div class="run-note" data-run-id="{_escape(rid)}">'
        f'<h3 class="run-note__head"><span class="mono">{_escape(rid)}</span>'
        + (f' <span class="muted">— {header_meta}</span>' if header_meta else "")
        + "</h3>"
        f'<div class="run-note__body">{body_html}</div>'
        "</div>"
    )


def render_brief_sections(
    entries: list[dict[str, Any]],
    runs: list[dict[str, Any]],
    *,
    prefix: str = "",
    base_url: str | None = None,
    entries_by_id: dict[str, dict[str, Any]] | None = None,
    card_html_by_id: dict[str, str] | None = None,
) -> str:
    """THE shared server-side assembler for the canonical daily / window
    brief structure — used by /brief/ (default window), every day page,
    and the daily RSS bodies; mirrored client-side by
    site/assets/js/brief.js. `entries` must already be scoped to the
    window/day (operational horizon). `runs` are the window's run
    records (their bodies become § 7). Sections always render; empty
    ones carry the explicit stub.

    `card_html_by_id` lets a caller inject pre-rendered card HTML (the
    briefbook path renders each card exactly once and reuses it here).
    """
    ops = operational_entries(entries)
    by_id = entries_by_id or {e["id"]: e for e in ops}

    def card(e: dict[str, Any], skey: str) -> str:
        if card_html_by_id is not None and e["id"] in card_html_by_id:
            return card_html_by_id[e["id"]]
        return render_entry_card(
            e, prefix=prefix, section_key=skey, base_url=base_url,
            entries_by_id=by_id,
        )

    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in ops:
        skey = entry_section_key(e)
        if skey:
            buckets[skey].append(e)
    for skey in buckets:
        buckets[skey].sort(key=entry_sort_key)

    picked_tldr = select_tldr_entries(ops)
    criticals = [e for e in ops if e.get("priority") == "critical"]

    out: list[str] = []
    for key, title in DAILY_SECTIONS:
        if key == "tldr":
            inner = render_tldr_bullets(picked_tldr, prefix=prefix)
            for e in sorted(criticals, key=entry_sort_key):
                inner += render_immediate_action_callout(e, prefix=prefix)
        elif key == "action-items":
            rows: list[str] = []
            for e in sorted(ops, key=entry_sort_key):
                url = f"{prefix}{entry_url_path(e)}"
                for a in e.get("actions") or []:
                    if not isinstance(a, str) or not a.strip():
                        continue
                    rows.append(
                        '<li class="action-list__item" '
                        f'data-entry-id="{_escape(e["id"])}">'
                        f'<div class="action-list__body">{render_inline(a.strip(), base_url=base_url)}'
                        f' <a class="action-list__ref" href="{_escape(url)}">'
                        f'{_escape(e.get("headline") or e.get("title") or e["id"])} →</a></div>'
                        "</li>"
                    )
            inner = (
                f'<ul class="action-list">{"".join(rows)}</ul>' if rows else _empty_stub_html()
            )
        elif key == "verification-notes":
            notes = [render_run_note(r, base_url=base_url) for r in runs or []]
            inner = "".join(notes) if notes else _empty_stub_html()
        else:
            section_entries = buckets.get(key, [])
            inner = (
                "".join(card(e, key) for e in section_entries)
                if section_entries else _empty_stub_html()
            )
        out.append(_section_shell(key, title, inner,
                                  collapsed=(key == "verification-notes")))
    return "".join(out)


def render_weekly_sections(
    week_entries: list[dict[str, Any]],
    runs: list[dict[str, Any]],
    *,
    prefix: str = "",
    base_url: str | None = None,
    entries_by_id: dict[str, dict[str, Any]] | None = None,
) -> str:
    """The weekly 12-section structure (v2 order and headings) over the
    week's STRATEGIC entries. § 0 'Week at a glance' is derived: one
    bullet per critical/high strategic entry (headline + summary).
    `runs` are the week's weekly-kind run records."""
    strat = strategic_entries(week_entries)
    by_id = entries_by_id or {e["id"]: e for e in strat}
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in strat:
        buckets[weekly_section_key(e)].append(e)
    for k in buckets:
        buckets[k].sort(key=entry_sort_key)

    glance = [
        e for e in sorted(strat, key=entry_sort_key)
        if e.get("priority") in ("critical", "high")
    ]

    out: list[str] = []
    for key, title in WEEKLY_STRUCTURE:
        if key == "weekly-glance":
            inner = render_tldr_bullets(glance, prefix=prefix)
        elif key == "verification-notes":
            notes = [render_run_note(r, base_url=base_url) for r in runs or []]
            inner = "".join(notes) if notes else _empty_stub_html()
        else:
            section_entries = buckets.get(key, [])
            inner = (
                "".join(
                    render_entry_card(e, prefix=prefix, section_key=key,
                                      base_url=base_url, entries_by_id=by_id)
                    for e in section_entries
                )
                if section_entries else _empty_stub_html()
            )
        out.append(_section_shell(key, title, inner,
                                  collapsed=(key == "verification-notes")))
    return "".join(out)


# === LIVE BRIEF + DAY PAGES (v3) =======================================

DEFAULT_WINDOW_HOURS = 24
BRIEF_WINDOW_CHOICES = (6, 12, 24, 48, 72)
BRIEFBOOK_WINDOW_DAYS = 35
ALERTS_WINDOW_DAYS = 7


def _brief_filter_aside(entries: list[dict[str, Any]]) -> str:
    """Section TOC + tag/region filter chips (same DOM contract as v2 so
    filter.min.js + app.js keep working on day pages)."""
    all_tags = sorted({t for e in entries for t in (e.get("tags") or [])})
    all_regions = sorted({r for e in entries for r in (e.get("regions") or [])})

    def _toc_rows() -> str:
        rows = []
        for key, title in DAILY_SECTIONS:
            anchor = slugify(title)
            hidden = key == "verification-notes"
            rows.append(
                f'<li class="toc-row{" toc-row-hidden" if hidden else ""}" data-section-row="{_escape(anchor)}">'
                f'<a class="toc-link" href="#{_escape(anchor)}">{_escape(title)}</a>'
                f'<button type="button" class="toc-toggle" data-section-toggle="{_escape(anchor)}" '
                f'aria-pressed="{"false" if hidden else "true"}" aria-label="Toggle section visibility" title="Hide / show section">'
                '<svg viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
                '<path class="eye-open" d="M8 3.5c-3 0-5.5 2.4-6.5 4.5 1 2.1 3.5 4.5 6.5 4.5s5.5-2.4 6.5-4.5C13.5 5.9 11 3.5 8 3.5zm0 7.2a2.7 2.7 0 1 1 0-5.4 2.7 2.7 0 0 1 0 5.4z" fill="currentColor"/>'
                '<path class="eye-shut" d="M2 3l12 10" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
                "</svg></button></li>"
            )
        return "".join(rows)

    def _chips(values: list[str], attr: str) -> str:
        return "".join(
            f'<button type="button" class="filter-chip" data-filter-{attr}="{_escape(v)}" '
            f'aria-pressed="true" title="Toggle {_escape(v)}">{_escape(v)}</button>'
            for v in values
        )

    tag_group = (
        '<details class="filter-group" open><summary>Tags <span class="filter-count">'
        f'<span class="muted">({len(all_tags)})</span></span></summary>'
        f'<div class="filter-chip-row">{_chips(all_tags, "tag")}</div></details>'
    ) if all_tags else ""
    region_group = (
        '<details class="filter-group" open><summary>Regions <span class="filter-count">'
        f'<span class="muted">({len(all_regions)})</span></span></summary>'
        f'<div class="filter-chip-row">{_chips(all_regions, "region")}</div></details>'
    ) if all_regions else ""
    return (
        "<h3>On this page</h3>"
        f'<ul class="toc-sections">{_toc_rows()}</ul>'
        '<div class="toc-filters">'
        f"{tag_group}{region_group}"
        '<button type="button" class="filter-reset" data-action="clear-filters" hidden>Reset filters</button>'
        '<p class="filter-status" data-role="filter-status" hidden></p>'
        "</div>"
    )


def _ai_notice_html() -> str:
    return (
        '<aside class="brief-notice" role="note" aria-label="AI-generated content notice">'
        '<span class="brief-notice__label" aria-hidden="true">'
        '<svg viewBox="0 0 16 16" focusable="false" aria-hidden="true">'
        '<path fill="currentColor" d="M8 1.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13Zm0 1.5a5 5 0 1 1 0 10A5 5 0 0 1 8 3Zm-.75 2.25v3.5h1.5v-3.5h-1.5Zm0 4.5v1.5h1.5v-1.5h-1.5Z"/>'
        "</svg>"
        "<span>AI-generated · no human review</span>"
        "</span>"
        '<div class="brief-notice__body">Autonomous CTI pipeline output — every entry passed '
        "two-source verification, the mechanical self-check and an adversarial verifier loop, "
        "but no human reviewed it before publication.</div>"
        "</aside>"
    )


def render_runs_overview(
    all_entries: list[dict[str, Any]],
    all_runs: list[dict[str, Any]],
    *,
    prefix: str = "",
    limit: int = 10,
) -> str:
    """A compact readout of the last `limit` pipeline fires: when each
    finished, how many items it published and the per-brief-section
    breakdown. Entries are mapped to their fire via the `run_id` they
    carry in frontmatter. Static (window-independent) — the panel is the
    same whatever reading window the visitor picks."""
    counts_by_run: dict[str, Counter] = defaultdict(Counter)
    strategic_by_run: Counter = Counter()
    for e in all_entries:
        rid = e.get("run_id")
        if not rid:
            continue
        if (e.get("horizon") or "operational") != "operational":
            strategic_by_run[rid] += 1
            continue
        skey = entry_section_key(e)
        if skey:
            counts_by_run[rid][skey] += 1

    runs_sorted = sorted(
        (r for r in all_runs if r.get("run_id")),
        key=lambda r: str(r.get("completed") or r.get("started") or r.get("run_id")),
        reverse=True,
    )[:limit]
    if not runs_sorted:
        return ""

    rows: list[str] = []
    for r in runs_sorted:
        rid = str(r.get("run_id"))
        ts = parse_ts(r.get("completed") or r.get("started"))
        when = ts.strftime("%d.%m.%Y&nbsp;%H:%M") if ts else "—"
        kind = str(r.get("kind") or "intel")
        counts = counts_by_run.get(rid, Counter())
        total = sum(counts.values()) + strategic_by_run.get(rid, 0)

        cats: list[str] = []
        for key, _title in DAILY_SECTIONS:
            c = counts.get(key)
            if c:
                cats.append(
                    f'<span class="runs-cat"><span class="runs-cat__n">{c}</span>'
                    f'{_escape(SECTION_SHORT.get(key, key))}</span>'
                )
        if strategic_by_run.get(rid):
            cats.append(
                f'<span class="runs-cat"><span class="runs-cat__n">'
                f'{strategic_by_run[rid]}</span>Strategic</span>'
            )
        breakdown = (
            "".join(cats)
            if cats
            else '<span class="runs-cat runs-cat--none">quiet window</span>'
        )
        day = str(r.get("date") or "")
        run_label = (
            f'<a class="runs-row__run" href="{_escape(prefix)}briefs/{_escape(day)}/">'
            f'<span class="runs-row__kind runs-row__kind--{_escape(kind)}">{_escape(kind)}</span></a>'
            if day
            else f'<span class="runs-row__kind runs-row__kind--{_escape(kind)}">{_escape(kind)}</span>'
        )
        rows.append(
            '<li class="runs-row">'
            f'<span class="runs-row__when mono">{when}</span>'
            f"{run_label}"
            f'<span class="runs-row__total"><span class="runs-row__total-n">{total}</span>'
            f'<span class="runs-row__total-l">item{"" if total == 1 else "s"}</span></span>'
            f'<span class="runs-row__cats">{breakdown}</span>'
            "</li>"
        )

    latest = parse_ts(runs_sorted[0].get("completed") or runs_sorted[0].get("started"))
    latest_html = (
        f'<span class="runs-overview__latest">last update '
        f'<span class="mono">{latest.strftime("%d.%m.%Y&nbsp;%H:%M")}</span> UTC</span>'
        if latest else ""
    )
    # Collapsed by default (both breakpoints): the summary surfaces the most
    # recent fire so the reader sees freshness at a glance without expanding.
    return (
        '<details class="runs-overview">'
        '<summary class="runs-overview__summary">'
        '<span class="runs-overview__title">Recent pipeline runs</span>'
        f"{latest_html}"
        f'<span class="runs-overview__meta muted">{len(runs_sorted)} fires</span>'
        "</summary>"
        f'<ol class="runs-list">{"".join(rows)}</ol>'
        "</details>"
    )


def render_live_brief_page(
    window_entries: list[dict[str, Any]],
    window_runs: list[dict[str, Any]],
    *,
    all_entries: list[dict[str, Any]] | None = None,
    all_runs: list[dict[str, Any]] | None = None,
    ref_ts: datetime,
    entries_by_id: dict[str, dict[str, Any]],
    card_html_by_id: dict[str, str],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/brief/ — the dynamic window brief. The default window (last
    24 h relative to the build's reference moment) is fully
    server-rendered; brief.js re-renders #brief-sections client-side
    from data/briefbook.json when the reader changes the window."""
    ops = sorted(operational_entries(window_entries), key=entry_sort_key)
    n = len(ops)
    cve_count = len({c for e in ops for c in entry_cve_ids(e)})
    toc_html = _brief_filter_aside(ops)

    # The server-rendered default is an explicit clock window ending at the
    # build's reference moment (the newest published signal): [ref-24h, ref].
    # It is presented as a plain From→To range in European DD.MM.YYYY HH:MM
    # form — no "anchor" concept. brief.js re-computes presets against the
    # visitor's real clock and always fills the boxes with the exact range.
    win_to = ref_ts
    win_from = ref_ts - timedelta(hours=DEFAULT_WINDOW_HOURS)
    from_str = win_from.strftime("%d.%m.%Y %H:%M")
    to_str = win_to.strftime("%d.%m.%Y %H:%M")
    range_label = f"{from_str} &rarr; {to_str} UTC"

    meta_items = (
        '<div class="brief-meta">'
        '<div class="brief-meta__item brief-meta__item--lead brief-meta__item--live">'
        '<span class="brief-meta__label">Type</span>'
        '<span class="brief-meta__value"><span class="brief-meta__type brief-meta__type--live">live</span></span></div>'
        '<div class="brief-meta__item"><span class="brief-meta__label">Window</span>'
        f'<span class="brief-meta__value" data-window-label>last {DEFAULT_WINDOW_HOURS} h</span></div>'
        '<div class="brief-meta__item brief-meta__item--count"><span class="brief-meta__label">Entries</span>'
        f'<span class="brief-meta__value"><span class="brief-meta__count" data-window-entries>{n}</span></span></div>'
        '<div class="brief-meta__item brief-meta__item--count"><span class="brief-meta__label">CVEs</span>'
        f'<span class="brief-meta__value"><span class="brief-meta__count" data-window-cves>{cve_count}</span></span></div>'
        "</div>"
    )

    chips = "".join(
        f'<button type="button" class="chip{" active" if h == DEFAULT_WINDOW_HOURS else ""}" '
        f'data-window-hours="{h}">{h}h</button>'
        for h in BRIEF_WINDOW_CHOICES
    )
    control_bar = (
        '<div class="brief-controls" data-brief-controls>'
        '<div class="brief-controls__row brief-controls__row--presets">'
        '<span class="brief-controls__label" id="brief-window-label">Window</span>'
        '<div class="brief-seg" role="group" aria-labelledby="brief-window-label">'
        f"{chips}"
        "</div>"
        "</div>"
        '<div class="brief-controls__row brief-controls__row--range">'
        '<label class="brief-field"><span class="brief-field__label">From</span>'
        '<input type="text" inputmode="numeric" class="input brief-field__input" '
        f'data-window-from value="{_escape(from_str)}" placeholder="DD.MM.YYYY HH:MM" '
        'autocomplete="off" spellcheck="false" '
        'aria-label="Range start — UTC, format DD.MM.YYYY HH:MM" /></label>'
        '<label class="brief-field"><span class="brief-field__label">To</span>'
        '<input type="text" inputmode="numeric" class="input brief-field__input" '
        f'data-window-to value="{_escape(to_str)}" placeholder="DD.MM.YYYY HH:MM" '
        'autocomplete="off" spellcheck="false" '
        'aria-label="Range end — UTC, format DD.MM.YYYY HH:MM" /></label>'
        '<span class="brief-field__tz">UTC</span>'
        '<button type="button" class="brief-range-apply" data-window-apply>Apply</button>'
        "</div>"
        f'<p class="brief-controls__status" data-window-status>'
        f"Showing {n} entr{'y' if n == 1 else 'ies'} &middot; {range_label}</p>"
        "</div>"
    )
    console_note = (
        '<p class="muted brief-controls__note">Times are UTC. Presets are measured back from '
        "now; edit From / To for an exact range. Without JavaScript this page shows the last "
        f"{DEFAULT_WINDOW_HOURS} h up to the newest published signal.</p>"
    )
    runs_overview = render_runs_overview(
        all_entries if all_entries is not None else window_entries,
        all_runs if all_runs is not None else window_runs,
        prefix=prefix,
    )
    # The metadata band + window controls + recent-runs readout read as one
    # cohesive console panel directly under the title — a single full-width
    # card so the left content column never opens with a height-mismatch void.
    console = (
        '<section class="brief-console" aria-label="Window summary and controls">'
        f"{meta_items}"
        f"{control_bar}"
        f"{console_note}"
        f"{runs_overview}"
        "</section>"
    )

    # Data island: the grouping constants brief.js needs, embedded as a
    # non-executable JSON <script> (CSP-safe — application/json never runs).
    config = {
        "briefbook_url": "data/briefbook.json",
        "default_hours": DEFAULT_WINDOW_HOURS,
        "window_choices": list(BRIEF_WINDOW_CHOICES),
        "lens_regions": list(ORG_LENS_REGIONS),
        "priority_rank": PRIORITY_RANK,
        "kind_section": {k: v for k, v in KIND_DAILY_SECTION.items() if v},
        "sections": [
            {"key": k, "title": t, "anchor": slugify(t)} for k, t in DAILY_SECTIONS
        ],
        "empty_stub": SECTION_EMPTY_STUB,
        "generated_at": ref_ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "reference_ts": ref_ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    data_island = (
        '<script type="application/json" id="brief-config">'
        + _escape_json_island(json.dumps(config, sort_keys=True))
        + "</script>"
    )

    sections_html = render_brief_sections(
        ops, window_runs,
        prefix=prefix, base_url=canonical,
        entries_by_id=entries_by_id,
        card_html_by_id=card_html_by_id,
    )

    body = f"""
<header class="brief-page-head">
  <h1>Live brief</h1>
</header>
<article class="brief-layout brief-layout--live" data-brief-page data-filter="brief">
  {console}
  {data_island}
  <div class="brief-main">
    <details class="toc-mobile" data-filter="brief">
      <summary>On this page</summary>
      <div class="toc-mobile-body aside-toc">{toc_html}</div>
    </details>
    {_ai_notice_html()}
    <div class="brief-prose" id="brief-sections" data-default-hours="{DEFAULT_WINDOW_HOURS}">{sections_html}</div>
  </div>
  <aside class="aside-toc aside-toc--desktop" aria-label="In this brief" data-filter="brief">
    {toc_html}
  </aside>
</article>
"""
    top = ops[0] if ops else None
    description = (
        f"Live CTI brief — {n} entries in the current 24 h window."
        + (f" Top: {top.get('headline') or ''}" if top else "")
    )[:300]
    return base_template(
        title=f"Live brief — {SITE_NAME}",
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
        extra_head=f'<script defer src="{prefix}assets/js/brief.js?v={cachebust}"></script>',
    )


def _escape_json_island(payload: str) -> str:
    """Make a JSON payload safe inside a <script type="application/json">
    data island: forbid `</script>` breakouts and HTML comment openers."""
    return (
        payload.replace("</", "<\\/")
        .replace("<!--", "<\\u0021--")
    )


def render_day_page(
    day: str,
    day_entries: list[dict[str, Any]],
    day_runs: list[dict[str, Any]],
    *,
    entries_by_id: dict[str, dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/briefs/YYYY-MM-DD/ — static day archive: the UTC day's
    operational entries in the canonical daily structure + that day's
    run-record notes. Preserves the v2 daily-brief reading experience
    and URL shape."""
    ops = sorted(operational_entries(day_entries), key=entry_sort_key)
    sections_html = render_brief_sections(
        ops, day_runs, prefix=prefix, base_url=canonical,
        entries_by_id=entries_by_id,
    )
    toc_html = _brief_filter_aside(ops)
    n = len(ops)
    cve_count = len({c for e in ops for c in entry_cve_ids(e)})
    runs_label = f"{len(day_runs)} run{'' if len(day_runs) == 1 else 's'}"

    meta_items = (
        '<div class="brief-meta">'
        '<div class="brief-meta__item brief-meta__item--lead">'
        '<span class="brief-meta__label">Type</span>'
        '<span class="brief-meta__value"><span class="brief-meta__type">daily</span></span></div>'
        '<div class="brief-meta__item"><span class="brief-meta__label">Date</span>'
        f'<span class="brief-meta__value"><span class="mono">{_escape(day)}</span></span></div>'
        '<div class="brief-meta__item"><span class="brief-meta__label">Runs</span>'
        f'<span class="brief-meta__value">{_escape(runs_label)}</span></div>'
        '<div class="brief-meta__item brief-meta__item--count"><span class="brief-meta__label">Entries</span>'
        f'<span class="brief-meta__value"><span class="brief-meta__count">{n}</span></span></div>'
        + (
            '<div class="brief-meta__item brief-meta__item--count"><span class="brief-meta__label">CVEs</span>'
            f'<span class="brief-meta__value"><span class="brief-meta__count">{cve_count}</span></span></div>'
            if cve_count else ""
        )
        + "</div>"
    )

    title = f"CTI Daily Brief — {day}"
    body = f"""
<header class="brief-page-head">
  <h1>{_escape(title)}</h1>
</header>
<article class="brief-layout" data-brief="{_escape(day)}">
  {meta_items}
  <div class="brief-main">
    <details class="toc-mobile" data-filter="brief">
      <summary>On this page</summary>
      <div class="toc-mobile-body aside-toc">{toc_html}</div>
    </details>
    {_ai_notice_html()}
    <div class="brief-prose">{sections_html}</div>
  </div>
  <aside class="aside-toc aside-toc--desktop" aria-label="In this brief" data-filter="brief">
    {toc_html}
  </aside>
</article>
"""
    tldr = select_tldr_entries(ops)
    description = (tldr[0].get("summary") or "").strip()[:280] if tldr else f"Daily CTI brief for {day}."
    return base_template(
        title=title,
        description=description or f"Daily CTI brief for {day}.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_days_index_page(
    days: dict[str, list[dict[str, Any]]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/briefs/ — index of day pages grouped by month, newest first."""
    groups: dict[str, dict[str, Any]] = {}
    for day in sorted(days.keys(), reverse=True):
        key = day[:7]
        try:
            label = datetime.strptime(day, "%Y-%m-%d").strftime("%B %Y")
        except ValueError:
            label = key
        groups.setdefault(key, {"label": label, "days": []})["days"].append(day)

    section_html: list[str] = []
    for grp in groups.values():
        items_html = ""
        for day in grp["days"]:
            entries = days[day]
            n = len(entries)
            cves = len({c for e in entries for c in entry_cve_ids(e)})
            crit = sum(1 for e in entries if e.get("priority") == "critical")
            top = select_tldr_entries(entries)
            hint = (top[0].get("headline") or "") if top else ""
            haystack = " ".join(
                [day, hint] + [e.get("title") or "" for e in entries]
                + [c for e in entries for c in entry_cve_ids(e)]
            ).lower()
            items_html += (
                f'<li data-brief-kind="daily" data-brief-haystack="{_escape(haystack)}">'
                "<span>"
                f'<a class="e-title" href="{prefix}briefs/{_escape(day)}/">CTI Daily Brief — {_escape(day)}</a>'
                '<div class="e-meta">'
                f'<span class="e-tag">daily</span>'
                f'<span>{n} entr{"y" if n == 1 else "ies"}</span>'
                + (f"<span>{cves} CVE{'' if cves == 1 else 's'}</span>" if cves else "")
                + (f'<span class="badge badge--crit">{crit} critical</span>' if crit else "")
                + "</div>"
                + (f'<div class="e-meta"><span class="muted">{_inline_text(hint[:160])}</span></div>' if hint else "")
                + "</span>"
                f'<span class="mono muted">{_escape(day)}</span>'
                "</li>"
            )
        section_html.append(
            f'<section style="margin-top:1.4rem"><h2 class="section-head">{_escape(grp["label"])}</h2>'
            f'<ul class="entity-list" data-filter-list="briefs">{items_html}</ul></section>'
        )

    n_days = len(days)
    body = f"""
<h1>Daily briefs</h1>
<p class="subtitle">{n_days} archived day page{'' if n_days == 1 else 's'}, newest first. Each day page renders that UTC day's published entries in the canonical brief structure. For the rolling window view, read the <a href="{prefix}brief/">live brief</a>.</p>

<div class="toolbar">
  <input class="input" id="briefs-q" type="search" placeholder="Filter by date, headline, or CVE…" autocomplete="off" spellcheck="false" data-filter-input="briefs" />
</div>
{''.join(section_html) or '<div class="empty">No entries published yet.</div>'}
"""
    return base_template(
        title=f"Daily briefs — {SITE_NAME}",
        description=f"{n_days} archived daily brief day pages, newest first.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === WEEKLY PAGES (v3) =================================================


def render_weekly_page(
    week: str,
    week_entries: list[dict[str, Any]],
    week_runs: list[dict[str, Any]],
    *,
    entries_by_id: dict[str, dict[str, Any]],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/weekly/YYYY-Www/ — the week's strategic entries in the v2
    12-section weekly structure, referenced operational entries linked
    in place (each card's `Builds on:` line)."""
    strat = strategic_entries(week_entries)
    sections_html = render_weekly_sections(
        strat, week_runs, prefix=prefix, base_url=canonical,
        entries_by_id=entries_by_id,
    )
    n = len(strat)
    title = f"CTI Weekly Summary — {week}"
    body = f"""
<header class="brief-page-head">
  <h1>{_escape(title)}</h1>
</header>
<article class="brief-layout" data-brief="{_escape(week)}">
  <div class="brief-meta">
    <div class="brief-meta__item brief-meta__item--lead">
      <span class="brief-meta__label">Type</span>
      <span class="brief-meta__value"><span class="brief-meta__type">weekly</span></span></div>
    <div class="brief-meta__item"><span class="brief-meta__label">ISO week</span>
      <span class="brief-meta__value"><span class="mono">{_escape(week)}</span></span></div>
    <div class="brief-meta__item brief-meta__item--count"><span class="brief-meta__label">Entries</span>
      <span class="brief-meta__value"><span class="brief-meta__count">{n}</span></span></div>
  </div>
  <div class="brief-main">
    {_ai_notice_html()}
    <div class="brief-prose">{sections_html}</div>
  </div>
</article>
"""
    glance = [e for e in strat if e.get("priority") in ("critical", "high")]
    description = (glance[0].get("summary") or "").strip()[:280] if glance else f"Weekly CTI summary — {week}."
    return base_template(
        title=title,
        description=description or f"Weekly CTI summary — {week}.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_weekly_index_page(
    weeks: dict[str, list[dict[str, Any]]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/weekly/ — index of weekly pages, newest first."""
    items_html = ""
    for week in sorted(weeks.keys(), reverse=True):
        entries = strategic_entries(weeks[week])
        n = len(entries)
        top = [e for e in sorted(entries, key=entry_sort_key)
               if e.get("priority") in ("critical", "high")]
        hint = (top[0].get("headline") or "") if top else ""
        items_html += (
            "<li><span>"
            f'<a class="e-title" href="{prefix}weekly/{_escape(week)}/">CTI Weekly Summary — {_escape(week)}</a>'
            '<div class="e-meta">'
            f'<span class="e-tag">weekly</span>'
            f'<span>{n} strategic entr{"y" if n == 1 else "ies"}</span>'
            "</div>"
            + (f'<div class="e-meta"><span class="muted">{_inline_text(hint[:160])}</span></div>' if hint else "")
            + "</span>"
            f'<span class="mono muted">{_escape(week)}</span>'
            "</li>"
        )
    n_weeks = len(weeks)
    body = f"""
<h1>Weekly summaries</h1>
<p class="subtitle">{n_weeks} weekly summar{'y' if n_weeks == 1 else 'ies'}, newest first — the strategic lens over each ISO week: multi-day chains, research and threat-actor developments, annual reports, policy, and the look ahead.</p>
{('<ul class="entity-list">' + items_html + '</ul>') if items_html else '<div class="empty">No weekly summaries yet.</div>'}
"""
    return base_template(
        title=f"Weekly summaries — {SITE_NAME}",
        description=f"{n_weeks} weekly CTI summaries, newest first.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === PER-ENTRY PERMALINK (v3) ==========================================


def render_entry_page(
    entry: dict[str, Any],
    *,
    entries_by_id: dict[str, dict[str, Any]],
    updated_by: dict[str, list[str]],
    registry: dict[str, dict[str, Any]],
    runs_by_id: dict[str, dict[str, Any]],
    day_pages: set[str],
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """/entries/YYYY-MM-DD/<slug>/ — full metadata badge block, body,
    evidence, actions, sources with roles, the update chain, entity
    links, and the part-of-run link."""
    body_html = enhance_brief_item_html(
        render_markdown(entry.get("body") or "", base_url=canonical)
    )
    is_op = (entry.get("horizon") or "operational") == "operational"
    day = entry["date"]
    parent_url = (
        f"{prefix}briefs/{day}/" if (is_op and day in day_pages)
        else f"{prefix}weekly/{iso_week_of_entry(entry)}/" if not is_op and iso_week_of_entry(entry)
        else f"{prefix}briefs/"
    )
    parent_label = f"Daily brief {day}" if is_op else f"Weekly {iso_week_of_entry(entry) or ''}"

    # --- update chain -------------------------------------------------
    chain_bits: list[str] = []
    target = str(entry.get("update_of") or "")
    if target:
        orig = entries_by_id.get(target)
        chain_bits.append(
            '<li><span class="e-tag">updates</span> '
            f'<a href="{prefix}entries/{_escape(target)}/">'
            f'{_escape((orig or {}).get("title") or target)}</a>'
            f' <span class="mono muted">{_escape(target.split("/", 1)[0])}</span></li>'
        )
    for uid in updated_by.get(entry["id"], []):
        upd = entries_by_id.get(uid)
        chain_bits.append(
            '<li><span class="e-tag">updated by</span> '
            f'<a href="{prefix}entries/{_escape(uid)}/">'
            f'{_escape((upd or {}).get("title") or uid)}</a>'
            f' <span class="mono muted">{_escape(uid.split("/", 1)[0])}</span></li>'
        )
    chain_html = (
        '<section class="entry-chain"><h2 class="section-head">Update chain</h2>'
        f'<ul class="entity-list">{"".join(chain_bits)}</ul></section>'
    ) if chain_bits else ""

    # --- entities ------------------------------------------------------
    ent_bits: list[str] = []
    for key in entry.get("entities") or []:
        ent = registry.get(key) or {}
        ent_bits.append(
            f'<a class="pill pill-tag" href="{prefix}entities/{urllib.parse.quote(str(key), safe="")}/">'
            f'{_escape(ent.get("name") or str(key))}</a>'
        )
    entities_html = (
        '<p class="entry-entities"><strong>Entities:</strong> ' + " ".join(ent_bits) + "</p>"
    ) if ent_bits else ""

    # --- actions ------------------------------------------------------
    actions = [a for a in (entry.get("actions") or []) if isinstance(a, str) and a.strip()]
    actions_html = (
        '<section><h2 class="section-head">Action items</h2><ul class="action-list">'
        + "".join(
            f'<li class="action-list__item"><div class="action-list__body">'
            f"{render_inline(a.strip(), base_url=canonical)}</div></li>"
            for a in actions
        )
        + "</ul></section>"
    ) if actions else ""

    # --- run lineage ----------------------------------------------------
    rid = str(entry.get("run_id") or "")
    run = runs_by_id.get(rid)
    run_html = ""
    if rid:
        run_link = f'{prefix}ops/#run={urllib.parse.quote(rid, safe="")}'
        run_meta = ""
        if run:
            bits = [str(run.get("kind") or "")]
            if run.get("model"):
                bits.append(str(run["model"]))
            run_meta = " · ".join(b for b in bits if b)
        run_html = (
            '<p class="entry-run muted">Part of run '
            f'<a class="mono" href="{_escape(run_link)}">{_escape(rid)}</a>'
            + (f' <span class="muted">({_escape(run_meta)})</span>' if run_meta else "")
            + "</p>"
        )

    ia_html = render_immediate_action_callout(entry, prefix=prefix)
    update_lead = render_update_lead(entry, prefix=prefix, entries_by_id=entries_by_id)

    body = f"""
<article class="single-item entry-page">
  <p class="subtitle"><a href="{prefix}">Home</a> · <a href="{prefix}brief/">Live brief</a> · <a href="{_escape(parent_url)}">{_escape(parent_label)}</a></p>
  <h1>{_escape(entry.get("title") or entry["id"])}</h1>
  {render_entry_badges(entry, prefix=prefix)}
  {entities_html}
  {run_html}
  {ia_html}
  {update_lead}
  <div class="brief-prose">{body_html}</div>
  {render_entry_evidence(entry)}
  {actions_html}
  {chain_html}
  {render_entry_taxonomy(entry, prefix=prefix)}
  {render_entry_sources(entry, with_roles=True)}
</article>
"""
    description = (entry.get("summary") or "").strip()[:280] or (entry.get("headline") or "")[:280]
    return base_template(
        title=entry.get("title") or entry["id"],
        description=description,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


def render_embedded_entries_section(
    entries: list[dict[str, Any]],
    *,
    heading: str,
    empty_text: str,
    prefix: str,
    entries_by_id: dict[str, dict[str, Any]] | None = None,
    limit: int = 20,
) -> str:
    """Full entry cards embedded on an entity page (newest first) — the
    v3 replacement for the v2 brief-item embeds."""
    if not entries:
        return (
            f'<h2 class="section-head" style="margin-top:1.5rem">{_escape(heading)}</h2>'
            f'<p class="muted">{_escape(empty_text)}</p>'
        )
    ordered = sorted(
        entries,
        key=lambda e: (str(e.get("discovered_at") or ""), e.get("id") or ""),
        reverse=True,
    )
    shown = ordered[:limit]
    cards = "".join(
        '<article class="embedded-item">'
        '<header class="embedded-item__head">'
        '<p class="embedded-item__lineage muted">'
        f'{_escape(e["date"])} · <a class="embedded-item__permalink" href="{prefix}{entry_url_path(e)}">view entry permalink &rarr;</a>'
        "</p></header>"
        f'<div class="embedded-item__body brief-prose">'
        + render_entry_card(e, prefix=prefix, entries_by_id=entries_by_id)
        + "</div></article>"
        for e in shown
    )
    more = (
        f'<p class="muted">+ {len(ordered) - limit} earlier entries — see the timeline above.</p>'
        if len(ordered) > limit else ""
    )
    return (
        f'<h2 class="section-head" style="margin-top:1.5rem">{_escape(heading)} ({len(ordered)})</h2>'
        f'<div class="embedded-items">{cards}{more}</div>'
    )


# === HOME (v3) =========================================================


def _home_tldr_list(picked: list[dict[str, Any]], *, cap_chars: int = 240) -> str:
    """Compact TL;DR bullet list for a home feature card — headline +
    (length-capped) summary + a permalink arrow, one bullet per picked
    entry."""
    lis: list[str] = []
    for e in picked:
        url = entry_url_path(e)
        headline = (e.get("headline") or e.get("title") or e["id"]).strip().strip("*").rstrip(".")
        summ = (e.get("summary") or "").strip()
        if len(summ) > cap_chars:
            summ = summ[: cap_chars - 1].rstrip() + "…"
        lis.append(
            "<li>"
            f"<strong>{_inline_text(headline)}.</strong> "
            f"{_inline_text(summ)} "
            f'<a href="{_escape(url)}">→</a>'
            "</li>"
        )
    return f"<ul>{''.join(lis)}</ul>" if lis else ""


def render_home_page(
    *,
    today: str | None,
    today_entries: list[dict[str, Any]],
    prev_day: str | None,
    prev_day_entries: list[dict[str, Any]],
    latest_week: str | None,
    latest_week_entries: list[dict[str, Any]],
    site_url: str,
    cachebust: str,
    canonical: str,
) -> str:
    """Home — hero + three feature cards, each leading with its TL;DR:
    (1) the current day's live entries, (2) the previous — now completed —
    day's brief, (3) the latest weekly summary."""
    redirect_js = f'<script src="assets/js/spa-redirect.js?v={cachebust}"></script>'

    # (1) Live — the current day's entries, still being appended to.
    if today:
        live_ops = sorted(operational_entries(today_entries), key=entry_sort_key)
        live_tldr = _home_tldr_list(select_tldr_entries(live_ops))
        live_card = (
            '<section class="home-today home-today--live">'
            '<p class="home-today-eyebrow">Live — today</p>'
            f"<h2>CTI Daily Brief — {_escape(today)}</h2>"
            f'<p class="muted">{len(live_ops)} entr{"y" if len(live_ops) == 1 else "ies"} '
            f"published so far today — updates through the day.</p>"
            + (live_tldr or '<p class="muted">A quiet day so far — no new verified signal yet.</p>')
            + '<p class="home-today-cta"><a class="cta" href="brief/">Open the live brief →</a></p>'
            "</section>"
        )
    else:
        live_card = (
            '<section class="home-today home-today--live">'
            '<p class="home-today-eyebrow">Live — today</p>'
            '<p class="muted">No entries published yet — the first pipeline run will open today\'s brief.</p>'
            '<p class="home-today-cta"><a class="cta" href="brief/">Open the live brief →</a></p>'
            "</section>"
        )

    # (2) Latest completed day — the day before today, now finalised.
    if prev_day:
        day_ops = sorted(operational_entries(prev_day_entries), key=entry_sort_key)
        day_tldr = _home_tldr_list(select_tldr_entries(day_ops))
        day_card = (
            '<section class="home-today home-today--daily">'
            '<p class="home-today-eyebrow">Completed daily brief</p>'
            f"<h2>CTI Daily Brief — {_escape(prev_day)}</h2>"
            f'<p class="muted">{len(day_ops)} entr{"y" if len(day_ops) == 1 else "ies"} '
            f"published on {_escape(prev_day)}.</p>"
            + (day_tldr or "")
            + f'<p class="home-today-cta"><a class="cta" href="briefs/{_escape(prev_day)}/">Read the day page →</a></p>'
            "</section>"
        )
    else:
        day_card = (
            '<section class="home-today home-today--daily">'
            '<p class="home-today-eyebrow">Completed daily brief</p>'
            '<p class="muted">No completed day yet — the previous day\'s brief appears here once a new day begins.</p>'
            "</section>"
        )

    # (3) Latest weekly summary.
    if latest_week:
        strat = sorted(strategic_entries(latest_week_entries), key=entry_sort_key)
        glance = [e for e in strat if e.get("priority") in ("critical", "high")][:6]
        weekly_card = (
            '<section class="home-today home-today--weekly">'
            '<p class="home-today-eyebrow">This week\'s summary</p>'
            f"<h2>CTI Weekly Summary — {_escape(latest_week)}</h2>"
            f'<p class="muted">{len(strat)} strategic entr{"y" if len(strat) == 1 else "ies"} this ISO week.</p>'
            + (_home_tldr_list(glance) or "")
            + f'<p class="home-today-cta"><a class="cta" href="weekly/{_escape(latest_week)}/">Read the full weekly →</a></p>'
            "</section>"
        )
    else:
        weekly_card = (
            '<section class="home-today home-today--weekly">'
            '<p class="home-today-eyebrow">This week\'s summary</p>'
            '<p class="muted">No weekly summary yet — published Sundays.</p>'
            "</section>"
        )

    body = f"""
<section class="home-hero">
  <h1>{_escape(SITE_NAME)}</h1>
  <p class="lede">{_escape(HOME_LEDE)}</p>
</section>

<div class="home-today-grid home-today-grid--three">
{live_card}
{day_card}
{weekly_card}
</div>

{redirect_js}
"""
    return base_template(
        title=f"{SITE_NAME} — {TAGLINE}",
        description=HOME_META_DESCRIPTION,
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix="",
    )


# === BRIEFBOOK + ALERTS JSON (v3) ======================================


def build_briefbook(
    entries: list[dict[str, Any]],
    runs: list[dict[str, Any]],
    *,
    ref_ts: datetime,
    prefix: str = "../",
    card_html_by_id: dict[str, str] | None = None,
) -> dict[str, Any]:
    """data/briefbook.json — the last BRIEFBOOK_WINDOW_DAYS days of
    entries (both horizons; brief.js filters operational) and runs, each
    entry carrying the SAME server-rendered card HTML the day pages use.
    `prefix` is /brief/'s path back to the site root (the only consumer
    of the embedded HTML)."""
    since = ref_ts - timedelta(days=BRIEFBOOK_WINDOW_DAYS)
    window = content_model.entries_in_window(entries, since, None)
    by_id = {e["id"]: e for e in entries}
    updated_by = build_update_chains(entries)

    out_entries: list[dict[str, Any]] = []
    for e in sorted(window, key=lambda x: (str(x.get("discovered_at") or ""), x["id"]),
                    reverse=True):
        ia = e.get("immediate_action")
        ia_out = None
        if isinstance(ia, dict):
            ia_out = {
                "title": str(ia.get("title") or ""),
                "action": str(ia.get("action") or "").strip(),
            }
            for ev in e.get("evidence") or []:
                if isinstance(ev, dict) and ev.get("quote"):
                    ia_out["evidence_quote"] = str(ev["quote"])
                    ia_out["evidence_publisher"] = str(ev.get("publisher") or "")
                    break
        if card_html_by_id is not None and e["id"] in card_html_by_id:
            html = card_html_by_id[e["id"]]
        else:
            html = render_entry_card(e, prefix=prefix, entries_by_id=by_id)
            if card_html_by_id is not None:
                card_html_by_id[e["id"]] = html
        out_entries.append({
            "id": e["id"],
            "url": prefix + entry_url_path(e),
            "date": e["date"],
            "discovered_at": e.get("discovered_at"),
            "kind": e.get("kind"),
            "horizon": e.get("horizon") or "operational",
            "priority": e.get("priority") or "notable",
            "headline": e.get("headline") or "",
            "summary": (e.get("summary") or "").strip(),
            "title": e.get("title") or e["id"],
            "tags": list(e.get("tags") or []),
            "regions": list(e.get("regions") or []),
            "sectors": list(e.get("sectors") or []),
            "entities": list(e.get("entities") or []),
            "cve_ids": entry_cve_ids(e),
            "cve_status": entry_cve_status_union(e),
            "update_of": e.get("update_of"),
            "updated_by": updated_by.get(e["id"], []),
            "deep_dive": bool(e.get("deep_dive")),
            "actions": [a for a in (e.get("actions") or []) if isinstance(a, str)],
            "watchlist_hit": bool(e.get("watchlist_hit")),
            "verification": e.get("verification"),
            "immediate_action": ia_out,
            "html": html,
        })

    out_runs: list[dict[str, Any]] = []
    for r in runs_in_window(runs, since, None):
        out_runs.append({
            "run_id": r.get("run_id"),
            "url": f"{prefix}briefs/{r.get('date')}/",
            "date": r.get("date"),
            "kind": r.get("kind"),
            "started": r.get("started"),
            "completed": r.get("completed"),
            "window_hours": r.get("window_hours"),
            "gap_hours": r.get("gap_hours"),
            "model": r.get("model"),
            "entries_published": r.get("entries_published"),
            "html": render_markdown(r.get("body") or ""),
        })

    return {
        "generated_at": ref_ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_days": BRIEFBOOK_WINDOW_DAYS,
        "entries": out_entries,
        "runs": out_runs,
    }


ALERTS_COMMENT = (
    "Notification-hook surface: the last 7 days of priority critical|high "
    "entries, newest first. Poll this file and alert on new `id` values; "
    "`immediate_action` is non-null exactly when priority is critical. "
    "URLs are absolute. Schema: {id, url, priority, headline, summary, "
    "discovered_at, immediate_action:{title,action}|null, cve_ids[], "
    "entities[], tags[], sectors[], regions[]}. See docs/pipeline.md."
)


def build_alerts(
    entries: list[dict[str, Any]],
    *,
    ref_ts: datetime,
    site_url: str,
) -> dict[str, Any]:
    """data/alerts.json — last ALERTS_WINDOW_DAYS days of critical/high
    entries; the notification-hook surface."""
    since = ref_ts - timedelta(days=ALERTS_WINDOW_DAYS)
    window = content_model.entries_in_window(entries, since, None)
    alerts: list[dict[str, Any]] = []
    for e in sorted(window, key=lambda x: (str(x.get("discovered_at") or ""), x["id"]),
                    reverse=True):
        if e.get("priority") not in ("critical", "high"):
            continue
        ia = e.get("immediate_action")
        alerts.append({
            "id": e["id"],
            "url": site_url + entry_url_path(e),
            "priority": e.get("priority"),
            "headline": e.get("headline") or "",
            "summary": (e.get("summary") or "").strip(),
            "discovered_at": e.get("discovered_at"),
            "immediate_action": (
                {"title": str(ia.get("title") or ""), "action": str(ia.get("action") or "").strip()}
                if isinstance(ia, dict) else None
            ),
            "cve_ids": entry_cve_ids(e),
            "entities": list(e.get("entities") or []),
            "tags": list(e.get("tags") or []),
            "sectors": list(e.get("sectors") or []),
            "regions": list(e.get("regions") or []),
        })
    return {
        "_comment": ALERTS_COMMENT,
        "generated_at": ref_ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "window_days": ALERTS_WINDOW_DAYS,
        "alerts": alerts,
    }


# === CVE LIST (filtered view of /entities/) ===========================
# CVE detail lives in `render_entity_page` (one renderer for every entity
# type). This section only owns the type-filtered listing page at
# /cves/. The legacy /cves/<id>/ URLs are HTML meta-refresh stubs to
# /entities/CVE-<id>/, emitted by `render_redirect_page`.

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
        # Unified entity model: `appearances` is now the structured list
        # `[{date, section, brief_path, delta_summary}]`; the flat list
        # of brief names lives on `briefs`. Iterate the flat list here.
        names = c.get("briefs") or []
        app_links = "".join(
            f'<a href="{prefix}briefs/{_escape(n)}/" class="mono" style="margin-right:0.4rem">{_escape(n)}</a>'
            for n in names
        )
        rows.append(
            f'<tr>'
            f'<td class="cve-id"><a href="{prefix}entities/{_escape(c["id"])}/">{_escape(c["id"])}</a></td>'
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

    chart_block = render_overview_charts(cves, prefix=prefix, label="CVEs")
    body = f"""
<h1>CVEs</h1>
<p class="subtitle">{len(cves)} CVE{'' if len(cves) == 1 else 's'} referenced across all briefs. Click an ID for the full appearance trail.</p>

{chart_block}

<div class="toolbar" style="margin-top:1rem">
  <input class="input" id="cves-q" type="search" placeholder="Filter by CVE id, title, or brief date…" autocomplete="off" spellcheck="false" data-filter-input="cves" />
</div>
{table}
"""
    return base_template(
        title=f"CVEs — {SITE_NAME}",
        description=f"{len(cves)} CVEs referenced across all briefs.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )



# === TOPIC LIST (filtered view of /entities/) =========================
# Topic detail lives in `render_entity_page` (one renderer for every
# entity type). This section only owns the type-filtered listing page
# at /topics/. The legacy /topics/<key>/ URLs are HTML meta-refresh
# stubs to /entities/<key>/, emitted by `render_redirect_page`.

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
            '<li data-topic-type="' + _escape(t.get("type", "")) + '" data-topic-flags="' + _escape(",".join(f.upper() for f in t.get("flags", []))) + '">'
            f'<span>'
            f'<a class="e-title" href="{prefix}entities/{urllib.parse.quote(t["key"], safe="")}/">{_escape(t.get("title") or t["key"])}</a>'
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

    chart_block = render_overview_charts(topics, prefix=prefix, label="topics")
    body = f"""
<h1>Topics</h1>
<p class="subtitle">Actors, campaigns, malware, tools, incidents, reports, trends and policy items tracked across the pipeline. The badge marks entities covered on more than one day — these are the "stories that unfolded".</p>

{chart_block}

<div class="toolbar" style="margin-top:1rem">
  <input class="input" id="topics-q" type="search" placeholder="Filter topics…" autocomplete="off" spellcheck="false" data-filter-input="topics" />
  <span class="chip active" data-filter-chip="topic-type" data-value="all">All types</span>
  {type_chips}
</div>
<div class="toolbar" style="margin-top:-0.5rem">
  <span class="chip active" data-filter-chip="topic-flag" data-value="all">All verification</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="multi" title="Entities whose entries all held two-source verification">Corroborated</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE">Single-source</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE-NATIONAL-CERT">National-CERT carve-out</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="SINGLE-SOURCE-VICTIM">Victim disclosure</span>
  <span class="chip" data-filter-chip="topic-flag" data-value="CONTRADICTED">Contradicted</span>
</div>

{list_html}
"""
    return base_template(
        title=f"Topics — {SITE_NAME}",
        description=f"{len(topics)} tracked topics — CVEs, actors, campaigns, incidents, tools.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )



# === SOURCE LIST + DETAIL ==============================================

def _stale_days_for_source(s: dict[str, Any], today: date) -> int:
    """Days since `last_successful_fetch`. Returns -1 if the source
    has never been successfully fetched (or the field is malformed). Caller
    decides whether to flag negative as 'never fetched' or 'stale forever'."""
    lf = s.get("last_successful_fetch")
    if not lf or not re.match(r"^\d{4}-\d{2}-\d{2}$", str(lf)):
        return -1
    try:
        dt = datetime.strptime(lf, "%Y-%m-%d").date()
        return (today - dt).days
    except ValueError:
        return -1


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
    today = datetime.now(timezone.utc).date()

    cat_chips = "".join(
        f'<span class="chip" data-filter-chip="source-cat" data-value="{_escape(c)}">{_escape(c)}</span>'
        for c in cats
    )
    status_chips = "".join(
        f'<span class="chip" data-filter-chip="source-status" data-value="{_escape(s)}">{_escape(s)}</span>'
        for s in stats
    )

    # (The "Stale active sources" dedicated section was removed; the
    # main sources table still carries a `data-source-stale` attribute
    # per row + a "Stale only" filter chip in the toolbar that lets the
    # reader narrow the existing table to silent-active sources without
    # a separate block.)

    rows = []
    for s in sources:
        appearances = s.get("appearances", []) or []
        app_links = "".join(
            f'<span class="mono" style="margin-right:0.3rem">{_escape(n)}</span>'
            for n in appearances[:6]
        )
        if len(appearances) > 6:
            app_links += f' <span class="muted">+{len(appearances) - 6}</span>'
        cat_tags = "".join(
            f'<span class="e-tag">{_escape(c)}</span>'
            for c in (s.get("category") or [])
        )
        # Stale data attribute so the "Stale" filter chip can
        # toggle the table to silent-active sources only.
        days = _stale_days_for_source(s, today)
        is_stale_active = (s.get("status") == "active") and (days == -1 or days > 7)
        stale_attr = "yes" if is_stale_active else "no"
        rows.append(
            f'<tr data-source-cats="{_escape(",".join(s.get("category") or []))}" '
            f'data-source-status="{_escape(s.get("status") or "")}" '
            f'data-source-stale="{stale_attr}">'
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

    chart_block = render_sources_overview_charts(sources, prefix=prefix)
    body = f"""
<h1>Sources</h1>
<p class="subtitle">{len(sources)} curated source{'' if len(sources) == 1 else 's'}. Each source can be searched and shows the entries that have cited it.</p>

{chart_block}

<div class="toolbar" style="margin-top:1rem">
  <input class="input" id="sources-q" type="search" placeholder="Filter by name, id, notes, URL…" autocomplete="off" spellcheck="false" data-filter-input="sources" />
  <span class="chip active" data-filter-chip="source-cat" data-value="all">All categories</span>
  {cat_chips}
</div>
<div class="toolbar" style="margin-top:-0.5rem">
  <span class="chip active" data-filter-chip="source-status" data-value="all">All statuses</span>
  {status_chips}
  <span class="chip" data-filter-chip="source-stale" data-value="yes" title="Active sources whose last successful fetch is &gt; 7 days ago">Stale only</span>
</div>

{table}
"""
    return base_template(
        title=f"Sources — {SITE_NAME}",
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
    # Per-source citation timeline — same ISO-week bucketing the entity
    # pages use, zero-filled across the source's coverage span. Quick
    # at-a-glance read of "is this source still active in our coverage
    # cadence or is it slipping out of rotation?".
    spark_block = ""
    if appearances:
        wk_counts: dict[str, int] = {}
        for n in appearances:
            wk = _iso_week_of(n)
            if wk:
                wk_counts[wk] = wk_counts.get(wk, 0) + 1
        timeline = _fill_weekly_timeline(sorted(wk_counts.items()))
        spark_values = [float(c) for _, c in timeline]
        if spark_values:
            spark_svg = _ops_svg_sparkline(
                spark_values, width=300, height=48,
                label=f"Citations per ISO week for {source.get('publisher') or source['id']}",
            )
            spark_block = (
                '<div class="ops-chart-card" style="margin-top:1rem">'
                '<h3 class="section-head" style="margin-top:0">Citation cadence</h3>'
                '<p class="muted" style="font-size:0.78rem;margin:0 0 0.3rem">'
                f'Citation days per ISO week ({len(timeline)} weeks of coverage span, '
                f'total {sum(int(c) for _, c in timeline)}).'
                '</p>'
                f'{spark_svg}'
                '</div>'
            )

    entry_refs = source.get("entry_refs", []) or []
    if entry_refs:
        app_lis = []
        for ref in entry_refs[:60]:
            app_lis.append(
                f'<li><span><a class="e-title" href="{prefix}entries/{_escape(ref["id"])}/">{_escape(ref["title"])}</a></span>'
                f'<span class="mono muted">{_escape(ref["date"])}</span></li>'
            )
        if len(entry_refs) > 60:
            app_lis.append(f'<li class="muted">+ {len(entry_refs) - 60} earlier entries</li>')
        appearances_block = f'<ul class="entity-list">{"".join(app_lis)}</ul>'
    else:
        appearances_block = '<p class="muted">Not cited in any entry yet.</p>'

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

<h2 class="section-head" style="margin-top:1.5rem">Cited in {len(entry_refs)} entr{'y' if len(entry_refs) == 1 else 'ies'}</h2>
{spark_block}
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



# === TRENDS DASHBOARD ====================================

# Trend "cohorts" — each tile on /trends/ aggregates by week the count of
# items whose footer carries any of the listed taxonomy values. Cohorts
# match the audience's mental model (a SOC manager skimming the site
# monthly) rather than every taxonomy value verbatim. Add cohorts here
# as the brief's coverage shifts; never silently rename one (entity URLs
# don't move, but the trend chart's labels do).
_DEFAULT_TREND_COHORTS: list[dict[str, Any]] = [
    {
        "key": "ransomware",
        "title": "Ransomware items / week",
        "tags": ("ransomware",),
        "sectors": (),
        "regions": (),
        "match": "any",
    },
    {
        "key": "actively-exploited",
        "title": "Actively-exploited vulnerabilities / week",
        "tags": ("actively-exploited", "vulnerabilities"),
        "sectors": (),
        "regions": (),
        "match": "all",
    },
    {
        "key": "public-sector",
        "title": "Public-sector items / week",
        "tags": (),
        "sectors": ("public-sector",),
        "regions": (),
        "match": "any",
    },
    {
        "key": "ot-ics",
        "title": "OT / ICS items / week",
        "tags": ("ot-ics",),
        "sectors": ("energy", "water", "manufacturing", "transport"),
        "regions": (),
        "match": "any",
    },
    {
        "key": "supply-chain",
        "title": "Supply-chain items / week",
        "tags": ("supply-chain",),
        "sectors": (),
        "regions": (),
        "match": "any",
    },
    {
        "key": "ai-abuse",
        "title": "AI-abuse items / week",
        "tags": ("ai-abuse",),
        "sectors": (),
        "regions": (),
        "match": "any",
    },
    {
        "key": "ch-eu",
        "title": "Switzerland + Europe items / week",
        "tags": (),
        "sectors": (),
        "regions": ("switzerland", "dach", "europe"),
        "match": "any",
    },
    {
        "key": "nation-state",
        "title": "Nation-state items / week",
        "tags": ("nation-state", "espionage",
                 "china-nexus", "russia-nexus",
                 "north-korea-nexus", "iran-nexus"),
        "sectors": (),
        "regions": (),
        "match": "any",
    },
]

# config/branding.yaml `trends.cohorts` replaces the default cohort set
# wholesale when non-empty (a fork tracking a different region/sector lens
# redefines the tiles without touching this file).
TREND_COHORTS: list[dict[str, Any]] = branding_config.trend_cohorts(
    BRANDING, _DEFAULT_TREND_COHORTS
)

TRENDS_PAGE_DESCRIPTION = (
    "Weekly trend dashboard across all CTI briefs — ransomware, "
    "actively-exploited vulnerabilities, public-sector, OT/ICS, "
    "supply-chain, AI-abuse, Switzerland + Europe, nation-state."
    if TREND_COHORTS is _DEFAULT_TREND_COHORTS
    else "Weekly trend dashboard across all CTI briefs — "
    + ", ".join(c["title"] for c in TREND_COHORTS) + "."
)


def _trends_cohort_note(prefix: str) -> str:
    """Explanatory paragraph under the trends grid. The upstream default
    prose names the default cohorts' framing; a custom cohort set gets a
    neutral line instead."""
    if TREND_COHORTS is _DEFAULT_TREND_COHORTS:
        return (
            "<p>The cohorts are coarse on purpose: they're the questions a "
            "Swiss / EU public-sector SOC manager would ask scanning the site "
            'monthly ("are we seeing more ransomware?", "is OT/ICS '
            'escalating?", "did public-sector targeting move?"). For finer '
            f'slicing, use the per-tag list pages under <a href="{prefix}tags/">/tags/</a>.</p>'
        )
    return (
        "<p>The cohorts are coarse on purpose — they mirror the deployment's "
        "trend cohorts in config/branding.yaml. For finer slicing, use the "
        f'per-tag list pages under <a href="{prefix}tags/">/tags/</a>.</p>'
    )


def _iso_week_str(date_iso: str) -> str | None:
    """`YYYY-MM-DD` → `YYYY-Www`. Used to bucket items into ISO weeks for
    the trends sparkline. Returns None on parse failure (item is then
    silently skipped from the cohort)."""
    try:
        y, m, d = (int(x) for x in date_iso[:10].split("-"))
    except Exception:
        return None
    try:
        iso = date(y, m, d).isocalendar()
    except Exception:
        return None
    return f"{iso[0]:04d}-W{iso[1]:02d}"


def _item_matches_cohort(footer: dict[str, Any], cohort: dict[str, Any]) -> bool:
    """Returns True when a parsed footer dict matches the cohort spec.
    Cohort match modes: `any` — at least one of the listed tags / sectors /
    regions appears in the footer. `all` — every listed tag must be in the
    footer's tags (sectors / regions ignored)."""
    tags = set(footer.get("tags") or [])
    sectors = set(footer.get("sectors") or [])
    regions = set(footer.get("regions") or [])
    want_tags = set(cohort.get("tags") or [])
    want_sectors = set(cohort.get("sectors") or [])
    want_regions = set(cohort.get("regions") or [])
    if cohort.get("match") == "all":
        return bool(want_tags and want_tags.issubset(tags))
    # `any` (default)
    return bool(
        (want_tags and tags & want_tags)
        or (want_sectors and sectors & want_sectors)
        or (want_regions and regions & want_regions)
    )


def fetch_github_metadata(repo: str, *, timeout: float = 6.0) -> dict[str, Any]:
    """Best-effort fetch of `https://api.github.com/repos/<repo>`
    so the topbar can render a live star count. Returns `{url, stars,
    full_name}` on success; empty dict on any failure (network down, rate
    limited, parse error, blocked address). The build never fails on this —
    the topbar gracefully degrades to icon-only when stars are absent."""
    if not repo or "/" not in repo:
        return {}
    api = f"https://api.github.com/repos/{repo}"
    try:
        import urllib.request, urllib.error
        req = urllib.request.Request(
            api,
            headers={
                "User-Agent": f"{SITE_NAME} site build (github.com/{repo})",
                "Accept": "application/vnd.github+json",
            },
            method="GET",
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status != 200:
                return {}
            data = json.loads(resp.read(64 * 1024).decode("utf-8", errors="replace"))
            return {
                "url": data.get("html_url") or f"https://github.com/{repo}",
                "stars": int(data.get("stargazers_count") or 0),
                "full_name": data.get("full_name") or repo,
            }
    except Exception:
        return {}


def render_feeds_page(*, site_url: str, cachebust: str,
                       prefix: str, canonical: str) -> str:
    """Single discovery page for all 11 RSS feeds (3 main +
    8 sector slices). The topbar/footer link to this page; the brief-list
    page no longer carries chip-style per-feed links. `<head>` rel=alternate
    autodiscovery for the three main feeds is unchanged."""
    main_feeds: list[tuple[str, str, str]] = [
        ("feed.xml", "Daily — one item per day page, last 30",
         "One item per archived day. Description carries the day's TL;DR bullets; <code>&lt;content:encoded&gt;</code> carries the full day-page HTML. Categories carry the day's CVEs."),
        ("feed-weekly.xml", "Weekly — every weekly summary, last 30",
         "One item per weekly page. Same shape as daily."),
        ("feed-items.xml", "Per entry — every published finding, last 50",
         "One item per pipeline entry. <code>&lt;pubDate&gt;</code> is the entry's <code>discovered_at</code> — true discovery latency. Categories carry tags + regions + CVE status + CVE ids."),
    ]
    sector_feeds: list[tuple[str, str, str]] = [
        (fname, f"Sector — {title}", description)
        for fname, _accept_sectors, _accept_tags, title, description
        in SECTOR_FEED_SLICES
    ]

    def _row(fname: str, title: str, description: str) -> str:
        return (
            '<li class="feeds-row">'
            f'<div class="feeds-row__head">'
            f'<a class="feeds-row__title" href="{prefix}{fname}">{_escape(title)}</a>'
            f'<a class="feeds-row__url mono" href="{prefix}{fname}">/{fname}</a>'
            f'</div>'
            f'<p class="feeds-row__desc">{description}</p>'
            '</li>'
        )

    body = f"""
<header>
  <h1>RSS feeds</h1>
  <p class="subtitle">Eleven feeds in total. The three main feeds carry every day page, weekly page and entry; the eight sector slices filter the per-entry feed to the audience you care about. <code>&lt;pubDate&gt;</code> derives from each entry's <code>discovered_at</code> — the moment the pipeline verified the finding, not a publish schedule. <code>&lt;content:encoded&gt;</code> carries full HTML; categories carry tags / regions / CVE / status. No UTM parameters, no per-source variants — every link is plain canonical.</p>
</header>

<section style="margin-top:1.4rem">
  <h2 class="section-head">Main feeds</h2>
  <ul class="feeds-list">{''.join(_row(f, t, d) for f, t, d in main_feeds)}</ul>
</section>

<section style="margin-top:1.6rem">
  <h2 class="section-head">Sector slices</h2>
  <p class="muted" style="margin:0 0 0.6rem">Per-sector filtered slices of <a href="{prefix}feed-items.xml" class="mono">feed-items.xml</a>, matched on each entry's sectors / tags. Subscribe to the slice you care about instead of parsing every entry.</p>
  <ul class="feeds-list">{''.join(_row(f, t, d) for f, t, d in sector_feeds)}</ul>
</section>

<section style="margin-top:1.6rem">
  <h2 class="section-head">Autodiscovery</h2>
  <p>Every page on this site advertises the three main feeds via <code>&lt;link rel="alternate" type="application/rss+xml"&gt;</code> in the document head, so any feed reader pointed at the homepage finds them automatically. The eight sector slices are accessible through this page.</p>
</section>
"""
    return base_template(
        title=f"RSS feeds — {SITE_NAME}",
        description=FEEDS_PAGE_DESCRIPTION,
        body=body,
        canonical=canonical, site_url=site_url, cachebust=cachebust,
        home_relative_prefix=prefix,
    )



# === ACTOR-TIMELINE STRIP =================================

def _actor_timeline_strip(entity: dict[str, Any]) -> str:
    """Horizontal timeline strip for actor / campaign /
    incident / tool entity pages. Marker dot per appearance between the
    first and last coverage dates. Hover tooltip names the brief. Renders
    above the existing Story timeline; falls back to empty string for
    entity types where the strip would add no signal (CVE, vulnerability-
    trend — those use a different sparkline shape already)."""
    etype = (entity.get("type") or "").lower()
    if etype not in ("actor", "campaign", "incident", "tool", "annual-report"):
        return ""
    apps = sorted(entity.get("appearances", []) or [],
                  key=lambda a: a.get("date") or "")
    if len(apps) < 2:
        return ""
    first_iso = apps[0].get("date") or ""
    last_iso = apps[-1].get("date") or ""
    try:
        y0, m0, d0 = (int(x) for x in first_iso[:10].split("-"))
        y1, m1, d1 = (int(x) for x in last_iso[:10].split("-"))
        first = date(y0, m0, d0)
        last = date(y1, m1, d1)
    except Exception:
        return ""
    span_days = max((last - first).days, 1)
    dots: list[str] = []
    for a in apps:
        d_iso = a.get("date") or ""
        try:
            y, m, d = (int(x) for x in d_iso[:10].split("-"))
            here = date(y, m, d)
        except Exception:
            continue
        offset_pct = max(0.0, min(100.0, (here - first).days / span_days * 100.0))
        bp = a.get("brief_path") or ""
        title = (a.get("delta_summary") or "").strip()
        title_full = f"{d_iso}" + (f" — {title}" if title else "")
        dots.append(
            f'<span class="actor-timeline__dot" style="left:{offset_pct:.2f}%" title="{_escape(title_full)}"></span>'
        )
    return (
        '<section class="actor-timeline" aria-label="Coverage timeline">'
        '<div class="actor-timeline__strip">'
        '<div class="actor-timeline__line"></div>'
        + "".join(dots)
        + '</div>'
        '<div class="actor-timeline__ends">'
        f'<span class="mono">{_escape(first_iso)}</span>'
        f'<span class="mono muted">{len(apps)} appearance{"s" if len(apps) != 1 else ""}</span>'
        f'<span class="mono">{_escape(last_iso)}</span>'
        '</div>'
        '</section>'
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
        # Absolute URLs pass through untouched — the rewrite only applies
        # to repo-relative paths.
        if path.startswith(("http://", "https://", "mailto:", "tel:")):
            return path
        # Drop a leading `./` if the author wrote one.
        p = path[2:] if path.startswith("./") else path
        # Strip optional fragment / query so we can route by extension.
        frag = ""
        if "#" in p:
            p, frag = p.split("#", 1)
            frag = "#" + frag
        # entries/<date>/<slug>.md → the entry permalink
        m = re.match(r"^entries/(\d{4}-\d{2}-\d{2})/([a-z0-9-]+)\.md$", p)
        if m:
            return prefix + f"entries/{m.group(1)}/{m.group(2)}/" + frag
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
        # Legacy day-brief doc links → the day-page URL (same URL shape).
        m = re.match(r"^briefs/(\d{4}-\d{2}-\d{2})(?:\.md|/)?$", p)
        if m:
            return prefix + f"briefs/{m.group(1)}/" + frag
        # Legacy weekly doc links → the /weekly/ page.
        m = re.match(r"^briefs/weekly/(\d{4}-W\d{2})(?:\.md|/)?$", p)
        if m:
            return prefix + f"weekly/{m.group(1)}/" + frag
        if p == "briefs/" or p == "briefs":
            return prefix + "briefs/" + frag
        if p in ("entries/", "entries"):
            return prefix + "briefs/" + frag
        if p in ("runs/", "runs"):
            return prefix + "ops/" + frag
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


# === TRENDS PAGE (v3 — counts ENTRIES per ISO week) ====================


def render_trends_page(entries: list[dict[str, Any]], *,
                        site_url: str, cachebust: str,
                        prefix: str, canonical: str) -> str:
    """/trends/ — the cohort sparkline dashboard, bucketing ENTRIES by
    the ISO week of discovered_at. Cohorts match on the entry's own
    tags / sectors / regions frontmatter (no footer parsing)."""
    ops = operational_entries(entries)
    if not ops:
        body = (
            "<h1>Trends</h1>"
            '<p class="muted">No entries yet — trend dashboard is empty.</p>'
        )
        return base_template(
            title=f"Trends — {SITE_NAME}",
            description="Weekly trend dashboard across all published entries.",
            body=body,
            canonical=canonical, site_url=site_url, cachebust=cachebust,
            home_relative_prefix=prefix,
        )

    week_buckets: dict[str, dict[str, int]] = {c["key"]: {} for c in TREND_COHORTS}
    week_set: set[str] = set()
    for e in ops:
        week = iso_week_of_entry(e) or "unknown"
        week_set.add(week)
        for cohort in TREND_COHORTS:
            if _item_matches_cohort(e, cohort):
                bucket = week_buckets[cohort["key"]]
                bucket[week] = bucket.get(week, 0) + 1

    weeks_sorted = sorted(week_set)[-16:]
    if not weeks_sorted:
        body = '<h1>Trends</h1><p class="muted">No weekly buckets yet.</p>'
        return base_template(
            title=f"Trends — {SITE_NAME}",
            description="Weekly trend dashboard across all published entries.",
            body=body, canonical=canonical, site_url=site_url, cachebust=cachebust,
            home_relative_prefix=prefix,
        )

    cards: list[str] = []
    for cohort in TREND_COHORTS:
        bucket = week_buckets[cohort["key"]]
        values = [float(bucket.get(w, 0)) for w in weeks_sorted]
        total_recent = int(sum(values))
        last_week_count = int(values[-1]) if values else 0
        delta = ""
        if len(values) >= 2:
            prev = values[-2]
            now = values[-1]
            if prev == 0 and now == 0:
                delta = "no change"
            elif prev == 0 and now > 0:
                delta = "new this week (was 0)"
            else:
                pct = (now - prev) / prev * 100 if prev else 0
                arrow = "▲" if now > prev else ("▼" if now < prev else "→")
                delta = f"{arrow} {pct:+.0f}% vs prior week"
        spark_html = _ops_svg_sparkline(
            values,
            label=f"{cohort['title']} (last {len(weeks_sorted)} weeks)",
            width=240, height=44,
        )
        cards.append(
            '<div class="trends-card">'
            f'<p class="trends-card__title">{_escape(cohort["title"])}</p>'
            f'<p class="trends-card__value">{last_week_count}</p>'
            f'<p class="trends-card__sub">{_escape(delta)} · {total_recent} over last {len(weeks_sorted)} wk</p>'
            f"{spark_html}"
            "</div>"
        )

    weeks_label = f"{weeks_sorted[0]} → {weeks_sorted[-1]}"
    body = f"""
<header>
  <h1>Trends</h1>
  <p class="subtitle muted">Weekly counts of published entries by threat class, across {len(ops)} operational entries ({weeks_label}). Pure post-hoc analytics from entry frontmatter.</p>
</header>
<section>
  <div class="trends-grid">{''.join(cards)}</div>
</section>
<section style="margin-top:1.5rem">
  <h2 class="section-head">How to read this</h2>
  <p>Each tile counts entries whose frontmatter carries the relevant taxonomy values. Tiles aggregate over the ISO week of the entry's <code>discovered_at</code>. The "vs prior week" delta is week-over-week.</p>
  {_trends_cohort_note(prefix)}
</section>
"""
    return base_template(
        title=f"Trends — {SITE_NAME}",
        description=TRENDS_PAGE_DESCRIPTION,
        body=body,
        canonical=canonical, site_url=site_url, cachebust=cachebust,
        home_relative_prefix=prefix,
    )


# === OPS DASHBOARD =====================================================
#
# The Ops page renders directly from runs/** (content_model.collect_runs)
# and sources/sources.json.
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
                       stroke: str = "var(--accent)", fill: str = f"rgba({CHART_ACCENT_RGB},0.18)",
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
            colour = f"rgba({CHART_ACCENT_RGB},{alpha:.2f})" if v > 0 else "var(--bg-elev-2)"
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


_MODEL_PALETTE: list[str] = BRANDING["charts"]["model_palette"] or [
    "#e85d75", "#79c0ff", "#56d364", "#ffd866", "#d2a8ff",
    "#ff9b6b", "#56b3d3", "#bd9bff", "#9bdc4d",
]


def _ops_canonical_model(name: Any) -> str:
    """Collapse a self-reported model string to a canonical family+version tag
    for the Ops dashboard. Self-identification lives in the agents (the prompts
    say nothing about this normalisation) — here we just fold the harmless
    variants together so the "Models in use" view is legible:

        "Claude Opus 4.8"                        → "Claude Opus 4.8"
        "Anthropic Claude Opus 4.8"              → "Claude Opus 4.8"
        "Claude Opus 4.8 (1M context)"           → "Claude Opus 4.8"
        "Anthropic Claude Opus 4.8 (1M context)" → "Claude Opus 4.8"
        "Claude Fable 5"                         → "Claude Fable 5"   (future-proof)

    Anything that doesn't self-identify as `Claude <Family> <Version>` —
    "unknown", "manual full-source audit session", "Anthropic Claude (specific
    model not determined)", "" — folds to "unknown". No model list is hardcoded,
    so a new family/version works without a code change."""
    if not isinstance(name, str):
        return "unknown"
    s = re.sub(r"^\s*anthropic\s+", "", name.strip(), flags=re.I)  # drop vendor prefix
    s = re.sub(r"\s*\([^)]*\)\s*", " ", s).strip()                 # drop "(1M context)" etc.
    m = re.match(r"(?i)^claude\s+([a-z]+)\s+(\d+(?:\.\d+)?)\b", s)
    if not m:
        return "unknown"
    return f"Claude {m.group(1).capitalize()} {m.group(2)}"


def _ops_color_for_model(name: str, assigned: dict[str, str]) -> str:
    """Stable palette assignment; 'unknown' always renders muted. The name is
    canonicalised first so every variant of a model shares one colour."""
    key = _ops_canonical_model(name)
    if not key or key.lower() in ("unknown", "—"):
        return "var(--text-muted)"
    if key in assigned:
        return assigned[key]
    colour = _MODEL_PALETTE[len(assigned) % len(_MODEL_PALETTE)]
    assigned[key] = colour
    return colour


def _ops_pill(text: str, *, kind: str = "neutral") -> str:
    return f'<span class="ops-pill ops-pill--{kind}">{_escape(text)}</span>'


def _ops_count_sources(value: Any) -> int:
    # Sub-agent telemetry records sources_attempted / sources_used as either a
    # list of source IDs (legacy) or an integer count. Accept both.
    if isinstance(value, bool):
        return 0
    if isinstance(value, int):
        return max(0, value)
    if isinstance(value, list):
        return len(value)
    return 0


def _verification_clean_publish(run: dict[str, Any]) -> bool:
    """True when a run published with the verifier's final verdict CLEAN.

    The canonical signal is ``verification_residual_count == 0``: per the
    run-log schema it is ``0`` on a clean publish and ``> 0`` only when the
    iteration cap was hit with NEEDS_FIXES still outstanding. This is
    independent of how many iterations it took — a brief that reached CLEAN
    after remediation published just as clean as one that passed on the first
    pass. The earlier definition required ``verification_iterations == 1``,
    which conflated "clean on the first try" with "published clean" and
    undercounted the rate badly (it counted only the single-pass runs and
    dropped every brief that reached CLEAN after one or more remediation
    rounds — the bulk of all runs).

    Returns ``False`` for runs where verification never ran / was not recorded
    (``verification_iterations is None``) so they are excluded from the rate
    rather than silently counted as clean.
    """
    if run.get("verification_iterations") is None:
        return False
    return (run.get("verification_residual_count") or 0) == 0


def render_ops_page(
    runs_input: list[dict[str, Any]] | None,
    sources: list[dict[str, Any]] | None,
    *,
    prefix: str,
    site_url: str,
    cachebust: str,
    canonical: str,
    source_health: dict[str, Any] | None = None,
    day_pages: set[str] | None = None,
    entries_by_run: dict[str, list[dict[str, Any]]] | None = None,
) -> str:
    """Operations dashboard.

    Reads run records from `runs/**` (via content_model.collect_runs) and
    `sources/sources.json`. Renders KPI tiles, charts (inline SVG, no JS),
    per-run tables, sub-agent telemetry, verification breakdown. Every
    visualisation degrades gracefully when a (migrated, sparse) record is
    missing optional blocks — em-dash cells, never a crash.
    """
    all_runs = list(runs_input or [])
    day_pages = day_pages or set()
    entries_by_run = entries_by_run or {}
    # Dashboard structure:
    #   - Health KPIs + trend charts are GLOBAL — computed over every recorded
    #     run, not a 30-run slice (the operator asked for global stats).
    #   - The run-log table renders all runs (paginated client-side).
    #   - The run-detail selector is bounded to the most-recent 30 (each panel
    #     is heavy; older runs remain inspectable via the run-log table).
    #   - The fetch-density heatmap stays a compact recent window.
    all_desc = list(reversed(all_runs))          # newest first, ALL runs
    runs_desc = all_desc                          # KPIs + charts: global
    runs_asc = list(reversed(runs_desc))          # chronological, all runs
    picker_runs = all_desc[:30]                   # run-detail selector (bounded)
    heatmap_runs = all_desc[:16]                  # fetch-density (compact)

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
    items_published = [r.get("entries_published") or 0 for r in runs_desc if r.get("entries_published") is not None]
    avg_items = sum(items_published) / len(items_published) if items_published else 0
    total_items = sum(items_published)
    total_updates = sum(r.get("entries_updated") or 0 for r in runs_desc)

    # Verification cleanliness: a brief "published clean" whenever the final
    # verifier verdict was CLEAN (residual == 0), whether that took one pass
    # or several remediation rounds. See _verification_clean_publish.
    clean_runs = sum(1 for r in runs_desc if _verification_clean_publish(r))
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

    # Distinct models across main agent + sub-agents + verifiers — counted on
    # the canonical tag, excluding the "unknown" bucket (not a real model).
    distinct_models: set[str] = set()
    for r in runs_desc:
        for cand in [r.get("model")]:
            c = _ops_canonical_model(cand)
            if c != "unknown":
                distinct_models.add(c)
        for a in (r.get("sub_agents") or {}).values():
            if not isinstance(a, dict):
                continue
            c = _ops_canonical_model(a.get("model"))
            if c != "unknown":
                distinct_models.add(c)
        for it in ((r.get("verification") or {}).get("iterations") or []):
            if isinstance(it, dict):
                c = _ops_canonical_model(it.get("model"))
                if c != "unknown":
                    distinct_models.add(c)

    # ----- Sparkline series (chronological order) ---------------------------
    duration_series = [r.get("duration_seconds") or 0 for r in runs_asc]
    items_series = [r.get("entries_published") or 0 for r in runs_asc]
    failures_series = [len(r.get("fetch_failures") or []) for r in runs_asc]

    # Verification stacks: clean outcome (green) + remediation rounds (yellow)
    # + residuals (red). Green marks a clean publish regardless of how many
    # iterations it took; yellow shows the remediation rounds it took to get
    # there, so a brief that reached CLEAN after several iterations still
    # reads as ultimately-clean rather than as a string of yellow with no
    # green (which contradicted the clean-rate KPI).
    verification_stacks: list[list[tuple[float, str]]] = []
    for r in runs_asc:
        clean = 1 if _verification_clean_publish(r) else 0
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
        # Canonicalise so all variants of a model fold into one slice; the
        # "unknown" bucket is kept (it surfaces identification gaps).
        canon = _ops_canonical_model(name)
        bucket = model_role_counts.setdefault(canon, {"main": 0, "research": 0, "verify": 0})
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
    sa_keys = ["S1", "S2", "S3", "S4", "S5", "W1", "W2", "W3"]
    heatmap_rows: list[tuple[str, list[tuple[float, str]]]] = []
    heatmap_asc = list(reversed(heatmap_runs))  # compact recent window, chronological
    for k in sa_keys:
        cells: list[tuple[float, str]] = []
        present = False
        for r in heatmap_asc:
            a = (r.get("sub_agents") or {}).get(k)
            if not isinstance(a, dict):
                cells.append((0.0, f"{r.get('date','?')} {k}: not in this run"))
                continue
            present = True
            if a.get("returned") is False:
                cells.append((0.0, f"{r.get('date','?')} {k}: stalled"))
                continue
            attempted = _ops_count_sources(a.get("sources_attempted"))
            used = _ops_count_sources(a.get("sources_used"))
            ratio = (used / attempted) if attempted else 0.0
            cells.append((ratio, f"{r.get('date','?')} {k}: {used}/{attempted} sources used, {a.get('items_returned', 0)} items"))
        if present:
            heatmap_rows.append((k, cells))
    heatmap_html = _ops_svg_heatmap(heatmap_rows, cell=14, gap=2, label="Sub-agent fetch density (used/attempted)") \
        if heatmap_rows else '<p class="muted">No sub-agent allocation recorded yet.</p>'

    # ----- Run-detail picker -----------------------------------------------
    # The detail panel is selectable across every run in the window, not just
    # the latest. Each run's panel is rendered into the page; a <select>
    # toggles which one is visible (app.js wireOpsRunPicker — CSP-safe, no
    # inline handlers). The latest run (first of runs_desc) is the default.
    # All but the selected panel carry `hidden`, so the page is fully usable
    # with JS disabled (the latest panel shows; the rest are reachable once
    # JS wires the select).
    if picker_runs:
        run_options: list[str] = []
        run_panels: list[str] = []
        for i, r in enumerate(picker_runs):
            key = r.get("run_id") or f"idx-{i}"
            label = _ops_run_picker_label(r)
            selected = " selected" if i == 0 else ""
            run_options.append(
                f'<option value="{_escape(key)}"{selected}>{_escape(label)}</option>'
            )
            run_panels.append(
                f'<div class="ops-run-panel" data-run-panel="{_escape(key)}"'
                f'{"" if i == 0 else " hidden"}>'
                + _ops_render_latest_run_panel(
                    r, palette, prefix=prefix,
                    day_pages=day_pages,
                    run_entries=entries_by_run.get(str(r.get("run_id") or ""), []),
                )
                + '</div>'
            )
        run_detail_html = (
            '<div class="ops-run-picker">'
            '<label class="ops-run-picker__label" for="ops-run-select">Showing run</label>'
            f'<select id="ops-run-select" class="ops-run-picker__select" '
            f'aria-label="Select a run to inspect">{"".join(run_options)}</select>'
            '</div>'
            + "".join(run_panels)
        )
    else:
        run_detail_html = '<p class="muted">No runs recorded yet.</p>'

    # The GLOBAL "Verification iterations" table was removed. Per-
    # iteration verdicts now live ONLY in each run's detail panel
    # (_ops_render_verification_iterations, called from the run-detail
    # selector), so the same data is not presented twice.

    # ----- Run-log table (ALL runs, paginated client-side) -----------------
    runs_table_html = _ops_render_runs_table(all_desc, palette, prefix=prefix,
                                             day_pages=day_pages)

    # ----- Stale-active-sources MOVED TO /sources/ ----------------
    # The "Stale active sources" panel that previously lived here is now
    # rendered exclusively on /sources/ — alongside the source's
    # reliability, status, category tags, and lifecycle counters
    # (consecutive_quiet_periods, consecutive_fetch_failures). The Ops
    # dashboard no longer surfaces it at all (follow-up: the
    # placeholder block was confusing — the operator just wants it gone).

    # ----- KPI tiles --------------------------------------------------------
    last_run_label = _escape(last_run_date or "—")
    if days_since_last >= 0:
        last_run_label += f' <span class="muted ops-kpi__delta">({days_since_last}d ago)</span>'
    clean_rate_str = f"{clean_rate:.0f}%" if clean_rate is not None else "—"
    clean_rate_sub = f"{clean_runs}/{rated_runs} clean publish" if rated_runs else "no telemetry yet"
    if clean_rate is None:
        clean_rate_kind = "neutral"
    elif clean_rate >= 80:
        clean_rate_kind = "ok"
    elif clean_rate >= 50:
        clean_rate_kind = "warn"
    else:
        clean_rate_kind = "crit"
    distinct_models_str = str(len(distinct_models)) if distinct_models else "—"
    distinct_models_sub = ", ".join(sorted(distinct_models)[:3]) if distinct_models else "no model recorded"

    # Primary row — the operator's first look: freshness, verification quality,
    # sub-agent reliability. Each carries a status colour. Volume / cadence /
    # runtime KPIs sit in the smaller secondary grid below.
    primary_kpis = (
        '<div class="ops-kpi-row">'
        + _ops_kpi_tile("Last run", last_run_label,
                        sub=f"{total_failures} fetch failure{'s' if total_failures != 1 else ''} in window",
                        kind=("warn" if days_since_last > 1 else "ok"),
                        primary=True)
        + _ops_kpi_tile("Verification clean-rate", clean_rate_str, sub=clean_rate_sub,
                        kind=clean_rate_kind, primary=True,
                        chart=_ops_svg_stacked_bars(verification_stacks, width=160, height=30,
                                                      label="Verification verdicts"))
        + _ops_kpi_tile("Sub-agent stalls", str(stalled_subagents),
                        sub=f"out of {sub_agent_returns} sub-agent returns in window",
                        kind=("crit" if stalled_subagents > 0 else "ok"), primary=True)
        + _ops_kpi_tile("Fetch failures", str(total_failures),
                        sub=f"coverage gaps across {len(runs_desc)} runs",
                        kind=("warn" if total_failures > 0 else "ok"), primary=True,
                        chart=_ops_svg_bars(failures_series, width=160, height=30,
                                              color="var(--warn)",
                                              label="Fetch failures per run (chronological)"))
        + '</div>'
    )

    secondary_kpis = (
        '<div class="ops-kpi-grid">'
        + _ops_kpi_tile("Total runs (window)", str(min(total_runs, len(runs_desc))),
                        sub=f"{len(daily_runs)} intel · {len(weekly_runs)} weekly",
                        chart=_ops_svg_bars([1] * len(runs_desc) if runs_desc else [],
                                              width=140, height=28,
                                              color="var(--accent)", track="var(--bg)",
                                              label="Run cadence"))
        + _ops_kpi_tile("Avg duration",
                        _ops_format_duration(avg_duration),
                        sub=f"min {_ops_format_duration(min(durations) if durations else 0)} · "
                            f"max {_ops_format_duration(max(durations) if durations else 0)}",
                        chart=_ops_svg_sparkline(duration_series, width=140, height=28,
                                                  stroke="var(--info)", fill=f"rgba({CHART_INFO_RGB},0.2)",
                                                  label="Run duration over time"))
        + _ops_kpi_tile("Entries published",
                        str(total_items),
                        sub=f"avg {avg_items:.1f} per run · {total_updates} update entries",
                        chart=_ops_svg_bars(items_series, width=140, height=28,
                                              color="var(--ok)",
                                              label="Entries per run"))
        + '</div>'
    )

    run_count_label = f"{len(all_desc)} run{'' if len(all_desc) == 1 else 's'}"
    source_health_html = _ops_render_source_health(source_health, prefix=prefix)
    picker_count_label = f"{len(picker_runs)} most-recent run{'' if len(picker_runs) == 1 else 's'}"
    body = f"""
<h1>Operations</h1>
<p class="subtitle">Live telemetry from the per-run records under <code>runs/</code> (sub-agent allocation, model split, verification verdicts, fetch failures, source-list edits, entries published, wall-clock duration) and <code>sources/sources.json</code> + <code>state/source_health.json</code> (last-successful-fetch timestamps + independent accessibility probe). Stats below are global across all {run_count_label}.</p>

<nav class="ops-nav" aria-label="Dashboard sections">
  <span class="ops-nav__label">Jump to</span>
  <a href="#health">Health</a>
  <a href="#runlog">Run log</a>
  <a href="#latest">Run detail</a>
</nav>

<section class="ops-cluster" id="health">
  <h2 class="ops-cluster__head">Health</h2>
  <p class="ops-cluster__intro">Global overview across all {run_count_label}. The top row is the operator's first look — run freshness, verification quality, and sub-agent reliability; the secondary tiles cover cadence, volume, and runtime. Below: source-accessibility action items, then a compact model split and sub-agent fetch summary for the whole window.</p>
  {primary_kpis}
  {secondary_kpis}

  <div class="ops-subsection">
    <h3 class="ops-subhead">Source accessibility — needs attention</h3>
    {source_health_html}
  </div>

  <div class="ops-subsection">
    <h3 class="ops-subhead">Models in use <span class="muted" style="font-weight:400">· {distinct_models_str} distinct</span></h3>
    <p class="ops-subtitle"><strong>{distinct_models_str} distinct Claude model(s)</strong> signed work across all runs ({_escape(distinct_models_sub)}) — main agent, research sub-agents, verifiers. Variants of a model (vendor prefix, 1M-context suffix) fold into one tag; agents that did not self-identify fold into <code>unknown</code>. The split surfaces runtime-config changes and any sub-agent that forgot to self-identify.</p>
    <div class="ops-models">
      <div class="ops-models__chart">{donut_html}</div>
      <div class="ops-models__table">{models_table_html}</div>
    </div>
  </div>

  <div class="ops-subsection">
    <h3 class="ops-subhead">Sub-agent fetch density <span class="muted" style="font-weight:400">· last {len(heatmap_runs)} runs</span></h3>
    <p class="ops-subtitle">Each cell is one run × one sub-agent (most recent {len(heatmap_runs)}). Intensity = used / attempted source ratio. Empty rows = sub-agent not in this routine (S1–S4 daily, W1–W2 weekly). White cells = stalled or absent.</p>
    <div class="ops-heatmap-wrap">{heatmap_html}</div>
  </div>
</section>

<section class="ops-cluster" id="runlog">
  <h2 class="ops-cluster__head">Run log</h2>
  <p class="ops-cluster__intro">Every recorded run, newest first — duration, entries published / updated, fetch failures, source-list edits (<strong>Src Δ</strong>), and verification verdict. Shows 10 per page by default; use the selector to expand to 35 / 50 / 100 and the pager to step through the rest.</p>
  {runs_table_html}
</section>

<section class="ops-cluster" id="latest">
  <h2 class="ops-cluster__head">Run detail</h2>
  <p class="ops-cluster__intro">Everything about a single run in one place — pick any of the {picker_count_label} from the selector. Each panel carries the sub-agent allocation + telemetry, <strong>Verification iterations</strong>, <strong>Sources changed (this run)</strong>, <strong>Coverage gaps (this run)</strong> (sources <em>that run's</em> brief needed but couldn't fetch), and <strong>Bridge invocations (this run)</strong>. Global source-accessibility action items live in the <a href="#health">Health</a> section above — distinct from a single run's coverage gaps.</p>
  {run_detail_html}
</section>

<p class="muted ops-footnote">
  See <a href="{prefix}about/docs/pipeline/">the pipeline data model</a> for the run-record contract. Per-agent self-identification is documented in <a href="{prefix}about/prompts/cti-run/">prompts/cti-run.md</a> § Self-identification.
</p>
"""
    return base_template(
        title=f"Operations dashboard — {SITE_NAME}",
        description="Live agent telemetry: run cadence, durations, model split, sub-agent allocation, verification verdicts, fetch failures, source-rotation health.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


_SOURCES_CHANGE_BADGE = {
    "promoted": "ok", "recovered": "ok", "added": "ok",
    "demoted": "crit",
    "recategorised": "neutral", "url": "neutral",
    "reliability": "warn", "fetch_method": "warn",
}


def _ops_pager_wrap(inner_html: str, *, pagesize: int = 10, size_select: bool = False) -> str:
    """Wrap a table (whose <tbody> carries `data-pager-rows`) in a client-side
    pager container (app.js `wireOpsPagers`). The control bar is hidden until JS
    reveals it, so the no-JS fallback is the full, unpaginated table. When
    `size_select` is set, a 10/35/50/100 rows-per-page <select> is offered."""
    size_html = ""
    if size_select:
        opts = "".join(
            f'<option value="{s}"{" selected" if s == pagesize else ""}>{s}</option>'
            for s in (10, 35, 50, 100)
        )
        size_html = ('<label class="ops-pager__size">Rows per page '
                     f'<select data-pager-size aria-label="Rows per page">{opts}</select></label>')
    bar = (
        '<div class="ops-pager__bar" data-pager-bar hidden>'
        f'{size_html}'
        '<div class="ops-pager__nav">'
        '<button type="button" class="ops-pager__btn" data-pager-prev>‹ Prev</button>'
        '<span class="ops-pager__status" data-pager-status></span>'
        '<button type="button" class="ops-pager__btn" data-pager-next>Next ›</button>'
        '</div></div>'
    )
    return f'<div class="ops-pager" data-ops-pager data-pagesize="{pagesize}">{bar}{inner_html}</div>'


def _ops_render_run_sources_changed(run: dict[str, Any], *, prefix: str) -> str:
    """the `sources_changed[]` edits a SINGLE run made to
    sources/sources.json, rendered as a table of what moved (promotions,
    demotions, new candidates, and fetch-method / category / reliability / url
    corrections). Lives inside the per-run detail panel so the run-detail
    selector shows each run's source-list edits, not just the latest's."""
    sc = [c for c in (run.get("sources_changed") or []) if isinstance(c, dict)]
    if not sc:
        body = '<p class="muted">No source-list edits recorded for this run.</p>'
    else:
        counts = Counter(c.get("change") for c in sc)
        summary = " · ".join(f"{n} {k}" for k, n in counts.most_common())
        rows = "".join(
            f'<tr><td class="mono"><a href="{prefix}sources/{urllib.parse.quote(c.get("id", "?"), safe="")}/">{_escape(c.get("id", "?"))}</a></td>'
            f'<td><span class="ops-pill ops-pill--{_SOURCES_CHANGE_BADGE.get(c.get("change"), "neutral")}">{_escape(c.get("change", "?"))}</span></td>'
            f'<td class="mono muted">{_escape(str(c.get("from") or "—"))} → {_escape(str(c.get("to") or "—"))}</td>'
            f'<td class="muted">{_escape(c.get("reason", ""))}</td></tr>'
            for c in sc
        )
        table = (
            '<div class="data-wrap"><table class="data">'
            '<thead><tr><th>Source</th><th>Change</th><th>From → To</th><th>Reason</th></tr></thead>'
            f'<tbody data-pager-rows>{rows}</tbody></table></div>'
        )
        body = (
            f'<p class="muted ops-latest__failures-help">{_escape(summary)}.</p>'
            + _ops_pager_wrap(table, pagesize=10, size_select=False)
        )
    return (
        '<div class="ops-latest__failures">'
        '<h3 class="ops-mini-head">Sources changed (this run)</h3>'
        '<p class="muted ops-latest__failures-help">Edits this run made to <code>sources/sources.json</code> — '
        'promotions, demotions, new candidates, and fetch-method / category / reliability / url corrections '
        '(the run record&#39;s <code>sources_changed[]</code>). Paginated; 10 per page.</p>'
        f'{body}</div>'
    )


_SOURCE_STATUS_KIND = {"active": "ok", "candidate": "neutral", "demoted": "crit"}


def _ops_render_source_health(source_health: dict[str, Any] | None, *, prefix: str = "") -> str:
    """surface ONLY the unsolved accessibility problems from
    `state/source_health.json` (written by tools/source_health.py, which probes
    EVERY source with the bridge's UA and exercises the api/bridge recipes).

    The panel floats only sources whose derived `action` is not `none` — i.e.
    sources that need a dedicated bridge fetcher (browser UA refused, not yet on
    the bridge) or need demotion (dead/erroring, or an already-implemented
    bridge recipe now failing). It deliberately does NOT list healthy sources,
    already-demoted sources, or sources already served by a working bridge —
    those are handled, not problems."""
    if not isinstance(source_health, dict) or not source_health:
        return (
            '<div class="empty"><p>No <code>state/source_health.json</code> snapshot yet.</p>'
            '<p class="muted">Written by <code>tools/source_health.py</code> (run at the end of every '
            'routine + a weekly GitHub Action) — a periodic accessibility probe of every source that '
            'also verifies the api/bridge recipes still work.</p></div>'
        )
    latest = source_health.get("latest") or {}
    fetched_at = source_health.get("last_updated", "?")
    total = len(latest)
    flagged = [r for r in latest.values()
               if isinstance(r, dict) and r.get("action") not in (None, "", "none")]
    intro = (
        f'<p class="ops-subtitle">Periodic probe of all <strong>{total}</strong> sources — snapshot '
        f'<span class="mono">{_escape(str(fetched_at))}</span>. Uses the bridge\'s browser UA and '
        f'exercises the <code>api</code>/<code>bridge</code> recipes, so "reachable here" means '
        f'"reachable via the configured fetch method". Only <strong>unsolved problems</strong> are '
        f'listed below — healthy sources, already-demoted sources, and sources already served by a '
        f'working bridge are omitted.</p>'
    )
    if not flagged:
        return (
            intro
            + '<p class="ops-pill ops-pill--ok" style="display:inline-block">✓ All '
            + f'{total} sources reachable via their configured fetch method — nothing needs a '
            + 'dedicated bridge or demotion.</p>'
        )

    def _group(rows_data: list[dict[str, Any]], heading: str, help_txt: str) -> str:
        if not rows_data:
            return ""
        rows = "".join(
            f'<tr>'
            f'<td class="mono"><a href="{prefix}sources/{urllib.parse.quote(r.get("id", "?"), safe="")}/">'
            f'{_escape(r.get("id", "?"))}</a></td>'
            f'<td><span class="ops-pill ops-pill--{_SOURCE_STATUS_KIND.get(r.get("status"), "neutral")}">'
            f'{_escape(r.get("status") or "?")}</span></td>'
            f'<td class="mono muted">{_escape(r.get("fetch_method") or "—")}</td>'
            f'<td class="mono muted">{_escape(r.get("class") or "?")}'
            f'{(" " + str(r.get("status_code"))) if r.get("status_code") else ""}</td>'
            f'<td class="muted">{_escape(r.get("action_reason") or "")}</td>'
            f'</tr>'
            for r in sorted(rows_data, key=lambda x: x.get("id", ""))
        )
        return (
            f'<h4 class="ops-mini-head" style="margin-top:1rem">{heading} '
            f'<span class="ops-pill ops-pill--crit">{len(rows_data)}</span></h4>'
            f'<p class="muted ops-latest__failures-help">{help_txt}</p>'
            '<div class="data-wrap"><table class="data">'
            '<thead><tr><th>Source</th><th>Status</th><th>Method</th><th>Probe</th><th>What to do</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>'
        )

    needs_bridge = [r for r in flagged if r.get("action") == "needs-bridge"]
    needs_demote = [r for r in flagged if r.get("action") == "needs-demote"]
    other = [r for r in flagged if r.get("action") not in ("needs-bridge", "needs-demote")]
    return (
        intro
        + _group(needs_bridge, "Needs a dedicated bridge fetcher (or demotion)",
                 "A browser-grade UA is refused on these, but they are not yet routed through "
                 "<code>tools/fetch_source.py</code>. Build a dedicated bridge recipe — or demote if "
                 "even the bridge can't reach them.")
        + _group(needs_demote, "Failing — fix the recipe or demote",
                 "Dead / erroring sources, or sources whose already-implemented "
                 "<code>api</code>/<code>bridge</code> recipe is now failing. Update the URL/recipe, or demote.")
        + _group(other, "Review", "Unexpected probe outcome — inspect.")
    )


def _ops_kpi_tile(label: str, value: str, *, sub: str = "", kind: str = "neutral",
                   chart: str = "", primary: bool = False) -> str:
    """One KPI tile. `value` may contain HTML (e.g. embedded muted span).

    `primary=True` marks a prominent tile for the Health cluster's top row
    (larger value, more padding via the `.ops-kpi--primary` modifier)."""
    sub_html = f'<div class="ops-kpi__sub">{_escape(sub)}</div>' if sub else ""
    chart_html = f'<div class="ops-kpi__chart">{chart}</div>' if chart else ""
    primary_cls = " ops-kpi--primary" if primary else ""
    return (
        f'<div class="ops-kpi ops-kpi--{kind}{primary_cls}">'
        f'<div class="ops-kpi__label">{_escape(label)}</div>'
        f'<div class="ops-kpi__value">{value}</div>'
        f'{sub_html}'
        f'{chart_html}'
        f'</div>'
    )


# error-class → CSS-modifier mapping for the rich fetch_failures table.
_FETCH_FAILURE_CLASS_KIND: dict[str, str] = {
    "transport-403": "warn",
    "transport-429": "warn",
    "transport-5xx": "crit",
    "transport-tls": "crit",
    "transport-dns": "crit",
    "transport-timeout": "warn",
    "spa-empty-body": "warn",
    "paywall": "warn",
    "robots-blocked": "warn",
    "geo-blocked": "warn",
    "rate-limited": "warn",
    "other": "neutral",
}


def _ops_render_fetch_failures(failures: list[dict[str, Any]], *, prefix: str) -> str:
    """render the (now-strict) fetch_failures shape as a "Coverage
    gaps" table. Each row is a source the brief needed but couldn't get
    via any recipe (bridge / corroborating alternate publisher), so the row's
    intrinsic meaning is "operator should look at this — content was
    missing." Earlier versions of this table doubled as a bridge-use log;
    those were split out into `bridge_uses[]` (rendered separately).

    Soft-signal handling: a record with `covered_anyway: true` survived
    in the data only because an older sub-agent prompt logged a recovered
    fetch here — the agent prompts tell sub-agents not to do this, but the table
    still tolerates such records and tags them yellow ("recovered — does
    not belong here") so the operator can quickly
    distinguish current-shape from drift.
    """
    if not failures:
        return (
            '<p class="muted">No coverage gaps in this run — every source '
            'the brief needed returned usable content via its documented '
            'recipe.</p>'
        )

    rows: list[str] = []
    for f in failures:
        if not isinstance(f, dict):
            rows.append('<tr><td colspan="5" class="muted">malformed entry (not a dict)</td></tr>')
            continue
        sid = f.get("id") or "?"
        is_legacy = "url_tried" not in f and "attempted_methods" not in f
        url_tried = f.get("url_tried") or ""
        fetch_method = f.get("fetch_method") or ""
        status_code = f.get("status_code", f.get("code", f.get("status", "")))
        error_class = f.get("error_class") or ("legacy-shape" if is_legacy else "other")
        error_message = f.get("error_message") or f.get("note") or ""
        attempted = f.get("attempted_methods") or []
        mitigation = f.get("mitigation_applied") or ""
        covered_anyway = f.get("covered_anyway")
        kind = _FETCH_FAILURE_CLASS_KIND.get(error_class, "warn" if is_legacy else "neutral")

        # yellow soft-signal flag when a recovered fetch is logged
        # here against the new (stricter) schema rule.
        soft_signal = (covered_anyway is True) and not is_legacy

        method_chain_html = ""
        if attempted:
            method_chain_html = " → ".join(
                f'<span class="ops-pill ops-pill--{("ok" if m.startswith("bridge:") else "warn")}">{_escape(m)}</span>'
                for m in attempted if isinstance(m, str)
            )
        elif fetch_method:
            method_chain_html = f'<span class="ops-pill ops-pill--neutral">{_escape(fetch_method)}</span>'
        else:
            method_chain_html = '<span class="muted mono">—</span>'

        url_html = (
            f'<a class="mono" href="{_escape(_safe_url(url_tried))}" target="_blank" rel="noopener noreferrer">{_escape(url_tried[:80])}</a>'
            if url_tried.startswith(("http://", "https://"))
            else f'<span class="mono muted">{_escape(url_tried[:80] or "—")}</span>'
        )
        mitigation_html = (
            f'<span class="mono">{_escape(mitigation[:160])}</span>'
            if mitigation else '<span class="muted">none</span>'
        )

        # Source cell — with the soft-signal badge when applicable.
        sid_extra = ""
        if is_legacy:
            sid_extra = '<div class="muted" style="font-size:0.72rem">legacy shape — needs detail</div>'
        elif soft_signal:
            sid_extra = (
                '<div class="muted" style="font-size:0.72rem;color:var(--warn)">'
                'covered via alternate — should NOT be in this list'
                '</div>'
            )

        row_class = ' class="ops-coverage-gaps__row--soft"' if soft_signal else ""
        rows.append(
            f'<tr{row_class}>'
            f'<td><a href="{prefix}sources/{urllib.parse.quote(sid, safe="")}/" class="mono"><strong>{_escape(sid)}</strong></a>'
            + sid_extra
            + '</td>'
            f'<td>{url_html}</td>'
            f'<td>{method_chain_html}</td>'
            f'<td>{_ops_pill(str(status_code) if status_code != "" else "—", kind=kind)}'
            + (f' <span class="muted mono">{_escape(error_class)}</span>' if error_class != "other" else '')
            + (f'<div class="muted" style="font-size:0.72rem;margin-top:0.15rem">{_escape(error_message[:160])}</div>' if error_message else '')
            + '</td>'
            f'<td>{mitigation_html}</td>'
            '</tr>'
        )
    return (
        '<div class="data-wrap"><table class="data ops-fetch-failures ops-coverage-gaps">'
        '<thead><tr>'
        '<th>Source (uncovered)</th><th>URL tried</th><th>Method chain</th>'
        '<th>Status / class</th><th>What the agent did instead</th>'
        '</tr></thead>'
        '<tbody>' + "".join(rows) + '</tbody></table></div>'
    )


def _ops_render_bridge_uses(uses: list[dict[str, Any]] | None) -> str:
    """render the optional bridge_uses[] telemetry as a compact
    counter strip. Each entry is `{id, method, outcome}` from a sub-agent's
    `## Bridge uses` section. Outcomes are grouped (ok / empty-feed /
    item-not-found / other) so the operator sees bridge effectiveness at
    a glance without the "is this a failure?" ambiguity that polluted the
    legacy fetch_failures table.
    """
    if not uses:
        return ""

    from collections import Counter
    by_outcome: Counter[str] = Counter()
    by_method: Counter[str] = Counter()
    for u in uses:
        if not isinstance(u, dict):
            continue
        by_outcome[u.get("outcome") or "unknown"] += 1
        m = u.get("method") or ""
        # Drop the source-id from bridge:url; group by subcommand only.
        by_method[m.split(":", 1)[0] + (":" + m.split(":", 1)[1].split(" ", 1)[0] if ":" in m else "")] += 1

    total = sum(by_outcome.values())
    if total == 0:
        return ""

    outcome_chips = []
    for outcome, label, kind in (
        ("ok",             "ok",             "ok"),
        ("empty-feed",     "empty feed",     "neutral"),
        ("item-not-found", "item not found", "warn"),
    ):
        n = by_outcome.get(outcome, 0)
        if n:
            outcome_chips.append(
                f'<span class="ops-pill ops-pill--{kind}"><span class="mono">{n}</span> {_escape(label)}</span>'
            )
    other = total - sum(by_outcome.get(k, 0) for k in ("ok", "empty-feed", "item-not-found"))
    if other:
        outcome_chips.append(
            f'<span class="ops-pill ops-pill--neutral"><span class="mono">{other}</span> other</span>'
        )

    method_lines = [
        f'<li><span class="mono">{_escape(method)}</span> <span class="muted">×{count}</span></li>'
        for method, count in by_method.most_common(8)
    ]

    return (
        '<div class="ops-bridge-uses">'
        '<h3 class="ops-mini-head">Bridge invocations (this run)</h3>'
        f'<p class="muted">{total} bridge call{"s" if total != 1 else ""} this run — '
        'these are <em>successful</em> bridge fetches (separate from "Coverage gaps" above).</p>'
        f'<div class="ops-bridge-uses__chips">{"".join(outcome_chips)}</div>'
        f'<ul class="ops-bridge-uses__methods">{"".join(method_lines)}</ul>'
        '</div>'
    )


_F_CODE_LABEL: dict[str, str] = {
    "F1": "broken-url", "F2": "generic-url", "F3": "claim-not-supported",
    "F4": "hallucinated-fact", "F5": "missing-citation",
    "F6": "strengthen-primary-source", "F7": "drop",
    "F8": "needs-more-research", "F9": "surface-contradiction",
    "F10": "missed-angle", "F11": "editorial-advisory",
    "F12": "single-source-flag-missing",
}


def _ops_render_verification_iterations(
    iters: list[Any], *,
    legacy_count: int | None,
    legacy_residual: int | None,
) -> tuple[str, str]:
    """return (chips_html, findings_html) instead of one combined
    string. The chips_html is the compact iteration timeline that fits in
    the 2-column "Verification" panel slot; the findings_html is a stack
    of per-iteration finding tables intended to be rendered in a
    full-width block beneath the latest-run card, like the Coverage Gaps
    table already gets full-width treatment.

    Previously only the FINAL iteration's findings rendered (the
    cap-breach signal). The dashboard renders every iteration's `findings[]`
    that is non-empty so the operator can walk the verifier's full
    debugging trail — what did iter-1 flag, what did the main agent fix,
    what did iter-2 then flag, etc.

    The chip row remains the at-a-glance roll-up; the per-iteration
    tables are the debug surface.
    """
    if not iters:
        if legacy_count is not None:
            chip = (
                f'<p class="muted">{legacy_count} iteration{"s" if (legacy_count or 0) != 1 else ""} · '
                f'{legacy_residual or 0} residual{"s" if (legacy_residual or 0) != 1 else ""} '
                '(legacy scalar — per-iteration breakdown not recorded)</p>'
            )
            return chip, ""
        return '<p class="muted">No verification telemetry recorded.</p>', ""

    # ── Chip row (compact roll-up) ────────────────────────────────────
    chip_blocks: list[str] = []
    for it in iters:
        if not isinstance(it, dict):
            continue
        verdict = it.get("verdict", "?")
        kind = "ok" if verdict == "CLEAN" else "warn"
        n = it.get("n", "?")
        model = it.get("model", "unknown")
        t = it.get("truth", 0)
        e = it.get("editorial", 0)
        a = it.get("advisory", 0)
        chip_blocks.append(
            f'<span class="ops-pill ops-pill--{kind}">'
            f'#{_escape(str(n))} {_escape(verdict)} '
            f'<span class="muted">· {_escape(model)} · t={t} e={e} a={a}</span>'
            '</span>'
        )
    chips_html = '<div class="ops-chip-row">' + " ".join(chip_blocks) + '</div>'

    # ── Per-iteration findings tables (full-width, stacked) ───────────
    final_idx = len(iters) - 1

    def _render_one_iter_table(it: dict[str, Any], iter_idx: int) -> str:
        """Render the findings table for one iteration; return '' when
        the iteration has no findings[] or only empty entries."""
        findings = it.get("findings") or []
        # Filter out non-dict garbage early.
        findings = [fd for fd in findings if isinstance(fd, dict)]
        if not findings:
            return ""

        n = it.get("n", "?")
        verdict = (it.get("verdict") or "").upper() or "?"
        verdict_kind = "ok" if verdict == "CLEAN" else "warn"
        model = _ops_canonical_model(it.get("model"))
        t_count = it.get("truth", 0)
        e_count = it.get("editorial", 0)
        a_count = it.get("advisory", 0)
        dur = _ops_format_duration(it.get("duration_seconds"))
        is_final = iter_idx == final_idx
        cap_breach_badge = (
            ' <span class="ops-pill ops-pill--crit" title="cap-breach safety valve fired — brief published at iteration 5 without CLEAN">cap-breach</span>'
            if is_final and verdict == "NEEDS_FIXES" else ""
        )

        f_rows: list[str] = []
        for fd in findings:
            code = fd.get("code") or "?"
            category = fd.get("category") or _F_CODE_LABEL.get(code, "?")
            section = fd.get("section") or "—"
            item = (fd.get("item") or "")[:80]
            url_or_quote = (fd.get("url_or_quote") or "")[:120]
            summary = (fd.get("summary") or "")[:200]
            rem = (fd.get("remediation_applied") or "")[:160]
            outcome = (fd.get("remediation_outcome") or "")
            outcome_kind = {
                "fixed-clean": "ok", "fixed-degraded": "warn",
                "dropped-item": "neutral", "deferred": "warn",
                "residual-at-cap": "crit",
            }.get(outcome, "neutral")
            url_html = (
                f'<a class="mono" href="{_escape(_safe_url(url_or_quote))}" target="_blank" rel="noopener noreferrer">{_escape(url_or_quote)}</a>'
                if url_or_quote.startswith(("http://", "https://"))
                else f'<span class="muted mono">{_escape(url_or_quote)}</span>' if url_or_quote else ''
            )
            f_rows.append(
                '<tr>'
                f'<td><span class="mono"><strong>{_escape(code)}</strong></span><div class="muted mono" style="font-size:0.72rem">{_escape(category)}</div></td>'
                f'<td><span class="e-tag">{_escape(section)}</span></td>'
                f'<td>{_escape(item)}<div class="muted" style="font-size:0.72rem;margin-top:0.15rem">{url_html}</div></td>'
                f'<td>{_escape(summary)}</td>'
                f'<td><span class="mono">{_escape(rem) or "—"}</span>{(" " + _ops_pill(outcome, kind=outcome_kind)) if outcome else ""}</td>'
                '</tr>'
            )

        # Heading line: iteration number, verdict pill, counts, model, duration.
        heading = (
            f'<h4 class="ops-iter__head">'
            f'Iteration <span class="mono">#{_escape(str(n))}</span> '
            f'<span class="ops-pill ops-pill--{verdict_kind}">{_escape(verdict)}</span>'
            f'{cap_breach_badge}'
            f' <span class="muted">— {len(findings)} finding{"s" if len(findings) != 1 else ""} '
            f'(truth={t_count}, editorial={e_count}, advisory={a_count}) · '
            f'<span class="mono">{_escape(model)}</span>'
            f'{f" · {_escape(dur)}" if dur else ""}'
            '</span>'
            '</h4>'
        )
        return (
            '<div class="ops-iter">'
            + heading
            + '<div class="data-wrap"><table class="data ops-iter__table">'
            '<thead><tr><th>F-code</th><th>Section</th><th>Item · URL/quote</th>'
            '<th>Verifier summary</th><th>Remediation · outcome</th></tr></thead>'
            f'<tbody>{"".join(f_rows)}</tbody></table></div>'
            '</div>'
        )

    iter_tables: list[str] = []
    has_any_findings = False
    cap_breach_iter = None
    for idx, it in enumerate(iters):
        if not isinstance(it, dict):
            continue
        table = _render_one_iter_table(it, idx)
        if table:
            iter_tables.append(table)
            has_any_findings = True
        if idx == final_idx and (it.get("verdict") or "").upper() == "NEEDS_FIXES":
            cap_breach_iter = it

    # If the final iteration was a NEEDS_FIXES cap-breach but recorded no
    # findings[], note that explicitly — the operator still needs to see
    # the cap-breach signal even when the verifier's findings array is
    # empty (legacy contract).
    cap_breach_note = ""
    if cap_breach_iter is not None and not (cap_breach_iter.get("findings") or []):
        n = cap_breach_iter.get("n", "?")
        cap_breach_note = (
            '<div class="ops-iter ops-iter--no-detail">'
            f'<h4 class="ops-iter__head">Iteration <span class="mono">#{_escape(str(n))}</span> '
            '<span class="ops-pill ops-pill--crit">cap-breach</span></h4>'
            '<p class="muted">Cap-breach iteration recorded no per-finding detail. '
            'The dashboard cannot show WHAT the verifier flagged. '
            'See <code>.claude/agents/cti-verification.md</code> § Findings summary for the contract.</p>'
            '</div>'
        )

    findings_html = ""
    if has_any_findings or cap_breach_note:
        intro = (
            '<p class="muted ops-verif-intro">'
            'Per-iteration finding detail. Each table is one verifier pass — what was flagged, '
            'how the main agent remediated it, and the outcome. Walking the tables top-to-bottom '
            'shows the verifier\'s debugging trail across iterations.'
            '</p>'
        )
        findings_html = (
            '<div class="ops-latest__verification">'
            f'<h3 class="ops-mini-head">Verification findings — all iterations</h3>'
            + intro
            + "".join(iter_tables)
            + cap_breach_note
            + '</div>'
        )

    return chips_html, findings_html


def _ops_run_picker_label(run: dict[str, Any]) -> str:
    """One-line label for a run in the run-detail <select>.

    `<run_id> · <kind> · <verdict>` — e.g. "2026-07-03T0412Z-intel · intel ·
    CLEAN". Multiple runs per day make the date alone ambiguous, so the
    label leads with the run id. The verdict mirrors the clean-publish
    definition: residual == 0 ⇒ CLEAN, else NEEDS_FIXES with the residual
    count. Runs without verification telemetry show no verdict tag.
    """
    rid = run.get("run_id") or run.get("date") or "?"
    kind = run.get("kind", "intel")
    bits = [str(rid), str(kind)]
    if run.get("verification_iterations") is not None:
        residual = run.get("verification_residual_count") or 0
        if residual == 0:
            bits.append("CLEAN")
        else:
            bits.append(f"NEEDS_FIXES ({residual} residual)")
    return " · ".join(bits)


def _ops_render_latest_run_panel(run: dict[str, Any], palette: dict[str, str], *,
                                   prefix: str,
                                   day_pages: set[str] | None = None,
                                   run_entries: list[dict[str, Any]] | None = None) -> str:
    """Detailed panel for one run — main-agent model, every sub-agent's
    contribution + telemetry, verification roll-up, plus the entries the
    run published. The 'one glance, full picture' card."""
    date = run.get("date") or "?"
    rid = str(run.get("run_id") or date)
    kind = run.get("kind", "intel")
    day_pages = day_pages or set()
    main_name = _ops_canonical_model(run.get("model"))
    main_id = run.get("model_id") or ""
    main_colour = _ops_color_for_model(main_name, palette)
    pv = (run.get("prompt_version") or "?").lstrip("v")
    duration = _ops_format_duration(run.get("duration_seconds"))
    items_pub = run.get("entries_published")
    items_pub_str = str(items_pub) if items_pub is not None else "—"
    items_upd = run.get("entries_updated")
    items_upd_str = str(items_upd) if items_upd is not None else "—"
    deep_dive = run.get("deep_dive") or "—"
    failures = run.get("fetch_failures") or []

    # Sub-agent cards. Base slots per kind + any extra recorded keys
    # (the conditional S5 / W3 closed-source intake agents).
    base_keys = ("W1", "W2") if kind == "weekly" else ("S1", "S2", "S3", "S4")
    recorded = run.get("sub_agents") or {}
    extra_keys = tuple(k for k in sorted(recorded) if k not in base_keys)
    sa_cards: list[str] = []
    for k in base_keys + extra_keys:
        a = recorded.get(k) or {}
        sa_cards.append(_ops_render_subagent_card(k, a, palette))
    sa_grid = f'<div class="ops-sa-grid">{"".join(sa_cards)}</div>'

    # Entries this run published (links to permalinks).
    entries_block = ""
    if run_entries:
        lis = "".join(
            f'<li><a href="{prefix}entries/{_escape(e["id"])}/">{_escape(e.get("title") or e["id"])}</a>'
            f' <span class="e-tag">{_escape(e.get("kind") or "")}</span>'
            f' <span class="muted mono">{_escape(e.get("priority") or "")}</span>'
            + (' <span class="ops-pill ops-pill--neutral">update</span>' if e.get("update_of") else "")
            + "</li>"
            for e in run_entries
        )
        entries_block = (
            '<div class="ops-latest__failures">'
            '<h3 class="ops-mini-head">Entries published (this run)</h3>'
            f'<ul class="entity-list">{lis}</ul>'
            "</div>"
        )
    elif isinstance(items_pub, int) and items_pub == 0:
        entries_block = (
            '<div class="ops-latest__failures">'
            '<h3 class="ops-mini-head">Entries published (this run)</h3>'
            '<p class="muted">Empty run — no new verified signal; only the run record was published (a healthy outcome).</p>'
            "</div>"
        )

    # "Coverage gaps" table replaces the old "Fetch failures"
    # one. Schema is the same; the sub-agent prompt rule is that
    # only un-recoverable misses get logged here. Soft-signal records
    # (covered_anyway: true that survived from the old logging rule)
    # render with a yellow row badge.
    failures_html = _ops_render_fetch_failures(failures, prefix=prefix)
    # `bridge_uses[]` is an optional sub-agent telemetry stream
    # showing where the bridge was successfully invoked. Separate panel
    # so success and failure don't share a list.
    bridge_uses_html = _ops_render_bridge_uses(run.get("bridge_uses") or [])
    # per-run source-list edits, rendered inside this panel so the
    # run-detail selector shows each run's source changes, not just the latest.
    run_sources_changed_html = _ops_render_run_sources_changed(run, prefix=prefix)

    # verification iteration renderer now returns TWO fragments:
    # a compact chip row (iteration timeline) for the 2-col Verification
    # slot, and a full-width findings_html block (per-iteration finding
    # tables for EVERY iteration with findings — not just the final one).
    # The findings_html escapes the .ops-latest card the same way the
    # Coverage Gaps table does, so the operator gets full-page-width to
    # read the verifier's debugging trail across all iterations.
    iters = ((run.get("verification") or {}).get("iterations") or [])
    verif_chips_html, verif_findings_html = _ops_render_verification_iterations(
        iters,
        legacy_count=run.get("verification_iterations"),
        legacy_residual=run.get("verification_residual_count"),
    )

    return f"""
<div class="ops-latest">
  <div class="ops-latest__head">
    <div>
      {f'<a class="ops-latest__date mono" href="{prefix}briefs/{_escape(date)}/">{_escape(rid)}</a>' if date in day_pages else f'<span class="ops-latest__date mono">{_escape(rid)}</span>'}
      <span class="ops-pill ops-pill--neutral">{_escape(kind)}</span>
      <span class="ops-pill ops-pill--accent">prompt v{_escape(pv)}</span>
    </div>
    <div class="ops-latest__meta">
      <span class="mono">{_escape(duration)}</span>
      <span class="muted">duration</span>
      <span class="mono">{_escape(items_pub_str)}</span>
      <span class="muted">published</span>
      <span class="mono">{_escape(items_upd_str)}</span>
      <span class="muted">updates</span>
    </div>
  </div>
  <div class="ops-latest__main">
    <span class="ops-legend__swatch" style="background:{main_colour}"></span>
    <span class="mono"><strong>{_escape(main_name)}</strong></span>
    {f'<span class="mono muted">({_escape(main_id)})</span>' if main_id else ''}
    <span class="muted">main agent</span>
  </div>
  {sa_grid}
  <!-- Verification (chips only) + Deep-dive share a 2-column row at
       desktop; both are short so two columns is plenty. The per-
       iteration finding TABLES escape this row into a full-width
       section below the Coverage Gaps table. -->
  <div class="ops-latest__row ops-latest__row--summary">
    <div>
      <h3 class="ops-mini-head">Verification</h3>
      {verif_chips_html}
    </div>
    <div>
      <h3 class="ops-mini-head">Deep dive</h3>
      <p class="mono ops-deep">{_escape(deep_dive)}</p>
    </div>
  </div>
</div>

<!-- table renamed "Coverage gaps" because that's what it
     actually contains now (sub-agent prompt was tightened to only log
     real, unrecovered failures). The bridge_uses panel below it tracks
     bridge invocations separately so success and failure don't get
     conflated in the same list. -->
{entries_block}
{run_sources_changed_html}
<div class="ops-latest__failures">
  <h3 class="ops-mini-head">Coverage gaps (this run)</h3>
  <p class="muted ops-latest__failures-help">Sources <em>this run's</em> brief needed that returned no usable content via any documented recipe. Bridge-recovered or quiet-day sources do NOT appear here. (Distinct from the independent source-accessibility probe at the foot of this section, which probes <em>all</em> active sources regardless of what any run needed.)</p>
  {failures_html}
</div>
{bridge_uses_html}
{verif_findings_html}
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
        model_name = _ops_canonical_model(data.get("model"))
        return (
            f'<div class="ops-sa-card ops-sa-card--stalled">'
            f'<div class="ops-sa-card__head"><strong>{_escape(key)}</strong>'
            ' <span class="ops-pill ops-pill--crit">stalled</span></div>'
            f'<p class="muted mono">{_escape(model_name)}</p>'
            '<p class="muted">Past the 30-min wall-clock cap; abandoned.</p>'
            '</div>'
        )

    model_name = _ops_canonical_model(data.get("model"))
    model_id = data.get("model_id") or ""
    colour = _ops_color_for_model(model_name, palette)
    used = _ops_count_sources(data.get("sources_used"))
    attempted = _ops_count_sources(data.get("sources_attempted"))
    items = data.get("items_returned") or 0
    tele = data.get("telemetry") or {}

    # operator feedback drove a second round of card simplification:
    #   1. Drop the `used / attempted` progress bar entirely — it visually
    #      implied a quality score, but a 5/63-source slice on a quiet day
    #      is perfectly normal for S3 and 14/16 on a busy day for S1 is also
    #      normal. Same percentage, different meanings.
    #   2. Reorder metrics so what-the-agent-delivered is first, source
    #      coverage (a debug signal) is last.
    #   3. "Cited sources: 14 of 16 in slice" instead of "Sources 14 of 16
    #      contributed (87%)" — the new phrasing tells the operator what the
    #      denominator actually is (the spawn-message slice) without the
    #      misleading percentage chrome.

    def _format_duration(secs: Any) -> str | None:
        try:
            n = int(secs)
        except (TypeError, ValueError):
            return None
        if n < 60:
            return f"{n}s"
        return f"{n // 60}m {n % 60:02d}s"

    # Duration: prefer top-level duration_seconds; fall back to telemetry.
    dur_raw = data.get("duration_seconds")
    if dur_raw in (None, ""):
        dur_raw = tele.get("duration_seconds")
    dur_str = _format_duration(dur_raw)

    # 1. Items returned — primary "did the agent deliver" signal.
    items_line = (
        '<dt>Items returned</dt>'
        f'<dd><span class="mono">{items}</span></dd>'
    )

    # 2. Duration — wall-clock against the 30-min cap. Raw seconds in tooltip.
    if dur_str:
        duration_line = (
            '<dt>Duration</dt>'
            f'<dd><span class="mono" title="{dur_raw} s wall-clock; sub-agent cap is 30 min">{_escape(dur_str)}</span></dd>'
        )
    else:
        duration_line = '<dt>Duration</dt><dd class="muted">not reported</dd>'

    # 3. Tool calls — three related counters on one line.
    def _tc(name: str) -> Any:
        v = tele.get(name)
        if v in (None, ""):
            return None
        # Coerce non-numeric strings ("not captured", "unknown", "n/a", …) to
        # None so the card renders "not reported" instead of "not captured
        # WebFetch". Older sub-agent prompts allowed string sentinels; the
        # current contract says integer-or-omit.
        if isinstance(v, str):
            try:
                return int(v)
            except (TypeError, ValueError):
                return None
        return v

    wf = _tc("webfetch_calls")
    ws = _tc("websearch_calls")
    br = _tc("bridge_fetches")
    if wf is not None or ws is not None or br is not None:
        tc_parts = []
        if wf is not None:
            tc_parts.append(f'<span class="ops-sa-card__tc" title="WebFetch tool calls"><span class="mono">{_escape(str(wf))}</span> <span class="muted">WebFetch</span></span>')
        if ws is not None:
            tc_parts.append(f'<span class="ops-sa-card__tc" title="WebSearch tool calls"><span class="mono">{_escape(str(ws))}</span> <span class="muted">WebSearch</span></span>')
        if br is not None:
            tc_parts.append(f'<span class="ops-sa-card__tc" title="`python3 tools/fetch_source.py` invocations"><span class="mono">{_escape(str(br))}</span> <span class="muted">bridge</span></span>')
        toolcalls_line = (
            '<dt>Tool calls</dt>'
            f'<dd class="ops-sa-card__toolcalls">{"".join(tc_parts)}</dd>'
        )
    else:
        toolcalls_line = '<dt>Tool calls</dt><dd class="muted">not reported</dd>'

    # 4. Cited sources — single number with the denominator visible inline as
    # "of N in slice" (no percentage, no bar). Tooltip explains what the
    # denominator IS (the spawn-message slice) so the operator doesn't read
    # the number as a quality score.
    sources_tooltip = (
        f"sub-agent was given a {attempted}-source slice in its spawn message; "
        "cited the listed N. quiet-day slices legitimately cite few — this is "
        "coverage telemetry, not a quality score."
    )
    if attempted:
        cited_line = (
            '<dt>Cited sources</dt>'
            f'<dd><span class="mono" title="{_escape(sources_tooltip)}">{used}</span>'
            f' <span class="muted">of {attempted} in slice</span></dd>'
        )
    elif used:
        cited_line = (
            '<dt>Cited sources</dt>'
            f'<dd><span class="mono">{used}</span></dd>'
        )
    else:
        cited_line = '<dt>Cited sources</dt><dd class="muted">none</dd>'

    # Optional extras (urls_checked, tokens_in/out) — deemphasised secondary row.
    extras: list[str] = []
    if _tc("urls_checked") is not None:
        extras.append(f'<span class="ops-sa-card__extra"><span class="mono">{_escape(str(_tc("urls_checked")))}</span> <span class="muted">URLs checked</span></span>')
    if _tc("tokens_in") is not None or _tc("tokens_out") is not None:
        ti = _tc("tokens_in")
        to = _tc("tokens_out")
        if ti is not None:
            extras.append(f'<span class="ops-sa-card__extra"><span class="mono">{_escape(str(ti))}</span> <span class="muted">tokens in</span></span>')
        if to is not None:
            extras.append(f'<span class="ops-sa-card__extra"><span class="mono">{_escape(str(to))}</span> <span class="muted">tokens out</span></span>')
    extras_block = (
        f'<div class="ops-sa-card__extras">{"".join(extras)}</div>'
        if extras else ""
    )

    return f"""
<div class="ops-sa-card">
  <div class="ops-sa-card__head">
    <strong>{_escape(key)}</strong>
    <span class="ops-legend__swatch" style="background:{colour}"></span>
    <span class="mono">{_escape(model_name)}</span>
    {f'<span class="mono muted">({_escape(model_id)})</span>' if model_id else ''}
  </div>
  <dl class="ops-sa-card__metrics">
    {items_line}
    {duration_line}
    {toolcalls_line}
    {cited_line}
  </dl>
  {extras_block}
</div>
"""


def _ops_render_runs_table(runs: list[dict[str, Any]], palette: dict[str, str], *,
                            prefix: str,
                            day_pages: set[str] | None = None) -> str:
    day_pages = day_pages or set()
    if not runs:
        return (
            '<div class="empty">'
            '<p>No run records under <code>runs/</code> yet.</p>'
            '<p class="muted">Every pipeline fire writes one record at <code>runs/&lt;date&gt;/&lt;run-id&gt;.md</code> in its final phase. The first run will create it.</p>'
            '</div>'
        )

    def _sa_cell(a: dict[str, Any] | None) -> str:
        if not a:
            return '<span class="muted">—</span>'
        if a.get("returned") is False:
            return '<span class="ops-pill ops-pill--crit">stalled</span>'
        used = _ops_count_sources(a.get("sources_used"))
        attempted = _ops_count_sources(a.get("sources_attempted"))
        items = a.get("items_returned") or 0
        m = _ops_canonical_model(a.get("model"))
        colour = _ops_color_for_model(m, palette) if m else "var(--text-muted)"
        # runs-table cells show the items-returned headline only;
        # source coverage moved to a tooltip on the cell. The inline
        # "(12/18 sources)" parenthetical was visual clutter at table
        # density and the number-pair was ambiguous without context.
        tooltip = (
            f"{_escape(m or 'unknown')} · "
            f"{used} of {attempted} sources cited (slice size = {attempted}, contributed = {used})"
            if attempted else _escape(m or "unknown")
        )
        return (
            f'<span class="ops-legend__swatch" style="background:{colour}" '
            f'title="{tooltip}"></span>'
            f' <span class="mono" title="{tooltip}">{items}</span>'
            f'<span class="muted" title="{tooltip}"> items</span>'
        )

    rows: list[str] = []
    for r in runs:
        sa = r.get("sub_agents") or {}
        kind = r.get("kind", "intel")
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
        main_name = _ops_canonical_model(r.get("model"))
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
        items_pub = r.get("entries_published")
        items_pub_str = str(items_pub) if items_pub is not None else "—"
        items_upd = r.get("entries_updated")
        items_upd_str = str(items_upd) if items_upd is not None else "—"
        sc = [c for c in (r.get("sources_changed") or []) if isinstance(c, dict)]
        if sc:
            sc_counts = Counter(c.get("change") for c in sc)
            sc_tip = ", ".join(f"{n} {k}" for k, n in sc_counts.most_common())
            src_delta_html = (f'<span class="ops-pill ops-pill--neutral" title="{_escape(sc_tip)}">'
                              f'{len(sc)}</span>')
        else:
            src_delta_html = '<span class="muted">0</span>'

        rid = str(r.get("run_id") or r.get("date") or "?")
        rdate = str(r.get("date") or "")
        date_cell = (
            f'<a href="{prefix}briefs/{_escape(rdate)}/" title="{_escape(rid)}">{_escape(rdate)}</a>'
            if rdate in day_pages
            else f'<span title="{_escape(rid)}">{_escape(rdate or "?")}</span>'
        )
        rows.append(
            '<tr>'
            f'<td class="mono">{date_cell}</td>'
            f'<td><span class="ops-pill ops-pill--neutral">{_escape(kind)}</span></td>'
            f'<td><span class="ops-legend__swatch" style="background:{main_colour}"></span>'
            f' <span class="mono">{_escape(main_name)}</span></td>'
            f'<td class="mono muted">v{_escape(str(r.get("prompt_version", "?")).lstrip("v"))}</td>'
            f'<td class="mono">{_escape(duration)}</td>'
            f'<td class="mono">{_escape(items_pub_str)}</td>'
            f'<td class="mono">{_escape(items_upd_str)}</td>'
            f'{cells}'
            f'<td>{failures_html}</td>'
            f'<td>{src_delta_html}</td>'
            f'<td>{verif_html}</td>'
            '</tr>'
        )

    table = (
        '<div class="data-wrap"><table class="data ops-runs-table">'
        '<thead><tr><th>Run</th><th>Kind</th><th>Main model</th><th>Prompt</th><th>Duration</th>'
        '<th title="Entries published this run">Entries</th>'
        '<th title="Of which update_of entries">Upd</th>'
        '<th>S1/W1</th><th>S2/W2</th><th>S3</th><th>S4</th>'
        '<th title="Fetch failures (coverage gaps)">Fetch fail</th>'
        '<th title="sources/sources.json edits this run (hover for breakdown)">Src Δ</th>'
        '<th>Verif</th></tr></thead>'
        '<tbody data-pager-rows>' + "".join(rows) + '</tbody></table></div>'
    )
    return _ops_pager_wrap(table, pagesize=10, size_select=True)



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


# === SECTOR-SPECIFIC RSS FEED SLICES ======================
#
# One feed per audience sector. Each is a filtered slice of build_items_feed
# (per-H3 entries) where the item's footer Sector / Tags carry the relevant
# value. Subscribers filter at the feed layer instead of trying to parse the
# brief.
#
# (sector_filename, [accept_sectors], [accept_tags], title_suffix, description)
_DEFAULT_SECTOR_FEED_SLICES: list[tuple[str, tuple[str, ...], tuple[str, ...], str, str]] = [
    (
        "feed-public-sector.xml",
        ("public-sector",),
        (),
        "Public sector",
        "Items affecting public-sector environments (national / cantonal / federal administration, regulators, public-sector technology suppliers).",
    ),
    (
        "feed-healthcare.xml",
        ("healthcare",),
        (),
        "Healthcare",
        "Items affecting healthcare providers, hospitals, public health, medical devices.",
    ),
    (
        "feed-finance.xml",
        ("finance",),
        (),
        "Finance",
        "Items affecting financial services, banks, insurance, fintech.",
    ),
    (
        "feed-energy.xml",
        ("energy",),
        (),
        "Energy",
        "Items affecting energy operators, utilities, grid infrastructure.",
    ),
    (
        "feed-ot-ics.xml",
        ("energy", "water", "manufacturing", "transport"),
        ("ot-ics",),
        "OT / ICS",
        "Items affecting operational-technology / industrial-control-system environments — energy, water, manufacturing, transport, and any item tagged ot-ics.",
    ),
    (
        "feed-defense.xml",
        ("defense",),
        (),
        "Defense",
        "Items affecting defense, intelligence, military supply chain.",
    ),
    (
        "feed-telco.xml",
        ("telco",),
        (),
        "Telecommunications",
        "Items affecting telecommunications operators and infrastructure.",
    ),
    (
        "feed-education.xml",
        ("education",),
        (),
        "Education",
        "Items affecting education institutions, ed-tech platforms, research universities.",
    ),
]

# config/branding.yaml `feeds.sector_slices` replaces the default slice set
# wholesale when non-empty.
SECTOR_FEED_SLICES: list[tuple[str, tuple[str, ...], tuple[str, ...], str, str]] = (
    branding_config.sector_feed_slices(BRANDING, _DEFAULT_SECTOR_FEED_SLICES)
)

FEEDS_PAGE_DESCRIPTION = (
    "All RSS feeds — daily, weekly, per item, plus eight sector-specific "
    "slices (public sector, healthcare, finance, energy, OT/ICS, defense, "
    "telco, education)."
    if SECTOR_FEED_SLICES is _DEFAULT_SECTOR_FEED_SLICES
    else "All RSS feeds — daily, weekly, per item, plus "
    f"{len(SECTOR_FEED_SLICES)} sector-specific slices "
    "(" + ", ".join(s[3] for s in SECTOR_FEED_SLICES) + ")."
)



# === FEED BUILDERS (v3) ================================================


def _day_pub_ts(day_entries: list[dict[str, Any]]) -> datetime:
    """A day page's publish moment = the newest discovered_at among its
    entries (deterministic; true discovery latency, not commit time)."""
    best = datetime(2000, 1, 1, tzinfo=timezone.utc)
    for e in day_entries:
        ts = parse_ts(e.get("discovered_at"))
        if ts and ts > best:
            best = ts
    return best


def build_daily_feed(
    days: dict[str, list[dict[str, Any]]],
    runs_by_day: dict[str, list[dict[str, Any]]],
    *,
    site_url: str,
    ref_ts: datetime,
) -> tuple[str, datetime]:
    """feed.xml — one item per DAY page: title `CTI Daily Brief — <date>`,
    description = the day's TL;DR bullets, content = the day page's body
    HTML. Last FEED_DAILY_MAX days."""
    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for day in sorted(days.keys(), reverse=True)[:FEED_DAILY_MAX]:
        day_entries = sorted(operational_entries(days[day]), key=entry_sort_key)
        url = f"{site_url}briefs/{day}/"
        by_id = {e["id"]: e for e in day_entries}
        body_html = render_brief_sections(
            day_entries, runs_by_day.get(day, []),
            prefix=site_url, base_url=url, entries_by_id=by_id,
        )
        tldr = select_tldr_entries(day_entries)
        desc_html = render_tldr_bullets(tldr, prefix=site_url)
        cve_ids = sorted({c for e in day_entries for c in entry_cve_ids(e)})
        cats = "".join(f"<category>{_escape(c)}</category>" for c in cve_ids[:8])
        pub = _day_pub_ts(day_entries)
        items_xml.append(
            "<item>"
            f"<title>{_escape(f'CTI Daily Brief — {day}')}</title>"
            f"<link>{_escape(url)}</link>"
            f'<guid isPermaLink="true">{_escape(url)}</guid>'
            f"<pubDate>{rfc822(pub)}</pubDate>"
            f"<dc:date>{_escape(pub.strftime('%Y-%m-%dT%H:%M:%SZ'))}</dc:date>"
            f"{cats}"
            f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
            f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
            "</item>"
        )
        if pub > most_recent:
            most_recent = pub
    feed = _channel_rss(
        title=f"{SITE_NAME} — Daily ({TAGLINE})",
        link=site_url,
        self_link=site_url + "feed.xml",
        description=FEED_DAILY_DESCRIPTION,
        last_build=rfc822(most_recent if items_xml else ref_ts),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


def build_weekly_feed(
    weeks: dict[str, list[dict[str, Any]]],
    runs_by_week: dict[str, list[dict[str, Any]]],
    *,
    site_url: str,
    ref_ts: datetime,
) -> tuple[str, datetime]:
    """feed-weekly.xml — one item per weekly page, last FEED_WEEKLY_MAX."""
    items_xml: list[str] = []
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for week in sorted(weeks.keys(), reverse=True)[:FEED_WEEKLY_MAX]:
        strat = sorted(strategic_entries(weeks[week]), key=entry_sort_key)
        url = f"{site_url}weekly/{week}/"
        by_id = {e["id"]: e for e in strat}
        body_html = render_weekly_sections(
            strat, runs_by_week.get(week, []),
            prefix=site_url, base_url=url, entries_by_id=by_id,
        )
        glance = [e for e in strat if e.get("priority") in ("critical", "high")]
        desc_html = render_tldr_bullets(glance, prefix=site_url)
        cve_ids = sorted({c for e in strat for c in entry_cve_ids(e)})
        cats = "".join(f"<category>{_escape(c)}</category>" for c in cve_ids[:8])
        pub = _day_pub_ts(strat)
        items_xml.append(
            "<item>"
            f"<title>{_escape(f'CTI Weekly Summary — {week}')}</title>"
            f"<link>{_escape(url)}</link>"
            f'<guid isPermaLink="true">{_escape(url)}</guid>'
            f"<pubDate>{rfc822(pub)}</pubDate>"
            f"<dc:date>{_escape(pub.strftime('%Y-%m-%dT%H:%M:%SZ'))}</dc:date>"
            f"{cats}"
            f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
            f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
            "</item>"
        )
        if pub > most_recent:
            most_recent = pub
    feed = _channel_rss(
        title=f"{SITE_NAME} — Weekly ({TAGLINE})",
        link=site_url,
        self_link=site_url + "feed-weekly.xml",
        description=FEED_WEEKLY_DESCRIPTION,
        last_build=rfc822(most_recent if items_xml else ref_ts),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


def _entry_feed_item(entry: dict[str, Any], *, site_url: str,
                     entries_by_id: dict[str, dict[str, Any]] | None = None) -> str:
    """One RSS <item> for an entry: title = headline, description =
    summary, content = rendered body + badge footer, pubDate =
    discovered_at, categories = tags + regions + CVE ids."""
    url = site_url + entry_url_path(entry)
    ts = parse_ts(entry.get("discovered_at")) or datetime(2000, 1, 1, tzinfo=timezone.utc)
    body_html = (
        render_entry_card(entry, prefix=site_url, base_url=url,
                          entries_by_id=entries_by_id)
    )
    cat_parts = (
        list(entry.get("tags") or [])
        + list(entry.get("regions") or [])
        + entry_cve_status_union(entry)
        + entry_cve_ids(entry)
    )
    cats = "".join(f"<category>{_escape(c)}</category>" for c in cat_parts[:16])
    desc_html = f"<p>{_inline_text(entry.get('summary') or '')}</p>"
    return (
        "<item>"
        f"<title>{_escape(entry.get('headline') or entry.get('title') or entry['id'])}</title>"
        f"<link>{_escape(url)}</link>"
        f'<guid isPermaLink="true">{_escape(url)}</guid>'
        f"<pubDate>{rfc822(ts)}</pubDate>"
        f"<dc:date>{_escape(entry.get('discovered_at') or '')}</dc:date>"
        f"{cats}"
        f"<description><![CDATA[{_cdata_safe(desc_html)}]]></description>"
        f"<content:encoded><![CDATA[{_cdata_safe(body_html)}]]></content:encoded>"
        "</item>"
    )


def build_items_feed(
    entries: list[dict[str, Any]],
    *,
    site_url: str,
    ref_ts: datetime,
) -> tuple[str, datetime]:
    """feed-items.xml — one item per ENTRY, last FEED_ITEMS_MAX, newest
    first by discovered_at (true discovery latency)."""
    by_id = {e["id"]: e for e in entries}
    ordered = sorted(
        entries,
        key=lambda e: (str(e.get("discovered_at") or ""), e["id"]),
        reverse=True,
    )[:FEED_ITEMS_MAX]
    items_xml = [_entry_feed_item(e, site_url=site_url, entries_by_id=by_id) for e in ordered]
    most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
    for e in ordered:
        ts = parse_ts(e.get("discovered_at"))
        if ts and ts > most_recent:
            most_recent = ts
    feed = _channel_rss(
        title=f"{SITE_NAME} — Per item",
        link=site_url,
        self_link=site_url + "feed-items.xml",
        description=FEED_ITEMS_DESCRIPTION,
        last_build=rfc822(most_recent if ordered else ref_ts),
        items_xml="".join(items_xml),
    )
    return feed, most_recent


def build_sector_feeds(
    entries: list[dict[str, Any]],
    *,
    site_url: str,
    ref_ts: datetime,
) -> list[tuple[str, str, datetime]]:
    """The 8 sector slices — the per-entry feed filtered on entry
    sectors / tags (SECTOR_FEED_SLICES, branding-overridable). Returns
    `[(filename, xml, most_recent_ts), …]`."""
    by_id = {e["id"]: e for e in entries}
    out: list[tuple[str, str, datetime]] = []
    for fname, accept_sectors, accept_tags, title_suffix, description in SECTOR_FEED_SLICES:
        accept_sectors_set = set(accept_sectors)
        accept_tags_set = set(accept_tags)
        candidates = [
            e for e in entries
            if (set(e.get("sectors") or []) & accept_sectors_set)
            or (set(e.get("tags") or []) & accept_tags_set)
        ]
        candidates.sort(
            key=lambda e: (str(e.get("discovered_at") or ""), e["id"]), reverse=True
        )
        candidates = candidates[:FEED_ITEMS_MAX]
        items_xml = [
            _entry_feed_item(e, site_url=site_url, entries_by_id=by_id)
            for e in candidates
        ]
        most_recent = datetime.fromtimestamp(0, tz=timezone.utc)
        for e in candidates:
            ts = parse_ts(e.get("discovered_at"))
            if ts and ts > most_recent:
                most_recent = ts
        feed = _channel_rss(
            title=f"{SITE_NAME} — {title_suffix}",
            link=site_url,
            self_link=site_url + fname,
            description=description,
            last_build=rfc822(most_recent if candidates else ref_ts),
            items_xml="".join(items_xml),
        )
        out.append((fname, feed, most_recent))
    return out


# Stable colour palette for non-model legend swatches (donut slices,
# bar segments). Distinct from `_MODEL_PALETTE` so a future page that
# ever needs both at once doesn't collide.
_ENTITY_PALETTE: list[str] = BRANDING["charts"]["entity_palette"] or [
    "#e85d75", "#79c0ff", "#56d364", "#ffd866", "#d2a8ff",
    "#ff9b6b", "#56b3d3", "#bd9bff", "#9bdc4d", "#f48fb1",
    "#a3d977", "#7eb9ff",
]


def _entity_palette_color(label: str, assigned: dict[str, str]) -> str:
    key = (label or "").strip().lower()
    if not key:
        return "var(--text-muted)"
    if key in assigned:
        return assigned[key]
    color = _ENTITY_PALETTE[len(assigned) % len(_ENTITY_PALETTE)]
    assigned[key] = color
    return color


def _fill_weekly_timeline(buckets: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Take a sparse `[(YYYY-Www, count)]` list and fill in zero counts
    for every ISO week between min and max so the sparkline shows the
    coverage rhythm rather than a single dot. If only one bucket
    exists, return it as-is — the sparkline helper handles that."""
    if len(buckets) < 2:
        return buckets
    from datetime import date as _date, timedelta as _td

    def parse_wk(s: str) -> _date | None:
        m = re.match(r"^(\d{4})-W(\d{2})$", s)
        if not m:
            return None
        try:
            return _date.fromisocalendar(int(m.group(1)), int(m.group(2)), 1)
        except (ValueError, OverflowError):
            return None

    by_label = dict(buckets)
    starts = [parse_wk(lbl) for lbl, _ in buckets]
    starts = [s for s in starts if s]
    if len(starts) < 2:
        return buckets
    cur, end = min(starts), max(starts)
    out: list[tuple[str, int]] = []
    while cur <= end:
        iso_year, iso_week, _ = cur.isocalendar()
        lbl = f"{iso_year}-W{iso_week:02d}"
        out.append((lbl, by_label.get(lbl, 0)))
        cur += _td(days=7)
    return out


def render_redirect_page(
    target_url: str, *, title: str, site_url: str, cachebust: str,
) -> str:
    """Minimal HTML meta-refresh stub. Used at /cves/<id>/ and
    /topics/<key>/ now that the canonical URL is /entities/<key>/.

    Plain HTML, not the full base_template — these pages are never
    indexed (canonical points elsewhere), and we don't want the navbar /
    analytics overhead of a full render for what's essentially a
    redirect."""
    safe_target = _safe_url(target_url)
    return (
        '<!doctype html>\n<html lang="en"><head>\n'
        '<meta charset="utf-8">\n'
        f'<title>{_escape(title)}</title>\n'
        f'<link rel="canonical" href="{_escape(site_url + target_url.lstrip("/"))}">\n'
        f'<meta http-equiv="refresh" content="0; url={_escape(safe_target)}">\n'
        '<meta name="robots" content="noindex">\n'
        '</head><body>\n'
        f'<p>Redirecting to <a href="{_escape(safe_target)}">{_escape(target_url)}</a>.</p>\n'
        '</body></html>\n'
    )


def _entity_url(entity: dict[str, Any], *, prefix: str = "") -> str:
    """Canonical URL for an entity. Always under /entities/<key>/."""
    key = entity.get("key") or ""
    return f"{prefix}entities/{urllib.parse.quote(key, safe='')}/"


def render_overview_charts(
    entities: list[dict[str, Any]],
    *,
    prefix: str,
    label: str = "entities",
) -> str:
    """KPI strip + type-distribution donut + activity sparkline for the
    CVE / topic / entity overview pages. Reuses the Ops-page SVG
    primitives so the dashboard look stays consistent across the
    site. Returns an HTML block ready to drop into a page body.

    The strip auto-adapts to the entity set passed in:
      - /cves/ overview filters to type=cve  → Year-distribution bars
      - /topics/ overview filters out CVEs   → Type-distribution donut
      - /entities/ overview shows everything → Type-distribution donut
                                                + Coverage activity
                                                  sparkline (per ISO
                                                  week, last 26 weeks)
    """
    if not entities:
        return '<div class="empty muted">No entities yet.</div>'

    total = len(entities)
    by_type: dict[str, int] = {}
    by_year: dict[str, int] = {}
    weeks_combined: dict[str, int] = {}
    sources_total: set[str] = set()
    related_total = 0
    appearances_total = 0
    last_30d_count = 0

    from datetime import date as _date, timedelta as _td
    today = _date.today()
    cutoff = today - _td(days=30)

    for e in entities:
        t = e.get("type") or "—"
        by_type[t] = by_type.get(t, 0) + 1
        appearances_total += len(e.get("appearances", []) or [])
        for h in (e.get("source_distribution") or {}).keys():
            sources_total.add(h)
        related_total += len(e.get("related_entities", []) or [])
        # Per-year bucket from CVE id when applicable.
        if t == "cve":
            ym = re.match(r"^CVE-(\d{4})", e.get("key", ""))
            if ym:
                by_year[ym.group(1)] = by_year.get(ym.group(1), 0) + 1
        # Recent-30-day coverage.
        last = e.get("last_covered") or ""
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", last)
        if m:
            try:
                d = _date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                if d >= cutoff:
                    last_30d_count += 1
            except (ValueError, OverflowError):
                pass
        # Roll up weekly buckets across the entity set.
        for wk, n in (e.get("weekly_buckets") or []):
            weeks_combined[wk] = weeks_combined.get(wk, 0) + n

    # Top types (any with at least one entry).
    type_pairs = sorted(by_type.items(), key=lambda kv: -kv[1])
    assigned: dict[str, str] = {}
    type_slices = [(k, float(v), _entity_palette_color(k, assigned)) for k, v in type_pairs]
    donut_html = _ops_svg_donut(type_slices, size=140, label=f"{label} by type")

    # Per-year bars when CVE-heavy (only show if we have ≥ 2 distinct years).
    bars_block = ""
    if len(by_year) >= 2:
        year_pairs = sorted(by_year.items(), key=lambda kv: kv[0])
        bar_svg = _ops_svg_bars([float(v) for _, v in year_pairs], width=320, height=80,
                                 label="CVE entries by year")
        legend_lis = "".join(
            f'<li class="ops-legend__item">'
            f'<span class="ops-legend__swatch" style="background:var(--accent-soft)"></span>'
            f'<span class="ops-legend__label">{_escape(y)}</span>'
            f'<span class="ops-legend__value mono">{n}</span></li>'
            for y, n in year_pairs
        )
        bars_block = (
            '<div class="ops-chart-card">'
            '<h3 class="section-head" style="margin-top:0">By year</h3>'
            f'{bar_svg}'
            f'<ul class="ops-legend">{legend_lis}</ul>'
            '</div>'
        )

    # Activity sparkline — last 26 weeks of combined coverage.
    spark_block = ""
    if weeks_combined:
        all_weeks = sorted(weeks_combined.keys())[-26:]
        spark_values = [float(weeks_combined.get(w, 0)) for w in all_weeks]
        spark_svg = _ops_svg_sparkline(
            spark_values, width=300, height=58,
            label=f"Aggregate {label} mentions per week"
        )
        spark_block = (
            '<div class="ops-chart-card">'
            '<h3 class="section-head" style="margin-top:0">Recent coverage</h3>'
            '<p class="muted" style="font-size:0.78rem;margin:0 0 0.3rem">'
            f'Aggregate mentions per ISO week, last {len(all_weeks)} weeks.'
            '</p>'
            f'{spark_svg}'
            '</div>'
        )

    # KPI strip.
    kpi_html = (
        '<div class="ops-kpi-grid">'
        + _ops_kpi_tile(f"Total {label}", str(total),
                         sub=f"{len(by_type)} types", kind="accent")
        + _ops_kpi_tile("Recent (30 d)", str(last_30d_count),
                         sub="entities with new coverage in window",
                         kind="ok" if last_30d_count else "neutral")
        + _ops_kpi_tile("Distinct sources", str(len(sources_total)),
                         sub="hosts cited at least once")
        + _ops_kpi_tile("Total appearances", str(appearances_total),
                         sub="brief-section attributions")
        + _ops_kpi_tile("Co-occurrence links", str(related_total),
                         sub="entity ↔ entity in same item")
        + '</div>'
    )

    donut_block = (
        '<div class="ops-chart-card">'
        '<h3 class="section-head" style="margin-top:0">By type</h3>'
        f'{donut_html}'
        '</div>'
    )

    return (
        '<section class="ops-section">'
        f'{kpi_html}'
        '<div class="ops-charts-row">'
        f'{donut_block}'
        f'{spark_block}'
        f'{bars_block}'
        '</div>'
        '</section>'
    )


def render_sources_overview_charts(
    sources: list[dict[str, Any]],
    *,
    prefix: str,
) -> str:
    """Bias-detection chart strip for the /sources/ overview page.

    Surfaces the kind of structural questions an operator should be
    asking weekly:
      - Status / reliability / category distribution — does the source
        list lean toward news outlets or national CERTs?
      - Most-cited sources (top 12) — which sources do briefs actually
        rely on? An over-narrow distribution is a citation-bias risk.
      - Cited-count per category bars — are HIGH-reliability categories
        (national CERT, vendor PSIRT) under-cited relative to their
        share of the source list? That's the lopsided-coverage signal.
      - Active-but-never-cited count — sources kept on the active list
        that aren't pulling weight; rotation candidates.
    """
    if not sources:
        return '<div class="empty muted">No sources yet.</div>'

    total = len(sources)
    by_status: dict[str, int] = {}
    by_reliability: dict[str, int] = {}
    by_category: dict[str, int] = {}
    citations_by_category: dict[str, int] = {}
    citations_by_source: list[tuple[str, str, int]] = []  # (id, publisher, count)
    active_uncited = 0
    n_active = n_demoted = n_candidate = 0

    for s in sources:
        status = s.get("status") or "—"
        by_status[status] = by_status.get(status, 0) + 1
        if status == "active":
            n_active += 1
        elif status == "demoted":
            n_demoted += 1
        elif status == "candidate":
            n_candidate += 1
        by_reliability[s.get("reliability") or "—"] = by_reliability.get(s.get("reliability") or "—", 0) + 1
        cats = s.get("category") or []
        n_apps = len(s.get("appearances") or [])
        for c in cats:
            by_category[c] = by_category.get(c, 0) + 1
            citations_by_category[c] = citations_by_category.get(c, 0) + n_apps
        if s.get("status") == "active" and n_apps == 0:
            active_uncited += 1
        citations_by_source.append((s.get("id", ""), s.get("publisher", "") or s.get("id", ""), n_apps))

    # KPI strip.
    kpi_html = (
        '<div class="ops-kpi-grid">'
        + _ops_kpi_tile("Total sources", str(total),
                         sub=f"{len(by_category)} categories", kind="accent")
        + _ops_kpi_tile("Active", str(n_active),
                         sub=f"{active_uncited} never cited",
                         kind="warn" if active_uncited > n_active * 0.25 else "ok")
        + _ops_kpi_tile("Candidate", str(n_candidate),
                         sub="awaiting promotion review")
        + _ops_kpi_tile("Demoted", str(n_demoted),
                         sub="kept for audit history",
                         kind="neutral")
        + _ops_kpi_tile("Citation density",
                         f"{sum(c for _, _, c in citations_by_source)}",
                         sub=f"avg {sum(c for _, _, c in citations_by_source) / max(n_active, 1):.1f} per active source")
        + '</div>'
    )

    # Status donut.
    assigned_a: dict[str, str] = {}
    status_slices = [
        (k, float(v), _entity_palette_color(k, assigned_a))
        for k, v in sorted(by_status.items(), key=lambda kv: -kv[1])
    ]
    status_donut = _ops_svg_donut(status_slices, size=140, label="Sources by status")

    # Reliability donut — fixed colour mapping so HIGH always reads green.
    reliability_color = {
        "HIGH": BRANDING["charts"]["reliability_high"].strip() or "#56d364",
        "MEDIUM": BRANDING["charts"]["reliability_medium"].strip() or "#ffd866",
        "LOW": BRANDING["charts"]["reliability_low"].strip() or "#e85d75",
        "—": "var(--text-muted)",
    }
    rel_slices = [
        (k, float(v), reliability_color.get(k, "var(--text-muted)"))
        for k, v in sorted(by_reliability.items(), key=lambda kv: (-kv[1], kv[0]))
    ]
    rel_donut = _ops_svg_donut(rel_slices, size=140, label="Sources by reliability")

    # Top-12 most-cited sources — bias surface.
    top_cited = sorted(
        [t for t in citations_by_source if t[2] > 0],
        key=lambda t: (-t[2], t[1].lower()),
    )[:12]
    top_block = ""
    if top_cited:
        bar_svg = _ops_svg_bars(
            [float(c) for _, _, c in top_cited], width=320, height=80,
            label="Top-cited sources",
        )
        legend_lis = "".join(
            f'<li class="ops-legend__item">'
            f'<span class="ops-legend__swatch" style="background:var(--accent-soft)"></span>'
            f'<span class="ops-legend__label">'
            f'<a href="{prefix}sources/{urllib.parse.quote(sid, safe="")}/">{_escape(pub[:40])}</a>'
            f'</span>'
            f'<span class="ops-legend__value mono">{n}</span></li>'
            for sid, pub, n in top_cited
        )
        top_block = (
            '<div class="ops-chart-card">'
            '<h3 class="section-head" style="margin-top:0">Most-cited sources</h3>'
            '<p class="muted" style="font-size:0.78rem;margin:0 0 0.3rem">'
            'Top 12 by brief-appearance count. A narrow distribution here is a '
            'citation-bias risk — look for diversity of publisher and category.'
            '</p>'
            f'{bar_svg}'
            f'<ul class="ops-legend">{legend_lis}</ul>'
            '</div>'
        )

    # Per-category citation bars — bias detector. Shows total citations
    # per category alongside source count to surface lopsided coverage
    # (e.g. many news sources but few national CERT citations).
    cat_pairs = sorted(by_category.items(), key=lambda kv: -citations_by_category.get(kv[0], 0))[:14]
    cat_block = ""
    if cat_pairs:
        # Two stacked metrics per category: source count + citation count.
        # Render as a side-by-side legend table — easier to read than dual bars.
        rows = []
        for cat, src_count in cat_pairs:
            cit_count = citations_by_category.get(cat, 0)
            ratio = cit_count / max(src_count, 1)
            kind_pill = '<span class="badge badge--low" title="cited fewer than 0.5 times per active source on average">under-cited</span>' if ratio < 0.5 else (
                '<span class="badge badge--accent" title="cited heavily relative to source count">heavy</span>' if ratio > 3 else ''
            )
            rows.append(
                f'<tr><td><a href="{prefix}sources/?cat={_escape(cat)}">{_escape(cat)}</a></td>'
                f'<td class="mono">{src_count}</td>'
                f'<td class="mono">{cit_count}</td>'
                f'<td class="mono">{ratio:.1f}{kind_pill}</td></tr>'
            )
        cat_block = (
            '<div class="ops-chart-card" style="grid-column:1/-1">'
            '<h3 class="section-head" style="margin-top:0">Citations per category</h3>'
            '<p class="muted" style="font-size:0.78rem;margin:0 0 0.3rem">'
            '<code>citations / sources</code> &lt; 0.5 means a category has many sources but few citations '
            '(over-supplied); &gt; 3 means heavy concentration on a small number of sources.'
            '</p>'
            '<div class="data-wrap"><table class="data">'
            '<thead><tr><th>Category</th><th>Sources</th><th>Citations</th><th>Ratio</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody>'
            '</table></div>'
            '</div>'
        )

    # Fetch-failure sparklines live on /ops/ (run-log table + Coverage
    # gaps), not on the source-catalogue page.

    return (
        '<section class="ops-section">'
        f'{kpi_html}'
        '<div class="ops-charts-row">'
        f'<div class="ops-chart-card">'
        '<h3 class="section-head" style="margin-top:0">By status</h3>'
        f'{status_donut}'
        '</div>'
        f'<div class="ops-chart-card">'
        '<h3 class="section-head" style="margin-top:0">By reliability</h3>'
        f'{rel_donut}'
        '</div>'
        f'{top_block}'
        f'{cat_block}'
        '</div>'
        '</section>'
    )


def render_entities_index_page(
    entities: list[dict[str, Any]],
    *,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Unified /entities/ index — every entity, every type, with the
    same KPI strip + chart row that the per-page renderer uses, and a
    type-filter chip toolbar above a single ranked list."""
    types = sorted({e.get("type", "") for e in entities if e.get("type")})
    type_chips = "".join(
        f'<span class="chip" data-filter-chip="entity-type" data-value="{_escape(t)}">{_escape(t)}</span>'
        for t in types
    )

    rows: list[str] = []
    for e in entities:
        n = len(e.get("briefs") or [])
        flag_badges = "".join(
            f'<span class="badge badge--low" title="Verification flag">{_escape(f)}</span>'
            for f in (e.get("flags") or [])
        )
        url = _entity_url(e, prefix=prefix)
        rows.append(
            '<li data-entity-type="' + _escape(e.get("type", "") or "") + '" '
            'data-entity-flags="' + _escape(",".join(e.get("flags") or [])) + '">'
            f'<span>'
            f'<a class="e-title" href="{url}">{_escape(e.get("title") or e["key"])}</a>'
            f'<div class="e-meta">'
            f'<span class="e-tag">{_escape(e.get("type", "") or "—")}</span>'
            f'<span class="mono">{_escape(e["key"])}</span>'
            f'<span>last covered {_escape(e.get("last_covered", "") or "—")}</span>'
            + (f'<span class="badge badge--accent" title="Story unfolds across {n} briefs">×{n} appearances</span>' if n > 1 else '')
            + flag_badges
            + '</div></span>'
            '</li>'
        )

    chart_block = render_overview_charts(entities, prefix=prefix, label="entities")
    list_html = (
        '<ul class="entity-list" data-filter-list="entities">' + "".join(rows) + '</ul>'
    ) if rows else '<div class="empty">No entities match.</div>'

    body = f"""
<h1>Entities</h1>
<p class="subtitle">{len(entities)} CVEs, actors, campaigns, incidents, tools, advisories, and reports tracked across briefs. The badge marks items covered in more than one brief — these are the "stories that unfolded".</p>

{chart_block}

<div class="toolbar" style="margin-top:1rem">
  <input class="input" id="entities-q" type="search" placeholder="Filter entities…" autocomplete="off" spellcheck="false" data-filter-input="entities" />
  <span class="chip active" data-filter-chip="entity-type" data-value="all">All types</span>
  {type_chips}
</div>

{list_html}
"""
    return base_template(
        title=f"Entities — {SITE_NAME}",
        description=f"{len(entities)} tracked entities across all briefs.",
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )



# === SOURCE + ENTITY ANNOTATION (v3) ===================================
#
# The entity universe = entities/registry.yaml (actors, campaigns,
# malware, tools, incidents, reports, trends, policy) + CVE entities
# (from entries' cves[] and state/cves_seen.json for historical ids).
# Appearances come from entries: an entry counts when its `entities`
# list carries the key, or its title/body mentions the entity's name or
# an alias (the v2 phrase-matching approach, ported to entry dicts).
# Timelines derive from entry dates; citations from entry sources; the
# old v2 coverage-log "delta timeline" is replaced by the update_of chain
# plus appearance dates.


def _source_prefix_index(sources_raw: dict[str, Any]) -> list[tuple[str, str, str]]:
    prefixes: list[tuple[str, str, str]] = []
    for s in sources_raw.get("sources", []):
        pfx = url_prefix_of(s.get("url") or "")
        host = host_of(s.get("url") or "")
        if pfx or host:
            prefixes.append((pfx, host, s["id"]))
    prefixes.sort(key=lambda t: (len(t[0]), len(t[1])), reverse=True)
    return prefixes


def _resolve_source_id(prefixes: list[tuple[str, str, str]],
                       host: str, prefix: str) -> str | None:
    for pfx, _h, sid in prefixes:
        if pfx and prefix.startswith(pfx):
            return sid
    for _p, h, sid in prefixes:
        if not h:
            continue
        if host == h or host.endswith("." + h):
            return sid
    return None


def _entry_link_records(entry: dict[str, Any]) -> list[dict[str, str]]:
    """Frontmatter sources + inline body links of one entry, deduped by
    URL (frontmatter wins — it carries the publisher label)."""
    seen: dict[str, dict[str, str]] = {}
    for s in entry.get("sources") or []:
        if not isinstance(s, dict):
            continue
        url = str(s.get("url") or "")
        if not url or url in seen:
            continue
        seen[url] = {
            "label": str(s.get("publisher") or url),
            "url": url,
            "host": host_of(url),
            "prefix": url_prefix_of(url),
        }
    for m in LINK_RE.finditer(entry.get("body") or ""):
        url = m.group(2).strip()
        if url in seen:
            continue
        seen[url] = {
            "label": m.group(1).strip(),
            "url": url,
            "host": host_of(url),
            "prefix": url_prefix_of(url),
        }
    return list(seen.values())


def annotate_sources(sources_raw: dict[str, Any],
                     entries: list[dict[str, Any]]) -> dict[str, Any]:
    """Attach per-source citation telemetry derived from entries:
    `appearances` (sorted dates, newest first — drives the list page and
    the cadence sparkline) and `entry_refs` ([{id, title, date}], newest
    first — drives the per-source page)."""
    prefixes = _source_prefix_index(sources_raw)
    dates: dict[str, set[str]] = defaultdict(set)
    refs: dict[str, dict[str, dict[str, str]]] = defaultdict(dict)
    for e in entries:
        for link in _entry_link_records(e):
            sid = _resolve_source_id(prefixes, link["host"], link["prefix"])
            if not sid:
                continue
            dates[sid].add(e["date"])
            refs[sid].setdefault(e["id"], {
                "id": e["id"],
                "title": e.get("title") or e["id"],
                "date": e["date"],
            })
    enriched = []
    for s in sources_raw.get("sources", []):
        entry_refs = sorted(refs.get(s["id"], {}).values(),
                            key=lambda r: (r["date"], r["id"]), reverse=True)
        enriched.append({
            **s,
            "appearances": sorted(dates.get(s["id"], set()), reverse=True),
            "entry_refs": entry_refs,
        })
    return {**sources_raw, "sources": enriched}


def _registry_phrases(ent: dict[str, Any]) -> list[str]:
    """Case-folded match phrases for a registry entity: name + aliases
    (min length 4 to avoid noise matches)."""
    phrases: list[str] = []
    for label in [ent.get("name")] + list(ent.get("aliases") or []):
        if isinstance(label, str):
            p = label.strip().lower()
            if len(p) >= 4 and p not in phrases:
                phrases.append(p)
    return phrases


def _entry_appearance(entry: dict[str, Any]) -> dict[str, Any]:
    skey = entry_section_key(entry) if (entry.get("horizon") or "operational") == "operational" \
        else weekly_section_key(entry)
    return {
        "date": entry["date"],
        "section": skey or "",
        "entry_id": entry["id"],
        "entry_title": entry.get("title") or entry["id"],
        "delta_summary": entry.get("headline") or "",
        # kept for _actor_timeline_strip compatibility
        "brief_path": entry.get("path") or "",
    }


def build_entities(
    registry: dict[str, dict[str, Any]],
    entries: list[dict[str, Any]],
    cves_seen_raw: dict[str, Any],
    sources_raw: dict[str, Any],
    day_pages: set[str],
) -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    """Returns `(entities, entries_by_entity_key)`.

    Every entity carries the unified render shape: key, type, title,
    summary, aliases, appearances[], briefs (linkable day dates),
    flags (non-multi-source verification values seen), citations[],
    weekly_buckets, section_distribution, source_distribution,
    external_refs (CVE only), first/last_covered (+ first/last_seen id
    aliases for CVEs), related_entities (filled by
    compute_related_entities)."""
    prefixes = _source_prefix_index(sources_raw)
    matched: dict[str, list[dict[str, Any]]] = defaultdict(list)

    # --- registry entities: explicit key + phrase matching -------------
    specs = []
    for key, ent in registry.items():
        specs.append((key, _registry_phrases(ent)))
    for e in entries:
        explicit = set(str(k) for k in (e.get("entities") or []))
        haystack = ((e.get("title") or "") + "\n" + (e.get("headline") or "")
                    + "\n" + (e.get("body") or "")).lower()
        for key, phrases in specs:
            if key in explicit or any(p in haystack for p in phrases):
                matched[key].append(e)

    # --- CVE entities ---------------------------------------------------
    cve_entries: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in entries:
        for cid in entry_cve_ids(e):
            cve_entries[cid].append(e)
    cves_seen_by_id: dict[str, dict[str, Any]] = {}
    for c in cves_seen_raw.get("cves", []) or []:
        if isinstance(c, dict) and c.get("id"):
            cves_seen_by_id[str(c["id"])] = c

    def _mk_common(key: str, ents: list[dict[str, Any]]) -> dict[str, Any]:
        apps = sorted((_entry_appearance(e) for e in ents),
                      key=lambda a: (a["date"], a["entry_id"]))
        flags = sorted({
            str(e.get("verification"))
            for e in ents
            if e.get("verification") and e.get("verification") != "multi-source"
        })
        cite_bucket: dict[str, dict[str, Any]] = {}
        for e in ents:
            for link in _entry_link_records(e):
                cur = cite_bucket.get(link["url"])
                if cur:
                    if e["id"] not in cur["entry_ids"]:
                        cur["entry_ids"].append(e["id"])
                    continue
                cite_bucket[link["url"]] = {
                    "label": link["label"],
                    "url": link["url"],
                    "host": link["host"],
                    "source_id": _resolve_source_id(prefixes, link["host"], link["prefix"]),
                    "entry_ids": [e["id"]],
                }
        citations = sorted(cite_bucket.values(), key=lambda c: (c.get("host") or "", c["url"]))
        wk_counts: dict[str, int] = {}
        sd: dict[str, int] = {}
        for a in apps:
            wk = _iso_week_of(a["date"])
            if wk:
                wk_counts[wk] = wk_counts.get(wk, 0) + 1
            if a["section"]:
                sd[a["section"]] = sd.get(a["section"], 0) + 1
        host_counts: dict[str, int] = {}
        for c in citations:
            h = (c.get("host") or "").strip()
            if h:
                host_counts[h] = host_counts.get(h, 0) + 1
        dates = [a["date"] for a in apps]
        return {
            "appearances": apps,
            "briefs": sorted({d for d in dates if d in day_pages}, reverse=True),
            "flags": flags,
            "citations": citations,
            "weekly_buckets": sorted(wk_counts.items()),
            "section_distribution": sd,
            "source_distribution": host_counts,
            "first_covered": dates[0] if dates else "",
            "last_covered": dates[-1] if dates else "",
            "related_entities": [],
            "external_refs": [],
        }

    entities: list[dict[str, Any]] = []
    for key, ent in registry.items():
        ents = matched.get(key, [])
        rec = _mk_common(key, ents)
        first_seen = str(ent.get("first_seen") or "")
        if first_seen and (not rec["first_covered"] or first_seen < rec["first_covered"]):
            rec["first_covered"] = first_seen
        entities.append({
            "key": key,
            "type": ent.get("type") or key.split(":", 1)[0],
            "title": ent.get("name") or key,
            "summary": ent.get("summary") or "",
            "aliases": list(ent.get("aliases") or []),
            "nexus": ent.get("nexus"),
            **rec,
        })

    all_cve_ids = set(cve_entries) | set(cves_seen_by_id)
    for cid in sorted(all_cve_ids):
        ents = cve_entries.get(cid, [])
        rec = _mk_common(cid, ents)
        seen = cves_seen_by_id.get(cid, {})
        first = rec["first_covered"] or str(seen.get("first_seen") or "")
        last = rec["last_covered"] or str(seen.get("last_seen") or "")
        if seen.get("first_seen") and str(seen["first_seen"]) < (first or "9999"):
            first = str(seen["first_seen"])
        if seen.get("last_seen") and str(seen["last_seen"]) > (last or ""):
            last = str(seen["last_seen"])
        rec["first_covered"], rec["last_covered"] = first, last
        rec["external_refs"] = [
            {"label": "NVD", "url": f"https://nvd.nist.gov/vuln/detail/{cid}"},
            {"label": "cve.org", "url": f"https://www.cve.org/CVERecord?id={cid}"},
            {"label": "CISA KEV", "url": cisa_kev_search_url(cid)},
        ]
        entities.append({
            "key": cid,
            "id": cid,
            "type": "cve",
            "title": (seen.get("title") or (ents[0].get("title") if ents else "") or cid),
            "summary": "",
            "aliases": [],
            "first_seen": first,
            "last_seen": last,
            "primary_source_url": seen.get("primary_source_url") or "",
            **rec,
        })
        matched[cid] = ents

    entities.sort(key=lambda e: e.get("last_covered", "") or "", reverse=True)
    return entities, dict(matched)


def compute_related_entities(
    entities: list[dict[str, Any]],
    entries_by_entity_key: dict[str, list[dict[str, Any]]],
) -> None:
    """Co-occurrence: two entities are related when they appear in the
    same entry; score = count of distinct shared entries, top 8."""
    entry_to_keys: dict[str, set[str]] = defaultdict(set)
    for k, ents in entries_by_entity_key.items():
        for e in ents:
            entry_to_keys[e["id"]].add(k)
    by_key = {e["key"]: e for e in entities}
    co: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for keys in entry_to_keys.values():
        klist = sorted(keys)
        for i, a in enumerate(klist):
            for b in klist[i + 1:]:
                co[a][b] += 1
                co[b][a] += 1
    for k, related_counts in co.items():
        ent = by_key.get(k)
        if not ent:
            continue
        rows = []
        for other_key, n in related_counts.items():
            other = by_key.get(other_key)
            if not other:
                continue
            rows.append({
                "key": other_key,
                "type": other.get("type") or "",
                "title": other.get("title") or other_key,
                "count": n,
            })
        rows.sort(key=lambda r: (-r["count"], r["title"].lower()))
        ent["related_entities"] = rows[:8]


# === ENTITY DETAIL PAGE (v3) ===========================================


def render_entity_page(
    entity: dict[str, Any],
    *,
    matching_entries: list[dict[str, Any]] | None = None,
    entries_by_id: dict[str, dict[str, Any]] | None = None,
    site_url: str,
    cachebust: str,
    prefix: str,
    canonical: str,
) -> str:
    """Single renderer for every entity type — CVE + every registry type
    (actor, campaign, malware, tool, incident, report, trend, policy).
    Same layout as v2: header pills → KPI tiles → coverage strip →
    story timeline (entry permalinks; the update_of chain lives on the
    entry pages) → charts → related entities → external refs + cited
    sources → embedded matching entries."""
    etype = (entity.get("type") or "").lower()
    title = entity.get("title") or entity.get("key") or "Untitled"
    key = entity.get("key") or ""
    apps = sorted(entity.get("appearances", []) or [],
                  key=lambda a: (a.get("date") or "", a.get("entry_id") or ""),
                  reverse=True)
    citations = entity.get("citations", []) or []

    # --- Story timeline (entry permalinks) ----------------------------
    timeline_lis: list[str] = []
    for a in apps:
        eid = a.get("entry_id") or ""
        e_title = a.get("entry_title") or eid or "?"
        section = a.get("section") or ""
        delta = a.get("delta_summary") or ""
        link = f'{prefix}entries/{_escape(eid)}/' if eid else "#"
        timeline_lis.append(
            "<li><span>"
            f'<span class="mono" style="margin-right:0.6rem">{_escape(a.get("date", "") or "")}</span>'
            f'<a href="{link}">{_escape(e_title)}</a>'
            '<div class="e-meta" style="margin-top:0.2rem">'
            + (f'<span class="e-tag">{_escape(section)}</span>' if section else "")
            + (f'<span class="muted">{_escape(delta)}</span>' if delta else "")
            + "</div></span></li>"
        )
    timeline_block = (
        f'<ol class="entity-list" style="list-style:none">{"".join(timeline_lis)}</ol>'
    ) if timeline_lis else '<p class="muted">No published entries reference this entity yet.</p>'

    # --- KPI tiles + sparkline ----------------------------------------
    sparkline_buckets = _fill_weekly_timeline(entity.get("weekly_buckets", []) or [])
    spark_values = [float(c) for _, c in sparkline_buckets]
    spark_html = _ops_svg_sparkline(
        spark_values, label=f"Weekly mention count for {title}", width=240, height=42,
    ) if spark_values else '<div class="ops-spark ops-spark--empty">no data</div>'
    sd = entity.get("section_distribution", {}) or {}
    src_dist = entity.get("source_distribution", {}) or {}
    hosts = {c.get("host") for c in citations if c.get("host")}

    kpi_html = (
        '<div class="ops-kpi-grid">'
        + _ops_kpi_tile(
            "Coverage timeline",
            str(len(apps)),
            sub=f"first {entity.get('first_covered', '—') or '—'} → last {entity.get('last_covered', '—') or '—'}",
            kind="accent",
            chart=spark_html,
        )
        + _ops_kpi_tile(
            "Entries",
            str(len(apps)),
            sub=f"{len({a.get('date') for a in apps})} distinct days",
            kind="neutral",
        )
        + _ops_kpi_tile(
            "Sources cited",
            str(len(citations)),
            sub=f"{len(hosts)} hosts",
            kind="neutral",
        )
        + _ops_kpi_tile(
            "Sections touched",
            str(len(sd)),
            sub=", ".join(sorted(sd.keys())[:3]) or "—",
            kind="neutral",
        )
        + _ops_kpi_tile(
            "Co-occurring entities",
            str(len(entity.get("related_entities", []) or [])),
            sub="see Related entities below" if entity.get("related_entities") else "no co-occurrence",
            kind="neutral",
        )
        + "</div>"
    )

    # --- Section distribution bars ------------------------------------
    section_block = ""
    if sd:
        items_sorted = sorted(sd.items(), key=lambda kv: -kv[1])
        bar_svg = _ops_svg_bars([float(v) for _, v in items_sorted], width=320, height=80,
                                 label="Section distribution")
        legend_lis = "".join(
            f'<li class="ops-legend__item">'
            f'<span class="ops-legend__swatch" style="background:var(--accent-soft)"></span>'
            f'<span class="ops-legend__label">{_escape(k or "—")}</span>'
            f'<span class="ops-legend__value mono">{v}</span></li>'
            for k, v in items_sorted
        )
        section_block = (
            '<div class="ops-section">'
            '<h3 class="section-head">Where this entity is cited</h3>'
            '<div class="ops-charts-row">'
            f'<div class="ops-chart-card">{bar_svg}'
            f'<ul class="ops-legend">{legend_lis}</ul>'
            "</div></div></div>"
        )

    # --- Source distribution donut --------------------------------------
    donut_block = ""
    if src_dist:
        items_sorted = sorted(src_dist.items(), key=lambda kv: -kv[1])
        head, tail = items_sorted[:8], items_sorted[8:]
        if tail:
            head.append(("other", sum(v for _, v in tail)))
        assigned: dict[str, str] = {}
        slices = [(k, float(v), _entity_palette_color(k, assigned)) for k, v in head]
        donut_html = _ops_svg_donut(slices, size=140, label="Source distribution")
        donut_block = (
            '<div class="ops-section">'
            '<h3 class="section-head">Source distribution</h3>'
            f'<div class="ops-chart-card">{donut_html}</div>'
            "</div>"
        )

    # --- Related entities ------------------------------------------------
    related = entity.get("related_entities", []) or []
    related_block = ""
    if related:
        rows: list[str] = []
        for r in related:
            other_url = f'{prefix}entities/{urllib.parse.quote(r["key"], safe="")}/'
            rows.append(
                "<li>"
                f'<span><a class="e-title" href="{other_url}">{_escape(r["title"])}</a>'
                f'<div class="e-meta"><span class="e-tag">{_escape(r.get("type") or "—")}</span>'
                f'<span class="mono">{_escape(r["key"])}</span>'
                f'<span class="badge badge--low" title="Number of entries where both entities co-appear">×{r["count"]}</span></div>'
                "</span></li>"
            )
        related_block = (
            '<h2 class="section-head" style="margin-top:1.5rem">Related entities</h2>'
            f'<ul class="entity-list">{"".join(rows)}</ul>'
        )

    # --- Cited sources ---------------------------------------------------
    primary_host = host_of(entity.get("primary_source_url", "") or "")
    cite_items: list[str] = []
    for c in sorted(citations, key=lambda c: ((c.get("host") or "") != primary_host,
                                              c.get("host") or "", c.get("url") or "")):
        h = c.get("host") or ""
        is_primary = bool(primary_host) and h == primary_host
        source_id = c.get("source_id")
        cite_url = _safe_url(c.get("url", ""))
        eids = c.get("entry_ids") or []
        entry_links = ", ".join(
            f'<a href="{prefix}entries/{_escape(eid)}/" class="mono">{_escape(eid.split("/", 1)[0])}</a>'
            for eid in sorted(set(eids), reverse=True)[:6]
        )
        cite_items.append(
            '<li class="cite">'
            f'<a class="cite-link" href="{_escape(cite_url)}" target="_blank" rel="noopener noreferrer">'
            f'<span class="cite-host">{_escape(h)}</span>'
            + ('<span class="badge badge--accent" title="Primary source recorded by the agent">primary</span>' if is_primary else "")
            + f'<span class="cite-label">{_escape(c.get("label") or c.get("url", ""))}</span>'
            f'<span class="cite-url muted">{_escape(c.get("url", ""))}</span>'
            "</a>"
            '<div class="cite-meta muted">'
            + (f'<a href="{prefix}sources/{urllib.parse.quote(source_id, safe="")}/">source profile</a> · ' if source_id else "")
            + "cited in " + (entry_links or '<span class="muted">—</span>')
            + "</div></li>"
        )
    citations_block = ""
    if cite_items:
        citations_block = (
            f'<h2 class="section-head" style="margin-top:1.5rem">All cited sources ({len(citations)})</h2>'
            f'<ul class="cite-list">{"".join(cite_items)}</ul>'
        )

    # --- External references (CVE only) --------------------------------
    ext_block = ""
    if entity.get("external_refs"):
        ext_links = " · ".join(
            f'<a href="{_escape(_safe_url(r["url"]))}" target="_blank" rel="noopener noreferrer">{_escape(r["label"])}</a>'
            for r in entity["external_refs"]
        )
        ext_block = (
            '<h3 style="margin-top:1.2rem">External references</h3>'
            f"<p>{ext_links}</p>"
        )

    # --- Header ----------------------------------------------------------
    flag_badges = "".join(
        f'<span class="badge badge--low" title="Verification status seen on referencing entries">{_escape(f)}</span>'
        for f in (entity.get("flags") or [])
    )
    alias_html = ""
    if entity.get("aliases"):
        alias_html = (
            '<p class="muted">Aliases: '
            + ", ".join(_escape(a) for a in entity["aliases"])
            + "</p>"
        )
    summary_html = (
        f'<p class="subtitle" style="max-width:60rem">{_escape(entity["summary"])}</p>'
        if entity.get("summary") else ""
    )

    actor_timeline_html = _actor_timeline_strip(entity)

    body = f"""
<h1{' class="mono"' if etype == 'cve' else ''}>{_escape(title)}</h1>
<p class="subtitle">
  <span class="badge badge--accent">{_escape(etype or "entity")}</span>
  · <span class="mono">{_escape(key)}</span>
  {flag_badges}
</p>
{summary_html}
{alias_html}

{kpi_html}

{actor_timeline_html}

<h2 class="section-head" style="margin-top:1.5rem">Story timeline</h2>
{timeline_block}

{section_block}
{donut_block}
{related_block}

<div class="panel" style="margin-top:1.5rem">
  {ext_block}
  {citations_block}
</div>

{render_embedded_entries_section(
    matching_entries or [],
    heading=f"Entries about {title}",
    empty_text=(
        "No published entry references this entity yet — entries match by "
        "registry key, by the entity's name or a public alias appearing in "
        "the entry title or body, or (for CVE entities) by exact CVE id."
    ),
    prefix=prefix,
    entries_by_id=entries_by_id,
)}
"""
    return base_template(
        title=f"{title} — {etype or 'entity'}",
        description=(entity.get("summary") or title)[:280],
        body=body,
        canonical=canonical,
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=prefix,
    )


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

    # Downstream branding assets (logos, favicon, fonts, custom.css) from
    # site/branding/ → _site/branding/. Docs stay out of the output.
    bsrc = BRANDING_ASSETS_DIR
    if bsrc.exists():
        for src_path in bsrc.rglob("*"):
            if not src_path.is_file() or src_path.suffix == ".md":
                continue
            size = src_path.stat().st_size
            if size > MAX_VENDOR_BYTES:
                raise RuntimeError(
                    f"refused: branding asset {src_path} is {size} bytes, "
                    f"exceeds cap of {MAX_VENDOR_BYTES}"
                )
            atomic_write_bytes(
                OUT / "branding" / src_path.relative_to(bsrc),
                src_path.read_bytes(),
            )


def cachebust_value() -> str:
    """A short content-hashed fingerprint over the JS + CSS assets +
    taxonomy + branding overrides. Deterministic across runs with the
    same inputs; identical to the pre-branding fingerprint while no
    branding override exists (empty theme, no site/branding/ assets)."""
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
    if BRANDING_CSS:
        h.update(b"\x00branding.css\x00")
        h.update(BRANDING_CSS.encode("utf-8"))
    if BRANDING_ASSETS_DIR.exists():
        for p in sorted(BRANDING_ASSETS_DIR.rglob("*")):
            if p.is_file() and p.suffix != ".md":
                h.update(p.relative_to(SITE).as_posix().encode("utf-8"))
                h.update(b"\x00")
                h.update(p.read_bytes())
                h.update(b"\x00")
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


def write_security_txt(out_path: Path, *, repo: str, expires: str, site_url: str) -> None:
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
        f"Canonical: {site_url}.well-known/security.txt\n"
    )
    atomic_write_text(out_path, body)



# === SELF-CHECK =========================================================

def self_check(
    *,
    manifest: dict[str, Any],
    feed_files: list[Path],
    site_url: str,
) -> tuple[list[str], list[str]]:
    """Run the post-build self-check.

    Returns ``(errors, warnings)``. Errors block the build (exit 4) —
    they're truly broken-site signals: missing manifest page, inline
    <script> (CSP-fatal), Markdown-renderer placeholder leakage (the
    renderer's fixed-point regressed), XML parse error in a feed,
    secret-shaped token leaked into output. Warnings are cosmetic /
    quality signals — Umami snippet count mismatch on a non-redirect
    page, raw `**Markdown**` or `[..](http..)` surviving into RSS
    `<content:encoded>`, UTM parameters in URLs. They get printed but
    do not abort the build, because the deploy-site workflow blocking
    on a cosmetic regression has historically caused outages — see
    the 2026-05-10 incident where the build failed on a sub-agent's
    verbatim `**Model:**` self-id string inside a `<code>` block."""
    errors: list[str] = []
    warnings: list[str] = []
    # Every page in the manifest exists on disk.
    for url_path, info in manifest.get("pages", {}).items():
        path = OUT / info["path"]
        if not path.exists():
            errors.append(f"manifest page missing on disk: {url_path} -> {info['path']}")
    # Every emitted HTML file contains the Umami snippet exactly once and
    # carries no inline `<script>` block (CSP `script-src 'self'` would
    # refuse to execute it).
    inline_script_re = re.compile(r"<script(?:\s[^>]*)?>(?!\s*</script>)[^<]", re.IGNORECASE)
    # Non-executable JSON data islands (<script type="application/json">,
    # used by /brief/ to hand grouping constants to brief.js) are exempt:
    # browsers never execute them and CSP script-src does not apply. Strip
    # them before scanning so only genuinely executable inline bodies flag.
    data_island_re = re.compile(
        r'<script\s[^>]*type=(?:"|\')application/(?:ld\+)?json(?:"|\')[^>]*>.*?</script>',
        re.IGNORECASE | re.DOTALL,
    )
    # Match the actual `<script>` tag that loads Umami, not stray textual
    # mentions of the URL (which can appear in docs that describe the
    # analytics setup). Host comes from config/branding.yaml; with
    # analytics off, every page must carry ZERO analytics tags.
    expected_umami_count = 1 if ANALYTICS_ENABLED else 0
    umami_script_host = UMAMI_SCRIPT_HOST or "https://cloud.umami.is"
    umami_tag_re = re.compile(
        r'<script[^>]*\bsrc=(?:"|&quot;)' + re.escape(umami_script_host) + r'/script\.js',
        re.IGNORECASE,
    )
    # Pages with a `meta http-equiv="refresh"` redirect are intentionally
    # minimal stubs (e.g. /cves/<id>/ → /entities/<key>/ back-compat
    # redirects). Skip them — they're noindex'd, don't load the navbar,
    # and don't load Umami because the visit is forwarded immediately.
    redirect_re = re.compile(r'<meta\s+http-equiv=["\']refresh["\']', re.IGNORECASE)
    umami_warnings: list[str] = []
    for path in OUT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        if redirect_re.search(text):
            continue
        umami_count = len(umami_tag_re.findall(text))
        if umami_count != expected_umami_count:
            # Cosmetic — analytics may not load on this page, but the
            # page itself is fine. Aggregate so one umami misconfig
            # doesn't produce 100 lines of warnings.
            umami_warnings.append(str(path.relative_to(OUT)))
        if inline_script_re.search(data_island_re.sub("", text)):
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
    if umami_warnings:
        if len(umami_warnings) == 1:
            warnings.append(
                f"umami <script> tag count != {expected_umami_count} in {umami_warnings[0]}"
            )
        else:
            warnings.append(
                f"umami <script> tag count != {expected_umami_count} in {len(umami_warnings)} pages "
                f"(first: {umami_warnings[0]}) — analytics misconfig, page content unaffected"
            )
    # No raw `**Markdown**` survives in any RSS content. Cosmetic — feed
    # readers still parse and display the content; the regression is
    # editorial drift the maintainer should know about, not a delivery
    # failure that justifies blocking the deploy.
    for fp in feed_files:
        text = fp.read_text(encoding="utf-8")
        if not text:
            continue
        # Strip all CDATA payload comparisons: only inspect content:encoded
        # bodies.
        for m in re.finditer(r"<content:encoded><!\[CDATA\[(.+?)\]\]></content:encoded>", text, re.DOTALL):
            payload = m.group(1)
            # `**...**` and `[..](http..)` inside <code>/<pre> are literal text
            # correctly rendered from backtick-quoted markdown — not unrendered
            # emphasis/link tokens. Strip those spans before scanning so the
            # check only flags genuinely-leaked markdown (e.g. an item body
            # discussing a sub-agent's verbatim `**Model:**` self-id string is
            # rendered as <code>**Model:**</code> and must not false-positive).
            scrub = re.sub(r"<code\b[^>]*>.*?</code>", "", payload, flags=re.DOTALL)
            scrub = re.sub(r"<pre\b[^>]*>.*?</pre>", "", scrub, flags=re.DOTALL)
            # Markdown emphasis tokens that should have rendered to HTML
            if re.search(r"\*\*[^\n*]{1,80}\*\*", scrub):
                warnings.append(f"feed {fp.name}: unrendered Markdown `**...**` in content:encoded")
                break
            if re.search(r"\[[^\]\n]{1,80}\]\((https?://)", scrub):
                warnings.append(f"feed {fp.name}: unrendered Markdown `[..](http..)` in content:encoded")
                break
    # All three feeds parse as valid XML — CRITICAL (broken feed = broken
    # delivery, not cosmetic).
    for fp in feed_files:
        if fp.exists():
            errs = _xml_validate(fp.read_text(encoding="utf-8"))
            for e in errs:
                errors.append(f"feed {fp.name}: XML parse error — {e}")
    # No UTM parameters in any URL on the site. Cosmetic / privacy-tracking
    # hygiene; not a delivery failure.
    utm_re = re.compile(r"[?&]utm_[a-z_]+=", re.IGNORECASE)
    utm_pages: list[str] = []
    for path in list(OUT.rglob("*.html")) + list(OUT.rglob("*.xml")):
        text = path.read_text(encoding="utf-8")
        if utm_re.search(text):
            utm_pages.append(str(path.relative_to(OUT)))
    if utm_pages:
        if len(utm_pages) == 1:
            warnings.append(f"UTM parameter present in URL inside {utm_pages[0]}")
        else:
            warnings.append(
                f"UTM parameter present in URL inside {len(utm_pages)} pages "
                f"(first: {utm_pages[0]}) — strip and reissue"
            )

    # No known-shape secret tokens in any emitted file. CRITICAL — failing
    # the build is always preferable to silently propagating a secret to
    # gh-pages and the RSS feeds.
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
    return errors, warnings


# === MAIN ==============================================================

def main() -> int:
    verify_vendored_hashes()
    taxonomy = parse_taxonomy(SITE / "taxonomy.yaml")

    site_url = os.environ.get("SITE_URL", DEFAULT_SITE_URL).rstrip("/") + "/"

    OUT.mkdir(exist_ok=True)
    tmp_dir = OUT / ".tmp"
    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)

    copy_assets()
    cachebust = cachebust_value()
    atomic_write_bytes(OUT / ".nojekyll", b"")
    if BRANDING_CSS:
        atomic_write_text(OUT / "assets" / "css" / "branding.css", BRANDING_CSS)

    # ---- Content-tree size guard --------------------------------------
    total_content = 0
    for tree in (ROOT / "entries", ROOT / "runs"):
        if tree.exists():
            total_content += sum(p.stat().st_size for p in tree.rglob("*") if p.is_file())
    if total_content > MAX_ENTRIES_DIR_BYTES:
        print(
            f"error: entries/ + runs/ trees are {total_content} bytes, "
            f"exceeds cap of {MAX_ENTRIES_DIR_BYTES}",
            file=sys.stderr,
        )
        return 5

    # ---- Load the v3 content model ------------------------------------
    try:
        entries = collect_entries()
        registry = load_registry()
        runs = collect_runs()
    except content_model.YamlSubsetError as exc:
        print(f"CONTENT PARSE FAILED: {exc}", file=sys.stderr)
        return 3

    # ---- Fail-loud schema validation (entries + registry) -------------
    fatal_errors: list[str] = list(validate_registry(registry))
    registry_keys = set(registry)
    for e in entries:
        fatal_errors.extend(validate_entry(e, taxonomy, registry_keys=registry_keys))
        if not is_safe_path_segment(e.get("date") or "") or not is_safe_path_segment(e.get("slug") or ""):
            fatal_errors.append(f"{e.get('id')}: unsafe path segment in date/slug")
    if fatal_errors:
        print("CONTENT VALIDATION FAILED:", file=sys.stderr)
        for err in fatal_errors:
            print(f"  · {err}", file=sys.stderr)
        return 3

    # ---- Supporting state ----------------------------------------------
    cves_raw = {"cves": []}
    if (ROOT / "state" / "cves_seen.json").exists():
        cves_raw = json.loads(
            _read_text_capped(ROOT / "state" / "cves_seen.json", MAX_STATE_BYTES)
        )
    sources_raw = json.loads(
        _read_text_capped(ROOT / "sources" / "sources.json", MAX_STATE_BYTES)
    )
    source_health = None
    sh_src = ROOT / "state" / "source_health.json"
    if sh_src.exists():
        try:
            source_health = json.loads(_read_text_capped(sh_src, MAX_STATE_BYTES))
        except Exception:
            source_health = None

    # ---- Derived indexes -------------------------------------------------
    entries_by_id = {e["id"]: e for e in entries}
    updated_by = build_update_chains(entries)
    days = entries_by_day(entries)
    weeks = entries_by_week(entries)
    day_pages = set(days)
    ref = reference_ts(entries, runs)
    runs_by_id = {str(r.get("run_id")): r for r in runs if r.get("run_id")}
    entries_by_run: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in entries:
        rid = str(e.get("run_id") or "")
        if rid:
            entries_by_run[rid].append(e)
    runs_by_day: dict[str, list[dict[str, Any]]] = defaultdict(list)
    runs_by_week: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in runs:
        rdate = str(r.get("date") or "")
        if not DATE_RE.match(rdate):
            continue
        if r.get("kind") == "weekly":
            try:
                y, m, d = (int(x) for x in rdate.split("-"))
                iso = date(y, m, d).isocalendar()
                runs_by_week[f"{iso[0]:04d}-W{iso[1]:02d}"].append(r)
            except ValueError:
                pass
        else:
            runs_by_day[rdate].append(r)
    for bucket in (runs_by_day, runs_by_week):
        for k in bucket:
            bucket[k].sort(key=lambda r: str(r.get("started") or ""), reverse=True)

    sources = annotate_sources(sources_raw, entries)
    entities_list, entries_by_entity_key = build_entities(
        registry, entries, cves_raw, sources_raw, day_pages
    )
    compute_related_entities(entities_list, entries_by_entity_key)
    cves_list = [e for e in entities_list if e.get("type") == "cve"]
    topics_list = [e for e in entities_list if e.get("type") != "cve"]

    manifest_pages: dict[str, dict[str, Any]] = {}
    sitemap: list[tuple[str, str]] = []

    def emit_html(rel_url: str, html: str, *, lastmod: str = "") -> None:
        """`rel_url` looks like 'briefs/2026-07-03/' or '' for home. The
        path on disk becomes `<rel_url>index.html`, with percent-encoded
        characters decoded back to literal form (GitHub Pages decodes
        `%3A` → `:` before file lookup)."""
        rel_path = rel_url + "index.html" if rel_url.endswith("/") or rel_url == "" else rel_url
        if rel_url == "":
            rel_path = "index.html"
        fs_path = urllib.parse.unquote(rel_path)
        out_path = OUT / fs_path
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
        except Exception as exc:  # noqa: BLE001
            raise RuntimeError(f"refused: cannot resolve {rel_url!r}: {exc}")
        atomic_write_text(out_path, html)
        h = hashlib.sha256(html.encode("utf-8")).hexdigest()
        manifest_pages[rel_url or "/"] = {"path": fs_path, "hash": h}
        sitemap.append((site_url + rel_url, lastmod))

    # ---- /brief/ — the dynamic window brief + briefbook ----------------
    card_html_by_id: dict[str, str] = {}
    briefbook = build_briefbook(
        entries, runs, ref_ts=ref, prefix="../", card_html_by_id=card_html_by_id
    )
    window_since = ref - timedelta(hours=DEFAULT_WINDOW_HOURS)
    window_entries = content_model.entries_in_window(entries, window_since, None)
    window_runs = runs_in_window(runs, window_since, None)
    emit_html(
        "brief/",
        render_live_brief_page(
            window_entries, window_runs,
            all_entries=entries, all_runs=runs,
            ref_ts=ref,
            entries_by_id=entries_by_id,
            card_html_by_id=card_html_by_id,
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "brief/",
        ),
        lastmod=ref.strftime("%Y-%m-%d"),
    )

    # ---- Day pages + index ---------------------------------------------
    for day, day_entries in days.items():
        rel_url = f"briefs/{day}/"
        emit_html(
            rel_url,
            render_day_page(
                day, day_entries, runs_by_day.get(day, []),
                entries_by_id=entries_by_id,
                site_url=site_url,
                cachebust=cachebust,
                prefix="../../",
                canonical=site_url + rel_url,
            ),
            lastmod=day,
        )
    emit_html(
        "briefs/",
        render_days_index_page(
            days,
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "briefs/",
        ),
        lastmod=max(days) if days else "",
    )

    # ---- Weekly pages + index + legacy redirects ------------------------
    for week, week_entries in weeks.items():
        if not is_safe_path_segment(week):
            continue
        rel_url = f"weekly/{week}/"
        emit_html(
            rel_url,
            render_weekly_page(
                week, week_entries, runs_by_week.get(week, []),
                entries_by_id=entries_by_id,
                site_url=site_url,
                cachebust=cachebust,
                prefix="../../",
                canonical=site_url + rel_url,
            ),
            lastmod=max(e["date"] for e in week_entries),
        )
        # Legacy URL shape /briefs/weekly/YYYY-Www/ → /weekly/YYYY-Www/.
        emit_html(
            f"briefs/weekly/{week}/",
            render_redirect_page(
                target_url=f"/{rel_url}",
                title=f"{week} — moved",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )
    emit_html(
        "weekly/",
        render_weekly_index_page(
            weeks,
            site_url=site_url,
            cachebust=cachebust,
            prefix="../",
            canonical=site_url + "weekly/",
        ),
        lastmod=max(weeks) if weeks else "",
    )
    emit_html(
        "briefs/weekly/",
        render_redirect_page(
            target_url="/weekly/",
            title="Weekly summaries — moved",
            site_url=site_url,
            cachebust=cachebust,
        ),
    )


    # ---- Per-entry permalinks + tag/region indexes ----------------------
    tag_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    region_index: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in entries:
        rel_url = entry_url_path(e)
        emit_html(
            rel_url,
            render_entry_page(
                e,
                entries_by_id=entries_by_id,
                updated_by=updated_by,
                registry=registry,
                runs_by_id=runs_by_id,
                day_pages=day_pages,
                site_url=site_url,
                cachebust=cachebust,
                prefix="../../../",
                canonical=site_url + rel_url,
            ),
            lastmod=e["date"],
        )
        for t in e.get("tags") or []:
            tag_index[t].append(e)
        for r in e.get("regions") or []:
            region_index[r].append(e)

    def tag_or_region_page(facet: str, value: str, bucket: list[dict[str, Any]]) -> str:
        rel_url = f"{facet}/{value}/"
        prefix = "../" * 2
        ordered = sorted(bucket, key=lambda e: (str(e.get("discovered_at") or ""), e["id"]),
                         reverse=True)
        items = [
            (
                e.get("title") or e["id"],
                f"{prefix}{entry_url_path(e)}",
                f"{e['date']} · {e.get('kind') or ''} · {e.get('priority') or ''}",
            )
            for e in ordered
        ]
        return render_index_page(
            title=f"{facet[:-1].capitalize()}: {value}",
            intro=f"All entries tagged {value}.",
            items=items,
            site_url=site_url,
            cachebust=cachebust,
            prefix=prefix,
            canonical=site_url + rel_url,
            description=f"CTI entries tagged {value}.",
        )

    for tag, bucket in tag_index.items():
        if not is_safe_path_segment(tag):
            print(f"warning: skipping tag index with unsafe tag {tag!r}", file=sys.stderr)
            continue
        emit_html(f"tags/{tag}/", tag_or_region_page("tags", tag, bucket))
    for region, bucket in region_index.items():
        if not is_safe_path_segment(region):
            print(f"warning: skipping region index with unsafe region {region!r}", file=sys.stderr)
            continue
        emit_html(f"regions/{region}/", tag_or_region_page("regions", region, bucket))

    # ---- Entity pages + legacy redirects ---------------------------------
    for ent in entities_list:
        ekey = ent.get("key", "") or ""
        if not is_safe_path_segment(ekey):
            print(f"warning: skipping entity with unsafe key {ekey!r}", file=sys.stderr)
            continue
        rel_url = f"entities/{urllib.parse.quote(ekey, safe='')}/"
        emit_html(
            rel_url,
            render_entity_page(
                ent,
                matching_entries=entries_by_entity_key.get(ekey, []),
                entries_by_id=entries_by_id,
                site_url=site_url,
                cachebust=cachebust,
                prefix="../../",
                canonical=site_url + rel_url,
            ),
            lastmod=(ent.get("last_covered") or "")[:10],
        )
        if ent.get("type") == "cve" and CVE_RE.fullmatch(ekey):
            stub_rel = f"cves/{ekey}/"
        else:
            stub_rel = f"topics/{urllib.parse.quote(ekey, safe='')}/"
        emit_html(
            stub_rel,
            render_redirect_page(
                target_url=f"/{rel_url}",
                title=f"{ekey} — moved",
                site_url=site_url,
                cachebust=cachebust,
            ),
            lastmod=(ent.get("last_covered") or "")[:10],
        )

    # ---- Source pages ------------------------------------------------------
    for s in sources["sources"]:
        if not is_safe_path_segment(s.get("id", "") or ""):
            print(f"warning: skipping source entry with unsafe id {s.get('id')!r}", file=sys.stderr)
            continue
        rel_url = f"sources/{urllib.parse.quote(s['id'], safe='')}/"
        emit_html(
            rel_url,
            render_source_page(
                s,
                site_url=site_url,
                cachebust=cachebust,
                prefix="../../",
                canonical=site_url + rel_url,
            ),
            lastmod=(s.get("last_successful_fetch") or "")[:10],
        )

    # ---- List pages -----------------------------------------------------
    emit_html(
        "entities/",
        render_entities_index_page(
            entities_list, site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "entities/",
        ),
    )
    emit_html(
        "cves/",
        render_cve_list_page(
            cves_list, site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "cves/",
        ),
    )
    emit_html(
        "topics/",
        render_topic_list_page(
            topics_list, site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "topics/",
        ),
    )
    emit_html(
        "sources/",
        render_source_list_page(
            sources["sources"], site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "sources/",
        ),
    )

    # ---- Home -------------------------------------------------------------
    # "today" = the newest day with entries (the live, still-appended day);
    # "prev_day" = the most recent completed day before it.
    day_keys = sorted(days.keys(), reverse=True)
    today = day_keys[0] if day_keys else None
    prev_day = day_keys[1] if len(day_keys) > 1 else None
    latest_week = max(weeks) if weeks else None
    recent_entries = sorted(
        entries, key=lambda e: (str(e.get("discovered_at") or ""), e["id"]), reverse=True
    )
    counts = {
        "entries": len(entries),
        "days": len(days),
        "weeklies": len(weeks),
        "entities": len(entities_list),
        "cves": len(cves_list),
        "sources": len(sources["sources"]),
    }
    emit_html(
        "",
        render_home_page(
            today=today,
            today_entries=days.get(today, []) if today else [],
            prev_day=prev_day,
            prev_day_entries=days.get(prev_day, []) if prev_day else [],
            latest_week=latest_week,
            latest_week_entries=weeks.get(latest_week, []) if latest_week else [],
            site_url=site_url,
            cachebust=cachebust,
            canonical=site_url,
        ),
        lastmod=ref.strftime("%Y-%m-%d"),
    )

    # ---- /about/** static docs ------------------------------------------
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
    about_landing_md += "System reference for operators, contributors, and curious readers. The pipeline data model, end-to-end map, runbook, privacy disclosure, open backlog.\n\n"
    for p in docs_files:
        title = p.stem.replace("-", " ").capitalize()
        about_landing_md += f"- [{title}](docs/{p.stem}.md)\n"
    about_landing_md += "\n## [Prompts](prompts/)\n\n"
    about_landing_md += "Everything the pipeline loads at runtime — the run prompts, the verification policy, the entry template, the check-run fix recipes, and the version-history changelog.\n\n"
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
            title=f"About — {SITE_NAME}",
            description="What this project is, how the entries are produced, and how to read them.",
            prefix="../",
            canonical=site_url + "about/",
            site_url=site_url,
            cachebust=cachebust,
        ),
    )
    if docs_files:
        docs_index_md = "# Documentation\n\nSystem reference for operators, contributors, and curious readers. Pure docs — none of the files here are loaded by the prompt at runtime (that material lives under [`prompts/`](../prompts/)).\n\n"
        for p in docs_files:
            title = p.stem.replace("-", " ").capitalize()
            docs_index_md += f"- [**{title}**](../docs/{p.stem}.md)\n"
        emit_html(
            "about/docs/",
            render_static_doc(
                md_text=docs_index_md,
                title=f"Documentation — {SITE_NAME}",
                description="System reference: pipeline model, architecture, operating, customization.",
                prefix="../../",
                canonical=site_url + "about/docs/",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )
        for p in docs_files:
            rel_url = f"about/docs/{p.stem}/"
            title = p.stem.replace("-", " ").capitalize()
            emit_html(
                rel_url,
                render_static_doc(
                    md_text=_read_text_capped(p, MAX_BRIEF_BYTES),
                    title=f"{title} — {SITE_NAME}",
                    description=f"{title} — system documentation.",
                    prefix="../../../",
                    canonical=site_url + rel_url,
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )


    changelog_path = ROOT / "prompts" / "CHANGELOG.md"
    if prompt_files or changelog_path.exists():
        prompts_index_md = "# Prompts\n\nEverything the pipeline loads at runtime. The run prompts drive every fire; the supporting files (verification policy, entry template, check-run fix recipes) are read by the prompts at runtime.\n\n"
        if prompt_files:
            prompts_index_md += "## Prompts and runtime policies\n\n"
            for p in prompt_files:
                title = p.stem.replace("-", " ").capitalize()
                prompts_index_md += f"- [**{title}**](../prompts/{p.stem}.md)\n"
            prompts_index_md += "\n"
        prompts_index_md += "## Version history\n\n"
        prompts_index_md += "Every substantive prompt edit ships with a [CHANGELOG](../prompts/CHANGELOG.md) entry explaining *why* the editorial policy shifted. Recent versions:\n\n"
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
                title=f"Prompts — {SITE_NAME}",
                description="The prompts the pipeline loads at runtime, plus their version-history changelog.",
                prefix="../../",
                canonical=site_url + "about/prompts/",
                site_url=site_url,
                cachebust=cachebust,
            ),
        )
        for p in prompt_files:
            rel_url = f"about/prompts/{p.stem}/"
            title = p.stem.replace("-", " ").capitalize()
            emit_html(
                rel_url,
                render_static_doc(
                    md_text=_read_text_capped(p, MAX_BRIEF_BYTES),
                    title=f"{title} — {SITE_NAME}",
                    description=f"{title} — runtime prompt / policy.",
                    prefix="../../../",
                    canonical=site_url + rel_url,
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )
        if changelog_path.exists():
            emit_html(
                "about/prompts/changelog/",
                render_static_doc(
                    md_text=_read_text_capped(changelog_path, MAX_BRIEF_BYTES),
                    title=f"Prompt CHANGELOG — {SITE_NAME}",
                    description="Editorial-policy audit trail — every prompt-version change explained.",
                    prefix="../../../",
                    canonical=site_url + "about/prompts/changelog/",
                    site_url=site_url,
                    cachebust=cachebust,
                ),
            )

    # ---- /ops/ + /trends/ + /feeds/ ---------------------------------------
    emit_html(
        "ops/",
        render_ops_page(
            runs,
            sources["sources"],
            prefix="../",
            site_url=site_url,
            cachebust=cachebust,
            canonical=site_url + "ops/",
            source_health=source_health,
            day_pages=day_pages,
            entries_by_run=entries_by_run,
        ),
    )
    emit_html(
        "trends/",
        render_trends_page(
            entries, site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "trends/",
        ),
        lastmod=ref.strftime("%Y-%m-%d"),
    )
    emit_html(
        "feeds/",
        render_feeds_page(
            site_url=site_url, cachebust=cachebust,
            prefix="../", canonical=site_url + "feeds/",
        ),
        lastmod=ref.strftime("%Y-%m-%d"),
    )

    # ---- /404.html ---------------------------------------------------------
    site_base_path = urllib.parse.urlparse(site_url).path or "/"
    if not site_base_path.endswith("/"):
        site_base_path += "/"
    latest_entries_html = ""
    if recent_entries:
        latest_entries_html = '<ul class="entity-list">' + "".join(
            f'<li><span><a class="e-title" href="{site_base_path}{entry_url_path(e)}">{_escape(e.get("title") or e["id"])}</a>'
            f'<div class="e-meta"><span class="e-tag">{_escape(e.get("kind") or "")}</span>'
            f'<span class="muted">{_escape(e.get("priority") or "")}</span></div></span>'
            f'<span class="mono muted">{_escape(e["date"])}</span></li>'
            for e in recent_entries[:5]
        ) + "</ul>"
    err_body = f"""
<section style="max-width:62rem;margin-top:1rem">
  <p class="mono muted" style="font-size:0.78rem;letter-spacing:0.06em;text-transform:uppercase">Error 404</p>
  <h1 style="margin-top:0.2rem">That page is not on this site.</h1>
  <p class="subtitle" style="margin-top:0.6rem">
    The link you followed may be wrong, the page may have moved, or the entry that referenced it may have been corrected.
    <strong>CVE pages take a single ID</strong> — multi-CVE links like <code>cves/CVE-X,&nbsp;CVE-Y/</code> are not valid.
  </p>

  <div class="panel" style="margin-top:1.2rem">
    <h3 style="margin-top:0">Common ways here</h3>
    <ul style="margin-top:0.4rem">
      <li><strong>Renamed CVE / source / entity page.</strong> Use the search box above (also at the top of every page).</li>
      <li><strong>Old bookmark.</strong> Weekly pages moved from <code>/briefs/weekly/…</code> to <code>/weekly/…</code>; day pages keep their URLs.</li>
      <li><strong>Multi-CVE link from an older entry.</strong> Each CVE has its own page — use the search box or the
        <a href="{site_base_path}cves/">full CVE list</a>.</li>
    </ul>
  </div>

  <div class="row" style="gap:0.8rem;flex-wrap:wrap;margin-top:1.4rem">
    <a class="cta" href="{site_base_path}">Return home</a>
    <a class="cta cta--secondary" href="{site_base_path}brief/">Live brief</a>
    <a class="cta cta--secondary" href="{site_base_path}briefs/">Day archive</a>
    <a class="cta cta--secondary" href="{site_base_path}entities/">Entities</a>
    <a class="cta cta--secondary" href="{site_base_path}ops/">Operations</a>
  </div>

  {f'<h2 class="section-head" style="margin-top:1.8rem">Latest entries</h2>{latest_entries_html}' if latest_entries_html else ''}

  <p class="muted" style="margin-top:1.6rem;font-size:0.82rem">
    If you think this is a broken link inside the site, please open an issue at
    <a href="https://github.com/{os.environ.get('GITHUB_REPO', DEFAULT_GITHUB_REPO)}/issues" target="_blank" rel="noopener noreferrer">github.com/{os.environ.get('GITHUB_REPO', DEFAULT_GITHUB_REPO)}</a>.
  </p>
</section>
"""
    err = base_template(
        title=f"404 — Not found · {SITE_NAME}",
        description="The page you requested is not on this site. Search or use the suggested links to find what you were looking for.",
        body=err_body,
        canonical=site_url + "404.html",
        site_url=site_url,
        cachebust=cachebust,
        home_relative_prefix=site_base_path,
    )
    atomic_write_text(OUT / "404.html", err)

    # ---- RSS feeds -----------------------------------------------------
    daily_xml, _daily_recent = build_daily_feed(days, runs_by_day, site_url=site_url, ref_ts=ref)
    weekly_xml, _weekly_recent = build_weekly_feed(weeks, runs_by_week, site_url=site_url, ref_ts=ref)
    items_xml, _items_recent = build_items_feed(entries, site_url=site_url, ref_ts=ref)
    atomic_write_text(OUT / "feed.xml", daily_xml)
    atomic_write_text(OUT / "feed-weekly.xml", weekly_xml)
    atomic_write_text(OUT / "feed-items.xml", items_xml)
    sector_feed_results = build_sector_feeds(entries, site_url=site_url, ref_ts=ref)
    sector_feed_hashes: dict[str, str] = {}
    for fname, xml, _ts in sector_feed_results:
        atomic_write_text(OUT / fname, xml)
        sector_feed_hashes[fname] = hashlib.sha256(xml.encode("utf-8")).hexdigest()

    # ---- Sitemap / robots / security.txt / CNAME -----------------------
    write_sitemap(sorted(sitemap, key=lambda x: x[0]), out_path=OUT / "sitemap.xml")
    write_robots(OUT / "robots.txt", sitemap_url=site_url + "sitemap.xml")
    write_security_txt(
        OUT / ".well-known" / "security.txt",
        repo=os.environ.get("GITHUB_REPO", DEFAULT_GITHUB_REPO),
        expires="2027-05-08T00:00:00Z",
        site_url=site_url,
    )
    cname_src = ROOT / "CNAME"
    if cname_src.exists():
        atomic_write_text(OUT / "CNAME", _read_text_capped(cname_src, 1024))

    # ---- data/ payloads --------------------------------------------------
    atomic_write_text(
        OUT / "data" / "briefbook.json", json.dumps(briefbook, sort_keys=True)
    )
    alerts = build_alerts(entries, ref_ts=ref, site_url=site_url)
    atomic_write_text(
        OUT / "data" / "alerts.json", json.dumps(alerts, indent=2, sort_keys=True)
    )

    # ---- Manifest --------------------------------------------------------
    manifest = {
        "version": 3,
        "site_url": site_url,
        "cachebust": cachebust,
        "feeds": {
            "feed.xml": hashlib.sha256(daily_xml.encode("utf-8")).hexdigest(),
            "feed-weekly.xml": hashlib.sha256(weekly_xml.encode("utf-8")).hexdigest(),
            "feed-items.xml": hashlib.sha256(items_xml.encode("utf-8")).hexdigest(),
            **sector_feed_hashes,
        },
        "pages": manifest_pages,
        "counts": dict(counts, tags=len(tag_index), regions=len(region_index)),
    }
    atomic_write_text(OUT / "data" / "build_manifest.json", json.dumps(manifest, indent=2, sort_keys=True))

    # ---- Search index -----------------------------------------------------
    search_idx: list[dict[str, Any]] = []
    for day in sorted(days.keys(), reverse=True):
        day_ops = days[day]
        tldr = select_tldr_entries(day_ops, cap=1)
        search_idx.append({
            "kind": "day",
            "id": day,
            "title": f"CTI Daily Brief — {day}",
            "hint": (tldr[0].get("headline") or "")[:240] if tldr else f"{len(day_ops)} entries",
            "route": f"briefs/{day}/",
            "tags": sorted({c for e in day_ops for c in entry_cve_ids(e)})[:6],
        })
    for week in sorted(weeks.keys(), reverse=True):
        search_idx.append({
            "kind": "weekly",
            "id": week,
            "title": f"CTI Weekly Summary — {week}",
            "hint": f"{len(weeks[week])} strategic entries",
            "route": f"weekly/{week}/",
            "tags": [],
        })
    for e in recent_entries:
        search_idx.append({
            "kind": "entry",
            "id": e["id"],
            "title": e.get("title") or e["id"],
            "hint": (e.get("summary") or "").strip()[:240],
            "route": entry_url_path(e),
            "tags": list(e.get("tags") or [])[:4] + entry_cve_ids(e)[:4],
        })
    for ent in entities_list:
        search_idx.append({
            "kind": "entity",
            "id": ent["key"],
            "title": ent.get("title") or ent["key"],
            "hint": f"{ent.get('type', '')} · last covered {ent.get('last_covered') or '?'}",
            "route": f"entities/{urllib.parse.quote(ent['key'], safe='')}/",
            "tags": [ent.get("type") or ""] + (ent.get("flags") or []),
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

    # ---- site.json ---------------------------------------------------------
    repo = os.environ.get("GITHUB_REPO", DEFAULT_GITHUB_REPO)
    github_meta = fetch_github_metadata(repo)
    site_meta = {
        "site_url": site_url,
        "cachebust": cachebust,
        "latest_entry": recent_entries[0]["discovered_at"] if recent_entries else None,
        "counts": manifest["counts"],
        "github": github_meta or {"url": f"https://github.com/{repo}"},
    }
    atomic_write_text(OUT / "data" / "site.json", json.dumps(site_meta, indent=2, sort_keys=True))

    # ---- Prune orphans + self-check --------------------------------------
    prune_orphans(OUT)
    feed_files = [OUT / "feed.xml", OUT / "feed-weekly.xml", OUT / "feed-items.xml"] + [
        OUT / fname for fname, _xml, _ts in sector_feed_results
    ]
    errors, warnings = self_check(manifest=manifest, feed_files=feed_files, site_url=site_url)
    if warnings:
        print("SELF-CHECK WARNINGS (non-blocking):", file=sys.stderr)
        for w in warnings:
            print(f"  · {w}", file=sys.stderr)
    if errors:
        print("SELF-CHECK FAILED:", file=sys.stderr)
        for e in errors:
            print(f"  · {e}", file=sys.stderr)
        return 4

    print(
        f"built {OUT} · entries={counts['entries']} days={counts['days']} "
        f"weeklies={counts['weeklies']} entities={counts['entities']} "
        f"cves={counts['cves']} sources={counts['sources']} "
        f"tags={manifest['counts']['tags']} regions={manifest['counts']['regions']} "
        f"cachebust={cachebust} "
        f"· writes={_WRITE_COUNTER['writes']} skips={_WRITE_COUNTER['skips']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())


