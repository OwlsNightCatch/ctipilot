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
        html = await Render.home();
        // Home renders the latest daily brief inline — record that visit too.
        const latest = (Store.manifest.find((b) => b.kind === 'daily') || {}).name;
        if (latest) visitedBrief = latest;
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

  window.Router = {
    parseHash,
    buildHash,
    updateQuery,
    dispatch,
    boot() {
      window.addEventListener('hashchange', dispatch);
      window.addEventListener('popstate', dispatch);
    },
  };
})();
