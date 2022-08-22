**TestDisk** is a free software data recovery utility licensed under the
terms of the GNU General Public License (GPL). It was primarily designed
to help recover lost data storage partitions and/or make non-booting
disks bootable again when these symptoms are caused by faulty software,
certain types of viruses or human error (such as accidentally erasing a
partition table).

[Forensics usage of TestDisk and
PhotoRec](http://www.cgsecurity.org/wiki/TestDisk_%26_PhotoRec_in_various_digital_forensics_testcase)
is described on the web site.

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

- [DOS](DOS "wikilink") (either real or in a Windows 9x DOS box);
- [Microsoft](Microsoft "wikilink") [Windows](Windows "wikilink") (NT4,
  2000, XP, 2003, Vista);
- [Linux](Linux "wikilink");
- [FreeBSD](FreeBSD "wikilink"), [NetBSD](NetBSD "wikilink"),
  [OpenBSD](OpenBSD "wikilink");
- SunOS and
- [Mac OS X](Mac_OS_X "wikilink")

## File systems

TestDisk can find lost partitions of the following file systems:

- Be File System (BeOS)
- BSD disklabel
  ([FreeBSD](FreeBSD "wikilink")/[OpenBSD](OpenBSD "wikilink")/[NetBSD](NetBSD "wikilink"))
- [Cramfs](Cramfs "wikilink"), Compressed File System
- DOS/Windows [FAT](FAT "wikilink") 12, 16, and 32
- [HFS](HFS "wikilink"), [HFS+](HFS+ "wikilink") and
  [HFSX](HFS+ "wikilink"), Hierarchical File System
- IBM Journaled File System 2 (JFS2), IBM's Journaled File System
- [Linux](Linux "wikilink") [ext2](ext2 "wikilink") and
  [ext3](ext3 "wikilink")
- [Linux](Linux "wikilink") RAID
  - RAID 1: mirroring
  - RAID 4: striped array with parity device
  - RAID 5: striped array with distributed parity information
  - RAID 6: striped array with distributed dual redundancy information
- Linux Swap (versions 1 and 2)
- [LVM](Linux_Logical_Volume_Manager_(LVM) "wikilink") and
  [LVM2](Linux_Logical_Volume_Manager_(LVM) "wikilink"), [Linux Logical
  Volume Manager](Linux_Logical_Volume_Manager_(LVM) "wikilink")
- Mac partition map
- Novell Storage Services (NSS)
- [NTFS](NTFS "wikilink") ([Windows](Windows "wikilink")
  NT/2000/XP/2003/Vista/2008)
- [ReiserFS](Reiserfs "wikilink") 3.5, 3.6 and 4
- Sun Solaris i386 disklabel
- Unix File System: [UFS](Unix_File_System "wikilink") and
  [UFS2](Unix_File_System "wikilink") (Sun/BSD/...)
- XFS, SGI's Journaled File System

## See also

- [PhotoRec](PhotoRec "wikilink")

## External links

- [TestDisk Wiki](http://www.cgsecurity.org/wiki/TestDisk)
- [TestDisk main functions
  review](http://howtorecover.me/cgsecurity-testdisk-partition-recovery-windows-app-review)