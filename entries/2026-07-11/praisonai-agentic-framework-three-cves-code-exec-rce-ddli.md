---
schema: 1
kind: vulnerability
horizon: operational
title: "PraisonAI agent framework: three CVEs — unsandboxed LLM code execution, tool-call RCE, and vector-store DDL injection"
headline: "PraisonAI: three critical CVEs — unsandboxed LLM code execution leaks all env secrets, plus tool-call RCE and DDL injection"
summary: >
  Three CVEs disclosed in PraisonAI, an open-source multi-agent LLM orchestration
  framework (pip packages praisonaiagents / praisonai): CVE-2026-61447 (CVSS 10.0)
  runs LLM-generated Python in a subprocess with the full parent environment and a
  dead sandbox flag, and CVE-2026-61445 (9.4) lets AICoder tool calls write
  arbitrary files and run shell commands — both reachable by influencing the
  model's output through prompt injection. CVE-2026-60090 (9.3) is a separate
  SQL/CQL injection: a caller-controlled vector-store dimension parameter is
  interpolated into knowledge-store DDL, with no LLM nexus. The advisories ship
  proof-of-concept code, and all three are fixed in praisonaiagents ≥ 1.6.78 /
  praisonai ≥ 4.6.78.
discovered_at: "2026-07-11T20:25:13Z"
event_date: "2026-07-11"
run_id: 2026-07-11T2009Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, ai-abuse, poc-public, patch-available, pre-auth]
regions: [global]
sectors: [technology, public-sector]
entities: []
techniques: [T1190, T1059.006, T1059.004, T1552]
affected_products: ["PraisonAI"]
cves:
  - id: CVE-2026-61447
    cvss: "10.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "praisonaiagents ≤ 1.6.77"
    fixed: "praisonaiagents 1.6.78"
  - id: CVE-2026-61445
    cvss: "9.4"
    epss: null
    type: rce
    vector: zero-click
    auth: post-auth
    status: [poc-public, patch-available]
    affected: "praisonai ≤ 4.6.77"
    fixed: "praisonai 4.6.78"
  - id: CVE-2026-60090
    cvss: "9.3"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [poc-public, patch-available]
    affected: "praisonai 3.10.0 – 4.6.64"
    fixed: "praisonai 4.6.78"
sources:
  - url: "https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-2xv2-w8cq-5gxw"
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
    date: "2026-06-25"
    role: primary
  - url: "https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-9mp3-24cc-77mg"
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
    date: "2026-06-25"
    role: primary
  - url: "https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-wf65-4jjx-q444"
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
    date: "2026-06-25"
    role: primary
  - url: "https://www.thehackerwire.com/praisonai-rce-cve-2026-61447/"
    publisher: "TheHackerWire"
    date: "2026-07-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CodeAgent._execute_python() executes LLM-generated Python code in a subprocess with the complete parent-process environment (os.environ.copy()), zero AST validation, zero import restrictions, and no sandbox enforcement — even when CodeConfig(sandbox=True) is explicitly set."
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
  - quote: "sandbox=True is dead code"
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
  - quote: "**Root access**: All Docker containers run as root (no USER directive)"
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
  - quote: "A caller that can influence collection creation dimensions can append SQL/CQL tokens to the generated DDL executed by the database driver."
    publisher: "PraisonAI / MervinPraison (GitHub Security Advisory)"
verification: multi-source
sourcing_note: "CVE ids and CVSS come from the three per-CVE GitHub Security Advisories (vendor primary; MervinPraison is the PraisonAI maintainer) and are corroborated by ENISA EUVD (EUVD-2026-43182 / -43181 / -43175) and TheHackerWire. Recency anchor: all three CVE ids were published to NVD on 2026-07-11T14:16Z (confirmed via the NVD API, CVSS 4.0 base scores 10.0 / 9.4 / 9.3 CRITICAL) — the in-window event; the three GitHub advisories themselves have been public since 2026-06-25 (dated accordingly in sources[]), so this entry is anchored on the CVE-id publication rather than the advisory drafting. Severity note: for CVE-2026-60090 the GitHub advisory GHSA-wf65 self-labels the severity 'Moderate' with no CVSS, but NVD/VulnCheck assign CVSS 4.0 = 9.3 (CRITICAL); the entry uses the authoritative NVD score and records the vendor's lower self-rating here. The advisories publish proof-of-concept code; no independent weaponised exploit or in-the-wild exploitation of these three CVEs has been reported."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade PraisonAI to praisonaiagents ≥ 1.6.78 and praisonai ≥ 4.6.78 on any self-hosted deployment — all three CVEs are fixed in that release line."
migrated_from: null
---

