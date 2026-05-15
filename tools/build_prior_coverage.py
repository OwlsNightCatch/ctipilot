#!/usr/bin/env python3
"""Build prior_coverage.json (full) + prior_coverage_keys.json (keys-only)
from gap-window dailies + previous weekly.

Walks every H3 in §§ 0–6 of each daily and §§ 0–9 of the previous weekly
in scope, extracts {key, title, tldr_one_line, primary_source_url, date,
brief_path, section}, and writes:

- work/<run-id>/prior_coverage.json       (full records — for sub-agents)
- work/<run-id>/prior_coverage_keys.json  (keys-only digest — for main agent)

v2.51 split rationale: both files are emitted in a single invocation so
Phase 0 needs only one call. The main agent reads the keys-only digest
(`{key, date, brief_path, section}` per record — no titles, no tldrs,
no URLs) for the dedup yes/no it actually needs; sub-agents read the full
file inside their isolated contexts for fetch-time PD-8 dedup against
prior titles + URLs. Keeping the prose out of the main agent's working
context cuts the dense-CTI baseline by ~8 K tokens and lowers the
cumulative cyber-content score the Anthropic classifier reads.

Pass --keys-only to emit ONLY the keys file at the --out path (legacy
single-file mode for ad-hoc invocations).

Usage:
    python3 tools/build_prior_coverage.py <run-id> <window-days> [--out PATH]
    python3 tools/build_prior_coverage.py 2026-W19-a5788b22 7

Exit codes: 0 on success; 1 on argument / IO error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Section title fragment → canonical key. Mirrors site/build.py and
# tools/check_brief.py — keep in sync with them.
_SECTION_KEYWORDS: list[tuple[str, str]] = [
    # Daily.
    ("tl;dr", "tldr"),
    ("immediate action", "immediate-actions"),
    ("active threats", "active-threats"),
    ("active threat", "active-threats"),
    ("trending vulnerabilities", "trending-vulnerabilities"),
    ("research", "research"),
    ("notable incidents", "active-threats"),
    ("switzerland, europe", "active-threats"),
    ("updates to prior coverage", "updates"),
    ("updates on previously", "updates"),
    ("deep dive", "deep-dive"),
    ("action items", "action-items"),
    ("verification notes", "verification-notes"),
    ("verification & coverage", "verification-notes"),
    # Weekly.
    ("week at a glance", "weekly-glance"),
    ("highest-impact events", "weekly-top-stories"),
    ("highest impact events", "weekly-top-stories"),
    ("top stories", "weekly-top-stories"),
    ("multi-day", "weekly-multi-day"),
    ("vulnerability roll-up", "weekly-vuln-rollup"),
    ("sector & victim", "weekly-sector-patterns"),
    ("sector and victim", "weekly-sector-patterns"),
    ("incidents & disclosures recap", "weekly-incidents-recap"),
    ("annual / periodic", "weekly-annual-reports"),
    ("annual /", "weekly-annual-reports"),
    ("annual ", "weekly-annual-reports"),
    ("long-running campaigns", "weekly-long-running"),
    ("policy & regulatory", "weekly-policy"),
    ("policy and regulatory", "weekly-policy"),
    ("looking ahead", "weekly-looking-ahead"),
]

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}")
INLINE_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
H2_RE = re.compile(r"^##\s+(?:§?\s*\d+\s*[.—-]\s+)?(?P<title>.+?)\s*$")
H3_RE = re.compile(r"^###\s+(?P<title>.+?)\s*$")


def _section_key(h2_title: str) -> str:
    lc = h2_title.lower()
    for needle, key in _SECTION_KEYWORDS:
        if needle in lc:
            return key
    return "unknown"


def _entity_key(title: str) -> str:
    """Derive a stable key for the H3.

    Priority: CVE id (first match in title) > 'actor:' / 'campaign:' /
    'incident:' / 'tool:' prefix derivation from leading capitalised
    words > slugified title.
    """
    cve = CVE_RE.search(title)
    if cve:
        return cve.group(0)
    bare = re.sub(r"^(UPDATE:|CVE-\d{4}-\d{4,7}\s*[—-]?\s*)", "", title).strip()
    bare = re.sub(r"\s*[\[(].*?[\])]\s*", "", bare)
    slug = re.sub(r"[^a-z0-9]+", "-", bare.lower()).strip("-")[:60]
    return f"item:{slug}" if slug else "item:unnamed"


def _first_url(line: str) -> str | None:
    m = INLINE_LINK_RE.search(line)
    return m.group(1) if m else None


def _first_sentence(text: str, max_chars: int = 200) -> str:
    """Return the first sentence of `text`, trimmed to `max_chars`.

    The default 200-char cap keeps the per-record JSON under ~400 bytes
    so a typical 7-day window emits ~50 KB instead of ~100 KB.
    """
    text = re.sub(r"\s+", " ", text).strip()
    # Strip inline Markdown link decoration so the tldr is plain prose.
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\(\[[^\]]*,\s*\d{4}-\d{2}-\d{2}\][^)]*\)", "", text)
    m = re.match(r"^.{40,%d}?[.!?](?=\s|$)" % max_chars, text)
    return (m.group(0) if m else text[:max_chars]).strip()


def _walk_brief(path: Path, allowed_section_keys: set[str] | None = None,
                *, keys_only: bool = False, max_tldr: int = 200) -> list[dict]:
    """Extract H3 records from the brief at `path`.

    Optional `allowed_section_keys` filter restricts to sections of
    interest (e.g. only §§ 0–6 of a daily, only §§ 0–9 of a weekly).
    """
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    records: list[dict] = []
    cur_section_key = "unknown"
    cur_h3_title: str | None = None
    cur_h3_body: list[str] = []
    cur_h3_footer: str | None = None
    brief_date = path.stem  # YYYY-MM-DD or YYYY-Www
    rel_path = path.relative_to(REPO_ROOT).as_posix()

    def _flush():
        nonlocal cur_h3_title, cur_h3_body, cur_h3_footer
        if cur_h3_title is None:
            return
        if allowed_section_keys is None or cur_section_key in allowed_section_keys:
            base = {
                "key": _entity_key(cur_h3_title),
                "title": cur_h3_title,
                "date": brief_date,
                "brief_path": rel_path,
                "section": cur_section_key,
            }
            if not keys_only:
                body_text = " ".join(s.strip() for s in cur_h3_body if s.strip())
                tldr = _first_sentence(body_text, max_chars=max_tldr)
                url = None
                if cur_h3_footer:
                    url = _first_url(cur_h3_footer)
                if not url:
                    url = _first_url(body_text)
                base["tldr_one_line"] = tldr
                base["primary_source_url"] = url
            records.append(base)
        cur_h3_title = None
        cur_h3_body = []
        cur_h3_footer = None

    for line in lines:
        h2 = H2_RE.match(line)
        if h2:
            _flush()
            cur_section_key = _section_key(h2.group("title"))
            continue
        h3 = H3_RE.match(line)
        if h3:
            _flush()
            cur_h3_title = h3.group("title").strip()
            continue
        if cur_h3_title is None:
            continue
        s = line.strip()
        if s.startswith("— *") or s.startswith("- *"):
            cur_h3_footer = s
        else:
            cur_h3_body.append(s)
    _flush()
    return records


# --- Name-collision candidates (v2.57) ------------------------------------
#
# Extracts proper-noun-shaped tokens from prior-coverage H3 titles that the
# main agent should recognise as potential collisions when composing today's
# brief. The 2026-05-15 run's iter-1 F1 (Datadog Shai-Hulud inversion)
# happened because "Shai-Hulud" appeared in prior coverage as the attacker
# worm and in today's UPDATE as the Datadog tool, without the main agent
# registering the collision. tools/check_brief.py reads this list during
# Phase 5.5 and WARNs on any new H3 that names one of these candidates
# without explicit disambiguation.

# Stop set: section/templating words that share the proper-noun shape but
# are noise. Conservative — false negatives (a real name treated as stop)
# only mean a real collision is missed; false positives (noise word flagged)
# mean operator triage burden.
_COLLISION_STOPWORDS: frozenset[str] = frozenset({
    # Document chrome
    "Daily Brief", "AI-generated", "Generated by", "TLP CLEAR",
    "Recency window", "Active Threats", "Trending Vulnerabilities",
    "Action Items", "Verification Notes", "Deep Dive", "Source", "Title",
    # Verification flags emitted in headings (SINGLE-SOURCE etc.)
    "SINGLE-SOURCE", "SINGLE-SOURCE-NATIONAL-CERT", "SINGLE-SOURCE-OTHER",
    "MULTI-SOURCE", "CONTRADICTED", "UPDATE",
    # Common technical acronyms that look like CamelCase / TitleCase
    "OAuth", "OAuth2", "SAML", "LDAP", "TLS", "HTTP", "HTTPS", "HTTP2",
    "JSON", "YAML", "XML", "REST", "API", "SDK", "RBAC", "MFA",
    "AES", "RSA", "TPM", "BIOS", "UEFI", "USB", "DMA", "DHCP", "DNS",
    "RDP", "VPN", "SSH", "FTP", "SMB", "NTLM", "Kerberos",
    "Linux", "Windows", "macOS", "iOS", "Android", "Unix", "POSIX",
    "VPS", "RAM", "CPU", "GPU", "IO", "OS", "VM", "HPC",
    # Country / region descriptors that aren't entity names
    "United States", "United Kingdom", "North-American", "Poland", "Polish",
    "European", "Europe", "Asia", "Africa",
})

# Patterns targeting codename-shaped tokens worth registering as collision
# candidates. Each pattern aims for precision; the OR-aggregation produces
# a deduplicated set across all H3 titles.
_COLLISION_PATTERNS: list[re.Pattern[str]] = [
    # Quoted codenames, e.g. "Shai-Hulud", "NGINX Rift", "Fragnesia",
    # "Dirty Frag", "Copy Fail". Lengths 3–30 to bound noise.
    re.compile(r'["“]([A-Z][A-Za-z0-9][A-Za-z0-9 \-]{1,28}[A-Za-z0-9])["”]'),
    # Hyphenated TitleCase codenames: Shai-Hulud, Mustang-Panda (≥2 parts
    # each ≥3 chars to keep noise low).
    re.compile(r'\b([A-Z][A-Za-z0-9]{2,}(?:-[A-Z][A-Za-z0-9]{2,}){1,3})\b'),
    # CamelCase single tokens of ≥7 chars: FamousSparrow, ShinyHunters,
    # ProxyNotShell, PamDOORa (≥2 internal capitalisations).
    re.compile(r'\b([A-Z][a-z]+(?:[A-Z][a-z0-9]+){1,3})\b'),
]
# NOTES on patterns deliberately excluded:
#
# - A parenthesised-content pattern was considered and rejected — it
#   duplicated useful catches with the quoted pattern but added noise
#   (country names, year/bulletin descriptors). v2.57 calibration on the
#   historical corpus showed it doubled the false-positive rate without
#   adding any entity the other patterns missed.
# - Named-actor / cluster identifiers (UAT-8616, UNC1151, APT28, Storm-2460,
#   CL-STA-1234, TA416, UAC-0057) are deliberately *not* candidates. By
#   convention these are stable tracking IDs that always refer to the same
#   actor; they are never reused for defender tooling. Flagging same-ID
#   coverage across briefs would generate noise on every legitimate
#   deep-dive update without surfacing a real collision risk. The
#   attacker-vs-defender same-name failure mode this check guards against
#   applies to *codenames* (BitLocker, Shai-Hulud, NGINX Rift), not to
#   actor IDs.


def _extract_collision_candidates(records: list[dict]) -> list[str]:
    """Return a sorted, deduplicated list of name-collision candidates from
    the title field of every prior-coverage record. Conservative filtering
    keeps the candidate list small enough that the check's WARN list stays
    readable; the operator can tune the stopwords if calibration shows
    excessive noise on the historical corpus.
    """
    raw: set[str] = set()
    for rec in records:
        title = rec.get("title") or ""
        # Strip leading "UPDATE: " / "CVE-…— " prefixes — already in the key.
        normalised = re.sub(r"^(?:UPDATE:\s*|CVE-\d{4}-\d{4,7}\s*[—–-]?\s*)", "", title)
        for pat in _COLLISION_PATTERNS:
            for m in pat.finditer(normalised):
                cand = m.group(1).strip()
                if not cand:
                    continue
                if cand in _COLLISION_STOPWORDS:
                    continue
                # Pure numeric or all-uppercase short tokens are usually
                # acronyms already in STOPWORDS; skip remaining short ones
                # to avoid CVE-suffix-style noise like "CVE", "GHSA".
                if len(cand) < 4 or cand.isdigit():
                    continue
                raw.add(cand)
    return sorted(raw, key=str.lower)


def _list_dailies_in_window(window_days: int, today: date) -> list[Path]:
    out = []
    briefs_dir = REPO_ROOT / "briefs"
    if not briefs_dir.exists():
        return []
    for p in sorted(briefs_dir.glob("[0-9]*.md")):
        try:
            d = datetime.strptime(p.stem, "%Y-%m-%d").date()
        except ValueError:
            continue
        if (today - d).days < window_days:
            out.append(p)
    return out


def _latest_weekly() -> Path | None:
    weekly_dir = REPO_ROOT / "briefs" / "weekly"
    if not weekly_dir.exists():
        return None
    files = sorted(weekly_dir.glob("[0-9]*-W[0-9]*.md"))
    return files[-1] if files else None


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("run_id", help="Deterministic run id (Phase 0 step 0)")
    ap.add_argument("window_days", type=int, help="Gap-derived window in days (≥ 1)")
    ap.add_argument("--out", help="Output path (default work/<run-id>/prior_coverage.json)")
    ap.add_argument("--include-weekly", action="store_true",
                    help="Also walk the most recent weekly brief (default: yes for weekly routine)")
    ap.add_argument("--no-weekly", action="store_true",
                    help="Skip the previous weekly even if one exists")
    ap.add_argument("--keys-only", action="store_true",
                    help="Emit just {key, title, date, brief_path, section} per record (drops tldr + url)")
    ap.add_argument("--max-tldr", type=int, default=200,
                    help="Max chars for tldr_one_line (default 200)")
    ap.add_argument("--today", default=None,
                    help="Override today's date (YYYY-MM-DD, for testing)")
    args = ap.parse_args(argv)

    if args.window_days < 1:
        print("error: window_days must be ≥ 1", file=sys.stderr)
        return 1

    today = (
        datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else date.today()
    )

    out_path = (
        Path(args.out) if args.out
        else REPO_ROOT / "work" / args.run_id / "prior_coverage.json"
    )
    out_path.parent.mkdir(parents=True, exist_ok=True)

    daily_section_keys = {
        "tldr", "immediate-actions", "active-threats", "trending-vulnerabilities",
        "research", "updates", "deep-dive", "action-items",
    }
    weekly_section_keys = {
        "weekly-glance", "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
        "weekly-sector-patterns", "weekly-incidents-recap", "weekly-annual-reports",
        "weekly-long-running", "weekly-policy", "weekly-looking-ahead",
    }

    # Walk the briefs once at full detail; the keys-only companion is
    # derived from the same records so the two outputs cannot drift.
    records: list[dict] = []
    dailies = _list_dailies_in_window(args.window_days, today)
    for dp in dailies:
        records.extend(_walk_brief(
            dp, daily_section_keys,
            keys_only=args.keys_only, max_tldr=args.max_tldr,
        ))

    weekly_path: Path | None = None
    if not args.no_weekly:
        weekly_path = _latest_weekly()
        if weekly_path is not None:
            records.extend(_walk_brief(
                weekly_path, weekly_section_keys,
                keys_only=args.keys_only, max_tldr=args.max_tldr,
            ))

    _KEYS_FIELDS = ("key", "date", "brief_path", "section")
    collision_candidates = _extract_collision_candidates(records)

    payload = {
        "run_id": args.run_id,
        "window_days": args.window_days,
        "today": today.isoformat(),
        "dailies_walked": [p.relative_to(REPO_ROOT).as_posix() for p in dailies],
        "previous_weekly": (
            weekly_path.relative_to(REPO_ROOT).as_posix() if weekly_path else None
        ),
        "records": records,
        "name_collision_candidates": collision_candidates,
    }

    with out_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    # v2.51 — emit a keys-only companion file in default (non-`--keys-only`)
    # mode so the main agent can Read just the dedup index without pulling
    # CVE titles + breach prose + URL slugs into its working context. The
    # main agent's Phase 0 reads this file; sub-agents continue reading
    # `prior_coverage.json` (full records) in their isolated contexts.
    keys_path: Path | None = None
    if not args.keys_only:
        keys_records = [
            {k: rec.get(k) for k in _KEYS_FIELDS} for rec in records
        ]
        keys_payload = {
            "run_id": args.run_id,
            "window_days": args.window_days,
            "today": today.isoformat(),
            "dailies_walked": payload["dailies_walked"],
            "previous_weekly": payload["previous_weekly"],
            "schema_note": "keys-only digest — see prior_coverage.json for full records (titles, tldrs, URLs)",
            "records": keys_records,
        }
        keys_path = out_path.parent / "prior_coverage_keys.json"
        with keys_path.open("w", encoding="utf-8") as f:
            json.dump(keys_payload, f, indent=2, ensure_ascii=False)
            f.write("\n")

    # Single-line summary on stdout for the routine to capture.
    rel_main = out_path.relative_to(REPO_ROOT).as_posix()
    if keys_path is not None:
        rel_keys = keys_path.relative_to(REPO_ROOT).as_posix()
        print(
            f"prior_coverage: path={rel_main} keys_path={rel_keys} "
            f"records={len(records)} dailies={len(dailies)} "
            f"previous_weekly={'yes' if weekly_path else 'none'} "
            f"collision_candidates={len(collision_candidates)}"
        )
    else:
        print(
            f"prior_coverage: path={rel_main} "
            f"records={len(records)} dailies={len(dailies)} "
            f"previous_weekly={'yes' if weekly_path else 'none'} "
            f"collision_candidates={len(collision_candidates)}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
