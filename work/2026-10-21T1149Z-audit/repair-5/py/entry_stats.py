"""Headline length, main-analysis words, em dashes, parse check for entries."""
import re, sys
sys.path.insert(0, '/home/user/ctipilot/site')
import content_model as cm
for p in sys.argv[1:]:
    raw = open(p, encoding='utf-8').read()
    fm, body = raw.split('\n---\n', 1)
    import yaml
    d = yaml.safe_load(fm.lstrip('-\n'))
    main, secs = cm.split_update_sections(body)
    rx = re.compile(r"\[([^\]\n]*)\]\((?:https?://)[^)\s]*\)")   # check_run _MD_LINK_TEXT_RE
    words = len(re.sub(r"\s+", " ", rx.sub(r"\1", main)).split())
    reader = '\n'.join([str(d.get('title')), str(d.get('headline')), str(d.get('summary')),
                        str(d.get('sourcing_note')), str(d.get('actions'))]
                       + [l for l in body.splitlines() if not l.startswith('## ')])
    print(p.split('/')[-1][:60], '| headline', len(str(d.get('headline')).strip()),
          '| title', len(str(d.get('title')).strip()), '| main words', words,
          '| em dashes', reader.count('—'), '| sections', [s.get('at') for s in secs])
