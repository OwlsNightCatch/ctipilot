---
title: "fix(security): [develop] harden user settings validation, Guest writes, and realtime graph access by somethingwithproof · Pull Request #9015 · Cacti/cacti"
url: https://github.com/Cacti/cacti/pull/9015
hostname: github.com
description: Summary Hardens user-preference validation, Guest account write restrictions, tree pagination bounds, and realtime graph access control on develop (companion to the 1.2.x security hardening PR; lea...
sitename: GitHub
date: "2026-11-28"
categories: ['pull_request:5535209490']
fingerprint: d0dec8b945b9d7fc
language: en
image: https://opengraph.githubassets.com/6d9f43834d5e9390892df65aa3ac61cee258021b04ccf240a0b398c8700f0bd3/Cacti/cacti/pull/9015
pagetype: object
filedate: "2026-11-28"
---
## Repository navigation

# fix(security): \[develop\] harden user settings validation, Guest writes, and realtime graph access - #9015

Merged

[TheWitness](https://github.com/TheWitness)merged 2 commits into

## Conversation

…me graph access
Validate user preference values against $settings\_user field schemas in
auth\_profile.php and save\_user\_settings(), enforce POST on profile save
and update\_data actions, and reject Guest account mutations across
profile, 2FA, and realtime endpoints.
Validate tree pagination and numeric user settings before SQL LIMIT and
JavaScript output in lib/html\_tree.php.
Enforce is\_graph\_allowed() before realtime poller execution and cache
reads in graph\_realtime.php, anchor the graph\_nolegend regex, and clamp
realtime intervals before shell execution.
Signed-off-by: Thomas Vincent \<thomasvincent@gmail.com>

[somethingwithproof](https://github.com/somethingwithproof)requested review from

[cigamit](https://github.com/cigamit)and removed request for a team

[November 28, 2026 01:06](https://github.com/Cacti/cacti/pull/9015#event-37521731998)

…8n messages
Use existing 'Permission Denied' message in auth\_profile.php and raw
'GRAPH ACCESS DENIED' token in graph\_realtime.php so locales/po/cacti.pot
stays in sync without template churn.
Minimize indentation churn in auth\_profile.php and graph\_realtime.php,
load user\_setting\_validation.php via CACTI\_PATH\_LIBRARY in
save\_user\_settings(), and add UserSettingsAndRealtimeHardening fixture
coverage probes for PR changed-code coverage gates.
Signed-off-by: Thomas Vincent \<thomasvincent@gmail.com>

| **Quality Gate passed** Issues  [0 New issues](https://sonarcloud.io/project/issues?id=Cacti_cacti&pullRequest=9015&issueStatuses=OPEN,CONFIRMED&sinceLeakPeriod=true)  [0 Accepted issues](https://sonarcloud.io/project/issues?id=Cacti_cacti&pullRequest=9015&issueStatuses=ACCEPTED) Measures  [0 Security Hotspots](https://sonarcloud.io/project/security_hotspots?id=Cacti_cacti&pullRequest=9015&issueStatuses=OPEN,CONFIRMED&sinceLeakPeriod=true)  [0.0% Coverage on New Code](https://sonarcloud.io/component_measures?id=Cacti_cacti&pullRequest=9015&metric=new_coverage&view=list)  [0.0% Duplication on New Code](https://sonarcloud.io/component_measures?id=Cacti_cacti&pullRequest=9015&metric=new_duplicated_lines_density&view=list) [See analysis details on SonarQube Cloud](https://sonarcloud.io/dashboard?id=Cacti_cacti&pullRequest=9015) | 


**[TheWitness](https://github.com/TheWitness)**
    
              approved these changes

[Nov 28, 2026](https://github.com/Cacti/cacti/pull/9015#pullrequestreview-6094883752)
                  

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Hardens user-preference validation, Guest account write restrictions, tree pagination bounds, and realtime graph access control on `develop` (companion to the `1.2.x` security hardening PR; leaves `lib/html_graph.php` untouched since `ae54a2a55` already validates preview pagination on `develop`).

## Changes

User-setting schema validation (`lib/user_setting_validation.php`, `auth_profile.php`, `lib/functions.php`):`$settings_user`field definitions (`checkbox`,`drop_array`,`themes`,`drop_language`,`drop_sql`,`drop_color`, numeric/time`textbox`, and`font`) plus Guest-account and numeric/interval sanitization helpers.`auth_profile_require_post()`on`save`and`update_data`.`save`,`logout_everywhere`,`clear_user_settings`,`reset_default`,`update_data`,`disable_2fa`,`enable_2fa`,`verify_2fa`) and returns early in`save_user_settings()`.`is_view_allowed('graph_settings')`and schema validation (HTTP 400 on invalid values) in`api_auth_update_user_setting()`.Tree pagination and numeric settings (`lib/html_tree.php`):`$graph_rows`(`treeview_graphs_per_page`/`graphs`) as a bounded positive integer.`min_tree_width`,`max_tree_width`, and`page_refresh`to bounded integers before`<script>`output.Realtime graph authorization and argument hardening (`graph_realtime.php`):`is_graph_allowed($local_graph_id)`returning HTTP 403 before invoking`shell_exec()`and before reading cached files in`case 'view'`.`graph_nolegend`validation to`/^(true|false)$/`.`ds_step`via`cacti_sanitize_realtime_interval()`and blocks Guest writes to`set_user_setting()`.Regression tests (`tests/Unit/Security/InputValidation/UserSettingsAndRealtimeHardeningTest.php`):
## Verification

`php -l`passed on all 6 modified/added files.`tests/Unit/Security/InputValidation/UserSettingsAndRealtimeHardeningTest.php`): 4 passed (48 assertions).`php-cs-fixer --dry-run`: 0 of 6 files need formatting changes.`tests/tools/check_hardening_patterns.php`,`tests/security/verify_sink_inventory.sh`, and`tests/security/verify_architectural_hotspots.sh`: all passed.
