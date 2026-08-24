import re,html,sys
p=sys.argv[1]
raw=open(p,encoding='utf-8',errors='replace').read()
raw=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>',' ',raw)
raw=re.sub(r'(?i)</(p|div|li|tr|h[1-6]|td|blockquote)>','\n',raw)
raw=re.sub(r'(?i)<br\s*/?>','\n',raw)
txt=re.sub(r'<[^>]+>','',raw)
txt=html.unescape(txt)
lines=[l.strip() for l in txt.split('\n')]
lines=[l for l in lines if l]
out='\n'.join(lines)
o=p.replace('.txt','.clean.txt')
open(o,'w').write(out)
print(o, len(out))
