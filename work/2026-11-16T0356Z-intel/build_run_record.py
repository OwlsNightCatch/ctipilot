#!/usr/bin/env python3
"""Write runs/2026-11-16/2026-11-16T0356Z-intel.md (skeleton telemetry; verification filled by Phase 5.7)."""
import json
import yaml
from pathlib import Path

ROOT = Path('/home/user/ctipilot')
RUN = '2026-11-16T0356Z-intel'
att = json.loads((ROOT / 'work' / RUN / 'sources_attempted.json').read_text())

sa = {
    'S1': dict(started_at='2026-11-16T03:58:33Z', ended_at='2026-11-16T04:21:22Z', duration_seconds=1369, items_returned=4,
               used=[], tel=dict(webfetch_calls=6, websearch_calls=13, bridge_fetches=95)),
    'S2': dict(started_at='2026-11-16T03:58:32Z', ended_at='2026-11-16T04:24:13Z', duration_seconds=1541, items_returned=5,
               used=[], tel=dict(webfetch_calls=2, websearch_calls=28, bridge_fetches=120)),
    'S3': dict(started_at='2026-11-16T03:58:33Z', ended_at='2026-11-16T04:21:40Z', duration_seconds=1387, items_returned=7,
               used=[], tel=dict(webfetch_calls=2, websearch_calls=9, bridge_fetches=100)),
    'S4': dict(started_at='2026-11-16T03:58:32Z', ended_at='2026-11-16T04:22:11Z', duration_seconds=1419, items_returned=10,
               used=['bleepingcomputer'], tel=dict(webfetch_calls=3, websearch_calls=24, bridge_fetches=70)),
}
sub_agents = {}
for k, v in sa.items():
    sub_agents[k] = {
        'model': 'Sonnet 5.5', 'model_id': 'claude-sonnet-5-5',
        'started_at': v['started_at'], 'ended_at': v['ended_at'], 'duration_seconds': v['duration_seconds'],
        'sources_attempted': att[k], 'sources_used': v['used'],
        'items_returned': v['items_returned'], 'returned': True, 'telemetry': v['tel'],
    }

