/* router.js — hash-based router. URLs:
       #/                     → home
       #/briefs               → briefs index
       #/briefs/<name>        → single brief (daily YYYY-MM-DD or weekly YYYY-Www)
       #/cves                 → CVE list
       #/cves/<id>            → CVE detail
       #/topics               → topics list
       #/topics/<key>         → topic detail (encoded)
       #/sources              → sources list
       #/sources/<id>         → source detail (encoded)
       #/search?q=...         → search results
       #/about                → about / docs

   Filter / search query is also pushed into the hash for shareable URLs:
       #/briefs?q=apache&kind=daily
       #/topics?q=copy+fail&type=cve
*/

(function () {
  'use strict';

  function parseHash() {
    const raw = window.location.hash || '#/';
    const cleaned = raw.startsWith('#') ? raw.slice(1) : raw;
    const [pathRaw, queryRaw] = cleaned.split('?');
    const path = (pathRaw || '/').split('/').filter(Boolean); // ['briefs','2026-05-06']
    const query = {};
    if (queryRaw) {
      for (const pair of queryRaw.split('&')) {
        if (!pair) continue;
        const [k, v] = pair.split('=');
        if (k) query[decodeURIComponent(k)] = decodeURIComponent((v || '').replace(/\+/g, ' '));
      }
    }
    return { path, query };
  }

  /** Build a hash URL from a route + query. */
  function buildHash(route, query) {
    const qs = query
      ? Object.entries(query)
          .filter(([_, v]) => v != null && String(v).length > 0)
          .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
          .join('&')
      : '';
    return '#' + route + (qs ? '?' + qs : '');
  }

  /** Update only the query part of the current hash without re-routing. */
  function updateQuery(query) {
    const { path } = parseHash();
    const route = '/' + path.join('/');
    const target = buildHash(route, query);
    if (target !== window.location.hash) {
      // Use replaceState so filter changes don't pollute history.
      history.replaceState(null, '', target);
    }
  }

  async function dispatch() {
    const { path, query } = parseHash();
    const view = document.getElementById('view');
    view.innerHTML = '<p class="loading">Loading…</p>';

    let html = '';
    let visitedBrief = null;
    try {
      if (path.length === 0) {
        // Redirect home → latest daily brief so the URL bar reflects what's
        // actually being read (and GitHub Pages logs a path-level view of
        // briefs/<name>.md when the SPA fetches the markdown). This is a
        // replaceState — the browser back button still goes to wherever
        // the visitor came from. Falls through to the Render.home empty
        // state if there are no daily briefs yet.
        const latest = (Store.manifest.find((b) => b.kind === 'daily') || {}).name;
        if (latest) {
          history.replaceState(null, '', '#/briefs/' + latest);
          // Re-route now that the path has changed. parseHash will see the
          // new hash. No infinite loop: dispatch always takes the briefs
          // branch on the next call.
          return dispatch();
        }
        html = await Render.home();
      } else if (path[0] === 'briefs') {
        if (path.length === 1) {
          html = Render.briefs({ q: query.q, filterKind: query.kind || 'all' });
        } else if (path[1] === 'weekly' && path[2]) {
          html = await Render.brief({ name: path[2] });
          visitedBrief = path[2];
        } else {
          html = await Render.brief({ name: path[1] });
          visitedBrief = path[1];
        }
      } else if (path[0] === 'cves') {
        if (path.length === 1) html = Render.cves({ q: query.q });
        else html = Render.cve({ id: decodeURIComponent(path[1]) });
      } else if (path[0] === 'topics') {
        if (path.length === 1) html = Render.topics({ q: query.q, filterType: query.type || 'all' });
        else html = Render.topic({ key: decodeURIComponent(path[1]) });
      } else if (path[0] === 'sources') {
        if (path.length === 1) {
          html = Render.sources({ q: query.q, filterCat: query.cat || 'all', filterStatus: query.status || 'all' });
        } else {
          html = Render.source({ id: decodeURIComponent(path[1]) });
        }
      } else if (path[0] === 'search') {
        html = Render.search({ q: query.q || '' });
      } else if (path[0] === 'about') {
        html = await Render.about();
      } else {
        html = Render.notFound();
      }
    } catch (e) {
      console.error('Route render failed:', e);
      html = `<div class="empty"><h1>Error</h1><p>${Render.esc(e.message)}</p><p><a href="#/">← back home</a></p></div>`;
    }

    view.innerHTML = html;
    document.title = inferTitle(path);
    highlightActiveNav(path[0] || 'home');
    window.scrollTo({ top: 0 });
    bindRouteHandlers(path, query);
    if (visitedBrief && window.Personal && Personal.isEnabled()) {
      try { Personal.recordVisit(visitedBrief); } catch (_) {}
    }
    // Dwell-time FSM. Entering a brief route starts the clock; leaving any
    // brief route flushes whatever was accrued. Re-entering the same brief
    // is a no-op.
    if (visitedBrief) startDwell(visitedBrief);
    else flushDwell();
  }

  function inferTitle(path) {
    const root = path[0];
    const map = {
      undefined: 'CTI Briefs',
      briefs: 'Briefs · CTI Briefs',
      cves: 'CVEs · CTI Briefs',
      topics: 'Topics · CTI Briefs',
      sources: 'Sources · CTI Briefs',
      search: 'Search · CTI Briefs',
      about: 'About · CTI Briefs',
    };
    if (root && path[1]) return `${decodeURIComponent(path[1])} · CTI Briefs`;
    return map[root] || 'CTI Briefs';
  }

  function highlightActiveNav(root) {
    document.querySelectorAll('.nav a').forEach((a) => {
      const dr = a.dataset.route;
      const match = (root === '' && dr === 'home') || dr === root;
      a.classList.toggle('active', !!match);
    });
  }

  /** Wire up filter chips and inline search inputs after each render. */
  function bindRouteHandlers(path, query) {
    const root = path[0] || '';

    // Filter chips with data-kind / data-type / data-cat / data-status
    document.querySelectorAll('[data-kind]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, kind: el.dataset.kind === 'all' ? undefined : el.dataset.kind }) || dispatch())
    );
    document.querySelectorAll('[data-type]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, type: el.dataset.type === 'all' ? undefined : el.dataset.type }) || dispatch())
    );
    document.querySelectorAll('[data-cat]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, cat: el.dataset.cat === 'all' ? undefined : el.dataset.cat }) || dispatch())
    );
    document.querySelectorAll('[data-status]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, status: el.dataset.status === 'all' ? undefined : el.dataset.status }) || dispatch())
    );

    // "Clear" link in the personal-history panel.
    document.querySelectorAll('[data-action="clear-personal"]').forEach((el) => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
        if (window.Personal) Personal.clear();
        dispatch();
      });
    });

    // Inline search input on list views: debounce, push q into URL.
    const inlineIds = ['briefs-q', 'cves-q', 'topics-q', 'sources-q', 'search-q'];
    for (const id of inlineIds) {
      const el = document.getElementById(id);
      if (!el) continue;
      let t;
      el.addEventListener('input', () => {
        clearTimeout(t);
        t = setTimeout(() => {
          updateQuery({ ...query, q: el.value || undefined });
          dispatch();
        }, 120);
      });
      // Restore caret to end of value after re-render
      el.focus();
      const len = el.value.length;
      try { el.setSelectionRange(len, len); } catch (_) {}
    }
  }

  /* Dwell-time tracking ------------------------------------------------

     One pending dwell session at a time, bound to the brief currently in
     view. State machine:

         enter brief X     →  startDwell(X)        : starts the clock
         leave brief X     →  flushDwell()         : commits to localStorage
         tab hidden        →  pause                : accumulate, stop clock
         tab visible again →  resume               : restart clock
         pagehide / unload →  flushDwell()         : last-chance commit

     Persisted only via Personal.recordDwell, which is DNT/GPC-aware and
     localStorage-only. No telemetry leaves the device.
  */
  let _dwellName = null;
  let _dwellStart = null;        // ms, null when paused
  let _dwellAccumulated = 0;     // ms accrued before the current segment

  function startDwell(name) {
    if (!name) return;
    if (_dwellName === name) {
      // already tracking this brief; if paused (tab was hidden), resume
      if (_dwellStart == null) _dwellStart = Date.now();
      return;
    }
    flushDwell();
    _dwellName = name;
    _dwellStart = Date.now();
    _dwellAccumulated = 0;
  }

  function flushDwell() {
    if (!_dwellName) return;
    let total = _dwellAccumulated;
    if (_dwellStart != null) total += Date.now() - _dwellStart;
    if (window.Personal && Personal.recordDwell) {
      try { Personal.recordDwell(_dwellName, total); } catch (_) {}
    }
    _dwellName = null;
    _dwellStart = null;
    _dwellAccumulated = 0;
  }

  function pauseDwell() {
    if (_dwellStart == null) return;
    _dwellAccumulated += Date.now() - _dwellStart;
    _dwellStart = null;
  }

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pauseDwell();
    else if (_dwellName && _dwellStart == null) _dwellStart = Date.now();
  });
  // pagehide is the cross-browser final-chance event (covers tab close,
  // navigation, BFCache freeze). beforeunload is unreliable on mobile.
  window.addEventListener('pagehide', flushDwell);

  window.Router = {
    parseHash,
    buildHash,
    updateQuery,
    dispatch,
    startDwell,    // exposed so dispatch() can drive the FSM
    flushDwell,
    boot() {
      window.addEventListener('hashchange', dispatch);
      window.addEventListener('popstate', dispatch);
    },
  };
})();
