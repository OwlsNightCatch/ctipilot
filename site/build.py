#!/usr/bin/env python3
"""Build the static site bundle for GitHub Pages.

Reads:
    briefs/YYYY-MM-DD.md       (daily briefs)
    briefs/weekly/YYYY-Www.md  (weekly summaries)
    state/covered_items.json   (rolling coverage log)
    state/cves_seen.json       (flat CVE index)
    state/run_log.json         (per-run sub-agent allocation; optional)
    sources/sources.json       (curated source list)
    README.md                  (project overview)
    docs/*.md                  (workflow / verification / setup / etc.)
    prompts/CHANGELOG.md       (editorial-policy audit trail)

Writes everything the SPA needs into ./_site/:
    _site/index.html              (copied from ./index.html)
    _site/assets/...              (copied unchanged)
    _site/.nojekyll               (disable Jekyll on Pages)
    _site/feed.xml                (RSS 2.0 feed of recent briefs)
    _site/briefs/<name>.md        (raw markdown, fetched on demand)
    _site/docs/<name>.md          (raw docs)
    _site/data/manifest.json      (brief metadata, newest first)
    _site/data/cves.json          (CVE list joined with brief appearances)
    _site/data/topics.json        (covered_items joined with brief paths + verification flags)
    _site/data/sources.json       (sources joined with brief appearances)
    _site/data/search.json        (flat unified search index — briefs, sections, CVEs, topics, sources)
    _site/data/run_log.json       (mirror of state/run_log.json — for the #/ops view)
    _site/data/site.json          (build metadata: build time, counts, site URL)

Stdlib only. No build dependencies.

The site URL used in the RSS feed is read from the SITE_URL env var when set
(typical CI usage: SITE_URL=https://owlsnightcatch.github.io/security-newsletter).
Fallback default points at the project's deployed Pages URL.
"""

from __future__ import annotations

import hashlib
import html as html_mod
import json
import os
import re
import shutil
import sys
import urllib.parse
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent
OUT = SITE / "_site"

DEFAULT_SITE_URL = "https://owlsnightcatch.github.io/security-newsletter/"

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b")
LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
PROMPT_VERSION_RE = re.compile(r"\*\*Prompt:\*\*\s*v?([0-9]+\.[0-9]+)", re.IGNORECASE)
SINGLE_SOURCE_FLAGS = ("SINGLE-SOURCE-NATIONAL-CERT", "SINGLE-SOURCE-OTHER", "SINGLE-SOURCE")


def _split_sentences(s: str) -> list[str]:
    """Split a Markdown chunk into sentences, respecting bracket/paren nesting
    so `.` inside `[label, 2026-05-06]` or `(...)` does not break a sentence.
    A sentence ends at `.`, `!`, or `?` when bracket depth is zero and the
    following character is whitespace / EOS / a likely sentence opener
    (uppercase, `*` for bold, `(` for parenthetical)."""
    parts: list[str] = []
    cur: list[str] = []
    depth_brk = 0
    depth_par = 0
    n = len(s)
    i = 0
    while i < n:
        ch = s[i]
        cur.append(ch)
        if ch == "[":
            depth_brk += 1
        elif ch == "]":
            depth_brk = max(0, depth_brk - 1)
        elif ch == "(":
            depth_par += 1
        elif ch == ")":
            depth_par = max(0, depth_par - 1)
        elif ch in ".!?" and depth_brk == 0 and depth_par == 0:
            nxt = s[i + 1:i + 6]
            stripped = nxt.lstrip()
            ends_sentence = (
                not nxt
                or (nxt[:1] in (" ", "\n", "\t") and (
                    not stripped
                    or stripped[0].isupper()
                    or stripped[0] in "*_("
                ))
            )
            if ends_sentence:
                parts.append("".join(cur).strip())
                cur = []
        i += 1
    if cur:
        parts.append("".join(cur).strip())
    return [p for p in parts if p]


