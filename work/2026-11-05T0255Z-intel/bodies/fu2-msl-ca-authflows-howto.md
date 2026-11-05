---
title: Block authentication flows with Conditional Access policy - Microsoft Entra ID
url: https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows
hostname: microsoft.com
description: Secure your organization by blocking device code flow and authentication transfer. Learn how to configure Conditional Access policies effectively.
sitename: MicrosoftLearn
date: "2026-04-07"
fingerprint: fc7cda9a4cc6e69e
---
Note

Access to this page requires authorization. You can try [signing in](https://learn.microsoft.com) or [changing directories].

Access to this page requires authorization. You can try [changing directories].

## Overview

The following steps help you create Conditional Access policies to restrict how [device code flow](https://learn.microsoft.com/concept-authentication-flows#device-code-flow) and [authentication transfer](https://learn.microsoft.com/concept-authentication-flows#authentication-transfer) are used within your organization.

## Device code flow policies

We recommend organizations get as close as possible to a unilateral block on device code flow. Consider creating a policy to audit the existing use of device code flow and determine if it's still necessary. Only allow device code flow in well documented and secured use cases, like legacy tooling that can't be updated.

For organizations that don't use device code flow, block it with the following Conditional Access policy:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/role-based-access-control/permissions-reference#conditional-access-administrator).
2. Browse to **Entra ID** > **Conditional Access** > **Policies**.
3. Select **New policy**.
4. Under **Assignments**, select **Users or workload identities**.
  1. Under **Include**, select the users you want to be in-scope for the policy (**all users** recommended).
  2. Under **Exclude**:
    1. Select **Users and groups** and choose your organization's emergency access or break-glass accounts and any other necessary users. Audit this exclusion list regularly.
5. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select the apps you want to be in-scope for the policy (**All resources (formerly 'All cloud apps')** recommended).
6. Under **Conditions** > **Authentication Flows**, set **Configure** to **Yes**.
  1. Select **Device code flow**.
  2. Select **Done**.
7. Under **Access controls** > **Grant**, select **Block access**.
  1. Select **Select**.
8. Confirm your settings and set **Enable policy** to **Report-only**.
9. Select **Create** to enable your policy.

After confirming your settings using [policy impact or report-only mode](https://learn.microsoft.com/concept-conditional-access-report-only#reviewing-results), move the **Enable policy** toggle from **Report-only** to **On**.

## Authentication transfer policies

Use the **Authentication flows** condition in Conditional Access to manage the feature. Block [authentication transfer](https://learn.microsoft.com/concept-authentication-transfer) if you don't want users to transfer authentication from their PC to a mobile device. For example, block authentication transfer if you don't allow Outlook to be used on personal devices by certain groups. Use the following Conditional Access policy to block authentication transfer:

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Conditional Access Administrator](https://learn.microsoft.com/role-based-access-control/permissions-reference#conditional-access-administrator).
2. Browse to **Entra ID** > **Conditional Access** > **Policies**.
3. Select **New policy**.
4. Under **Assignments**, select **Users or workload identities**.
  1. Under **Include**, select **All users** or user groups you want to block for authentication transfer.
  2. Under **Exclude**:
    1. Select **Users and groups** and choose your organization's emergency access or break-glass accounts and any other necessary users. Audit this exclusion list regularly.
5. Under **Target resources** > **Resources (formerly cloud apps)** > **Include**, select **All resources (formerly 'All cloud apps')** or apps you want to block for authentication transfer.
6. Under **Conditions** > **Authentication Flows**, set **Configure** to **Yes**
  1. Select **Authentication transfer**.
  2. Select **Done**.
7. Under **Access controls** > **Grant**, select **Block access**.
  1. Select **Select**.
8. Confirm your settings and set **Enable policy** to **Enabled**.
9. Select **Create** to enable your policy.

## User exclusions

Conditional Access policies are powerful tools. We recommend excluding the following accounts from your policies:

- **Emergency access** or **break-glass** accounts to prevent lockout due to policy misconfiguration. In the unlikely scenario where all administrators are locked out, your emergency access administrative account can be used to sign in and recover access.
  - More information can be found in the article, [Manage emergency access accounts in Microsoft Entra ID](https://learn.microsoft.com/role-based-access-control/security-emergency-access).
- **Service accounts** and **Service principals**, such as the Microsoft Entra Connect Sync Account. Service accounts are noninteractive accounts that aren't tied to any specific user. They're typically used by backend services to allow programmatic access to applications, but they're also used to sign in to systems for administrative purposes. Calls made by service principals aren't blocked by Conditional Access policies scoped to users. Use Conditional Access for workload identities to define policies that target service principals.
  - If your organization uses these accounts in scripts or code, replace them with [managed identities](https://learn.microsoft.com/managed-identities-azure-resources/overview).
