<!DOCTYPE html>
<html lang="en">
<head>
        <!-- Meta Data -->
    <meta charset="UTF-8">
    <meta content="text/html; charset=UTF-8" http-equiv="Content-Type"/>
    <meta content="IE=edge" http-equiv="X-UA-Compatible">
    <meta content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" name="viewport">
    <link href="/favicon.ico" rel="apple-touch-icon" sizes="180x180">
    <link href="/favicon.ico" rel="icon" sizes="32x32" type="image/png">
    <link href="/favicon.ico" rel="icon" sizes="16x16" type="image/png">

    <!-- Site Stylesheet -->
    <link href="/files/css/styles.min.css?v=1.0" rel="stylesheet">
    <link href="//fonts.googleapis.com" rel="preconnect">
    <link crossorigin href="//fonts.gstatic.com" rel="preconnect">
    <link href="//fonts.googleapis.com/css2?family=Barlow:wght@200;300;400;500;600&display=swap" rel="stylesheet">
    <!--Basic meta information-->
    <title>CERT-EU - From Penetration Testing to Cyber Threat: Beware of ARTEX</title>
    <meta content="CERT-EU - In recent weeks, CERT-EU has observed several threat actors around the world that have used ARTEX, an AI-powered penetration-testing framework, to automate their campaigns." name="description">
    <meta content="CERT-EU - cert-eu, ARTEX" name="keywords">

    <!--Share information-->
    <meta property="og:title" content="From Penetration Testing to Cyber Threat: Beware of ARTEX">
    <meta property="og:description" content="In recent weeks, CERT-EU has observed several threat actors around the world that have used ARTEX, an AI-powered penetration-testing framework, to automate their campaigns.">
    <meta property="og:url" content="https://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex">
    <meta property="og:image" content="https://cert.europa.eu/files/images/certeu_home_share-v2.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="600">

    <style nonce="WG4TW_p3mEHskCivAl9aNMMV5SovH9sD">
        .tlp_red {
            padding: 0 3px;
            background-color: #000;
            color: #FF2B2B;
            font-weight: 600;
            line-height: 1.4em;
        }

        .tlp_amber,
        .tlp_amber_strict {
            padding: 0 3px;
            background-color: #000;
            color: #FFC000;
            font-weight: 600;
            line-height: 1.4em;
        }

        .tlp_green {
            padding: 0 3px;
            background-color: #000;
            color: #33FF00;
            font-weight: 600;
            line-height: 1.4em;
        }

        .tlp_clear,
        .tlp_white {
            padding: 0 3px;
            background-color: #000;
            color: #FFFFFF;
            font-weight: 600;
            line-height: 1.4em;
        }
    </style>
</head>
<body>
<header class="header_website--not_scrolled">
    <section class="header_website_top d-flex justify-content-between px-15">
        <div class="header_website_top--social d-flex align-items-center">
            <a href="https://www.linkedin.com/company/certeu/mycompany/" target="_blank"
               class="header_website_top--social--icon">
                <span class="share-xs share-icon-linkedin-white m-2"></span>
            </a>
            <a href="https://github.com/certeu" target="_blank" class="header_website_top--social--icon">
                <span class="share-sm share-icon-github-white"></span>
            </a>
            <a href="https://infosec.exchange/@cert_eu" target="_blank"
               class="header_website_top--social--icon" rel="me">
                <span class="share-sm share-icon-mastodon-white"></span>
            </a>
        </div>
        <div class="d-flex">
            <a class="header_website_top--right mt-5 mr-40 a-norm-rev" href="//goo.gl/maps/sNEAsRwQ739XLHVz9"
               target="_blank">
                Address: Rue de la Loi 107, 1049 Brussels, Belgium
            </a>
            <a class="header_website_top--right mt-5 a-norm-rev" href="tel:+32 229 52100">Tel: +32 2 295 2100</a>
        </div>
    </section>

    <section class="d-flex flex-row px-10 header_website">
        <a href="/" class="flex-grow-1 align-self-center header_website--logo"></a>
        <input class="menu-btn" id="menu-btn" type="checkbox"/>
        <nav class="align-self-center horizontal-menu" role="navigation">
            <ul>
                <li><a class="small-caps hover-underline-animation-white" href="/about-us">About us</a></li>

                <li><a class="small-caps hover-underline-animation-orange text-orange" href="/conference">Conference</a></li>

                <li><a class="small-caps hover-underline-animation-white" href="/blog">Blog</a></li>
                <li><a class="small-caps" href="/publications">Publications</a>
                    <ul>
                        <li>
                            <a class="small-caps hover-underline-animation-blue"
                               href="/publications/security-advisories/">
                                Security advisories
                            </a>
                        </li>
                        <li>
                            <a class="small-caps hover-underline-animation-blue"
                               href="/publications/security-guidance/">
                                Security guidance
                            </a>
                        </li>
                        <li>
                            <a class="small-caps hover-underline-animation-blue"
                               href="/publications/threat-intelligence/">
                                Threat intelligence
                            </a>
                        </li>
                        <li>
                            <a class="small-caps hover-underline-animation-blue"
                               href="/publications/tlr-10-years/">
                                TLR 10 Years
                            </a>
                        </li>
                    </ul>
                </li>
                <li><a class="small-caps hover-underline-animation-white" href="/vacancies">Vacancies</a></li>
                <li>
                    <a class="small-caps hover-underline-animation-white" href="/hall-of-fame">
                        Hall of fame
                    </a>
                </li>
                <li><a class="small-caps" href="/iicb/">IICB</a></li>
                <li><a class="small-caps hover-underline-animation-white" href="/contact-us">Contact us</a></li>
            </ul>
        </nav>
        <label class="menu-icon" for="menu-btn"><span class="navicon"></span></label>
    </section>
