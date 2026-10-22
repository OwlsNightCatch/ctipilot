#!/usr/bin/env python3
"""Look up EUVD records for CVE ids via the EUVD search API (repair-2 helper)."""
import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "tools"))
import fetch_source as fs  # noqa: E402

out = pathlib.Path(__file__).resolve().parent / "src"
for cve in sys.argv[1:]:
    url = f"{fs.ENISA_EUVD_API_BASE}/api/search?text={cve}&size=10"
    try:
        data = fs.fetch_json(url)
    except Exception as exc:  # noqa: BLE001
        print(cve, "ERROR", exc)
        continue
    (out / f"euvd-search-{cve}.json").write_text(json.dumps(data, indent=2))
    items = data.get("items", data) if isinstance(data, dict) else data
    for it in (items or []):
        if not isinstance(it, dict):
            continue
        print(cve, it.get("id"), it.get("aliases", "").replace("\n", " "), it.get("baseScore"),
              it.get("baseScoreVersion"), it.get("baseScoreVector"), it.get("datePublished"))
