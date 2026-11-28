---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Palo Alto Networks PAN-OS and Panorama: the PHP2Shell flaws affect every release below its train's hotfix through the management web interface, and Palo Alto reports active exploitation against internet-exposed management interfaces; all twenty hotfixes are out"
headline: "PAN-OS management interfaces rooted via PHP2Shell and a kernel flaw, both exploited per Palo Alto: hotfix, then check"
summary: >
  Palo Alto Networks' advisory, first published on 2026-10-21 and revised since, says active exploitation has been observed against PAN-OS management interfaces exposed to the
  internet, and Dream Research, with Unit 42's verification, reports a custom PHP2Shell build chained with a Linux kernel flaw that rooted 25 PAN-OS
  firewall and management servers in the United States, Japan, Taiwan and South Korea and went on to attack a US government-affiliated Active
  Directory. The advisory lists every release below the hotfix for its train, of PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and of Panorama, as affected through the management web
  interface by CVE-2026-109618 and CVE-2026-109619 (CVSS-B 9.2); all twenty hotfixes are released, and GlobalProtect and the captive portal are not
  affected. Palo Alto's bulletin PAN-SA-2026-0015 of 2026-11-24 says exploitation of that kernel flaw has been observed against internet-exposed management interfaces and lists a
  later hotfix per train that fixes it. A device that was exposed and unpatched needs a compromise check as well as the hotfix, and CISA added both PHP flaws to its Known
  Exploited Vulnerabilities catalog on 2026-10-26.
discovered_at: "2026-10-22T03:41:00Z"
updated_at: "2026-11-27T04:53:00Z"
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, patch-available]
regions: [global]
sectors: []
entities: ["product:php", "product:palo-alto-networks-pan-os", "product:palo-alto-networks-panorama", "tool:php2shell", "trend:dirty-frag-linux-kernel-page-cache-lpe", "actor:cl-unk-1280", "campaign:php2shell-pan-os-fragnesia-rooting-2026-10"]
techniques: [T1190, T1068, T1505.003, T1572, T1090, T1543.002, T1037.004, T1110.003, T1087.002, T1552.004]
affected_products: ["Palo Alto Networks PAN-OS", "Palo Alto Networks Panorama"]
cves:
  - id: CVE-2026-109618
    cvss: "9.2 (CVSS-B 4.0, Palo Alto's rating of the PAN-OS impact with management reachable from the internet; 7.7 where it is reachable only from an adjacent network)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (every release below the hotfix for its train); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "Released per the advisory as read on 2026-10-30: 12.2.4-h1; 12.1.4-h13, 12.1.7-h11, 12.1.10-h3; 11.2.4-h23, 11.2.7-h23, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 11.2.13-h4, 11.2.16-h1; 11.1.4-h38, 11.1.6-h40, 11.1.7-h12, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4; 10.2.7-h39, 10.2.10-h42, 10.2.13-h27, 10.2.16-h12, 10.2.18-h13; Panorama: the table no longer distinguishes it from the PAN-OS trains"
  - id: CVE-2026-46300
    cvss: null
    epss: null
    type: lpe
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "PAN-OS software below the bulletin's hotfix for its train; the bulletin has no affected-version table and says nothing on Panorama, Prisma Access or Cloud NGFW for this flaw"
    fixed: "12.2.4-h3; 12.1.4-h15, 12.1.7-h15, 12.1.10-h6; 11.2.4-h25, 11.2.7-h25, 11.2.10-h19, 11.2.13-h6, 11.2.16-h3; 11.1.4-h40, 11.1.6-h42, 11.1.7-h14, 11.1.10-h38, 11.1.13-h18, 11.1.16-h6; 10.2.7-h41, 10.2.10-h45, 10.2.13-h29, 10.2.16-h14, 10.2.18-h15"
  - id: CVE-2026-109619
    cvss: "9.2 (CVSS-B 4.0, Palo Alto's rating of the PAN-OS impact with management reachable from the internet; 7.7 where it is reachable only from an adjacent network)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 (every release below the hotfix for its train); Panorama (PAN-OS software on virtual and M-Series appliances; the advisory table has no separate Panorama row); WildFire Appliance WF-500 and WF-500-B are listed as unaffected after the correction of 2026-10-23"
    fixed: "Released per the advisory as read on 2026-10-30: 12.2.4-h1; 12.1.4-h13, 12.1.7-h11, 12.1.10-h3; 11.2.4-h23, 11.2.7-h23, 11.2.10-h16 (11.2.10-h17 adds the Brotli fix), 11.2.13-h4, 11.2.16-h1; 11.1.4-h38, 11.1.6-h40, 11.1.7-h12, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4; 10.2.7-h39, 10.2.10-h42, 10.2.13-h27, 10.2.16-h12, 10.2.18-h13; Panorama: the table no longer distinguishes it from the PAN-OS trains"
