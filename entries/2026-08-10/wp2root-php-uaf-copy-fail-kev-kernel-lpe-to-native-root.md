---
schema: 1
kind: vulnerability
horizon: operational
title: "UPDATE — wp2root turns the WP2Shell foothold into fileless native root using a PHP unserialize use-after-free and the KEV-listed 'Copy Fail' kernel bug, defeating disable_functions and on-disk integrity monitoring"
headline: "The WordPress chain this pipeline tracks as exploited against Swiss sites now has a published route from sandboxed PHP to root"
summary: >
  Calif published wp2root on 2026-08-05, a post-exploitation chain that starts where the WP2Shell
  pre-auth WordPress RCE ends — sandboxed PHP execution — and reaches fileless native root even where
  disable_functions blocks system() and the filesystem is read-only. A use-after-free in PHP's legacy
  Serializable path yields native code execution that calls PHP's own system handler directly,
  bypassing disable_functions because that setting removes only the PHP-level name. The root step is
  CVE-2026-31431 ("Copy Fail"), a Linux kernel flaw that overwrites the page-cache copy of a
  setuid-root binary without touching the file on disk — and which has been CISA KEV-listed for
  confirmed exploitation since 2026-05-01, independent of this research.
discovered_at: "2026-08-10T04:43:00Z"
event_date: "2026-08-05"
run_id: 2026-08-10T0411Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, priv-esc, lpe, actively-exploited, cisa-kev, poc-public, patch-available]
regions: [global, europe, switzerland]
sectors: [public-sector, education, technology]
entities: []
techniques: [T1190, T1068, T1027.011]
affected_products: ["WordPress", "PHP", "Linux kernel"]
cves:
  - id: CVE-2026-31431
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, poc-public, patch-available]
    affected: "Linux kernel from the 2017 in-place AEAD change"
    fixed: "mainline commit a664bf3d603d and distribution backports"
sources:
  - url: "https://blog.calif.io/p/the-wordpress-chain-massacre"
    publisher: "Calif"
    date: "2026-08-05"
    role: primary
  - url: "https://copy.fail/"
    publisher: "Xint Code"
    date: "2026-04-29"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-08-07"
    role: corroborating
  - url: "https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/"
    publisher: "Linux kernel CVE team"
    date: "2026-04-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "wp2shell drops you inside the PHP interpreter, and on a hardened host that interpreter is locked down. Dangerous functions like system() and exec() are switched off with disable_functions, the filesystem can be mounted read-only, and there may be nowhere to write a file."
    publisher: "Calif"
  - quote: "The first recovers the native system handler and calls it directly, in native code, even though disable_functions took away the PHP-level name."
    publisher: "Calif"
  - quote: "The su file on disk is never modified, so file-integrity monitoring that watches file contents or writes to the binary sees nothing."
    publisher: "Calif"
  - quote: "The same 732-byte Python script roots every Linux distribution shipped since 2017."
    publisher: "Xint Code"
verification: multi-source
sourcing_note: >
  The chain write-up is the researcher's own; the kernel flaw it depends on is separately documented
  by its discloser and independently catalogued by CISA as exploited, which is what carries
  credibility to 1. The PHP unserialize use-after-free carries no CVE — this run confirmed that
  absence is consistent with PHP's own position that unserialize() memory-corruption bugs are not
  treated as security issues, and no identifier was invented for it. The KEV listing is cited to the
  catalog itself and the kernel flaw to the kernel's own CVE announcement, because neither of the two
  research write-ups mentions KEV, CISA or a score.
confidence: high
update_of: 2026-08-08/ncsc-ch-clickfix-wp2shell-etherhiding-vidar-swiss-websites
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Check kernel patch state for CVE-2026-31431 on any host running PHP web applications — it is KEV-listed since 2026-05-01 and fixed upstream; where patching lags, blocking AF_ALG socket creation removes the root step without affecting dm-crypt, kTLS, IPsec or the default TLS libraries."
migrated_from: null
---

