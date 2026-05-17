**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-17T04:46:37Z · ended_at=2026-05-17T04:50:42Z · duration_seconds=245

## Verification report — briefs/2026-05-17.md (iteration 2)

**Prior-iteration delta walk:** Performed per v2.53 alt-verifier protocol. All five prior-iteration findings (F1–F5 from iter 1) plus F6–F8 editorial remediations were verified against freshly fetched sources in this iteration. Two prior remediations are confirmed correct; one remediation introduced a new truth defect (see F1 below); one is partially correct; one has a separate CVSS discrepancy surfaced as F2 below.

---

### Prior-iteration delta status

**F1 (iter 1) — CWE-345 removal from SzafirHost:** CONFIRMED CORRECT. The brief contains no CWE number for SzafirHost. CERT-PL page fetched this iteration confirms the actual CWE is CWE-434 (not CWE-345), so removing the incorrect CWE reference was the right remediation. The CERT-PL page also confirms verbatim evidence matches what the brief quotes.

**F2 (iter 1) — Day 1/2 attribution inversions (Viettel-Cursor, STARLabs-LMStudio, k3vg3n-LiteLLM-Day2):** REMEDIATION PARTIALLY CORRECT BUT INTRODUCED NEW ERROR. Full ZDI Day 1 entry list fetched and verified. See finding F1 below for the regression.

**F3 (iter 1) — NVIDIA Container Toolkit Day 2:** CONFIRMED CORRECT. ZDI Day 2 confirms 0xDACA/Noam Trobinski → NV Container Toolkit → use-after-free → $25K on Day 2. Brief now states this correctly.

**F4 (iter 1) — Satoki Tsuji / Ikotas Labs:** REMEDIATION INCORRECT — NEW DEFECT INTRODUCED. See finding F1 below.

**F5 (iter 1) — cohesion:** PARTIALLY CONFIRMED. Day 2 and Day 3 now internally consistent. Day 1 has a residual error (F1).

**F6 (iter 1) — "43 CVEs" attribution:** CONFIRMED CORRECT. Brief now reads: "SecurityWeek tallies '51 high and medium-severity vulnerabilities impacting BIG-IP, BIG-IQ, and NGINX'; NCSC-NL's CSAF restatement (NCSC-2026-0162) lists 43 CVEs in the BIG-IP / BIG-IQ scope (NGINX bugs counted separately)." Both counts properly attributed.

**F7 (iter 1) — F5 footer source order:** CONFIRMED CORRECT. Footer now reads "Source: [F5 K000160932] · Additional source: [SecurityWeek] · Additional source: [NCSC-NL]."

**F8 (iter 1) — AI Agents category list expansion:** CONFIRMED CORRECT. TL;DR bullet and § 5 AI Agents paragraph now enumerate: Codex (Compass Security CWE-150, $40K), Cursor (Compass Security, $15K), LM Studio (OtterSec), LiteLLM (k3vg3n), Claude Code/Chroma/Megatron Bridge/Ollama collisions. NVIDIA Container Toolkit removed from the agent-target list.

---

### Hallucinated / incorrect facts (residual from remediation)

**F1 — Satoki Tsuji Day 1 attribution remains wrong after remediation**

- **Section:** § 5 Deep Dive — Day 1 paragraph
- **Brief text (verbatim):** *"Satoki Tsuji's Codex attempt collided with a vulnerability ZDI already had on file ($8,000 reduced reward)"*
- **ZDI Day 1 source (fetched this iteration):** The complete Day 1 entry list shows:
  - Satoki Tsuji (Ikotas Labs): **NVIDIA Megatron Bridge** → SUCCESS → $20,000 (Overly Permissive Allowed List bug) — NOT a Codex attempt, NOT a collision
  - Ikotas Labs: **LiteLLM** → COLLISION → $8,000 (previously known bugs)
  - maitai (Doyensec): **OpenAI Codex** → COLLISION → $10,000
