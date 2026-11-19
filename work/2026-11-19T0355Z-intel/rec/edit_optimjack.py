p='entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router.md'
s=open(p,encoding='utf-8').read()
def rep(old,new,cnt=1):
    global s
    assert s.count(old)==cnt,(old[:80],s.count(old)); s=s.replace(old,new)
ST="https://status.optimizely.com/incidents/ftw0fh9wx43z"
ZS="https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript"
rep('headline: "OptimJack: Optimizely confirms an exploited flaw; Report URI counts 178 organisations served poisoned scripts"',
    'headline: "OptimJack: Optimizely names the exploited signup-flow flaw; Report URI counts 178 organisations, Zscaler 450+ domains"')
rep("Optimizely says an unauthorized party exploited a vulnerability in its Experimentation product to add malicious JavaScript to some customer projects, and Report URI counts 178 organisations that served the code on 2026-11-16, among them a crypto clipper and card skimmer in the Optimizely files.",
    "Optimizely says an unauthorized party exploited a flaw in its Web Experimentation account signup flow to impersonate users and add malicious JavaScript to some customer projects, fewer than 5% of its customers, and Report URI counts 178 organisations that served the code on 2026-11-16 while Zscaler ThreatLabz counts more than 450 domains, among them a crypto clipper and card skimmer in the Optimizely files.")
rep('  - url: "STATUS"\n    publisher: "Optimizely status page"\n    date: "2026-11-17"'.replace('STATUS',ST),
    '  - url: "STATUS"\n    publisher: "Optimizely status page"\n    date: "2026-11-18"'.replace('STATUS',ST))
rep('    publisher: "Report URI Blog (Scott Helme)"\n    date: "2026-11-16"\n    role: corroborating\nclosed_sources: []',
    '    publisher: "Report URI Blog (Scott Helme)"\n    date: "2026-11-16"\n    role: corroborating\n  - url: "ZSURL"\n    publisher: "Zscaler ThreatLabz"\n    date: "2026-11-18"\n    role: corroborating\nclosed_sources: []'.replace('ZSURL',ZS))
rep('''    source_url: "https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/"
verification: multi-source''','''    source_url: "https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/"
  - quote: "On 16 November 2026, an unauthorized third party exploited a flaw in the Optimizely Web Experimentation account signup flow."
    publisher: "Optimizely status page"
    source_url: "STATUS"
  - quote: "ThreatLabz identified more than 450 unique domains and more than 3,000 URLs serving the malicious script."
    publisher: "Zscaler ThreatLabz"
    source_url: "ZSURL"
verification: multi-source'''.replace('STATUS',ST).replace('ZSURL',ZS))
rep("and Optimizely's own status entry confirms an exploited vulnerability on its side.",
    "and Optimizely's own status entry confirms an exploited vulnerability on its side and, since 2026-11-18, names it as a weakness in the Web Experimentation account signup flow that let the attacker impersonate users on targeted accounts. Zscaler ThreatLabz states neither the vantage point nor the time window of its count of more than 450 domains, so it is not reconciled with Report URI's 178 organisations.")
rep("treat the payment, login and form pages that loaded an affected Optimizely file as exposed to card and session theft.\"\nupdates:",
    "treat the payment, login and form pages that loaded an affected Optimizely file as exposed to card and session theft.\"\n  - \"If your organisation or an agency building its sites has an Optimizely Web Experimentation account, audit every Project JavaScript field for code nobody wrote, review account-creation events and administrative access, and rotate the API tokens, session tokens and integration keys tied to it, because the attacker impersonated users on targeted accounts to edit that field.\"\nupdates:")
rep("Optimizely says an unauthorized party exploited a vulnerability in Experimentation to add the JavaScript to some customer projects and that it has fixed the flaw, naming no flaw class or count ([Optimizely, 2026-11-17](STATUS)). Hudson Rock recovered nine poisoned vendor files itself and names 21 web properties, among them BBC, Zoom, GitLab's marketing site, HSBC UAE and the University of Basel".replace('STATUS',ST),
    "Optimizely says an unauthorized party exploited a flaw in its Web Experimentation account signup flow on 2026-11-16 to impersonate users on targeted customer accounts and insert malicious JavaScript into their projects, that it closed the vulnerability within three hours of detection, that this was not a credentials breach and that fewer than 5% of its customers were affected ([Optimizely, 2026-11-18](STATUS)); Zscaler ThreatLabz counts more than 450 unique domains and more than 3,000 URLs serving the script ([Zscaler ThreatLabz, 2026-11-18](ZSURL)). Hudson Rock names 21 web properties, among them BBC, Zoom, HSBC UAE and the University of Basel".replace('STATUS',ST).replace('ZSURL',ZS))
rep("; Optimizely names only an exploited vulnerability ([Optimizely, 2026-11-17](STATUS)).".replace('STATUS',ST),
    "; Zscaler advises customers to review recent changes, user activity, account creation events and administrative access in the Optimizely account, to audit all Project JavaScript fields for unauthorized code and to rotate the Optimizely API tokens, session tokens and integration keys ([Zscaler ThreatLabz, 2026-11-18](ZSURL)).".replace('ZSURL',ZS))
rep("; the status entry names no flaw class, CVE, count or stolen credentials ([Optimizely, 2026-11-17](STATUS)). The status entry covers".replace('STATUS',ST),
    "; that post named no flaw class, CVE or count, and the status entry's later post of 2026-11-18 is described below ([Optimizely, 2026-11-18](STATUS)). The status entry covers".replace('STATUS',ST))
open(p,'w',encoding='utf-8').write(s)
print('ok')
