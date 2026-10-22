# Prior-iteration deltas (iteration 4 NEEDS_FIXES → iteration 5 post-fix pass)

| finding | entry | remediation applied | verify in this iteration |
|---|---|---|---|
| F3 Publica "as Inside IT relays" covered the 100 GB figure | publica-pk-softech-supplier-malware-intrusion-data-outflow | summary: Tamedia carries the 100 GB, the ransom and the assumed scope; Inside IT relays the actor and the demand, Netzwoche the demand and the scope | attribution against the three pages |
| F3 LiteLLM "domain imitating the project's" cited to Socket only | litellm-1-107-0-pypi-docker-credential-stealer-lookalike | Detection now says "a look-alike health-check endpoint" (Socket's wording) | wording against Socket |
| F8 Cisco standalone Expressway | cve-2026-76466-cisco-expressway-cluster-unauth-root-rce | Exposure: standalone unit is outside the CVE-2026-76466 statement but still needs X15.5.20 for the hardening fixes Cisco lists for every Expressway-C/E regardless of configuration (own citation); action and takeaway now say every Expressway, clustered ones first | against the Expressway hardening advisory |
| F8 GitLab host-level code-execution hunt | cve-2026-110264-gitlab-org-mode-renderer-unauth-rce | Detection adds Puma child processes, new git-owned files in the temporary directory, outbound connections, changed crontabs or SSH keys for the git user, merged with the secrets sentence; two phrases trimmed elsewhere to stay within the word limit | against org_mode_render_error_burst write-up |
| F8 k0t private-data-encryption caveat | k0t-fortiweb-fortigate-globalprotect-edge-device-campaign | Exposure states Fortinet's warning about install errors and split-brain on FortiManager-managed or HA FortiGates; action carries the FortiOS floor and the pointer to that note | against FG-IR-19-007 |
| F9 k0t Fortinet vs Group-IB on administrator secrets and FIPS-CC | same | body now says Group-IB reports administrator credentials although Fortinet's advisory excludes the administrator's password and says FIPS-CC devices are not impacted; Exposure says "except FIPS-CC models"; body trimmed (noPac, the priorities sentence, search-engine clause) to stay within the word limit | both sources |

Declined again: OVH envchecker folder and extension name (advisory, iteration 4 says the main agent may leave it).
