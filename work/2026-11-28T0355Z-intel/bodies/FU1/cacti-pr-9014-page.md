---
title: "fix(security): [1.2.x] harden user settings validation, Guest writes, and realtime graph access by somethingwithproof · Pull Request #9014 · Cacti/cacti"
url: https://github.com/Cacti/cacti/pull/9014
hostname: github.com
description: Summary Hardens user-preference validation, Guest account write restrictions, graph preview/tree pagination bounds, and realtime graph access control on 1.2.x. Changes User-setting schema validati...
sitename: GitHub
date: "2026-11-28"
categories: ['pull_request:5535209274']
fingerprint: c0fc88ab65b99ffc
language: en
image: https://opengraph.githubassets.com/1f9a375235c73dcd8b3dd0fe92e06eb9c7a37ab8531a474ffcb3c647f6f6ed63/Cacti/cacti/pull/9014
pagetype: object
filedate: "2026-11-28"
---
## Repository navigation

# fix(security): \[1.2.x\] harden user settings validation, Guest writes, and realtime graph access - #9014

Merged

[TheWitness](https://github.com/TheWitness)merged 2 commits into

## Conversation

…me graph access
Validate user preference values against $settings\_user field schemas in
auth\_profile.php and save\_user\_settings(), enforce POST/CSRF on
auth\_profile.php?action=update\_data, and reject Guest account mutations
across profile and realtime endpoints.
Validate preview and tree graph pagination and column settings before
building SQL LIMIT clauses or rendering JavaScript configuration values.
Enforce is\_graph\_allowed() before realtime poller execution and cache
reads in graph\_realtime.php, anchor the graph\_nolegend regex, validate
sess\_realtime\_hash, and clamp realtime intervals before shell execution.
Signed-off-by: Thomas Vincent \<thomasvincent@gmail.com>


**[github-advanced-security](https://github.com/apps/github-advanced-security)
    Bot**
              found potential problems

[Nov 28, 2026](https://github.com/Cacti/cacti/pull/9014#pullrequestreview-6094825234)
                  

[tests/Unit/Security/InputValidation/UserSettingsAndRealtimeHardeningTest.php](https://github.com/Cacti/cacti/pull/9014/files/e049bad440627d649a1aeb1b152971eb99a82171#diff-7dfc21631a349dd6bbc1818df9ec7f3a5e1888786a3c93a304de3b1905879adc)Fixed

…n hardening test
Signed-off-by: Thomas Vincent \<thomasvincent@gmail.com>

| **Quality Gate passed** Issues  [0 New issues](https://sonarcloud.io/project/issues?id=Cacti_cacti&pullRequest=9014&issueStatuses=OPEN,CONFIRMED&sinceLeakPeriod=true)  [0 Accepted issues](https://sonarcloud.io/project/issues?id=Cacti_cacti&pullRequest=9014&issueStatuses=ACCEPTED) Measures  [0 Security Hotspots](https://sonarcloud.io/project/security_hotspots?id=Cacti_cacti&pullRequest=9014&issueStatuses=OPEN,CONFIRMED&sinceLeakPeriod=true)  [0.0% Coverage on New Code](https://sonarcloud.io/component_measures?id=Cacti_cacti&pullRequest=9014&metric=new_coverage&view=list)  [0.0% Duplication on New Code](https://sonarcloud.io/component_measures?id=Cacti_cacti&pullRequest=9014&metric=new_duplicated_lines_density&view=list) [See analysis details on SonarQube Cloud](https://sonarcloud.io/dashboard?id=Cacti_cacti&pullRequest=9014) | 


**[TheWitness](https://github.com/TheWitness)**
    
              approved these changes

[Nov 28, 2026](https://github.com/Cacti/cacti/pull/9014#pullrequestreview-6094897574)
                  

### 
            **[TheWitness](https://github.com/TheWitness)**
    
      
      
      left a comment

Member


There was a problem hiding this comment.

Seems hackish, but letting it go. Seems the texbox forms need some types like string, int, positive int, double, etc. we can do this for now.

Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

Hardens user-preference validation, Guest account write restrictions, graph preview/tree pagination bounds, and realtime graph access control on `1.2.x`.

## Changes

User-setting schema validation (`lib/user_setting_validation.php`, `auth_profile.php`, `lib/functions.php`):`$settings_user`field definitions (`checkbox`,`drop_array`,`themes`,`drop_language`,`drop_sql`,`drop_color`, numeric/time`textbox`, and`font`) plus Guest-account and numeric/interval/hash sanitization helpers.`csrf_require_post()`on`auth_profile.php?action=update_data`.`logout_everywhere`,`clear_user_settings`,`reset_default`,`update_data`,`save`) and returns early in`save_user_settings()`.`is_view_allowed('graph_settings')`and schema validation (HTTP 400 on invalid values) in`api_auth_update_user_setting()`.Graph pagination and numeric settings (`lib/html_graph.php`, `graph_view.php`, `lib/html_tree.php`):`html_graph_validate_columns()`and`html_graph_validate_page_size()`to`lib/html_graph.php`and validates`preview_graphs_per_page`and`num_columns`defaults.`$graphs`and`$page`as positive integers before constructing the SQL`LIMIT`clause in`graph_view.php`, and validates`treeview_graphs_per_page`and`num_columns_tree`in`lib/html_tree.php`.`min_tree_width`,`max_tree_width`, and`page_refresh`to bounded integers before`<script>`output.Realtime graph authorization and argument hardening (`graph_realtime.php`):`is_graph_allowed($local_graph_id)`returning HTTP 403 before invoking`shell_exec()`and before reading cached files in`case 'view'`.`graph_nolegend`validation to`/^(true|false)$/`.`sess_realtime_hash`, clamps`ds_step`via`cacti_sanitize_realtime_interval()`, escapes`$hash`with`cacti_escapeshellarg()`, and blocks Guest writes to`set_user_setting()`.Regression tests (`tests/Unit/Security/InputValidation/UserSettingsAndRealtimeHardeningTest.php`):
## Verification

`php -l`passed on all 8 modified/added files.`tests/Unit/Security/InputValidation/UserSettingsAndRealtimeHardeningTest.php`): 6 passed (64 assertions).
