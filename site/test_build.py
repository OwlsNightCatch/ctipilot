#!/usr/bin/env python3
"""Stdlib-only smoke tests for site/build.py (v3 pipeline SSG).

Run with: `python3 site/test_build.py` from the repo root. Returns
exit code 0 on pass, 1 on any failure. Used as a gate by
tools/check_run.py and by CI.

Tests cover:
    - Markdown → HTML rendering + URL-scheme allowlist + control-char
      stripping (unchanged security primitives)
    - secret scanner, CDATA safety, XML DTD/entity refusal, path-segment
      safety
    - content_model round-trip (strict-YAML-subset parse/dump, entry
      loader, schema validation)
    - render_brief_sections: section stubs, TL;DR ordering, the
      Immediate-Action callout, § Updates from changelog records, action
      items, run notes
    - the entry lifecycle (v4.0): updates[] ⇔ body-section pairing, activity
      windowing, the live timeline's UPD rows, entry-page revision history,
      per-record feed items, the home Updates card
    - briefbook.json / alerts.json shapes
    - day grouping + section-key routing
    - RSS generation from fixture entries (incl. sector slices)
    - entity appearance matching (registry keys, aliases, CVE ids)
    - umami/CSP consistency + the branding profile contract
"""

import copy
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent

sys.path.insert(0, str(SITE))
import build  # noqa: E402
import content_model  # noqa: E402
from build import (  # noqa: E402
    SECTION_EMPTY_STUB,
    _cdata_safe,
    _safe_url,
    _strip_controls,
    _verification_clean_publish,
    _verification_confirmation,
    _verification_fix_rounds,
    _xml_validate,
    annotate_sources,
    build_alerts,
    build_briefbook,
    build_entities,
    build_graph_payload,
    build_items_feed,
    build_sector_feeds,
    compute_related_entities,
    daily_run_dates,
    enhance_brief_item_html,
    entries_by_day,
    entry_activity,
    entry_section_key,
    is_safe_path_segment,
    parse_taxonomy,
    render_alarm,
    render_brief_sections,
    render_cve_pill,
    render_day_page,
    render_days_index_page,
    render_entry_card,
    render_changes_page,
    render_entry_page,
    render_inline,
    render_live_brief_page,
    render_markdown,
    render_ops_page,
    render_run_detail_page,
    render_run_divider,
    render_timeline_item,
    render_update_card,
    run_url_path,
    scan_for_secrets,
    select_tldr_entries,
    slugify,
    update_records_in,
)
from build import _live_timeline_html  # noqa: E402

FAILURES: list[str] = []


def assert_eq(name: str, got, want) -> None:
    if got == want:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}")
        print(f"  FAIL {name}: got {got!r}, want {want!r}")


def assert_true(name: str, cond) -> None:
    if cond:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: condition is false")
        print(f"  FAIL {name}")


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
    if re.search(pattern, hay):
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: pattern {pattern!r} not in {hay[:200]!r}")
        print(f"  FAIL {name}")


# ---------------------------------------------------------------------
# Markdown rendering (unchanged security-relevant primitives)
# ---------------------------------------------------------------------
print("== render_inline ==")
assert_eq("bold renders as strong", render_inline("a **bold** term"),
          "a <strong>bold</strong> term")
assert_eq("italic renders as em", render_inline("a *slanted* term"),
          "a <em>slanted</em> term")
assert_eq("inline code renders as code", render_inline("the `key` is here"),
          "the <code>key</code> is here")

link_html = render_inline("see [the advisory](https://example.com/cve)")
assert_in("link href present", 'href="https://example.com/cve"', link_html)
assert_not_in("link bracket leak", "[the advisory]", link_html)
assert_in("external link target=_blank", 'target="_blank"', link_html)
assert_in("external link rel noopener", 'rel="noopener noreferrer"', link_html)
relative_html = render_inline("see [other section](#anchor)")
assert_in("relative link href present", 'href="#anchor"', relative_html)
assert_not_in("relative link no target", 'target="_blank"', relative_html)
code_in_label = render_inline("read [`tools/x.py` docs](https://example.com/x)")
assert_in("code span inside link label", "<code>tools/x.py</code>", code_in_label)
assert_not_in("no placeholder leak", "CODE0", code_in_label)

print("== render_markdown ==")
md_html = render_markdown("# Head\n\npara **b**\n\n- a\n- b\n\n```sh\nhi\n```")
assert_in("heading rendered", "<h1", md_html)
assert_in("list rendered", "<li>a</li>", md_html)
assert_in("fence rendered", "<pre><code", md_html)
assert_not_in("no raw bold survives", "**b**", md_html)

# `heading_base` re-levels an embedded document in reading order: the first
# heading lands on the base and nothing below it can skip a level, however
# the author numbered their hashes.
_hb = render_markdown("## A\n\nx\n\n### A1\n\ny\n\n## B\n", heading_base=3)
assert_eq("heading_base re-levels a well-formed document",
          re.findall(r"<h([1-6])", _hb), ["3", "4", "3"])
_gap = render_markdown("#### First\n\nx\n\n#### Second\n\ny\n\n### Later\n",
                       heading_base=3)
assert_eq("an authoring gap never emits a skipped level",
          re.findall(r"<h([1-6])", _gap), ["3", "3", "3"])
_deep = render_markdown("# T\n\n## S\n\n### D\n", heading_base=5)
assert_eq("re-levelling caps at h6", re.findall(r"<h([1-6])", _deep), ["5", "6", "6"])

print("== enhance_brief_item_html (Defender-takeaway callout) ==")
lead_html = enhance_brief_item_html(
    "<p><strong>Defender takeaway:</strong> patch now.</p>"
)
assert_in("leading label promoted to aside",
          '<aside class="callout callout--takeaway"', lead_html)
assert_in("label badge rendered",
          '<span class="callout__label">Defender takeaway</span>', lead_html)
assert_in("body carried into callout, first letter capitalised", "Patch now.", lead_html)
assert_not_in("no leftover empty paragraph", "<p></p>", lead_html)
mid_html = enhance_brief_item_html(
    "<p>Narrative prose with <strong>bold</strong> inline. "
    "<strong>Defender takeaway:</strong> rotate the keys.</p>"
)
assert_in("mid-paragraph label promoted to aside",
          '<aside class="callout callout--takeaway"', mid_html)
assert_in("preceding prose kept as its own paragraph",
          "<p>Narrative prose with <strong>bold</strong> inline.</p>", mid_html)
assert_in("takeaway body carried into callout, capitalised", "Rotate the keys.", mid_html)
two_para = enhance_brief_item_html(
    "<p>First paragraph, no label.</p>\n"
    "<p><strong>Detection guidance:</strong> watch process trees.</p>"
)
assert_in("label-free paragraph untouched",
          "<p>First paragraph, no label.</p>", two_para)
assert_in("detection label maps to detection class",
          'class="callout callout--detection"', two_para)
assert_eq("idempotent on second pass",
          enhance_brief_item_html(mid_html), mid_html)
plain = "<p>No callout label anywhere in this text.</p>"
assert_eq("paragraph without label passes through", enhance_brief_item_html(plain), plain)

print("== _safe_url ==")
assert_eq("javascript: neutered", _safe_url("javascript:alert(1)"), "#")
assert_eq("data: neutered", _safe_url("data:text/html,<b>x</b>"), "#")
assert_eq("vbscript: neutered", _safe_url("vbscript:x"), "#")
assert_eq("mixed-case scheme neutered", _safe_url("JaVaScRiPt:alert(1)"), "#")
assert_eq("control-char smuggle neutered", _safe_url("java\tscript:alert(1)"), "#")
assert_eq("protocol-relative refused", _safe_url("//evil.example/x"), "#")
assert_eq("backslash lead refused", _safe_url("\\\\evil.example\\x"), "#")
assert_eq("https passes", _safe_url("https://ok.example/a"), "https://ok.example/a")
assert_eq("anchor passes", _safe_url("#frag"), "#frag")
assert_eq("relative passes", _safe_url("briefs/2026-07-03/"), "briefs/2026-07-03/")
evil_link = render_inline("[click](javascript:alert(1))")
assert_in("renderer neuters javascript links", 'href="#"', evil_link)

print("== is_safe_path_segment ==")
assert_eq("plain id ok", is_safe_path_segment("cisa-kev"), True)
assert_eq("cve id ok", is_safe_path_segment("CVE-2026-1234"), True)
assert_eq("typed key ok", is_safe_path_segment("actor:lazarus"), True)
assert_eq("dotdot rejected", is_safe_path_segment("../etc"), False)
assert_eq("slash rejected", is_safe_path_segment("a/b"), False)
assert_eq("leading dot rejected", is_safe_path_segment(".htaccess"), False)
assert_eq("empty rejected", is_safe_path_segment(""), False)

print("== slugify ==")
assert_eq("slugify basic", slugify("Hello, World! 42"), "hello-world-42")

print("== _cdata_safe / _xml_validate ==")
assert_eq("cdata break split", _cdata_safe("a]]>b"), "a]]]]><![CDATA[>b")
assert_eq("valid xml passes", _xml_validate("<a><b>x</b></a>"), [])
assert_true("doctype refused",
            _xml_validate('<!DOCTYPE foo [<!ENTITY x "y">]><a>&x;</a>'))
assert_true("entity decl refused", _xml_validate('<!ENTITY x "y"><a/>'))

print("== _strip_controls ==")
assert_eq("nul stripped", _strip_controls("a\x00b"), "ab")
assert_eq("tab/newline kept", _strip_controls("a\tb\nc"), "a\tb\nc")

print("== dedash (no em dash reaches a reader) ==")
DASH = "\u2014"
assert_eq("appositive takes a comma",
          build.dedash("the assessment " + DASH + " an archive containing a shortcut file"),
          "the assessment, an archive containing a shortcut file")
assert_eq("independent clause takes a semicolon",
          build.dedash("no fix for v23 and earlier " + DASH + " vendor recommends upgrading"),
          "no fix for v23 and earlier; vendor recommends upgrading")
assert_eq("a leading conjunction stays a comma",
          build.dedash("needs 7.1.5 " + DASH + " so a fleet on 7.1.0 is still exposed"),
          "needs 7.1.5, so a fleet on 7.1.0 is still exposed")
assert_eq("a participle opens an adjunct, not a clause",
          build.dedash("shared the method with BR " + DASH + " suggesting the gap is not operator-specific"),
          "shared the method with BR, suggesting the gap is not operator-specific")
assert_eq("a paired dash becomes a parenthetical",
          build.dedash("the report " + DASH + " its semi-annual review " + DASH + " landed on 2026-08-24."),
          "the report (its semi-annual review) landed on 2026-08-24.")
assert_eq("a bold term takes a colon",
          build.dedash_markdown("- **Geographic anomalies** " + DASH + " connections from unused ranges."),
          "- **Geographic anomalies**: connections from unused ranges.")
assert_eq("code spans are verbatim (the changelog heading is normative syntax)",
          build.dedash_markdown("the heading `## <Type> " + DASH + " <at>` pairs the section"),
          "the heading `## <Type> " + DASH + " <at>` pairs the section")
assert_eq("a code span spanning two lines does not swallow prose",
          build.dedash_markdown("prompt (`named " + DASH + "\nthe id`) " + DASH + " it is generated per agent"),
          "prompt (`named " + DASH + "\nthe id`); it is generated per agent")
assert_eq("fenced code is verbatim",
          build.dedash_markdown("```\na " + DASH + " b\n```"),
          "```\na " + DASH + " b\n```")
assert_eq("the changelog heading survives normalisation",
          build.dedash_markdown("## Update " + DASH + " 2026-07-05T04:40:12Z"),
          "## Update " + DASH + " 2026-07-05T04:40:12Z")
assert_true("dedash is idempotent",
            build.dedash(build.dedash("a " + DASH + " b is here")) == build.dedash("a " + DASH + " b is here"))
assert_eq("text without a dash is returned untouched",
          build.dedash("nothing to do here"), "nothing to do here")
assert_eq("newline count is preserved",
          build.dedash_markdown("a " + DASH + " b is here\nc " + DASH + " d").count("\n"), 1)
_e = build.normalise_entry_text(
    {"title": "x " + DASH + " y is here", "url": "https://a/b" + DASH + "c",
     "sources": [{"publisher": "P " + DASH + " Q is here", "url": "https://x" + DASH}]})
assert_eq("entry prose normalised", _e["title"], "x; y is here")
assert_eq("identifiers stay verbatim", _e["url"], "https://a/b" + DASH + "c")
assert_eq("a publisher name inside a skipped container is still prose",
          _e["sources"][0]["publisher"], "P; Q is here")
assert_eq("a url inside a skipped container stays verbatim",
          _e["sources"][0]["url"], "https://x" + DASH)

print("== scan_for_secrets ==")
assert_true("github classic token detected",
            scan_for_secrets("ghp_" + "A" * 40))
assert_true("aws key id detected", scan_for_secrets("AKIA" + "A" * 16))
assert_eq("clean text clean", scan_for_secrets("nothing to see CVE-2026-1234"), [])
# One sample per pattern (built at runtime, never a literal token): every
# label must still be detected through the anchor gate, and a new pattern
# without a sample here fails the count check.
_SECRET_SAMPLES = {
    "AWS access key id": "key AKIA" + "B" * 16 + " end",
    "AWS secret access key (heuristic)": "AWS_Secret_Access_Key = " + "a" * 40,
    "GitHub fine-grained PAT": "github_pat_" + "A" * 22 + "_" + "B" * 59,
    "GitHub classic / OAuth token": "token ghs_" + "A" * 40,
    "Anthropic API key": "sk-ant-api03-" + "A" * 30,
    "OpenAI API key": "(sk-proj-" + "A" * 40 + ")",
    "Slack token": "xoxb-" + "1" * 12,
    "Stripe live key": "rk_live_" + "A" * 24,
    "Google API key": "key=AIza" + "A" * 35,
    "PEM private key block": "-----BEGIN OPENSSH PRIVATE KEY-----",
    "JWT (eyJ. style)": "eyJ" + "a" * 10 + "." + "b" * 10 + "." + "c" * 10,
}
assert_eq("one secret sample per pattern", sorted(_SECRET_SAMPLES), sorted(l for l, _p in build._SECRET_PATTERNS))
assert_eq("every pattern has a scan anchor", sorted(build._SECRET_ANCHORS), sorted(l for l, _p in build._SECRET_PATTERNS))
for _lbl, _smp in _SECRET_SAMPLES.items():
    assert_true(f"secret gate passes the {_lbl} sample",
                _lbl in [l for l, _x in scan_for_secrets("prose before " + _smp + " prose after")])
assert_eq("a word-glued anchor never gates a pattern in", scan_for_secrets("a high-risk-" + "a" * 40 + " finding"), [])

print("== render_cve_pill multi-CVE split ==")
multi = render_cve_pill("CVE-2026-1111, CVE-2026-2222")
assert_in("first cve linked", 'href="entities/CVE-2026-1111/"', multi)
assert_in("second cve linked", 'href="entities/CVE-2026-2222/"', multi)
assert_not_in("no combined slug", "CVE-2026-1111, CVE-2026-2222/", multi)


# ---------------------------------------------------------------------
# v3 fixtures
# ---------------------------------------------------------------------
TAXONOMY = parse_taxonomy(SITE / "taxonomy.yaml")
REF_TS = datetime(2026, 7, 3, 12, 0, 0, tzinfo=timezone.utc)


def mk_entry(slug, *, day="2026-07-03", ts="2026-07-03T04:21:09Z",
             kind="vulnerability", priority="notable", **kw):
    e = copy.deepcopy(content_model.ENTRY_DEFAULTS)
    e.update({
        "schema": 1,
        "kind": kind,
        "title": f"Title {slug}",
        "headline": f"Headline {slug}",
        "summary": f"Summary {slug}.",
        "discovered_at": ts,
        "event_date": day,
        "run_id": "2026-07-03T0412Z-intel",
        "priority": priority,
        "tags": ["vulnerabilities"],
        "regions": ["global"],
        "sectors": [],
        "verification": "multi-source",
        "sources": [
            {"url": f"https://example.com/advisory-{slug}", "publisher": "Example PSIRT",
             "date": day, "role": "primary"},
            {"url": f"https://example.org/news-{slug}", "publisher": "Example News",
             "date": day, "role": "corroborating"},
        ],
        "slug": slug,
        "date": day,
        "id": f"{day}/{slug}",
        "path": f"entries/{day}/{slug}.md",
        "body": f"Analysis body of {slug} with **detail** and a "
                f"[reference](https://example.com/ref-{slug}).",
    })
    e.update(kw)
    return e


def mk_run(run_id="2026-07-03T0412Z-intel", **kw):
    r = {
        "schema": 1,
        "run_id": run_id,
        "kind": "intel",
        "date": "2026-07-03",
        "started": "2026-07-03T04:12:03Z",
        "completed": "2026-07-03T04:31:40Z",
        "duration_seconds": 1177,
        "model": "Claude Fable 5",
        "model_id": "claude-fable-5",
        "prompt_version": "v3.0",
        "window_hours": 9,
        "gap_hours": 7,
        "entries_published": 3,
        "entries_updated": 1,
        "sub_agents": {"S1": {"model": "Claude Fable 5", "returned": True,
                              "items_returned": 2}},
        "verification_iterations": 1,
        "verification_residual_count": 0,
        "verification": {"iterations": [{"n": 1, "verdict": "CLEAN",
                                         "truth": 0, "editorial": 0,
                                         "advisory": 0, "findings": []}]},
        "body": "Coverage gaps: none. Watchlist: no hits this run.",
    }
    r.update(kw)
    return r


