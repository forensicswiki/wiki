---
tags:
  - Commercial Software
  - iOS
  - Mac OS
  - Tools
  - Web Browsers
  - Windows
---
Apple Safari is the default [web browser](web_browser.md)
included with [Mac OS X](mac_os_x.md).

## Locations

The Safari browser uses different locations to store different kind of
information.

The user directory:

On Mac OS X

```text
/Users/$USER/Library/Safari/
```

On Windows XP

```text
C:\Documents and Settings\%USERNAME%\Application Data\Apple Computer\Safari\
```

On Windows 7

```text
C:\Users\{user}\AppData\Roaming\Apple Computer\Safari\
```

The cache directory:

On Mac OS X

```text
/Users/$USER/Library/Caches/com.apple.Safari/
```

On Windows XP

```text
C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Apple Computer\Safari\
```

On Windows 7

```text
C:\Users\{user}\AppData\Local\Apple Computer\Safari\
```

## History

The browser history is stored in a [binary plist file](property_list_(plist).md) named
**History.plist** in the user directory.

For each website, the program records the URL visited, the date and time of
the last visit, and the number of times the site has been visited.

The date and time values are stored as a floating point value containing
the number of seconds since Jan 1, 2001 00:00:00 UTC.

## Downloads

The downloads history is stored in a [plist file](property_list_(plist).md) named
**Downloads.plist** in the user directory.

## Last Session

The browser last session information is stored in a [plist file](property_list_(plist).md)
named **LastSession.plist** in the user directory.

## Cache

The Safari cache is stored in **Cache.db** in the cache directory.

This file uses the [SQLite database format](sqlite_database_format.md).

## External Links

* [iOS / macOS - Tracking Downloads from Safari Without Downloads](https://blog.d204n6.com/2021/05/ios-macos-tracking-downloads-from.html)
  by Scott Vance, May 28, 2021

## Tools

* [J.A.F.A.T. Archive of Forensics Analysis Tools](https://jafat.sourceforge.net/) home of Safari
  Forensic Tools (SFT)
