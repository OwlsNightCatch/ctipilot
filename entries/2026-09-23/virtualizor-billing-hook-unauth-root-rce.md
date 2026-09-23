---
schema: 1
kind: vulnerability
title: "Virtualizor VPS/hypervisor control panel: a login-page guard's own exemption for act=login lets an unauthenticated attacker reach root"
headline: "A single mis-scoped pre-auth check in a hosting control panel opens three unauthenticated paths to root"
summary: >
  Softaculous Virtualizor's admin panel guards every pre-authentication
  request except one: a request with act=login walks straight into an
  unauthenticated billing-module handler. From there, an attacker reaches
  unauthenticated root command execution, PHP object injection, or
  arbitrary tenant-balance manipulation. Fixed in 3.2.9 patch 9 / 3.3.0;
  VulnCheck's disclosure does not state whether it observed in-the-wild
  exploitation, and built a fully automated internal exploit module — using
  its own open-source go-exploit framework, not published for this CVE —
  that requires no credentials or account information from the operator.
discovered_at: "2026-09-23T04:52:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, default-config, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:softaculous-virtualizor"]
techniques: [T1190, T1068]
affected_products: ["Softaculous Virtualizor"]
cves:
  - id: CVE-2026-43641
    cvss: "9.8 (CVSS3.1) / 9.3 (CVSS4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "≤ 3.2.9 patch 8 (in-house billing enabled, an existing suspended account, MySQL default non-strict sql_mode)"
    fixed: "3.2.9 patch 9 (2026-09-01) / 3.3.0"
  - id: CVE-2026-43642
    cvss: "8.1 (CVSS3.1) / 9.2 (CVSS4.0)"
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "≤ 3.2.9 patch 8"
    fixed: "3.2.9 patch 9 (2026-09-01) / 3.3.0"
  - id: CVE-2026-43643
    cvss: "7.5 (CVSS3.1) / 8.7 (CVSS4.0)"
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "≤ 3.2.9 patch 8"
    fixed: "3.2.9 patch 9 (2026-09-01) / 3.3.0"
sources:
  - url: "https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce"
    publisher: "VulnCheck"
    date: "2026-09-22"
    role: primary
closed_sources: []
evidence:
  - quote: "The redirect that guards the admin panel fires for every action except one. That one is `login`."
    publisher: "VulnCheck"
    source_url: "https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce"
  - quote: "Verified on the lab: /tmp/x reads uid=0(root) gid=0(root) groups=0(root)."
    publisher: "VulnCheck"
    source_url: "https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce"
  - quote: "Softaculous patched all three in 3.2.9 patch 9 (2026-09-01), and the fix carries into 3.3.0 (2026-09-09), the current build. Patch 7, the build audited above, and patch 8 are both still vulnerable"
    publisher: "VulnCheck"
    source_url: "https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce"
verification: single-source
sourcing_note: "VulnCheck is both the discovering researcher and the CVE Numbering Authority for these three ids — treated as an authoritative single primary equivalent to a vendor advisory; no independent second technical analysis has been published yet. CVSS scores were not stated in VulnCheck's post and are instead read from NVD's own CVE 2.0 API record for each id, checked directly; a generic NVD per-CVE page is never cited as a source, so NVD is not listed among the sources cited above."
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Patch every self-managed Virtualizor installation to 3.2.9 patch 9 or 3.3.0 now, and keep admin-panel ports 4084/4085 off the public internet or behind an allowlist regardless of patch level."
updates: []
migrated_from: null
---

