**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-21T05:19:43Z · ended_at=2026-07-21T05:28:01Z · duration_seconds=498

## Verification report — 2026-07-21T0409Z-intel (iteration 3)

Cold read of 8 new entries + run record. Every inline and sources[] primary URL was fetched this iteration (Group-IB and Sysdig required the jina last-resort after WebFetch 503s / bridge returned only HTML head; ServiceNow/NCSC-CH via the bridge). CVE authorities checked directly (NVD API for CVE-2026-2291; NCSC-CH bridge for CVE-2026-6875). Corroborators fetched: BleepingComputer(ServiceNow), Searchlight(ServiceNow), Risky.biz, KELA, Digi24, SecurityWeek(HF), Infosecurity(JADEPUFFER/Cruciferra/HOLLOWGRAPH). Two corroborators sampled-out under time budget (BleepingComputer-HF, Infosecurity-WP2Shell) — both back primaries already fully confirmed and pass the mechanical URL-pattern gate.

### Re-verification of the four previously-remediated F4 quotes (spawn-message focus)
- **cruciferra** — evidence[0] "the malware reads a clean copy of ntdll.dll on disk and stores all stub pointers in a global structure for later usage." is a contiguous verbatim substring of Proofpoint ("To do so, the malware reads a clean copy of ntdll.dll…"). evidence[1] "Proofpoint observed four campaigns attributed to Chinese-speaking cybercrime actor TA4922 using Cruciferra to ultimately deliver AsyncRAT." is a contiguous substring of Proofpoint ("Between late April and early June 2026, Proofpoint observed four campaigns…"). Both now correctly attributed to Proofpoint. CONFIRMED FIXED.
- **dnsmasq** — evidence[0] "The root cause of the vulnerability is an unsafe strcpy() when a domain name is cached." matches Exodus verbatim, single contiguous sentence, no ellipsis. Body inline quote "the length of the string is not checked to ensure it does not exceed the size of the bigname buffer" is contiguous verbatim. CONFIRMED FIXED.
- **hugging-face** — evidence[0] parenthetical "(a remote-code dataset loader and a template-injection in a dataset configuration)" restored and verbatim; evidence[1] "executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services." contiguous verbatim; evidence[2] verbatim. CONFIRMED FIXED.
- **hollowgraph** — evidence[1] "we cannot confidently attribute this activity to any previously identified threat actor." is a single contiguous Group-IB sentence (no splice); evidence[0] high-confidence-Cavern quote contiguous verbatim. CONFIRMED FIXED.

