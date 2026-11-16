#!/usr/bin/env python3
"""Phase 5 source bookkeeping for 2026-11-16T0356Z-intel (run-local, forensic copy)."""
import json
import yaml
from pathlib import Path

ROOT = Path('/home/user/ctipilot')
RUN = '2026-11-16T0356Z-intel'
TODAY = '2026-11-16'
SJ = ROOT / 'sources' / 'sources.json'
d = json.loads(SJ.read_text(encoding='utf-8'))
recs = {r['id']: r for r in d['sources']}

attempted, rows = [], {}
for dom in ('S1', 'S2', 'S3', 'S4'):
    y = yaml.safe_load(open(ROOT / 'work' / RUN / f'findings.{dom}.yaml'))
    ids = []
    for r in y['source_ledger']:
        if r.get('attempted'):
            ids.append(r['id'])
            rows[r['id']] = r
    attempted.append((dom, ids))
(ROOT / 'work' / RUN / 'sources_attempted.json').write_text(
    json.dumps({k: v for k, v in attempted}, indent=1))

all_ids = [i for _, ids in attempted for i in ids]
# transport-level failures (nothing readable on any rung); 403 never demotes
FAILED = {'belden-psirt', 'sygnia', 'ico-uk', 'lab52'}
# fetched AND used in this run's published work (the FBI FLASH reached the run through the BleepingComputer feed)
USED = {'bleepingcomputer'}

changes = {'quiet': [], 'failed': [], 'used': [], 'notes': [], 'added': [], 'promoted': []}
for i in dict.fromkeys(all_ids):
    r = recs.get(i)
    if r is None:
        continue
    if i in FAILED:
        r['consecutive_fetch_failures'] = int(r.get('consecutive_fetch_failures') or 0) + 1
        changes['failed'].append(i)
    elif i in USED:
        r['last_successful_fetch'] = TODAY
        r['consecutive_quiet_periods'] = 0
        r['consecutive_fetch_failures'] = 0
        changes['used'].append(i)
    else:
        r['consecutive_quiet_periods'] = int(r.get('consecutive_quiet_periods') or 0) + 1
        r['consecutive_fetch_failures'] = 0
        changes['quiet'].append(i)

NOTES = {
    'ico-uk': "2026-11-16 (intel): the main host answers 403 on every rung (bridge ico-uk.enforcement, extract, WebFetch) and the reader pool is dead. The Welsh mirror cy.ico.org.uk is not blocked: `url --direct https://cy.ico.org.uk/sitemap.xml` gives <loc>/<lastmod> pairs and the news pages read with `extract`.",
    'europol-newsroom': "2026-11-16 (intel): recipe confirmed. Item dates come from `url --direct <item URL>` (datePublished); the body is in window.SERVER_DATA node.body.",
    'tio-ch-attacco-informatico': "2026-11-16 (intel): `url --direct https://www.tio.ch/temi/attacco-informatico` gives the current headlines with article hrefs (the extract capture of the topic page stays stale); `extract` of each article reads cleanly.",
    'nict-cynex-lettice': "2026-11-16 (intel): `python3 tools/fetch_source.py url https://cynex.nict.go.jp/js/data/library-results.json --direct` returns the full dated item list without reader credit; newest item then was 2026-10-13.",
    'le-monde-info': "2026-11-16 (intel): the site is now Next.js; cybersecurity items sit under /cybersecurite-conformite/<slug> hrefs, and the old /actualites/lire-*.html pattern returns nothing.",
    'vd-grand-conseil': "2026-11-16 (intel): `extract` of the sessions list drops hrefs; use `url --direct` and match the detail-seance links.",
    'connectwise-trust-center': "2026-11-16 (intel): the Trust Center answers 403 on every transport; the CNA repository's commits API reads with `url --direct`, and the advisory text comes from `commits/<sha>` patch output.",
    'darkreading': "2026-11-16 (intel): `extract` on article URLs was served by the metered jina reader; use the feed and pivot to the named primaries instead.",
    'github-advisory': "2026-11-16 (intel): `url --direct 'https://api.github.com/advisories?severity=critical&per_page=30&sort=published&direction=desc'` works unauthenticated and was the only weekend-capable sweep.",
    'msrc-update-guide': "2026-11-16 (intel): the OData revised-CVE sweep with isMariner eq false and $orderby=latestRevisionDate desc works, and the revisions array carries each revision's text; `msrc release` rows carry no exploited or publiclyDisclosed values.",
    'helpnetsecurity': "2026-11-16 (intel): front-page `extract` still returns raw HTML; match the dated hrefs with a regex.",
}
for i, n in NOTES.items():
    r = recs[i]
    r['notes'] = (r.get('notes') or '').rstrip() + ' | ' + n
    changes['notes'].append(i)

