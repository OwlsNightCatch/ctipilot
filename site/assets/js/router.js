/* router.js — hash-based router. URLs:
       #/                     → home (preview of latest daily brief)
       #/briefs               → briefs index
       #/briefs/<name>        → single brief (full text; daily YYYY-MM-DD or weekly YYYY-Www)
       #/cves                 → CVE list
       #/cves/<id>            → CVE detail
       #/topics               → topics list
       #/topics/<key>         → topic detail (encoded)
       #/sources              → sources list
       #/sources/<id>         → source detail (encoded)
       #/ops                  → operations dashboard (run log + stale sources)
       #/search?q=...         → search results
       #/about                → about / docs

   Filter / search query is also pushed into the hash for shareable URLs:
       #/briefs?q=apache&kind=daily
       #/topics?q=copy+fail&type=cve&flag=SINGLE-SOURCE

   ?at=<anchor> — after render, scroll the matching #anchor into view.
   Used by section-level search results (S5) and the prompt-version badge.
*/

(function () {
  'use strict';

  function parseHash() {
    const raw = window.location.hash || '#/';
    const cleaned = raw.startsWith('#') ? raw.slice(1) : raw;
    const [pathRaw, queryRaw] = cleaned.split('?');
    const path = (pathRaw || '/').split('/').filter(Boolean);
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

  function buildHash(route, query) {
    const qs = query
      ? Object.entries(query)
          .filter(([_, v]) => v != null && String(v).length > 0)
          .map(([k, v]) => `${encodeURIComponent(k)}=${encodeURIComponent(v)}`)
          .join('&')
      : '';
    return '#' + route + (qs ? '?' + qs : '');
  }

  function updateQuery(query) {
    const { path } = parseHash();
    const route = '/' + path.join('/');
    const target = buildHash(route, query);
    if (target !== window.location.hash) {
      history.replaceState(null, '', target);
    }
  }

  function writeView(view, html) {
    view.innerHTML = html;
  }

  /** Update document.title, meta[name=description] and the OpenGraph
      equivalents to match the current route. Helps both link-preview
      and search engines treat each route as its own page even though
      we're a hash-routed SPA. */
  function setMeta({ title, description }) {
    if (title) document.title = title;
    const ensureMeta = (selector, attr, value) => {
      const el = document.head.querySelector(selector);
      if (!el || value == null) return;
      el.setAttribute(attr, value);
    };
    if (description) {
      ensureMeta('meta[name="description"]', 'content', description);
      ensureMeta('meta[property="og:description"]', 'content', description);
      ensureMeta('meta[name="twitter:description"]', 'content', description);
    }
    if (title) {
      ensureMeta('meta[property="og:title"]', 'content', title);
      ensureMeta('meta[name="twitter:title"]', 'content', title);
    }
    // Canonical: include the current hash so each route has a distinct URL.
    const link = document.head.querySelector('link[rel="canonical"]');
    if (link) {
      const base = (link.dataset.base || link.getAttribute('href') || '').replace(/#.*/, '').replace(/\/$/, '');
      if (!link.dataset.base) link.dataset.base = base;
      link.setAttribute('href', base + '/' + (window.location.hash || ''));
    }
    const og = document.head.querySelector('meta[property="og:url"]');
    if (og) og.setAttribute('content', window.location.href);
  }

  async function dispatch() {
    const { path, query } = parseHash();
    const view = document.getElementById('view');
    writeView(view, '<p class="loading">Loading…</p>');

    let html = '';
    try {
      if (path.length === 0) {
        html = await Render.home();
      } else if (path[0] === 'briefs') {
        if (path.length === 1) {
          html = Render.briefs({ q: query.q, filterKind: query.kind || 'all' });
        } else if (path[1] === 'weekly' && path[2]) {
          html = await Render.brief({ name: path[2] });
        } else {
          html = await Render.brief({ name: path[1] });
        }
      } else if (path[0] === 'cves') {
        if (path.length === 1) html = Render.cves({ q: query.q });
        else html = Render.cve({ id: decodeURIComponent(path[1]) });
      } else if (path[0] === 'topics') {
        if (path.length === 1) html = Render.topics({ q: query.q, filterType: query.type || 'all', filterFlag: query.flag || 'all' });
        else html = Render.topic({ key: decodeURIComponent(path[1]) });
      } else if (path[0] === 'sources') {
        if (path.length === 1) {
          html = Render.sources({ q: query.q, filterCat: query.cat || 'all', filterStatus: query.status || 'all' });
        } else {
          html = Render.source({ id: decodeURIComponent(path[1]) });
        }
      } else if (path[0] === 'ops') {
        html = await Render.ops();
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

    writeView(view, html);
    setMeta(inferMeta(path, query));
    highlightActiveNav(path[0] || 'home');
    closeMobileNav();
    bindRouteHandlers(path, query);
    trackPageview();

    // Scroll behaviour: if ?at=anchor is in the hash, jump there; else top.
    if (query.at) {
      // Two-step scroll because <details>-wrapped sections expand on click.
      const target = document.getElementById(query.at);
      if (target) {
        const det = target.closest('details');
        if (det) det.open = true;
        target.scrollIntoView({ block: 'start' });
      } else {
        window.scrollTo({ top: 0 });
      }
    } else {
      window.scrollTo({ top: 0 });
    }
  }

  function inferMeta(path, query) {
    const root = path[0];
    const SUFFIX = ' · CTI Briefs';
    const desc = (s) => `${s} — daily and weekly cyber threat intelligence briefing covering Switzerland, Europe, and the public sector. Source-linked, IOC-free, autonomously generated.`;

    if (!root) return {
      title: 'CTI Briefs — Daily cyber threat intelligence for Switzerland, Europe & the public sector',
      description: desc('Latest CTI briefs'),
    };
    if (root === 'briefs' && path[1]) {
      const name = decodeURIComponent(path[1] === 'weekly' ? path[2] || '' : path[1]);
      const brief = window.Store && Store.findBrief && Store.findBrief(name);
      if (brief) {
        const tldr = (brief.tldr || []).slice(0, 2).map((s) => s.replace(/\([^)]*\)/g, '').replace(/[*_`]/g, '').trim()).join(' ');
        return {
          title: brief.title + SUFFIX,
          description: tldr ? tldr.slice(0, 280) : desc(brief.title),
        };
      }
      return { title: name + SUFFIX, description: desc(name) };
    }
    if (root === 'cves' && path[1]) {
      const id = decodeURIComponent(path[1]);
      const cve = window.Store && Store.findCve && Store.findCve(id);
      const title = (cve && cve.title) || id;
      return { title: id + ' — ' + title + SUFFIX, description: title };
    }
    if (root === 'topics' && path[1]) {
      const key = decodeURIComponent(path[1]);
      const t = window.Store && Store.findTopic && Store.findTopic(key);
      const title = (t && t.title) || key;
      return { title: title + SUFFIX, description: 'Tracked topic: ' + title };
    }
    if (root === 'sources' && path[1]) {
      const id = decodeURIComponent(path[1]);
      const s = window.Store && Store.findSource && Store.findSource(id);
      const title = (s && s.publisher) || id;
      return { title: title + SUFFIX, description: 'Source: ' + title };
    }
    const map = {
      briefs: 'All briefs',
      cves: 'CVEs referenced across briefs',
      topics: 'Tracked topics across briefs',
      sources: 'Curated source list',
      ops: 'Operations dashboard',
      search: query.q ? `Search results for "${query.q}"` : 'Search',
      about: 'About this newsletter',
    };
    const label = map[root] || 'CTI Briefs';
    return { title: label + SUFFIX, description: desc(label) };
  }

  function highlightActiveNav(root) {
    document.querySelectorAll('.nav a').forEach((a) => {
      const dr = a.dataset.route;
      const match = (root === '' && dr === 'home') || dr === root;
      a.classList.toggle('active', !!match);
    });
  }

  function closeMobileNav() {
    const bar = document.querySelector('.bar-inner');
    const toggle = document.getElementById('nav-toggle');
    if (bar) bar.classList.remove('is-open');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
  }

  /** Tell Umami the current "page" changed.

      Umami's auto-tracker hooks into the History API (`pushState` /
      `popstate`); it does NOT fire on `hashchange`. Our SPA is
      hash-routed (`#/briefs/foo`), so without this manual call only
      the initial page load would be recorded and every subsequent
      navigation would be invisible in the dashboard. We call this
      after every router dispatch.

      `umami.track()` with no args sends a default pageview payload
      using the current `location.href` and `document.title` (already
      updated by `setMeta()` above). If Umami isn't loaded — script
      blocked, host unreachable, or the visitor's browser sent DNT and
      our `data-do-not-track="true"` flag silenced the tracker — this
      is a silent no-op. */
  let _lastTrackedUrl = null;
  function trackPageview() {
    try {
      if (typeof window.umami === 'undefined' || typeof window.umami.track !== 'function') {
        // Surface ONCE so the operator can debug missing analytics in the console.
        if (!trackPageview._warned) {
          trackPageview._warned = true;
          // eslint-disable-next-line no-console
          console.info('[umami] window.umami is not available. Likely causes: tracker script blocked by an ad-blocker / Brave Shields / browser privacy extension, or cloud.umami.is is unreachable. Run `window.checkUmami()` for a full diagnostic.');
        }
        return;
      }
      // hashchange + popstate both fire on hash navigation — only count
      // once per actual URL change.
      if (window.location.href === _lastTrackedUrl) return;
      _lastTrackedUrl = window.location.href;
      window.umami.track();
      // eslint-disable-next-line no-console
      if (window.__ctibriefsDebugUmami) console.info('[umami] tracked', window.location.href);
    } catch (_) {
      // never let analytics break navigation
    }
  }

  function showToast(text) {
    let el = document.getElementById('toast');
    if (!el) {
      el = document.createElement('div');
      el.id = 'toast';
      el.className = 'toast';
      el.setAttribute('role', 'status');
      document.body.appendChild(el);
    }
    el.textContent = text;
    el.classList.add('show');
    clearTimeout(showToast._t);
    showToast._t = setTimeout(() => el.classList.remove('show'), 1500);
  }

  /** Wire up filter chips, share button, and inline search inputs after each render. */
  function bindRouteHandlers(path, query) {
    document.querySelectorAll('[data-kind]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, kind: el.dataset.kind === 'all' ? undefined : el.dataset.kind }) || dispatch())
    );
    document.querySelectorAll('[data-type]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, type: el.dataset.type === 'all' ? undefined : el.dataset.type }) || dispatch())
    );
    document.querySelectorAll('[data-flag]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, flag: el.dataset.flag === 'all' ? undefined : el.dataset.flag }) || dispatch())
    );
    document.querySelectorAll('[data-cat]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, cat: el.dataset.cat === 'all' ? undefined : el.dataset.cat }) || dispatch())
    );
    document.querySelectorAll('[data-status]').forEach((el) =>
      el.addEventListener('click', () => updateQuery({ ...query, status: el.dataset.status === 'all' ? undefined : el.dataset.status }) || dispatch())
    );

    // Share / copy-permalink
    document.querySelectorAll('[data-action="share"]').forEach((el) => {
      el.addEventListener('click', async () => {
        const url = window.location.href;
        try {
          await navigator.clipboard.writeText(url);
          showToast('Permalink copied');
        } catch (_) {
          // Fallback: highlight the URL bar
          window.prompt('Copy this URL', url);
        }
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
      el.focus();
      const len = el.value.length;
      try { el.setSelectionRange(len, len); } catch (_) {}
    }
  }

  /** Mobile hamburger menu — toggles a class on .bar-inner that the CSS uses
      to drop the nav into a panel below the topbar. Closes on route change
      (handled by closeMobileNav after dispatch) and on outside click. */
  function wireNavToggle() {
    const toggle = document.getElementById('nav-toggle');
    const bar = document.querySelector('.bar-inner');
    if (!toggle || !bar) return;
    toggle.addEventListener('click', () => {
      const open = bar.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', (e) => {
      if (!bar.contains(e.target)) closeMobileNav();
    });
    // Close on Escape.
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeMobileNav();
    });
  }

  window.Router = {
    parseHash,
    buildHash,
    updateQuery,
    dispatch,
    boot() {
      window.addEventListener('hashchange', dispatch);
      window.addEventListener('popstate', dispatch);
      wireNavToggle();
    },
  };
})();
