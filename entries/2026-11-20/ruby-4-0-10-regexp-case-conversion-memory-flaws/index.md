---
schema: 1
kind: vulnerability
title: "Ruby 4.0.10, 3.4.13 and 3.3.14: seven memory-safety flaws in the regexp engine and string case conversion, three rated Critical by the project, with proofs of concept for code execution; Veria Labs says Rails and classic Sinatra are exposed by default and announces a public Rails exploit for 25 November 2026 (CVE-2026-132825, CVSS 3.1 7.4)"
headline: "Ruby 4.0.10, 3.4.13, 3.3.14 fix seven memory flaws; Veria's Rails exploit not found yet: update the interpreter"
summary: >
  The Ruby project released 4.0.10, 3.4.13 and 3.3.14 on 2026-11-18 for seven memory-corruption flaws in the regexp engine and in string case conversion, three rated Critical, and says it knows of proofs of concept that reach remote code execution. Veria Labs, which found the case-conversion flaw independently (CVE-2026-132825, a one-byte heap overflow), says Rails and classic-style Sinatra are exposed without authentication in their default configuration and announced a code-execution proof of concept on stock Rails for 25 November 2026, which its page, blog feed and GitHub organisation did not show as released on 2026-11-27; no exploitation is reported. GitHub Enterprise Server and older GitLab branches now carry the fix. Ruby 3.2 and earlier are end of life, and the interpreter itself, not a gem, must be updated.
discovered_at: "2026-11-20T05:07:00Z"
updated_at: "2026-11-27T04:57:00Z"
event_date: "2026-11-18"
run_id: 2026-11-20T0356Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, patch-available]
regions: [global]
sectors: [public-sector, technology]
entities: ["product:ruby", "product:gitlab", "product:github-enterprise-server"]
techniques: [T1190]
affected_products: ["Ruby", "GitLab", "GitHub Enterprise Server"]
cves:
  - id: CVE-2026-132825
    cvss: "7.4"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "Ruby 3.3.13 and earlier, 3.4.0 to 3.4.12, 4.0.0 to 4.0.9, where an attacker-controlled string in a single-byte encoding such as ISO-8859-1 or Windows-1252 reaches a case-changing method; Ruby 3.2 and earlier are end of life"
    fixed: "3.3.14; 3.4.13; 4.0.10; no fix for Ruby 3.2 and earlier"
sources:
  - url: "https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/"
    publisher: "Ruby project"
    date: "2026-11-18"
    role: primary
  - url: "https://github.com/ruby/ruby/security/advisories/GHSA-34m4-m9fh-gqp5"
    publisher: "Ruby project (GHSA-34m4-m9fh-gqp5)"
    date: "2026-11-18"
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/13205"
    publisher: "NCSC.ch Cyber Security Hub"
    date: "2026-11-19"
    role: corroborating
  - url: "https://verialabs.com/ruby2shell/"
    publisher: "Veria Labs"
    date: "2026-11-19"
    role: corroborating
  - url: "https://watchtowr.com/intelligence/ruby-cve-2026-132825-faq/"
    publisher: "watchTowr"
    date: "2026-11-19"
    role: corroborating
  - url: "https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-129481"
    publisher: "ENISA EUVD (EUVD-2026-129481)"
    date: "2026-11-19"
    role: corroborating
  - url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/"
    publisher: "GitLab"
    date: "2026-11-20"
    role: corroborating
  - url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/"
    publisher: "GitLab (19.6.2)"
    date: "2026-11-25"
    role: corroborating
  - url: "https://docs.github.com/en/enterprise-server@3.22/admin/release-notes"
    publisher: "GitHub Enterprise Server release notes"
    date: "2026-11-22"
    role: corroborating
  - url: "https://docs.github.com/en/enterprise-server@3.21/admin/release-notes"
    publisher: "GitHub Enterprise Server release notes"
    date: "2026-11-22"
    role: corroborating
  - url: "https://docs.github.com/en/enterprise-server@3.20/admin/release-notes"
    publisher: "GitHub Enterprise Server release notes"
    date: "2026-11-22"
    role: corroborating
  - url: "https://docs.github.com/en/enterprise-server@3.19/admin/release-notes"
    publisher: "GitHub Enterprise Server release notes"
    date: "2026-11-22"
    role: corroborating
  - url: "https://durendal.sh/blog/ruby-case-mapping-bugs"
    publisher: "Durendal (Moritz Sanft)"
    date: "2026-11-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We are aware of PoCs that prove some of them can be used to trigger remote code execution."
    publisher: "Ruby project"
    source_url: "https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/"
  - quote: "We'll be publishing a proof of concept demonstrating remote code execution on stock Rails on 25 November 2026"
    publisher: "Veria Labs"
    source_url: "https://verialabs.com/ruby2shell/"
  - quote: "Proof of Concepts will become available in a week."
    publisher: "NCSC.ch Cyber Security Hub"
    source_url: "https://security-hub.ncsc.admin.ch/#/posts/13205"
  - quote: "The fix for CVE-2026-132825 is a patch to Ruby."
    publisher: "GitLab"
    source_url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/"
  - quote: "Where an update was not immediately possible, mitigations were introduced at the application level."
    publisher: "GitHub Enterprise Server release notes"
    source_url: "https://docs.github.com/en/enterprise-server@3.22/admin/release-notes"
  - quote: "backported to GitLab versions 19.3.10, 19.2.11, 19.1.11, 19.0.12, and 18.11.15"
    publisher: "GitLab (19.6.2)"
    source_url: "https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/"