# promotion due per the state digest (candidate cited by >= 3 distinct runs)
aw = recs['arctic-wolf-labs']
aw['status'] = 'active'
aw['notes'] = (aw.get('notes') or '').rstrip() + ' | 2026-11-16 (intel): promoted to active: the digest counts published entries from 5 distinct runs citing it.'
changes['promoted'].append('arctic-wolf-labs')

NEW = [
    {
        'category': ['gov', 'vulns'],
        'consecutive_failures': 0,
        'consecutive_fetch_failures': 0,
        'consecutive_quiet_periods': 0,
        'fetch_method': 'rss',
        'first_seen': TODAY,
        'id': 'cis-msisac-advisories',
        'language': ['en'],
        'last_successful_fetch': TODAY,
        'publisher': 'Center for Internet Security (MS-ISAC) Cybersecurity Advisories',
        'reliability': 'B',
        'rss_url': 'https://www.cisecurity.org/feed/advisories',
        'status': 'candidate',
        'tier': 'standard',
        'url': 'https://www.cisecurity.org/advisory',
        'notes': "Added 2026-11-16 as a candidate (promote to active after 3 contributing runs). Public-sector (state and local government) multi-vendor advisory stream; the feed read on the direct transport with 15 dated items (2026-10-27 to 2026-11-11, e.g. the Microsoft November patch row, Fortinet, SAP, Chrome, SonicWall) and gives a dated cross-vendor release calendar that doubles as a scheduled-release check for S1. An aggregator of vendor advisories, so reliability B and each item traces to the vendor's own page.",
    },
    {
        'category': ['gov'],
        'consecutive_failures': 0,
        'consecutive_fetch_failures': 0,
        'consecutive_quiet_periods': 0,
        'fetch_method': 'rss',
        'first_seen': TODAY,
        'id': 'bka-presseportal',
        'language': ['de'],
        'last_successful_fetch': TODAY,
        'publisher': 'Bundeskriminalamt press releases (presseportal.de, Dienststelle 7)',
        'reliability': 'A',
        'rss_url': 'https://www.presseportal.de/rss/dienststelle_7.rss2',
        'status': 'candidate',
        'tier': 'standard',
        'url': 'https://www.presseportal.de/blaulicht/nr/7',
        'notes': "Added 2026-11-16 as a candidate (promote to active after 3 contributing runs). German federal police primary for Operation Endgame and other cybercrime takedowns: the BKA and ZIT release of 2026-11-12 carried the StealC rebuild fact that Europol's text lacks. The feed read on the direct transport with 5 dated items, no reader needed. Serves the law-enforcement line of the policy watch.",
    },
]
for n in NEW:
    assert n['id'] not in recs
    d['sources'].append(n)
    changes['added'].append(n['id'])

d['last_updated'] = TODAY
SJ.write_text(json.dumps(d, indent=1, ensure_ascii=True) + '\n', encoding='utf-8')
(ROOT / 'work' / RUN / 'sources_changed.json').write_text(json.dumps(changes, indent=1))
print({k: len(v) for k, v in changes.items()})
