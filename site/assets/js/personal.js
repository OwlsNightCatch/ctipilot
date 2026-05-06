/* personal.js — strictly local, never-leaves-device "your reading history".
   Uses one localStorage key. Stores brief names + per-name visit counts +
   last-visited timestamp. No identifiers, no fingerprints, no network I/O.
   Honors "Do Not Track" — when DNT is set, the module silently no-ops. */

(function () {
  'use strict';

  const KEY = 'cti.briefs.personal.v1';
  const MAX_ENTRIES = 100;

  function dnt() {
    // Modern browsers expose navigator.doNotTrack === '1' or globalPrivacyControl.
    try {
      if (navigator.doNotTrack === '1') return true;
      if (window.globalPrivacyControl) return true;
    } catch (_) {}
    return false;
  }

  function load() {
    if (dnt()) return { entries: {} };
    try {
      const raw = localStorage.getItem(KEY);
      if (!raw) return { entries: {} };
      const parsed = JSON.parse(raw);
      if (!parsed || typeof parsed !== 'object' || !parsed.entries) return { entries: {} };
      return parsed;
    } catch (_) {
      return { entries: {} };
    }
  }

  function save(state) {
    if (dnt()) return;
    try {
      // Cap to MAX_ENTRIES, drop the oldest by last-visit.
      const items = Object.entries(state.entries);
      if (items.length > MAX_ENTRIES) {
        items.sort(([, a], [, b]) => (b.last || '').localeCompare(a.last || ''));
        state.entries = Object.fromEntries(items.slice(0, MAX_ENTRIES));
      }
      localStorage.setItem(KEY, JSON.stringify(state));
    } catch (_) {
      // Quota exhausted, private mode, etc. — silently degrade.
    }
  }

  function recordVisit(name) {
    if (!name || dnt()) return;
    const state = load();
    const cur = state.entries[name] || { count: 0, first: null, last: null, totalDwellMs: 0, lastDwellMs: 0 };
    cur.count = (cur.count || 0) + 1;
    cur.last = new Date().toISOString();
    if (!cur.first) cur.first = cur.last;
    state.entries[name] = cur;
    save(state);
  }

  /** Record dwell time spent on a brief in milliseconds. Sane bounds:
      < 1s is treated as a bounce and not stored; > 4h is treated as a
      forgotten tab and clipped to 4h. Aggregate dwell is per-device only;
      it never leaves localStorage. Honours DNT / GPC. */
  function recordDwell(name, ms) {
    if (!name || dnt() || !ms || typeof ms !== 'number') return;
    if (ms < 1000) return;
    const clipped = Math.min(ms, 4 * 60 * 60 * 1000);
    const state = load();
    const cur = state.entries[name] || { count: 0, first: null, last: null, totalDwellMs: 0, lastDwellMs: 0 };
    cur.totalDwellMs = (cur.totalDwellMs || 0) + clipped;
    cur.lastDwellMs = clipped;
    state.entries[name] = cur;
    save(state);
  }

  function recent(n) {
    const state = load();
    return Object.entries(state.entries)
      .map(([name, v]) => ({
        name,
        count: v.count || 0,
        first: v.first,
        last: v.last,
        totalDwellMs: v.totalDwellMs || 0,
        lastDwellMs: v.lastDwellMs || 0,
      }))
      .sort((a, b) => (b.last || '').localeCompare(a.last || ''))
      .slice(0, n || 5);
  }

  /** Format milliseconds as a compact "1h 4m" / "3m 21s" / "47s" string. */
  function formatDwell(ms) {
    if (!ms || ms < 1000) return '<1s';
    const sec = Math.floor(ms / 1000);
    if (sec < 60) return sec + 's';
    const min = Math.floor(sec / 60);
    if (min < 60) return min + 'm ' + (sec % 60) + 's';
    const hr = Math.floor(min / 60);
    return hr + 'h ' + (min % 60) + 'm';
  }

  function clear() {
    try { localStorage.removeItem(KEY); } catch (_) {}
  }

  function isEnabled() { return !dnt(); }

  window.Personal = { recordVisit, recordDwell, recent, clear, isEnabled, formatDwell };
})();
