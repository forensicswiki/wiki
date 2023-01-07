---
tags:
  - No Category
---
The LastVisitedMRU Windows Registry key records recently used
applications and the last path those applications used to open a file
[1](https://www.sans.org/digital-forensics-incident-response/).
It is used by the Windows operating system to store common paths used to
open or save files and provide auto-complete services to the user within
the Windows Common Dialog. The Common Dialog libraries can be used by
any Windows application and Microsoft highly recommends that developers
use them instead of creating novel user interface elements
[2](https://learn.microsoft.com/en-us/).
A wide variety of applications use the Common Dialog, including
encryption products like TrueCrypt, media players, and document viewers.

## Registry Key Location

The key is present in each user's NTUSER.DAT at
\Software\Microsoft\Windows\CurrentVersion\Explorer\ComDIg32\LastVisitedMRU.
It contains data stored as registry values and a
[MRUList](list_of_windows_mru_locations.md). Value data is
stored in binary (REG_BINARY) format.

## LastVisitedMRU in Windows 7

Starting with Windows Vista, the key was renamed to LastVisitedPidlMRU.