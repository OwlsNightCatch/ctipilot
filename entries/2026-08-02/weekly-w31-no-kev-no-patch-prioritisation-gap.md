---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Both standard prioritisation feeds failed in the same week — an exploited flaw absent from KEV, and four critical flaws with no fix to apply"
headline: "W31 broke KEV-driven and patch-driven triage at once: exploited-but-unlisted, and critical-but-unfixable"
summary: >
  A vulnerability process built on two signals — is it in CISA's Known Exploited Vulnerabilities catalog, and
  is there a patch — had blind spots on both axes this week. VulnCheck observed attackers exploiting Langflow
  through CVE-2026-0769, a pre-auth eval injection with no documented fixed version, and stated the flaw is
  not in KEV. Separately, four critical flaws arrived or persisted with nothing to install: fastjson 1.x is
  end-of-life with attacks under way and no 1.x patch, Siemens records the entire Desigo CC V7 family as
  affected with no fix available, IBM offers only interim APARs for two CVSS 9.8 pre-auth WebSphere flaws with
  fix packs not expected before 3Q2026, and CERT@VDE published 20 Phoenix Contact EV-charger CVEs whose
  remediating firmware was unreleased at disclosure. In every case the only available control is network
  position, which is an architecture decision rather than a patch-cycle task.
discovered_at: "2026-08-02T23:52:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, pre-auth, actively-exploited, rce, ot-ics, poc-public]
regions: [global, europe, dach]
sectors: [technology, energy, public-sector, manufacturing, transport]
entities: []
techniques: [T1190, T1068, T1542.001]
affected_products: ["Langflow", "Alibaba fastjson", "Siemens Desigo CC", "IBM WebSphere Application Server", "Phoenix Contact CHARX SEC-3000", "Phoenix Contact CHARX SEC-3050", "Phoenix Contact CHARX SEC-3100", "Phoenix Contact CHARX SEC-3150"]
cves: []
sources:
  - url: "https://www.vulncheck.com/blog/state-of-exploitation-1h-2026"
    publisher: "VulnCheck"
    date: "2026-07-28"
    role: primary
  - url: "https://www.zerodayinitiative.com/advisories/ZDI-26-035/"
    publisher: "Zero Day Initiative (ZDI-26-035)"
    date: "2026-01-09"
    role: primary
  - url: "https://github.com/alibaba/fastjson2/wiki/Security-Advisory:-Remote-Code-Execution-in-fastjson-1.2.68%E2%80%931.2.83"
    publisher: "Alibaba fastjson2 project"
    date: "2026-07-21"
    role: primary
  - url: "https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-16723-critical-fastjson-1-x-zero-day-rce/"
    publisher: "Imperva"
    date: "2026-07-24"
    role: primary
  - url: "https://cert-portal.siemens.com/productcert/csaf/ssa-734552.json"
    publisher: "Siemens ProductCERT (SSA-734552, CSAF)"
    date: "2026-07-14"
    role: primary
  - url: "https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-01"
    publisher: "CISA (ICSA-26-209-01)"
    date: "2026-07-28"
    role: primary
  - url: "https://www.ibm.com/support/pages/node/7281631"
    publisher: "IBM PSIRT"
    date: "2026-07-28"
    role: primary
  - url: "https://www.ibm.com/support/pages/node/7281649"
    publisher: "IBM PSIRT"
    date: "2026-07-28"
    role: primary
  - url: "https://certvde.com/en/advisories/VDE-2026-008/"
    publisher: "CERT@VDE"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "With LangFlow, we've seen attackers gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027, harvest credentials, likely for services such as OpenAI and Claude, deploy cryptominers, and attempt lateral movement. Neither of these vulnerabilities have been added to CISA KEV."
    publisher: "VulnCheck"
  - quote: "FastJson 1.x is no longer actively maintained, and no patched 1.x version has been released for this vulnerability."
    publisher: "Imperva"
  - quote: "The updated firmware will be made available as soon as possible, but no later than August 12, 2026."
    publisher: "CERT@VDE"
verification: multi-source
sourcing_note: >
  Each strand is cited to the party that states it: VulnCheck for the observed Langflow exploitation and the
  KEV absence, ZDI for the flaw mechanics and the absence of a fixed version, the Alibaba fastjson2 project
  for the stock-default exploitability and Imperva separately for the in-the-wild targeting and the
  end-of-life status, Siemens' own CSAF for the Desigo CC per-family remediation categories with CISA's
  ICSA-26-209-01 as the in-window republication that surfaced them, IBM for the interim-APAR-only position and the 3Q2026 fix-pack
  target, split across the two same-day bulletins it published — the first carries the missing-authentication
  flaw and APAR DT496500, the second the deserialization flaw and APAR PH72166, and neither carries both, CERT@VDE for the Phoenix Contact firmware
  commitment date. The no-fix condition is stated per product rather than generalised: it applies to the
  Desigo CC V7 family specifically, since V9 and V8 do have fixes, and to the permanent WebSphere fix packs,
  since interim APARs do exist. Per-CVE metadata is deliberately not duplicated into this entry's cves[] —
  the identifiers, scores and version boundaries live on the operational entries that own that surface for
  the dedup index, the per-CVE pages and automated triage matching.