fm = {
    'schema': 1, 'run_id': RUN, 'kind': 'intel', 'date': '2026-11-16',
    'started': '2026-11-16T03:56:35Z', 'completed': '2026-11-16T05:00:54Z', 'duration_seconds': 3859,
    'model': 'Sonnet 5.5', 'model_id': 'claude-sonnet-5-5', 'prompt_version': 'v4.25',
    'window_hours': 26, 'gap_hours': 24.0,
    'entries_published': 0, 'entries_updated': 1,
    'updated_entry_ids': ['2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse'],
    'deep_dive': None,
    'sub_agents': sub_agents,
    'fetch_failures': [
        {'id': 'belden-psirt', 'url_tried': 'https://www.belden.com/security', 'fetch_method': 'bridge:extract', 'status_code': 403,
         'error_class': 'transport-403', 'error_message': '403 on every transport; the reader pool answered 402 on every key',
         'attempted_methods': ['bridge:extract', 'webfetch', 'bridge:jina'],
         'mitigation_applied': 'none; candidate record, Belden products already appear in earlier PHP2Shell entries', 'covered_anyway': False},
        {'id': 'sygnia', 'url_tried': 'https://www.sygnia.co/blog/', 'fetch_method': 'bridge:extract', 'status_code': 403,
         'error_class': 'transport-403', 'error_message': 'direct 403 on extract and WebFetch, no trafilatura body, reader pool exhausted',
         'attempted_methods': ['bridge:extract', 'webfetch', 'websearch'],
         'mitigation_applied': 'none; the record is pinned fetch_method blocked and earlier fires failed the same way', 'covered_anyway': False},
        {'id': 'lab52', 'url_tried': 'https://lab52.io/blog/feed/', 'fetch_method': 'bridge:feed', 'status_code': 'n/a',
         'error_class': 'transport-timeout', 'error_message': 'feed connection reset, WebFetch HTTP 503; extract returned six undated cards through the reader with no hrefs',
         'attempted_methods': ['bridge:feed', 'webfetch', 'bridge:extract'],
         'mitigation_applied': 'none; no in-window Lab52 item could be identified', 'covered_anyway': False},
        {'id': 'ico-uk', 'url_tried': 'https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/', 'fetch_method': 'bridge:ico-uk.enforcement', 'status_code': 403,
         'error_class': 'transport-403', 'error_message': 'upstream HTTP 403 on the sitemap, extract and WebFetch; reader pool exhausted',
         'attempted_methods': ['bridge:ico-uk.enforcement', 'bridge:extract', 'webfetch', 'websearch'],
         'mitigation_applied': 'WebSearch found no ICO action dated in the window; S2 found the Welsh mirror cy.ico.org.uk unblocked, recorded as a recipe note', 'covered_anyway': False},
    ],
    'bridge_uses': [
        {'id': 'cisa-kev', 'method': 'tools/fetch_source.py cisa-kev and tools/kev_window_diff.py',
         'outcome': 'success: catalogue 2026.11.13, no addition dated inside the window; no covered CVE changed its ransomware flag'},
        {'id': 'extract', 'method': 'tools/fetch_source.py extract',
         'outcome': 'success on vendor, CERT and news pages and on the deep reads (Proofpoint, Symantec, BleepingComputer); a 403-walled host now ends in a long chain of reader 402 messages before it fails'},
        {'id': 'url-direct', 'method': 'tools/fetch_source.py url --direct',
         'outcome': 'success: GitHub APIs, MSRC OData, CNA commits API, tio.ch and cy.ico.org.uk, edoeb sitemap; HTTP 500 on every safeonweb.be path'},
        {'id': 'pdf', 'method': 'tools/fetch_source.py pdf',
         'outcome': 'success: the FBI FLASH PDF, 13 pages decoded (22 of 50 streams)'},
        {'id': 'feed', 'method': 'tools/fetch_source.py feed',
         'outcome': 'success on BleepingComputer, heise, databreaches.net, borncity and the research blogs'},
        {'id': 'jina-reader', 'method': 'tools/fetch_source.py jina (last rung)',
         'outcome': 'dead: HTTP 402 on every pooled key and 401 on the anonymous tier; extract falls through to it silently on direct failure'},
    ],
    'sources_changed': [
        {'change': 'added candidate', 'id': 'cis-msisac-advisories',
         'reason': 'public-sector multi-vendor advisory feed that reads direct with 15 dated items and gives a cross-vendor release calendar for the S1 scheduled-release duty'},
        {'change': 'added candidate', 'id': 'bka-presseportal',
         'reason': 'German federal police primary for Operation Endgame and other takedowns; carried a fact (StealC rebuild) that Europol lacks; feed reads direct'},
        {'change': 'status', 'id': 'arctic-wolf-labs', 'from': 'candidate', 'to': 'active',
         'reason': 'promotion_due in the state digest: cited by published entries from 5 distinct runs'},
        {'change': 'max_staleness_days', 'id': 'edoeb-ch-press',
         'reason': 'health flagged the listing stale at 61 days; the regulator releases a few items per quarter and the listing is a stale cache, the sitemap recipe finds the real releases; limit set to 120'},
        {'change': 'notes', 'id': 'safeonweb-be',
         'reason': 'health still classes a shell; the whole host answers HTTP 500 on every path and language, a server-side outage with nothing to repair; kept active, a 5xx never demotes'},
        {'change': 'notes', 'id': 'ico-uk, europol-newsroom, tio-ch-attacco-informatico, nict-cynex-lettice, le-monde-info, vd-grand-conseil, connectwise-trust-center, darkreading, github-advisory, msrc-update-guide, helpnetsecurity',
         'reason': 'recipe corrections and confirmations found by the sub-agents (Welsh ICO mirror, Europol dates, tio.ch topic page, NICT JSON list, Le Monde Next.js paths, Vaud detail links, CNA commits API, Dark Reading extract falling to the reader, GitHub advisories API, MSRC OData filter, Help Net Security hrefs)'},
        {'change': 'consecutive_fetch_failures', 'id': 'belden-psirt, sygnia, ico-uk, lab52',
         'reason': 'transport failures on every route (no demotion: 403 or anti-bot blocks never demote)'},
        {'change': 'last_successful_fetch', 'id': 'bleepingcomputer',
         'reason': 'fetched and used: the FBI FLASH on ARTEX reached the run through its feed'},
        {'change': 'consecutive_quiet_periods', 'id': '(71 slice records)',
         'reason': '200 but nothing publishable in the horizon: counters incremented by one'},
    ],
    'entities_added': [],
    'entries_dropped_by_verification': 0,
    'publish_status': 'pending', 'publish_checked_at': None, 'publish_note': None,
    'verification_iterations': 3, 'verification_residual_count': 0,
    'verification': {'confirmation_waived': None, 'iterations': [
        {'n': 1, 'model': 'Sonnet 5.5', 'model_id': 'claude-sonnet-5-5', 'subagent_type': 'cti-verification',
         'started_at': '2026-11-16T04:38:57Z', 'ended_at': '2026-11-16T04:45:40Z', 'duration_seconds': 403,
         'verdict': 'NEEDS_FIXES', 'truth': 1, 'editorial': 2, 'advisory': 1, 'claims_in_scope': 14, 'claims_checked': 14,
         'findings': [
            {'code': 'F9', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The new section relays the FBI advice to keep ConnectWise connections disabled until ConnectWise gives restoration instructions, although ConnectWise had already published them on 2026-10-28.',
             'remediation_applied': 'fixed: the clause was removed; the section keeps the FBI review-by-application-ID request and its advice not to delete the enterprise application before evidence is preserved'},
            {'code': 'F8', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The section drops the FLASH hardening levers (restrict Kudu/SCM, disable basic publishing authentication, inventory peripheral internet-facing applications), so the newest section gives no decision for the exposure it introduces.',
             'remediation_applied': 'fixed: the final paragraph now carries the FBI recommendations; the main analysis, already over its length bound, was left unedited'},
            {'code': 'F14', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': '(low confidence) "ten sectors" in the headline, summary and record summary is the pipeline count of a list the FLASH introduces with "including"; the FLASH states no number.',
             'remediation_applied': 'fixed: headline says many sectors, summary and record summary name sectors without a count; the run record no longer says ten'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'T1059.001 is absent from techniques[] although the section describes PowerShell enumeration, and the XXE metadata query is grouped under internal networks while the FLASH lists it under privilege escalation.',
             'remediation_applied': 'fixed: T1059.001 added and the sentence regrouped as privilege escalation and internal discovery'}]},
        {'n': 2, 'model': 'Sonnet 5.5', 'model_id': 'claude-sonnet-5-5', 'subagent_type': 'cti-verification',
         'started_at': '2026-11-16T04:47:19Z', 'ended_at': '2026-11-16T04:53:54Z', 'duration_seconds': 395,
         'verdict': 'CLEAN', 'truth': 0, 'editorial': 0, 'advisory': 3, 'claims_in_scope': 15, 'claims_checked': 15,
         'findings': [
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The frontmatter summary is six long sentences against the documented 1 to 3 sentences; each update appended one.',
             'remediation_applied': 'left: advisory; accurate, the audit may tighten the summary'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': '(low confidence) The FLASH collection row lists T1074.002 and the section describes new 100 GB volumes, but techniques[] has no T1074 id; the FLASH does not tie the id to a bullet.',
             'remediation_applied': 'left: advisory; no source ties the id to the described behaviour'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The record summary omits the ConnectWise-tenant review ask that the section states; not an overstatement.',
             'remediation_applied': 'left: advisory'}]},
        {'n': 3, 'model': 'Sonnet 5.5', 'model_id': 'claude-sonnet-5-5', 'subagent_type': 'cti-verification',
         'started_at': '2026-11-16T04:54:50Z', 'ended_at': '2026-11-16T04:59:39Z', 'duration_seconds': 289,
         'verdict': 'CLEAN', 'truth': 0, 'editorial': 0, 'advisory': 4, 'claims_in_scope': 15, 'claims_checked': 15,
         'findings': [
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The frontmatter summary is about 243 words in five long sentences against the 1 to 3 sentence contract (carried over from iteration 2).',
             'remediation_applied': 'left: advisory'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': '(low confidence) The Exposure and Defender takeaway lines still read identity-only while the newest section carries non-identity levers from the FBI; the takeaway is attributed to Expel and not disproved.',
             'remediation_applied': 'left: advisory; the main analysis already exceeds its length bound and the new levers sit in the section'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': '(low confidence) "Telemetry the FBI lists" includes IAM DryRun-flag tests, which the FLASH puts in its observed-activity row rather than its indicator lists; techniques[] has no T1074.002.',
             'remediation_applied': 'left: advisory; the item is the FBI observed behaviour and the lead-in sits within the FLASH content'},
            {'code': 'F11', 'entry': '2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse',
             'summary': 'The sourcing_note is now about ten sentences against the two-sentence provenance standard; accurate.',
             'remediation_applied': 'left: advisory; the audit may tighten it'}]},
    ]},
}

body = open(ROOT / 'work' / RUN / 'record_body.md', encoding='utf-8').read()
class D(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

out = '---\n' + yaml.dump(fm, Dumper=D, sort_keys=False, allow_unicode=True, width=100000) + '---\n\n' + body
p = ROOT / 'runs' / '2026-11-16' / f'{RUN}.md'
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(out, encoding='utf-8')
print('wrote', p, len(out))
