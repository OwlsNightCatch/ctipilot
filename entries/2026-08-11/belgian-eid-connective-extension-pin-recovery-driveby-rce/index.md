---
schema: 1
kind: research
title: "Belgium's eID signing extension handed any web page the card, the PIN and a drive-by RCE — an eIDAS Qualified Trust Service Provider's browser bridge that never checked the caller's origin"
headline: "An eIDAS-qualified eID browser bridge let any website read the card, recover the PIN and load an arbitrary DLL"
summary: >
  Bay Area Labs disclosed three chained flaws in Connective, the browser extension and native host from Nitro Software
  Belgium that lets web pages talk to Belgian eID and Maestro smart cards for authentication and eIDAS qualified
  signatures, and which the researchers say is used by 8 of Belgium's 10 largest banks and 60+ government agencies
  across a 2-million-user install base. Because the extension never forwarded the calling page's origin to the native
  host, any site or hidden iframe could replay a signed activation token and drive the card; the PIN token handed back
  to the page carried both the ciphertext and its own AES key with a hardcoded IV, so the eID PIN could be recovered
  outright; and a reader-enumeration command accepted a relative library path, turning a single site visit into
  arbitrary DLL execution. No CVE has been assigned, and the vendor took 146 days from first report to complete fix,
  shipping an incomplete one in between.
discovered_at: "2026-08-11T04:40:00Z"
event_date: "2026-08-07"
run_id: 2026-08-11T0411Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, identity, rce, pre-auth, supply-chain, info-disclosure]
regions: [europe]
sectors: [public-sector, finance]
entities: []
techniques: [T1189, T1129, T1056.002, T1111]
affected_products: ["Nitro Software Belgium Connective Signing Extension"]
cves: []
sources:
  - url: "https://amibeingpwned.com/blog/8-in-10-banks-in-belgium"
    publisher: "James Arnott, Bay Area Labs"
    date: "2026-08-07"
    role: primary
  - url: "https://www.securityweek.com/critical-flaws-discovered-in-belgian-eid-software-used-by-2-million-people/"
    publisher: "SecurityWeek"
    date: "2026-08-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "That means any web page can just replay these tokens and get full access to the Connective system on the user's machine."
    publisher: "James Arnott, Bay Area Labs"
  - quote: "having the PIN plus the ability to send commands to the card is the same thing as having the card in your hand, with a wider blast radius since it works from an iframe"
    publisher: "James Arnott, Bay Area Labs"
  - quote: "There were also no security-adverse actions required from the user to enable this drive-by RCE, they simply needed to visit a website with the Connective signing extension and native host installed."
    publisher: "James Arnott, Bay Area Labs"
verification: multi-source
sourcing_note: "The technical detail is the discovering researchers' own write-up; SecurityWeek independently reported the disclosure three days later. No vendor advisory and no CVE identifier was located for this software in this run."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Connective is the browser extension plus native host that lets Belgian web services talk to the smart card in the reader — the national eID and Maestro payment cards — to authenticate users and produce eIDAS *qualified* electronic signatures, the tier that carries the same legal weight as a wet signature. Its vendor, Nitro Software Belgium, sits on the EU eIDAS Trusted List as a Qualified Trust Service Provider, the highest trust tier the regulation defines ([Bay Area Labs, 2026-08-07](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium)). The researchers cite the vendor's own marketing for the deployment figures — "8 of the 10 largest banks in Belgium and 60+ Belgian government agencies and departments" — and say they independently confirmed the 2-million weekly-active-user count from the Chrome and Edge store listings; SecurityWeek, reporting the disclosure on 2026-08-10, put the affected population at roughly two million people ([SecurityWeek, 2026-08-10](https://www.securityweek.com/critical-flaws-discovered-in-belgian-eid-software-used-by-2-million-people/)).

