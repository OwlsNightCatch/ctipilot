import sys,re,json,html
from html.parser import HTMLParser
src=sys.argv[1]; out=sys.argv[2]
raw=open(src,encoding='utf-8',errors='replace').read()
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tables=[]; s.cur=None; s.row=None; s.cell=None; s.depth=0; s.lasttext=[]; s.headings=[]; s.intable=0
        s.buf=[]
    def handle_starttag(s,tag,attrs):
        if tag=='table':
            s.intable+=1
            s.cur={'rows':[], 'before':' '.join(s.buf[-6:])}
        elif tag=='tr' and s.cur is not None:
            s.row=[]
        elif tag in('td','th') and s.row is not None:
            s.cell=[]
        elif tag=='br' and s.cell is not None:
            s.cell.append(' ')
    def handle_endtag(s,tag):
        if tag in('td','th') and s.cell is not None and s.row is not None:
            s.row.append(re.sub(r'\s+',' ',''.join(s.cell)).strip()); s.cell=None
        elif tag=='tr' and s.row is not None and s.cur is not None:
            s.cur['rows'].append(s.row); s.row=None
        elif tag=='table':
            s.intable-=1
            if s.cur is not None:
                s.tables.append(s.cur); s.cur=None
    def handle_data(s,d):
        d=d.strip()
        if s.cell is not None: s.cell.append(d+' ')
        elif not s.intable and d:
            s.buf.append(re.sub(r'\s+',' ',d))
p=P(); p.feed(raw)
json.dump(p.tables,open(out,'w'),indent=1)
print(len(p.tables),[len(t['rows']) for t in p.tables])
