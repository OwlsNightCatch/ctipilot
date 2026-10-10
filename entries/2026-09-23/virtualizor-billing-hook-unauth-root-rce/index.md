---
schema: 1
kind: vulnerability
title: "Virtualizor VPS/hypervisor control panel: a login-page guard's own exemption for act=login lets an unauthenticated attacker reach root"
headline: "A single mis-scoped pre-auth check in a hosting control panel exposes three unauthenticated flaws, one a path to root"
summary: >
  Softaculous Virtualizor's admin panel guards every pre-authentication
  request except one: a request with act=login walks straight into an
  unauthenticated billing-module handler. From there, an attacker reaches
  unauthenticated root command execution, PHP object injection, or
  arbitrary tenant-balance manipulation. Fixed in 3.2.9 patch 9 / 3.3.0. The root command injection needs an existing suspended in-house-billing account, so it is not precondition-free. VulnCheck turned it into a self-contained module for its open-source go-exploit framework that needs no credentials from the operator, and its post says neither whether that module is public nor whether it observed in-the-wild exploitation.
discovered_at: "2026-09-23T04:52:00Z"
updated_at: null
event_date: "2026-09-22"
run_id: 2026-09-23T0405Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [technology]
entities: ["product:softaculous-virtualizor"]
techniques: [T1190]
affected_products: ["Softaculous Virtualizor"]
cves:
  - id: CVE-2026-43641
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "≤ 3.2.9 patch 8 (in-house billing enabled, an existing suspended account, MySQL default non-strict sql_mode)"
    fixed: "3.2.9 patch 9 (2026-09-01) / 3.3.0"
  - id: CVE-2026-43642
    cvss: null
    epss: null
    type: deserialization
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "≤ 3.2.9 patch 8"
    fixed: "3.2.9 patch 9 (2026-09-01) / 3.3.0"
  - id: CVE-2026-43643
    cvss: null
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
sourcing_note: "VulnCheck is both the discovering researcher and the CVE Numbering Authority for these three ids, so its disclosure serves as the primary in place of a vendor advisory. No independent technical analysis has been published yet."
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
updates:
  - at: "2026-09-30T06:56:15Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Priority is lowered from high to notable: a flaw in hosting-provider billing software outside
      the typical public-administration estate. CVSS scores that the cited disclosure does not carry
      are removed from the text and the structured data, and the sourcing note keeps provenance
      only. The patch-level statement now separates the audited patch 7 from VulnCheck's re-test of
      patch 8, the summary no longer calls VulnCheck's exploit module internal or unpublished, and
      the detection concept and triage line now cite VulnCheck. The default-configuration tag is
      removed, because the root command injection needs an existing suspended in-house-billing
      account. The headline now says only one of the three flaws reaches root.
    fields: [priority, cves, body, sourcing_note, summary, tags, headline, techniques]
migrated_from: null
---

VulnCheck's Initial Access Intelligence team discloses three unauthenticated vulnerabilities in Virtualizor, Softaculous' commercial VPS/hypervisor control panel (KVM/OpenVZ/LXC), all reached through a single mis-scoped pre-authentication guard. In `enduser/admin.php`, the admin panel (ports 4084/4085) redirects every request to the login page except one: "the redirect that guards the admin panel fires for every action except one. That one is `login`" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). The `act=login` request that should only reach the login page instead falls through the guard and reaches an unauthenticated `from_billing_module` handler with no session, API key or slave credentials. CVE-2026-43641 (CWE-78 OS command injection) is the flagship: the handler's `uid` field, taken unvalidated from an unserialized attacker POST body, is concatenated into a shell command inside `billing_unsuspend()` → `vexec()` → `proc_open()`, giving remote root command execution. VulnCheck states "verified on the lab: /tmp/x reads uid=0(root) gid=0(root) groups=0(root)" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). Exploitation requires an existing in-house-billing account on the target that is currently suspended and paid up, server state that exists on any install using that billing mode by design, and no separate enumeration step is needed because the same request path is a non-destructive timing oracle: injecting a `sleep` payload via the `uid` field hangs the response only for a valid, eligible uid. The bug additionally needs MySQL's default non-strict `sql_mode`, which VulnCheck confirmed is what Virtualizor's own bundled MySQL 5.5.62 stack ships uncorrected, so this is a default-production condition, not a lab artifact. The root-level impact is possible because Virtualizor's EMPS stack splits PHP execution across separate php-fpm pools by port: the admin-panel `index.php` on ports 4084/4085 runs in a pool that executes as root, while the client panel and every other `.php` file run in an unprivileged pool. The exploit therefore never drops a PHP web shell (which would run unprivileged) and instead relays each command's output to a randomly named static file written into the webroot and served directly by nginx.

