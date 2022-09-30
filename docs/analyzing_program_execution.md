---
tags:
  -  Analysis
---
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

- [Executable](executable.md)
- [Memory analysis](memory_analysis.md)

### Linux

- [Linux Memory Analysis](linux_memory_analysis.md)

### Mac OS X

- [Launch Agents](mac_os_x#launch_agents.md)
- [Launch Daemons](mac_os_x#launch_daemons.md)
- [Mac OS X Memory Analysis](mac_os_x_memory_analysis.md)

### Windows

- Program crashes
  - Windows Error Reporting (WER)
  - Minidumps
- Services and drivers
- UserAssist Registry key
- [Windows Application
  Compatibility](windows_application_compatibility.md)
  - RecentFileCache.bcf
  - Amcache.hve
  - AppCompatCache Registry key
- [Windows Memory Analysis](windows_memory_analysis.md)
  - Hibernation file
  - Page file
- Windows Event Log
- Windows PC Accelerators
  - [Prefetch](prefetch.md)
  - [ReadyBoot](readyboot.md)
  - [ReadyBoost](readyboost.md)
  - [ReadyDrive](readydrive.md)
  - [SuperFetch](superfetch.md)
- [Run/RunOnce Registry keys](windows_registry#run/runonce.md)
  (and equivalents)
- Windows Task Scheduler
  - [Job files](windows_job_file_format.md)
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
  by [Harlan Carvey](harlan_carvey.md), July 06, 2013
- [It Is All About Program
  Execution](http://journeyintoir.blogspot.com/2014/01/it-is-all-about-program-execution.html),
  by [Corey Harrell](corey_harrell.md), January 14, 2014
- [Know your Windows Processes or Die
  Trying](http://sysforensics.org/2014/01/know-your-windows-processes.html),
  by [Patrick Olsen](patrick_olsen.md), January 18, 2014