- The brief's current text conflates three separate Day 1 entries into one incorrect statement. Satoki Tsuji did not attempt Codex; he hit Megatron Bridge successfully. The $8,000 collision was Ikotas Labs against LiteLLM. The Codex collision was maitai/Doyensec for $10,000.
- The prior-iteration F4 remediation replaced one wrong attribution ("Ikotas Labs external-control abuse") with a different wrong attribution ("Satoki Tsuji's Codex collision, $8K").
- **Correct text:** "Satoki Tsuji (Ikotas Labs) exploited NVIDIA Megatron Bridge via an overly permissive allowed-list bug for $20,000; Ikotas Labs separately collided against LiteLLM ($8,000 reduced reward); maitai (Doyensec) collided against OpenAI Codex ($10,000)."
- **Source:** ZDI Day 1 complete entry list (`https://www.thezdi.com/blog/2026/5/13/pwn2own-berlin-2026-day-one-results`), fetched this iteration.

---

### Citation does not support the claim

**F2 — CVE-2026-41225 CVSS score stated as 9.1 but SecurityWeek primary source says 8.6**

- **Section:** TL;DR, § 2 heading, § 2 body, CVE table, § 6 Action Items
- **Brief text (verbatim):** TL;DR: *"CVE-2026-41225 (CVSS 9.1, post-auth Manager-role RCE)"*; § 2 heading: *"CVE-2026-41225 — F5 BIG-IP / BIG-IQ: iControl REST Manager-role authenticated RCE (CVSS 9.1)"*; body: *"CVSS 3.1: 9.1"*; CVE table: *"9.1"*
- **SecurityWeek source (fetched this iteration, `https://www.securityweek.com/f5-patches-over-50-vulnerabilities/`):** *"CVE-2026-41225 (CVSS 8.6) permits authenticated managers to create configuration objects via iControl REST, potentially enabling privilege escalation."* SecurityWeek explicitly assigns CVSS **8.6** to CVE-2026-41225.
- The F5 K000160932 portal page is inaccessible to WebFetch (returns a CSS-error/loading page — JavaScript rendering required). The NCSC-NL advisory redirected without content. The brief attributes CVSS 9.1 without a source that verifiably states it; SecurityWeek (the brief's second cited source) explicitly contradicts it with 8.6. The brief's CWE-250 attribution for CVE-2026-41225 is also unverifiable from accessible sources; SecurityWeek does not cite a CWE.
- **Action required:** Verify the CVSS against the F5 K000160932 portal using the bridge fetcher or NCSC-NL CSAF; if 8.6 is correct per F5's own advisory, correct throughout (TL;DR, heading, body, table, action items); if F5's advisory actually states 9.1, add a note that SecurityWeek differs.

---

### Claim does not support technique description

**F3 — OtterSec LM Studio: "SSRF-plus-code-injection" overstates the ZDI-cited technique**

- **Section:** § 5 Deep Dive — Day 2 paragraph; § 6 Action Items
- **Brief text (verbatim):** *"OtterSec popped LM Studio with an SSRF-plus-code-injection chain"*
- **ZDI Day 2 (fetched this iteration):** OtterSec's LM Studio entry lists only **"Code Injection bug"** — no SSRF component is mentioned. SSRF-plus-code-injection is the ZDI Day 1 STARLabs SG description for their LM Studio chain ("chained 5 bugs incl. SSRF and Code Injection"). The brief appears to have transferred STARLabs SG's Day 1 technique descriptor to OtterSec's Day 2 entry.
- **Correct text:** "OtterSec popped LM Studio via a code-injection bug on Day 2 ($20,000)"
- **Source:** ZDI Day 2 (`https://www.zerodayinitiative.com/blog/2026/5/15/pwn2own-berlin-2026-day-two-results`), fetched this iteration.

---

### Unsupported facts (minor)

**F4 — Viettel "targeted Codex" — correct but incomplete framing**

- **Section:** § 5 Deep Dive — Day 1 paragraph
- **Brief text (verbatim):** *"Viettel also targeted Codex on Day 1"*
- **ZDI Day 1 (fetched this iteration):** Le Duc Anh Vu (Viettel) attempted Codex on Day 1 — FAILURE (no prize). Separately, Nguyen Thanh Dat (Viettel) hit Claude Code on Day 1 — COLLISION ($20,000). The brief's statement "Viettel targeted Codex" is technically accurate (Le Duc Anh Vu did attempt Codex and failed), but omits the more notable Viettel result — the Claude Code collision ($20K). Since the TL;DR and AI Agents paragraph list "Claude Code" as a collision target without naming the researcher, readers may not connect Viettel to the Claude Code collision.
- **Severity:** Advisory — the Codex failure statement is not wrong, but the Claude Code collision attribution to Viettel ($20K) is missing from the Day 1 paragraph and would complete the picture.
- **Classification:** F11 advisory (the claim is accurate but incomplete; the more significant Viettel result is omitted from the day-by-day account).

---

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)

