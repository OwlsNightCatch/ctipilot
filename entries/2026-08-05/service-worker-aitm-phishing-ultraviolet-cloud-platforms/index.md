---
schema: 1
kind: threat
title: "Phishing kits are registering browser service workers to build in-page transparent proxies — relaying credentials and live MFA codes from a fake browser window on trusted cloud hosting"
headline: "A service worker turns the victim's own browser into the adversary-in-the-middle proxy, on hosting you cannot block"
summary: >
  Kaspersky documents a three-stage adversary-in-the-middle phishing chain assembled entirely on
  legitimate serverless and CDN platforms. After a fake CAPTCHA step, the page registers a malicious
  browser service worker that deploys the open-source Ultraviolet proxy library to rewrite every link
  and form so subsequent traffic routes through attacker infrastructure; a fake browser window rendered
  inside the page then presents a real login flow tunnelled through that proxy, relaying the password
  and the live MFA response to the genuine service. Kaspersky's 12-month telemetry spans Cloudflare
  Pages, Vercel, GitHub Pages, IPFS gateways and Netlify — shared hosting defenders cannot block by
  parent domain without collateral damage.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-08-04"
run_id: 2026-08-05T0412Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global, europe]
sectors: [public-sector, finance, telco]
entities: [tool:ultraviolet-proxy]
techniques: [T1566.002, T1557, T1539]
affected_products: ["Cloudflare Pages", "Vercel", "Netlify", "GitHub Pages"]
cves: []
sources:
  - url: "https://securelist.com/cloud-platforms-in-phishing/120832/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-08-04"
    role: primary
closed_sources: []
evidence:
  - quote: "As this type of script was designed as a core component of progressive web apps (PWAs) to optimize load times and support offline functionality, browsers treat service workers as standard site feature and execute them without prompting for user consent as long as the website uses an HTTPS connection."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "Security teams cannot simply block the parent domain or its subdomains without inflicting collateral damage on bona fide users – a limitation that malicious actors take advantage of."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "BitB attacks operate by rendering a block inside a legitimate webpage that visually mimics a native browser pop-up window."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: "Single-source: Kaspersky GReAT is the only party publishing this chain's mechanics and its platform-abuse telemetry. The underlying technique classes — adversary-in-the-middle relay and browser-in-the-browser spoofing — are separately established in prior public reporting, but the service-worker/Ultraviolet construction and the distribution figures are Kaspersky's own analysis and are uncorroborated."
confidence: medium
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

Kaspersky has published the mechanics of an adversary-in-the-middle phishing chain that differs from the hosted-reverse-proxy kits defenders are used to in one important respect: the proxy runs inside the victim's own browser ([Kaspersky Securelist, 2026-08-04](https://securelist.com/cloud-platforms-in-phishing/120832/)). The lure arrives as a link to a fake CAPTCHA page on a compromised site, with the target's email address carried in the URL fragment — the portion a browser never transmits in the request, which keeps it out of server-side and proxy URL inspection. Completing the CAPTCHA is what triggers the real payload: the page registers a malicious service worker, and that worker deploys Ultraviolet, an open-source web-proxy library, to rewrite the links and forms of everything the user sees afterwards so all subsequent traffic is relayed through attacker infrastructure.

The choice of a service worker is the load-bearing evasion. Kaspersky notes that because this type of script was designed as a core component of progressive web apps, to optimise load times and support offline functionality, browsers treat service workers as a standard site feature and execute them without prompting for user consent so long as the site is served over HTTPS ([Kaspersky Securelist, 2026-08-04](https://securelist.com/cloud-platforms-in-phishing/120832/)) — there is no prompt, no warning surface, and no signal that distinguishes a hostile registration from a legitimate one at the moment it happens.

The final stage renders a fake browser pop-up window inside the page — an element styled to look like a native operating-system window — displaying a genuine login flow tunnelled through the in-page proxy. The victim's password and their live multi-factor response are both relayed to the real service as they are entered, which is what defeats one-time-code and push-approval factors: the attacker is not stealing a reusable secret, they are borrowing a valid authentication in real time. Kaspersky describes the technique as rendering a block inside a legitimate webpage that visually mimics a native browser pop-up window ([Kaspersky Securelist, 2026-08-04](https://securelist.com/cloud-platforms-in-phishing/120832/)) — the convincing address bar is a picture inside the page, and the browser's real one still shows the attacker's domain.

**The hosting choice is deliberate and it constrains the response.** Kaspersky's telemetry from August 2025 to July 2026 covers pages served from Cloudflare Pages, Vercel, GitHub Pages, IPFS gateways and Netlify, and states plainly that security teams cannot simply block the parent domain or its subdomains without inflicting collateral damage on bona fide users — a limitation it says malicious actors take advantage of ([Kaspersky Securelist, 2026-08-04](https://securelist.com/cloud-platforms-in-phishing/120832/)). Domain-reputation and parent-domain blocking, the two cheapest controls, are both unavailable here by construction.

Detection concepts, telemetry class first. Two hooks survive the constant rotation of hosting subdomains, because both are properties of the mechanism rather than of the infrastructure. The first is service-worker registration on an origin with no legitimate reason to have one, visible through browser-managed telemetry, endpoint browser-extension data or a proxy that inspects service-worker script responses. The second is the identity side: an authentication that completes normally but whose session characteristics — client address, network path, or the interval between the credential and the second factor — do not match the user's device, because the request the identity provider sees originates from the relay rather than the person.

**Triage:** progressive web apps register service workers legitimately and constantly, so registration alone is noise. The discriminator is the origin: a service worker registering on a freshly-created subdomain of a hosting platform, in the same page flow as a credential prompt for an unrelated service, is the pattern; a service worker on an application the organisation actually deploys is not.

**Defender takeaway:** this chain relays rather than steals, so any factor whose response can be replayed by a proxy — one-time codes, push approvals, telephone verification — provides no protection against it. Origin-bound authentication is the control that does not degrade, because the credential is cryptographically tied to the domain in the address bar and the proxy cannot forward it to a domain it does not control. For an estate that has deployed phishing-resistant factors for administrators but left the general population on codes and push prompts, this is the tradecraft that exploits the difference.