def slugify(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def verify_vendored_hashes() -> None:
    """Abort the build if any vendored library's bytes do not match HASHES."""
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
    failures = []
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


def host_of(url: str) -> str:
    try:
        h = (urllib.parse.urlparse(url).hostname or "").lower().strip()
        # `lstrip("www.")` strips any of {w, .} which corrupts hosts like
        # "windowsforum.com" → "indowsforum.com". `removeprefix` is the
        # right tool: it strips the literal "www." prefix exactly once.
        return h.removeprefix("www.")
    except Exception:
        return ""


def url_prefix_of(url: str) -> str:
    """Normalised URL prefix used for longest-prefix source matching (S7).

    Drops the trailing fragment / query / file, lowercases scheme+host,
    keeps the path stem so two paths under the same publisher path can
    be distinguished.
    """
    try:
        u = urllib.parse.urlparse(url)
        host = (u.hostname or "").lower().removeprefix("www.")
        if not host:
            return ""
        path = u.path or "/"
        # Strip trailing filename so /security/blog/2024/x.html and
        # /security/blog/2024/y.html share the same prefix.
        if "/" in path:
            head, _, tail = path.rpartition("/")
            if "." in tail:
                path = head + "/"
        return f"{host}{path}"
    except Exception:
        return ""


def parse_brief(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    rel = str(path.relative_to(ROOT))
    name = path.stem
    is_weekly = path.parent.name == "weekly"

    m = re.search(r"^# (.+?)\s*$", text, re.MULTILINE)
    title = m.group(1).strip() if m else name

    gen_match = re.search(r"\*\*Generated by:\*\*\s*([^\n·]+)", text)
    generated_by = gen_match.group(1).strip() if gen_match else None

    pv_match = PROMPT_VERSION_RE.search(text)
    prompt_version = pv_match.group(1) if pv_match else None

    sections = []
    for m in re.finditer(r"^## (.+?)\s*$", text, re.MULTILINE):
        heading = m.group(1).strip()
        sections.append({"heading": heading, "anchor": slugify(heading)})

    # H3 headings are item-level. We index them for section-level search (S5).
    subsections = []
    for m in re.finditer(r"^### (.+?)\s*$", text, re.MULTILINE):
        heading = m.group(1).strip()
        # Drop verification-flag tags from search-result titles to keep them tidy
        clean = re.sub(r"\s*\[(SINGLE-SOURCE(?:-[A-Z-]+)?)\]\s*", " ", heading).strip()
        subsections.append({
            "heading": clean,
            "raw_heading": heading,
            "anchor": slugify(heading),
        })

    tldr = []
    tldr_block = re.search(
        r"##\s*0\.\s*TL;DR\s*\n(.+?)(?=\n##\s|\Z)",
        text,
        re.DOTALL,
    )
    if tldr_block:
        for raw in tldr_block.group(1).splitlines():
            line = raw.strip()
            if line.startswith("- "):
                tldr.append(line[2:].strip())

    cves = sorted(set(CVE_RE.findall(text)))

    links = []
    seen = set()
    for m in LINK_RE.finditer(text):
        label, url = m.group(1).strip(), m.group(2).strip()
        if url in seen:
            continue
        seen.add(url)
        links.append({"label": label, "url": url, "host": host_of(url), "prefix": url_prefix_of(url)})

    h3 = len(re.findall(r"^### .+$", text, re.MULTILINE))

    # Per-CVE citations: walk the brief by *paragraph* (blank-line-separated
    # blocks) plus by *table-row* for the trending-vulns table in § 1b. For
    # each unit that mentions a CVE id, register every inline `[label](url)`
    # citation from that same unit under the CVE. Paragraph scope (vs H3
    # section scope) avoids the bleed where one section discusses CVE-A in
    # body and only mentions CVE-B in passing — both used to inherit each
    # other's citations. The CVE detail page surfaces this list as "All
    # cited sources for this CVE", complementing the single
    # `primary_source_url` recorded in cves_seen.json.
    cve_citations: dict[str, list[dict]] = {}

    def register(cve_id: str, label: str, url: str) -> None:
        bucket = cve_citations.setdefault(cve_id, [])
        if any(c["url"] == url for c in bucket):
            return
        bucket.append({
            "label": label,
            "url": url,
            "host": host_of(url),
            "prefix": url_prefix_of(url),
        })

    # Skip the metadata header above the first H2.
    body_start_match = re.search(r"^## ", text, re.MULTILINE)
    body = text[body_start_match.start():] if body_start_match else text

    # Each "unit" is either a Markdown paragraph (\n\n separated) OR a
    # single Markdown table row (`| ... |`). Headings count as their own
    # standalone unit so a CVE in an H3 heading still grabs citations
    # only from the immediate body paragraph that follows.
    units: list[str] = []
    for chunk in re.split(r"\n\s*\n", body):
        chunk = chunk.strip()
        if not chunk:
            continue
        # Table block? Split into rows so each row's CVE only inherits
        # citations from its own row.
        if "\n|" in chunk and chunk.lstrip().startswith("|"):
            for line in chunk.splitlines():
                if line.strip().startswith("|"):
                    units.append(line)
            continue
        # List block? Split into individual bullets so a 5-bullet TL;DR
        # doesn't get treated as one giant paragraph mentioning 5 CVEs.
        # A bullet line starts with `- ` or `* `; continuation lines start
        # with whitespace.
        if re.match(r"^[-*]\s+", chunk):
            current: list[str] = []
            for line in chunk.splitlines():
                if re.match(r"^[-*]\s+", line) and current:
                    units.append("\n".join(current))
                    current = [line]
                else:
                    current.append(line)
            if current:
                units.append("\n".join(current))
            continue
        units.append(chunk)

    # Walk by unit (paragraph / bullet / table-row). Each unit that
    # mentions one or more CVEs has every inline `[label](url)` in the
    # unit attributed to each of those CVEs. The bullet-split + table-row-
    # split keep each TL;DR bullet and each table row as its own unit so
    # adjacent items can't bleed into each other. A unit listing more
    # than 3 distinct CVEs is treated as a summary recap (e.g. § 7
    # "Items verified multi-source: CVE-A (src1); CVE-B (src2); …") and
    # skipped — those lists mention every CVE alongside every citation
    # and would leak every source under every CVE.
    for unit in units:
        cves_in_unit = set(CVE_RE.findall(unit))
        if not cves_in_unit:
            continue
        if len(cves_in_unit) > 3:
            continue
        for m in LINK_RE.finditer(unit):
            label = m.group(1).strip()
            url = m.group(2).strip()
            for cve_id in cves_in_unit:
                register(cve_id, label, url)

    # URL-embedded-CVE rule (independent of unit scope): a citation whose
    # URL itself contains a CVE id is attributed to that CVE wherever it
    # appears in the brief. Catches NVD / CISA KEV detail URLs and vendor
    # PSIRT pages whose path is `…/CVE-YYYY-NNNNN`.
    for m in LINK_RE.finditer(body):
        label = m.group(1).strip()
        url = m.group(2).strip()
        for url_cve in CVE_RE.findall(url):
            register(url_cve, label, url)

    # Cache per-unit text + link list so `annotate_topics()` can run the
    # same paragraph-scope citation aggregation against topic titles
    # (actor / campaign / incident / tool / annual-report names).
    unit_data: list[dict] = []
    for unit in units:
        unit_links: list[dict] = []
        for m in LINK_RE.finditer(unit):
            unit_links.append({
                "label": m.group(1).strip(),
                "url": m.group(2).strip(),
                "host": host_of(m.group(2).strip()),
                "prefix": url_prefix_of(m.group(2).strip()),
            })
        if not unit_links:
            continue
        unit_data.append({
            "text": unit,
            "text_lower": unit.lower(),
            "cves": sorted(set(CVE_RE.findall(unit))),
            "links": unit_links,
        })

    # Verification flags per item (S9) — extract per H3-heading SINGLE-SOURCE-* tags.
    item_flags: dict[str, list[str]] = {}
    # split text on H3 boundaries to associate flags with the section that contained them
    for m in re.finditer(r"^### (.+?)\s*$", text, re.MULTILINE):
        heading = m.group(1).strip()
        flags = []
        for f in SINGLE_SOURCE_FLAGS:
            if f"[{f}]" in heading:
                flags.append(f)
                # only one flag per heading is meaningful; longest-first
                break
        if flags:
            item_flags[heading] = flags

    return {
        "name": name,
        "kind": "weekly" if is_weekly else "daily",
        "path": rel,
        "title": title,
        "generated_by": generated_by,
        "prompt_version": prompt_version,
        "sections": sections,
        "subsections": subsections,
        "tldr": tldr,
        "cves": cves,
        "links": links,
        "items": h3,
        "size": len(text),
        "item_flags": item_flags,
        "cve_citations": cve_citations,
        "unit_data": unit_data,
    }


def collect_briefs() -> list[dict]:
    out = []
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


def annotate_sources(sources: dict, briefs: list[dict]) -> dict:
    """Match brief citations to sources by longest URL prefix (S7).

    A source whose `url` prefix is a strict superset of another source's
    prefix wins over the shorter one. Falls back to host match when no
    source has a path-level prefix that fits the link.
    """
    prefixes: list[tuple[str, str, str]] = []  # (prefix, host, source_id)
    for s in sources["sources"]:
        pfx = url_prefix_of(s["url"])
        host = host_of(s["url"])
        if pfx or host:
            prefixes.append((pfx, host, s["id"]))

    # Longest prefix first. Empty-prefix entries sort to the bottom.
    prefixes.sort(key=lambda t: (len(t[0]), len(t[1])), reverse=True)

    src_appearances: dict[str, set[str]] = defaultdict(set)
    for b in briefs:
        for link in b["links"]:
            link_pfx = link.get("prefix", "")
            link_host = link.get("host", "")
            if not link_pfx and not link_host:
                continue
            best_id = None
            # Prefer URL-prefix match.
            for pfx, host, sid in prefixes:
                if pfx and link_pfx.startswith(pfx):
                    best_id = sid
                    break
            if best_id is None:
                # Fall back to host match (exact or subdomain).
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

    return {
        **sources,
        "sources": enriched,
    }


def annotate_cves(cves: dict, briefs: list[dict], sources: dict | None = None) -> dict:
    by_id: dict[str, set[str]] = defaultdict(set)
    # citations_by_id[cve_id][url] = {label, url, host, prefix, source_id?, briefs: [...]}
    citations_by_id: dict[str, dict[str, dict]] = defaultdict(dict)

    # Pre-build the source-prefix table so we can attach a source_id to every
    # citation (lets the CVE detail page link the citation back to the source's
    # entry in #/sources/<id>).
    src_prefixes: list[tuple[str, str, str]] = []
    if sources is not None:
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
        cites = sorted(citations_by_id.get(c["id"], {}).values(), key=lambda x: x["host"] or x["url"])
        enriched.append({**c, "appearances": appearances, "citations": cites})
        seen_ids.add(c["id"])
    for cid, briefs_set in by_id.items():
        if cid in seen_ids:
            continue
        cites = sorted(citations_by_id.get(cid, {}).values(), key=lambda x: x["host"] or x["url"])
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


def annotate_topics(items: dict, briefs: list[dict], sources: dict | None = None) -> dict:
    """Normalize, attach `briefs[]`, fold per-item verification flags from
    the brief markdown back onto each topic (S9), and — same as for CVEs —
    aggregate every cited source from the paragraphs/bullets/table-rows
    that mention the topic across all briefs. The Topic detail page uses
    this list to surface "All cited sources for this topic" so the reader
    can pivot directly to the underlying article.

    Topic-to-paragraph matching:
    - For type=`cve` topics, the topic key is a `CVE-YYYY-NNNNN` id and
      we reuse the existing CVE-id substring index (already accurate).
    - For other types (actor, campaign, incident, tool, annual-report),
      we match on the topic title's primary phrase: the part before
      ` — ` or `: ` if present, otherwise the whole title. Case-insensitive
      substring match against each unit's text.

    The same "skip a unit if it mentions more than 3 distinct CVEs"
    summary-recap guard applies, with an analogous guard "skip a unit
    that matches more than 3 distinct topics" so the § 7 verification
    summary line never leaks every source under every topic.
    """
    # Index brief flags by (brief_name, normalised_heading)
    flag_lookup: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for b in briefs:
        for heading, flags in b.get("item_flags", {}).items():
            flag_lookup[b["name"]].append((heading.lower(), flags[0] if flags else ""))

    # Pre-build the source-prefix table so we can attach a source_id to
    # every citation (mirrors the CVE-detail logic).
    src_prefixes: list[tuple[str, str, str]] = []
    if sources is not None:
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

    # Build a per-topic match-phrase. Used as case-insensitive substring
    # against each unit. We also keep a separate `cves_in_topic` set for
    # CVE-typed topics to reuse the CVE-id substring index.
    def topic_phrase(t: dict) -> str:
        title = (t.get("title") or "").strip()
        if not title:
            return (t.get("key") or "").strip()
        # Trim at em-dash or colon — keeps just the proper noun / id.
        for sep in (" — ", " – ", ": "):
            if sep in title:
                title = title.split(sep, 1)[0]
                break
        return title.strip()

    topic_match: list[dict] = []
    for it in items["items"]:
        ttype = (it.get("type") or "").lower()
        phrase = topic_phrase(it).lower()
        cve_match = None
        if ttype == "cve":
            cve_match = (it.get("key") or "").upper()
        topic_match.append({
            "key": it["key"],
            "phrase": phrase,
            "cve_match": cve_match,
        })

    # Aggregate citations per topic by walking each brief's unit_data.
    # citations_by_key[topic_key][url] = {label, url, host, source_id, briefs}
    citations_by_key: dict[str, dict[str, dict]] = defaultdict(dict)
    for b in briefs:
        for unit in b.get("unit_data") or []:
            text_lower = unit["text_lower"]
            cves_in_unit = unit["cves"]
            # Skip the >3-CVE summary recap line.
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
    for it in items["items"]:
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
        cites = sorted(citations_by_key.get(it["key"], {}).values(), key=lambda x: x["host"] or x["url"])
        enriched.append({**it, "briefs": names, "flags": sorted(flags), "citations": cites})
    enriched.sort(key=lambda i: i.get("last_covered", ""), reverse=True)
    return {**items, "items": enriched}


def build_search_index(
    briefs: list[dict],
    cves: dict,
    topics: dict,
    sources: dict,
) -> list[dict]:
    """Flat unified search index. Each entry:
        {kind, id, title, hint, briefs, route, tags}
    """
    idx = []

    for b in briefs:
        hint = " · ".join(b["tldr"][:2])[:240] if b["tldr"] else ""
        idx.append(
            {
                "kind": "brief",
                "id": b["name"],
                "title": b["title"],
                "hint": hint or f"{b['kind'].capitalize()} brief · {b['items']} items",
                "tags": [b["kind"]] + b["cves"][:6],
                "route": f"#/briefs/{b['name']}",
            }
        )
        # Section-level entries (S5) — every H3 inside the brief.
        for sub in b.get("subsections", []):
            idx.append({
                "kind": "section",
                "id": f"{b['name']}#{sub['anchor']}",
                "title": sub["heading"],
                "hint": f"in {b['title']}",
                "tags": [b["kind"]],
                "route": f"#/briefs/{b['name']}?at={urllib.parse.quote(sub['anchor'], safe='')}",
            })

    for c in cves["cves"]:
        idx.append(
            {
                "kind": "cve",
                "id": c["id"],
                "title": c["id"],
                "hint": c.get("title", "")[:240],
                "tags": [],
                "route": f"#/cves/{c['id']}",
            }
        )

    for t in topics["items"]:
        idx.append(
            {
                "kind": "topic",
                "id": t["key"],
                "title": t["title"],
                "hint": f"{t['type']} · last covered {t.get('last_covered','?')}",
                "tags": [t["type"]] + (t.get("flags") or []),
                "route": f"#/topics/{urllib.parse.quote(t['key'], safe='')}",
            }
        )

    for s in sources["sources"]:
        cats = ", ".join(s.get("category", []))
        idx.append(
            {
                "kind": "source",
                "id": s["id"],
                "title": s["publisher"],
                "hint": f"{s['reliability']} · {cats}",
                "tags": s.get("category", []) + [s.get("reliability", ""), s.get("status", "")],
                "route": f"#/sources/{urllib.parse.quote(s['id'], safe='')}",
            }
        )

    return idx


def write_rss_feed(briefs: list[dict], site_url: str, out_path: Path) -> None:
    """RSS 2.0 feed. Most-recent 30 briefs (S1).

    Each item links to the SPA route #/briefs/<name>; the description
    is the TL;DR bullets joined with HTML line breaks.
    """
    site_url = site_url.rstrip("/") + "/"
    now = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")

    def item_xml(b: dict) -> str:
        link = f"{site_url}#/briefs/{b['name']}"
        guid = link
        # pubDate: midnight UTC of the brief date (best-effort)
        pub = ""
        if re.match(r"^\d{4}-\d{2}-\d{2}$", b["name"]):
            try:
                dt = datetime.strptime(b["name"], "%Y-%m-%d").replace(tzinfo=timezone.utc)
                pub = dt.strftime("%a, %d %b %Y 00:00:00 +0000")
            except Exception:
                pass
        elif re.match(r"^\d{4}-W\d{2}$", b["name"]):
            try:
                # ISO week: pick the Monday of that week
                yr, wk = b["name"].split("-W")
                dt = datetime.strptime(f"{yr}-W{wk}-1", "%G-W%V-%u").replace(tzinfo=timezone.utc)
                pub = dt.strftime("%a, %d %b %Y 00:00:00 +0000")
            except Exception:
                pass
        body_lines = [f"<li>{html_mod.escape(line)}</li>" for line in b.get("tldr", [])[:6]]
        body = ("<ul>" + "".join(body_lines) + "</ul>") if body_lines else f"<p>{html_mod.escape(b['kind'])} brief · {b.get('items', 0)} items</p>"
        title = html_mod.escape(b["title"])
        cats = "".join(f"<category>{html_mod.escape(c)}</category>" for c in b.get("cves", [])[:8])
        return (
            "<item>"
            f"<title>{title}</title>"
            f"<link>{html_mod.escape(link)}</link>"
            f"<guid isPermaLink=\"true\">{html_mod.escape(guid)}</guid>"
            + (f"<pubDate>{pub}</pubDate>" if pub else "")
            + cats
            + f"<description><![CDATA[{body}]]></description>"
            + "</item>"
        )

    items_xml = "".join(item_xml(b) for b in briefs[:30])
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">'
        '<channel>'
        '<title>CTI Briefs — Switzerland, Europe &amp; Public Sector</title>'
        f'<link>{html_mod.escape(site_url)}</link>'
        f'<atom:link href="{html_mod.escape(site_url + "feed.xml")}" rel="self" type="application/rss+xml"/>'
        '<description>Daily and weekly cyber threat intelligence briefs covering Switzerland, Europe, and the public sector — autonomously generated, source-linked, IOC-free.</description>'
        '<language>en</language>'
        f'<lastBuildDate>{now}</lastBuildDate>'
        f'{items_xml}'
        '</channel></rss>'
    )
    out_path.write_text(feed, encoding="utf-8")


def write_sitemap(briefs: list[dict], site_url: str, out_path: Path) -> None:
    """Emit an XML sitemap listing the home page, the static routes, and
    every brief's hash URL. Each entry has a <lastmod> derived from the
    brief date when applicable."""
    site = site_url.rstrip("/") + "/"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls: list[tuple[str, str, str]] = []  # (loc, lastmod, changefreq)

    static_routes = [
        ("", "daily"),
        ("#/briefs", "daily"),
        ("#/cves", "weekly"),
        ("#/topics", "weekly"),
        ("#/sources", "monthly"),
        ("#/ops", "daily"),
        ("#/about", "monthly"),
    ]
    for path, freq in static_routes:
        urls.append((site + path, today, freq))

    for b in briefs[:200]:
        # Briefs are immutable once published; their lastmod is the brief date.
        date = b["name"] if re.match(r"^\d{4}-\d{2}-\d{2}$", b["name"]) else today
        prefix = "#/briefs/weekly/" if b["kind"] == "weekly" else "#/briefs/"
        urls.append((site + prefix + b["name"], date, "never"))

    body = "".join(
        "<url>"
        f"<loc>{html_mod.escape(loc)}</loc>"
        f"<lastmod>{lastmod}</lastmod>"
        f"<changefreq>{freq}</changefreq>"
        "</url>"
        for loc, lastmod, freq in urls
    )
    out_path.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + body
        + '</urlset>',
        encoding="utf-8",
    )


