/* app.js — topbar wiring + per-page light interactivity.
 *
 * The site is fully readable without this script. Everything below is
 * progressive enhancement: the More / display menus, the mobile drawer,
 * the search modal + autocomplete, the AI-provenance bar dismiss, the
 * copy-link button, the finding chip filters, list-page filters, and the
 * Ops dashboard pagers / run picker.
 *
 * No SPA: every page is a real HTML document. The script reads
 * `data/search.json` for autocomplete and `data/site.json` for the
 * GitHub-stars badge.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', init);

  function sitePrefix() {
    var m = document.querySelector('meta[name="cti-site-prefix"]');
    return (m && m.getAttribute('content')) || '';
  }

  async function init() {
    wireMenus();
    wireDrawer();
    wireSearchModal();
    wireKeyboardShortcuts();
    wireAiBar();
    wireCopyLink();
    wireFindingFilters();
    wireOpsRunPicker();
    wireOpsPagers();
    wireTableOverflow();
    foldOnPhone();
    await Promise.all([wireGlobalSearch(), wireGithubBadge(), wireListFilters()]);
  }

  // ── topbar dropdown menus (More + display/accessibility) ───────────
  // Escape closes and hands focus back to the button that opened the
  // menu; clicking or tabbing out of it closes it too.
  function wireMenus() {
    var pairs = [
      ['[data-more-toggle]', '[data-more-menu]'],
      ['[data-display-toggle]', '[data-display-menu]'],
    ];
    var open = [];
    function closeAll(restoreFocus) {
      open.forEach(function (p) {
        p.btn.setAttribute('aria-expanded', 'false');
        p.btn.classList.remove('open');
        p.menu.hidden = true;
        if (restoreFocus) p.btn.focus();
      });
      open = [];
    }
    pairs.forEach(function (sel) {
      var btn = document.querySelector(sel[0]);
      var menu = document.querySelector(sel[1]);
      if (!btn || !menu) return;
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        var isOpen = !menu.hidden;
        closeAll(false);
        if (!isOpen) {
          menu.hidden = false;
          btn.setAttribute('aria-expanded', 'true');
          btn.classList.add('open');
          open.push({ btn: btn, menu: menu });
        }
      });
      menu.addEventListener('focusout', function (e) {
        var to = e.relatedTarget;
        if (to && !menu.contains(to) && !btn.contains(to)) closeAll(false);
      });
    });
    document.addEventListener('click', function (e) {
      if (!open.length) return;
      var inside = open.some(function (p) { return p.menu.contains(e.target) || p.btn.contains(e.target); });
      if (!inside) closeAll(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && open.length) closeAll(true);
    });
  }

  // ── mobile drawer ──────────────────────────────────────────────────
  var drawerApi = { close: function () {} };
  function wireDrawer() {
    var btn = document.querySelector('[data-drawer-toggle]');
    var drawer = document.querySelector('[data-drawer]');
    if (!btn || !drawer) return;
    function set(openIt, restoreFocus) {
      drawer.hidden = !openIt;
      btn.setAttribute('aria-expanded', openIt ? 'true' : 'false');
      btn.setAttribute('aria-label', openIt ? 'Close menu' : 'Open menu');
      btn.classList.toggle('open', openIt);
      if (!openIt && restoreFocus) btn.focus();
    }
    drawerApi.close = function () { if (!drawer.hidden) set(false, false); };
    btn.addEventListener('click', function (e) { e.stopPropagation(); set(drawer.hidden, false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !drawer.hidden) set(false, true);
    });
    document.addEventListener('click', function (e) {
      if (drawer.hidden) return;
      if (drawer.contains(e.target) || btn.contains(e.target)) return;
      set(false, false);
    });
  }

  // ── search modal ───────────────────────────────────────────────────
  // A real dialog: focus moves in and is trapped there, the page behind
  // stops scrolling, and closing returns focus to whatever opened it.
  var searchModal = null, searchOpener = null;
  function searchOpen() { return !!(searchModal && searchModal.classList.contains('open')); }
  function openSearch(opener) {
    if (!searchModal) return;
    drawerApi.close();
    searchOpener = opener || document.activeElement;
    searchModal.classList.add('open');
    document.body.classList.add('modal-open');
    var input = document.getElementById('q');
    if (input) setTimeout(function () { input.focus(); input.select(); }, 20);
  }
  function closeSearch() {
    if (!searchOpen()) return;
    searchModal.classList.remove('open');
    document.body.classList.remove('modal-open');
    if (searchOpener && typeof searchOpener.focus === 'function' && document.contains(searchOpener)) {
      searchOpener.focus();
    }
    searchOpener = null;
  }
  function wireSearchModal() {
    searchModal = document.querySelector('[data-search-modal]');
    document.querySelectorAll('[data-search-open]').forEach(function (btn) {
      btn.addEventListener('click', function (e) { e.preventDefault(); openSearch(btn); });
    });
    if (!searchModal) return;
    searchModal.querySelectorAll('[data-search-close]').forEach(function (el) {
      el.addEventListener('click', closeSearch);
    });
    searchModal.addEventListener('keydown', function (e) {
      if (e.key !== 'Tab') return;
      var f = Array.prototype.filter.call(
        searchModal.querySelectorAll('input, button, [href], [tabindex]:not([tabindex="-1"])'),
        function (el) { return !el.disabled && el.offsetParent !== null; });
      if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  function wireKeyboardShortcuts() {
    document.addEventListener('keydown', function (e) {
      var tag = (e.target.tagName || '').toUpperCase();
      var editable = tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || e.target.isContentEditable;
      if (e.key === '/' && !editable && !e.metaKey && !e.ctrlKey && !e.altKey) { e.preventDefault(); openSearch(null); }
      if (e.key === 'Escape' && searchOpen()) closeSearch();
    });
  }

  // ── AI-provenance bar ──────────────────────────────────────────────
  // The bar is in the page for every reader (no-JS included); theme.js
  // marks <html data-ai-ack> before first paint once it was dismissed.
  var AI_KEY = 'ctipilot_ai_ack';
  function wireAiBar() {
    var bar = document.querySelector('[data-aibar]');
    if (!bar) return;
    var close = bar.querySelector('[data-ai-dismiss]');
    if (close) close.addEventListener('click', function () {
      try { localStorage.setItem(AI_KEY, '1'); } catch (_) {}
      document.documentElement.setAttribute('data-ai-ack', '');
    });
  }

  // ── copy-link (entry detail share button) ──────────────────────────
  function wireCopyLink() {
    document.querySelectorAll('[data-copy-link]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var url = window.location.href.split('#')[0];
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(function () { toast('Link copied'); });
        } else {
          toast(url);
        }
      });
    });
  }

  var toastEl = null;
  function toast(msg) {
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.className = 'toast';
      document.body.appendChild(toastEl);
    }
    toastEl.textContent = msg;
    toastEl.classList.add('show');
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { toastEl.classList.remove('show'); }, 1800);
  }

  // ── finding chip filters (live / day pages) ────────────────────────
  // The chip bar toggles a shared filter state; app.js applies it to
  // any `.finding[data-*]` on the page AND fires `cti:filterchange` so
  // brief.js can re-render the live timeline with the same state.
  function wireFindingFilters() {
    var toggle = document.querySelector('[data-filter-toggle]');
    var bar = document.querySelector('[data-filterbar]');
    var chips = Array.prototype.slice.call(document.querySelectorAll('.fchip[data-fk]'));
    if (!toggle && !chips.length) return;

    if (toggle && bar) {
      if (!bar.id) bar.id = 'filterbar';
      toggle.setAttribute('aria-controls', bar.id);
      toggle.addEventListener('click', function () {
        var isOpen = bar.classList.toggle('open');
        toggle.classList.toggle('active', isOpen);
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    }
    chips.forEach(function (c) { c.setAttribute('aria-pressed', 'false'); });

    function activeSets() {
      var sets = { priority: [], kind: [], tag: [], region: [] };
      chips.forEach(function (c) {
        if (c.classList.contains('on')) sets[c.getAttribute('data-fk')].push(c.getAttribute('data-fv'));
      });
      return sets;
    }

    function refresh() {
      var sets = activeSets();
      var count = sets.priority.length + sets.kind.length + sets.tag.length + sets.region.length;
      var badge = document.querySelector('[data-filter-count]');
      if (badge) { badge.textContent = String(count); badge.hidden = count === 0; }
      var clear = document.querySelector('[data-filter-clear]');
      if (clear) clear.hidden = count === 0;
      applyToFindings(sets, count);
      document.dispatchEvent(new CustomEvent('cti:filterchange', { detail: { sets: sets } }));
    }

    chips.forEach(function (c) {
      c.addEventListener('click', function () {
        var on = c.classList.toggle('on');
        c.setAttribute('aria-pressed', on ? 'true' : 'false');
        refresh();
      });
    });
    var clear = document.querySelector('[data-filter-clear]');
    if (clear) clear.addEventListener('click', function () {
      chips.forEach(function (c) { c.classList.remove('on'); c.setAttribute('aria-pressed', 'false'); });
      refresh();
    });
    document.addEventListener('click', function (e) {
      var t = e.target.closest && e.target.closest('[data-filter-reset]');
      if (t && clear) { e.preventDefault(); clear.click(); }
    });
  }

  function findingMatches(el, sets) {
    var pr = el.getAttribute('data-priority') || '';
    var kind = el.getAttribute('data-kind') || '';
    var tags = (el.getAttribute('data-tags') || '').split(/\s+/).filter(Boolean);
    var regions = (el.getAttribute('data-regions') || '').split(/\s+/).filter(Boolean);
    if (sets.priority.length && sets.priority.indexOf(pr) < 0) return false;
    if (sets.kind.length && sets.kind.indexOf(kind) < 0) return false;
    if (sets.tag.length && !sets.tag.some(function (t) { return tags.indexOf(t) >= 0; })) return false;
    if (sets.region.length && !sets.region.some(function (r) { return regions.indexOf(r) >= 0; })) return false;
    return true;
  }

  // Day pages: the filter applies to the whole page, not just the cards.
  // Everything that points at a finding (TL;DR line, alarm row, action
  // item) follows that finding; a section with nothing left disappears,
  // the jump chips follow their sections, and a filter that matches
  // nothing says so instead of leaving a blank page.
  function applyToFindings(sets, activeCount) {
    var findings = document.querySelectorAll('.finding[data-entry-id]');
    if (!findings.length) return;
    var shown = {};
    var nShown = 0;
    findings.forEach(function (el) {
      var ok = findingMatches(el, sets);
      el.style.display = ok ? '' : 'none';
      var id = el.getAttribute('data-entry-id');
      if (ok) { shown[id] = true; nShown++; } else if (!(id in shown)) { shown[id] = false; }
    });
    document.querySelectorAll('[data-entry-id]:not(.finding)').forEach(function (el) {
      if (el.closest('[data-brief-timeline]')) return;
      var id = el.getAttribute('data-entry-id');
      if (id in shown) el.style.display = shown[id] ? '' : 'none';
    });
    document.querySelectorAll('.sect').forEach(function (sect) {
      var linked = 0, visible = 0, n = sect.nextElementSibling;
      while (n && !n.classList.contains('sect')) {
        var ids = n.matches('[data-entry-id]') ? [n] : Array.prototype.slice.call(n.querySelectorAll('[data-entry-id]'));
        ids.forEach(function (x) { linked++; if (x.style.display !== 'none') visible++; });
        n = n.nextElementSibling;
      }
      sect.style.display = (!linked || visible) ? '' : 'none';
      var c = sect.querySelector('.c');
      if (c && linked) {
        if (!c.hasAttribute('data-total')) c.setAttribute('data-total', c.textContent);
        c.textContent = activeCount ? (visible + ' of ' + c.getAttribute('data-total')) : c.getAttribute('data-total');
      }
    });
    document.querySelectorAll('.secnav-chip').forEach(function (chip) {
      var id = (chip.getAttribute('href') || '').slice(1);
      var target = id ? document.getElementById(id) : null;
      chip.style.display = (target && target.style.display === 'none') ? 'none' : '';
    });
    var empty = document.querySelector('[data-filter-empty-findings]');
    if (!empty) {
      var bar = document.querySelector('[data-filterbar]');
      if (!bar) return;
      empty = document.createElement('p');
      empty.className = 'filter-empty';
      empty.setAttribute('data-filter-empty-findings', '');
      empty.setAttribute('role', 'status');
      empty.innerHTML = 'No finding on this page matches the active filters. <a href="#" data-filter-reset>Clear filters</a>';
      bar.parentNode.insertBefore(empty, bar.nextSibling);
    }
    empty.hidden = nShown > 0;
  }

  // ── search autocomplete (inside the modal) ─────────────────────────
  async function wireGlobalSearch() {
    var input = document.getElementById('q');
    var ul = document.getElementById('suggestions');
    if (!input || !ul) return;
    var form = input.form;
    if (form) form.addEventListener('submit', function (e) { e.preventDefault(); });
    // Combobox semantics, so a screen reader hears the highlighted result.
    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-controls', 'suggestions');
    input.setAttribute('aria-expanded', 'false');
    var emptyEl = document.createElement('p');
    emptyEl.className = 'search-empty';
    emptyEl.setAttribute('role', 'status');
    emptyEl.hidden = true;
    ul.parentNode.insertBefore(emptyEl, ul.nextSibling);

    var index = null, loading = null;
    function ensureIndex() {
      if (index) return Promise.resolve(index);
      if (loading) return loading;
      loading = fetch(sitePrefix() + 'data/search.json')
        .then(function (r) { return r.ok ? r.json() : []; })
        .then(function (j) { index = j || []; return index; })
        .catch(function () { index = []; return index; });
      return loading;
    }

    var active = -1, current = [];
    function close() {
      ul.hidden = true; ul.innerHTML = ''; active = -1; current = [];
      input.setAttribute('aria-expanded', 'false');
      input.removeAttribute('aria-activedescendant');
    }
    function open(results, q) {
      current = results; active = -1;
      emptyEl.hidden = !!results.length;
      if (!results.length) {
        emptyEl.textContent = 'No match for “' + q + '”. Try a CVE id, an actor, a product or a vendor.';
        close();
        return;
      }
      ul.innerHTML = results.map(function (r, i) {
        return '<li role="option" id="sugg-' + i + '" aria-selected="false" data-route="' + escapeAttr(r.route) + '" data-idx="' + i + '">'
          + '<span class="kind-pill">' + escapeHtml(r.kind) + '</span>'
          + '<div class="s-row"><span class="s-title">' + (window.Search ? Search.highlight(r.title, q) : escapeHtml(r.title)) + '</span>'
          + (r.hint ? '<span class="s-hint">' + (window.Search ? Search.highlight(r.hint, q) : escapeHtml(r.hint)) + '</span>' : '')
          + '</div></li>';
      }).join('');
      ul.hidden = false;
      input.setAttribute('aria-expanded', 'true');
    }
    function setActive(i) {
      var items = ul.querySelectorAll('li');
      items.forEach(function (el, idx) { el.setAttribute('aria-selected', idx === i ? 'true' : 'false'); });
      active = i;
      if (i >= 0 && items[i]) {
        items[i].scrollIntoView({ block: 'nearest' });
        input.setAttribute('aria-activedescendant', items[i].id);
      }
    }
    function navigate(route) { window.location.href = sitePrefix() + route; }

    input.addEventListener('input', async function () {
      var q = input.value.trim();
      if (!q) { close(); emptyEl.hidden = true; return; }
      var idx = await ensureIndex();
      if (!window.Search) { close(); return; }
      if (input.value.trim() !== q) return;
      open(window.Search.query(idx, q, { limit: 10 }), q);
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); if (current.length) setActive(Math.min(active + 1, current.length - 1)); return; }
      if (e.key === 'ArrowUp') { e.preventDefault(); if (current.length) setActive(Math.max(active - 1, 0)); return; }
      if (e.key === 'Enter') {
        e.preventDefault();
        if (active >= 0 && current[active]) navigate(current[active].route);
        else if (current[0]) navigate(current[0].route);
      }
    });
    ul.addEventListener('mousedown', function (e) {
      var li = e.target.closest('li[data-route]');
      if (!li) return;
      e.preventDefault();
      navigate(li.dataset.route);
    });
  }

  // ── github badge ────────────────────────────────────────────────────
  async function wireGithubBadge() {
    var link = document.getElementById('github-link');
    var stars = document.getElementById('github-stars');
    var starsMenu = document.getElementById('github-stars-menu');
    function show(n) {
      var txt = formatStars(n);
      [stars, starsMenu].forEach(function (el) { if (el) { el.textContent = txt; el.hidden = false; } });
      if (link) link.title = 'View source on GitHub · ' + n + ' stars';
    }
    var repoUrl = null;
    try {
      var r = await fetch(sitePrefix() + 'data/site.json');
      if (r.ok) {
        var gh = (await r.json()).github || {};
        if (gh.url) { repoUrl = gh.url; if (link) link.setAttribute('href', gh.url); }
        if (typeof gh.stars === 'number') { show(gh.stars); return; }
      }
    } catch (_) { /* fall through to the live API */ }
    // No build-time star count (offline build): fetch it live from GitHub.
    var repo = null;
    var m = (repoUrl || (link && link.getAttribute('href')) || '').match(/github\.com\/([^/]+\/[^/?#]+)/);
    if (m) repo = m[1].replace(/\.git$/, '');
    if (!repo) return;
    try {
      var gr = await fetch('https://api.github.com/repos/' + repo);
      if (!gr.ok) return;
      var gj = await gr.json();
      if (typeof gj.stargazers_count === 'number') show(gj.stargazers_count);
    } catch (_) { /* fail open: icon-only is fine */ }
  }
  function formatStars(n) {
    if (n < 1000) return String(n);
    if (n < 10000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return Math.round(n / 1000) + 'k';
  }

  // ── Ops dashboard: generic table pager ─────────────────────────────
  function wireOpsPagers() {
    var pagers = document.querySelectorAll('[data-ops-pager]');
    if (!pagers.length) return;
    pagers.forEach(function (pager) {
      var tbody = pager.querySelector('[data-pager-rows]');
      if (!tbody) return;
      var rows = Array.prototype.slice.call(tbody.rows);
      var total = rows.length;
      var sizeSel = pager.querySelector('[data-pager-size]');
      var prev = pager.querySelector('[data-pager-prev]');
      var next = pager.querySelector('[data-pager-next]');
      var status = pager.querySelector('[data-pager-status]');
      var bar = pager.querySelector('[data-pager-bar]');
      function curSize() {
        var v = parseInt((sizeSel && sizeSel.value) || pager.getAttribute('data-pagesize') || '10', 10);
        return (v > 0) ? v : 10;
      }
      var page = 1;
      function render() {
        var pageSize = curSize();
        var pages = Math.max(1, Math.ceil(total / pageSize));
        if (page > pages) page = pages;
        if (page < 1) page = 1;
        var start = (page - 1) * pageSize, end = Math.min(start + pageSize, total);
        for (var i = 0; i < rows.length; i++) rows[i].style.display = (i >= start && i < end) ? '' : 'none';
        if (status) status.textContent = total === 0 ? '0 of 0'
          : (start + 1) + '–' + end + ' of ' + total + ' · page ' + page + '/' + pages;
        if (prev) prev.disabled = (page <= 1);
        if (next) next.disabled = (page >= pages);
      }
      if (bar) bar.hidden = false;
      if (sizeSel) sizeSel.addEventListener('change', function () { page = 1; render(); });
      if (prev) prev.addEventListener('click', function () { if (page > 1) { page--; render(); } });
      if (next) next.addEventListener('click', function () {
        var pages = Math.max(1, Math.ceil(total / curSize()));
        if (page < pages) { page++; render(); }
      });
      render();
    });
  }

  // ── Ops dashboard: legacy #run=<id> deep links ─────────────────────
  // The in-page run picker is gone — every run lives on its own page at
  // /runs/<run-id>/, and the Run log table's run ids link there. Old
  // bookmarked /ops/#run=<id> links redirect to the run's page.
  function wireOpsRunPicker() {
    var marker = document.querySelector('[data-runs-base]');
    if (!marker) return;
    var m = (window.location.hash || '').match(/run=([^&]+)/);
    if (m) {
      window.location.replace(
        marker.getAttribute('data-runs-base') + encodeURIComponent(decodeURIComponent(m[1])) + '/'
      );
    }
  }

  // ── list-page filters (briefs / cves / topics / sources / entities) ─
  // Chips are buttons with aria-pressed; every list says so when a
  // filter leaves it empty.
  function wireListFilters() {
    document.querySelectorAll('[data-filter-input]').forEach(function (input) {
      input.addEventListener('input', function () { applyListFilters(input.dataset.filterInput); });
    });
    var chips = document.querySelectorAll('[data-filter-chip]');
    function syncPressed() {
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c.classList.contains('active') ? 'true' : 'false'); });
    }
    syncPressed();
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var facet = chip.dataset.filterChip;
        var siblings = document.querySelectorAll('[data-filter-chip="' + facet + '"]');
        var hasAllCompanion = false;
        siblings.forEach(function (c) { if (c.dataset.value === 'all') hasAllCompanion = true; });
        if (!hasAllCompanion) { chip.classList.toggle('active'); }
        else { siblings.forEach(function (c) { c.classList.remove('active'); }); chip.classList.add('active'); }
        syncPressed();
        var scope = facet.startsWith('brief-') ? 'briefs'
          : facet.startsWith('topic-') ? 'topics'
          : facet.startsWith('source-') ? 'sources'
          : facet.startsWith('cve-') ? 'cves'
          : facet.startsWith('entity-') ? 'entities' : null;
        if (scope) applyListFilters(scope);
      });
    });
  }

  function listEmpty(scope, container, nVisible) {
    if (!container) return;
    var msg = document.querySelector('[data-filter-empty="' + scope + '"]');
    if (!msg) {
      msg = document.createElement('p');
      msg.className = 'filter-empty';
      msg.setAttribute('data-filter-empty', scope);
      msg.setAttribute('role', 'status');
      msg.textContent = 'Nothing matches this filter.';
      container.parentNode.insertBefore(msg, container.nextSibling);
    }
    msg.hidden = nVisible > 0;
  }

  function applyListFilters(scope) {
    var q = '';
    var input = document.querySelector('[data-filter-input="' + scope + '"]');
    if (input) q = (input.value || '').toLowerCase().trim();
    function chipValue(facet) {
      var c = document.querySelector('[data-filter-chip="' + facet + '"].active');
      return c ? c.dataset.value : 'all';
    }
    function hay(el, extra) { return ((extra || '') + ' ' + el.textContent).toLowerCase(); }
    var n = 0;
    function show(el, ok) { el.style.display = ok ? '' : 'none'; if (ok) n++; }
    if (scope === 'briefs') {
      document.querySelectorAll('[data-filter-list="briefs"] .arc').forEach(function (a) {
        show(a, !q || hay(a, a.dataset.briefHaystack).indexOf(q) >= 0);
      });
      listEmpty(scope, document.querySelector('[data-filter-list="briefs"]'), n);
    } else if (scope === 'cves') {
      var cveYear = chipValue('cve-year');
      document.querySelectorAll('[data-filter-table="cves"] tbody tr').forEach(function (tr) {
        var matchYear = cveYear === 'all' || (tr.dataset.cveYear || '') === cveYear;
        show(tr, matchYear && (!q || hay(tr).indexOf(q) >= 0));
      });
      var t = document.querySelector('[data-filter-table="cves"]');
      listEmpty(scope, t && (t.closest('.data-wrap') || t), n);
    } else if (scope === 'topics') {
      var ttype = chipValue('topic-type'), tflag = chipValue('topic-flag');
      document.querySelectorAll('[data-filter-list="topics"] li').forEach(function (li) {
        var typ = li.dataset.topicType || '';
        var flags = (li.dataset.topicFlags || '').split(',').filter(Boolean);
        var matchType = ttype === 'all' || typ === ttype;
        var matchFlag = (tflag === 'all')
          || (tflag === 'multi' && !flags.some(function (f) { return f.indexOf('SINGLE-SOURCE') === 0; }))
          || (tflag !== 'multi' && tflag !== 'all' && flags.indexOf(tflag) >= 0);
        show(li, matchType && matchFlag && (!q || hay(li, li.dataset.aliases).indexOf(q) >= 0));
      });
      listEmpty(scope, document.querySelector('[data-filter-list="topics"]'), n);
    } else if (scope === 'sources') {
      var cat = chipValue('source-cat'), stat = chipValue('source-status'), rel = chipValue('source-rel');
      var staleOnly = !!document.querySelector('[data-filter-chip="source-stale"].active');
      document.querySelectorAll('[data-filter-table="sources"] tbody tr').forEach(function (tr) {
        var cats = (tr.dataset.sourceCats || '').split(',').filter(Boolean);
        var matchCat = cat === 'all' || cats.indexOf(cat) >= 0;
        var matchStat = stat === 'all' || (tr.dataset.sourceStatus || '') === stat;
        var matchRel = !rel || rel === 'all' || (tr.dataset.sourceRel || '') === rel;
        var matchStale = !staleOnly || (tr.dataset.sourceStale || 'no') === 'yes';
        show(tr, matchCat && matchStat && matchRel && matchStale && (!q || hay(tr).indexOf(q) >= 0));
      });
      var st = document.querySelector('[data-filter-table="sources"]');
      listEmpty(scope, st && (st.closest('.data-wrap') || st), n);
    } else if (scope === 'entities') {
      var etype = chipValue('entity-type');
      document.querySelectorAll('[data-filter-list="entities"] li').forEach(function (li) {
        var matchType = etype === 'all' || (li.dataset.entityType || '') === etype;
        show(li, matchType && (!q || hay(li, li.dataset.aliases).indexOf(q) >= 0));
      });
      listEmpty(scope, document.querySelector('[data-filter-list="entities"]'), n);
    }
  }

  // ── list-page statistics fold away on a phone ──────────────────────
  function foldOnPhone() {
    if (!window.matchMedia || !window.matchMedia('(max-width: 639px)').matches) return;
    document.querySelectorAll('details[data-fold-on-phone]').forEach(function (d) { d.open = false; });
  }

  // ── wide tables: flag the edge that has more to scroll ─────────────
  function wireTableOverflow() {
    var wraps = document.querySelectorAll('.data-wrap');
    if (!wraps.length) return;
    function flag(w) {
      var more = w.scrollWidth - w.clientWidth;
      w.toggleAttribute('data-more-right', more > 2 && w.scrollLeft < more - 2);
      w.toggleAttribute('data-more-left', more > 2 && w.scrollLeft > 2);
    }
    wraps.forEach(function (w) {
      flag(w);
      w.addEventListener('scroll', function () { flag(w); }, { passive: true });
    });
    window.addEventListener('resize', function () { wraps.forEach(flag); });
  }

  // ── helpers ─────────────────────────────────────────────────────────
  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }
  function escapeAttr(s) { return escapeHtml(s); }
})();
