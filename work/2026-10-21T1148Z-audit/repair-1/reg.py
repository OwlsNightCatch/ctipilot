import sys, yaml
d = yaml.safe_load(open('entities/registry.yaml'))['entities']
for term in sys.argv[1:]:
    t = term.lower()
    for e in d:
        labels = [e.get('key',''), e.get('name','')] + list(e.get('aliases') or [])
        if any(t in str(l).lower() for l in labels):
            print(term, '|', e['key'], '|', e.get('name'), '|', e.get('aliases'), '| merged_into=' + str(e.get('merged_into')) if e.get('merged_into') else '')
