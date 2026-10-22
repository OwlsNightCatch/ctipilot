import difflib, re, subprocess, sys
sys.path.insert(0, "tools")
import check_run as cr
for rel in sys.argv[1:]:
    before = subprocess.run(["git", "show", f"HEAD:{rel}"], capture_output=True, text=True).stdout
    after = open(rel, encoding="utf-8").read()
    _, bb = cr._frontmatter_and_body(before)
    _, ba = cr._frontmatter_and_body(after)
    ma, sa = cr.cm.split_update_sections(ba)
    mb, sb = cr.cm.split_update_sections(bb)
    def words(parts):
        text = re.sub(r"\s*\(\s*\[[^\]\n]+\]\([^)\s]+\)(?:\s*[;·,]\s*\[[^\]\n]+\]\([^)\s]+\))*\s*\)", "", "\n".join(parts))
        text = re.sub(r"\]\([^)]*\)", "]", text)
        return text.split()
    pa = [ma.strip()] + [f"{s.get('at')}\n{(s.get('body') or '').strip()}" for s in sa if not str(s.get('at')).startswith('2026-10-21')]
    pb = [mb.strip()] + [f"{s.get('at')}\n{(s.get('body') or '').strip()}" for s in sb]
    wa, wb = words(pb), words(pa)
    n = sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in difflib.SequenceMatcher(a=wa, b=wb, autojunk=False).get_opcodes() if t != "equal")
    print(rel, "changed_words=", n)
