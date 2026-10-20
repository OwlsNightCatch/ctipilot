#!/usr/bin/env python3
"""Stdlib-only offline self-test for `tools/entry_record.py`.

    python3 tools/test_entry_record.py

Each case builds a throwaway store in a temporary directory, so nothing in the
repository is touched and no network is used. The cases pin the changelog
rules the tool exists to get right (docs/pipeline.md § Entry lifecycle): `at`
strictly later than the last stamp, `updated_at` moved only by a non-internal
`update`, a section for every non-internal record and none for an internal
one, one record per fire per entry, and every byte outside the inserted lines
left as it was.
"""
from __future__ import annotations

import importlib.util
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load():
    spec = importlib.util.spec_from_file_location("entry_record_under_test", _HERE / "entry_record.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


er = _load()
cm = er.cm

FRESH = """---
schema: 1
kind: vulnerability
title: "Example flaw"
headline: "Example flaw"
summary: >
  An example.
discovered_at: "2026-05-10T04:00:00Z"
run_id: 2026-05-10T0400Z-intel
priority: notable
updated_at: null
updates: []
tags: [vulnerability]
---

The analysis ([Vendor, 2026-05-10](https://example.org/advisory)).
"""

UPDATED = """---
schema: 1
kind: vulnerability
title: "Example flaw"
headline: "Example flaw"
summary: >
  An example.
discovered_at: "2026-05-10T04:00:00Z"
run_id: 2026-05-10T0400Z-intel
priority: notable
updated_at: "2026-05-12T04:00:00Z"
updates:
  - at: "2026-05-12T04:00:00Z"
    run_id: 2026-05-12T0400Z-intel
    type: update
    summary: >
      Now exploited.
    fields:
      - cves
      - body
  - at: "2026-05-13T04:00:00Z"
    run_id: 2026-05-13T0400Z-audit
    type: improvement
    internal: true
    summary: >
      Mapping added.
    fields: [techniques]
tags: [vulnerability]
---

The analysis.

## Update — 2026-05-12T04:00:00Z

Exploited now ([CISA, 2026-05-12](https://example.org/kev)).
"""

RUN = "2026-10-21T0900Z-audit"


class Store:
    def __init__(self, text: str):
        self.dir = Path(tempfile.mkdtemp(prefix="entry-record-test-"))
        self.path = self.dir / "entries" / "2026-05-10" / "example-flaw.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(text, encoding="utf-8")
        self.id = "2026-05-10/example-flaw"

    def entry(self) -> dict:
        return cm.load_entry(self.path, root=self.dir)

    def text(self) -> str:
        return self.path.read_text(encoding="utf-8")

    def close(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def _raises(fn, needle: str):
    try:
        fn()
    except er.RecordError as exc:
        assert needle in str(exc), f"expected {needle!r} in {exc!r}"
        return
    raise AssertionError(f"expected RecordError containing {needle!r}")


def test_correction_on_fresh_entry():
    s = Store(FRESH)
    try:
        at = er.add(s.dir, s.id, "correction", RUN, ["summary", "body"], "Fixed the version.",
                    "The fixed release is 2.1 ([Vendor](https://example.org/advisory)).", False)
        e = s.entry()
        assert e["updated_at"] is None, "a correction never moves updated_at"
        assert len(e["updates"]) == 1 and e["updates"][0]["type"] == "correction"
        assert e["updates"][0]["fields"] == ["summary", "body"]
        assert f"## Correction — {at}" in e["body"]
        assert "updates: []" not in s.text()
    finally:
        s.close()


def test_update_moves_updated_at_and_preserves_bytes():
    s = Store(UPDATED)
    try:
        before = s.text()
        at = er.add(s.dir, s.id, "update", RUN, ["cves"], "Patched.", "Patch out.", False)
        e = s.entry()
        assert e["updated_at"] == at
        assert [u["run_id"] for u in e["updates"]][-1] == RUN
        assert e["updates"][1]["fields"] == ["techniques"], "earlier records untouched"
        after = s.text()
        # Everything before `updated_at` and the whole prior body survive verbatim.
        assert after.startswith(before.split("updated_at:")[0])
        assert before.split("---\n", 2)[2].rstrip("\n") in after
        assert after.index(f'  - at: "{at}"') < after.index("tags: [vulnerability]")
    finally:
        s.close()


def test_internal_has_no_section_and_keeps_updated_at():
    s = Store(UPDATED)
    try:
        er.add(s.dir, s.id, "improvement", RUN, ["tags"], "Tag added.", None, True)
        e = s.entry()
        assert e["updated_at"] == "2026-05-12T04:00:00Z"
        assert e["updates"][-1].get("internal") is True
        assert "## Improvement" not in e["body"]
    finally:
        s.close()


def test_guards():
    s = Store(UPDATED)
    try:
        _raises(lambda: er.add(s.dir, s.id, "correction", RUN, ["body"], "x", None, False),
                "needs its section")
        _raises(lambda: er.add(s.dir, s.id, "correction", RUN, ["tags"], "x", "y", True),
                "carries no section")
        _raises(lambda: er.add(s.dir, s.id, "correction", RUN, ["body"], "x", "y", False,
                               at="2026-05-13T04:00:00Z"), "not later")
        _raises(lambda: er.add(s.dir, s.id, "correction", "2026-05-10T0400Z-intel", ["body"],
                               "x", "y", False), "created the entry")
        er.add(s.dir, s.id, "correction", RUN, ["body"], "x", "y", False)
        _raises(lambda: er.add(s.dir, s.id, "improvement", RUN, ["tags"], "x", None, True),
                "one record per fire")
        _raises(lambda: er.parse_fields("cves, Bad Field"), "not a field name")
    finally:
        s.close()


def test_amend_own_record_only():
    s = Store(UPDATED)
    try:
        at = er.add(s.dir, s.id, "correction", RUN, ["body"], "First wording.", "Delta.", False)
        er.amend(s.dir, s.id, RUN, "Second, better wording of the same change.", None, ["cves"],
                 check_published=False)
        rec = s.entry()["updates"][-1]
        assert rec["at"] == at
        assert rec["summary"].strip() == "Second, better wording of the same change."
        assert rec["fields"] == ["body", "cves"]
        er.amend(s.dir, s.id, RUN, None, ["summary"], None, check_published=False)
        assert s.entry()["updates"][-1]["fields"] == ["summary"]
        _raises(lambda: er.amend(s.dir, s.id, "2026-01-01T0000Z-intel", "x", None, None,
                                 check_published=False), "carries no record")
        _raises(lambda: er.amend(s.dir, s.id, RUN, None, None, None, check_published=False),
                "nothing to amend")
    finally:
        s.close()


def test_amend_block_list_fields():
    s = Store(UPDATED)
    try:
        er.amend(s.dir, s.id, "2026-05-12T0400Z-intel", None, None, ["affected_products"],
                 check_published=False)
        e = s.entry()
        assert e["updates"][0]["fields"] == ["cves", "body", "affected_products"]
        assert e["updates"][1]["fields"] == ["techniques"]
    finally:
        s.close()


def test_diff_names_changed_fields():
    if shutil.which("git") is None:
        print("  skip test_diff_names_changed_fields: no git")
        return
    s = Store(UPDATED)
    try:
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.org"}
        for cmd in (["git", "init", "-q"], ["git", "add", "."], ["git", "commit", "-qm", "base"]):
            subprocess.run(cmd, cwd=s.dir, check=True, env=env, capture_output=True)
        s.path.write_text(s.text().replace("priority: notable", "priority: high")
                          .replace("The analysis.", "The corrected analysis."), encoding="utf-8")
        er.add(s.dir, s.id, "correction", RUN, ["priority", "body"], "x", "Delta.", False)
        assert er.changed_fields(s.dir, s.id, RUN) == ["body", "priority"]
    finally:
        s.close()


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok   {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  FAIL {t.__name__}: {exc!r}")
    print(f"{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
