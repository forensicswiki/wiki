---
tags:
  - Data Recovery
  - FreeBSD
  - Linux
  - MacOS
  - NetBSD
  - OpenBSD
  - Solaris
  - Tools
  - Windows
---
**TestDisk** is a free software data recovery utility licensed under the
terms of the GNU General Public License (GPL). It was primarily designed
to help recover lost data storage partitions and/or make non-booting
disks bootable again when these symptoms are caused by faulty software,
certain types of viruses or human error (such as accidentally erasing a
partition table).

[Forensics usage of TestDisk and
PhotoRec](https://www.cgsecurity.org/wiki/TestDisk_%26_PhotoRec_in_various_digital_forensics_testcase)
is described on the website.

## Summary

TestDisk queries the BIOS or the operating system in order to find the
hard disks and their characteristics (LBA size and Cylinder-head-sector
geometry). TestDisk does a quick check of your disk's structure and
compares it with your Partition Table for entry errors. If the Partition
Table has entry errors, TestDisk can repair them.

However, it's up to the user to look over the list of possible
partitions found by TestDisk and to select the one(s) which were being
used just before the drive failed to boot or the partition(s) were lost.
In some cases, especially after initiating a detailed search for lost
partitions, TestDisk may show partition data which is simply from the
remnants of a partition that had been deleted and overwritten long ago.

TestDisk has features for both novices and experts. For those who know
little or nothing about data recovery techniques, TestDisk can be used
to collect detailed information about a non-booting drive which can then
be sent to a tech for further analysis. Those more familiar with such
procedures should find TestDisk a handy tool in performing onsite
recovery.

## Supported operating systems

- DOS;
- [Microsoft Windows](windows.md) (NT4, 2000, XP, 2003, Vista);
- [Linux](linux.md);
- [FreeBSD](freebsd.md), [NetBSD](netbsd.md ),
  [OpenBSD](openbsd.md);
- SunOS and
- [Mac OS X](mac_os_x.md)

## File systems

TestDisk can find lost partitions of the following file systems:

- Be File System (BeOS)
- BSD disklabel
  ([FreeBSD](freebsd.md)/[OpenBSD](openbsd.md)/[NetBSD](netbsd.md)
- Cramfs, Compressed File System
- DOS/Windows [FAT](fat.md) 12, 16, and 32
- (Classic) HFS, [HFS+](hfs+.md) and [HFSX](hfs+.md), Hierarchical File
  System
- IBM Journaled File System 2 (JFS2), IBM's Journaled File System
- [Linux](linux.md) [ext2 and ext3](extended_file_system_(ext).md)
- [Linux](linux.md) RAID
  - RAID 1: mirroring
  - RAID 4: striped array with parity device
  - RAID 5: striped array with distributed parity information
  - RAID 6: striped array with distributed dual redundancy information
- Linux Swap (versions 1 and 2)
- [Linux Logical Volume Manager](linux_logical_volume_manager_(lvm).md) (LVM and LVM2)
- Mac partition map
- Novell Storage Services (NSS)
- [NTFS](ntfs.md) ([Windows](windows.md)
  NT/2000/XP/2003/Vista/2008)
- [ReiserFS](reiserfs.md) 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System: [UFS and UFS2](unix_file_system_(ufs).md) (Sun/BSD/...)
- XFS, SGI's Journaled File System

## External links

- [TestDisk Wiki](https://www.cgsecurity.org/wiki/TestDisk)
- [TestDisk main functions review](https://howtorecover.me/cgsecurity-testdisk-partition-recovery-windows-app-review)
