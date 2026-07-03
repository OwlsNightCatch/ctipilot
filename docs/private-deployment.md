# Private deployment

The stack runs unchanged as an **organization-internal** service: private
GitHub repository, the same routines and publishing chain, and the reader
site served by your own web server instead of GitHub Pages. This is the
supported mode for closed-source intelligence above TLP:CLEAR
(see [`intel/README.md`](../intel/README.md)).

## What changes, what doesn't

| Piece | Public (default) | Private |
|---|---|---|
| Repository | public | **private** (routines, auto-merge, compose workflows all work identically) |
| `config/org-profile.yaml` `deployment.visibility` | `public` | `private` |
| `deployment.site_url` | `https://ctipilot.ch/` | your internal URL, or `""` to skip site polling |
| Site hosting | GitHub Pages via `deploy-site.yml` | internal web server pulling + building on a schedule |
| Closed-source TLP ceiling (`check_run.py` gate) | TLP:CLEAR only | up to the drop file's marking |
| Routine phases | identical | identical — only Phase 7's site poll adapts to `site_url` |

`site/build.py` is stdlib-only and emits a fully static bundle into
`site/_site/` — no server-side code, so **any** static web server can host
it. All assets are vendored (strict CSP, no external requests), which means
the site works on an air-gapped network segment.

## Step-by-step

1. **Make the repository private** (or create a private fork/mirror your
   routines run against). Verify the scheduled Claude Code routines and the
   GitHub App still have access; `auto-merge-claude.yml`,
   `compose-profile.yml`, and `source-health.yml` keep working — Actions run
   fine on private repos (minutes are metered).
2. **Disable GitHub Pages publishing**: either disable Pages in the repo
   settings, or delete/disable `.github/workflows/deploy-site.yml` (it is
   the only Pages-specific piece; nothing else references it).
3. **Set the deployment profile** and compose:

   ```sh
   # config/org-profile.yaml
   # deployment:
   #   visibility: "private"
   #   site_url: "https://cti.intra.example.ch/"   # or "" to skip Phase 7 site polling
   python3 tools/compose_prompts.py --write && git add -A config prompts .claude && git commit
   ```

   `visibility: private` lifts the TLP:CLEAR ceiling on closed-source
   citations (the drop file's own marking becomes the limit) and tells the
   verifier to judge accordingly. An empty `site_url` makes the routine's
   Phase 7 report `publish: ok (main — site polling disabled)` after the
   auto-merge lands, instead of polling a site it cannot reach.
4. **Host the site internally — scheduled pull + build + serve.** On the
   internal web host:

   ```sh
   # /opt/ctipilot/refresh.sh — pull main, rebuild, atomically swap the webroot
   set -euo pipefail
   cd /opt/ctipilot/repo                       # git clone <repo-url> repo  (once)
   git fetch origin main && git reset --hard origin/main
   python3 site/build.py                        # writes site/_site/
   rsync -a --delete site/_site/ /var/www/ctipilot/
   ```

   Schedule it (systemd timer shown; cron works the same):

   ```ini
   # /etc/systemd/system/ctipilot-refresh.service
   [Service]
   Type=oneshot
   User=ctipilot
   ExecStart=/opt/ctipilot/refresh.sh

   # /etc/systemd/system/ctipilot-refresh.timer
   [Timer]
   OnCalendar=*:0/15          # every 15 min; entries land throughout the day
   Persistent=true
   [Install]
   WantedBy=timers.target
   ```

   Serve `/var/www/ctipilot/` with any static server. nginx example:

   ```nginx
   server {
     listen 443 ssl;
     server_name cti.intra.example.ch;
     root /var/www/ctipilot;
     index index.html;
     # Mirror the Pages behaviour: extensionless pretty URLs resolve to dirs.
     location / { try_files $uri $uri/ $uri/index.html =404; }
   }
   ```

   Quick local preview without a real server:
   `python3 -m http.server --directory site/_site 8080`.
5. **Access control** is the web server's job (VPN-only vhost, mTLS, SSO
   proxy — whatever your estate uses). The bundle itself is inert static
   HTML; there is nothing session-based to protect inside it.
6. **Ops dashboard included** — `/ops/` ships in the same bundle, so the
   operator view is available internally with no extra steps.

## Notes and sharp edges

- **The routine cannot verify your internal site.** With `site_url` set to
  an internal URL, the Anthropic-managed routine container generally cannot
  reach it; leave `site_url: ""` and treat "on `main`" as the routine's
  definition of published — the timer owns the last mile. If you point
  `site_url` at a URL the container *can* reach, Phase 7 polls it as usual.
- **Custom domain artefacts**: `CNAME` and `.nojekyll` are Pages-specific
  and harmless to keep; delete `CNAME` if you disable Pages to avoid
  confusion.
- **Feed scripts** (intel drops, source-health cron) need push access to the
  private repo — deploy keys or a machine PAT scoped to the repo.
- **Back to public**: flip `visibility` to `public`, recompose, re-enable
  `deploy-site.yml` — but first audit `intel/` and every published entry for
  above-CLEAR closed-source content: git history is forever once public.