sources:
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    date: "2026-10-21"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-23)"
    date: "2026-10-23"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-24)"
    date: "2026-10-24"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    date: "2026-10-25"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history)"
    date: "2026-10-25"
    role: primary
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, 2026-10-27)"
    date: "2026-10-27"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
    publisher: "Palo Alto Networks Unit 42 (threat brief, revised 2026-10-25)"
    date: "2026-10-25"
    role: corroborating
  - url: "https://www.php.net/archive/2026.php#2026-10-21-5"
    publisher: "PHP (security advisory)"
    date: "2026-10-21"
    role: corroborating
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    date: "2026-10-28"
    role: primary
  - url: "https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, Internet Archive copy of 2026-10-27 17:10 UTC)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.27)"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.11.25)"
    date: "2026-11-25"
    role: corroborating
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, as read on 2026-10-28)"
    date: "2026-10-28"
    role: corroborating
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-29)"
    date: "2026-10-29"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, as read on 2026-10-29)"
    date: "2026-10-29"
    role: corroborating
  - url: "https://security.paloaltonetworks.com/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-30)"
    date: "2026-10-30"
    role: primary
  - url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, as read on 2026-10-30)"
    date: "2026-10-30"
    role: corroborating
  - url: "https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
    publisher: "Dream Research (report on the chained PHP2Shell and Fragnesia exploit against PAN-OS, updated 2026-10-29)"
    date: "2026-10-29"
    role: primary
  - url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
    publisher: "Palo Alto Networks Unit 42 (threat brief, updated 2026-10-29)"
    date: "2026-10-29"
    role: primary
  - url: "https://security.paloaltonetworks.com/PAN-SA-2026-0015"
    publisher: "Palo Alto Networks PSIRT (bulletin PAN-SA-2026-0015)"
    date: "2026-11-24"
    role: primary