</header>

<main>
    <section class="top_section d-flex flex-column justify-content-center">
        <h1 class="top_section--title text-center">From Penetration Testing to Cyber Threat: Beware of ARTEX</h1>
        <ul class="top_section--breadcrumb d-flex flex-row justify-content-center mt-20">
            <li><a class="a-norm" href="/">Home</a></li>
            <li><a class="a-norm" href="/blog">Blog</a></li>
            <li>Article</li>
        </ul>
    </section>

    <section class="news py-30 blog">
        <article class="container d-flex flex-column">
            <div class="d-flex justify-content-between align-items-center">
                <div class="d-flex flex-row flex-wrap">
                    <span class="mr-5 text-grey">By</span>
                    <span class="author">
                        CERT-EU 
                    </span>
                    <span class="mr-5 text-grey">, on</span>
                    <time class="text-grey"
                          datetime="2026-11-05T22:05:00+01:00">Thursday, November 05, 2026 10:05:00 PM CET</time>
                </div>
                <aside
                    class="mt-30-sm mt-40-lg justify-content-center justify-content-sm-end justify-content-lg-end align-self-end">
                    <div class="font-amender">
                        <a data-font-amender-class="font-amender-small">A</a>
                        <a data-font-amender-class="font-amender-normal" class="font-amender-selected">A</a>
                        <a data-font-amender-class="font-amender-medium">A</a>
                        <a data-font-amender-class="font-amender-big">A</a>
                    </div>
                </aside>
            </div>
            <div class="mt-30 blog--body font-amender-apply">
                <h2>Foreword</h2><p>In recent weeks, CERT-EU has observed several threat actors around the world that have used ARTEX, an AI-powered penetration-testing framework, to automate their campaigns. ARTEX rapidly identifies and exploits misconfigurations in addition to targeting traditional software vulnerabilities.</p><p>CERT-EU has observed similar instances of AI-driven activities against its constituency. These activities highly likely involved the use of ARTEX.</p><p>We assess that ARTEX’s public availability will likely accelerate adoption by threat actors, resulting in more frequent, faster, and more scalable automated attacks with a higher success rate.</p><p>In April 2026, in our blog post <a href="/blog/ai-vulnerability-discovery-defenders-must-adapt" target="_blank">AI is changing the economics of vulnerability discovery</a>, we warned that autonomous offensive capabilities would progressively reach a wider range of actors. ARTEX is a concrete example of that shift materialising.</p><p>CERT-EU is publishing this blog post to raise awareness of the widespread use of ARTEX by threat actors.</p><h2>What is ARTEX</h2><p>ARTEX is an open-source, LLM-driven autonomous penetration testing platform. It takes a security objective in natural language, decomposes it into goals and intents, and then has one or more agent workers execute reconnaissance and testing steps autonomously, within a scope defined by the operator, using real tooling rather than simulated actions.</p><p>It is designed to be observed and steered by a human operator through a dashboard covering task orchestration, traffic recording, findings, coverage and an approval queue. The tool relies on configurable rules and the model itself to respect scope and avoid destructive actions; there is no hard technical enforcement.</p><p>Following reports of misuse, the original author made the repository unavailable in October 2026. The publicly available versions are now independent forks rather than an official upstream release. ARTEX does not include its own AI model; it integrates with external LLM providers, and operators supply a compatible model of their choosing. Integrations and capabilities may differ between forks.</p><p>Its relevance to us lies in its scale, speed and persistence. ARTEX can test large numbers of low-complexity misconfigurations, including those a human tester would notice but not have time to check, and it can work through long attack chains without the fatigue that limits manual testing. The same is true of complex payload crafting. Exploitation paths that need carefully tailored payloads often take more effort than the severity of the finding justifies, so a manual assessment may leave them untested.</p><h3>Tactics, Techniques and Procedures (TTPs)</h3><p> </p><table class="table"><thead><tr><th scope="col">ATT&amp;CK ID</th><th scope="col">Technique</th></tr></thead><tbody><tr><td><a target="_blank" rel="noopener noreferrer" href="https://attack.mitre.org/techniques/T1595/">T1595</a></td><td>Active Scanning</td></tr><tr><td><a target="_blank" rel="noopener noreferrer" href="https://attack.mitre.org/techniques/T1588/002/">T1588.002</a></td><td>Obtain Capabilities: Tool</td></tr><tr><td><a target="_blank" rel="noopener noreferrer" href="https://attack.mitre.org/techniques/T1190/">T1190</a></td><td>Exploit Public-Facing Application</td></tr></tbody></table><h2>What you can do</h2><h3>Immediate</h3><ul><li data-list-item-id="e32812c0ba2651945817f35f4131f06c5">Identify internet-exposed IT assets and limit internet exposure to only those assets that require it.</li><li data-list-item-id="e9f32b6f319e2b614d7b8af6c1baba068">Ensure management and control panels are isolated from the internet or from untrusted/insecure networks.</li><li data-list-item-id="e8357793361861be995141917241c4b76">Prioritise emergency patching for all internet-exposed assets.</li><li data-list-item-id="e400303d9c9f95cd848d82b141b7502a5">Closely monitor privileged and administrator account activity to detect anomalous behaviour, unauthorised actions, and potential abuse of elevated privileges.</li></ul><h3>Short-term</h3><ul><li data-list-item-id="e32617dd94e059ba601c11aef200fcfb3">Implement Multi-Factor Authentication (MFA) across all critical systems and services to protect against account takeover and unauthorised access.</li><li data-list-item-id="ea1d118b3697a6545ed4ba5493746e389">Hunt for and alert on connections to known or suspected actor infrastructure to identify potential targeting or compromise. Hunt for artefacts and behaviours consistent with ARTEX usage (e.g. automated scanning patterns, specific tool signatures) in your organisation's logging.</li><li data-list-item-id="ef4aec0b9c2fd42043eed5605ea87f6d7">Use Endpoint Detection and Response (EDR) tools to monitor and block processes exhibiting unusual behaviour, such as privilege escalation attempts.</li></ul><h3>Continuously</h3><ul><li data-list-item-id="eda91cedcd521575ae82bb328b2116507">Sanitise error responses from internet-facing devices to minimise information disclosure and hinder adversary fingerprinting and identification of underlying technologies and infrastructure.</li><li data-list-item-id="e81f2b2adc0d1c200f9eeda67e7633e1b">Protect internet-exposed assets with a web application firewall (WAF) or equivalent security solution.</li><li data-list-item-id="eb38b25b74a727729dcc4e9d65dd2e399">Prioritise implementation of detection and logging good practices for internet-exposed assets to support security monitoring and incident response.</li><li data-list-item-id="ee590f60deaea9591d6da922408354ff1">Ensure security monitoring also covers AI tools and internet-connected assets that use AI processes.</li><li data-list-item-id="e34c12d452983d6a359a6fc38247ecbe1">Assess the security of your internet-facing devices with regular vulnerability scans, penetration tests, and trusted AI-assisted cybersecurity tools and frameworks.</li><li data-list-item-id="e3655ee88c21cc40602e7be7b98738e94">Retain all findings, including non-severe ones, in the remediation cycle to prevent AI-enabled tooling from chaining minor misconfigurations into higher-impact attack paths.</li></ul><h2>References</h2><ul><li data-list-item-id="e753bebb8487bdaf7429bc19ebe0bb242"><a target="_blank" rel="noopener noreferrer" href="https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks">https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks</a></li><li data-list-item-id="e3eac5c1929854858403bfe6fe4ced0aa"><a target="_blank" rel="noopener noreferrer" href="https://www.zscaler.com/blogs/security-research/inside-global-ai-assisted-hacking-campaign">https://www.zscaler.com/blogs/security-research/inside-global-ai-assisted-hacking-campaign</a></li><li data-list-item-id="e9d28a09673213392ecf44feee965f0d9"><a target="_blank" rel="noopener noreferrer" href="https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/">https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/</a></li><li data-list-item-id="e3596e231d94f070a0c7df22528217234"><a target="_blank" rel="noopener noreferrer" href="https://www.khan.co.kr/en/article/202610042320007">https://www.khan.co.kr/en/article/202610042320007</a></li><li data-list-item-id="e12bd37203e789d51369b5ee4026f7767"><a target="_blank" rel="noopener noreferrer" href="https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/">https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/</a></li><li data-list-item-id="eec5b86f86ccb5156eb06f17df5107483"><a target="_blank" rel="noopener noreferrer" href="https://www.yna.co.kr/view/AKR20261026075100004">https://www.yna.co.kr/view/AKR20261026075100004</a></li><li data-list-item-id="e38ebc3bd922d5a9fafb9a0f055544ef3"><a target="_blank" rel="noopener noreferrer" href="https://www.japantimes.co.jp/news/2026/10/20/japan/china-ai-cyberattacks/">https://www.japantimes.co.jp/news/2026/10/20/japan/china-ai-cyberattacks/</a></li></ul><h2>About CERT-EU</h2><p>CERT-EU is the Cybersecurity Service for the Union institutions, bodies, offices and agencies, established under <a target="_blank" rel="noopener noreferrer" href="https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202302841">Regulation (EU, Euratom) 2023/2841</a>. Under the Cybersecurity Regulation, CERT-EU acts as the central cybersecurity hub for all Union entities, providing threat intelligence, incident response coordination, vulnerability management, and security guidance. CERT-EU also supports Union entities in implementing their cybersecurity risk-management frameworks and issues calls for action to raise the collective level of cybersecurity across the EU institutional ecosystem.</p><p>CERT-EU is a member of the CSIRTs Network, the network of national Computer Security Incident Response Teams established under the NIS2 Directive (Directive (EU) 2022/2555). The CSIRTs Network facilitates operational cooperation and the exchange of cybersecurity information between EU Member States and Union entities, enabling coordinated responses to cross-border cyber incidents.</p><p>CERT-EU also maintains a structured cooperation with ENISA, the European Union Agency for Cybersecurity, as provided for under Regulation (EU) 2019/881 (the Cybersecurity Act). This cooperation covers areas such as cyber threat analysis and the sharing of threat landscape assessments.</p>
            </div>
            <div class="mt-40">
                <div class="share-title">Share this post</div>
                <ul class="mt-15 d-flex flex-row justify-content-between blog--share">
                    <li>
                        <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex"
                           target="_blank" class="share-md share-icon-linkedin-blue_dark"></a>
                    </li>
                    <li>
                        <a href="https://www.facebook.com/sharer.php?u=https://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex"
                           target="_blank" class="share-md share-icon-fb-blue_dark"></a>
                    </li>
                    <li>
                        <a href="mailto:?subject=From Penetration Testing to Cyber Threat: Beware of ARTEX&body=Hi,%0D%0DI thought the following article might be of interest to you:%0Dhttps://cert.europa.eu/blog/from-penetration-testing-to-cyber-threat-beware-of-artex%0D%0DCheers."
                           target="_blank" class="share-md share-icon-email-blue_dark"></a>
                    </li>
                </ul>
            </div>
        </article>
    </section>

        <section class="accept_cookies">
        <div class="accept_cookies--modal d-flex flex-column">
        <h2>We got cookies</h2>
            <p class="mt-30">
                We only use cookies that are necessary for the technical functioning of our website. Find out more on
                <a class="a-norm" href="/cookies-policy">here</a>.
            </p>
            <div class="align-self-end mt-auto">
                <button class="btn accept_cookies--modal--btn--accept">OK</button>
            </div>
        </div>
    </section>
        <section class="hidden" data-certeu-scrollTop=""></section>
