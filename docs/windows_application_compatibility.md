---
tags:
  - Windows
---
## sysmain.sdb

System compatibility database.

## RecentFileCache.bcf

In Windows 7 the RecentFileCache.bcf file is stored in:

    C:\Windows\AppCompat\Programs\

## Amcache.hve

See: [AMCache](amcache.md)

## AppCompatCache

In Windows 2000 and XP:

    Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatibility

In Windows 2003 and later:

    Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\AppCompatCache

## External Links

* [Demystifying Shims - or - Using the App Compat Toolkit to make your old stuff work with your new stuff](https://techcommunity.microsoft.com/t5/ask-the-performance-team/demystifying-shims-or-using-the-app-compat-toolkit-to-make-your/ba-p/374947),
  by [Microsoft](microsoft.md)
* [Application Compatibility Database](https://learn.microsoft.com/en-us/windows/win32/devnotes/application-compatibility-database),
  by [Microsoft](microsoft.md)
* [Secrets of the Application Compatilibity Database (SDB) – Part 1](https://www.alex-ionescu.com/?p=39),
  by Alex Ionescu, May 20, 2007
* [Secrets of the Application Compatilibity Database (SDB) – Part 2](https://www.alex-ionescu.com/?p=40),
  by Alex Ionescu, May 21, 2007
* [Secrets of the Application Compatilibity Database (SDB) – Part 3](https://www.alex-ionescu.com/?p=41),
  by Alex Ionescu, May 26, 2007
* Leveraging the Application Compatibility Cache in Forensic Investigations
  by Andrew Davis, May 4, 2012
* [Revealing Program Compatibility Assistant HKCU AppCompatFlags Registry Keys](http://journeyintoir.blogspot.com/2013/12/revealing-program-compatibility.html),
  by Corey Harrell, December 17, 2013
* [Persist It Using and Abusing Microsoft’s Fix It Patches](https://www.blackhat.com/docs/asia-14/materials/Erickson/WP-Asia-14-Erickson-Persist-It-Using-And-Abusing-Microsofts-Fix-It-Patches.pdf),
  by Jon Erickson, BlackHat Asia 2014
* [Shim Shady: Live Investigations of the Application Compatibility Cache](https://www.fireeye.com/blog/threat-research/2015/10/shim_shady_live_inv.html),
  by Fred House, Claudiu Teodorescu, Andrew Davis, October 27, 2015
* [Shim Shady Part 2](https://www.fireeye.com/blog/threat-research/2015/10/shim_shady_live_inv/shim-shady-part-2.html)
* [To SDB, Or Not To SDB: FIN7 Leveraging Shim Databases for Persistence](https://www.mandiant.com/resources/blog/fin7-shim-databases-persistence)

### RecentFileCache

* [Revealing the RecentFileCache.bcf File](http://journeyintoir.blogspot.com/2013/12/revealing-recentfilecachebcf-file.html),
  by Corey Harrell, December 2, 2013
* [Triaging with the RecentFileCache.bcf File](http://journeyintoir.blogspot.com/2014/04/triaging-with-recentfilecachebcf-file.html),
  by Corey Harrell, April 21, 2014