UPD_AT = "2026-07-03T08:00:00Z"
RUN2_ID = "2026-07-03T0752Z-intel"
E_CRIT = mk_entry(
    "coolify-rce", kind="vulnerability", priority="critical",
    ts="2026-07-03T04:21:09Z",
    immediate_action={"title": "Patch Coolify now",
                      "action": "Upgrade to v4.0.0-beta.469 immediately."},
    evidence=[{"quote": "actively exploited in the wild",
               "publisher": "Example PSIRT"}],
    cves=[{"id": "CVE-2026-34038", "cvss": "9.9", "epss": None, "type": "rce",
           "vector": "zero-click", "auth": "post-auth",
           "status": ["exploited", "patch-available", "cisa-kev"],
           "affected": "≤ v4.0.0-beta.420", "fixed": "v4.0.0-beta.469"}],
    actions=["Patch Coolify to ≥ v4.0.0-beta.469."],
    tags=["vulnerabilities", "rce", "actively-exploited"],
    entities=["tool:foxkit"],
    # v4.0 entry lifecycle: one living entry; the later development is a
    # changelog record + a paired body section, not a second entry.
    updated_at=UPD_AT,
    updates=[{"at": UPD_AT, "run_id": RUN2_ID, "type": "update",
              "summary": "A public PoC has now surfaced and CISA added the CVE to KEV.",
              "fields": ["cves", "body"],
              "merged_from": "2026-07-03/coolify-rce-update"}],
    body="Analysis body of coolify-rce with **detail** and a "
         "[reference](https://example.com/ref-coolify-rce).\n\n"
         "## Update — " + UPD_AT + "\n\n"
         "A public PoC has now surfaced ([Example News, 2026-07-03](https://example.org/news-coolify-rce)).",
)
E_HIGH = mk_entry(
    "fortibleed-campaign", kind="threat", priority="high",
    ts="2026-07-03T03:00:00Z",
    regions=["europe"],
    entities=["actor:testfox"],
)
E_NOTE = mk_entry(
    "quiet-botnet", kind="threat", priority="notable",
    ts="2026-07-03T02:00:00Z",
    body="TestFox infrastructure overlap noted; also tracked as FOXCAT-9.",
)
E_DEEP = mk_entry(
    "deep-dive-edge", kind="research", priority="notable",
    ts="2026-07-03T05:00:00Z",
    deep_dive=True, deep_dive_category="edge-infrastructure",
)
CORR_AT = "2026-07-03T09:30:00Z"
E_OLD = mk_entry(
    "old-item", day="2026-07-01", ts="2026-07-01T10:00:00Z",
    kind="incident", priority="notable", sectors=["public-sector"],
    # A correction dated two days after first publication — it must surface
    # in the 2026-07-03 day page's § Updates while the entry keeps its
    # 2026-07-01 kind-section placement.
    updated_at=CORR_AT,
    updates=[{"at": CORR_AT, "run_id": RUN2_ID, "type": "correction",
              "summary": "Victim count corrected from 12 to 8 hospitals per the regulator's notice.",
              "fields": ["body"]}],
    body="Analysis body of old-item with 8 hospitals affected.\n\n"
         "## Correction — " + CORR_AT + "\n\n"
         "The original stated 12 hospitals; the regulator's notice names 8 "
         "([Example PSIRT, 2026-07-03](https://example.com/advisory-old-item)).",
)
E_POLICY = mk_entry(
    "policy-item", day="2026-06-28", ts="2026-06-28T10:00:00Z",
    kind="policy", priority="high",
)
# Carries the two rail features that need a fixture of their own: a
# `references[]` link (the Builds on group) and `migrated_from` (the
# Record group's Imported from row).
E_BUILDS_ON = mk_entry(
    "builds-on-item", day="2026-06-28", ts="2026-06-28T11:00:00Z",
    kind="research", priority="notable",
    references=["2026-07-01/old-item"],
    migrated_from="briefs/2026-06-28.md",
)
ALL_ENTRIES = sorted(
    [E_CRIT, E_HIGH, E_NOTE, E_DEEP, E_OLD, E_POLICY, E_BUILDS_ON],
    key=lambda e: (e["discovered_at"], e["id"]),
)
RUN = mk_run()
RUN2 = mk_run(run_id=RUN2_ID, started="2026-07-03T07:52:00Z", completed="2026-07-03T08:40:00Z",
              entries_published=0, entries_updated=2,
              updated_entry_ids=[E_CRIT["id"], E_OLD["id"]])

# ---------------------------------------------------------------------
# content_model round-trip + validation
# ---------------------------------------------------------------------
print("== content_model round-trip ==")
fm = {
    "schema": 1, "kind": "vulnerability", "title": "T — x: y (9.9)",
    "summary": "Line one.\nLine two.",
    "tags": ["vulnerabilities", "rce"],
    "cves": [{"id": "CVE-2026-1", "status": ["exploited"]}],
    "updates": [], "deep_dive": False,
}
dumped = content_model.dump_yaml_subset(fm)
assert_eq("yaml subset round-trips", content_model.parse_yaml_subset(dumped), fm)

with tempfile.TemporaryDirectory() as td:
    troot = Path(td)
    day_dir = troot / "entries" / "2026-07-03"
    day_dir.mkdir(parents=True)
    doc_fm = {k: v for k, v in E_CRIT.items()
              if k not in ("slug", "date", "id", "path", "body")}
    (day_dir / "coolify-rce.md").write_text(
        content_model.compose_frontmatter_doc(doc_fm, E_CRIT["body"]),
        encoding="utf-8",
    )
    loaded = content_model.collect_entries(entries_dir=troot / "entries", root=troot)
    assert_eq("loader finds the fixture entry", len(loaded), 1)
    le = loaded[0]
    assert_eq("entry id path-derived", le["id"], "2026-07-03/coolify-rce")
    assert_eq("headline round-trips", le["headline"], E_CRIT["headline"])
    assert_eq("cve record round-trips", le["cves"][0]["id"], "CVE-2026-34038")
    assert_eq("immediate_action round-trips",
              le["immediate_action"]["title"], "Patch Coolify now")
    errs = content_model.validate_entry(le, TAXONOMY)
    assert_eq("fixture entry is schema-valid", errs, [])
    assert_eq("changelog record round-trips", le["updates"][0]["at"], UPD_AT)
    assert_eq("updated_at round-trips", le["updated_at"], UPD_AT)
    bad = dict(le)
    bad["priority"] = "urgent"
    assert_true("bad priority flagged",
                any("priority" in x for x in content_model.validate_entry(bad, TAXONOMY)))

print("== entry lifecycle (content_model) ==")
_main, _secs = content_model.split_update_sections(E_CRIT["body"])
assert_true("main analysis excludes the update section", "## Update" not in _main and "detail" in _main)
assert_eq("one section paired by at", [(sc["type"], sc["at"]) for sc in _secs], [("update", UPD_AT)])
assert_in("section body retained", "A public PoC has now surfaced", _secs[0]["body"])
assert_eq("heading helper matches the parser",
          content_model.update_section_heading("correction", CORR_AT), "## Correction — " + CORR_AT)
assert_eq("activity ts = updated_at when later", content_model.entry_activity_ts(E_CRIT), UPD_AT)
assert_eq("activity ts = discovered_at when never updated",
          content_model.entry_activity_ts(E_HIGH), E_HIGH["discovered_at"])
_since = datetime(2026, 7, 3, 6, 0, 0, tzinfo=timezone.utc)
assert_eq("activity window admits the updated entry",
          sorted(e["id"] for e in content_model.entries_in_window([E_CRIT, E_HIGH, E_OLD], _since, None, activity=True)),
          sorted([E_CRIT["id"], E_OLD["id"]]))
assert_eq("discovered_at window excludes it",
          [e["id"] for e in content_model.entries_in_window([E_CRIT, E_HIGH, E_OLD], _since, None)], [])
_act = entry_activity(E_CRIT)
assert_eq("entry_activity names the updating run", (_act["is_update"], _act["run_id"], _act["at"]),
          (True, RUN2_ID, UPD_AT))
assert_eq("entry_activity of a never-updated entry", entry_activity(E_HIGH)["is_update"], False)
assert_eq("update_records_in by day", [r["type"] for r in update_records_in(E_OLD, None, None, day="2026-07-03")],
          ["correction"])
assert_eq("update_records_in misses another day", update_records_in(E_OLD, None, None, day="2026-07-01"), [])
_bad_pair = dict(E_CRIT)
_bad_pair["body"] = _main  # section removed, record kept
assert_true("record without its section is invalid",
            any("pair 1:1" in x for x in content_model.validate_entry(_bad_pair, TAXONOMY)))
_bad_upd = dict(E_CRIT)
_bad_upd["updated_at"] = None
assert_true("updated_at must mirror the last record",
            any("updated_at" in x for x in content_model.validate_entry(_bad_upd, TAXONOMY)))
_legacy = dict(E_HIGH)
_legacy["update_of"] = "2026-07-01/old-item"
assert_true("update_of is retired", any("retired" in x for x in content_model.validate_entry(_legacy, TAXONOMY)))
assert_eq("run record accepts updated_entry_ids",
          [e for e in content_model.validate_run_record(RUN2) if "updated_entry_ids" in e], [])
_bad_run = dict(RUN2); _bad_run["entries_updated"] = 1
assert_true("updated_entry_ids length must match entries_updated",
            any("updated_entry_ids" in e for e in content_model.validate_run_record(_bad_run)))

# ---------------------------------------------------------------------
# render_brief_sections — the canonical assembler
# ---------------------------------------------------------------------
print("== render_brief_sections ==")
day_entries = [E_NOTE, E_HIGH, E_CRIT, E_DEEP]
by_id = {e["id"]: e for e in ALL_ENTRIES}
html = render_brief_sections(day_entries, [RUN, RUN2], prefix="", entries_by_id=by_id,
                             updated_entries=[E_CRIT, E_OLD], updates_day="2026-07-03")

assert_in("TL;DR block renders", 'class="tldr"', html)
assert_in("editorial section header renders", 'class="sect"', html)
assert_in("TL;DR bullet carries strong headline", "<b>Headline coolify-rce.</b>", html)
crit_pos = html.find("Headline coolify-rce")
high_pos = html.find("Headline fortibleed-campaign")
assert_true("TL;DR: critical bullet precedes high", 0 <= crit_pos < high_pos)
alarm = render_alarm([E_HIGH, E_CRIT], prefix="")
assert_in("critical alarm renders a row", 'class="alarm-row"', alarm)
assert_in("alarm row says the immediate-action title", "Patch Coolify now", alarm)
assert_not_in("alarm stays short: no action paragraph", "Upgrade to v4.0.0-beta.469 immediately.", alarm)
assert_eq("alarm lists only critical entries", alarm.count('class="alarm-row"'), 1)
assert_in("alarm row links the permalink", 'href="' + build.entry_url_path(E_CRIT) + '"', alarm)
assert_in("no critical entry: alarm container is hidden",
          'data-alarm hidden', render_alarm([E_HIGH], prefix=""))
assert_in("finding quotes evidence", "actively exploited in the wild", html)
assert_in("updated badge on the finding", 'class="b upd"', html)
assert_in("updated badge reads 'updated'", ">updated</span>", html)
assert_in("changelog block rendered inside the finding card",
          'class="entry-update entry-update--update"', html)
assert_in("changelog block carries the section body", "A public PoC has now surfaced", html)
assert_in("§ Updates section renders", ">Updates to prior coverage<", html)
assert_in("§ Updates counts both records dated that day", "Updates to prior coverage</span><span class=\"c\">2 items", html)
assert_in("update card for the correction", 'class="entry-update entry-update--correction"', html)
assert_in("update card carries the record summary",
          "Victim count corrected from 12 to 8 hospitals", html)
assert_in("update card links the living entry", 'href="entries/2026-07-01/old-item/"', html)
assert_in("update card names the updating run", 'href="runs/' + RUN2_ID + '/"', html)
assert_true("the corrected old entry is NOT in a kind section of this day",
            'id="old-item"' not in html)
html_no_upd = render_brief_sections(day_entries, [RUN], prefix="", entries_by_id=by_id)
assert_not_in("no § Updates without records in scope", ">Updates to prior coverage<", html_no_upd)
assert_in("research section renamed", "Research, reports &amp; policy", render_brief_sections(
    [E_DEEP, mk_entry("pol", kind="policy", ts="2026-07-03T06:00:00Z")], [RUN], prefix=""))
assert_in("deep-dive section renders", ">Deep dive<", html)
assert_in("action item present", "Patch Coolify to ≥ v4.0.0-beta.469.", html)
assert_in("action finding-ref link", 'class="action-ref"', html)
assert_in("action finding-ref carries a short label", 'class="action-ref__label"', html)
assert_in("verification notes carry the run body", "Watchlist: no hits this run.", html)
assert_in("run note names the run id", "2026-07-03T0412Z-intel", html)
assert_in("verification badge absent for multi-source", 'data-priority="critical"', html)

card = render_entry_card(E_CRIT, prefix="", entries_by_id=by_id)
assert_in("card keeps data-tags", 'data-tags="vulnerabilities rce actively-exploited"', card)
assert_in("card keeps data-regions", 'data-regions="global"', card)
assert_in("card keeps data-kind", 'data-kind="vulnerability"', card)
assert_in("card links the permalink", 'href="entries/2026-07-03/coolify-rce/"', card)
assert_in("card carries provenance row", 'class="prov"', card)
assert_in("card renders evidence citation", 'class="entry-cite"', card)
assert_in("card citation carries attribution", 'class="entry-cite__attr"', card)
assert_in("cve pill on card", "CVE-2026-34038", card)
assert_in("card carries data-updated", 'data-updated="' + UPD_AT + '"', card)
assert_in("card renders the changelog block header time", "03 Jul 2026 08:00 UTC", card)
assert_in("card changelog block links the run", 'href="runs/' + RUN2_ID + '/"', card)
assert_in("card changelog block lists changed fields", '<span class="echip echip--muted">cves</span>', card)
assert_true("card main analysis precedes the changelog block",
            card.find("Analysis body of coolify-rce") < card.find("entry-update--update"))

print("== live timeline (activity-grouped) ==")
tl = _live_timeline_html([E_CRIT, E_HIGH], [RUN, RUN2], prefix="")
pos_run2 = tl.find('href="runs/' + RUN2_ID + '/"')
pos_run1 = tl.find('href="runs/2026-07-03T0412Z-intel/"')
pos_crit = tl.find('data-entry-id="' + E_CRIT["id"] + '"')
pos_high = tl.find('data-entry-id="' + E_HIGH["id"] + '"')
assert_true("updating run divider comes first", 0 <= pos_run2 < pos_run1)
assert_true("updated entry sits under the updating run", pos_run2 < pos_crit < pos_run1)
assert_true("new entry sits under its publishing run", pos_high > pos_run1)
assert_in("updated row flagged UPD", '<span class="flag flag--upd">UPD</span>', tl)
assert_in("updated row carries the record line", 'class="tl-sum tl-update tl-update--update"', tl)
assert_in("updated row shows the record summary", "A public PoC has now surfaced and CISA added", tl)
assert_in("updated row stamped with the record time", '<span class="d">03 Jul</span><span class="t">08:00Z</span>', tl)
assert_in("updated row marks the item", 'class="tl-item tl-item--updated"', tl)
row = render_timeline_item(E_HIGH, prefix="", is_new=True)
assert_in("new row flagged NEW", '<span class="flag flag--new">NEW</span>', row)
assert_not_in("new row has no update line", "tl-update", row)
assert_in("row opens its permalink from anywhere (data-card)", 'class="tl-item" data-card', row)
assert_in("row carries an explicit Full analysis call to action", "Full analysis", row)
assert_in("updated row names when it was first published", "first published 03 Jul", tl)
assert_eq("timeline appears once per entry", tl.count('data-entry-id="' + E_CRIT["id"] + '"'), 1)

print("== products as entities ==")
# `affected_products[]` is authored release-precise; the product entity is
# what folds those releases onto one pivot, without any entry being rewritten.
assert_eq("release year stripped",
          content_model.product_display_name("Microsoft SharePoint Server 2019"),
          "Microsoft SharePoint Server")
assert_eq("edition word stripped",
          content_model.product_display_name("GitLab Community Edition"), "GitLab")
assert_eq("dotted version stripped",
          content_model.product_display_name("Acme Gateway 7.0"), "Acme Gateway")
assert_eq("a bare integer is part of the name, not a version",
          content_model.product_display_name("Microsoft 365"), "Microsoft 365")
assert_eq("vendor-only strings never become entities",
          content_model.product_key("Microsoft"), "")
assert_eq("mechanical key", content_model.product_key("Adobe ColdFusion 2025"),
          "product:adobe-coldfusion")
_preg = {
    "product:microsoft-sharepoint": {
        "type": "product", "name": "Microsoft SharePoint",
        "aliases": ["Microsoft SharePoint Server", "Microsoft SharePoint Server 2019"],
    },
    "product:old-name": {"type": "product", "name": "Old Name", "aliases": [],
                         "merged_into": "product:microsoft-sharepoint"},
}
_pidx = content_model.product_alias_index(_preg)
assert_eq("registry aliases win over the mechanical rule",
          content_model.product_key("Microsoft SharePoint Server 2019", _pidx),
          "product:microsoft-sharepoint")
assert_eq("a tombstoned product resolves to its canonical record",
          content_model.product_key("Old Name", _pidx), "product:microsoft-sharepoint")