confidence: high
update_of: null
references:
  - 2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev
  - 2026-07-27/cve-2026-16723-fastjson-1x-spring-boot-fat-jar-rce-no-patch
  - 2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed
  - 2026-08-01/ibm-websphere-cve-2026-14512-14446-preauth-no-fix-pack
  - 2026-08-02/phoenix-contact-charx-sec-3xxx-unauth-root-no-firmware-yet
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Most vulnerability processes reduce to two questions: is anyone exploiting it, and is there something to install. The KEV catalog answers the first for a great many flaws, and a vendor advisory answers the second. This week produced counterexamples to both, in the same seven days.

On the exploitation axis, VulnCheck reported that it has watched attackers use Langflow's pre-authentication eval injection and stated the gap directly: "with LangFlow, we've seen attackers gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027, harvest credentials, likely for services such as OpenAI and Claude, deploy cryptominers, and attempt lateral movement. Neither of these vulnerabilities have been added to CISA KEV." ([VulnCheck, 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)). The underlying advisory compounds it: Zero Day Initiative published CVE-2026-0769 as a 0-day, records that "this vulnerability allows remote attackers to execute arbitrary code on affected installations of Langflow. Authentication is not required to exploit this vulnerability." ([Zero Day Initiative, 2026-01-09](https://www.zerodayinitiative.com/advisories/ZDI-26-035/)), and offers restricting interaction with the product as its only mitigation. A KEV-driven patch queue surfaces neither the flaw nor the fact that there is nothing to queue.

On the remediation axis, four items arrived with no fix to apply. The fastjson flaw "is exploitable under fastjson's stock default configuration — no AutoType enablement required, no classpath gadget required" ([Alibaba fastjson2 project, 2026-07-21](https://github.com/alibaba/fastjson2/wiki/Security-Advisory:-Remote-Code-Execution-in-fastjson-1.2.68%E2%80%931.2.83)), attacks are already under way against organisations across financial services, healthcare and retail ([Imperva, 2026-07-24](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-16723-critical-fastjson-1-x-zero-day-rce/)), and the line is finished: "FastJson 1.x is no longer actively maintained, and no patched 1.x version has been released for this vulnerability." ([Imperva, 2026-07-24](https://www.imperva.com/blog/imperva-customers-protected-against-cve-2026-16723-critical-fastjson-1-x-zero-day-rce/)). Siemens' own machine-readable advisory splits Desigo CC three ways — V9 fixed in 9.0.1, V8 fixed by applying patch V8.0 QU2.0021, and the entire V7 family carrying remediation category `none_available` with network segmentation as the only offered control ([Siemens ProductCERT, 2026-07-14](https://cert-portal.siemens.com/productcert/csaf/ssa-734552.json)) — which for a building-management platform means the unpatchable population is a set of buildings, not a set of servers. That advisory predates this week; what puts it in the window is CISA's republication of it as ICSA-26-209-01 on 2026-07-28 ([CISA, 2026-07-28](https://www.cisa.gov/news-events/ics-advisories/icsa-26-209-01)). IBM disclosed a missing-authentication flaw in the WebSphere Application Server traditional administrative console at CVSS 9.8, states no workaround exists, and names APAR DT496500 with the permanent Fix Packs 9.0.5.29 / 8.5.5.31 targeted for 3Q2026 ([IBM PSIRT, 2026-07-28](https://www.ibm.com/support/pages/node/7281631)); a companion bulletin the same day covers the unsafe-deserialization flaw and its interim fix under APAR PH72166 ([IBM PSIRT, 2026-07-28](https://www.ibm.com/support/pages/node/7281649)). And CERT@VDE published 20 CVEs in Phoenix Contact CHARX SEC-3xxx EV charging controllers — five of them CVSS 9.8 with an unauthenticated network vector, including command injection that executes as root — with the fix still in the future at publication: "the updated firmware will be made available as soon as possible, but no later than August 12, 2026." ([CERT@VDE, 2026-07-30](https://certvde.com/en/advisories/VDE-2026-008/)).

The operational consequence is that for five of this week's most severe items, the work is not a patch ticket. It is answering an architecture question — what can reach this, and can that be reduced — on a building-management platform, a Java dependency buried inside vendor-supplied fat-JARs, an application server, an EV-charging controller fleet, and a self-hosted AI-agent platform. Those are different teams and different change processes from the one that applies monthly updates, and none of them is triggered by a KEV addition or a patch-available flag.

**Defender takeaway:** a vulnerability programme keyed on KEV plus patch availability had two categories of blind spot this week, and both need a deliberate second pass. For the exploitation axis, KEV absence is not evidence of safety — VulnCheck's canary telemetry contradicted it for a flaw with no fix at all, so exploitation intelligence needs a second source. For the remediation axis, the estate needs a standing answer to "which of our critical findings currently have no fix", because those items never leave the queue by being patched; they leave it by being made unreachable, or they stay. The Phoenix Contact case is the one with a date attached, and 12 August is the day to check whether the promised firmware actually shipped.
