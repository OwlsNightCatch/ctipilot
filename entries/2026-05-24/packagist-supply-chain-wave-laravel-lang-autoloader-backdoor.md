---
schema: 1
kind: threat
horizon: operational
title: "Packagist supply-chain wave: Laravel-Lang autoloader backdoor and the cross-ecosystem postinstall strand"
headline: "Packagist supply-chain wave: Laravel-Lang autoloader backdoor and the cross-ecosystem postinstall strand"
summary: "A Packagist (PHP/Composer) supply-chain wave hit the Laravel-Lang ecosystem — 700+ version tags rewritten to point at attacker forks, an autoload.files backdoor that executes on every request, and a separate 8-package package.json postinstall strand dropping a Linux implant. Full mechanics in today's deep dive (Socket, 2026-05-23)."
discovered_at: "2026-05-24T05:00:06Z"
event_date: 2026-05-23
run_id: 2026-05-24-f1fd8070
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - data-breach
  - cloud
regions:
  - global
  - europe
sectors:
  - public-sector
  - technology
  - education
entities:
  - "campaign:packagist-laravel-lang-supply-chain-2026"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://socket.dev/blog/laravel-lang-compromise"
    publisher: "Socket — Laravel-Lang, 2026-05-23"
    role: primary
  - url: "https://socket.dev/blog/malicious-postinstall-hook-found-across-700-github-repos"
    publisher: "Socket — postinstall strand, 2026-05-22"
    role: corroborating
  - url: "https://www.aikido.dev/blog/supply-chain-attack-targets-laravel-lang-packages-with-credential-stealer"
    publisher: "Aikido, 2026-05-23"
    role: corroborating
  - url: "https://www.stepsecurity.io/blog/laravel-lang-supply-chain-attack"
    publisher: "StepSecurity, 2026-05-22"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html"
    publisher: "The Hacker News, 2026-05-23"
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-24.md
---

