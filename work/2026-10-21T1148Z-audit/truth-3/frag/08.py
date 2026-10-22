P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
SA = 'https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited'
BC = 'https://www.bleepingcomputer.com/news/security/funnel-builder-wordpress-plugin-bug-exploited-to-steal-credit-cards/'
TH = 'https://thehackernews.com/2026/05/funnel-builder-flaw-under-active.html'
CVE = 'https://cveawg.mitre.org/api/cve/CVE-2026-47100'
ENTRY = {
 'entry': '2026-05-17/funnelkit-funnel-builder-for-woocommerce-actively-exploited',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'title; headline; summary; actions[0]',
   'claim': 'actively exploited as Magecart skimmer on 40,000+ WordPress stores / Active exploitation across 40,000+ stores',
   'defect': '40,000+ is the plugin\'s install base. Sansec observed exploitation "in at least one case"; FunnelKit later reported only three compromised sites among a sample of more than 1,300 monitored.',
   'ground_truth': 'Funnel Builder by FunnelKit, a checkout and upsell plugin used on 40,000+ WooCommerce stores. ... In at least one case, Sansec found a payload posing as a Google Tag Manager loader. / FunnelKit: "During the nine days following disclosure, our monitoring covered a sample of more than 1,300 sites. Of those, only three showed signs of compromise before our mitigations took effect."',
   'ground_truth_url': SA,
   'fix': 'Sansec reports active exploitation of Funnel Builder, a plugin installed on 40,000+ WooCommerce stores; the extent of compromise is not stated (FunnelKit: 3 of 1,300+ sampled sites).',
   'class': 'factual-error'},
  {'where': 'title; headline; summary; body paragraph 1 (No CVE has been assigned); cves[]',
   'claim': 'no CVE assigned / No CVE has been assigned. / cves: []',
   'defect': 'True on 2026-05-17 per BleepingComputer and The Hacker News, false since 2026-05-19: VulnCheck published CVE-2026-47100 (reserved 2026-05-18) and Sansec\'s article, as it stands, names it.',
   'ground_truth': 'Sansec: "The flaw is tracked as CVE-2026-47100, rated 8.7 (high) on CVSS 4.0." CNA record: Funnel Builder for WooCommerce Checkout < 3.15.0.3 Missing Authorization via AJAX; CVSS 4.0 8.7 (VC:N/VI:H/VA:N), CVSS 3.1 7.5; datePublished 2026-05-19; CISA ADP SSVC Exploitation poc (2026-05-19); not in CISA KEV 2026-10-21.',
   'ground_truth_url': SA,
   'fix': 'Add cves[] CVE-2026-47100 (CVSS 4.0 8.7; affected < 3.15.0.3; fixed 3.15.0.3; missing authorization, unauthenticated) via a correction record and remove "no CVE assigned".',
   'class': 'factual-error'},
  {'where': 'evidence[0]; evidence[1]',
   'claim': '"Funnel Builder includes a publicly exposed checkout endpoint ... In at least one case, Sansec observed a payload masquerading as ... It subsequently opens a WebSocket connection to the attacker\'s command-and-control (C2) server to retrieve a skimmer ..." / "It affects all versions of the plugin before v3.15.0.3 and is used in more than 40,000 WooCommerce stores."',
   'defect': 'Neither evidence quote is a contiguous verbatim passage of The Hacker News page. Quote 1 splices two paragraphs, changes "Sansec said it observed" to "Sansec observed" and drops the C2 URL parenthetical; quote 2 reads "before 3.15.0.3. It\'s used in more than 40,000 WooCommerce stores" on the page.',
   'ground_truth': 'The vulnerability currently does not have an official CVE identifier. It affects all versions of the plugin before 3.15.0.3. It\'s used in more than 40,000 WooCommerce stores. / In at least one case, Sansec said it observed a payload masquerading as a Google Tag Manager (GTM) loader to launch JavaScript hosted on a remote domain.',
   'ground_truth_url': TH,
   'fix': 'Replace with single contiguous quotes, for example Sansec: "All versions before 3.15.0.3 let unauthenticated attackers inject arbitrary JavaScript into every checkout page on the store."',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (last sentence)',
   'claim': 'Three independent corroborating sources clear the SINGLE-SOURCE rule.',
   'defect': 'BleepingComputer and The Hacker News both attribute the activity to Sansec ("Sansec detected the malicious activity", "Per Sansec"); they are restatements, not independent corroboration. The sentence is also pipeline self-reference.',
   'ground_truth': 'BleepingComputer: "E-commerce security company Sansec detected the malicious activity"; THN: "Details of the activity were published by Sansec this week."',
   'ground_truth_url': BC,
   'fix': 'Delete the sentence; the vendor advisory relayed by Sansec and BleepingComputer is the second party.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (Why it matters; detection sentence); actions[0]',
   'claim': 'The WebSocket-to-attacker-C2 channel makes the skimmer payload polymorphic per victim ... alert on any WebSocket (`wss://`) connection initiated from a WordPress PHP process ... audit `wp_options` for unrecognised `funnel-builder` external-script entries / Swiss/EU cantonal e-service portals, healthcare patient-payment systems, and university e-commerce instances running WooCommerce are exposed without operator action / increasingly common across WordPress commerce plugins',
   'defect': 'The sources say the skimmer is "tailored to the victim store", not polymorphic. The WebSocket is opened by the injected loader script running in the shopper\'s browser, not by a WordPress PHP process. No source names the wp_options key, Swiss/EU/healthcare/university exposure or a trend; Sansec says many stores were patched automatically through WordPress.org without manual action.',
   'ground_truth': 'On page load, the script decodes the base64 string at the end and loads it as an external script ... That loader opens a WebSocket to the attacker\'s C2 ... which streams back a skimmer tailored to the victim store. / Worked with the WordPress.org plugin team to push the patch to older release branches automatically, so many stores were updated without manual action.',
   'ground_truth_url': SA,
   'fix': 'Detection: review Settings > Checkout > External Scripts for unfamiliar entries and watch checkout pages for scripts loading from unfamiliar hosts or opening a WebSocket in the browser. Drop the polymorphic, PHP-process, wp_options and Swiss/EU exposure claims.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (vulnerable-component sentence; T1505.003 sentence)',
   'claim': 'a publicly-exposed POST endpoint for checkout-funnel session management ... Mapped to `T1190` ... + `T1505.003` Web-Shell-equivalent (Magecart variant).',
   'defect': 'The sources say "public checkout endpoint that lets the request pick which internal method to run"; "POST" and "session management" are not stated. T1505.003 (Web Shell) does not describe injecting a script into a plugin setting.',
   'ground_truth': 'Funnel Builder includes a public checkout endpoint that lets the request pick which internal method to run. Older releases never check the caller\'s permissions or restrict which methods are allowed.',
   'ground_truth_url': SA,
   'fix': 'Describe the endpoint as Sansec does (public checkout endpoint, no capability check, no method allow-list); remove T1505.003; map T1190, T1059.007, T1036.005, T1071.001, T1056.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (status); tags',
   'claim': 'actively-exploited (tag); present-tense exploitation throughout',
   'defect': 'The Hacker News updated its story on 2026-05-31: FunnelKit says the fix was backported to all earlier versions, WordPress.org auto-updated installs and attacker domains were DNS-blocked, and the story reflects that the vulnerability is no longer actively exploited. The entry has no changelog record for this.',
   'ground_truth': '"The vulnerability has been patched and the active exploitation path has been closed," FunnelKit said in a statement. (The story was updated after publication on May 31, 2026 ... to reflect the fact that the vulnerability is no longer actively exploited.)',
   'ground_truth_url': TH,
   'fix': 'Add an update/correction record with the vendor statement (auto-update, backport, 3 of 1,300+ sampled sites compromised, no longer actively exploited as of 2026-05-31).',
   'class': 'imprecision'},
  {'where': 'body paragraph 1; actions[0]',
   'claim': '**Why it matters to us:** ... Reference: § 1 FunnelKit item.',
   'defect': 'Pipeline self-reference ("to us", "§ 1 FunnelKit item") in reader text; clauses after sentence 1 carry no inline citation although they are Sansec, BleepingComputer or THN facts; composed hardening ("deploy a server-side malware scanner against the plugin install path", Sansec recommends its own eComscan) is not sourced.',
   'ground_truth': 'FunnelKit advisory via Sansec: "Update FunnelKit plugins to the latest version from your WordPress dashboard. ... review your Settings > Checkout > External Scripts (or other script settings) & remove any script that looks unfamiliar."',
   'ground_truth_url': SA,
   'fix': 'Cite Sansec for each clause; keep the two vendor-advised steps; drop the self-references.',
   'class': 'imprecision'},
  {'where': 'priority',
   'claim': 'priority: high',
   'defect': '(low confidence) Actively exploited, but patched within 36 hours, auto-updated through WordPress.org, observed compromise limited, and no source shows a Swiss or public-sector exposure (the only nexus claim is unsupported).',
   'ground_truth': 'FunnelKit: "Released a fix within 36 hours ... push the patch to older release branches automatically"',
   'ground_truth_url': SA,
   'fix': 'Consider notable absent a shown constituency exposure.',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1190', 'behavior': 'Unauthenticated request to the plugin\'s public checkout endpoint invokes an internal method that writes the plugin\'s global External Scripts setting', 'url': SA},
   {'id': 'T1059.007', 'behavior': 'Injected script in the External Scripts setting executes on every checkout page', 'url': SA},
   {'id': 'T1036.005', 'behavior': 'Payload disguised as a Google Tag Manager / Analytics loader placed next to the store\'s legitimate tags', 'url': SA},
   {'id': 'T1071.001', 'behavior': 'Loader opens a WebSocket to attacker C2 that streams back a store-specific skimmer', 'url': SA},
   {'id': 'T1056', 'behavior': 'Skimmer steals credit card numbers, CVVs and billing addresses entered at checkout', 'url': SA},
  ],
  'note': 'Attackers reach the endpoint directly (no phishing stage); the skimmer runs in shoppers\' browsers.',
  'cve_facts': {'CVE-2026-47100': {'product': 'Funnel Builder for WooCommerce Checkout (FunnelKit)', 'flaw': 'missing authorization via AJAX (CWE not stated), unauthenticated write to External Scripts setting', 'affected': '< 3.15.0.3', 'fixed': '3.15.0.3', 'cvss_4_0': '8.7 (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:H/VA:N/SC:N/SI:N/SA:N)', 'cvss_3_1': '7.5', 'cna': 'VulnCheck, published 2026-05-19T14:00Z', 'ssvc': 'Exploitation poc (CISA ADP 2026-05-19)', 'kev': 'not in CISA KEV 2026-10-21'}},
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Sansec is a specialist e-commerce security firm reporting its own observation; the vendor advisory it relays confirms the injection issue; BleepingComputer and THN restate Sansec. One observing assessor plus the vendor confirmation.'},
  'exposure': [
   {'quote': 'All versions before 3.15.0.3 let unauthenticated attackers inject arbitrary JavaScript into every checkout page on the store.', 'url': SA},
   {'quote': 'Funnel Builder by FunnelKit, a checkout and upsell plugin used on 40,000+ WooCommerce stores.', 'url': SA},
  ],
  'detection': [
   {'quote': 'Attackers are planting fake Google Tag Manager scripts into the plugin\'s "External Scripts" setting. The injected code looks like ordinary analytics next to the store\'s real tags, but loads a payment skimmer', 'url': SA},
   {'quote': 'Take a moment to review your Settings > Checkout > External Scripts (or other script settings) & remove any script that looks unfamiliar.', 'url': SA},
  ],
  'triage': [],
  'takeaway': [
   {'quote': 'Update FunnelKit plugins to the latest version from your WordPress dashboard.', 'url': SA},
   {'quote': 'Stores running version 3.15.0.3 or later, including those automatically updated through WordPress.org, are no longer vulnerable to this issue', 'url': TH},
  ],
  'bodies': [P + 'fk-sansec.txt', P + 'fk-bc.txt', P + 'fk-thn.txt', P + 'fk-cverecord-47100.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
88327176e4 ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ "a checkout and upsell plugin used on 40,000+ WooCommerce stores" (install base); "In at least one case"; Sansec now: "tracked as CVE-2026-47100"
8ec589deb4 ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ install base 40,000+, not 40,000+ exploited; "no CVE assigned" stale (CVE-2026-47100, 2026-05-19); "POST" not stated; fixed 3.15.0.3 confirmed
febb5fed5f ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ exploitation seen "in at least one case"; skimmer "tailored to the victim store" (not polymorphic); update to 3.15.0.3 and review External Scripts confirmed
4772940f26 ¦ ok ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ Sansec published May 14, 2026; BleepingComputer 2026-05-15; THN 2026-05-16; "Sansec is tracking active attacks against Funnel Builder"
53bbb7ce66 ¦ F4 ¦ https://thehackernews.com/2026/05/funnel-builder-flaw-under-active.html ¦ quote verbatim ("Per Sansec, Funnel Builder includes a publicly exposed checkout endpoint ... run"); "POST" and "checkout-funnel session management" not in any source
d91b301256 ¦ F5 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ An unauthenticated request can therefore reach the internal method that writes attacker-controlled data straight into the plugin's global settings ... External Scripts ... every Funnel Builder checkout page
c4dac791df ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ injected script in External Scripts setting; no web shell described (T1505.003 does not fit)
9f97b3e0e7 ¦ F5 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ In at least one case, Sansec found a payload posing as a Google Tag Manager loader ... opens a WebSocket to the attacker's C2 ... streams back a skimmer tailored to the victim store ... steals credit card numbers, CVVs, billing addresses
53a6304cb6 ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ true on 2026-05-17 (BC, THN) but stale: "The flaw is tracked as CVE-2026-47100, rated 8.7 (high) on CVSS 4.0" (CNA published 2026-05-19)
cef4725b02 ¦ F5 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ All versions before 3.15.0.3 let unauthenticated attackers inject arbitrary JavaScript into every checkout page
41dcc16c61 ¦ F4 ¦ null ¦ no fetched source states a trend, Swiss/EU cantonal, healthcare or university exposure; Sansec: many stores were updated without manual action
72c6d9588c ¦ F4 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ "That loader opens a WebSocket to the attacker's C2" (browser-side loader, not a PHP process); skimmer "tailored to the victim store" not polymorphic; wp_options not mentioned
2980da667a ¦ F5 ¦ https://sansec.io/research/funnelkit-woocommerce-vulnerability-exploited ¦ FunnelKit advisory: update to latest and review Settings > Checkout > External Scripts; server-side scanner advice not in source (Sansec recommends eComscan)
70408de4f5 ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/funnel-builder-wordpress-plugin-bug-exploited-to-steal-credit-cards/ ¦ BC: "E-commerce security company Sansec detected the malicious activity"; THN: "Details ... published by Sansec" (restatements, not independent)
'''
