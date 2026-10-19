"""Print the cached body path(s) for a URL from this audit's quote-bodies cache,
or with --grep "<text>" report whether the text occurs verbatim (whitespace-normalised)."""
import hashlib, sys, re
from pathlib import Path
D = Path(__file__).resolve().parent / "quote-bodies"
url = sys.argv[1]
key = hashlib.sha1(url.encode()).hexdigest()[:16]
paths = sorted(D.glob(f"{key}.*.txt"))
if "--grep" in sys.argv:
    q = " ".join(sys.argv[sys.argv.index("--grep") + 1].split())
    for p in paths:
        t = " ".join(p.read_text(errors="replace").split())
        print(p.name, "HIT" if q in t else "miss")
    if not paths: print("NOT CACHED")
else:
    print("\n".join(str(p) for p in paths) or "NOT CACHED")