closed_sources: []
evidence:
  - quote: "Current analysis shows no impact of CVE-2026-115560 on PAN-OS (NGFW and Panorama)."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue will be fixed in the upcoming releases of PAN-OS."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-25)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "removed the ETA for 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 as these versions are released"
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history)"
    source_url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
  - quote: "Removed the ETAs for 10.2.13-h27 and 10.2.16-h12 as these versions are released."
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
  - quote: "The only exception is 11.2.10-h16 which only includes the fix for PHP vulnerabilities; 11.2.10-h17 includes fixes for both vulnerabilities."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue strictly affects the management web interface, which includes the HTTPS web UI and XML API service."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue will be fixed in the upcoming releases of PAN-OS."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Active exploitation has been observed targeting the Palo Alto Networks management interface"
    publisher: "Palo Alto Networks PSIRT (advisory, as read on 2026-10-28)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Very limited exploitation has been observed targeting the Palo Alto Networks management interface."
    publisher: "Palo Alto Networks PSIRT (advisory, Internet Archive copy of 2026-10-27 17:10 UTC)"
    source_url: "https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Severity Updated to Critical and Urgency updated as Highest"
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "The risk is highest on PAN-OS when you allow access to the management interface from external IP addresses on the internet."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-27)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "No special configuration is required to be affected by this issue."
    publisher: "Palo Alto Networks PSIRT (advisory, Impact of Critical Vulnerabilities in PHP on Palo Alto Networks Products)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Although WildFire Cloud was previously impacted, a remediation patch was deployed on October 22, 2026."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-23)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "This issue is applicable to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series)."
    publisher: "Palo Alto Networks PSIRT (advisory, revised 2026-10-24)"
    source_url: "https://security.paloaltonetworks.com/CVE-2026-109618"
  - quote: "Removed ETAs for 11.1.7-h12 as the version is released."
    publisher: "Palo Alto Networks PSIRT (advisory record with revision history, as read on 2026-10-30)"
    source_url: "https://security.paloaltonetworks.com/json/CVE-2026-109618"
  - quote: "The affected devices run specific versions of Palo Alto Networks PAN-OS."
    publisher: "Dream Research"
    source_url: "https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
  - quote: "For 22 of the 24 rooted firewalls, the attacker did nothing beyond planting the webshell."
    publisher: "Dream Research"
    source_url: "https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
  - quote: "Palo Alto Networks’ Unit 42 tracks this activity as CL-UNK-1280 and attributes it to a Chinese-speaking attacker in the UTC+8 time zone."
    publisher: "Dream Research"
    source_url: "https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers"
  - quote: "Unit 42 has independently verified the same attacker’s tooling and confirmed the reported results."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
  - quote: "Customers who have applied the available patches are not affected."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/"
  - quote: "Exploitation of CVE-2026-46300 has been observed targeting the Palo Alto Networks management interface exposed to the internet."
    publisher: "Palo Alto Networks PSIRT (bulletin PAN-SA-2026-0015)"
    source_url: "https://security.paloaltonetworks.com/PAN-SA-2026-0015"
  - quote: "The only known way to exploit this vulnerability requires an attacker to first exploit the PHP2Shell vulnerability through an internet-exposed management interface, and we are not aware of any other exploitation method."
    publisher: "Palo Alto Networks PSIRT (bulletin PAN-SA-2026-0015)"
    source_url: "https://security.paloaltonetworks.com/PAN-SA-2026-0015"
verification: multi-source
sourcing_note: >
  Palo Alto Networks' advisory is the first-party record for its own products and the only source for the PAN-OS and Panorama impact and for
  the statement that exploitation has been observed; an Internet Archive copy of 2026-10-27 17:10 UTC says very limited exploitation, and the page
  read on 2026-10-28 says active exploitation, with no matching change recorded in the vendor timeline. The chain, the 25 rooted servers and the attack on the
  Active Directory are Dream Research's account of artifacts it recovered, which Unit 42 says it independently verified; Dream worked with Palo Alto
  Networks, so the two are not fully independent. The CL-UNK-1280 designation comes only from Dream's page. The two PHP flaws are
  described by the PHP project, and the listing of both in CISA's Known Exploited Vulnerabilities catalog comes from the catalog itself. The bulletin PAN-SA-2026-0015 is labelled Informational and carries a zero CVSS block, but its exploitation-status block is Palo Alto's own statement for the kernel flaw; it has no product table.
confidence: high
references:
  - "2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619"
  - "2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x"
  - "2026-10-15/cve-2026-0322-pan-os-management-interface-code-injection"
  - "2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Take the management interface of every PA-Series and VM-Series firewall and Panorama off the internet now by restricting it to a jump box or trusted internal addresses, because Palo Alto reports active exploitation against internet-exposed management interfaces, and install the hotfix PAN-SA-2026-0015 lists for your maintenance release (12.2.4-h3; 12.1.4-h15, 12.1.7-h15, 12.1.10-h6; 11.2.4-h25, 11.2.7-h25, 11.2.10-h19, 11.2.13-h6, 11.2.16-h3; 11.1.4-h40, 11.1.6-h42, 11.1.7-h14, 11.1.10-h38, 11.1.13-h18, 11.1.16-h6; 10.2.7-h41, 10.2.10-h45, 10.2.13-h29, 10.2.16-h14, 10.2.18-h15), which includes the PHP2Shell fix and fixes the kernel flaw as well."
  - "Rotate the directory bind account, HA replication keys, certificate private keys and device authentication keys of every PAN-OS firewall and Panorama that was reachable from the internet while unpatched and shows a PHP web shell or a tunnel, because the chain Dream Research recovered harvested exactly those from rooted firewalls, and the hotfix does not remove a web shell or tunnel already in place."
