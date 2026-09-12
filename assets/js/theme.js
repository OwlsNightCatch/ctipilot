/* theme.js — reader display & accessibility preferences.

   Manages three <html> attributes, each persisted in localStorage and
   applied synchronously on script execution (before first paint, so no
   flash of the wrong state):

     data-theme     = "light" | "dark"     (absent → follow prefers-color-scheme)
     data-font      = "dyslexic"           (absent → default font)
     data-density   = "comfortable"        (absent → default line-height)

   Wires the display/accessibility popover + the mobile drawer copies:
     [data-theme-set="system|light|dark"]  segmented buttons
     [data-font-toggle]                     dyslexia-friendly switch
     [data-density-toggle]                  comfortable-spacing switch
*/
(function () {
  'use strict';

  var TKEY = 'ctipilot_theme', FKEY = 'ctipilot_font', DKEY = 'ctipilot_density';
  var THEMES = ['system', 'light', 'dark'];

  function ls(k, d) { try { var v = localStorage.getItem(k); return v == null ? d : v; } catch (_) { return d; } }
  function save(k, v) { try { localStorage.setItem(k, v); } catch (_) {} }

  var theme = ls(TKEY, 'system');
  if (THEMES.indexOf(theme) < 0) theme = 'system';
  var dys = ls(FKEY, '0') === '1';
  var comfy = ls(DKEY, '0') === '1';

  function apply() {
    var h = document.documentElement;
    if (theme === 'light' || theme === 'dark') h.setAttribute('data-theme', theme);
    else h.removeAttribute('data-theme');
    if (dys) h.setAttribute('data-font', 'dyslexic'); else h.removeAttribute('data-font');
    if (comfy) h.setAttribute('data-density', 'comfortable'); else h.removeAttribute('data-density');
  }

  // Apply immediately (before paint).
  apply();

  function sync() {
    document.querySelectorAll('[data-theme-set]').forEach(function (b) {
      b.classList.toggle('active', b.getAttribute('data-theme-set') === theme);
    });
    document.querySelectorAll('[data-font-toggle]').forEach(function (b) {
      b.setAttribute('aria-checked', dys ? 'true' : 'false');
      var sw = b.querySelector('.sw'); if (sw) sw.classList.toggle('on', dys);
    });
    document.querySelectorAll('[data-density-toggle]').forEach(function (b) {
      b.setAttribute('aria-checked', comfy ? 'true' : 'false');
      var sw = b.querySelector('.sw'); if (sw) sw.classList.toggle('on', comfy);
    });
  }

  function wire() {
    sync();
    document.querySelectorAll('[data-theme-set]').forEach(function (b) {
      b.addEventListener('click', function () {
        theme = b.getAttribute('data-theme-set'); save(TKEY, theme); apply(); sync();
      });
    });
    document.querySelectorAll('[data-font-toggle]').forEach(function (b) {
      b.addEventListener('click', function () { dys = !dys; save(FKEY, dys ? '1' : '0'); apply(); sync(); });
    });
    document.querySelectorAll('[data-density-toggle]').forEach(function (b) {
      b.addEventListener('click', function () { comfy = !comfy; save(DKEY, comfy ? '1' : '0'); apply(); sync(); });
    });
  }

  if (document.readyState !== 'loading') wire();
  else document.addEventListener('DOMContentLoaded', wire);

  window.Theme = { get: function () { return theme; } };
})();