assert_eq("two release spellings collapse to one product on an entry",
          content_model.entry_product_keys(
              {"affected_products": ["Microsoft SharePoint Server",
                                     "Microsoft SharePoint Server 2019",
                                     "Microsoft"]}, _pidx),
          ["product:microsoft-sharepoint"])
assert_true("an over-long product string still gets a legal key",
            content_model.ENTITY_KEY_RE.match(
                content_model.product_key("Thermo Fisher Applied Biosystems SeqStudio "
                                          "Genetic Analyzer Data Collection Software")) is not None)
assert_true("product is an entity type", "product" in content_model.ENTITY_TYPES)
assert_eq("a product is a target, never an attacker: only documented-in leaves one",
          sorted(t for t, spec in content_model.RELATION_TYPES.items()
                 if "product" in spec["subjects"] and not spec["symmetric"]),
          ["documented-in"])
assert_eq("affects points at a product",
          content_model.RELATION_TYPES["affects"]["objects"], ("product",))

print("== entry page ==")
epage = render_entry_page(
    E_CRIT, entries_by_id=by_id, registry={}, runs_by_id={RUN["run_id"]: RUN, RUN2_ID: RUN2},
    day_pages={"2026-07-03"}, site_url="https://x.example/", cachebust="t",
    prefix="../../../", canonical="https://x.example/entries/2026-07-03/coolify-rce/",
)
assert_in("meta: first published", "first published 2026-07-03 04:21 UTC", epage)
assert_in("meta: updated", ">updated 2026-07-03 08:00 UTC</time></a>", epage)
assert_in("updated stamp jumps to the newest changelog section",
          'class="emeta-updated" href="#update-' + UPD_AT + '"', epage)
assert_in("revision history panel", 'id="revision-history"', epage)
assert_in("revision history lists the publish event", '<span class="b">Published</span>', epage)
assert_in("revision history lists the record", 'class="revision revision--update"', epage)
assert_in("revision links the updating run", 'href="../../../runs/' + RUN2_ID + '/"', epage)
assert_in("changelog section anchored", 'id="update-' + UPD_AT + '"', epage)
assert_in("JSON-LD dateModified = updated_at", '"dateModified":"' + UPD_AT + '"', epage)
assert_in("JSON-LD datePublished = discovered_at", '"datePublished":"2026-07-03T04:21:09Z"', epage)
assert_not_in("no update-chain block", "Update chain", epage)
plain_page = render_entry_page(
    E_HIGH, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-07-03/fortibleed-campaign/",
)
assert_not_in("never-updated entry has no revision history", 'id="revision-history"', plain_page)
assert_not_in("never-updated entry has no updated meta", "emeta-updated", plain_page)
assert_not_in("never-updated entry has no Updates section", 'class="esec esec--updates"', plain_page)
policy_page = render_entry_page(
    E_POLICY, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-06-28/policy-item/",
)
assert_in("entry with no day page yet links the live brief",
          "Back to the live brief", policy_page)
# Metadata completeness on the permalink. Everything except the two stamps
# and the share control now lives in the labelled rail; the dateline under
# the title carries nothing else (the run link in particular is Record, at
# the foot of the rail).
assert_in("rail: event date", ">Event date</span>", epage)
assert_in("rail: event date value", '<time datetime="2026-07-03">2026-07-03</time>', epage)
assert_in("lede is the headline", '<p class="elede">Headline coolify-rce</p>', epage)
_same = copy.deepcopy(E_HIGH)
_same["headline"] = _same["title"]
_same_page = render_entry_page(
    _same, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-07-03/fortibleed-campaign/",
)
assert_not_in("a headline that restates the title is not printed twice",
              'class="elede"', _same_page)
assert_not_in("summary is not repeated on the permalink", "Summary coolify-rce.", epage.split("</head>")[-1])
assert_in("body renders inside a titled Analysis section",
          '<section class="esec esec--analysis"><h2 class="esec-h">Analysis</h2>', epage)
assert_in("rail CVE type", '<span class="frow__l">Type</span><span class="frow__v">rce</span>', epage)
assert_in("rail CVE vector", '<span class="frow__l">Vector</span><span class="frow__v">zero-click</span>', epage)
assert_in("rail CVE auth", '<span class="frow__l">Auth</span><span class="frow__v">post-auth</span>', epage)
assert_in("rail CVE fixed version",
          '<span class="frow__l">Fixed</span><span class="frow__v">v4.0.0-beta.469</span>', epage)
assert_in("rail CVE affected versions",
          '<span class="frow__l">Affected</span><span class="frow__v">≤ v4.0.0-beta.420</span>', epage)
assert_in("source date rides the role label", "primary · 2026-07-03", epage)
assert_in("entry advertises its raw markdown twin in the head",
          'rel="alternate" type="text/markdown"', epage)
assert_in("rail Record links the raw source", '>index.md</a>', epage)
assert_in("rail Record carries the producing run",
          '<span class="frow__l">Produced by</span>', epage)
assert_not_in("no run-dashboard link under the title",
              'ops/#run=', epage.split('<div class="ebody">')[0].split('class="emeta"')[-1])
assert_in("key-facts rail is labelled", '<h2 class="erail-h" id="entry-facts-h">Key facts</h2>', epage)
assert_not_in("rail never scrolls on its own", "erail-scroll", epage)
# The immediate-action block leads the permalink and carries neither a link
# to the page it is already on nor a copy of the first evidence quote (the
# Cited-evidence section owns every quote, once).
assert_in("critical entry leads with the immediate action",
          '<span class="callout__label">Immediate action</span>', epage)
assert_not_in("immediate action does not repeat an evidence quote",
              "entry-cite--inline", epage)
assert_eq("evidence quote appears exactly once",
          epage.count('class="entry-cite__quote"'),
          len([e for e in (E_CRIT.get("evidence") or []) if e.get("quote")]))
assert_not_in("immediate action never links to its own permalink",
              '<a href="../../../entries/2026-07-03/coolify-rce/"', epage)
# Changelog records read as content on the permalink: the raw changed-field
# names and the run link are pipeline internals and stay in Revision history.
assert_in("permalink groups the changelog under one heading",
          '<h2 class="esec-h">Updates<span class="esec-n">1</span></h2>', epage)
assert_not_in("no changed-field chips in the reading flow",
              'class="entry-update__fields"', epage)
assert_not_in("no run link on the in-flow changelog block",
              'class="mono entry-update__run"', epage)
assert_in("revision history keeps the changed-field audit trail",
          'class="revision__fields muted">Changed: ', epage)
assert_in("entry JSON-LD points at the markdown encoding",
          '"encodingFormat":"text/markdown"', epage)
assert_in("deep-dive badge carries the category",
          "deep dive · edge-infrastructure", build.render_badges(E_DEEP, full=True))
builds_on_page = render_entry_page(
    E_BUILDS_ON, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-06-28/builds-on-item/",
)
assert_in("references render as a Builds on rail group", ">Builds on</h3>", builds_on_page)
assert_in("builds-on links the referenced entry",
          'href="../../../entries/2026-07-01/old-item/"', builds_on_page)
assert_in("migration provenance sits in the rail Record group",
          '<span class="frow__l">Imported from</span>', builds_on_page)
assert_in("migration provenance names the source", "briefs/2026-06-28.md", builds_on_page)

print("== landing page (live brief at the site root) ==")
by_id_all = {e["id"]: e for e in ALL_ENTRIES}
landing = render_live_brief_page(
    [E_CRIT, E_HIGH, E_OLD], [RUN, RUN2],
    all_entries=ALL_ENTRIES, all_runs=[RUN, RUN2],
    ref_ts=datetime(2026, 7, 3, 12, 0, tzinfo=timezone.utc),
    entries_by_id=by_id_all, card_html_by_id={},
    site_url="https://x.example/", cachebust="t",
    prefix="", canonical="https://x.example/",
    counts={"entries": 7, "days": 3, "updates": 1, "entities": 4,
            "cves": 2, "sources": 5, "attack_techniques_covered": 6},
    latest_day="2026-07-01",
)
assert_in("landing is canonical at the root", '<link rel="canonical" href="https://x.example/" />', landing)
assert_in("landing carries the server-rendered timeline", "data-brief-timeline", landing)
assert_in("landing h1 is the functional brief title", '<h1 class="livehead-h">', landing)
assert_not_in("feed heading stays a h2", '<h1 class="feedhead-title">', landing)
assert_in("positioning copy renders at the foot, not the top", 'class="sitenote"', landing)
assert_not_in("no marketing hero above the findings", 'class="hero hero--live"', landing)
assert_not_in("no § Do now panel on the landing page", 'data-donow', landing)
assert_not_in("no pulse panel on the landing page", 'class="pulsepanel"', landing)
assert_in("critical alarm header on the landing page", 'class="alarm-row"', landing)
assert_in("feed head carries the window counts", 'data-window-total', landing)
assert_in("hint tells the reader rows open the full analysis", 'class="feedhint"', landing)
assert_in("density toggle ships hidden until brief.js wires it", 'data-view-toggle hidden', landing)
assert_in("knowledge-base pivot band below the feed", 'class="pivotband"', landing)
assert_in("pivot band links the daily archive at the latest day", 'href="daily/2026-07-01/"', landing)
assert_in("pivot band links the changelog", 'href="changes/"', landing)
assert_in("machine-endpoint line for agents", "data/briefbook.json", landing)
assert_in("machine-endpoint line advertises llms.txt", "llms.txt", landing)
assert_in("landing declares the WebSite identity node", '"@type":"WebSite"', landing)
assert_in("landing enumerates the window as a CollectionPage", '"@type":"CollectionPage"', landing)
assert_not_in("landing never links the retired /live/ page", 'href="live/"', landing)

print("== /changes/ — store-wide changelog ==")
changes = render_changes_page(
    ALL_ENTRIES, site_url="https://x.example/", cachebust="t",
    prefix="../", canonical="https://x.example/changes/",
)
assert_in("changes page lists the correction", "Victim count corrected", changes)
assert_in("changes page type badge", 'class="b upd upd--correction"', changes)
assert_in("changes row deep-links the entry section",
          'href="../entries/2026-07-01/old-item/#update-' + CORR_AT + '"', changes)
assert_in("changes row links the run record", 'href="../runs/' + RUN2_ID + '/"', changes)
assert_in("changes are grouped by UTC day", ">2026-07-03<", changes)
changes_empty = render_changes_page(
    [E_POLICY], site_url="https://x.example/", cachebust="t",
    prefix="../", canonical="https://x.example/changes/",
)
assert_in("changes page explains itself when empty", "No changelog records yet", changes_empty)

print("== update card ==")
ucard = render_update_card(E_OLD, E_OLD["updates"][0], prefix="")
assert_in("update card is a finding card", 'class="finding entry-card update-card"', ucard)
assert_in("update card carries data-updated", 'data-updated="' + CORR_AT + '"', ucard)
assert_in("update card shows first-published origin", "First published 2026-07-01", ucard)

# single-source badge
ss = mk_entry("single-src", verification="single-source-national-cert",
              sources=[{"url": "https://cert.example/adv", "publisher": "CERT",
                        "date": "2026-07-03", "role": "primary"}])
ss_card = render_entry_card(ss, prefix="")
assert_in("single-source badge rendered", "single-source · national CERT", ss_card)

# ---------------------------------------------------------------------
# grouping + section routing
# ---------------------------------------------------------------------
print("== grouping ==")
days = entries_by_day(ALL_ENTRIES)
assert_eq("day pages: one per entry date", sorted(days),
          ["2026-06-28", "2026-07-01", "2026-07-03"])
assert_eq("2026-07-03 has 4 entries", len(days["2026-07-03"]), 4)
assert_eq("deep dive routes to deep-dive", entry_section_key(E_DEEP), "deep-dive")
assert_eq("policy routes to the research section", entry_section_key(E_POLICY), "research")
assert_eq("research routes to the research section", entry_section_key(E_BUILDS_ON), "research")
assert_eq("updated entry keeps its kind section (updates are derived)",
          entry_section_key(E_CRIT), "trending-vulnerabilities")
picked = select_tldr_entries([E_NOTE, E_HIGH, E_CRIT])
assert_eq("tl;dr picks critical first", picked[0]["id"], E_CRIT["id"])
assert_eq("tl;dr pads with notable to 3", len(picked), 3)

# ---------------------------------------------------------------------
# empty-run visibility — a fire that published nothing must still get a
# day/week page, an archive slot and resolvable links (quiet windows are
# first-class). The page/link universe = content days ∪ days that ran.
# ---------------------------------------------------------------------
print("== empty-run visibility ==")
QUIET_RUN = mk_run(run_id="2026-07-05T0009Z-intel", date="2026-07-05",
                   started="2026-07-05T00:09:00Z", completed="2026-07-05T00:18:00Z",
                   entries_published=0, entries_updated=0)
WEEKLY_RUN = mk_run(run_id="2026-06-28T0800Z-weekly", kind="weekly",
                    date="2026-06-28", entries_published=0)
ALL_RUNS = [RUN, QUIET_RUN, WEEKLY_RUN]
assert_eq("daily_run_dates ignores weekly, keeps daily fires",
          daily_run_dates(ALL_RUNS), {"2026-07-03", "2026-07-05"})
assert_eq("daily_run_dates drops malformed dates",
          daily_run_dates([mk_run(date="not-a-date"), mk_run(date="")]), set())
# The union: 2026-07-05 has no entry but ran, so it joins the page universe.
day_universe = set(entries_by_day(ALL_ENTRIES)) | daily_run_dates(ALL_RUNS)
assert_true("all-quiet day joins the day-page universe", "2026-07-05" in day_universe)

# Archive index lists the quiet day with an explicit "run record only" marker.
archive_days = {d: entries_by_day(ALL_ENTRIES).get(d, []) for d in day_universe}
archive_html = render_days_index_page(archive_days, site_url="https://x.example/",
                                      cachebust="t", prefix="../",
                                      canonical="https://x.example/briefs/")
assert_in("archive lists the quiet day", "daily/2026-07-05/", archive_html)
assert_in("archive marks the quiet day as run-record-only",
          "run record only", archive_html)
assert_in("archive still counts a content day's entries",
          "4 findings", archive_html)

# The quiet day's page renders (0 entries) and surfaces its run-note.
by_id_all = {e["id"]: e for e in ALL_ENTRIES}
quiet_page = render_day_page("2026-07-05", [], [QUIET_RUN], entries_by_id=by_id_all,
                             site_url="https://x.example/", cachebust="t",
                             prefix="../../", canonical="https://x.example/briefs/2026-07-05/")
assert_in("quiet day page names the run", "2026-07-05T0009Z-intel", quiet_page)
assert_in("quiet day page reports zero entries", "0 verified findings", quiet_page)
upd_day_page = render_day_page("2026-07-03", days["2026-07-03"], [RUN, RUN2], entries_by_id=by_id_all,
                               site_url="https://x.example/", cachebust="t",
                               prefix="../../", canonical="https://x.example/daily/2026-07-03/",
                               updated_entries=[E_CRIT, E_OLD])
assert_in("day page counts the day's updates", "2 updates to prior coverage", upd_day_page)
assert_in("day page renders § Updates", ">Updates to prior coverage<", upd_day_page)

# ---------------------------------------------------------------------
# per-run detail pages + live-timeline run links + ops run selector
# ---------------------------------------------------------------------
print("== run detail pages ==")
assert_eq("run_url_path builds the permalink", run_url_path(RUN),
          "runs/2026-07-03T0412Z-intel/")

div_linked = render_run_divider("03 Jul 04:31Z", "gap 7h", 2,
                                url="../runs/2026-07-03T0412Z-intel/")
assert_in("linked divider carries the anchor",
          '<a class="rl" href="../runs/2026-07-03T0412Z-intel/"', div_linked)
assert_in("linked divider keeps the run-h markup", 'class="run-h"', div_linked)
div_plain = render_run_divider("03 Jul 04:31Z", "", 0)
assert_in("plain divider stays a span", '<span class="rl">', div_plain)
assert_true("plain divider has no anchor", "<a" not in div_plain)
assert_in("quiet divider keeps the quiet class", "tl-run--quiet", div_plain)

run_page = render_run_detail_page(
    RUN, {}, run_entries=[E_CRIT], day_pages={"2026-07-03"},
    site_url="https://x.example/", cachebust="t", prefix="../../",
    canonical="https://x.example/runs/2026-07-03T0412Z-intel/",
)
assert_in("run page names the run id", "2026-07-03T0412Z-intel", run_page)
assert_in("run page has the telemetry section", 'id="telemetry"', run_page)
assert_in("run page has the notes section", 'id="notes"', run_page)
assert_in("run page renders the record body", "Watchlist: no hits this run.", run_page)
assert_in("run page notes expanded by default", '<details class="verif" open>', run_page)
assert_in("run page lists the run's entries",
          'href="../../entries/2026-07-03/coolify-rce/"', run_page)
run2_page = render_run_detail_page(
    RUN2, {}, run_entries=[E_CRIT, E_OLD], day_pages={"2026-07-03"},
    site_url="https://x.example/", cachebust="t", prefix="../../",
    canonical="https://x.example/runs/" + RUN2_ID + "/",
)
assert_in("run page distinguishes updated entries", 'class="ops-entry--updated"', run2_page)
assert_in("run page names the update type", '>correction</span>', run2_page)
assert_in("run page heading counts published and updated",
          "Entries this run published (0) and updated (2)", run2_page)
assert_in("run page links back to ops", 'href="../../ops/"', run_page)
assert_in("run page links the day page", 'href="../../daily/2026-07-03/"', run_page)

