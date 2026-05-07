/* theme.js — light/dark/system theme toggle.

   Reads `cti.briefs.theme` from localStorage and applies it to <html>
   before the rest of the SPA boots. Wires the topbar button to cycle
   system → light → dark → system on click. The CSS targets
   [data-theme="light"] / [data-theme="dark"] explicitly; absence of the
   attribute means "follow prefers-color-scheme".

   Loaded with `defer` like every other script, but its first job runs
   synchronously when the script body executes — that's before the SPA
   makes the first paint, so there is no flash of the wrong theme. */

(function () {
  'use strict';

  const KEY = 'cti.briefs.theme';
  const ORDER = ['system', 'light', 'dark'];

  function read() {
    try {
      const v = localStorage.getItem(KEY);
      return ORDER.includes(v) ? v : 'system';
    } catch (_) {
      return 'system';
    }
  }

  function write(v) {
    try { localStorage.setItem(KEY, v); } catch (_) {}
  }

  function apply(v) {
    const html = document.documentElement;
    if (v === 'light' || v === 'dark') html.setAttribute('data-theme', v);
    else html.removeAttribute('data-theme');
  }

  // Apply immediately on script execution (before paint).
  let current = read();
  apply(current);

  function cycle() {
    const i = ORDER.indexOf(current);
    current = ORDER[(i + 1) % ORDER.length];
    apply(current);
    write(current);
    syncButton();
  }

  function syncButton() {
    const btn = document.getElementById('theme-toggle');
    if (!btn) return;
    btn.dataset.theme = current;
    btn.title = 'Theme: ' + current + ' (click to change)';
    btn.setAttribute('aria-label', 'Theme: ' + current + ' (click to change)');
  }

  document.addEventListener('DOMContentLoaded', () => {
    syncButton();
    const btn = document.getElementById('theme-toggle');
    if (btn) btn.addEventListener('click', cycle);
  });

  window.Theme = { get: () => current, cycle };
})();
