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
    Router.boot();
    Router.dispatch();
  });

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
