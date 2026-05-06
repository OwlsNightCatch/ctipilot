/* store.js — central data cache. Loads JSON bundles produced by build.py and
   memoizes brief markdown fetches. All routes consume this store. */

(function () {
  'use strict';

  const Store = {
    /** Loaded data bundles. */
    site: null,
    manifest: null,   // [{name, kind, path, title, sections, tldr, cves, links, items, size, ...}]
    cves: null,       // {cves: [{id, title, primary_source_url, first_seen, last_seen, appearances}]}
    topics: null,     // {items: [{key, type, title, first_covered, last_covered, primary_source_url, briefs, appearances}]}
    sources: null,    // {sources: [{id, publisher, url, category, reliability, language, status, notes, appearances, ...}]}
    search: null,     // [{kind, id, title, hint, tags, route}]
    engagement: null, // {updated_at, by_brief: [{name, views_14d, uniques_14d}]} | null

    /** Lazily-fetched markdown by path. */
    _md: new Map(),

    /** Top-level load. Call once at boot. Resolves with { site, manifest, ... }. */
    async load() {
      if (this._loadPromise) return this._loadPromise;
      this._loadPromise = (async () => {
        const [site, manifest, cves, topics, sources, search, engagement] = await Promise.all([
          this._json('data/site.json'),
          this._json('data/manifest.json'),
          this._json('data/cves.json'),
          this._json('data/topics.json'),
          this._json('data/sources.json'),
          this._json('data/search.json'),
          this._json('data/engagement.json'),
        ]);
        this.site = site;
        this.manifest = manifest || [];
        this.cves = cves || { cves: [] };
        this.topics = topics || { items: [] };
        this.sources = sources || { sources: [] };
        this.search = search || [];
        this.engagement = engagement || null;
        return this;
      })();
      return this._loadPromise;
    },

    /** Fetch raw markdown for a brief path (e.g. "briefs/2026-05-06.md"). */
    async getMarkdown(path) {
      if (this._md.has(path)) return this._md.get(path);
      const p = (async () => {
        const res = await fetch(path);
        if (!res.ok) throw new Error(`Failed to load ${path}: ${res.status}`);
        return res.text();
      })();
      this._md.set(path, p);
      return p;
    },

    /** Lookup by id. */
    findBrief(name) {
      return this.manifest.find((b) => b.name === name);
    },
    findCve(id) {
      const want = id.toUpperCase();
      return this.cves.cves.find((c) => c.id === want);
    },
    findTopic(key) {
      return this.topics.items.find((t) => t.key === key);
    },
    findSource(id) {
      return this.sources.sources.find((s) => s.id === id);
    },

    /** Reverse lookup: which CVEs / topics / sources appear in a given brief. */
    cvesInBrief(name) {
      return this.cves.cves.filter((c) => c.appearances.includes(name));
    },
    topicsInBrief(name) {
      return this.topics.items.filter((t) => (t.briefs || []).includes(name));
    },
    sourcesInBrief(name) {
      return this.sources.sources.filter((s) => (s.appearances || []).includes(name));
    },

    /** Internal JSON fetch with helpful errors. */
    async _json(path) {
      try {
        const res = await fetch(path);
        if (!res.ok) throw new Error(`${path}: HTTP ${res.status}`);
        return await res.json();
      } catch (err) {
        console.error('Store load error:', err);
        return null;
      }
    },
  };

  window.Store = Store;
})();