updates:
  - at: "2026-10-23T03:42:16Z"
    run_id: 2026-10-23T0256Z-intel
    type: update
    summary: >
      Palo Alto Networks' revised advisory now also lists the WildFire appliances WF-500 and WF-500-B as
      affected by the PHP flaws in all versions, schedules hotfix builds of every PAN-OS train between
      2026-10-26 and 2026-10-30, and leaves Panorama and WF-500 undated; Cortex XCORE (SaaS) and WildFire
      Cloud are already remediated.
    fields: [title, headline, summary, entities, affected_products, cves, sources, evidence, body]
  - at: "2026-10-24T03:37:34Z"
    run_id: 2026-10-24T0255Z-intel
    type: update
    summary: >
      Palo Alto Networks' advisory now lists the WildFire appliances WF-500 and WF-500-B as unaffected, a
      correction its timeline dates 2026-10-23, has no separate Panorama row while a note keeps Panorama
      in scope, and extends the Threat Prevention coverage; the PAN-OS hotfix dates of 2026-10-26 to
      2026-10-30 and the exploitation statement are unchanged.
    fields: [affected_products, body, cves, entities, evidence, headline, sources, summary, title]
  - at: "2026-10-25T14:00:17Z"
    run_id: 2026-10-25T1308Z-audit
    type: update
    summary: >
      Palo Alto's revision of 2026-10-25 lists the first three PAN-OS hotfixes (10.2.18-h13, 11.1.16-h4,
      11.2.10-h16) as released, although its solution text still speaks of upcoming releases; the
      remaining hotfixes are due 2026-10-27 to 2026-10-30, and Palo Alto's current analysis finds no
      impact of CVE-2026-115560 on PAN-OS.
    fields: [title, headline, summary, cves, sources, evidence, body, tags, sourcing_note]
  - at: "2026-10-26T03:40:53Z"
    run_id: 2026-10-26T0256Z-intel
    type: correction
    summary: >
      The entry said Unit 42 had seen a proof of concept of the PHP flaws; Unit 42's brief, revised on
      2026-10-25, no longer says so, and the statement is removed.
    fields: [body, evidence, sources, sourcing_note]
  - at: "2026-10-27T05:15:00Z"
    run_id: 2026-10-27T0256Z-intel
    type: update
    summary: >
      Palo Alto Networks now records eleven PAN-OS hotfixes as released (10.2.13-h27, 10.2.16-h12,
      10.2.18-h13, 11.1.4-h38, 11.1.6-h40, 11.1.10-h36, 11.1.13-h16, 11.1.16-h4, 11.2.10-h16, 12.1.7-h11
      and 12.2.4-h1) with nine others due by 2026-10-30; CISA added both PHP flaws to its Known Exploited
      Vulnerabilities catalog on 2026-10-26, while Palo Alto still reports no malicious exploitation
      against its products.
    fields: [actions, body, cves, evidence, headline, sources, sourcing_note, summary, tags, title]
  - at: "2026-10-28T03:38:43Z"
    run_id: 2026-10-28T0256Z-intel
    type: update
    summary: >
      Palo Alto Networks' advisory now says, as read on 2026-10-28, that active exploitation has been
      observed targeting the PAN-OS management interface exposed to the internet, after a copy of
      2026-10-27 said very limited exploitation; severity is Critical with urgency Highest (CVSS-B 9.2, up
      from 8.7 for availability impact only), and the priority moves from notable to high.
    fields: [title, headline, summary, priority, cves, evidence, sourcing_note, actions, body, tags, sources]
  - at: "2026-10-29T07:04:32Z"
    run_id: 2026-10-29T0255Z-intel
    type: update
    summary: >
      Palo Alto's advisory as read on 2026-10-29 shows nineteen of the twenty PAN-OS hotfixes released,
      the ETAs of 10.2.7-h39, 10.2.10-h42, 11.2.4-h23, 12.1.4-h13 and 12.1.10-h3 having been removed, with
      only 11.1.7-h12 still carrying an estimated date of 2026-10-30. The title, headline, summary,
      fixed-release strings, the first action and the hotfix sentences in the text are updated to match.
    fields: [title, headline, summary, updated_at, cves, actions, sources, body]
  - at: "2026-10-30T03:52:50Z"
    run_id: 2026-10-30T0255Z-intel
    type: update
    summary: >
      Palo Alto's advisory timeline of 2026-10-29 23:54 UTC removes the estimated date of 11.1.7-h12
      because the build is released, so all twenty PAN-OS hotfixes are now available and no estimate
      remains; the exploitation statement is unchanged. The title, headline, summary, fixed-release
      strings, the action and the hotfix sentences in the text are updated to match.
    fields: [actions, body, cves, evidence, headline, sources, summary, title]
  - at: "2026-11-01T03:27:57Z"
    run_id: 2026-11-01T0256Z-intel
    type: update
    summary: >
      Dream Research's report, updated 2026-10-29, names Palo Alto Networks PAN-OS as the product behind
      the chain it had first described with an unnamed vendor: a custom PHP2Shell build chained with a
      Linux kernel flaw rooted 25 PAN-OS firewall and management servers and was followed by an attack on
      a US government-affiliated Active Directory, and Unit 42 says it independently verified the tooling
      and results. The advisory's exploitation statement is unchanged; a device that was exposed and
      unpatched needs a compromise check as well as the hotfix, and Dream says the affected web server
      also fronts the GlobalProtect portal, which Palo Alto's advisory lists as not affected.
    fields: [headline, summary, entities, techniques, sources, evidence, verification, sourcing_note, references, actions, body, cves, title]
  - at: "2026-11-01T14:01:22Z"
    run_id: 2026-11-01T1312Z-audit
    type: correction
    internal: true
    summary: >
      The summary dated Palo Alto's active-exploitation statement to the advisory of 2026-10-21; the
      statement came with a later revision (the first text reported no known malicious exploitation, as
      the 2026-10-23 section records), so the summary now says the advisory was first published on
      2026-10-21 and revised since.
    fields: [summary]
  - at: "2026-11-27T04:53:00Z"
    run_id: 2026-11-27T0355Z-intel
    type: update
    summary: >
      Palo Alto's bulletin PAN-SA-2026-0015 (2026-11-24, labelled Informational) says exploitation of the kernel flaw
      CVE-2026-46300 has been observed against internet-exposed management interfaces, which makes the vendor itself a source for
      the second half of the chain Dream Research described, and lists a later hotfix in every train that fixes the kernel flaw as
      well as the PHP flaws.
    fields: [headline, summary, updated_at, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

Palo Alto Networks' advisory of 2026-10-21 lists PAN-OS 12.2, 12.1, 11.2, 11.1 and 10.2 and Panorama as affected by CVE-2026-109618 and CVE-2026-109619, the unauthenticated PHP remote-code-execution flaws ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)) ([PHP, 2026-10-21](https://www.php.net/archive/2026.php#2026-10-21-5)). Only the management web interface is affected; the GlobalProtect portal and gateway and the captive portal are not ([Palo Alto Networks, 2026-10-21](https://security.paloaltonetworks.com/CVE-2026-109618)).

The advisory says active exploitation has been observed against the management interface exposed to the internet ([Palo Alto Networks, 2026-10-28](https://security.paloaltonetworks.com/CVE-2026-109618)). Dream Research reports that a custom PHP2Shell build for the PAN-OS management web server, chained with the Linux kernel flaw CVE-2026-46300 to turn the web server's unprivileged context into root in one unauthenticated HTTPS request, rooted 25 PAN-OS firewall and management servers in the United States, Japan, Taiwan and South Korea ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)). On the second of two firewalls of a US government-affiliated organization (the first crashed) it added a reboot-persistent reverse SSH tunnel and, through it, ran the same chain against the organization's internal firewall management server, decrypted the directory service account's password from the device configuration, enumerated the Active Directory and attempted a password spray and backdoor accounts, which Dream cannot say succeeded ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)). Unit 42 says it independently verified the attacker's tooling and results and that customers who applied the available patches are not affected ([Unit 42, 2026-10-29](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)); Dream relays that Unit 42 tracks it as CL-UNK-1280, a Chinese-speaking attacker in UTC+8, while Dream names none ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)).

All twenty hotfixes are released ([Palo Alto Networks, 2026-10-30](https://security.paloaltonetworks.com/json/CVE-2026-109618)). Palo Alto's bulletin PAN-SA-2026-0015 of 2026-11-24, labelled Informational, says exploitation of the kernel flaw CVE-2026-46300 has been observed against internet-exposed management interfaces and that the only known way to exploit it is PHP2Shell first, so a PHP2Shell hotfix protects against that chain; it lists a later hotfix in every train that also fixes the kernel flaw, to install at the next maintenance interval where management access is restricted and immediately, with access restricted, where it is internet-reachable ([Palo Alto Networks, 2026-11-24](https://security.paloaltonetworks.com/PAN-SA-2026-0015)).

**Exposure:** every PAN-OS firewall and Panorama appliance below its train's hotfix through its management web interface; it is reachable from the internet where the management port, or a dataplane interface with a management profile, answers from outside the administrator range ([Palo Alto Networks, 2026-11-24](https://security.paloaltonetworks.com/PAN-SA-2026-0015)).

**Detection:** in management-plane web access logs, very large multipart POST requests from outside the administrator range ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)). A hotfix does not remove an attacker already in: on an interface that was internet-reachable and unpatched, look for a PHP file nobody deployed in a web-reachable directory of the management web server, a systemd service or rc.local entry that starts scripts from a hidden directory under /usr/local/lib, and outbound SSH from the management plane; in directory logs, bulk LDAP enumeration and password-spray bursts against all users, launched from the firewall management server ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)).

**Defender takeaway:** move management access behind a jump box or trusted internal addresses, as Palo Alto recommends ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/json/CVE-2026-109618)), and install the hotfix for your maintenance line. An interface that was internet-reachable and unpatched is a possible root compromise until those checks are clean; where a web shell or tunnel turns up, rotate what the device held: the directory bind account, HA replication keys, certificate private keys and device authentication keys ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)).

