import re,sys,html
def text(path):
    s=open(path,encoding='utf-8',errors='replace').read()
    s=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',s)
    # newline for block-level closes, empty string otherwise (no injected spaces)
    s=re.sub(r'(?i)</(p|div|li|tr|h[1-6]|section|article|br|blockquote)\s*>','\n',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s)
    s=re.sub(r'\n{3,}','\n\n',s)
    return s
if __name__=='__main__':
    for p in sys.argv[1:]:
        open(p.replace('raw.','txt.'),'w',encoding='utf-8').write(text(p))
        print(p, '->', p.replace('raw.','txt.'))
