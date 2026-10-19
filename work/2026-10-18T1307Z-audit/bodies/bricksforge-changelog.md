---
title: Changelog – Bricksforge
url: https://bricksforge.io/version-changelog/
hostname: bricksforge.io
description: Here you will be informed about all changes and stay up to date.
sitename: Bricksforge – One Plugin. Countless Possibilities.
date: "2026-09-17"
fingerprint: "3e3898072cb1f200"
---
### 4.0.2

13\. October 2026

### Image uploads are no longer rejected by mistake

The upload check introduced in 4.0.1 could refuse a perfectly normal image, roughly one in sixty. Uploads behave normally again, while files that genuinely carry code are still rejected.

###### fix

### Security hardening across the REST endpoints

We reviewed every Bricksforge REST endpoint and tightened a number of them, covering form submissions, CAPTCHA verification, required-field validation, template rendering and media access. Access to form submissions now requires an editor-level account, and clearing the submissions table is reserved for administrators; both are adjustable by filter if your site delegates differently. Everything keeps working as before — these are tighter checks, not new restrictions on normal use.

###### fix

### Email Designer test mails are now restricted to administrators

Sending a test email from the Email Designer now requires an administrator account, like the rest of the designer. Nothing changes when you use it from the Bricksforge admin.

###### fix

### Stored API keys stay out of the front end

Credentials saved in the tool settings are filtered more thoroughly before anything reaches the front end. If you have stored API keys there, we recommend renewing them at your provider as a precaution.

###### fix

### Maintenance mode unlock is now verified

The unlock that maintenance mode grants after the password is entered is now tied to your password and your site. Entering the password works exactly as before; anyone who unlocked a site earlier simply enters it once more.

###### fix

### Creating user roles is restricted to administrators

Creating a user role through the Builder Customizer now requires an administrator, and a new role can never receive permissions beyond those of the person creating it.

###### fix

### Location conditions use the visitor address the server sees

The country behind a location condition is now determined from the address your server observes directly. If your site runs behind a proxy or CDN such as Cloudflare, name the header to trust with the bricksforge/conditional\_logic/trusted\_ip\_headers filter, otherwise visitors may appear to come from your proxy.

###### fix

### Login cookies stay on your own site in API Query Builder

The option that passes along WordPress cookies exists so a query can call your own site's REST API. It now applies only when the request actually goes to your site.

###### fix

### Temporary upload files are cleaned up reliably

The hourly clean-up of the Pro Forms temp folder is now kept scheduled automatically. On long-running sites it could previously be missing, leaving files in place.

###### fix

### Fewer notification emails when a form is hit by bots

Every failed submission sent an admin notification, so a bot hammering a form could fill your inbox overnight. You now get at most one notification per form per hour. The interval can be changed with the bricksforge/pro\_forms/admin\_notification\_interval filter.

###### improvement

### The Pro Forms temp folder protects itself

The temporary upload folder now always carries its own protection against anything being executed inside it.

###### improvement

### 4.0.1

8\. October 2026

### Security fix for the Pro Forms file upload

A security issue in the Pro Forms file upload has been fixed. It affects every site with Pro Forms active, including sites whose forms use no upload fields, so updating is strongly recommended. Forms with upload fields keep working exactly as before. Related: CVE-2026-85097, an arbitrary file upload in the same area that was fixed earlier in 3.1.8.10 and in 4.0.0.

###### fix

### 4.0.0

17\. September 2026

### \[Animation Panel\] New Image Sequence Studio

Create frame-by-frame and scroll-driven image sequence animations.

###### new

### \[API Query Builder\] New interface with advanced auth & CPT Sync

Advanced authentication (dynamic tokens and refresh flows), a full request builder with dynamic routes, plus CPT Sync to pull external API data into your own post types with webhooks, pagination and scheduling.

###### new

### \[Page Transitions\] Progress bar, debug mode, exclude rules & custom hooks

New progress bar, a debug mode, exclude rules and custom hooks.

###### new

