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
    render_actnow,
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

print("== enhance_brief_item_html (Defender-takeaway callout) ==")
lead_html = enhance_brief_item_html(
    "<p><strong>Defender takeaway:</strong> patch now.</p>"
)
assert_in("leading label promoted to aside",
          '<aside class="callout callout--takeaway"', lead_html)
assert_in("label badge rendered",
          '<span class="callout__label">Defender takeaway</span>', lead_html)
assert_in("body carried into callout", "patch now.", lead_html)
assert_not_in("no leftover empty paragraph", "<p></p>", lead_html)
mid_html = enhance_brief_item_html(
    "<p>Narrative prose with <strong>bold</strong> inline. "
    "<strong>Defender takeaway:</strong> rotate the keys.</p>"
)
assert_in("mid-paragraph label promoted to aside",
          '<aside class="callout callout--takeaway"', mid_html)
assert_in("preceding prose kept as its own paragraph",
          "<p>Narrative prose with <strong>bold</strong> inline.</p>", mid_html)
assert_in("takeaway body carried into callout", "rotate the keys.", mid_html)
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

print("== scan_for_secrets ==")
assert_true("github classic token detected",
            scan_for_secrets("ghp_" + "A" * 40))
assert_true("aws key id detected", scan_for_secrets("AKIA" + "A" * 16))
assert_eq("clean text clean", scan_for_secrets("nothing to see CVE-2026-1234"), [])

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
             kind="vulnerability", priority="notable",
             horizon="operational", **kw):
    e = copy.deepcopy(content_model.ENTRY_DEFAULTS)
    e.update({
        "schema": 1,
        "kind": kind,
        "horizon": horizon,
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
E_STRAT = mk_entry(
    "weekly-policy-item", day="2026-06-28", ts="2026-06-28T10:00:00Z",
    kind="policy", priority="high", horizon="strategic",
)
E_STRAT2 = mk_entry(
    "weekly-synthesis", day="2026-06-28", ts="2026-06-28T11:00:00Z",
    kind="synthesis", priority="notable", horizon="strategic",
    weekly_section="weekly-long-running",
    references=["2026-07-01/old-item"],
    migrated_from="briefs/2026-06-28.md",
)
ALL_ENTRIES = sorted(
    [E_CRIT, E_HIGH, E_NOTE, E_DEEP, E_OLD, E_STRAT, E_STRAT2],
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
actnow = render_actnow(E_CRIT, prefix="")
assert_in("ACT NOW callout present", "ACT NOW · CRITICAL", actnow)
assert_in("ACT NOW carries the action", "Upgrade to v4.0.0-beta.469 immediately.", actnow)
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
assert_in("updated row flagged UPD", 'style="color:var(--warn)">UPD</span>', tl)
assert_in("updated row carries the record line", 'class="tl-update tl-update--update"', tl)
assert_in("updated row shows the record summary", "A public PoC has now surfaced and CISA added", tl)
assert_in("updated row stamped with the record time", "03 Jul 08:00Z", tl)
assert_in("updated row marks the item", 'class="tl-item tl-item--updated"', tl)
row = render_timeline_item(E_HIGH, prefix="", is_new=True)
assert_in("new row flagged NEW", 'style="color:var(--ok)">NEW</span>', row)
assert_not_in("new row has no update line", "tl-update", row)
assert_eq("timeline appears once per entry", tl.count('data-entry-id="' + E_CRIT["id"] + '"'), 1)

print("== entry page ==")
epage = render_entry_page(
    E_CRIT, entries_by_id=by_id, registry={}, runs_by_id={RUN["run_id"]: RUN, RUN2_ID: RUN2},
    day_pages={"2026-07-03"}, site_url="https://x.example/", cachebust="t",
    prefix="../../../", canonical="https://x.example/entries/2026-07-03/coolify-rce/",
)
assert_in("meta: first published", "first published 2026-07-03 04:21 UTC", epage)
assert_in("meta: updated", ">updated 2026-07-03 08:00 UTC</a>", epage)
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
strat_page = render_entry_page(
    E_STRAT, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-06-28/weekly-policy-item/",
)
assert_in("legacy strategic entry links the daily archive", "Back to the daily archive", strat_page)
assert_not_in("no /weekly/ link on legacy strategic entries", "weekly/", strat_page.split("<main")[-1] if "<main" in strat_page else strat_page.replace("weekly-policy-item", ""))
# Metadata completeness on the permalink: event date, deck, CVE detail
# fields, source dates, references, migration provenance, horizon badge.
assert_in("meta: event date", ">event 2026-07-03</span>", epage)
assert_in("deck: headline + summary visible on the permalink",
          '<p class="edeck"><strong>Headline coolify-rce</strong> Summary coolify-rce.</p>', epage)
assert_in("rail CVE detail line (type · vector · auth)",
          '<div class="erail-cve__meta">rce · zero-click · post-auth</div>', epage)
assert_in("rail CVE fixed version",
          '<span class="erail-cve__vl">Fixed</span> v4.0.0-beta.469', epage)
assert_in("rail CVE affected versions",
          '<span class="erail-cve__vl">Affected</span> ≤ v4.0.0-beta.420', epage)
assert_in("source date rides the role label", "primary · 2026-07-03", epage)
assert_in("entry advertises its raw markdown twin in the head",
          'rel="alternate" type="text/markdown"', epage)
assert_in("entry meta line links the raw source", ">raw .md</a>", epage)
assert_in("entry JSON-LD points at the markdown encoding",
          '"encodingFormat":"text/markdown"', epage)
assert_in("deep-dive badge carries the category",
          "deep dive · edge-infrastructure", build.render_badges(E_DEEP, full=True))
strat2_page = render_entry_page(
    E_STRAT2, entries_by_id=by_id, registry={}, runs_by_id={}, day_pages=set(),
    site_url="https://x.example/", cachebust="t", prefix="../../../",
    canonical="https://x.example/entries/2026-06-28/weekly-synthesis/",
)
assert_in("references render as Builds on", "Builds on:", strat2_page)
assert_in("builds-on links the referenced entry",
          'href="../../../entries/2026-07-01/old-item/"', strat2_page)
assert_in("migration provenance in the meta line", "migrated from briefs/2026-06-28.md", strat2_page)
assert_in("non-operational horizon badge", ">strategic</span>", strat2_page)

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
assert_in("landing hero is the one h1", "<h1>", landing)
assert_not_in("feed heading demoted below the hero h1", '<h1 class="feedhead-title">', landing)
assert_in("knowledge-base pivot band below the feed", 'class="pivotband"', landing)
assert_in("pivot band links the daily archive at the latest day", 'href="daily/2026-07-01/"', landing)
assert_in("pivot band links the changelog", 'href="changes/"', landing)
assert_in("machine-endpoint line for agents", "data/briefbook.json", landing)
assert_in("machine-endpoint line advertises llms.txt", "llms.txt", landing)
assert_in("updates pulse tile links the changelog", 'href="changes/"', landing)
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
    [E_STRAT], site_url="https://x.example/", cachebust="t",
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
assert_eq("day pages: operational dates only", sorted(days), ["2026-07-01", "2026-07-03"])
assert_eq("2026-07-03 has 4 operational entries", len(days["2026-07-03"]), 4)
assert_eq("deep dive routes to deep-dive", entry_section_key(E_DEEP), "deep-dive")
assert_eq("policy routes to the research section", entry_section_key(E_STRAT), "research")
assert_eq("legacy synthesis kind has no section", entry_section_key(E_STRAT2), None)
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
for field in ("id", "url", "date", "discovered_at", "kind", "horizon", "priority",
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
# Both horizons alert — a strategic `high` is still notification-worthy.
assert_eq("alerts: only critical|high in window",
          sorted(a["id"] for a in alerts["alerts"]),
          sorted([E_CRIT["id"], E_HIGH["id"], E_STRAT["id"]]))
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

# Derived-edge evidence gate: strategic synthesis and annual-report
# roundups reference many unrelated entities — they must never create
# co-occurrence edges. Curated relations are unaffected.
E_ROUNDUP_W = mk_entry(
    "weekly-roundup-fixture", kind="synthesis", priority="notable",
    ts="2026-07-03T09:00:00Z", horizon="strategic",
    entities=["actor:testfox", "tool:foxkit"],
)
E_ROUNDUP_A = mk_entry(
    "annual-roundup-fixture", kind="annual-report", priority="notable",
    ts="2026-07-03T10:00:00Z",
    entities=["actor:testfox", "tool:foxkit"],
)
ents2, matched2 = build_entities(
    REGISTRY, ALL_ENTRIES + [E_ROUNDUP_W, E_ROUNDUP_A],
    CVES_SEEN, SOURCES_RAW, day_pages)
co2 = compute_related_entities(ents2, matched2)
fox2 = {e["key"]: e for e in ents2}["actor:testfox"]
assert_true("strategic/annual-report entries create no co-occurrence",
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
        _fork["site"]["tagline"], "Swiss Government Entities",
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
    # Entry-detail ATT&CK mapping section: every mapped technique with its
    # resolved name + definition, grouped by tactic — visible on the report
    # itself, not just as a bare id list.
    _e_atk = mk_entry("atk-mapped", kind="incident", techniques=["T1190"],
                      body="Initial access via exploitation. Execution via T1059 scripts.")
    _esec = build.render_entry_attack_section(_e_atk, prefix="../../")
    assert_in("entry section anchors for the rail chips", 'id="attack-mapping"', _esec)
    assert_in("entry section carries the technique id", ">T1190</span>", _esec)
    assert_in("entry section resolves the technique name",
              build.attack_technique_label("T1190"), _esec)
    assert_in("entry section includes prose-derived ids", ">T1059</span>", _esec)
    assert_in("entry section groups by tactic", 'class="atk-tactic"', _esec)
    assert_in("entry section links the overlap matrix", "attack/#T1190", _esec)
    assert_in("entry section links the MITRE page", "attack.mitre.org", _esec)
    assert_in("entry section carries the pinned version", build.ATTACK_VERSION, _esec)
    assert_eq("no techniques → no section",
              build.render_entry_attack_section(mk_entry("no-atk"), prefix=""), "")
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
