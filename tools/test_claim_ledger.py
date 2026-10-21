#!/usr/bin/env python3
"""Stdlib-only offline self-test for `tools/claim_ledger.py`.

    python3 tools/test_claim_ledger.py

Each case builds a throwaway store in a temporary git repository, so nothing
in the repository is touched and no network is used. The cases pin what a
verifier pass must answer for on an entry the fire updated against a base
commit: the fire's own section, the sentences it changed in the main analysis,
and the sentences it edited inside an EARLIER dated section (tracker row W7-14:
the ledger used to skip those, so a post-fix pass never saw them), while text
the fire left alone stays out.
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
    spec = importlib.util.spec_from_file_location("claim_ledger_under_test", _HERE / "claim_ledger.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cl = _load()

RUN = "2026-10-21T0900Z-audit"
EARLIER = "2026-05-12T04:00:00Z"
OWN = "2026-10-21T09:05:00Z"

BASE = f"""---
schema: 1
kind: vulnerability
title: "Example flaw"
headline: "Example flaw"
summary: >
  An example.
discovered_at: "2026-05-10T04:00:00Z"
run_id: 2026-05-10T0400Z-intel
priority: notable
updated_at: "{EARLIER}"
updates:
  - at: "{EARLIER}"
    run_id: 2026-05-12T0400Z-intel
    type: update
    summary: >
      Now exploited.
    fields: [cves, body]
tags: [vulnerability]
---

The vendor fixed the flaw in release 2.1 of the product line ([Vendor, 2026-05-10](https://example.org/advisory)).

## Update — {EARLIER}

The agency added the flaw to its catalogue of exploited flaws ([Agency, 2026-05-12](https://example.org/kev)). The vendor counted four hundred affected customers in its first statement ([Vendor, 2026-05-12](https://example.org/statement)).
"""

RECORD = f"""  - at: "{OWN}"
    run_id: {RUN}
    type: correction
    summary: >
      The customer count is corrected.
    fields: [body]
"""

OWN_SECTION = f"""
## Correction — {OWN}

The vendor's statement gives forty affected customers, not four hundred ([Vendor, 2026-05-12](https://example.org/statement)).
"""


class Store:
    def __init__(self):
        self.dir = Path(tempfile.mkdtemp(prefix="claim-ledger-test-"))
        self.path = self.dir / "entries" / "2026-05-10" / "example-flaw.md"
        self.path.parent.mkdir(parents=True)
        self.path.write_text(BASE, encoding="utf-8")
        env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.org",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.org"}
        for cmd in (["git", "init", "-q"], ["git", "add", "."], ["git", "commit", "-qm", "base"]):
            subprocess.run(cmd, cwd=self.dir, check=True, env=env, capture_output=True)
        self.base = subprocess.run(["git", "rev-parse", "HEAD"], cwd=self.dir, check=True,
                                   capture_output=True, text=True).stdout.strip()

    def fire(self, earlier_edit: bool):
        """This fire's record and own section; optionally an in-place fix of
        the earlier section's wrong count."""
        text = self.path.read_text(encoding="utf-8")
        text = text.replace("tags: [vulnerability]\n---", RECORD + "tags: [vulnerability]\n---", 1)
        if earlier_edit:
            text = text.replace("counted four hundred affected customers in its first statement",
                                "counted forty affected customers in its first statement")
        self.path.write_text(text + OWN_SECTION, encoding="utf-8")

    def surfaces(self, base: str | None) -> dict[str, list[str]]:
        out: dict[str, list[str]] = {}
        for c in cl.build(RUN, base, root=self.dir):
            out.setdefault(c["surface"], []).append(c["text"])
        return out

    def close(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def _git_or_skip(name: str) -> bool:
    if shutil.which("git") is None:
        print(f"  skip {name}: no git")
        return False
    return True


def test_earlier_section_edit_is_listed():
    if not _git_or_skip("test_earlier_section_edit_is_listed"):
        return
    s = Store()
    try:
        s.fire(earlier_edit=True)
        got = s.surfaces(s.base)
        earlier = got.get(f"section {EARLIER}", [])
        assert len(earlier) == 1 and "forty affected customers" in earlier[0], earlier
        assert f"section {OWN}" in got, "the fire's own section is always listed"
        assert "body" not in got, "the untouched main analysis stays out"
    finally:
        s.close()


def test_untouched_earlier_section_stays_out():
    if not _git_or_skip("test_untouched_earlier_section_stays_out"):
        return
    s = Store()
    try:
        s.fire(earlier_edit=False)
        got = s.surfaces(s.base)
        assert f"section {EARLIER}" not in got, got.keys()
        assert f"section {OWN}" in got and f"record {OWN}" in got
    finally:
        s.close()


def test_repointed_citation_counts_as_changed():
    if not _git_or_skip("test_repointed_citation_counts_as_changed"):
        return
    s = Store()
    try:
        s.fire(earlier_edit=False)
        text = s.path.read_text(encoding="utf-8").replace(
            "([Agency, 2026-05-12](https://example.org/kev))",
            "([Agency, 2026-05-12](https://example.org/kev-entry))")
        s.path.write_text(text, encoding="utf-8")
        earlier = s.surfaces(s.base).get(f"section {EARLIER}", [])
        assert len(earlier) == 1 and "catalogue of exploited flaws" in earlier[0], earlier
    finally:
        s.close()


def test_without_base_scope_is_unchanged():
    if not _git_or_skip("test_without_base_scope_is_unchanged"):
        return
    s = Store()
    try:
        s.fire(earlier_edit=True)
        got = s.surfaces(None)
        assert f"section {EARLIER}" not in got, "no base: earlier sections are not diffed"
        assert "body" in got, "no base: a declared body is listed whole"
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