### \[Animation Panel\] Split Text: new Mask option for reveal animations

Split Text animations now have a Mask setting. Pick lines, words or chars, and each of them gets wrapped in a clipping container — so text can slide in from outside without you adding overflow: hidden in your CSS. Left on None, everything behaves exactly as before.

###### new

### \[Pro Forms\] Sublabel for form fields

Form fields now have an optional Sublabel — a short description line shown between the label and the input. It comes with its own typography and margin settings under Global Field Styles, so you can style it independently from the label. Supports dynamic data and HTML, and screen readers announce it together with the field.

###### new

### \[Pro Forms\] Aria Label control for input fields

Every input field now has an optional Aria Label setting that outputs an aria-label on the field — improving screen-reader accessibility, especially when the visible label is hidden. Supports dynamic data.

###### new

### \[General\] Bricksforge is now its own top-level admin menu

Bricksforge moved out from under the Bricks menu into a dedicated top-level admin menu for more room and flexibility. The submenu now updates live when you activate or deactivate a tool — no reload needed.

###### new

### \[API Query Builder\] New Raw / Plain text body type for POST requests

The request body of a POST query could only be built from key/value pairs, which made endpoints with their own query language unusable — IGDB, for example, expects something like fields name,total\_rating; where id = 23248;. Body Type now offers Raw / Plain text: you type the body into a textarea and it is sent exactly as entered, with a Content-Type you can set yourself (text/plain by default). JSON and Form Data queries are untouched.

###### new

### \[Email Designer\] Completely reimagined

A rebuilt designer with ready-made starters, AI assistance, conditional logic and loops, variables, themes, dedicated breakpoints, a structure panel, undo/redo, WooCommerce email support and a built-in health check.

###### improvement

### \[Animation Panel\] Rebuilt from the ground up

Fully redesigned, with a rewritten rendering engine that runs far more efficiently and a real-time live preview that updates even while scrolling.

###### improvement

### \[General\] Completely redesigned settings backend

Every settings screen has been rebuilt from the ground up for a cleaner, faster and more consistent experience across the whole plugin.

###### improvement

### \[Backend Designer\] Redesigned with themes, import/export & Menu Editor

Rebuilt interface with themes and import/export, plus a new Menu Editor with folders — multi-select, custom icons and a visual picker.

###### improvement

### \[Node Editor\] Standalone visual-logic workspace

Redesigned grid canvas, a Structure panel with canvases and folders, and variables.

###### improvement

### \[Animation Panel & Node Editor\] Now two separate, focused tools

The Animation Panel and the Node Editor are no longer combined — each has its own dedicated workspace.

###### improvement

### \[Bricks\] Compatibility with Bricks 2.4

The toolbar icon, Terminal and Node Editor are updated for the redesigned Bricks 2.4 toolbar, while staying compatible with the previous Bricks version.

###### improvement

### \[General\] Bricksforge can now be translated

The plugin now ships a translation template (languages/bricksforge.pot) containing every string it displays, and all of those strings finally live under Bricksforge's own text domain. Translators can get started right away, and a finished translation dropped into wp-content/languages/plugins is picked up automatically. One side note: a few strings that Bricks happens to use as well ("Label", "Required", ...) came along with the Bricks translation until now. Until a Bricksforge translation exists for your language, they appear in English.

###### improvement

### \[Pro Forms\] The Honeypot field is now configurable

Until now every Honeypot rendered exactly the same markup on every site, which made it easy for bots to recognise and skip. You can now set its label, field name and input type, add your own wrapper and field classes, or switch off the default classes and hiding entirely to camouflage the field with your own CSS. Existing forms keep working as before.

###### improvement

### \[Pro Forms\] Turnstile, hCaptcha and Google Maps keys are inherited from the Bricks settings

If you already entered your Cloudflare Turnstile, hCaptcha or Google Maps API key in the Bricks settings, you no longer have to enter it a second time. Pro Forms now falls back to the Bricks key whenever the matching Bricksforge field is left empty. A key entered in Bricksforge always wins, so existing setups are unchanged.