## Update — 2026-10-23T03:42:16Z

Palo Alto Networks revised its advisory on 2026-10-23: the WildFire appliances WF-500 and WF-500-B are now listed as affected in all versions, and the footnotes say Cortex XCORE (SaaS) was remediated on 2026-10-21 and WildFire Cloud on 2026-10-22 ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory now also gives estimated availability dates for hotfix builds of every supported PAN-OS train, from 2026-10-26 (for example 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16) to 2026-10-30, while Panorama and the WildFire appliances remain with no date ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). Palo Alto still states that it is not aware of malicious exploitation against its products, and the Threat Prevention coverage and the jump-box restriction are unchanged ([Palo Alto Networks, 2026-10-23](https://security.paloaltonetworks.com/CVE-2026-109618)). The advisory names the management web interface only for PAN-OS and does not say which interface of the WildFire appliances is reachable.

## Update — 2026-10-24T03:37:34Z

Palo Alto Networks' advisory now lists the WildFire appliances WF-500 and WF-500-B, which an earlier revision of 2026-10-23 had listed as affected, as unaffected, a correction its timeline dates 2026-10-23, and the table no longer distinguishes Panorama while a note says the issue applies to PAN-OS software on PA-Series and VM-Series firewalls and on Panorama (virtual and M-Series) and the mitigation text covers PAN-OS and Panorama together ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)). The estimated hotfix dates for PAN-OS, 2026-10-26 to 2026-10-30, the CVSS-B scores of 8.7 and 7.1, and the statement that Palo Alto Networks is not aware of malicious exploitation against its products are unchanged; on 2026-10-24 the advisory added updated threat-signature and content-version details, and the Threat Prevention coverage now lists twenty further Threat IDs, from 97643 to 97678 ([Palo Alto Networks, 2026-10-24](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-25T14:00:17Z

Palo Alto Networks' revision of 2026-10-25 removed the estimated dates of 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 "as these versions are released" ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/json/CVE-2026-109618)); the advisory's solution text, unrevised, still says the issue will be fixed in upcoming releases of PAN-OS, and every other hotfix carries an estimated date from 2026-10-27 to 2026-10-30 ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)). The FAQ adds that Palo Alto's current analysis shows no impact on PAN-OS firewalls or Panorama of CVE-2026-115560, the new vulnerability PHP announced, and Palo Alto still knows of no malicious exploitation against its products ([Palo Alto Networks, 2026-10-25](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Correction — 2026-10-26T03:40:53Z