The root defect is a missing trust boundary rather than a memory-safety bug: the extension forwards messages from web pages to the native host without telling the host which page sent them, so the component holding the card has no way to know who it is talking to ([Bay Area Labs, 2026-08-07](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium)). The one gate that existed, an RSA-signed `activationToken` issued by partner sites, decodes to a UUID, a time-to-live and a feature bitmask — and carries no origin either, so any page can replay a token harvested from a legitimate site and reach every card command it enables. The researchers took theirs from a live Belgian service whose tokens allowed all operations with a 24-hour lifetime.

From there the second flaw hands over the secret the whole scheme rests on. When a user types their PIN into the native Connective dialog, the host returns a `pinToken` to the calling page — and the researchers found that token is a 48-byte blob containing both the ciphertext *and* the AES-128 key needed to decrypt it, alternating bytes of the first 32, with a hardcoded initialisation vector recovered from the binary; decrypting it yields the PIN digits plus an expiry ([Bay Area Labs, 2026-08-07](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium)). Worse for the social-engineering step, the page controls the dialog's title and body text, so the prompt asking for the PIN can be made to read as an official identity confirmation while being driven by an advertisement in an invisible frame. With the PIN in hand the attacker can mint their own PIN tokens and keep using the card whenever it is in the reader. The researchers demonstrated an account takeover against a Belgian federal authentication portal on this path, and are explicit about what they did *not* test: they did not exercise the flow against the country's dominant identity app itself, and note there may be further steps involved.

The third flaw is the one the researchers call the most impactful. The reader-enumeration command accepts a `library` parameter naming a DLL to load, relative paths included, with the only constraint that the path contains `.dll` ([Bay Area Labs, 2026-08-07](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium)). Because the browser blocks downloads with a bare `.dll` extension, they used a polyglot file whose name embeds the string inside an innocuous-looking document name, had the page download it automatically, and then walked a relative path from the extension's own directory under the user profile back into the downloads folder — arbitrary code execution at user privilege, out of the browser sandbox, from a page visit. They note there was nothing preventing it from spreading by stealing session material and messaging the link onward to other users of the same extension.

Remediation took 146 days from first report, and the interim state is the part worth studying: the first fix, on 2026-05-08, added a remote origin check, which the researchers point out meant only approved sites could still trigger the RCE or steal the PIN token; they told the vendor the same month that the library command was untouched and the PIN token was still reaching web pages. The complete fix landed on 2026-06-01 by disabling the library command and replacing the PIN token with a randomly generated identifier cached inside the extension, with the remote origin checks fully enforced from 2026-07-22 ([Bay Area Labs, 2026-08-07](https://amibeingpwned.com/blog/8-in-10-banks-in-belgium)). No CVE was assigned, and this run located no vendor advisory. The researchers also observe that the vendor advertises yearly penetration tests.

**Defender takeaway:** the pattern generalises well beyond one Belgian vendor, and that is why it matters to a Swiss or European public-sector defender who has never heard of Connective. Any smart-card, eID or qualified-signature browser bridge follows the same architecture — a thin extension relaying messages from arbitrary web content to a privileged native host that holds a cryptographic device — and the security of the whole arrangement rests on the host knowing which origin is calling it. Where such software is deployed on managed estates, or accepted from counterparties in cross-border signing workflows, the questions that separate a safe implementation from this one are answerable without source access: does the native host receive and enforce the caller's origin, does any secret derived from user input ever cross back into page context, and can the page influence what the host loads or executes. Note also what a compromise of this class costs downstream — a forged qualified signature shifts the burden of proof onto the person whose card was used, and being a Qualified Trust Service Provider on the eIDAS Trusted List was not, here, evidence that any of these questions had been asked.

**Triage:** on an endpoint, the observable is a signing or smart-card native-messaging host process spawning or loading code that did not ship with it — in process-creation and image-load telemetry with parent lineage, a browser-installed helper under the user profile loading a library from a user-writable location such as the downloads directory, rather than from its own install path. Legitimate use of these bridges loads only the vendor's own modules and the platform smart-card libraries from fixed paths, so the discriminator is the load *source*, not the load itself.
