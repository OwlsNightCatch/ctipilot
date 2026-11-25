---
title: Unit42-timely-threat-intel/2026-11-23-Legal-themed-vishing-activity.txt at main · PaloAltoNetworks/Unit42-timely-threat-intel
url: https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt
hostname: github.com
description: A collection of files with indicators supporting social media posts from Palo Alto Network's Unit 42 team to disseminate timely threat intelligence. - PaloAltoNetworks/Unit42-timely-threat-intel
sitename: GitHub
date: "2026-11-23"
categories: ['repository:684806858']
fingerprint: "3f00a4b40e96eaed"
language: en
image: https://opengraph.githubassets.com/40dd7092d9a94411233b45cd46c576931cbfb7d4fef372a70524968c6e6294c7/PaloAltoNetworks/Unit42-timely-threat-intel
pagetype: object
filedate: "2026-11-25"
---
Skip to content
Navigation Menu
Sign in
Products
Platform
GitHub
Repository hosting, code review, and collaboration
Copilot
AI coding agent for tasks, projects, and automated work
Build & Ship
Actions
CI/CD and automation
Code Quality
Quality analysis, fixes, and enforcement
Codespaces
Cloud development environments
Secure
Code Security
Vulnerability detection and remediation
Secret Protection
Secret scanning and leak prevention
All Features
Developers
Learn
Documentation
Training
Certifications
Build
Build with Copilot
Customize Copilot
Integrations
Explore
Trending repos
GitHub Sponsors
Developer articles
Changelog
Changelog
Your source for the latest features, improvements, and fixes across GitHub products, all in one place.
Businesses
By Stage
Enterprises
Team
Startups
Nonprofits
By Industry
Healthcare
Financial services
Manufacturing
Government
See all industries
Evaluate GitHub
Why GitHub
Customer Stories
Business insights
Trust Center
Add-ons
GitHub Advanced Security
Enterprise-grade code security
Copilot for business
Enterprise-grade AI features
Premium Support
Enterprise-grade 24/7 support
Resources
Learn & Connect
Documentation
Resource center
Blog
Events & webinars
Community Forum
Customer Stories
Integrations
Support
Customer support
Training
GitHub Status
Company
About
Partners
Changelog
GitHub Universe
GitHub Universe
The event for developers, by developers — talks, workshops, and what’s next for GitHub.
Pricing
Search
/
Sign in
Sign up
Appearance settings
You signed in with another tab or window.
Reload
to refresh your session.
You signed out in another tab or window.
Reload
to refresh your session.
You switched accounts on another tab or window.
Reload
to refresh your session.
Dismiss alert
PaloAltoNetworks
Unit42-timely-threat-intel
Repository navigation
Code
Issues
Pull requests
3
(3)
Actions
Projects
Security and quality
Insights
More
items
Files
Expand file tree
main
Breadcrumbs
Unit42-timely-threat-intel
/
2026-11-23-Legal-themed-vishing-activity.txt
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
38 lines (29 loc) · 1.28 KB
main
Breadcrumbs
Unit42-timely-threat-intel
/
2026-11-23-Legal-themed-vishing-activity.txt
Copy path
Top
File metadata and controls
Code
Blame
38 lines (29 loc) · 1.28 KB
Raw
Copy raw file
Download raw file
Open symbols panel
Edit and raw actions
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
2026-11-23 (Monday): Widespread Vishing via Legal-Themed Domains
AUTHOR:
- Matt Brady
REFERENCES:
- https://www.linkedin.com/posts/we-continue-to-track-network-infrastructure-share-7530750290657132544-FWUY/
- https://x.com/Unit42\_Intel/status/2124984598622773606
NOTES:
- The activity has been ongoing since at least October 2026.
- Many of the domains were created using NiceNIC as a registrar
-- These have Cloudflare for name servers
-- However, we have observed other providers used for both categories.
- Each domain is specifically created for an intended target using one of the following criteria:
-- Domain begins with "legal-" or ends with "-legal" using the .com TLD
-- example: legal-xyz\[.\]com or xyz-legal\[.\]com).
- We analyzed more than 70 observed domains
- The results revealed targeted organizations operating in different industries
- Based on previously observed activity, the following industries could be targeted by vishing attempts:
–- Cryptocurrency
–- Financial Services
–- Healthcare
–- High Technology
–- Hospitality
–- Media & Entertainment
–- Pharma & Life Sciences
–- Professional & Legal Services
–- Transportation & Logistics
–- Utilities & Energy
–- Wholesale & Retail
Nexus review: 3ec826cf-8807-403e-8797-6e5b1cf18802
You can’t perform that action at this time.
