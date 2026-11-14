/* spa-redirect.js — convert legacy SPA hash routes to clean URLs.
 *
 * One-time bootstrap loaded only on the home page. Runs at script-load
 * time (not on DOMContentLoaded) so we can replace the URL before the
 * page paints any content. CSP-safe: external `<script src>`, not inline.
 *
 * Indexed `#/daily/2026-05-07` -> `daily/2026-05-07/`
 * Indexed `#/cves/CVE-2026-0300` -> `cves/CVE-2026-0300/`
 * Indexed `#/sources/<id>`        -> `sources/<id>/`
 * Indexed `#/topics/<key>`        -> `topics/<key>/`
 * Indexed `#/<route>`             -> `<route>/`
 */
(function () {
  'use strict';
  var h = window.location.hash || '';
  if (!h) return;
  var m;
  m = h.match(/^#\/daily\/(\d{4}-\d{2}-\d{2})$/);
  if (m) { window.location.replace('daily/' + m[1] + '/'); return; }
  m = h.match(/^#\/cves\/(CVE-[0-9]+-[0-9]+)$/);
  if (m) { window.location.replace('cves/' + m[1] + '/'); return; }
  m = h.match(/^#\/sources\/(.+)$/);
  if (m) { window.location.replace('sources/' + decodeURIComponent(m[1]) + '/'); return; }
  m = h.match(/^#\/topics\/(.+)$/);
  if (m) { window.location.replace('topics/' + decodeURIComponent(m[1]) + '/'); return; }
  m = h.match(/^#\/(live|daily|weekly|cves|topics|sources|ops|about)(?:\/.*)?$/);
  // The live brief renders at the site root now, and the weekly pages are
  // retired (2026-08-29): both land on the brief.
  if (m) { window.location.replace(m[1] === 'live' || m[1] === 'weekly' ? './' : m[1] + '/'); return; }
})();
