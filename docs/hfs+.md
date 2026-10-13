---
tags:
  - File Systems
  - MacOS
---
HFS+, or Hierarchical File System Plus, is the file system designed by
[Apple](apple_inc.md) to supersede (classic) HFS.

HFS+ was first introduced with Mac OS 8.1, one of the biggest
differences was the lower allocation block size of 4 KiB (4096 bytes),
which increased performance and lowered fragmentation (See: Technical
Note TN1121). It also implemented Unicode (rather than Mac proprietary
encoding formats) for naming files. HFSX is a variant of HSF+ that is
case sensitive.

Mac OS X 10.6, dropped support for formatting or writing (classic) HFS
and macOS 10.15 can no longer read [(classic) HFS](https://en.wikipedia.org/wiki/Hierarchical_File_System).

## Features

There are structurally many differences between HFS and HFS+, which are
listed below (Also see: Technical Note TN1150).

| Feature | HFS | HFS Plus | Benefit/Comment |
| --- | --- | --- | --- |
| User visible name | Mac OS Standard | Mac OS Extended | |
| Number of allocation blocks | 16 bits worth | 32 bits worth | Radical decrease in disk space used on large volumes, and a larger number of files per volume. |
| Long file names | 31 characters | 255 characters | Obvious user benefit; also improves cross-platform compatibility |
| File name encoding | Mac OS encoding (such as MacRoman) | Unicode | Allows for international-friendly file names, including mixed script names |
| File/folder attributes | Support for fixed size attributes (FileInfo and ExtendedFileInfo) | Allows for future meta-data extensions | Future systems may use metadata for a richer Finder experience |
| OS startup support | System Folder ID | Also supports a dedicated startup file | May help non-Mac OS systems to boot from HFS Plus volumes |
| catalog node size | 512 bytes | 4 KiB (4096 bytes) | Maintains efficiency in the face of the other changes. (This larger catalog node size is due to the much longer file names [512 bytes as opposed to 32 bytes], and larger catalog records (because of more/larger fields)). |
| Maximum file size | 2<sup>31</sup> bytes | 2<sup>63</sup> bytes | Obvious user benefit, especially for multimedia content creators. |
| Hard links | Not supported | File only | |
| Symbolic links | Not supported | Directories and files | |

## File system metadata file entries

An HFS volume contains multiple special file entries:

1. Catalog file - Describes the folder and file hierarchy of the
   volume. It is organized as a "balanced tree" for fast and efficient
   searches
2. Extents overflow file - Additional extents (contiguous allocation
   blocks allocated to forks) are stored in a b-tree in this file
3. Allocation file - Specifies whether an allocation block is free
   (similar to \$Bitmap in NTFS). This is stored in a bitmap,
   specifying a free allocation block with a "clear bit" (introduced in
   HFS+)
4. Attributes file - Contains attribute information regarding files or
   folders (introduced in HFS+)
5. Startup file - Allows computers to boot that do have built in
   support for HFS+ file systems (introduced in HFS+)

The first 16 catalog node identifiers (CNIDs) are reserved for special
file system metadata file entries. Note that these file entries are not
full fledged files, like for example on other file systems like NTFS.
These file entries do not appear to have a corresponding entry in the
catalog file.

## Journaling

HFS+ also implements journaling, which allows fast recovery in the case
of a crash or power outage. According to Apple, "The purpose of the
journal is to ensure that when a group of related changes are being
made, that either all of those changes are actually made, or none of
them are made."

## Date and time values

In HFS+ date and time values are stored in an unsigned 32-bit integer
containing the number of seconds since January 1, 1904 at 00:00:00
(midnight) UTC (GMT). This is slightly different from HFS where the date
and time value are stored using the local time. The maximum
representable date is February 6, 2040 at 06:28:15 UTC (GMT). The date
values do not account for leap seconds. They do include a leap day in
every year that is evenly divisible by four. This is sufficient given
that the range of representable dates does not contain 1900 or 2100,
neither of which have leap days. Also see: [Technical Note TN1150 - HFS Plus Volume Format](http://web.archive.org/web/20220208191804/https://developer.apple.com/documentation/technotes)

Converting HFS/HFS+ date and time values with Python:

```python
import datetime

print datetime.datetime( 1904, 1, 1 ) + datetime.timedelta( seconds=0xCBDAF25B )
```

## Observations

Observed on Mac OS 10.15.7

HFS+ allows for the '/' character in file names. On Mac OS, Finder this
will be represented as a '/' but in Terminal it is replaced by ':'
seeing the same character is used as path segment separator. A file name
with a ':' created in Terminal will be shown as '/' in Finder. Finder
does not allow the creation of a file containing ':' in the name. A
symbolic link created in Terminal to a file with a ':' in name will not
convert the ':' character in the link target data. The Linux HFS+
implementation appears to apply a similar conversion logic as Terminal.

HFS+ stores U+2400 as U+0

## Also see

* [Apple File System (apfs)](apple_file_system_(apfs).md)

## External Links

* [Inside Macintosh: Files - Data Organization on Volumes](https://developer.apple.com/library/archive/documentation/mac/Files/Files-99.html),
  by Apple 1996
* Internet Archive Copy of: [Technical Note TN1121](http://web.archive.org/web/20090530120010/http://developer.apple.com/technotes/tn/tn1121.html)
* Internet Archive Copy of: [Technical Note TN1150: HFS plus volume format](http://web.archive.org/web/20220208191804/https://developer.apple.com/documentation/technotes)
* [Mac Forensics: Mac OS X and the HFS+ File System](http://cet4861.pbworks.com/w/file/fetch/71245694/mac.forensics.craiger-burke.IFIP.06.pdf)
  by P. Craiger, November 2005
* [Using the HFSD journal for deleted ﬁle recovery](https://dfrws.org/sites/default/files/session-files/2008_USA_pres-using_the_hfs_journal_for_deleted_file_recovery.pdf),
  by Aaron Burghardt, Adam Feldman, DRFWS 2008

## Tools

* [The Sleuth Kit](the_sleuth_kit.md) - partially supports HFS+/HSX, does
  not support [(classic) HFS](https://wiki.sleuthkit.org/HFS/)
* [HFSExplorer](http://www.catacombae.org/hfsexplorer/)
