---
tags:
  - Operating Systems
---
Initially Windows 8 had a workstation and server edition. The server
edition became Windows Server 2012.

## New Features

The following new features were introduced in Windows 8:

- [File History](windows_file_history.md)
- [Storage Spaces](windows_storage_spaces.md)
- Search Charm History

## File System

The file system used by Windows 8 is primarily [NTFS](ntfs.md).

The [Resilient File System
(refs)](resilient_file_system_(refs).md) was initially available
in the Windows 8 server edition but became part of Windows 2012 server
edition.

## Jump Lists

[Jump Lists](jump_lists.md) are Task Bar artifacts that were
first introduced on Windows 7 and are also available on Windows 8.

## [Prefetch](prefetch.md)

The prefetch hash function is similar to Windows 2008.

The [Windows Prefetch File
Format](windows_prefetch_file_format.md) was changed on Windows
8.1 to version 26. (note this could be Windows 8 as well but has not
been confirmed)

## Registry

The [Windows Registry](windows_registry.md) remains a core
component of the Windows operating system.

## Application Experience and Compatibility

On Windows 8 Amcache.hve replaces RecentFileCache.bcf and uses the
[Windows NT Registry File (regf)](windows_nt_registry_file_(regf).md) format.
A common location for Amcache.hve is:

    C:\Windows\AppCompat\Programs\Amcache.hve

## See Also

- [Windows](windows.md)
- [Windows Vista](windows_vista.md)
- [Windows 7](windows_7.md)

## External Links

- [Features new to Windows 8](http://en.wikipedia.org/wiki/Features_new_to_Windows_8), Wikipedia
- [Windows 8 Forensics - part 1](http://computerforensics.champlain.edu/blog/windows-8-forensics)
- [Windows 8 Forensics - part 2](http://computerforensics.champlain.edu/blog/windows-8-forensics-part-2)
- [Windows 8 Forensics - part 3](http://computerforensics.champlain.edu/blog/windows-8-forensics-part-3)
- [Windows 8 Registry Forensics](http://www.dataforensics.org/windows-8-file-history-forensics/)
- [Windows 8 Forensic Guide](http://propellerheadforensics.files.wordpress.com/2012/05/thomson_windows-8-forensic-guide2.pdf),
  by [Amanda C. F. Thomson](amanda_thomson.md), 2012
- [Forensic Focus: Windows 8 Forensics - A First Look](https://www.forensicfocus.com/Forums/viewtopic/t=9604/),
  [Presentation](http://www.youtube.com/watch?v=uhCooEz9FQs&feature=youtu.be),
  [Slides](https://www.forensicfocus.com/downloads/windows-8-forensics-josh-brunty.pdf),
  by [Josh Brunty](josh_brunty.md), August 2012
- [Windows 8: Tracking Opened Photos](http://dfstream.blogspot.ch/2013/03/windows-8-tracking-opened-photos.html),
  by Jason Hale, March 8, 2013
- [Windows 8 and 8.1: Search Charm History](http://dfstream.blogspot.com/2013/09/windows-8-and-81-search-charm-history.html),
  by Jason Hale, September 9, 2013
- [Amcache.hve in Windows 8 - Goldmine for malware hunters](http://www.swiftforensics.com/2013/12/amcachehve-in-windows-8-goldmine-for.html),
  by Yogesh Khatri, December 4, 2013
- [Amcache.hve - Part 2](http://www.swiftforensics.com/2013/12/amcachehve-part-2.html), by
  Yogesh Khatri, December 16, 2013
- [SRUM forensics](https://files.sans.org/summit/Digital_Forensics_and_Incident_Response_Summit_2015/PDFs/Windows8SRUMForensicsYogeshKhatri.pdf),
  by Yogesh Khatri
