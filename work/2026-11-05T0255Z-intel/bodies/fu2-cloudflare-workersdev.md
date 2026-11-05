---
title: workers.dev · Cloudflare Workers docs
url: https://developers.cloudflare.com/workers/configuration/routing/workers-dev/
hostname: cloudflare.com
description: Deploy Cloudflare Workers on a workers.dev subdomain for quick testing and personal projects.
sitename: Cloudflare Docs
date: "2026-09-22"
fingerprint: ec12733708f1d785
---
Cloudflare Workers accounts come with a `workers.dev` subdomain that is configurable in the Cloudflare dashboard. Your `workers.dev` subdomain allows you getting started quickly by deploying Workers without first onboarding your custom domain to Cloudflare.

It's recommended to run production Workers on a [Workers route or custom domain](https://developers.cloudflare.com/workers/configuration/routing/), rather than on your `workers.dev` subdomain. Your `workers.dev` subdomain is treated as a [Free website ↗︎](https://www.cloudflare.com/plans/) and is intended for personal or hobby projects that aren't business-critical.

`workers.dev` subdomains take the format: `<YOUR_ACCOUNT_SUBDOMAIN>.workers.dev`. To change your `workers.dev` subdomain:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.
	[Go to **Workers & Pages** ↗](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
2. Select **Change** next to **Your subdomain**.

All Workers are assigned a `workers.dev` route when they are created or renamed following the syntax `<YOUR_WORKER_NAME>.<YOUR_SUBDOMAIN>.workers.dev`. The [`name`](https://developers.cloudflare.com/workers/wrangler/configuration/#inheritable-keys) field in your Worker configuration is used as the subdomain for the deployed Worker.

When enabled, your `workers.dev` URL is available publicly. You can use [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) to require visitors to authenticate before accessing [Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/), [Preview URLs](https://developers.cloudflare.com/workers/previews/), and Deployment URLs. You can limit access to yourself, your teammates, your organization, or anyone else you specify in your [access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

Access can protect one Worker's production `workers.dev` URL, preview URLs, or both. You can also protect all Workers or all Worker previews in an account.

To use details about the signed-in user in your Worker, use [`ctx.access`](https://developers.cloudflare.com/workers/configuration/cloudflare-access/#read-authenticated-user-identity-with-ctxaccess). You can also read the [user's identity](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/#user-identity) from the validated JWT or the `/cdn-cgi/access/get-identity` endpoint.

To disable the `workers.dev` route for a Worker:

1. In the Cloudflare dashboard, go to the **Workers & Pages** page.
	[Go to **Workers & Pages** ↗](https://dash.cloudflare.com/?to=/:account/workers-and-pages)
2. In **Overview**, select your Worker.
3. Go to **Settings** > **Domains & Routes**.
4. On `workers.dev` click "Disable".
5. Confirm you want to disable.

To disable the `workers.dev` route for a Worker, include the following in your Worker's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):

When you redeploy your Worker with this change, the `workers.dev` route will be disabled. Disabling your `workers.dev` route does not disable [Version URLs](https://developers.cloudflare.com/workers/versions-and-deployments/version-urls/), [Preview URLs](https://developers.cloudflare.com/workers/previews/), or Deployment URLs.

If you do not specify `workers_dev = false` but add a [`routes` component](https://developers.cloudflare.com/workers/wrangler/configuration/#routes) to your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/), the value of `workers_dev` will be inferred as `false` on the next deploy.

When deploying a Worker with a `workers.dev` subdomain enabled, your Worker name must meet the following requirements:

- Must be 63 characters or less
- Must contain only alphanumeric characters (`a-z`, `A-Z`, `0-9`) and dashes (`-`)
- Cannot start or end with a dash (`-`)

These restrictions apply because the Worker name is used as a DNS label in your `workers.dev` URL. DNS labels have a maximum length of 63 characters and cannot begin or end with a dash.
