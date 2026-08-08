---
schema: 1
kind: annual-report
horizon: operational
title: "Wiz Cloud Threat Highlights H1 2026: LiteLLM had four separate security events in six months, unauthenticated MCP endpoints turned up across hundreds of environments, and a new extortion actor goes after service accounts rather than people"
headline: "The AI toolchain became a cloud attack surface with its own recurring vulnerability cadence, and the credentials it holds are non-human"
summary: >
  Wiz Research's semi-annual cloud threat report, covering January to June 2026, names the specific AI
  infrastructure attackers went after. LiteLLM — an AI gateway Wiz says is present in over a third of the
  cloud environments it monitors — had four separate security events in six months, including an SQL
  injection exploited in the wild; Dify, Langflow, n8n and Ollama each had critical unauthenticated flaws.
  Wiz found unauthenticated Model Context Protocol endpoints across hundreds of environments, each holding
  backend credentials. It also profiles JINX-0163, a cloud extortion group that targets service accounts and
  IAM roles rather than end users, pivoting from a single over-privileged identity or exposed state file.
discovered_at: "2026-08-08T05:22:00Z"
event_date: "2026-08-06"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [cloud, ai-abuse, supply-chain, identity, organized-crime]
regions: [global]
sectors: [technology, public-sector, finance, telco]
entities: [report:wiz-cloud-threat-highlights-h1-2026, actor:jinx-0163, actor:teampcp]
techniques: [T1195.001, T1078.004, T1552, T1190]
affected_products: ["LiteLLM", "Dify", "Langflow", "n8n", "Ollama"]
cves: []
sources:
  - url: "https://www.wiz.io/blog/cloud-threat-highlights-h1-2026"
    publisher: "Wiz Research"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "We found unauthenticated MCP endpoints across hundreds of environments, each one a pre-authenticated proxy holding backend credentials and bridging multiple services."
    publisher: "Wiz Research"
  - quote: "They went from making up about 10% of significant incidents in H2 2025 to 25% in H1 2026."
    publisher: "Wiz Research"
verification: single-source
sourcing_note: "A vendor's own semi-annual telemetry report; the population is Wiz's monitored cloud estate, not the internet, and the incident counts are its own customer-facing designations. Carried for the named exposure classes and the actor profile rather than the aggregate figures."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Inventory Model Context Protocol endpoints in your cloud estate and confirm each one requires authentication — Wiz found unauthenticated MCP endpoints across hundreds of environments, and each is a pre-authenticated proxy already holding the backend credentials it bridges."
migrated_from: null
---

Wiz Research's semi-annual cloud threat report covers January to June 2026, and its value for this constituency is the named inventory rather than the trend lines: it says concretely which AI infrastructure attracted attacker and researcher attention, and what the resulting exposure looks like in a cloud estate.

The AI toolchain now has its own vulnerability cadence. LiteLLM — an AI gateway Wiz says is present in over a third of the cloud environments it monitors — "had four separate security events in six months: a supply-chain compromise, an SQL injection vulnerability exploited in the wild, a privilege escalation chain and an authentication bypass", while Dify, Langflow, n8n and Ollama "each had critical unauthenticated vulnerabilities of their own" ([Wiz Research, 2026-08-06](https://www.wiz.io/blog/cloud-threat-highlights-h1-2026)). That list is worth reading as an asset-inventory prompt: these are components teams stand up quickly, often outside the change process that governs the rest of the estate, and three of the five have already reached this pipeline's coverage through separate exploited-vulnerability events.

The exposure finding is sharper than the vulnerability one. On Model Context Protocol servers, Wiz reports: "We found unauthenticated MCP endpoints across hundreds of environments, each one a pre-authenticated proxy holding backend credentials and bridging multiple services" ([Wiz Research, 2026-08-06](https://www.wiz.io/blog/cloud-threat-highlights-h1-2026)). The reason that shape matters is that an MCP server is not a data store to be broken into — it is a component that already holds the credentials for everything behind it and exists to act on their behalf, so reaching it unauthenticated is not a step toward access, it is the access.

On the actor side, Wiz profiles JINX-0163, a cloud-native extortion group it began tracking in 2026 and that "consistently targets non-human identities - service accounts and IAM roles - rather than end users", in some cases leveraging a single over-privileged identity or an exposed state file to pivot to a full inventory ([Wiz Research, 2026-08-06](https://www.wiz.io/blog/cloud-threat-highlights-h1-2026)). An extortion group that skips human identity entirely bypasses most of the control stack organisations have spent two years building — phishing-resistant MFA, conditional access, helpdesk verification — none of which applies to a service account.

On supply chain, Wiz records that notable supply-chain attacks "went from making up about 10% of significant incidents in H2 2025 to 25% in H1 2026", with TeamPCP, North Korea and at least three independent operations running campaigns concurrently across npm, PyPI, Composer, VSCode extensions, Jenkins plugins and AUR, several of which had not been targeted this way before ([Wiz Research, 2026-08-06](https://www.wiz.io/blog/cloud-threat-highlights-h1-2026)). It also notes that malicious packages' shrinking availability window is what makes an install cooldown policy effective — declining to download packages published less than 24 hours ago — which is a specific, cheap control rather than a general recommendation.

**Defender takeaway:** three things here are directly checkable against your own estate this week — whether LiteLLM, Dify, Langflow, n8n or Ollama are deployed and at what versions; whether any MCP endpoint answers without authentication; and whether your service accounts and IAM roles are scoped such that one over-privileged identity or a readable state file yields the inventory. The aggregate incident percentages are a vendor's view of its own customer base and should not be read as a measurement of the wider landscape.
