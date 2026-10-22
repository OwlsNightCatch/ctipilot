P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
SW = 'https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/'
BC = 'https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/'
TH = 'https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html'
TH2 = 'https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html'
G25 = 'https://grafana.com/blog/2025/05/15/grafana-security-update-post-incident-review-for-github-workflow-vulnerability-and-whats-next/'
ENTRY = {
 'entry': '2026-05-19/grafana-labs-coinbasecartel-breach-victim-confirms-source-co',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'summary; body paragraph 1 (Pwn-Request and technical-mechanism sentences); Defender takeaway (Pwn-Request sentence)',
   'claim': 'the GitHub Pwn-Request breach ... The technical-mechanism details (`pull_request_target` workflow misconfiguration, forked-PR injection of a `curl` command, harvested write-scoped GitHub token, canary-token detection) were previously reported ... citing THN\'s earlier coverage / The Pwn-Request attack pattern is the same class of CI/CD misconfiguration',
   'defect': 'Wrong incident. The pull-request-target Action, the branch-name command injection and the canary-token alert are Grafana\'s April 2025 incident. The May 2026 breach, per Grafana\'s 2026-05-19 update, originated in the TanStack npm supply-chain attack attributed to TeamPCP, with a missed GitHub workflow token. The cited THN 2026-05-17 article carries none of these mechanism details.',
   'ground_truth': 'the breach originated from the TanStack npm supply chain attack orchestrated by TeamPCP ... and that it detected the activity on May 11, 2026. "We performed analysis and quickly rotated a significant number of GitHub workflow tokens, but a missed token led to the attackers gaining access to our GitHub repositories" (THN 2026-05-20) / On April 26, 2025, we had a security incident via an insecure GitHub Action ... utilizing pull-request-target instead of the safer pull-request (Grafana, 2025)',
   'ground_truth_url': TH2,
   'fix': 'Replace the mechanism with the May 2026 facts: access via a GitHub workflow token missed during rotation after the TanStack npm supply-chain compromise (TeamPCP), detected 2026-05-11; drop "Pwn-Request" and the pull_request_target hardening (or keep it as a general lesson citing the 2025 incident separately).',
   'class': 'factual-error'},
  {'where': 'title; headline; body paragraph 1 (material new disclosures sentence)',
   'claim': 'victim confirms source-code-only theft, no customer data / Grafana explicitly states (a) only source code was accessed',
   'defect': 'Superseded on 2026-05-19: Grafana said the downloaded content also included internal GitHub repositories with internal operational information and business contact names and email addresses. The entry has no record of this.',
   'ground_truth': '"After the initial assessment, we found that in addition to source code, the downloaded content included GitHub repositories that some Grafana Labs teams use to collaborate on and store internal operational information and other details about our business," ... "This includes business contact names and email addresses"',
   'ground_truth_url': TH2,
   'fix': 'Add an update record (2026-05-19): scope widened to internal repositories including business contact names and emails; no customer production systems or Grafana Cloud data affected.',
   'class': 'factual-error'},
  {'where': 'body Defender takeaway paragraph (first sentence)',
   'claim': 'Grafana OSS is the de facto monitoring/observability platform in EU/CH public-sector SOC and NOC environments; defenders should monitor non-official Grafana plugin updates and unsigned Grafana agent builds for the next 30 days',
   'defect': 'No source states Grafana\'s share of EU/CH public-sector SOC/NOC deployments; BleepingComputer cites Grafana\'s own figure (7,000+ organizations, 70% of the Fortune 50). The 30-day plugin/agent watch is composed.',
   'ground_truth': 'Paying customers are primarily large enterprises, cloud providers, telecos, banks, governments, e-commerce platforms, and infrastructure operators. According to Grafana, more than 7,000 organizations use the product',
   'ground_truth_url': BC,
   'fix': 'Drop the EU/CH claim or cite it; mark the monitoring advice as derived; Grafana says it audits all commits for malicious activity (THN 2026-05-20).',
   'class': 'factual-error'},
  {'where': 'title; entities; body paragraph 1 (CoinbaseCartel sentence)',
   'claim': 'Grafana Labs CoinbaseCartel breach / entities: actor:shinyhunters / CoinbaseCartel is assessed by THN as an offshoot of the ShinyHunters / Scattered Spider / LAPSUS$ ecosystem and has accumulated ~170 victims since September 2025',
   'defect': 'CoinbaseCartel\'s role is a leak-site claim (listing on 2026-05-15); THN says the breach is not attributed and Grafana speaks of an unnamed actor. The ShinyHunters link is contested: ShinyHunters told BleepingComputer CoinbaseCartel is not linked to it, so actor:shinyhunters on this entry is unsupported. Victim counts conflict (THN 170, SecurityWeek 105, BleepingComputer "more than 100").',
   'ground_truth': 'After publishing this article, the ShinyHunters extortion gang told BleepingComputer that the CoinbaseCartel is not linked to their group or ransomware operation. / The Coinbase Cartel website currently lists 105 victims. (SecurityWeek)',
   'ground_truth_url': BC,
   'fix': 'Title: Grafana Labs confirms GitHub breach claimed by CoinbaseCartel; add a Contradiction line on the ShinyHunters link and the victim count; remove actor:shinyhunters (link CoinbaseCartel and, for the origin, TeamPCP/TanStack).',
   'class': 'imprecision'},
  {'where': 'summary; body paragraph 1 (sentence 1); sourcing_note',
   'claim': 'UPDATE (originally covered 2026-W21): Grafana Labs issued an official 2026-05-18 confirmation ... previously reported in the 2026-W21 weekly summary / sourcing_note: "migration: update target unresolved ..."',
   'defect': 'Grafana confirmed on Sunday 2026-05-17 in posts on X (SecurityWeek: "confirmed suffering a data breach on Sunday"; THN 2026-05-17). The W21 weekly and "referenced 2026-05-16" are pipeline self-reference, and sourcing_note carries a migration note.',
   'ground_truth': 'Grafana confirmed suffering a data breach on Sunday, two days after a cybercrime group listed the company on its leak website.',
   'ground_truth_url': SW,
   'fix': 'Grafana confirmed the breach on 2026-05-17; remove the UPDATE/W21 framing; write a provenance sourcing_note.',
   'class': 'imprecision'},
  {'where': 'body Defender takeaway (T-id line)',
   'claim': 'MITRE T1195.002 / T1552.004 / T1567.',
   'defect': 'No source mentions private keys (T1552.004) or exfiltration over a web service (T1567); the supported behaviors are a stolen GitHub workflow token, codebase download from GitHub, a supply-chain origin and extortion.',
   'ground_truth': 'an "unauthorized party" obtained a token that granted them the ability to access the company\'s GitHub environment and download its codebase (THN 2026-05-17)',
   'ground_truth_url': TH,
   'fix': 'techniques[]: T1195.001 (TanStack npm dependency compromise), T1528 (GitHub workflow token), T1213.003 (code repositories), T1657 (extortion).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1195.001', 'behavior': 'Breach originated in the TanStack npm supply-chain attack (TeamPCP)', 'url': TH2},
   {'id': 'T1528', 'behavior': 'A GitHub workflow token missed during rotation gave access to Grafana\'s GitHub environment', 'url': TH2},
   {'id': 'T1213.003', 'behavior': 'Public and private source code and internal GitHub repositories downloaded', 'url': TH2},
   {'id': 'T1657', 'behavior': 'Extortion demand on 2026-05-16 to prevent publication; leak-site listing by CoinbaseCartel on 2026-05-15', 'url': SW},
  ],
  'note': 'Attribution of the intrusion itself is not established; CoinbaseCartel claimed it, TeamPCP is named for the upstream TanStack compromise.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'Victim statements (Grafana posts on X and its 2026-05-19 blog) relayed by SecurityWeek, BleepingComputer and THN; the victim is the only party with direct knowledge; actor links rest on third-party threat-intel assessments and are contested.'},
  'exposure': [
   {'quote': 'It said the scope of the incident is limited to the Grafana Labs GitHub environment, which includes public and private source code along with internal GitHub repositories.', 'url': TH2},
  ],
  'detection': [
   {'quote': 'Since then, Grafana has taken steps to rotate automation tokens, implement enhanced monitoring, audit all commits for signs of malicious activity, and bolster its overall GitHub security posture.', 'url': TH2},
  ],
  'triage': [],
  'takeaway': [
   {'quote': '"We performed analysis and quickly rotated a significant number of GitHub workflow tokens, but a missed token led to the attackers gaining access to our GitHub repositories," it said.', 'url': TH2},
  ],
  'bodies': [P + 'gr-sw.txt', P + 'gr-bc.txt', P + 'gr-thn.txt', P + 'gr-thn2.txt', P + 'gr-grafana-2025.txt', P + 'gr-reg.txt'],
 },
 'possible_twin_outside_batch': 'entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands (TanStack supply-chain cascade; may already carry the Grafana origin)',
}
CLAIMS = '''
04e5af457e ¦ F4 ¦ https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html ¦ superseded 2026-05-19: "in addition to source code, the downloaded content included GitHub repositories ... business contact names and email addresses"; ransom refused confirmed
cc33b4fb05 ¦ F4 ¦ https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/ ¦ confirmed "on Sunday" (2026-05-17); no source calls it a Pwn-Request breach (origin: TanStack npm attack, missed workflow token)
1eec1f3168 ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/ ¦ "breaching its GitHub environment using a stolen access token"; no pull_request_target/Pwn-Request; announcement "over the weekend"
cabc0e204d ¦ F3 ¦ https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html ¦ THN 2026-05-17 carries no pull_request_target, curl, canary or write-scoped token detail; those are Grafana's April 2025 incident
7d7e5a49d6 ¦ F5 ¦ https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/ ¦ "no personal or customer information was stolen and the incident has not impacted customer systems or operations"; ransom refused (superseded scope logged)
a36654bbf2 ¦ F5 ¦ https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html ¦ "assessed to be an offshoot of the ShinyHunters, Scattered Spider, and LAPSUS$ ecosystems ... amassed 170 victims"; SW: 105; ShinyHunters denies link (BC)
2ad6563d52 ¦ F4 ¦ https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/ ¦ no source on EU/CH public-sector SOC/NOC share; BC: "more than 7,000 organizations use the product"
45c479015b ¦ F4 ¦ https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html ¦ "the breach originated from the TanStack npm supply chain attack orchestrated by TeamPCP" (not a pull_request_target Pwn-Request)
65a5ba072e ¦ F4 ¦ https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html ¦ token used to access GitHub and download codebase; no private keys (T1552.004) or web-service exfiltration (T1567) described
'''
