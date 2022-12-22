---
tags:
  -  Disk Encryption
  -  Encryption
  -  Anti-Forensics
  -  File Systems
  -  MacOS
  -  Windows
  -  Linux
---
# Conventional File Systems

[Apple File System (apfs)](apple_file_system_(apfs).md)
A file system for [Apple](apple.md) systems optimized for
flash/SSD media.

<!-- -->

[Extended File System (ext)](extended_file_system_(ext).md)
File system (family) introduced with [Linux](linux.md). Consist
of Ext, Ext2, Ext3, Ext4. Ext3 is a journaled version of Ext2 which
allows for speedy disk recovery after a crash.

<!-- -->

[Extent File System (EFS)](https://en.wikipedia.org/wiki/Extent_File_System)
SGI Extent File System, predecessor to XFS

<!-- -->

[FAT](fat.md)
Originally used by [MS-DOS](ms-dos.md). Includes [FAT12](fat.md),
[FAT16](fat.md) and [FAT32](fat.md).

<!-- -->

[FFS](ffs.md)
The **Fast File System** used by some BSD versions of
[UNIX](unix.md) and from which [UFS](ufs.md) was derived
supporting faster disk access and [symbolic
links](symbolic_link.md) like ffs.

<!-- -->

(Traditional) HFS
Hierarchical File System used by [Apple](apple.md) systems, it
has been succeed by [HFS+](hfs+.md).

<!-- -->

[JFS](jfs.md)
IBM's Journaled File System introduced with their flavor of UNIX (AIX)

<!-- -->

[New Technology File System (ntfs)](new_technology_file_system_(ntfs).md)
File system introduced by [Microsoft](microsoft.md) with
[Windows NT 4.0](windows.md).

<!-- -->

[reiserfs](reiserfs.md)
A journaling filesystem for Linux.

<!-- -->

[Resilient File System (refs)](resilient_file_system_(refs).md)
File system introduced by [Microsoft](microsoft.md) with
[Windows 8](windows.md).

<!-- -->

[UFS](ufs.md)
The **Unix File System**, introduced with [UNIX](unix.md).

<!-- -->

[XFS](xfs.md)
[SGI](sgi.md)’s high performance journaling file system that
originated on their [IRIX](irix.md) (flavor of
[UNIX](unix.md)) platform. XFS supports variable blocking sizes,
is extent based, and makes extensive use of [Btrees](btree.md)
to facilitate both performance and scalability. Additionally, support is
also provided for real-time environments.

<!-- -->

[YAFFS2](yaffs2.md)
Yet Another Flash File System is a filesystem which is used on Android
smartphones and was build for NAND and NOR flash.

<!-- -->

[Next3](next3.md)
An open-source file system based on the Ext3 file system, for the
purpose of supporting enterprise-grade snapshot capabilities.

# Cryptographic File Systems

**Cryptographic file systems,** also known as encrypted file systems,
encrypt information before it is stored on the media. Some of these file
systems store encrypted files directly. Others are better thought of as
device drivers, which are then used to store some of the file systems
discussed above.

[File Vault](file_vault.md)
A clever user interface to [Apple](apple.md)'s encrypted disk
images. Uses the ".sparseimage" extension on disk files.

<!-- -->

[CFS](cfs.md)
Matt Blaze's **Cryptographic File System** for [Unix](unix.md).

[Key Management in an Encrypting File
System](http://www.crypto.com/papers/cfskey.pdf), Matt Blaze, USENIX
Summer 1994 Technical Conference, Boston, MA, June 1994.

[A Cryptographic File System for
Unix](http://www.crypto.com/papers/cfs.pdf), Matt Blaze, Proceedings of
the First ACM Conference on Computer and Communications Security,
Fairfax, VA, November 1993.

<!-- -->

[Encrypted File System (efs)](windows_encrypted_file_system.md)
EFS is the Encrypted File System built into versions of Microsoft
Windows.

<!-- -->

[NCryptfs](ncryptfs.md)
[NCryptfs: A Secure and Convenient Cryptographic File
System](http://www.fsl.cs.sunysb.edu/docs/ncryptfs/ncryptfs.pdf),
Charles P. Wright, Michael C. Martino, and Erez Zadok, Stony Brook
University, USENIX 2003 Annual Technical Conference.

<!-- -->

[TCFS](tcfs.md)
**Transparent Cryptographic File System**.

<http://www.tcfs.it/>

<http://www.tcfs.it/docs/tcfs.ps>

<!-- -->

[SFS](sfs.md)
**Secure File System**.

<http://atrey.karlin.mff.cuni.cz/~rebel/sfs/>

<!-- -->

[ZFS](zfs.md)
<http://hub.opensolaris.org/bin/view/Project+zfs-crypto/WebHome>

See also [Full Disk Encryption](full_disk_encryption.md), which
are disk- or applicance-based cryptographic file systems.

# CD and DVD File Systems

Optical media use different file systems than hard disks or flash media,
primarily because of the write-once nature of most optical discs. Even
rewritable discs use different file systems because of the way that
rewritable media is managed. So while you will never find NTFS or FAT32
on an optical disc (though the exceptional nature of DVD-RAM must be
remembered -- you *can* create a FAT DVD-RAM), you will find the systems
listed below.

(Traditional) HFS and [HFS+](hfs+.md)
These file systems are defined by Apple and only limited support is available for them outside of the Macintosh world. These are the identical implementations for hard disk file systems on MacOS operating systems.

<!-- -->

[ISO 9660](iso_9660.md)
This is the most basic file system and the foundation for a number of
extensions which have been made to it. It was originally defined in 1989
and was an outgrowth of the previous HSG (High Sierra Group) definition
of a file system for CDs.

<!-- -->

[Joliet](joliet.md)
This is a Microsoft defined extension to ISO 9660 to support Unicode and
64-character file names. It was introduced with Windows 95. It has
gained some support for Linux and MacOS file systems but remains
something that is used primarily in the Windows environment.

<!-- -->

[Red Book](red_book.md)
The original definition of audio CDs was distributed with a red cover,
hence the term "Red Book". This is not properly a file system as it does
not define files, file names or any metadata. It is the definition by
which music discs are created.

<!-- -->

[Rock Ridge](rock_ridge.md)
Rock Ridge is a set of extensions based on the System Use Sharing
Protocol or SUSP definition. It is a method by which POSIX file
attributes, including very long file names, can be applied to optical
media. Today it is only really supported by Linux and other Unix-derived
operating systems.

<!-- -->

[UDF](udf.md)
UDF is the acronym for Universal Disk Format which was defined by the
Optical Storage Technology Association as an implementable subset of
ISO 13346. It is part of the definition for DVD Video and DVD Audio
discs as well as being used by a number of drag-and-drop disc writing
programs. It is supported for reading by Windows 98 and later versions
and is supported beginning with OS 9 on the Macintosh. Both Windows
Vista and Windows 7 can write discs using this as either a "mastered"
format with a static, read-only file system or as a "live" file system
which can be updated on both write-once and rewritable media.

# Distributed File Systems

**Distributed file systems,** also known as network file systems, allow
any number of remote clients to access one or more servers which store
the files. The client nodes do not have direct access to the underlying
block storage on the server(s), which are transparent to the clients and
may include facilities for replication or fault tolerance.

Ceph

OracleFS

AndrewFS

[HDFS](hadoop_distributed_file_system.md)
The GoogleFS clone, built from a cluster of data nodes.

<!-- -->

[NFS](network_file_system.md)
Originally from Sun, it is the standard in UNIX-based networks.

# Also see

- [Identifying file systems](identifying_file_systems.md)

# External Links

- <http://en.wikipedia.org/wiki/File_system>
- <http://en.wikipedia.org/wiki/List_of_file_systems>
- <http://en.wikipedia.org/wiki/Comparison_of_file_systems>
- <http://www.ctera.com/home/next3.html>
- <http://en.wikipedia.org/wiki/Next3>
- [Overwriting Hard Drive Data: The Great Wiping
  Controversy](http://www.springerlink.com/content/408263ql11460147/)
