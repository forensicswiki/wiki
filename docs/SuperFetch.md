SuperFetch is a performance enhancement introduced in
[Microsoft](Microsoft "wikilink") [Windows Vista](Windows "wikilink") to
reduce the time necessary to launch applications. SuperFetch works with
the memory manager service in Windows to analyze memory usage patterns
over time to determine the optimal memory content for a given user for a
date or time of day. This differs from the
[Prefetch](Prefetch "wikilink") technique used in Microsoft Windows XP,
which preloads data into memory without analyzing usage patterns.

From
\[<http://msdn.microsoft.com/en-us/library/windows/hardware/dn653317(v=vs.85>).aspx\]:
SuperFetch prioritizes the following kinds of pages to remain in memory:

- Pages of applications that are used most frequently overall.
- Pages of applications that are commonly used when resuming:
  - After extensive hibernation (for example, first thing in the
    morning).
  - After shorter periods of sleep or hibernation (for example, after
    lunch).

Prefetched pages are added to the system’s standby page list, which has
been reorganized and redesigned to retain useful data in memory over
longer periods of time.

If SuperFetch detects that the system drive is a fast SSD (as measured
by Windows Experience Index Disk score), then SuperFetch turns off
[ReadyBoot](ReadyBoot "wikilink"), [ReadyBoost](ReadyBoost "wikilink"),
and the SuperFetch service itself.

To calculate the Windows Experience Index Disk score run:

    winsat formal

## Components

### Robust performance

Robust performance (or robustness) is a component of SuperFetch to watch
for specific file I/O access that might harm system performance by
populating the standby lists with unneeded data.

## Scenarios

SuperFetch distinguishes between different scenarios to accurately
measure performance.

### Cold scenario

In a cold scenario, the test applications are not already in memory when
the test begins. Cold scenarios measure performance either after a state
transition, such as boot or resume from hibernation, or after another
application claims most of the available memory, such as after launching
and quitting a game.

### Warm scenario

In a warm scenario, some or all the scenario contents are in memory
before measurement. This usually means that the test has run at least
once during this logon session.

### Performance scenarios

Performance scenarios defined by the Windows Performance Recorder (WPR):

- General: Records general performance while the computer is running.
- On/Off - Boot: Records performance while the computer is booting.
- On/Off – Fast Startup: Records performance during a fast startup.
- On/Off - Shutdown: Records performance while shutting the computer
  down.
- On/Off - RebootCycle: Records performance during the entire cycle
  while the computer is rebooting.
- On/Off - Standby/Resume: Records performance when the computer is
  placed on standby and then resumed.
- On/Off - Hibernate/Resume: Records performance when the computer is
  placed in hibernation and then resumed.

Where "On/Off" likely refers to a cold scenario.

## Configuration

Because SuperFetch appears to leave a system with no available memory,
some users turn it off to create the appearance of having more free
memory. The feature can be configured by changing the
[Registry](Registry "wikilink") value
[1](http://www.codinghorror.com/blog/archives/000688.html):

    Key: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters
    Value: EnableSuperfetch

A value of zero disables SuperFetch, one enables it for booting only,
two for applications, and three for both applications and boot. This
setting can also be changed using the Services console, `services.msc`
[2](http://tiredblogger.wordpress.com/2007/03/27/superfetch-not-so-super-for-gaming/).

## File Formats

Data for SuperFetch is gathered by the
`%SystemRoot%\System32\Sysmain.dll`, part of the Service Host process,
`%SystemRoot%\System32\Svchost.exe`, and stored in a series of files in
the `%SystemRoot%\Prefetch` directory
[3](http://www.microsoft.com/technet/technetmag/issues/2007/03/VistaKernel/).
These files appear to start with the prefix `Ag` and have a `.db`
extension. Note that there are likely more SuperFetch database files
named differently, presumably all using the .db extension.

The format of the SuperFetch database files is not fully known, there is
available unofficial partial specification
[4](http://blog.rewolf.pl/blog/?p=214) and open source (GPL) dumper for
.db files [5](http://code.google.com/p/rewolf-superfetch-dumper/). For
more information see [SuperFetch
Format](Windows_SuperFetch_Format "wikilink").

The SuperFetch feature is seeded with some basic usage patterns when the
operating system is installed
[6](http://channel9.msdn.com/showpost.aspx?postid=242429).

The SuperFetch service is managed by the File Information FS MiniFilter
service. It appears that most of the SuperFetch database files are
updated (written) when the service is shut down. AgAppLaunch.db is also
written when the service starts.

## See Also

- [Prefetch](Prefetch "wikilink")
- [ReadyBoost](ReadyBoost "wikilink")
- [ReadyBoot](ReadyBoot "wikilink")
- [SuperFetch Format](Windows_SuperFetch_Format "wikilink")
- [Windows](Windows "wikilink")

## External Links

- [Inside the Windows Vista Kernel: Part
  2](http://technet.microsoft.com/en-us/magazine/2007.03.vistakernel.aspx),
  by [Mark Russinovich](Mark_Russinovich "wikilink"), March 2007
- [Performance Testing Guide
  for Windows](http://download.microsoft.com/download/7/E/7/7E7662CF-CBEA-470B-A97E-CE7CE0D98DC2/Win7Perf.docx),
  by [Microsoft](Microsoft "wikilink"), August 18, 2009 
- [Performance
  Scenarios](http://msdn.microsoft.com/en-us/library/windows/hardware/hh162965.aspx),
  by [Microsoft](Microsoft "wikilink"), October 20, 2013
- [Wikipedia: Windows Vista I/O technologies -
  SuperFetch](http://en.wikipedia.org/wiki/Windows_Vista_I/O_technologies#SuperFetch)
- [Channel 9 Interview with Michael Fortin of Microsoft on
  SuperFetch](http://channel9.msdn.com/showpost.aspx?postid=242429)
- [Microsoft Predicts The Future With Vista's
  SuperFetch](http://www.informationweek.com/news/showArticle.jhtml?articleID=196902178)
  from Information Week
- [DC3 Presentation: My You Look
  SuperFetching](http://jessekornblum.com/presentations/dodcc08-2.pdf),
  by Jesse Kornblum

## Tools

### Open Source

- [rewolf-superfetch-dumper](https://code.google.com/p/rewolf-superfetch-dumper/)
- [CrowdResponse](https://www.crowdstrike.com/resources/community-tools/crowdresponse/)

[Category:Windows](Category:Windows "wikilink")