# Prior-iteration deltas (iteration 2 NEEDS_FIXES → iteration 3 post-fix pass)

| finding | entry | remediation applied | verify in this iteration |
|---|---|---|---|
| F4 CVE mapping half-reversed (introduced by the iteration-1 fix) | php-critical-release-pre-announced-cve-2026-109618-109619 | sentence now says Sansec assigns the upload-progress memory disclosure to CVE-2026-109618 while the PHP advisories list memory disclosure and session upload progress under CVE-2026-109619, both put the fatal-backtrace path under 109619, and the PHP advisories are the authority | against Sansec's table and GHSA-6wmf-4rv5-p3rp / GHSA-w8hw-w9fx-j79w |
| F3 LiteLLM Exposure list is Socket's | litellm-1-107-0-pypi-docker-credential-stealer-lookalike | Socket citation added beside the vendor post on that clause | citation |
| F11 LiteLLM loader stated as capability | same | title says "dormant remote-code loader"; summary says the loader "could execute code" and that Socket saw its pointer empty at 13:01 UTC; body adds the empty-body sentence from Socket; the Wiz credential-abuse sentence was merged into the Detection line to stay within the word limit | summary, title and body consistent with Socket and Wiz |
| F3 + F5 ARTEX Microsoft half uncited; malformed link | artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse | Microsoft link added to the first half; the broken "(Microsoft, 2026-10-21](" link repaired | links render |
| F11 ARTEX 327-account spray duplicated | same | sentence removed here (kept in the ConnectWise update section) | no duplicate |
| F3 PHP update-section time spread cited to CERT-EU alone | php-critical-release-pre-announced-cve-2026-109618-109619 | ENISA and Sansec links added to the clause | citation |
| F11 PHP "when these sources were read" | same | "as of the early morning of 2026-10-22 UTC" | wording |
| F3 PAN-OS multipart attack path cited to php.net | pan-os-panorama-php2shell-mgmt-interface-no-fixed-release | multipart clause removed from Detection (it keeps "no cited source says which PAN-OS logs record request bodies") | no uncited extrapolation |
| F18 PAN-OS actions[0] duplicates the CVE-2026-0322 entry's task | same | actions: [] | empty actions acceptable |
| F11 k0t reference to the CVE-2026-0322 entry unsupported | k0t-fortiweb-fortigate-globalprotect-edge-device-campaign | reference removed; product:palo-alto-networks-pan-os entity removed again (it caused the dedup WARN against the 0322 entry; the registry relation stays) | references and entities |
| F11 Cisco "the same run" | cve-2026-76466-cisco-expressway-cluster-unauth-root-rce | "The same day Cisco ships"; summary "Cisco's disclosure of 2026-10-21" | wording |
| F11 GitLab fragment quote | cve-2026-110264-gitlab-org-mode-renderer-unauth-rce | quote extended to "only one public project that can hold the .org payload" | quote verbatim on the page |
| F3 OVH advisory date label | ovhcloud-cli-release-assets-replaced-secret-stealing-build | sources[].date and the six inline labels for GHSA-862f-55f5-vmvw now 2026-10-20 (the advisory's publication date) | labels |

Declined again: OVH `envchecker` folder name and extension name (F11 advisory; iteration 2 itself calls leaving it defensible).
