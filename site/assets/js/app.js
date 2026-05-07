/* app.js — topbar wiring + per-page light interactivity.
 *
 * The site is fully readable without this script. Everything below is
 * progressive enhancement: topbar searchbox autocomplete, list-page
 * filter chips (briefs / cves / topics / sources), copy-link button on
 * the brief page, mobile nav toggle, '/' to focus search.
 *
 * No SPA: every page is a real HTML document. The script reads
 * `data/search.json` for autocomplete and `data/site.json` for the
 * GitHub-stars badge in the topbar.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', init);

  // Path prefix back to site root, written by the build into the
  // <meta name="cti-site-prefix"> tag. Used to build absolute URLs from
  // search-index `route` values (which are root-relative).
  function sitePrefix() {
    var m = document.querySelector('meta[name="cti-site-prefix"]');
    return (m && m.getAttribute('content')) || '';
  }

  async function init() {
    wireThemeButtonTitle();
    wireMobileNavToggle();
    wireKeyboardShortcuts();
    wireCopyLinkButtons();
    await Promise.all([wireGlobalSearch(), wireGithubBadge(), wireListFilters()]);
  }

  // ── search ──────────────────────────────────────────────────────────

  async function wireGlobalSearch() {
    var input = document.getElementById('q');
    var ul = document.getElementById('suggestions');
    if (!input || !ul) return;

    var form = input.form;
    if (form) form.addEventListener('submit', function (e) { e.preventDefault(); });

    var index = null;
    var loading = null;
    function ensureIndex() {
      if (index) return Promise.resolve(index);
      if (loading) return loading;
      loading = fetch(sitePrefix() + 'data/search.json')
        .then(function (r) { return r.ok ? r.json() : []; })
        .then(function (j) { index = j || []; return index; })
        .catch(function () { index = []; return index; });
      return loading;
    }

    var active = -1;
    var current = [];

    function close() { ul.hidden = true; ul.innerHTML = ''; active = -1; current = []; }

    function open(results, q) {
      current = results;
      active = -1;
      if (!results.length) { close(); return; }
      var html = results.map(function (r, i) {
        return (
          '<li role="option" data-route="' + escapeAttr(r.route) + '" data-idx="' + i + '">'
          + '<span class="kind-pill">' + escapeHtml(r.kind) + '</span>'
          + '<div class="s-row">'
          + '<span class="s-title">' + (window.Search ? Search.highlight(r.title, q) : escapeHtml(r.title)) + '</span>'
          + (r.hint ? '<span class="s-hint">' + (window.Search ? Search.highlight(r.hint, q) : escapeHtml(r.hint)) + '</span>' : '')
          + '</div>'
          + '</li>'
        );
      }).join('');
      ul.innerHTML = html;
      ul.hidden = false;
    }

    function setActive(i) {
      var items = ul.querySelectorAll('li');
      items.forEach(function (el, idx) { el.setAttribute('aria-selected', idx === i ? 'true' : 'false'); });
      active = i;
      if (i >= 0 && items[i]) items[i].scrollIntoView({ block: 'nearest' });
    }

    function navigate(route) {
      // route is root-relative (e.g. 'briefs/2026-05-07/'); resolve via prefix.
      window.location.href = sitePrefix() + route;
    }

    input.addEventListener('input', async function () {
      var q = input.value.trim();
      if (!q) { close(); return; }
      var idx = await ensureIndex();
      if (!window.Search) { close(); return; }
      var results = window.Search.query(idx, q, { limit: 10 });
      open(results, q);
    });

    input.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { input.blur(); close(); return; }
      if (e.key === 'ArrowDown') { e.preventDefault(); if (current.length) setActive(Math.min(active + 1, current.length - 1)); return; }
      if (e.key === 'ArrowUp')   { e.preventDefault(); setActive(Math.max(active - 1, 0)); return; }
      if (e.key === 'Enter') {
        e.preventDefault();
        if (active >= 0 && current[active]) {
          navigate(current[active].route);
        } else if (current[0]) {
          navigate(current[0].route);
        }
        close();
      }
    });

    ul.addEventListener('mousedown', function (e) {
      var li = e.target.closest('li[data-route]');
      if (!li) return;
      e.preventDefault();
      navigate(li.dataset.route);
      close();
    });

    document.addEventListener('click', function (e) {
      if (!input.contains(e.target) && !ul.contains(e.target)) close();
    });
  }

  // ── github badge ────────────────────────────────────────────────────

  async function wireGithubBadge() {
    var link = document.getElementById('github-link');
    var stars = document.getElementById('github-stars');
    if (!link) return;
    try {
      var r = await fetch(sitePrefix() + 'data/site.json');
      if (!r.ok) return;
      var s = await r.json();
      var gh = s.github || {};
      if (gh.url) link.setAttribute('href', gh.url);
      if (stars && typeof gh.stars === 'number') {
        stars.textContent = formatStars(gh.stars);
        stars.hidden = false;
        link.title = 'View source on GitHub · ' + gh.stars + ' stars';
      }
    } catch (_) { /* fail open: icon-only is fine */ }
  }

  function formatStars(n) {
    if (n < 1000) return String(n);
    if (n < 10000) return (n / 1000).toFixed(1).replace(/\.0$/, '') + 'k';
    return Math.round(n / 1000) + 'k';
  }

  // ── theme button / mobile nav ───────────────────────────────────────

  function wireThemeButtonTitle() {
    // theme.js handles the click; this is just a no-op placeholder for
    // future tweaks.
  }

  function wireMobileNavToggle() {
    var btn = document.getElementById('nav-toggle');
    var bar = document.querySelector('.bar-inner');
    if (!btn || !bar) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', open ? 'false' : 'true');
      bar.classList.toggle('is-open', !open);
    });
  }

  function wireKeyboardShortcuts() {
    document.addEventListener('keydown', function (e) {
      var tag = (e.target.tagName || '').toUpperCase();
      var editable = tag === 'INPUT' || tag === 'TEXTAREA' || e.target.isContentEditable;
      if (e.key === '/' && !editable) {
        e.preventDefault();
        var input = document.getElementById('q');
        if (input) input.focus();
      }
    });
  }

  // ── copy-link button (brief page) ──────────────────────────────────

  function wireCopyLinkButtons() {
    document.querySelectorAll('button[data-action="share"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var url = window.location.href.split('#')[0];
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(url).then(function () {
            btn.textContent = 'Copied!';
            setTimeout(function () { btn.textContent = 'Copy link'; }, 1500);
          });
        }
      });
    });
  }

  // ── list-page filters (briefs / cves / topics / sources) ───────────

  function wireListFilters() {
    // 1. text-input + chip filters (briefs / topics / sources)
    document.querySelectorAll('[data-filter-input]').forEach(function (input) {
      input.addEventListener('input', function () { applyFilters(input.dataset.filterInput); });
    });
    document.querySelectorAll('[data-filter-chip]').forEach(function (chip) {
      chip.addEventListener('click', function () {
        var facet = chip.dataset.filterChip;
        // toggle: only one chip per facet active.
        document.querySelectorAll('[data-filter-chip="' + facet + '"]').forEach(function (c) {
          c.classList.remove('active');
        });
        chip.classList.add('active');
        // Determine the parent table/list scope from facet prefix:
        var scope = facet.startsWith('brief-') ? 'briefs'
                  : facet.startsWith('topic-') ? 'topics'
                  : facet.startsWith('source-') ? 'sources'
                  : null;
        if (scope) applyFilters(scope);
      });
    });
  }

  function applyFilters(scope) {
    var q = '';
    var input = document.querySelector('[data-filter-input="' + scope + '"]');
    if (input) q = (input.value || '').toLowerCase().trim();

    function chipValue(facet) {
      var c = document.querySelector('[data-filter-chip="' + facet + '"].active');
      return c ? c.dataset.value : 'all';
    }

    if (scope === 'briefs') {
      var kind = chipValue('brief-kind');
      document.querySelectorAll('[data-filter-list="briefs"] li').forEach(function (li) {
        var matchKind = kind === 'all' || li.dataset.briefKind === kind;
        var hay = li.dataset.briefHaystack || li.textContent.toLowerCase();
        var matchText = !q || hay.indexOf(q) >= 0;
        li.style.display = (matchKind && matchText) ? '' : 'none';
      });
    } else if (scope === 'cves') {
      // text-only filter on the CVEs table
      document.querySelectorAll('[data-filter-table="cves"] tbody tr').forEach(function (tr) {
        var hay = tr.textContent.toLowerCase();
        tr.style.display = (!q || hay.indexOf(q) >= 0) ? '' : 'none';
      });
    } else if (scope === 'topics') {
      var ttype = chipValue('topic-type');
      var tflag = chipValue('topic-flag');
      document.querySelectorAll('[data-filter-list="topics"] li').forEach(function (li) {
        var typ = li.dataset.topicType || '';
        var flags = (li.dataset.topicFlags || '').split(',').filter(Boolean);
        var matchType = ttype === 'all' || typ === ttype;
        var matchFlag = (tflag === 'all')
          || (tflag === 'multi' && !flags.some(function (f) { return f.indexOf('SINGLE-SOURCE') === 0; }))
          || (tflag !== 'multi' && tflag !== 'all' && flags.indexOf(tflag) >= 0);
        var hay = li.textContent.toLowerCase();
        var matchText = !q || hay.indexOf(q) >= 0;
        li.style.display = (matchType && matchFlag && matchText) ? '' : 'none';
      });
    } else if (scope === 'sources') {
      var cat = chipValue('source-cat');
      var stat = chipValue('source-status');
      document.querySelectorAll('[data-filter-table="sources"] tbody tr').forEach(function (tr) {
        var cats = (tr.dataset.sourceCats || '').split(',').filter(Boolean);
        var st = tr.dataset.sourceStatus || '';
        var matchCat = cat === 'all' || cats.indexOf(cat) >= 0;
        var matchStat = stat === 'all' || st === stat;
        var hay = tr.textContent.toLowerCase();
        var matchText = !q || hay.indexOf(q) >= 0;
        tr.style.display = (matchCat && matchStat && matchText) ? '' : 'none';
      });
    }
  }

  // CVE list page also reacts to its text input directly:
  document.addEventListener('DOMContentLoaded', function () {
    var input = document.querySelector('[data-filter-input="cves"]');
    if (input) input.addEventListener('input', function () { applyFilters('cves'); });
  });

  // ── helpers ─────────────────────────────────────────────────────────

  function escapeHtml(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }
  function escapeAttr(s) { return escapeHtml(s); }
})();
