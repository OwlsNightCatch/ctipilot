FAIL=[]
class E:
    def __init__(s,p): s.p=p; s.s=open(p,encoding='utf-8').read()
    def rep(s,a,b,cnt=1):
        n=s.s.count(a)
        if n!=cnt: FAIL.append((s.p.split('/')[-1][:28],a[:60],n)); return
        s.s=s.s.replace(a,b)
    def save(s): open(s.p,'w',encoding='utf-8').write(s.s)
OB="https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce"
THN="https://thehackernews.com/2026/06/litellm-vulnerability-chain-lets-low.html"
# ---------- LiteLLM
l=E('entries/2026-06-16/obsidian-security-a-three-cve-chain-turns-any-litellm-user-i.md')
l.s=l.s.replace("[Obsidian Security, 2026-06-15]","[Obsidian Security, 2026-06-11]")
l.rep('    publisher: Obsidian Security\n    date: "2026-06-15"','    publisher: Obsidian Security\n    date: "2026-06-11"')
l.rep('cvss: "5.9"','cvss: "5.9 (CVSS 4.0, vendor)"')
l.rep('    affected: "LiteLLM before v1.83.14-stable"\n    fixed: "v1.83.14-stable"\n  - id: CVE-2026-47102','    affected: "LiteLLM before v1.83.14-stable"\n    fixed: "v1.83.14-stable"\n  - id: CVE-2026-47102')
# 47102 per VulnCheck record
i=l.s.index("  - id: CVE-2026-47102"); j=l.s.index("  - id: CVE-2026-40217")
blk=l.s[i:j].replace('affected: "LiteLLM before v1.83.14-stable"','affected: "LiteLLM before 1.83.10 per the VulnCheck record"').replace('fixed: "v1.83.14-stable"','fixed: "1.83.10 per the VulnCheck record; v1.83.14-stable for the whole chain"')
l.s=l.s[:i]+blk+l.s[j:]
l.rep("VulnCheck scores CVE-2026-47102 at CVSS 8.8 (3.1), and Obsidian rates","VulnCheck scores CVE-2026-47102 at CVSS 8.8 (3.1) ([The Hacker News, 2026-06-15](%s)), and Obsidian rates"%THN)
l.rep(" The chain is fixed in v1.83.14-stable, but Obsidian reports broad under-deployment of the fix."," The chain is fixed in v1.83.14-stable, the first release that Obsidian says contains the complete fix set.")
l.rep("and that POST /guardrails/test_custom_code needs a proxy-admin credential in default configurations ([LiteLLM advisory, 2026-05-07](https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p)).","and that POST /guardrails/test_custom_code needs a proxy-admin credential in default configurations ([LiteLLM advisory, 2026-05-07](https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p)); Obsidian also ties CVE-2026-40217 to the production routes POST /guardrails and PUT /guardrails/{id}, which run user code with exec(), while the vendor's workaround names only the test endpoint ([Obsidian Security, 2026-06-11](%s))."%OB)
l.rep("**Detection:** proxy access logs for POST requests to /guardrails/test_custom_code and for","**Detection:** proxy access logs for POST requests to /guardrails/test_custom_code, POST /guardrails and PUT /guardrails/{id}, and for")
l.rep("**Defender takeaway:** upgrade to v1.83.14-stable or later, block the guardrail endpoint at the reverse proxy until then, keep admin endpoints off the internet, and rotate the master key, the salt key and every provider API key on any instance that an untrusted user could reach on an older build.","**Defender takeaway:** upgrade to v1.83.14-stable or later, block the guardrail endpoint at the reverse proxy until then, keep admin endpoints off the internet, and on any instance that an untrusted user could reach on an older build rotate the master key, the salt key and every provider API key and audit every Custom Code Guardrail, the callbacks loaded under litellm_settings.callbacks and the holders of proxy_admin, as Obsidian advises ([Obsidian Security, 2026-06-11](%s))."%OB)
l.rep("until it is in, block POST /guardrails/test_custom_code at the reverse proxy or API gateway; on any instance an untrusted user could reach on an older build, rotate the master key, the salt key and every provider API key, because","until it is in, block POST /guardrails/test_custom_code at the reverse proxy or API gateway; on any instance an untrusted user could reach on an older build, rotate the master key, the salt key and every provider API key and audit every Custom Code Guardrail, the litellm_settings.callbacks entries and every proxy_admin holder, because")
l.rep("The analysis above now uses the advisory's description in place of the earlier statement that the guardrail runs attacker-supplied Python through exec(); v1.83.14-stable remains the fix for the whole chain.","v1.83.14-stable remains the fix for the whole chain.")
l.rep("while the 8.8 on the two other CVEs is VulnCheck's score for CVE-2026-47102 as Obsidian cites it.","while the CNA record held by VulnCheck scores CVE-2026-40217 CVSS 3.1 8.8 with low privileges required, a conflict resolved here in favour of the vendor advisory's CVSS 4.0 5.9 and its proxy-admin prerequisite; the 8.8 on the two other CVEs is VulnCheck's score for CVE-2026-47102 as The Hacker News relays it.")
l.save()
# ---------- nginx
n=E('entries/2026-11-19/nginx-nginx2root-five-unauth-memory-corruption-flaws.md')
n.rep("with the privileges of the worker process (CVSS 4.0 9.2, high attack complexity).","with the privileges of the worker process; NCSC.ch, NCSC-NL and Rapid7 score them CVSS 4.0 9.2.")
n.rep("F5's own K-articles could not be read by any fetch tool, so","F5's K-articles are not publicly readable, so")
n.rep('entities: []','entities: ["product:f5-nginx-open-source", "product:f5-nginx-plus"]')
# cut P1 prerequisites sentence
i=n.s.index("In Xint's tests CVE-2026-121810 needs HTTP/3"); j=n.s.index("\n\nRapid7 published",i)
n.s=n.s[:i].rstrip()+n.s[j:]
n.rep("Rapid7 says execution has the worker's permissions and that execution as the master process or root is not established, and Wiz is not releasing its exploits (","Rapid7 says execution has the worker's permissions and that execution as the master process or root is not established, Wiz says ASLR does not protect against these flaws because attackers can use them to read memory before executing code, and Wiz is not releasing its exploits (")
n.rep("**Defender takeaway:** update and restart nginx, because a configuration reload does not replace the running executable; disabling HTTP/2 on exposed listeners blocks only the two HTTP/2 flaws, and an empty execution-audit result after the update cannot rule out an earlier compromise ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).","**Defender takeaway:** update and restart nginx, because a configuration reload does not replace the running executable; disabling HTTP/2 on exposed listeners blocks only the two HTTP/2 flaws, and Xint gives interim measures for the others: a fixed upstream group in place of request-time DNS lookups for CVE-2026-123634, no QUIC listeners for CVE-2026-121810 and bound or firewalled mail listeners for CVE-2026-113425 ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)). An empty execution-audit result after the update cannot rule out an earlier compromise, and Xint chained CVE-2026-123007 with a separate Linux kernel SCTP flaw, unpatched when it published, to reach root on the host and escape a Docker container; hosts that do not use SCTP can block the module from loading ([Xint, 2026-11-18](https://xint.io/blog/nginx2root-remote-code-execution)).")
n.save()
# ---------- REDCap
r=E('entries/2026-11-19/redcap-cve-2026-90817-unauth-survey-rce-exploited-kev.md')
r.rep("priority: notable","priority: high")
r.rep("references: []",'references: ["2026-06-16/prc-unc6508-ran-year-plus-espionage-through-internet-facing"]')
r.rep("entities: []",'entities: ["product:redcap"]')
r.rep("    publisher: \"Securifera proof-of-concept repository\"","    publisher: \"Securifera proof-of-concept repository\"")
r.rep('closed_sources: []','  - url: "https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research"\n    publisher: "Google GTIG"\n    date: "2026-06-15"\n    role: corroborating\nclosed_sources: []')
r.rep("**Detection:** web access logs for POSTs to public survey URLs with a double percent-encoded passthrough and a Data Import route, and for a php:// stream in the file-name field; transient Blade-template files","**Detection:** web access logs for POSTs to public survey URLs with a double percent-encoded passthrough and a Data Import route ([Unit 42, 2026-10-07](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-10-07-XMRig-campaign-through-CVE-2026-90817.txt)) and, where a WAF or proxy logs request bodies, a php:// stream in the file-name field ([Securifera, 2026-09-27](https://www.securifera.com/blog/2026/09/27/survey-says-remote-code-execution-cve-2026-90817/)); transient Blade-template files")
r.rep("the Data Import controller or carries","the Data Import controller or carries") 
r.rep("REDCap 13.3.0 through 16.0.48 LTS, 17.3.9 LTS and 17.4.3 Standard are vulnerable (","Google's GTIG reported in June 2026 that the PRC-nexus cluster UNC6508 had exploited internet-facing REDCap servers of North American academic and medical organisations ([Google GTIG, 2026-06-15](https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research)). REDCap 13.3.0 through 16.0.48 LTS, 17.3.9 LTS and 17.4.3 Standard are vulnerable (")
r.save()
# ---------- Idunno
x=E('entries/2026-11-19/idunno-anticsrf-cve-2026-131914-exploited-no-patch-w3wp-rce.md')
x.rep('entities: []','entities: ["product:idunno-anticsrf"]')
x.rep("so the fix is to remove the module, rotate the secrets held in the web configuration and check the web root.","so the fix is to remove the module, and Mandiant adds that environments with evidence of exploitation should rotate the secrets held in the web configuration and inspect the web root.")
x.rep("check IIS logs for POSTs to .aspx pages that returned 302 or 500 with unusually large request sizes and rotate the machineKey, encryption keys and database credentials in Web.config and applicationHost.config, because Mandiant observed exploitation and no patch exists.","check IIS logs for POSTs to .aspx pages that returned 302 or 500 with unusually large request sizes and, where there is evidence of exploitation, rotate the machineKey, encryption keys and database credentials in Web.config and applicationHost.config, treating an internet-reachable server that ran the module as a candidate for the same rotation because request bodies are rarely logged, since Mandiant observed exploitation and no patch exists.")
x.rep("and process-creation telemetry for children of w3wp.exe, which follows from code execution in the worker (","and process-creation telemetry for children of w3wp.exe, which follows from code execution in the worker; if the csrfSettings section is omitted from Web.config, a setter bug overwrites the fallback form field name with RaiseException, so the default field name is not a reliable hunting key on every deployment (")
x.save()
print('FAIL',FAIL)
