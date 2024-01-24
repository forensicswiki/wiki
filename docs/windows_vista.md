---
tags:
  - Operating Systems
  - Windows
---
## New Features

- [BitLocker](bitlocker_disk_encryption.md)
- [Search](windows_desktop_search.md) integrated in operating
  system
- [ReadyBoost](readyboost.md)
- [SuperFetch](superfetch.md)
- [Transactional NTFS (txf)](ntfs.md)
- [Transactional Registry (txr)](windows_nt_registry_file_(regf).md)
- [Shadow Volumes](windows_shadow_volumes.md); the volume-based
  storage of the Volume Shadow Copy data
- \$Recycle.Bin
- [Windows XML Event Log (evtx)](windows_xml_event_log_(evtx).md)
- [User Account Control (uac)](user_account_control_(uac).md)

## File System

The file system used by Windows Vista is primarily
[NTFS](ntfs.md).

In Windows Vista, NTFS no longer tracks the Last Access time of a file
by default. This feature can be enabled by setting the
NtfsDisableLastAccessUpdate value to '0' in the Registry key:

    HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem

Note that this feature has been around since as early as Windows 2000
[1](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-2000-server/cc959914(v=technet.10)?redirectedfrom=MSDN).

## [Prefetch](prefetch.md)

Note that the prefetch hash function is different then that of Windows XP.

The [Windows Prefetch File Format](windows_prefetch_file_format.md) was changed
to version 23.

## Registry

The [Windows Registry](windows_registry.md) remains a central component of the
Windows Vista operating system.

## User Interface Privilege Isolation (UIPI)

As part of the secure initiative in Vista, applications with UI will run
in three different levels of privilege. Application windows can interact
with others windows of the same or lower levels, but cannot interact
with applications at higher level/permission.

## See Also

- [SuperFetch](superfetch.md)
- [Windows](windows.md)
- [Windows 7](windows_7.md)
- [Windows 8](windows_8.md)

## External Links

- [Windows Vista Network Attack Surface Analysis](https://www.grc.com/sn/files/atr-vistaattacksurface.pdf),
  by Tim Newsham, James Hoagland
- [Inside the Windows Vista Kernel: Part 1](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc162494(v=msdn.10)),
  by [Mark Russinovich](mark_russinovich.md), February 2007
- [Inside the Windows Vista Kernel: Part 2](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc162480(v=msdn.10)?redirectedfrom=MSDN),
  by [Mark Russinovich](mark_russinovich.md), March 2007
- [Inside the Windows Vista Kernel: Part 3](https://learn.microsoft.com/en-us/previous-versions/technet-magazine/cc162458(v=msdn.10)),
  by [Mark Russinovich](mark_russinovich.md), April 2007
- [Forensic Implications of Windows Vista](https://whereismydata.files.wordpress.com/2009/09/forensic-implications-of-windows-vista.pdf),
  by Barrie Stewart, September 2007
