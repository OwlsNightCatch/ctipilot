---
schema: 1
kind: threat
horizon: operational
title: "JWR: a phishing kit that streams keystrokes to a live operator over an encrypted WebSocket, so the criminal decides what page to show next before the victim presses submit"
headline: "Talos dissects an operator-driven checkout-impersonation kit with 44 pages, 40-plus remote instructions and a long-poll fallback"
summary: >
  Cisco Talos published an analysis on 2026-08-13 of JWR, an undocumented phishing framework impersonating Shopify,
  PayPal, Apple, Klarna and bank checkout and login flows. Rather than logging a form submission, the client holds an
  AES-CTR-encrypted WebSocket open to the operator for the whole session and streams the victim's keystrokes as they
  are typed, while the operator drives the victim between 44 pages using more than 40 instructions — including one
  that fakes a declined card to harvest a second one, and one that injects an operator-supplied one-time code.
  Everything collected is POSTed to the server only when the operator closes the session. Talos assesses with medium
  confidence that JWR is a variant of The Outsider, the phishing-as-a-service platform an FBI-led operation took down
  in June 2026, and observed delivery through toll, postal and courier SMS lures across Southeast Asia and the UAE.
discovered_at: "2026-08-14T05:04:00Z"
event_date: "2026-08-13"
run_id: 2026-08-14T0417Z-intel
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
  - organized-crime
  - cryptocrime
regions:
  - apac
  - middle-east
  - global
sectors:
  - finance
  - retail
entities:
  - tool:jwr-phishing-framework
  - campaign:outsider-phaas-gemini-2026
techniques:
  - T1566
  - T1111
  - T1071.001
  - T1056.001
  - T1027
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/"
    publisher: "Cisco Talos"
    date: "2026-08-13"
    role: primary
closed_sources: []
evidence:
  - quote: "The client engine of the JWR phishing framework is a real-time, operator-driven system that, rather than merely logging form submissions like a static credential-stealing page, keeps an AES-CTR encrypted WebSocket open to the threat actor so they can steer each victim's session live."
    publisher: "Cisco Talos"
  - quote: "The victim data targeted by the actor using JWR extends well beyond payment data, encompassing identity documents, Social Security numbers, passport and driver's license images, website and PayPal credentials, 2FA codes, and full device fingerprints, all committed to the actor's server once a session ends."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Cisco Talos is the sole source: this is its own first-hand reverse-engineering of the client engine, and no independent analysis was found this run. Single-source under the standard rule rather than a carve-out — Talos is a research lab, not a national authority — so the technical detail carries the weight of one assessor."
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

Cisco Talos published a teardown on 2026-08-13 of a phishing framework its developer brands **JWR**, built to impersonate checkout and login flows for Shopify, PayPal, Apple, Klarna and unnamed banks. The architectural point is the one that matters: ["The client engine of the JWR phishing framework is a real-time, operator-driven system that, rather than merely logging form submissions like a static credential-stealing page, keeps an AES-CTR encrypted WebSocket open to the threat actor so they can steer each victim's session live"](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/). The client splits into a host-bridge module that relays commands into a child iframe carrying the actual phishing form, and a Vue.js application that renders across 44 pages, streams keystrokes to the server as they are typed, and executes more than 40 distinct instructions issued from the operator's console.

**The session is a conversation, not a form.** Talos reconstructs the card-theft flow step by step. The victim's arrival fires a beacon that puts a live "new visitor" entry on the operator's console before any instruction is sent, reporting the landing page, the referring storefront and device metadata. The operator sends the victim to a personal-details page and simply watches the stream while they type; once satisfied, moves them to the card page and watches the card number arrive digit by digit. If the operator does not like what they see, an instruction delivers a fake "card declined" message and returns the victim to the card page to try another — a loop the operator can repeat as often as they want, each pass aimed at a further card from the same person. If the card is accepted, the operator routes the victim to an SMS, 2FA, PIN or in-app verification page to capture the one-time code, sends the same fake-failure instruction if the code is rejected, and finally redirects the victim to the genuine website. Only when the operator closes the session is the accumulated record — full card data, PIN, expiry, national identity number, passport or driving-licence images, up to three sets of website credentials, PayPal login and a device fingerprint — POSTed to the server in one call. A separate REST endpoint provides an HTTP long-poll fallback delivering the same operator instructions when a persistent WebSocket is unavailable or blocked, so network-level blocking of WebSockets degrades the operator's channel rather than closing it.

**Provenance and campaign.** Talos found the client engine shares significant code and functional similarity with the client of The Outsider, a phishing-as-a-service platform run by a Chinese-speaking actor, and [assesses with medium confidence that JWR is a variant of The Outsider, based on several similarities in the client engine scripts and functionalities of the two platforms](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/). It notes that an FBI-led takedown operation moved against the Outsider platform in June 2026, but that the kit had been sold as a self-service product through the actor's Telegram channels — which is the mechanism by which a disrupted platform reappears as somebody else's framework. The operator-facing status strings are hardcoded in Simplified Chinese and read as an admin dashboard feed. The observed campaign is smishing at scale rather than targeted: unpaid road-toll and road-pricing lures impersonating a national land transport authority in Singapore, parcel-and-customs-fee lures impersonating a national postal service, a smaller cluster mimicking an electronic toll system in the UAE, and a regional courier brand used across several Southeast Asian countries. Talos published detection coverage for its own products alongside the analysis.

**Defender takeaway:** the reason this matters outside the observed geography is that it breaks a common detection assumption. Controls built around form submission — watching for credentials leaving a page, or for a POST to a suspicious endpoint — see nothing until the operator ends the session, by which point the card, the identity documents and the one-time code have all already been read. The durable hooks are the transport and the shape of the page: a persistent WebSocket opened from a page that presents itself as a payment checkout, an HTTP long-poll loop against the same origin where WebSockets are blocked, and a session in which a background worker keeps a connection alive across navigation within the same site. Operator-driven relay also defeats the reflex that a one-time code is a safe second factor: the code is requested from the genuine service and re-presented to the victim on the operator's cue, so the only controls that survive are phishing-resistant authenticators bound to the origin, and, on the fraud side, the pattern of a single cardholder presenting several cards in one session after repeated declines.

**Triage:** a persistent WebSocket is not by itself suspicious — real checkout and support pages use them. The discriminators are the combination Talos describes: a WebSocket or long-poll channel from a page that renders a payment or login flow the organisation does not operate, on a domain reached from an SMS link, with the visible brand and the connection destination disagreeing. On the victim-support side, the tell that separates this from a static phishing page is the narrative the victim reports: being told a card was declined and asked for another, or being asked for a one-time code more than once, means an operator was present in real time and the exposure includes everything typed, not just what was submitted.