verification: multi-source
sourcing_note: >
  The Ruby project is the disclosing party and published seven GitHub advisories by GHSA id because CVE ids had not been assigned. CVE-2026-132825, assigned by MITRE and not by the Ruby project, names the case-conversion overflow (GHSA-34m4), and ENISA lists it under a different GHSA id; the other six flaws have no CVE id yet. The default-configuration exposure of Rails and Sinatra, the product list and the 25 November proof-of-concept date come from Veria Labs (and, for Rails and Sinatra, NCSC.ch), not from the Ruby advisories, which name no product. Veria Labs says it found the flaw independently and was the first to demonstrate remote code execution, and its page acknowledges the project's credit.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Update the Ruby interpreter to 4.0.10, 3.4.13 or 3.3.14 on every application host, worker, CI runner and container image that runs Rails, Sinatra or other Ruby code that handles untrusted text, rebuild the images and restart the workers, because updating a gem does not fix the interpreter, Rails is exposed in its default configuration and Veria Labs' Rails exploit, announced for 25 November 2026, may be released at any time."
  - "Upgrade every self-managed GitLab to 19.6.1, 19.5.8 or 19.4.10 or later, or on an older branch to 19.3.10, 19.2.11, 19.1.11, 19.0.12 or 18.11.15 (a self-compiled installation rebuilds Ruby 3.3.14 or 3.4.13 instead), because GitLab ships the Ruby fix as critical patch releases and Veria Labs' Rails exploit is announced."
  - "Upgrade every GitHub Enterprise Server appliance to 3.22.6, 3.21.11, 3.20.13 or 3.19.17, because GitHub's release of 2026-11-22 carries the Ruby fix and Rails-class exploit proofs exist."
updates:
  - at: "2026-11-22T04:32:01Z"
    run_id: 2026-11-22T0355Z-intel
    type: update
    summary: >
      GitLab shipped an ad-hoc critical patch release, 19.6.1, 19.5.8 and 19.4.10, whose only security fix
      is the Ruby flaw CVE-2026-132825, and Veria Labs' table now lists Chatwoot as patched in 4.20.1;
      only GitHub Enterprise Server 3.22.5 and earlier is still shown without a fix.
    fields: [affected_products, entities, sources, evidence, actions, body]
  - at: "2026-11-27T04:57:00Z"
    run_id: 2026-11-27T0355Z-intel
    type: update
    summary: >
      GitHub Enterprise Server 3.22.6, 3.21.11, 3.20.13 and 3.19.17 (2026-11-22) carry the Ruby fix and GitLab's
      2026-11-25 release backports it to five older branches, so Veria Labs' table, unchanged since 2026-11-21, is stale;
      Veria's announced Rails exploit was not found released on 2026-11-27, and a co-discoverer says a plain Rails app is
      exploitable.
    fields: [headline, summary, affected_products, entities, sources, evidence, sourcing_note, actions, body, updated_at]
migrated_from: null
---

