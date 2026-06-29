**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-29T04:36:06Z · ended_at=2026-06-29T04:38:46Z · duration_seconds=160
**Self-telemetry:** urls_checked=14 · webfetch_calls=7 · bridge_fetches=2

## Verification report — briefs/2026-06-29.md (iteration 1)

Cold read of a quiet-window 3-item daily brief (§1 KDDI ISP breach, §3 0DIN AI-coding-agent prompt-injection research, §4 Gogs CVE-2026-52806 exploitation UPDATE; §2/§5 intentionally empty). Mechanical gate passed pre-spawn (47 pass · 3 warn · 0 fail).

### Truth pass — what I fetched this iteration

- **threats.wiz.io cryptojacking-campaign-targeting-k8s-clusters** (WebFetch) — supports every §4 claim: Gogs+Argo chain, thousands of Linux hosts, 300+ K8s nodes, stolen service-account tokens, privileged-container escape to deploy miners, actor "Unknown", "Realm C2", dates 2026-06-13–23. Page published 2026-06-25, last edit 2026-06-28; brief's "2026-06-28" citation matches the edit date — acceptable for an UPDATE.
- **0din.ai/blog/clone-this-repo-and-i-own-your-machine** (WebFetch ×3) — supports §3 chain (three components, error→DNS→shell indirection, the verbatim "Claude Code never decided to open a shell…" quote, names Claude Code). **Byline date is "6 min read June 25, 2026 By Andre Hall & Miller Engelbrecht"; no other date appears anywhere in the article body** — see F4 below.
- **bleepingcomputer …data-breach-…six-isps** (bridge) — `datePublished 2026-06-28T10:13:46-04:00`, author Bill Toulas. Supports KDDI claims; meta "five other ISPs" + KDDI = six.
- **securityaffairs …kddi-…six-isps** (WebFetch) — supports all KDDI claims; names six ISPs STNet, KDDI Web Communications, JCOM, Chubu Telecommunications, Nifty, BIGLOBE. Brief's "…and a further KDDI ISP" = KDDI Web Communications; accurate.
- **infosecurity-magazine …kddi-breach-japanese-telcos** (WebFetch) — specific article (not index); corroborates six ISPs / 14.22M / third-party software / detection ~June 17.
- **rapid7 …gogs-unfixed** (WebFetch) — supports §4 Gogs mechanics (`--exec` into `git rebase` via PR branch name; effectively unauthenticated on default open-registration); references CVE-2026-52806 extensively; fix 0.14.3 (2026-06-07).
- **bleepingcomputer …clean-github-repo…** (bridge) — `datePublished 2026-06-27T10:22:36-04:00` = **14:22:36 UTC**, exactly matching the brief's §7 recency annotation "2026-06-27 14:22 UTC". Confirms the three-component chain, attributes to Mozilla 0DIN, carries the quoted text.
- **8 ATT&CK technique URLs** (T1566, T1071.004, T1059.004, T1190, T1078.004, T1610, T1611, T1496) — all curl 200.

### Unsupported / hallucinated facts

- **F4 — 0DIN research date stated as 2026-06-15; the cited 0DIN page says June 25, 2026 and contains no June-15 date anywhere.** The claim appears three times:
  - TL;DR (line 11): "([Mozilla 0DIN, 2026-06-15](https://0din.ai/blog/clone-this-repo-and-i-own-your-machine)…)"
  - §3 (line 31): "([Mozilla 0DIN, 2026-06-15](https://0din.ai/blog/clone-this-repo-and-i-own-your-machine)…)"
  - §7 (line 67): "the underlying 0DIN research is 2026-06-15."
  I fetched the 0DIN page three times in this iteration. The byline reads verbatim "6 min read June 25, 2026 By Andre Hall & Miller Engelbrecht", and a targeted re-fetch for any other date returned "No other dates appear in the article body. The publication date of June 25, 2026 is the only temporal reference." The cited source does not support 2026-06-15; it supports 2026-06-25. A June-25 0DIN post reported by BleepingComputer on June-27 is also the internally-coherent timeline (2 days), whereas June-15 → June-27 (12 days) is not. **Remediation: change all three 2026-06-15 references to 2026-06-25.** This does not weaken inclusion — a June-25 research date sits even closer to the window and the §7 recency reasoning (BC article 2026-06-27 14:22 UTC as the in-window anchor, ~1.7h before the strict 36h cutoff) is unaffected and independently verified correct.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One truth defect (F4 — a date the cited source contradicts, repeated 3×). Everything else verified clean:

- All cited URLs resolve to specific articles/advisories/research posts (no homepages, no NVD/MITRE per-CVE Source links; the only ATT&CK and per-CVE references are inline technique/UPDATE context, not primary Source footers).
- §1 KDDI: six-ISP list, 14.22M worst-case, third-party-platform vector, detection ~June 17, PIPC notification, no CVE/no actor — all corroborated across three outlets; §7 aggregator-only reduced-confidence caveat is honestly stated.
- §3 0DIN: three-stage chain, indirection levels, Claude Code naming, the Evidence quote — all verbatim-supported; §7 recency annotation (BC 2026-06-27 14:22 UTC) confirmed to the second; ATT&CK mappings resolve.
- §4 Gogs UPDATE: correctly delta-only (exploitation status change), not a recap — CVE mechanics/patch/CVSS 9.4 carried forward from 2026-06-20 coverage (verified against that brief), new Wiz campaign claims (scale/attribution) honestly fenced as single-substantive-source in §7; Rapid7 corroborates only the CVE mechanics, as the brief states. ATT&CK chain resolves.
- Dedup: KDDI was "Rolled forward" in 2026-06-28 §7 — carrying it today on fresh 2026-06-28 disclosure reporting is consistent, not recycled. The Amazon Q CVE-2026-12957 "covered 2026-06-27" comparison in §3 is accurate. StrikeShark/SharkLoader correctly dropped as out-of-window.
- Name-collision WARN (§3 "GitHub"): **benign** — refers to attacker-planted repo on the GitHub platform, not an attacker/defender name inversion. No F15, no disambiguation needed.
- No IOCs (no IPs/hashes/rule code). English throughout. No vanity metrics. No workflow-internal language in published prose.
- §2/§5 empty stubs justified and honest. Coverage shape appropriate for a quiet 36h window.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: tldr-and-research-and-verification-notes
  item: "Mozilla 0DIN AI-coding-agent indirect prompt-injection research"
  url_or_quote: "Mozilla 0DIN, 2026-06-15 (lines 11, 31, 67) — https://0din.ai/blog/clone-this-repo-and-i-own-your-machine"
  summary: "Brief dates the 0DIN research 2026-06-15 in three places; the cited 0DIN page byline reads 'June 25, 2026' (Andre Hall & Miller Engelbrecht) and the body contains no June-15 date. Fetched 3x this iteration. Change all three 2026-06-15 references to 2026-06-25. Coherence check: BleepingComputer reported it 2026-06-27 (2 days after a June-25 post). Inclusion/recency reasoning unaffected."
```