def copy_tree(src: Path, dst: Path):
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def cachebust_index(index_path: Path) -> str:
    """Append ?v=<fingerprint> to every asset URL in index.html."""
    assets_dir = index_path.parent / "assets"
    h = hashlib.sha256()
    for p in sorted(assets_dir.rglob("*")):
        if p.is_file() and p.suffix in (".js", ".css"):
            h.update(p.read_bytes())
    fingerprint = h.hexdigest()[:10]

    html = index_path.read_text()

    def add_v(match: re.Match) -> str:
        prefix, attr_, url = match.group(1), match.group(2), match.group(3)
        if "?" in url:
            return match.group(0)
        return f'{prefix}{attr_}="{url}?v={fingerprint}"'

    html = re.sub(
        r'(<(?:script|link)[^>]*?\s)(src|href)="(assets/[^"]+\.(?:js|css))"',
        add_v,
        html,
    )
    index_path.write_text(html)
    return fingerprint


def main() -> int:
    if not (ROOT / "briefs").exists():
        print(f"error: no briefs/ directory at {ROOT}", file=sys.stderr)
        return 1

    verify_vendored_hashes()

    site_url = os.environ.get("SITE_URL", DEFAULT_SITE_URL)

    OUT.mkdir(exist_ok=True)
    for child in OUT.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()

    # 1. Copy SPA shell.
    shutil.copy(SITE / "index.html", OUT / "index.html")
    copy_tree(SITE / "assets", OUT / "assets")
    (OUT / ".nojekyll").write_text("")

    # 1a. Cache-bust the asset URLs.
    fp = cachebust_index(OUT / "index.html")

    # 2. Copy briefs (raw markdown, fetched on demand by the SPA).
    briefs_out = OUT / "briefs"
    briefs_out.mkdir(exist_ok=True)
    for p in (ROOT / "briefs").glob("*.md"):
        if re.match(r"^\d{4}-\d{2}-\d{2}\.md$", p.name):
            shutil.copy(p, briefs_out / p.name)
    weekly_dir = ROOT / "briefs" / "weekly"
    if weekly_dir.exists():
        (briefs_out / "weekly").mkdir(exist_ok=True)
        for p in weekly_dir.glob("*.md"):
            if re.match(r"^\d{4}-W\d{2}\.md$", p.name):
                shutil.copy(p, briefs_out / "weekly" / p.name)

    # 3. Copy README, docs, and the prompt CHANGELOG (for the About page).
    docs_out = OUT / "docs"
    docs_out.mkdir(exist_ok=True)
    shutil.copy(ROOT / "README.md", docs_out / "README.md")
    if (ROOT / "briefs" / "README.md").exists():
        shutil.copy(ROOT / "briefs" / "README.md", docs_out / "briefs-README.md")
    for p in (ROOT / "docs").glob("*.md"):
        shutil.copy(p, docs_out / p.name)
    if (ROOT / "prompts" / "CHANGELOG.md").exists():
        shutil.copy(ROOT / "prompts" / "CHANGELOG.md", docs_out / "CHANGELOG.md")

    # 4. Build data bundle.
    data_out = OUT / "data"
    data_out.mkdir(exist_ok=True)

    briefs = collect_briefs()
    cves_raw = json.loads((ROOT / "state" / "cves_seen.json").read_text())
    topics_raw = json.loads((ROOT / "state" / "covered_items.json").read_text())
    sources_raw = json.loads((ROOT / "sources" / "sources.json").read_text())

    sources = annotate_sources(sources_raw, briefs)
    cves = annotate_cves(cves_raw, briefs, sources)
    topics = annotate_topics(topics_raw, briefs, sources)

    # Strip internal-only fields from the published manifest. `item_flags`
    # is rolled up into `topics.json`; `cve_citations` is rolled up into
    # `cves.json`; `unit_data` is consumed by `annotate_topics`.
    public_briefs = []
    for b in briefs:
        copy = {k: v for k, v in b.items() if k not in ("item_flags", "cve_citations", "unit_data")}
        public_briefs.append(copy)

    (data_out / "manifest.json").write_text(json.dumps(public_briefs, indent=2))
    (data_out / "cves.json").write_text(json.dumps(cves, indent=2))
    (data_out / "topics.json").write_text(json.dumps(topics, indent=2))
    (data_out / "sources.json").write_text(json.dumps(sources, indent=2))
    (data_out / "search.json").write_text(
        json.dumps(build_search_index(public_briefs, cves, topics, sources))
    )

    # Run log — optional, surfaced by #/ops.
    run_log_src = ROOT / "state" / "run_log.json"
    if run_log_src.exists():
        try:
            payload = json.loads(run_log_src.read_text())
            (data_out / "run_log.json").write_text(json.dumps(payload, indent=2))
        except Exception as e:
            print(f"warning: state/run_log.json failed to parse ({e}); skipping copy", file=sys.stderr)

    # 5. RSS feed (S1) at the site root.
    write_rss_feed(briefs, site_url, OUT / "feed.xml")

    # 5a. SEO: sitemap.xml + robots.txt. Hash-routed SPA → most crawlers
    # treat #/path as a fragment (one URL). We still emit a sitemap that
    # lists every brief's hash URL plus the static routes; modern
    # crawlers that respect rel=canonical + JS rendering will pick them
    # up (Bing, Brave, DuckDuckBot, etc.). Google ignores hash fragments
    # but the canonical/og tags compensate.
    write_sitemap(briefs, site_url, OUT / "sitemap.xml")
    (OUT / "robots.txt").write_text(
        "User-agent: *\n"
        "Allow: /\n"
        f"Sitemap: {site_url.rstrip('/')}/sitemap.xml\n",
        encoding="utf-8",
    )

    site_meta = {
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "site_url": site_url,
        "counts": {
            "briefs": len(briefs),
            "daily": sum(1 for b in briefs if b["kind"] == "daily"),
            "weekly": sum(1 for b in briefs if b["kind"] == "weekly"),
            "cves": len(cves["cves"]),
            "topics": len(topics["items"]),
            "sources": len(sources["sources"]),
        },
    }
    (data_out / "site.json").write_text(json.dumps(site_meta, indent=2))

    print(f"built {OUT} · {site_meta['counts']} · cachebust=v={fp} · feed={site_url}feed.xml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
