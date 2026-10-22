#!/usr/bin/env python3
import sys, re, pathlib
sys.path.insert(0, '/home/user/ctipilot/site')
import content_model as cm
root=pathlib.Path('/home/user/ctipilot')
SELF=re.compile(r'\b(this entry|the entry|this brief|in this brief|brief series|tracked here|migrated|first covered|previously[- ]covered|§ ?\d|ctipilot|this run|this pipeline|Inclusion gate|cves\[\]|techniques\[\]|actions\[\])', re.I)
for eid in sys.argv[1:]:
    p=root/f'entries/{eid}.md'
    e=cm.load_entry(p, root=root)
    txt=p.read_text()
    fm, body = cm.split_frontmatter(txt)
    probs=[]
    reader={'title':e.get('title'),'headline':e.get('headline'),'summary':e.get('summary'),'sourcing_note':e.get('sourcing_note')}
    for i,a in enumerate(e.get('actions') or []): reader[f'actions[{i}]']=a if isinstance(a,str) else str(a)
    for k,v in reader.items():
        if v and '—' in str(v): probs.append(f'emdash in {k}')
        if v and SELF.search(str(v)): probs.append(f'selfref in {k}: {SELF.search(str(v)).group(0)}')
    if e.get('headline') and len(e['headline'])>120: probs.append(f"headline {len(e['headline'])} chars")
    for n,line in enumerate(body.split('\n')):
        if re.match(r'^## (Update|Correction|Improvement) — ', line): continue
        if '—' in line: probs.append(f'emdash body line {n}: {line[:60]}')
        for m in re.finditer(r'(?<![\w.])\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?![\w.])', line):
            pre=line[max(0,m.start()-9):m.start()].lower()
            if 'version' not in pre and 'release' not in pre: probs.append(f'ipv4-like {m.group(0)} line {n}')
        for m in re.finditer(r'\bT1\d{3}(\.\d{3})?\b', line): probs.append(f'T-id in prose {m.group(0)}')
        if SELF.search(line): probs.append(f'selfref body line {n}: {SELF.search(line).group(0)}')
    for c in e.get('cves') or []:
        for k,v in c.items():
            if isinstance(v,str) and '—' in v: probs.append(f'emdash cves {k}')
    # citations must point at sources[]
    srcs={s['url'] for s in e.get('sources') or []}
    for u in re.findall(r'\]\((https?://[^)\s]+)\)', body):
        if u not in srcs: probs.append(f'cited not in sources: {u}')
    for s in srcs:
        if s not in body: probs.append(f'source never cited in body: {s}')
    main, secs = cm.split_update_sections(e.get('body') or '')
    words=len(re.sub(r"\s+"," ",re.sub(r"\[([^\]]*)\]\([^)]*\)",r"\1",main)).split())
    lim=1100 if e.get('deep_dive') else 550
    if words>lim: probs.append(f'main analysis {words} words > {lim}')
    sd={s['url']:str(s.get('date') or '') for s in e.get('sources') or []}
    for m in re.finditer(r"\[[^\]\n]*?(\d{4}-\d{2}-\d{2})\]\((https?://[^)\s]+)\)", e.get('body') or ''):
        if m.group(2) in sd and sd[m.group(2)]!=m.group(1): probs.append(f'citation date {m.group(1)} != source {sd[m.group(2)]} for {m.group(2)[:60]}')
    print(eid, 'OK' if not probs else '', f'({words} words)')
    for x in probs: print('   ', x)
