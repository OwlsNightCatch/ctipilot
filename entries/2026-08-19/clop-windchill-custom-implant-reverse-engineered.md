---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — Cl0p's Windchill implant, reverse-engineered: a custom request header carries the commands, one of them decrypts the whole keystore including the LDAP manager password, and a built-in class loader turns it into an unlimited backdoor"
headline: "The web shell is written against Windchill's own Java classes, so its database queries wear the application's identity"
summary: >
  ReliaQuest published a reverse-engineering analysis on 2026-08-18 of the custom web shell deployed after
  exploitation of CVE-2026-12569 in PTC Windchill, attributing it highly likely to Cl0p. The implant is
  purpose-built against the application: commands arrive in a custom X-windchill-req HTTP request header
  rather than a body, a single S command reads Windchill's configuration file and decrypts every value in
  the application keystore — the LDAP manager password and all site administrator keys included — and a
  built-in Java class loader executes attacker-supplied bytecode from a Base64 ZIP entirely in memory. Its
  database queries run through Windchill's own MethodContext and WTConnection classes, so database
  telemetry attributes them to the application's normal service identity. General Electric confirmed on
  2026-08-17 that it is assessing Cl0p's claims, joining Philips and Shell.
discovered_at: "2026-08-19T04:58:00Z"
event_date: "2026-08-18"
run_id: 2026-08-19T0410Z-intel
priority: high
immediate_action: null
tags: [ransomware, organized-crime, data-breach, vulnerabilities, actively-exploited, rce, pre-auth, cisa-kev]
regions: [global, europe]
sectors: [manufacturing, energy, healthcare, defense, retail]
entities: [actor:clop, campaign:clop-windchill-flexplm-extortion-2026]
techniques: [T1190, T1505.003, T1071.001, T1620, T1555, T1552.001, T1213, T1041, T1657]
affected_products: ["PTC Windchill", "PTC FlexPLM"]
cves:
  - id: CVE-2026-12569
    cvss: "9.3"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Internet-exposed PTC Windchill and PTC FlexPLM instances prior to the vendor fix"
    fixed: "PTC began releasing fixes on 2026-06-17"
sources:
  - url: "https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign"
    publisher: "ReliaQuest Threat Research Team"
    date: "2026-08-18"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/"
    publisher: "BleepingComputer"
    date: "2026-08-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext."
    publisher: "ReliaQuest Threat Research Team"
  - quote: "It accepts a Base64-encoded ZIP file containing compiled Java bytecode, loads it directly into memory, and executes it."
    publisher: "ReliaQuest Threat Research Team"
  - quote: "Identifying this activity requires header logging that captures non-standard values, response decompression, and TLS inspection; without all three, coverage against this web shell's traffic is partial at best."
    publisher: "ReliaQuest Threat Research Team"
  - quote: "This activity was highly likely conducted by the Clop extortion group."
    publisher: "ReliaQuest Threat Research Team"
  - quote: "While a GE spokesperson said the company is aware of the claim and is \"working to assess the potential issue,\" a Philips spokesperson confirmed its systems were breached but said the incident has been contained and didn't affect customers."
    publisher: "BleepingComputer"
verification: multi-source
sourcing_note: >
  The implant analysis rests on ReliaQuest's own reverse engineering, read directly; it is the only party to
  have published the mechanism, and its Cl0p attribution is explicitly "highly likely" rather than
  confirmed, resting on three stated bases — extortion-email sender addresses matching contacts on Cl0p's
  live leak site, prior external reporting linking the same X-windchill-req header value to Cl0p, and
  consistency with the group's established mass-exploitation-then-custom-web-shell pattern. That hedge is
  carried throughout and not upgraded. BleepingComputer independently carries the victim-response half (the
  GE and Philips statements, the Philips statement having been given to Reuters) and PTC's own customer
  figures. BleepingComputer puts the leak-site batch at 43 new victims, which is not a count of
  confirmed compromises; a differing figure circulating elsewhere is carried in this store's earlier
  coverage of that batch rather than in either source cited here, so no comparison is drawn in this entry. Neither cited
  source names a Swiss or Dutch organisation in this campaign, so this entry asserts none: the store's own
  earlier coverage of that leak-site batch records that no source links those listings to the Windchill
  exploitation, and the caveat is preserved here rather than quietly dropped. ReliaQuest
  publishes file hashes and addresses which are deliberately excluded here. CVE-2026-12569's CVSS of 9.3 is
  ReliaQuest's figure. The entry deliberately states no flaw class in its body — ReliaQuest calls it a remote
  code execution flaw and BleepingComputer an improper-input-validation one, and nothing in this run's
  sources reconciles the two — so the structured record carries the impact class the primary asserts and
  the prose makes no claim about the underlying defect.