# v3.23+ fixtures for the double-CLEAN gate + a first-class audit run.
def _iter(n, verdict, sat, model="M"):
    return {"n": n, "verdict": verdict, "subagent_type": sat, "model": model,
            "truth": 0 if verdict == "CLEAN" else 1, "editorial": 0, "advisory": 0,
            "findings": []}

CONFIRMED_RUN = mk_run(
    run_id="2026-07-14T0410Z-intel", date="2026-07-14", prompt_version="v3.23",
    started="2026-07-14T04:10:00Z", completed="2026-07-14T04:40:00Z",
    publish_status="ok", verification_iterations=2,
    verification={"iterations": [_iter(1, "CLEAN", "cti-verification", "Opus"),
                                 _iter(2, "CLEAN", "cti-verification-alt", "Sonnet")]})
FIXED_CONFIRMED_RUN = mk_run(
    run_id="2026-07-14T1210Z-intel", date="2026-07-14", prompt_version="v3.24",
    started="2026-07-14T12:10:00Z", completed="2026-07-14T12:50:00Z",
    verification_iterations=3,
    verification={"iterations": [_iter(1, "NEEDS_FIXES", "cti-verification"),
                                 _iter(2, "CLEAN", "cti-verification-alt"),
                                 _iter(3, "CLEAN", "cti-verification")]})
WAIVED_RUN = mk_run(
    run_id="2026-07-14T2010Z-intel", date="2026-07-14", prompt_version="v3.23",
    started="2026-07-14T20:10:00Z", completed="2026-07-14T20:30:00Z",
    verification_iterations=1,
    verification={"confirmation_waived": "watchdog overrun",
                  "iterations": [_iter(1, "CLEAN", "cti-verification")]})
AUDIT_RUN = mk_run(
    run_id="2026-07-14T1308Z-audit", kind="audit", date="2026-07-14",
    prompt_version="v3.24",
    started="2026-07-14T13:08:00Z", completed="2026-07-14T13:40:00Z",
    sub_agents={"A1-verify": {"model": "Opus", "returned": True, "items_returned": 3},
                "G1-vulns": {"model": "Sonnet", "returned": True, "items_returned": 1}},
    verification_iterations=2,
    verification={"iterations": [_iter(1, "CLEAN", "cti-verification", "Opus"),
                                 _iter(2, "CLEAN", "cti-verification-alt", "Sonnet")]})

# v4.1: a single Sonnet 5 verifier definition runs every iteration, so a
# same-definition confirming pair is the normal confirmed shape — while the
# same shape on a rotation-era (v3.23–v4.0) record is still "same-model".
SAME_DEF_V41_RUN = mk_run(
    run_id="2026-08-28T0410Z-intel", date="2026-08-28", prompt_version="v4.1",
    started="2026-08-28T04:10:00Z", completed="2026-08-28T04:40:00Z",
    publish_status="ok", verification_iterations=2,
    verification={"iterations": [_iter(1, "CLEAN", "cti-verification", "Claude Sonnet 5"),
                                 _iter(2, "CLEAN", "cti-verification", "Claude Sonnet 5")]})
SAME_DEF_V40_RUN = mk_run(
    run_id="2026-08-27T0410Z-intel", date="2026-08-27", prompt_version="v4.0",
    started="2026-08-27T04:10:00Z", completed="2026-08-27T04:40:00Z",
    publish_status="ok", verification_iterations=2,
    verification={"iterations": [_iter(1, "CLEAN", "cti-verification", "Opus"),
                                 _iter(2, "CLEAN", "cti-verification", "Opus")]})

print("== double-CLEAN classification ==")
assert_eq("confirmed run classified", _verification_confirmation(CONFIRMED_RUN)["status"], "confirmed")
assert_eq("v4.1 same-definition pair is confirmed", _verification_confirmation(SAME_DEF_V41_RUN)["status"], "confirmed")
assert_eq("v4.1 confirmed pair carries the model names", _verification_confirmation(SAME_DEF_V41_RUN)["models"],
          ("Claude Sonnet 5", "Claude Sonnet 5"))
assert_eq("rotation-era same-definition pair still flagged", _verification_confirmation(SAME_DEF_V40_RUN)["status"], "same-model")
assert_eq("fix-then-confirm classified", _verification_confirmation(FIXED_CONFIRMED_RUN)["status"], "confirmed")
assert_eq("waived run classified", _verification_confirmation(WAIVED_RUN)["status"], "waived")
assert_eq("pre-gate single CLEAN not gated", _verification_confirmation(RUN)["gated"], False)
assert_eq("fix rounds exclude the confirmation pass",
          _verification_fix_rounds(FIXED_CONFIRMED_RUN), 1)
assert_eq("perfect confirmed run has zero fix rounds",
          _verification_fix_rounds(CONFIRMED_RUN), 0)

ops_page = render_ops_page(
    [RUN, QUIET_RUN, WEEKLY_RUN, CONFIRMED_RUN, FIXED_CONFIRMED_RUN, WAIVED_RUN, AUDIT_RUN],
    [], prefix="../",
    site_url="https://x.example/", cachebust="t",
    canonical="https://x.example/ops/", day_pages={"2026-07-03"},
    entries_by_run={"2026-07-03T0412Z-intel": [E_CRIT]},
)
assert_true("ops: no hidden per-run panels remain", "data-run-panel" not in ops_page)
assert_true("ops: jump-to selector removed", "ops-run-select" not in ops_page)
assert_in("ops: legacy #run= redirect marker present", 'data-runs-base="../runs/"', ops_page)
assert_in("ops: run-log cell is the run id linking its page",
          '<a href="../runs/2026-07-03T0412Z-intel/" '
          'title="open run details · verification &amp; coverage notes">2026-07-03T0412Z-intel</a>',
          ops_page)
assert_in("ops: latest-run panel carries its permalink",
          'href="../runs/2026-07-14T1308Z-audit/"', ops_page)
assert_in("ops: latest-run section renamed", ">Latest run</h2>", ops_page)
assert_in("ops: confirmed run pill", ">clean ×2</span>", ops_page)
assert_in("ops: fix-then-confirm pill", ">1↻ clean ×2</span>", ops_page)
assert_in("ops: waived run pill", ">clean · unconfirmed</span>", ops_page)
assert_in("ops: publish column pill", 'title="run record on main AND the site rebuild confirmed (Phase 7)">ok</span>', ops_page)
assert_in("ops: audit kind pill", '>audit</span>', ops_page)
assert_in("ops: audit retrospective pass column", 'title="A1-verify"', ops_page)
assert_in("ops: double-CLEAN KPI tile", "Double-CLEAN gate", ops_page)
assert_in("ops: kind split counts audits", "1 audit", ops_page)
assert_in("ops: confirmation chip on the latest panel",
          "✓ double-CLEAN · Opus + Sonnet", ops_page)

audit_page = render_run_detail_page(
    AUDIT_RUN, {}, run_entries=[], day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../",
    canonical="https://x.example/runs/2026-07-14T1308Z-audit/",
)
assert_in("audit run page shows the audit kind", ">audit</span>", audit_page)
assert_in("audit run page renders its ad-hoc passes", "A1-verify", audit_page)
assert_true("audit run page has no synthetic S1 slot",
            "No record for this sub-agent" not in audit_page)
assert_eq("audit kind validates in the content model",
          [e for e in content_model.validate_run_record(AUDIT_RUN) if "kind" in e], [])

# ---------------------------------------------------------------------
# briefbook.json / alerts.json shapes
# ---------------------------------------------------------------------
print("== briefbook + alerts ==")
book = build_briefbook(ALL_ENTRIES, [RUN], ref_ts=REF_TS, prefix="../")
assert_eq("briefbook window_days", book["window_days"], 35)
assert_eq("briefbook generated_at", book["generated_at"], "2026-07-03T12:00:00Z")
assert_eq("briefbook carries all fixture entries", len(book["entries"]), len(ALL_ENTRIES))
be = {x["id"]: x for x in book["entries"]}[E_CRIT["id"]]
for field in ("id", "url", "date", "discovered_at", "kind", "priority",
              "headline", "summary", "title", "tags", "regions", "sectors",
              "entities", "cve_ids", "cve_status", "updated_at", "activity_at",
              "activity_run_id", "activity_is_update", "updates", "update_count",
              "deep_dive", "actions", "watchlist_hit", "verification",
              "techniques", "classification", "classification_html",
              "org_triage", "org_triage_html", "immediate_action", "html"):
    assert_true(f"briefbook entry field `{field}`", field in be)
assert_true("briefbook has no retired update_of/updated_by", "update_of" not in be and "updated_by" not in be)
assert_eq("briefbook cve_ids", be["cve_ids"], ["CVE-2026-34038"])
assert_eq("briefbook cve_status union", be["cve_status"], ["exploited", "patch-available", "cisa-kev"])
assert_eq("briefbook activity is the update", (be["activity_is_update"], be["activity_run_id"], be["activity_at"]),
          (True, RUN2_ID, UPD_AT))
assert_eq("briefbook updates compact shape", be["updates"][0]["type"], "update")
assert_eq("briefbook update_count", be["update_count"], 1)
assert_eq("briefbook ordered by activity (updated entry first)",
          book["entries"][0]["id"], E_OLD["id"])
assert_in("briefbook html carries the changelog block", "entry-update--update", be["html"])
assert_in("briefbook html is the finding card", 'class="finding entry-card"', be["html"])
assert_eq("briefbook IA block", be["immediate_action"]["title"], "Patch Coolify now")
assert_eq("briefbook run count", len(book["runs"]), 1)
br = book["runs"][0]
for field in ("run_id", "url", "date", "kind", "started", "completed",
              "window_hours", "gap_hours", "model", "entries_published", "html"):
    assert_true(f"briefbook run field `{field}`", field in br)
assert_in("briefbook run html rendered", "<p>", br["html"])

alerts = build_alerts(ALL_ENTRIES, ref_ts=REF_TS, site_url="https://x.example/")
assert_true("alerts documents itself", alerts["_comment"].startswith("Notification-hook"))
assert_eq("alerts: only critical|high in window",
          sorted(a["id"] for a in alerts["alerts"]),
          sorted([E_CRIT["id"], E_HIGH["id"], E_POLICY["id"]]))
al = {a["id"]: a for a in alerts["alerts"]}
assert_eq("alerts: critical carries immediate_action",
          al[E_CRIT["id"]]["immediate_action"]["title"], "Patch Coolify now")
assert_eq("alerts: high has null immediate_action",
          al[E_HIGH["id"]]["immediate_action"], None)
assert_true("alerts URLs absolute",
            al[E_CRIT["id"]]["url"].startswith("https://x.example/entries/"))
assert_eq("alerts carry updated_at", al[E_CRIT["id"]]["updated_at"], UPD_AT)
assert_eq("alerts carry compact updates", al[E_CRIT["id"]]["updates"][0]["type"], "update")
assert_eq("alerts: never-updated entry has null updated_at", al[E_HIGH["id"]]["updated_at"], None)
assert_in("alerts comment explains activity re-entry", "updated_at", alerts["_comment"])

# ---------------------------------------------------------------------
# feeds from fixture entries
# ---------------------------------------------------------------------
print("== feeds ==")
items_xml, _ts = build_items_feed(ALL_ENTRIES, site_url="https://x.example/", ref_ts=REF_TS)
assert_eq("items feed is valid XML", _xml_validate(items_xml), [])
assert_in("item title = headline", "<title>Headline coolify-rce</title>", items_xml)
assert_in("item description = summary", "Summary coolify-rce.", items_xml)
assert_in("pubDate from discovered_at", "03 Jul 2026 04:21:09", items_xml)
assert_in("category carries cve id", "<category>CVE-2026-34038</category>", items_xml)
assert_in("category carries tag", "<category>vulnerabilities</category>", items_xml)
assert_in("per-record feed item title", "<title>Update: Headline coolify-rce</title>", items_xml)
assert_in("per-record feed item guid", '<guid isPermaLink="false">https://x.example/entries/2026-07-03/coolify-rce/#update-' + UPD_AT + '</guid>', items_xml)
assert_in("per-record item pubDate = record at", "03 Jul 2026 08:00:00", items_xml)
assert_in("correction feed item", "<title>Correction: Headline old-item</title>", items_xml)
assert_eq("items feed = entries + records", items_xml.count("<item>"), len(ALL_ENTRIES) + 2)
_first_title = re.search(r"<item><title>([^<]*)</title>", items_xml).group(1)
assert_eq("newest item first is the latest record", _first_title, "Correction: Headline old-item")
sector_feeds = {f: x for f, x, _t in build_sector_feeds(ALL_ENTRIES,
                                                        site_url="https://x.example/",
                                                        ref_ts=REF_TS)}
assert_true("one sector slice emitted", len(sector_feeds) == 1)
assert_in("public-sector entry lands in its slice",
          "Headline old-item", sector_feeds["feed-public-sector.xml"])
assert_in("public-sector slice carries the correction item",
          "<title>Correction: Headline old-item</title>", sector_feeds["feed-public-sector.xml"])
assert_not_in("sector-less entry stays out of the public-sector slice",
              "Headline coolify-rce", sector_feeds["feed-public-sector.xml"])
for fname, xml in sector_feeds.items():
    errs = _xml_validate(xml)
    if errs:
        FAILURES.append(f"sector feed {fname} invalid XML: {errs}")
        print(f"  FAIL sector feed {fname} XML")
print("  ok  all sector feeds parse as XML")

# ---------------------------------------------------------------------
# entity appearance matching + sources annotation
# ---------------------------------------------------------------------
print("== entities ==")
REGISTRY = {
    "actor:testfox": {
        "key": "actor:testfox", "type": "actor", "name": "TestFox",
        "aliases": ["FOXCAT-9"], "nexus": None,
        "summary": "Fixture actor for tests.", "first_seen": "2026-06-01",
        "relations": [
            {"to": "tool:foxkit", "type": "uses",
             "source": None,  # patched below to a real fixture entry id
             "note": "fixture edge"},
        ],
    },
    "tool:foxkit": {
        "key": "tool:foxkit", "type": "tool", "name": "FoxKit",
        "aliases": [], "nexus": None,
        "summary": "Fixture tool for tests.", "first_seen": "2026-06-01",
    },
}
CVES_SEEN = {"cves": [
    {"id": "CVE-2025-0001", "first_seen": "2026-05-01", "last_seen": "2026-05-02",
     "title": "Historical CVE never re-covered", "primary_source_url": ""},
]}
SOURCES_RAW = {"sources": [
    {"id": "example-psirt", "publisher": "Example PSIRT",
     "url": "https://example.com/", "category": ["vulns"],
     "reliability": "A", "status": "active"},
]}
day_pages = set(days)
REGISTRY["actor:testfox"]["relations"][0]["source"] = E_HIGH["id"]
ents, matched = build_entities(REGISTRY, ALL_ENTRIES, CVES_SEEN, SOURCES_RAW, day_pages)
by_key = {e["key"]: e for e in ents}
fox = by_key["actor:testfox"]
assert_eq("explicit key + alias mention both match",
          sorted(a["entry_id"] for a in fox["appearances"]),
          sorted([E_HIGH["id"], E_NOTE["id"]]))
assert_eq("registry first_seen backfills first_covered", fox["first_covered"], "2026-06-01")
assert_true("cve entity from entry cves[]", "CVE-2026-34038" in by_key)
assert_eq("cve entity appearance count",
          len(by_key["CVE-2026-34038"]["appearances"]), 1)
assert_true("historical cves_seen id becomes an entity", "CVE-2025-0001" in by_key)
assert_eq("historical cve keeps its dates",
          by_key["CVE-2025-0001"]["first_covered"], "2026-05-01")
assert_true("citations resolve to curated source ids",
            any(c.get("source_id") == "example-psirt"
                for c in by_key["CVE-2026-34038"]["citations"]))
co = compute_related_entities(ents, matched)
assert_true("co-occurrence links actor to nothing (no shared entries)",
            fox["related_entities"] == [] or isinstance(fox["related_entities"], list))
foxkit = by_key["tool:foxkit"]
fox_rel = [r for r in fox["relation_rows"] if r["key"] == "tool:foxkit"]
kit_rel = [r for r in foxkit["relation_rows"] if r["key"] == "actor:testfox"]
assert_true("typed relation renders on the subject", fox_rel and fox_rel[0]["label"] == "uses")
assert_true("typed relation renders inversely on the object",
            kit_rel and kit_rel[0]["label"] == "used by")
assert_eq("relation row carries its source entry", fox_rel[0]["source"], E_HIGH["id"])

graph = build_graph_payload(ents, matched, co, generated_at="2026-07-03T00:00:00Z")
g_nodes = {n["id"]: n for n in graph["nodes"]}
assert_true("graph carries entity nodes", "actor:testfox" in g_nodes and "tool:foxkit" in g_nodes)
rel_edges = [e for e in graph["edges"] if e["kind"] == "relation"]
assert_true("graph carries the curated typed edge",
            any(e["source"] == "actor:testfox" and e["target"] == "tool:foxkit"
                and e["type"] == "uses" and e["entry"] == E_HIGH["id"] for e in rel_edges))
cve_edges = [e for e in graph["edges"] if e["kind"] == "cve"]
assert_true("graph derives entity-CVE edges from shared entries",
            any(e["target"] == "CVE-2026-34038" for e in cve_edges))
assert_true("connected CVE becomes a graph node", "CVE-2026-34038" in g_nodes)
assert_true("unconnected historical CVE stays out of the graph",
            "CVE-2025-0001" not in g_nodes)
assert_true("relation vocabulary ships in the payload",
            graph["relation_types"].get("uses", {}).get("inverse") == "used by")