**Background.** The 2026 software supply chain has absorbed a sustained run of registry- and repo-level compromises — the mini-shai-hulud / TeamPCP npm/PyPI worm, the Megalodon GitHub-repo backdooring campaign (covered 2026-05-23), and the actions-cool/issues-helper GitHub Action and nx-console VS Code extension compromises (covered 2026-05-20). Those targeted npm, PyPI and CI tooling; the Packagist (PHP/Composer) ecosystem had largely escaped. Between 2026-05-22 and 2026-05-23 that changed, in two technically distinct, concurrent strands with different delivery mechanics — each flagged within hours by Socket, Aikido and StepSecurity ([Socket, 2026-05-23](https://socket.dev/blog/laravel-lang-compromise)). Socket reports the postinstall strand alone spans 700+ associated GitHub repositories under common attacker infrastructure ([Socket, 2026-05-22](https://socket.dev/blog/malicious-postinstall-hook-found-across-700-github-repos)); whether a single operator runs both strands is not established by the cited reporting.

**Strand 1 — Laravel-Lang tag rewrite + autoloader backdoor.** An actor with organisation-level push access to the Laravel-Lang GitHub org rewrote more than 700 historical version tags across four community PHP localisation packages — `laravel-lang/lang` (~7.8k stars), `laravel-lang/http-statuses`, `laravel-lang/attributes`, `laravel-lang/actions`. Rather than committing to the canonical repos, the attacker pointed existing version tags at commits in attacker-controlled forks, so the malicious code never appears in the main repository's commit history ([StepSecurity, 2026-05-22](https://www.stepsecurity.io/blog/laravel-lang-supply-chain-attack)). The injected `src/helpers.php` is registered under each `composer.json`'s `autoload.files` key. Because every Composer application executes `require __DIR__.'/vendor/autoload.php'` at boot — Laravel, Symfony and PHPUnit included — the backdoor runs on every request with no post-install step required. A per-host MD5 fingerprint (directory path + architecture + inode) makes the payload fire once per machine to evade redundant-execution detection. The dropper builds its command-and-control hostname at runtime from character-code arrays (`array_map('chr', …)`) to defeat static string analysis, disables TLS certificate verification, spoofs a browser User-Agent, and fetches a ~5,900-line PHP credential stealer, which it writes to a hidden temp file and runs via `exec("php …")` on Unix or a VBScript-plus-`cscript` chain on Windows ([Socket, 2026-05-23](https://socket.dev/blog/laravel-lang-compromise)). The stealer is organised into fifteen collector modules targeting saved passwords from multiple Chromium-based browsers, Google Cloud application-default credentials, Docker auth tokens, SSH private keys, Git credentials (`.gitconfig`, `.git-credentials`, `.netrc`), shell and database history, `kubeconfig`, `.env`, `wp-config.php`, `docker-compose.yml`, VPN configurations, cryptocurrency wallets and password-manager vaults; results are AES-256-encrypted, exfiltrated, and the stealer self-deletes ([Aikido, 2026-05-23](https://www.aikido.dev/blog/supply-chain-attack-targets-laravel-lang-packages-with-credential-stealer)).

**Strand 2 — eight packages, cross-ecosystem postinstall.** A concurrent campaign poisoned eight Packagist packages — `devdojo/wave`, `devdojo/genesis`, `katanaui/katana`, `elitedevsquad/sidecar-laravel`, `r2luna/brain`, `baskarcm/tzi-chat-ui`, `moritz-sauer-13/silverstripe-cms-theme` and `crosiersource/crosierlib-base` — by inserting a malicious hook into `package.json` (not `composer.json`) `scripts.postinstall` ([Socket, 2026-05-22](https://socket.dev/blog/malicious-postinstall-hook-found-across-700-github-repos)). The cross-ecosystem placement is deliberate: teams auditing PHP/Composer dependencies routinely skip the `package.json` lifecycle hooks bundled alongside JS build tooling. The hook downloads a Linux ELF from a code-hosting release URL, writes it to a hidden executable file under `/tmp` masquerading as an SSH daemon (e.g. `/tmp/.sshd`), marks it executable and launches it in the background with TLS verification suppressed and error output silenced ([The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/packagist-supply-chain-attack-infects-8.html)). The eight span CMS themes and developer libraries — including a SilverStripe CMS theme (`moritz-sauer-13/silverstripe-cms-theme`) and the `crosiersource/crosierlib-base` library — so the blast radius reaches any PHP project that pulled them as a direct or transitive dependency.

**Kill chain → MITRE ATT&CK.** Initial access and execution map to [`T1195.002`](https://attack.mitre.org/techniques/T1195/002/) (Compromise Software Supply Chain) and [`T1059.004`](https://attack.mitre.org/techniques/T1059/004/) (Unix Shell, via `exec`/postinstall); the runtime C2-hostname assembly and AES-256 output to [`T1140`](https://attack.mitre.org/techniques/T1140/) (Deobfuscate/Decode Information); the `/tmp/.sshd` naming to [`T1036.005`](https://attack.mitre.org/techniques/T1036/005/) (Masquerading: Match Legitimate Name or Location); the stealer's harvesting to [`T1552.001`](https://attack.mitre.org/techniques/T1552/001/) (Credentials in Files) and [`T1083`](https://attack.mitre.org/techniques/T1083/) (File and Directory Discovery); and the JS-side delivery to [`T1204.002`](https://attack.mitre.org/techniques/T1204/002/) (User Execution: Malicious File).

**Detection concepts (no IOCs).** Audit `composer.lock` for any of the four `laravel-lang/*` packages at versions tagged in the 2026-05-22 → 2026-05-23 window, and for the eight named Strand-2 packages. Flag any `autoload.files` entry introduced by a version-tag change that has no counterpart in the package's upstream git history, and treat any `scripts.postinstall` / `scripts.preinstall` hook inside a PHP-only Composer package as a high-fidelity anomaly. On hosts and CI runners, hunt (Sysmon EID 1 / Linux auditd) for web-server worker processes (`php-fpm`, `php-cgi`, `apache2`, `nginx`) spawning `exec("php …")` or `cscript.exe`, for `composer`/`npm` spawning shells or initiating network connections during install, and for an executable hidden file under `/tmp` resembling `sshd`. Egress monitoring: outbound HTTPS from PHP worker processes during autoload, and installs pulling binaries from code-hosting release CDNs during `composer`/`npm install`.

**Hardening.** Run `composer audit` (Composer 2.6+), pin exact dependency versions, and verify `composer.lock` hash integrity in CI. Review whether organisation-level GitHub token scoping permits tag rewrites across all repositories and rotate admin tokens if compromise is suspected. On any affected host, treat **all** secrets reachable by the PHP worker process — cloud keys, SSH keys, `.env`, Git tokens — as compromised and rotate aggressively. For the JS-tooling surface, adopt npm's new staged-publishing 2FA gate and `--allow-remote none` / `--allow-directory none` install controls (. Note that Packagist removed the malicious versions, but development branches stay infected while upstream GitHub repos remain compromised — verify upstream state before reinstalling any of the named packages.