confidence: high
update_of: 2026-08-15/clop-windchill-philips-shell-first-victim-confirmations
references: []
deep_dive: true
deep_dive_category: ransomware-affiliate
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every Windchill server, review the windchill/codebase/login directory and the other codebase paths for unexpected JSP files, prioritising recent modification timestamps and any file whose content references X-windchill-req, MethodContext, WTConnection or WTKeyStoreUtil — ReliaQuest's own stated hunt criteria."
  - "On any Windchill server confirmed or suspected compromised, rotate the LDAP manager password and every other credential held in the application keystore, treat the full set as exfiltrated, and terminate existing sessions for those accounts — rotated passwords alone leave issued tokens valid."
migrated_from: null
---

**UPDATE (originally covered 2026-08-15):** the campaign's post-exploitation tooling now has a published mechanism, and it is not a generic web shell. ReliaQuest's threat research team released a reverse-engineering analysis on 2026-08-18 of the implant deployed after exploitation of CVE-2026-12569 in PTC Windchill, stating that "This activity was highly likely conducted by the Clop extortion group" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). The prior entry recorded only that JSP web shells were being deployed; what follows is the mechanism, which changes what a defender can look for.

**Background.** Cl0p's pattern is well documented over several years and is the reason a single flaw in a data-holding enterprise platform reliably becomes a mass-extortion wave rather than an isolated intrusion. ReliaQuest places this implant in a lineage: the group deployed the custom web shell DEWMODE after exploiting CVE-2021-27101, and LEMURLOOT after exploiting CVE-2023-34362 ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). BleepingComputer's account of the group's history adds the platform list those campaigns ran through — Accellion FTA, GoAnywhere MFT, SolarWinds Serv-U FTP, Cleo and MOVEit Transfer, the last of which affected more than 2,770 organisations — along with an Oracle E-Business Suite zero-day campaign from early August 2025 ([BleepingComputer, 2026-08-17](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)). Each followed the same order: pick software that stores other people's sensitive data, exploit it at scale immediately after disclosure, deploy a purpose-built shell, then extort from the stolen data rather than from encryption.

### What the implant does

The single most consequential command is a credential dump. ReliaQuest states that "A single \"S\" command to the web shell returns Windchill's directory-management and administrative credentials in plaintext" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)), implemented by an internal function the analysis calls `gs` in three steps: read Windchill's `ieStructProperties.txt` configuration file, decrypt the LDAP manager password from the application keystore, then iterate every stored local property decrypting the remaining encrypted values — administrative account credentials, object-storage credentials and all site administrator keys. Because LDAP credentials in most estates govern directory authentication for Active Directory, mail, VPN and whatever else federates against it, ReliaQuest's reading is that this turns one application compromise into an enterprise-wide credential compromise. A separate command exfiltrates the result.

Discovery is equally application-aware. A function `fl`, backed by a class the analysis names `Flst1`, queries Windchill's database for vault stream identifiers, filenames, storage paths and file sizes, writing the result to a file named `flst.txt` — a ready-made index of the repository from which the operator picks what to steal. The helper that opens that database connection uses Windchill's own internal Java classes, and this is the detection problem rather than a footnote: the implant connects through the application's `MethodContext` and `WTConnection` classes, so "its queries run under the application’s existing database identity rather than through a separately configured attacker account" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). Database telemetry attributes the theft to the application's normal service account.