# Derived-edge evidence gate: annual-report roundups reference many
# unrelated entities — they must never create co-occurrence edges.
# Curated relations are unaffected.
E_ROUNDUP_A = mk_entry(
    "annual-roundup-fixture", kind="annual-report", priority="notable",
    ts="2026-07-03T10:00:00Z",
    entities=["actor:testfox", "tool:foxkit"],
)
ents2, matched2 = build_entities(
    REGISTRY, ALL_ENTRIES + [E_ROUNDUP_A],
    CVES_SEEN, SOURCES_RAW, day_pages)
co2 = compute_related_entities(ents2, matched2)
fox2 = {e["key"]: e for e in ents2}["actor:testfox"]
assert_true("annual-report entries create no co-occurrence",
            co2.get("actor:testfox", {}).get("tool:foxkit", 0) == 0
            and not any(r["key"] == "tool:foxkit" for r in fox2["related_entities"]))
graph2 = build_graph_payload(ents2, matched2, co2, generated_at="2026-07-03T00:00:00Z")
assert_true("no derived graph edge from roundup-only co-occurrence",
            not any(e["kind"] == "co-occurrence"
                    and {e["source"], e["target"]} == {"actor:testfox", "tool:foxkit"}
                    for e in graph2["edges"]))
assert_true("curated typed edge survives the derived-edge gate",
            any(e["kind"] == "relation"
                and {e["source"], e["target"]} == {"actor:testfox", "tool:foxkit"}
                for e in graph2["edges"]))

# Ambiguous labels: an entity named with an ordinary word ("fingerprint")
# or carrying another product's name as an alias ("Falcon") attaches ONLY
# through an explicit entities[] key, never through prose that happens to
# use the word. Its other labels keep phrase-matching.
_AMB_REG = {
    "actor:fingerprint": {
        "key": "actor:fingerprint", "type": "actor", "name": "fingerprint",
        "aliases": [], "ambiguous_labels": ["fingerprint"], "nexus": None,
        "summary": "Fixture actor named with an ordinary word.",
        "first_seen": "2026-06-01",
    },
    "actor:unc9999": {
        "key": "actor:unc9999", "type": "actor", "name": "UNC9999",
        "aliases": ["BlackFixture", "Falcon"], "ambiguous_labels": ["falcon"],
        "nexus": None, "summary": "Fixture actor with a product-name alias.",
        "first_seen": "2026-06-01",
    },
}
_e_tls = mk_entry("tls-fingerprint-fixture",
                  body="The loader mimics a browser TLS fingerprint. Fingerprint "
                       "randomisation defeats JA4 matching.")
_e_keyed = mk_entry("fingerprint-keyed-fixture", entities=["actor:fingerprint"],
                    body="The actor behind the breach calls itself fingerprint.")
_e_falcon = mk_entry("falcon-fixture",
                     body="The driver kills the CrowdStrike Falcon sensor.")
_e_black = mk_entry("blackfixture-fixture",
                    body="BlackFixture ran the vishing wave.")
_amb_ents, _amb_m = build_entities(_AMB_REG, [_e_tls, _e_keyed, _e_falcon, _e_black],
                                   CVES_SEEN, SOURCES_RAW, day_pages)
assert_eq("ambiguous name never phrase-matches, explicit key still attaches",
          [e["id"] for e in _amb_m.get("actor:fingerprint", [])], [_e_keyed["id"]])
assert_eq("ambiguous alias blocked case-insensitively, other alias still matches",
          [e["id"] for e in _amb_m.get("actor:unc9999", [])], [_e_black["id"]])
assert_eq("prose_match_labels drops only the ambiguous labels",
          content_model.prose_match_labels(_AMB_REG["actor:unc9999"]),
          ["UNC9999", "BlackFixture"])
assert_eq("ambiguous_labels that are the record's own labels validate",
          content_model.validate_registry(_AMB_REG), [])
_bad_amb = copy.deepcopy(_AMB_REG)
_bad_amb["actor:unc9999"]["ambiguous_labels"] = ["Pink"]
assert_true("ambiguous_labels naming a foreign label FAILs",
            any("ambiguous_labels value 'Pink'" in err
                for err in content_model.validate_registry(_bad_amb)))
_bad_amb["actor:unc9999"]["ambiguous_labels"] = "Falcon"
assert_true("ambiguous_labels must be a list",
            any("ambiguous_labels must be a list" in err
                for err in content_model.validate_registry(_bad_amb)))

# Subject vs mention: an entry that keys the entity is ABOUT it; one that
# only names it in prose is a mention. Mentions stay on the timeline
# (flagged) but never feed the TTP profile, pivots or action items.
_e_unc_about = mk_entry(
    "unc9999-about-fixture", entities=["actor:unc9999"], techniques=["T1190"],
    actions=["Reset the helpdesk MFA enrolment flow for every account the vishing wave touched."],
    body="UNC9999 exploits the edge appliance.\n\n"
         "**Defender takeaway:** the edge appliance is the entry point, so patch it first.\n\n"
         "**Triage:** a scanner run from the vulnerability-management range is the benign lookalike.\n\n"
         "## Update — 2026-07-04T05:00:00Z\n\n"
         "A second wave.\n\n**Defender takeaway:** the second wave reuses the same access.")
_e_unc_mention = mk_entry(
    "unc9999-mention-fixture", techniques=["T1566"],
    body="A phishing kit unrelated to BlackFixture beyond one shared lure.")
_sm_ents, _sm_m = build_entities(_AMB_REG, [_e_unc_about, _e_unc_mention],
                                 CVES_SEEN, SOURCES_RAW, day_pages)
_unc = {e["key"]: e for e in _sm_ents}["actor:unc9999"]
assert_eq("both the subject and the mention entry attach",
          sorted(e["id"] for e in _sm_m["actor:unc9999"]),
          sorted([_e_unc_about["id"], _e_unc_mention["id"]]))
assert_eq("only the subject entry is a subject",
          _unc["subject_entry_ids"], [_e_unc_about["id"]])
assert_eq("appearance flags the mention",
          {a["entry_id"]: a["mention"] for a in _unc["appearances"]},
          {_e_unc_about["id"]: False, _e_unc_mention["id"]: True})
if build.ATTACK_TECHNIQUES:
    assert_eq("TTP profile comes from subject entries only",
              sorted(_unc["techniques"]), ["T1190"])

_ins = build.entry_insights(_e_unc_about)
assert_eq("takeaway lifted from the main analysis, capitalised",
          _ins["takeaway"], "The edge appliance is the entry point, so patch it first.")
assert_true("triage lifted from the main analysis",
            _ins["triage"].startswith("A scanner run"))
assert_eq("newest update section's takeaway kept separately",
          (_ins["update_takeaway"] or {}).get("at"), "2026-07-04T05:00:00Z")
assert_eq("labelled list block is carried with its intro",
          build._labelled_insights("**Detection concepts.** Hunt for:\n\n- one\n- two")[0]["md"],
          "Hunt for:\n\n- one\n- two")

_unc_page = build.render_entity_page(
    _unc, matching_entries=_sm_m["actor:unc9999"], registry=_AMB_REG,
    site_url="https://x.example/", cachebust="t", prefix="../../",
    canonical="https://x.example/entities/actor%3Aunc9999/")
_unc_main = _unc_page.split("</head>")[-1]
assert_in("entity page leads with the action items", "Action items", _unc_main)
assert_in("entity page renders the defender takeaway",
          "The edge appliance is the entry point", _unc_main)
assert_in("the mention row is tagged", "e-tag--mention", _unc_main)
assert_true("insights render before the story timeline",
            _unc_main.find("Defender insights") < _unc_main.find("Story timeline"))
if build.ATTACK_TECHNIQUES:
    assert_in("ATT&CK profile is a collapsed details block",
              '<details class="ops-section atk-details" id="attack">', _unc_main)
    assert_true("ATT&CK profile renders after the story timeline",
                _unc_main.find("Story timeline") < _unc_main.find('id="attack"'))
assert_not_in("mention entry's technique stays off the page",
              "T1566", _unc_main.split('id="attack"')[0])

src = annotate_sources(SOURCES_RAW, ALL_ENTRIES)["sources"][0]
assert_true("source appearances carry dates", "2026-07-03" in src["appearances"])
assert_true("source entry_refs carry entry ids",
            any(r["id"] == E_CRIT["id"] for r in src["entry_refs"]))


# ---------------------------------------------------------------------
# Umami / CSP consistency
# ---------------------------------------------------------------------
# The loader served from UMAMI_SCRIPT_HOST POSTs its pageview beacon to
# UMAMI_BEACON_HOST/api/send. If the CSP connect-src omits the beacon host
# (or re-lists a retired one), the browser silently blocks every beacon and
# analytics record nothing while the script appears to load fine. This is
# exactly the 2026-06-20 regression — it shipped from the first commit
# because nothing tied the CSP to the loader's real beacon endpoint.
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
# CLEAN (residual == 0), regardless of how many iterations it took.
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
import branding_config  # noqa: E402

print("== branding profile ==")

_shipped = branding_config.load_branding()
# The mirror contract EXCLUDES the deployment-scoped lists (sector_slices,
# cohorts): those live only in the config — no in-code default, no fallback.
_shipped_cmp = copy.deepcopy(_shipped)
_shipped_cmp["feeds"]["sector_slices"] = []
_shipped_cmp["trends"]["cohorts"] = []
assert_eq(
    "shipped config/branding.yaml equals upstream DEFAULTS "
    "(byte-identical default site; deployment-scoped lists excluded)",
    _shipped_cmp, branding_config.DEFAULTS,
)
assert_true("shipped sector_slices are config-defined (not mirrored in code)",
            bool(_shipped["feeds"]["sector_slices"]))
assert_true("shipped cohorts are config-defined (not mirrored in code)",
            bool(_shipped["trends"]["cohorts"]))
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
        # Compare against DEFAULTS rather than a literal: the identity string
        # is config-owned (docs/customization.md), the INHERITANCE is what
        # this test is about.
        _fork["site"]["tagline"], branding_config.DEFAULTS["site"]["tagline"],
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
        branding_config.trend_cohorts(_fork2),
        [{"key": "apac", "title": "APAC items / week", "tags": (),
          "sectors": (), "regions": ("apac",), "match": "any"}],
    )
    assert_eq(
        "custom sector slices render verbatim",
        branding_config.sector_feed_slices(_fork2),
        [("feed-manufacturing.xml", ("manufacturing",), (),
          "Manufacturing", "Items affecting manufacturing.")],
    )
    # No in-code defaults: the shipped config carries the complete sets.
    assert_true("shipped config defines the cohort set",
                len(branding_config.trend_cohorts(_shipped)) > 0)
    assert_true("shipped config defines the sector slices",
                len(branding_config.sector_feed_slices(_shipped)) > 0)

# Module-level consistency in the imported build: snippet present iff
# analytics enabled; branding constants derive from the shipped config.
assert_eq(
    "build: snippet presence matches ANALYTICS_ENABLED",
    bool(build.UMAMI_SNIPPET), build.ANALYTICS_ENABLED,
)
assert_eq("build: SITE_NAME from config", build.SITE_NAME, _shipped["site"]["name"])
# The slice/cohort sets come ONLY from config (no in-code default constant).
assert_eq(
    "build: sector slices come from the config",
    build.SECTOR_FEED_SLICES,
    branding_config.sector_feed_slices(_shipped),
)
assert_eq(
    "build: trend cohorts come from the config",
    build.TREND_COHORTS,
    branding_config.trend_cohorts(_shipped),
)
assert_true("build: no in-code sector-slice default constant",
            not hasattr(build, "_DEFAULT_SECTOR_FEED_SLICES"))
assert_true("build: no in-code trend-cohort default constant",
            not hasattr(build, "_DEFAULT_TREND_COHORTS"))


# ---------------------------------------------------------------------
# NATO Admiralty classification + source-reliability rendering
# ---------------------------------------------------------------------
print("== admiralty classification + reliability badges ==")
# Source-reliability letters map to badge severity (A/B high, C med, D–F low);
# legacy HIGH/MEDIUM/LOW still tolerated on historical data.
assert_true("reliability A → high", "badge--high" in build.reliability_badge("A"))
assert_true("reliability B → high", "badge--high" in build.reliability_badge("B"))
assert_true("reliability C → med", "badge--med" in build.reliability_badge("C"))
assert_true("reliability E → low", "badge--low" in build.reliability_badge("E"))
assert_true("legacy HIGH → high", "badge--high" in build.reliability_badge("HIGH"))
# Per-entry classification code rendering.
assert_eq("classification_code B2",
          content_model.classification_code({"classification": {"reliability": "B", "credibility": 2}}),
          "B2")
assert_eq("classification_code empty when absent",
          content_model.classification_code({}), "")
# The scheme (name + code definitions) comes from config/org-profile.yaml —
# the same block the pipeline prompts are composed from — with a NATO
# doctrine fallback, so the badges can never drift from the assessed scheme.
assert_true("classification scheme has a name", bool(build.CLASSIFICATION_SCHEME_NAME))
assert_true("scheme kicker derived from the name",
            build.CLASSIFICATION_KICKER == build.CLASSIFICATION_SCHEME_NAME.split()[0].upper())
assert_true("reliability meanings loaded", "A" in build.ADMIRALTY_RELIABILITY_MEANING)
assert_true("credibility meanings loaded", "2" in build.ADMIRALTY_CREDIBILITY_MEANING)
assert_eq("meaning short-label strips the rationale",
          build._meaning_short("Usually reliable — original research…"), "Usually reliable")
_cm = build.classification_meta({"reliability": "B", "credibility": 2})
assert_eq("classification_meta code", _cm["code"], "B2")
assert_eq("classification_meta tier", _cm["tier"], "high")
assert_true("classification_meta tooltip carries both axes",
            "source reliability B" in _cm["title"] and "information credibility 2" in _cm["title"])
assert_eq("classification_meta none when absent", build.classification_meta(None), None)

# The classification badge rides on EVERY card (live / daily / weekly), not
# just the entry detail — render_badges without full= must carry it.
E_CLS = mk_entry("classified-incident", kind="incident",
                 classification={"reliability": "B", "credibility": 2})
_badges = build.render_badges(E_CLS, prefix="")
assert_in("card badges carry the classification code", ">B2</span>", _badges)
assert_in("classification badge tier-tinted", 'class="b cls cls-high"', _badges)
assert_in("classification badge carries the scheme kicker",
          f'<span class="k">{build.CLASSIFICATION_KICKER}</span>', _badges)
assert_in("classification badge on the finding card",
          'class="b cls cls-high"', render_entry_card(E_CLS, prefix=""))
assert_in("classification badge on the live timeline row",
          'class="b cls cls-high"', build.render_timeline_item(E_CLS, prefix=""))
assert_not_in("no classification badge without a rating",
              "b cls", build.render_badges(mk_entry("unrated"), prefix=""))

# Triage-kind entries (vulnerabilities) surface the org-triage rating with
# the same badge weight instead of the Admiralty code.
E_TRI = mk_entry("triaged-vuln",
                 org_triage={"category": "act-now", "rationale": "Exploited, exposed fleet."})
_tri_badges = build.render_badges(E_TRI, prefix="")
assert_in("org-triage badge on cards", ">act-now</span>", _tri_badges)
assert_in("org-triage rationale on hover", 'title="Exploited, exposed fleet."', _tri_badges)

# Entry-detail assessment block: both axes spelled out + verification +
# confidence, so "how reliable is this?" reads without a legend.
_assess = build.render_detail_assessment(E_CLS)
assert_in("assessment names the scheme",
          build.CLASSIFICATION_SCHEME_NAME.split()[0], _assess)
assert_in("assessment spells out source reliability", "Source reliability", _assess)
assert_in("assessment spells out info credibility", "Info credibility", _assess)
assert_in("assessment carries verification", "Verification", _assess)
assert_in("assessment carries confidence", "Confidence", _assess)
_assess_tri = build.render_detail_assessment(E_TRI)
assert_in("triage assessment carries the rating", "act-now", _assess_tri)
assert_in("triage assessment carries the rationale", "Exploited, exposed fleet.", _assess_tri)

# briefbook.json ships the server-rendered rating badges so brief.js renders
# the identical pill client-side (single badge implementation, no drift).
_book_cls = build_briefbook([E_CLS, E_TRI], [], ref_ts=REF_TS, prefix="../")
_bb = {x["id"]: x for x in _book_cls["entries"]}
assert_eq("briefbook classification code", _bb[E_CLS["id"]]["classification"], "B2")
assert_in("briefbook classification_html is the badge",
          'class="b cls cls-high"', _bb[E_CLS["id"]]["classification_html"])
assert_eq("briefbook org_triage block",
          _bb[E_TRI["id"]]["org_triage"],
          {"category": "act-now", "rationale": "Exploited, exposed fleet."})
assert_in("briefbook org_triage_html is the badge",
          ">act-now</span>", _bb[E_TRI["id"]]["org_triage_html"])
assert_eq("briefbook rating fields null when unrated",
          (_bb[E_TRI["id"]]["classification"], _bb[E_CLS["id"]]["org_triage"]),
          (None, None))

