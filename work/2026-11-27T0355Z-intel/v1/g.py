import re,sys,subprocess
key=sys.argv[1]
h=subprocess.check_output(['./pg.sh',key]).decode().strip()
try:
    t=open(f'pages/{h}.txt').read()
except Exception as e:
    print('NOFILE',key,h); sys.exit()
f=re.sub(r'\s+',' ',t)
w=int(__import__('os').environ.get('W','220'))
print('#####',key,h,len(f))
for kw in sys.argv[2:]:
    ms=list(re.finditer(kw,f,re.I))
    print('##',kw,len(ms))
    for m in ms[:2]: print('   ..',f[max(0,m.start()-w):m.end()+w])
