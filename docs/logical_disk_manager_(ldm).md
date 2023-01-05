---
tags:
  - Volume Systems
---
The [Windows](windows.md) Logical Disk Manager, is commonly
abbreviated to LDM.

## On-disk structures

According to
[TECHNET](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc737048(v=ws.10)?redirectedfrom=MSDN):

The location of the database is determined by the partition style of the
disk.

- On MBR disks, the database is contained in the last 1 megabyte (MB) of
  the disk.
- On GPT disks, the database is contained in a 1-MB reserved (hidden)
  partition known as the Logical Disk Manager (LDM) Metadata partition.

## Types of dynamic volumes

- Simple volume
- Spanned volume
- Striped volume
- Mirrored volume (Server editions of Windows 2000, Windows 2003)
- RAID-5 volume (Server editions of Windows 2003)

## Also see

- [File Systems](tags/#file-systems)

## External Links

- \[<https://learn.microsoft.com/en-us/>).aspx
  Basic and Dynamic Disks\], by Microsoft
- [What Are Dynamic Disks and
  Volumes?](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc737048(v=ws.10)?redirectedfrom=MSDN),
  by Microsoft, March 2003
- [Dynamic disks and
  volumes](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc757696(v=ws.10)?redirectedfrom=MSDN), by
  Microsoft, January 2005
- [Logical Disk Manager documentation](http://www.ntfs.com/ldm.htm)