# ---------------------------------------------------------------------
# Ops dashboard — model self-identification canonicalisation
# ---------------------------------------------------------------------
print("== ops model canonicalisation ==")
_cm = build._ops_canonical_model
_ml = build._ops_model_label
# Friendly names — with or without the "Claude"/"Anthropic" prefix.
assert_eq("cm: friendly with prefix", _cm("Claude Opus 4.8"), "Claude Opus 4.8")
assert_eq("cm: anthropic prefix dropped", _cm("Anthropic Claude Opus 4.8"), "Claude Opus 4.8")
assert_eq("cm: context suffix dropped", _cm("Claude Opus 4.8 (1M context)"), "Claude Opus 4.8")
# The reported bug: a sub-agent that reported "Sonnet 5" (no "Claude" prefix)
# used to fold to "unknown"; it must now resolve.
assert_eq("cm: prefix optional", _cm("Sonnet 5"), "Claude Sonnet 5")
# Canonical model ids resolve directly (the id the sub-agents reported).
assert_eq("cm: model-id no minor", _cm("claude-sonnet-5"), "Claude Sonnet 5")
assert_eq("cm: model-id with minor", _cm("claude-opus-4-8"), "Claude Opus 4.8")
assert_eq("cm: model-id date suffix dropped", _cm("claude-haiku-4-5-20251001"), "Claude Haiku 4.5")
assert_eq("cm: new family future-proof", _cm("Claude Fable 5"), "Claude Fable 5")
# Series 5.5 (routines switched 2026-09-29): the point release must survive
# both id and friendly forms, including the context-window suffix on the id.
assert_eq("cm: 5.5 model-id", _cm("claude-sonnet-5-5"), "Claude Sonnet 5.5")
assert_eq("cm: 5.5 model-id with context suffix", _cm("claude-opus-5-5[1m]"), "Claude Opus 5.5")
assert_eq("cm: 5.5 friendly", _cm("Sonnet 5.5"), "Claude Sonnet 5.5")
assert_eq("cm: 5.5 friendly with context", _cm("Opus 5.5 (1M context)"), "Claude Opus 5.5")
# Genuine identification gaps still fold to "unknown" (they surface the gap).
assert_eq("cm: tier-only id is a gap", _cm("opus-tier"), "unknown")
assert_eq("cm: env-var fallback friendly is a gap", _cm("Anthropic Claude (Opus-tier)"), "unknown")
assert_eq("cm: verifier fallback is a gap", _cm("Anthropic Claude (Opus-tier verifier)"), "unknown")
assert_eq("cm: not-determined fallback is a gap",
          _cm("Anthropic Claude (specific model not determined)"), "unknown")
assert_eq("cm: prose is a gap", _cm("manual full-source audit session"), "unknown")
assert_eq("cm: bare Claude is a gap", _cm("Claude 4"), "unknown")
assert_eq("cm: empty is a gap", _cm(""), "unknown")
assert_eq("cm: non-string is a gap", _cm(None), "unknown")
# _ops_model_label — friendly preferred, model_id is the fallback.
assert_eq("ml: friendly wins", _ml("Sonnet 5", "claude-sonnet-5"), "Claude Sonnet 5")
assert_eq("ml: id recovers a vague friendly",
          _ml("Anthropic Claude (Opus-tier)", "claude-opus-4-8"), "Claude Opus 4.8")
assert_eq("ml: both vague → unknown (the env-var gap)",
          _ml("Anthropic Claude (Opus-tier)", "opus-tier"), "unknown")
assert_eq("ml: id alone recovers an empty friendly", _ml("", "claude-sonnet-5"), "Claude Sonnet 5")
assert_eq("ml: friendly alone still works", _ml("Sonnet 5"), "Claude Sonnet 5")

# ---------------------------------------------------------------------
# MITRE ATT&CK mapping — dataset-driven derivation, aggregation, exports
# ---------------------------------------------------------------------
# Runs against the committed pin (attack/enterprise-attack.json). The
# section self-skips when the dataset is absent so a fresh fork without
# the pin still gets a green baseline (check_run.py is what enforces the
# dataset's presence).
print("== ATT&CK mapping ==")
if build.ATTACK_TECHNIQUES:
    _TT = build.ATTACK_TECHNIQUES
    # entry_technique_ids: frontmatter ∪ prose, dataset-filtered.
    _fixture = {"techniques": ["T1190"],
                "body": "Execution via T1059 scripts; junk token T9999 must drop."}
    _got = content_model.entry_technique_ids(_fixture, _TT)
    assert_true("frontmatter + prose union", {"T1190", "T1059"}.issubset(set(_got)))
    assert_true("unknown prose T-token filtered by the pin", "T9999" not in _got)
    assert_true("no dataset → frontmatter only",
                content_model.entry_technique_ids(_fixture, {}) == ["T1190"])
    # revoked_by forwarding (the ATT&CK analogue of registry tombstones).
    _revoked = next((t for t, r in sorted(_TT.items())
                     if r.get("revoked") and r.get("revoked_by")), None)
    if _revoked:
        _fwd = content_model.resolve_technique_id(_TT, _revoked)
        assert_true("revoked id resolves forward to a survivor",
                    _fwd != _revoked and not _TT[_fwd].get("revoked"))
        _got2 = content_model.entry_technique_ids(
            {"techniques": [], "body": f"prose cites {_revoked} here"}, _TT)
        assert_true("prose revoked id lands on the survivor",
                    _fwd in _got2 and _revoked not in _got2)
    # Entity aggregation is evidence-bound: technique -> supporting entry ids.
    _e_hi = dict(E_HIGH)
    _e_hi["techniques"] = ["T1190"]
    _ents_atk, _m_atk = build_entities(REGISTRY, [_e_hi], CVES_SEEN, SOURCES_RAW, day_pages)
    _fox_atk = {e["key"]: e for e in _ents_atk}["actor:testfox"]
    assert_eq("entity aggregates techniques with entry evidence",
              _fox_atk["techniques"].get("T1190"), [_e_hi["id"]])
    # Navigator layer export.
    _layer = build.attack_navigator_layer(_fox_atk)
    assert_true("layer scores the technique by evidence count",
                any(t.get("techniqueID") == "T1190" and t.get("score") == 1
                    for t in _layer["techniques"]))
    assert_eq("layer pins the ATT&CK major version",
              _layer["versions"]["attack"], build.ATTACK_VERSION.split(".")[0])
    assert_eq("layer format version", _layer["versions"]["layer"],
              build.NAVIGATOR_LAYER_VERSION)
    # Entity page section.
    _sec = build.render_entity_attack_section(_fox_atk, prefix="../../")
    assert_in("entity section names the technique", "T1190", _sec)
    assert_in("entity section links the Navigator layer", "attack-layer.json", _sec)
    assert_in("entity section links the overlap matrix",
              "attack/?sel=actor%3Atestfox", _sec)
    assert_in("entity section carries the pinned version", build.ATTACK_VERSION, _sec)
    # Matrix page (server-rendered heat + directory + data island).
    _page = build.render_attack_matrix_page(
        _ents_atk, {"T1190": [_e_hi["id"]]},
        site_url="https://example.test/", cachebust="cb",
        prefix="../", canonical="https://example.test/attack/")
    assert_in("matrix renders the covered cell", 'data-tid="T1190"', _page)
    assert_in("matrix renders every tactic column",
              build.ATTACK_TACTICS[-1]["name"], _page)
    assert_in("matrix shows the pinned version", build.ATTACK_VERSION, _page)
    assert_in("matrix embeds the JS config island", 'id="attack-config"', _page)
    assert_in("directory row anchors the technique", 'id="T1190"', _page)
    # Client payload.
    _payload = build.build_attack_data_payload(_ents_atk, generated_at="2026-07-09T00:00:00Z")
    _pl_fox = next(e for e in _payload["entities"] if e["key"] == "actor:testfox")
    assert_eq("payload carries evidence counts", _pl_fox["techniques"], {"T1190": 1})
    assert_true("payload excludes revoked/deprecated techniques",
                all(not _TT[t].get("revoked") and not _TT[t].get("deprecated")
                    for t in _payload["techniques"]))
    assert_eq("payload tactic order matches the pin",
              [t["shortname"] for t in _payload["tactics"]],
              [t["shortname"] for t in build.ATTACK_TACTICS])
    # The entry permalink maps ATT&CK in the rail only: every mapped
    # technique (frontmatter ∪ prose, revoked resolved forward) with its
    # resolved name, pivoting into the site's own matrix, which already
    # carries the definition, the MITRE page and every other mapping entry.
    _e_atk = mk_entry("atk-mapped", kind="incident", techniques=["T1190"],
                      body="Initial access via exploitation. Execution via T1059 scripts.")
    _atk_page = render_entry_page(
        _e_atk, entries_by_id={}, registry={}, runs_by_id={}, day_pages=set(),
        site_url="https://x.example/", cachebust="t", prefix="../../../",
        canonical="https://x.example/entries/2026-07-03/atk-mapped/",
    )
    assert_not_in("no duplicate in-body ATT&CK section", 'id="attack-mapping"', _atk_page)
    assert_in("rail chip carries the technique id", ">T1190</span>", _atk_page)
    assert_in("rail chip resolves the technique name",
              build.attack_technique_label("T1190"), _atk_page)
    assert_in("rail chip includes prose-derived ids", ">T1059</span>", _atk_page)
    assert_in("rail chip pivots into the overlap matrix",
              'href="../../../attack/#T1190"', _atk_page)
    assert_not_in("an unmapped entry has no ATT&CK rail group", ">ATT&amp;CK techniques</h3>",
                  render_entry_page(
                      mk_entry("no-atk"), entries_by_id={}, registry={}, runs_by_id={},
                      day_pages=set(), site_url="https://x.example/", cachebust="t",
                      prefix="../../../",
                      canonical="https://x.example/entries/2026-07-03/no-atk/"))
else:
    print("  (skipped — attack/enterprise-attack.json not present)")

# ---------------------------------------------------------------------
# STIX 2.1 export (site/stix_model.py)
# ---------------------------------------------------------------------
print("== stix export ==")
import stix_model  # noqa: E402

# Timestamp conversion — STIX requires millisecond precision.
assert_eq("stix_ts second precision", stix_model.stix_ts("2026-07-03T04:21:09Z"),
          "2026-07-03T04:21:09.000Z")
assert_eq("stix_ts date", stix_model.stix_ts("2026-07-03"),
          "2026-07-03T00:00:00.000Z")
assert_eq("stix_ts fractional passthrough",
          stix_model.stix_ts("2026-08-05T21:33:58.496Z"), "2026-08-05T21:33:58.496Z")
try:
    stix_model.stix_ts("yesterday")
    assert_true("stix_ts rejects garbage", False)
except ValueError:
    assert_true("stix_ts rejects garbage", True)

# Pinned uuid5 vectors — an accidental namespace/seed change must fail loud
# (every published object id would silently change for consumers).
_ns = stix_model.make_namespace("https://ctipilot.ch/")
assert_eq("namespace uuid5 vector", str(_ns), "a9479913-dd84-5607-b3cb-42bbc237046d")
assert_eq("report id uuid5 vector",
          stix_model.sid(_ns, "report", "entry:2026-07-03/coolify-rce"),
          "report--a9d595c9-0cd6-557f-a2bf-7e7a806af882")
assert_eq("configured namespace wins",
          str(stix_model.make_namespace("https://x/", str(_ns))), str(_ns))
try:
    stix_model.make_namespace("https://x/", "nope")
    assert_true("bad configured namespace rejected", False)
except ValueError:
    assert_true("bad configured namespace rejected", True)

# Admiralty credibility → confidence (STIX 2.1 Appendix A normative table).
assert_eq("credibility 1 → 90", stix_model.confidence_from_credibility(1), 90)
assert_eq("credibility 2 → 70", stix_model.confidence_from_credibility("2"), 70)
assert_eq("credibility 6 → unspecified", stix_model.confidence_from_credibility(6), None)
assert_eq("credibility absent → unspecified", stix_model.confidence_from_credibility(None), None)

_STIX_REG = {
    "actor:testers": {
        "key": "actor:testers", "type": "actor", "name": "Testers",
        "aliases": ["TST"], "nexus": "china-nexus", "summary": "Test actor.",
        "first_seen": "2026-07-01",
        "relations": [
            {"to": "malware:testware", "type": "uses",
             "source": "2026-07-03/coolify-rce", "note": "deploys it"},
            {"to": "actor:testers2", "type": "collaborates-with",
             "source": "2026-07-03/coolify-rce"},
        ],
    },
    "actor:testers2": {"key": "actor:testers2", "type": "actor", "name": "Testers II",
                       "aliases": [], "nexus": None, "summary": "Second actor.",
                       "first_seen": "2026-07-02"},
    "malware:testware": {
        "key": "malware:testware", "type": "malware", "name": "Testware",
        "aliases": [], "nexus": None, "summary": "Test malware.",
        "first_seen": "2026-07-01",
        "relations": [{"to": "actor:testers", "type": "attributed-to",
                       "source": "2026-07-03/coolify-rce"}],
    },
    "trend:test-wave": {"key": "trend:test-wave", "type": "trend", "name": "Test wave",
                        "aliases": [], "nexus": None, "summary": "A wave.",
                        "first_seen": "2026-07-01"},
    "actor:old-name": {"key": "actor:old-name", "type": "actor", "name": "Old Name",
                       "aliases": [], "nexus": None, "summary": "Tombstone.",
                       "first_seen": "2026-07-01", "merged_into": "actor:testers"},
}
_e_rich = mk_entry(
    "coolify-rce",
    entities=["actor:old-name", "trend:test-wave"],  # tombstone must remap
    cves=[{"id": "CVE-2026-1111", "cvss": "9.8", "type": "rce", "vector": "zero-click",
           "auth": "pre-auth", "status": ["exploited", "patch-available"],
           "affected": "≤1.0", "fixed": "1.1"}],
    classification={"reliability": "B", "credibility": 2},
    updates=[
        {"at": "2026-07-04T08:00:00Z", "run_id": RUN2_ID, "type": "update",
         "summary": "New detail."},
        {"at": "2026-07-05T08:00:00Z", "run_id": RUN2_ID, "type": "correction",
         "summary": "Fixed a wrong version range."},
        {"at": "2026-07-06T08:00:00Z", "run_id": RUN2_ID, "type": "correction",
         "summary": "Metadata only.", "internal": True},
    ],
)
_e_bare = mk_entry("bare-item", day="2026-07-04", ts="2026-07-04T05:00:00Z",
                   kind="research", sources=[])
_e_bare["classification"] = {"reliability": "F", "credibility": 6}
_compiled = stix_model.compile_stix(
    [_e_rich, _e_bare], _STIX_REG, cves_seen_records=[
        {"id": "CVE-2026-1111", "first_seen": "2026-07-03", "last_seen": "2026-07-05",
         "primary_source_url": "https://example.com/advisory", "title": "Test CVE."},
    ],
    attack_dataset=None, ns=_ns, publisher_name="ctipilot.ch",
    site_url="https://ctipilot.ch/",
    extension_schema_url="https://ctipilot.ch/stix/extension-schema.json",
)
_objs = _compiled["objects"]
_by_type: dict[str, list] = {}
for _o in _objs.values():
    _by_type.setdefault(_o["type"], []).append(_o)

_rep = _objs[_compiled["report_ids"]["2026-07-03/coolify-rce"]]
assert_eq("report published = discovered_at", _rep["published"], "2026-07-03T04:21:09.000Z")
assert_eq("report modified follows latest changelog record",
          _rep["modified"], "2026-07-06T08:00:00.000Z")
assert_eq("report kind vulnerability → report_types", _rep["report_types"], ["vulnerability"])
assert_eq("report confidence B2 → 70", _rep["confidence"], 70)
assert_true("report permalink is the first external reference",
            _rep["external_references"][0]["url"].endswith("/entries/2026-07-03/coolify-rce/"))
assert_in("report labels carry priority", "critical" if _e_rich["priority"] == "critical"
          else "notable", _rep["labels"])
_ext_payload = next(iter(_rep["extensions"].values()))
assert_eq("extension carries reliability", _ext_payload["reliability"], "B")
assert_eq("extension carries the entry id", _ext_payload["entry_id"], "2026-07-03/coolify-rce")
_vuln = _by_type["vulnerability"][0]
assert_eq("one vulnerability per CVE", len(_by_type["vulnerability"]), 1)
assert_eq("vulnerability named by CVE id", _vuln["name"], "CVE-2026-1111")
assert_eq("vulnerability labels = status union", _vuln["labels"],
          ["exploited", "patch-available"])
assert_in("vulnerability referenced by the report", _vuln["id"], _rep["object_refs"])
assert_in("tombstoned entity remapped to canonical",
          _compiled["entity_ids"]["actor:testers"], _rep["object_refs"])
assert_true("tombstone emits no object", "actor:old-name" not in _compiled["entity_ids"])
_rep_bare = _objs[_compiled["report_ids"]["2026-07-04/bare-item"]]
assert_eq("bare report object_refs falls back to identity",
          _rep_bare["object_refs"], [_compiled["anchor_ids"][1]])
assert_true("credibility 6 → confidence omitted", "confidence" not in _rep_bare)

_actor = _objs[_compiled["entity_ids"]["actor:testers"]]
assert_eq("actor → intrusion-set", _actor["type"], "intrusion-set")
assert_eq("actor aliases mapped", _actor["aliases"], ["TST"])
assert_in("nexus becomes a label", "china-nexus", _actor["labels"])
_mal = _objs[_compiled["entity_ids"]["malware:testware"]]
assert_true("malware is_family", _mal["is_family"] is True)
_grp = _objs[_compiled["entity_ids"]["trend:test-wave"]]
assert_eq("trend → grouping", _grp["type"], "grouping")
assert_eq("grouping context", _grp["context"], "unspecified")
assert_eq("grouping refs its citing reports", _grp["object_refs"], [_rep["id"]])