The Ruby project released 4.0.10, 3.4.13 and 3.3.14 on 2026-11-18 to fix seven vulnerabilities in the regexp engine and in string case conversion, and says it is aware of proofs of concept that prove some of them can be used to trigger remote code execution ([Ruby project, 2026-11-18](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)). NCSC.ch lists three as Critical, a one-byte heap overflow in case conversion of strings in single-byte encodings such as ISO-8859-1 and Windows-1252, a double free in regexp compilation and a heap overflow from an integer overflow in regexp compilation, and the rest as High or Moderate ([NCSC.ch, 2026-11-19](https://security-hub.ncsc.admin.ch/#/posts/13205)); the project's advisory for the first confirms it can write one byte past the output buffer ([Ruby project, 2026-11-18](https://github.com/ruby/ruby/security/advisories/GHSA-34m4-m9fh-gqp5)). Affected are Ruby 3.3.13 and earlier, 3.4.0 to 3.4.12 and 4.0.0 to 4.0.9, and Ruby 3.2 and earlier are end of life and unfixed ([Ruby project, 2026-11-18](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)).

NCSC.ch says Rails and classic-style Sinatra are exposed to the case-conversion overflow in their default configuration ([NCSC.ch, 2026-11-19](https://security-hub.ncsc.admin.ch/#/posts/13205)); watchTowr reports no exploitation as of 2026-11-19 ([watchTowr, 2026-11-19](https://watchtowr.com/intelligence/ruby-cve-2026-132825-faq/)). Veria Labs, which says it found the flaw independently and first demonstrated code execution, calls it Ruby2Shell, says it is reachable without authentication on Rails and classic Sinatra and that plain Rack and other frameworks are not exposed by default, and announced a proof of concept for remote code execution on stock Rails for 25 November 2026, or later if major vendors have not shipped a fix; its page, blog feed and GitHub organisation showed no release on 2026-11-27 ([Veria Labs, 2026-11-19](https://verialabs.com/ruby2shell/)). Moritz Sanft, a co-discoverer Veria names, writes that a plain Rails application is enough to be exploitable and that OpenAI sent the Ruby maintainers working exploit proofs on 2026-11-07 ([Durendal, 2026-11-19](https://durendal.sh/blog/ruby-case-mapping-bugs)). GitHub Enterprise Server 3.22.6 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.22/admin/release-notes)), 3.21.11 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.21/admin/release-notes)), 3.20.13 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.20/admin/release-notes)) and 3.19.17 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.19/admin/release-notes)) carry the Ruby fix, although Veria's table, last changed on 2026-11-21, still shows 3.22.5 and earlier unfixed; it lists Chatwoot (4.20.1), GitLab, Mastodon, OpenProject and the Discourse base image as patched, and the Ruby advisories name no product, so the vendors' own advisories decide for each ([Veria Labs, 2026-11-19](https://verialabs.com/ruby2shell/)). CVE-2026-132825 names the case-conversion overflow and is scored CVSS 3.1 7.4 with a local attack vector and high complexity ([ENISA EUVD, 2026-11-19](https://euvdservices.enisa.europa.eu/api/enisaid?id=EUVD-2026-129481)); the Ruby announcement says CVE identifiers were requested and none was assigned at publication, so the other six flaws are known by GHSA id ([Ruby project, 2026-11-18](https://www.ruby-lang.org/en/news/2026/11/18/multiple-vulnerabilities-in-regexp-and-string/)).

**Exposure:** Ruby 3.3, 3.4 and 4.0 below the fixed releases that run Rails or classic Sinatra, or any application that passes untrusted text to a case-changing method or compiles untrusted regexp patterns; the interpreter version is shown by `ruby -v`, and self-hosted products that bundle Ruby carry their own fix timeline ([NCSC.ch, 2026-11-19](https://security-hub.ncsc.admin.ch/#/posts/13205)).

**Detection:** crashes, segmentation faults and abnormal restarts of Ruby application workers that coincide with requests carrying long single-byte-encoded text or unusual regexp parameters, and a shell or network tool spawned by a Ruby worker process.

**Defender takeaway:** update the interpreter, not the gems, rebuild container images and restart workers, since exploit proofs exist and Veria's proof of concept may appear at any time; until then NCSC.ch's temporary measures are to avoid compiling regexps from untrusted input and, for the case-conversion flaw, to convert input to UTF-8 so the vulnerable path is not reached ([NCSC.ch, 2026-11-19](https://security-hub.ncsc.admin.ch/#/posts/13205)).

## Update — 2026-11-22T04:32:01Z

GitLab released 19.6.1, 19.5.8 and 19.4.10 on 2026-11-20 as a critical patch release for self-managed installations, with CVE-2026-132825 as its only security fix; GitLab.com and GitLab Dedicated are already patched ([GitLab, 2026-11-20](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/)). The fix is a patch to Ruby: official Linux packages and container images already carry it, while a self-compiled installation must rebuild Ruby 3.3.14 or 3.4.13 or a later release of the same series, and the release also covers the other flaws in the Ruby advisory ([GitLab, 2026-11-20](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-1-released/)). Veria Labs' software table now lists Chatwoot 4.20.0 and earlier as fixed in 4.20.1, leaving GitHub Enterprise Server 3.22.5 and earlier as the one product shown without a fixed release, and its proof of concept for stock Rails is still announced for 25 November 2026, or later if major vendors have not shipped a fix ([Veria Labs, 2026-11-19](https://verialabs.com/ruby2shell/)).

## Update — 2026-11-27T04:57:00Z

GitHub's release notes list the Ruby update as a critical fix in GitHub Enterprise Server 3.22.6 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.22/admin/release-notes)), 3.21.11 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.21/admin/release-notes)), 3.20.13 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.20/admin/release-notes)) and 3.19.17 ([GitHub, 2026-11-22](https://docs.github.com/en/enterprise-server@3.19/admin/release-notes)), all dated 2026-11-22, with application-level mitigations where an update was not immediately possible; they name no Ruby version or CVE. GitLab's release of 2026-11-25 backports the Ruby fix, a bump to Ruby 3.3.14 and 3.4.13, to 19.3.10, 19.2.11, 19.1.11, 19.0.12 and 18.11.15, which it calls an exception to its maintenance policy ([GitLab, 2026-11-25](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-6-2-released/)).

Veria Labs' Rails proof of concept was announced for 2026-11-25 or later; its page, blog feed and GitHub organisation show no release as of 2026-11-27, which does not show that no exploit exists. Sanft writes that Rack's multipart method override and a field charset reach the vulnerable case conversion in a plain Rails application, and that OpenAI sent the Ruby maintainers working exploit proofs for the case-conversion and an integer-overflow flaw on 2026-11-07; the second flaw is limited to Rack 3.2.1 and earlier ([Durendal, 2026-11-19](https://durendal.sh/blog/ruby-case-mapping-bugs)).