VulnCheck's Initial Access Intelligence team discloses three unauthenticated vulnerabilities in Virtualizor, Softaculous' commercial VPS/hypervisor control panel (KVM/OpenVZ/LXC), all reached through a single mis-scoped pre-authentication guard. In `enduser/admin.php`, the admin panel (ports 4084/4085) redirects every request to the login page except one: "the redirect that guards the admin panel fires for every action except one. That one is `login`" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)) — the `act=login` request that should only reach the login page instead falls through the guard and reaches an unauthenticated `from_billing_module` handler with no session, API key or slave credentials. CVE-2026-43641 (CVSS 9.8, CWE-78 OS command injection) is the flagship: the handler's `uid` field, taken unvalidated from an unserialized attacker POST body, is concatenated into a shell command inside `billing_unsuspend()` → `vexec()` → `proc_open()`, giving remote root command execution — VulnCheck states "verified on the lab: /tmp/x reads uid=0(root) gid=0(root) groups=0(root)" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). Exploitation requires only an existing, currently-suspended in-house-billing account on the target — server state that exists on any install using that billing mode by design — and no separate enumeration step is needed because the same request path is a non-destructive timing oracle: injecting a `sleep` payload via the `uid` field hangs the response only for a valid, eligible uid. The bug additionally needs MySQL's default non-strict `sql_mode`, which VulnCheck confirmed is what Virtualizor's own bundled MySQL 5.5.62 stack ships uncorrected — this is a default-production condition, not a lab artifact. The root-level impact is possible because Virtualizor's EMPS stack splits PHP execution across separate php-fpm pools by port: the admin-panel `index.php` on ports 4084/4085 runs in a pool that executes as root, while the client panel and every other `.php` file run in an unprivileged pool — the exploit therefore never drops a PHP web shell (which would run unprivileged) and instead relays each command's output to a randomly named static file written into the webroot and served directly over plain HTTP.

CVE-2026-43642 (CVSS 8.1, CWE-502 PHP object injection) reaches the same unauthenticated handler's native `unserialize()` call on attacker-controlled POST data with no `allowed_classes` restriction; no working exploitation gadget chain exists in the stock code today, but the primitive is live for any add-on or plugin that introduces a class with a `__wakeup` or `__destruct` method. CVE-2026-43643 (CVSS 7.5, CWE-639 authorization bypass through a user-controlled key) lets an unauthenticated caller zero out or inflate any tenant's account balance through the same handler's `whmcs` branch, via a parameterized but unauthenticated balance UPDATE with no ownership check. All three were confirmed exploitable on Virtualizor 3.2.9 patch 7 and patch 8. "Softaculous patched all three in 3.2.9 patch 9 (2026-09-01), and the fix carries into 3.3.0 (2026-09-09), the current build. Patch 7, the build audited above, and patch 8 are both still vulnerable" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)) — the fix requires a validated API call (HMAC API key or admin credentials) before the billing hook is reachable at all, casts the `uid` value to an integer before it reaches the shell, restricts the deserialization call with `allowed_classes => false`, and adds an ownership check to the balance-write branch. VulnCheck's post does not state whether it has observed in-the-wild exploitation; it also turned the command-injection flaw into a self-contained exploit module, built on VulnCheck's own open-source "go-exploit" framework, that fingerprints the Virtualizor admin panel, finds an eligible suspended account on its own via the timing oracle, and returns a root shell with no credentials and no account information supplied by the operator — VulnCheck's post demonstrates this module against its own lab instance and does not state that the CVE-specific module itself was released publicly, only that it is built on the publicly available go-exploit framework.

Detection concept: on any self-managed Virtualizor installation, monitor admin-panel access logs (ports 4084/4085) for unauthenticated POST requests carrying an `act=login` parameter combined with a `billing_data` or similar serialized payload field — a legitimate login request does not carry billing-module parameters. In host telemetry, alert on any process spawned by the root-privileged admin-panel php-fpm pool that is not part of Virtualizor's own known process tree, and on unexpected static files newly created directly in the webroot outside a deployment. **Triage:** a legitimate billing operation always carries valid session or API-key context; a request reaching the billing handler with neither is the discriminator, whatever its `act` parameter claims.

**Defender takeaway:** patch to 3.2.9 patch 9 or 3.3.0 now; independent of patch level, VulnCheck's own operational guidance is to keep Virtualizor's admin-panel ports off the public internet or behind an allowlist, since the underlying lesson — a shared tainted value trusted by a parameterized query is not automatically safe when the same value later reaches a shell command or file path — is a defect class a patch fixes once but a code-review habit prevents going forward.
