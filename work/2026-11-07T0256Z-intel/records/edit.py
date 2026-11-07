import sys, re
def apply(path, reps):
    s=open(path,encoding='utf-8').read()
    for old,new in reps:
        n=s.count(old)
        assert n==1, f"count={n} for: {old[:90]!r}"
        s=s.replace(old,new)
    open(path,'w',encoding='utf-8').write(s)
