"""Run check_run's quote-skeleton and CVE-clause logic on my entries against saved bodies."""
import json, re, sys
sys.path.insert(0, '/home/user/ctipilot/tools'); sys.path.insert(0, '/home/user/ctipilot/site')
import check_run as cr, content_model as cm, yaml
S = '/home/user/ctipilot/work/2026-10-21T1149Z-audit/repair-5/src/'
T = '/home/user/ctipilot/work/2026-10-21T1149Z-audit/truth-T1/'
def txt(f): return open(f, encoding='utf-8', errors='replace').read()
def cvrf_vuln(month, cve):
    d = json.load(open(T + 'cvrf-2026-%s.json' % month))
    return json.dumps([v for v in d['Vulnerability'] if v.get('CVE') == cve])
BODIES = {
 'https://www.bleepingcomputer.com/news/security/windows-bitlocker-zero-day-gives-access-to-protected-drives-poc-released/': [txt(S+'bc-yellowkey.txt')],
 'https://www.theregister.com/security/2026/05/13/disgruntled-researcher-releases-two-more-microsoft-zero-days/5239758': [txt(S+'reg-yellowkey-clean.txt')],
 'https://security-hub.ncsc.admin.ch/#/posts/12574': [txt(S+'ncsc-12574.txt')],
 'https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-45585': [txt(S+'msrc-cve-CVE-2026-45585.json'), cvrf_vuln('May','CVE-2026-45585')],
 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45585': [txt(S+'msrc-cve-CVE-2026-45585.json'), cvrf_vuln('May','CVE-2026-45585')],
 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-45586': [txt(S+'msrc-cve-CVE-2026-45586.json'), cvrf_vuln('Jun','CVE-2026-45586')],
 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2020-17103': [txt(S+'msrc-cve-CVE-2020-17103.json')],
 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62911': [txt(S+'msrc-cve-CVE-2026-62911.json'), cvrf_vuln('Aug','CVE-2026-62911')],
 'https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42897': [txt(S+'msrc-cve-CVE-2026-42897.json')],
 'https://www.bleepingcomputer.com/news/microsoft/microsoft-patches-yellowkey-greenplasma-miniplasma-zero-days/': [txt(S+'bc-patches.txt')],
 'https://www.bleepingcomputer.com/news/microsoft/new-windows-miniplasma-zero-day-exploit-gives-system-access-poc-released/': [txt(S+'bc-miniplasma.txt')],
 'https://therecord.media/microsoft-calls-zero-day-releases-never-justifiable-as-researcher-threatens-more': [txt(S+'record.txt')],
 'https://www.heise.de/en/news/Too-many-zero-days-Microsoft-threatens-legal-action-11310736.html': [txt(S+'heise.txt')],
 'https://www.microsoft.com/en-us/msrc/blog/2026/05/a-shared-responsibility-protecting-customers-through-coordinated-vulnerability-disclosure': [txt(S+'msrc-blog.txt')],
 'https://github.com/TryGhost/Ghost/security/advisories/GHSA-w52v-v783-gw97': [txt(S+'ghsa-repo-clean.txt')],
 'https://blog.xlab.qianxin.com/ghost-cms-mass-compromised-via-cve-2026-26980-now-fueling-clickfix-attacks/': [txt(S+'xlab.txt')],
 'https://www.bleepingcomputer.com/news/security/ghost-cms-sql-injection-flaw-exploited-in-large-scale-clickfix-campaign/': [txt(S+'bc-ghost.txt')],
 'https://www.thezdi.com/blog/2026/5/16/pwn2own-berlin-2026-day-three-results-and-master-of-pwn': [txt(S+'zdi-d3.txt')],
 'https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results': [txt(S+'zdi-d2.txt')],
 'https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results': [txt(S+'zdi-d1.txt')],
 'https://www.bleepingcomputer.com/news/security/pwn2own-day-two-hackers-demo-microsoft-exchange-windows-11-red-had-enterprise-linux-zero-days/': [txt(S+'bc-d2.txt')],
 'https://hackread.com/pwn2own-berlin-2026-hits-capacity-hackers-0-days/': [txt(S+'hackread.txt')],
 'https://www.zerodayinitiative.com/blog/2026/3/11/announcing-pwn2own-berlin-for-2026': [txt(S+'zdi-announce.txt')],
 'https://www.zerodayinitiative.com/Pwn2OwnBerlin2026Rules.html': [txt(S+'zdi-rules.txt')],
 'https://www.frankysweb.de/en/exchange-public-exploit-for-critical-vulnerability-cve-2026-62911/': [txt(S+'frankys.txt')],
 'https://vred.mbbank.com.vn/p/analysis-of-exchange-server-pre-auth': [txt(S+'mbvred.txt')],
}
SK = {u: [cr._quote_skeleton(b) for b in bs] for u, bs in BODIES.items()}
for p in sys.argv[1:]:
    raw = open(p, encoding='utf-8').read()
    fm, body = raw.split('\n---\n', 1)
    d = yaml.safe_load(fm.lstrip('-\n'))
    eid = p.split('entries/')[1][:-3]
    for ev in d.get('evidence') or []:
        u = ev.get('source_url'); q = ev.get('original') or ev.get('quote')
        ok = u in SK and any(cr._quote_skeleton(q) in b for b in SK[u])
        print('QUOTE', 'ok ' if ok else 'MISS', eid[:40], (u or '')[:60], q[:60])
    main, secs = cm.split_update_sections(body)
    own = [s_['body'] for s_ in secs if str(s_.get('at','')).startswith('2026-10-21')]
    for text in [main] + own:
        for clause, urls in cr._citation_clauses(text):
            for cve in sorted({c.upper() for c in cr._CVE_ID_RE.findall(clause)}):
                pat = re.compile(re.escape(cr._quote_skeleton(cve)) + r'(?!\d)')
                miss = [u for u in urls if u not in SK]
                hit = any(pat.search(b) for u in urls for b in SK.get(u, []))
                print('CVE  ', 'ok ' if hit else ('UNREAD' if miss else 'MISS'), eid[:40], cve, [u[-40:] for u in urls])
