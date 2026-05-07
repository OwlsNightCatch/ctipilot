/* app.js — boot the SPA. Loads data, wires up the global search box, and
   drops control to the router. */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', async () => {
    const view = document.getElementById('view');
    try {
      await Store.load();
    } catch (e) {
      writeView(view, `<div class="empty"><h1>Failed to load data</h1><p>${escapeHtml(e.message)}</p></div>`);
      return;
    }

    setFooterMeta();
    wireGithubBadge();
    wireGlobalSearch();
    wireKeyboard();
    wireLinkBehaviour();
    surfaceSanitiserHealth();
    Router.boot();
    Router.dispatch();
  });

  function writeView(view, html) { view.innerHTML = html; }
  function setHTML(el, html) { el.innerHTML = html; }

  /** If render.js's boot-time XSS self-test failed (the sanitiser was
      somehow broken or replaced), show a persistent warning banner. */
  function surfaceSanitiserHealth() {
    if (!window.Render || typeof Render.selfTest !== 'function') return;
    let reason = Render.renderUnsafeReason && Render.renderUnsafeReason();
    if (!reason) reason = Render.selfTest();
    if (!reason) return;
    const banner = document.createElement('div');
    banner.setAttribute('role', 'alert');
    banner.style.cssText = (
      'position:sticky;top:0;z-index:1000;padding:.7rem 1rem;'
      + 'background:#5a0e0e;color:#ffe;border-bottom:2px solid #ff8a8a;'
      + 'font:600 .85rem/1.4 ui-monospace,monospace;'
    );
    banner.textContent = (
      '⚠ Markdown sanitiser self-test failed. Brief content is being '
      + 'rendered as escaped plain text for safety. Reload after the next '
      + 'site deploy. (Detail in browser console.)'
    );
    document.body.insertBefore(banner, document.body.firstChild);
  }

  /** Global click delegate for anchor behaviour. */
  function wireLinkBehaviour() {
    document.addEventListener('click', (e) => {
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
      const a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      const href = a.getAttribute('href');
      if (!href) return;

      // In-page anchor (NOT an SPA hash route): smooth-scroll, keep SPA hash.
      if (href.startsWith('#') && !href.startsWith('#/')) {
        const id = decodeURIComponent(href.slice(1));
        const el = id ? document.getElementById(id) : null;
        if (el) {
          e.preventDefault();
          const det = el.closest('details');
          if (det) det.open = true;
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
          el.setAttribute('tabindex', '-1');
          el.focus({ preventScroll: true });
        } else {
          e.preventDefault();
        }
        return;
      }

      // Off-origin absolute URL: ensure new tab.
      if (/^https?:\/\//i.test(href)) {
        try {
          const u = new URL(href);
          if (u.origin !== location.origin && a.target !== '_blank') {
            e.preventDefault();
            window.open(u.href, '_blank', 'noopener,noreferrer');
          }
        } catch (_) { /* malformed URL — let the browser decide */ }
      }
    });
  }

  /** Populate the topbar GitHub icon's href and star count from
      `data/site.json#github`. The values are baked at build time
      (site/build.py fetches the GitHub repo metadata once per deploy);
      no per-visitor request to api.github.com — and therefore no
      cross-origin connection from the visitor's browser. If the
      build-time fetch failed (rate limit, no network in CI), the
      number stays hidden and only the icon shows. */
  function wireGithubBadge() {
    const link = document.getElementById('github-link');
    const stars = document.getElementById('github-stars');
    const gh = (Store.site && Store.site.github) || {};
    if (link && gh.url) link.setAttribute('href', gh.url);
    if (stars && typeof gh.stars === 'number') {
      stars.textContent = formatStars(gh.stars);
      stars.hidden = false;
      if (link) link.title = `View source on GitHub · ${gh.stars} stars`;
    }
  }

  /** Compact star formatter: 1234 → "1.2k", 12345 → "12.3k". */
  function formatStars(n) {
    if (n < 1000) return String(n);
    if (n < 10000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return Math.round(n / 1000) + 'k';
  }

  function setFooterMeta() {
    const meta = document.getElementById('footer-meta');
    if (!meta) return;
    const c = (Store.site && Store.site.counts) || {};
    const t = (Store.site && Store.site.built_at) || '—';
    meta.textContent = `${c.briefs || 0} briefs · ${c.cves || 0} CVEs · ${c.topics || 0} topics · ${c.sources || 0} sources · built ${t}`;
  }

  /** Top-bar search: live suggestions + Enter to go to /search?q=. */
  function wireGlobalSearch() {
    const input = document.getElementById('q');
    const ul = document.getElementById('suggestions');
    if (!input || !ul) return;

    let active = -1;
    let current = [];

    function close() { ul.hidden = true; setHTML(ul, ''); active = -1; current = []; }

    function open(results) {
      current = results;
      active = -1;
      if (!results.length) { close(); return; }
      const html = results.map((r, i) => `
        <li role="option" data-route="${escapeAttr(r.route)}" data-idx="${i}">
          <span class="kind-pill">${escapeHtml(r.kind)}</span>
          <div class="s-row">
            <span class="s-title">${highlight(r.title, input.value)}</span>
            ${r.hint ? `<span class="s-hint">${highlight(r.hint, input.value)}</span>` : ''}
          </div>
        </li>
      `).join('');
      setHTML(ul, html);
      ul.hidden = false;
    }

    function setActive(i) {
      const items = ul.querySelectorAll('li');
      items.forEach((el, idx) => el.setAttribute('aria-selected', idx === i ? 'true' : 'false'));
      active = i;
      if (i >= 0 && items[i]) items[i].scrollIntoView({ block: 'nearest' });
    }

    input.addEventListener('input', () => {
      const q = input.value.trim();
      if (!q) { close(); return; }
      const results = Search.query(Store.search, q, { limit: 10 });
      open(results);
    });

    input.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') { input.blur(); close(); return; }
      if (e.key === 'ArrowDown') { e.preventDefault(); if (current.length) setActive(Math.min(active + 1, current.length - 1)); return; }
      if (e.key === 'ArrowUp')   { e.preventDefault(); setActive(Math.max(active - 1, 0)); return; }
      if (e.key === 'Enter') {
        e.preventDefault();
        if (active >= 0 && current[active]) {
          window.location.hash = current[active].route.startsWith('#') ? current[active].route.slice(1) : current[active].route;
        } else {
          window.location.hash = '/search?q=' + encodeURIComponent(input.value.trim());
        }
        close();
      }
    });

    ul.addEventListener('mousedown', (e) => {
      const li = e.target.closest('li[data-route]');
      if (!li) return;
      e.preventDefault();
      const route = li.dataset.route;
      window.location.hash = route.startsWith('#') ? route.slice(1) : route;
      close();
    });

    document.addEventListener('click', (e) => {
      if (!input.contains(e.target) && !ul.contains(e.target)) close();
    });
  }

  /** Keyboard: '/' focuses search; 'Esc' clears it. Don't eat keys in editable fields. */
  function wireKeyboard() {
    document.addEventListener('keydown', (e) => {
      const tag = (e.target.tagName || '').toUpperCase();
      const editable = tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable;
      if (e.key === '/' && !editable) {
        e.preventDefault();
        const input = document.getElementById('q');
        if (input) input.focus();
      }
    });
  }

  /** Console diagnostic — call from DevTools as `checkUmami()`.
      Helps the operator figure out why a visit isn't appearing in the
      Umami dashboard. Tests in order:
        1. Is the umami script element in the DOM?
        2. Is the `window.umami` global defined? (script may have loaded
           but a privacy extension stripped its init.)
        3. Is `navigator.doNotTrack` set? Combined with our
           `data-do-not-track="true"` flag, that silences the tracker.
        4. Does an actual fetch to https://cloud.umami.is/api/send
           succeed? If this fails with `Failed to fetch` and no other
           obvious cause, it's almost certainly a content-blocker —
           Brave Shields, uBlock Origin, AdGuard, Pi-hole, etc. — that
           blacklists cloud.umami.is at the network layer. The script
           tag may load (cached), but the beacon POST is dropped.
      Logs each result as `info` / `warn` / `error` so it's easy to
      eyeball in the console. */
  window.checkUmami = async function checkUmami() {
    const tag = document.querySelector('script[src*="cloud.umami.is"]');
    console.group('[checkUmami]');
    console.info('1. <script> tag in DOM:', tag ? 'yes' : 'NO — markup missing');
    console.info('   src:', tag?.src, '· website-id:', tag?.dataset?.websiteId);
    console.info('   data-do-not-track:', tag?.dataset?.doNotTrack || '(not set)');
    console.info('2. window.umami global:', typeof window.umami !== 'undefined' ? 'defined' : 'UNDEFINED — script loaded but did not initialise (likely a content-blocker stripped it)');
    console.info('3. navigator.doNotTrack:', navigator.doNotTrack, '· globalPrivacyControl:', !!window.globalPrivacyControl);
    if (navigator.doNotTrack === '1' || window.globalPrivacyControl) {
      console.warn('   ⚠ Browser sends DNT/GPC. With data-do-not-track="true" the tracker is a deliberate no-op. Test in another browser or disable DNT to see your own visits.');
    }
    console.info('4. POST to cloud.umami.is/api/send …');
    try {
      const r = await fetch('https://cloud.umami.is/api/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          payload: {
            hostname: location.hostname,
            language: navigator.language || 'en-US',
            referrer: document.referrer || '',
            screen: screen.width + 'x' + screen.height,
            title: 'checkUmami diagnostic',
            url: location.pathname + location.hash,
            website: tag?.dataset?.websiteId,
          },
          type: 'event',
        }),
      });
      console.info('   HTTP', r.status, '— if 200, the beacon endpoint is reachable from your browser.');
      if (!r.ok) console.warn('   ⚠ Non-200 response. Check the website-id matches the dashboard.');
    } catch (e) {
      console.error('   ❌ Fetch failed:', e.message, '— this almost always means a privacy extension / Brave Shields / Pi-hole is blocking cloud.umami.is at the network layer. Disable shields for this site or test in another browser.');
    }
    console.info('5. Verbose logging: set `window.__ctibriefsDebugUmami = true` to log every umami.track() call to the console.');
    console.groupEnd();
    return 'See console output above';
  };

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }
  function escapeAttr(s) { return escapeHtml(s); }
  function highlight(text, q) { return Search.highlight(text, q); }
})();
