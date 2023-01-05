---
tags:
  -  Tools
  -  Windows
  -  iOS
  -  MacOS
  -  Windows
  -  Commercial Software
  -  Web Browsers
---
Apple Safari is the default [web browser](web_browser.md)
included with [Mac OS X](mac_os_x.md).

## Locations

The Safari browser uses different locations to store different kind of
information.

The user directory:

On MacOS-X

    /Users/$USER/Library/Safari/

On Windows XP

    C:\Documents and Settings\%USERNAME%\Application Data\Apple Computer\Safari\

On Windows 7

    C:\Users\{user}\AppData\Roaming\Apple Computer\Safari\

The cache directory:

On MacOS-X

    /Users/$USER/Library/Caches/com.apple.Safari/

On Windows XP

    C:\Documents and Settings\%USERNAME%\Local Settings\Application Data\Apple Computer\Safari\

On Windows 7

    C:\Users\{user}\AppData\Local\Apple Computer\Safari\

## History

The browser history is stored in a [binary plist file](property_list.md) named
**History.plist** in the user directory.

For each website, the program records the URL visited, the date and time of
the last visit, and the number of times the site has been visited.

The date and time values are stored as a floating point value containing
the number of seconds since Jan 1, 2001 00:00:00 UTC.

## Downloads

The downloads history is stored in a [plist file](property_list.md) named
**Downloads.plist** in the user directory.

## Last Session

The browser last session information is stored in a [plist file](property_list.md)
named **LastSession.plist** in the user directory.

## Cache

The Safari cache is stored in **Cache.db** in the cache directory.

This file uses the [SQLite database
format](sqlite_database_format.md).

## External Links

- [Official website](https://www.apple.com/macos/ventura/)
- [Safari Cache
  Revisited](http://www.appleexaminer.com/files/Safari_Cache.db_Revisited.pdf)
  by Sean Cavanaugh
- [Analyzing Apple Safari
  Artifacts](http://www.appleexaminer.com/MacsAndOS/Analysis/HowTo/SafariBrowserAnalysis/SafariBrowserAnalysis.html),
  by Selena Ley
- [iOS / macOS - Tracking Downloads from Safari Without Downloads](https://blog.d204n6.com/2021/05/ios-macos-tracking-downloads-from.html)
  by Scott Vance, Friday, 28 May 2021

## Tools

- [J.A.F.A.T. Archive of Forensics Analysis
  Tools](https://jafat.sourceforge.net/) home of Safari Forensic Tools (SFT)
