<!DOCTYPE html>
<!-- Adapted from haphash for Varnish PoW -->
<meta name="viewport" content="width=device-width">
<title>I Challenge Thee</title>
<style>
  body { background: #ddd; color: #000; margin: 0; padding: 0; }
  #progress { position: absolute; margin: 0; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; font-size: 125%; }
  #progressBar { font-size: 250%; user-select: none; }
  #progressBar.done { transition: font-size 2s linear, opacity 2s linear; font-size: 1000%; opacity: 0.5; }
  .animate { animation: spin 2s infinite linear; }
  @keyframes spin {
    to { transform:rotate(360deg); }
  }
  footer { position: fixed; bottom: 4px; width: 100%; text-align: center; }
</style>
<div id="progress"><span id="progressText"></span><div id="progressBar"></div></div>
<script>
  "use strict";
  async function solve() {
    const output = document.getElementById('progressText');
    const bar = document.getElementById('progressBar');
    // Get challenge from cookie
    const match = document.cookie.match(/pow_challenge=([^;]+)/);
    if (!match) {
        output.innerText = "Error: No challenge cookie found. Please enable cookies.";
        return;
    }
    const challenge = match[1];
    
    output.innerText = "✋ Checking connection, please wait";
    bar.innerText = '🌀';
    bar.className = 'animate';
    const te = new TextEncoder();
    let tries = 0;
    
    // Get original URL from query params
    const params = new URLSearchParams(location.search);
    const _originalUrl = params.get("original") || "/";
    // Ignore attempts to redirect out of the site
    let originalUrl = _originalUrl.replace(new RegExp("^//+"), "/")
    originalUrl = originalUrl.replace(new RegExp("^[^/]*//.*"), "/")
    // Capture the original referer so we can forward it on the redirect.
    // params.has() distinguishes "no referer" (empty) from "absent".
    const hasReferer = params.has("referer");
    const referer = params.get("referer") || "";
    for (; tries < 10000000; tries++) {
      // PoW: SHA256(challenge + ";" + tries)
      const msg = challenge + ";" + tries;
      const hashBuffer = await crypto.subtle.digest("SHA-256", te.encode(msg));
      const hashArray = new Uint8Array(hashBuffer);
      // Check for Diff=2 (2 zero nibbles => 1 zero byte)
      if (hashArray[0] === 0) {
          console.log("Success: " + msg);
          // Success
          document.cookie = "pow_nonce=" + tries + "; path=/; max-age=3000";
          
          bar.className = 'done';
          bar.innerText = '✅';
          output.innerText = "Verified!";
          
          // Redirect back to original URL, replacing history so challenge page is not reachable via back button
          let finalUrl = originalUrl;
          if (hasReferer) {
              const sep = finalUrl.indexOf("?") !== -1 ? "&" : "?";
              finalUrl = finalUrl + sep + "pow_referer=" + encodeURIComponent(referer);
          }
          location.replace(finalUrl + location.hash);
          return;
      }
    }
    
    output.innerText = "Failed to solve challenge.";
    bar.className = 'error';
    bar.innerText = '🤯';
  }
  window.addEventListener("load", solve);
</script>
<noscript>AI scrapers break the web, to use this page you'll need JavaScript enabled.</noscript>