**UPDATE (originally covered 2026-08-08):** the WP2Shell WordPress chain that NCSC-CH named as the entry point for compromised Swiss websites serving fake-CAPTCHA lures now has a published, fully documented route from where it stops to native root. Calif's wp2root write-up of 2026-08-05 is the delta ([Calif, 2026-08-05](https://blog.calif.io/p/the-wordpress-chain-massacre)); the original entry stands unchanged.

The premise is the hardened-host case defenders actually rely on. As the researcher puts it, "wp2shell drops you inside the PHP interpreter, and on a hardened host that interpreter is locked down. Dangerous functions like system() and exec() are switched off with disable_functions, the filesystem can be mounted read-only, and there may be nowhere to write a file." wp2root's contribution is that none of those three controls holds.

Escaping PHP uses a use-after-free on the legacy `Serializable` interface path, where recursive `unserialize()` calls inside a `Serializable::unserialize()` body share the outer parser's reference table and a later property-table resize frees a bucket the outer parser still holds. The resulting arbitrary read builds a chain that locates the PHP binary and its gadgets in the live process rather than relying on hardcoded offsets, and then — this is the part that matters for anyone treating `disable_functions` as a boundary — "recovers the native system handler and calls it directly, in native code, even though disable_functions took away the PHP-level name." The setting removes a name, not the underlying handler. The alternative path launches a position-independent stager that creates an anonymous in-memory file, pins it on a file descriptor that survives `execve`, and executes it without anything reaching disk.

The root step is where this stops being a research curiosity. It is CVE-2026-31431, "Copy Fail" — a logic flaw reachable through the kernel's AF_ALG crypto socket interface and `splice()` that lets an unprivileged local user overwrite the page-cache copy of a setuid-root binary with a small write. Running that binary then executes the attacker's cached stub as root. Its discloser is explicit about the defensive consequence: "The su file on disk is never modified, so file-integrity monitoring that watches file contents or writes to the binary sees nothing." The same page records that "The same 732-byte Python script roots every Linux distribution shipped since 2017" ([Xint Code, 2026-04-29](https://copy.fail/)).

The fact that changes the risk calculation, and that neither the original coverage nor the queue note carried: CVE-2026-31431 has been on CISA's Known Exploited Vulnerabilities catalogue since 2026-05-01, listed as a Linux Kernel incorrect-resource-transfer flaw allowing privilege escalation, entirely independent of this chain-building exercise ([CISA, catalog version 2026.08.07](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); the kernel's own CVE announcement records the flaw ([Linux kernel CVE team, 2026-04-22](https://lore.kernel.org/linux-cve-announce/2026042214-CVE-2026-31431-3d65@gregkh/)). The kernel half of wp2root is not a proof of concept — it is a bug attackers are already using, now documented as the root step for a WordPress compromise path with confirmed exploitation against this constituency's own web estate.

Detection, telemetry class first. On the PHP side the discriminating signal is a web-server worker process spawning a child whose executable resolves to an anonymous memory-backed file rather than a normal on-disk binary — legitimate PHP application workflows do not create processes that way, which makes it low-noise. For the kernel step, any process holding an AF_ALG socket is itself unusual: the mainstream consumers of kernel crypto, including disk encryption, kernel TLS and IPsec, use the in-kernel API and never touch AF_ALG. **Triage:** a setuid-root binary executing is ordinary on every Linux host, so that event alone is noise; the composite that is not ordinary is an AF_ALG socket opened and closed by a web-application process, followed shortly by a setuid binary running under that same process tree. **Defender takeaway:** the durable lesson is that `disable_functions` and a read-only filesystem are defence in depth, not a boundary — this chain walks through both — so a WordPress pre-auth RCE should be scoped as potential host root, not as contained web-tier execution. Patching the kernel closes the published root step; the PHP-side escape remains reachable from any pre-existing code-execution foothold.
