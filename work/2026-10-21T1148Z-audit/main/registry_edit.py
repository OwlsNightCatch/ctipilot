"""Apply the repair workers' registry changes block by block (cleanup wave 04).

Usage: python3 registry_edit.py <ops.json>

Each op edits one entity block of entities/registry.yaml and re-emits only
that block, so every other byte of the file stays as it was (tools/merge_state.py
merges the registry per block). Ops:
  {"op": "set", "key": K, "field": F, "value": V}
  {"op": "add_alias", "key": K, "alias": A}       {"op": "remove_alias", "key": K, "alias": A}
  {"op": "add_relation", "key": K, "rel": {"to", "type", "source", "note"?}}
  {"op": "new", "entity": {...}}                   appended at the end of the file
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
REG = ROOT / "entities" / "registry.yaml"
ORDER = ["key", "type", "name", "aliases", "ambiguous_labels", "nexus", "summary",
         "first_seen", "merged_into", "relations"]


def q(v):
    if v is None:
        return "null"
    if isinstance(v, (dt.date, dt.datetime)):
        return v.isoformat()
    if isinstance(v, bool):
        return "true" if v else "false"
    return json.dumps(str(v), ensure_ascii=False)


def emit(e: dict) -> str:
    out = []
    keys = [k for k in ORDER if k in e] + [k for k in e if k not in ORDER]
    for i, k in enumerate(keys):
        lead = "  - " if i == 0 else "    "
        v = e[k]
        if k == "relations" and not v:
            out.append(f"{lead}relations: []")
        elif k == "relations":
            out.append(f"{lead}relations:")
            for r in v:
                rk = [x for x in ("to", "type", "source", "note") if x in r] + \
                     [x for x in r if x not in ("to", "type", "source", "note")]
                for j, x in enumerate(rk):
                    val = r[x] if x != "type" else r[x]
                    s = val if x == "type" else q(val)
                    out.append(("      - " if j == 0 else "        ") + f"{x}: {s}")
        elif isinstance(v, list):
            out.append(f"{lead}{k}: [" + ", ".join(q(x) for x in v) + "]")
        elif k == "first_seen" and isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
            out.append(f"{lead}{k}: {v}")
        elif k in ("type", "nexus") and v is not None:
            out.append(f"{lead}{k}: {v}")
        else:
            out.append(f"{lead}{k}: {q(v)}")
    return "\n".join(out) + "\n"


def blocks(text: str):
    starts = [m.start() for m in re.finditer(r"(?m)^  - key: ", text)]
    return starts


def find(text: str, key: str):
    starts = blocks(text)
    for i, s in enumerate(starts):
        line = text[s:text.index("\n", s)]
        if line.strip() in (f'- key: "{key}"', f"- key: {key}"):
            end = starts[i + 1] if i + 1 < len(starts) else len(text)
            return s, end
    raise KeyError(key)


def main():
    ops = json.load(open(sys.argv[1]))
    text = REG.read_text(encoding="utf-8")
    for op in ops:
        if op["op"] == "new":
            e = op["entity"]
            try:
                find(text, e["key"])
                raise SystemExit(f"exists: {e['key']}")
            except KeyError:
                pass
            if not text.endswith("\n"):
                text += "\n"
            text += emit(e)
            print("new", e["key"])
            continue
        s, end = find(text, op["key"])
        e = yaml.safe_load("entities:\n" + text[s:end])["entities"][0]
        if op["op"] == "set":
            e[op["field"]] = op["value"]
        elif op["op"] == "add_alias":
            if op["alias"] not in e.setdefault("aliases", []):
                e["aliases"].append(op["alias"])
        elif op["op"] == "remove_alias":
            e["aliases"] = [a for a in e.get("aliases") or [] if a != op["alias"]]
        elif op["op"] == "add_relation":
            rels = e.setdefault("relations", [])
            if not any(r.get("to") == op["rel"]["to"] and r.get("type") == op["rel"]["type"] for r in rels):
                rels.append(op["rel"])
        else:
            raise SystemExit(f"unknown op {op}")
        text = text[:s] + emit(e) + text[end:]
        print(op["op"], op["key"], op.get("field") or op.get("alias") or (op.get("rel") or {}).get("to") or "")
    REG.write_text(text, encoding="utf-8")
    yaml.safe_load(REG.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
