/* app.js — boot the SPA. Loads data, wires up the global search box, and
   drops control to the router. */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', async () => {
    const view = document.getElementById('view');
    try {
      await Store.load();
    } catch (e) {
      view.innerHTML = `<div class="empty"><h1>Failed to load data</h1><p>${e.message}</p></div>`;
      return;
    }

    setFooterMeta();
    wireGlobalSearch();
    wireKeyboard();
    wireLinkBehaviour();
    surfaceSanitiserHealth();
    Router.boot();
    Router.dispatch();
  });

  /** If render.js's boot-time XSS self-test failed (the sanitiser was
      somehow broken or replaced), show a persistent warning banner above
      the view so operators see it immediately on the next visit. The
      site still renders — just with markdown content escaped to plain
      text — so an attacker payload cannot execute. */
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

  /** Global click delegate for anchor behaviour:
       - href="#section"  (in-page anchor; not "#/...")  → smooth-scroll to
         the matching id, do not change the SPA's hash. Fixes the bug where
         clicking "On this page" links landed nowhere because the SPA's
         hashchange listener treated them as routes.
       - href="https?://..." that isn't already same-origin → open in a new
         tab. This is a safety net beyond the DOMPurify hook in render.js,
         so any externally-pointing <a> in any template (markdown, sidebar,
         topic/CVE/source pages) gets the same treatment.

      Honours modifier-key clicks (cmd/ctrl/shift/alt) and middle-click —
      the browser's native "open in new tab / window" stays untouched. */
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
          el.scrollIntoView({ behavior: 'smooth', block: 'start' });
          el.setAttribute('tabindex', '-1');
          el.focus({ preventScroll: true });
        } else {
          // Anchor target missing — at least don't blow away the SPA hash.
          e.preventDefault();
        }
        return;
      }

      // Off-origin absolute URL: ensure new tab. (Same-origin / relative
      // links and mailto:/tel:/#/ SPA routes pass through untouched.)
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

    let active = -1; // index into current results
    let current = [];

    function close() { ul.hidden = true; ul.innerHTML = ''; active = -1; current = []; }

    function open(results) {
      current = results;
      active = -1;
      if (!results.length) { close(); return; }
      ul.innerHTML = results.map((r, i) => `
        <li role="option" data-route="${escapeAttr(r.route)}" data-idx="${i}">
          <span class="kind-pill">${escapeHtml(r.kind)}</span>
          <div class="s-row">
            <span class="s-title">${highlight(r.title, input.value)}</span>
            ${r.hint ? `<span class="s-hint">${highlight(r.hint, input.value)}</span>` : ''}
          </div>
        </li>
      `).join('');
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
        document.getElementById('q').focus();
      }
    });
  }

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }
  function escapeAttr(s) { return escapeHtml(s); }
  function highlight(text, q) { return Search.highlight(text, q); }
})();
