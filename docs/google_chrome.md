---
tags:
  -  Applications
  -  Web Browsers
---
Google Chrome is a [web browser](web_browser.md) developed by
Google Inc.

## Configuration

The Google Chrome configuration can be found in the **Preferences**
file. From the Chromium site, 'Preferences are kept in a file named
"Preferences", which every Chromium / Google Chrome user will have in
their own user directory.' The file combines some settings from the
policies, master_preferences, and local state.

There might be a copy of the **Preferences** file called **Secure
Preferences**. The purpose of the file is so that the browser can
compare the saved profile to a "good copy" (the **Secure Preferences**
file), and if the two do not match then the browser will reset the
settings when it is restarted, as [explained
here](https://superuser.com/a/1276934)).

On Linux

    /home/$USER/.config/google-chrome/Default/Preferences
    /home/$USER/.config/google-chrome/Default/Secure Preferences

On MacOS-X

    /Users/$USER/Library/Application Support/Google/Chrome/Default/Preferences
    /Users/$USER/Library/Application Support/Google/Chrome/Default/Secure Preferences

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Google\Chrome\User Data\Default\Preferences
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Google\Chrome\User Data\Default\Secure Preferences

On Windows Vista and later

    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Preferences
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Secure Preferences

Or for **Chrome SxS** (Chrome side-by-side)

    C:\Users\%USERNAME%\AppData\Local\Google\Chrome SxS\User Data\Default\Preferences
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome SxS\User Data\Default\Secure Preferences

Or for **Chromium**

On Linux

    /home/$USER/.config/chromium/Default/Preferences
    /home/$USER/.config/chromium/Default/Secure Preferences

On MacOS-X

    /Users/$USER/Library/Application Support/Chromium/Default/Preferences
    /Users/$USER/Library/Application Support/Chromium/Default/Secure Preferences

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Chromium\User Data\Default\Preferences
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Chromium\User Data\Default\Secure Preferences

On Windows Vista and later

    C:\Users\%USERNAME%\AppData\Local\Chromium\User Data\Default\Preferences
    C:\Users\%USERNAME%\AppData\Local\Chromium\User Data\Default\Secure Preferences

In browser way to control some settings:

    chrome://extensions/
    chrome://flags
    chrome://settings

### Useful values in the Preferences file

Signed in users are stored here, along with timestamps for when they
first and last used this profile.

Under "plugins" you can find whether the plugin is enabled, the name,
the path, and the version. (If the plugin provides all those values.)

#### Installed Extensions

This file contains several useful details about the installed extensions
(under "extensions"):

- "install_time": The timestamp of when the extension was installed in
  this Chrome profile.
- "manifest": full extension manifest JSON
  - "key": the key associated with the extension (Used to determine the
    Extension ID)
- "path": the Extension/ sub-path that the code is stored in under the
  profile
- "state": The current state of the extension from this Chrome Profile's
  perspective.
  [1](https://code.google.com/p/chromium/codesearch#chromium/src/extensions/common/extension.h&l=63)
  - 0: DISABLED
  - 1: ENABLED
  - 2: EXTERNAL_EXTENSION_UNINSTALLED

#### DNS Prefetching

DNS is prefetched for related sites, e.g. links on the page. This
behavior is controlled by the setting "Predict network actions to
improve page load performance", which is enabled by default.

If enabled the Preferences file contains:

       "dns_prefetching": {
          "enabled": true,

If disabled the Preferences file contains:

       "dns_prefetching": {
          "enabled": false,

## Start-up DNS queries

When Chrome starts it queries for several non-existing hostnames that
consists of a 10 random characters, E.g.

    ttrgoiknff.mydomain.com
    bxjhgftsyu.mydomain.com
    yokjbjiagd.mydomain.com

This is used to determine if your ISP is hijacking NXDOMAIN results
[2](http://www.google.com/support/forum/p/Chrome/thread?tid=3511015c72a7b314&hl=en).

## Disk Cache

Google Chrome uses multiple caches, from
[3](http://src.chromium.org/viewvc/chrome/trunk/src/net/base/cache_type.h?view=markup):

    // The types of caches that can be created.
    enum CacheType {
        DISK_CACHE,  // Disk is used as the backing storage.
        MEMORY_CACHE,  // Data is stored only in memory.
        MEDIA_CACHE,  // Optimized to handle media files.
        APP_CACHE,  // Backing store for an AppCache.
        SHADER_CACHE, // Backing store for the GL shader cache.
        PNACL_CACHE, // Backing store the PNaCl translation cache
    };

**Note that \$PROFILE (or %PROFILE%) the paths below is the profile
dependent subdirectory which is normally Default but also could be
Profile1, Profile2, etc.**

The Google Chrome disk cache uses the [Chrome Disk Cache
Format](chrome_disk_cache_format.md) and can be found in:

On Linux

    /home/$USER/.cache/chromium/$PROFILE/Cache/
    /home/$USER/.cache/google-chrome/$PROFILE/Cache/
    /home/$USER/.config/chromium/$PROFILE/Cache/
    /home/$USER/.config/google-chrome/$PROFILE/Cache/

    /home/$USER/.cache/chromium/$PROFILE/Media Cache/
    /home/$USER/.cache/google-chrome/$PROFILE/Media Cache/
    /home/$USER/.config/chromium/$PROFILE/Media Cache/
    /home/$USER/.config/google-chrome/$PROFILE/Media Cache/

    /home/$USER/.config/chromium/$PROFILE/Application Cache/Cache/
    /home/$USER/.config/google-chrome/$PROFILE/Application Cache/Cache/

    /home/$USER/.config/chromium/$PROFILE/GPUCache/
    /home/$USER/.config/google-chrome/$PROFILE/GPUCache/

    /home/$USER/.cache/chromium/PnaclTranslationCache/
    /home/$USER/.cache/google-chrome/PnaclTranslationCache/

On MacOS-X

    /Users/$USER/Library/Caches/Chromium/$PROFILE/Cache
    /Users/$USER/Library/Caches/Google/Chrome/$PROFILE/Cache

**TODO confirm the following paths**

    /Users/$USER/Caches/Chromium/$PROFILE/Cache/
    /Users/$USER/Caches/Google/Chrome/$PROFILE/Cache/

    /Users/$USER/Library/Caches/Chromium/$PROFILE/Media Cache
    /Users/$USER/Library/Caches/Google/Chrome/$PROFILE/Media Cache

    /Users/$USER/Library/Application Support/Chromium/$PROFILE/Application Cache/Cache/
    /Users/$USER/Library/Application Support/Google/Chrome/$PROFILE/Application Cache/Cache/

    /Users/$USER/Library/Application Support/Chromium/$PROFILE/GPUCache/
    /Users/$USER/Library/Application Support/Google/Chrome/$PROFILE/GPUCache/

    /Users/$USER/Library/Caches/Chromium/PnaclTranslationCache/
    /Users/$USER/Library/Caches/Google/Chrome/PnaclTranslationCache/

On Windows XP

**TODO confirm the following paths**

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Chromium\User Data\Cache\
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Google\Chrome\User Data\Cache\

On Windows Vista and later

    C:\Users\%USERNAME%\AppData\Local\Google\Chromium\%PROFILE%\Cache\
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\%PROFILE%\Cache\

    C:\Users\%USERNAME%\AppData\Local\Google\Chromium\%PROFILE%\Application Cache\Cache\
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\%PROFILE%\Application Cache\Cache\

    C:\Users\%USERNAME%\AppData\Local\Google\Chromium\%PROFILE%\Media Cache\
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\%PROFILE%\Media Cache\

    C:\Users\%USERNAME%\AppData\Local\Google\Chromium\%PROFILE%\GPUCache\
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\%PROFILE%\GPUCache\

The Chrome Cache contains different files with the following file names:

- index
- data_#; where \# contains a decimal digit.
- f_######; where \# contains a hexadecimal digit.

## History

Chrome stores the history of visited sites in a file named **History**.
This file uses the [SQLite database
format](sqlite_database_format.md).

The **History** file can be found in same location as the
**Preferences** file.

There is also **Archived History** that predates information in the
**History** file. Note that the **Archived History** only contains
visits.

### Timestamps

The **History** file uses the different timestamps.

#### visits.visit_time

The **visits.visit_time** is in (the number of) microseconds since
January 1, 1601 UTC

Some Python code to do the conversion into human readable format:

    date_string = datetime.datetime( 1601, 1, 1 )
                + datetime.timedelta( microseconds=timestamp )

Note that this timestamp is not the same as a Windows filetime which is
(the number of) 100 nanoseconds since January 1, 1601 UTC

#### downloads.start_time

The **downloads.start_time** is in (the number of) seconds since January
1, 1970 UTC

Some Python code to do the conversion into human readable format:

    date_string = datetime.datetime( 1970, 1, 1 )
                + datetime.timedelta( seconds=timestamp )

### Example queries

Some example queries:

To get an overview of the visited sites:

    SELECT datetime(((visits.visit_time/1000000)-11644473600), "unixepoch"), urls.url, urls.title FROM urls, visits WHERE urls.id = visits.url;

Note that the visit_time conversion looses precision.

To get an overview of the downloaded files:

    SELECT datetime(downloads.start_time, "unixepoch"), downloads.url, downloads.full_path, downloads.received_bytes, downloads.total_bytes FROM downloads;

How the information of the downloaded files is stored in the database
can vary per version of Chrome as of version 26:

    SELECT datetime(((downloads.start_time/1000000)-11644473600), "unixepoch"), downloads.target_path, downloads_url_chains.url, downloads.received_bytes, downloads.total_bytes \
    FROM downloads, downloads_url_chains WHERE downloads.id = downloads_url_chains.id;

## Autofill

Chrome stores previous filled in form values a file named **Web Data**.
This file uses the [SQLite database
format](sqlite_database_format.md).

The **Web Data** file can be found in same location as the
**Preferences** file.

## Cookies

Chrome stores the cookies in a file named **Cookies**. This file uses
the [SQLite database format](sqlite_database_format.md).

### Extension Cookies

Chrome stores the cookies used by extensions in a file named **Extension
Cookies**. This file uses the [SQLite database
format](sqlite_database_format.md).

    SELECT datetime(((cookies.creation_utc/1000000)-11644473600), "unixepoch"), cookies.host_key, cookies.name, cookies.value, cookies.path, \
    datetime(((cookies.expires_utc/1000000)-11644473600), "unixepoch"), cookies.secure, cookies.httponly, datetime(((cookies.last_access_utc/1000000)-11644473600), "unixepoch"), \
    cookies.has_expires, cookies.persistent, cookies.priority FROM cookies;

## Extensions

Chrome extensions are stored under user data directory in the extensions
folder.

On Linux

    /home/$USER/.config/google-chrome/Default/Extensions/
    /home/$USER/.config/google-chrome-beta/Default/Extensions/
    /home/$USER/.config/chromium/Default/Extensions/

On MacOS-X

    /Users/$USER/Library/Application Support/Google/Chrome/Default/Extensions/
    /Users/$USER/Library/Application Support/Chromium/Default/Extensions/
    /Users/$USER/Library/Application Support/Google/Chrome Canary/Default/Extensions/

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Google\Chrome\User Data\Default\Extensions\
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Chromium\User Data\Default\Extensions\
    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Google\Chrome SxS\User Data\Default\Extensions\

On Windows Vista and later

    C:\Users\%USERNAME%\AppData\Local\Google\Chrome\User Data\Default\Extensions\
    C:\Users\%USERNAME%\AppData\Local\Chromium\User Data\Default\Extensions\
    C:\Users\%USERNAME%\AppData\Local\Google\Chrome SxS\User Data\Default\Extensions\

### Extension Activity database

Chrome, presumably as of version 29
[4](http://src.chromium.org/viewvc/chrome/trunk/src/chrome/browser/extensions/activity_log/activity_database.cc?view=log),
stores exension activity in a file named **Extension Activity**. This
file uses the [SQLite database
format](sqlite_database_format.md).

It can be turned on by running:

    ./google-chrome --enable-extension-activity-logging

Query to get most of the relevant data:

    SELECT datetime(((time/1000000)-11644473600), "unixepoch"), extension_id, action_type, api_name, args, page_url, page_title, arg_url, other, activity_id FROM activitylog_uncompressed;

The time span of the data tracked seems to be limited to a couple of
days but can be useful in troubleshooting extension behavior.

## Plugins

In the browser, you can view the plugins accessible by Chrome (and where
on the filesystem they reside) here:

    chrome://plugins/

Common Plugin install paths:

On Linux

    /opt/google/chrome
    /home/$USER/.config/

On MacOS-X

    /Library/Internet Plug-Ins/
    /Users/$USER/Library/Internet Plug-Ins/

On Windows

    ???

Plugins added through an extension will reside inside the extension
installation path.

## Visited Link

In order to store which link was visited (and color them purple when
links are rendered), Chrome uses the file **Visited Links** in the
profile directory.

The file starts with header (magic : " VLnk ") followed by a list of URL
fingerprints. No timing information is saved.

A URL
[fingerprint](https://chromium.googlesource.com/chromium/src/+/master/components/visitedlink/common/visitedlink_common.cc)
is computed the following way: **first 8 bytes of MD5( SALT + URL )**.
SALT is at offset 0x10 in the header.

The table is zero'ed if the user clears browsing history, and is not
updated in Private Mode.

TODO Explain discrepancies between the browsing history and this file.

## Chromium-based Browsers

[Chromium](https://en.wikipedia.org/wiki/Chromium_(web_browser)) is a
free and open-source web browser project, principally developed and
maintained by Google. This codebase provides the vast majority of code
for the Google Chrome browser, which is proprietary software and has
some additional features.

There are many other browsers that are based on the The Chromium
codebase. This section provides locations on disk of the user data for
several of those
[browsers](https://github.com/osquery/osquery/blob/6969e075fd4118e36f6cab54b0956e53dde5ba3f/osquery/tables/applications/chrome/utils.cpp):
Brave, Chromium, Yandex, Opera, Edge and EdgeBeta.

On Linux

    /home/$USER/.config/BraveSoftware/Brave-Browser/
    /home/$USER/.config/chrome-remote-desktop/chrome-config/google-chrome/
    /home/$USER/.config/chrome-remote-desktop/chrome-profile/
    /home/$USER/.config/chromium/
    /home/$USER/.config/google-chrome-beta/
    /home/$USER/.config/google-chrome/
    /home/$USER/.config/opera/
    /home/$USER/.config/yandex-browser-beta/
    /home/$USER/snap/chromium/common/chromium/

On MacOS-X

    /Users/$USER/Library/Application Support/BraveSoftware/Brave-Browser/
    /Users/$USER/Library/Application Support/Chromium/
    /Users/$USER/Library/Application Support/Google/Chrome Canary/
    /Users/$USER/Library/Application Support/Google/Chrome/
    /Users/$USER/Library/Application Support/Microsoft Edge Beta/
    /Users/$USER/Library/Application Support/Microsoft Edge/
    /Users/$USER/Library/Application Support/Yandex/YandexBrowser/
    /Users/$USER/Library/Application Support/com.operasoftware.Opera/

On Windows

    %APPDATA%\Opera Software\Opera Stable\
    %APPDATA%\Brave\
    %LOCALAPPDATA%\Chromium\
    %LOCALAPPDATA%\Google\Chrome SxS\
    %LOCALAPPDATA%\Google\Chrome\
    %LOCALAPPDATA%\Microsoft\Edge Beta\
    %LOCALAPPDATA%\Microsoft\Edge\
    %LOCALAPPDATA%\Yandex\YandexBrowser\

## See Also

- [Chrome Disk Cache Format](chrome_disk_cache_format.md)
- [SQLite database format](sqlite_database_format.md)

## External Links

- [Wikipedia article on Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome)
- [The Chromium Projects - User Data Directory](https://www.chromium.org/user-experience/user-data-directory/)
- [Chrome Disk Cache](http://www.chromium.org/developers/design-documents/network-stack/disk-cache)
- [Chrome support forum article random 10 character hostnames on startup](http://www.google.com/support/forum/p/Chrome/thread?tid=3511015c72a7b314&hl=en)
- [Chrome User Agent strings](https://www.useragentstring.com/pages/Chrome/)
- [Google Chrome Forensics](https://www.sans.org/digital-forensics-incident-response/),
  by [Kristinn Guðjónsson](kristinn_gudjonsson.md), January 21, 2010
- [Cashing in on the Google Chrome Cache](https://linuxsleuthing.blogspot.com/2013/02/cashing-in-on-google-chrome-cache.html?m=1),
  John Lehr, February 24, 2013
- [History Index files removed from Chrome v30](https://dfir.blog/history-index-files-removed-from-chrome-v30/),
  by Ryan Benson, October 2, 2013
- [The Chrome history was cleared! Now what?](https://dfir.blog/the-chrome-history-was-cleared-now-what-part-0/),
  by Ryan Benson, May 1, 2015
- [Evolution of Chrome Databases](https://dfir.blog/evolution-of-chrome-databases-reference-chart/),
  by Ryan Benson, November 12, 2013
- [Chromebook Forensics](https://www.dataforensics.org/google-chromebook-forensics/),
  by Dexter Morgan, April 30, 2015
- [The Chromium Projects - Configuring Other Preferences](https://www.chromium.org/administrators/configuring-other-preferences/)

## Tools

### Free Tools

- [Chromensics](https://sourceforge.net/projects/chromensics/)

### Open Source

- [Hindsight](https://github.com/obsidianforensics/hindsight)
- [Plaso](plaso.md)
