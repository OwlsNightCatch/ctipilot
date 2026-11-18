import os, re, json
ROOT = '/home/user/ctipilot/work/2026-11-18T0356Z-intel/bodies/FU2/'
_cache = {}
FAILS = []
CHECKED = [0]

def body(rel):
    if rel not in _cache:
        _cache[rel] = open(ROOT + rel, encoding='utf-8', errors='replace').read()
    return _cache[rel]

def chk(rel, passage):
    ok = passage in body(rel)
    CHECKED[0] += 1
    if not ok:
        FAILS.append((rel, passage[:140]))
    return ok

def esc(s):
    return s.replace('|', '\\|').replace('\n', ' ')

def table(rows, header=('claim', 'source URL', 'verbatim passage', 'saved body')):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    for claim, url, rel, passage in rows:
        ok = chk(rel, passage)
        out.append('| %s | %s | "%s"%s | `%s` |' % (esc(claim), url, esc(passage), '' if ok else ' **[NOT FOUND IN BODY]**', rel))
    return '\n'.join(out)