</main>

<footer class="footer_website d-flex flex-row flex-lg-column">
    <section class="container">
        <p>
            This website is managed by CERT-EU.
        </p>
        <div class="d-flex flex-column flex-lg-row pb-lg-20 bb-0 bb-1-lg bc-200">
            <div class="mr-lg-30">
                <p class="mt-20">
                    <strong>Please send any comments or suggestions to</strong>
                    <br>
                    <a class="a-norm" href="mailto:services@cert.europa.eu">services@cert.europa.eu</a>
                </p>
                <p class="footer_website--link-sm-h">
                    <strong>The information on this site is subject to a</strong>
                    <br>
                    <a class="a-norm" href="/legal-notice">Legal notice</a>
                </p>
            </div>
            <div class="mr-lg-30">
                <p class="mt-20">
                    <strong>PGP fingerprint:</strong>
                    <br>
                    <a class="a-norm" href="/files/certs/2025-CERT-EU-PGP.asc" target="_blank">
                        152D 5B54 B526 4A3D F420 35D3 FCB2 4C57 FE5E 446A</a>
                    <br>
                    <a class="a-norm footer_website--link-sm" href="/files/certs/891D04EC_Revocation_certificate-2024.asc"
                       target="_blank">
                        revocation certificate</a>
                </p>
                <p class="mt-20">
                    <strong>Emergency phone:</strong>
                    <br>
                    <a class="a-norm" href="tel:+3222990005">+32 2 299 0005</a>
                </p>
            </div>
            <div class="ml-lg-auto footer_website--social">
                <div class="d-flex flex-row mt-20">
                    <a href="https://www.linkedin.com/company/certeu/mycompany/" target="_blank"
                       class="footer_website--social--icon">
                        <span class="share-sm share-icon-linkedin-white m-4"></span>
                    </a>
                    <a href="https://github.com/certeu" target="_blank" class="footer_website--social--icon">
                        <span class="share-md share-icon-github-white"></span>
                    </a>
                    <a href="https://infosec.exchange/@cert_eu" target="_blank"
                       class="footer_website--social--icon" rel="me">
                        <span class="share-md share-icon-mastodon-white"></span>
                    </a>
                </div>
                <p class="mt-20">
                    <strong>Address:</strong>
                    <br>
                    <a class="a-norm" href="//goo.gl/maps/sNEAsRwQ739XLHVz9" target="_blank">
                        Rue de la Loi 107<br>1049 Brussels, Belgium
                    </a>
                </p>
            </div>
        </div>
        <div class="d-flex flex-column flex-lg-row mt-20 footer_website--bottom">
            <div class="d-flex flex-column flex-lg-row mt-20 footer_website--bottom--left">
                <a class="a-norm mx-lg-10 footer_website--bottom--item" href="/cookies-policy">Cookies</a>
                <a class="a-norm mx-lg-10 footer_website--bottom--item" href="/privacy-policy">Privacy policy</a>
                <a class="a-norm mx-lg-10 footer_website--bottom--item"
                   href="/coordinated-vulnerability-disclosure-policy">
                    Coordinated vulnerability disclosure policy</a>
                <a class="a-norm mx-lg-10 footer_website--bottom--item"
                   href="/static/files/RFC2350.pdf" target="_blank">RFC2350</a>
            </div>
            <div class="d-flex flex-column flex-lg-row mt-20 footer_website--bottom--right ml-auto">
                &copy; 2022-2026 CERT-EU. All rights reserved.
            </div>
        </div>
    </section>
</footer>

<script src="/files/js/functions.min.js?v=1.1" nonce="WG4TW_p3mEHskCivAl9aNMMV5SovH9sD"></script>
<script type="text/javascript" nonce="WG4TW_p3mEHskCivAl9aNMMV5SovH9sD">
    CERTEU.UTILS.MENUBAR_HORIZONTAL_LEVEL1.init();
    CERTEU.UTILS.SCROLL_TOP.init();
    CERTEU.UTILS.STICKY_HEADER.init();
    CERTEU.UTILS.COOKIES_POLICY.init();
</script>


<script type="text/javascript" nonce="WG4TW_p3mEHskCivAl9aNMMV5SovH9sD">
    CERTEU.UTILS.FONT_AMENDER.init();
</script>
</body>
</html>