Unit 42's brief, revised on 2026-10-25, no longer says that it has seen a proof of concept of the PHP flaws ([Unit 42, 2026-10-25](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)).

## Update — 2026-10-27T05:15:00Z

Palo Alto Networks' advisory now records eleven PAN-OS hotfixes as released: 10.2.18-h13, 11.1.16-h4 and 11.2.10-h16 (revision of 2026-10-25), 11.1.4-h38, 11.1.6-h40, 11.1.10-h36 and 11.1.13-h16 (2026-10-26), and 10.2.13-h27, 10.2.16-h12, 12.1.7-h11 and 12.2.4-h1 (2026-10-27) ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/json/CVE-2026-109618)). Nine hotfixes still carry estimated dates from 2026-10-27 to 2026-10-30, among them 12.1.4-h13, 12.1.10-h3 and four 11.2 lines, and the FAQ says 11.2.10-h16 carries only the PHP fix while 11.2.10-h17 carries the PHP and the Brotli fixes ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)). Palo Alto still says it is not aware of malicious exploitation of this issue against its products ([Palo Alto Networks, 2026-10-27](https://security.paloaltonetworks.com/CVE-2026-109618)). CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26, as the PHP flaws themselves rather than as a PAN-OS finding ([CISA KEV, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

## Update — 2026-10-28T03:38:43Z