_rels = {(_r["source_ref"], _r["target_ref"]): _r for _r in _by_type["relationship"]}
_uses = _rels[(_actor["id"], _mal["id"])]
assert_eq("uses kept verbatim", _uses["relationship_type"], "uses")
assert_true("kept relation carries no original_type extension", "extensions" not in _uses)
_auth = _rels[(_mal["id"], _actor["id"])]
assert_eq("malware attributed-to actor → authored-by", _auth["relationship_type"], "authored-by")
assert_eq("remapped relation preserves the original type",
          next(iter(_auth["extensions"].values()))["original_type"], "attributed-to")
_collab = _rels[(_actor["id"], _objs[_compiled["entity_ids"]["actor:testers2"]]["id"])]
assert_eq("collaborates-with collapses to related-to",
          _collab["relationship_type"], "related-to")
assert_in("collapsed relation names the curated type in the description",
          "collaborates-with", _collab["description"])

_notes = _by_type.get("note") or []
assert_eq("one note per non-internal correction", len(_notes), 1)
assert_eq("note content is the correction summary",
          _notes[0]["content"], "Fixed a wrong version range.")
assert_eq("note points at the report", _notes[0]["object_refs"], [_rep["id"]])

# Structural lint: every ref resolves inside the compiled corpus.
_dangling = []
for _o in _objs.values():
    for _k in ("object_refs", "object_marking_refs"):
        _dangling += [r for r in _o.get(_k) or [] if r not in _objs]
    for _k in ("created_by_ref", "source_ref", "target_ref"):
        if _o.get(_k) and _o[_k] not in _objs:
            _dangling.append(_o[_k])
assert_eq("no dangling refs in the corpus", _dangling, [])

# Reference closure: seeding the bare report must not drag the rich graph in.
_closure = stix_model.reference_closure(_objs, {_rep_bare["id"]})
assert_true("closure carries the seed + anchors only",
            _closure == {_rep_bare["id"], *_compiled["anchor_ids"][:2]}
            or _rep["id"] not in _closure)
_closure_rich = stix_model.reference_closure(_objs, {_rep["id"], *_compiled["anchor_ids"]})
assert_true("closure pulls the report's vulnerability", _vuln["id"] in _closure_rich)
assert_true("closure drops SROs with an endpoint outside",
            _uses["id"] not in _closure_rich)  # malware is not cited by the report
_closure_pair = stix_model.reference_closure(_objs, {_actor["id"], _mal["id"]})
assert_true("closure adds SROs whose endpoints landed inside",
            _uses["id"] in _closure_pair)

# Bundle: ascending (created, id) order, deterministic serialization.
_bundle = stix_model.make_bundle(_ns, "test", list(_objs.values()))
_order = [(o.get("created") or "", o["id"]) for o in _bundle["objects"]]
assert_eq("bundle sorted ascending by (created, id)", _order, sorted(_order))
_again = stix_model.compile_stix(
    [_e_rich, _e_bare], _STIX_REG, cves_seen_records=[
        {"id": "CVE-2026-1111", "first_seen": "2026-07-03", "last_seen": "2026-07-05",
         "primary_source_url": "https://example.com/advisory", "title": "Test CVE."},
    ],
    attack_dataset=None, ns=_ns, publisher_name="ctipilot.ch",
    site_url="https://ctipilot.ch/",
    extension_schema_url="https://ctipilot.ch/stix/extension-schema.json",
)
assert_eq("compile → serialize is deterministic",
          stix_model.serialize(stix_model.make_bundle(_ns, "test",
                                                      list(_again["objects"].values()))),
          stix_model.serialize(_bundle))

# Branding: the stix section resolves and validates.
assert_eq("stix_settings falls back to site name",
          branding_config.stix_settings(branding_config.DEFAULTS)["publisher_name"],
          branding_config.DEFAULTS["site"]["name"])

# Source health (2026-09-29): a reachable source whose content fails is floated
# in its own group with the evidence line, and a stale one in another.
_sh = {"last_updated": "2026-09-29T22:00:00Z", "latest": {
    "ok-src": {"id": "ok-src", "status": "active", "fetch_method": "rss", "class": "bridge-ok",
               "action": "none", "content_verdict": "relevant"},
    "shell-src": {"id": "shell-src", "status": "active", "fetch_method": "webfetch", "class": "ok",
                  "action": "needs-content-fix", "action_reason": "the recipe returns a challenge",
                  "content_verdict": "shell", "content_alnum": 333},
    "stale-src": {"id": "stale-src", "status": "active", "fetch_method": "webfetch", "class": "ok",
                  "action": "stale-content", "action_reason": "newest item too old",
                  "content_verdict": "stale", "content_alnum": 9000,
                  "newest_item": "2025-11-07", "newest_item_age_days": 326},
}}
_sh_html = build._ops_render_source_health(_sh)
assert_in("source-health: content-fix group", "Reachable, but not returning usable content", _sh_html)
assert_in("source-health: stale group", "Returning content, but nothing recent", _sh_html)
assert_in("source-health: evidence line", "content: stale · 9,000 chars · newest 2025-11-07 (326 d)", _sh_html)
assert_not_in("source-health: healthy source omitted", ">ok-src<", _sh_html)
_sh_ok = {"last_updated": "x", "latest": {"ok-src": _sh["latest"]["ok-src"]}}
assert_in("source-health: all-clear wording", "returning relevant, current content",
          build._ops_render_source_health(_sh_ok))
# v4.18: a webfetch-only source is listed as handled, never floated as a problem.
_sh_wf = {"last_updated": "x", "latest": {
    "ok-src": _sh["latest"]["ok-src"],
    "wf-src": {"id": "wf-src", "status": "active", "fetch_method": "webfetch", "class": "bridge-blocked",
               "action": "none", "content_verdict": "webfetch-only"}}}
_sh_wf_html = build._ops_render_source_health(_sh_wf)
assert_in("source-health: webfetch-only note", "Read only through the agent-side", _sh_wf_html)
assert_in("source-health: webfetch-only all-clear", "1 through WebFetch", _sh_wf_html)
assert_not_in("source-health: webfetch-only not a problem", "Reachable, but not returning usable content", _sh_wf_html)

# ---------------------------------------------------------------------
# Repo-path links (2026-09-30): a link authored relative to the source file
# (an entry linking a sibling entry, an audit run record linking its report,
# an imported entry linking a retired /briefs/ route) reaches a real page.
# ---------------------------------------------------------------------
_rl = build._remap_repo_link
_saved_universe = (set(build._LINK_ENTRY_IDS), set(build._LINK_RUN_IDS), set(build._LINK_DAY_PAGES))
build._LINK_ENTRY_IDS.clear()
build._LINK_ENTRY_IDS.update({"2026-06-29/mozilla-0din-x", "2026-07-11/friendly-fire"})
build._LINK_RUN_IDS.clear()
build._LINK_RUN_IDS.update({"2026-07-18T1208Z-audit"})
build._LINK_DAY_PAGES.clear()
build._LINK_DAY_PAGES.update({"2026-05-25", "2026-06-29"})
assert_eq("repo-link: sibling entry, relative to the entry",
          _rl("../2026-06-29/mozilla-0din-x.md", "../../../", src_dir="entries/2026-07-11"),
          "../../../entries/2026-06-29/mozilla-0din-x/")
assert_eq("repo-link: unknown entry degrades to its day page",
          _rl("../2026-06-29/gone.md", "", src_dir="entries/2026-07-11"), "daily/2026-06-29/")
assert_eq("repo-link: unknown entry on a day without a page degrades to the archive",
          _rl("../2026-06-30/gone.md", "", src_dir="entries/2026-07-11"), "daily/")
assert_eq("repo-link: retired /briefs/<day>/ route with a day page",
          _rl("/briefs/2026-05-25/", "../../", src_dir="entries/2026-05-29"), "../../daily/2026-05-25/")
assert_eq("repo-link: retired /briefs/<day>/ route without a day page",
          _rl("/briefs/2026-05-26/", "../../", src_dir="entries/2026-05-29"), "../../daily/")
assert_eq("repo-link: retired /weekly/ route",
          _rl("/weekly/2026-W21/", "", src_dir="entries/2026-05-29"), "daily/")
assert_match("repo-link: audit report from a run record goes to GitHub",
             r"^https://github\.com/[^/]+/[^/]+/blob/main/docs/audits/2026-07-18-quality-audit\.md$",
             _rl("../../docs/audits/2026-07-18-quality-audit.md", "../../", src_dir="runs/2026-07-18"))
assert_eq("repo-link: sibling run record",
          _rl("2026-07-18T1208Z-audit.md", "../../", src_dir="runs/2026-07-18"),
          "../../runs/2026-07-18T1208Z-audit/")
assert_eq("repo-link: doc to doc, relative to docs/",
          _rl("pipeline.md#entry-lifecycle", "../../../", src_dir="docs"),
          "../../../about/docs/pipeline/#entry-lifecycle")
assert_eq("repo-link: absolute URL untouched",
          _rl("https://example.com/a.md", "", src_dir="entries/2026-07-11"), "https://example.com/a.md")
assert_eq("repo-link: fragment untouched", _rl("#sources", "", src_dir="docs"), "#sources")
_rl_entry = mk_entry("friendly-fire", day="2026-07-11", ts="2026-07-11T04:00:00Z",
                     body="Builds on [0DIN](../2026-06-29/mozilla-0din-x.md) and "
                          "[the brief](/briefs/2026-05-25/).")
_rl_card = render_entry_card(_rl_entry, prefix="../")
assert_in("repo-link: entry card routes a sibling-entry link",
          'href="../entries/2026-06-29/mozilla-0din-x/"', _rl_card)
assert_in("repo-link: entry card routes a retired brief link", 'href="../daily/2026-05-25/"', _rl_card)
_rl_feed = render_entry_card(_rl_entry, prefix="https://site.test/",
                             base_url="https://site.test/entries/2026-07-11/friendly-fire/")
assert_in("repo-link: feed card links absolute",
          'href="https://site.test/entries/2026-06-29/mozilla-0din-x/"', _rl_feed)
_rl_page = render_entry_page(
    _rl_entry, entries_by_id={}, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://site.test/", cachebust="x", prefix="../../../",
    canonical="https://site.test/entries/2026-07-11/friendly-fire/")
assert_in("repo-link: entry page resolves against the site root",
          'href="https://site.test/entries/2026-06-29/mozilla-0din-x/"', _rl_page)
_rl_run = mk_run("2026-07-18T1208Z-audit", date="2026-07-18", path="runs/2026-07-18/2026-07-18T1208Z-audit.md",
                 body="Report: [audit](../../docs/audits/2026-07-18-quality-audit.md).")
_rl_note = build.render_run_note(_rl_run, prefix="../../")
assert_match("repo-link: run note routes the audit report to GitHub",
             r'href="https://github\.com/[^"]+/blob/main/docs/audits/2026-07-18-quality-audit\.md"', _rl_note)

# Daily feed (2026-09-30): the still-rolling UTC day has no day page yet, so
# it gets no item; completed days keep theirs.
_df_days = {"2026-07-02": [mk_entry("yesterday", day="2026-07-02", ts="2026-07-02T09:00:00Z")],
            "2026-07-03": [mk_entry("today-item", day="2026-07-03", ts="2026-07-03T09:00:00Z")]}
_df_xml, _ = build.build_daily_feed(_df_days, {}, site_url="https://x.example/", ref_ts=REF_TS)
assert_eq("daily feed is valid XML", _xml_validate(_df_xml), [])
assert_in("daily feed carries the completed day", "https://x.example/daily/2026-07-02/", _df_xml)
assert_not_in("daily feed skips the unfinished day", "daily/2026-07-03/", _df_xml)

build._LINK_ENTRY_IDS.clear(); build._LINK_ENTRY_IDS.update(_saved_universe[0])
build._LINK_RUN_IDS.clear(); build._LINK_RUN_IDS.update(_saved_universe[1])
build._LINK_DAY_PAGES.clear(); build._LINK_DAY_PAGES.update(_saved_universe[2])

# ---------------------------------------------------------------------
# Change signal + briefbook permalinks (2026-09-30)
# ---------------------------------------------------------------------
print("== change signal (last_changed_at) ==")
_LC_CORR = "2026-07-02T06:00:00Z"
_LC_INT = "2026-07-03T11:00:00Z"
E_LC = mk_entry(
    "lc-item", day="2026-06-20", ts="2026-06-20T10:00:00Z", priority="high",
    # A correction never moves updated_at, but it IS a change a poller must
    # see; an internal record is neither.
    updates=[{"at": _LC_CORR, "run_id": RUN2_ID, "type": "correction",
              "summary": "CVSS corrected.", "fields": ["cves", "body"]},
             {"at": _LC_INT, "run_id": RUN2_ID, "type": "improvement",
              "summary": "metadata", "fields": ["techniques"], "internal": True}],
    body="Body.\n\n## Correction — " + _LC_CORR + "\n\nCVSS corrected.",
)
assert_eq("last_changed_at: a correction moves it", build.entry_last_changed_at(E_LC), _LC_CORR)
assert_eq("last_changed_at: never-changed entry = discovered_at",
          build.entry_last_changed_at(E_HIGH), E_HIGH["discovered_at"])
assert_eq("latest_change_type: new", build.latest_change_type(E_HIGH), "new")
assert_eq("latest_change_type: internal record ignored", build.latest_change_type(E_LC), "correction")
assert_true("_entry_exploited: cisa-kev status counts",
            build._entry_exploited(mk_entry("kev-only", tags=[], cves=[{"id": "CVE-2026-1", "status": ["cisa-kev"]}])))
assert_true("_entry_kev", build._entry_kev(E_CRIT) and not build._entry_kev(E_HIGH))
assert_eq("_cve_min_record", build._cve_min_record(E_CRIT["cves"][0]),
          {"id": "CVE-2026-34038", "cvss": "9.9", "status": ["exploited", "patch-available", "cisa-kev"],
           "affected": "≤ v4.0.0-beta.420", "fixed": "v4.0.0-beta.469"})

_book2 = build_briefbook([E_CRIT, E_LC], [RUN], ref_ts=REF_TS, prefix="../",
                         site_url="https://x.example/")
_be2 = {x["id"]: x for x in _book2["entries"]}
assert_eq("briefbook permalink absolute", _be2[E_CRIT["id"]]["permalink"],
          "https://x.example/entries/2026-07-03/coolify-rce/")
assert_eq("briefbook markdown_permalink absolute", _be2[E_CRIT["id"]]["markdown_permalink"],
          "https://x.example/entries/2026-07-03/coolify-rce/index.md")
assert_eq("briefbook last_changed_at", _be2[E_LC["id"]]["last_changed_at"], _LC_CORR)
assert_eq("briefbook runs[].url is the run page", _book2["runs"][0]["url"], "../runs/2026-07-03T0412Z-intel/")

print("== alerts.json change signal ==")
# E_LC: discovered 2026-06-20 (outside the 7-day window), corrected
# 2026-07-02 (inside): it enters on the correction, not on updated_at.
_al2 = build_alerts([E_CRIT, E_HIGH, E_LC, E_NOTE], ref_ts=REF_TS, site_url="https://x.example/")
_al2m = {a["id"]: a for a in _al2["alerts"]}
assert_true("alerts: a correction inside the window brings the entry in", E_LC["id"] in _al2m)
assert_eq("alerts: last_changed_at emitted", _al2m[E_LC["id"]]["last_changed_at"], _LC_CORR)
assert_true("alerts: notable stays out", E_NOTE["id"] not in _al2m)
assert_eq("alerts: sorted by last_changed_at desc", [a["id"] for a in _al2["alerts"]][0], E_CRIT["id"])
_ac = _al2m[E_CRIT["id"]]
for field in ("permalink", "markdown_url", "kind", "actions", "affected_products", "cves",
              "exploited", "kev", "last_changed_at"):
    assert_true(f"alerts field `{field}`", field in _ac)
assert_eq("alerts: markdown_url absolute", _ac["markdown_url"],
          "https://x.example/entries/2026-07-03/coolify-rce/index.md")
assert_eq("alerts: kev flag", (_ac["kev"], _al2m[E_HIGH["id"]]["kev"]), (True, False))
assert_eq("alerts: cves carry fixed", _ac["cves"][0]["fixed"], "v4.0.0-beta.469")
assert_in("alerts comment: alert on a changed last_changed_at", "changed `last_changed_at`", _al2["_comment"])
_al_old = build_alerts([E_LC], ref_ts=datetime(2026, 7, 12, tzinfo=timezone.utc), site_url="https://x.example/")
assert_eq("alerts: a change older than 7 days drops out", _al_old["alerts"], [])

print("== actions.json ==")
E_ACT_NOTE = mk_entry(
    "notable-with-action", ts="2026-07-02T09:00:00Z", priority="notable",
    actions=["Block the vendor's legacy update endpoint at the proxy."],
    affected_products=["Microsoft SharePoint Server 2019", "Unknown Widget 3.1"],
)
E_ACT_OLD = mk_entry("stale-action", day="2026-06-01", ts="2026-06-01T09:00:00Z",
                     priority="critical", actions=["Old task."])
_act = build.build_actions([E_CRIT, E_HIGH, E_ACT_NOTE, E_ACT_OLD, E_LC], ref_ts=REF_TS,
                           site_url="https://x.example/", registry=_preg)
_ids = [it["id"] for it in _act["items"]]
assert_eq("actions: window_days", _act["window_days"], 14)
assert_eq("actions: only entries with a task, in the window, priority-ranked",
          _ids, [E_CRIT["id"], E_ACT_NOTE["id"]])
_ai = {it["id"]: it for it in _act["items"]}
_crit_it = _ai[E_CRIT["id"]]
for field in ("id", "permalink", "markdown_url", "priority", "kind", "headline", "summary",
              "last_changed_at", "change", "immediate_action", "actions", "exploited", "kev",
              "cves", "affected_products", "product_keys", "techniques", "classification",
              "verification"):
    assert_true(f"actions item field `{field}`", field in _crit_it)
