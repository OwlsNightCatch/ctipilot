<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<script>(function(t,n,r,e,m){t[e]=t[e]||[],t[e].push({"gtm.start":new Date().getTime(),event:"gtm.js"});var g=n.getElementsByTagName(r)[0],a=n.createElement(r),s=e!="dataLayer"?"&l="+e:"";a.async=!0,a.src="https://www.googletagmanager.com/gtm.js?id="+m+s,g.parentNode.insertBefore(a,g)})(window,document,"script","dataLayer","GTM-TKVKGB67");</script><script async src="https://www.googletagmanager.com/gtag/js?id=AW-18195309024"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}gtag("js",new Date),gtag("config","AW-18195309024");</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>NGINX2Root by Xint — From nginx visitor to root of the server host</title>
<meta name="description" content="Xint discovered five nginx vulnerabilities, including CVE-2026-123007. From unauthenticated RCE to host root, chained with a kernel exploit.">
<meta property="og:type" content="website">
<meta property="og:site_name" content="NGINX2Root">
<meta property="og:title" content="NGINX2Root by Xint — From nginx visitor to root of the server host">
<meta property="og:description" content="Xint discovered five nginx vulnerabilities, including CVE-2026-123007. From unauthenticated RCE to host root, chained with a kernel exploit.">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="ko_KR">
<meta property="og:locale:alternate" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@xint_official">
<meta name="theme-color" content="#ffffff">
<link rel="canonical" href="https://nginx2root.com/">
<meta property="og:url" content="https://nginx2root.com/">
<link rel="alternate" hreflang="en" href="https://nginx2root.com/">
<link rel="alternate" hreflang="ko" href="https://nginx2root.com/ko/">
<link rel="alternate" hreflang="ja" href="https://nginx2root.com/ja/">
<link rel="alternate" hreflang="x-default" href="https://nginx2root.com/">
<meta property="og:image" content="https://nginx2root.com/assets/og.03b1de4f.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="NGINX2Root — Found by Xint">
<meta name="twitter:image" content="https://nginx2root.com/assets/og.03b1de4f.jpg">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="icon" href="/favicon.ico">
<link rel="stylesheet" href="/assets/site.87c68c7d.css">
<script>window.N2R_LANG="en";window.N2R_PAGES={"en": "/", "ko": "/ko/", "ja": "/ja/"};window.N2R_HUBSPOT={"portalId": "244114931", "region": "na2", "en": "f4b5e243-d2ef-427c-bcb8-02efa125bd41", "ko": "6ca861ee-a17f-4593-aa6a-957731823000", "script": "https://js-na2.hsforms.net/forms/embed/244114931.js"};</script>
<script src="/assets/app.7df320cd.js" defer></script>
</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TKVKGB67"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<div class="stage" id="stage" data-hl="en"><div class="v3top v3sticky">
  <header class="v3nav"><div class="v3in">
    <a class="v3brand" href="#top"><b>NGINX2Root</b></a>
    <nav class="v3links">
      <a href="https://xint.io/blog/nginx2root-remote-code-execution" target="_blank" rel="noopener" data-blog-link><span data-hl="en"><span class="v3x">Read on </span>Xint Blog</span><span data-hl="ko">Xint 블로그<span class="v3x">에서 읽기</span></span><span data-hl="ja">Xintブログ<span class="v3x">で読む</span></span>&nbsp;↗</a>
      <div class="v3lang v3dd"><button type="button" class="v3dd-btn" aria-haspopup="true" aria-expanded="false" aria-label="Language"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9c-2.5-2.6-3.8-5.6-3.8-9S9.5 5.6 12 3z"/></svg><span data-lc="en">English</span><span data-lc="ko">한국어</span><span data-lc="ja">日本語</span><svg class="v3dd-chev" viewBox="0 0 12 12" width="10" height="10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 4.5 6 7.5 9 4.5"/></svg></button><ul class="v3dd-menu" hidden><li><a href="/" hreflang="en" lang="en">English</a></li><li><a href="/ko/" hreflang="ko" lang="ko">한국어</a></li><li><a href="/ja/" hreflang="ja" lang="ja">日本語</a></li></ul></div>
    </nav>
  </div></header>
</div><div class="n2r" id="top">
  <section class="x-hero x-hero2 h2-nodesc" id="x-hero-tune" data-cve="text" data-xint="hero" style="--h2-h:440px">
    <div class="x-herobg" aria-hidden="true"><canvas id="x-net-t"></canvas></div>
    <div class="h2-in">
      <a class="h2-found" href="https://xint.io" target="_blank" rel="noopener"><span>Found by</span><svg viewBox="0 0 73 29" fill="currentColor" role="img" aria-label="Xint"><path d="M54.9153 7.66895H40.1635V28.2942H44.3521V11.5129H54.4877V28.2942H58.6774V11.058L54.9153 7.66895Z"/><path d="M36.3212 2.01758H32.1289V5.51266H36.3212V2.01758Z"/><path d="M36.3212 7.60742H32.1289V28.2314H36.3212V7.60742Z"/><path d="M73 11.3975V7.61891H66.7129V0L62.5205 3.77492V24.5321L66.7129 28.2441H73V24.6369H66.7129V11.3975H73Z"/><path d="M23.0619 3.83496L16.4383 10.6673L5.93916 3.83496H3.49426L18.1832 16.0659L30.0416 3.83496H23.0619Z"/><path d="M6.99699 28.2974L15.2151 19.7638L27.596 28.2974H30.0409L13.4554 14.3184L0 28.2974H6.99699Z"/></svg></a>
      <h1 class="h2-title">NGINX2Root</h1>
      <p class="h2-sub"><span data-hl="en">From nginx visitor to root of the server host</span><span data-hl="ko">nginx 방문자에서 서버 호스트의 root까지</span><span data-hl="ja">nginxへの未認証アクセスから、サーバーホストのroot権限へ</span></p>
      <ul class="h2-cves" aria-label="CVE"><li>CVE-2026-123007</li><li>CVE-2026-123634</li><li>CVE-2026-123633</li><li>CVE-2026-121810</li><li>CVE-2026-113425</li></ul>
      <div class="h2-ctas">
        <a class="h2-btn" href="#fix"><span data-hl="en">How to Fix it</span><span data-hl="ko">대응 방법 보기</span><span data-hl="ja">対処方法</span></a>
        <a class="h2-link" href="https://xint.io/blog/nginx2root-remote-code-execution" target="_blank" rel="noopener" data-blog-link><span data-hl="en">Full Writeup</span><span data-hl="ko">전체 분석 보기</span><span data-hl="ja">技術解説を読む</span></a>
      </div>
    </div>
  </section>
</div>
<div id="mount" class="draft v-polish"></div></div>
<script type="text/javascript" id="hs-script-loader" async defer src="//js-na2.hs-scripts.com/244114931.js"></script><script type="text/javascript">_linkedin_partner_id="9557308",window._linkedin_data_partner_ids=window._linkedin_data_partner_ids||[],window._linkedin_data_partner_ids.push(_linkedin_partner_id);</script><script type="text/javascript">(function(i){i||(window.lintrk=function(e,r){window.lintrk.q.push([e,r])},window.lintrk.q=[]);var n=document.getElementsByTagName("script")[0],t=document.createElement("script");t.type="text/javascript",t.async=!0,t.src="https://snap.licdn.com/li.lms-analytics/insight.min.js",n.parentNode.insertBefore(t,n)})(window.lintrk);</script><noscript><img height="1" width="1" style="display:none;" alt="" src="https://px.ads.linkedin.com/collect/?pid=9557308&fmt=gif" /></noscript>
</body>
</html>
