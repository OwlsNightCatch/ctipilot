# Prior-iteration deltas (iteration 5 NEEDS_FIXES → iteration 6 post-fix pass)

| finding | entry | remediation applied | verify in this iteration |
|---|---|---|---|
| F3 LiteLLM Defender takeaway attributed Socket's and Wiz's points to the maintainers | litellm-1-107-0-pypi-docker-credential-stealer-lookalike | takeaway now: rotate every credential the host could reach (maintainers' post), because removing the package does not remove the startup files (Socket) and stolen cloud credentials were in use within hours (Wiz); rebuild from a reviewed release and pin container digests (Socket); move to 1.106.2 or an explicit earlier version as the maintainers advise (maintainers' post); "clean machine" dropped; body trimmed (temporary-directory, container-layers and a few connective phrases) to stay within the word limit | each clause against its cited page |
| F3 Publica main analysis: "Inside IT relays" covered the 100 GB | publica-pk-softech-supplier-malware-intrusion-data-outflow | sentence now: Tamedia's Tages-Anzeiger reports ... holds about 100 GB ... and demands ransom, "which Inside IT relays without the volume" | attribution |
| F4 Cisco "the reachable interface is the clustering database service" | cve-2026-76466-cisco-expressway-cluster-unauth-root-rce | Exposure: "the affected component is the database service"; Detection: "connections to the database service" | Cisco's wording |

Declined again: LiteLLM omitting the March hardening and an earlier-coverage reference (advisory; no earlier LiteLLM entry overlaps on CVE or entity beyond what the registry already links); OVH envchecker folder and extension name (advisory, declined in iterations 1 to 5).