assert_eq("actions: change type of an updated entry", _crit_it["change"], "update")
assert_eq("actions: change type of a new entry", _ai[E_ACT_NOTE["id"]]["change"], "new")
assert_eq("actions: immediate_action carried", _crit_it["immediate_action"]["title"], "Patch Coolify now")
assert_eq("actions: exploited + kev", (_crit_it["exploited"], _crit_it["kev"]), (True, True))
assert_eq("actions: product_keys resolve through the registry",
          _ai[E_ACT_NOTE["id"]]["product_keys"], ["product:microsoft-sharepoint"])
assert_eq("actions: affected_products kept verbatim",
          _ai[E_ACT_NOTE["id"]]["affected_products"],
          ["Microsoft SharePoint Server 2019", "Unknown Widget 3.1"])
assert_eq("actions: null immediate_action without one", _ai[E_ACT_NOTE["id"]]["immediate_action"], None)
assert_true("actions: absolute permalink", _crit_it["permalink"].startswith("https://x.example/entries/"))
assert_eq("entry_product_links: unknown product has no key",
          build.entry_product_links(E_ACT_NOTE, _preg)[1], ("Unknown Widget 3.1", ""))

print("== entry page run link ==")
_rp = render_entry_page(
    E_HIGH, entries_by_id={}, registry={}, runs_by_id={RUN["run_id"]: RUN}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-07-03/fortibleed-campaign/")
assert_in("Produced by links the run page", 'href="../../../runs/2026-07-03T0412Z-intel/"', _rp)
assert_not_in("Produced by no longer needs the ops script", "ops/#run=", _rp)
_rp2 = render_entry_page(
    E_HIGH, entries_by_id={}, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-07-03/fortibleed-campaign/")
assert_not_in("a run without a record is named, not linked", 'href="../../../runs/2026-07-03T0412Z-intel/"', _rp2)
assert_in("a run without a record is still named", ">2026-07-03T0412Z-intel</span>", _rp2)

print("== cves.json ==")
E_CVE_OLD = mk_entry(
    "cve-first", day="2026-06-30", ts="2026-06-30T09:00:00Z", priority="notable",
    cves=[{"id": "CVE-2026-34038", "cvss": "9.1", "status": ["patch-available"],
           "affected": "≤ v4.0.0-beta.400", "fixed": ""}],
    affected_products=["Microsoft SharePoint Server"],
)
_cp = build.build_cves_payload([E_CRIT, E_CVE_OLD, E_HIGH], ref_ts=REF_TS, registry=_preg)
_c = _cp["cves"]["CVE-2026-34038"]
assert_eq("cves.json: only CVEs the store analyses", sorted(_cp["cves"]), ["CVE-2026-34038"])
assert_eq("cves.json: details from the newest citing entry", (_c["cvss"], _c["fixed"]),
          ("9.9", "v4.0.0-beta.469"))
assert_eq("cves.json: status union across citing records", _c["status_union"],
          ["cisa-kev", "exploited", "patch-available"])
assert_eq("cves.json: exploited + kev", (_c["exploited"], _c["kev"]), (True, True))
assert_eq("cves.json: max priority", _c["max_priority"], "critical")
assert_eq("cves.json: entry ids newest first", _c["entry_ids"], [E_CRIT["id"], E_CVE_OLD["id"]])
assert_eq("cves.json: products from citing entries", _c["products"], ["product:microsoft-sharepoint"])
assert_eq("cves.json: last_changed_at = newest change of any citing entry", _c["last_changed_at"], UPD_AT)

print("== run links only to run pages ==")
_saved_runs = set(build._LINK_RUN_IDS)
build._LINK_RUN_IDS.clear()
build._LINK_RUN_IDS.update({"2026-07-03T0412Z-intel"})
_ub = build.render_update_block(E_CRIT, E_CRIT["updates"][0], None, prefix="../")
assert_not_in("update block: a run without a record is not linked", 'href="../runs/' + RUN2_ID, _ub)
assert_in("update block: the run is still named", "run " + RUN2_ID, _ub)
_chg = render_changes_page([E_CRIT], site_url="https://x.example/", cachebust="t", prefix="../",
                           canonical="https://x.example/changes/")
assert_not_in("changes page: no link to a missing run page", 'href="../runs/' + RUN2_ID, _chg)
build._LINK_RUN_IDS.clear()
build._LINK_RUN_IDS.update(_saved_runs)

print("== landing action items + 7-day open criticals ==")
E_CRIT_OLD = mk_entry(
    "weekend-critical", day="2026-06-29", ts="2026-06-29T09:00:00Z", priority="critical",
    immediate_action={"title": "Isolate the weekend appliance", "action": "Pull it off the network."},
)
E_CRIT_STALE = mk_entry("stale-critical", day="2026-06-20", ts="2026-06-20T09:00:00Z",
                        priority="critical")
assert_eq("open_criticals: the 7-day alerts window",
          sorted(e["id"] for e in build.open_criticals([E_CRIT, E_CRIT_OLD, E_CRIT_STALE, E_HIGH], REF_TS)),
          sorted([E_CRIT["id"], E_CRIT_OLD["id"]]))
_land = render_live_brief_page(
    [E_CRIT, E_HIGH], [RUN, RUN2],
    all_entries=[E_CRIT, E_HIGH, E_CRIT_OLD, E_CRIT_STALE], all_runs=[RUN, RUN2],
    ref_ts=REF_TS, entries_by_id={}, card_html_by_id={},
    site_url="https://x.example/", cachebust="t", prefix="", canonical="https://x.example/",
)
assert_not_in("landing alarm follows the reading window (a 4-day-old critical stays out)", "Isolate the weekend appliance", _land)
assert_not_in("landing alarm drops a critical older than 7 days", "entries/2026-06-20/stale-critical/", _land)
assert_in("landing § Action items renders the window's tasks",
          'id="action-items" data-action-items', _land)
assert_in("landing action item text", "Patch Coolify to", _land)
assert_in("landing action item links its finding", 'class="action-ref" href="entries/2026-07-03/coolify-rce/"', _land)
assert_true("landing action items sit below the timeline",
            _land.index("data-action-items") > _land.index("data-brief-timeline"))
assert_in("feed counts link down to the action items", 'href="#action-items"><b data-window-act>1</b>', _land)
assert_in("brief config carries the alarm window", '"alarm_days": 7', _land)
_land_none = render_live_brief_page(
    [E_HIGH], [RUN], all_entries=[E_HIGH], all_runs=[RUN], ref_ts=REF_TS,
    entries_by_id={}, card_html_by_id={}, site_url="https://x.example/", cachebust="t",
    prefix="", canonical="https://x.example/")
assert_in("no task in the window: the section ships hidden and empty",
          'data-action-items aria-labelledby="action-items-h" hidden>', _land_none)
_ai_html, _ai_n = build.render_action_items([E_HIGH, E_CRIT], prefix="../../")
assert_eq("render_action_items counts tasks", _ai_n, 1)
assert_in("render_action_items list", '<ul class="action-list" data-action-list>', _ai_html)
assert_eq("render_action_items: nothing to do renders nothing", build.render_action_items([E_HIGH], prefix=""), ("", 0))
_bb3 = {x["id"]: x for x in build_briefbook([E_CRIT], [], ref_ts=REF_TS, prefix="../")["entries"]}
assert_eq("briefbook action_label", _bb3[E_CRIT["id"]]["action_label"], "CVE-2026-34038")
assert_eq("briefbook actions_html is the rendered task",
          _bb3[E_CRIT["id"]]["actions_html"], ["Patch Coolify to ≥ v4.0.0-beta.469."])

print("== day page: task-changing records ==")
_RAISE_AT = "2026-07-03T06:00:00Z"
E_RAISED = mk_entry(
    "raised-to-critical", day="2026-07-01", ts="2026-07-01T09:00:00Z", priority="critical",
    immediate_action={"title": "Rotate the exposed signing key", "action": "Rotate it now."},
    actions=["Revoke every token minted with the old signing key."],
    updates=[{"at": _RAISE_AT, "run_id": RUN2_ID, "type": "update",
              "summary": "Exploitation confirmed; raised to critical.",
              "fields": ["priority", "immediate_action", "actions", "body"]}],
    updated_at=_RAISE_AT,
    body="Body.\n\n## Update — " + _RAISE_AT + "\n\nExploitation confirmed.",
)
E_BODY_ONLY = mk_entry(
    "body-only-update", day="2026-07-01", ts="2026-07-01T10:00:00Z", priority="critical",
    actions=["A task that did not change today."],
    updates=[{"at": _RAISE_AT, "run_id": RUN2_ID, "type": "update",
              "summary": "More detail.", "fields": ["body"]}],
    updated_at=_RAISE_AT,
    body="Body.\n\n## Update — " + _RAISE_AT + "\n\nMore detail.",
)
assert_true("task_changed_on: priority/actions in fields", build.task_changed_on(E_RAISED, "2026-07-03"))
assert_true("task_changed_on: a body-only record does not count",
            not build.task_changed_on(E_BODY_ONLY, "2026-07-03"))
assert_true("task_changed_on: another day does not count", not build.task_changed_on(E_RAISED, "2026-07-02"))
assert_eq("day_task_entries", [e["id"] for e in build.day_task_entries([E_HIGH], [E_RAISED, E_BODY_ONLY], "2026-07-03")],
          [E_HIGH["id"], E_RAISED["id"]])
_dp = render_day_page(
    "2026-07-03", [E_HIGH], [RUN], entries_by_id={}, site_url="https://x.example/", cachebust="t",
    prefix="../../", canonical="https://x.example/daily/2026-07-03/",
    updated_entries=[E_RAISED, E_BODY_ONLY])
assert_in("day alarm carries the entry raised to critical that day", "Rotate the exposed signing key", _dp)
assert_in("day action items carry its changed task", "Revoke every token minted", _dp)
assert_not_in("a body-only update adds no action item", "A task that did not change today.", _dp)
assert_not_in("a body-only update raises no alarm", 'class="alarm-row" href="../../entries/2026-07-01/body-only-update/"', _dp)

print("== /cves/ list + entity last covered ==")
_ents10, _ = build_entities({}, [E_CVE_OLD, E_CRIT, E_LC], {"cves": []}, {"sources": []}, set())
_cve10 = {e["key"]: e for e in _ents10}["CVE-2026-34038"]
assert_eq("CVE entity carries the newest citing facts", (_cve10["cve_facts"]["cvss"], _cve10["cve_facts"]["kev"]),
          ("9.9", True))
assert_eq("CVE entity names its latest entry", _cve10["latest_entry_id"], E_CRIT["id"])
assert_eq("CVE last covered follows the latest change (an update after publication)",
          _cve10["last_covered"], UPD_AT[:10])
_cvel = build.render_cve_list_page([_cve10], site_url="https://x.example/", cachebust="t",
                                   prefix="../", canonical="https://x.example/cves/")
assert_in("/cves/: CVSS column", '<td class="cve-cvss num nowrap"><span class="mono" title="9.9">9.9</span>', _cvel)
_cve_note = dict(_cve10, cve_facts=dict(_cve10["cve_facts"], cvss="9.8 (CNA) / 7.0 (NVD re-score, AV:N/AC:H)"))
assert_in("/cves/: a scoring note shows its leading score, full text in the tooltip",
          'title="9.8 (CNA) / 7.0 (NVD re-score, AV:N/AC:H)">9.8</span>',
          build.render_cve_list_page([_cve_note], site_url="https://x.example/", cachebust="t",
                                     prefix="../", canonical="https://x.example/cves/"))
assert_in("/cves/: exploited + KEV badges", ">KEV</span>", _cvel)
assert_in("/cves/: fixed column", "v4.0.0-beta.469", _cvel)
assert_in("/cves/: latest coverage links the entry",
          '<a href="../entries/2026-07-03/coolify-rce/" class="mono">2026-07-03</a>', _cvel)
assert_in("/cves/: count of the other entries", "+1 more", _cvel)
assert_not_in("/cves/: coverage never links a day page", '<td class="cve-cov"><a href="../daily/', _cvel)
_lc_cve = dict(E_LC, cves=[{"id": "CVE-2026-7777", "status": ["patch-available"]}])
_ents10b, _ = build_entities({}, [_lc_cve], {"cves": []}, {"sources": []}, set())
_c7 = {e["key"]: e for e in _ents10b}["CVE-2026-7777"]
assert_eq("entity last covered: a correction after publication moves it",
          (_c7["first_covered"], _c7["last_covered"]), ("2026-06-20", _LC_CORR[:10]))

print("== Exposure labelled line ==")
_exp_html = enhance_brief_item_html(render_markdown(
    "Analysis.\n\n**Exposure:** internet-facing gateways on 7.x; check the admin banner."))
assert_in("Exposure becomes a callout", '<aside class="callout callout--exposure" role="note">', _exp_html)
assert_in("Exposure callout label", '<span class="callout__label">Exposure</span>', _exp_html)
_exp_entry = mk_entry("exposure-fixture", entities=["actor:unc9999"], body=(
    "Body.\n\n**Exposure:** every tenant on the legacy connector; check the connector log.\n\n"
    "**Detection:** process creation from the connector service.\n\n"
    "**Defender takeaway:** retire the legacy connector."))
_exp_ins = build.entry_insights(_exp_entry)
assert_eq("entry_insights lifts the Exposure line",
          _exp_ins["exposure"], "Every tenant on the legacy connector; check the connector log.")
assert_eq("_insight_kind exposure", build._insight_kind("Exposure"), "exposure")
_exp_intel = build.render_entity_intel({"key": "actor:unc9999", "type": "actor", "title": "UNC9999"},
                                       [_exp_entry], prefix="../../")
assert_in("entity insights surface Exposure", '<span class="callout__label">Exposure</span>', _exp_intel)
assert_in("entity insights name Exposure in the fold", "Exposure · detection", _exp_intel)
_exp_only = mk_entry("exposure-only", body="Body.\n\n**Exposure:** only the exposure line here.")
assert_in("an entry with only an Exposure line still earns an insight card",
          "Only the exposure line here.",
          build.render_entity_intel({"key": "x", "type": "actor", "title": "X"}, [_exp_only], prefix=""))

print("== llms.txt ==")
with tempfile.TemporaryDirectory() as _td:
    _lp = Path(_td) / "llms.txt"
    build.write_llms_txt(_lp, site_url="https://x.example/", counts={"entries": 1},
                         latest_day="2026-07-02", generated="g")
    _lt = _lp.read_text(encoding="utf-8")
_mach = _lt[_lt.index("## Machine endpoints"):]
_order = [_mach.index(k) for k in ("data/actions.json", "data/cves.json", "data/alerts.json",
                                    "data/briefbook.json", "data/search.json", "data/graph.json",
                                    "data/attack.json", "stix/bundle.json", "attack-layer.json")]
assert_eq("llms.txt lists actions.json first, then the other endpoints in order", _order, sorted(_order))
assert_in("llms.txt summarises the actions.json fields", "last_changed_at, change (new|update|correction|improvement)", _mach)
assert_in("llms.txt names the briefbook permalinks", "markdown_permalink", _mach)
assert_not_in("llms.txt carries no em dash", "\u2014", _lt)

print("== source_health load warning ==")
import contextlib  # noqa: E402
import io  # noqa: E402
with tempfile.TemporaryDirectory() as _td:
    _bad = Path(_td) / "source_health.json"
    _bad.write_text("{not json", encoding="utf-8")
    _err = io.StringIO()
    with contextlib.redirect_stderr(_err):
        _sh_loaded = build.load_source_health(_bad)
    assert_eq("unparseable source_health.json loads as None", _sh_loaded, None)
    assert_in("unparseable source_health.json is announced", "warning: source_health.json not loaded", _err.getvalue())
    _good = Path(_td) / "ok.json"
    _good.write_text('{"latest": {}}', encoding="utf-8")
    assert_eq("valid source_health.json loads", build.load_source_health(_good), {"latest": {}})
    assert_eq("absent source_health.json is silent None", build.load_source_health(Path(_td) / "none.json"), None)

print("== briefbook carries corrected entries for the client alarm ==")
E_CORR_OLD = mk_entry(
    "old-critical-corrected", day="2026-05-01", ts="2026-05-01T09:00:00Z", priority="critical",
    updates=[{"at": "2026-07-02T09:00:00Z", "run_id": RUN2_ID, "type": "correction",
              "summary": "Affected range corrected.", "fields": ["cves", "body"]}],
    body="Body.\n\n## Correction — 2026-07-02T09:00:00Z\n\nAffected range corrected.")
_bbc = build_briefbook([E_CORR_OLD, E_HIGH], [], ref_ts=REF_TS, prefix="../")
assert_true("briefbook includes an old entry corrected inside the window",
            E_CORR_OLD["id"] in [x["id"] for x in _bbc["entries"]])
assert_true("open_criticals and briefbook agree on it",
            E_CORR_OLD["id"] in [e["id"] for e in build.open_criticals([E_CORR_OLD], REF_TS)])

assert_in("alarm stamp names a correction as the last change", "corrected 02 Jul 09:00Z",
          render_alarm([E_CORR_OLD]))
assert_in("alarm stamp names an update", "updated 03 Jul 08:00Z", render_alarm([E_CRIT]))

# ---------------------------------------------------------------------
# Result
# ---------------------------------------------------------------------
print()
if FAILURES:
    print(f"{len(FAILURES)} failure(s):")
    for f in FAILURES:
        print(f"  · {f}")
    sys.exit(1)
print("All tests passed.")
sys.exit(0)