Palo Alto Networks' advisory now states that active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet ([Palo Alto Networks, 2026-10-28](https://security.paloaltonetworks.com/CVE-2026-109618)). A copy of the page taken on 2026-10-27 at 17:10 UTC said instead that very limited exploitation had been observed ([Palo Alto Networks, 2026-10-27](https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618)); the vendor timeline records no change of wording, and its entries of 2026-10-27 are two removals of hotfix estimated dates and the 16:40 UTC change that raised the severity to Critical and the urgency to Highest ([Palo Alto Networks, 2026-10-28](https://security.paloaltonetworks.com/json/CVE-2026-109618)). The vendor score is now CVSS-B 9.2 with high impact on confidentiality, integrity and availability when management is reachable from the internet, and 7.7 when it is reachable only from an adjacent network; the earlier text scored availability impact only (8.7) and knew of no exploitation. The advisory names no actor, victim or post-exploitation behaviour. CISA's catalog flags both PHP flaws with forensic triage requirements ([CISA KEV, 2026-10-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The hotfix table has moved on since the previous record: as read on 2026-10-28, fourteen builds are released and six are due by 2026-10-30 ([Palo Alto Networks, 2026-10-28](https://security.paloaltonetworks.com/CVE-2026-109618)).

## Update — 2026-10-29T07:04:32Z

Palo Alto Networks' advisory timeline of 2026-10-29 removes the estimated dates of 10.2.7-h39, 10.2.10-h42, 11.2.4-h23, 12.1.4-h13 and 12.1.10-h3 because those builds are released ([Palo Alto Networks, 2026-10-29](https://security.paloaltonetworks.com/json/CVE-2026-109618)). Nineteen of the twenty hotfixes are now available, and the advisory table gives only 11.1.7-h12 an estimated date, 2026-10-30 ([Palo Alto Networks, 2026-10-29](https://security.paloaltonetworks.com/CVE-2026-109618)). Its exploitation statement is unchanged.

## Update — 2026-10-30T03:52:50Z

Palo Alto Networks' advisory timeline of 2026-10-29 at 23:54 UTC removes the estimated date of 11.1.7-h12 "as the version is released" ([Palo Alto Networks, 2026-10-30](https://security.paloaltonetworks.com/json/CVE-2026-109618)). With it, all twenty PAN-OS hotfixes are available and the advisory table gives no estimated date for any build ([Palo Alto Networks, 2026-10-30](https://security.paloaltonetworks.com/CVE-2026-109618)). The exploitation statement is unchanged.

## Update — 2026-11-01T03:27:57Z

Dream Research updated its report on 2026-10-29 to say that the affected devices run Palo Alto Networks PAN-OS; the operation it had described with an unnamed vendor rooted 25 PAN-OS firewall and management servers, and Unit 42 says it independently verified the attacker's tooling and confirmed the reported results ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers); [Unit 42, 2026-10-29](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)). Dream's recovered artifacts show web shells left on 24 firewalls, 22 of them parked with nothing further done, and a boot-persistent tunnel into the internal network of a US government-affiliated organization that it assesses is likely still active ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers)). Unit 42 says customers who applied the available patches are not affected and that the management interface is not exposed to the internet by default ([Unit 42, 2026-10-29](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/)). Dream also says the management web server fronts the GlobalProtect portal, which Palo Alto's advisory lists as not affected ([Dream Research, 2026-10-29](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers); [Palo Alto Networks, 2026-10-30](https://security.paloaltonetworks.com/CVE-2026-109618)). A device that was exposed and unpatched therefore needs the compromise checks in the Detection line, not only the hotfix.

## Update — 2026-11-27T04:53:00Z

Palo Alto Networks published bulletin PAN-SA-2026-0015 on 2026-11-24 at 23:10 UTC (its timeline's initial-publication entry; the page header reads 2026-11-25), titled "OSS CVEs Fixed in PAN-OS" and labelled Informational with a zero CVSS block; its exploitation-status block reads "Exploitation of CVE-2026-46300 has been observed targeting the Palo Alto Networks management interface exposed to the internet" ([Palo Alto Networks, 2026-11-24](https://security.paloaltonetworks.com/PAN-SA-2026-0015)). CVE-2026-46300 is the Linux kernel flaw Dream Research chained with PHP2Shell, so the vendor now itself states exploitation of the second half of the chain that Dream Research described; CISA's catalog has listed the kernel flaw as exploited since 2026-10-28 ([CISA KEV, 2026-11-25](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). The bulletin's FAQ says all observed exploitation targeted devices with an internet-exposed management interface, that a device on a fixed PAN-OS listed in the PHP2Shell advisory is protected, and that "The only known way to exploit this vulnerability requires an attacker to first exploit the PHP2Shell vulnerability through an internet-exposed management interface, and we are not aware of any other exploitation method"; it still recommends upgrading to a fixed release at the next maintenance interval where management access is restricted, and upgrading immediately and restricting access where the management interface or a dataplane interface with a management profile is internet-reachable ([Palo Alto Networks, 2026-11-24](https://security.paloaltonetworks.com/PAN-SA-2026-0015)).

The bulletin lists the first fixed build for the kernel flaw per train, two to four hotfixes after the PHP2Shell build: 12.2.4-h3; 12.1.4-h15, 12.1.7-h15, 12.1.10-h6; 11.2.4-h25, 11.2.7-h25, 11.2.10-h19, 11.2.13-h6, 11.2.16-h3; 11.1.4-h40, 11.1.6-h42, 11.1.7-h14, 11.1.10-h38, 11.1.13-h18, 11.1.16-h6; 10.2.7-h41, 10.2.10-h45, 10.2.13-h29, 10.2.16-h14, 10.2.18-h15. It has no workaround section and no affected-product table and says nothing on Panorama, Prisma Access or Cloud NGFW for this flaw; its mitigation is restricting management access to trusted internal addresses ([Palo Alto Networks, 2026-11-24](https://security.paloaltonetworks.com/PAN-SA-2026-0015)).
