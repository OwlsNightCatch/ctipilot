import re
def load(p): return open(p,encoding='utf-8').read()
def save(p,s): open(p,'w',encoding='utf-8').write(s)
def cut_sentence(s,start,end_marker,repl=''):
    i=s.index(start); j=s.index(end_marker,i)+len(end_marker)
    return s[:i]+repl+s[j:]
# HPE
p='entries/2026-10-23/hpesbnw05162-hpe-aruba-aos-8-aos-10-72-cves-19-unauth.md'; s=load(p)
s=cut_sentence(s,"HPE's workaround is to restrict the CLI and web-based management interfaces","docLocale=en_US)).")
s=s.replace("CVE-2026-95788, CVE-2026-95789, CVE-2026-95790 and CVE-2026-95791 were added, all below CVSS 3.1 9.0","CVE-2026-95788 to CVE-2026-95791 were added, all below CVSS 3.1 9.0")
a="apply the management-segment restriction at once where the upgrade has to wait"
assert s.count(a)==1
s=s.replace(a,"apply HPE's management-segment restriction (a dedicated layer 2 segment or VLAN behind firewall policy) at once where the upgrade has to wait")
save(p,s)
# Trend
p='entries/2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap.md'; s=load(p)
i=s.index("The Apex Central readme says the patch upgrades the bundled PHP module to build 8.2.35 and names PHP2Shell (")
j=s.index("The customer advisory KA-0024802, updated 2026-11-18",i)
s=s[:i]+"Both patches upgrade the bundled PHP module to 8.2.35, and only the Apex Central readme names PHP2Shell ([Trend Micro, 2026-11-05](https://files.trendmicro.com/documentation/readme/CP/apexcentral_win_en_criticalpatch_b7351_Readme.html); [Trend Micro, 2026-11-09](https://files.trendmicro.com/documentation/readme/Apex%20One/2020/apex_one_2019_win_cp_b20113_EN_hotfix_Readme.html)). "+s[j:]
s=cut_sentence(s,"NetApp's knowledge-base article names all ONTAP web services as affected","(https://kb.netapp.com/on-prem/ontap/Ontap_OS/OS-KBs/How_to_apply_ONTAP_workarounds_for_PHP2SHELL_vulnerabilities)). ")
save(p,s)
# OptimJack
p='entries/2026-11-17/optimjack-poisoned-vendor-scripts-skimmer-iphone-router.md'; s=load(p)
s=cut_sentence(s,"Report URI saw a mass clean-up of the Optimizely snippets between about 20:40 and 21:10 UTC on 2026-11-16, and a snippet that was cleaned and then re-infected shows the writer still had access at that point (","optimizely/)).")
s=cut_sentence(s,"The BBC and HSBC UAE Optimizely files also embed a full fallback copy","optimizely/))."  ) if False else s
save(p,s)