**Summary:**
- F1 (truth/hallucinated-fact): Satoki Tsuji attribution wrong — targeted Megatron Bridge successfully ($20K), not a Codex collision ($8K). The LiteLLM collision was Ikotas Labs; the Codex collision was maitai/Doyensec.
- F2 (truth/claim-not-supported): CVSS 9.1 stated for CVE-2026-41225 but SecurityWeek (cited source) says 8.6. F5 portal inaccessible; no other accessible source confirms 9.1.
- F3 (truth/claim-not-supported): "SSRF-plus-code-injection" technique descriptor for OtterSec LM Studio is from ZDI Day 1 STARLabs entry, not ZDI Day 2 OtterSec entry (which says only "Code Injection bug").
- F4 (advisory/editorial): Viettel Claude Code collision ($20K, Day 1) omitted from Day 1 paragraph; only their failed Codex attempt mentioned.

**Confirmed clean (no further issues):** § 1 SzafirHost (CWE removed, CERT-PL quote accurate), § 1 FunnelKit (Sansec primary confirmed, BleepingComputer corroborating), § 2 DHTMLX (CERT-PL quote accurate), § 3 Kimsuky (Securelist confirmed, [SINGLE-SOURCE] flag present), § 4 UPDATE Exchange (ZDI Day 2 confirmed Orange Tsai chain), § 5 Day 3 ESXi (STARLabs SG Nguyen Hoang Thach, $200K memory-corruption confirmed), § 5 NVIDIA Container Toolkit (0xDACA/Noam Trobinski, $25K, Day 2, UAF confirmed), § 5 Day 2 Compass Security/Cursor ($15K confirmed), § 6 Action Items source-linking consistent with brief content, § 7 Verification Notes accurate. F5 BIG-IP CVE count attribution (43 NCSC-NL / 51 SecurityWeek) correctly framed. F5 footer source order correct.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F1
  category: hallucinated-fact
  section: deep-dive
  item: "§ 5 Day 1 — Satoki Tsuji Codex collision"
  url_or_quote: "Satoki Tsuji's Codex attempt collided with a vulnerability ZDI already had on file ($8,000 reduced reward)"
  summary: "ZDI Day 1 entry list shows Satoki Tsuji (Ikotas Labs) hit NVIDIA Megatron Bridge successfully for $20K. The $8K collision was Ikotas Labs against LiteLLM. The Codex collision was maitai/Doyensec for $10K. Prior-iteration F4 remediation introduced this new error."

- code: F2
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-41225 — F5 BIG-IP CVSS score"
  url_or_quote: "CVSS 9.1"
  summary: "SecurityWeek (cited source, fetched this iteration) explicitly states CVSS 8.6 for CVE-2026-41225. F5 K000160932 portal inaccessible to WebFetch. No accessible source confirms 9.1. Appears everywhere: TL;DR, heading, body, CVE table, action items."

- code: F3
  category: claim-not-supported
  section: deep-dive
  item: "§ 5 Day 2 — OtterSec LM Studio technique"
  url_or_quote: "OtterSec popped LM Studio with an SSRF-plus-code-injection chain"
  summary: "ZDI Day 2 lists OtterSec LM Studio as 'Code Injection bug' only — no SSRF. The SSRF+code-injection descriptor belongs to ZDI Day 1 STARLabs SG LM Studio entry (5-bug chain). Technique over-claimed."

- code: F4
  category: editorial-advisory
  section: deep-dive
  item: "§ 5 Day 1 — Viettel Claude Code collision omitted"
  url_or_quote: "Viettel also targeted Codex on Day 1"
  summary: "ZDI Day 1 shows Nguyen Thanh Dat (Viettel) hit Claude Code on Day 1 for a $20K collision — omitted from the Day 1 paragraph. Le Duc Anh Vu (Viettel) also attempted Codex (failure). Only the Codex failure is mentioned; the Claude Code collision is missing from the day-by-day account."
```