The third component is what makes the shell open-ended. A custom Java class loader the analysis calls `Cldr` takes attacker-supplied code as a Base64-encoded ZIP: "It accepts a Base64-encoded ZIP file containing compiled Java bytecode, loads it directly into memory, and executes it" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). Nothing is written to disk, and the capability set is therefore not fixed at deployment — ReliaQuest notes the same channel could carry propagation tooling or file-encrypting payloads, which is a stated possibility rather than observed activity and is carried here as such.

### Why ordinary monitoring misses it

Commands travel in a custom HTTP request header, `X-windchill-req`, rather than in a URL or a request body, and responses are GZIP-compressed so the returned data looks like ordinary compressed web content. ReliaQuest is explicit about what that costs a defender: controls inspecting only URL paths or body parameters see no command traffic at all, and controls that log headers without decompressing responses "will capture the instructions but miss the data being returned". Its conclusion is a three-part requirement — "Identifying this activity requires header logging that captures non-standard values, response decompression, and TLS inspection; without all three, coverage against this web shell's traffic is partial at best" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). The analysis contrasts this with China Chopper, which it offers as the reusable-shell baseline: widely available, application-agnostic, and carrying the known patterns signature-based controls are built around. This implant carries none of them, because it behaves like the application.

### Hunting and response

The hunt has three independent footholds, and the file-system one is the cheapest. ReliaQuest's own guidance is to "Review the windchill/codebase/login directory and other Windchill codebase paths on all Windchill servers for unexpected JavaServer Pages (JSP) files that could be web shells", prioritising recent modification timestamps, unfamiliar filenames, or content referencing the `X-windchill-req` header, `MethodContext`, `WTConnection` or `WTKeyStoreUtil` ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). In web-tier telemetry, the signal is requests to Windchill carrying a non-standard request header at all — the header name is the artifact, and an estate that logs only method, path and status will not have recorded it. In file and database telemetry, the creation of `flst.txt` on a Windchill server and vault-table enumeration queries that select stream identifiers and storage paths in bulk are both discoverable, as is a large outbound transfer following shortly after.

**Triage:** every one of these signals has a benign twin on a healthy PLM server, which is why the sequence rather than any single event is the discriminator. Windchill queries its own vault tables constantly and always under the service identity, so identity is useless as a filter and volume nearly so; what does not happen normally is a bulk enumeration of stream identifiers, filenames and sizes landing in a text file in a codebase directory, followed by an outbound transfer, followed by authentication attempts elsewhere in the estate using the LDAP manager account. Likewise, JSP files legitimately live in Windchill's codebase — a recently modified one with an unfamiliar name that references the application's keystore utility class does not.

**Defender takeaway:** patch CVE-2026-12569 and restrict internet exposure of Windchill management interfaces, but treat the credential half as the part that outlives the patch. ReliaQuest's response guidance states that because the `S` command returns every encrypted value in plaintext, an operator should "assume the full set has been exfiltrated and rotate accordingly across every downstream system where those credentials are reused", and separately that "Session termination is critical because rotated passwords alone leave existing tokens valid" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)). For this constituency the exposure runs through the product estate rather than through any confirmed regional victim: neither source cited here places a Swiss or Dutch organisation in this campaign, and the store's own earlier coverage of the leak-site batch is explicit that no source links those listings to the Windchill exploitation. What is established is that named multinationals are responding — General Electric confirmed on 2026-08-17 that it is assessing Cl0p's claims while Philips said it "has identified ​and contained an attempted cybersecurity compromise of a specific enterprise server related to ⁠internal data" with no impact on customer environments ([BleepingComputer, 2026-08-17](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)). PTC states that "more than 30,000 customers globally use its products" ([BleepingComputer, 2026-08-17](https://www.bleepingcomputer.com/news/security/philips-and-ge-investigating-clop-ransomware-data-theft-claims/)), across aerospace, defence, automotive, heavy machinery, retail and medtech — and ReliaQuest "assesses with high confidence that exploitation of CVE-2026-12569 will expand to compromise more organizations in the coming weeks" ([ReliaQuest, 2026-08-18](https://reliaquest.com/blog/clop-returns-with-custom-implant-in-mass-extortion-campaign)), with copycat adoption a moderate-confidence expectation as exploit code spreads.
