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
    wireMdSplitButtons();
    wireSectionCollapse();
    wireOpsRunPicker();
    wireOpsPagers();
    await Promise.all([wireGlobalSearch(), wireGithubBadge(), wireListFilters()]);
  }

  // ── ops dashboard: generic table pager ─────────────────────────────
  // Any [data-ops-pager] container with a <tbody data-pager-rows> is
  // paginated client-side: default page size from data-pagesize (10),
  // optional [data-pager-size] <select> (e.g. 10/35/50/100), and
  // [data-pager-prev] / [data-pager-next] / [data-pager-status] controls
  // inside a [data-pager-bar] (hidden until JS reveals it, so the no-JS
  // fallback is the full, unpaginated table). Used by the run-log table
  // and every per-run "Sources changed" table. Each container is wired
  // independently, so many pagers on one page (one per run panel) is fine.
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
        var start = (page - 1) * pageSize;
        var end = Math.min(start + pageSize, total);
        for (var i = 0; i < rows.length; i++) {
          rows[i].style.display = (i >= start && i < end) ? '' : 'none';
        }
        if (status) {
          status.textContent = total === 0
            ? '0 of 0'
            : (start + 1) + '–' + end + ' of ' + total + ' · page ' + page + '/' + pages;
        }
        if (prev) prev.disabled = (page <= 1);
        if (next) next.disabled = (page >= pages);
      }

      if (bar) bar.hidden = false; // controls only make sense with JS
      if (sizeSel) sizeSel.addEventListener('change', function () { page = 1; render(); });
      if (prev) prev.addEventListener('click', function () { if (page > 1) { page--; render(); } });
      if (next) next.addEventListener('click', function () {
        var pages = Math.max(1, Math.ceil(total / curSize()));
        if (page < pages) { page++; render(); }
      });
      render();
    });
  }

  // ── ops dashboard: run-detail picker ───────────────────────────────
  // The /ops/ "Run detail" cluster renders one .ops-run-panel per run in
  // the window; #ops-run-select toggles which is visible. No-ops on every
  // other page (the select is absent). Deep-linkable via `#run=<key>` so a
  // specific run can be shared; on load that run is selected if present.
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
      if (window.history && history.replaceState) {
        history.replaceState(null, '', '#run=' + encodeURIComponent(sel.value));
      }
    });

    var m = (window.location.hash || '').match(/run=([^&]+)/);
    if (m) {
      var key = decodeURIComponent(m[1]);
      if (show(key)) sel.value = key;
    }
  }

  // ── collapsible H2 sections (brief pages) ──────────────────────────
  // Each <section class="brief-section"> carries a chevron toggle inside
  // its H2 with `data-section-collapse-toggle="<anchor>"`. Clicking the
  // chevron toggles `.section-collapsed` on the section AND mirrors the
  // state into the TOC eye toggle (`[data-section-toggle="<anchor>"]`)
  // so both views stay in sync. The TOC eye toggle is bound by
  // filter.min.js — its click handler already fires `applyFilters()`
  // which sets `.section-collapsed` and updates the chevron's
  // `aria-expanded`. This handler covers the reverse direction.
  function wireSectionCollapse() {
    var chevrons = document.querySelectorAll('[data-section-collapse-toggle]');
    if (!chevrons.length) return;
    chevrons.forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var anchor = btn.getAttribute('data-section-collapse-toggle');
        var section = document.getElementById(anchor);
        if (!section) return;
        var nowCollapsed = !section.classList.contains('section-collapsed');
        section.classList.toggle('section-collapsed', nowCollapsed);
        btn.setAttribute('aria-expanded', nowCollapsed ? 'false' : 'true');
        // Mirror state to every TOC eye toggle (desktop + mobile aside copies).
        var eyeToggles = document.querySelectorAll(
          '[data-section-toggle="' + anchor.replace(/"/g, '\\"') + '"]'
        );
        eyeToggles.forEach(function (eye) {
          // eye `aria-pressed=true` means "section visible"; pressed=false means "collapsed".
          eye.setAttribute('aria-pressed', nowCollapsed ? 'false' : 'true');
        });
        // Mirror the strikethrough state on the TOC row.
        document.querySelectorAll('[data-section-row="' + anchor.replace(/"/g, '\\"') + '"]')
          .forEach(function (row) {
            row.classList.toggle('toc-row-hidden', nowCollapsed);
          });
      });
    });
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

  // ── md split-button (brief page) ───────────────────────────────────

  function wireMdSplitButtons() {
    var roots = document.querySelectorAll('[data-md-split]');
    if (!roots.length) return;

    function flashPrimary(root, msg) {
      var label = root.querySelector('.md-split__primary .md-split__label');
      if (!label) return;
      var prev = label.textContent;
      label.textContent = msg;
      setTimeout(function () { label.textContent = prev; }, 1500);
    }

    function closeMenu(root) {
      var caret = root.querySelector('.md-split__caret');
      var menu = root.querySelector('.md-split__menu');
      if (!caret || !menu) return;
      caret.setAttribute('aria-expanded', 'false');
      menu.hidden = true;
    }

    function closeAllMenus() {
      roots.forEach(closeMenu);
    }

    function copyMarkdown(rawUrl, root) {
      if (!rawUrl) return;
      fetch(rawUrl, { credentials: 'same-origin' })
        .then(function (r) { return r.ok ? r.text() : Promise.reject(new Error('http ' + r.status)); })
        .then(function (text) {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            return navigator.clipboard.writeText(text);
          }
          return Promise.reject(new Error('no clipboard'));
        })
        .then(function () { flashPrimary(root, 'Copied!'); })
        .catch(function () { window.open(rawUrl, '_blank', 'noopener'); });
    }

    function copyLink(root) {
      var url = window.location.href.split('#')[0];
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function () { flashPrimary(root, 'Link copied!'); });
      }
    }

    roots.forEach(function (root) {
      var caret = root.querySelector('.md-split__caret');
      var menu = root.querySelector('.md-split__menu');

      if (caret && menu) {
        caret.addEventListener('click', function (e) {
          e.stopPropagation();
          var open = caret.getAttribute('aria-expanded') === 'true';
          closeAllMenus();
          if (!open) {
            caret.setAttribute('aria-expanded', 'true');
            menu.hidden = false;
          }
        });
      }

      root.querySelectorAll('[data-action]').forEach(function (el) {
        el.addEventListener('click', function (e) {
          var action = el.getAttribute('data-action');
          if (action === 'copy-md') {
            e.preventDefault();
            copyMarkdown(el.getAttribute('data-raw-url'), root);
          } else if (action === 'share') {
            e.preventDefault();
            copyLink(root);
          }
          if (el.getAttribute('role') === 'menuitem') closeMenu(root);
        });
      });

      root.querySelectorAll('a[role="menuitem"]').forEach(function (a) {
        a.addEventListener('click', function () { closeMenu(root); });
      });
    });

    document.addEventListener('click', function (e) {
      var inside = e.target.closest && e.target.closest('[data-md-split]');
      if (!inside) closeAllMenus();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var anyOpen = false;
      roots.forEach(function (root) {
        var caret = root.querySelector('.md-split__caret');
        if (caret && caret.getAttribute('aria-expanded') === 'true') {
          anyOpen = true;
          closeMenu(root);
          caret.focus();
        }
      });
      if (anyOpen) e.stopPropagation();
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
        var siblings = document.querySelectorAll('[data-filter-chip="' + facet + '"]');
        // Boolean-flag facets (no "All" companion in the sibling set) act as
        // toggle-on / toggle-off — clicking the active chip again clears it.
        // Multi-value facets (cat / status / kind) still behave as a radio:
        // exactly one chip per facet is active at all times.
        var hasAllCompanion = false;
        siblings.forEach(function (c) {
          if (c.dataset.value === 'all') hasAllCompanion = true;
        });
        if (!hasAllCompanion) {
          // Toggle this chip on/off without disturbing siblings.
          chip.classList.toggle('active');
        } else {
          siblings.forEach(function (c) { c.classList.remove('active'); });
          chip.classList.add('active');
        }
        // Determine the parent table/list scope from facet prefix:
        var scope = facet.startsWith('brief-') ? 'briefs'
                  : facet.startsWith('topic-') ? 'topics'
                  : facet.startsWith('source-') ? 'sources'
                  : facet.startsWith('entity-') ? 'entities'
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
      // Boolean-flag chip (toggle on/off, no "All" companion). Active =
      // show only stale-active rows; inactive = show every row.
      var staleChip = document.querySelector('[data-filter-chip="source-stale"].active');
      var staleOnly = !!staleChip;
      document.querySelectorAll('[data-filter-table="sources"] tbody tr').forEach(function (tr) {
        var cats = (tr.dataset.sourceCats || '').split(',').filter(Boolean);
        var st = tr.dataset.sourceStatus || '';
        var stale = tr.dataset.sourceStale || 'no';
        var matchCat = cat === 'all' || cats.indexOf(cat) >= 0;
        var matchStat = stat === 'all' || st === stat;
        var matchStale = !staleOnly || stale === 'yes';
        var hay = tr.textContent.toLowerCase();
        var matchText = !q || hay.indexOf(q) >= 0;
        tr.style.display = (matchCat && matchStat && matchStale && matchText) ? '' : 'none';
      });
    } else if (scope === 'entities') {
      var etype = chipValue('entity-type');
      document.querySelectorAll('[data-filter-list="entities"] li').forEach(function (li) {
        var typ = li.dataset.entityType || '';
        var matchType = etype === 'all' || typ === etype;
        var hay = li.textContent.toLowerCase();
        var matchText = !q || hay.indexOf(q) >= 0;
        li.style.display = (matchType && matchText) ? '' : 'none';
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
