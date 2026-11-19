# MNDT-2026-0048

## Description
The legacy ASP.NET anti-CSRF library `Idunno.AntiCsrf` (`Idunno.AntiCsrf.dll`, version `0.9.1.0` / `0.9.1 Beta`) contains an insecure deserialization vulnerability in the `Idunno.AntiCsrf.AntiCsrfModule` HTTP module (`PreRequestHandlerExecute`). When processing incoming HTTP `POST` requests to ASP.NET WebForms (`System.Web.UI.Page`) endpoints, the module deserializes untrusted CSRF form token data using an unkeyed `.NET` `System.Web.UI.ObjectStateFormatter` instance without cryptographic MAC or signature verification, allowing a remote attacker to achieve arbitrary remote code execution (RCE).

## Impact
Critical: A remote attacker can supply any non-empty value in the configured CSRF cookie alongside a Base64-encoded `.NET` `ObjectStateFormatter` gadget chain in the configured CSRF form field to execute arbitrary code in the context of the IIS worker process (`w3wp.exe`), resulting in complete compromise of the web application server.

## Exploitability
High: `AntiCsrfModule.PreRequestHandlerExecute` executes at the `HttpApplication` pipeline level prior to `IHttpHandler.ProcessRequest` and the ASP.NET `Page` lifecycle (`PreInit`, `Init`, and `Page_Load`). Although pipeline-level authentication rules (`AuthenticateRequest` / `AuthorizeRequest`) execute earlier, any anonymously reachable `.aspx` page or any page relying on application-level session checks inside `Page_Load` (and neither implementing `ISuppressCsrfCheck` nor decorated with `[SuppressCsrfCheck]`) exposes the deserialization sink on `POST`--even if the page contains no `<form runat="server">`. Exploitation requires only a single HTTP `POST` request with no prior authentication or valid CSRF token. Active exploitation in the wild has been observed.

## CVE ID
CVE-2026-131914

## Common Weakness Enumeration
* CWE-502: Deserialization of Untrusted Data

## Details
`Idunno.AntiCsrf` is a third-party ASP.NET `IHttpModule` originally published on CodePlex (`http://anticsrf.codeplex.com/`) to provide double-submit cookie Cross-Site Request Forgery (CSRF) protection for ASP.NET WebForms applications. It is registered in `Web.config` under `<httpModules>` / `<modules>` as `Idunno.AntiCsrf.AntiCsrfModule, Idunno.AntiCsrf` and configured via `<csrfSettings>` (`Idunno.AntiCsrf.Configuration.CsrfSettings`), where `[ConfigurationProperty]` defaults set `cookieName` to `__CSRFCOOKIE`, `formFieldName` to `__CSRFTOKEN`, and `detectionResult` to `RaiseException` unless overridden in `Web.config`. In the decompiled `CsrfSettings` source, if the `<csrfSettings>` section is omitted from `Web.config` entirely, a setter bug in `CsrfSettings.DetectionResult` overwrites the fallback `FormFieldName` value with `"RaiseException"`.

In `AntiCsrfModule.Init`, the module subscribes to `PreSendRequestHeaders` and `PreRequestHandlerExecute`, and `PreRequestHandlerExecute` attaches `PageLoad` and `PagePreRender` to each `Page` handler (`Init` -> `PreRequestHandlerExecute` -> `PageLoad` -> `PagePreRender` -> `PreSendRequestHeaders`):

1. **Pre-`Page_Load` Unkeyed `ObjectStateFormatter.Deserialize` Sink on `POST` (`PreRequestHandlerExecute`):**
   For any `System.Web.UI.Page` handler neither implementing `ISuppressCsrfCheck` nor decorated with `[SuppressCsrfCheck]`, `PreRequestHandlerExecute` runs before `Page_Load` and inspects incoming `POST` requests. After checking only that both `Request.Cookies[CsrfSettings.Settings.CookieName]` and `Request.Form[CsrfSettings.Settings.FormFieldName]` are non-empty--without validating that the cookie is a well-formed GUID or requiring a `<form runat="server">`--it instantiates a parameterless `new ObjectStateFormatter()` and calls `Deserialize(context.Request.Form[CsrfSettings.Settings.FormFieldName])` before comparing the result against the cookie value. Because the parameterless `ObjectStateFormatter` constructor performs zero MAC, signature, encryption, or `machineKey` validation and enforces no `SerializationBinder` restrictions, supplying any non-empty cookie (e.g., `Cookie: __CSRFCOOKIE=1`) and a Base64-encoded `.NET` `ObjectStateFormatter` gadget chain in the CSRF form field executes arbitrary code inside `Deserialize()` under `w3wp.exe`. Immediately afterward, `RaiseError` either redirects (`HTTP 302`) to `<csrfSettings errorPage="..." />` when `detectionResult="Redirect"`, or throws `PotentialCsrfException` when `detectionResult="RaiseException"` (returning `HTTP 302` to `<customErrors defaultRedirect="..." />` when `customErrors` is active, or `HTTP 500` when `mode="Off"`).