### Truth pass (per entry) — no defects
- **ServiceNow CVE-2026-6875** — NCSC-CH bridge confirms "Current exploitation status: Actively exploited", CVSS 9.5, KB3137947, hosted+self-hosted. BleepingComputer confirms Defused ITW attribution and July-18 ("Friday") first attempts. Searchlight confirms the eval/new Function sandbox-escape quote and sysparm_assessable_type / GlideRecord path (detection guidance is source-grounded). update_of target file exists; delta-only body.
- **dnsmasq CVE-2026-2291** — Exodus confirms strcpy/really_insert/bigname-1025/OpenWrt RCE chain and 2.92rel2/2.93 (2026-05-11). NVD API confirms CVSS 7.3 HIGH (AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L) and the cache-poisoning/DoS framing the entry contrasts against. verification: single-source correctly set; sourcing_note explains NVD non-citation. (NVD attributes the overflow to extract_name() vs Exodus's really_insert()/strcpy — not a contradiction; entry follows the primary and the impact framing agrees.)
- **JADEPUFFER/ENCFORGE** — Sysdig confirms ENCFORGE=lockd, UPX Go, ~180 extensions, AES-256-CTR + RSA-2048 KEM, and every named ML format (.ckpt/.safetensors/.gguf/.faiss/.parquet/.tfrecord/.npy/LoRA), same-operator (extortion contact match), Langflow CVE-2025-3248, MySQL AES_ENCRYPT prior. T1190/T1611/T1486 all supported. update target exists.
- **Cruciferra** — Proofpoint confirms process ghosting (NtCreateSection/SEC_IMAGE), ZwQueryVirtualMemory/NtManageHotPatch, GoFlyDrv.sys BYOVD, 90+ polymorphic ciphers/.reloc/Base16, EnumWindows, tax-portal lures, four TA4922 AsyncRAT campaigns. Registry relation ta4922 uses cruciferra correct.
- **HOLLOWGRAPH** — Group-IB (jina) confirms high-confidence Cavern link, 2050-05-13 22:00-23:00 UTC calendar dead-drop, RSA-OAEP+AES-256-GCM per-direction keys, IPv6 AAAA DNS-tunneled Entra refresh (tenant/client/secret/mailbox), get/send, 12 systems ~3 communicating, Israeli, 3 Jun-9 Jul 2026, NativeAOT .NET, low-confidence Lyceum/OilRig overlap. All IOCs (cloudlanecdn, logAzure.txt, mailbox) correctly omitted. Registry variant-of Cavern correct.
- **GPT5.6 WP2Shell** — Searchlight confirms both evidence quotes verbatim, CVE-2026-63030 (REST batch route-confusion) + CVE-2026-60137 (WP_Query author__not_in SQLi), 7.0.2/6.9.5/6.8.6 patched 2026-07-17, oEmbed/parse_request/cache-poisoning/admin chain, GPT5.6, ~10h. update target exists; correctly framed as capability-only delta.
- **ANCPI** — Digi24 confirms "bazele de date tehnice și juridice ale instituției nu au fost afectate" + Gov Cloud migration 22 July via STS; Risky.biz confirms the wipe-claim quote verbatim; KELA confirms the Zakaria Mahdjoub / Oran, Algeria attribution verbatim plus forums/sectors/access methods. verification: contradicted, confidence medium, credibility 3 — correctly calibrated for a genuine unresolved contradiction. update target exists.
- **Hugging Face** — first-party disclosure confirms all three evidence quotes verbatim (parenthetical intact), 17,000+ events, node-level/credential/lateral, public assets + supply chain clean, guardrail-lockout → open-weight forensic reconstruction. Sygnia cross-reference entry (2026-07-09) exists on disk, so the "second concrete July-2026 case" framing is an accurate, transparently-marked internal reference, not a fabricated quantifier. Out-of-nexus victim but earns inclusion on transferable-TTP grounds (autonomous-agent intrusion) with an explicit CH/EU research/public-sector takeaway.

### Editorial pass — no defects
- Relevance: all 8 clear the gate. dnsmasq clears the vulnerability gate on triage-recalibration (DoS→pre-auth-RCE on broad embedded/OT install base). HF and Cruciferra clear the out-of-nexus/breach bar on transferable-TTP + in-nexus sector targeting respectively.
- Priority: one `high` (ServiceNow ITW flip) is well-calibrated and defensible as not-`critical` (week-old patch available, exposure bounded to self-hosted/partner-managed). No `notable` clears the critical bar.
- Classification: every entry carries exactly one Admiralty block (no triage scheme / no watchlists configured — correct); no org_triage, no watchlist_hit. Reliabilities track source nature (A: NCSC-CH, HF first-party; B: research labs; ANCPI B/3 for the contradiction). No F17.
- Actions (F18): four entries carry one concrete, entry-specific do-now task each (ServiceNow patch, dnsmasq version-verify, JADEPUFFER off-host model backup, HF pre-provision open-weight forensic model); four correctly empty (Cruciferra, HOLLOWGRAPH, GPT5.6, ANCPI). No generic advice, no body-restatement, no cross-entry duplication.
- Style: zero IOCs across all entries (sources carried IPs/hashes/domains/YARA — all excluded); English; no workflow-internal language; no vanity metrics.
- Coverage: five borderline drops each carry a defensible rationale (out-of-nexus / no new TTP / unconfirmed leak-claim / 9-month-old patch / repeat-theme). No nameable in-window in-nexus item was missed. Coverage looks complete.

### Verdict
CLEAN

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
[]
```
