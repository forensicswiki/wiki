---
tags:
  -  Disk Analysis
  -  Tools
  -  Windows
  -  Linux
  -  MacOS
  -  FreeBSD
  -  NetBSD
  -  OpenBSD
  -  Open Source Software
---
**Snorkel** is a Java software library that is used by developers of
forensic software. Snorkel is not a standalone forensic application, but
it is an important piece of infrastructure that can be used by many
forensic applications: Snorkel gives access to digital evidence files,
file systems, files, slack space, unallocated clusters, etc. This type
of access is a key enabler in the development of forensic software
systems, ranging from single-purpose stand-alone tools to integrated
forensic processing systems.

Snorkel is developed by the Netherlands Forensic Institute

# Features

Snorkel recognizes and gives access to numerous storage formats for
digital evidence, disk partitioning schemes, volume managers, file
systems, and structured files. The formats supported are summarized
below.

## Image File Formats Understood

|                    |                                                               |
|--------------------|---------------------------------------------------------------|
| Image file formats | [EnCase](encase_image_file_format.md)                 |
|                    | [RAW (dd)](raw_image_format.md)                       |
|                    | [VMWare (vmdk)](vmware_virtual_disk_format_(vmdk).md) |

## File Systems Understood

|                      |                                                                               |
|----------------------|-------------------------------------------------------------------------------|
| Volume managers      | [Windows (ldm)](logical_disk_manager_(ldm).md)                        |
| Partitioning schemes | PC/MBR                                                                        |
|                      | Apple                                                                         |
|                      | GPT                                                                           |
|                      | BSD                                                                           |
| File systems         | Windows ([fat](fat.md), [NTFS](ntfs.md))                      |
|                      | Apple ([mfs](mfs.md), (Traditional) HFS, [HFS+](hfs+.md)) |
|                      | Linux ([ext](extended_file_system_(ext).md), [Reiser](reiserfs.md))                 |
|                      | Solaris, BSD ([ufs](ufs.md)                                          |
|                      | CD ([iso9660](iso9660.md)                                    |
| File Formats         | Windows registry (Win 9x, NT)                                                 |
|                      | Microsoft Office (OLE2)                                                       |

## License Notes

Snorkel is has a proprietary license. An evaluation version is available
from the website.

# External Links

- [the Netherlands Forensic
  Institute](http://www.forensischinstituut.nl/)
- [Snorkel website](http://www.holmes.nl/NFIlabs/Snorkel)
