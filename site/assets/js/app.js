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
    await Promise.all([wireGlobalSearch(), wireGithubBadge(), wireListFilters()]);
  }

  // ── topbar dropdown menus (More + display/accessibility) ───────────
  function wireMenus() {
    var pairs = [
      ['[data-more-toggle]', '[data-more-menu]'],
      ['[data-display-toggle]', '[data-display-menu]'],
    ];
    var open = [];
    function closeAll() {
      open.forEach(function (p) {
        p.btn.setAttribute('aria-expanded', 'false');
        p.btn.classList.remove('open');
        p.menu.hidden = true;
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
        closeAll();
        if (!isOpen) {
          menu.hidden = false;
          btn.setAttribute('aria-expanded', 'true');
          btn.classList.add('open');
          open.push({ btn: btn, menu: menu });
        }
      });
    });
    document.addEventListener('click', function (e) {
      if (!open.length) return;
      var inside = open.some(function (p) { return p.menu.contains(e.target) || p.btn.contains(e.target); });
      if (!inside) closeAll();
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
  }

  // ── mobile drawer ──────────────────────────────────────────────────
  function wireDrawer() {
    var btn = document.querySelector('[data-drawer-toggle]');
    var drawer = document.querySelector('[data-drawer]');
    if (!btn || !drawer) return;
    btn.addEventListener('click', function () {
      var isOpen = !drawer.hidden;
      drawer.hidden = isOpen;
      btn.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
      btn.classList.toggle('open', !isOpen);
    });
  }

  // ── search modal ───────────────────────────────────────────────────
  var searchModal = null;
  function openSearch() {
    if (!searchModal) return;
    searchModal.classList.add('open');
    var input = document.getElementById('q');
    if (input) setTimeout(function () { input.focus(); }, 20);
  }
  function closeSearch() {
    if (!searchModal) return;
    searchModal.classList.remove('open');
  }
  function wireSearchModal() {
    searchModal = document.querySelector('[data-search-modal]');
    document.querySelectorAll('[data-search-open]').forEach(function (btn) {
      btn.addEventListener('click', function (e) { e.preventDefault(); openSearch(); });
    });
    if (!searchModal) return;
    searchModal.querySelectorAll('[data-search-close]').forEach(function (el) {
      el.addEventListener('click', closeSearch);
    });
  }

  function wireKeyboardShortcuts() {
    document.addEventListener('keydown', function (e) {
      var tag = (e.target.tagName || '').toUpperCase();
      var editable = tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable;
      if (e.key === '/' && !editable) { e.preventDefault(); openSearch(); }
      if (e.key === 'Escape') closeSearch();
    });
  }

  // ── AI-provenance bar ──────────────────────────────────────────────
  var AI_KEY = 'ctipilot_ai_ack';
  function wireAiBar() {
    var bar = document.querySelector('[data-aibar]');
    if (!bar) return;
    var acked = false;
    try { acked = localStorage.getItem(AI_KEY) === '1'; } catch (_) {}
    if (!acked) bar.hidden = false;
    var close = bar.querySelector('[data-ai-dismiss]');
    if (close) close.addEventListener('click', function () {
      try { localStorage.setItem(AI_KEY, '1'); } catch (_) {}
      bar.hidden = true;
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

  // ── finding chip filters (live / day / weekly) ─────────────────────
  // The chip bar toggles a shared filter state; app.js applies it to
  // any `.finding[data-*]` on the page AND fires `cti:filterchange` so
  // brief.js can re-render the live timeline with the same state.
  function wireFindingFilters() {
    var toggle = document.querySelector('[data-filter-toggle]');
    var bar = document.querySelector('[data-filterbar]');
    var chips = Array.prototype.slice.call(document.querySelectorAll('.fchip[data-fk]'));
    if (!toggle && !chips.length) return;

    if (toggle && bar) {
      toggle.addEventListener('click', function () {
        var isOpen = bar.classList.toggle('open');
        toggle.classList.toggle('active', isOpen);
        toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      });
    }

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
      applyToFindings(sets);
      document.dispatchEvent(new CustomEvent('cti:filterchange', { detail: { sets: sets } }));
    }

    chips.forEach(function (c) {
      c.addEventListener('click', function () { c.classList.toggle('on'); refresh(); });
    });
    var clear = document.querySelector('[data-filter-clear]');
    if (clear) clear.addEventListener('click', function () {
      chips.forEach(function (c) { c.classList.remove('on'); });
      refresh();
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

  function applyToFindings(sets) {
    var findings = document.querySelectorAll('.finding[data-entry-id]');
    if (!findings.length) return;
    findings.forEach(function (el) {
      el.style.display = findingMatches(el, sets) ? '' : 'none';
    });
    // Hide a section header whose findings are now all hidden.
    document.querySelectorAll('.sect').forEach(function (sect) {
      var visible = false, n = sect.nextElementSibling;
      while (n && !n.classList.contains('sect')) {
        if (n.classList.contains('finding') && n.style.display !== 'none') { visible = true; break; }
        n = n.nextElementSibling;
      }
      sect.style.display = visible ? '' : 'none';
    });
  }

  // ── search autocomplete (inside the modal) ─────────────────────────
  async function wireGlobalSearch() {
    var input = document.getElementById('q');
    var ul = document.getElementById('suggestions');
    if (!input || !ul) return;
    var form = input.form;
    if (form) form.addEventListener('submit', function (e) { e.preventDefault(); });

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
    function close() { ul.hidden = true; ul.innerHTML = ''; active = -1; current = []; }
    function open(results, q) {
      current = results; active = -1;
      if (!results.length) { close(); return; }
      ul.innerHTML = results.map(function (r, i) {
        return '<li role="option" data-route="' + escapeAttr(r.route) + '" data-idx="' + i + '">'
          + '<span class="kind-pill">' + escapeHtml(r.kind) + '</span>'
          + '<div class="s-row"><span class="s-title">' + (window.Search ? Search.highlight(r.title, q) : escapeHtml(r.title)) + '</span>'
          + (r.hint ? '<span class="s-hint">' + (window.Search ? Search.highlight(r.hint, q) : escapeHtml(r.hint)) + '</span>' : '')
          + '</div></li>';
      }).join('');
      ul.hidden = false;
    }
    function setActive(i) {
      var items = ul.querySelectorAll('li');
      items.forEach(function (el, idx) { el.setAttribute('aria-selected', idx === i ? 'true' : 'false'); });
      active = i;
      if (i >= 0 && items[i]) items[i].scrollIntoView({ block: 'nearest' });
    }
    function navigate(route) { window.location.href = sitePrefix() + route; }

    input.addEventListener('input', async function () {
      var q = input.value.trim();
      if (!q) { close(); return; }
      var idx = await ensureIndex();
      if (!window.Search) { close(); return; }
      open(window.Search.query(idx, q, { limit: 10 }), q);
    });
    input.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); if (current.length) setActive(Math.min(active + 1, current.length - 1)); return; }
      if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(active - 1, 0)); return; }
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

  // ── Ops dashboard: run-detail picker ───────────────────────────────
  function wireOpsRunPicker() {
    var sel = document.getElementById('ops-run-select');
    if (!sel) return;
    var panels = document.querySelectorAll('[data-run-panel]');
    if (!panels.length) return;
    function show(key) {
      var matched = false;
      panels.forEach(function (p) {
        var isMatch = p.getAttribute('data-run-panel') === key;
        p.hidden = !isMatch;
        if (isMatch) matched = true;
      });
      return matched;
    }
    sel.addEventListener('change', function () {
      show(sel.value);
      if (window.history && history.replaceState) history.replaceState(null, '', '#run=' + encodeURIComponent(sel.value));
    });
    var m = (window.location.hash || '').match(/run=([^&]+)/);
    if (m) { var key = decodeURIComponent(m[1]); if (show(key)) sel.value = key; }
  }

  // ── list-page filters (briefs / cves / topics / sources / entities) ─
  function wireListFilters() {
    document.querySelectorAll('[data-filter-input]').forEach(function (input) {
      input.addEventListener('input', function () { applyListFilters(input.dataset.filterInput); });
    });
    document.querySelectorAll('[data-filter-chip]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        var facet = chip.dataset.filterChip;
        var siblings = document.querySelectorAll('[data-filter-chip="' + facet + '"]');
        var hasAllCompanion = false;
        siblings.forEach(function (c) { if (c.dataset.value === 'all') hasAllCompanion = true; });
        if (!hasAllCompanion) { chip.classList.toggle('active'); }
        else { siblings.forEach(function (c) { c.classList.remove('active'); }); chip.classList.add('active'); }
        var scope = facet.startsWith('brief-') ? 'briefs'
          : facet.startsWith('topic-') ? 'topics'
          : facet.startsWith('source-') ? 'sources'
          : facet.startsWith('entity-') ? 'entities' : null;
        if (scope) applyListFilters(scope);
      });
    });
    var cveInput = document.querySelector('[data-filter-input="cves"]');
    if (cveInput) cveInput.addEventListener('input', function () { applyListFilters('cves'); });
  }

  function applyListFilters(scope) {
    var q = '';
    var input = document.querySelector('[data-filter-input="' + scope + '"]');
    if (input) q = (input.value || '').toLowerCase().trim();
    function chipValue(facet) {
      var c = document.querySelector('[data-filter-chip="' + facet + '"].active');
      return c ? c.dataset.value : 'all';
    }
    if (scope === 'briefs') {
      document.querySelectorAll('[data-filter-list="briefs"] .arc').forEach(function (a) {
        var hay = a.dataset.briefHaystack || a.textContent.toLowerCase();
        a.style.display = (!q || hay.indexOf(q) >= 0) ? '' : 'none';
      });
    } else if (scope === 'cves') {
      document.querySelectorAll('[data-filter-table="cves"] tbody tr').forEach(function (tr) {
        var hay = tr.textContent.toLowerCase();
        tr.style.display = (!q || hay.indexOf(q) >= 0) ? '' : 'none';
      });
    } else if (scope === 'topics') {
      var ttype = chipValue('topic-type'), tflag = chipValue('topic-flag');
      document.querySelectorAll('[data-filter-list="topics"] li').forEach(function (li) {
        var typ = li.dataset.topicType || '';
        var flags = (li.dataset.topicFlags || '').split(',').filter(Boolean);
        var matchType = ttype === 'all' || typ === ttype;
        var matchFlag = (tflag === 'all')
          || (tflag === 'multi' && !flags.some(function (f) { return f.indexOf('SINGLE-SOURCE') === 0; }))
          || (tflag !== 'multi' && tflag !== 'all' && flags.indexOf(tflag) >= 0);
        var hay = li.textContent.toLowerCase();
        li.style.display = (matchType && matchFlag && (!q || hay.indexOf(q) >= 0)) ? '' : 'none';
      });
    } else if (scope === 'sources') {
      var cat = chipValue('source-cat'), stat = chipValue('source-status'), rel = chipValue('source-rel');
      var staleOnly = !!document.querySelector('[data-filter-chip="source-stale"].active');
      document.querySelectorAll('[data-filter-table="sources"] tbody tr').forEach(function (tr) {
        var cats = (tr.dataset.sourceCats || '').split(',').filter(Boolean);
        var matchCat = cat === 'all' || cats.indexOf(cat) >= 0;
        var matchStat = stat === 'all' || (tr.dataset.sourceStatus || '') === stat;
        var matchRel = !rel || rel === 'all' || (tr.dataset.sourceRel || '') === rel;
        var matchStale = !staleOnly || (tr.dataset.sourceStale || 'no') === 'yes';
        var hay = tr.textContent.toLowerCase();
        tr.style.display = (matchCat && matchStat && matchRel && matchStale && (!q || hay.indexOf(q) >= 0)) ? '' : 'none';
      });
    } else if (scope === 'entities') {
      var etype = chipValue('entity-type');
      document.querySelectorAll('[data-filter-list="entities"] li').forEach(function (li) {
        var matchType = etype === 'all' || (li.dataset.entityType || '') === etype;
        var hay = li.textContent.toLowerCase();
        li.style.display = (matchType && (!q || hay.indexOf(q) >= 0)) ? '' : 'none';
      });
    }
  }

  // ── helpers ─────────────────────────────────────────────────────────
  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }
  function escapeAttr(s) { return escapeHtml(s); }
})();
