# Conventional File Systems

[Apple File System (APFS)](Apple_File_System_(APFS) "wikilink")
A file system for [Apple](Apple "wikilink") systems optimized for
flash/SSD media.

<!-- -->

[Extended File System (Ext)](Extended_File_System_(Ext) "wikilink")
File system (family) introduced with [Linux](Linux "wikilink"). Consist
of Ext, Ext2, Ext3, Ext4. Ext3 is a journaled version of Ext2 which
allows for speedy disk recovery after a crash.

<!-- -->

[Extent File System (EFS)](https://en.wikipedia.org/wiki/Extent_File_System)
SGI Extent File System, predecessor to XFS

<!-- -->

[FAT](FAT "wikilink")
Originally used by [MS-DOS](MS-DOS "wikilink"). Includes
[FAT12](FAT12 "wikilink") (for floppy disks), [FAT16](FAT16 "wikilink")
and [FAT32](FAT32 "wikilink").

<!-- -->

[FFS](Ffs "wikilink")
The **Fast File System** used by some BSD versions of
[UNIX](UNIX "wikilink") and from which [UFS](UFS "wikilink") was derived
supporting faster disk access and [symbolic
links](symbolic_link "wikilink") like ffs.

<!-- -->

[HFS](HFS "wikilink")
Hierarchical File System used by [Apple](Apple "wikilink") systems, it
has been succeed by [HFS+](HFS+ "wikilink").

<!-- -->

[JFS](JFS "wikilink")
IBM's Journaled File System introduced with their flavor of UNIX (AIX)

<!-- -->

[New Technology File System (NTFS)](New_Technology_File_System_(NTFS) "wikilink")
File system introduced by [Microsoft](Microsoft "wikilink") with
[Windows NT 4.0](Windows "wikilink").

<!-- -->

[reiserfs](reiserfs "wikilink")
A journaling filesystem for Linux.

<!-- -->

[Resilient File System (ReFS)](Resilient_File_System_(ReFS) "wikilink")
File system introduced by [Microsoft](Microsoft "wikilink") with
[Windows 8](Windows "wikilink").

<!-- -->

[UFS](Ufs "wikilink")
The **Unix File System**, introduced with [UNIX](UNIX "wikilink").

<!-- -->

[XFS](XFS "wikilink")
[SGI](SGI "wikilink")’s high performance journaling file system that
originated on their [IRIX](IRIX "wikilink") (flavor of
[UNIX](UNIX "wikilink")) platform. XFS supports variable blocking sizes,
is extent based, and makes extensive use of [Btrees](Btree "wikilink")
to facilitate both performance and scalability. Additionally, support is
also provided for real-time environments.

<!-- -->

[YAFFS2](YAFFS2 "wikilink")
Yet Another Flash File System is a filesystem which is used on Android
smartphones and was build for NAND and NOR flash.

<!-- -->

[Next3](Next3 "wikilink")
An open-source file system based on the Ext3 file system, for the
purpose of supporting enterprise-grade snapshot capabilities.

# Cryptographic File Systems

**Cryptographic file systems,** also known as encrypted file systems,
encrypt information before it is stored on the media. Some of these file
systems store encrypted files directly. Others are better thought of as
device drivers, which are then used to store some of the file systems
discussed above.

[File Vault](File_Vault "wikilink")
A clever user interface to [Apple](Apple "wikilink")'s encrypted disk
images. Uses the ".sparseimage" extension on disk files.

<!-- -->

[CFS](CFS "wikilink")
Matt Blaze's **Cryptographic File System** for [Unix](Unix "wikilink").

[Key Management in an Encrypting File
System](http://www.crypto.com/papers/cfskey.pdf), Matt Blaze, USENIX
Summer 1994 Technical Conference, Boston, MA, June 1994.

[A Cryptographic File System for
Unix](http://www.crypto.com/papers/cfs.pdf), Matt Blaze, Proceedings of
the First ACM Conference on Computer and Communications Security,
Fairfax, VA, November 1993.

<!-- -->

[Encrypted File System (EFS)](Windows_Encrypted_File_System "wikilink")
EFS is the Encrypted File System built into versions of Microsoft
Windows.

<!-- -->

[NCryptfs](NCryptfs "wikilink")
[NCryptfs: A Secure and Convenient Cryptographic File
System](http://www.fsl.cs.sunysb.edu/docs/ncryptfs/ncryptfs.pdf),
Charles P. Wright, Michael C. Martino, and Erez Zadok, Stony Brook
University, USENIX 2003 Annual Technical Conference.

<!-- -->

[TCFS](TCFS "wikilink")
**Transparent Cryptographic File System**.

<http://www.tcfs.it/>

<http://www.tcfs.it/docs/tcfs.ps>

<!-- -->

[SFS](SFS "wikilink")
**Secure File System**.

<http://atrey.karlin.mff.cuni.cz/~rebel/sfs/>

<!-- -->

[ZFS](ZFS "wikilink")
<http://hub.opensolaris.org/bin/view/Project+zfs-crypto/WebHome>

See also [Full Disk Encryption](Full_Disk_Encryption "wikilink"), which
are disk- or applicance-based cryptographic file systems.

# CD and DVD File Systems

Optical media use different file systems than hard disks or flash media,
primarily because of the write-once nature of most optical discs. Even
rewritable discs use different file systems because of the way that
rewritable media is managed. So while you will never find NTFS or FAT32
on an optical disc (though the exceptional nature of DVD-RAM must be
remembered -- you *can* create a FAT DVD-RAM), you will find the systems
listed below.

[HFS](HFS "wikilink") and [HFS+](HFS+ "wikilink")
These file systems are defined by Apple and only limited support is available for them outside of the Macintosh world. These are the identical implementations for hard disk file systems on MacOS operating systems.

<!-- -->

[ISO 9660](ISO_9660 "wikilink")
This is the most basic file system and the foundation for a number of
extensions which have been made to it. It was originally defined in 1989
and was an outgrowth of the previous HSG (High Sierra Group) definition
of a file system for CDs.

<!-- -->

[Joliet](Joliet "wikilink")
This is a Microsoft defined extension to ISO 9660 to support Unicode and
64-character file names. It was introduced with Windows 95. It has
gained some support for Linux and MacOS file systems but remains
something that is used primarily in the Windows environment.

<!-- -->

[Red Book](Red_Book "wikilink")
The original definition of audio CDs was distributed with a red cover,
hence the term "Red Book". This is not properly a file system as it does
not define files, file names or any metadata. It is the definition by
which music discs are created.

<!-- -->

[Rock Ridge](Rock_Ridge "wikilink")
Rock Ridge is a set of extensions based on the System Use Sharing
Protocol or SUSP definition. It is a method by which POSIX file
attributes, including very long file names, can be applied to optical
media. Today it is only really supported by Linux and other Unix-derived
operating systems.

<!-- -->

[UDF](UDF "wikilink")
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

[HDFS](Hadoop_Distributed_File_System "wikilink")
The GoogleFS clone, built from a cluster of data nodes.

<!-- -->

[NFS](Network_File_System "wikilink")
Originally from Sun, it is the standard in UNIX-based networks.

# Also see

- [Identifying file systems](Identifying_file_systems "wikilink")

# External Links

- <http://en.wikipedia.org/wiki/File_system>
- <http://en.wikipedia.org/wiki/List_of_file_systems>
- <http://en.wikipedia.org/wiki/Comparison_of_file_systems>
- <http://www.ctera.com/home/next3.html>
- <http://en.wikipedia.org/wiki/Next3>
- [Overwriting Hard Drive Data: The Great Wiping
  Controversy](http://www.springerlink.com/content/408263ql11460147/)

[Category:Disk encryption](Category:Disk_encryption "wikilink")
[Category:File Systems](Category:File_Systems "wikilink")