###### improvement

### \[Animation Panel\] Cleaner exported code for a single animation

Exporting a timeline that holds just one animation produced a full gsap.timeline() wrapper around a single tween — boilerplate you had to unpick before you could use the code anywhere else. Such a timeline is now exported as the plain gsap.to() / gsap.from() / gsap.fromTo() call it really is, with the ScrollTrigger and the repeat, yoyo and delay settings moved onto the tween itself. Click and hover triggers still get their handle, and timelines with several animations, image sequences, Split Text or Batch mode are unchanged.

###### improvement

### \[Security\] Includes all hardening and fixes from the 3.x line

Bundles the latest security fixes (including the Pro Forms post-action hardening) so 4.0 doesn't regress them.

###### fix

### \[Email Designer\] Closed a privilege escalation through Twig in email content

Email bodies are rendered as Twig templates, and the Email Designer did that without a sandbox. Wherever part of a mail comes from a submitted form field — a confirmation mail, an admin notification, a WooCommerce mail — a crafted field value could reach the methods of the WordPress user object behind {{ user }}: it could raise the sender to administrator, or print the password hash into the mail, while the mail itself looked completely normal. Twig now runs sandboxed. Tags, filters and functions are limited to what an email needs, method calls are blocked, and {{ user }} carries plain data instead of the live user object — unknown fields still fall back to user meta. On top of that, template syntax inside a submitted field value is no longer executed: if a visitor types {{ ... }} or {% ... %} into a form field, it now appears in the mail as the text they typed. Templates that use variables, conditions, loops, filters or the built-in functions are unaffected. Reported by dutafi via Patchstack.

###### fix

### \[Pro Forms\] Card and Image choices now work with the keyboard

Card Radio, Card Checkbox, Image Radio and Image Checkbox hid their actual input completely, so you could not reach them with the Tab key and screen readers skipped them. The input is now only hidden visually: it can be focused and selected with the keyboard, and screen readers announce each choice together with its checked state. Your cards look exactly as before.

###### fix

### \[Pro Forms\] Multiple uploaded files are separated properly again in emails and submissions

Since 3.1.8.9, the links of a multi-file upload were joined without a space in notification emails and form submissions. Mail clients then turned all of them into one single, broken link. The files are listed as "a, b" again, like before. Values saved to post meta, user meta or sent to webhooks keep their current format.

###### fix

### \[Pro Forms\] {{all\_fields}} shows field labels instead of field IDs

For fields without a visible label, such as a Textarea, Select, Rich Text, Calculation or Map field, {{all\_fields}} listed the field ID in the email instead of its label. Checkbox and radio groups could even show the label of their first option. The label from the field settings is now used in these cases. Fields whose label is visible on the form show exactly what they did before.

###### fix

### \[Pro Forms\] Update Post Meta updates every post you target

If the Update Post Meta action contained rows for several different posts, all of them were written to the same post. Each row now updates the post it points to.

###### fix

### \[Pro Forms\] Rich Text fields keep their content when repeater rows change

In a form with a Repeater, adding or removing a row emptied every Rich Text field that uses the WordPress editor style. The content now stays where it is.

###### fix

### \[Builder\] No more empty column next to the Structure panel in Bricks 2.4

With Bricks 2.4, resizing the browser window could shrink the Structure panel and leave an empty column in the right sidebar. Bricksforge no longer touches the panel width, so the Structure panel keeps the size you gave it.

###### fix

### \[Builder\] Only one Bricksforge icon in the toolbar on Bricks 2.3 and older

On Bricks versions before 2.4, the old Bricksforge Panel icon showed up next to the new Bricksforge menu. The toolbar now shows a single Bricksforge icon on every Bricks version.

###### fix

### \[General\] Notices from other plugins no longer end up inside the Bricksforge welcome header

WordPress notices from other plugins, for example a cookie banner reminder, were placed in the middle of the welcome header on the Bricksforge settings page. They now appear above the page, styled to match.

###### fix