CVE-2026-43642 (CWE-502 PHP object injection) reaches the same unauthenticated handler's native `unserialize()` call on attacker-controlled POST data with no `allowed_classes` restriction; no working exploitation gadget chain exists in the stock code today, but the primitive is live for any add-on or plugin that introduces a class with a `__wakeup` or `__destruct` method. CVE-2026-43643 (CWE-639 authorization bypass through a user-controlled key) lets an unauthenticated caller zero out or inflate any tenant's account balance through the same handler's `whmcs` branch, via a parameterized but unauthenticated balance UPDATE with no ownership check. VulnCheck audited 3.2.9 patch 7 and, in a 2026-09-20 re-test from decoded source, found patch 8 vulnerable as well ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). "Softaculous patched all three in 3.2.9 patch 9 (2026-09-01), and the fix carries into 3.3.0 (2026-09-09), the current build. Patch 7, the build audited above, and patch 8 are both still vulnerable" ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). The fix requires a validated API call (HMAC API key or admin credentials) before the billing hook is reachable at all, casts the `uid` value to an integer before it reaches the shell, restricts the deserialization call with `allowed_classes => false`, and adds an ownership check to the balance-write branch. VulnCheck's post does not state whether it has observed in-the-wild exploitation; it also turned the command-injection flaw into a self-contained exploit module, built on VulnCheck's own open-source "go-exploit" framework, that fingerprints the Virtualizor admin panel, finds an eligible suspended account on its own via the timing oracle, and returns a root shell with no credentials and no account information supplied by the operator. VulnCheck's post demonstrates this module against its own lab instance and does not state that the CVE-specific module itself was released publicly, only that it is built on the publicly available go-exploit framework.

Detection concept: VulnCheck's exploit reaches the admin panel on ports 4084/4085 with `act=login` and `from_billing_module` set and a serialized `billing_data` field in the POST body ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). On any self-managed Virtualizor installation, look in admin-panel access logs for unauthenticated requests carrying that combination, since a login request has no use for billing-module parameters. The injected commands run in the admin panel's root php-fpm pool and relay their output through randomly named static files written into the webroot and then removed ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)), so in host telemetry alert on processes spawned by that pool outside Virtualizor's own process tree and on short-lived static files created in the webroot outside a deployment. **Triage:** in the fixed build the billing hook runs only after a validated API call, a valid API key or admin API credentials ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)), so a request reaching the billing handler with no session or API-key context is the discriminator, whatever its `act` parameter claims.

**Defender takeaway:** patch to 3.2.9 patch 9 or 3.3.0 now; independent of patch level, VulnCheck's own operational guidance is to keep Virtualizor's admin-panel ports off the public internet or behind an allowlist, since the underlying lesson — a shared tainted value trusted by a parameterized query is not automatically safe when the same value later reaches a shell command or file path — is a defect class a patch fixes once but a code-review habit prevents going forward.

## Correction — 2026-09-30T06:56:15Z

VulnCheck's disclosure gives no CVSS scores for the three flaws ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)). The scores shown earlier are not on that page and are no longer shown. The weakness classes, CWE-78, CWE-502 and CWE-639, come from VulnCheck's own table ([VulnCheck, 2026-09-22](https://www.vulncheck.com/blog/virtualizor-billing-hook-unauthenticated-root-rce)).
