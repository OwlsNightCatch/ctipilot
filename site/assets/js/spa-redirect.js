/* spa-redirect.js — convert legacy SPA hash routes to clean URLs.
 *
 * One-time bootstrap loaded only on the home page. Runs at script-load
 * time (not on DOMContentLoaded) so we can replace the URL before the
 * page paints any content. CSP-safe: external `<script src>`, not inline.
 *
 * Indexed `#/briefs/2026-05-07` → `briefs/2026-05-07/`
 * Indexed `#/cves/CVE-2026-0300` → `cves/CVE-2026-0300/`
 * Indexed `#/sources/<id>`        → `sources/<id>/`
 * Indexed `#/topics/<key>`        → `topics/<key>/`
 * Indexed `#/<route>`             → `<route>/`
 */
(function () {
  'use strict';
  var h = window.location.hash || '';
  if (!h) return;
  var m;
  m = h.match(/^#\/briefs\/(\d{4}-\d{2}-\d{2})$/);
  if (m) { window.location.replace('briefs/' + m[1] + '/'); return; }
  m = h.match(/^#\/briefs\/(\d{4}-W\d{2})$/);
  if (m) { window.location.replace('briefs/weekly/' + m[1] + '/'); return; }
  m = h.match(/^#\/cves\/(CVE-[0-9]+-[0-9]+)$/);
  if (m) { window.location.replace('cves/' + m[1] + '/'); return; }
  m = h.match(/^#\/sources\/(.+)$/);
  if (m) { window.location.replace('sources/' + decodeURIComponent(m[1]) + '/'); return; }
  m = h.match(/^#\/topics\/(.+)$/);
  if (m) { window.location.replace('topics/' + decodeURIComponent(m[1]) + '/'); return; }
  m = h.match(/^#\/(briefs|cves|topics|sources|ops|about)$/);
  if (m) { window.location.replace(m[1] + '/'); return; }
})();