### \[Page Transitions\] Settings now behave the way the panel shows them

Some page transition options did not match what you set in the panel: an option you deliberately switched off could still end up active on the site, the cache setting differed between panel and frontend, and the \[data-no-swup\] attribute was ignored as long as both exclude fields were empty. All defaults now come from a single source, so a fresh install and a saved one behave the same. Links that open a PhotoSwipe lightbox are also left alone by the transition handler again.

###### fix

### \[Pro Forms\] The Map field icon now replaces the map marker

The Map field offered an Icon setting that did nothing. It is now called Marker Icon and replaces the default pin on OpenStreetMap and Google Maps, with its own size and color settings. Leave it empty to keep the default pin.

###### fix

### \[Pro Forms\] The Custom ID of a field now resolves dynamic data

The Custom ID of a form field offered dynamic data, but the tag ended up in the form as plain text. Inside a query loop every field therefore got the same name. The tag is now resolved, so each loop item gets its own field ID.

###### fix

### \[Dynamic Data\] brf\_post\_\* tags stay empty when their post ID is empty

Tags like 4.0.0 fell back to the current page when the post ID you passed resolved to nothing, for example a  that is missing from the URL. A form for creating posts could therefore show up prefilled with the title of the page it sits on. The tags now stay empty in that case. Without a post ID they still use the current post, as before.

###### fix

### \[Pro Forms\] Dynamic "Enable / Disable Dates" no longer breaks the form

Using a dynamic source for the enabled or disabled dates of a Date field could throw a fatal error in the classic form element. Fixed.

###### fix

### \[Pro Forms\] Sublabels now show their default styling

Sublabels always came with default styling, but chances are you never saw it. Bricksforge's frontend stylesheet was the only one whose address did not change when its contents did, so browsers kept handing out an older cached copy — and a sublabel showed up completely unstyled. The stylesheet now carries its own file version, so a changed style always reaches the site. The spacing has been tuned as well: the sublabel now sits close to its label and keeps a clear distance to the field, so the two read as one block instead of three separate lines. Everything stays adjustable under Global Field Styles.

###### fix

### \[Backend Designer\] Replace Howdy now works in every admin language

The greeting in the admin bar only changed when WordPress ran in US English. In any other language, including English (UK), it stayed untouched. Your replacement text now shows up regardless of the site or profile language.

###### fix

### \[Backend Designer\] The Form Submissions page is no longer recoloured

With the Backend Designer active, its page colours were applied to the Form Submissions page as well, which broke its layout. The page now keeps its own design, just like the Bricksforge settings.

###### fix

### \[Pro Forms\] The Date field's "Language" control now accepts dynamic data

Setting the Language of a Date field to a dynamic value kept the datepicker in English. The value is now evaluated, so the calendar shows up in the language you picked.

###### fix

### \[Pro Forms\] Modern Select: search placeholder and working keyboard on iOS

The search field of a searchable Modern Select stayed empty instead of showing a placeholder — there is now a dedicated Search Placeholder setting, and it falls back to the field placeholder. On iPhone and iPad the keyboard no longer stays hidden when you open the dropdown.

###### fix

### \[Pro Forms\] Map fields show their marker icons

The marker images of the Map field were missing from the plugin package, so the map tried to load icons that did not exist. They now ship with Bricksforge.

###### fix

### \[Email Designer\] The canvas previews images from the Image URL field

An Image element whose source was entered in the Image URL field kept showing a placeholder on the canvas, even though the sent email used the right image. The canvas now shows that image too.

###### fix

### \[Backend Designer\] The theme generator accepts colors with an alpha channel

Pasting a brand color with eight digits, such as #EDFF85FF from Figma, silently disabled the Generate button. Colors with an alpha channel are now accepted; the transparency is simply ignored for the palette.

###### fix

### \[Pro Forms\] The submit button loading icon spins in the right direction

While a form was being submitted, the loading icon rotated against the direction its arrows point. It now turns the way it should. A custom loading icon keeps its own direction.
