---
title: Apache Core Features
url: https://httpd.apache.org/docs/2.4/mod/core.html
hostname: apache.org
sitename: Apache HTTP Server Version 2.4
date: "2011-03-02"
fingerprint: b51ccb5bfe820f91
---
Apache HTTP Server Version 2.4

| [Description:](https://httpd.apache.org/module-dict.html#Description) | Core Apache HTTP Server features that are always available | 
|---|---|
| [Status:](https://httpd.apache.org/module-dict.html#Status) | Core | 

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures optimizations for a Protocol's Listener Sockets | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AcceptFilter` `protocol accept_filter` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive enables operating system specific optimizations for a
       listening socket by the `Protocol` type.
       The basic premise is for the kernel to not send a socket to the server
       process until either data is received or an entire HTTP Request is buffered.
       Only 
       [FreeBSD's Accept Filters](http://www.freebsd.org/cgi/man.cgi?query=accept_filter&sektion=9), Linux's more primitive
       `TCP_DEFER_ACCEPT`, and Windows' optimized AcceptEx()
       are currently supported.

Using `none` for an argument will disable any accept filters
       for that protocol.  This is useful for protocols that require a server
       send data first, such as `ftp:` or `nntp`:

AcceptFilter nntp none

The default protocol names are `https` for port 443
       and `http` for all other ports.  To specify that another
       protocol is being used with a listening port, add the `protocol`
       argument to the [Listen](https://httpd.apache.org/mod/mpm_common.html#listen)

The default values on FreeBSD are:

AcceptFilter http httpready
AcceptFilter https dataready

The `httpready` accept filter buffers entire HTTP requests at
       the kernel level.  Once an entire request is received, the kernel then
       sends it to the server. See the
       
       [accf\_http(9)](http://www.freebsd.org/cgi/man.cgi?query=accf_http&sektion=9) man page for more details.  Since HTTPS requests are
       encrypted, only the 
       [accf\_data(9)](http://www.freebsd.org/cgi/man.cgi?query=accf_data&sektion=9) filter is used.

The default values on Linux are:

AcceptFilter http data
AcceptFilter https data

Linux's `TCP_DEFER_ACCEPT` does not support buffering http
       requests.  Any value besides `none` will enable
       `TCP_DEFER_ACCEPT` on that listener. For more details
       see the Linux
       
       [tcp(7)](http://man7.org/linux/man-pages/man7/tcp.7.html) man page.

The default values on Windows are:

AcceptFilter http connect
AcceptFilter https connect

Window's mpm\_winnt interprets the AcceptFilter to toggle the AcceptEx()
       API, and does not support http protocol buffering. `connect`
       will use the AcceptEx() API, also retrieve the network endpoint
       addresses, but like `none` the `connect` option
       does not wait for the initial data transmission.

On Windows, `none` uses accept() rather than AcceptEx()
       and will not recycle sockets between connections.  This is useful for
       network adapters with broken driver support, as well as some virtual
       network providers such as vpn drivers, or spam, virus or spyware
       filters.

`data` AcceptFilter (Windows)
For versions 2.4.23 and prior, the Windows `data` accept
         filter waited until data had been transmitted and the initial data
         buffer and network endpoint addresses had been retrieved from the
         single AcceptEx() invocation. This implementation was subject to a
         denial of service attack and has been disabled.

Current releases of httpd default to the `connect` filter
         on Windows, and will fall back to `connect` if
         `data` is specified. Users of prior releases are encouraged
         to add an explicit setting of `connect` for their
         AcceptFilter, as shown above.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Resources accept trailing pathname information | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AcceptPathInfo On\|Off\|Default` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AcceptPathInfo Default` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive controls whether requests that contain trailing
    pathname information that follows an actual filename (or
    non-existent file in an existing directory) will be accepted or
    rejected.  The trailing pathname information can be made
    available to scripts in the `PATH_INFO` environment
    variable.

For example, assume the location `/test/` points to
    a directory that contains only the single file
    `here.html`.  Then requests for
    `/test/here.html/more` and
    `/test/nothere.html/more` both collect
    `/more` as `PATH_INFO`.

The three possible arguments for the
    `AcceptPathInfo` directive are:

- `Off`
- A request will only be accepted if it
    maps to a literal path that exists.  Therefore a request with
    trailing pathname information after the true filename such as
    `/test/here.html/more` in the above example will return
    a 404 NOT FOUND error.
- `On`
- A request will be accepted if a
    leading path component maps to a file that exists.  The above
    example `/test/here.html/more` will be accepted if `/test/here.html` maps to a valid file.
- `Default`
- The treatment of requests with
    trailing pathname information is determined by the [handler](https://httpd.apache.org/handler.html) responsible for the request.
    The core handler for normal files defaults to rejecting `PATH_INFO` requests. Handlers that serve scripts, such as [cgi-script](https://httpd.apache.org/mod_cgi.html) and [isapi-handler](https://httpd.apache.org/mod_isapi.html), generally accept `PATH_INFO` by default.

The primary purpose of the `AcceptPathInfo`
    directive is to allow you to override the handler's choice of
    accepting or rejecting `PATH_INFO`. This override is required,
    for example, when you use a [filter](https://httpd.apache.org/filter.html), such
    as [INCLUDES](https://httpd.apache.org/mod_include.html), to generate content
    based on `PATH_INFO`.  The core handler would usually reject
    the request, so you can use the following configuration to enable
    such a script:

\<Files "mypaths.shtml">
  Options +Includes
  SetOutputFilter INCLUDES
  AcceptPathInfo On
\</Files>

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Name of the distributed configuration file | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AccessFileName` `filename` [`filename`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AccessFileName .htaccess` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The AccessFileName directive allows you to change the name of the file
    that will be considered for per-directory configuration overrides, in the
    event that [AllowOverride](https://httpd.apache.org#allowoverride)

We do not recommend that you change this value, and
    especially that you do not list multiple possible file names, as it makes
    troubleshooting more difficult for anyone not familiar with your local
    settings.

While processing a request, the server looks for files with the name
    (or names) defined in `AccessFileName`
    in every directory of the path to the document, if distributed
    configuration files are [enabled for that
    directory](https://httpd.apache.org#allowoverride). For example Before returning the document
    `/usr/local/web/index.html`, the server will read
    `/.htaccess`, `/usr/.htaccess`,
    `/usr/local/.htaccess` and `/usr/local/web/.htaccess`
    for directives.

For this reason, the default configuration file contains the following stanza:

```
<Directory "/">
    AllowOverride None
</Directory>
```
    This configuration block helps prevent unnecessary file accesses in directories
    outside of your [DocumentRoot](https://httpd.apache.org#documentroot)`AllowOverride` directive documentation.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Default charset parameter to be added when a response content-type is `text/plain` or `text/html` | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AddDefaultCharset On\|Off\|``charset` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AddDefaultCharset Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive specifies a default value for the media type
    charset parameter (the name of a character encoding) to be added
    to a response if and only if the response's content-type is either
    `text/plain` or `text/html`.  This should override
    any charset specified in the body of the response via a `META`
    element, though the exact behavior is often dependent on the user's client
    configuration. A setting of `AddDefaultCharset Off`
    disables this functionality. `AddDefaultCharset On` enables
    a default charset of `iso-8859-1`. Any other value is assumed
    to be the `charset` to be used, which should be one of the
    [IANA registered
    charset values](http://www.iana.org/assignments/character-sets) for use in Internet media types (MIME types).
    For example:

AddDefaultCharset utf-8

`AddDefaultCharset` should only be used when all
    of the text resources to which it applies are known to be in that
    character encoding and it is too inconvenient to label their charset
    individually. One such example is to add the charset parameter
    to resources containing generated content, such as legacy CGI
    scripts, that might be vulnerable to cross-site scripting attacks
    due to user-provided data being included in the output.  Note, however,
    that a better solution is to just fix (or delete) those scripts, since
    setting a default charset does not protect users that have enabled
    the "auto-detect character encoding" feature on their browser.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determines whether encoded path separators in URLs are allowed to be passed through | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AllowEncodedSlashes On\|Off\|NoDecode` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AllowEncodedSlashes Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | NoDecode option available in 2.3.12 and later. | 

The `AllowEncodedSlashes` directive allows URLs
    which contain encoded path separators (`%2F` for `/`
    and additionally `%5C` for `\` on accordant systems)
    to be used in the path info.

With the default value, `Off`, such URLs are refused
    with a 404 (Not found) error.

With the value `On`, such URLs are accepted, and encoded
      slashes are decoded like all other encoded characters.

With the value `NoDecode`, such URLs are accepted, but
      encoded slashes are not decoded but left in their encoded state.

Turning `AllowEncodedSlashes` `On` is
    mostly useful when used in conjunction with `PATH_INFO`.

If encoded slashes are needed in path info, use of `NoDecode` is
      strongly recommended as a security measure.  Allowing slashes
      to be decoded could potentially allow unsafe paths.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Types of directives that are allowed in `.htaccess` files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AllowOverride All\|None\|``directive-type` [`directive-type`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AllowOverride None` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

When the server finds a distributed configuration file (Usually called
    `.htaccess` - configurable by the [AccessFileName](https://httpd.apache.org#accessfilename)

`AllowOverride` is valid only in
    [<Directory>](https://httpd.apache.org#directory)[<Location>](https://httpd.apache.org#location)[<DirectoryMatch>](https://httpd.apache.org#directorymatch)[<Files>](https://httpd.apache.org#files)
When this directive is set to `None` and [AllowOverrideList](https://httpd.apache.org#allowoverridelist)`None`, [.htaccess](https://httpd.apache.org#accessfilename) files are
    completely ignored. In this case, the server will not even attempt
    to read `.htaccess` files in the filesystem.

When this directive is set to `All`, then any
    directive which has the .htaccess [Context](https://httpd.apache.org/directive-dict.html#Context) is allowed in
    `.htaccess` files.

The `directive-type` can be one of the following
    groupings of directives. (See the [override class
    index](https://httpd.apache.org/overrides.html) for an up-to-date listing of which directives are enabled by each
    `directive-type`.)

- [AuthConfig](https://httpd.apache.org/overrides.html#override-authconfig)
- 
      Allow use of the authorization directives ([AuthDBMGroupFile](https://httpd.apache.org/mod/mod_authz_dbm.html#authdbmgroupfile)
[AuthDBMUserFile](https://httpd.apache.org/mod/mod_authn_dbm.html#authdbmuserfile)
[AuthGroupFile](https://httpd.apache.org/mod/mod_authz_groupfile.html#authgroupfile)
[AuthName](https://httpd.apache.org/mod/mod_authn_core.html#authname)
[AuthType](https://httpd.apache.org/mod/mod_authn_core.html#authtype)
[AuthUserFile](https://httpd.apache.org/mod/mod_authn_file.html#authuserfile)
[Require](https://httpd.apache.org/mod/mod_authz_core.html#require)
*etc.*).
- [FileInfo](https://httpd.apache.org/overrides.html#override-fileinfo)
- 
      Allow use of the directives controlling document types
     ([ErrorDocument](https://httpd.apache.org#errordocument)
[ForceType](https://httpd.apache.org#forcetype)
[LanguagePriority](https://httpd.apache.org/mod/mod_negotiation.html#languagepriority)
[SetHandler](https://httpd.apache.org#sethandler)
[SetInputFilter](https://httpd.apache.org#setinputfilter)
[SetOutputFilter](https://httpd.apache.org#setoutputfilter)
[mod_mime](https://httpd.apache.org/mod/mod_mime.html)
[Header](https://httpd.apache.org/mod/mod_headers.html#header)
[RequestHeader](https://httpd.apache.org/mod/mod_headers.html#requestheader)
[SetEnvIf](https://httpd.apache.org/mod/mod_setenvif.html#setenvif)
[SetEnvIfNoCase](https://httpd.apache.org/mod/mod_setenvif.html#setenvifnocase)
[BrowserMatch](https://httpd.apache.org/mod/mod_setenvif.html#browsermatch)
[CookieExpires](https://httpd.apache.org/mod/mod_usertrack.html#cookieexpires)
[CookieDomain](https://httpd.apache.org/mod/mod_usertrack.html#cookiedomain)
[CookieStyle](https://httpd.apache.org/mod/mod_usertrack.html#cookiestyle)
[CookieTracking](https://httpd.apache.org/mod/mod_usertrack.html#cookietracking)
[CookieName](https://httpd.apache.org/mod/mod_usertrack.html#cookiename)
[mod_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)
[RewriteEngine](https://httpd.apache.org/mod/mod_rewrite.html#rewriteengine)
[RewriteOptions](https://httpd.apache.org/mod/mod_rewrite.html#rewriteoptions)
[RewriteBase](https://httpd.apache.org/mod/mod_rewrite.html#rewritebase)
[RewriteCond](https://httpd.apache.org/mod/mod_rewrite.html#rewritecond)
[RewriteRule](https://httpd.apache.org/mod/mod_rewrite.html#rewriterule)
[mod_alias](https://httpd.apache.org/mod/mod_alias.html)
[Redirect](https://httpd.apache.org/mod/mod_alias.html#redirect)
[RedirectTemp](https://httpd.apache.org/mod/mod_alias.html#redirecttemp)
[RedirectPermanent](https://httpd.apache.org/mod/mod_alias.html#redirectpermanent)
[RedirectMatch](https://httpd.apache.org/mod/mod_alias.html#redirectmatch)
[Action](https://httpd.apache.org/mod/mod_actions.html#action)
[mod_actions](https://httpd.apache.org/mod/mod_actions.html)
- [Indexes](https://httpd.apache.org/overrides.html#override-indexes)
- 
      Allow use of the directives controlling directory indexing
      ([AddDescription](https://httpd.apache.org/mod/mod_autoindex.html#adddescription)
[AddIcon](https://httpd.apache.org/mod/mod_autoindex.html#addicon)
[AddIconByEncoding](https://httpd.apache.org/mod/mod_autoindex.html#addiconbyencoding)
[AddIconByType](https://httpd.apache.org/mod/mod_autoindex.html#addiconbytype)
[DefaultIcon](https://httpd.apache.org/mod/mod_autoindex.html#defaulticon)
[DirectoryIndex](https://httpd.apache.org/mod/mod_dir.html#directoryindex)
[`FancyIndexing`](https://httpd.apache.org/mod_autoindex.html#indexoptions.fancyindexing), [HeaderName](https://httpd.apache.org/mod/mod_autoindex.html#headername)
[IndexIgnore](https://httpd.apache.org/mod/mod_autoindex.html#indexignore)
[IndexOptions](https://httpd.apache.org/mod/mod_autoindex.html#indexoptions)
[ReadmeName](https://httpd.apache.org/mod/mod_autoindex.html#readmename)
*etc.*).
- [Limit](https://httpd.apache.org/overrides.html#override-limit)
- 
      Allow use of the legacy host access control directives ([Allow](https://httpd.apache.org/mod/mod_access_compat.html#allow)
[Deny](https://httpd.apache.org/mod/mod_access_compat.html#deny)
[Order](https://httpd.apache.org/mod/mod_access_compat.html#order)
[Require](https://httpd.apache.org/mod/mod_authz_core.html#require)
`AuthConfig`.
- Nonfatal=\[Override|Unknown|All\]
- 
      Allow use of AllowOverride option to treat syntax errors in
      .htaccess as nonfatal. Instead of causing an Internal Server
      Error, disallowed or unrecognized directives will be ignored
      and a warning logged:
      
  - **Nonfatal=Override** treats directives
              forbidden by AllowOverride as nonfatal.
  - **Nonfatal=Unknown** treats unknown directives
              as nonfatal.  This covers typos and directives implemented
              by a module that's not present.
  - **Nonfatal=All** treats both the above as nonfatal.
Note that a syntax error in a valid directive will still cause an internal server error. ### Security Nonfatal errors may have security implications for .htaccess users. For example, if AllowOverride disallows AuthConfig, users' configuration designed to restrict access to a site will be disabled.
- [Options](https://httpd.apache.org/overrides.html#override-options)\[=`Option`,...\]
- 
      Allow use of the directives controlling specific directory
      features ([Options](https://httpd.apache.org#options)
[XBitHack](https://httpd.apache.org/mod/mod_include.html#xbithack)
[Options](https://httpd.apache.org#options)
### Implicit disabling of Options This restriction only controls which options a
         `.htaccess` file may *enable*. It does not
         prevent inherited options from being *disabled*.
When a [Options](https://httpd.apache.org#options)`.htaccess` uses absolute syntax (without `+` or `-` prefixes), it *replaces* the entire inherited option set. Any previously active options
         not listed are implicitly turned off—even options that are
         not in the `AllowOverride` permitted list.
For example, if the server configuration sets: Options Indexes FollowSymLinks ExecCGI AllowOverride Options=Indexes and a `.htaccess` file contains:
Options Indexes then `FollowSymLinks` and `ExecCGI` are
         implicitly disabled for that directory, even though the `AllowOverride` line only permits setting `Indexes`.
In short, this mechanism cannot force a specific option to
         remain *set* while allowing any others to be set.
AllowOverride Options=Indexes,MultiViews

Example:

AllowOverride AuthConfig Indexes

In the example above, all directives that are neither in the group
    `AuthConfig` nor `Indexes` cause an internal
    server error.

For security and performance reasons, do not set
    `AllowOverride` to anything other than `None`
    in your `<Directory "/">` block. Instead, find (or
    create) the `<Directory>` block that refers to the
    directory where you're actually planning to place a
    `.htaccess` file.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Individual directives that are allowed in `.htaccess` files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `AllowOverrideList None\|``directive` [`directive`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `AllowOverrideList None` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

When the server finds an `.htaccess` file (as
    specified by [AccessFileName](https://httpd.apache.org#accessfilename)

`AllowOverrideList` is valid only in
    When this directive is set to `None` and [AllowOverride](https://httpd.apache.org#allowoverride)`None`,
    then [.htaccess](https://httpd.apache.org#accessfilename) files are completely
    ignored.  In this case, the server will not even attempt to read
    `.htaccess` files in the filesystem.

A value of `None` cannot be combined with other values. 
    Doing so will result in an error that aborts config parsing.

AllowOverride None
AllowOverrideList Redirect RedirectMatch

In the example above, only the `Redirect` and
    `RedirectMatch` directives are allowed. All others will
    cause an internal server error.

AllowOverride AuthConfig
AllowOverrideList CookieTracking CookieName

In the example above, [AllowOverride](https://httpd.apache.org#allowoverride)`AuthConfig`
    directive grouping and `AllowOverrideList` grants
    permission to only two directives from the `FileInfo` directive
    grouping. The effective set of permitted directives is the union of
    both. All others will cause an internal server error.

In addition, certain directives are always permitted in
    `.htaccess` files whenever the override mechanism is
    enabled (i.e., [AllowOverride](https://httpd.apache.org#allowoverride)`None`). These are listed in the
    [All](https://httpd.apache.org/overrides.html#override-all) section of the
    [override class index](https://httpd.apache.org/overrides.html).

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Technique for locating the interpreter for CGI scripts | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `CGIMapExtension` `cgi-path .extension` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | NetWare only | 

This directive is used to control how Apache httpd finds the
    interpreter used to run CGI scripts. For example, setting
    `CGIMapExtension sys:\foo.nlm .foo` will
    cause all CGI script files with a `.foo` extension to
    be passed to the FOO interpreter.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enables passing HTTP authorization headers to scripts as CGI variables | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `CGIPassAuth On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `CGIPassAuth Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | AuthConfig | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.4.13 and later | 

`CGIPassAuth` allows scripts access to HTTP
    authorization headers such as `Authorization`, which is
    required for scripts that implement HTTP Basic authentication.
    Normally these HTTP headers are hidden from scripts. This is to disallow
    scripts from seeing user ids and passwords used to access the server when
    HTTP Basic authentication is enabled in the web server.  This directive
    should be used when scripts are allowed to implement HTTP Basic
    authentication.

This directive can be used instead of the compile-time setting
    `SECURITY_HOLE_PASS_AUTHORIZATION` which has been available
    in previous versions of Apache HTTP Server.

The setting is respected by any modules which use
    `ap_add_common_vars()`, such as [mod\_cgi](https://httpd.apache.org/mod/mod_cgi.html)[mod\_cgid](https://httpd.apache.org/mod/mod_cgid.html)[mod\_proxy\_fcgi](https://httpd.apache.org/mod/mod_proxy_fcgi.html)[mod\_proxy\_scgi](https://httpd.apache.org/mod/mod_proxy_scgi.html)[mod\_include](https://httpd.apache.org/mod/mod_include.html)[mod\_ext\_filter](https://httpd.apache.org/mod/mod_ext_filter.html)`ap_add_common_vars()` may choose to respect the setting
    as well.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls how some CGI variables are set | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `CGIVar` `variable rule` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.4.21 and later | 

This directive controls how certain CGI environment variables are
  set when requests are passed to CGI scripts or other handlers that
  receive a CGI environment. Currently, the only variable supported is
  `REQUEST_URI`.

By default, the CGI environment variable `REQUEST_URI`
  is set to the original URI from the client's request line. This means
  that even if [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)

With `CGIVar REQUEST_URI current-uri`, the value is
  instead set to the current URI after any rewrites or internal
  redirects have been applied.

**Allowed values:**

- `original-uri` (default)
- Set `REQUEST_URI` to the URI from the original client
    request, regardless of any internal redirects or rewrites.
- `current-uri`
- Set `REQUEST_URI` to the URI of the resource
    currently being processed, which may differ from the original
    request due to internal redirects or rewrites.

\# Show CGI scripts the rewritten URI rather than the original
CGIVar REQUEST\_URI current-uri

The CGI environment variable `REQUEST_URI` (in either
  mode) contains the full URI including the query string. This differs
  from the server variable `%{REQUEST_URI}` used in
  [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)[ap\_expr](https://httpd.apache.org/expr.html),
  which contains only the path component (no query string).

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enables the generation of `Content-MD5` HTTP Response headers | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ContentDigest On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ContentDigest Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | Options | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive enables the generation of
    `Content-MD5` headers as defined in RFC1864
    respectively RFC2616.

MD5 is an algorithm for computing a "message digest" (sometimes called "fingerprint") of arbitrary-length data, with a high degree of confidence that any alterations in the data will be reflected in alterations in the message digest.

The `Content-MD5` header provides an end-to-end
    message integrity check (MIC) of the entity-body. A proxy or
    client may check this header for detecting accidental
    modification of the entity-body in transit. Example header:

```
      Content-MD5: AuLb7Dp1rqtRtxz2m9kRpA==
    
```

Note that this can cause performance problems on your server since the message digest is computed on every request (the values are not cached).

`Content-MD5` is only sent for documents served
    by the [core](https://httpd.apache.org/mod/core.html)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Base directory for the server run-time files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `DefaultRuntimeDir` `directory-path` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `DefaultRuntimeDir DEFAULT_REL_RUNTIMEDIR (logs/)` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache 2.4.2 and later | 

The `DefaultRuntimeDir` directive sets the
    directory in which the server will create various run-time files
    (shared memory, locks, etc.). If set as a relative path, the full path
    will be relative to `ServerRoot`.

**Example**

DefaultRuntimeDir scratch/

The default location of `DefaultRuntimeDir` may be
    modified by changing the `DEFAULT_REL_RUNTIMEDIR` #define
    at build time.

Note: `ServerRoot` should be specified before this
   directive is used. Otherwise, the default value of `ServerRoot`
   would be used to set the base directory.

- [the
    security tips](https://httpd.apache.org/misc/security_tips.html#serverroot) for information on how to properly set
    permissions on the `ServerRoot`

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | This directive has no effect other than to emit warnings if the value is not `none`. In prior versions, DefaultType would specify a default media type to assign to response content for which no other media type configuration could be found. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `DefaultType` `media-type\|none` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `DefaultType none` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | The argument `none` is available in Apache httpd 2.2.7 and later.  All other choices are DISABLED for 2.3.x and later. | 

This directive has been disabled.  For backwards compatibility
    of configuration files, it may be specified with the value
    `none`, meaning no default media type. For example:

DefaultType None

`DefaultType None` is only available in
    httpd-2.2.7 and later.

Use the mime.types configuration file and the
    [AddType](https://httpd.apache.org/mod/mod_mime.html#addtype)[ForceType](https://httpd.apache.org#forcetype)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Define a variable | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Define` `parameter-name` [`parameter-value`] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

In its one parameter form, `Define` is
    equivalent to passing the `-D` argument to
    [httpd](https://httpd.apache.org/programs/httpd.html)[\<IfDefine>](https://httpd.apache.org#ifdefine)`-D` arguments in any
    startup scripts.

In addition to that, if the second parameter is given, a config variable
    is set to this value. The variable can be used in the configuration using
    the `${VAR}` syntax. The variable is always globally defined
    and not limited to the scope of the surrounding config section.

```
<IfDefine TEST>
  Define servername test.example.com
</IfDefine>
<IfDefine !TEST>
  Define servername www.example.com
  Define SSL
</IfDefine>
DocumentRoot "/var/www/${servername}/htdocs"
```
    Variable names may not contain colon ":" characters, to avoid clashes
    with [RewriteMap](https://httpd.apache.org/mod/mod_rewrite.html#rewritemap)

While this directive is supported in virtual host context, the changes it makes are visible to any later configuration directives, beyond any enclosing virtual host.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enclose a group of directives that apply only to the named file-system directory, sub-directories, and their contents. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<Directory` `directory-path`> ... </Directory> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

`<Directory>` and
    `</Directory>` are used to enclose a group of
    directives that will apply only to the named directory,
    sub-directories of that directory, and the files within the respective
    directories.  Any directive that is allowed
    in a directory context may be used. `Directory-path` is
    either the full path to a directory, or a wild-card string using
    Unix shell-style matching. In a wild-card string, `?` matches
    any single character, and `*` matches any sequence of
    characters. You may also use `[]` character ranges. None
    of the wildcards match a \`/' character, so ```
<Directory
    "/*/public_html">
```
 will not match
    `/home/user/public_html`, but ```
<Directory
    "/home/*/public_html">
```
 will match. Example:

\<Directory "/usr/local/httpd/htdocs">
  Options Indexes FollowSymLinks
\</Directory>

Directory paths *may* be quoted, if you like, however, it
    *must* be quoted if the path contains spaces. This is because a
    space would otherwise indicate the end of an argument.

Be careful with the `directory-path` arguments:
      They have to literally match the filesystem path which Apache httpd uses
      to access the files. Directives applied to a particular
      `<Directory>` will not apply to files accessed from
      that same directory via a different path, such as via different symbolic
      links.

[Regular
    expressions](https://httpd.apache.org/glossary.html#regex) can also be used, with the addition of the
    `~` character. For example:

```
<Directory ~ "^/www/[0-9]{3}">
</Directory>
```
    would match directories in `/www/` that consisted of
    three numbers.

If multiple (non-regular expression) `<Directory>` sections
    match the directory (or one of its parents) containing a document,
    then the directives are applied in the order of shortest match
    first, interspersed with the directives from the [.htaccess](https://httpd.apache.org#accessfilename) files. For example,
    with

\<Directory "/">
  AllowOverride None
\</Directory>
\<Directory "/home">
  AllowOverride FileInfo
\</Directory>

for access to the document `/home/web/dir/doc.html`
    the steps are:

- Apply directive `AllowOverride None` (disabling `.htaccess` files).
- Apply directive `AllowOverride FileInfo` (for
      directory `/home`).
- Apply any `FileInfo` directives in `/home/.htaccess`, `/home/web/.htaccess` and `/home/web/dir/.htaccess` in that order.

Regular expressions are not considered until after all of the normal sections have been applied. Then all of the regular expressions are tested in the order they appeared in the configuration file. For example, with

\<Directory \~ "abc$">
  # ... directives here ...
\</Directory>

the regular expression section won't be considered until after
    all normal `<Directory>`s and
    `.htaccess` files have been applied. Then the regular
    expression will match on `/home/abc/public_html/abc` and
    the corresponding `<Directory>` will
    be applied.

The default access for
    `<Directory "/">` is to permit all access.
    This means that Apache httpd will serve any file mapped from an URL. It is
    recommended that you change this with a block such
    as

\<Directory "/">
  Require all denied
\</Directory>

Then override this for directories you
    *want* accessible. See the [Security Tips](https://httpd.apache.org/misc/security_tips.html) page for more
    details.

The directory sections occur in the `httpd.conf` file.
    `<Directory>` directives
    cannot nest, and cannot appear in a [\<Limit>](https://httpd.apache.org#limit)[\<LimitExcept>](https://httpd.apache.org#limitexcept)

- [How \<Directory>,
    \<Location> and \<Files> sections work](https://httpd.apache.org/sections.html) for an
    explanation of how these different sections are combined when a
    request is received

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enclose directives that apply to the contents of file-system directories matching a regular expression. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<DirectoryMatch` `regex`> ... </DirectoryMatch> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

`<DirectoryMatch>` and
    `</DirectoryMatch>` are used to enclose a group
    of directives which will apply to directories (and the files
    within) whose filesystem path matches the given
    [regular expression](https://httpd.apache.org/glossary.html#regex).
    Unlike [\<Directory>](https://httpd.apache.org#directory)`^` or `$` in the pattern.  For example:

```
<DirectoryMatch "^/www/(.+/)?[0-9]{3}/">
    # ...
</DirectoryMatch>
```
    matches directories in `/www/` (or any subdirectory thereof)
    that consist of three numbers.

`$`, you may need to match both forms, e.g.,
      `<DirectoryMatch "^/var/www/?$">`.
    From 2.4.8 onwards, named groups and backreferences are captured and
    written to the environment with the corresponding name prefixed with
    "MATCH\_" and in upper case. This allows elements of paths to be referenced
    from within [expressions](https://httpd.apache.org/expr.html) and modules like
    [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)

```
<DirectoryMatch "^/var/www/combined/(?<sitename>[^/]+)">
    Require ldap-group cn=%{env:MATCH_SITENAME},ou=combined,o=Example
</DirectoryMatch>
```
- [<Directory>](https://httpd.apache.org#directory)
`<Directory>`s
- [How \<Directory>, \<Location> and
\<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these different
sections are combined when a request is received

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Directory that forms the main document tree visible from the web | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `DocumentRoot` `directory-path` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `DocumentRoot "/usr/local/apache/htdocs"` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive sets the directory from which [httpd](https://httpd.apache.org/programs/httpd.html)[Alias](https://httpd.apache.org/mod/mod_alias.html#alias)

DocumentRoot "/usr/web"

then an access to
    `http://my.example.com/index.html` refers to
    `/usr/web/index.html`. If the `directory-path` is
    not absolute then it is assumed to be relative to the [ServerRoot](https://httpd.apache.org#serverroot)

The `DocumentRoot` should be specified without
    a trailing slash.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply only if the condition of a previous [<If>](https://httpd.apache.org#if) or [<ElseIf>](https://httpd.apache.org#elseif) section is not satisfied by a request at runtime | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<Else> ... </Else>` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Nested conditions are evaluated in 2.4.26 and later | 

The `<Else>` applies the enclosed
    directives if and only if the most recent
    `<If>` or
    `<ElseIf>` section
    in the same scope has not been applied.
    For example: In

```
<If "-z req('Host')">
  # ...
</If>
<Else>
  # ...
</Else>
```
    The `<If>` would match HTTP/1.0
        requests without a `Host:` header and the
        `<Else>` would match requests
        with a `Host:` header.

- [<If>](https://httpd.apache.org#if)
- [<ElseIf>](https://httpd.apache.org#elseif)
- [How \<Directory>, \<Location>,
    \<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these
    different sections are combined when a request is received. `<If>`, `<ElseIf>`, and `<Else>` are applied last.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply only if a condition is satisfied by a request at runtime while the condition of a previous [<If>](https://httpd.apache.org#if) or `<ElseIf>` section is not satisfied | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<ElseIf` `expression`> ... </ElseIf> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Nested conditions are evaluated in 2.4.26 and later | 

The `<ElseIf>` applies the enclosed
    directives if and only if both the given condition evaluates to true and
    the most recent `<If>` or
    `<ElseIf>` section in the same scope has
    not been applied.  For example: In

\<If "-R '10.1.0.0/16'">
  #...
\</If>
\<ElseIf "-R '10.0.0.0/8'">
  #...
\</ElseIf>
\<Else>
  #...
\</Else>

The `<ElseIf>` would match if
    the remote address of a request belongs to the subnet 10.0.0.0/8 but
    not to the subnet 10.1.0.0/16.

- [Expressions in Apache HTTP Server](https://httpd.apache.org/expr.html),
for a complete reference and more examples.
- [<If>](https://httpd.apache.org#if)
- [<Else>](https://httpd.apache.org#else)
- [How \<Directory>, \<Location>,
    \<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these
    different sections are combined when a request is received. `<If>`, `<ElseIf>`, and `<Else>` are applied last.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Use memory-mapping to read files during delivery | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `EnableMMAP On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `EnableMMAP On` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive controls whether the [httpd](https://httpd.apache.org/programs/httpd.html)[mod\_include](https://httpd.apache.org/mod/mod_include.html)

This memory-mapping sometimes yields a performance improvement. But in some environments, it is better to disable the memory-mapping to prevent operational problems:

- On some multiprocessor systems, memory-mapping can reduce the
    performance of the [httpd](https://httpd.apache.org/programs/httpd.html)
- Deleting or truncating a file while [httpd](https://httpd.apache.org/programs/httpd.html)
[httpd](https://httpd.apache.org/programs/httpd.html)

For server configurations that are vulnerable to these problems, you should disable memory-mapping of delivered files by specifying:

EnableMMAP Off

For NFS mounted files, this feature may be disabled explicitly for the offending files by specifying:

\<Directory "/path-to-nfs-files">
  EnableMMAP Off
\</Directory>

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Use the kernel sendfile support to deliver files to the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `EnableSendfile On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `EnableSendfile Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Default changed to Off in version 2.3.9. | 

This directive controls whether [httpd](https://httpd.apache.org/programs/httpd.html)

This sendfile mechanism avoids separate read and send operations, and buffer allocations. But on some platforms or within some filesystems, it is better to disable this feature to avoid operational problems:

- Some platforms may have broken sendfile support that the build system did not detect, especially if the binaries were built on another box and moved to such a machine with broken sendfile support.
- On Linux the use of sendfile triggers TCP-checksum offloading bugs on certain networking cards when using IPv6.
- On Linux on Itanium, `sendfile` may be unable to handle
    files over 2GB in size.
- With a network-mounted [DocumentRoot](https://httpd.apache.org#documentroot)

For server configurations that are not vulnerable to these problems, you may enable this feature by specifying:

EnableSendfile On

For network mounted files, this feature may be disabled explicitly for the offending files by specifying:

\<Directory "/path-to-nfs-files">
  EnableSendfile Off
\</Directory>

Please note that the per-directory and .htaccess configuration
       of `EnableSendfile` is not supported by
       [mod\_cache\_disk](https://httpd.apache.org/mod/mod_cache_disk.html)`EnableSendfile`
       is taken into account by the module.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Abort configuration parsing with a custom error message | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Error` `message` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.3.9 and later | 

If an error can be detected within the configuration, this directive can be used to generate a custom error message, and halt configuration parsing. The typical use is for reporting required modules which are missing from the configuration.

\# Example
# ensure that mod\_include is loaded
\<IfModule !include\_module>
  Error "mod\_include is required by mod\_foo.  Load it with LoadModule."
\</IfModule>
# ensure that exactly one of SSL,NOSSL is defined
\<IfDefine SSL>
\<IfDefine NOSSL>
  Error "Both SSL and NOSSL are defined.  Define only one of them."
\</IfDefine>
\</IfDefine>
\<IfDefine !SSL>
\<IfDefine !NOSSL>
  Error "Either SSL or NOSSL must be defined."
\</IfDefine>
\</IfDefine>

This directive is evaluated and configuration processing time, 
        not at runtime. As a result, this directive cannot be conditionally
        evaluated by enclosing it in an [\<If>](https://httpd.apache.org#if)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | What the server will return to the client in case of an error | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ErrorDocument` `error-code document` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

In the event of a problem or error, Apache httpd can be configured to do one of four things,

1. output a simple hardcoded error message
2. output a customized message
3. internally redirect to a local `URL-path` to handle the
      problem/error
4. redirect to an external `URL` to handle the
      problem/error

The first option is the default, while options 2-4 are
    configured using the `ErrorDocument`
    directive, which is followed by the HTTP response code and a URL
    or a message. Apache httpd will sometimes offer additional information
    regarding the problem/error.

From 2.4.13, [expression syntax](https://httpd.apache.org/expr.html) can be
    used inside the directive to produce dynamic strings and URLs.

URLs can begin with a slash (/) for local web-paths (relative
    to the [DocumentRoot](https://httpd.apache.org#documentroot)

```
ErrorDocument 500 http://example.com/cgi-bin/server-error.cgi
ErrorDocument 404 /errors/bad_urls.php
ErrorDocument 401 /subscription_info.html
ErrorDocument 403 "Sorry, can't allow you access today"
ErrorDocument 403 Forbidden!
ErrorDocument 403 /errors/forbidden.py?referrer=%{escape:%{HTTP_REFERER}}
```
    When the argument is a text string (i.e., not a path or URL),
    it is sent to the client with a content type of
    `text/html`, so you may include HTML markup. You can
    use the backslash line-continuation character to spread the
    document across multiple lines:

ErrorDocument 403 "\
\<html>\<head>\
\<title>403 Forbidden\</title>\
\</head>\<body>\
\<h1>Forbidden\</h1>\
\<p>You do not have permission to access this resource.\</p>\
\</body>\</html>"

Additionally, the special value `default` can be used
    to specify Apache httpd's simple hardcoded message.  While not required
    under normal circumstances, `default` will restore
    Apache httpd's simple hardcoded message for configurations that would
    otherwise inherit an existing `ErrorDocument`.

ErrorDocument 404 /cgi-bin/bad\_urls.pl
\<Directory "/web/docs">
  ErrorDocument 404 default
\</Directory>

Note that when you specify an `ErrorDocument`
    that points to a remote URL (ie. anything with a method such as
    `http` in front of it), Apache HTTP Server will send a redirect to the
    client to tell it where to find the document, even if the
    document ends up being on the same server. This has several
    implications, the most important being that the client will not
    receive the original error status code, but instead will
    receive a redirect status code. This in turn can confuse web
    robots and other clients which try to determine if a URL is
    valid using the status code. In addition, if you use a remote
    URL in an `ErrorDocument 401`, the client will not
    know to prompt the user for a password since it will not
    receive the 401 status code. Therefore, **if you use an
    `ErrorDocument 401` directive, then it must refer to a local
    document.**

Although most error messages can be overridden, there are certain
    circumstances where the internal messages are used regardless of the
    setting of `ErrorDocument`.  In
    particular, if a malformed request is detected, normal request processing
    will be immediately halted and the internal error message returned.
    This is necessary to guard against security problems caused by
    bad requests.

If you are using mod\_proxy, you may wish to enable
    [ProxyErrorOverride](https://httpd.apache.org/mod/mod_proxy.html#proxyerroroverride)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Location where the server will log errors | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) |  `ErrorLog` `file-path`\|syslog[:[`facility`][:`tag`]] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ErrorLog logs/error_log (Unix) ErrorLog logs/error.log (Windows and OS/2)` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ErrorLog` directive sets the name of
    the file to which the server will log any errors it encounters. If
    the `file-path` is not absolute then it is assumed to be
    relative to the [ServerRoot](https://httpd.apache.org#serverroot)

ErrorLog "/var/log/httpd/error\_log"

If the `file-path`
    begins with a pipe character "`|`" then it is assumed to be a
    command to spawn to handle the error log.

ErrorLog "|/usr/local/bin/httpd\_errors"

See the notes on [piped logs](https://httpd.apache.org/logs.html#piped) for
    more information.

Using `syslog` instead of a filename enables logging
    via syslogd(8) if the system supports it. The default is to use
    syslog facility `local7`, but you can override this by
    using the `syslog:` syntax where
    `facilityfacility` can be one of the names usually documented in
    syslog(1).  The facility is effectively global, and if it is changed
    in individual virtual hosts, the final facility specified affects the
    entire server. Same rules apply for the syslog tag, which by default
    uses the Apache binary name, `httpd` in most cases. You can
    also override this by using the `syslog::`
    syntax.`tag`

ErrorLog syslog:user
ErrorLog syslog:user:httpd.srv1
ErrorLog syslog::httpd.srv2

SECURITY: See the [security tips](https://httpd.apache.org/misc/security_tips.html#serverroot)
    document for details on why your security could be compromised
    if the directory where log files are stored is writable by
    anyone other than the user that starts the server.

When entering a file path on non-Unix platforms, care should be taken to make sure that only forward slashes are used even though the platform may allow the use of back slashes. In general it is a good idea to always use forward slashes throughout the configuration files.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Format specification for error log entries | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) |  `ErrorLogFormat [connection\|request]` `format` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

`ErrorLogFormat` allows to specify what
    supplementary information is logged in the error log in addition to the
    actual log message.

#Simple example
ErrorLogFormat "\[%t\] \[%l\] \[pid %P\] %F: %E: \[client %a\] %M"

Specifying `connection` or `request` as first
    parameter allows to specify additional formats, causing additional
    information to be logged when the first message is logged for a specific
    connection or request, respectively. This additional information is only
    logged once per connection/request. If a connection or request is processed
    without causing any log message, the additional information is not logged
    either.

It can happen that some format specifiers do not produce output.  For
    example, the Referer header is only present if the log message is
    associated to a request and the log message happens at a time when the
    Referer header has already been read from the client.  If no output is
    produced, the default behavior is to delete everything from the preceding
    space character to the next space character.  This means the format string is
    implicitly divided into fields on non-whitespace to whitespace transitions.
    If a format specifier does not produce output, the whole field is
    omitted.  For example, if the remote address `%a` in the log
    format `[%t] [%l] [%a] %M`  is not available, the surrounding
    brackets are not logged either.  Space characters can be escaped with a
    backslash to prevent them from delimiting a field.  The combination '% '
    (percent space) is a zero-width field delimiter that does not produce any
    output.

The above behavior can be changed by adding modifiers to the format
    string item. A `-` (minus) modifier causes a minus to be logged if the
    respective item does not produce any output. In once-per-connection/request
    formats, it is also possible to use the `+` (plus) modifier. If an
    item with the plus modifier does not produce any output, the whole line is
    omitted.

A number as modifier can be used to assign a log severity level to a format item. The item will only be logged if the log message has a severity level of the specified number or more severe (i.e., the message's level number is less than or equal to the modifier). The number can range from 1 (alert) over 4 (warn) and 7 (debug) to 15 (trace8).

For example, here's what would happen if you added modifiers to
    the `%{Referer}i` token, which logs the
    `Referer` request header.

| Modified Token | Meaning | 
|---|---|
| `%-{Referer}i` | Logs a `-` if `Referer` is not set. | 
| `%+{Referer}i` | Omits the entire line if `Referer` is not set. | 
| `%4{Referer}i` | Logs the `Referer` only if the log message severity     is 4 (warn) or more severe (i.e., levels 1 through 4:     alert, crit, error, warn). | 

Some format specifiers accept additional parameters in braces.

| Format String | Description | 
|---|---|
| `%%` | The percent sign | 
| `%a` | Client IP address and port of the request | 
| `%{c}a` | Underlying peer IP address and port of the connection (see the [mod_remoteip](https://httpd.apache.org/mod/mod_remoteip.html) module) | 
| `%A` | Local IP-address and port | 
| `%{`*name*}e | Request environment variable *name* | 
| `%E` | APR/OS error status code and string | 
| `%F` | Source file name and line number of the log call | 
| `%{`*name*}i | Request header *name* | 
| `%k` | Number of keep-alive requests on this connection | 
| `%l` | Loglevel of the message | 
| `%L` | Log ID of the request | 
| `%{c}L` | Log ID of the connection | 
| `%{C}L` | Log ID of the connection if used in connection scope, empty otherwise | 
| `%m` | Name of the module logging the message | 
| `%M` | The actual log message | 
| `%{`*name*}n | Request note *name* | 
| `%P` | Process ID of current process | 
| `%T` | Thread ID of current thread | 
| `%{g}T` | System unique thread ID of current thread (the same ID as             displayed by e.g. `top`; currently Linux only) | 
| `%t` | The current time | 
| `%{u}t` | The current time including micro-seconds | 
| `%{m}t` | The current time including milliseconds | 
| `%{cu}t` | The current time in ISO 8601 extended format (compact), including micro-seconds | 
| `%{cuz}t` | The current time in ISO 8601 extended format (compact), including micro-seconds and time zone in the ISO 8601:2000 standard format. Available since 2.4.58 only | 
| `%{%-format}t` | The current time formatted per the `strftime(3)` function. 	    Available since 2.4.58 only | 
| `%v` | The canonical [ServerName](https://httpd.apache.org#servername) of the current server. | 
| `%V` | The server name of the server serving the request according to the [UseCanonicalName](https://httpd.apache.org#usecanonicalname) setting. | 
| `\`  (backslash space) | Non-field delimiting space | 
| `%`  (percent space) | Field delimiter (no output) | 

The log ID format `%L` produces a unique id for a connection
    or request. This can be used to correlate which log lines belong to the
    same connection or request, which request happens on which connection.
    A `%L` format string is also available in
    [mod\_log\_config](https://httpd.apache.org/mod/mod_log_config.html)[mod\_unique\_id](https://httpd.apache.org/mod/mod_unique_id.html)

```
#Example (default format for threaded MPMs)
ErrorLogFormat "[%{u}t] [%-m:%l] [pid %P:tid %T] %7F: %E: [client\ %a] %M% ,\ referer\ %{Referer}i"
```
    This would result in error messages such as:

```
    [Thu May 12 08:28:57.652118 2011] [core:error] [pid 8777:tid 4326490112] [client ::1:58619] AH00124: Request exceeded the limit of 10 internal redirects due to probable configuration error
    
```

Notice that, as discussed above, some fields are omitted entirely because they are not defined.

```
#Example (similar to the 2.2.x format)
ErrorLogFormat "[%t] [%l] %7F: %E: [client\ %a] %M% ,\ referer\ %{Referer}i"
```
    ```
#Advanced example with request/connection log IDs
ErrorLogFormat "[%{uc}t] [%-m:%-l] [R:%L] [C:%{C}L] %7F: %E: %M"
ErrorLogFormat request "[%{uc}t] [R:%L] Request %k on C:%{c}L pid:%P tid:%T"
ErrorLogFormat request "[%{uc}t] [R:%L] UA:'%+{User-Agent}i'"
ErrorLogFormat request "[%{uc}t] [R:%L] Referer:'%+{Referer}i'"
ErrorLogFormat connection "[%{uc}t] [C:%{c}L] remote\ %a local\ %A"
```
| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Keep track of extended status information for each request | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ExtendedStatus On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ExtendedStatus Off[*]` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This option tracks additional data per worker about the
    currently executing request and creates a utilization summary.
    You can see these variables during runtime by configuring
    [mod\_status](https://httpd.apache.org/mod/mod_status.html)

This setting applies to the entire server and cannot be enabled or disabled on a virtualhost-by-virtualhost basis. The collection of extended status information can slow down the server. Also note that this setting cannot be changed during a graceful restart.

Note that loading [mod\_status](https://httpd.apache.org/mod/mod_status.html)[mod\_status](https://httpd.apache.org/mod/mod_status.html)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | File attributes used to create the ETag HTTP response header for static files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `FileETag` `component` ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `FileETag MTime Size` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | The default used to be "INode MTime Size" in 2.3.14 and earlier. | 

The `FileETag` directive configures the file
    attributes that are used to create the `ETag` (entity
    tag) response header field when the document is based on a static file.
    (The `ETag` value is used in cache management to save
    network bandwidth.) The
    `FileETag` directive allows you to choose
    which of these -- if any -- should be used. The recognized keywords are:

- **INode**
- The file's i-node number will be included in the calculation
- **MTime**
- The date and time the file was last modified will be included
- **Size**
- The number of bytes in the file will be included
- **All**
- All available fields will be used. This is equivalent to:
         FileETag INode MTime Size
- **Digest**
- If a document is file-based, the `ETag` field will be
       calculated by taking the digest over the file.
- **None**
- If a document is file-based, no `ETag` field will be
       included in the response

The `INode`, `MTime`, `Size` and
    `Digest` keywords may be prefixed with either `+`
    or `-`, which allow changes to be made to the default setting
    inherited from a broader scope. Any keyword appearing without such a prefix
    immediately and completely cancels the inherited setting.

If a directory's configuration includes
    `FileETag INode MTime Size`, and a
    subdirectory's includes `FileETag -INode`,
    the setting for that subdirectory (which will be inherited by
    any sub-subdirectories that don't override it) will be equivalent to
    `FileETag MTime Size`.

[mod_include](https://httpd.apache.org/mod/mod_include.html)
| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply to matched filenames | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<Files` `filename`> ... </Files> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `<Files>` directive
    limits the scope of the enclosed directives by filename. It is comparable
    to the [\<Directory>](https://httpd.apache.org#directory)[\<Location>](https://httpd.apache.org#location)`</Files>`
    directive. The directives given within this section will be applied to
    any object with a basename (last component of filename) matching the
    specified filename. `<Files>`
    sections are processed in the order they appear in the
    configuration file, after the [\<Directory>](https://httpd.apache.org#directory)`.htaccess` files are read, but before [\<Location>](https://httpd.apache.org#location)`<Files>` can be nested
    inside [\<Directory>](https://httpd.apache.org#directory)

The `filename` argument should include a filename, or
    a wild-card string, where `?` matches any single character,
    and `*` matches any sequence of characters.

```
<Files "cat.html">
    # Insert stuff that applies to cat.html here
</Files>
<Files "?at.*">
    # This would apply to cat.html, bat.html, hat.php and so on.
</Files>
```
    ```
<Files ~ "\.(gif|jpe?g|png)$">
    #...
</Files>
```
    would match most common Internet graphics formats. [\<FilesMatch>](https://httpd.apache.org#filesmatch)

Note that unlike [\<Directory>](https://httpd.apache.org#directory)[\<Location>](https://httpd.apache.org#location)`<Files>` sections can be used inside
    `.htaccess` files. This allows users to control access to
    their own files, at a file-by-file level.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply to regular-expression matched filenames | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<FilesMatch` `regex`> ... </FilesMatch> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `<FilesMatch>` directive
    limits the scope of the enclosed directives by filename, just as the
    [\<Files>](https://httpd.apache.org#files)[regular
    expression](https://httpd.apache.org/glossary.html#regex). For example:

```
<FilesMatch ".+\.(gif|jpe?g|png)$">
    # ...
</FilesMatch>
```
    would match most common Internet graphics formats.

The `.+` at the start of the regex ensures that
    files named `.png`, or `.gif`, for example,
    are not matched.

From 2.4.8 onwards, named groups and backreferences are captured and
    written to the environment with the corresponding name prefixed with
    "MATCH\_" and in upper case. This allows elements of files to be referenced
    from within [expressions](https://httpd.apache.org/expr.html) and modules like
    [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)

```
<FilesMatch "^(?<sitename>[^/]+)">
    Require ldap-group cn=%{env:MATCH_SITENAME},ou=combined,o=Example
</FilesMatch>
```
| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Maximum number of pipelined responses above which they are flushed to the network | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `FlushMaxPipelined` `number` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `FlushMaxPipelined 5` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.4.47 and later | 

This directive allows to configure the maximum number of pipelined responses, which remain pending so long as pipelined request are received. When the limit is reached, responses are forcibly flushed to the network in blocking mode, until passing under the limit again.

`FlushMaxPipelined` helps constraining memory
    usage. When set to `0` pipelining is disabled, when set to
    `-1` there is no limit ([FlushMaxThreshold](https://httpd.apache.org#flushmaxthreshold)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Threshold above which pending data are flushed to the network | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `FlushMaxThreshold` `number-of-bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `FlushMaxThreshold 65535` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.4.47 and later | 

This directive allows to configure the threshold for pending output data (in bytes). When the limit is reached, data are forcibly flushed to the network in blocking mode, until passing under the limit again.

`FlushMaxThreshold` helps constraining memory
    usage. When set to `0` or a too small value there are actually
    no pending data, but for threaded MPMs there can be more threads busy
    waiting for the network thus less ones available to handle the other
    simultaneous connections.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Forces all matching files to be served with the specified media type in the HTTP Content-Type header field | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ForceType` `media-type`\|None | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

When placed into an `.htaccess` file or a
    [\<Directory>](https://httpd.apache.org#directory)[\<Location>](https://httpd.apache.org#location)[\<Files>](https://httpd.apache.org#files)`media-type`. For example, if you had a directory full of
    GIF files, but did not want to label them all with `.gif`,
    you might want to use:

ForceType image/gif

Note that this directive overrides other indirect media type
    associations defined in mime.types or via the
    [AddType](https://httpd.apache.org/mod/mod_mime.html#addtype)

You can also override more general
    `ForceType` settings
    by using the value of `None`:

\# force all files to be image/gif:
\<Location "/images">
  ForceType image/gif
\</Location>
# but normal mime-type associations here:
\<Location "/images/mixed">
  ForceType None
\</Location>

This directive primarily overrides the content types generated for static files served out of the filesystem. For resources other than static files, where the generator of the response typically specifies a Content-Type, this directive has no effect.

When explicit directives such as
    [SetHandler](https://httpd.apache.org#sethandler)[AddHandler](https://httpd.apache.org/mod/mod_mime.html#addhandler)[SetHandler](https://httpd.apache.org#sethandler)[AddHandler](https://httpd.apache.org/mod/mod_mime.html#addhandler)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Directory to write gmon.out profiling data to. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `GprofDir` `/tmp/gprof/`\|`/tmp/gprof/`% | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

When the server has been compiled with gprof profiling support,
    `GprofDir` causes `gmon.out` files to
    be written to the specified directory when the process exits.  If the
    argument ends with a percent symbol ('%'), subdirectories are created
    for each process id.

This directive currently only works with the [prefork](https://httpd.apache.org/mod/prefork.html)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enables DNS lookups on client IP addresses | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `HostnameLookups On\|Off\|Double` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `HostnameLookups Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive enables DNS lookups so that host names can be
    logged (and passed to CGIs/SSIs in `REMOTE_HOST`).
    The value `Double` refers to doing double-reverse
    DNS lookup. That is, after a reverse lookup is performed, a forward
    lookup is then performed on that result. At least one of the IP
    addresses in the forward lookup must match the original
    address. (In "tcpwrappers" terminology this is called
    `PARANOID`.)

Regardless of the setting, when [mod\_authz\_host](https://httpd.apache.org/mod/mod_authz_host.html)`HostnameLookups Double`. For example, if only
    `HostnameLookups On` and a request is made to an object
    that is protected by hostname restrictions, regardless of whether
    the double-reverse fails or not, CGIs will still be passed the
    single-reverse result in `REMOTE_HOST`.

The default is `Off` in order to save the network
    traffic for those sites that don't truly need the reverse
    lookups done. It is also better for the end users because they
    don't have to suffer the extra latency that a lookup entails.
    Heavily loaded sites should leave this directive
    `Off`, since DNS lookups can take considerable
    amounts of time. The utility [logresolve](https://httpd.apache.org/programs/logresolve.html)`bin` subdirectory of your installation
    directory, can be used to look up host names from logged IP addresses
    offline.

Finally, if you have [hostname-based Require
    directives](https://httpd.apache.org/mod_authz_host.html#reqhost), a hostname lookup will be performed regardless of
    the setting of `HostnameLookups`.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Modify restrictions on HTTP Request Messages | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | ``` HttpProtocolOptions [Strict\|Unsafe] [RegisteredMethods\|LenientMethods]  [Allow0.9\|Require1.0] ```  | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `HttpProtocolOptions Strict LenientMethods Allow0.9` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.2.32 or 2.4.24 and later | 

This directive changes the rules applied to the HTTP Request Line
    ([RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#section-3.1.1)) and the HTTP Request Header Fields
    ([RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#section-3.2)), which are now applied by default or using
    the `Strict` option. Due to legacy modules, applications or
    custom user-agents which must be deprecated the `Unsafe`
    option has been added to revert to the legacy behaviors.

These rules are applied prior to request processing, so must be configured at the global or default (first) matching virtual host section, by IP/port interface (and not by name) to be honored.

The directive accepts three parameters from the following list of choices, applying the default to the ones not specified:

- Strict|Unsafe
- Prior to the introduction of this directive, the Apache HTTP Server
      request message parsers were tolerant of a number of forms of input
      which did not conform to the protocol.
      [RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#section-9.4) (Request Splitting) and [RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#section-9.5) (Response Smuggling) call out only two of the potential
      risks of accepting non-conformant request messages, while [RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#section-3.5) "Message Parsing Robustness" identify the
      risks of accepting obscure whitespace and request message formatting. 
      As of the introduction of this directive, all grammar rules of the
      specification are enforced in the default `Strict` operating
      mode, and the strict whitespace suggested by section 3.5 is enforced
      and cannot be relaxed.
### Security risks of Unsafe Users are strongly cautioned against toggling the `Unsafe` mode of operation, particularly on outward-facing, publicly accessible
        server deployments.  If an interface is required for faulty monitoring
        or other custom service consumers running on an intranet, users should
        toggle the Unsafe option only on a specific virtual host configured
        to service their internal private network.
### Example of a request leading to HTTP 400 with Strict mode ```
        
        # Missing CRLF
```
GET / HTTP/1.0\n\n
### Command line tools and CRLF Some tools need to be forced to use CRLF, otherwise httpd will return
        a HTTP 400 response like described in the above use case. For example,
        the **OpenSSL s\_client needs the -crlf parameter to work
        properly**.
The [DumpIOInput](https://httpd.apache.org/mod/mod_dumpio.html#dumpioinput)
- RegisteredMethods|LenientMethods
- [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-4.1) "Request Methods" "Overview" requires that
      origin servers shall respond with a HTTP 501 status code when an
      unsupported method is encountered in the request line.
      This already happens when the `LenientMethods` option is used,
      but administrators may wish to toggle the `RegisteredMethods` option and register any non-standard methods using the [RegisterHttpMethod](https://httpd.apache.org#registerhttpmethod)`Unsafe` option has been toggled.
### Forward Proxy compatibility The `RegisteredMethods` option should **not** be toggled for forward proxy hosts, as the methods supported by the
        origin servers are unknown to the proxy server.
### Example of a request leading to HTTP 501 with LenientMethods mode ```
        
        # Unknown HTTP method
```
WOW / HTTP/1.0\r\n\r\n
# Lowercase HTTP method
get / HTTP/1.0\r\n\r\n
- Allow0.9|Require1.0
- [RFC 2616](https://www.rfc-editor.org/rfc/rfc2616#section-19.6) "Compatibility With Previous Versions" had
      encouraged HTTP servers to support legacy HTTP/0.9 requests. RFC 7230
      supersedes this with "The expectation to support HTTP/0.9 requests has
      been removed" and offers additional comments in [RFC 7230](https://www.rfc-editor.org/rfc/rfc7230#appendix-A) Appendix A. The `Require1.0` option allows
      the user to remove support of the default `Allow0.9` option's
      behavior.
### Example of a request leading to HTTP 400 with Require1.0 mode ```
        
        # Unsupported HTTP version
```
GET /\r\n\r\n

Reviewing the messages logged to the
    [ErrorLog](https://httpd.apache.org#errorlog)[LogLevel](https://httpd.apache.org#loglevel)`debug` level,
    can help identify such faulty requests along with their origin.
    Users should pay particular attention to the 400 responses in the access
    log for invalid requests which were unexpectedly rejected.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply only if a condition is satisfied by a request at runtime | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<If` `expression`> ... </If> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Nested conditions are evaluated in 2.4.26 and later | 

The `<If>` directive
    evaluates an expression at runtime, and applies the enclosed
    directives if and only if the expression evaluates to true.
    For example:

`<If "-z req('Host')">`
    would match HTTP/1.0 requests without a `Host:` header.
    Expressions may contain various shell-like operators for string
    comparison (`==`, `!=`, `<`, ...),
    integer comparison (`-eq`, `-ne`, ...),
    and others (`-n`, `-z`, `-f`, ...).
    It is also possible to use regular expressions,

`<If "%{QUERY_STRING} =~ /(delete|commit)=.*?elem/">`
    shell-like pattern matches and many other operations. These operations
    can be done on request headers (`req`), environment variables
    (`env`), and a large number of other properties. The full
    documentation is available in [Expressions in
    Apache HTTP Server](https://httpd.apache.org/expr.html).

Only directives that support the [directory context](https://httpd.apache.org/directive-dict.html#Context) can be used within this configuration section.

Certain variables, such as `CONTENT_TYPE` and other
    response headers, are set after \<If> conditions have already
    been evaluated, and so will not be available to use in this
    directive.

Directives that take affect during configuration parsing, such as 
    `Define`, `Include`, and
    `Error` cannot be made conditional by enclosing
    them in an if `<If>` configuration
    section.  These sections are always part of the configuration, 
    regardless of how they evaluate at runtime.

- [Expressions in Apache HTTP Server](https://httpd.apache.org/expr.html),
for a complete reference and more examples.
- [<ElseIf>](https://httpd.apache.org#elseif)
- [<Else>](https://httpd.apache.org#else)
- [How \<Directory>, \<Location>,
    \<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these
    different sections are combined when a request is received. `<If>`, `<ElseIf>`, and `<Else>` are applied last.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Encloses directives that will be processed only if a test is true at startup | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<IfDefine [!]``parameter-name`> ...     </IfDefine> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `<IfDefine`  section is used to mark directives that are conditional. The
    directives within an `test`>...\</IfDefine>
    `<IfDefine>`
    section are only processed if the `test` is true. If 
    `test` is false, everything between the start and end markers is
    ignored.

The `test` in the `<IfDefine>` section directive can be one of two forms:

- `parameter-name`
- `!``parameter-name`

In the former case, the directives between the start and end
    markers are only processed if the parameter named
    `parameter-name` is defined. The second format reverses
    the test, and only processes the directives if
    `parameter-name` is **not** defined.

The `parameter-name` argument is a define as given on the
    [httpd](https://httpd.apache.org/programs/httpd.html)`-D` at the time the server was started or by the `parameter`
    [Define](https://httpd.apache.org#define)

`<IfDefine>` sections are
    nest-able, which can be used to implement simple
    multiple-parameter tests. Example:

`httpd -DReverseProxy -DUseCache -DMemCache ...`

```
<IfDefine ReverseProxy>
  LoadModule proxy_module   modules/mod_proxy.so
  LoadModule proxy_http_module   modules/mod_proxy_http.so
  <IfDefine UseCache>
    LoadModule cache_module   modules/mod_cache.so
    <IfDefine MemCache>
      LoadModule mem_cache_module   modules/mod_mem_cache.so
    </IfDefine>
    <IfDefine !MemCache>
      LoadModule cache_disk_module   modules/mod_cache_disk.so
    </IfDefine>
  </IfDefine>
</IfDefine>
```
| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Encloses directives that are processed conditional on the presence or absence of a specific directive | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<IfDirective [!]``directive-name`> ...     </IfDirective> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in 2.4.34 and later. | 

The `<IfDirective` 
    section is used to mark directives that are conditional on the presence of
    a specific directive. The directives within an `test`>...\</IfDirective>`<IfDirective>` section are only processed if the `test`
    is true. If `test` is false, everything between the start and
    end markers is ignored.

The `test` in the `<IfDirective>` section can be one of two forms:

- `directive-name`
- !`directive-name`

In the former case, the directives between the start and end
    markers are only processed if a directive of the given name is
    available at the time of processing.  The second format reverses the test,
    and only processes the directives if `directive-name` is
    **not** available.

This section should only be used if you need to have one
    configuration file that works across multiple versions of
    [httpd](https://httpd.apache.org/programs/httpd.html)`<IfDirective>`
    sections.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Encloses directives that will be processed only if file exists at startup | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<IfFile [!]``filename`> ...     </IfFile> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in 2.4.34 and later. | 

The `<IfFile`  section is used to mark directives that are conditional on
    the existence of a file on disk. The directives within an
    `filename`>...\</IfFile>
    `<IfFile>` section are only
    processed if `filename` exists. If `filename`
    doesn't exist, everything between the start and end markers is
    ignored. `filename` can be an absolute path or a path
    relative to the server root.

The `filename` in the `<IfFile>` section directive can take the same forms as the
    `test` variable in the [\<IfDefine>](https://httpd.apache.org#ifdefine)```
    !
```
 character is placed directly before `filename`.

If a relative `filename` is supplied, the check is
    [ServerRoot](https://httpd.apache.org#serverroot)[ServerRoot](https://httpd.apache.org#serverroot)`-d`
    parameter.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Encloses directives that are processed conditional on the presence or absence of a specific module | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<IfModule [!]``module-file`\|`module-identifier`> ...     </IfModule> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Module identifiers are available in version 2.1 and later. | 

The `<IfModule` 
    section is used to mark directives that are conditional on the presence of
    a specific module. The directives within an `test`>...\</IfModule>`<IfModule>` section are only processed if the `test`
    is true. If `test` is false, everything between the start and
    end markers is ignored.

The `test` in the `<IfModule>` section directive can be one of two forms:

- `module`
- !`module`

In the former case, the directives between the start and end
    markers are only processed if the module named `module`
    is included in Apache httpd -- either compiled in or
    dynamically loaded using [LoadModule](https://httpd.apache.org/mod/mod_so.html#loadmodule)`module` is
    **not** included.

The `module` argument can be either the module identifier or
    the file name of the module, at the time it was compiled.  For example,
    `rewrite_module` is the identifier and
    `mod_rewrite.c` is the file name. If a module consists of
    several source files, use the name of the file containing the string
    `STANDARD20_MODULE_STUFF`.

`<IfModule>` sections are
    nest-able, which can be used to implement simple multiple-module
    tests.

This section should only be used if you need to have one
    configuration file that works whether or not a specific module
    is available. In normal operation, directives need not be
    placed in `<IfModule>`
    sections.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Encloses directives that are processed conditional on the presence or absence of a specific section directive | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<IfSection [!]``section-name`> ...     </IfSection> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in 2.4.34 and later. | 

The ```
<IfSection
    
```
 section is used
    to mark directives that are conditional on the presence of a
    specific section directive.  A section directive is any directive
    such as `test`>...\</IfSection>`<VirtualHost>` which
    encloses other directives, and has a directive name with a leading
    "\<".

The directives within an `<IfSection>` section are only processed if the `test`
    is true. If `test` is false, everything between the start and
    end markers is ignored.

The `section-name` must be specified without either
    the leading "\<" or closing ">".  The `test` in the
    `<IfSection>` section can be one
    of two forms:

- `section-name`
- !`section-name`

In the former case, the directives between the start and end
    markers are only processed if a section directive of the given
    name is available at the time of processing.  The second format
    reverses the test, and only processes the directives if
    `section-name` is **not** an available
    section directive.

For example:

\<IfSection VirtualHost>
   ...
\</IfSection>

This section should only be used if you need to have one
    configuration file that works across multiple versions of [httpd](https://httpd.apache.org/programs/httpd.html)`<IfSection>` sections.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Includes other configuration files from within the server configuration files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Include` `file-path`\|`directory-path`\|`wildcard` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Directory wildcard matching available in 2.3.6 and later | 

This directive allows inclusion of other configuration files from within the server configuration files.

Shell-style (`fnmatch()`) wildcard characters can be used
    in the filename or directory parts of the path to include several files
    at once, in alphabetical order. In addition, if
    `Include` points to a directory, rather than a file,
    Apache httpd will read all files in that directory and any subdirectory.
    However, including entire directories is not recommended, because it is
    easy to accidentally leave temporary files in a directory that can cause
    [httpd](https://httpd.apache.org/programs/httpd.html)

The `Include` directive will
    **fail with an error** if a wildcard expression does not
    match any file. The [IncludeOptional](https://httpd.apache.org#includeoptional)

The file path specified may be an absolute path, or may be relative
    to the [ServerRoot](https://httpd.apache.org#serverroot)

Examples:

Include /usr/local/apache2/conf/ssl.conf
Include /usr/local/apache2/conf/vhosts/\*.conf

Or, providing paths relative to your [ServerRoot](https://httpd.apache.org#serverroot)

Include conf/ssl.conf
Include conf/vhosts/\*.conf

Wildcards may be included in the directory or file portion of the path. This example will fail if there is no subdirectory in conf/vhosts that contains at least one \*.conf file:

Include conf/vhosts/\*/\*.conf

Alternatively, the following command will just be ignored in case of missing files or directories:

IncludeOptional conf/vhosts/\*/\*.conf

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Includes other configuration files from within the server configuration files | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `IncludeOptional` `file-path`\|`directory-path`\|`wildcard` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in 2.3.6 and later. Not existent file paths without wildcards do not cause SyntaxError after 2.4.30 | 

This directive allows inclusion of other configuration files
    from within the server configuration files. It works identically to the
    [Include](https://httpd.apache.org#include)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Enables HTTP persistent connections | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `KeepAlive On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `KeepAlive On` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The Keep-Alive extension to HTTP/1.0 and the persistent
    connection feature of HTTP/1.1 provide long-lived HTTP sessions
    which allow multiple requests to be sent over the same TCP
    connection. In some cases this has been shown to result in an
    almost 50% speedup in latency times for HTML documents with
    many images. To enable Keep-Alive connections, set
    `KeepAlive On`.

For HTTP/1.0 clients, Keep-Alive connections will only be used if they are specifically requested by a client. In addition, a Keep-Alive connection with an HTTP/1.0 client can only be used when the length of the content is known in advance. This implies that dynamic content such as CGI output, SSI pages, and server-generated directory listings will generally not use Keep-Alive connections to HTTP/1.0 clients. For HTTP/1.1 clients, persistent connections are the default unless otherwise specified. If the client requests it, chunked encoding will be used in order to send content of unknown length over persistent connections.

When a client uses a Keep-Alive connection, it will be counted
    as a single "request" for the [MaxConnectionsPerChild](https://httpd.apache.org/mod/mpm_common.html#maxconnectionsperchild)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Amount of time the server will wait for subsequent requests on a persistent connection | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `KeepAliveTimeout` `num`[ms] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `KeepAliveTimeout 5` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The number of seconds Apache httpd will wait for a subsequent
    request before closing the connection. By adding a postfix of ms the
    timeout can be also set in milliseconds. Once a request has been
    received, the timeout value specified by the
    [Timeout](https://httpd.apache.org#timeout)

Setting `KeepAliveTimeout` to a high value
    may cause performance problems in heavily loaded servers. The
    higher the timeout, the more server processes will be kept
    occupied waiting on connections with idle clients.

If `KeepAliveTimeout` is **not**
    set for a name-based virtual host, the value of the first defined
    virtual host best matching the local IP and port will be used.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Restrict enclosed access controls to only certain HTTP methods | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<Limit` `method` [`method`] ... > ...     </Limit> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | AuthConfig, Limit | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Access controls are normally effective for
    **all** access methods, and this is the usual
    desired behavior. **In the general case, access control
    directives should not be placed within a
    `<Limit>` section.**

The purpose of the `<Limit>`
    directive is to restrict the effect of the access controls to the
    nominated HTTP methods. For all other methods, the access
    restrictions that are enclosed in the `<Limit>` bracket **will have no
    effect**. The following example applies the access control
    only to the methods `POST`, `PUT`, and
    `DELETE`, leaving all other methods unprotected:

\<Limit POST PUT DELETE>
  Require valid-user
\</Limit>

The method names listed can be one or more of: `GET`,
    `POST`, `PUT`, `DELETE`,
    `CONNECT`, `OPTIONS`,
    `PATCH`, `PROPFIND`, `PROPPATCH`,
    `MKCOL`, `COPY`, `MOVE`,
    `LOCK`, and `UNLOCK`. **The method name is
    case-sensitive.** If `GET` is used, it will also
    restrict `HEAD` requests. The `TRACE` method
    cannot be limited (see [TraceEnable](https://httpd.apache.org#traceenable)

A [<LimitExcept>](https://httpd.apache.org#limitexcept)`<Limit>`
    section when restricting access, since a [<LimitExcept>](https://httpd.apache.org#limitexcept)[configuration sections
    merging documentation](https://httpd.apache.org/sections.html#merging) for a warning about how
    `<Limit>` inside
    [<Location>](https://httpd.apache.org#location)[<Directory>](https://httpd.apache.org#directory)

The `<Limit>` and
    [\<LimitExcept>](https://httpd.apache.org#limitexcept)`<Limit>` or [\<LimitExcept>](https://httpd.apache.org#limitexcept)

When using
    `<Limit>` or
    `<LimitExcept>` directives with
    the [Require](https://httpd.apache.org/mod/mod_authz_core.html#require)[Require](https://httpd.apache.org/mod/mod_authz_core.html#require)[Require](https://httpd.apache.org/mod/mod_authz_core.html#require)

For example, given the following configuration, all users will
    be authorized for `POST` requests, and the
    `Require group editors` directive will be ignored
    in all cases:

\<LimitExcept GET>
  Require valid-user
\</LimitExcept>
\<Limit POST>
  Require group editors
\</Limit>

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Restrict access controls to all HTTP methods except the named ones | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `<LimitExcept` `method` [`method`] ... > ...     </LimitExcept> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | AuthConfig, Limit | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

`<LimitExcept>` and
    `</LimitExcept>` are used to enclose
    a group of access control directives which will then apply to any
    HTTP access method **not** listed in the arguments;
    i.e., it is the opposite of a [\<Limit>](https://httpd.apache.org#limit)[\<Limit>](https://httpd.apache.org#limit)

\<LimitExcept POST GET>
  Require valid-user
\</LimitExcept>

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine maximum number of internal redirects and nested subrequests | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitInternalRecursion` `number` [`number`] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitInternalRecursion 10` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

An internal redirect happens, for example, when using the [Action](https://httpd.apache.org/mod/mod_actions.html#action)[mod\_dir](https://httpd.apache.org/mod/mod_dir.html)[DirectoryIndex](https://httpd.apache.org/mod/mod_dir.html#directoryindex)

`LimitInternalRecursion` prevents the server
    from crashing when entering an infinite loop of internal redirects or
    subrequests. Such loops are usually caused by misconfigurations.

The directive stores two different limits, which are evaluated on
    per-request basis. The first `number` is the maximum number of
    internal redirects that may follow each other. The second `number`
    determines how deeply subrequests may be nested. If you specify only one
    `number`, it will be assigned to both limits.

LimitInternalRecursion 5

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Restricts the total size of the HTTP request body sent from the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitRequestBody` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitRequestBody 1073741824` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | In Apache HTTP Server 2.4.53 and earlier, the default value was 0 (unlimited) | 

This directive specifies the number of `bytes`
    that are allowed in a request body. A value of `0` means unlimited.

The `LimitRequestBody` directive allows
    the user to set a limit on the allowed size of an HTTP request
    message body within the context in which the directive is given
    (server, per-directory, per-file or per-location). If the client
    request exceeds that limit, the server will return an error
    response instead of servicing the request. The size of a normal
    request message body will vary greatly depending on the nature of
    the resource and the methods allowed on that resource. CGI scripts
    typically use the message body for retrieving form information.
    Implementations of the `PUT` method will require
    a value at least as large as any representation that the server
    wishes to accept for that resource.

This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks.

If, for example, you are permitting file upload to a particular location and wish to limit the size of the uploaded file to 100K, you might use the following directive:

LimitRequestBody 102400

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the number of HTTP request header fields that will be accepted from the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitRequestFields` `number` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitRequestFields 100` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Setting `number` at 0 means unlimited.
    The default value is defined by the compile-time
    constant `DEFAULT_LIMIT_REQUEST_FIELDS` (100 as
    distributed).

The `LimitRequestFields` directive allows
    the server administrator to modify the limit on the number of
    request header fields allowed in an HTTP request. A server needs
    this value to be larger than the number of fields that a normal
    client request might include. The number of request header fields
    used by a client rarely exceeds 20, but this may vary among
    different client implementations, often depending upon the extent
    to which a user has configured their browser to support detailed
    content negotiation. Optional HTTP extensions are often expressed
    using request header fields.

This directive gives the server administrator greater control over abnormal client request behavior, which may be useful for avoiding some forms of denial-of-service attacks. The value should be increased if normal clients see an error response from the server that indicates too many fields were sent in the request.

LimitRequestFields 50

When name-based virtual hosting is used, the value for this directive is taken from the default (first-listed) virtual host for the local IP and port combination.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the size of the HTTP request header allowed from the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitRequestFieldSize` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitRequestFieldSize 8190` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive specifies the number of `bytes`
    that will be allowed in an HTTP request header.

The `LimitRequestFieldSize` directive
    allows the server administrator to set the limit
    on the allowed size of an HTTP request header field. A server
    needs this value to be large enough to hold any one header field
    from a normal client request. The size of a normal request header
    field will vary greatly among different client implementations,
    often depending upon the extent to which a user has configured
    their browser to support detailed content negotiation. SPNEGO
    authentication headers can be up to 12392 bytes.

LimitRequestFieldSize 4094

Under normal conditions, the value should not be changed from
    the default.

When name-based virtual hosting is used, the value for this directive is taken from the default (first-listed) virtual host best matching the current IP address and port combination.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limit the size of the HTTP request line that will be accepted from the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitRequestLine` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitRequestLine 8190` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive sets the number of `bytes` that will be
    allowed on the HTTP request-line.

The `LimitRequestLine` directive allows
    the server administrator to set the limit on the allowed size
    of a client's HTTP request-line. Since the request-line consists of the
    HTTP method, URI, and protocol version, the
    `LimitRequestLine` directive places a
    restriction on the length of a request-URI allowed for a request
    on the server. A server needs this value to be large enough to
    hold any of its resource names, including any information that
    might be passed in the query part of a `GET` request.

LimitRequestLine 4094

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the size of an XML-based request body | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LimitXMLRequestBody` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LimitXMLRequestBody 1000000` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Limit (in bytes) on the maximum size of an XML-based request
    body. A value of `0` will apply a hard limit (depending on
    32bit vs 64bit system) allowing for XML escaping within the bounds of
    the system addressable memory, but it exists for compatibility only
    and is not recommended since it does not account for memory consumed
    elsewhere or concurrent requests, which might result in an overall
    system out-of-memory.

\# Limit of 1 MiB
LimitXMLRequestBody 1048576

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Applies the enclosed directives only to matching URLs | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | ``` <Location      ``` `URL-path`\|`URL`> ... </Location> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `<Location>` directive
    limits the scope of the enclosed directives by URL. It is similar to the
    [\<Directory>](https://httpd.apache.org#directory)`</Location>` directive. `<Location>` sections are processed in the
    order they appear in the configuration file, after the [\<Directory>](https://httpd.apache.org#directory)`.htaccess` files are read, and after the [\<Files>](https://httpd.apache.org#files)

`<Location>` sections operate
    completely outside the filesystem.  This has several consequences.
    Most importantly, `<Location>`
    directives should not be used to control access to filesystem
    locations.  Since several different URLs may map to the same
    filesystem location, such access controls may by circumvented.

The enclosed directives will be applied to the request if the path component
    of the URL meets *any* of the following criteria:

- The specified location matches exactly the path component of the URL.
- The specified location, which ends in a forward slash, is a prefix of the path component of the URL (treated as a context root).
- The specified location, with the addition of a trailing slash, is a prefix of the path component of the URL (also treated as a context root).

In the example below, where no trailing slash is used, requests to /private1, /private1/ and /private1/file.txt will have the enclosed directives applied, but /private1other would not.

```
<Location "/private1">
    #  ...
</Location>
```
    In the example below, where a trailing slash is used, requests to /private2/ and /private2/file.txt will have the enclosed directives applied, but /private2 and /private2other would not.

\<Location "/private2*/*">
    # ...
\</Location>

Use `<Location>` to apply
    directives to content that lives outside the filesystem.  For
    content that lives in the filesystem, use [\<Directory>](https://httpd.apache.org#directory)[\<Files>](https://httpd.apache.org#files)`<Location "/">`, which is an easy way to
    apply a configuration to the entire server.

For all origin (non-proxy) requests, the URL to be matched is a
    URL-path of the form `/path/`.  *No scheme, hostname,
    port, or query string may be included.*  For proxy requests, the
    URL to be matched depends on the type of proxy. With a
    **forward** proxy ([ProxyRequests](https://httpd.apache.org/mod/mod_proxy.html#proxyrequests)`scheme://servername/path`, and you must include the
    prefix. With a **reverse** proxy (configured via
    [ProxyPass](https://httpd.apache.org/mod/mod_proxy.html#proxypass)[RewriteRule ... \[P\]](<https://httpd.apache.org/mod/mod_proxy.html#rewriterule ... [p]>)`/path/`
    just as you would for origin requests.

The URL may use wildcards. In a wild-card string, `?` matches
    any single character, and `*` matches any sequence of
    characters. Neither wildcard character matches a / in the URL-path.

```
<Location ~ "/(extra|special)/data">
    #...
</Location>
```
    would match URLs that contained the substring `/extra/data`
    or `/special/data`. The directive [\<LocationMatch>](https://httpd.apache.org#locationmatch)`<Location>`, and is preferred, for the
    simple reason that `~` is hard to distinguish from
    `-` in many fonts.

The `<Location>`
    functionality is especially useful when combined with the
    [SetHandler](https://httpd.apache.org#sethandler)`example.com`, you might use:

\<Location "/status">
  SetHandler server-status
  Require host example.com
\</Location>

The slash character has special meaning depending on where in a
      URL it appears. People may be used to its behavior in the filesystem
      where multiple adjacent slashes are frequently collapsed to a single
      slash (*i.e.*, `/home///foo` is the same as
      `/home/foo`). In URL-space this is not necessarily true if
      directive [MergeSlashes](https://httpd.apache.org#mergeslashes)[\<LocationMatch>](https://httpd.apache.org#locationmatch)`<Location>` require you to explicitly specify multiple
      slashes if the slashes are not being merged.

For example, `<LocationMatch "^/abc">` would match
      the request URL `/abc` but not the request URL ```
      //abc
```
. The (non-regex) `<Location>` directive behaves similarly when used for
      proxy requests. But when (non-regex) `<Location>` is used for non-proxy requests it will
      implicitly match multiple slashes with a single slash. For example,
      if you specify `<Location "/abc/def">` and the
      request is to `/abc//def` then it will match.

- [How \<Directory>, \<Location>
    and \<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these
    different sections are combined when a request is received.
- [LocationMatch](https://httpd.apache.org#locationmatch)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Applies the enclosed directives only to regular-expression matching URLs | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | ``` <LocationMatch      ``` `regex`> ... </LocationMatch> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `<LocationMatch>` directive
    limits the scope of the enclosed directives by URL, in an identical manner
    to [\<Location>](https://httpd.apache.org#location)[regular expression](https://httpd.apache.org/glossary.html#regex)
    as an argument instead of a simple string. For example:

```
<LocationMatch "/(extra|special)/data">
    # ...
</LocationMatch>
```
    If the intent is that a URL **starts with**
    `/extra/data`, rather than merely
    **contains** `/extra/data`, prefix the
    regular expression with a `^` to require this.

\<LocationMatch "^/(extra|special)/data">

From 2.4.8 onwards, named groups and backreferences are captured and
    written to the environment with the corresponding name prefixed with
    "MATCH\_" and in upper case. This allows elements of URLs to be referenced
    from within [expressions](https://httpd.apache.org/expr.html) and modules like
    [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)

```
<LocationMatch "^/combined/(?<sitename>[^/]+)">
    Require ldap-group cn=%{env:MATCH_SITENAME},ou=combined,o=Example
</LocationMatch>
```
     The slash character has special meaning depending on where in a
      URL it appears. People may be used to its behavior in the filesystem
      where multiple adjacent slashes are frequently collapsed to a single
      slash (*i.e.*, `/home///foo` is the same as
      `/home/foo`). In URL-space this is not necessarily true if
      directive [MergeSlashes](https://httpd.apache.org#mergeslashes)`<LocationMatch>`
      directive and the regex version of `<Location>` require you to explicitly specify multiple
      slashes if the slashes are not being merged.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls the verbosity of the ErrorLog | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `LogLevel [``module`:]`level` [`module`:`level`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `LogLevel warn` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Per-module and per-directory configuration is available in Apache HTTP Server 2.3.6 and later | 

`LogLevel` adjusts the verbosity of the
    messages recorded in the error logs (see [ErrorLog](https://httpd.apache.org#errorlog)`level`s are available, in order of decreasing
    significance:

| **Level** | **Description** | **Example** | 
|---|---|---|
| `emerg` | Emergencies - system is unusable. | "Child cannot open lock file. Exiting" | 
| `alert` | Action must be taken immediately. | "getpwuid: couldn't determine user name from uid" | 
| `crit` | Critical Conditions. | "socket: Failed to get a socket, exiting child" | 
| `error` | Error conditions. | "Premature end of script headers" | 
| `warn` | Warning conditions. | "child process 1234 did not exit, sending another SIGHUP" | 
| `notice` | Normal but significant condition. | "httpd: caught SIGBUS, attempting to dump core in ..." | 
| `info` | Informational. | "Server seems busy, (you may need to increase StartServers, or Min/MaxSpareServers)..." | 
| `debug` | Debug-level messages | "Opening config file ..." | 
| `trace1` | Trace messages | "proxy: FTP: control connection complete" | 
| `trace2` | Trace messages | "proxy: CONNECT: sending the CONNECT request to the remote proxy" | 
| `trace3` | Trace messages | "openssl: Handshake: start" | 
| `trace4` | Trace messages | "read from buffered SSL brigade, mode 0, 17 bytes" | 
| `trace5` | Trace messages | "map lookup FAILED: map=rewritemap key=keyname" | 
| `trace6` | Trace messages | "cache lookup FAILED, forcing new map lookup" | 
| `trace7` | Trace messages, dumping large amounts of data | "\| 0000: 02 23 44 30 13 40 ac 34 df 3d bf 9a 19 49 39 15 \|" | 
| `trace8` | Trace messages, dumping large amounts of data | "\| 0000: 02 23 44 30 13 40 ac 34 df 3d bf 9a 19 49 39 15 \|" | 

When a particular level is specified, messages from all
    other levels of higher significance will be reported as well.
    *E.g.*, when `LogLevel info` is specified,
    then messages with log levels of `notice` and
    `warn` will also be posted.

Using a level of at least `crit` is
    recommended.

LogLevel notice

When logging to a regular file, messages of the level
      `notice` cannot be suppressed and thus are always
      logged. However, this doesn't apply when logging is done
      using `syslog`.

Specifying a level without a module name will reset the level
    for all modules to that level.  Specifying a level with a module
    name will set the level for that module only. It is possible to
    use the module source file name, the module identifier, or the
    module identifier with the trailing `_module` omitted
    as module specification. This means the following three specifications
    are equivalent:

LogLevel info ssl:warn
LogLevel info mod\_ssl.c:warn
LogLevel info ssl\_module:warn

It is also possible to change the level per directory:

LogLevel info
\<Directory "/usr/local/apache/htdocs/app">
  LogLevel debug
\</Directory>

Per directory loglevel configuration only affects messages that are
        logged after the request has been parsed and that are associated with
        the request. Log messages which are associated with the connection or
        the server are not affected.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Number of requests allowed on a persistent connection | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MaxKeepAliveRequests` `number` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MaxKeepAliveRequests 100` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `MaxKeepAliveRequests` directive
    limits the number of requests allowed per connection when
    [KeepAlive](https://httpd.apache.org#keepalive)`0`, unlimited requests will be allowed. We
    recommend that this setting be kept to a high value for maximum
    server performance.

MaxKeepAliveRequests 500

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Number of overlapping ranges (eg: `100-200,150-300`) allowed before returning the complete         resource | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MaxRangeOverlaps default \| unlimited \| none \|` `number-of-ranges` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MaxRangeOverlaps 20` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.3.15 and later | 

The `MaxRangeOverlaps` directive
            limits the number of overlapping HTTP ranges the server is willing to
            return to the client. If more overlapping ranges than permitted are requested,
            the complete resource is returned instead.

- **default**
- Limits the number of overlapping ranges to a compile-time default of 20.
- **none**
- No overlapping Range headers are allowed.
- **unlimited**
- The server does not limit the number of overlapping ranges it is willing to satisfy.
- `number-of-ranges`
- A positive number representing the maximum number of overlapping ranges the server is willing to satisfy.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Number of range reversals (eg: `100-200,50-70`) allowed before returning the complete         resource | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MaxRangeReversals default \| unlimited \| none \|` `number-of-ranges` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MaxRangeReversals 20` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.3.15 and later | 

The `MaxRangeReversals` directive
            limits the number of HTTP Range reversals the server is willing to
            return to the client. If more ranges reversals than permitted are requested,
            the complete resource is returned instead.

- **default**
- Limits the number of range reversals to a compile-time default of 20.
- **none**
- No Range reversals headers are allowed.
- **unlimited**
- The server does not limit the number of range reversals it is willing to satisfy.
- `number-of-ranges`
- A positive number representing the maximum number of range reversals the server is willing to satisfy.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Number of ranges allowed before returning the complete resource | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MaxRanges default \| unlimited \| none \|` `number-of-ranges` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MaxRanges 200` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.3.15 and later | 

The `MaxRanges` directive
    limits the number of HTTP ranges the server is willing to
    return to the client. If more ranges than permitted are requested,
    the complete resource is returned instead.

- **default**
- Limits the number of ranges to a compile-time default of 200.
- **none**
- Range headers are ignored.
- **unlimited**
- The server does not limit the number of ranges it is willing to satisfy.
- `number-of-ranges`
- A positive number representing the maximum number of ranges the server is willing to satisfy.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls whether the server merges consecutive slashes in URLs. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MergeSlashes ON\|OFF` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MergeSlashes ON` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Added in 2.4.39 | 

By default, the server merges (or collapses) multiple consecutive slash ('/') characters in the path component of the request URL.

When mapping URL's to the filesystem, these multiple slashes are not 
    significant.  However, URL's handled other ways, such as by CGI or proxy,
    might prefer to retain the significance of multiple consecutive slashes. 
    In these cases `MergeSlashes` can be set to 
    *OFF* to retain the multiple consecutive slashes, which is the legacy behavior.

When set to "OFF", regular expressions used in the configuration file that match
    the path component of the URL (`LocationMatch`,
    `RewriteRule`, ...) need to take into account multiple 
    consecutive slashes. Non regular expression based `Location` always
    operate against a URL with merged slashes and cannot differentiate between multiple slashes.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determines whether trailers are merged into headers | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `MergeTrailers [on\|off]` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `MergeTrailers off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.4.11 and later | 

This directive controls whether HTTP trailers are copied into the internal representation of HTTP headers. This merging occurs when the request body has been completely consumed, long after most header processing would have a chance to examine or modify request headers.

This option is provided for compatibility with releases prior to 2.4.11, where trailers were always merged.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures mutex mechanism and lock file directory for all or specified mutexes | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Mutex` `mechanism` [default\|`mutex-name`] ... [OmitPID] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Mutex default` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.3.4 and later | 

The `Mutex` directive sets the mechanism,
    and optionally the lock file location, that httpd and modules use
    to serialize access to resources.  Specify `default` as
    the second argument to change the settings for all mutexes; specify
    a mutex name (see table below) as the second argument to override
    defaults only for that mutex.

The `Mutex` directive is typically used in
    the following exceptional situations:

- change the mutex mechanism when the default mechanism selected
        by [APR](https://httpd.apache.org/glossary.html#apr) has a functional or performance
        problem
- change the directory used by file-based mutexes when the default directory does not support locking

This directive only configures mutexes which have been registered
    with the core server using the `ap_mutex_register()` API.
    All modules bundled with httpd support the `Mutex`
    directive, but third-party modules may not.  Consult the documentation
    of the third-party module, which must indicate the mutex name(s) which
    can be configured if this directive is supported.

The following mutex *mechanisms* are available:

- `default | yes` This selects the default locking implementation, as determined by
        [APR](https://httpd.apache.org/glossary.html#apr).  The default locking implementation can
        be displayed by running [httpd](https://httpd.apache.org/programs/httpd.html)`-V` option.
- `none | no` This effectively disables the mutex, and is only allowed for a mutex if the module indicates that it is a valid choice. Consult the module documentation for more information.
- `posixsem` This is a mutex variant based on a Posix semaphore. ### Warning The semaphore ownership is not recovered if a thread in the process holding the mutex segfaults, resulting in a hang of the web server.
- `sysvsem` This is a mutex variant based on a SystemV IPC semaphore. ### Warning It is possible to "leak" SysV semaphores if processes crash before the semaphore is removed. ### Security The semaphore API allows for a denial of service attack by any
        CGIs running under the same uid as the webserver (*i.e.*,
        all CGIs, unless you use something like [suexec](https://httpd.apache.org/programs/suexec.html)`cgiwrapper`).
- `sem` This selects the "best" available semaphore implementation, choosing between Posix and SystemV IPC semaphores, in that order.
- `pthread` This is a mutex variant based on cross-process Posix thread mutexes. ### Warning On most systems, if a child process terminates abnormally while holding a mutex that uses this implementation, the server will deadlock and stop responding to requests. When this occurs, the server will require a manual restart to recover. Solaris and Linux are notable exceptions as they provide a mechanism which usually allows the mutex to be recovered after a child process terminates abnormally while holding a mutex. If your system is POSIX compliant or if it implements the
        `pthread_mutexattr_setrobust_np()` function, you may be able
        to use the `pthread` option safely.
- `fcntl:/path/to/mutex` This is a mutex variant where a physical (lock-)file and the
        `fcntl()` function are used as the mutex.
### Warning When multiple mutexes based on this mechanism are used within
        multi-threaded, multi-process environments, deadlock errors (EDEADLK)
        can be reported for valid mutex operations if `fcntl()` is not thread-aware, such as on Solaris.
- `flock:/path/to/mutex` This is similar to the `fcntl:/path/to/mutex` method
        with the exception that the `flock()` function is used to
        provide file locking.
- `file:/path/to/mutex` This selects the "best" available file locking implementation,
        choosing between `fcntl` and `flock`, in that
        order.

Most mechanisms are only available on selected platforms, where the
    underlying platform and [APR](https://httpd.apache.org/glossary.html#apr) support it.  Mechanisms
    which aren't available on all platforms are *posixsem*,
    *sysvsem*, *sem*, *pthread*, *fcntl*,
    *flock*, and *file*.

With the file-based mechanisms *fcntl* and *flock*,
    the path, if provided, is a directory where the lock file will be created.
    The default directory is httpd's run-time file directory relative to
    [ServerRoot](https://httpd.apache.org#serverroot)`/path/to/mutex` and never a directory residing
    on a NFS- or AFS-filesystem.  The basename of the file will be the mutex
    type, an optional instance string provided by the module, and unless the
    `OmitPID` keyword is specified, the process id of the httpd
    parent process will be appended to make the file name unique, avoiding
    conflicts when multiple httpd instances share a lock file directory.  For
    example, if the mutex name is `mpm-accept` and the lock file
    directory is `/var/httpd/locks`, the lock file name for the
    httpd instance with parent process id 12345 would be
    `/var/httpd/locks/mpm-accept.12345`.

It is best to *avoid* putting mutex files in a world-writable
    directory such as `/var/tmp` because someone could create
    a denial of service attack and prevent the server from starting by
    creating a lockfile with the same name as the one the server will try
    to create.

The following table documents the names of mutexes used by httpd and bundled modules.

| Mutex name | Module(s) | Protected resource | 
|---|---|---|
| `mpm-accept` | [prefork](https://httpd.apache.org/mod/prefork.html) and [worker](https://httpd.apache.org/mod/worker.html) MPMs | incoming connections, to avoid the thundering herd problem;             for more information, refer to the [performance tuning](https://httpd.apache.org/misc/perf-tuning.html) documentation | 
| `authdigest-client` | [mod_auth_digest](https://httpd.apache.org/mod/mod_auth_digest.html) | client list in shared memory | 
| `authdigest-opaque` | [mod_auth_digest](https://httpd.apache.org/mod/mod_auth_digest.html) | counter in shared memory | 
| `ldap-cache` | [mod_ldap](https://httpd.apache.org/mod/mod_ldap.html) | LDAP result cache | 
| `rewrite-map` | [mod_rewrite](https://httpd.apache.org/mod/mod_rewrite.html) | communication with external mapping programs, to avoid intermixed I/O from multiple requests | 
| `ssl-cache` | [mod_ssl](https://httpd.apache.org/mod/mod_ssl.html) | SSL session cache | 
| `ssl-stapling` | [mod_ssl](https://httpd.apache.org/mod/mod_ssl.html) | OCSP stapling response cache | 
| `watchdog-callback` | [mod_watchdog](https://httpd.apache.org/mod/mod_watchdog.html) | callback function of a particular client module | 

The `OmitPID` keyword suppresses the addition of the httpd
    parent process id from the lock file name.

In the following example, the mutex mechanism for the MPM accept
    mutex will be changed from the compiled-in default to `fcntl`,
    with the associated lock file created in directory
    `/var/httpd/locks`.  The mutex mechanism for all other mutexes
    will be changed from the compiled-in default to `sysvsem`.

Mutex sysvsem default
Mutex fcntl:/var/httpd/locks mpm-accept

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | DEPRECATED: Designates an IP address for name-virtual hosting | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `NameVirtualHost` `addr`[:`port`] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Prior to 2.3.11, `NameVirtualHost` was required
to instruct the server that a particular IP address and port combination
was usable as a name-based virtual host.  In 2.3.11 and later,
any time an IP address and port combination is used in multiple virtual
hosts, name-based virtual hosting is automatically enabled for that address.

This directive currently has no effect.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures what features are available in a particular directory | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | ``` Options     [+\|-] ``` `option` [[+\|-]`option`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Options FollowSymlinks` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | Options | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | The default was changed from All to FollowSymlinks in 2.3.11 | 

The `Options` directive controls which
    server features are available in a particular directory.

`option` can be set to `None`, in which
    case none of the extra features are enabled, or one or more of
    the following:

- `All`
- All options except for `MultiViews`.
- `ExecCGI`
- 
      Execution of CGI scripts using [mod_cgi](https://httpd.apache.org/mod/mod_cgi.html)
- `FollowSymLinks`
- 
      The server will follow symbolic links in this directory. This is
      the default setting.
      When the server follows the symlink it does *not* change the pathname used to match against [\<Directory>](https://httpd.apache.org#directory)
Disabling this option also prevents
      [mod\_rewrite](https://httpd.apache.org/mod/mod_rewrite.html)`.htaccess` files and [\<Directory>](https://httpd.apache.org#directory)
The `FollowSymLinks` and `SymLinksIfOwnerMatch` `Options` work only in [\<Directory>](https://httpd.apache.org#directory)`.htaccess` files.
Omitting this option should not be considered a security restriction, since symlink testing is subject to race conditions that make it circumventable.
- `Includes`
- 
      Server-side includes provided by [mod_include](https://httpd.apache.org/mod/mod_include.html)
- `IncludesNOEXEC`
- 
      Server-side includes are permitted, but the ```
#exec
      cmd
```
and `#exec cgi` are disabled. It is still
      possible to `#include virtual` CGI scripts from [ScriptAlias](https://httpd.apache.org/mod/mod_alias.html#scriptalias)
- `Indexes`
- 
      If a URL which maps to a directory is requested and there
      is no [DirectoryIndex](https://httpd.apache.org/mod/mod_dir.html#directoryindex)
*e.g.*, `index.html`) in that directory, then [mod_autoindex](https://httpd.apache.org/mod/mod_autoindex.html)
- `MultiViews`
- [Content negotiated](https://httpd.apache.org/content-negotiation.html) "MultiViews" are allowed using [mod_negotiation](https://httpd.apache.org/mod/mod_negotiation.html)
### Note This option gets ignored if set
      anywhere other than [\<Directory>](https://httpd.apache.org#directory)[mod\_negotiation](https://httpd.apache.org/mod/mod_negotiation.html)
- `SymLinksIfOwnerMatch`
- The server will only follow symbolic links for which the
      target file or directory is owned by the same user id as the
      link.
      ### Note The `FollowSymLinks` and `SymLinksIfOwnerMatch` `Options` work only in [\<Directory>](https://httpd.apache.org#directory)`.htaccess` files.
This option should not be considered a security restriction, since symlink testing is subject to race conditions that make it circumventable.

Normally, if multiple `Options` could
    apply to a directory, then the most specific one is used and
    others are ignored; the options are not merged. (See [how sections are merged](https://httpd.apache.org/sections.html#merging).)
    However if *all* the options on the
    `Options` directive are preceded by a
    `+` or `-` symbol, the options are
    merged. Any options preceded by a `+` are added to the
    options currently in force, and any options preceded by a
    `-` are removed from the options currently in
    force.

Mixing `Options` with a `+` or
    `-` with those without is not valid syntax and will be
    rejected during server startup by the syntax check with an abort.

For example, without any `+` and `-` symbols:

\<Directory "/web/docs">
  Options Indexes FollowSymLinks
\</Directory>
\<Directory "/web/docs/spec">
  Options Includes
\</Directory>

then only `Includes` will be set for the
    `/web/docs/spec` directory. However if the second
    `Options` directive uses the `+` and
    `-` symbols:

\<Directory "/web/docs">
  Options Indexes FollowSymLinks
\</Directory>
\<Directory "/web/docs/spec">
  Options +Includes -Indexes
\</Directory>

then the options `FollowSymLinks` and
    `Includes` are set for the `/web/docs/spec`
    directory.

Using `-IncludesNOEXEC` or
      `-Includes` disables server-side includes completely
      regardless of the previous setting.

The default in the absence of any other settings is
    `FollowSymlinks`.

When using the `All` and `None`, they must
    be the first option listed. The + and - modifiers cannot be used with
    the `All` and `None` options.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Protocol for a listening socket | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Protocol` `protocol` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache 2.1.5 and later. On Windows, from Apache 2.3.3 and later. | 

This directive specifies the protocol used for a specific listening socket.
       The protocol is used to determine which module should handle a request and
       to apply protocol specific optimizations with the `AcceptFilter`
       directive.

This directive not required for most
       configurations. If not specified, `https` is the default for
       port 443 and `http` the default for all other ports.  The
       protocol is used to determine which module should handle a request, and
       to apply protocol specific optimizations with the
       [AcceptFilter](https://httpd.apache.org#acceptfilter)

For example, if you are running `https` on a non-standard port,
       specify the protocol explicitly:

Protocol https

You can also specify the protocol using the [Listen](https://httpd.apache.org/mod/mpm_common.html#listen)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Protocols available for a server/virtual host | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `Protocols` `protocol` ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Protocols http/1.1` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Only available from Apache 2.4.17 and later. | 

This directive specifies the list of protocols supported for a server/virtual host. The list determines the allowed protocols a client may negotiate for this server/host.

You need to set protocols if you want to extend the available protocols for a server/host. By default, only the http/1.1 protocol (which includes the compatibility with 1.0 and 0.9 clients) is allowed.

For example, if you want to support HTTP/2 for a server with TLS, specify:

Protocols h2 http/1.1

Valid protocols are `http/1.1` for http and https connections,
            `h2` on https connections and `h2c` for http
            connections. Modules may enable more protocols.

It is safe to specify protocols that are unavailable/disabled. Such protocol names will simply be ignored.

The `http/1.1` protocol is always available and
            cannot be excluded by omitting it from this directive.
            This directive controls which additional protocols are
            available for negotiation, and, when used with
            `ProtocolsHonorOrder`, their preference
            order.

Protocols specified in base servers are inherited for virtual hosts only if the virtual host has no own Protocols directive. Or, the other way around, Protocols directives in virtual hosts replace any such directive in the base server.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determines if order of Protocols determines precedence during negotiation | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ProtocolsHonorOrder On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ProtocolsHonorOrder On` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Only available from Apache 2.4.17 and later. | 

This directive specifies if the server should honor the order in which
        the `Protocols` directive lists protocols.

If configured Off, the client supplied list order of protocols has precedence over the order in the server configuration.

With `ProtocolsHonorOrder` set to `on` 
            (default), the client ordering does not matter and only the ordering 
            in the server settings influences the outcome of the protocol 
            negotiation.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls whether the REDIRECT\_URL environment variable is fully qualified | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `QualifyRedirectURL On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `QualifyRedirectURL Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Directive supported in 2.4.18 and later. 2.4.17 acted as if 'QualifyRedirectURL On' was configured. | 

This directive controls whether the server will ensure that the 
    REDIRECT\_URL environment variable is fully qualified.  By default, 
    the variable contains the verbatim URL requested by the client, 
    such as "/index.html".  With `QualifyRedirectURL On`, the same request would result in a
    value such as "http://www.example.com/index.html".

Even without this directive set, when a request is issued against a fully qualified URL, REDIRECT\_URL will remain fully qualified.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Size of the buffers used to read data | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ReadBufferSize` `bytes` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ReadBufferSize 8192` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | 2.4.27 and later | 

This directive allows to configure the size (in bytes) of the memory buffer used to read data from the network or files.

A larger buffer can increase performances with larger data, but consumes
    more memory per connection. The minimum configurable size is
    `1024`.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Allow to configure global/default options for regexes | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `RegexDefaultOptions [none] [+\|-]``option` [[+\|-]`option`] ... | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `RegexDefaultOptions DOTALL DOLLAR_ENDONLY` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Only available from Apache 2.4.30 and later. | 

This directive adds some default behavior to ANY regular expression used afterwards.

Any option preceded by a '+' is added to the already set options.

Any option preceded by a '-' is removed from the already set options.

Any option without a '+' or a '-' will be set, removing any other
        already set option.

The `none` keyword resets any already set options.

`option` can be:

- `ICASE`
- Use a case-insensitive match.
- `EXTENDED`
- Perl's /x flag, ignore (unescaped-)spaces and comments in the pattern.
- `DOTALL`
- Perl's /s flag, '.' matches newline characters.
- `DOLLAR_ENDONLY`
- '$' matches at end of subject string only.

\# Add the ICASE option for all regexes by default
RegexDefaultOptions +ICASE
...
# Remove the default DOLLAR\_ENDONLY option, but keep any other one
RegexDefaultOptions -DOLLAR\_ENDONLY
...
# Set the DOTALL option only, resetting any other one
RegexDefaultOptions DOTALL
...
# Reset all defined options
RegexDefaultOptions none
...

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Register non-standard HTTP methods | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `RegisterHttpMethod` `method` [`method` [...]] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache HTTP Server 2.4.24 and later | 

This directive may be used to register additional HTTP methods. This is necessary if non-standard methods need to be used with directives that accept method names as parameters, or to allow particular non-standard methods to be used via proxy or CGI script when the server has been configured to only pass recognized methods to modules.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the CPU consumption of processes launched by Apache httpd children | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `RLimitCPU` `seconds`\|max [`seconds`\|max] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Unset; uses operating system defaults` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Takes 1 or 2 parameters. The first parameter sets the soft
    resource limit for all processes and the second parameter sets
    the maximum resource limit. Either parameter can be a number,
    or `max` to indicate to the server that the limit should
    be set to the maximum allowed by the operating system
    configuration. Raising the maximum resource limit requires that
    the server is running as `root` or in the initial startup
    phase.

This applies to processes forked from Apache httpd children servicing requests, not the Apache httpd children themselves. This includes CGI scripts and SSI exec commands, but not any processes forked from the Apache httpd parent, such as piped logs.

CPU resource limits are expressed in seconds per process.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the memory consumption of processes launched by Apache httpd children | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `RLimitMEM` `bytes`\|max [`bytes`\|max] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Unset; uses operating system defaults` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Memory resource limits are expressed in bytes per process.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Limits the number of processes that can be launched by processes launched by Apache httpd children | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `RLimitNPROC` `number`\|max [`number`\|max] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `Unset; uses operating system defaults` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Takes 1 or 2 parameters. The first parameter sets the soft
    resource limit for all processes, and the second parameter sets
    the maximum resource limit. Either parameter can be a number,
    or `max` to indicate to the server that the limit
    should be set to the maximum allowed by the operating system
    configuration. Raising the maximum resource limit requires that
    the server is running as `root` or in the initial startup
    phase.

Process limits control the number of processes per user.

If CGI processes are **not** running
      under user ids other than the web server user id, this directive
      will limit the number of processes that the server itself can
      create. Evidence of this situation will be indicated by
      **`cannot fork`** messages in the
      `error_log`.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Technique for locating the interpreter for CGI scripts | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ScriptInterpreterSource Registry\|Registry-Strict\|Script` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ScriptInterpreterSource Script` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Win32 only. | 

This directive is used to control how Apache httpd finds the
    interpreter used to run CGI scripts. The default setting is
    `Script`. This causes Apache httpd to use the interpreter pointed to
    by the shebang line (first line, starting with `#!`) in the
    script. On Win32 systems this line usually looks like:

#!C:/Perl/bin/perl.exe

or, if `perl` is in the `PATH`, simply:

#!perl

Setting `ScriptInterpreterSource Registry` will
    cause the Windows Registry tree `HKEY_CLASSES_ROOT` to be
    searched using the script file extension (e.g., `.pl`) as a
    search key. The command defined by the registry subkey
    `Shell\ExecCGI\Command` or, if it does not exist, by the subkey
    `Shell\Open\Command` is used to open the script file. If the
    registry keys cannot be found, Apache httpd falls back to the behavior of the
    `Script` option.

Be careful when using ```
ScriptInterpreterSource
    Registry
```
 with [ScriptAlias](https://httpd.apache.org/mod/mod_alias.html#scriptalias)**every** file within this
    directory. The `Registry` setting may cause undesired
    program calls on files which are typically not executed. For
    example, the default open command on `.htm` files on
    most Windows systems will execute Microsoft Internet Explorer, so
    any HTTP request for an `.htm` file existing within the
    script directory would start the browser in the background on the
    server. This is a good way to crash your system within a minute or
    so.

The option `Registry-Strict`
    does the same thing as `Registry` but uses only the
    subkey `Shell\ExecCGI\Command`. The
    `ExecCGI` key is not a common one. It must be
    configured manually in the windows registry and hence prevents
    accidental program calls on your system.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determine if mod\_status displays the first 63 characters of a request or the last 63, assuming the request itself is greater than 63 chars. | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `SeeRequestTail On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `SeeRequestTail Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Available in Apache httpd 2.2.7 and later. | 

[mod\_status](https://httpd.apache.org/mod/mod_status.html)`ExtendedStatus On`
    displays the actual request being handled.
    For historical purposes, only 63 characters of the request
    are actually stored for display purposes. This directive
    controls whether the first 63 characters are stored (the previous
    behavior and the default) or if the last 63 characters are. This
    is only applicable, of course, if the length of the request is
    64 characters or greater.

If Apache httpd is handling `GET /disk1/storage/apache/htdocs/images/imagestore1/food/apples.jpg HTTP/1.1` [mod\_status](https://httpd.apache.org/mod/mod_status.html)

| Off (default) | GET /disk1/storage/apache/htdocs/images/imagestore1/food/apples | 
|---|---|
| On | orage/apache/htdocs/images/imagestore1/food/apples.jpg HTTP/1.1 | 

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Email address that the server includes in error messages sent to the client | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerAdmin` `email-address`\|`URL` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerAdmin` sets the contact address
    that the server includes in any error messages it returns to the
    client. If the `httpd` doesn't recognize the supplied argument
    as an URL, it
    assumes, that it's an `email-address` and prepends it with
    `mailto:` in hyperlink targets. However, it's recommended to
    actually use an email address, since there are a lot of CGI scripts that
    make that assumption. If you want to use an URL, it should point to another
    server under your control. Otherwise users may not be able to contact you in
    case of errors.

It may be worth setting up a dedicated address for this, e.g.

ServerAdmin www-admin@foo.example.com

as users do not always mention that they are talking about the server!

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Alternate names for a host used when matching requests to name-virtual hosts | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerAlias` `hostname` [`hostname`] ... | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerAlias` directive sets the
    alternate names for a host, for use with [name-based virtual hosts](https://httpd.apache.org/vhosts/name-based.html). The
    `ServerAlias` may include wildcards, if appropriate.

\<VirtualHost \*:80>
  ServerName server.example.com
  ServerAlias server server2.example.com server2
  ServerAlias \*.example.com
  UseCanonicalName Off
  # ...
\</VirtualHost>

Name-based virtual hosts for the best-matching set of  [\<virtualhost>](https://httpd.apache.org#virtualhost)[ServerName](https://httpd.apache.org#servername)`ServerAlias` is used, with no different precedence for wildcards
    (nor for ServerName vs. ServerAlias).

The complete list of names in the [\<VirtualHost>](https://httpd.apache.org#virtualhost)`ServerAlias`.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Hostname and port that the server uses to identify itself | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerName [``scheme`://]`domain-name`\|`ip-address`[:`port`] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerName` directive sets the
    request scheme, hostname and port that the server uses to identify itself.

`ServerName` is used (possibly
    in conjunction with [ServerAlias](https://httpd.apache.org#serveralias)[name-based virtual hosts](https://httpd.apache.org/vhosts/name-based.html).

Additionally, this is used when
    creating self-referential redirection URLs when
    [UseCanonicalName](https://httpd.apache.org#usecanonicalname)`On`. When `UseCanonicalName` is set to
    `DNS`, a reverse DNS lookup is used instead.

For example, if the name of the
    machine hosting the web server is `simple.example.com`,
    but the machine also has the DNS alias `www.example.com`
    and you wish the web server to be so identified, the following
    directive should be used:

ServerName www.example.com

The `ServerName` directive
    may appear anywhere within the definition of a server. However,
    each appearance overrides the previous appearance (within that
    server).

If no `ServerName` is specified, the
    server attempts to deduce the client visible hostname by first asking 
    the operating system for the system hostname, and if that fails, 
    performing a reverse lookup on an IP address present on the system.

If no port is specified in the
    `ServerName`, then the server will use the
    port from the incoming request. For optimal reliability and
    predictability, you should specify an explicit hostname and port
    using the `ServerName` directive.

If you are using [name-based virtual hosts](https://httpd.apache.org/vhosts/name-based.html),
    the `ServerName` inside a
    [\<VirtualHost>](https://httpd.apache.org#virtualhost)`Host:` header to match this virtual host.

Sometimes, the server runs behind a device that processes SSL,
    such as a reverse proxy, load balancer or SSL offload
    appliance. When this is the case, specify the
    `https://` scheme and the port number to which the
    clients connect in the `ServerName` directive
    to make sure that the server generates the correct
    self-referential URLs.

See the description of the
    [UseCanonicalName](https://httpd.apache.org#usecanonicalname)[UseCanonicalPhysicalPort](https://httpd.apache.org#usecanonicalphysicalport)[mod\_dir](https://httpd.apache.org/mod/mod_dir.html)

Failure to set `ServerName` to a name that
    your server can resolve to an IP address will result in a startup
    warning. `httpd` will then use whatever hostname it can
    determine, using the system's `hostname` command. This
    will almost never be the hostname you actually want.

```
    httpd: Could not reliably determine the server's fully qualified domain name, using rocinante.local for ServerName
    
```

IPv6 addresses in `ServerName` are not
        currently supported and will produce a startup error, even when
        enclosed in square brackets. This is a
        [known issue](https://bz.apache.org/bugzilla/show_bug.cgi?id=52178).

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Legacy URL pathname for a name-based virtual host that is accessed by an incompatible browser | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerPath` `URL-path` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerPath` directive sets the legacy
    URL pathname for a host, for use with [name-based virtual hosts](https://httpd.apache.org/vhosts/name-based.html).

This is a legacy feature for providing compatibility with
    HTTP/1.0 clients that do not send a `Host:` header. When
    such a client requests a URL matching a vhost's
    `ServerPath`, the request is served from that
    vhost. In practice, all modern HTTP clients send the
    `Host:` header, making this directive unnecessary.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Base directory for the server installation | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerRoot` `directory-path` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ServerRoot /usr/local/apache` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerRoot` directive sets the
    directory in which the server lives. Typically it will contain the
    subdirectories `conf/` and `logs/`. Relative
    paths in other configuration directives (such as [Include](https://httpd.apache.org#include)[LoadModule](https://httpd.apache.org/mod/mod_so.html#loadmodule)

ServerRoot "/home/httpd"

The default location of `ServerRoot` may be
    modified by using the `--prefix` argument to
    [`configure`](https://httpd.apache.org/programs/configure.html), and
    most third-party distributions of the server have a different
    default location from the one listed above.

- [the `-d`
    option to `httpd`](https://httpd.apache.org/invoking.html)
- [the
    security tips](https://httpd.apache.org/misc/security_tips.html#serverroot) for information on how to properly set
    permissions on the `ServerRoot`

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures the footer on server-generated documents | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerSignature On\|Off\|EMail` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ServerSignature Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | All | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `ServerSignature` directive allows the
    configuration of a trailing footer line under server-generated
    documents (error messages, [mod\_proxy](https://httpd.apache.org/mod/mod_proxy.html)[mod\_info](https://httpd.apache.org/mod/mod_info.html)

The `Off`
    setting, which is the default, suppresses the footer line.
    The `On` setting simply adds a line with the
    server version number and [ServerName](https://httpd.apache.org#servername)`EMail` setting additionally creates a
    "mailto:" reference to the [ServerAdmin](https://httpd.apache.org#serveradmin)

The details of the server version number
    presented are controlled by the [ServerTokens](https://httpd.apache.org#servertokens)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures the `Server` HTTP response header | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `ServerTokens Major\|Minor\|Min[imal]\|Prod[uctOnly]\|OS\|Full` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `ServerTokens Full` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive controls whether `Server` response
    header field which is sent back to clients includes a
    description of the generic OS-type of the server as well as
    information about compiled-in modules.

- `ServerTokens Full` (or not specified)
- Server sends (*e.g.*): ```
Server: Apache/2.4.2
      (Unix) PHP/4.2.2 MyMod/1.2
```
- `ServerTokens Prod[uctOnly]`
- Server sends (*e.g.*): ```
Server:
      Apache
```
- `ServerTokens Major`
- Server sends (*e.g.*): ```
Server:
      Apache/2
```
- `ServerTokens Minor`
- Server sends (*e.g.*): ```
Server:
      Apache/2.4
```
- `ServerTokens Min[imal]`
- Server sends (*e.g.*): ```
Server:
      Apache/2.4.2
```
- `ServerTokens OS`
- Server sends (*e.g.*): ```
Server: Apache/2.4.2
      (Unix)
```

This setting applies to the entire server, and cannot be enabled or disabled on a virtualhost-by-virtualhost basis.

This directive also controls the
    information presented by the [ServerSignature](https://httpd.apache.org#serversignature)

Setting `ServerTokens` to less than
    `minimal` is not recommended because it makes it more
    difficult to debug interoperational problems. Also note that
    disabling the Server: header does nothing at all to make your
    server more secure. The idea of "security through obscurity"
    is a myth and leads to a false sense of safety.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Forces all matching files to be processed by a handler | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `SetHandler` `handler-name`\|none\|`expression` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | expression argument 2.4.19 and later | 

When placed into an `.htaccess` file or a
    [\<Directory>](https://httpd.apache.org#directory)[\<Location>](https://httpd.apache.org#location)[handler](https://httpd.apache.org/handler.html) given by
    `handler-name`. For example, if you had a directory you
    wanted to be parsed entirely as imagemap rule files, regardless
    of extension, you might put the following into an
    `.htaccess` file in that directory:

SetHandler imap-file

Another example: if you wanted to have the server display a
    status report whenever a URL of
    `http://servername/status` was called, you might put
    the following into `httpd.conf`:

\<Location "/status">
  SetHandler server-status
\</Location>

You could also use this directive to configure a particular handler for files with a particular file extension. For example:

```
<FilesMatch "\.php$">
    SetHandler application/x-httpd-php
</FilesMatch>
```
    String-valued expressions can be used to reference per-request variables, including backreferences to named regular expressions:

```
<LocationMatch ^/app/(?<sub>[^/]+)/>
     SetHandler "proxy:unix:/var/run/app_%{env:MATCH_sub}.sock|fcgi://localhost:8080"
</LocationMatch>
```
    You can override an earlier defined `SetHandler`
    directive by using the value `None`.

Because `SetHandler` overrides default handlers,
    normal behavior such as handling of URLs ending in a slash (/) as
    directories or index files is suppressed. It also overrides
    [FallbackResource](https://httpd.apache.org/mod/mod_dir.html#fallbackresource)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Sets the filters that will process client requests and POST input | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `SetInputFilter` `filter`[;`filter`...] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `SetInputFilter` directive sets the
    filter or filters which will process client requests and POST
    input when they are received by the server. This is in addition to
    any filters defined elsewhere, including the
    [AddInputFilter](https://httpd.apache.org/mod/mod_mime.html#addinputfilter)

If more than one filter is specified, they must be separated by semicolons in the order in which they should process the content.

- [Filters](https://httpd.apache.org/filter.html) documentation

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Sets the filters that will process responses from the server | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `SetOutputFilter` `filter`[;`filter`...] | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory, .htaccess | 
| [Override:](https://httpd.apache.org/directive-dict.html#Override) | FileInfo | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `SetOutputFilter` directive sets the filters
    which will process responses from the server before they are
    sent to the client. This is in addition to any filters defined
    elsewhere, including the
    [AddOutputFilter](https://httpd.apache.org/mod/mod_mime.html#addoutputfilter)

For example, the following configuration will process all files
    in the `/www/data/` directory for server-side
    includes.

\<Directory "/www/data/">
  SetOutputFilter INCLUDES
\</Directory>

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls whether the server requires the requested hostname be listed enumerated in the virtual host handling the request | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `StrictHostCheck ON\|OFF` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `StrictHostCheck OFF` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Added in 2.4.49 | 

By default, the server will respond to requests for any hostname, including requests addressed to unexpected or unconfigured hostnames. While this is convenient, it is sometimes desirable to limit what hostnames a backend application handles since it will often generate self-referential responses.

By setting `StrictHostCheck` to *ON*,
    the server will return an HTTP 400 error if the requested hostname
    hasn't been explicitly listed by either [ServerName](https://httpd.apache.org#servername)[ServerAlias](https://httpd.apache.org#serveralias)

This directive also allows matching of the requested hostname to hostnames
   specified within the opening [VirtualHost](https://httpd.apache.org#virtualhost)[ServerAlias](https://httpd.apache.org#serveralias)

This directive has no affect in non-default virtual hosts. The value inherited from the global server configuration, or the default virtualhost for the ip:port the underlying connection, determine the effective value.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Amount of time the server will wait for certain events before failing a request | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `TimeOut` `seconds` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `TimeOut 60` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

The `TimeOut` directive defines the length
    of time Apache httpd will wait for I/O in various circumstances:

- When reading data from the client, the length of time to wait for a TCP packet to arrive if the read buffer is empty. For initial data on a new connection, this directive doesn't
      take effect until after any configured 
      [AcceptFilter](https://httpd.apache.org#acceptfilter)
- When writing data to the client, the length of time to wait for an acknowledgment of a packet if the send buffer is full.
- In [mod_cgi](https://httpd.apache.org/mod/mod_cgi.html)
[mod_cgid](https://httpd.apache.org/mod/mod_cgid.html)
- In [mod_ext_filter](https://httpd.apache.org/mod/mod_ext_filter.html)
- In [mod_proxy](https://httpd.apache.org/mod/mod_proxy.html)
[ProxyTimeout](https://httpd.apache.org/mod/mod_proxy.html#proxytimeout)

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Determines the behavior on `TRACE` requests | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `TraceEnable` `[on\|off\|extended]` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `TraceEnable on` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

This directive overrides the behavior of `TRACE` for both
    the core server and [mod\_proxy](https://httpd.apache.org/mod/mod_proxy.html)`TraceEnable on` permits `TRACE` requests per
    RFC 2616, which disallows any request body to accompany the request.
    `TraceEnable off` causes the core server and
    [mod\_proxy](https://httpd.apache.org/mod/mod_proxy.html)`405` (Method not
    allowed) error to the client.

Finally, for testing and diagnostic purposes only, request
    bodies may be allowed using the non-compliant ```
TraceEnable
    extended
```
 directive.  The core (as an origin server) will
    restrict the request body to 64Kb (plus 8Kb for chunk headers if
    `Transfer-Encoding: chunked` is used).  The core will
    reflect the full headers and all chunk headers with the response
    body.  As a proxy server, the request body is not restricted to 64Kb.

The `TRACE` method cannot be restricted using
    [\<Limit>](https://httpd.apache.org#limit)[\<LimitExcept>](https://httpd.apache.org#limitexcept)`TraceEnable` instead.

Despite claims to the contrary, enabling the `TRACE`
    method does not expose any security vulnerability in Apache httpd.
    The `TRACE` method is defined by the HTTP/1.1
    specification and implementations are expected to support it.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Controls what UNC host names can be accessed by the server | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `UNCList` `hostname` [`hostname`...] | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `unset` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 
| [Compatibility:](https://httpd.apache.org/directive-dict.html#Compatibility) | Added in 2.4.60, Windows only. | 

During request processing, requests to access a filesystem path that resolves to a UNC path will fail unless the hostname in the UNC path has been specified by this directive. The intent is to limit access to paths derived from untrusted inputs.

UNCList example.com other.example.com

The values specified by this directive are only checked by some components of the server, prior to accessing filesystem paths that may be inadvertently derived from untrusted inputs.

Windows systems should be isolated at the network layer from making outbound SMB/NTLM calls to unexpected destinations as a more comprehensive and preemptive measure.

This directive should be placed before UNC paths used in httpd.conf. Multiple occurrences of the directive reset the list.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Undefine the existence of a variable | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `UnDefine` `parameter-name` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

Undoes the effect of a [Define](https://httpd.apache.org#define)`-D` argument to [httpd](https://httpd.apache.org/programs/httpd.html)

This directive can be used to toggle the use of [\<IfDefine>](https://httpd.apache.org#ifdefine)`-D` arguments in any startup scripts.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures how the server determines its own name and port | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `UseCanonicalName On\|Off\|DNS` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `UseCanonicalName Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

In many situations Apache httpd must construct a *self-referential*
    URL -- that is, a URL that refers back to the same server. With
    `UseCanonicalName On` Apache httpd will use the hostname and port
    specified in the [ServerName](https://httpd.apache.org#servername)`SERVER_NAME` and `SERVER_PORT` in CGIs.

With `UseCanonicalName Off` Apache httpd will form
    self-referential URLs using the hostname and port supplied by
    the client if any are supplied (otherwise it will use the
    canonical name, as defined above). These values are the same
    that are used to implement [name-based virtual hosts](https://httpd.apache.org/vhosts/name-based.html)
    and are available with the same clients. The CGI variables
    `SERVER_NAME` and `SERVER_PORT` will be
    constructed from the client supplied values as well.

An example where this may be useful is on an intranet server
    where you have users connecting to the machine using short
    names such as `www`. You'll notice that if the users
    type a shortname and a URL which is a directory, such as
    `http://www/splat`, *without the trailing
    slash*, then Apache httpd will redirect them to
    `http://www.example.com/splat/`. If you have
    authentication enabled, this will cause the user to have to
    authenticate twice (once for `www` and once again
    for `www.example.com` -- see 
    [the FAQ on this subject for more information](https://cwiki.apache.org/confluence/display/httpd/FAQ#Why_does_Apache_ask_for_my_password_twice_before_serving_a_file.3F)). But if
    `UseCanonicalName` is set `Off`, then
    Apache httpd will redirect to `http://www/splat/`.

There is a third option, `UseCanonicalName DNS`,
    which is intended for use with mass IP-based virtual hosting to
    support ancient clients that do not provide a
    `Host:` header. With this option, Apache httpd does a
    reverse DNS lookup on the server IP address that the client
    connected to in order to work out self-referential URLs.

If CGIs make assumptions about the values of `SERVER_NAME`,
    they may be broken by this option. The client is essentially free
    to give whatever value they want as a hostname. But if the CGI is
    only using `SERVER_NAME` to construct self-referential URLs,
    then it should be just fine.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Configures how the server determines its own port | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | `UseCanonicalPhysicalPort On\|Off` | 
| [Default:](https://httpd.apache.org/directive-dict.html#Default) | `UseCanonicalPhysicalPort Off` | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config, virtual host, directory | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

In many situations Apache httpd must construct a *self-referential*
    URL -- that is, a URL that refers back to the same server. With
    `UseCanonicalPhysicalPort On`, Apache httpd will, when
    constructing the canonical port for the server to honor
    the [UseCanonicalName](https://httpd.apache.org#usecanonicalname)`UseCanonicalPhysicalPort Off`,
    Apache httpd will not ever use the actual physical port number, instead
    relying on all configured information to construct a valid port number.

The ordering of the lookup when the physical port is used is as follows:

- `UseCanonicalName On`
  1. Port provided in [Servername](https://httpd.apache.org#servername)
  2. Physical port
  3. Default port for the scheme/protocol (such as 80 or 443)
- `UseCanonicalName Off | DNS`
  1. Parsed port from `Host:` header
  2. Physical port
  3. Port provided in [Servername](https://httpd.apache.org#servername)
  4. Default port for the scheme/protocol (such as 80 or 443)

With `UseCanonicalPhysicalPort Off`, the
    physical ports are removed from the ordering.

| [Description:](https://httpd.apache.org/directive-dict.html#Description) | Contains directives that apply only to a specific hostname or IP address | 
|---|---|
| [Syntax:](https://httpd.apache.org/directive-dict.html#Syntax) | ``` <VirtualHost      ``` `addr`[:`port`] [`addr`[:`port`]]     ...> ... </VirtualHost> | 
| [Context:](https://httpd.apache.org/directive-dict.html#Context) | server config | 
| [Status:](https://httpd.apache.org/directive-dict.html#Status) | Core | 
| [Module:](https://httpd.apache.org/directive-dict.html#Module) | core | 

`<VirtualHost>` and
    `</VirtualHost>` are used to enclose a group of
    directives that will apply only to a particular virtual host. Any
    directive that is allowed in a virtual host context may be
    used. When the server receives a request for a document on a
    particular virtual host, it uses the configuration directives
    enclosed in the `<VirtualHost>`
    section. `Addr` can be any of the following, optionally followed by
    a colon and a port number (or \*):

- The IP address of the virtual host;
- A fully qualified domain name for the IP address of the virtual host (not recommended);
- The character `*`, which acts as a wildcard and matches
      any IP address.
- The string `_default_`, which is an alias for `*`

\<VirtualHost 10.1.2.3:80>
  ServerAdmin webmaster@host.example.com
  DocumentRoot "/www/docs/host.example.com"
  ServerName host.example.com
  ErrorLog "logs/host.example.com-error\_log"
  TransferLog "logs/host.example.com-access\_log"
\</VirtualHost>

IPv6 addresses must be specified in square brackets because the optional port number could not be determined otherwise. An IPv6 example is shown below:

\<VirtualHost \[2001:db8::a00:20ff:fea7:ccea\]:80>
  ServerAdmin webmaster@host.example.com
  DocumentRoot "/www/docs/host.example.com"
  ServerName host.example.com
  ErrorLog "logs/host.example.com-error\_log"
  TransferLog "logs/host.example.com-access\_log"
\</VirtualHost>

Each Virtual Host must correspond to a different IP address,
    different port number, or a different host name for the server,
    in the former case the server machine must be configured to
    accept IP packets for multiple addresses. (If the machine does
    not have multiple network interfaces, then this can be
    accomplished with the `ifconfig alias` command -- if
    your OS supports it).

The use of `<VirtualHost>` does
    **not** affect what addresses Apache httpd listens on. You
    may need to ensure that Apache httpd is listening on the correct addresses
    using [Listen](https://httpd.apache.org/mod/mpm_common.html#listen)

A [ServerName](https://httpd.apache.org#servername)`<VirtualHost>` block. If it is absent, the
    [ServerName](https://httpd.apache.org#servername)

When a request is received, the server first maps it to the best matching
    `<VirtualHost>` based on the local
    IP address and port combination only.  Non-wildcards have a higher
    precedence. If no match based on IP and port occurs at all, the
    "main" server configuration is used.

If multiple virtual hosts contain the best matching IP address and port, the server selects from these virtual hosts the best match based on the requested hostname. If no matching name-based virtual host is found, then the first listed virtual host that matched the IP address will be used. As a consequence, the first listed virtual host for a given IP address and port combination is the default virtual host for that IP and port combination.

- [Apache HTTP Server Virtual Host documentation](https://httpd.apache.org/vhosts/)
- [Issues Regarding DNS and
    Apache HTTP Server](https://httpd.apache.org/dns-caveats.html)
- [Setting
    which addresses and ports Apache HTTP Server uses](https://httpd.apache.org/bind.html)
- [How \<Directory>, \<Location>
    and \<Files> sections work](https://httpd.apache.org/sections.html) for an explanation of how these
    different sections are combined when a request is received
