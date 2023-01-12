---
tags:
  - File Systems
  - Windows
---
**FAT**, or File Allocation Table, is a [file
system](file_systems.md) that is designed to keep track of
allocation status of clusters on a [hard drive](hard_drive.md).
Developed in 1977 by [Microsoft](microsoft.md) Corporation, FAT
was originally intended to be a [file system](file_systems.md)
for the Microsoft Disk BASIC interpreter. FAT was quickly incorporated
into an early version of Tim Patterson's QDOS, which was a moniker for
"Quick and Dirty Operating System". [Microsoft](microsoft.md)
later purchased the rights to QDOS and released it under Microsoft
branding as PC-DOS and later, MS-DOS.

## Specification

FAT is described by Microsoft in [Microsoft Extensible Firmware
Initiative FAT32 File System Specification - FAT: General Overview of
On-Disk
Format](http://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/fatgen103.doc).
Despite the name, the document includes descriptions of FAT12 and FAT16.

Closely related standards are: ECMA 107 and ISO/EIC 9293, which only
cover FAT12 and FAT16, and also are somewhat more restricted than the
file system described by Microsoft's document.

## Structure

<table>
<tbody>
<tr class="odd">
<td><p>Boot sector</p></td>
<td><p>More reserved<br />
sectors (optional)</p></td>
<td><p>FAT #1</p></td>
<td><p>FAT #2</p></td>
<td><p>Root directory<br />
(FAT12/16 only)</p></td>
<td><p>Data region<br />
(rest of disk)</p></td>
</tr>
</tbody>
</table>

### Boot Record

When a computer is powered on, a POST (power-on self test) is performed,
and control is then transferred to the [Master boot
record](master_boot_record.md) ([MBR](mbr.md)). The
[MBR](mbr.md) is present no matter what file system is in use,
and contains information about how the storage device is logically
partitioned. When using a FAT file system, the [MBR](mbr.md)
hands off control of the computer to the Boot Record, which is the first
sector on the partition. The Boot Record, which occupies a reserved area
on the partition, contains executable code, in addition to information
such as an OEM identifier, number of FATs, media descriptor (type of
storage device), and information about the operating system to be
booted. Once the Boot Record code executes, control is handed off to the
operating system installed on that partition.

Note that ECMA 107 does not define the boot record signature 0x55, 0xaa
(or 0xaa55)

### FATs

The primary task of the File Alocation Tables are to keep track of the
allocation status of clusters, or logical groupings of sectors, on the
disk drive. There are four different possible FAT entries: allocated
(along with the address of the next cluster associated with the file),
unallocated, end of file, and bad sector.

In order to provide redundancy in case of data corruption, two FATs,
FAT1 and FAT2, are stored in the file system. FAT2 is a typically a
duplicate of FAT1. However, FAT mirroring can be disabled on a FAT32
drive, thus enabling any of the FATs to become the Primary FAT. This
possibly leaves FAT1 empty, which can be deceiving.

### Root Directory

The Root Directory, sometimes referred to as the Root Folder, contains
an entry for each file and directory stored in the file system. This
information includes the file name, starting cluster number, and file
size. This information is changed whenever a file is created or
subsequently modified. Root directory has a fixed size of 512 entries on
a hard disk and the size on a floppy disk depends. With FAT32 it can be
stored anywhere within the partition, although in previous versions it
is always located immediately following the FAT region.

### Data Area

The Boot Record, FATs, and Root Directory are collectively referred to
as the System Area. The remaining space on the logical drive is called
the Data Area, which is where files are actually stored. It should be
noted that when a file is deleted by the operating system, the data
stored in the Data Area remains intact until it is overwritten.

### Clusters

In order for FAT to manage files with satisfactory efficiency, and also
to increase maximum size of the volume, it groups sectors into larger
blocks referred to as clusters. A cluster is the smallest unit of disk
space that can be allocated to a file, which is why clusters are often
called allocation units. Each cluster can be used by one and only one
file (or directory). Only the "data area" is divided into clusters, the
rest of the partition is simply sectors. Cluster size is determined by
the size of the disk volume and every file must be allocated an integral
number of clusters. Cluster sizing has a significant impact on
performance and disk utilization. Larger cluster sizes result in more
wasted space because files are less likely to fill up an even number of
clusters.

The size of one cluster is specified in the Boot Record and can range
from a single sector (512 bytes) to 128 sectors (65536 bytes). The
sectors in a cluster are continuous, therefore each cluster is a
continuous block of space on the disk. Note that only one file can be
allocated to a cluster. Therefore if a 1KB file is placed within a 32KB
cluster there are 31KB of wasted space. The formula for determining
clusters in a partition is (# of Sectors in Partition) - (# of Sectors
per Fat \* 2) - (# of Reserved Sectors) ) / (# of Sectors per Cluster).

### Wasted Sectors

**Wasted Sectors** (a.k.a. **partition [slack](slack.md) are
a result of the number of data sectors not being evenly distributed by
the cluster size. It's made up of unused bytes left at the end of a
file. Also, if the partition as declared in the partition table is
larger than what is claimed in the Boot Record the volume can be said to
have wasted sectors. Small files on a hard drive are the reason for
wasted space and the bigger the hard drive the more wasted space there
is.

### FAT Entry Values


FAT12

0x000 (Free Cluster)
0x001 (Reserved Cluster)
0x002 - 0xFEF (Used cluster; value points to next cluster)
0xFF0 - 0xFF6 (Reserved values)
0xFF7 (Bad cluster)
0xFF8 - 0xFFF (Last cluster in file)

FAT16

0x0000 (Free Cluster)
0x0001 (Reserved Cluster)
0x0002 - 0xFFEF (Used cluster; value points to next cluster)
0xFFF0 - 0xFFF6 (Reserved values)
0xFFF7 (Bad cluster)
0xFFF8 - 0xFFFF (Last cluster in file)

FAT32

0x?0000000 (Free Cluster)
0x?0000001 (Reserved Cluster)
0x?0000002 - 0x?FFFFFEF (Used cluster; value points to next cluster)
0x?FFFFFF0 - 0x?FFFFFF6 (Reserved values)
0x?FFFFFF7 (Bad cluster)
0x?FFFFFF8 - 0x?FFFFFFF (Last cluster in file)

Note: FAT32 uses only 28 of 32 possible bits, the upper 4 bits should be
left alone. Typically these bits are zero, and are represented above by
a question mark (?).

## Versions

There are multiple variants of FAT in existence, the most common ones
are probably: FAT12, FAT16, and FAT32.

### FAT12

* FAT12 is a type of FAT that uses a 12 bit file allocation table entry.
* FAT12 can hold a max of 4,084 clusters (which is 2<sup>12</sup>
  clusters minus a few values that are reserved for values used in the
  FAT).
* It is used for floppy disks and hard drive partitions that are smaller
  than 16 MB.
* All 1.44 MB 3.5" floppy disks are formatted using FAT12.
* Cluster size that is used is between 0.5 KB to 4 KB.

### FAT16

* It is called FAT16 because all entries are 16 bit.
* FAT16 can hold a max of 65,524 addressable units
* It is used for small and moderate sized hard disk volumes.

### FAT32

FAT32 is the enhanced version of the FAT system implemented beginning
with Windows 95 OSR2, Windows 98, and Windows Me. Features include:

* Drives of up to 2 terabytes are supported
  ([windows](windows.md)
* Since FAT32 uses smaller clusters (of 4 kilobytes each), it uses hard
  drive space more efficiently. This is a 10 to 15 percent improvement
  over FAT or FAT16.
* The limitations of FAT or FAT 16 on the number of root folder entries
  have been eliminated. In FAT32, the root folder is an ordinary cluster
  chain, and can be located anywhere on the drive.
* File allocation mirroring can be disabled in FAT32. This allows a
  different copy of the file allocation table then the default to be
  active.

#### Limitations with [Windows](windows.md) 2000 & [Windows](windows.md) XP

* Clusters cannot be 64KB or larger.
* Cannot decrease cluster size that will result in the the FAT being
  larger than 16 MB minus 64KB in size.
* Cannot contain fewer than 65,527 clusters.
* Maximum of 32KB per cluster.
* *[Windows](windows.md) XP*: The Windows XP installation
  program will not allow a user to format a drive of more than 32GB
  using the FAT32 file system. Using the installation program, the only
  way to format a disk greater than 32GB in size is to use NTFS. A disk
  larger than 32GB in size *can* be formatted with FAT32 for use with
  Windows XP if the system is booted from a Windows 98 or Windows ME
  startup disk, and formatted using the tool that will be on the disk.

### exFAT (sometimes incorrectly called FAT64)

exFAT (also know as Extended File Allocation Table or exFAT) is
Microsoft's latest version of FAT and works with Windows Embedded CE
6.0, Windows XP/Server 2003 (with a KB patch, Vista/Server 2008 SP 1 &
Later, and Windows 7. Features include:

* Largest file size is 2<sup>64</sup> bytes (16 exabytes) vs. FAT32's
  maximum file size of 4GB.
* Has transaction support using Transaction-Safe Extended FAT File
  System (TexFAT). (Not released yet in Desktop/Server OS)
* Speeds up storage allocation processes by using free space bitmaps.
* Support UTC timestamps (Vista/Server 2008 SP1 does not support UTC,
  UTC support came out with SP2)
* Maximum Cluster size of 32MB (Fat32 is 32KB)
* Sector sizes from 512 bytes to 4096 bytes in size
* Maximum FAT supportable volume size of 128PB
* Maximum Subdirectory size of 256MB which can support up to over 2
  million files in a single subdirectory
* Uses a Bitmap for cluster allocation
* Supports File Permissions (Not released yet in Desktop/Server OS)
* Has been selected as the exclusive file system of the SDXC memory card
  by the SD Association

Although Microsoft has published some information on exFAT, there are
more technical specifications available from third parties. For example,
here is a [detailed presentation on
exFAT](https://paradigmsolutions.files.wordpress.com/2009/12/exfat-excerpt-1-4.pdf).

Another published technical paper that goes in the internals in great
detail is in the SANS Reading Room at: [Reverse Engineering the
Microsoft exFAT File
System](https://www.sans.org/white-papers/33274/)

### Comparison of FAT Versions

See the table at <https://en.wikipedia.org/wiki/File_Allocation_Table>
for more detailed information about the various versions of FAT.

## Uses

Due to its low cost, mobility, and non-volatile nature, flash memory has
quickly become the choice medium for storing and transferring data in
consumer electronic devices. The majority of flash memory storage is
formatted using the FAT file system. In addition, FAT is also frequently
used in electronic devices with miniature hard drives.

Examples of devices in which FAT is utilized include:

* [USB](usb.md) thumb drives
* Digital cameras
* Digital camcorders
* Portable audio and video players
* Multifunction [printers](printers.md)
* Electronic photo frames
* Electronic musical instruments
* Standard televisions
* [PDAs](pdas.md)

## Data Recovery

Recovering directory entries from FAT filesystems as part of [recovering
deleted data](recovering_deleted_data.md) can be accomplished by
looking for entries that begin with a sigma 0xe5. When a file or
directory is deleted under a FAT filesystem, the first character of its
name is changed to sigma. The remainder of the directory entry
information remains intact.

The pointers are also changed to zero for each cluster used by the file.
Recovery tools look at the FAT to find the entry for the file. The
location of the starting cluster will still be in the directory file. It
is not deleted or modified. The tool will go straight to that cluster
and try to recover the file using the file size to determine the number
of clusters to recover. Some tools will go to the starting cluster and
recover the next "X" number of clusters needed for the specific file
size. However, this tool is not ideal. An ideal tool will locate "X"
number of available clusters. Since files are most often fragmented,
this will be a more precise way to recover the file.

An issue arises when two files in the same row of clusters are deleted.
If the clusters are not in sequential order, the tool will automatically
receive "X" number of clusters. However, because the file was
fragmented, it's most likely that all the clusters obtained will not all
contain data for that file. If these two deleted files are in the same
row of clusters, it is highly unlikely the file can be recovered.

## File [Slack](slack.md)

File [slack](slack.md) is data that starts from the end of the
file written and continues to the end of the sectors designated to the
file. There are two types of file [slack](slack.md), RAM slack
and Residual [slack](slack.md). RAM slack starts from the end of
the file and goes to the end of that sector. Residual slack then starts
at the next sector and goes to the end of the cluster allocated for the
file. File slack is a helpful tool when analyzing a hard drive because
the old data that is not overwritten by the new file is still in tact.
Go to <https://www.pcguide.com/hdd/> for
examples.

<table border="1" cellspacing="2" bordercolor="#000000" cellpadding="4" width="468" bordercolorlight="#C0C0C0">
<tr>
<td width="101" bgcolor="#808080">

<font size="2"><b>

<center>

Cluster

</center>

</b></font>

</td>
<td width="177" bgcolor="#808080">

<font size="2"><b>

<center>

Sample Slack Space,

`   50% Cluster Slack Per File`

</center>

</b></font>

</td>
<td width="178" bgcolor="#808080">

<font size="2"><b>

<center>

Sample Slack Space,

`   67% Cluster Slack Per File`

</center>

</b></font>

</td>
</tr>
<tr>
<td width="101" bgcolor="#C0C0C0">

<font size="2"><b>

<center>

2 kiB

</center>

</b></font>

</td>
<td width="177">

<font size="2">

<center>

17 MB

</center>

</font>

</td>
<td width="178">

<font size="2">

<center>

22 MB

</center>

</font>

</td>
</tr>
<tr>
<td width="101" bgcolor="#C0C0C0">

<font size="2"><b>

<center>

4 kiB

</center>

</b></font>

</td>
<td width="177">

<font size="2">

<center>

33 MB

</center>

</font>

</td>
<td width="178">

<font size="2">

<center>

44 MB

</center>

</font>

</td>
</tr>
<tr>
<td width="101" bgcolor="#C0C0C0">

<font size="2"><b>

<center>

8 kiB

</center>

</b></font>

</td>
<td width="177">

<font size="2">

<center>

66 MB

</center>

</font>

</td>
<td width="178">

<font size="2">

<center>

89 MB

</center>

</font>

</td>
</tr>
<tr>
<td width="101" bgcolor="#C0C0C0">

<font size="2"><b>

<center>

16 kiB

</center>

</b></font>

</td>
<td width="177">

<font size="2">

<center>

133 MB

</center>

</font>

</td>
<td width="178">

<font size="2">

<center>

177 MB

</center>

</font>

</td>
</tr>
<tr>
<td width="101" bgcolor="#C0C0C0">

<font size="2"><b>

<center>

32 kiB

</center>

</b></font>

</td>
<td width="177">

<font size="2">

<center>

265 MB

</center>

</font>

</td>
<td width="178">

<font size="2">

<center>

354 MB

</center>

</font>

</td>
</tr>
</table>

The diagram above demonstrates the larger the cluster size used, the
more disk space is wasted due to slack. This suggests it is better to
use smaller cluster sizes whenever possible.

## FAT Advantages

* Files available to multiple operating systems on the same computer
* Easier to switch from FAT to [NTFS](ntfs.md) than vice versa
* Performs faster on smaller volumes (\< 10GB)
* Does not index files, which causes slightly higher performance
* Performs better with small cache sizes (\< 96MB)
* More space-efficient on small volumes (\< 4GB)
* Performs better with slow disks (\< 5400RPM)

## FAT Disadvantages

* FAT has a fixed maximum number of clusters per partition, which means
  as the hard disk gets bigger the size of each cluster must increase,
  creating more slack space
* Doesn't natively support many abilities of [NTFS](ntfs.md)
  such as on-the-fly compression, [encryption](encryption.md),
  or advanced security using access control lists
* [NTFS](ntfs.md) recommended by
  [Microsoft](microsoft.md) for volumes larger than 32GB
* FAT slows down as the number of files on the disk increases
* FAT usually fragments files more
* FAT does not allow for indexing of files for faster searching
* FAT does not support user quotas
* FAT has minimal security features including no access control list
  (ACL) capability.

## FAT date and time values

Python code to convert a FAT date and time value into a Python datetime
object.

    import datetime

    def FromFatDateTime(fat_date_time):
      """Converts a FAT date and time into a Python datetime object.

      FAT date time is mainly used in DOS/Windows file formats and FAT.

      The FAT date and time is a 32-bit value containing two 16-bit values:
        * The date (lower 16-bit).
          * bits 0 - 4:  day of month, where 1 represents the first day
          * bits 5 - 8:  month of year, where 1 represent January
          * bits 9 - 15: year since 1980
        * The time of day (upper 16-bit).
          * bits 0 - 4: seconds (in 2 second intervals)
          * bits 5 - 10: minutes
          * bits 11 - 15: hours

      Args:
        fat_date_time: The 32-bit FAT date time.

      Returns:
        A datetime object containing the date and time or None.
      """
      day_of_month = (fat_date_time & 0x1f)
      month = ((fat_date_time >> 5) & 0x0f)
      year = (fat_date_time >> 9) & 0x7f

      if day_of_month < 0 or day_of_month > 30 or month < 0 or month > 11:
        return None

      fat_date_time >>= 16

      seconds = (fat_date_time & 0x1f) * 2
      minutes = (fat_date_time >> 5) & 0x3f
      hours = (fat_date_time >> 11) & 0x1f

      if hours > 23 or minutes > 59 or seconds > 59:
        return None

      return datetime.datetime(
          1980 + year, month, day_of_month, hours, minutes, seconds)

## External links

* [Wikipedia: File Allocation Table](https://en.wikipedia.org/wiki/File_Allocation_Table)
* [Wikipedia: Design of the FAT file system](https://en.wikipedia.org/wiki/Design_of_the_FAT_file_system)
* <http://www.ntfs.com>
* <http://www.ntfs.com/ntfs_vs_fat.htm>
* <http://support.microsoft.com/kb/q154997/#XSLTH3126121123120121120120>
* <http://www.dewassoc.com/kbase/hard_drives/boot_sector.htm>
* <http://home.teleport.com/~brainy/fat32.htm>
* <http://home.no.net/tkos/info/fat.html>
* <http://web.ukonline.co.uk/cook/fat32.htm>
* <http://www.ntfs.com/fat-systems.htm>
* <http://support.microsoft.com/kb/q140418>

### Format documentation

* [ECMA-107: Volume and File Structure of Disk Cartridges for Information Interchange](https://www.ecma-international.org/wp-content/uploads/ECMA-107_2nd_edition_june_1995.pdf),
  2nd Edition - June 1995
* [Microsoft Extensible Firmware Initiative FAT32 File System Specification - FAT: General Overview of On-Disk Format](http://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/fatgen103.doc),
  by Microsoft, December 6, 2000
* [An overview of FAT12](https://www.eit.lth.se/fileadmin/eit/courses/eitn50/Literature/fat12_description.pdf),
  by Archana Chidanandan, 2004
* [exFAT file system specification](https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification),
  by Microsoft, 2019-08-27

### Volume serial number

* [Volume Serial Numbers and Format Date/Time Verification](https://www.digital-detective.net/documents/Volume%20Serial%20Numbers.pdf),
  by Craig Wilson, October 2003 (updated June 2005)

### ExFAT

* [Wikipedia: ExFAT](https://en.wikipedia.org/wiki/ExFAT)
* [exFAT File System](http://www.active-undelete.com/xfat_volume.htm)
* [Reverse Engineering the Microsoft exFAT File System](https://www.sans.org/white-papers/33274/),
  by Robert Shullich, December 1, 2009
* [Extended FAT file system](https://paradigmsolutions.files.wordpress.com/2009/12/exfat-excerpt-1-4.pdf),
  by Jeff Hamm, December 2009
* [Demystifying the Microsoft Extended FAT File System (exFAT)](https://www.slideshare.net/overcertified/demystifying-the-microsoft-extended-fat-file-system-exfat),
  by Robert Shullich, September 20, 2010
* [Windows Phone 7 : Implications For Digital Forensic Investigators](http://aut.researchgateway.ac.nz/bitstream/handle/10292/4123/LeY.pdf),
  by Yung Anh Le, 2012

### textFAT

* [TexFAT Padding Directory Entry](http://www.ntfs.com/exfat-textFAT-padding.htm)

## Tools

### exFAT

* [Open Source exFAT file system implementation](https://github.com/relan/exfat)
