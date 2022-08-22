This article is intended to give a high-level overview of analyzing
program execution on the various operating systems. A typical operating
system has direct and indirect program executions indicators.

- direct indicators; these are artifacts of sub systems related to
  "executing" a program on the operating system, e.g. a Prefetch file.
- indirect indicators; these are artifacts that the program itself has
  left while running, e.g. a MRU Registry key.

This article focuses on the direct program execution indicators.

## Linux

## Mac OS X

## Windows

## See Also

- [Executable](Executable "wikilink")
- [Memory analysis](Memory_analysis "wikilink")

### Linux

- [Linux Memory Analysis](Linux_Memory_Analysis "wikilink")

### Mac OS X

- [Launch Agents](Mac_OS_X#Launch_Agents "wikilink")
- [Launch Daemons](Mac_OS_X#Launch_Daemons "wikilink")
- [Mac OS X Memory Analysis](Mac_OS_X_Memory_Analysis "wikilink")

### Windows

- Program crashes
  - Windows Error Reporting (WER)
  - Minidumps
- Services and drivers
- UserAssist Registry key
- [Windows Application
  Compatibility](Windows_Application_Compatibility "wikilink")
  - RecentFileCache.bcf
  - Amcache.hve
  - AppCompatCache Registry key
- [Windows Memory Analysis](Windows_Memory_Analysis "wikilink")
  - Hibernation file
  - Page file
- Windows Event Log
- Windows PC Accelerators
  - [Prefetch](Prefetch "wikilink")
  - [ReadyBoot](ReadyBoot "wikilink")
  - [ReadyBoost](ReadyBoost "wikilink")
  - [ReadyDrive](ReadyDrive "wikilink")
  - [SuperFetch](SuperFetch "wikilink")
- [Run/RunOnce Registry keys](Windows_Registry#Run/RunOnce "wikilink")
  (and equivalents)
- Windows Task Scheduler
  - [Job files](Windows_Job_File_Format "wikilink")
  - TaskCache Registry key
  - XML task/job files (C:\Windows\System32\Tasks,
    C:\Windows\SysWOW64\Tasks)

### Other

Note that third party tooling like "Anti-Virus" or Host-based Intrusions
Detection Systems (HIDS) can be used to track program executions. This
will vary per product.

## External Links

### Windows

- [HowTo: Determine Program
  Execution](http://windowsir.blogspot.com/2013/07/howto-determine-program-execution.html),
  by [Harlan Carvey](Harlan_Carvey "wikilink"), July 06, 2013
- [It Is All About Program
  Execution](http://journeyintoir.blogspot.com/2014/01/it-is-all-about-program-execution.html),
  by [Corey Harrell](Corey_Harrell "wikilink"), January 14, 2014
- [Know your Windows Processes or Die
  Trying](http://sysforensics.org/2014/01/know-your-windows-processes.html),
  by [Patrick Olsen](Patrick_Olsen "wikilink"), January 18, 2014

[Category:Analysis](Category:Analysis "wikilink")