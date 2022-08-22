## New Features

- [BitLocker](BitLocker_Disk_Encryption "wikilink")
- [Search](Windows_Desktop_Search "wikilink") integrated in operating
  system
- [ReadyBoost](ReadyBoost "wikilink")
- [SuperFetch](SuperFetch "wikilink")
- [Transactional NTFS (TxF)](NTFS "wikilink")
- [Transactional Registry
  (TxR)](Windows_NT_Registry_File_(REGF) "wikilink")
- [Shadow Volumes](Windows_Shadow_Volumes "wikilink"); the volume-based
  storage of the Volume Shadow Copy data
- \$Recycle.Bin
- [Windows XML Event Log
  (EVTX)](Windows_XML_Event_Log_(EVTX) "wikilink")
- [User Account Control (UAC)](User_Account_Control_(UAC) "wikilink")

## File System

The file system used by Windows Vista is primarily
[NTFS](NTFS "wikilink").

In Windows Vista, NTFS no longer tracks the Last Access time of a file
by default. This feature can be enabled by setting the
NtfsDisableLastAccessUpdate value to '0' in the Registry key:

    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem

Note that this feature has been around since as early as Windows 2000
[1](http://technet.microsoft.com/en-us/library/cc959914.aspx).

## [Prefetch](Prefetch "wikilink")

Note that the prefetch hash function is different then that of [Windows
XP](Windows_XP "wikilink").

The [Windows Prefetch File
Format](Windows_Prefetch_File_Format "wikilink") was changed to version
23.

## Registry

The [Windows Registry](Windows_Registry "wikilink") remains a central
component of the Windows Vista operating system.

## User Interface Privilege Isolation (UIPI)

As part of the secure initiative in Vista, applications with UI will run
in three different levels of privilege. Application windows can interact
with others windows of the same or lower levels, but cannot interact
with applications at higher level/permission.

## See Also

- [SuperFetch](SuperFetch "wikilink")
- [Windows](Windows "wikilink")
- [Windows 7](Windows_7 "wikilink")
- [Windows 8](Windows_8 "wikilink")

## External Links

- [Windows Vista Network Attack Surface
  Analysis](https://www.symantec.com/avcenter/reference/Vista_Network_Attack_Surface_RTM.pdf),
  James Hoagland, Matt Conover, Tim Newsham, Ollie Whitehouse
- [Inside the Windows Vista Kernel: Part
  1](http://technet.microsoft.com/en-us/magazine/2007.02.vistakernel.aspx),
  by [Mark Russinovich](Mark_Russinovich "wikilink"), February 2007
- [Inside the Windows Vista Kernel: Part
  2](http://technet.microsoft.com/en-us/magazine/2007.03.vistakernel.aspx),
  by [Mark Russinovich](Mark_Russinovich "wikilink"), March 2007
- [Inside the Windows Vista Kernel: Part
  3](http://technet.microsoft.com/en-us/magazine/2007.04.vistakernel.aspx),
  by [Mark Russinovich](Mark_Russinovich "wikilink"), April 2007
- [Forensic Implications of Windows
  Vista](http://whereismydata.files.wordpress.com/2009/09/forensic-implications-of-windows-vista.pdf),
  by Barrie Stewart, September 2007
- [What is User Interface Privilege Isolation (UIPI) on
  Vista](http://blogs.msdn.com/b/vishalsi/archive/2006/11/30/what-is-user-interface-privilege-isolation-uipi-on-vista.aspx),
  VishalSi, November 30, 2006

[Category:Operating systems](Category:Operating_systems "wikilink")