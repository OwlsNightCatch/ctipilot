import re,sys,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
t=re.sub(r'(?is)<(script|style)\b.*?</\1>','',t)
t=re.sub(r'(?i)</(p|div|li|tr|h[1-6]|br|section|table|ul|ol)>','\n',t)
t=re.sub(r'(?i)<br\s*/?>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[2],'w').write(t)