2. **Unkeyed `ObjectStateFormatter.Serialize` During Page Rendering (`PagePreRender` & `PreSendRequestHeaders`):**
   When a `Page` with a `<form runat="server">` renders, `PagePreRender` either generates a new GUID via `Guid.NewGuid().ToString("D", CultureInfo.InvariantCulture)` when the CSRF cookie is absent/empty (emitting `Set-Cookie: <cookieName>=<GUID>; HttpOnly` in `PreSendRequestHeaders`) or reuses the existing cookie value after checking `GuidTryParse` (which is enforced only in `PagePreRender`, never in `PreRequestHandlerExecute` prior to `Deserialize()`), and registers the hidden form field via `new ObjectStateFormatter().Serialize((object)text)`.

**Known Public `Idunno.AntiCsrf.dll` (`0.9.1.0`) Binaries**

Organizations that have recompiled or customized `Idunno.AntiCsrf` internally will have different file hashes while retaining the vulnerable `ObjectStateFormatter.Deserialize` sink, and should also search `Web.config` and `bin/` for `Idunno.AntiCsrf` and `Idunno.AntiCsrf.AntiCsrfModule` by name.

| Filename / Build Provenance | Size (Bytes) | MD5 | SHA-1 | SHA-256 |
| :--- | ---: | :--- | :--- | :--- |
| `Idunno.AntiCsrf.dll` (`0.9.1.0` Official 2008 Release Build) | `69,632` | `dba68f9a091242b70b31f12caf90fdf3` | `61c3b6250dd83b2ab018d01975b9123e09c0843f` | `da1efcfed182597ee946a9ef2895dfdfeab2bdff16855aeef01656d8158ead06` |
| `Idunno.AntiCsrf.dll` (Rebuild of CodePlex `0.9.1 Beta` Source, Release) | `69,632` | `6160ca8df91abd964c93ea98216e81f9` | `b594518539e2947fceb37befeab417ed30f9b600` | `c5c994891783453ae85f3ef8efb48592b7c560aeb56f531ee9ea5736518246eb` |
| `Idunno.AntiCsrf.dll` (Rebuild of CodePlex `0.9.1 Beta` Source, Debug) | `70,144` | `48acb50c210ede14de69efaf035465ff` | `5f7b617e39cfc6aec0e49b8ba9a63b36ca7ea36a` | `aa7bbad4a7ebc38519955ac65517716569508ee4f61fc2f1276086940501e9bf` |

## CVSS Metrics
* **CVSS 4.0 Vector (CVSS-BT):** `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N/E:A` (**9.3 Critical**)

## Resolution
`Idunno.AntiCsrf` is a defunct open-source project last released as `0.9.1 Beta` (official build dated December 2008) on the since-retired CodePlex platform, and has no active maintainer or official patch available. Organizations should **discontinue use of `Idunno.AntiCsrf` (`Idunno.AntiCsrf.dll`) and replace it with an actively supported anti-CSRF alternative**:

1. **Remove `Idunno.AntiCsrf` (`Idunno.AntiCsrf.dll`):** Remove all `<add name="..." type="Idunno.AntiCsrf.AntiCsrfModule, Idunno.AntiCsrf" />` entries from `<httpModules>` and `<modules>`, remove both `<section name="csrfSettings" ... />` from `<configSections>` and the `<csrfSettings ... />` element from `Web.config`, remove any code references to `ISuppressCsrfCheck` or `[SuppressCsrfCheck]`, and delete `Idunno.AntiCsrf.dll` from the application's `bin/` directory.
2. **Adopt a Supported Anti-CSRF Mechanism:** Replace `Idunno.AntiCsrf` with a supported framework anti-forgery implementation, such as `System.Web.Helpers.AntiForgery` (`AntiForgery.GetHtml()` and `AntiForgery.Validate()` from `System.Web.WebPages`), ASP.NET WebForms `Page.ViewStateUserKey` combined with MAC-verified/encrypted ViewState on postback forms, or ASP.NET Core Anti-Request Forgery (`IAntiforgery`).
3. **Detection & Post-Compromise Assessment:** Audit all ASP.NET `Web.config` files and `bin/` directories for references to `Idunno.AntiCsrf` or `AntiCsrfModule`, and review IIS logs for anomalous `POST` requests to `.aspx` endpoints returning `HTTP 302` or `HTTP 500` with elevated `cs-bytes` (where logged). Environments with evidence of exploitation should rotate all secrets stored in `Web.config` and `applicationHost.config` (including `<machineKey>` keys, encryption keys, and database credentials) and inspect webroots for unauthorized files.

## Discovery Credits
* LDB
* Genwei Jiang, [Google Cloud, FLARE OTF](https://cloud.google.com/security/flare)
* Dhanesh Kizhakkinan, [Google Cloud, FLARE OTF](https://cloud.google.com/security/flare)
* Brian Bahtiarian, [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
* Lucas Kossack, [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)

## Disclosure Timeline
* 2026-11-04: Vulnerability root-cause analysis completed by FLARE during incident response investigation
* 2026-11-11: Mandiant CNA initiated CVE assignment for public awareness (defunct upstream project; no vendor or maintainer patch available)
* 2026-11-18: Mandiant advisory and CVE-2026-131914 published

## References
* [Archived Project Page - AntiCSRF on CodePlex (Wayback Machine)](https://web.archive.org/web/20100129114934/http://anticsrf.codeplex.com/)
* [CodePlex Archive - AntiCSRF](https://codeplexarchive.org/project/AntiCSRF)
* [cve.org CVE-2026-131914](https://www.cve.org/CVERecord?id=CVE-2026-131914)