Three CVEs were published together on 2026-07-11 (NVD/EUVD) in PraisonAI — an open-source multi-agent LLM orchestration framework distributed as the `praisonaiagents` and `praisonai` pip packages. The first two share one root cause: the framework treats model output as trusted, so an attacker who can influence the LLM (via prompt injection in agent input, ingested documents, or tool results) reaches code execution without touching a classic network listener. **CVE-2026-61447 (CVSS 10.0)** is in `CodeAgent._execute_python()` (`src/praisonai-agents/praisonaiagents/agent/code_agent.py`, lines 253–308): LLM-generated Python is written to a temp file and run via `subprocess.run(["python", temp_file], env=os.environ.copy())` with no AST validation and no import restrictions, and `CodeConfig` declares `sandbox: bool = True` (line 21) that the execution path never reads — so the flag is inert and the subprocess inherits every credential in the parent environment (`OPENAI_API_KEY`, `DATABASE_URL`, cloud tokens) ([PraisonAI GHSA-2xv2-w8cq-5gxw, 2026-06-25](https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-2xv2-w8cq-5gxw)). The advisory contrasts this with the framework's own sandboxed `execute_code` tool, which runs with an empty environment.

**CVE-2026-61445 (CVSS 9.4)** is in the AICoder chat-UI component, which exposes `write_to_file` and `execute_command` tools to the model with no path validation or command sanitization; `apply_llm_response` joins the caller path with `os.path.join(self.cwd, args["path"])`, which does not block absolute paths, so a model-driven write can land at `/etc/crontab` or `/root/.ssh/authorized_keys`, and the advisory notes containers commonly run as root, turning tool-call abuse into full in-container compromise ([PraisonAI GHSA-9mp3-24cc-77mg, 2026-06-25](https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-9mp3-24cc-77mg)). **CVE-2026-60090 (CVSS 9.3)** is a different bug class with no LLM nexus — a classic SQL/CQL injection reachable by any caller who can influence collection-creation parameters (for example through a RAG ingestion API), not through the model: the PGVector and Cassandra knowledge-store backends validate schema/keyspace/collection identifiers but interpolate the caller-supplied `dimension` value straight into the `CREATE TABLE`/CQL vector-column DDL, and the `int` type hint is not enforced at runtime, so a value like `3); DROP TABLE tenant_secrets; --` reaches the database driver ([PraisonAI GHSA-wf65-4jjx-q444, 2026-06-25](https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-wf65-4jjx-q444)). The three CVEs — VulnCheck-assigned and carried on ENISA EUVD and NVD with CVSS 4.0 vectors consistent with the assigned scores — were also independently re-reported the same day ([TheHackerWire, 2026-07-11](https://www.thehackerwire.com/praisonai-rce-cve-2026-61447/)).

The exposure is narrow — self-hosted agent deployments, most likely in AI-pilot and innovation teams rather than production estate — but the transferable lesson is in the first two bugs: in an agentic framework the model's output is an execution surface, so the same detection thinking applies to any self-hosted LLM/agent tooling (CVE-2026-60090 is a conventional injection that the usual input-validation hygiene covers). Detection concepts, telemetry-class first: in process-creation telemetry with parent lineage (Sysmon EID 1, auditd `execve`, EDR process events), surface script interpreters (`python`, `sh`) whose parent is the agent-hosting Python process — and, more discriminating, where that child then reads credential-shaped environment variables or opens outbound connections; in the framework's own tool-call audit log, flag `write_to_file` / `execute_command` invocations whose arguments point outside the declared workspace (`/etc/`, `~/.ssh/`, cron paths); and in database audit logs, flag knowledge-store DDL carrying non-integer tokens (semicolons, comment sequences) in the vector-dimension position. **Defender takeaway:** patch to the fixed release line, and where a vulnerable `CodeAgent` ran with real secrets in its environment, treat those credentials as exposed and rotate them — the `os.environ.copy()` path handed the full environment to any code the model could be induced to emit. **Triage:** a `CodeAgent` legitimately spawns `python` subprocesses to do real data work, so parent-child lineage alone is not the signal — the discriminator the advisory's own mechanics dictate is the child's *behaviour*: imports or egress not required by the declared task (a `socket`/`urllib` call, a shell spawn) or a read of credential env vars; for AICoder, legitimate writes stay inside the project workspace, so a write to `/etc` or an SSH path is the separating signal. Do not rely on `CodeConfig(sandbox=True)` even after patching — verify the fixed version actually enforces isolation, and independently constrain agent code execution with OS-level sandboxing and a scoped (not inherited) environment.
