---
tags:
  -  Applications
---
Microsoft Internet Explorer (MSIE) is the default [Web
Browser](web_browser.md) included with [Microsoft
Windows](microsoft_windows.md).

## MSIE 4 to 9

MSIE 4 to 9 uses the [Internet Explorer History File
Format](internet_explorer_history_file_format.md) (or MSIE 4-9
Cache File format). The Cache Files commonly named index.dat are used to
store both cache and historical information.

## MSIE 10

    C:\Users\%USER%\AppData\Local\Microsoft\Windows\WebCache\

The WebCacheV01.dat and WebCacheV24.dat files are in the [Extensible
Storage Engine (ESE) Database File (EDB)
format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)

## Configuration

Internet Explorer will apply its setting in the following order, where
the lower the order overrides settings in the higer order.

1.  Settings in Machine policy key
2.  Settings in User policy key
3.  Settings in User preference key
4.  Settings in Machine preference key

Machine policy key

    HKET_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings

Machine preference key

    HKET_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings

User policy key

    HKEY_CURRENT_USER\SOFTWARE\Policies\Microsoft\Windows\CurrentVersion\Internet Settings

User preference key

    HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings

### Security Zones

0 - My Computer

1 - Local Intranet Zone

2 - Trusted Sites Zone

3 - Internet Zone

4 - Restricted Sites Zone

5 - Custom

### WPAD

<b>TODO add some text</b>

## Command line options

MSIE supports various command line options, see:
\[<http://msdn.microsoft.com/en-us/library/ie/hh826025(v=vs.85>).aspx\]
and
[1](http://windowssecrets.com/top-story/little-known-browser-commands-and-functions/)

## Artifacts

### Recovery store

<b>TODO add some text</b>

On Windows Vista and later:

    C:\Users\%USER%\AppData\Local\Microsoft\Internet Explorer\Recovery

### Typed URLs

Internet Explorer stores the cached History (or Address box) entries in
the following Windows Registry key
[2](http://support.microsoft.com/kb/157729).

    HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\TypedURLs

## See Also

- [Extensible Storage Engine (ESE) Database File (EDB)
  format](extensible_storage_engine_(ese)_database_file_(edb)_format.md)
- [Internet Explorer 4-9 Cache File
  Format](internet_explorer_history_file_format.md)

## External Links

- [Internet Explorer
  Cache](http://kb.digital-detective.co.uk/display/NetAnalysis1/Internet+Explorer+Cache)
- [Internet Explorer security zones registry entries for advanced
  users](http://support.microsoft.com/kb/182569), by
  [Microsoft](microsoft.md)
- [Troubleshooting Automatic
  Detection](http://technet.microsoft.com/en-us/library/cc302643.aspx),
  by [Microsoft](microsoft.md)
- [Windows Virtual PC VHDs for testing websites with different Internet
  Explorer
  versions](http://www.microsoft.com/en-us/download/details.aspx?id=11575),
  by [Microsoft](microsoft.md)
- \[<http://msdn.microsoft.com/en-us/library/ie/hh826025(v=vs.85>).aspx
  IE Command-Line Options\], by [Microsoft](microsoft.md),
  January, 2011
- [Little-known browser commands and
  functions](http://windowssecrets.com/top-story/little-known-browser-commands-and-functions/),
  by Fred Langa, June 21, 2012
- [Java Web Vulnerability Mitigation on
  Windows](http://tojoswalls.blogspot.com/2013/05/java-web-vulnerability-mitigation-on.html),
  by Tim Johnson, May 23, 2013
- [Internet Explorer EPM Sandbox Escape
  CVE-2014-6350](http://googleprojectzero.blogspot.co.uk/2014/12/internet-explorer-epm-sandbox-escape.html),
  by James Forshaw, December 1, 2014

### Recovery store

- [Internet Explorer RecoveryStore (aka Travelog) as evidence of
  Internet Browsing
  activity](http://www.swiftforensics.com/2011/09/internet-explorer-recoverystore-aka.html),
  by [Yogesh Khatri](yogesh_khatri.md), September 29, 2011

### Typed URLS

- [TypedURLs (Part
  1)](http://crucialsecurityblog.harris.com/2011/03/14/typedurls-part-1/),
  by Paul Nichols, March 14, 2011
- [TypedURLs (Part
  2)](http://crucialsecurityblog.harris.com/2011/03/23/typedurls-part-2/),
  by Paul Nichols, March 23, 2011
- [The Trouble with
  TypedUrlsTime](http://randomthoughtsofforensics.blogspot.co.uk/2012/07/trouble-with-typedurlstime.html),
  by Ken Johnson, July 4, 2012
- [TypedURLs Registry
  Key](http://sketchymoose.blogspot.ch/2014/02/typedurls-registry-key.html),
  Sketchymoose's Blog, February 18, 2014

### Internet Explorer 10

- [Windows 8 Forensics: Internet History
  Cache](http://cyberarms.wordpress.com/2012/08/21/windows-8-forensics-internet-cache-history/),
  by Ethan Fleisher, August 21, 2012
- [Forensic Analysis of ESE databases in Internet Explorer
  10](http://hh.diva-portal.org/smash/get/diva2:635743/FULLTEXT02.pdf),
  by Bonnie Malmström & Philip Teveldal, June 2013

[Category:Applications](category:applications.md) [Category:Web
